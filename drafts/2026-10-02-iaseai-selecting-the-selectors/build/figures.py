#!/usr/bin/env python3
"""Every number and data figure in "Selecting the Selectors" (v2).

Pure Python 3, no dependencies.  Run:  python3 figures.py
Writes checks.log, fig-capacity.tex, fig-field.tex, fig-hysteresis.tex.
The hysteresis sweep is cached in hyst-cache.json (delete it to recompute).
Modules: field.py (field model, Section 5), carrier.py (capacity, Section 4).
"""
import json
import math
import os
import random

from field import (n, D, E, S, P, F, I, SHORT, KAPPA, EPS, R_HUB, R_OWN, PHI,
                   THETA_PRE, THETA_GP, THETA_FW, MU, RHO, K, H, V_ALARM, V_MIN,
                   DELAY, C_REFORM, DT, C0, sig, logit, conv, to_b, inbound, simulate,
                   state, first_cross, captured, subsets, config_status, core,
                   closure, keystone_sets)
import field
from carrier import Carriers, bhat, field_mean_q, mean_q, advantage

LOG = []


def say(s=""):
    print(s, flush=True)
    LOG.append(s)


def fmt(v, nd=1):
    return "never" if v is None else f"{v:.{nd}f}"


def names(Sset):
    return "".join(SHORT[i] for i in Sset) or "none"


Y0 = state([0.9] + [0.02] * (n - 1), [1.5] + [0.0] * (n - 1))
YS0 = state([0.9] + [0.02] * (n - 1), [1.5] + [0.0] * (n - 1), V0=1.0)
RG = conv(THETA_GP)
RF = conv(THETA_GP, fw={E: THETA_FW, F: THETA_FW})
RP = conv(THETA_PRE)

say("== Parameters ==")
say(f"kappa={KAPPA} eps={EPS}; a=c=d=1 so R=b; entry mu={MU}; RK4 step {DT} in logit coordinates")
say(f"R_DD={R_HUB}, R_ii={R_OWN}, phi={PHI}, theta pre={THETA_PRE}, general-purpose={THETA_GP}, firewall={THETA_FW}")
say(f"V: rho={RHO}, h={H}, K={K}; V_alarm={V_ALARM}, floor={V_MIN}; reform c_D={C_REFORM} {DELAY} after detection")

# ---------------------------------------------------------------------------
say("\n== Configurations and certificates (Props. 1 and 4) ==")
for lab, R in (("theta=0.6", RP), ("theta=1.2", RG)):
    st = [Q for Q in subsets(n) if config_status(R, Q)[0] == "stable"]
    ties = [Q for Q in subsets(n) if config_status(R, Q)[0] == "tie"]
    minmargin = min(config_status(R, Q)[1] for Q in subsets(n))
    sel = [Q for Q in st if E in Q and F in Q and len(Q) < n]
    robust = [Q for Q in st if config_status(R, Q)[1] >= 0.05]
    robust_sel = [Q for Q in robust if E in Q and F in Q and len(Q) < n]
    say(f"{lab}: {len(st)} strictly stable configurations, {len(ties)} ties, smallest margin {minmargin:.3f}; "
        f"row sums {[round(sum(R[i]), 2) for i in range(n)]}; core(N)={names(core(R, range(n)))}; cl(D)={names(closure(R, [D]))}")
    say(f"   stable: {', '.join(names(Q) for Q in st)}")
    say(f"   stable with both selectors captured and not full: {len(sel)}; with every margin >= 0.05: "
        f"{len(robust)} stable, {len(robust_sel)} of them with both selectors and not full ({', '.join(names(Q) for Q in robust_sel)})")
say(f"Firewalled field: rows E={sum(RF[E]):.2f}, F={sum(RF[F]):.2f} (robust firewall: row < 1); "
    f"inbound to E from captured D,S,P,I = {inbound(RF, E, [D, S, P, I]):.2f}")
say(f"theta=1.2: keystones of full capture: {[names(Q) for Q in keystone_sets(RG, list(range(n)), 1)]}; "
    f"without D, inbound to each other domain = {inbound(RG, E, [E, S, P, F, I]):.2f}")
