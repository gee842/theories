"""Independent exact latent-event oracle for the two-account study.

No imports from the original research workspace or the new model. Written
from the frozen chronology; groups latent histories by complete public
observations before computing each posterior. H1/H2 only by default.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

@dataclass(frozen=True)
class State:
    t:int
    x:int
    b:int
    treasury:int
    ready:int
    p:Q
    unlock:int=-1

@dataclass(frozen=True)
class Choice:
    support:str
    test:bool
    repair_rule:tuple

def canonical(s,mode):
    if s.x==0 or s.t==0:
        return State(0,s.x,s.b,s.treasury,0,Q(0),s.unlock)
    if mode=='open' or (mode=='delayed' and s.unlock==0):
        total=s.b+s.treasury
        return State(s.t,s.x,min(8,total),max(0,total-8),s.ready,s.p,s.unlock)
    assert mode in ('barred','delayed')
    return s

def choices(s,mode):
    s=canonical(s,mode)
    if s.t==0:return []
    infra=[('drop',0)]
    if s.ready and s.b>=1:infra.append(('keep',1))
    if not s.ready and s.b>=3:infra.append(('rebuild',3))
    out=[]
    for support,fee in infra:
        for test in ((False,True) if support=='keep' and s.b>=3 else (False,)):
            upfront=fee+2*test
            labels=('positive','negative') if test else ('none',)
            # All diagnostic masses are positive for these .9/.1 likelihoods.
            for repairs in product((0,1) if s.b-upfront>=3 else (0,),repeat=len(labels)):
                out.append(Choice(support,test,tuple(zip(labels,repairs))))
    return out

def transition(s,a,mode):
    """Return expected expenses/burden, exact visible branches, ledger checks.

    This enumerates latent fault, noisy signal, damage, and next fault. It
    never calls diagnostic() or production() from either implementation.
    """
    s=canonical(s,mode)
    assert a in choices(s,mode)
    fee={'drop':0,'keep':1,'rebuild':3}[a.support]
    nextready=int(a.support!='drop')
    repair_rule=dict(a.repair_rule)
    observations=defaultdict(lambda:[Q(0),Q(0)])
    expense=Q(0);burden=Q(0);output=Q(0);repairs=Q(0)
    prefix_checks=0
    for theta,prtheta in ((0,1-s.p),(1,s.p)):
        signals=(('positive',Q(9,10) if theta else Q(1,10)),
                 ('negative',Q(1,10) if theta else Q(9,10))) if a.test else (('none',Q(1)),)
        for signal,prsignal in signals:
            repair=repair_rule[signal]
            bill=fee+2*a.test+3*repair
            assert bill<=s.b
            effective=0 if repair else theta
            damage_p=Q(4,5) if effective else Q(1,10)
            for damage,prdamage in ((0,1-damage_p),(1,damage_p)):
                mass=prtheta*prsignal*prdamage
                if not mass:continue
                xp=max(0,min(3,s.x+1+repair-2*damage))
                cash=s.b-bill+2*xp
                bp=min(8,cash)
                kp=s.treasury+cash-bp
                assert bp+kp+bill==s.b+s.treasury+2*xp
                prefix_checks+=1
                expense+=mass*bill
                burden+=mass*(Q(1,20)*a.test+(1-theta)*repair)
                output+=mass*2*xp
                repairs+=mass*repair
                next_fault_p=Q(19,20) if effective else Q(1,10)
                key=(signal,xp,bp,kp,nextready)
                observations[key][0]+=mass*(1-next_fault_p)
                observations[key][1]+=mass*next_fault_p
    branches=[]
    for (signal,xp,bp,kp,rp),(m0,m1) in sorted(observations.items()):
        mass=m0+m1
        unlock=max(0,s.unlock-1) if mode=='delayed' else s.unlock
        child=canonical(State(s.t-1,xp,bp,kp,rp,m1/mass,unlock),mode)
        branches.append((signal,mass,child))
    assert sum((pr for _,pr,_ in branches),Q(0))==1
    return {'expense':expense,'burden':burden,'output':output,'repairs':repairs,
            'tests':Q(a.test),'rebuilds':Q(a.support=='rebuild'),
            'upkeep':Q(a.support=='keep'),'inquiry_expense':Q(fee+2*a.test),
            'branches':branches,'prefix_checks':prefix_checks}

@lru_cache(None)
def solve(s,weights,mode):
    """Exact finite policy tree optimization, four terminal/additive metrics."""
    s=canonical(s,mode)
    if s.t==0:
        metrics=(Q(s.x==0),Q(0),Q(0),Q(s.x<2))
        return sum(w*v for w,v in zip(weights,metrics)),metrics,None
    candidates=[]
    for ai,a in enumerate(choices(s,mode)):
        tr=transition(s,a,mode)
        metrics=[Q(0),tr['expense'],tr['burden'],Q(0)]
        for _,pr,child in tr['branches']:
            _,childmetrics,_=solve(child,weights,mode)
            metrics=[v+pr*cv for v,cv in zip(metrics,childmetrics)]
        scalar=sum(w*v for w,v in zip(weights,metrics))
        candidates.append((scalar,tuple(metrics),ai,a))
    scalar,metrics,_,a=min(candidates,key=lambda row:(row[0],row[1],row[2]))
    return scalar,metrics,a

def serial(o):
    if isinstance(o,Q):return str(o)
    if isinstance(o,(State,Choice)):return {k:serial(v) for k,v in vars(o).items()}
    if isinstance(o,tuple):return [serial(v) for v in o]
    if isinstance(o,list):return [serial(v) for v in o]
    if isinstance(o,dict):return {str(k):serial(v) for k,v in o.items()}
    return o

def benchmark():
    weights=(Q(1),Q(0),Q(0),Q(0))
    low=State(2,2,0,5,0,Q(1))
    high=State(2,2,1,4,0,Q(1))
    assert choices(low,'barred')==choices(high,'barred')
    assert len(choices(low,'barred'))==1
    low_result=solve(low,weights,'barred')
    high_result=solve(high,weights,'barred')
    assert low_result[0]==Q(153,250)
    assert high_result[0]==0
    assert high_result[1][1]==Q(12,5)
    assert high_result[1][2]==Q(1,25)
    open_low=solve(low,weights,'open')
    open_high=solve(high,weights,'open')
    assert open_low==open_high
    return {'kind':'independent exact latent-event and policy-tree certificate',
            'metric_order':['failure','expense','burden','terminal_stock_below_2'],
            'identical_initial_action_witness':{
                'low':low,'high':high,'shared_actions':choices(low,'barred'),
                'barred_low':low_result,'barred_high':high_result,
                'immediate_access_both':open_low,
                'first_transition_low':transition(low,choices(low,'barred')[0],'barred'),
                'first_transition_high':transition(high,choices(high,'barred')[0],'barred')},
            'cache_info':str(solve.cache_info())}

if __name__=='__main__':
    result=serial(benchmark())
    target=Path(__file__).with_name('audit_oracle_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
