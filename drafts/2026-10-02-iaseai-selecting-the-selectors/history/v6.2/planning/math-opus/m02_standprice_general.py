"""m02  Compounding prices standing: the general form (Prop 3.9, key `standprice`; Prop 2.2(3), key `loopgain`).

Claims under test (memo item 2):
  (A) With a prize that depends on total stocks, a relative unit of net payoff is worth Grel_d/(1-Grel_d) of own future
      winnings and a common unit Gcom_d/(1-Gcom_d), where
         Grel_d = (1-beta) sum_j r_j kappa_j (Omega/S_j) delta / (1 - delta(1 - d_j - df_j))      [= Gamma_delta of Prop 2.2]
         Gcom_d = sum_j kappa_j g_j delta / (1 - delta(1 - d_j)),   g_j = dOmega/dS_j,
      at a symmetric steady state, and on a balanced-growth path when Omega is proportional to capacity.
      Tested by direct nonlinear simulation of the stock model (others' conduct fixed). [independent]
  (B) The working objective: (1+theta)/(n-1-theta) = (1+theta0)/(n-1-theta0) * (1-Grel_d)/(1-Gcom_d).
      Two-period strategic version: directly computed symmetric first-period equilibrium intensity vs e(theta).
      [independent of the formula, but first order by construction at a symmetric point: an algebra check]
  (C) Narrowing iff Grel_d > Gcom_d.  With Omega proportional to capacity and no provision or diffusion,
      Grel_d/Gcom_d = (1-beta) r, so the objective narrows exactly where equal shares are unstable. [independent sim]
  (D) Domain.  If Grel_d >= 1 (equivalently delta*m_rel >= 1, m_rel the per-period growth of a relative deviation),
      the first-order price is infinite: the value of standing has a cusp at parity, PV(eps) ~ eps^a with
      a = ln(1/delta)/ln(m_rel) < 1.  [independent sim; Codex case n=2, r=2, d=.2, delta=.9]
  (E) Test Gamma's observable: the ratio of intensity's response to shared loss and to private cost is 1+theta. [independent]
Standard library only.
"""
import math

# ---------------------------------------------------------------- the stock model with a prize that depends on totals
def simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, bump, T=4000):
    """Present value of carrier 0's winnings over t=1..T, starting from stocks X0 + bump (bump applied at t=0, i.e.
    counts from next period's winnings).  One stock per carrier, strength r ln X.  Others' conduct fixed (mechanical)."""
    X = [x + b for x, b in zip(X0, bump)]
    pv = 0.0; disc = 1.0
    for t in range(1, T + 1):
        S = sum(X); Om = Om_fun(S)
        w = [x ** r for x in X]; W = sum(w)
        p = [wi / W for wi in w]
        win0 = Om * ((1 - beta) * p[0] + beta / n)
        disc *= delta
        pv += disc * win0
        mean = S / n
        X = [(1 - d) * x + kap * Om * ((1 - beta) * pi + beta / n) + k0 - df * (x - mean) for x, pi in zip(X, p)]
    return pv

def steady(n, kap, d, k0, Om0, g):
    # dS = kap(Om0 + g S) + n k0  =>  S* = (kap Om0 + n k0)/(d - kap g)
    S = (kap * Om0 + n * k0) / (d - kap * g)
    return S

