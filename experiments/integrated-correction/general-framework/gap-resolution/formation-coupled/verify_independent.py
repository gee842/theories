"""Independent raw-case rational checks of representative formation transitions.

This checker does not call production portfolio, expression, physical-profile,
query, nomination, feasibility or transition functions to construct its rows.
It checks the frozen baseline join and, when present, the separate reopening
extension with its own explicitly changed inquiry and complaint-reset rules.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent


def independent(arm, state, reopening=False):
    k, q, complaint, n, e1, e2, frame, ratified = state
    train = k == 1 and q == 1 and arm.training
    query = k == 2 and q == 1 and complaint == 1 and (reopening or frame == -1)
    cases_per_round = 1 if train or query else 2
    # Explicitly draw each case's context, action, response noise and complaint.
    single = defaultdict(F)
    for x0, x1, action, noise, ticket in product((0, 1), repeat=5):
        predicted = ((x0, x1)[frame // 2] ^ (frame % 2)) if frame >= 0 else 0
        if query:
            p_action = F(1, 2)
        elif arm.execution and k > 0 and frame >= 0 and ratified:
            p_action = F(7, 8) * predicted
        else:
            p_action = F(0)
        probability = F(1, 4) * (p_action if action else 1 - p_action)
        probability *= F(1, 10) if noise else F(9, 10)
        harm = action ^ x0 ^ noise
        p_ticket = F(1, 2) if harm else F(0)
        probability *= p_ticket if ticket else 1 - p_ticket
        if probability:
            y = harm ^ action
            d1 = x0 ^ y if query and arm.linked else 0
            d2 = x1 ^ y if query and arm.linked else 0
            single[(harm, ticket, d1, d2, action)] += probability
    assert sum(single.values(), F()) == 1

    cases = {(0, 0, 0, 0, 0): F(1)}
    for _ in range(cases_per_round):
        updated = defaultdict(F)
        for a, pa in cases.items():
            for b, pb in single.items():
                outcome = (a[0] + b[0], a[1] | b[1], a[2] + b[2],
                           a[3] + b[3], a[4] + b[4])
                updated[outcome] += pa * pb
        cases = updated

    transitions, rewards = defaultdict(F), defaultdict(F)
    rewards['ordinary_cases'] = F(0 if query else cases_per_round)
    rewards['inquiry_cases'] = F(query)
    rewards['inquiry_slots'] = F(query)
    rewards['training_slots'] = F(train)
    rewards['nominations'] = F(query and n + 1 == 5)
    for (harms, ticket, d1, d2, action_one), p_case in cases.items():
        new_complaint = int(complaint or ticket)
        count = n + query
        count1, count2 = e1 + d1, e2 + d2
        completing = query and count == 5
        if completing and reopening:
            new_complaint = 0
        if completing:
            losses = (count1, 5 - count1, count2, 5 - count2)
            nominees = [j for j in range(4)
                        if not arm.linked or losses[j] == min(losses)]
        else:
            nominees = [frame]
        for next_frame in nominees:
            probability = p_case / len(nominees)
            counts = (0, 0, 0) if completing else (count, count1, count2)
            # Same candidate-assumed feasibility for every nominated expression.
            next_ratified = (int(F(str(arm.burden_cap)) >= F(7, 16))
                              if completing else ratified)
            pre_turnover_skill = 2 if train else k
            delta = F(1, 20) + F(harms, 5 * cases_per_round)
            before = (pre_turnover_skill, q, new_complaint, *counts,
                      next_frame, next_ratified)
            transitions[before] += probability * (1 - delta)
            remaining_skill = max(0, pre_turnover_skill - 1)
            package = pre_turnover_skill > 0 and bool(
                new_complaint or counts[0] or next_frame >= 0 or next_ratified)
            if remaining_skill == 0:
                transitions[(0, 0, 0, 0, 0, 0, -1, 0)] += probability * delta
            else:
                weight = F(4) if q else F(1, 4)
                p_adaptive = (F(1) if arm.protected else
                              remaining_skill * weight / (1 + remaining_skill * weight))
                retention = F(1) if arm.protected else F(9, 10)
                for next_q, p_q in [(0, 1 - p_adaptive), (1, p_adaptive)]:
                    full = (remaining_skill, next_q, new_complaint, *counts,
                            next_frame, next_ratified)
                    empty = (remaining_skill, next_q, 0, 0, 0, 0, -1, 0)
                    transitions[full] += probability * delta * p_q * retention
                    transitions[empty] += probability * delta * p_q * (1 - retention)
            rewards['harms'] += probability * harms
            rewards['ordinary_harms'] += probability * harms * (not query)
            rewards['inquiry_harms'] += probability * harms * query
            rewards['action_one_uses'] += probability * action_one
            rewards['turnovers'] += probability * delta
            loss = F(1) if remaining_skill == 0 else F(0) if arm.protected else F(1, 10)
            rewards['archive_erasures'] += probability * delta * package * loss

    final = defaultdict(F)
    for destination, probability in transitions.items():
        if probability:
            if destination[0] == 0:
                destination = (0, 0, 0, 0, 0, 0, -1, 0)
            final[destination] += probability
    assert sum(final.values(), F()) == 1
    assert sum(rewards[name] for name in (
        'ordinary_cases', 'inquiry_cases', 'inquiry_slots', 'training_slots')) == 2
    return final, rewards


def main():
    source = ROOT / 'analyze.py'
    spec = importlib.util.spec_from_file_location('formation_production_for_audit', source)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    states = [
        module.INITIAL,
        (1, 1, 1, 3, 1, 2, -1, 0),
        (1, 0, 1, 0, 0, 0, 1, 1),
        (2, 1, 1, 0, 0, 0, 0, 1),
        (2, 1, 1, 0, 0, 0, 1, 1),
        (2, 0, 1, 0, 0, 0, 2, 1),
        (2, 1, 1, 0, 0, 0, -1, 0),
        (2, 1, 1, 4, 2, 2, -1, 0),
        (2, 1, 1, 4, 0, 4, -1, 0),
        (0, 0, 0, 0, 0, 0, -1, 0),
    ]
    maximum_error = 0.
    reward_errors = defaultdict(float)
    for arm in module.ARMS:
        for state in states:
            expected, rewards = independent(arm, state)
            actual, actual_rewards = module.transition(arm, state)
            actual = dict(actual)
            assert set(expected) == set(actual), (arm.name, state)
            error = max(abs(float(expected[x]) - actual[x]) for x in expected)
            maximum_error = max(maximum_error, error)
            assert error < 2e-14
            for name, value in rewards.items():
                error = abs(float(value) - actual_rewards[module.REWARDS.index(name)])
                reward_errors[name] = max(reward_errors[name], error)
                assert error < 2e-14, (arm.name, state, name, error)
    consequences = []
    for frame in range(4):
        _, rewards = independent(module.ARMS[0], (2, 1, 1, 0, 0, 0, frame, 1))
        consequences.append({'frame': frame,
                             'mean_harm': str(rewards['harms'] / 2),
                             'turnover_probability': str(rewards['turnovers'])})
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    recorded = json.loads((ROOT / 'analysis.json').read_text())
    assert source_hash == recorded['code_sha256']
    report = {
        'scope': 'Independent rational raw-case reconstruction of 60 representative baseline transition rows; not exhaustive path verification.',
        'all_checks_passed': True,
        'checked_rows': len(states) * len(module.ARMS),
        'states_per_arm': states,
        'arms': [arm.name for arm in module.ARMS],
        'maximum_transition_probability_difference': maximum_error,
        'maximum_reward_differences': dict(reward_errors),
        'physical_consequence_witnesses': consequences,
        'production_source_sha256': source_hash,
        'checker_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol_sha256': hashlib.sha256((ROOT / 'PROTOCOL.md').read_bytes()).hexdigest(),
    }
    extension_path = ROOT / 'reopening.py'
    if extension_path.exists():
        ext_spec = importlib.util.spec_from_file_location('reopening_for_audit', extension_path)
        extension = importlib.util.module_from_spec(ext_spec)
        sys.modules[ext_spec.name] = extension
        ext_spec.loader.exec_module(extension)
        extension_states = [
            (2, 1, 1, 1, 0, 1, 0, 1),
            (2, 1, 1, 4, 0, 2, 1, 1),
            (2, 1, 1, 4, 4, 2, 0, 1),
            (2, 0, 1, 2, 1, 1, 2, 1),
            (1, 1, 1, 2, 1, 1, 0, 1),
        ]
        ext_error, ext_reward_error = 0., 0.
        for arm in extension.ARMS:
            for state in extension_states:
                expected, rewards = independent(arm, state, reopening=True)
                actual, actual_rewards = extension.transition(arm, state)
                actual = dict(actual)
                assert set(expected) == set(actual), (arm.name, state)
                error = max(abs(float(expected[x]) - actual[x]) for x in expected)
                assert error < 2e-14
                ext_error = max(ext_error, error)
                for name, value in rewards.items():
                    error = abs(float(value) - actual_rewards[extension.REWARDS.index(name)])
                    assert error < 2e-14, (arm.name, state, name, error)
                    ext_reward_error = max(ext_reward_error, error)
        ext_recorded = json.loads((ROOT / 'reopening-analysis.json').read_text())
        ext_hash = hashlib.sha256(extension_path.read_bytes()).hexdigest()
        assert ext_hash == ext_recorded['extension_code_sha256']
        assert ext_recorded['baseline_code_sha256'] == source_hash
        assert ext_recorded['baseline_result_sha256'] == hashlib.sha256((ROOT / 'analysis.json').read_bytes()).hexdigest()
        report['reopening_checks'] = {
            'scope': 'Ten representative raw-case transition rows and baseline reward fields; analyst change-classification rewards inspected separately.',
            'checked_rows': len(extension_states) * len(extension.ARMS),
            'states_per_arm': extension_states,
            'maximum_transition_probability_difference': ext_error,
            'maximum_baseline_reward_difference': ext_reward_error,
            'extension_source_sha256': ext_hash,
            'extension_protocol_sha256': hashlib.sha256((ROOT / 'REOPENING-PROTOCOL.md').read_bytes()).hexdigest(),
            'baseline_source_and_results_preserved': True,
        }
    destination = ROOT / 'independent-verification.json'
    destination.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
