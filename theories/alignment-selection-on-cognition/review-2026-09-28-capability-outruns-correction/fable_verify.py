import math, random, cmath
random.seed(7)

def rk4_step(f, y, t, dt):
    k1 = f(t, y)
    k2 = f(t+dt/2, [yi+dt/2*ki for yi,ki in zip(y,k1)])
    k3 = f(t+dt/2, [yi+dt/2*ki for yi,ki in zip(y,k2)])
    k4 = f(t+dt, [yi+dt*ki for yi,ki in zip(y,k3)])
    return [yi+dt/6*(p+2*q+2*u+v) for yi,p,q,u,v in zip(y,k1,k2,k3,k4)]

def integrate(f, y0, T, dt, stop=None):
    y = list(y0); t = 0.0; traj=[(t, list(y))]
    for i in range(int(T/dt)):
        y = rk4_step(f, y, t, dt); t += dt
        traj.append((t, list(y)))
        if stop and stop(t, y): break
    return traj

def core_f(p):
    a,b,c,d,kap,eps = p
    return lambda t,y: [kap*y[0]*(1-y[0])*(a*y[1]-c), eps*(b*y[0]-d*y[1])]
def jac(p,x,r):
    a,b,c,d,kap,eps = p
    return [[kap*(1-2*x)*(a*r-c), kap*a*x*(1-x)],[eps*b, -eps*d]]
def eig2(J):
    tr = J[0][0]+J[1][1]; det = J[0][0]*J[1][1]-J[0][1]*J[1][0]
    s = cmath.sqrt(complex(tr*tr-4*det))
    return (tr+s)/2, (tr-s)/2, det, tr
def Phi(p,x,r):
    a,b,c,d,kap,eps = p
    return a*x*r - c*x - a*d/(2*b)*r*r
def Phidot(p,x,r):
    a,b,c,d,kap,eps = p
    return kap*x*(1-x)*(a*r-c)**2 + eps*a/b*(b*x-d*r)**2
def Rcap(p):
    a,b,c,d,kap,eps = p
    return a*b/(c*d)

print("=== A. Equilibria and Jacobian eigenvalues ===")
for p in [(1,1,0.5,1,1,1),(1,1,2,1,1,1),(2,1.5,0.7,1.2,0.8,0.3),(1,1,1,1,1,1)]:
    a,b,c,d,kap,eps = p
    R = Rcap(p)
    print(f"p={p} R_cap={R:.3f}")
    for name,(x,r) in [("L",(0,0)),("H",(1,b/d)),("S",(c*d/(a*b), c/a))]:
        f = core_f(p)(0,[x,r])
        l1,l2,det,tr = eig2(jac(p,x,r))
        print(f"  {name}=({x:.3f},{r:.3f}) f={tuple(round(v,12) for v in f)} eig=({l1:.3f},{l2:.3f}) det={det:.3f}")
    print(f"  predicted H eigen: -kappa*c*(R-1)={-kap*c*(R-1):.3f}, -eps*d={-eps*d:.3f}")

print("\n=== B. Phi-dot formula check (finite difference along RK4 flow) ===")
p=(2,1.5,0.7,1.2,0.8,0.3); f=core_f(p); worst=0
for _ in range(200):
    x=random.uniform(0.001,0.999); r=random.uniform(0,3); dt=1e-4
    yp=rk4_step(f,[x,r],0,dt); ym=rk4_step(f,[x,r],0,-dt)
    num=(Phi(p,*yp)-Phi(p,*ym))/(2*dt); an=Phidot(p,x,r)
    worst=max(worst,abs(num-an)/(1+abs(an)))
print("max relative discrepancy:",worst)
print("Phidot at equilibria:", [Phidot(p,*e) for e in [(0,0),(1,p[1]/p[3]),(p[2]*p[3]/(p[0]*p[1]),p[2]/p[0])]])

print("\n=== C. R_cap<1: global convergence to (0,0) ===")
p=(1,1,2,1,1,1); f=core_f(p); worst=0; maxx=0
for _ in range(200):
    x0=random.uniform(0.01,0.99); r0=random.uniform(0,10)
    tr=integrate(f,[x0,r0],300,0.02)
    xs=[y[0] for _,y in tr]; maxx=max(maxx,max(xs))
    worst=max(worst,math.hypot(*tr[-1][1]))
print("R_cap=",Rcap(p)," max final distance from (0,0):",worst," (some transients rose to x=%.3f)"%maxx)
# monotone Phi check
p2=(1,1,0.5,1,1,1); f2=core_f(p2); mind=0
for _ in range(50):
    tr=integrate(f2,[random.uniform(0.01,0.99),random.uniform(0,3)],100,0.01)
    ph=[Phi(p2,*y) for _,y in tr]
    mind=min(mind,min(b-a for a,b in zip(ph,ph[1:])))
