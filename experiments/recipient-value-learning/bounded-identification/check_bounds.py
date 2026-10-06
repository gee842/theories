#!/usr/bin/env python3
"""Independent constructed-population checks; never reads empirical outcomes.

The declared grid is in BOUNDED-IDENTIFICATION-REVIEW.md. No producer module is
imported. Exact probability calculations use Fraction; logistic checks use only
the Python standard library and do not claim to prove real-variable calculus.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parent
QUARTERS = tuple(F(i, 4) for i in range(5))
HALVES = (F(0), F(1, 2), F(1))
D_GRID = (0.0, 0.1, 0.5, 1.0, 2.0, 4.0)
RHO_GRID = (0.0, 0.05, 0.25, 0.5, 0.9, 1.0)


def frontier(r0, r1, m, epsilon):
    common = max(F(0), r0 + r1 - 1 - epsilon)
    return -r0 + (1 - m) * common, r1 - (1 - m) * common


def atom(good, r0, r1, p0, p1):
    return (bool(good), F(r0), F(r1), F(p0), F(p1))


def summarize(population):
    assert sum(w for w, _ in population) == 1
    assert all(w >= 0 for w, _ in population)
    r0 = r1 = l0 = l1 = bad = overlap = F(0)
    m = F(0)
    for w, (good, a, b, x, y) in population:
        assert all(0 <= z <= 1 for z in (a, b, x, y))
        r0 += w * a
        r1 += w * b
        l0 += w * a * x
        l1 += w * b * y
        if good:
            overlap += w * min(a, b)
            if w:
                m = max(m, abs(y - x))
        else:
            bad += w
    return dict(R0=r0, R1=r1, L0=l0, L1=l1, delta=l1-l0,
                epsilon=bad, m=m, good_overlap=overlap)


def upper_witness(r0, r1, m, epsilon):
    both = max(F(0), r0 + r1 - 1)
    bad = min(epsilon, both)
    return [
        (bad, atom(False, 1, 1, 0, 1)),
        (both-bad, atom(True, 1, 1, (1-m)/2, (1+m)/2)),
        (r1-both, atom(True, 0, 1, 1, 1)),
        (r0-both, atom(True, 1, 0, 0, 0)),
        (1-r0-r1+both, atom(True, 0, 0, 0, 0)),
    ]


def reverse_probabilities(population):
    return [(w, atom(g, a, b, 1-x, 1-y)) for w, (g,a,b,x,y) in population]


def sigma(z):
    if z >= 0:
        return 1 / (1 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1 + ez)


def pointwise_envelope(d, rho):
    a, c = math.exp(d), 1-rho
    if a*c <= 1:
        return rho
    return (math.sqrt(a)-math.sqrt(c))**2 / (a-1)


def exact_checks():
    witnesses = 0
    for r0,r1,m,eps in product(QUARTERS, repeat=4):
        lo,hi = frontier(r0,r1,m,eps)
        pop = upper_witness(r0,r1,m,eps)
        for model, expected in ((pop,hi), (reverse_probabilities(pop),lo)):
            stats = summarize(model)
            assert stats['R0']==r0 and stats['R1']==r1
            assert stats['m']<=m and stats['epsilon']<=eps
            assert stats['delta']==expected
            witnesses += 1
        assert frontier(r1,r0,m,eps)==(-hi,-lo)
        if r0+r1 <= 1+eps:
            assert (lo,hi)==(-r0,r1)
        if r0==r1==1:
            assert hi==eps+(1-eps)*m and lo==-hi

    atoms = [atom(g,*values) for values in product(HALVES, repeat=4)
             for g in (False,True)]
    mixtures = mean_absolute_checks = 0
    for left,right,weight in product(atoms,atoms,QUARTERS):
        s = summarize([(weight,left),(1-weight,right)])
        lo,hi = frontier(s['R0'],s['R1'],s['m'],s['epsilon'])
        assert lo <= s['delta'] <= hi, (left,right,weight,s,lo,hi)
        assert s['good_overlap'] >= max(0,s['R0']+s['R1']-1-s['epsilon'])
        if s['epsilon']==0:
            rho=weight*abs(left[2]-left[1])+(1-weight)*abs(right[2]-right[1])
            assert abs(s['delta'])<=rho+(1-rho)*s['m']
            mean_absolute_checks+=1
        mixtures += 1

    rectangles = interior_comparisons = 0
    intervals=[(a,b) for a,b in product(QUARTERS,repeat=2) if a<=b]
    for (a,b),(c,d),m,eps in product(intervals,intervals,QUARTERS,QUARTERS):
        # R0 in [a,b], R1 in [c,d]. Use the conservative extrema, not plug-ins.
        lower=frontier(b,c,m,eps)[0]
        upper=frontier(a,d,m,eps)[1]
        for r0,r1 in product(QUARTERS,repeat=2):
            if a<=r0<=b and c<=r1<=d:
                lo,hi=frontier(r0,r1,m,eps)
                assert lower<=lo and hi<=upper
                interior_comparisons += 1
        rectangles += 1
    monotonicity = 0
    for r0,r1,m,eps in product(QUARTERS,repeat=4):
        lo,hi=frontier(r0,r1,m,eps)
        for mm,ee in product(QUARTERS,repeat=2):
            if mm>=m and ee>=eps:
                ll,hh=frontier(r0,r1,mm,ee)
                assert ll<=lo and hi<=hh
                monotonicity += 1
    assert frontier(F(99,100),F(99,100),F(1,10),F(1,100))[1]==F(117,1000)
    return dict(signed_sharp_witnesses=witnesses, two_atom_mixtures=mixtures,
                mean_absolute_gate_envelopes=mean_absolute_checks,
                canonical_example_ceiling=F(117,1000),
                confidence_rectangles=rectangles, rectangle_interior_comparisons=interior_comparisons,
                budget_monotonicity_comparisons=monotonicity)


def logistic_checks():
    dense_points=0; max_gap=0.0; rows=[]
    logits=tuple(-40+i/100 for i in range(8001))
    for d,rho in product(D_GRID,RHO_GRID):
        declared=pointwise_envelope(d,rho)
        observed=max(sigma(z+d)-(1-rho)*sigma(z) for z in logits)
        dense_points += len(logits)
        assert observed<=declared+2e-14
        gap=declared-observed
        assert gap<1e-5,(d,rho,gap)
        max_gap=max(max_gap,gap)
        a,c=math.exp(d),1-rho
        if a*c>1:
            t=(math.sqrt(a)-math.sqrt(c))/(a*math.sqrt(c)-math.sqrt(a))
            exact_point=sigma(math.log(t)+d)-c*sigma(math.log(t))
            assert abs(exact_point-declared)<2e-14
        if rho==0:assert abs(declared-math.tanh(d/4))<2e-14
        rows.append(dict(D=d,rho=rho,envelope=declared,dense_supremum=observed))

    approximations=0; approximation_max_gap=0.0
    for r0,r1,m,eps in product(QUARTERS,QUARTERS,QUARTERS[:-1],QUARTERS):
        d=4*math.atanh(float(m)); t=30.0
        both=max(F(0),r0+r1-1);bad=min(eps,both)
        achieved=(float(bad)*(sigma(t)-sigma(-t))
                  +float(both-bad)*(sigma(d/2)-sigma(-d/2))
                  +float(r1-both)*sigma(t)-float(r0-both)*sigma(-t))
        expected=float(frontier(r0,r1,m,eps)[1])
        gap=expected-achieved
        assert -1e-14<=gap<3e-13,(r0,r1,m,eps,gap)
        approximations+=1;approximation_max_gap=max(approximation_max_gap,gap)
    return dict(dense_logit_evaluations=dense_points,pointwise_rows=rows,
                largest_dense_gap=max_gap,finite_logit_sharpness_approximations=approximations,
                largest_finite_logit_gap=approximation_max_gap)


def fault_cases():
    equal_gates=summarize([
        (F(1,2),atom(True,0,1,F(3,4),F(3,4))),
        (F(1,2),atom(True,1,0,F(1,4),F(1,4)))])
    assert equal_gates['R0']==equal_gates['R1']==F(1,2)
    assert equal_gates['m']==0 and equal_gates['delta']==F(1,4)
    assert equal_gates['delta']>0 # A false rho=|R1-R0| would claim zero.

    # e1/log(3) equals 1 with mass 3/4 and -3 with mass 1/4; e0=0.
    # Their means agree exactly, while sigma(log3)=3/4 and sigma(-3log3)=1/28.
    assert F(3,4)*1+F(1,4)*(-3)==0
    choice=F(3,4)*F(3,4)+F(1,4)*F(1,28)
    assert choice-F(1,2)==F(1,14)

    union=summarize([
        (F(1,4),atom(False,1,1,F(1,10),F(9,10))),
        (F(1,4),atom(False,1,1,F(1,10),F(9,10))),
        (F(1,2),atom(True,1,1,F(1,2),F(1,2)))])
    # The first arm's calibration fails on the first atom, the second on the second.
    assert union['epsilon']==F(1,2) and union['delta']==F(2,5)
    false_bound=frontier(1,1,0,F(1,4))[1]
    correct_bound=frontier(1,1,0,F(1,2))[1]
    assert false_bound<union['delta']<=correct_bound

    population=summarize([
        (F(1,2),atom(True,1,1,F(3,4),F(3,4))),
        (F(1,2),atom(True,1,1,F(1,4),F(1,4)))])
    assert population['delta']==0 and frontier(1,1,0,0)==(0,0)
    selected_delta=F(3,4)-F(1,4)
    assert selected_delta==F(1,2)>0
    return dict(equal_response_means=equal_gates,
                equal_expectancy_means=dict(mean_scaled_expectancy_both=F(0),choice0=F(1,2),
                                            choice1=choice,delta=F(1,14)),
                disjoint_armwise_failures=dict(population=union,armwise_error=F(1,4),
                                              incorrect_paired_bound=false_bound,correct_bound=correct_bound),
                selected_population=dict(full_population=population,selected_delta=selected_delta,
                                         invalid_selected_frontier=F(0)))


def convert(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:convert(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [convert(v) for v in value]
    return value


def main():
    started=time.monotonic()
    report={'status':'running','started_at_utc':datetime.now(timezone.utc).isoformat(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'inputs':'Only declared synthetic grids; no empirical input files or producer imports.',
            'grid':dict(exact_probabilities=QUARTERS,atom_coordinates=HALVES,D=D_GRID,rho=RHO_GRID),
            'scope':'Independent exact finite checks and floating diagnostics; analytical and Lean scopes remain separate.'}
    out=ROOT/'checks.json'
    try:
        report['exact']=exact_checks()
        report['logistic']=logistic_checks()
        report['fault_cases']=fault_cases()
        report['status']='passed'
    except Exception as error:
        report['status']='failed';report['error']=repr(error)
        raise
    finally:
        report['elapsed_seconds']=time.monotonic()-started
        report['finished_at_utc']=datetime.now(timezone.utc).isoformat()
        if out.exists():
            prior=json.loads(out.read_text())
            report['preserved_previous_attempts']=prior.pop('preserved_previous_attempts',[])+[prior]
        out.write_text(json.dumps(convert(report),indent=2)+'\n')
        print(json.dumps(convert({'status':report['status'],'elapsed_seconds':report['elapsed_seconds'],
                                  'exact':report.get('exact'),'output':str(out)}),indent=2))


if __name__=='__main__':main()
