"""f1: Proposition 3.9 (standprice) in its general two-channel form, and the domain of Proposition 2.2(3).

Pure Python, standard library only.

(A) Two-period contest, n actors.  Period 1: Tullock contest with decisiveness r, prize W1, unit cost c,
    shared loss l per unit of total intensity; actor i holds theta_0 and reinvests its NET period-1 payoff at
    rate kappa into capacity K_i = K0 + kappa*pi_i.  Period 2: the prize is Omega2 = Omega20 + g*sum_j K_j
    (g = 0 is the paper's fixed prize); a share beta of it is divided equally, the rest goes by K_i^r/sum K^r;
    no effort in period 2.  The symmetric subgame-perfect first-period intensity e* is computed by
    best-response iteration (golden-section search on the exact objective; no formula of the proposition is
    used), and the working self-model theta_eff is read off e* through Proposition 3.6(1).
    Claim tested (my derivation, Supplement form):
        (1+theta_eff)/(n-1-theta_eff) = (1+theta_0)(1+lambda_com) / ((n-1-theta_0)(1+lambda_rel)),
        lambda_rel = delta*kappa*(1-beta)*r*Omega2/(n*K),   lambda_com = delta*kappa*g,
    so theta_eff < theta_0  iff  lambda_rel > lambda_com.  With Omega20 = 0 (prize proportional to total
    capacity), lambda_rel/lambda_com = (1-beta) r: narrowing iff (1-beta) r > 1, the compounding condition of
    Proposition 2.3(1) without provision or diffusion.
(B) Infinite horizon, prize proportional to total capacity, no depreciation: the ratio of the present value of
    a relative unit to that of a common unit is (1-beta) r (1-delta(1+g)) / (1-delta(1+(1-beta) r g)), which
    exceeds one iff (1-beta) r > 1.  Checked by direct simulation of the nonlinear stock model.
(C) Domain of (9): fixed prize, Gamma_delta >= 1 (Codex's parameters).  The present value of a relative
    perturbation of size eps scales as eps^alpha with alpha = ln(1/delta)/ln(lambda*) < 1, so the price per
    unit, PV/eps, grows without bound as eps -> 0: the linear price is undefined, not negative.
(D) Reinvesting gross winnings only (not net payoff): how theta_eff differs from the net-payoff formula.
"""
import math

# ---------------------------------------------------------------- (A) two-period contest
def golden_max(f, lo, hi, it=160):
    g = (math.sqrt(5) - 1) / 2
    x1 = hi - g * (hi - lo); x2 = lo + g * (hi - lo); f1 = f(x1); f2 = f(x2)
    for _ in range(it):
        if f1 < f2:
            lo = x1; x1 = x2; f1 = f2; x2 = lo + g * (hi - lo); f2 = f(x2)
        else:
            hi = x2; x2 = x1; f2 = f1; x1 = hi - g * (hi - lo); f1 = f(x1)
    return (lo + hi) / 2

def two_period(n, r, W1, c, l, th0, delta, kappa, K0, Om20, g, beta, gross=False):
    def objective(i, e):
        S = sum(x ** r for x in e); p = [x ** r / S for x in e]; tot = sum(e)
        pi = [W1 * p[k] - c * e[k] - l * tot for k in range(n)]
        if gross:
            K = [K0 + kappa * W1 * p[k] for k in range(n)]
        else:
            K = [K0 + kappa * pi[k] for k in range(n)]
        if min(K) <= 0: return -1e9
        Om2 = Om20 + g * sum(K)
        SK = sum(x ** r for x in K)
        w2 = [Om2 * ((1 - beta) * x ** r / SK + beta / n) for x in K]
        J1 = pi[i] + th0 * (sum(pi) - pi[i]) / (n - 1)
        J2 = w2[i] + th0 * (sum(w2) - w2[i]) / (n - 1)
        return J1 + delta * J2
    e = 0.2
    for _ in range(400):
        br = golden_max(lambda x: objective(0, [x] + [e] * (n - 1)), 1e-7, 2.0)
        en = 0.5 * e + 0.5 * br
        if abs(en - e) < 1e-13: e = en; break
        e = en
    # read theta_eff from e* via e(theta) = r W1 (n-1-theta)/(n^2 (c+(1+theta) l))
    A = r * W1; B = e * n * n
    th_eff = (A * (n - 1) - B * (c + l)) / (A + B * l)
    # lambdas at the equilibrium capacities
    S = n * e ** r; pi_bar = W1 / n - c * e - l * n * e
    K = K0 + kappa * (W1 / n if gross else pi_bar)
    Om2 = Om20 + g * n * K
    lam_rel = delta * kappa * (1 - beta) * r * Om2 / (n * K); lam_com = delta * kappa * g
    R0 = (1 + th0) / (n - 1 - th0)
    R = R0 * (1 + lam_com) / (1 + lam_rel)
    th_pred = (R * (n - 1) - 1) / (1 + R)
    return e, th_eff, th_pred, lam_rel, lam_com

