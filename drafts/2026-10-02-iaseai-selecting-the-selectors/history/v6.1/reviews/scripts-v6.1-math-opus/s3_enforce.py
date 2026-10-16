"""Prop 5.4 (enforcement condition), Prop 5.4(5) (reversion with breakouts), Cor 5.5 (role-differentiated punishment).
(1) EC block is an algebraic identity: show symbolically (random exact rationals) that VI-comparison == inequality.
(2) Prop 5.4(5): region where v<C (cooperation still preferred) but breakouts in the race make reversion fail;
    also check the paper's own example has v>C (the race-with-breakouts is preferred to cooperation by both).
    Credibility: is racing a best response inside the punishment phase?
(3) Prop 5.4(2): monotonicity of p_bar at the edges of [0,1).
(4) R4 exception 'D<C': is p_d <= p_bar still binding when D<C?
(5) Cor 5.5 counterexample: strictness of the punishment equilibrium; robustness to symmetric (anonymous) payoff
    perturbations; robustness to asymmetric noise.
"""
from fractions import Fraction as Fr
import random, itertools, math

rnd = random.Random(99)
# (1) identity
bad = 0
for _ in range(20000):
    dl = Fr(rnd.randint(1, 99), 100); pd = Fr(rnd.randint(0, 100), 100)
    C, g, D, v = (Fr(rnd.randint(-300, 300), 100) for _ in range(4))
    Vc = C / (1 - dl); Vd = C + g + dl * (pd * D / (1 - dl) + (1 - pd) * v / (1 - dl))
    lhs = (1 - dl) * g + dl * pd * (D - C); rhs = dl * (1 - pd) * (C - v)
    if (Vc >= Vd) != (lhs <= rhs): bad += 1
print(f"(1) EC 'direct values' vs (14) with exact rationals, 20,000 draws: disagreements {bad} -> the EC block tests algebra only")

# (2) Prop 5.4(5)
def vP(P, D, U, q, dl): return ((1 - dl) * P + dl * q * (D + U)) / (1 - dl + 2 * dl * q)
C, g, dl, P, D, U = 1.0, 0.5, 0.9, 0.0, 4.0, 0.0
print(f"(2) paper's example C=1,g=0.5,delta=0.9,P=0,D=4,U=0,q=0.1: v={vP(P,D,U,0.1,dl):.3f} > C={C}: both actors prefer the race-with-breakouts to cooperation")
for g in (0.5, 2.0, 5.0):
    lo = hi = None
    for k in range(1, 5000):
        q = k / 10000
        v = vP(P, D, U, q, dl)
        fails = (1 - dl) * g > dl * (C - v)
        if fails and v < C and lo is None: lo = q
        if v < C: hi = q
    print(f"    g={g}: q-window with v<C yet reversion fails to deter (deters at q=0: {(1-dl)*g <= dl*(C-P)}): [{lo}, {hi}]")
# credibility of 'both race' in punishment: restrain one period while rival races (payoff S, only rival can break out)
for S_ in (-0.5, 0.0):
    q = 0.03
    VP = vP(P, D, U, q, dl) / (1 - dl)
    dev = S_ + dl * (q * U / (1 - dl) + (1 - q) * VP)
    print(f"    credibility, S={S_}, q={q}: racing in punishment worth {VP:.3f}, restraining one period {dev:.3f} -> racing a best response: {VP >= dev}")

# (3) monotonicity at edges
def pbar(g, C, D, v, dl): return 1 - ((1 - dl) * g + dl * (D - C)) / (dl * (D - v))
g0 = (0.9 * (3 - 1)) / 0.1  # makes pbar = 0 at C=3,v=1,dl=.9? solve (1-dl)g = dl(C-v)
print(f"(3) at p_bar=0 (g=(delta/(1-delta))(C-v)={g0:.1f}): dp_bar/dD = {(pbar(g0,3,4+1e-6,1,0.9)-pbar(g0,3,4,1,0.9))/1e-6:.2e} (zero, not negative)")

# (4) R4's exception D<C
C, D, v, g, dl = 1.0, 0.9, 0.0, 2.0, 0.9
pb = pbar(g, C, D, v, dl)
print(f"(4) D<C: C=1, D=0.9, v=0, g=2, delta=0.9 -> p_bar={pb:.3f}; at p_d=0.9 restraint fails although D<C: "
      f"{(1-dl)*g+dl*0.9*(D-C) > dl*(1-0.9)*(C-v)}")

# (5) Cor 5.5 counterexample
acts = [(x, m) for x in 'RA' for m in 'XY']
def mat(prof, a=0.1, b=0.1, bonus=None):
    out = []
    for i, (x, mm) in enumerate(prof):
        unique = all(m2 != mm for j, (x2, m2) in enumerate(prof) if j != i)
        p = (1.0 if unique else 0.0) + (a if x == 'A' else 0.0) - b * sum(1 for j, (x2, m2) in enumerate(prof) if j != i and x2 == 'A')
        if bonus: p += bonus(i, x, mm, prof)
        out.append(p)
    return out
def obj(pis):
    n = len(pis); return [pis[i] - (sum(pis) - pis[i]) / (n - 1) for i in range(n)]
def gaps(prof, payf):
    """for each player, best objective from unilateral deviation minus current (<=0 means NE); and the
    smallest positive margin to the best alternative (strictness)"""
    base = obj(payf(prof)); res = []
    for i in range(3):
        alts = []
        for act in acts:
            if act == prof[i]: continue
            pr = list(prof); pr[i] = act
            alts.append(obj(payf(pr))[i] - base[i])
        res.append(max(alts))
    return base, res
pun = [('A', 'X'), ('A', 'X'), ('A', 'Y')]
base, res = gaps(pun, mat)
print(f"(5) punishment {pun}: objectives {[round(t,3) for t in base]}; best unilateral gain per player {[round(t,3) for t in res]}"
      " -> the deviator and one punisher are exactly indifferent (weak equilibrium)")
# symmetric perturbation: anonymous payoff table over (own action, multiset of others' actions), small noise eps
def anon_table(eps, rnd):
    tab = {}
    for own in acts:
        for others in itertools.combinations_with_replacement(acts, 2):
            tab[(own, tuple(sorted(others)))] = rnd.uniform(-eps, eps)
    return tab
def payf_from(tab):
    def f(prof):
        base = mat(prof)
        return [base[i] + tab[(prof[i], tuple(sorted(prof[:i] + prof[i+1:])))] for i in range(3)]
    return f
for eps in (0.01, 0.05, 0.1):
    found = strict = 0; dstars = []
    N = 400
    for _ in range(N):
        tab = anon_table(eps, rnd); pf = payf_from(tab)
        coop = [('R', 'X')] * 3
        C0 = obj(pf(coop))[0]
        g0 = max(obj(pf([a] + coop[1:]))[0] for a in acts) - C0
        best = None
        for prof in itertools.product(acts, repeat=3):
            b, r_ = gaps(list(prof), pf)
            if max(r_) <= 1e-12 and b[0] < C0 - 1e-9:
                ds = g0 / (g0 + C0 - b[0]) if g0 > 0 else 0
                if best is None or ds < best[0]: best = (ds, max(r_) < -1e-9)
        if best is not None:
            found += 1; strict += best[1]; dstars.append(best[0])
    dstars.sort()
    print(f"    anonymous perturbation eps={eps}: games with a stage-NE punishment holding the deviator below C: {found}/{N}; "
          f"of which strict NE: {strict}; median delta* {dstars[len(dstars)//2] if dstars else None:.3f}")
