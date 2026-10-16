"""Checks for THEORY v4.4 (pure Python, no dependencies). Writes checks_v44.log.

checks_v4.py and checks_v42.py still cover what v4.4 keeps. This script covers what v4.4
adds or repairs after the five-perspective review of v4.3 (reviews/R-v4.3-*.md: M = math,
IR = international relations, S = AI safety, E = economics, A = argument), and re-derives
the reviewers' counterexamples so that each repaired statement is checked against the case
that broke the old one.

  N22   Prop 22 in the consistent n-player game (M1, E1): Coop(k) vs Race(k+1), equilibria,
        thresholds; n = 2; sensitivity
  DC    the delegation condition: exact per-k form; survival form with subordination p (M7, E2)
  RC    risk compensation in Prop 6's model (S6)
  B2    branch II of Theorem A as a multi-period shift (M12)
  LM    Lemma M: understanding that grows sub-exponentially against capability that compounds
  SV    survival branches with state-dependent hazards; leader; Prop 24 path (M4-M6, E3, E4, IR1)
  P15   Prop 15(1): irreversible exit vs reversible covert preparation (M9)
"""
import math, os, itertools
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

def gmax(f, lo, hi, n=4000):
    bx, bv = lo, f(lo)
    for k in range(1, n + 1):
        x = lo + (hi - lo) * k / n; v = f(x)
        if v > bv: bx, bv = x, v
    # refine
    step = (hi - lo) / n
    a, b = max(lo, bx - step), min(hi, bx + step)
    for _ in range(60):
        m1, m2 = a + (b - a) / 3, b - (b - a) / 3
        if f(m1) < f(m2): a = m1
        else: b = m2
    x = (a + b) / 2
    return (x, f(x)) if f(x) > bv else (bx, bv)

# ------------------------------------------------------------------ N22
say("== N22: Proposition 22 in the consistent n-player game ==")
def payoffs(n, k, r, Om, Omc, Lb, c, l, ec, pooled, lose_pen=1.0):
    """k racers (symmetric Nash among them), m = n-k cooperators at effort ec.
    Returns (cooperator payoff, racer payoff). SEP: every effort enters the decisive contest
    separately. CF: cooperators pool into one entity of strength (m ec)^r; if the pool prevails
    each cooperator gets Omc/m and losing racers bear lose_pen*Lb; if a racer prevails it gets
    Om and everyone else bears Lb."""
    m = n - k
    def strengths(e_r, e_i=None):
        return e_r
    def racer_pay(ei, er):  # racer i at ei, other k-1 racers at er
        if pooled:
            S = ei ** r + (k - 1) * er ** r + ((m * ec) ** r if m > 0 else 0.0)
            wi = ei ** r / S if S > 0 else 1.0 / max(k, 1)
            E = ei + (k - 1) * er + m * ec
            return wi * Om - (1 - wi) * lose_pen * Lb - c * ei - l * E
        S = ei ** r + (k - 1) * er ** r + m * ec ** r
        wi = ei ** r / S if S > 0 else 1.0 / n
        E = ei + (k - 1) * er + m * ec
        return wi * Om - (1 - wi) * Lb - c * ei - l * E
    if k == 0:
        er = 0.0
    else:
        er = 0.2
        for _ in range(200):
            br, _ = gmax(lambda x: racer_pay(x, er), 0.0, 8.0, 800)
            if abs(br - er) < 1e-9: break
            er = 0.5 * er + 0.5 * br
    E = k * er + m * ec
    if pooled:
        S = k * er ** r + ((m * ec) ** r if m > 0 else 0.0)
        wp = ((m * ec) ** r / S) if (S > 0 and m > 0) else (1.0 if k == 0 else 0.0)
        coop = (wp * Omc / m - (1 - wp) * Lb - c * ec - l * E) if m > 0 else None
    else:
        S = k * er ** r + m * ec ** r
        wc = ec ** r / S if S > 0 else 1.0 / n
        coop = (wc * Om - (1 - wc) * Lb - c * ec - l * E) if m > 0 else None
    race = racer_pay(er, er) if k > 0 else None
    return coop, race, er

