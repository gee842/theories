# S5: where the quasi-static result is optimistic: reversals (E2), a slow human-capacity variable (E4), and the two clocks
# of Theorem 4.12 (E3).  Same field and capacity model as s4_joint.py; exponential integrators.
import math
p,A,chi,Y=0.6,0.3,1.0,1.0
zeta,eps=1.0,0.5
def sig(u): return 1/(1+math.exp(-u)) if u>=0 else math.exp(u)/(1+math.exp(u))
def qs_of(d,gam=1.0): return chi*p*p*Y/(gam*d)
def G_of(d,q): return (A+p*q)/d

# ---------- E2: temporary reform (d raised from d1 to d2 for T, then withdrawn), constant gamma ----------
def fate_E2(d1,d2,T,mode,kap,dt=0.01,Hpost=400.0):
    u=math.log(0.99/0.01); q=qs_of(d1); z=G_of(d1,q); t=0.0
    while True:
        d=d2 if t<T else d1
        qstar=qs_of(d)
        if mode=='QS': q=qstar
        else: q=qstar+(q-qstar)*math.exp(-kap*dt)
        G=G_of(d,q)
        zn=G+(z-G)*math.exp(-eps*d*dt); u+=zeta*(0.5*(z+zn)-1)*dt; z=zn; t+=dt
        if t>T+Hpost or u<-40 or (t>T and u>12 and z>1): break
    return 'undone' if u<0 else 'captured'
def tmin_E2(d1,d2,mode,kap):
    lo,hi=0.0,1.0
    while fate_E2(d1,d2,hi,mode,kap)=='captured':
        hi*=2
        if hi>4000: return float('inf')
    for _ in range(22):
        m=(lo+hi)/2
        if fate_E2(d1,d2,m,mode,kap)=='captured': lo=m
        else: hi=m
    return hi
d1=0.5
print(f"E2. Captured evaluation domain at d1={d1} (G={G_of(d1,qs_of(d1)):.3f}); reform raises d to d2 for T, then withdraws.")
print(f"    QS certificate restored for d2>0.638; with capacity frozen at its old level, only for d2>{(A+p*qs_of(d1)):.3f}")
for d2 in (0.7,1.0,2.0):
    row=[f"QS: {tmin_E2(d1,d2,'QS',None):.2f}"]+[f"R({k}): {tmin_E2(d1,d2,'R',k):.2f}" for k in (1.0,0.3,0.1,0.03)]
    print(f"   d2={d2}: minimal hold T (time units): "+"  ".join(row))

# ---------- E4: human capacity M as a slow variable of correction ----------
# M' = -delta_h D M + rho_h (1-D)(1-M);  effective correction d_eff = d * (M/M0)^w, M0 = M_eq(D0).
# (a) exogenous delegation rising to 1: rate-law threshold with trends (gamma, d) as in s4.
# (b) capture -> masking -> delegation looks safe: D = D0 + kD x_ev ; constant gamma and d; hysteresis in d.
def Meq(D,dh,rh): return rh*(1-D)/(dh*D+rh*(1-D))
def run_E4a(acor,dh,rh,w=1.0,H=600.0,dt=0.01,couple=True):
    actl,d0=0.2,2.0; D0=0.2; M0=Meq(D0,dh,rh); M=M0
    u=math.log(0.01/0.99); t=0.0
    d=d0; qst=chi*p*p*Y/d; z=G_of(d,qst)
    while t<H:
        D=1-(1-D0)*math.exp(-0.1*t)
        M=M+dt*(-dh*D*M+rh*(1-D)*(1-M))
        dn=d0*math.exp(acor*t)*((M/M0)**w if couple else 1.0)
        gam=math.exp(-actl*t); q=chi*p*p*Y/(gam*dn)
        G=G_of(dn,q)
        zn=G+(z-G)*math.exp(-eps*dn*dt); u+=zeta*(0.5*(z+zn)-1)*dt; z=zn; t+=dt
        if u>0: return t
    return None
def crit_E4a(dh,rh,couple):
    lo,hi=0.0,0.4
    for _ in range(16):
        m=(lo+hi)/2
        if run_E4a(m,dh,rh,couple=couple) is not None: lo=m
        else: hi=m
    return lo
print("E4a. Delegation D(t)=1-0.8 e^{-0.1t}; correction needs human capacity, d_eff=d*M/M0; largest alpha_cor with capture by t=600")
for dh,rh in ((0.05,0.05),(0.1,0.05),(0.2,0.1)):
    print(f"   delta_h={dh}, rho_h={rh}: uncoupled {crit_E4a(dh,rh,False):.4f}; coupled {crit_E4a(dh,rh,True):.4f}  (rate law 0.1; shifted law 0.1+delta_h={0.1+dh:.2f})")

