#!/usr/bin/env python3
"""Freeze and kernel-check the recurrence study with its actual core import."""
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
CORE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean'
LEAN = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    inputs = [CORE, HERE.parent/'formal/MarketGenerativity.lean', HERE/'RecursiveSelection.lean', HERE/'MarketDiagnosis.lean']
    sources = {p.name: p.read_bytes() for p in inputs}
    text = sources['RecursiveSelection.lean'].decode() + sources['MarketDiagnosis.lean'].decode()
    assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text)
    assert not re.search(r'^\s*(axiom|constant)\s', text, re.M)
    names = []
    for module in ['RecursiveSelection', 'MarketDiagnosis']:
        names.extend(module+'.'+n for n in re.findall(r'^(?:theorem|def|structure)\s+(\w+)', sources[module+'.lean'].decode(), re.M))
    theorems = re.findall(r'^theorem\s+(\w+)', text, re.M)
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    audit = 'import RecursiveSelection\nimport MarketDiagnosis\n' + ''.join(
        f'#print axioms {n}\n' for n in names)
    all_logs = {}
    with tempfile.TemporaryDirectory(prefix='meta-attractor-lean-') as td:
        build = Path(td)
        for name, b in sources.items():
            (build / name).write_bytes(b)
        (build / 'Audit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=td)
        for module in ['GenerativeCore', 'MarketGenerativity', 'RecursiveSelection', 'MarketDiagnosis', 'Audit']:
            p = subprocess.run([str(LEAN), '-o', module + '.olean', module + '.lean'],
                               cwd=build, env=env, text=True, capture_output=True, timeout=180)
            all_logs[module] = p.stdout + p.stderr
            if p.returncode or 'warning:' in all_logs[module]:
                print(all_logs[module])
                raise SystemExit(f'{module} failed or warned; no passing receipt written')
    audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", all_logs['Audit'])
    assert [n for n, _ in audits] == names
    axioms = sorted({a.strip() for _, group in audits for a in group.split(',') if a.strip()})
    assert set(axioms) <= {'propext', 'Classical.choice', 'Quot.sound'}
    assert all(p.read_bytes() == sources[p.name] for p in inputs)
    out = HERE/'verification'
    out.mkdir(exist_ok=True)
    for name, b in sources.items():
        (out/name).write_bytes(b)
    (out/'Audit.lean').write_text(audit)
    for name, log in all_logs.items():
        (out/(name+'.txt')).write_text(log)
    receipt = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'passed', 'version': version, 'compiler': str(LEAN),
        'compiler_sha256': sha(LEAN.read_bytes()),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'sources': {n: sha(b) for n, b in sources.items()},
        'theorems': theorems, 'theorem_count': len(theorems),
        'audited_declarations': [n for n, _ in audits], 'audit_count': len(audits),
        'axioms': axioms, 'per_declaration_axioms': dict(audits),
        'logs': {n: sha(log.encode()) for n, log in all_logs.items()},
        'scope': 'Conditional threshold recurrence, actual core traces, carrier turnover, finite supply failure, exact basin, intervention budget and passive nonidentification. No empirical fit or market refinement.'
    }
    (HERE/'verification.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k: receipt[k] for k in ['status','theorem_count','audit_count','axioms']}))


if __name__ == '__main__':
    main()
