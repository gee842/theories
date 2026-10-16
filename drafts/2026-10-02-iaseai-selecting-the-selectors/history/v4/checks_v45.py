"""Checks for THEORY v4.5 (pure Python, no dependencies). Writes checks_v45.log.

checks_v4.py, checks_v42.py and checks_v44.py still cover what v4.5 keeps. This script covers
what v4.5 adds or repairs after the second five-perspective review (reviews/R-v4.4-*.md:
M = math, IR = international relations, S = AI safety, E = economics, A = argument), and
re-derives the reviewers' counterexamples.

  Z2   two zeros: the delegation game in survival terms with the lock priced in (M-N3, A-N2, E-N2)
  HO   risk homeostasis: continuous delegation, closed form; the discrete saw-tooth (E-N9, S-N9, M-N18)
  CI   the catch-up index, and what a frozen lead is worth when others hold E3 (E-N1, A-N1)
  MF   Lemma M': freeze against roll back after a sprint (M-N6)
  SU   summability: E3 needs the uncovered fraction to be summable; the initial gap (M-N1, E-N6)
  HR   hazard-rate comparison instead of a summable residual hazard (A-N6, IR-N13, E-N3)
  LO   layered oversight: fidelity of a chain of overseers (S-N1)
  PH   predictability horizon under chaos (Ren, 10-03)
  LP   Lemma P: sustained prevention; the escalation needed to deter prevention (IR-N1)
  CC   c_conv = Q p; the region along the Prop 24 path (IR-N3)
  BC   degree of belief c in the premises: the survival trust threshold (M-N14)
  P24  Prop 24 with its own decisive probability p^H_dec (M-N8)
  N22  Prop 22 with Nash-verified racer subgames, two timings, risk dominance, the lid (M-N10, E-N8)
  K7   K7 as a mechanism-design problem (E 3.B)
  LD   a lead under diffusion (S-N3)
  DS   discounting: when a race that ends in catastrophe is still preferred (E-N3)
"""
import math, os, itertools, random
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

def gmax(f, lo, hi, n=800):
    bx, bv = lo, f(lo)
    for k in range(1, n + 1):
        x = lo + (hi - lo) * k / n; v = f(x)
        if v > bv: bx, bv = x, v
    step = (hi - lo) / n
    a, b = max(lo, bx - step), min(hi, bx + step)
    for _ in range(80):
        m1, m2 = a + (b - a) / 3, b - (b - a) / 3
        if f(m1) < f(m2): a = m1
        else: b = m2
    x = (a + b) / 2
    return (x, f(x)) if f(x) > bv else (bx, bv)

# ------------------------------------------------------------------ Z2
say("== Z2: two zeros (delegation game in survival terms, lock priced in) ==")
def w_of(s, prof, i, r=1.0):
    return (1 + s * prof[i]) ** r / sum((1 + s * d) ** r for d in prof)
def phi(s, prof, i, p0, p1, p, qL):
    Q = math.prod(1 - (p1 if d else p0) for d in prof)
    w = w_of(s, prof, i)
    base = Q * (w + (1 - w) * (1 - p))
    return base * ((1 - qL) if prof[i] else 1.0)
def pure_ne_phi(n, s, p0, p1, p, qL):
    out = []
    for prof in itertools.product((0, 1), repeat=n):
        ok, strict = True, True
        for i in range(n):
            alt = list(prof); alt[i] = 1 - prof[i]
            a, b = phi(s, alt, i, p0, p1, p, qL), phi(s, list(prof), i, p0, p1, p, qL)
            if a > b + 1e-12: ok = False; break
            if a > b - 1e-12: strict = False
        if ok: out.append((sum(prof), strict))
    return sorted(set(out))
s = 1e6
for (p0, p1, p) in ((0.0, 0.5, 1.0), (0.01, 0.05, 0.5), (0.01, 0.05, 1.0), (0.0, 0.5, 0.5), (0.01, 0.2, 1.0)):
    cells = []
    for qL in (0.0, 0.3, 0.6, 0.9, 1.0):
        ne = pure_ne_phi(3, s, p0, p1, p, qL)
        cells.append(f"qL={qL}: " + ("{" + ", ".join(f"{k}{'' if st else '(weak)'}" for k, st in ne) + "}"))
    say(f"  n=3 s=1e6 psi0={p0} psi1={p1} p={p}: delegators in pure equilibria -> " + "; ".join(cells))
