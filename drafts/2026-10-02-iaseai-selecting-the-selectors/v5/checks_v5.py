"""Checks for v5 (pure Python, no dependencies). Writes checks_v5.log.

v5 repairs the v4.5 results against the issues V45-01..V45-11 of the handoff review
(sources/19-v5-handoff-2026-10-03/v5_0_handoff/02_theory_v4_5_deep_review_and_handoff.md)
and adds the modules the v5 brief asks for. Each block names the claim in v5/THEORY.md it supports
and, where relevant, the counterexample it must respect. The reviewer's own script
(v5_0_handoff/verification/v4_5_review_checks.py) is a separate suite that needs NumPy and SciPy;
this script recomputes the cases v5 relies on independently.

  GM   the governing model: what a self-model can see, the race and the self-model, growth and the
       boundary, pooling and prize sharing (Props 1.2-1.5; v5.1, prize sharing v5.2)
  AG   perfect principal alignment in a harmful human game (Prop 4.1)
  CR   the chain-rule lemma and what a mere delay does (Lemma 4.4, Prop 4.5)
  FB   the local feedback benchmark ab < mu*delta (Remark 3.2)
  HO   risk homeostasis as an implicit equilibrium: branches, multiplicity, saturation (Prop 5.13; V45-02)
  DL   delegation in survival terms: exact dominance at qL = 1, qL < 1, bounded speed (Prop 5.5; V45-05)
  MM   the coverage mismatch theorem, the hazardous subset Y, catch-up and summability (Thm 5.8, Prop 5.9; V45-04)
  OV   oversight topology: serial chains, redundant checks, common cause (Prop 5.11; V45-03)
  SR   survival ratios in one discrete convention; mixed beliefs and their sign conditions (Prop 5.14; V45-07)
  FS   the finite sprint as a trade-off; prevention compared by hazard rates (Props 6.3, 6.5; V45-06)
  SG   a costly signal: when keeping AI out of one's decision loops separates types (Prop 8.4; V45-08)
  K7   interim incentive compatibility; equal shares without a lower value of winning (Prop 7.8; V45-09)
  N13  the n-player assurance condition needs a bound on deviation gains (Prop 8.1; V45-09)
  CAP  fixed splitting delays capture; third moment versus HHI; mean versus maximal load; a control screen (Props 2.4, 3.4-3.6; V45-11)
  CMP  a two-crux comparison of a continuation path and a cooperative path at common horizons (Section 6.9)
"""
import math, os, itertools, random
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

def bisect(f, lo, hi, it=200):
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2; fm = f(mid)
        if (fm > 0) == (flo > 0): lo, flo = mid, fm
        else: hi = mid
    return (lo + hi) / 2

# ------------------------------------------------------------------ GM
say("== GM: the governing model and the self-model ==")
random.seed(7)
# Prop 1.2: what a self-model can see
worst = 0.0
for trial in range(2000):
    n = random.randint(2, 6); th = random.uniform(-1, n - 1)
    pi = [random.uniform(-5, 5) for _ in range(n)]
    O = lambda p: [p[i] + th * sum(p[j] for j in range(n) if j != i) / (n - 1) for i in range(n)]
    o = O(pi); D = random.uniform(-3, 3)
    o2 = O([x + D for x in pi])
    worst = max(worst, abs(sum(o) - (1 + th) * sum(pi)), max(abs(o2[i] - o[i] - (1 + th) * D) for i in range(n)))
say(f"  Prop 1.2 (1)-(2): sum O = (1+theta) sum pi and a common shift D moves each O by (1+theta)D; max error over 2000 random games {worst:.1e}")
n = 4; pi = [3.0, -1.0, 0.5, 2.0]
zs = sum(p - sum(q for j, q in enumerate(pi) if j != i) / (n - 1) for i, p in enumerate(pi))
say(f"  Prop 1.2 (3): at theta=-1 objectives sum to {zs:.1e} (zero-sum); at theta=n-1 each objective equals the total: "
    f"{[round(p + (n - 1) * sum(q for j, q in enumerate(pi) if j != i) / (n - 1), 6) for i, p in enumerate(pi)]} vs {sum(pi)}")

# Prop 1.3 (1): faithful AI with a self-model
def ag_obj(n, b, c, d, eps, th, a):
    u = []
    for i in range(n):
        rel = a[i] - sum(a[j] for j in range(n) if j != i) / (n - 1)
        u.append(eps * b * rel - c * a[i] - eps * d * sum(a))
    return [u[i] + th * sum(u[j] for j in range(n) if j != i) / (n - 1) for i in range(n)]
