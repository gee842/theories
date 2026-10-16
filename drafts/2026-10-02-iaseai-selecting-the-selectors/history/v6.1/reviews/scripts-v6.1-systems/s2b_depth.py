# S2b: the dwell depends on the depth of lock-in at the start (x0), and a floor on alternatives bounds it.
# Reuses s2_dwell's separatrix and analytic insulated path.
import math, importlib.util, sys, io, contextlib
spec=importlib.util.spec_from_file_location("s2","s2_dwell.py"); s2=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(s2)
print("No floor: T_min*eps*d as a function of the starting share x0 (paper fixes x0=0.99)")
for eps in (0.1,1.0):
    for G in (2,10):
        pts=s2.separatrix(G,eps)
        row=[f"x0=1-{1-x0:.0e}: {s2.tmin_analytic(G,eps,pts,x0=x0):.2f}" for x0 in (0.9,0.99,1-1e-3,1-1e-6,1-1e-12)]
        print(f"   G={G}, eps/zeta={eps}: "+"  ".join(row))
print("Age of capture: at the captured state logit x grows at zeta(G-1) per unit time, so after capture has lasted A,")
print("   x0 ~ 1-exp(-zeta(G-1)A): with zeta=1, G=2, A=10 -> 1-4.5e-5; A=30 -> 1-9e-14. The dwell grows ~linearly with the age of capture")
print("   unless something (mutation, immigration, a recruiting alternative lineage) bounds the alternative's share from below.")
print("(B') mutation started from x0=0.99 (as in the paper), mu=lam*zeta*(G-1)")
def tmin_mut0(G,eps,lam,x0=0.99,zeta=1.0,dt=0.01):
    mu=lam*zeta*(G-1); u,z=s2.logit(x0),float(G)
    def f(uu,zz):
        x=s2.sig(uu); return (zeta*(zz-1.0)+mu*(1-2*x)/max(x*(1-x),1e-300), -eps*zz)
    def after(T):
        uu,zz=u,z
        for _ in range(int(T/dt)):
            k1=f(uu,zz);k2=f(uu+dt/2*k1[0],zz+dt/2*k1[1]);k3=f(uu+dt/2*k2[0],zz+dt/2*k2[1]);k4=f(uu+dt*k3[0],zz+dt*k3[1])
            uu+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; zz+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        return s2.fate_mut(uu,zz,G,eps,mu)
    lo,hi=0.0,40.0/eps
    for _ in range(26):
        m=(lo+hi)/2
        if after(m)=='cap': lo=m
        else: hi=m
    return hi*eps
for lam in (1e-3,1e-6):
    print(f"   lam={lam:g}: "+"  ".join(f"G={G},e/z={eps}: {tmin_mut0(G,eps,lam):.2f}" for eps in (0.1,1.0) for G in (5,10)))
