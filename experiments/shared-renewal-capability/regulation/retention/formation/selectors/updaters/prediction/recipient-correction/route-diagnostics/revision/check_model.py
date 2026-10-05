#!/usr/bin/env python3
"""Independent paid route-revision suffix interpreter.

Written from PROTOCOL.md and the agreed data contract before inspection of the
new producer. No producer imports. Actual first-monitor prefixes are inputs;
this does not reconstruct the entire accepted ancestor/monitor experiment.
"""

from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROUTES = ('target', 'closed', 'private_zero', 'frozen')


def diagnose(success, failure, binding):
    if not binding:
        return 'unresolved'
    signatures = {'target': (1, 2), 'private_zero': (2, 2), 'nonwriter': (1, 1)}
    possible = [name for name, (a, b) in signatures.items()
                if success in (0, a) and failure in (0, b)]
    return possible[0] if len(possible) == 1 else 'unresolved' if possible else 'conflict'


def update(route, code, action, receipt, channel):
    """Conventional table, not imported route functions or analyst labels."""
    if route in ('closed', 'frozen') or (not channel and route != 'private_zero'):
        return code
    signal = False if route == 'private_zero' else receipt
    prediction = action if signal else 1 - action
    return code % 2 + 2 * prediction


def recipient_class(route):
    # Equivalence concerns this recipient record-update interface, not complete
    # physical identity or every possible observation of the two mechanisms.
    return 'nonwriter' if route in ('closed', 'frozen') else route


