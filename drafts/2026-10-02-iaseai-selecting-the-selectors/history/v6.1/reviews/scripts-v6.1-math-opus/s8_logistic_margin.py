"""Theorem 10.5(1) on the forgiving logistic host: margin needed for VIABILITY (V>=V_min throughout), x0=0.99 race share."""
import math
rho,h=0.05,0.08
def vmin(Delta,emin=0.0,emax=1.0,x0=0.99,T=2000,dt=0.02):
    x,V=x0,1.0; m=V
    def f(x,V):
        return x*(1-x)*(-Delta*(emax-emin)), V*(rho*(1-V)-h*(emin+(emax-emin)*x))
    for _ in range(int(T/dt)):
        k1=f(x,V);k2=f(x+dt/2*k1[0],V+dt/2*k1[1]);k3=f(x+dt/2*k2[0],V+dt/2*k2[1]);k4=f(x+dt*k3[0],V+dt*k3[1])
        x+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; V+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6; m=min(m,V)
    return m
print("Delta=0.08 (paper): min V =", round(vmin(0.08),4))
for Vmin_ in (0.2,0.3,0.5):
    lo,hi=0.0,5.0
    for _ in range(40):
        mid=(lo+hi)/2
        if vmin(mid)<Vmin_: lo=mid
        else: hi=mid
    print(f"floor {Vmin_}: liability margin needed for viability on the logistic host, Delta_min={hi:.3f}")
