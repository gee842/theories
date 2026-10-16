"""Numerical checks and figure data for v3 of the paper (pure Python, no dependencies).

Writes fig-rate.tex (pgfplots) and checks.log next to this file.
"""
import math, os
here = os.path.dirname(os.path.abspath(__file__))
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

# ---------- Proposition 2: weight on winning ----------
def game(n, lam, theta):
    w = 1 + lam*(n-1)/n
    return ("deplete" if w > theta/n else "restrain"), w
say("Prop 2 checks (theta = omega K h/(rho nu)):")
for theta in (3.0, 8.0):
    for n in (2, 4, 10):
        lam_bar = (theta-n)/(n-1)
        say(f"  theta={theta} n={n}: lambda_bar={lam_bar:.3f};",
            ", ".join(f"lam={l}:{game(n,l,theta)[0]}" for l in (0, 1, 3, 10)))
# brute-force best response check for a symmetric linear game
def u_k(ek, others, n, lam, nu=1.0, omega=1.0, K=1.0, h=0.5, rho=1.0):
    es = [ek]+others
    E = sum(es)/n
    V = K*(1-h*E/rho)
    pis = [nu*e + omega*V for e in es]
    return pis[0] + lam*(pis[0]-sum(pis)/n)
ok = True
for n in (2,3,5):
    for lam in (0, 0.5, 2, 6):
        theta = 1.0*1.0*0.5/(1.0*1.0)  # omega K h/(rho nu) = 0.5
        for others in ([0.0]*(n-1), [1.0]*(n-1)):
            best = max((u_k(e/10, others, n, lam), e/10) for e in range(11))[1]
            pred = 1.0 if (1+lam*(n-1)/n) > theta/n else 0.0
            ok &= abs(best-pred) < 1e-9
say("  brute-force best responses match the dominant-strategy formula:", ok)

# ---------- Proposition 5: required independent correction ----------
def dstar(A, Z, cE=1.0):
    return (A + math.sqrt(A*A + 4*cE*Z))/(2*cE)
def sE(d, aE, B0, Bh, chi, Yh, gam, cE=1.0):
    q = chi*Yh/(gam*d)
    return aE*(B0 + q*Bh)/(cE*d)
aE, B0, Bh, chi, Yh, gam0, cE = 1.0, 0.3, 0.5, 0.8, 1.0, 1.0, 1.0
A = aE*B0; Z0 = aE*Bh*chi*Yh/gam0
d0 = dstar(A, Z0)
say(f"Prop 5: d*(0)={d0:.4f}, naive requirement A/cE={A/cE:.4f}")
for d in (d0*0.999, d0*1.001):
    say(f"  s_E at d={d:.4f}: {sE(d,aE,B0,Bh,chi,Yh,gam0):.5f}")
g = 0.2; dinit = 1.0
S = math.sqrt(Z0/cE)
def crossing(alpha, T=60, dt=0.001):
    t = 0.0
    while t < T:
        if dinit*math.exp(alpha*t) <= dstar(A, Z0*math.exp(g*t)):
            return t
        t += dt
    return None
for alpha in (0.05, 0.08, 0.10, 0.12):
    tc = crossing(alpha)
    bound = max(0.0, 2*math.log(dinit/S)/(g-2*alpha)) if alpha < g/2 else None
    say(f"  alpha={alpha}: certificate fails at t={tc if tc is None else round(tc,3)}; bound t*={bound if bound is None else round(bound,3)}"
        + ("" if alpha < g/2 else f"; sufficient condition d(0)>=A/cE+S={A/cE+S:.4f}: {dinit >= A/cE+S}"))

# fragmentation: k equal parts of a carrier with share s, quadratic return
s = 0.6
for k in (1, 2, 4):
    total = k*(s/k)**2
    say(f"  fragmentation k={k}: cultivated conversion proportional to {total:.4f}")

# ---------- Proposition 6: silent descent ----------
K, Vmin, Valarm = 1.0, 0.3, 0.6
mfloor = (Valarm-Vmin)/(K-Vmin)
say(f"Prop 6: m_floor=(Valarm-Vmin)/(K-Vmin)={mfloor:.4f}")
rho, h, nu = 0.05, 0.08, 0.08
def logistic(t, mid, rate):
    return 1/(1+math.exp(-rate*(t-mid)))
def run(beta_in, beta_out=0.05, tcap=20.0, T=160.0, dt=0.01):
    V = 1.0; t = 0.0; talarm = None; tfloor = None; tA = None
    pts = []
    while t <= T:
        E = logistic(t, 30.0, 0.15)      # race strategy spreading (share of depleting activity)
        xE = logistic(t, tcap, 0.25)      # evaluation captured around tcap
        m = beta_in*xE + beta_out*(1-xE)
        Vt = V + m*(K-V)
        if tA is None and V <= Valarm: tA = t
        if talarm is None and Vt <= Valarm: talarm = t
        if tfloor is None and V <= Vmin: tfloor = t
        pts.append((t, V, Vt))
        V += dt*V*(rho*(1-V/K) - h*E)
        t += dt
    return pts, tA, talarm, tfloor
