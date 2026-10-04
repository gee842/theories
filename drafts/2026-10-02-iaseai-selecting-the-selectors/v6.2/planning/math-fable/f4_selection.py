"""f4: Lemma 3.3(3) (tipping needs s(0) > c > s(1)); Lemma 3.10 under nonlinear payoff-monotone fitness;
Proposition 6.7 / R8 (unequal incidence; matched unsafe variant).  Standard library only.

(A) Replicator dynamics with a sanction that falls with the evading share: three regimes.
(B) Price decomposition with fitness w = phi(pi), phi increasing (random concave, convex and mixed phi), random
    partitions: total Cov(w,z) <= 0 and every within-group term <= 0 under EVERY increasing phi; the
    between-group term is <= 0 under affine phi and can take either sign otherwise.
(C) Two developer types with unequal compliance costs: compliance survives, shares among compliers shift.
    A safeguarded developer with a higher baseline outgrows an unsafe one with a lower baseline: extinction of
    safeguarding needs a MATCHED unsafe variant (same baseline, no tax).
"""
import math, random

def replicator(p, pi, dt=0.01, T=4000.0):
    for _ in range(int(T / dt)):
        f = pi(p); pb = sum(a * b for a, b in zip(p, f))
        p = [a + dt * a * (b - pb) for a, b in zip(p, f)]; s = sum(p); p = [a / s for a in p]
    return p

def part_A():
    print("(A) Lemma 3.3(3): compliers pay c=0.3; evaders face s(x) falling in the evading share x")
    cases = [("s(x)=0.48(1-x): s(0)=0.48>c>s(1)=0", lambda x: 0.48 * (1 - x)),
             ("s(x)=0.24(1-x): s(0)=0.24<c", lambda x: 0.24 * (1 - x)),
             ("s(x)=0.5+0.5(1-x): s(1)=0.5>c", lambda x: 0.5 + 0.5 * (1 - x)),
             ("s(x)=0.6-0.4x: s(0)=0.6>c>s(1)=0.2", lambda x: 0.6 - 0.4 * x)]
    for name, s in cases:
        outs = []
        for x0 in (0.05, 0.5, 0.95):
            p = replicator([1 - x0, x0], lambda p: [-0.3, -s(p[1])])
            outs.append(f"x0={x0}->{p[1]:.3f}")
        tip = None
        if s(0) > 0.3 > s(1):
            lo, hi = 0.0, 1.0
            for _ in range(60):
                m = (lo + hi) / 2
                if s(m) > 0.3: lo = m
                else: hi = m
            tip = hi
        print(f"   {name}: " + "; ".join(outs) + (f"  -> bistable, tipping share {tip:.3f}" if tip is not None else "  -> one global attractor"))

def cov(a, b):
    ma = sum(a) / len(a); mb = sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / len(a)

