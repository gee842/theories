import math
r,Gamma,beta,Om,kap,d,c,l,delta,N=1.5,0.6,0.0,1.0,0.5,0.2,1.0,0.0,0.9,100
om=Gamma/((1-beta)*r); k0=kap*Om*(1/om-1)/2; S=(kap*Om+2*k0)/d; m=kap*Om*(1-beta)/S
print('k0',k0,'S',S,'m',m)
grid=[i/N for i in range(N+1)]
V=[0.0]*(N+1)
def interp(arr,x):
    if x<=0: return arr[0]
    if x>=1: return arr[-1]
    k=min(int(x*N),N-1); w=x*N-k; return arr[k]*(1-w)+arr[k+1]*w
def deriv(V):
    D=[0.0]*(N+1)
    for i in range(1,N): D[i]=(V[i+1]-V[i-1])*N/2
    D[0]=(V[1]-V[0])*N; D[N]=(V[N]-V[N-1])*N
    return D
def sp(s,p): return (1-d)*s+(kap*Om*((1-beta)*p+beta/2)+k0)/S
for it in range(60):
    D=deriv(V); Vn=[0]*(N+1); info=[]
    for i,s in enumerate(grid):
        if s<=0 or s>=1:
            p=0.0 if s<=0 else 1.0; e1=e2=0.0
        else:
            lr=r*math.log(s/(1-s))
            Fp=lambda p: Om*(1-beta)+delta*m*interp(D,sp(s,p))
            Gp=lambda p: Om*(1-beta)+delta*m*interp(D,1-sp(s,p))
            def H(p):
                a,b=Fp(p),Gp(p)
                if a<=0: return 1e9
                if b<=0: return -1e9
                return math.log(p/(1-p))-lr-math.log(a)+math.log(b)
            lo,hi=1e-12,1-1e-12
            for _ in range(80):
                mid=(lo+hi)/2
                if H(mid)>0: hi=mid
                else: lo=mid
            p=(lo+hi)/2
            e1=max(Fp(p),0)*p*(1-p)/(c+l); e2=max(Gp(p),0)*p*(1-p)/(c+l)
        W1=Om*((1-beta)*p+beta/2)
        Vn[i]=W1-c*e1-l*(e1+e2)+delta*interp(V,sp(s,p))
    diff=max(abs(a-b) for a,b in zip(V,Vn))
    V=Vn
    if it%5==0 or it>50:
        print(it,'diff',round(diff,6),'V(.5)',round(V[N//2],4),'Vmin',round(min(V),3),'Vmax',round(max(V),3),'minD',round(min(D),3),'maxD',round(max(D),3), 'D(.5)',round(D[N//2],4))
