"""(v2: net payoff reinvested, as in THEORY Prop 2.2(3)/3.9) Independent check of Proposition 3.9 (compounding manufactures the relative objective)
in a two-period contest, with and without a growing (positive-sum) prize.

Period 1: n actors choose intensity e_i; win prob p_i = e_i^r / sum e^r; prize W1;
          private cost c per unit; shared loss l per unit of total intensity (as in THEORY 3.4).
          Winnings W1*p_i are reinvested at rate kappa into capacity K_i = K0 + kappa*W1*p_i.
Period 2: prize W2 = W2_0 + g * sum_j K_j   (g = 0 is the paper's fixed prize);
          winnings W2 * K_i^r / sum K^r, no effort.
Actor i acts on J_i = pi_i^1 + th0 * mean_{-i} pi^1 + delta * (w_i^2 + th0 * mean_{-i} w^2).

We find the symmetric equilibrium e* by best-response iteration (numerical derivative), then
back out the static theta_eff with e(theta_eff) = e* using THEORY Prop 3.6(1):
   e(theta) = r*W1*(n-1-theta) / (n^2 (c + (1+theta) l)).
Prediction (my derivation): with lambda_rel = delta*kappa*r*W2/(n*K) and lambda_com = delta*kappa*g,
   (1+th_eff)/(n-1-th_eff) = (1+th0)(1+lambda_com) / ((n-1-th0)(1+lambda_rel)).
With g = 0 this is the paper's formula with Gamma_delta := lambda_rel/(1+lambda_rel).
Pure python, no numpy.
"""
import math

def payoffs_period1(e, i, n, r, W1, c, l):
    s = sum(x**r for x in e)
    p = [x**r / s for x in e]
    tot = sum(e)
    pi = [W1*p[k] - c*e[k] - l*tot for k in range(n)]
    return p, pi

def objective(e, i, n, r, W1, c, l, th0, delta, kappa, K0, W20, g):
    p, pi1 = payoffs_period1(e, i, n, r, W1, c, l)
    K = [max(K0 + kappa*pi1[k], 1e-9) for k in range(n)]
    W2 = W20 + g*sum(K)
    sK = sum(x**r for x in K)
    w2 = [W2 * x**r / sK for x in K]
    def J(k, vec):
        others = [vec[j] for j in range(n) if j != k]
        return vec[k] + th0 * sum(others)/(n-1)
    return J(i, pi1) + delta * J(i, w2)

def best_response(e_others, i, n, args, lo=1e-6, hi=None):
    # golden-section maximize over e_i
    if hi is None:
        hi = 1.5
    phi = (math.sqrt(5)-1)/2
    a, b = lo, hi
    def f(x):
        e = list(e_others); e[i] = x
        return objective(e, i, n, *args)
    x1 = b - phi*(b-a); x2 = a + phi*(b-a)
    f1, f2 = f(x1), f(x2)
    for _ in range(200):
        if f1 < f2:
            a = x1; x1 = x2; f1 = f2; x2 = a + phi*(b-a); f2 = f(x2)
        else:
            b = x2; x2 = x1; f2 = f1; x1 = b - phi*(b-a); f1 = f(x1)
    return (a+b)/2

def symmetric_eq(n, args, e0=0.2):
    e = e0
    for _ in range(300):
        vec = [e]*n
        br = best_response(vec, 0, n, args)
        e_new = 0.5*e + 0.5*br
        if abs(e_new - e) < 1e-12: e = e_new; break
        e = e_new
    return e

def e_static(theta, n, r, W1, c, l):
    return r*W1*(n-1-theta)/(n*n*(c + (1+theta)*l))

def theta_from_e(estar, n, r, W1, c, l):
    # solve r W1 (n-1-th) = estar n^2 (c + (1+th) l)  for th
    A = r*W1; B = estar*n*n
    # A(n-1) - A th = B c + B l + B l th  ->  th (A + B l) = A(n-1) - B(c+l)
    return (A*(n-1) - B*(c+l)) / (A + B*l)

def theta_pred(th0, n, lam_rel, lam_com):
    R = (1+th0)*(1+lam_com)/((n-1-th0)*(1+lam_rel))
    # (1+th)/(n-1-th) = R  -> 1+th = R(n-1) - R th -> th(1+R) = R(n-1)-1
    return (R*(n-1)-1)/(1+R)

def paper_theta_gamma(th0, n, Gd):
    return (n*th0 - (n-1)*(1+th0)*Gd)/(n - (1+th0)*Gd)

if __name__ == "__main__":
    n = 4; W1 = 1.0; c = 1.0; l = 0.3; delta = 0.95; kappa = 1.0; K0 = 1.0; W20 = 1.0
    print("n=%d W1=%g c=%g l=%g delta=%g kappa=%g K0=%g W2_0=%g" % (n,W1,c,l,delta,kappa,K0,W20))
    print()
    for r in (0.8, 1.0, 1.2):
        for th0 in (0.0, 1.0):
            print("--- r=%.1f  theta0=%.1f ---" % (r, th0))
            for g in (0.0, 0.5, 1.0, 2.0):
                args = (r, W1, c, l, th0, delta, kappa, K0, W20, g)
                estar = symmetric_eq(n, args)
                th_eff = theta_from_e(estar, n, r, W1, c, l)
                # evaluate lambdas at the equilibrium (K at equal standing)
                K = K0 + kappa*(W1/n - estar*(c+n*l))
                W2 = W20 + g*n*K
                lam_rel = delta*kappa*r*W2/(n*K)
                lam_com = delta*kappa*g
                th_pred = theta_pred(th0, n, lam_rel, lam_com)
                Gd = lam_rel/(1+lam_rel)
                th_paper = paper_theta_gamma(th0, n, Gd)
                print("  g=%.1f  e*=%.5f  theta_eff(num)=%+.4f  mine=%+.4f  paper(g=0 formula, Gd=%.3f)=%+.4f  lam_rel=%.3f lam_com=%.3f"
                      % (g, estar, th_eff, th_pred, Gd, th_paper, lam_rel, lam_com))
    print()
    print("Proportional prize W2 = g*sum K (W2_0 = 0): sign of manufacture depends on r vs 1")
    W20 = 0.0
    for r in (0.7, 1.0, 1.3):
        th0 = 0.5
        for g in (1.0, 3.0):
            args = (r, W1, c, l, th0, delta, kappa, K0, W20, g)
            estar = symmetric_eq(n, args)
            th_eff = theta_from_e(estar, n, r, W1, c, l)
            print("  r=%.1f th0=%.1f g=%.1f  theta_eff=%+.4f  (theta0=%.1f; narrower? %s)" % (r, th0, g, th_eff, th0, "yes" if th_eff < th0-1e-6 else "no"))