def check_A():
    print("(A) prices of a relative and a common unit, nonlinear simulation vs closed forms (others' conduct fixed)")
    cases = [  # n, r, kap, d, df, k0, beta, Om0, g, delta
        (2, 1.5, 0.5, 0.2, 0.0, 0.1, 0.0, 1.0, 0.0, 0.9),      # fixed prize: Gcom = 0
        (2, 1.5, 0.5, 0.2, 0.0, 0.1, 0.0, 1.0, 0.2, 0.9),      # prize grows with capacity, stationary total
        (3, 1.2, 0.4, 0.15, 0.05, 0.05, 0.2, 2.0, 0.15, 0.95),  # with diffusion, sharing, provision
        (4, 0.8, 0.6, 0.1, 0.02, 0.0, 0.1, 1.0, 0.1, 0.9),
        (5, 2.0, 0.3, 0.25, 0.1, 0.2, 0.0, 3.0, 0.5, 0.85),
    ]
    worst = 0.0
    for (n, r, kap, d, df, k0, beta, Om0, g, delta) in cases:
        Om_fun = lambda S, Om0=Om0, g=g: Om0 + g * S
        S = steady(n, kap, d, k0, Om0, g); X0 = [S / n] * n
        Om = Om_fun(S)
        a = (1 - beta) * r * kap * Om / S
        Grel = delta * a / (1 - delta * (1 - d - df))
        Gcom = delta * kap * g / (1 - delta * (1 - d))
        lam_rel = Grel / (1 - Grel); lam_com = Gcom / (1 - Gcom)
        eps = 1e-5 * S / n
        # a relative unit y of net payoff: own stock +kap*y, others -kap*y/(n-1); a common unit: all +kap*y
        y = eps
        up = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [kap * y] + [-kap * y / (n - 1)] * (n - 1))
        dn = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [-kap * y] + [kap * y / (n - 1)] * (n - 1))
        sim_rel = (up - dn) / (2 * y)
        up = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [kap * y] * n)
        dn = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [-kap * y] * n)
        sim_com = (up - dn) / (2 * y)
        e1 = abs(sim_rel / lam_rel - 1); e2 = abs(sim_com - lam_com) / max(lam_com, 1e-12) if lam_com > 0 else abs(sim_com)
        worst = max(worst, e1, e2 if lam_com > 0 else 0)
        print(f"   n={n} r={r} kap={kap} d={d} df={df} k0={k0} beta={beta} Om=({Om0}+{g}S) delta={delta}: Grel_d={Grel:.4f} Gcom_d={Gcom:.4f} | "
              f"relative: sim {sim_rel:.6f} formula {lam_rel:.6f} | common: sim {sim_com:.6f} formula {lam_com:.6f}")
    # balanced growth: Omega = g S, no provision; growth factor G = 1-d+kap g (must have delta G < 1)
    for (n, r, kap, d, df, beta, g, delta) in [(2, 1.5, 0.5, 0.1, 0.0, 0.0, 0.3, 0.9), (3, 0.8, 0.5, 0.1, 0.0, 0.0, 0.3, 0.9),
                                              (3, 1.3, 0.5, 0.1, 0.05, 0.1, 0.3, 0.88)]:
        Om_fun = lambda S, g=g: g * S
        X0 = [1.0] * n
        a = (1 - beta) * r * kap * g
        Grel = delta * a / (1 - delta * (1 - d - df)); Gcom = delta * kap * g / (1 - delta * (1 - d))
        lam_rel = Grel / (1 - Grel); lam_com = Gcom / (1 - Gcom)
        y = 1e-6
        up = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [kap * y] + [-kap * y / (n - 1)] * (n - 1), T=3000)
        dn = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [-kap * y] + [kap * y / (n - 1)] * (n - 1), T=3000)
        sim_rel = (up - dn) / (2 * y)
        up = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [kap * y] * n, T=3000)
        dn = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [-kap * y] * n, T=3000)
        sim_com = (up - dn) / (2 * y)
        if Grel < 1: worst = max(worst, abs(sim_rel / lam_rel - 1), abs(sim_com / lam_com - 1))
        print(("   OUTSIDE THE DOMAIN (Grel_d>=1; the relative formula does not apply, see D): " if Grel >= 1 else "   ") + f"balanced growth n={n} r={r} df={df} beta={beta} Om={g}S (growth {1-d+kap*g:.3f}/period): Grel_d={Grel:.4f} Gcom_d={Gcom:.4f} | "
              f"relative: sim {sim_rel:.6f} formula {lam_rel:.6f} | common: sim {sim_com:.6f} formula {lam_com:.6f}")
    print(f"   largest relative error inside the domain {worst:.1e}")

# ---------------------------------------------------------------- (B) two-period strategic check
def golden(fn, lo, hi, it=120):
    gr = (math.sqrt(5) - 1) / 2; x1 = hi - gr * (hi - lo); x2 = lo + gr * (hi - lo); f1, f2 = fn(x1), fn(x2)
    for _ in range(it):
        if f1 < f2: lo = x1; x1 = x2; f1 = f2; x2 = lo + gr * (hi - lo); f2 = fn(x2)
        else: hi = x2; x2 = x1; f2 = f1; x1 = hi - gr * (hi - lo); f1 = fn(x1)
    return (lo + hi) / 2