def part_B():
    print("(B) Lemma 3.10 with nonlinear increasing fitness maps and random partitions (600 trials)")
    rnd = random.Random(5)
    bad_total = bad_within = 0; between_pos = between_neg = 0; affine_between_pos = 0; trials = 0
    for _ in range(600):
        N = rnd.randint(6, 40); z = [rnd.random() for _ in range(N)]
        b, c = rnd.uniform(0.2, 2.0), rnd.uniform(0.2, 2.0)
        zpop = sum(z) / N
        pi = [b * zpop - c * zz for zz in z]
        kind = rnd.choice(["affine", "concave", "convex", "mixed"])
        if kind == "affine":
            k = rnd.uniform(0.1, 3); phi = lambda x, k=k: 1 + k * x
        elif kind == "concave":
            k = rnd.uniform(0.5, 8); phi = lambda x, k=k: -math.exp(-k * x)   # increasing, concave
        elif kind == "convex":
            k = rnd.uniform(0.5, 6); phi = lambda x, k=k: math.exp(k * x)    # increasing, convex
        else:
            k = rnd.uniform(1, 6); phi = lambda x, k=k: x + math.sin(k * x) / k * 0.9 + 2  # increasing (derivative >= 0.1)
        w = [phi(x) for x in pi]
        G = rnd.randint(2, min(6, N // 2))
        groups = [[] for _ in range(G)]
        for j in range(N): groups[rnd.randrange(G)].append(j)
        groups = [g for g in groups if g]
        total = cov(z, w)
        zg = [sum(z[j] for j in g) / len(g) for g in groups]; wg = [sum(w[j] for j in g) / len(g) for g in groups]
        # between-group term weighted by group size (Price): Cov over individuals of group means
        between = cov([zg[i] for i, g in enumerate(groups) for _ in g], [wg[i] for i, g in enumerate(groups) for _ in g])
        within_terms = [cov([z[j] for j in g], [w[j] for j in g]) for g in groups]
        trials += 1
        if total > 1e-12: bad_total += 1
        if any(t > 1e-12 for t in within_terms): bad_within += 1
        if between > 1e-12:
            between_pos += 1
            if kind == "affine": affine_between_pos += 1
        else: between_neg += 1
    print(f"   total selection term > 0: {bad_total}/{trials}; any within-group term > 0: {bad_within}/{trials}")
    print(f"   between-group term > 0: {between_pos}/{trials} (of which under affine fitness: {affine_between_pos}); <= 0: {between_neg}")
    # Codex's explicit instance
    groups = [[0.0, 1.0], [0.4, 0.4]]
    allz = [x for g in groups for x in g]; w = [[math.exp(-5 * x) for x in g] for g in groups]; allw = [x for g in w for x in g]
    zg = [sum(g) / 2 for g in groups]; wg = [sum(g) / 2 for g in w]
    print(f"   Codex instance (groups (0,1),(0.4,0.4), w=e^(-5z)): between {cov([zg[0],zg[0],zg[1],zg[1]],[wg[0],wg[0],wg[1],wg[1]]):+.5f}, total {cov(allz,allw):+.5f}")

def part_C():
    print("(C) Proposition 6.7 / R8")
    # A: baseline 1, compliance cost .1; B: baseline 1, compliance cost .2; evasion sanctioned 1 (expected).  Variants: A_C, A_E, B_C, B_E
    pay = [0.9, 0.0, 0.8, 0.0]
    p = replicator([0.25] * 4, lambda p: pay, T=20.0)
    print(f"   unequal compliance costs (.1 vs .2), sanction 1: shares at t=20 {['%.6f'%x for x in p]}; compliant share {p[0]+p[2]:.9f} -> compliance survives, the cheaper complier gains share")
    # equal incidence preserves shares among compliers
    pay2 = [0.9, 0.0, 0.9, 0.0]
    p2 = replicator([0.3, 0.2, 0.3, 0.2], lambda p: pay2, T=20.0)
    print(f"   equal incidence (.1 and .1): compliers' relative shares {p2[0]/p2[2]:.6f} (started 1.0): preserved")
    # matched variant premise
    pay3 = [2.0 - 0.1, 1.0]   # safeguarded developer baseline 2 with tax .1 vs unsafe developer baseline 1
    p3 = replicator([0.5, 0.5], lambda p: pay3, T=20.0)
    pay4 = [2.0 - 0.1, 2.0]   # matched unsafe variant: same baseline, no tax
    p4 = replicator([0.5, 0.5], lambda p: pay4, T=200.0)
    print(f"   unmatched: safeguarded (baseline 2, tax .1) vs unsafe (baseline 1): safeguarded share at t=20 {p3[0]:.6f} (grows)")
    print(f"   matched: safeguarded (2-.1) vs its unsafe variant (2): safeguarded share at t=200 {p4[0]:.6e} (vanishes) -> (A_tau) + matched variant")
    pay5 = [1.0, 1.0]
    p5 = replicator([0.3, 0.7], lambda p: pay5, T=50.0)
    print(f"   zero tax: shares unchanged ({p5[0]:.3f}, {p5[1]:.3f}): neutral, the safeguard neither spreads nor is removed")

if __name__ == "__main__":
    part_A(); part_B(); part_C()
