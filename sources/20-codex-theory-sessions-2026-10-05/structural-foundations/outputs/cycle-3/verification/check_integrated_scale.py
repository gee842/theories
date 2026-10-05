#!/usr/bin/env python3
"""Paid shared diagnosis: analytic frontier and finite safety-game cross-check.

Standard library only. The checker enumerates all admissible stage schedules,
not just the proposed fastest pipeline. Nature chooses quiet/fault in healthy
states, with onset spacing; no repair output until all modules are restored.
Hidden bits are quotientable by perfect paid diagnosis and costless within-
episode registers. This is not the separate paid-memory/succession model.
"""
from collections import deque, defaultdict
from dataclasses import dataclass, asdict
from itertools import product
from pathlib import Path
import csv
import json

@dataclass(frozen=True)
class Config:
    n: int
    k: int
    c: int = 1
    p: int = 4
    u: int = 2
    gap: int = 8
    deadline: int = 6
    cap: int = 100

    def validate(self):
        assert 1 <= self.k <= self.n
        assert self.c >= 0 and self.u >= 0 and self.p + self.c >= 0
        assert self.gap >= 0 and self.deadline >= 1 and self.cap >= 0


def analytic(c):
    c.validate()
    t = (c.n+c.k-1)//c.k+2
    expense = 3*c.n+(c.c*c.n+c.u*c.k)*t
    net = c.p*c.n-c.u*c.k
    viable = (t <= c.deadline and net >= 0 and c.cap >= expense
              and max(c.gap-t,0)*net >= expense)
    return {'duration':t,'episode_cost':expense,'healthy_net':net,
            'minimum_healthy_slots':max(c.gap-t,0),
            'replenishment':max(c.gap-t,0)*net,
            'minimum_initial_cash':expense if viable else None}


def fault_choices(c,u,a,e,age,b):
    outcomes = set()
    for nd,na,ne in product(range(min(c.k,u)+1),range(a+1),range(e+1)):
        expense = c.c*c.n+c.u*c.k+nd+na+ne
        if b < expense:
            continue
        nxt=(u-nd,a+nd-na,e+na-ne)
        if nxt == (0,0,0):
            outcomes.add(('h',min(c.gap,age+1),b-expense))
        elif age+1 < c.deadline:
            outcomes.add(('f',*nxt,age+1,b-expense))
    return outcomes


def event_choices(c,s):
    if s[0]=='f':
        _,u,a,e,age,b=s
        return [fault_choices(c,u,a,e,age,b)]
    _,age,b=s
    nb=b+c.p*c.n-c.u*c.k
    quiet={('h',min(c.gap,age+1),min(c.cap,nb))} if nb>=0 else set()
    choices=[quiet]
    if age==c.gap:
        choices.append(fault_choices(c,c.n,0,0,0,b))
    return choices


def exact_game(c):
    c.validate()
    initials=[('h',c.gap,b) for b in range(c.cap+1)]
    todo=deque(initials); seen=set(initials); transitions={}
    while todo:
        s=todo.popleft(); events=event_choices(c,s); transitions[s]=events
        for event in events:
            for nxt in event:
                if nxt not in seen:
                    seen.add(nxt);todo.append(nxt)
    # A state loses when any environment event has no surviving response.
    remaining={}; parents=defaultdict(list); losing=set(); queue=deque()
    for s,events in transitions.items():
        for i,event in enumerate(events):
            remaining[(s,i)]=len(event)
            for nxt in event:
                parents[nxt].append((s,i))
            if not event and s not in losing:
                losing.add(s);queue.append(s)
    while queue:
        lost=queue.popleft()
        for key in parents[lost]:
            remaining[key]-=1
            s,_=key
            if remaining[key]==0 and s not in losing:
                losing.add(s);queue.append(s)
    winning=seen-losing
    assert all(all(any(nxt in winning for nxt in event) for event in transitions[s])
               for s in winning)
    cash=[s[2] for s in initials if s in winning]
    threshold=min(cash) if cash else None
    if cash:
        assert cash==list(range(threshold,c.cap+1))
    return threshold,len(seen),len(winning)


