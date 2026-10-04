"""JX  Joint scissors and the detect link (proposed block for checks_v62.py; keys `scissors`, `detectlink`,
`jointscissors`, `enforce`, `zonesillus`).  Pure Python, standard library only.  Run: python3 jx_joint_scissors.py
Written by the U05 drafter (A) for V6.2; nothing here is taken from the text it checks.

(A) detectlink [identity]: with p_d = 1 - upsilon(T_dec), condition (14) reads upsilon >= 1 - pbar_d; reading
    Proposition 8.10's payoffs as continuation values (R = C; T = a deviation that becomes decisive,
    (1-delta)(C+g) + delta D; P - F = a deviation detected and answered, (1-delta)(C+g) + delta v), its verification
    threshold (T-R)/(T-P+F) equals 1 - pbar_d.
(B) detectlink [independent]: a Poisson detection-and-response clock of mean tau gives p_d = exp(-T_dec/tau); Monte
    Carlo of the clock against the formula, and the discounted value of deviating from simulated outcomes against (14).
(C) the reduced joint model [num, one model; rivals do not respond strategically]:
    capacity loop (1) with one ratio channel (Proposition 2.3); won share omega = kappa*Omega/(kappa*Omega + n k0);
    structural gain Gamma (2) and discounted gain Gamma_delta (2.2(3)); time to decisiveness T_dec from the NONLINEAR
    stock dynamics (stakes and provision held at their current values while a lead opens), the linearized
    ln(gapbar/gap0)/ln Lambda* printed beside it; p_d = exp(-T_dec/tau); working objective theta_Gamma(theta_0,
    Gamma_delta) of (9), and -1 at Gamma_delta >= 1 (the limit from below); the stage game of Remark S5.1 with b, c,
    d all proportional to the stakes, so that every payoff, the decisive value included, scales with Omega and
    pbar_d is unchanged by scale (the stakes arm is off); pbar_d from (14).
    Decisive value: D = C (the boundary case of Remark S5.1) or D - C = 0.5 in objective units per unit of stakes.
    Punishment: (i) reversion to the race with no breakouts during punishment (as in the printed reduced form); (ii) one
    breakout technology throughout: during the punishment race each racer breaks out with the deviator's p_d
    (independent breakouts; a simultaneous breakout leaves the race as it was), being subordinated worth the race.
(D) paths: stakes outgrowing fixed provision; provision growing with the stakes (control); provision outgrowing stakes.
(E) robustness grid: the won share omega* at which restraint stops being enforceable, joint against each arm alone.
"""
import math, random

# ---------------------------------------------------------------- stage game of Remark S5.1, per unit of stakes
N = 4; B_ = 1.0; C_ = 0.3; DH = 0.2; EPS = 1.0; DELTA = 0.9
A_ = EPS * (B_ - DH) - C_          # material gain from racing alone
BB = EPS * (B_ / (N - 1) + DH)     # average loss each other actor suffers from one actor's racing
KK = C_ + N * EPS * DH             # each actor's loss when all race, against all restraining

def gain_obj(th):  return A_ - th * BB          # one-period deviation gain g, objective units (C = 0)
def race_obj(th):  return -KK * (1 + th)        # per-period value P of the race (stage equilibrium), objective units

def theta_gamma(th0, Gd, n=N):
    if Gd >= 1: return -1.0
    return (n * th0 - (n - 1) * (1 + th0) * Gd) / (n - (1 + th0) * Gd)

def punish_value(th, qb, DC, delta=DELTA, n=N):
    """(1-delta) x value of reversion to the race among n racers; a racer that breaks out gets D = C + DC = DC
    (C = 0), the others are subordinated at the race's value P; independent breakouts, so each racer's exclusive
    breakout has probability qb (1-qb)^(n-1) per period."""
    P = race_obj(th); D = DC; Vsub = P
    qe = qb * (1 - qb) ** (n - 1)
    return ((1 - delta) * P + delta * qe * (D + (n - 1) * Vsub)) / (1 - delta + n * delta * qe)

