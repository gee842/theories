"""Preserve source provenance and checked claims without implying a full inherited rerun."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json,hashlib

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parents[1]/'outputs'/'missing-possibilities-evidence.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def readj(p): return json.loads(p.read_text())
manifest=readj(ROOT/'source-manifest.json')
source_files={}
for entry in manifest['files']:
    p=Path(entry['snapshot'])
    assert sha(p)==entry['sha256'],p
    source_files[entry['relative']]={'original_path':entry['original'],'sha256':entry['sha256'],'text':p.read_text()}
audit_names=['discovery-audit.md','interface-audit.md','synthesis-audit.md','final-review.md']
check_paths=['interface-witness.py','interface-witness-results.json','check_joint_distinction.py',
             'check_expansion.py','expansion-check-results.json','discovery-checks/audit.py',
             'discovery-checks/audit-check-results.json','discovery-checks/source-hashes.json',
             'discovery-checks/grammar-witness.py','discovery-checks/grammar-witness-results.json']
evidence_dir=ROOT/'discovery-checks'/'inherited-evidence'
inherited={p.name:{'sha256':sha(p),'text':p.read_text()} for p in evidence_dir.iterdir()
           if p.is_file() and p.suffix in ['.md','.json']}
raw=evidence_dir/'runs.jsonl'
row_count=sum(1 for _ in raw.open())
assert row_count==7168
assert sha(raw)=='5ebfebbd2d87632469d90d2b0e070d5d0c2c4f3c23d91394c381b2d63692a963'
checks={name:{'sha256':sha(ROOT/name),'text':(ROOT/name).read_text()} for name in check_paths}
bundle={
 'title':'Sources and verification for noticing missing possibilities',
 'packaged_at':datetime.now(ZoneInfo('Asia/Bangkok')).isoformat(),
 'status':'Cross-session synthesis, inherited result audit, and new exact finite counterexamples complete.',
 'main_conclusion':'Bounded discovery is possible through richer linked observations, explicit candidate construction or grammar expansion, appropriate independent confirmation, and a feasible route to response. This is not a universal completeness guarantee.',
 'evidence_status':{
  'inherited_model_checks':'Four copied mechanism tests passed; full stored summary recounted; 56 selected trajectories replayed, not all 7168.',
  'new_exact_checks':['E/U observation-law and value-sign witness independently enumerated','Same-summary histories checked under temporal/nested model expansion','Two-bit joint-distinction witness','All73 original candidate policies evaluated for four-literal hazard','All729 conjunctions evaluated across depths0through6'],
  'proposed_practice':'Operational synthesis and scheduled candidate allocation are recommendations with explicit limits, not newly benchmarked general reasoning improvements.',
  'not_established':['Unrestricted invention of new observation variables or purposes','Finite-sample discovery reliability for expanded grammar','Universal exploration budget or optimal process','General superiority of six-question prompt','Empirical institutional prevalence','Ethical authority or alignment']},
 'source_manifest':manifest,'source_files':source_files,
 'internal_reviews':{n:(ROOT/n).read_text() for n in audit_names},
 'verification_files':checks,
 'new_check_results':{
  'interface':readj(ROOT/'interface-witness-results.json'),
  'joint_distinction':readj(ROOT.parents[1]/'outputs'/'missing-possibility-check.json'),
  'candidate_grammar':readj(ROOT/'discovery-checks'/'grammar-witness-results.json'),
  'scheduled_expansion':readj(ROOT/'expansion-check-results.json')},
 'inherited_evidence_metadata_and_summaries':inherited,
 'inherited_raw_trajectory_record':{'original_and_copy_paths':'See copy-manifest.json in inherited_evidence_metadata_and_summaries','copy_path':str(raw),'sha256':sha(raw),'row_count':row_count,'embedded':False,'note':'Raw rows remain in the saved work directory. This bundle embeds provenance, summaries and audit results rather than all inherited trajectories.'},
 'primary_literature_checked':[
  {'title':'Impossibility Theorems for Domain Adaptation','year':2010,'url':'https://proceedings.mlr.press/v9/david10a/david10a.pdf','examined':'Section5 proof sketches and related abstract/conclusion','use':'Related input-indistinguishability obstruction; distinct setting.'},
  {'title':'The Automation of Science','year':2009,'url':'https://research.aber.ac.uk/en/publications/the-automation-of-science/','examined':'Author institution publication record and abstract; preprint fetch timed out','use':'Generated and physically tested domain-specific hypotheses.'},
  {'title':'Towards Robot Scientists for autonomous scientific discovery','year':2010,'url':'https://link.springer.com/article/10.1186/1759-4499-2-1','examined':'Adam software and results sections','use':'Developers report hypothesis-generation mechanism and omitted-regulatory-mechanism caveat; historical, not current classification.'}
 ],
 'provenance_limits':['Internal AI-agent review, not external scientific replication.','Other-session source workspace read only; no messages sent to those chats.','Snapshot retention is not a claim that all copied files were fully read.','Inherited simulations are synthetic and paired within seed clusters.','New exact calculations use stipulated variables, actions, costs and model families.']
}
OUT.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'output':str(OUT),'bytes':OUT.stat().st_size,'source_files_verified':len(source_files),'inherited_rows_checked':row_count,'reviews':len(audit_names)}))
