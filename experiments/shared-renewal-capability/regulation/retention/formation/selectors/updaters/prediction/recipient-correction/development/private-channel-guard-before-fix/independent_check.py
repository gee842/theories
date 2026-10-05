#!/usr/bin/env python3
"""Independent suffix semantics over saved actual predecessor fixtures.

The calculation below uses no producer functions. main imports the producer
only to compare separately computed local output distributions. Saved fixtures
and aggregate results remain a second, hash-pinned comparison boundary.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
COUNTERS = ('eligible', 'setup_started', 'installed', 'rents', 'senses', 'trials',
            'recipient_trials', 'actor_trials', 'recipient_captures', 'actor_captures',
            'evidence', 'writes', 'missing_evidence', 'decoder_errors', 'unpaid_write',
            'actor_command_changed', 'spent', 'waste')
PACKED = frozenset(('indexed', 'conventional', 'private_only', 'private_as_recipient', 'frozen'))
PAYMENTS_CHECKED = 0


def observe_context(law, recipient):
    if law['identity'] == 'alias':
        return 0
    return int(recipient) if law['identity'] == 'correct' else int(not recipient)


def command(arm, payload, context):
    if arm not in PACKED:
        return payload // 4
    pair = (payload % 2, payload // 2)
    return pair[context]


def update(arm, payload, context, label):
    if arm not in PACKED:
        return 4 * label
    pair = [payload % 2, payload // 2]
    pair[context] = label
    return pair[0] + 2 * pair[1]


def admitted(state):
    return (state['stage'] == 2 and state['life'] > 0 and state['gate_life'] > 0
            and state['coupling_life'] > 0 and state['coupling'] == 0
            and state['written'] and state['q'] in (0, 4))


def evaluate(law, arm, inherited, actor_orientation):
    """Recursive complete suffix, auditing each payment before later receipts."""
    global PAYMENTS_CHECKED
    state = {**inherited, 'recipient': 0, 'active': False, 'installed': False, 'recoded': False}
    totals = dict.fromkeys(COUNTERS, 0)
    totals['eligible'] = int(admitted(inherited))

    def buy(s, c, price, counter=None):
        global PAYMENTS_CHECKED
        if s['fuel'] < price:
            return False
        before = s['fuel'] + s['recipient'] + c['spent'] + c['waste']
        s['fuel'] -= price
        c['spent'] += price
        if counter:
            c[counter] += 1
        assert before == s['fuel'] + s['recipient'] + c['spent'] + c['waste']
        PAYMENTS_CHECKED += 1
        return True

    if admitted(inherited) and buy(state, totals, 2, 'setup_started'):
        recoding = 0 if arm == 'shared_cheap' else 2
        if buy(state, totals, recoding):
            state.update(active=True, installed=True)
            totals['installed'] = 1
            if arm in PACKED:
                state.update(q=3 * (inherited['q'] // 4), recoded=True)

    def walk(step, s0, c0, history):
        if step == 4:
            first, self1, later, self2 = history
            corrected = (first['action'] is not None and first['capture'] is False
                         and first['paid_write'] and first['label'] is not None
                         and first['command_after'] != first['action']
                         and later['action'] is not None and later['capture'] is True
                         and later['action'] != first['action'])
            strict = (corrected and first['receipt_source'] == 'target'
                      and self1['capture'] is True and self2['capture'] is True)
            counts = dict(c0, recipient_correction=int(corrected), strict_witness=int(strict),
                          final_actor=s0['fuel'], final_recipient=s0['recipient'], active_memory=int(s0['active']))
            assert inherited['fuel'] + 4 * law['packet'] == sum(counts[k] for k in
                    ('final_actor', 'final_recipient', 'spent', 'waste'))
            if s0['recoded']:
                assert 0 <= s0['q'] <= 3
            return [(Q(1), s0, counts, history)]
        recipient = step % 2 == 0
        target = 'recipient' if recipient else 'actor'
        s, c = dict(s0), dict(c0)
        event = dict(target=target, report=None, action=None, capture=None, label=None,
                     paid_write=False, command_after=None, receipt_source=None,
                     q_before=s['q'], q_after=s['q'])

        def move_on(next_state, counts, receipt):
            # This also checks every aborted phase, which has no receipt.
            assert s0['fuel'] + s0['recipient'] + law['packet'] == (
                next_state['fuel'] + next_state['recipient'] + counts['spent'] - c0['spent']
                + counts['waste'] - c0['waste'])
            return walk(step + 1, next_state, counts, history + [receipt])

        def idle():
            c['waste'] += law['packet']
            return move_on(s, c, event)

        if not s['active']:
            return idle()
        if not buy(s, c, 1, 'rents'):
            s['active'] = False
            return idle()
        if not buy(s, c, 1, 'senses'):
            return idle()
        context = observe_context(law, recipient)
        event['report'] = context
        if not buy(s, c, 3, 'trials'):
            return idle()
        action = command(arm, s['q'], context)
        event['action'] = action
        s['last'] = action
        c[target + '_trials'] += 1
        useful = actor_orientation ^ int(recipient and law['opposite'])
        chance = Q(law['recipient_availability']) if recipient else Q(1)
        if action != useful:
            chance = Q(0)
        answers = []
        for captured, probability in ((False, 1 - chance), (True, chance)):
            if not probability:
                continue
            result, costs, receipt = dict(s), dict(c), dict(event, capture=captured)
            if captured:
                result['recipient' if recipient else 'fuel'] += law['packet']
                costs[target + '_captures'] += 1
            else:
                costs['waste'] += law['packet']
            if buy(result, costs, 1, 'evidence'):
                missing = recipient and (not law['channel'] or arm == 'private_only')
                label = None
                if missing:
                    costs['missing_evidence'] += 1
                else:
                    private_proxy = recipient and arm == 'private_as_recipient'
                    receipt['receipt_source'] = 'private' if private_proxy else 'target'
                    observed_capture = captured and not private_proxy
                    label = action if observed_capture else 1 - action
                    receipt['label'] = label
                    costs['decoder_errors'] += int(label != useful)
                if buy(result, costs, law['write'], 'writes'):
                    receipt['paid_write'] = True
                    actor_context = observe_context(law, False)
                    old_command = command(arm, result['q'], actor_context)
                    if label is not None and arm != 'frozen':
                        result['q'] = update(arm, result['q'], context, label)
                    if recipient:
                        costs['actor_command_changed'] += int(old_command != command(arm, result['q'], actor_context))
                else:
                    costs['unpaid_write'] += 1
            receipt['q_after'] = result['q']
            receipt['command_after'] = command(arm, result['q'], context)
            for future_mass, final, marks, trace in move_on(result, costs, receipt):
                answers.append((probability * future_mass, final, marks, trace))
        return answers

    result = walk(0, state, totals, [])
    assert sum(p for p, *_ in result) == 1
    return result


def normalized(rows):
    combined = defaultdict(Q)
    for mass, state, metrics, trace in rows:
        combined[json.dumps([state, metrics, trace], sort_keys=True)] += mass
    return dict(combined)


def validate_fixture(fixture):
    original, prefix = fixture['original_law'], fixture['prefix_law']
    assert original['initial_source'] == 121 and original['horizon'] == 12
    assert prefix['horizon'] == 8 and prefix['packet'] == 10
    assert {k: v for k, v in original.items() if k not in ('horizon', 'initial_source')} == {
        k: v for k, v in prefix.items() if k not in ('horizon', 'initial_source')}
    assert sum(Q(p['probability']) for p in fixture['preparations']) == 1
    for prep in fixture['preparations']:
        assert prep['preparation_spent'] + prep['remaining_energy'] == original['initial_common'] + 121
        if not prep['commissioned']:
            continue
        assert prep['packets'] == 12 and prep['remainder'] == 0
        assert prep['reserve'] + 120 + original['adapter'] == prep['remaining_energy']
        for producer, groups in fixture['prefix_records'].items():
            rows = groups[str(prep['reserve'])]
            assert sum(Q(row['probability']) for row in rows) == 1
            for row in rows:
                marks = row['conditional_mean_marks']
                assert row['final_regime'] == 1 - row['initial_regime']
                assert row['state']['fuel'] + Q(marks['spent']) + Q(marks['waste']) == prep['reserve'] + 80


def compare(case, arm, producer, fixture, expected, reference):
    totals, distribution = defaultdict(Q), defaultdict(Q)
    local_count = leaves = 0
    for prep in fixture['preparations']:
        preparation_mass = Q(prep['probability'])
        totals['preparation_spent'] += preparation_mass * prep['preparation_spent']
        if not prep['commissioned']:
            totals['uncommissioned_energy'] += preparation_mass * prep['remaining_energy']
            distribution[json.dumps(dict(kind='preparation_failure', state=prep['state']), sort_keys=True)] += preparation_mass
            continue
        totals['p_commissioned'] += preparation_mass
        totals['adapter_spent'] += preparation_mass * fixture['original_law']['adapter']
        for prior in fixture['prefix_records'][producer][str(prep['reserve'])]:
            weight = preparation_mass * Q(prior['probability'])
            totals['prefix_spent'] += weight * Q(prior['conditional_mean_marks']['spent'])
            totals['prefix_waste'] += weight * Q(prior['conditional_mean_marks']['waste'])
            independent = evaluate(case, arm, prior['state'], prior['final_regime'])
            # Producer access exists only at this comparison boundary.
            assert normalized(independent) == normalized(reference.suffix(case, arm, prior['state'], prior['final_regime']))
            local_count += 1
            leaves += len(independent)
            for mass, state, counts, trace in independent:
                for key, amount in counts.items():
                    totals[key] += weight * mass * amount
                key = json.dumps(dict(kind='suffix', state=state, metrics=counts), sort_keys=True)
                distribution[key] += weight * mass
    for key in COUNTERS + ('recipient_correction', 'strict_witness', 'final_actor', 'final_recipient', 'active_memory'):
        totals.setdefault(key, Q(0))
    assert {k: str(v) for k, v in totals.items()} == expected['metrics']
    expected_distribution = {json.dumps({k: v for k, v in row.items() if k != 'probability'}, sort_keys=True): Q(row['probability'])
                             for row in expected['distribution']}
    assert dict(distribution) == expected_distribution
    assert sum(distribution.values()) == 1
    assert sum(totals[k] for k in ('preparation_spent', 'adapter_spent', 'uncommissioned_energy',
                                 'prefix_spent', 'prefix_waste', 'spent', 'waste', 'final_actor', 'final_recipient')) == case['initial_common'] + 121
    return dict(local_distributions=local_count, terminal_branches=leaves, metrics=len(totals),
                final_distribution_classes=len(distribution))


def targeted_checks(case, fixture):
    predecessors = fixture['prefix_records']['fixed_normal']['26']
    actual = next(row for row in predecessors if admitted(row['state']) and row['state']['fuel'] >= 20)
    initial, orientation = actual['state'], actual['final_regime']
    # Genuine reachable witness; altered-fuel neighbors below are conditional
    # boundary interventions, not claimed as observed prefix histories.
    witness = evaluate(case, 'indexed', initial, orientation)
    assert len(witness) == 1 and witness[0][2]['strict_witness'] == 1
    boundaries = []
    for fuel in (19, 20):
        out = evaluate(case, 'indexed', dict(initial, fuel=fuel), orientation)
        assert len(out) == 1
        _, state, counts, trace = out[0]
        assert counts['strict_witness'] == int(fuel == 20)
        if fuel == 20:
            assert state['fuel'] == 8 and state['recipient'] == 10
        boundaries.append(dict(inherited_fuel=fuel, strict=counts['strict_witness'], actor=state['fuel'], recipient=state['recipient']))
    # Same total actor cost/return can accompany different recipient support.
    good = evaluate(case, 'indexed', dict(initial, fuel=40), orientation)[0]
    missing = evaluate(case, 'private_only', dict(initial, fuel=40), orientation)[0]
    assert good[1]['fuel'] == missing[1]['fuel'] == 28
    assert good[1]['recipient'] == 10 and missing[1]['recipient'] == 0
    assert missing[2]['strict_witness'] == 0 and missing[2]['missing_evidence'] == 2
    # A private zero happens to correct the first failed recipient attempt,
    # then flips a successful recipient record wrongly. It is not a true-receipt witness.
    proxy = evaluate(case, 'private_as_recipient', dict(initial, fuel=40), orientation)[0]
    assert proxy[2]['recipient_correction'] == 1 and proxy[2]['strict_witness'] == 0
    assert proxy[2]['decoder_errors'] == 1
    # Context aliasing fails, whereas a consistent bijective relabeling is harmless.
    alias = evaluate(dict(case, identity='alias'), 'indexed', dict(initial, fuel=40), orientation)[0]
    swap = evaluate(dict(case, identity='swapped'), 'indexed', dict(initial, fuel=40), orientation)[0]
    assert alias[2]['strict_witness'] == 0 and alias[2]['actor_command_changed'] > 0
    for key in ('actor_captures', 'recipient_captures', 'spent', 'final_actor', 'final_recipient', 'strict_witness'):
        assert good[2][key] == swap[2][key]
    # A recipient packet cannot pay acquisition or writing in the actor.
    # Begin with a same-law recipient success and exactly five operative units.
    paid_work_only = evaluate(dict(case, opposite=False), 'indexed', dict(initial, fuel=9), orientation)[0]
    assert paid_work_only[3][0]['capture'] is True
    assert paid_work_only[3][0]['label'] is None and not paid_work_only[3][0]['paid_write']
    assert paid_work_only[1]['recipient'] == 10 and paid_work_only[1]['fuel'] == 0
    assert not paid_work_only[1]['active']
    # Setup payment is sunk if the two-unit recoding cannot be paid.
    partial = evaluate(case, 'indexed', dict(initial, fuel=3), orientation)[0]
    assert partial[2]['setup_started'] == 1 and partial[2]['installed'] == 0
    assert partial[1]['fuel'] == 1 and partial[2]['spent'] == 2 and partial[2]['waste'] == 40
    return dict(actual_witness_predecessor=actual, sharp_route_boundaries=boundaries,
                equal_actor_stock_different_recipient_support='passed',
                private_proxy_is_not_actual_recipient_evidence='passed',
                alias_failure_and_bijective_relabeling='passed',
                recipient_capture_cannot_pay_actor_evidence='passed', partial_setup='passed')


def main():
    fixture_file, result_file = HERE / 'fixtures.json', HERE / 'results.json'
    fixtures = json.loads(fixture_file.read_text())
    results = json.loads(result_file.read_text())
    assert fixtures['source_sha256'] == results['source_sha256']
    hashes = dict(results['source_sha256'])
    for file in (fixture_file, result_file, Path(__file__).resolve()):
        hashes[str(file.relative_to(ROOT))] = hashlib.sha256(file.read_bytes()).hexdigest()
    for name, digest in hashes.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    # Import solely as an oracle being challenged by the independent calculation.
    spec = importlib.util.spec_from_file_location('_recipient_producer_under_test', HERE / 'model.py')
    reference = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = reference
    spec.loader.exec_module(reference)
    for fixture in fixtures['fixtures'].values():
        validate_fixture(fixture)
    audit = {}
    for name, case in results['cases'].items():
        law = case['law']
        audit[name] = {}
        for producer, arms in case['producers'].items():
            audit[name][producer] = {}
            for arm, expected in arms.items():
                audit[name][producer][arm] = compare(law, arm, producer,
                    fixtures['fixtures'][str(law['initial_common'])], expected, reference)
        print(name + ': complete local and aggregate distributions agree', flush=True)
    diagnostics = targeted_checks(results['cases']['primary']['law'], fixtures['fixtures']['30'])
    rows = [row for case in audit.values() for producer in case.values() for row in producer.values()]
    for name, digest in hashes.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    report = dict(status='passed', source_sha256=hashes, case_producer_arms=len(rows),
                  local_distributions=sum(r['local_distributions'] for r in rows),
                  terminal_branches=sum(r['terminal_branches'] for r in rows),
                  metric_comparisons=sum(r['metrics'] for r in rows),
                  successful_payment_ledgers=PAYMENTS_CHECKED, cases=audit, diagnostics=diagnostics,
                  scope='Independent suffix semantics and exact distribution/accounting checks over supplied hash-pinned actual predecessor fixtures; no independent reconstruction of the coupling prefix or chemical identification.')
    (HERE / 'independent-check.json').write_text(json.dumps(report, indent=2) + '\n')
    print({k: report[k] for k in ('status', 'case_producer_arms', 'local_distributions', 'terminal_branches', 'metric_comparisons')})


if __name__ == '__main__':
    main()
