"""f3: Proposition 2.3(2) (caps, diffusion, equality), the sign of correction/depreciation by channel form,
and Remark S2.1's multiplier.  Standard library only; all outcomes by direct simulation or numerical Jacobian.

(A) Cap at K_bar <= K*: the laggard's net inflow with others HELD at the cap, with diffusion:
      phi(K) = kap Om[(1-beta) K^r/(K^r+(n-1)Kbar^r) + beta/n] + k0 - dK K + df (n-1)(Kbar-K)/n.
    Local stability at K_bar = K* iff  Gamma_0 (n-1)/n < 1 + df (n-1)/(n dK),  Gamma_0 = (1-beta) r omega
    (derivation: phi(K*) = 0 and phi'(K*) = dK[Gamma_0 (n-1)/n - 1] - df (n-1)/n).  For K_bar < K* a laggard
    just below returns.  Restoration from every start iff phi > 0 on (0, Kbar); with r > 1 this needs inflow
    not tied to rank (sharing, provision or diffusion): phi(0+) = beta kap Om/n + k0 + df (n-1) Kbar/n.
(B) d-sign by channel: ratio-form strength (r ln X) vs level-form strength (a X); numerical spectral radius.
(C) Remark S2.1: the single-channel multiplier is 1 + (dK + df)(Gamma - 1); multi-channel: the secular root.
"""
import math

def simulate_cap(n, r, kap, Om, dK, beta, k0, df, cap, K_lag0, T=20000):
    K = [K_lag0] + [cap] * (n - 1)
    for _ in range(T):
        P = sum(x ** r for x in K); p = [x ** r / P for x in K]; m = sum(K) / n
        K = [min(cap, (1 - dK) * K[i] + kap * Om * ((1 - beta) * p[i] + beta / n) + k0 - df * (K[i] - m)) for i in range(n)]
    return K

def phi(K, n, r, kap, Om, dK, beta, k0, df, cap):
    return kap * Om * ((1 - beta) * K ** r / (K ** r + (n - 1) * cap ** r) + beta / n) + k0 - dK * K + df * (n - 1) * (cap - K) / n

def part_A():
    print("(A) caps: local stability at K_bar = K* and the role of diffusion")
    for (n, r, beta, k0, df) in [(2, 3.0, 0.0, 0.0, 0.0), (2, 1.5, 0.0, 0.0, 0.0), (4, 2.0, 0.0, 0.0, 0.0), (4, 1.2, 0.0, 0.0, 0.0),
                                 (5, 1.5, 0.0, 0.0, 0.0), (2, 3.0, 0.0, 0.0, 0.6), (4, 2.0, 0.0, 0.0, 0.3), (4, 2.0, 0.0, 0.0, 0.1),
                                 (3, 2.0, 0.3, 0.0, 0.0), (3, 2.0, 0.0, 0.05, 0.0)]:
        kap, Om, dK = 0.5, 1.0, 0.2
        Ks = (kap * Om / n + k0) / dK; om = kap * Om / (kap * Om + n * k0); G0 = (1 - beta) * r * om
        lhs = G0 * (n - 1) / n; rhs = 1 + df * (n - 1) / (n * dK)
        Kend = simulate_cap(n, r, kap, Om, dK, beta, k0, df, Ks, 0.999 * Ks)[0]
        pred = "returns" if lhs < rhs else "falls away"
        obs = "returns" if Kend > 0.99 * Ks else "falls away"
        print(f"   n={n} r={r} beta={beta} k0={k0} df={df}: Gamma0(n-1)/n={lhs:.3f} vs 1+df(n-1)/(n dK)={rhs:.3f} -> predicted {pred}; "
              f"laggard from 0.999 K* ends at {Kend/Ks:.4f} K* ({obs}) {'OK' if pred==obs else 'MISMATCH'}")
    Ks2 = (0.5 * 1.0 / 2) / 0.2
    for frac in (0.98, 0.9):
        Kend = simulate_cap(2, 3.0, 0.5, 1.0, 0.2, 0.0, 0.0, 0.0, frac * Ks2, 0.999 * frac * Ks2)[0]
        print(f"   strictly lower cap ({frac} K*), n=2 r=3 (Gamma=3), no diffusion: laggard from 0.999 cap ends at {Kend/(frac*Ks2):.4f} cap ({'returns' if Kend > 0.99*frac*Ks2 else 'falls away'})")
    print("   diffusion as the third restoring source (n=2, r=2, d=0.2, df=0.6, cap=K*=2.5, beta=k0=0): from K=0.01 ->",
          f"{simulate_cap(2,2.0,1.0,1.0,0.2,0.0,0.0,0.6,2.5,0.01)}")
    mn = min(phi(k / 1000 * 2.5, 2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.6, 2.5) for k in range(1, 1000))
    print(f"   min phi on (0, Kbar) = {mn:.4f} > 0 (restored from every start without sharing or provision)")
    print("   necessity: beta=k0=df=0, r=2, n=2, cap=0.9 K*: laggard from 0.3 cap ->", f"{simulate_cap(2,2.0,1.0,1.0,0.2,0.0,0.0,0.0,2.25,0.3*2.25)[0]:.2e} (excluded)")
    print("   with df=0.05 only: laggard from 0.3 cap ->", f"{simulate_cap(2,2.0,1.0,1.0,0.2,0.0,0.0,0.05,2.25,0.3*2.25)[0]:.4f};",
          "phi(0+)=", f"{phi(1e-9,2,2.0,1.0,1.0,0.2,0.0,0.0,0.05,2.25):.4f}", "min phi on (0,Kbar)=", f"{min(phi(k/1000*2.25,2,2.0,1.0,1.0,0.2,0.0,0.0,0.05,2.25) for k in range(1,1000)):.4f}")