def theta_star(n, b, c, d, eps):
    return (eps * (b - d) - c) / (eps * (b / (n - 1) + d))
for (n, b, c, d) in ((4, 1.0, 0.3, 0.2), (3, 2.0, 0.5, 0.1)):
    row = []
    for eps in (1.0, 2.0, 10.0, 1e6):
        ts = theta_star(n, b, c, d, eps)
        ok = True
        for th, sign in ((ts - 1e-3, 1), (ts + 1e-3, -1)):
            for rest in itertools.product((0, 1), repeat=n - 1):
                g = ag_obj(n, b, c, d, eps, th, [1] + list(rest))[0] - ag_obj(n, b, c, d, eps, th, [0] + list(rest))[0]
                ok &= (g > 0) if sign > 0 else (g < 0)
        row.append(f"eps={eps:g}: theta*={ts:.4f} (brute force agrees {ok})")
    say(f"  Prop 1.3 (1) n={n} b={b} c={c} d={d}: " + "; ".join(row) + f"; limit (b-d)/(b/(n-1)+d) = {(b - d) / (b / (n - 1) + d):.4f} < n-1 = {n - 1}")

# Prop 1.3 (2)-(3): contest intensity, dissipation, and power
def e_sym(n, r, Om, c, l, th):
    return r * Om * (n - 1 - th) / (n * n * (c + (1 + th) * l))
def obj_i(ei, eo, n, r, Om, c, l, th):
    tot = ei ** r + (n - 1) * eo ** r
    wi = ei ** r / tot; wo = eo ** r / tot
    E = ei + (n - 1) * eo
    pi_i = Om * wi - c * ei - l * E; pi_o = Om * wo - c * eo - l * E
    return pi_i + th * pi_o
def br(eo, n, r, Om, c, l, th):
    lo, hi = 1e-9, 10 * Om / c + 1
    for _ in range(200):
        m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
        if obj_i(m1, eo, n, r, Om, c, l, th) < obj_i(m2, eo, n, r, Om, c, l, th): lo = m1
        else: hi = m2
    return (lo + hi) / 2
err = 0.0
for th in (-1.0, 0.0, 0.4, 1.0, 2.0, 2.9):
    e = e_sym(4, 1.0, 1.0, 1.0, 0.3, th)
    err = max(err, abs(br(e, 4, 1.0, 1.0, 1.0, 0.3, th) - e))
say(f"  Prop 1.3 (2): closed-form symmetric intensity equals the numerical best response (n=4, r=1, l=0.3c), max error {err:.1e}")
def diss_share(n, r, c, l, th):
    return r * (n - 1 - th) * (c + n * l) / (n * (c + (1 + th) * l))
n, r, c, l0 = 4, 1.0, 1.0, 0.3
for th in (-1.0, 0.0, 0.4, 1.0, 2.0, 2.9):
    shares = [diss_share(n, r, c, s * l0, th) for s in (1, 10, 100, 1000)]
    ceil = "unbounded" if th == -1 else f"{r * (n - 1 - th) / (1 + th):.3f}"
    mono = all(shares[k] < shares[k + 1] for k in range(3))
    say(f"  Prop 1.3 (3) theta={th:+.1f}: dissipated share at power s=1,10,100,1000: "
        + ", ".join(f"{x:.3f}" for x in shares) + f"; rising {mono}; ceiling {ceil}")
say(f"  Prop 1.3 (3): total stays positive at every scale iff theta >= (r(n-1)-1)/(1+r) = {(r * (n - 1) - 1) / (1 + r):.3f} (n=4, r=1)")
# total material payoff = Omega - n e (c + n l)
e = e_sym(4, 1.0, 1.0, 1.0, 0.3, 0.4)
say(f"  check: dissipation n e (c+nl) / Omega at theta=0.4, s=1: {4 * e * (1.0 + 4 * 0.3):.4f} vs formula {diss_share(4, 1.0, 1.0, 0.3, 0.4):.4f}")

# Prop 1.4: growth and the boundary
def q_round(a, n, r, Om, c, L, th):
    return a * L * n * e_sym(n, r, Om, c, L, th)
def q_formula(a, n, r, Om, c, L, th):
    return a * r * Om * L * (n - 1 - th) / (n * (c + (1 + th) * L))
say(f"  Prop 1.4: q = a L E equals a r Omega L (n-1-theta)/(n(c+(1+theta)L)): "
    f"{q_round(0.01, 4, 1.0, 5.0, 1.0, 0.3, 0.4):.6f} vs {q_formula(0.01, 4, 1.0, 5.0, 1.0, 0.3, 0.4):.6f}")
