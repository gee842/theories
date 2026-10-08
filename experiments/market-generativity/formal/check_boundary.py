#!/usr/bin/env python3
"""Freeze and kernel-check the market boundary extension and its actual import."""
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
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    paths = [HERE/'MarketGenerativity.lean', HERE/'RegimeBoundary.lean']
    sources = {p.name: p.read_bytes() for p in paths}
    for name, raw in sources.items():
        code = raw.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', code), name
        assert not re.search(r'^\s*(axiom|constant)\s', code, re.M), name
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    code = sources['RegimeBoundary.lean'].decode()
    names = re.findall(r'^(?:theorem|def|abbrev|structure|inductive)\s+(\w+)', code, re.M)
    inherited = re.findall(r'^theorem\s+(\w+)', sources['MarketGenerativity.lean'].decode(), re.M)
    audit = 'import RegimeBoundary\n' + ''.join(
        f'#print axioms RegimeBoundary.{name}\n' for name in names)
    logs = {}
    with tempfile.TemporaryDirectory(prefix='market-boundary-check-') as td:
        build = Path(td)
        for name, data in sources.items():
            (build/name).write_bytes(data)
        (build/'BoundaryAudit.lean').write_text(audit)
        for module in ['MarketGenerativity', 'RegimeBoundary', 'BoundaryAudit']:
            p = subprocess.run([str(LEAN), '-o', module+'.olean', module+'.lean'],
                               cwd=build, env=dict(os.environ, LEAN_PATH=td),
                               text=True, capture_output=True, timeout=180)
            logs[module] = p.stdout+p.stderr
            if p.returncode or 'warning:' in logs[module]:
                print(logs[module])
                raise SystemExit(module+' failed or warned')
    pattern = r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
    audits = re.findall(pattern, logs['BoundaryAudit'])
    old_audits = re.findall(pattern, logs['MarketGenerativity'])
    assert [n for n, _ in audits] == ['RegimeBoundary.'+n for n in names]
    assert [n for n, _ in old_audits] == ['MarketGenerativity.'+n for n in inherited]
    for _, group in audits+old_audits:
        assert {a.strip() for a in group.split(',') if a.strip()} <= ALLOWED
    assert all(p.read_bytes() == sources[p.name] for p in paths)
    out = HERE/'boundary-verification'
    out.mkdir(exist_ok=True)
    for name, data in sources.items():
        (out/name).write_bytes(data)
    (out/'BoundaryAudit.lean').write_text(audit)
    for name, log in logs.items():
        (out/(name+'.txt')).write_text(log)
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'version': version, 'compiler_sha256': sha(LEAN.read_bytes()),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'sources': {n: sha(b) for n, b in sources.items()},
        'theorems': re.findall(r'^theorem\s+(\w+)', code, re.M),
        'new_audits': dict(audits), 'inherited_audits': dict(old_audits),
        'log_hashes': {n: sha(log.encode()) for n, log in logs.items()},
        'scope': 'Exact rational uniform selection-floor protection (including bounded error), '
                 'existence boundary for positive-width low-selection certificates, '
                 'one-step and all-time closure in the paid, authorized, operating projection, '
                 'strict renewing-share decline while positive, and three parameter witnesses. '
                 'Supplied market laws and correspondence; no full basin, limit, spectral '
                 'bifurcation, inevitable collapse, empirical calibration or ethical axiom proof.'}
    (HERE/'boundary-verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'new_theorems': len(result['theorems']),
                      'new_audits': len(audits), 'inherited_audits': len(old_audits)}))


if __name__ == '__main__':
    main()