def run(prefix, case, proposal, world):
    """Return independent suffix state and payment snapshots.

    Phase labels/output adapters follow DATA-CONTRACT.md; the arithmetic
    is intentionally independent of the new producer and old copier code.
    """
    s = deepcopy(prefix['state'])
    s.update(held_fuel=case['grant'], probe_reserve=case['probe_source'],
             copy_source=case['copy_source'], free_revision_heads=case['heads'],
             installed_revision_heads=0, replacement_parts=case['parts'], retired_parts=0,
             installed_route_parts=prefix.get('material', {}).get('current_routing_part', int(bool(s['carrier_active']))), revision_armed=False,
             phase='prefix', probe_index=0, successor_cash=0,
             successor_blank=case['receiver_blank'], successor_occupied=0,
             successor_part=case['receiver_part'], successor_assembled=0,
             successor_latch=None, successor_template=None, successor_retained=False,
             successor_capture=None)
    trace = []
    counters = dict(head_assemblies=0, diagnostic_reads=0, swaps=0, configuration_changes=0, behavior_changes=0,
                    probe_work=0, probe_captures=0, completed_probes=0, copied=0, requests=0, prefix_complete=0, grant_released=0,
                    successor_capture=0, successor_retained=0)
    initial = deepcopy(s)
    total = sum(s[k] for k in ('untouched_energy', 'recipient', 'child_cash', 'new_source',
                              'spent', 'lost', 'held_fuel', 'probe_reserve', 'copy_source', 'successor_cash'))
    actor_bit = None if s['q'] is None else s['q'] % 2

    def record(phase):
        s['stage'] = phase
        assert sum(s[k] for k in ('untouched_energy', 'recipient', 'child_cash', 'new_source',
                                  'spent', 'lost', 'held_fuel', 'probe_reserve', 'copy_source', 'successor_cash')) == total
        assert s['recipient'] >= min(initial['recipient'], 1)
        assert all(s[k] >= 0 for k in ('recipient', 'child_cash', 'new_source', 'spent', 'lost',
                                       'held_fuel', 'probe_reserve', 'copy_source', 'successor_cash'))
        assert s['free_revision_heads'] + s['installed_revision_heads'] == case['heads']
        assert s['replacement_parts'] + s['retired_parts'] == case['parts']
        assert s['successor_blank'] + s['successor_occupied'] == case['receiver_blank']
        assert s['successor_part'] + s['successor_assembled'] == case['receiver_part']
        assert s['q'] is None or (0 <= s['q'] < 4 and s['q'] % 2 == actor_bit)
        trace.append(deepcopy(s))

    def finish(phase):
        record(phase)
        metrics = dict(
            prefix_complete=counters['prefix_complete'], grants_released=counters['grant_released'],
            head_assemblies=counters['head_assemblies'], reads=counters['diagnostic_reads'],
            swap_requests=counters['requests'], swaps=counters['swaps'],
            route_changes=counters['configuration_changes'],
            recipient_updater_changes=counters['behavior_changes'], probes_completed=counters['completed_probes'],
            probe_work=counters['probe_work'], probe_captures=counters['probe_captures'],
            copies=counters['copied'], child_captures=counters['successor_capture'],
            child_retained=counters['successor_retained'],
            revised_productive_successor=int(bool(counters['configuration_changes'] and
                s['successor_capture'] and s['successor_retained'])),
            behaviorally_revised_productive_successor=int(bool(counters['behavior_changes'] and
                s['successor_capture'] and s['successor_retained'])),
            new_spent=s['spent']-initial['spent'], new_lost=s['lost']-initial['lost'],
            total_spent=s['spent'], total_lost=s['lost'], final_recipient=s['recipient'],
            final_donor=s['child_cash'], final_successor=s['successor_cash'],
            source_remaining=s['new_source']+s['probe_reserve']+s['copy_source'], held_fuel=s['held_fuel'])
        return {'state': s, 'trace': trace, 'metrics': metrics}

    def pay(fee):
        missing = max(0, fee-s['child_cash'])
        if s['recipient'] < 1+missing:
            return False
        s['recipient'] -= missing
        s['child_cash'] += missing
        s['transferred'] += missing
        s['child_cash'] -= fee
        s['spent'] += fee
        return True

    def recipient_pay(fee):
        if s['recipient'] < 1+fee:
            return False
        s['recipient'] -= fee
        s['spent'] += fee
        return True

    def stopped(label):
        return case.get('stop_before') == label

    record('revision_initial')
    if prefix['state']['stage'] not in ('episode_complete', 'commit') or not s['carrier_active']:
        return finish('incomplete_prefix')
    if s['monitor_installed'] and not s['binding']:
        return finish('invalid_prefix_binding')
    counters['prefix_complete'] = 1
    counters['grant_released'] = s['held_fuel']
    s['recipient'] += s['held_fuel']; s['held_fuel'] = 0
    s['new_source'] += s['probe_reserve']; s['probe_reserve'] = 0
    s['phase'] = 'ready'
    record('handoff')

    if case['mode'] != 'no_repair' and s['monitor_installed']:
        if stopped('head'):
            return finish('stopped_head_assembly')
        if s['free_revision_heads'] < 1:
            return finish('missing_revision_head')
        if not pay(1):
            return finish('blocked_head_assembly')
        s['free_revision_heads'] -= 1; s['installed_revision_heads'] += 1
        counters['head_assemblies'] += 1
        record('head_assembled')
        if stopped('read'):
            return finish('stopped_diagnostic_read')
        if not pay(1):
            return finish('blocked_diagnostic_read')
        value = diagnose(s['success_summary'], s['failure_summary'], s['binding'])
        s['revision_armed'] = value in ('nonwriter', 'private_zero')
        counters['diagnostic_reads'] += 1
        counters['requests'] += int(s['revision_armed'])
        record('diagnosis_read')
        if case.get('break_after_read'):
            s.update(revision_armed=False, binding=False, success_summary=0,
                     failure_summary=0, diagnosis='unresolved')
            return finish('binding_broken')
        if s['revision_armed']:
            if stopped('swap'):
                return finish('stopped_swap')
            if s['replacement_parts'] < 1:
                return finish('missing_replacement_part')
            if not pay(1):
                return finish('blocked_swap')
            next_route = s['gamma'] if case['mode'] == 'same_route' else proposal
            assert next_route in ROUTES
            counters['configuration_changes'] += int(next_route != s['gamma'])
            counters['behavior_changes'] += int(recipient_class(next_route) != recipient_class(s['gamma']))
            s['gamma'] = next_route
            s['replacement_parts'] -= 1; s['retired_parts'] += 1
            s.update(revision_armed=False, binding=False, success_summary=0,
                     failure_summary=0, diagnosis='unresolved')
            counters['swaps'] += 1
            record('route_swapped')

    for i in range(case['probes']):
        action = None; receipt = False; candidate = None
        for stage, fee in (('rent', 1), ('sense', 1), ('work', 3), ('acquire', 1), ('write', 1)):
            label = f'probe_{i}_{stage}'
            if stopped(label):
                return finish('stopped_' + label)
            if stage == 'work' and s['new_source'] < 10:
                return finish('blocked_probe_packet')
            if not pay(fee):
                if stage == 'rent': s['carrier_active'] = False
                return finish('blocked_' + label)
            if stage == 'rent':
                s.update(target_report=None, issued=None, candidate=None, route_receipt=False)
            elif stage == 'sense':
                s['target_report'] = 1
            elif stage == 'work':
                action = s['q'] // 2
                current_world = world ^ int(bool(case['reverse_third']) and i >= 2)
                receipt = bool(case['availability'][i]) and action == current_world
                s['issued'] = action
                s['route_receipt'] = receipt
                s['new_source'] -= 10
                s['recipient' if receipt else 'lost'] += 10
                counters['probe_work'] += 1
                counters['probe_captures'] += int(receipt)
            elif stage == 'acquire':
                candidate = update(s['gamma'], s['q'], s['issued'], s['route_receipt'], case['channel'])
                s['candidate'] = candidate
            elif stage == 'write':
                s['q'] = candidate
                counters['completed_probes'] += 1
            s['phase'] = {'rent': 'rented', 'sense': 'sensed', 'work': 'worked',
                          'acquire': 'observed', 'write': 'ready'}[stage]
            if stage == 'write': s['probe_index'] += 1
            record(label)

    # Exact existing donor-funding bridge and copying fees, reimplemented.
    missing = max(0, 1-s['child_cash'])
    if s['recipient'] < 1+missing:
        return finish('blocked_donor_funding')
    s['recipient'] -= missing; s['child_cash'] += missing; s['transferred'] += missing
    s['phase'] = 'copy'
    record('copy_funded')
    s['child_cash'] -= 1; s['spent'] += 1
    record('copy_donor_held')
    if not recipient_pay(1):
        return finish('blocked_own_use')
    record('copy_recipient_operated')
    if s['successor_blank'] < 1 or not recipient_pay(1):
        return finish('blocked_read')
    s['successor_blank'] -= 1; s['successor_occupied'] += 1
    s['successor_latch'] = [s['gamma'], s['q']]
    record('copy_template_read')
    if s['successor_part'] < 1 or not recipient_pay(1):
        return finish('blocked_assembly')
    s['successor_part'] -= 1; s['successor_assembled'] += 1
    record('copy_receiver_assembled')
    if not recipient_pay(1):
        return finish('blocked_write')
    s['successor_template'] = s['successor_latch']; s['successor_latch'] = None
    counters['copied'] = 1
    record('copy_template_written')
    if s['recipient'] < 6:
        return finish('blocked_seed')
    s['recipient'] -= 5; s['successor_cash'] += 5
    record('copy_child_seeded')
    for stage, fee in (('child_rented', 1), ('target_sensed', 1), ('work_paid', 3)):
        if stage == 'work_paid' and s['copy_source'] < 10:
            return finish('blocked_copy_packet')
        if s['successor_cash'] < fee:
            return finish('blocked_' + stage)
        s['successor_cash'] -= fee; s['spent'] += fee
        record('copy_' + stage)
    child_world = world ^ int(bool(case['reverse_third']) and case['probes'] >= 3) ^ int(bool(case['reverse_child']))
    capture = s['successor_template'][1] // 2 == child_world
    s['copy_source'] -= 10
    s['recipient' if capture else 'lost'] += 10
    s['successor_capture'] = capture
    counters['successor_capture'] = int(capture)
    record('copy_child_acted')
    if not recipient_pay(1):
        return finish('blocked_child_hold')
    s['successor_retained'] = True; counters['successor_retained'] = 1
    record('copy_child_held')
    return finish('revision_complete')


