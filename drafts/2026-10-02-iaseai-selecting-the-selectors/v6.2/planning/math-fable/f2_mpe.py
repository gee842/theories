"""f2: the price of standing and the stability of equal standing when rivals respond to the state
(Markov-perfect equilibrium of the stochastic compounding contest).  Independent implementation; not the
reviewers' scripts.

Model (the paper's compounding contest with intensity).  Two actors; total capacity held at its steady value
S* so the state is s = K_1/S*.  Each period a contested prize (1-beta)*Om goes to actor 1 with probability
p = a1 e1/(a1 e1 + a2 e2), a_i = K_i^r (lottery: the state jumps); beta*Om is split equally.  Winnings convert
at rate kappa; k0 is provision; depreciation d; shared loss l per unit of total intensity; cost c; discount
delta; theta_0 = 0.  Effort is chosen each period given the state (MPE, value iteration, closed-form stage
equilibrium for given continuation values).

Quantities at parity s = 1/2:
  lambda_formula = Gd/(1-Gd), Gd = Gamma delta d/(1-delta(1-d))         (Prop 2.2(3), others fixed)
  lambda_MPE     = delta [V(s_win)-V(s_lose)] / ((1-beta) Om)            (equilibrium price of a relative unit)
  p'_eq  = d p_eq/ds  (full equilibrium elasticity, both efforts respond)       -> Gamma_eq = (1-beta) omega p'_eq
  p~'    = dp/ds with OWN effort fixed and the rival responding (envelope)     -> Gamma~  = (1-beta) omega p~'
Derivation (memo D2, item 2): with small jumps and l = 0, the equilibrium price is the closed-loop gain of
the PARTIAL-equilibrium loop, lambda_MPE ~ Gd~/(1-Gd~), Gd~ = Gamma~ delta d/(1-delta(1-d)); the stability of
the expected deviation at parity is decided by the FULL equilibrium gain, multiplier 1 + d(Gamma_eq - 1).
The two gains coincide when strategies are fixed, and differ by the own-response term otherwise.  Tested below.
"""
import math, random

def solve(r, Gamma, beta=0.0, Om=1.0, kap=0.5, d=0.2, c=1.0, l=0.0, delta=0.9, N=400, tol=1e-11, maxit=40000):
    om = Gamma / ((1 - beta) * r)
    assert om <= 1.0
    k0 = kap * Om * (1 / om - 1) / 2
    S = (kap * Om + 2 * k0) / d
    jw = (kap * Om * ((1 - beta) + beta / 2) + k0) / S     # jump of s on winning (before decay)
    jl = (kap * Om * beta / 2 + k0) / S                    # on losing
    grid = [i / N for i in range(N + 1)]
    def interp(V, x):
        if x <= 0: return V[0]
        if x >= 1: return V[-1]
        k = min(int(x * N), N - 1); w = x * N - k
        return V[k] * (1 - w) + V[k + 1] * w
    def nxt(s): return (1 - d) * s + jw, (1 - d) * s + jl
    def stage(s, V, e1_fixed=None):
        sw, sl = nxt(s)
        A1 = (1 - beta) * Om + delta * (interp(V, sw) - interp(V, sl))
        A2 = (1 - beta) * Om + delta * (interp(V, 1 - sl) - interp(V, 1 - sw))
        a1 = s ** r if s > 0 else 0.0; a2 = (1 - s) ** r if s < 1 else 0.0
        A1p, A2p = max(A1, 0.0), max(A2, 0.0)
        if a1 * A1p + a2 * A2p == 0: return 0.5, 0.0, 0.0, sw, sl
        if e1_fixed is None:
            p = a1 * A1p / (a1 * A1p + a2 * A2p)
            e1 = A1p * p * (1 - p) / (c + l); e2 = A2p * p * (1 - p) / (c + l)
        else:
            # rival best-responds to a fixed e1: maximize A2 * a2 e2/(a1 e1 + a2 e2) - (c+l) e2 over e2
            e1 = e1_fixed
            # FOC: A2 a2 a1 e1/(a1 e1 + a2 e2)^2 = c+l  ->  a1 e1 + a2 e2 = sqrt(A2 a2 a1 e1/(c+l))
            X = math.sqrt(max(A2p * a2 * a1 * e1 / (c + l), 0.0))
            e2 = max((X - a1 * e1) / a2, 0.0) if a2 > 0 else 0.0
            p = a1 * e1 / (a1 * e1 + a2 * e2) if a1 * e1 + a2 * e2 > 0 else 0.5
        return p, e1, e2, sw, sl
    V = [0.0] * (N + 1)
    for it in range(maxit):
        Vn = []
        for s in grid:
            p, e1, e2, sw, sl = stage(s, V)
            Vn.append((1 - beta) * Om * p + beta * Om / 2 - c * e1 - l * (e1 + e2) + delta * (p * interp(V, sw) + (1 - p) * interp(V, sl)))
        diff = max(abs(a - b) for a, b in zip(V, Vn)); V = Vn
        if diff < tol: break
    s0 = 0.5
    p, e1, e2, sw, sl = stage(s0, V)
    lam_mpe = delta * (interp(V, sw) - interp(V, sl)) / ((1 - beta) * Om)
    Gd = Gamma * delta * d / (1 - delta * (1 - d)); lam_formula = Gd / (1 - Gd) if Gd < 1 else float('inf')
    h = 2.0 / N
    pa, e1a, e2a, _, _ = stage(s0 + h, V); pb, e1b, e2b, _, _ = stage(s0 - h, V)
    p_eq = (pa - pb) / (2 * h)                         # full equilibrium derivative
    # partial: own effort fixed at the parity level e1, rival re-optimizes
    pa2, _, _, _, _ = stage(s0 + h, V, e1_fixed=e1); pb2, _, _, _, _ = stage(s0 - h, V, e1_fixed=e1)
    p_tilde = (pa2 - pb2) / (2 * h)
    G_eq = (1 - beta) * om * p_eq; G_t = (1 - beta) * om * p_tilde
    Gd_eq = G_eq * delta * d / (1 - delta * (1 - d)); Gd_t = G_t * delta * d / (1 - delta * (1 - d))
    lam_t = Gd_t / (1 - Gd_t) if Gd_t < 1 else float('inf')
    # expected deviation multiplier at parity (from the MPE policy) and its prediction 1 + d (Gamma_eq - 1)
    def Es(s):
        p, _, _, sw, sl = stage(s, V); return p * sw + (1 - p) * sl
    mult = (Es(s0 + h) - Es(s0 - h)) / (2 * h)
    # laggard's price far from parity
    lagg = []
    for sx in (0.25, 0.1):
        p_, _, _, sw_, sl_ = stage(sx, V)
        lagg.append((sx, delta * (interp(V, sw_) - interp(V, sl_)) / ((1 - beta) * Om)))
    # Monte Carlo: E|s - 1/2| from s = 0.52 over 60 periods, under the MPE and under the structural lottery (efforts fixed, p = a1/(a1+a2))
    rnd = random.Random(11); acc = 0.0; accp = 0.0; M = 400
    for _ in range(M):
        s = 0.52; sp = 0.52
        for t in range(60):
            p_, _, _, sw_, sl_ = stage(s, V)
            s = sw_ if rnd.random() < p_ else sl_
            a1 = sp ** r; a2 = (1 - sp) ** r; pp = a1 / (a1 + a2)
            swp, slp = nxt(sp); sp = swp if rnd.random() < pp else slp
        acc += abs(s - 0.5); accp += abs(sp - 0.5)
    return dict(k0=k0, jump=jw - jl, Gd=Gd, lam_formula=lam_formula, lam_mpe=lam_mpe, p_eq=p_eq, p_tilde=p_tilde,
                G_eq=G_eq, G_t=G_t, Gd_t=Gd_t, lam_t=lam_t, mult=mult, mult_pred=1 + d * (G_eq - 1), lagg=lagg,
                Eabs=acc / M, Eabs_passive=accp / M, it=it, diff=diff, e1=e1, de1=(e1a - e1b) / (2 * h))

