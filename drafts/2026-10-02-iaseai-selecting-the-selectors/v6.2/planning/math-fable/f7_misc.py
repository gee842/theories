"""f7: smaller items.  Standard library only.
(A) Proposition 6.4 (delegatelock): with p<1 an interior profile can be the only pure equilibrium (Codex); with p=1 at least one corner is.
(B) Proposition 6.8: the printed example (c_b=.99 fixed, q0=.1) is NOT summable; a summable example; the 0.63 vs 0.473 start index.
(C) Proposition 6.11(3): full delegation is an equilibrium at every t; realized risk from t=5 is at most 3/16.
(D) Theorem 10.5(1): the transient minimum on the logistic host and the liability margin Delta_min for floors .2, .3, .5.
(E) Proposition 10.3(2): sharing divided among all n vs among the n-1 others: effective prize (1-beta rho)Om_e vs (1-beta rho n/(n-1))Om_e,
    by the numerical symmetric equilibrium of the contest.
(F) Theorem 4.12: (b),(c) do not imply (e): a case with capture completed but after the host has passed the alarm band.
(G) Proposition 6.9: a full row sum below one is sufficient, not necessary, and does not certify independent errors.
"""
import math

def part_A():
    print("(A) delegatelock: n=3, s=1, q_L=0, psi0=0, psi1=.015")
    n, s, qL, psi0, psi1 = 3, 1.0, 0.0, 0.0, 0.015
    def surv(delegate, k, p):
        cnt = k + int(delegate); Q = (1 - psi1) ** cnt * (1 - psi0) ** (n - cnt)
        w = (1 + s * int(delegate)) / (n + s * cnt)
        return (1 - qL * int(delegate)) * Q * (w + (1 - w) * (1 - p))
    for p in (0.1, 1.0):
        ratios = [surv(True, k, p) / surv(False, k, p) for k in range(n)]
        eq = []
        for k in range(n + 1):  # k delegators total
            ok = True
            if k > 0 and surv(True, k - 1, p) < surv(False, k - 1, p): ok = False   # a delegator prefers not to
            if k < n and surv(False, k, p) < surv(True, k, p): ok = False           # a non-delegator prefers to
            if ok: eq.append(k)
        print(f"   p={p}: Phi_D/Phi_N for k=0,1,2 others delegating: {[round(x,6) for x in ratios]}; pure equilibria (number of delegators): {eq}")
    print("   -> with p<1 the ratio falls with k (substitutes): the only equilibrium has two delegators; with p=1 it rises (complements): corners")

def part_B():
    print("(B) Proposition 6.8")
    q0 = 0.1
    def surv(resid, T):
        s = 1.0
        for t in range(T): s *= (1 - resid(t))
        return s
    r1 = lambda t: q0 * (1 - 0.99) + 2.0 ** (-(t + 2))
    print(f"   printed example (c_b=.99 fixed, q_c=2^-(t+2)): residual -> {q0*0.01:.3f} per period, not summable; survival to 200: {surv(r1,200):.3f}, to 20000: {surv(r1,20000):.2e}")
    r2 = lambda t: q0 * 2.0 ** (-(t + 1)) + 2.0 ** (-(t + 2))
    print(f"   summable example (c_b,t = 1 - 2^-(t+1), q_c = 2^-(t+2)): survival to 200: {surv(r2,200):.4f}, to 20000: {surv(r2,20000):.4f} (bounded away from zero)")
    s_from1 = 1.0
    for t in range(1, 201): s_from1 *= (1 - (q0 * 0.01 + 2.0 ** (-(t + 2))))
    print(f"   the quoted 0.63 needs the sum to start at t=1: from t=1 {s_from1:.3f}; from t=0 {surv(r1,200):.3f}")

def part_C():
    print("(C) Proposition 6.11(3): n=3, L_e=L_c=1, psi0=0, s_t=2^t, Delta psi_t=2^-t")
    n = 3
    for t in range(0, 8):
        s = 2.0 ** t; dp = 2.0 ** (-t)
        # objective of actor i at symmetric iota: -L_e(1-w_i) - L_c[1 - prod(1-psi_j)], psi = dp*iota; check iota=1 is a best response on a grid
        def obj(iota, others=1.0):
            w = (1 + s * iota) / (1 + s * iota + 2 * (1 + s * others))
            Q = (1 - dp * iota) * (1 - dp * others) ** 2
            return -(1 - w) - (1 - Q)
        best = max(obj(k / 200) for k in range(201)); at1 = obj(1.0)
        print(f"   t={t}: objective at iota=1 {at1:.4f}, best on grid {best:.4f} -> full delegation {'is' if at1 >= best - 1e-12 else 'is NOT'} a best response; realized hazard n*Delta psi = {n*dp:.4f}")
    print(f"   realized risk summed from t=5: {sum(3*2.0**(-t) for t in range(5,60)):.4f} = 3/16; from t=0 it is {sum(3*2.0**(-t) for t in range(0,60)):.1f} (the t=0 hazard alone is 1)")