def table(n, r, Om, Omc, Lb, c, l, ec, pooled):
    rows = []
    for k in range(n):  # k = number of OTHERS racing
        coop, _, _ = payoffs(n, k, r, Om, Omc, Lb, c, l, ec, pooled)
        _, race, _ = payoffs(n, k + 1, r, Om, Omc, Lb, c, l, ec, pooled)
        rows.append((k, coop, race))
    return rows

def equilibria(rows, n):
    eq = []
    for j in range(n + 1):  # j racers in profile
        ok = True
        if j < n:   # a cooperator facing j racers must not prefer racing
            ok &= rows[j][1] >= rows[j][2] - 1e-12
        if j > 0:   # a racer facing j-1 other racers must not prefer cooperating
            ok &= rows[j - 1][2] >= rows[j - 1][1] - 1e-12
        if ok: eq.append(j)
    return eq

def per_rival_threshold(rows, n):
    # each other actor races independently with prob q; find largest q with coop >= race
    def adv(q):
        s = 0.0
        for k in range(n):
            pk = math.comb(n - 1, k) * q ** k * (1 - q) ** (n - 1 - k)
            s += pk * (rows[k][1] - rows[k][2])
        return s
    lo, hi = 0.0, 1.0
    if adv(0) < 0: return None
    if adv(1) >= 0: return 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if adv(mid) >= 0: lo = mid
        else: hi = mid
    return lo

base = dict(Om=1.0, Omc=1.0, Lb=1.0, c=1.0, l=0.3, ec=0.05)
for pooled in (False, True):
    rows = table(4, 1.3, pooled=pooled, **base)
    lab = 'CF ' if pooled else 'SEP'
    say(f" {lab} n=4 r=1.3: " + "  ".join(f"k={k}: Coop {co:+.3f} Race {ra:+.3f}" for k, co, ra in rows))
    eq = equilibria(rows, 4)
    q = per_rival_threshold(rows, 4)
    R, T, Sp, P = rows[0][1], rows[0][2], rows[3][1], rows[3][2]
    agg = (P - Sp) / ((R - T) + (P - Sp)) if (R > T and P > Sp) else None
    say(f"     pure equilibria (number racing): {eq}; per-rival: cooperate iff each other races with prob < "
        f"{q if q is None else round(q, 3)}; aggregate reduction R={R:+.3f} T={T:+.3f} S'={Sp:+.3f} P={P:+.3f}"
        + (f", threshold {agg:.3f}, risk-dominant {R - T > P - Sp}" if agg is not None else ""))
rows2 = table(2, 1.3, pooled=True, **base)
say(f" CF n=2 r=1.3: R={rows2[0][1]:+.3f} T={rows2[0][2]:+.3f} S={rows2[1][1]:+.3f} P={rows2[1][2]:+.3f} "
    f"equilibria {equilibria(rows2, 2)} (prisoner's dilemma if only all-race)")
say(" sensitivity, CF (n=4 unless stated): equilibria by variation")
for name, kw, n_, r_ in (("ec=0.1", dict(base, ec=0.1), 4, 1.3), ("Lb=2", dict(base, Lb=2.0), 4, 1.3),
                        ("Omc=2", dict(base, Omc=2.0), 4, 1.3), ("l=0", dict(base, l=0.0), 4, 1.3),
                        ("r=1.2", base, 4, 1.2), ("n=6", base, 6, 1.3)):
    rws = table(n_, r_, pooled=True, **kw)
    say(f"   {name}: equilibria {equilibria(rws, n_)}; cooperation dominant: "
        f"{all(co >= ra for _, co, ra in rws)}")

# ------------------------------------------------------------------ DC
say("\n== DC: the delegation condition ==")
def lim_gain(n, k): return (1 - 1 / n) if k == 0 else 1 / (k + 1)
def cost(n, k, Lc, p0, p1): return Lc * (p1 - p0) * (1 - p0) ** (n - 1 - k) * (1 - p1) ** k
for (n, Le, Lc, p0, p1) in ((3, 1, 1, 0.01, 0.5), (3, 1, 1, 0.01, 0.4)):
    say(f" n={n} Le={Le} Lc={Lc} psi0={p0} psi1={p1}: D (Le/n > Lc dpsi) = {Le / n > Lc * (p1 - p0)}; "
        + ", ".join(f"k={k}: {Le * lim_gain(n, k) - cost(n, k, Lc, p0, p1):+.3f}" for k in range(n))
        + "  (positive: delegation strictly dominant as s grows)")