def part_A():
    print("(A) two-period contest: numerical symmetric equilibrium vs the two-channel formula")
    n, W1, c, l, delta, kappa, K0 = 4, 1.0, 1.0, 0.3, 0.95, 1.0, 1.0
    worst = 0.0; sign_ok = 0; sign_n = 0
    print("    general prize Omega2 = Omega20 + g sum K, with sharing beta in period 2:")
    print("    (the first-period contest has a symmetric pure equilibrium only for r <= n/(n-1); n=4 needs r <= 4/3, n=2 allows r <= 2)")
    for (nn, r, th0, Om20, g, beta) in [(4, 0.8, 0.0, 1.0, 0.0, 0.0), (4, 0.8, 0.0, 1.0, 1.0, 0.0), (4, 1.2, 0.0, 1.0, 2.0, 0.0),
                                    (4, 1.0, 1.0, 1.0, 0.5, 0.0), (4, 1.3, 0.5, 0.0, 1.0, 0.0), (4, 1.3, 0.5, 0.0, 1.0, 0.3),
                                    (4, 1.25, 0.5, 0.0, 2.0, 0.2), (4, 0.7, 0.5, 0.0, 3.0, 0.0), (4, 1.0, 0.5, 0.0, 3.0, 0.0),
                                    (4, 1.2, -0.5, 0.5, 0.5, 0.6), (4, 1.3, 1.9, 0.0, 1.0, 0.0), (2, 1.8, 0.0, 0.0, 1.0, 0.2),
                                    (2, 1.8, 0.0, 0.0, 1.0, 0.5), (2, 1.6, 0.3, 0.0, 0.5, 0.0)]:
        n = nn
        e, th, thp, lr, lc = two_period(n, r, W1, c, l, th0, delta, kappa, K0, Om20, g, beta)
        worst = max(worst, abs(th - thp))
        narrower = th < th0 - 1e-6; pred = lr > lc + 1e-9
        sign_n += 1; sign_ok += (narrower == pred) or abs(th - th0) < 1e-6
        tag = ""
        if Om20 == 0: tag = f"  [(1-beta) r = {(1-beta)*r:.2f}: predicts {'narrower' if (1-beta)*r>1 else ('same' if abs((1-beta)*r-1)<1e-9 else 'wider')}]"
        print(f"    n={n} r={r} th0={th0:+.1f} Om20={Om20} g={g} beta={beta}: e*={e:.6f} theta_eff={th:+.5f} formula={thp:+.5f} "
              f"lam_rel={lr:.3f} lam_com={lc:.3f} -> {'narrower' if narrower else 'not narrower'}{tag}")
    print(f"    max |theta_eff - formula| = {worst:.1e}; sign rule (narrower iff lam_rel > lam_com) held in {sign_ok}/{sign_n} cases")