def two_period(n, th0, Om1, c, ell, K0, kap, Om20, g, r, delta):
    def objective(i, es):
        E = sum(es)
        pis = [Om1 * es[j] / E - c * es[j] - ell * E for j in range(n)]
        Ks = [K0 + kap * p for p in pis]
        S = sum(Ks); Om2 = Om20 + g * S
        w = [k ** r for k in Ks]; Wt = sum(w)
        W2 = [Om2 * x / Wt for x in w]
        oth = lambda v: (sum(v) - v[i]) / (n - 1)
        return pis[i] + th0 * oth(pis) + delta * (W2[i] + th0 * oth(W2))
    e = 0.1
    for _ in range(300):
        en = golden(lambda x: objective(0, [x] + [e] * (n - 1)), 1e-7, 2.0)
        if abs(en - e) < 1e-12: break
        e = 0.5 * e + 0.5 * en
    # formula
    pibar = Om1 / n - c * e - ell * n * e; Kb = K0 + kap * pibar
    Om2 = Om20 + g * n * Kb
    lam_rel = delta * Om2 * r * kap / (n * Kb)
    lam_com = delta * g * kap
    rho = (1 + th0) * (1 + lam_com) / ((n - 1 - th0) * (1 + lam_rel))
    th = (rho * (n - 1) - 1) / (1 + rho)
    e_form = Om1 * (n - 1 - th) / (n * n * (c + (1 + th) * ell))
    # formula ignoring the common channel (Prop 3.9 of V6.1, g taken as zero)
    rho0 = (1 + th0) / ((n - 1 - th0) * (1 + lam_rel)); th_old = (rho0 * (n - 1) - 1) / (1 + rho0)
    e_old = Om1 * (n - 1 - th_old) / (n * n * (c + (1 + th_old) * ell))
    return e, e_form, e_old, th, th_old, lam_rel, lam_com

def check_B():
    print("(B) two-period contest, net payoffs convert to capacity, period-2 prize Om20 + g*sum(K): direct symmetric equilibrium e*")
    print("    vs e(theta) with the general form, and vs e(theta) of the fixed-prize formula (9)")
    for kw in [dict(g=0.0), dict(g=0.3), dict(g=0.6, Om20=0.0), dict(g=0.6, Om20=0.0, r=0.7), dict(g=0.6, Om20=0.0, r=1.4), dict(g=0.3, th0=1.0, n=4)]:
        base = dict(n=3, th0=0.5, Om1=1.0, c=1.0, ell=0.2, K0=1.0, kap=0.5, Om20=1.0, g=0.0, r=1.0, delta=0.9); base.update(kw)
        e, ef, eo, th, tho, lr, lc = two_period(**base)
        print(f"   {kw}: e*={e:.7f} e(theta_general)={ef:.7f} [theta={th:+.4f}; lam_rel={lr:.4f} lam_com={lc:.4f}] e(theta_fixedprize)={eo:.7f} [theta={tho:+.4f}]"
              f" | narrows: {th < base['th0']}")

# ---------------------------------------------------------------- (C) narrowing vs share instability under balanced growth
def share_unstable(n, r, kap, d, df, beta, g, T=600):
    X = [1.0 + 1e-6] + [1.0 - 1e-6 / (n - 1)] * (n - 1)
    dev0 = None
    for t in range(T):
        S = sum(X); Om = g * S
        w = [x ** r for x in X]; W = sum(w)
        X = [(1 - d) * x + kap * Om * ((1 - beta) * wi / W + beta / n) - df * (x - S / n) for x, wi in zip(X, w)]
        S = sum(X); X = [x / S * n for x in X]     # renormalize (shares are what matter)
    return abs(X[0] - 1) > 1e-6

def check_C():
    print("(C) prize proportional to capacity: narrowing (Grel_d>Gcom_d) vs instability of equal shares (simulated)")
    agree = disagree = 0; examples = []
    for r in (0.5, 0.8, 0.95, 1.05, 1.17, 1.2, 1.6, 2.5):
        for beta in (0.0, 0.2, 0.4):
            for df in (0.0, 0.03):
                n, kap, d, g, delta = 3, 0.5, 0.1, 0.3, 0.9
                a = (1 - beta) * r * kap * g
                Grel = delta * a / (1 - delta * (1 - d - df)); Gcom = delta * kap * g / (1 - delta * (1 - d))
                narrows = Grel > Gcom
                unstable = share_unstable(n, r, kap, d, df, beta, g)
                if df == 0.0:
                    if narrows == unstable: agree += 1
                    else: disagree += 1; examples.append((r, beta))
                elif narrows != unstable and len(examples) < 12:
                    examples.append(('with diffusion', r, beta, 'narrows' if narrows else 'widens', 'unstable' if unstable else 'stable'))
    print(f"   no diffusion: narrowing and instability coincide in {agree} of {agree+disagree} cases; (1-beta)r>1 decides both")
    print(f"   cases where they part (only with diffusion expected): {examples}")
    # stationary total (Om0>0): a band in which the objective narrows while equal standing is stable
    n, r, kap, d, df, k0, beta, Om0, g, delta = 3, 1.5, 0.5, 0.2, 0.0, 0.1, 0.0, 1.0, 0.0, 0.9
    S = steady(n, kap, d, k0, Om0, g); Om = Om0 + g * S
    a = (1 - beta) * r * kap * Om / S
    Gam = a / (d + df)
    print(f"   stationary total, fixed prize (n=3, r=1.5, k0=0.1): Gamma={Gam:.3f} (<1, equal standing stable) while Gcom_d=0 < Grel_d: the objective narrows")