R0 = conv(0.0, phi=0.22)
five = [E, S, P, F, I]
say(f"theta=0, phi=0.22: inbound within E..I = {inbound(R0, E, five):.2f}; keystones of E..I: "
    f"{[names(Q) for Q in keystone_sets(R0, five, 1)]}; with one removed, inbound = {inbound(R0, E, [S, P, F, I]):.2f}")
Rg22 = conv(THETA_GP, phi=0.22)
say(f"theta=1.2, phi=0.22: single keystones of full capture: {[names(Q) for Q in keystone_sets(Rg22, list(range(n)), 1)]}; "
    f"keystone pairs: {[names(Q) for Q in keystone_sets(Rg22, list(range(n)), 2) if len(Q) == 2][:6]} ...")

# random check of the row-sum certificate
random.seed(7)
worst = 0.0
for trial in range(12):
    R = [[random.random() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        s = sum(R[i])
        scale = random.uniform(0.5, 0.97) / s
        R[i] = [v * scale for v in R[i]]
    y = state([0.999] * n, [5.0] * n)
    rec, info, yy = simulate(R, y, 600, mu=0.0, every=600)
    worst = max(worst, max(rec[-1][1]))
say(f"Row-sum certificate: 12 random fields with every row sum < 1, started at x=0.999, r=5, mu=0: largest share at t=600 = {worst:.2e}")

# ---------------------------------------------------------------------------
say("\n== Cascade (Prop. 5i), seed x_D=0.9, r_D=1.5, x_i=0.02 ==")
runs = {}
for lab, R in (("theta=0.6", RP), ("theta=1.2", RG), ("firewalled", RF)):
    rec, info, y = simulate(R, Y0, 400)
    runs[lab] = rec
    xs = rec[-1][1]
    say(f"{lab:10s} final x: " + " ".join(f"{SHORT[i]}={xs[i]:.3f}" for i in range(n)))
    say("           x>0.5 at t: " + " ".join(f"{SHORT[i]}={fmt(first_cross(rec, i), 0)}" for i in range(1, n)))

# ---------------------------------------------------------------------------
say("\n== Re-absorption and firewalls (Prop. 5iii) ==")
recfull, info, yfull = simulate(RG, state([0.9] + [0.5] * 5, [1.5] * 6), 600, every=600)
yref = list(yfull)
yref[S] = logit(0.01)
yref[n + S] = 0.0
R2 = conv(THETA_GP)
R2[S][S] = 0.0
rec2, info, y = simulate(R2, yref, 300)
say(f"Standards reset (x_S=0.01, r_S=0, own conversion 0): recaptured (x_S>0.5) at t={fmt(first_cross(rec2, S))}; "
    f"inbound from the others = {inbound(R2, S, [D, E, P, F, I]):.2f}")
R3 = conv(THETA_GP)
R3[S][S] = 0.0
R3[S][D] = THETA_FW
rec3, info, y = simulate(R3, yref, 300)
say(f"Same reset plus firewall D->S={THETA_FW}: x_S(300)={rec3[-1][1][S]:.4f}; inbound = {inbound(R3, S, [D, E, P, F, I]):.2f}")

# ---------------------------------------------------------------------------
say("\n== Masking and detection (Prop. 6): reform on D after detection ==")
a_, b_ = H - RHO, RHO / K   # under full capture dV/dt = -V (a_ + b_ V)


def delay_formula(beta):
    veff = (V_ALARM - beta * K) / (1 - beta)
    if veff <= 0:
        return None
    G = lambda v: math.log(v / (a_ + b_ * v)) / a_
    return G(V_ALARM) - G(veff)


det = {}
say("beta | coupled: t_det  delay(predicted)  min V  floor  captured at end | firewalled: t_det  min V")
for beta in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.6, 0.7):
    rec, info, y = simulate(RG, YS0, 600, sub=True, beta=beta, reform={"c": {D: C_REFORM}}, every=2.0)
    recf, infof, yf = simulate(RF, YS0, 600, sub=True, beta=beta, reform={"c": {D: C_REFORM}}, every=2.0)
    det[beta] = (info, infof, rec, recf)
    pred = delay_formula(beta)
    t0 = det[0.0][0]["t_alarm"] if 0.0 in det else info["t_alarm"]
    meas = None if info["t_alarm"] is None else info["t_alarm"] - t0
    say(f"{beta:.2f} | {fmt(info['t_alarm'])}  {fmt(meas)}({fmt(pred)})  {info['minV']:.3f}  "
        f"{'breached' if info['t_floor'] else 'held'}  {names(captured(rec[-1][1]))} | "
        f"{fmt(infof['t_alarm'])}  {infof['minV']:.3f}")
say(f"strict silencing needs beta*x_E >= V_alarm/K = {V_ALARM / K:.2f}")

# ---------------------------------------------------------------------------
say("\n== Feedback into development psi (keystone reform), beta=0 ==")
psi_rows = []
for psi in (0.0, 0.05, 0.10, 0.13, 0.15, 0.20):
    Rg = conv(THETA_GP, psi=psi)
    rec, info, y = simulate(Rg, YS0, 800, sub=True, beta=0.0, reform={"c": {D: C_REFORM}}, every=4.0)
    sD = inbound(Rg, D, range(n)) / C_REFORM
    psi_rows.append((psi, sD, info["minV"], names(captured(rec[-1][1]))))
    say(f"psi={psi:.2f}: reformed s_D over the captured set = {sD:.3f}; min V = {info['minV']:.3f}; captured at t=800: {names(captured(rec[-1][1]))}")
say(f"analytic: the reform holds iff (1.3 + 5 psi)/2 < 1, i.e. psi < {(2 - 1.3) / 5:.2f}")

# ---------------------------------------------------------------------------
say("\n== Entry rate mu: capture times and unwinding after the keystone reform (beta=0) ==")
mu_rows = []
for mu in (1e-3, 1e-4, 1e-6, 1e-8):
    rec, info, y = simulate(RG, YS0, 900, sub=True, beta=0.0, reform={"c": {D: C_REFORM}}, mu=mu)
    tr = info["t_reform"]
    up = [first_cross(rec, i) for i in range(1, n)]
    down = [first_cross(rec, i, above=False, after=tr) for i in range(n)]
    lag = [None if v is None else v - tr for v in down]
    say(f"mu={mu:.0e}: x>0.5 at " + " ".join(f"{SHORT[i + 1]}={fmt(up[i], 0)}" for i in range(5)) +
        f"; alarm {fmt(info['t_alarm'])}; min V {info['minV']:.3f}; x<0.5 after reform at +" +
        " ".join(f"{SHORT[i]}={fmt(lag[i], 0)}" for i in range(n)))
    mu_rows.append((mu, up[P - 1], info["minV"], lag[S]))

# ---------------------------------------------------------------------------
say("\n== Hysteresis in theta ==")
CACHE = "hyst-cache.json"
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
thetas = [round(0.025 + 0.05 * k, 3) for k in range(30)]   # offset grid: no point sits on a threshold


MU_SWEEP = 1e-6   # entry shifts thresholds by order sqrt(mu); 1e-6 keeps the shift below the grid spacing


def sweep(phi, T=1500):
    y = state([0.9] + [0.02] * 5, [1.5] + [0.0] * 5)
    up, down = [], []
    for th in thetas:
        rec, info, y = simulate(conv(th, phi=phi), y, T, every=T, mu=MU_SWEEP)
        up.append((th, sum(1 for v in rec[-1][1][1:] if v > 0.5)))
    for th in reversed(thetas):
        rec, info, y = simulate(conv(th, phi=phi), y, T, every=T, mu=MU_SWEEP)
        down.append((th, sum(1 for v in rec[-1][1][1:] if v > 0.5)))
    return up, down


hyst = {}
for phi in (0.11, 0.22):
    key = f"{phi}"
    if key not in cache:
        cache[key] = sweep(phi)
        json.dump(cache, open(CACHE, "w"))
    up, down = [tuple(p) for p in cache[key][0]], [tuple(p) for p in cache[key][1]]
    hyst[phi] = (up, down)
    first_up = next((th for th, k in up if k > 0), None)
    first_down = next((th for th, k in down if k < 5), None)
    say(f"phi={phi}: capture appears at theta={first_up} (theory: theta>1); first loss on the way down at theta={first_down} "
        f"(theory: below {1 - R_OWN - 4 * phi:.2f})")

# ---------------------------------------------------------------------------
say("\n== Selection for conversion capacity (Props. 2-3) ==")
B0 = to_b(RP)
BH = bhat()
QS = [0.0, 1.0]
GAMMA = 0.05
say(f"incidental conversion = theta {THETA_PRE} field; capacity adds per unit: 0.5 from D into each domain, 0.2 D->D, "
    f"0.1 into D from each domain, 0.05 among and within the others; types q={QS}; cost gamma*q, gamma={GAMMA}")
cap_runs = {}
for chi in (0.8, 0.3, 0.1):
    C = Carriers(QS, chi, GAMMA, B0, BH)
    y = C.init([0.9] + [0.02] * 5, [1.5] + [0.0] * 5)
    rec, y = C.run(y, 500, every=2.0)
    cap_runs[chi] = rec
    x0 = rec[0][1]
    advD0 = advantage(x0, chi, GAMMA, BH, D)
    t_q = next((t for t, x, rho, r in rec if field_mean_q(x, QS) > 0.9), None)
    t_all = next((t for t, x, rho, r in rec if all(sum(x[i]) > 0.5 for i in range(n))), None)
    xe = rec[-1][1]
    advDend = advantage(xe, chi, GAMMA, BH, D)
    say(f"chi={chi}: advantage in D at t=0 = {advD0:+.3f}, at t=500 = {advDend:+.3f}; mean q > 0.9 at t={fmt(t_q, 0)}; "
        f"every domain captured at t={fmt(t_all, 0)}; final mean q = {field_mean_q(xe, QS):.3f}; "
        f"captured at end: {names([i for i in range(n) if sum(xe[i]) > 0.5])}")
say(f"chi threshold in D with only D captured: gamma / sum_j bh_Dj x_j = {GAMMA / (0.2 * 1.0 + 0.1 * 0.0):.2f}")
Rhalf = [[RP[i][j] + 0.5 * BH[i][j] for j in range(n)] for i in range(n)]
rec, info, y = simulate(Rhalf, Y0, 500, every=500)
say(f"counterfactual, capacity frozen at mean 0.5 (conversion b0 + 0.5 bh, cost +0.025): "
    f"captured at t=500: {names(captured(rec[-1][1]))}; inbound from D = {inbound(Rhalf, E, [D]):.2f}")
say(f"cascade needs (theta_pre + 0.5 q) / (1 + gamma q) > 1, i.e. mean q > {(1 - THETA_PRE) / (0.5 - GAMMA):.2f}")

# ---------------------------------------------------------------------------
say("\n== Discrete-time capacity model (Appendix D): Gamma_T = (chi a b / delta) L_T ==")
for T_, delta, chi in ((5, 0.2, 0.5), (20, 0.2, 0.5), (20, 0.8, 0.5), (20, 0.2, 0.1)):
    L = 1 - (1 - (1 - delta) ** T_) / (delta * T_)
    G = chi * L / delta
    # direct accumulation check
    r, acc = 0.0, 0.0
    for t in range(T_):
        acc += chi * r
        r = (1 - delta) * r + 1.0
    say(f"T={T_:2d} delta={delta} chi={chi}: Gamma_T={G:.4f} (direct {acc / T_:.4f}); "
        f"{'favoured' if G > 0.9 else 'disfavoured'} at marginal cost 0.9")

open("checks.log", "w").write("\n".join(LOG) + "\n")

# robustness table (Appendix B)
T = [r"\begin{tabular}{@{}lccc@{}}", r"\toprule",
     r"$\beta$ & $t_{\mathrm{det}}$ & delay (formula) & min $V$ \\", r"\midrule"]
for beta in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.55):
    info = det[beta][0]
    pred = delay_formula(beta)
    meas = info["t_alarm"] - det[0.0][0]["t_alarm"]
    star = r"\textsuperscript{*}" if info["t_floor"] else ""
    T.append(f"{beta:g} & {info['t_alarm']:.1f} & {meas:.1f} ({pred:.1f}) & {info['minV']:.2f}{star} \\\\")
