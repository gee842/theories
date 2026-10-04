"""Forward-looking contestants: the irreversible event priced into the objective.
Each actor also receives a non-contested flow Y_t = y0 * g^t (its share of everything outside the contest),
which is lost with the irreversible event. With self-model theta it counts theta * others' continuation too.
  marginal cost of own intensity: c + (1+theta) L (1 + a delta V_{t+1})
  e_t = r (n-1-theta) Om_t / (n^2 (c + (1+theta) L (1 + a delta V_{t+1})))
  V_t = Y_t + Om_t/n - (c + nL) e_t + delta (1 - a L n e_t) V_{t+1}
Linear link (A_G) as in the paper, truncated below 1."""
def forward(theta, delta, y0, T=4000, g=1.03, a=0.01, n=4, r=1.0, c=1.0, L=0.3):
    V = 0.0; qs = [0.0] * (T + 1)
    for t in range(T, 0, -1):
        Om = g ** t; Y = y0 * g ** t
        e = r * (n - 1 - theta) * Om / (n * n * (c + (1 + theta) * L * (1 + a * delta * V)))
        qt = min(a * L * n * e, 0.999999); qs[t] = qt
        V = Y + Om / n - (c + n * L) * e + delta * (1 - qt) * V
    s = 1.0; surv = {}
    for t in range(1, T + 1):
        s *= 1 - qs[t]
        surv[t] = s
    return qs, surv
for y0 in (1.0, 10.0):
    for theta in (0.0, 0.4, -1.0):
        for delta in (0.95, 0.99):
            qs, sv = forward(theta, delta, y0)
            print(f"y0={y0:>4}, theta={theta:+.1f}, delta={delta}: q_t at t=10,100,200,500,1000,2000 = "
                  + ", ".join(f"{qs[t]:.4f}" for t in (10, 100, 200, 500, 1000, 2000))
                  + " | survival at 100, 200, 1000 = " + ", ".join(f"{sv[t]:.3g}" for t in (100, 200, 1000)))