def pipeline(n,k):
    u,a,e=n,0,0
    out=[]
    while (u,a,e)!=(0,0,0):
        nd,na,ne=min(k,u),a,e
        out.append((nd,na,ne))
        u,a,e=u-nd,a+nd-na,e+na-ne
    return out


def main():
    cases=[]
    # All fixed designs at n=1..4; includes viable and nonviable bottlenecks.
    configs=[Config(n,k,cap=60) for n in range(1,5) for k in range(1,n+1)]
    # Adversarial boundaries: insufficient storage, exact storage, late/early
    # onset, negative quiet return, zero carrying expense, tight deadline.
    configs += [Config(2,1,cap=b) for b in (21,22,23)]
    configs += [Config(2,1,gap=g,cap=40) for g in (0,4,7,9)]
    configs += [Config(2,1,p=p,cap=40) for p in (-1,0,3,5)]
    configs += [Config(2,1,deadline=h,cap=40) for h in (3,4)]
    configs += [Config(2,1,c=0,u=0,p=2,gap=6,cap=6)]
    for c in configs:
        expected=analytic(c); observed,states,wins=exact_game(c)
        assert observed==expected['minimum_initial_cash'],(c,expected,observed)
        cases.append({'config':asdict(c),**expected,'exact_minimum_cash':observed,
                      'states':states,'winning_states':wins})
    rows=[]
    for n in range(1,65):
        for k in range(1,n+1):
            c=Config(n,k,cap=10000);a=analytic(c)
            trace=pipeline(n,k)
            assert len(trace)==a['duration']
            assert sum(sum(t) for t in trace)==3*n
            assert sum(sum(t)+n+2*k for t in trace)==a['episode_cost']
            rows.append({'n':n,'k':k,**a})
    # Exact proportional copies preserve normalized balances and feasibility.
    proportional=0
    for n in range(1,9):
        for k in range(1,n+1):
            a=analytic(Config(n,k,cap=20*n))
            for factor in (2,3,5):
                b=analytic(Config(factor*n,factor*k,cap=20*factor*n))
                assert b['duration']==a['duration']
                assert b['episode_cost']==factor*a['episode_cost']
                assert b['healthy_net']==factor*a['healthy_net']
                assert (a['minimum_initial_cash'] is None)==(b['minimum_initial_cash'] is None)
                proportional+=1
    example=[{'k':k,**analytic(Config(8,k,cap=200))} for k in range(1,9)]
    assert [r['k'] for r in example if r['minimum_initial_cash'] is not None]==[4]
    fastest=min(example,key=lambda row:row['duration'])
    assert fastest['k']==8 and fastest['episode_cost']-fastest['replenishment']==16
    install_examples=[]
    for fee in (1,10):
        choices=[]
        for k in range(1,9):
            a=analytic(Config(8,k,u=1,cap=200))
            if a['minimum_initial_cash'] is not None:
                choices.append((fee*k+a['episode_cost'],k))
        best=min(choices)
        install_examples.append({'installation_fee_per_channel':fee,'least_endowment':best[0],
                                 'optimal_k':best[1],'feasible_design_costs':choices})
    assert [(r['optimal_k'],r['least_endowment']) for r in install_examples]==[(4,76),(3,109)]
    out={'status':'all assertions passed','exact_game_cases':len(cases),
         'enumerated_game_states':sum(r['states'] for r in cases),
         'frontier_rows':len(rows),'proportional_scaling_checks':proportional,
         'eight_module_example':example,'installation_examples':install_examples,
         'exact_cases':cases,
         'limits':['Synthetic model, no empirical fit','Fixed channel count during operation',
                   'All-module shutdown during a fault wave','Perfect diagnosis and free intra-episode bit registers',
                   'Finite exact checks support analytic proof, not general machine proof']}
    base=Path(__file__).parent
    (base/'integrated-scale-results.json').write_text(json.dumps(out,indent=2)+'\n')
    with (base/'integrated-scale-frontier.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(json.dumps({k:out[k] for k in ('status','exact_game_cases','enumerated_game_states','frontier_rows','proportional_scaling_checks')},indent=2))

if __name__=='__main__':main()
