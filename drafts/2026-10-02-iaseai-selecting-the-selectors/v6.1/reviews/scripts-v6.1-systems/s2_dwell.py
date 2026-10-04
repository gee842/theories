# S2: dwell times of an insulating reform in the D=1 field model (10), by a method independent of checks_v61 DW:
#  - the separatrix (stable manifold of the saddle) is computed by BACKWARD integration from the saddle;
#  - the insulated trajectory is ANALYTIC: z(t)=G e^{-eps t}, u(t)=u0+zeta[G(1-e^{-eps t})/eps - t]   (a=c=d=1, b=G);
#  - T_min = first time the insulated trajectory is below the separatrix (absence basin is a down-set, so first entry suffices).
# Alternative lineage, three formulations:
#  (A) hard floor on the alternative share lam (u <= logit(1-lam)) -- the formulation behind the 3.81 figure;
#  (B) symmetric mutation/re-seeding at rate mu (x' += mu(1-2x)), mu set so the captured alternative share is ~lam;
#  (C) a protected share lam outside selection that does not recruit (x=(1-lam) y): equivalent to b -> b(1-lam).
import math
def sig(u): return 1/(1+math.exp(-u)) if u>=0 else math.exp(u)/(1+math.exp(u))
def logit(x): return math.log(x/(1-x))

def separatrix(G,eps,zeta=1.0,h=1e-4,dt=1e-3):
    # returns list of (u,z) on the stable manifold of the saddle (u_s,1), both branches, by RK4 in reversed time
    us=-math.log(G-1.0); b=G
    lam=(-eps-math.sqrt(eps*eps+4*zeta*eps*(1-1/G)))/2
    v=(1.0,lam/zeta); nv=math.hypot(*v); v=(v[0]/nv,v[1]/nv)
    def f(u,z): return (-zeta*(z-1.0), -eps*(b*sig(u)-z))   # reversed time
    pts=[]
    for sgn in (1,-1):
        u,z=us+sgn*h*v[0],1.0+sgn*h*v[1]; br=[(u,z)]
        for _ in range(4000000):
            k1=f(u,z);k2=f(u+dt/2*k1[0],z+dt/2*k1[1]);k3=f(u+dt/2*k2[0],z+dt/2*k2[1]);k4=f(u+dt*k3[0],z+dt*k3[1])
            u+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; z+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
            br.append((u,z))
            if z<-0.05 or z>60 or u<-60: break
        pts+=br
    pts.sort()
    return pts
def zsep(pts,u):
    # separatrix height at u (decreasing curve); linear interpolation; +inf left of range, -inf right of range
    if u<=pts[0][0]: return float('inf')
    if u>=pts[-1][0]: return -float('inf')
    lo,hi=0,len(pts)-1
    while hi-lo>1:
        m=(lo+hi)//2
        if pts[m][0]<=u: lo=m
        else: hi=m
    (u0,z0),(u1,z1)=pts[lo],pts[hi]
    return z0+(z1-z0)*(u-u0)/(u1-u0) if u1>u0 else z0
def x_sigma(pts):
    # share where separatrix meets z=0
    for (u0,z0),(u1,z1) in zip(pts,pts[1:]):
        if z0>=0>z1: return sig(u0+(u1-u0)*z0/(z0-z1))
    return None

def tmin_analytic(G,eps,pts,zeta=1.0,x0=0.99,ucap=None,dt=1e-3):
    u0=logit(x0); t=0.0
    tpk=math.log(G)/eps
    while t<500/eps:
        if ucap is None:
            u=u0+zeta*(G*(1-math.exp(-eps*t))/eps-t)
        else:
            # capped: u rises until cap, sticks while z>1, then falls from the cap
            tc=None
            # time to hit cap during rise (bisection on rising part)
            f=lambda s:u0+zeta*(G*(1-math.exp(-eps*s))/eps-s)-ucap
            if f(tpk)>0:
                lo,hi=0.0,tpk
                for _ in range(80):
                    m=(lo+hi)/2
                    if f(m)>0: hi=m
                    else: lo=m
                tc=hi
            if tc is None or t<=tc: u=min(u0+zeta*(G*(1-math.exp(-eps*t))/eps-t),ucap)
            elif t<=tpk: u=ucap
            else: u=ucap+zeta*(G*(math.exp(-eps*tpk)-math.exp(-eps*t))/eps-(t-tpk))
        z=G*math.exp(-eps*t)
        if z<zsep(pts,u): return t*eps
        t+=dt/eps
    return float('inf')

