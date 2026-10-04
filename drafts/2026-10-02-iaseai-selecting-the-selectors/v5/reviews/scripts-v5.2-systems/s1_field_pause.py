"""S1. Field model (3) with D=1: separatrix, time-scale ratio, insulated-pause dwell time,
and the local spectrum at absence vs capture (does critical slowing down warn of capture?).
Pure Python, RK4.
  x' = zeta x(1-x)(a z - c),  z' = eps (b x - d z),  R = a b /(c d)
"""
import math

def rk4(f, y, dt, n):
    for _ in range(n):
        k1 = f(y)
        k2 = f([y[i] + 0.5*dt*k1[i] for i in range(len(y))])
        k3 = f([y[i] + 0.5*dt*k2[i] for i in range(len(y))])
        k4 = f([y[i] + dt*k3[i] for i in range(len(y))])
        y = [y[i] + dt*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6 for i in range(len(y))]
    return y

def field(zeta, a, c, b, d, eps):
    def f(y):
        x, z = y
        return [zeta*x*(1-x)*(a*z - c), eps*(b*x - d*z)]
    return f

def fate(x0, z0, zeta, a, c, b, d, eps, T=4000.0):
    f = field(zeta, a, c, b, d, eps)
    dt = min(0.05, 0.2/max(zeta, eps))
    y = rk4(f, [x0, z0], dt, int(T/dt))
    return 1 if y[0] > 0.5 else 0

def sigma0(zeta, a, c, b, d, eps):
    lo, hi = 1e-6, 1-1e-6
    if fate(hi, 0.0, zeta, a, c, b, d, eps) == 0:
        return 1.0
    for _ in range(40):
        mid = 0.5*(lo+hi)
        if fate(mid, 0.0, zeta, a, c, b, d, eps):
            hi = mid
        else:
            lo = mid
    return 0.5*(lo+hi)

print("== S1a: separatrix at z=0, sigma(0), vs time-scale ratio eps/zeta (R=2, saddle x=1/R=0.5)")
zeta, a, c, b, d = 1.0, 1.0, 1.0, 2.0, 1.0
for eps in [10.0, 3.0, 1.0, 0.3, 0.1, 0.03]:
    s = sigma0(zeta, a, c, b, d, eps)
    print(f"  eps/zeta={eps:6.2f}  sigma(0)={s:.3f}")

print("== S1b: insulated pause (b_p=0) of length Tp, share frozen at x_p, z starts at captured level b/d")
print("   minimal Tp for release to go to absence, in units of 1/(eps d)")
for eps in [1.0, 0.1]:
    for xp in [0.6, 0.8, 0.95]:
        z0 = b/d
        # z(Tp) = z0 exp(-eps d Tp); find smallest Tp such that (xp, z(Tp)) -> 0
        lo, hi = 0.0, 50.0/(eps*d)
        if fate(xp, z0*math.exp(-eps*d*hi), zeta, a, c, b, d, eps) == 1:
            print(f"  eps={eps} x_p={xp}: not undone even after {hi:.0f}")
            continue
        for _ in range(30):
            mid = 0.5*(lo+hi)
            if fate(xp, z0*math.exp(-eps*d*mid), zeta, a, c, b, d, eps):
                lo = mid
            else:
                hi = mid
        print(f"  eps={eps:4.2f} x_p={xp:.2f}: Tp_min={hi:8.2f}  = {hi*eps*d:5.2f}/(eps d)")

print("== S1c: ordinary pause (b_p=b): share frozen at x_p, release -> capture iff x_p>1/R")
for xp in [0.45, 0.55]:
    print(f"  x_p={xp}: fate={'capture' if fate(xp, b*xp/d, zeta, a, c, b, d, 1.0) else 'absence'}")

print("== S1d: local eigenvalues. At absence (0,0): -zeta c and -eps d, independent of R.")
print("   At capture (1,b/d): -zeta c (R-1) and -eps d; slowing down as R->1 from above.")
for R in [3.0, 2.0, 1.5, 1.2, 1.05]:
    bb = R*c*d/a
    print(f"  R={R:4.2f}: absence eig_x={-zeta*c:+.3f}; capture eig_x={-zeta*c*(R-1):+.3f}; saddle x=1/R={1/R:.3f}")

print("== S1e: Remark 3.2 check: if ab<mu*delta with mu,delta in (0,1], is the smaller root > -1 automatically?")
import random
random.seed(1)
viol = 0; N = 200000
for _ in range(N):
    mu = random.uniform(1e-3, 1); de = random.uniform(1e-3, 1)
    ab = random.uniform(0, mu*de*0.999999)
    disc = (mu-de)**2/4 + ab
    small = 1 - (mu+de)/2 - math.sqrt(disc)
    if small <= -1: viol += 1
print(f"  draws={N}, violations={viol}")
