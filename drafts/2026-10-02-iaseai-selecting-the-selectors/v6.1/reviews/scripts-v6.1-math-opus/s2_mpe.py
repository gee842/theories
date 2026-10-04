"""Attack 1: does the price of standing (Prop 2.2(3)) and theta_Gamma (Prop 3.9) survive when the rival's
strategy responds to the state (Markov-perfect equilibrium of the stochastic game), rather than held fixed?

Two actors. Capacities K1, K2 with total held at its steady value S*, state s = K1/S*. Each period the contested
part (1-beta)Om of the prize goes to actor 1 with probability p = a1 e1/(a1 e1 + a2 e2), a_i = K_i^r (a lottery,
so the state jumps); beta*Om is split equally. Winnings convert: K1' = (1-d)K1 + kap W1 + k0 (total stays S*).
Material payoff pi1 = W1 - c e1 - l (e1+e2); objective theta_0 = 0; discount delta.

Reduced form (Props 2.2(3), 3.9): price of a unit of relative winnings lambda = Gd/(1-Gd),
Gd = Gamma delta d/(1-delta(1-d)), Gamma = (1-beta) r omega, omega = kap Om/(kap Om + 2 k0).
Three quantities are compared at s = 1/2:
  lambda_formula;
  lambda_fixed: exact (nonlinear, finite-jump) value of winning vs losing today when BOTH actors' future efforts
               are held at the symmetric level (policy evaluation): the "others' strategies fixed" premise;
  lambda_MPE:  the same difference under the Markov-perfect equilibrium (rival responds to the state).
lambda_* := delta [V(s_win) - V(s_lose)] / ((1-beta) Om). The stage game is a Tullock contest with valuations
A_i = (1-beta)Om + delta[V_i(win) - V_i(lose)], solved in closed form (unique equilibrium for positive A_i).
"""
import math

def run(r, Gamma, beta=0.0, Om=1.0, kap=0.5, d=0.2, c=1.0, l=0.0, delta=0.9, N=800, tol=1e-12, maxit=20000):
    om = Gamma / ((1 - beta) * r)
    if om > 1: return None
    k0 = kap * Om * (1 / om - 1) / 2
    S = (kap * Om + 2 * k0) / d
    jump_w = (kap * (Om * (1 - beta) + Om * beta / 2) + k0) / S
    jump_l = (kap * Om * beta / 2 + k0) / S
    grid = [i / N for i in range(N + 1)]
    def interp(arr, x):
        if x <= 0: return arr[0]
        if x >= 1: return arr[-1]
        k = min(int(x * N), N - 1); w = x * N - k
        return arr[k] * (1 - w) + arr[k + 1] * w
    def nxt(s):
        return (1 - d) * s + jump_w, (1 - d) * s + jump_l
    def stage(s, V):
        sw, sl = nxt(s)
        A1 = (1 - beta) * Om + delta * (interp(V, sw) - interp(V, sl))
        A2 = (1 - beta) * Om + delta * (interp(V, 1 - sl) - interp(V, 1 - sw))
        if s <= 0: a1, a2 = 0.0, 1.0
        elif s >= 1: a1, a2 = 1.0, 0.0
        else: a1, a2 = s ** r, (1 - s) ** r
        A1p, A2p = max(A1, 0.0), max(A2, 0.0)
        if a1 * A1p + a2 * A2p == 0: return 0.5, 0.0, 0.0, sw, sl
        p = a1 * A1p / (a1 * A1p + a2 * A2p)
        e1 = A1p * p * (1 - p) / (c + l); e2 = A2p * p * (1 - p) / (c + l)
        return p, e1, e2, sw, sl
    # --- MPE by value iteration
    V = [0.0] * (N + 1)
    for it in range(maxit):
        Vn = []
        for s in grid:
            p, e1, e2, sw, sl = stage(s, V)
            Vn.append((1 - beta) * Om * p + beta * Om / 2 - c * e1 - l * (e1 + e2)
                      + delta * (p * interp(V, sw) + (1 - p) * interp(V, sl)))
        diff = max(abs(a - b) for a, b in zip(V, Vn)); V = Vn
        if diff < tol: break
    p, e1, e2, sw, sl = stage(0.5, V)
    lam_mpe = delta * (interp(V, sw) - interp(V, sl)) / ((1 - beta) * Om)
    # --- others fixed: efforts held equal forever, so p = a1/(a1+a2); value of own future winnings only
    W = [0.0] * (N + 1)
    for it2 in range(maxit):
        Wn = []
        for s in grid:
            if s <= 0: pp = 0.0
            elif s >= 1: pp = 1.0
            else: pp = s ** r / (s ** r + (1 - s) ** r)
            sw2, sl2 = nxt(s)
            Wn.append((1 - beta) * Om * pp + delta * (pp * interp(W, sw2) + (1 - pp) * interp(W, sl2)))
        dd = max(abs(a - b) for a, b in zip(W, Wn)); W = Wn
        if dd < tol: break
    sw2, sl2 = nxt(0.5)
    lam_fixed = delta * (interp(W, sw2) - interp(W, sl2)) / ((1 - beta) * Om)
    Gd = Gamma * delta * d / (1 - delta * (1 - d))
    lam = Gd / (1 - Gd) if Gd < 1 else float('inf')
    e_rf = (1 - beta) * Om * (1 + lam) / (4 * (c + l))
    # rival's effort response to the state at s=1/2
    h = 4.0 / N
    _, e1a, e2a, _, _ = stage(0.5 + h, V); _, e1b, e2b, _, _ = stage(0.5 - h, V)
    # global best-response check for actor 1 at s=1/2
    sw, sl = nxt(0.5)
    A1 = (1 - beta) * Om + delta * (interp(V, sw) - interp(V, sl))
    def pay(x):
        pp = x / (x + e2) if x + e2 > 0 else 0.5
        return A1 * pp - (c + l) * x
    best = max(pay(e2 * 10 ** (k / 100.0)) for k in range(-400, 401))
    return dict(k0=k0, jump=jump_w - jump_l, Gd=Gd, lam=lam, lam_fixed=lam_fixed, lam_mpe=lam_mpe, e_rf=e_rf, e_mpe=e1,
                de1=(e1a - e1b) / (2 * h), de2=(e2a - e2b) / (2 * h), conv=(it, diff, it2, dd), br_gap=best - pay(e1))

if __name__ == '__main__':
    import sys
    print(__doc__.split('\n')[0])
    for d in (0.2, 0.05):
        for r in (1.0, 1.5):
            for G in (0.3, 0.6, 0.9, 1.2):
                if G / r > 1: continue
                res = run(r, G, d=d)
                th = lambda L: -L / (2 + L)   # n=2: theta = -lam(n-1)/(n+lam(n-1))
                print(f"d={d} r={r} Gamma={G}: jump={res['jump']:.3f} Gd={res['Gd']:.3f} | lambda formula {res['lam']:.4f}, "
                      f"fixed {res['lam_fixed']:.4f}, MPE {res['lam_mpe']:.4f} (MPE/formula {res['lam_mpe']/res['lam']:.3f}) | "
                      f"theta_Gamma {th(res['lam']):+.3f}, theta_MPE {th(res['lam_mpe']):+.3f} | e_RF {res['e_rf']:.4f} e_MPE {res['e_mpe']:.4f} | "
                      f"de1/ds {res['de1']:+.3f} de2/ds {res['de2']:+.3f} | BR gap {res['br_gap']:.1e} | conv {res['conv'][0]},{res['conv'][1]:.0e}", flush=True)
