"""Additional checks for v3.1 (pure Python). Appends to checks.log."""
import math, os
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

# 1. Prop 2 brute force on both branches
def u_k(ek, others, n, lam, nu, omega, K, h, rho):
    es = [ek]+others; E = sum(es)/n; V = K*(1-h*E/rho)
    pis = [nu*e + omega*V for e in es]
    return pis[0] + lam*(pis[0]-sum(pis)/n)
mism = 0; cases = 0
for theta in (0.5, 3.0, 8.0):
    for n in (2, 3, 4, 5, 10):
        for lam in (0, 0.5, 1, 2, 6, 10):
            nu, omega, K, rho = 1.0, 1.0, 1.0, 1.0
            h = theta*rho*nu/(omega*K)   # theta = omega K h/(rho nu)
            ebar = 0.9*rho/h if h > 0 else 1.0   # keep h*ebar < rho
            for others in ([0.0]*(n-1), [ebar]*(n-1)):
                best = max((u_k(ebar*e/10, others, n, lam, nu, omega, K, h, rho), ebar*e/10) for e in range(11))[1]
                w = 1+lam*(n-1)/n
                pred = ebar if w > theta/n else 0.0
                cases += 1
                if abs(w-theta/n) > 1e-12 and abs(best-pred) > 1e-9: mism += 1
say(f"Prop 2 brute force over theta in (0.5,3,8): {cases} cases, {mism} mismatches")

# 2. repeated game cutoff
def deltastar(theta, n, lam):
    w = 1+lam*(n-1)/n; a = w-theta/n
    return a/(a+theta-1) if a > 0 else 0.0
for lam in (0, 2, 50):
    say(f"Repeated game theta=3 n=4 lambda={lam}: delta*={deltastar(3,4,lam):.3f}")
# brute check of one-shot deviation inequality
th, n, lam = 3.0, 4, 2.0
nu=omega=K=rho=1.0; h=th*rho*nu/(omega*K); eb=0.9*rho/h
uc = u_k(0.0,[0.0]*(n-1),n,lam,nu,omega,K,h,rho)
ud = u_k(eb,[0.0]*(n-1),n,lam,nu,omega,K,h,rho)
uN = u_k(eb,[eb]*(n-1),n,lam,nu,omega,K,h,rho)
dnum = (ud-uc)/(ud-uN)
say(f"  direct one-shot deviation cutoff (ud-uc)/(ud-uN)={dnum:.3f} vs formula {deltastar(th,n,lam):.3f}")

# 3. rate law generalised
def sE(d, gam, eta, A=0.3, Bh=0.5, chi=0.8, Yh=1.0, cE=1.0, short=False):
    if short:
        q = (chi*Yh/gam)**(1/eta)        # return independent of d
    else:
        q = (chi*Yh/(gam*d))**(1/eta)
    return A/(cE*d) + q*Bh/(cE*d)
def dstar(gam, eta, short=False):
    lo, hi = 1e-9, 1e300
    for _ in range(400):
        mid = math.sqrt(lo*hi)
        if sE(mid, gam, eta, short=short) > 1: lo = mid
        else: hi = mid
    return hi
g = 0.2
for eta in (0.5, 1.0, 2.0, 3.0):
    for short in (False, True):
        t1, t2 = 60.0, 80.0
        rate = (math.log(dstar(math.exp(-g*t2), eta, short)) - math.log(dstar(math.exp(-g*t1), eta, short)))/(t2-t1)
        pred = g/eta if short else g/(1+eta)
        say(f"  eta={eta} {'short' if short else 'long '} horizon: asymptotic growth of d* = {rate:.4f}, predicted {pred:.4f}")
# dichotomy: alpha >= g/(1+eta) and d0 > d*(0) keeps the certificate
for eta in (1.0, 2.0):
    a_c = g/(1+eta); d0 = dstar(1.0, eta)*1.02
    worst = max(sE(d0*math.exp(a_c*t), math.exp(-g*t), eta) for t in range(0, 400))
    say(f"  eta={eta}: alpha=g/(1+eta), d0=1.02 d*(0): max s_E over t in [0,400) = {worst:.4f} (<1 expected)")
# fixed cost f>0 saturation
def sE_f(d, gam, f, A=0.3, Bh=0.5, chi=0.8, Yh=1.0):
    q = max(0.0, chi*Yh/d - f)/gam
    return A/d + q*Bh/d
for f in (0.0, 0.1):
    reqs = []
    for t in (0, 20, 50, 100, 200):
        gam = math.exp(-g*t); lo, hi = 1e-9, 1e12
        for _ in range(200):
            mid = math.sqrt(lo*hi)
            if sE_f(mid, gam, f) > 1: lo = mid
            else: hi = mid
        reqs.append(round(hi, 2))
    say(f"  fixed cost f={f}: required d at t=0,20,50,100,200: {reqs}")
# two rates: alpha = b + g_c; capture requires g > (1+eta)(b+g_c)
say(f"  two rates (eta=1): g=0.2, g_c=0.2, b=0 -> alpha=0.2 >= g/2=0.1: correction keeps pace")

# 4. order of events: lower bound T_A on time to reach the alarm level
rho, h, K, V0, Va = 0.05, 0.08, 1.0, 1.0, 0.6
# use ebar with h*ebar<rho for the closed form
for eb in (0.5,):
    r = rho-h*eb; Vs = K*(1-h*eb/rho)
    TA = math.log((1-Vs/V0)/(1-Vs/Va))/r
    V = V0; t = 0.0; dt = 0.001
    while V > Va: V += dt*V*(rho*(1-V/K)-h*eb); t += dt
    say(f"T_A bound (ebar={eb}): formula {TA:.2f}, simulated with E=ebar {t:.2f}")

# 5. fragmentation factor k^2
for k in (1, 2, 4):
    total = k*(1/k)**2*(1/k)
    say(f"fragmentation k={k}: cultivated conversion factor {total:.4f} (=1/k^2)")

# 6. sufficiency transient (math-check counterexample)
rho, h, K, Vmin, nu = 0.05, 0.08, 1.0, 0.3, 0.08
tau = 2*nu
for p0, V0 in ((0.99, 1.0), (0.5, 1.0), (0.1, 1.0)):
    p = p0; V = V0; vmin = V; dt = 0.01
    for i in range(int(400/dt)):
        E = p
        V += dt*V*(rho*(1-V/K)-h*E)
        p += dt*p*(1-p)*(nu-tau)*1.0
        vmin = min(vmin, V)
    say(f"liability tau=2nu from t=0, race share {p0}: min V = {vmin:.3f} (floor 0.3), final V = {V:.3f}")
open(os.path.join(here, "checks.log"), "a").write("\n--- v3.1 checks ---\n" + "\n".join(log) + "\n")
