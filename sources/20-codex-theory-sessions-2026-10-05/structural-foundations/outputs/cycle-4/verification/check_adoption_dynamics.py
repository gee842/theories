#!/usr/bin/env python3
"""Rolling finite-horizon adoption on the paid shared-repair plant.

Exact integer arithmetic; deterministic fault cycles. The actual planner uses
only finite terminal cash and payment-feasible schedules, never a viability
kernel. Physical implementation is independently expanded into slot ledgers.
"""
from dataclasses import dataclass, replace, asdict
from functools import lru_cache
from collections import deque, defaultdict
from itertools import product
from pathlib import Path
import json
import csv

@dataclass(frozen=True)
class Config:
    n: int = 8
    c: int = 1
    p: int = 4
    u: int = 2
    gap: int = 8
    deadline: int = 6
    install: int = 30
    cap: int = 240
    menu: tuple = tuple(range(1,9))
    hazard: bool = True

    def validate(self):
        assert self.n >= 1 and self.c >= 0 and self.p+self.c >= 0
        assert self.u >= 0 and self.install >= 0 and self.cap >= 0
        assert self.gap >= 1 and self.deadline >= 1
        assert self.menu and len(set(self.menu)) == len(self.menu)
        assert all(isinstance(k,int) and 0 <= k <= self.n for k in self.menu)


def quantities(c,k):
    if not c.hazard:
        return 0,0,c.p*c.n-c.u*k,c.gap
    if k == 0:
        return None
    t=(c.n+k-1)//k+2
    if t>c.deadline or t>c.gap:
        return None
    expense=3*c.n+(c.c*c.n+c.u*k)*t
    q=c.p*c.n-c.u*k
    return t,expense,q,c.gap-t


def cycle(c,b,old,new):
    info=quantities(c,new)
    if info is None:
        return None
    t,expense,q,healthy=info
    capital=c.install*max(new-old,0)
    b-=capital
    if b<expense:
        return None
    b-=expense
    for _ in range(healthy):
        b+=q
        if b<0:
            return None
        b=min(c.cap,b)
    return b


def expanded_cycle(c,b,old,new):
    """Separate slot-by-slot implementation including receipt/payment order."""
    info=quantities(c,new)
    if info is None:
        return None
    before=b
    capital=c.install*max(new-old,0)
    b-=capital
    ledger=[{'phase':'installation','cash':b,'expense':capital}]
    if b<0:
        return None
    if c.hazard:
        undiag,auth,execute=c.n,0,0
        ticks=0
        while (undiag,auth,execute)!=(0,0,0):
            nd,na,ne=min(new,undiag),auth,execute
            payment=c.c*c.n+c.u*new+nd+na+ne
            b-=payment;ticks+=1
            if b<0:
                return None
            ledger.append({'phase':'repair','tick':ticks,'stages':[nd,na,ne],
                           'expense':payment,'cash':b})
            undiag,auth,execute=undiag-nd,auth+nd-na,execute+na-ne
        assert ticks==info[0]
    for tick in range(info[3]):
        receipt=(c.p+c.c)*c.n
        b+=receipt
        ledger.append({'phase':'healthy_receipt','receipt':receipt,'cash':b})
        payment=c.c*c.n+c.u*new
        b-=payment
        if b<0:
            return None
        spill=max(0,b-c.cap);b=min(c.cap,b)
        ledger.append({'phase':'healthy_payment','expense':payment,'spill':spill,'cash':b})
    return {'start_cash':before,'old_channels':old,'new_channels':new,
            'end_cash':b,'minimum_cash':min(row['cash'] for row in ledger),'ledger':ledger}


@lru_cache(None)
def plan(c,b,old,horizon):
    if horizon==0:
        return b,()
    best=None
    for new in sorted(c.menu):
        nb=cycle(c,b,old,new)
        if nb is None:
            continue
        tail=plan(c,nb,new,horizon-1)
        if tail is None:
            continue
        candidate=tail[0],(new,)+tail[1]
        if best is None or candidate[0]>best[0] or (candidate[0]==best[0] and candidate[1]<best[1]):
            best=candidate
    return best


def actual_choice(c,b,old,horizon):
    # Explicit fallback if the preferred lookahead cannot be financed: use the
    # longest shorter complete horizon; fail when no full cycle is available.
    for depth in range(horizon,0,-1):
        result=plan(c,b,old,depth)
        if result is not None:
            return result[1][0],depth,result[0],result[1]
    return None


