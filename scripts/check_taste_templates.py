#!/usr/bin/env python3
"""Validate Taste output schemas against positive and negative fixtures."""
import json,pathlib,re,hashlib
import jsonschema
ROOT=pathlib.Path(__file__).resolve().parents[1]
names=['taste-extract-beta','frontend-taste-brief-beta','frontend-taste-review-beta']
count=0
for name in names:
 folder=ROOT/'solutions/design'/name
 solution=json.loads((folder/'solution.json').read_text())
 assert {t['locale']for t in solution['templates']}=={'en'}
 contract=json.loads((folder/'contracts/main.en.json').read_text())
 body=(ROOT/contract['template_path']).read_bytes()
 assert contract['template_digest']=='sha256:'+hashlib.sha256(body).hexdigest()
 assert set(re.findall(r'\{\{\s*([A-Za-z][A-Za-z0-9_]*)\s*\}\}',body.decode()))=={field['name']for field in contract['inputs']}
 manifest=json.loads((folder/'contracts/fixtures/main.en.fixtures.json').read_text())
 schema=json.loads((ROOT/manifest['schema']['ref']).read_text())
 validator=jsonschema.Draft202012Validator(schema)
 for case in manifest['cases']:
  output=json.loads((ROOT/case['output']['ref']).read_text());errors=list(validator.iter_errors(output))
  assert (not errors)==(case['kind']=='valid'),name+':'+case['case_id']
  count+=1
print(json.dumps({'status':'pass','templates':len(names),'schema_cases':count,'provider_calls':0}))
