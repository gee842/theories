"""Equilibrium loop gain: in the MPE of s2_mpe, efforts respond to standing, so the win probability responds to
standing by dp/ds != r. Effective loop gain Gamma_eq = Gamma * (dp/ds)/r at s=1/2 (expected-share dynamics)."""
import math
def mpe(r,G,d=0.2,delta=0.9,N=800,l=0.0):
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
        return p,A1p*p*(1-p)/(1+l),A2p*p*(1-p)/(1+l),sw,sl
    V=[0.0]*(N+1)
    for it in range(5000):
        Vn=[]
        for s in grid:
            p,e1,e2,sw,sl=stage(s,V)
            Vn.append(Om*p-e1-l*(e1+e2)+delta*(p*interp(V,sw)+(1-p)*interp(V,sl)))
        diff=max(abs(a-b) for a,b in zip(V,Vn)); V=Vn
        if diff<1e-12: break
    h=2.0/N
    dp=(stage(0.5+h,V)[0]-stage(0.5-h,V)[0])/(2*h)
    return dp
for r,G in ((1.0,0.6),(1.5,0.6),(1.5,0.9),(1.0,0.9)):
    for delta in (0.9,0.97):
        dp=mpe(r,G,delta=delta)
        print(f"r={r} Gamma={G} delta={delta}: dp/ds at parity, MPE = {dp:.3f} vs r = {r}; equilibrium loop gain Gamma*(dp/ds)/r = {G*dp/r:.3f}")