res = {}
for b in (0.0, 0.3, 0.5):
    pts, tA, ta, tf = run(b, beta_out=(0.0 if b == 0.0 else 0.05))
    res[b] = (pts, tA, ta, tf)
    say(f"  capture at t=20, beta_in={b}: V reaches alarm level at t={tA:.1f}; alarm fires at t={'never' if ta is None else round(ta,1)}; floor crossed at t={tf:.1f}")
for b in (0.3, 0.5):
    _, tA2, ta2, tf2 = run(b, tcap=45.0)
    say(f"  capture at t=45 (after the alarm level), beta_in={b}: alarm fires at t={'never' if ta2 is None else round(ta2,1)}; floor crossed at t={tf2:.1f}")

# ---------- figure ----------
def coords(seq):
    return " ".join(f"({x:.2f},{y:.4f})" for x, y in seq)
ts = [i*0.5 for i in range(0, 81)]
dstar_pts = [(t, dstar(A, Z0*math.exp(g*t))) for t in ts]
low = [(t, dinit*math.exp(0.05*t)) for t in ts]
high = [(t, dinit*math.exp(0.12*t)) for t in ts]
pts, tA, ta0, tf = res[0.0]
_, _, ta3, _ = res[0.3]
_, _, ta5, _ = res[0.5]
sub = [p for i, p in enumerate(pts) if i % 100 == 0]
Vline = [(t, V) for t, V, _ in sub]
V5 = [(t, Vt) for t, _, Vt in res[0.5][0][::100]]
V3 = [(t, Vt) for t, _, Vt in res[0.3][0][::100]]
tc = crossing(0.05)
fig = r"""\begin{tikzpicture}
\begin{groupplot}[group style={group size=2 by 1, horizontal sep=1.1cm}, width=0.6\columnwidth, height=0.5\columnwidth,
  tick label style={font=\scriptsize}, label style={font=\scriptsize}, title style={font=\scriptsize}]
\nextgroupplot[ymode=log, xmin=0, xmax=40, ymin=0.7, ymax=60, xlabel={time}, ylabel={correction rate}, title={(a) required vs.\ supplied}]
\addplot[cE, very thick] coordinates {%s};\label{pl:dstar}
\addplot[cD, thick, dashed] coordinates {%s};\label{pl:dlow}
\addplot[cS, thick, dashdotted] coordinates {%s};\label{pl:dhigh}
\draw[black!60] (axis cs:%.2f,0.7) -- (axis cs:%.2f,60);
\node[font=\tiny, anchor=north west] at (axis cs:%.2f,55) {$t^\ast$};
\nextgroupplot[xmin=0, xmax=160, ymin=0, ymax=1.02, xlabel={time}, ylabel={condition}, title={(b) silent descent}]
\addplot[black, very thick] coordinates {%s};\label{pl:Vtrue}
\addplot[cE, thick, dashed] coordinates {%s};\label{pl:V5}
\addplot[cP, thick, dashdotted] coordinates {%s};\label{pl:V3}
\draw[black!50, densely dashed] (axis cs:0,0.6) -- (axis cs:160,0.6);
\draw[black!50, dotted, thick] (axis cs:0,0.3) -- (axis cs:160,0.3);
\draw[-{Stealth[length=4pt]}, black] (axis cs:%.1f,0.85) -- (axis cs:%.1f,0.62);
\draw[-{Stealth[length=4pt]}, cP] (axis cs:%.1f,0.85) -- (axis cs:%.1f,0.62);
\draw[-{Stealth[length=4pt]}, cE] (axis cs:%.1f,0.85) -- (axis cs:%.1f,0.62);
\draw[black!70] (axis cs:%.1f,0.22) -- (axis cs:%.1f,0.38);
\end{groupplot}
\end{tikzpicture}
""" % (coords(dstar_pts), coords(low), coords(high), tc, tc, tc+0.5,
       coords(Vline), coords(V5), coords(V3), tA, tA, ta3, ta3, ta5, ta5, tf, tf)
open(os.path.join(here, "fig-rate.tex"), "w").write(fig)
say(f"figure: t*={tc:.2f}; independent alarm t={tA:.1f}; beta_in=0.3 alarm t={ta3:.1f}; beta_in=0.5 alarm {'never' if ta5 is None else round(ta5,1)}; floor t={tf:.1f}")
open(os.path.join(here, "checks.log"), "w").write("\n".join(log)+"\n")