def run(c,cash,horizon,cycles=40):
    old=0;trace=[]
    for wave in range(1,cycles+1):
        chosen=actual_choice(c,cash,old,horizon)
        if chosen is None:
            return {'status':'no payable complete repair','failed_wave':wave,
                    'cash':cash,'channels':old,'completed_cycles':len(trace),'trace':trace}
        new,depth,value,word=chosen
        implementation=expanded_cycle(c,cash,old,new)
        assert implementation is not None
        nb=cycle(c,cash,old,new)
        assert nb==implementation['end_cash']
        trace.append({'wave':wave,'cash_before':cash,'old_channels':old,'chosen_channels':new,
                      'forecast_depth':depth,'forecast_terminal_cash':value,
                      'forecast_designs':word,'cash_after':nb,
                      'minimum_realized_cash':implementation['minimum_cash']})
        cash,old=nb,new
    return {'status':'completed requested finite trace','cash':cash,'channels':old,
            'completed_cycles':len(trace),'trace':trace}


def exhaustive_plan(c,b,old,horizon):
    best=None
    for word in product(sorted(c.menu),repeat=horizon):
        cash=b;current=old
        for new in word:
            record=expanded_cycle(c,cash,current,new)
            if record is None:
                break
            cash,current=record['end_cash'],new
        else:
            candidate=cash,word
            if best is None or candidate[0]>best[0] or (candidate[0]==best[0] and candidate[1]<best[1]):
                best=candidate
    return best


def exact_viability(c):
    # Deterministic periodic plant: existence of an infinite feasible path is
    # the greatest fixed point of states with at least one winning successor.
    states={(b,k) for b in range(c.cap+1) for k in range(c.n+1)}
    successors={};reverse=defaultdict(set)
    for b,k in states:
        nxt={(nb,new) for new in c.menu if (nb:=cycle(c,b,k,new)) is not None}
        successors[b,k]=nxt
        for target in nxt:
            reverse[target].add((b,k))
    remaining={s:len(nxt) for s,nxt in successors.items()}
    lost={s for s,nxt in successors.items() if not nxt};pending=deque(lost)
    while pending:
        target=pending.popleft()
        for source in reverse[target]:
            remaining[source]-=1
            if remaining[source]==0 and source not in lost:
                lost.add(source);pending.append(source)
    winning=states-lost
    assert all(any(nxt in winning for nxt in successors[s]) for s in winning)
    # A second descending-set implementation checks the same fixed point.
    naive=states
    while True:
        reduced={s for s in naive if successors[s]&naive}
        if reduced==naive:
            break
        naive=reduced
    assert naive==winning
    return winning,len(states)


