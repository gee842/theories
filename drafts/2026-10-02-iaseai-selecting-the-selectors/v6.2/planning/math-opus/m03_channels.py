"""m03  What moves the loop gain, channel by channel (Prop 2.2 key `loopgain`; Remark S2.1; the shared-parameter table).

Claims under test (memo items 3, 4, 5):
  (A) Correction/depreciation of stock j (raising d_j, everything else fixed) changes Gamma with the sign of
         delta_f/(d+delta_f) - eps_r,      eps_r = dln r_j / dln X_j  (elasticity of decisiveness in the stock's level).
      Ratio channels (sigma = r ln X): eps_r = 0, so faster depreciation leaves Gamma unchanged without diffusion and
      raises it with diffusion.  Level channels (sigma = a X, rule support in the field model): eps_r = 1, it lowers Gamma.
      Gamma_delta: rises with d iff eps_r < (1-delta+delta df)/(1-delta+delta d+delta df) (always, for ratio channels).
  (B) Provision not won (k0) lowers Gamma through stock j iff eps_r < 1; no effect for a linear level channel.
  (C) Remark S2.1: a relative gap grows by 1 + (d+df)(Gamma-1) per period (single channel); with several channels by
      the Perron root of (S1), which Gamma does not determine: same Gamma, different speeds.
  (D) A countervailing channel cannot be subtracted from Gamma: with a delayed negative channel the net DC gain can be
      below one while deviations grow in oscillation.
All by direct simulation of the nonlinear stock model or numerical spectral radius, never by the formula under test.
Standard library only.
"""
import math, random

def relmode_multiplier(n, chans, beta=0.0, Om=1.0, T=400, eps=1e-7):
    """Estimate the growth factor of a relative deviation by simulating the nonlinear stock model (1) with
    strength sigma_i = sum_j h_j(X_i^j); chans: list of dicts with h, kap, d, df, k0.  Returns the asymptotic
    per-period factor of the deviation (power iteration on the nonlinear map, renormalized)."""
    m = len(chans)
    Xs = []
    for c in chans:  # steady state at equal standing
        Xs.append((c['kap'] * Om / n + c['k0']) / c['d'])
    # perturbation: carrier 0 up, others down
    X = [[Xs[j] * (1 + (eps if i == 0 else -eps / (n - 1))) for j in range(m)] for i in range(n)]
    fac = 1.0
    for t in range(T):
        sig = [sum(chans[j]['h'](X[i][j]) for j in range(m)) for i in range(n)]
        mx = max(sig); w = [math.exp(s - mx) for s in sig]; W = sum(w); p = [x / W for x in w]
        Xn = []
        for i in range(n):
            row = []
            for j, c in enumerate(chans):
                mean = sum(X[k][j] for k in range(n)) / n
                row.append((1 - c['d']) * X[i][j] + c['kap'] * Om * ((1 - beta) * p[i] + beta / n) + c['k0'] - c['df'] * (X[i][j] - mean))
            Xn.append(row)
        # deviation norm relative to the steady state
        dev = math.sqrt(sum((Xn[i][j] - Xs[j]) ** 2 / Xs[j] ** 2 for i in range(n) for j in range(m)))
        dev0 = math.sqrt(sum((X[i][j] - Xs[j]) ** 2 / Xs[j] ** 2 for i in range(n) for j in range(m)))
        fac = dev / dev0
        # renormalize to keep the deviation small
        X = [[Xs[j] + (Xn[i][j] - Xs[j]) * eps / dev for j in range(m)] for i in range(n)]
    return fac

def gamma_formula(n, chans, beta=0.0, Om=1.0, h=1e-6):
    G = 0.0
    for c in chans:
        X = (c['kap'] * Om / n + c['k0']) / c['d']
        r = (c['h'](X * (1 + h)) - c['h'](X * (1 - h))) / (2 * h)      # dh/dln X
        w = c['kap'] * Om / (c['kap'] * Om + n * c['k0'])
        G += (1 - beta) * r * w * c['d'] / (c['d'] + c['df'])
    return G

