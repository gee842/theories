"""Independent public-policy evaluator for target.py; no predictor imports.

Run only after root's prediction freeze. True latent branches are integrated
exactly; policy_action receives PublicState and one public memory bit only.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import target

POLICIES = ('serve', 'restart_first', 'inspect_then_repair', 'deadline_aware')
QUEUES = ((1,), (2,), (3,), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3))
METRICS = ('failure', 'completion', 'expense', 'tests', 'restarts',
           'terminal_cash', 'terminal_treasury')


def policy_action(policy, slot, public, first_inspection_positive):
    """Controller cannot access true fault or a hidden restart outcome."""
    if public.failed or not public.jobs:
        raise ValueError('terminal policy call')
    if policy == 'serve':
        requested = 'serve'
    elif policy == 'restart_first':
        requested = 'restart' if slot == 0 else 'serve'
    elif policy in ('inspect_then_repair', 'deadline_aware'):
        if policy == 'deadline_aware' and public.jobs[0] == 1:
            requested = 'serve'
        elif slot == 0:
            requested = 'inspect'
        elif slot == 1 and first_inspection_positive:
            requested = 'restart'
        else:
            requested = 'serve'
    else:
        raise ValueError(policy)
    required_cash = {'serve': 0, 'inspect': 1, 'restart': 2}[requested]
    return requested if public.cash >= required_cash else 'serve'


def public_observation(branch):
    """JSON-ready adapter for the target's event and public state."""
    event = branch.observation.event
    s = branch.observation.state
    return {'event': event,
            'test_positive': (event == 'positive') if event in ('positive','negative') else None,
            'completed': event == 'complete',
            'jobs': list(s.jobs), 'cash': s.cash, 'treasury': s.treasury,
            'finance': s.access, 'enactment': s.enactment,
            'terminal_failure': s.failed,
            'terminal_success': not s.failed and not s.jobs}


def evaluate(case):
    prior = Q(case['fault_prior'])
    active = defaultdict(Q)
    terminal = defaultdict(Q)
    for fault, mass in ((0, 1-prior), (1, prior)):
        if mass:
            state = target.State(tuple(case['jobs']), case['initial_cash'],
                                 3-case['initial_cash'], fault,
                                 case['finance'], case['enactment'])
            active[(state, False)] += mass
    values = {key: Q(0) for key in METRICS}
    income = Q(0)
    branch_count = 0
    for slot in range(3):
        next_active = defaultdict(Q)
        for (raw_state, first_positive), occupancy in active.items():
            state = target.normalize(raw_state)
            if state.terminal:
                terminal[state] += occupancy
                continue
            action = policy_action(case['policy'], slot, state.public(), first_positive)
            for branch in target.step(state, action):
                branch_count += 1
                mass = occupancy*branch.probability
                values['expense'] += mass*branch.expense
                values['tests'] += mass*(action == 'inspect')
                values['restarts'] += mass*(action == 'restart')
                income += mass*branch.income
                observed = public_observation(branch)
                memory = bool(observed['test_positive']) if slot == 0 and action == 'inspect' else first_positive
                if branch.state.terminal:
                    terminal[branch.state] += mass
                else:
                    next_active[(branch.state, memory)] += mass
        active = next_active
    assert not active, 'registered maximum deadline3 must terminate by slot3'
    assert sum(terminal.values()) == 1
    for state, mass in terminal.items():
        values['failure'] += mass*state.failed
        values['completion'] += mass*(not state.failed and not state.jobs)
        values['terminal_cash'] += mass*state.cash
        values['terminal_treasury'] += mass*state.treasury
    assert values['failure']+values['completion'] == 1
    assert values['terminal_cash']+values['terminal_treasury']+values['expense'] == 3+income
    return {'case': case, 'outcomes': {k: str(v) for k,v in values.items()},
            'audit': {'income': str(income), 'branch_count': branch_count,
                      'terminal_probability': '1', 'ledger_residual': '0'}}


def cases():
    for jobs in QUEUES:
        for prior in ('0', '1/2', '1'):
            for cash in (0, 3):
                for finance in ('barred', 'immediate'):
                    for enactment in ('restricted', 'enabled'):
                        for policy in POLICIES:
                            yield {'jobs': list(jobs), 'fault_prior': prior,
                                   'initial_cash': cash, 'finance': finance,
                                   'enactment': enactment, 'policy': policy}


def case_key(case):
    return (tuple(case['jobs']), str(Q(case['fault_prior'])), case['initial_cash'],
            case['finance'], case['enactment'], case['policy'])


def run(prediction_path):
    """Called only after the separate freeze notice; frozen predictions read-only."""
    base = Path(__file__).parent
    if not prediction_path.is_file():
        raise ValueError('frozen prediction file must already exist')
    prediction_bytes = prediction_path.read_bytes()
    predicted = json.loads(prediction_bytes)
    cells = [evaluate(case) for case in cases()]
    assert len(cells) == 864
    pred_map = {case_key(row['case']): row['outcomes'] for row in predicted['cells']}
    assert len(pred_map) == 864
    differences = []
    for row in cells:
        key = case_key(row['case'])
        for metric in METRICS:
            if Q(row['outcomes'][metric]) != Q(pred_map[key][metric]):
                differences.append({'case': row['case'], 'metric': metric,
                                    'target': row['outcomes'][metric],
                                    'prediction': pred_map[key][metric]})
    result = {'status': 'exact_match' if not differences else 'disagreement',
              'cell_count': len(cells), 'coordinate_count': len(cells)*len(METRICS),
              'target_sha256': hashlib.sha256((base/'target.py').read_bytes()).hexdigest(),
              'evaluator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'prediction_sha256': hashlib.sha256(prediction_bytes).hexdigest(),
              'differences': differences, 'cells': cells}
    (base/'target-outcomes.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'cells'}, indent=2))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-after-freeze', action='store_true', required=True)
    parser.add_argument('--predictions', type=Path,
                        default=Path(__file__).with_name('frozen-predictions.json'))
    args = parser.parse_args()
    run(args.predictions)