def holds14(th, pd, qb, DC, delta=DELTA):
    """(14): (1-delta) g + delta pd (D - C) <= delta (1-pd)(C - v), with C = 0, D = DC."""
    v = punish_value(th, qb, DC, delta)
    return (1 - delta) * gain_obj(th) + delta * pd * DC <= delta * (1 - pd) * (0.0 - v) + 1e-12

def pbar(th, DC, delta=DELTA):
    """pbar_d with no breakouts during punishment; -inf where no sanction remains."""
    v = punish_value(th, 0.0, DC, delta); D = DC
    if D - v <= 1e-12: return -math.inf
    return 1 - ((1 - delta) * gain_obj(th) + delta * (D - 0.0)) / (delta * (D - v))

# ---------------------------------------------------------------- capacity loop, one ratio channel
def gains(omega, r, dK, df, beta=0.0, delta=DELTA):
    G = (1 - beta) * r * omega * dK / (dK + df)
    Gd = (1 - beta) * r * omega * delta * dK / (1 - delta * (1 - dK - df))
    return G, Gd

def tdec_linear(G, dK, df, gap0, gapbar):
    lam = 1 + (dK + df) * (G - 1)
    return math.log(gapbar / gap0) / math.log(lam) if lam > 1 else math.inf

def tdec_nonlinear(omega, r, dK, df, gap0, gapbar, beta=0.0, n=N, tmax=5000):
    """Simulate (1) with kappa*Omega = 1, k0 set by omega; the leader starts gap0 above the others' common stock;
    T_dec = first period at which K_1/K_other - 1 >= gapbar (inf if never)."""
    kO = 1.0
    k0 = kO * (1 - omega) / (n * omega)
    Kst = (kO / n + k0) / dK
    K = [Kst * (1 + gap0)] + [Kst] * (n - 1)
    for t in range(1, tmax + 1):
        w = [k ** r for k in K]; s = sum(w); mean = sum(K) / n
        K = [(1 - dK) * K[i] + kO * ((1 - beta) * w[i] / s + beta / n) + k0 - df * (K[i] - mean) for i in range(n)]
        if K[0] / K[1] - 1 >= gapbar:
            return float(t)
    return math.inf

def state(omega, P):
    G, Gd = gains(omega, P['r'], P['dK'], P['df'])
    th = theta_gamma(P['th0'], Gd)
    Tn = tdec_nonlinear(omega, P['r'], P['dK'], P['df'], P['gap0'], P['gapbar'])
    Tl = tdec_linear(G, P['dK'], P['df'], P['gap0'], P['gapbar'])
    pd = math.exp(-Tn / P['tau']) if Tn < math.inf else 0.0
    return G, Gd, th, Tn, Tl, pd

def enforceable(omega, P, arm='joint', variant='i'):
    G, Gd, th, Tn, Tl, pd = state(omega, P)
    if arm == 'objective': pd = 0.0                 # breakout blade held still
    if arm == 'breakout':  th = P['th0']            # objective blade held still
    qb = pd if variant == 'ii' else 0.0
    return holds14(th, pd, qb, P['DC'])

def omega_star(P, arm='joint', variant='i', lo=0.01, hi=0.999):
    """largest won share at which restraint is enforceable (bisection; enforceability falls with omega here)."""
    if not enforceable(lo, P, arm, variant): return lo
    if enforceable(hi, P, arm, variant): return None
    for _ in range(50):
        mid = (lo + hi) / 2
        if enforceable(mid, P, arm, variant): lo = mid
        else: hi = mid
    return lo

BASE = dict(r=3.0, dK=0.2, df=0.05, th0=0.0, tau=10.0, gap0=0.05, gapbar=0.5, DC=0.0)
fmt = lambda z: 'never' if z is None else f'{z:.3f}'

