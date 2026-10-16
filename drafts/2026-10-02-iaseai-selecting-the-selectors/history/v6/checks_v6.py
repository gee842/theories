"""Numerical checks for Theory v6.0 (THEORY.md). Pure Python, standard library only.

Each block is named by the code cited in the text and in Appendix B. Results carried unchanged from
v5.2 are checked by ../v5/checks_v5.py and the earlier suites listed in Appendix B; this script covers
what v6 adds or restates. Run:  python3 checks_v6.py > checks_v6.log
"""
import itertools, math, random

def block(name, title):
    print(f"\n=== {name}: {title}")

# ---------------------------------------------------------------- FB
block("FB", "Remark 2.3: local feedback benchmark, ab < mu*delta <=> spectral radius < 1")
random.seed(11)
agree = 0; N = 200000
for _ in range(N):
    a, b = random.uniform(0, 2), random.uniform(0, 2)
    mu, de = random.uniform(1e-3, 1), random.uniform(1e-3, 1)
    tr = 2 - mu - de; det = (1 - mu) * (1 - de) - a * b
    disc = tr * tr / 4 - det
    if disc >= 0:
        r1 = tr / 2 + math.sqrt(disc); r2 = tr / 2 - math.sqrt(disc); rad = max(abs(r1), abs(r2))
    else:
        rad = math.sqrt(det)
    agree += ((rad < 1) == (a * b < mu * de))
print(f"agreement {agree}/{N}")

# ---------------------------------------------------------------- UC
block("UC", "Lemma 3.3(2): a universal constraint is invisible to relative selection; a unilateral one is not")
p = [0.25] * 4; pi = [1.0, 1.2, 0.9, 1.1]; cost = 0.3
def rates(p, pi):
    m = sum(pp * x for pp, x in zip(p, pi)); return [round(x - m, 3) for x in pi]
print("baseline", rates(p, pi))
print("universal cost 0.3", rates(p, [x - cost for x in pi]))
print("cost 0.3 on carrier 1 only", rates(p, [pi[0] - cost] + pi[1:]))

# ---------------------------------------------------------------- TC
block("TC", "Proposition 3.5: two-channel accounting identity and its consequences")
random.seed(5)
fails = 0
for _ in range(4000):
    n = random.randint(2, 7); th = random.uniform(-1, n - 1)
    d = [random.uniform(-3, 3) for _ in range(n)]; db = sum(d) / n
    for i in range(n):
        lhs = d[i] + th * (sum(d) - d[i]) / (n - 1)
        rhs = (1 + th) * db + (n - 1 - th) / (n - 1) * (d[i] - db)
        fails += abs(lhs - rhs) > 1e-9
print(f"identity on 4,000 random games: failures {fails}")
# (4) lambda <-> theta
fails = 0
for _ in range(2000):
    n = random.randint(2, 7); lam = random.uniform(0, 50)
    pis = [random.uniform(-2, 2) for _ in range(n)]
    i = 0; pbar = sum(pis) / n; po = sum(pis[1:]) / (n - 1)
    u = pis[0] + lam * (pis[0] - pbar)
    th = -lam * (n - 1) / (n + lam * (n - 1)); k = 1 + lam * (n - 1) / n
    fails += abs(u - k * (pis[0] + th * po)) > 1e-9
print(f"weight on winning maps to theta = -lam(n-1)/(n+lam(n-1)): failures {fails}")
# (5) rebated levy and renege gain
def dO(d, th, i=0):
    n = len(d); return d[i] + th * (sum(d) - d[i]) / (n - 1)
n, tau, beta, Om = 4, 0.2, 0.5, 1.0
for th in (-1, 0, 1, 3):
    levy = [-tau * (n - 1) / n] + [tau / n] * (n - 1)
    ren = [beta * Om * (n - 1) / n] + [-beta * Om / n] * (n - 1)
    print(f"theta={th}: rebated levy enters as {dO(levy, th):+.4f} (formula {-tau*(n-1-th)/n:+.4f}); renege gain {dO(ren, th):+.4f} (formula {beta*Om*(n-1-th)/n:+.4f})")
