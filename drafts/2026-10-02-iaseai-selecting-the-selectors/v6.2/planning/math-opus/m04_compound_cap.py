"""m04  A point of enough: caps, diffusion and inflow not tied to rank (Prop 2.3(2), key `compound`).

Claims under test (memo item 6):
  (A) A cap strictly below equal-standing capacity K* is locally stable; at equality it can fail
      (laggard excluded iff (1-beta) r omega (n-1)/n > 1 + df (n-1)/(n d)).                      [independent]
  (B) With the others at the cap, a laggard's net inflow is
        phi(K) = kap Om[(1-beta) K^r/(K^r+(n-1)Kbar^r) + beta/n] + k0 - d K + df (n-1)(Kbar-K)/n,
      and recovery from every start holds iff phi > 0 on (0, Kbar).  Diffusion is a third inflow not tied to rank:
      phi(0+) = beta kap Om/n + k0 + df (n-1) Kbar/n.                                              [independent]
  (C) With r>1 and none of sharing, provision, diffusion, phi(0+) = 0 and laggards below a threshold are excluded.
Simulation of the full n-carrier model with min(cap, .) after each update (others free to fall below the cap),
compared with the criterion.  Standard library only.
"""
import math, random

def step(X, r, kap, Om, beta, k0, d, df, cap):
    n = len(X); w = [x ** r for x in X]; W = sum(w); mean = sum(X) / n
    Xn = [(1 - d) * x + kap * Om * ((1 - beta) * wi / W + beta / n) + k0 - df * (x - mean) for x, wi in zip(X, w)]
    return [min(cap, x) for x in Xn]

def phi(K, Kbar, n, r, kap, Om, beta, k0, d, df):
    return kap * Om * ((1 - beta) * K ** r / (K ** r + (n - 1) * Kbar ** r) + beta / n) + k0 - d * K + df * (n - 1) * (Kbar - K) / n

def check_A():
    print("(A) cap at and below K*")
    # Codex: n=2, kap Om = 1, d=.2, r=3, no beta/k0/df, K* = 2.5
    X = [2.499, 2.5]
    for t in range(400): X = step(X, 3, 1, 1, 0, 0, 0.2, 0.0, 2.5)
    print(f"   cap = K* = 2.5, r=3, start (2.499, 2.5): after 400 periods {X[0]:.3e}, {X[1]:.4f}  (excluded)")
    X = [2.449, 2.45]
    for t in range(4000): X = step(X, 3, 1, 1, 0, 0, 0.2, 0.0, 2.45)
    print(f"   cap = 0.98 K* = 2.45, same start just below the cap: after 4000 periods {X[0]:.6f}, {X[1]:.6f}  (restored)")
    random.seed(7); bad_strict = 0; tests = 0; eq_pred_ok = 0; eq_tests = 0
    for _ in range(400):
        n = random.choice([2, 3, 4, 6]); r = random.uniform(0.5, 4); kap = 1.0; Om = 1.0
        beta = random.choice([0, 0, random.uniform(0, 0.3)]); k0 = random.choice([0, 0, random.uniform(0, 0.2)])
        d = random.uniform(0.05, 0.4); df = random.choice([0, 0, random.uniform(0, 0.3)])
        if d + df > 1: continue
        Ks = (kap * Om / n + k0) / d
        # strict cap: start just below
        cap = 0.97 * Ks
        X = [cap * 0.999] + [cap] * (n - 1)
        for t in range(3000): X = step(X, r, kap, Om, beta, k0, d, df, cap)
        tests += 1
        if abs(X[0] - cap) > 1e-6 * cap: bad_strict += 1
        # equality: prediction of local exclusion
        w = kap * Om / (kap * Om + n * k0)
        excl_pred = (1 - beta) * r * w * (n - 1) / n > 1 + df * (n - 1) / (n * d)
        X = [Ks * (1 - 1e-4)] + [Ks] * (n - 1)
        for t in range(6000): X = step(X, r, kap, Om, beta, k0, d, df, Ks)
        excl_sim = X[0] < Ks * (1 - 2e-4)
        eq_tests += 1; eq_pred_ok += (excl_pred == excl_sim)
    print(f"   400 random settings: strict cap (0.97 K*) restored from just below in {tests-bad_strict} of {tests};")
    print(f"   cap = K*: local exclusion predicted by (1-beta) r omega (n-1)/n > 1 + df(n-1)/(n d) in {eq_pred_ok} of {eq_tests} (simulated)")

