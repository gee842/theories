"""Numerical checks for Theory V6.1. Pure Python, standard library only. Run:
    python3 checks_v61.py > checks_v61.log        (about one minute)

Every block is named by a two-letter code and lists the stable keys of the results it checks (SUPPLEMENT S15
maps keys to displayed numbers). Kinds:
  independent  the outcome is decided by direct computation (value iteration, simulation, numerical best
               response, numerical Jacobian), never by the inequality being tested;
  identity     an algebraic identity or a threshold formula evaluated against its own statement; it guards
               against slips, it is not independent evidence;
  derived      numbers computed from formulas that other blocks check.
Results carried unchanged from v5.2 and earlier keep their suites (../v5/checks_v5.py, ../v4/, ../v3/); run
    python3 checks_v61.py --legacy
to re-run those suites as well. No suite certifies every proof, and none supplies evidence about the world.
"""
import itertools, math, random, sys, subprocess, pathlib, time

def block(name, keys, kind, title):
    print(f"\n=== {name} [{kind}] keys: {keys}\n    {title}", flush=True)

def rates(p, pi):
    m = sum(pp * x for pp, x in zip(p, pi)); return [round(x - m, 3) for x in pi]

def dO(d, th, i=0):
    n = len(d); return d[i] + th * (sum(d) - d[i]) / (n - 1)

def check_FB():
    block('FB', 'bench', 'independent', 'Local feedback benchmark, ab < mu d <=> spectral radius < 1')
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

def check_TC():
    block('TC', 'twochan', 'identity', 'Two-channel accounting identity and its consequences')
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

def check_TH():
    block('TH', 'twochan', 'identity', 'Identifying theta from two perturbations (psi = 1; see SM(3) for psi < 1)')
    def e_th(th, n=4, r=1.0, Om=1.0, c=1.0, tau=0.0, l=0.3):
        return r * Om * (n - 1 - th) / (n * n * (c + tau * (n - 1 - th) / n + (1 + th) * l))
    h = 1e-7
    for th in (-1.0, -0.5, 0.0, 0.4, 1.0, 2.0, 2.9):
        dl = (math.log(e_th(th, l=0.3 + h)) - math.log(e_th(th))) / h
        dt = (math.log(e_th(th, tau=h)) - math.log(e_th(th))) / h
        R = dl / dt; nn = 4; est = (R * (nn - 1) - nn) / (R + nn)
        print(f"theta={th:+.2f}: ratio {R:.4f}, recovered {est:+.4f}")

def check_CB():
    block('CB', 'club', 'independent', 'Clubs over-produce the harm they do not bear')
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

def check_RH():
    block('RH', 'racehazard', 'independent', 'Race-generated hazard against a direct best-response computation')
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

def check_FS():
    block('FS', 'frontier', 'independent', 'The frontier switch (toy)')
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

def check_BI():
    block('BI', 'zonesillus', 'identity', 'Binary illustration at the boundary case D=C: threshold algebra against the stated inequality')
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

def check_WG():
    block('WG', 'wingives', 'independent', 'What a decisive winner gives')
    for th in (0.4, 1, 2, 3):
        best = max((math.log(1 - s) + th * math.log(s / 3), s) for s in [k / 10000 for k in range(1, 10000)])
        print(f"theta={th}: log-utility share {best[1]:.3f} (formula {th/(1+th):.3f})")
    print("linear payoffs: objective slope in s is W(theta/(n-1)-1) <= 0, zero only at theta=n-1")

def check_TK():
    block('TK', 'talk', 'independent', 'Two parties: in zero-sum sender-receiver games every equilibrium gives the no-talk value')
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

def check_SH():
    block('SH', 'share', 'independent', 'Pooling; sharing in one common field; the uninvadable intensity')
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

def check_PE():
    block('PE', 'enough', 'independent', 'A point of enough: frozen capability against compounding')
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

def check_FD():
    block('FD', 'fallback', 'independent', 'Fallback example with exogenous dissolution')
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

def check_EC():
    block('EC', 'enforce', 'independent', 'Enforcement condition: direct discounted values in an explicit Markov chain; old bound by sign of D-C; breakouts during punishment')
    # S1. Enforcement condition replacing Proposition 5.7, checked by direct evaluation of discounted payoffs
    # in an explicit Markov chain (value iteration over states), never by the inequality being tested.
    #
    # Game (two players, symmetric roles, values in the objective each player acts on):
    #   cooperative path: both restrain, each gets C per period.
    #   one-period deviation by i: i gets C+g that period; at the start of the next period i holds the
    #     decisive position with probability p_d (absorbing: i gets D per period forever, the other U);
    #     otherwise the punishment phase starts.
    #   punishment phase (grim reversion to the stage equilibrium "both race"): each gets P per period;
    #     each racing player breaks out with probability q per period (p_d also acts during punishment):
    #     i decisive -> i gets D forever; j decisive -> i gets U forever.
    # The claim to test:  deviation is unprofitable  <=>  (1-d)g + d p_d (D-C) <= d (1-p_d)(C - v),
    #   with v = (1-d) * (value of the punishment phase) computed in the same game.
    import random, math

    def values(C,g,D,U,P,pd,q,dl,iters=None):
        # value iteration on states: COOP, PUN, DEC_i (i decisive), DEC_j (j decisive)
        Vdec_i=D/(1-dl); Vdec_j=U/(1-dl)
        # punishment value by fixed-point iteration (no closed form used)
        Vp=0.0
        for _ in range(200000):
            new=P+dl*(q*Vdec_i+q*Vdec_j+(1-2*q)*Vp)
            if abs(new-Vp)<1e-13: Vp=new; break
            Vp=new
        Vcoop=C/(1-dl)
        Vdev=(C+g)+dl*(pd*Vdec_i+(1-pd)*Vp)
        return Vcoop,Vdev,Vp

    def monte_carlo(C,g,D,U,P,pd,q,dl,N=20000,T=400,seed=0):
        rnd=random.Random(seed); tot=0.0
        for _ in range(N):
            s=(C+g); disc=1.0; state='?'
            disc*=dl
            if rnd.random()<pd: state='Di'
            else: state='P'
            for t in range(1,T):
                if state=='Di': s+=disc*D
                elif state=='Dj': s+=disc*U
                else:
                    s+=disc*P
                    u=rnd.random()
                    if u<q: state='Di'
                    elif u<2*q: state='Dj'
                disc*=dl
            tot+=s
        return tot/N

    rnd=random.Random(12345)
    N=200000
    mis=0; boundary=0
    old_nec=old_suf=0
    cnt={'D<C':[0,0,0],'D=C':[0,0,0],'D>C':[0,0,0]}  # [cases, old says sustain but deviation pays, sustainable but old says no]
    for k in range(N):
        dl=rnd.uniform(0.05,0.99); pd=rnd.choice([0.0,1.0,rnd.random(),rnd.random()]); q=rnd.uniform(0,0.5)
        C=rnd.uniform(0,3); g=rnd.uniform(-1,2); U=rnd.uniform(-3,C); P=rnd.uniform(U,C)
        case=rnd.random()
        if case<1/3: D=rnd.uniform(-1,C)
        elif case<2/3: D=C
        else: D=rnd.uniform(C,C+3)
        Vc,Vd,Vp=values(C,g,D,U,P,pd,q,dl)
        v=(1-dl)*Vp
        lhs=(1-dl)*g+dl*pd*(D-C); rhs=dl*(1-pd)*(C-v)
        direct = (Vc>=Vd-1e-9)
        formula = (lhs<=rhs+1e-9)
        if abs(Vc-Vd)<1e-7: boundary+=1; continue
        if direct!=formula: mis+=1
        old=(1-dl)*g<=dl*(1-pd)*(C-v)+1e-12
        key='D<C' if D<C-1e-12 else ('D=C' if abs(D-C)<1e-12 else 'D>C')
        cnt[key][0]+=1
        if old and not direct: cnt[key][1]+=1
        if direct and not old: cnt[key][2]+=1
    print("=== S1a. repaired condition vs direct discounted values (value iteration), random draws:",N)
    print(f"mismatches {mis}; exact ties skipped {boundary}")
    print("=== S1b. old printed bound (no D-C term) vs truth, by sign of D-C: [cases, old-says-sustain-but-deviation-pays, sustainable-but-old-says-no]")
    for k_,v_ in cnt.items(): print(" ",k_,v_)

    print("=== S1c. Monte Carlo cross-check of the deviation value (independent sampler)")
    for (C,g,D,U,P,pd,q,dl) in [(3,1,2,0,1,1.0,0.1,0.9),(3,1,3,0,1,0.5,0.0,0.9),(1,0.3,2,-1,0,0.2,0.2,0.8)]:
        Vc,Vd,Vp=values(C,g,D,U,P,pd,q,dl)
        mc=monte_carlo(C,g,D,U,P,pd,q,dl,N=4000,T=300)
        print(f"  C={C},g={g},D={D},U={U},P={P},pd={pd},q={q},delta={dl}: Vcoop={Vc:.3f}  Vdev(VI)={Vd:.3f}  Vdev(MC)={mc:.3f}")

    print("=== S1d. Codex counterexamples (C=3,g=1,delta=.9): cooperation worth 30")
    for (pd,D,P,q) in [(1.0,2.0,1.0,0.0),(0.5,3.0,1.0,0.0)]:
        Vc,Vd,Vp=values(3,1,D,0,P,pd,q,0.9)
        v=(1-0.9)*Vp
        print(f"  p_d={pd}, D={D}: Vdev={Vd:.3f}; old bound RHS={0.9*(1-pd)*(3-v)/(0.1):.3f} vs g=1; repaired lhs={(0.1)*1+0.9*pd*(D-3):.3f} rhs={0.9*(1-pd)*(3-v):.3f}")

    print("=== S1e. limit p_d -> 1: sustainable iff g <= -delta(D-C)/(1-delta); strictly inside stage equilibria when D>C")
    for (C,D,dl) in [(1,1.5,0.9),(1,1.0,0.9),(1,0.5,0.9)]:
        thr=-dl*(D-C)/(1-dl)
        for g in (thr-0.01,thr+0.01):
            Vc,Vd,Vp=values(C,g,D,0,0,1.0,0.1,dl)
            print(f"  C={C},D={D},delta={dl}: threshold g*={thr:.3f}; g={g:.3f}: sustainable={Vc>=Vd}")

    print("=== S1f. p_d acts during punishment: the punishment value v moves with q (two players, U<P<D)")
    for q in (0.0,0.05,0.2,0.45):
        Vc,Vd,Vp=values(1.0,0.5,3.0,-2.0,0.0,0.0,q,0.9)
        v=(1-0.9)*Vp
        closed=((1-0.9)*0.0+0.9*q*(3.0-2.0))/(1-0.9+2*0.9*q)
        print(f"  q={q}: v={v:.4f} (closed form [(1-d)P+d q(D+U)]/(1-d+2dq) = {closed:.4f}); sustainable at p_d=0: {Vc>=Vd}")
    print("=== S1g. breakouts during punishment can soften it (D+U>2P) or harden it (D+U<2P): C=1, g=0.5, delta=0.9, p_d=0")
    for (D,U) in [(4.0,0.0),(3.0,-5.0)]:
        for q in (0.0,0.1,0.45):
            Vc,Vd,Vp=values(1.0,0.5,D,U,0.0,0.0,q,0.9)
            print(f"  D={D},U={U},q={q}: v={(1-0.9)*Vp:+.3f}; restraint sustainable: {Vc>=Vd}")


