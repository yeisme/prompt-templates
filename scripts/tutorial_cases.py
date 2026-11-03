#!/usr/bin/env python3
"""Author data-only tutorial cases through the Registry CLI; reuse semantic fixtures."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

import author_guides as guides
from tutorial_values import EMPTY_NOTES, value_for

ROOT=Path(__file__).resolve().parents[1]

def fixture(folder,role):
 for locale in ['en','zh-CN']:
  path=folder/'contracts/fixtures'/f"{role['role']}.{locale}.fixtures.json"
  if not path.exists():continue
  manifest=json.loads(path.read_text())
  for case in manifest['cases']:
   if case['kind']=='valid':
    return locale,case,json.loads((ROOT/case['input']['ref']).read_text()),json.loads((ROOT/case['output']['ref']).read_text())
 return None

def load_case(folder,role,manifest,case):
 if not case.get('fixture_case_id'):return case['inputs'],case.get('output')
 locale=case.get('fixture_locale',role['locale']);set_=json.loads((folder/'contracts/fixtures'/f"{role['role']}.{locale}.fixtures.json").read_text())
 item=next(c for c in set_['cases'] if c['case_id']==case['fixture_case_id'])
 raw=json.loads((ROOT/item['input']['ref']).read_text());output=json.loads((ROOT/item['output']['ref']).read_text())
 values={}
 for target,key in case.get('fixture_input_map',{k:k for k in raw}).items():
  v=raw[key]
  if target.endswith('_json') and not isinstance(v,str):v=json.dumps(v,ensure_ascii=False,separators=(',',':'))
  values[target]=v
 values.update(case.get('inputs',{}))
 return values,output

def author(folder,solution,role):
 contract=json.loads((folder/'contracts'/f"{role['role']}.en.json").read_text());source=guides.SCENARIOS.get(solution['category'],guides.SCENARIOS['general'])[1]
 existing=fixture(folder,role);values={};mapping={};supplement={}
 for f in contract['inputs']:
  n=f['name'];key=n
  if existing and key not in existing[2] and n.endswith('_json'):key=n[:-5]
  if existing and key in existing[2]:
   value=existing[2][key]
   if n.endswith('_json') and not isinstance(value,str):value=json.dumps(value,ensure_ascii=False,separators=(',',':'))
   if f.get('enum') and value not in f['enum']:
    value=f['enum'][0];supplement[n]=value
   else:mapping[n]=key
   values[n]=value
  else:
   value=value_for(f,guides.example(f,source,{}))
   if existing and n=='authoring_json':value=json.dumps(existing[2],ensure_ascii=False,separators=(',',':'))
   values[n]=value;supplement[n]=value
 # Use the actual source material from a referenced case, not a different category vignette.
 for key in ['source_text','meeting_record','sources','source_material','source_brief','script']:
  if key in values and isinstance(values[key],str):source=values[key];break
 if existing and source==guides.SCENARIOS.get(solution['category'],guides.SCENARIOS['general'])[1]:
  source='本次合成任务采用已验证案例 '+existing[1]['case_id']+'；各字段以该案例的公开输入为准，不追加资料外事实。'
 notes={};required_keys={}
 for n,v in values.items():
  if not n.endswith('_json'):continue
  parsed=json.loads(v)
  if parsed in ({},[]):
   note=EMPTY_NOTES.get(n)
   if n=='accepted_story_context_refs_json':note='首次从给定剧本创建分镜，没有已接受的长篇上下文引用；来源片段仍须提供。'
   if note is None:raise ValueError('unexplained empty JSON: '+solution['id']+':'+n)
   notes[n]=note
  elif isinstance(parsed,dict):required_keys[n]=sorted(parsed)
  notes.setdefault(n,'案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。')
 checks=['核对所有事实能在输入资料或已接受引用中找到。','核对输出满足 '+role.get('summary',solution['locales'].get('zh-CN',solution['locales']['en']).get('summary','当前角色职责')),'缺失或未确认信息必须明确标注；不得新增授权、执行或生产完成声明。']
 positive={'id':'complete-scenario','kind':'valid','review_checks':checks}
 if existing:
  positive.update(fixture_case_id=existing[1]['case_id'],fixture_locale=existing[0],fixture_input_map=mapping)
  if supplement:positive['inputs']=supplement
 else:
  positive.update(inputs=values,output={'role':role['role'],'example':guides.result_example(solution['category'],solution['locales'].get('zh-CN',solution['locales']['en']).get('title',solution['id']),role,folder),'acceptance':'synthetic-example-only'})
 missing=next((f['name'] for f in contract['inputs'] if f.get('required') and 'default' not in f),None)
 bad=dict(values)
 if missing:bad.pop(missing);code='INPUT_REQUIRED';reason='缺少必填字段 '+missing+'，必须补齐后再确认。'
 else:bad['unexpected_field']='denied';code='TUTORIAL_UNKNOWN_FIELD';reason='拒绝未声明字段，不能让额外输入绕过合同。'
 cases=[positive,{'id':'missing-required-input','kind':'invalid','inputs':bad,'expected_code':code,'review_checks':[reason]}]
 # A separate data-shape negative checks complex JSON, beyond mere string length.
 if required_keys:
  field=next(iter(required_keys));broken=dict(values);broken[field]='[]'
  cases.append({'id':'wrong-json-shape','kind':'invalid','inputs':broken,'expected_code':'TUTORIAL_JSON_KEY_REQUIRED','review_checks':['JSON 语法合法但缺少业务对象字段，不能标为场景通过。']})
 return {'source_text':source,'input_notes':notes,'json_required_keys':required_keys,'cases':cases}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--registry',default='template-registry');parser.add_argument('--check',action='store_true');args=parser.parse_args()
 binary=str(Path(args.registry).resolve()) if '/' in args.registry else args.registry
 count=0;reused=0
 for p in sorted(ROOT.glob('solutions/*/*/solution.json')):
  solution=json.loads(p.read_text())
  for role in solution['templates']:
   if role['locale']!='en':continue
   op='validate' if args.check else 'set';command=[binary,'tutorial','case',op,'--repository',str(ROOT),'--package',solution['package_id'],'--id',solution['id'],'--role',role['role'],'--locale','en','--json']
   payload=None
   if not args.check:payload=json.dumps(author(p.parent,solution,role),ensure_ascii=False);command.append('--stdin')
   result=subprocess.run(command,input=payload,text=True,capture_output=True)
   if result.returncode:
    try:message=json.loads(result.stdout).get('error',{}).get('message','TUTORIAL_FAILED')
    except ValueError:message='TUTORIAL_FAILED'
    print(solution['id'],role['role'],message,file=sys.stderr);return result.returncode
   manifest=json.loads((p.parent/'tutorials'/f"{role['role']}.en.json").read_text());reused+=any(c.get('fixture_case_id') for c in manifest['cases']);count+=1
 print(json.dumps({'status':'passed','english_roles':count,'reused_fixture_roles':reused,'human_review':'pending'}));return 0

if __name__=='__main__':raise SystemExit(main())
