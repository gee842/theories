"""m1: Proposition 2.2 with THREE stocks and a strength function that is not log-linear in every stock,
plus the price of standing on the same model, plus the Prop 2.3 cap boundary at K_bar = K*.

Independent of checks_v61.py LG, which only tests two stocks with sigma = r ln K + r a Z.
Here sigma_i = r1 ln X1 + a X2 + b sqrt(X3). Stability decided by (i) the Perron root of the deviation
Jacobian (finite differences on the actual map) and (ii) nonlinear simulation of a small deviation.
"""
import math, random

def make(P):
    n, r1, a, b, Om, beta, kap, k0, d, df = P
    def sigma(X):  # X = (X1, X2, X3)
        return r1*math.log(X[0]) + a*X[1] + b*math.sqrt(X[2])
    def step(S):  # S: list of n stock vectors
        s = [sigma(X) for X in S]; mx = max(s)
        e = [math.exp(t-mx) for t in s]; Z = sum(e); p = [t/Z for t in e]
        W = [Om*((1-beta)*p[i] + beta/n) for i in range(n)]
        mean = [sum(S[i][j] for i in range(n))/n for j in range(3)]
        return [[(1-d[j])*S[i][j] + kap[j]*W[i] + k0[j] - df[j]*(S[i][j]-mean[j]) for j in range(3)] for i in range(n)], W
    Xs = [(kap[j]*Om/n + k0[j])/d[j] for j in range(3)]
    # r_j = d sigma / d ln X_j at the steady state
    r = [r1, a*Xs[1], 0.5*b*math.sqrt(Xs[2])]
    om = [kap[j]*Om/(kap[j]*Om + n*k0[j]) if kap[j]*Om + n*k0[j] > 0 else 0.0 for j in range(3)]
    G = (1-beta)*sum(r[j]*om[j]*d[j]/(d[j]+df[j]) for j in range(3))
    return sigma, step, Xs, r, om, G

def perron(J, iters=4000):
    m = len(J); c = 1.0  # shift so the Perron root is strictly dominant in modulus
    v = [1.0]*m
    lam = 0.0
    for _ in range(iters):
        w = [sum(J[i][k]*v[k] for k in range(m)) + c*v[i] for i in range(m)]
        nrm = math.sqrt(sum(x*x for x in w)); v = [x/nrm for x in w]; lam = nrm
    return lam - c

def dev_jacobian(P, step, Xs, h=1e-6):
    n = P[0]
    J = [[0.0]*3 for _ in range(3)]
    for col in range(3):
        S = [list(Xs) for _ in range(n)]
        S[0][col] += h
        for i in range(1, n): S[i][col] -= h/(n-1)
        S2, _ = step(S)
        for row in range(3): J[row][col] = (S2[0][row]-Xs[row])/h
    return J

def run_A(N=3000, seed=1):
    rnd = random.Random(seed); mis = 0; near = 0; tested = 0
    for _ in range(N):
        n = rnd.randint(2, 6); r1 = rnd.uniform(0.2, 2.5); a = rnd.uniform(0, 1.5); b = rnd.uniform(0, 2)
        Om = rnd.uniform(0.5, 3); beta = rnd.uniform(0, 0.8)
        kap = [rnd.uniform(0.05, 1), rnd.uniform(0, 0.5), rnd.uniform(0, 0.8)]
        k0 = [rnd.choice([0.0, rnd.uniform(0, 0.5)]) for _ in range(3)]
        d = [rnd.uniform(0.02, 0.6) for _ in range(3)]
        df = [rnd.choice([0.0, rnd.uniform(0, 0.3)]) for _ in range(3)]
        df = [min(df[j], 1-d[j]) for j in range(3)]
        P = (n, r1, a, b, Om, beta, kap, k0, d, df)
        sigma, step, Xs, r, om, G = make(P)
        if min(Xs) <= 1e-9: continue
        J = dev_jacobian(P, step, Xs)
        rho = perron(J)
        if abs(G-1) < 2e-3: near += 1; continue
        tested += 1
        if (rho > 1) != (G > 1): mis += 1
    print(f"(A) three stocks, sigma = r1 ln X1 + a X2 + b sqrt(X3): {tested} systems, Perron root > 1 <=> Gamma > 1 mismatches: {mis} (skipped {near} near the boundary)")