# (6) host and spite thresholds
g, H, c, Dy = 0.5, 1.6, 0.1, 0.9
for th in (-1, 0, 1):
    host = [g - H / n] + [-H / n] * (n - 1); spite = [-c] + [-Dy / (n - 1)] * (n - 1)
    print(f"theta={th}: host action value {dO(host, th):+.4f} (formula g-(1+th)H/n {g-(1+th)*H/n:+.4f}); spite value {dO(spite, th):+.4f}, threshold {-(n-1)*c/Dy:+.3f}")

# ---------------------------------------------------------------- TH
block("TH", "Section 3.4: identifying theta from two perturbations")
def e_th(th, n=4, r=1.0, Om=1.0, c=1.0, tau=0.0, l=0.3):
    return r * Om * (n - 1 - th) / (n * n * (c + tau * (n - 1 - th) / n + (1 + th) * l))
h = 1e-7
for th in (-1.0, -0.5, 0.0, 0.4, 1.0, 2.0, 2.9):
    dl = (math.log(e_th(th, l=0.3 + h)) - math.log(e_th(th))) / h
    dt = (math.log(e_th(th, tau=h)) - math.log(e_th(th))) / h
    R = dl / dt; nn = 4; est = (R * (nn - 1) - nn) / (R + nn)
    print(f"theta={th:+.2f}: ratio {R:.4f}, recovered {est:+.4f}")

# ---------------------------------------------------------------- CB
block("CB", "Proposition 3.11: clubs over-produce the harm they do not bear")
def argmax(f, lo=1e-9, hi=1e4):
    for _ in range(300):
        m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2): lo = m1
        else: hi = m2
    return (lo + hi) / 2
W, nn, cc, l, m, lo_ = 10, 4, 1, 0.3, 20, 0.3
Ec = argmax(lambda E: W * math.sqrt(E) - cc * E - nn * l * E)
Ep = argmax(lambda E: W * math.sqrt(E) - cc * E - nn * l * E - m * lo_ * E)
print(f"club intensity {Ec:.3f}, system {Ep:.3f}; harm to non-contestants {m*lo_*Ec:.2f} vs {m*lo_*Ep:.2f}")

# ---------------------------------------------------------------- RI
block("RI", "Remark 5.3: reinvestment threshold chi*r = 1 and the point of enough")
def sim(n=5, r=1.5, chi=1.0, kappa=0.5, Kbar=float('inf'), delta=0.05, Om=1.0, T=6000, seed=1):
    rnd = random.Random(seed)
    K = [1.0 + 0.1 * rnd.random() for _ in range(n)]
    for _ in range(T):
        s = sum(k ** r for k in K); pp = [k ** r / s for k in K]
        K = [(1 - delta) * K[i] + (kappa * (chi * Om * pp[i] + (1 - chi) * Om / n) if K[i] < Kbar else 0.0) for i in range(n)]
    tot = sum(K); return sorted([k / tot for k in K], reverse=True), max(K)
for r in (1.2, 1.5, 2.0, 3.0):
    thr = next((chi for chi in [i / 20 for i in range(1, 21)] if sim(r=r, chi=chi)[0][0] > 0.3), None)
    print(f"r={r}: predicted chi* = 1/r = {1/r:.3f}; first chi on a 0.05 grid with concentration {thr}")
print("K* = kappa*Om/(n*delta) =", 0.5 * 1 / (5 * 0.05))
for Kbar in (1.0, 1.5, 1.9, 2.5):
    sh, mx = sim(Kbar=Kbar)
    print(f"cap {Kbar}: shares {[round(s, 3) for s in sh]}")
# linearized multiplier
for r, chi, de in ((1.5, 1.0, 0.05), (1.5, 0.5, 0.05), (2.0, 0.5, 0.05)):
    print(f"r={r}, chi={chi}: multiplier 1+delta(chi r-1) = {1+de*(chi*r-1):.4f}")

