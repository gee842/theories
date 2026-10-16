# Review checks for v5.1 Section 1
def e_sym(n,r,Om,c,l,th): return r*Om*(n-1-th)/(n*n*(c+(1+th)*l))
def obj(ei,eo,n,r,Om,c,l,th,beta_prize=0.0):
    tot=ei**r+(n-1)*eo**r; wi=ei**r/tot; wo=eo**r/tot; E=ei+(n-1)*eo
    pool=beta_prize*Om/n
    pi=(1-beta_prize)*Om*wi+pool-c*ei-l*E; po=(1-beta_prize)*Om*wo+pool-c*eo-l*E
    return pi+th*po
def br(eo,*a,**k):
    lo,hi=1e-9,50.0
    for _ in range(300):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if obj(m1,eo,*a,**k)<obj(m2,eo,*a,**k): lo=m1
        else: hi=m2
    return (lo+hi)/2
n,r,Om,c,l=4,1.0,1.0,1.0,0.3
print("F3: sharing only the contested prize (share beta pooled), purely relative objective theta=-1")
for beta in (0.0,0.5,0.9):
    e=e_sym(n,r,(1-beta)*Om,c,l,-1.0)
    print(f"  beta={beta}: predicted e={e:.4f}; best response to it {br(e,n,r,Om,c,l,-1.0,beta_prize=beta):.4f}")
# replicator: payoff gap between a high-effort and low-effort carrier facing the same field
print("F3: selection gap pi(hi)-pi(lo) against a field at e=0.1, prize pooled at beta")
for beta in (0.0,0.5,0.9):
    def pay(ei, eo=0.1):
        tot=ei+(n-1)*eo; return (1-beta)*Om*ei/tot - c*ei
    print(f"  beta={beta}: hi(0.2)-lo(0.05) = {pay(0.2)-pay(0.05):+.4f}")
print("F1: constant stakes, fixed theta=0.4, constant r and L: survival never stays positive")
a=0.01
q=a*r*Om*l*(n-1-0.4)/(n*(c+1.4*l)); s=1.0
for H in (100,1000,10000):
    print(f"  H={H}: {(1-q)**H:.4f}")
print("F1: stakes stop growing at round 50 (lever 2 as worded): still -> 0")
s=1.0
for t in range(1,5001):
    Omt=1.03**min(t,50); s*=1-a*r*Omt*l*(n-1-0.4)/(n*(c+1.4*l))
print(f"  survival at 5000: {s:.2e}")
print("F6: without scaling the shared loss, the dissipated share is constant in s")
for s_ in (1,10,100):
    D=n*e_sym(n,r,s_*Om,c,l,0.4)*(c+n*l)/(s_*Om); print(f"  s={s_}: {D:.4f}")
