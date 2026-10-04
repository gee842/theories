"""m01  Loop gain and price of standing when rivals respond (Prop 2.2, key `loopgain`; Prop 3.9, key `standprice`).

Claims under test (memo D2-math-opus, item 1):
  (A) In any symmetric (exchangeable) Markov equilibrium with policies differentiable at equal standing, the
      deviation dynamics keep the rank-one form of Prop 2.2, so (1)-(2) hold with r replaced by the EQUILIBRIUM
      decisiveness r_eq = (n^2/(n-1)) dp_i/dln X_i (all policies responding).  [thm; here only illustrated]
  (B) The first-order price of standing is Gpr_d/(1-Gpr_d), where Gpr uses r_pr = (n^2/(n-1)) dp_i/dln X_i with
      the actor's OWN intensity held at its current level and the rivals' intensities at their equilibrium
      policies at the perturbed state (envelope theorem).  [thm; tested here: independent]
  (C) Magnitudes: r_eq, r_pr exceed r near parity in a Tullock contest with effort (discouragement), so structural
      Gamma<1 does not ensure stability; away from parity the laggard's price falls.  [num]
  (D) Static n-player Tullock with weights: r_pr/r = 2(n-1)/n (Fable m2), derived here by the same envelope rule.

Model (n=2).  State s = K1/(K1+K2), total at its steady value.  Each period a lottery: actor 1 wins the contested
part (1-beta)Om with prob p = a1 e1/(a1 e1 + a2 e2), a1 = s^r, a2 = (1-s)^r.  Winnings convert:
  s' = (1-d) s + d [ w((1-beta) W + beta/2) + (1-w)/2 ],  W in {0,1},  w = won share of the stock (omega).
Structural gain Gamma = (1-beta) r w; discounted Gd = Gamma * delta d / (1 - delta (1-d)).
Stage: Tullock with valuations A_i = (1-beta)Om + delta [V_i(win) - V_i(lose)]; p = a1A1/(a1A1+a2A2),
e_i = A_i p (1-p) / (c + l).  Value iteration on a grid; symmetric MPE, V2(s) = V1(1-s).
To approach the local (small-jump) regime the jump d*w*(1-beta) is shrunk with delta = 1/(1+d), which keeps
delta d/(1-delta(1-d)) = 1/2, so Gd = Gamma/2 throughout.
Standard library only.
"""
import math, sys, time

