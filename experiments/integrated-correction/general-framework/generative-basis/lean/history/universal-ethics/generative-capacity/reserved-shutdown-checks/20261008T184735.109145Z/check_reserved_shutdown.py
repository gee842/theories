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
NEW = ['ReservedShutdown']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','FaultTolerantCorrection','CorrectionReconfiguration','EvidenceQualifiedCorrection','FallibleInspection','TemporalInspection','MediatedControl','MediatedControlCases','RecoverableControl','ReservedShutdown','ReservedShutdownCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

import check_recoverable_control as prior

def initial(w,fuel,deadline):
    _,d=prior.run(prior.inspection(w),{'ready':prior.machine(w,fuel,deadline)})
    return d['ready']

def eligible(g,d):
    m=prior.active(d)
    return g[3] and g[0]==m['gen']+7 and g[1] and g[2]==m['serial'] and m.get('shutdown',True)

def admit(m,g,p,generation=0):
    t=prior.prepare_target(m,generation,p)
    if t is None:return None
    d=dict(origin=m,program=p[:],target=t,actual=m['a'],todo=p[:])
    return {'d':d,'stopped':False} if eligible(g,d) and t['reserve']>=3 and t['time']+3<=t['deadline'] else None

def execute(s,g,events):
    s=copy.deepcopy(s)
    for e in events:
        if s['stopped']:continue
        d=s['d'];m=prior.active(d)
        if 'target' in d and m['reserve']>=4 and m['time']+5<=m['deadline']:
            if e is None:
                out=prior.event(('tick',),d)
                if out is None:return False,s
                s['d']=out
            else:
                m['time']+=e;d['todo']=d['program'][:]
                if not prior.debit(m,1):return False,s
        else:
            if not eligible(g,d) or not prior.debit(m,3):return False,s
            m.update(completed=True,running=False,serial=m['serial']+1)
            s['stopped']=True
    return True,s

def outputs(g,result):
    if result is None:return [0]
    ok,s=result;d=s['d'];m=prior.active(d)
    return [1,int(ok),int(s['stopped']),int('target' in d),prior.present(d),m['k'],m['spent'],m['reserve'],m['time'],
        int(m['completed']),int(m['running']),m['serial'],m['gen'],m['journal'],prior.todo_count(d),int(eligible(g,d))]

def evaluate(m,g,p,events,generation=0):
    s=admit(m,g,p,generation)
    return outputs(g,None if s is None else execute(s,g,events))

def reference_rows():
    g=[8,True,1,True]
    for old,new,code,fuel,deadline in itertools.product(range(18),[0,7,13],range(16),[11,12,14,18],[12,30]):
        es=[1 if code & (1<<i) else None for i in range(4)]+[None]*8
        yield [0,old,new,code,fuel,deadline]+evaluate(initial(old,fuel,deadline),g,prior.target(new),es)
    for variant,fuel,deadline in itertools.product(range(8),[9,10,11,14],[10,11,30]):
        m=initial(1,fuel,deadline);gg=g[:]
        if variant==1:gg[0]=7
        if variant==2:gg[1]=False
        if variant==3:gg[2]=0
        if variant==4:gg[3]=False
        if variant==5:m['shutdown']=False
        yield [1,variant,fuel,deadline]+evaluate(m,gg,[9] if variant==7 else [2,6],[None]*12,int(variant==6))
    for fuel,deadline,prefix,delay in itertools.product([14,18],[15,20,30],range(4),range(11)):
        es=[None]*prefix+[delay]+[None]*12
        yield [2,fuel,deadline,prefix,delay]+evaluate(initial(1,fuel,deadline),g,[2,6],es)

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'reserved-shutdown-checks'/stamp
    out.mkdir(parents=True)
    source_bytes={m:p.read_bytes() for m,p in SOURCES.items()}
    helpers={p.name:p.read_bytes() for p in [Path(__file__),HERE/'check.py',HERE/'check_recoverable_control.py']}
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
        'scope':'A current authorized stop grant, three reserved units/steps, protected existing issue-deliver-enact protocol and bounded interruption intervals support shutdown during incomplete recovery. Every admissible schedule of at least initial remaining reserve minus two supervisor cycles stops; pending evidence and actual writes remain retained. No successful recovery suffix is needed. Supervisor scheduling, bounded interruption, durable gate/state and physical command correspondence remain supplied.'}
    try:
        with tempfile.TemporaryDirectory(prefix='reserved-shutdown-') as td:
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
            runner='import ReservedShutdownCases\ndef main := ReservedShutdownCases.main\n'
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
                correspondence='6912 supervised histories, 96 admission/authority records and 264 interruption-boundary histories match a separately expressed reference. Inherited Python world/write semantics are reused with a new supervisor reference. Same-author finite comparison, not independent acceptance or hardware validation.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'reserved-shutdown-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
