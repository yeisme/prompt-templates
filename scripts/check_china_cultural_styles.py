#!/usr/bin/env python3
"""Check cultural templates through provider-free Registry sessions; redact evidence."""
import argparse
import hashlib
import json
import os
import re
import runpy
import shlex
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

AUTHOR = runpy.run_path(str(Path(__file__).with_name('author_china_cultural_styles.py')))
ENTRIES, ROOT, VERSION = (AUTHOR[name] for name in ('ENTRIES', 'ROOT', 'VERSION'))

VARIABLE = re.compile(r'\{\{\s*([a-z_]+)\s*\}\}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--registry', required=True)
    args = parser.parse_args()
    binary = str(Path(args.registry).resolve())
    run = ROOT / 'temp/integration-test-runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + '-china-styles-' + uuid.uuid4().hex[:8])
    (run / 'artifacts').mkdir(parents=True)
    operations = []
    completed = []
    failure = ''
    code = 0
    with tempfile.TemporaryDirectory(prefix='china-style-check-') as workspace:
        project = str(Path(workspace) / 'project')
        env = {**os.environ, 'TEMPLATE_REGISTRY_CONFIG_ROOT': str(Path(workspace) / 'config')}

        def call(name, payload, reject=False):
            result = subprocess.run([binary, 'prompt', *name.split(), '--project', project, '--stdin', '--json'],
                                    input=json.dumps(payload), capture_output=True, text=True, env=env)
            try:
                response = json.loads(result.stdout)
            except ValueError as exc:
                raise RuntimeError('Registry returned invalid JSON') from exc
            success = result.returncode == 0 and response.get('status') in {'success', 'partial'}
            matched = success != reject
            operations.append({'operation': name, 'expected_rejection': reject, 'matched': matched})
            if not matched:
                raise RuntimeError('Unexpected Registry outcome: ' + name)
            return response.get('data', {})

        try:
            catalog = json.loads((ROOT / 'catalog.json').read_text())
            catalog_ids = {s['id'] for s in catalog['solutions']}
            call('repository add', {'id': 'official', 'source': ROOT.resolve().as_uri(), 'trust': 'user_trusted'})
            call('repository sync', {'id': 'official'})
            for row in ENTRIES:
                sid = row[0] + '-beta'
                folder = ROOT / 'solutions/image' / sid
                en = (folder / 'prompts/main.en.md').read_text()
                zh = (folder / 'docs/template-zh-CN.md').read_text()
                contract = json.loads((folder / 'contracts/main.en.json').read_text())
                metadata = json.loads((folder / 'solution.json').read_text())
                assert sid in catalog_ids
                assert set(VARIABLE.findall(en)) == set(VARIABLE.findall(zh)) == {i['name'] for i in contract['inputs']}
                assert [t['locale'] for t in metadata['templates']] == ['en']
                assert metadata['rights'] == 'internal' and metadata['maturity'] == 'exploratory'
                assert contract['template_digest'] == 'sha256:' + hashlib.sha256(en.encode()).hexdigest()
                ref = f'promptrepo://official/image/{sid}@{VERSION}?locale=en'
                call('inspect', {'ref': ref, 'role': 'main'})
                call('session create', {'ref': ref.replace('locale=en', 'locale=zh-CN'), 'role': 'main', 'goal': 'Synthetic locale rejection'}, True)
                session = call('session create', {'ref': ref, 'role': 'main', 'goal': 'Synthetic cultural-template validation'})
                call('compile', {'session_id': session['id'], 'expected_revision': session['revision']}, True)
                for n, medium in enumerate(['contemporary painting', 'documentary-style illustration']):
                    session = call('session update', {'session_id': session['id'], 'expected_revision': session['revision'],
                                   'fields': {'main.medium_clause': {'value': medium, 'kind': 'user', 'source': 'user', 'confirmed': False}}})
                    call('compile', {'session_id': session['id'], 'expected_revision': session['revision']}, True)
                    session = call('session confirm', {'session_id': session['id'], 'expected_revision': session['revision'],
                                   'goal': True, 'fields': ['main.medium_clause'], 'decision_ref': 'synthetic-template-check'})
                    compiled = call('compile', {'session_id': session['id'], 'expected_revision': session['revision']})
                    assert compiled.get('provider_calls') == 0
                    output = str(Path(project) / (sid + '-' + str(n)))
                    call('export', {'compile_id': compiled['id'], 'output': output})
                    call('bundle verify', {'path': output})
                    bodies = list((Path(output) / 'prompts').glob('*.txt'))
                    assert bodies, 'No exported prompt'
                    body = '\n'.join(p.read_text() for p in bodies)
                    assert not VARIABLE.search(body), 'Unresolved variables'
                    assert medium in body and row[4] in body, 'Lost binding or local scope'
                    if n == 1:
                        assert 'Medium: contemporary painting' not in body, 'Stale medium binding'
                completed.append(sid)
        except Exception as exc:
            code = 1
            # Do not echo tool payloads, prompt bodies, input values or environment values.
            failure = type(exc).__name__
        finally:
            summary = {'passed': code == 0, 'completed_count': len(completed), 'expected_count': len(ENTRIES),
                       'completed_ids': completed, 'operations': operations, 'failure_type': failure,
                       'provider_calls': 0, 'source_verification': 'not_performed', 'image_generation': 'not_performed'}
            (run / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
            (run / 'command.txt').write_text(shlex.join(['python3', 'scripts/check_china_cultural_styles.py', *sys.argv[1:]]) + '\n')
            (run / 'stdout.log').write_text(f'completed={len(completed)} expected=20 passed={code == 0}\n')
            (run / 'stderr.log').write_text(f'failure_type={failure}\n' if failure else '')
            (run / 'env.json').write_text(json.dumps({'isolated_config': True, 'python': sys.version.split()[0], 'network_generation': False}) + '\n')
    print(f'completed={len(completed)} passed={code == 0} evidence={run.relative_to(ROOT)}')
    return code


if __name__ == '__main__':
    sys.exit(main())
