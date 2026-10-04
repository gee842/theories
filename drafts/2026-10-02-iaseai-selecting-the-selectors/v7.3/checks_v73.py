"""Numerical checks for Theory V7.3. Pure Python, standard library only. Run:
    python3 checks_v73.py > checks_v73.log        (default sizes; see the timing line at the end of the log)
    python3 checks_v73.py --full > checks_v73_full.log
                                                  (adds the heavy grids, all in MP and QS: the Markov-perfect
                                                   multiplicity at N=6000 and a finer-round smooth branch, the
                                                   full s2_mpe/s2b/s2d tables, s2c_profile and s2e_check, the
                                                   full prop39 grid in SP(J), and the replicator-with-mutation
                                                   capacity dynamics of s4_cost(c) in QS. Every other ported
                                                   script runs at its source's own size by default, including the
                                                   20,000-game explicit-action sweep in ES)
    python3 checks_v73.py SP PD ...               (only the named blocks)

Every block is named by a two-letter code and lists the stable keys of the results it checks (SUPPLEMENT S15
maps keys to displayed numbers). Kinds:
  independent  the outcome is decided by direct computation (value iteration, simulation, numerical best
               response, numerical Jacobian), never by the inequality being tested;
  identity     an algebraic identity or a threshold formula evaluated against its own statement; it guards
               against slips, it is not independent evidence. A *valuation check* is an identity of a
               particular kind: it computes the discounted values of a fixed play path directly and compares
               them with an inequality that is the same comparison rearranged (EC); it checks the valuation,
               not the incentives (those are checked in ES);
  derived      numbers computed from formulas that other blocks check.
A block whose parts differ in kind says so in its header (for example LG: (A),(A'),(B) independent; (C),(C')
identity). Blocks added in v6.2 assert the relations the text will claim, with stated tolerances; each assertion
prints one line beginning "  [ok]" or "  [FAIL]", and the run ends with a count. A failed assertion is a finding to
record in verification notes, never a reason to loosen the tolerance silently. The v6.1 blocks keep their
printed output; their kind labels follow the review round (EC valuation check; LG(C),(C') and RH identities).

Sources of the v6.2 blocks (ported, not rewritten; the notes file maps every script to its block):
  ../v6.2/planning/math-fable/f1-f7, ../v6.2/planning/math-opus/m01-m10, ../v6.1/reviews/counterexamples_v61_codex.py and
  ../v6.1/reviews/scripts-v6.1-{math-fable,math-opus,systems,alignment,adv-fable,adv-opus}/*.py; the unit drafts'
  scripts planning/drafts/U05/{A/checks/jx_joint_scissors.py,B/scripts/jx_joint.py} (JX), U06/B/checks/dl_nearlock.py
  (DL(e)) and U11/A/checks/tr_transition.py (TR); ../v5/checks_v5.py HO's two-root example (SM(15)). Checks written for
  results the merges added: SM(16) thrrep, CI(k) unravel across types, and QS's S4.2(2)(b),(c) and capture-lag lines.
Print-only output. Fourteen v6.1 blocks (FB before its v6.2 assertion was added, TC, TH, CB, RH, FS, BI, WG, PE, FD, LG,
T3, AC, FA) print comparisons that no expect() gates; their printed lines are diagnostics to read, not a regression gate,
and only the counted assertions affect the exit status (outside review of V6.2, I1). Block CX holds the counterexamples
of that review.
Results carried unchanged from v5.2 and earlier keep their suites (../v5/checks_v5.py, ../v4/, ../v3/); run
    python3 checks_v73.py --legacy
to re-run those suites as well. No suite certifies every proof, and none supplies evidence about the world.
"""
import itertools, math, random, statistics, sys, subprocess, pathlib, time

FULL = '--full' in sys.argv
_ASSERT = {'ok': 0, 'fail': []}
_CURRENT = {'block': None}

def block(name, keys, kind, title):
    _CURRENT['block'] = name
    print(f"\n=== {name} [{kind}] keys: {keys}\n    {title}", flush=True)

def expect(cond, label):
    """Assert a claimed relation; print one line; record failures (they are findings, see the notes file)."""
    if cond:
        _ASSERT['ok'] += 1; print(f"  [ok] {label}", flush=True)
    else:
        _ASSERT['fail'].append(f"{_CURRENT['block']}: {label}"); print(f"  [FAIL] {label}", flush=True)

def close(a, b, rel=1e-6, abs_=0.0):
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b), 1e-300))

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
    expect(agree == N, "bench: the criterion agrees with the spectral radius in every sampled case")

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
    # v6.2 relabel (Math-Fable minor 9; Math-Opus M6; SYNTHESIS H): sym_eq assigns the closed-form intensity at every
    # iteration, so "h direct" equals "formula" by construction: an identity. Only the final line (best response of
    # one carrier on a grid of 3,000 intensities against the others at the symmetric level) is an independent check.
    block('RH', 'racehazard', 'identity; the last line (grid best response) independent',
          'Race-generated hazard: closed form against itself (identity); symmetric intensity against a grid best response')
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
        print(f"n={n}, r={r}, Om={Om}, theta={th}: h direct {h_direct:.6f}, formula {h_formula:.6f}  [identity: sym_eq assigns the closed form]")
    # numerical best-response check of the symmetric intensity
    def obj(i, es, n, r, Om, c, L, th):
        S = sum(x ** r for x in es)
        pis = [Om * (es[k] ** r / S) - c * es[k] - L * sum(es) for k in range(n)]
        return pis[i] + th * (sum(pis) - pis[i]) / (n - 1)
    n, r, Om, c, L, th = 4, 1, 1, 1, 0.3, 0.4
    e = sym_eq(n, r, Om, c, L, th)
    best = max((obj(0, [x] + [e] * (n - 1), n, r, Om, c, L, th), x) for x in [e * k / 1000 for k in range(1, 3001)])
    print(f"symmetric intensity {e:.5f}; best response on a grid {best[1]:.5f}  [independent]")

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
    block('EC', 'enforce', 'identity: valuation check',
          'Valuation check of (14): discounted values of the fixed deviation path in an explicit Markov chain; old bound by sign of D-C; breakouts during punishment')
    # v6.2 relabel (Math-Opus M6, SYNTHESIS H, Codex): V_coop >= V_dev is (14) multiplied by (1-delta) and rearranged,
    # and the only computed object is the punishment value V_P (the closed form (5)), so S1a agrees with (14) by algebra
    # (exact rationals: ES(g) and ../v6.1/reviews/scripts-v6.1-math-opus/s3_enforce.py (1)). It checks the valuation
    # of a fixed play path, not the incentives: the punisher's incentive, multi-period deviation plans and the link
    # between p_d and q are checked by best response over plans in block ES. Core wording: "a valuation check confirms
    # the algebra of (1)", not "agrees in all of 200,000 random settings".
    # S1. Enforcement condition replacing Proposition 5.7, computed by direct evaluation of discounted payoffs
    # in an explicit Markov chain (value iteration over states).
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
    print("=== S1a. [valuation check] repaired condition vs direct discounted values (value iteration), random draws:",N)
    print(f"mismatches {mis}; exact ties skipped {boundary}")
    print("=== S1b. old printed bound (no D-C term) vs truth, by sign of D-C: [cases, old-says-sustain-but-deviation-pays, sustainable-but-old-says-no]")
    for k_,v_ in cnt.items(): print(" ",k_,v_)

    print("=== S1c. Monte Carlo cross-check of the deviation value (independent sampler)")
    for (C,g,D,U,P,pd,q,dl) in [(3,1,2,0,1,1.0,0.1,0.9),(3,1,3,0,1,0.5,0.0,0.9),(1,0.3,2,-1,0,0.2,0.2,0.8)]:
        Vc,Vd,Vp=values(C,g,D,U,P,pd,q,dl)
        mc=monte_carlo(C,g,D,U,P,pd,q,dl,N=4000,T=300)
        print(f"  C={C},g={g},D={D},U={U},P={P},pd={pd},q={q},delta={dl}: Vcoop={Vc:.3f}  Vdev(VI)={Vd:.3f}  Vdev(MC)={mc:.3f}")
    # v6.2 (port of ../v6.1/reviews/scripts-v6.1-math-opus/s6_ec_mc.py): the second case's 22.414 against the exact 22.000
    # is z ~ +2.9 at seed 0; over five seeds the standard error is 0.142 and |z| < 1.1, so the gap is sampling noise.
    C,g,D,U,P,pd,q,dl=3,1,3,0,1,0.5,0.0,0.9
    Vexact=(C+g)+dl*(pd*D/(1-dl)+(1-pd)*P/(1-dl)); zs=[]
    for seed in range(5):
        rnd_=random.Random(seed); Nmc=4000; tot=0.0; sq=0.0
        for _ in range(Nmc):
            s=C+g; s+=dl*(D/(1-dl) if rnd_.random()<pd else P/(1-dl)); tot+=s; sq+=s*s
        m=tot/Nmc; sd=math.sqrt(sq/Nmc-m*m); zs.append((m-Vexact)/(sd/math.sqrt(Nmc)))
        print(f"  S1c' case 2 by a one-step sampler, seed {seed}: mean {m:.3f} (exact {Vexact:.3f}), SE {sd/math.sqrt(Nmc):.3f}, z={zs[-1]:+.2f}")
    expect(max(abs(z) for z in zs) < 3.0, "S1c Monte Carlo gaps are sampling noise (|z| < 3 over five seeds)")

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
    block('LG', 'loopgain, compound, standprice', "independent; (C),(C') identity",
          'One loop gain: numerical Jacobian vs Gamma; nonlinear deviations; present value of standing; two-period contest vs e(theta_Gamma)')
    # v6.2 relabel (Math-Opus M6): in (C) and (C') lambda is the two-period model's own second-period derivative
    # delta*Om2*r2*kap/(n*Kbar), not Gamma_delta/(1-Gamma_delta), and the symmetric equilibrium's first-order condition
    # involves only first derivatives at the symmetric point, so the agreement is by construction: an identity that
    # checks the lambda <-> theta map of Proposition 3.5(3), not the dynamic content of Proposition 3.9. Core wording:
    # "an algebraic check", not "to six digits". The dynamic content is checked in (B) here and in SP, PD and MP.
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
    print("(C) [identity: first order by construction at the symmetric point] two-period contest (first-period payoffs become second-period capacity): direct equilibrium vs e(theta_eff)")
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
    print("(C') [identity] held self-model theta0: direct equilibrium vs e(theta_eff), lambda' = lambda (n-1-theta0)/(n-1)")
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

    print("(c) rate law with gam(t)=e^{-g t}, d(t)=d0 e^{alpha t}, dominant carrier share 0.6 (A=0.3, aE*sum_j bhat_ev,j*ybar_j=1, so aE*Bhat=p=0.6; cE=1, d0=2, g=0.2, eta=1, f=0)")
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
    for th0 in (0.0,0.4):
        lo_,hi_=0.0,1.0
        for _ in range(60):
            m_=(lo_+hi_)/2
            if th0>=th_rep(m_): lo_=m_
            else: hi_=m_
        print(f"   v6.2: no G_delta>=0 sustains restraint above p_d={lo_:.4f} for theta_0={th0} (v6.1 wrote 0.99; JX recomputes this by direct valuation)")
        expect(abs(lo_-(0.9495 if th0==0 else 0.9793))<5e-4, f"derived threshold for theta_0={th0}: {lo_:.4f}")
    print("   with a decisive value above cooperation, D=0.5 (objective units):")
    for pd in (0.5,0.9):
        print(f"   p_d={pd}: theta_rep={th_rep(pd,0.5):+.3f} (vs {th_rep(pd):+.3f} at D=C)")
    print("(c) largest enforceable breakout probability p_bar = 1 - [(1-delta)g + delta(D-C)]/[delta(D-v)]")
    for (g,C,D,v,dl_) in [(1.0,3.0,3.0,1.0,0.9),(1.0,3.0,4.0,1.0,0.9),(0.0,3.0,4.0,1.0,0.9),(-0.5,3.0,3.0,1.0,0.9)]:
        pb=1-((1-dl_)*g+dl_*(D-C))/(dl_*(D-v))
        print(f"   g={g},C={C},D={D},v={v},delta={dl_}: p_bar={pb:.3f}")
    print("(d) time to decisiveness in the linearized compounding loop: T_dec = ln(gap_bar/gap_0)/ln(1+(dK+df)(Gamma-1)), here df=0 (v6.1 omitted df; TD checks the general form)")
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


# =====================================================================================================================
# v6.2 blocks. Each ports one or more memo or reviewer scripts (named in its comment); the code is the source script's,
# with its cases kept, wrapped in a function and given assertions. Sizes marked "default" can be raised with --full.
# =====================================================================================================================

def _golden_max(f, lo, hi, it=160):
    g = (math.sqrt(5) - 1) / 2
    x1 = hi - g * (hi - lo); x2 = lo + g * (hi - lo); f1 = f(x1); f2 = f(x2)
    for _ in range(it):
        if f1 < f2:
            lo = x1; x1 = x2; f1 = f2; x2 = lo + g * (hi - lo); f2 = f(x2)
        else:
            hi = x2; x2 = x1; f2 = f1; x1 = hi - g * (hi - lo); f1 = f(x1)
    return (lo + hi) / 2


def check_SP():
    block('SP', 'standprice, twoerrors, growprize (S3), twochan',
          'independent: (B),(C),(D),(F),(G); identity: (A),(E) (first order by construction at a symmetric point)',
          'Compounding prices standing, general form: relative against common return; growing prize, two-period and infinite horizon')
    # Sources: planning/math-fable/f1_standprice.py (A,B,D); planning/math-opus/m02_standprice_general.py (A,B,C,E);
    # ../v6.1/reviews/scripts-v6.1-adv-fable/prop39_growing_prize.py; scripts-v6.1-adv-opus/adv_checks.py section 2;
    # ../v6.1/reviews/counterexamples_v61_codex.py case 9.
    # Claims (D2-fable s2, D2-opus s7): (1+theta)/(n-1-theta) = (1+theta0)/(n-1-theta0) (1+lam_com)/(1+lam_rel)
    #   = (1+theta0)/(n-1-theta0) (1-Grel_d)/(1-Gcom_d); narrowing iff lam_rel > lam_com; fixed prize: lam_com = 0;
    #   prize proportional to capacity without diffusion: lam_rel/lam_com = (1-beta) r at every horizon.

    # ---------------- (A) f1(A): two-period contest, general prize, sharing in period 2 [identity]
    def two_period(n, r, W1, c, l, th0, delta, kappa, K0, Om20, g, beta, gross=False):
        def objective(i, e):
            S = sum(x ** r for x in e); p = [x ** r / S for x in e]; tot = sum(e)
            pi = [W1 * p[k] - c * e[k] - l * tot for k in range(n)]
            if gross:
                K = [K0 + kappa * W1 * p[k] for k in range(n)]
            else:
                K = [K0 + kappa * pi[k] for k in range(n)]
            if min(K) <= 0: return -1e9
            Om2 = Om20 + g * sum(K)
            SK = sum(x ** r for x in K)
            w2 = [Om2 * ((1 - beta) * x ** r / SK + beta / n) for x in K]
            J1 = pi[i] + th0 * (sum(pi) - pi[i]) / (n - 1)
            J2 = w2[i] + th0 * (sum(w2) - w2[i]) / (n - 1)
            return J1 + delta * J2
        e = 0.2
        for _ in range(400):
            br = _golden_max(lambda x: objective(0, [x] + [e] * (n - 1)), 1e-7, 2.0)
            en = 0.5 * e + 0.5 * br
            if abs(en - e) < 1e-13: e = en; break
            e = en
        A = r * W1; B = e * n * n
        th_eff = (A * (n - 1) - B * (c + l)) / (A + B * l)
        pi_bar = W1 / n - c * e - l * n * e
        K = K0 + kappa * (W1 / n if gross else pi_bar)
        Om2 = Om20 + g * n * K
        lam_rel = delta * kappa * (1 - beta) * r * Om2 / (n * K); lam_com = delta * kappa * g
        R0 = (1 + th0) / (n - 1 - th0)
        R = R0 * (1 + lam_com) / (1 + lam_rel)
        th_pred = (R * (n - 1) - 1) / (1 + R)
        return e, th_eff, th_pred, lam_rel, lam_com
    print("(A) [identity] f1(A): two-period contest, prize Om20 + g sum K with sharing beta in period 2; theta_eff read off e* vs (9) general")
    W1, c, l, delta, kappa, K0 = 1.0, 1.0, 0.3, 0.95, 1.0, 1.0
    worst = 0.0; sign_ok = 0; sign_n = 0
    for (nn, r, th0, Om20, g, beta) in [(4, 0.8, 0.0, 1.0, 0.0, 0.0), (4, 0.8, 0.0, 1.0, 1.0, 0.0), (4, 1.2, 0.0, 1.0, 2.0, 0.0),
                                    (4, 1.0, 1.0, 1.0, 0.5, 0.0), (4, 1.3, 0.5, 0.0, 1.0, 0.0), (4, 1.3, 0.5, 0.0, 1.0, 0.3),
                                    (4, 1.25, 0.5, 0.0, 2.0, 0.2), (4, 0.7, 0.5, 0.0, 3.0, 0.0), (4, 1.0, 0.5, 0.0, 3.0, 0.0),
                                    (4, 1.2, -0.5, 0.5, 0.5, 0.6), (4, 1.3, 1.9, 0.0, 1.0, 0.0), (2, 1.8, 0.0, 0.0, 1.0, 0.2),
                                    (2, 1.8, 0.0, 0.0, 1.0, 0.5), (2, 1.6, 0.3, 0.0, 0.5, 0.0)]:
        n = nn
        e, th, thp, lr, lc = two_period(n, r, W1, c, l, th0, delta, kappa, K0, Om20, g, beta)
        worst = max(worst, abs(th - thp))
        narrower = th < th0 - 1e-6; pred = lr > lc + 1e-9
        sign_n += 1; sign_ok += (narrower == pred) or abs(th - th0) < 1e-6
        tag = ""
        if Om20 == 0: tag = f"  [(1-beta) r = {(1-beta)*r:.2f}: predicts {'narrower' if (1-beta)*r>1+1e-9 else ('same' if abs((1-beta)*r-1)<1e-9 else 'wider')}]"
        print(f"   n={n} r={r} th0={th0:+.1f} Om20={Om20} g={g} beta={beta}: e*={e:.6f} theta_eff={th:+.5f} formula={thp:+.5f} "
              f"lam_rel={lr:.3f} lam_com={lc:.3f} -> {'narrower' if narrower else 'not narrower'}{tag}")
    print(f"   max |theta_eff - formula| = {worst:.1e}; sign rule held in {sign_ok}/{sign_n} cases")
    expect(worst < 1e-6, f"f1(A): theta_eff equals the general form (9) in 14 cases (max error {worst:.1e} < 1e-6)")
    expect(sign_ok == sign_n == 14, "f1(A): narrower iff lam_rel > lam_com in 14/14, ties at (1-beta) r = 1")

    # ---------------- (B) f1(B): infinite horizon, prize proportional to capacity, no depreciation [independent]
    print("(B) [independent] f1(B): infinite horizon, prize Omega_t = g S_t, no depreciation: PV(relative unit)/PV(common unit) by simulation")
    n, g, kappa, delta = 3, 0.05, 1.0, 0.9
    okB = True
    for (r, beta) in [(1.5, 0.0), (0.8, 0.0), (1.5, 0.5), (1.0, 0.0), (2.0, 0.3), (1.2, 0.2)]:
        if delta * (1 + max(g, (1 - beta) * r * g)) >= 1: continue
        def run(K, T=4000, r=r, beta=beta):
            Ks = list(K); out = []
            for t in range(T):
                S = sum(Ks); Om = g * S
                P = sum(x ** r for x in Ks); p = [x ** r / P for x in Ks]
                W = [Om * ((1 - beta) * p[i] + beta / n) for i in range(n)]
                out.append(W[0])
                Ks = [Ks[i] + kappa * W[i] for i in range(n)]
            return out
        K0_ = 1.0; eps = 1e-6
        base = run([K0_] * n)
        rel = run([K0_ + eps] + [K0_ - eps / (n - 1)] * (n - 1))
        com = run([K0_ + eps] * n)
        pv_rel = sum(delta ** (t + 1) * (rel[t] - base[t]) for t in range(len(base)))
        pv_com = sum(delta ** (t + 1) * (com[t] - base[t]) for t in range(len(base)))
        ratio = pv_rel / pv_com
        pred = (1 - beta) * r * (1 - delta * (1 + g)) / (1 - delta * (1 + (1 - beta) * r * g))
        okB &= abs(ratio - pred) < 1e-4 and ((ratio > 1 + 1e-6) == ((1 - beta) * r > 1 + 1e-9))
        print(f"   r={r} beta={beta}: PV_rel/PV_com = {ratio:.5f}, predicted {pred:.5f}; (1-beta) r = {(1-beta)*r:.2f}")
    expect(okB, "f1(B): PV ratio equals (1-beta)r(1-delta(1+g))/(1-delta(1+(1-beta)rg)) to 1e-4 and exceeds one iff (1-beta)r > 1")

    # ---------------- (C) m02(A): prices of a relative and a common unit, nonlinear simulation [independent]
    def simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, bump, T=4000):
        X = [x + b for x, b in zip(X0, bump)]
        pv = 0.0; disc = 1.0
        for t in range(1, T + 1):
            S = sum(X); Om = Om_fun(S)
            w = [x ** r for x in X]; W = sum(w)
            p = [wi / W for wi in w]
            win0 = Om * ((1 - beta) * p[0] + beta / n)
            disc *= delta
            pv += disc * win0
            mean = S / n
            X = [(1 - d) * x + kap * Om * ((1 - beta) * pi + beta / n) + k0 - df * (x - mean) for x, pi in zip(X, p)]
        return pv
    def steady(n, kap, d, k0, Om0, g):
        return (kap * Om0 + n * k0) / (d - kap * g)
    print("(C) [independent] m02(A): prices of a relative and a common unit, nonlinear simulation vs Grel_d/(1-Grel_d), Gcom_d/(1-Gcom_d)")
    cases = [(2, 1.5, 0.5, 0.2, 0.0, 0.1, 0.0, 1.0, 0.0, 0.9), (2, 1.5, 0.5, 0.2, 0.0, 0.1, 0.0, 1.0, 0.2, 0.9),
             (3, 1.2, 0.4, 0.15, 0.05, 0.05, 0.2, 2.0, 0.15, 0.95), (4, 0.8, 0.6, 0.1, 0.02, 0.0, 0.1, 1.0, 0.1, 0.9),
             (5, 2.0, 0.3, 0.25, 0.1, 0.2, 0.0, 3.0, 0.5, 0.85)]
    worst = 0.0
    for (n, r, kap, d, df, k0, beta, Om0, g, delta) in cases:
        Om_fun = lambda S, Om0=Om0, g=g: Om0 + g * S
        S = steady(n, kap, d, k0, Om0, g); X0 = [S / n] * n; Om = Om_fun(S)
        a = (1 - beta) * r * kap * Om / S
        Grel = delta * a / (1 - delta * (1 - d - df)); Gcom = delta * kap * g / (1 - delta * (1 - d))
        lam_rel = Grel / (1 - Grel); lam_com = Gcom / (1 - Gcom)
        y = 1e-5 * S / n
        up = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [kap * y] + [-kap * y / (n - 1)] * (n - 1))
        dn = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [-kap * y] + [kap * y / (n - 1)] * (n - 1))
        sim_rel = (up - dn) / (2 * y)
        up = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [kap * y] * n)
        dn = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [-kap * y] * n)
        sim_com = (up - dn) / (2 * y)
        worst = max(worst, abs(sim_rel / lam_rel - 1), abs(sim_com - lam_com) / lam_com if lam_com > 0 else abs(sim_com))
        print(f"   n={n} r={r} kap={kap} d={d} df={df} k0={k0} beta={beta} Om=({Om0}+{g}S) delta={delta}: Grel_d={Grel:.4f} Gcom_d={Gcom:.4f} | "
              f"relative: sim {sim_rel:.6f} formula {lam_rel:.6f} | common: sim {sim_com:.6f} formula {lam_com:.6f}")
    outside = None
    for (n, r, kap, d, df, beta, g, delta) in [(2, 1.5, 0.5, 0.1, 0.0, 0.0, 0.3, 0.9), (3, 0.8, 0.5, 0.1, 0.0, 0.0, 0.3, 0.9),
                                              (3, 1.3, 0.5, 0.1, 0.05, 0.1, 0.3, 0.88)]:
        Om_fun = lambda S, g=g: g * S
        X0 = [1.0] * n
        a = (1 - beta) * r * kap * g
        Grel = delta * a / (1 - delta * (1 - d - df)); Gcom = delta * kap * g / (1 - delta * (1 - d))
        lam_rel = Grel / (1 - Grel); lam_com = Gcom / (1 - Gcom)
        y = 1e-6
        up = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [kap * y] + [-kap * y / (n - 1)] * (n - 1), T=3000)
        dn = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [-kap * y] + [kap * y / (n - 1)] * (n - 1), T=3000)
        sim_rel = (up - dn) / (2 * y)
        up = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [kap * y] * n, T=3000)
        dn = simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [-kap * y] * n, T=3000)
        sim_com = (up - dn) / (2 * y)
        if Grel < 1: worst = max(worst, abs(sim_rel / lam_rel - 1), abs(sim_com / lam_com - 1))
        else: outside = (sim_rel, lam_rel)
        print(("   OUTSIDE THE DOMAIN (Grel_d>=1): " if Grel >= 1 else "   ") + f"balanced growth n={n} r={r} df={df} beta={beta} Om={g}S (growth {1-d+kap*g:.3f}/period): "
              f"Grel_d={Grel:.4f} Gcom_d={Gcom:.4f} | relative: sim {sim_rel:.6f} formula {lam_rel:.6f} | common: sim {sim_com:.6f} formula {lam_com:.6f}")
    print(f"   largest relative error inside the domain {worst:.1e}")
    expect(worst < 1e-4, f"m02(A): both closed-loop prices match the nonlinear simulation inside the domain (max rel. error {worst:.1e} < 1e-4)")
    expect(outside is not None and outside[0] > 0 > outside[1], "m02(A): outside the domain (Grel_d=1.066) the simulated price is positive and large while the formula is negative")

    # ---------------- (D) f1(D): gross winnings only (premise 'reinvests net payoff' is load-bearing) [identity-type, numerical]
    print("(D) f1(D): if only GROSS winnings convert, theta_eff read from e* differs from the net-payoff formula")
    gd_ok = True
    for (r, th0) in [(1.0, 0.0), (1.2, 0.5)]:
        e_net, th_net, thp, lr, lc = two_period(4, r, 1.0, 1.0, 0.3, th0, 0.95, 1.0, 1.0, 1.0, 0.0, 0.0, gross=False)
        e_gr, th_gr, thp2, lr2, lc2 = two_period(4, r, 1.0, 1.0, 0.3, th0, 0.95, 1.0, 1.0, 1.0, 0.0, 0.0, gross=True)
        gd_ok &= th_gr < th_net - 0.05
        print(f"   r={r} th0={th0}: net payoff reinvested: theta_eff={th_net:+.4f} (formula {thp:+.4f}); gross winnings only: theta_eff={th_gr:+.4f}")
    expect(gd_ok, "f1(D): with gross winnings only, theta_eff is lower still (premise 'net payoff reinvested' is load-bearing)")

    # ---------------- (E) m02(B): two-period strategic contest, general form [identity]
    def two_period_m02(n, th0, Om1, c, ell, K0, kap, Om20, g, r, delta):
        def objective(i, es):
            E = sum(es)
            pis = [Om1 * es[j] / E - c * es[j] - ell * E for j in range(n)]
            Ks = [K0 + kap * p for p in pis]
            S = sum(Ks); Om2 = Om20 + g * S
            w = [k ** r for k in Ks]; Wt = sum(w)
            W2 = [Om2 * x / Wt for x in w]
            oth = lambda v: (sum(v) - v[i]) / (n - 1)
            return pis[i] + th0 * oth(pis) + delta * (W2[i] + th0 * oth(W2))
        e = 0.1
        for _ in range(300):
            en = _golden_max(lambda x: objective(0, [x] + [e] * (n - 1)), 1e-7, 2.0, it=120)
            if abs(en - e) < 1e-12: break
            e = 0.5 * e + 0.5 * en
        pibar = Om1 / n - c * e - ell * n * e; Kb = K0 + kap * pibar
        Om2 = Om20 + g * n * Kb
        lam_rel = delta * Om2 * r * kap / (n * Kb); lam_com = delta * g * kap
        rho = (1 + th0) * (1 + lam_com) / ((n - 1 - th0) * (1 + lam_rel))
        th = (rho * (n - 1) - 1) / (1 + rho)
        e_form = Om1 * (n - 1 - th) / (n * n * (c + (1 + th) * ell))
        rho0 = (1 + th0) / ((n - 1 - th0) * (1 + lam_rel)); th_old = (rho0 * (n - 1) - 1) / (1 + rho0)
        e_old = Om1 * (n - 1 - th_old) / (n * n * (c + (1 + th_old) * ell))
        return e, e_form, e_old, th, th_old, lam_rel, lam_com
    print("(E) [identity] m02(B): two-period contest, period-2 prize Om20 + g sum K: direct e* vs e(theta) general and fixed-prize")
    worstB = 0.0; maxold = 0.0; narrow_flags = {}
    for kw in [dict(g=0.0), dict(g=0.3), dict(g=0.6, Om20=0.0), dict(g=0.6, Om20=0.0, r=0.7), dict(g=0.6, Om20=0.0, r=1.4), dict(g=0.3, th0=1.0, n=4)]:
        base = dict(n=3, th0=0.5, Om1=1.0, c=1.0, ell=0.2, K0=1.0, kap=0.5, Om20=1.0, g=0.0, r=1.0, delta=0.9); base.update(kw)
        e, ef, eo, th, tho, lr, lc = two_period_m02(**base)
        worstB = max(worstB, abs(e - ef) / e); maxold = max(maxold, abs(e - eo) / e)
        narrow_flags[str(kw)] = th - base['th0']
        print(f"   {kw}: e*={e:.7f} e(theta_general)={ef:.7f} [theta={th:+.4f}; lam_rel={lr:.4f} lam_com={lc:.4f}] e(theta_fixedprize)={eo:.7f} [theta={tho:+.4f}]")
    expect(worstB < 1e-6, f"m02(B): e* equals e(theta) of the general form (rel. error {worstB:.1e})")
    expect(maxold > 0.1, f"m02(B): the fixed-prize form misses e* by up to {maxold:.0%} when the prize grows")
    expect(abs(narrow_flags[str(dict(g=0.6, Om20=0.0))]) < 1e-6 and narrow_flags[str(dict(g=0.6, Om20=0.0, r=0.7))] > 0
           and narrow_flags[str(dict(g=0.6, Om20=0.0, r=1.4))] < 0, "m02(B): proportional prize: theta = theta0 at r=1, wider at r=0.7, narrower at r=1.4")

    # ---------------- (F) m02(C): narrowing vs share instability under balanced growth; thresholds with diffusion [independent]
    def share_unstable(n, r, kap, d, df, beta, g, T=600):
        X = [1.0 + 1e-6] + [1.0 - 1e-6 / (n - 1)] * (n - 1)
        for t in range(T):
            S = sum(X); Om = g * S
            w = [x ** r for x in X]; W = sum(w)
            X = [(1 - d) * x + kap * Om * ((1 - beta) * wi / W + beta / n) - df * (x - S / n) for x, wi in zip(X, w)]
            S = sum(X); X = [x / S * n for x in X]
        return abs(X[0] - 1) > 1e-6
    print("(F) [independent] m02(C): prize proportional to capacity: narrowing (Grel_d > Gcom_d) vs instability of equal shares (simulated)")
    agree = disagree = 0; parting = []
    for r in (0.5, 0.8, 0.95, 1.05, 1.17, 1.2, 1.6, 2.5):
        for beta in (0.0, 0.2, 0.4):
            for df in (0.0, 0.03):
                n, kap, d, g, delta = 3, 0.5, 0.1, 0.3, 0.9
                a = (1 - beta) * r * kap * g
                Grel = delta * a / (1 - delta * (1 - d - df)); Gcom = delta * kap * g / (1 - delta * (1 - d))
                narrows = Grel > Gcom
                unstable = share_unstable(n, r, kap, d, df, beta, g)
                if df == 0.0:
                    if narrows == unstable: agree += 1
                    else: disagree += 1
                elif narrows != unstable:
                    parting.append((r, beta, 'narrows' if narrows else 'widens', 'unstable' if unstable else 'stable'))
    print(f"   no diffusion: narrowing and instability coincide in {agree} of {agree+disagree} cases; with diffusion they part in {parting}")
    expect(agree == 24 and disagree == 0, "m02(C): without diffusion, narrowing iff equal shares unstable, 24/24")
    expect(len(parting) >= 1 and all(p[2] == 'narrows' and p[3] == 'stable' for p in parting), "m02(C): with diffusion the objective can narrow while equal shares are stable")
    # the two thresholds with diffusion, located by simulation alone (bisection on r): instability (share simulation) and
    # narrowing (nonlinear PV of a relative against a common unit); predicted 1 + delta_f/(kap g) and 1 + delta delta_f/(1-delta(1-d)).
    n, kap, d, g, delta, df, beta = 3, 0.5, 0.1, 0.3, 0.9, 0.03, 0.0
    lo, hi = 1.0, 1.5
    for _ in range(30):
        m = (lo + hi) / 2
        if share_unstable(n, m, kap, d, df, beta, g, T=3000): hi = m
        else: lo = m
    r_inst = (lo + hi) / 2
    def rel_minus_com(r):
        Om_fun = lambda S: g * S; X0 = [1.0] * n; y = 1e-6
        rel = (simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [kap * y] + [-kap * y / (n - 1)] * (n - 1), T=2500)
               - simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [-kap * y] + [kap * y / (n - 1)] * (n - 1), T=2500)) / (2 * y)
        com = (simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [kap * y] * n, T=2500)
               - simulate_pv(n, r, kap, d, df, 0.0, beta, Om_fun, delta, X0, [-kap * y] * n, T=2500)) / (2 * y)
        return rel - com
    lo, hi = 1.0, 1.5
    for _ in range(22):
        m = (lo + hi) / 2
        if rel_minus_com(m) > 0: hi = m
        else: lo = m
    r_narr = (lo + hi) / 2
    p_inst = 1 + df / (kap * g); p_narr = 1 + delta * df / (1 - delta * (1 - d))
    print(f"   with df={df}: simulated instability threshold r={r_inst:.4f} (1+df/(kap g)={p_inst:.4f}); simulated narrowing threshold r={r_narr:.4f} (1+delta df/(1-delta(1-d))={p_narr:.4f})")
    expect(abs(r_inst - p_inst) < 2e-3 and abs(r_narr - p_narr) < 2e-3, "diffusion separates the thresholds: narrowing at (1-beta)r > 1+delta df/(1-delta(1-d)), instability at 1+df/(kap g)")
    n, r, kap, d, df, k0, beta, Om0, g, delta = 3, 1.5, 0.5, 0.2, 0.0, 0.1, 0.0, 1.0, 0.0, 0.9
    S = steady(n, kap, d, k0, Om0, g); a = (1 - beta) * r * kap * (Om0 + g * S) / S
    print(f"   stationary total, fixed prize (n=3, r=1.5, k0=0.1): Gamma={a/(d+df):.3f} (<1: equal standing stable) while Gcom_d=0 < Grel_d: the objective narrows")

    # ---------------- (G) m02(E): Test Gamma's observable, (de/d ell)/(de/dc) = 1+theta [independent]
    def contest_eq(n, theta, Om, c, ell, r=1.0):
        def J(x, e):
            E = x + (n - 1) * e
            w = x ** r / (x ** r + (n - 1) * e ** r)
            return Om * w - c * x - ell * E + theta * (Om * (1 - w) / (n - 1) - c * e - ell * E)
        e = 0.1
        for _ in range(300):
            en = _golden_max(lambda x: J(x, e), 1e-9, 5.0, it=120)
            if abs(en - e) < 1e-13: break
            e = 0.5 * e + 0.5 * en
        return e
    print("(G) [independent] m02(E): Test Gamma's observable: ratio of intensity's response to shared loss and to private cost vs 1+theta")
    worstG = 0.0
    for (n, th) in ((2, -0.5), (3, 0.0), (4, -0.43), (4, 1.0)):
        h = 1e-4; Om, c, ell = 1.0, 1.0, 0.3
        dl = (contest_eq(n, th, Om, c, ell + h) - contest_eq(n, th, Om, c, ell - h)) / (2 * h)
        dc = (contest_eq(n, th, Om, c + h, ell) - contest_eq(n, th, Om, c - h, ell)) / (2 * h)
        worstG = max(worstG, abs(dl / dc - (1 + th)))
        print(f"   n={n} theta={th}: ratio {dl/dc:.5f}, 1+theta {1+th:.5f}")
    expect(worstG < 1e-3, f"m02(E): the observable equals 1+theta (max error {worstG:.1e})")

    # ---------------- (H) Codex case 9: provision raises the normalized common-channel weight 1+theta (Test Gamma sign)
    def gains(r, decay, diffusion, discount=0.9, won_share=1.0):
        return (r * won_share * decay / (decay + diffusion),
                r * won_share * discount * decay / (1 - discount * (1 - decay - diffusion)))
    def theta_effective(Gd, n=4, theta0=0):
        return (n * theta0 - (n - 1) * (1 + theta0) * Gd) / (n - (1 + theta0) * Gd)
    cb = 1 + theta_effective(gains(1, 0.2, 0.1, won_share=1)[1]); ca = 1 + theta_effective(gains(1, 0.2, 0.1, won_share=0.5)[1])
    print(f"(H) Codex case 9: 1+theta_Gamma with won share 1 -> {cb:.4f}; with provision (won share 0.5) -> {ca:.4f}")
    expect(ca > cb, "Codex 9: provision raises the weight on what all share (Test Gamma's sign: 1+theta rises with provision)")
    _codex(10, ca > cb)

    # ---------------- (I) adv_checks.py section 2: twoerrors (accurate coupling overridden by compounding) [identity]
    print("(I) [identity] twoerrors (Adv-O I2): an actor whose held theta0 equals the true coupling kappa acts on theta_Gamma(kappa) < 0 once Gamma_delta > n kappa/((n-1)(1+kappa))")
    def theta_G(t0, G, n): return (n * t0 - (n - 1) * (1 + t0) * G) / (n - (1 + t0) * G)
    okI = True
    for n in (2, 4):
        for kappa in (0.2, 0.4, 1.0):
            Gstar = n * kappa / ((n - 1) * (1 + kappa))
            row = ", ".join(f"G={G}:{theta_G(kappa,G,n):+.2f}" for G in (0.25, 0.5, 0.75, 0.9))
            okI &= abs(theta_G(kappa, Gstar, n)) < 1e-12 and theta_G(kappa, Gstar + 1e-3, n) < 0 < theta_G(kappa, Gstar - 1e-3, n) if Gstar < 1 else True
            print(f"   n={n} kappa={kappa}: working theta below 0 once Gamma_delta > {Gstar:.3f};  {row}")
    expect(okI, "twoerrors threshold Gamma_delta* = n kappa/((n-1)(1+kappa)) (n=4, kappa=0.4: 0.381)")

    # ---------------- (J) prop39_growing_prize.py (Adv-F F1): the fixed-prize formula fails when the prize grows [identity]
    print("(J) [identity] prop39 (Adv-F): two-period contest, gross-vs-net as in v2 (net payoff reinvested), prize W2_0 + g sum K")
    def p39_obj(e, i, n, r, W1, c, l, th0, delta, kappa, K0, W20, g):
        s = sum(x ** r for x in e); p = [x ** r / s for x in e]; tot = sum(e)
        pi1 = [W1 * p[k] - c * e[k] - l * tot for k in range(n)]
        K = [max(K0 + kappa * pi1[k], 1e-9) for k in range(n)]
        W2 = W20 + g * sum(K); sK = sum(x ** r for x in K); w2 = [W2 * x ** r / sK for x in K]
        def J(k, vec): return vec[k] + th0 * sum(vec[j] for j in range(n) if j != k) / (n - 1)
        return J(i, pi1) + delta * J(i, w2)
    def p39_eq(n, args):
        e = 0.2
        for _ in range(300):
            br = _golden_max(lambda x: p39_obj([x] + [e] * (n - 1), 0, n, *args), 1e-6, 1.5, it=200)
            en = 0.5 * e + 0.5 * br
            if abs(en - e) < 1e-12: e = en; break
            e = en
        return e
    n = 4; W1 = 1.0; c = 1.0; l = 0.3; delta = 0.95; kappa = 1.0; K0 = 1.0
    cases = ([(r, th0, 1.0, g) for r in (0.8, 1.0, 1.2) for th0 in (0.0, 1.0) for g in (0.0, 0.5, 1.0, 2.0)] if FULL
             else [(r, 0.0, 1.0, g) for r in (0.8, 1.2) for g in (0.0, 1.0)])
    okJ = True
    for (r, th0, W20, g) in cases:
        args = (r, W1, c, l, th0, delta, kappa, K0, W20, g)
        estar = p39_eq(n, args)
        A = r * W1; B = estar * n * n; th_eff = (A * (n - 1) - B * (c + l)) / (A + B * l)
        K = K0 + kappa * (W1 / n - estar * (c + n * l)); W2 = W20 + g * n * K
        lam_rel = delta * kappa * r * W2 / (n * K); lam_com = delta * kappa * g
        R = (1 + th0) * (1 + lam_com) / ((n - 1 - th0) * (1 + lam_rel)); th_pred = (R * (n - 1) - 1) / (1 + R)
        Gd = lam_rel / (1 + lam_rel); th_paper = (n * th0 - (n - 1) * (1 + th0) * Gd) / (n - (1 + th0) * Gd)
        okJ &= abs(th_eff - th_pred) < 1e-4
        print(f"   r={r} theta0={th0} g={g}: theta_eff(num)={th_eff:+.4f} general form {th_pred:+.4f}; fixed-prize formula {th_paper:+.4f}")
    for r in (0.7, 1.0, 1.3):
        args = (r, W1, c, l, 0.5, delta, kappa, K0, 0.0, 1.0)
        estar = p39_eq(n, args); A = r * W1; B = estar * n * n; th_eff = (A * (n - 1) - B * (c + l)) / (A + B * l)
        okJ &= (th_eff < 0.5 - 1e-6) == (r > 1)
        print(f"   proportional prize W2 = sum K, r={r}, theta0=0.5: theta_eff={th_eff:+.4f} ({'narrower' if th_eff < 0.5-1e-6 else 'not narrower'})")
    expect(okJ, "prop39: theta_eff matches the general form; with a proportional prize it narrows iff r > 1")


def check_PD():
    block('PD', 'loopgain, standprice', 'independent',
          'Price domain: beyond Gamma_delta = 1 the price of standing is infinite (a cusp), not negative; slow convergence inside; logarithm at the boundary')
    # Sources: planning/math-fable/f1_standprice.py (C); planning/math-opus/m02_standprice_general.py (D);
    # ../v6.1/reviews/counterexamples_v61_codex.py case 1 (Codex boundary case: Gamma_delta >= 1).
    # Claim (D2-fable s1-2, D2-opus s1): the series converges iff Gamma_delta < 1; for delta*Lambda* > 1,
    # PV(eps) ~ eps^alpha with alpha = ln(1/delta)/ln(Lambda*) < 1, so PV/eps diverges as eps^(alpha-1); at
    # delta*Lambda* = 1 PV/eps grows like ln(1/eps); for Gamma > 1 > Gamma_delta it converges to Gd/(1-Gd) at rate eps^(-ln(delta Lambda*)/ln Lambda*).
    # ---- Codex case 1
    def stock_step(stocks, r, decay, diffusion=0.0, cap=None):
        strengths = [x ** r for x in stocks]; mean = sum(stocks) / len(stocks)
        new = [(1 - decay) * x + s / sum(strengths) + diffusion * (mean - x) for x, s in zip(stocks, strengths)]
        return new if cap is None else [min(cap, x) for x in new]
    G = 2 * 0.2 / 0.2; Gd = 2 * 0.9 * 0.2 / (1 - 0.9 * 0.8)
    stocks = [2.50001, 2.49999]; pv = 0.0
    for t in range(1000):
        p = stocks[0] ** 2 / sum(x ** 2 for x in stocks)
        pv += 0.9 ** (t + 1) * (p - 0.5)
        stocks = stock_step(stocks, 2, 0.2)
    print(f"(a) Codex case 1 (n=2, kappa Omega=1, d=0.2, r=2, delta=0.9): Gamma={G:.3f}, Gamma_delta={Gd:.6f}, printed multiplier Gd/(1-Gd)={Gd/(1-Gd):.3f}; "
          f"nonlinear discounted advantage from (2.50001, 2.49999): {pv:.7f}")
    expect(Gd > 1 and Gd / (1 - Gd) < 0 < pv, "Codex 1: outside the domain the printed multiplier is negative while the true discounted advantage is positive")
    _codex(1, Gd > 1 and Gd / (1 - Gd) < 0 < pv)
    # ---- f1(C): local exponent of PV/eps
    n, r, d, delta = 2, 2.0, 0.2, 0.9
    lam_star = 1 + d * (r - 1); alpha = math.log(1 / delta) / math.log(lam_star)
    print(f"(b) f1(C): Lambda*={lam_star:.3f}, delta*Lambda*={delta*lam_star:.3f} > 1; predicted PV ~ eps^alpha, alpha={alpha:.4f}; PV/eps ~ eps^{alpha-1:+.4f}")
    def pv_f1(eps, T=3000):
        K = [2.5 + eps, 2.5 - eps]; s = 0.0; disc = delta
        for t in range(T):
            P = sum(x ** r for x in K); p = K[0] ** r / P
            s += disc * (p - 0.5); disc *= delta
            K = [(1 - d) * x + x ** r / P for x in K]
        return s
    prev = None; slopes = []; allpos = True
    for eps in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
        v = pv_f1(eps); allpos &= v > 0
        sl = None if prev is None else (math.log(v / eps) - math.log(prev[1] / prev[0])) / (math.log(eps) - math.log(prev[0]))
        if sl is not None: slopes.append(sl)
        print(f"   eps={eps:.0e}: PV={v:.6e}, PV/eps={v/eps:.4e}" + ("" if sl is None else f"  local exponent of PV/eps {sl:+.4f}"))
        prev = (eps, v)
    expect(allpos and abs(slopes[-1] - (alpha - 1)) < 2e-3, f"f1(C): PV > 0 at every eps and the exponent of PV/eps tends to alpha-1 = {alpha-1:.4f} (last {slopes[-1]:.4f})")
    # ---- m02(D): fitted exponents, inside-domain convergence, the boundary
    def simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, bump, T=4000):
        X = [x + b for x, b in zip(X0, bump)]; pv = 0.0; disc = 1.0
        for t in range(1, T + 1):
            S = sum(X); Om = Om_fun(S); w = [x ** r for x in X]; W = sum(w); p = [wi / W for wi in w]
            disc *= delta; pv += disc * Om * ((1 - beta) * p[0] + beta / n); mean = S / n
            X = [(1 - d) * x + kap * Om * ((1 - beta) * pi + beta / n) + k0 - df * (x - mean) for x, pi in zip(X, p)]
        return pv
    n, r, kap, d, df, k0, beta, delta = 2, 2.0, 1.0, 0.2, 0.0, 0.0, 0.0, 0.9
    Om_fun = lambda S: 1.0; S = 1.0 / d; X0 = [S / 2, S / 2]
    m = 1 - d - df + (1 - beta) * r * kap * 1.0 / S; alpha = math.log(1 / delta) / math.log(m)
    base = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [0, 0], T=1500)
    rows = []
    for k in range(2, 11, 2):
        eps = 10.0 ** (-k)
        rows.append((eps, simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [eps, -eps], T=1500) - base))
    print(f"(c) m02(D): m_rel={m:.3f}, predicted exponent of PV in eps {alpha:.4f}")
    fitted = []
    for (e1, p1), (e2, p2) in zip(rows, rows[1:]):
        fitted.append(math.log(p2 / p1) / math.log(e2 / e1))
        print(f"   eps {e1:.0e}: PV {p1:.6e}, PV/eps {p1/e1:.3e}; fitted exponent to next: {fitted[-1]:.4f}")
    expect(abs(fitted[-1] - alpha) < 1e-3, f"m02(D): fitted exponent {fitted[-1]:.4f} equals ln(1/delta)/ln(m) = {alpha:.4f}")
    delta = 0.8; fac = delta * d / (1 - delta * (1 - d)); Gd = 2 * fac
    base = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [0, 0], T=1500)
    gaps = []
    print(f"   inside the domain but above Gamma=1 (delta=0.8, Gd={Gd:.4f}, delta*m=0.96): formula Gd/(1-Gd) = {Gd/(1-Gd):.6f}; PV/eps:")
    for k in (4, 6, 8, 10, 12):
        eps = 10.0 ** (-k)
        pv = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [eps, -eps], T=1500) - base
        gaps.append(Gd / (1 - Gd) - pv / eps)
        print(f"      eps 1e-{k}: {pv/eps:.6f} (gap {gaps[-1]:.2e})")
    pred_rate = 10 ** (-2 * (-math.log(delta * m) / math.log(m)))
    expect(all(g > 0 for g in gaps) and abs(gaps[-1] / gaps[-2] / pred_rate - 1) < 0.1,
           f"m02(D): for Gamma > 1 > Gamma_delta, PV/eps -> Gd/(1-Gd) = 8 from below, the gap shrinking by {pred_rate:.3f} per two decades (eps^0.224)")
    delta = 1 / m
    base = simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [0, 0], T=3000)
    vals = []
    for k in (3, 5, 7, 9):
        eps = 10.0 ** (-k)
        vals.append((simulate_pv(n, r, kap, d, df, k0, beta, Om_fun, delta, X0, [eps, -eps], T=3000) - base) / eps)
    incs = [b - a for a, b in zip(vals, vals[1:])]
    print(f"   at delta*m = 1: PV/eps at eps=1e-3,1e-5,1e-7,1e-9: {', '.join('%.2f' % v for v in vals)}; increments {', '.join('%.2f' % x for x in incs)}")
    expect(max(incs) - min(incs) < 0.05 * max(incs), "m02(D): at delta*Lambda* = 1, PV/eps grows by a constant per two decades (logarithmic)")


def check_MP():
    block('MP', 'loopgain, standprice, eqgain (S2)', 'independent',
          'Markov-perfect compounding contest: price of standing and both elasticities (r_eq for stability, r_pr for the price); amplification; laggards; multiplicity')
    # Sources: planning/math-opus/m01_loopgain_mpe.py (B-F); planning/math-fable/f2_mpe.py (1,2);
    # ../v6.1/reviews/scripts-v6.1-math-opus/s2_mpe.py, s2b_mpe_extra.py, s2c_profile.py, s2d_eqgain.py, s2e_check.py;
    # ../v6.1/reviews/scripts-v6.1-math-fable/m2_fullgame.py; ../v6.1/reviews/scripts-v6.1-adv-opus/adv_checks.py section 3.
    # Claims (D2-opus s1(4), D2-fable Remark S2.2): with rivals responding, stability is decided by the equilibrium
    # gain (r_eq), the price by the partial-equilibrium gain (r_pr: own intensity held, rivals responding):
    # lambda = Gpr_d/(1-Gpr_d) (+ the rivals' shared-loss term); static Tullock r_pr/r = 2(n-1)/n; in discouragement
    # contests r_eq > r, so a structural Gamma < 1 does not ensure stability; catch-up can reverse the sign.
    # Multiplicity (a winner-take-all equilibrium coexisting with the smooth one) is a numerical finding held for
    # outside review (plan s3): it is reported, and asserted only as "two distinct converged fixed points".
    # ---------------------------------------------------------------- m01 machinery (ported)
    def m01_solve(r=1.0, Gamma=0.6, beta=0.0, d=0.05, delta=None, Om=1.0, c=1.0, l=0.0, N=1200, tol=1e-11, maxit=40000, Lsub=0.0, damp=1.0, V0=None):
        if delta is None: delta = 1.0 / (1.0 + d)
        w = Gamma / ((1 - beta) * r)
        assert 0 < w <= 1
        jw = d * (w * ((1 - beta) + beta / 2) + (1 - w) / 2)
        jl = d * (w * beta / 2 + (1 - w) / 2)
        grid = [i / N for i in range(N + 1)]
        def I(V, x):
            if x <= 0: return V[0]
            if x >= 1: return V[-1]
            k = int(x * N)
            if k >= N: k = N - 1
            t = x * N - k
            return V[k] + t * (V[k + 1] - V[k])
        def stage(s, V):
            sw = (1 - d) * s + jw; sl = (1 - d) * s + jl
            A1 = (1 - beta) * Om + delta * (I(V, sw) - I(V, sl))
            A2 = (1 - beta) * Om + delta * (I(V, 1 - sl) - I(V, 1 - sw))
            a1 = s ** r if s > 0 else 0.0
            a2 = (1 - s) ** r if s < 1 else 0.0
            A1p = max(A1, 0.0); A2p = max(A2, 0.0)
            den = a1 * A1p + a2 * A2p
            if den == 0: return 0.5, 0.0, 0.0, sw, sl, A1, A2
            p = a1 * A1p / den
            e1 = A1p * p * (1 - p) / (c + l); e2 = A2p * p * (1 - p) / (c + l)
            return p, e1, e2, sw, sl, A1, A2
        V = [0.0] * (N + 1) if V0 is None else [V0(s) for s in grid]
        for it in range(maxit):
            Vn = [0.0] * (N + 1)
            for k, s in enumerate(grid):
                p, e1, e2, sw, sl, _, _ = stage(s, V)
                Vn[k] = (1 - beta) * Om * p + beta * Om / 2 - c * e1 - l * (e1 + e2) - Lsub * (1 - s) ** 2 + delta * (p * I(V, sw) + (1 - p) * I(V, sl))
            diff = max(abs(a - b) for a, b in zip(V, Vn)); V = [a + damp * (b - a) for a, b in zip(V, Vn)]
            if diff < tol: break
        p0, e10, e20, sw0, sl0, A10, _ = stage(0.5, V)
        lam_mpe = delta * (I(V, sw0) - I(V, sl0)) / ((1 - beta) * Om)
        res = dict(it=it, diff=diff, lam_mpe=lam_mpe, e=e10, w=w, jump=jw - jl)
        for hcells in (2, 6, 12):
            h = hcells / N
            pa, e1a, e2a, *_ = stage(0.5 + h, V); pb, e1b, e2b, *_ = stage(0.5 - h, V)
            r_eq = (pa - pb) / (2 * h)
            def p_ownfixed(s, e2s):
                a1 = s ** r; a2 = (1 - s) ** r
                return a1 * e10 / (a1 * e10 + a2 * e2s)
            r_pr = (p_ownfixed(0.5 + h, e2a) - p_ownfixed(0.5 - h, e2b)) / (2 * h)
            res[f'r_eq_{hcells}'] = r_eq; res[f'r_pr_{hcells}'] = r_pr; res[f'de2_{hcells}'] = (e2a - e2b) / (2 * h)
        fac = delta * d / (1 - delta * (1 - d)); Gd = Gamma * fac
        res['lam_struct'] = Gd / (1 - Gd)
        r_pr = res['r_pr_6']; r_eq = res['r_eq_6']
        Gpr_d = (1 - beta) * r_pr * w * fac; res['Gpr_d'] = Gpr_d
        res['lam_pred'] = (Gpr_d - fac * w * l * res['de2_6'] / ((1 - beta) * Om)) / (1 - Gpr_d) if Gpr_d < 1 else float('inf')
        res['Geq_d'] = (1 - beta) * r_eq * w * fac; res['Geq'] = (1 - beta) * r_eq * w; res['Gpr'] = (1 - beta) * r_pr * w
        for s in (0.25, 0.75):
            p, e1, e2, sw, sl, *_ = stage(s, V)
            res[f'lam_at_{s}'] = delta * (I(V, sw) - I(V, sl)) / ((1 - beta) * Om); res[f'e1_at_{s}'] = e1; res[f'e2_at_{s}'] = e2
        s = 0.52
        for t in range(40):
            p, *_ = stage(s, V); s = (1 - d) * s + jl + (jw - jl) * p
        res['s40'] = s
        A1 = A10
        def pay(x):
            a1 = 0.5 ** r; a2 = 0.5 ** r
            pp = a1 * x / (a1 * x + a2 * e20) if x + e20 > 0 else 0.5
            return A1 * pp - (c + l) * x
        best = max(pay(e20 * 10 ** (k / 200.0)) for k in range(-600, 601))
        res['br_gap'] = best - pay(e10)
        return res
    def static_tullock_factor(n, eps=1e-6):
        def eq(alpha):
            Sig = sum(1 / a for a in alpha); X = (n - 1) / Sig
            return [X / a * (1 - (n - 1) / (a * Sig)) for a in alpha]
        f0 = eq([1.0] * n)
        def p_own_fixed(e):
            alpha = [math.exp(e)] + [1.0] * (n - 1); f = eq(alpha)
            return alpha[0] * f0[0] / (alpha[0] * f0[0] + sum(alpha[k] * f[k] for k in range(1, n)))
        def p_rel_fixed(e):
            alpha = [math.exp(e)] + [math.exp(-e / (n - 1))] * (n - 1)
            return alpha[0] * f0[0] / sum(alpha[k] * f0[k] for k in range(n))
        def p_rel_resp(e):
            alpha = [math.exp(e)] + [math.exp(-e / (n - 1))] * (n - 1); f = eq(alpha)
            return alpha[0] * f0[0] / (alpha[0] * f0[0] + sum(alpha[k] * f[k] for k in range(1, n)))
        def p_struct(e):
            alpha = [math.exp(e)] + [1.0] * (n - 1); return alpha[0] / sum(alpha)
        dpr = (p_own_fixed(eps) - p_own_fixed(-eps)) / (2 * eps); dst = (p_struct(eps) - p_struct(-eps)) / (2 * eps)
        drel_r = (p_rel_resp(eps) - p_rel_resp(-eps)) / (2 * eps); drel_f = (p_rel_fixed(eps) - p_rel_fixed(-eps)) / (2 * eps)
        return dpr / dst, drel_r / drel_f
    # ---------------------------------------------------------------- (a) m01(D): static Tullock 2(n-1)/n
    print("(a) m01(D): static Tullock with weights, own effort fixed, rivals at their equilibrium: r_pr/r vs 2(n-1)/n")
    okD = True
    for n in (2, 3, 4, 6, 10):
        a, b = static_tullock_factor(n); okD &= abs(a - 2 * (n - 1) / n) < 1e-6 and abs(b - 2 * (n - 1) / n) < 1e-6
        print(f"   n={n}: own-only {a:.6f}, relative {b:.6f}, 2(n-1)/n = {2*(n-1)/n:.6f}")
    expect(okD, "m01(D): r_pr/r = 2(n-1)/n exactly in the static Tullock (n = 2, 3, 4, 6, 10)")
    # ---------------------------------------------------------------- (b) m2_fullgame (Fable reviewer): two-period, period-2 effort
    print("(b) m2_fullgame (Math-Fable reviewer): two-period game, period-2 effort responding to capacity; lambda_full/lambda_red vs 2(n-1)/n")
    def period2(alpha, Om2, c2):
        n = len(alpha); Sig = sum(1 / a for a in alpha); X = Om2 * (n - 1) / (c2 * Sig)
        f = [X / alpha[k] * (1 - (n - 1) / (alpha[k] * Sig)) for k in range(n)]
        if min(f) <= 0: raise ValueError('corner')
        w = [alpha[k] * f[k] / X for k in range(n)]
        return f, w, [Om2 * w[k] - c2 * f[k] for k in range(n)]
    def m2_solve(n=3, Om1=1.0, c=1.0, l=0.3, K0=2.0, kap=0.5, Om2=2.0, r2=1.5, c2=1.0, dl=0.9):
        def U(i, es):
            E = sum(es); pis = [Om1 * es[j] / E - c * es[j] - l * E for j in range(n)]
            Ks = [K0 + kap * p for p in pis]
            if min(Ks) <= 0: return -1e9
            try: f, w, V = period2([k ** r2 for k in Ks], Om2, c2)
            except ValueError: return -1e9
            return pis[i] + dl * V[i]
        e = 0.2
        for _ in range(400):
            en = _golden_max(lambda x: U(0, [x] + [e] * (n - 1)), 1e-6, 3.0, it=200)
            if abs(en - e) < 1e-13: break
            e = 0.5 * e + 0.5 * en
        pibar = Om1 / n - c * e - l * n * e; Kbar = K0 + kap * pibar
        alpha0 = [Kbar ** r2] * n; f0, w0, V0 = period2(alpha0, Om2, c2); h = 1e-6
        def w_fixed(Ki):
            ai = Ki ** r2; return Om2 * ai * f0[0] / (ai * f0[0] + sum(alpha0[k] * f0[k] for k in range(1, n)))
        def Vfull(Ki):
            f, w, V = period2([Ki ** r2] + [Kbar ** r2] * (n - 1), Om2, c2); return V[0]
        lam_red = dl * kap * n / (n - 1) * (w_fixed(Kbar + h) - w_fixed(Kbar - h)) / (2 * h)
        lam_full = dl * kap * n / (n - 1) * (Vfull(Kbar + h) - Vfull(Kbar - h)) / (2 * h)
        th = -lam_full * (n - 1) / (n + lam_full * (n - 1))
        return e, Om1 * (n - 1 - th) / (n * n * (c + (1 + th) * l)), lam_red, lam_full
    okM2 = True
    for kw in [dict(n=2), dict(n=3), dict(n=4), dict(n=6), dict(n=3, r2=1.0, Om2=4.0), dict(n=4, dl=0.5), dict(n=3, kap=1.0, K0=1.0)]:
        e, e_full, lr, lf = m2_solve(**kw); n = kw.get('n', 3)
        okM2 &= abs(lf / lr - 2 * (n - 1) / n) < 1e-4 and abs(e - e_full) < 1e-6
        print(f"   {kw}: e*={e:.6f}; e(theta(lambda_full))={e_full:.6f}; lambda_full/lambda_red={lf/lr:.4f} vs 2(n-1)/n={2*(n-1)/n:.4f}")
    expect(okM2, "m2_fullgame: the two-period price with responding period-2 effort is lambda_red * 2(n-1)/n, and e* = e(theta(lambda_full))")
    # ---------------------------------------------------------------- (c) m01(B,C): MPE table
    print("(c) m01(B,C): MPE, n=2, delta=1/1.1 (Gd = Gamma/2), small jumps by large r; lam_MPE vs envelope formula with measured r_pr")
    def row(R, tag, r):
        print(f"   {tag}: jump={R['jump']:.4f} lam_MPE={R['lam_mpe']:.4f} lam_pred={R['lam_pred']:.4f} struct={R['lam_struct']:.4f} "
              f"MPE/struct={R['lam_mpe']/R['lam_struct']:.2f} | r_eq/r={R['r_eq_6']/r:.2f} (h=2,12 cells: {R['r_eq_2']/r:.2f},{R['r_eq_12']/r:.2f}) "
              f"r_pr/r={R['r_pr_6']/r:.2f} | Geq={R['Geq']:.2f} Geq_d={R['Geq_d']:.2f} Gpr_d={R['Gpr_d']:.2f} | lam(.25)={R['lam_at_0.25']:.4f} "
              f"lam(.75)={R['lam_at_0.75']:.4f} | s40={R['s40']:.3f} | BRgap {R['br_gap']:.0e} conv {R['diff']:.0e}", flush=True)
    tab = {}
    for G in (0.2, 0.3, 0.4, 0.45, 0.5, 0.6, 0.8):
        R = m01_solve(r=4.0, Gamma=G, d=0.1, N=1500, maxit=5000); tab[G] = R; row(R, f"r=4 Gamma={G}", 4.0)
    for G in (0.3, 0.6):
        R = m01_solve(r=8.0, Gamma=G, d=0.1, N=3000, maxit=5000); tab[('r8', G)] = R; row(R, f"r=8 Gamma={G} (jump halved)", 8.0)
    for kw in (dict(l=0.5), dict(beta=0.3)):
        R = m01_solve(r=4.0, Gamma=0.3, d=0.1, N=1500, maxit=5000, **kw); tab[str(kw)] = R; row(R, f"r=4 Gamma=0.3 {kw}", 4.0)
    for G in (0.3, 0.6, 0.9):
        R = m01_solve(r=1.0, Gamma=G, d=0.1, N=600, maxit=5000); tab[('r1', G)] = R; row(R, f"r=1 Gamma={G} (large jumps)", 1.0)
    smooth = [tab[G] for G in (0.2, 0.3, 0.4)] + [tab[('r8', 0.3)], tab[str(dict(l=0.5))], tab[str(dict(beta=0.3))]]
    expect(all(abs(R['lam_mpe'] / R['lam_pred'] - 1) < 0.025 for R in smooth),
           "m01: smooth branch (structural Gamma <= 0.4, incl. shared loss and sharing): MPE price = envelope formula with r_pr to 2.5% (0.5% at Gamma <= 0.3)")
    expect(all(abs(tab[G]['lam_mpe'] / tab[G]['lam_pred'] - 1) < 0.006 for G in (0.2, 0.3)), "m01: at Gamma = 0.2, 0.3 the agreement is within 0.5%")
    expect(all(R['br_gap'] < 1e-12 for R in tab.values()), "m01: the computed policy is a global best response at parity (gap < 1e-12)")
    expect(tab[0.45]['Geq'] > 1 and tab[0.6]['Geq'] > 2 and tab[0.6]['lam_mpe'] / tab[0.6]['lam_struct'] > 2,
           f"m01: above structural Gamma ~ 0.45 equal standing is unstable in equilibrium (Gamma_eq = {tab[0.45]['Geq']:.2f} at 0.45, {tab[0.6]['Geq']:.2f} at 0.6) and the price is amplified")
    expect(all(R['r_eq_6'] > R['r_pr_6'] > (4.0 if k not in [('r8', 0.3), ('r8', 0.6), ('r1', 0.3), ('r1', 0.6), ('r1', 0.9)] else (8.0 if k[0] == 'r8' else 1.0))
               for k, R in tab.items()), "m01: in this discouragement contest r_eq > r_pr > r at every computed point")
    r1 = tab[('r1', 0.3)]; r16 = tab[('r1', 0.6)]
    print(f"   off parity (r=1): laggard's price at s=0.25 is {r1['lam_at_0.25']/r1['lam_struct']:.0%} of the structural value at Gamma=0.3 and "
          f"{r16['lam_at_0.25']/r16['lam_struct']:.0%} at 0.6; the leader's at s=0.75 is {r1['lam_at_0.75']/r1['lam_struct']:.0%} at 0.3")
    expect(r1['lam_at_0.25'] < r1['lam_struct'] < r1['lam_at_0.75'], "m01: near parity a laggard prices standing below, a leader above, the structural value")
    # ---------------------------------------------------------------- (d) m01(E): catch-up
    print("(d) m01(E): catch-up: a flow cost Lsub (1-s)^2 of standing below the top (r=4)")
    catch = {}
    for Ls in (0.0, 10.0, 100.0):
        for G in (0.3, 0.6):
            R = m01_solve(r=4.0, Gamma=G, d=0.1, N=1500, maxit=5000, Lsub=Ls); catch[(Ls, G)] = R
            print(f"   Lsub={Ls} Gamma={G}: r_eq/r={R['r_eq_6']/4:.3f} r_pr/r={R['r_pr_6']/4:.3f} Geq={R['Geq']:.3f} e1(.25)={R['e1_at_0.25']:.4f} e2(.25)={R['e2_at_0.25']:.4f} "
                  f"(laggard {'tries harder' if R['e1_at_0.25']>R['e2_at_0.25'] else 'gives up'})", flush=True)
    expect(catch[(100.0, 0.3)]['r_eq_6'] / 4 < 1 and catch[(0.0, 0.3)]['r_eq_6'] / 4 > 1,
           f"m01(E): the sign of the strategic correction is not universal: r_eq/r = {catch[(100.0, 0.3)]['r_eq_6']/4:.3f} < 1 with a strong catch-up motive")
    # ---------------------------------------------------------------- (e) m01(F): multiplicity [numerical finding, outside review]
    print("(e) m01(F): value iteration from V=0 and from a step at parity (V0 = 3 sign(s-1/2)); r=4, delta=1/(1+d), damping 0.5")
    step = lambda s: 3.0 * (1 if s > 0.5 else (-1 if s < 0.5 else 0))
    mult = {}
    grid_cases = [(0.2, 0.1, 1500), (0.2, 0.05, 3000), (0.3, 0.05, 3000)] + ([(0.2, 0.05, 6000)] if FULL else [])
    for (G, d, N) in grid_cases:
        for init, V0 in (('V=0 ', None), ('step', step)):
            if init == 'V=0 ' and N == 6000: continue
            R = m01_solve(r=4.0, Gamma=G, d=d, N=N, maxit=20000, damp=0.5, V0=V0); mult[(G, d, N, init)] = R
            print(f"   Gamma={G} d={d} N={N} init {init}: lam_MPE={R['lam_mpe']:.4f} (struct {R['lam_struct']:.4f}, x{R['lam_mpe']/R['lam_struct']:.2f}); "
                  f"lam_pred={R['lam_pred']:.4f}; r_eq/r={R['r_eq_6']/4:.2f} (h=12: {R['r_eq_12']/4:.2f}); lam(.25)={R['lam_at_0.25']:.4f}; conv {R['diff']:.0e}", flush=True)
    a = mult[(0.2, 0.05, 3000, 'V=0 ')]; b = mult[(0.2, 0.05, 3000, 'step')]
    expect(a['diff'] < 1e-10 and b['diff'] < 1e-10 and b['lam_mpe'] > 5 * a['lam_mpe'],
           f"m01(F) [finding held for outside review]: two converged fixed points at Gamma=0.2, d=0.05: price {a['lam_mpe']:.4f} (smooth) and {b['lam_mpe']:.4f} (winner-take-all, x{b['lam_mpe']/b['lam_struct']:.1f} structural)")
    c_ = mult[(0.2, 0.1, 1500, 'V=0 ')]; d_ = mult[(0.2, 0.1, 1500, 'step')]
    expect(abs(c_['lam_mpe'] - d_['lam_mpe']) < 1e-6, "m01(F): at coarser rounds (d=0.1) the step start returns to the smooth equilibrium")
    if FULL:
        R = m01_solve(r=4.0, Gamma=0.2, d=0.025, N=4000, maxit=20000, damp=0.5)
        print(f"   finer rounds, smooth branch: Gamma=0.2 d=0.025 N=4000 init V=0: lam_MPE={R['lam_mpe']:.4f} lam_pred={R['lam_pred']:.4f} r_eq/r={R['r_eq_6']/4:.3f}")
    # ---------------------------------------------------------------- (f) f2: partial- and full-equilibrium gains (Fable's model)
    def f2_solve(r, Gamma, beta=0.0, Om=1.0, kap=0.5, d=0.2, c=1.0, l=0.0, delta=0.9, N=400, tol=1e-11, maxit=40000, mc=True):
        om = Gamma / ((1 - beta) * r)
        assert om <= 1.0
        k0 = kap * Om * (1 / om - 1) / 2; S = (kap * Om + 2 * k0) / d
        jw = (kap * Om * ((1 - beta) + beta / 2) + k0) / S; jl = (kap * Om * beta / 2 + k0) / S
        grid = [i / N for i in range(N + 1)]
        def interp(V, x):
            if x <= 0: return V[0]
            if x >= 1: return V[-1]
            k = min(int(x * N), N - 1); w = x * N - k
            return V[k] * (1 - w) + V[k + 1] * w
        def nxt(s): return (1 - d) * s + jw, (1 - d) * s + jl
        def stage(s, V, e1_fixed=None):
            sw, sl = nxt(s)
            A1 = (1 - beta) * Om + delta * (interp(V, sw) - interp(V, sl))
            A2 = (1 - beta) * Om + delta * (interp(V, 1 - sl) - interp(V, 1 - sw))
            a1 = s ** r if s > 0 else 0.0; a2 = (1 - s) ** r if s < 1 else 0.0
            A1p, A2p = max(A1, 0.0), max(A2, 0.0)
            if a1 * A1p + a2 * A2p == 0: return 0.5, 0.0, 0.0, sw, sl
            if e1_fixed is None:
                p = a1 * A1p / (a1 * A1p + a2 * A2p)
                e1 = A1p * p * (1 - p) / (c + l); e2 = A2p * p * (1 - p) / (c + l)
            else:
                e1 = e1_fixed
                X = math.sqrt(max(A2p * a2 * a1 * e1 / (c + l), 0.0))
                e2 = max((X - a1 * e1) / a2, 0.0) if a2 > 0 else 0.0
                p = a1 * e1 / (a1 * e1 + a2 * e2) if a1 * e1 + a2 * e2 > 0 else 0.5
            return p, e1, e2, sw, sl
        V = [0.0] * (N + 1)
        for it in range(maxit):
            Vn = []
            for s in grid:
                p, e1, e2, sw, sl = stage(s, V)
                Vn.append((1 - beta) * Om * p + beta * Om / 2 - c * e1 - l * (e1 + e2) + delta * (p * interp(V, sw) + (1 - p) * interp(V, sl)))
            diff = max(abs(a - b) for a, b in zip(V, Vn)); V = Vn
            if diff < tol: break
        s0 = 0.5; p, e1, e2, sw, sl = stage(s0, V)
        lam_mpe = delta * (interp(V, sw) - interp(V, sl)) / ((1 - beta) * Om)
        Gd = Gamma * delta * d / (1 - delta * (1 - d)); lam_formula = Gd / (1 - Gd) if Gd < 1 else float('inf')
        h = 2.0 / N
        pa, *_ = stage(s0 + h, V); pb, *_ = stage(s0 - h, V); p_eq = (pa - pb) / (2 * h)
        pa2, *_ = stage(s0 + h, V, e1_fixed=e1); pb2, *_ = stage(s0 - h, V, e1_fixed=e1); p_tilde = (pa2 - pb2) / (2 * h)
        G_eq = (1 - beta) * om * p_eq; G_t = (1 - beta) * om * p_tilde
        Gd_t = G_t * delta * d / (1 - delta * (1 - d)); lam_t = Gd_t / (1 - Gd_t) if Gd_t < 1 else float('inf')
        def Es(s):
            p, _, _, sw, sl = stage(s, V); return p * sw + (1 - p) * sl
        mult_ = (Es(s0 + h) - Es(s0 - h)) / (2 * h)
        lagg = []
        for sx in (0.25, 0.1):
            p_, _, _, sw_, sl_ = stage(sx, V); lagg.append(delta * (interp(V, sw_) - interp(V, sl_)) / ((1 - beta) * Om))
        Eabs = Eabs_p = None
        if mc:
            rnd = random.Random(11); acc = 0.0; accp = 0.0; M = 400
            for _ in range(M):
                s = 0.52; sp = 0.52
                for t in range(60):
                    p_, _, _, sw_, sl_ = stage(s, V); s = sw_ if rnd.random() < p_ else sl_
                    a1 = sp ** r; a2 = (1 - sp) ** r; pp = a1 / (a1 + a2)
                    swp, slp = nxt(sp); sp = swp if rnd.random() < pp else slp
                acc += abs(s - 0.5); accp += abs(sp - 0.5)
            Eabs = acc / M; Eabs_p = accp / M
        return dict(jump=jw - jl, lam_formula=lam_formula, lam_mpe=lam_mpe, p_eq=p_eq, p_tilde=p_tilde, G_eq=G_eq, G_t=G_t,
                    lam_t=lam_t, mult=mult_, mult_pred=1 + d * (G_eq - 1), lagg=lagg, Eabs=Eabs, Eabs_passive=Eabs_p, it=it)
    print("(f) f2(1): small jumps (d=0.02), l=0: equilibrium price vs the closed-loop gain of the partial-equilibrium loop; expected-deviation multiplier vs 1+d(Gamma_eq-1)")
    ok1 = True
    for (r, G) in [(1.0, 0.2), (1.0, 0.3), (1.5, 0.3), (1.0, 0.45), (1.5, 0.6)]:
        R = f2_solve(r, G, d=0.02, N=400, mc=False)
        ok1 &= abs(R['lam_mpe'] / R['lam_t'] - 1) < 0.005 and abs(R['mult'] - R['mult_pred']) < 1e-4
        print(f"   r={r} Gamma={G}: jump={R['jump']:.4f} | lambda: formula {R['lam_formula']:.4f}, MPE {R['lam_mpe']:.4f}, closed-loop(Gamma~_delta) {R['lam_t']:.4f} | "
              f"Gamma_eq={R['G_eq']:.3f} Gamma~={R['G_t']:.3f} | E-dev multiplier {R['mult']:.5f} vs {R['mult_pred']:.5f}", flush=True)
    expect(ok1, "f2(1): with small jumps the MPE price equals the closed-loop gain of the partial-equilibrium loop (0.5%) and the expected deviation grows by 1+d(Gamma_eq-1) (1e-4)")
    print("(g) f2(2): the paper's jumps (d=0.2), l=0 and l=0.5: amplification at parity, stability, the laggard's price")
    f2b = {}
    for (r, G, l) in [(1.0, 0.3, 0.0), (1.0, 0.6, 0.0), (1.5, 0.6, 0.0), (1.5, 0.6, 0.5), (1.5, 0.9, 0.0)]:
        R = f2_solve(r, G, d=0.2, l=l, N=400); f2b[(r, G, l)] = R
        print(f"   r={r} Gamma={G} l={l}: lambda formula {R['lam_formula']:.4f}, MPE {R['lam_mpe']:.4f} (x{R['lam_mpe']/R['lam_formula']:.2f}) | "
              f"Gamma_eq={R['G_eq']:.3f} Gamma~={R['G_t']:.3f} | E|s-1/2| after 60 periods from 0.52: MPE {R['Eabs']:.3f} vs structural lottery {R['Eabs_passive']:.3f} "
              f"(E-dev multiplier {R['mult']:.3f}) | laggard price at s=0.25: {R['lagg'][0]:.4f}, at 0.1: {R['lagg'][1]:.4f}", flush=True)
    expect(all(R['lam_mpe'] > R['lam_formula'] for R in f2b.values()), "f2(2): the equilibrium price at parity exceeds the fixed-strategy value in every case (x1.12 to x4.75)")
    expect(f2b[(1.0, 0.6, 0.0)]['G_eq'] > 1 and f2b[(1.0, 0.6, 0.0)]['mult'] > 1 and f2b[(1.0, 0.6, 0.0)]['Eabs'] > f2b[(1.0, 0.6, 0.0)]['Eabs_passive'],
           "f2(2): structural Gamma=0.6 < 1 yet Gamma_eq = 1.96 > 1: equal standing unstable in equilibrium, dispersion larger than under the structural lottery")
    expect(f2b[(1.5, 0.6, 0.5)]['lagg'][0] < 0 and all(R['lagg'][0] < R['lam_mpe'] for R in f2b.values()),
           "f2(2): far from parity the laggard's price falls (to below zero with shared loss): it stops contesting standing")
    # ---------------------------------------------------------------- (h) s2_mpe (Math-Opus reviewer): others fixed vs MPE
    def s2_run(r, Gamma, beta=0.0, Om=1.0, kap=0.5, d=0.2, c=1.0, l=0.0, delta=0.9, N=800, tol=1e-12, maxit=20000):
        om = Gamma / ((1 - beta) * r)
        k0 = kap * Om * (1 / om - 1) / 2; S = (kap * Om + 2 * k0) / d
        jump_w = (kap * (Om * (1 - beta) + Om * beta / 2) + k0) / S; jump_l = (kap * Om * beta / 2 + k0) / S
        grid = [i / N for i in range(N + 1)]
        def interp(arr, x):
            if x <= 0: return arr[0]
            if x >= 1: return arr[-1]
            k = min(int(x * N), N - 1); w = x * N - k
            return arr[k] * (1 - w) + arr[k + 1] * w
        def nxt(s): return (1 - d) * s + jump_w, (1 - d) * s + jump_l
        def stage(s, V):
            sw, sl = nxt(s)
            A1 = (1 - beta) * Om + delta * (interp(V, sw) - interp(V, sl))
            A2 = (1 - beta) * Om + delta * (interp(V, 1 - sl) - interp(V, 1 - sw))
            if s <= 0: a1, a2 = 0.0, 1.0
            elif s >= 1: a1, a2 = 1.0, 0.0
            else: a1, a2 = s ** r, (1 - s) ** r
            A1p, A2p = max(A1, 0.0), max(A2, 0.0)
            if a1 * A1p + a2 * A2p == 0: return 0.5, 0.0, 0.0, sw, sl
            p = a1 * A1p / (a1 * A1p + a2 * A2p)
            return p, A1p * p * (1 - p) / (c + l), A2p * p * (1 - p) / (c + l), sw, sl
        V = [0.0] * (N + 1)
        for it in range(maxit):
            Vn = []
            for s in grid:
                p, e1, e2, sw, sl = stage(s, V)
                Vn.append((1 - beta) * Om * p + beta * Om / 2 - c * e1 - l * (e1 + e2) + delta * (p * interp(V, sw) + (1 - p) * interp(V, sl)))
            diff = max(abs(a - b) for a, b in zip(V, Vn)); V = Vn
            if diff < tol: break
        p, e1, e2, sw, sl = stage(0.5, V)
        lam_mpe = delta * (interp(V, sw) - interp(V, sl)) / ((1 - beta) * Om)
        W = [0.0] * (N + 1)
        for it2 in range(maxit):
            Wn = []
            for s in grid:
                pp = 0.0 if s <= 0 else (1.0 if s >= 1 else s ** r / (s ** r + (1 - s) ** r))
                sw2, sl2 = nxt(s)
                Wn.append((1 - beta) * Om * pp + delta * (pp * interp(W, sw2) + (1 - pp) * interp(W, sl2)))
            dd = max(abs(a - b) for a, b in zip(W, Wn)); W = Wn
            if dd < tol: break
        sw2, sl2 = nxt(0.5)
        lam_fixed = delta * (interp(W, sw2) - interp(W, sl2)) / ((1 - beta) * Om)
        Gd = Gamma * delta * d / (1 - delta * (1 - d)); lam = Gd / (1 - Gd) if Gd < 1 else float('inf')
        return dict(lam=lam, lam_fixed=lam_fixed, lam_mpe=lam_mpe, Gd=Gd)
    print("(h) s2_mpe (Math-Opus reviewer): 'others fixed' (policy evaluation) vs MPE vs formula; the price under patience (s2b)")
    s2cases = ([(d, r, G) for d in (0.2, 0.05) for r in (1.0, 1.5) for G in (0.3, 0.6, 0.9, 1.2) if G / r <= 1] if FULL
               else [(0.2, 1.0, 0.6), (0.05, 1.0, 0.3)])
    okfix = True
    for (d, r, G) in s2cases:
        R = s2_run(r, G, d=d)
        if r == 1.0: okfix &= abs(R['lam_fixed'] - R['lam']) < 1e-3
        print(f"   d={d} r={r} Gamma={G}: Gd={R['Gd']:.3f} | lambda formula {R['lam']:.4f}, others fixed {R['lam_fixed']:.4f}, MPE {R['lam_mpe']:.4f} (MPE/formula {R['lam_mpe']/R['lam']:.3f})", flush=True)
    expect(okfix, "s2_mpe: with others' strategies fixed (r=1), the exact finite-jump price equals Gd/(1-Gd): the premise, not the jumps, drives the amplification")
    Rp = s2_run(1.5, 0.6, d=0.2, delta=0.97)
    print(f"   s2b patience: r=1.5 Gamma=0.6 d=0.2 delta=0.97: formula {Rp['lam']:.4f}, others fixed {Rp['lam_fixed']:.4f}, MPE {Rp['lam_mpe']:.4f} (ratio {Rp['lam_mpe']/Rp['lam']:.2f})")
    expect(Rp['lam_mpe'] / Rp['lam'] > 7, f"s2b: the amplification reaches x{Rp['lam_mpe']/Rp['lam']:.2f} at delta=0.97 (range quoted: about 1.05 to 7.9)")
    if FULL:
        for kw in (dict(r=0.5, Gamma=0.45, d=0.2), dict(r=0.5, Gamma=0.45, d=0.05), dict(r=1.5, Gamma=0.6, d=0.2, beta=0.5),
                   dict(r=1.5, Gamma=0.6, d=0.2, l=0.5), dict(r=1.5, Gamma=0.6, d=0.2, delta=0.5), dict(r=1.5, Gamma=0.6, d=0.2, N=1600)):
            kw = dict(kw); r = kw.pop('r'); G = kw.pop('Gamma'); R = s2_run(r, G, **kw)
            print(f"   s2b r={r} Gamma={G} {kw}: formula {R['lam']:.4f} fixed {R['lam_fixed']:.4f} MPE {R['lam_mpe']:.4f} ratio {R['lam_mpe']/R['lam']:.3f}", flush=True)
    # ---------------------------------------------------------------- (i) adv_checks.py section 3: tug-of-war, effort lives at parity
    print("(i) adv_checks section 3 (Adv-O reviewer): tug-of-war MPE (Tullock r=1 per step, absorbing at +/-K): total effort by state relative to parity")
    def tug(K, delta, iters=20000):
        S = list(range(-K, K + 1)); V1 = {s: 0.0 for s in S}; V2 = {s: 0.0 for s in S}
        V1[K], V2[K] = 1.0, 0.0; V1[-K], V2[-K] = 0.0, 1.0; x1 = {}; x2 = {}
        for _ in range(iters):
            diff = 0.0
            for s in range(-K + 1, K):
                v1 = delta * (V1[s + 1] - V1[s - 1]); v2 = delta * (V2[s - 1] - V2[s + 1])
                v1 = max(v1, 1e-15); v2 = max(v2, 1e-15)
                a = v1 * v1 * v2 / (v1 + v2) ** 2; b = v1 * v2 * v2 / (v1 + v2) ** 2; p = v1 / (v1 + v2)
                n1 = p * delta * V1[s + 1] + (1 - p) * delta * V1[s - 1] - a
                n2 = p * delta * V2[s + 1] + (1 - p) * delta * V2[s - 1] - b
                diff = max(diff, abs(n1 - V1[s]), abs(n2 - V2[s])); V1[s], V2[s] = n1, n2; x1[s], x2[s] = a, b
            if diff < 1e-13: break
        return x1, x2
    oktug = True
    for K, delta in ((3, 0.95), (5, 0.95), (5, 0.99)):
        x1, x2 = tug(K, delta); tot0 = x1[0] + x2[0]
        rel = [(x1[s] + x2[s]) / tot0 for s in range(0, K)]; oktug &= all(v <= 1 + 1e-12 for v in rel)
        print(f"   K={K} delta={delta}: " + "  ".join(f"s={s:+d}:{rel[s]:.3f}" for s in range(0, K)) + "   laggard effort/parity: "
              + "  ".join(f"{x2[s]/x2[0]:.3f}" for s in range(0, K)))
    expect(oktug, "tug-of-war: total effort is highest at parity and falls with the lead (near parity the price of standing is highest)")
    if FULL:
        # s2d / s2e (Math-Opus reviewer): Gamma_eq at delta 0.9 and 0.97; finite-difference robustness
        for (r, G) in ((1.0, 0.6), (1.5, 0.6), (1.5, 0.9), (1.0, 0.9)):
            for delta in (0.9, 0.97):
                R = f2_solve(r, G, d=0.2, delta=delta, N=800, mc=False)
                print(f"   s2d r={r} Gamma={G} delta={delta}: dp/ds at parity {R['p_eq']:.3f} vs r = {r}; Gamma_eq = {R['G_eq']:.3f}", flush=True)
        # s2c_profile (Math-Opus reviewer, ported; --full only): the price of standing away from parity, MPE and others fixed
        print("(j) [--full] s2c_profile (Math-Opus reviewer): lambda by state s, MPE vs others fixed (r=1.5, d=0.2, delta=0.9, N=800)")
        def s2c_profile(r, G, d=0.2, delta=0.9, N=800):
            om = G / r; kap = 0.5; Om = 1.0; k0 = kap * Om * (1 / om - 1) / 2; S = (kap * Om + 2 * k0) / d
            jw = (kap * Om + k0) / S; jl = k0 / S
            grid = [i / N for i in range(N + 1)]
            def interp(a, x):
                if x <= 0: return a[0]
                if x >= 1: return a[-1]
                k = min(int(x * N), N - 1); w = x * N - k; return a[k] * (1 - w) + a[k + 1] * w
            V = [0.0] * (N + 1)
            for it in range(5000):
                Vn = []
                for s in grid:
                    sw, sl = (1 - d) * s + jw, (1 - d) * s + jl
                    A1 = Om + delta * (interp(V, sw) - interp(V, sl)); A2 = Om + delta * (interp(V, 1 - sl) - interp(V, 1 - sw))
                    a1, a2 = (s ** r, (1 - s) ** r) if 0 < s < 1 else ((0.0, 1.0) if s <= 0 else (1.0, 0.0))
                    A1p, A2p = max(A1, 0), max(A2, 0); den = a1 * A1p + a2 * A2p
                    p = a1 * A1p / den if den > 0 else 0.5; e1 = A1p * p * (1 - p)
                    Vn.append(Om * p - e1 + delta * (p * interp(V, sw) + (1 - p) * interp(V, sl)))
                diff = max(abs(a - b) for a, b in zip(V, Vn)); V = Vn
                if diff < 1e-12: break
            W = [0.0] * (N + 1)
            for it in range(5000):
                Wn = []
                for s in grid:
                    pp = s ** r / (s ** r + (1 - s) ** r) if 0 < s < 1 else (0.0 if s <= 0 else 1.0)
                    sw, sl = (1 - d) * s + jw, (1 - d) * s + jl
                    Wn.append(Om * pp + delta * (pp * interp(W, sw) + (1 - pp) * interp(W, sl)))
                diff = max(abs(a - b) for a, b in zip(W, Wn)); W = Wn
                if diff < 1e-12: break
            Gd = G * delta * d / (1 - delta * (1 - d)); lam = Gd / (1 - Gd)
            print(f"   r={r} Gamma={G}: formula lambda at s=1/2 = {lam:.3f}", flush=True)
            for s in (0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9):
                sw, sl = (1 - d) * s + jw, (1 - d) * s + jl
                lm = delta * (interp(V, sw) - interp(V, sl)) / Om; lf = delta * (interp(W, sw) - interp(W, sl)) / Om
                print(f"      s={s}: lambda_fixed={lf:.3f} lambda_MPE={lm:.3f}  theta(n=2): fixed {-lf/(2+lf):+.3f}, MPE {-lm/(2+lm):+.3f}")
        s2c_profile(1.5, 0.9); s2c_profile(1.5, 1.2)
        # s2e_check (Math-Opus reviewer, ported; --full only): finite-difference robustness of Gamma_eq; dispersion MPE vs passive
        print("(k) [--full] s2e_check (Math-Opus reviewer): r=1.5, Gamma=0.6, d=0.2, delta=0.9, N=1600")
        r, G, d, delta, N = 1.5, 0.6, 0.2, 0.9, 1600
        om = G / r; kap = 0.5; Om = 1.0; k0 = kap * Om * (1 / om - 1) / 2; S = (kap * Om + 2 * k0) / d
        jw = (kap * Om + k0) / S; jl = k0 / S; grid = [i / N for i in range(N + 1)]
        def interp(a, x):
            if x <= 0: return a[0]
            if x >= 1: return a[-1]
            k = min(int(x * N), N - 1); w = x * N - k; return a[k] * (1 - w) + a[k + 1] * w
        def stage(s, V):
            sw, sl = (1 - d) * s + jw, (1 - d) * s + jl
            A1 = Om + delta * (interp(V, sw) - interp(V, sl)); A2 = Om + delta * (interp(V, 1 - sl) - interp(V, 1 - sw))
            a1, a2 = (s ** r, (1 - s) ** r) if 0 < s < 1 else ((0.0, 1.0) if s <= 0 else (1.0, 0.0))
            A1p, A2p = max(A1, 0), max(A2, 0); den = a1 * A1p + a2 * A2p
            p = a1 * A1p / den if den > 0 else 0.5
            return p, A1p * p * (1 - p), A2p * p * (1 - p), sw, sl
        V = [0.0] * (N + 1)
        for it in range(5000):
            Vn = []
            for s in grid:
                p, e1, e2, sw, sl = stage(s, V); Vn.append(Om * p - e1 + delta * (p * interp(V, sw) + (1 - p) * interp(V, sl)))
            diff = max(abs(a - b) for a, b in zip(V, Vn)); V = Vn
            if diff < 1e-12: break
        for h in (0.0025, 0.01, 0.02, 0.05):
            dp = (stage(0.5 + h, V)[0] - stage(0.5 - h, V)[0]) / (2 * h); print(f"   h={h}: dp/ds={dp:.3f}; Gamma_eq={G*dp/r:.3f}")
        s = 0.52
        for t in range(40):
            p, _, _, sw, sl = stage(s, V); s = p * sw + (1 - p) * sl
        print("   expected-share path from 0.52 after 40 periods:", round(s, 3))
        def simul(policy, T=100, R=2000, seed=1):
            rnd_ = random.Random(seed); out = []
            for _ in range(R):
                s = 0.5
                for t in range(T):
                    p = stage(s, V)[0] if policy == 'mpe' else s ** r / (s ** r + (1 - s) ** r)
                    sw, sl = (1 - d) * s + jw, (1 - d) * s + jl; s = sw if rnd_.random() < p else sl
                out.append(abs(s - 0.5))
            out.sort(); return sum(out) / R, out[int(0.9 * R)]
        print("   mean |s-1/2|, 90th pct after 100 periods: MPE", [round(x, 3) for x in simul('mpe')], " passive", [round(x, 3) for x in simul('passive')])


# ---------------------------------------------------------------------------------------------------------------------
# Codex's boundary cases (../v6.1/reviews/counterexamples_v61_codex.py). Plan s7 requires each of the eight to appear in
# some block; _codex() records where each one ran, and the run ends with the index (entries 2 and 10 are extra).
_CODEX = {}
_CODEX_NAMES = {1: 'Gamma_delta >= 1', 2: 'decay raises the loop gain (ratio channel with diffusion)', 3: 'cap equality',
                4: 'positive diffusion restores without provision', 5: 'falling positive per-unit floor f',
                6: 'unequal compliance costs (incidence)', 7: 'stochastic punishment asymmetry', 8: 'p < 1 in delegation',
                9: 'nonlinear fitness', 10: 'provision raises the common-channel weight (Test Gamma sign)'}
# Codex's own numbering: 1 price outside convergence; 2 decay; 3a cap equality; 3b diffusion; 4 falling f; 5 unequal
# costs; 6 targeted continuation; 7 delegation p<1; 8 nonlinear fitness; 9 provision sign. Mapped above to 1..10.
def _codex(k, ok):
    _CODEX[k] = (_CURRENT['block'], bool(ok))


# m03 machinery (planning/math-opus/m03_channels.py, ported verbatim; used by CH and TD)
def _m03_relmode_multiplier(n, chans, beta=0.0, Om=1.0, T=400, eps=1e-7):
    m = len(chans)
    Xs = []
    for c in chans:
        Xs.append((c['kap'] * Om / n + c['k0']) / c['d'])
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
        dev = math.sqrt(sum((Xn[i][j] - Xs[j]) ** 2 / Xs[j] ** 2 for i in range(n) for j in range(m)))
        dev0 = math.sqrt(sum((X[i][j] - Xs[j]) ** 2 / Xs[j] ** 2 for i in range(n) for j in range(m)))
        fac = dev / dev0
        X = [[Xs[j] + (Xn[i][j] - Xs[j]) * eps / dev for j in range(m)] for i in range(n)]
    return fac
def _m03_gamma_formula(n, chans, beta=0.0, Om=1.0, h=1e-6):
    G = 0.0
    for c in chans:
        X = (c['kap'] * Om / n + c['k0']) / c['d']
        r = (c['h'](X * (1 + h)) - c['h'](X * (1 - h))) / (2 * h)
        w = c['kap'] * Om / (c['kap'] * Om + n * c['k0'])
        G += (1 - beta) * r * w * c['d'] / (c['d'] + c['df'])
    return G

# f3 machinery (planning/math-fable/f3_compound.py, ported verbatim; used by CH and TD)
def _f3_spectral_radius_dev(step, Xs, n, m, h=1e-6):
    J = [[0.0] * m for _ in range(m)]
    for col in range(m):
        S = [list(Xs) for _ in range(n)]
        S[0][col] += h
        for i in range(1, n): S[i][col] -= h / (n - 1)
        S2 = step(S)
        for row in range(m): J[row][col] = (S2[0][row] - Xs[row]) / h
    v = [1.0] * m; lam = 0.0
    for _ in range(3000):
        w = [sum(J[i][k] * v[k] for k in range(m)) + 2 * v[i] for i in range(m)]
        nrm = math.sqrt(sum(x * x for x in w)); v = [x / nrm for x in w]; lam = nrm
    return lam - 2


def check_CH():
    block('CH', 'loopgain, chansign (S2), delayosc (S2), gammarange (S2)', 'independent (the last part, (h), derived)',
          'Which levers lower the loop gain, channel by channel: correction and provision by the level elasticity xi_r; '
          'sharing and diffusion in every channel; three stocks; a delayed countervailing channel')
    # Sources (ported): planning/math-opus/m03_channels.py (A,B,D); planning/math-fable/f3_compound.py (B);
    # ../v6.1/reviews/counterexamples_v61_codex.py case 2; ../v6.1/reviews/scripts-v6.1-systems/s1_loopgain.py (a),(a'),(d);
    # ../v6.1/reviews/scripts-v6.1-math-fable/m1_loopgain.py (A),(A'),(B); ../v6.1/reviews/scripts-v6.1-math-opus/s1_loopgain.py;
    # ../v6.1/reviews/scripts-v6.1-adv-opus/adv_checks.py section 1 (illustrative ranges, derived).
    # Claims (D2-opus s4, plan s1 item 2): correction (raising d_j) changes Gamma with the sign of df/(d+df) - xi_r;
    # provision k0 lowers it iff xi_r < 1; sharing and diffusion lower it in every channel; Gamma_delta of a ratio
    # channel rises with d even without diffusion; a delayed countervailing channel can oscillate below net gain 1.
    sgn = lambda v, tol: '+' if v > tol else ('-' if v < -tol else '0')
    print("(a) m03(A,B): sign of dGamma/dd and of dGamma/dk0 by channel form; Gamma read off the simulated relative-mode growth factor")
    forms = {
        'ratio  r ln X (xi_r=0)': (lambda X: 1.8 * math.log(X), 0.0),
        'level  a X    (xi_r=1)': (lambda X: 0.9 * X, 1.0),
        'power  a X^.5 (xi_r=.5)': (lambda X: 1.5 * X ** 0.5, 0.5),
        'power  a X^2  (xi_r=2)': (lambda X: 0.4 * X ** 2, 2.0),
        'saturating ln(1+X)': (lambda X: 2.5 * math.log(1 + X), None),
    }
    okA = True; okF = True; rowsA = []
    for name, (h, er) in forms.items():
        for df in (0.0, 0.1):
            base = dict(h=h, kap=0.5, d=0.2, df=df, k0=0.1)
            def G_at(**kw):
                c = dict(base); c.update(kw); return _m03_gamma_formula(2, [c]), _m03_relmode_multiplier(2, [c])
            g1, m1 = G_at(d=0.2); g2, m2 = G_at(d=0.3); g3, m3 = G_at(k0=0.2)
            gam_sim = lambda m, d: (m - 1) / (d + df) + 1
            Gs1, Gs2, Gs3 = gam_sim(m1, 0.2), gam_sim(m2, 0.3), gam_sim(m3, 0.2)
            X = (0.5 / 2 + 0.1) / 0.2
            if er is None:
                hh = 1e-4
                r_of = lambda X: (h(X * (1 + hh)) - h(X * (1 - hh))) / (2 * hh)
                er = (math.log(r_of(X * 1.001)) - math.log(r_of(X / 1.001))) / (2 * math.log(1.001))
            pred_d = df / (0.2 + df) - er
            rule_d = sgn(pred_d, 1e-12); rule_k = sgn(-(er - 1), 1e-9)   # dGamma/dk0 has the sign of (xi_r - 1)... lowers iff xi_r<1
            obs_d = sgn(Gs2 - Gs1, 1e-4); obs_k = sgn(Gs3 - Gs1, 1e-4)
            okA &= (obs_d == rule_d) and ({'+': '-', '-': '+', '0': '0'}[obs_k] == rule_k)
            okF &= abs(Gs1 - g1) < 1e-3 and abs(Gs2 - g2) < 1e-3 and abs(Gs3 - g3) < 1e-3
            rowsA.append((name, df, Gs1, Gs2, Gs3))
            print(f"   {name:26s} df={df}: Gamma sim {Gs1:.4f} -> {Gs2:.4f} when d .2->.3 (formula {g1:.4f}->{g2:.4f}); "
                  f"rule sign(df/(d+df)-xi_r)={rule_d} (xi_r={er:.2f}), observed {obs_d} | k0 .1->.2: Gamma sim {Gs1:.4f} -> {Gs3:.4f}; "
                  f"provision lowers iff xi_r<1: observed change {obs_k}")
    expect(okA, "m03(A,B): every simulated sign agrees with the rule (correction: sign of df/(d+df)-xi_r; provision: lowers iff xi_r<1, none at xi_r=1) in 10/10 settings")
    expect(okF, "m03(A,B): Gamma read off the nonlinear relative-mode factor equals formula (2) to 1e-3 in every setting")
    gdel = [1.8 * 1.0 * 0.9 * d / (1 - 0.9 * (1 - d)) for d in (0.1, 0.2, 0.4)]
    print("   Gamma_delta, ratio channel, no diffusion, delta=0.9: " + "  ".join(f"d={d}: {g:.4f}" for d, g in zip((0.1, 0.2, 0.4), gdel))
          + "  (rises with d although Gamma = 1.8*omega is unchanged)")
    expect(gdel[0] < gdel[1] < gdel[2], f"Gamma_delta of a ratio channel rises with d without diffusion ({gdel[0]:.4f}, {gdel[1]:.4f}, {gdel[2]:.4f})")
    print("(b) f3(B): sign of d by channel form (n=2, kap*Om=1, k0=0.2, df=0.1): numerical spectral radius of the deviation map")
    n, Om, kap, k0, df, beta = 2, 1.0, 1.0, 0.2, 0.1, 0.0
    okB = True; Gs = {'ratio': [], 'level': []}
    for form in ("ratio", "level"):
        for d in (0.1, 0.2, 0.3, 0.6):
            Xs = (kap * Om / n + k0) / d
            def step(S, d=d, form=form):
                if form == "ratio": s = [2.0 * math.log(S[i][0]) for i in range(n)]
                else: s = [1.2 * S[i][0] for i in range(n)]
                mx = max(s); e = [math.exp(t - mx) for t in s]; Z = sum(e); p = [t / Z for t in e]
                m = sum(S[i][0] for i in range(n)) / n
                return [[(1 - d) * S[i][0] + kap * Om * ((1 - beta) * p[i] + beta / n) + k0 - df * (S[i][0] - m)] for i in range(n)]
            rj = 2.0 if form == "ratio" else 1.2 * Xs
            om = kap * Om / (kap * Om + n * k0)
            G = (1 - beta) * rj * om * d / (d + df)
            rho = _f3_spectral_radius_dev(step, [Xs], n, 1)
            okB &= (rho < 1) == (G < 1); Gs[form].append(G)
            print(f"   {form}-form, d={d}: r_j={rj:.3f} Gamma={G:.3f} spectral radius={rho:.4f} -> {'stable' if rho<1 else 'UNSTABLE'}")
    expect(okB and all(a < b for a, b in zip(Gs['ratio'], Gs['ratio'][1:])) and all(a > b for a, b in zip(Gs['level'], Gs['level'][1:])),
           "f3(B): stable iff Gamma<1 in 8/8; faster depreciation raises Gamma of a ratio-form stock with diffusion (0.71->1.22), correction lowers a level-form stock's (3.00->0.86)")
    # ---------------------------------------------------------------- Codex case 2
    def gains(r, decay, diffusion, discount=0.9, won_share=1.0):
        G = r * won_share * decay / (decay + diffusion)
        Gd = r * won_share * discount * decay / (1 - discount * (1 - decay - diffusion))
        return G, Gd
    before = gains(1.8, 0.1, 0.1); after = gains(1.8, 0.2, 0.1)
    print(f"(c) Codex case 2: r=1.8, df=0.1: d=0.1 -> (Gamma, Gamma_delta) = ({before[0]:.4f}, {before[1]:.4f}); d=0.2 -> ({after[0]:.4f}, {after[1]:.4f})")
    ok2 = before[0] < 1 < after[0] and before[1] < after[1] < 1
    expect(ok2, "Codex 2: raising the decay rate of a log-strength stock raises Gamma across 1 and raises Gamma_delta")
    _codex(2, ok2)
    # ---------------------------------------------------------------- systems s1 (a), (a'), (d) (ported)
    import cmath
    def s1_step(X, d, kO, beta, k0, df, sig):
        n = len(X); s = [sig(x) for x in X]; m = max(s); w = [math.exp(v - m) for v in s]; S = sum(w); p = [v / S for v in w]
        Xb = sum(X) / n
        return [(1 - d) * X[i] + kO * ((1 - beta) * p[i] + beta / n) + k0 - df * (X[i] - Xb) for i in range(n)]
    def jac_dev_eig(d, kO, beta, k0, df, sig, h=1e-7):
        Xs = (kO / 2 + k0) / d
        X = [Xs, Xs]
        base = s1_step(X, d, kO, beta, k0, df, sig)
        J = [[0, 0], [0, 0]]
        for j in range(2):
            Xp = list(X); Xp[j] += h
            f = s1_step(Xp, d, kO, beta, k0, df, sig)
            for i in range(2): J[i][j] = (f[i] - base[i]) / h
        tr = J[0][0] + J[1][1]; det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        disc = cmath.sqrt(tr * tr - 4 * det)
        ev = [(tr + disc) / 2, (tr - disc) / 2]
        return max(abs(e) for e in ev), Xs
    def sim_growth(d, kO, beta, k0, df, sig, T=400):
        Xs = (kO / 2 + k0) / d; X = [Xs * (1 + 1e-4), Xs * (1 - 1e-4)]
        g0 = abs(X[0] - X[1])
        for _ in range(T): X = s1_step(X, d, kO, beta, k0, df, sig)
        return abs(X[0] - X[1]) / g0
    kO, beta, k0, df = 1.0, 0.0, 0.2, 0.1
    print("(d) systems s1(a): ratio form sigma = r ln X, r=2; kappa*Omega=1, k0=0.2, delta_f=0.1, n=2")
    r = 2.0; omega = kO / (kO + 2 * k0); okS = True; Gprev = -1
    for d in (0.05, 0.1, 0.2, 0.3, 0.6, 0.9):
        rho, Xs = jac_dev_eig(d, kO, beta, k0, df, lambda x: r * math.log(x))
        G = (1 - beta) * r * omega * d / (d + df)
        gr = sim_growth(d, kO, beta, k0, df, lambda x: r * math.log(x))
        okS &= (rho > 1) == (G > 1) and (gr > 1) == (G > 1) and G > Gprev; Gprev = G
        print(f"   d={d:4.2f}: Gamma={G:.3f}  numerical spectral radius={rho:.4f}  deviation x{gr:.3g} after 400 periods  -> {'UNSTABLE' if rho>1 else 'stable'}")
    print("(d') systems s1(a'): difference form sigma = s X, s=1.2 (strength linear in the stock, like rule support)")
    s = 1.2; Gprev = 1e9
    for d in (0.05, 0.1, 0.2, 0.3, 0.6, 0.9):
        rho, Xs = jac_dev_eig(d, kO, beta, k0, df, lambda x: s * x)
        rj = s * Xs
        G = (1 - beta) * rj * omega * d / (d + df)
        okS &= (rho > 1) == (G > 1) and G < Gprev; Gprev = G
        print(f"   d={d:4.2f}: r_j=s X*={rj:.3f}  Gamma={G:.3f}  spectral radius={rho:.4f}  -> {'UNSTABLE' if rho>1 else 'stable'}")
    expect(okS, "systems s1(a,a'): spectral radius > 1 iff Gamma > 1 in 12/12; Gamma rises with d (ratio form, df>0) and falls with d (level form)")
    print("(e) m03(D) and systems s1(d): a delayed countervailing channel, net DC gain below one, growing oscillation [key delayosc]")
    D = [0.6, 0.95]; a = [0.5, -0.05]
    J = [[D[0] + a[0], a[1]], [a[0], D[1] + a[1]]]
    dc = sum(aj / (1 - Dj) for aj, Dj in zip(a, D))
    tr = J[0][0] + J[1][1]; det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
    disc = tr * tr - 4 * det
    mod = math.sqrt(det) if disc < 0 else max(abs((tr + math.sqrt(disc)) / 2), abs((tr - math.sqrt(disc)) / 2))
    period = 2 * math.pi / math.atan2(math.sqrt(-disc) / 2, tr / 2)
    y = [1.0, 0.0]
    for t in range(600):
        y = [J[0][0] * y[0] + J[0][1] * y[1], J[1][0] * y[0] + J[1][1] * y[1]]
    print(f"   net DC gain sum a_j/(1-D_j) = {dc:.3f} (<1); eigenvalue modulus {mod:.4f}; period {period:.1f}; |y| after 600 periods {math.hypot(*y):.1f}")
    expect(dc < 1 and mod > 1 and math.hypot(*y) > 100 and abs(mod - 1.0075) < 1e-4 and abs(period - 51.6) < 0.1,
           f"delayosc: net DC gain {dc:.2f} < 1 yet modulus {mod:.4f} > 1, period {period:.1f}, |y(600)| = {math.hypot(*y):.0f}: correction cannot be subtracted from Gamma")
    # ---------------------------------------------------------------- math-fable reviewer m1 (A),(A'),(B): three stocks, mixed forms
    def m1_make(P):
        n, r1, a, b, Om, beta, kap, k0, d, df = P
        def sigma(X):
            return r1 * math.log(X[0]) + a * X[1] + b * math.sqrt(X[2])
        def step(S):
            s = [sigma(X) for X in S]; mx = max(s)
            e = [math.exp(t - mx) for t in s]; Z = sum(e); p = [t / Z for t in e]
            W = [Om * ((1 - beta) * p[i] + beta / n) for i in range(n)]
            mean = [sum(S[i][j] for i in range(n)) / n for j in range(3)]
            return [[(1 - d[j]) * S[i][j] + kap[j] * W[i] + k0[j] - df[j] * (S[i][j] - mean[j]) for j in range(3)] for i in range(n)], W
        Xs = [(kap[j] * Om / n + k0[j]) / d[j] for j in range(3)]
        r = [r1, a * Xs[1], 0.5 * b * math.sqrt(Xs[2])]
        om = [kap[j] * Om / (kap[j] * Om + n * k0[j]) if kap[j] * Om + n * k0[j] > 0 else 0.0 for j in range(3)]
        G = (1 - beta) * sum(r[j] * om[j] * d[j] / (d[j] + df[j]) for j in range(3))
        return sigma, step, Xs, r, om, G
    def m1_perron(J, iters=4000):
        m = len(J); c = 1.0
        v = [1.0] * m; lam = 0.0
        for _ in range(iters):
            w = [sum(J[i][k] * v[k] for k in range(m)) + c * v[i] for i in range(m)]
            nrm = math.sqrt(sum(x * x for x in w)); v = [x / nrm for x in w]; lam = nrm
        return lam - c
    def m1_dev_jacobian(P, step, Xs, h=1e-6):
        n = P[0]
        J = [[0.0] * 3 for _ in range(3)]
        for col in range(3):
            S = [list(Xs) for _ in range(n)]
            S[0][col] += h
            for i in range(1, n): S[i][col] -= h / (n - 1)
            S2, _ = step(S)
            for row in range(3): J[row][col] = (S2[0][row] - Xs[row]) / h
        return J
    rnd = random.Random(1); mis = 0; near = 0; tested = 0; Nm1 = 3000
    for _ in range(Nm1):
        n = rnd.randint(2, 6); r1 = rnd.uniform(0.2, 2.5); a = rnd.uniform(0, 1.5); b = rnd.uniform(0, 2)
        Om = rnd.uniform(0.5, 3); beta = rnd.uniform(0, 0.8)
        kap = [rnd.uniform(0.05, 1), rnd.uniform(0, 0.5), rnd.uniform(0, 0.8)]
        k0 = [rnd.choice([0.0, rnd.uniform(0, 0.5)]) for _ in range(3)]
        d = [rnd.uniform(0.02, 0.6) for _ in range(3)]
        df = [rnd.choice([0.0, rnd.uniform(0, 0.3)]) for _ in range(3)]
        df = [min(df[j], 1 - d[j]) for j in range(3)]
        P = (n, r1, a, b, Om, beta, kap, k0, d, df)
        sigma, step, Xs, r, om, G = m1_make(P)
        if min(Xs) <= 1e-9: continue
        J = m1_dev_jacobian(P, step, Xs)
        rho = m1_perron(J)
        if abs(G - 1) < 2e-3: near += 1; continue
        tested += 1
        if (rho > 1) != (G > 1): mis += 1
    print(f"(f) m1(A) (Math-Fable reviewer): three stocks, sigma = r1 ln X1 + a X2 + b sqrt(X3): {tested} systems, Perron root > 1 <=> Gamma > 1 mismatches: {mis} (skipped {near} near the boundary)")
    expect(mis == 0, f"m1(A): three stocks with ratio, linear and square-root channels: Perron root > 1 iff Gamma > 1 in {tested}/{tested}")
    print("   m1(A'): nonlinear simulation, three stocks, deviation 1e-4 for 3000 periods:")
    base = dict(n=4, Om=1.0, beta=0.0, kap=[0.5, 0.2, 0.3], k0=[0.0, 0.0, 0.1], d=[0.05, 0.2, 0.1], df=[0.0, 0.0, 0.05])
    okAp = True
    for (r1, a, b) in [(1.2, 0.0, 0.0), (0.7, 0.8, 0.0), (0.7, 0.0, 1.5), (0.5, 0.3, 0.6), (0.9, 0.6, 0.8)]:
        P = (base['n'], r1, a, b, base['Om'], base['beta'], base['kap'], base['k0'], base['d'], base['df'])
        sigma, step, Xs, r, om, G = m1_make(P)
        n = P[0]
        S = [list(Xs) for _ in range(n)]
        S[0][0] *= 1 + 1e-4
        for i in range(1, n): S[i][0] *= 1 - 1e-4 / (n - 1)
        for _ in range(3000): S, W = step(S)
        gap = (max(x[0] for x in S) - min(x[0] for x in S)) / Xs[0]
        okAp &= (gap > 2e-4) == (G > 1)
        print(f"   r1={r1}, a={a}, b={b}: r_j={[round(x,3) for x in r]}, omega={[round(x,3) for x in om]}, Gamma={G:.3f} -> gap {gap:.2e} ({'grows' if gap > 2e-4 else 'decays'})")
    expect(okAp, "m1(A'): the nonlinear gap grows iff Gamma > 1 in 5/5 (channels each too weak to open the loop open it together: Gamma 1.201)")
    rnd = random.Random(2); worst = 0.0; cnt = 0
    for _ in range(200):
        n = rnd.randint(2, 5); r1 = rnd.uniform(0.2, 2); a = rnd.uniform(0, 1); b = rnd.uniform(0, 1.5)
        Om = rnd.uniform(0.5, 2); beta = rnd.uniform(0, 0.7)
        kap = [rnd.uniform(0.05, 1), rnd.uniform(0, 0.5), rnd.uniform(0, 0.6)]
        k0 = [rnd.uniform(0, 0.4) for _ in range(3)]
        d = [rnd.uniform(0.05, 0.6) for _ in range(3)]
        df = [rnd.uniform(0, 0.2) for _ in range(3)]; df = [min(df[j], 1 - d[j]) for j in range(3)]
        dl = rnd.uniform(0.5, 0.97)
        P = (n, r1, a, b, Om, beta, kap, k0, d, df)
        sigma, step, Xs, r, om, G = m1_make(P)
        Gd = (1 - beta) * sum(r[j] * om[j] * dl * d[j] / (1 - dl * (1 - d[j] - df[j])) for j in range(3))
        if G >= 1 or Gd > 0.9: continue
        lam = Gd / (1 - Gd)
        x = 1e-6
        S = [list(Xs) for _ in range(n)]
        _, W0 = step(S); base_ = W0[0]
        S[0] = [Xs[j] + kap[j] * x for j in range(3)]
        pv = 0.0; disc = dl
        T = int(math.log(1e-13) / math.log(dl * max(0.5, 1 - min(d)))) + 100
        for _ in range(T):
            S, W = step(S); pv += disc * (W[0] - base_); disc *= dl
        est = pv / (x * (n - 1) / n)
        worst = max(worst, abs(est - lam) / max(1e-9, lam)); cnt += 1
    print(f"   m1(B): price of standing on the three-stock model: {cnt} systems with Gamma<1, Gd<0.9: max relative error of PV vs Gd/(1-Gd) {worst:.2e}")
    expect(worst < 1e-5, f"m1(B): the price of standing equals Gamma_delta/(1-Gamma_delta) on three mixed stocks ({cnt} systems, max rel. error {worst:.1e})")
    # ---------------------------------------------------------------- math-opus reviewer s1_loopgain (ported)
    def s1_makeP(n, m, rnd):
        P = dict(n=n, m=m)
        P['beta'] = rnd.uniform(0, 0.8)
        P['Om'] = rnd.uniform(0.5, 3)
        P['kap'] = [rnd.uniform(0.02, 1.0) for _ in range(m)]
        P['k0'] = [rnd.choice([0.0, rnd.uniform(0, 0.6)]) for _ in range(m)]
        P['d'] = [rnd.uniform(0.03, 0.9) for _ in range(m)]
        P['df'] = [rnd.choice([0.0, rnd.uniform(0, 1 - P['d'][j])]) for j in range(m)]
        P['kind'] = [rnd.choice(['log', 'lin']) for _ in range(m)]
        P['coef'] = [rnd.uniform(0, 2.5) for _ in range(m)]
        return P
    def s1_steady(P):
        n = P['n']
        return [(P['kap'][j] * P['Om'] / n + P['k0'][j]) / P['d'][j] for j in range(P['m'])]
    def s1_sigma(P, x):
        s = 0.0
        for j in range(P['m']):
            if P['kind'][j] == 'log': s += P['coef'][j] * math.log(x[j])
            else: s += P['coef'][j] * x[j]
        return s
    def s1_stepP(P, X):
        n, m = P['n'], P['m']
        sg = [s1_sigma(P, X[i]) for i in range(n)]
        mx = max(sg); e = [math.exp(t - mx) for t in sg]; S = sum(e); p = [t / S for t in e]
        mean = [sum(X[i][j] for i in range(n)) / n for j in range(m)]
        Y = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append((1 - P['d'][j]) * X[i][j] + P['kap'][j] * P['Om'] * ((1 - P['beta']) * p[i] + P['beta'] / n)
                           + P['k0'][j] - P['df'][j] * (X[i][j] - mean[j]))
            Y.append(row)
        return Y, p
    def s1_gamma(P, delta=None):
        n, m = P['n'], P['m']; Xs = s1_steady(P); G = 0.0
        for j in range(m):
            rj = P['coef'][j] if P['kind'][j] == 'log' else P['coef'][j] * Xs[j]
            om = P['kap'][j] * P['Om'] / (P['kap'][j] * P['Om'] + n * P['k0'][j])
            if delta is None: G += (1 - P['beta']) * rj * om * P['d'][j] / (P['d'][j] + P['df'][j])
            else: G += (1 - P['beta']) * rj * om * delta * P['d'][j] / (1 - delta * (1 - P['d'][j] - P['df'][j]))
        return G
    def s1_spectral(P, h=1e-7, iters=3000):
        n, m = P['n'], P['m']; Xs = s1_steady(P)
        base = [[Xs[j] for j in range(m)] for _ in range(n)]
        rr = random.Random(1)
        v = [[rr.uniform(-1, 1) for j in range(m)] for i in range(n)]
        def proj(v):
            mu = [sum(v[i][j] for i in range(n)) / n for j in range(m)]
            return [[v[i][j] - mu[j] for j in range(m)] for i in range(n)]
        def norm(v): return math.sqrt(sum(t * t for r_ in v for t in r_))
        v = proj(v); nv = norm(v); v = [[t / nv for t in r_] for r_ in v]
        lam = 0.0
        for it in range(iters):
            X = [[base[i][j] + h * v[i][j] for j in range(m)] for i in range(n)]
            Y, _ = s1_stepP(P, X)
            w = [[(Y[i][j] - base[i][j]) / h for j in range(m)] for i in range(n)]
            w = proj(w); nw = norm(w)
            if nw == 0: return 0.0
            lam_new = nw
            v = [[t / nw for t in r_] for r_ in w]
            if it > 200 and abs(lam_new - lam) < 1e-10: lam = lam_new; break
            lam = lam_new
        return lam
    def s1_pv(P, delta, x=1e-7, T=None):
        n, m = P['n'], P['m']; Xs = s1_steady(P)
        X = [[Xs[j] + (P['kap'][j] * x if i == 0 else -P['kap'][j] * x / (n - 1)) for j in range(m)] for i in range(n)]
        base_W = P['Om'] / n
        pv = 0.0; disc = delta
        if T is None: T = 6000
        for t in range(T):
            sg = [s1_sigma(P, X[i]) for i in range(n)]
            mx = max(sg); e = [math.exp(s_ - mx) for s_ in sg]; S = sum(e); p = [s_ / S for s_ in e]
            W0 = P['Om'] * ((1 - P['beta']) * p[0] + P['beta'] / n)
            pv += disc * (W0 - base_W); disc *= delta
            X, _ = s1_stepP(P, X)
            if disc < 1e-16: break
        return pv / x
    rnd = random.Random(2026)
    mis = 0; near = 0; Ns1 = 1500
    for k in range(Ns1):
        n = rnd.randint(2, 5); m = rnd.randint(1, 3)
        P = s1_makeP(n, m, rnd)
        G = s1_gamma(P)
        if abs(G - 1) < 0.02: near += 1; continue
        rad = s1_spectral(P)
        if (rad > 1) != (G > 1): mis += 1
    print(f"(g) s1 (Math-Opus reviewer): Prop 2.2(1): {Ns1} random systems (1-3 channels, log/linear entry, k0, diffusion): mismatches {mis}, skipped near boundary {near}"
          )
    expect(mis == 0, f"s1: power iteration on the sum-zero subspace agrees with Gamma>1 in every one of {Ns1-near} systems")
    worst = 0; cnt = 0
    for k in range(300):
        n = rnd.randint(2, 5); m = rnd.randint(1, 3)
        P = s1_makeP(n, m, rnd)
        if s1_gamma(P) >= 0.95: continue
        dl = rnd.uniform(0.3, 0.97)
        Gd = s1_gamma(P, dl)
        lam = Gd / (1 - Gd)
        pv = s1_pv(P, dl)
        cnt += 1
        err = abs(pv - lam) / max(1e-9, abs(lam)) if lam > 1e-6 else abs(pv - lam)
        worst = max(worst, err)
    print(f"   Prop 2.2(3): {cnt} systems with Gamma<0.95: max relative error of PV vs Gd/(1-Gd) = {worst:.2e}")
    expect(worst < 1e-5, f"s1: the price of standing equals Gd/(1-Gd) in {cnt} systems with up to three channels (max rel. error {worst:.1e})")
    viol = 0
    for k in range(2000):
        P = s1_makeP(rnd.randint(2, 5), rnd.randint(1, 3), rnd)
        G = s1_gamma(P)
        for dl in (0.1, 0.5, 0.9, 0.999):
            if s1_gamma(P, dl) > G + 1e-12: viol += 1
    print(f"   Gamma_delta <= Gamma violations: {viol}")
    expect(viol == 0, "s1: Gamma_delta <= Gamma in 2,000 random systems at four discount factors")
    print("   finite perturbations when Gamma>1 but Gd<1: PV per unit y vs first-order lambda")
    P = dict(n=2, m=1, beta=0.0, Om=1.0, kap=[0.5], k0=[0.0], d=[0.2], df=[0.0], kind=['log'], coef=[1.5])
    for dl in (0.7, 0.8, 0.85):
        Gd = s1_gamma(P, dl); lam = Gd / (1 - Gd)
        out = [f"x={x}: {s1_pv(P, dl, x=x):.3f}" for x in (1e-6, 1e-3, 1e-2, 0.05, 0.2)]
        print(f"     Gamma={s1_gamma(P):.2f}, delta={dl}: Gd={Gd:.3f}, lambda={lam:.3f}; " + "; ".join(out))
    # ---------------------------------------------------------------- (h) adv_checks section 1 [derived]: illustrative ranges, Gamma not estimated
    print("(h) [derived] adv_checks s1 (Adv-O reviewer), key gammarange: decisiveness r* that a single channel needs for Gamma=1 (beta=0, omega=1)")
    for dfx in (0.05, 0.10):
        row = []
        for d in (0.01, 0.02, 0.03, 0.05, 0.10):
            ratio = d / (d + dfx); row.append(f"d={d:.2f}: r*={1/ratio:.2f}")
        print(f"   delta_f={dfx:.2f}/month: " + "  ".join(row))
    print("   (Remark 8.6 uses delta_f = 0.1/month for a lead diffusing; no channel's Gamma is estimated anywhere in the paper)")


def check_TD():
    block('TD', 'tdec (S2), loopgain', 'independent; (c) derived (roots of the secular equation)',
          'Time to decisiveness: the gap multiplier 1+(d+df)(Gamma-1); Gamma sets the sign, turnover the speed; several channels: the Perron root')
    # Sources (ported): planning/math-fable/f3_compound.py (C); planning/math-opus/m03_channels.py (C);
    # ../v6.1/reviews/scripts-v6.1-systems/s1_loopgain.py (b),(c); ../v6.1/reviews/scripts-v6.1-math-fable/m6_misc.py (3).
    # Claims (D2-fable s5, D2-opus s2): a relative gap grows by Lambda* = 1+(d_K+df)(Gamma-1) a period (V6.1 omitted df);
    # with several channels by the Perron root of (S1), not a function of Gamma; T_dec ~ ln(gapbar/gap0)/ln Lambda*.
    print("(a) f3(C): exact growth factor of a single-channel gap (numerical Jacobian) vs 1+(dK+df)(Gamma-1) and vs V6.1's 1+dK(Gamma-1)")
    n, Om, kap, k0, beta = 2, 1.0, 1.0, 0.0, 0.0
    okA = True; differ = 0
    for (d, df, r) in [(0.2, 0.0, 3.0), (0.2, 0.1, 2.0), (0.05, 0.05, 3.0), (0.2, 0.3, 1.2)]:
        Xs = (kap * Om / n + k0) / d
        def step(S, d=d, df=df, r=r):
            s = [r * math.log(S[i][0]) for i in range(n)]
            mx = max(s); e = [math.exp(t - mx) for t in s]; Z = sum(e); p = [t / Z for t in e]
            m = sum(S[i][0] for i in range(n)) / n
            return [[(1 - d) * S[i][0] + kap * Om * p[i] + k0 - df * (S[i][0] - m)] for i in range(n)]
        om = 1.0; G = r * om * d / (d + df)
        rho = _f3_spectral_radius_dev(step, [Xs], n, 1)
        okA &= abs(rho - (1 + (d + df) * (G - 1))) < 1e-4
        differ += df > 0 and abs(rho - (1 + d * (G - 1))) > 1e-3
        print(f"   d={d} df={df} r={r}: Gamma={G:.3f}; exact multiplier {rho:.4f}; 1+(d+df)(Gamma-1)={1+(d+df)*(G-1):.4f}; text 1+d(Gamma-1)={1+d*(G-1):.4f}; "
              f"periods 1%->50%: exact {math.log(50)/math.log(rho):.1f}, text {math.log(50)/math.log(1+d*(G-1)) if 1+d*(G-1)>1 else float('inf'):.1f}")
    expect(okA and differ == 3, "f3(C): the exact multiplier is 1+(d+df)(Gamma-1) in 4/4 (1.4000, 1.1000, 1.0500, 0.7400); V6.1's 1+d(Gamma-1) is wrong in the 3 cases with diffusion")
    print("(b) m03(C): simulated factor of the nonlinear model vs 1+(d+df)(Gamma-1); time 1% -> 50% in the nonlinear model")
    okB = True; tnl = {}
    for (r, d, df) in ((3.0, 0.2, 0.0), (3.0, 0.05, 0.05), (2.0, 0.2, 0.1), (1.5, 0.1, 0.02)):
        c = dict(h=lambda X, r=r: r * math.log(X), kap=0.5, d=d, df=df, k0=0.0)
        G = _m03_gamma_formula(2, [c]); m = _m03_relmode_multiplier(2, [c])
        old = 1 + d * (G - 1); new = 1 + (d + df) * (G - 1)
        Xs = (0.5 / 2) / d
        X = [Xs * 1.01, Xs * 0.99]; t = 0
        while True:
            w = [x ** r for x in X]; p = [x / sum(w) for x in w]; mean = sum(X) / 2
            X = [(1 - d) * x + 0.5 * pi - df * (x - mean) for x, pi in zip(X, p)]; t += 1
            if (X[0] - X[1]) / sum(X) >= 0.5 or t > 10000: break
        tnl[(r, d, df)] = t
        okB &= abs(m - new) < 1e-4
        print(f"   r={r} d={d} df={df}: Gamma={G:.3f}; simulated factor {m:.5f}; 1+(d+df)(Gamma-1)={new:.5f}; V6.1's 1+d(Gamma-1)={old:.5f}; "
              f"1%->50% gap in {t if t <= 10000 else 'more than 10,000'} periods (linear estimate {math.log(50)/math.log(new):.1f})")
    expect(okB, "m03(C): the simulated factor equals 1+(d+df)(Gamma-1) to 1e-4 in 4/4 (1.40000, 1.05000, 1.10000, 1.03000)")
    expect(tnl[(3.0, 0.2, 0.0)] == 13 and tnl[(3.0, 0.05, 0.05)] > 10000,
           "m03(C): at Gamma=3, d=0.2, df=0 the nonlinear gap goes from 1% to 50% in 13 periods (linear estimate 11.6); with diffusion (Gamma=1.5, d=df=0.05, r=3) it never reaches 50%")
    print("   same Gamma=1.2, different turnover (Sys I1):")
    fac = {}
    for (d, df) in ((0.4, 0.1), (0.015, 0.005)):
        r = 1.2 * (d + df) / d
        c = dict(h=lambda X, r=r: r * math.log(X), kap=0.5, d=d, df=df, k0=0.0)
        m = _m03_relmode_multiplier(2, [c], T=2000); fac[d + df] = m
        print(f"      d+df={d+df}: factor {m:.5f}, periods to grow 50x {math.log(50)/math.log(m):.0f}")
    expect(abs(math.log(50) / math.log(fac[0.5]) - 41) < 0.5 and abs(math.log(50) / math.log(fac[0.02]) - 980) < 2,
           "at the same Gamma=1.2 a channel with turnover 0.5 needs 41 periods to grow a gap 50-fold, one with turnover 0.02 needs 980: Gamma sets the sign, turnover the speed")
    print("   two channels with the same Gamma but different turnover split:")
    okP = True; roots = []
    for (d1, d2) in ((0.3, 0.02), (0.1, 0.1)):
        chans = [dict(h=lambda X: 0.6 * math.log(X), kap=0.5, d=d1, df=0.0, k0=0.0), dict(h=lambda X: 0.6 * math.log(X), kap=0.5, d=d2, df=0.0, k0=0.0)]
        G = _m03_gamma_formula(2, chans); m = _m03_relmode_multiplier(2, chans, T=3000)
        a = [0.6 * d1, 0.6 * d2]; D = [1 - d1, 1 - d2]
        lo, hi = max(D) + 1e-12, 3.0
        for _ in range(200):
            mid = (lo + hi) / 2
            if sum(aj / (mid - Dj) for aj, Dj in zip(a, D)) > 1: lo = mid
            else: hi = mid
        okP &= abs(m - lo) < 1e-4 and abs(G - 1.2) < 1e-6; roots.append(lo)
        print(f"      d=({d1},{d2}): Gamma={G:.3f}; simulated factor {m:.5f}; Perron root of (S1) {lo:.5f}")
    expect(okP and abs(roots[0] - roots[1]) > 0.01, f"m03(C): with two channels the simulated factor is the Perron root of (S1) ({roots[0]:.5f} vs {roots[1]:.5f} at the same Gamma=1.2): not a function of Gamma")
    print("(c) [derived] f3(C): secular roots for two channels with gains 0.6+0.6 (Gamma=1.2), turnovers (dK, dZ)")
    sec = []
    for (dK, dZ) in [(0.5, 0.5), (0.02, 0.02), (0.5, 0.02)]:
        gK = gZ = 0.6
        lo, hi = 1 - min(dK, dZ) + 1e-9, 5.0
        for _ in range(200):
            m = (lo + hi) / 2
            val = gK * dK / (m - (1 - dK)) + gZ * dZ / (m - (1 - dZ))
            if val > 1: lo = m
            else: hi = m
        sec.append(hi)
        print(f"   dK={dK}, dZ={dZ}: lambda*={hi:.4f}; periods 1%->50% = {math.log(50)/math.log(hi):.0f}")
    expect(abs(sec[0] - 1.1) < 1e-4 and abs(sec[1] - 1.004) < 1e-4 and abs(sec[2] - 1.0092) < 1e-4,
           "secular roots 1.1000, 1.0040, 1.0092 (41, 980 and 427 periods from 1% to 50%)")
    print("(d) [derived] systems s1(b),(c) and Math-Fable m6(3): the V6.1 factor against the corrected one")
    for d, df_ in ((0.2, 0.0), (0.2, 0.1), (0.2, 0.3)):
        r = 3.0; G = r * d / (d + df_)
        print(f"   d={d}, delta_f={df_}: Gamma={G:.3f}; 1+d(G-1)={1+d*(G-1):.4f}; 1+(d+df)(G-1)={1+(d+df_)*(G-1):.4f}")
    for (dK, df, Gamma) in [(0.2, 0.0, 1.5), (0.2, 0.1, 1.5), (0.05, 0.05, 3.0)]:
        lam_true = 1 + (dK + df) * (Gamma - 1); lam_text = 1 + dK * (Gamma - 1)
        print(f"   dK={dK}, df={df}, Gamma={Gamma}: 1+(dK+df)(Gamma-1)={lam_true:.3f} (V6.1 {lam_text:.3f}); periods 1%->50%: {math.log(50)/math.log(lam_true):.0f} vs V6.1 {math.log(50)/math.log(lam_text):.0f}")


def check_CE():
    block('CE', 'compound', 'independent',
          'A point of enough: a cap strictly below K* holds, a cap at K* can fail; recovery from every start needs an inflow not tied to rank (sharing, provision or diffusion)')
    # Sources (ported): planning/math-fable/f3_compound.py (A); planning/math-opus/m04_compound_cap.py (A,B,C);
    # ../v6.1/reviews/counterexamples_v61_codex.py cases 3a (cap equality) and 3b (positive diffusion);
    # ../v6.1/reviews/scripts-v6.1-math-opus/s9_cap_edge.py; ../v6.1/reviews/scripts-v6.1-math-fable/m1_loopgain.py (C).
    # Claims (D2-fable s3, D2-opus s3): at the cap K_bar = K* a laggard just below returns iff
    # Gamma_0 (n-1)/n < 1 + df (n-1)/(n dK); for K_bar < K* it returns; from every start iff phi > 0 on (0, K_bar), with
    # phi(0+) = beta kap Om/n + k0 + df (n-1) K_bar/n when r > 1: diffusion is a third source, not a guarantee.
    # ---------------------------------------------------------------- f3(A)
    def simulate_cap(n, r, kap, Om, dK, beta, k0, df, cap, K_lag0, T=20000):
        K = [K_lag0] + [cap] * (n - 1)
        for _ in range(T):
            P = sum(x ** r for x in K); p = [x ** r / P for x in K]; m = sum(K) / n
            K = [min(cap, (1 - dK) * K[i] + kap * Om * ((1 - beta) * p[i] + beta / n) + k0 - df * (K[i] - m)) for i in range(n)]
        return K
    def phi(K, n, r, kap, Om, dK, beta, k0, df, cap):
        return kap * Om * ((1 - beta) * K ** r / (K ** r + (n - 1) * cap ** r) + beta / n) + k0 - dK * K + df * (n - 1) * (cap - K) / n
    print("(a) f3(A): caps: local stability at K_bar = K* and the role of diffusion")
    okA = True
    for (n, r, beta, k0, df) in [(2, 3.0, 0.0, 0.0, 0.0), (2, 1.5, 0.0, 0.0, 0.0), (4, 2.0, 0.0, 0.0, 0.0), (4, 1.2, 0.0, 0.0, 0.0),
                                 (5, 1.5, 0.0, 0.0, 0.0), (2, 3.0, 0.0, 0.0, 0.6), (4, 2.0, 0.0, 0.0, 0.3), (4, 2.0, 0.0, 0.0, 0.1),
                                 (3, 2.0, 0.3, 0.0, 0.0), (3, 2.0, 0.0, 0.05, 0.0)]:
        kap, Om, dK = 0.5, 1.0, 0.2
        Ks = (kap * Om / n + k0) / dK; om = kap * Om / (kap * Om + n * k0); G0 = (1 - beta) * r * om
        lhs = G0 * (n - 1) / n; rhs = 1 + df * (n - 1) / (n * dK)
        Kend = simulate_cap(n, r, kap, Om, dK, beta, k0, df, Ks, 0.999 * Ks)[0]
        pred = "returns" if lhs < rhs else "falls away"
        obs = "returns" if Kend > 0.99 * Ks else "falls away"
        okA &= pred == obs
        print(f"   n={n} r={r} beta={beta} k0={k0} df={df}: Gamma0(n-1)/n={lhs:.3f} vs 1+df(n-1)/(n dK)={rhs:.3f} -> predicted {pred}; "
              f"laggard from 0.999 K* ends at {Kend/Ks:.4f} K* ({obs}) {'OK' if pred==obs else 'MISMATCH'}")
    expect(okA, "f3(A): the local condition at K_bar = K* predicts return or exclusion in 10/10 (incl. diffusion and provision cases)")
    Ks2 = (0.5 * 1.0 / 2) / 0.2; okS = True
    for frac in (0.98, 0.9):
        Kend = simulate_cap(2, 3.0, 0.5, 1.0, 0.2, 0.0, 0.0, 0.0, frac * Ks2, 0.999 * frac * Ks2)[0]
        okS &= Kend > 0.99 * frac * Ks2
        print(f"   strictly lower cap ({frac} K*), n=2 r=3 (Gamma=3), no diffusion: laggard from 0.999 cap ends at {Kend/(frac*Ks2):.4f} cap ({'returns' if Kend > 0.99*frac*Ks2 else 'falls away'})")
    expect(okS, "f3(A): strictly lower caps (0.98 K*, 0.9 K*) hold a laggard at Gamma=3")
    Kd = simulate_cap(2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.6, 2.5, 0.01)
    mn = min(phi(k / 1000 * 2.5, 2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.6, 2.5) for k in range(1, 1000))
    print(f"   diffusion as the third restoring source (n=2, r=2, d=0.2, df=0.6, cap=K*=2.5, beta=k0=0): from K=0.01 -> {Kd}; min phi on (0, Kbar) = {mn:.4f}")
    Kx = simulate_cap(2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.0, 2.25, 0.3 * 2.25)[0]
    Kst = simulate_cap(2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.05, 2.25, 0.3 * 2.25)[0]
    phi0 = phi(1e-9, 2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.05, 2.25); mnst = min(phi(k / 1000 * 2.25, 2, 2.0, 1.0, 1.0, 0.2, 0.0, 0.0, 0.05, 2.25) for k in range(1, 1000))
    print(f"   necessity: beta=k0=df=0, r=2, n=2, cap=0.9 K*: laggard from 0.3 cap -> {Kx:.2e} (excluded)")
    print(f"   with df=0.05 only: laggard from 0.3 cap -> {Kst:.4f} ({Kst/2.25:.2f} of the cap); phi(0+)={phi0:.4f}; min phi on (0,Kbar)={mnst:.4f}")
    # Finding (notes, CE): D2-fable s3(d) and s29.9 read the stall as "0.36 K_bar"; the stalled level is K = 0.36, that is
    # 0.16 of the cap K_bar = 2.25. The claim (diffusion alone: phi(0+) > 0 yet min phi < 0, so the laggard stalls) holds.
    print(f"   [finding] the stall is at K = {Kst:.2f}, i.e. {Kst/2.25:.2f} K_bar (D2-fable wrote '0.36 K_bar'); the minimum of phi on a 1,000-point grid "
          f"({mn:.4f}) is grid-dependent: 0.0001 on m04's 10,000-point grid and 0.000075 in Codex's exact factorization (f below)")
    expect(min(Kd) > 2.4999 and mn > 0 and Kx < 1e-100 and phi0 > 0 > mnst and 0.15 < Kst / 2.25 < 0.17,
           f"f3(A): diffusion alone restores (min phi > 0); with none of the three the laggard is excluded; df=0.05 alone stalls it at K={Kst:.2f} ({Kst/2.25:.2f} of the cap): a source, not a guarantee")
    # ---------------------------------------------------------------- m04 (ported)
    def step4(X, r, kap, Om, beta, k0, d, df, cap):
        n = len(X); w = [x ** r for x in X]; W = sum(w); mean = sum(X) / n
        Xn = [(1 - d) * x + kap * Om * ((1 - beta) * wi / W + beta / n) + k0 - df * (x - mean) for x, wi in zip(X, w)]
        return [min(cap, x) for x in Xn]
    def phi4(K, Kbar, n, r, kap, Om, beta, k0, d, df):
        return kap * Om * ((1 - beta) * K ** r / (K ** r + (n - 1) * Kbar ** r) + beta / n) + k0 - d * K + df * (n - 1) * (Kbar - K) / n
    print("(b) m04(A): cap at and below K*")
    X = [2.499, 2.5]
    for t in range(400): X = step4(X, 3, 1, 1, 0, 0, 0.2, 0.0, 2.5)
    X2 = [2.449, 2.45]
    for t in range(4000): X2 = step4(X2, 3, 1, 1, 0, 0, 0.2, 0.0, 2.45)
    print(f"   cap = K* = 2.5, r=3, start (2.499, 2.5): after 400 periods {X[0]:.3e}, {X[1]:.4f}  (excluded)")
    print(f"   cap = 0.98 K* = 2.45, same start just below the cap: after 4000 periods {X2[0]:.6f}, {X2[1]:.6f}  (restored)")
    rr = random.Random(7); bad_strict = 0; tests = 0; eq_pred_ok = 0; eq_tests = 0
    for _ in range(400):
        n = rr.choice([2, 3, 4, 6]); r = rr.uniform(0.5, 4); kap = 1.0; Om = 1.0
        beta = rr.choice([0, 0, rr.uniform(0, 0.3)]); k0 = rr.choice([0, 0, rr.uniform(0, 0.2)])
        d = rr.uniform(0.05, 0.4); df = rr.choice([0, 0, rr.uniform(0, 0.3)])
        if d + df > 1: continue
        Ks = (kap * Om / n + k0) / d
        cap = 0.97 * Ks
        Xc = [cap * 0.999] + [cap] * (n - 1)
        for t in range(3000): Xc = step4(Xc, r, kap, Om, beta, k0, d, df, cap)
        tests += 1
        if abs(Xc[0] - cap) > 1e-6 * cap: bad_strict += 1
        w = kap * Om / (kap * Om + n * k0)
        excl_pred = (1 - beta) * r * w * (n - 1) / n > 1 + df * (n - 1) / (n * d)
        Xc = [Ks * (1 - 1e-4)] + [Ks] * (n - 1)
        for t in range(6000): Xc = step4(Xc, r, kap, Om, beta, k0, d, df, Ks)
        excl_sim = Xc[0] < Ks * (1 - 2e-4)
        eq_tests += 1; eq_pred_ok += (excl_pred == excl_sim)
    print(f"   400 random settings: strict cap (0.97 K*) restored from just below in {tests-bad_strict} of {tests};")
    print(f"   cap = K*: local exclusion predicted by (1-beta) r omega (n-1)/n > 1 + df(n-1)/(n d) in {eq_pred_ok} of {eq_tests} (simulated)")
    expect(X[0] < 1e-20 and abs(X2[0] - 2.45) < 1e-9 and bad_strict == 0 and eq_pred_ok == eq_tests == tests,
           f"m04(A): Codex's cap-equality case excluded ({X[0]:.1e}); 0.98 K* restores; strict cap holds in {tests}/{tests}; the criterion at equality predicts {eq_pred_ok}/{eq_tests}")
    print("(c) m04(B): global recovery: criterion phi>0 on (0,Kbar) vs simulation from a laggard at 1% of the cap")
    n, r, kap, Om, beta, k0, d, df, cap = 2, 2.0, 1.0, 1.0, 0.0, 0.0, 0.2, 0.6, 2.5
    mnB = min(phi4(cap * k / 10000, cap, n, r, kap, Om, beta, k0, d, df) for k in range(1, 10000))
    Xb = [0.01, 2.5]
    for t in range(2000): Xb = step4(Xb, r, kap, Om, beta, k0, d, df, cap)
    print(f"   Codex: n=2 r=2 d=.2 df=.6, cap=K*=2.5, no sharing or provision: min phi on grid {mnB:.4f} (>0); from (0.01, 2.5) -> ({Xb[0]:.6f}, {Xb[1]:.6f})")
    rr = random.Random(11); agree = 0; tot = 0; examples = []
    for _ in range(600):
        n = rr.choice([2, 3, 5]); r = rr.uniform(1.05, 4); kap = 1.0; Om = 1.0
        beta = rr.choice([0, rr.uniform(0, 0.4)]); k0 = rr.choice([0, rr.uniform(0, 0.15)])
        d = rr.uniform(0.05, 0.4); df = rr.choice([0, rr.uniform(0, 0.5)])
        if d + df > 1: continue
        Ks = (kap * Om / n + k0) / d; cap = rr.uniform(0.5, 0.99) * Ks
        if cap > (kap * Om + n * k0) / (n * d + df): continue
        crit = min(phi4(cap * k / 2000, cap, n, r, kap, Om, beta, k0, d, df) for k in range(1, 2000)) > 0
        Xr = [0.01 * cap] + [cap] * (n - 1)
        for t in range(5000): Xr = step4(Xr, r, kap, Om, beta, k0, d, df, cap)
        rec = abs(Xr[0] - cap) < 1e-6 * cap
        tot += 1; agree += (crit == rec)
        if crit != rec:
            thr = max([k / 2000 for k in range(1, 2000) if phi4(cap * k / 2000, cap, n, r, kap, Om, beta, k0, d, df) <= 0] or [0])
            examples.append(dict(n=n, r=round(r, 2), d=round(d, 3), cap_over_Kstar=round(cap / Ks, 3), criterion=crit, recovered_from_1pct=rec, exclusion_threshold_over_cap=thr))
    print(f"   random settings with leaders provably held at the cap (Kbar <= (kap Om + n k0)/(n d + df)): criterion agrees with simulation in {agree} of {tot}")
    if examples: print("   disagreements: the criterion concerns EVERY start; these laggards start above the exclusion threshold:", examples[:5])
    expect(mnB > 0 and abs(Xb[0] - 2.5) < 1e-6 and all((not e['criterion']) and e['recovered_from_1pct'] and e['exclusion_threshold_over_cap'] < 0.01 for e in examples),
           f"m04(B): phi>0 agrees with simulation in {agree}/{tot}; every disagreement is a start above an exclusion threshold below 1% of the cap")
    print("(d) m04(C): r>1 and no inflow not tied to rank: laggards below a threshold are excluded; any one of the three restores")
    n, r, kap, Om, d, cap = 5, 1.5, 1.0, 1.0, 0.2, 0.8
    res_C = {}
    for (beta, k0, df) in ((0, 0, 0), (0.1, 0, 0), (0, 0.05, 0), (0, 0, 0.15)):
        res = []
        for K0 in (0.05, 0.2, 0.5):
            Xr = [K0] + [cap] * (n - 1)
            for t in range(4000): Xr = step4(Xr, r, kap, Om, beta, k0, d, df, cap)
            res.append(Xr[0])
        res_C[(beta, k0, df)] = res
        print(f"   beta={beta} k0={k0} df={df}: phi(0+)={beta*kap*Om/n + k0 + df*(n-1)*cap/n:.4f}; laggard " + ", ".join(f"{K0}->{x:.4f}" for K0, x in zip((0.05, 0.2, 0.5), res)))
    okC = res_C[(0, 0, 0)][0] < 1e-6 and res_C[(0, 0, 0)][1] < 1e-6 and abs(res_C[(0, 0, 0)][2] - cap) < 1e-6 and \
          all(abs(x - cap) < 1e-6 for key in ((0.1, 0, 0), (0, 0.05, 0), (0, 0, 0.15)) for x in res_C[key])
    expect(okC, "m04(C): with none of sharing, provision, diffusion, laggards at 0.05 and 0.2 are excluded; with any one of them all return")
    # ---------------------------------------------------------------- Codex 3a, 3b (ported)
    def stock_step(stocks, r, decay, diffusion=0.0, cap=None):
        strengths = [x ** r for x in stocks]
        mean = sum(stocks) / len(stocks)
        new = [(1 - decay) * x + strength / sum(strengths) + diffusion * (mean - x) for x, strength in zip(stocks, strengths)]
        return new if cap is None else [min(cap, x) for x in new]
    stocks = [2.499, 2.5]
    first = stock_step(stocks, 3, 0.2, cap=2.5)
    for _ in range(400): stocks = stock_step(stocks, 3, 0.2, cap=2.5)
    ok3a = first[0] < 2.499 and stocks[0] < 1e-20 and stocks[1] == 2.5
    print(f"(e) Codex 3a (cap equality): first step {first}; after 400 periods {stocks}")
    expect(ok3a, "Codex 3a: a cap equal to the symmetric steady capacity is not locally stable at r=3"); _codex(3, ok3a)
    smallest = math.inf; ok_f = True
    for k in range(1, 10000):
        s_ = k / 10000
        direct = s_ * s_ / (1 + s_ * s_) - 0.5 * s_ + 0.75 * (1 - s_)
        factored = (1 - s_) * (1.25 * s_ * s_ - 0.5 * s_ + 0.75) / (1 + s_ * s_)
        ok_f &= direct > 0 and math.isclose(direct, factored, abs_tol=1e-14)
        smallest = min(smallest, direct)
    stocks = [0.01, 2.5]
    for _ in range(1000): stocks = stock_step(stocks, 2, 0.2, 0.6, 2.5)
    ok3b = ok_f and all(abs(x - 2.5) < 1e-10 for x in stocks)
    print(f"(f) Codex 3b (positive diffusion): smallest laggard inflow on the grid {smallest:.6f}; after 1000 periods from (0.01, 2.5): {stocks}")
    expect(ok3b, "Codex 3b: diffusion restores the laggard with no sharing or outside provision (inflow positive on the whole grid)"); _codex(4, ok3b)
    # ---------------------------------------------------------------- s9_cap_edge (Math-Opus reviewer) and m1(C) (Math-Fable reviewer)
    print("(g) s9 (Math-Opus reviewer): cap exactly at K*, df=0: local stability fails when Gamma > n/(n-1)")
    ok9 = True
    for (n, r, beta, k0) in [(2, 3.0, 0.0, 0.0), (2, 1.5, 0.0, 0.0), (4, 2.0, 0.0, 0.0), (4, 1.2, 0.0, 0.0)]:
        kap, Om, dK = 0.5, 1.0, 0.2
        Ks = (kap * Om / n + k0) / dK; G = (1 - beta) * r * (kap * Om / (kap * Om + n * k0))
        vals = [phi(Ks * (1 - e), n, r, kap, Om, dK, beta, k0, 0.0, Ks) for e in (1e-3, 1e-2)]
        ok9 &= (vals[0] > 0) == (G < n / (n - 1))
        print(f"   n={n}, r={r}: Gamma={G:.2f} vs n/(n-1)={n/(n-1):.2f}; phi just below the cap K*: {vals[0]:+.2e}, {vals[1]:+.2e} -> laggard {'returns' if vals[0]>0 else 'falls away'}")
    expect(ok9, "s9: at a cap equal to K* without diffusion the laggard returns iff Gamma < n/(n-1) (4/4)")
    print("(h) m1(C) (Math-Fable reviewer): n=5, r=1.5, dK=0.05: caps at 1.00, 0.98, 0.90 of K*")
    n, r, kap, Om, dK, beta, k0 = 5, 1.5, 0.5, 1.0, 0.05, 0.0, 0.0
    Ks = (kap * Om / n + k0) / dK; outs = []
    def phi1(K, cap): return kap * Om * ((1 - beta) * K ** r / (K ** r + (n - 1) * cap ** r) + beta / n) + k0 - dK * K
    for cap in (Ks, 0.98 * Ks, 0.9 * Ks):
        K = [0.97 * cap] + [cap] * (n - 1)
        for _ in range(40000):
            Ssum = sum(k ** r for k in K); p = [k ** r / Ssum for k in K]
            K = [min(cap, (1 - dK) * K[i] + kap * Om * ((1 - beta) * p[i] + beta / n) + k0) for i in range(n)]
        slope = (phi1(cap, cap) - phi1(cap * (1 - 1e-6), cap)) / (cap * 1e-6)
        outs.append(K[0] / cap)
        print(f"   cap/K* = {cap/Ks:.2f}: phi(cap) = {phi1(cap,cap):+.4f}, phi'(cap) = {slope:+.4f}, laggard from 0.97 cap ends at {K[0]:.4f} ({'excluded/stalled' if K[0] < 0.99*cap else 'returns to cap'})")
    expect(outs[0] < 0.99 and outs[1] > 0.999 and outs[2] > 0.999, "m1(C): at equality the laggard is excluded (phi'(K*) = +0.0100 > 0); caps at 0.98 and 0.90 of K* hold")


def check_QS():
    block('QS', 'corrrate, humancorr, capdyn (S4)', 'independent',
          'Capacity off its selected level, jointly with the field model: the rate law\'s two halves (QS/R/GA/GM), the lag delay, '
          'reversal, and correction resting on human capacity eroded at delta_h (+w delta_h; hysteresis)')
    # Sources (ported): planning/math-fable/f5_corrrate.py (A); planning/math-opus/m06_corrrate.py (D),(E);
    # ../v6.1/reviews/scripts-v6.1-systems/s4_joint.py (E1, E1', E1''), s5_joint2.py (E2, E4a, E4b; E3 is in SR);
    # ../v6.1/reviews/scripts-v6.1-math-fable/m5_quasistatic.py; ../v6.1/reviews/scripts-v6.1-math-opus/s4_cost.py (c)
    # (the replicator-with-mutation dynamics of s4_cost(c) only with --full).
    # Claims (D2-fable s9, s27; D2-opus s9; plan s1 item 4): sufficient whatever the adaptation speed (q <= q*);
    # necessary if liminf q/q* > 0 (only 'if': merge note U04 s2 item 1); lag at rate k delays failure by eta ln(1+g/k)/(alpha_ctl-(1+eta)alpha_cor),
    # g = (alpha_ctl-alpha_cor)/eta; additive (constant-variance) selection keeps q bounded; humancorr: the threshold
    # rises by w delta_h; the quasi-static model is optimistic after reversals.
    # ---------------------------------------------------------------- f5(A) (ported)
    p, A, d0, actl = 0.6, 0.3, 2.0, 0.2
    def gam(t): return math.exp(-actl * t)
    def dd(t, a): return d0 * math.exp(a * t)
    def qstar(t, a, f=0.0, eta=1.0):
        m = p * p / dd(t, a) - f
        return (m / gam(t)) ** (1 / eta) if m > 0 else 0.0
    def run5(acor, mode, par=None, H=400.0, dt=0.01):
        q = qstar(0, 0.0); t = 0.0; first = None; smax = 0.0
        while t < H:
            tm = t + dt / 2; qs = qstar(tm, acor); d = dd(tm, acor)
            if mode == "QS": q = qs
            elif mode == "R": q = qs + (q - qs) * math.exp(-par * dt)
            elif mode == "GA": q = max(0.0, q + dt * par * (p * p / d - gam(tm) * q))
            elif mode == "GM": q = qs + (q - qs) * math.exp(-(par / qstar(0, 0.0) ** 2) * q * q * gam(tm) * dt)
            G = (A + p * q) / d
            if G > 1 and first is None: first = t
            smax = max(smax, G); t += dt
        return first, smax, q
    print("(a) f5(A): rate law under finite adjustment (threshold alpha_ctl/(1+eta) = 0.1); first certificate failure")
    tab5 = {}
    for acor in (0.05, 0.08, 0.09, 0.11):
        row = []
        for mode, par in [("QS", None), ("R", 0.3), ("R", 0.1), ("R", 0.03), ("GA", 1.0), ("GM", 1.0)]:
            fi, sm, q = run5(acor, mode, par); tab5[(acor, mode, par)] = fi
            row.append(f"{mode}{'' if par is None else '('+str(par)+')'}: {('%.1f' % fi) if fi is not None else 'never'}")
        print(f"   alpha_cor={acor}: " + " | ".join(row))
    okT = all(tab5[(0.11, m, p_)] is None for (m, p_) in [("QS", None), ("R", 0.3), ("R", 0.1), ("R", 0.03), ("GA", 1.0), ("GM", 1.0)])
    okT &= all(tab5[(a, "GA", 1.0)] is None for a in (0.05, 0.08, 0.09))
    okT &= all(tab5[(a, "QS", None)] < tab5[(a, "R", 0.3)] < tab5[(a, "R", 0.1)] < tab5[(a, "R", 0.03)] for a in (0.05, 0.08, 0.09))
    okT &= all(abs(tab5[(a, "GM", 1.0)] - tab5[(a, "QS", None)]) < 1.0 for a in (0.05, 0.08, 0.09))
    expect(okT, "f5(A): above the threshold nothing fails; below it QS fails first (28.8 at 0.05), lags fail later, multiplicative selection tracks QS, additive selection never fails")
    print("   constant-rate lag: delay vs eta ln(1+g/k)/(alpha_ctl-(1+eta)alpha_cor), g=(alpha_ctl-alpha_cor)/eta")
    worst = 0.0
    for acor in (0.05, 0.08):
        tq = run5(acor, "QS")[0]
        for k in (0.3, 0.1, 0.03):
            tr = run5(acor, "R", k)[0]; g = actl - acor; pred = math.log(1 + g / k) / (actl - 2 * acor)
            worst = max(worst, abs((tr - tq) / pred - 1))
            print(f"      alpha_cor={acor}, k={k}: delay {tr-tq:.2f} vs formula {pred:.2f}")
    expect(worst < 0.03, f"f5(A): the lag delay matches eta ln(1+g/k)/(alpha_ctl-(1+eta)alpha_cor) within {worst:.1%} in 6 cases")
    okGA = True
    for acor in (0.02, 0.05):
        fi, sm, q = run5(acor, "GA", 1.0, H=600.0)
        bound = qstar(0, 0.0) + p * p / (d0 * acor)
        okGA &= q <= bound and fi is None and sm < 1
        print(f"      GA, alpha_cor={acor}: q(600)={q:.3f} <= bound {bound:.3f}; max G_ev over [0,600] = {sm:.3f} ({'never fails' if fi is None else 'fails at %.1f'%fi})")
    expect(okGA, "f5(A): constant-variance gradient selection keeps q <= q0 + V p^2/(d0 alpha_cor) and the certificate never fails at alpha_cor = 0.02, 0.05")
    # ---------------------------------------------------------------- m06(D),(E) (ported)
    def joint(alpha_cor, dyn='QS', kappa=0.1, V=1.0, T=400.0, dt=0.01, alpha_ctl=0.2, d0=2.0, A=0.3, eps=0.5, zeta=1.0,
              x0=0.01, q0=None, w=0.0, delta_h=0.0):
        t = 0.0
        q = 0.5 if q0 is None else q0
        z = A / d0
        u = math.log(x0 / (1 - x0)); fail = None; cap = None
        while t < T:
            d = d0 * math.exp(alpha_cor * t)
            if w: d *= math.exp(-w * delta_h * t)
            g = math.exp(-alpha_ctl * t)
            qs = 1.0 / (g * d)
            if dyn == 'QS': q = qs
            elif dyn == 'lag': q = qs + (q - qs) * math.exp(-kappa * dt)
            elif dyn == 'add': q = qs + (q - qs) * math.exp(-V * g * dt)
            elif dyn == 'mult': q = qs / (1 + (qs / q - 1) * math.exp(-V * dt / d))
            G = (A + q) / d
            if G >= 1 and fail is None: fail = t
            zs = (A + q) / d
            z = zs + (z - zs) * math.exp(-eps * d * dt)
            u += dt * zeta * (z - 1.0)
            if u > 0 and cap is None: cap = t
            t += dt
        x = 1 / (1 + math.exp(-u)) if u > -700 else 0.0
        return fail, cap, x, (A + q) / d
    print("(b) m06(D): capacity off its optimum, joint with one evaluation domain (alpha_ctl=.2, eta=1: rate law .1)")
    fmt = lambda v: '   never' if v is None else f"{v:8.1f}"
    print("   alpha_cor | dynamics           | cert. fails | captured (x>1/2) | final G")
    tabD = {}; tabG = {}
    for ac in (0.05, 0.09, 0.1, 0.12):
        for (dyn, kw, tag) in (('QS', {}, 'quasi-static      '), ('lag', dict(kappa=0.1), 'lag kappa=.1      '), ('lag', dict(kappa=0.03), 'lag kappa=.03     '),
                               ('add', dict(V=1.0), 'additive V=1      '), ('add', dict(V=100.0), 'additive V=100    '), ('mult', dict(V=1.0), 'multiplicative V=1')):
            f, c, x, G = joint(ac, dyn, **kw); tabD[(ac, tag.strip())] = (f, c); tabG[(ac, tag.strip())] = G
            print(f"   {ac:9.2f} | {tag} | {fmt(f)}    | {fmt(c)}         | {G:.3g}")
    okD = all(tabD[(ac, k)] == (None, None) for ac in (0.1, 0.12) for k in ('quasi-static', 'lag kappa=.1', 'lag kappa=.03', 'additive V=1', 'additive V=100', 'multiplicative V=1'))
    okD &= tabD[(0.05, 'quasi-static')][0] < tabD[(0.05, 'lag kappa=.1')][0] < tabD[(0.05, 'lag kappa=.03')][0] and tabD[(0.05, 'additive V=1')] == (None, None)
    gaps = [c - f for (f, c) in tabD.values() if f is not None and c is not None]
    okD &= 12 <= min(gaps) and max(gaps) <= 76
    expect(okD, f"m06(D): at alpha_cor >= 0.1 no dynamics fails; at 0.05 lags delay failure, additive selection prevents it; capture follows failure by {min(gaps):.0f}-{max(gaps):.0f} periods (the two clocks)")
    # v6.2 addition (merge note U04 s4): Proposition S4.2(2)(b), selection variance proportional to q ('multiplicative' in m06).
    fM, cM = tabD[(0.05, 'multiplicative V=1')]; GM_ = tabG[(0.05, 'multiplicative V=1')]
    print(f"   S4.2(2)(b): variance proportional to q at alpha_cor=0.05 fails at {fM:.1f}, is captured at {cM:.1f}, and ends at row sum {GM_:.2e}: capacity bounded, certificate held again")
    expect(fM is not None and GM_ < 1e-6, "S4.2(2)(b): with selection variance proportional to q the certificate fails transiently (23.8) and holds again by the end (final row sum 9e-8 < 1): capacity stays bounded")
    print("   lag delay vs eta ln(1+g/kappa)/(alpha_ctl-(1+eta)alpha_cor):")
    worst = 0.0
    for (ac, kap) in ((0.05, 0.1), (0.05, 0.03), (0.02, 0.1)):
        fq, *_ = joint(ac, 'QS', T=600.0); fl, *_ = joint(ac, 'lag', kappa=kap, T=600.0)
        g = (0.2 - ac); pred = math.log(1 + g / kap) / (0.2 - 2 * ac); worst = max(worst, abs((fl - fq) / pred - 1))
        print(f"      alpha_cor={ac} kappa={kap}: simulated delay {fl-fq:.2f}, formula {pred:.2f} (asymptotic)")
    expect(worst < 0.05, f"m06(D): lag delays 9.42/9.16, 18.23/17.92, 6.33/6.44 (simulated/formula), within {worst:.1%}")
    okAdd = True
    for ac in (0.01, 0.03):
        f, c, x, G = joint(ac, 'add', V=1.0, T=1500.0)
        okAdd &= f is not None and G < 1e-6
        print(f"   additive selection, alpha_cor={ac} (far below .1): first failure {f if f is None else round(f,1)}, final G {G:.3g} (bound q <= q0 + V/(d0 alpha_cor) = {0.5+1/(2*ac):.1f})")
    expect(okAdd, "m06(D): under additive selection any alpha_cor > 0 certifies eventually, after a transient failure (t = 10.6 at alpha_cor = 0.01)")
    print("   [humancorr] correction resting on human capacity eroded by delegation (w=1), quasi-static certificate eventually held?")
    okH = True
    for dh in (0.0, 0.05, 0.1):
        res = []
        for ac in (0.1, 0.12, 0.15, 0.2, 0.22):
            f, c, x, G = joint(ac, 'QS', w=1.0, delta_h=dh, T=800.0)
            held = G < 1; res.append(f"{ac}:{'held' if held else 'fails'}")
            okH &= held == (ac >= 0.1 + dh - 1e-12)
        print(f"      delta_h={dh}: threshold predicted {0.1+dh:.2f}; " + ", ".join(res))
    expect(okH, "humancorr (m06 D): the certificate is held eventually iff alpha_cor >= alpha_ctl/(1+eta) + w delta_h (0.10, 0.15, 0.20), 15/15")
    print("(c) m06(E): reversal in a self-sustaining domain; minimal hold of d2=1.5 that undoes capture at d1=0.9")
    d1, d2 = 0.9, 1.5
    def undone(T, dyn, kappa):
        q = 1.0 / d1; z = (0.3 + q) / d1; u = math.log((1 - 1e-6) / 1e-6); t = 0.0; dt = 0.01
        while t < T + 400.0:
            d = d2 if t < T else d1
            qs = 1.0 / d
            if dyn == 'QS': q = qs
            else: q = qs + (q - qs) * math.exp(-kappa * dt)
            x = 1 / (1 + math.exp(-u)) if u > -700 else 0.0
            zs = (0.3 + q) * x / d
            z = zs + (z - zs) * math.exp(-0.5 * d * dt)
            u += dt * 1.0 * (z - 1.0)
            t += dt
        return u < 0
    holds = {}
    for (dyn, kap) in (('QS', None), ('lag', 0.1), ('lag', 0.03)):
        lo, hi = 0.0, 400.0
        if not undone(hi, dyn, kap): holds[(dyn, kap)] = None; continue
        for _ in range(40):
            mid = (lo + hi) / 2
            if undone(mid, dyn, kap): hi = mid
            else: lo = mid
        holds[(dyn, kap)] = hi
    qs_ = holds[('QS', None)]
    for k, v in holds.items():
        print(f"   {k}: minimal hold {v:.2f}" + (f"  (+{100*(v/qs_-1):.0f}% over quasi-static)" if k[0] != 'QS' else ''))
    print(f"   G at d1 = {(0.3+1/d1)/d1:.2f} (captured), at d2 = {(0.3+1/d2)/d2:.2f}")
    expect(qs_ < holds[('lag', 0.1)] < holds[('lag', 0.03)] and abs(holds[('lag', 0.1)] / qs_ - 1.17) < 0.01 and abs(holds[('lag', 0.03)] / qs_ - 1.54) < 0.01,
           f"m06(E): after a withdrawn reform, slow capacity lengthens the hold needed: {qs_:.2f} quasi-static, +17% at kappa_q=0.1, +54% at 0.03")
    # ---------------------------------------------------------------- systems s4_joint (ported)
    pS, AS, chiS, YS = 0.6, 0.3, 1.0, 1.0
    actlS, d0S = 0.2, 2.0
    zetaS, epsS = 1.0, 0.5
    def gamS(t): return math.exp(-actlS * t)
    def ddS(t, acor): return d0S * math.exp(acor * t)
    def qstarS(t, acor): return chiS * pS * pS * YS / (gamS(t) * ddS(t, acor))
    q0S = qstarS(0, 0.0)
    def qrate(mode, par, t, q):
        if mode == 'R': return par
        if mode == 'GA': return par * gamS(t)
        if mode == 'GM': return (par / q0S ** 2) * q * q * gamS(t)
    def runS(acor, mode, par=None, H=300.0, dt=0.01, x0=0.01, record=False):
        u = math.log(x0 / (1 - x0)); q = q0S; z = (AS + pS * q0S) / d0S; t = 0.0; Tc = None; rec = []
        while t < H:
            tm = t + dt / 2; d = ddS(tm, acor); qs = qstarS(tm, acor)
            if mode == 'QS': qn = qs
            else:
                k = qrate(mode, par, tm, q); qn = qs + (q - qs) * math.exp(-k * dt)
            qq = 0.5 * (q + qn) if mode != 'QS' else qs
            G = (AS + pS * qq) / d
            if Tc is None and G > 1: Tc = t
            zn = G + (z - G) * math.exp(-epsS * d * dt)
            u += zetaS * (0.5 * (z + zn) - 1.0) * dt
            z, q = zn, qn; t += dt
            if record and abs(t - round(t)) < dt / 2 and int(round(t)) % 10 == 0: rec.append((round(t), G, q / qs, u))
            if u > 0: return Tc, t, rec
        return Tc, None, rec
    modes = [('QS', None), ('R', 1.0), ('R', 0.1), ('R', 0.03), ('GA', 1.0), ('GA', 0.1), ('GM', 1.0), ('GM', 0.1)]
    def lab(m, par): return m + ('' if par is None else '(' + str(par) + ')')
    print("(d) systems s4_joint E1: certificate failure T_cert (G_ev>1) / capture T_cap (x_ev>1/2), horizon 300")
    E1 = {}
    for acor in (0.0, 0.05, 0.08, 0.09, 0.095, 0.10, 0.105):
        row = []
        for m, par in modes:
            Tc, Tx, _ = runS(acor, m, par); E1[(acor, m, par)] = (Tc, Tx)
            f_ = lambda v: '  -  ' if v is None else f"{v:5.1f}"
            row.append(f"{lab(m,par)}: {f_(Tc)}/{f_(Tx)}")
        print(f"   alpha_cor={acor:5.3f}  " + " | ".join(row))
    expect(all(E1[(a, m, p_)] == (None, None) for a in (0.10, 0.105) for (m, p_) in modes) and E1[(0.05, 'QS', None)][0] < E1[(0.05, 'R', 0.03)][0],
           "s4_joint E1: at alpha_cor >= 0.1 no dynamics fails or is captured; below it lags delay failure (QS 28.8, R(0.03) 46.9 at 0.05)")
    def crit(mode, par, H):
        lo, hi = 0.0, 0.2
        for _ in range(16):
            m = (lo + hi) / 2
            if runS(m, mode, par, H=H)[1] is not None: lo = m
            else: hi = m
        return lo
    print("   E1': largest alpha_cor at which x_ev is captured within horizon H (rate-law asymptote 0.100)")
    cr = {}
    for H in (150.0, 300.0, 600.0):
        vals = [(lab(m, par), crit(m, par, H)) for m, par in modes]; cr[H] = dict(vals)
        print(f"   H={H:.0f}: " + "  ".join(f"{k}={v:.4f}" for k, v in vals))
    expect(cr[150.0]['QS'] < cr[300.0]['QS'] < cr[600.0]['QS'] < 0.1 and cr[600.0]['GA(1.0)'] < 0.01,
           f"s4_joint E1': the finite-horizon threshold rises toward 0.1 under QS ({cr[150.0]['QS']:.4f}, {cr[300.0]['QS']:.4f}, {cr[600.0]['QS']:.4f}); additive selection is captured only near alpha_cor=0 ({cr[600.0]['GA(1.0)']:.4f})")
    # v6.2 additions (merge note U04 s4): S4.2(2)(c) slow selection with variance proportional to q^2 stays bounded below the
    # rate law; and the capture lag across every rate and dynamics of E1 (the '8 to 85' of S4 and of the slowroute Scope).
    gm01 = [cr[H]['GM(0.1)'] for H in (150.0, 300.0, 600.0)]
    print(f"   S4.2(2)(c): variance proportional to q^2 at speed 0.1: largest captured alpha_cor {gm01[0]:.4f}, {gm01[1]:.4f}, {gm01[2]:.4f} at H = 150, 300, 600 (does not rise with H)")
    expect(max(gm01) - min(gm01) < 1e-3 and max(gm01) < 0.07,
           f"S4.2(2)(c): slow selection with variance proportional to q^2 is captured only below alpha_cor = {gm01[2]:.3f} at every horizon: bounded below the rate law, not tracking")
    lagsE1 = {(a, lab(m, p_)): E1[(a, m, p_)][1] - E1[(a, m, p_)][0] for (a, m, p_) in E1 if E1[(a, m, p_)][0] is not None and E1[(a, m, p_)][1] is not None}
    lag0 = [v_ for (a, k_), v_ in lagsE1.items() if a == 0.0]
    print(f"   capture lag T_cap - T_cert across E1: {min(lagsE1.values()):.1f} to {max(lagsE1.values()):.1f} periods over {len(lagsE1)} runs "
          f"(at alpha_cor = 0: {min(lag0):.1f} to {max(lag0):.1f}); by rate: " +
          ", ".join(f"{a}: {min(v_ for (b, k_), v_ in lagsE1.items() if b == a):.1f}-{max(v_ for (b, k_), v_ in lagsE1.items() if b == a):.1f}" for a in sorted({a for a, _ in lagsE1})))
    expect(round(min(lagsE1.values())) == 8 and round(max(lagsE1.values())) == 85 and round(min(lag0)) == 8 and round(max(lag0)) == 60,
           "capture follows the certificate's failure by 8 to 85 periods across E1 (8 to 60 with correction not growing), longer as correction approaches the rate law")
    print("   E1'': lag ratio q/q* along the path, alpha_cor=0.05 (constant-rate lag tends to k/(k+g), g=0.15)")
    ratios = {}
    for m, par in modes[1:]:
        _, _, rec = runS(0.05, m, par, record=True, H=60)
        ratios[lab(m, par)] = rec[-1][2] if rec else None
        print(f"   {lab(m,par)}: " + " ".join(f"t={t}:{r_:.2f}" for t, G, r_, u in rec))
    expect(abs(ratios['R(1.0)'] - 1 / 1.15) < 0.01 and abs(ratios['R(0.1)'] - 0.4) < 0.01 and abs(ratios['R(0.03)'] - 0.03 / 0.18) < 0.01 and ratios['GA(1.0)'] < 0.02,
           "s4_joint E1'': a constant-rate lag tracks q* at the ratio k/(k+g) (0.87, 0.40, 0.17); additive selection falls behind without limit (liminf q/q* = 0)")
    # ---------------------------------------------------------------- systems s5_joint2 E2, E4a, E4b (ported)
    def sig(u): return 1 / (1 + math.exp(-u)) if u >= 0 else math.exp(u) / (1 + math.exp(u))
    def qs_of(d, gam_=1.0): return chiS * pS * pS * YS / (gam_ * d)
    def G_of(d, q): return (AS + pS * q) / d
    def fate_E2(d1, d2, T, mode, kap, dt=0.01, Hpost=400.0):
        u = math.log(0.99 / 0.01); q = qs_of(d1); z = G_of(d1, q); t = 0.0
        while True:
            d = d2 if t < T else d1
            qstar_ = qs_of(d)
            if mode == 'QS': q = qstar_
            else: q = qstar_ + (q - qstar_) * math.exp(-kap * dt)
            G = G_of(d, q)
            zn = G + (z - G) * math.exp(-epsS * d * dt); u += zetaS * (0.5 * (z + zn) - 1) * dt; z = zn; t += dt
            if t > T + Hpost or u < -40 or (t > T and u > 12 and z > 1): break
        return 'undone' if u < 0 else 'captured'
    def tmin_E2(d1, d2, mode, kap):
        lo, hi = 0.0, 1.0
        while fate_E2(d1, d2, hi, mode, kap) == 'captured':
            hi *= 2
            if hi > 4000: return float('inf')
        for _ in range(22):
            m = (lo + hi) / 2
            if fate_E2(d1, d2, m, mode, kap) == 'captured': lo = m
            else: hi = m
        return hi
    d1 = 0.5
    print(f"(e) systems s5_joint2 E2: captured evaluation domain at d1={d1} (G={G_of(d1,qs_of(d1)):.3f}); reform raises d to d2 for T, then withdraws")
    print(f"    QS certificate restored for d2>0.638; with capacity frozen at its old level, only for d2>{(AS+pS*qs_of(d1)):.3f}")
    incs = []
    for d2 in (0.7, 1.0, 2.0):
        tq = tmin_E2(d1, d2, 'QS', None); tl = {k: tmin_E2(d1, d2, 'R', k) for k in (1.0, 0.3, 0.1, 0.03)}
        incs.append(tl[0.03] / tq - 1)
        print(f"   d2={d2}: minimal hold T: QS: {tq:.2f}  " + "  ".join(f"R({k}): {v:.2f}" for k, v in tl.items()) + f"  (R(0.03) +{100*(tl[0.03]/tq-1):.0f}%)")
    expect(all(0.05 < x < 0.15 for x in incs), f"s5 E2: the slowest lag lengthens the hold by {100*min(incs):.0f}-{100*max(incs):.0f}% (Sys I3: 6-14%); fast lags change it by under 1%")
    def Meq(D, dh, rh): return rh * (1 - D) / (dh * D + rh * (1 - D))
    def run_E4a(acor, dh, rh, w=1.0, H=600.0, dt=0.01, couple=True):
        actl_, d0_ = 0.2, 2.0; D0 = 0.2; M0 = Meq(D0, dh, rh); M = M0
        u = math.log(0.01 / 0.99); t = 0.0
        d = d0_; qst = chiS * pS * pS * YS / d; z = G_of(d, qst)
        while t < H:
            D = 1 - (1 - D0) * math.exp(-0.1 * t)
            M = M + dt * (-dh * D * M + rh * (1 - D) * (1 - M))
            dn = d0_ * math.exp(acor * t) * ((M / M0) ** w if couple else 1.0)
            gam_ = math.exp(-actl_ * t); q = chiS * pS * pS * YS / (gam_ * dn)
            G = G_of(dn, q)
            zn = G + (z - G) * math.exp(-epsS * dn * dt); u += zetaS * (0.5 * (z + zn) - 1) * dt; z = zn; t += dt
            if u > 0: return t
        return None
    def crit_E4a(dh, rh, couple):
        lo, hi = 0.0, 0.4
        for _ in range(16):
            m = (lo + hi) / 2
            if run_E4a(m, dh, rh, couple=couple) is not None: lo = m
            else: hi = m
        return lo
    print("(f) [humancorr] s5 E4a: delegation D(t)=1-0.8e^{-0.1t}; d_eff = d M/M0; largest alpha_cor with capture by t=600")
    e4a = []
    for dh, rh in ((0.05, 0.05), (0.1, 0.05), (0.2, 0.1)):
        un = crit_E4a(dh, rh, False); co = crit_E4a(dh, rh, True); e4a.append((dh, un, co))
        print(f"   delta_h={dh}, rho_h={rh}: uncoupled {un:.4f}; coupled {co:.4f}  (rate law 0.1; shifted law 0.1+delta_h={0.1+dh:.2f}); shift {co-un:+.4f}")
    expect(all(co > un for _, un, co in e4a) and e4a[0][2] < e4a[1][2] < e4a[2][2] and abs(e4a[0][2] - e4a[0][1] - 0.05) < 0.005 and abs(e4a[1][2] - e4a[1][1] - 0.1) < 0.01,
           "s5 E4a: delegation that erodes the corrector raises the finite-horizon threshold by about delta_h (0.049 and 0.094 for delta_h = 0.05, 0.1); "
           "at delta_h=0.2 with recovery rho_h=0.1 the shift is 0.135 (see notes)")
    def run_E4b(d, x0, dh, rh, kD, D0=0.1, w=0.5, H=1500.0, dt=0.01, M_init=None):
        M0 = Meq(D0, dh, rh)
        u = math.log(x0 / (1 - x0)); M = M0 if M_init is None else M_init
        deff = d * (M / M0) ** w; z = G_of(deff, qs_of(deff)) * x0 if x0 < 0.5 else G_of(deff, qs_of(deff)); t = 0.0
        while t < H:
            x = sig(u); D = min(1.0, D0 + kD * x)
            M = M + dt * (-dh * D * M + rh * (1 - D) * (1 - M))
            deff = d * (M / M0) ** w; G = G_of(deff, qs_of(deff))
            b = G * x * deff
            zt = b / deff
            zn = zt + (z - zt) * math.exp(-epsS * deff * dt); u += zetaS * (0.5 * (z + zn) - 1) * dt; z = zn; t += dt
            if u < -40: return 'absent'
            if u > 15 and t > 200: return 'captured'
        return 'captured' if u > 0 else 'absent'
    print("(g) [humancorr] s5 E4b: capture-delegation loop (D=0.1+kD x_ev, delta_h=0.2, rho_h=0.05, d_eff=d (M/M0)^0.5): smallest permanent d that undoes capture")
    dneed = []
    for kD in (0.0, 0.3, 0.6):
        dh, rh = 0.2, 0.05
        Mc = Meq(min(1.0, 0.1 + kD * 0.99), dh, rh)
        lo, hi = 0.3, 20.0
        for _ in range(30):
            m = (lo + hi) / 2
            if run_E4b(m, 0.99, dh, rh, kD, M_init=Mc) == 'captured': lo = m
            else: hi = m
        dneed.append(hi)
        print(f"   kD={kD}: d needed = {hi:.3f}  (captured-state M/M0 = {Mc/Meq(0.1,dh,rh):.3f}); x{hi/dneed[0]:.2f} the quasi-static reform")
    expect(dneed[0] < dneed[1] < dneed[2] and abs(dneed[0] - 0.638) < 0.01 and 1.5 < dneed[1] / dneed[0] < 1.7 and 2.5 < dneed[2] / dneed[0] < 2.8,
           f"s5 E4b: hysteresis of release: undoing capture needs {dneed[1]/dneed[0]:.2f}x and {dneed[2]/dneed[0]:.2f}x the quasi-static reform when capture makes delegation look safe")
    # ---------------------------------------------------------------- Math-Fable reviewer m5_quasistatic (ported)
    def run_m5(alpha, s_q, eta=1.0, g=0.2, d0=2.0, A=0.3, aB=1.0, c=1.0, eps=1.0, zeta=1.0, a=1.0, x0=0.01, T=250.0, dt=0.01):
        q = (1 / (1.0 * d0)) ** (1 / eta)
        z = A / d0; ux = math.log(x0 / (1 - x0)); t = 0.0
        fail_qs = None; fail_act = None; tcap = None; minratio = 1e9; maxratio = 0.0
        while t < T:
            gam_ = math.exp(-g * t); d = d0 * math.exp(alpha * t)
            qs = (1 / (gam_ * d)) ** (1 / eta)
            if fail_qs is None and (A + aB * qs) / (c * d) > 1: fail_qs = t
            if fail_act is None and a * z > c: fail_act = t
            if tcap is None and ux > 0: tcap = t
            r_ = q / qs; minratio = min(minratio, r_); maxratio = max(maxratio, r_)
            k = s_q * eta * qs / d
            nsub = max(1, int(k * dt / 0.05) + 1)
            if nsub > 2000:
                q = qs
            else:
                h = dt / nsub
                for _ in range(nsub):
                    u_ = math.log(q)
                    du = s_q * q * (1 / d - gam_ * q ** eta)
                    u_ += h * du
                    q = math.exp(min(u_, 700.0))
            E = math.exp(-eps * d * dt)
            z = z * E + (A + aB * q) / d * (1 - E)
            ux += dt * zeta * (a * z - c)
            t += dt
        return fail_qs, fail_act, tcap, minratio, maxratio
    print("(h) m5 (Math-Fable reviewer): multiplicative selection on capacity at speed s_q, jointly with one evaluation domain")
    fm = lambda v: ('%.1f' % v) if v is not None else 'never (T=250)'
    okM5 = True
    for eta in (1.0, 2.0):
        thr = 0.2 / (1 + eta)
        for alpha in (thr - 0.01, thr + 0.01):
            for s_q in (100.0, 1.0, 0.1, 0.01):
                fq, fa, tc, mn, mx = run_m5(alpha, s_q, eta=eta)
                if alpha > thr: okM5 &= fq is None and fa is None and tc is None
                elif s_q == 100.0: okM5 &= fa is not None and abs(fa - fq) < 0.5 and tc is not None
                print(f"   eta={eta} alpha_cor={alpha:.4f} ({'below' if alpha < thr else 'above'} {thr:.4f}) s_q={s_q:>6}: QS certificate fails {fm(fq)}; actual (a z > c) {fm(fa)}; captured {fm(tc)}; q/q* in [{mn:.3f}, {mx:.3f}]")
    expect(okM5, "m5: with fast selection the joint dynamics reproduce the rate law (actual failure = quasi-static failure, then capture); above the threshold nothing is captured; slow selection delays failure past the horizon")
    # ---------------------------------------------------------------- Math-Opus reviewer s4_cost (c) (ported)
    def qstar4(p_, chi, Y, d, f, xf, gam_, xv, eta):
        def dpay(q): return chi * p_ * p_ * Y / d - f * p_ ** xf - gam_ * p_ ** xv * q ** eta
        if dpay(0.0) <= 0: return 0.0
        lo, hi = -400.0, 400.0
        for _ in range(200):
            m = (lo + hi) / 2
            if dpay(math.exp(m)) > 0: lo = m
            else: hi = m
        return math.exp((lo + hi) / 2)
    def simulate4(alpha, mode, V=1.0, T=400.0, dt=0.01, xv=0.0, eta=1.0, g=0.2, d0=2.0, A=0.3, p_=0.6):
        q = qstar4(p_, 1, 1, d0, 0, 0, 1.0, xv, eta)
        t = 0.0; first = None; smax = 0
        if mode == 'replicator':
            L = [math.exp(-10 + 0.1 * i) for i in range(351)]
            x = [0.0] * len(L); j0 = min(range(len(L)), key=lambda i: abs(math.log(L[i]) - math.log(q))); x[j0] = 1.0
        while t < T:
            gam_ = math.exp(-g * t); d = d0 * math.exp(alpha * t)
            if mode == 'qs':
                q = qstar4(p_, 1, 1, d, 0, 0, gam_, xv, eta)
            elif mode == 'additive':
                q = max(0.0, q + dt * V * (p_ * p_ / d - gam_ * p_ ** xv * q ** eta))
            elif mode == 'log':
                q = q * math.exp(dt * V * q * (p_ * p_ / d - gam_ * p_ ** xv * q ** eta))
            elif mode == 'replicator':
                fit = [qq * p_ * p_ / d - gam_ * p_ ** xv * qq ** (1 + eta) / (1 + eta) for qq in L]
                mu = 1e-3
                mx = max(fit)
                xn = [x[i] * math.exp(max(-50.0, dt * V * (fit[i] - mx))) for i in range(len(L))]
                sn = sum(xn); xn = [v / sn for v in xn]
                xm = [0.0] * len(L)
                for i in range(len(L)):
                    xm[i] += xn[i] * (1 - mu * dt)
                    if i > 0: xm[i - 1] += xn[i] * mu * dt / 2
                    if i < len(L) - 1: xm[i + 1] += xn[i] * mu * dt / 2
                s_ = sum(xm); x = [v / s_ for v in xm]
                q = sum(a * b for a, b in zip(x, L))
            sE = (A + p_ * q) / d
            smax = max(smax, sE)
            if first is None and sE > 1: first = t
            t += dt
        return first, sE, q
    print("(i) s4_cost(c) (Math-Opus reviewer): quasi-static vs selection with finite speed (dominant share 0.6, rate law 0.1)"
          + ("" if FULL else "; replicator-with-mutation dynamics only with --full"))
    mlist = [('qs', None), ('additive', 1.0), ('additive', 100.0), ('log', 1.0), ('log', 100.0)] + ([('replicator', 1.0), ('replicator', 20.0)] if FULL else [])
    first4 = {}
    for alpha in (0.09, 0.11, 0.05, 0.0):
        out = []
        for mode, V in mlist:
            fc, sE, q = simulate4(alpha, mode, V=V if V else 1.0, T=300.0, dt=0.02 if mode != 'replicator' else 0.05)
            first4[(alpha, mode, V)] = fc
            out.append(f"{mode}{'' if V is None else '(V='+str(V)+')'}: first failure {('%.1f'%fc) if fc is not None else 'none by 300'}, s_E(T)={sE:.3g}")
        print(f"   alpha={alpha}: " + " | ".join(out), flush=True)
    expect(all(first4[(0.11, m, V)] is None for m, V in mlist) and
           all(first4[(a, m, V)] is None or first4[(a, m, V)] >= first4[(a, 'qs', None)] - 1e-9 for a in (0.0, 0.05, 0.09) for m, V in mlist),
           "s4_cost(c): above the threshold no dynamics fails; below it no dynamics fails earlier than quasi-static capacity (the worst case for a falling cost of control)")


def check_FF():
    block('FF', 'corrrate, costq', 'independent',
          'A per-unit cost floor f: falling f can stop cultivation (Codex); under [H_f] d_f rises at alpha_f and three cases decide; '
          'a lump-sum cost only delays cultivation (threshold exponent eta/(2eta+2-xi_v-eta xi_f)) and does not cap the requirement')
    # Sources (ported): planning/math-fable/f5_corrrate.py (B),(C); planning/math-opus/m06_corrrate.py (A),(B),(C);
    # ../v6.1/reviews/counterexamples_v61_codex.py case 4; ../v6.1/reviews/scripts-v6.1-math-opus/s7_Hf.py, s4_cost.py (b).
    # Claims (D2-fable s9(3), D2-opus s9(3)): cultivation only while d < d_f = chi Y/(f p^xi_f); under [H_f] d_f rises; the
    # certificate holds eventually iff alpha_cor > alpha_f, or = with no cultivation at the start, or the rate law holds;
    # alpha_cor > alpha_f alone does not protect the transient (Fable: fails at 38.4 although cultivation ends at 588).
    # ---------------------------------------------------------------- Codex case 4
    def cultivated(t):
        gamma = math.exp(-0.2 * t)
        d = 2 * math.exp(0.05 * t)
        f = 0.49 * math.exp(-0.01 * t)
        q = max(0.0, (1 / d - f) / gamma)
        return q, q / d
    cutoff = math.log(0.5 / 0.49) / 0.04
    rows = [(t, *cultivated(t)) for t in [0, 0.25, 0.5, 1, 10, 100]]
    ok4 = 0.01 < 0.05 < 0.2 / 2 and all(cultivated(t / 1000)[1] <= 0.005 + 1e-12 for t in range(1000)) and cultivated(1) == (0.0, 0.0)
    print(f"(a) Codex 4: eta=p=chiY=1, A=0, gamma=e^(-.2t), d=2e^(.05t), f=.49e^(-.01t): cultivation stops at t = {cutoff:.4f}; (t, q*, G): "
          + "; ".join(f"({t}, {q:.5f}, {G:.5f})" for t, q, G in rows))
    expect(ok4, "Codex 4: a falling positive floor stops cultivation at t=0.505 although alpha_cor=0.05 < alpha_ctl/(1+eta)=0.1; the certificate never fails")
    _codex(5, ok4)
    # ---------------------------------------------------------------- f5(B) (ported)
    p, A, d0, actl = 0.6, 0.3, 2.0, 0.2
    def gam(t): return math.exp(-actl * t)
    def dd(t, a): return d0 * math.exp(a * t)
    def qstar(t, a, f=0.0, eta=1.0):
        m = p * p / dd(t, a) - f
        return (m / gam(t)) ** (1 / eta) if m > 0 else 0.0
    def run_f(acor, af, f0, H=600.0, dt=0.02):
        t = 0.0; first = None; smax = 0.0; endcult = None
        while t < H:
            f = f0 * math.exp(-af * t); q = qstar(t, acor, f); d = dd(t, acor)
            if q == 0 and endcult is None and t > 0: endcult = t
            G = (A + p * q) / d
            if G > 1 and first is None: first = t
            smax = max(smax, G); t += dt
        return first, smax, endcult
    print("(b) f5(B): falling f: cultivation on iff d(t) < d_f(t) = p^2/f(t); alpha_ctl=.2, eta=1, alpha_f=0.05")
    tb = {}
    for f0 in (0.1, 0.17, 0.3):
        for acor in (0.05, 0.051, 0.06, 0.08, 0.11):
            fi, sm, ec = run_f(acor, 0.05, f0); tb[(f0, acor)] = (fi, ec)
            print(f"   f0={f0} (d_f(0)/d0={p*p/(f0*d0):.2f}), alpha_cor={acor}: first failure {('%.1f'%fi) if fi is not None else 'never'}, max G_ev {sm:.3g}, cultivation ends {('%.0f'%ec) if ec else 'never'}")
    expect(tb[(0.1, 0.051)][0] is not None and tb[(0.1, 0.051)][1] is not None and tb[(0.1, 0.051)][0] < tb[(0.1, 0.051)][1],
           f"f5(B): alpha_cor > alpha_f alone is not sufficient: f0=0.1, alpha_cor=0.051 fails at t={tb[(0.1,0.051)][0]:.1f} although cultivation ends at t={tb[(0.1,0.051)][1]:.0f}")
    # Finding (notes, FF): f5.py's printed reading says "alpha_cor = alpha_f: f0=0.17: 1.06>1 -> no cultivation, holds". With
    # d_f(0)/d0 = 1.06 > 1 cultivation is ON at the start (d0 < d_f(0)) and the f=0 rate law decides: the run fails at t=58.0.
    # The no-cultivation case at alpha_cor = alpha_f is f0 = 0.3 (d_f(0)/d0 = 0.60), which holds. D2-fable's statement is right.
    print(f"   [finding] at alpha_cor = alpha_f = 0.05: f0=0.1 (ratio 1.80) fails at {tb[(0.1,0.05)][0]:.1f}; f0=0.17 (ratio 1.06 > 1, cultivation at the start) "
          f"fails at {tb[(0.17,0.05)][0]:.1f}; f0=0.3 (ratio 0.60, none at the start) never fails. f5.py's printed note mislabels f0=0.17 as 'no cultivation, holds'")
    expect(tb[(0.1, 0.05)][0] is not None and tb[(0.17, 0.05)][0] is not None and tb[(0.3, 0.05)][0] is None,
           "f5(B): at alpha_cor = alpha_f the initial ratio decides: cultivation at the start (d0 < d_f(0)) -> the f=0 rate law (fails); none at the start -> holds")
    expect(all(tb[(f0, a)][0] is None for f0 in (0.1, 0.17, 0.3) for a in (0.06, 0.08, 0.11)), "f5(B): alpha_cor >= 0.06 never fails at any f0")
    df_ = [p * p / (0.3 * math.exp(-0.05 * t)) for t in (0, 10, 20)]
    print("   S4's 'that level falls at alpha_f': d_f(t)=p^2/f(t) with f falling RISES:", ", ".join(f"t={t}: {v:.3f}" for t, v in zip((0, 10, 20), df_)))
    expect(df_[0] < df_[1] < df_[2], "f5(B): d_f rises at alpha_f under [H_f] (1.200, 1.978, 3.262): V6.1's S4 had the sign wrong")
    # ---------------------------------------------------------------- m06(A),(B) (ported)
    def qstar6(chiY, d, f, gamma, eta=1.0, pxf=1.0, pxv=1.0):
        v = (chiY / d - f * pxf) / (gamma * pxv)
        return max(v, 0.0) ** (1 / eta)
    def certificate_path(alpha_ctl, alpha_cor, d0, f0, alpha_f, A=0.3, aB=1.0, cev=1.0, eta=1.0, chiY=1.0, T=400.0, dt=0.05):
        fail = None; held_end = None
        t = 0.0
        while t <= T:
            d = d0 * math.exp(alpha_cor * t); g = math.exp(-alpha_ctl * t); f = f0 * math.exp(-alpha_f * t)
            q = qstar6(chiY, d, f, g, eta)
            G = (A + aB * q) / (cev * d)
            if G >= 1 and fail is None: fail = t
            held_end = G < 1
            t += dt
        return fail, held_end
    print("(c) m06(B): [H_f] corrected rule vs eventual certificate (alpha_ctl=.2, eta=1, rate law .1)")
    print(f"   d_f(0)={1/0.2:.2f}, d_f(50)={1/(0.2*math.exp(-0.03*50)):.2f} for f0=.2, alpha_f=.03 (V6.1's S4 said this level 'falls')")
    agree = 0; tot = 0; mism = []
    for alpha_f in (0.02, 0.05):
        for alpha_cor in (0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.12):
            for (d0_, f0) in ((2.0, 0.1), (2.0, 0.6)):
                fail, held = certificate_path(0.2, alpha_cor, d0_, f0, alpha_f, T=1500.0, dt=0.25)
                cultivates0 = d0_ < 1 / f0
                pred = (alpha_cor > alpha_f) or (alpha_cor == alpha_f and not cultivates0) or (alpha_cor >= 0.1)
                tot += 1; agree += (pred == held)
                if pred != held: mism.append((alpha_f, alpha_cor, d0_, f0, held))
    print(f"   eventual certificate predicted by [alpha_cor > alpha_f, or = with no initial cultivation, or >= alpha_ctl/(1+eta)] in {agree} of {tot}; mismatches {mism}")
    expect(agree == tot == 32, "m06(B): the corrected three-case rule predicts the eventual certificate in 32/32")
    fail1, held1 = certificate_path(0.2, 0.05, 2.0, 0.1, 0.05, T=1500.0, dt=0.05)
    fail2, held2 = certificate_path(0.2, 0.05, 2.0, 0.6, 0.05, T=1500.0, dt=0.05)
    print(f"   alpha_cor = alpha_f = .05 with cultivation at the start (f0=.1): fails at t={fail1:.1f}, held at the end: {held1}; without (f0=.6): first failure {fail2}, held: {held2}")
    expect(fail1 is not None and not held1 and fail2 is None and held2, "m06(B): equal rates: initial cultivation decides (fails at 15.4 with it, holds without)")
    # ---------------------------------------------------------------- s7_Hf (Math-Opus reviewer, ported)
    def qstar7(p_, d, f, gam_, eta=1.0):
        m = p_ * p_ / d - f
        return (m / gam_) ** (1 / eta) if m > 0 else 0.0
    def run7(alpha, af, f0, g=0.2, d0=2.0, A=0.3, p_=0.6, T=600, dt=0.05):
        t = 0; first = None; last = None; smax = 0
        while t < T:
            d = d0 * math.exp(alpha * t); f = f0 * math.exp(-af * t); gam_ = math.exp(-g * t)
            sE = (A + p_ * qstar7(p_, d, f, gam_)) / d
            if sE > 1:
                if first is None: first = t
                last = t
            smax = max(smax, sE); t += dt
        return first, last, smax
    print("(d) s7_Hf (Math-Opus reviewer): is min{alpha_f, alpha_ctl/(1+eta)} the required rate? (alpha_f=0.05)")
    s7 = {}
    for f0 in (0.1, 0.17, 0.3):
        for alpha in (0.05, 0.06, 0.08):
            fi, la, sm = run7(alpha, 0.05, f0); s7[(f0, alpha)] = fi
            print(f"   f0={f0}, alpha_cor={alpha}: certificate first fails at {None if fi is None else round(fi,2)}, last failure {None if la is None else round(la,2)}, max s_E {sm:.3g}")
    expect(s7[(0.1, 0.05)] is not None and s7[(0.17, 0.05)] is not None and s7[(0.3, 0.05)] is None and all(s7[(f0, a)] is None for f0 in (0.1, 0.17, 0.3) for a in (0.06, 0.08)),
           "s7_Hf: at alpha_cor = alpha_f with cultivation at the start the certificate fails (37.1, 58.0); above alpha_f it holds")
    # ---------------------------------------------------------------- f5(C), m06(C), s4_cost(b): lump sum vs per-unit floor
    def qopt(pp, chi, Y, d, f, xf, g, xv, eta):
        def dpay(q): return chi * pp * pp * Y / d - f * pp ** xf - g * pp ** xv * q ** eta
        if dpay(0.0) <= 0: return 0.0
        lo, hi = -400.0, 400.0
        for _ in range(200):
            m = (lo + hi) / 2
            if dpay(math.exp(m)) > 0: lo = m
            else: hi = m
        return math.exp((lo + hi) / 2)
    def threshold(F, xf, xv, eta, lump):
        lo, hi = 1e-9, 1.0
        for _ in range(100):
            m = (lo + hi) / 2
            if lump:
                q = qopt(m, 1, 1, 1, 0, xf, 1, xv, eta)
                pos = q * m * m - m ** xv * q ** (1 + eta) / (1 + eta) - F * m ** xf > 0
            else:
                pos = qopt(m, 1, 1, 1, F, xf, 1, xv, eta) > 0
            if pos: hi = m
            else: lo = m
        return hi
    print("(e) f5(C) and s4_cost(b): lump-sum fixed cost F p^xf (paid iff q>0) vs the per-unit floor f p^xf q")
    okE = True
    for (xf, xv, eta) in [(0, 0, 1), (1, 1, 1), (0, 0, 2), (0, 1, 0.5)]:
        e_l = (math.log(threshold(2e-3, xf, xv, eta, True)) - math.log(threshold(1e-3, xf, xv, eta, True))) / math.log(2)
        e_f = (math.log(threshold(2e-3, xf, xv, eta, False)) - math.log(threshold(1e-3, xf, xv, eta, False))) / math.log(2)
        okE &= abs(e_l - eta / (2 * eta + 2 - xv - eta * xf)) < 1e-3 and abs(e_f - 1 / (2 - xf)) < 1e-3
        print(f"   xf={xf} xv={xv} eta={eta}: lump-sum threshold exponent {e_l:.4f} (eta/(2eta+2-xv-eta xf)={eta/(2*eta+2-xv-eta*xf):.4f}); per-unit floor exponent {e_f:.4f} (1/(2-xf)={1/(2-xf):.4f})")
    def dstar(g, F, lump):
        def G(d):
            if lump:
                q = qopt(p, 1, 1, d, 0, 0, g, 0, 1.0); prof = q * p * p / d - g * q * q / 2 - F
                q = q if prof > 0 else 0.0
            else: q = qopt(p, 1, 1, d, F, 0, g, 0, 1.0)
            return (A + p * q) / d
        lo, hi = 1e-6, 1e9
        for _ in range(200):
            m = math.sqrt(lo * hi)
            if G(m) > 1: lo = m
            else: hi = m
        return hi
    ds = {}
    for g in (1.0, 1e-2, 1e-4, 1e-6, 1e-8):
        ds[g] = (dstar(g, 0.3, False), dstar(g, 0.3, True), dstar(g, 0.0, False))
        print(f"   gamma={g:.0e}: required d* with per-unit floor f=0.3: {ds[g][0]:.3f}; with lump-sum F=0.3: {ds[g][1]:.3f}; with f=0: {ds[g][2]:.3f}")
    expect(okE and abs(ds[1e-8][0] - p * p / 0.3) < 1e-3 and ds[1e-8][1] > 1000 and ds[1e-8][1] / ds[1e-6][1] > 9,
           "f5(C)/s4_cost(b): lump-sum threshold exponents eta/(2eta+2-xi_v-eta xi_f) and per-unit 1/(2-xi_f) in 4/4; the per-unit floor caps d* at p^2/f = 1.2, a lump sum does not (d* ~ 1/gamma)")
    def lump_sum_q(chiY, d, F, gamma, p_, eta, xi_v, xi_f):
        Yp = chiY * p_ * p_
        q = (Yp / (d * gamma * p_ ** xi_v)) ** (1 / eta)
        gain = Yp * q / d - gamma * p_ ** xi_v * q ** (1 + eta) / (1 + eta)
        return q if gain > F * p_ ** xi_f else 0.0
    print("(f) m06(C): lump-sum threshold exponent in F by bisection on p (four settings incl. fractional xi_v, xi_f); d*(gamma) with A=0, p=1")
    okC = True
    for (eta, xi_v, xi_f) in ((1, 0, 0), (1, 1, 0), (2, 0, 0.5), (0.5, 0.3, 1)):
        ps = []
        for F in (1e-4, 1e-6):
            lo, hi = 1e-9, 1.0
            for _ in range(200):
                mid = math.sqrt(lo * hi)
                if lump_sum_q(1.0, 1.0, F, 1.0, mid, eta, xi_v, xi_f) > 0: hi = mid
                else: lo = mid
            ps.append(hi)
        expo = math.log(ps[0] / ps[1]) / math.log(1e-4 / 1e-6)
        okC &= abs(expo - eta / (2 + 2 * eta - xi_v - eta * xi_f)) < 1e-3
        print(f"   eta={eta} xi_v={xi_v} xi_f={xi_f}: threshold exponent in F {expo:.4f}; eta/(2+2eta-xi_v-eta xi_f) = {eta/(2+2*eta-xi_v-eta*xi_f):.4f}; per-unit floor 1/(2-xi_f) = {1/(2-xi_f):.4f}")
    dl_ = {}
    for gm in (1e-2, 1e-4, 1e-6, 1e-8):
        def G_lump(d): return lump_sum_q(1.0, d, 0.3, gm, 1.0, 1, 0, 0) / d
        def G_unit(d): return qstar6(1.0, d, 0.3, gm) / d
        out = []
        for Gf in (G_lump, G_unit):
            lo, hi = 1e-6, 1e9
            for _ in range(300):
                mid = math.sqrt(lo * hi)
                if Gf(mid) >= 1: lo = mid
                else: hi = mid
            out.append(hi)
        dl_[gm] = out
        print(f"   gamma={gm:.0e}: d* lump-sum {out[0]:.2f}; d* per-unit floor {out[1]:.4f} (levels off at chiY/f = {1/0.3:.4f})")
    expect(okC and abs(dl_[1e-8][1] - 1 / 0.3) < 1e-3 and abs(dl_[1e-8][0] - 1e4) / 1e4 < 1e-3,
           "m06(C): lump-sum exponents 0.2500, 0.3333, 0.4000, 0.2273 match; d* = 10, 100, 1000, 10000 under a lump sum against 3.03 -> 3.33 under a per-unit floor")


def check_SR():
    block('SR', 'slowroute, masking', 'independent',
          'Silent crossing when capture precedes evidence: the two clocks (host to the alarm band; captured evaluation past the masking threshold)')
    # Sources (ported): planning/math-fable/f7_misc.py (F); ../v6.1/reviews/scripts-v6.1-systems/s5_joint2.py (E3) and
    # s5b_clocks.py (E3' at alpha_cor = 0), with s4_joint.py's capacity model; plus an independent integration of T_A.
    # Claims (D2-fable s10, D2-opus s10): (b),(c) give x_ev -> 1 but do not imply (e), which compares two clocks; with (b),
    # (c) and T_cap < T_A in place of (e) the theorem holds; a slower adjustment of capacity can reverse the order.
    print("(a) f7(F): logistic capture of evaluation with midpoint 'mid'; host under the race load (rho=.05, h_V=.08); floor .3, alarm .6, m_in=.5")
    rho, h, Vmin, Val, m_in, m_out = 0.05, 0.08, 0.3, 0.6, 0.5, 0.0
    m_fl = (Val - Vmin) / (1 - Vmin); thr = (m_fl - m_out) / (m_in - m_out)
    res = {}
    for mid in (0.0, 20.0, 45.0):
        V = 1.0; x = 0.0; t = 0.0; dt = 0.01; alarm = None; cross = None
        while t < 200 and cross is None:
            x = 1 / (1 + math.exp(-(t - mid) / 2))
            m = x * m_in + (1 - x) * m_out; Vt = V + m * (1 - V)
            if alarm is None and Vt <= Val: alarm = t
            if V < Vmin: cross = t
            V += dt * V * (rho * (1 - V) - h * 1.0); t += dt
        res[mid] = (alarm, cross)
        print(f"   capture midpoint {mid}: x_ev crosses threshold {thr:.3f} at t={mid+2*math.log(thr/(1-thr)):.1f}; alarm at {alarm if alarm is None else round(alarm,1)}; floor crossed at {round(cross,1) if cross else None} -> "
              f"{'silent crossing (e holds)' if (alarm is None or alarm > cross) else 'alarm before the floor (e fails although x_ev -> 1)'}")
    expect(res[0.0][0] is None and abs(res[0.0][1] - 21.0) < 0.1 and all(res[m][0] is not None and res[m][0] < res[m][1] for m in (20.0, 45.0)),
           f"f7(F): capture complete by t=3.6 -> silent crossing at t=21.0; capture midpoints 20 and 45 -> alarm at t=7.4 before the floor: (b),(c) do not imply (e)")
    # ---------------------------------------------------------------- s5_joint2 E3 and s5b E3' (ported; s4's capacity model)
    pS, AS = 0.6, 0.3; actlS, d0S = 0.2, 2.0; zetaS, epsS = 1.0, 0.5
    def gamS(t): return math.exp(-actlS * t)
    def ddS(t, acor): return d0S * math.exp(acor * t)
    def qstarS(t, acor): return pS * pS / (gamS(t) * ddS(t, acor))
    q0S = qstarS(0, 0.0)
    def qrate(mode, par, t, q):
        if mode == 'R': return par
        if mode == 'GA': return par * gamS(t)
        if mode == 'GM': return (par / q0S ** 2) * q * q * gamS(t)
    def sig(u): return 1 / (1 + math.exp(-u)) if u >= 0 else math.exp(u) / (1 + math.exp(u))
    def E3(mode, par, acor=0.05, rho=0.05, hV=0.08, sP=0.12, P0=0.05, Va=0.6, Vm=0.3, m_in=0.5, m_out=0.05, dt=0.01, H=200):
        V = 1.0; P = P0; t = 0.0
        u = math.log(0.01 / 0.99); q = q0S; z = (AS + pS * q0S) / d0S
        while t < H:
            tm = t + dt / 2; d = ddS(tm, acor); qst = qstarS(tm, acor)
            if mode == 'QS': qq = qst
            else:
                k = qrate(mode, par, tm, q); qn = qst + (q - qst) * math.exp(-k * dt); qq = 0.5 * (q + qn); q = qn
            G = (AS + pS * qq) / d; zn = G + (z - G) * math.exp(-epsS * d * dt); u += zetaS * (0.5 * (z + zn) - 1) * dt; z = zn
            x = sig(u); m = x * m_in + (1 - x) * m_out
            P += dt * sP * P * (1 - P); E = P
            V += dt * V * (rho * (1 - V) - hV * E)
            t += dt
            if V + m * (1 - V) <= Va: return ('alarm', round(t, 1), round(V, 3), V >= Vm, round(x, 2))
            if V < Vm - 0.1: return ('none', round(t, 1), round(V, 3), False, round(x, 2))
        return ('horizon', None, None, None, None)
    def show(r): return (f"alarm at t={r[1]} with V={r[2]} ({'before' if r[3] else 'AFTER'} the floor); x_ev={r[4]}" if r[0] == 'alarm'
                         else f"no alarm; V={r[2]} at t={r[1]}; x_ev={r[4]}")
    print("(b) s5 E3: the two clocks with capture endogenous (alpha_cor=0.05; m_in=0.5 > m_fl=0.43; floor 0.3, alarm 0.6; race share from 0.05 at rate 0.12)")
    e3 = {}
    print(f"   independent evaluation (x_ev=0): {show(E3('QS', None, m_in=0.05))}")
    for m, par in (('QS', None), ('R', 1.0), ('R', 0.1), ('R', 0.03), ('GA', 1.0)):
        e3[(m, par)] = E3(m, par); print(f"   {m}{'' if par is None else '('+str(par)+')'}: {show(e3[(m, par)])}")
    print("(c) s5b E3': alpha_cor=0 so that the capture clock and the host clock are comparable")
    e3b = {}
    print(f"   independent: {show(E3('QS', None, acor=0.0, m_in=0.05))}")
    for m, par in (('QS', None), ('R', 1.0), ('R', 0.1), ('R', 0.03), ('GA', 1.0)):
        e3b[(m, par)] = E3(m, par, acor=0.0); print(f"   {m}{'' if par is None else '('+str(par)+')'}: {show(e3b[(m, par)])}")
    expect(all(r[0] == 'alarm' and r[3] for r in e3.values()) and
           all(e3b[k][0] == 'alarm' and not e3b[k][3] for k in (('QS', None), ('R', 1.0), ('R', 0.1))) and
           all(e3b[k][0] == 'alarm' and e3b[k][3] for k in (('R', 0.03), ('GA', 1.0))),
           "s5 E3/E3': at alpha_cor=0.05 capture is too slow and the alarm fires before the floor under every dynamics; at alpha_cor=0 capture wins "
           "(silent until V=0.200 at t=58.8) under QS and fast lags, while slow adjustment (R(0.03), additive) reverses the clocks")
    # ---------------------------------------------------------------- T_A against direct integration [independent]
    print("(d) [independent] T_A = (rho-h_V e)^-1 ln[(1-V*/V0)/(1-V*/V_alarm)], V* = 1-h_V e/rho, against direct integration of the host")
    okT = True
    for (rho_, hV_, e_, V0_, Va_) in ((0.05, 0.08, 0.4, 1.0, 0.6), (0.05, 0.08, 0.5, 1.0, 0.5), (0.1, 0.2, 0.3, 0.9, 0.6)):
        Vs = 1 - hV_ * e_ / rho_
        TA = math.log((1 - Vs / V0_) / (1 - Vs / Va_)) / (rho_ - hV_ * e_)
        V = V0_; t = 0.0; dt = 1e-3
        while V > Va_:
            k1 = V * (rho_ * (1 - V) - hV_ * e_); k2 = (V + dt / 2 * k1) * (rho_ * (1 - (V + dt / 2 * k1)) - hV_ * e_)
            k3 = (V + dt / 2 * k2) * (rho_ * (1 - (V + dt / 2 * k2)) - hV_ * e_); k4 = (V + dt * k3) * (rho_ * (1 - (V + dt * k3)) - hV_ * e_)
            V += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += dt
        okT &= abs(t - TA) < 2e-3
        print(f"   rho={rho_}, h_V={hV_}, load {e_}: V*={Vs:.3f}; T_A formula {TA:.3f}; integrated {t:.3f}")
    expect(okT, "T_A formula (stated in the Scope of slowroute) equals the integrated time to the alarm band in 3/3")


def check_ES():
    block('ES', 'enforce, relpunish, restraint, require (R4)', 'independent; (f) identity (exact rationals)',
          'Explicit-action enforcement: per-deviation p_d; exclusive vs independent breakouts; the P<v<C window; '
          'best response over all deviation plans; the R4 exception; exchangeable vs label-dependent continuations')
    # Sources (ported): planning/math-fable/f6_enforce.py (A)-(D); planning/math-opus/m07_enforce.py (A)-(E), m08_relpunish.py (C);
    # ../v6.1/reviews/scripts-v6.1-math-opus/s3_enforce.py (1)-(4); ../v6.1/reviews/scripts-v6.1-math-fable/m6_misc.py (2),(5);
    # ../v6.1/reviews/counterexamples_v61_codex.py case 6 (stochastic punishment asymmetry).
    # Claims (D2-fable s11-12, D2-opus s11-12): (14) per deviation; (5) needs q <= 1/2 (independent: q -> q(1-q));
    # P<v<C example; best response over plans agrees with (14) where the punishment is credible; R4's exception is
    # (1-delta)g <= delta(C-D); Cor 5.5 needs an exchangeable continuation.
    def cond(g, pd, C, D, v, dl): return (1 - dl) * g + dl * pd * (D - C) <= dl * (1 - pd) * (C - v) + 1e-12
    print("(a) f6(A)/m07(A)/m6(2): per-deviation p_d (C=3, D=6, v=1, delta=.9): deviation X (g=1.0, p_d=.1), deviation Y (g=.2, p_d=.6)")
    dl, C, D, v = 0.9, 3.0, 6.0, 1.0
    Vc = C / (1 - dl); verdict = {}
    for name, g, pd in (("X", 1.0, 0.1), ("Y", 0.2, 0.6)):
        Vd = C + g + dl * (pd * D / (1 - dl) + (1 - pd) * v / (1 - dl)); verdict[name] = Vc >= Vd
        lhs = (1 - dl) * g + dl * pd * (D - C); rhs = dl * (1 - pd) * (C - v)
        print(f"   deviation {name}: V_coop={Vc:.2f}, V_dev={Vd:.2f} -> {'deterred' if Vc>=Vd else 'NOT deterred'}; temptation {lhs:.3f}, remaining sanction {rhs:.3f}")
    expect(verdict['X'] and not verdict['Y'], "per-deviation p_d: the larger-g deviation is deterred (17.5 < 30), the quiet one with p_d=0.6 is not (39.2 > 30)")
    def vP_excl(P, D, U, q, dl): return ((1 - dl) * P + dl * q * (D + U)) / (1 - dl + 2 * dl * q)
    def vP_indep(P, D, U, q, dl):
        qq = q * (1 - q); return ((1 - dl) * P + dl * qq * (D + U)) / (1 - dl + 2 * dl * qq)
    def vP_sim(P, D, U, q, dl, indep, T=4000):
        V = 0.0
        for _ in range(T):
            if indep:
                pi = q * (1 - q); pj = q * (1 - q); pboth = q * q; pnone = (1 - q) ** 2
                V = P + dl * (pi * D / (1 - dl) + pj * U / (1 - dl) + (pboth + pnone) * V)
            else:
                V = P + dl * (q * D / (1 - dl) + q * U / (1 - dl) + (1 - 2 * q) * V)
        return (1 - dl) * V
    print("(b) f6(B): 5.4(5): punishment = reversion to the race with breakouts; closed forms vs value iteration on the explicit chain")
    dl, P, D, U, C = 0.9, 0.0, 4.0, 0.0, 1.0; okB = True
    for q in (0.045, 0.1, 0.3):
        a1, a2, b1, b2 = vP_excl(P, D, U, q, dl), vP_sim(P, D, U, q, dl, False), vP_indep(P, D, U, q, dl), vP_sim(P, D, U, q, dl, True)
        okB &= abs(a1 - a2) < 1e-9 and abs(b1 - b2) < 1e-9
        print(f"   q={q}: v exclusive {a1:.4f} (VI {a2:.4f}); v independent {b1:.4f} (VI {b2:.4f})")
    g = 2.0; q = 0.045; v_ = vP_excl(P, D, U, q, dl)
    det0 = cond(g, 0, C, C, P, dl); det1 = cond(g, 0, C, C, v_, dl)
    print(f"   example C=1, P=0, D=4, U=0, g=2, delta=.9, q=.045: v={v_:.3f} < C; deviation (p_d=0) deterred at q=0: {det0}; at q=.045: {det1}")
    print(f"   V6.1's example (g=.5, q=.1): v={vP_excl(P,D,U,0.1,dl):.3f} > C: the race-with-breakouts is preferred to cooperation itself (kept in S5 for that point)")
    print(f"   q=.6 exclusive: 1-2q={1-1.2:+.1f} (invalid); independent form stays valid: v={vP_indep(P,D,U,0.6,dl):.4f}")
    expect(okB and det0 and not det1 and abs(v_ - 0.895) < 1e-3 and abs(vP_indep(P, D, U, 0.6, dl) - 1.6241) < 1e-4,
           "f6(B): closed forms equal the explicit chain (exclusive and independent); new example deterred at q=0, not at q=0.045 with v=0.895 < C; independent form valid at q=0.6 (v=1.6241)")
    def punishment_value(P, D, U, q, delta, iters=20000):
        VP = 0.0
        for _ in range(iters):
            VP = P + delta * (q * D / (1 - delta) + q * U / (1 - delta) + (1 - 2 * q) * VP)
        return (1 - delta) * VP
    print("(c) m07(B): the window q in (0.0354, 0.0556): deterrence fails while the punishment is still worse than cooperation (C=1, P=0, D=4, D-=0, g=2)")
    C, P, D, U, g, dl = 1.0, 0.0, 4.0, 0.0, 2.0, 0.9; win = {}
    for q in (0.0, 0.02, 0.035, 0.036, 0.045, 0.055, 0.056, 0.1):
        v_chain = punishment_value(P, D, U, q, dl)
        ok = cond(g, 0.0, C, D, v_chain, dl); win[q] = (ok, v_chain < C)
        print(f"   q={q:.3f}: v chain {v_chain:.4f}; v<C: {v_chain < C}; restraint enforceable at p_d=0: {ok}")
    expect(all(win[q][0] for q in (0.0, 0.02, 0.035)) and all((not win[q][0]) and win[q][1] for q in (0.036, 0.045, 0.055)) and not win[0.056][1],
           "m07(B): enforceable at q <= 0.035; not at 0.036-0.055 although v < C; at 0.056 v > C")
    # ---------------------------------------------------------------- m07(C): explicit-action best response over all plans
    def explicit_game(C, g, S, P, SP, D, U, q, h, delta, iters=3000):
        pd = 1 - (1 - q) ** h
        VD, VU = D / (1 - delta), U / (1 - delta)
        Vc = Vp = 0.0
        for _ in range(iters):
            race = P + delta * (q * VD + q * VU + (1 - 2 * q) * Vp)
            quit = SP + delta * (q * VU + (1 - q) * Vp)
            Vp_new = max(race, quit)
            stay = C + delta * Vc
            dev = (C + g) + delta * (pd * VD + (1 - pd) * Vp)
            Vc_new = max(stay, dev)
            Vc, Vp = Vc_new, Vp_new
        sustained = Vc <= C / (1 - delta) + 1e-7 * (1 + abs(Vc))
        race_val = P + delta * (q * VD + q * VU + (1 - 2 * q) * Vp)
        quit_val = SP + delta * (q * VU + (1 - q) * Vp)
        credible = race_val >= quit_val - 1e-9
        return sustained, credible, pd, (1 - delta) * Vp
    Ngames = 20000
    print(f"(d) m07(C): explicit-action stochastic game: player 1's best response over all deviation plans (value iteration on the MDP) vs (14) with v from (5); {Ngames:,} random settings")
    rr = random.Random(5); agree = 0; tot = 0; cred_fail = 0; sus = 0; dis = []
    for _ in range(Ngames):
        C = 1.0; g = rr.uniform(0.05, 3); P = rr.uniform(-1, 0.9); SP = P - rr.uniform(0.01, 2)
        D = rr.uniform(-0.5, 6); U = rr.uniform(-6, 0.5); q = rr.uniform(0, 0.5); h = rr.choice([1, 2, 3, 5])
        delta = rr.uniform(0.5, 0.99); S = rr.uniform(-2, 1)
        sustained, credible, pd, v_ = explicit_game(C, g, S, P, SP, D, U, q, h, delta)
        v5 = ((1 - delta) * P + delta * q * (D + U)) / (1 - delta + 2 * delta * q)
        pred = cond(g, pd, C, D, v5, delta)
        tot += 1; sus += sustained
        if not credible: cred_fail += 1
        else:
            agree += (pred == sustained)
            if pred != sustained and len(dis) < 5: dis.append((round(g, 3), round(P, 3), round(D, 3), round(U, 3), round(q, 3), h, round(delta, 3)))
    print(f"   cooperation sustained in {sus}; punishment not credible (quitting the race pays) in {cred_fail}; where credible, (14) agrees with the best response in {agree} of {tot-cred_fail}; disagreements {dis}")
    expect(agree == tot - cred_fail and cred_fail > 0, f"m07(C): best response over plans agrees with (14) in {agree}/{tot-cred_fail} credible settings; in {cred_fail} the punisher prefers to quit, where (5) is not the credible value")
    print("(e) m07(D)/f6(C)/s3(4): R4 with D < C: C=1, D=.9, v=0, g=2, delta=.9")
    def pbar(g, C, D, v, delta): return 1 - ((1 - delta) * g + delta * (D - C)) / (delta * (D - v))
    C, D, v, g, dl = 1.0, 0.9, 0.0, 2.0, 0.9
    pb = pbar(g, C, D, v, dl); r4 = {pd: cond(g, pd, C, D, v, dl) for pd in (0.8, 0.86, 0.87, 0.9)}
    print(f"   p_bar={pb:.4f}; (14) holds at p_d=0.8, 0.86, 0.87, 0.9: {list(r4.values())}")
    r4b = [cond(0.5, pd, 1.0, 0.9, 0.0, dl) for pd in (0, 0.5, 0.9, 1.0)]
    print(f"   (1-delta)g={0.1*0.5:.3f} <= delta(C-D)={dl*0.1:.3f} with g=0.5: sustained at p_d = 0, .5, .9, 1: {r4b}")
    expect(abs(pb - 0.8642) < 1e-4 and r4[0.86] and not r4[0.87] and not r4[0.9] and all(r4b),
           "R4: D < C does not exempt (p_bar = 0.8642; (14) fails at p_d = 0.87, 0.9); (1-delta)g <= delta(C-D), i.e. p_bar >= 1, exempts at every p_d")
    print("(f) [identity] s3(1) (Math-Opus reviewer): V_coop >= V_dev vs (14), exact rationals, 20,000 draws")
    from fractions import Fraction as Fr
    rq = random.Random(99); bad = 0
    for _ in range(20000):
        dlf = Fr(rq.randint(1, 99), 100); pdf = Fr(rq.randint(0, 100), 100)
        Cf, gf, Df, vf = (Fr(rq.randint(-300, 300), 100) for _ in range(4))
        Vcf = Cf / (1 - dlf); Vdf = Cf + gf + dlf * (pdf * Df / (1 - dlf) + (1 - pdf) * vf / (1 - dlf))
        lhs = (1 - dlf) * gf + dlf * pdf * (Df - Cf); rhs = dlf * (1 - pdf) * (Cf - vf)
        if (Vcf >= Vdf) != (lhs <= rhs): bad += 1
    print(f"   disagreements {bad} -> EC tests the valuation (algebra) only; the incentives are tested in (d)")
    expect(bad == 0, "s3(1): EC's 'direct values' are (14) rearranged (exact rationals, 0/20,000): EC is a valuation check")
    print("(g) s3(2),(3) (Math-Opus reviewer): q-windows by g; credibility of racing in punishment; monotonicity of p_bar at its edge")
    C, P, D, U, dl = 1.0, 0.0, 4.0, 0.0, 0.9; wins = {}
    for g in (0.5, 2.0, 5.0):
        lo = hi = None
        for k in range(1, 5000):
            q = k / 10000; v_ = vP_excl(P, D, U, q, dl)
            fails = (1 - dl) * g > dl * (C - v_)
            if fails and v_ < C and lo is None: lo = q
            if v_ < C: hi = q
        wins[g] = (lo, hi)
        print(f"   g={g}: q-window with v<C yet reversion fails to deter (deters at q=0: {(1-dl)*g <= dl*(C-P)}): [{lo}, {hi}]")
    cred = []
    for S_ in (-0.5, 0.0):
        q = 0.03; VP = vP_excl(P, D, U, q, dl) / (1 - dl); dev = S_ + dl * (q * U / (1 - dl) + (1 - q) * VP)
        cred.append(VP >= dev)
        print(f"   credibility, S={S_}, q={q}: racing in punishment worth {VP:.3f}, restraining one period {dev:.3f} -> racing a best response: {VP >= dev}")
    g0 = (0.9 * (3 - 1)) / 0.1
    dpb = (pbar(g0, 3, 4 + 1e-6, 1, 0.9) - pbar(g0, 3, 4, 1, 0.9)) / 1e-6
    print(f"   at p_bar=0 (g={g0:.1f}): dp_bar/dD = {dpb:.2e} (zero, not negative: monotonicities are weak at the edges of [0,1))")
    expect(wins[0.5] == (0.0498, 0.0555) and wins[2.0] == (0.0354, 0.0555) and wins[5.0] == (0.0159, 0.0555) and all(cred) and abs(dpb) < 1e-6,
           "s3(2,3): windows [0.0498,0.0555], [0.0354,0.0555], [0.0159,0.0555] for g=0.5, 2, 5 (not knife-edge); racing credible; dp_bar/dD = 0 at p_bar = 0")
    print("(h) m07(E): homogeneity of p_bar in (g, C, D, v)")
    g, C, D, v, dl = 1.0, 1.0, 3.0, 0.0, 0.9
    base = pbar(g, C, D, v, dl); hom = []
    for s_ in (2, 10):
        a, b = pbar(s_ * g, s_ * C, s_ * D, s_ * v, dl), pbar(s_ * g, C, s_ * D, v, dl); hom.append((a, b))
        print(f"   all stakes x{s_}: {a:.4f} (base {base:.4f}); only g and D x{s_}: {b:.4f}")
    expect(all(abs(a - base) < 1e-12 for a, _ in hom) and hom[0][1] < base and abs(hom[1][1] + 0.0037) < 1e-4,
           "m07(E): p_bar is homogeneous of degree zero (0.2963 at x2, x10); scaling only g and D lowers it (0.1296, -0.0037): the stakes arm needs g and D to outgrow C-v")
    print("(i) m6(5) (Math-Fable reviewer): v = [(1-d)P + d q (D+U)]/(1-d+2dq) with q=0.6: the 'neither' probability 1-2q is negative")
    for q in (0.3, 0.5, 0.6):
        print(f"   q={q}: 1-2q = {1-2*q:+.2f}; v = {((1-0.9)*0.0 + 0.9*q*(3.0-2.0))/(1-0.9+2*0.9*q):.4f}")
    # ---------------------------------------------------------------- continuations: exchangeable vs label-dependent (relpunish)
    print("(j) f6(D)/m08(C)/Codex 6: the continuation premise of Corollary 5.5 (two actors, theta=-1, delta=.9)")
    dl = 0.9
    def rel_value_mirror(eP, eI, T=2000, qe=0.3):
        V = 0.0
        for _ in range(T):
            pwin = eI / (eI + eP)
            V = 0.0 + dl * (qe * (pwin * 10 / (1 - dl) + (1 - pwin) * (-10) / (1 - dl)) + (1 - qe) * V)
        return (1 - dl) * V
    mir = rel_value_mirror(1.0, 1.0)
    print(f"   (i) exchangeable lottery continuation: mirrored strategy gives the punished normalized relative value {mir:+.6f}")
    V = 0.0
    for _ in range(2000): V = dl * (0.5 * (-10) / (1 - dl) + 0.5 * V)
    dev_lab = 4 + dl * V
    print(f"   (ii) label-dependent continuation (target gets -10 w.p. .5 whatever it does): normalized value {(1-dl)*V:+.4f}; deviation worth {dev_lab:.2f} < 0 -> cooperation sustained among relative actors")
    Vs = 0.0
    for _ in range(5000): Vs = dl * (0.25 * 10 / (1 - dl) + 0.25 * (-10) / (1 - dl) + 0.5 * Vs)
    dev_sym = 4 + dl * Vs
    print(f"   (iii) m08(C): symmetric variant (absorbing prize to either player w.p. .25 each): punishment value {(1-dl)*Vs:.4f}; deviation worth {dev_sym:.3f} > 0: not sustained")
    discount, q, terminal = 0.9, 0.5, -10.0
    pv_ = 0.0
    for _ in range(1000): pv_ = discount * (q * terminal / (1 - discount) + (1 - q) * pv_)
    dv_ = 4 + discount * pv_
    ok6 = pv_ < 0 and dv_ < 0
    print(f"   Codex 6 (ported): normalized punishment {(1-discount)*pv_:.4f}; deviation value {dv_:.3f}; cooperation value 0")
    expect(abs(mir) < 1e-12 and abs((1 - dl) * V + 8.1818) < 1e-4 and dev_lab < 0 and abs(dev_sym - 4) < 1e-9 and ok6,
           "relpunish: an exchangeable continuation leaves the punished at 0; a label-dependent one holds it at -8.18 (deviation -69.6), sustaining non-stage cooperation; the symmetric variant does not")
    _codex(7, ok6)


def check_JX():
    block('JX', 'scissors, detectlink, jointscissors (S5), zonesillus, enforce, standprice',
          'independent: (a)-(c) direct valuation, (e) Monte Carlo of the clock; (d), and (e)\'s deviation values, identity (the one-period reduction); (f),(g) one reduced model [num, rivals not responding]',
          'The scissors arm by arm in reduced form (direct discounted streams); Test G; the detect link; the joint scissors model')
    # Sources (ported): planning/math-opus/m10_scissors.py (A),(B),(C); planning/math-fable/f6_enforce.py (F);
    # ../v6.1/reviews/scripts-v6.1-systems/s3_zones.py; the two unit drafts' proposed JX scripts,
    # planning/drafts/U05/A/checks/jx_joint_scissors.py (A)-(E) and planning/drafts/U05/B/scripts/jx_joint.py (A)-(E)
    # (both ported, since the merge of U05 has not chosen between them; their models differ and both are labelled).
    # Claims (plan s3 'scissors', D1-opus s2.3, D2-opus s14): 0.9495 not 0.99; the restraint gap is monotone in p_d at
    # D=C and humped for D>C; p_d = 1 - upsilon(T_dec), (14) reads upsilon >= 1 - p_bar, and Prop 8.10's threshold
    # (T-R)/(T-P+F) is the same number under the continuation reading; in one reduced joint model the blades meet when
    # stakes outgrow provision and stay apart when provision grows with the stakes.
    n, b, c, dd, eps, delta = 4, 1.0, 0.3, 0.2, 1.0, 0.9
    A = eps * (b - dd) - c; B = eps * (b / (n - 1) + dd); K = c + n * eps * dd
    def sustained(theta, pd, D=0.0):
        coop = 0.0
        dev = (A - theta * B) + delta * (pd * D + (1 - pd) * (-K * (1 + theta))) / (1 - delta)
        return dev <= coop + 1e-12
    def theta_of(theta0, Grel, Gcom=0.0):
        rho = (1 + theta0) / (n - 1 - theta0) * (1 - Grel) / (1 - Gcom)
        return (rho * (n - 1) - 1) / (1 + rho)
    def largest_G(theta0, pd, Gcom=0.0):
        if not sustained(theta_of(theta0, 0.0, Gcom), pd): return None
        lo, hi = 0.0, 0.999999
        if sustained(theta_of(theta0, hi, Gcom), pd): return hi
        for _ in range(80):
            mid = (lo + hi) / 2
            if sustained(theta_of(theta0, mid, Gcom), pd): lo = mid
            else: hi = mid
        return lo
    print("(a) m10(A): largest enforceable discounted relative loop gain by p_d (binary game n=4, b=1, c=.3, d=.2, eps=1, delta=.9; D=C; rivals not responding)")
    LG = {}; lastpd = {}
    for th0 in (0.0, 0.4):
        row = []
        for pd in (0.0, 0.5, 0.9, 0.94, 0.95, 0.97, 0.98, 0.99):
            G = largest_G(th0, pd); LG[(th0, pd)] = G
            row.append(f"p_d={pd}: {'none' if G is None else f'{G:.3f}'}")
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if largest_G(th0, mid) is not None: lo = mid
            else: hi = mid
        lastpd[th0] = lo
        print(f"   theta0={th0}: " + "; ".join(row) + f"  | none above p_d = {lo:.4f}")
    expect(abs(LG[(0.0, 0.0)] - 0.924) < 5e-4 and abs(LG[(0.0, 0.5)] - 0.852) < 5e-4 and abs(LG[(0.0, 0.9)] - 0.387) < 5e-4
           and abs(lastpd[0.0] - 0.9495) < 5e-4 and abs(lastpd[0.4] - 0.9793) < 5e-4,
           "m10(A): the largest enforceable Gamma_delta is 0.924, 0.852, 0.387 at p_d = 0, 0.5, 0.9; none above p_d = 0.9495 (theta0=0) or 0.9793 (theta0=0.4), not 0.99")
    print("(b) m10(B): with a common return Gcom_d (prize growing with capacity), theta0=0")
    LB = {}
    for Gc in (0.0, 0.3, 0.6):
        row = []
        for pd in (0.0, 0.5, 0.9):
            G = largest_G(0.0, pd, Gc); LB[(Gc, pd)] = G
            row.append(f"p_d={pd}: {'none' if G is None else ('any' if G > 0.9999 else f'{G:.3f}')}")
        print(f"   Gcom_d={Gc}: " + "; ".join(row))
    expect(abs(LB[(0.3, 0.9)] - 0.571) < 5e-4 and abs(LB[(0.6, 0.9)] - 0.755) < 5e-4 and LB[(0.3, 0.0)] > LB[(0.0, 0.0)],
           "m10(B): a common return widens the enforceable range (at p_d = 0.9: 0.387 -> 0.571 at Gcom_d = 0.3, 0.755 at 0.6)")
    print("(c) m10(C), f6(F), s3_zones: Test G: share of theta ~ U[-1,3] sustaining restraint, wider (theta>1) minus narrower (theta<1)")
    gapsC = {}
    for D in (0.0, 0.5):
        row = []; vals = []
        for pd in (0.0, 0.5, 0.8, 0.9, 0.95, 0.99, 1.0):
            thetas = [-1 + 4 * (k + 0.5) / 4000 for k in range(4000)]
            wide = [t for t in thetas if t > 1]; narrow = [t for t in thetas if t < 1]
            fw = sum(sustained(t, pd, D) for t in wide) / len(wide); fn = sum(sustained(t, pd, D) for t in narrow) / len(narrow)
            row.append(f"{pd}: {fw-fn:+.2f}"); vals.append(round(fw - fn, 2))
        gapsC[D] = vals
        print(f"   D-C={D}: gap by p_d  " + "; ".join(row))
    expect(all(a <= b_ for a, b_ in zip(gapsC[0.0], gapsC[0.0][1:])) and gapsC[0.0] == [0.05, 0.09, 0.21, 0.34, 0.5, 0.82, 0.97]
           and gapsC[0.5] == [0.05, 0.3, 0.92, 0.33, 0.0, 0.0, 0.0],
           "Test G: the gap rises with p_d at D=C (+0.05 ... +0.97); with D-C=0.5 it is humped (+0.05, +0.30, +0.92, +0.33, 0, 0, 0): the test discriminates at intermediate p_d")
    # f6(F) / s3_zones: theta_rep by direct discounted streams over 3,000 periods (not the closed form)
    def u_(i, a): return eps * b * (a[i] - sum(a[j] for j in range(n) if j != i) / (n - 1)) - c * a[i] - eps * dd * sum(a)
    def J_(i, a, th): return u_(i, a) + th * sum(u_(j, a) for j in range(n) if j != i) / (n - 1)
    def V_dev(th, pd, D, T=3000):
        g = J_(0, [1, 0, 0, 0], th); P = J_(0, [1] * n, th); v = g; disc = delta
        for t in range(1, T): v += disc * (pd * D + (1 - pd) * P); disc *= delta
        return v
    def theta_rep(pd, D):
        lo, hi = -1.0, 3.0
        if V_dev(hi, pd, D) > 0: return float("inf")
        for _ in range(60):
            m = (lo + hi) / 2
            if V_dev(m, pd, D) > 0: lo = m
            else: hi = m
        return hi
    def stage_race_dominant(th): return J_(0, [1] * n, th) >= J_(0, [0, 1, 1, 1], th)
    trs = {pd: theta_rep(pd, 0.0) for pd in (0, .5, .9, .95, .99, 1.0)}
    print("   f6(F)/s3: theta_rep(p_d) at D=C by direct discounted streams: " + ", ".join(f"p_d={pd}: {v:+.3f}" for pd, v in trs.items())
          + f"; racing credible at each: {all(stage_race_dominant(v - 1e-9) for v in trs.values())}")
    tr9 = theta_rep(0.9, 0.5); tr1 = theta_rep(1.0, 0.5)
    print(f"   D-C=0.5: theta_rep at p_d=.9 = {tr9:+.3f}; at p_d=1: {tr1} (no theta <= n-1 sustains restraint)")
    pairs = {}
    for D in (0.0, 0.5):
        for (tn, tw) in [(-0.5, 0.5), (0.0, 1.0), (0.0, 0.9)]:
            row = [str(int(tw >= theta_rep(pd, D)) - int(tn >= theta_rep(pd, D))) for pd in (0.0, 0.3, 0.6, 0.8, 0.9, 0.95, 0.99, 1.0)]
            pairs[(D, tn, tw)] = row
            print(f"   s3 Test G pairs: D={D}, theta narrow={tn}, wide={tw}: gap at p_d=0,.3,.6,.8,.9,.95,.99,1 -> {' '.join(row)}")
    expect(abs(trs[0] + 0.901) < 1e-3 and abs(trs[.95] - 0.005) < 1e-3 and abs(trs[1.0] - 0.937) < 1e-3 and abs(tr9 - 2.337) < 1e-3 and tr1 == float('inf'),
           "f6(F)/s3: theta_rep = -0.901, -0.812, -0.322, +0.005, +0.634, +0.937 at p_d = 0, .5, .9, .95, .99, 1 by direct streams; at D-C=0.5 none sustains at p_d=1")
    # ---------------------------------------------------------------- (d),(e) detect link: U05/A (A),(B) and U05/B (E)
    print("(d) [identity] detectlink (U05/A A, U05/B E): 1 - p_bar_d against Prop 8.10's (T-R)/(T-P+F) under the continuation reading")
    rnd = random.Random(11); worst = 0.0; cnt = 0
    for _ in range(100000):
        dl = rnd.uniform(0.3, 0.99); C = rnd.uniform(-2, 3); v = C - rnd.uniform(0.01, 3)
        D = v + rnd.uniform(0.01, 6); g = rnd.uniform(-1, 4)
        one_minus_pbar = ((1 - dl) * g + dl * (D - C)) / (dl * (D - v))
        R = C; T = (1 - dl) * (C + g) + dl * D; PF = (1 - dl) * (C + g) + dl * v
        worst = max(worst, abs(one_minus_pbar - (T - R) / (T - PF))); cnt += 1
    print(f"   {cnt} random settings with D > v: largest |difference| = {worst:.2e}  (R = C; T = (1-delta)(C+g)+delta D; P-F = (1-delta)(C+g)+delta v)")
    caseE = []
    for (g, C, D, v, dl) in [(2.0, 1.0, 4.0, 0.0, 0.9), (1.0, 3.0, 6.0, 1.0, 0.9), (0.5, 1.0, 0.9, 0.0, 0.9)]:
        pb = 1 - ((1 - dl) * g + dl * (D - C)) / (dl * (D - v))
        R = C; Tt = (1 - dl) * (C + g) + dl * D; PF = (1 - dl) * (C + g) + dl * v
        caseE.append((abs((1 - pb) - (Tt - R) / (Tt - PF)) < 1e-12, (Tt < R) == (pb >= 1)))
        print(f"   g={g} C={C} D={D} v={v} delta={dl}: 1-p_bar = {1-pb:.4f}; (T-R)/(T-(P-F)) = {(Tt-R)/(Tt-PF):.4f}; T<R = {Tt < R}; p_bar>=1 (R4 exception) = {pb >= 1}")
    expect(worst < 1e-9 and all(a and b_ for a, b_ in caseE),
           "detectlink: (14) with p_d = 1-upsilon reads upsilon >= 1-p_bar, numerically identical to Prop 8.10's threshold; its case T<R is p_bar >= 1. They differ in what is given: 8.10 takes F and trust, (14) a credible continuation")
    print("(e) [independent] U05/A (B): a Poisson detection clock of mean tau gives p_d = exp(-T_dec/tau); [identity] deviation values sampled in the one-period reduction against (14) (exact timings: block VF (b))")
    rr = random.Random(7); okE = True
    for Tdec, tau in ((8.0, 10.0), (20.0, 10.0), (5.0, 2.0)):
        M = 200000; hit = sum(1 for _ in range(M) if rr.expovariate(1 / tau) > Tdec); ps = hit / M; pf = math.exp(-Tdec / tau)
        okE &= abs(ps - pf) < 4 * math.sqrt(pf * (1 - pf) / M)
        print(f"   T_dec={Tdec:4.1f}, tau={tau:4.1f}: simulated p_d {ps:.4f}; exp(-T_dec/tau) {pf:.4f}")
    C, D, v, g, dl = 1.0, 1.5, 0.0, 0.3, 0.9
    for Tdec, tau in ((8.0, 10.0), (2.0, 10.0)):
        M = 200000; tot = 0.0
        for _ in range(M):
            dec = rr.expovariate(1 / tau) > Tdec
            tot += (1 - dl) * (C + g) + dl * (D if dec else v)
        Vdev = tot / M; pd = math.exp(-Tdec / tau)
        lhs = (1 - dl) * g + dl * pd * (D - C); rhs = dl * (1 - pd) * (C - v)
        okE &= (Vdev <= C) == (lhs <= rhs)
        print(f"   C=1, D=1.5, v=0, g=.3, T_dec={Tdec:4.1f}, tau=10: simulated value of deviating {Vdev:.4f} vs restraint {C:.4f} -> deterred {Vdev <= C}; (14) says {lhs <= rhs}")
    expect(okE, "detectlink (U05/A B): the Poisson clock's simulated escape probability equals exp(-T_dec/tau) within 4 SE; deviation values sampled in the one-period reduction agree with (14), an identity, not a test of the timing")
    # ---------------------------------------------------------------- (f) U05/A (C)-(E): reduced joint model, nonlinear T_dec
    N_ = 4; B_ = 1.0; C_ = 0.3; DH = 0.2; EPS = 1.0; DELTA = 0.9
    A_ = EPS * (B_ - DH) - C_; BB = EPS * (B_ / (N_ - 1) + DH); KK = C_ + N_ * EPS * DH
    def gain_obj(th): return A_ - th * BB
    def race_obj(th): return -KK * (1 + th)
    def theta_gamma(th0, Gd, n=N_):
        if Gd >= 1: return -1.0
        return (n * th0 - (n - 1) * (1 + th0) * Gd) / (n - (1 + th0) * Gd)
    def punish_value(th, qb, DC, delta=DELTA, n=N_):
        P = race_obj(th); D = DC; Vsub = P
        qe = qb * (1 - qb) ** (n - 1)
        return ((1 - delta) * P + delta * qe * (D + (n - 1) * Vsub)) / (1 - delta + n * delta * qe)
    def holds14(th, pd, qb, DC, delta=DELTA):
        v = punish_value(th, qb, DC, delta)
        return (1 - delta) * gain_obj(th) + delta * pd * DC <= delta * (1 - pd) * (0.0 - v) + 1e-12
    def pbarA(th, DC, delta=DELTA):
        v = punish_value(th, 0.0, DC, delta); D = DC
        if D - v <= 1e-12: return -math.inf
        return 1 - ((1 - delta) * gain_obj(th) + delta * (D - 0.0)) / (delta * (D - v))
    def gainsA(omega, r, dK, df, beta=0.0, delta=DELTA):
        G = (1 - beta) * r * omega * dK / (dK + df)
        Gd = (1 - beta) * r * omega * delta * dK / (1 - delta * (1 - dK - df))
        return G, Gd
    def tdec_linear(G, dK, df, gap0, gapbar):
        lam = 1 + (dK + df) * (G - 1)
        return math.log(gapbar / gap0) / math.log(lam) if lam > 1 else math.inf
    def tdec_nonlinear(omega, r, dK, df, gap0, gapbar, beta=0.0, n=N_, tmax=5000):
        kO = 1.0
        k0 = kO * (1 - omega) / (n * omega)
        Kst = (kO / n + k0) / dK
        Kv = [Kst * (1 + gap0)] + [Kst] * (n - 1)
        for t in range(1, tmax + 1):
            w = [k ** r for k in Kv]; s = sum(w); mean = sum(Kv) / n
            Kv = [(1 - dK) * Kv[i] + kO * ((1 - beta) * w[i] / s + beta / n) + k0 - df * (Kv[i] - mean) for i in range(n)]
            if Kv[0] / Kv[1] - 1 >= gapbar:
                return float(t)
        return math.inf
    _tcache = {}
    def state(omega, P):
        G, Gd = gainsA(omega, P['r'], P['dK'], P['df'])
        th = theta_gamma(P['th0'], Gd)
        key = (omega, P['r'], P['dK'], P['df'], P['gap0'], P['gapbar'])
        if key not in _tcache: _tcache[key] = tdec_nonlinear(omega, P['r'], P['dK'], P['df'], P['gap0'], P['gapbar'])
        Tn = _tcache[key]
        Tl = tdec_linear(G, P['dK'], P['df'], P['gap0'], P['gapbar'])
        pd = math.exp(-Tn / P['tau']) if Tn < math.inf else 0.0
        return G, Gd, th, Tn, Tl, pd
    def enforceable(omega, P, arm='joint', variant='i'):
        G, Gd, th, Tn, Tl, pd = state(omega, P)
        if arm == 'objective': pd = 0.0
        if arm == 'breakout': th = P['th0']
        qb = pd if variant == 'ii' else 0.0
        return holds14(th, pd, qb, P['DC'])
    def omega_star(P, arm='joint', variant='i', lo=0.01, hi=0.999):
        if not enforceable(lo, P, arm, variant): return lo
        if enforceable(hi, P, arm, variant): return None
        for _ in range(50):
            mid = (lo + hi) / 2
            if enforceable(mid, P, arm, variant): lo = mid
            else: hi = mid
        return lo
    BASE = dict(r=3.0, dK=0.2, df=0.05, th0=0.0, tau=10.0, gap0=0.05, gapbar=0.5, DC=0.0)
    fmt = lambda z: 'never' if z is None else f'{z:.3f}'
    print("(f) [num, one reduced model; rivals do not respond] U05/A (C): capacity loop with one ratio channel; nonlinear T_dec; p_d = exp(-T_dec/tau); theta_Gamma; stage game of S5.1 scaled by the stakes")
    print("    parameters: " + ', '.join(f'{k}={v}' for k, v in BASE.items()))
    summ = {}
    for DCv in (0.0, 0.5):
        P = dict(BASE, DC=DCv)
        print(f"   D-C={DCv}:  omega   Gamma  Gamma_d  theta   T_dec(nonlin)  T_dec(lin)   p_d    pbar_d(i)  enforceable (i)  (ii)")
        for om in ((0.2, 0.3, 0.4, 0.42, 0.45, 0.5, 0.55, 0.6, 0.7, 0.9) if DCv == 0 else (0.2, 0.3, 0.4, 0.42, 0.45, 0.5, 0.55, 0.6)):
            G, Gd, th, Tn, Tl, pd = state(om, P)
            pb = pbarA(th, P['DC'])
            e1 = holds14(th, pd, 0.0, P['DC']); e2 = holds14(th, pd, pd, P['DC'])
            pbs = f"{pb:+7.3f}" if pb > -50 else "  -inf "
            print(f"            {om:5.2f}  {G:6.3f}  {Gd:6.3f}  {th:+6.3f}   {Tn:10.1f}   {Tl:10.1f}   {pd:6.3f}   {pbs}     {str(e1):5}            {str(e2):5}")
        w1 = omega_star(P, 'joint', 'i'); w2 = omega_star(P, 'joint', 'ii'); wo = omega_star(P, 'objective', 'i'); wb = omega_star(P, 'breakout', 'i')
        summ[DCv] = (w1, w2, wo, wb)
        print(f"   D-C={DCv}: restraint enforceable iff omega < omega*: joint (i) {fmt(w1)}; joint (ii) one breakout technology {fmt(w2)}; objective blade alone {fmt(wo)}; breakout blade alone {fmt(wb)}")
        if w1 is not None:
            G, Gd = gainsA(w1, P['r'], P['dK'], P['df'])
            print(f"      at the joint crossing (i): Gamma = {G:.3f}, Gamma_delta = {Gd:.3f}, p_d = {state(w1, P)[5]:.3f}")
    w1 = summ[0.0][0]
    expect(w1 is not None and w1 <= summ[0.0][2] + 1e-9 and summ[0.0][1] <= w1 + 1e-9,
           f"U05/A (C): at D=C the blades close at won share {w1:.3f} (one breakout technology throughout: {summ[0.0][1]:.3f}), at or below the objective blade alone ({summ[0.0][2]:.3f})")
    print("   U05/A (D): paths (D = C): x = kappa*Omega/(n k0) = omega/(1-omega) grows at g_Omega - g_k")
    x0 = 0.25; gO = 0.05; paths = {}
    for gk, xs, label in ((0.0, x0, 'stakes outgrow fixed provision'), (0.05, x0, 'provision grows with the stakes'), (0.08, 1.5, 'provision outgrows the stakes')):
        rows = []; seq = []
        for t in (0, 10, 20, 30, 40, 60):
            x = xs * math.exp((gO - gk) * t); om = x / (1 + x)
            G, Gd, th, Tn, Tl, pd = state(om, BASE); pb = pbarA(th, BASE['DC']); seq.append((om, pd, pb))
            rows.append(f"t={t}: omega {om:.2f}, p_d {pd:.3f}, pbar {pb:+.3f}" if pb > -50 else f"t={t}: omega {om:.2f}, p_d {pd:.3f}, pbar -inf")
        paths[gk] = seq
        print(f"      {label} (g_Omega={gO}, g_k={gk}): " + "; ".join(rows))
    tstar = math.log((w1 / (1 - w1)) / x0) / gO
    print(f"      with fixed provision from omega=0.20 at g_Omega=0.05 the blades cross at t* = ln(x*/x0)/(g_Omega-g_k) = {tstar:.1f}; with g_k = g_Omega never")
    expect(all(s_ == paths[0.05][0] for s_ in paths[0.05]) and paths[0.0][-1][1] > paths[0.0][0][1] and paths[0.0][3][2] < paths[0.0][0][2],
           "U05/A (D): with provision growing with the stakes neither blade moves; with fixed provision p_d rises and p_bar falls until they cross")
    print("   U05/A (E): robustness: omega* (variant (i)) joint against each blade alone, over tau, diffusion, theta_0, r, D-C")
    nset = 0; below = 0; strict = 0; brk_alone = 0; rows = []
    for DCv in (0.0, 0.5):
        for tau in (5.0, 10.0, 20.0, 40.0):
            for df in (0.0, 0.05, 0.1):
                for th0 in (0.0, 0.4):
                    for r in (2.0, 3.0):
                        P = dict(BASE, tau=tau, df=df, th0=th0, r=r, DC=DCv)
                        w = omega_star(P, 'joint', 'i'); wo = omega_star(P, 'objective', 'i'); wb = omega_star(P, 'breakout', 'i')
                        alone = [z for z in (wo, wb) if z is not None]
                        m = min(alone) if alone else None
                        nset += 1
                        if w is not None and (m is None or w <= m + 1e-9): below += 1
                        if w is not None and m is not None and w < m - 1e-3: strict += 1
                        if wb is not None: brk_alone += 1
                        rows.append((DCv, tau, df, th0, r, w, wo, wb))
    for row in rows[::8]:
        DCv, tau, df, th0, r, w, wo, wb = row
        print(f"      D-C={DCv:.1f} tau={tau:4.1f} df={df:.2f} theta0={th0:.1f} r={r:.0f}: omega* joint {fmt(w)}, objective alone {fmt(wo)}, breakout alone {fmt(wb)}")
    print(f"      {nset} settings: the joint threshold lies at or below each blade's own in {below}; strictly below (by > 0.001) in {strict}; the breakout blade alone closes in {brk_alone}")
    expect(below == nset, f"U05/A (E): the joint threshold lies at or below each blade's own in {below}/{nset} settings, as it must by construction (p_d >= 0, theta_Gamma <= theta_0, p_bar rising in theta): a check of the implementation; the informative counts are the {strict} strictly below and the {brk_alone} in which the breakout blade alone closes")
    # ---------------------------------------------------------------- (g) U05/B: linearized T_dec, exogenous stakes and provision paths
    def theta_gammaB(theta0, Gd, n): return (n * theta0 - (n - 1) * (1 + theta0) * Gd) / (n - (1 + theta0) * Gd)
    def pbarB(theta, b, c, d, eps, n, delta):
        A = eps * (b - d) - c; B = eps * (b / (n - 1) + d); K = c + n * eps * d
        return 1 - (1 - delta) * (A - theta * B) / (delta * K * (1 + theta))
    def runB(n=4, r=1.5, beta=0.0, kappa=1.0, dK=0.5, df=0.0, delta=0.8, Omega0=1.0, k0=1.0, g_Om=0.05, g_k=0.0, eps0=0.01, Dbar=0.5,
             tau_det=12.0, theta0=0.0, b=1.0, c=0.3, d=0.2, eps=1.0, scale_stage=False, T=200, every=20, label=''):
        print(f'   --- {label}: n={n} r={r} d_K={dK} delta={delta} g_Om={g_Om} g_k={g_k} eps0={eps0} Dbar={Dbar} tau_det={tau_det} theta0={theta0} scale_stage={scale_stage}')
        print('      t   omega  Gamma  Gamma_d  Lambda*   T_dec     p_d   theta   pbar_d  gap')
        tstar = None; prev = None; seq = []
        for t in range(T + 1):
            Om = Omega0 * math.exp(g_Om * t); k = k0 * math.exp(g_k * t)
            w = (kappa * Om / n) / (kappa * Om / n + k)
            G = (1 - beta) * r * w * dK / (dK + df)
            Gd = (1 - beta) * r * w * delta * dK / (1 - delta * (1 - dK - df))
            Lam = 1 + (dK + df) * (G - 1)
            Tdec = math.log(Dbar / eps0) / math.log(Lam) if Lam > 1 else float('inf')
            pd = math.exp(-Tdec / tau_det) if Tdec < float('inf') else 0.0
            th = theta_gammaB(theta0, Gd, n) if Gd < 1 else float('nan')
            s_ = Om / Omega0 if scale_stage else 1.0
            pb = pbarB(th, b * s_, c, d * s_, eps, n, delta) if Gd < 1 else float('nan')
            gap = pb - pd; seq.append((w, pd, pb))
            if prev is not None and prev > 0 and gap <= 0 and tstar is None: tstar = t
            prev = gap
            if t % every == 0 or (tstar == t):
                print(f'   {t:4d}  {w:6.3f} {G:6.3f} {Gd:7.3f} {Lam:7.4f} {Tdec:8.2f} {pd:7.4f} {th:7.3f} {pb:8.4f} {gap:+.3f}' + ('   <- blades meet' if tstar == t else ''))
        print('      blades do not meet within the horizon' if tstar is None else f'      first t with p_d >= pbar_d: t* = {tstar}')
        return tstar, seq
    print("(g) [num, one reduced model; rivals do not respond; linearized T_dec] U05/B: the scissors along exogenous paths of stakes and provision (D=C)")
    tA, seqA = runB(label='A: stakes outgrow provision, stage fixed')
    tA2, _ = runB(label='A2: stage payoffs b,d scaling with the stakes', scale_stage=True)
    tBB, seqB = runB(label='B: provision grows with the stakes (g_k = g_Om)', g_k=0.05, T=100, every=25)
    tC, _ = runB(label='C: detection twice as fast (tau_det = 6)', tau_det=6.0, T=300, every=50)
    tD, _ = runB(label='D: a wider held self-model (theta_0 = 0.4)', theta0=0.4, T=300, every=50)
    mono = all(seqA[i][1] <= seqA[i + 1][1] + 1e-15 and seqA[i][2] >= seqA[i + 1][2] - 1e-12 for i in range(tA))
    expect(tA == 59 and tA2 == 47 and tBB is None and tC == 60 and tD == 69 and mono and seqA[0][0] == 0.2 and abs(seqA[0][2] - 0.8423) < 1e-4,
           "U05/B: the won share rises from 0.20, p_d rises and p_bar falls (from 0.842) monotonically until the blades meet at t=59 (47 if stage payoffs scale); "
           "with provision growing with the stakes they never meet; faster detection or a held self-model of 0.4 delays the meeting (60, 69)")


def check_DL():
    block('DL', 'delegatelock, nearlock (S6)', 'independent',
          'Delegation when the lock counts: q_L=1 makes not delegating strictly better; with q_L<1 and p=1 a corner is an equilibrium; with p<1 an interior profile can be the only one')
    # Sources (ported): planning/math-fable/f7_misc.py (A); planning/math-opus/m09_misc.py (check_delegation);
    # ../v6.1/reviews/counterexamples_v61_codex.py case 7. V6.1's SM(6) checked the p=1 'at least one' identity.
    # Claims (D2-fable s17, D2-opus s15): restore p=1 in the 'at least one corner' statement; with p<1 the gain from
    # delegating can fall as others delegate and an interior profile can be the only pure equilibrium.
    def surv(n, s, p, qL, psi0, psi1, me, k):
        cnt = k + me
        Q = (1 - psi1) ** cnt * (1 - psi0) ** (n - cnt)
        w = (1 + s * me) / (n + s * cnt)
        return (1 - qL * me) * Q * (w + (1 - w) * (1 - p))
    print("(a) f7(A): n=3, s=1, q_L=0, psi0=0, psi1=.015: Phi_D/Phi_N for k others delegating; pure equilibria (number of delegators)")
    n, s, qL, psi0, psi1 = 3, 1.0, 0.0, 0.0, 0.015; out = {}
    for p in (0.1, 1.0):
        ratios = [surv(n, s, p, qL, psi0, psi1, 1, k) / surv(n, s, p, qL, psi0, psi1, 0, k) for k in range(n)]
        eq = []
        for k in range(n + 1):
            ok = True
            if k > 0 and surv(n, s, p, qL, psi0, psi1, 1, k - 1) < surv(n, s, p, qL, psi0, psi1, 0, k - 1): ok = False
            if k < n and surv(n, s, p, qL, psi0, psi1, 0, k) < surv(n, s, p, qL, psi0, psi1, 1, k): ok = False
            if ok: eq.append(k)
        out[p] = (ratios, eq)
        print(f"   p={p}: ratios for k=0,1,2: {[round(x,6) for x in ratios]}; pure equilibria: {eq}")
    expect(out[0.1][1] == [2] and out[1.0][1] == [3] and out[0.1][0][0] > out[0.1][0][1] > 1 > out[0.1][0][2] and out[1.0][0][0] < out[1.0][0][1] < out[1.0][0][2],
           "f7(A): with p=0.1 the ratio falls with k (1.00259, 1.00097, 0.99928): the only pure equilibrium has two delegators; with p=1 it rises (1.48, 1.58, 1.64): all delegate")
    # Codex 7 (ported verbatim)
    n, speed, p, lock, psi0_, psi1_ = 3, 1, 0.1, 0, 0, 0.015
    def survival(delegate, other_delegators):
        count = other_delegators + int(delegate)
        Q = (1 - psi1_) ** count * (1 - psi0_) ** (n - count)
        w = (1 + speed * int(delegate)) / (n + speed * count)
        return (1 - lock * int(delegate)) * Q * (w + (1 - w) * (1 - p))
    ratios = [survival(True, k) / survival(False, k) for k in range(n)]
    ok7 = ratios[0] > 1 and ratios[1] > 1 > ratios[2]
    print(f"(b) Codex 7: ratios {ratios}; equilibrium delegators 2")
    expect(ok7, "Codex 7: with p<1 neither corner is an equilibrium; two delegators"); _codex(8, ok7)
    print("(c) m09: random draws with q_L<1: how often is neither all nor none an equilibrium, by p (20,000 each)")
    random.seed(2); neither = {1.0: 0, 0.5: 0, 0.1: 0}; T = 20000
    for p in neither:
        for _ in range(T):
            n = random.randint(2, 6); s = random.uniform(0, 20); qL = random.uniform(0, 0.99)
            psi0 = random.uniform(0, 0.05); psi1 = psi0 + random.uniform(0, 0.3)
            allD = surv(n, s, p, qL, psi0, psi1, 1, n - 1) >= surv(n, s, p, qL, psi0, psi1, 0, n - 1)
            noneD = surv(n, s, p, qL, psi0, psi1, 0, 0) >= surv(n, s, p, qL, psi0, psi1, 1, 0)
            neither[p] += (not allD and not noneD)
    print(f"   'neither all nor none is an equilibrium': {neither} of {T} each")
    expect(neither[1.0] == 0 and neither[0.5] > 0 and neither[0.1] > 0, f"m09: p=1 restores 'at least one corner' (0/20,000); p=0.5 and 0.1 do not ({neither[0.5]}, {neither[0.1]})")
    print("(d) q_L=1: not delegating strictly better for every s, n, p and profile (random draws)")
    rr = random.Random(3); viol = 0
    for _ in range(20000):
        n = rr.randint(2, 8); s = 10 ** rr.uniform(-2, 3); p = rr.random(); k = rr.randint(0, n - 1)
        psi0 = rr.uniform(0, 0.1); psi1 = psi0 + rr.uniform(0, 0.5)
        viol += not (surv(n, s, p, 1.0, psi0, psi1, 0, k) > surv(n, s, p, 1.0, psi0, psi1, 1, k))
    expect(viol == 0, "q_L=1: not delegating gives strictly higher survival in 20,000/20,000 random settings (no one delegating is the unique equilibrium)")
    # ---------------------------------------------------------------- (e) nearlock (v6.2, merge note U06 s4)
    # Source (ported): planning/drafts/U06/B/checks/dl_nearlock.py, same seed and draw order (a local Random(1) gives the
    # sequence of the source's random.seed(1)). Claim (Remark S6.1 `nearlock`): not delegating is strictly better for every
    # n, p and profile whenever (1-q_L)(1+s)(1-psi_1) < 1-psi_0; the bound is approached as n -> infinity with k=0, p=1.
    # Independent: direct survival comparison at settings drawn above the bound.
    print("(e) nearlock (Remark S6.1): q_L above 1 - 1/(a(1+s)), a = (1-psi1)/(1-psi0): is not delegating strictly better? (200,000 draws)")
    def ratioNL(n, k, s, qL, p0, p1, p):
        QN = (1-p0)**(n-k)*(1-p1)**k; wN = 1/(n+k*s)
        QD = (1-p0)**(n-k-1)*(1-p1)**(k+1); wD = (1+s)/(n+(k+1)*s)
        return (1-qL)*QD*(wD+(1-wD)*(1-p))/(QN*(wN+(1-wN)*(1-p)))
    rn = random.Random(1); violNL = 0; NNL = 200000; testedNL = 0
    for _ in range(NNL):
        n = rn.randint(2, 12); k = rn.randint(0, n-1); s = 10**rn.uniform(-2, 4)
        p0 = rn.uniform(0, 0.3); p1 = rn.uniform(p0, 0.9); p = rn.random()
        a = (1-p1)/(1-p0); qstar = 1-1/(a*(1+s))
        qL = rn.uniform(max(qstar, 0), 1)
        if qL <= qstar: continue
        testedNL += 1
        if ratioNL(n, k, s, qL, p0, p1, p) >= 1: violNL += 1
    print(f"   violations of 'not delegating strictly better' above the bound: {violNL} of {testedNL} tested ({NNL} drawn)")
    tight = []
    for n in (2, 10, 100, 10000):
        s, p0, p1 = 5, .01, .1; a = (1-p1)/(1-p0)
        tight.append(ratioNL(n, 0, s, 0.0, p0, p1, 1.0)/(a*(1+s)))
        print(f"   tightness, n={n}, k=0, p=1: ratio/bound = {tight[-1]:.4f} (= n/(n+s), -> 1 as n grows)")
    expect(violNL == 0 and testedNL == NNL and all(x < y for x, y in zip(tight, tight[1:])) and tight[-1] > 0.999
           and all(abs(t_ - n/(n+5)) < 1e-12 for t_, n in zip(tight, (2, 10, 100, 10000))),
           "nearlock: above the bound not delegating is strictly better in 200,000/200,000 draws; the bound is tight as n grows (ratio/bound 0.29, 0.67, 0.95, 0.9995 = n/(n+s))")


def check_AL():
    block('AL', 'faithful, delegate, delegatelock, nested, transmit, opaquecorr, topology, lyapunov, homeostasis, masked',
          'independent (parts marked [derived] evaluate stated formulas)',
          "The alignment reviewer's independent recomputation of Section 6 (al_checks), ported whole as one block; parts named as the reviewer named them")
    # Source (ported): ../v6.1/reviews/scripts-v6.1-alignment/al_checks.py, all sections, in order, with the reviewer's seeds.
    # The 06_S6 draft cites "al_checks, block BT", "blocks `bounded objective` and `contest`", "7.39 and 37.31",
    # "1.1628 and 0.5196": these are AL(BT), AL(bounded), AL(contest), AL(6.10), AL(6.2).
    def hdr(s_): print("   --- " + s_)
    hdr("(6.1) faithful: theta* and loss")
    def theta_star(eps, b=1.0, d=0.2, c=0.3, n=4):
        return (eps * (b - d) - c) / (eps * (b / (n - 1) + d))
    print("      eps=1:", round(theta_star(1), 4), " eps=10 (c fixed):", round(theta_star(10), 4), " eps=10, c=3:", round((10 * 0.8 - 3) / (10 * (1 / 3 + 0.2)), 4))
    for d in (0.2, 0.1, 0.05):
        print(f"      d={d}: all-racing payoff {-0.3-4*d:.3f}, theta*={theta_star(1,d=d):.3f}")
    def dJ(theta, eps=1.0, b=1.0, d=0.2, c=0.3, n=4):
        return eps * b * (1 - theta / (n - 1)) - c - eps * d * (1 + theta)
    ts = theta_star(1)
    sw = round(dJ(ts - 1e-6), 8) > 0 and round(dJ(ts + 1e-6), 8) < 0
    print("      dJ changes sign at theta*:", sw)
    expect(abs(ts - 0.9375) < 1e-9 and sw, "AL(6.1): theta* = 0.9375 at eps=1 (1.4438 at eps=10 with c fixed; 0.9375 when c scales with eps); dominance switches at theta*")
    hdr("(6.2) delegate: dominance threshold")
    def w(own, others, s):
        st = [1 + s * own] + [1 + s * o for o in others]
        return st[0] / sum(st)
    def gain_cost(s, k, n=3, psi0=0.01, psi1=0.2, Le=1.0, Lc=1.0):
        others = [1] * k + [0] * (n - 1 - k)
        g = Le * (w(1, others, s) - w(0, others, s))
        c = Lc * (psi1 - psi0) * (1 - psi0) ** (n - 1 - k) * (1 - psi1) ** k
        return g, c
    lo, hi = 0.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2
        ok = all(gain_cost(mid, k)[0] > gain_cost(mid, k)[1] for k in range(3))
        if ok: hi = mid
        else: lo = mid
    print("      s* =", round(hi, 4), " lone delegator win prob =", round(w(1, [0, 0], hi), 4))
    expect(abs(hi - 1.1628) < 1e-4 and abs(w(1, [0, 0], hi) - 0.5196) < 1e-4, "AL(6.2): delegation dominant above s* = 1.1628 (lone delegator wins with probability 0.5196)")
    hdr("(6.4) delegatelock: at-least-one identity, direct recomputation")
    random.seed(7)
    neither = both = 0; N = 100000; mism = 0
    for _ in range(N):
        n = random.randint(2, 8); s = 10 ** random.uniform(-2, 3)
        qL = random.random(); psi0 = random.uniform(0, 0.2); psi1 = random.uniform(psi0, 1.0)
        a = (1 - psi1) / (1 - psi0); A_ = (1 - qL) * a
        alleq = A_ * (n + (n - 1) * s) / n >= 1
        noneq = A_ * n * (1 + s) / (n + s) <= 1
        def Phi(own, k):
            st = [1 + s * own] + [1 + s] * k + [1.0] * (n - 1 - k)
            wv = st[0] / sum(st)
            Q = (1 - psi1) ** (k + own) * (1 - psi0) ** (n - k - own)
            return (1 - qL * own) * Q * wv
        alleq2 = Phi(1, n - 1) >= Phi(0, n - 1)
        noneq2 = Phi(0, 0) >= Phi(1, 0)
        mism += not (alleq == alleq2 and noneq == noneq2)
        if not alleq and not noneq: neither += 1
        if alleq and noneq: both += 1
    A_ = 0.01 * 0.95 / 0.99
    print("      random draws:", N, " neither:", neither, " both:", both, " formula vs direct mismatches:", mism)
    print("      n=2 all-delegate threshold s >=", round(2 / A_ - 2, 2), " survival", round(0.01 * 0.95 ** 2 * 0.5, 5))
    expect(mism == 0 and neither == 0 and both > 0, "AL(6.4): with p=1, at least one corner is an equilibrium in 100,000/100,000 draws, both in some; the closed forms equal the direct survival comparison")
    hdr("(6.7) nested: unilateral safeguard with private vs common benefit (own replicator)")
    def replicate(pay_fn, p0=0.5, T=4000, dt=0.05):
        p = p0
        for _ in range(int(T / dt)):
            pa, pb = pay_fn(p)
            p += dt * p * (1 - p) * (pa - pb)
        return p
    priv = replicate(lambda p: (-0.01 - 0.01, -0.20))
    def common(p):
        E = p * 0.01 + (1 - p) * 0.20
        return (-0.01 - E, -E)
    com = replicate(common)
    advs = {adv: replicate(lambda p, adv=adv: (-0.01 + adv, 0.0)) for adv in (0.005, 0.02)}
    print("      share of safeguard, private benefit:", round(priv, 4), "; common benefit:", round(com, 6),
          "; tax 0.01 with independent advantage 0.005:", round(advs[0.005], 4), ", 0.02:", round(advs[0.02], 4))
    expect(priv > 0.999 and com < 1e-6 and advs[0.005] < 1e-6 and advs[0.02] > 0.999,
           "AL(6.7): a safeguard with private benefit spreads; with common benefit it is selected out; a lead larger than the tax pays it while the lead lasts")
    hdr("(BT) Bradley-Terry translation invariance inside training")
    def bt(r1, r2): return 1 / (1 + math.exp(-(r1 - r2)))
    q1, q2 = 1.3, 0.4
    b0, b5 = bt(q1, q2), bt(q1 - 5, q2 - 5); ab = bt(1.3 - 5, 0.0)
    print(f"      shared harm 0: P(y1>y2)={b0:.6f}; shared harm -5: {b5:.6f}; comply(q=1.3,h=-5) vs abstain(q=0,h=0): P(comply preferred)={ab:.4f}")
    expect(abs(b0 - b5) < 1e-12 and abs(b0 - 0.7110) < 1e-4 and abs(ab - 0.0241) < 1e-4,
           "AL(BT): a harm shared by both compared responses leaves the preference at 0.7110; with abstention in the comparison set the complying response is preferred with probability 0.024")
    hdr("(6.8) opaquecorr numbers")
    s0 = 0.9 ** 200
    s1 = 1.0
    for t in range(1, 201): s1 *= (1 - 0.1 * 0.01 - 2 ** -(t + 2))
    s1b = 1.0
    for t in range(0, 200): s1b *= (1 - 0.1 * 0.01 - 2 ** -(t + 2))
    sl = 1.0
    for t in range(1, 20001): sl *= (1 - 0.001 - 2 ** -(t + 2))
    print(f"      no corrector: {s0:.2e}; corrector (t=1..200): {s1:.3f}; (t=0..199): {s1b:.3f}; corrector to period 20000: {sl:.2e} (constant c_b: not summable)")
    expect(abs(s1 - 0.630) < 5e-4 and abs(s1b - 0.473) < 5e-4 and sl < 1e-8, "AL(6.8): 0.630 counts from t=1, 0.473 from t=0; with c_b fixed the residual is not summable (1.6e-9 by 20,000)")
    hdr("(6.9) topology: random vs adversarial blind spot")
    f, k = 0.9, 6
    print("      serial", round(f ** k, 3), " k checks across gap", round(1 - (1 - f ** k) ** k, 3), " with qcc=.05", round(0.95 * (1 - (1 - f ** k) ** k), 3),
          " m=2", round((1 - 0.1 ** 2) ** k, 3), " m=3", round((1 - 0.1 ** 3) ** k, 3))
    for rho in (0.0, 0.05, 0.3):
        print(f"      blind spot {rho}: random-hazard catch {(1-rho)*(1-0.1**6):.3f}")
    for know in (0.0, 0.5, 0.9, 1.0):
        rho = 0.05; catch = know * 0.0 + (1 - know) * ((1 - rho) * (1 - 0.1 ** 6))
        print(f"      attacker knows the common blind spot w.p. {know}: catch {catch:.3f}")
    print("      [derived: evaluates the stated formulas]")
    hdr("(6.10) logistic map horizon (lyapunov)")
    random.seed(3)
    def steps(e0, tol=0.1, trials=2000):
        tot = 0
        for _ in range(trials):
            x = random.random(); y = x + e0
            n_ = 0
            while abs(x - y) < tol and n_ < 500:
                x = 4 * x * (1 - x); y = 4 * y * (1 - y); n_ += 1
            tot += n_
        return tot / trials
    st3, st12 = steps(1e-3), steps(1e-12)
    print(f"      mean steps e=1e-3: {st3:.2f}  e=1e-12: {st12:.2f} (ln-precision theory: (ln(0.1/e))/ln 2 = {math.log(100)/math.log(2):.1f}, {math.log(1e11)/math.log(2):.1f})")
    expect(abs(st3 - 7.39) < 0.01 and abs(st12 - 37.31) < 0.01, "AL(6.10): errors of 1e-3 and 1e-12 reach 0.1 after 7.39 and 37.31 steps on average (seeded as the reviewer did)")
    hdr("(6.11) homeostasis")
    def interior_x(n, s, Le, Lc, psi0, Dpsi):
        q = 1 - psi0; K = (n - 1) * Le / (n * n * Lc); bs = Dpsi / s
        f_ = lambda x: (x + bs) * (q - x) ** (n - 1) - K
        lo, hi = 0.0, min(Dpsi, q / n)
        if f_(lo) > 0: return 0.0
        if f_(hi) < 0: return Dpsi
        for _ in range(200):
            m = (lo + hi) / 2
            if f_(m) < 0: lo = m
            else: hi = m
        return lo
    for D in (0.19, 0.05, 0.02, 0.01, 0.005):
        x = interior_x(3, 100, 1, 100, 0.01, D)
        print(f"      Dpsi={D}: iota={x/D:.3f}, added hazard n*x={3*x:.4f}")
    x = interior_x(3, 100, 1, 100, 0.01, 0.001); print("      Dpsi=0.001: added hazard", 3 * x)
    mgs = []
    for t in range(2, 8):      # the example shifted by one period (FIXES-v6.2-verify, M2-03): s_t=2^(t+1), dpsi_t=2^-(t+1)
        s = 2 ** (t + 1); D = 2 ** -(t + 1)
        mg = 2 * s / (9 * (1 + s)) - D * (1 - D) ** 2; mgs.append(mg)
        print(f"      t={t}: own marginal gain at full delegation {mg:+.4f}")
    tail = sum(3 * 2 ** -(t + 1) for t in range(4, 200))
    print("      sum_{t>=4} 3*2^-(t+1) =", tail)
    expect(all(m > 0 for m in mgs) and abs(tail - 3 / 16) < 1e-12, "AL(6.11): full delegation's own marginal gain is positive at t = 2..7 (shifted example); realized risk from t=4 summed by the union bound is 3/16")
    hdr("(bounded objective) bounded maximizer vs satisficer as the cost of resources falls")
    Rs = []
    for c in (0.1, 0.01, 0.001, 1e-6):
        Rmax = math.log(1 / c); Rsat = math.log(1 / 0.05); Rs.append(Rmax)
        print(f"      cost {c:g}: bounded maximizer acquires R={Rmax:.2f}; satisficer R={Rsat:.2f}")
    expect(all(a < b_ for a, b_ in zip(Rs, Rs[1:])) and abs(Rs[-1] - 13.82) < 0.01, "AL(bounded): a maximizer of a bounded goal acquires ln(1/c): 2.30, 4.61, 6.91, 13.8 without limit; a satisficer stops at 3.0")
    hdr("(contest) intensity as the private cost c -> 0, by self-model (Prop 3.6(1) formula)")
    def e(theta, c, n=4, r=1.0, Om=1.0, l=0.3):
        return r * Om * (n - 1 - theta) / (n * n * (c + (1 + theta) * l))
    for th in (-1.0, -0.5, 0.0):
        print(f"      theta={th}:", [round(e(th, c), 3) if c + (1 + th) * 0.3 > 0 else 'inf' for c in (1.0, 0.1, 0.01, 0.001)])
    expect(abs(e(-1.0, 0.001) - 250) < 1e-6 and e(0.0, 0.001) < 1, "AL(contest): under the relative objective intensity rises 0.25 -> 250 as c falls 1 -> 0.001; counting the shared loss keeps it bounded (0.62)")


def check_TR():
    block('TR', 'signal, pausevalue, readiness, readrule (S11); the staying-out identity (X11)',
          'independent: (a)-(c) brute-force search over strategy profiles; (d)-(f) direct computation; (g) simulation; (h) identity',
          'The transition: the signal game (separation, the bound on restraint after a reversible step, the intuitive criterion); '
          'a pause valued by what changes; readiness under conjunction and noise against sequential tests; staying out alone')
    # Source (ported verbatim, as one function): planning/drafts/U11/A/checks/tr_transition.py (12 assertions; merge note
    # U11 s4 item 2), with its seed and draw order, so the numbers reproduce its log (planning/drafts/U11/A/checks/
    # tr_transition.log). Only the script's own expect() and final count are replaced by this file's. Cited as [num: TR]
    # by Proposition 11.1 `signal`, Proposition S11.2 `pausevalue`, Remark S11.3 `readrule` and X11's staying-out identity.
    rnd = random.Random(20261004)

    # ---------------------------------------------------------------------------------------------------------------
    # (A) signal: a sender of type S (prob 1-mu) or R (prob mu) sends E at cost k_t or not (N); the receiver restrains
    # with probability rho_m after message m; restraint is worth G_t to type t; the receiver restrains iff its posterior
    # that the sender is S is at least w (= varpi*), and is indifferent at equality.
    # Brute force: candidate (rho_E, rho_N) pairs on a grid plus the indifference lines rho_E - rho_N = k_t/G_t; for each,
    # the senders' best-response sets; then whether some sigma in those sets makes the receiver's rho a best response
    # (posterior > w -> rho=1; < w -> rho=0; = w -> any; message off path -> any rho is supportable).
    # ---------------------------------------------------------------------------------------------------------------
    def br_set(rE, rN, k, G, tol=1e-9):
        d = (rE * G - k) - rN * G
        if d > tol: return (1.0, 1.0)
        if d < -tol: return (0.0, 0.0)
        return (0.0, 1.0)

    def receiver_ok(rho, post, w, tol=1e-9):
        if post is None: return True                      # off path: any belief, so any rho
        if post > w + tol: return abs(rho - 1) < 1e-12
        if post < w - tol: return abs(rho) < 1e-12
        return True

    def equilibria(mu, w, kS, kR, GS, GR, grid=101):
        cands = set()
        base = [i / (grid - 1) for i in range(grid)]
        for rN in base:
            cands.add((rN, rN))
            for dlt in (kS / GS, kR / GR):
                if 0 <= rN + dlt <= 1: cands.add((rN + dlt, rN))
        for rE in base:
            cands.add((rE, 0.0)); cands.add((rE, 1.0))
        out = []
        sig_grid = [i / 400 for i in range(401)]
        for rE, rN in cands:
            sS = br_set(rE, rN, kS, GS); sR = br_set(rE, rN, kR, GR)
            SS = [s for s in sig_grid if sS[0] <= s <= sS[1]]
            SR = [s for s in sig_grid if sR[0] <= s <= sR[1]]
            # exact posterior-equalizing sigma_R for the hybrid, if R is indifferent
            if sR == (0.0, 1.0) and (1 - mu) < w:
                SR.append((1 - mu) * (1 - w) / (mu * w))
            for a in SS:
                for b in SR:
                    if not (0 <= b <= 1): continue
                    pE = (1 - mu) * a + mu * b; pN = (1 - mu) * (1 - a) + mu * (1 - b)
                    postE = None if pE < 1e-12 else (1 - mu) * a / pE
                    postN = None if pN < 1e-12 else (1 - mu) * (1 - a) / pN
                    if receiver_ok(rE, postE, w) and receiver_ok(rN, postN, w):
                        out.append((a, b, rE, rN, pE > 1e-12))
                        break
                else:
                    continue
                break
        return out

    print("(a) signal(1): a separating equilibrium (S sends, R does not, restraint after E only) exists iff kS <= GS and kR >= GR")
    bad = 0; n = 0
    for _ in range(300):
        mu = rnd.uniform(0.05, 0.95); w = rnd.uniform(0.05, 0.95)
        GS = rnd.uniform(0.1, 1); GR = rnd.uniform(0.1, 1); kS = rnd.uniform(-0.3, 1.2); kR = rnd.uniform(-0.1, 1.2)
        eqs = equilibria(mu, w, kS, kR, GS, GR, grid=11)
        sep = any(abs(a - 1) < 1e-9 and abs(b) < 1e-9 and abs(rE - 1) < 1e-9 and abs(rN) < 1e-9 for a, b, rE, rN, _ in eqs)
        pred = (kS <= GS) and (kR >= GR)
        n += 1; bad += (sep != pred)
    expect(bad == 0, f"signal(1): brute-force search agrees with the condition in {n - bad}/{n} random games")

    print("(b) signal(2): if 0 <= kR < GR and 1-mu < w, restraint after E has probability at most kR/GR in every equilibrium")
    worst = -1; n = 0; found_hybrid = 0; nh = 0
    for _ in range(200):
        mu = rnd.uniform(0.2, 0.95); w = rnd.uniform(1 - mu + 0.02, 0.99) if 1 - mu + 0.02 < 0.99 else 0.99
        GS = rnd.uniform(0.1, 1); GR = rnd.uniform(0.1, 1); kR = rnd.uniform(0, GR * 0.98); kS = rnd.uniform(-0.3, GS)
        eqs = equilibria(mu, w, kS, kR, GS, GR, grid=21)
        for a, b, rE, rN, onE in eqs:
            if onE: worst = max(worst, rE - kR / GR)
        n += 1
        if kS <= GS * kR / GR:
            nh += 1
            sR = (1 - mu) * (1 - w) / (mu * w)
            found_hybrid += any(abs(a - 1) < 1e-9 and abs(b - sR) < 1e-6 and abs(rE - kR / GR) < 1e-9 and abs(rN) < 1e-12 for a, b, rE, rN, _ in eqs)
    expect(worst <= 1e-9, f"signal(2): over {n} random games, max over equilibria of (restraint after E) - kR/GR = {worst:.2e} <= 0")
    expect(found_hybrid == nh, f"signal(2): the hybrid equilibrium (S sends; R sends with prob (1-mu)(1-w)/(mu w); restraint after E w.p. kR/GR) is found in {found_hybrid}/{nh} games with kS <= GS kR/GR")

    print("(c) signal: the printed example")
    kS, kR, GS, GR = -0.05, 0.30, 0.40, 0.20
    eqs = equilibria(0.5, 0.6, kS, kR, GS, GR, grid=21)
    sep = any(abs(a - 1) < 1e-9 and abs(b) < 1e-9 and abs(rE - 1) < 1e-9 and abs(rN) < 1e-9 for a, b, rE, rN, _ in eqs)
    expect(sep, "kS=-0.05, kR=0.30, GS=0.40, GR=0.20 (mu=0.5, w=0.6): the separating equilibrium exists")
    kR2 = 0.05
    eqs2 = equilibria(0.5, 0.6, kS, kR2, GS, GR, grid=21)
    sep2 = any(abs(a - 1) < 1e-9 and abs(b) < 1e-9 and abs(rE - 1) < 1e-9 and abs(rN) < 1e-9 for a, b, rE, rN, _ in eqs2)
    mx = max([rE for a, b, rE, rN, onE in eqs2 if onE] or [0])
    sR = (1 - 0.5) * (1 - 0.6) / (0.5 * 0.6)
    print(f"   reversible step kR=0.05: separating exists: {sep2}; max restraint after E over equilibria {mx:.3f} = kR/GR = {kR2/GR:.3f}; hybrid: R imitates w.p. {sR:.3f}")
    expect((not sep2) and abs(mx - 0.25) < 1e-9, "kR=0.05: no separation; the step buys restraint with probability 0.25 at most")
    # intuitive criterion: pooling on N when 1-mu < w, kR > GR, 0 < kS < GS
    mu, w = 0.5, 0.6
    eqp = equilibria(mu, w, 0.1, 0.3, 0.4, 0.2, grid=21)
    pool = [e for e in eqp if abs(e[0]) < 1e-9 and abs(e[1]) < 1e-9]
    print(f"   pooling on N exists with skeptical off-path beliefs (restraint after E <= kS/GS): {bool(pool)}; "
          f"E is equilibrium-dominated for R (best {0.2-0.3:+.2f} < 0) and not for S (best {0.4-0.1:+.2f} > 0)")
    expect(bool(pool) and (0.2 - 0.3) < 0 < (0.4 - 0.1), "intuitive criterion: beliefs after E must put weight on S, which removes the pooling equilibrium")

    # ---------------------------------------------------------------------------------------------------------------
    # (d) pausevalue
    # ---------------------------------------------------------------------------------------------------------------
    print("(d) pausevalue(1): a pause that changes nothing leaves survival over any number of active rounds unchanged")
    okd = True
    for _ in range(200):
        N = rnd.randint(5, 200); P = rnd.randint(1, 50)
        h = [rnd.uniform(0, 0.05) for _ in range(N)]
        no_pause = math.prod(1 - x for x in h)
        with_pause = math.prod(1 - x for x in ([0.0] * P + h))       # the pause adds no hazard of its own
        okd &= abs(no_pause - with_pause) < 1e-12
    expect(okd, "shift invariance in 200 random sequences")
    print("(e) pausevalue(2): hazard 0.01 a round for 20 rounds, then 0.01/k^1.5 in the k-th round after a change")
    s = 0.99 ** 20 * math.prod(1 - 0.01 / k ** 1.5 for k in range(1, 10001 - 20))
    s_un = 0.99 ** 10000
    lim = 0.99 ** 20 * math.exp(sum(math.log(1 - 0.01 / k ** 1.5) for k in range(1, 2_000_001)))
    print(f"   survival to round 10,000: {s:.4f} (limit {lim:.4f}); unchanged process at 0.01 a round: {s_un:.2e}")
    expect(abs(s - 0.80) < 0.005 and s_un < 1e-40, "survival to 10,000 rounds is 0.80 after a change to a summable sequence, 2e-44 without one")

    # ---------------------------------------------------------------------------------------------------------------
    # (f), (g) readiness: fixed readings under conjunction and noise, against sequential tests (Wald 1945)
    # ---------------------------------------------------------------------------------------------------------------
    print("(f) readiness: seven dimensions, each read once with a 5% chance of missing a met dimension")
    p7 = 0.95 ** 7
    print(f"   a ready state passes all seven with probability 0.95^7 = {p7:.4f}")
    expect(abs(p7 - 0.70) < 0.005, "0.95^7 = 0.70")
    # fixed-sample design at sigma=1: alpha=0.01 (false 'met' at mean 0), beta=0.05 (missed 'met' at mean 1)
    z = lambda p: statistics.NormalDist().inv_cdf(p)
    nfix = math.ceil((z(0.99) + z(0.95)) ** 2)
    def fixed_power(sigma):
        c = z(0.99) * sigma / math.sqrt(nfix)
        return 1 - statistics.NormalDist(1, sigma / math.sqrt(nfix)).cdf(c)
    for sg in (1, 2):
        pw = fixed_power(sg)
        print(f"   fixed design (n={nfix} readings, set for noise 1): at noise {sg}, a met dimension passes w.p. {pw:.3f}; seven pass w.p. {pw**7:.4f}")
    expect(fixed_power(2) ** 7 < 0.01, "a fixed reading designed for one noise level, read at twice the noise, almost never passes a ready state")
    print("(g) sequential test per dimension (SPRT, means 0 vs 1, alpha=0.01, beta=0.05/7): error rates and duration by noise")
    alpha, beta = 0.01, 0.05 / 7
    A = math.log((1 - beta) / alpha); B = math.log(beta / (1 - alpha))
    def sprt(mean, sigma):
        llr = 0.0; t = 0
        while B < llr < A:
            x = rnd.gauss(mean, sigma); t += 1
            llr += (x - 0.5) / sigma ** 2            # log LR of N(1,s^2) vs N(0,s^2) for one reading
        return llr >= A, t
    res = {}
    for sg in (1, 2, 4):
        runs = 4000
        fa = [sprt(0.0, sg) for _ in range(runs)]; mi = [sprt(1.0, sg) for _ in range(runs)]
        a_hat = sum(d for d, _ in fa) / runs; b_hat = sum(1 - d for d, _ in mi) / runs
        tn = statistics.mean(t for _, t in mi)
        res[sg] = (a_hat, b_hat, tn)
        print(f"   noise {sg}: false 'met' {a_hat:.4f} (bound {alpha/(1-beta):.4f}); missed 'met' {b_hat:.4f} (bound {beta/(1-alpha):.4f}); mean readings when met {tn:.1f}")
    print(f"   seven dimensions: a ready state is held back with probability at most 7*beta/(1-alpha) = {7*beta/(1-alpha):.4f}")
    expect(all(res[s][0] < 0.02 and res[s][1] < 0.015 for s in res) and res[4][2] > 8 * res[1][2],
           "noise lengthens the sequential test (mean readings x16 at four times the noise, within sampling) and leaves its error rates at the registered levels")

    # ---------------------------------------------------------------------------------------------------------------
    # (h) X11: staying out alone, in the survival accounting of survassure (n=2; q_I = p_dec = 1-eps; p_ext = 1)
    # ---------------------------------------------------------------------------------------------------------------
    print("(h) X11 identity: joining Phi^P = (1-q_I)(1-p_dec/2) = eps(1+eps)/2; staying out Phi^S = 1 - p^S_dec p_ext")
    okh = True
    for eps in (0.05, 0.1, 0.3, 0.6):
        PhiP = eps * (1 - (1 - eps) / 2); stay_same = 1 - (1 - eps); stay_worse = 1 - (1 - eps ** 2)
        okh &= abs(PhiP - eps * (1 + eps) / 2) < 1e-12 and stay_same > PhiP > stay_worse
        print(f"   eps={eps}: joining {PhiP:.4f}; staying out, rival's decisive chance unchanged {stay_same:.4f}; raised to 1-eps^2 {stay_worse:.4f}")
    expect(okh, "staying out beats joining when it leaves the rival's decisive chance unchanged, and loses when it raises it to 1-eps^2")


def check_ML():
    block('ML', 'metaloop (TESTS research programme; not cited in the core)', 'derived (toy)',
          "The meta-loop toy (Sys s6): rule-making by actors with working objective theta_Gamma sets the next period's Gamma_delta")
    # Source (ported): ../v6.1/reviews/scripts-v6.1-systems/s6_metaloop.py. Plan s9 declines the toy for the paper and moves
    # it to the TESTS research programme as a suggestion; it is kept here so the reviewer's script has a findable home.
    n, th0 = 4, 0.5
    def thG(G): return (n * th0 - (n - 1) * (1 + th0) * G) / (n - (1 + th0) * G)
    def S(v): return 1 / (1 + math.exp(-v))
    def F(G, k, thc, Gmin=0.1, Gmax=0.98): return Gmin + (Gmax - Gmin) * S(k * (thc - thG(G)))
    nfp = {}
    for k in (2.0, 6.0, 12.0):
        for thc in (-0.2, 0.0, 0.2):
            fps = []; prev = None
            N = 20000
            for i in range(N + 1):
                G = 0.0 + 0.999 * i / N
                h = F(G, k, thc) - G
                if prev is not None and (h == 0 or (h > 0) != (prev[1] > 0)):
                    slope = (F(G + 1e-6, k, thc) - F(G - 1e-6, k, thc)) / 2e-6
                    fps.append((round(G, 3), 'stable' if abs(slope) < 1 else 'unstable', round(thG(G), 2)))
                prev = (G, h)
            nfp[(k, thc)] = len(fps)
            print(f"   k={k}, theta_c={thc}: fixed points (Gamma, stability, theta_Gamma): {fps}")
    expect(nfp[(2.0, 0.0)] == 1 and nfp[(12.0, 0.0)] == 3, "ML (toy): a steep rule-making response makes the loop bistable (a narrow-objective high-Gamma state and a wide-objective low-Gamma one)")


# =====================================================================================================================
# v6.2 extensions of v6.1 blocks. The v6.1 function bodies are left byte-identical; _with_ext() runs the v6.1 block and
# then its extension under the same block code, with a sub-header naming the extension's keys and kind.
# =====================================================================================================================
def subblock(name, keys, kind, title):
    print(f"\n--- {name} (v6.2 extension) [{kind}] keys: {keys}\n    {title}", flush=True)


def _replicator(p, pi, dt=0.01, T=4000.0):
    for _ in range(int(T / dt)):
        f = pi(p); pb = sum(a * b for a, b in zip(p, f))
        p = [a + dt * a * (b - pb) for a, b in zip(p, f)]; s = sum(p); p = [a / s for a in p]
    return p


def ext_CI():
    subblock('CI', 'blind, nested, require (R8); unravel (S9)', 'independent',
             'Lemma 3.3(3) with a sanction that falls as evaders spread; unequal compliance costs; the matched unsafe variant; a tax paid from a lead; the participation threshold across types')
    # Sources (ported): planning/math-fable/f4_selection.py (A),(C); planning/math-opus/m05_selection.py (A),(B),(D);
    # ../v6.1/reviews/scripts-v6.1-math-fable/m6_misc.py (1); ../v6.1/reviews/counterexamples_v61_codex.py case 5.
    print("(f) f4(A): compliers pay c=0.3; evaders face s(x) falling in the evading share x")
    cases = [("s(x)=0.48(1-x): s(0)=0.48>c>s(1)=0", lambda x: 0.48 * (1 - x)), ("s(x)=0.24(1-x): s(0)=0.24<c", lambda x: 0.24 * (1 - x)),
             ("s(x)=0.5+0.5(1-x): s(1)=0.5>c", lambda x: 0.5 + 0.5 * (1 - x)), ("s(x)=0.6-0.4x: s(0)=0.6>c>s(1)=0.2", lambda x: 0.6 - 0.4 * x)]
    finals = {}
    for name, s in cases:
        outs = []
        for x0 in (0.05, 0.5, 0.95):
            p = _replicator([1 - x0, x0], lambda p: [-0.3, -s(p[1])]); outs.append(p[1])
        tip = None
        if s(0) > 0.3 > s(1):
            lo, hi = 0.0, 1.0
            for _ in range(60):
                m = (lo + hi) / 2
                if s(m) > 0.3: lo = m
                else: hi = m
            tip = hi
        finals[name] = (outs, tip)
        print(f"   {name}: " + "; ".join(f"x0={x0}->{o:.3f}" for x0, o in zip((0.05, 0.5, 0.95), outs)) + (f"  -> bistable, tipping share {tip:.3f}" if tip is not None else "  -> one global attractor"))
    v = list(finals.values())
    expect([round(x) for x in v[0][0]] == [0, 1, 1] and abs(v[0][1] - 0.375) < 1e-6 and [round(x) for x in v[1][0]] == [1, 1, 1]
           and [round(x) for x in v[2][0]] == [0, 0, 0] and [round(x) for x in v[3][0]] == [0, 0, 1] and abs(v[3][1] - 0.75) < 1e-6,
           "f4(A): s(0) > c > s(1): bistable, tipping at s(x)=c (0.375, 0.750); s(0) < c: evasion global; s(1) > c: compliance global")
    print("(g) m05(A) and m6(1): the same three regimes by a different integrator (x' = x(1-x)(c - s(x)))")
    c = 0.3; okA = True
    for name, s, expect_tip in (('s = .5 + .5(1-x)', lambda x: 0.5 + 0.5 * (1 - x), None), ('s = .24(1-x)', lambda x: 0.24 * (1 - x), None),
                                ('s = .48(1-x)', lambda x: 0.48 * (1 - x), 0.375), ('s = 1.2(1-x)', lambda x: 1.2 * (1 - x), 0.75)):
        out = []
        for x0 in (0.02, 0.3, 0.5, 0.7, 0.98):
            x = x0
            for _ in range(20000): x += 0.01 * x * (1 - x) * (c - s(x))
            out.append(x)
            if expect_tip is not None: okA &= (x > 0.5) == (x0 > expect_tip)
        print(f"   {name}: " + ", ".join(f"{x0}->{x:.3f}" for x0, x in zip((0.02, 0.3, 0.5, 0.7, 0.98), out)))
    for q0, F in [(0.8, 0.6), (2.0, 0.6), (0.4, 0.6)]:
        outs = [_replicator([1 - x0, x0], lambda p: [-0.3, -q0 * p[0] * F], T=3000.0)[1] for x0 in (0.05, 0.5, 0.95)]
        print(f"   m6(1): s(x) = q0 (1-x) F with s(0) = {q0*F:.2f}: " + "; ".join(f"x0={x0}: {o:.3f}" for x0, o in zip((0.05, 0.5, 0.95), outs)))
    expect(okA, "m05(A): the tipping share is where s(x) = c; on either side the population goes to compliance or evasion")
    print("(h) m05(B): two developer types, unequal compliance costs; replicator on (A comply, A evade, B comply, B evade)")
    resB = []
    for (cA, cB, sA, sB) in ((0.1, 0.2, 1.0, 1.0), (0.1, 0.2, 0.15, 0.25), (0.1, 0.2, 1.0, 0.15), (0.1, 0.2, 1.0, 0.05)):
        pay = [1 - cA, 1 - sA, 1 - cB, 1 - sB]
        x = [0.25] * 4
        for _ in range(40000):
            m = sum(p * xi for p, xi in zip(pay, x))
            x = [xi + 0.01 * xi * (p - m) for xi, p in zip(x, pay)]
            S = sum(x); x = [xi / S for xi in x]
        comp = x[0] + x[2]; resB.append(comp)
        print(f"   costs ({cA},{cB}) sanctions ({sA},{sB}): compliant share {comp:.6f}; among compliers A:B = {x[0]:.4f}:{x[2]:.4f}")
    expect(resB[0] > 0.999999 and resB[1] > 0.999999 and resB[2] > 0.999999 and resB[3] < 1e-6,
           "m05(B): every s_k > c_k -> compliance; s_B < c_B can still lose to A's compliers (0.15 < 0.2: evasion vanishes) or win (0.05: evasion takes over): "
           "'s_k >= c_k for every type' is sufficient, not necessary (finding: D2-fable's 'iff' holds within a type)")
    print("(i) f4(C) and Codex 5: unequal incidence among compliers; the matched variant; zero tax")
    pay = [0.9, 0.0, 0.8, 0.0]
    p = _replicator([0.25] * 4, lambda p: pay, T=20.0)
    p2 = _replicator([0.3, 0.2, 0.3, 0.2], lambda p: [0.9, 0.0, 0.9, 0.0], T=20.0)
    p3 = _replicator([0.5, 0.5], lambda p: [2.0 - 0.1, 1.0], T=20.0)
    p4 = _replicator([0.5, 0.5], lambda p: [2.0 - 0.1, 2.0], T=200.0)
    p5 = _replicator([0.3, 0.7], lambda p: [1.0, 1.0], T=50.0)
    print(f"   unequal compliance costs (.1 vs .2), sanction 1: shares at t=20 {['%.6f'%x for x in p]}; compliant share {p[0]+p[2]:.9f}")
    print(f"   equal incidence: compliers' relative shares {p2[0]/p2[2]:.6f} (started 1.0); unmatched (baseline 2, tax .1 vs baseline 1): safeguarded {p3[0]:.6f};"
          f" matched (2-.1 vs 2): safeguarded {p4[0]:.3e} at t=200; zero tax: ({p5[0]:.3f}, {p5[1]:.3f})")
    payoffs = [0.9, 0.0, 0.8, 0.0]
    weights = [math.exp(20 * x) for x in payoffs]; shares = [x / sum(weights) for x in weights]
    ok5 = shares[0] + shares[2] > 0.9999999
    print(f"   Codex 5 (closed-form replicator at t=20): shares {[f'{x:.3e}' for x in shares]}; compliant share {shares[0]+shares[2]:.9f}")
    expect(p[0] + p[2] > 0.9999999 and abs(p2[0] / p2[2] - 1) < 1e-9 and p3[0] > 0.999 and p4[0] < 1e-8 and abs(p5[0] - 0.3) < 1e-9 and ok5,
           "f4(C)/Codex 5: unequal costs re-sort compliers without letting evasion back in; equal incidence preserves shares; a matched unsafe variant eliminates the safeguarded one, an unmatched one does not")
    _codex(6, ok5)
    print("(j) m05(D): the alignment tax under selection: matched twin; a lead that pays the tax")
    def run(pay, T=2000.0, dt=0.01):
        x = [1 / len(pay)] * len(pay)
        for _ in range(int(T / dt)):
            m = sum(p * xi for p, xi in zip(pay, x))
            x = [xi * math.exp(dt * (p - m)) for xi, p in zip(x, pay)]; S = sum(x); x = [xi / S for xi in x]
        return x
    a = run([2.0 - 0.1, 1.0]); b = run([2.0 - 0.1, 1.0, 2.0]); c2 = run([1.0 + 0.02 - 0.01, 1.0], T=3000.0); c3 = run([1.0 + 0.005 - 0.01, 1.0], T=3000.0)
    print(f"   safeguarded (2, tax .1) vs unsafe (1): {a[0]:.4f}; with its matched twin: safeguarded {b[0]:.2e}, twin {b[2]:.4f}; tax .01 from a lead .02: {c2[0]:.4f}; from .005: {c3[0]:.4f}")
    expect(a[0] > 0.999 and b[0] < 1e-50 and c2[0] > 0.999 and c3[0] < 1e-6, "m05(D): a tax alone does not eliminate a safeguarded developer with a larger advantage; its matched twin does; a lead pays the tax while it lasts")
    # ---------------------------------------------------------------- (k) v6.2 addition (merge note U09 s4 item 9)
    # Remark S9.1 `unravel` across types: x = sum_k m_k x_k is the outside share weighted by type mass; each type moves as
    # x_k' = x_k(1-x_k)(c_k - s_k(x)) (integrated in logit coordinates, u_k' = c_k - s_k(x)); the tipping shares are not
    # used by the dynamics. Independent. Claims: below min_k x_k^dagger every state returns to full participation; just
    # above it the type with the smallest tipping share leaves, and the others follow only if that carries x past theirs;
    # a type with s_k(0) <= c_k leaves from every state, so full participation is impossible.
    print("(k) unravel (Remark S9.1) across types: type 1 c=0.3, s=0.48(1-x) (tips at 0.375); type 2 c=0.3, s=0.6-0.4x (tips at 0.75)")
    def unr(types, x0, dt=0.1, T=50000.0):
        u = [math.log(v / (1 - v)) for v in x0]; t = 0.0
        while t < T:
            xs = [1 / (1 + math.exp(-v)) if v > -700 else 0.0 for v in u]
            x = sum(m * xk for (m, c_, s_), xk in zip(types, xs))
            if all(v < -14 or v > 14 for v in u): break
            u = [v + dt * (c_ - s_(x)) for v, (m, c_, s_) in zip(u, types)]; t += dt
        xs = [1 / (1 + math.exp(-v)) if v > -700 else 0.0 for v in u]
        return xs, sum(m * xk for (m, c_, s_), xk in zip(types, xs))
    s1 = lambda x: 0.48 * (1 - x); s2 = lambda x: 0.6 - 0.4 * x; s3 = lambda x: 0.24 * (1 - x)
    okU = True
    for m1 in (0.5, 0.8):
        types = [(m1, 0.3, s1), (1 - m1, 0.3, s2)]
        ru = random.Random(7); back = 0; Nu = 400
        for _ in range(Nu):
            while True:
                a1, a2 = ru.uniform(1e-4, 1 - 1e-4), ru.uniform(1e-4, 1 - 1e-4)
                if m1 * a1 + (1 - m1) * a2 < 0.375: break
            back += unr(types, [a1, a2])[1] < 1e-5
        x1 = 0.38 / m1; xs, xf = unr(types, [x1, 1e-4])
        print(f"   masses ({m1}, {1-m1:.1f}): {back}/{Nu} random states with outside share below 0.375 return to full participation; "
              f"from x = 0.38 held by type 1: type shares outside ({xs[0]:.4f}, {xs[1]:.4f}), outside share {xf:.4f}")
        okU &= back == Nu
        okU &= (xs[0] > 1 - 1e-5 and xs[1] < 1e-5 and abs(xf - 0.5) < 1e-5) if m1 == 0.5 else (xf > 1 - 1e-5)
    types3 = [(0.5, 0.3, s1), (0.4, 0.3, s2), (0.1, 0.3, s3)]
    xs3, xf3 = unr(types3, [0.01, 0.01, 0.01])
    print(f"   adding a type of mass 0.1 with s=0.24(1-x) < c at every x: from 1% outside in each type, outside shares ({', '.join(f'{v:.4f}' for v in xs3)}), outside share {xf3:.4f}")
    okU &= xs3[2] > 1 - 1e-5 and xs3[0] < 1e-5 and xs3[1] < 1e-5
    expect(okU, "unravel across types: below min_k x_k^dagger (0.375) every state returns (800/800); just above it type 1 leaves, settling at 0.5 when its mass is 0.5 "
                "and carrying type 2 out when it is 0.8; a type with s_k(0) <= c_k leaves from every state, so full participation is impossible")


def ext_PR():
    subblock('PR', 'onegroup', 'independent',
             'Lemma 3.10 under nonlinear payoff-monotone fitness: total and within-group terms <= 0 always; the between-group term only under affine fitness')
    # Sources (ported): planning/math-fable/f4_selection.py (B); planning/math-opus/m05_selection.py (C);
    # ../v6.1/reviews/counterexamples_v61_codex.py case 8; ../v6.1/reviews/scripts-v6.1-math-opus/s5_misc.py (Lemma 3.10).
    def cov(a, b):
        ma = sum(a) / len(a); mb = sum(b) / len(b)
        return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / len(a)
    print("(e) f4(B): 600 random populations, random partitions, four families of increasing fitness maps")
    rnd = random.Random(5)
    bad_total = bad_within = 0; between_pos = 0; affine_between_pos = 0; trials = 0
    for _ in range(600):
        N = rnd.randint(6, 40); z = [rnd.random() for _ in range(N)]
        b, c = rnd.uniform(0.2, 2.0), rnd.uniform(0.2, 2.0)
        zpop = sum(z) / N
        pi = [b * zpop - c * zz for zz in z]
        kind = rnd.choice(["affine", "concave", "convex", "mixed"])
        if kind == "affine":
            k = rnd.uniform(0.1, 3); phi = lambda x, k=k: 1 + k * x
        elif kind == "concave":
            k = rnd.uniform(0.5, 8); phi = lambda x, k=k: -math.exp(-k * x)
        elif kind == "convex":
            k = rnd.uniform(0.5, 6); phi = lambda x, k=k: math.exp(k * x)
        else:
            k = rnd.uniform(1, 6); phi = lambda x, k=k: x + math.sin(k * x) / k * 0.9 + 2
        w = [phi(x) for x in pi]
        G = rnd.randint(2, min(6, N // 2))
        groups = [[] for _ in range(G)]
        for j in range(N): groups[rnd.randrange(G)].append(j)
        groups = [g for g in groups if g]
        total = cov(z, w)
        zg = [sum(z[j] for j in g) / len(g) for g in groups]; wg = [sum(w[j] for j in g) / len(g) for g in groups]
        between = cov([zg[i] for i, g in enumerate(groups) for _ in g], [wg[i] for i, g in enumerate(groups) for _ in g])
        within_terms = [cov([z[j] for j in g], [w[j] for j in g]) for g in groups]
        trials += 1
        if total > 1e-12: bad_total += 1
        if any(t > 1e-12 for t in within_terms): bad_within += 1
        if between > 1e-12:
            between_pos += 1
            if kind == "affine": affine_between_pos += 1
    print(f"   total > 0: {bad_total}/{trials}; any within-group term > 0: {bad_within}/{trials}; between > 0: {between_pos}/{trials} (under affine fitness: {affine_between_pos})")
    expect(bad_total == 0 and bad_within == 0 and between_pos > 0 and affine_between_pos == 0,
           f"f4(B): total and within-group terms are never positive (0/600); the between-group term is positive in {between_pos}/600, never under affine fitness")
    groups = [[0.0, 1.0], [0.4, 0.4]]
    mean = lambda seq: sum(seq) / len(seq)
    def covariance(a, b): return mean([x * y for x, y in zip(a, b)]) - mean(a) * mean(b)
    fitness = [[math.exp(-5 * z) for z in group] for group in groups]
    between = covariance([mean(g) for g in groups], [mean(w) for w in fitness])
    within = mean([covariance(g, w) for g, w in zip(groups, fitness)])
    total = covariance([z for g in groups for z in g], [w for g in fitness for w in g])
    ok8 = between > 0 > total and math.isclose(total, between + within)
    print(f"(f) Codex 8: groups (0,1),(0.4,0.4), w=e^(-5z): between {between:+.5f}, within {within:+.5f}, total {total:+.5f}")
    expect(ok8, "Codex 8: a nonlinear monotone fitness makes the between-group term positive (+0.0092) while total selection still opposes the trait (-0.1150)")
    _codex(9, ok8)
    print("(g) m05(C): six increasing transforms x 3,000 random populations, size-weighted Price terms")
    def price_terms(groups, psi, b=0.5, cost=0.2, w0=1.0):
        pop = [z for g in groups for z in g]; N = len(pop)
        zbar = sum(pop) / N
        fit = [[psi(w0 + b * zbar - cost * z) for z in g] for g in groups]
        allw = [w for g in fit for w in g]
        mean_ = lambda v: sum(v) / len(v)
        def cov_(a, b_):
            ma, mb = mean_(a), mean_(b_); return mean_([(x - ma) * (y - mb) for x, y in zip(a, b_)])
        total = cov_(allw, pop)
        wsz = [len(g) / N for g in groups]
        zg = [mean_(g) for g in groups]; wg = [mean_(f) for f in fit]
        mz = sum(s * z for s, z in zip(wsz, zg)); mw = sum(s * w for s, w in zip(wsz, wg))
        between = sum(s * (z - mz) * (w - mw) for s, z, w in zip(wsz, zg, wg))
        within = sum(s * cov_(f, g) for s, f, g in zip(wsz, fit, groups))
        return total, between, within
    transforms = {'affine 1+2pi': lambda p: 1 + 2 * p, 'exp(5 pi)': lambda p: math.exp(5 * p),
                  'log(.05+pi)': lambda p: math.log(0.05 + p) if p > -0.05 else -1e9, 'pi^3 (on pi>0)': lambda p: max(p, 0) ** 3,
                  'logistic 20(pi-1)': lambda p: 1 / (1 + math.exp(-20 * (p - 1))), 'step-like tanh(50(pi-.95))': lambda p: math.tanh(50 * (p - 0.95))}
    random.seed(3); okC = True
    for name, psi in transforms.items():
        tot_pos = within_pos = between_pos = 0; T = 3000; maxb = 0.0
        for _ in range(T):
            k = random.randint(2, 6)
            groups = [[random.random() if random.random() < 0.7 else random.choice([0.0, 1.0]) for _ in range(random.randint(2, 6))] for _ in range(k)]
            t, bt, wi = price_terms(groups, psi)
            tot_pos += t > 1e-12; within_pos += wi > 1e-12; between_pos += bt > 1e-12; maxb = max(maxb, bt)
            okC &= abs(t - bt - wi) < 1e-9
        okC &= tot_pos == 0 and within_pos == 0 and (between_pos == 0 if name.startswith('affine') else True)
        print(f"   {name:28s}: total>0 in {tot_pos}/{T}; within>0 in {within_pos}/{T}; between>0 in {between_pos}/{T} (largest between {maxb:.2e})")
    for groups, psi, tag in (([[0.0, 1.0], [0.6, 0.6]], lambda p: math.log(1.05 + p), 'Opus: log(1.05+pi), payoff -z'),
                             ([[0.0, 1.0], [0.4, 0.4]], lambda p: math.exp(5 * p), 'Codex: exp(-5z)')):
        t, bt, wi = price_terms(groups, psi, b=0.0, cost=1.0, w0=0.0)
        print(f"   {tag}: total {t:+.6f}, between {bt:+.6f}, within {wi:+.6f}")
    expect(okC, "m05(C): the decomposition is an identity; total and within terms <= 0 under all six transforms (18,000 populations); between > 0 occurs only for non-affine transforms")
    print("(h) s5_misc (Math-Opus reviewer): two groups, global benefit, concave fitness maps")
    b, c = 1.0, 1.0; zA = [0.0, 1.0]; zB = [0.6, 0.6]; zbar = (sum(zA) + sum(zB)) / 4; sgn = []
    for name, phi in [('linear', lambda x: 1 + x), ('concave 1-exp(-8(x+1))', lambda x: 1 - math.exp(-8 * (x + 1))), ('concave log(1.05+x)', lambda x: math.log(1.05 + x))]:
        w = lambda z: phi(b * zbar - c * z)
        wA = sum(w(z) for z in zA) / 2; wB = sum(w(z) for z in zB) / 2
        gz = [sum(zA) / 2, sum(zB) / 2]; gw = [wA, wB]; mz = sum(gz) / 2; mw = sum(gw) / 2
        cb = sum((a - mz) * (bb - mw) for a, bb in zip(gz, gw)) / 2
        allz = zA + zB; allw = [w(z) for z in allz]
        ct = sum((a - sum(allz) / 4) * (bb - sum(allw) / 4) for a, bb in zip(allz, allw)) / 4
        sgn.append((cb, ct))
        print(f"   {name}: between-group Cov(w_g,z_g) = {cb:+.4f}; total Cov(w,z) = {ct:+.4f}")
    expect(sgn[0][0] < 0 and sgn[1][0] > 0 and sgn[2][0] > 0 and all(ct < 0 for _, ct in sgn), "s5_misc: linear fitness gives a negative between term; concave maps a positive one; total negative in all three")


def ext_CS():
    subblock('CS', 'influence, corrrate, costq', 'independent',
             'Section 4 at eta != 1 and fractional size elasticities; Y_hat scaling; the rate law at eta = 0.5 and 2')
    # Sources (ported): ../v6.1/reviews/scripts-v6.1-math-fable/m4_cost.py (a)-(e); ../v6.1/reviews/scripts-v6.1-math-opus/s4_cost.py (a);
    # planning/math-fable/f5_corrrate.py (D).
    def payoff(q, p, chi, Y, d, f, xf, gam, xv, eta):
        return chi * q * p * p * Y / d - f * p ** xf * q - gam * p ** xv * q ** (1 + eta) / (1 + eta)
    def qstar(p, chi, Y, d, f, xf, gam, xv, eta):
        best = (payoff(0.0, p, chi, Y, d, f, xf, gam, xv, eta), 0.0)
        grid = [10 ** (-10 + 50 * k / 2000) for k in range(2001)]
        for q in grid:
            v = payoff(q, p, chi, Y, d, f, xf, gam, xv, eta)
            if v > best[0]: best = (v, q)
        if best[1] == 0.0: return 0.0
        lo, hi = best[1] / 1.05, best[1] * 1.05
        g = (math.sqrt(5) - 1) / 2; x1 = hi - g * (hi - lo); x2 = lo + g * (hi - lo)
        fn = lambda q: payoff(q, p, chi, Y, d, f, xf, gam, xv, eta)
        f1, f2 = fn(x1), fn(x2)
        for _ in range(200):
            if f1 < f2: lo = x1; x1 = x2; f1 = f2; x2 = lo + g * (hi - lo); f2 = fn(x2)
            else: hi = x2; x2 = x1; f2 = f1; x1 = hi - g * (hi - lo); f1 = fn(x1)
        return (lo + hi) / 2
    def slope(xs, ys):
        n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
        return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    chi, Y = 1.0, 1.0
    print("(f) m4(a): size threshold exponent 1/(2-xf), f=0.05 (q* by grid maximization, not the first-order condition)")
    okA = True
    for xf in (0.0, 0.3, 0.7, 1.0):
        lo, hi = 1e-6, 1.0
        for _ in range(60):
            m = (lo + hi) / 2
            if qstar(m, chi, Y, 1.0, 0.05, xf, 1.0, 0.0, 1.0) > 0: hi = m
            else: lo = m
        okA &= abs(hi - 0.05 ** (1 / (2 - xf))) < 1e-4
        print(f"   xf={xf}: threshold {hi:.5f} vs (f/(chi Y))^(1/(2-xf)) = {0.05**(1/(2-xf)):.5f}")
    print("(g) m4(b): exponents of q*, p q* and spending in p (f=0), log-log regression over p in [0.05, 1]")
    ps = [0.05 * 1.35 ** k for k in range(9) if 0.05 * 1.35 ** k <= 1.0]
    for eta in (0.5, 1.0, 2.0):
        for xv in (0.0, 0.3, 1.0):
            qs = [qstar(p, chi, Y, 1.0, 0.0, 0, 1.0, xv, eta) for p in ps]
            sq = slope([math.log(p) for p in ps], [math.log(q) for q in qs])
            spend = [1.0 * p ** xv * q ** (1 + eta) / (1 + eta) for p, q in zip(ps, qs)]
            ss = slope([math.log(p) for p in ps], [math.log(s) for s in spend])
            okA &= abs(sq - (2 - xv) / eta) < 2e-3 and abs(ss - (2 + (2 - xv) / eta)) < 4e-3
            print(f"   eta={eta}, xv={xv}: q* ~ p^{sq:.3f} (formula {(2-xv)/eta:.3f}); p q* ~ p^{sq+1:.3f}; spending ~ p^{ss:.3f} (formula {2+(2-xv)/eta:.3f})")
    print("(h) m4(c): splitting factor k^((2-xv)/eta) (f=0)")
    for eta in (0.5, 2.0):
        for xv in (0.0, 0.5, 1.0):
            mono = qstar(1.0, chi, Y, 1.0, 0.0, 0, 1.0, xv, eta); out = []
            for k in (2, 5):
                part = k * (1 / k) * qstar(1 / k, chi, Y, 1.0, 0.0, 0, 1.0, xv, eta)
                okA &= abs(mono / part / k ** ((2 - xv) / eta) - 1) < 1e-3
                out.append(f"k={k}: {mono/part:.3f} vs {k**((2-xv)/eta):.3f}")
            print(f"   eta={eta}, xv={xv}: " + "; ".join(out))
    print("(i) m4(d): rate law at eta = 0.5 and 2 (threshold alpha_ctl/(1+eta)); growth rate of the cultivated term (g-(1+eta)alpha)/eta")
    for eta in (0.5, 2.0):
        thr = 0.2 / (1 + eta)
        for alpha in (thr - 0.02, thr + 0.02):
            vals = []
            for t in (0, 50, 100, 150):
                gam = math.exp(-0.2 * t); d = 2.0 * math.exp(alpha * t)
                q = qstar(0.6, chi, Y, d, 0.0, 0, gam, 0.5, eta); vals.append((0.3 + 0.6 * q) / d)
            emp = (math.log(0.6 * qstar(0.6, chi, Y, 2.0 * math.exp(alpha * 150), 0.0, 0, math.exp(-30), 0.5, eta) / (2.0 * math.exp(alpha * 150)))
                   - math.log(0.6 * qstar(0.6, chi, Y, 2.0 * math.exp(alpha * 50), 0.0, 0, math.exp(-10), 0.5, eta) / (2.0 * math.exp(alpha * 50)))) / 100
            okA &= abs(emp - (0.2 - (1 + eta) * alpha) / eta) < 1e-3 and ((vals[-1] > 1) == (alpha < thr))
            print(f"   eta={eta}, alpha={alpha:.4f} ({'below' if alpha < thr else 'above'} {thr:.4f}): G at t=0,50,100,150: {', '.join('%.3g'%v for v in vals)}; growth rate {emp:+.4f} vs {(0.2-(1+eta)*alpha)/eta:+.4f}")
    base = dict(p=0.5, chi=1.0, Y=1.0, d=1.0, f=0.0, xf=0, gam=1.0, xv=0.4, eta=1.7)
    def q_of(**kw):
        a = dict(base); a.update(kw); return qstar(a['p'], a['chi'], a['Y'], a['d'], a['f'], a['xf'], a['gam'], a['xv'], a['eta'])
    h = 1e-3
    sg = ((q_of(gam=1 + h) - q_of(gam=1 - h)) / (2 * h), (q_of(d=1 + h) - q_of(d=1 - h)) / (2 * h), (q_of(chi=1 + h) - q_of(chi=1 - h)) / (2 * h))
    print(f"(j) m4(e): signs at eta=1.7, xv=0.4, p=0.5: dq*/dgam = {sg[0]:+.4f}, dq*/dd = {sg[1]:+.4f}, dq*/dchi = {sg[2]:+.4f}")
    expect(okA and sg[0] < 0 and sg[1] < 0 and sg[2] > 0,
           "m4: size threshold 1/(2-xf), q* ~ p^((2-xv)/eta), spending ~ p^(2+(2-xv)/eta), splitting k^((2-xv)/eta) and the rate law alpha_ctl/(1+eta) hold at eta = 0.5, 1, 2 and fractional xv, xf")
    # s4_cost (a) (Math-Opus reviewer): 300 random (xf, xv, eta), bisection q*
    def qstar4(p, chi, Y, d, f, xf, gam, xv, eta):
        def dpay(q): return chi * p * p * Y / d - f * p ** xf - gam * p ** xv * q ** eta
        if dpay(0.0) <= 0: return 0.0
        lo, hi = -400.0, 400.0
        for _ in range(200):
            m = (lo + hi) / 2
            if dpay(math.exp(m)) > 0: lo = m
            else: hi = m
        return math.exp((lo + hi) / 2)
    def threshold4(f, xf, xv=0.0, eta=1.0):
        lo, hi = 1e-9, 1.0
        for _ in range(100):
            m = (lo + hi) / 2
            if qstar4(m, 1.0, 1.0, 1.0, f, xf, 1.0, xv, eta) > 0: hi = m
            else: lo = m
        return hi
    rnd = random.Random(7); bad = dict(thr=0, split=0, conc=0, spend=0)
    for _ in range(300):
        xf, xv, eta = rnd.uniform(0, 1), rnd.uniform(0, 1), rnd.uniform(0.2, 3)
        e_thr = (math.log(threshold4(2e-3, xf, xv=xv, eta=eta)) - math.log(threshold4(1e-3, xf, xv=xv, eta=eta))) / math.log(2)
        if abs(e_thr - 1 / (2 - xf)) > 1e-4: bad['thr'] += 1
        q1 = qstar4(0.3, 1, 1, 1, 0, 0, 1, xv, eta); q2 = qstar4(0.6, 1, 1, 1, 0, 0, 1, xv, eta)
        e_q = math.log(q2 / q1) / math.log(2)
        k = 7
        mono = 1.0 * qstar4(1.0, 1, 1, 1, 0, 0, 1, xv, eta); split = k * (1 / k) * qstar4(1 / k, 1, 1, 1, 0, 0, 1, xv, eta)
        if abs(math.log(mono / split) / math.log(k) - (2 - xv) / eta) > 1e-6: bad['split'] += 1
        if abs(e_q - (2 - xv) / eta) > 1e-6: bad['conc'] += 1
        s1 = 0.3 ** xv * q1 ** (1 + eta) / (1 + eta); s2 = 0.6 ** xv * q2 ** (1 + eta) / (1 + eta)
        if abs(math.log(s2 / s1) / math.log(2) - (xv + (1 + eta) * (2 - xv) / eta)) > 1e-6: bad['spend'] += 1
    print(f"(k) s4_cost(a): 300 random (xf, xv, eta): mismatches against the stated exponents {bad}")
    expect(all(v == 0 for v in bad.values()), "s4_cost(a): threshold, splitting, concentration and spending exponents hold in 300/300 random settings")
    print("(l) f5(D): Y_hat = p^2 ybar^T A_hat ybar: q* ~ p^((2-xi_v)/eta), so splitting into k parts divides Y_hat by k^2")
    okD = True
    for (xv, eta) in [(0, 1), (1, 1), (0, 2), (0.5, 0.5)]:
        q1 = qstar4(0.3, 1, 1, 1, 0, 0, 1, xv, eta); q2 = qstar4(0.6, 1, 1, 1, 0, 0, 1, xv, eta)
        sl = math.log(q2 / q1) / math.log(2); okD &= abs(sl - (2 - xv) / eta) < 1e-6
        print(f"   xi_v={xv} eta={eta}: d ln q*/d ln p = {sl:.4f} vs (2-xi_v)/eta = {(2-xv)/eta:.4f}")
    expect(okD, "f5(D): q* scales as p^((2-xi_v)/eta) in 4/4 (2, 1, 1, 3)")


def ext_DW():
    subblock('DW', 'pausefield, dwell, reachable', 'independent',
             'Dwell by an independent method (separatrix by backward integration, analytic insulated path); depth of lock-in; a floor on alternatives; the frozen-share pause')
    # Sources (ported): ../v6.1/reviews/scripts-v6.1-systems/s2_dwell.py, s2b_depth.py, s2c_pause.py.
    # Claims (plan s4 'pausefield', s4 'dwell depth ... 10.45 -> 3.81'): the dwell depends on the depth of lock-in; a
    # recruitable lineage at a floor lam bounds it; the share-freezing pause must last ln(G/S(x_p))/(eps d).
    def sig(u): return 1 / (1 + math.exp(-u)) if u >= 0 else math.exp(u) / (1 + math.exp(u))
    def logit(x): return math.log(x / (1 - x))
    def separatrix(G, eps, zeta=1.0, h=1e-4, dt=1e-3):
        us = -math.log(G - 1.0); b = G
        lam = (-eps - math.sqrt(eps * eps + 4 * zeta * eps * (1 - 1 / G))) / 2
        v = (1.0, lam / zeta); nv = math.hypot(*v); v = (v[0] / nv, v[1] / nv)
        def f(u, z): return (-zeta * (z - 1.0), -eps * (b * sig(u) - z))
        pts = []
        for sgn in (1, -1):
            u, z = us + sgn * h * v[0], 1.0 + sgn * h * v[1]; br = [(u, z)]
            for _ in range(4000000):
                k1 = f(u, z); k2 = f(u + dt / 2 * k1[0], z + dt / 2 * k1[1]); k3 = f(u + dt / 2 * k2[0], z + dt / 2 * k2[1]); k4 = f(u + dt * k3[0], z + dt * k3[1])
                u += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6; z += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
                br.append((u, z))
                if z < -0.05 or z > 60 or u < -60: break
            pts += br
        pts.sort()
        return pts
    def zsep(pts, u):
        if u <= pts[0][0]: return float('inf')
        if u >= pts[-1][0]: return -float('inf')
        lo, hi = 0, len(pts) - 1
        while hi - lo > 1:
            m = (lo + hi) // 2
            if pts[m][0] <= u: lo = m
            else: hi = m
        (u0, z0), (u1, z1) = pts[lo], pts[hi]
        return z0 + (z1 - z0) * (u - u0) / (u1 - u0) if u1 > u0 else z0
    def x_sigma(pts):
        for (u0, z0), (u1, z1) in zip(pts, pts[1:]):
            if z0 >= 0 > z1: return sig(u0 + (u1 - u0) * z0 / (z0 - z1))
        return None
    def tmin_analytic(G, eps, pts, zeta=1.0, x0=0.99, ucap=None, dt=1e-3):
        u0 = logit(x0); t = 0.0
        tpk = math.log(G) / eps
        while t < 500 / eps:
            if ucap is None:
                u = u0 + zeta * (G * (1 - math.exp(-eps * t)) / eps - t)
            else:
                tc = None
                f = lambda s: u0 + zeta * (G * (1 - math.exp(-eps * s)) / eps - s) - ucap
                if f(tpk) > 0:
                    lo, hi = 0.0, tpk
                    for _ in range(80):
                        m = (lo + hi) / 2
                        if f(m) > 0: hi = m
                        else: lo = m
                    tc = hi
                if tc is None or t <= tc: u = min(u0 + zeta * (G * (1 - math.exp(-eps * t)) / eps - t), ucap)
                elif t <= tpk: u = ucap
                else: u = ucap + zeta * (G * (math.exp(-eps * tpk) - math.exp(-eps * t)) / eps - (t - tpk))
            z = G * math.exp(-eps * t)
            if z < zsep(pts, u): return t * eps
            t += dt / eps
        return float('inf')
    print("(a) s2: T_min*eps*d by separatrix + analytic insulated path (DW above: eps/zeta=0.1: 1.886, 5.318, 10.453; eps=zeta: 5.859, 10.343, 16.181)")
    seps = {}; tm = {}; xs = {}
    for eps in (0.1, 1.0):
        row = []
        for G in (2, 5, 10):
            pts = separatrix(G, eps); seps[(G, eps)] = pts
            tm[(G, eps)] = tmin_analytic(G, eps, pts); xs[(G, eps)] = x_sigma(pts)
            row.append(f"G={G}: {tm[(G,eps)]:.3f} (x_sigma={xs[(G,eps)]:.3f})")
        print(f"   eps/zeta={eps}: " + "; ".join(row))
    ref = {(2, 0.1): 1.886, (5, 0.1): 5.318, (10, 0.1): 10.453, (2, 1.0): 5.859, (5, 1.0): 10.343, (10, 1.0): 16.181}
    expect(all(abs(tm[k] - v) < 2e-3 for k, v in ref.items()) and abs(xs[(2, 1.0)] - 0.676) < 2e-3 and abs(xs[(2, 0.1)] - 0.984) < 2e-3,
           "s2: a second method (backward-integrated separatrix, analytic path) reproduces DW's dwell to 3 decimals in 6/6; x_sigma = 0.676 at eps=zeta, 0.984 at eps/zeta = 0.1 (G=2)")
    print("(b) s2(A): a hard floor lam on the alternative share bounds the dwell (cap on u during insulation)")
    capd = {}
    for lam in (1e-2, 1e-3, 1e-6, 1e-12):
        ucap = logit(1 - lam); row = []
        for eps in (0.1, 1.0):
            for G in (5, 10):
                v = tmin_analytic(G, eps, seps[(G, eps)], ucap=ucap); capd[(lam, G, eps)] = v
                row.append(f"G={G},e/z={eps}: {v:.2f}")
        print(f"   lam={lam:g}: " + "  ".join(row))
    expect(abs(capd[(1e-3, 10, 0.1)] - 3.81) < 0.01 and capd[(1e-3, 10, 0.1)] < tm[(10, 0.1)],
           f"s2(A): a recruitable lineage held at 0.1% bounds the dwell at G=10, eps/zeta=0.1 from {tm[(10,0.1)]:.2f} to {capd[(1e-3,10,0.1)]:.2f} (10.45 -> 3.81)")
    def fate_mut(u, z, G, eps, mu, zeta=1.0, dt=0.01, T=3000):
        b = G
        def f(u, z):
            x = sig(u)
            return (zeta * (z - 1.0) + mu * (1 - 2 * x) / max(x * (1 - x), 1e-300), eps * (b * x - z))
        for _ in range(int(T / dt)):
            k1 = f(u, z); k2 = f(u + dt / 2 * k1[0], z + dt / 2 * k1[1]); k3 = f(u + dt / 2 * k2[0], z + dt / 2 * k2[1]); k4 = f(u + dt * k3[0], z + dt * k3[1])
            u += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6; z += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
            if z > 0.5 * (1 + G) and u > 2: return 'cap'
            if z < 0.2 and u < -2: return 'abs'
        return 'cap' if u > 0 else 'abs'
    def tmin_mut(G, eps, lam, zeta=1.0, dt=0.01, x0=None):
        mu = lam * zeta * (G - 1)
        if x0 is None: u, z = logit(1 - lam), G * (1 - lam)
        else: u, z = logit(x0), float(G)
        def after(T):
            uu, zz = u, z; n = int(T / dt)
            def f(uu, zz):
                x = sig(uu); return (zeta * (zz - 1.0) + mu * (1 - 2 * x) / max(x * (1 - x), 1e-300), -eps * zz)
            for _ in range(n):
                k1 = f(uu, zz); k2 = f(uu + dt / 2 * k1[0], zz + dt / 2 * k1[1]); k3 = f(uu + dt / 2 * k2[0], zz + dt / 2 * k2[1]); k4 = f(uu + dt * k3[0], zz + dt * k3[1])
                uu += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6; zz += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
            return fate_mut(uu, zz, G, eps, mu)
        lo, hi = 0.0, 40.0 / eps
        for _ in range(26):
            m = (lo + hi) / 2
            if after(m) == 'cap': lo = m
            else: hi = m
        return hi * eps
    print("(c) s2(B), s2b(B'): mutation/re-seeding at rate mu = lam*zeta*(G-1), from its own captured equilibrium and from x0 = 0.99")
    mut = {}
    for lam in (1e-3, 1e-6):
        r1 = [(G, eps, tmin_mut(G, eps, lam)) for eps in (0.1, 1.0) for G in (5, 10)]
        r2 = [(G, eps, tmin_mut(G, eps, lam, x0=0.99)) for eps in (0.1, 1.0) for G in (5, 10)]
        for G, eps, v in r1: mut[(lam, G, eps)] = v
        print(f"   lam={lam:g}, own equilibrium: " + "  ".join(f"G={G},e/z={eps}: {v:.2f}" for G, eps, v in r1))
        print(f"   lam={lam:g}, from x0=0.99:    " + "  ".join(f"G={G},e/z={eps}: {v:.2f}" for G, eps, v in r2))
    expect(mut[(1e-3, 10, 0.1)] < tm[(10, 0.1)] and mut[(1e-3, 10, 0.1)] < mut[(1e-6, 10, 0.1)],
           f"s2(B): a recruitable alternative at 0.1% (mutation) bounds the dwell too ({mut[(1e-3,10,0.1)]:.2f} at G=10, eps/zeta=0.1), less at 1e-6 ({mut[(1e-6,10,0.1)]:.2f})")
    pts = separatrix(10 * (1 - 1e-3), 0.1); pr = tmin_analytic(10 * (1 - 1e-3), 0.1, pts)
    print(f"(d) s2(C): a protected share outside selection that does not recruit (b -> b(1-lam), lam=1e-3): G=9.99, eps/zeta=0.1: {pr:.2f} (essentially unchanged)")
    expect(abs(pr - tm[(10, 0.1)]) < 0.05, "s2(C): a protected share that does not recruit leaves the dwell essentially unchanged (10.44): the bound needs a recruitable lineage")
    print("(e) s2b: no floor: T_min*eps*d as a function of the starting share x0 (depth of lock-in; the paper fixes x0=0.99)")
    depth = {}
    for eps in (0.1, 1.0):
        for G in (2, 10):
            pts_ = seps[(G, eps)]
            row = []
            for x0 in (0.9, 0.99, 1 - 1e-3, 1 - 1e-6, 1 - 1e-12):
                v = tmin_analytic(G, eps, pts_, x0=x0); depth[(G, eps, x0)] = v; row.append(f"x0=1-{1-x0:.0e}: {v:.2f}")
            print(f"   G={G}, eps/zeta={eps}: " + "  ".join(row))
    print("   at the captured state logit x grows at zeta(G-1) per unit time: after capture has lasted A, x0 ~ 1-exp(-zeta(G-1)A); the dwell grows ~linearly with the age of capture")
    expect(all(depth[(G, eps, 0.9)] < depth[(G, eps, 0.99)] < depth[(G, eps, 1 - 1e-12)] for G in (2, 10) for eps in (0.1, 1.0)) and depth[(2, 1.0, 1 - 1e-12)] > 28,
           "s2b: the dwell rises with the depth of lock-in (G=2, eps=zeta: 5.86 at x0=0.99, 28.9 at 1-1e-12) unless a floor on alternatives bounds it")
    print("(f) s2c: the share-freezing pause with rule-making insulated: required length ln(G/S(x_p))/(eps d), S = separatrix height at the frozen share")
    sc = {}
    for eps in (1.0, 0.1):
        for G in (2, 5):
            pts_ = seps[(G, eps)] if (G, eps) in seps else separatrix(G, eps)
            row = []
            for xp in (0.1, 0.3, 1 / G, 0.6, 0.8, 0.95):
                S = zsep(pts_, logit(xp)); T = math.log(G / S) if S > 0 else float('inf'); sc[(eps, G, round(xp, 3))] = T
                row.append(f"x_p={xp:.2f}: S={S:.2f}, eps*d*T={T:.2f}")
            print(f"   eps/zeta={eps}, G={G} (ln G={math.log(G):.2f}, x_sigma={x_sigma(pts_):.3f}): " + "; ".join(row))
    expect(sc[(1.0, 2, 0.3)] < 0 and abs(sc[(1.0, 2, 0.5)] - math.log(2)) < 1e-2 and abs(sc[(1.0, 2, 0.6)] - 1.50) < 0.01 and sc[(1.0, 2, 0.8)] == float('inf'),
           "s2c: at equal speeds and G=2 no pause is needed at x_p=0.3, ln G at x_p=1/G, 1.5/(eps d) at 0.6, and none suffices above x_sigma=0.68")


def ext_CR():
    subblock('CR', 'relpunish', 'independent',
             'Strictness of the role-differentiated punishment; label asymmetry; random anonymous perturbations; a relative punisher is indifferent about whom it hurts')
    # Sources (ported): planning/math-fable/f6_enforce.py (E); planning/math-opus/m08_relpunish.py (A),(B);
    # ../v6.1/reviews/scripts-v6.1-math-fable/m3_cor55.py; ../v6.1/reviews/scripts-v6.1-math-opus/s3_enforce.py (5).
    acts = [(x, m) for x in "RA" for m in "XY"]
    def pis(prof, eps=0.0, a=0.1, b=0.1):
        out = []
        for i, (x, m) in enumerate(prof):
            unique = all(m2 != m for j, (x2, m2) in enumerate(prof) if j != i)
            prize = (1.0 + (eps if m == "X" else 0.0)) if unique else 0.0
            out.append(prize + (a if x == "A" else 0.0) - b * sum(1 for j, (x2, m2) in enumerate(prof) if j != i and x2 == "A"))
        return out
    def O(prof, eps=0.0):
        p = pis(prof, eps); return [p[i] - (sum(p) - p[i]) / 2 for i in range(3)]
    pun = [("A", "X"), ("A", "X"), ("A", "Y")]
    print("(d) f6(E): strictness of the printed punishment under +-eps on the X prize")
    kinds = {}
    for eps in (0.0, 0.02, -0.02):
        base = O(pun, eps); margins = []
        for i in range(3):
            best = max(O(list(pun[:i]) + [a] + list(pun[i + 1:]), eps)[i] for a in acts if a != pun[i])
            margins.append(base[i] - best)
        kind = "strict NE" if min(margins) > 1e-12 else ("weak NE" if min(margins) > -1e-12 else "not an equilibrium")
        kinds[eps] = kind
        print(f"   eps={eps:+.2f}: objectives {[round(v,3) for v in base]}, margins over best deviation {[round(m,3) for m in margins]} -> {kind}")
    expect(kinds[0.0] == "weak NE" and kinds[0.02] == "strict NE" and kinds[-0.02] == "not an equilibrium",
           "f6(E): the printed punishment is a weak stage equilibrium, strict under +0.02 on the X prize, destroyed by -0.02 (roles must then swap)")
    ACTS = [(r, l) for r in ('R', 'A') for l in ('X', 'Y')]
    def base_payoffs(profile, eps_label=0.0, pert=None):
        n = len(profile); pi = [0.0] * n
        for i, (r, l) in enumerate(profile):
            others = [profile[j][1] for j in range(n) if j != i]
            if l not in others: pi[i] += 1.0 + (eps_label if l == 'X' else 0.0)
            if r == 'A':
                pi[i] += 0.1
                for j in range(n):
                    if j != i: pi[j] -= 0.1
        if pert:
            for i in range(n):
                others = tuple(sorted(profile[j] for j in range(n) if j != i))
                pi[i] += pert(profile[i], others)
        return pi
    def J(profile, i, **kw):
        pi = base_payoffs(profile, **kw)
        return pi[i] - sum(pi[j] for j in range(len(pi)) if j != i) / (len(pi) - 1)
    def dev_gains(profile, **kw):
        out = []
        for i in range(3):
            base = J(profile, i, **kw)
            best = max(J(tuple(a if k == i else profile[k] for k in range(3)), i, **kw) for a in ACTS if a != profile[i])
            out.append(best - base)
        return out
    print("(e) m08(A,B): the printed example; label asymmetry; random anonymous perturbations")
    prof = (('A', 'X'), ('A', 'X'), ('A', 'Y'))
    coop = (('R', 'X'),) * 3
    g = max(J(tuple(a if k == 0 else coop[k] for k in range(3)), 0) for a in ACTS)
    print(f"   deviator's objective {J(prof, 0):+.3f}; best unilateral deviation gains {[round(x, 3) for x in dev_gains(prof)]}; deviation gain from cooperation {g:.3f}; delta* = {g/(g+0.5):.3f}")
    strict_map = {}
    for eps in (0.01, 0.05, -0.05):
        p1 = (('A', 'X'), ('A', 'X'), ('A', 'Y')); p2 = (('A', 'Y'), ('A', 'Y'), ('A', 'X'))
        for prof_, tag in ((p1, 'roles (X,X,Y)'), (p2, 'roles (Y,Y,X)')):
            gains = dev_gains(prof_, eps_label=eps); v = J(prof_, 0, eps_label=eps)
            gdev = max(J(tuple(a if k == 0 else coop[k] for k in range(3)), 0, eps_label=eps) for a in ACTS)
            strict = all(x < -1e-12 for x in gains); strict_map[(eps, tag)] = strict
            print(f"   eps={eps:+.2f} {tag}: deviator held at {v:+.3f}; deviation gains {[round(x, 4) for x in gains]} -> {'STRICT' if strict else 'not strict'}"
                  + (f"; delta* = {gdev/(gdev-v):.3f}" if strict and v < 0 else ''))
    random.seed(1); found_by = {}
    for e in (0.02, 0.05, 0.1):
        found = 0; T = 300; dstars = []
        for _ in range(T):
            table = {}
            def pert(a, others, table=table, e=e):
                key = (a, others)
                if key not in table: table[key] = random.uniform(-e, e)
                return table[key]
            g_ = max(J(tuple(a if k == 0 else coop[k] for k in range(3)), 0, pert=pert) for a in ACTS) - J(coop, 0, pert=pert)
            best = None
            for prof_ in itertools.product(ACTS, repeat=3):
                v = J(prof_, 0, pert=pert) - J(coop, 0, pert=pert)
                if v >= 0: continue
                if all(x < -1e-12 for x in dev_gains(prof_, pert=pert)):
                    if best is None or v < best: best = v
            if best is not None and g_ > 0:
                found += 1; dstars.append(g_ / (g_ - best))
        dstars.sort(); found_by[e] = found
        print(f"   random anonymous perturbations e={e}: a strict punishment holding the deviator below cooperation exists in {found}/{T} games; median delta* {dstars[len(dstars)//2]:.3f}")
    expect(strict_map[(0.01, 'roles (X,X,Y)')] and not strict_map[(0.01, 'roles (Y,Y,X)')] and strict_map[(-0.05, 'roles (Y,Y,X)')]
           and found_by[0.02] == 300 and found_by[0.05] == 300 and found_by[0.1] >= 270,
           f"m08: strict under any label asymmetry with roles assigned accordingly; strict punishments exist in 300/300, 300/300, {found_by[0.1]}/300 perturbed games")
    print("(f) m3 (Math-Fable reviewer): ties, role preference and the targeted-attack game")
    def make_game(a=0.1, b=0.1, eps=0.0):
        def pis_(prof):
            out = []
            for i, (x, m) in enumerate(prof):
                unique = all(m2 != m for j, (x2, m2) in enumerate(prof) if j != i)
                prize = (1.0 + (eps if m == 'X' else 0.0)) if unique else 0.0
                out.append(prize + (a if x == 'A' else 0.0) - b * sum(1 for j, (x2, m2) in enumerate(prof) if j != i and x2 == 'A'))
            return out
        def O_(prof):
            p = pis_(prof); n = len(p)
            return [p[i] - (sum(p) - p[i]) / (n - 1) for i in range(n)]
        return O_
    okm3 = True
    for (a, b, eps, label) in ((0.1, 0.1, 0.0, "the paper's game"), (0.3, 0.05, 0.0, "other a, b"), (0.1, 0.1, 0.02, "eps=+0.02"), (0.1, 0.1, -0.02, "eps=-0.02")):
        O_ = make_game(a, b, eps)
        c0 = [('R', 'X')] * 3
        g_ = max(O_([act] + c0[1:])[0] for act in acts) - O_(c0)[0]
        alt = [('A', 'X'), ('A', 'Y'), ('A', 'Y')]
        print(f"   {label}: g={g_:.3f}; punishment objectives {[round(x,3) for x in O_(pun)]}; if punisher 1 takes its tie (A,Y) the deviator gets {O_(alt)[0]:+.3f}; "
              f"punisher in the X role {O_(pun)[1]:+.3f} vs Y role {O_(pun)[2]:+.3f}; delta* = {g_/(g_-O_(pun)[0]):.4f}")
        okm3 &= abs(O_(pun)[0] + 0.5) < 1e-12 and O_(pun)[2] > O_(pun)[1]
    c_, L = 0.1, 1.0
    def Ot(pi): return [pi[i] - (sum(pi) - pi[i]) / 2 for i in range(3)]
    att = Ot([-2 * L, -c_, -c_])[1]; abst = Ot([-L, 0.0, -c_])[1]; oth = Ot([-L, -c_, -c_ - L])[1]
    print(f"   targeted attack: punisher 1 attacking the deviator {att:+.3f}; abstaining {abst:+.3f}; attacking the other punisher {oth:+.3f}")
    expect(okm3 and abs(att - oth) < 1e-12 and att > abst,
           "m3: the deviator is held at -0.5 for every a, b; both punishers prefer the Y role (coordination on roles); a theta=-1 punisher is exactly indifferent between hurting the deviator and its fellow")
    print("(g) s3(5) (Math-Opus reviewer): anonymous perturbations, stage-NE punishments holding the deviator below C (400 games each)")
    rnd = random.Random(99)
    for _ in range(20000):   # advance the stream as s3_enforce.py does before section (5): (1) uses 20,000 x 6 draws
        rnd.randint(1, 99); rnd.randint(0, 100); [rnd.randint(-300, 300) for _ in range(4)]
    def mat(prof, a=0.1, b=0.1):
        out = []
        for i, (x, mm) in enumerate(prof):
            unique = all(m2 != mm for j, (x2, m2) in enumerate(prof) if j != i)
            out.append((1.0 if unique else 0.0) + (a if x == 'A' else 0.0) - b * sum(1 for j, (x2, m2) in enumerate(prof) if j != i and x2 == 'A'))
        return out
    def obj(pis_): n = len(pis_); return [pis_[i] - (sum(pis_) - pis_[i]) / (n - 1) for i in range(n)]
    def gaps(prof, payf):
        base = obj(payf(prof)); res = []
        for i in range(3):
            alts = []
            for act in acts:
                if act == prof[i]: continue
                pr = list(prof); pr[i] = act
                alts.append(obj(payf(pr))[i] - base[i])
            res.append(max(alts))
        return base, res
    def anon_table(eps, rnd):
        tab = {}
        for own in acts:
            for others in itertools.combinations_with_replacement(acts, 2):
                tab[(own, tuple(sorted(others)))] = rnd.uniform(-eps, eps)
        return tab
    def payf_from(tab):
        def f(prof):
            base = mat(prof)
            return [base[i] + tab[(prof[i], tuple(sorted(prof[:i] + prof[i + 1:])))] for i in range(3)]
        return f
    s3f = {}
    for eps in (0.01, 0.05, 0.1):
        found = strict = 0; dstars = []
        for _ in range(400):
            tab = anon_table(eps, rnd); pf = payf_from(tab)
            c0 = [('R', 'X')] * 3
            C0 = obj(pf(c0))[0]
            g0 = max(obj(pf([a] + c0[1:]))[0] for a in acts) - C0
            best = None
            for prof_ in itertools.product(acts, repeat=3):
                b_, r_ = gaps(list(prof_), pf)
                if max(r_) <= 1e-12 and b_[0] < C0 - 1e-9:
                    ds = g0 / (g0 + C0 - b_[0]) if g0 > 0 else 0
                    if best is None or ds < best[0]: best = (ds, max(r_) < -1e-9)
            if best is not None:
                found += 1; strict += best[1]; dstars.append(best[0])
        dstars.sort(); s3f[eps] = (found, strict)
        print(f"   eps={eps}: games with a stage-NE punishment holding the deviator below C: {found}/400; of which strict: {strict}; median delta* {dstars[len(dstars)//2]:.3f}")
    expect(s3f[0.01] == (400, 400) and s3f[0.05] == (400, 400) and s3f[0.1][0] == s3f[0.1][1] >= 350,
           f"s3(5): under anonymous perturbations a strict punishment exists in 400/400, 400/400 and {s3f[0.1][0]}/400 games (median delta* about 0.71)")


def ext_TK():
    subblock('TK', 'talk', 'independent',
             'Talk unified: with a common theta among n actors the effective bias is b0 (n-1-theta)/(n-1+theta); informative iff below 1/4')
    # Sources (ported): planning/math-opus/m09_misc.py (check_talk, check_talk_theta); ../v6.1/reviews/scripts-v6.1-math-opus/s5_misc.py (Prop 5.15(2)).
    def argmax(fn, lo=-5, hi=5, it=200):
        for _ in range(it):
            m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
            if fn(m1) < fn(m2): lo = m1
            else: hi = m2
        return (lo + hi) / 2
    print("(d) m09: ideal points at theta=-1 among n, uniform-quadratic, random linear third-party terms")
    random.seed(4); okT = True
    for n in (3, 4, 6, 10):
        b0 = 0.05; u = 0.3; K = random.uniform(-1, 1)
        def JS(y): pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = K * y; return pS - (pR + pk) / (n - 1)
        def JR(y): pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = K * y; return pR - (pS + pk) / (n - 1)
        gap = argmax(JS) - argmax(JR); okT &= abs(gap - b0 * n / (n - 2)) < 1e-6
        print(f"   n={n}: ideal-point gap {gap:.6f}; b0 n/(n-2) = {b0*n/(n-2):.6f}; informative talk iff gap < 1/4 -> material bias below {(n-2)/(4*n):.4f}")
    expect(okT, "m09: at theta=-1 the pair's effective bias is b0 n/(n-2) (0.150, 0.100, 0.075, 0.0625 at b0=0.05), independent of third-party terms")
    print("(e) m09: common theta among n: effective bias b0 (n-1-theta)/(n-1+theta)")
    random.seed(9); worst = 0.0
    for n in (2, 3, 4, 6):
        for th in (-0.9 if n == 2 else -1.0, -0.5, 0.0, 0.5, 1.5):
            b0 = 0.07; u = 0.2; K = random.uniform(-1, 1)
            def J(y, who):
                pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = K * y
                if who == 'S': return pS + th * (pR + (n - 2) * pk) / (n - 1)
                return pR + th * (pS + (n - 2) * pk) / (n - 1)
            gap = argmax(lambda y: J(y, 'S'), -50, 50, 300) - argmax(lambda y: J(y, 'R'), -50, 50, 300)
            pred = b0 * (n - 1 - th) / (n - 1 + th); worst = max(worst, abs(gap - pred))
            print(f"   n={n} theta={th:+.1f}: ideal-point gap {gap:.6f}; formula {pred:.6f}; informative iff below .25: {pred < 0.25}")
    expect(worst < 1e-6, f"m09: the unified formula matches numerically maximized ideal points in 19 combinations (max deviation {worst:.1e}); n=2: b0(1-theta)/(1+theta), infinite at theta=-1")
    print("(f) s5_misc (Math-Opus reviewer): third-party payoff -k y^2 (nonlinear): the gap in state units is still b0 n/(n-2)")
    def ideal(n, b0, u, k, who):
        best = None
        for i in range(-4000, 4001):
            y = u + i / 1000
            pS = -(y - u - b0) ** 2; pR = -(y - u) ** 2; pk = -k * y * y
            J_ = pS - (pR + (n - 2) * pk) / (n - 1) if who == 'S' else pR - (pS + (n - 2) * pk) / (n - 1)
            if best is None or J_ > best[0]: best = (J_, y)
        return best[1]
    okN = True
    for n in (3, 4):
        for u in (0.0, 0.5, 1.0):
            gap = ideal(n, 0.05, u, 0.3, 'S') - ideal(n, 0.05, u, 0.3, 'R')
            okN &= abs(gap * 0.7 - 0.05 * n / (n - 2)) < 1e-3
            print(f"   n={n}, u={u}: gap in y {gap:.4f}; in state units gap*(1-k) = {gap*0.7:.4f} (b0 n/(n-2) = {0.05*n/(n-2):.4f})")
    expect(okN, "s5_misc: with a nonlinear third-party term the gap in state units is b0 n/(n-2) to the grid's resolution (1e-3)")


def ext_HO():
    subblock('HO', 'safeguards, require (R1)', 'independent',
             'The margin Delta_min on the forgiving (logistic) host, three implementations; the harsher (Allee) host; R1 with limsup is necessary, not sufficient')
    # Sources (ported): planning/math-fable/f7_misc.py (D); planning/math-opus/m09_misc.py (check_safeguards, check_R1);
    # ../v6.1/reviews/scripts-v6.1-math-opus/s8_logistic_margin.py and s5_misc.py (Theorem 10.5 on the Allee host).
    rho, h = 0.05, 0.08
    def runF(Delta, emin=0.0, emax=1.0, T=1500.0, dt=0.02):
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
    print("(d) f7(D): logistic host, race share 0.99 declining at rate Delta*(e_max-e_min); transient minimum and Delta_min by floor")
    dm = {}
    for emin in (0.0, 0.1):
        vmin, Vend = runF(0.08, emin=emin)
        print(f"   e_min={emin}: Delta=.08 -> transient minimum {vmin:.4f}, long-run level {Vend:.3f} (1 - h e_min/rho = {1-h*emin/rho:.3f})")
        dm[(emin, 'min')] = vmin
        for floor in (0.2, 0.3, 0.5):
            lo, hi = 0.0, 2.0
            for _ in range(30):
                m = (lo + hi) / 2
                if runF(m, emin=emin)[0] < floor: lo = m
                else: hi = m
            dm[(emin, floor)] = hi
            print(f"      floor {floor}: Delta_min = {hi:.3f}")
    expect(abs(dm[(0.0, 'min')] - 0.1397) < 1e-4 and abs(dm[(0.0, 0.2)] - 0.108) < 1e-3 and abs(dm[(0.0, 0.3)] - 0.165) < 1e-3 and abs(dm[(0.0, 0.5)] - 0.355) < 1e-3
           and abs(dm[(0.1, 0.2)] - 0.125) < 1e-3 and abs(dm[(0.1, 0.3)] - 0.192) < 1e-3 and abs(dm[(0.1, 0.5)] - 0.414) < 1e-3,
           "f7(D): V6.1's Delta=0.08 dips to 0.1397; Delta_min = 0.108, 0.165, 0.355 for floors 0.2, 0.3, 0.5 (0.125, 0.192, 0.414 with e_min = 0.1)")
    def vmin9(Delta, emin=0.0, emax=1.0, x0=0.99, dt=0.01, T=3000.0):
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
    m9 = []
    for floor in (0.2, 0.3, 0.5):
        lo, hi = 0.0, 2.0
        for _ in range(30):
            mid = (lo + hi) / 2
            if vmin9(mid, dt=0.05) < floor: lo = mid
            else: hi = mid
        m9.append(hi)
    def vmin8(Delta, emin=0.0, emax=1.0, x0=0.99, T=2000, dt=0.02):
        x, V = x0, 1.0; m = V
        def f(x, V): return x * (1 - x) * (-Delta * (emax - emin)), V * (rho * (1 - V) - h * (emin + (emax - emin) * x))
        for _ in range(int(T / dt)):
            k1 = f(x, V); k2 = f(x + dt / 2 * k1[0], V + dt / 2 * k1[1]); k3 = f(x + dt / 2 * k2[0], V + dt / 2 * k2[1]); k4 = f(x + dt * k3[0], V + dt * k3[1])
            x += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6; V += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6; m = min(m, V)
        return m
    s8 = []
    for Vmin_ in (0.2, 0.3, 0.5):
        lo, hi = 0.0, 5.0
        for _ in range(40):
            mid = (lo + hi) / 2
            if vmin8(mid) < Vmin_: lo = mid
            else: hi = mid
        s8.append(hi)
    print(f"(e) m09 (closed-form share, own stopping rule): Delta=.08 minimum {vmin9(0.08):.4f}; Delta_min {', '.join('%.3f' % x for x in m9)}")
    print(f"    s8 (Math-Opus reviewer, replicator integrated jointly): Delta=.08 minimum {vmin8(0.08):.4f}; Delta_min {', '.join('%.3f' % x for x in s8)}")
    expect(all(abs(a - b) < 2e-3 and abs(a - c) < 2e-3 for a, b, c in zip((dm[(0.0, 0.2)], dm[(0.0, 0.3)], dm[(0.0, 0.5)]), m9, s8)),
           "three independent integrations agree on Delta_min = 0.108, 0.165, 0.355 to 0.002")
    print("(f) s5_misc (Math-Opus reviewer): minimal margin on the pointwise-harsher Allee host (e_min = 0.1); V_u is the host's own degradation threshold")
    def Vu(A, E):
        rA = rho * A / (1 - A)
        a_ = -rA / A; b_ = rA * (1 / A + 1); c_ = -rA - h * E
        disc = b_ * b_ - 4 * a_ * c_
        return min((-b_ + math.sqrt(disc)) / (2 * a_), (-b_ - math.sqrt(disc)) / (2 * a_))
    def runA(Delta, A, emin=0.1, emax=1.0, x0=0.99, V0=1.0, T=1500.0, dt=0.02):
        rA = rho * A / (1 - A)
        def f(x, V):
            E = emin + (emax - emin) * x
            return x * (1 - x) * (-Delta * (emax - emin)), V * (rA * (V / A - 1) * (1 - V) - h * E)
        x, V = x0, V0; vmin = V
        for _ in range(int(T / dt)):
            k1 = f(x, V); k2 = f(x + dt / 2 * k1[0], V + dt / 2 * k1[1]); k3 = f(x + dt / 2 * k2[0], V + dt / 2 * k2[1]); k4 = f(x + dt * k3[0], V + dt * k3[1])
            x += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6; V += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
            vmin = min(vmin, V)
            if V < 1e-6: return vmin, 0.0
        return vmin, V
    al = []
    for A in (0.05, 0.10, 0.15, 0.20, 0.25):
        lo, hi = 0.0, 3.0
        for _ in range(30):
            m = (lo + hi) / 2
            if runA(m, A)[1] < 0.01: lo = m
            else: hi = m
        al.append((A, hi, Vu(A, 0.1)))
        print(f"   A={A:.2f}: Delta_min={hi:.3f}, V_u(e_min)={Vu(A,0.1):.3f}; transient minimum at Delta_min+0.01: {runA(hi+0.01, A)[0]:.3f}")
    expect(all(a[1] < b[1] for a, b in zip(al, al[1:])) and all(dmn > 0.2 for _, dmn, _ in al),
           "s5_misc: on a host that degrades by itself below V_u the margin must keep the transient above V_u: Delta_min 0.26-0.51, rising with A, and a shortfall is permanent")
    print("(g) m09(R1): long-run average liability vs cumulative advantage")
    nu, Vmin = 1.0, 0.3; crosses = {}
    for name, adv_fn in (("tau = nu (B=0)", lambda t: 0.0), ("tau = nu - 1/(2 sqrt(t+1))", lambda t: 1 / (2 * math.sqrt(t + 1)))):
        u = math.log(1e-3 / (1 - 1e-3)); V = 1.0; t = 0.0; dt = 0.01; cross = None
        while t < 4000:
            u += dt * adv_fn(t)
            E = 1 / (1 + math.exp(-u))
            V += dt * V * (rho * (1 - V) - h * E); t += dt
            if cross is None and V < Vmin: cross = t
        crosses[name] = cross
        print(f"   {name}: race share starts at 0.001; host {'crosses the floor at t = %.0f' % cross if cross else 'stays above the floor'}")
    c2 = crosses["tau = nu - 1/(2 sqrt(t+1))"]
    expect(crosses["tau = nu (B=0)"] is None and c2 is not None and abs(c2 - 89) < 1.5,
           "m09(R1): both paths have long-run average liability nu, yet the one whose cumulative advantage grows (sqrt(t+1)-1) crosses the floor at t=89: limsup-average >= nu is necessary, not sufficient")


def ext_SH():
    subblock('SH', 'share', 'independent', 'Sharing among all n or among the n-1 others: two effective prizes, two solution concepts')
    # Sources (ported): planning/math-fable/f7_misc.py (E) (Nash intensity); planning/math-opus/m09_misc.py (check_share) (uninvadable intensity).
    n, r, c = 4, 1.0, 1.0
    def eq_intensity(payoff):
        e = 0.2
        for _ in range(300):
            br = _golden_max(lambda x: payoff(x, e), 1e-7, 1.5, it=120); en = 0.5 * e + 0.5 * br
            if abs(en - e) < 1e-13: e = en; break
            e = en
        return e
    print("(f) f7(E): Nash intensity (n=4, r=1, c=1, Om_e=1, Om_s=0, rho=1) vs r Om_eff (n-1)/(n^2 c)")
    okE = True
    for beta in (0.3, 0.6):
        def pay_all(x, e, beta=beta):
            w = x ** r / (x ** r + (n - 1) * e ** r); return w * (1 - beta) + beta / n - c * x
        def pay_others(x, e, beta=beta):
            w = x ** r / (x ** r + (n - 1) * e ** r); return w * (1 - beta) + (1 - w) * beta / (n - 1) - c * x
        ea = eq_intensity(pay_all); eo = eq_intensity(pay_others)
        fa = r * (1 - beta) * (n - 1) / (n * n * c); fo = r * (1 - beta * n / (n - 1)) * (n - 1) / (n * n * c)
        okE &= abs(ea - fa) < 1e-6 and abs(eo - fo) < 1e-6
        print(f"   beta={beta}: shared among all n: {ea:.5f} vs formula {fa:.5f} (Om_eff=(1-beta)Om_e); among the n-1 others: {eo:.5f} vs {fo:.5f} (Om_eff=(1-beta n/(n-1))Om_e)")
    expect(okE, "f7(E): Nash intensities 0.13125/0.11250 (beta=0.3) and 0.07500/0.03750 (beta=0.6) equal the two effective-prize formulas")
    print("(g) m09: uninvadable intensity in one field (Om_e=1, Om_s=0.5) vs r Om_eff/(n c)")
    Oe, Os = 1.0, 0.5; okU = True
    for beta in (0.3, 0.6):
        for scheme in ('n', 'n-1'):
            def rel_payoff(y, x, beta=beta, scheme=scheme):
                w = y ** r / (y ** r + (n - 1) * x ** r)
                own = w * ((1 - beta) * Oe + Os) + (beta * Oe / n if scheme == 'n' else (1 - w) * beta * Oe / (n - 1))
                wo = x ** r / (y ** r + (n - 1) * x ** r)
                oth = wo * ((1 - beta) * Oe + Os) + (beta * Oe / n if scheme == 'n' else (1 - wo) * beta * Oe / (n - 1))
                return (own - c * y) - (oth - c * x)
            def slope(x, h=1e-7): return (rel_payoff(x + h, x) - rel_payoff(x - h, x)) / (2 * h)
            lo, hi = 1e-6, 5.0
            for _ in range(200):
                mid = (lo + hi) / 2
                if slope(mid) > 0: lo = mid
                else: hi = mid
            x = (lo + hi) / 2
            gridok = max(rel_payoff(x * k / 100, x) for k in range(1, 400)) <= 1e-12
            Oeff = ((1 - beta) * Oe + Os) if scheme == 'n' else ((1 - beta * n / (n - 1)) * Oe + Os)
            okU &= gridok and abs(x - r * Oeff / (n * c)) < 1e-6
            print(f"   beta={beta} shared among {scheme:3s}: uninvadable intensity {x:.5f}; r Om_eff/(n c) = {r*Oeff/(n*c):.5f} (Om_eff = {Oeff:.4f}); no mutant gains on a grid: {gridok}")
    expect(okU, "m09: uninvadable intensities 0.300, 0.275, 0.225, 0.175 equal r Om_eff/(n c) under both conventions (the n vs n-1 distinction of Props 3.5(4) and 5.7)")


def ext_SM():
    subblock('SM', 'opaquecorr, homeostasis, topology, fallback; thrrep (S3)', 'independent; (13) derived; in (15) the branch slope derived; (16) derived',
             'Proposition 6.8: summable vs not; 6.11(3) at every t; 6.9 topology numbers; Lemma 8.2 coupling by exact DP; S6.2(2) two roots; S3.1 reversion cutoffs')
    # Sources (ported): planning/math-fable/f7_misc.py (B),(C),(G); planning/math-opus/m09_misc.py (check_opaque, check_absorb, check_topology);
    # ../v6.1/reviews/scripts-v6.1-math-opus/s5_misc.py (Lemma 8.2).
    q0 = 0.1
    def surv(resid, T):
        s = 1.0
        for t in range(T): s *= (1 - resid(t))
        return s
    r1 = lambda t: q0 * (1 - 0.99) + 2.0 ** (-(t + 2))
    r2 = lambda t: q0 * 2.0 ** (-(t + 1)) + 2.0 ** (-(t + 2))
    s_from1 = 1.0
    for t in range(1, 201): s_from1 *= (1 - (q0 * 0.01 + 2.0 ** (-(t + 2))))
    a200, a20k, b200, b20k = surv(r1, 200), surv(r1, 20000), surv(r2, 200), surv(r2, 20000)
    print(f"(11) f7(B): printed example (c_b=.99 fixed): survival to 200 {a200:.3f} from t=0 ({s_from1:.3f} from t=1), to 20,000 {a20k:.2e}; "
          f"Fable's summable example c_b,t = 1-2^-(t+1): {b200:.4f} at 200, {b20k:.4f} at 20,000")
    def survO(T, cb, qc, t0):
        S = 1.0
        for t in range(t0, T + t0): S *= 1 - (q0 * (1 - cb(t)) + qc(t))
        return S
    qc = lambda t: 2.0 ** (-(t + 2)); rising = lambda t: 1 - 2.0 ** (-t)
    o200, o20k = survO(200, rising, qc, 1), survO(20000, rising, qc, 1)
    print(f"     m09: Opus's summable example c_b,t = 1-2^-t from t=1: {o200:.4f} at 200, {o20k:.4f} at 20,000 (without the corrector {(1-q0)**200:.1e} at 200)")
    expect(abs(a200 - 0.473) < 5e-4 and abs(s_from1 - 0.630) < 5e-4 and a20k < 1e-8 and abs(b200 - b20k) < 1e-9 and abs(b200 - 0.5101) < 1e-4 and abs(o200 - 0.6888) < 1e-4 and abs(o200 - o20k) < 1e-9,
           "6.8: V6.1's example is not summable (0.473 from t=0, 0.630 from t=1, 1.2e-9 by 20,000); both memos' replacement examples are (0.5101 Fable, 0.6888 Opus; different examples)")
    # v6.2 verification round (FIXES-v6.2-verify, M2-03): the example is shifted by one period, s_t=2^(t+1), dpsi_t=2^-(t+1),
    # so that every hazard is below one ({{nonsum}}); V6.2's printed "exact 0.1836" was the sum of the hazards, not the risk.
    print("(12) f7(C) and m09: Proposition 6.11(3), n=3, L_e=L_c=1, psi0=0, s_t=2^(t+1), dpsi_t=2^-(t+1) (shifted by one period)")
    okC = True; mgs12 = []
    for t in range(0, 41):
        s = 2.0 ** (t + 1); dp = 2.0 ** (-(t + 1))
        def obj(iota, others=1.0, s=s, dp=dp):
            w = (1 + s * iota) / (1 + s * iota + 2 * (1 + s * others))
            Q = (1 - dp * iota) * (1 - dp * others) ** 2
            return -(1 - w) - (1 - Q)
        best = max(obj(k / 200) for k in range(201)); at1 = obj(1.0)
        mg = 2 * s / (9 * (1 + s)) - dp * (1 - dp) ** 2; mgs12.append(mg)
        okC &= at1 >= best - 1e-12 and mg > 0 and 1 - (1 - dp) ** 3 < 1
        if t < 8:
            print(f"   t={t}: objective at iota=1 {at1:.4f}, best on grid {best:.4f}; own marginal gain {mg:+.4f}; realized hazard n dpsi = {3*dp:.4f}, exact 1-(1-dpsi)^3 = {1-(1-dp)**3:.4f}")
    ub = sum(3 * 2.0 ** (-(t + 1)) for t in range(4, 60))
    hsum = sum(1 - (1 - 2.0 ** (-(t + 1))) ** 3 for t in range(4, 200))
    surv4 = 1.0
    for t in range(4, 200): surv4 *= (1 - 2.0 ** (-(t + 1))) ** 3
    surv0 = 1.0
    for t in range(0, 200): surv0 *= (1 - 2.0 ** (-(t + 1))) ** 3
    ex = 1 - surv4
    print(f"   full delegation a best response on the grid at t=0..40: {okC}; realized risk from t=4: union bound {ub:.4f} = 3/16; sum of hazards {hsum:.4f}; exact 1-prod {ex:.4f}; survival from the start {surv0:.4f}")
    expect(okC and abs(ub - 3 / 16) < 1e-12 and abs(hsum - 0.1836) < 5e-5 and abs(ex - 0.1726) < 5e-5 and ex <= hsum <= 3 / 16 and abs(surv0 - 0.0241) < 5e-5
           and [round(m, 3) for m in mgs12[:5]] == [0.023, 0.037, 0.102, 0.154, 0.186],
           "6.11(3), shifted: full delegation is an equilibrium at every t (marginal gain +0.023, +0.037, +0.102, +0.154, +0.186, ...), every hazard below one, survival from the start 0.0241; realized risk from t=4 exactly 0.1726 (sum of hazards 0.1836, union bound 3/16)")
    f, k = 0.9, 6
    vals = (f ** k, 1 - (1 - f ** k) ** k, (1 - (1 - f ** k) ** k) * 0.95, (1 - (1 - f) ** 2) ** k, (1 - (1 - f) ** 3) ** k)
    print(f"(13) [derived] 6.9 topology (f=.9, k=6): serial {vals[0]:.3f}; independent across the gap {vals[1]:.3f}; with common cause .05 {vals[2]:.3f}; layered m=2 {vals[3]:.3f}, m=3 {vals[4]:.3f}; "
          + "blind spot catch " + ", ".join(f"rho_cc={r_}: {(1-r_)*(1-0.1**6):.3f}" for r_ in (0, .05, .3)))
    print("(14) s5_misc (Math-Opus reviewer): Lemma 8.2 by exact DP over (world, active, A survived, C survived) with a common uniform")
    import collections
    def exact(H):
        hz = {'C': {'G': 0.01, 'B': 0.05}, 'A': {'G': 0.005, 'B': 0.02}, 'dis': {'G': 0.01, 'B': 0.2}}
        dist = collections.defaultdict(float); dist[('G', True, True, True)] = 1.0
        for t in range(H):
            nd = collections.defaultdict(float)
            for (w, act, sa, sc), pr in dist.items():
                hA = hz['A'][w] if act else hz['C'][w]; hC = hz['C'][w]
                lo_ = min(hA, hC); hi_ = max(hA, hC)
                for pu, fa, fc in ((lo_, True, True), (hi_ - lo_, hA > hC, hC > hA), (1 - hi_, False, False)):
                    if pu <= 0: continue
                    sa2 = sa and not fa; sc2 = sc and not fc
                    for pdis, act2 in ((hz['dis'][w] if act else 0.0, False), (1 - (hz['dis'][w] if act else 0.0), act)):
                        if pdis <= 0: continue
                        for w2, pw in ((w, 0.9), ('B' if w == 'G' else 'G', 0.1)):
                            nd[(w2, act2, sa2, sc2)] += pr * pu * pdis * pw
            dist = nd
        SA = sum(p for (w, a, sa, sc), p in dist.items() if sa); SC = sum(p for (w, a, sa, sc), p in dist.items() if sc)
        return SA, SC
    okL = True
    for H in (10, 30, 100):
        SA, SC = exact(H); okL &= SA >= SC - 1e-12
        print(f"   H={H}: S^A={SA:.4f} >= S^C={SC:.4f}: {SA >= SC - 1e-12}")
    expect(okL, "Lemma 8.2: with dissolution more likely in the bad state, the coupled arrangement still survives at least as well at H = 10, 30, 100")
    # ---------------------------------------------------------------- (15), (16): v6.2 additions (merge notes U06 s4, U03 s4)
    # (15) Source (ported): ../v5/checks_v5.py block HO (sym_eq_roots), which S6 cites through --legacy; the merge of U06
    # recomputed it independently. Interior roots of the first-order condition by sign change and bisection; each root
    # and the corner kept only if it is a global best response on a grid; then the branch slope of S6.2(2) against a
    # finite difference of the computed roots. Independent (grid best response); the slope comparison is [derived].
    print("(15) Proposition S6.2(2) (homeostasis): n=2, s=100, L_e=0.5, L_c=1, psi0=0.01; symmetric equilibria by grid best response")
    def ho_util(i_self, i_other, n, s, Le, Lc, p0, dpsi):
        sig_s, sig_o = 1 + s * i_self, 1 + s * i_other
        w = sig_s / (sig_s + (n - 1) * sig_o)
        Q = (1 - p0 - dpsi * i_self) * (1 - p0 - dpsi * i_other) ** (n - 1)
        return -Le * (1 - w) - Lc * (1 - Q)
    def ho_bisect(f, lo, hi, it=200):
        flo = f(lo)
        for _ in range(it):
            mid = (lo + hi) / 2; fm = f(mid)
            if (fm > 0) == (flo > 0): lo, flo = mid, fm
            else: hi = mid
        return (lo + hi) / 2
    def ho_eqs(n, s, Le, Lc, p0, dpsi, N=4000):
        F = lambda i: Le * s * (n - 1) / (n * n * (1 + s * i)) - Lc * dpsi * (1 - p0 - dpsi * i) ** (n - 1)
        grid = [k / N for k in range(N + 1)]; roots = []
        for a_, b_ in zip(grid, grid[1:]):
            if F(a_) == 0: roots.append(a_)
            elif (F(a_) > 0) != (F(b_) > 0): roots.append(ho_bisect(F, a_, b_))
        eqs = [r_ for r_ in roots if ho_util(r_, r_, n, s, Le, Lc, p0, dpsi) >= max(ho_util(k / N, r_, n, s, Le, Lc, p0, dpsi) for k in range(N + 1)) - 1e-9]
        corner = max(ho_util(k / N, 1.0, n, s, Le, Lc, p0, dpsi) for k in range(N + 1)) <= ho_util(1.0, 1.0, n, s, Le, Lc, p0, dpsi) + 1e-12
        return roots, eqs, corner
    hoR = {}
    for dpsi in (0.9, 0.9 + 1e-4, 0.9 - 1e-4):
        hoR[dpsi] = ho_eqs(2, 100.0, 0.5, 1.0, 0.01, dpsi)
    roots, eqs, corner = hoR[0.9]
    Kh = (2 - 1) * 0.5 / (4 * 1.0); bs = 0.9 / 100.0
    resid = max(abs((0.9 * r_ + bs) * (1 - 0.01 - 0.9 * r_) - Kh) for r_ in roots)
    print(f"   Delta psi=0.9: interior roots iota = {', '.join(f'{r_:.6f}' for r_ in roots)}; global best responses: {', '.join(f'{r_:.6f}' for r_ in eqs)}; corner iota=1 an equilibrium: {corner}; "
          f"realized hazard {', '.join(f'{1-(1-0.01-0.9*r_)**2:.4f}' for r_ in eqs)}; max residual of (x+b_s)(1-psi0-x)^(n-1) = K_h: {resid:.1e}")
    slopes = []
    for j in range(2):
        xp = (0.9 + 1e-4) * hoR[0.9 + 1e-4][0][j]; xm = (0.9 - 1e-4) * hoR[0.9 - 1e-4][0][j]; x = 0.9 * roots[j]
        fd = (xp - xm) / 2e-4; fo = -(1 - 0.01 - x) / (100.0 * (1 - 0.01 - 2 * x - bs))
        slopes.append((fd, fo)); print(f"   [derived] branch {j+1} (x = {x:.4f}): dx/dDelta psi by finite difference {fd:+.5f}, by S6.2(2) {fo:+.5f}")
    expect(len(roots) == 2 and eqs == roots and corner and abs(roots[0] - 0.153) < 5e-4 and abs(roots[1] - 0.937) < 5e-4 and resid < 1e-12
           and all(abs(fd - fo) < 1e-3 * abs(fo) for fd, fo in slopes) and slopes[0][1] < 0 < slopes[1][1],
           "S6.2(2): two interior roots, iota = 0.153 and 0.937, both global best responses, with the corner also an equilibrium; the branch slope formula holds and its sign differs between branches")
    # (16) thrrep cutoffs (Remark S3.1), U03 merge note: from the stage payoffs of Proposition 3.7 (`wow`; pi_k = nu e_k +
    # g_V(1 - h_V E/(n rho)), Upsilon = g_V h_V/(rho nu) = 3, h_V ebar < rho); the discount cutoff by bisection on discounted streams (cooperate forever vs deviate once, then reversion to
    # full depletion), not by the formula. [derived: the stage payoffs are the model's; checks the arithmetic of 0.11/0.47/0.95]
    print("(16) Remark S3.1 (thrrep): Upsilon=3, n=4; reversion cutoff delta by bisection on discounted streams vs (w-U/n)/(w-U/n+U-1)")
    nu, eb, gV, hV, rho, n = 1.0, 0.5, 3.0, 1.0, 1.0, 4
    Ups = gV * hV / (rho * nu)
    def u_k(e, k, lam):
        E = sum(e); pis = [nu * x + gV * (1 - hV * E / (n * rho)) for x in e]
        return pis[k] + lam * (pis[k] - sum(pis) / n)
    okTR = True; cuts = []
    for lam in (0.0, 2.0, 50.0):
        R = u_k([0.0] * n, 0, lam); T = u_k([eb] + [0.0] * (n - 1), 0, lam); P = u_k([eb] * n, 0, lam)
        dep_dominant = all(u_k([eb] + list(o), 0, lam) > u_k([0.0] + list(o), 0, lam) for o in itertools.product((0.0, eb), repeat=n - 1))
        lo, hi = 0.0, 1.0
        for _ in range(80):
            dl = (lo + hi) / 2
            if R / (1 - dl) >= T + dl * P / (1 - dl): hi = dl
            else: lo = dl
        w = 1 + lam * (n - 1) / n; form = (w - Ups / n) / (w - Ups / n + Ups - 1)
        cuts.append(hi); okTR &= dep_dominant and abs(hi - form) < 1e-12
        print(f"   lambda={lam:g}: R={R:.4f}, T={T:.4f}, P={P:.4f}; depletion dominant in the stage game: {dep_dominant}; cutoff by bisection {hi:.4f}, formula {form:.4f}")
    expect(okTR and [round(c_, 2) for c_ in cuts] == [0.11, 0.47, 0.95],
           "thrrep: joint restraint is sustained by reversion iff delta >= 0.11, 0.47, 0.95 at lambda = 0, 2, 50 (Upsilon=3, n=4); reversion to depletion is credible (dominant)")


# =====================================================================================================================
# The verification round of V6.2 (reviews/FIXES-v6.2-verify.md): one block for the numbers that its fixes added.
# =====================================================================================================================
def check_VF():
    block('VF', 'loopgain, tdec, compound, relsel, load, detectlink, jointscissors, scissors, talk, nearlock, preventown, readrule, dwell (S2-S11)',
          'independent: direct computation (Nash iteration, period-by-period sums, simulation, numerical Jacobian, grid maximization, Monte Carlo); (b) closed forms checked against the sums',
          'Numbers added by the fixes of the V6.2 verification round, each checked by direct computation')
    # ---------------------------------------------------------------- (a) loopgain(4): r^pr along a relative shift (math-I M2)
    print("(a) Proposition 2.2(4): r^pr along a relative shift against a move of the actor's stock alone; static contest p_i = X_i e_i / sum X_k e_k, cost e/X^s, rivals at their Nash efforts at the shifted state")
    def br(i, X, e, s):
        R = sum(X[k] * e[k] for k in range(len(X)) if k != i)
        v = math.sqrt(X[i] ** (1 + s) * R) - R
        return max(v / X[i], 0.0)
    def nash(X, s, iters=6000):
        n = len(X); e = [0.1] * n
        for _ in range(iters):
            new = [br(k, X, e, s) for k in range(n)]
            e = [0.7 * a + 0.3 * b for a, b in zip(e, new)]
        return e
    def share0(X, e):
        t = sum(a * b for a, b in zip(X, e)); return X[0] * e[0] / t
    res = {}
    for (n, s) in ((2, 0.0), (3, 0.0), (2, 1.0)):
        e0 = nash([1.0] * n, s)[0]; h = 1e-4
        def deriv(shift):
            out = []
            for sg in (1, -1):
                X = shift(sg * h); e = nash(X, s); e[0] = e0; out.append(share0(X, e))
            return (out[0] - out[1]) / (2 * h)
        own = n * n / (n - 1) * deriv(lambda y: [1 + y] + [1.0] * (n - 1))
        rel = n * deriv(lambda y: [1 + y] + [1 - y / (n - 1)] * (n - 1))
        com = deriv(lambda y: [1 + y] * n)
        res[(n, s)] = (own, rel, com)
        print(f"   n={n}, s={s}: r^pr/r own-only {own:.4f}, along the relative shift {rel:.4f}; a common shift moves p_i by {com:+.4f} per unit")
    expect(abs(res[(2, 0.0)][0] - res[(2, 0.0)][1]) < 1e-4 and abs(res[(3, 0.0)][0] - res[(3, 0.0)][1]) < 1e-4 and abs(res[(3, 0.0)][1] - 4 / 3) < 1e-3
           and abs(res[(2, 1.0)][0] - 1.0) < 1e-3 and abs(res[(2, 1.0)][1] - 1.5) < 1e-3 and abs(res[(2, 1.0)][2] + 0.25) < 1e-3,
           "loopgain(4): at s=0 the own-only and relative derivatives agree (2(n-1)/n); at n=2, s=1 they are 1.00 and 1.50, a common shift moving p_i by -0.25: r^pr must be read along the relative shift")
    # ---------------------------------------------------------------- (b) detectlink: exact timings (math-I M1)
    print("(b) Remark 5.5: the one-period reduction against two exact timings; closed forms against period-by-period sums")
    rnd = random.Random(5); worstA = worstB = 0.0
    for _ in range(20000):
        d = rnd.uniform(0.5, 0.99); lam = rnd.uniform(0.01, 0.9); T = rnd.randint(1, 30)
        C = rnd.uniform(-1, 2); v = C - rnd.uniform(0, 2); D = C + rnd.uniform(-1, 3); g = rnd.uniform(0, 3)
        V = (1 - d) * (C + g); surv = 1.0
        for t in range(1, T + 1):
            V += d ** t * surv * lam * v; surv *= (1 - lam)
            V += d ** t * surv * ((1 - d) * C if t < T else D)
        a = d * (1 - lam)
        worstA = max(worstA, abs((V - C) - ((1 - d) * g + a ** T * (D - C) - lam * d * (1 - a ** T) / (1 - a) * (C - v))))
        pd = (1 - lam) ** T; V = (1 - d) * (C + g)
        for t in range(1, T): V += d ** t * (1 - d) * v
        V += d ** T * (pd * D + (1 - pd) * v)
        worstB = max(worstB, abs((V - C) - ((1 - d) * g + d ** T * pd * (D - v) - d * (C - v))))
    lam10 = 1 - math.exp(-0.1); w_reduced, w_A = 0.9, lam10 * 0.9 / (1 - 0.9 * (1 - lam10))
    print(f"   20,000 random settings: largest |closed form - period sum| {worstA:.1e} under (A), {worstB:.1e} under (B); sanction weight with no breakout, clock of mean 10, delta=0.9: reduction {w_reduced}, (A) {w_A:.3f}")
    expect(worstA < 1e-12 and worstB < 1e-12 and abs(w_A - 0.461) < 5e-4,
           "detectlink: the closed forms of timings (A) and (B) equal the period-by-period values; under (A) a slow clock weakens the sanction even without breakout (0.461 against 0.9)")
    # the joint model of Remark S5.2 (as in JX (f)), under the reduction and the two timings
    N_, DELTA = 4, 0.9
    A_ = 1.0 * (1.0 - 0.2) - 0.3; BB = 1.0 * (1.0 / 3 + 0.2); KK = 0.3 + 4 * 0.2
    gain_obj = lambda th: A_ - th * BB
    race_obj = lambda th: -KK * (1 + th)
    def theta_gamma(th0, Gd):
        return -1.0 if Gd >= 1 else (N_ * th0 - (N_ - 1) * (1 + th0) * Gd) / (N_ - (1 + th0) * Gd)
    tcache = {}
    def tdec_nl(omega, r, dK, df, gap0=0.05, gapbar=0.5, tmax=5000):
        key = (omega, r, dK, df)
        if key in tcache: return tcache[key]
        k0 = (1 - omega) / (N_ * omega); Kst = (1.0 / N_ + k0) / dK
        Kv = [Kst * (1 + gap0)] + [Kst] * (N_ - 1); res_ = None
        for t in range(1, tmax + 1):
            w = [k ** r for k in Kv]; S = sum(w); mean = sum(Kv) / N_
            Kv = [(1 - dK) * Kv[i] + w[i] / S + k0 - df * (Kv[i] - mean) for i in range(N_)]
            if Kv[0] / Kv[1] - 1 >= gapbar: res_ = t; break
        tcache[key] = res_; return res_
    def holds(omega, P, timing='reduced', arm='joint'):
        r, dK, df = P['r'], P['dK'], P['df']
        Gd = r * omega * DELTA * dK / (1 - DELTA * (1 - dK - df))
        th = theta_gamma(P['th0'], Gd); T = tdec_nl(omega, r, dK, df)
        if arm == 'breakout': th = P['th0']
        pd = 0.0 if T is None else math.exp(-T / P['tau'])
        if arm == 'objective': pd = 0.0; T = None
        g, v, C, D, dl = gain_obj(th), race_obj(th), 0.0, P['DC'], DELTA
        if timing == 'reduced': return (1 - dl) * g + dl * pd * (D - C) <= dl * (1 - pd) * (C - v) + 1e-12
        lam = 1 - math.exp(-1 / P['tau']); a = dl * (1 - lam)
        if T is None:
            return (1 - dl) * g <= (lam * dl / (1 - a) if timing == 'A' else dl) * (C - v) + 1e-12
        if timing == 'A': return (1 - dl) * g + a ** T * (D - C) <= lam * dl * (1 - a ** T) / (1 - a) * (C - v) + 1e-12
        return (1 - dl) * g + dl ** T * pd * (D - v) <= dl * (C - v) + 1e-12
    def wstar(P, timing='reduced', arm='joint', lo=0.01, hi=0.999):
        if not holds(lo, P, timing, arm): return lo
        if holds(hi, P, timing, arm): return None
        for _ in range(50):
            m = (lo + hi) / 2
            if holds(m, P, timing, arm): lo = m
            else: hi = m
        return lo
    BASE = dict(r=3.0, dK=0.2, df=0.05, th0=0.0, tau=10.0, DC=0.0)
    thr = {(DC, tm): wstar(dict(BASE, DC=DC), tm) for DC in (0.0, 0.5) for tm in ('reduced', 'A', 'B')}
    print("   joint threshold (i) of Remark S5.2: " + "; ".join(f"D-C={k[0]}, {k[1]}: {v:.3f}" for k, v in thr.items()))
    expect([round(thr[(0.0, t)], 3) for t in ('reduced', 'A', 'B')] == [0.551, 0.514, 0.556] and [round(thr[(0.5, t)], 3) for t in ('reduced', 'A', 'B')] == [0.536, 0.514, 0.554],
           "jointscissors: the reduction's thresholds 0.551 (D=C) and 0.536 (D-C=0.5) become 0.514 and 0.514 under timing (A), 0.556 and 0.554 under timing (B)")
    # ---------------------------------------------------------------- (c) jointscissors: the 96 settings and the sweep over r (coldread M5; math-I M9)
    print("(c) Remark S5.2: how far the joint threshold lies below the objective blade alone over the 96 settings; the sweep over decisiveness")
    gaps = []
    for DC in (0.0, 0.5):
        for tau in (5.0, 10.0, 20.0, 40.0):
            for df in (0.0, 0.05, 0.1):
                for th0 in (0.0, 0.4):
                    for r in (2.0, 3.0):
                        P = dict(BASE, tau=tau, df=df, th0=th0, r=r, DC=DC)
                        w = wstar(P); wo = wstar(P, arm='objective')
                        if w is not None and wo is not None: gaps.append((wo - w, tau, DC))
    big = [g_ for g_ in gaps if g_[0] > 0.05]
    print(f"   {len(gaps)} settings close; the joint threshold lies more than 0.05 below the objective blade's in {len(big)}, by at most {max(g_[0] for g_ in gaps):.3f}; clocks of those: {sorted(set(g_[1] for g_ in big))}; D-C=0.5 in {sum(g_[2] == 0.5 for g_ in big)}")
    expect(len(gaps) == 96 and len(big) == 26 and 0.13 <= max(g_[0] for g_ in gaps) < 0.135 and set(g_[1] for g_ in big) == {20.0, 40.0} and sum(g_[2] == 0.5 for g_ in big) >= 20,
           "jointscissors: in 26 of 96 settings, all with a slow clock (20 or 40 periods) and mostly at D-C=0.5, detection speed moves the threshold by 0.05 to 0.13")
    sw = {}
    for r in (1.0, 1.5, 1.7):
        for df in (0.0, 0.05, 0.1):
            sw[(r, df)] = wstar(dict(BASE, r=r, df=df))
    print("   sweep: " + "; ".join(f"r={k[0]}, df={k[1]}: {'never' if v is None else f'{v:.3f}'}" for k, v in sw.items()))
    expect(all(sw[(1.0, df)] is None for df in (0.0, 0.05, 0.1)) and sw[(1.5, 0.0)] is not None and abs(sw[(1.5, 0.0)] - 0.95) < 0.005
           and sw[(1.5, 0.05)] is None and sw[(1.5, 0.1)] is None and abs(sw[(1.7, 0.05)] - 0.975) < 0.001,
           "jointscissors: at r=1 the blades never close (df 0 to 0.1); at r=1.5 only without diffusion, near 0.95; at r=1.7 with df=0.05 at 0.975")
    # ---------------------------------------------------------------- (d) scissors pivot: level channel (math-I M3)
    print("(d) Proposition 5.17, the pivot: scaling stakes and provision together, numerical Jacobian of the relative deviation (n=2, d=0.2, no diffusion)")
    def gamma_num(sig, Om, k0, d=0.2, n=2):
        lo, hi = 1e-9, 1e6
        f = lambda X: (1 - d) * X + Om / n + k0 - X
        Xs = (Om / n + k0) / d
        def step(X):
            s_ = [sig(x) for x in X]; m = max(s_); e = [math.exp(t - m) for t in s_]; Z = sum(e)
            return [(1 - d) * X[i] + Om * e[i] / Z + k0 for i in range(n)]
        h = 1e-6 * Xs
        Y = step([Xs + h, Xs - h]); lamb = (Y[0] - Y[1]) / (2 * h)
        return (lamb - 1) / d + 1
    lev = [gamma_num(lambda x: 0.5 * x, 1.0 * c, 0.1 * c) for c in (1, 2, 4)]
    rat = [gamma_num(lambda x: 3.0 * math.log(x), 1.0 * c, 0.1 * c) for c in (1, 2, 4)]
    print(f"   level channel (strength a*X): Gamma at scale 1, 2, 4: {', '.join(f'{x:.4f}' for x in lev)}; ratio channel (strength r ln X): {', '.join(f'{x:.4f}' for x in rat)}")
    expect(abs(lev[1] / lev[0] - 2) < 1e-4 and abs(lev[2] / lev[0] - 4) < 1e-4 and max(rat) - min(rat) < 1e-4,
           "scissors: provision that keeps pace with the stakes holds the gain still in a ratio channel, while in a linear level channel scaling both by 2 and 4 scales Gamma by 2 and 4")
    # ---------------------------------------------------------------- (e) tdec: the gap measure and the number of carriers (math-I M7)
    print("(e) Remark S2.1: the diffusion example (Gamma=1.5, d=df=0.05, r=3) under two gap measures and with four carriers")
    def run_gap(n, X, T=10000, r=3.0, d=0.05, df=0.05, kap=0.5):
        out = {}
        for t in range(1, T + 1):
            w = [x ** r for x in X]; W = sum(w); mean = sum(X) / n
            X = [(1 - d) * x + kap * wi / W - df * (x - mean) for x, wi in zip(X, w)]
            if 'mean' not in out and (X[0] - mean) / mean >= 0.5: out['mean'] = t
            if 'other' not in out and X[0] / X[1] - 1 >= 0.5: out['other'] = t
        out['fmean'] = (X[0] - sum(X) / n) / (sum(X) / n); out['fother'] = X[0] / X[1] - 1
        return out
    Xs2 = (0.5 / 2) / 0.05; Xs4 = (0.5 / 4) / 0.05
    g2 = run_gap(2, [Xs2 * 1.01, Xs2 * 0.99]); g2o = run_gap(2, [Xs2 * 1.01, Xs2]); g4 = run_gap(4, [Xs4 * 1.01] + [Xs4] * 3)
    print(f"   n=2 from (1.01, 0.99): excess over the mean settles at {g2['fmean']:.4f}, never 50%: {'mean' not in g2}; n=2, leader 1% above the other: excess over the other reaches 50% at {g2o.get('other')}, settles at {g2o['fother']:.3f}; n=4, leader 1% above the others: excess over the mean reaches 50% at {g4.get('mean')}")
    expect('mean' not in g2 and abs(g2['fmean'] - 0.4472) < 1e-4 and g2o.get('other') == 80 and abs(g2o['fother'] - 1.618) < 1e-3 and g4.get('mean') == 77,
           "tdec: the stall at 0.447 holds for two carriers measured against their mean; against the other carrier the gap reaches 50% at period 80, and with four carriers the excess over the mean reaches it at 77")
    # ---------------------------------------------------------------- (f) compound(2)(i): the two cases at the cap K* with diffusion (math-I M8)
    print("(f) Proposition 2.3(2)(i) at a cap equal to K* with diffusion, every carrier moving: the two first-order cases")
    rr = random.Random(23); c1 = c2 = ok1 = ok2 = 0
    for _ in range(300):
        n = rr.choice([2, 3, 4, 6]); r = rr.uniform(0.5, 4); d = rr.uniform(0.05, 0.4); df = rr.uniform(0.005, 0.3)
        beta = rr.choice([0, 0, rr.uniform(0, 0.3)]); k0 = rr.choice([0, 0, rr.uniform(0, 0.2)])
        if d + df > 1: continue
        Ks = (1.0 / n + k0) / d; om = 1.0 / (1.0 + n * k0); G0 = (1 - beta) * r * om
        if abs(df - d * G0) < 1e-3 * d: continue
        X = [Ks * (1 - 1e-4)] + [Ks] * (n - 1); lead_min = Ks
        for t in range(6000):
            w = [x ** r for x in X]; W = sum(w); mean = sum(X) / n
            X = [min(Ks, (1 - d) * x + ((1 - beta) * wi / W + beta / n) + k0 - df * (x - mean)) for x, wi in zip(X, w)]
            if t < 200: lead_min = min(lead_min, min(X[1:]))
        if df < d * G0:
            c1 += 1; ok1 += lead_min > Ks * (1 - 1e-9) and ((G0 * (n - 1) / n < 1 + df * (n - 1) / (n * d)) == (X[0] > Ks * (1 - 2e-4)))
        else:
            G = G0 * d / (d + df); c2 += 1; ok2 += G < G0 / (1 + G0) < 1 and X[0] > Ks * (1 - 1e-6) and min(X) > Ks * (1 - 1e-6)
    print(f"   {c1 + c2} random settings: df < d_K Gamma0 in {c1}, leaders held at the cap and (i)'s criterion right in {ok1}; df > d_K Gamma0 in {c2}, Gamma < Gamma0/(1+Gamma0) < 1 and every carrier back at K* in {ok2}")
    expect(c1 > 50 and c2 > 50 and ok1 == c1 and ok2 == c2,
           "compound(2)(i): with diffusion at a cap equal to K*, below the knife edge the leaders stay at the cap and the criterion decides; above it Gamma < 1 and all return")
    # ---------------------------------------------------------------- (g) relsel / load: payoff-monotone without a rate bound (math-II M2-01)
    print("(g) Proposition 3.4: a relative, payoff-monotone rule without a rate bound; host rho=0.05, h_V=0.08, floor 0.3, race share from 0.001, tau_eff = nu - 1/(1+t)")
    def sim_host(rate, T=2000.0, dt=0.01, x0=0.001):
        u = math.log(x0 / (1 - x0)); V = 1.0; minV = 1.0; t = 0.0; xmax = x0
        while t < T:
            dpi = 1.0 / (1 + t); u += dt * rate(dpi); x = 1 / (1 + math.exp(-u))
            V += dt * V * (0.05 * (1 - V) - 0.08 * x); minV = min(minV, V); xmax = max(xmax, x); t += dt
        return xmax, x, minV
    xc, _, vc = sim_host(lambda g_: g_ ** 3); xr_max, xr, vr = sim_host(lambda g_: g_)
    print(f"   rate (gap)^3: B(t)=ln(1+t) unbounded, race share at most {xc:.5f}, host at least {vc:.4f}; replicator: race share {xr:.3f} at t=2000, host down to {vr:.4f}")
    expect(xc < 0.0017 and vc > 0.99 and xr > 0.5 and abs(vr - 0.017) < 0.002,
           "relsel: payoff-monotonicity alone does not carry Proposition 3.4's second sentence (share stays below 0.0017, host above 0.99), while replicator dynamics on the same path take the host to 0.017")
    # ---------------------------------------------------------------- (h) talk: quadratic third parties (math-I M6)
    print("(h) Proposition 5.16: third-party payoffs summing to -k y^2: curvature, ideal points and the gap in units of the state")
    def ideal(J):
        lo, hi = -50.0, 50.0
        for _ in range(200):
            m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
            if J(m1) < J(m2): lo = m1
            else: hi = m2
        return (lo + hi) / 2
    okT = True
    for (n, th, k, b0) in ((3, -1.0, 0.5, 0.05), (4, -0.5, 2.0, 0.08), (6, 0.5, 1.0, 0.1), (3, -0.5, 0.8, 0.05)):
        c_ = th / (n - 1)
        def JS(y, u): return -(y - u - b0) ** 2 + c_ * (-(y - u) ** 2 - k * y * y)
        def JR(y, u): return -(y - u) ** 2 + c_ * (-(y - u - b0) ** 2 - k * y * y)
        curv = 1 + c_ + c_ * k
        yS0, yR0, yR1 = ideal(lambda y: JS(y, 0.0)), ideal(lambda y: JR(y, 0.0)), ideal(lambda y: JR(y, 1.0))
        slope = yR1 - yR0; gap = (yS0 - yR0) / slope
        want = b0 * (n - 1 - th) / (n - 1 + th)
        okT &= curv > 0 and abs(gap - want) < 1e-6 and abs(slope - (n - 1 + th) / (n - 1 + th * (1 + k))) < 1e-6
        print(f"   n={n} theta={th} k={k}: n-1+theta(1+k) = {(n-1)*curv:.3f}; gap in units of the state {gap:.6f}, b0(n-1-theta)/(n-1+theta) = {want:.6f}")
    nonconc = [(n, th, k) for (n, th, k) in ((3, -1.0, 1.0), (3, -1.0, 1.5)) if n - 1 + th * (1 + k) <= 0]
    expect(okT and len(nonconc) == 2, "talk: with quadratic third parties the gap in units of the state is unchanged where n-1+theta(1+k) > 0; at n=3, theta=-1 concavity fails from k=1")
    # ---------------------------------------------------------------- (i) nearlock: the binding profile for a given n (math-II M2-09)
    print("(i) Remark S6.1: for a given n the binding profile is all others delegating at p=1")
    s_ = 2.0; facs = {}
    for n in (2, 3, 10, 100):
        ratios = [(1 + s_) * (k * s_ + n) / ((k + 1) * s_ + n) for k in range(n)]
        facs[n] = (max(ratios), ratios.index(max(ratios)))
    print("   s=2: " + "; ".join(f"n={n}: worst factor {v[0]:.3f} at k={v[1]}" for n, v in facs.items()) + f"; uniform bound 1+s = {1+s_}")
    expect(all(facs[n][1] == n - 1 for n in facs) and [round(facs[n][0], 2) for n in (2, 3, 10, 100)] == [2.0, 2.33, 2.8, 2.98],
           "nearlock: the worst factor is 1+(n-1)s/n, at k=n-1: 2.0, 2.33, 2.8, 2.98 for n=2, 3, 10, 100 at s=2, against the uniform 3")
    # ---------------------------------------------------------------- (j) preventown (math-II M2-07)
    bnd = lambda S, P, R, sP: 1 - max(S, P) / (sP * R + (1 - sP) * P)
    b1, b2 = bnd(0.5, 0.4, 0.9, 0.5), bnd(0.5, 0.3, 0.9, 0.5)
    prop = [bnd(0.5 * lam, 0.4 * lam, 0.9, 0.5) for lam in (1.0, 0.75, 0.5, 0.25, 0.1)]
    print(f"(j) Proposition 8.5(1): bound {b1:.4f} at Phi^P=0.4 and {b2:.4f} at 0.3 (Phi^S=0.5, Phi^R=0.9, s_P=0.5); proportional falls: {', '.join(f'{x:.3f}' for x in prop)}")
    expect(abs(b1 - 0.2308) < 1e-4 and abs(b2 - 0.1667) < 1e-4 and all(a < b for a, b in zip(prop, prop[1:])),
           "preventown: lowering Phi^P alone can lower the bound (0.231 to 0.167); falling in proportion it rises")
    # ---------------------------------------------------------------- (k) readrule: the indifference zone and unknown noise (math-II M2-14)
    print("(k) Remark S11.3(2): SPRT between levels 0 and 1, a=0.01, b=0.05/7; a met dimension inside the indifference zone, and a test that assumes the wrong noise")
    aq, bq = 0.01, 0.05 / 7; Aup, Blo = math.log((1 - bq) / aq), math.log(bq / (1 - aq))
    def sprt(mu, sig_true, sig_assumed, rng):
        L = 0.0
        while True:
            x = rng.gauss(mu, sig_true); L += (x - 0.5) / sig_assumed ** 2
            if L >= Aup: return 'met'
            if L <= Blo: return 'unmet'
    rg = random.Random(31); M = 20000
    held = sum(sprt(0.75, 1.0, 1.0, rg) == 'unmet' for _ in range(M)) / M
    falsemet = sum(sprt(0.0, 2.0, 1.0, rg) == 'met' for _ in range(M)) / M
    held1 = sum(sprt(1.0, 1.0, 1.0, rg) == 'unmet' for _ in range(M)) / M
    print(f"   true level 0.75, unit noise: held back {held:.4f} (bound {bq/(1-aq):.4f}); at the registered level 1: {held1:.4f}; true noise 2, assumed 1, level 0: declared met {falsemet:.4f} (bound {aq/(1-bq):.4f})")
    expect(0.04 < held < 0.08 and held1 <= bq / (1 - aq) + 0.003 and 0.17 < falsemet < 0.23,
           "readrule: Wald's bounds hold at the registered levels with known noise (held back at most 0.0072 at level 1), not inside the indifference zone (about 0.06 at 0.75) nor with the noise misspecified (about 0.2 against 0.0101)")
    # ---------------------------------------------------------------- (l) dwell: the depth reached without a floor (math-II M2-15)
    print("(l) Proposition S11.4: the logit's peak under insulation from x0=0.99, G=10")
    u0 = math.log(99.0); peaks = {}
    for ratio in (10.0, 1.0):          # zeta c / (epsilon d)
        best = u0; s_ = 0.0
        while s_ < 10.0:
            best = max(best, u0 + ratio * (10.0 * (1 - math.exp(-s_)) - s_)); s_ += 1e-4
        peaks[ratio] = best
    sh = {k: 1 / (1 + math.exp(v)) for k, v in peaks.items()}
    print(f"   rule-making ten times slower: peak logit {peaks[10.0]:.2f}, alternative's share {sh[10.0]:.1e}; equal speeds: {peaks[1.0]:.2f}, share {sh[1.0]:.1e}; formula u0+(zeta c/eps d)(G-1-ln G): {u0+10*(9-math.log(10)):.2f}, {u0+(9-math.log(10)):.2f}")
    expect(abs(peaks[10.0] - 71.57) < 0.01 and abs(peaks[1.0] - 11.29) < 0.01 and 5e-32 < sh[10.0] < 1e-31 and 1.0e-5 < sh[1.0] < 1.4e-5,
           "dwell: without a floor the alternative's share falls to about 8e-32 at slow rule-making (1.2e-5 at equal speeds), extinct in any finite population")


check_CI = (lambda base: (lambda: (base(), ext_CI())))(check_CI)
check_PR = (lambda base: (lambda: (base(), ext_PR())))(check_PR)
check_CS = (lambda base: (lambda: (base(), ext_CS())))(check_CS)
check_DW = (lambda base: (lambda: (base(), ext_DW())))(check_DW)
check_CR = (lambda base: (lambda: (base(), ext_CR())))(check_CR)
check_TK = (lambda base: (lambda: (base(), ext_TK())))(check_TK)
check_HO = (lambda base: (lambda: (base(), ext_HO())))(check_HO)
check_SH = (lambda base: (lambda: (base(), ext_SH())))(check_SH)
check_SM = (lambda base: (lambda: (base(), ext_SM())))(check_SM)


# v6.1 blocks first, in their v6.1 order (CI, PR, CS, DW, CR, TK, HO, SH and SM carry their v6.2 extensions at the end of the
# same function); then the v6.2 blocks in the order of the paper's sections; VF, last, holds the numbers of the verification round.
def check_CX():
    block('CX', 'standprice, detectlink, load, certificate, readrule, dwell, frontier, onegroup, lockin', 'mixed: (A),(C),(D),(G),(H),(I) closed form; (B) identity; (E),(F) independent integration; (J) independent simulation',
          "Outside review of V6.2 (Codex, both reviews): the counterexamples behind the repairs, each asserted where the repaired text cites it")
    sig = lambda u: 1/(1+math.exp(-u)) if u >= 0 else math.exp(u)/(1+math.exp(u))
    # (A) balanced path with linear strength: the relative derivative diverges while the common one is 4/3
    stock, sens, pv, disc = 1.0, .2, 0.0, .8
    sums = {}
    for t in range(1, 31):
        pv += disc*stock*sens; sens *= .9+.2*stock; stock *= 1.1; disc *= .8; sums[t] = pv
    common = .8*.2/(1-.8*1.1)
    print(f"  (A) relative partial sums at 10, 20, 30: {sums[10]:.5f}, {sums[20]:.5f}, {sums[30]:.2f}; common {common:.5f}")
    expect(close(common, 4/3, 1e-12) and close(sums[10], 1.80051, 1e-5) and close(sums[20], 27.47743, 1e-6) and sums[30] > 1e5,
           "standprice: along a balanced path whose elasticity grows, the gains at the start certify nothing (relative sum diverges, common 4/3)")
    # (B) detection with delay: the conditional continuation values of detectlink reproduce the delayed condition
    C, D, v, g, dl, pd = 1.0, 1.5, 0.0, .3, .9, .64
    printed = (1-dl)*g + dl*(pd*(D-C) + (1-pd)*(v-C))
    actual = (1-dl)*g + pd*dl**10*(D-C) + (1-pd)*dl**9*(v-C)
    Dt, vt = C + dl**9*(D-C), C + dl**8*(v-C)
    reduced = (1-dl)*g + dl*(pd*(Dt-C) + (1-pd)*(vt-C))
    print(f"  (B) immediate {printed:.6f}, delayed {actual:.12f}, one-period reduction with conditional values {reduced:.12f}")
    expect(printed < 0 < actual and close(actual, .002105724792, 1e-9) and close(reduced, actual, 1e-12),
           "detectlink: an eventual escape probability in a next-period equation reverses deterrence; continuation values that carry the waiting restore it")
    # (C) a payoff-monotone rule that is not cumulative: raw advantage diverges, the share does not go to one
    lim = sig(math.log(.001/.999) + .5)
    expect(close(lim, .00164765, 1e-5) and 1 - .08*lim/.05 > .3, "load: cubic payoff-monotone selection stops near 0.00165 and the host stays above its floor")
    # (D) a row sum of one half certifies eventual removal, not present independence
    st = lambda t: (sig(math.log(9) - .5*t + 150*(-math.expm1(-.01*t))), .5 + 1.5*math.exp(-.01*t))
    x50, z50 = st(50)
    expect(x50 > 1 - 1e-12 and z50 > 1.4 and st(1000)[0] < 1e-100, "certificate: captured share above 0.999999999999 at t=50, then removed")
    # (E) a gain exactly one survives pruning but its captured corner is unstable
    def rk(u, z, G, T, dt=.005):
        f = lambda a, b: (b - 1, G*sig(a) - b)
        for _ in range(int(round(T/dt))):
            a, b = f(u, z); c, d = f(u+dt*a/2, z+dt*b/2); e, h = f(u+dt*c/2, z+dt*d/2); q, r = f(u+dt*e, z+dt*h)
            u, z = u+dt*(a+2*c+2*e+q)/6, z+dt*(b+2*d+2*h+r)/6
        return u, z
    u1, z1 = rk(math.log(99), .99, 1, 300)
    expect(sig(u1) < 1e-6 and z1 < 1e-3, "certificate(4): at G=1 a start at (0.99, 0.99) leaves the captured corner for no capture")
    # (F) dwell is an infimum: releases just either side of the boundary go to opposite basins
    ins = lambda u0, G, T: (u0 + G*(-math.expm1(-T)) - T, G*math.exp(-T))
    fate = lambda u, z: rk(u, z, 2, 100, .01)[0] < 0
    lo, hi, u0 = 0.0, 40.0, math.log(99)
    for _ in range(24):
        m = (lo + hi)/2
        if fate(*ins(u0, 2, m)): hi = m
        else: lo = m
    Tb = (lo + hi)/2
    print(f"  (F) boundary at G=2, equal speeds, x0=0.99: {Tb:.6f}")
    expect(abs(Tb - 5.858956) < 2e-3 and fate(*ins(u0, 2, Tb + .01)) and not fate(*ins(u0, 2, Tb - .01)),
           "dwell: T_min near 5.859 is a boundary; release 0.01 beyond it is restored, 0.01 short is recaptured")
    # (G) frontier: destruction must beat rest as well as expansion
    vX, vD = .1 - 1.1, -1 + 1/3
    expect(vD > vX and max(0, vX, vD) == 0, "frontier: with n=4, c_y=Delta_y=1, destruction beats expansion and rest beats both")
    # (H) onegroup: a background advantage correlated with the trait carries it
    z, ph = (0, 1), (0, 2); pay = [ph[i] + .5 - z[i] for i in range(2)]
    cov = sum((z[i]-.5)*(pay[i]-1) for i in range(2))/2
    expect(close(cov, .25, 1e-12), "onegroup: Cov(phi,z) - c Var(z) = 0.25 > 0 with a correlated background")
    # (I) lockin: delayed recovery, not irreversibility, unless the interval is denied
    rec = math.log((1-.2)/(1-.5))/.1
    expect(close(rec, 4.70004, 1e-5), "lockin: capacity 0.2 recovers to the floor 0.5 after 10 ln 1.6 = 4.70004")
    # (J) readiness: an indifference band about the threshold releases a level just below it about half the time;
    #     the lower registered level at the threshold controls release below it; decaying information never decides
    random.seed(20261004)
    a_, b_ = .01, .01; A, B = math.log((1-b_)/a_), math.log(b_/(1-a_))
    def sprt(mu, lo_, hi_, nmax=10000):
        L = 0.0
        for _ in range(nmax):
            x = random.gauss(mu, 1.0); L += (hi_ - lo_)*(x - (lo_ + hi_)/2)
            if L >= A: return 1
            if L <= B: return 0
        return 0
    n = 3000
    band = sum(sprt(.49, 0.0, 1.0) for _ in range(n))/n
    atthr = sum(sprt(.49, .5, 1.5) for _ in range(n))/n
    up = sum(math.log1p(2*2**(-t-4)) for t in range(1, 400)); dn = sum(math.log1p(-2*2**(-t-4)) for t in range(1, 400))
    print(f"  (J) met at 0.49 with levels (0,1): {band:.3f}; with levels (0.5,1.5): {atthr:.4f}; decaying-information LLR range [{dn:.6f}, {up:.6f}]")
    expect(.40 < band < .58 and atthr < .03 and up < math.log((1-.05/7)/.01) and dn > math.log((.05/7)/(1-.01)),
           "readrule: band about the threshold ~ half; lower level at the threshold <= 3%; decaying information never reaches either boundary")

def check_RV():
    """Preserved V7 review regressions. Each authored group is one counted gate."""
    import importlib.util, unittest, json
    block('RV', 'standprice loopgain onegroup masked enough rivalverify share relaxtrust dwell',
          'independent regression groups', 'Preserved V7 counterexamples and special cases')
    directory = pathlib.Path(__file__).resolve().parent / 'verification'
    def module(name):
        spec = importlib.util.spec_from_file_location('v7_' + name, directory / (name + '_checks.py'))
        loaded = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(loaded)
        return loaded
    mathematical = module('math')
    results = {}
    for name in ('check_lottery_distinction', 'check_nonlinear_prize_domain',
                 'check_preserved_proportional_case', 'check_background_scope'):
        try:
            results[name] = getattr(mathematical, name)()
            expect(True, 'math: ' + name)
        except Exception as error:
            expect(False, 'math: ' + name + ': ' + repr(error))
    print('  RV mathematical values: ' + json.dumps(results, sort_keys=True))
    for domain, cls in (('systems', 'SystemsChecks'), ('transition', 'TransitionChecks')):
        loaded = module(domain)
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(getattr(loaded, cls))
        for case in suite:
            result = unittest.TestResult()
            case.run(result)
            expect(result.wasSuccessful() and not result.skipped, domain + ': ' + case._testMethodName)
            for _, detail in result.failures + result.errors:
                print(detail)

def check_RP():
    """Inherited V7.1 readiness counterexamples and retained positive cases."""
    import importlib.util, json
    block('RP', 'require safeguards standprice corrrate scope enforce coverage nested',
          'analytical witnesses with independent computations',
          'Inherited V7.1 readiness boundaries and retained cases')
    path = pathlib.Path(__file__).resolve().parent / 'verification' / 'readiness_checks.py'
    spec = importlib.util.spec_from_file_location('v73_readiness', path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    try:
        results = loaded.run_checks()
    except Exception as error:
        expect(False, 'readiness: ' + repr(error))
        raise
    for name in results:
        expect(True, 'readiness: ' + name)
    print('  RP values: ' + json.dumps(results, sort_keys=True))

def check_RC():
    """V7.3 reduced joint certificate and the limits of its diagnostics."""
    import importlib.util, json
    block('RC', 'jointcorrection certificate safeguards',
          'independent integration with analytical and identity controls',
          'Correction, load and host viability; transient and selection counterexamples')
    path = pathlib.Path(__file__).resolve().parent / 'verification' / 'correction_checks.py'
    spec = importlib.util.spec_from_file_location('v73_correction', path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    try:
        results = loaded.run_checks()
    except Exception as error:
        expect(False, 'correction: ' + repr(error))
        raise
    for name in results:
        expect(True, 'correction: ' + name)
    print('  RC values: ' + json.dumps(results, sort_keys=True))

def check_PT():
    """V7.3 finite reform path and implementation boundaries."""
    import importlib.util, json
    block('PT', 'reformpath jointcorrection',
          'comparison bounds with independent trajectory checks and adverse controls',
          'Finite correction, delayed structural reform and protected transition')
    path = pathlib.Path(__file__).resolve().parent / 'verification' / 'path_checks.py'
    spec = importlib.util.spec_from_file_location('v73_path', path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    try:
        results = loaded.run_checks()
    except Exception as error:
        expect(False, 'path: ' + repr(error))
        raise
    for name in results:
        expect(True, 'path: ' + name)
    print('  PT values: ' + json.dumps(results, sort_keys=True))

ORDER = ['PT', 'RC', 'RP', 'RV', 'CX', 'FB', 'LG', 'CI', 'TC', 'TH', 'SM', 'CB', 'PR', 'CS', 'FA', 'DW', 'AC', 'RH', 'FS', 'EC', 'CR', 'BI', 'WG', 'TK', 'T3', 'HO', 'SH', 'PE', 'FD', 'NB',
         'CH', 'TD', 'CE', 'PD', 'SP', 'MP', 'QS', 'FF', 'SR', 'ES', 'JX', 'DL', 'AL', 'TR', 'ML', 'VF']

LEGACY = [('../v5', 'checks_v5.py'), ('../v4', 'checks_v4.py'), ('../v4', 'checks_v42.py'), ('../v4', 'checks_v44.py'),
          ('../v4', 'checks_v45.py'), ('../v3', 'checks_v31.py')]

if __name__ == '__main__':
    t0 = time.time()
    only = [a for a in sys.argv[1:] if not a.startswith('--')]
    timing = []
    for code in ORDER:
        if only and code not in only: continue
        if 'check_' + code not in globals(): print(f"\n=== {code}: not defined"); continue
        t1 = time.time()
        globals()['check_' + code]()
        timing.append((code, time.time() - t1))
    print("\n=== timing by block (s): " + ", ".join(f"{c} {t:.0f}" for c, t in timing))
    if not only or _CODEX:
        print("=== Codex's boundary cases (../v6.1/reviews/counterexamples_v61_codex.py; plan s7 requires the eight marked *):")
        for k_, name in _CODEX_NAMES.items():
            req = '*' if k_ in (1, 3, 4, 5, 6, 7, 8, 9) else ' '
            where = _CODEX.get(k_)
            print(f"   {req} {name}: " + ("not run in this selection" if where is None else f"block {where[0]}, {'holds' if where[1] else 'FAILS'}"))
        if not only:
            _CURRENT['block'] = 'index'
            expect(all(k_ in _CODEX and _CODEX[k_][1] for k_ in (1, 3, 4, 5, 6, 7, 8, 9)), "all eight of Codex's boundary cases appear in a block and hold")
    print(f"=== assertions: {_ASSERT['ok']} passed, {len(_ASSERT['fail'])} failed" + (" (mode --full)" if FULL else " (default sizes)"))
    for f in _ASSERT['fail']: print(f"    FAILED: {f}")
    print(f"=== done in {time.time()-t0:.0f} s")
    if '--legacy' in sys.argv:
        here = pathlib.Path(__file__).parent
        for d, f in LEGACY:
            p = (here / d / f)
            if not p.exists(): print(f"legacy {d}/{f}: missing"); continue
            r = subprocess.run([sys.executable, f], cwd=p.parent, capture_output=True, text=True)
            log = p.with_suffix('.v7run.log'); log.write_text(r.stdout + r.stderr)
            print(f"legacy {d}/{f}: exit {r.returncode}; output in {log.name}")
    if _ASSERT['fail']: sys.exit(1)
