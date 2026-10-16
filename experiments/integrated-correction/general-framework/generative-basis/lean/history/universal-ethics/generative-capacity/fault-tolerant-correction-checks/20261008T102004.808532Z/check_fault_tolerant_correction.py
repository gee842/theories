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
NEW = ['FaultTolerantCorrection']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','FaultTolerantCorrectionCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

def cert(roster_mask,envelope,support):
    # Set arithmetic, independently expressed from Lean's nested list traversal.
    return bool(envelope) and all((support & roster_mask & ~bad) != 0 for bad in envelope)

def reference_rows():
    for em in range(256):
        envelope=[bad for bad in range(8) if em & (1<<bad)]
        for support in range(8): yield [0,em,support,int(cert(7,envelope,support))]
        apart=all((7 & ~(a|b))!=0 for a in envelope for b in envelope)
        available=all(cert(7,envelope,7 & ~bad) for bad in envelope)
        assert apart==available
        # Soundness: false supporters confined to an admitted fault set never certify.
        for bad in envelope:
            for support in range(8):
                if support & ~bad == 0: assert not cert(7,envelope,support)
        yield [1,em,int(apart),int(available)]
    profiles=[(0,20),(6,20),(9,9),(11,11)]
    for scheme,rm,am,route,cmd,profile,frame in itertools.product(range(3),range(16),range(16),range(3),range(3),range(4),range(3)):
        n=4 if scheme==2 else 3
        faults=[[1,2,4],[3,4],[3,4,8]][scheme]
        roster_mask=(1<<n)-1
        gate=frame==0 and cert(roster_mask,faults,rm) and cert(roster_mask,faults,am)
        fuel,deadline=profiles[profile];spent=0;serial=0;ok=False
        if 2*n<=min(fuel,deadline):
            spent=2*n
            if gate and spent+3<=min(fuel,deadline):
                spent+=3;serial=1
                ok=route==2
        yield [2,scheme,rm,am,route,cmd,profile,frame,int(gate),int(ok),int(not(ok and cmd==2)),int(ok),fuel-spent,spent,spent,serial,int(ok and cmd==0),int(ok and cmd==1)]
    for depth,profile,scheme,cmd in itertools.product(range(8),range(6),range(3),range(3)):
        fuel=[0,5,10,15,25,50][profile];n=4 if scheme==2 else 3
        cost=n*(depth+2);spent=0;ok=False
        if cost<=min(fuel,50):
            spent=cost
            if cmd==2 and cost+3<=min(fuel,50):spent+=3;ok=True
        yield [3,depth,profile,scheme,cmd,int(ok),spent,fuel-spent,int(ok)]

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'fault-tolerant-correction-checks'/stamp
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
        'scope':'Single-transaction observation and bounded-mandate attestation under explicit correlated fault envelopes. Protected registry/mandate/monitor and actual fault coverage remain supplied. Not Byzantine agreement, ethical legitimacy from signatures, cryptographic implementation or deployed-AI validation.'}
    try:
        with tempfile.TemporaryDirectory(prefix='fault-tolerant-correction-') as td:
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
            runner='import FaultTolerantCorrectionCases\ndef main := FaultTolerantCorrectionCases.main\n'
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
                correspondence='2048 support decisions, 256 availability conditions, 82944 concrete execution records and 432 variable-depth execution records match separate set-arithmetic and accounting reference. Same-author comparison, not independent review.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'fault-tolerant-correction-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
