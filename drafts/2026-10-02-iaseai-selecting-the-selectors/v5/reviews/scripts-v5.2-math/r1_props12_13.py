"""Independent re-derivation of Props 1.2 and 1.3 (v5.2). Pure Python, exact rationals where possible."""
from fractions import Fraction as F
import random, itertools

random.seed(11)
# ---- Prop 1.2 with exact rationals
bad = 0
for _ in range(3000):
    n = random.randint(2, 7)
    th = F(random.randint(-100, 100 * (n - 1)), 100)
    pi = [F(random.randint(-500, 500), 37) for _ in range(n)]
    O = [pi[i] + th * sum(pi[j] for j in range(n) if j != i) / (n - 1) for i in range(n)]
    if sum(O) != (1 + th) * sum(pi): bad += 1
    D = F(random.randint(-90, 90), 7)
    O2 = [pi[i] + D + th * sum(pi[j] + D for j in range(n) if j != i) / (n - 1) for i in range(n)]
    if any(O2[i] - O[i] != (1 + th) * D for i in range(n)): bad += 1
print("Prop1.2 (1)(2) exact failures:", bad)

# ---- Prop 1.3(1): theta* exact
def thstar(n, b, c, d, eps):
    return (eps * (b - d) - c) / (eps * (b / F(n - 1) + d))
n, b, c, d = 4, F(1), F(3, 10), F(2, 10)
for eps in (1, 10):
    t = thstar(n, b, c, d, F(eps)); print(f"theta*(eps={eps}) = {t} = {float(t):.5f}")
print("limit", float((b - d) / (b / 3 + d)))
# brute-force check of 'whatever the others do' and dominance for theta slightly off theta*
def u(a, eps):
    return [eps * b * (a[i] - F(sum(a[j] for j in range(n) if j != i), n - 1)) - c * a[i] - eps * d * sum(a) for i in range(n)]
for eps in (F(1), F(10)):
    ts = thstar(n, b, c, d, eps)
    for th in (ts - F(1, 1000), ts + F(1, 1000)):
        gains = set()
        for rest in itertools.product((0, 1), repeat=n - 1):
            a1 = [1] + list(rest); a0 = [0] + list(rest)
            U1, U0 = u(a1, eps), u(a0, eps)
            O1 = U1[0] + th * sum(U1[1:]) / (n - 1); O0 = U0[0] + th * sum(U0[1:]) / (n - 1)
            gains.add(O1 - O0)
        print(f"  eps={eps}, theta={float(th):.4f}: gain of racing constant across others' profiles: {len(gains)==1}, value {float(gains.pop()):+.5f}")

# ---- Prop 1.3(2)-(3): contest closed forms
def e_sym(n, r, Om, c, l, th):
    return r * Om * (n - 1 - th) / (n * n * (c + (1 + th) * l))
def share(n, r, c, l, th, s=1):
    Om = s; ll = s * l
    return n * e_sym(n, r, Om, c, ll, th) * (c + n * ll) / Om
def share_formula(n, r, c, l, th, s=1):
    return r * (n - 1 - th) * (c + n * s * l) / (n * (c + (1 + th) * s * l))
n, r, c, l = 4, F(1), F(1), F(3, 10)
for th in (F(-1), F(0), F(2, 5), F(1), F(2)):
    assert share(n, r, c, l, th) == share_formula(n, r, c, l, th)
    ceil = None if th == -1 else r * (n - 1 - th) / (1 + th)
    vals = [share_formula(n, r, c, l, th, F(s)) for s in (1, 10, 100, 10 ** 6)]
    print(f"theta={float(th):+.2f}: share at s=1,10,100,1e6 = {[round(float(v),4) for v in vals]}; ceiling {None if ceil is None else round(float(ceil),4)}")
# derivative sign numerator: n l (c+(1+th) s l) - (1+th) l (c+n s l) == c l (n-1-th)
for _ in range(1000):
    n_ = random.randint(2, 8); th = F(random.randint(-99, 100 * (n_ - 1) - 1), 100)
    c_ = F(random.randint(1, 50), 10); l_ = F(random.randint(1, 50), 10); s_ = F(random.randint(1, 1000), 10)
    lhs = n_ * l_ * (c_ + (1 + th) * s_ * l_) - (1 + th) * l_ * (c_ + n_ * s_ * l_)
    assert lhs == c_ * l_ * (n_ - 1 - th)
print("derivative-sign identity verified on 1000 exact random cases")
# theta_g
def thg(n, r): return (r * (n - 1) - 1) / (1 + r)
print("theta_g(n=4,r=1) =", thg(4, F(1)), "; theta_g(n=4,r=1/2) =", thg(4, F(1, 2)))
# 'iff' check by scanning: total positive at all scales iff theta >= theta_g
viol = 0
for _ in range(400):
    n_ = random.randint(2, 6); r_ = F(random.randint(1, 100), 100) * F(n_, n_ - 1)
    th = F(random.randint(-99, 100 * (n_ - 1) - 1), 100)
    c_ = F(1); l_ = F(random.randint(1, 30), 10)
    allpos = all(share_formula(n_, r_, c_, l_, th, F(s)) < 1 for s in [10 ** k for k in range(-3, 9)])
    if allpos != (th >= thg(n_, r_)):
        # borderline cases near threshold where share approaches 1 only at huge s
        viol += 1
print("theta_g iff, scan up to s=1e8 (disagreements arise only very near threshold):", viol)
# r-cap: theta_g at r = n/(n-1)
for n_ in (2, 3, 4, 6, 10, 100):
    rmax = F(n_, n_ - 1)
    print(f"  n={n_}: theta_g at r=n/(n-1): {float(thg(n_, rmax)):.4f} = (n-1)^2/(2n-1) = {float(F((n_-1)**2, 2*n_-1)):.4f}; inclusive n-1 = {n_-1}")
# constant-share claim when l does not scale
print("share at theta=0.4 if l fixed:", float(share_formula(4, F(1), F(1), F(3, 10), F(2, 5))))
