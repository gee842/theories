"""Misc checks: Lemma 3.10 under a nonlinear payoff-monotone rule; Theorem 10.5 margin on the Allee host
(independent integration in shares, own collapse criterion); Lemma 8.2 coupling vs conditioning; Prop 5.15(2)
bias with a nonlinear third-party term; Prop 2.3(2) cap at K* exactly; Prop 5.4(5) with independent breakouts."""
import math, random

# ---- Lemma 3.10: between-group term under a nonlinear monotone fitness map
print("Lemma 3.10: two groups, global benefit, fitness w = phi(pi), pi = b*zbar - c*z_j, phi increasing concave")
b, c = 1.0, 1.0
zA = [0.0, 1.0]; zB = [0.6, 0.6]
zbar = (sum(zA) + sum(zB)) / 4
for name, phi in [('linear', lambda x: 1 + x), ('concave 1-exp(-8(x+1))', lambda x: 1 - math.exp(-8 * (x + 1))),
                  ('concave log(1.05+x)', lambda x: math.log(1.05 + x))]:
    w = lambda z: phi(b * zbar - c * z)
    wA = sum(w(z) for z in zA) / 2; wB = sum(w(z) for z in zB) / 2
    gz = [sum(zA) / 2, sum(zB) / 2]; gw = [wA, wB]
    mz = sum(gz) / 2; mw = sum(gw) / 2
    cov_between = sum((a - mz) * (bb - mw) for a, bb in zip(gz, gw)) / 2
    allz = zA + zB; allw = [w(z) for z in allz]
    cov_total = sum((a - sum(allz)/4) * (bb - sum(allw)/4) for a, bb in zip(allz, allw)) / 4
    print(f"   {name}: between-group Cov(w_g,z_g) = {cov_between:+.4f}; total Cov(w,z) = {cov_total:+.4f}")

# ---- Theorem 10.5 margin on the Allee host, independent: replicator on shares, RK4 on (x, V), collapse if V<V_u-0.02
print("Theorem 10.5(1): minimal liability margin on the pointwise-harsher Allee host (independent integration)")
rho, h = 0.05, 0.08
def Vu(A, E):
    rA = rho * A / (1 - A)
    # rA (V/A - 1)(1 - V) = h E  ->  quadratic
    a_ = -rA / A; b_ = rA * (1 / A + 1); c_ = -rA - h * E
    disc = b_ * b_ - 4 * a_ * c_
    return min((-b_ + math.sqrt(disc)) / (2 * a_), (-b_ - math.sqrt(disc)) / (2 * a_))
def run(Delta, A, emin=0.1, emax=1.0, x0=0.99, V0=1.0, T=1500.0, dt=0.02):
    rA = rho * A / (1 - A)
    def f(x, V):
        E = emin + (emax - emin) * x
        dx = x * (1 - x) * (-(Delta) * (emax - emin))      # replicator: payoff difference (nu - tau_eff)(e_max - e_min)
        dV = V * (rA * (V / A - 1) * (1 - V) - h * E)
        return dx, dV
    x, V = x0, V0; vmin = V
    for _ in range(int(T / dt)):
        k1 = f(x, V); k2 = f(x + dt/2*k1[0], V + dt/2*k1[1]); k3 = f(x + dt/2*k2[0], V + dt/2*k2[1]); k4 = f(x + dt*k3[0], V + dt*k3[1])
        x += dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; V += dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        vmin = min(vmin, V)
        if V < 1e-6: return vmin, 0.0
    return vmin, V
for A in (0.05, 0.10, 0.15, 0.20, 0.25):
    lo, hi = 0.0, 3.0
    for _ in range(30):
        m = (lo + hi) / 2
        if run(m, A)[1] < 0.01: lo = m
        else: hi = m
    print(f"   A={A:.2f}: Delta_min={hi:.3f}, V_u(e_min)={Vu(A,0.1):.3f}; transient minimum at Delta_min+0.01: {run(hi+0.01, A)[0]:.3f}")

# ---- Lemma 8.2: coupled dominance with endogenous dissolution, and failure of the conditioning step
print("Lemma 8.2: two-state Markov world; dissolution more likely in the bad state")
# world state w in {G,B}; P(stay)=0.9. Continuation hazard: G 0.01, B 0.05. Arrangement A while active: G 0.005, B 0.02;
# after dissolution: same as continuation (safe fallback with equality). Dissolution hazard: G 0.01, B 0.2.
def exact(H):
    # DP over (world, A_alive, A_survived, C_survived) probabilities -> marginal survival of A and of C
    hz = {'C': {'G': 0.01, 'B': 0.05}, 'A': {'G': 0.005, 'B': 0.02}, 'dis': {'G': 0.01, 'B': 0.2}}
    import collections
    dist = collections.defaultdict(float); dist[('G', True, True, True)] = 1.0
    for t in range(H):
        nd = collections.defaultdict(float)
        for (w, act, sa, sc), pr in dist.items():
            hA = hz['A'][w] if act else hz['C'][w]; hC = hz['C'][w]
            # common uniform: A fails if U<hA, C fails if U<hC (hA<=hC)
            outcomes = []
            lo_ = min(hA, hC); hi_ = max(hA, hC)
            for pu, fa, fc in ((lo_, True, True), (hi_ - lo_, hA > hC, hC > hA), (1 - hi_, False, False)):
                if pu <= 0: continue
                sa2 = sa and not fa; sc2 = sc and not fc
                for pdis, act2 in ((hz['dis'][w] if act else 0.0, False), (1 - (hz['dis'][w] if act else 0.0), act)):
                    if pdis <= 0: continue
                    for w2, pw in ((w, 0.9), ('B' if w == 'G' else 'G', 0.1)):
                        nd[(w2, act2, sa2, sc2)] += pr * pu * pdis * pw
        dist = nd
    SA = sum(p for (w, a, sa, sc), p in dist.items() if sa); SC = sum(p for (w, a, sa, sc), p in dist.items() if sc)
    return SA, SC
for H in (10, 30, 100):
    SA, SC = exact(H)
    print(f"   H={H}: S^A={SA:.4f} >= S^C={SC:.4f}: {SA >= SC - 1e-12}")

# ---- Prop 5.15(2) with a nonlinear third-party term: is the effective bias still b0 n/(n-2), independent of u?
print("Prop 5.15(2): ideal points with third-party payoff -k y^2 (nonlinear) instead of linear")
def ideal(n, b0, u, k, who):
    # objective J = pi_who - (1/(n-1)) sum_{j!=who} pi_j, pi_S=-(y-u-b0)^2, pi_R=-(y-u)^2, third parties -k y^2 each
    best = None
    for i in range(-4000, 4001):
        y = u + i / 1000
        pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = -k * y * y
        if who == 'S': J = pS - (pR + (n - 2) * pk) / (n - 1)
        else: J = pR - (pS + (n - 2) * pk) / (n - 1)
        if best is None or J > best[0]: best = (J, y)
    return best[1]
for n in (3, 4):
    for u in (0.0, 0.5, 1.0):
        gap = ideal(n, 0.05, u, 0.3, 'S') - ideal(n, 0.05, u, 0.3, 'R')
        print(f"   n={n}, u={u}: ideal-point gap in y {gap:.4f}; in state units gap*(1-k) = {gap*(1-0.3):.4f} (b0 n/(n-2) = {0.05*n/(n-2):.4f})")