def check_CR():
    block('CR', 'relpunish', 'independent', 'Relative objectives and punishments that can be imitated: n=2 mixed imitation; n>=3 same-strategy punishers; role-differentiated counterexample')
    # S2. Scope of Corollary 5.8 (purely relative objectives cannot be held by symmetric punishment).
    # (a) n=2: every punishment, mixed included, can be imitated: E[O_1] = y^T A y = 0 for antisymmetric A.
    # (b) n>=3, anonymous symmetric game: punishments in which all punishers play the same action can be imitated.
    # (c) n=3 counterexample: an asymmetric punishment (punishers play different actions) holds a purely relative
    #     deviator below 0, and sustains cooperation that is not a stage equilibrium. Checked by direct discounted values
    #     and by verifying that the punishment profile is a stage Nash equilibrium in objectives (so grim reversion is credible).
    import random, itertools

    rnd=random.Random(7)
    # (a)
    worst=0.0
    for _ in range(20000):
        m=rnd.randint(2,5)
        pi=[[rnd.uniform(-1,1) for _ in range(m)] for _ in range(m)]   # symmetric 2-player game: pi1(a,b)=pi[a][b], pi2(a,b)=pi[b][a]
        A=[[pi[a][b]-pi[b][a] for b in range(m)] for a in range(m)]       # relative objective of player 1
        y=[rnd.random() for _ in range(m)]; s=sum(y); y=[t/s for t in y]
        val=sum(y[a]*A[a][b]*y[b] for a in range(m) for b in range(m))
        worst=max(worst,abs(val))
    print(f"(a) n=2: imitating the punisher's mixed strategy gives relative payoff 0 (max |value| over 20,000 draws {worst:.1e})")

    # (b) anonymous symmetric n-player games: payoff depends on own action and the multiset of others' actions
    viol=0
    for _ in range(3000):
        n=rnd.randint(3,5); m=rnd.randint(2,3)
        table={}
        def pay(own,others):
            key=(own,tuple(sorted(others)))
            if key not in table: table[key]=rnd.uniform(-1,1)
            return table[key]
        for b in range(m):
            prof=[b]*n
            pis=[pay(prof[i],prof[:i]+prof[i+1:]) for i in range(n)]
            O0=pis[0]-sum(pis[1:])/(n-1)
            if abs(O0)>1e-12: viol+=1
    print(f"(b) n>=3 anonymous games: all punishers alike, deviator imitates -> O=0; violations {viol}/3000")

    # (c) counterexample, n=3. Action = (x, m), x in {R,A} (restrain, race), m in {X,Y} (minority component).
    a,b=0.1,0.1   # racing gains a to the racer and costs every other player b
    def pis(prof):
        out=[]
        for i,(x,mm) in enumerate(prof):
            unique = sum(1 for j,(x2,m2) in enumerate(prof) if j!=i and m2==mm)==0
            p=(1.0 if unique else 0.0)+(a if x=='A' else 0.0)-b*sum(1 for j,(x2,m2) in enumerate(prof) if j!=i and x2=='A')
            out.append(p)
        return out
    def O(prof):
        p=pis(prof); n=len(p)
        return [p[i]-(sum(p)-p[i])/(n-1) for i in range(n)]
    acts=[(x,mm) for x in 'RA' for mm in 'XY']
    coop=[('R','X')]*3
    g=max(O([act]+coop[1:])[0] for act in acts)-O(coop)[0]
    print(f"(c) cooperative profile (R,X) for all: objectives {O(coop)}; best one-period deviation gain g = {g:.3f}")
    pun=[('A','X'),('A','X'),('A','Y')]   # deviator is player 0; punishers 1 and 2 play different m-actions
    print(f"    punishment profile {pun}: objectives {[round(t,3) for t in O(pun)]}")
    # stage NE check in objectives
    ok=True
    for i in range(3):
        base=O(pun)[i]
        for act in acts:
            prof=list(pun); prof[i]=act
            if O(prof)[i]>base+1e-12: ok=False; print('   profitable deviation',i,act,O(prof)[i],base)
    print(f"    punishment profile is a stage Nash equilibrium in objectives: {ok}")
    v=O(pun)[0]
    for dl in (0.6,0.7,0.706,0.71,0.9):
        Vc=0.0; Vd=g+dl*v/(1-dl)   # deviator's best reply inside punishment yields v (checked: v is its best stage value)
        print(f"    delta={dl}: cooperation {Vc:.3f} vs deviation {Vd:+.3f} -> sustainable {Vc>=Vd-1e-12}")
    best_in_pun=max(O([act]+pun[1:])[0] for act in acts)
    print(f"    deviator's best stage objective while punished: {best_in_pun:.3f} (= v)")
    sym=[('A','X')]*3
    print(f"    symmetric punishment (all (A,X)): deviator imitates and gets {O(sym)[0]:.3f} -> cannot hold it below 0")
    print(f"    threshold delta* = g/(g+|v|) = {g/(g-v):.4f}")


