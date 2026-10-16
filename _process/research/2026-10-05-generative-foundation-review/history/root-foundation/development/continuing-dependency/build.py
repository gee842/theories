"""Preserve every isolated proof attempt and bind the unchanged source law."""
from pathlib import Path
import hashlib, json, os, shutil, subprocess, tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LAW = ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean'
NEW = ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeReconstructionRequirement.lean'
BUILD = HERE/'isolated'
BUILD.mkdir(exist_ok=True)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
attempt = 1 + len(list(HERE.glob('attempt-*.json')))
stem = f'attempt-{attempt:02d}'
shutil.copyfile(NEW, HERE/(stem+'.lean'))
logs = []
with tempfile.TemporaryDirectory(prefix='continuing-dependency-lean-') as temporary:
    output = Path(temporary)
    env = dict(os.environ, LEAN_PATH=str(output))
    for source in (LAW, NEW):
        copied = BUILD/source.name
        shutil.copyfile(source, copied)
        run = subprocess.run(['lean','+leanprover/lean4:v4.29.1','-o',str(output/(source.stem+'.olean')),str(copied)],
                             cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        logs.append(f'SOURCE {source.relative_to(ROOT)}\n{run.stdout}')
        if run.returncode: break
log = '\n'.join(logs)
(HERE/(stem+'.log')).write_text(log)
receipt = dict(attempt=attempt, status='passed' if not run.returncode else 'failed',
               law=str(LAW.relative_to(ROOT)), law_sha256=sha(LAW),
               new=str(NEW.relative_to(ROOT)), new_sha256=sha(NEW),
               preserved_source_sha256=sha(HERE/(stem+'.lean')),
               log_sha256=sha(HERE/(stem+'.log')), build_script_sha256=sha(Path(__file__)))
(HERE/(stem+'.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(log)
print(json.dumps(receipt,indent=2))
raise SystemExit(run.returncode)