say(" the two zeros (p=1, qL=1): Phi of not delegating when k others delegate, as s grows")
for k in (0, 1, 2):
    vals = []
    for s_ in (1.0, 10.0, 100.0, 1e4, 1e6):
        prof = [0] + [1] * k + [0] * (2 - k)
        vals.append(f"s={s_:g}: {phi(s_, prof, 0, 0.01, 0.05, 1.0, 1.0):.4f}")
    say(f"  k={k} others delegate: " + ", ".join(vals) + "   (delegating gives 0 for every s)")

# ------------------------------------------------------------------ HO
say("\n== HO: risk homeostasis ==")
def cont_eq(n, s, Le, Lc, p0, dpsi):
    # symmetric equilibrium in continuous delegation delta in [0,1]
    def u(di, d):
        sig_i, sig = 1 + s * di, 1 + s * d
        w = sig_i / (sig_i + (n - 1) * sig)
        Q = (1 - p0 - dpsi * di) * (1 - p0 - dpsi * d) ** (n - 1)
        return -Le * (1 - w) - Lc * (1 - Q)
    d = 0.5
    for _ in range(300):
        br, _ = gmax(lambda x: u(x, d), 0.0, 1.0, 400)
        if abs(br - d) < 1e-11: break
        d = 0.5 * d + 0.5 * br
    return d
def closed(n, s, Le, Lc, psi, dpsi):
    return (n - 1) * Le / (n * Lc * (1 - psi) ** (n - 1)) - n * dpsi / s
for n in (2, 3, 5):
    rows = []
    for dpsi in (0.19, 0.05, 0.02, 0.01, 0.005, 0.003, 0.001):
        d = cont_eq(n, 100.0, 1.0, 100.0, 0.01, dpsi)
        psi = 0.01 + dpsi * d
        cf = closed(n, 100.0, 1.0, 100.0, psi, dpsi)
        rows.append(f"dpsi={dpsi}: delta={d:.3f} added hazard n*dpsi*delta={n * dpsi * d:.4f} (closed form {cf:.4f}{', corner' if d > 0.999 else ''})")
    say(f"  n={n}, s=100, Le=1, Lc=100, psi0=0.01:")
    for r_ in rows: say("    " + r_)
say(" ratio Le/Lc drives the added hazard (n=3, s=100, dpsi=0.01):")
for Lc in (200.0, 100.0, 50.0):
    d = cont_eq(3, 100.0, 1.0, Lc, 0.01, 0.01)
    say(f"   Le/Lc={1 / Lc:.3f}: added hazard {3 * 0.01 * d:.4f}")
say(" discrete delegation, n=3, s=100, Le=1, Lc=100, psi0=0.01 (Proposition 6's model): the saw-tooth")
def u_disc(s, prof, i, Le, Lc, p0, p1):
    Q = math.prod(1 - (p1 if d else p0) for d in prof)
    return -Le * (1 - w_of(s, prof, i)) - Lc * (1 - Q)
def ne_disc(n, s, Le, Lc, p0, p1):
    out = []
    for prof in itertools.product((0, 1), repeat=n):
        if all(u_disc(s, list(prof), i, Le, Lc, p0, p1) >= u_disc(s, [1 - prof[j] if j == i else prof[j] for j in range(n)], i, Le, Lc, p0, p1) - 1e-12 for i in range(n)):
            out.append(prof)
    return out
cells = []
for dpsi in (0.19, 0.007, 0.0066, 0.006, 0.005, 0.004, 0.0034, 0.003, 0.002, 0.001):
    ne = ne_disc(3, 100.0, 1.0, 100.0, 0.01, 0.01 + dpsi)
    ks = sorted(set(sum(p_) for p_ in ne))
    hz = sorted(set(round(1 - (1 - 0.01) ** (3 - sum(p_)) * (1 - 0.01 - dpsi) ** sum(p_), 4) for p_ in ne))
    cells.append(f"{dpsi}: k={ks} hazard={hz}")
say("   " + "; ".join(cells) + f"  (baseline {1 - 0.99 ** 3:.4f})")
say(" general form (S-N9): any equilibrium with k>=1 delegators has realized hazard above the baseline for every dpsi>0:")
ok = all(1 - (0.99) ** (3 - k) * (0.99 - dp) ** k > 1 - 0.99 ** 3 for k in (1, 2, 3) for dp in (1e-4, 1e-3, 0.01, 0.1))
say(f"   checked k=1..3, dpsi in {{1e-4,1e-3,0.01,0.1}}: {ok}")

