"""m08  Relative objectives and punishments that can be imitated (Cor 5.5, key `relpunish`).

Claims under test (memo item 12):
  (A) The printed three-player role-differentiated punishment is a WEAK stage equilibrium in objectives (best unilateral
      deviation gains 0, 0, -0.2): a theta=-1 punisher is indifferent between hurting the deviator and hurting its fellow.
  (B) It is strict under any small asymmetry between the positional payoffs of the labels (unique X pays 1+eps): every
      unilateral deviation strictly loses; with -eps the mirror assignment of roles is strict. And under small RANDOM
      anonymous perturbations of all payoffs, a strict role-differentiated punishment holding the deviator below zero
      exists in most games.                                                                              [independent search]
  (C) The imitation bound needs a symmetric continuation: Codex's stochastic punishment (absorbing +10 to the punisher,
      -10 to the target, w.p. .5 a period) sustains cooperation among purely relative actors; the same game with the
      absorbing prize going to either player at random does not.                                           [independent]
Standard library only.
"""
import itertools, random

ACTS = [(r, l) for r in ('R', 'A') for l in ('X', 'Y')]

def base_payoffs(profile, eps_label=0.0, pert=None):
    """profile: tuple of actions for 3 players. Unique second component pays 1 (+eps_label if the unique label is X);
    racing gives the racer +0.1 and costs each other -0.1.  pert: anonymous perturbation function (own action, sorted others)."""
    n = len(profile); pi = [0.0] * n
    for i, (r, l) in enumerate(profile):
        others = [profile[j][1] for j in range(n) if j != i]
        if l not in others: pi[i] += 1.0 + (eps_label if l == 'X' else 0.0)
        if r == 'A':
            pi[i] += 0.1
            for j in range(n):
                if j != i: pi[j] -= 0.1
    if pert:
        for i in range(n):
            others = tuple(sorted(profile[j] for j in range(n) if j != i))
            pi[i] += pert(profile[i], others)
    return pi

def J(profile, i, **kw):
    pi = base_payoffs(profile, **kw)
    return pi[i] - sum(pi[j] for j in range(len(pi)) if j != i) / (len(pi) - 1)

def dev_gains(profile, **kw):
    out = []
    for i in range(3):
        base = J(profile, i, **kw)
        best = max(J(tuple(a if k == i else profile[k] for k in range(3)), i, **kw) for a in ACTS if a != profile[i])
        out.append(best - base)
    return out

def check_A_B():
    print("(A) the printed example: punishment [(A,X) deviator, (A,X) punisher 1, (A,Y) punisher 2]")
    prof = (('A', 'X'), ('A', 'X'), ('A', 'Y'))
    print(f"   deviator's objective {J(prof, 0):+.3f}; best unilateral deviation gains {[round(x, 3) for x in dev_gains(prof)]}  (weak: two zeros)")
    coop = (('R', 'X'),) * 3
    g = max(J(tuple(a if k == 0 else coop[k] for k in range(3)), 0) for a in ACTS)
    print(f"   deviation gain from cooperation {g:.3f}; grim reversion sustains cooperation for delta >= g/(g-v) = {g/(g+0.5):.3f}")
    print("(B) label asymmetry eps: unique X pays 1+eps")
    for eps in (0.01, 0.05, -0.05):
        p1 = (('A', 'X'), ('A', 'X'), ('A', 'Y')); p2 = (('A', 'Y'), ('A', 'Y'), ('A', 'X'))
        for prof, tag in ((p1, 'roles (X,X,Y)'), (p2, 'roles (Y,Y,X)')):
            gains = dev_gains(prof, eps_label=eps); v = J(prof, 0, eps_label=eps)
            coop = (('R', 'X'),) * 3
            gdev = max(J(tuple(a if k == 0 else coop[k] for k in range(3)), 0, eps_label=eps) for a in ACTS)
            strict = all(x < -1e-12 for x in gains)
            print(f"   eps={eps:+.2f} {tag}: deviator held at {v:+.3f}; deviation gains {[round(x, 4) for x in gains]} -> {'STRICT' if strict else 'not strict'}"
                  + (f"; delta* = {gdev/(gdev-v):.3f}" if strict and v < 0 else ''))
    print("    random anonymous perturbations of every payoff (uniform in [-e, e], same function for all players):")
    random.seed(1)
    for e in (0.02, 0.05, 0.1):
        found = 0; T = 300; dstars = []
        for _ in range(T):
            table = {}
            def pert(a, others, table=table):
                key = (a, others)
                if key not in table: table[key] = random.uniform(-e, e)
                return table[key]
            # cooperation: all (R,X); deviation gain for player 0
            coop = (('R', 'X'),) * 3
            g = max(J(tuple(a if k == 0 else coop[k] for k in range(3)), 0, pert=pert) for a in ACTS) - J(coop, 0, pert=pert)
            best = None
            for prof in itertools.product(ACTS, repeat=3):
                v = J(prof, 0, pert=pert) - J(coop, 0, pert=pert)
                if v >= 0: continue
                if all(x < -1e-12 for x in dev_gains(prof, pert=pert)):
                    if best is None or v < best: best = v
            if best is not None and g > 0:
                found += 1; dstars.append(g / (g - best))
        dstars.sort()
        print(f"      e={e}: a strict punishment holding the deviator below cooperation exists in {found}/{T} games; median delta* {dstars[len(dstars)//2]:.3f}")

def check_C():
    print("(C) continuation symmetry. Prisoner's dilemma CC=(3,3), DC=(4,0), DD=(1,1); relative objectives (pi_i - pi_j)")
    dl = 0.9
    # Codex: after a deviation, both play D (relative stage payoff 0); each period w.p. .5 an absorbing state:
    # the punisher gets +10 (relative) forever, the target -10.  Actions do not affect transitions.
    v = 0.0
    for _ in range(5000): v = dl * (0.5 * (-10) / (1 - dl) + 0.5 * v)
    dev = 4 + dl * v      # deviating from CC: relative stage gain 4 - 0 = 4
    print(f"   role-dependent continuation: target's punishment value {(1-dl)*v:.4f}; deviation worth {dev:.3f} < 0 = cooperation: sustained")
    # symmetric continuation: the absorbing prize goes to either player with prob .25 each
    v = 0.0
    for _ in range(5000): v = dl * (0.25 * 10 / (1 - dl) + 0.25 * (-10) / (1 - dl) + 0.5 * v)
    dev = 4 + dl * v
    print(f"   symmetric continuation: target's punishment value {(1-dl)*v:.4f}; deviation worth {dev:.3f} > 0: not sustained (the bound v >= 0 holds)")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A_B(); print(); check_C()
