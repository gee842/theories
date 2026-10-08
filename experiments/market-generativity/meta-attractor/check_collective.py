#!/usr/bin/env python3
"""Check only this study, with frozen source and per-declaration Lean audits."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
LEAN = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    source = HERE / 'CollectiveDestruction.lean'
    frozen = source.read_bytes()
    txt = frozen.decode()
    assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', txt)
    assert not re.search(r'^\s*(axiom|constant)\s', txt, re.M)
    names = re.findall(r'^(?:theorem|def|structure)\s+(\w+)', txt, re.M)
    theorems = re.findall(r'^theorem\s+(\w+)', txt, re.M)
    audit = 'import CollectiveDestruction\n' + ''.join(
        f'#print axioms CollectiveDestruction.{name}\n' for name in names)
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    logs = {}
    with tempfile.TemporaryDirectory(prefix='collective-destruction-') as td:
        build = Path(td)
        (build / source.name).write_bytes(frozen)
        (build / 'Audit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=td)
        for module in ['CollectiveDestruction', 'Audit']:
            p = subprocess.run([str(LEAN), '-o', module + '.olean', module + '.lean'],
                               cwd=build, env=env, text=True, capture_output=True, timeout=120)
            logs[module] = p.stdout + p.stderr
            if p.returncode or 'warning:' in logs[module]:
                raise RuntimeError(logs[module])
    audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", logs['Audit'])
    assert [n for n, _ in audits] == ['CollectiveDestruction.' + n for n in names]
    axioms = sorted({a.strip() for _, group in audits for a in group.split(',') if a.strip()})
    assert set(axioms) <= {'propext', 'Classical.choice', 'Quot.sound'}
    assert source.read_bytes() == frozen
    out = HERE / 'collective-verification'
    out.mkdir(exist_ok=True)
    (out / source.name).write_bytes(frozen)
    (out / 'Audit.lean').write_text(audit)
    for name, log in logs.items():
        (out / (name + '.txt')).write_text(log)
    receipt = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'version': version, 'compiler': str(LEAN), 'compiler_sha256': sha(LEAN.read_bytes()),
        'source_sha256': sha(frozen), 'checker_sha256': sha(Path(__file__).read_bytes()),
        'theorems': theorems, 'theorem_count': len(theorems),
        'audit_count': len(audits), 'per_declaration_axioms': dict(audits), 'axioms': axioms,
        'logs': {n: sha(log.encode()) for n, log in logs.items()},
        'scope': 'Exact stage optimization, joint loss, finite attraction for arbitrary positive throughput schedules, exact basin for declared tie-break, strict protection, rank and invariance certificates. No empirical correspondence, long-horizon equilibrium, endogenous capability growth or carrier-replacement theorem.'
    }
    (HERE / 'collective-verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ['status', 'theorem_count', 'audit_count', 'axioms']}))


if __name__ == '__main__':
    main()
