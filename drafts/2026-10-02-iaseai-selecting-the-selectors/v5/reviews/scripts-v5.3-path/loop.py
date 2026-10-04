import math
F=lambda x: 1/(1+math.exp(-x))
def fixed_points(beta,nu=2.0,cu=0.6,s=0.1,k=0.4,G=0.4):
    # quasi-static z = b psi/d, so a z = G psi with G = ab/d
    h=lambda p: F(((1-beta)*nu-cu+G*p-k*(1-p))/s)-p
    pts=[];N=20000;prev=h(0.0)
    for i in range(1,N+1):
        p=i/N;cur=h(p)
        if (prev>0)!=(cur>0):
            lo,hi=p-1/N,p
            for _ in range(60):
                m=(lo+hi)/2
                if (h(lo)>0)!=(h(m)>0): hi=m
                else: lo=m
            pts.append(round((lo+hi)/2,4))
        prev=cur
    return pts
def band(**kw):
    multi=[b/1000 for b in range(0,1001) if len(fixed_points(b/1000,**kw))>=3]
    return (min(multi),max(multi)) if multi else None
print("B=k+G; bistable band in beta:")
for s in (0.2,0.1,0.05,0.025):
    for k,G in ((0.4,0.4),(0.4,0.0),(0.0,0.4)):
        print(f"  s={s} k={k} G={G} B={k+G} 4s={4*s}: band={band(s=s,k=k,G=G)}")
# time to leave: start in Psi state (high psi), push beta high for T, then return to 0.70; does it stay out?
def simulate(Tpush,beta_push=0.97,beta_after=0.70,eps=0.1,d=1.0,zeta=1.0,nu=2.0,cu=0.6,s=0.1,k=0.4,a=0.4,b=1.0,T=400,dt=0.01):
    # start at the high-psi equilibrium for beta_after
    fp=fixed_points(beta_after,nu,cu,s,k,a*b/d); psi=max(fp); z=b*psi/d
    t=0.0
    while t<T:
        beta=beta_push if t<Tpush else beta_after
        Delta=(1-beta)*nu-cu+a*z-k*(1-psi)
        psi+=dt*zeta*(F(Delta/s)-psi); z+=dt*eps*(b*psi-d*z); t+=dt
    return psi
for eps in (0.1,0.03):
    for Tp in (1,2,3,4,5,6,8,10,15,20,25):
        if simulate(Tp,eps=eps)<0.5:
            print(f"eps={eps}: minimal push duration ~{Tp} (0.5/(eps d)={0.5/eps})");break
