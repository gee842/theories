"""Checks for THEORY v4.2 (pure Python, no dependencies). Writes checks_v42.log.

checks_v4.py still covers the v4.1 results that v4.2 keeps unchanged. This script covers
what v4.2 adds or repairs, and reproduces every counterexample in the two reviews of v4.1
(reviews/R-v4.1-external-gpt.md, labelled G-*; the independent Claude review, labelled C-*),
so that each repaired statement is checked against the case that broke the old one.

  G-R1a  delegation is not forced when the control loss dominates (Prop 6(5))
  G-R1b  small positive r still leaves a deviation incentive at a low baseline (Thm A, branch III)
  G-R2   preventive attack depends on the bargaining protocol (Prop 8)
  G-R3a  an asymmetric pure equilibrium beyond r = n/(n-1) (Prop 5(3))
  G-R3b  best response in the objective vs material and true-welfare comparisons (Prop 4(2))
  G-R4   cooperation without verification; imperfect verification sufficing (Prop 13, Thm B)
  G-R5   partial row sum below one, full row sum above one: capture (Prop 18, Def 3(c))
  G-R6   overhang growing faster than the exit hazard falls, with falling expected loss (Prop 15)
  G-R7   trust above the threshold without risk dominance (Prop 13(4), Thm C)
  G-14   cumulative selection vs long-run average liability (C1 falsifier); Prop 6 raw payoffs
  C-1    joining vs staying out with a penalty for falling behind (Prop 4(3))
  C-2    PD correction for x' = a x + u(t - tau): stabilizing gains exist at a*tau = 1.5 (Prop 7)
  C-3    the peak-sensitivity bound e^{a tau} (Prop 7(2))
  N-22   a common frontier in the assurance game (Prop 22)
  N-S    the race in survival terms; staying out of an AI-instrumented race (Thm S, Prop 23-24)
"""
import math, os, random
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

def grid_max(f, lo, hi, n=20000):
    best_x, best_v = lo, f(lo)
    for k in range(1, n + 1):
        x = lo + (hi - lo) * k / n
        v = f(x)
        if v > best_v: best_x, best_v = x, v
    return best_x, best_v

def tullock_w(i, e, r):
    s = sum(x ** r for x in e)
    return (e[i] ** r / s) if s > 0 else 1.0 / len(e)

# ------------------------------------------------------------------ G-R1a
say("== G-R1a: Prop 6, delegation never chosen when L_c * dpsi dominates ==")
def deleg_gain(n, k, s, r, Le):
    # w with own delegation vs without, k others delegating
    def w(own):
        num = (1 + s * own) ** r
        return num / (num + k * (1 + s) ** r + (n - 1 - k))
    return Le * (w(1) - w(0))
def deleg_cost(n, k, Lc, p0, p1):
    return Lc * (p1 - p0) * (1 - p0) ** (n - 1 - k) * (1 - p1) ** k
n, Le, Lc, p0, p1 = 3, 1.0, 100.0, 0.01, 0.2
worst = -1e9
for k in range(n):
    for s in (0.1, 1, 10, 100, 1e4):
        for r in (0.5, 1, 2, 8):
            worst = max(worst, deleg_gain(n, k, s, r, Le) - deleg_cost(n, k, Lc, p0, p1))
say(f"n=3, L_e=1, L_c=100, psi0=0.01, psi1=0.2: min cost = {deleg_cost(n, 2, Lc, p0, p1):.2f}; "
    f"max (gain - cost) over k, s, r = {worst:.3f} (negative: delegation never chosen)")
say("survival-first actors (L_e = L_c = 1), n=3: limiting gain vs cost by k:")
for k in range(n):
    g = (1 - 1 / n) if k == 0 else 1 / (k + 1)
    c_ = deleg_cost(n, k, 1.0, p0, p1)
    say(f"  k={k}: gain {g:.3f}  cost {c_:.3f}  delegate: {g > c_}")

# ------------------------------------------------------------------ G-R1b
say("\n== G-R1b: small r, deviation from a low symmetric baseline ==")
def m_contest(i, e, Om, r, c, l):
    return Om * tullock_w(i, e, r) - c * e[i] - l * sum(e)