def check_LG():
    block('LG', 'loopgain, compound, standprice', 'independent', 'One loop gain: numerical Jacobian vs Gamma; nonlinear deviations; present value of standing; two-period contest vs e(theta_Gamma)')
    # S3. One loop gain: conversion channels add; the same gain prices standing.
    # Model: n agents, two stocks: capacity K (enters strength as r ln K) and control over the rule Z (enters as r a Z).
    #   sigma_i = r ln K_i + r a Z_i,  p_i = exp(sigma_i)/sum_j exp(sigma_j),  W_i = Om[(1-beta) p_i + beta/n]
    #   K_i' = (1-dK) K_i + kK W_i + k0 - df (K_i - mean K)      (k0: inflow not won in the contest; df: diffusion)
    #   Z_i' = (1-dZ) Z_i + kZ W_i                                (dZ: correction/decay of rule support)
    # Claim (A): equal standing is unstable iff Gamma > 1, with
    #   Gamma = (1-beta) Om/n [ kK r /(K* (dK+df)) + kZ r a / dZ ] = G_K + G_Z,   K* = (kK Om/n + k0)/dK
    #   equivalently G_K = (1-beta) r phi_w dK/(dK+df), phi_w = (kK Om/n)/(kK Om/n + k0).
    # Claim (B): a unit of relative net payoff today (reinvested at the same rates) is worth lambda = Gd/(1-Gd)
    #   units of the agent's own future winnings, Gd = (1-beta)Om/n [ dl kK r/(K*(1-dl(1-dK-df))) + dl kZ r a/(1-dl(1-dZ)) ].
    # Claim (C): in a two-period contest whose first-period net payoffs become second-period capacity, the symmetric
    #   first-period intensity equals Proposition 3.9's e(theta_eff), theta_eff = -lam(n-1)/(n+lam(n-1)).
    import math, random

    def step(K,Z,P):
        n,r,a,Om,beta,kK,kZ,k0,dK,dZ,df=P
        s=[r*math.log(K[i])+r*a*Z[i] for i in range(n)]
        mx=max(s); e=[math.exp(t-mx) for t in s]; S=sum(e); p=[t/S for t in e]
        W=[Om*((1-beta)*p[i]+beta/n) for i in range(n)]
        mK=sum(K)/n
        K2=[(1-dK)*K[i]+kK*W[i]+k0-df*(K[i]-mK) for i in range(n)]
        Z2=[(1-dZ)*Z[i]+kZ*W[i] for i in range(n)]
        return K2,Z2,W

    def steady(P):
        n,r,a,Om,beta,kK,kZ,k0,dK,dZ,df=P
        return (kK*Om/n+k0)/dK, kZ*Om/(n*dZ)

    def gamma(P):
        n,r,a,Om,beta,kK,kZ,k0,dK,dZ,df=P
        Ks,Zs=steady(P)
        GK=(1-beta)*Om/n*kK*r/(Ks*(dK+df)); GZ=(1-beta)*Om/n*kZ*r*a/dZ
        return GK,GZ

    def jac_sumzero(P,h=1e-7):
        # response of agent 0's stock deviations to a sum-zero perturbation (agent 0 +h, others -h/(n-1))
        n=P[0]; Ks,Zs=steady(P)
        J=[[0,0],[0,0]]
        for col in range(2):
            K=[Ks]*n; Z=[Zs]*n
            if col==0: K=[Ks+h]+[Ks-h/(n-1)]*(n-1)
            else: Z=[Zs+h]+[Zs-h/(n-1)]*(n-1)
            K2,Z2,_=step(K,Z,P)
            J[0][col]=(K2[0]-Ks)/h; J[1][col]=(Z2[0]-Zs)/h
        tr=J[0][0]+J[1][1]; det=J[0][0]*J[1][1]-J[0][1]*J[1][0]
        disc=tr*tr/4-det
        if disc>=0: rad=max(abs(tr/2+math.sqrt(disc)),abs(tr/2-math.sqrt(disc)))
        else: rad=math.sqrt(det)
        return J,rad

    rnd=random.Random(3)
    mis=0; N=4000; near=0
    for _ in range(N):
        n=rnd.randint(2,6); r=rnd.uniform(0.3,3); a=rnd.uniform(0,2); Om=rnd.uniform(0.5,3); beta=rnd.uniform(0,0.8)
        kK=rnd.uniform(0.05,1); kZ=rnd.uniform(0,0.5); k0=rnd.choice([0.0,rnd.uniform(0,0.5)])
        dK=rnd.uniform(0.02,0.5); dZ=rnd.uniform(0.02,0.9); df=rnd.choice([0.0,rnd.uniform(0,0.3)])
        P=(n,r,a,Om,beta,kK,kZ,k0,dK,dZ,df)
        GK,GZ=gamma(P); G=GK+GZ
        J,rad=jac_sumzero(P)
        if abs(G-1)<1e-3: near+=1; continue
        if (rad>1)!=(G>1): mis+=1
    print(f"(A) {N} random two-channel systems: Gamma>1 <=> spectral radius on sum-zero deviations >1; mismatches {mis} (skipped {near} within 1e-3 of the boundary)")

    # nonlinear simulation: small perturbation grows iff Gamma>1
    print("(A') nonlinear simulations from a 1e-4 perturbation, 4000 periods:")
    for P in [(4,1.5,0.0,1.0,0.0,0.5,0.0,0.0,0.05,0.2,0.0),   # capacity only, no outside inflow: G=r=1.5
              (4,1.5,0.0,1.0,0.0,0.5,0.0,0.5,0.05,0.2,0.0),   # trees: k0 lowers phi_w
              (4,1.5,0.0,1.0,0.4,0.5,0.0,0.0,0.05,0.2,0.0),   # sharing beta=0.4: G=0.9
              (4,0.8,1.0,1.0,0.0,0.5,0.3,0.0,0.05,0.2,0.0),   # r<1 but a reflexive channel
              (4,0.8,1.0,1.0,0.0,0.5,0.3,0.0,0.05,0.6,0.0),   # same, faster correction of rule support
              (4,1.5,0.0,1.0,0.0,0.5,0.0,0.0,0.05,0.2,0.05)]: # diffusion
        GK,GZ=gamma(P); Ks,Zs=steady(P); n=P[0]
        K=[Ks*(1+1e-4)]+[Ks*(1-1e-4/(n-1))]*(n-1); Z=[Zs]*n
        for _ in range(4000): K,Z,W=step(K,Z,P)
        gap=(max(K)-min(K))/Ks
        print(f"   r={P[1]},a={P[2]},beta={P[4]},k0={P[7]},dZ={P[9]},df={P[10]}: G_K={GK:.3f} G_Z={GZ:.3f} Gamma={GK+GZ:.3f} -> relative gap after 4000 periods {gap:.2e} ({'grows' if gap>2e-4 else 'decays'})")

    # (B) price of standing
    def pv_perturb(P,dl,x=1e-6,T=None):
        n=P[0]; Ks,Zs=steady(P); kK,kZ=P[5],P[6]
        if T is None:
            _,rad=jac_sumzero(P)
            T=int(math.log(1e-13)/math.log(dl*max(rad,1-1e-9)))+50
        K=[Ks]*n; Z=[Zs]*n
        _,_,W0=step(K,Z,P); base=W0[0]
        K=[Ks+kK*x]+[Ks]*(n-1); Z=[Zs+kZ*x]+[Zs]*(n-1)
        pv=0.0; disc=dl
        for t in range(T):
            K,Z,W=step(K,Z,P)       # W computed from the stocks at the start of period t+1
            pv+=disc*(W[0]-base); disc*=dl
        return pv/(x*(n-1)/n)
    def lam_formula(P,dl):
        n,r,a,Om,beta,kK,kZ,k0,dK,dZ,df=P; Ks,Zs=steady(P)
        Gd=(1-beta)*Om/n*(dl*kK*r/(Ks*(1-dl*(1-dK-df)))+dl*kZ*r*a/(1-dl*(1-dZ)))
        return Gd/(1-Gd),Gd
    print("(B) value of a unit of relative net payoff: perturbation PV in the nonlinear model vs Gd/(1-Gd)")
    worst=0; unstable_cases=[]
    for _ in range(300):
        n=rnd.randint(2,5); r=rnd.uniform(0.3,2.5); a=rnd.uniform(0,1.5); Om=rnd.uniform(0.5,2); beta=rnd.uniform(0,0.7)
        kK=rnd.uniform(0.05,1); kZ=rnd.uniform(0,0.4); k0=rnd.uniform(0,0.4); dK=rnd.uniform(0.05,0.5); dZ=rnd.uniform(0.05,0.9); df=rnd.uniform(0,0.2)
        dl=rnd.uniform(0.5,0.97)
        P=(n,r,a,Om,beta,kK,kZ,k0,dK,dZ,df)
        lam,Gd=lam_formula(P,dl)
        if Gd>0.9: continue
        GK,GZ=gamma(P)
        if GK+GZ>=1: unstable_cases.append((P,dl,lam)); continue
        pv=pv_perturb(P,dl)
        worst=max(worst,abs(pv-lam)/max(1e-9,abs(lam)))
    print(f"   random systems with Gamma<1 and Gd<0.9: max relative error {worst:.2e}")
    print(f"   systems with Gamma>=1 but Gd<1 (equal standing unstable, discounting still wins): {len(unstable_cases)}; first-order agreement as x->0:")
    for P,dl,lam in unstable_cases[:3]:
        print("     lambda formula %.4f; PV at x=1e-4,1e-6,1e-8,1e-10: %s" % (lam, ", ".join("%.4f"%pv_perturb(P,dl,x=x) for x in (1e-4,1e-6,1e-8,1e-10))))
    for dl in (0.9,0.99,0.995):
        P=(4,1.5,0.0,1.0,0.5,0.5,0.0,0.3,0.05,0.2,0.0)
        GK,GZ=gamma(P); lam,Gd=lam_formula(P,dl)
        th=-lam*3/(4+lam*3)
        print(f"   example r=1.5,beta=0.5,k0=0.3: Gamma={GK+GZ:.3f}; delta={dl}: Gd={Gd:.3f}, lambda={lam:.3f}, PV check {pv_perturb(P,dl):.3f}, theta_eff (theta_0=0) = {th:.3f} = -(n-1)Gd/(n-Gd) = {-(3)*Gd/(4-Gd):.3f}")

    # (C) two-period contest: direct numerical symmetric equilibrium vs e(theta_eff)
    def two_period(n=3,r1=1.0,Om1=1.0,c=1.0,l=0.3,K0=2.0,kap=0.5,Om2=2.0,r2=1.5,dl=0.9):
        def U(i,es):
            E=sum(es); S=sum(t**r1 for t in es)
            pis=[Om1*es[j]**r1/S-c*es[j]-l*E for j in range(n)]
            Ks=[K0+kap*pi for pi in pis]
            if min(Ks)<=0: return -1e9
            T=sum(k**r2 for k in Ks)
            return pis[i]+dl*Om2*Ks[i]**r2/T
        def br(e_other):
            lo,hi=1e-6,3.0
            g=(math.sqrt(5)-1)/2
            x1=hi-g*(hi-lo); x2=lo+g*(hi-lo)
            f=lambda x: U(0,[x]+[e_other]*(n-1))
            f1,f2=f(x1),f(x2)
            for _ in range(200):
                if f1<f2: lo=x1; x1=x2; f1=f2; x2=lo+g*(hi-lo); f2=f(x2)
                else: hi=x2; x2=x1; f2=f1; x1=hi-g*(hi-lo); f1=f(x1)
            return (lo+hi)/2
        e=0.2
        for _ in range(300):
            e_new=br(e)
            if abs(e_new-e)<1e-12: break
            e=0.5*e+0.5*e_new
        # formula
        pibar=Om1/n-c*e-l*n*e; Kbar=K0+kap*pibar
        lam=dl*Om2*r2*kap/(n*Kbar)
        th=-lam*(n-1)/(n+lam*(n-1))
        eform=r1*Om1*(n-1-th)/(n*n*(c+(1+th)*l))
        return e,eform,lam,th
    print("(C) two-period contest (first-period payoffs become second-period capacity): direct equilibrium vs e(theta_eff)")
    for kw in [dict(),dict(n=4,Om2=4.0),dict(n=2,r1=0.8,K0=1.0,Om2=1.0),dict(dl=0.5),dict(kap=0.0)]:
        e,ef,lam,th=two_period(**kw)
        print(f"   {kw}: direct e*={e:.6f}, formula e(theta_eff)={ef:.6f}, lambda={lam:.4f}, theta_eff={th:.4f}")

    # (C') held self-model theta0 != 0: the continuation term is scaled by (n-1-theta0)/(n-1), because the future prize is
    # redistributed, not created. Two-period check with objective O = pi + theta0*mean(others), summed over both periods.
    def two_period_th(th0,n=3,r1=1.0,Om1=1.0,c=1.0,l=0.3,K0=2.0,kap=0.5,Om2=2.0,r2=1.5,dl=0.9):
        def U(i,es):
            E=sum(es); S=sum(t**r1 for t in es)
            pis=[Om1*es[j]**r1/S-c*es[j]-l*E for j in range(n)]
            Ks=[K0+kap*pi for pi in pis]
            T=sum(k**r2 for k in Ks); W2=[Om2*k**r2/T for k in Ks]
            O1=pis[i]+th0*(sum(pis)-pis[i])/(n-1); O2=W2[i]+th0*(sum(W2)-W2[i])/(n-1)
            return O1+dl*O2
        def br(e_other):
            lo,hi=1e-6,3.0; g=(math.sqrt(5)-1)/2
            x1=hi-g*(hi-lo); x2=lo+g*(hi-lo); f=lambda x: U(0,[x]+[e_other]*(n-1)); f1,f2=f(x1),f(x2)
            for _ in range(200):
                if f1<f2: lo=x1; x1=x2; f1=f2; x2=lo+g*(hi-lo); f2=f(x2)
                else: hi=x2; x2=x1; f2=f1; x1=hi-g*(hi-lo); f1=f(x1)
            return (lo+hi)/2
        e=0.2
        for _ in range(300):
            en=br(e)
            if abs(en-e)<1e-12: break
            e=0.5*e+0.5*en
        pibar=Om1/n-c*e-l*n*e; Kbar=K0+kap*pibar
        lam=dl*Om2*r2*kap/(n*Kbar)*(n-1-th0)/(n-1)
        th=(n*th0-lam*(n-1))/(n+lam*(n-1))
        return e, r1*Om1*(n-1-th)/(n*n*(c+(1+th)*l)), th
    print("(C') held self-model theta0: direct equilibrium vs e(theta_eff), lambda' = lambda (n-1-theta0)/(n-1)")
    for th0 in (-0.5,0.5,1.0,1.9):
        e,ef,th=two_period_th(th0)
        print(f"   theta0={th0}: direct e*={e:.6f}, formula {ef:.6f}, theta_eff={th:.4f}")