# ---------------------------------------------------------------- RH
block("RH", "Proposition 5.4: race-generated hazard equals a*L*E at the symmetric equilibrium")
def sym_eq(n, r, Om, c, L, th, iters=4000):
    # best-response iteration on a grid-free first-order condition for symmetric equilibrium
    e = 0.1
    for _ in range(iters):
        # marginal objective at symmetric point: Om(1-th/(n-1)) * r(n-1)/(n^2 e) - (c+(1+th)L)
        e = r * Om * (n - 1 - th) / (n * n * (c + (1 + th) * L))
    return e
a = 0.01
for (n, r, Om, c, L, th) in ((4, 1, 1, 1, 0.3, 0), (4, 1, 2, 1, 0.3, -1), (3, 0.8, 1, 0.5, 0.2, 1.0)):
    e = sym_eq(n, r, Om, c, L, th)
    h_direct = a * L * n * e
    h_formula = a * r * Om * L * (n - 1 - th) / (n * (c + (1 + th) * L))
    print(f"n={n}, r={r}, Om={Om}, theta={th}: h direct {h_direct:.6f}, formula {h_formula:.6f}")
# numerical best-response check of the symmetric intensity
def obj(i, es, n, r, Om, c, L, th):
    S = sum(x ** r for x in es)
    pis = [Om * (es[k] ** r / S) - c * es[k] - L * sum(es) for k in range(n)]
    return pis[i] + th * (sum(pis) - pis[i]) / (n - 1)
n, r, Om, c, L, th = 4, 1, 1, 1, 0.3, 0.4
e = sym_eq(n, r, Om, c, L, th)
best = max((obj(0, [x] + [e] * (n - 1), n, r, Om, c, L, th), x) for x in [e * k / 1000 for k in range(1, 3001)])
print(f"symmetric intensity {e:.5f}; best response on a grid {best[1]:.5f}")

# ---------------------------------------------------------------- FS2
block("FS2", "Remark 5.6: the frontier switch (toy)")
def run(theta, n=4, A0=(1.0, 1.0, 1.0, 1.0), F0=1000.0, phi0=0.30, cx=0.05, cy=0.02, dl=0.20, H=0.12,
        rho=0.02, hV=0.0004, T=400, dt=0.05):
    A = list(A0); F = F0; V = 1.0; t = 0.0; phase = None; switch = None; Fsw = None; peak = 0; peakt = 0; Vmin = 1.0
    while t < T:
        alive = [i for i in range(n) if A[i] > 1e-9]; m = len(alive)
        phi = phi0 * F / F0
        ve = (phi - cx) - (1 + theta) * H / max(m, 1)
        va = (-cy - theta * dl / (m - 1)) if m > 1 else -1e9
        choice = 'expand' if ve >= max(va, 0) and ve > 0 else ('attack' if va > 0 else 'idle')
        if choice != phase:
            if phase == 'expand' and choice == 'attack': switch = t; Fsw = F
            phase = choice
        dA = [0.0] * n; tot = sum(A)
        if choice == 'expand':
            for i in alive: dA[i] += A[i] * (phi - cx)
            F = max(0.0, F - dt * tot * phi); load = tot
        else:
            load = 0.0
        if choice == 'attack':
            for i in alive:
                dA[i] -= cy * A[i]
                for j in alive:
                    if j != i: dA[j] -= dl * A[i] / (m - 1)
        V = max(0.0, V + dt * (rho * V * (1 - V) - hV * load * V))
        A = [max(0.0, A[i] + dt * dA[i]) for i in range(n)]
        if sum(A) > peak: peak = sum(A); peakt = t
        Vmin = min(Vmin, V); t += dt
    return dict(final=sum(A), peak=peak, peakt=peakt, F=F, Vmin=Vmin, switch=switch, Fsw=Fsw)