Om, c, l, r, e0 = 100.0, 1.0, 0.1, 0.1, 0.01
gain = m_contest(0, [0.02, e0], Om, r, c, l) - m_contest(0, [e0, e0], Om, r, c, l)
say(f"n=2, Omega=100, c=1, l=0.1, r=0.1, e0=0.01 -> 0.02: payoff change {gain:+.5f}")
say(f"marginal at baseline: Omega r (n-1)/(n^2 e0) - (c+l) = {Om*r*1/(4*e0) - (c+l):+.3f}")
say("symmetric equilibrium intensity e = r Om (n-1)/(n^2 (c+l)) scales with r:",
    ", ".join(f"r={rr}: {rr*Om/(4*(c+l)):.3f}" for rr in (0.01, 0.1, 1.0)))

# ------------------------------------------------------------------ G-R2
say("\n== G-R2: Prop 8 and the bargaining protocol ==")
w1, w2, cA, cB, d = 0.5, 0.0, 0.2, 0.2, 0.8
warA = (w1 - cA) / (1 - d); warB = (1 - w1 - cB) / (1 - d)
def peace(x):  # A gets 1 now, then x per period; B gets 0 now, then 1-x
    return 1 + d * x / (1 - d), d * (1 - x) / (1 - d)
for label, x in (("rising side B proposes (x = max(w2 - cA, 0))", max(w2 - cA, 0)),
                 ("a mutually acceptable split x = 0.19", 0.19),
                 ("A proposes (x = min(w2 + cB, 1))", min(w2 + cB, 1))):
    pA, pB = peace(x)
    say(f"  {label}: peace A={pA:.2f} B={pB:.2f} | war now A={warA:.2f} B={warB:.2f} | "
        f"A attacks: {warA > pA}")
say(f"general condition w1 - cA > (1-d) + d x: B-proposer {w1 - cA > (1-d) + d*max(w2-cA,0)}, "
    f"A-proposer {w1 - cA > (1-d) + d*min(w2+cB,1)}")
say(f"large war cost cA = 0.6 >= w1: attack never rational: {not (w1 - 0.6 > (1-d))}")

# ------------------------------------------------------------------ G-R3a
say("\n== G-R3a: asymmetric pure equilibrium, n=3, r=2 ==")
C = 1.3  # c + l, any positive value
eq = [1 / (2 * C), 1 / (2 * C), 0.0]
def obj(i, e):  # theta = 0, material payoff with c + l folded into C (others' load is constant)
    return tullock_w(i, e, 2) - C * e[i]
best_dev = -1e9
for i in range(3):
    base = obj(i, eq)
    for k in range(1, 4001):
        x = 3.0 * k / 4000
        e = list(eq); e[i] = x
        best_dev = max(best_dev, obj(i, e) - base)
say(f"(1/(2C), 1/(2C), 0) with C={C}: best unilateral improvement {best_dev:.2e} (<= 0: equilibrium)")

# ------------------------------------------------------------------ G-R3b
say("\n== G-R3b: theta = -1, best response vs material and true welfare ==")
Om, c, l, kappa = 1.0, 1.0, 0.1, 0.2
e = 1 / 2  # r Om / (n c) at n=2, r=1
P_m = m_contest(0, [e, e], Om, 1, c, l)
S_m = m_contest(0, [0.0, e], Om, 1, c, l)
other_S = m_contest(1, [0.0, e], Om, 1, c, l)
say(f"material: race P = {P_m:+.3f}, stop alone S = {S_m:+.3f} (S > P)")
say(f"true welfare kappa=0.2: race {P_m + kappa*P_m:+.3f}, stop {S_m + kappa*other_S:+.3f}")
def rel_obj(x):  # theta = -1: own minus other's material payoff
    ee = [x, e]
    return m_contest(0, ee, Om, 1, c, l) - m_contest(1, ee, Om, 1, c, l)
bx, _ = grid_max(rel_obj, 0.0, 3.0, 30000)
say(f"best response under theta = -1 to e = 0.5: {bx:.3f} (racing is still the strict best response)")

