"""m2: attack 1. Does the price of standing (Prop 2.2(3), Prop 3.9) survive when the rivals' future
strategies respond to the state?

Two-period game. Period 1: Tullock contest in effort e_i (r=1), prize Om1, unit cost c, shared loss l.
Capacity K_i = K0 + kap*pi_i. Period 2: a Tullock contest in EFFORT f_i with strengths alpha_i = K_i^r2,
w_i = alpha_i f_i / sum alpha_k f_k, prize Om2, unit cost c2. Period-2 equilibrium efforts respond to the
capacities (closed form for r_f = 1; verified by a best-response check).

Reduced form (the paper): lambda_red = delta * kap * n/(n-1) * d/dK_i [Om2 w_i] with rivals' f fixed.
Full game:                 lambda_full = delta * kap * n/(n-1) * dV_i/dK_i with f* re-solved (envelope on own f).
Both give theta = -lam(n-1)/(n+lam(n-1)) and e(theta) = Om1 (n-1-theta)/(n^2 (c+(1+theta) l)).
The direct symmetric subgame-perfect first-period intensity is computed by best-response iteration and compared.
"""
import math

def period2(alpha, Om2, c2):
    n = len(alpha); Sig = sum(1/a for a in alpha)
    X = Om2*(n-1)/(c2*Sig)
    f = [X/alpha[k]*(1 - (n-1)/(alpha[k]*Sig)) for k in range(n)]
    if min(f) <= 0: raise ValueError('corner')
    w = [alpha[k]*f[k]/X for k in range(n)]
    V = [Om2*w[k] - c2*f[k] for k in range(n)]
    return f, w, V

def check_p2_br(alpha, Om2, c2):
    f, w, V = period2(alpha, Om2, c2)
    n = len(alpha); worst = 0.0
    for i in range(n):
        others = sum(alpha[k]*f[k] for k in range(n) if k != i)
        best = max((Om2*alpha[i]*x/(alpha[i]*x + others) - c2*x, x) for x in [f[i]*j/500 for j in range(1, 1501)])
        worst = max(worst, abs(best[1]-f[i])/f[i])
    return worst

def golden(fn, lo, hi, it=200):
    g = (math.sqrt(5)-1)/2; x1 = hi-g*(hi-lo); x2 = lo+g*(hi-lo); f1, f2 = fn(x1), fn(x2)
    for _ in range(it):
        if f1 < f2: lo = x1; x1 = x2; f1 = f2; x2 = lo+g*(hi-lo); f2 = fn(x2)
        else: hi = x2; x2 = x1; f2 = f1; x1 = hi-g*(hi-lo); f1 = fn(x1)
    return (lo+hi)/2

def solve(n=3, Om1=1.0, c=1.0, l=0.3, K0=2.0, kap=0.5, Om2=2.0, r2=1.5, c2=1.0, dl=0.9):
    def U(i, es):
        E = sum(es); S = sum(es)
        pis = [Om1*es[j]/S - c*es[j] - l*E for j in range(n)]
        Ks = [K0 + kap*p for p in pis]
        if min(Ks) <= 0: return -1e9
        alpha = [k**r2 for k in Ks]
        try: f, w, V = period2(alpha, Om2, c2)
        except ValueError: return -1e9
        return pis[i] + dl*V[i]
    def br(e_other):
        return golden(lambda x: U(0, [x] + [e_other]*(n-1)), 1e-6, 3.0)
    e = 0.2
    for _ in range(400):
        en = br(e)
        if abs(en-e) < 1e-13: break
        e = 0.5*e + 0.5*en
    # symmetric capacities at the equilibrium
    pibar = Om1/n - c*e - l*n*e; Kbar = K0 + kap*pibar
    alpha0 = [Kbar**r2]*n
    f0, w0, V0 = period2(alpha0, Om2, c2)
    h = 1e-6
    # reduced: rivals' f fixed at f0, own f fixed too (first order in w only, as in LG(C) where there is no effort)
    def w_fixed(Ki):
        ai = Ki**r2; return Om2*ai*f0[0]/(ai*f0[0] + sum(alpha0[k]*f0[k] for k in range(1, n)))
    dW_red = (w_fixed(Kbar+h) - w_fixed(Kbar-h))/(2*h)
    # full: re-solve period 2
    def Vfull(Ki):
        alpha = [Ki**r2] + [Kbar**r2]*(n-1); f, w, V = period2(alpha, Om2, c2); return V[0]
    dV_full = (Vfull(Kbar+h) - Vfull(Kbar-h))/(2*h)
    lam_red = dl*kap*n/(n-1)*dW_red
    lam_full = dl*kap*n/(n-1)*dV_full
    def e_of(lam):
        th = -lam*(n-1)/(n+lam*(n-1))
        return Om1*(n-1-th)/(n*n*(c+(1+th)*l)), th
    e_red, th_red = e_of(lam_red); e_full, th_full = e_of(lam_full)
    return e, e_red, e_full, lam_red, lam_full, th_red, th_full, check_p2_br(alpha0, Om2, c2)

if __name__ == '__main__':
    print("Two-period game with endogenous period-2 effort (strength K^r2 * f). Direct symmetric SPE intensity e* vs the")
    print("reduced-form e(theta(lambda_red)) [rivals' strategies fixed, as in Prop 2.2(3)] and e(theta(lambda_full)) [rivals respond].")
    print("Analytic prediction for r_f=1 Tullock: lambda_full/lambda_red = 2(n-1)/n (rivals are discouraged by a stronger field).")
    for kw in [dict(n=2), dict(n=3), dict(n=4), dict(n=6), dict(n=3, r2=1.0, Om2=4.0), dict(n=4, dl=0.5), dict(n=3, kap=1.0, K0=1.0)]:
        e, e_red, e_full, lr, lf, tr, tf, brerr = solve(**kw)
        n = kw.get('n', 3)
        print(f"   {kw}: e*={e:.6f}; e(theta_red)={e_red:.6f} (lam_red={lr:.4f}, theta={tr:+.4f}); e(theta_full)={e_full:.6f} (lam_full={lf:.4f}, theta={tf:+.4f}); "
              f"lam_full/lam_red={lf/lr:.4f} vs 2(n-1)/n={2*(n-1)/n:.4f}; period-2 BR check err {brerr:.1e}")
    print("Reading: the first-order structure (objective pi_i + lambda(pi_i - mean)) survives in the full game, but lambda is the")
    print("full derivative dV_i/dK_i, not the reduced one. Here the strategic term is positive (rivals reduce effort), so the reduced")
    print("form UNDERSTATES the price of standing by a factor approaching 2 as n grows; with a different period-2 technology the sign")
    print("of the correction can differ. The reduced form is exact only for n=2 in this technology.")
