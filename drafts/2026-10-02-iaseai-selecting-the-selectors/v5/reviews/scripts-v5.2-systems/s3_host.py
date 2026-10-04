"""S3. The host of Section 2.2.
 (a) Viability kernel slice: with load that can only be reduced by selection (replicator, liability
     margin Delta = tau_eff - nu > 0 from t=0, optional enactment delay), what initial V is needed
     to keep V >= V_min for all t?  Paper's illustration: rho=0.05, h=0.08, K=1, V_alarm=0.6, V_min=0.3.
 (b) Logistic vs Allee host: hysteresis and recovery after the load is removed.
 (c) Two coupled host components: aggregate scalar vs weakest component.
"""
import math

rho, h, K, Vmin, Valarm = 0.05, 0.08, 1.0, 0.3, 0.6
ebar, emin = 1.0, 0.1

def min_path_V(V0, p0, Delta, delay, T=600.0, dt=0.02):
    V, p, t, vmin = V0, p0, 0.0, V0
    while t < T:
        E = p*ebar + (1-p)*emin
        dV = V*(rho*(1-V/K) - h*E)
        dp = 0.0 if t < delay else -Delta*(ebar-emin)*p*(1-p)
        V += dt*dV; p += dt*dp; t += dt
        if V < vmin: vmin = V
    return vmin

def kernel_V(p0, Delta, delay):
    lo, hi = Vmin, K
    if min_path_V(hi, p0, Delta, delay) < Vmin: return None
    for _ in range(40):
        mid = 0.5*(lo+hi)
        if min_path_V(mid, p0, Delta, delay) >= Vmin: hi = mid
        else: lo = mid
    return hi

print("== S3a: viability-kernel boundary V_crit(p0): smallest V at which acting NOW still keeps V>=V_min")
print(f"   rho={rho}, h={h}, ebar={ebar}, e_min={emin}, V_min={Vmin}, V_alarm={Valarm}")
for Delta in [1.0, 0.3, 0.1]:
    for delay in [0.0, 10.0]:
        row = []
        for p0 in [0.5, 0.9, 0.99]:
            v = kernel_V(p0, Delta, delay)
            row.append("none" if v is None else f"{v:.3f}")
        print(f"  Delta={Delta:4.2f} delay={delay:4.1f}:  V_crit at p0=0.5/0.9/0.99 = {row}")

print("== S3b: logistic vs Allee host (A=0.2). Equilibria vs load E, then remove the load after collapse.")
A = 0.2
def logi(V, E): return V*(rho*(1-V/K) - h*E)
def allee(V, E): return V*(rho*(V/A-1)*(1-V/K)*1.0 - h*E)
def eq_pos(f, E):
    roots = []; N = 4000; prev = f(1e-6, E)
    for i in range(1, N+1):
        V = i/N*K; cur = f(V, E)
        if prev*cur < 0: roots.append(round(V, 3))
        prev = cur
    return roots
# Allee fold load: max over V of rho (V/A-1)(1-V/K)/h
Ef = max(rho*(V/A-1)*(1-V/K)/h for V in [i/10000 for i in range(1, 10000)])
print(f"  Allee fold load E_f = {Ef:.3f}; logistic collapse load rho/h = {rho/h:.3f}")
for E in [0.0, 0.2, 0.4, 0.5, Ef-0.01]:
    print(f"  E={E:.3f}: logistic interior eq {eq_pos(logi, E)}; Allee positive eq {eq_pos(allee, E)}")
def run(f, V, E, T, dt=0.02):
    t = 0.0
    while t < T:
        V += dt*f(V, E); V = max(V, 0.0); t += dt
    return V
for name, f in [("logistic", logi), ("Allee", allee)]:
    V = run(f, 0.9, 0.8, 60.0)      # overload for 60 time units
    V2 = run(f, V, 0.0, 400.0)      # remove the load entirely
    print(f"  {name:8s}: after overload V={V:.3f}; after load removed for 400 units V={V2:.3f}")

print("== S3c: two coupled host components (1 fast: cyber/infra; 2 slow, Allee: trust/institutions)")
print("   dV1 = V1[r1(1-V1) - h1 E - c(1-V2)],  dV2 = V2[r2(V2/A2-1)(1-V2) - h2 E - c(1-V1)]")
r1, r2, A2, h1, h2 = 0.2, 0.05, 0.2, 0.08, 0.02
def coupled(V1, V2, E, c, T=2000.0, dt=0.02):
    t = 0.0
    while t < T:
        d1 = V1*(r1*(1-V1) - h1*E - c*(1-V2))
        d2 = V2*(r2*(V2/A2-1)*(1-V2) - h2*E - c*(1-V1))
        V1 = max(V1+dt*d1, 0.0); V2 = max(V2+dt*d2, 0.0); t += dt
    return V1, V2
for c in [0.0, 0.02, 0.04]:
    Ecrit = None
    for i in range(0, 301):
        E = i/100
        V1, V2 = coupled(0.95, 0.95, E, c)
        if V2 < 0.05 or V1 < 0.05:
            Ecrit = E; break
    V1, V2 = coupled(0.95, 0.95, Ecrit - 0.01 if Ecrit else 3.0, c)
    print(f"  coupling c={c:.2f}: first load with collapse E={Ecrit}; just below it V1={V1:.3f}, V2={V2:.3f}, mean={(V1+V2)/2:.3f}")