for th in (-1.0, 0.0, 3.0):
    R = run(th)
    print(f"theta={th}: peak {R['peak']:.1f} at t={R['peakt']:.1f}; final stock {R['final']:.3g}; frontier left {R['F']:.1f}; host min {R['Vmin']:.3f}; frontier at switch {R['Fsw']}")
print("predicted frontier at switch, theta=-1:", round(1000 * (0.05 + 0.20 / 3 - 0.02) / 0.30, 1))
R = run(-1.0, A0=(1.2, 1.0, 1.0, 1.0)); print(f"asymmetric start: final stock {R['final']:.1f} = {R['final']/R['peak']:.1%} of peak")
for th in (-1.0, 0.0):
    R = run(th, dl=0.05); print(f"destruction too costly, theta={th}: host min {R['Vmin']:.3f}, switch {R['switch']}")

# ---------------------------------------------------------------- DF
block("DF", "Proposition 5.7, Corollary 5.8, Remark 5.9: decisiveness and enforcement")
random.seed(3)
def objectives(pay, theta, n):
    return [pay[i] + theta * sum(pay[j] for j in range(n) if j != i) / (n - 1) for i in range(n)]
def random_game(n, m):
    return {a: [random.uniform(-1, 1) for _ in range(n)] for a in itertools.product(range(m), repeat=n)}
def stage_nash(G, n, m, theta):
    out = []
    for a in G:
        O = objectives(G[a], theta, n); ok = True
        for i in range(n):
            for x in range(m):
                b = list(a); b[i] = x; b = tuple(b)
                if objectives(G[b], theta, n)[i] > O[i] + 1e-12: ok = False; break
            if not ok: break
        if ok: out.append(a)
    return out
tested = 0; collapse_ok = 0; collapse_tests = 0
for trial in range(400):
    n = random.choice([2, 3]); m = random.choice([2, 3]); theta = random.uniform(-0.9, n - 1); G = random_game(n, m)
    NE = stage_nash(G, n, m, theta)
    if not NE: continue
    for astar in random.sample(list(G), min(6, len(G))):
        Ostar = objectives(G[astar], theta, n)
        ne = min(NE, key=lambda a: sum(objectives(G[a], theta, n)))
        On = objectives(G[ne], theta, n)
        gg = [max(objectives(G[tuple(astar[:i] + (x,) + astar[i + 1:])], theta, n)[i] for x in range(m)) - Ostar[i] for i in range(n)]
        for delta in (0.5, 0.9, 0.99):
            for pd in (0.0, 0.5, 0.9, 1.0):
                D = delta * (1 - pd) / (1 - delta)
                sust = all(gg[i] <= D * (Ostar[i] - On[i]) + 1e-12 for i in range(n))
                tested += 1
                if pd == 1.0:
                    collapse_tests += 1
                    if sust == (astar in NE) or (sust and all(x <= 1e-12 for x in gg)): collapse_ok += 1
print(f"cases evaluated {tested}; at p_d=1, sustainable <=> stage equilibrium in objectives: {collapse_ok}/{collapse_tests}")
def random_symmetric_game(n, m):
    base = {(own, others): random.uniform(-1, 1) for own in range(m) for others in itertools.combinations_with_replacement(range(m), n - 1)}
    return {a: [base[(a[i], tuple(sorted(a[:i] + a[i + 1:])))] for i in range(n)] for a in itertools.product(range(m), repeat=n)}
bad = 0; checks = 0
for trial in range(500):
    n = random.choice([2, 3, 4]); m = random.choice([2, 3]); G = random_symmetric_game(n, m)
    for k in range(m):
        O = objectives(G[tuple([k] * n)], -1.0, n); checks += 1; bad += abs(O[0]) > 1e-12
print(f"symmetric profiles give the relative objective 0 (imitation guarantees 0): violations {bad}/{checks}")
n, b, c, d, eps, delta = 4, 1, 0.3, 0.2, 1, 0.9
A = eps * (b - d) - c; B = eps * (b / (n - 1) + d); K = c + n * eps * d
print(f"theta* = {A/B:.4f}")
for pd in (0, 0.5, 0.9, 0.99, 1):
    D = delta * (1 - pd) / (1 - delta); print(f"  p_d={pd}: theta_rep = {(A-D*K)/(B+D*K):+.3f}")
