"""Independent calculations for second V6.2 review; stdlib only."""
import math

def sigmoid(u):
    return 1/(1+math.exp(-u)) if u >= 0 else math.exp(u)/(1+math.exp(u))

def step(u,z,G,dt):
    def f(a,b): return b-1,G*sigmoid(a)-b
    a,b=f(u,z);c,d=f(u+dt*a/2,z+dt*b/2);e,fv=f(u+dt*c/2,z+dt*d/2);g,h=f(u+dt*e,z+dt*fv)
    return u+dt*(a+2*c+2*e+g)/6,z+dt*(b+2*d+2*fv+h)/6

def run(u,z,G,T,dt=.001):
    for i in range(math.ceil(T/dt)):
        u,z=step(u,z,G,min(dt,T-i*dt))
    return u,z

def insulated(u0,G,T): return u0+G*(-math.expm1(-T))-T,G*math.exp(-T)
def fate(u,z,G=2):
    u,z=run(u,z,G,100)
    return 'absence' if u<0 else 'capture',u,z

def threshold(u0,G=2):
    lo,hi=0,40
    for _ in range(36):
        m=(lo+hi)/2
        if fate(*insulated(u0,G,m),G)[0]=='absence':hi=m
        else:lo=m
    return (lo+hi)/2

print('MIXED SIGNAL')
mu,w,kS,kR,GS,GR=.5,.6,-.05,.05,.4,.2
sigR=(1-mu)*(1-w)/(mu*w);rho=kR/GR;post=(1-mu)/(1-mu+mu*sigR)
print('sigma_R, rho_E, posterior_E =',sigR,rho,post)
print('R payoffs E,N:',rho*GR-kR,0,'; S payoffs E,N:',rho*GS-kS,0)
print('Under core deterministic tie rule receiver must use rho=1, so R strictly chooses E:',GR-kR,'>',0)

print('\nDWELL G=2, equal speeds')
u0=math.log(99);T=threshold(u0)
print('Threshold:',T)
for dt in [-.001,.001]:print('T',T+dt,'release',insulated(u0,2,T+dt),'fate',fate(*insulated(u0,2,T+dt)))
for x0 in [.9,.99,.999]:print('depth',math.log(x0/(1-x0)),'duration threshold',threshold(math.log(x0/(1-x0))))
print('Continuity + open basin => first crossing lies on stable manifold, converges to saddle, infimum not minimum.')

print('\nPULSES: G=2, insulation 0.2 then restored conversion 0.05, no floor')
u,z=u0,2
for cycle in range(1,81):
    u,z=run(u,z,0,.2)
    u,z=run(u,z,2,.05)
    if cycle in [1,10,20,40,80]: print('cycles',cycle,'share',sigmoid(u),'support',z,'release fate',fate(u,z)[0])

print('\nSPRT COUNTEREXAMPLE: informative independent but nonidentical readings')
a=.01;b=.05/7;A=math.log((1-b)/a);B=math.log(b/(1-a))
# Under H0, X_t ~ Bernoulli(.5); H1, X_t ~ Bernoulli(.5+2^(-t-4)), t>=1.
# Every correct log likelihood increment belongs to [log(1-2 epsilon_t),log(1+2 epsilon_t)].
lo=sum(math.log1p(-2**(-t-3)) for t in range(1,1000));hi=sum(math.log1p(2**(-t-3)) for t in range(1,1000))
print('boundaries',B,A,'but every partial sum lies in',lo,hi)
assert B<lo<hi<A
print('Neither boundary can ever be reached; all readings are informative, independent, correctly modeled.')
