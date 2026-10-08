#!/usr/bin/env python3
"""Check mutual reproduction and changing admission on actual frozen sources."""
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
LEAN = Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
CORE = ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    paths = [CORE, HERE/'ReproductionNetwork.lean']
    sources = {p.name:p.read_bytes() for p in paths}
    for name, data in sources.items():
        code = data.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', code), name
        assert not re.search(r'^\s*(axiom|constant)\s', code, re.M), name
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    code = sources['ReproductionNetwork.lean'].decode()
    names = re.findall(r'^(?:theorem|def|structure|inductive)\s+(\w+)', code, re.M)
    audit = 'import ReproductionNetwork\n'+''.join(
        f'#print axioms ReproductionNetwork.{name}\n' for name in names)
    logs = {}
    with tempfile.TemporaryDirectory(prefix='meta-reproduction-') as td:
        build = Path(td)
        for name, data in sources.items():
            (build/name).write_bytes(data)
        (build/'ReproductionAudit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=td)
        for module in ['GenerativeCore', 'ReproductionNetwork', 'ReproductionAudit']:
            p = subprocess.run([str(LEAN), '-o', module+'.olean', module+'.lean'],
                               cwd=build, env=env, text=True, capture_output=True, timeout=180)
            logs[module] = p.stdout+p.stderr
            if p.returncode or 'warning:' in logs[module]:
                print(logs[module])
                raise SystemExit(module+' failed or warned')
    pattern = r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
    audits = re.findall(pattern, logs['ReproductionAudit'])
    assert [n for n,_ in audits] == ['ReproductionNetwork.'+n for n in names]
    for _, group in audits:
        assert {a.strip() for a in group.split(',') if a.strip()} <= {
            'propext', 'Classical.choice', 'Quot.sound'}
    assert all(p.read_bytes() == sources[p.name] for p in paths)
    out = HERE/'reproduction-verification'
    out.mkdir(exist_ok=True)
    for name, data in sources.items():
        (out/name).write_bytes(data)
    (out/'ReproductionAudit.lean').write_text(audit)
    for name, log in logs.items():
        (out/(name+'.txt')).write_text(log)
    result = {
        'status':'passed', 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'version':version, 'compiler_sha256':sha(LEAN.read_bytes()),
        'checker_sha256':sha(Path(__file__).read_bytes()),
        'sources':{n:sha(b) for n,b in sources.items()},
        'theorems':re.findall(r'^theorem\s+(\w+)', code, re.M),
        'new_audits':dict(audits),
        'log_hashes':{n:sha(log.encode()) for n,log in logs.items()},
        'scope':'Conditional finite role networks, establishment, coupling, costed revision, material-retention rival and state-dependent admission. Supplied laws and repertoire; no empirical or normative validation.'}
    (HERE/'reproduction-verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':'passed','theorems':len(result['theorems']),
                      'new_audits':len(audits)}))


if __name__ == '__main__':
    main()