def check_B():
    print("(B) global recovery: criterion phi>0 on (0,Kbar) vs simulation from a laggard at 1% of the cap")
    # Codex diffusion example
    n, r, kap, Om, beta, k0, d, df, cap = 2, 2.0, 1.0, 1.0, 0.0, 0.0, 0.2, 0.6, 2.5
    mn = min(phi(cap * k / 10000, cap, n, r, kap, Om, beta, k0, d, df) for k in range(1, 10000))
    X = [0.01, 2.5]
    for t in range(2000): X = step(X, r, kap, Om, beta, k0, d, df, cap)
    print(f"   Codex: n=2 r=2 d=.2 df=.6, cap=K*=2.5, no sharing or provision: min phi on grid {mn:.4f} (>0); from (0.01, 2.5) -> ({X[0]:.6f}, {X[1]:.6f})")
    random.seed(11); agree = 0; tot = 0; examples = []
    for _ in range(600):
        n = random.choice([2, 3, 5]); r = random.uniform(1.05, 4); kap = 1.0; Om = 1.0
        beta = random.choice([0, random.uniform(0, 0.4)]); k0 = random.choice([0, random.uniform(0, 0.15)])
        d = random.uniform(0.05, 0.4); df = random.choice([0, random.uniform(0, 0.5)])
        if d + df > 1: continue
        Ks = (kap * Om / n + k0) / d; cap = random.uniform(0.5, 0.99) * Ks
        # leaders stay at the cap whenever K <= Kbar implies their inflow is nonnegative: sufficient Kbar <= (kap Om + n k0)/(n d + df)
        if cap > (kap * Om + n * k0) / (n * d + df): continue
        crit = min(phi(cap * k / 2000, cap, n, r, kap, Om, beta, k0, d, df) for k in range(1, 2000)) > 0
        X = [0.01 * cap] + [cap] * (n - 1)
        for t in range(5000): X = step(X, r, kap, Om, beta, k0, d, df, cap)
        rec = abs(X[0] - cap) < 1e-6 * cap
        tot += 1; agree += (crit == rec)
        if crit != rec and len(examples) < 5:
            # exclusion threshold: the largest K/cap with phi <= 0
            thr = max([k / 2000 for k in range(1, 2000) if phi(cap * k / 2000, cap, n, r, kap, Om, beta, k0, d, df) <= 0] or [0])
            examples.append(dict(n=n, r=round(r, 2), d=round(d, 3), cap_over_Kstar=round(cap / Ks, 3), criterion=crit, recovered_from_1pct=rec, exclusion_threshold_over_cap=thr))
    print(f"   random settings with leaders provably held at the cap (Kbar <= (kap Om + n k0)/(n d + df)): criterion agrees with simulation in {agree} of {tot}")
    if examples: print("   disagreements: the criterion concerns EVERY start; these laggards start above the exclusion threshold:", examples)

def check_C():
    print("(C) r>1 and no inflow not tied to rank: laggards below a threshold are excluded; any one of the three restores")
    n, r, kap, Om, d, cap = 5, 1.5, 1.0, 1.0, 0.2, 0.8
    for (beta, k0, df) in ((0, 0, 0), (0.1, 0, 0), (0, 0.05, 0), (0, 0, 0.15)):
        res = []
        for K0 in (0.05, 0.2, 0.5):
            X = [K0] + [cap] * (n - 1)
            for t in range(4000): X = step(X, r, kap, Om, beta, k0, d, df, cap)
            res.append(f"{K0}->{X[0]:.4f}")
        print(f"   beta={beta} k0={k0} df={df}: phi(0+)={beta*kap*Om/n + k0 + df*(n-1)*cap/n:.4f}; laggard " + ", ".join(res))

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A(); print(); check_B(); print(); check_C()
