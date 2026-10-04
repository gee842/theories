"""Prop 4.5(3) under [H_f]: is min{alpha_f, alpha_ctl/(1+eta)} the required rate? (linear 'fixed part' f p q)"""
import math
def qstar(p,d,f,gam,eta=1.0):
    m=p*p/d-f
    return (m/gam)**(1/eta) if m>0 else 0.0
def run(alpha,af,f0,g=0.2,d0=2.0,A=0.3,p=0.6,T=600,dt=0.05):
    t=0; first=None; last=None; smax=0
    while t<T:
        d=d0*math.exp(alpha*t); f=f0*math.exp(-af*t); gam=math.exp(-g*t)
        sE=(A+p*qstar(p,d,f,gam))/d
        if sE>1:
            if first is None: first=t
            last=t
        smax=max(smax,sE); t+=dt
    return first,last,smax
print("alpha_ctl=0.2, eta=1 (alpha_ctl/(1+eta)=0.1), alpha_f=0.05; f0 chosen so cultivation is positive at t=0 (p^2/d0=0.18>f0)")
for f0 in (0.1,0.17,0.3):
    for alpha in (0.05,0.06,0.08):
        fi,la,sm=run(alpha,0.05,f0)
        print(f"  f0={f0}, alpha_cor={alpha}: certificate first fails at {fi}, last failure {la}, max s_E {sm:.3g}")
print("Supplement S4 says the level chi*Y/(f p^xf) 'falls at alpha_f' under [H_f]; with f=f0 e^{-alpha_f t} it rises:")
for t in (0,10,20): print(f"  t={t}: level ~ 1/f = {1/(0.3*math.exp(-0.05*t)):.3f}")
