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
NEW = ['FallibleInspection']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','EvidenceQualifiedCorrection','FallibleInspection','FallibleInspectionCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

def cert(roster_mask,envelope,support):
    # Set arithmetic, independently expressed from Lean's nested list traversal.
    return bool(envelope) and all((support & roster_mask & ~bad) != 0 for bad in envelope)

OWNERS=[[0,0,2,3],[0,0,3,2],[0,1,2,2]]
def faults(h,extended=False):
    owners=OWNERS[h]+([4] if extended else [])
    return [sum(1<<d for d,r in enumerate(owners) if r==cause) for cause in range(4+extended)]
def envelope(family): return [bad for h in range(3) if family & (1<<h) for bad in faults(h)]
def decode(code,n): return [None if (v:=code//(3**d)%3)==0 else v==2 for d in range(n)]
def explains(reports,bad,answer):
    return all(value is None or value==answer or bad & (1<<d) for d,value in enumerate(reports))
def posterior(family,extended,reports):
    return sum(1<<h for h in range(3) if family & (1<<h)
        and any(explains(reports,bad,h!=2) for bad in faults(h,extended)))
def simulation(h,roots,extended,arbitrary):
    owners=OWNERS[h]+([4] if extended else [])
    return [arbitrary[d] if roots & (1<<cause) else h!=2 for d,cause in enumerate(owners)]
def execution(h,roots,extended,reports,fuel,deadline,allowed):
    cost=4+extended
    if not allowed or cost>min(fuel,deadline):return [0,7,0,0,fuel,0,0,1,0,0]
    updated=posterior(7,extended,reports)
    faultmask=sum(1<<d for d,r in enumerate(OWNERS[h]) if roots & (1<<r))
    accepted=cert(15,envelope(updated),15 & ~faultmask)
    spent=cost;complete=False
    if cost+8<=min(fuel,deadline):
        spent+=8
        if accepted and cost+11<=min(fuel,deadline):spent+=3;complete=True
    encoded=sum((0 if v is None else 2 if v else 1)*3**d for d,v in enumerate(reports))
    return [1,updated,int(complete),spent,fuel-spent,spent,int(complete),int(not complete),cost,encoded]
def reference_rows():
    for extended in range(2):
        n=4+extended
        for family,code in itertools.product(range(8),range(3**n)):
            reports=decode(code,n);updated=posterior(family,extended,reports);pool=envelope(updated)
            ready=bool(pool) and all((15 & ~(a|b))!=0 for a in pool for b in pool)
            support=lambda value:sum(1<<d for d,v in enumerate(reports) if v is not None and v==value)
            yield [0,extended,family,code,updated,int(ready),
                int(cert((1<<n)-1,faults(0,extended),support(True))),
                int(cert((1<<n)-1,faults(2,extended),support(False)))]
    for h,extended,roots,mode in itertools.product(range(3),range(2),[0,1,2,4,8,16,20],range(5)):
        arbitrary=[[None,False,True,d%2==0,d>=2][mode] for d in range(4+extended)]
        reports=simulation(h,roots,extended,arbitrary)
        for fuel,deadline,allowed in itertools.product([0,10,14,15,16,20],[15,16,20],range(2)):
            yield [1,h,extended,roots,mode,fuel,deadline,allowed]+execution(h,roots,extended,reports,fuel,deadline,allowed)
    for extended in range(2):
        for h,roots,code in itertools.product(range(3),[0,1,2,4,8,16,20],range(3**(4+extended))):
            reports=simulation(h,roots,extended,decode(code,4+extended))
            yield [2,extended,h,roots,code]+execution(h,roots,extended,reports,20,20,True)
    for a,b,code in itertools.product(range(8),range(8),range(27)):
        reports=decode(code,3)
        yield [3,a,b,code,int(explains(reports,a,True)),int(explains(reports,b,False)),
            int(all(v is not None for v in reports)),int(a|b==7)]

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'fallible-inspection-checks'/stamp
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
        'scope':'Joint inference of structural answers and fallible witness faults; retention, exact complete-transcript diagnosability, current command soundness and conditional completion. Actual candidate/fault coverage, truthful surviving reports, fixed roster and interval, mandate and protected execution remain supplied.'}
    try:
        with tempfile.TemporaryDirectory(prefix='fallible-inspection-') as td:
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
            runner='import FallibleInspectionCases\ndef main := FallibleInspectionCases.main\n'
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
                correspondence='2592 transcript refinements/certificates, 7560 costed executions, 6804 executions over arbitrary faulty-report assignments, and 1728 paired-fault transcript records match a separately expressed bitset/accounting reference. Same-author comparison, not independent review or empirical data.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'fallible-inspection-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
