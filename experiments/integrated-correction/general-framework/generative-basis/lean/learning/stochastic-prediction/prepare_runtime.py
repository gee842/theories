#!/usr/bin/env python3
"""Compile the frozen exposure evaluator in a fresh temporary directory."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,tempfile,shutil,hashlib,json,os
HERE=Path(__file__).resolve().parent
EXPECTED={'Exposure.lean':'99ae15f4c34a90d7f5f77440a392181af72f11586f8ced29de0f4e9f8a2d7063','Evaluate.lean':'7860a7b4d7f806613a8f62712b1b70fab0872c52a483a1a2c415d85cde090788'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    for n,v in EXPECTED.items():assert digest(HERE/n)==v,(n,'changed')
    prefix=Path(subprocess.check_output(['lean','+leanprover/lean4:v4.29.1','--print-prefix'],text=True).strip())
    lean=prefix/'bin/lean';tmp=Path(tempfile.mkdtemp(prefix='stochastic-prediction-eval-'))
    for n in EXPECTED:shutil.copyfile(HERE/n,tmp/n)
    build=subprocess.run([str(lean),'-o','Exposure.olean','Exposure.lean'],cwd=tmp,
        capture_output=True,text=True,env={**os.environ,'LEAN_PATH':str(tmp)})
    (HERE/'runtime-evaluator-build.txt').write_text(build.stdout+build.stderr)
    assert build.returncode==0,build.stdout+build.stderr
    for n,v in EXPECTED.items():assert digest(tmp/n)==v
    record=dict(status='compiled_frozen_evaluator_before_comparison',timestamp_utc=datetime.now(timezone.utc).isoformat(),
        sources=EXPECTED,initial_source_snapshot_sha256=digest(HERE/'check-source-freeze.json'),
        scope_clarification_sha256=digest(HERE/'CHECK-CLARIFICATION.md'),
        independent_checker_sha256_before_first_run=digest(HERE/'check_runtime.py'),
        preparation_program_sha256=digest(Path(__file__)),lean_executable=str(lean),lean_executable_sha256=digest(lean),
        lean_path=str(tmp),command=[str(lean),'--run',str(tmp/'Evaluate.lean')],
        compiled_object_sha256=digest(tmp/'Exposure.olean'),build_output_sha256=digest(HERE/'runtime-evaluator-build.txt'),
        note='Initial formal snapshot preserved; proof/audit finalization rebound before outcomes. Parent laws unchanged. First compile working-directory error preserved under development/.')
    (HERE/'runtime-formal-freeze.json').write_text(json.dumps(record,indent=2)+'\n')
    print('Fresh evaluator compiled; final source and clarification hashes recorded.')
if __name__=='__main__':main()
