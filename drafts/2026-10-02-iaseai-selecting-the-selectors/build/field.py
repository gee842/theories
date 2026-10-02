"""Field model of recursive selection (v2), with persistent two-way entry.

    dx_i/dt = kappa_i x_i (1-x_i)(a_i r_i - c_i) + mu (1 - 2 x_i)
    dr_i/dt = eps_i (sum_j b_ij x_j - d_i r_i)

integrated in logit coordinates z_i = log(x_i / (1 - x_i)), in which the entry
term is -2 mu sinh(z_i), so shares never round to exactly 0 or 1.
Shared condition dV/dt = V [rho (1 - V/K) - h x_D], integrated as log V.
Observed condition y = V + beta x_E (K - V).
"""
import math

n = 6
D, E, S, P, F, I = range(n)
SHORT = ["D", "E", "S", "P", "F", "I"]

KAPPA = [1.0, 0.5, 0.5, 1.0, 0.2, 0.5]   # selection speed (formation slowest)
EPS = [0.2, 0.2, 0.1, 0.2, 0.05, 0.2]    # rule-revision speed
A = [1.0] * n
C0 = [1.0] * n
DD = [1.0] * n                            # a = c = d = 1 at baseline, so R = b

R_HUB, R_OWN, PHI = 1.3, 0.3, 0.11
THETA_PRE, THETA_GP, THETA_FW = 0.6, 1.2, 0.2
MU = 1e-4
RHO, K, H = 0.005, 1.0, 0.008
V_ALARM, V_MIN = 0.6, 0.3
DELAY, C_REFORM = 10.0, 2.0
DT = 0.05


def sig(z):
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    e = math.exp(z)
    return e / (1.0 + e)


def logit(x):
    return math.log(x / (1.0 - x))


def conv(theta, phi=PHI, psi=0.0, own=R_OWN, hub=R_HUB, fw=None):
    """Normalised conversion R: hub D, all-pairs phi among the others, feedback psi into D."""
    R = [[0.0] * n for _ in range(n)]
    R[D][D] = hub
    for i in range(1, n):
        R[i][i] = own
        R[i][D] = theta
        R[D][i] = psi
        for j in range(1, n):
            if j != i:
                R[i][j] = phi
    for i, v in (fw or {}).items():
        R[i][D] = v
    return R


def to_b(R):
    """Physical conversion rates b_ij = R_ij c_i d_i / a_i at the baseline c."""
    return [[R[i][j] * C0[i] * DD[i] / A[i] for j in range(n)] for i in range(n)]


def inbound(R, i, Sset):
    return sum(R[i][j] for j in Sset)


def rhs(y, B, c, mu, sub):
    z, r = y[:n], y[n:2 * n]
    x = [sig(v) for v in z]
    out = []
    for i in range(n):
        dz = KAPPA[i] * (A[i] * r[i] - c[i])
        if mu:
            dz -= 2.0 * mu * math.sinh(z[i])
        out.append(dz)
    for i in range(n):
        out.append(EPS[i] * (sum(B[i][j] * x[j] for j in range(n)) - DD[i] * r[i]))
    if sub:
        out.append(RHO * (1.0 - math.exp(y[2 * n]) / K) - H * x[D])
    return out


def rk4(y, B, c, mu, sub, dt=DT):
    k1 = rhs(y, B, c, mu, sub)
    y2 = [y[i] + dt / 2 * k1[i] for i in range(len(y))]
    k2 = rhs(y2, B, c, mu, sub)
    y3 = [y[i] + dt / 2 * k2[i] for i in range(len(y))]
    k3 = rhs(y3, B, c, mu, sub)
    y4 = [y[i] + dt * k3[i] for i in range(len(y))]
    k4 = rhs(y4, B, c, mu, sub)
    return [y[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(y))]


def state(x0, r0, V0=None):
    y = [logit(v) for v in x0] + list(r0)
    if V0 is not None:
        y.append(math.log(V0))
    return y


def simulate(R, y0, T, c=None, mu=MU, sub=False, beta=0.0, reform=None, every=1.0,
             R_after=None):
    """Integrate. reform = dict(c={i: value}, delay=...) applied `delay` after the first alarm.
    Returns (records, info): records are (t, x list, r list, V or None)."""
    B = to_b(R)
    c = list(c or C0)
    y = list(y0)
    t = 0.0
    steps = int(round(T / DT))
    k_every = max(1, int(round(every / DT)))
    rec = []
    info = {"t_alarm": None, "t_reform": None, "minV": None, "t_floor": None}

    def snap():
        x = [sig(v) for v in y[:n]]
        V = math.exp(y[2 * n]) if sub else None
        rec.append((t, x, list(y[n:2 * n]), V))

    snap()
    for k in range(steps):
        y = rk4(y, B, c, mu, sub)
        t += DT
        if sub:
            V = math.exp(y[2 * n])
            xE = sig(y[E])
            obs = V + beta * xE * (K - V)
            if info["t_alarm"] is None and obs <= V_ALARM:
                info["t_alarm"] = t
            if reform and info["t_alarm"] is not None and info["t_reform"] is None \
                    and t >= info["t_alarm"] + reform.get("delay", DELAY):
                info["t_reform"] = t
                for i, v in reform["c"].items():
                    c[i] = v
                if R_after is not None:
                    B = to_b(R_after)
            info["minV"] = V if info["minV"] is None else min(info["minV"], V)
            if info["t_floor"] is None and V < V_MIN:
                info["t_floor"] = t
        if (k + 1) % k_every == 0:
            snap()
    return rec, info, y


def first_cross(rec, i, level=0.5, above=True, after=0.0):
    for t, x, r, V in rec:
        if t < after:
            continue
        if (x[i] > level) if above else (x[i] < level):
            return t
    return None


def captured(x, level=0.5):
    return [i for i in range(n) if x[i] > level]


# --- configuration analysis (Proposition 1, certificates) -------------------
def subsets(m):
    for mask in range(1 << m):
        yield [i for i in range(m) if mask >> i & 1]


def config_status(R, Sset):
    """Return ('stable'|'unstable'|'tie', min |s-1|) for E_S."""
    margins = []
    stable = True
    for i in range(len(R)):
        s = inbound(R, i, Sset)
        margins.append(abs(s - 1))
        if i in Sset and not s > 1:
            stable = False
        if i not in Sset and not s < 1:
            stable = False
    tie = min(margins) < 1e-9
    return ("tie" if tie else ("stable" if stable else "unstable")), min(margins)


def core(R, C):
    C = list(C)
    changed = True
    while changed:
        changed = False
        for k in list(C):
            if inbound(R, k, C) < 1:
                C.remove(k)
                changed = True
    return C


def closure(R, Sset, support=None):
    """Cascade closure computed within the support (Proposition 3)."""
    Sk = set(Sset)
    sup = set(range(len(R))) if support is None else set(support)
    while True:
        new = {i for i in sup if i not in Sk and inbound(R, i, Sk) > 1}
        if not new:
            return sorted(Sk)
        Sk |= new


def keystone_sets(R, Sset, max_size=2):
    """Minimal sets Q in S whose removal prunes the core of S minus Q to the empty set or below S minus Q."""
    out = []
    for size in range(1, max_size + 1):
        for Q in subsets_of(Sset, size):
            rest = [k for k in Sset if k not in Q]
            if sorted(core(R, rest)) != sorted(rest):
                if not any(set(q) <= set(Q) for q in out):
                    out.append(Q)
    return out


def subsets_of(Sset, size):
    import itertools
    return [list(c) for c in itertools.combinations(Sset, size)]
