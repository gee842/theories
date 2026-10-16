# Independent referee checks (pure stdlib). Not a re-run of the authors' inequalities.
import math

print("=== 1. Calibrating the single-channel loop gain with the paper's own diffusion figure")
print("Gamma = (1-beta) r omega d/(d+delta_f); r* = decisiveness needed for Gamma=1 at beta=0, omega=1")
for df in (0.05, 0.10):
    for d in (0.01, 0.02, 0.03, 0.05, 0.10):
        ratio = d/(d+df)
        print(f"  delta_f={df:.2f}/mo  d={d:.2f}/mo  d/(d+df)={ratio:.3f}  r*={1/ratio:.2f}")
print("  (Remark 8.6 uses delta_f = 0.1/month for a lead diffusing.)")

print("\n=== 2. Accurate coupling vs. compounding: working theta of an actor whose held theta0 equals the true coupling kappa")
def theta_G(t0, G, n):
    return (n*t0 - (n-1)*(1+t0)*G)/(n - (1+t0)*G)
for n in (2, 4):
    for kappa in (0.2, 0.4, 1.0):
        Gstar = n*kappa/((n-1)*(1+kappa))
        row = ", ".join(f"G={G}:{theta_G(kappa,G,n):+.2f}" for G in (0.25,0.5,0.75,0.9))
        print(f"  n={n} kappa={kappa}: working theta falls below 0 (isolated self) once Gamma_delta > {Gstar:.3f};  {row}")
# also verify the weight-on-standing decomposition
n, t0, G = 4, 0.0, 0.5
lam = ((n-1-t0)/(n-1))*G/(1-G)
alt = (n*t0 - lam*(n-1))/(n + lam*(n-1))
print(f"  decomposition check: formula {theta_G(t0,G,n):.6f} vs lambda-form {alt:.6f}")

print("\n=== 3. Tug-of-war MPE (Tullock r=1 per step, absorbing at +/-K, prize 1 to winner): where does effort live?")
def tug(K, delta, iters=20000):
    S = list(range(-K, K+1))
    V1 = {s: 0.0 for s in S}; V2 = {s: 0.0 for s in S}
    V1[K], V2[K] = 1.0, 0.0
    V1[-K], V2[-K] = 0.0, 1.0
    x1 = {}; x2 = {}
    for _ in range(iters):
        diff = 0.0
        for s in range(-K+1, K):
            v1 = delta*(V1[s+1]-V1[s-1]); v2 = delta*(V2[s-1]-V2[s+1])
            v1 = max(v1, 1e-15); v2 = max(v2, 1e-15)
            a = v1*v1*v2/(v1+v2)**2; b = v1*v2*v2/(v1+v2)**2
            p = v1/(v1+v2)
            n1 = p*delta*V1[s+1] + (1-p)*delta*V1[s-1] - a
            n2 = p*delta*V2[s+1] + (1-p)*delta*V2[s-1] - b
            diff = max(diff, abs(n1-V1[s]), abs(n2-V2[s]))
            V1[s], V2[s] = n1, n2; x1[s], x2[s] = a, b
        if diff < 1e-13: break
    return x1, x2, V1
for K, delta in ((3, 0.95), (5, 0.95), (5, 0.99)):
    x1, x2, V1 = tug(K, delta)
    tot0 = x1[0]+x2[0]
    print(f"  K={K} delta={delta}: total effort by state / effort at parity:")
    print("   " + "  ".join(f"s={s:+d}:{(x1[s]+x2[s])/tot0:.3f}" for s in range(0, K)))
    print("   laggard effort / its effort at parity: " + "  ".join(f"s={-s:+d}:{x2[s]/x2[0]:.3f}" for s in range(0, K)))
