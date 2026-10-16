"""m4: attack 4. Section 4 exponents and signs at eta != 1 and fractional xi_v, xi_f. checks_v61 CS tests only eta = 1.

Cost C(q;p) = f p^xf q + gam p^xv q^(1+eta)/(1+eta); return chi q Yhat(p)/d with Yhat(p) = p^2 Y (Prop 4.3's p^2).
q* by numerical maximization of the payoff on a log grid (not by the FOC).
Checked: size threshold exponent 1/(2-xf); q* ~ p^((2-xv)/eta); cultivated conversion p q* ~ p^(1+(2-xv)/eta);
splitting factor k^((2-xv)/eta); spending exponent 2+(2-xv)/eta; rate-law threshold alpha_ctl/(1+eta) by simulating G(t).
"""
import math

def payoff(q, p, chi, Y, d, f, xf, gam, xv, eta):
    return chi*q*p*p*Y/d - f*p**xf*q - gam*p**xv*q**(1+eta)/(1+eta)

def qstar(p, chi, Y, d, f, xf, gam, xv, eta):
    # maximize over a log grid, then refine by golden section around the best grid point
    best = (payoff(0.0, p, chi, Y, d, f, xf, gam, xv, eta), 0.0)
    grid = [10**(-10 + 50*k/2000) for k in range(2001)]
    for q in grid:
        v = payoff(q, p, chi, Y, d, f, xf, gam, xv, eta)
        if v > best[0]: best = (v, q)
    if best[1] == 0.0: return 0.0
    lo, hi = best[1]/1.05, best[1]*1.05
    g = (math.sqrt(5)-1)/2; x1 = hi-g*(hi-lo); x2 = lo+g*(hi-lo)
    fn = lambda q: payoff(q, p, chi, Y, d, f, xf, gam, xv, eta)
    f1, f2 = fn(x1), fn(x2)
    for _ in range(200):
        if f1 < f2: lo = x1; x1 = x2; f1 = f2; x2 = lo+g*(hi-lo); f2 = fn(x2)
        else: hi = x2; x2 = x1; f2 = f1; x1 = hi-g*(hi-lo); f1 = fn(x1)
    return (lo+hi)/2

def slope(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs)

if __name__ == '__main__':
    chi, Y = 1.0, 1.0
    print("(a) size threshold exponent 1/(2-xf), f=0.05, d=1, gam=1 (eta irrelevant for the threshold):")
    for xf in (0.0, 0.3, 0.7, 1.0):
        lo, hi = 1e-6, 1.0
        for _ in range(60):
            m = (lo+hi)/2
            if qstar(m, chi, Y, 1.0, 0.05, xf, 1.0, 0.0, 1.0) > 0: hi = m
            else: lo = m
        print(f"   xf={xf}: threshold {hi:.5f} vs (f/(chi Y))^(1/(2-xf)) = {(0.05/(chi*Y))**(1/(2-xf)):.5f}")
    print("(b) exponents of q*, p q*, and spending in p (f=0), by log-log regression over p in [0.05, 1]:")
    ps = [0.05*1.35**k for k in range(9) if 0.05*1.35**k <= 1.0]
    for eta in (0.5, 1.0, 2.0):
        for xv in (0.0, 0.3, 1.0):
            qs = [qstar(p, chi, Y, 1.0, 0.0, 0, 1.0, xv, eta) for p in ps]
            sq = slope([math.log(p) for p in ps], [math.log(q) for q in qs])
            spend = [1.0*p**xv*q**(1+eta)/(1+eta) for p, q in zip(ps, qs)]
            ss = slope([math.log(p) for p in ps], [math.log(s) for s in spend])
            print(f"   eta={eta}, xv={xv}: q* ~ p^{sq:.3f} (formula {(2-xv)/eta:.3f}); p q* ~ p^{sq+1:.3f} (formula {1+(2-xv)/eta:.3f}); spending ~ p^{ss:.3f} (formula {2+(2-xv)/eta:.3f})")
    print("(c) splitting factor k^((2-xv)/eta), cultivated conversion sum_k p_k q*_k, monopoly over k equal parts (f=0):")
    for eta in (0.5, 2.0):
        for xv in (0.0, 0.5, 1.0):
            mono = qstar(1.0, chi, Y, 1.0, 0.0, 0, 1.0, xv, eta)
            out = []
            for k in (2, 5):
                part = k*(1/k)*qstar(1/k, chi, Y, 1.0, 0.0, 0, 1.0, xv, eta)
                out.append(f"k={k}: {mono/part:.3f} vs {k**((2-xv)/eta):.3f}")
            print(f"   eta={eta}, xv={xv}: " + "; ".join(out))
    print("(d) rate law: G(t) = (A + aB q*(t))/(c d(t)), gam = e^{-g t}, d = d0 e^{alpha t}, g=0.2, dominant share 0.6, f=0.")
    print("    Threshold predicted alpha_ctl/(1+eta): eta=0.5 -> 0.1333, eta=2 -> 0.0667. Growth exponent of the cultivated term predicted (g-(1+eta)alpha)/eta.")
    for eta in (0.5, 2.0):
        thr = 0.2/(1+eta)
        for alpha in (thr-0.02, thr+0.02):
            vals = []
            for t in (0, 50, 100, 150):
                gam = math.exp(-0.2*t); d = 2.0*math.exp(alpha*t)
                q = qstar(0.6, chi, Y, d, 0.0, 0, gam, 0.5, eta)
                vals.append((0.3 + 0.6*q)/d)
            emp = (math.log(0.6*qstar(0.6, chi, Y, 2.0*math.exp(alpha*150), 0.0, 0, math.exp(-30), 0.5, eta)/(2.0*math.exp(alpha*150)))
                   - math.log(0.6*qstar(0.6, chi, Y, 2.0*math.exp(alpha*50), 0.0, 0, math.exp(-10), 0.5, eta)/(2.0*math.exp(alpha*50))))/100
            print(f"   eta={eta}, alpha={alpha:.4f} ({'below' if alpha < thr else 'above'} {thr:.4f}): G at t=0,50,100,150: {', '.join('%.3g'%v for v in vals)}; cultivated-term growth rate {emp:+.4f} vs (g-(1+eta)alpha)/eta = {(0.2-(1+eta)*alpha)/eta:+.4f}")
    print("(e) sign checks by finite differences at eta=1.7, xv=0.4, p=0.5: dq*/dgam, dq*/dd, dq*/dchi")
    base = dict(p=0.5, chi=1.0, Y=1.0, d=1.0, f=0.0, xf=0, gam=1.0, xv=0.4, eta=1.7)
    def q_of(**kw):
        a = dict(base); a.update(kw); return qstar(a['p'], a['chi'], a['Y'], a['d'], a['f'], a['xf'], a['gam'], a['xv'], a['eta'])
    h = 1e-3
    print(f"   dq*/dgam = {(q_of(gam=1+h)-q_of(gam=1-h))/(2*h):+.4f} (<0 expected); dq*/dd = {(q_of(d=1+h)-q_of(d=1-h))/(2*h):+.4f} (<0); dq*/dchi = {(q_of(chi=1+h)-q_of(chi=1-h))/(2*h):+.4f} (>0)")
