"""New-this-cycle exact synthetic witness; not the inherited experiment.

Enumerates all 64 equally probable assignments of six binary attributes and
each of the inherited generator's 73 single-predicate policies. No randomness,
observed data, participant, or statistical estimate is involved.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json

contexts = list(product((0, 1), repeat=6))
assert len(contexts) == 64 and len(set(contexts)) == 64
grammar = [()]
grammar += [((i, v),) for i in range(6) for v in (0, 1)]
grammar += [((i, a), (j, b)) for i, j in combinations(range(6), 2)
            for a, b in product((0, 1), repeat=2)]
assert len(grammar) == len(set(grammar)) == 73
truth = tuple((i, 1) for i in range(4))

def match(x, terms):
    return all(x[i] == v for i, v in terms)

def name(terms):
    return 'all' if not terms else '&'.join(f'x{i}={v}' for i, v in terms)

def gain(terms):
    return sum((F(3, 4) * match(x, truth) - F(1, 4)) * match(x, terms)
               for x in contexts) / 64

def record(terms):
    selected = [x for x in contexts if match(x, terms)]
    hazardous_selected = [x for x in selected if match(x, truth)]
    return {'predicate': name(terms), 'terms': terms,
            'selected_support_count': len(selected),
            'hazardous_selected_support_count': len(hazardous_selected),
            'gain_fraction': str(gain(terms)), 'gain_decimal': float(gain(terms))}

all_gains = [gain(p) for p in grammar]
best = max(all_gains)
correct = gain(truth)
assert best == -F(1, 64)
assert correct == F(1, 32)
assert all(g < 0 for g in all_gains)
result = {
    'provenance': 'New-this-cycle exact synthetic witness, not inherited held-out experiment',
    'kind': 'Finite exhaustive enumeration, not sampled performance evaluation',
    'model': {
        'attributes': 6, 'uniform_binary_support_size': 64,
        'hazard_terms': truth, 'hazard_support_count': 4,
        'extra_failure_probability_under_A_in_hazard': '3/4',
        'extra_action_cost_of_B': '1/4',
        'failure_probability_A_outside_hazard_and_B_everywhere': '1/20',
        'gain_reference': 'Always A',
        'policy_class': 'Use B for one supplied predicate; A outside',
        'candidate_max_literal_count': 2,
        'composition_limit': 'No conjunctions of multiple candidate predicates in a policy. Such composition would expand the implemented class.'
    },
    'support': [{'x': x, 'hazard': match(x, truth),
                 'benefit_of_B_minus_cost_fraction':
                     str(F(3, 4) * match(x, truth) - F(1, 4))}
                for x in contexts],
    'all_73_policies': [record(p) for p in grammar],
    'best_supplied_policy_gain_fraction': str(best),
    'best_supplied_policy_gain_decimal': float(best),
    'best_supplied_policies': [name(p) for p in grammar if gain(p) == best],
    'unavailable_four_literal_policy': record(truth),
    'always_A_gain_fraction': '0',
    'checks': {
        'all_64_contexts_enumerated': True,
        'all_73_distinct_predicates_enumerated': True,
        'all_available_predicate_policy_gains_negative': True,
        'four_literal_policy_gain_positive': True
    }
}
out = Path(__file__).with_name('grammar-witness-results.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['provenance', 'best_supplied_policy_gain_fraction',
      'best_supplied_policies', 'unavailable_four_literal_policy', 'checks']}, indent=2))
