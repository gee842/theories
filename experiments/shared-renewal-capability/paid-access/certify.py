#!/usr/bin/env python3
"""Directed integer/rational uniformization for the fixed H=10 comparison.

Reuses compute.py's enumerated generator; it does not independently reconstruct
the chemistry. No floating arithmetic enters any probability bound.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('paid_access_model',HERE/'compute.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
LAMBDA=21
H=10
ORDER=512
SCALE=2**128
GRID=10**30


def ceilq(q): return -(-q.numerator//q.denominator)


def bound(rows):
    assert max(total for total,_ in rows)<=LAMBDA
    lo=[0]*len(rows);hi=lo.copy()
    weight=Q(1);exp_lower=Q(1)
    sum_lo=Q(0);sum_hi=Q(0)
    mu=LAMBDA*H
    for n in range(1,ORDER+1):
        nlo=[];nhi=[]
        for s,(total,dest) in enumerate(rows):
            num_lo=(LAMBDA-total)*lo[s]
            num_hi=(LAMBDA-total)*hi[s]
            for d,rate in dest.items():
                num_lo+=rate*(SCALE if d==-1 else lo[d])
                num_hi+=rate*(SCALE if d==-1 else hi[d])
            nlo.append(num_lo//LAMBDA)
            nhi.append((num_hi+LAMBDA-1)//LAMBDA)
        lo,hi=nlo,nhi
        assert 0<=lo[0]<=hi[0]<=SCALE
        weight*=Q(mu,n)
        exp_lower+=weight
        sum_lo+=weight*lo[0]
        sum_hi+=weight*hi[0]
    # e^mu tail begins at ORDER+1. Every subsequent ratio is <=mu/(ORDER+2).
    tail=weight*Q(mu,ORDER+1)/(1-Q(mu,ORDER+2))
    exp_upper=exp_lower+tail
    lower=sum_lo/(SCALE*exp_upper)
    upper=sum_hi/(SCALE*exp_lower)+tail/exp_lower
    grid_lo=(lower*GRID).numerator//(lower*GRID).denominator
    grid_hi=ceilq(upper*GRID)
    assert Q(grid_lo,GRID)<=lower<=upper<=Q(grid_hi,GRID)
    assert tail/exp_lower<Q(1,10**65)
    return dict(lower_grid_integer=str(grid_lo),upper_grid_integer=str(grid_hi),
                denominator=str(GRID),lower_exact=str(Q(grid_lo,GRID)),
                upper_exact=str(Q(grid_hi,GRID)),
                poisson_tail_upper='1/10^65',transient_states=len(rows)),(grid_lo,grid_hi)


def main():
    arms={};intervals={};leading={}
    for zeta in (0,1):
        states,rows=model.graph(zeta)
        arms[str(zeta)],intervals[zeta]=bound(rows)
        order,coefficient,numerator=model.leading_coefficient(rows)
        leading[zeta]=(order,coefficient,numerator)
    gap_lo=intervals[0][0]-intervals[1][1]
    gap_hi=intervals[0][1]-intervals[1][0]
    assert gap_lo>0
    assert leading[0][0]==leading[1][0]==24
    early=leading[0][1]-leading[1][1]
    assert early<0
    result=dict(status='passed',method='Directed integer propagation and rational exponential-tail bounds; no floating arithmetic',
                uniformization_rate=LAMBDA,deadline=H,poisson_order=ORDER,
                integer_scale=str(SCALE),reported_denominator=str(GRID),arms=arms,
                difference_lower_exact=str(Q(gap_lo,GRID)),difference_upper_exact=str(Q(gap_hi,GRID)),
                earliest_success_order=24,earliest_difference_coefficient=str(early),
                earliest_rate_sum_difference=str(leading[0][2]-leading[1][2]),
                protocol_sha256=hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),
                model_sha256=hashlib.sha256((HERE/'compute.py').read_bytes()).hexdigest(),
                certificate_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
