#!/usr/bin/env python3
"""Owned documentation, current proof/archive bindings and data provenance.
This does not rerun Lean, repeat experiments, or constitute independent review.
"""
from pathlib import Path
import json,hashlib,re,importlib.util
from urllib.parse import unquote
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
R=P.parents[3]
A=R/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
E=R/'experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence'
S=R/'sources/biological-scale-correspondence/elife-65935'
T=R/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('chain',P/'build_generative_chain.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
errors=[];links=[]
docs=[P/'ORGANIZED-SCALES-INTEGRATION.md',P/'ORGANIZED-SCALES-EVIDENCE.md',T/'RELATIONS-ACROSS-SCALES.md',S/'README.md',E/'README.md',R/'sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md']
for p in docs:
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match('[a-z]+:',target):continue
  f,_,fragment=unquote(target).partition('#');dest=(p.parent/f).resolve() if f else p
  good=dest.exists() and (not fragment or fragment in m.heading_ids(dest))
  links.append({'from':str(p.relative_to(R)),'target':target,'valid':good})
  if not good:errors.append(f'Invalid link {p.name}: {target}')
rec=json.loads((A/'organized-scale-verification.json').read_text());archive=A/rec['archive']
assert rec['status']=='passed' and rec['new_audits']==26 and rec['replayed_inherited_audits']==77 and rec['inputs_unchanged']
assert (archive/'receipt.json').read_bytes()==(A/'organized-scale-verification.json').read_bytes()
assert sha(A/'check_organized_scales.py')==sha(archive/'sources/check_organized_scales.py')==rec['checker_sha256']
assert sha(A/'lean-toolchain')==rec['toolchain_sha256']
for module in rec['modules']:
 name=module['module']
 current=A/(name+'.lean')
 if name=='SystemsOrganization':current=A.parent/(name+'.lean')
 if name=='GenerativeCore':current=A.parent.parent/(name+'.lean')
 assert sha(current)==sha(archive/'sources'/(name+'.lean'))==module['source_sha256']
 assert sha(archive/(name+'.txt'))==module['output_sha256'] and module['passed']
 assert all(set(x['axioms'])<={'propext','Classical.choice','Quot.sound'} for x in module['audits'])
res=json.loads((E/'results.json').read_text());man=json.loads((S/'manifest.json').read_text())
assert res['status']=='passed' and res['diameter_measurements']==268 and res['occupancy_measurements']==135
assert res['script_sha256']==sha(E/'analyze_measurements.py') and res['extractor_sha256']==sha(E/'extract_measurements.mjs')
assert man['files']==res['source_files']
for f in man['files']:assert sha(S/f['file'])==f['sha256'] and (S/f['file']).stat().st_size==f['bytes']
data=m.read_data()
# Verify already-recorded reviews; never mark later unread changes reviewed.
for p in [P/'ORGANIZED-SCALES-INTEGRATION.md',P/'ORGANIZED-SCALES-EVIDENCE.md']:
 assert data['reviewed_sources'][str(p.relative_to(R))]==sha(p)
edit=json.loads((P/'ORGANIZED-SCALES-INDEX-EDITS.json').read_text())
entries={e['id']:e for section in data['sections'] for e in section['entries']}
rendered=m.render(data);saved=m.OUTPUT.read_text()
for ident,e in edit['after'].items():
 assert entries[ident]==e
 row=next(x for x in rendered.splitlines() if x.startswith('| '+ident+' |'))
 assert row in saved
record={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'status':'passed' if not errors else 'failed','errors':errors,'scope':'Owned links, passing Lean receipt/current/archive bindings, numerical scripts and original source hashes, and C29/F21 rows. Not a new proof run, biological validation, independent review or whole-table certification.','links':links,'checker_sha256':sha(Path(__file__)),'proof_receipt_sha256':sha(A/'organized-scale-verification.json'),'empirical_results_sha256':sha(E/'results.json'),'source_manifest_sha256':sha(S/'manifest.json'),'documents':{str(p.relative_to(R)):sha(p) for p in docs},'global_chain_pending':m.changes(data)}
(P/'ORGANIZED-SCALES-CHECKS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':record['status'],'links_checked':len(links),'errors':errors,'new_theorems':26,'replayed_audits':77,'published_measurements':403,'global_table_status':'pending source review'},indent=2))
if errors:raise SystemExit(1)
