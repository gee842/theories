"""m06  How fast independent correction must grow (Prop 4.5, key `corrrate`; Assumption 4.2 `costq`; R3a; Study 2).

Claims under test (memo item 10):
  (A) Part (2) holds for f = 0 only: a positive per-unit cost floor f that falls can stop cultivation although
      correction grows below alpha_ctl/(1+eta) (Codex counterexample).                                  [independent]
  (B) Under [H_f] (f = f0 e^{-alpha_f t}) the level at which cultivation stops, d_f = chi Y/(f p^xi_f), RISES at alpha_f.
      The certificate holds eventually iff alpha_cor > alpha_f, or alpha_cor = alpha_f with no cultivation at the start,
      or alpha_cor >= alpha_ctl/(1+eta) (with a valid start).                                           [independent sweep]
  (C) A lump-sum (true fixed) cost F only delays cultivation: size threshold ~ F^{eta/(2+2eta-xi_v-eta xi_f)}, and no
      cap on the requirement: d* keeps rising as gamma falls (Opus M3).                                  [independent]
  (D) Capacity off its optimum (joint capacity-field simulation, the core of Study 2):
      - sufficiency: alpha_cor >= alpha_ctl/(1+eta) keeps the certificate under every capacity dynamics that moves
        monotonically toward its selected level, from q(0) <= q*(0);                                    [thm; checked]
      - lag q' = kappa(q*-q): failure delayed by eta ln(1+g/kappa)/(alpha_ctl-(1+eta)alpha_cor), g=(alpha_ctl-alpha_cor)/eta;
      - additive selection q' = V dDpi/dq: q <= q0 + V chi Y/(d0 alpha_cor), so ANY alpha_cor > 0 eventually certifies;
      - multiplicative selection q' = V q dDpi/dq: tracks the optimum, the rate law returns;
      - correction resting on human capacity eroded by delegation, d_eff = d (M/M0)^w, M' = -delta_h M: the threshold
        rises by w delta_h.
  (E) After a reform (a temporary rise in d from a captured state), a capacity stock that adjusts slowly makes the
      quasi-static model optimistic: the hold needed to undo capture is longer.                          [independent]
Model: one evaluation domain, x' = zeta x(1-x)(a z - c), z' = eps(A + B q - d z), certificate G = a(A+Bq)/(c d) < 1;
chi = Y = 1, xi_v = 0, a = c = B = 1, A = 0.3, d = d0 e^{alpha_cor t}, gamma = e^{-alpha_ctl t}.
Standard library only.
"""
import math

# ------------------------------------------------------------------------------------------------- (A), (B)
def qstar(chiY, d, f, gamma, eta=1.0, pxf=1.0, pxv=1.0):
    v = (chiY / d - f * pxf) / (gamma * pxv)
    return max(v, 0.0) ** (1 / eta)

def certificate_path(alpha_ctl, alpha_cor, d0, f0, alpha_f, A=0.3, aB=1.0, cev=1.0, eta=1.0, chiY=1.0, T=400.0, dt=0.05):
    fail = None; held_end = None
    t = 0.0
    while t <= T:
        d = d0 * math.exp(alpha_cor * t); g = math.exp(-alpha_ctl * t); f = f0 * math.exp(-alpha_f * t)
        q = qstar(chiY, d, f, g, eta)
        G = (A + aB * q) / (cev * d)
        if G >= 1 and fail is None: fail = t
        held_end = G < 1
        t += dt
    return fail, held_end

def check_A():
    print("(A) Codex: eta=p=chiY=c_ev=a_ev B=1, A=0, gamma=e^{-.2t}, d=2e^{.05t}, f=.49e^{-.01t}")
    rows = []
    for t in (0, 0.25, 0.5, 0.51, 1, 10, 100):
        d = 2 * math.exp(0.05 * t); g = math.exp(-0.2 * t); f = 0.49 * math.exp(-0.01 * t)
        q = qstar(1, d, f, g)
        rows.append(f"t={t}: q*={q:.5f}, G={q/d:.5f}")
    print("   " + "; ".join(rows))
    print(f"   cultivation stops at t = ln(.5/.49)/.04 = {math.log(0.5/0.49)/0.04:.5f}; alpha_cor=.05 < alpha_ctl/(1+eta)=.1, yet the certificate never fails")

