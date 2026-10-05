"""Exact finite account-access study. All arithmetic uses fractions.

Operational kernel follows the snapshotted recoverable-inquiry model;
treasury access/normalization and vector support probes are explicit extensions.
No code in the original research workspace is imported or modified.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from typing import NamedTuple

METRICS = ('failure','expense','burden','unrecovered','tests','repairs',
           'rebuilds','upkeep','inquiry_expense','output','terminal_cash','terminal_treasury')
INDEX = {v:i for i,v in enumerate(METRICS)}
ZERO = (Q(0),)*len(METRICS)
WEIGHTS = {
    'failure':(1,0,0,0), 'recovery':(0,0,0,1),
    'expense':(0,1,0,0), 'burden':(0,0,1,0),
    'failure_expense':(12,1,0,0),
    'failure_expense_burden':(12,1,4,0),
    'mixed':(4,1,1,4),
}

@dataclass(frozen=True)
class Config:
    cap:int=8
    stock_cap:int=3
    onset:Q=Q(1,10)
    clearance:Q=Q(1,20)
    damage_healthy:Q=Q(1,10)
    damage_fault:Q=Q(4,5)
    sensitivity:Q=Q(9,10)
    specificity:Q=Q(9,10)
    output_rate:int=2
    upkeep:int=1
    rebuild:int=3
    test:int=2
    repair:int=3
    test_burden:Q=Q(1,20)

class State(NamedTuple):
    remaining:int
    stock:int
    cash:int
    treasury:int
    ready:int
    belief:Q
    unlock:int

@dataclass(frozen=True)
class Branch:
    probability:Q
    child:State
    signal:str
    repair:int
    expense:int
    output:int

@dataclass(frozen=True)
class Action:
    support:str
    test:bool
    repair_rule:tuple
    stage:tuple
    branches:tuple

class Engine:
    def __init__(self, cfg=Config()):
        self.cfg=cfg
        self.branch_checks=0
        self.solve=lru_cache(None)(self._solve)
        self.actions=lru_cache(None)(self._actions)

    def normalize(self,s):
        n,x,b,k,r,p,d=s
        assert n>=0 and 0<=x<=self.cfg.stock_cap and 0<=b<=self.cfg.cap and k>=0
        assert p>=0 and p<=1 and d in (-1,0,1)
        if x==0 or n==0:
            return State(0,x,b,k,0,Q(0),d)
        if d==0:
            transfer=min(k,self.cfg.cap-b)
            b+=transfer;k-=transfer
        return State(n,x,b,k,r,Q(p),d)

    def terminal(self,s):
        v=list(ZERO)
        v[0]=Q(s.stock==0);v[3]=Q(s.stock<2)
        v[10]=Q(s.cash);v[11]=Q(s.treasury)
        return tuple(v)

    def diagnostic(self,p):
        c=self.cfg
        out=[]
        for label,l1,l0 in (('positive',c.sensitivity,1-c.specificity),
                            ('negative',1-c.sensitivity,c.specificity)):
            mass=p*l1+(1-p)*l0
            if mass: out.append((label,mass,p*l1/mass))
        assert sum(o[1] for o in out)==1
        return tuple(out)

    def production(self,p,x,repair):
        c=self.cfg
        effective=Q(0) if repair else p
        groups={}
        for hidden,prior in ((0,1-effective),(1,effective)):
            risk=c.damage_fault if hidden else c.damage_healthy
            for damage,pr in ((0,1-risk),(1,risk)):
                xp=max(0,min(c.stock_cap,x+1+repair-2*damage))
                mass=groups.setdefault(xp,[Q(0),Q(0)])
                mass[hidden]+=prior*pr
        out=[]
        for xp,(p0,p1) in sorted(groups.items()):
            mass=p0+p1
            if mass:
                next_p=c.onset+(1-c.onset-c.clearance)*p1/mass
                out.append((xp,mass,next_p))
        assert sum(o[1] for o in out)==1
        return tuple(out)

    def _actions(self,s):
        assert s==self.normalize(s)
        if not s.remaining:return ()
        n,x,b,k,r,p,d=s;c=self.cfg
        infrastructure=[('drop',0,0)]
        if r and b>=c.upkeep:infrastructure.append(('keep',c.upkeep,1))
        if not r and b>=c.rebuild:infrastructure.append(('rebuild',c.rebuild,1))
        actions=[]
        for support,fee,rnext in infrastructure:
            tests=[False]
            if r and support=='keep' and b>=fee+c.test:tests.append(True)
            for test in tests:
                upfront=fee+int(test)*c.test
                observations=self.diagnostic(p) if test else (('none',Q(1),p),)
                choices=(0,1) if b-upfront>=c.repair else (0,)
                for prescription in product(choices,repeat=len(observations)):
                    v=list(ZERO);branches=[]
                    v[2]=int(test)*c.test_burden
                    v[4]=Q(test);v[6]=Q(support=='rebuild');v[7]=Q(support=='keep')
                    v[8]=Q(upfront)
                    for (label,po,posterior),repair in zip(observations,prescription):
                        spend=upfront+c.repair*repair
                        assert 0<=spend<=b
                        v[1]+=po*spend
                        v[2]+=po*(1-posterior)*repair
                        v[5]+=po*repair
                        for xp,pp,pnext in self.production(posterior,x,repair):
                            income=c.output_rate*xp
                            raw=b-spend+income
                            bp=min(c.cap,raw);kp=k+raw-bp
                            assert bp+kp+spend==b+k+income
                            child=self.normalize(State(n-1,xp,bp,kp,rnext,pnext,max(0,d-1) if d>=0 else -1))
                            assert child.cash+child.treasury==bp+kp
                            pr=po*pp
                            v[9]+=pr*income
                            branches.append(Branch(pr,child,label,repair,spend,income))
                            self.branch_checks+=1
                    assert sum(br.probability for br in branches)==1
                    actions.append(Action(support,test,tuple(zip((o[0] for o in observations),prescription)),tuple(v),tuple(branches)))
        assert actions
        return tuple(actions)

    @staticmethod
    def score(values,weights):
        return sum((w*v for w,v in zip(weights,values[:4]) if w),Q(0))

    def _solve(self,s,weights):
        assert s==self.normalize(s)
        if not s.remaining:return self.terminal(s),-1
        best=None
        for ai,a in enumerate(self.actions(s)):
            v=list(a.stage)
            for br in a.branches:
                cv,_=self.solve(br.child,weights)
                for j,value in enumerate(cv):
                    if value:v[j]+=br.probability*value
            v=tuple(v)
            key=(self.score(v,weights),v[1],v[2],v[3],v[0],v[4],v[6],ai)
            if best is None or key<best[0]:best=(key,v,ai)
        return best[1],best[2]

    def result(self,state,weights):
        original=state
        s=self.normalize(state)
        values,ai=self.solve(s,weights)
        assert values[10]+values[11]+values[1]==original.cash+original.treasury+values[9]
        action=self.actions(s)[ai] if ai>=0 else None
        return {'support_value':str(self.score(values,weights)),
                'metrics_exact':dict(zip(METRICS,map(str,values))),
                'metrics':dict(zip(METRICS,map(float,values))),
                'normalized_cash':s.cash,'normalized_treasury':s.treasury,
                'root_action':None if action is None else {
                    'support':action.support,'test':action.test,'repair_rule':dict(action.repair_rule)},
                'initial_action_count':len(self.actions(s)) if ai>=0 else 0,
                'ledger_residual':'0'}

    def reachable_policy(self,state,weights):
        initial=self.normalize(state)
        reachable={initial:Q(1)}
        rows=[]
        for n in range(initial.remaining,0,-1):
            current=[(s,p) for s,p in reachable.items() if s.remaining==n]
            for s,mass in current:
                _,ai=self.solve(s,weights)
                a=self.actions(s)[ai]
                rows.append({'state':[str(v) for v in s], 'probability':str(mass),
                             'support':a.support,'test':a.test,'repair_rule':dict(a.repair_rule)})
                for br in a.branches:
                    reachable[br.child]=reachable.get(br.child,Q(0))+mass*br.probability
        return rows

def make_state(horizon=4,stock=2,cash=0,total=5,ready=0,belief='1',access='barred'):
    return State(horizon,stock,cash,total-cash,ready,Q(belief),{'barred':-1,'immediate':0,'delayed':1}[access])