T.append(r"$\ge0.6$ & never & never & $\to0$\textsuperscript{*} \\")
T += [r"\midrule", r"$\psi$ & reformed $s_{\mathsf D}$ & min $V$ & outcome \\", r"\midrule"]
for psi, sD, mv, cap in psi_rows:
    T.append(f"{psi:g} & {sD:.3f} & {mv:.2f} & {'unwound' if cap == 'none' else 'stays captured'} \\\\")
T += [r"\midrule", r"$\mu$ & $\mathsf P$ captured & min $V$ & $\mathsf S$ unwound \\", r"\midrule"]
for mu, tp, mv, ls in mu_rows:
    e = int(round(math.log10(mu)))
    T.append(f"$10^{{{e}}}$ & {tp:.0f} & {mv:.3f} & +{ls:.0f} \\\\")
T += [r"\bottomrule", r"\end{tabular}"]
open("tab-robust.tex", "w").write("\n".join(T) + "\n")

# ---------------------------------------------------------------------------
# pgfplots output
COL = ["cD", "cE", "cS", "cP", "cF", "cI"]
STY = ["thick", "very thick", "thick, densely dashed", "thick, dashdotted", "very thick, dotted", "thick, loosely dashed"]


def pts(series, step=1):
    s = series[::step]
    if series and s[-1] != series[-1]:
        s.append(series[-1])
    return " ".join(f"({t:.0f},{v:.4f})" for t, v in s)


