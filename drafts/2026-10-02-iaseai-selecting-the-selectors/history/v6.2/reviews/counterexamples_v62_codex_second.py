"""Independent second review of V6.2, 4 October 2026.

Run: python3 counterexamples_v62_codex_second.py
Standard library only; does not import the manuscript/check implementation.
THEORY SHA256: f50fb6a1b0f71ce33374946ab77da607a9631998d390e619296e6549e6822872
Numeric examples establish model counterexamples, not real-world estimates.
"""
import math

def equilibrium(k1,k2):
    # FOC e_i=K_i*p*(1-p), so p=logistic((K1^2-K2^2)*p*(1-p)).
    lo,hi=0.,1.
    for _ in range(80):
        p=(lo+hi)/2
        target=1/(1+math.exp(-(k1*k1-k2*k2)*p*(1-p)))
        if p<target: lo=p
        else: hi=p
    p=(lo+hi)/2
    e1,e2=k1*p*(1-p),k2*p*(1-p)
    return p,e1,e2,p-e1*e1/2

def private_share(k1,k2):
    e2=equilibrium(k1,k2)[2]
    return 1/(1+math.exp(-(k1*.25-k2*e2)))

def audit_private():
    h=1e-5
    own=(private_share(1+h,1)-private_share(1-h,1))/(2*h)
    relative=(private_share(1+h,1-h)-private_share(1-h,1+h))/(2*h)
    net_relative=(equilibrium(1+h,1-h)[3]-equilibrium(1-h,1+h)[3])/(2*h)
    common=(equilibrium(1+h,1+h)[3]-equilibrium(1-h,1-h)[3])/(2*h)
    rpr=4*own
    assert abs(rpr-.25)<1e-8
    assert abs(relative-3/16)<1e-8
    assert abs(net_relative-3/16)<1e-8
    assert abs(common+1/16)<1e-8
    print('private elasticity:',dict(rpr=rpr,claimed_relative=rpr/2,
          actual_relative=relative,net_relative=net_relative,common=common))

def audit_balanced():
    # n=2, sigma=K, Omega=S, kappa=.2,d=.1,delta=.8,K*=1 at reference.
    # Sum first T derivatives of discounted future winnings per relative payoff.
    for horizon in (5,10,20,30,40):
        stock=1.; sensitivity=.2; pv=0.; disc=.8
        for _ in range(horizon):
            pv+=disc*stock*sensitivity
            sensitivity*=.9+.2*stock
            stock*=1.1; disc*=.8
        print('balanced relative derivative partial sum',horizon,pv)
    common=.8*.2/(1-.8*1.1)
    assert abs(common-4/3)<1e-12
    print('claimed relative and correct common price:',common)
    for epsilon in (1e-3,1e-6,1e-9,1e-12):
        base=1.; gap=.2*epsilon; value=0.; disc=.8
        for _ in range(1000):
            winnings=base*math.tanh(gap)
            value+=disc*winnings
            gap=.9*gap+.2*winnings
            base*=1.1; disc*=.8
        print('nonlinear relative value / epsilon',epsilon,value/epsilon)

def audit_endpoint():
    n=2; theta0=-1.; rel=.5; common=0.
    theta=(n*theta0-(n-1)*(1+theta0)*rel)/(n-(1+theta0)*rel)
    assert theta==theta0
    print('theta endpoint:',theta)


from fractions import Fraction as F
from math import exp


def delayed_detection():
    # t=0 deviation yields C+g. Pending dates yield C. With probability
    # 1-p it is detected/answered at t=9; otherwise decisive at t=10.
    # Eventual absorbing per-period payoffs are v and D, respectively.
    C, D, v, g, delta, p = F(1), F(3, 2), F(0), F(3, 10), F(9, 10), F(16, 25)
    printed = (1-delta)*g + delta*(p*(D-C)+(1-p)*(v-C))
    actual = (1-delta)*g + p*delta**10*(D-C) + (1-p)*delta**9*(v-C)
    printed_bound = ((C-v)-(1-delta)*g/delta)/(D-v)
    actual_bound = (delta**9*(C-v)-(1-delta)*g)/(delta**10*(D-C)+delta**9*(C-v))
    assert printed == F(-3, 500)
    assert actual == F(263215599, 125000000000)
    assert actual_bound < p < printed_bound
    print('delayed_detection', dict(printed=float(printed), actual=float(actual),
        printed_bound=float(printed_bound), actual_bound=float(actual_bound)))


def old_floor_counterexample_is_now_in_repaired_branch():
    # V6.1 falling-floor counterexample: alpha_cor=.05 > alpha_f=.01.
    # The revised floor branch predicts cultivation ends, correctly.
    rows = []
    for t in (0., .25, .5, 1., 10., 100.):
        d = 2*exp(.05*t)
        q = max(0., .5*exp(-.05*t)-.49*exp(-.01*t))*exp(.2*t)
        rows.append(q/d)
    assert all(0 <= x < 1 for x in rows)
    assert rows[-3:] == [0., 0., 0.]
    print('repaired_falling_floor', rows)


def cheap_talk_ideal_gap():
    # Direct quadratic derivative solutions, including common third-party slope.
    for n in (2, 3, 4, 6):
        for theta in (F(-1), F(0), F(1, 2), F(n-1)):
            if n-1+theta <= 0:
                continue
            b, L = F(1, 20), F(7, 3)
            sender = (2*b*(n-1)+theta*L)/(2*(n-1+theta))
            receiver = (2*theta*b+theta*L)/(2*(n-1+theta))
            assert sender-receiver == b*(n-1-theta)/(n-1+theta)
    print('cheap_talk_ideal_gap', 'exact identity confirmed')



import math

def sigmoid(u):
    return 1/(1+math.exp(-u)) if u >= 0 else math.exp(u)/(1+math.exp(u))