def solve(r=1.0, Gamma=0.6, beta=0.0, d=0.05, delta=None, Om=1.0, c=1.0, l=0.0, N=1200, tol=1e-11, maxit=40000, Lsub=0.0, damp=1.0, V0=None):
    # Lsub > 0 adds a flow term -Lsub (1-s)^2: falling behind costs more than getting ahead gains (concave in standing)
    if delta is None: delta = 1.0 / (1.0 + d)
    w = Gamma / ((1 - beta) * r)
    assert 0 < w <= 1
    jw = d * (w * ((1 - beta) + beta / 2) + (1 - w) / 2)
    jl = d * (w * beta / 2 + (1 - w) / 2)
    grid = [i / N for i in range(N + 1)]
    def I(V, x):
        if x <= 0: return V[0]
        if x >= 1: return V[-1]
        k = int(x * N)
        if k >= N: k = N - 1
        t = x * N - k
        return V[k] + t * (V[k + 1] - V[k])
    def stage(s, V):
        sw = (1 - d) * s + jw; sl = (1 - d) * s + jl
        A1 = (1 - beta) * Om + delta * (I(V, sw) - I(V, sl))
        A2 = (1 - beta) * Om + delta * (I(V, 1 - sl) - I(V, 1 - sw))
        a1 = s ** r if s > 0 else 0.0
        a2 = (1 - s) ** r if s < 1 else 0.0
        A1p = max(A1, 0.0); A2p = max(A2, 0.0)
        den = a1 * A1p + a2 * A2p
        if den == 0: return 0.5, 0.0, 0.0, sw, sl, A1, A2
        p = a1 * A1p / den
        e1 = A1p * p * (1 - p) / (c + l); e2 = A2p * p * (1 - p) / (c + l)
        return p, e1, e2, sw, sl, A1, A2
    V = [0.0] * (N + 1) if V0 is None else [V0(s) for s in grid]
    for it in range(maxit):
        Vn = [0.0] * (N + 1)
        for k, s in enumerate(grid):
            p, e1, e2, sw, sl, _, _ = stage(s, V)
            Vn[k] = (1 - beta) * Om * p + beta * Om / 2 - c * e1 - l * (e1 + e2) - Lsub * (1 - s) ** 2 + delta * (p * I(V, sw) + (1 - p) * I(V, sl))
        diff = max(abs(a - b) for a, b in zip(V, Vn)); V = [a + damp * (b - a) for a, b in zip(V, Vn)]
        if diff < tol: break
    # measurements at parity
    p0, e10, e20, sw0, sl0, A10, _ = stage(0.5, V)
    lam_mpe = delta * (I(V, sw0) - I(V, sl0)) / ((1 - beta) * Om)
    res = dict(it=it, diff=diff, lam_mpe=lam_mpe, e=e10, w=w, jump=jw - jl)
    for hcells in (2, 6, 12):
        h = hcells / N
        pa, e1a, e2a, *_ = stage(0.5 + h, V); pb, e1b, e2b, *_ = stage(0.5 - h, V)
        r_eq = (pa - pb) / (2 * h)                      # dp/ds = (n^2/(n-1)) dp/dln K at s=1/2 for n=2
        def p_ownfixed(s, e2s):
            a1 = s ** r; a2 = (1 - s) ** r
            return a1 * e10 / (a1 * e10 + a2 * e2s)
        r_pr = (p_ownfixed(0.5 + h, e2a) - p_ownfixed(0.5 - h, e2b)) / (2 * h)
        res[f'r_eq_{hcells}'] = r_eq; res[f'r_pr_{hcells}'] = r_pr
        res[f'de2_{hcells}'] = (e2a - e2b) / (2 * h)
    fac = delta * d / (1 - delta * (1 - d))
    Gd = Gamma * fac
    res['lam_struct'] = Gd / (1 - Gd)
    r_pr = res['r_pr_6']; r_eq = res['r_eq_6']
    Gpr_d = (1 - beta) * r_pr * w * fac
    res['Gpr_d'] = Gpr_d
    # envelope: V'(1-delta(1-d)) = r_pr A1 - l de2/ds  =>  lam = [Gpr_d - fac*w*l*de2/ds/((1-beta)Om)] / (1 - Gpr_d)
    res['lam_pred'] = (Gpr_d - fac * w * l * res['de2_6'] / ((1 - beta) * Om)) / (1 - Gpr_d) if Gpr_d < 1 else float('inf')
    res['Geq_d'] = (1 - beta) * r_eq * w * fac
    res['Geq'] = (1 - beta) * r_eq * w
    res['Gpr'] = (1 - beta) * r_pr * w
    # laggard and leader price
    for s in (0.25, 0.75):
        p, e1, e2, sw, sl, *_ = stage(s, V)
        res[f'lam_at_{s}'] = delta * (I(V, sw) - I(V, sl)) / ((1 - beta) * Om)
        res[f'e1_at_{s}'] = e1; res[f'e2_at_{s}'] = e2
    # expected drift path from s=0.52 under the equilibrium (no noise: expected share), and noisy mean |s-1/2|
    s = 0.52
    for t in range(40):
        p, *_ = stage(s, V); s = (1 - d) * s + jl + (jw - jl) * p
    res['s40'] = s
    # global best-response check at parity for actor 1 (grid search over own effort)
    A1 = A10
    def pay(x):
        a1 = 0.5 ** r; a2 = 0.5 ** r
        pp = a1 * x / (a1 * x + a2 * e20) if x + e20 > 0 else 0.5
        return A1 * pp - (c + l) * x
    best = max(pay(e20 * 10 ** (k / 200.0)) for k in range(-600, 601))
    res['br_gap'] = best - pay(e10)
    return res