# ------------------------------------------------------------------ CI
say("\n== CI: the catch-up index; a frozen lead against rivals holding E3 ==")
def deviator_survival(kappa, t0, hphi=0.05, u=0.5, U0=1.0, gT=0.3, dt=1e-3):
    """Rivals hold capability at U(t). The deviator starts from U(t0), grows at gT until it holds
    kappa times the rivals' level (decisive), then freezes there until understanding catches up."""
    U = lambda t: U0 + u * t
    Ut0 = U(t0)
    H, t, X = 0.0, t0, Ut0
    while X < kappa * U(t):  # build-up
        H += hphi * max(0.0, 1 - U(t) / X) * dt; t += dt; X = Ut0 * math.exp(gT * (t - t0))
    t1, Xf = t, X
    while U(t) < Xf:  # frozen, waiting for understanding
        H += hphi * max(0.0, 1 - U(t) / Xf) * dt; t += dt
    return math.exp(-H), t, t1
def Hc(kappa, t0, hphi=0.05, u=0.5, U0=1.0):
    gU = u / (U0 + u * t0)
    return hphi * (kappa - 1) ** 2 / (2 * kappa * gU)
for kappa in (1.5, 2.0, 4.0):
    cells = []
    for t0 in (0, 20, 60, 200):
        sv, _, t1 = deviator_survival(kappa, t0)
        cells.append(f"t0={t0}: {sv:.3f} (exp(-Hc at the date of victory)={math.exp(-Hc(kappa, t1)):.3f})")
    say(f"  kappa={kappa}: " + "; ".join(cells))
say(" exponential understanding with g_U=0.2: psi(kappa)=ln kappa - 1 + 1/kappa, survival "
    + ", ".join(f"kappa={k}: {math.exp(-0.05 / 0.2 * (math.log(k) - 1 + 1 / k)):.3f}" for k in (2, 4)))
say(" the frozen lead: rivals at the tempo of understanding U(t); winner frozen at kappa times their level at victory")
for kappa, t0 in ((2.0, 20), (4.0, 60)):
    _, tc, t1 = deviator_survival(kappa, t0)
    Xf = kappa * (1 + 0.5 * t1)
    edge_at_tc = Xf / (1 + 0.5 * tc)
    say(f"  kappa={kappa} t0={t0}: understanding catches up at t={tc:.1f}; the winner's edge over E3 rivals then is {edge_at_tc:.3f}")

# ------------------------------------------------------------------ MF
say("\n== MF: Lemma M' (freeze against roll back) ==")
def lemma_m_path(g=0.3, u=0.5, hphi=0.05, tau=10):
    surv = 1.0
    for t in range(tau + 1):
        X = math.exp(g * t); U = 1 + u * t
        surv *= 1 - hphi * max(0.0, 1 - U / X)
    Xt = math.exp(g * tau)
    catch = (Xt - (1 + u * tau)) / u
    sf, t = surv, tau + 1
    while 1 + u * t < Xt:
        sf *= 1 - hphi * max(0.0, 1 - (1 + u * t) / Xt); t += 1
    return Xt, catch, surv, sf
for tau in (10, 15, 20):
    Xt, catch, sv, sf = lemma_m_path(tau=tau)
    say(f"  sprint to tau={tau}: X(tau)={Xt:.0f}, time for understanding to catch up {catch:.0f}, survival to tau {sv:.3f}, "
        f"freeze then wait {sf:.3g}; roll back at tau {sv:.3f}")

# ------------------------------------------------------------------ SU
say("\n== SU: summability ==")
def surv_path(Xf, Uf, T, hphi=0.05):
    s_ = 1.0
    for t in range(T + 1):
        s_ *= 1 - hphi * max(0.0, 1 - Uf(t) / Xf(t))
    return s_
say(f"  X = 2U (same tempo, half uncovered): survival to 1000 = {surv_path(lambda t: 2 * (1 + t), lambda t: 1 + t, 1000):.2e}")
say("  X = 2+t, U = 1+t (same speed, gap closes like 1/t, not summable): "
    + ", ".join(f"t={T}: {surv_path(lambda t: 2 + t, lambda t: 1 + t, T):.2f}" for T in (100, 1000, 10000, 100000)))
