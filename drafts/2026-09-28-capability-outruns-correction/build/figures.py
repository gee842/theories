"""Figure data and numerical checks for "When Capability Outruns Correction", v2.

Writes the four pgfplots figures (fig-*.tex) beside this script and prints the checks the text relies on.
Pure Python (no dependencies); fourth-order Runge-Kutta. Run: python3 figures.py
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Running example (Section 3 onward)
P0 = dict(a=1.0, b=1.0, c=0.4, d=1.0, kap=1.0, eps=0.2, rho=1.0, K=1.0, h=1.5)
V_MIN, V_ALARM = 0.3, 0.6
Y0 = (0.5, 0.5, 1.0)
# Four reforms, each taking R_cap from 2.5 to 0.8
LEVERS = [("c", r"raise $c$ (margin)", dict(c=1.25), "cC", "solid"),
          ("a", r"lower $a$ (margin)", dict(a=0.32), "cA", "densely dashed"),
          ("d", r"raise $d$ (decay)", dict(d=3.125), "cD", "dashdotted"),
          ("b", r"lower $b$ (flow)", dict(b=0.32), "cB", "densely dotted")]


def rk4(f, y, dt):
    k1 = f(y)
    k2 = f([a + dt / 2 * b for a, b in zip(y, k1)])
    k3 = f([a + dt / 2 * b for a, b in zip(y, k2)])
    k4 = f([a + dt * b for a, b in zip(y, k3)])
    return [a + dt / 6 * (p + 2 * q + 2 * s + u) for a, p, q, s, u in zip(y, k1, k2, k3, k4)]


def field(P):
    def f(y):
        x, r, V = y[0], y[1], y[2] if len(y) > 2 else 1.0
        out = [P['kap'] * x * (1 - x) * (P['a'] * r - P['c']), P['eps'] * (P['b'] * x - P['d'] * r)]
        if len(y) > 2:
            out.append(V * (P['rho'] * (1 - V / P['K']) - P['h'] * x))
        return out
    return f


def rcap(P):
    return P['a'] * P['b'] / (P['c'] * P['d'])


def fate(P, x0, r0, T=400.0, dt=0.02):
    f, y = field(P), [x0, r0]
    for _ in range(int(T / dt)):
        y = rk4(f, y, dt)
        if y[0] < 1e-5:
            return "L"
        if y[0] > 1 - 1e-5:
            return "H"
    return "?"


def separatrix(P, box_r=1.6, dt=0.002):
    """Stable manifold of S by backward integration along the stable eigenvector."""
    xs, rs = P['c'] * P['d'] / (P['a'] * P['b']), P['c'] / P['a']
    j12, j21, j22 = P['kap'] * P['a'] * xs * (1 - xs), P['eps'] * P['b'], -P['eps'] * P['d']
    lam = (j22 - math.sqrt(j22 * j22 + 4 * j12 * j21)) / 2      # stable eigenvalue (j11 = 0)
    v = (j12, lam)                                             # (J - lam I) v = 0
    n = math.hypot(*v); v = (v[0] / n, v[1] / n)
    fb = field(P)
    back = lambda y: [-z for z in fb(y)]
    branches = []
    for sgn in (1, -1):
        y = [xs + sgn * 1e-6 * v[0], rs + sgn * 1e-6 * v[1]]
        pts = []
        while 0 <= y[0] <= 1 and 0 <= y[1] <= box_r:
            pts.append(tuple(y)); y = rk4(back, y, dt)
        branches.append(pts)
    pts = list(reversed(branches[0])) + [(xs, rs)] + branches[1]
    return sorted(pts, key=lambda p: p[1])


def x_sep(sep, r):
    """Separatrix as x = x_sep(r) (a decreasing graph: the system is cooperative)."""
    if r <= sep[0][1]:
        return sep[0][0]
    for (x1, r1), (x2, r2) in zip(sep, sep[1:]):
        if r1 <= r <= r2:
            return x1 + (x2 - x1) * (r - r1) / (r2 - r1) if r2 > r1 else x1
    return sep[-1][0]


def simulate(P, lever=None, tau=0.0, mu=0.0, T=30.0, dt=0.005, keep=False):
    """Reform fires when the delayed, capture-flattered observation of V reaches V_ALARM."""
    P = dict(P); f = field(P); r_H = P['b'] / P['d']
    y, hist, fired, minV = list(Y0), [list(Y0)], None, 1.0
    lag = int(round(tau / dt)); t = 0.0; traj = [(0.0, *y)]
    for i in range(int(T / dt)):
        if lever is not None and fired is None:
            xd, rd, Vd = hist[max(0, len(hist) - 1 - lag)]
            beta = mu * min(1.0, rd / r_H)
            if Vd + beta * (P['K'] - Vd) <= V_ALARM:
                P.update(lever); f = field(P); fired = t
        y = rk4(f, y, dt); t += dt; hist.append(list(y)); minV = min(minV, y[2])
        if keep and i % 10 == 9:
            traj.append((t, *y))
    return fired, minV, traj


def coords(pts, nd=4):
    return " ".join(f"({p[0]:.{nd}f},{p[1]:.{nd}f})" for p in pts)


def write(name, body):
    with open(os.path.join(HERE, name), "w") as fh:
        fh.write(body)


def fig_phase():
    P = dict(P0); sep = separatrix(P)
    starts = [(0.95, 0.02), (0.8, 0.02), (0.7, 0.02), (0.64, 0.02), (0.5, 0.02), (0.02, 1.55), (0.01, 1.55),
              (0.2, 1.2), (0.02, 0.9), (0.97, 0.3), (0.12, 0.45)]
    lines = []
    f = field(P)
    for x0, r0 in starts:
        y = [x0, r0]; pts = [tuple(y)]
        for i in range(6000):
            y = rk4(f, y, 0.02)
            if i % 5 == 4:
                pts.append(tuple(y))
            if min(abs(y[0]), abs(y[1])) < 1e-3 and y[0] < 1e-3 or (y[0] > 0.999 and abs(y[1] - 1) < 0.01):
                break
        dest = "cL" if y[0] < 0.5 else "cH"
        lines.append(rf"\addplot[{dest}, thin, -{{Stealth[length=4pt]}}] coordinates {{{coords(pts[:: max(1, len(pts) // 40)] + [pts[-1]], 3)}}};")
    body = r"""\begin{tikzpicture}
