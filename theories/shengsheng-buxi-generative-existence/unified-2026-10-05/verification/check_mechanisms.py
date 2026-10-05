"""Independent audit: imports none of the source models. Stdlib only."""
from fractions import Fraction as F
from itertools import product
from collections import deque
from math import sqrt, exp
from pathlib import Path
import json

OUT=Path(__file__).parent
results={}

# Conservation, threshold and global-convergence witnesses: direct RK4.
def rhs(z,a,b,k):
    r,c,d=z
    return (k*c*d-a*r,a*r-b*c,b*c-k*c*d)
def rk(z,a,b,k,dt):
    ks=[rhs(z,a,b,k)]
    for factor in (dt/2,dt/2,dt):
        ks.append(rhs(tuple(z[i]+factor*ks[-1][i] for i in range(3)),a,b,k))
    return tuple(z[i]+dt*(ks[0][i]+2*ks[1][i]+2*ks[2][i]+ks[3][i])/6 for i in range(3))
cases=[]
for a,b,k,m,z in [(1,1,1,3,(3,0,0)),(1,1,1,3,(0,.1,2.9)),(.3,.7,2,2,(.2,0,1.8)),(1,1,1,.5,(.5,0,0)),(1,1,1,1,(1,0,0)),(1,1,1,3,(0,0,3))]:
    final=[]
    for dt in (.02,.01):
        x=z
        for _ in range(round(200/dt)):
            prev=x
            x=rk(x,a,b,k,dt)
            assert min(x)>-1e-10
            assert abs(sum(x)-m)<1e-9
            assert abs(x[2]-b/k)<=abs(prev[2]-b/k)+1e-12
        final.append(x)
    assert max(abs(final[0][i]-final[1][i]) for i in range(3))<1e-8
    if sum(z[:2])==0: target=(0,0,m)
    elif k*m>b: target=(b/(a+b)*(m-b/k),a/(a+b)*(m-b/k),b/k)
    else: target=(0,0,m)
    if k*m!=b: assert max(abs(final[-1][i]-target[i]) for i in range(3))<1e-8
    else: assert final[-1][0]+final[-1][1]<.02
    cases.append(dict(parameters=[a,b,k,m],initial=z,t=200,final=final[-1],equilibrium=target,step_size_error=max(abs(final[0][i]-final[1][i]) for i in range(3))))
results['renewal_ode']=cases

# Independent exact determinant checks for both 4D control and reduced chemistry.
def det(mat):
    a=[list(map(F,row)) for row in mat]; ans=F(1)
    for j in range(len(a)):
        idx=next((i for i in range(j,len(a)) if a[i][j]),None)
        if idx is None:return F(0)
        if idx!=j:a[idx],a[j]=a[j],a[idx];ans=-ans
        v=a[j][j];ans*=v
        for i in range(j+1,len(a)):
            q=a[i][j]/v
            for n in range(j,len(a)):a[i][n]-=q*a[j][n]
    return ans
matrix_cases=0
for a,b,k,gamma,h in product((F(1),F(2)),(F(1),F(3)),(F(1),F(2)),(F(2),F(4)),(F(0),F(1,2),F(1))):
    H=((1+h)/2,(1-h)/2)
    A=[[a,0,-b,0],[0,a,0,-b],[k*H[0],k*H[1],-gamma,0],[k*H[1],k*H[0],0,-gamma]]
    for lam in (F(-3),F(0),F(1,3),F(2)):
        actual=det([[lam*(i==j)-A[i][j] for j in range(4)] for i in range(4)])
        expected=(lam*lam+(gamma-a)*lam+b*k-a*gamma)*(lam*lam+(gamma-a)*lam+b*k*h-a*gamma)
        assert actual==expected
        matrix_cases+=1
results['control_exact_determinant_checks']=matrix_cases

# Finite-particle CTMC: all states reverse-reachable from absorbing state.
absorption=[]
for N in range(1,26):
    states=[(r,c,N-r-c) for r in range(N+1) for c in range(N-r+1)]
    predecessors={x:[] for x in states}
    for r,c,d in states:
        ns=[]
        if r:ns.append((r-1,c+1,d))
        if c:ns.append((r,c-1,d+1))
        if c and d:ns.append((r+1,c,d-1))
        for x in ns:predecessors[x].append((r,c,d))
    seen={(0,0,N)}; q=deque(seen)
    while q:
        for x in predecessors[q.popleft()]:
            if x not in seen:seen.add(x);q.append(x)
    assert len(seen)==len(states)
    absorption.append(dict(N=N,states=len(states),reach_absorption=len(seen)))
results['finite_particle_graphs']=absorption

