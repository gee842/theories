"""Check for Remark S6 `nearlock` (How certain the lock must be), proposed as an extension of block DL in checks_v62.py.
Claim: in the survival model of Proposition `delegatelock`, not delegating is strictly better for every n, p and profile
whenever (1-q_L)(1+s)(1-psi_1) < 1-psi_0; the bound is approached as n -> infinity with k=0, p=1.
Independent: direct survival comparison over random settings drawn above the bound. Standard library only."""
import random
random.seed(1)
def ratio(n, k, s, qL, p0, p1, p):
    QN = (1-p0)**(n-k)*(1-p1)**k; wN = 1/(n+k*s)
    QD = (1-p0)**(n-k-1)*(1-p1)**(k+1); wD = (1+s)/(n+(k+1)*s)
    return (1-qL)*QD*(wD+(1-wD)*(1-p))/(QN*(wN+(1-wN)*(1-p)))
viol = 0; N = 200000
for _ in range(N):
    n = random.randint(2, 12); k = random.randint(0, n-1); s = 10**random.uniform(-2, 4)
    p0 = random.uniform(0, 0.3); p1 = random.uniform(p0, 0.9); p = random.random()
    a = (1-p1)/(1-p0); qstar = 1-1/(a*(1+s))
    qL = random.uniform(max(qstar, 0), 1)
    if qL <= qstar: continue
    if ratio(n, k, s, qL, p0, p1, p) >= 1: viol += 1
print(f"nearlock: violations of 'not delegating strictly better' above the bound: {viol} of {N}")
for n in (2, 10, 100, 10000):
    s, p0, p1 = 5, .01, .1; a = (1-p1)/(1-p0)
    print(f"  tightness, n={n}, k=0, p=1: ratio/bound = {ratio(n,0,s,0.0,p0,p1,1.0)/(a*(1+s)):.4f}  (-> 1 as n grows)")
assert viol == 0
