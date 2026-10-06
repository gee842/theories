"""Check preserved Lean build receipts without rerunning the scientific model."""
from pathlib import Path
import hashlib, json, re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
attempts = []
for p in sorted(HERE.glob('attempt-*.json')):
    receipt = json.loads(p.read_text())
    stem = p.stem
    assert sha(HERE/(stem+'.lean')) == receipt['preserved_source_sha256']
    assert sha(HERE/(stem+'.log')) == receipt['log_sha256']
    builders = [HERE/'build.py', HERE/'build-before-cleanup.py']
    assert any(sha(builder) == receipt['build_script_sha256'] for builder in builders)
    assert sha(ROOT/receipt['law']) == receipt['law_sha256']
    attempts.append(dict(path=str(p.relative_to(ROOT)), sha256=sha(p), status=receipt['status']))
assert attempts and receipt['status'] == 'passed'
assert sha(ROOT/receipt['new']) == receipt['new_sha256']
log = (HERE/(stem+'.log')).read_text()
rows = re.findall(r"'(Generative\.ReconstructionRequirement\.[^']+)' depends on axioms:\s*\[([^\]]*)\]", log)
audits = {name: re.findall(r'[A-Za-z_.]+', ax) for name,ax in rows}
source = (ROOT/receipt['new']).read_text()
declared = {'Generative.ReconstructionRequirement.'+name for name in re.findall(r'^theorem (\w+)', source, re.M)}
assert set(audits) == declared and len(audits) == 20
assert all(set(xs) <= {'propext','Quot.sound'} for xs in audits.values())
assert not re.search(r'\b(sorry|admit|axiom)\b', source)
prior = json.loads((HERE/'VERIFICATION.json').read_text())
assert sha(HERE/'verify-before-cleanup.py') == prior['verify_source_sha256']
cleanup = json.loads((HERE/'CACHE-CLEANUP.json').read_text())
assert all(sha(ROOT/p) == digest for p,digest in cleanup['protected_hashes'].items())
assert all(not (ROOT/entry['path']).exists() for entry in cleanup['removed'])
report = dict(status='passed', scope='Preserved proof receipt rechecked after cache cleanup; no Lean or model rerun',
              lean_toolchain='leanprover/lean4:v4.29.1', source=receipt['new'], source_sha256=receipt['new_sha256'],
              unchanged_law=receipt['law'], unchanged_law_sha256=receipt['law_sha256'],
              successful_log_sha256=receipt['log_sha256'], attempts=attempts,
              declarations=len(audits), dependency_audits=audits,
              verify_source_sha256=sha(Path(__file__)),
              original_verification_sha256=sha(HERE/'VERIFICATION.json'),
              cleanup_manifest_sha256=sha(HERE/'CACHE-CLEANUP.json'))
(HERE/'VERIFICATION-AFTER-CLEANUP.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('dependency_audits','attempts')},indent=2))
