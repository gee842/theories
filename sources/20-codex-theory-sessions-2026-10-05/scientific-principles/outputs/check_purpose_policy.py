"""Independent input-contrast checks of the proposed ballot, not full system audit."""
import copy
import json
from purpose_policy import hearing_decision

base = dict(service={'A': {'n':16, 'error':0}, 'B': {'n':16, 'error':.5}},
            pilot={'incumbent':{'A':0, 'B':.5}, 'edited':{'A':0, 'B':0}},
            extra_round_cost=.15, cash_after_hearing=20,
            next_required_payment=2, reserve_floor=5, usable_checker=True)
contrasts = {'canonical': base}
for name in ['similar_groups','no_benefit','costly','a_harm','poor_liquidity',
             'no_checker','insufficient_record']:
    contrasts[name] = copy.deepcopy(base)
contrasts['similar_groups']['service']['B']['error'] = 0
contrasts['no_benefit']['pilot']['edited']['B'] = .5
contrasts['costly']['extra_round_cost'] = .6
contrasts['a_harm']['pilot']['edited']['A'] = 1/32
contrasts['poor_liquidity']['cash_after_hearing'] = 6.99
contrasts['no_checker']['usable_checker'] = False
contrasts['insufficient_record']['service']['B']['n'] = 15
results = {name: hearing_decision(**case) for name,case in contrasts.items()}
assert results['canonical']['adopt']
assert [v['yes'] for v in results['canonical']['votes']] == [False, True, True]
assert results['canonical']['gain_under_old_mandate'] == -.15
assert abs(results['canonical']['gain_under_inclusive_mandate']-.10) < 1e-12
assert all(not r['adopt'] for name,r in results.items() if name != 'canonical')
print(json.dumps({'status':'passed','scope':'branch contrasts only','results':results},indent=2))
