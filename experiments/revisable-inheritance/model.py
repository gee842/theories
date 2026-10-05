"""Finite team decisions with model-relative inherited records."""
from dataclasses import dataclass,asdict,replace
from itertools import product
from math import ceil,log2
import numpy as np

FORMATS=('last','count','timed','raw')


@dataclass(frozen=True)
class Costs:
    retention_bit: float=.003
    inspect: float=.01
    setup: float=.003
    payload_bit: float=.01
    ready: float=.015
    diagnostic: float=.16
    response: float=.3
    loss: float=1.
    cap: float=.4


def rates(family,n=4):
    assert n%2==0
    low=[.05]*n;high=[.45]*n
    ordered=[low[:n//2]+high[n//2:],high[:n//2]+low[n//2:]]
    return {'homogeneous':[low,high], 'ordered':ordered,
            'expanded':[low,high]+ordered}[family]


def bits_for(fmt,n=4):
    return {'last':0,'count':ceil(log2(n+1)),
            'timed':2*ceil(log2(n//2+1)),'raw':n}[fmt]


def projection(word,fmt):
    n=len(word)
    return {'last':(), 'count':(sum(word),),
            'timed':(sum(word[:n//2]),sum(word[n//2:])),
            'raw':tuple(word)}[fmt]


def histories(family,z,n=4):
    rr=rates(family,n);records=[]
    for word in product((0,1),repeat=n):
        likelihood=np.array([np.prod([h if b else 1-h for h,b in zip(r,word)]) for r in rr])
        mass=float(likelihood.mean())
        posterior=likelihood/likelihood.sum()
        need=float(sum(w*(r[-1] if z==0 else 1-r[-1]) for w,r in zip(posterior,rr)))
        records.append(dict(word=list(word),mass=mass,need=need,models=posterior.tolist()))
    assert abs(sum(r['mass'] for r in records)-1)<1e-12
    return records


def types_for(family,z,fmt,n=4):
    grouped={}
    for row in histories(family,z,n):
        key=projection(row['word'],fmt)
        if key not in grouped:grouped[key]=dict(key=list(key),mass=0.,need_mass=0.,models_mass=np.zeros(len(row['models'])))
        target=grouped[key];target['mass']+=row['mass']
        target['need_mass']+=row['mass']*row['need']
        target['models_mass']+=row['mass']*np.array(row['models'])
    result=[]
    for key in sorted(grouped):
        v=grouped[key]
        result.append(dict(key=v['key'],mass=v['mass'],need=v['need_mass']/v['mass'],
                           models=(v['models_mass']/v['mass']).tolist()))
    return result


def action_cost(p,action,costs):
    # Diagnostic is itself charged separately; this returns response and harm.
    if action==0:return costs.loss*p
    if action==1:return costs.response
    if action==2:return costs.response*p
    raise ValueError(action)


def response_options(ready,spent,costs,allow_diagnostic=True):
    result=[0,1]
    if ready and allow_diagnostic and spent+costs.diagnostic<=costs.cap+1e-12:result.append(2)
    return result


def optimal_action(p,ready,spent,costs,allow_diagnostic=True):
    return min(response_options(ready,spent,costs,allow_diagnostic),
               key=lambda a:(action_cost(p,a,costs)+(costs.diagnostic if a==2 else 0),a))


def continuation(types,base,bits,costs,channel,ready_constraint=None,
                 allow_diagnostic=True,brute=False):
    """Solve joint sender/receiver decisions after private observation."""
    ready_values=(0,1) if ready_constraint is None else (ready_constraint,)
    actions=list(product(ready_values,(0,1) if channel and bits else (0,)))
    best=None
    # Enumeration over decoders is small; brute=True is an independent check.
    decoders=product((0,1),(0,1,2) if allow_diagnostic else (0,1))
    candidates=product(actions,repeat=len(types)) if brute else decoders
    for candidate in candidates:
        chosen=[]
        if brute:
            policy=list(candidate)
            decoder={}
            for u in (0,1):
                members=[t for t,a in zip(types,policy) if a==(u,0)]
                mass=sum(t['mass'] for t in members)
                if mass:
                    p=sum(t['mass']*t['need'] for t in members)/mass
                    decoder[u]=optimal_action(p,u,base+u*costs.ready,costs,allow_diagnostic)
                else:decoder[u]=0
        else:decoder=dict(enumerate(candidate))
        valid=True
        for i,t in enumerate(types):
            options=[]
            for u,send in ([policy[i]] if brute else actions):
                spent=base+u*costs.ready+send*bits*costs.payload_bit
                if spent>costs.cap+1e-12:continue
                a=optimal_action(t['need'],u,spent,costs,allow_diagnostic) if send else decoder[u]
                if a not in response_options(u,spent,costs,allow_diagnostic):continue
                inquiry=spent+(costs.diagnostic if a==2 else 0)
                total=inquiry+action_cost(t['need'],a,costs)
                options.append((total,u,send,a,inquiry))
            if not options:valid=False;break
            total,u,send,a,inquiry=min(options)
            chosen.append(dict(type=t['key'],mass=t['mass'],need=t['need'],
                               ready=u,send=send,response=a,inquiry=inquiry,total=total))
        if not valid:continue
        total=sum(row['mass']*row['total'] for row in chosen)
        if best is None or total<best['total_loss']-1e-12:
            best=dict(total_loss=total,branches=chosen)
    if best is None:return None
    signals=[]
    for u in (0,1):
        members=[r for r in best['branches'] if r['ready']==u and not r['send']]
        mass=sum(r['mass'] for r in members)
        if mass:
            p=sum(r['mass']*r['need'] for r in members)/mass
            actions_used={r['response'] for r in members}
            assert len(actions_used)==1
            a=actions_used.pop()
            optimum=optimal_action(p,u,base+u*costs.ready,costs,allow_diagnostic)
            val=lambda action:action_cost(p,action,costs)+(costs.diagnostic if action==2 else 0)
            assert abs(val(a)-val(optimum))<1e-10,(p,u,a,optimum)
            signals.append(dict(ready=u,message='silent',mass=mass,need=p,response=a))
    for row in best['branches']:
        if row['send']:signals.append(dict(ready=row['ready'],message=row['type'],mass=row['mass'],need=row['need'],response=row['response']))
    best['signals']=signals
    best['inquiry_cost']=sum(r['mass']*r['inquiry'] for r in best['branches'])
    best['operating_loss']=best['total_loss']-best['inquiry_cost']
    best['readiness_probability']=sum(r['mass']*r['ready'] for r in best['branches'])
    best['send_probability']=sum(r['mass']*r['send'] for r in best['branches'])
    best['diagnostic_probability']=sum(r['mass']*(r['response']==2) for r in best['branches'])
    best['unused_ready_probability']=sum(r['mass']*(r['ready'] and r['response']!=2) for r in best['branches'])
    return best


def solve(family,fmt,costs=Costs(),n=4,allow_payload=True,ready_constraint=None,
          allow_diagnostic=True,brute=False):
    bits=bits_for(fmt,n);retention=bits*costs.retention_bit
    contexts=[]
    for z in (0,1):
        best=None
        for inspect in ((0,1) if bits else (0,)):
            ts=types_for(family,z,fmt if inspect else 'last',n)
            for channel in ((0,1) if inspect and allow_payload else (0,)):
                base=retention+inspect*costs.inspect+channel*costs.setup
                result=continuation(ts,base,bits,costs,channel,ready_constraint,allow_diagnostic,brute)
                if result is None:continue
                result.update(z=z,inspect=inspect,channel=channel,
                              components=dict(retention=retention,inspection=inspect*costs.inspect,
                                 setup=channel*costs.setup,readiness=costs.ready*result['readiness_probability'],
                                 payload=costs.payload_bit*bits*result['send_probability'],
                                 diagnostic=costs.diagnostic*result['diagnostic_probability']))
                assert abs(sum(result['components'].values())-result['inquiry_cost'])<1e-10
                if best is None or result['total_loss']<best['total_loss']-1e-12:best=result
        if best is None:return dict(feasible=False)
        contexts.append(best)
    result=dict(feasible=True,family=family,format=fmt,bits=bits,n=n,costs=asdict(costs),
                controls=dict(allow_payload=allow_payload,ready_constraint=ready_constraint,allow_diagnostic=allow_diagnostic),
                contexts=contexts)
    for key in ['total_loss','operating_loss','inquiry_cost','readiness_probability','send_probability',
                'diagnostic_probability','unused_ready_probability']:
        result[key]=.5*sum(c[key] for c in contexts)
    result['inspect_probability']=.5*sum(c['inspect'] for c in contexts)
    result['components']={key:.5*sum(c['components'][key] for c in contexts) for key in contexts[0]['components']}
    return result


def full_information_risk(family,fmt,n=4,costs=Costs()):
    return .5*sum(t['mass']*min(costs.loss*t['need'],costs.response)
                   for z in (0,1) for t in types_for(family,z,fmt,n))


def path_details(path,family):
    z=path[-1];word=[int(a!=b) for a,b in zip(path,path[1:])]
    row=next(r for r in histories(family,z,len(word)) if r['word']==word)
    return dict(path=list(path),last=z,count=sum(word),timed=list(projection(word,'timed')),
                family=family,models=row['models'],need=row['need'])
