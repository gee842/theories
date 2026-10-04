"""m09  Smaller items: delegation (6.4), correction beyond understanding (6.8), saturation (6.11(3)), topology (6.9),
sharing among n or n-1 (10.3(2)), the safeguards' margin on the forgiving host (10.5(1)), R1, talk among three or more (5.15(2)).
Keys: `delegatelock`, `opaque`, `absorb`, `topology`, `share`, `safeguards`, `require`, `talk`.  Standard library only.
"""
import math, random

def check_delegation():
    print("(6.4) delegation when the lock counts. Phi_i = (1 - q_L i_i) Q [w_i + (1-w_i)(1-p)], Q = prod (1-psi_j), r=1, strength 1+s i_i")
    def surv(n, s, p, qL, psi0, psi1, me, k):
        cnt = k + me
        Q = (1 - psi1) ** cnt * (1 - psi0) ** (n - cnt)
        w = (1 + s * me) / (n + s * cnt)
        return (1 - qL * me) * Q * (w + (1 - w) * (1 - p))
    n, s, p, qL, psi0, psi1 = 3, 1.0, 0.1, 0.0, 0.0, 0.015
    ratios = [surv(n, s, p, qL, psi0, psi1, 1, k) / surv(n, s, p, qL, psi0, psi1, 0, k) for k in range(n)]
    eqs = [k for k in range(n + 1) if (k == 0 or ratios[k - 1] >= 1) and (k == n or ratios[k] <= 1)]
    print(f"   Codex p=.1: delegate/not ratios for k=0,1,2 others delegating {[round(x, 7) for x in ratios]} -> equilibrium numbers of delegators {eqs} (neither 0 nor 3)")
    random.seed(2); neither = {1.0: 0, 0.5: 0, 0.1: 0}; T = 20000
    for p in neither:
        for _ in range(T):
            n = random.randint(2, 6); s = random.uniform(0, 20); qL = random.uniform(0, 0.99)
            psi0 = random.uniform(0, 0.05); psi1 = psi0 + random.uniform(0, 0.3)
            allD = surv(n, s, p, qL, psi0, psi1, 1, n - 1) >= surv(n, s, p, qL, psi0, psi1, 0, n - 1)
            noneD = surv(n, s, p, qL, psi0, psi1, 0, 0) >= surv(n, s, p, qL, psi0, psi1, 1, 0)
            neither[p] += (not allD and not noneD)
    print(f"   random draws with q_L<1: 'neither all nor none is an equilibrium' in {neither} of {T} each (p=1 restores 'at least one')")

def check_opaque():
    print("(6.8) correction people cannot understand: residual q0(1-c_b)+q_c")
    q0 = 0.1
    def surv(T, cb, qc, t0):
        S = 1.0
        for t in range(t0, T + t0):
            S *= 1 - (q0 * (1 - cb(t)) + qc(t))
        return S
    fixed = lambda t: 0.99; qc = lambda t: 2.0 ** (-(t + 2))
    print(f"   V6.1's example (c_b = .99 fixed, q_c = 2^-(t+2)): survival to 200 = {surv(200, fixed, qc, 1):.3f} counting from t=1, {surv(200, fixed, qc, 0):.3f} from t=0;"
          f" to 20,000 = {surv(20000, fixed, qc, 1):.2e} (not summable: tends to zero)")
    rising = lambda t: 1 - 2.0 ** (-t)
    print(f"   blocking that tends to complete, c_b,t = 1-2^-t: survival to 200 = {surv(200, rising, qc, 1):.4f}, to 20,000 = {surv(20000, rising, qc, 1):.4f}"
          f" (summable residual; without the corrector: {(1-q0)**200:.1e} at 200)")

def check_absorb():
    print("(6.11(3)) n=3, L_e=L_c=1, psi0=0, s_t=2^t, dpsi_t=2^-t: own marginal gain at full delegation, 2s/(9(1+s)) - dpsi(1-dpsi)^2")
    for t in range(0, 7):
        s = 2.0 ** t; dp = 2.0 ** (-t)
        print(f"   t={t}: {2*s/(9*(1+s)) - dp*(1-dp)**2:+.4f}; realized hazard 1-(1-dpsi)^3 = {1-(1-dp)**3:.4f}")
    tail = sum(1 - (1 - 2.0 ** (-t)) ** 3 for t in range(5, 200))
    print(f"   full delegation is an equilibrium at EVERY t (the gain is positive from t=0; at t=0 the realized hazard is 1); from t=5 the realized risk sums to {tail:.4f} <= 3/16 = {3/16:.4f}")