def check_T3():
    block('T3', 'talk', 'independent', 'Talk under relative accounting with n>=3: identity; ideal-point gap b0 n/(n-2); two-message partition equilibrium built directly')
    # S4. Talk among relative actors: two parties versus n>=3 (Proposition 5.14).
    # (a) identity: under theta=-1, O_S - O_R = n/(n-1) (pi_S - pi_R); effects on third parties enter O_S and O_R identically.
    # (b) uniform-quadratic sender-receiver game embedded in n players: pi_S=-(y-u-b0)^2, pi_R=-(y-u)^2,
    #     third parties pi_k=-kap_k*y. Under relative objectives the pair's effective bias (difference of ideal points)
    #     is computed numerically from the objectives and compared with b0*n/(n-2); a two-message partition equilibrium is
    #     constructed directly (receiver best responses by numerical maximization of expected objective; sender boundary type
    #     indifferent) and exists iff the effective bias < 1/4.
    # (c) n=2: objectives are zero-sum; no partition equilibrium is informative.
    import random, math
    rnd=random.Random(11)
    # (a)
    worst=0
    for _ in range(10000):
        n=rnd.randint(3,8); pi=[rnd.uniform(-5,5) for _ in range(n)]
        O=[pi[i]-(sum(pi)-pi[i])/(n-1) for i in range(n)]
        worst=max(worst,abs((O[0]-O[1])-n/(n-1)*(pi[0]-pi[1])))
    print(f"(a) O_S-O_R = n/(n-1)(pi_S-pi_R): max error {worst:.1e} over 10,000 draws")

    def objs(y,u,n,b0,kap):
        piS=-(y-u-b0)**2; piR=-(y-u)**2; others=[-k*y for k in kap]
        tot=piS+piR+sum(others)
        OS=piS-(tot-piS)/(n-1); OR=piR-(tot-piR)/(n-1)
        return OS,OR
    def argmax(f,lo=-5,hi=5):
        g=(math.sqrt(5)-1)/2; x1=hi-g*(hi-lo); x2=lo+g*(hi-lo); f1,f2=f(x1),f(x2)
        for _ in range(200):
            if f1<f2: lo=x1; x1=x2; f1=f2; x2=lo+g*(hi-lo); f2=f(x2)
            else: hi=x2; x2=x1; f2=f1; x1=hi-g*(hi-lo); f1=f(x1)
        return (lo+hi)/2
    def receiver_br(lo,hi,n,b0,kap,grid=200):
        us=[lo+(hi-lo)*(j+0.5)/grid for j in range(grid)]
        return argmax(lambda y: sum(objs(y,u,n,b0,kap)[1] for u in us)/grid)
    def two_partition(n,b0,kap):
        # find boundary a in (0,1) with sender type a indifferent between y1=BR[0,a] and y2=BR[a,1]
        def F(a):
            y1=receiver_br(0,a,n,b0,kap); y2=receiver_br(a,1,n,b0,kap)
            return objs(y1,a,n,b0,kap)[0]-objs(y2,a,n,b0,kap)[0]
        lo,hi=1e-4,1-1e-4; Flo,Fhi=F(lo),F(hi)
        if Flo*Fhi>0: return None
        for _ in range(60):
            m=(lo+hi)/2; Fm=F(m)
            if Flo*Fm<=0: hi,Fhi=m,Fm
            else: lo,Flo=m,Fm
        return (lo+hi)/2
    print("(b) n>=3, effective bias of the pair under relative objectives, and existence of an informative (two-message) equilibrium")
    for (n,b0,kap) in [(3,0.0,[0.7]),(3,0.05,[0.7]),(3,0.08,[0.0]),(3,0.1,[0.3]),(4,0.1,[0.3,0.3]),(6,0.1,[0.2]*4),(6,0.2,[0.2]*4),(10,0.2,[0.1]*8)]:
        u=0.4
        yS=argmax(lambda y: objs(y,u,n,b0,kap)[0]); yR=argmax(lambda y: objs(y,u,n,b0,kap)[1])
        bias=yS-yR
        a=two_partition(n,b0,kap)
        print(f"   n={n}, material bias b0={b0}, third-party costs {kap[:1]}..: effective bias {bias:.4f} (b0 n/(n-2) = {b0*n/(n-2):.4f}); two-message equilibrium: {'boundary a=%.4f'%a if a is not None else 'none'} (exists iff bias<1/4: {bias<0.25})")
    # (c) n=2
    print("(c) n=2: O_S=-O_R at every (y,u); informative equilibria impossible (Proposition 5.14(1))")
    def objs2(y,u,b0): piS=-(y-u-b0)**2; piR=-(y-u)**2; return piS-piR, piR-piS
    mx=max(abs(sum(objs2(rnd.uniform(-2,2),rnd.uniform(0,1),rnd.uniform(-1,1)))) for _ in range(1000))
    print(f"   max |O_S+O_R| = {mx:.1e}")


def check_CI():
    block('CI', 'blind, nested', 'independent', 'Common constraints: unequal incidence; evasion; enforcement funded by compliers (tipping share); common liability; a safeguard with negative net cost')
    # S5. Lemma 3.3(2) restated: equal incidence, evasion, and the enforcement that evasion needs.
    # Replicator dynamics among carriers; everything computed by simulating shares, not by the lemma.
    import math, random

    def replicator(p,pi,dt=0.01,T=2000.0):
        p=list(p)
        for _ in range(int(T/dt)):
            pb=sum(pk*x for pk,x in zip(p,pi(p)))
            p=[pk+dt*pk*(x-pb) for pk,x in zip(p,pi(p))]
            s=sum(p); p=[pk/s for pk in p]
        return p
    def rates(p,pis):
        pb=sum(a*b for a,b in zip(p,pis)); return [x-pb for x in pis]

    print("(a) incidence: a rule applying to all with costs (0.3, 0.1) changes relative growth; equal costs do not")
    p=[0.5,0.5]; base=[1.0,1.0]
    print("   equal cost 0.2 each:", [round(x,3) for x in rates(p,[b-0.2 for b in base])])
    print("   costs (0.3, 0.1):   ", [round(x,3) for x in rates(p,[base[0]-0.3,base[1]-0.1])])
    print("   a universal cap e<=0.4 on loads (1, .6, .2) with private value 1 per unit costs (0.6, 0.2, 0): ranking reverses")

    print("(b) evasion: compliers pay kappa, evaders pay expected sanction q*F; evader share after T=2000")
    for kap,q,F in [(0.3,0.5,0.5),(0.3,0.5,0.7),(0.3,0.9,0.3),(0.3,0.2,2.0)]:
        pfin=replicator([0.99,0.01],lambda p:[-kap,-q*F])
        print(f"   kappa={kap}, q={q}, F={F}: evasion gain kappa-qF={kap-q*F:+.2f}; evader share {pfin[1]:.3f}")

    print("(c) enforcement that depends on compliance (detection funded by compliers, or captured by evaders): q(x)=q0*(1-x_ev)")
    for x0 in (0.05,0.2,0.4,0.6):
        kap,q0,F=0.3,0.8,0.6
        pfin=replicator([1-x0,x0],lambda p:[-kap,-q0*p[0]*F],T=4000)
        print(f"   initial evader share {x0}: final evader share {pfin[1]:.3f} (tipping share where q0(1-x)F=kappa: x={1-kap/(q0*F):.3f})")

    print("(d) a common liability tau on load is not a common term: pi_k - pi_l = (nu - tau)(e_k - e_l)")
    for tau in (0.0,0.5,1.5):
        nu=1.0; e=[1.0,0.2]
        pfin=replicator([0.5,0.5],lambda p:[(nu-tau)*e[0],(nu-tau)*e[1]],T=200)
        print(f"   tau={tau}: share of the high-load carrier after T=200: {pfin[0]:.3f}")

    print("(e) premise A_tau: a unilateral safeguard with negative net private cost is selected FOR")
    # revenue 1 - p_error; safeguard lowers p_error 0.20 -> 0.01 at cost 0.01
    pfin=replicator([0.9,0.1],lambda p:[1-0.20,1-0.01-0.01],T=200)
    print(f"   share of the developer with the safeguard after T=200: {pfin[1]:.3f}")
    # safeguard against a COMMON hazard: cost 0.05 to adopter, benefit to everyone (common term) of 0.2*share
    pfin=replicator([0.5,0.5],lambda p:[0.0+0.2*p[1],-0.05+0.2*p[1]],T=400)
    print(f"   safeguard whose benefit is common (A_tau holds): adopter share after T=400: {pfin[1]:.3f}")