def part_D():
    print("(D) Theorem 10.5(1): logistic host rho=.05, h_V=.08, race share x0=.99 declining by replicator at rate Delta*(e_max-e_min), V0=1 (HO's model: e_min=0, e_max=1)")
    rho, h = 0.05, 0.08
    def run(Delta, emin=0.0, emax=1.0, T=1500.0, dt=0.02):
        de = emax - emin; x0 = 0.99
        def xt(t):
            u = math.log(x0 / (1 - x0)) - Delta * de * t
            return 1 / (1 + math.exp(-u)) if u >= 0 else math.exp(u) / (1 + math.exp(u))
        def f(t, V): return V * (rho * (1 - V) - h * (emin + de * xt(t)))
        V = 1.0; t = 0.0; vmin = V
        for _ in range(int(T / dt)):
            k1 = f(t, V); k2 = f(t + dt / 2, V + dt / 2 * k1); k3 = f(t + dt / 2, V + dt / 2 * k2); k4 = f(t + dt, V + dt * k3)
            V += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += dt; vmin = min(vmin, V)
        return vmin, V
    for emin in (0.0, 0.1):
        vmin, Vend = run(0.08, emin=emin)
        print(f"   e_min={emin}: Delta=.08 -> transient minimum {vmin:.4f} (text 0.14 for e_min=0), long-run level {Vend:.3f} = 1 - h e_min/rho")
        for floor in (0.2, 0.3, 0.5):
            lo, hi = 0.0, 2.0
            for _ in range(30):
                m = (lo + hi) / 2
                if run(m, emin=emin)[0] < floor: lo = m
                else: hi = m
            print(f"      floor {floor}: Delta_min = {hi:.3f} (viable iff Delta >= Delta_min; below it the logistic host dips under the floor and recovers)")
    print("   -> the viability clause of 10.5(1) is a margin condition on every host; on the logistic host the shortfall is recoverable, on a threshold host permanent")

def part_E():
    print("(E) Proposition 10.3(2): sharing divided among all n vs the n-1 others; numerical symmetric equilibrium (n=4, r=1, c=1, Om_e=1, Om_s=0, rho=1)")
    n, r, c = 4, 1.0, 1.0
    def eq_intensity(payoff):
        e = 0.2
        for _ in range(300):
            # best response by golden section
            g = (math.sqrt(5) - 1) / 2; lo, hi = 1e-7, 1.5
            f = lambda x: payoff(x, e)
            x1 = hi - g * (hi - lo); x2 = lo + g * (hi - lo); f1 = f(x1); f2 = f(x2)
            for _ in range(120):
                if f1 < f2: lo = x1; x1 = x2; f1 = f2; x2 = lo + g * (hi - lo); f2 = f(x2)
                else: hi = x2; x2 = x1; f2 = f1; x1 = hi - g * (hi - lo); f1 = f(x1)
            br = (lo + hi) / 2; en = 0.5 * e + 0.5 * br
            if abs(en - e) < 1e-13: e = en; break
            e = en
        return e
    for beta in (0.3, 0.6):
        def pay_all(x, e):   # winner gives beta Om_e to be divided among all n
            w = x ** r / (x ** r + (n - 1) * e ** r)
            return w * (1 - beta) + beta / n - c * x
        def pay_others(x, e):  # winner gives beta Om_e divided among the n-1 others
            w = x ** r / (x ** r + (n - 1) * e ** r)
            return w * (1 - beta) + (1 - w) * beta / (n - 1) - c * x
        ea = eq_intensity(pay_all); eo = eq_intensity(pay_others)
        fa = r * (1 - beta) * (n - 1) / (n * n * c); fo = r * (1 - beta * n / (n - 1)) * (n - 1) / (n * n * c)
        print(f"   beta={beta}: Nash intensity, shared among all n: {ea:.5f} vs r Om_eff (n-1)/(n^2 c) with Om_eff=(1-beta)Om_e: {fa:.5f}; among the n-1 others: {eo:.5f} vs Om_eff=(1-beta n/(n-1))Om_e: {fo:.5f}")

def part_F():
    print("(F) Theorem 4.12: (b),(c) hold (certificate fails, x_ev -> 1) yet (e) fails: capture arrives after the host passes the alarm band")
    rho, h, Vmin, Val, m_in, m_out = 0.05, 0.08, 0.3, 0.6, 0.5, 0.0
    m_fl = (Val - Vmin) / (1 - Vmin); thr = (m_fl - m_out) / (m_in - m_out)
    for mid in (0.0, 20.0, 45.0):
        V = 1.0; x = 0.0; t = 0.0; dt = 0.01; alarm = None; cross = None
        while t < 200 and cross is None:
            x = 1 / (1 + math.exp(-(t - mid) / 2))       # logistic capture of evaluation, midpoint 'mid'
            m = x * m_in + (1 - x) * m_out; Vt = V + m * (1 - V)
            if alarm is None and Vt <= Val: alarm = t
            if V < Vmin: cross = t
            V += dt * V * (rho * (1 - V) - h * 1.0); t += dt
        print(f"   capture midpoint {mid}: x_ev crosses threshold {thr:.3f} at t={mid+2*math.log(thr/(1-thr)):.1f}; alarm at {alarm if alarm is None else round(alarm,1)}; floor crossed at {round(cross,1) if cross else None} -> "
              f"{'silent crossing (e holds)' if (alarm is None or alarm > cross) else 'alarm before the floor (e fails although x_ev -> 1)'}")

def part_G():
    print("(G) Proposition 6.9: six checks f=.9, common blind spot rho_cc: catch rate (1-rho_cc)(1-.1^6):",
          ", ".join(f"rho_cc={r}: {(1-r)*(1-0.1**6):.3f}" for r in (0, .05, .3)), "-> row sums (capture) and error correlation are separate quantities")

if __name__ == "__main__":
    part_A(); part_B(); part_C(); part_D(); part_E(); part_F(); part_G()
