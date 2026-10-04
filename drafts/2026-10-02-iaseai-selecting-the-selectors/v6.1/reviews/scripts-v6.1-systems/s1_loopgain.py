# S1: does Gamma (Prop 2.2) behave like a loop gain?  Pure python.
# (a) sign of dGamma/dd: ratio-form (sigma=r ln X) vs difference-form (sigma=s X) channel, by numerical Jacobian
#     of the nonlinear map (1) with n=2, and by nonlinear simulation of a small deviation.
# (b) growth factor per period: 1+d(Gamma-1) (Remark S2.1) vs 1+(d+delta_f)(Gamma-1).
# (c) equal Gamma, different speed: gain on a fast vs a slow channel.
# (d) a countervailing delayed channel: net DC gain < 1 yet growing oscillation.
import math, cmath

def step(X, d, kO, beta, k0, df, sig):
    n=len(X); s=[sig(x) for x in X]; m=max(s); w=[math.exp(v-m) for v in s]; S=sum(w); p=[v/S for v in w]
    Xb=sum(X)/n
    return [(1-d)*X[i]+kO*((1-beta)*p[i]+beta/n)+k0-df*(X[i]-Xb) for i in range(n)]

def jac_dev_eig(d,kO,beta,k0,df,sig,h=1e-7):
    # numerical 2x2 Jacobian at equal standing, eigenvalues
    Xs=(kO/2+k0)/d
    X=[Xs,Xs]
    base=step(X,d,kO,beta,k0,df,sig)
    J=[[0,0],[0,0]]
    for j in range(2):
        Xp=list(X); Xp[j]+=h
        f=step(Xp,d,kO,beta,k0,df,sig)
        for i in range(2): J[i][j]=(f[i]-base[i])/h
    tr=J[0][0]+J[1][1]; det=J[0][0]*J[1][1]-J[0][1]*J[1][0]
    disc=cmath.sqrt(tr*tr-4*det)
    ev=[(tr+disc)/2,(tr-disc)/2]
    return max(abs(e) for e in ev), Xs

def sim_growth(d,kO,beta,k0,df,sig,T=400):
    Xs=(kO/2+k0)/d; X=[Xs*(1+1e-4),Xs*(1-1e-4)]
    g0=abs(X[0]-X[1])
    for _ in range(T): X=step(X,d,kO,beta,k0,df,sig)
    return abs(X[0]-X[1])/g0

kO,beta,k0,df=1.0,0.0,0.2,0.1
print("(a) Ratio form sigma=r ln X, r=2 (decisiveness elasticity held fixed); kappa*Omega=1, k0=0.2, delta_f=0.1, n=2")
r=2.0
omega=kO/(kO+2*k0)
for d in (0.05,0.1,0.2,0.3,0.6,0.9):
    rho,Xs=jac_dev_eig(d,kO,beta,k0,df,lambda x:r*math.log(x))
    G=(1-beta)*r*omega*d/(d+df)
    gr=sim_growth(d,kO,beta,k0,df,lambda x:r*math.log(x))
    print(f"   d={d:4.2f}: Gamma={G:.3f}  numerical spectral radius={rho:.4f}  deviation x{gr:.3g} after 400 periods  -> {'UNSTABLE' if rho>1 else 'stable'}")
print("   => raising the decay/correction rate d of a ratio-form stock RAISES Gamma (and destabilizes) when delta_f>0; with delta_f=0 it has no effect.")
print("(a') Difference form sigma=s X, s=1.2 (strength linear in the stock, like rule support offsetting a cost)")
s=1.2
for d in (0.05,0.1,0.2,0.3,0.6,0.9):
    rho,Xs=jac_dev_eig(d,kO,beta,k0,df,lambda x:s*x)
    rj=s*Xs
    G=(1-beta)*rj*omega*d/(d+df)
    print(f"   d={d:4.2f}: r_j=s X*={rj:.3f}  Gamma={G:.3f}  spectral radius={rho:.4f}  -> {'UNSTABLE' if rho>1 else 'stable'}")
print("   => here correction lowers Gamma, through r_j = s X* = s (kO/n+k0)/d.")

print("(b) growth factor per period of a single channel: exact lambda* vs Remark S2.1's 1+d(Gamma-1)")
for d,df_ in ((0.2,0.0),(0.2,0.1),(0.2,0.3)):
    r=3.0; k0_=0.0
    rho,_=jac_dev_eig(d,1.0,0.0,1e-12,df_,lambda x:r*math.log(x))
    G=r*d/(d+df_)
    print(f"   d={d}, delta_f={df_}: Gamma={G:.3f}; exact {rho:.4f}; 1+d(G-1)={1+d*(G-1):.4f}; 1+(d+df)(G-1)={1+(d+df_)*(G-1):.4f}")

print("(c) same Gamma=1.2, gain placed on a fast channel (d+df=0.5) or a slow one (d+df=0.02): periods for a 1% gap to reach 50%")
for lab,den in (("fast",0.5),("slow",0.02)):
    lam=1+den*(1.2-1)
    print(f"   {lab}: lambda*={lam:.4f}, periods={math.log(50)/math.log(lam):.0f}")

print("(d) two channels, one countervailing and slow (mobilization against the leader): J = D + (1/n) u v^T with g2<0")
D1,D2,g1,g2=0.6,0.95,0.5,-0.05
J=[[D1+g1,None],[None,D2+g2]]
off=g1*g2    # product of off-diagonals of a rank-one perturbation
tr=D1+g1+D2+g2; det=(D1+g1)*(D2+g2)-off
disc=cmath.sqrt(tr*tr-4*det); ev=[(tr+disc)/2,(tr-disc)/2]
net=g1/(1-D1)+g2/(1-D2)
print(f"   net DC gain sum g_j/(1-D_j) = {net:.3f} (<1);  eigenvalues {ev[0]:.4f}, {ev[1]:.4f}; modulus {abs(ev[0]):.4f} -> growing oscillation, period {2*math.pi/abs(cmath.phase(ev[0])):.0f}")
# simulate
u=[1.0,0.0]
mx=[]
for t in range(600):
    y1=(D1+g1)*u[0]+math.sqrt(abs(off))*u[1]
    y2=-math.sqrt(abs(off))*u[0]+(D2+g2)*u[1]
    u=[y1,y2]; mx.append(abs(u[0]))
print(f"   simulated |deviation| at t=100,300,600: {mx[99]:.3g}, {mx[299]:.3g}, {mx[599]:.3g}")
