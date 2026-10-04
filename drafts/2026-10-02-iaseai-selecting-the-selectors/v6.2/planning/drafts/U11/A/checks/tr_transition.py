"""Block TR (proposed): the transition, Section 11 and S11 of V6.2.  Pure standard library.

Keys: signal, pausevalue, readiness (and its decision rule, Remark S11 `readrule`), the staying-out identity of X11.
Independent where marked: the signal game is checked by brute-force search over strategy profiles, not by the
formulas it tests; the readiness rule by simulation.  Port into checks_v62.py as block TR (one function, check_TR).

Run:  python3 tr_transition.py      (about 30 s)
"""
import math, random, statistics

PASS = []
def expect(ok, msg):
    PASS.append(bool(ok))
    print(("  [ok] " if ok else "  [FAIL] ") + msg)

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

print("=== TR [independent: (a)-(c) brute-force search over strategy profiles; (d)-(f) by direct computation; (g) simulation] keys: signal, pausevalue, readiness, readrule (S11)")
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

print(f"=== TR assertions: {sum(PASS)} passed, {len(PASS) - sum(PASS)} failed")