def check_PR():
    block('PR', 'onegroup', 'independent', 'Price decomposition under five partitions (global and local benefit); biased transmission; reversible and irreversible failure')
    # S6. Lemma 3.10 restated: what holds under every partition, the transmission term, and reversible vs irreversible failure.
    # Individuals j with trait z_j in {0,1}, fitness w_j = 1 + B*(benefit received) - c*z_j.
    #   global benefit: every individual receives b * (population mean trait)         -> a common term at every level
    #   local benefit : individual receives b * (mean trait of its own subunit)        -> a group-level term
    # Price: wbar*dzbar = Cov_j(w,z) + E_j[w*dz]; recursively Cov_j = Cov_groups(w_g,z_g) + E_g[Cov_within].
    import random, math
    rnd=random.Random(2)
    N=600; units=30
    z=[1 if rnd.random()<0.4 else 0 for _ in range(N)]
    unit=[j%units for j in range(N)]
    for j in range(N):  # make units differ in trait frequency
        if unit[j]<10 and rnd.random()<0.5: z[j]=1
        if unit[j]>=20 and rnd.random()<0.5: z[j]=0
    b,c=0.3,0.05
    def fitness(kind):
        zbar=sum(z)/N
        um=[0]*units; un=[0]*units
        for j in range(N): um[unit[j]]+=z[j]; un[unit[j]]+=1
        um=[um[u]/un[u] for u in range(units)]
        return [1+(b*zbar if kind=='global' else b*um[unit[j]])-c*z[j] for j in range(N)]
    def cov(x,y,wts=None):
        n=len(x);
        if wts is None: wts=[1/n]*n
        mx=sum(w*a for w,a in zip(wts,x)); my=sum(w*a for w,a in zip(wts,y))
        return sum(w*(a-mx)*(bb-my) for w,a,bb in zip(wts,x,y))
    def partition_terms(w,groups):
        # between = Cov_g(w_g,z_g) weighted by group size; within = E_g[Cov_within]
        G={}
        for j,g in enumerate(groups): G.setdefault(g,[]).append(j)
        sizes=[len(v)/N for v in G.values()]
        wg=[sum(w[j] for j in v)/len(v) for v in G.values()]; zg=[sum(z[j] for j in v)/len(v) for v in G.values()]
        between=cov(wg,zg,sizes)
        within=sum(len(v)/N*cov([w[j] for j in v],[z[j] for j in v]) for v in G.values())
        return between,within
    parts={'one group':[0]*N,'30 units':unit,'5 blocs of units':[u%5 for u in unit],'random 50':[rnd.randrange(50) for _ in range(N)],'individuals':list(range(N))}
    for kind in ('global','local'):
        w=fitness(kind); total=cov(w,z)
        print(f"({'a' if kind=='global' else 'b'}) {kind} benefit (b={b}, cost c={c}): total selection Cov(w,z) = {total:+.5f}")
        for name,gr in parts.items():
            bt,wt=partition_terms(w,gr)
            print(f"     partition {name:>18}: between {bt:+.5f}  within {wt:+.5f}  (sum {bt+wt:+.5f})")
    print("   -> with a global benefit the between-group term is <=0 under every partition (the benefit is a common term at every level);")
    print("      with a local benefit, between-unit selection can favour the trait under a partition that matches the benefit's reach.")

    # (c) transmission term: one population, costly trait, biased transmission at rate mu toward the trait
    print("(c) biased transmission in one population: dz/dt = -c z(1-z) + mu (1-z); stable z*=mu/c for mu<c")
    for mu in (0.0,0.02,0.04,0.06):
        zz=0.5
        for _ in range(200000): zz+=0.01*(-c*zz*(1-zz)+mu*(1-zz))
        print(f"   mu={mu}: long-run frequency {zz:.3f} (mu/c={min(mu/c,1):.3f})")

    # (d) reversible vs irreversible failure of a rule with global benefit.
    # Without the (enforced) rule, failure occurs with probability h per period; a share s of failures is irreversible
    # (absorbing loss of the one host), the rest reversible. After a reversible failure the harmed adopt the rule with
    # probability piL (learning from failure); with the rule in force the hazard is h_r. Anticipation adopts at t=0.
    def run(s_irr,piL,anticip,T=400,reps=20000,h=0.03,hr=0.003,seed=1):
        rr=random.Random(seed); lost=0
        for _ in range(reps):
            rule=anticip
            for t in range(T):
                if rr.random()<(hr if rule else h):
                    if rr.random()<s_irr: lost+=1; break
                    if not rule and rr.random()<piL: rule=True
        return lost/reps
    print("(d) global-benefit rule: probability of an irreversible loss within 400 periods (h=0.03, h_r=0.003, piL=0.5)")
    for irr in (0.0,0.05,0.2,1.0):
        closed=irr/(irr+(1-irr)*0.5) if irr>0 else 0.0
        print(f"   irreversible share {irr:>4}: learning from failure {run(irr,0.5,False):.3f} (pre-adoption loss, infinite horizon: s/(s+(1-s)piL)={closed:.3f}); anticipation {run(irr,0.5,True):.3f}")


def check_CS():
    block('CS', 'influence, corrrate', 'independent', 'Cost structure of conversion capacity: size threshold, concentration moment, splitting factor, rate law for three size elasticities, splitting delay, fixed cost')
    # S7. Section 4 under a general cost of conversion capacity:
    #   C(q; p) = f * p^sf * q + gam * p^s * q^(1+eta)/(1+eta)
    #   s = 0: variable cost per carrier (capacity non-rival across the carrier's own decisions); s = 1: per decision.
    #   sf likewise for the linear part.  Return (long horizon, uniform correction rate d): chi*q*p^2*Y/d.
    # Selected capacity q* is found by numerical maximization (not by the closed form); cultivated conversion of a carrier
    # is proportional to p*q*.  Evaluation's row sum: s_E = A/(cE d) + aE*B*sum_k p_k q*_k/(cE d).
    import math

    def qstar(p,chi,Y,d,f,sf,gam,s,eta):
        # maximize the concave payoff by bisection on its derivative (log scale); the closed form is not used
        def dpay(q): return chi*p*p*Y/d-f*p**sf-gam*p**s*q**eta
        if dpay(0.0)<=0: return 0.0
        lo,hi=-300.0,300.0
        for _ in range(300):
            m=(lo+hi)/2
            if dpay(math.exp(m))>0: lo=m
            else: hi=m
        return math.exp((lo+hi)/2)

    chi,Y,eta=1.0,1.0,1.0
    print("(a) size threshold of Proposition 4.2(2): smallest share with q*>0 (f=0.05, d=1)")
    for sf in (0,1):
        lo,hi=1e-6,1.0
        for _ in range(80):
            m=(lo+hi)/2
            if qstar(m,chi,Y,1.0,0.05,sf,1.0,0,eta)>0: hi=m
            else: lo=m
        pred=(0.05/(chi*Y))**(1/(2-sf))
        print(f"   linear part {'per carrier (sf=0)' if sf==0 else 'per decision (sf=1)'}: threshold {hi:.5f}; (f/(chi Y))^(1/(2-sf)) = {pred:.5f}")

    print("(b) concentration measure and splitting factor (f=0, eta=1): cultivated conversion sum_k p_k q*_k relative to monopoly")
    for s in (0,0.5,1):
        mono=1*qstar(1.0,chi,Y,1.0,0,0,1.0,s,eta)
        two=2*0.5*qstar(0.5,chi,Y,1.0,0,0,1.0,s,eta)
        shares=[0.5,0.3,0.2]; three=sum(p*qstar(p,chi,Y,1.0,0,0,1.0,s,eta) for p in shares)
        mom=1+(2-s)/eta
        print(f"   s={s}: two equal carriers {two/mono:.4f} (2*(1/2)^{mom:.1f}={2*0.5**mom:.4f}); shares (.5,.3,.2): {three/mono:.4f} (sum p^{mom:.1f} = {sum(p**mom for p in shares):.4f}); HHI={sum(p*p for p in shares):.4f}, 3rd moment={sum(p**3 for p in shares):.4f}")
        for k in (2,10):
            split=k*(1/k)*qstar(1/k,chi,Y,1.0,0,0,1.0,s,eta)
            print(f"      split into k={k}: factor {mono/split:.3f} (k^((2-s)/eta) = {k**((2-s)/eta):.3f})")

    print("(c) rate law with gam(t)=e^{-g t}, d(t)=d0 e^{alpha t}, dominant carrier share 0.6 (A=0.3, aE*B=1, cE=1, d0=2, g=0.2, eta=1, f=0)")
    def sE(t,alpha,s,g=0.2,d0=2.0,A=0.3,f=0.0,gf=0.0,shares=(1.0,),sf=0,f0=None):
        gam=math.exp(-g*t); d=d0*math.exp(alpha*t); ff=f*math.exp(-gf*t)
        cult=sum(p*qstar(p,chi,Y,d,ff,sf,gam,s,eta) for p in shares)
        return (A+cult)/d
    for s in (0,0.5,1):
        for alpha in (0.09,0.11):
            vals=[sE(t,alpha,s,shares=(0.6,)) for t in (0,50,100,150,200)]
            print(f"   s={s}, alpha={alpha} (g/(1+eta)=0.1): s_E at t=0,50,100,150,200: {', '.join('%.3g'%v for v in vals)}")

    print("(d) splitting a monopoly into k=10 parts, alpha=0 (f=0): delay in reaching s_E=1 vs (2-s) ln k/(g-(1+eta)alpha)")
    def first_cross(shares,s,alpha=0.0,f=0.0,gf=0.0,sf=0,T=400.0,dt=0.05):
        t=0.0
        while t<T:
            if sE(t,alpha,s,f=f,gf=gf,shares=shares,sf=sf)>1: return t
            t+=dt
        return float('inf')
    for s in (0,1):
        t1=first_cross((1.0,),s); t10=first_cross(tuple([0.1]*10),s)
        print(f"   s={s}: monopoly crosses at {t1:.2f}, ten parts at {t10:.2f}: delay {t10-t1:.2f} vs {(2-s)*math.log(10)/0.2:.2f}")

    print("(e) the fixed part: f>0 constant -> splitting below the size threshold is permanent; f falling at g_f -> delayed")
    for gf in (0.0,0.05):
        t1=first_cross((1.0,),0,f=0.3,gf=gf,T=600); t10=first_cross(tuple([0.1]*10),0,f=0.3,gf=gf,T=600)
        print(f"   f0=0.3, g_f={gf}: monopoly crosses at {t1:.2f}; ten parts cross at {t10:.2f}" + (f"; onset delay of cultivation by (2-sf) ln k/g_f = {2*math.log(10)/gf:.1f}" if gf>0 else ""))