def run_Aprime():
    print("(A') nonlinear simulation, three stocks, deviation 1e-4 for 3000 periods:")
    base = dict(n=4, Om=1.0, beta=0.0, kap=[0.5, 0.2, 0.3], k0=[0.0, 0.0, 0.1], d=[0.05, 0.2, 0.1], df=[0.0, 0.0, 0.05])
    for (r1, a, b) in [(1.2, 0.0, 0.0), (0.7, 0.8, 0.0), (0.7, 0.0, 1.5), (0.5, 0.3, 0.6), (0.9, 0.6, 0.8)]:
        P = (base['n'], r1, a, b, base['Om'], base['beta'], base['kap'], base['k0'], base['d'], base['df'])
        sigma, step, Xs, r, om, G = make(P)
        n = P[0]
        S = [list(Xs) for _ in range(n)]
        S[0][0] *= 1 + 1e-4
        for i in range(1, n): S[i][0] *= 1 - 1e-4/(n-1)
        for _ in range(3000): S, W = step(S)
        gap = (max(x[0] for x in S) - min(x[0] for x in S))/Xs[0]
        print(f"   r1={r1}, a={a}, b={b}: r_j={[round(x,3) for x in r]}, omega={[round(x,3) for x in om]}, Gamma={G:.3f} -> gap {gap:.2e} ({'grows' if gap > 2e-4 else 'decays'})")

def run_B(seed=2):
    print("(B) price of standing on the three-stock model: PV of a relative payoff shock vs Gamma_delta/(1-Gamma_delta)")
    rnd = random.Random(seed); worst = 0.0; cnt = 0
    for _ in range(200):
        n = rnd.randint(2, 5); r1 = rnd.uniform(0.2, 2); a = rnd.uniform(0, 1); b = rnd.uniform(0, 1.5)
        Om = rnd.uniform(0.5, 2); beta = rnd.uniform(0, 0.7)
        kap = [rnd.uniform(0.05, 1), rnd.uniform(0, 0.5), rnd.uniform(0, 0.6)]
        k0 = [rnd.uniform(0, 0.4) for _ in range(3)]
        d = [rnd.uniform(0.05, 0.6) for _ in range(3)]
        df = [rnd.uniform(0, 0.2) for _ in range(3)]; df = [min(df[j], 1-d[j]) for j in range(3)]
        dl = rnd.uniform(0.5, 0.97)
        P = (n, r1, a, b, Om, beta, kap, k0, d, df)
        sigma, step, Xs, r, om, G = make(P)
        Gd = (1-beta)*sum(r[j]*om[j]*dl*d[j]/(1-dl*(1-d[j]-df[j])) for j in range(3))
        if G >= 1 or Gd > 0.9: continue
        lam = Gd/(1-Gd)
        x = 1e-6
        S = [list(Xs) for _ in range(n)]
        _, W0 = step(S); base = W0[0]
        S[0] = [Xs[j] + kap[j]*x for j in range(3)]
        pv = 0.0; disc = dl
        T = int(math.log(1e-13)/math.log(dl*max(0.5, 1-min(d)))) + 100
        for _ in range(T):
            S, W = step(S); pv += disc*(W[0]-base); disc *= dl
        est = pv/(x*(n-1)/n)
        worst = max(worst, abs(est-lam)/max(1e-9, lam)); cnt += 1
    print(f"   {cnt} systems with Gamma<1, Gd<0.9: max relative error {worst:.2e}")

def run_cap():
    print("(C) Prop 2.3(2) at the boundary K_bar = K*: 'no higher than' includes equality, where the cap does not protect")
    n, r, kap, Om, dK, beta, k0 = 5, 1.5, 0.5, 1.0, 0.05, 0.0, 0.0
    Ks = (kap*Om/n + k0)/dK
    def phi(K, cap):
        return kap*Om*((1-beta)*K**r/(K**r + (n-1)*cap**r) + beta/n) + k0 - dK*K
    for cap in (Ks, 0.98*Ks, 0.9*Ks):
        K = [0.97*cap] + [cap]*(n-1)
        for _ in range(40000):
            Ssum = sum(k**r for k in K); p = [k**r/Ssum for k in K]
            K = [min(cap, (1-dK)*K[i] + kap*Om*((1-beta)*p[i] + beta/n) + k0) for i in range(n)]
        slope = (phi(cap, cap) - phi(cap*(1-1e-6), cap))/(cap*1e-6)
        print(f"   cap/K* = {cap/Ks:.2f}: phi(cap) = {phi(cap,cap):+.4f}, phi'(cap) = {slope:+.4f}, laggard from 0.97 cap ends at {K[0]:.4f} ({'excluded/stalled' if K[0] < 0.99*cap else 'returns to cap'})")
    print(f"   at equality phi'(K*) = dK[(1-beta) r omega (n-1)/n - 1] = {dK*((1-beta)*r*1.0*(n-1)/n - 1):+.4f} (positive here, so a laggard just below K* diverges)")

if __name__ == '__main__':
    run_A(); run_Aprime(); run_B(); run_cap()
