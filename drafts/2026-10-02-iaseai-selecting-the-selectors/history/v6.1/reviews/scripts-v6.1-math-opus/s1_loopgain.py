"""Independent checks of Proposition 2.2 (loop gain) and 2.3 (compounding), V6.1.
Different construction from checks_v61 LG: up to 3 channels, per-channel k0 and diffusion, strength enters
as sigma_i = sum_j r_j * phi_j(X_ij) with phi_j either log or linear (so r_j = v_j X*), full n*m Jacobian
by finite differences, spectral radius on the sum-zero subspace by power iteration (no secular equation used).
"""
import math, random

def make(n, m, rnd):
    P = dict(n=n, m=m)
    P['beta'] = rnd.uniform(0, 0.8)
    P['Om'] = rnd.uniform(0.5, 3)
    P['kap'] = [rnd.uniform(0.02, 1.0) for _ in range(m)]
    P['k0'] = [rnd.choice([0.0, rnd.uniform(0, 0.6)]) for _ in range(m)]
    P['d'] = [rnd.uniform(0.03, 0.9) for _ in range(m)]
    P['df'] = [rnd.choice([0.0, rnd.uniform(0, 1 - P['d'][j])]) for j in range(m)]
    P['kind'] = [rnd.choice(['log', 'lin']) for _ in range(m)]
    P['coef'] = [rnd.uniform(0, 2.5) for _ in range(m)]
    return P

def steady(P):
    n = P['n']
    return [(P['kap'][j] * P['Om'] / n + P['k0'][j]) / P['d'][j] for j in range(P['m'])]

def sigma(P, x):
    s = 0.0
    for j in range(P['m']):
        if P['kind'][j] == 'log':
            s += P['coef'][j] * math.log(x[j])
        else:
            s += P['coef'][j] * x[j]
    return s

def step(P, X):
    n, m = P['n'], P['m']
    sg = [sigma(P, X[i]) for i in range(n)]
    mx = max(sg); e = [math.exp(t - mx) for t in sg]; S = sum(e); p = [t / S for t in e]
    mean = [sum(X[i][j] for i in range(n)) / n for j in range(m)]
    Y = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append((1 - P['d'][j]) * X[i][j] + P['kap'][j] * P['Om'] * ((1 - P['beta']) * p[i] + P['beta'] / n)
                       + P['k0'][j] - P['df'][j] * (X[i][j] - mean[j]))
        Y.append(row)
    return Y, p

def gamma(P, delta=None):
    n, m = P['n'], P['m']; Xs = steady(P); G = 0.0
    for j in range(m):
        rj = P['coef'][j] if P['kind'][j] == 'log' else P['coef'][j] * Xs[j]
        om = P['kap'][j] * P['Om'] / (P['kap'][j] * P['Om'] + n * P['k0'][j])
        if delta is None:
            G += (1 - P['beta']) * rj * om * P['d'][j] / (P['d'][j] + P['df'][j])
        else:
            G += (1 - P['beta']) * rj * om * delta * P['d'][j] / (1 - delta * (1 - P['d'][j] - P['df'][j]))
    return G

def spectral_sumzero(P, h=1e-7, iters=3000):
    """power iteration with the finite-difference Jacobian-vector product, restricted to sum-zero deviations"""
    n, m = P['n'], P['m']; Xs = steady(P)
    base = [[Xs[j] for j in range(m)] for _ in range(n)]
    rnd = random.Random(1)
    v = [[rnd.uniform(-1, 1) for j in range(m)] for i in range(n)]
    def proj(v):
        mu = [sum(v[i][j] for i in range(n)) / n for j in range(m)]
        return [[v[i][j] - mu[j] for j in range(m)] for i in range(n)]
    def norm(v): return math.sqrt(sum(t * t for r in v for t in r))
    v = proj(v); nv = norm(v); v = [[t / nv for t in r] for r in v]
    lam = 0.0
    for it in range(iters):
        X = [[base[i][j] + h * v[i][j] for j in range(m)] for i in range(n)]
        Y, _ = step(P, X)
        w = [[(Y[i][j] - base[i][j]) / h for j in range(m)] for i in range(n)]
        w = proj(w); nw = norm(w)
        if nw == 0: return 0.0
        lam_new = nw
        v = [[t / nw for t in r] for r in w]
        if it > 200 and abs(lam_new - lam) < 1e-10: lam = lam_new; break
        lam = lam_new
    return lam

