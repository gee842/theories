"""At theta=-1 (objectives constant-sum), can repeated play deter a deviation from joint restraint?
Deviator's minmax in objectives: others choose a common intensity x (and also asymmetric two-level profiles);
deviator best-responds. If the minmax is >= 0 = value of joint restraint, no punishment deters a deviation that gains > 0."""
def O_dev(y, others, n=4, Om=1.0, c=1.0, l=0.3, th=-1.0):
    es = [y] + others; E = sum(es)
    if E == 0: w = [1.0 / n] * n
    else: w = [x / E for x in es]
    pi = [Om * w[j] - c * es[j] - l * E for j in range(len(es))]
    return pi[0] + th * sum(pi[1:]) / (len(es) - 1)
ys = [0.0] + [k / 2000 for k in range(1, 4001)]
best_min = 1e9; arg = None
xs = [k / 200 for k in range(0, 601)]
for x1 in xs[::5]:
    for x2 in xs[::5]:
        others = [x1, x2, x2]
        m = max(O_dev(y, others) for y in ys[::4])
        if m < best_min: best_min, arg = m, others
print(f"theta=-1, n=4: deviator's minmax over others' profiles (grid) = {best_min:+.4f} at others = {arg}")
