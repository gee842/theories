"""Exact illustrations of the continuation verification argument.

Authored finite environments, not measurements or a solver for the full R2 game.
Policy values are solved from transition equations, then every action is checked.
"""

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


def solve(matrix, vector):
    """Exact Gauss-Jordan elimination; singular systems are rejected."""
    rows = [[F(x) for x in row] + [F(y)] for row, y in zip(matrix, vector)]
    n = len(rows)
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [x / scale for x in rows[col]]
        for i in range(n):
            if i != col:
                factor = rows[i][col]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]


def value(actions, policy, discount):
    states = list(actions)
    matrix = [[F(i == j) for j in range(len(states))] for i in range(len(states))]
    rewards = []
    for i, state in enumerate(states):
        action = actions[state][policy[state]]
        matrix[i][states.index(action['next'])] -= discount
        rewards.append(F(action['reward']))
    return dict(zip(states, solve(matrix, rewards)))


def certificate(actions, policy, discount, values):
    assert set(values) == set(actions), 'An off-path state is missing'
    residuals = {}
    for state, menu in actions.items():
        residuals[state] = {
            name: values[state] - F(a['reward']) - discount * values[a['next']]
            for name, a in menu.items()
        }
    evaluated = all(residuals[s][policy[s]] == 0 for s in actions)
    optimal = evaluated and all(v >= 0 for row in residuals.values() for v in row.values())
    return {'evaluated': evaluated, 'optimal': optimal, 'residuals': residuals}


def enumerate_policies(actions, discount):
    states = list(actions)
    records = []
    for names in product(*(list(actions[s]) for s in states)):
        policy = dict(zip(states, names))
        values = value(actions, policy, discount)
        check = certificate(actions, policy, discount, values)
        records.append({'policy': policy, 'values': values, **check})
    optimal = [x for x in records if x['optimal']]
    assert optimal, 'Finite discounted process has no accepted stationary optimum'
    assert all(x['values'] == optimal[0]['values'] for x in optimal)
    # Independent finite-policy comparison, separate from action residual checks.
    for candidate in optimal:
        for alternative in records:
            assert all(candidate['values'][s] >= alternative['values'][s] for s in states)
    return records


def funded_prefixes(actions, reserve):
    records = []
    for state, menu in actions.items():
        for name, action in menu.items():
            assert {'cost', 'gross', 'dividend'} <= set(action)
            after_cost = reserve - action['cost']
            after_receipt = after_cost + action['gross']
            after_dividend = after_receipt - action['dividend']
            assert after_cost >= 0 and after_dividend == reserve
            assert action['gross'] - action['cost'] == action['dividend'] == action['reward']
            records.append({'state': state, 'action': name, 'opening': reserve,
                            'after_cost': after_cost, 'after_receipt': after_receipt,
                            'dividend': action['dividend'], 'closing': after_dividend})
    return records


def main():
    folder = Path(__file__).resolve().parent
    fixture_path = folder / 'fixtures.json'
    fixtures = json.loads(fixture_path.read_text())
    records = []
    policy_count = 0
    for example in fixtures['processes']:
        actions = example['actions']
        prefixes = funded_prefixes(actions, example['reserve']) if 'reserve' in example else None
        for discount_text in example['discounts']:
            discount = F(discount_text)
            assert 0 <= discount < 1
            policies = enumerate_policies(actions, discount)
            policy_count += len(policies)
            candidate = example['candidate']
            values = value(actions, candidate, discount)
            check = certificate(actions, candidate, discount, values)
            if example['id'] == 'changed_opportunity':
                assert values == {'H': 3 / (1 - discount), 'X': 6 / (1 - discount)}
                assert check['residuals']['H']['attack'] == (1 - 4 * discount) / (1 - discount)
                assert check['optimal'] == (discount <= F(1, 4))
            elif example['id'] == 'future_support':
                assert values['O'] == 2 + 6 * discount / (1 - discount)
                assert check['residuals']['O']['defect'] == (-1 + 4 * discount) / (1 - discount)
                assert check['optimal'] == (discount >= F(1, 4))
            elif example['id'] == 'off_path_two_step':
                assert values == {'S': F(2), 'A': F(1), 'C': F(20)}
                assert all(x >= 0 for x in check['residuals']['S'].values())
                assert check['residuals']['A']['advance'] == -9 and not check['optimal']
                optimum = next(x for x in policies if x['optimal'])
                assert optimum['values'] == {'S': F(5), 'A': F(10), 'C': F(20)}
            else:
                raise AssertionError('Unreviewed example')
            records.append({'id': example['id'], 'discount': discount,
                            'candidate_policy': candidate, 'candidate_values': values,
                            'candidate_certificate': check, 'policies': policies,
                            'funded_prefixes': prefixes})

    # A favorable invented continuation must fail the policy-evaluation equality.
    example = fixtures['processes'][0]
    forged = certificate(example['actions'], example['candidate'], F(1, 2), {'H': F(6), 'X': F(0)})
    assert not forged['evaluated'] and not forged['optimal']
    # Omitting the node at which a second deviation becomes profitable is invalid.
    example = next(x for x in fixtures['processes'] if x['id'] == 'off_path_two_step')
    missing_rejected = False
    try:
        certificate(example['actions'], example['candidate'], F(1, 2), {'S': F(2), 'C': F(20)})
    except AssertionError:
        missing_rejected = True
    assert missing_rejected

    game = fixtures['two_stage_game']
    respect = game['respect']
    punishment = game['after_attack']['punish']
    tolerance = game['after_attack']['tolerate']
    assert respect[0] > punishment[0]  # Best response to the stipulated threat.
    assert tolerance[1] > punishment[1]  # The threat fails at its own decision node.
    assert tolerance[0] > respect[0]  # Backward induction selects attack/tolerance.
    result = {
        'status': 'pass', 'scope': fixtures['scope'],
        'fixture_sha256': hashlib.sha256(fixture_path.read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'process_discount_cases': len(records), 'stationary_policies_evaluated': policy_count,
        'results': records,
        'invalid_certificates_rejected': ['fabricated continuation value', 'missing off-path state'],
        'two_stage_game': {'fixed_threat_operator_best_reply': 'respect',
                           'trustee_credible_response': 'tolerate',
                           'backward_induction_outcome': 'attack then tolerate'},
        'limits': ['Authored examples, not empirical observations.',
                   'Enumerations corroborate finite examples, not the general written proof.',
                   'No integration with the full R2 game or physical learner is asserted.',
                   'Rewards, transitions, gross receipts and ethical interpretations are supplied.']
    }
    encoded = json.dumps(result, default=lambda x: str(x) if isinstance(x, F) else x,
                         ensure_ascii=False, indent=2) + '\n'
    (folder / 'results.json').write_text(encoded)
    print(json.dumps({k: result[k] for k in ['status', 'process_discount_cases',
                                           'stationary_policies_evaluated']}))


if __name__ == '__main__':
    main()
