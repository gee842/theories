"""Is moving to the accurate self-model in an actor's own interest when self-models are observed?
Stage 1: actor 1 commits (observably) to theta_1; the others hold theta = kappa.
Stage 2: Nash equilibrium of the asymmetric r=1 contest in objectives.
Player i's effective game: prize V_i = Om (1 - theta_i/(n-1)), unit cost k_i = c + (1+theta_i) l.
r=1 closed form: a_i = k_i/V_i; active set by ascending a; X = (m-1)/sum a; e_i = X - a_i X^2.
Actor 1's true welfare W_1 = pi_1 + kappa * mean(pi_others)."""
def eq(thetas, n, Om, c, l):
    V = [Om * (1 - t / (n - 1)) for t in thetas]; k = [c + (1 + t) * l for t in thetas]
    a = [k[i] / V[i] for i in range(n)]
    order = sorted(range(n), key=lambda i: a[i])
    for m in range(n, 1, -1):
        act = order[:m]; X = (m - 1) / sum(a[i] for i in act)
        if all(a[i] * X < 1 for i in act):
            e = [0.0] * n
            for i in act: e[i] = X - a[i] * X * X
            return e
    return [0.0] * n
def material(e, n, Om, c, l):
    E = sum(e)
    return [Om * e[i] / E - c * e[i] - l * E for i in range(n)]
def W1(th1, kappa, n=4, Om=1.0, c=1.0, l=0.3):
    e = eq([th1] + [kappa] * (n - 1), n, Om, c, l)
    p = material(e, n, Om, c, l)
    return p[0] + kappa * sum(p[1:]) / (n - 1), e
for n in (2, 3, 4):
    for kappa in (0.0, 0.4):
        if kappa >= n - 1: continue
        grid = [-1 + k * (n - 1 + 0.999) / 4000 for k in range(4000)]
        grid = [g for g in grid if g < n - 1 - 1e-6]
        best = max(grid, key=lambda t: W1(t, kappa, n)[0])
        wk = W1(kappa, kappa, n)[0]; wb = W1(best, kappa, n)[0]
        print(f"n={n}, kappa={kappa}: committed theta_1 maximizing own true welfare = {best:+.3f} (W={wb:.4f}) vs accurate theta_1=kappa (W={wk:.4f})")
