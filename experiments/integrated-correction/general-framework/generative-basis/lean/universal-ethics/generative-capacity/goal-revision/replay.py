#!/usr/bin/env python3
"""Ordinary finite interpreter, independently written from the joint-history law.

Compares every retained state, including both complete packet stores, with fresh
Lean evaluation. Same-author operational reconstruction, not independent review
or a general language-refinement proof. All numerical parameters are supplied.
"""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
FORMAL = HERE.parent


def initial(**changes):
    state = dict(context=0, cash=14, fund=200, spent=0, goal=0, rule=0,
                 judgment=0, quote=0, adopts=True, authority=True, approval=True,
                 halted=False, losses=0, performed=0, fulfilled=0,
                 archive=[], acquired=[])
    state.update(changes)
    return state


def impact(context, goal):
    participant = (goal == 2) if context == 0 else (goal == 1)
    return [int(participant), 1, int(goal == 2), int(goal == 1)]


def better(left, right):
    # Extensional claim sets; no scalar weighting or counts of lives.
    left_basic = {i for i in range(2) if left[i]}
    right_basic = {i for i in range(2) if right[i]}
    left_gain = {i for i in range(2, 4) if left[i]}
    right_gain = {i for i in range(2, 4) if right[i]}
    return (right_basic < left_basic or
            (right_basic == left_basic and right_gain < left_gain))


def charge(s, cost, credit=0):
    if s['cash'] < cost or s['fund'] < credit:
        s['halted'] = True
        return False
    s['cash'] += credit - cost
    s['fund'] -= credit
    s['spent'] += cost
    return True


def lookup(s, goal):
    return next((p for p in s['acquired'] if p[0] == goal), None)


def perform(s, goal, delivery):
    tariffs = {0: {1: 3, 2: 1}, 1: {1: 1, 2: 2}}
    credit = tariffs[s['rule']][goal]
    if charge(s, 2, credit):
        effect = impact(s['context'], goal)
        s['archive'].insert(0, [goal, s['context'], *effect,
                               8 if goal == 1 else 3, credit])
        intact = bool(effect[0] and effect[1])
        s['losses'] += int(not intact)
        s['performed'] += int(delivery)
        s['fulfilled'] += int(delivery and intact)


def step(previous, event):
    s = deepcopy(previous)
    if s['halted']:
        return s
    kind, value = event
    if kind == 'probe':
        perform(s, value, False)
    elif kind == 'read' and charge(s, 1):
        s['acquired'] = [] if value == 'missing' else deepcopy(s['archive'])
        if value == 'reversed':
            for packet in s['acquired']:
                packet[2] = 1 - packet[2]
        if value == 'creditInflated':
            for packet in s['acquired']:
                if packet[0] == 2:
                    packet[7] = 2
        s['judgment'] = 0
    elif kind == 'learn' and charge(s, 1):
        scores = {g: (lookup(s, g)[6] if lookup(s, g) else 0) for g in (1, 2)}
        s['goal'] = 1 if scores[1] > scores[2] else (2 if scores[2] > scores[1] else 0)
    elif kind == 'assess' and charge(s, 1):
        old, alternative = lookup(s, 1), lookup(s, 2)
        s['judgment'] = 0
        if (s['adopts'] and old and alternative and
                old[1] == alternative[1] == s['context']):
            if better(alternative[2:6], old[2:6]):
                s['judgment'] = 2
            elif better(old[2:6], alternative[2:6]):
                s['judgment'] = 1
    elif kind == 'enact' and charge(s, 1):
        if value and s['judgment']:
            s['goal'] = s['judgment']
    elif kind == 'quote' and charge(s, 1):
        s['quote'] = 2
    elif kind == 'reform':
        def covers(cash, fund, credit):
            for _ in range(value):
                if cash < 2 or fund < credit:
                    return False
                cash += credit - 2
                fund -= credit
            return True
        receipt = lookup(s, 2)
        authorized = s['authority'] and s['goal'] == s['judgment'] == 2
        if (receipt and authorized and s['rule'] == 0 and
                receipt[1] == s['context'] and s['quote'] == 2 and s['cash'] >= 2):
            needed = not covers(s['cash'], s['fund'], receipt[7])
            payable = covers(s['cash'] - 2, s['fund'], s['quote'])
            if needed and payable and charge(s, 2):
                s['rule'] = 1
    elif kind == 'act':
        old, alternative = lookup(s, 1), lookup(s, 2)
        practice = 0
        if old and alternative:
            if s['goal'] == 1:
                practice = 1 if old[6] > alternative[6] else (2 if alternative[6] > old[6] else 0)
            elif s['goal'] == 2:
                practice = 2 if better(alternative[2:6], old[2:6]) else (1 if better(old[2:6], alternative[2:6]) else 0)
        evidence = lookup(s, practice)
        if evidence and evidence[1] == s['context']:
            perform(s, practice, True)
        else:
            s['halted'] = True
    elif kind == 'shift':
        s.update(context=value, acquired=[], judgment=0, quote=0)
    return s


