"""Variants of the practice that differ in conversion capacity q (Section 4).

Domain i holds the alternative (share x_i0) and carriers of the practice of types
k = 1..m (shares x_ik, practice share x_i = sum_k x_ik).  Incidental conversion b0
turns the practice's success into shared rule support r_i.  Capacity q adds
conversion q * bh; a fraction chi of it is keyed to the carrier that produced it
(private stock rho_ik, per decision of a type-k carrier), the rest is shared.
Carriers are representative: a type-k carrier's activity profile is proportional
to the practice's profile x_j, so its private stock depends on its own q and on x.

    d rho_ik/dt = eps_i ( chi q_k sum_j bh_ij x_j - d_i rho_ik )
    d r_i/dt    = eps_i ( sum_j b0_ij x_j + (1-chi) sum_j bh_ij qbar_j x_j - d_i r_i )
    g_ik        = a_i (r_i + rho_ik) - c_i - gamma q_k          (alternative: 0)
    d/dt log(x_ik / x_i0) = kappa_i g_ik  + entry (mu) + trait mutation (nu)

Aggregated over types at steady state, this is the field model with conversion
b0 + qbar * bh.  Within the practice, type k beats type l in domain i at steady
state iff  chi c_i (q_k - q_l) sum_j Rh_ij x_j  >  gamma (q_k - q_l).
"""
import math
from field import n, D, E, S, P, F, I, SHORT, KAPPA, EPS, A, C0, DD, conv, to_b, DT

MU = 1e-4     # entry between the alternative and the practice
NU = 1e-4     # trait mutation among carrier types


def bhat(theta_h=0.5, hub_h=0.2, psi_h=0.1, phi_h=0.05, own_h=0.05):
    """Conversion added per unit of capacity (physical rates; a = c = d = 1)."""
    R = [[0.0] * n for _ in range(n)]
    R[D][D] = hub_h
    for i in range(1, n):
        R[i][i] = own_h
        R[i][D] = theta_h
        R[D][i] = psi_h
        for j in range(1, n):
            if j != i:
                R[i][j] = phi_h
    return to_b(R)


class Carriers:
    def __init__(self, qs, chi, gamma, B0, BH, d=None, mu=MU, nu=NU):
        self.qs, self.chi, self.gamma = list(qs), chi, gamma
        self.m = len(qs)
        self.B0, self.BH = B0, BH
        self.d = list(d or DD)
        self.mu, self.nu = mu, nu

    def unpack(self, y):
        m = self.m
        w = [y[i * m:(i + 1) * m] for i in range(n)]                  # log(x_ik/x_i0)
        rho = [y[n * m + i * m:n * m + (i + 1) * m] for i in range(n)]
        r = y[2 * n * m:2 * n * m + n]
        return w, rho, r

    def shares(self, w):
        out = []
        for i in range(n):
            mx = max(0.0, max(w[i]))
            ex = [math.exp(v - mx) for v in w[i]]
            den = math.exp(-mx) + sum(ex)
            out.append([e / den for e in ex])
        return out

    def rhs(self, y):
        m, chi = self.m, self.chi
        w, rho, r = self.unpack(y)
        x = self.shares(w)
        X = [sum(x[i]) for i in range(n)]
        Qx = [sum(self.qs[k] * x[j][k] for k in range(m)) for j in range(n)]   # qbar_j x_j
        dw, drho, dr = [], [], []
        for i in range(n):
            x0 = 1.0 - X[i]
            for k in range(m):
                g = A[i] * (r[i] + rho[i][k]) - C0[i] - self.gamma * self.qs[k]
                ent = self.mu * (x0 / (m * x[i][k]) - X[i] / x0)
                mut = self.nu * (X[i] / (m * x[i][k]) - 1.0)
                dw.append(KAPPA[i] * g + ent + mut)
        for i in range(n):
            hx = sum(self.BH[i][j] * X[j] for j in range(n))
            for k in range(m):
                drho.append(EPS[i] * (chi * self.qs[k] * hx - self.d[i] * rho[i][k]))
        for i in range(n):
            inc = sum(self.B0[i][j] * X[j] for j in range(n))
            cap = (1 - chi) * sum(self.BH[i][j] * Qx[j] for j in range(n))
            dr.append(EPS[i] * (inc + cap - self.d[i] * r[i]))
        return dw + drho + dr

    def step(self, y, dt=DT):
        k1 = self.rhs(y)
        k2 = self.rhs([y[i] + dt / 2 * k1[i] for i in range(len(y))])
        k3 = self.rhs([y[i] + dt / 2 * k2[i] for i in range(len(y))])
        k4 = self.rhs([y[i] + dt * k3[i] for i in range(len(y))])
        return [y[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(y))]

    def init(self, x_tot, r_shared, split=None):
        m = self.m
        split = split or [1.0 / m] * m
        y = []
        for i in range(n):
            x0 = 1.0 - x_tot[i]
            y += [math.log(x_tot[i] * split[k] / x0) for k in range(m)]
        y += [0.0] * (n * m)
        y += list(r_shared)
        return y

    def run(self, y, T, every=1.0):
        steps = int(round(T / DT))
        ke = max(1, int(round(every / DT)))
        rec = []
        t = 0.0

        def snap():
            w, rho, r = self.unpack(y)
            rec.append((t, self.shares(w), [list(v) for v in rho], list(r)))
        snap()
        for s in range(steps):
            y = self.step(y)
            t += DT
            if (s + 1) % ke == 0:
                snap()
        return rec, y


def mean_q(x_i, qs):
    X = sum(x_i)
    return sum(xk * q for xk, q in zip(x_i, qs)) / X


def field_mean_q(x, qs):
    """Practice-weighted mean capacity over all domains."""
    num = sum(x[i][k] * qs[k] for i in range(n) for k in range(len(qs)))
    den = sum(sum(x[i]) for i in range(n))
    return num / den


def advantage(x, chi, gamma, BH, i, dq=1.0):
    """Steady-state payoff advantage per unit of capacity in domain i: chi c_i sum_j Rh_ij x_j - gamma."""
    X = [sum(x[j]) for j in range(n)]
    return dq * (chi * A[i] * sum(BH[i][j] * X[j] for j in range(n)) / DD[i] - gamma)
