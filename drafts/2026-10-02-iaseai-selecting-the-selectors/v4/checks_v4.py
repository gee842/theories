"""Checks for the v4 theory (pure Python, no dependencies). Writes checks_v4.log.

Each block checks one formal claim of THEORY.md by direct computation:
  P1  contest with objective m_i + theta * mean(m_-i): closed-form equilibrium,
      true welfare monotone in theta, the selected objective theta = -1
  P3  dissipation and overdissipation with shared risk
  P4  delegation: dominance threshold and the prisoner's dilemma
  L1  delay bound (Hayes): x' = a x - k x(t - tau) is stabilizable iff a*tau < 1
  P6  preventive war condition (Fearon commitment problem)
  P8  assurance: verification, sanctions, trust threshold, risk dominance
  L2  Crawford-Sobel: informative communication iff bias < 1/4
"""
import math, os, cmath
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

def golden_max(f, lo, hi, tol=1e-12, it=300):
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(it):
        if fc > fd: b, d, fd = d, c, fc; c = b - g * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + g * (b - a); fd = f(d)
        if b - a < tol: break
    return (a + b) / 2

# ---------------------------------------------------------------- P1, P3
say("== P1/P3: contest with objective m_i + theta*mean(m_-i) ==")
def m_i(i, e, V, r, c, rhoL):
    s = sum(x ** r for x in e)
    p = (e[i] ** r / s) if s > 0 else 1 / len(e)
    return V * p - c * e[i] - rhoL * sum(e)
def objective(i, e, theta, V, r, c, rhoL):
    n = len(e)
    others = [m_i(j, e, V, r, c, rhoL) for j in range(n) if j != i]
    return m_i(i, e, V, r, c, rhoL) + theta * sum(others) / (n - 1)
def e_formula(theta, n, V, r, c, rhoL):
    return r * V * (n - 1 - theta) / (n * n * (c + (1 + theta) * rhoL))
worst = 0.0
for n in (2, 3, 5):
    for r in (0.5, 1.0, n / (n - 1)):
        for theta in (-1.0, -0.5, 0.0, 0.5, n - 1 - 0.5):
            V, c, rhoL = 1.0, 1.0, 0.3
            ef = e_formula(theta, n, V, r, c, rhoL)
            # best response of actor 0 to others at ef: must return ef
            def f(x):
                e = [x] + [ef] * (n - 1)
                return objective(0, e, theta, V, r, c, rhoL)
            br = golden_max(f, 0.0, 5 * max(ef, 1e-3) + 1.0)
            worst = max(worst, abs(br - ef) / max(ef, 1e-9))
say("max relative gap between numerical best response and closed form:", f"{worst:.2e}")
# true welfare monotone in common theta
n, V, r, c, rhoL, kappa = 4, 1.0, 1.0, 1.0, 0.3, 0.4
ths = [-1 + 0.25 * k for k in range(int((n - 1 + 1) / 0.25))]
Ws = []
for th in ths:
    e = e_formula(th, n, V, r, c, rhoL)
    Ws.append((1 + kappa) * (V / n - c * e - rhoL * n * e))
say("true welfare at common theta -1..n-1 (n=4, r=1, rhoL=0.3, kappa=0.4):",
    " ".join(f"{w:.3f}" for w in Ws))
say("monotone increasing:", all(Ws[k + 1] > Ws[k] for k in range(len(Ws) - 1)))
# selected objective theta=-1: effort rV/(nc), shared risk cancels
for rhoL in (0.0, 0.3, 3.0):
    e = e_formula(-1, n, V, r, c, rhoL)
    say(f"theta=-1, rhoL={rhoL}: e={e:.4f} (rV/(nc)={r*V/(n*c):.4f});",
        f"material payoff each={V/n - c*e - rhoL*n*e:.4f} vs joint restraint {V/n:.4f}")
# unilateral misspecification: given others' efforts, acting on theta<kappa lowers own true welfare
n, kappa, rhoL = 4, 0.4, 0.3
eo = e_formula(kappa, n, V, r, c, rhoL)
def true_W(x):
    e = [x] + [eo] * (n - 1)
    return objective(0, e, kappa, V, r, c, rhoL)
for th in (kappa, 0.0, -1.0):
    def f(x):
        e = [x] + [eo] * (n - 1)
        return objective(0, e, th, V, r, c, rhoL)
    x = golden_max(f, 0, 5)
    say(f"acting on theta={th:+.1f} against others at the kappa-equilibrium: own effort {x:.4f}, own true welfare {true_W(x):.5f}")
