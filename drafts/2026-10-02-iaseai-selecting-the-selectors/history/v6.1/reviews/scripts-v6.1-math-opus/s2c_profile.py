"""Price of standing away from equal standing, in the MPE and with others fixed (same model as s2_mpe)."""
import s2_mpe, math
def profile(r,G,d=0.2,delta=0.9,N=800):
    om=G/r; kap=0.5; Om=1.0; k0=kap*Om*(1/om-1)/2; S=(kap*Om+2*k0)/d
    jw=(kap*Om+k0)/S; jl=k0/S
    # rerun to get V and W: copy of internals
    grid=[i/N for i in range(N+1)]
    def interp(a,x):
        if x<=0: return a[0]
        if x>=1: return a[-1]
        k=min(int(x*N),N-1); w=x*N-k; return a[k]*(1-w)+a[k+1]*w
    V=[0.0]*(N+1)
    for it in range(5000):
        Vn=[]
        for s in grid:
            sw,sl=(1-d)*s+jw,(1-d)*s+jl
            A1=Om+delta*(interp(V,sw)-interp(V,sl)); A2=Om+delta*(interp(V,1-sl)-interp(V,1-sw))
            a1,a2=(s**r,(1-s)**r) if 0<s<1 else ((0.0,1.0) if s<=0 else (1.0,0.0))
            A1p,A2p=max(A1,0),max(A2,0); den=a1*A1p+a2*A2p
            p=a1*A1p/den if den>0 else 0.5; e1=A1p*p*(1-p); e2=A2p*p*(1-p)
            Vn.append(Om*p-e1+delta*(p*interp(V,sw)+(1-p)*interp(V,sl)))
        diff=max(abs(a-b) for a,b in zip(V,Vn)); V=Vn
        if diff<1e-12: break
    W=[0.0]*(N+1)
    for it in range(5000):
        Wn=[]
        for s in grid:
            pp=s**r/(s**r+(1-s)**r) if 0<s<1 else (0.0 if s<=0 else 1.0)
            sw,sl=(1-d)*s+jw,(1-d)*s+jl
            Wn.append(Om*pp+delta*(pp*interp(W,sw)+(1-pp)*interp(W,sl)))
        diff=max(abs(a-b) for a,b in zip(W,Wn)); W=Wn
        if diff<1e-12: break
    Gd=G*delta*d/(1-delta*(1-d)); lam=Gd/(1-Gd)
    print(f"r={r} Gamma={G}: formula lambda at s=1/2 = {lam:.3f}")
    for s in (0.1,0.25,0.4,0.5,0.6,0.75,0.9):
        sw,sl=(1-d)*s+jw,(1-d)*s+jl
        lm=delta*(interp(V,sw)-interp(V,sl))/Om; lf=delta*(interp(W,sw)-interp(W,sl))/Om
        print(f"   s={s}: lambda_fixed={lf:.3f} lambda_MPE={lm:.3f}  theta(n=2): fixed {-lf/(2+lf):+.3f}, MPE {-lm/(2+lm):+.3f}")
profile(1.5,0.9); profile(1.5,1.2)