# ------------------------------------------------------------------ G-R4 / G-R7
say("\n== G-R4, G-R7: assurance game ==")
def thr(R, T, P, S, ups=0.0, F=0.0):
    Tu = ups * (P - F) + (1 - ups) * T
    gC, gD = R - Tu, (1 - ups) * (P - S)
    return Tu, gC, gD, (gD / (gC + gD) if gC > 0 else float('nan'))
for (R, T, P, S, u, F, note) in ((3, 2, 1, 0.5, 0.0, 0, "no verification, T < R"),
                                (3, 4, 1, 0.0, 0.6, 0, "T > R, imperfect verification"),
                                (3, 2.5, 1, -5, 0.1, 0, "trust above threshold, not risk dominant")):
    Tu, gC, gD, ps = thr(R, T, P, S, u, F)
    say(f"  {note}: T_u={Tu:.2f} gC={gC:.3f} gD={gD:.3f} threshold={ps:.5f} risk-dominant={gC > gD}")
say(f"  perfect timely detection (u=1): T_u = P - F = 1 < R = 3, threshold {thr(3,100,1,-5,1.0,0)[3]:.3f}")

# ------------------------------------------------------------------ G-R5
say("\n== G-R5: partial vs full row sum (one domain, sources held captured) ==")
def run_domain(row_sum, x0=0.05, z0=0.0, a=1.0, cc=1.0, dd=1.0, zeta=1.0, eps=1.0, T=400, dt=0.01):
    # x' = zeta x (1-x)(a z - c), z' = eps(sum_j b_j x_j - d z), sources x_j = 1
    b = row_sum * cc * dd / a   # so that R = a b /(c d) = row_sum
    x, z = x0, z0
    for _ in range(int(T / dt)):
        x += dt * zeta * x * (1 - x) * (a * z - cc)
        z += dt * eps * (b - dd * z)
    return x
for parts in ((0.95, 0.10), (0.6, 0.6), (0.85, 0.10)):
    say(f"  inbound parts {parts}: each < 1, full row {sum(parts):.2f} -> long-run share {run_domain(sum(parts)):.3f}")

# ------------------------------------------------------------------ G-R6
say("\n== G-R6: Prop 15, overhang vs expected exit loss ==")
for t in (0, 2, 4, 8):
    O, H = math.exp(2 * t), math.exp(-1.5 * t)
    say(f"  t={t}: O={O:.1f} H={H:.4f} L = H*sqrt(O) = {H*math.sqrt(O):.4f}")
say("  growth rate of L = dH/H - dmu/(1-mu) + elasticity * dO/O = -1.5 + 0.5*2 = -0.5")

# ------------------------------------------------------------------ G-14
say("\n== G-14: C1 is cumulative; long-run average liability can equal nu ==")
nu = 1.0
def tau_eff(t): return nu - 1 / (1 + t)
for T in (10, 1e3, 1e6):
    say(f"  T={T:g}: average tau_eff ~ {nu - math.log(1+T)/T:.4f}, cumulative advantage log(1+T) = {math.log(1+T):.2f}")
# replicator share of the race carrier under this tau_eff (two carriers, loads 1 and 0)
p, dt, t = 0.01, 0.01, 0.0
while t < 2e4:
    p += dt * p * (1 - p) * (nu - tau_eff(t)); t += dt
say(f"  race share from 0.01 after t = 2e4: {p:.4f} (cumulative selection still drives it up)")
say("Prop 6 example, raw payoffs u (n=3, r=1, L_e=L_c=1, psi0=0.01, psi1=0.2):")
none = -1 * (2 / 3) - 1 * (1 - 0.99 ** 3); allD = -1 * (2 / 3) - 1 * (1 - 0.8 ** 3)
say(f"  none delegate {none:.5f}, all delegate {allD:.5f}; shifted by L_e: {none+1:.4f}, {allD+1:.4f}")

# ------------------------------------------------------------------ C-1
say("\n== C-1: joining vs staying out with a penalty Lb for falling behind (theta = 0) ==")
def pay_pen(ei, eo, n, r, Om, Lb, c, l):
    tot = ei ** r + (n - 1) * eo ** r
    w = ei ** r / tot if tot > 0 else 1.0 / n
    return w * (Om + Lb) - Lb - c * ei - l * (ei + (n - 1) * eo)