print("min increment of Phi along 50 trajectories (R_cap=2):",mind)

print("\n=== D. R_cap>1: bistability, basins, path dependence ===")
p=(1,1,0.5,1,1,1); f=core_f(p); a,b,c,d,kap,eps=p
L=(0,0); H=(1,b/d); S=(c*d/(a*b),c/a)
def classify(x0,r0,T=400):
    stop=lambda t,y: math.hypot(y[0]-L[0],y[1]-L[1])<1e-4 or math.hypot(y[0]-H[0],y[1]-H[1])<1e-4
    tr=integrate(f,[x0,r0],T,0.02,stop)
    y=tr[-1][1]
    if math.hypot(y[0]-L[0],y[1]-L[1])<1e-3: return "L"
    if math.hypot(y[0]-H[0],y[1]-H[1])<1e-3: return "H"
    return "?"+str(y)
print("S =",S,"  1/R_cap =",1/Rcap(p))
print("basin map (rows r0 from 3.0 down to 0, cols x0 0.05..0.95):")
for r0 in [3,2.5,2,1.5,1,0.75,0.5,0.25,0]:
    print(f"  r0={r0:<4}", "".join(classify(x0/20,r0) for x0 in range(1,20)))
lo,hi=0.01,0.99
for _ in range(40):
    mid=(lo+hi)/2
    if classify(mid,0)=="L": lo=mid
    else: hi=mid
print("basin boundary on r=0 axis: x_exit ~",(lo+hi)/2," vs instantaneous-rule threshold 1/R_cap =",1/Rcap(p))
print("path dependence: x0=0.3,r0=0 ->",classify(0.3,0),"; x0=0.3,r0=2 ->",classify(0.3,2))

print("\n=== E. Stable manifold of S by backward integration ===")
J=jac(p,*S); l1,l2,det,tr=eig2(J); lam=min(l1.real,l2.real)
v=[1.0, lam/(kap*a*S[0]*(1-S[0]))]  # from first row: kap*a*x*(1-x)*v2 = lam*v1
n=math.hypot(*v); v=[v[0]/n,v[1]/n]
print("eigenvalues at S:",l1,l2," stable eigvec:",v)
fb=lambda t,y: [-z for z in f(t,y)]
for sgn in (+1,-1):
    y0=[S[0]+sgn*1e-6*v[0], S[1]+sgn*1e-6*v[1]]
    tr=integrate(fb,y0,60,0.001,lambda t,y: y[1]<0 or y[0]>1-1e-9 or y[0]<1e-9 or y[1]>50)
    t,y=tr[-1]
    print(f"  branch sgn={sgn:+d}: leaves domain at t_back={t:.2f}, point=({y[0]:.4f},{y[1]:.4f})")
    if y[1]<0:
        (t1,y1),(t2,y2)=tr[-2],tr[-1]
        xe=y1[0]+(y2[0]-y1[0])*(0-y1[1])/(y2[1]-y1[1])
        print(f"     crosses r=0 at x_exit ~ {xe:.4f} (compare bisection above)")

print("\n=== F. Substrate eq.(3) with x(t) from a trajectory to H (R_cap=2) ===")
trH=integrate(f,[0.6,0.6],200,0.01)
xs=[y[0] for _,y in trH]
def xof(t):
    i=min(int(round(t/0.01)),len(xs)-1); return xs[i]
K=1.0
for h,rho in [(1.0,0.5),(0.5,0.5),(0.25,0.5)]:
    g=lambda t,y: [y[0]*(rho*(1-y[0]/K)-h*xof(t))]
    tv=integrate(g,[1.0],200,0.01)
    V=lambda t: tv[int(round(t/0.01))][1][0]
    tag = "h>rho" if h>rho else ("h=rho" if h==rho else "h<rho")
    print(f"  {tag}: V(50)={V(50):.4e} V(100)={V(100):.4e} V(200)={V(200):.4e}", end=" ")
    if h>rho: print(f"  log-decay rate over [100,200] = {(math.log(V(200))-math.log(V(100)))/100:.4f}  (predicted -(h-rho)={-(h-rho)})")
    elif h==rho: print(f"  t*V(t) at 100,200 = {100*V(100):.3f},{200*V(200):.3f} (predicted K/rho={K/rho})")
    else: print(f"  predicted limit K(1-h/rho)={K*(1-h/rho)}")

