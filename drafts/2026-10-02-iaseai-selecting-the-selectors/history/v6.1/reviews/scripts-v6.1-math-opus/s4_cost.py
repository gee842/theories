"""Section 4 of V6.1: Assumption 4.2 cost C(q;p) = f p^xf q + gam p^xv q^(1+eta)/(1+eta); Props 4.3-4.5.
(a) exponents by numerical differentiation of log-quantities over random (xf, xv, eta): threshold, q*, splitting,
    concentration, spending;
(b) the 'fixed part' f is a constant MARGINAL cost (linear in q). With a genuine lump-sum fixed cost the threshold
    exponent and Prop 4.5(3) ('requirement levels off') change;
(c) the quasi-static assumption: capacity q following selection with finite speed instead of sitting at q*(t).
"""
import math, random

def qstar(p, chi, Y, d, f, xf, gam, xv, eta):
    # maximize chi q p^2 Y/d - f p^xf q - gam p^xv q^(1+eta)/(1+eta) by bisection on derivative (log scale)
    def dpay(q): return chi * p * p * Y / d - f * p ** xf - gam * p ** xv * q ** eta
    if dpay(0.0) <= 0: return 0.0
    lo, hi = -400.0, 400.0
    for _ in range(200):
        m = (lo + hi) / 2
        if dpay(math.exp(m)) > 0: lo = m
        else: hi = m
    return math.exp((lo + hi) / 2)

def threshold(f, xf, chi=1.0, Y=1.0, d=1.0, gam=1.0, xv=0.0, eta=1.0, lump=False):
    lo, hi = 1e-9, 1.0
    for _ in range(100):
        m = (lo + hi) / 2
        if lump:
            q = qstar(m, chi, Y, d, 0.0, xf, gam, xv, eta)
            prof = chi * q * m * m * Y / d - gam * m ** xv * q ** (1 + eta) / (1 + eta) - f * m ** xf
            pos = prof > 0
        else:
            pos = qstar(m, chi, Y, d, f, xf, gam, xv, eta) > 0
        if pos: hi = m
        else: lo = m
    return hi

rnd = random.Random(7)
print("(a) exponents, numerical, 300 random (xf, xv, eta):")
bad = dict(thr=0, split=0, conc=0, spend=0)
for _ in range(300):
    xf, xv, eta = rnd.uniform(0, 1), rnd.uniform(0, 1), rnd.uniform(0.2, 3)
    # threshold exponent: p* = (f/chiY)^(1/(2-xf))  ->  d ln p*/d ln f = 1/(2-xf)
    f1, f2 = 1e-3, 2e-3
    e_thr = (math.log(threshold(f2, xf, xv=xv, eta=eta)) - math.log(threshold(f1, xf, xv=xv, eta=eta))) / math.log(2)
    if abs(e_thr - 1 / (2 - xf)) > 1e-4: bad['thr'] += 1
    # q* exponent in p (f=0): (2-xv)/eta
    q1 = qstar(0.3, 1, 1, 1, 0, 0, 1, xv, eta); q2 = qstar(0.6, 1, 1, 1, 0, 0, 1, xv, eta)
    e_q = math.log(q2 / q1) / math.log(2)
    # splitting k parts: total p q* summed, ratio
    k = 7
    mono = 1.0 * qstar(1.0, 1, 1, 1, 0, 0, 1, xv, eta); split = k * (1 / k) * qstar(1 / k, 1, 1, 1, 0, 0, 1, xv, eta)
    if abs(math.log(mono / split) / math.log(k) - (2 - xv) / eta) > 1e-6: bad['split'] += 1
    if abs(e_q - (2 - xv) / eta) > 1e-6: bad['conc'] += 1
    # spending C(q*) exponent in p: xv + (1+eta)(2-xv)/eta
    s1 = 1 * 0.3 ** xv * q1 ** (1 + eta) / (1 + eta); s2 = 1 * 0.6 ** xv * q2 ** (1 + eta) / (1 + eta)
    if abs(math.log(s2 / s1) / math.log(2) - (xv + (1 + eta) * (2 - xv) / eta)) > 1e-6: bad['spend'] += 1
print("   mismatches against stated exponents:", bad)

print("(b) a genuine lump-sum fixed cost F p^xf (paid iff q>0) instead of the linear term f p^xf q:")
for xf, xv, eta in [(0, 0, 1), (1, 1, 1), (0, 0, 2), (0, 1, 0.5)]:
    F1, F2 = 1e-3, 2e-3
    e_l = (math.log(threshold(F2, xf, xv=xv, eta=eta, lump=True)) - math.log(threshold(F1, xf, xv=xv, eta=eta, lump=True))) / math.log(2)
    pred_l = eta / (2 * eta + 2 - xv - eta * xf)
    print(f"   xf={xf}, xv={xv}, eta={eta}: lump-sum threshold exponent {e_l:.4f} (eta/(2eta+2-xv-eta xf) = {pred_l:.4f}); linear-term exponent 1/(2-xf) = {1/(2-xf):.4f}")