def step(u,z,G,dt):
    def f(a,b): return b-1,G*sigmoid(a)-b
    a,b=f(u,z);c,d=f(u+dt*a/2,z+dt*b/2);e,fv=f(u+dt*c/2,z+dt*d/2);g,h=f(u+dt*e,z+dt*fv)
    return u+dt*(a+2*c+2*e+g)/6,z+dt*(b+2*d+2*fv+h)/6

def run(u,z,G,T,dt=.005):
    for i in range(math.ceil(T/dt)):
        u,z=step(u,z,G,min(dt,T-i*dt))
    return u,z

def insulated(u0,G,T): return u0+G*(-math.expm1(-T))-T,G*math.exp(-T)
def fate(u,z,G=2):
    u,z=run(u,z,G,100)
    return 'absence' if u<0 else 'capture',u,z

def threshold(u0,G=2):
    lo,hi=0,40
    for _ in range(28):
        m=(lo+hi)/2
        if fate(*insulated(u0,G,m),G)[0]=='absence':hi=m
        else:lo=m
    return (lo+hi)/2


def audit_selection_clock():
    # Relative, strictly payoff-monotone selection can scale a payoff gap cubically.
    # nu=1, tau(t)=1-1/(1+t): raw cumulative advantage diverges, effective does not.
    p0 = .001
    limit = sigmoid(math.log(p0/(1-p0))+.5)
    assert .001 < limit < .00165
    rho, harm, floor = .05, .08, .3
    lower_host = 1-harm*limit/rho
    assert lower_host > floor
    print('cubic selection:', dict(initial_share=p0, limit_share=limit,
          host_lower_bound_from_V0_1=lower_host,
          raw_advantage_at_1e12=math.log1p(1e12)))


def audit_certificate_transient():
    # Evaluation receives b=.5 from a permanently captured external domain.
    # a=c=d=zeta=1, epsilon=.01; full row sum .5, x(0)=.9,z(0)=2.
    # z=.5+1.5 exp(-.01t); integrate the exact logit equation u'=z-1.
    def state(t):
        z = .5+1.5*math.exp(-.01*t)
        u = math.log(9)-.5*t+150*(-math.expm1(-.01*t))
        return sigmoid(u), z, u
    x50,z50,u50=state(50)
    assert x50 > .999999999999 and z50 > 1
    assert state(1000)[0] < 1e-100
    print('certified yet currently captured:', dict(row_sum=.5, x0=.9,
          x50=x50,z50=z50,log_odds50=u50,x1000=state(1000)[0]))


def audit_neutrality():
    # Equality of sanction and cost leaves the unsafe variant neutral.
    base, cost, sanction = F(1), F(1,5), F(1,5)
    assert base-cost == base-sanction
    p0 = F(1,2)
    assert p0*(1-p0)*((base-cost)-(base-sanction)) == 0
    # A zero alignment tax is likewise neutral, not adoption pressure.
    assert F(1)-F(0) == F(1)
    print('zero tax / equal sanction:', '50% unsafe stays 50% unsafe under replicator selection')


def audit_core_equality():
    # G=1 stays in a core pruned only below 1, but its captured corner is unstable.
    u,z=run(math.log(99),.99,1,1000)
    assert sigmoid(u)<1e-100 and z<1e-100
    print('gain-one surviving core:', dict(x0=.99,z0=.99,x1000=sigmoid(u),z1000=z))


def audit_recovery():
    capacity, target, floor, rate = .2, 1., .5, .1
    recovery = math.log((target-capacity)/(target-floor))/rate
    value = target-(target-capacity)*math.exp(-rate*recovery)
    assert abs(value-floor)<1e-12
    print('human capacity recovery:',dict(duration=recovery,recovered=value))


def audit_transition():
    mu,w,cS,cR,piS,piR=.5,.6,-.05,.05,.4,.2
    imitates=(1-mu)*(1-w)/(mu*w)
    receiver=cR/piR
    posterior=(1-mu)/(1-mu+mu*imitates)
    assert abs(posterior-w)<1e-12
    assert abs(receiver*piR-cR)<1e-12
    assert piR-cR>0
    print('signal mixing:', dict(imitation=imitates,receiver=receiver,posterior=posterior))
    durations=[]
    for x in (.9,.99,.999):
        duration=threshold(math.log(x/(1-x)))
        durations.append(duration)
    assert durations[0]<durations[1]<durations[2]
    u=math.log(99)
    assert fate(*insulated(u,2,durations[1]-.001))[0]=='capture'
    assert fate(*insulated(u,2,durations[1]+.001))[0]=='absence'
    print('dwell infima for shares .9,.99,.999:',durations)
    a,b=.01,.05/7
    A,B=math.log((1-b)/a),math.log(b/(1-a))
    lo=sum(math.log1p(-2**(-t-3)) for t in range(1,1000))
    hi=sum(math.log1p(2**(-t-3)) for t in range(1,1000))
    assert B<lo<hi<A
    print('informative independent SPRT that never stops:', dict(lower_boundary=B,
          all_paths_lower=lo,all_paths_upper=hi,upper_boundary=A))
    hazards=[1.,0.,0.]
    assert sum(hazards)==1 and math.prod(1-h for h in hazards)==0
    print('summable hazard boundary:', 'one hazard=1 makes survival zero')


if __name__ == '__main__':
    audit_private()
    audit_balanced()
    audit_endpoint()
    delayed_detection()
    old_floor_counterexample_is_now_in_repaired_branch()
    cheap_talk_ideal_gap()
    audit_selection_clock()
    audit_certificate_transient()
    audit_neutrality()
    audit_core_equality()
    audit_recovery()
    audit_transition()
    print('All independent second-review assertions passed.')
