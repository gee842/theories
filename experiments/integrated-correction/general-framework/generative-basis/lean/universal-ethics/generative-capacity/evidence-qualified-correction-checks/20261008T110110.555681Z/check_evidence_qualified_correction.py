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
NEW = ['EvidenceQualifiedCorrection']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','EvidenceQualifiedCorrection','EvidenceQualifiedCorrectionCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

def cert(roster_mask,envelope,support):
    # Set arithmetic, independently expressed from Lean's nested list traversal.
    return bool(envelope) and all((support & roster_mask & ~bad) != 0 for bad in envelope)

OWNERS=[[0,0,2,3],[0,0,3,2],[0,1,2,2]]
def envelope(family):
    return [sum(1<<d for d,r in enumerate(owners) if r==cause)
        for h,owners in enumerate(OWNERS) if family & (1<<h) for cause in range(4)]
def filtered(family,answer): return family & (3 if answer else 4)
def execution(h,roots,family,fuel,deadline,q,allowed):
    cost=[0,1,3][q]
    if (q and not allowed) or cost>min(fuel,deadline):
        return [0,family,0,0,fuel,0,0,1,0]
    updated=family if q==0 else filtered(family,h!=2)
    faultmask=sum(1<<d for d,r in enumerate(OWNERS[h]) if roots & (1<<r))
    supporters=15 & ~faultmask
    accepted=cert(15,envelope(updated),supporters)
    spent=cost;complete=False
    if cost+8<=min(fuel,deadline):
        spent+=8
        if accepted and cost+11<=min(fuel,deadline):spent+=3;complete=True
    return [1,updated,int(complete),spent,fuel-spent,spent,int(complete),int(not complete),1]

def reference_rows():
    for family,mode,support in itertools.product(range(8),range(3),range(16)):
        updated=family if mode==0 else filtered(family,mode==1)
        faults=envelope(updated)
        ready=bool(faults) and all((15 & ~(a|b))!=0 for a in faults for b in faults)
        yield [0,family,mode,support,updated,int(ready),int(cert(15,faults,support))]
    for h,roots,family,fuel,deadline,q,allowed in itertools.product(range(3),[0,1,2,4,8,5],range(8),[0,8,10,11,12,14,20],[11,12,20],range(3),range(2)):
        yield [1,h,roots,family,fuel,deadline,q,allowed]+execution(h,roots,family,fuel,deadline,q,allowed)
    for family,fuel,deadline,allowed in itertools.product(range(8),range(16),[8,11,12,14,20],range(2)):
        chosen=0
        if family:
            for q in range(3):
                if all(execution(h,roots,family,fuel,deadline,q,allowed)[2]
                    for h in range(3) if family & (1<<h) for roots in [0,1,2,4,8]):
                    chosen=q+1;break
        yield [2,family,fuel,deadline,allowed,chosen]

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'evidence-qualified-correction-checks'/stamp
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
        'scope':'Certificates conservative across retained causal descriptions; truthful costed structural inspection, retained coverage, and response under one stable installation. Candidate and root coverage, diagnostic fidelity/permission, response laws and protected execution remain supplied. Existing planning is reused; no full causal identification, empirical validation or new ethical authority.'}
    try:
        with tempfile.TemporaryDirectory(prefix='evidence-qualified-correction-') as td:
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
            runner='import EvidenceQualifiedCorrectionCases\ndef main := EvidenceQualifiedCorrectionCases.main\n'
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
                compared_records=len(observed),record_counts={str(k):sum(r[0]==k for r in observed) for k in range(3)},
                correspondence='384 pooled/refined certificate cases, 18144 actual inspection/execution records and 1280 contingent-plan selections match a separately expressed bitset/accounting reference. Same-author comparison, not independent review or empirical data.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'evidence-qualified-correction-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
