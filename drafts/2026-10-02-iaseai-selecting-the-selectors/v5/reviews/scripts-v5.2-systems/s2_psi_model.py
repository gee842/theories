"""S2. A minimal dynamical model of Psi as a meta-attractor in the space of governing models.

 psi : share of consequential decision positions governed by Psi (fast-ish)
 z   : institutional embodiment of Psi (decisiveness r, appropriability chi, winner-take-all
       prizes, dominance-route status); a slow variable written by those in power.

 Relative advantage of Psi-conduct for an actor:
   Delta = (1-beta)*nu_g - c_u + a*z - k*(1-psi)
     (1-beta)nu_g - c_u : net contested gain after prize sharing (Prop 1.5(2))
     a z                : performativity: institutions built under Psi make winning pay
     -k(1-psi)          : self-confirmation / attribution: where few hold Psi, reciprocal
                          cooperators exclude Psi-holders; where many do, restraint is exploited
 Heterogeneous actors (logistic thresholds, scale s; Granovetter 1978):
   psi' = zeta*(F(Delta/s) - psi),  z' = eps*(b*psi - d*z)
 Equilibria: z = b psi/d, psi = F(((1-beta)nu_g - c_u - k + (ab/d + k) psi)/s).
"""
import math, random

def F(u):
    if u > 50: return 1.0
    if u < -50: return 0.0
    return 1.0/(1.0+math.exp(-u))

P = dict(nu_g=2.0, c_u=0.6, a=1.0, b=0.4, d=1.0, k=0.4, s=0.1, zeta=1.0)

def g(psi, beta, p):
    D = (1-beta)*p['nu_g'] - p['c_u'] - p['k'] + (p['a']*p['b']/p['d'] + p['k'])*psi
    return F(D/p['s']) - psi

def equilibria(beta, p, N=4000):
    roots = []
    prev = g(0.0, beta, p)
    for i in range(1, N+1):
        x = i/N
        cur = g(x, beta, p)
        if prev == 0 or prev*cur < 0:
            lo, hi = (i-1)/N, x
            for _ in range(60):
                mid = 0.5*(lo+hi)
                if g(lo, beta, p)*g(mid, beta, p) <= 0: hi = mid
                else: lo = mid
            roots.append(0.5*(lo+hi))
        prev = cur
    return roots

def sim(psi, z, beta_fn, p, eps, T, dt=0.02, noise=0.0, rng=None, record_every=0):
    t = 0.0; out = []
    n = int(T/dt)
    for i in range(n):
        beta = beta_fn(t)
        D = (1-beta)*p['nu_g'] - p['c_u'] + p['a']*z - p['k']*(1-psi)
        dpsi = p['zeta']*(F(D/p['s']) - psi)
        dz = eps*(p['b']*psi - p['d']*z)
        psi += dt*dpsi
        if noise > 0:
            psi += noise*math.sqrt(dt)*rng.gauss(0, 1)
        psi = min(max(psi, 0.0), 1.0)
        z += dt*dz
        t += dt
        if record_every and i % record_every == 0:
            out.append((t, psi, z, beta))
    return psi, z, out

print("== S2a: equilibria of psi vs prize-sharing beta (k=0.4, ab/d=0.4). Without k and a: threshold 1-c_u/nu_g=0.7")
bist = []
for i in range(0, 101, 5):
    beta = i/100
    r = equilibria(beta, P)
    print(f"  beta={beta:4.2f}  equilibria psi={['%.3f' % x for x in r]}")
    if len(r) == 3: bist.append(beta)
print(f"  bistable for beta in approx [{min(bist):.2f}, {max(bist):.2f}] on this grid")

# fine search of fold points
def nroots(beta): return len(equilibria(beta, P, 3000))
lo_f = None; hi_f = None
prev = nroots(0.0)
for i in range(1, 1001):
    beta = i/1000; n = nroots(beta)
    if prev == 1 and n == 3 and lo_f is None: lo_f = beta
    if prev == 3 and n == 1: hi_f = beta
    prev = n
print(f"  fold points: beta_lo ~ {lo_f}, beta_hi ~ {hi_f}")

print("== S2b: quasi-static sweep (hysteresis). eps=0.1")
psi, z = 0.95, 0.38
up = []
for i in range(0, 101, 5):
    beta = i/100
    psi, z, _ = sim(psi, z, lambda t, b=beta: b, P, 0.1, 300)
    up.append((beta, psi))
down = []
for i in range(100, -1, -5):
    beta = i/100
    psi, z, _ = sim(psi, z, lambda t, b=beta: b, P, 0.1, 300)
    down.append((beta, psi))
print("  beta   psi(up)  psi(down)")
dd = dict(down)
for beta, pu in up:
    print(f"  {beta:4.2f}   {pu:.3f}    {dd[beta]:.3f}")