def check_topology():
    print("(6.9) topology, f=.9, k=6")
    f, k = 0.9, 6
    print(f"   serial {f**k:.3f}; independent across the gap {1-(1-f**k)**k:.3f}; with common cause .05 {(1-(1-f**k)**k)*0.95:.3f}; "
          f"layered m=2 {(1-(1-f)**2)**k:.3f}, m=3 {(1-(1-f)**3)**k:.3f}")

def check_share():
    print("(10.3(2)) sharing a fraction beta of the divisible prize among all n, or among the n-1 losers: uninvadable intensity in one field")
    n, r, c, Oe, Os = 4, 1.0, 1.0, 1.0, 0.5
    for beta in (0.3, 0.6):
        for scheme in ('n', 'n-1'):
            def rel_payoff(y, x):
                w = y ** r / (y ** r + (n - 1) * x ** r)
                if scheme == 'n': own = w * ((1 - beta) * Oe + Os) + beta * Oe / n
                else: own = w * ((1 - beta) * Oe + Os) + (1 - w) * beta * Oe / (n - 1)
                wo = x ** r / (y ** r + (n - 1) * x ** r)
                if scheme == 'n': oth = wo * ((1 - beta) * Oe + Os) + beta * Oe / n
                else: oth = wo * ((1 - beta) * Oe + Os) + (1 - wo) * beta * Oe / (n - 1)
                return (own - c * y) - (oth - c * x)
            # uninvadable x: the mutant's relative-payoff slope at y = x vanishes (bisection on the slope), then a grid check
            def slope(x, h=1e-7): return (rel_payoff(x + h, x) - rel_payoff(x - h, x)) / (2 * h)
            lo, hi = 1e-6, 5.0
            for _ in range(200):
                mid = (lo + hi) / 2
                if slope(mid) > 0: lo = mid
                else: hi = mid
            x = (lo + hi) / 2
            assert max(rel_payoff(x * k / 100, x) for k in range(1, 400)) <= 1e-12
            Oeff = ((1 - beta) * Oe + Os) if scheme == 'n' else ((1 - beta * n / (n - 1)) * Oe + Os)
            print(f"   beta={beta} shared among {scheme:3s}: uninvadable intensity {x:.5f}; r Omega_eff/(n c) = {r*Oeff/(n*c):.5f} with Omega_eff = {Oeff:.4f}")

def check_safeguards():
    print("(10.5(1)) the forgiving (logistic) host: margin Delta needed to stay above the floor through the transient")
    rho, h = 0.05, 0.08
    def vmin(Delta, emin=0.0, emax=1.0, x0=0.99, dt=0.01, T=3000.0):
        de = emax - emin; V = 1.0; lo = 1.0; t = 0.0
        u0 = math.log(x0 / (1 - x0))
        def E(t):
            u = u0 - Delta * de * t
            return emin + de * (1 / (1 + math.exp(-u)) if u > -700 else 0.0)
        while t < T:
            f = lambda tt, VV: VV * (rho * (1 - VV) - h * E(tt))
            k1 = f(t, V); k2 = f(t + dt / 2, V + dt / 2 * k1); k3 = f(t + dt / 2, V + dt / 2 * k2); k4 = f(t + dt, V + dt * k3)
            V += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += dt; lo = min(lo, V)
            if t > 50 and E(t) < 1e-6 and V > lo + 0.3: break
        return lo
    print(f"   V6.1's transient: Delta=.08, 99% race: minimum {vmin(0.08):.4f}")
    for floor in (0.2, 0.3, 0.5):
        lo, hi = 0.0, 2.0
        for _ in range(30):
            mid = (lo + hi) / 2
            if vmin(mid, dt=0.05) < floor: lo = mid
            else: hi = mid
        print(f"   floor {floor}: Delta_min = {hi:.3f}")
    print("   (without the margin the logistic host dips below the floor and recovers: crossing is recoverable here, permanent on a threshold host)")