def survive(H, a, n, r, c, Om_fn, L_fn, th_fn):
    s = 1.0
    for t in range(1, H + 1):
        q = q_formula(a, n, r, Om_fn(t), c, L_fn(t), th_fn(t))
        if q >= 1: return 0.0
        s *= 1 - q
    return s
a, n, r, c = 0.01, 4, 1.0, 1.0
g = 1.03
cases = (
    ("stakes grow 3%/round, accurate self-model fixed (theta=0.4), L fixed 0.3", lambda t: g ** t, lambda t: 0.3, lambda t: 0.4),
    ("stakes grow 3%/round, gap closes as 2.6 g^-t t^-1.5", lambda t: g ** t, lambda t: 0.3, lambda t: 3 - 2.6 * g ** (-t) * t ** -1.5),
    ("stakes grow 3%/round, gap closes as 2.6/t (slower than stakes grow)", lambda t: g ** t, lambda t: 0.3, lambda t: 3 - 2.6 / t),
    ("stakes grow 3%/round, theta=-1, L fixed 0.3", lambda t: g ** t, lambda t: 0.3, lambda t: -1.0),
    ("stakes grow 3%/round, theta=-1, correction L = 0.3 g^-t t^-1.5", lambda t: g ** t, lambda t: 0.3 * g ** (-t) * t ** -1.5, lambda t: -1.0),
    ("stakes fixed, accurate self-model fixed, L fixed", lambda t: 1.0, lambda t: 0.3, lambda t: 0.4),
    ("stakes grow 3%/round until round 50 and then stop, accurate self-model fixed, L fixed", lambda t: g ** min(t, 50), lambda t: 0.3, lambda t: 0.4),
)
for name, Om_fn, L_fn, th_fn in cases:
    vals = [survive(H, a, n, r, c, Om_fn, L_fn, th_fn) for H in (10, 50, 100, 200, 1000, 10000)]
    say(f"  Prop 1.4 {name}: survival at H=10,50,100,200,1000,10000: " + ", ".join(f"{v:.3g}" for v in vals))

# Prop 1.5: institutions widen the effective self
def th_eff(beta, th0, n):
    return (th0 * (1 - beta) + beta * (1 + th0) * (n - 1) / n) / ((1 - beta) + beta * (1 + th0) / n)
worst = 0.0
for trial in range(2000):
    n = random.randint(2, 6); th0 = random.uniform(-0.99, n - 1.01); beta = random.uniform(0, 0.999)
    pi = [random.uniform(-5, 5) for _ in range(n)]
    pbar = sum(pi) / n
    pp = [(1 - beta) * x + beta * pbar for x in pi]
    O = [pp[i] + th0 * sum(pp[j] for j in range(n) if j != i) / (n - 1) for i in range(n)]
    te = th_eff(beta, th0, n); scale = (1 - beta) + beta * (1 + th0) / n
    Oe = [scale * (pi[i] + te * sum(pi[j] for j in range(n) if j != i) / (n - 1)) for i in range(n)]
    worst = max(worst, max(abs(O[i] - Oe[i]) for i in range(n)))
say(f"  Prop 1.5 (1): pooled objective equals a positive multiple of the objective with theta_eff; max error over 2000 random cases {worst:.1e}")
mono = all(th_eff(b2, th0, 4) > th_eff(b1, th0, 4) for th0 in (-0.9, 0.0, 0.4, 2.0) for b1, b2 in zip([k / 100 for k in range(99)], [k / 100 for k in range(1, 100)]))
say(f"  Prop 1.5 (1): theta_eff strictly rising in beta for theta0 in (-1, n-1): {mono}; theta_eff(1-1e-9, 0, 4) = {th_eff(1 - 1e-9, 0.0, 4):.4f}")
say(f"  Prop 1.5 (1): theta0=-1 gives theta_eff = {[round(th_eff(b, -1.0, 4), 6) for b in (0.0, 0.5, 0.9, 0.99)]}")
for eps in (1.0, 10.0):
    ts = theta_star(4, 1.0, 0.3, 0.2, eps)
    bstar = bisect(lambda b: th_eff(b, 0.0, 4) - ts, 0.0, 0.999)
    say(f"  Prop 1.5 (1) example: isolated self (theta0=0), faithful-AI game n=4 b=1 c=0.3 d=0.2 eps={eps:g}: racing ends once beta > {bstar:.3f}")
