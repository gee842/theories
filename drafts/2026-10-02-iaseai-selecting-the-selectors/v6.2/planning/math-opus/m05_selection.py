"""m05  Selection results: blindness, evasion, incidence, Price decomposition, the matched variant.
Keys: `blind` (Lemma 3.3), `onegroup` (Lemma 3.10), `nested` (Prop 6.7), `require` (R8).

Claims under test (memo items 7-9, 18):
  (A) Lemma 3.3(3): with a sanction s(x) falling in the evading share x, both states are stable iff s(0) > c > s(1);
      if s(1) >= c compliance is globally stable, if s(0) <= c evasion is.                            [independent]
  (B) Unequal compliance costs: compliance still goes to one when every type's expected sanction exceeds its gain from
      evasion; incidence decides only the shares AMONG compliers. Equal incidence is not necessary for keeping
      evasion out (Codex 5). One type with s_k < c_k keeps evasion alive.                              [independent]
  (C) Lemma 3.10: for a trait that costs its bearer and benefits everyone equally, under every monotone fitness
      transform the TOTAL and the WITHIN-group selection terms are <= 0; the BETWEEN-group term is <= 0 for affine
      fitness and can be positive otherwise (Jensen).                                                     [independent]
  (D) Prop 6.7(2) needs a matched unsafe variant: a positive tax alone does not eliminate a safeguarded developer with
      a larger independent advantage; against its matched twin it is eliminated; a lead pays the tax while it lasts.
Standard library only.
"""
import math, random

def check_A():
    print("(A) evasion with a sanction that falls as evaders spread: x' = x(1-x)(c - s(x)), c = 0.3")
    c = 0.3
    cases = {
        's = .5 + .5(1-x)  [s(1)=.5 >= c]': lambda x: 0.5 + 0.5 * (1 - x),
        's = .24(1-x)      [s(0)=.24 <= c]': lambda x: 0.24 * (1 - x),
        's = .48(1-x)      [s(0)>c>s(1)]': lambda x: 0.48 * (1 - x),
        's = 1.2(1-x)      [s(0)>c>s(1)]': lambda x: 1.2 * (1 - x),
    }
    for name, s in cases.items():
        out = []
        for x0 in (0.02, 0.3, 0.5, 0.7, 0.98):
            x = x0
            for _ in range(20000):
                x += 0.01 * x * (1 - x) * (c - s(x))
            out.append(f"{x0}->{x:.3f}")
        # tipping share where s(x)=c, if any in (0,1)
        root = None
        for k in range(1, 10000):
            if (s(k / 10000) - c) * (s((k - 1) / 10000) - c) <= 0: root = k / 10000; break
        print(f"   {name}: " + ", ".join(out) + (f"   tipping share {root}" if root else "   no tipping share"))

def check_B():
    print("(B) two developer types, unequal compliance costs; replicator on (A comply, A evade, B comply, B evade)")
    for (cA, cB, sA, sB) in ((0.1, 0.2, 1.0, 1.0), (0.1, 0.2, 0.15, 0.25), (0.1, 0.2, 1.0, 0.15), (0.1, 0.2, 1.0, 0.05)):
        pay = [1 - cA, 1 - sA, 1 - cB, 1 - sB]
        x = [0.25] * 4
        for _ in range(40000):
            m = sum(p * xi for p, xi in zip(pay, x))
            x = [xi + 0.01 * xi * (p - m) for xi, p in zip(x, pay)]
            S = sum(x); x = [xi / S for xi in x]
        comp = x[0] + x[2]
        best = max(range(4), key=lambda k: pay[k])
        note = ("every s_k > c_k: compliance -> 1, incidence only re-sorts compliers" if sA > cA and sB > cB else
                ("s_B < c_B, yet B's evaders are beaten by A's compliers: evasion vanishes" if best in (0, 2) else "s_B < c_B and B's evaders earn most: evasion takes over"))
        print(f"   costs ({cA},{cB}) sanctions ({sA},{sB}): compliant share {comp:.6f}; among compliers A:B = {x[0]:.4f}:{x[2]:.4f}   ({note})")