say(f"  X = 2+sqrt(t), U = 1+t (understanding catches up): survival to 10^5 = {surv_path(lambda t: 2 + math.sqrt(t), lambda t: 1 + t, 100000):.3f}")
say(" the initial gap (continuous, hphi=0.05, U = 1 + 0.5 t):")
for k0 in (1.25, 2.0):
    same = [math.exp(-0.05 * (1 - 1 / k0) * T) for T in (100, 400)]
    # pause: hold X = k0 until U = k0, then grow with U
    tc = (k0 - 1) / 0.5
    Hp = 0.05 * ((1 - 1 / k0) * tc - 0.5 * tc ** 2 / (2 * k0))
    say(f"  k0={k0}: grow at the tempo of understanding from the gap: survival to 100 = {same[0]:.3f}, to 400 = {same[1]:.3f}; "
        f"pause until understanding catches up, then E3: {math.exp(-Hp):.3f} for every horizon")

# ------------------------------------------------------------------ HR
say("\n== HR: hazard-rate comparison ==")
def race_hazard(t, g=0.3, u=0.5, hphi=0.05):
    return hphi * max(0.0, 1 - (1 + u * t) / math.exp(g * t))
for hbar in (0.005, 0.02):
    cells = []
    for T in (20, 40, 60, 100):
        sr = math.prod(1 - race_hazard(t) for t in range(T + 1))
        sR = (1 - hbar) ** (T + 1)
        cells.append(f"H={T}: race {sr:.3f}, arrangement {sR:.3f}, ratio {sr / sR:.3f}, bound exp(-(hphi-hbar)H) {math.exp(-(0.05 - hbar) * T):.3f}")
    say(f"  residual hazard under the arrangement {hbar}: " + "; ".join(cells))

# ------------------------------------------------------------------ LO
say("\n== LO: layered oversight ==")
for f in (0.95, 0.9, 0.8):
    for m in (10.0,):
        cells = []
        for t in (0, 5, 10, 20, 40):
            XB = 10.0 * math.exp(1.2 * t / 1.0) if False else math.exp(0.3 * t) * 10.0
            k = max(1.0, math.log(XB) / math.log(m))
            cells.append(f"t={t}: k={k:.1f}, fidelity {f ** k:.3f}")
        say(f"  per-layer fidelity f={f}, amplification m={m:g}, X/B = 10 e^(0.3t): " + "; ".join(cells))
say(" per-layer error needed to hold chain fidelity at 0.5 (m=10): "
    + ", ".join(f"t={t}: 1-f <= {1 - 0.5 ** (1 / max(1.0, math.log(10 * math.exp(0.3 * t)) / math.log(10))):.4f}" for t in (0, 10, 20, 40, 80)))

# ------------------------------------------------------------------ PH
say("\n== PH: predictability horizon (logistic map at r=4, Lyapunov exponent ln 2) ==")
random.seed(1)
for d0 in (1e-3, 1e-6, 1e-9, 1e-12):
    hs = []
    for _ in range(400):
        x = random.uniform(0.05, 0.95); y = x + d0
        t = 0
        while abs(x - y) < 0.1 and t < 200:
            x, y = 4 * x * (1 - x), 4 * y * (1 - y); t += 1
        hs.append(t)
    say(f"  initial error {d0:g}: mean steps until error > 0.1 = {sum(hs) / len(hs):.1f}  (ln(0.1/d0)/ln2 = {math.log(0.1 / d0) / math.log(2):.1f})")

# ------------------------------------------------------------------ LP
say("\n== LP: prevention under the individual criterion ==")
R, P, S_ = 0.900, 0.134, 0.140
for sig, e in ((0.7, 0.2), (0.3, 0.2)):
    prev = (1 - e) * (sig * R + (1 - sig) * P)
    estar = 1 - max(S_, P) / (sig * R + (1 - sig) * P)
    say(f"  one strike, success sigma={sig}, escalation e={e}: Phi_prev={prev:.3f}; prevention beats staying out or joining unless e > {estar:.3f}")
say(" escalation needed to deter prevention along the Prop 24 path (sigma=0.7, Phi_R=0.9):")
for eps in (0.1, 0.01, 0.001):
    Pp = eps * (1 + eps) / 2; Sp = eps ** 2
    say(f"  eps={eps}: e* = {1 - max(Pp, Sp) / (0.7 * 0.9 + 0.3 * Pp):.4f}")
