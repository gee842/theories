"""Independent checks for the alignment review of Theory V6.1, Section 6 / S6.
Pure standard library. Written from the statements, not from checks_v61.py."""
import math, random

def hdr(s): print("\n=== " + s)

# ---------- Prop 6.1 ----------
hdr("6.1 faithful: theta* and loss")
def theta_star(eps, b=1.0, d=0.2, c=0.3, n=4):
    return (eps*(b-d)-c)/(eps*(b/(n-1)+d))
print("eps=1:", round(theta_star(1),4), " eps=10 (c fixed):", round(theta_star(10),4))
# c scaling with eps
print("eps=10, c=3:", round((10*0.8-3)/(10*(1/3+0.2)),4))
for d in (0.2,0.1,0.05):
    n=4; c=0.3
    print(f"d={d}: all-racing payoff {-c-n*d:.3f}, theta*={theta_star(1,d=d):.3f}")
# brute-force: check dominance switch at theta*
def dJ(theta, eps=1.0,b=1.0,d=0.2,c=0.3,n=4):
    return eps*b*(1-theta/(n-1)) - c - eps*d*(1+theta)
ts=theta_star(1)
print("dJ just below/above theta*:", round(dJ(ts-1e-6),8)>0, round(dJ(ts+1e-6),8)<0)

# ---------- Prop 6.2 ----------
hdr("6.2 delegate: dominance threshold")
def w(own, others, s):  # r=1; own in {0,1}; others = list of 0/1
    st=[1+s*own]+[1+s*o for o in others]
    return st[0]/sum(st)
def gain_cost(s,k,n=3,psi0=0.01,psi1=0.2,Le=1.0,Lc=1.0):
    others=[1]*k+[0]*(n-1-k)
    g=Le*(w(1,others,s)-w(0,others,s))
    c=Lc*(psi1-psi0)*(1-psi0)**(n-1-k)*(1-psi1)**k
    return g,c
lo,hi=0.0,10.0
for _ in range(100):
    mid=(lo+hi)/2
    ok=all(gain_cost(mid,k)[0]>gain_cost(mid,k)[1] for k in range(3))
    if ok: hi=mid
    else: lo=mid
print("s* =", round(hi,4), " lone delegator win prob =", round(w(1,[0,0],hi),4))

# ---------- Prop 6.4 ----------
hdr("6.4 delegatelock: at-least-one identity, n=2 numbers")
random.seed(7)
neither=both=0; N=100000
for _ in range(N):
    n=random.randint(2,8); s=10**random.uniform(-2,3)
    qL=random.random(); psi0=random.uniform(0,0.2); psi1=random.uniform(psi0,1.0)
    a=(1-psi1)/(1-psi0); A=(1-qL)*a
    alleq = A*(n+(n-1)*s)/n >= 1
    noneq = A*n*(1+s)/(n+s) <= 1
    # direct recomputation from survival formula, p=1
    def Phi(own,k):
        st=[1+s*own]+[1+s]*k+[1.0]*(n-1-k)
        wv=st[0]/sum(st)
        Q=(1-psi1)**(k+own)*(1-psi0)**(n-k-own)
        return (1-qL*own)*Q*wv
    alleq2 = Phi(1,n-1) >= Phi(0,n-1)
    noneq2 = Phi(0,0) >= Phi(1,0)
    assert alleq==alleq2 and noneq==noneq2
    if not alleq and not noneq: neither+=1
    if alleq and noneq: both+=1
print("random draws:",N," neither:",neither," both:",both)
A=0.01*0.95/0.99
print("n=2 all-delegate threshold s >=", round(2/A-2,2), " survival", round(0.01*0.95**2*0.5,5))

# ---------- Prop 6.7 / CI-type numerics, own replicator ----------
hdr("6.7 nested: unilateral safeguard with private vs common benefit")
def replicate(pay_fn, p0=0.5, T=4000, dt=0.05):
    p=p0
    for _ in range(int(T/dt)):
        pa,pb=pay_fn(p)
        p+=dt*p*(1-p)*(pa-pb)
    return p
# safeguard cuts own error 0.20 -> 0.01 at cost 0.01; error cost borne privately (customers) at 1 per unit
priv=replicate(lambda p:(-0.01-0.01, -0.20))
# same safeguard, but the error's cost is common (spread over all, weighted by shares): drop from comparison
def common(p):
    E = p*0.01+(1-p)*0.20  # field error, borne equally by everyone
    return (-0.01-E, -E)
com=replicate(common)
print("share of safeguard, private benefit:", round(priv,4), "; common benefit:", round(com,6))
# heterogeneity: safeguarding developer with an independent advantage a
for adv in (0.005,0.02):
    print(f"safeguard tax 0.01, independent advantage {adv}: final share",
          round(replicate(lambda p:(-0.01+adv,0.0)),4))

