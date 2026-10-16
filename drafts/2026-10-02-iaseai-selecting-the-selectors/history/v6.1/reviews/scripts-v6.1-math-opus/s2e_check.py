"""Robustness of the equilibrium loop gain (r=1.5, Gamma=0.6, d=0.2, delta=0.9, N=1600): dp/ds at parity for several
finite-difference steps; expected-share path from 0.52; stochastic dispersion after 100 periods, MPE vs passive."""
import math, random
r,G,d,delta,N=1.5,0.6,0.2,0.9,1600
om=G/r; kap=0.5; Om=1.0; k0=kap*Om*(1/om-1)/2; S=(kap*Om+2*k0)/d
jw=(kap*Om+k0)/S; jl=k0/S; grid=[i/N for i in range(N+1)]
def interp(a,x):
    if x<=0: return a[0]
    if x>=1: return a[-1]
    k=min(int(x*N),N-1); w=x*N-k; return a[k]*(1-w)+a[k+1]*w
def stage(s,V):
    sw,sl=(1-d)*s+jw,(1-d)*s+jl
    A1=Om+delta*(interp(V,sw)-interp(V,sl)); A2=Om+delta*(interp(V,1-sl)-interp(V,1-sw))
    a1,a2=(s**r,(1-s)**r) if 0<s<1 else ((0.0,1.0) if s<=0 else (1.0,0.0))
    A1p,A2p=max(A1,0),max(A2,0); den=a1*A1p+a2*A2p
    p=a1*A1p/den if den>0 else 0.5
    return p,A1p*p*(1-p),A2p*p*(1-p),sw,sl
V=[0.0]*(N+1)
for it in range(5000):
    Vn=[]
    for s in grid:
        p,e1,e2,sw,sl=stage(s,V); Vn.append(Om*p-e1+delta*(p*interp(V,sw)+(1-p)*interp(V,sl)))
    diff=max(abs(a-b) for a,b in zip(V,Vn)); V=Vn
    if diff<1e-12: break
for h in (0.0025,0.01,0.02,0.05):
    dp=(stage(0.5+h,V)[0]-stage(0.5-h,V)[0])/(2*h); print(f"h={h}: dp/ds={dp:.3f}; Gamma_eq={G*dp/r:.3f}")
s=0.52
for t in range(40):
    p,_,_,sw,sl=stage(s,V); s=p*sw+(1-p)*sl
print("expected-share path from 0.52 after 40 periods:", round(s,3))
def simul(policy,T=100,R=2000,seed=1):
    rnd=random.Random(seed); out=[]
    for _ in range(R):
        s=0.5
        for t in range(T):
            p=stage(s,V)[0] if policy=='mpe' else s**r/(s**r+(1-s)**r)
            sw,sl=(1-d)*s+jw,(1-d)*s+jl; s=sw if rnd.random()<p else sl
        out.append(abs(s-0.5))
    out.sort(); return sum(out)/R, out[int(0.9*R)]
print("mean |s-1/2|, 90th pct after 100 periods: MPE", [round(x,3) for x in simul('mpe')], " passive", [round(x,3) for x in simul('passive')])