bstar = bisect(lambda b: th_eff(b, 0.0, 4) - 1.0, 0.0, 0.999)
say(f"  Prop 1.5 (1) example: contest n=4 r=1, the total stays positive at every scale once beta > {bstar:.3f} (theta_eff >= 1)")

# Prop 1.5 (2): sharing the contested prize (v5.2)
def obj_prize(ei, eo, n, r, Om, c, l, th, beta):
    tot = ei ** r + (n - 1) * eo ** r
    wi = ei ** r / tot; wo = eo ** r / tot
    E = ei + (n - 1) * eo
    pool = beta * Om / n
    pi_i = (1 - beta) * Om * wi + pool - c * ei - l * E
    pi_o = (1 - beta) * Om * wo + pool - c * eo - l * E
    return pi_i + th * pi_o
def br_prize(eo, n, r, Om, c, l, th, beta):
    lo, hi = 1e-9, 10 * Om / c + 1
    for _ in range(200):
        m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
        if obj_prize(m1, eo, n, r, Om, c, l, th, beta) < obj_prize(m2, eo, n, r, Om, c, l, th, beta): lo = m1
        else: hi = m2
    return (lo + hi) / 2
err = 0.0
for th in (-1.0, 0.0, 0.4, 2.0):
    for beta in (0.0, 0.5, 0.9):
        e = (1 - beta) * e_sym(4, 1.0, 1.0, 1.0, 0.3, th)
        err = max(err, abs(br_prize(e, 4, 1.0, 1.0, 1.0, 0.3, th, beta) - e))
say(f"  Prop 1.5 (2): with a share beta of the prize pooled, intensity = (1-beta) e(theta) for theta in (-1,0,0.4,2), beta in (0,.5,.9); max error {err:.1e}")
say(f"  Prop 1.5 (2) example: theta=-1, intensity {e_sym(4,1.0,1.0,1.0,0.3,-1.0):.3f} without sharing, {0.5*e_sym(4,1.0,1.0,1.0,0.3,-1.0):.3f} with half the prize shared")
def pay_field(ei, beta, eo=0.1, n=4, Om=1.0, c=1.0):
    return (1 - beta) * Om * ei / (ei + (n - 1) * eo) - c * ei
for beta in (0.0, 0.5, 0.9):
    say(f"  Prop 1.5 (2) selection: field at 0.1, carrier at 0.2 minus carrier at 0.05, prize shared beta={beta}: {pay_field(0.2, beta) - pay_field(0.05, beta):+.4f}")
nu_g, c_u = 1.0, 0.3
say(f"  Prop 1.5 (2) linear selection model: nu_g={nu_g}, c_u={c_u}: net advantage of load (1-beta)nu_g-c_u changes sign at beta = 1-c_u/nu_g = {1 - c_u / nu_g:.2f}; "
    f"at beta=0.6 {(1 - 0.6) * nu_g - c_u:+.2f}, at beta=0.8 {(1 - 0.8) * nu_g - c_u:+.2f}")

# ------------------------------------------------------------------ AG
say("\n== AG: faithful AI in a harmful human game ==")
def ag_payoffs(n, b, c, d, a):
    out = []
    for i in range(n):
        rel = a[i] - sum(a[j] for j in range(n) if j != i) / (n - 1)
        out.append(b * rel - c * a[i] - d * sum(a))
    return out
for (n, b, c, d) in ((4, 1.0, 0.3, 0.2), (2, 0.6, 0.1, 0.3), (10, 2.0, 0.5, 0.1)):
    dom = all(ag_payoffs(n, b, c, d, [1] + list(rest))[0] - ag_payoffs(n, b, c, d, [0] + list(rest))[0] > 0
              for rest in itertools.product((0, 1), repeat=n - 1))
    allR = ag_payoffs(n, b, c, d, [1] * n)[0]; none = ag_payoffs(n, b, c, d, [0] * n)[0]
    say(f"  n={n} b={b} c={c} d={d}: b>c+d {b > c + d}; racing strictly dominant {dom}; all race {allR:+.3f} "
        f"(= -c-nd {-c - n * d:+.3f}); all restrain {none:+.3f}; sum of objectives at all race {sum(ag_payoffs(n, b, c, d, [1] * n)):+.3f}")

# ------------------------------------------------------------------ CR
say("\n== CR: the chain-rule lemma ==")
def surv(h, N, start=1):
    s = 1.0
    for k in range(start, N + 1): s *= 1 - h(k)
    return s
