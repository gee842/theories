#!/usr/bin/env python3
"""Check the costed carrier/probe continuation without replacing prior receipts."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
LEAN=Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
CORE=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean'

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    inputs=[CORE,HERE/'RecursiveSelection.lean',HERE/'CarrierDiagnosis.lean']
    sources={p.name:p.read_bytes() for p in inputs}
    for name,b in sources.items():
        s=b.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b',s),name
        assert not re.search(r'^\s*(axiom|constant)\s',s,re.M),name
    version=subprocess.check_output([str(LEAN),'--version'],text=True).strip()
    assert 'version 4.29.1,' in version
    names=re.findall(r'^(?:theorem|def|structure|inductive)\s+(\w+)',sources['CarrierDiagnosis.lean'].decode(),re.M)
    inherited=re.findall(r'^(?:theorem|def|structure|inductive)\s+(\w+)',sources['RecursiveSelection.lean'].decode(),re.M)
    audit='import CarrierDiagnosis\n'+''.join(f'#print axioms CarrierDiagnosis.{n}\n' for n in names)
    iaudit='import RecursiveSelection\n'+''.join(f'#print axioms RecursiveSelection.{n}\n' for n in inherited)
    logs={}
    with tempfile.TemporaryDirectory(prefix='meta-carrier-') as td:
        build=Path(td)
        for name,b in sources.items():(build/name).write_bytes(b)
        (build/'CarrierAudit.lean').write_text(audit)
        (build/'InheritedAudit.lean').write_text(iaudit)
        env=dict(os.environ,LEAN_PATH=td)
        for module in ['GenerativeCore','RecursiveSelection','CarrierDiagnosis','CarrierAudit','InheritedAudit']:
            p=subprocess.run([str(LEAN),'-o',module+'.olean',module+'.lean'],cwd=build,env=env,text=True,capture_output=True,timeout=180)
            logs[module]=p.stdout+p.stderr
            if p.returncode or 'warning:' in logs[module]:
                print(logs[module]);raise SystemExit(module+' failed or warned')
    pattern=r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
    audits=re.findall(pattern,logs['CarrierAudit'])
    iaudits=re.findall(pattern,logs['InheritedAudit'])
    assert [n for n,_ in audits]==['CarrierDiagnosis.'+n for n in names]
    assert [n for n,_ in iaudits]==['RecursiveSelection.'+n for n in inherited]
    for _,group in audits+iaudits:
        assert set(a.strip() for a in group.split(',') if a.strip()) <= {'propext','Quot.sound','Classical.choice'}
    assert all(p.read_bytes()==sources[p.name] for p in inputs)
    out=HERE/'carrier-verification';out.mkdir(exist_ok=True)
    for name,b in sources.items():(out/name).write_bytes(b)
    (out/'CarrierAudit.lean').write_text(audit)
    (out/'InheritedAudit.lean').write_text(iaudit)
    for name,log in logs.items():(out/(name+'.txt')).write_text(log)
    result={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),
            'version':version,'compiler_sha256':sha(LEAN.read_bytes()),
            'checker_sha256':sha(Path(__file__).read_bytes()),
            'sources':{n:sha(b) for n,b in sources.items()},
            'theorems':re.findall(r'^theorem\s+(\w+)',sources['CarrierDiagnosis.lean'].decode(),re.M),
            'new_audits':dict(audits),'inherited_audits':dict(iaudits),
            'log_hashes':{n:sha(log.encode()) for n,log in logs.items()},
            'scope':'Conditional heterogeneous carrier recurrence, actual material/funding accounts, receipt-based probe and repair. No empirical validation.'}
    (HERE/'carrier-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','new_theorems':len(result['theorems']),
                      'new_audits':len(audits),'inherited_audits':len(iaudits)}))

if __name__=='__main__':main()
