"""Independent v4.5 game/mechanism checks. No author scripts used.
Source THEORY-clean.md, SHA256 cf7e96d3a98c8b7878bfabf9fbea88e627923f0ccd2ab6acafe5905148977be3.
Run: python v4_5_review_checks.py
Dependencies: numpy, scipy. These are reviewer checks, not author scripts.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from math import comb, prod, sqrt, exp, log


def roots_on(f,lo,hi,count=1500):
    grid=np.linspace(lo,hi,count)
    roots=[]
    for a,b in zip(grid[:-1],grid[1:]):
        if f(a)==0: roots.append(a)
        elif f(a)*f(b)<0: roots.append(brentq(f,a,b,xtol=1e-14))
    if f(hi)==0: roots.append(hi)
    return sorted(set(round(x,13) for x in roots))


def continuous_eq(n,s,Le,Lc,psi0,delta):
    # Fixed rivals => success concave in own action and common hazard affine.
    # Every interior stationary point found here is a global best-response fixed point.
    a=1-psi0
    def foc(i):
        return Le*s*(n-1)/(n*n*(1+s*i))-Lc*delta*(a-delta*i)**(n-1)
    candidates=roots_on(foc,0,1)
    if foc(0)<=0: candidates.append(0.)
    if foc(1)>=0: candidates.append(1.)
    rows=[]
    for i in sorted(set(candidates)):
        def payoff(x):
            w=(1+s*x)/(1+s*x+(n-1)*(1+s*i))
            return -Le*(1-w)-Lc*(1-(a-delta*x)*(a-delta*i)**(n-1))
        opt=minimize_scalar(lambda x:-payoff(x),bounds=(0,1),method='bounded',options={'xatol':1e-13})
        best=max(payoff(0),payoff(1),-opt.fun)
        assert best-payoff(i)<1e-9
        y=delta*i
        rows.append(dict(i=i,added_sum=n*y,total_risk=1-(a-y)**n,BR_gap=best-payoff(i),FOC=foc(i)))
    return rows


def contest_br(B,V=2,C=1.3,r=1.3):
    assert B>0
    # No y>V/C beats zero; enumerate stationary points plus both boundaries.
    def payoff(y):return V*y**r/(y**r+B)-C*y
    def df(y):return V*r*y**(r-1)*B/(y**r+B)**2-C
    grid=np.r_[1e-15,np.geomspace(1e-14,V/C,2000)]
    candidates=[0.,V/C]
    for a,b in zip(grid[:-1],grid[1:]):
        if df(a)*df(b)<0:candidates.append(brentq(df,a,b,xtol=1e-14))
    y=max(candidates,key=payoff)
    return y,payoff(y)


def frontier(regime,n=4,Om=1,Omc=1,Lb=1,c=1,ell=.3,ec=.05,r=1.3):
    V,C=Om+Lb,c+ell
    states=[]
    for k in range(n+1):
        m=n-k; pool=m*ec**r if regime=='SEP' else (m*ec)**r
        if k==0:x=0.
        elif m==0:x=V*r*(k-1)/(C*k*k)
        else:
            def foc(x):return V*r*x**(r-1)*((k-1)*x**r+pool)/(k*x**r+pool)**2-C
            grid=np.geomspace(1e-14,V/C,2000)
            candidates=[brentq(foc,a,b) for a,b in zip(grid[:-1],grid[1:]) if foc(a)*foc(b)<0]
            if contest_br(pool,V,C,r)[1]<=1e-10:candidates.append(0.)
            good=[]
            for x0 in candidates:
                B=(k-1)*x0**r+pool
                own=V*x0**r/(x0**r+B)-C*x0
                if contest_br(B,V,C,r)[1]-own<1e-8:good.append(x0)
            if len(good)!=1:raise RuntimeError(('No unique symmetric pure continuation',regime,n,k,good))
            x=good[0]
        E=k*x+m*ec; den=k*x**r+pool
        rp=(V*x**r/den-Lb-c*x-ell*E) if k else None
        if m:
            cp=(V*ec**r/den-Lb-c*ec-ell*E) if regime=='SEP' else pool/den*Omc/m-(1-pool/den)*Lb-c*ec-ell*E
        else:cp=None
        gap=None
        if k:
            own=V*x**r/den-C*x
            gap=contest_br((k-1)*x**r+pool,V,C,r)[1]-own
            assert gap<1e-8,('not a global BR',k,gap)
        states.append(dict(k=k,x=x,Coop=cp,Race=rp,BRgap=gap))
    d=[states[k]['Coop']-states[k+1]['Race'] for k in range(n)]
    def mix(p):return sum(comb(n-1,k)*(1-p)**k*p**(n-1-k)*d[k] for k in range(n))
    thresholds=roots_on(mix,0,1)
    pure=[j for j in range(n+1) if (j==0 or d[j-1]<=0) and (j==n or d[j]>=0)]
    return states,d,thresholds,pure


def simultaneous_deviation(states,n=4,Om=1,Omc=1,Lb=1,c=1,ell=.3,ec=.05,r=1.3):
    # Paper's .82 calculation: start from each cooperator state's incumbent effort,
    # remove own contribution to pool, hold incumbent efforts fixed, optimize entrant.
    d=[]
    for k in range(n):
        x=states[k]['x']; m=n-k
        B=k*x**r+((m-1)*ec)**r
        y,v=contest_br(B,Om+Lb,c+ell,r)
        entrant=v-Lb-ell*(k*x+(m-1)*ec)
        d.append(states[k]['Coop']-entrant)
    def mix(p):return sum(comb(n-1,k)*(1-p)**k*p**(n-1-k)*d[k] for k in range(n))
    return d,roots_on(mix,0,1)


def main():
    print('PROP28: baseline continuous equilibrium')
    for delta in [.19,.05,.02,.01,.005,.003,.001]:
        print(delta,continuous_eq(3,100,1,100,.01,delta))
    print('PROP28: multiplicity, both interior roots are GLOBAL best responses')
    for delta in [.95,.9,.85]:
        print(delta,continuous_eq(2,100,.5,1,.01,delta))
    print('PROP28 -> M(4): falling summable risk despite accelerating strength and full delegation')
    for t in [5,6,8,12,20]:
        n=3;s=2.**t;delta=2.**(-t)
        rows=continuous_eq(n,s,1,1,0,delta)
        derivative=s*(n-1)/(n*n*(1+s))-delta*(1-delta)**(n-1)
        print(dict(t=t,s=s,delta=delta,derivative_at_full=derivative,risk=1-(1-delta)**n,eq=rows))
        assert derivative>0 and rows[-1]['i']==1
    # Union bound t>=5 gives survival >=1-3 sum_{t>=5}2^-t=13/16.
    print('survival lower bound from t=5:',1-3*2**(-4))
    print('PROP22 baseline/global BR checks and two timings')
    for reg in ['SEP','CF']:
        states,d,roots,pure=frontier(reg)
        print(reg,states,d,roots,pure)
        if reg=='CF':
            print('fixed-incumbent deviations',simultaneous_deviation(states))
            print('endpoint belief cutoff',-d[-1]/(d[0]-d[-1]))
            print('actual coalition payoff C-vs-D differences, against singleton C and D:',
                  states[0]['Coop']-states[3]['Race'], states[1]['Coop']-states[4]['Race'])
    print('PROP32 BIC nonconstant ex-post shares')
    p=.8;eps=.5
    h={'S':1-p,'W':-p};prob={'S':p,'W':1-p}
    def share1(a,b):return .5+eps*h[a]*h[b]
    for report1 in h:
        print(report1,[share1(report1,b) for b in h],sum(prob[b]*share1(report1,b) for b in h))
    for report2 in h:
        print('agent2',report2,sum(prob[a]*(1-share1(a,report2)) for a in h))
    print('PROP32 arithmetic')
    for p in [.8,.5,.2,.05]:print(p,2*(1-p)*.9)
    for p in [.2,.05]:print('Lb=.5',p,2*((1-p)*1.5*.9-.5))
    print('survival ratio threshold',1.5/1.72)
    print('equal shares without lower Omega/compression: Sa=2; strongest outside=',1.5*.95-.5,'equal share=',1.)
    print('PROP13 insufficient n-player sufficient condition')
    p=sqrt(.5)
    diff=p*p*1+2*p*(1-p)*(-10)+(1-p)**2*(-1)
    print('each cooperates=',p,'all cooperate=',p*p,'claimed threshold=.5, actual advantage=',diff)
    assert diff<0
    print('PROP6 additive thresholds')
    n=3;psi0=.01;delta=.19;Le=Lc=1
    def gain(s,k):
        a=1+s
        return Le*(a/((k+1)*a+n-1-k)-1/(k*a+n-k))-Lc*delta*(1-psi0)**(n-1-k)*(1-psi0-delta)**k
    thresholds=[brentq(lambda s:gain(s,k),0,100) for k in range(n)]
    print('roots by rivals delegating:',thresholds,'dominance threshold:',max(thresholds))
    print('unshifted none,all:',-2/3-(1-.99**3),-2/3-(1-.8**3))
    print('PROP14 boundary example N=2: strict positive interval condition b<1/4 confirmed analytically.')
    print('PROP15 two enforcement formulas and log derivative verified analytically; no numeric contradiction.')
    print('M-prime: dangerous subset already covered, but X-based formula adds exposure')
    X,Y,U0,slope,h=2.,1.,1.,1.,.05
    true_area=0.
    wrong_area=(X-U0)**2/(2*X*slope)
    print(dict(X=X,Y=Y,U0=U0,true_area=true_area,X_based_area=wrong_area,
               invalid_survival_upper=exp(-h*wrong_area)))
    assert true_area==0 and wrong_area==.25
    print('PROP31: lock probability below one; all-D survival does not vanish with s')
    n,qL,psi0,psi1=2,.99,.01,.05
    A=(1-qL)*(1-psi1)/(1-psi0)
    threshold=(n/A-n)/(n-1)
    survival=(1-qL)*(1-psi1)**n/n
    print(dict(qL=qL,all_D_survival=survival,all_D_NE_speed_threshold=threshold))
    assert survival>0 and threshold>200
    print('PROP31/E: bounded-speed nondelegator, after one completed contest')
    print('n=2,s=1,p=qL=1,psi0=0,psi1=.01 -> nondelegator survival:',.99/3)
    print('THEOREM S: exact discrete survival-rate gap')
    print('qR=.005,qB=.05:',log(.995/.95),'small-risk approximation:',.05-.005)
    print('S5: high confidence does not preserve assurance when cooperative survival tends to zero')
    p,H=.99,1000
    R=exp(-.005*H)
    premise_race=exp(-.05*H)
    T=p*premise_race+(1-p)*.9
    P=p*premise_race+(1-p)*.4
    S=p*premise_race+(1-p)*.1
    print(dict(H=H,p=p,R=R,T=T,P=P,S=S,T_above_R=T>R,P_above_S=P>S))
    assert T>R and P>S
    print('Fixed independent splitting: eta=1,g=.2,alpha=0,k=10 delay=',2*log(10)/.2)
    print('Serial versus redundant oversight, f=.9,k=6:',.9**6,1-(1-.9)**6)

if __name__=='__main__':main()
