#!/usr/bin/env python3
"""Check current documents, frozen Lean receipt and owned bilingual rows."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,importlib.util
from urllib.parse import unquote
H=Path(__file__).resolve().parent;R=H.parents[3]
T=R/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
A=R/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('chain',H/'build_generative_chain.py');chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
docs=[H/'SEEDED-CONTINUATION-INTEGRATION.md',T/'RELATIONS-ACROSS-SCALES.md',R/'sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md']
errors=[];links=[]
for p in docs:
 for ref in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'[a-z]+:',ref):continue
  name,_,anchor=unquote(ref).partition('#');target=(p.parent/name).resolve() if name else p
  valid=target.is_file() and (not anchor or anchor in chain.heading_ids(target));links.append({'from':str(p.relative_to(R)),'reference':ref,'valid':valid})
  if not valid:errors.append('Bad link: '+ref)
receipt=json.loads((A/'seeded-continuation-verification.json').read_text())
if not (receipt['status']=='passed' and receipt['inputs_unchanged'] and receipt['new_audits']==13 and receipt['replayed_inherited_audits']==30):errors.append('Proof receipt scope')
for key,p in [('checker_sha256',A/'check_seeded_continuation.py'),('toolchain_sha256',A/'lean-toolchain')]:
 if receipt[key]!=sha(p):errors.append('Proof input mismatch: '+p.name)
empty=0; new_count=0; inherited_count=0
for m in receipt['modules']:
 for p in [A/(m['module']+'.lean'),A/'seeded-continuation-verification/sources'/(m['module']+'.lean')]:
  if sha(p)!=m['source_sha256']:errors.append('Proof source mismatch: '+str(p))
 if sha(A/'seeded-continuation-verification'/(m['module']+'.txt'))!=m['output_sha256']:errors.append('Proof output mismatch')
 if not m['passed']:errors.append('Module not passed')
 if m['module']=='SeededContinuation':new_count+=len(m['audits'])
 else:inherited_count+=len(m['audits'])
 for audit in m['audits']:
  if not set(audit['axioms']) <= {'propext','Classical.choice','Quot.sound'}:errors.append('Unexpected axioms')
  if m['module']=='SeededContinuation':empty+=not audit['axioms']
if (new_count,inherited_count,empty)!=(13,30,6):errors.append('Module audit counts differ')
edits=json.loads((H/'SEEDED-CONTINUATION-INDEX-EDITS.json').read_text());data=chain.read_data();entries={e['id']:e for s in data['sections'] for e in s['entries']}
canonical=chain.render(data).splitlines();actual=chain.OUTPUT.read_text().splitlines()
for e in edits['updated_entries']:
 if entries[e['id']]!=e:errors.append('Owned row changed: '+e['id'])
 prefix='| '+e['id']+' |'
 if [l for l in canonical if l.startswith(prefix)] != [l for l in actual if l.startswith(prefix)]:errors.append('Rendered row mismatch')
for name in edits['reviewed_paths']:
 if data['reviewed_sources'].get(name)!=sha(R/name):errors.append('Owned review version differs: '+name)
table=json.loads((H/'SEEDED-CONTINUATION-TABLE-CHECKS.json').read_text())
if table['status']!='passed':errors.append('Scoped table failed')
record={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'status':'passed' if not errors else 'failed','scope':'Document links, retained checked Lean bindings, counts and canonical C28/F20 rows only; no independent-agent review, full-table validation or new empirical evidence.','errors':errors,'new_theorems':13,'empty_dependencies':empty,'inherited_audits_rerun':30,'proof_receipt_sha256':sha(A/'seeded-continuation-verification.json'),'checker_sha256':sha(Path(__file__)),'documents':{str(p.relative_to(R)):sha(p) for p in docs},'links':links,'owned_entries':edits['entry_ids']}
(H/'SEEDED-CONTINUATION-CHECKS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':record['status'],'links':len(links),'errors':errors}))
if errors:raise SystemExit(1)
