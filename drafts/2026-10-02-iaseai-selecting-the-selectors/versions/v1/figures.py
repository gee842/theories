#!/usr/bin/env python3
"""Figures and every number quoted in the paper "Selecting the Selectors".

Pure Python, no dependencies. Writes fig-field.tex and fig-hysteresis.tex
(pgfplots code) and prints the checked numbers to stdout (see checks.log).

Model (Section 4): n domains, practice share x_i and rule support r_i,
    dx_i/dt = kappa_i x_i (1 - x_i) (a_i r_i - c_i)
    dr_i/dt = eps_i (sum_j b_ij x_j - d_i r_i)
with normalised conversion R_ij = a_i b_ij / (c_i d_i).
Shared condition and evaluation (Section 4.4):
    dV/dt = V [rho (1 - V/K) - h x_D],   y = V + beta x_E (K - V).
"""

N = ["Development", "Evaluation", "Standards", "Procurement", "Formation", "Information"]
SHORT = ["D", "E", "S", "P", "F", "I"]
n = len(N)
D, E, S, P, F, I = range(n)

KAPPA = [1.0, 0.5, 0.5, 1.0, 0.2, 0.5]   # selection speed (formation slowest)
EPS = [0.2, 0.2, 0.1, 0.2, 0.05, 0.2]    # rule-revision speed
A = [1.0] * n
C = [1.0] * n
DD = [1.0] * n

R_HUB_SELF = 1.3   # development's own conversion (self-sustaining)
R_OWN = 0.3        # every other domain's own conversion (subcritical)
PHI = 0.1          # conversion among non-hub domains
THETA_PRE = 0.6    # hub-to-domain conversion before general-purpose coupling
THETA_GPAI = 1.2   # hub-to-domain conversion with general-purpose coupling
THETA_FIREWALL = 0.2

RHO, K, H = 0.005, 1.0, 0.008
BETA, V_ALARM, V_MIN = 0.7, 0.6, 0.3
DELAY = 10.0       # alarm-to-reform delay
C_REFORM = 2.0     # liability on development after the alarm

FLOOR = 1e-4       # persistent entry: no domain is ever exactly empty


def conv_matrix(theta, phi=PHI, own=R_OWN, hub_self=R_HUB_SELF, firewall=None):
    R = [[0.0] * n for _ in range(n)]
    R[D][D] = hub_self
    for i in range(1, n):
        R[i][i] = own
        R[i][D] = theta
        for j in range(1, n):
            if j != i:
                R[i][j] = phi
    for i, val in (firewall or {}).items():
        R[i][D] = val
    return R


def make_field(R, c=None, with_substrate=False):
    c = list(c or C)
    b = [[R[i][j] * C[i] * DD[i] / A[i] for j in range(n)] for i in range(n)]

    def f(t, y, cc=None):
        cc = cc or c
        x, r = y[:n], y[n:2 * n]
        dx = [KAPPA[i] * x[i] * (1 - x[i]) * (A[i] * r[i] - cc[i]) for i in range(n)]
        dr = [EPS[i] * (sum(b[i][j] * x[j] for j in range(n)) - DD[i] * r[i]) for i in range(n)]
        out = dx + dr
        if with_substrate:
            V = y[2 * n]
            out.append(V * (RHO * (1 - V / K) - H * x[D]))
        return out
    return f


def clamp(y):
    z = list(y)
    for i in range(n):
        z[i] = min(1 - 1e-12, max(FLOOR, z[i]))
        z[n + i] = max(0.0, z[n + i])
    return z


def rk4_step(f, t, y, dt, **kw):
    k1 = f(t, y, **kw)
    k2 = f(t + dt / 2, [y[i] + dt / 2 * k1[i] for i in range(len(y))], **kw)
    k3 = f(t + dt / 2, [y[i] + dt / 2 * k2[i] for i in range(len(y))], **kw)
    k4 = f(t + dt, [y[i] + dt * k3[i] for i in range(len(y))], **kw)
    return [y[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(y))]


def simulate(R, y0, T, dt=0.05, every=1.0, with_substrate=False, correction=False):
    """Integrate; if correction, raise c_D to C_REFORM DELAY after the first alarm."""
    f = make_field(R, with_substrate=with_substrate)
    cc = list(C)
    t, y = 0.0, list(y0)
    rec = [(t, list(y))]
    t_alarm = None
    steps, k_every = int(round(T / dt)), int(round(every / dt))
    for k in range(steps):
        y = rk4_step(f, t, y, dt, cc=cc)
        y = clamp(y) if not with_substrate else clamp(y[:2 * n]) + [max(0.0, y[2 * n])]
        t += dt
        if with_substrate:
            V = y[2 * n]
            obs = V + BETA * y[E] * (K - V)
            if t_alarm is None and obs <= V_ALARM:
                t_alarm = t
            if correction and t_alarm is not None and t >= t_alarm + DELAY:
                cc[D] = C_REFORM
        if (k + 1) % k_every == 0:
            rec.append((t, list(y)))
    return rec, t_alarm