if __name__ == "__main__":
    print(__doc__.split("\n")[0])
    print("(1) small jumps (d=0.02), l=0: does the equilibrium price equal the closed-loop gain of the partial-equilibrium loop?")
    for (r, G) in [(1.0, 0.2), (1.0, 0.3), (1.5, 0.3), (1.0, 0.45), (1.5, 0.6)]:
        R = solve(r, G, d=0.02, N=400)
        print(f"   r={r} Gamma={G}: jump={R['jump']:.4f} | lambda: formula {R['lam_formula']:.4f}, MPE {R['lam_mpe']:.4f} | "
              f"p'_eq={R['p_eq']:.3f} p~'={R['p_tilde']:.3f} (structural r={r}) | Gamma_eq={R['G_eq']:.3f} Gamma~={R['G_t']:.3f} | "
              f"closed-loop(Gamma~_delta)={R['lam_t']:.4f} | E-dev multiplier {R['mult']:.5f} vs 1+d(Gamma_eq-1)={R['mult_pred']:.5f} | conv {R['it']}")
    print("(2) the paper's jumps (d=0.2), l=0 and l=0.5: amplification at parity, stability, and the laggard's price")
    for (r, G, l) in [(1.0, 0.3, 0.0), (1.0, 0.6, 0.0), (1.5, 0.6, 0.0), (1.5, 0.6, 0.5), (1.5, 0.9, 0.0)]:
        R = solve(r, G, d=0.2, l=l, N=400)
        print(f"   r={r} Gamma={G} l={l}: lambda formula {R['lam_formula']:.4f}, MPE {R['lam_mpe']:.4f} (x{R['lam_mpe']/R['lam_formula']:.2f}) | "
              f"Gamma_eq={R['G_eq']:.3f} (p'_eq={R['p_eq']:.2f}) Gamma~={R['G_t']:.3f} | E|s-1/2| after 60 periods from 0.52: MPE {R['Eabs']:.3f} vs structural lottery {R['Eabs_passive']:.3f} "
              f"(expected-deviation multiplier {R['mult']:.3f}: {'unstable' if R['mult']>1 else 'stable'}) | laggard price at s=0.25: {R['lagg'][0][1]:.4f}, at 0.1: {R['lagg'][1][1]:.4f}")
    print("Reading: the first-order structure survives; which gain prices standing (partial-equilibrium, own effort fixed) and which decides")
    print("stability (full equilibrium) are two numbers once strategies respond, and both can exceed the structural gain several-fold.")