for n_ in (2, 4):
    for r_ in (0.5, 1.0, n_ / (n_ - 1)):
        for Lb in (0.0, 1.0, 5.0):
            Om, c, l = 1.0, 1.0, 0.3
            e_ = r_ * (n_ - 1) * (Om + Lb) / (n_ ** 2 * (c + l))
            P = pay_pen(e_, e_, n_, r_, Om, Lb, c, l); S = pay_pen(0.0, e_, n_, r_, Om, Lb, c, l)
            f = (Om + Lb) / n_ * (1 - r_ * (n_ - 1) / n_)
            say(f"  n={n_} r={r_:.2f} Lb={Lb:.0f}: P-S = {P-S:+.4f}  formula (Om+Lb)/n (1 - r(n-1)/n) = {f:+.4f}")
random.seed(1); N = 400000
for Lb in (0.0, 1.0, 5.0):
    v = 1.0 + Lb; s = 0.0
    for _ in range(N):
        b1, b2 = random.uniform(0, v), random.uniform(0, v)
        s += (1.0 if b1 > b2 else -Lb) - b1
    say(f"  all-pay limit n=2, Lb={Lb:.0f}: E[join] = {s/N:+.3f}, stay out = {-Lb:+.3f}")

# ------------------------------------------------------------------ C-2
say("\n== C-2: correction with derivative action, y' = a y - kp y(t-tau) - kd y'(t-tau), a = 1 ==")
def windows(tau, kp, kd, T=150.0, dt=0.01):
    nd = int(round(tau / dt)); N = int(T / dt)
    y = [1.0] * (nd + 1); dy = [0.0] * (nd + 1)
    w1 = w2 = 0.0
    for k in range(N):
        d = y[-1] - kp * y[-1 - nd] - kd * dy[-1 - nd]
        y.append(y[-1] + dt * d); dy.append(d)
        t = (k + 1) * dt
        if T - 60 < t <= T - 30: w1 = max(w1, abs(y[-1]))
        if t > T - 30: w2 = max(w2, abs(y[-1]))
        if abs(y[-1]) > 1e8: return float('inf'), float('inf')
    return w1, w2
for (tau, kp, kd, note) in ((1.5, 1.02, 0.0, "proportional only"),
                            (1.5, 1.02, 0.644, "with derivative action"),
                            (1.2, 1.10, 0.548, "with derivative action")):
    w1, w2 = windows(tau, kp, kd)
    say(f"  a*tau={tau} kp={kp} kd={kd} ({note}): max|y| on [90,120] = {w1:.2e}, on [120,150] = {w2:.2e}")
best = float('inf')
for i in range(25):
    for j in range(20):
        best = min(best, windows(2.2, 0.9 + 0.04 * i, 0.5 + 0.024 * j)[1])
for i in range(20):
    for j in range(19):
        best = min(best, windows(2.2, 0.8 + 0.1 * i, -0.9 + 0.1 * j)[1])
say(f"  a*tau=2.2: smallest late max|y| over two (kp, kd) grids = {best:.2e} (no decay found)")

# ------------------------------------------------------------------ C-3
say("\n== C-3: peak complementary sensitivity >= e^{a tau} (maximum modulus) ==")
for at in (0.5, 1.0, 1.5, 2.0, 3.0):
    say(f"  a*tau = {at}: ||T|| >= {math.exp(at):.2f}; tolerated relative model error <= {math.exp(-at):.3f}")

# ------------------------------------------------------------------ N-22
say("\n== N-22: a common frontier in the assurance game ==")
def classify(R, T, P, S):
    gC, gS = R - T, S - P   # advantage of cooperating when the other cooperates / defects
    if gC >= 0 and gS >= 0: return "cooperation dominant"
    if gC > 0 and gS < 0:   return f"stag hunt, trust threshold {(-gS)/(gC - gS):.3f}, risk-dominant {gC > -gS}"
    if gC < 0 and gS > 0:   return f"chicken (cooperate only if the other is likely to defect, below {gS/(gS - gC):.3f})"
    return "prisoner's dilemma (defection dominant)"
