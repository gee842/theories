#!/usr/bin/env python3
"""Exact scheduling countermodel; standard library only.

n modules each require D -> A -> E, one paid unit per stage, 3n reserve.
At most k diagnostics per tick; authorization and execution have independent
unlimited per-module capacity. Stages in the same tick use the pre-tick state.
Every newly diagnosed hidden fault has a reliably readable type; downstream
execution is chosen accordingly. The script checks scheduling, not discovery.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json


def enumerate_schedules(n, k):
    # Counts: undiagnosed, awaiting authorization, awaiting execution.
    start = (n, 0, 0)
    dist = {start: 0}
    pending = deque([start])
    edges = 0
    while pending:
        q = pending.popleft()
        u, a, e = q
        # Remaining reserve exactly equals remaining stage payments.
        reserve = 3*u + 2*a + e
        for nd, na, ne in product(range(min(k,u)+1), range(a+1), range(e+1)):
            if nd+na+ne == 0:
                continue  # Idle cannot improve a shortest schedule.
            nq = (u-nd, a+nd-na, e+na-ne)
            payment = nd+na+ne
            assert payment <= reserve
            assert 3*nq[0]+2*nq[1]+nq[2] == reserve-payment
            edges += 1
            if nq not in dist:
                dist[nq] = dist[q]+1
                pending.append(nq)
    return dist[(0,0,0)], len(dist), edges


def constructive_pipeline(n,k):
    q=(n,0,0)
    trace=[]
    while q != (0,0,0):
        u,a,e=q
        nd,na,ne=min(k,u),a,e
        nq=(u-nd,a+nd-na,e+na-ne)
        trace.append({'before':q,'diagnose':nd,'authorize':na,'execute':ne,'after':nq})
        q=nq
    return trace


def main():
    cases=[]
    deadline_cases=0
    for n in range(1,9):
        for k in range(1,n+1):
            minimum,states,edges=enumerate_schedules(n,k)
            formula=(n+k-1)//k+2
            witness=constructive_pipeline(n,k)
            assert minimum==formula==len(witness)
            for deadline in range(13):
                assert (minimum <= deadline) == (deadline >= 3 and n <= k*(deadline-2))
                deadline_cases+=1
            cases.append({'modules':n,'diagnostic_parallelism':k,'reserve':3*n,
                          'minimum_ticks':minimum,'enumerated_states':states,'enumerated_edges':edges})
    out={'status':'all assertions passed','model':'supplied unit-stage parallel scheduling model',
         'frontier_cases':len(cases),'deadline_cases':deadline_cases,'cases':cases,
         'two_module_shared_diagnostic_witness':constructive_pipeline(2,1),
         'two_module_dedicated_diagnostic_witness':constructive_pipeline(2,2),
         'limits':['No empirical cross-scale calibration','Supplied perfect diagnostic and fixed three-stage protocol',
                   'Only diagnostics share a throughput bottleneck; other stages run in parallel',
                   'Analytic necessity uses independent hidden modes and sure successful repair, not guessed success',
                   'All 3n costs are prepaid from declared reserve; no productive inflow modeled during repair']}
    p=Path(__file__).with_name('scale-deadline-results.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'frontier_cases':len(cases),'deadline_cases':deadline_cases,
                      'two_modules_shared':4,'two_modules_dedicated':3},indent=2))

if __name__=='__main__': main()