def interface_tests():
    """Constructive interface fixtures, not probability-weighted ancestor claims."""
    prefix = {'metrics': {'admitted': 1}, 'state': {
        'recipient': 11, 'child_cash': 0, 'new_source': 10, 'spent': 14,
        'lost': 10, 'transferred': 14, 'untouched_energy': 8, 'q': 0,
        'gamma': 'frozen', 'carrier_active': True, 'stage': 'episode_complete',
        'monitor_installed': True, 'binding': True, 'success_summary': 0,
        'failure_summary': 1, 'diagnosis': 'nonwriter'}}
    case = dict(grant=5, probe_source=20, copy_source=10, heads=1, parts=1,
                receiver_blank=1, receiver_part=1, mode='revise', probes=3,
                availability=[True]*3, channel=True, reverse_third=False,
                reverse_child=False, break_after_read=False, stop_before=None)
    tested = 0
    for bit in (0, 1):
        local = deepcopy(prefix); local['state']['q'] = bit
        for recipe in ROUTES:
            result = run(local, case, recipe, 1)['state']
            assert result['q'] % 2 == bit
            if recipe == 'target':
                assert result['recipient'] == 11 and result['successor_retained']
                assert result['successor_capture'] is True and result['successor_template'] == [recipe, bit+2]
            else:
                assert result['recipient'] == 1 and not result['successor_retained']
                assert result['successor_template'] is None
            tested += 1
    for recipe in ('target', 'private_zero'):
        result = run(prefix, dict(case, reverse_third=True), recipe, 1)['state']
        assert result['recipient'] == 1
        assert result['successor_retained'] == (recipe == 'private_zero')
        if recipe == 'private_zero': assert result['successor_capture'] is False
        tested += 1
    result = run(prefix, dict(case, probes=0), 'target', 1)['state']
    assert result['successor_retained'] and result['successor_capture'] is False and result['recipient'] == 2
    tested += 1
    for recipe in ('target', 'private_zero'):
        result = run(prefix, dict(case, probes=2), recipe, 1)['state']
        assert result['successor_template'] is not None and not result['successor_retained']
        assert result['recipient'] == 4 and result['successor_cash'] == 0
        tested += 1
    signatures = {recipe: tuple(update(recipe, q, q//2, received, channel)
        for q in range(4) for received in (False,True) for channel in (False,True)) for recipe in ROUTES}
    for a in ROUTES:
        for b in ROUTES:
            assert (signatures[a] == signatures[b]) == (recipient_class(a) == recipient_class(b))
            tested += 1
    return tested


def sha_bytes(value):
    return hashlib.sha256(value).hexdigest()


def expand_trace(value):
    if isinstance(value, list):
        return value
    state = deepcopy(value['initial'])
    result = [deepcopy(state)]
    for delta in value['deltas']:
        state.update(delta)
        result.append(deepcopy(state))
    return result


def physical_projection(state):
    # Stage is an observer label. Phase, completed-write index, armed permission,
    # every stored bit, all accounts and all physical stocks remain compared.
    return {k: v for k, v in state.items() if k != 'stage'}


def physical_trace(trace):
    result = []
    for state in expand_trace(trace):
        projected = physical_projection(state)
        if not result or result[-1] != projected:
            result.append(projected)
    return result


def compare_run(actual, expected, name):
    if physical_projection(actual['state']) != physical_projection(expected['state']):
        keys = sorted(set(actual['state']) | set(expected['state']))
        different = {k: (actual['state'].get(k), expected['state'].get(k))
                     for k in keys if k != 'stage' and actual['state'].get(k) != expected['state'].get(k)}
        raise AssertionError(('state', name, different))
    got, want = physical_trace(actual['trace']), physical_trace(expected['trace'])
    if got != want:
        for i, (a, b) in enumerate(zip(got, want)):
            if a != b:
                different = {k: (a.get(k), b.get(k)) for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)}
                raise AssertionError(('trace', name, i, different, len(got), len(want)))
        raise AssertionError(('trace-length', name, len(got), len(want)))
    return len(want)


