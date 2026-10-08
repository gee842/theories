#!/usr/bin/env python3
"""Check current documents, frozen Lean receipt and owned bilingual rows."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,importlib.util
from urllib.parse import unquote
H=Path(__file__).resolve().parent;R=H.parents[3]
T=R/'theories/becoming/chapters'
A=R/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('chain',H/'build_generative_chain.py');chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
docs=[H/'CONTINUATION-ADEQUACY-INTEGRATION.md',T/'RELATIONS-ACROSS-SCALES.md',R/'sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md']
errors=[];links=[]
for p in docs:
 for ref in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'[a-z]+:',ref):continue
  name,_,anchor=unquote(ref).partition('#');target=(p.parent/name).resolve() if name else p
  valid=target.is_file() and (not anchor or anchor in chain.heading_ids(target));links.append({'from':str(p.relative_to(R)),'reference':ref,'valid':valid})
  if not valid:errors.append('Bad link: '+ref)
receipt=json.loads((A/'continuation-adequacy-verification.json').read_text())
if not (receipt['status']=='passed' and receipt['inputs_unchanged'] and receipt['new_audits']==14 and receipt['replayed_inherited_audits']==0):errors.append('Proof receipt scope')
for key,p in [('checker_sha256',A/'check_continuation_adequacy.py'),('toolchain_sha256',A/'lean-toolchain')]:
 if receipt[key]!=sha(p):errors.append('Proof input mismatch: '+p.name)
empty=0
for m in receipt['modules']:
 for p in [A/(m['module']+'.lean'),A/'continuation-adequacy-verification/sources'/(m['module']+'.lean')]:
  if sha(p)!=m['source_sha256']:errors.append('Proof source mismatch: '+str(p))
 if sha(A/'continuation-adequacy-verification'/(m['module']+'.txt'))!=m['output_sha256']:errors.append('Proof output mismatch')
 if not m['passed']:errors.append('Module not passed')
 for audit in m['audits']:
  if not set(audit['axioms']) <= {'propext','Classical.choice','Quot.sound'}:errors.append('Unexpected axioms')
  empty+=not audit['axioms']
if empty!=9:errors.append('Empty dependency count differs')
edits=json.loads((H/'CONTINUATION-ADEQUACY-INDEX-EDITS.json').read_text());data=chain.read_data();entries={e['id']:e for s in data['sections'] for e in s['entries']}
canonical=chain.render(data).splitlines();actual=chain.OUTPUT.read_text().splitlines()
for e in edits['updated_entries']:
 if entries[e['id']]!=e:errors.append('Owned row changed: '+e['id'])
 prefix='| '+e['id']+' |'
 if [l for l in canonical if l.startswith(prefix)] != [l for l in actual if l.startswith(prefix)]:errors.append('Rendered row mismatch')
for name in edits['reviewed_paths']:
 if data['reviewed_sources'].get(name)!=sha(R/name):errors.append('Owned review version differs: '+name)
table=json.loads((H/'CONTINUATION-ADEQUACY-TABLE-CHECKS.json').read_text())
if table['status']!='passed':errors.append('Scoped table failed')
record={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'status':'passed' if not errors else 'failed','scope':'Document links, retained checked Lean bindings, counts and canonical C28/F20 rows only; no independent-agent review, full-table validation or new empirical evidence.','errors':errors,'new_theorems':14,'empty_dependencies':empty,'inherited_audits_rerun':0,'proof_receipt_sha256':sha(A/'continuation-adequacy-verification.json'),'checker_sha256':sha(Path(__file__)),'documents':{str(p.relative_to(R)):sha(p) for p in docs},'links':links,'owned_entries':edits['entry_ids']}
(H/'CONTINUATION-ADEQUACY-CHECKS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':record['status'],'links':len(links),'errors':errors}))
if errors:raise SystemExit(1)