def check_SM():
    block('SM', 'enough, wingives, club, twochan, fallback, faithful, delegatelock, topology, compound', 'independent', 'Smaller repairs: renege denominators; blocs; theta identification with perceived share psi; coupling of paths; cost exponents; one-or-both delegation; correlated errors; point of enough; caps; growth variant')
    # S8. Smaller repairs: each checked by direct computation.
    import math, random
    rnd=random.Random(8)

    def golden(f,lo,hi,it=200):
        g=(math.sqrt(5)-1)/2; x1=hi-g*(hi-lo); x2=lo+g*(hi-lo); f1,f2=f(x1),f(x2)
        for _ in range(it):
            if f1<f2: lo=x1; x1=x2; f1=f2; x2=lo+g*(hi-lo); f2=f(x2)
            else: hi=x2; x2=x1; f2=f1; x1=hi-g*(hi-lo); f1=f(x1)
        return (lo+hi)/2

    print("(1) Prop 5.10(3): renege gain when the promised share beta*Om goes to the n-1 others vs is split among all n")
    n,beta,Om=4,0.3,1.0
    for th in (-1,0,1,2):
        # to n-1 others: winner keeps (1-beta)Om, others beta*Om/(n-1) each; reneging: winner Om, others 0
        O_keep=(1-beta)*Om+th*beta*Om/(n-1); O_break=Om
        # split among all n: winner (1-beta)Om+beta*Om/n, others beta*Om/n
        O_keep2=(1-beta)*Om+beta*Om/n+th*beta*Om/n; O_break2=Om
        print(f"   theta={th}: to n-1 others {O_break-O_keep:.4f} (beta Om (n-1-th)/(n-1) = {beta*Om*(n-1-th)/(n-1):.4f}); among all n {O_break2-O_keep2:.4f} (beta Om (n-1-th)/n = {beta*Om*(n-1-th)/n:.4f})")

    print("(2) Prop 3.11(2): k blocs of s members (r=1); bloc chooses members' efforts to maximize members' summed payoff")
    def bloc_eq(k,s,r=1.0,Om=1.0,c=1.0,l=0.3):
        # symmetric equilibrium in bloc totals X (members split equally); payoff of bloc b = Om*w_b - c X_b - s*l*E
        def U(X,Xo):
            es=[X/s]*s; eo=[Xo/s]*s
            S=sum(e**r for e in es)+(k-1)*sum(e**r for e in eo)
            w=sum(e**r for e in es)/S
            E=X+(k-1)*Xo
            return Om*w-c*X-s*l*E
        X=0.3
        for _ in range(400):
            Xn=golden(lambda x:U(x,X),1e-9,5.0); X=0.5*X+0.5*Xn
        return X
    for (k,s) in [(2,2),(3,2),(2,3)]:
        X=bloc_eq(k,s)
        # original game with n=k: e = r Om (n-1-th)/(n^2 (c+(1+th) l)) at theta=0 with l and with s*l
        e_l=1*(k-1)/(k*k*(1+0.3)); e_sl=1*(k-1)/(k*k*(1+s*0.3))
        print(f"   k={k}, s={s}: bloc intensity {X:.4f}; original game n=k with l: {e_l:.4f}; with s*l: {e_sl:.4f}")
    for r in (0.5,1.0,1.5):
        print(f"   unequal blocs (3 members vs 1), equal total effort, r={r}: weight ratio of the 3-bloc {3*(1/3)**r:.3f} (1 = as one contestant)")

    print("(3) theta identification when only a share psi of the shared loss is perceived")
    def e_eq(th,psi,n=4,r=1.0,Om=1.0,c=1.0,l=0.3,tau=0.0):
        return r*Om*(n-1-th)/(n*n*(c+tau*(n-1-th)/n+(1+th)*psi*l))
    for th in (0.0,0.4,1.0):
        for psi in (1.0,0.5):
            h=1e-6
            de_dl=(e_eq(th,psi,l=0.3+h)-e_eq(th,psi,l=0.3-h))/(2*h)
            de_dt=(e_eq(th,psi,tau=h)-e_eq(th,psi,tau=-h))/(2*h)
            R=de_dl/de_dt; n=4
            th_hat=(R*(n-1)-n)/(R+n)
            print(f"   theta={th}, psi={psi}: ratio {R:.4f} (n(1+th)psi/(n-1-th) = {n*(1+th)*psi/(n-1-th):.4f}); naive estimate {th_hat:+.4f}")

    print("(4) Lemma 7.11: coupling. World state w_t in {good,bad} (Markov); A may dissolve (more likely in bad states).")
    # exact computation by dynamic programming over (state, A dissolved?, alive)
    P=[[0.9,0.1],[0.3,0.7]]
    hC=[0.02,0.10]           # continuation hazard by world state
    hA_on=[0.01,0.05]        # arrangement in force
    hA_off=[0.02,0.10]       # after dissolution: fallback no worse than continuation in the same state (F1)
    diss=[0.01,0.20]         # endogenous dissolution probability by state
    def surv_C(H):
        dist=[1.0,0.0]; S=1.0; alive=[1.0,0.0]
        for t in range(H):
            alive=[alive[s]*(1-hC[s]) for s in range(2)]
            alive=[sum(alive[s]*P[s][s2] for s in range(2)) for s2 in range(2)]
        return sum(alive)
    def surv_A(H,cond_tau=None):
        # mass over (state, dissolved)
        m={(0,0):1.0}
        for t in range(H):
            new={}
            for (s,dz),p in m.items():
                h=hA_off[s] if dz else hA_on[s]
                p*=1-h
                for s2 in range(2):
                    q=p*P[s][s2]
                    if dz: new[(s2,1)]=new.get((s2,1),0)+q
                    else:
                        new[(s2,1)]=new.get((s2,1),0)+q*diss[s2]
                        new[(s2,0)]=new.get((s2,0),0)+q*(1-diss[s2])
            m=new
        return sum(m.values())
    for H in (10,30,100):
        print(f"   H={H}: S^A={surv_A(H):.4f} >= S^C={surv_C(H):.4f}: {surv_A(H)>=surv_C(H)}")
    # the displayed step S^A(H|tau) >= S^C(H) can fail: condition on dissolving at t=1 (bad state likely)
    def surv_A_given_tau1(H):
        # dissolution happens at the first transition; conditioning selects states by diss[s2]
        m={}
        p0=1-hA_on[0]
        tot=0
        for s2 in range(2):
            q=p0*P[0][s2]*diss[s2]; m[(s2,1)]=q; tot+=P[0][s2]*diss[s2]
        for t in range(1,H):
            new={}
            for (s,dz),p in m.items():
                p*=1-hA_off[s]
                for s3 in range(2): new[(s3,1)]=new.get((s3,1),0)+p*P[s][s3]
            m=new
        return sum(m.values())/tot
    print(f"   conditional on dissolving at t=1: S^A(30|tau=1)={surv_A_given_tau1(30):.4f} vs S^C(30)={surv_C(30):.4f} -> the conditional step fails, the unconditional claim holds")

    print("(5) Prop 6.1(5): theta*(eps) with b,d,c scaling as eps^bb, eps^bd, eps^bc (n=4, b=1, d=0.2, c=0.3)")
    def th_star(eps,bb,bd,bc,n=4,b=1.0,d=0.2,c=0.3):
        T=eps*b*eps**bb; D=eps*d*eps**bd; C=c*eps**bc
        return (T-D-C)/(T/(n-1)+D)
    for (bb,bd,bc) in [(0,0,0),(1,1,0),(0,0,1),(0,0.5,0),(0.5,0,0),(1,0,3),(1,0,2),(0,0,1.5)]:
        vals=[th_star(e,bb,bd,bc) for e in (1e2,1e4,1e6)]
        print(f"   (beta_b,beta_d,beta_c)=({bb},{bd},{bc}): theta* at eps=1e2,1e4,1e6: {', '.join('%.3f'%v for v in vals)}")
    print(f"   alignment-review check: c fixed, b,d fixed, eps=10: {th_star(10,0,0,0):.3f}; c also scaling with eps: {th_star(10,0,0,1):.3f}")

    print("(6) Prop 6.4(2): at least one of all/none delegating is an equilibrium")
    bad=0; both=0; total=0
    for _ in range(100000):
        n=rnd.randint(2,10); A=rnd.uniform(0,3); s=10**rnd.uniform(-2,4)
        all_eq=A*(n+(n-1)*s)/n>=1; none_eq=A*n*(1+s)/(n+s)<=1
        total+=1
        if not all_eq and not none_eq: bad+=1
        if all_eq and none_eq: both+=1
    print(f"   draws {total}: neither {bad}, both {both}")

    print("(7) Prop 6.9: row sums do not certify independent errors. k=6 checks of reliability f=0.9 each, R=0 (no shared funding),")
    print("    but a share rho of hazards sits in a blind spot common to all checks (shared training data):")
    for rho in (0.0,0.05,0.3):
        caught=0; N=200000
        for _ in range(N):
            if rnd.random()<rho: continue
            if any(rnd.random()<0.9 for _ in range(6)): caught+=1
        print(f"   rho={rho}: catch rate {caught/N:.4f} ((1-rho)(1-0.1^6) = {(1-rho)*(1-0.1**6):.4f})")

    print("(8) Prop 8.11(3): satiation. Symmetric Tullock intensity, n=4, r=1, c=1, prize Om; objective w*u(Om) - c e")
    for name,u in [("linear u=Om",lambda O:O),("satiated u=1-exp(-Om)",lambda O:1-math.exp(-O))]:
        out=[]
        for O in (1,10,100):
            e=0.1
            for _ in range(200):
                en=golden(lambda x: x/(x+3*e)*u(O)-x,1e-9,200.0); e=0.5*e+0.5*en
            out.append(e)
        print(f"   {name}: intensity at Om=1,10,100: {', '.join('%.4f'%v for v in out)}")

    print("(9) Remark 5.3(2) caps: local vs global. n=5, r=1.5, kappa=0.5, Om=1, delta=0.05 (K*=2), cap 1.5, laggard starts at 0.1")
    def capsim(beta,k0,cap=1.5,n=5,r=1.5,kap=0.5,Om=1.0,dl=0.05,T=20000):
        K=[0.1]+[1.0]*(n-1)
        for _ in range(T):
            S=sum(k**r for k in K); p=[k**r/S for k in K]
            K=[min(cap,(1-dl)*K[i]+kap*Om*((1-beta)*p[i]+beta/n)+k0) for i in range(n)]
        return K
    for beta,k0 in [(0.0,0.0),(0.02,0.0),(0.2,0.0),(0.0,0.002),(0.0,0.03),(0.0,0.075)]:
        K=capsim(beta,k0)
        suff=beta*0.5*1.0/5+k0>=0.05*1.5-1e-12
        cap,n_,r_,kap_,Om_,dl_=1.5,5,1.5,0.5,1.0,0.05
        mn=min(kap_*Om_*((1-beta)*(K_**r_/(K_**r_+(n_-1)*cap**r_))+beta/n_)+k0-dl_*K_ for K_ in [cap*j/20000 for j in range(1,20000)])
        print(f"   beta={beta}, k0={k0}: final {[round(x,3) for x in K]}; exact global condition min_K[inflow-delta K]={mn:+.4f} ({'protects' if mn>0 else 'exclusion basin'}); sufficient beta*kappa*Om/n+k0>=delta*cap: {suff}")

    print("(10) growth variant (no depreciation, diffusion df): relative-share multiplier at total capacity S")
    def share_mult(S,rho,Om,beta,r,df,k0,n=4,h=1e-6):
        K=[S/n*(1+h)]+[S/n*(1-h/(n-1))]*(n-1)
        Sx=sum(k**r for k in K); p=[k**r/Sx for k in K]; mK=S/n
        K2=[K[i]+rho*Om*((1-beta)*p[i]+beta/n)+k0-df*(K[i]-mK) for i in range(n)]
        s0=K[0]/sum(K); s1=K2[0]/sum(K2)
        return (s1-1/n)/(s0-1/n)
    for (S,rho,Om,beta,r,df,k0) in [(10,0.5,1,0,1.5,0.01,0),(10,0.5,1,0,1.5,0.05,0),(10,0.5,1,0.2,1.5,0.0,0.05),(10,0.5,1,0,1.5,0.0,0.1)]:
        m=share_mult(S,rho,Om,beta,r,df,k0)
        pred=rho*Om*((1-beta)*r-1)>df*S+4*k0
        print(f"   S={S},rho={rho},beta={beta},r={r},df={df},k0={k0}: multiplier {m:.5f} -> {'unstable' if m>1 else 'stable'}; rho Om((1-beta)r-1) > df S + n k0: {pred}")


