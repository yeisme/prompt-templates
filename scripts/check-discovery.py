#!/usr/bin/env python3
"""Audit official source/index consistency and save redacted count evidence."""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--cli', default='template-registry')
parser.add_argument('--expected-solutions', type=int)
parser.add_argument('--expected-documents', type=int)
args = parser.parse_args()
root = pathlib.Path(__file__).resolve().parents[1]
run_id = 'integration-' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
evidence = root / 'temp' / 'integration-test-runs' / run_id
(evidence / 'artifacts').mkdir(parents=True)
command = [args.cli, 'catalog', 'audit', '--repository', str(root), '--json']
result = subprocess.run(command, capture_output=True, text=True)
catalog = json.loads((root / 'catalog.json').read_text())
solutions = catalog['solutions']
counts = {'solutions': len(solutions), 'roles': sum(len({t['role'] for t in s['templates']}) for s in solutions), 'documents': sum(len(s['templates']) for s in solutions)}
counts['image_documents'] = sum('image' in a.get('media', []) for a in catalog.get('discovery', []))
counts['image_solutions'] = len({(a['package_id'], a['solution_id']) for a in catalog.get('discovery', []) if 'image' in a.get('media', [])})
code = result.returncode
if args.expected_solutions is not None and counts['solutions'] != args.expected_solutions:
    code = 1
if args.expected_documents is not None and counts['documents'] != args.expected_documents:
    code = 1
(evidence / 'command.txt').write_text('template-registry catalog audit --repository . --json\n')
(evidence / 'stdout.log').write_text(result.stdout.replace(str(root), '<repository>'))
(evidence / 'stderr.log').write_text(result.stderr.replace(str(root), '<repository>'))
(evidence / 'env.json').write_text(json.dumps({'provider_calls': False, 'network': False}) + '\n')
summary = {'schema_version': 'yeisme.integration_test_evidence.v1', 'run_id': run_id, 'status': 'passed' if code == 0 else 'failed', 'exit_code': code, 'command': ['template-registry', 'catalog', 'audit'], 'redaction': {'enabled': True}, 'counts': counts, 'content_digest': catalog['digest']}
(evidence / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(counts))
print('Evidence: ' + str(evidence.relative_to(root)))
sys.exit(code)