def main():
    c=Config();c.validate()
    short=run(c,240,1,40)
    longer=run(c,240,2,40)
    assert [r['chosen_channels'] for r in short['trace']]==[2,2,2]
    assert [r['cash_after'] for r in short['trace']]==[140,100,60]
    assert short['failed_wave']==4
    assert longer['completed_cycles']==40 and all(r['chosen_channels']==4 for r in longer['trace'])
    assert [r['cash_after'] for r in longer['trace'][:3]]==[128,136,144]

    winning,viability_states=exact_viability(c)
    assert (240,0) in winning and (140,2) not in winning and (128,4) in winning
    minima={k:min(b for b,old in winning if old==k) for k in range(9)}
    assert minima=={k:88+30*max(4-k,0) for k in range(9)}

    # Exact comparisons with direct enumeration of every design word; the
    # alternate evaluator expands each physical slot and payment.
    comparisons=0
    for cash,old,horizon in product((0,88,96,156,184,207,208,240),(0,2,3,4,8),(1,2,3)):
        assert plan(c,cash,old,horizon)==exhaustive_plan(c,cash,old,horizon),(cash,old,horizon)
        comparisons+=1

    # Direct transition expansion versus compressed boundary transition.
    ledger_checks=0
    for b,old,new in product(range(241),range(9),range(1,9)):
        compressed=cycle(c,b,old,new)
        expanded=expanded_cycle(c,b,old,new)
        assert compressed==(None if expanded is None else expanded['end_cash'])
        ledger_checks+=1

    # An all-state invariant verifies h=2 actual behavior beyond a finite run.
    invariant=[]
    for b in range(88,241):
        choice=actual_choice(c,b,4,2)
        assert choice is not None and choice[0]==4
        assert actual_choice(c,b,4,1)[0]==4
        nb=cycle(c,b,4,4)
        assert nb==min(c.cap,b+8) and nb>=88
        invariant.append(b)

    grid=[]
    for cash,horizon in product(range(0,241),range(1,7)):
        outcome=run(c,cash,horizon,40)
        grid.append({'initial_cash':cash,'horizon':horizon,
                     'first_choice':outcome['trace'][0]['chosen_channels'] if outcome['trace'] else None,
                     'completed_cycles':outcome['completed_cycles'],
                     'failure_wave':outcome.get('failed_wave'),
                     'entered_certified_invariant':any(r['chosen_channels']==4 and r['cash_after']>=88 for r in outcome['trace'])})
    for horizon in range(2,7):
        minimum=min(r['initial_cash'] for r in grid if r['horizon']==horizon and r['entered_certified_invariant'])
        assert minimum==208
    assert not any(r['entered_certified_invariant'] for r in grid if r['horizon']==1)

    # Finite one-cycle duty with a freely permitted exit at its end: every
    # successful design is tested fairly, without assigning failure after exit.
    one_cycle={k:cycle(c,240,0,k) for k in c.menu}
    assert max((cash,-k) for k,cash in one_cycle.items() if cash is not None)==(140,-2)

    # No-fault control: zero diagnostic channels is admissible and sufficient.
    # A larger cap avoids hiding cash differences through immediate spilling.
    harmless=replace(c,hazard=False,menu=tuple(range(9)),cap=2000)
    nohazard=[actual_choice(harmless,240,0,h) for h in (1,2,3)]
    assert all(choice[0]==0 for choice in nohazard)

    # Genuine exact physical replication: action menu is the image of the old
    # menu, so extra intermediate channel designs are not silently introduced.
    scale_checks=0
    for factor in (2,3,5):
        scaled=replace(c,n=8*factor,cap=240*factor,menu=tuple(factor*k for k in c.menu))
        for cash,old,horizon in product((88,156,184,208,240),(0,2,3,4),(1,2,3)):
            p=plan(c,cash,old,horizon)
            q=plan(scaled,factor*cash,factor*old,horizon)
            assert (p is None)==(q is None)
            if p is not None:
                assert q==(factor*p[0],tuple(factor*k for k in p[1]))
            scale_checks+=1

    # Two-design threshold in a no-cap, sufficiently funded comparison.
    # Under constant cycle returns, immediate rather than delayed upgrade
    # weakly dominates whenever adopting the higher-return design is chosen.
    threshold_checks=0
    for install in sorted(set(range(0,81,5)) | {24,48,72}):
        for horizon in range(1,7):
            two=replace(c,install=install,cap=10000,menu=(2,4))
            result=plan(two,5000,0,horizon)
            difference=horizon*48-2*install
            expected=4 if difference>0 else 2
            assert result[1][0]==expected
            assert len(set(result[1]))==1
            threshold_checks+=1

    out={'status':'all assertions passed','short_horizon':short,'two_cycle_horizon':longer,
         'short_first_cycle_ledger':expanded_cycle(c,240,0,2),
         'longer_first_cycle_ledger':expanded_cycle(c,240,0,4),
         'all_state_invariant':{'channels':4,'cash_min':88,'cash_max':240,'states_checked':len(invariant),'actual_horizons_verified':[1,2]},
         'viability_states':viability_states,'minimum_viable_cash_by_installed_channels':minima,
         'capacity_loss':{'initial_winning':True,'after_first_h1_cycle_winning':False,'after_first_h2_cycle_winning':True},
         'exhaustive_plan_comparisons':comparisons,'slot_ledger_comparisons':ledger_checks,
         'wealth_horizon_grid_rows':len(grid),'replication_checks':scale_checks,
         'two_design_threshold_checks':threshold_checks,
         'one_cycle_safe_exit_terminal_cash':one_cycle,
         'no_hazard_choices':nohazard,
         'minimum_initial_cash_horizons_2_through_6':208,
         'config':asdict(c),
         'limits':['Periodic fault law, not every prior-cycle fault schedule',
                   'Perfectly known model and free planning computation; horizon/objective supplied',
                   'Installation has zero latency; removal free with no salvage value',
                   'No empirical data; no evolutionary origin of objective or horizon modeled',
                   'Safe-exit control assumes declared duty ends and closure is permitted without extra cost']}
    directory=Path(__file__).parent
    (directory/'adoption-dynamics-results.json').write_text(json.dumps(out,indent=2)+'\n')
    with (directory/'adoption-frontier.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(grid[0]));writer.writeheader();writer.writerows(grid)
    print(json.dumps({k:out[k] for k in ['status','exhaustive_plan_comparisons','slot_ledger_comparisons','wealth_horizon_grid_rows','replication_checks','two_design_threshold_checks']},indent=2))

if __name__=='__main__':main()
