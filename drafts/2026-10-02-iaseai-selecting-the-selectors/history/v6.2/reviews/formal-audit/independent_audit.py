"""Independent V6.2 formal audit. Standard library only; no manuscript code imported.

Run: python3 reviews/formal-audit/independent_audit.py
The lottery Bellman solver is intentionally independent of checks_v62.py. It
compares three distinct objects: the exact lottery prize premium, an infinitesimal
stock injection's marginal value, and the asserted local resolvent formula.
"""
import json
import math


def lottery(ncells, gamma=.45, r=4., d=.1, discount=1/1.1):
    omega = gamma/r
    step = d*omega
    grid = [i/ncells for i in range(ncells+1)]
    low = [(1-d)*s + d*(1-omega)/2 for s in grid]
    high = [s+step for s in low]
    weights = [(s**r, (1-s)**r) for s in grid]
    def sample(values, point):
        i = min(max(int(point*ncells), 0), ncells-1)
        fraction = point*ncells-i
        return values[i]*(1-fraction)+values[i+1]*fraction
    def actions(i, values):
        a,b = weights[i]
        prize1 = 1+discount*(sample(values,high[i])-sample(values,low[i]))
        prize2 = 1+discount*(sample(values,1-low[i])-sample(values,1-high[i]))
        assert prize1 > 0 and prize2 > 0
        p = a*prize1/(a*prize1+b*prize2)
        effort1=prize1*p*(1-p)
        effort2=prize2*p*(1-p)
        return p,effort1,effort2
    value=[0.]*(ncells+1)
    for iteration in range(5000):
        updated=[]
        for i in range(ncells+1):
            p,e,_=actions(i,value)
            updated.append(p-e+discount*(p*sample(value,high[i])+(1-p)*sample(value,low[i])))
        error=max(abs(x-y) for x,y in zip(value,updated))
        value=updated
        if error<1e-12:
            break
    mid=ncells//2
    p,effort,_=actions(mid,value)
    def frozen_probability(i):
        _,_,rival_effort=actions(i,value)
        a,b=weights[i]
        return a*effort/(a*effort+b*rival_effort)
    h=1/ncells
    rpr=(frozen_probability(mid+1)-frozen_probability(mid-1))/(2*h)
    req=(actions(mid+1,value)[0]-actions(mid-1,value)[0])/(2*h)
    gpr=discount*d*omega*rpr/(1-discount*(1-d))
    premium=discount*(sample(value,high[mid])-sample(value,low[mid]))
    marginal=discount*d*omega*(value[mid+1]-value[mid-1])/(2*h)
    predicted=gpr/(1-gpr)
    return dict(cells=ncells,iterations=iteration+1,residual=error,
                structural_gamma=gamma,equilibrium_gamma=omega*req,
                partial_discounted_gain=gpr,local_formula=predicted,
                lottery_prize_premium=premium,marginal_stock_injection=marginal,
                formula_relative_error=predicted/premium-1)


def main():
    output={}
    # Positive rate, autonomous/payoff-monotone selection can run out of force.
    # xdot=x(1-x)*(payoff_gap)^2, gap=1/(1+t), integrates to one.
    x0=.1
    xlimit=1/(1+(1/x0-1)*math.exp(-1))
    output['payoff_monotone_counterexample']={
        'initial_race_share':x0,'limiting_race_share':xlimit,
        'raw_payoff_advantage_integral':'infinity: integral 1/(1+t) dt',
        'actual_log_odds_increment':1,
        'host_floor':.5,'rho':1,'load_coefficient':1,
        'reach_condition':'1 > 1*(1-.5)',
        'limiting_host':1-xlimit,
        'selection_rule':'dot p_i=p_i*gap*(pi_i-mean pi); gap=1/(1+t)>0',
    }
    output['theta_endpoint']={
        'n':4,'theta_held':-1,'relative_gain':.5,'common_gain':0,
        'theta_working':(4*(-1)-3*(1-1)*.5)/(4-(1-1)*.5),
    }
    output['exact_fixed_conduct_lottery']={
        'n':2,'prize':1,'conversion':1,'provision':.5,'depreciation':1,
        'decisiveness':2,'discount':.5,'symmetric_stock':1,
        'winner_next_stock':1.5,'loser_next_stock':.5,
        'leader_win_probability':.9,'retention_eigenvalue':.8,
        'discounted_gain':.5,'deterministic_local_price':1,
        'actual_lottery_marginal_price':.5/(1-.5*.8),
    }
    output['slow_breakout_timing']={
        'discount':.9,'cooperation':1,'immediate_gain':.3,
        'decisive_flow':1.5,'punishment_flow':0,'breakout_time':8,
        'escape_probability':.7,'detection_time_if_detected':1,
        'compressed_normalized_deviation_value':.1*1.3+.9*.7*1.5,
        'actual_normalized_deviation_value':.1*1.3+.7*(.9-.9**8+.9**8*1.5),
    }
    output['trait_background_scope']={
        'traits':[0,1],'background_payoffs':[0,2],'cost_per_trait':1,
        'shared_benefit':.5,'material_payoffs':[.5,1.5],
        'covariance_trait_payoff':.25,
    }
    output['frontier_rest_counterexample']={
        'n':4,'theta':-1,'private_destruction_cost':1,'rival_loss':1,
        'frontier_marginal_net':-1,'destruction_value':-1+1/3,
        'rest_value':0,'claimed_switch_inequality':(-1)<(-1+1/3),
        'actual_choice':'rest',
    }
    # A linear level channel has gain proportional to stakes even if omega fixed.
    output['multi_channel_pivot_scope']=[dict(prize=om,provision=om/2,
        omega=.5,stock=5*om,gamma=2.5*om)
        for om in (.2,.4,.8)]
    output['lottery']=[lottery(N) for N in (800,1600,3200)]
    output['lottery_stable_case']=[lottery(N,gamma=.3) for N in (800,1600,3200)]
    assert output['payoff_monotone_counterexample']['limiting_host'] > .5
    assert output['theta_endpoint']['theta_working'] == -1
    assert output['slow_breakout_timing']['compressed_normalized_deviation_value'] > 1
    assert output['slow_breakout_timing']['actual_normalized_deviation_value'] < 1
    assert output['lottery'][-1]['partial_discounted_gain'] < 1
    assert output['lottery'][-1]['formula_relative_error'] > .25
    print(json.dumps(output,indent=2))


if __name__=='__main__':
    main()