# ---------- Bradley-Terry: shared component cancels ----------
hdr("BT translation invariance inside training")
def bt(r1,r2): return 1/(1+math.exp(-(r1-r2)))
q1,q2=1.3,0.4
for h in (0.0,-5.0):  # harm common to both sampled responses (e.g., both comply)
    print(f"shared harm {h}: P(y1>y2)={bt(q1+h,q2+h):.6f}")
# with abstention in the comparison set
print("comply(q=1.3,h=-5) vs abstain(q=0,h=0): P(comply preferred)=", round(bt(1.3-5,0.0),4))

# ---------- Prop 6.8 ----------
hdr("6.8 opaquecorr numbers")
s0=0.9**200
s1=1.0
for t in range(1,201): s1*=(1-0.1*0.01-2**-(t+2))
s1b=1.0
for t in range(0,200): s1b*=(1-0.1*0.01-2**-(t+2))
print("no corrector:",f"{s0:.2e}"," corrector (t=1..200):",round(s1,3)," (t=0..199):",round(s1b,3))
# long-run with constant c_b: residual 0.001 per period not summable
sl=1.0
for t in range(1,20001): sl*=(1-0.001-2**-(t+2))
print("corrector, period 20000:", f"{sl:.2e}", "(constant c_b: not summable)")

# ---------- Prop 6.9 ----------
hdr("6.9 topology: random vs adversarial blind spot")
f,k=0.9,6
print("serial",round(f**k,3)," k checks across gap",round(1-(1-f**k)**k,3),
      " with qcc=.05",round(0.95*(1-(1-f**k)**k),3),
      " m=2",round((1-(0.1)**2)**k,3)," m=3",round((1-(0.1)**3)**k,3))
for rho in (0.0,0.05,0.3):
    print(f"blind spot {rho}: random-hazard catch {(1-rho)*(1-0.1**6):.3f}")
# adversarial placement: attacker knows the blind spot with probability kappa_know
for know in (0.0,0.5,0.9,1.0):
    rho=0.05
    catch = know*0.0 + (1-know)*((1-rho)*(1-0.1**6))
    print(f"attacker knows common blind spot w.p. {know}: catch {catch:.3f}")

# ---------- Remark 6.10 ----------
hdr("6.10 logistic map horizon")
random.seed(3)
def steps(e0,tol=0.1,trials=2000):
    tot=0
    for _ in range(trials):
        x=random.random(); y=x+e0
        n=0
        while abs(x-y)<tol and n<500:
            x=4*x*(1-x); y=4*y*(1-y); n+=1
        tot+=n
    return tot/trials
print("mean steps e=1e-3:",round(steps(1e-3),2)," e=1e-12:",round(steps(1e-12),2))

# ---------- Prop 6.11 ----------
hdr("6.11 homeostasis")
def interior_x(n,s,Le,Lc,psi0,Dpsi):
    q=1-psi0; K=(n-1)*Le/(n*n*Lc); bs=Dpsi/s
    f=lambda x:(x+bs)*(q-x)**(n-1)-K
    # smallest root in (0, min(Dpsi,q/n))
    lo,hi=0.0,min(Dpsi,q/n)
    if f(lo)>0: return 0.0
    if f(hi)<0: return Dpsi  # saturate
    for _ in range(200):
        m=(lo+hi)/2
        if f(m)<0: lo=m
        else: hi=m
    return lo
for D in (0.19,0.05,0.02,0.01,0.005):
    x=interior_x(3,100,1,100,0.01,D)
    print(f"Dpsi={D}: iota={x/D:.3f}, added hazard n*x={3*x:.4f}")
x=interior_x(3,100,1,100,0.01,0.001); print("Dpsi=0.001:",3*x)
# (3): n=3, Le=Lc=1, psi0=0, s_t=2^t, Dpsi_t=2^-t ; own marginal at full delegation
for t in range(3,9):
    s=2**t; D=2**-t
    mg = 2*s/(9*(1+s)) - D*(1-D)**2
    print(f"t={t}: own marginal gain at full delegation {mg:+.4f}")
print("sum_{t>=5} 3*2^-t =", sum(3*2**-t for t in range(5,200)))

# ---------- bounded objective, falling cost (for 'growth is not the danger; the mind is') ----------
hdr("bounded objective vs satisficer as the cost of resources falls")
for c in (0.1,0.01,0.001,1e-6):
    # maximize p(R)-cR with p(R)=1-exp(-R): R*=ln(1/c)
    Rmax=math.log(1/c)
    Rsat=math.log(1/0.05)  # stop at p>=0.95
    print(f"cost {c:g}: bounded maximizer acquires R={Rmax:.2f}; satisficer R={Rsat:.2f}")

# ---------- contest intensity as private cost vanishes (Prop 3.6(1) formula) ----------
hdr("contest: intensity as c -> 0, by self-model")
def e(theta,c,n=4,r=1.0,Om=1.0,l=0.3):
    return r*Om*(n-1-theta)/(n*n*(c+(1+theta)*l))
for th in (-1.0,-0.5,0.0):
    print(f"theta={th}:", [round(e(th,c),3) if c+(1+th)*0.3>0 else 'inf' for c in (1.0,0.1,0.01,0.001)])