# P3 closed form for loss relative to joint restraint at theta=0
say("P3 loss per actor at theta=0 relative to joint restraint, as a fraction of V/n:")
for n in (2, 4):
    for r in (0.5, 1.0, n / (n - 1)):
        for rhoL in (0.0, 0.3, 3.0):
            e = e_formula(0, n, V, r, c, rhoL)
            frac = e * (c + n * rhoL) / (V / n)
            pred = r * (n - 1) * (c + n * rhoL) / (n * (c + rhoL))
            say(f"  n={n} r={r:.2f} rhoL={rhoL}: {frac:.4f} (formula {pred:.4f})")

# ---------------------------------------------------------------- P4
say("\n== P4: delegation ==")
def pdel(di, k, n, a, r):
    s_i = (1 + a * di) ** r
    tot = s_i + k * (1 + a) ** r + (n - 1 - k)
    return s_i / tot
def gain_cost(k, n, a, r, Le, Lc, h0, h1):
    gain = Le * (pdel(1, k, n, a, r) - pdel(0, k, n, a, r))
    cost = Lc * (h1 - h0) * (1 - h0) ** (n - 1 - k) * (1 - h1) ** k
    return gain, cost
n, r, Le, Lc, h0, h1 = 3, 1.0, 1.0, 1.0, 0.01, 0.2   # Delta h = 0.19 < 1/n
for a in (0.1, 0.5, 2, 10, 100):
    rows = [gain_cost(k, n, a, r, Le, Lc, h0, h1) for k in range(n)]
    dom = all(g > cst for g, cst in rows)
    say(f"a={a}: gain-cost by k others delegating:", " ".join(f"{g-cst:+.3f}" for g, cst in rows), "| dominant:", dom)
# threshold a*: smallest a with dominance
lo, hi = 0.0, 1e6
for _ in range(200):
    mid = (lo + hi) / 2
    dom = all(g > cst for g, cst in (gain_cost(k, n, mid, r, Le, Lc, h0, h1) for k in range(n)))
    lo, hi = (lo, mid) if dom else (mid, hi)
say(f"dominance threshold a* = {hi:.4f} (n=3, r=1, Le=Lc, h0=0.01, h1=0.2)")
say("limit gain at k=n-1 as a->inf equals Le/n:", f"{gain_cost(n-1, n, 1e9, r, Le, Lc, h0, h1)[0]:.4f}", "vs", f"{Le/n:.4f}")
allD = Le / n - Lc * (1 - (1 - h1) ** n)
noneD = Le / n - Lc * (1 - (1 - h0) ** n)
say(f"payoff when all delegate {allD:.4f} < none delegate {noneD:.4f}:", allD < noneD)
# Delta h above Le/n: no dominance even as a -> inf
rows = [gain_cost(k, n, 1e9, r, Le, Lc, 0.01, 0.5) for k in range(n)]
say("with Delta h = 0.49 > 1/n, gain-cost at a->inf:", " ".join(f"{g-cst:+.3f}" for g, cst in rows))
# relative objective: shared control loss cancels -> delegate whenever gain>0
say("under relative objectives the shared loss term cancels: delegation chosen for every a>0 (gain>0):",
    all(gain_cost(k, n, 0.01, r, Le, Lc, h0, h1)[0] > 0 for k in range(n)))

# ---------------------------------------------------------------- L1 Hayes
say("\n== L1: delay bound for x' = a x - k x(t - tau) ==")
def simulate(a, k, tau, T=200.0, dt=0.001):
    lag = int(round(tau / dt)); buf = [1.0] * (lag + 1); x = 1.0
    peak_late = 0.0; steps = int(T / dt)
    for s in range(steps):
        xd = buf[-lag - 1] if lag > 0 else x
        x = x + dt * (a * x - k * xd); buf.append(x)
        if len(buf) > lag + 2: buf.pop(0)
        if s > steps * 0.8: peak_late = max(peak_late, abs(x))
        if abs(x) > 1e12: return float("inf")
    return peak_late
def hayes_kmax(a, tau):
    # omega in (0, pi) solving omega = a*tau*tan(omega); omega = pi/2 when a = 0
    if a == 0: return math.pi / (2 * tau)
    lo, hi = 1e-9, math.pi - 1e-9
    g = lambda w: w - a * tau * math.tan(w)
    # for 0 < a*tau < 1 the root lies in (0, pi/2); for a < 0 in (pi/2, pi)
    lo, hi = (1e-9, math.pi / 2 - 1e-12) if a > 0 else (math.pi / 2 + 1e-12, math.pi - 1e-12)
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(lo) * g(mid) <= 0: hi = mid
        else: lo = mid
    w = (lo + hi) / 2
    return math.sqrt(a * a + (w / tau) ** 2)