print("\n=== G. Forward invariance (eq.5) ===")
K=1.0; rho=0.5; h=1.0; Vmin=0.3; xbar=rho*(1-Vmin/K)/h
print("xbar bound =",xbar)
for label,xfun in [("x<=xbar",lambda t: xbar*(0.6+0.4*math.sin(2*t))),("x=xbar",lambda t: xbar),("x=0.5>xbar",lambda t: 0.5)]:
    g=lambda t,y: [y[0]*(rho*(1-y[0]/K)-h*xfun(t))]
    tv=integrate(g,[Vmin],100,0.01)
    print(f"  {label}: min V = {min(y[0] for _,y in tv):.5f} (Vmin={Vmin})")

print("\n=== H. Transition-path demo: reform makes R_cap<1, but V crosses the floor first ===")
pre=(1,1,0.5,1,1,0.2); post=(1,1,0.5,3,1,0.2)
print("R_cap before reform:",Rcap(pre)," after:",Rcap(post))
K=1.0; rho=0.5; h=0.8; Vmin=0.3
fp=core_f(post)
def full(t,y):
    x,r,V=y; dx,dr=fp(t,[x,r]); return [dx,dr,V*(rho*(1-V/K)-h*x)]
tr=integrate(full,[0.98,1.0,0.6],80,0.005)
tV=next((t for t,y in tr if y[2]<Vmin),None); tx=next((t for t,y in tr if y[0]<0.5),None)
tmin,ymin=min(tr,key=lambda e:e[1][2])
print(f"  V first < Vmin at t={tV}; x first < 0.5 at t={tx}; min V={ymin[2]:.4f} at t={tmin:.2f}; final (x,r,V)={tuple(round(v,4) for v in tr[-1][1])}")

print("\n=== I. Spectral-radius threshold, incl. reducible cases ===")
def cubic_roots(c2,c1,c0):
    roots=[complex(0.4,0.9)**k for k in range(3)]
    for _ in range(800):
        new=[]
        for i,ri in enumerate(roots):
            num=ri**3+c2*ri**2+c1*ri+c0; den=1
            for j,rj in enumerate(roots):
                if j!=i: den*=(ri-rj)
            new.append(ri-num/den if den!=0 else ri+1e-3)
        roots=new
    return roots
def eig3(M):
    tr=M[0][0]+M[1][1]+M[2][2]
    m2=(M[0][0]*M[1][1]-M[0][1]*M[1][0])+(M[0][0]*M[2][2]-M[0][2]*M[2][0])+(M[1][1]*M[2][2]-M[1][2]*M[2][1])
    det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    return cubic_roots(-tr,m2,-det)
for g in [0.5,1.0,1.5]:
    print(f"  2-channel g={g}: eig(B-D)=({-1+g},{-1-g}); rho(D^-1B)={g}")
print("  reducible B=[[0,g],[0,0]], D=I: rho(D^-1 B)=0, eig(B-D)=(-1,-1) for any g -> stable, threshold holds")
print("  reducible B=diag(2,0), D=I: rho=2, eig(B-D)=(1,-1) -> growing direction, threshold holds")
mism=0; tested=0
for trial in range(400):
    B=[[random.choice([0,0,random.uniform(0,2)]) for j in range(3)] for i in range(3)]
    D=[random.uniform(0.3,2) for i in range(3)]
    DinvB=[[B[i][j]/D[i] for j in range(3)] for i in range(3)]
    BmD=[[B[i][j]-(D[i] if i==j else 0) for j in range(3)] for i in range(3)]
    rho_sp=max(abs(z) for z in eig3(DinvB)); s=max(z.real for z in eig3(BmD))
    if abs(rho_sp-1)<0.02 or abs(s)<0.01: continue
    tested+=1
    if (rho_sp<1)!=(s<0): mism+=1
print(f"  random 3x3 (many reducible): tested={tested}, sign mismatches between rho(D^-1B)<1 and s(B-D)<0: {mism}")

print("\n=== J. Crossing time eq.(6) and worst-case EV rule ===")
C0,A0,qmax,g,al=1.0,2.0,4.0,0.3,0.1
ts=math.log(qmax*A0/C0)/(g-al); q=lambda t:(C0/A0)*math.exp((g-al)*t)
print(f"  t*={ts:.4f}, q(t*)={q(ts):.6f} (=qmax {qmax}); q(0)={q(0)} inside region")
pm,pp,Lo,Be=0.001,0.01,1000,5
print(f"  worst-case EV of proceeding = B - p+ L = {Be-pp*Lo}; delay preferred iff p+L>B: {pp*Lo>Be}")
