from itertools import product
import json
from pathlib import Path

# Outcome tuples are independently declared harm/burden components to be minimized.
# No weighted sum of components is used.
def dominates(x, y):
    return all(a <= b for a, b in zip(x, y)) and any(a < b for a, b in zip(x, y))

def minima(table):
    return [a for a, x in table.items() if not any(dominates(y, x) for b, y in table.items() if a != b)]

# 1. Flatten the two possible worlds' two protected interests.
case1 = {'left': (0, 0, 0, 1), 'right': (1, 0, 0, 0), 'defer': (1, 1, 1, 1), 'probe_then_match': (0, 0, 0, 0)}
assert minima(case1) == ['probe_then_match']
assert all(dominates(case1['probe_then_match'], case1[a]) for a in ('left', 'right', 'defer'))
# Probe cost 1 fits the independently declared budget 1. Static policies cost 0.
assert {'left': 0, 'right': 0, 'defer': 0, 'probe_then_match': 1}['probe_then_match'] <= 1

# 2. Both policies avoid outcome harm in either world; inquiry adds a privacy burden.
case2 = {'common_action': (0, 0, 0, 0), 'probe_then_common': (0, 1, 0, 1)}
assert minima(case2) == ['common_action']

# 3. Two protected persons have a certain conflicting allocation.
case3 = {'help_A': (0, 1), 'help_B': (1, 0), 'defer': (1, 1)}
assert set(minima(case3)) == {'help_A', 'help_B'}

# 4. The ideal prevention is outside the agent's feasible response set.
case4_world = {'prevention': (0,), 'available_response': (1,)}
case4_feasible = {'available_response': case4_world['available_response']}
assert minima(case4_world) == ['prevention']
assert minima(case4_feasible) == ['available_response']
assert case4_feasible['available_response'] != case4_world['prevention']

# 5. Old outcome interface, observations, and routine histories agree across worlds.
old_observation = {'safe': 'output=1', 'toxic': 'output=1'}
assert old_observation['safe'] == old_observation['toxic']
# Every deterministic detector over that observation has identical outputs.
for detector_output in (False, True):
    detector = {'output=1': detector_output}
    assert detector[old_observation['safe']] == detector[old_observation['toxic']]
old_outcomes = {'operate': (0,), 'stop': (1,)}
assert minima(old_outcomes) == ['operate']
expanded_outcomes_toxic = {'operate': (0, 2), 'stop': (1, 0), 'filter': (0, 0)}
assert minima(expanded_outcomes_toxic) == ['filter']
# New, independently declared constraint: forbid an imposed serious irreversible harm (2).
allowed_before_filter = {a: h for a, h in expanded_outcomes_toxic.items() if a != 'filter' and max(h) < 2}
assert minima(allowed_before_filter) == ['stop']

result = {
    'status': 'five exact synthetic witnesses checked',
    'meaning': 'arithmetic, order, feasibility, and indistinguishability checks only; not a wisdom benchmark',
    'case1_minimal_policy': minima(case1),
    'case2_minimal_policy': minima(case2),
    'case3_unresolved_minimal_set': minima(case3),
    'case4_feasible_minimal_set': minima(case4_feasible),
    'case5_old_minimal_set': minima(old_outcomes),
    'case5_expanded_minimal_set': minima(expanded_outcomes_toxic),
}
Path('work/root-formalization-cases-check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
