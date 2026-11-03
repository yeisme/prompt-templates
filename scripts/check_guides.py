#!/usr/bin/env python3
"""Replay typed cases through fixed argv operations. Markdown is never executed."""
import argparse
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
import threading
import uuid
from urllib.parse import urlparse

from tutorial_cases import load_case

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--registry', default='template-registry')
    args = parser.parse_args()
    binary = str(Path(args.registry).resolve()) if '/' in args.registry else args.registry
    run = ROOT / 'temp/integration-test-runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-scenarios-' + uuid.uuid4().hex[:8])
    (run / 'artifacts').mkdir(parents=True)
    (run / 'command.txt').write_text(shlex.join(['python3', 'scripts/check_guides.py', *sys.argv[1:]]) + '\n')
    rows, failures = [], []
    journeys = []
    calls = [0]

    class DenyBackend(BaseHTTPRequestHandler):
        def do_POST(self):
            calls[0] += 1
            self.send_response(503)
            self.end_headers()
        def log_message(self, *_):
            pass

    server = ThreadingHTTPServer(('127.0.0.1', 0), DenyBackend)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    code = 0
    try:
        with tempfile.TemporaryDirectory(prefix='template-scenarios-') as tmp:
            work = Path(tmp)
            env = {**os.environ, 'TEMPLATE_REGISTRY_CONFIG_ROOT': str(work / 'config')}

            def invoke(project, command, payload=None, allow_failure=False):
                argv = [binary, *command, '--json']
                if payload is not None:
                    argv.append('--stdin')
                result = subprocess.run(argv, input=None if payload is None else json.dumps(payload, ensure_ascii=False), cwd=project, env=env, capture_output=True, text=True, timeout=120)
                try:
                    response = json.loads(result.stdout)
                except ValueError:
                    raise RuntimeError('CLI_OUTPUT_INVALID')
                if (result.returncode or response.get('status') == 'failed') and not allow_failure:
                    raise RuntimeError(response.get('error', {}).get('code', 'CLI_FAILED'))
                return response

            def call(project, *command, payload=None):
                return invoke(project, list(command), payload).get('data')

            call(work, 'prompt', 'repository', 'add', '--id', 'official', '--source', ROOT.as_uri(), '--trust', 'official')
            call(work, 'prompt', 'repository', 'sync', '--id', 'official')
            call(work, 'prompt', 'analysis', 'configure', payload={'endpoint': f'http://127.0.0.1:{server.server_port}/v1/chat/completions', 'model': 'synthetic-deny-backend'})
            for metadata in sorted(ROOT.glob('solutions/*/*/solution.json')):
                solution = json.loads(metadata.read_text())
                folder = metadata.parent
                guide = folder / 'docs/README.md'
                document = guide.read_text()
                roles = [r for r in solution['templates'] if r['locale'] == 'en'] or solution['templates']
                for role in roles:
                    identity = solution['package_id'] + '/' + solution['id'] + ':' + role['role']
                    project = work / str(len(rows))
                    project.mkdir()
                    ref = f"promptrepo://official/{solution['package_id']}/{solution['id']}@{solution['version']}?locale={role['locale']}"
                    row = {'template': identity, 'guide': False, 'engineering': 'not_applicable', 'scenario': 'not_applicable', 'human_review': 'pending'}
                    try:
                        view = call(project, 'prompt', 'guide', '--ref', ref, '--role', role['role'], '--output', 'guide.md')
                        expected = 'sha256:' + hashlib.sha256(guide.read_bytes()).hexdigest()
                        if view['digest'] != expected or (project / 'guide.md').read_bytes() != guide.read_bytes():
                            raise RuntimeError('GUIDE_MISMATCH')
                        for section in ('overview', 'inputs'):
                            part = call(project, 'prompt', 'guide', '--ref', ref, '--role', role['role'], '--section', section, '--output', section + '.md')
                            body = (project / (section + '.md')).read_bytes()
                            if part['digest'] != expected or part['content_digest'] != 'sha256:' + hashlib.sha256(body).hexdigest() or len(body) >= guide.stat().st_size:
                                raise RuntimeError('GUIDE_SECTION_MISMATCH')
                        row['guide'] = True
                        if role['locale'] != 'en':
                            rows.append(row)
                            continue
                        call(project, 'tutorial', 'case', 'validate', '--repository', str(ROOT), '--package', solution['package_id'], '--id', solution['id'], '--role', role['role'])
                        cases = json.loads((folder / 'tutorials' / f"{role['role']}.en.json").read_text())
                        positive = next(c for c in cases['cases'] if c['kind'] == 'valid')
                        values, output = load_case(folder, role, cases, positive)
                        section = document.split(f"## 角色 `{role['role']}`", 1)[1].split('\n## ', 1)[0]
                        snippet = re.search(r"<<'INPUT'\n(.*?)\nINPUT", section, re.S)
                        if snippet is None or {k.removeprefix('main.'): v['value'] for k, v in json.loads(snippet.group(1))['fields'].items()} != values:
                            raise RuntimeError('DOCUMENTED_INPUT_DRIFT')
                        for operation in ('session create', 'source import', 'session update', 'session confirm', 'compile', 'export', 'bundle verify'):
                            if 'template-registry prompt ' + operation not in section:
                                raise RuntimeError('DOCUMENTED_OPERATION_MISSING')
                        state = call(project, 'prompt', 'session', 'create', payload={'ref': ref, 'role': role['role'], 'goal': 'Synthetic scenario: ' + solution['id']})
                        sid = state['id']
                        state = call(project, 'prompt', 'source', 'import', payload={'session_id': sid, 'expected_revision': state['revision'], 'id': 'tutorial-source', 'text': cases['source_text']})
                        fields = {}
                        for name, value in values.items():
                            factual = name in ('source_text', 'meeting_record', 'sources', 'source_material') and value == cases['source_text']
                            fields['main.' + name] = {'value': value, 'kind': 'fact' if factual else 'user', 'source': 'tutorial-source' if factual else 'user'}
                        state = call(project, 'prompt', 'session', 'update', payload={'session_id': sid, 'expected_revision': state['revision'], 'fields': fields})
                        before = state['revision']
                        same = call(project, 'prompt', 'session', 'update', payload={'session_id': sid, 'expected_revision': before, 'fields': fields})
                        if same['revision'] != before:
                            raise RuntimeError('UNCHANGED_INPUT_INVALIDATED')
                        state = call(project, 'prompt', 'session', 'confirm', payload={'session_id': sid, 'expected_revision': before, 'goal': True, 'fields': list(fields), 'sources': ['tutorial-source'], 'decision_ref': 'synthetic-reviewed-case'})
                        compiled = call(project, 'prompt', 'compile', payload={'session_id': sid, 'expected_revision': state['revision']})
                        exported = call(project, 'prompt', 'export', payload={'compile_id': compiled['id'], 'output': 'result'})
                        call(project, 'prompt', 'bundle', 'verify', '--path', 'result')
                        resumed = call(project, 'prompt', 'session', 'resume', '--session', sid)
                        if resumed['id'] != sid or resumed['revision'] != state['revision']:
                            raise RuntimeError('RESUME_IDENTITY_CHANGED')
                        row['engineering'] = 'passed'
                        row['scenario'] = 'input_contract_and_authored_expectations_validated'
                        row['negative_cases'] = sum(c['kind'] == 'invalid' for c in cases['cases'])
                        row['output_schema'] = 'fixture_schema_verified' if positive.get('fixture_case_id') else 'authored_review_checks_pending_human'
                    except Exception as error:
                        row['error'] = str(error) if isinstance(error, RuntimeError) else type(error).__name__
                        failures.append(identity)
                        code = 1
                    rows.append(row)
                    print(json.dumps(row), flush=True)
            for recipe_path in [ROOT / 'recipes/research-summary-en.json', ROOT / 'solutions/video/product-promo-shot-design-beta/examples/video-shotcraft-product-promo.recipe.json']:
                recipe = json.loads(recipe_path.read_text())
                project = work / ('workflow-' + recipe['id'])
                project.mkdir()
                state = call(project, 'prompt', 'session', 'create', payload={'goal': 'Synthetic staged task', 'recipe': recipe})
                sid = state['id']
                fields, sources, expected_outputs = {}, {}, {}
                for step in recipe['steps']:
                    address = urlparse(step['ref'])
                    package, identity = address.path.strip('/').split('/')
                    solution_id = identity.split('@')[0]
                    folder = ROOT / 'solutions' / package / solution_id
                    role = {'role': step.get('role', 'main'), 'locale': 'en'}
                    cases = json.loads((folder / 'tutorials' / (role['role'] + '.en.json')).read_text())
                    positive = next(c for c in cases['cases'] if c['kind'] == 'valid')
                    values, output = load_case(folder, role, cases, positive)
                    expected_outputs[step['id']] = output
                    for field, value in values.items():
                        binding = step.get('bindings', {}).get(field, {})
                        if binding.get('kind') == 'step_output':
                            continue
                        if binding.get('kind') == 'source':
                            sources[binding['ref']] = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
                            continue
                        key = binding['ref'] if binding.get('kind') == 'field' else step['id'] + '.' + field
                        fields.setdefault(key, {'value': value, 'kind': 'user', 'source': 'user'})
                for source_id, text in sources.items():
                    state = call(project, 'prompt', 'source', 'import', payload={'session_id': sid, 'expected_revision': state['revision'], 'id': source_id, 'text': text})
                state = call(project, 'prompt', 'session', 'update', payload={'session_id': sid, 'expected_revision': state['revision'], 'fields': fields})
                call(project, 'prompt', 'session', 'read', payload={'session_id': sid, 'resource': 'confirmation', 'output': 'confirmation.json'})
                state = call(project, 'prompt', 'session', 'confirm', payload={'session_id': sid, 'expected_revision': state['revision'], 'goal': True, 'fields': list(fields), 'sources': list(sources), 'decision_ref': 'synthetic-staged-user-answer'})
                first = recipe['steps'][0]['id']
                partial = call(project, 'prompt', 'compile', payload={'session_id': sid, 'expected_revision': state['revision']})
                if not partial.get('delivery', {}).get('waiting_steps'):
                    raise RuntimeError('UPSTREAM_RESULT_NOT_REQUIRED')
                resumed = call(project, 'prompt', 'session', 'resume', '--session', sid)
                if resumed['id'] != sid:
                    raise RuntimeError('WORKFLOW_RESUME_CHANGED_IDENTITY')
                # This is a supplied synthetic upstream RESULT, not the upstream prompt.
                actual = expected_outputs[first]
                state = call(project, 'prompt', 'source', 'import', payload={'session_id': sid, 'expected_revision': state['revision'], 'id': 'upstream-result', 'step_output': first, 'text': actual if isinstance(actual, str) else json.dumps(actual, ensure_ascii=False)})
                state = call(project, 'prompt', 'session', 'confirm', payload={'session_id': sid, 'expected_revision': state['revision'], 'sources': ['upstream-result'], 'decision_ref': 'synthetic-upstream-review'})
                complete = call(project, 'prompt', 'compile', payload={'session_id': sid, 'expected_revision': state['revision']})
                if complete.get('delivery', {}).get('waiting_steps'):
                    raise RuntimeError('UPSTREAM_RESULT_NOT_BOUND')
                call(project, 'prompt', 'export', payload={'compile_id': complete['id'], 'output': 'result'})
                call(project, 'prompt', 'bundle', 'verify', '--path', 'result')
                changed = 'question' if first == 'research' else 'brief.audience_and_outcome'
                stale_revision = state['revision']
                state = call(project, 'prompt', 'session', 'update', payload={'session_id': sid, 'expected_revision': stale_revision, 'fields': {changed: {'value': fields[changed]['value'] + ' (revised)', 'kind': 'user', 'source': 'user'}}})
                if not any(item.get('kind') == 'step_output' for item in state.get('agenda', [])):
                    raise RuntimeError('DOWNSTREAM_OUTPUT_NOT_INVALIDATED')
                conflict = invoke(project, ['prompt', 'session', 'update'], {'session_id': sid, 'expected_revision': stale_revision, 'fields': fields}, allow_failure=True)
                if conflict.get('error', {}).get('code') != 'REVISION_CONFLICT':
                    raise RuntimeError('REVISION_CONFLICT_NOT_PRESERVED')
                journeys.append({'recipe': recipe['id'], 'state': 'passed', 'upstream_result': 'supplied_synthetic_fixture', 'resume_identity_preserved': True, 'downstream_invalidation': True})
            if calls[0] != 0:
                failures.append('UNEXPECTED_ANALYSIS_REQUEST')
                code = 1
    except Exception as error:
        failures.append(str(error) if isinstance(error, RuntimeError) else type(error).__name__)
        code = 1
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
        if calls[0] != 0:
            code = 1
            if 'UNEXPECTED_ANALYSIS_REQUEST' not in failures:
                failures.append('UNEXPECTED_ANALYSIS_REQUEST')
        environment = {'data': 'synthetic', 'isolated_project': True, 'analysis_backend': 'local-deny-stub', 'observed_analysis_requests': calls[0], 'external_provider_verification': 'not_run'}
        (run / 'env.json').write_text(json.dumps(environment, indent=2) + '\n')
        (run / 'stdout.log').write_text('\n'.join(json.dumps(row) for row in rows) + '\n')
        (run / 'stderr.log').write_text('\n'.join(failures) + '\n')
        summary = {'status': 'failed' if code else 'passed', 'roles': len(rows), 'compiled': sum(r['engineering'] == 'passed' for r in rows), 'negative_cases': sum(r.get('negative_cases', 0) for r in rows), 'failed': failures, **environment, 'human_review': 'pending', 'workflows': journeys}
        (run / 'artifacts/workflows.json').write_text(json.dumps(journeys, indent=2) + '\n')
        (run / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
        print(json.dumps({'summary': summary, 'evidence': str(run.relative_to(ROOT))}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