# ---------------------------------------------------------------- (D) the domain: a cusp beyond Gd=1
def check_D():
    print("(D) beyond the domain: Codex case n=2, kap*Om=1, d=0.2, r=2, no provision/diffusion, delta=0.9 (Gamma=2, Gd=9/7)")
    n, r, kap, d, df, k0, beta, delta = 2, 2.0, 1.0, 0.2, 0.0, 0.0, 0.0, 0.9
    Om_fun = lambda S: 1.0
    S = 1.0 / d; X0 = [S / 2, S / 2]
    m = 1 - d - df + (1 - beta) * r * kap * 1.0 / S
    alpha = math.log(1 / delta) / math.log(m)
    base = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [0, 0], T=1500)
    rows = []
    for k in range(2, 11, 2):
        eps = 10.0 ** (-k)
        pv = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [eps, -eps], T=1500) - base
        rows.append((eps, pv))
    print(f"   m_rel = {m:.3f}, delta*m_rel = {delta*m:.3f}; predicted exponent ln(1/delta)/ln(m_rel) = {alpha:.4f}")
    for (e1, p1), (e2, p2) in zip(rows, rows[1:]):
        print(f"   eps {e1:.0e}: PV {p1:.6e}, PV/eps {p1/e1:.3e}; fitted exponent to next: {math.log(p2/p1)/math.log(e2/e1):.4f}")
    print("   printed multiplier Gd/(1-Gd) =", round((9 / 7) / (1 - 9 / 7), 3), "(negative, meaningless); the true marginal value diverges as eps->0")
    # inside the domain the exponent is 1 and PV/eps tends to the formula
    delta = 0.8
    fac = delta * d / (1 - delta * (1 - d)); Gd = 2 * fac
    base = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [0, 0], T=1500)
    pv = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [1e-6, -1e-6], T=1500) - base
    # a relative unit y of net payoff raises own stock by kap*y: here bump 1e-6 on own stock, -1e-6 on the other = deviation 1e-6
    print(f"   inside the domain but above Gamma=1 (delta=0.8, Gd={Gd:.4f}, m_rel=1.2, delta*m_rel=0.96): formula Gd/(1-Gd)/kap = {Gd/(1-Gd)/kap:.6f}; PV/eps:")
    for k in (4, 6, 8, 10, 12):
        eps = 10.0 ** (-k)
        pv = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [eps, -eps], T=1500) - base
        print(f"      eps 1e-{k}: {pv/eps:.6f}  (gap to formula {Gd/(1-Gd)/kap - pv/eps:.2e}; predicted to shrink like eps^{-math.log(delta*m)/math.log(m):.3f})")
    # boundary delta*m = 1 exactly: PV/eps grows like log(1/eps)
    delta = 1 / m
    base = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [0, 0], T=3000)
    out = []
    for k in (3, 5, 7, 9):
        eps = 10.0 ** (-k)
        pv = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [eps, -eps], T=3000) - base
        out.append(f"eps 1e-{k}: PV/eps {pv/eps:.2f}")
    print(f"   at the boundary delta*m_rel = 1: {'; '.join(out)}  (grows by a constant per decade: logarithmic)")

# ---------------------------------------------------------------- (E) the observable of Test Gamma
def contest_eq(n, theta, Om, c, ell, r=1.0):
    # numerical symmetric equilibrium of the static contest with objective J = pi_i + theta*mean(others' pi)
    def J(x, e):
        E = x + (n - 1) * e
        w = x ** r / (x ** r + (n - 1) * e ** r)
        pi_i = Om * w - c * x - ell * E
        pi_o = Om * (1 - w) / (n - 1) - c * e - ell * E
        return pi_i + theta * pi_o
    e = 0.1
    for _ in range(300):
        en = golden(lambda x: J(x, e), 1e-9, 5.0)
        if abs(en - e) < 1e-13: break
        e = 0.5 * e + 0.5 * en
    return e

def check_E():
    print("(E) Test Gamma's observable: (de/d ell)/(de/dc) from numerical equilibria vs 1+theta")
    for (n, th) in ((2, -0.5), (3, 0.0), (4, -0.43), (4, 1.0)):
        h = 1e-4; Om, c, ell = 1.0, 1.0, 0.3
        dl = (contest_eq(n, th, Om, c, ell + h) - contest_eq(n, th, Om, c, ell - h)) / (2 * h)
        dc = (contest_eq(n, th, Om, c + h, ell) - contest_eq(n, th, Om, c - h, ell)) / (2 * h)
        print(f"   n={n} theta={th}: ratio {dl/dc:.5f}, 1+theta {1+th:.5f}")
    print("   so the registered observable is 1+theta, which RISES with provision (provision lowers Grel_d) - the sign Test Gamma must use")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A(); print(); check_B(); print(); check_C(); print(); check_D(); print(); check_E()
