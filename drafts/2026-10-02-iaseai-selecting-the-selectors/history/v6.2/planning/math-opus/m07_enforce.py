"""m07  The enforcement condition with explicit actions (Prop 5.4 key `enforce`; R4 in Prop 9.1 key `require`).

Claims under test (memo item 11):
  (A) Per-deviation breakout: condition (14) must hold for every deviation a with its own (g(a), p_d(a), D(a)); the
      deviation with the largest g need not bind (Fable).                                                   [arithmetic]
  (B) Part (5): v = [(1-delta)P + delta q (D+U)]/(1-delta+2 delta q) needs at most one breakout per period (2q <= 1).
      New example with P < v < C: C=1, P=0, D=4, U=0, g=2, delta=.9: restraint enforceable at q=0, not for
      q in (0.0354, 0.0556), although punishment still leaves the deviator below cooperation.                [independent]
  (C) Explicit-action stochastic game: grim reversion to a race with breakouts, one breakout technology setting both the
      deviation's p_d and the race's q.  Every one-shot deviation is checked in every state (cooperation AND punishment,
      so the punishers' incentive is checked too), by value iteration on the explicit chain; the verdict is compared with
      (14) evaluated with v from (5).                                                                          [independent]
  (D) R4: with D < C the bound still binds unless (1-delta) g <= delta (C-D) (Opus counterexample).          [independent]
  (E) p_d-bar is homogeneous of degree zero in (g, C, D, v): larger stakes lower it only if g and D grow faster than C - v.
Standard library only.
"""
import random

def pbar(g, C, D, v, delta):
    return 1 - ((1 - delta) * g + delta * (D - C)) / (delta * (D - v))

def cond14(g, C, D, v, pd, delta):
    return (1 - delta) * g + delta * pd * (D - C) <= delta * (1 - pd) * (C - v) + 1e-12

def check_A():
    print("(A) per-deviation breakout (Fable): C=3, D=6, v=1, delta=.9")
    C, D, v, dl = 3.0, 6.0, 1.0, 0.9
    for name, g, pd in (("A: g=1,  p_d=.1", 1.0, 0.1), ("B: g=.2, p_d=.6", 0.2, 0.6)):
        lhs = (1 - dl) * g + dl * pd * (D - C); rhs = dl * (1 - pd) * (C - v)
        print(f"   deviation {name}: temptation {lhs:.3f}, remaining sanction {rhs:.3f} -> {'deterred' if lhs <= rhs else 'NOT deterred'}")
    print("   the larger-g deviation is deterred, the quiet one is not: (14) must hold deviation by deviation")

def punishment_value(P, D, U, q, delta, iters=20000):
    # explicit chain: in the race both race; w.p. q each breaks out (at most one), absorbing values D/(1-delta), U/(1-delta)
    VP = 0.0
    for _ in range(iters):
        VP = P + delta * (q * D / (1 - delta) + q * U / (1 - delta) + (1 - 2 * q) * VP)
    return (1 - delta) * VP

def check_B():
    print("(B) part (5): race reversion with breakouts; closed form vs explicit chain; the P<v<C example")
    C, P, D, U, g, dl = 1.0, 0.0, 4.0, 0.0, 2.0, 0.9
    for q in (0.0, 0.02, 0.035, 0.036, 0.045, 0.055, 0.056, 0.1):
        v_chain = punishment_value(P, D, U, q, dl)
        v_form = ((1 - dl) * P + dl * q * (D + U)) / (1 - dl + 2 * dl * q)
        ok = cond14(g, C, D, v_chain, 0.0, dl)
        print(f"   q={q:.3f}: v chain {v_chain:.4f}, formula {v_form:.4f}; v<C: {v_chain < C}; restraint enforceable at p_d=0: {ok}")
    print(f"   predicted window: q in ({0.0778/2.2:.4f}, {0.1/1.8:.4f}) - deterrence fails while the punishment is still worse than cooperation")
    print("   with 2q>1 the 'neither breaks out' probability 1-2q is negative: the closed form needs at most one breakout per period")

