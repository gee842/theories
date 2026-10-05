"""Compose isolated service kernels without importing the integrated target.

Exact finite predictions for the locally frozen 864-cell queue challenge.
This code was written separately from target.py; all component probabilities
come from calibration.json. The queue chronology is a declared shared input.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
POLICIES = ('serve', 'restart_first', 'inspect_then_repair', 'deadline_aware')
QUEUES = [(d,) for d in range(1, 4)] + list(combinations_with_replacement(range(1, 4), 2))


def policy_action(policy, turn, jobs, cash, first_test):
    action = 'serve'
    if policy == 'restart_first' and turn == 0:
        action = 'restart'
    elif policy in ('inspect_then_repair', 'deadline_aware'):
        if policy != 'deadline_aware' or jobs[0] != 1:
            if turn == 0:
                action = 'inspect'
            elif turn == 1 and first_test is True:
                action = 'restart'
    if cash < {'serve': 0, 'inspect': 1, 'restart': 2}[action]:
        action = 'serve'
    return action


def prediction(case, calibration):
    initial_jobs, prior, initial_cash, finance, enactment, policy = case
    prior = Q(prior)
    # State: jobs, fault, cash, treasury, first test, failed, paid, tests, restarts.
    dist = {}
    for fault, mass in ((False, 1-prior), (True, prior)):
        if mass:
            dist[(initial_jobs, fault, initial_cash, 3-initial_cash,
                  None, False, 0, 0, 0)] = mass
    for turn in range(3):
        nxt = defaultdict(Q)
        for state, mass in dist.items():
            jobs, fault, cash, treasury, first_test, failed, paid, tests, restarts = state
            if failed or not jobs:
                nxt[state] += mass
                continue
            if finance == 'immediate':
                move = min(3-cash, treasury)
                cash += move
                treasury -= move
            action = policy_action(policy, turn, jobs, cash, first_test)
            fee = {'serve': 0, 'inspect': 1, 'restart': 2}[action]
            cash -= fee
            paid += fee
            mode = 'fault' if fault else 'healthy'
            if action == 'serve':
                p = Q(calibration['serve_success'][mode])
                branches = ((p, fault, True, None), (1-p, fault, False, None))
            elif action == 'inspect':
                tests += 1
                p = Q(calibration['diagnostic_positive'][mode])
                branches = ((p, fault, False, True), (1-p, fault, False, False))
            else:
                restarts += 1
                if fault:
                    p = Q(calibration['restart_clears_fault'][enactment])
                    branches = ((p, False, False, None), (1-p, True, False, None))
                else:
                    branches = ((Q(1), False, False, None),)
            for chance, new_fault, completed, signal in branches:
                if not chance:
                    continue
                new_jobs = jobs[1:] if completed else jobs
                new_cash = min(3, cash + int(completed))
                new_treasury = treasury + max(0, cash + int(completed)-3)
                new_jobs = tuple(d-1 for d in new_jobs)
                new_failed = any(d <= 0 for d in new_jobs)
                remembered = signal if turn == 0 and action == 'inspect' else first_test
                next_state = (new_jobs, new_fault, new_cash, new_treasury,
                              remembered, new_failed, paid, tests, restarts)
                nxt[next_state] += mass * chance
        assert sum(nxt.values()) == 1
        dist = nxt
    values = defaultdict(Q)
    for state, mass in dist.items():
        jobs, fault, cash, treasury, signal, failed, paid, tests, restarts = state
        assert failed or not jobs
        for name, value in [('failure', failed), ('completion', not jobs),
                            ('expense', paid), ('tests', tests), ('restarts', restarts),
                            ('terminal_cash', cash), ('terminal_treasury', treasury)]:
            values[name] += mass * value
    assert values['failure'] + values['completion'] == 1
    return {k: str(values[k]) for k in sorted(values)}


def all_predictions(calibration):
    rows = []
    for case in product(QUEUES, ('0', '1/2', '1'), (0, 3),
                        ('barred', 'immediate'), ('restricted', 'enabled'), POLICIES):
        jobs, prior, cash, finance, enactment, policy = case
        rows.append({'case': {'jobs': list(jobs), 'fault_prior': prior,
                             'initial_cash': cash, 'finance': finance,
                             'enactment': enactment, 'policy': policy},
                     'outcomes': prediction(case, calibration)})
    assert len(rows) == 864
    return rows


if __name__ == '__main__':
    calibration_path = HERE / 'calibration.json'
    calibration = json.loads(calibration_path.read_text())
    result = {'kind': 'exact composed predictions before integrated target execution',
              'calibration_sha256': hashlib.sha256(calibration_path.read_bytes()).hexdigest(),
              'cells': all_predictions(calibration)}
    (HERE / 'frozen-predictions.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'prediction_cells': len(result['cells']),
                      'calibration_sha256': result['calibration_sha256']}))
