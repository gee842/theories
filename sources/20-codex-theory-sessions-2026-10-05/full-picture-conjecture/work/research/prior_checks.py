"""Independent, read-only-reference checks for the prior-results audit.

Run from any directory. This script reads and changes no source-workspace files.
Only standard-library arithmetic is used; output is a compact JSON certificate.
"""
from fractions import Fraction as F
from itertools import product
import json
import math

out = {}

# U20: likelihoods of switch words under the ordered models.
rates = ((F(1,20),)*2+(F(9,20),)*2,
         (F(9,20),)*2+(F(1,20),)*2)
def likelihood(word, rate):
    p = F(1)
    for z, h in zip(word, rate):
        p *= h if z else 1-h
    return p
predictions = []
for word in ((0,0,1,1), (1,1,0,0)):
    a, b = (likelihood(word, rate) for rate in rates)
    w = a/(a+b)
    predictions.append(F(1,20)+F(2,5)*w)
assert predictions[0] > F(3,10) > predictions[1]
for count in range(5):
    law = [sum((likelihood(z, rate) for z in product((0,1), repeat=4)
                if sum(z)==count), F(0)) for rate in rates]
    assert law[0] == law[1]
out['U20_same_count_opposite_actions'] = {
    'predictions': [float(p) for p in predictions],
    'all_five_count_masses_equal': True,
}

# U24: solve the two-state lifetime equations exactly, then check both.
e1, e2 = F(4), F(6)
assert e1 == 1+e2/2
assert e2 == 1+e1/2+e2/2
out['U24_positive_uncapped_return_ruin'] = {
    'uncapped_net_income': .5, 'lifetime_from_1': float(e1),
    'lifetime_from_2': float(e2),
    'spectral_radius': (1+math.sqrt(5))/4,
}

# U27: cash minimum from integrated production, rather than using the result
# as the numerical function being checked.
A,D,delta=1.,3.,1.
t=math.log(D/A)/delta
cash_change=A*t-D*(1-math.exp(-delta*t))/delta
bridge=(D-A-A*math.log(D/A))/delta
assert abs(cash_change+bridge) < 1e-14
assert abs(A-D*math.exp(-delta*t)) < 1e-14
out['U27_bridge']={'time_of_dip':t,'minimum_cash_change':cash_change,
                  'required_bridge':bridge}

# U26: compute information necessity for a binary 90%-accurate paid test.
def kl(p,q):
    return p*math.log(p/q)+(1-p)*math.log((1-p)/(1-q))
information_requirement=kl(.9,.05)
information_per_test=kl(.9,.1)
out['U26_necessary_sample_floor']={
    'alpha':.05,'power':.9,'ordinary_divergence':0,
    'required_divergence':information_requirement,
    'test_divergence':information_per_test,
    'necessary_number':math.ceil(information_requirement/information_per_test),
    'not_a_sufficiency_certificate':True,
}
# Exact Neyman--Pearson enumeration for all two-sample outcomes.
test_rows=[]
for word in product((0,1),repeat=2):
    p0=likelihood(word,(F(1,10),)*2)
    p1=likelihood(word,(F(9,10),)*2)
    test_rows.append((p1/p0,word,p0,p1))
remaining_size=F(5,100); two_test_max_power=F(0); np_rule=[]
for ratio,word,p0,p1 in sorted(test_rows,reverse=True):
    used=min(remaining_size,p0)
    accept=used/p0
    two_test_max_power+=accept*p1
    remaining_size-=used
    np_rule.append({'word':word,'p0':str(p0),'p1':str(p1),
                    'likelihood_ratio':str(ratio),'accept_probability':str(accept)})
assert two_test_max_power == F(85,100)
three_test_size=F(1,10)**3+3*F(1,10)**2*F(9,10)
three_test_power=F(9,10)**3+3*F(9,10)**2*F(1,10)
assert two_test_max_power < F(9,10)
assert three_test_size <= F(5,100) and three_test_power >= F(9,10)
out['U26_necessary_not_sufficient']={
    'two_test_exact_max_power_at_size_005':float(two_test_max_power),
    'two_test_exact_np_rule':np_rule,
    'three_test_at_least_two_positive_size':float(three_test_size),
    'three_test_at_least_two_positive_power':float(three_test_power),
}

# U18: independent risk subtraction for stationary-prior historical state.
values=[]
for age in range(1,5):
    r=(1-(1-2*.2)**age)/2
    direct=min(4.,10.*.5)-.5*(min(4.,10.*r)+min(4.,10.*(1-r)))
    formula=10./4*max(0.,(1-2*.2)**age-abs(1-2*4./10))
    assert abs(direct-formula)<1e-14
    values.append(direct)
out['U18_historical_decision_values_ages_1_to_4']=values

# U10: integrate the specified logistic adoption/maturation using its
# independent analytic antiderivative and locate the flow sign change.
seed=.01; eta=2.; lag=2.; speed=1.; q=seed/(1-seed)
w=(math.exp(speed*lag)-eta)/(eta-1)
tstar=math.log(w/q)/speed
def adoption(t): return q*math.exp(speed*t)/(1+q*math.exp(speed*t))
def adoption_integral(t):
    return (math.log1p(q*math.exp(speed*t))-math.log1p(q))/speed
reserve_change=eta*(seed*lag+adoption_integral(tstar-lag))-adoption_integral(tstar)
assert abs(eta*adoption(tstar-lag)-adoption(tstar))<1e-14
assert abs(-reserve_change-.729169)<5e-7
out['U10_transition_reserve']={'time_of_minimum':tstar,
                            'required_reserve':-reserve_change}

# State compression counterexample: the total is identical, but a required
# prepaid cost has different feasibility when the second account is barred.
states=((1,4),(0,5)); cost=1
assert sum(states[0])==sum(states[1])
assert (states[0][0]>=cost) != (states[1][0]>=cost)
out['typed_access_counterexample']={'states':states,'total':5,'cost':1,
                                 'feasible':[True,False]}

print(json.dumps(out,indent=2))
