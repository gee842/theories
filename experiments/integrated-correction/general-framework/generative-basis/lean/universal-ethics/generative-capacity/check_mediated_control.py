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
NEW = ['MediatedControl']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','EvidenceQualifiedCorrection','FallibleInspection','TemporalInspection','MediatedControl','MediatedControlCases']}


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

# Integer opcodes deliberately differ from Lean constructors. Model/fault fields
# are overwritten by the last such instruction; permission is checked as a set.
PROGRAMS=[[]]+[[a] for a in range(13)]+[[a,b] for a,b in itertools.product(range(13),repeat=2)]
EXACT=[[],[0],[8],[2,5],[0,2],[6,3],[1,7,2]]
def effect(p):return 2*int(any(a<3 for a in p))+int(any(3<=a<9 for a in p))
def transform(p,w):
    hm=[a for a in p if a<3]; fs=[a-3 for a in p if 3<=a<9]
    return 6*(hm[-1] if hm else w//6)+(fs[-1] if fs else w%6)
def exact_image(p,possible):
    return sum(1<<v for v in {transform(p,w) for w in WORLDS if possible & (1<<w)})
def target(w):return [w//6,3+w%6]
def full_events(old,new):
    return [('read',d,physical(old,d,old//6==2)) for d in range(5)]+[('patch',0,target(new)),('command',)]
def execution(events,old,fuel,deadline,rights=3):
    actual=old;possible=ALL;spent=0;serial=0;completed=False;records=0;finished=True
    generation=0;journal=0;last=4;authority=7;signed=True;issued=False;delivered=False
    for e in events:
        if e[0]=='read':
            if spent+1>min(fuel,deadline):finished=False;break
            spent+=1;records+=1;possible=receive(possible,e[1],e[2])
        elif e[0]=='patch':
            p=e[2];has_model=any(a<3 for a in p);has_fault=any(3<=a<9 for a in p)
            denied=any(a>=9 for a in p) or (has_model and not rights&1) or (has_fault and not rights&2)
            if e[1]!=generation or denied or spent+len(p)+1>min(fuel,deadline):finished=False;break
            spent+=len(p)+1;records+=1;serial+=1;authority+=1
            generation+=1;journal+=1;last=effect(p);signed=issued=delivered=completed=False
            actual=transform(p,actual);possible=exact_image(p,possible)
        else:
            records+=1
            hs=model_mask(possible)
            pool=[sum(1<<d for d,owner in enumerate(OWNERS[h]) if owner==r)
                for h in range(3) if hs & (1<<h) for r in range(4)]
            supporters=sum(1<<d for d in range(4) if not bad(actual,d))
            if spent+8<=min(fuel,deadline):
                spent+=8
                if cert(15,pool,supporters) and spent+3<=min(fuel,deadline):
                    spent+=3;completed=True;serial+=1;signed=issued=delivered=True
    return [int(finished),actual,possible,model_mask(possible),spent,fuel-spent,spent,serial,
        int(completed),int(not completed),records,int(bool(possible & (1<<actual))),generation,journal,last,authority,
        int(signed),int(issued),int(delivered),rights]

def reference_rows():
    for pi,p in enumerate(PROGRAMS):
        for w in WORLDS:
            out=transform(p,w)
            yield [0,pi,w,out,effect(p),int(successor(effect(p),w,out))]
    for hs,fs in itertools.product(range(8),range(64)):
        for pi,p in enumerate(EXACT):
            old=family(hs,fs)
            yield [1,hs,fs,pi,exact_image(p,old),predict(effect(p),old)]
    for pi,p in enumerate(PROGRAMS):
        for rights,generation,claim in itertools.product(range(4),range(2),range(4)):
            yield [2,pi,rights,generation,claim]+execution([('patch',generation,p)],1,30,30,rights)
    for old,new in itertools.product(WORLDS,WORLDS):
        for fuel,rights in itertools.product([0,4,5,7,8,15,18,19],range(4)):
            yield [3,old,new,fuel,rights]+execution(full_events(old,new),old,fuel,19,rights)
    for old,new,deadline in itertools.product(WORLDS,WORLDS,[8,16,18]):
        yield [4,old,new,deadline]+execution(full_events(old,new),old,30,deadline)
    old_possible=ALL
    for d,r in enumerate([False,False,True,True,True]):old_possible=receive(old_possible,d,r)
    for new in WORLDS:yield [5,new,1,int(bool(old_possible & (1<<new))),1]
    for old,new in itertools.product(WORLDS,WORLDS):
        yield [6,old,new]+execution([('patch',0,target(new)),('patch',0,target(new))],old,30,30)

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'mediated-control-checks'/stamp
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
        'scope':'Instruction-derived transition coverage, exact-image evidence transport, checked rights and generation, coupled mutation/recording, old-command revocation and paid local correction. Initial coverage, current read correspondence, complete runtime mediation, atomic implementation and protected final command remain supplied; neither physical fault repair nor hardware refinement is established.'}
    try:
        with tempfile.TemporaryDirectory(prefix='mediated-control-') as td:
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
            runner='import MediatedControlCases\ndef main := MediatedControlCases.main\n'
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
                compared_records=len(observed),record_counts={str(k):sum(r[0]==k for r in observed) for k in range(7)},
                correspondence='3294 instruction/world records, 3584 exact/coarse possibility transforms, 5856 claim/rights/generation records, 10368 full budget/rights histories, 972 deadline histories, 18 bypass records and 324 replay histories match a separately expressed integer-opcode/bitset reference. Same-author comparison; not independent review or empirical data.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'mediated-control-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