for th in (0.0, 0.4):
    pd_star = next(x / 1000 for x in range(1001) if th < (A - (delta * (1 - x / 1000) / (1 - delta)) * K) / (B + (delta * (1 - x / 1000) / (1 - delta)) * K))
    print(f"  theta={th}: enforced restraint lost once p_d > {pd_star:.3f}")
# brute force against the closed form in the binary game
random.seed(1); bad = 0; Nb = 0
for _ in range(20000):
    n = random.randint(2, 6); b = random.uniform(0.1, 2); c = random.uniform(0, 1); d = random.uniform(0.01, 1)
    eps = random.uniform(1, 10); th = random.uniform(-1, n - 1); delta = random.uniform(0.01, 0.99); pd = random.uniform(0, 1)
    A = eps * (b - d) - c
    if A <= 0: continue
    B = eps * (b / (n - 1) + d); K = c + n * eps * d; Nb += 1
    gain = A - B * th; pun = -(1 + th) * K; D = delta * (1 - pd) / (1 - delta)
    brute = 'III' if gain <= 0 else ('II' if gain <= D * (0 - pun) + 1e-12 else 'I')
    form = 'III' if th >= A / B else ('II' if th >= (A - D * K) / (B + D * K) else 'I')
    bad += brute != form
print(f"binary game: closed form vs brute force, {Nb} draws, mismatches {bad}")

# ---------------------------------------------------------------- WG
block("WG", "Proposition 5.10: what a decisive winner gives")
for th in (0.4, 1, 2, 3):
    best = max((math.log(1 - s) + th * math.log(s / 3), s) for s in [k / 10000 for k in range(1, 10000)])
    print(f"theta={th}: log-utility share {best[1]:.3f} (formula {th/(1+th):.3f})")
print("linear payoffs: objective slope in s is W(theta/(n-1)-1) <= 0, zero only at theta=n-1")

# ---------------------------------------------------------------- TK
block("TK", "Proposition 5.14(1): in zero-sum sender-receiver games every equilibrium gives the no-talk value")
random.seed(17); games = 0; eqs = 0; viol = 0
for _ in range(300):
    S = random.choice([2, 3]); Aa = random.choice([2, 3]); M = 2
    prior = [random.random() for _ in range(S)]; z = sum(prior); prior = [x / z for x in prior]
    uR = [[random.uniform(-1, 1) for _ in range(Aa)] for _ in range(S)]   # receiver payoff; sender = -uR
    v0 = max(sum(prior[s] * uR[s][a] for s in range(S)) for a in range(Aa))
    games += 1
    for sstrat in itertools.product(range(M), repeat=S):
        for rstrat in itertools.product(range(Aa), repeat=M):
            ok = True
            for msg in range(M):   # receiver best responds on path
                post = [prior[s] if sstrat[s] == msg else 0 for s in range(S)]
                if sum(post) == 0: continue
                val = [sum(post[s] * uR[s][a] for s in range(S)) for a in range(Aa)]
                if val[rstrat[msg]] < max(val) - 1e-12: ok = False; break
            if not ok: continue
            for s in range(S):     # sender best responds (minimizes receiver payoff)
                if uR[s][rstrat[sstrat[s]]] > min(uR[s][rstrat[mm]] for mm in range(M)) + 1e-12: ok = False; break
            if not ok: continue
            eqs += 1
            UR = sum(prior[s] * uR[s][rstrat[sstrat[s]]] for s in range(S))
            viol += abs(UR - v0) > 1e-9
print(f"games {games}, pure equilibria found {eqs}, equilibria whose receiver payoff differs from the no-talk value: {viol}")

