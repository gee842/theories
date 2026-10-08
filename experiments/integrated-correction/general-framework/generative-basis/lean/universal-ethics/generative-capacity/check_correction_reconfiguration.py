#!/usr/bin/env python3
"""Fresh kernel audits plus independently expressed finite execution comparisons."""
from datetime import datetime, timezone
import hashlib
import itertools
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
import check as scanner

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
LEAN = Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
NEW = ['CorrectionReconfiguration']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','CorrectionReconfigurationCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

def cert(roster_mask,envelope,support):
    # Set arithmetic, independently expressed from Lean's nested list traversal.
    return bool(envelope) and all((support & roster_mask & ~bad) != 0 for bad in envelope)

def reference_rows():
    # Truth-table composition, independent of Lean's recursive expression evaluation.
    atoms=[sum(1<<mask for mask in range(16) if mask & (1<<i)) for i in range(4)]
    base=atoms[:3]+[v for x in atoms[:3] for y in atoms[:3] for v in [x|y,x&y]]
    formulas=base+[v for x in base for v in [x|atoms[3],x&atoms[3]]]
    for i,table in enumerate(formulas):
        for mask in range(16): yield [0,i,mask,(table>>mask)&1]
        for x in range(16):
            for y in range(16):
                if x & ~y == 0 and (table>>x)&1: assert (table>>y)&1
    for code,family in itertools.product(range(64),range(16)):
        owners=[code//(4**d)%4 for d in range(3)]
        faults=[sum(1<<d for d,r in enumerate(owners) if r==cause)
            for cause in range(4) if family & (1<<cause)]
        ready=bool(faults) and all((7 & ~(x|y))!=0 for x in faults for y in faults)
        for support in range(8): yield [1,code,family,support,int(ready),int(cert(7,faults,support))]
        for actual in range(16):
            exposed=sum(1<<d for d,r in enumerate(owners) if actual & (1<<r))
            available=cert(7,faults,7 & ~exposed)
            covered=any(actual & ~(1<<r)==0 for r in range(4) if family & (1<<r))
            if covered and ready: assert available
            if covered:
                for support in range(8):
                    if support & ~exposed == 0: assert not cert(7,faults,support)
            yield [2,code,family,actual,exposed,int(available)]
    for scheme,auth,cost,depth,fuel,deadline in itertools.product(range(4),range(2),range(4),range(4),range(21),[5,13,20]):
        n=3 if scheme<2 else 4
        ready=scheme in (0,2)
        admitted=bool(auth) and ready and cost+n*(depth+2)+3<=min(fuel,deadline)
        yield [3,scheme,auth,cost,depth,fuel,deadline,int(admitted),fuel-cost if admitted else fuel,
               cost if admitted else 0,8 if admitted else 7,1 if admitted else 0]

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'correction-reconfiguration-checks'/stamp
    out.mkdir(parents=True)
    source_bytes={m:p.read_bytes() for m,p in SOURCES.items()}
    helpers={p.name:p.read_bytes() for p in [Path(__file__),HERE/'check.py']}
    for m,b in source_bytes.items(): (out/(m+'.lean')).write_bytes(b)
    for name,b in helpers.items(): (out/name).write_bytes(b)
    registry={}
    for m in NEW:
        source=source_bytes[m].decode()
        imports=re.findall(r'^import (.+)$',scanner.code_only(source),re.M)
        assert all(x in SOURCES or x=='Std' for x in imports),imports
        registry[m]=scanner.declarations(re.sub(r'^import .+$','import Std',source,flags=re.M))
    receipt={'status':'checking','utc':stamp,'retained_run':str(out.relative_to(HERE)),
        'compiler_sha256':sha(LEAN.read_bytes()),
        'sources':{m:{'path':str(SOURCES[m].relative_to(ROOT)),'sha256':sha(b)} for m,b in source_bytes.items()},
        'checker_sha256':{n:sha(b) for n,b in helpers.items()},
        'scope':'Computed fault envelopes from supplied monotone causal formulas; atomic authorized reviewer reconfiguration preserving mandate, revoking old requests and reserving correction capacity. Physical causal correspondence, root fault coverage, protected monitor and reorganization authority remain supplied; no distributed reconfiguration or ethical legitimacy theorem.'}
    try:
        with tempfile.TemporaryDirectory(prefix='correction-reconfiguration-') as td:
            work=Path(td); env=dict(os.environ,LEAN_PATH=td)
            for m,b in source_bytes.items(): (work/(m+'.lean')).write_bytes(b)
            def run(args,name):
                p=subprocess.run([str(LEAN)]+args,cwd=work,env=env,text=True,capture_output=True,timeout=180)
                log=p.stdout+p.stderr; (out/(name+'.log')).write_text(log)
                assert p.returncode==0 and not re.search(r'\b(?:error|warning):',log),log
                return log
            receipt['version']=run(['--version'],'version').strip()
            assert 'version 4.29.1,' in receipt['version']
            for m in SOURCES: run(['-o',m+'.olean',m+'.lean'],m)
            audits={}
            for m,decls in registry.items():
                src='import '+m+'\n'+''.join('#print axioms '+d['name']+'\n' for d in decls)
                src+=''.join('#check '+d['name']+'\n' for d in decls if d['kind']=='theorem')
                (work/(m+'Audit.lean')).write_text(src); (out/(m+'Audit.lean')).write_text(src)
                log=run([m+'Audit.lean'],m+'Audit')
                matches=re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])",log)
                assert [n for n,_ in matches]==[d['name'] for d in decls]
                deps={n:[a.strip() for a in aa.split(',') if a.strip()] for n,aa in matches}
                assert all(set(aa)<={'propext','Quot.sound','Classical.choice'} for aa in deps.values())
                audits[m]={'declarations':decls,'dependencies':deps,'theorems':sum(d['kind']=='theorem' for d in decls)}
            runner='import CorrectionReconfigurationCases\ndef main := CorrectionReconfigurationCases.main\n'
            (work/'RunCases.lean').write_text(runner); (out/'RunCases.lean').write_text(runner)
            log=run(['--run','RunCases.lean'],'cases')
            observed=[[int(v) for v in line.split(',')] for line in log.splitlines()]
            expected=list(reference_rows())
            assert len(observed)==len(expected),(len(observed),len(expected))
            for i,(a,b) in enumerate(zip(observed,expected)):
                assert a==b,(i,a,b)
            (out/'reference.json').write_text(json.dumps(expected,separators=(',',':'))+'\n')
            receipt.update(modules=audits,new_theorems=sum(x['theorems'] for x in audits.values()),
                audited_declarations=sum(len(x['declarations']) for x in audits.values()),
                compared_records=len(observed),record_counts={str(k):sum(r[0]==k for r in observed) for k in range(4)},
                correspondence='1008 formula truth values, 8192 support/readiness decisions, 16384 structural fault/availability cases and 8064 admission/accounting cases match separately expressed truth-table, set and arithmetic reference. Same-author comparison, not independent review or deployment evidence.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'correction-reconfiguration-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