def run_E4b(d,x0,dh,rh,kD,D0=0.1,w=0.5,H=1500.0,dt=0.01,M_init=None):
    M0=Meq(D0,dh,rh)
    u=math.log(x0/(1-x0)); M=M0 if M_init is None else M_init
    deff=d*(M/M0)**w; z=G_of(deff,qs_of(deff))*x0 if x0<0.5 else G_of(deff,qs_of(deff)); t=0.0
    while t<H:
        x=sig(u); D=min(1.0,D0+kD*x)
        M=M+dt*(-dh*D*M+rh*(1-D)*(1-M))
        deff=d*(M/M0)**w; G=G_of(deff,qs_of(deff))   # capacity quasi-static on purpose: isolates the M loop
        b=G*x*deff  # z' = eps(b x - deff z) with b = G deff: field model with conversion from x itself
        zt=b/deff
        zn=zt+(z-zt)*math.exp(-eps*deff*dt); u+=zeta*(0.5*(z+zn)-1)*dt; z=zn; t+=dt
        if u<-40: return 'absent'
        if u>15 and t>200: return 'captured'
    return 'captured' if u>0 else 'absent'
print("E4b. Capture-delegation loop (D=0.1+kD*x_ev, delta_h=0.2, rho_h=0.05, d_eff=d*(M/M0)^0.5), constant gamma; one-domain field")
print("     Smallest permanent d that undoes capture from the captured state (QS certificate without M: G<1 at d>0.638)")
for kD in (0.0,0.3,0.6):
    dh,rh=0.2,0.05
    # captured state: M at its captured equilibrium
    Mc=Meq(min(1.0,0.1+kD*0.99),dh,rh)
    lo,hi=0.3,20.0
    for _ in range(30):
        m=(lo+hi)/2
        if run_E4b(m,0.99,dh,rh,kD,M_init=Mc)=='captured': lo=m
        else: hi=m
    print(f"   kD={kD}: d needed = {hi:.3f}  (captured-state M/M0 = {Mc/Meq(0.1,dh,rh):.3f})")

# ---------- E3: the two clocks of Theorem 4.12, with capture timing endogenous ----------
import importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location("s4","s4_joint.py"); s4=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(s4)
def E3(mode,par,acor=0.05,rho=0.05,hV=0.08,sP=0.12,P0=0.05,Va=0.6,Vm=0.3,m_in=0.5,m_out=0.05,dt=0.01,H=200):
    # host loaded by a race carrier with share P growing by replicator; alarm on masked reports; evaluation capture from s4 model
    V=1.0; P=P0; t=0.0
    u=math.log(0.01/0.99); q=s4.q0; z=(s4.A+s4.p*s4.q0)/s4.d0
    while t<H:
        tm=t+dt/2; d=s4.dd(tm,acor); qst=s4.qstar(tm,acor)
        if mode=='QS': qq=qst
        else:
            k=s4.qrate(mode,par,tm,q); qn=qst+(q-qst)*math.exp(-k*dt); qq=0.5*(q+qn); q=qn
        G=(s4.A+s4.p*qq)/d; zn=G+(z-G)*math.exp(-s4.eps*d*dt); u+=s4.zeta*(0.5*(z+zn)-1)*dt; z=zn
        x=sig(u); m=x*m_in+(1-x)*m_out
        P+=dt*sP*P*(1-P); E=P
        V+=dt*V*(rho*(1-V)-hV*E)
        t+=dt
        if V+m*(1-V)<=Va: return f"alarm at t={t:.1f} with V={V:.3f} ({'before' if V>=Vm else 'AFTER'} the floor); x_ev={x:.2f}"
        if V<Vm-0.1: return f"no alarm; V={V:.3f} at t={t:.1f}; x_ev={x:.2f}"
    return "none"
print("E3. Theorem 4.12's two clocks with capture endogenous (alpha_cor=0.05; m_in=0.5>m_fl=0.43; floor 0.3, alarm 0.6)")
print(f"   independent evaluation (x_ev=0): {E3('QS',None,m_in=0.05)}")
for m,par in (('QS',None),('R',1.0),('R',0.1),('R',0.03),('GA',1.0)):
    print(f"   {m}{'' if par is None else '('+str(par)+')'}: {E3(m,par)}")
