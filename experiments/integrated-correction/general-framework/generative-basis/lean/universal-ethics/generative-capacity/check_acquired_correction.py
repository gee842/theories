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
NEW = ['AcquiredCorrection']
SOURCES = {m: HERE/(m+'.lean') for m in
    ['AlignmentInquiry','EffectiveCommand','AcquiredCorrection','AcquiredCorrectionCases']}


def sha(b): return hashlib.sha256(b).hexdigest()

def trees(depth):
    leaves=[None,False,True]
    if not depth: return leaves
    smaller=trees(depth-1)
    return leaves+[(l,r) for l in smaller for r in smaller]

def independent_scan(root,fuel):
    # Iterative stack transcription, independent of Lean's recursive definition.
    stack=[([],root)]; spent=0
    while stack and spent < fuel:
        path,node=stack.pop(); spent+=1
        if node is None: continue
        if isinstance(node,bool): return 2,path,int(node),spent
        left,right=node
        stack.extend([(path+[1],right),(path+[0],left)])
    return (0 if stack else 1),[],0,spent

def code(path):
    answer=1
    for b in path: answer=2*answer+b
    return answer

def locate(root,path):
    for b in path:
        if not isinstance(root,tuple): return None
        root=root[b]
    return root if isinstance(root,bool) else None

def reference_rows():
    profiles=[(0,0),(4,20),(20,4),(8,8),(10,10),(20,20)]
    for i,root in enumerate(trees(2)):
        for fuel in range(10):
            verdict,path,key,spent=independent_scan(root,fuel)
            yield [0,i,fuel,verdict,code(path) if verdict==2 else 0,key,spent]
        for cmd,j,mutation,auth in itertools.product(range(3),range(6),range(3),range(3)):
            reserve,deadline=profiles[j]
            row=[1,i,cmd,j,mutation,auth]
            if min(reserve,deadline)<7:
                yield row+[0,0,1,0,reserve,0,0,0,0]; continue
            verdict,path,key,spent=independent_scan(root,7)
            ok=False
            if verdict==2:
                cost=len(path)+1
                if spent+cost<=min(reserve,deadline):
                    spent+=cost
                    actual=locate(root,path)
                    if mutation==1 and actual is not None: actual=not actual
                    if mutation==2: actual=None
                    ok=actual is not None and int(actual)==key and auth==0 and spent+3<=min(reserve,deadline)
                    if ok: spent+=3
            yield row+[1,int(ok),int(not(ok and cmd==2)),int(ok),reserve-spent,spent,spent,int(ok and cmd==0),int(ok and cmd==1)]

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'acquired-correction-checks'/stamp
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
        'scope':'Finite inspection-driven route acquisition, scoped absence, query accounting, current route and credential revalidation, conditional actual execution. Fixed faithful scan substrate and atomic dispatch; no authority-legitimacy, capture-resistance, empirical deployment or algorithmic novelty claim.'}
    try:
        with tempfile.TemporaryDirectory(prefix='acquired-correction-') as td:
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
            runner='import AcquiredCorrectionCases\ndef main := AcquiredCorrectionCases.main\n'
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
                compared_records=len(observed),record_counts={str(k):sum(r[0]==k for r in observed) for k in range(2)},
                correspondence='All 147 depth-two substrates, 1470 search records and 23814 acquisition/dispatch records match a separately written iterative stack reference. Same-author comparison, not independent review.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'acquired-correction-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
