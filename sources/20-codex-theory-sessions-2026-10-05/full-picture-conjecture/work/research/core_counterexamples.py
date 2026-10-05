"""Exact finite checks for the full-picture research synthesis.

These are constructed counterexamples, not empirical data.
Run from any directory; only this session's work directory is written.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def distribution(model, do_x=None):
    law = {}
    for u in (0, 1):
        x = u if do_x is None else do_x
        y = x if model == 'mediated' else u
        law[(x, y)] = law.get((x, y), F(0)) + F(1, 2)
    return law


observed_a = distribution('mediated')
observed_b = distribution('common_cause')
assert observed_a == observed_b
do_a = sum(p for (x, y), p in distribution('mediated', 1).items() if y == 1)
do_b = sum(p for (x, y), p in distribution('common_cause', 1).items() if y == 1)
assert do_a == 1 and do_b == F(1, 2)

reversal = [{'forecast': bit, 'response': 1-bit, 'correct': bit == 1-bit}
            for bit in (0, 1)]
assert not any(row['correct'] for row in reversal)

# Adding duplicate labels changes the raw action count, not reachable states.
actions_a = {'renew': 'safe', 'consume': 'failed'}
actions_b = {'renew': 'safe', 'renew_copy_1': 'safe',
             'renew_copy_2': 'safe', 'consume': 'failed'}
assert len(actions_a) != len(actions_b)
assert set(actions_a.values()) == set(actions_b.values())

# Same total support does not preserve a person-specific entitlement predicate.
states = [(1, 0), (0, 1)]
assert sum(states[0]) == sum(states[1])
assert (states[0][0] >= 1) != (states[1][0] >= 1)

# Same two-state cycle has no instantaneous unique equilibrium interpretation.
fixed_boolean_equal = [(x, y) for x in (0, 1) for y in (0, 1)
                      if x == y and y == x]
fixed_boolean_reverse = [(x, y) for x in (0, 1) for y in (0, 1)
                        if x == 1-y and y == x]
assert fixed_boolean_equal == [(0, 0), (1, 1)]
assert fixed_boolean_reverse == []

result = {
    'kind': 'exact finite constructed counterexamples',
    'observational_equivalence': {
        'natural_joint_distribution': {str(k): str(v) for k, v in observed_a.items()},
        'P_Y1_do_X1_mediated': str(do_a),
        'P_Y1_do_X1_common_cause': str(do_b),
    },
    'public_binary_prediction_reversal': reversal,
    'action_label_counts': [len(actions_a), len(actions_b)],
    'same_reachable_outcomes': sorted(set(actions_a.values())),
    'same_total_different_person_A_protection': states,
    'instantaneous_boolean_cycle_solutions': {
        'x_equals_y_y_equals_x': fixed_boolean_equal,
        'x_equals_not_y_y_equals_x': fixed_boolean_reverse,
    },
    'checks_passed': 9,
}
destination = Path(__file__).with_name('core-counterexamples-results.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