def static_tullock_factor(n, eps=1e-6):
    """r_pr / r in a static n-player Tullock with weights alpha (strength alpha_i f_i), prize 1, cost 1.
    Own effort held fixed, rivals at their equilibrium efforts for the perturbed weights (closed form for the
    asymmetric Tullock equilibrium, Hillman-Riley/Stein): f_k = (X/alpha_k)(1-(n-1)/(alpha_k Sig)), X = (n-1)/Sig."""
    def eq(alpha):
        Sig = sum(1 / a for a in alpha); X = (n - 1) / Sig
        return [X / a * (1 - (n - 1) / (a * Sig)) for a in alpha]
    f0 = eq([1.0] * n)
    def p_own_fixed(e):
        alpha = [math.exp(e)] + [1.0] * (n - 1)
        f = eq(alpha)
        return alpha[0] * f0[0] / (alpha[0] * f0[0] + sum(alpha[k] * f[k] for k in range(1, n)))
    def p_rel_fixed(e):  # relative perturbation: own up e, others down e/(n-1), all efforts fixed
        alpha = [math.exp(e)] + [math.exp(-e / (n - 1))] * (n - 1)
        return alpha[0] * f0[0] / sum(alpha[k] * f0[k] for k in range(n))
    def p_rel_resp(e):
        alpha = [math.exp(e)] + [math.exp(-e / (n - 1))] * (n - 1)
        f = eq(alpha)
        return alpha[0] * f0[0] / (alpha[0] * f0[0] + sum(alpha[k] * f[k] for k in range(1, n)))
    def p_struct(e):
        alpha = [math.exp(e)] + [1.0] * (n - 1)
        return alpha[0] / sum(alpha)
    dpr = (p_own_fixed(eps) - p_own_fixed(-eps)) / (2 * eps)
    dst = (p_struct(eps) - p_struct(-eps)) / (2 * eps)
    drel_r = (p_rel_resp(eps) - p_rel_resp(-eps)) / (2 * eps)
    drel_f = (p_rel_fixed(eps) - p_rel_fixed(-eps)) / (2 * eps)
    return dpr / dst, drel_r / drel_f