\begin{axis}[width=0.66\linewidth, height=0.52\linewidth, xmin=0, xmax=1, ymin=0, ymax=1.6,
  xlabel={share of the practice, $x$}, ylabel={rule support, $r$}, tick label style={font=\small},
  label style={font=\small}, clip=true]
\fill[cL, opacity=0.10] (axis cs:0,0) rectangle (axis cs:0.4,0.4);
\fill[cH, opacity=0.10] (axis cs:0.4,0.4) rectangle (axis cs:1,1.6);
\addplot[gray, dashed, domain=0:1, samples=2] {x};
\addplot[gray, dotted, thick, domain=0:1, samples=2] {0.4};
""" + "\n".join(lines) + rf"""
\addplot[black, very thick] coordinates {{{coords(sep[:: max(1, len(sep) // 120)] + [sep[-1]], 4)}}};
\addplot[only marks, mark=*, mark size=2pt] coordinates {{(0,0) (1,1)}};
\addplot[only marks, mark=*, mark options={{fill=white}}, mark size=2pt] coordinates {{(0.4,0.4)}};
\node[anchor=south west, font=\small] at (axis cs:0.005,0.005) {{$L$}};
\node[anchor=north east, font=\small] at (axis cs:0.995,0.995) {{$H$}};
\node[anchor=north west, font=\small] at (axis cs:0.41,0.395) {{$S$}};
\node[font=\scriptsize, gray, rotate=38] at (axis cs:0.83,0.88) {{$\dot r=0$}};
\node[font=\scriptsize, gray, anchor=south] at (axis cs:0.9,0.4) {{$\dot x=0$}};
\end{{axis}}
\end{{tikzpicture}}
"""
    write("fig-phase.tex", body)
    return sep


def fig_levers():
    cur = {}
    for key, label, lev, col, sty in LEVERS:
        fired, minV, traj = simulate(P0, lev, T=10.0, keep=True)
        cur[key] = (label, col, sty, traj, fired, minV)
    _, _, none_traj = simulate(P0, None, T=10.0, keep=True)
    t_ref = cur["c"][4]

    def panel(idx, ylabel, ymax, extra):
        out = [rf"\nextgroupplot[ylabel={{{ylabel}}}, ymin=0, ymax={ymax}]"]
        out.append(rf"\addplot[gray!70, very thick] coordinates {{{coords([(p[0], p[idx]) for p in none_traj[::5]], 3)}}};")
        if idx == 1:
            out.append(r"\addlegendentry{no reform}")
        for key, (label, col, sty, traj, fired, minV) in cur.items():
            out.append(rf"\addplot[{col}, {sty}, thick] coordinates {{{coords([(p[0], p[idx]) for p in traj[::5]], 3)}}};")
            if idx == 1:
                out.append(rf"\addlegendentry{{{label}}}")
        out.append(extra)
        out.append(rf"\draw[black!50, thin] (axis cs:{t_ref:.3f},0) -- (axis cs:{t_ref:.3f},{ymax});")
        return "\n".join(out)

    body = r"""\begin{tikzpicture}
\begin{groupplot}[group style={group size=2 by 1, horizontal sep=1.5cm}, width=0.47\linewidth, height=0.38\linewidth,
  xmin=0, xmax=10, xlabel={time}, tick label style={font=\small}, label style={font=\small},
  legend cell align=left, legend columns=5, legend style={font=\scriptsize, at={(1.12,-0.3)}, anchor=north, draw=none, /tikz/every even column/.append style={column sep=6pt}}]
""" + panel(1, r"share $x$", 1.0, "") + "\n" + panel(3, r"substrate $V$", 1.0,
        r"\addplot[black, dashed, domain=0:10, samples=2] {0.3}; \node[font=\scriptsize, anchor=south east] at (axis cs:10,0.3) {$V_{\min}$};") + r"""
\end{groupplot}
\end{tikzpicture}
"""
    write("fig-levers.tex", body)
    return cur


def fig_chain():
    taus = [i * 0.1 for i in range(21)]
    mus = [i * 0.05 for i in range(17)]
    res_tau, res_mu = {}, {}
    for key, label, lev, col, sty in LEVERS:
        res_tau[key] = [(t, simulate(P0, lev, tau=t)[1]) for t in taus]
        res_mu[key] = [(m, simulate(P0, lev, mu=m)[1]) for m in mus]

    def panel(res, xlabel, xmax, legend):
        out = [rf"\nextgroupplot[xlabel={{{xlabel}}}, xmin=0, xmax={xmax}]"]
        for key, label, lev, col, sty in LEVERS:
            out.append(rf"\addplot[{col}, {sty}, thick] coordinates {{{coords(res[key], 3)}}};")
            if legend:
                out.append(rf"\addlegendentry{{{label}}}")
        out.append(rf"\addplot[black, dashed, domain=0:{xmax}, samples=2] {{0.3}};")
        return "\n".join(out)

    body = r"""\begin{tikzpicture}
\begin{groupplot}[group style={group size=2 by 1, horizontal sep=1.5cm}, width=0.47\linewidth, height=0.38\linewidth,
  ymin=0.15, ymax=0.55, ylabel={lowest substrate level, $\min_t V$}, tick label style={font=\small}, label style={font=\small},
  legend cell align=left, legend style={font=\scriptsize, at={(0.02,0.02)}, anchor=south west, draw=none, fill=white, fill opacity=0.8, text opacity=1}]
""" + panel(res_tau, r"observation and decision delay, $\tau$", 2.0, True) + "\n" + panel(res_mu, r"masking at full capture, $\mu$", 0.8, False) + r"""
\end{groupplot}
\end{tikzpicture}
"""
    write("fig-chain.tex", body)
    return res_tau, res_mu


def fig_coalition(sep):
    x0, P = 0.95, dict(P0)
    rs = [i * 0.02 for i in range(76)]
    nopause = [(r, max(0.0, x0 - x_sep(sep, r))) for r in rs]
    ordinary = x0 - 1 / rcap(P)
    insulated = x0 - x_sep(sep, 0.0)
    body = rf"""\begin{{tikzpicture}}
\begin{{axis}}[width=0.62\linewidth, height=0.45\linewidth, xmin=0, xmax=1.5, ymin=0, ymax=1,
  xlabel={{inherited rule support, $r_0$}}, ylabel={{minimal exiting share, $s^\ast$}}, tick label style={{font=\small}},
  label style={{font=\small}}, legend cell align=left, legend style={{font=\scriptsize, at={{(0.98,0.03)}}, anchor=south east, draw=none, fill=white, fill opacity=0.8, text opacity=1}}]
\addplot[cH, very thick] coordinates {{{coords(nopause, 3)}}};
\addlegendentry{{restraint alone}}
\addplot[cD, thick, dashdotted, domain=0:1.5, samples=2] {{{ordinary:.4f}}};
\addlegendentry{{restraint + pause, ordinary rule-making}}
\addplot[cL, thick, densely dashed, domain=0:1.5, samples=2] {{{insulated:.4f}}};
\addlegendentry{{restraint + pause, insulated rule-making}}
\draw[black!50, thin] (axis cs:0.4,0) -- (axis cs:0.4,1);
\node[font=\scriptsize, anchor=north west] at (axis cs:0.4,0.99) {{$r_0=c/a$}};
\end{{axis}}
\end{{tikzpicture}}
"""
    write("fig-coalition.tex", body)
    return nopause, ordinary, insulated


def main():
    P = dict(P0)
    print(f"R_cap = {rcap(P)}; S = ({1 / rcap(P)}, {P['c'] / P['a']})")
    sep = fig_phase()
    print("separatrix x_sep(r):", [(r, round(x_sep(sep, r), 4)) for r in (0, 0.2, 0.4, 0.6, 1.0, 1.5)])
    for (x0, r0) in [(0.39, 0.39), (0.1, 0.05), (0.41, 0.41), (0.9, 1.5)]:
        print(f"  quadrant check ({x0},{r0}) -> {fate(P, x0, r0)}")
    cur = fig_levers()
    for key, (label, col, sty, traj, fired, minV) in cur.items():
        print(f"lever {key}: reform at t={fired:.3f}, min V = {minV:.3f}, floor crossed: {minV < V_MIN}")
    r0 = next(p for p in cur['b'][3] if p[0] >= cur['b'][4])[2]
    for key, deff in (("d", 3.125), ("b", 1.0)):
        print(f"  latency lower bound {key}: ln(a r0/c)/(eps d_eff) = {math.log(P['a'] * r0 / P['c']) / (P['eps'] * deff):.3f}")
    res_tau, res_mu = fig_chain()
    for key in res_tau:
        ok = [t for t, m in res_tau[key] if m >= V_MIN]
        okm = [u for u, m in res_mu[key] if m >= V_MIN]
        print(f"lever {key}: largest delay keeping V >= V_min: {max(ok) if ok else 'none'}; largest masking: {max(okm) if okm else 'none'}")
    nopause, ordinary, insulated = fig_coalition(sep)
    print(f"coalition (x0=0.95): restraint alone s*(r0=1.0) = {dict(nopause)[1.0]:.3f}; ordinary pause {ordinary:.3f}; insulated pause {insulated:.3f}")
    for xp, r0, T, bp in [(0.3, 1.2, 40, 1.0), (0.6, 0.1, 40, 1.0), (0.6, 0.1, 40, 0.0), (0.649, 1.0, 40, 0.0)]:
        rT = bp * xp / P['d'] + (r0 - bp * xp / P['d']) * math.exp(-P['eps'] * P['d'] * T)
        print(f"  pause x_p={xp}, r0={r0}, T={T}, b_pause={bp}: before {fate(P, xp, r0)}, after {fate(P, xp, rT)}")


if __name__ == "__main__":
    main()