def check_B():
    print("(B) [H_f]: d_f(t) = chiY/f(t) rises at alpha_f; eventual certificate vs the corrected rule (alpha_ctl=.2, eta=1, rate law .1)")
    print(f"   d_f(0)={1/0.2:.2f}, d_f(50)={1/(0.2*math.exp(-0.03*50)):.2f} for f0=.2, alpha_f=.03 (V6.1's S4 said this level 'falls')")
    agree = 0; tot = 0; rows = []
    for alpha_f in (0.02, 0.05):
        for alpha_cor in (0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.12):
            for (d0, f0) in ((2.0, 0.1), (2.0, 0.6)):     # d_f(0) = 1/f0 = 10 (> d0: cultivation at start) or 1.67 (< d0: none)
                fail, held = certificate_path(0.2, alpha_cor, d0, f0, alpha_f, T=1500.0, dt=0.25)
                cultivates0 = d0 < 1 / f0
                pred = (alpha_cor > alpha_f) or (alpha_cor == alpha_f and not cultivates0) or (alpha_cor >= 0.1)
                tot += 1; agree += (pred == held)
                if pred != held: rows.append((alpha_f, alpha_cor, d0, f0, held))
    print(f"   eventual certificate predicted by [alpha_cor > alpha_f, or = with no initial cultivation, or >= alpha_ctl/(1+eta)] in {agree} of {tot}; mismatches {rows}")
    fail, held = certificate_path(0.2, 0.05, 2.0, 0.1, 0.05, T=1500.0, dt=0.05)
    print(f"   Opus's case alpha_cor = alpha_f = .05 with cultivation at the start (f0=.1): fails at t={fail:.1f}, held at the end: {held}")
    fail, held = certificate_path(0.2, 0.05, 2.0, 0.6, 0.05, T=1500.0, dt=0.05)
    print(f"   same rates with no cultivation at the start (f0=.6, d0 > d_f(0)): first failure {fail}, held at the end: {held}")

# ------------------------------------------------------------------------------------------------- (C)
def lump_sum_q(chiY, d, F, gamma, p, eta, xi_v, xi_f):
    # cultivation pays iff max_q [chiY p^2 q/d - gamma p^xi_v q^(1+eta)/(1+eta)] > F p^xi_f
    Yp = chiY * p * p
    q = (Yp / (d * gamma * p ** xi_v)) ** (1 / eta)
    gain = Yp * q / d - gamma * p ** xi_v * q ** (1 + eta) / (1 + eta)
    return q if gain > F * p ** xi_f else 0.0

