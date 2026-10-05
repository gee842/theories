#!/usr/bin/env python3
"""Independent successor learning AND grandchild copying arithmetic.

The producer is imported only by the comparison driver. Independent operations
below read pinned predecessor fixtures and never call producer/parent policies.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
METRICS = ('admitted', 'trials', 'captures', 'acquisitions', 'writes', 'missing_evidence',
           'decoder_errors', 'transferred', 'spent', 'lost', 'copied', 'grandchild_capture',
           'grandchild_retained', 'recipient_correction', 'strict_witness')
PAYMENT_CHECKS = 0


def admitted(prior):
    child = prior['child']
    return bool(prior['retained'] and prior['copied'] and child is not None
                and child[0] is not None and 0 <= child[1] < 4
                and prior['child_recipient_action_enabled'])


def response(payload):
    return payload // 2


def revise(route, payload, action, captured, channel):
    if route == 'closed' or (not channel and route != 'private_zero'):
        return payload, None, None
    source = 'private' if route == 'private_zero' else 'target'
    receipt = captured if source == 'target' else False
    label = action if receipt else 1 - action
    return (payload if route == 'frozen' else payload % 2 + 2 * label), label, source


def grandchild(donor, recipient, route, payload, parts, target_law, copied_payload):
    """Independent exact copy/read/use/hold tree; no parent transmit call."""
    global PAYMENT_CHECKS
    g = dict(actor=donor, recipient=recipient, child_fuel=0, auxiliary_source=10,
             blank=parts, routing_part=parts, occupied_blank=0, assembled_part=0,
             latch=None, child=None, copied=False, retained=False, action=None,
             capture=None, spent=0, lost=0, stage='start')
    initial = donor + recipient + 10

    def account():
        assert sum(g[k] for k in ('actor', 'recipient', 'child_fuel', 'auxiliary_source', 'spent', 'lost')) == initial
        assert g['blank'] + g['occupied_blank'] == parts
        assert g['routing_part'] + g['assembled_part'] == parts

    def spend(payer, price, floor):
        global PAYMENT_CHECKS
        if g[payer] < floor + price:
            return False
        g[payer] -= price
        g['spent'] += price
        PAYMENT_CHECKS += 1
        account()
        return True

    def end(stage):
        g['stage'] = stage
        account()
        return g

    if not spend('actor', 1, 0):
        return end('blocked_donor_hold')
    if not spend('recipient', 1, 1):
        return end('blocked_own_use')
    if not g['blank'] or not spend('recipient', 1, 1):
        return end('blocked_read')
    g['blank'] -= 1
    g['occupied_blank'] += 1
    g['latch'] = [route, copied_payload]
    account()
    if not g['routing_part'] or not spend('recipient', 1, 1):
        return end('blocked_assembly')
    g['routing_part'] -= 1
    g['assembled_part'] += 1
    account()
    if not spend('recipient', 1, 1):
        return end('blocked_write')
    g['child'] = g['latch']
    g['latch'] = None
    g['copied'] = True
    if g['recipient'] < 6:
        return end('blocked_seed')
    g['recipient'] -= 5
    g['child_fuel'] += 5
    account()
    for stage, bill in (('child_rented', 1), ('target_sensed', 1), ('work_paid', 3)):
        if stage == 'work_paid' and g['child'][0] is None:
            return end('blocked_child_route')
        if not spend('child_fuel', bill, 0):
            return end('blocked_' + stage)
    g['action'] = response(g['child'][1])
    g['capture'] = g['action'] == target_law
    g['auxiliary_source'] = 0
    if g['capture']:
        g['recipient'] += 10
    else:
        g['lost'] += 10
    account()
    if not spend('recipient', 1, 1):
        return end('blocked_child_hold')
    g['retained'] = True
    return end('child_held')


def continuation(law, prior, target_law, control):
    global PAYMENT_CHECKS
    n = law['warmups']
    child = prior['child']
    s = dict(original_actor=prior['actor'], recipient=prior['recipient'],
             learner_fuel=prior['child_fuel'], gamma=None if child is None else child[0],
             q=None if child is None else child[1], active=admitted(prior),
             old_auxiliary_source=prior['auxiliary_source'], new_source=10 * (n + 3),
             grandchild_fuel=0, grandchild_blank=law['grandchild_parts'],
             grandchild_part=law['grandchild_parts'], grandchild_occupied=0,
             grandchild_assembled=0, grandchild=None, grandchild_retained=False,
             old_material={k: prior[k] for k in ('blank', 'routing_part', 'occupied_blank', 'assembled_part', 'latch')},
             grandchild_latch=None, grandchild_stage='not_attempted')
    counts = dict.fromkeys(METRICS, 0)
    counts['admitted'] = int(s['active'])
    initial_q = s['q']
    initial_energy = sum(s[k] for k in ('original_actor', 'recipient', 'learner_fuel', 'old_auxiliary_source', 'new_source'))

    def audit(state, c):
        assert sum(state[k] for k in ('original_actor', 'recipient', 'learner_fuel',
            'old_auxiliary_source', 'new_source', 'grandchild_fuel')) + c['spent'] + c['lost'] == initial_energy
        assert state['original_actor'] == prior['actor']
        assert state['old_auxiliary_source'] == prior['auxiliary_source']
        assert state['old_material'] == {k: prior[k] for k in ('blank', 'routing_part', 'occupied_blank', 'assembled_part', 'latch')}
        assert state['recipient'] >= min(1, prior['recipient'])
        assert state['grandchild_blank'] + state['grandchild_occupied'] == law['grandchild_parts']
        assert state['grandchild_part'] + state['grandchild_assembled'] == law['grandchild_parts']

    def finish(state, c, trace):
        failed = trace[n] if len(trace) > n else None
        later = trace[n + 1] if len(trace) > n + 1 else None
        corrected = (failed is not None and later is not None and failed['capture'] is False
                     and failed['paid_write'] and failed['receipt_source'] == 'target'
                     and failed['action'] != failed['command_after']
                     and later['capture'] is True and later['action'] != failed['action'])
        strict = (corrected and c['copied'] and c['grandchild_capture'] and c['grandchild_retained']
                  and state['grandchild'] is not None
                  and list(state['grandchild']) == [state['gamma'], state['q']])
        c = dict(c, recipient_correction=int(corrected), strict_witness=int(strict),
                 final_actor=state['original_actor'], final_recipient=state['recipient'],
                 final_learner=state['learner_fuel'], final_grandchild=state['grandchild_fuel'],
                 remaining_new_source=state['new_source'], remaining_old_auxiliary=state['old_auxiliary_source'],
                 active_learner=int(state['active']))
        audit(state, c)
        return state, c, trace

    def fund_and_pay(state, c, event, price, name):
        global PAYMENT_CHECKS
        needed = max(0, price - state['learner_fuel'])
        if state['recipient'] - needed < 1:
            return False
        state['recipient'] -= needed
        state['learner_fuel'] += needed
        c['transferred'] += needed
        audit(state, c)
        state['learner_fuel'] -= price
        c['spent'] += price
        event['bills'].append([name, price, needed])
        PAYMENT_CHECKS += 1
        audit(state, c)
        return True

    def copy_after_probes(state, c, history):
        state, c = dict(state), dict(c)
        needed = max(0, 1 - state['learner_fuel'])
        if state['active'] and state['recipient'] >= 1 + needed:
            state['recipient'] -= needed
            state['learner_fuel'] += needed
            c['transferred'] += needed
            audit(state, c)
            world = target_law ^ int(law['reverse']) ^ int(law['reverse_grandchild'])
            g = grandchild(state['learner_fuel'], state['recipient'], state['gamma'], state['q'],
                           law['grandchild_parts'], world, initial_q if control == 'copy_old' else state['q'])
            state.update(recipient=g['recipient'], learner_fuel=g['actor'], grandchild_fuel=g['child_fuel'],
                         new_source=g['auxiliary_source'], grandchild_blank=g['blank'],
                         grandchild_occupied=g['occupied_blank'], grandchild_part=g['routing_part'],
                         grandchild_assembled=g['assembled_part'], grandchild=g['child'], grandchild_retained=g['retained'],
                         grandchild_latch=g['latch'], grandchild_stage=g['stage'])
            c['spent'] += g['spent']
            c['lost'] += g['lost']
            c.update(copied=int(g['copied']), grandchild_capture=int(g['capture'] is True),
                     grandchild_retained=int(g['retained']))
            history = history + [dict(grandchild_stage=g['stage'], grandchild_action=g['action'],
                                      grandchild_capture=g['capture'], grandchild_copy=g['child'])]
        elif state['active']:
            state['grandchild_stage'] = 'blocked_donor_funding'
        return [(Q(1), *finish(state, c, history))]

    def probes(index, state0, counters0, history):
        if index == n + 2:
            return copy_after_probes(state0, counters0, history)
        state, c = dict(state0), dict(counters0)
        ev = dict(index=index, action=None, capture=None, label=None, receipt_source=None,
                  paid_write=False, q_before=state['q'], q_after=state['q'], command_after=None,
                  bills=[], status='start')

        def abort(reason):
            state['new_source'] -= 10
            c['lost'] += 10
            ev['status'] = reason
            audit(state, c)
            return probes(index + 1, state, c, history + [ev])

        if not state['active']:
            return abort('inaccessible')
        if not fund_and_pay(state, c, ev, 1, 'rent'):
            state['active'] = False
            return abort('unpaid_rent')
        if not fund_and_pay(state, c, ev, 1, 'sense'):
            return abort('unpaid_sense')
        if not fund_and_pay(state, c, ev, 3, 'work'):
            return abort('unpaid_work')
        action = response(state['q'])
        ev['action'] = action
        c['trials'] += 1
        world = target_law ^ int(law['reverse'] and index >= n)
        probability = Q(law['availability']) if action == world else Q(0)
        result = []
        for captured, weight in ((True, probability), (False, 1 - probability)):
            if not weight:
                continue
            out, marks = dict(state), dict(c)
            event = dict(ev, capture=captured, bills=list(ev['bills']))
            out['new_source'] -= 10
            if captured:
                out['recipient'] += 10
                marks['captures'] += 1
            else:
                marks['lost'] += 10
            audit(out, marks)
            if fund_and_pay(out, marks, event, 1, 'acquire'):
                marks['acquisitions'] += 1
                revised, label, source = revise(out['gamma'], out['q'], action, captured, law['channel'])
                event.update(label=label, receipt_source=source)
                marks['missing_evidence'] += int(label is None)
                marks['decoder_errors'] += int(label is not None and label != world)
                if fund_and_pay(out, marks, event, 1, 'write'):
                    marks['writes'] += 1
                    event['paid_write'] = True
                    out['q'] = initial_q if control == 'clamp_learning' else revised
                    event['status'] = 'written'
                else:
                    event['status'] = 'unpaid_write'
            else:
                event['status'] = 'unpaid_acquire'
            event.update(q_after=out['q'], command_after=response(out['q']))
            assert out['q'] % 2 == initial_q % 2
            for mass, terminal, metrics, trace in probes(index + 1, out, marks, history + [event]):
                result.append((weight * mass, terminal, metrics, trace))
        return result

    audit(s, counts)
    if not s['active']:
        return [(Q(1), *finish(s, counts, []))]
    result = probes(0, s, counts, [])
    assert sum(p for p, *_ in result) == 1
    return result


def normalize(paths):
    mass = defaultdict(Q)
    for p, state, counts, trace in paths:
        mass[json.dumps([state, counts, trace], sort_keys=True)] += p
    return dict(mass)


def compare(law, control, entries, expected, producer):
    totals, distribution = defaultdict(Q), defaultdict(Q)
    local = branches = 0
    for entry in entries:
        mass = Q(entry['mass'])
        if entry['kind'] == 'preparation_failure':
            totals['uncommissioned_energy'] += mass * (entry['preparation']['remaining_energy'] + 10 + 10 * (law['warmups'] + 3))
            totals['earlier_costs'] += mass * entry['preparation']['preparation_spent']
            key = json.dumps(dict(kind='preparation_failure', state=entry['preparation']['state'],
                            unused_extended_source=10 + 10 * (law['warmups'] + 3)), sort_keys=True)
            distribution[key] += mass
            continue
        prior = entry['transmission']['state']
        totals['earlier_costs'] += mass * (Q(entry['earlier_costs']) + prior['spent'] + prior['lost'])
        actual = continuation(law, prior, entry['target_law'], control)
        reference = producer.continuation(law, prior, entry['target_law'], control)
        assert normalize(actual) == normalize(reference), (law, control, prior)
        local += 1
        branches += len(actual)
        for probability, state, counts, trace in actual:
            for key, value in counts.items():
                totals[key] += mass * probability * value
            key = json.dumps(dict(kind='continuation', state=state, metrics=counts), sort_keys=True)
            distribution[key] += mass * probability
    for name in METRICS + ('final_actor', 'final_recipient', 'final_learner', 'final_grandchild',
                           'remaining_new_source', 'remaining_old_auxiliary', 'active_learner'):
        totals.setdefault(name, Q(0))
    assert {k: str(v) for k, v in totals.items()} == expected['metrics']
    wanted = {json.dumps({k: v for k, v in row.items() if k != 'probability'}, sort_keys=True): Q(row['probability'])
              for row in expected['distribution']}
    assert dict(distribution) == wanted
    assert sum(distribution.values()) == 1
    assert sum(totals[k] for k in ('uncommissioned_energy', 'earlier_costs', 'spent', 'lost',
               'final_actor', 'final_recipient', 'final_learner', 'final_grandchild',
               'remaining_new_source', 'remaining_old_auxiliary')) == 161 + 10 * (law['warmups'] + 3)
    return dict(local_distributions=local, terminal_branches=branches, metrics=len(totals),
                final_classes=len(distribution))


def validate_inputs(inputs):
    inspected = 0
    for parent_case in inputs.values():
        for entries in parent_case.values():
            assert sum(Q(e['mass']) for e in entries) == 1
            for e in entries:
                prep = e['preparation']
                assert prep['preparation_spent'] + prep['remaining_energy'] == 151
                if e['kind'] == 'preparation_failure':
                    continue
                ts = e['transmission']['state']
                assert Q(e['earlier_costs']) + sum(ts[k] for k in ('actor', 'recipient', 'child_fuel',
                        'auxiliary_source', 'spent', 'lost')) == 161
                for event in e['transmission']['trace']:
                    assert sum(event[k] for k in ('actor', 'recipient', 'child_fuel', 'auxiliary_source',
                                                 'spent', 'lost')) == e['transmission']['initial_total']
                    assert event['blank'] + event['occupied_blank'] == 1
                    assert event['routing_part'] + event['assembled_part'] == 1
                assert ts['original_source'] == 0
                inspected += 1
    return inspected


def main():
    files = {name: HERE / name for name in ('inputs.json', 'results.json')}
    inputs, results = (json.loads(files[name].read_text()) for name in ('inputs.json', 'results.json'))
    assert inputs['source_sha256'] == results['source_sha256']
    hashes = dict(inputs['source_sha256'])
    for p in (*files.values(), Path(__file__).resolve()):
        hashes[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    for path, expected in hashes.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path
    spec = importlib.util.spec_from_file_location('_successor_under_test', HERE / 'model.py')
    producer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = producer
    spec.loader.exec_module(producer)
    fixture_count = validate_inputs(inputs['inputs'])
    checks = {}
    for name, saved in results['cases'].items():
        law = saved['law']
        checks[name] = {}
        for origin, controls in saved['producers'].items():
            checks[name][origin] = {}
            for control, expected in controls.items():
                checks[name][origin][control] = compare(law, control,
                    inputs['inputs'][law['parent_case']][origin], expected, producer)
        print(name + ': independent local and full distributions match', flush=True)
    for path, expected in hashes.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path
    rows = [a for c in checks.values() for p in c.values() for a in p.values()]
    report = dict(status='passed', source_sha256=hashes, inherited_transmission_branches=fixture_count,
                  case_producer_controls=len(rows), local_distributions=sum(r['local_distributions'] for r in rows),
                  terminal_branches=sum(r['terminal_branches'] for r in rows),
                  metric_comparisons=sum(r['metrics'] for r in rows), payment_checks=PAYMENT_CHECKS,
                  cases=checks, scope='Independent exact learner and grandchild arithmetic over pinned complete inherited fixtures; no independent reconstruction of all ancestor stochastic laws or physical identification.')
    (HERE / 'independent-check.json').write_text(json.dumps(report, indent=2) + '\n')
    print({k: report[k] for k in ('status', 'case_producer_controls', 'local_distributions', 'terminal_branches', 'metric_comparisons')})


if __name__ == '__main__':
    main()