for name, h in (("h_k = 0.2/k (not summable)", lambda k: 0.2 / k), ("h_k = 0.2/k^2 (summable)", lambda k: 0.2 / k ** 2),
                ("h_k = 0.01 (constant)", lambda k: 0.01)):
    say(f"  {name}: survival to N=10, 100, 1000, 10000: " + ", ".join(f"{surv(h, N):.4f}" for N in (10, 100, 1000, 10000)))
say("  a pause of D rounds that merely delays the same sequence (h_k = 0.01 after the pause): survival to round 1000 after the pause "
    + ", ".join(f"D={D}: {surv(lambda k: 0.0 if k <= D else 0.01, 1000 + D):.4f}" for D in (0, 50, 500)))
say("  a pause that changes the process (h_k = 0.01 before, 0.01/(k-D)^1.5 after): survival to 10000 = "
    f"{surv(lambda k: 0.01 if k <= 20 else 0.01 / (k - 20) ** 1.5, 10000):.4f}")

# ------------------------------------------------------------------ FB
say("\n== FB: the local feedback benchmark ==")
random.seed(3)
ok = 0
for _ in range(20000):
    a, b = random.uniform(0, 2), random.uniform(0, 2)
    mu, de = random.uniform(0.01, 1), random.uniform(0.01, 1)
    lam = 1 - (mu + de) / 2 + math.sqrt((mu - de) ** 2 / 4 + a * b)
    lam2 = 1 - (mu + de) / 2 - math.sqrt((mu - de) ** 2 / 4 + a * b)
    stable = max(abs(lam), abs(lam2)) < 1
    if stable == (a * b < mu * de) or abs(a * b - mu * de) < 1e-9 or lam2 <= -1: ok += 1
say(f"  stability iff ab < mu*delta (where the second root stays above -1): agreement in {ok} of 20000 random draws")

# ------------------------------------------------------------------ HO
say("\n== HO: risk homeostasis as an implicit equilibrium ==")
def br_util(i_self, i_other, n, s, Le, Lc, p0, dpsi):
    sig_s, sig_o = 1 + s * i_self, 1 + s * i_other
    w = sig_s / (sig_s + (n - 1) * sig_o)
    Q = (1 - p0 - dpsi * i_self) * (1 - p0 - dpsi * i_other) ** (n - 1)
    return -Le * (1 - w) - Lc * (1 - Q)
def sym_eq_roots(n, s, Le, Lc, p0, dpsi):
    # interior symmetric FOC: Le*s*(n-1)/(n^2 (1+s i)) = Lc*dpsi*(1-p0-dpsi*i)^(n-1)
    F = lambda i: Le * s * (n - 1) / (n * n * (1 + s * i)) - Lc * dpsi * (1 - p0 - dpsi * i) ** (n - 1)
    grid = [k / 4000 for k in range(4001)]
    roots = []
    for a_, b_ in zip(grid, grid[1:]):
        if F(a_) == 0: roots.append(a_)
        elif (F(a_) > 0) != (F(b_) > 0): roots.append(bisect(F, a_, b_))
    eqs = []
    for r_ in roots:
        best = max(br_util(k / 4000, r_, n, s, Le, Lc, p0, dpsi) for k in range(4001))
        if br_util(r_, r_, n, s, Le, Lc, p0, dpsi) >= best - 1e-9: eqs.append(r_)
    # corner at full delegation
    if max(br_util(k / 4000, 1.0, n, s, Le, Lc, p0, dpsi) for k in range(4001)) <= br_util(1.0, 1.0, n, s, Le, Lc, p0, dpsi) + 1e-12:
        eqs.append(1.0)
    return eqs
for dpsi in (0.95, 0.9, 0.85):
    eqs = sym_eq_roots(2, 100.0, 0.5, 1.0, 0.01, dpsi)
    cells = [f"iota={e:.6f} total risk={1 - (1 - 0.01 - dpsi * e) ** 2:.7f}" for e in eqs]
    say(f"  n=2 s=100 Le=0.5 Lc=1 psi0=0.01 dpsi={dpsi}: symmetric equilibria (global best responses): " + "; ".join(cells))
say("  saturation with summable risk: n=3, Le=Lc=1, psi0=0, s_t=2^t, dpsi_t=2^-t")
tot = 0.0; ok = True
for t in range(5, 60):
    s, dp = 2.0 ** t, 2.0 ** -t
    marg = 2 * s / (9 * (1 + s)) - dp * (1 - dp) ** 2
    ok &= marg > 0
    tot += 1 - (1 - dp) ** 3
