"""f5: Proposition 4.5 (corrrate): the rate law's two halves under finite adjustment, the falling-f branch,
marginal-cost floor vs lump-sum fixed cost, and the definition of Y_hat.  Standard library only.

Model (as in checks CS / the reviewers' joint simulations): chi = Yhat = eta = 1, xi_v = 0, dominant share p = 0.6,
A = 0.3, a_ev B_hat = c_ev = 1, d(t) = d0 e^{alpha_cor t} with d0 = 2, gamma(t) = e^{-alpha_ctl t}, alpha_ctl = 0.2.
Rate-law threshold alpha_ctl/(1+eta) = 0.1.  Certificate G_ev = (A + p q)/d < 1.  q* = [(p^2/d - f)/gamma]_+^(1/eta).

(A) sufficiency under any lag with q <= q*; necessity iff liminf q/q* > 0 (constant-rate lag R(k) tracks at ratio
    k/(k+g), g = (alpha_ctl-alpha_cor)/eta; the failure delay is eta ln(1+g/k)/(alpha_ctl-(1+eta)alpha_cor));
    constant-variance gradient dynamics GA(V): q bounded by q0 + V p^2/(d0 alpha_cor), so no failure for any alpha_cor>0.
(B) the falling-f branch: cultivation is positive iff d(t) < d_f(t) = p^2/f(t); under [H_f] d_f rises at alpha_f.
    Cases alpha_cor > alpha_f (cultivation ends; amplitude matters), alpha_cor < alpha_f (f=0 law decides),
    alpha_cor = alpha_f (initial ratio decides).  Codex's counterexample.
(C) lump-sum fixed cost F (paid iff q>0): threshold exponent eta/(2 eta + 2 - xi_v - eta xi_f); requirement does not
    level off as gamma -> 0; the linear 'f' (marginal-cost floor) does level off.
(D) Yhat = p^2 ybar^T Ahat ybar: q* proportional to p^{(2-xi_v)/eta}, so splitting into k parts divides Yhat by k^2.
"""
import math

p, A, d0, actl = 0.6, 0.3, 2.0, 0.2
def gam(t): return math.exp(-actl * t)
def dd(t, a): return d0 * math.exp(a * t)
def qstar(t, a, f=0.0, eta=1.0):
    m = p * p / dd(t, a) - f
    return (m / gam(t)) ** (1 / eta) if m > 0 else 0.0

def run(acor, mode, par=None, H=400.0, dt=0.01):
    q = qstar(0, 0.0); t = 0.0; first = None; smax = 0.0
    while t < H:
        tm = t + dt / 2; qs = qstar(tm, acor); d = dd(tm, acor)
        if mode == "QS": q = qs
        elif mode == "R": q = qs + (q - qs) * math.exp(-par * dt)
        elif mode == "GA": q = max(0.0, q + dt * par * (p * p / d - gam(tm) * q))
        elif mode == "GM": q = qs + (q - qs) * math.exp(-(par / qstar(0, 0.0) ** 2) * q * q * gam(tm) * dt)
        G = (A + p * q) / d
        if G > 1 and first is None: first = t
        smax = max(smax, G); t += dt
    return first, smax, q

def part_A():
    print("(A) rate law under finite adjustment (threshold 0.1)")
    for acor in (0.05, 0.08, 0.09, 0.11):
        row = []
        for mode, par in [("QS", None), ("R", 0.3), ("R", 0.1), ("R", 0.03), ("GA", 1.0), ("GM", 1.0)]:
            fi, sm, q = run(acor, mode, par)
            row.append(f"{mode}{'' if par is None else '('+str(par)+')'}: {('%.1f' % fi) if fi is not None else 'never'}")
        print(f"   alpha_cor={acor}: first failure -> " + " | ".join(row))
    print("   constant-rate lag: delay vs eta ln(1+g/k)/(alpha_ctl-(1+eta)alpha_cor), g=(alpha_ctl-alpha_cor)/eta")
    for acor in (0.05, 0.08):
        tq = run(acor, "QS")[0]
        for k in (0.3, 0.1, 0.03):
            tr = run(acor, "R", k)[0]; g = actl - acor
            print(f"      alpha_cor={acor}, k={k}: delay {tr-tq:.2f} vs formula {math.log(1+g/k)/(actl-2*acor):.2f}")
    print("   GA bound: q(t) <= q0 + V p^2/(d0 alpha_cor)")
    for acor in (0.02, 0.05):
        fi, sm, q = run(acor, "GA", 1.0, H=600.0)
        print(f"      alpha_cor={acor}: q(600)={q:.3f} <= bound {qstar(0,0.0)+p*p/(d0*acor):.3f}; max G_ev over [0,600] = {sm:.3f} ({'never fails' if fi is None else 'fails at %.1f'%fi})")

def run_f(acor, af, f0, H=600.0, dt=0.02):
    t = 0.0; first = None; smax = 0.0; endcult = None
    while t < H:
        f = f0 * math.exp(-af * t); q = qstar(t, acor, f); d = dd(t, acor)
        if q == 0 and endcult is None and t > 0: endcult = t
        G = (A + p * q) / d
        if G > 1 and first is None: first = t
        smax = max(smax, G); t += dt
    return first, smax, endcult