tau = 1.0
for a in (0.5, 0.9, 1.1, 2.0):
    if a * tau < 1:
        kmax = hayes_kmax(a, tau); kmid = (a + kmax) / 2
        say(f"a*tau={a*tau}: Hayes window k in ({a:.3f}, {kmax:.3f}); simulate k={kmid:.3f}: late |x| = {simulate(a, kmid, tau):.2e}")
    else:
        best = min(simulate(a, k, tau, T=100.0) for k in [a * f for f in (0.5, 0.8, 1.0, 1.05, 1.2, 1.5, 2.0, 3.0)])
        say(f"a*tau={a*tau}: smallest late |x| over a grid of k = {best:.2e} (no stabilizing gain)")

# ---------------------------------------------------------------- P6 Fearon
say("\n== P6: preventive war ==")
def war_now(p1, p2, cA, delta):
    war = (p1 - cA) / (1 - delta)
    peace = 1 + delta * max(p2 - cA, 0) / (1 - delta)
    return war > peace
def cond(p1, p2, cA, delta):
    if p2 >= cA: return p1 - p2 > (1 - delta) * (1 + cA - p2)
    return p1 > cA + (1 - delta)
mism = 0; ncases = 0
for p1 in [x / 20 for x in range(1, 20)]:
    for p2 in [x / 20 for x in range(0, 20)]:
        if p2 > p1: continue
        for cA in (0.05, 0.2, 0.5):
            for delta in (0.3, 0.6, 0.9, 0.99):
                ncases += 1
                if war_now(p1, p2, cA, delta) != cond(p1, p2, cA, delta):
                    w = (p1 - cA) / (1 - delta); pc = 1 + delta * max(p2 - cA, 0) / (1 - delta)
                    if abs(w - pc) > 1e-9: mism += 1   # count only non-ties
say(f"closed-form condition vs direct comparison over {ncases} cases, mismatches:", mism)
for cA in (0.05, 0.2):
    for delta in (0.5, 0.8, 0.95, 0.99):
        say(f"parity p1=0.5, decisive shift p2=0, war cost cA={cA}, delta={delta}: preventive war rational:", war_now(0.5, 0.0, cA, delta))
for p2 in (0.45, 0.4, 0.3):
    say(f"gradual shift 0.5 -> {p2}, cA=0.05, delta=0.8: preventive war rational:", war_now(0.5, p2, 0.05, 0.8))

# ---------------------------------------------------------------- P8 assurance
say("\n== P8: assurance ==")
def coop_br(p, R, S, T, P, q, F):
    Tq = q * (P - F) + (1 - q) * T; Sq = q * P + (1 - q) * S
    return p * R + (1 - p) * Sq >= p * Tq + (1 - p) * P
def pstar(R, S, T, P, q, F):
    Tq = q * (P - F) + (1 - q) * T
    if R < Tq: return float("inf")
    if R == Tq: return 1.0          # cooperation only under certainty (a tie)
    return (1 - q) * (P - S) / ((R - Tq) + (1 - q) * (P - S))
mism = 0
for R, S, T, P in ((3, 0, 2, 1), (3, -5, 2.5, 1), (3, 0, 5, 1), (3, -10, 10, 1)):
    for q in (0, 0.5, 0.9, 0.99):
        for F in (0, 2):
            ps = pstar(R, S, T, P, q, F)
            for p in [x / 100 for x in range(101)]:
                if coop_br(p, R, S, T, P, q, F) != (p >= ps - 1e-12) and abs(p - ps) > 1e-9: mism += 1
say("threshold formula vs direct best response (4 payoff sets x 4 q x 2 F x 101 beliefs), mismatches:", mism)
R, S, P = 3, -5, 1
for T in (2.5, 4, 10, 100):
    qmin = max(0.0, (T - R) / (T - P + 0))
    say(f"T={T}: minimal verification for cooperation to be possible (F=0): q > {qmin:.3f};",
        "trust needed at q=0:", "impossible" if pstar(R, S, T, P, 0, 0) == float('inf') else f"{pstar(R,S,T,P,0,0):.3f}",
        "| at q=0.9:", "impossible" if pstar(R, S, T, P, 0.9, 0) == float('inf') else f"{pstar(R,S,T,P,0.9,0):.3f}")