# Does a constant lump-sum fixed cost make the requirement level off as gam -> 0 ?
print("   requirement d* (certificate root) as gam falls, A=0.3, cE=1, aB=1, p=0.6, chi=Y=1, eta=1:")
def dstar(gam, f, lump, p=0.6, A=0.3):
    def G(d):
        if lump:
            q = qstar(p, 1, 1, d, 0, 0, gam, 0, 1.0)
            prof = q * p * p / d - gam * q * q / 2 - f
            q = q if prof > 0 else 0.0
        else:
            q = qstar(p, 1, 1, d, f, 0, gam, 0, 1.0)
        return (A + p * q) / d
    lo, hi = 1e-6, 1e9
    for _ in range(200):
        m = math.sqrt(lo * hi)
        if G(m) > 1: lo = m
        else: hi = m
    return hi
for gam in (1.0, 1e-2, 1e-4, 1e-6, 1e-8):
    print(f"     gam={gam:.0e}: linear part f=0.3 -> d*={dstar(gam,0.3,False):.3f};  lump-sum F=0.3 -> d*={dstar(gam,0.3,True):.3f};  f=0 -> d*={dstar(gam,0.0,False):.3f}")

print("(c) quasi-static vs selection with finite speed. Dominant share p=0.6, A=0.3, aB=cE=1, chi=Y=1, eta=1, f=0,")
print("    gam=e^{-0.2t}, d=2 e^{alpha t} (rate law threshold alpha = 0.1). Certificate s_E=(A+p q)/d.")
def simulate(alpha, mode, V=1.0, T=400.0, dt=0.01, xv=0.0, eta=1.0, g=0.2, d0=2.0, A=0.3, p=0.6):
    q = qstar(p, 1, 1, d0, 0, 0, 1.0, xv, eta)   # start at the quasi-static level
    t = 0.0; first = None; smax = 0
    # discrete-type replicator: types on a log grid
    if mode == 'replicator':
        L = [math.exp(-10 + 0.1 * i) for i in range(351)]   # q from e^-10 to e^25
        x = [0.0] * len(L); j0 = min(range(len(L)), key=lambda i: abs(math.log(L[i]) - math.log(q))); x[j0] = 1.0
    while t < T:
        gam = math.exp(-g * t); d = d0 * math.exp(alpha * t)
        if mode == 'qs':
            q = qstar(p, 1, 1, d, 0, 0, gam, xv, eta)
        elif mode == 'additive':
            q = max(0.0, q + dt * V * (p * p / d - gam * p ** xv * q ** eta))
        elif mode == 'log':
            q = q * math.exp(dt * V * q * (p * p / d - gam * p ** xv * q ** eta))
        elif mode == 'replicator':
            fit = [qq * p * p / d - gam * p ** xv * qq ** (1 + eta) / (1 + eta) for qq in L]
            mf = sum(a * b for a, b in zip(x, fit))
            mu = 1e-3
            mx = max(fit)
            xn = [x[i] * math.exp(max(-50.0, dt * V * (fit[i] - mx))) for i in range(len(L))]
            sn = sum(xn); xn = [v / sn for v in xn]
            # mutation to neighbours
            xm = [0.0] * len(L)
            for i in range(len(L)):
                xm[i] += xn[i] * (1 - mu * dt)
                if i > 0: xm[i - 1] += xn[i] * mu * dt / 2
                if i < len(L) - 1: xm[i + 1] += xn[i] * mu * dt / 2
            s = sum(xm); x = [v / s for v in xm]
            q = sum(a * b for a, b in zip(x, L))
        sE = (A + p * q) / d
        smax = max(smax, sE)
        if first is None and sE > 1: first = t
        t += dt
    return first, sE, q

for alpha in (0.09, 0.11, 0.05, 0.0):
    out = []
    for mode, V in (('qs', None), ('additive', 1.0), ('additive', 100.0), ('log', 1.0), ('log', 100.0), ('replicator', 1.0), ('replicator', 20.0)):
        T = 300.0
        fc, sE, q = simulate(alpha, mode, V=V if V else 1.0, T=T, dt=0.02 if mode != 'replicator' else 0.05)
        out.append(f"{mode}{'' if V is None else '(V='+str(V)+')'}: first failure {('%.1f'%fc) if fc is not None else 'none by '+str(int(T))}, s_E(T)={sE:.3g}")
    print(f"   alpha={alpha}: " + " | ".join(out), flush=True)