say(f"    full delegation is an equilibrium at every t>=5: {ok}; sum of realized risk from t=5: {tot:.4f} (<= 3/16 = 0.1875); "
    f"survival from t=5 >= {1 - tot:.4f}")

# ------------------------------------------------------------------ DL
say("\n== DL: delegation in survival terms ==")
def phi_ND(n, k, s, qL, p0, p1, p=1.0):
    QN = (1 - p0) ** (n - k) * (1 - p1) ** k
    wN = 1 / (n + k * s)            # r=1: own strength 1, k delegators at 1+s, n-1-k others at 1
    PhiN = QN * (wN + (1 - wN) * (1 - p))
    QD = (1 - p0) ** (n - k - 1) * (1 - p1) ** (k + 1)
    wD = (1 + s) / (n + (k + 1) * s)
    PhiD = (1 - qL) * QD * (wD + (1 - wD) * (1 - p))
    return PhiN, PhiD
random.seed(5)
viol = 0
for _ in range(20000):
    n = random.randint(2, 8); k = random.randint(0, n - 1); s = random.uniform(0, 1e4)
    p0 = random.uniform(0, 0.3); p1 = random.uniform(p0, 0.6); p = random.uniform(0, 1)
    PN, PD = phi_ND(n, k, s, 1.0, p0, p1, p)
    if not PN > PD: viol += 1
say(f"  qL=1: not delegating strictly better than delegating in 20000 random (n,k,s,psi,p): violations {viol}")
n, qL, p0, p1 = 2, 0.99, 0.01, 0.05
A = (1 - qL) * (1 - p1) / (1 - p0)
s_allD = (1 / A - 1) * n / (n - 1)
say(f"  qL=0.99, n=2, psi0=0.01, psi1=0.05: all-delegate survival per actor (1-qL)(1-psi1)^n/n = {(1 - qL) * (1 - p1) ** n / n:.7f} for every s; "
    f"all-delegate is an equilibrium only for s >= {s_allD:.2f}")
PN, PD = phi_ND(2, 1, 1.0, 1.0, 0.0, 0.01, 1.0)
say(f"  bounded speed: n=2, s=1, p=qL=1, psi0=0, psi1=0.01, one delegator: the non-delegator's one-contest survival = {PN:.4f}")
say("  ratio Phi_D/Phi_N = (1-qL) a (1+s)(n+ks)/(n+(k+1)s) with a=(1-psi1)/(1-psi0): check at n=3,k=1,s=50,qL=0.5,p=1: "
    f"{phi_ND(3, 1, 50, 0.5, 0.01, 0.05)[1] / phi_ND(3, 1, 50, 0.5, 0.01, 0.05)[0]:.6f} vs "
    f"{0.5 * (0.95 / 0.99) * 51 * (3 + 50) / (3 + 100):.6f}")

# ------------------------------------------------------------------ MM
say("\n== MM: the coverage mismatch theorem ==")
def area_frozen(Yf, U0, slope):
    if U0 >= Yf: return 0.0
    T = (Yf - U0) / slope
    return T - (U0 * T + slope * T * T / 2) / Yf
say(f"  frozen X=2, Y=1, U(tau)=1, slope 1: exposure with Y = {area_frozen(1.0, 1.0, 1.0):.3f}; the v4.5 formula with X gives {area_frozen(2.0, 1.0, 1.0):.3f}")
say("  summable without catch-up: u_t = 1/(t+2)^2 > 0 for every t; with h=0.05 survival to 10^5 = "
    f"{surv(lambda k: 0.05 / (k + 2) ** 2, 100000):.4f}")
def U_burst(t):
    # smooth-ish increasing U with a burst of proportional growth 0.5 over [n^2, n^2+1] for each n, flat otherwise
    logU, n = 0.0, 1
    while n * n <= t:
        logU += 0.5 * min(1.0, t - n * n); n += 1
    return math.exp(logU)
gU = [(U_burst(t + 0.01) - U_burst(t)) / 0.01 / U_burst(t) for t in (100.5, 400.5, 2500.5)]
say(f"  sub-exponential U with bursts: log U(t)/t at t=10^4 = {math.log(U_burst(10000)) / 10000:.4f}; "
    f"g_U inside bursts at t=100.5, 400.5, 2500.5 = {', '.join(f'{g:.3f}' for g in gU)} (does not tend to zero)")