if __name__ == '__main__':
    t0 = time.time()
    print(__doc__.split('\n')[0])
    print("\n(D) static Tullock with weights, own effort fixed, rivals at their equilibrium: r_pr/r (own-only and relative perturbation) vs 2(n-1)/n")
    for n in (2, 3, 4, 6, 10):
        a, b = static_tullock_factor(n)
        print(f"   n={n}: own-only {a:.6f}, relative {b:.6f}, 2(n-1)/n = {2*(n-1)/n:.6f}")
    print("\n(B,C) MPE, n=2, theta0=0, d=0.1, delta=1/1.1 (so Gd = Gamma/2).  Small jumps by large r and small omega")
    print("  (jump = d*omega*(1-beta)); lam_MPE measured from the value function; lam_pred = envelope formula with measured r_pr;")
    print("  struct = Gd/(1-Gd).  Geq_d = (1-beta) r_eq omega delta d/(1-delta(1-d)): the local formula applies only while Geq_d<1.")
    def row(R, tag):
        print(f"  {tag}: jump={R['jump']:.4f} lam_MPE={R['lam_mpe']:.4f} lam_pred={R['lam_pred']:.4f} struct={R['lam_struct']:.4f} "
              f"MPE/struct={R['lam_mpe']/R['lam_struct']:.2f} | r_eq/r={R['r_eq_6']/R['r']:.2f} (h=2,12 cells: {R['r_eq_2']/R['r']:.2f},{R['r_eq_12']/R['r']:.2f}) "
              f"r_pr/r={R['r_pr_6']/R['r']:.2f} | Geq={R['Geq']:.2f} Geq_d={R['Geq_d']:.2f} Gpr_d={R['Gpr_d']:.2f} | lam(.25)={R['lam_at_0.25']:.4f} "
              f"lam(.75)={R['lam_at_0.75']:.4f} | s40={R['s40']:.3f} | BRgap {R['br_gap']:.0e} conv {R['diff']:.0e}", flush=True)
    for G in (0.2, 0.3, 0.4, 0.45, 0.5, 0.6, 0.8):
        R = solve(r=4.0, Gamma=G, d=0.1, N=1500, maxit=5000); R['r'] = 4.0
        row(R, f"r=4 Gamma={G}")
    print("  jump halved (r=8, N=3000):")
    for G in (0.3, 0.6):
        R = solve(r=8.0, Gamma=G, d=0.1, N=3000, maxit=5000); R['r'] = 8.0
        row(R, f"r=8 Gamma={G}")
    print("  shared loss and sharing (r=4, Gamma=0.3):")
    for kw in (dict(l=0.5), dict(beta=0.3)):
        R = solve(r=4.0, Gamma=0.3, d=0.1, N=1500, maxit=5000, **kw); R['r'] = 4.0
        row(R, f"{kw}")
    print("  large jumps, r=1 (the reviewer's regime; local formula not expected to hold):")
    for G in (0.3, 0.6, 0.9):
        R = solve(r=1.0, Gamma=G, d=0.1, N=600, maxit=5000); R['r'] = 1.0
        row(R, f"r=1 Gamma={G}")
    print("\n(E) catch-up: a flow cost Lsub*(1-s)^2 of standing below the top (concave value of standing; r=4, Gamma=0.3/0.6).")
    print("    The price formula (3) is then not the whole price (the flow term adds its own slope), so only r_eq is compared:")
    for Ls in (0.0, 10.0, 100.0):
        for G in (0.3, 0.6):
            R = solve(r=4.0, Gamma=G, d=0.1, N=1500, maxit=5000, Lsub=Ls); R['r'] = 4.0
            print(f"  Lsub={Ls} Gamma={G}: r_eq/r={R['r_eq_6']/4:.3f} r_pr/r={R['r_pr_6']/4:.3f} Geq={R['Geq']:.3f} e1(.25)={R['e1_at_0.25']:.4f} e2(.25)={R['e2_at_0.25']:.4f} "
                  f"(laggard {'tries harder' if R['e1_at_0.25']>R['e2_at_0.25'] else 'gives up'})", flush=True)
    print("\n(F) multiplicity: value iteration from V=0 vs from a step at parity (V0 = 3 sign(s-1/2)); r=4, delta=1/(1+d), damping .5")
    step = lambda s: 3.0 * (1 if s > 0.5 else (-1 if s < 0.5 else 0))
    for (G, d, N) in ((0.2, 0.1, 1500), (0.2, 0.05, 3000), (0.2, 0.05, 6000), (0.3, 0.05, 3000)):
        for init, V0 in (('V=0 ', None), ('step', step)):
            if init == 'V=0 ' and N == 6000: continue
            R = solve(r=4.0, Gamma=G, d=d, N=N, maxit=20000, damp=0.5, V0=V0)
            print(f"  Gamma={G} d={d} N={N} init {init}: lam_MPE={R['lam_mpe']:.4f} (struct {R['lam_struct']:.4f}, x{R['lam_mpe']/R['lam_struct']:.2f}); "
                  f"lam_pred={R['lam_pred']:.4f}; r_eq/r={R['r_eq_6']/4:.2f} (h=12: {R['r_eq_12']/4:.2f}); lam(.25)={R['lam_at_0.25']:.4f}; conv {R['diff']:.0e}", flush=True)
    R = solve(r=4.0, Gamma=0.2, d=0.025, N=4000, maxit=20000, damp=0.5)
    print(f"  finer rounds, smooth branch: Gamma=0.2 d=0.025 N=4000 init V=0: lam_MPE={R['lam_mpe']:.4f} lam_pred={R['lam_pred']:.4f} r_eq/r={R['r_eq_6']/4:.3f}")
    print(f"\n(elapsed {time.time()-t0:.0f}s)")
