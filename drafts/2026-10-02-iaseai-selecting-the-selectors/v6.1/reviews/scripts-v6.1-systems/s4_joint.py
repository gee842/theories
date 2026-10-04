# S4: a minimal joint simulation for TESTS Study 2: conversion capacity q evolving at a finite rate together with the
# evaluation domain of the field model (10), against the quasi-static (QS) assumption of Assumption 4.2.
# Shared parameters as in checks_v61 block CS: chi=Y=eta=1, xi_v=0, dominant share p=0.6, A=0.3, a_E*B=1, c_E=1,
# d(t)=d0 e^{alpha_cor t} with d0=2, gamma(t)=e^{-alpha_ctl t} with alpha_ctl=0.2.  Rate law: alpha_cor >= alpha_ctl/2 = 0.1.
# Field: u=logit x_ev, u'=zeta(z-1), z'=eps(A+p q - d z), G_ev=(A+p q)/d. Seeded x_ev(0)=0.01; zeta=1, eps=0.5.
# Capacity dynamics:
#   QS        q=q*(t)=chi p^2 Y/(gamma d)
#   R(k)      q'=k (q*-q)                                  (constant-rate lag: management, investment pipeline)
#   GA(V)     q'=V (chi p^2 Y/d - gamma q) = V gamma (q*-q)   (Price gradient, constant additive trait variance)
#   GM(V)     q'=(V/q0^2) q^2 gamma (q*-q)                  (Price gradient, variance proportional to q^2)
# Integration: exponential (exact-for-frozen-coefficients) updates for the stiff linear z and q equations; trapezoid for u.
import math
p,A,chi,Y=0.6,0.3,1.0,1.0
actl,d0=0.2,2.0
zeta,eps=1.0,0.5
def gam(t): return math.exp(-actl*t)
def dd(t,acor): return d0*math.exp(acor*t)
def qstar(t,acor): return chi*p*p*Y/(gam(t)*dd(t,acor))
q0=qstar(0,0.0)
def qrate(mode,par,t,q):
    if mode=='R': return par
    if mode=='GA': return par*gam(t)
    if mode=='GM': return (par/q0**2)*q*q*gam(t)
def run(acor,mode,par=None,H=300.0,dt=0.01,x0=0.01,record=False):
    u=math.log(x0/(1-x0)); q=q0; z=(A+p*q0)/d0; t=0.0; Tc=None; rec=[]
    while t<H:
        tm=t+dt/2; d=dd(tm,acor); qs=qstar(tm,acor)
        if mode=='QS': qn=qs
        else:
            k=qrate(mode,par,tm,q); qn=qs+(q-qs)*math.exp(-k*dt)
        qq=0.5*(q+qn) if mode!='QS' else qs
        G=(A+p*qq)/d
        if Tc is None and G>1: Tc=t
        zn=G+(z-G)*math.exp(-eps*d*dt)
        u+=zeta*(0.5*(z+zn)-1.0)*dt
        z,q=zn,qn; t+=dt
        if record and abs(t-round(t))<dt/2 and int(round(t))%10==0: rec.append((round(t),G,q/qs,u))
        if u>0: return Tc,t,rec
    return Tc,None,rec
modes=[('QS',None),('R',1.0),('R',0.1),('R',0.03),('GA',1.0),('GA',0.1),('GM',1.0),('GM',0.1)]
def lab(m,par): return m+('' if par is None else '('+str(par)+')')
if __name__=='__main__':
    print("E1. Certificate failure time T_cert (G_ev>1) / capture time T_cap (x_ev>1/2), horizon 300")
    for acor in (0.0,0.05,0.08,0.09,0.095,0.10,0.105):
        row=[]
        for m,par in modes:
            Tc,Tx,_=run(acor,m,par)
            f=lambda v: '  -  ' if v is None else f"{v:5.1f}"
            row.append(f"{lab(m,par)}: {f(Tc)}/{f(Tx)}")
        print(f"   alpha_cor={acor:5.3f}  "+" | ".join(row))
    def crit(mode,par,H):
        lo,hi=0.0,0.2
        for _ in range(16):
            m=(lo+hi)/2
            if run(m,mode,par,H=H)[1] is not None: lo=m
            else: hi=m
        return lo
    print("E1'. Largest alpha_cor at which x_ev is captured within horizon H (rate-law asymptote 0.100)")
    for H in (150.0,300.0,600.0):
        print(f"   H={H:.0f}: "+"  ".join(f"{lab(m,par)}={crit(m,par,H):.4f}" for m,par in modes))
    print("E1''. Lag ratio q/q* along the path, alpha_cor=0.05")
    for m,par in modes[1:]:
        _,_,rec=run(0.05,m,par,record=True,H=60)
        print(f"   {lab(m,par)}: "+" ".join(f"t={t}:{r:.2f}" for t,G,r,u in rec))
