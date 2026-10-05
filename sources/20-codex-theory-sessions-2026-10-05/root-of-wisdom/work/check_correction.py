"""Exact finite illustrations, not an empirical test of wisdom.

Probe spending is a separate hard resource constraint, not operating loss.
Expected operating loss is required in each declared world; it is not a
pathwise guarantee. The two-world mixture optimum is computed independently
of the closed-form answer by intersecting every pair of risk vectors with
the equal-risk diagonal, as well as checking every pure policy.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json

LOSS = {'A': {'a': F(0), 'b': F(8), 'wait': F(3)},
        'B': {'a': F(8), 'b': F(0), 'wait': F(3)},
        'C': {'a': F(8), 'b': F(8), 'wait': F(3)}}

def risks(error, actions=('a', 'b', 'wait'), informative=True):
    points = []
    for pair in product(actions, repeat=2):
        if not informative and pair[0] != pair[1]:
            continue
        vector = tuple((1-error)*LOSS[w][pair[i]] + error*LOSS[w][pair[1-i]]
                       for i, w in enumerate(('A', 'B')))
        points.append((pair, vector))
    return points

def exact_two_world_minimax(points):
    candidates = [(max(v), {'policy': list(p)}, v) for p, v in points]
    for (p, v), (q, u) in combinations(points, 2):
        dv, du = v[0]-v[1], u[0]-u[1]
        if dv == du:
            continue
        weight = -du/(dv-du)
        if 0 <= weight <= 1:
            z = tuple(weight*x+(1-weight)*y for x,y in zip(v,u))
            candidates.append((max(z), {'first':list(p), 'second':list(q),
                                        'first_weight':str(weight)}, z))
    return min(candidates, key=lambda item:item[0])

rows = []
for label,e,budget,timely,signal,actions in [
    ('ordinary observations', F(1,10), 0, True, True, ('a','b','wait')),
    ('funded timely probe', F(1,10), 1, True, True, ('a','b','wait')),
    ('probe arrives late', F(1,10), 1, False, True, ('a','b','wait')),
    ('probe signal cannot inform action', F(1,10), 1, True, False, ('a','b','wait')),
    ('response a unavailable', F(1,10), 1, True, True, ('b','wait')),
    ('uninformative probe', F(1,2), 1, True, True, ('a','b','wait')),
    ('noisier probe', F(1,5), 1, True, True, ('a','b','wait')),
    ('perfect probe', F(0), 1, True, True, ('a','b','wait')),
    ('reversed labels known', F(9,10), 1, True, True, ('a','b','wait')),
    ('threshold equality', F(1,8), 1, True, True, ('a','b','wait')),
]:
    available = budget >= 1 and timely and signal
    points = risks(e, actions, available)
    value, witness, vector = exact_two_world_minimax(points)
    rows.append({'case':label, 'error':str(e), 'budget':budget,
                 'informative_probe_usable':available,
                 'minimax_expected_operating_loss':str(value),
                 'meets_per_world_expected_bound_one':value<=1,
                 'witness':witness, 'world_risks':list(map(str, vector))})

# Independent analytic lower bound and attainable symmetric policy.
for numerator in range(101):
    e = F(numerator,100)
    exact, _, _ = exact_two_world_minimax(risks(e))
    assert exact == min(F(3), 8*min(e,1-e))
assert [r['minimax_expected_operating_loss'] for r in rows] == [
    '3','4/5','3','3','3','3','8/5','0','4/5','1']

# In C every action has loss at least 3. Always waiting attains 3 in all
# worlds, proving expanded-model minimax 3 even with arbitrary lotteries.
assert min(LOSS['C'].values()) == 3
assert all(LOSS[w]['wait'] == 3 for w in LOSS)
rows.append({'case':'add omitted world C', 'minimax_expected_operating_loss':'3',
             'meets_per_world_expected_bound_one':False,
             'witness':{'policy':['wait','wait']},
             'old_probe_policy_loss_in_C':'8'})

# A stronger demand that loss <= 1 on every realized path fails for any
# nonzero, nonunit symmetric error: both worlds can yield either signal,
# while their acceptable action sets {a} and {b} are disjoint.
assert {a for a in LOSS['A'] if LOSS['A'][a] <= 1}.isdisjoint(
       {a for a in LOSS['B'] if LOSS['B'][a] <= 1})

report = {'status':'exact rational constructed examples',
          'assumptions':['one free routine observation identical in A and B',
                         'known binary symmetric probe, cost one, duration one',
                         'deadline one; final action has zero modeled duration',
                         'probe does not change the hidden world or cause harm',
                         'probe spending constrained separately from operating loss',
                         'conditional action computation and interpretation are supplied'],
          'checks':{'noise_grid_values':101,'scenario_cases':len(rows),
                    'all_checks_passed':True}, 'cases':rows}
out=Path(__file__).resolve().parents[1]/'outputs'/'worked-test-results.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report['checks']))
for row in rows:
    print(row['case'], row['minimax_expected_operating_loss'])
