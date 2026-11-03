#!/usr/bin/env python3
"""Author the English successor using Registry recipe operations."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]

def main():
 p=argparse.ArgumentParser();p.add_argument('--registry',default='template-registry');a=p.parse_args()
 binary=str(Path(a.registry).resolve()) if '/' in a.registry else a.registry
 original=(ROOT/'recipes/research-summary.json').read_bytes()
 path='recipes/research-summary-en.json'
 with tempfile.TemporaryDirectory(prefix='recipe-author-') as tmp:
  env={**os.environ,'TEMPLATE_REGISTRY_CONFIG_ROOT':tmp}
  def call(operation,payload):
   r=subprocess.run([binary,'prompt','recipe',operation,'--project',str(ROOT),'--stdin','--json'],input=json.dumps({'path':path,**payload}),capture_output=True,text=True,env=env)
   if r.returncode:raise RuntimeError(json.loads(r.stdout).get('error',{}).get('code','RECIPE_AUTHOR_FAILED'))
  if not (ROOT/path).exists():call('init',{'id':'research-summary-en'})
  call('step',{'step':{'id':'research','ref':'promptrepo://official/research/evidence-research-brief-beta@2.0.0-beta.1?locale=en','role':'main'}})
  call('step',{'step':{'id':'summary','ref':'promptrepo://official/general/structured-summary-beta@2.0.0-beta.1?locale=en','role':'main'}})
  for step,field,kind,ref in [('research','sources','source','evidence'),('research','research_question','field','question'),('research','decision_maker','field','audience'),('summary','source_text','step_output','research'),('summary','target_audience','field','audience')]:
   call('bind',{'step_id':step,'field':field,'binding':{'kind':kind,'ref':ref}})
  call('validate',{})
 assert original==(ROOT/'recipes/research-summary.json').read_bytes()
 print('English successor validated; legacy recipe unchanged.')

if __name__=='__main__':main()
