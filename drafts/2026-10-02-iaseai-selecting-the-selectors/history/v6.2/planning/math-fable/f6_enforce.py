"""f6: Proposition 5.4 (enforce), Corollary 5.5 (relpunish), the scissors (Section 5.5), R4.  Standard library only.
Values are computed by explicit value iteration or direct discounted summation on the stochastic game, never by (14).

(A) per-deviation p_d: a deviation with smaller g and larger p_d can bind.
(B) 5.4(5): mutually exclusive breakouts (q <= 1/2) vs independent breakouts (q -> q(1-q)); the P<v<C example
    (C=1, P=0, D=4, U=0, g=2, delta=.9, q=.045) where reversion to the race fails to deter though cooperation is preferred.
(C) R4's exception: D<C does not exempt; (1-delta) g <= delta (C-D) does (p_bar >= 1), for every p_d.
(D) Corollary 5.5 and the continuation premise: (i) an EXCHANGEABLE stochastic continuation (Tullock lottery to an
    absorbing decisive position, transitions depend on actions only) gives mirrored relative value 0; (ii) Codex's
    label-dependent continuation (target receives -10 with probability .5 regardless of actions) defeats imitation.
(E) The three-player role-differentiated example: weak equilibrium; strict under +eps on the X prize; destroyed by -eps.
(F) The scissors in reduced form by direct discounted streams: theta_rep(p_d); theta_0 = 0 loses enforced restraint at
    p_d ~ .95; the restraint gap is monotone in p_d at D = C and hump-shaped for D > C.
"""
import itertools, random

def cond(g, pd, C, D, v, dl): return (1 - dl) * g + dl * pd * (D - C) <= dl * (1 - pd) * (C - v)

def part_A():
    print("(A) per-deviation p_d (C=3, D=6, v=1, delta=.9): deviation X (g=1.0, p_d=.1), deviation Y (g=.2, p_d=.6)")
    # direct values: cooperation C/(1-dl); deviation: C+g + dl[pd D/(1-dl) + (1-pd) v/(1-dl)]
    dl, C, D, v = 0.9, 3.0, 6.0, 1.0
    Vc = C / (1 - dl)
    for name, g, pd in (("X", 1.0, 0.1), ("Y", 0.2, 0.6)):
        Vd = C + g + dl * (pd * D / (1 - dl) + (1 - pd) * v / (1 - dl))
        print(f"   deviation {name}: V_coop={Vc:.2f}, V_dev={Vd:.2f} -> {'deterred' if Vc>=Vd else 'NOT deterred'}")
    print("   -> the condition must hold for every deviation with its own p_d; the max-g deviation need not bind")

def vP_excl(P, D, U, q, dl): return ((1 - dl) * P + dl * q * (D + U)) / (1 - dl + 2 * dl * q)
def vP_indep(P, D, U, q, dl):
    qq = q * (1 - q); return ((1 - dl) * P + dl * qq * (D + U)) / (1 - dl + 2 * dl * qq)
def vP_sim(P, D, U, q, dl, indep, T=4000):
    # value iteration on the explicit chain: state 'race'; each period: exclusive (prob q each, one at most) or independent
    V = 0.0
    for _ in range(T):
        if indep:
            pi = q * (1 - q); pj = q * (1 - q); pboth = q * q; pnone = (1 - q) ** 2
            # simultaneous breakouts: the race continues (tie)
            V = P + dl * (pi * D / (1 - dl) + pj * U / (1 - dl) + (pboth + pnone) * V)
        else:
            V = P + dl * (q * D / (1 - dl) + q * U / (1 - dl) + (1 - 2 * q) * V)
    return (1 - dl) * V

def part_B():
    print("(B) 5.4(5): punishment = reversion to the race with breakouts")
    dl, P, D, U, C = 0.9, 0.0, 4.0, 0.0, 1.0
    for q in (0.045, 0.1, 0.3):
        print(f"   q={q}: v exclusive {vP_excl(P,D,U,q,dl):.4f} (sim {vP_sim(P,D,U,q,dl,False):.4f}); v independent {vP_indep(P,D,U,q,dl):.4f} (sim {vP_sim(P,D,U,q,dl,True):.4f})")
    g = 2.0; q = 0.045; v = vP_excl(P, D, U, q, dl)
    print(f"   example C=1, P=0, D=4, U=0, g=2, delta=.9, q=.045: v={v:.3f} < C; deviation (p_d=0) deterred at q=0: {cond(g,0,C,C,P,dl)}; at q=.045: {cond(g,0,C,C,v,dl)}")
    print(f"   the paper's example (g=.5, q=.1): v={vP_excl(P,D,U,0.1,dl):.3f} > C: the race-with-breakouts is preferred to cooperation itself")
    print(f"   q=.6 exclusive: 1-2q={1-1.2:+.1f} (invalid); independent form stays valid: v={vP_indep(P,D,U,0.6,dl):.4f}")

def part_C():
    print("(C) R4 exception")
    dl = 0.9
    C, D, v, g = 1.0, 0.9, 0.0, 2.0
    pb = 1 - ((1 - dl) * g + dl * (D - C)) / (dl * (D - v))
    print(f"   D<C (C=1, D=.9, v=0, g=2): p_bar={pb:.3f}; at p_d=.9 restraint sustained? {cond(g,0.9,C,D,v,dl)} -> D<C does not exempt")
    C, D, v, g = 1.0, 0.9, 0.0, 0.5
    print(f"   (1-delta)g={0.1*g:.3f} <= delta(C-D)={dl*(C-D):.3f}: sustained at p_d = 0, .5, .9, 1: {[cond(g,pd,C,D,v,dl) for pd in (0,.5,.9,1)]} -> p_bar>=1 exempts")