print("Dwell T_min*eps*d by separatrix + analytic insulated path (paper S11: eps/zeta=0.1: 1.89,5.32,10.45; eps=zeta: 5.86,10.34,16.18)")
seps={}
for eps in (0.1,1.0):
    row=[]
    for G in (2,5,10):
        pts=separatrix(G,eps); seps[(G,eps)]=pts
        row.append(f"G={G}: {tmin_analytic(G,eps,pts):.3f} (x_sigma={x_sigma(pts):.3f})")
    print(f"   eps/zeta={eps}: "+"; ".join(row))
print("Back-to-start time s*: G(1-e^-s)=s")
for G in (2,5,10):
    lo,hi=1e-9,60.0
    for _ in range(200):
        m=(lo+hi)/2
        if G*(1-math.exp(-m))-m>0: lo=m
        else: hi=m
    print(f"   G={G}: ln G={math.log(G):.3f}, s*={lo:.3f}")
print("(A) hard floor on the alternative share lam (cap on u during insulation; separatrix unchanged below the cap)")
for lam in (1e-2,1e-3,1e-6,1e-12):
    ucap=logit(1-lam); row=[]
    for eps in (0.1,1.0):
        for G in (5,10):
            pts=seps[(G,eps)]
            row.append(f"G={G},e/z={eps}: {tmin_analytic(G,eps,pts,ucap=ucap):.2f}")
    print(f"   lam={lam:g}: "+"  ".join(row))

# (B) mutation: forward simulation in logit coordinates, fate decided by long run
def fate_mut(u,z,G,eps,mu,zeta=1.0,dt=0.01,T=3000):
    b=G
    def f(u,z):
        x=sig(u)
        return (zeta*(z-1.0)+mu*(1-2*x)/max(x*(1-x),1e-300), eps*(b*x-z))
    for _ in range(int(T/dt)):
        k1=f(u,z);k2=f(u+dt/2*k1[0],z+dt/2*k1[1]);k3=f(u+dt/2*k2[0],z+dt/2*k2[1]);k4=f(u+dt*k3[0],z+dt*k3[1])
        u+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; z+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        if z>0.5*(1+G) and u>2: return 'cap'
        if z<0.2 and u<-2: return 'abs'
    return 'cap' if u>0 else 'abs'
def tmin_mut(G,eps,lam,zeta=1.0,dt=0.01):
    mu=lam*zeta*(G-1)       # captured alternative share ~ lam
    # start at the captured equilibrium of the mutated system
    u,z=logit(1-lam),G*(1-lam)
    def after(T):
        uu,zz=u,z; n=int(T/dt)
        def f(uu,zz):
            x=sig(uu); return (zeta*(zz-1.0)+mu*(1-2*x)/max(x*(1-x),1e-300), -eps*zz)
        for _ in range(n):
            k1=f(uu,zz);k2=f(uu+dt/2*k1[0],zz+dt/2*k1[1]);k3=f(uu+dt/2*k2[0],zz+dt/2*k2[1]);k4=f(uu+dt*k3[0],zz+dt*k3[1])
            uu+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; zz+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        return fate_mut(uu,zz,G,eps,mu)
    lo,hi=0.0,40.0/eps
    for _ in range(26):
        m=(lo+hi)/2
        if after(m)=='cap': lo=m
        else: hi=m
    return hi*eps
print("(B) mutation/re-seeding at rate mu=lam*zeta*(G-1), started from its own captured equilibrium")
for lam in (1e-3,1e-6):
    print(f"   lam={lam:g}: "+"  ".join(f"G={G},e/z={eps}: {tmin_mut(G,eps,lam):.2f}" for eps in (0.1,1.0) for G in (5,10)))
print("(C) protected share outside selection, no recruitment: b->b(1-lam); lam=1e-3 changes G=10 to 9.99, dwell essentially unchanged")
pts=separatrix(10*(1-1e-3),0.1)
print(f"   G=9.99, eps/zeta=0.1: {tmin_analytic(10*(1-1e-3),0.1,pts):.2f}")