def price_terms(groups, psi, b=0.5, cost=0.2, w0=1.0):
    pop = [z for g in groups for z in g]; N = len(pop)
    zbar = sum(pop) / N
    fit = [[psi(w0 + b * zbar - cost * z) for z in g] for g in groups]
    allw = [w for g in fit for w in g]
    mean = lambda v: sum(v) / len(v)
    def cov(a, b_):
        ma, mb = mean(a), mean(b_); return mean([(x - ma) * (y - mb) for x, y in zip(a, b_)])
    total = cov(allw, pop)
    # group-size weighted between and within terms
    wsz = [len(g) / N for g in groups]
    zg = [mean(g) for g in groups]; wg = [mean(f) for f in fit]
    mz = sum(s * z for s, z in zip(wsz, zg)); mw = sum(s * w for s, w in zip(wsz, wg))
    between = sum(s * (z - mz) * (w - mw) for s, z, w in zip(wsz, zg, wg))
    within = sum(s * cov(f, g) for s, f, g in zip(wsz, fit, groups))
    return total, between, within

def check_C():
    print("(C) Price decomposition of a costly trait with a benefit shared by all; fitness w = psi(payoff), psi increasing")
    transforms = {
        'affine 1+2pi': lambda p: 1 + 2 * p,
        'exp(5 pi)': lambda p: math.exp(5 * p),
        'log(.05+pi)': lambda p: math.log(0.05 + p) if p > -0.05 else -1e9,
        'pi^3 (on pi>0)': lambda p: max(p, 0) ** 3,
        'logistic 20(pi-1)': lambda p: 1 / (1 + math.exp(-20 * (p - 1))),
        'step-like tanh(50(pi-.95))': lambda p: math.tanh(50 * (p - 0.95)),
    }
    random.seed(3)
    for name, psi in transforms.items():
        tot_pos = within_pos = between_pos = 0; T = 3000; maxb = 0.0
        for _ in range(T):
            k = random.randint(2, 6)
            groups = [[random.random() if random.random() < 0.7 else random.choice([0.0, 1.0]) for _ in range(random.randint(2, 6))] for _ in range(k)]
            t, bt, wi = price_terms(groups, psi)
            tot_pos += t > 1e-12; within_pos += wi > 1e-12; between_pos += bt > 1e-12; maxb = max(maxb, bt)
            assert abs(t - bt - wi) < 1e-9
        print(f"   {name:28s}: total>0 in {tot_pos}/{T}; within>0 in {within_pos}/{T}; between>0 in {between_pos}/{T} (largest between {maxb:.2e})")
    # the reviewers' two-group examples
    for groups, psi, tag in (([[0.0, 1.0], [0.6, 0.6]], lambda p: math.log(1.05 + p), 'Opus: log(1.05+pi), payoff -z'),
                             ([[0.0, 1.0], [0.4, 0.4]], lambda p: math.exp(5 * p), 'Codex: exp(-5z)')):
        t, bt, wi = price_terms(groups, psi, b=0.0, cost=1.0, w0=0.0)
        print(f"   {tag}: total {t:+.6f}, between {bt:+.6f}, within {wi:+.6f}")

def check_D():
    print("(D) the alignment tax under selection: matched variant, heterogeneous advantage, a lead that pays the tax")
    def run(pay, T=2000.0, dt=0.01):
        x = [1 / len(pay)] * len(pay)
        for _ in range(int(T / dt)):
            m = sum(p * xi for p, xi in zip(pay, x))
            x = [xi * math.exp(dt * (p - m)) for xi, p in zip(x, pay)]; S = sum(x); x = [xi / S for xi in x]
        return x
    x = run([2.0 - 0.1, 1.0])
    print(f"   safeguarded developer, baseline 2, tax .1, vs unsafe developer baseline 1: safeguarded share -> {x[0]:.4f} (tax alone does not eliminate it)")
    x = run([2.0 - 0.1, 1.0, 2.0])
    print(f"   add its matched unsafe twin (baseline 2, no tax): shares safeguarded {x[0]:.2e}, unsafe-1 {x[1]:.2e}, twin {x[2]:.4f}")
    for adv in (0.02, 0.005):
        x = run([1.0 + adv - 0.01, 1.0], T=3000.0)
        print(f"   tax .01 paid out of an independent advantage {adv}: safeguarded share -> {x[0]:.4f}")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A(); print(); check_B(); print(); check_C(); print(); check_D()
