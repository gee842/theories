#!/usr/bin/env python3
"""Fresh kernel audits plus independently expressed finite execution comparisons."""
from datetime import datetime, timezone
import hashlib
import itertools
import copy
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
NEW = ['RecoverableControl']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','EvidenceQualifiedCorrection','FallibleInspection','TemporalInspection','MediatedControl','MediatedControlCases','RecoverableControl','RecoverableControlCases']}


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
def machine(w,fuel,deadline,rights=3):
    return dict(a=w,k=ALL,spent=0,reserve=fuel,time=0,deadline=deadline,serial=0,gen=0,journal=0,
        completed=False,running=True,rights=rights)
def debit(m,n):
    if m['reserve']<n or m['time']+n>m['deadline']:return False
    m['reserve']-=n;m['spent']+=n;m['time']+=n;return True
def prepare_target(m,g,p):
    if g!=m['gen'] or any(a>=9 for a in p):return None
    if any(a<3 for a in p) and not m['rights']&1:return None
    if any(3<=a<9 for a in p) and not m['rights']&2:return None
    out=copy.deepcopy(m)
    if not debit(out,len(p)+1):return None
    out.update(a=transform(p,m['a']),k=exact_image(p,m['k']),serial=m['serial']+1,gen=m['gen']+1,
        journal=m['journal']+1,completed=False)
    return out
def active(d):return d['target'] if 'target' in d else d['ready']
def present(d):return d['actual'] if 'target' in d else d['ready']['a']
def todo_count(d):return len(d['todo'])+1 if 'target' in d else 0
def event(e,old):
    d=copy.deepcopy(old);op=e[0]
    if op=='crash':
        active(d)['time']+=e[1]
        if 'target' in d:d['todo']=d['program'][:]
        return d
    if op=='tick':
        if 'target' not in d or not debit(d['target'],1):return None
        if d['todo']:
            d['actual']=transform([d['todo'].pop(0)],d['actual']);return d
        d['target']['a']=d['actual'];return {'ready':d['target']}
    if 'target' in d:return None
    m=d['ready']
    if op=='prepare':
        t=prepare_target(m,e[1],e[2])
        return None if t is None else dict(origin=m,program=e[2][:],target=t,actual=m['a'],todo=e[2][:])
    if op=='read':
        if not debit(m,1):return None
        m['k']=receive(m['k'],e[1],e[2]);return d
    if op=='command':
        hs=model_mask(m['k'])
        pool=[sum(1<<i for i,owner in enumerate(OWNERS[h]) if owner==r)
            for h in range(3) if hs & (1<<h) for r in range(4)]
        support=sum(1<<i for i in range(4) if not bad(m['a'],i))
        if debit(m,8) and cert(15,pool,support) and debit(m,3):
            m['completed']=True;m['running']=False;m['serial']+=1
        return d
    raise AssertionError(e)
def run(events,d):
    for e in events:
        out=event(e,d)
        if out is None:return False,d
        d=out
    return True,d
def outputs(d):
    m=active(d);w=present(d);busy='target' in d
    return [int(busy),w,m['k'],m['spent'],m['reserve'],m['time'],int(m['completed']),int(m['running']),
        m['serial'],m['gen'],m['journal'],todo_count(d),int(busy),int(bool(m['k'] & (1<<w)))]
def inspection(w):return [('read',i,physical(w,i,w//6==2)) for i in range(5)]
def marker_loss(d):
    if 'target' not in d:return d
    m=copy.deepcopy(d['origin']);m['a']=d['actual'];return {'ready':m}
def reference_rows():
    replay=[[]]+[[a] for a in range(9)]+[[a,b] for a,b in itertools.product(range(9),repeat=2)]
    for pi,p in enumerate(replay):
        for w in WORLDS:
            for n in range(len(p)+1):
                intermediate=transform(p[:n],w)
                yield [0,pi,w,n,intermediate,transform(p,intermediate),transform(p,w)]
    for old,new,code,fuel,deadline in itertools.product(WORLDS,WORLDS,range(8),[10,22,23,30],[22,30]):
        schedule=[('crash',1) if code & (1<<i) else ('tick',) for i in range(3)]
        ok,d=run(inspection(old)+[('prepare',0,target(new))]+schedule,{'ready':machine(old,fuel,deadline)})
        complete,out=run([('tick',)]*todo_count(d)+[('command',)],d)
        yield [1,old,new,code,fuel,deadline,int(ok),int(complete)]+outputs(out)
    for pi,p in enumerate(PROGRAMS):
        for rights,g in itertools.product(range(4),range(2)):
            ok,d=run([('prepare',g,p)],{'ready':machine(1,30,30,rights)})
            yield [2,pi,rights,g,int(ok)]+outputs(d)
    for old,new,n in itertools.product(WORLDS,WORLDS,range(3)):
        _,d=run(inspection(old)+[('prepare',0,target(new))]+[('tick',)]*n,{'ready':machine(old,30,30)})
        out=marker_loss(d);m=active(out);w=present(out)
        hs=model_mask(m['k'])
        pool=[sum(1<<i for i,owner in enumerate(OWNERS[h]) if owner==r)
            for h in range(3) if hs & (1<<h) for r in range(4)]
        yield [3,old,new,n,1,int(bool(m['k'] & (1<<w))),int(cert(15,pool,12))]+outputs(out)

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'recoverable-control-checks'/stamp
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
        'scope':'Staged overwrite recovery preserves quarantined intermediate states and published candidate coverage across arbitrary admitted finite crash histories. A sufficiently funded/timely uninterrupted suffix publishes with exact additional consumption. Durable descriptor/gate, atomic microsteps and publication, overwrite semantics, no extra writer, current source correspondence and stable final command remain supplied.'}
    try:
        with tempfile.TemporaryDirectory(prefix='recoverable-control-') as td:
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
            runner='import RecoverableControlCases\ndef main := RecoverableControlCases.main\n'
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
                correspondence='4716 prefix/redo records, 20736 interrupted-and-resumed histories, 1464 permission/generation preparation records, and 972 marker-loss records match a separately expressed reference. Same-author finite comparison, not independent acceptance or hardware validation.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'recoverable-control-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
