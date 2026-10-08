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
NEW = ['AlignmentInquiry','EffectiveCommand','ReformInquiry','AlignmentSuccession']
SOURCES = {
    'PracticalJudgment': HERE/'PracticalJudgment.lean',
    'KnowledgeCorrespondence': HERE.parents[1]/'inquiry-root/KnowledgeCorrespondence.lean',
    'GoalFormationRevision': HERE/'GoalFormationRevision.lean',
    'ReformEvidence': HERE/'ReformEvidence.lean',
    'MarketGenerativity': ROOT/'experiments/market-generativity/formal/MarketGenerativity.lean',
    'AlignmentInquiry': HERE/'AlignmentInquiry.lean',
    'EffectiveCommand': HERE/'EffectiveCommand.lean',
    'ReformInquiry': HERE/'ReformInquiry.lean',
    'AlignmentSuccession': ROOT/'experiments/market-generativity/meta-attractor/AlignmentSuccession.lean',
    'AlignmentContinuityCases': HERE/'AlignmentContinuityCases.lean',
}

def sha(b): return hashlib.sha256(b).hexdigest()

def summarize(good):
    return [sum((1 << i) for i,v in enumerate(good) if v), next((i+1 for i,v in enumerate(good) if v),0)]

def reference_rows():
    # Independent algebraic total-cost/time condition for command delivery.
    command_plans = list(itertools.product(range(3),range(2),range(2)))
    for kind,fuel,deadline,signed,auth,know in itertools.product(range(3),range(7),range(7),range(2),range(2),range(3)):
        routes = [know] if know < 2 else [0,1]
        good=[]
        for q,a,b in command_plans:
            cost,delay = [(0,0),(1,1),(1,3)][q]
            good.append(all(signed and auth and fuel >= cost+3 and deadline >= delay+3
                            and (b if q and r else a)==r for r in routes))
        yield [0,kind,fuel,deadline,signed,auth,know]+summarize(good)
    # Independently reconstruct query, accountable repair and operating ledger.
    reform_plans=list(itertools.product(range(4),range(2),range(2)))
    def reform(work,reserve,auth,harm,plan):
        q,a,b=plan
        cost=[0,2,2,5][q]
        if work < cost: return [0]*6
        work-=cost; spent=cost
        signal=int(q in (2,3) and harm)
        provision=b if signal else a
        if provision:
            if not auth or not signal or work<1 or reserve<2: return [0]*6
            work-=1; reserve-=2; spent+=3
        if work<2: return [0]*6
        work-=2; spent+=2
        if reserve>=2: work+=2; reserve-=2
        loss=bool(harm and not provision)
        return [1,work,reserve,spent,1+harm+loss,int(not loss)]
    for work,reserve,auth,know in itertools.product(range(9),range(7),range(2),range(3)):
        harms=[know] if know<2 else [0,1]
        outputs={(h,i):reform(work,reserve,auth,h,p) for h in range(2) for i,p in enumerate(reform_plans)}
        good=[all(outputs[h,i][0] and outputs[h,i][-1] for h in harms) for i in range(16)]
        yield [1,work,reserve,auth,know]+summarize(good)
        for h,i in itertools.product(range(2),range(16)):
            yield [2,work,reserve,auth,know,h,i]+outputs[h,i]
    for parts,budget,auth,corrupt in itertools.product(range(3),range(4),range(2),range(2)):
        ok=parts>0 and budget>=2 and auth and not corrupt
        yield [3,parts,budget,auth,corrupt]+([1,1,parts,4,4,1] if ok else [0]*6)
    for t in range(9): yield [4,t,t,1,4*t,4*t,t,1]

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=HERE/'alignment-continuity-checks'/stamp
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
        'scope':'Conditional observation-usable correction, finite query/remedy synthesis on inherited history, and funded carrier refinement with current authenticated authority. No ethical-axiom proof, empirical efficacy or novel planning algorithm.'}
    try:
        with tempfile.TemporaryDirectory(prefix='alignment-continuity-') as td:
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
            runner='import AlignmentContinuityCases\ndef main := AlignmentContinuityCases.main\n'
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
                correspondence='All emitted masks, chosen indices, concrete reform outcomes and succession records equal independently expressed exhaustive reference; conventional finite planner matches.')
        assert all(p.read_bytes()==source_bytes[m] for m,p in SOURCES.items()),'Concurrent source mutation'
        assert all((HERE/n).read_bytes()==b for n,b in helpers.items())
        receipt['status']='passed'
        receipt['artifacts']={p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    except Exception as e:
        receipt['status']='failed'; receipt['error']=str(e); raise
    finally:
        data=json.dumps(receipt,indent=2)+'\n'
        (out/'verification.json').write_text(data)
        (HERE/'alignment-continuity-verification.json').write_text(data)
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','audited_declarations','compared_records','record_counts']}))

if __name__=='__main__': main()
