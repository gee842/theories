#!/usr/bin/env python3
"""Freeze dependencies; compile two population modules; audit every declaration."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LEAN = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
MODULES = {
    'CorrectionDependence': HERE / 'CorrectionDependence.lean',
    'CorrectionCommitment': HERE / 'CorrectionCommitment.lean',
}
NEW = ['CorrectionCommitment']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    frozen = {n: p.read_bytes() for n, p in MODULES.items()}
    declarations, theorems = {}, {}
    for n, raw in frozen.items():
        txt = raw.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', txt)
        assert not re.search(r'^\s*(axiom|constant)\s', txt, re.M)
        if n in NEW:
            declarations[n] = re.findall(r'^(?:theorem|def|structure)\s+(\w+)', txt, re.M)
            theorems[n] = re.findall(r'^theorem\s+(\w+)', txt, re.M)
    names = [n + '.' + d for n in NEW for d in declarations[n]]
    audit = 'import CorrectionCommitment\n' + ''.join(f'#print axioms {n}\n' for n in names)
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    logs = {}
    with tempfile.TemporaryDirectory(prefix='correction-commitment-') as td:
        build = Path(td)
        for name, raw in frozen.items():
            (build / (name + '.lean')).write_bytes(raw)
        (build / 'Audit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=td)
        for name in [*MODULES, 'Audit']:
            p = subprocess.run([str(LEAN), '-o', name + '.olean', name + '.lean'],
                               cwd=build, env=env, capture_output=True, text=True, timeout=180)
            logs[name] = p.stdout + p.stderr
            if p.returncode or 'warning:' in logs[name]:
                raise RuntimeError(name + '\n' + logs[name])
    audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", logs['Audit'])
    assert [n for n, _ in audits] == names
    axioms = sorted({a.strip() for _, group in audits for a in group.split(',') if a.strip()})
    assert set(axioms) <= {'propext', 'Classical.choice', 'Quot.sound'}
    for n, p in MODULES.items():
        assert p.read_bytes() == frozen[n], 'Source changed during build: ' + n
    out = HERE / 'correction-commitment-verification'
    out.mkdir(exist_ok=True)
    for name, raw in frozen.items():
        (out / (name + '.lean')).write_bytes(raw)
    (out / 'Audit.lean').write_text(audit)
    for name, log in logs.items():
        (out / (name + '.txt')).write_text(log)
    receipt = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'version': version, 'compiler': str(LEAN), 'compiler_sha256': sha(LEAN.read_bytes()),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'sources': {n: {'path': str(p.relative_to(ROOT)), 'sha256': sha(frozen[n]),
                         'role': 'new module' if n in NEW else 'inherited dependency'} for n, p in MODULES.items()},
        'theorems': theorems, 'theorem_count': sum(map(len, theorems.values())),
        'audit_count': len(audits), 'per_declaration_axioms': dict(audits), 'axioms': axioms,
        'logs': {n: sha(log.encode()) for n, log in logs.items()},
        'scope': 'Actual posted-stake settlement, exact audit-separation threshold for all optimizing plans in the inherited correction model, finite-capacity implementability, independent exit provision, false positives and coalition/custody failures. Supplied linear task preferences, lottery, classification, protected custody and participation; not intrinsic motivation or general self-modification stability.'
    }
    (HERE / 'correction-commitment-verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ['status', 'theorem_count', 'audit_count', 'axioms']}))


if __name__ == '__main__':
    main()