say(" sustained prevention: the target rebuilds with prob b per period, each strike escalates with prob e:")
for b, e in ((0.2, 0.05), (0.1, 0.02)):
    say(f"  b={b} e={e}: Phi_prev(H) = " + ", ".join(f"H={H}: {(1 - b * e) ** H:.3f}" for H in (50, 200, 1000)))

# ------------------------------------------------------------------ CC
say("\n== CC: conversion of standing into survival ==")
for Q in (0.9, 0.5, 0.1):
    say(f"  Q={Q}: c_conv = Q p = " + ", ".join(f"p={p}: {Q * p:.2f}" for p in (0.5, 0.9, 1.0)))
say(" along the Prop 24 path, staying out against joining: " + ", ".join(
    f"eps={eps}: Phi_S/Phi_P={(eps ** 2) / (eps * (1 + eps) / 2):.3f}" for eps in (0.1, 0.01)) + "  (the region shrinks on this path)")

# ------------------------------------------------------------------ BC
say("\n== BC: degree of belief c in (X), (U), (phi') ==")
Rn, Tn, Pn, Sn = 0.900, 0.769, 0.654, 0.630   # the 'premises false' world: the low-delegation stag hunt
for c in (0.0, 0.5, 0.9, 0.99):
    T_, P_, S2 = (1 - c) * Tn, (1 - c) * Pn, (1 - c) * Sn
    thr = max(P_ - S2, 0) / ((Rn - T_) + max(P_ - S2, 0))
    say(f"  c={c}: survival trust threshold {thr:.4f}")

# ------------------------------------------------------------------ P24
say("\n== P24: E1 kept alone, with its own decisive probability ==")
for eps in (0.1, 0.01):
    Pp = eps * (1 + eps) / 2
    say(f"  eps={eps}: Phi_P={Pp:.4f}; E1 alone with p^H=p_dec: {eps:.4f} (better); with p^H=1-eps^2: {eps ** 2:.4f} (worse)")

# ------------------------------------------------------------------ N22
say("\n== N22: Proposition 22 with Nash-verified racer subgames ==")
def pay_focal(focal_race, x, others_r, m_coop, prm, pooled):
    """focal_race: focal is a racer at x; else focal is a cooperator (x ignored).
    others_r: intensities of the other racers; m_coop: number of cooperators (incl. focal if cooperator)."""
    r, Om, Omc, Lb, c, l, ec = prm['r'], prm['Om'], prm['Omc'], prm['Lb'], prm['c'], prm['l'], prm['ec']
    racers = ([x] if focal_race else []) + list(others_r)
    E = sum(racers) + m_coop * ec
    if pooled:
        pool = (m_coop * ec) ** r if m_coop > 0 else 0.0
        Ssum = sum(e ** r for e in racers) + pool
        if focal_race:
            wi = x ** r / Ssum if Ssum > 0 else 1.0
            return wi * Om - (1 - wi) * Lb - c * x - l * E
        wp = pool / Ssum if Ssum > 0 else 1.0
        return wp * Omc / m_coop - (1 - wp) * Lb - c * ec - l * E
    Ssum = sum(e ** r for e in racers) + m_coop * ec ** r
    if focal_race:
        wi = x ** r / Ssum if Ssum > 0 else 1.0 / (len(racers) + m_coop)
        return wi * Om - (1 - wi) * Lb - c * x - l * E
    wc = ec ** r / Ssum if Ssum > 0 else 1.0 / (len(racers) + m_coop)
    return wc * Om - (1 - wc) * Lb - c * ec - l * E
def racer_eq(n, k, prm, pooled):
    if k == 0: return 0.0, True
    m = n - k
    er = 0.2
    for _ in range(400):
        br, _ = gmax(lambda x: pay_focal(True, x, [er] * (k - 1), m, prm, pooled), 0.0, 8.0)
        if abs(br - er) < 1e-10: break
        er = 0.5 * er + 0.5 * br
    br, bv = gmax(lambda x: pay_focal(True, x, [er] * (k - 1), m, prm, pooled), 0.0, 8.0, 4000)
    ok = bv <= pay_focal(True, er, [er] * (k - 1), m, prm, pooled) + 1e-6
    return er, ok