def check_A_B():
    print("(A) sign of dGamma/dd and of d(growth factor)/dd by channel form; (B) sign of dGamma/dk0")
    forms = {
        'ratio  r ln X (eps_r=0)': (lambda X: 1.8 * math.log(X), 0.0),
        'level  a X    (eps_r=1)': (lambda X: 0.9 * X, 1.0),
        'power  a X^.5 (eps_r=.5)': (lambda X: 1.5 * X ** 0.5, 0.5),
        'power  a X^2  (eps_r=2)': (lambda X: 0.4 * X ** 2, 2.0),
        'saturating ln(1+X)': (lambda X: 2.5 * math.log(1 + X), None),
    }
    for name, (h, er) in forms.items():
        for df in (0.0, 0.1):
            base = dict(h=h, kap=0.5, d=0.2, df=df, k0=0.1)
            def G_at(**kw):
                c = dict(base); c.update(kw); return gamma_formula(2, [c]), relmode_multiplier(2, [c])
            g1, m1 = G_at(d=0.2); g2, m2 = G_at(d=0.3); g3, m3 = G_at(k0=0.2)
            # the growth factor m = 1+(d+df)(Gamma-1): compare signs of Gamma change via the simulated m
            gam_sim = lambda m, d: (m - 1) / (d + df) + 1
            Gs1, Gs2, Gs3 = gam_sim(m1, 0.2), gam_sim(m2, 0.3), gam_sim(m3, 0.2)
            X = (0.5 / 2 + 0.1) / 0.2
            if er is None:
                hh = 1e-4
                r_of = lambda X: (h(X * (1 + hh)) - h(X * (1 - hh))) / (2 * hh)
                er = (math.log(r_of(X * 1.001)) - math.log(r_of(X / 1.001))) / (2 * math.log(1.001))
            pred_d = df / (0.2 + df) - er
            print(f"   {name:26s} df={df}: Gamma sim {Gs1:.4f} -> {Gs2:.4f} when d .2->.3 (formula {g1:.4f}->{g2:.4f}); "
                  f"rule sign(df/(d+df)-eps_r)={'+' if pred_d>1e-12 else ('0' if abs(pred_d)<1e-12 else '-')} (eps_r={er:.2f}) | "
                  f"k0 .1->.2: Gamma sim {Gs1:.4f} -> {Gs3:.4f}; rule sign(eps_r-1)={'+' if er>1+1e-9 else ('0' if abs(er-1)<1e-9 else '-')} (lowers iff -)")
    # discounted gain for the ratio channel without diffusion: rises with d
    print("   Gamma_delta, ratio channel, no diffusion, delta=0.9: ", end='')
    for d in (0.1, 0.2, 0.4):
        print(f"d={d}: {1.8*1.0*0.9*d/(1-0.9*(1-d)):.4f}  ", end='')
    print("(rises with d although Gamma=1.8*omega is unchanged)")