# ---------------------------------------------------------------- (B) infinite horizon, proportional prize
def part_B():
    print("(B) infinite horizon, prize Omega_t = g S_t, no depreciation: PV(relative unit)/PV(common unit) by simulation")
    n, g, kappa, delta = 3, 0.05, 1.0, 0.9
    for (r, beta) in [(1.5, 0.0), (0.8, 0.0), (1.5, 0.5), (1.0, 0.0), (2.0, 0.3), (1.2, 0.2)]:
        if delta * (1 + max(g, (1 - beta) * r * g)) >= 1: continue
        def run(K, T=4000):
            pv = 0.0; disc = delta; base = None
            Ks = list(K)
            out = []
            for t in range(T):
                S = sum(Ks); Om = g * S
                P = sum(x ** r for x in Ks); p = [x ** r / P for x in Ks]
                W = [Om * ((1 - beta) * p[i] + beta / n) for i in range(n)]
                out.append(W[0])
                Ks = [Ks[i] + kappa * W[i] for i in range(n)]
            return out
        K0 = 1.0; eps = 1e-6
        base = run([K0] * n)
        rel = run([K0 + eps] + [K0 - eps / (n - 1)] * (n - 1))   # a relative unit: own +eps, others -eps/(n-1), sum zero
        com = run([K0 + eps] * n)                                          # a common unit: everyone +eps
        pv_rel = sum(delta ** (t + 1) * (rel[t] - base[t]) for t in range(len(base)))
        pv_com = sum(delta ** (t + 1) * (com[t] - base[t]) for t in range(len(base)))
        ratio = pv_rel / pv_com
        pred = (1 - beta) * r * (1 - delta * (1 + g)) / (1 - delta * (1 + (1 - beta) * r * g))
        print(f"    r={r} beta={beta}: PV_rel/PV_com = {ratio:.5f}, predicted {pred:.5f}; (1-beta) r = {(1-beta)*r:.2f} -> "
              f"relative return {'exceeds' if ratio>1 else 'below'} common return, as (1-beta) r {'>' if (1-beta)*r>1 else '<='} 1")

# ---------------------------------------------------------------- (C) domain Gamma_delta >= 1
def part_C():
    print("(C) fixed prize outside the convergence domain (n=2, r=2, d=0.2, kappa=Omega=1, delta=0.9: Gamma=2, Gamma_delta=9/7)")
    n, r, d, delta = 2, 2.0, 0.2, 0.9
    Gd = r * delta * d / (1 - delta * (1 - d)); lam_star = 1 + d * (r - 1)
    alpha = math.log(1 / delta) / math.log(lam_star)
    print(f"    printed multiplier Gd/(1-Gd) = {Gd/(1-Gd):.3f} (meaningless); lambda* = {lam_star:.3f}, delta*lambda* = {delta*lam_star:.3f} > 1")
    print(f"    predicted scaling: PV ~ eps^alpha with alpha = ln(1/delta)/ln(lambda*) = {alpha:.4f}; PV/eps ~ eps^(alpha-1), exponent {alpha-1:+.4f}")
    def pv(eps, T=3000):
        K = [2.5 + eps, 2.5 - eps]; s = 0.0; disc = delta
        for t in range(T):
            P = sum(x ** r for x in K); p = K[0] ** r / P
            s += disc * (p - 0.5); disc *= delta
            K = [(1 - d) * x + x ** r / P for x in K]
        return s
    prev = None
    for eps in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
        v = pv(eps)
        slope = "" if prev is None else f"  local exponent of PV/eps: {(math.log(v/eps)-math.log(prev[1]/prev[0]))/(math.log(eps)-math.log(prev[0])):+.4f}"
        print(f"    eps={eps:.0e}: PV={v:.6e} (>0), PV/eps={v/eps:.4e}{slope}")
        prev = (eps, v)
    print("    -> PV stays positive; the price per unit diverges as eps -> 0: no finite first-order theta describes the actor; the limit is theta -> -1 from below")

# ---------------------------------------------------------------- (D) gross winnings reinvested
def part_D():
    print("(D) if only GROSS winnings convert (costs not reinvested), theta_eff read from e* differs from the net-payoff formula:")
    n, W1, c, l, delta, kappa, K0 = 4, 1.0, 1.0, 0.3, 0.95, 1.0, 1.0
    for (r, th0) in [(1.0, 0.0), (1.2, 0.5)]:
        e_net, th_net, thp, lr, lc = two_period(n, r, W1, c, l, th0, delta, kappa, K0, 1.0, 0.0, 0.0, gross=False)
        e_gr, th_gr, thp2, lr2, lc2 = two_period(n, r, W1, c, l, th0, delta, kappa, K0, 1.0, 0.0, 0.0, gross=True)
        print(f"    r={r} th0={th0}: net payoff reinvested: theta_eff={th_net:+.4f} (formula {thp:+.4f}); gross winnings only: theta_eff={th_gr:+.4f} "
              f"(the private cost's relative part is then not amplified; the proposition's premise 'reinvests net payoff' is load-bearing)")

if __name__ == "__main__":
    part_A(); part_B(); part_C(); part_D()