def rows_two_stage(n, prm, pooled):
    out = []
    for k in range(n):
        er, ok1 = racer_eq(n, k, prm, pooled)
        coop = pay_focal(False, 0, [er] * k, n - k, prm, pooled)
        er2, ok2 = racer_eq(n, k + 1, prm, pooled)
        race = pay_focal(True, er2, [er2] * k, n - k - 1, prm, pooled)
        out.append((k, coop, race, ok1 and ok2))
    return out
def rows_simultaneous(n, prm, pooled):
    out = []
    for k in range(n):
        er, ok1 = racer_eq(n, k, prm, pooled)
        coop = pay_focal(False, 0, [er] * k, n - k, prm, pooled)
        _, race = gmax(lambda x: pay_focal(True, x, [er] * k, n - k - 1, prm, pooled), 0.0, 8.0, 4000)
        out.append((k, coop, race, ok1))
    return out
def eqs(rows, n):
    e = []
    for j in range(n + 1):
        ok = True
        if j < n: ok &= rows[j][1] >= rows[j][2] - 1e-12
        if j > 0: ok &= rows[j - 1][2] >= rows[j - 1][1] - 1e-12
        if ok: e.append(j)
    return e
def per_rival(rows, n):
    def adv(q):
        return sum(math.comb(n - 1, k) * q ** k * (1 - q) ** (n - 1 - k) * (rows[k][1] - rows[k][2]) for k in range(n))
    if adv(0) < 0: return None
    if adv(1) >= 0: return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if adv(mid) >= 0: lo = mid
        else: hi = mid
    return lo
def agg(rows, n):
    R, T, Sp, P = rows[0][1], rows[0][2], rows[n - 1][1], rows[n - 1][2]
    if R > T and P > Sp: return (P - Sp) / ((R - T) + (P - Sp)), (R - T) > (P - Sp)
    return None, None
base = dict(r=1.3, Om=1.0, Omc=1.0, Lb=1.0, c=1.0, l=0.3, ec=0.05)
for pooled in (False, True):
    rows = rows_two_stage(4, base, pooled)
    lab = 'CF ' if pooled else 'SEP'
    say(f" {lab} n=4 r=1.3 (two-stage): " + "  ".join(f"k={k}: Coop {co:+.3f} Race {ra:+.3f}{'' if ok else ' [no sym. pure racer eq.]'}" for k, co, ra, ok in rows))
    q = per_rival(rows, 4); a, rd = agg(rows, 4)
    say(f"     equilibria {eqs(rows, 4)}; per-rival trust needed {('%.3f' % (1 - q)) if q is not None else 'none suffices'}; aggregate threshold {a if a is None else round(a, 3)}, risk-dominant {rd}")
rows_s = rows_simultaneous(4, base, True)
q = per_rival(rows_s, 4)
say(f" CF n=4 r=1.3 (simultaneous: a deviator best-responds to fixed intensities): Race(2)={rows_s[1][2]:+.3f} against Coop(1)={rows_s[1][1]:+.3f}; per-rival trust needed {1 - q:.3f}")
say(" CF: does all-cooperate hold (R >= T) as r varies?")
for n in (2, 3, 4):
    cells = []
    for r in (0.5, 0.8, 1.0, 1.2, 1.25, 1.3):
        prm = dict(base, r=r)
        R = pay_focal(False, 0, [], n, prm, True)
        _, T = gmax(lambda x: pay_focal(True, x, [], n - 1, prm, True), 0.0, 8.0, 4000)
        cells.append(f"r={r}: {'yes' if R >= T else 'no'} (R={R:.3f}, T={T:.3f})")
    say(f"  n={n}: " + "; ".join(cells))
say(" CF variations (two-stage; Nash-verified):")
for name, prm, n_ in (("base", base, 4), ("n=3", base, 3), ("Lb=0.5", dict(base, Lb=0.5), 4), ("ec=0.03", dict(base, ec=0.03), 4),
                      ("l=0", dict(base, l=0.0), 4), ("Omc=2", dict(base, Omc=2.0), 4),
                      ("n=6, r=1.0", dict(base, r=1.0), 6), ("n=6, r=0.8", dict(base, r=0.8), 6), ("n=6, r=1.3", base, 6)):
    rws = rows_two_stage(n_, prm, True)
    a, rd = agg(rws, n_)
    bad = [k for k, _, _, ok in rws if not ok]
    say(f"  {name}: equilibria {eqs(rws, n_)}; aggregate threshold {a if a is None else round(a, 3)}; risk-dominant {rd}"
        + (f"; racer subgames without a symmetric pure equilibrium at k={bad} (results there are not equilibria)" if bad else ""))
