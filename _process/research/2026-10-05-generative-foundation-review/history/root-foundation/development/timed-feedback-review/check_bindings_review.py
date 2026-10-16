"""Bind independently inspected timing review documents and passed receipts."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
OUT=Path(__file__).resolve().parent;ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file());STUDY=OUT.parent.parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text());bindings={}
def bind(p,expected=None):
 h=sha(p)
 if expected:assert h==expected,(p,h,expected)
 bindings[str(p.relative_to(ROOT))]=h
 return h
EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence';ANALYSIS=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
r=load(OUT/'verification.json');assert r['status']=='passed';bind(OUT/'verification.json');bind(OUT/'check_lean_review.py',r['review_script_sha256']);bind(ANALYSIS/'check_timed_feedback.py',r['checker_sha256']);bind(ANALYSIS/'timed-feedback-verification.json',r['author_receipt_sha256']);bind(OUT/'Audit.lean',r['audit_source_sha256'])
for name,h in r['log_sha256'].items():bind(OUT/name,h)
for module in load(ANALYSIS/'timed-feedback-verification.json')['modules']:
 assert r['source_sha256'][module['module']]==module['source_sha256'];bind(ROOT/module['source'],module['source_sha256'])
n=load(OUT/'numerical-verification.json');assert n['status']=='passed';bind(OUT/'numerical-verification.json');bind(OUT/'check_numeric_review.py',n['script_sha256']);bind(EXP/'timing-results.json',n['author_results_sha256']);bind(EXP/'analyze_timing.py',n['author_producer_sha256']);bind(ROOT/'sources/tclab-benchmark/TIMING-PROVENANCE.json',n['manifest_sha256']);bind(OUT/'numerical-log.txt')
for path,h in n['original_members_sha256'].items():bind(ROOT/path,h)
m=load(ROOT/'sources/tclab-benchmark/TIMING-PROVENANCE.json');bind(ROOT/m['archive_path'],m['archive_sha256']);bind(EXP/'extract_timing_sources.py',m['producer_sha256']);bind(ROOT/m['original_provenance']);bind(ROOT/'sources/tclab-benchmark/CACE_2020_Preprint.pdf')
prose=[STUDY/'TIMED-FEEDBACK-INTEGRATION.md',STUDY/'THREE-CONNECTIONS-COMPLETION-AUDIT.md',ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MEASURED-FEEDBACK-CORRESPONDENCE.md']
prose_hashes={str(p.relative_to(ROOT)):bind(p) for p in prose}
for p in [STUDY/'INQUIRY-JUDGMENT-INTEGRATION.md',ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PROVED-CONNECTIONS.md',STUDY/'development/tuning-accepted-documents/THREE-CONNECTIONS-COMPLETION-AUDIT.md']:bind(p)
result={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),'document_sha256':prose_hashes,'file_sha256':bindings,'scope':'Exact source, provenance, receipt and final inspected prose bindings; not a new scientific rerun.'}
(OUT/'bindings.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'passed','document_sha256':prose_hashes,'bound_files':len(bindings)},indent=2))
