#!/usr/bin/env python3
"""Independent microphase interpreter for the frozen predictor exposure contract.

The parent is imported only as the callable comparison oracle. No parent helper
implements the interpreter, its random tape, ledger or distribution propagation.
The input domain and analytical diagnostics were fixed in CHECK-PROTOCOL.md.
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import asdict
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import importlib.util
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
PRED=ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction'
FIELDS=('fuel','gate','gate_life','stage','life','q','last','written','prelearn','stale','corrected','witness')
METRICS=('gate_forms','base_forms','retrofits','rents','trials','captures','writes','updater_changes','post_captures','brier16','decoder_errors','spent','waste','unpaid_writes','slow_writes','fast_writes','acquired_uses')
ARMS=('variable','conventional','fixed_fast','fixed_slow','direct_record','frozen_register','inverted_record','inverted_action')
LAW_FIELDS=('gate_assembly','base','retrofit','rent','trial','write','renewal','gate_renewal','packet','lifetime','gate_lifetime')
ZERO=(Q(0),)*len(METRICS)
TEMPLATES=[(-1,0,0,0,2,0,False),(0,2,1,0,2,1,False),(0,0,2,6,4,1,True),(1,2,2,6,4,1,True),(0,2,2,6,1,0,True),(0,1,2,1,2,0,True),(1,2,2,0,4,1,True),(1,1,2,6,2,1,True),(0,2,2,6,0,0,True),(1,0,1,0,2,0,False)]


def digest(p):return sha256(p.read_bytes()).hexdigest()
def statekey(s):return tuple(s[k] for k in FIELDS)
def statefrom(t):return dict(zip(FIELDS,t))
def newstate(fuel):return dict(zip(FIELDS,(fuel,-1,0,0,0,2,0,False,False,-1,False,False)))
def jsontext(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def save(name,value):(HERE/name).write_text(json.dumps(value,indent=2,sort_keys=True,allow_nan=False)+'\n')
def write_gzip(path,text):path.write_bytes(gzip.compress(text.encode(),mtime=0))


def action(arm,q,last):
    a=last if q==2 else int(q>=3)
    return 1-a if arm=='inverted_action' else a


def micro(law,entry,arm,regime,after,seed):
    """One deterministic tape. Prefix objects retain the in-flight packet."""
    s=dict(entry); m=dict.fromkeys(METRICS,0); pending=law['packet']; trace=[]
    assert 0<=s['q']<=4 and s['stage'] in (0,1,2)
    assert 0<=s['life']<=law['lifetime'] and 0<=s['gate_life']<=law['gate_lifetime']
    assert s['gate'] in (-1,0,1) and (not s['gate_life'] or s['gate'] in (0,1))
    def snap(event,**transient):
        assert min(s['fuel'],pending,m['spent'],m['waste'])>=0
        assert s['fuel']+pending+m['spent']+m['waste']==entry['fuel']+law['packet']
        trace.append(dict(event=event,state=dict(s),inflight_packet=pending,
                          spent=m['spent'],waste=m['waste'],transient=transient))
    def pay(amount,event):
        assert s['fuel']>=amount,(event,s,amount)
        s['fuel']-=amount;m['spent']+=amount;snap(event)
    def finish(status):
        nonlocal pending
        if pending:
            m['waste']+=pending;pending=0;snap('opportunity_expired')
        snap('boundary',status=status)
        return dict(state=s,moments=m,status=status,trace=trace)
    gbit,pbit,available=seed
    snap('entry')
    if s['gate_life']==0 and s['fuel']>=law['gate_assembly']:
        kind=1 if arm in ('fixed_fast','direct_record') else 0 if arm=='fixed_slow' else gbit
        old=s['gate'];pay(law['gate_assembly'],'gate_paid')
        s.update(gate=kind,gate_life=law['gate_lifetime'])
        m['gate_forms']+=1;m['updater_changes']+=int(old>=0 and old!=kind)
        snap('gate_formed')
    if s['gate_life']>0 and s['life']==0 and s['stage']!=1 and s['fuel']>=law['base']:
        pay(law['base'],'base_paid')
        s.update(stage=1,life=0,q=2,last=pbit,written=False,prelearn=False,stale=-1,corrected=False)
        m['base_forms']+=1;snap('base_formed')
    price=1 if arm=='direct_record' else law['retrofit']
    if s['gate_life']>0 and s['stage']==1 and s['fuel']>=price:
        pay(price,'retrofit_paid');s.update(stage=2,life=law['lifetime'],q=2)
        m['retrofits']+=1;snap('retrofitted')
    if s['life']==0 or s['stage']!=2:return finish(0)
    if s['fuel']<law['rent']:
        s.update(stage=0,life=0,q=2,last=0,written=False,prelearn=False,stale=-1,corrected=False)
        snap('rent_failed_memory_destroyed');return finish(1)
    pay(law['rent'],'rent_paid');m['rents']+=1
    if s['gate_life']==0 or s['fuel']<law['trial']:return finish(2)
    old=dict(s);a=action(arm,s['q'],s['last'])
    forecast=s['q'] if a else 4-s['q']
    pay(law['trial'],'work_paid')
    captured=bool(available and a==regime)
    pending=0
    if captured:
        s['fuel']+=law['packet']-law['renewal']-law['gate_renewal']
        m['spent']+=law['renewal']+law['gate_renewal']
    else:m['waste']+=law['packet']
    observed=a if captured else 1-a
    snap('receipt',action=a,receipt=captured,decoded=observed,forecast_numerator=forecast)
    wrote=s['fuel']>=law['write']
    if wrote:
        pay(law['write'],'write_paid')
        if arm!='frozen_register':
            target=1-observed if arm=='inverted_record' else observed
            s['q']=4*target if s['gate']==1 else max(0,min(4,s['q']+(1 if target else -1)))
        s['written']=True;snap('record_written',action=a,receipt=captured)
    else:snap('write_unaffordable_record_retained',action=a,receipt=captured)
    s['last']=a
    s['gate_life']=law['gate_lifetime'] if captured else s['gate_life']-1
    s['life']=law['lifetime'] if captured else s['life']-1
    s['prelearn']=bool(old['prelearn'] or (not after and captured and old['written'] and old['q']!=2))
    if after and not captured and old['prelearn'] and old['stale']==-1:s['stale']=a
    s['corrected']=bool(old['corrected'] or (after and wrote and s['q']!=old['q'] and s['stale']>=0
        and action(arm,old['q'],a)==s['stale'] and action(arm,s['q'],a)!=s['stale']))
    s['witness']=bool(old['witness'] or (after and captured and old['corrected'] and old['stale']>=0 and a!=old['stale']))
    m.update(trials=1,captures=int(captured),writes=int(wrote),post_captures=int(after and captured),
             brier16=(forecast-4*int(captured))**2,decoder_errors=int(observed!=regime),
             unpaid_writes=int(not wrote),slow_writes=int(wrote and old['gate']==0),
             fast_writes=int(wrote and old['gate']==1),acquired_uses=int(old['written'] and old['q']!=2))
    snap('renewed_or_worn',action=a,receipt=captured)
    return finish(4 if wrote else 3)


def tapes(law):
    p=Q(law['availability'])
    for g,b,v in itertools.product((0,1),repeat=3):
        weight=(p if v else 1-p)/4
        if weight:yield (g,b,v),weight


def tsvinput(law,s,arm,z,seed):
    data=[law[k] for k in LAW_FIELDS]+[s[k] for k in FIELDS[:8]]+[ARMS.index(arm),z,*seed]
    data[12]=2 if s['gate']==-1 else s['gate']
    return '\t'.join(str(int(x)) for x in data)


def tsvoutput(out):
    data=[out['state'][k] for k in FIELDS[:8]]
    data[1]=2 if out['state']['gate']==-1 else out['state']['gate']
    m=out['moments'];data += [m['spent'],m['waste'],m['trials'],m['captures'],m['writes'],out['status']]
    return '\t'.join(str(int(x)) for x in data)


def main():
    freeze=json.loads((HERE/'check-source-freeze.json').read_text())
    # Formal finalization is a separate, explicit pre-comparison record.
    final_path=HERE/'runtime-formal-freeze.json'
    assert final_path.exists(),'Mechanism must finish evaluator; write explicit final freeze first.'
    final=json.loads(final_path.read_text())
    for n,rec in freeze['files'].items():
        if Path(n).name in ('Exposure.lean','Evaluate.lean'):continue
        assert digest(ROOT/n)==rec['sha256'],('frozen source changed',n)
    for n,h in final['sources'].items():assert digest(HERE/n)==h,('formal source changed',n)
    exe=Path(final['lean_executable']);assert exe.is_file()
    assert digest(exe)==final['lean_executable_sha256']
    spec=importlib.util.spec_from_file_location('_stochastic_prediction_reference',PRED/'model.py')
    parent=importlib.util.module_from_spec(spec);sys.modules[spec.name]=parent;spec.loader.exec_module(parent)
    assert parent.ARMS==ARMS and parent.MOMENTS==METRICS
    assert tuple(parent.State.__dataclass_fields__)==FIELDS
    saved=json.loads((PRED/'results.json').read_text())
    calls={};formal_rows={};sample_traces={};prefix_count=0;branch_count=0
    def compare(law,s,arm,z,after,tag):
        nonlocal prefix_count,branch_count
        key=(jsontext(law),statekey(s),arm,z,bool(after))
        if key in calls:return calls[key]['kernel']
        ours=defaultdict(Q);outputs=[]
        for seed,weight in tapes(law):
            out=micro(law,s,arm,z,after,seed);branch_count+=1;prefix_count+=len(out['trace'])
            joint=(statekey(out['state']),tuple(out['moments'][k] for k in METRICS))
            ours[joint]+=weight
            row=tsvinput(law,s,arm,z,seed);answer=tsvoutput(out)
            assert row not in formal_rows or formal_rows[row]==answer
            formal_rows[row]=answer
            outputs.append(dict(seed=list(seed),weight=str(weight),status=out['status'],
                                state=out['state'],moments=out['moments']))
            if tag.startswith('diagnostic'):sample_traces[f'{tag}/{seed}']=out['trace']
        plaw=parent.Law(**{k:(Q(v) if k=='availability' else tuple(v) if k=='reversals' else v)
                          for k,v in law.items() if k!='initial_source'})
        actual=defaultdict(Q)
        for nxt,p,m in parent.advance(plaw,parent.State(**s),arm,z,after):
            actual[(tuple(getattr(nxt,k) for k in FIELDS),tuple(m))]+=p
        assert sum(ours.values())==sum(actual.values())==1
        assert dict(ours)==dict(actual),(tag,s,arm,z,after,ours,actual)
        calls[key]=dict(kernel=dict(ours),record=dict(tag=tag,law=law,state=s,arm=arm,
                       regime=z,after=bool(after),outcomes=outputs))
        return dict(ours)
    composition=[];reachable_calls=0
    for case,report in saved['cases'].items():
        law=report['law']
        for arm in ARMS:
            weighted=defaultdict(Q);entrance=Q(0);prep_spent=Q(0);failed=Q(0)
            reserves=sorted({r['reserve'] for r in report['preparations'] if r['commissioned']})
            continuation={}
            for reserve in reserves:
                table={(z,statekey(newstate(reserve))):(Q(1,2),ZERO) for z in (0,1)}
                boundary=law['reversals'][0] if law['reversals'] else law['horizon']
                for t in range(law['horizon']):
                    nxt={};parity=sum(v<=t for v in law['reversals'])%2
                    for (z,sk),(mass,mom) in table.items():
                        reachable_calls+=1
                        k=compare(law,statefrom(sk),arm,z^parity,t>=boundary,f'inherited/{case}/{arm}/{t}')
                        for (ns,inc),prob in k.items():
                            oldmass,oldmom=nxt.get((z,ns),(Q(0),ZERO))
                            nxt[(z,ns)]=(oldmass+mass*prob,tuple(a+prob*b+mass*prob*c for a,b,c in zip(oldmom,mom,inc)))
                    table=nxt;assert sum(p for p,_ in table.values())==1
                plaw=parent.Law(**{k:(Q(v) if k=='availability' else tuple(v) if k=='reversals' else v)
                                  for k,v in law.items() if k!='initial_source'})
                source_table,_=parent.evolve(plaw,arm,reserve)
                normalized={(z,tuple(getattr(s,k) for k in FIELDS)):(mass,mom)
                            for (z,s),(mass,mom) in source_table.items()}
                assert table==normalized,('composed endpoint mass and weighted first moments',case,arm,reserve)
                vals={k:sum(m[i] for p,m in table.values()) for i,k in enumerate(METRICS)}
                vals.update(reserve=sum(p*sk[0] for (z,sk),(p,m) in table.items()),
                    p_correction=sum(p*sk[11] for (z,sk),(p,m) in table.items()),
                    p_active_memory=sum(p*int(sk[3]==2 and sk[4]>0) for (z,sk),(p,m) in table.items()),
                    p_written_active_memory=sum(p*int(sk[3]==2 and sk[4]>0 and sk[7]) for (z,sk),(p,m) in table.items()),
                    final_q=sum(p*sk[5] for (z,sk),(p,m) in table.items()))
                vals['brier_loss']=vals.pop('brier16')/16
                continuation[reserve]=vals
            for row in report['preparations']:
                mass=Q(row['probability']);prep_spent+=mass*row['preparation_spent']
                if not row['commissioned']:failed+=mass*row['remaining_energy'];continue
                entrance+=mass
                for key,value in continuation[row['reserve']].items():weighted[key]+=mass*value
                weighted['source_remainder']+=mass*(row['remainder']+(row['packets']-law['horizon'])*law['packet'])
            weighted.update(p_commissioned=entrance,preparation_spent=prep_spent,
                            adapter_spent=entrance*law['adapter'],uncommissioned_energy=failed)
            expected={k:Q(v) for k,v in report['arms'][arm]['metrics'].items()}
            assert dict(weighted)==expected,(case,arm,dict(weighted),expected)
            composition.append(dict(case=case,arm=arm,metrics={k:str(v) for k,v in sorted(weighted.items())}))
    primary=saved['cases']['primary']['law']
    grid_count=0
    for template,F,avail,arm,z,after in itertools.product(TEMPLATES,(0,1,2,3,4,5,6,7,8,12),('0','3/4','1'),ARMS,(0,1),(False,True)):
        s=newstate(F);s.update(dict(zip(FIELDS[1:8],template)))
        law={**primary,'availability':avail}
        compare(law,s,arm,z,after,f'grid/{grid_count}');grid_count+=1
    assert grid_count==9600
    diagnostics={}
    s=newstate(4);s.update(gate=1,gate_life=2,stage=2,life=6,q=0,last=0)
    law={**primary,'availability':'1/2'}
    k=compare(law,s,'variable',0,False,'diagnostic/fuel4_write1')
    capture=sum(p for (ns,m),p in k.items() if m[METRICS.index('captures')])
    paid=sum(p for (ns,m),p in k.items() if m[METRICS.index('writes')])
    both=sum(p for (ns,m),p in k.items() if m[METRICS.index('writes')] and m[METRICS.index('captures')])
    assert capture==paid==both==Q(1,2)
    diagnostics['payable_selection']=dict(capture=str(capture),paid_write=str(paid),capture_given_paid=str(both/paid))
    law2={**law,'write':6};s2={**s,'fuel':8}
    first=compare(law2,s2,'variable',0,False,'diagnostic/fuel8_write6_first')
    second_capture=Q(0);recovery=Q(0);two=[]
    for (ns,m),p in first.items():
        nxt=compare(law2,statefrom(ns),'variable',0,False,'diagnostic/fuel8_write6_second')
        for (ns2,m2),p2 in nxt.items():
            assert m2[METRICS.index('trials')]==1
            assert ns[5]==ns2[5]==0
            if m2[METRICS.index('captures')]:
                second_capture+=p*p2
                if not m[METRICS.index('writes')]:
                    recovery+=p*p2;assert ns[0]==4 and ns2[0]==2 and m2[METRICS.index('writes')]==1
            two.append(dict(first=statefrom(ns),second=statefrom(ns2),mass=str(p*p2),first_moments=dict(zip(METRICS,m)),second_moments=dict(zip(METRICS,m2))))
    assert second_capture==Q(1,2) and recovery==Q(1,4)
    diagnostics['unpaid_write_recovery']=dict(second_capture=str(second_capture),recovered_capture_and_write=str(recovery),paths=two)
    # Compare actual compiled Lean tape evaluator, with one row per distinct input.
    rows=sorted(formal_rows)
    raw='\n'.join(rows)+'\n'
    proc=subprocess.run(final['command'],input=raw,text=True,capture_output=True,check=False,
                        env={**os.environ,'LEAN_PATH':final['lean_path']})
    assert proc.returncode==0,(proc.returncode,proc.stderr[:4000])
    answers=proc.stdout.splitlines();assert len(answers)==len(rows),(len(answers),len(rows),proc.stderr[:1000])
    for n,(row,got) in enumerate(zip(rows,answers)):
        got='\t'.join(got.split())
        assert got==formal_rows[row],('compiled Lean mismatch',n,row,got,formal_rows[row])
    write_gzip(HERE/'formal-fixtures.tsv.gz','\n'.join(row+'\t'+formal_rows[row] for row in rows)+'\n')
    write_gzip(HERE/'runtime-calls.jsonl.gz','\n'.join(jsontext(v['record']) for v in calls.values())+'\n')
    save('prefix-traces.json',sample_traces)
    save('runtime-results.json',dict(status='passed',composed_case_arms=composition,diagnostics=diagnostics,
        counts=dict(reachable_invocations=reachable_calls,guard_calls=grid_count,unique_calls=len(calls),
                    positive_weight_tapes=branch_count,checked_prefix_states=prefix_count,compiled_distinct_tapes=len(rows))))
    for n,h in final['sources'].items():assert digest(HERE/n)==h
    outputs=['formal-fixtures.tsv.gz','runtime-calls.jsonl.gz','prefix-traces.json','runtime-results.json']
    save('runtime-verification.json',dict(status='passed',timestamp_utc=datetime.now(timezone.utc).isoformat(),
        counts=json.loads((HERE/'runtime-results.json').read_text())['counts'],
        source_freeze_sha256=digest(HERE/'check-source-freeze.json'),formal_freeze_sha256=digest(final_path),
        checker_sha256=digest(Path(__file__)),parent_model_sha256=digest(PRED/'model.py'),
        outputs_sha256={n:digest(HERE/n) for n in outputs},
        scope='Exact finite full-state/increment kernels, inherited endpoint laws and weighted cumulative first moments; compiled Lean operational tapes agree on declared source-valid inputs. No universal Python refinement or new empirical validation.'))
    print(jsontext(dict(status='passed',**json.loads((HERE/'runtime-results.json').read_text())['counts'])))


if __name__=='__main__':main()