say(" the lid: smallest pooled effort e* with T <= R")
def lid(Om, Omc, Lb, n=4):
    def gap(ec):
        prm = dict(base, Om=Om, Omc=Omc, Lb=Lb, ec=ec)
        R = pay_focal(False, 0, [], n, prm, True)
        _, T = gmax(lambda x: pay_focal(True, x, [], n - 1, prm, True), 0.0, 8.0, 2000)
        return T - R, R
    grid = [0.0005 * j for j in range(1, 2001)]
    prev = None
    for ec in grid:
        if gap(ec)[0] <= 0:
            lo, hi = (prev if prev is not None else 0.0), ec
            for _ in range(40):
                mid = (lo + hi) / 2
                if gap(mid)[0] > 0: lo = mid
                else: hi = mid
            return hi, gap(hi)[1]
        prev = ec
    return None, None
for Om in (0.5, 1.0, 2.0, 4.0):
    e1, R1 = lid(Om, 1.0, 1.0)
    e2, R2 = lid(Om, Om, Om)
    say(f"  Omega={Om}: fixed Omega_c=L_b=1: e*={'none' if e1 is None else round(e1, 4)}" + ("" if e1 is None else f" (R={R1:+.3f})")
        + f"; scaled Omega_c=L_b=Omega: e*={'none' if e2 is None else round(e2, 4)}" + ("" if e2 is None else f" (R={R2:+.3f})"))

# ------------------------------------------------------------------ K7
say("\n== K7: the mechanism-design form ==")
def race_U(rho, Om, Lb, strong_self, strong_other):
    if strong_self and not strong_other: return (Om + Lb) * (1 - rho) - Lb
    return -Lb
for Lb in (0.0, 0.5):
    cells = []
    for ps in (0.8, 0.5, 0.2, 0.05):
        EUs = (1 - ps) * race_U(0.1, 1.0, Lb, True, False) + ps * race_U(0.1, 1.0, Lb, True, True)
        EUw = race_U(0.1, 1.0, Lb, False, False)
        need = 2 * max(EUs, EUw)
        cells.append(f"p_s={ps}: sum of sup {need:.2f} -> {'feasible' if need <= 1.0 + 1e-12 else 'infeasible'} without verification")
    say(f"  rho=0.1, Omega=1, L_b={Lb}, S=1, all Phi=1: " + "; ".join(cells))
say(" survival compression (p_s=0.2, L_b=0, Phi_R=0.95, B=1): equal shares feasible iff Phi_race/Phi_R <= "
    f"{(0.95 * 3 / (2 * (0.72 + 1))) / 0.95:.3f}; at Phi_race=0.85: {2 * 1.72 * 0.85:.3f} vs {0.95 * 3:.3f}; at 0.80: {2 * 1.72 * 0.80:.3f} vs {0.95 * 3:.3f}")
say(" distribution: the strong type's minimum share under full information (L_b=0.5, S=1): "
    + ", ".join(f"rho={rho}: {race_U(rho, 1.0, 0.5, True, False):.3f}" for rho in (0.05, 0.2)))

# ------------------------------------------------------------------ LD
say("\n== LD: a lead under diffusion (leader pauses fully; dDelta/dt = -delta Delta - 1) ==")
for d0, dl in ((6.0, 0.05), (6.0, 0.1), (12.0, 0.1), (24.0, 0.1)):
    say(f"  lead {d0:g} months, diffusion {dl}/month: exhausted after {math.log(1 + dl * d0) / dl:.1f} months")

# ------------------------------------------------------------------ DS
say("\n== DS: discounting ==")
def value(rho, h, g):  # integral of e^{-rho t} e^{-h t} e^{g t}
    return 1 / (rho + h - g) if rho + h > g else float('inf')
for h in (0.01, 0.03, 0.05):
    vr, vp = value(0.05, h, 0.04), value(0.05, 0.0, 0.01)
    say(f"  rho=0.05, race hazard h={h}, race growth 0.04, paced growth 0.01: race {vr:.1f}, pace {vp:.1f} -> "
        f"{'race preferred' if vr > vp else 'pace preferred'} (rule: race iff h < g_r - g_p = 0.03); survival to infinity: race 0, pace 1")

with open(os.path.join(here, "checks_v45.log"), "w") as fh:
    fh.write("\n".join(log) + "\n")
