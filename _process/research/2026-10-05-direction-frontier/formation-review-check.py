"""Independent reviewer reconstruction; no imports from the author's model."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, math

def build(A,B,K,lam,q,oper,repair,d,e,mu,alpha):
    b=min(d,e); C=B+K
    s=[A-lam*b,A-oper-lam*repair-lam*(1-q)*b]
    # Assemble columns directly from per-parent resource allocation events.
    columns=[]
    for parent in (0,1):
        allocations=[mu*(1-alpha)*s[parent],mu*alpha*s[parent]]
        allocations[parent]+=(1-mu)*s[parent]
        columns.append([allocations[0]/B,allocations[1]/C])
    M=[[columns[j][i] for j in range(2)] for i in range(2)]
    return s,M

checks=0; equality=0; limits=0
for B,K,lam,q,oper,repair,d,e,mu,alpha in product([F(1),F(3)],[F(0),F(2)],
        [F(0),F(1,3),F(1)],[F(0),F(1,3),F(1)],
        [F(0),F(1)],[F(0),F(1)],[F(1),F(4)],[F(1),F(5)],
        [F(1,7),F(1,2),F(1)],[F(1,5),F(1,2),F(4,5)]):
    A=F(10); C=B+K; s,M=build(A,B,K,lam,q,oper,repair,d,e,mu,alpha)
    if min(s)<=0:continue
    w0=s[0]/B;w1=s[1]/C
    numerator=lam*min(d,e)*(B*q+K)-B*(oper+lam*repair)-K*A
    assert w1-w0==numerator/(B*C)
    assert M[0][0]*M[1][1]-M[0][1]*M[1][0]==(1-mu)*w0*w1
    assert all(x>0 for row in M for x in row)
    for n in [(F(1),F(0)),(F(0),F(1)),(F(2,3),F(4,5))]:
        nxt=[sum(M[i][j]*n[j] for j in range(2)) for i in range(2)]
        construction=B*nxt[0]+C*nxt[1]
        operating=oper*n[1]+lam*repair*n[1]+lam*min(d,e)*(n[0]+(1-q)*n[1])
        assert construction+operating==A*sum(n)
    if w0==w1:
        r=alpha*B/((1-alpha)*C)
        assert M[0][1]*r*r+(M[0][0]-M[1][1])*r-M[1][0]==0
        equality+=1
    checks+=1

# Independent positive Perron vector from normalization iteration; ratio root
# obtained from eigenvalue, rather than author's quadratic-root formula.
num=[]
for S0,S1,B,K in [(F(19),F(37,2),F(10),F(1)),(F(15),F(37,2),F(10),F(1)),
                    (F(1,5),F(1,4),F(2),F(1)),(F(2),F(3),F(2),F(1))]:
    C=B+K;w0=S0/B;w1=S1/C
    for alpha in [F(1,5),F(1,2),F(4,5)]:
        shares=[]
        for mu in [F(1,100),F(1,10000),F(1,1000000)]:
            m00=float((1-mu*alpha)*w0);m01=float(mu*(1-alpha)*S1/B)
            m10=float(mu*alpha*S0/C);m11=float((1-mu*(1-alpha))*w1)
            rho=((m00+m11)+math.hypot(m00-m11,2*math.sqrt(m01*m10)))/2
            # Use eigenvector component less vulnerable to cancellation.
            r=m10/(rho-m11) if w0>=w1 else (rho-m00)/m01
            x=r/(1+r)
            assert abs((m10+m11*r)/(m00+m01*r)-r)<1e-9*max(1,r)
            shares.append(x);limits+=1
        if w1>w0:assert shares[0]<shares[1]<shares[2] and shares[-1]>.9999
        if w1<w0:assert shares[0]>shares[1]>shares[2] and shares[-1]<.0001
        if w1==w0:
            baseline=float(alpha*B/((1-alpha)*C+alpha*B))
            assert max(abs(x-baseline) for x in shares)<1e-9
        num.append({'W0':str(w0),'W1':str(w1),'alpha':str(alpha),'shares_at_mu_1e-2_1e-4_1e-6':shares})

out={'status':'passed','rational_reconstructions':checks,'equal_fitness_ratios':equality,
     'numerical_eigenvector_and_small_mutation_checks':limits,'examples':num,
     'resource_account':'External A times parent mass equals all stated operating/fallback costs plus all paid successor capital.'}
Path(__file__).with_name('formation-review-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='examples'},indent=2))