say(" survival measure: Phi_i = Q [w_i + (1 - w_i)(1 - p)], p = prob. that losing means subordination")
def phi_gain(n, k, p0, p1, p):
    Qd = (1 - p0) ** (n - 1 - k) * (1 - p1) ** (k + 1)
    Qn = (1 - p0) ** (n - k) * (1 - p1) ** k
    w1 = 1.0 if k == 0 else 1 / (k + 1); w0 = 1 / n if k == 0 else 0.0
    return Qd * (w1 + (1 - w1) * (1 - p)) - Qn * (w0 + (1 - w0) * (1 - p))
for (n, p0, p1, p) in ((3, 0.0, 0.5, 1.0), (3, 0.01, 0.2, 0.1), (3, 0.01, 0.5, 1.0), (2, 0.2, 0.65, 1.0)):
    say(f"  n={n} psi0={p0} psi1={p1} p={p}: 1/n > dpsi: {1 / n > p1 - p0}; Phi gain by k: "
        + ", ".join(f"{phi_gain(n, k, p0, p1, p):+.3f}" for k in range(n)))

# ------------------------------------------------------------------ RC
say("\n== RC: risk compensation in Proposition 6's model ==")
def w_of(n, s, profile, i, r=1.0):
    num = (1 + s * profile[i]) ** r
    return num / sum((1 + s * d) ** r for d in profile)
def u(n, s, profile, i, Le, Lc, p0, p1):
    Q = 1.0
    for d in profile: Q *= (1 - (p1 if d else p0))
    return -Le * (1 - w_of(n, s, profile, i)) - Lc * (1 - Q)
def pure_ne(n, s, Le, Lc, p0, p1):
    out = []
    for prof in itertools.product((0, 1), repeat=n):
        ok = True
        for i in range(n):
            alt = list(prof); alt[i] = 1 - prof[i]
            if u(n, s, alt, i, Le, Lc, p0, p1) > u(n, s, list(prof), i, Le, Lc, p0, p1) + 1e-12: ok = False; break
        if ok: out.append(prof)
    return out
n, Le, Lc, p0 = 3, 1.0, 100.0, 0.01
base_h = 1 - (1 - p0) ** n
for dpsi in (0.19, 0.01, 0.005, 0.003, 0.001):
    p1 = p0 + dpsi
    for s in (100.0, 1000.0):
        nes = pure_ne(n, s, Le, Lc, p0, p1)
        hs = sorted(set(round(1 - math.prod(1 - (p1 if d else p0) for d in pr), 4) for pr in nes))
        say(f"  dpsi={dpsi} s={s:g}: equilibria (delegators) {[sum(pr) for pr in nes]}; realized hazard {hs} (baseline {base_h:.4f})")

# ------------------------------------------------------------------ B2
say("\n== B2: a decisive but slow shift (multi-period, A8) ==")
def first_attack(N, w0=0.5, wN=0.0, cA=0.05, d=0.8, horizon=400):
    ws = [w0 + (wN - w0) * min(t, N) / N for t in range(horizon + 1)]
    W = [(w - cA) / (1 - d) for w in ws]
    V = [0.0] * (horizon + 2)
    V[horizon + 1] = max(W[horizon], 0.0)
    attack = [False] * (horizon + 1)
    for t in range(horizon, -1, -1):
        cont = d * V[t + 1]
        if W[t] > 1 + cont: attack[t] = True; V[t] = W[t]
        else: V[t] = max(W[t], cont)
    return next((t for t in range(horizon + 1) if attack[t]), None)
for N in (1, 2, 3, 4, 5, 8, 20):
    say(f"  w from 0.5 to 0 over N={N} periods (cA=0.05, delta=0.8): first period with attack: {first_attack(N)}")

# ------------------------------------------------------------------ LM
say("\n== LM: Lemma M, compounding capability against sub-exponential understanding ==")
def run_mismatch(g, u, h_phi, T=60, capped=False):
    surv, t = 1.0, 0
    X, U = 1.0, 1.0
    uncovered_hist = []
    for t in range(T + 1):
        X = math.exp(g * t) if not capped else min(math.exp(g * t), 1.0 + u * t)
        U = 1.0 + u * t
        unc = max(0.0, 1.0 - U / X)
        uncovered_hist.append(unc)
        surv *= (1 - h_phi * unc)
    return surv, uncovered_hist
