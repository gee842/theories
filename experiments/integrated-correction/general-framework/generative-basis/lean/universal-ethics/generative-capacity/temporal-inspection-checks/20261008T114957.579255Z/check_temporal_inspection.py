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
NEW = ['TemporalInspection']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','EvidenceQualifiedCorrection','FallibleInspection','TemporalInspection','TemporalInspectionCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

def cert(roster_mask,envelope,support):
    # Set arithmetic, independently expressed from Lean's nested list traversal.
    return bool(envelope) and all((support & roster_mask & ~bad) != 0 for bad in envelope)

OWNERS=[[0,0,2,3],[0,0,3,2],[0,1,2,2]]
ALL=(1<<18)-1
WORLDS=range(18)
def model_mask(possible):return sum(1<<h for h in range(3) if possible & (63<<(6*h)))
def bad(w,d):
    h,f=divmod(w,6)
    return f!=0 and (OWNERS[h]+[4])[d]==f-1
def fits(w,d,r):return bad(w,d) or r is None or r==(w//6!=2)
def receive(possible,d,r):return sum(1<<w for w in WORLDS if possible & (1<<w) and fits(w,d,r))
def successor(c,w,v):
    return [v==w,v//6==w//6,v%6==w%6,True][c]
def predict(c,possible):
    return sum(1<<v for v in WORLDS if any(possible & (1<<w) and successor(c,w,v) for w in WORLDS))
def family(hs,fs):return sum(1<<w for w in WORLDS if hs & (1<<(w//6)) and fs & (1<<(w%6)))
def decode(r):return [None,False,True][r]
def physical(w,d,r):return r if bad(w,d) else w//6!=2

def execution(events,old,fuel,deadline,permission=3):
    actual=old;possible=ALL;spent=0;serial=0;completed=False;records=0;finished=True;lawful=True
    for event in events:
        op=event[0]
        cost=1 if op=='read' else [0,0,2,2][event[1]] if op=='move' else 0
        permitted=bool(permission&1) if op=='read' else bool(permission&2) if cost else True
        if op=='read':lawful=lawful and fits(actual,event[1],event[2])
        if op=='move':lawful=lawful and successor(event[1],actual,event[2])
        if not permitted or spent+cost>min(fuel,deadline):finished=False;break
        spent+=cost;records+=1
        if op=='read':possible=receive(possible,event[1],event[2])
        elif op=='move':possible=predict(event[1],possible);actual=event[2]
        else:
            hs=model_mask(possible)
            pool=[sum(1<<d for d,owner in enumerate(OWNERS[h]) if owner==r)
                for h in range(3) if hs & (1<<h) for r in range(4)]
            supporters=sum(1<<d for d in range(4) if not bad(actual,d))
            accepted=cert(15,pool,supporters)
            if spent+8<=min(fuel,deadline):
                spent+=8
                if accepted and spent+3<=min(fuel,deadline):spent+=3;completed=True;serial+=1
    return [int(finished),actual,possible,model_mask(possible),spent,fuel-spent,spent,serial,
        int(completed),int(not completed),records,int(bool(possible & (1<<actual))),int(finished and lawful)]

def reference_rows():
    for hs,fs,d,r in itertools.product(range(8),range(64),range(5),range(3)):
        out=receive(family(hs,fs),d,decode(r))
        yield [0,hs,fs,d,r,out,model_mask(out)]
    for hs,fs,c in itertools.product(range(8),range(64),range(4)):
        out=predict(c,family(hs,fs));yield [1,hs,fs,c,out,model_mask(out)]
    for w,code in itertools.product(WORLDS,range(243)):
        events=[('read',d,physical(w,d,decode(code//(3**d)%3))) for d in range(5)]+[('command',)]
        yield [2,w,code]+execution(events,w,16,16)
    for old,new in itertools.product(WORLDS,WORLDS):
        events=[('read',d,physical(old,d,old//6==2)) for d in range(5)]
        events += [('move',3,new)]+[('read',d,physical(new,d,new//6==2)) for d in range(5)]+[('command',)]
        for fuel,deadline,permission in itertools.product([0,4,5,6,12,20,22,23],[22,23],range(4)):
            yield [3,old,new,fuel,deadline,permission]+execution(events,old,fuel,deadline,permission)
    for h,code in itertools.product(range(3),range(216)):
        events=[]
        for i,d in enumerate([0,2,4]):
            target=6*h+code//(6**i)%6
            events += [('move',1,target),('read',d,physical(target,d,h==2))]
        events += [('command',)]
        yield [4,h,code]+execution(events,6*h,30,30)

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'temporal-inspection-checks'/stamp
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
        'scope':'Time-ordered structural/fault possibilities, covered transition prediction, lawful finite-history retention and current correction with paid inspection. Transition and source-response laws, initial coverage, protected recording and stable command execution remain supplied; mobile responses do not imply a physical recovery protocol.'}
    try:
        with tempfile.TemporaryDirectory(prefix='temporal-inspection-') as td:
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
            runner='import TemporalInspectionCases\ndef main := TemporalInspectionCases.main\n'
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
                compared_records=len(observed),record_counts={str(k):sum(r[0]==k for r in observed) for k in range(5)},
                correspondence='7680 individual evidence updates, 2048 change predictions, 4374 stable scan/executions, 20736 change/reinspection budget-permission records, and 648 three-read mobile-fault histories match a separately expressed bitset/history reference. Same-author comparison, not independent review or empirical data.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'temporal-inspection-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