h, eps, T = 0.05, 0.1, 20
say(f"  uniform-gap bound: with h={h}, eps={eps}, survival after T is at most (1-h(1-eps))^(H-T): H=100 -> {(1 - h * (1 - eps)) ** (100 - T):.4f}, H=300 -> {(1 - h * (1 - eps)) ** (300 - T):.6f}")
say("  freeze with Y: build Gamma times the rivals' level, Y = phi*X; exposure is zero when phi*Gamma <= 1: "
    + ", ".join(f"phi={ph}, Gamma={G}: {area_frozen(ph * G * 1.0, 1.0, 0.5):.3f}" for ph, G in ((0.5, 2.0), (0.5, 4.0), (1.0, 2.0))))

# ------------------------------------------------------------------ OV
say("\n== OV: oversight topology ==")
for f, k in ((0.9, 6), (0.8, 3)):
    say(f"  f={f}, k={k}: serial chain (each link must pass the problem on) {f ** k:.6f}; redundant independent checks {1 - (1 - f) ** k:.6f}")
def redundant_common_cause(f, k, rho):
    # with probability rho a common cause defeats every check; otherwise checks independent
    return (1 - rho) * (1 - (1 - f) ** k)
say("  redundant checks with a common cause that defeats all of them with probability rho (f=0.9, k=6): "
    + ", ".join(f"rho={r}: {redundant_common_cause(0.9, 6, r):.4f}" for r in (0.0, 0.05, 0.2)))
say("  a fallible corrector that still lowers risk: base hazard 0.1 per period; corrector blocks 99% and adds residual 2^-(t+2):")
s_base = surv(lambda k: 0.1, 200); s_corr = surv(lambda k: 0.001 + 2.0 ** -(k + 2), 200)
say(f"    survival to 200 without it {s_base:.2e}; with it {s_corr:.4f}")

# ------------------------------------------------------------------ SR
say("\n== SR: one discrete convention for survival ratios ==")
qR, qB = 0.005, 0.05
say(f"  qR={qR}, qB={qB}: exact rate log((1-qR)/(1-qB)) = {math.log((1 - qR) / (1 - qB)):.8f}; small-risk approximation qB-qR = {qB - qR:.3f}")
p_, H = 0.99, 1000
R = math.exp(-0.005 * H); T_, P_, S_ = (1 - p_) * 0.9, (1 - p_) * 0.4, (1 - p_) * 0.1
say(f"  mixed beliefs with cooperative survival tending to zero: H={H}, p={p_}: R={R:.6f}, T={T_:.4f}, P={P_:.4f}, S={S_:.4f}; "
    f"T>R {T_ > R}, P>S {P_ > S_} -> racing dominant at this horizon")
for Hh in (10, 100, 300, 600):
    R = math.exp(-0.005 * Hh); Tb = p_ * math.exp(-0.05 * Hh) + (1 - p_) * 0.9
    say(f"    H={Hh}: R={R:.4f}, mixed T={Tb:.4f}, R-T={R - Tb:+.4f}")

# ------------------------------------------------------------------ FS
say("\n== FS: the finite sprint and prevention as trade-offs ==")
say("  freeze and roll back after a sprint (v4.5's numbers, g=0.3, U=1+0.5t, h=0.05, Y=X): tau=10: freeze 0.531, roll back 0.860 (checks_v45.log, MF)")
say("  prevention compared by hazard rate: sustained prevention 0.01 per period against racing 0.05: "
    + ", ".join(f"H={Hh}: {0.99 ** Hh:.4f} vs {0.95 ** Hh:.4f}" for Hh in (10, 50, 200)))
say(f"  a single strike with Phi_R=1, Phi_P,Phi_S -> 0, sigma=0.7, eps=0.2: Phi_prev = {(1 - 0.2) * 0.7:.2f}")

# ------------------------------------------------------------------ SG
say("\n== SG: a costly signal ==")
def separating(kS, kR, GS, GR):
    return kS <= GS and kR >= GR
for (kS, kR, GS, GR, lab) in ((-0.05, 0.30, 0.40, 0.20, "durable, verifiable E1: costly to mimic"),
                               (-0.05, 0.05, 0.40, 0.20, "reversible E1: cheap to mimic"),
                               (0.10, 0.30, 0.05, 0.20, "E1 too costly for the survival-first type")):
    say(f"  {lab}: k_S={kS}, k_R={kR}, G_S={GS}, G_R={GR} -> separating equilibrium exists: {separating(kS, kR, GS, GR)}")
eps = 0.1
say(f"  near-indifference is not credibility: R=1, T=2eps, P=eps, S=0 with eps={eps}: a sender that will race still gains {eps} from the receiver's cooperation")