def check_A():
    print("(A) detectlink identity: 1 - pbar_d against Proposition 8.10's (T-R)/(T-P+F) under the continuation reading")
    random.seed(11); worst = 0.0; cnt = 0
    for _ in range(100000):
        dl = random.uniform(0.3, 0.99); C = random.uniform(-2, 3); v = C - random.uniform(0.01, 3)
        D = v + random.uniform(0.01, 6); g = random.uniform(-1, 4)
        one_minus_pbar = ((1 - dl) * g + dl * (D - C)) / (dl * (D - v))
        R = C; T = (1 - dl) * (C + g) + dl * D; PF = (1 - dl) * (C + g) + dl * v
        thr = (T - R) / (T - PF)
        worst = max(worst, abs(one_minus_pbar - thr)); cnt += 1
    print(f"   {cnt} random settings with D > v: largest |difference| = {worst:.2e}  (the two thresholds are one number)")
    print("   they differ in what is held fixed: (14) is the equilibrium-path condition (the other restrains, trust 1) and")
    print("   computes v in the same game; 8.10's one-shot game adds trust below 1 and takes the answered value P - F as given")

def check_B():
    print("(B) detectlink, independent: a Poisson detection clock of mean tau gives p_d = exp(-T_dec/tau)")
    random.seed(7)
    for Tdec, tau in ((8.0, 10.0), (20.0, 10.0), (5.0, 2.0)):
        M = 200000; hit = sum(1 for _ in range(M) if random.expovariate(1 / tau) > Tdec)
        print(f"   T_dec={Tdec:4.1f}, tau={tau:4.1f}: simulated p_d {hit / M:.4f}; exp(-T_dec/tau) {math.exp(-Tdec / tau):.4f}")
    C, D, v, g, dl = 1.0, 1.5, 0.0, 0.3, 0.9
    for Tdec, tau in ((8.0, 10.0), (2.0, 10.0)):
        M = 200000; tot = 0.0
        for _ in range(M):
            dec = random.expovariate(1 / tau) > Tdec
            tot += (1 - dl) * (C + g) + dl * (D if dec else v)
        Vdev = tot / M; pd = math.exp(-Tdec / tau)
        lhs = (1 - dl) * g + dl * pd * (D - C); rhs = dl * (1 - pd) * (C - v)
        print(f"   C=1, D=1.5, v=0, g=.3, T_dec={Tdec:4.1f}, tau=10: simulated value of deviating {Vdev:.4f} vs restraint {C:.4f}"
              f" -> deterred {Vdev <= C}; (14) says {lhs <= rhs}")

def table(P, oms):
    print("    omega   Gamma  Gamma_d  theta   T_dec(nonlin)  T_dec(lin)   p_d    pbar_d(i)  enforceable (i)  (ii)")
    for om in oms:
        G, Gd, th, Tn, Tl, pd = state(om, P)
        pb = pbar(th, P['DC'])
        e1 = holds14(th, pd, 0.0, P['DC']); e2 = holds14(th, pd, pd, P['DC'])
        pbs = f"{pb:+7.3f}" if pb > -50 else "  -inf "
        print(f"    {om:5.2f}  {G:6.3f}  {Gd:6.3f}  {th:+6.3f}   {Tn:10.1f}   {Tl:10.1f}   {pd:6.3f}   {pbs}     {str(e1):5}            {str(e2):5}")

def summary(P, label):
    w1 = omega_star(P, 'joint', 'i'); w2 = omega_star(P, 'joint', 'ii')
    wo = omega_star(P, 'objective', 'i'); wb = omega_star(P, 'breakout', 'i')
    print(f"   {label}: restraint enforceable iff omega < omega*: joint (i) {fmt(w1)}; joint (ii) one breakout technology {fmt(w2)};"
          f" objective blade alone {fmt(wo)}; breakout blade alone {fmt(wb)}")
    if w1 is not None:
        G, Gd = gains(w1, P['r'], P['dK'], P['df'])
        print(f"      at the joint crossing (i): Gamma = {G:.3f}, Gamma_delta = {Gd:.3f}, p_d = {state(w1, P)[5]:.3f}")
    return w1, w2, wo, wb