def check_R1():
    print("(R1) long-run average liability vs cumulative advantage: tau(t) = nu - 1/(2 sqrt(t+1)) has average -> nu yet B(t) = sqrt(t+1)-1 -> infinity")
    nu, rho, h, Vmin = 1.0, 0.05, 0.08, 0.3     # (reach): h*1 > rho*(1-Vmin) = .035
    for name, adv_fn in (("tau = nu (B=0)", lambda t: 0.0), ("tau = nu - 1/(2 sqrt(t+1))", lambda t: 1 / (2 * math.sqrt(t + 1)))):
        u = math.log(1e-3 / (1 - 1e-3)); V = 1.0; t = 0.0; dt = 0.01; cross = None
        while t < 4000:
            u += dt * adv_fn(t)                                    # race carrier (load 1) vs restrained (load 0)
            E = 1 / (1 + math.exp(-u))
            V += dt * V * (rho * (1 - V) - h * E); t += dt
            if cross is None and V < Vmin: cross = t
        print(f"   {name}: race share starts at 0.001; host {'crosses the floor at t = %.0f' % cross if cross else 'stays above the floor'}")
    print("   both have long-run average liability nu: 'average at least nu' (with limsup) is necessary, not sufficient;"
          " the sharp necessary condition is that the cumulative advantage does not tend to infinity")

def check_talk():
    print("(5.15(2)) ideal points of sender and receiver at theta=-1 among n, uniform-quadratic, random linear third-party terms")
    random.seed(4)
    for n in (3, 4, 6, 10):
        b0 = 0.05; u = 0.3; K = random.uniform(-1, 1)
        def JS(y): pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = K * y; return pS - (pR + pk) / (n - 1)
        def JR(y): pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = K * y; return pR - (pS + pk) / (n - 1)
        def argmax(fn):
            lo, hi = -5, 5
            for _ in range(200):
                m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
                if fn(m1) < fn(m2): lo = m1
                else: hi = m2
            return (lo + hi) / 2
        print(f"   n={n}: ideal-point gap {argmax(JS)-argmax(JR):.6f}; b0 n/(n-2) = {b0*n/(n-2):.6f}; informative talk iff gap < 1/4 -> material bias below {(n-2)/(4*n):.4f}")

def check_talk_theta():
    print("(5.15 unified) common theta among n: J_k = pi_k + theta*mean(others); effective bias b0 (n-1-theta)/(n-1+theta)")
    random.seed(9)
    worst = 0.0
    for n in (2, 3, 4, 6):
        for th in (-0.9 if n == 2 else -1.0, -0.5, 0.0, 0.5, 1.5):
            if n == 2 and th <= -1: continue
            b0 = 0.07; u = 0.2; K = random.uniform(-1, 1)
            def J(y, who):
                pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = K * y
                if who == 'S': return pS + th * (pR + (n - 2) * pk) / (n - 1)
                return pR + th * (pS + (n - 2) * pk) / (n - 1)
            def argmax(fn):
                lo, hi = -50, 50
                for _ in range(300):
                    m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
                    if fn(m1) < fn(m2): lo = m1
                    else: hi = m2
                return (lo + hi) / 2
            gap = argmax(lambda y: J(y, 'S')) - argmax(lambda y: J(y, 'R'))
            pred = b0 * (n - 1 - th) / (n - 1 + th)
            worst = max(worst, abs(gap - pred))
            print(f"   n={n} theta={th:+.1f}: ideal-point gap {gap:.6f}; b0(n-1-theta)/(n-1+theta) = {pred:.6f}; informative iff below .25: {pred < 0.25}")
    print(f"   largest deviation {worst:.1e}  (n=2: b0(1-theta)/(1+theta), infinite at theta=-1: Prop 5.15(1); theta=-1, n>=3: b0 n/(n-2): Prop 5.15(2))")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    for f in (check_delegation, check_opaque, check_absorb, check_topology, check_share, check_safeguards, check_R1, check_talk, check_talk_theta):
        f(); print()
