"""Existence/uniqueness of the symmetric pure equilibrium of the Tullock contest with O_i = pi_i + theta*mean(pi_-i).
Game in objectives = standard contest with prize V = Omega (n-1-theta)/(n-1) and unit cost k = c + (1+theta) l.
We verify directly on the ORIGINAL objective (not the reduced one), with a dense grid + golden refinement for the
global best response, over theta in [-1, n-1) and r in (0, n/(n-1)]. Then look for asymmetric pure equilibria."""
import math

def obj(i_e, others, n, r, Om, c, l, th):
    es = [i_e] + others
    tot = sum(x ** r for x in es)
    w = [x ** r / tot for x in es] if tot > 0 else [1.0 / n] * n
    E = sum(es)
    pi = [Om * w[j] - c * es[j] - l * E for j in range(n)]
    return pi[0] + th * sum(pi[1:]) / (n - 1)

def e_sym(n, r, Om, c, l, th):
    return r * Om * (n - 1 - th) / (n * n * (c + (1 + th) * l))

def global_br(others, n, r, Om, c, l, th, hi):
    # dense log+linear grid, then local refinement around best
    grid = [0.0] + [hi * (k / 4000) for k in range(1, 4001)] + [hi * 10 ** (-k / 50) for k in range(1, 400)]
    best = max(grid, key=lambda y: obj(y, others, n, r, Om, c, l, th))
    lo_, hi_ = max(0.0, best - hi / 2000), best + hi / 2000
    for _ in range(100):
        m1 = lo_ + (hi_ - lo_) / 3; m2 = hi_ - (hi_ - lo_) / 3
        if obj(m1, others, n, r, Om, c, l, th) < obj(m2, others, n, r, Om, c, l, th): lo_ = m1
        else: hi_ = m2
    y = (lo_ + hi_) / 2
    return y, obj(y, others, n, r, Om, c, l, th)

worst_gap = 0.0; cases = 0; fails = []
for n in (2, 3, 4, 6):
    rmax = n / (n - 1)
    for r in (0.2, 0.5, 1.0, 0.5 * (1 + rmax), rmax):
        for th in (-1.0, -0.5, 0.0, 0.4, 0.5 * (n - 1), n - 1 - 0.3, n - 1 - 0.01):
            for (c, l) in ((1.0, 0.3), (1.0, 3.0), (0.2, 0.05)):
                Om = 1.0
                e = e_sym(n, r, Om, c, l, th)
                others = [e] * (n - 1)
                at_e = obj(e, others, n, r, Om, c, l, th)
                hi = 3 * max(e, 1e-6) + Om / c
                y, best = global_br(others, n, r, Om, c, l, th, hi)
                gap = best - at_e  # >0 means a profitable deviation
                cases += 1
                # tolerate numerical noise; at r=rmax the deviation to 0 is exactly indifferent
                if gap > 1e-9 * max(1.0, abs(at_e)):
                    fails.append((n, r, th, c, l, e, y, gap))
                worst_gap = max(worst_gap, gap)
print(f"symmetric FOC point checked as global best response in {cases} cases; failures: {len(fails)}; worst gain from deviating {worst_gap:.2e}")
for f in fails[:10]: print("  FAIL", f)

# second-order condition at symmetric point: w'' sign = (r-1)n - 2r  (<0 iff r < n/(n-2))
for n in (2, 3, 4, 6, 10):
    rmax = n / (n - 1)
    print(f"  n={n}: SOC coefficient (r-1)n-2r at r=n/(n-1): {(rmax-1)*n-2*rmax:+.4f} (negative => strict local max)")

# indifference at r = n/(n-1): equilibrium objective vs deviation to zero, effective game
for n in (2, 3, 4):
    r = n / (n - 1); V = 1.0; k = 1.0
    x = r * (n - 1) * V / (n * n * k)
    print(f"  n={n}, r=n/(n-1): effective payoff at equilibrium V/n - kx = {V/n - k*x:+.2e} (= payoff of e=0): weak equilibrium")

# ---- asymmetric pure equilibria: m active at the m-player symmetric level, n-m inactive
def entrant_best(n, m, r, V=1.0, k=1.0):
    x = r * (m - 1) * V / (m * m * k)
    best = -1e9; ybest = 0
    for j in range(1, 20001):
        y = 2.0 * j / 20000
        g = V * y ** r / (y ** r + m * x ** r) - k * y
        if g > best: best, ybest = g, y
    return best, ybest, x
print("\nasymmetric pure equilibria with m < n active (prize V=1, cost k=1 in the effective game):")
for n in (3, 4, 6):
    rmax = n / (n - 1)
    m = n - 1
    # find smallest r in (1, rmax] at which the inactive player prefers to stay out
    lo, hi = 1.0, rmax
    b_hi, _, _ = entrant_best(n, m, hi)
    if b_hi > 0:
        print(f"  n={n}, m={m}: entrant profits even at r=n/(n-1); no such equilibrium"); continue
    for _ in range(40):
        mid = (lo + hi) / 2
        b, _, _ = entrant_best(n, m, mid)
        if b > 0: lo = mid
        else: hi = mid
    b, y, x = entrant_best(n, m, rmax)
    print(f"  n={n}: {m} active at x={x:.4f} and one inactive is a pure equilibrium for r in [{hi:.4f}, {rmax:.4f}] "
          f"(at r=n/(n-1) the entrant's best payoff is {b:+.4f}); total intensity there {m*x:.4f} vs symmetric {n*rmax*(n-1)/(n*n):.4f}")

# ---- r beyond n/(n-1): expected total effort bounded by V/k (non-negative expected payoffs), equal to Tullock value at r=n/(n-1)
for n in (2, 4):
    rmax = n / (n - 1)
    print(f"  n={n}: total intensity at r=n/(n-1): n*e = {n*rmax*(n-1)/(n*n):.4f} * V/k  (upper bound V/k for every r)")