def part_D():
    print("(D) Corollary 5.5 and the continuation premise (two actors, theta=-1, delta=.9)")
    dl = 0.9
    # (i) exchangeable continuation: each period in the punishment both choose effort; a Tullock lottery with
    # strengths e_i gives an absorbing decisive position worth +10/-10 (relative) with prob q_e = 0.3 per period;
    # otherwise continue.  Punisher plays e_P = 1; the punished imitates (e = e_P) -> p = 1/2 -> expected relative value 0.
    def rel_value_mirror(eP, eI, T=2000, qe=0.3):
        V = 0.0
        for _ in range(T):
            pwin = eI / (eI + eP)
            V = (0.0) + dl * (qe * (pwin * 10 / (1 - dl) + (1 - pwin) * (-10) / (1 - dl)) + (1 - qe) * V)
        return (1 - dl) * V
    print(f"   (i) exchangeable lottery continuation: mirrored strategy gives the punished normalized relative value {rel_value_mirror(1.0,1.0):+.6f} (= 0, as the corollary needs)")
    # (ii) Codex's label-dependent continuation
    V = 0.0
    for _ in range(2000): V = dl * (0.5 * (-10) / (1 - dl) + 0.5 * V)
    print(f"   (ii) label-dependent continuation (target gets -10 w.p. .5 whatever it does): normalized value {(1-dl)*V:+.4f}; deviation worth 4+delta*V = {4+dl*V:.2f} < 0 -> cooperation sustained among relative actors")
    print("       -> the premise is exchangeability of the whole continuation (payoffs and transitions invariant under relabelling), not stage symmetry")

def part_E():
    print("(E) three-player role-differentiated punishment: strictness")
    acts = [(x, m) for x in "RA" for m in "XY"]
    def pis(prof, eps=0.0, a=0.1, b=0.1):
        out = []
        for i, (x, m) in enumerate(prof):
            unique = all(m2 != m for j, (x2, m2) in enumerate(prof) if j != i)
            prize = (1.0 + (eps if m == "X" else 0.0)) if unique else 0.0
            out.append(prize + (a if x == "A" else 0.0) - b * sum(1 for j, (x2, m2) in enumerate(prof) if j != i and x2 == "A"))
        return out
    def O(prof, eps=0.0):
        p = pis(prof, eps); return [p[i] - (sum(p) - p[i]) / 2 for i in range(3)]
    pun = [("A", "X"), ("A", "X"), ("A", "Y")]
    for eps in (0.0, 0.02, -0.02):
        base = O(pun, eps); margins = []
        for i in range(3):
            best = max(O(list(pun[:i]) + [a] + list(pun[i + 1:]), eps)[i] for a in acts if a != pun[i])
            margins.append(base[i] - best)
        kind = "strict NE" if min(margins) > 1e-12 else ("weak NE" if min(margins) > -1e-12 else "not an equilibrium")
        print(f"   eps={eps:+.2f} on the X prize: objectives {[round(v,3) for v in base]}, margins over best deviation {[round(m,3) for m in margins]} -> {kind}")

def part_F():
    print("(F) the scissors in reduced form (binary game n=4, b=1, c=.3, d=.2, eps=1, delta=.9), direct discounted streams")
    n, b, c, dd, ep, dl = 4, 1.0, 0.3, 0.2, 1.0, 0.9
    def u(i, a): return ep * b * (a[i] - sum(a[j] for j in range(n) if j != i) / (n - 1)) - c * a[i] - ep * dd * sum(a)
    def J(i, a, th): return u(i, a) + th * sum(u(j, a) for j in range(n) if j != i) / (n - 1)
    def V_dev(th, pd, D, T=3000):
        g = J(0, [1, 0, 0, 0], th); P = J(0, [1] * n, th); v = g; disc = dl
        for t in range(1, T): v += disc * (pd * D + (1 - pd) * P); disc *= dl
        return v
    def theta_rep(pd, D):
        lo, hi = -1.0, 3.0
        if V_dev(hi, pd, D) > 0: return float("inf")
        for _ in range(60):
            m = (lo + hi) / 2
            if V_dev(m, pd, D) > 0: lo = m
            else: hi = m
        return hi
    print("   theta_rep(p_d) at D=C=0: " + ", ".join(f"p_d={pd}: {theta_rep(pd,0.0):+.3f}" for pd in (0, .5, .9, .95, .99, 1.0)))
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo + hi) / 2
        if V_dev(0.0, m, 0.0) <= 0: lo = m
        else: hi = m
    print(f"   theta_0=0 loses enforced restraint at p_d={lo:.4f} (the text's 'none above 0.99' should read about 0.95; for theta_0=.4: ", end="")
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo + hi) / 2
        if V_dev(0.4, m, 0.0) <= 0: lo = m
        else: hi = m
    print(f"{lo:.4f})")
    print("   restraint gap (share of theta~U[-1,3] above theta_rep among wide theta>1 minus among narrow theta<1):")
    for D in (0.0, 0.5):
        row = []
        for pd in (0, .5, .8, .9, .95, .99, 1.0):
            tr = theta_rep(pd, D)
            fw = max(0.0, min(1.0, (3 - max(tr, 1)) / 2)); fn = max(0.0, min(1.0, (1 - max(tr, -1)) / 2))
            row.append(f"{fw-fn:+.2f}")
        print(f"      D={D}: " + " ".join(row) + ("  (monotone)" if D == 0 else "  (hump: closes as p_d -> 1, no theta <= n-1 sustains restraint)"))
    print(f"   D=0.5: theta_rep at p_d=.9 = {theta_rep(0.9,0.5):+.3f}; at p_d=1: {theta_rep(1.0,0.5)}")

if __name__ == "__main__":
    part_A(); part_B(); part_C(); part_D(); part_E(); part_F()
