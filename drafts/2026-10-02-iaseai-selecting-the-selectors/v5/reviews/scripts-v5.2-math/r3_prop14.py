"""Prop 1.4 (growth and the boundary): independent recomputation, the q_t<1 premise, the missing levers,
forward-looking actors, and repeated play."""
import math

def e_sym(n, r, Om, c, L, th):
    return r * Om * (n - 1 - th) / (n * n * (c + (1 + th) * L))

def q(a, n, r, Om, c, L, th):
    return a * L * n * e_sym(n, r, Om, c, L, th)

def survival(H, a, n, r, c, Om, L, th, link="linear"):
    s = 1.0; first_bad = None
    for t in range(1, H + 1):
        x = a * L(t) * n * e_sym(n, r, Om(t), c(t) if callable(c) else c, L(t), th(t))
        if link == "linear":
            if x >= 1:
                if first_bad is None: first_bad = t
                return 0.0, first_bad
            s *= 1 - x
        else:
            s *= math.exp(-x)
    return s, first_bad

a, n, r = 0.01, 4, 1.0
g = 1.03
cases = {
  "theta=0.4 fixed, L=0.3": (lambda t: g ** t, lambda t: 0.3, lambda t: 0.4),
  "gap 2.6 g^-t t^-1.5": (lambda t: g ** t, lambda t: 0.3, lambda t: 3 - 2.6 * g ** (-t) * t ** -1.5),
  "gap 2.6/t": (lambda t: g ** t, lambda t: 0.3, lambda t: 3 - 2.6 / t),
  "theta=-1, L=0.3": (lambda t: g ** t, lambda t: 0.3, lambda t: -1.0),
  "theta=-1, L=0.3 g^-t t^-1.5": (lambda t: g ** t, lambda t: 0.3 * g ** (-t) * t ** -1.5, lambda t: -1.0),
  "constant stakes, theta=0.4, L=0.3": (lambda t: 1.0, lambda t: 0.3, lambda t: 0.4),
}
for name, (Om, L, th) in cases.items():
    row = []
    for H in (100, 200, 1000, 10000):
        s, fb = survival(H, a, n, r, 1.0, Om, L, th)
        row.append(f"H={H}: {s:.3g}" + (f" (q>=1 first at t={fb})" if fb else ""))
    print(f"{name}: " + "; ".join(row))

# when does q_t reach 1 under the linear link?
for name, th in (("theta=0.4", 0.4), ("theta=-1", -1.0), ("theta=0", 0.0)):
    q1 = q(a, n, r, 1.0, 1.0, 0.3, th)
    T = math.log(1 / q1) / math.log(g)
    print(f"linear link: {name}, q_t = {q1:.6f} * 1.03^t reaches 1 at t = {T:.1f}")

# Poisson link q = 1 - exp(-a L E): survival = exp(-a * cumulative shared damage), no q<1 caveat
for name, (Om, L, th) in list(cases.items())[:4]:
    s, _ = survival(200, a, n, r, 1.0, Om, L, th, link="poisson")
    print(f"Poisson link, {name}: survival at H=200 = {s:.3g}")

# ---- The missing lever: private cost per unit (liability / levy tau_t), at theta = -1, L fixed
for name, cfun in (("c fixed at 1", lambda t: 1.0),
                   ("c_t = 1 + tau_t with tau_t = g^t t^1.5 (levy rising faster than stakes)", lambda t: 1.0 + g ** t * t ** 1.5),
                   ("c_t = g^t (cost of a unit of racing rises with the stakes)", lambda t: g ** t)):
    row = []
    for H in (100, 1000, 10000):
        s, fb = survival(H, a, n, r, cfun, lambda t: g ** t, lambda t: 0.3, lambda t: -1.0)
        row.append(f"H={H}: {s:.3g}")
    print(f"theta=-1, L=0.3, stakes 3%/round, {name}: " + "; ".join(row))

# ---- Forward-looking actors: the irreversible event priced into the objective.
# Each actor values its own continuation V_{t+1}; with self-model theta it also counts theta * others' continuation.
# Per-unit shared cost becomes L(1 + a*delta*V_{t+1}), entering marginal cost with weight (1+theta):
#   e_t = r(n-1-theta) Om_t / (n^2 (c + (1+theta) L (1 + a delta V_{t+1})))
#   V_t = Om_t/n - (c + nL) e_t + delta (1 - a L n e_t) V_{t+1}
def forward(theta, delta, T=3000, g=1.03, a=0.01, n=4, r=1.0, c=1.0, L=0.3):
    V = 0.0; qs = [0.0] * (T + 1)
    for t in range(T, 0, -1):
        Om = g ** t
        e = r * (n - 1 - theta) * Om / (n * n * (c + (1 + theta) * L * (1 + a * delta * V)))
        qt = a * L * n * e
        qt = min(qt, 0.999999)
        qs[t] = qt
        V = Om / n - (c + n * L) * e + delta * (1 - qt) * V
    s = 1.0; out = {}
    for t in range(1, T + 1):
        s *= 1 - qs[t]
        if t in (50, 100, 200, 500, 1000): out[t] = s
    return qs, out
for theta in (0.0, 0.4, -1.0):
    for delta in (0.95, 0.99):
        qs, out = forward(theta, delta)
        print(f"forward-looking theta={theta:+.1f}, delta={delta}: q_t at t=10,100,200,500,1000 = "
              + ", ".join(f"{qs[t]:.4f}" for t in (10, 100, 200, 500, 1000))
              + "; survival at 100, 200, 1000 = " + ", ".join(f"{out[t]:.3g}" for t in (100, 200, 1000)))
print("myopic theta=0: q_t at t=10,100,200 =", ", ".join(f"{q(a, n, r, g ** t, 1.0, 0.3, 0.0):.4f}" for t in (10, 100, 200)))

# ---- Repeated play: grim reversion sustaining near-zero intensity (stage contest, stationary stakes)
# effective game: V = Om (n-1-theta)/(n-1), k = c + (1+theta) l; objective payoffs (ignoring e-independent terms that are the same across paths? no: compute full O)
def stage_O(es, n, r, Om, c, l, th):
    tot = sum(x ** r for x in es); w = [x ** r / tot for x in es]; E = sum(es)
    pi = [Om * w[j] - c * es[j] - l * E for j in range(n)]
    return [pi[i] + th * sum(pi[j] for j in range(n) if j != i) / (n - 1) for i in range(n)]
def delta_crit(th, n=4, r=1.0, Om=1.0, c=1.0, l=0.3, e0=1e-6):
    coop = stage_O([e0] * n, n, r, Om, c, l, th)[0]
    # best deviation against others at e0
    best = max(stage_O([y] + [e0] * (n - 1), n, r, Om, c, l, th)[0] for y in [k / 10000 for k in range(1, 20001)])
    en = e_sym(n, r, Om, c, l, th)
    nash = stage_O([en] * n, n, r, Om, c, l, th)[0]
    # sustain iff coop >= (1-d) best + d nash
    if best <= coop: return 0.0, coop, best, nash
    if coop <= nash: return None, coop, best, nash
    return (best - coop) / (best - nash), coop, best, nash
for th in (0.0, 0.4, -0.5, -1.0):
    d, co, be, na = delta_crit(th)
    print(f"repeated contest, theta={th:+.1f}: cooperation {co:+.4f}, best deviation {be:+.4f}, stage Nash {na:+.4f} -> "
          + ("never sustainable (cooperation not above Nash in objectives)" if d is None else f"near-zero intensity sustained by grim reversion iff delta >= {d:.3f}"))