def explicit_game(C, g, S, P, SP, D, U, q, h, delta, iters=3000):
    """Two players; states coop, pun, dec1, dec2 (absorbing).  Player 2 plays grim: restrain in coop, race in pun.
    One breakout technology: in the race each racer breaks out w.p. q per period (at most one per period); a lone
    deviator from coop breaks out w.p. p_d = 1-(1-q)^h (head start h).  Stage payoffs: coop (R,R) C each; deviator C+g;
    race (A,A) P each; a restrainer facing a racer SP.  Breakout: D per period to the breaker, U to the other, forever.
    Player 1's BEST RESPONSE over all (Markov) deviation plans is computed by value iteration on this MDP -- not by
    comparing a one-period deviation (which would be (14) rearranged).  Cooperation is sustained iff the optimal value
    at coop equals C/(1-delta).  The same DP for the punisher in pun checks that racing there is a best response."""
    pd = 1 - (1 - q) ** h
    VD, VU = D / (1 - delta), U / (1 - delta)
    Vc = Vp = 0.0
    for _ in range(iters):
        race = P + delta * (q * VD + q * VU + (1 - 2 * q) * Vp)
        quit = SP + delta * (q * VU + (1 - q) * Vp)
        Vp_new = max(race, quit)
        stay = C + delta * Vc
        dev = (C + g) + delta * (pd * VD + (1 - pd) * Vp)
        Vc_new = max(stay, dev)
        Vc, Vp = Vc_new, Vp_new
    sustained = Vc <= C / (1 - delta) + 1e-7 * (1 + abs(Vc))
    race_val = P + delta * (q * VD + q * VU + (1 - 2 * q) * Vp)
    quit_val = SP + delta * (q * VU + (1 - q) * Vp)
    credible = race_val >= quit_val - 1e-9
    return sustained, credible, pd, (1 - delta) * Vp

def check_C():
    print("(C) explicit-action stochastic game: player 1's best response over all deviation plans (value iteration on the MDP)")
    print("    vs condition (14) evaluated with v from (5)")
    random.seed(5); agree = 0; tot = 0; cred_fail = 0; sus = 0; dis = []
    for _ in range(20000):
        C = 1.0; g = random.uniform(0.05, 3); P = random.uniform(-1, 0.9); SP = P - random.uniform(0.01, 2)
        D = random.uniform(-0.5, 6); U = random.uniform(-6, 0.5); q = random.uniform(0, 0.5); h = random.choice([1, 2, 3, 5])
        delta = random.uniform(0.5, 0.99); S = random.uniform(-2, 1)
        sustained, credible, pd, v = explicit_game(C, g, S, P, SP, D, U, q, h, delta)
        v5 = ((1 - delta) * P + delta * q * (D + U)) / (1 - delta + 2 * delta * q)
        pred = cond14(g, C, D, v5, pd, delta)
        tot += 1; sus += sustained
        if not credible: cred_fail += 1
        if credible:
            agree += (pred == sustained)
            if pred != sustained and len(dis) < 5: dis.append((round(g, 3), round(P, 3), round(D, 3), round(U, 3), round(q, 3), h, round(delta, 3)))
    print(f"   20,000 random settings: cooperation sustained in {sus}; punishment not credible (quitting the race pays) in {cred_fail}")
    print(f"   where the punishment is credible, (14) agrees with the best-response computation in {agree} of {tot-cred_fail}; disagreements {dis}")
    print("   where it is not credible, (14) must use the value of the credible punishment (the theorem's premise), not (5)")

def check_D():
    print("(D) R4 with D < C (Opus): C=1, D=.9, v=0, g=2, delta=.9")
    C, D, v, g, dl = 1.0, 0.9, 0.0, 2.0, 0.9
    pb = pbar(g, C, D, v, dl)
    for pd in (0.8, 0.86, 0.87, 0.9):
        print(f"   p_d={pd}: (14) holds: {cond14(g, C, D, v, pd, dl)}   (p_d-bar = {pb:.4f})")
    print(f"   (1-delta)g = {(1-dl)*g:.2f} > delta(C-D) = {dl*(C-D):.2f}: the bound binds although D<C; the right exception is (1-delta)g <= delta(C-D), i.e. p_d-bar >= 1")

def check_E():
    print("(E) homogeneity of p_d-bar in (g, C, D, v)")
    g, C, D, v, dl = 1.0, 1.0, 3.0, 0.0, 0.9
    base = pbar(g, C, D, v, dl)
    for s in (2, 10):
        print(f"   all stakes x{s}: {pbar(s*g, s*C, s*D, s*v, dl):.4f} (base {base:.4f}); only g and D x{s}: {pbar(s*g, C, s*D, v, dl):.4f}")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A(); print(); check_B(); print(); check_C(); print(); check_D(); print(); check_E()
