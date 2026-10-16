"""Independent scratch compilation; preserve logs, never olean/build products.
Uses the inspected author checker's source-closure parser, not its main runner.
Reuses pinned upstream caches; does not claim hermetic toolchain attestation.
"""
from pathlib import Path
import datetime, hashlib, importlib.util, json, os, subprocess, tempfile
OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if (p / 'RESEARCH.md').is_file())
HERE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
checker = HERE / 'check_measured_feedback.py'
spec = importlib.util.spec_from_file_location('author_parser', checker)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
sources = m.closure()
names = [d['name'] for s in sources for d in s['declarations']]
project = Path.home() / 'repos/生生不息'
manifest = json.loads((project / 'lake-manifest.json').read_text())
packages = project / manifest.get('packagesDir', '.lake/packages')
libs = sorted(p / '.lake/build/lib/lean' for p in packages.iterdir() if (p / '.lake/build/lib/lean').is_dir())
version = subprocess.check_output([str(m.LEAN), '--version'], text=True).strip()
assert 'version 4.30.0-rc2,' in version
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=packages/'mathlib', text=True).strip()
assert revision == 'ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa'
audit = 'import MeasuredFeedback\n' + '\n'.join('#print axioms ' + n for n in names) + '\n'
(OUT / 'Audit.lean').write_text(audit)
commands = []
with tempfile.TemporaryDirectory(prefix='independent-inquiry-review-') as td:
    stage = Path(td)
    env = dict(os.environ, LEAN_PATH=':'.join([td] + [str(p) for p in libs]))
    for s in sources:
        (stage / (s['module'] + '.lean')).write_bytes(s['data'])
    def execute(args, log):
        commands.append([str(m.LEAN)] + args)
        p = subprocess.run([str(m.LEAN)] + args, cwd=stage, env=env, capture_output=True, text=True, timeout=300)
        text = p.stdout + p.stderr
        (OUT / log).write_text(text)
        assert p.returncode == 0 and 'warning:' not in text and 'error:' not in text, (log, text)
        return text
    for s in sources:
        execute(['-o', s['module'] + '.olean', s['module'] + '.lean'], s['module'] + '.txt')
        print(s['module'] + ' compiled', flush=True)
    (stage / 'Audit.lean').write_text(audit)
    result = m.AUDIT.findall(execute(['Audit.lean'], 'axioms.txt'))
    assert [n for n, _ in result] == names
    dependencies = {n: [a.strip() for a in deps.split(',') if a.strip()] for n, deps in result}
    assert all(set(a) <= m.ALLOWED for a in dependencies.values())
    assert all(s['path'].read_bytes() == s['data'] for s in sources)
r = json.loads((HERE / 'measured-feedback-verification.json').read_text())
snap = ROOT / r['snapshot']
for s in r['modules']:
    assert sha(ROOT / s['source']) == s['source_sha256']
    assert sha(snap / 'sources' / (s['module'] + '.lean')) == s['source_sha256']
assert sha(checker) == r['checker_sha256']
assert sha(m.LEAN.resolve()) == r['compiler_sha256']
assert json.loads((snap / 'verification.json').read_text()) == r
for k, v in r['log_sha256'].items():
    assert sha(snap / k) == v
assert sha(project / 'lake-manifest.json') == r['manifest_sha256']
assert sha(snap / 'lake-manifest.json') == r['manifest_sha256']
for k, v in r['direct_import_sha256'].items():
    if Path(k).is_absolute():
        assert sha(Path(k)) == v
receipt = {
    'status': 'passed', 'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'version': version, 'executable_sha256': sha(m.LEAN.resolve()), 'mathlib_revision': revision,
    'source_sha256': {s['module']: hashlib.sha256(s['data']).hexdigest() for s in sources},
    'checker_sha256': sha(checker), 'review_script_sha256': sha(Path(__file__)),
    'author_snapshot': r['snapshot'], 'author_receipt_sha256': sha(HERE / 'measured-feedback-verification.json'),
    'audits': len(names), 'new_theorems': r['new_theorems'], 'new_audits': r['new_audits'],
    'axiom_dependencies': dependencies, 'commands': commands,
    'log_sha256': {p.name: sha(p) for p in OUT.glob('*.txt')}, 'audit_source_sha256': sha(OUT / 'Audit.lean'),
    'scope': 'All five repository modules independently compiled from current source in scratch; complete explicit-declaration axiom audit. Existing upstream cache reused. Executable hash does not fingerprint the full linked compiler runtime; no hermetic attestation. Author closure parser reused; author main runner not invoked. No proof of ethical premise warrant or empirical applicability.'
}
(OUT / 'verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({k: receipt[k] for k in ['status', 'audits', 'new_theorems', 'new_audits', 'checked_at_utc']}))
