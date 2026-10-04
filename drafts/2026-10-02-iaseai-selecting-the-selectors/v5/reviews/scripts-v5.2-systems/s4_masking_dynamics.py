"""S4. Masking (eq. 6) hides levels, not dynamics.
Stochastic logistic host at constant load: dV = V[rho(1-V/K) - hE]dt + sig dW.
Linearized recovery rate at V* = K(1-hE/rho) is lambda = -rho V*/K, so AR1 = exp(-rho V* dt_s/K)
reveals V* from the reports' dynamics. Reports: Vt = V + m(K - V) (constant m) or m(V) state-dependent.
A static (memoryless, smooth, monotone) masking preserves lag-1 autocorrelation to first order; it scales variance.
"""
import math, random

rho, h, K = 0.05, 0.08, 1.0
sig = 0.004
dt = 0.05
ds = 1.0          # sampling interval
Tburn, T = 400.0, 40000.0

def run(E, seed):
    rng = random.Random(seed)
    V = K*(1-h*E/rho); t = 0.0; out = []
    nsub = int(ds/dt); n = int((Tburn+T)/ds)
    for i in range(n):
        for _ in range(nsub):
            V += dt*V*(rho*(1-V/K) - h*E) + sig*math.sqrt(dt)*rng.gauss(0, 1)
        if i*ds >= Tburn: out.append(V)
    return out

def ar1_var(x):
    m = sum(x)/len(x); r = [v-m for v in x]
    var = sum(v*v for v in r)/len(r)
    ac = sum(r[i]*r[i+1] for i in range(len(r)-1))/sum(v*v for v in r)
    return ac, var

masks = {
    "none (m=0)": lambda V: V,
    "constant m=0.5": lambda V: V + 0.5*(K-V),
    "state-dependent m=0.4+0.3(1-V)": lambda V: V + (0.4+0.3*(1-V))*(K-V),
}
Valarm, Vmin = 0.6, 0.3
print(f"  sigma={sig}, sampling={ds}, series length={int(T/ds)}")
for E in [0.35, 0.40]:
    Vstar = K*(1-h*E/rho)
    xs = run(E, 11)
    print(f"== load E={E}: true V*={Vstar:.3f} (V_alarm={Valarm}, V_min={Vmin})")
    for name, f in masks.items():
        rep = [f(v) for v in xs]
        ac, var = ar1_var(rep)
        Vhat = -K*math.log(ac)/(rho*ds)
        mean = sum(rep)/len(rep)
        print(f"   {name:32s} mean report={mean:.3f}  level alarm={'FIRES' if mean <= Valarm else 'silent'}  "
              f"AR1={ac:.4f}  var={var:.2e}  V* inferred from AR1={Vhat:.3f}")