def main():
    from collections import defaultdict
    from datetime import datetime, timezone
    import gzip
    import importlib.util
    import sys
    sys.dont_write_bytecode = True
    here = Path(__file__).resolve().parent
    repo = next(p for p in here.parents if (p/'AGENTS.md').exists())
    monitor = here.parent/'monitor'
    frozen = {}

    def read(path):
        path = path.resolve()
        assert path.is_relative_to(repo), path
        if path not in frozen:
            frozen[path] = path.read_bytes()
        return frozen[path]

    def manifest(values):
        for relative, expected in values.items():
            assert sha_bytes(read(repo/relative)) == expected, ('source hash', relative)

    inputs = json.loads(read(here/'inputs.json'))
    results = json.loads(gzip.decompress(read(here/'results.json.gz')))
    handoff = json.loads(read(monitor/'handoff/boundary.json'))
    accepted_handoff = json.loads(read(monitor/'handoff/independent-verification.json'))
    assert handoff['status'] == accepted_handoff['status'] == 'passed'
    manifest(inputs['source_sha256']); manifest(results['source_sha256'])
    manifest(handoff['source_sha256'])
    if 'source_sha256' in accepted_handoff: manifest(accepted_handoff['source_sha256'])
    assert results['inputs_sha256'] == sha_bytes(read(here/'inputs.json'))
    assert inputs['entries'] == handoff['entries']
    assert inputs['mixtures'] == handoff['mixtures']
    assert results['cases'] == inputs['cases']
    read(Path(__file__))
    independent_monitor = monitor/'independent_check.py'
    read(independent_monitor)
    spec = importlib.util.spec_from_file_location('_independent_monitor_reference', independent_monitor)
    prior = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prior)

    prefix_counts = defaultdict(int)
    for key, value in inputs['prefixes'].items():
        entry = inputs['entries'][value['entry']]['entry']
        physical = value['result']
        material = physical['material']
        expected_part = entry['parent_state']['grandchild_assembled'] if entry['parent_kind'] == 'continuation' else 0
        assert material == {'current_routing_part': expected_part,
                            'old_stocks_reference': 'entries/'+value['entry']+'/entry/parent_state'}, key
        if entry['base_law'] is not None:
            assert value['world'] == entry['base_law'] ^ int(value['case']['reverse']), key
        source = value['source']
        if source['kind'] == 'exact_export':
            old = handoff['boundaries'][source['boundary']]
            assert old['entry'] == value['entry'], key
            assert physical['state'] == old['analyst_state'], key
            assert physical['metrics'] == old['analyst_metrics'], key
            assert physical['trace'] == old['trace'], key
        else:
            assert source['kind'] == 'existing_monitor_reconstruction', source
            expected = prior.reference(entry, value['case'])
            assert physical['state'] == expected['state'], ('monitor state', key)
            assert physical['metrics'] == expected['metrics'], ('monitor metrics', key)
            assert physical_trace(physical['trace']) == physical_trace(expected['trace']), ('monitor trace', key)
        prefix_counts[source['kind']] += 1

    counts = dict(interface_tests=interface_tests(), suffix_invocations=0, physical_states=0,
                  metric_checks=0, mixture_checks=0, local_checks=0, mass_references=0)
    checked, used = {}, set()

    def check_call(prefix_id, case_id, proposal, execution_id):
        key = (prefix_id, case_id, proposal)
        actual = results['executions'][execution_id]
        used.add(execution_id)
        if key not in checked:
            prefix = inputs['prefixes'][prefix_id]
            wanted = run(prefix['result'], inputs['cases'][case_id]['suffix'], proposal, prefix['world'])
            counts['physical_states'] += compare_run(actual, wanted, key)
            assert actual['metrics'] == wanted['metrics'], ('suffix metrics', key, actual['metrics'], wanted['metrics'])
            counts['metric_checks'] += len(wanted['metrics'])
            counts['suffix_invocations'] += 1
            checked[key] = dict(state=wanted['state'], metrics=wanted['metrics'], execution=execution_id)
        else:
            assert checked[key]['execution'] == execution_id, ('inconsistent invocation', key)
        return checked[key]

    full_cases = {name for name, case in inputs['cases'].items() if case['full']}
    expected_names = {case+'/'+group for case in full_cases for group in inputs['mixtures']}
    assert set(results['mixtures']) == expected_names
    for name, mixture in results['mixtures'].items():
        case_id, group, producer = mixture['case'], mixture['group'], mixture['producer']
        assert name == '/'.join((case_id, group, producer)), name
        baseline = inputs['mixtures'][group+'/'+producer]
        intervention = inputs['cases'][case_id]['prefix']
        expected_refs = []
        for ancestor in baseline['boundary_refs']:
            old = handoff['boundaries'][ancestor['boundary']]
            prefix_id = '/'.join((group, intervention, old['entry']))
            for proposal in ROUTES:
                expected_refs.append((prefix_id, proposal, ancestor['upstream_row'], Fraction(ancestor['mass'])/4))
        got_refs = [(ref['prefix'], ref['proposal'], ref['upstream_row'], Fraction(ref['mass']))
                    for ref in mixture['references']]
        assert got_refs == expected_refs, ('ancestor/proposal references', name)
        assert sum(item[3] for item in got_refs) == 1, ('total mass', name)
        aggregate = defaultdict(Fraction)
        stages = defaultdict(Fraction)
        remaining = Fraction(0)
        for ref in mixture['references']:
            mass = Fraction(ref['mass'])
            wanted = check_call(ref['prefix'], case_id, ref['proposal'], ref['execution'])
            counts['mass_references'] += 1
            for metric, value in wanted['metrics'].items(): aggregate[metric] += mass*value
            actual = results['executions'][ref['execution']]
            stages[actual['state']['stage']] += mass
            state = wanted['state']
            remaining += mass*sum(state[k] for k in ('untouched_energy','recipient','child_cash','new_source',
                'held_fuel','probe_reserve','copy_source','successor_cash'))
        assert {k: Fraction(v) for k,v in mixture['metrics'].items()} == dict(aggregate), ('mixture metrics', name)
        assert {k: Fraction(v) for k,v in mixture['stages'].items()} == dict(stages), ('stage aggregation', name)
        energy = mixture['energy']
        new = inputs['cases'][case_id]['suffix']
        initial = Fraction(baseline['energy']['initial'])+new['grant']+new['probe_source']+new['copy_source']
        prior_cost = Fraction(baseline['energy']['prior_consumed'])
        assert Fraction(energy['initial']) == initial, ('initial energy', name)
        assert Fraction(energy['prior_consumed']) == prior_cost, ('prior energy', name)
        assert Fraction(energy['remaining']) == remaining, ('remaining energy', name)
        assert Fraction(energy['accounted']) == remaining+prior_cost+aggregate['total_spent']+aggregate['total_lost'] == initial, ('full energy', name)
        counts['mixture_checks'] += 1

    for item in results['local_checks']:
        check_call(item['prefix'], item['case'], item['proposal'], item['execution'])
        counts['local_checks'] += 1
    assert used == set(results['executions']), ('unreferenced executions', set(results['executions'])-used)
    for key in inputs['mixtures']:
        ordinary = results['mixtures']['primary/'+key]
        conventional = results['mixtures']['ordinary_conventional/'+key]
        assert ordinary['metrics'] == conventional['metrics'], ('conventional mixture', key)
        assert ordinary['energy'] == conventional['energy'], ('conventional accounts', key)

    # Concrete prospective adverse/positive probabilities, preserving all failure mass.
    actual_summary = {}
    for group in ('primary', 'stable', 'controlled_proxy_stable'):
        for mode in ('primary', 'no_repair', 'no_monitor', 'late_reversal'):
            values = results['mixtures'][mode+'/'+group+'/variable']['metrics']
            actual_summary[mode+'/'+group] = {k:values[k] for k in
                ('revised_productive_successor','behaviorally_revised_productive_successor',
                 'recipient_updater_changes','child_captures','child_retained','copies')}
    assert Fraction(actual_summary['primary/primary']['revised_productive_successor']) == Fraction(1,72)
    assert Fraction(actual_summary['primary/primary']['behaviorally_revised_productive_successor']) == Fraction(1,72)
    assert Fraction(actual_summary['primary/controlled_proxy_stable']['behaviorally_revised_productive_successor']) == Fraction(1,144)
    assert Fraction(actual_summary['primary/primary']['child_retained']) == Fraction(1,24)
    assert Fraction(actual_summary['no_monitor/primary']['child_retained']) == Fraction(1,36)
    assert Fraction(actual_summary['primary/controlled_proxy_stable']['child_retained']) == Fraction(13,144)
    assert Fraction(actual_summary['no_monitor/controlled_proxy_stable']['child_retained']) == Fraction(1,9)
    assert all(path.read_bytes() == data for path, data in frozen.items()), 'Source/data changed during check'
    record = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  checker_sha256=sha_bytes(read(Path(__file__))),
                  counts=dict(counts, **dict(prefix_counts), distinct_executions=len(used)),
                  excluded_from_state_comparison=['stage (observer label only)'],
                  normalization='Consecutive identical physical snapshots coalesced; all phase, access, record, resource and material fields retained.',
                  producer_imported=False, producer_code_inspected=False,
                  scope='Independent new-suffix conventional update/payment/copy arithmetic and full physical trajectories; exact weighted ancestry/prefix binding. Existing monitor reference independently checks nonexport variants. No reexecution of the whole historical formation process, no empirical calibration and no Lean/Python refinement.',
                  summary=actual_summary,
                  source_sha256={str(path.relative_to(repo)):sha_bytes(data) for path,data in sorted(frozen.items())})
    (here/'check-model.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':record['status'],'counts':record['counts']},indent=2))


if __name__ == '__main__':
    main()