# ------------------------------------------------------------------ K7
say("\n== K7: interim incentive compatibility ==")
hmap = {"S": 0.2, "W": -0.8}; pr = {"S": 0.8, "W": 0.2}
for own in ("S", "W"):
    shares = [0.5 + 0.5 * hmap[own] * hmap[o] for o in ("S", "W")]
    exp_share = sum(pr[o] * (0.5 + 0.5 * hmap[own] * hmap[o]) for o in ("S", "W"))
    say(f"  report {own}: ex-post shares against S,W = {shares[0]:.2f}, {shares[1]:.2f}; interim expected share = {exp_share:.3f}")
say(f"  equal shares without a lower value of winning: c_s/c_w=0.05, L_b=0.5, strong outside option {(1.5) * 0.95 - 0.5:.3f}; with S_a=2 the equal share is 1.0")

# ------------------------------------------------------------------ N13
say("\n== N13: the n-player assurance condition ==")
w1 = math.sqrt(0.5)
adv = sum(math.comb(2, k) * (1 - w1) ** k * w1 ** (2 - k) * d for k, d in enumerate((1, -10, -1)))
say(f"  three players, cooperation minus defection by number of other defectors (1, -10, -1); each other cooperates with prob {w1:.4f} "
    f"(all others cooperate with prob 0.5): expected advantage {adv:.4f}")

# ------------------------------------------------------------------ CAP
say("\n== CAP: capture structure ==")
say(f"  fixed split into k=10 parts, eta=1, g=0.2, alpha=0: capture delayed by 2 ln k/(g-(1+eta)alpha) = {2 * math.log(10) / 0.2:.2f}")
for shares in ((1.0,), (0.5, 0.5), (0.25,) * 4, (0.7, 0.1, 0.1, 0.1)):
    say(f"  shares {shares}: HHI {sum(p * p for p in shares):.3f}; third moment sum p^3 (eta=1) {sum(p ** 3 for p in shares):.3f}")
p = [1 / 3] * 3; e = [0.0, 0.9, 1.0]; phi = [0.0, 10.0, 0.0]
pi = [phi[i] + 1.0 * e[i] for i in range(3)]
pbar = sum(p[i] * pi[i] for i in range(3))
Ebar = sum(p[i] * e[i] for i in range(3))
dE = sum(p[i] * (pi[i] - pbar) * e[i] for i in range(3))
cov = sum(p[i] * (e[i] - Ebar) * (phi[i] - sum(p[j] * phi[j] for j in range(3))) for i in range(3))
say(f"  mean load versus the maximal-load share: Cov(e,phi)={cov:.4f}, dE/dt={dE:.4f}, d p_max/dt={p[2] * (pi[2] - pbar):.4f}")
a = 1.0
for om in (0.0, 1.0, 10.0, 100.0):
    num = complex(0, om) - a; den = complex(0, om) + a
    say(f"  control screen: w(s)=2(s-a)/(s+a), |w(j{om})| = {abs(2 * num / den):.3f}" + (f"; w(a) = {2 * (a - a) / (a + a):.1f}" if om == 0 else ""))

# ------------------------------------------------------------------ CMP
say("\n== CMP: two cruxes at common horizons ==")
def path_surv(H, h_unc, u_fn, base, dissolve=0.0, fallback=0.0):
    s = 1.0
    for t in range(1, H + 1):
        s *= 1 - (h_unc * u_fn(t) + base + dissolve * fallback)
    return s
cont_u = lambda t: min(1.0, 0.2 + 0.01 * t)        # uncovered share rising on the continuation path
cont_u_sum = lambda t: 0.2 / t ** 1.2               # continuation that keeps the uncovered share summable
coop_u = lambda t: 0.2 / t ** 1.2                   # cooperative path with catch-up
for H in (10, 30, 100):
    a1 = path_surv(H, 0.05, cont_u, 0.001)
    a2 = path_surv(H, 0.05, cont_u_sum, 0.001)
    b1 = path_surv(H, 0.05, coop_u, 0.001, dissolve=0.02, fallback=0.5)
    b2 = path_surv(H, 0.05, coop_u, 0.001, dissolve=0.002, fallback=0.5)
    say(f"  H={H}: continuation with rising gap {a1:.3f}; continuation with summable gap {a2:.3f}; "
        f"cooperation with dissolution 2%/yr x fallback 0.5 {b1:.3f}; with dissolution 0.2%/yr {b2:.3f}")

with open(os.path.join(here, "checks_v5.log"), "w") as fh:
    fh.write("\n".join(log) + "\n")