print("== S2c: temporary sharing pulse. Baseline beta0 inside the bistable band; pulse beta=0.97 for Tp,")
print("   then back to beta0. Minimal Tp for a lasting exit from the Psi state, vs eps (slow z).")
beta0 = 0.5*(lo_f + hi_f)
r0 = equilibria(beta0, P)
print(f"  beta0={beta0:.3f}, equilibria at beta0: {['%.3f' % x for x in r0]}")
psi_hi = max(r0); z_hi = P['b']*psi_hi/P['d']
for eps in [1.0, 0.3, 0.1, 0.03]:
    def lasting(Tp):
        psi, z, _ = sim(psi_hi, z_hi, lambda t: 0.97 if t < Tp else beta0, P, eps, Tp + 60/eps + 200)
        return psi < 0.5
    lo, hi = 0.0, 200/eps
    if not lasting(hi):
        print(f"  eps={eps}: no lasting exit"); continue
    for _ in range(25):
        mid = 0.5*(lo+hi)
        if lasting(mid): hi = mid
        else: lo = mid
    print(f"  eps={eps:5.2f}: Tp_min={hi:8.2f}  (= {hi*eps*P['d']:.2f} x 1/(eps d))")

print("== S2d: which feedback creates the hysteresis? bistable band in beta for four variants")
for lab, kk, aa in [("neither (pure Prop 1.5)", 0.0, 0.0), ("self-confirmation only k=0.4", 0.4, 0.0),
                    ("performativity only ab/d=0.4", 0.0, 1.0), ("both", 0.4, 1.0)]:
    Q = dict(P); Q['k'] = kk; Q['a'] = aa
    band = [i/200 for i in range(0, 201) if len(equilibria(i/200, Q, 1500)) == 3]
    one = [i/200 for i in range(0, 201) if len(equilibria(i/200, Q, 1500)) == 1]
    if band:
        print(f"  {lab:32s}: bistable beta in [{min(band):.3f}, {max(band):.3f}]")
    else:
        # locate where psi* crosses 0.5
        cross = None
        for i in range(0, 201):
            r = equilibria(i/200, Q, 1500)
            if r and r[0] < 0.5: cross = i/200; break
        print(f"  {lab:32s}: monostable everywhere; psi* < 0.5 from beta ~ {cross}")

print("== S2e: critical slowing down. Noise on psi; beta ramped slowly from 0.0 toward beta_hi.")
print("   Rolling lag-1 autocorrelation and variance of detrended psi in windows.")
rng = random.Random(7)
eps = 0.1
Tr = 3000.0
ramp = lambda t: 0.0 + (hi_f - 0.01)*min(t/Tr, 1.0)
psi, z, rec = sim(0.95, 0.38, ramp, P, eps, Tr, dt=0.02, noise=0.004, rng=rng, record_every=50)
xs = [r[1] for r in rec]; ts = [r[0] for r in rec]; bs = [r[3] for r in rec]
W = len(xs)//6
def stats(seg):
    m = len(seg); tt = list(range(m))
    mt = sum(tt)/m; ms = sum(seg)/m
    sl = sum((tt[i]-mt)*(seg[i]-ms) for i in range(m))/sum((tt[i]-mt)**2 for i in range(m))
    res = [seg[i] - (ms + sl*(tt[i]-mt)) for i in range(m)]
    v = sum(r*r for r in res)/m
    ac = sum(res[i]*res[i+1] for i in range(m-1))/sum(r*r for r in res)
    return ac, v
for j in range(6):
    seg = xs[j*W:(j+1)*W]
    ac, v = stats(seg)
    print(f"  window {j+1}: beta {bs[j*W]:.3f}-{bs[(j+1)*W-1]:.3f}  mean psi={sum(seg)/len(seg):.3f}  AR1={ac:.3f}  var={v:.2e}")

print("== S2f: analytic recovery rate of psi near the Psi-state vs beta (eps=0.1)")
for beta in [0.0, 0.2, 0.3, 0.35, 0.38, hi_f - 0.005]:
    r = equilibria(beta, P)
    ps = max(r)
    h = 1e-6
    # Jacobian of (psi,z) system at (ps, b ps/d)
    zz = P['b']*ps/P['d']
    def Dlt(psi, z): return (1-beta)*P['nu_g'] - P['c_u'] + P['a']*z - P['k']*(1-psi)
    def f1(psi, z): return P['zeta']*(F(Dlt(psi, z)/P['s']) - psi)
    def f2(psi, z): return eps*(P['b']*psi - P['d']*z)
    J11 = (f1(ps+h, zz)-f1(ps-h, zz))/(2*h); J12 = (f1(ps, zz+h)-f1(ps, zz-h))/(2*h)
    J21 = (f2(ps+h, zz)-f2(ps-h, zz))/(2*h); J22 = (f2(ps, zz+h)-f2(ps, zz-h))/(2*h)
    tr = J11+J22; det = J11*J22-J12*J21
    disc = tr*tr-4*det
    if disc >= 0:
        ev = max((tr+math.sqrt(disc))/2, (tr-math.sqrt(disc))/2)
    else:
        ev = tr/2
    print(f"  beta={beta:.3f}: psi*={ps:.3f}, leading eigenvalue={ev:+.4f}")