def check_C():
    print("(C) a lump-sum fixed cost F p^xi_f: size threshold exponent (numerical, by bisection on p) and the requirement d*")
    for (eta, xi_v, xi_f) in ((1, 0, 0), (1, 1, 0), (2, 0, 0.5), (0.5, 0.3, 1)):
        ps = []
        for F in (1e-4, 1e-6):
            lo, hi = 1e-9, 1.0
            for _ in range(200):
                mid = math.sqrt(lo * hi)
                if lump_sum_q(1.0, 1.0, F, 1.0, mid, eta, xi_v, xi_f) > 0: hi = mid
                else: lo = mid
            ps.append(hi)
        expo = math.log(ps[0] / ps[1]) / math.log(1e-4 / 1e-6)
        print(f"   eta={eta} xi_v={xi_v} xi_f={xi_f}: threshold exponent in F {expo:.4f}; eta/(2+2eta-xi_v-eta xi_f) = {eta/(2+2*eta-xi_v-eta*xi_f):.4f};"
              f" per-unit floor gives 1/(2-xi_f) = {1/(2-xi_f):.4f}")
    print("   requirement d*(gamma) with A=0, B=1, p=1, eta=1: lump-sum F=0.3 vs per-unit floor f=0.3")
    for gam in (1e-2, 1e-4, 1e-6, 1e-8):
        # d* solves (A + B q(d))/d = 1, by bisection on d
        def G_lump(d): return lump_sum_q(1.0, d, 0.3, gam, 1.0, 1, 0, 0) / d
        def G_unit(d): return qstar(1.0, d, 0.3, gam) / d
        out = []
        for Gf in (G_lump, G_unit):
            lo, hi = 1e-6, 1e9
            for _ in range(300):
                mid = math.sqrt(lo * hi)
                if Gf(mid) >= 1: lo = mid
                else: hi = mid
            out.append(hi)
        print(f"   gamma={gam:.0e}: d* lump-sum {out[0]:.2f}; d* per-unit floor {out[1]:.4f} (levels off at chiY/f = {1/0.3:.4f})")

# ------------------------------------------------------------------------------------------------- (D), (E)
def joint(alpha_cor, dyn='QS', kappa=0.1, V=1.0, T=400.0, dt=0.01, alpha_ctl=0.2, d0=2.0, A=0.3, eps=0.5, zeta=1.0,
          x0=0.01, q0=None, w=0.0, delta_h=0.0):
    """Returns (first certificate failure time, capture time x>1/2, final x, final G).  Exact steps for the linear
    pieces (stiff when d is large): z relaxes exponentially to (A+q)/d; logit x moves at zeta (a z - c);
    capacity: lag and additive dynamics are linear in q (additive = lag with rate V*gamma, which falls as control cheapens),
    multiplicative is logistic."""
    t = 0.0
    q = 0.5 if q0 is None else q0           # q*(0) = 1/(gamma d) at eta=1 = 0.5
    z = A / d0
    u = math.log(x0 / (1 - x0)); fail = None; cap = None
    while t < T:
        d = d0 * math.exp(alpha_cor * t)
        if w: d *= math.exp(-w * delta_h * t)        # human capacity eroded by delegation
        g = math.exp(-alpha_ctl * t)
        qs = 1.0 / (g * d)
        if dyn == 'QS': q = qs
        elif dyn == 'lag': q = qs + (q - qs) * math.exp(-kappa * dt)
        elif dyn == 'add': q = qs + (q - qs) * math.exp(-V * g * dt)
        elif dyn == 'mult': q = qs / (1 + (qs / q - 1) * math.exp(-V * dt / d))
        G = (A + q) / d
        if G >= 1 and fail is None: fail = t
        zs = (A + q) / d
        z = zs + (z - zs) * math.exp(-eps * d * dt)
        u += dt * zeta * (z - 1.0)
        if u > 0 and cap is None: cap = t
        t += dt
    x = 1 / (1 + math.exp(-u)) if u > -700 else 0.0
    return fail, cap, x, (A + q) / d