def preparation(meter='faithful', write=True):
    return [('probe', 1), ('read', 'faithful'), ('learn', None),
            ('probe', 2), ('read', meter), ('assess', None),
            ('enact', write), ('quote', None)]


def history(meter='faithful', write=True, reform=True):
    return preparation(meter, write) + ([('reform', 8)] if reform else []) + [('act', None)] * 8


def menu():
    return [
        ('success', initial(), history()),
        ('unreformed', initial(), history(reform=False)),
        ('write_clamp', initial(), history(write=False, reform=False)),
        ('no_adoption', initial(adopts=False), history()),
        ('approval_reversed', initial(approval=False), history()),
        ('missing', initial(), history(meter='missing')),
        ('restriction', initial(context=1), history()),
        ('misleading', initial(context=1), history(meter='reversed')),
        ('unauthorized', initial(authority=False), history()),
        ('unfunded', initial(fund=5), history()),
        ('credit_inflated', initial(), history(meter='creditInflated')),
        ('short_demand', initial(), preparation() + [('reform', 3)] + [('act', None)] * 3),
        ('context_shift', initial(), preparation() + [('shift', 1), ('assess', None), ('act', None)]),
    ]


def code(s):
    fixed = ['context', 'cash', 'fund', 'spent', 'goal', 'rule', 'judgment',
             'quote', 'adopts', 'authority', 'approval', 'halted', 'losses',
             'performed', 'fulfilled']
    return ([int(s[k]) for k in fixed] + [len(s['archive'])] +
            [x for p in s['archive'] for x in p] + [len(s['acquired'])] +
            [x for p in s['acquired'] for x in p])


def main():
    receipt = json.loads((FORMAL / 'goal-revision-verification.json').read_text())
    assert receipt['status'] == 'passed'
    retained = FORMAL / receipt['retained_run']
    for name, digest in receipt['artifact_sha256'].items():
        assert sha256((retained / name).read_bytes()).hexdigest() == digest, name
    for module, digest in receipt['source_sha256'].items():
        assert sha256((FORMAL / (module + '.lean')).read_bytes()).hexdigest() == digest
    compiled = {}
    for line in (retained / 'GoalRevision.log').read_text().splitlines():
        m = re.fullmatch(r'TRACE (\w+) (\d+) (\[.*\])', line)
        assert m, ('Unexpected compiler output', line)
        key = (m[1], int(m[2]))
        assert key not in compiled
        compiled[key] = json.loads(m[3])
    observed, results = {}, {}
    for name, start, events in menu():
        rows, s = [deepcopy(start)], start
        for event in events:
            next_state = step(s, event)
            assert next_state['losses'] >= s['losses']
            assert sum(next_state[k] for k in ('cash', 'fund', 'spent')) == start['cash'] + start['fund']
            assert min(next_state[k] for k in ('cash', 'fund', 'spent')) >= 0
            s = next_state
            rows.append(s)
        for i, state in enumerate(rows):
            observed[name, i] = code(state)
        results[name] = {'events': events, 'states': rows, 'final': rows[-1]}
    assert observed.keys() == compiled.keys()
    assert observed == compiled, [k for k in observed if observed[k] != compiled[k]]
    report = {
        'status': 'passed', 'cases': len(results), 'complete_state_comparisons': len(observed),
        'source_sha256': receipt['source_sha256'],
        'formal_run': receipt['retained_run'],
        'replay_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Same-author independent finite interpreter; all stored packet and state fields compared at every prefix. No empirical validation, independent agent review or general refinement claimed.',
        'prefix_accounting': 'All finite common-fund transfers and expenditure conserved; past loss never decreases.',
        'results': results,
    }
    (HERE / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'cases', 'complete_state_comparisons')}))
    for name, r in results.items():
        s = r['final']
        print(name, {k: s[k] for k in ('goal', 'rule', 'fulfilled', 'cash', 'losses', 'halted')})


if __name__ == '__main__':
    main()