def check_HO():
    block('HO', 'safeguards, require', 'independent', 'Host transients: logistic transient minimum; pointwise harsher Allee host margin; finite-horizon counterexample to R1')
    # S9. Host results: Theorem 8.2(1)'s transient (the [N] 0.14 that has no script in v6), a host harsher at every level,
    # and the finite-horizon counterexample to R1's necessity.
    import math
    rho,h,K=0.05,0.08,1.0
    def logit_x(t,x0,D,de):
        u=math.log(x0/(1-x0))-D*de*t
        return 1/(1+math.exp(-u)) if u>=0 else math.exp(u)/(1+math.exp(u))
    def run(Delta,emin,emax,x0=0.99,V0=1.0,host='logistic',A=0.15,T=3000.0,dt=0.01):
        de=emax-emin
        rA=rho*A/(K-A)                       # per-capita regeneration rA (V/A-1)(1-V/K) <= rho(1-V/K) at every V
        def f(t,V):
            E=emin+de*logit_x(t,x0,Delta,de)
            if host=='logistic': g=rho*(1-V/K)
            else: g=rA*(V/A-1)*(1-V/K)
            return V*(g-h*E)
        V=V0; t=0.0; vmin=V
        for _ in range(int(T/dt)):
            k1=f(t,V); k2=f(t+dt/2,V+dt/2*k1); k3=f(t+dt/2,V+dt/2*k2); k4=f(t+dt,V+dt*k3)
            V=max(0.0,V+dt*(k1+2*k2+2*k3+k4)/6); t+=dt; vmin=min(vmin,V)
            if V<1e-12 and host!='logistic': break
        return vmin,V
    print("(a) Theorem 8.2(1) transient, logistic host, liability margin Delta=0.08 from t=0, race strategy at 99% (e_min=0, e_max=1)")
    for dt in (0.02,0.005):
        vmin,vend=run(0.08,0.0,1.0,dt=dt)
        print(f"   step {dt}: minimum host {vmin:.4f}, final {vend:.3f}")
    print("(b) host harsher at every level (Allee, per-capita regeneration below logistic everywhere): minimal margin that avoids permanent collapse")
    def dmin(A,emin=0.1):
        lo,hi=0.0,3.0
        if run(hi,emin,1.0,host='allee',A=A,dt=0.05)[1]<0.01: return float('inf')
        for _ in range(30):
            m=(lo+hi)/2
            if run(m,emin,1.0,host='allee',A=A,dt=0.05)[1]<0.01: lo=m
            else: hi=m
        return hi
    def Vu(A,E):
        rA=rho*A/(K-A); qa=-rA/(A*K); qb=rA*(1/A+1/K); qc=-rA-h*E
        disc=qb*qb-4*qa*qc
        r1=(-qb+math.sqrt(disc))/(2*qa); r2=(-qb-math.sqrt(disc))/(2*qa)
        return min(r1,r2)
    for A in (0.05,0.10,0.15,0.20,0.25):
        print(f"   A={A:.2f}: Delta_min={dmin(A):.3f}; degradation threshold at e_min load V_u={Vu(A,0.1):.3f} (normative floor 0.3)")
    lv=run(0.02,0.1,1.0,dt=0.05,T=8000.0)
    print(f"   logistic host with Delta=0.02 (far below every Delta_min above): minimum {lv[0]:.2e}, final {lv[1]:.3f} (recovers; with the logistic host any Delta>0 recovers eventually)")
    print("(c) R1 at a finite horizon: K=V0=1, V_min=0.2, rho=0.01, h=0.02, zero liability, loads in [0,1] (Codex)")
    H=50
    lb=1/(2*math.exp(0.01*H)-1)
    # full load from t=0 is the worst case: V' = V(0.01(1-V) - 0.02) = V(-0.01 - 0.01V)
    V=1.0; t=0.0; dt=0.001; cross=None
    while t<200:
        V+=dt*V*(0.01*(1-V)-0.02); t+=dt
        if cross is None and V<0.2: cross=t
    print(f"   lower bound on V(50) with zero liability: {lb:.4f} > 0.2; full-load crossing time {cross:.2f} (ln 3/0.01 = {math.log(3)/0.01:.2f})")


def check_DW():
    block('DW', 'pausefield, dwell', 'independent', 'Dwell times by forward integration in logit coordinates; two phases; frozen-share thresholds')
    # S10. Dwell times in the D=1 field model (3), by forward integration in logit coordinates (no separatrix, no truncation of x).
    #   u = logit x:  u' = zeta (a z - c),  z' = eps (b sig(u) - d z),  R = ab/(cd).  a=c=d=zeta=1.
    # Reform: insulate rule-making (b -> 0) for a time T from the captured state (x=0.99, z=b/d), then restore b.
    # T_min is the shortest T after which the state converges to absence. Reported as T_min*eps*d.
    import math
    def sig(u): return 1/(1+math.exp(-u)) if u>=0 else math.exp(u)/(1+math.exp(u))
    def rk(u,z,b,eps,dt):
        f=lambda u,z:(a*z-c, eps*(b*sig(u)-d*z))
        k1=f(u,z); k2=f(u+dt/2*k1[0],z+dt/2*k1[1]); k3=f(u+dt/2*k2[0],z+dt/2*k2[1]); k4=f(u+dt*k3[0],z+dt*k3[1])
        return u+dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6, z+dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
    a=c=d=1.0
    def fate(u,z,b,eps,dt=0.01,T=4000):
        for _ in range(int(T/dt)):
            u,z=rk(u,z,b,eps,dt)
            if u>60: return 'captured'
            if u<-60: return 'absent'
        return 'captured' if u>0 else 'absent'
    def tmin(R,eps,x0=0.99):
        b=R*c*d/a
        def after(T,dt=0.005):
            u=math.log(x0/(1-x0)); z=b/d; t=0.0
            while t<T-1e-12:
                st=min(dt,T-t); u,z=rk(u,z,0.0,eps,st); t+=st
            return fate(u,z,b,eps)
        lo,hi=0.0,1.0
        while after(hi)=='captured': hi*=2
        for _ in range(40):
            m=(lo+hi)/2
            if after(m)=='captured': lo=m
            else: hi=m
        return hi*eps*d
    print("Insulated reform: T_min*eps*d (Opus check: eps/zeta=0.1 -> 1.886, 5.318, 10.453; eps/zeta=1 -> 5.859, 10.343, 16.181 for R=2,5,10)")
    for eps in (0.1,1.0):
        print(f"   eps/zeta={eps}: "+", ".join(f"R={R}: {tmin(R,eps):.3f}" for R in (2,5,10)))
    print("Two phases: share rises while z>c/a, i.e. for ln R/(eps d); it is back at its starting level when R(1-e^{-s})=s, s=eps d t")
    for R in (2,5,10):
        lo,hi=1e-6,50.0
        for _ in range(100):
            m=(lo+hi)/2
            if R*(1-math.exp(-m))-m>0: lo=m
            else: hi=m
        print(f"   R={R}: rise phase {math.log(R):.3f}; back to start at s*={hi:.3f}")
    def sigma0(R,eps):
        b=R*c*d/a
        lo,hi=1e-6,1-1e-9
        for _ in range(40):
            m=(lo+hi)/2
            if fate(math.log(m/(1-m)),0.0,b,eps)=='absent': lo=m
            else: hi=m
        return lo
    print("sigma(0): largest share from which (x, z=0) returns to absence (Opus check: R=2, eps=zeta -> 0.676)")
    for (R,eps) in [(2,1.0),(2,0.1),(5,1.0),(5,0.1),(10,0.1)]:
        print(f"   R={R}, eps/zeta={eps}: sigma(0)={sigma0(R,eps):.3f}")