def inbound(R, i, Sset):
    return sum(R[i][j] for j in Sset)


def first_cross(rec, idx, level=0.5, above=True):
    for t, y in rec:
        if (y[idx] > level) if above else (y[idx] < level):
            return t
    return None


def fmt(v, nd=2):
    return f"{v:.{nd}f}" if v is not None else "never"


# ---------------------------------------------------------------------------
lines = []
def say(s=""):
    print(s)
    lines.append(s)

say("== Field parameters ==")
say(f"kappa={KAPPA} eps={EPS}; a=c=d=1 so R_ij=b_ij")
say(f"R_DD={R_HUB_SELF}, R_ii={R_OWN} (i!=D), phi={PHI}, theta pre={THETA_PRE}, GPAI={THETA_GPAI}, firewall={THETA_FIREWALL}")

# Proposition 1 checks: stable configurations
Rg = conv_matrix(THETA_GPAI)
full = list(range(n))
say("\n== Configurations (Prop. 1) ==")
say("GPAI field, full capture row sums: " + ", ".join(f"{SHORT[i]}={inbound(Rg, i, full):.2f}" for i in range(n)))
Rp = conv_matrix(THETA_PRE)
say("Pre-GPAI field, inbound to non-hubs from {D}: " + ", ".join(f"{SHORT[i]}={inbound(Rp, i, [D]):.2f}" for i in range(1, n)))
say("Pre-GPAI field, full-capture row sums: " + ", ".join(f"{SHORT[i]}={inbound(Rp, i, full):.2f}" for i in range(n)))

y0 = [0.9] + [0.02] * (n - 1) + [1.5] + [0.0] * (n - 1)

say("\n== Cascade (Prop. 2), y0: x_D=0.9, r_D=1.5, x_i=0.02, r_i=0 ==")
results = {}
for label, R in [("pre", Rp), ("gpai", Rg), ("firewall", conv_matrix(THETA_GPAI, firewall={E: THETA_FIREWALL, F: THETA_FIREWALL}))]:
    rec, _ = simulate(R, y0, T=400, every=1.0)
    results[label] = rec
    xs = rec[-1][1][:n]
    say(f"{label:9s} final x: " + " ".join(f"{SHORT[i]}={xs[i]:.3f}" for i in range(n)))
    say("          x_i>0.5 at t: " + " ".join(f"{SHORT[i]}={fmt(first_cross(rec, i), 0)}" for i in range(n)))
Rf = conv_matrix(THETA_GPAI, firewall={E: THETA_FIREWALL, F: THETA_FIREWALL})
capt = [D, S, P, I]
say("Firewall field, inbound from captured {D,S,P,I}: E=%.2f F=%.2f; S=%.2f P=%.2f I=%.2f" % (
    inbound(Rf, E, capt), inbound(Rf, F, capt), inbound(Rf, S, capt), inbound(Rf, P, capt), inbound(Rf, I, capt)))

# Corollary 2: re-absorption of a one-domain reform
say("\n== Re-absorption (Cor. 2) ==")
recfull, _ = simulate(Rg, [0.9] + [0.5] * (n - 1) + [1.5] * n, T=600)
yfull = recfull[-1][1]
say("full-capture state x: " + " ".join(f"{v:.3f}" for v in yfull[:n]))
yref = list(yfull); yref[S] = 0.01; yref[n + S] = 0.0
R2 = conv_matrix(THETA_GPAI); R2[S][S] = 0.0
rec2, _ = simulate(R2, yref, T=300)
say(f"Standards reform (x_S->0.01, r_S->0, own conversion cut to 0): x_S(300)={rec2[-1][1][S]:.3f}; re-captured (x_S>0.5) at t={fmt(first_cross(rec2, S), 1)}; inbound from others={inbound(R2, S, [D, E, P, F, I]):.2f}")
R3 = conv_matrix(THETA_GPAI); R3[S][S] = 0.0; R3[S][D] = THETA_FIREWALL
rec3, _ = simulate(R3, yref, T=300)
say(f"Standards reform + firewall D->S ({THETA_FIREWALL}): x_S(300)={rec3[-1][1][S]:.4f}; inbound from others={inbound(R3, S, [D, E, P, F, I]):.2f}")

