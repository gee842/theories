#!/usr/bin/env python3
"""Independent audit: cyclic linear systems and phase-specific productive reserves.
Does not import either author verification file or solve phases by its closed form.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import random


def solve(a,b):
    n=len(b)
    a=[list(row)+[rhs] for row,rhs in zip(a,b)]
    for c in range(n):
        p=next(i for i in range(c,n) if a[i][c])
        a[c],a[p]=a[p],a[c]
        q=a[c][c]
        a[c]=[v/q for v in a[c]]
        for i in range(n):
            if i != c:
                q=a[i][c]
                a[i]=[u-q*v for u,v in zip(a[i],a[c])]
    return [row[-1] for row in a]


def phase_solution(r,A,t,m):
    # Unknowns are values at every decision phase, including post-succession.
    eq=[[F(0) for _ in range(m)] for __ in range(m)]
    rhs=[F(0) for _ in range(m)]
    eq[0][0]+=1
    eq[0][m-1]-=t*r
    rhs[0]=t*A
    for p in range(1,m):
        eq[p][p]=1
        eq[p][p-1]=-r
        rhs[p]=A
    return solve(eq,rhs)


rng=random.Random(20261005)
phase_cases=0
threshold_cases=0
for _ in range(180):
    m=rng.choice([1,2,3,5])
    pars=[]
    phases=[]
    for c in range(3):
        r=rng.choice([F(0),F(1,5),F(3,5),F(9,10)])
        t=rng.choice([F(1,4),F(3,4),F(1)])
        target=rng.choice([F(0),F(1,2),F(1)])
        if c==0:
            target+=F(1,2)
        A=(1-r)*target
        pars.append((r,A,t))
        phases.append(phase_solution(r,A,t,m))
    b,H=F(rng.choice([0,1,3])),F(rng.choice([1,5,10]))
    scores=[phases[2][p]*(b+H*phases[0][p]*phases[1][p]) for p in range(m)]
    assert min(scores)==scores[0]
    for p in range(m):
        for coord in phases:
            assert coord[p]>=coord[0]
    x=[F(0)]*3
    observed=[]
    for n in range(70):
        row=[]
        for p in range(m):
            score=x[2]*(b+H*x[0]*x[1])
            row.append(score)
            assert all(x[i]<=phases[i][p] for i in range(3))
            x=[r*xi+A for xi,(r,A,t) in zip(x,pars)]
        assert min(row)==row[0]
        observed.append(row)
        x=[t*xi for xi,(_,_,t) in zip(x,pars)]
    for threshold in [scores[0]/2,scores[0],scores[0]*F(3,2),F(1)]:
        if threshold<=0:
            continue
        criterion=scores[0]>threshold
        if criterion:
            # Numerical budget has a uniform contraction <=.9; chosen margins
            # for threshold 1 could be very small, so check only detected cases
            # plus the deliberately half-limit threshold for finite crossing.
            if threshold==scores[0]/2:
                assert all(s>threshold for s in observed[-1])
            if all(s>threshold for s in observed[-1]):
                first=next(n for n,row in enumerate(observed) if min(row)>threshold)
                assert all(min(row)>threshold for row in observed[first:])
        else:
            assert all(row[0]<=threshold for row in observed)
        threshold_cases+=1
    phase_cases+=1

# Equality productive regime, arbitrary within-generation receipt placement.
# Capital gap X*-X0 decays, while total generation income tends to total costs.
# Derive exact infinite reserve by taking the supremum of each phase obligation.
productive_cases=0
underfunded_witnesses=0
for ell,p,slope,base,xfrac,m in product(
    [F(1,4),F(1,2),F(1)], [F(1),F(2)], [F(1),F(2)],
    [F(0),F(1)], [F(0),F(1,2),F(1)], [2,3]):
    Xstar=p/ell
    X0=xfrac*Xstar
    Ystar=base+slope*Xstar
    beta=slope*(Xstar-X0)
    r=1-ell
    costs=[Ystar/F(m)]*m
    for weights in [[F(1)]+[F(0)]*(m-1),[F(0)]*(m-1)+[F(1)],[F(1,m)]*m]:
        f=F(0); prev_cost=F(0); phase_constants=[]
        for c,weight in zip(costs,weights):
            phase_constants.append(prev_cost+c-f*Ystar)
            prev_cost+=c
            f+=weight
        Dcycle=max([F(0)]+phase_constants)
        D=Dcycle+beta/ell
        reserve=D
        reserve_low=D-F(1,100)
        low_failed=False
        X=X0
        cumulative=F(0)
        for n in range(110):
            income=base+slope*X
            f=F(0); prev_cost=F(0)
            for j,(c,weight) in enumerate(zip(costs,weights)):
                # Evaluate required initial reserve from raw history, then
                # verify an independently derived nonnegative residual.
                need=c-cumulative
                residual=D-need
                expected=Dcycle-phase_constants[j]+beta*(1/ell-f)*(r**n)
                assert residual==expected and residual>=0
                assert reserve>=c
                reserve=reserve-c+weight*income
                if not low_failed:
                    if reserve_low<c:
                        low_failed=True
                    else:
                        reserve_low=reserve_low-c+weight*income
                cumulative+=weight*income-c
                f+=weight
                prev_cost+=c
            X=(1-ell)*X+p
        assert low_failed
        underfunded_witnesses+=1
        productive_cases+=1

result={
    "status":"passed",
    "independent_periodic_linear_systems":phase_cases,
    "durable_threshold_and_tie_cases":threshold_cases,
    "phase_specific_productive_equality_reserves":productive_cases,
    "slightly_underfunded_finite_failure_witnesses":underfunded_witnesses,
    "method":"Exact rational Gaussian elimination of all phase equations; raw decision-before-update traces; infinite-prefix reserve residual identities with varying receipt timing.",
    "scope":"Constructed independent checks, not empirical evidence or substitutes for proofs."
}
Path(__file__).with_name("independent-review-checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
