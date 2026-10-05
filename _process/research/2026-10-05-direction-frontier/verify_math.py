"""Independent exact checks for the direction-frontier construction.

This is a deterministic resource-allocation model, not empirical data.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math


def costs(A, B, K, hazard, repair, upkeep, efficacy, returned, bypass):
    b = min(returned, bypass)
    S0 = A - hazard*b
    S1 = A - upkeep - hazard*repair - hazard*(1-efficacy)*b
    return b, S0, S1, S0/B, S1/(B+K)


def matrix(S0, S1, B, K, mu, alpha):
    C = B+K
    return (((1-mu*alpha)*S0/B, mu*(1-alpha)*S1/B),
            (mu*alpha*S0/C, (1-mu*(1-alpha))*S1/C))


def stationary_ratio(M):
    a,b=map(float,M[0]); c,d=map(float,M[1])
    gap=a-d
    disc=math.sqrt(gap*gap+4*b*c)
    # Numerically stable positive quadratic root.
    return 2*c/(gap+disc) if gap>=0 else (-gap+disc)/(2*b)


def main():
    checks=0
    for A,B,K,h,a,c,q,d,e in product(
        map(F,[5,10,20]),map(F,[2,5,10]),map(F,[0,1,3]),
        [F(1,4),F(1,2),F(1)],map(F,[0,1]),map(F,[0,1,2]),
        [F(0),F(1,2),F(1)],map(F,[1,4,10]),map(F,[1,4,10])):
        b,S0,S1,W0,W1=costs(A,B,K,h,a,c,q,d,e)
        if A<c+a+b or S0<=0 or S1<=0:
            continue
        gap=h*b*(B*q+K)-B*(c+h*a)-K*A
        assert (W1>W0)==(gap>0)
        assert (W1==W0)==(gap==0)
        assert W1-W0==gap/(B*(B+K))
        checks+=1

    static=0
    for c,d,e,v,H in product(map(F,[0,1,2,4]),map(F,[0,1,2,4]),
                            map(F,[0,1,2,4]),[F(0),F(1,2),F(1),F(2)],map(F,[1,2])):
        unique=c<d+v*H and c<e+v*H
        assert unique==(v*H>c-min(d,e))
        tied=c==min(d+v*H,e+v*H)
        assert tied==(v*H==c-min(d,e))
        static+=1

    illustrations=[]; conservation=0
    for bypass in [F(2),F(10)]:
        b,S0,S1,W0,W1=costs(F(20),F(10),F(1),F(1,2),F(1),F(1),F(1),F(12),bypass)
        assert costs(F(20),F(10),F(1),F(1,2),F(1),F(1),F(1),F(100),bypass)==(b,S0,S1,W0,W1)
        rows=[]
        for mu in [F(1,2),F(1,20),F(1,200),F(1,2000)]:
            M=matrix(S0,S1,F(10),F(1),mu,F(1,2))
            for n0,n1 in product(range(4),repeat=2):
                nxt0=M[0][0]*n0+M[0][1]*n1
                nxt1=M[1][0]*n0+M[1][1]*n1
                assert 10*nxt0+11*nxt1==S0*n0+S1*n1
                conservation+=1
            assert M[1][0]>0  # paid formation with no responsive parent
            determinant=M[0][0]*M[1][1]-M[0][1]*M[1][0]
            assert determinant==(1-mu)*W0*W1
            rstar=stationary_ratio(M)
            a0,b0=map(float,M[0]); c0,d0=map(float,M[1])
            assert abs((c0+d0*rstar)/(a0+b0*rstar)-rstar)<1e-9*max(1,rstar)
            for start in [0.0, rstar/2, rstar*2+1]:
                r=start
                for _ in range(10000):
                    nxt=(c0+d0*r)/(a0+b0*r)
                    assert min(r,rstar)-1e-10<=nxt<=max(r,rstar)+1e-10
                    if abs(nxt-r)<1e-13*max(1,rstar):
                        r=nxt;break
                    r=nxt
                assert abs(r-rstar)<1e-8*max(1,rstar)
            rows.append({'exploration_fraction':float(mu),'responsive_share':rstar/(1+rstar)})
        illustrations.append({'bypass_cost':float(bypass),'returned_loss':12,
                              'W0':str(W0),'W1':str(W1),'stationary_composition':rows})

    # Arithmetic gain can disagree with multiplicative cumulative gain.
    assert (F(1,2)+F(3))/2 > F(3,2)
    assert F(1,2)*F(3) < F(3,2)**2
    result={'status':'passed','resource_threshold_cases':checks,
            'static_protection_and_tie_cases':static,'exact_capital_conservation_cases':conservation,
            'formation_and_limit_cases':8,'threshold_example_b':str(F(70,11)),
            'illustrations':illustrations,
            'scope':'Exact rational finite checks and numerical stationary-ratio corroboration; general results are proved in math-note.md.'}
    Path(__file__).with_name('math-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