def check_C():
    print("(C) Remark S2.1: growth factor of a relative gap, simulated vs 1+(d+df)(Gamma-1); and time 1% -> 50%")
    for (r, d, df) in ((3.0, 0.2, 0.0), (3.0, 0.05, 0.05), (2.0, 0.2, 0.1), (1.5, 0.1, 0.02)):
        c = dict(h=lambda X, r=r: r * math.log(X), kap=0.5, d=d, df=df, k0=0.0)
        G = gamma_formula(2, [c]); m = relmode_multiplier(2, [c])
        old = 1 + d * (G - 1); new = 1 + (d + df) * (G - 1)
        # time from 1% to 50% share gap, by direct simulation of shares
        X = [1.0 + 0.0, 1.0]; Xs = (0.5 / 2) / d
        X = [Xs * 1.01, Xs * 0.99]; t = 0
        while True:
            w = [x ** r for x in X]; p = [x / sum(w) for x in w]; mean = sum(X) / 2
            X = [(1 - d) * x + 0.5 * pi - df * (x - mean) for x, pi in zip(X, p)]; t += 1
            if (X[0] - X[1]) / sum(X) >= 0.5 or t > 10000: break
        print(f"   r={r} d={d} df={df}: Gamma={G:.3f}; simulated factor {m:.5f}; 1+(d+df)(Gamma-1)={new:.5f}; V6.1's 1+d(Gamma-1)={old:.5f}; "
              f"1%->50% gap in {t} periods (linear estimate {math.log(50)/math.log(new):.1f})")
    print("   same Gamma=1.2, different turnover (Sys I1): ", end='')
    for (d, df) in ((0.4, 0.1), (0.015, 0.005)):
        r = 1.2 * (d + df) / d
        c = dict(h=lambda X, r=r: r * math.log(X), kap=0.5, d=d, df=df, k0=0.0)
        m = relmode_multiplier(2, [c], T=2000)
        print(f"d+df={d+df}: factor {m:.5f}, periods to grow 50x {math.log(50)/math.log(m):.0f};  ", end='')
    print()
    # two channels: the growth factor is the Perron root of (S1), not a function of Gamma
    print("   two channels with the same Gamma but different turnover split:")
    for (d1, d2) in ((0.3, 0.02), (0.1, 0.1)):
        chans = [dict(h=lambda X: 0.6 * math.log(X), kap=0.5, d=d1, df=0.0, k0=0.0), dict(h=lambda X: 0.6 * math.log(X), kap=0.5, d=d2, df=0.0, k0=0.0)]
        G = gamma_formula(2, chans); m = relmode_multiplier(2, chans, T=3000)
        # root of (S1): 1 = sum a_j/(lam - (1-d_j)),  a_j = (1-beta) r_j omega_j d_j
        a = [0.6 * d1, 0.6 * d2]; D = [1 - d1, 1 - d2]
        lo, hi = max(D) + 1e-12, 3.0
        for _ in range(200):
            mid = (lo + hi) / 2
            if sum(aj / (mid - Dj) for aj, Dj in zip(a, D)) > 1: lo = mid
            else: hi = mid
        print(f"      d=({d1},{d2}): Gamma={G:.3f}; simulated factor {m:.5f}; Perron root of (S1) {lo:.5f}")

def check_D():
    print("(D) a delayed countervailing channel: net DC gain below one, yet growing oscillation (eigenvalues of J = D + a-vector)")
    # deviation dynamics y' = D y + 1 (sum_j a_j y_j)-type rank one: J = diag(D) + u v^T with u_j v_j = a_j, here u = 1
    D = [0.6, 0.95]; a = [0.5, -0.05]
    J = [[D[0] + a[0], a[1]], [a[0], D[1] + a[1]]]     # rows: stock j receives u_j * (v . y); u=(1,1), v=a
    dc = sum(aj / (1 - Dj) for aj, Dj in zip(a, D))
    tr = J[0][0] + J[1][1]; det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
    disc = tr * tr - 4 * det
    mod = math.sqrt(det) if disc < 0 else max(abs((tr + math.sqrt(disc)) / 2), abs((tr - math.sqrt(disc)) / 2))
    y = [1.0, 0.0]; peak = 0
    for t in range(600):
        y = [J[0][0] * y[0] + J[0][1] * y[1], J[1][0] * y[0] + J[1][1] * y[1]]
    print(f"   net DC gain sum a_j/(1-D_j) = {dc:.3f} (<1); eigenvalue modulus {mod:.4f}; period {2*math.pi/math.atan2(math.sqrt(-disc)/2, tr/2):.1f}; "
          f"|y| after 600 periods {math.hypot(*y):.1f} (grows)")
    print("   Prop 2.2's criterion needs every channel reinforcing (nonnegative J); correction is not a negative term of Gamma")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A_B(); print(); check_C(); print(); check_D()
