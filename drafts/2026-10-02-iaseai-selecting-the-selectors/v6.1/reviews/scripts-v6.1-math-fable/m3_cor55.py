"""m3: attack 2. Does the role-differentiated counterexample of Corollary 5.5 rest on a weak equilibrium, a
knife-edge or an equilibrium-selection choice? Is it robust to small perturbations?

Three-player minority game (as in CR(c)): action = (x, m), x in {R, A}, m in {X, Y}. A player whose m is unique
earns 1 (times 1+eps if the unique component is X: eps=0 is the paper's game). Racing (A) gains a to the racer
and costs every other player b. Objectives are purely relative, J_i = pi_i - mean of the others.
"""
import itertools

def make_game(a=0.1, b=0.1, eps=0.0):
    def pis(prof):
        out = []
        for i, (x, m) in enumerate(prof):
            unique = all(m2 != m for j, (x2, m2) in enumerate(prof) if j != i)
            prize = (1.0 + (eps if m == 'X' else 0.0)) if unique else 0.0
            p = prize + (a if x == 'A' else 0.0) - b*sum(1 for j, (x2, m2) in enumerate(prof) if j != i and x2 == 'A')
            out.append(p)
        return out
    def O(prof):
        p = pis(prof); n = len(p)
        return [p[i] - (sum(p)-p[i])/(n-1) for i in range(n)]
    return pis, O

acts = [(x, m) for x in 'RA' for m in 'XY']

def ne_report(O, prof):
    """For each player: list of alternative actions that are payoff-equivalent (weak) or strictly better."""
    rep = []
    base = O(prof)
    for i in range(3):
        ties, better = [], []
        for act in acts:
            if act == prof[i]: continue
            q = list(prof); q[i] = act; v = O(q)[i]
            if v > base[i] + 1e-12: better.append((act, round(v, 3)))
            elif abs(v-base[i]) <= 1e-12: ties.append(act)
        rep.append((base[i], ties, better))
    return rep

def analyse(a, b, eps, label):
    pis, O = make_game(a, b, eps)
    coop = [('R', 'X')]*3
    g = max(O([act] + coop[1:])[0] for act in acts) - O(coop)[0]
    pun = [('A', 'X'), ('A', 'X'), ('A', 'Y')]
    rep = ne_report(O, pun)
    isNE = all(not r[2] for r in rep)
    v = O(pun)[0]
    print(f"{label}: a={a}, b={b}, eps={eps}")
    print(f"   cooperative deviation gain g = {g:.3f}; punishment objectives {[round(x,3) for x in O(pun)]}; stage NE in objectives: {isNE}")
    for i, (val, ties, better) in enumerate(rep):
        print(f"   player {i} ({pun[i]}): payoff-equivalent alternatives {ties}, strictly better {better}")
    # what happens if punisher 1 takes its payoff-equivalent alternative
    alt = [('A', 'X'), ('A', 'Y'), ('A', 'Y')]
    print(f"   if punisher 1 switches to its tie (A,Y): deviator's objective becomes {O(alt)[0]:+.3f} (punishment released)")
    if v < 0:
        print(f"   threshold delta* = g/(g+|v|) = {g/(g-v):.4f}")
    # role assignment: both punishers prefer the Y role
    print(f"   punisher payoffs in the X role {O(pun)[1]:+.3f} vs the Y role {O(pun)[2]:+.3f}: both prefer Y (coordination on roles needed)")

def targeted_attack():
    """Relative punishers are indifferent about WHOM they hurt: a targeted-attack game."""
    print("Targeted attack game (3 players): attacking player j costs the attacker c and costs j a loss L; relative objectives.")
    c, L = 0.1, 1.0
    # punishers 1,2 both attack 0. Payoffs: pi0 = -2L, pi1 = pi2 = -c.
    def O(pi): return [pi[i] - (sum(pi)-pi[i])/2 for i in range(3)]
    base = O([-2*L, -c, -c])
    alt_none = O([-L, 0.0, -c])        # punisher 1 abstains
    alt_other = O([-L, -c, -c-L])      # punisher 1 attacks punisher 2 instead
    print(f"   punisher 1: attack deviator {base[1]:+.3f}; abstain {alt_none[1]:+.3f}; attack the other punisher {alt_other[1]:+.3f}")
    print("   -> with theta=-1 a punisher is exactly indifferent between hurting the deviator and hurting its fellow punisher;")
    print("      role-differentiated punishment among purely relative actors is at best a weak equilibrium unless the technology targets the deviator.")

if __name__ == '__main__':
    analyse(0.1, 0.1, 0.0, "(a) the paper's game")
    analyse(0.3, 0.05, 0.0, "(b) other a, b (deviator's objective in punishment is -0.5 for every a, b)")
    analyse(0.1, 0.1, +0.02, "(c) X unique worth 1+eps: strict for punisher 1")
    analyse(0.1, 0.1, -0.02, "(d) Y unique worth more (eps<0 on X): punisher 1 strictly prefers to release the deviator")
    targeted_attack()