def spectral_radius_dev(step, Xs, n, m, h=1e-6):
    # Jacobian of agent 0's deviation under a sum-zero perturbation
    J = [[0.0] * m for _ in range(m)]
    for col in range(m):
        S = [list(Xs) for _ in range(n)]
        S[0][col] += h
        for i in range(1, n): S[i][col] -= h / (n - 1)
        S2 = step(S)
        for row in range(m): J[row][col] = (S2[0][row] - Xs[row]) / h
    # power iteration with shift
    v = [1.0] * m; lam = 0.0
    for _ in range(3000):
        w = [sum(J[i][k] * v[k] for k in range(m)) + 2 * v[i] for i in range(m)]
        nrm = math.sqrt(sum(x * x for x in w)); v = [x / nrm for x in w]; lam = nrm
    return lam - 2

def part_B():
    print("(B) sign of d by channel form (n=2, kap*Om=1, k0=0.2, df=0.1): numerical spectral radius of the deviation map")
    n, Om, kap, k0, df, beta = 2, 1.0, 1.0, 0.2, 0.1, 0.0
    for form in ("ratio", "level"):
        for d in (0.1, 0.2, 0.3, 0.6):
            Xs = (kap * Om / n + k0) / d
            def step(S):
                if form == "ratio": s = [2.0 * math.log(S[i][0]) for i in range(n)]
                else: s = [1.2 * S[i][0] for i in range(n)]
                mx = max(s); e = [math.exp(t - mx) for t in s]; Z = sum(e); p = [t / Z for t in e]
                m = sum(S[i][0] for i in range(n)) / n
                return [[(1 - d) * S[i][0] + kap * Om * ((1 - beta) * p[i] + beta / n) + k0 - df * (S[i][0] - m)] for i in range(n)]
            rj = 2.0 if form == "ratio" else 1.2 * Xs
            om = kap * Om / (kap * Om + n * k0)
            G = (1 - beta) * rj * om * d / (d + df)
            rho = spectral_radius_dev(step, [Xs], n, 1)
            print(f"   {form}-form, d={d}: r_j={rj:.3f} Gamma={G:.3f} spectral radius={rho:.4f} -> {'stable' if rho<1 else 'UNSTABLE'}")
    print("   -> faster depreciation of a ratio-form stock raises Gamma (with diffusion); correction of a level-form stock lowers it")
    print("   Gamma_delta of a ratio-form channel rises with d even without diffusion: d/dd [delta d/(1-delta(1-d))] has sign delta(1-delta) > 0")

def part_C():
    print("(C) Remark S2.1: exact growth factor of a single-channel gap vs 1+(dK+df)(Gamma-1) and vs the text's 1+dK(Gamma-1)")
    n, Om, kap, k0, beta = 2, 1.0, 1.0, 0.0, 0.0
    for (d, df, r) in [(0.2, 0.0, 3.0), (0.2, 0.1, 2.0), (0.05, 0.05, 3.0), (0.2, 0.3, 1.2)]:
        Xs = (kap * Om / n + k0) / d
        def step(S):
            s = [r * math.log(S[i][0]) for i in range(n)]
            mx = max(s); e = [math.exp(t - mx) for t in s]; Z = sum(e); p = [t / Z for t in e]
            m = sum(S[i][0] for i in range(n)) / n
            return [[(1 - d) * S[i][0] + kap * Om * p[i] + k0 - df * (S[i][0] - m)] for i in range(n)]
        om = 1.0; G = r * om * d / (d + df)
        rho = spectral_radius_dev(step, [Xs], n, 1)
        print(f"   d={d} df={df} r={r}: Gamma={G:.3f}; exact multiplier {rho:.4f}; 1+(d+df)(Gamma-1)={1+(d+df)*(G-1):.4f}; text 1+d(Gamma-1)={1+d*(G-1):.4f}; "
              f"periods 1%->50%: exact {math.log(50)/math.log(rho):.1f}, text {math.log(50)/math.log(1+d*(G-1)) if 1+d*(G-1)>1 else float('inf'):.1f}")
    print("   two channels with different turnover and the same Gamma=1.2: the multiplier is the secular root, not a function of Gamma alone")
    for (dK, dZ) in [(0.5, 0.5), (0.02, 0.02), (0.5, 0.02)]:
        # gains gK + gZ = 1.2 split equally; secular equation 1 = gK dK/(lam-(1-dK)) + gZ dZ/(lam-(1-dZ))
        gK = gZ = 0.6
        lo, hi = 1 - min(dK, dZ) + 1e-9, 5.0
        for _ in range(200):
            m = (lo + hi) / 2
            val = gK * dK / (m - (1 - dK)) + gZ * dZ / (m - (1 - dZ))
            if val > 1: lo = m
            else: hi = m
        print(f"   dK={dK}, dZ={dZ}: lambda*={hi:.4f}; periods 1%->50% = {math.log(50)/math.log(hi):.0f}")

if __name__ == "__main__":
    part_A(); part_B(); part_C()