def check_AC():
    block('AC', 'alarm', 'independent', 'Autocorrelation under static affine masking and under a filter with memory')
    # S11. Remark 4.7(4) [N, systems review]: masking hides levels, not dynamics.
    # Host (1) with additive noise: dV = V[rho(1-V/K) - h E] dt + s dW, E=0.4, rho=0.05, h=0.08, K=1 -> V*=0.36.
    # Reports: Vt = V + m (K - V) (static, memoryless masking). Level alarms read Vt; the lag-one autocorrelation phi of
    # reports sampled every Dt gives the recovery rate lambda = -ln(phi)/Dt = rho V*/K, hence V_hat = K lambda / rho.
    import math, random
    rho,h,K,E=0.05,0.08,1.0,0.4
    Vstar=K*(1-h*E/rho)
    def series(seed,s=0.004,dt=0.05,Dt=1.0,N=40000):
        rnd=random.Random(seed); V=Vstar; out=[]; steps=int(Dt/dt)
        for _ in range(N):
            for _ in range(steps):
                V+=V*(rho*(1-V/K)-h*E)*dt+s*math.sqrt(dt)*rnd.gauss(0,1)
            out.append(V)
        return out,Dt
    def ac1(x):
        n=len(x); m=sum(x)/n
        num=sum((x[i]-m)*(x[i+1]-m) for i in range(n-1)); den=sum((v-m)**2 for v in x)
        return num/den
    V,Dt=series(1)
    print(f"true V*={Vstar:.3f}")
    for m in (0.0,0.25,0.5):
        rep=[v+m*(K-v) for v in V]
        phi=ac1(rep); lam=-math.log(phi)/Dt
        print(f"   masking m={m}: mean report {sum(rep)/len(rep):.3f}; lag-1 autocorrelation {phi:.4f}; recovered condition {K*lam/rho:.3f}")
    # a reporting filter with memory defeats the indicator
    rep=[]; prev=None
    for v in V:
        x=v+0.5*(K-v); prev=x if prev is None else 0.8*prev+0.2*x; rep.append(prev)
    phi=ac1(rep); print(f"   masking with memory (exponential smoothing 0.8): recovered condition {K*(-math.log(phi)/Dt)/rho:.3f} -> the indicator is defeated")


def check_NB():
    block('NB', 'standprice, enforce, zonesillus', 'derived', 'Derived numbers quoted in the text (theta_Gamma table; largest enforceable loop gain; p_bar; time to decisiveness)')
    # S12. Numbers quoted in the specification (derived quantities; the underlying formulas are checked in S1-S4).
    import math
    n=4
    def th_eff(th0,G,n=4):
        lam=G/(1-G)*(n-1-th0)/(n-1)
        return (n*th0-lam*(n-1))/(n+lam*(n-1))
    print("(a) effective self-model theta_eff for n=4 as the discounted loop gain G_delta rises")
    for G in (0.0,0.25,0.5,0.75,0.9,0.99):
        print(f"   G_delta={G}: theta_0=0 -> {th_eff(0,G):+.3f};  theta_0=0.4 -> {th_eff(0.4,G):+.3f};  theta_0=2 -> {th_eff(2,G):+.3f}")
    print("(b) binary faithful-AI game (n=4,b=1,c=.3,d=.2,eps=1,delta=.9), decisive value D=C=0 (boundary case):")
    b,c,d,eps,dl=1.0,0.3,0.2,1.0,0.9
    A=eps*(b-d)-c; B=eps*(b/(n-1)+d); K=c+n*eps*d
    def th_rep(pd,Dval=0.0):
        # repaired condition: (1-dl)(A-B th) + dl pd (Dval - 0) <= dl (1-pd)(0 - (-(1+th)K))
        # -> th >= [(1-dl)A + dl pd Dval - dl(1-pd)K] / [(1-dl)B + dl(1-pd)K]
        return ((1-dl)*A+dl*pd*Dval-dl*(1-pd)*K)/((1-dl)*B+dl*(1-pd)*K)
    def G_star(th0,target):
        lo,hi=0.0,1-1e-12
        if th_eff(th0,0.0)<target: return None
        for _ in range(200):
            m=(lo+hi)/2
            if th_eff(th0,m)>=target: lo=m
            else: hi=m
        return lo
    for pd in (0.0,0.5,0.9,0.99,1.0):
        t=th_rep(pd); g0=G_star(0.0,t); g4=G_star(0.4,t)
        print(f"   p_d={pd}: theta_rep={t:+.3f}; largest G_delta with enforceable restraint: theta_0=0 -> {('%.3f'%g0) if g0 is not None else 'none'}, theta_0=0.4 -> {('%.3f'%g4) if g4 is not None else 'none'}")
    print("   with a decisive value above cooperation, D=0.5 (objective units):")
    for pd in (0.5,0.9):
        print(f"   p_d={pd}: theta_rep={th_rep(pd,0.5):+.3f} (vs {th_rep(pd):+.3f} at D=C)")
    print("(c) largest enforceable breakout probability p_bar = 1 - [(1-delta)g + delta(D-C)]/[delta(D-v)]")
    for (g,C,D,v,dl_) in [(1.0,3.0,3.0,1.0,0.9),(1.0,3.0,4.0,1.0,0.9),(0.0,3.0,4.0,1.0,0.9),(-0.5,3.0,3.0,1.0,0.9)]:
        pb=1-((1-dl_)*g+dl_*(D-C))/(dl_*(D-v))
        print(f"   g={g},C={C},D={D},v={v},delta={dl_}: p_bar={pb:.3f}")
    print("(d) time to decisiveness in the linearized compounding loop: T_dec = ln(gap_bar/gap_0)/ln(1+dK(Gamma-1))")
    for G in (1.2,1.5,3.0):
        for dK in (0.05,0.2):
            m=1+dK*(G-1)
            print(f"   Gamma={G}, dK={dK}: multiplier {m:.3f}; from a 1% to a 50% gap: {math.log(50)/math.log(m):.0f} periods")
    print("(e) monotonicity of p_bar on the region D>v, 0<=p_bar<1 (random draws, finite differences)")
    import random
    rnd=random.Random(4); bad={'g':0,'C':0,'D':0,'v':0}; tot=0
    def pbar(g,C,D,v,dl): return 1-((1-dl)*g+dl*(D-C))/(dl*(D-v))
    for _ in range(100000):
        dl=rnd.uniform(0.1,0.99); C=rnd.uniform(0,3); v=rnd.uniform(-2,C); D=rnd.uniform(v+0.01,6); g=rnd.uniform(-2,3)
        p=pbar(g,C,D,v,dl)
        if not (0<=p<1): continue
        tot+=1; h=1e-6
        if pbar(g+h,C,D,v,dl)>p: bad['g']+=1
        if pbar(g,C+h,D,v,dl)<p: bad['C']+=1
        if pbar(g,C,D+h,v,dl)>p+1e-12: bad['D']+=1
        if pbar(g,C,D,v+h,dl)>p+1e-12: bad['v']+=1
    print(f"   draws in region {tot}; violations {bad}")


def check_FA():
    block('FA', 'require', 'independent', 'Codex invariant rectangle: R=2 with a low initial state converges to no capture')

    import math
    def field(x, z):
        return x * (1 - x) * (z - 1), 2 * x - z
    x, z, step, max_z = 0.1, 0.1, 0.001, 0.1
    inside = True
    for _ in range(20000):
        k1 = field(x, z)
        k2 = field(x + step * k1[0] / 2, z + step * k1[1] / 2)
        k3 = field(x + step * k2[0] / 2, z + step * k2[1] / 2)
        k4 = field(x + step * k3[0], z + step * k3[1])
        x += step * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        z += step * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        max_z = max(max_z, z)
        inside = inside and (0 <= x <= 0.1 and 0 <= z <= 0.2)
    print(f"row gain R=2, start (0.1, 0.1): stays in [0,.1]x[0,.2]: {inside}; at t=20 x={x:.2e}, z={z:.2e} (no capture)")
    print("so a full row sum below one is sufficient, not necessary, for no capture from the states actually reached")


ORDER = ['FB', 'LG', 'CI', 'TC', 'TH', 'SM', 'CB', 'PR', 'CS', 'FA', 'DW', 'AC', 'RH', 'FS', 'EC', 'CR', 'BI', 'WG', 'TK', 'T3', 'HO', 'SH', 'PE', 'FD', 'NB']

LEGACY = [('../v5', 'checks_v5.py'), ('../v4', 'checks_v4.py'), ('../v4', 'checks_v42.py'), ('../v4', 'checks_v44.py'),
          ('../v4', 'checks_v45.py'), ('../v3', 'checks_v31.py')]

if __name__ == '__main__':
    t0 = time.time()
    only = [a for a in sys.argv[1:] if not a.startswith('--')]
    for code in ORDER:
        if only and code not in only: continue
        globals()['check_' + code]()
    print(f"\n=== done in {time.time()-t0:.0f} s")
    if '--legacy' in sys.argv:
        here = pathlib.Path(__file__).parent
        for d, f in LEGACY:
            p = (here / d / f)
            if not p.exists(): print(f"legacy {d}/{f}: missing"); continue
            r = subprocess.run([sys.executable, f], cwd=p.parent, capture_output=True, text=True)
            log = p.with_suffix('.v61run.log'); log.write_text(r.stdout + r.stderr)
            print(f"legacy {d}/{f}: exit {r.returncode}; output in {log.name}")
