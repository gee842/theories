"""Prop 1.5: pooling and prize sharing. Independent checks, and the mapping of the selection claim onto the Tullock contest."""
from fractions import Fraction as F
import random

def th_eff(beta, th0, n):
    return (th0 * (1 - beta) + beta * (1 + th0) * F(n - 1, n)) / ((1 - beta) + beta * (1 + th0) / F(n))
# derivative numerator identity: N'D - ND' = A (n-1-th0), A=(1+th0)/n
random.seed(5)
for _ in range(500):
    n = random.randint(2, 8); th0 = F(random.randint(-99, 100 * (n - 1) - 1), 100); beta = F(random.randint(0, 999), 1000)
    A = (1 + th0) / F(n)
    N = th0 * (1 - beta) + beta * A * (n - 1); D = (1 - beta) + beta * A
    Np = -th0 + A * (n - 1); Dp = -1 + A
    assert Np * D - N * Dp == A * (n - 1 - th0)
print("theta_eff derivative identity verified (exact, 500 cases)")
# examples
def thstar(n, b, c, d, eps): return (eps * (b - d) - c) / (eps * (b / F(n - 1) + d))
for eps in (1, 10):
    ts = thstar(4, F(1), F(3, 10), F(1, 5), F(eps))
    # theta_eff(beta,0,4) = 0.75 beta / (1 - 0.75 beta) = ts  => beta = ts / (0.75 (1 + ts))
    beta = ts / (F(3, 4) * (1 + ts))
    assert th_eff(beta, F(0), 4) == ts
    print(f"pooling ends racing in faithful-AI game (eps={eps}) at beta = {beta} = {float(beta):.4f}")
beta = F(1) / (F(3, 4) * 2); print("pooling: theta_eff=1 (theta_g, n=4, r=1) at beta =", beta)

# ---- prize sharing: intensities
def e_sym(n, r, Om, c, l, th): return r * Om * (n - 1 - th) / (n * n * (c + (1 + th) * l))
print("theta=-1 intensity, no sharing / half shared:", e_sym(4, 1, 1, 1, 0.3, -1), 0.5 * e_sym(4, 1, 1, 1, 0.3, -1))

# ---- the paper's selection example: two carriers, EACH facing a separate field of three at 0.1 (no shared loss)
def sep(e, beta, x=0.1, n=4, Om=1.0, c=1.0, l=0.0):
    return (1 - beta) * Om * e / (e + (n - 1) * x) + beta * Om / n - c * e - l * (e + (n - 1) * x)
for beta in (0.0, 0.5):
    print(f"paper's comparison (separate fields, l=0): beta={beta}: pay(0.2)-pay(0.05) = {sep(0.2, beta)-sep(0.05, beta):+.4f}")
    print(f"   same with l=0.3 counted in each carrier's own field: {sep(0.2, beta, l=0.3)-sep(0.05, beta, l=0.3):+.4f}")

# ---- one common field of n=4 carriers (Section 2.3: a handful of frontier developers): loads (0.2, 0.05, 0.1, 0.1)
def common(es, beta, Om=1.0, c=1.0, l=0.3):
    n = len(es); E = sum(es)
    return [(1 - beta) * Om * x / E + beta * Om / n - c * x - l * E for x in es]
for beta in (0.0, 0.5, 0.9):
    p = common([0.2, 0.05, 0.1, 0.1], beta)
    print(f"common field (0.2, 0.05, 0.1, 0.1), beta={beta}: pay(0.2)-pay(0.05) = {p[0]-p[1]:+.4f}")

# ---- finite-field relative selection (one mutant y against three residents x): sign of (mutant - resident)
def rel(y, x, beta, n=4, Om=1.0, c=1.0, r=1.0):
    tot = y ** r + (n - 1) * x ** r
    return (1 - beta) * Om * (y ** r - x ** r) / tot - c * (y - x)
for beta in (0.0, 0.5, 0.9):
    xstar = (1 - beta) * 1.0 / (4 * 1.0)  # (1-beta) r Om/(n c)
    s = [f"y={y}: {rel(y, 0.1, beta):+.4f}" for y in (0.05, 0.15, 0.2)]
    print(f"residents at 0.1, beta={beta}: mutant minus resident: " + ", ".join(s) + f" | relative-selection rest point (1-beta)rOm/(nc) = {xstar:.4f}")
# global check that (1-beta) r Om/(n c) is the finite-population ESS (mutant never beats residents there)
for beta in (0.0, 0.5, 0.9, 0.99):
    x = (1 - beta) / 4
    worst = max(rel(y / 1000 * 4 * max(x, 1e-3), x, beta) for y in range(0, 4001))
    print(f"  beta={beta}: ESS candidate x={x:.4f}: best mutant advantage {worst:+.2e} (<=0 means uninvadable); positive for every beta<1")

# ---- discrete replicator in the common field: two types, high H and low Lo, shares p, field of n=4 drawn as expected payoff
# (the 'handful of developers' case: each type's payoff computed in one field containing both types in proportion)
def replicate(beta, eH=0.2, eL=0.05, p0=0.5, steps=400, k=0.5):
    p = p0
    for _ in range(steps):
        # four developers: mix by shares (continuous approximation of a field with mean load)
        E = 4 * (p * eH + (1 - p) * eL)
        wH = eH / E; wL = eL / E
        piH = (1 - beta) * wH - eH; piL = (1 - beta) * wL - eL
        p = p * (1 + k * piH) / (p * (1 + k * piH) + (1 - p) * (1 + k * piL))
    return p
for beta in (0.0, 0.5, 0.75):
    print(f"common-field replicator, loads 0.2 vs 0.05, beta={beta}: share of high-load type after 400 steps = {replicate(beta):.3f}")

# ---- positional component and credibility
# prize = shareable material part Om_m + positional part P (domination / loss L_b avoided). Sharing beta of Om_m only.
for beta in (0.0, 0.5, 0.9, 1.0):
    Om_m, P = 1.0, 1.0
    eff = (1 - beta) * Om_m + P
    print(f"material 1 + positional 1: sharing beta={beta} of the material part leaves effective prize {eff:.2f} (intensity x{eff/(Om_m+P):.2f})")
# winner honours the sharing agreement with probability rho
for rho in (1.0, 0.5, 0.0):
    beta = 0.9
    print(f"beta=0.9 honoured with prob rho={rho}: effective contested prize = {1 - beta*rho:.2f} of Omega")
