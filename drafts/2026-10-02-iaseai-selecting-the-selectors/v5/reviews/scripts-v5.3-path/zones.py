import itertools, math
# Stage game of Prop 4.1 with common self-model theta (objectives O_i = u_i + theta * mean_{j!=i} u_j)
def u(n,b,c,d,eps,a):
    return [eps*b*(a[i]-sum(a[j] for j in range(n) if j!=i)/(n-1)) - c*a[i] - eps*d*sum(a) for i in range(n)]
def O(n,b,c,d,eps,th,a):
    v=u(n,b,c,d,eps,a); return [v[i]+th*sum(v[j] for j in range(n) if j!=i)/(n-1) for i in range(n)]
def consts(n,b,c,d,eps):
    A=eps*(b-d)-c; B=eps*(b/(n-1)+d); K=c+n*eps*d
    return A,B,K
def theta_star(n,b,c,d,eps):
    A,B,K=consts(n,b,c,d,eps); return A/B
def theta_rep(n,b,c,d,eps,delta,pd):
    A,B,K=consts(n,b,c,d,eps); dp=delta*(1-pd); D=dp/(1-dp)
    return (A-D*K)/(B+D*K)
def sustainable_bruteforce(n,b,c,d,eps,th,delta,pd):
    # grim trigger: cooperate = all restrain forever; deviation gain today, then with prob (1-pd) per period punished by all-race forever,
    # with prob pd the deviator is decisive and beyond punishment (valued conservatively at the cooperative payoff 0)
    coop=O(n,b,c,d,eps,th,[0]*n)[0]
    dev=O(n,b,c,d,eps,th,[1]+[0]*(n-1))[0]
    pun=O(n,b,c,d,eps,th,[1]*n)[0]
    dp=delta*(1-pd)
    # value of cooperating forever: coop/(1-delta); deviating: dev + continuation; continuation each future period: punished only while not decisive
    # conservative: decisive state absorbing with payoff coop; punishment state absorbing with payoff pun while game continues
    # V_dev = dev + delta*[(1-pd)*pun/(1-delta) + pd*coop/(1-delta)]  (decisiveness resolved once, right after deviation)
    Vc=coop/(1-delta); Vd=dev+delta*((1-pd)*pun+pd*coop)/(1-delta)
    return Vc>=Vd-1e-12
n,b,c,d,eps=4,1.0,0.3,0.2,1.0
print("theta* =",round(theta_star(n,b,c,d,eps),4))
# theta_rep with D = delta*(1-pd)/(1-delta): decisiveness resolved once, right after a deviation (as in V5.3-PATH.md)
def theta_rep2(n,b,c,d,eps,delta,pd):
    A,B,K=consts(n,b,c,d,eps); D=delta*(1-pd)/(1-delta)
    return (A-D*K)/(B+D*K)
print("brute-force check of theta_rep2 (decisiveness resolved once after deviation):")
for delta in (0.5,0.9):
    for pd in (0.0,0.5,0.9,0.99,1.0):
        tr=theta_rep2(n,b,c,d,eps,delta,pd)
        ok=all(sustainable_bruteforce(n,b,c,d,eps,tr+1e-6,delta,pd)==True for _ in [0]) and (not sustainable_bruteforce(n,b,c,d,eps,tr-1e-3,delta,pd) or tr-1e-3< -1)
        print(f"  delta={delta} pd={pd}: theta_rep={tr:.4f}  boundary verified {ok}; theta=-1 sustainable? {sustainable_bruteforce(n,b,c,d,eps,-1.0,delta,pd)}")
# zone III: theta >= theta* => restraint self-enforcing (racing weakly dominated in stage game)
ts=theta_star(n,b,c,d,eps)
dom=all(O(n,b,c,d,eps,ts+1e-6,[1]+list(r))[0]<=O(n,b,c,d,eps,ts+1e-6,[0]+list(r))[0] for r in itertools.product((0,1),repeat=n-1))
print("Zone III check: racing dominated just above theta*:",dom)
# structure moves theta*: sharing the rank prize b->(1-beta)b ; levy c up ; perceived harm d up
for beta in (0,0.25,0.5,0.75):
    print(f"  rank-prize sharing beta={beta}: theta*={theta_star(n,(1-beta)*b,c,d,eps):.4f}")
for cc in (0.3,0.6,0.9):
    print(f"  private cost/levy c={cc}: theta*={theta_star(n,b,cc,d,eps):.4f}")
# growth: eps up with c fixed raises theta*; harm superlinear lowers it
for e in (1,10,100):
    print(f"  eps={e}: theta*(cost diluted)={theta_star(n,b,c,d,e):.4f}; theta*(harm d*eps^0.5 extra)={theta_star(n,b,c,d*e**0.5,e):.4f}")
# decisive winner's post-victory sharing with objective O_w = pi_w + theta*mean others; linear: share s to others
def winner_share(n,theta,concave=False,W=1.0):
    best=None
    for k in range(0,1001):
        s=k/1000
        pw=W*(1-s); po=W*s/(n-1)
        if concave:
            f=lambda x: math.log(1e-9+x)
            val=f(pw)+theta*f(po)
        else:
            val=pw+theta*po
        if best is None or val>best[0]+1e-15: best=(val,s)
    return best[1]
print("decisive winner's share to others (linear):",[ (th,winner_share(4,th)) for th in (-1,0,0.4,2,2.9,3)])
print("decisive winner's share to others (log utility):",[ (th,winner_share(4,th,True)) for th in (-1,0,0.4,1,2,3) if th>=0])
# theta <-> lambda (weight on winning)
def th_from_lambda(lam,n): return -lam*(n-1)/(n+lam*(n-1))
print("theta from weight on winning lambda (n=4):",[(lam,round(th_from_lambda(lam,4),4)) for lam in (0,0.5,1,2,10,1e6)])
