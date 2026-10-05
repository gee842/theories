#!/usr/bin/env python3
"""Independent exact ledger, reserve-pump, and truncation checks.

Reconstructs the declared 42 channels; imports no producer. No CTMC probabilities
are simulated. Tail bounds use exact rational positive-series inequalities.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPECIES = ('R','C','CF','Y','D','F','A0','A1','G0','G1','GF0','GF1','YG0','YG1')
N = {s: (0 if s == 'F' else 2 if s.startswith('YG') else 1) for s in SPECIES}
U = {s: int(s in ('F','CF','GF0','GF1')) for s in SPECIES}
FREE_POOL = {s: int(s in ('F','GF0','GF1')) for s in SPECIES}
W = {s: N[s] - int(s == 'D') + U[s] for s in SPECIES}
S = {s: W[s] + FREE_POOL[s] for s in SPECIES}


def channels():
    rows = {}
    def add(name, lhs, rhs):
        rows[name] = (lhs, rhs)
    add('assemble', {'R':1}, {'C':1})
    add('Cwear', {'C':1}, {'D':1})
    add('reproduce', {'R':1,'Y':1}, {'Y':2})
    add('Ywear', {'Y':1}, {'D':1})
    add('capture', {'C':1}, {'CF':1})
    add('Fleak', {'F':1}, {})
    add('recycleC', {'D':1,'F':1,'C':1}, {'R':1,'C':1})
    add('recycleY', {'D':1,'F':1,'Y':1}, {'R':1,'Y':1})
    add('CFleak', {'CF':1}, {'C':1})
    add('CFwear', {'CF':1}, {'D':1,'F':1})
    add('accessRepair', {'D':1,'CF':1}, {'R':1,'C':1})
    for i in (0,1):
        a,g,gf,yg = (f'{p}{i}' for p in ('A','G','GF','YG'))
        add(f'formA{i}', {'R':1,'F':1}, {a:1})
        add(f'copyA{i}', {'R':1,'F':1,a:1}, {a:2})
        add(f'fabricateG{i}', {a:1,'R':1,'F':1}, {a:1,g:1})
        add(f'A{i}wear', {a:1}, {'D':1})
        add(f'G{i}wear', {g:1}, {'D':1})
        add(f'bindF{i}', {g:1,'F':1}, {gf:1})
        add(f'unbindF{i}', {gf:1}, {g:1,'F':1})
        add(f'GF{i}leak', {gf:1}, {g:1})
        add(f'GF{i}wear', {gf:1}, {'D':1,'F':1})
        add(f'bindY{i}', {g:1,'Y':1}, {yg:1})
        add(f'unbindY{i}', {yg:1}, {g:1,'Y':1})
        add(f'YG{i}Gwear', {yg:1}, {'Y':1,'D':1})
        add(f'YG{i}Ywear', {yg:1}, {g:1,'D':1})
        add(f'accessForm{i}', {'R':1,'CF':1}, {a:1,'C':1})
        add(f'accessFabricate{i}', {a:1,'R':1,'CF':1}, {a:1,g:1,'C':1})
    add('boundReproduce1', {'R':1,'YG1':1}, {'Y':1,'YG1':1})
    assert len(rows) == 42
    return rows


CHANNELS = channels()


def dot(w, x):
    return sum(w[s] * x.get(s,0) for s in SPECIES)


def delta(w, lhs, rhs):
    return dot(w, rhs) - dot(w, lhs)


def run_path(initial, names):
    x = {s:initial.get(s,0) for s in SPECIES}
    steps = []
    for name in names:
        lhs,rhs = CHANNELS[name]
        assert all(x[s] >= n for s,n in lhs.items()), (name,x)
        rate = 1
        for s,n in lhs.items():
            for j in range(n): rate *= x[s]-j
        assert rate > 0
        before = x.copy()
        for s in SPECIES: x[s] += rhs.get(s,0)-lhs.get(s,0)
        assert min(x.values()) >= 0 and dot(N,x) == 4
        steps.append({'event':name,'selected_rate':rate,
                      'before':{s:n for s,n in before.items() if n},
                      'after':{s:n for s,n in x.items() if n},
                      'Q':dot(FREE_POOL,x),'U':dot(U,x),'W':dot(W,x),'S':dot(S,x)})
    return x,steps


def poisson_tail_upper(mean, threshold):
    # Geometric majorant for the positive tail / finite lower sum for exp(mean).
    assert Q(mean, threshold+1) < 1
    exp_lower = sum((Q(mean**k, factorial(k)) for k in range(120)), Q(0))
    numerator = Q(mean**threshold,factorial(threshold))/(1-Q(mean,threshold+1))
    return min(Q(1),numerator/exp_lower)


def main():
    ledger = {}
    for name,(lhs,rhs) in CHANNELS.items():
        dn,dw,dq,ds = (delta(w,lhs,rhs) for w in (N,W,FREE_POOL,S))
        assert dn == 0
        assert dq == 1 if name == 'CFwear' else dq <= 0
        assert ds == 1 if name == 'capture' else ds <= 0
        ledger[name] = {'material':dn,'work':dw,'mobile_packet_pool':dq,'S':ds}
    assert delta(FREE_POOL,*CHANNELS['Fleak']) == -1
    assert all(delta(FREE_POOL,*CHANNELS[f'GF{i}leak']) == -1 for i in (0,1))

    initial = {'R':3,'Y':1,'F':2}
    approach = ['assemble','assemble','capture','capture']
    x,approach_steps = run_path(initial,approach)
    assert x['CF']==2 and x['R']==1 and x['Y']==1 and x['F']==2
    pump = ['CFwear','accessRepair','assemble','capture','capture']
    y,pump_steps = run_path(x,pump)
    assert all(y[s]==x[s]+int(s=='F') for s in SPECIES)
    # All m>=1 are first-entry reachable: repeat the exact pump m-1 times.
    suffix = ['formA0','CFwear','accessRepair','fabricateG0','bindY0','capture']
    z,suffix_steps = run_path(y,suffix)
    assert {s:n for s,n in z.items() if n} == {'CF':1,'F':2,'A0':1,'YG0':1}
    # Repeat for a few finite values as checks of the symbolic pump composition.
    entries = {}
    for m in (1,2,5,20):
        end,path = run_path(initial,approach+pump*(m-1)+suffix)
        assert end['F']==m and end['A0']==end['CF']==end['YG0']==1
        assert all(not (st['after'].get('CF')==1 and
                       st['after'].get('A0',0)+st['after'].get('A1',0)==1 and
                       st['after'].get('YG0',0)+st['after'].get('YG1',0)==1)
                   for st in path[:-1])
        entries[str(m)] = {'jumps':len(path),'captures':sum(s['event']=='capture' for s in path)}

    # Before lineage loss, mobile-pool births <=3 and per-packet leakage =1.
    # Starting Q=2, upcrossing to Q>=M+1 before H10 is bounded by
    # 30 P(Pois(3)>=M-2), a deliberately conservative analytic bound.
    tails = {}
    for M in (20,25,27,30,35,40,90):
        bound = min(Q(1),30*poisson_tail_upper(3,M-2))
        tails[str(M)] = {'upper_exact':str(bound),'upper_decimal':float(bound)}
    assert Q(tails['30']['upper_exact']) < Q(1,10**15)
    assert Q(tails['40']['upper_exact']) < Q(1,10**25)

    result = {
        'status':'all exact assertions passed',
        'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'scope':'Exact channel increments, positive finite path witness, and rational analytic tail bounds; no successor CTMC calculation or probability comparison',
        'channel_count':len(CHANNELS),'ledger':ledger,
        'approach':approach_steps,'one_pump':pump_steps,'example_entry_suffix':suffix_steps,
        'first_entry_path_checks':entries,
        'analytic_mobile_pool_upcrossing_bounds_H10':tails,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'sources_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in [
            'experiments/shared-renewal-capability/full-entry/compute.py',
            '_process/research/2026-10-05-support-and-shared-generativity/completion/FULL-ENTRY-SUCCESSOR.md',
            'experiments/shared-renewal-capability/formal/TypedRenewal.lean',
            'experiments/shared-renewal-capability/formal/ReserveTurnover.lean']}}
    (HERE/'exact-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'H10_bounds':{m:v['upper_decimal'] for m,v in tails.items()}},indent=2))


if __name__=='__main__':main()
