"""Review evidence and inspected final prose bindings; no scientific rerun."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, io, json, zipfile
OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file())
EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
STUDY=OUT.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
bindings={}
def bind(path, expected=None):
 actual=sha(path)
 if expected is not None:assert actual==expected,(str(path),actual,expected)
 bindings[str(path.relative_to(ROOT))]=actual
 return actual
contracts={
 'tuning-source-contract.json':{'inspection_source_sha256':'inspect_tuning_source.py'},
 'tuning-model.json':{'producer_sha256':'fit_tuning_model.py','solver_log_sha256':'tuning-fit-log.txt'},
 'tuning-results.json':{'producer_sha256':'analyze_tuning.py','fit_sha256':'tuning-model.json'},
 'tuning-runtime-checks.json':{'checker_sha256':'check_tuning_runtime.py','producer_sha256':'analyze_tuning.py','fit_sha256':'tuning-model.json','results_sha256':'tuning-results.json','log_sha256':'tuning-runtime-log.txt'},
 'tuning-reference-check.json':{'checker_sha256':'check_initial_reference.py','analysis_source_sha256':'analyze_tuning.py','fit_sha256':'tuning-model.json'},
}
for name,pairs in contracts.items():
 d=read(EXP/name);bind(EXP/name)
 for field,name2 in pairs.items():bind(EXP/name2,d[field])
source=read(EXP/'tuning-source-contract.json');archive=ROOT/'sources/tclab-benchmark/CACE_2020_source.zip';bind(archive,source['archive_sha256'])
with zipfile.ZipFile(archive) as z:
 train=z.read(source['training_member'])
 assert hashlib.sha256(train).hexdigest()==source['training_member_sha256']
 initial=ROOT/'sources/tclab-benchmark/extracted/2_PID/0_initial_PID/data.txt';assert train==initial.read_bytes();bind(initial,source['training_member_sha256'])
 rows=list(csv.DictReader(io.StringIO(train.decode())))
 assert len(rows)==599 and all(float(r['Q2'])==0 for r in rows)
 for name in ['2_PID/2_optimize_PID/tclab_optimal.py','2_PID/2_optimize_PID/validation_test1/validate.txt','2_PID/2_optimize_PID/validation_test2/validate.txt']:
  p=ROOT/'sources/tclab-benchmark/extracted'/name;assert p.read_bytes()==z.read(name);bind(p)
bind(ROOT/'sources/tclab-benchmark/extracted/2_PID/2_optimize_PID/tclab_optimal.py',source['optimizer_source_sha256'])
f=read(EXP/'tuning-model.json');bind(ROOT/f['training_source'],f['training_sha256'])
for receipt,script,field in [('verification.json','check_lean_review.py','review_script_sha256'),('grid-verification.json','check_grid_review.py','script_sha256'),('solver-verification.json','check_solver_review.py','review_script_sha256')]:
 d=read(OUT/receipt);assert d['status']=='passed';bind(OUT/receipt);bind(OUT/script,d[field])
 for name,value in d.get('log_sha256',{}).items():bind(OUT/name,value)
 for field2,name in [('fit_sha256','tuning-model.json'),('results_sha256','tuning-results.json'),('reference_sha256','tuning-reference-check.json')]:
  if field2 in d:bind(EXP/name,d[field2])
d=read(OUT/'verification.json')
lean=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean'
author=read(lean/'systems-complexity/analysis/tuning-correspondence-verification.json')
for module in author['modules']:
 assert d['source_sha256'][module['module']]==module['source_sha256']
 bind(ROOT/module['source'],module['source_sha256'])
analysis=lean/'systems-complexity/analysis'
bind(analysis/'check_tuning_correspondence.py',d['checker_sha256']);bind(analysis/'tuning-correspondence-verification.json',d['author_receipt_sha256']);bind(OUT/'Audit.lean',d['audit_source_sha256'])
prose=[STUDY/'TUNING-CORRESPONDENCE-INTEGRATION.md',STUDY/'THREE-CONNECTIONS-COMPLETION-AUDIT.md',ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MEASURED-FEEDBACK-CORRESPONDENCE.md']
prose_hashes={str(p.relative_to(ROOT)):bind(p) for p in prose}
record={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),'document_sha256':prose_hashes,'file_sha256':bindings,'archive_training_duplicate':True,'training_rows':len(rows),'second_heater_command_all_zero':True,'scope':'Exact bindings of inspected final prose, preserved original members, author artifacts and independently produced receipts. Does not itself rerun proof, fitting or numerical analysis.'}
(OUT/'bindings.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'document_sha256':prose_hashes,'bound_files':len(bindings)},indent=2))