# ---------------------------------------------------------------- SH
block("SH", "Proposition 8.6: pooling, sharing in one common field, and convertibility")
def th_eff(beta, th0, n):
    return (th0 * (1 - beta) + beta * (1 + th0) * (n - 1) / n) / ((1 - beta) + beta * (1 + th0) / n)
mono = all(th_eff(b2, th0, n) > th_eff(b1, th0, n) for n in (2, 4, 7) for th0 in (-0.5, 0, 1) if th0 < n - 1
           for b1, b2 in zip([i / 20 for i in range(20)], [(i + 1) / 20 for i in range(20)]))
print("theta_eff strictly increasing in beta:", mono, "; at beta=1:", round(th_eff(1, 0, 4), 6))
def Delta(y, x, Oe, n, r, c):
    return Oe * (y ** r - x ** r) / (y ** r + (n - 1) * x ** r) - c * (y - x)
for (n, r, c, Oe) in ((4, 1.0, 1.0, 1.0), (4, 1.0, 1.0, 0.5), (4, 1.0, 1.0, 2.0), (4, 0.5, 1.0, 1.0), (3, 0.8, 0.7, 1.3), (6, 1.0, 2.0, 1.0)):
    xs = r * Oe / (n * c)
    worst = max(Delta(y, xs, Oe, n, r, c) for y in [xs * k / 500 for k in range(1, 3001)])
    print(f"n={n}, r={r}, c={c}, Omega_eff={Oe}: x* = {xs:.4f}; best mutant advantage {worst:.2e}")
print("x* with Omega_e=1: no sharing", 0.25, "; half shared", 0.5 * 1 / 4, "; with Omega_s=1, none shared", 2 / 4, "; all shared", 1 / 4)
def field_diff(beta, es=(0.2, 0.05, 0.1, 0.1), Om=1.0, c=1.0):
    S = sum(es); return (1 - beta) * Om * (es[0] - es[1]) / S - c * (es[0] - es[1])
print(f"common field (0.2,0.05,0.1,0.1): carrier 0.2 minus carrier 0.05 at beta=0.5: {field_diff(0.5):+.4f}; sign change at beta = {1-0.15*0.45/0.15:.3f}")
print(f"  at beta=0.9: {field_diff(0.9):+.4f}")

# ---------------------------------------------------------------- PE
block("PE", "Proposition 8.11: a point of enough")
hbar = 0.05; Y = 8; U0 = 1; slope = 0.5
S = 1; t = 0
while True:
    u = max(0, 1 - (U0 + slope * t) / Y)
    if u == 0: break
    S *= 1 - hbar * u; t += 1
print(f"capability frozen at need: survival {S:.3f}, coverage catches up at t={t}")
S = 1
for t in range(400):
    Yt = 8 * math.exp(0.1 * t); u = max(0, 1 - (U0 + slope * t) / Yt); S *= 1 - hbar * u
print(f"capability compounding at 10%: survival at t=400 {S:.2e}")
for Om in (1, 10, 100):
    print(f"  Tullock intensity at stakes {Om}: {1*Om*(4-1-0)/(16*(1+0.3)):.3f} (linear in the stakes)")

# ---------------------------------------------------------------- FD
block("FD", "Lemma 7.11: fallback dominance example")
def surv(h, H):
    S = 1
    for t in range(H): S *= 1 - h(t)
    return S
hc = lambda t: min(0.05 * (0.2 + 0.01 * t) + 0.001, 1)
def arr(H, q, ha, shift):
    tot = 0
    for tau in range(H + 1):
        S = 1
        for t in range(H):
            S *= 1 - (ha if t < tau else hc(max(t - shift, 0)))
        tot += (q * (1 - q) ** tau if tau < H else (1 - q) ** H) * S
    return tot
for q in (0.02,):
    print(f"dissolution {q}:", [(H, round(arr(H, q, 0.001 + 0.05 * 0.01, 10), 3), round(surv(hc, H), 3)) for H in (10, 30, 100)], "(arrangement, continuation)")
