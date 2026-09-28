"""Numerical checks of the dynamical claims in 'When Capability Outruns Correction' (2026-09-28).

Model (eqs. 1 and 3 of the paper):
    x' = kap * x(1-x)(a r - c)          share of practice E
    r' = eps * (b x - d r)              rule support favouring E
    V' = V [rho (1 - V/K) - h x]        common substrate
Pure Python, fourth-order Runge-Kutta. Run: python3 check_models.py
"""
import math
import random

BASE = dict(a=1.0, b=1.0, c=0.5, d=1.0, kap=1.0, eps=0.2, rho=1.0, K=1.0, h=0.5)


def rk4(f, y, t, dt):
    k1 = f(t, y)
    k2 = f(t + dt / 2, [yi + dt / 2 * ki for yi, ki in zip(y, k1)])
    k3 = f(t + dt / 2, [yi + dt / 2 * ki for yi, ki in zip(y, k2)])
    k4 = f(t + dt, [yi + dt * ki for yi, ki in zip(y, k3)])
    return [yi + dt / 6 * (p + 2 * q + 2 * s + u) for yi, p, q, s, u in zip(y, k1, k2, k3, k4)]


def field(P):
    def f(t, y):
        x, r, V = y
        return [P['kap'] * x * (1 - x) * (P['a'] * r - P['c']),
                P['eps'] * (P['b'] * x - P['d'] * r),
                V * (P['rho'] * (1 - V / P['K']) - P['h'] * x)]
    return f


def run(P, y0, T, dt, events=None):
    """Integrate; each event is dict(when=pred(t, y), set={param: value}) and fires once."""
    f, y, t, traj = field(P), list(y0), 0.0, [(0.0, *y0)]
    while t < T:
        for ev in events or []:
            if 'at' not in ev and ev['when'](t, y):
                P.update(ev['set']); f = field(P); ev['at'] = (t, list(y))
        y = rk4(f, y, t, dt); t += dt
        traj.append((t, *y))
    return traj


def r_cap(P):
    return P['a'] * P['b'] / (P['c'] * P['d'])


def phi(P, x, r):
    return P['a'] * x * r - P['c'] * x - P['a'] * P['d'] / (2 * P['b']) * r * r


def main():
    print("1. R_cap < 1: every start with 0<x<1 converges to (0,0)")
    P = dict(BASE, c=1.5)
    random.seed(1)
    worst = max(sum(abs(v) for v in run(dict(P), [random.uniform(.01, .99), random.uniform(0, 5), 1], 300, .02)[-1][1:3])
                for _ in range(200))
    print(f"   R_cap = {r_cap(P):.3f}; max |x|+|r| at t=300 over 200 random starts (r0 up to 5): {worst:.1e}")

    print("2. R_cap > 1: bistability; the potential Phi never decreases")
    P = dict(BASE)
    random.seed(2)
    toL = toH = other = drops = 0
    for _ in range(300):
        tr = run(dict(P), [random.uniform(.01, .99), random.uniform(0, 2), 1], 300, .02)
        xe = tr[-1][1]
        toL += xe < 1e-3; toH += xe > 1 - 1e-3; other += 1e-3 <= xe <= 1 - 1e-3
        ph = [phi(P, s[1], s[2]) for s in tr[::10]]
        drops += sum(ph[i] < ph[i - 1] - 1e-9 for i in range(1, len(ph)))
    print(f"   R_cap = {r_cap(P)}; S = (0.5, 0.5); 300 random starts -> L: {toL}, H: {toH}, other: {other}; Phi decreases: {drops}")
    for r0 in (0.3, 0.7):
        print(f"   path dependence: x0 = 0.55, r0 = {r0} -> x(300) = {run(dict(P), [.55, r0, 1], 300, .02)[-1][1]:.4f}")

    print("3. Substrate under capture (x -> 1)")
    for h in (1.5, 1.0, 0.5):
        Q = dict(BASE, h=h)
        tr = run(Q, [.9, 1, 1], 400, .02)
        limit = "0" if h >= Q['rho'] else f"{Q['K'] * (1 - h / Q['rho']):.3f}"
        print(f"   h = {h}: V(100) = {tr[5000][3]:.4f}, V(400) = {tr[-1][3]:.5f}; predicted limit {limit}")

    print("4. Transition path: reform to R_cap = 0.67 when V reaches 0.6; functional floor V_min = 0.3")
    for name, change in [("raise c 0.5 -> 1.5 (liability)", dict(c=1.5)),
                         ("raise d 1 -> 3 (rule sunset)", dict(d=3.0)),
                         ("no reform", None)]:
        Q = dict(BASE, h=1.5)
        ev = [dict(when=lambda t, y: y[2] <= 0.6, set=change)] if change else []
        tr = run(Q, [.6, .6, 1], 250, .01, ev)
        minV = min(s[3] for s in tr)
        cross = next((s[0] for s in tr if s[3] < 0.3), None)
        line = f"   {name}: min V = {minV:.3f}, floor crossed: {'yes, t = %.1f' % cross if cross else 'no'}, x(250) = {tr[-1][1]:.3f}, V(250) = {tr[-1][3]:.3f}"
        if ev:
            t0, y0 = ev[0]['at']
            peak = max((s for s in tr if s[0] >= t0), key=lambda s: s[1])
            line += f"; x keeps rising {peak[0] - t0:.1f} after the reform"
        print(line)


if __name__ == "__main__":
    main()