# Hysteresis
say("\n== Hysteresis in hub coupling theta ==")
def sweep(phi, thetas, T=1500):
    yy = [0.9] + [FLOOR] * (n - 1) + [1.5] + [0.0] * (n - 1)
    up, down = [], []
    for th in thetas:
        rec, _ = simulate(conv_matrix(th, phi=phi), yy, T=T, every=T)
        yy = rec[-1][1]; up.append((th, sum(1 for v in yy[1:n] if v > 0.5)))
    for th in reversed(thetas):
        rec, _ = simulate(conv_matrix(th, phi=phi), yy, T=T, every=T)
        yy = rec[-1][1]; down.append((th, sum(1 for v in yy[1:n] if v > 0.5)))
    return up, down
thetas = [round(0.05 * k, 2) for k in range(0, 31)]
import json, os
CACHE = "hyst-cache.json"
hyst = {}
cached = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
for phi in (0.1, 0.2):
    if str(phi) in cached:
        up, down = [tuple(p) for p in cached[str(phi)][0]], [tuple(p) for p in cached[str(phi)][1]]
    else:
        up, down = sweep(phi, thetas)
        cached[str(phi)] = (up, down)
        json.dump(cached, open(CACHE, "w"))
    hyst[phi] = (up, down)
    up_switch = next(th for th, k in up if k > 0)
    down_switch = next((th for th, k in down if k < 5), None)
    say(f"phi={phi}: up-sweep first capture at theta={up_switch}; down-sweep first loss at theta={down_switch}; theory: up at theta>1, down below theta=1-{R_OWN}-4*{phi}={1 - R_OWN - 4 * phi:.2f}")

# Closure via evaluation
say("\n== Selecting the selectors (Prop. 3) ==")
say(f"rho={RHO}, h={H}, K={K}, beta={BETA}, V_alarm={V_ALARM}, V_min={V_MIN}; silencing needs beta*x_E >= {V_ALARM / (BETA * K):.3f}")
ys0 = y0 + [1.0]
recG, taG = simulate(Rg, ys0, T=400, with_substrate=True, correction=True)
recF, taF = simulate(Rf, ys0, T=400, with_substrate=True, correction=True)
def vmin_time(rec, level):
    return next((t for t, y in rec if y[2 * n] < level), None)
say(f"GPAI: alarm at t={fmt(taG, 1)}; V(400)={recG[-1][1][2*n]:.3f}; V<V_min at t={fmt(vmin_time(recG, V_MIN), 0)}; x_E(75)={[y for t, y in recG if abs(t-75)<1e-6][0][E]:.3f}")
say(f"Firewall: alarm at t={fmt(taF, 1)}; reform at t={fmt(taF + DELAY if taF else None, 1)}; min V={min(y[2*n] for t, y in recF):.3f}; V(400)={recF[-1][1][2*n]:.3f}")
xF = recF[-1][1][:n]
say("Firewall, final x after correction: " + " ".join(f"{SHORT[i]}={xF[i]:.3f}" for i in range(n)))
# masking-free GPAI counterfactual
BETA_SAVE = BETA
BETA = 0.0
recG0, taG0 = simulate(Rg, ys0, T=400, with_substrate=True, correction=True)
BETA = BETA_SAVE
say(f"GPAI with independent measurement (beta=0): alarm at t={fmt(taG0, 1)}; V(400)={recG0[-1][1][2*n]:.3f}; final x: " + " ".join(f"{SHORT[i]}={recG0[-1][1][i]:.3f}" for i in range(n)))

open("checks.log", "w").write("\n".join(lines) + "\n")

# ---------------------------------------------------------------------------
# pgfplots output
COL = ["cD", "cE", "cS", "cP", "cF", "cI"]
STY = ["thick", "very thick", "thick, densely dashed", "thick, dashdotted", "very thick, dotted", "thick, loosely dashed"]

def coords(rec, idx, tmax, step=4):
    pts = [(t, y[idx]) for t, y in rec if t <= tmax + 1e-9]
    pts = pts[::step] + ([pts[-1]] if (len(pts) - 1) % step else [])
    return " ".join(f"({t:.0f},{v:.4f})" for t, v in pts)

def obs_coords(rec, tmax, step=4):
    pts = []
    for t, y in rec:
        if t <= tmax + 1e-9:
            V = y[2 * n]
            pts.append((t, V + BETA * y[E] * (K - V)))
    pts = pts[::step]
    return " ".join(f"({t:.0f},{v:.4f})" for t, v in pts)