def regime(n, r, Om, Omc, Lb, c, l, ec, pooled, lose_pen=1.0):
    # cooperators hold effort ec; one defector best-responds. A losing defector bears lose_pen*Lb.
    if pooled:
        R = Omc / n - c * ec - l * n * ec           # common value, no dominance among cooperators
        others = ((n - 1) * ec) ** r                # the pool contests a defector as one entity
    else:
        R = Om / n - (n - 1) / n * Lb - c * ec - l * n * ec   # slow, but someone still wins
        others = (n - 1) * ec ** r
    def T_of(ed):
        wd = ed ** r / (ed ** r + others)
        return wd * Om - (1 - wd) * lose_pen * Lb - c * ed - l * (ed + (n - 1) * ec)
    ed, T = grid_max(T_of, 0.0, 6.0, 12000)
    wd = ed ** r / (ed ** r + others)
    if pooled: S = (1 - wd) * Omc / (n - 1) - wd * Lb - c * ec - l * (ed + (n - 1) * ec)
    else:
        wj = ec ** r / (ed ** r + others)
        S = wj * Om - (1 - wj) * Lb - c * ec - l * (ed + (n - 1) * ec)
    eP = r * (n - 1) * (Om + Lb) / (n ** 2 * (c + l))
    P = (Om + Lb) / n - Lb - c * eP - l * n * eP
    return R, T, P, S, wd
base = dict(n=4, Omc=1.0, Lb=1.0, c=1.0, l=0.3)
for r_ in (1.3, 1.0):
    for pooled in (False, True):
        R, T, P, S, wd = regime(r=r_, Om=1.0, ec=0.05, pooled=pooled, **base)
        say(f"  r={r_} {'CF ' if pooled else 'SEP'} (Om=1, ec=0.05): R={R:+.3f} T={T:+.3f} P={P:+.3f} S={S:+.3f} "
            f"defector w={wd:.2f} -> {classify(R, T, P, S)}")
say("  pooled effort per cooperator needed for T <= R (r=1.3), by the value of winning Om:")
for lp in (1.0, 0.0):
    for Om in (0.5, 1.0, 2.0, 4.0):
        found = None
        for k in range(1, 401):
            ec = 0.0025 * k
            R, T, P, S, wd = regime(r=1.3, Om=Om, ec=ec, pooled=True, lose_pen=lp, **base)
            if T <= R: found = (ec, R); break
        say(f"    losing defector penalty {lp:.0f}, Om={Om}: " +
            (f"e* = {found[0]:.4f}, R at e* = {found[1]:+.3f}" if found else "none up to e = 1"))

# ------------------------------------------------------------------ N-S
say("\n== N-S: the race in survival terms ==")
def survival_branches(n, qI, qII, qW, pdec, pdecS, hR):
    PhiR = 1 - hR
    PhiT = (1 - qII) * (1 - qW)
    PhiP = (1 - qI) * (1 - qII) * (1 - qW) * (1 - pdec * (n - 1) / n)
    PhiS = (1 - qII) * (1 - pdecS)
    return PhiR, PhiT, PhiP, PhiS
for (qI, qII, qW, pdec, pdecS) in ((0.05, 0.1, 0.1, 0.3, 0.3), (0.2, 0.1, 0.1, 0.3, 0.3), (0.6, 0.3, 0.2, 0.6, 0.6),
                                    (0.6, 0.3, 0.2, 0.6, 0.8), (0.9, 0.6, 0.3, 0.9, 0.9), (0.99, 0.9, 0.3, 0.99, 0.99)):
    R, T, P, S = survival_branches(2, qI, qII, qW, pdec, pdecS, 0.1)
    num = P - S
    th = num / ((R - T) + num) if num > 0 else 0.0
    qbar = 1 - (1 - pdecS) / ((1 - qW) * (1 - pdec * 0.5))
    say(f"  qI={qI} qII={qII} qW={qW} pdec={pdec} pdecS={pdecS}: Phi R={R:.3f} T={T:.3f} P={P:.3f} S={S:.3f} | "
        f"threshold {th:.3f} | staying out >= joining: {S >= P} (needs qI >= {qbar:.3f})")

with open(os.path.join(here, "checks_v42.log"), "w") as fh:
    fh.write("\n".join(log) + "\n")
