"""Minimal independent calculations for general-standing counterexamples."""
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

if __name__=='__main__':
    audit_private(); audit_balanced(); audit_endpoint()