# Figure: capacity
out = [r"\begin{tikzpicture}",
       r"\begin{groupplot}[group style={group size=2 by 1, horizontal sep=0.95cm}, width=0.555\columnwidth, height=3.5cm,",
       r"  xmin=0, xmax=500, xtick={0,250,500}, tick label style={font=\scriptsize}, label style={font=\scriptsize},",
       r"  title style={font=\scriptsize, yshift=-1ex}, xlabel={time}]"]
CHI_STY = {0.8: ("cD", "very thick"), 0.3: ("cE", "thick, densely dashed"), 0.1: ("cF", "thick, dotted")}
out.append(r"\nextgroupplot[title={(a) Mean capacity $\bar q$}, ymin=-0.03, ymax=1.05, ytick={0,0.5,1}]")
for chi, rec in cap_runs.items():
    col, sty = CHI_STY[chi]
    out.append(r"\addplot[%s, %s] coordinates {%s};" % (col, sty, pts([(t, field_mean_q(x, QS)) for t, x, rho, r in rec], 3)))
    out.append(r"\label{pl:chi%s}" % str(chi).replace(".", ""))
out.append(r"\nextgroupplot[title={(b) Domains captured}, ymin=-0.2, ymax=6.3, ytick={0,2,4,6}]")
for chi, rec in cap_runs.items():
    col, sty = CHI_STY[chi]
    out.append(r"\addplot[%s, %s, const plot] coordinates {%s};" % (
        col, sty, pts([(t, sum(1 for i in range(n) if sum(x[i]) > 0.5)) for t, x, rho, r in rec], 1)))