def part_B():
    print("(B) falling f (marginal-cost floor): cultivation on iff d(t) < d_f(t) = p^2/f(t); d_f(0)/d0 = p^2/(f0 d0)")
    print("   Codex: eta=p=1, A=0, gamma=e^{-.2t}, d=2e^{.05t}, f=.49e^{-.01t}: q*=[.5e^{-.05t}-.49e^{-.01t}]_+ e^{.2t}")
    def q_codex(t): return max(0.0, (0.5 * math.exp(-0.05 * t) - 0.49 * math.exp(-0.01 * t))) * math.exp(0.2 * t)
    print(f"      q*(0)={q_codex(0):.4f}, q*(0.3)={q_codex(0.3):.5f}, q*(0.6)={q_codex(0.6):.4f}, q*(5)={q_codex(5):.4f}; cutoff ln(.5/.49)/.04={math.log(0.5/0.49)/0.04:.4f}; alpha_cor=.05<.1 yet the certificate never fails")
    print("   this model (alpha_ctl=.2, eta=1): alpha_f=0.05")
    for f0 in (0.1, 0.17, 0.3):
        for acor in (0.05, 0.051, 0.06, 0.08, 0.11):
            fi, sm, ec = run_f(acor, 0.05, f0)
            ratio = p * p / (f0 * d0)
            print(f"      f0={f0} (d_f(0)/d0={ratio:.2f}), alpha_cor={acor}: first failure {('%.1f'%fi) if fi is not None else 'never'}, max G_ev {sm:.3g}, cultivation ends {('%.0f'%ec) if ec else 'never'}")
    print("   -> alpha_cor > alpha_f alone is NOT sufficient (f0=0.1, alpha_cor=0.051: fails at a finite time although cultivation ends later);")
    print("      alpha_cor = alpha_f: the initial ratio d_f(0)/d0 decides (f0=0.17: 1.06>1 -> no cultivation, holds; f0=0.1: 1.8 -> f=0 law, fails)")
    print("   S4's 'that level falls at alpha_f': d_f(t)=p^2/f(t) with f falling RISES:", ", ".join(f"t={t}: {p*p/(0.3*math.exp(-0.05*t)):.3f}" for t in (0, 10, 20)))

def qopt(pp, chi, Y, d, f, xf, g, xv, eta):
    def dpay(q): return chi * pp * pp * Y / d - f * pp ** xf - g * pp ** xv * q ** eta
    if dpay(0.0) <= 0: return 0.0
    lo, hi = -400.0, 400.0
    for _ in range(200):
        m = (lo + hi) / 2
        if dpay(math.exp(m)) > 0: lo = m
        else: hi = m
    return math.exp((lo + hi) / 2)

def part_C():
    print("(C) lump-sum fixed cost F p^xf (paid iff q>0) vs the linear floor f p^xf q")
    def threshold(F, xf, xv, eta, lump):
        lo, hi = 1e-9, 1.0
        for _ in range(100):
            m = (lo + hi) / 2
            if lump:
                q = qopt(m, 1, 1, 1, 0, xf, 1, xv, eta)
                pos = q * m * m - m ** xv * q ** (1 + eta) / (1 + eta) - F * m ** xf > 0
            else:
                pos = qopt(m, 1, 1, 1, F, xf, 1, xv, eta) > 0
            if pos: hi = m
            else: lo = m
        return hi
    for (xf, xv, eta) in [(0, 0, 1), (1, 1, 1), (0, 0, 2), (0, 1, 0.5)]:
        e_l = (math.log(threshold(2e-3, xf, xv, eta, True)) - math.log(threshold(1e-3, xf, xv, eta, True))) / math.log(2)
        e_f = (math.log(threshold(2e-3, xf, xv, eta, False)) - math.log(threshold(1e-3, xf, xv, eta, False))) / math.log(2)
        print(f"   xf={xf} xv={xv} eta={eta}: lump-sum threshold exponent {e_l:.4f} (predicted eta/(2eta+2-xv-eta xf)={eta/(2*eta+2-xv-eta*xf):.4f}); linear-floor exponent {e_f:.4f} (1/(2-xf)={1/(2-xf):.4f})")
    def dstar(g, F, lump):
        def G(d):
            if lump:
                q = qopt(p, 1, 1, d, 0, 0, g, 0, 1.0); prof = q * p * p / d - g * q * q / 2 - F
                q = q if prof > 0 else 0.0
            else: q = qopt(p, 1, 1, d, F, 0, g, 0, 1.0)
            return (A + p * q) / d
        lo, hi = 1e-6, 1e9
        for _ in range(200):
            m = math.sqrt(lo * hi)
            if G(m) > 1: lo = m
            else: hi = m
        return hi
    for g in (1.0, 1e-2, 1e-4, 1e-6):
        print(f"   gamma={g:.0e}: required d* with linear floor f=0.3: {dstar(g,0.3,False):.3f}; with lump-sum F=0.3: {dstar(g,0.3,True):.3f}; with f=0: {dstar(g,0.0,False):.3f}")
    print("   -> the linear floor caps the requirement (levels off at p^2/f = 1.2); a true fixed cost only delays cultivation")

def part_D():
    print("(D) Yhat = p^2 ybar^T Ahat ybar: q* scaling in p (f=0) is p^{(2-xi_v)/eta}; splitting into k parts divides Yhat by k^2")
    for (xv, eta) in [(0, 1), (1, 1), (0, 2), (0.5, 0.5)]:
        q1 = qopt(0.3, 1, 1, 1, 0, 0, 1, xv, eta); q2 = qopt(0.6, 1, 1, 1, 0, 0, 1, xv, eta)
        print(f"   xi_v={xv} eta={eta}: d ln q*/d ln p = {math.log(q2/q1)/math.log(2):.4f} vs (2-xi_v)/eta = {(2-xv)/eta:.4f}")

if __name__ == "__main__":
    part_A(); part_B(); part_C(); part_D()
