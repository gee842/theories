#!/usr/bin/env python3
"""Check source in an isolated pinned Lean build and audit every declaration."""
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'LifecycleCorrespondence.lean'
TOOLCHAIN='leanprover/lean4:v4.29.1'

def sha(x):return hashlib.sha256(x).hexdigest()

def main():
    raw=SOURCE.read_bytes()
    code=re.sub(r'/-.*?-/|--[^\n]*','',raw.decode(),flags=re.S)
    assert re.findall(r'^import\s+(\S+)',code,re.M)==['Std']
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|skipKernelTC',code)
    names=['LifecycleCorrespondence.'+n for n in re.findall(r'^(?:def|theorem)\s+(\w+)',code,re.M)]
    theorems=re.findall(r'^theorem\s+(\w+)',code,re.M)
    audit=('import LifecycleCorrespondence\n\n'+'\n'.join('#print axioms '+n for n in names)+'\n').encode()
    files={'LifecycleCorrespondence.lean':raw,'LifecycleCorrespondenceAudit.lean':audit,'lean-toolchain':(TOOLCHAIN+'\n').encode()}
    logs={};commands=[]
    with tempfile.TemporaryDirectory(prefix='lifecycle-correspondence-') as temp:
        stage=Path(temp)
        for name,b in files.items():(stage/name).write_bytes(b)
        env=dict(os.environ,LEAN_PATH=str(stage))
        def run(args,name):
            cmd=[str(Path.home()/'.elan/bin/lean'),'+'+TOOLCHAIN]+args;commands.append(cmd)
            r=subprocess.run(cmd,cwd=stage,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=120)
            logs[name]=r.stdout
            assert r.returncode==0 and 'warning:' not in r.stdout and 'error:' not in r.stdout,r.stdout
            return r.stdout
        version=run(['--version'],'version.txt').strip()
        run(['-o','LifecycleCorrespondence.olean','LifecycleCorrespondence.lean'],'compiler.txt')
        out=run(['LifecycleCorrespondenceAudit.lean'],'axioms.txt')
    parsed=re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])",out,re.S)
    assert [n for n,_ in parsed]==names
    dependencies={n:[v.strip() for v in a.split(',') if v.strip()] for n,a in parsed}
    assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in dependencies.values())
    assert SOURCE.read_bytes()==raw
    (HERE/'sources').mkdir(exist_ok=True)
    for n,b in files.items():(HERE/'sources'/n).write_bytes(b)
    for n,b in logs.items():(HERE/n).write_text(b)
    receipt={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'version':version,
             'toolchain':TOOLCHAIN,'fresh_temporary_build':True,'commands':commands,
             'new_theorem_count':len(theorems),'declaration_audit_count':len(names),
             'axiom_dependencies':dependencies,'checker_sha256':sha(Path(__file__).read_bytes()),
             'source_sha256':{n:sha(b) for n,b in files.items()},'log_sha256':{n:sha(b.encode()) for n,b in logs.items()},
             'scope':'Rational joint-outcome and conditional-stage algebra, plus source-count witnesses. Independence, biological causality, data extraction and experimental correspondence are not proved.'}
    (HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','new_theorem_count','declaration_audit_count']},indent=2))

if __name__=='__main__':main()