for (g, u) in ((0.3, 0.5), (0.3, 2.0), (0.1, 0.5)):
    s, unc = run_mismatch(g, u, 0.05)
    sc, _ = run_mismatch(g, u, 0.05, capped=True)
    say(f"  g={g} u={u}: uncovered fraction at t=10,20,40: {unc[10]:.2f}, {unc[20]:.2f}, {unc[40]:.2f}; "
        f"survival to t=60 with h*phi=0.05: race {s:.3f}; capability held to the tempo of understanding (E3) {sc:.3f}")

# ------------------------------------------------------------------ SV
say("\n== SV: survival branches with state-dependent hazards ==")
def branches(n, qI, qIIT, qIIP, qIIS, qW, pdec, pdecS, hR, qIT=None):
    qIT = qI if qIT is None else qIT
    R = 1 - hR
    T = (1 - qIT) * (1 - qIIT) * (1 - qW)
    P = (1 - qI) * (1 - qIIP) * (1 - qW) * (1 - pdec * (n - 1) / n)
    S = (1 - qIIS) * (1 - pdecS)
    return R, T, P, S
def classify(R, T, P, S):
    gC, gS = R - T, S - P
    if gC >= 0 and gS >= 0: return "cooperation dominant"
    if gC > 0 and gS < 0: return f"stag hunt, threshold {(-gS) / (gC - gS):.3f}"
    if gC < 0 and gS > 0: return "chicken"
    return "prisoner's dilemma"
for lab, args in (("symmetric, joining raises the shared hazard", (2, 0.6, 0.3, 0.4, 0.3, 0.2, 0.6, 0.6, 0.1)),
                  ("same, shared hazard equal across branches", (2, 0.6, 0.3, 0.3, 0.3, 0.2, 0.6, 0.6, 0.1)),
                  ("staying out raises the racer's decisive chance", (2, 0.6, 0.3, 0.4, 0.3, 0.2, 0.6, 0.8, 0.1)),
                  ("low forced delegation", (2, 0.05, 0.1, 0.1, 0.1, 0.1, 0.3, 0.3, 0.1))):
    R, T, P, S = branches(*args)
    say(f"  {lab}: Phi R={R:.3f} T={T:.3f} P={P:.3f} S={S:.3f} -> {classify(R, T, P, S)}")
say(" leader (wins the race with prob 0.8; exiting hands the decisive advantage to the rival):")
for qII in (0.3, 0.8):
    R = 0.9; qI, qW, pdec, pS = 0.2, 0.2, 0.9, 0.95
    T = (1 - qI) * (1 - qII) * (1 - qW)
    P = (1 - qI) * (1 - qII) * (1 - qW) * (1 - pdec * (1 - 0.8))
    S = (1 - qII) * (1 - pS)
    say(f"  shared qII={qII}: Phi R={R:.3f} T={T:.3f} P={P:.3f} S={S:.3f} -> {classify(R, T, P, S)}")
say(" Proposition 24 path (M5): n=2, qW=0, qI = pdec = 1 - eps, pdecS = 1 - eps^2")
for eps in (0.1, 0.01):
    qI, p, pS = 1 - eps, 1 - eps, 1 - eps ** 2
    P = (1 - qI) * (1 - p / 2); S = (1 - pS)
    say(f"  eps={eps}: Phi P={P:.2e} S={S:.2e}; staying out at least as good: {S >= P}")

# ------------------------------------------------------------------ P15
say("\n== P15: two enforcement forms ==")
ups, F, gap = 0.9, 1.0, 5.0
say(f"  upsilon={ups} F={F} X-Xstay={gap}: irreversible exit deterred (uF >= gap): {ups * F >= gap}; "
    f"reversible covert preparation deterred (uF >= (1-u) gap): {ups * F >= (1 - ups) * gap}")

with open(os.path.join(here, "checks_v44.log"), "w") as fh:
    fh.write("\n".join(log) + "\n")