out += [r"\end{groupplot}", r"\end{tikzpicture}"]
open("fig-capacity.tex", "w").write("\n".join(out) + "\n")

# Figure: field
TMAX = 300
out = [r"\begin{tikzpicture}",
       r"\begin{groupplot}[group style={group size=4 by 1, horizontal sep=1.15cm}, width=4.55cm, height=3.5cm,",
       r"  tick label style={font=\scriptsize}, label style={font=\scriptsize}, title style={font=\scriptsize, yshift=-1ex},",
       r"  every axis plot/.append style={line join=round}]"]
for k, (lab, rec) in enumerate((("(a) Coupled field", runs["theta=1.2"]), ("(b) Selectors firewalled", runs["firewalled"]))):
    opts = "title={%s}, xmin=0, xmax=%d, ymin=-0.03, ymax=1.05, xtick={0,100,200,300}, ytick={0,0.5,1}, xlabel={time}" % (lab, TMAX)
    if k == 0:
        opts += ", ylabel={share $x_i$}"
    out.append(r"\nextgroupplot[%s]" % opts)
    for i in range(n):
        out.append(r"\addplot[%s, %s] coordinates {%s};" % (
            COL[i], STY[i], pts([(t, x[i]) for t, x, r, V in rec if t <= TMAX], 4)))
        if k == 0:
            out.append(r"\label{pl:%s}" % SHORT[i])
# (c) condition and observation at beta = 0.3
info, infof, rec, recf = det[0.3]
out.append(r"\nextgroupplot[title={(c) Condition, $\beta=0.3$}, xmin=0, xmax=%d, ymin=0, ymax=1.05, xtick={0,100,200,300}, ytick={0,0.5,1}, xlabel={time}, ylabel={condition}]" % TMAX)
out.append(r"\addplot[gray, thin, dashed, domain=0:%d] {%.2f};" % (TMAX, V_ALARM))
out.append(r"\addplot[cH, thin, dotted, domain=0:%d] {%.2f};" % (TMAX, V_MIN))
out.append(r"\addplot[black, very thick] coordinates {%s};" % pts([(t, V) for t, x, r, V in rec if t <= TMAX], 2))
out.append(r"\label{pl:V}")
out.append(r"\addplot[cE, very thick, densely dashed] coordinates {%s};" % pts(
    [(t, V + 0.3 * x[E] * (K - V)) for t, x, r, V in rec if t <= TMAX], 2))