def check_C():
    print("(C) the reduced joint model; base parameters:", ', '.join(f'{k}={v}' for k, v in BASE.items()))
    print("   (C1) boundary case D = C:")
    table(BASE, (0.2, 0.3, 0.4, 0.42, 0.45, 0.5, 0.55, 0.6, 0.7, 0.9))
    r1 = summary(BASE, 'D = C')
    P2 = dict(BASE, DC=0.5)
    print("   (C2) a decisive position worth more than cooperation, D - C = 0.5 per unit of stakes:")
    table(P2, (0.2, 0.3, 0.4, 0.42, 0.45, 0.5, 0.55, 0.6))
    r2 = summary(P2, 'D - C = 0.5')
    return r1, r2

def check_D(w1):
    P = BASE
    print("(D) paths (D = C): x = kappa*Omega/(n k0) = omega/(1-omega) grows at g_Omega - g_k")
    x0 = 0.25; gO = 0.05
    for gk, xs, label in ((0.0, x0, 'stakes outgrow fixed provision'), (0.05, x0, 'provision grows with the stakes'),
                          (0.08, 1.5, 'provision outgrows the stakes')):
        rows = []
        for t in (0, 10, 20, 30, 40, 60):
            x = xs * math.exp((gO - gk) * t); om = x / (1 + x)
            G, Gd, th, Tn, Tl, pd = state(om, P); pb = pbar(th, P['DC'])
            pbs = f"{pb:+.3f}" if pb > -50 else "-inf"
            rows.append(f"t={t}: omega {om:.2f}, p_d {pd:.3f}, pbar {pbs}")
        print(f"   {label} (g_Omega={gO}, g_k={gk}):"); print("      " + "; ".join(rows))
    x_star = w1 / (1 - w1); tstar = math.log(x_star / x0) / gO
    print(f"   with fixed provision from omega=0.20 at g_Omega=0.05 the blades cross at t* = ln(x*/x0)/(g_Omega-g_k) = {tstar:.1f};"
          " with g_k = g_Omega never")

def check_E():
    print("(E) robustness: omega* (variant (i)) joint against each blade alone, over tau, diffusion, theta_0, r, D - C")
    n = 0; below = 0; strict = 0; brk_alone = 0; rows = []
    for DC in (0.0, 0.5):
        for tau in (5.0, 10.0, 20.0, 40.0):
            for df in (0.0, 0.05, 0.1):
                for th0 in (0.0, 0.4):
                    for r in (2.0, 3.0):
                        P = dict(BASE, tau=tau, df=df, th0=th0, r=r, DC=DC)
                        w = omega_star(P, 'joint', 'i'); wo = omega_star(P, 'objective', 'i'); wb = omega_star(P, 'breakout', 'i')
                        alone = [z for z in (wo, wb) if z is not None]
                        m = min(alone) if alone else None
                        n += 1
                        if w is not None and (m is None or w <= m + 1e-9): below += 1
                        if w is not None and m is not None and w < m - 1e-3: strict += 1
                        if wb is not None: brk_alone += 1
                        rows.append((DC, tau, df, th0, r, w, wo, wb))
    for row in rows[::12]:
        DC, tau, df, th0, r, w, wo, wb = row
        print(f"   D-C={DC:.1f} tau={tau:4.1f} df={df:.2f} theta0={th0:.1f} r={r:.0f}: omega* joint {fmt(w)}, objective alone {fmt(wo)}, breakout alone {fmt(wb)}")
    print(f"   {n} settings: the joint threshold lies at or below each blade's own in {below}; strictly below (by > 0.001) in {strict};"
          f" the breakout blade alone closes in {brk_alone}")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A(); print(); check_B(); print(); (r1, r2) = check_C(); print(); check_D(r1[0]); print(); check_E()
