#!/usr/bin/env python3
"""Check legacy corrections and the joined formation/revision history on frozen sources."""
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
    formation = ROOT/'experiments/shared-renewal-capability/regulation/retention/formation'
    paths = [CORE, formation/'formal/FormedSelection.lean', formation/'selectors/formal/SelectorRevision.lean', formation/'selectors/updaters/formal/UpdaterFormation.lean', HERE/'LegacyReconciliation.lean', HERE/'CommonOrganization.lean']
    sources = {p.name:p.read_bytes() for p in paths}
    for name, data in sources.items():
        code = re.sub(r'/\-.*?\-/', '', data.decode(), flags=re.S)
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', code), name
        assert not re.search(r'^\s*(axiom|constant)\s', code, re.M), name
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    new_modules = ['LegacyReconciliation','CommonOrganization']
    codes = {m:re.sub(r'/\-.*?\-/', '', sources[m+'.lean'].decode(), flags=re.S) for m in new_modules}
    names = [m+'.'+n for m,code in codes.items() for n in re.findall(r'^(?:theorem|def|abbrev|structure|inductive|instance)\s+(\w+)', code, re.M)]
    inherited = [m+'.'+n for m in ['GenerativeCore','FormedSelection','SelectorRevision','UpdaterFormation']
                 for n in re.findall(r'^theorem\s+(\w+)', sources[m+'.lean'].decode(), re.M)]
    inherited = [n.replace('GenerativeCore.','Generative.') for n in inherited]
    audit = 'import LegacyReconciliation\nimport CommonOrganization\n'+''.join(
        f'#print axioms {name}\n' for name in names+inherited)
    logs = {}
    with tempfile.TemporaryDirectory(prefix='meta-reconciliation-') as td:
        build = Path(td)
        for name, data in sources.items():
            (build/name).write_bytes(data)
        (build/'ReconciliationAudit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=td)
        for module in ['GenerativeCore','FormedSelection','SelectorRevision','UpdaterFormation','LegacyReconciliation','CommonOrganization','ReconciliationAudit']:
            p = subprocess.run([str(LEAN), '-o', module+'.olean', module+'.lean'],
                               cwd=build, env=env, text=True, capture_output=True, timeout=180)
            logs[module] = p.stdout+p.stderr
            if p.returncode or 'warning:' in logs[module]:
                print(logs[module])
                raise SystemExit(module+' failed or warned')
    pattern = r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
    audits = re.findall(pattern, logs['ReconciliationAudit'])
    assert [n for n,_ in audits] == names+inherited
    for _, group in audits:
        assert {a.strip() for a in group.split(',') if a.strip()} <= {
            'propext', 'Classical.choice', 'Quot.sound'}
    assert all(p.read_bytes() == sources[p.name] for p in paths)
    out = HERE/'reconciliation-verification'
    out.mkdir(exist_ok=True)
    for name, data in sources.items():
        (out/name).write_bytes(data)
    (out/'ReconciliationAudit.lean').write_text(audit)
    for name, log in logs.items():
        (out/(name+'.txt')).write_text(log)
    result = {
        'status':'passed', 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'version':version, 'compiler_sha256':sha(LEAN.read_bytes()),
        'checker_sha256':sha(Path(__file__).read_bytes()),
        'sources':{n:sha(b) for n,b in sources.items()},
        'source_paths':{p.name:str(p.relative_to(ROOT)) for p in paths},
        'theorems':{m:re.findall(r'^theorem\s+(\w+)', code, re.M) for m,code in codes.items()},
        'new_audits':{n:a for n,a in audits if n in names},
        'inherited_audits':{n:a for n,a in audits if n in inherited},
        'log_hashes':{n:sha(log.encode()) for n,log in logs.items()},
        'scope':'Exact finite-dimensional algebraic corrections; one paid history from native component formation through regulation, acquired updater choice and further revision; general paid trace accounting and conditional revision availability. No continuous-time convergence theorem, spontaneous schedule, derived retooling chemistry, unlimited support, empirical correspondence or ethical warrant is established.'}
    (HERE/'reconciliation-verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':'passed','theorems':sum(map(len,result['theorems'].values())),
                      'new_audits':len(names), 'inherited_audits':len(inherited)}))


if __name__ == '__main__':
    main()