say("risk dominance of (C,C) iff R-T > P-S; p* < 1/2 iff the same (q=0):",
    all((pstar(3, S, T, 1, 0, 0) < 0.5) == (3 - T > 1 - S) for S in (-3, -1, 0, 0.5) for T in (1.5, 2, 2.5)))

# ---------------------------------------------------------------- L2 Crawford-Sobel
say("\n== L2: Crawford-Sobel ==")
def N_max(b):
    if b <= 0: return float("inf")
    N = 1
    while 2 * (N + 1) * N * b < 1: N += 1
    return N
for b in (0.01, 0.05, 0.1, 0.2, 0.249, 0.25, 0.4):
    say(f"bias b={b}: most informative equilibrium has {N_max(b)} message(s)")

# ---------------------------------------------------------------- repairs of v3.1 (review R1, R2, R4)
say("\n== Repairs: Proposition 1(3)-(4), Theorem 1 C1 (review R1) ==")
def run_field(tau_eff_fn, T=2000.0, dt=0.02, p0=0.1, nu=1.0, rho=0.05, h=0.08, K=1.0, Vmin=0.3):
    # classical RK4 on (p, V); loads e in {0, 1}, equal phi
    def f(t, p, V):
        return p * (1 - p) * (nu - tau_eff_fn(t)), V * (rho * (1 - V / K) - h * p)
    p, V, t, minV, cross = p0, 1.0, 0.0, 1.0, None
    while t < T:
        k1 = f(t, p, V); k2 = f(t + dt/2, p + dt/2*k1[0], V + dt/2*k1[1])
        k3 = f(t + dt/2, p + dt/2*k2[0], V + dt/2*k2[1]); k4 = f(t + dt, p + dt*k3[0], V + dt*k3[1])
        p += dt/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); V += dt/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]); t += dt
        minV = min(minV, V)
        if cross is None and V < Vmin: cross = t
    return p, minV, cross
p, minV, cross = run_field(lambda t: 1 - 1 / (1 + math.exp(min(t, 700))))
say(f"review counterexample (tau_eff = 1 - 1/(1+e^t) < nu, finite cumulative advantage): p(2000) = {p:.6f} (2/11 = {2/11:.6f}),",
    f"min V = {minV:.6f} (39/55 = {39/55:.6f}), floor crossed: {cross is not None}")
p, minV, cross = run_field(lambda t: 0.9)
say(f"repaired C1 (tau_eff = nu - 0.1, cumulative advantage unbounded): p(2000) = {p:.6f}, floor crossed at t = {cross:.1f}")

say("\n== Repair: Theorem 2(3) support assumption (review R2) ==")
# only loads 0 and 0.1 present, tau_eff = 0, C0 holds for ebar = 1 but not for the actual maximum
p, V, dt = 0.5, 1.0, 0.01
minV = 1.0
for _ in range(int(2000 / dt)):
    p += dt * p * (1 - p) * 0.1
    V += dt * V * (0.05 * (1 - V) - 0.08 * 0.1 * p)
    minV = min(minV, V)
say(f"no positive-share carrier above the unsafe load: tau_eff = 0 throughout, yet min V = {minV:.4f} > V_min = 0.3 (limit 0.84)")

say("\n== Repair: conservative alarm (Remark 5, review R4) ==")
import random
random.seed(7)
K, b_in, Vt = 1.0, 0.5, 0.6
a_thr = Vt + b_in * (K - Vt)
misses = 0; early = []
for trial in range(2000):
    V, t, dt = 1.0, 0.0, 0.01
    rate = random.uniform(0.005, 0.05)
    m = random.uniform(0, b_in); fired = None; reached = None
    while V > 0.05:
        if random.random() < 0.01: m = random.uniform(0, b_in)   # masking can jump anywhere in [0, b_in]
        rep = V + m * (K - V)
        if fired is None and rep <= a_thr: fired = t
        if reached is None and V <= Vt: reached = t
        V -= dt * rate * V; t += dt
    if fired is None or fired > reached + 1e-9: misses += 1
    else: early.append(reached - fired)
say(f"report threshold a = {a_thr:.2f} for true target {Vt} with masking bound {b_in}: misses in 2000 random paths = {misses};",
    f"median lead time of the alarm = {sorted(early)[len(early)//2]:.1f}")

with open(os.path.join(here, "checks_v4.log"), "w") as fh:
    fh.write("\n".join(log) + "\n")