TMAX = 300
out = []
out.append(r"\begin{tikzpicture}")
out.append(r"\begin{groupplot}[group style={group size=4 by 1, horizontal sep=1.15cm}, width=4.55cm, height=3.5cm,")
out.append(r"  xmin=0, xmax=%d, ymin=-0.03, ymax=1.05, xtick={0,100,200,300}, ytick={0,0.5,1}," % TMAX)
out.append(r"  tick label style={font=\scriptsize}, label style={font=\scriptsize}, title style={font=\scriptsize, yshift=-1ex},")
out.append(r"  xlabel={time}, every axis plot/.append style={line join=round}]")
for k, (lab, rec) in enumerate([("(a) Coupled field", results["gpai"]), ("(b) Selectors firewalled", results["firewall"])]):
    out.append(r"\nextgroupplot[title={%s}%s]" % (lab, ", ylabel={share $x_i$}" if k == 0 else ""))
    for i in range(n):
        out.append(r"\addplot[%s, %s] coordinates {%s};" % (COL[i], STY[i], coords(rec, i, TMAX)))
        if k == 0:
            out.append(r"\label{pl:%s}" % SHORT[i])
for k, (lab, rec, ta) in enumerate([("(c) Condition, coupled", recG, taG), ("(d) Condition, firewalled", recF, taF)]):
    out.append(r"\nextgroupplot[title={%s}%s, ymin=0, ymax=1.05]" % (lab, ", ylabel={condition}" if k == 0 else ""))
    out.append(r"\addplot[gray, thin, dashed, domain=0:%d] {%.2f};" % (TMAX, V_ALARM))
    out.append(r"\addplot[cH, thin, dotted, domain=0:%d] {%.2f};" % (TMAX, V_MIN))
    out.append(r"\addplot[black, very thick] coordinates {%s};" % coords(rec, 2 * n, TMAX))
    if k == 0:
        out.append(r"\label{pl:V}")
    out.append(r"\addplot[cE, very thick, densely dashed] coordinates {%s};" % obs_coords(rec, TMAX))
    if k == 0:
        out.append(r"\label{pl:y}")
    if ta is not None and ta <= TMAX:
        out.append(r"\draw[->, thin] (axis cs:%.0f,0.22) -- (axis cs:%.0f,%.2f);" % (ta, ta, 0.52))
        out.append(r"\node[font=\tiny, anchor=north west, inner sep=1pt] at (axis cs:%.0f,0.24) {alarm};" % (ta + 4))
out.append(r"\end{groupplot}")
out.append(r"\end{tikzpicture}")
open("fig-field.tex", "w").write("\n".join(out) + "\n")

h = []
h.append(r"\begin{tikzpicture}")
h.append(r"\begin{groupplot}[group style={group size=2 by 1, horizontal sep=0.55cm, y descriptions at=edge left}, width=0.565\columnwidth, height=3.6cm,")
h.append(r"  xmin=0, xmax=1.5, ymin=-0.3, ymax=5.6, xtick={0,0.5,1,1.5}, ytick={0,1,2,3,4,5},")
h.append(r"  xlabel={hub coupling $\theta$}, tick label style={font=\scriptsize}, label style={font=\scriptsize}, title style={font=\scriptsize, yshift=-1ex}]")
for k, phi in enumerate((0.1, 0.2)):
    up, down = hyst[phi]
    opts = "title={(%s) $\\varphi=%.1f$}" % ("ab"[k], phi)
    if k == 0:
        opts += ", ylabel={domains captured}"
    h.append(r"\nextgroupplot[%s]" % opts)
    h.append(r"\addplot[gray, thin, dotted] coordinates {(1,-0.3) (1,5.6)};")
    thr = 1 - R_OWN - 4 * phi
    if thr > 0:
        h.append(r"\addplot[gray, thin, dotted] coordinates {(%.2f,-0.3) (%.2f,5.6)};" % (thr, thr))
    h.append(r"\addplot[cD, thick, mark=*, mark size=0.9pt] coordinates {%s};" % " ".join(f"({th},{c})" for th, c in up))
    if k == 0:
        h.append(r"\label{pl:up}")
    h.append(r"\addplot[cH, thick, densely dashed, mark=o, mark size=1.1pt] coordinates {%s};" % " ".join(f"({th},{c})" for th, c in reversed(down)))
    if k == 0:
        h.append(r"\label{pl:down}")
h.append(r"\end{groupplot}")
h.append(r"\end{tikzpicture}")
open("fig-hysteresis.tex", "w").write("\n".join(h) + "\n")
print("\nwrote fig-field.tex, fig-hysteresis.tex, checks.log")