out.append(r"\label{pl:y}")
out.append(r"\addplot[cS, thick, dashdotted] coordinates {%s};" % pts([(t, V) for t, x, r, V in recf if t <= TMAX], 2))
out.append(r"\label{pl:Vf}")
for ta in (infof["t_alarm"], info["t_alarm"]):
    out.append(r"\draw[->, thin] (axis cs:%.0f,0.2) -- (axis cs:%.0f,0.5);" % (ta, ta))
# (d) detection time against beta
out.append(r"\nextgroupplot[title={(d) Detection time}, xmin=0, xmax=0.7, ymin=0, ymax=520, xtick={0,0.3,0.6}, ytick={0,250,500}, xlabel={masking $\beta$}, ylabel={$t_{\mathrm{det}}$}]")
bet = sorted(det)
out.append(r"\addplot[cE, very thick, mark=*, mark size=0.9pt] coordinates {%s};" % " ".join(
    f"({b},{det[b][0]['t_alarm']:.1f})" for b in bet if det[b][0]["t_alarm"] is not None))
out.append(r"\label{pl:detc}")
out.append(r"\addplot[cS, thick, dashdotted, mark=square*, mark size=0.8pt] coordinates {%s};" % " ".join(
    f"({b},{det[b][1]['t_alarm']:.1f})" for b in bet if det[b][1]["t_alarm"] is not None))
out.append(r"\label{pl:detf}")
out.append(r"\addplot[gray, thin, dotted] coordinates {(0.6,0) (0.6,520)};")
out.append(r"\node[font=\tiny, anchor=west] at (axis cs:0.605,150) {never};")
out += [r"\end{groupplot}", r"\end{tikzpicture}"]
open("fig-field.tex", "w").write("\n".join(out) + "\n")

# Figure: hysteresis (appendix)
h = [r"\begin{tikzpicture}",
     r"\begin{groupplot}[group style={group size=2 by 1, horizontal sep=0.55cm, y descriptions at=edge left}, width=0.565\columnwidth, height=3.6cm,",
     r"  xmin=0, xmax=1.5, ymin=-0.3, ymax=5.6, xtick={0,0.5,1,1.5}, ytick={0,1,2,3,4,5},",
     r"  xlabel={conversion from development $\theta$}, tick label style={font=\scriptsize}, label style={font=\scriptsize}, title style={font=\scriptsize, yshift=-1ex}]"]
for k, phi in enumerate((0.11, 0.22)):
    up, down = hyst[phi]
    opts = "title={(%s) $\\varphi=%.2f$}" % ("ab"[k], phi)
    if k == 0:
        opts += ", ylabel={domains captured}"
    h.append(r"\nextgroupplot[%s]" % opts)
    h.append(r"\addplot[gray, thin, dotted] coordinates {(1,-0.3) (1,5.6)};")
    thr = 1 - R_OWN - 4 * phi
    if thr > 0:
        h.append(r"\addplot[gray, thin, dotted] coordinates {(%.2f,-0.3) (%.2f,5.6)};" % (thr, thr))
    h.append(r"\addplot[cD, thick, mark=*, mark size=1.1pt] coordinates {%s};" % " ".join(f"({th},{c})" for th, c in up))
    if k == 0:
        h.append(r"\label{pl:up}")
    h.append(r"\addplot[cH, thick, densely dashed, mark=o, mark size=1.3pt] coordinates {%s};" % " ".join(
        f"({th},{c})" for th, c in reversed(down)))
    if k == 0:
        h.append(r"\label{pl:down}")
h += [r"\end{groupplot}", r"\end{tikzpicture}"]
open("fig-hysteresis.tex", "w").write("\n".join(h) + "\n")
print("\nwrote checks.log, fig-capacity.tex, fig-field.tex, fig-hysteresis.tex, tab-robust.tex")