# Institution reconstructed from its textual event order.
# phase 0=incumbent choice, -1=restoration, positive=remaining delayed rounds.
def transition(st,f=F(11,9),K=F(3),h=4,d=2,access=True,authority=True,M=6,cost=1):
    e,B,Q,phase,alive=st
    productive=e>=2
    paid=alive and Q>=1
    if paid: Q-=1
    else: Q=F(0)
    alive=paid
    if not alive or not authority:phase=0
    file=productive and alive and access and authority and phase==0 and 1<=B<=h and Q>=2 and B>=cost
    if file:Q-=2;B-=cost;phase=d
    rule='F' if phase==-1 else 'X'
    receipt=(3 if rule=='F' else 1) if productive else 0
    B=min(M,max(0,B+receipt-2))
    if phase>0:phase=phase-1 if phase>1 else -1
    elif phase==-1 and B==M:phase=0
    Q=min(K,Q+f) if alive and productive else Q
    return (e if productive else 0,B,Q,phase,alive),dict(rule=rule,file=bool(file))
def safe(st):return st[0]>=2 and st[1]>=1 and st[4]
def orbit(st,**kw):
    history=[];seen={};details=[]
    while st not in seen:
        seen[st]=len(history);history.append(st)
        st,row=transition(st,**kw);details.append(row)
    return history,details,seen[st]
base=(3,6,F(23,9),0,True)
history,details,start=orbit(base)
assert len(history)==9 and start==0 and min(s[1] for s in history)==1
assert [s[1] for s in history]==[6,5,4,2,1,2,3,4,5]
assert sum(r['file'] for r in details)==1
results['correction_cycle']=[dict(B=s[1],Q=str(s[2]),phase=s[3],**row) for s,row in zip(history,details)]
states=[]
for e,B in product(range(4),range(7)):
    states.append((e,B,F(0),0,False))
    states.extend((e,B,F(q,9),phase,True) for q,phase in product(range(28),(0,-1,1)))
state_set=set(states);cycles=set();safecycles=set();protected=0;viable=0
for st in states:
    hh,_,s=orbit(st)
    assert all(transition(x)[0] in state_set for x in hh)
    cyc=frozenset(hh[s:]);cycles.add(cyc)
    if all(map(safe,cyc)):safecycles.add(cyc)
    if safe(st):
        protected+=1
        if all(map(safe,hh)):viable+=1
counts=dict(states=len(states),pointwise_protected=protected,indefinitely_protected=viable,attractors=len(cycles),protected_attractors=len(safecycles))
assert counts==dict(states=2380,pointwise_protected=1008,indefinitely_protected=272,attractors=7,protected_attractors=2)
results['correction_graph']=counts
thresholds=[]
for q in range(28):
    hh,_,_=orbit((3,6,F(q,9),0,True))
    assert all(map(safe,hh))==(q>=23)
    thresholds.append(dict(Q_ninths=q,protected=all(map(safe,hh))))
results['initial_funding_threshold']=thresholds
failures=[]
for name,kw,Q in [('no_access',dict(access=False),F(3)),('upkeep_only',dict(f=F(1)),F(3)),('delay3',dict(d=3),F(3)),('below_threshold_large_reserve',dict(f=F(109,90),K=F(5)),F(5))]:
    hh,_,_=orbit((3,6,Q,0,True),**kw)
    failure=next((i for i,s in enumerate(hh) if not safe(s)),None)
    failures.append(dict(case=name,first_failure_round=failure))
assert [f['first_failure_round'] for f in failures]==[6,15,5,194]
results['correction_failures']=failures

# General safe timing/cycle claims are tested over a separate parameter family.
family=0
for M,h,d,c in product(range(4,10),range(1,10),range(1,5),range(1,3)):
    if h>M or h-c-d<1:continue
    length=2*(M-h)+c+2*d
    f=1+F(2,length)
    hh,_,s=orbit((3,M,F(3),0,True),f=f,h=h,d=d,M=M,cost=c)
    assert all(map(safe,hh))
    assert len(hh)-s==length
    family+=1
results['safe_general_parameter_cases']=family

# Exact renewal-weight witness for a high-gain but acyclic network.
# capacities 1<-2<-3, production 2->1=10 and 3->2=10, all losses one.
# (I-B)^-1=I+B+B^2, so column-sum weights are (1,11,111).
B=[[0,10,0],[0,0,10],[0,0,0]]
w=[1,11,111]
assert [sum(w[i]*(B[i][j]-(i==j)) for i in range(3)) for j in range(3)]==[-1,-1,-1]
results['acyclic_renewal_weight']={'B':B,'losses':[1,1,1],'weights':w,'weighted_drift_coefficients':[-1,-1,-1]}
results['status']='all_checks_passed'
(OUT/'independent-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'status':results['status'],'control_determinants':matrix_cases,'chemical_cases':len(cases),'finite_particle_graphs':len(absorption),'correction_graph':counts,'general_safe_cases':family,'failures':failures},indent=2))
