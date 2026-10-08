#!/usr/bin/env python3
"""Freeze, compile and audit finite-support market obstruction proofs."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
LEAN = Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def declarations(code):
    return re.findall(r'^(?:theorem|def|abbrev|structure|inductive)\s+(\w+)', code, re.M)


def main():
    modules = ['MarketGenerativity', 'RegimeBoundary', 'RegimeAttraction', 'RegimeTransition', 'FiniteSupportObstruction']
    sources = {name: (HERE/(name+'.lean')).read_bytes() for name in modules}
    for name, raw in sources.items():
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', raw.decode()), name
        assert not re.search(r'^\s*(axiom|constant)\s', raw.decode(), re.M), name
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    new_names = ['FiniteSupportObstruction.'+n for n in declarations(sources['FiniteSupportObstruction'].decode())]
    boundary_names = [name+'.'+n for name in modules[1:4] for n in declarations(sources[name].decode())]
    market_names = ['MarketGenerativity.'+n for n in re.findall(
        r'^theorem\s+(\w+)', sources['MarketGenerativity'].decode(), re.M)]
    audit = 'import FiniteSupportObstruction\n'+''.join(
        '#print axioms '+name+'\n' for name in boundary_names+new_names)
    logs = {}
    with tempfile.TemporaryDirectory(prefix='market-finite-support-check-') as td:
        build = Path(td)
        for name, raw in sources.items():
            (build/(name+'.lean')).write_bytes(raw)
        (build/'FiniteSupportAudit.lean').write_text(audit)
        for name in modules+['FiniteSupportAudit']:
            p = subprocess.run([str(LEAN), '-o', name+'.olean', name+'.lean'],
                               cwd=build, env=dict(os.environ, LEAN_PATH=td),
                               capture_output=True, text=True, timeout=180)
            logs[name] = p.stdout+p.stderr
            if p.returncode or 'warning:' in logs[name]:
                print(logs[name])
                raise SystemExit(name+' failed or warned')
    pattern = r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
    audit_rows = re.findall(pattern, logs['FiniteSupportAudit'])
    old_rows = re.findall(pattern, logs['MarketGenerativity'])
    assert [n for n, _ in audit_rows] == boundary_names+new_names
    assert [n for n, _ in old_rows] == market_names
    for _, group in audit_rows+old_rows:
        assert {v.strip() for v in group.split(',') if v.strip()} <= ALLOWED
    assert all((HERE/(name+'.lean')).read_bytes() == raw for name, raw in sources.items())
    out = HERE/'finite-support-verification'
    out.mkdir(exist_ok=True)
    for name, raw in sources.items():
        (out/(name+'.lean')).write_bytes(raw)
    (out/'FiniteSupportAudit.lean').write_text(audit)
    for name, log in logs.items():
        (out/(name+'.txt')).write_text(log)
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'version': version, 'compiler_sha256': sha(LEAN.read_bytes()),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'sources': {name+'.lean': sha(raw) for name, raw in sources.items()},
        'theorems': re.findall(r'^theorem\s+(\w+)', sources['FiniteSupportObstruction'].decode(), re.M),
        'new_audits': {n: v for n, v in audit_rows if n in new_names},
        'inherited_audits': dict(old_rows+[(n, v) for n, v in audit_rows if n in boundary_names]),
        'inherited_theorems': {name: re.findall(r'^theorem\s+(\w+)', sources[name].decode(), re.M)
                               for name in modules[:4]},
        'log_hashes': {name: sha(log.encode()) for name, log in logs.items()},
        'scope': 'For each finite initial essential stock at least five, an explicit positive '
                 'seed interval fails within a finite horizon under every time-varying beta and '
                 'quality error schedule and every nonnegative stock shock. The inherited share '
                 'growth and support laws stay fixed; there is no direct entry or stock injection. '
                 'The same positive seed has projected finite recovery under the original zero-beta '
                 'pulse while its full guarded history terminates. Not an exact viability kernel, '
                 'a physical extinction theorem, or a zero-substantive-axiom foundation.'}
    (HERE/'finite-support-verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'new_theorems': len(result['theorems']),
                      'new_audits': len(result['new_audits']),
                      'inherited_theorems': sum(map(len, result['inherited_theorems'].values())),
                      'inherited_audits': len(result['inherited_audits'])}))


if __name__ == '__main__':
    main()
