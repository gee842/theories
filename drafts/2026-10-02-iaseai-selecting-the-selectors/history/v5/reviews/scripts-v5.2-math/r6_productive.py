"""When intensity is productive (Prop 7.4's common value), what does the inclusive self-model do to the (A_G) hazard?
pi_i = A_t E^alpha / n - c e_i - L E. Self-model theta: O_i = pi_i + theta mean(pi_-i).
Symmetric FOC in E (each e_i): (1+theta)/n * alpha A E^(alpha-1) = c + (1+theta) L  [common value enters all payoffs]
   -> at theta=n-1: alpha A E^(alpha-1) = c + n L (joint optimum); at theta=0: alpha A E^(alpha-1)/n = c + L."""
import math
def E_star(theta, A, n=4, alpha=0.5, c=1.0, L=0.3):
    rhs = (c + (1 + theta) * L) * n / (1 + theta)
    return (alpha * A / rhs) ** (1 / (1 - alpha))
a, g = 0.01, 1.03
for theta in (0.0, 1.0, 3.0):
    s = 1.0; out = {}
    for t in range(1, 2001):
        q = 1 - math.exp(-a * 0.3 * E_star(theta, 5 * g ** t))
        s *= 1 - q
        if t in (10, 50, 100, 200): out[t] = (q, s)
    print(f"productive intensity, theta={theta}: " + "; ".join(f"t={t}: q={out[t][0]:.4f}, S={out[t][1]:.3g}" for t in out))
