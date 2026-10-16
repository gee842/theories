#!/usr/bin/env python3
"""Check owned integration; empirical arithmetic has its separate retained receipt."""
import hashlib,importlib.util,json,re,sys
from pathlib import Path
from urllib.parse import unquote
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
E=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/situated-recovery'
def sha(b):return hashlib.sha256(b).hexdigest()
spec=importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py');chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
edits=json.loads((HERE/'CONTEXT-UPDATING-INDEX-EDITS.json').read_text());data=chain.read_data()
e=next(e for s in data['sections'] for e in s['entries'] if e['id']=='M20')
for k,v in edits['owned_suffixes'].items():assert e[k].count(v)==1 and edits['entry_before'][k]+v==edits['entry_after'][k]
for link in edits['entry_before']['links']+edits['added_links']:assert link in e['links']
assert next(x for x in chain.render(data).splitlines() if x.startswith('| M20 |'))==next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith('| M20 |'))
passages=[]
for name,h in edits['owned_reviewed_sources'].items():
 p=ROOT/name;assert sha(p.read_bytes())==h==data['reviewed_sources'][name],name
 if name in edits['prior_content']:
  before=edits['prior_content'][name];b=p.read_bytes();assert sha(b[:before['prior_length']])==before['prior_sha256'];assert b[before['prior_length']:before['prior_length']+len(before['addition'].encode())].decode()==before['addition'];passages.append((p,before['addition']))
 elif p.suffix=='.md':passages.append((p,p.read_text()))
for name,info in edits['shared_fragments'].items():
 p=ROOT/name;assert p.read_text().count(info['fragment'])==1 and info['other_bytes_preserved'];passages.append((p,info['fragment']))
for name in ['MEMORY-UPDATING-PLAN.md','MEMORY-UPDATING.md']:passages.append((E/name,(E/name).read_text()))
links=[]
for p,body in passages:
 for ref in re.findall(r'\]\(([^\s)]+)\)',body):
  if re.match(r'[a-zA-Z]+:',ref):continue
  name,_,anchor=ref.partition('#');target=(p.parent/unquote(name)).resolve() if name else p
  assert target.is_relative_to(ROOT) and target.exists(),(p,ref)
  assert not anchor or unquote(anchor) in chain.heading_ids(target),(p,ref)
  links.append({'from':str(p.relative_to(ROOT)),'reference':ref})
for link in edits['added_links']:
 p,anchor=chain.local_target(link['path']);assert p.exists() and (not anchor or anchor in chain.heading_ids(p))
receipt=json.loads((E/'memory-updating-verification.json').read_text());assert receipt['status']=='passed'
for name,h in receipt['source_sha256'].items():assert sha((E/name).read_bytes())==h,name
assert receipt['participants']==24 and receipt['channel_measurements']==7008 and receipt['triplets']==2304
for name,h in edits['unchanged_prior_scientific_files'].items():assert sha((ROOT/name).read_bytes())==h,name
L=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
prior=json.loads((L/'diagnostic-tracking-verification.json').read_text());assert prior['status']=='passed'
for name,h in prior['source_sha256'].items():assert sha((L/(name+'.lean')).read_bytes())==h
others=[e for s in data['sections'] for e in s['entries'] if e['id']!='M20']
other_lines=''.join(x for x in chain.OUTPUT.read_text().splitlines(keepends=True) if not x.startswith('| M20 |'))
result={'status':'passed','scope':edits['scope'],'local_links_checked':len(links),'links':links,'prior_documents_preserved':len(edits['prior_content']),'owned_M20_matches_renderer':True,'other_entries_preserved_at_mutation':edits['other_entries_preserved_at_mutation'],'unrelated_entries_match_edit_baseline':sha(json.dumps(others,ensure_ascii=False,sort_keys=True).encode())==edits['unrelated_entries_sha256'],'other_table_lines_match_edit_baseline':sha(other_lines.encode())==edits['other_table_lines_sha256'],'source_sha256':edits['owned_reviewed_sources'],'checker_sha256':sha(Path(__file__).read_bytes()),'empirical_receipt_sha256':sha((E/'memory-updating-verification.json').read_bytes()),'prior_Lean_sources_unchanged':True,'new_theorems':0,'proof_recompiled':False,'pending_global_chain_review':chain.changes(data),'whole_chain_certified':False,'independent_review':False}
(HERE/'CONTEXT-UPDATING-CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','local_links_checked','prior_documents_preserved','owned_M20_matches_renderer','prior_Lean_sources_unchanged']}))