def pv_relative(P, delta, x=1e-7, T=None):
    """carrier 0's relative net payoff y=x (relative to mean), reinvested: relative stock deviation kap_j*y;
    implement by giving carrier 0 +kap_j*x and every other -kap_j*x/(n-1) (sum zero, so relative stock deviation of 0 is kap_j*x).
    Return PV of carrier 0's excess winnings over the unperturbed path, per unit y."""
    n, m = P['n'], P['m']; Xs = steady(P)
    X = [[Xs[j] + (P['kap'][j] * x if i == 0 else -P['kap'][j] * x / (n - 1)) for j in range(m)] for i in range(n)]
    base_W = P['Om'] / n
    pv = 0.0; disc = delta
    if T is None: T = 6000
    for t in range(T):
        p = None
        sg = [sigma(P, X[i]) for i in range(n)]
        mx = max(sg); e = [math.exp(s - mx) for s in sg]; S = sum(e); p = [s / S for s in e]
        W0 = P['Om'] * ((1 - P['beta']) * p[0] + P['beta'] / n)
        pv += disc * (W0 - base_W); disc *= delta
        X, _ = step(P, X)
        if disc < 1e-16: break
    return pv / x

rnd = random.Random(2026)
mis = 0; near = 0; N = 1500; maxerr = 0
for k in range(N):
    n = rnd.randint(2, 5); m = rnd.randint(1, 3)
    P = make(n, m, rnd)
    G = gamma(P)
    if abs(G - 1) < 0.02: near += 1; continue
    rad = spectral_sumzero(P)
    if (rad > 1) != (G > 1): mis += 1; print('MISMATCH', G, rad, P)
print(f"Prop 2.2(1): {N} random systems (1-3 channels, log/linear entry, k0, diffusion): mismatches {mis}, skipped near boundary {near}")

# Prop 2.2(3): PV of a unit relative payoff vs Gd/(1-Gd), 3-channel systems with Gamma<1
worst = 0; cnt = 0
for k in range(300):
    n = rnd.randint(2, 5); m = rnd.randint(1, 3)
    P = make(n, m, rnd)
    if gamma(P) >= 0.95: continue
    dl = rnd.uniform(0.3, 0.97)
    Gd = gamma(P, dl)
    lam = Gd / (1 - Gd)
    pv = pv_relative(P, dl)
    cnt += 1
    err = abs(pv - lam) / max(1e-9, abs(lam)) if lam > 1e-6 else abs(pv - lam)
    worst = max(worst, err)
print(f"Prop 2.2(3): {cnt} systems with Gamma<0.95: max relative error of PV vs Gd/(1-Gd) = {worst:.2e}")

# Gamma_delta < Gamma and -> Gamma
viol = 0
for k in range(2000):
    P = make(rnd.randint(2, 5), rnd.randint(1, 3), rnd)
    G = gamma(P)
    for dl in (0.1, 0.5, 0.9, 0.999):
        if gamma(P, dl) > G + 1e-12: viol += 1
print(f"Gamma_delta <= Gamma violations: {viol}")

# How large is lambda for a FINITE relative gain when Gamma>1 (nonlinear saturation)?
print("Finite perturbations when Gamma>1 but Gd<1: PV per unit y vs first-order lambda")
P = dict(n=2, m=1, beta=0.0, Om=1.0, kap=[0.5], k0=[0.0], d=[0.2], df=[0.0], kind=['log'], coef=[1.5])
for dl in (0.7, 0.8, 0.85):
    Gd = gamma(P, dl); lam = Gd / (1 - Gd)
    out = []
    for x in (1e-6, 1e-3, 1e-2, 0.05, 0.2):
        out.append(f"x={x}: {pv_relative(P, dl, x=x):.3f}")
    print(f"  Gamma={gamma(P):.2f}, delta={dl}: Gd={Gd:.3f}, lambda={lam:.3f}; " + "; ".join(out))