def check_D():
    print("(D) capacity off its optimum, joint with the evaluation domain (alpha_ctl=.2, eta=1: rate law .1)")
    fmt = lambda v: '   never' if v is None else f"{v:8.1f}"
    print("   alpha_cor | dynamics           | cert. fails | captured (x>1/2) | final G")
    for ac in (0.05, 0.09, 0.1, 0.12):
        for (dyn, kw, tag) in (('QS', {}, 'quasi-static      '), ('lag', dict(kappa=0.1), 'lag kappa=.1      '), ('lag', dict(kappa=0.03), 'lag kappa=.03     '),
                               ('add', dict(V=1.0), 'additive V=1      '), ('add', dict(V=100.0), 'additive V=100    '), ('mult', dict(V=1.0), 'multiplicative V=1')):
            f, c, x, G = joint(ac, dyn, **kw)
            print(f"   {ac:9.2f} | {tag} | {fmt(f)}    | {fmt(c)}         | {G:.3g}")
    # lag delay formula
    print("   lag delay vs eta ln(1+g/kappa)/(alpha_ctl-(1+eta)alpha_cor):")
    for (ac, kap) in ((0.05, 0.1), (0.05, 0.03), (0.02, 0.1)):
        fq, *_ = joint(ac, 'QS', T=600.0); fl, *_ = joint(ac, 'lag', kappa=kap, T=600.0)
        g = (0.2 - ac); pred = math.log(1 + g / kap) / (0.2 - 2 * ac)
        print(f"      alpha_cor={ac} kappa={kap}: simulated delay {fl-fq:.2f}, formula {pred:.2f} (asymptotic; exact once both fail in the exponential regime)")
    # additive bound
    for ac in (0.01, 0.03):
        f, c, x, G = joint(ac, 'add', V=1.0, T=1500.0)
        print(f"   additive selection, alpha_cor={ac} (far below .1): failure {f}, final G {G:.3g} (bound q <= q0 + V/(d0 alpha_cor) = {0.5+1/(2*ac):.1f})")
    # human capacity
    print("   correction resting on human capacity eroded by delegation (w=1): quasi-static certificate eventually held?")
    for dh in (0.0, 0.05, 0.1):
        res = []
        for ac in (0.1, 0.12, 0.15, 0.2, 0.22):
            f, c, x, G = joint(ac, 'QS', w=1.0, delta_h=dh, T=800.0)
            res.append(f"{ac}:{'held' if G < 1 else 'fails'}")
        print(f"      delta_h={dh}: threshold predicted {0.1+dh:.2f}; " + ", ".join(res))

def check_E():
    print("(E) reversal in a self-sustaining domain (conversion from its own share, z' = eps((A+q)x - d z): bistable when G>1).")
    print("    From capture at d1, raise d to d2 for a hold T, then return to d1. Minimal T to undo capture (x -> 0).")
    d1, d2, alpha_ctl = 0.9, 1.5, 0.0     # stationary cost of control; captured state with q at its optimum q* = 1/(gamma d)
    def undone(T, dyn, kappa):
        # start captured: x ~ 1, z at its steady level, q at q*(d1)
        q = 1.0 / d1; z = (0.3 + q) / d1; u = math.log((1 - 1e-6) / 1e-6); t = 0.0; dt = 0.01
        while t < T + 400.0:
            d = d2 if t < T else d1
            qs = 1.0 / d
            if dyn == 'QS': q = qs
            else: q = qs + (q - qs) * math.exp(-kappa * dt)
            x = 1 / (1 + math.exp(-u)) if u > -700 else 0.0
            zs = (0.3 + q) * x / d
            z = zs + (z - zs) * math.exp(-0.5 * d * dt)
            u += dt * 1.0 * (z - 1.0)
            t += dt
        return u < 0
    out = {}
    for (dyn, kap) in (('QS', None), ('lag', 0.1), ('lag', 0.03)):
        lo, hi = 0.0, 400.0
        if not undone(hi, dyn, kap): out[(dyn, kap)] = None; continue
        for _ in range(40):
            mid = (lo + hi) / 2
            if undone(mid, dyn, kap): hi = mid
            else: lo = mid
        out[(dyn, kap)] = hi
    qs = out[('QS', None)]
    for k, v in out.items():
        if v is None: print(f"   {k}: not undone by any hold up to 400"); continue
        print(f"   {k}: minimal hold {v:.2f}" + (f"  (+{100*(v/qs-1):.0f}% over quasi-static)" if qs and k[0] != 'QS' else ''))
    print(f"   G at d1 = {(0.3+1/d1)/d1:.2f} (captured), at d2 = {(0.3+1/d2)/d2:.2f}")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A(); print(); check_B(); print(); check_C(); print(); check_D(); print(); check_E()
