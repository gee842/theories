#!/usr/bin/env python3
"""Independent oracle for the actual-recipient-cache / paid-reason interface.

The first reference functions were written from the prospective protocol, before
reading the producer implementation.  No producer module is imported.  Accepted
predecessor records are an explicit, hash-bound input, not synthetic observations.
"""
from collections import defaultdict, deque
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import copy
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
DESIGNATED = (False, True, False)
UNKNOWN = (None, None, None)
GRAPH = (('root', 'p'), ('root', 'q'), ('root', 'p'))
CATALOGUE = (('root', 'p'), ('root', 'q'),
             ('root', 'p', 'q'), ('root', 'q', 'p'))


def stable_key(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def normalize(cache, inaccessible=()):
    """Read all three signed facts; None never becomes a negative fact."""
    assert len(cache) == 3 and all(x is None or type(x) is bool for x in cache)
    normalized = [None if x is None or i in inaccessible else
                  (DESIGNATED[i] if x else not DESIGNATED[i])
                  for i, x in enumerate(cache)]
    known = {x for x in normalized if x is not None}
    conflict = len(known) > 1
    orientation = next(iter(known)) if len(known) == 1 else None
    facts = list(UNKNOWN) if orientation is None else [not orientation, orientation, None]
    return dict(normalized=normalized, orientation=orientation,
                conflict=conflict, facts=facts)


def closure(facts):
    """Independent breadth-first graph traversal; no path-catalogue fold."""
    reachable, todo = {'root'}, deque(['root'])
    while todo:
        node = todo.popleft()
        for (a, b), value in zip(GRAPH, facts):
            if a == node and value is True and b not in reachable:
                reachable.add(b)
                todo.append(b)
    return dict(p='p' in reachable, q='q' in reachable)


def path_valid(path, facts):
    return all(any(a == u and b == v and value is True
                   for (a, b), value in zip(GRAPH, facts))
               for u, v in zip(path, path[1:]))


def reason_reference(cache, fuel, *, workspace=True, current=True,
                     inaccessible=(), invalidation_after=None, lookup=False):
    """Execute the declared finite circuit, preserving paid incomplete prefixes.

    This deliberately models only reasoning.  The existing factual reader must
    already have completed its own paid work.  The lookup comparator's one-unit
    final operation is declared separately; it shares the same three paid reads.
    """
    out = dict(fuel=fuel, spent=0, normalized=[None]*3,
               facts=[None]*3, conflict=False, working=dict(p=False, q=False),
               published=False, result=None, completed=[], active=False)
    if not workspace or not current:
        return out
    analysis = normalize(cache, inaccessible)
    schedule = [('activate', 1)] + [('infer_' + str(i), 1) for i in range(3)]
    schedule += [('lookup', 1)] if lookup else [('path_' + str(i), len(p)-1)
                                             for i, p in enumerate(CATALOGUE)]
    for name, price in schedule:
        if out['fuel'] < price:
            break
        out['fuel'] -= price
        out['spent'] += price
        out['completed'].append(name)
        if name == 'activate':
            out['active'] = True
        elif name.startswith('infer_'):
            i = int(name[-1])
            out['normalized'][i] = analysis['normalized'][i]
            if i == 2:
                out['facts'] = analysis['facts']
                out['conflict'] = analysis['conflict']
        elif name == 'lookup':
            out['working'] = closure(out['facts'])
        else:
            i = int(name[-1])
            if path_valid(CATALOGUE[i], out['facts']):
                out['working'][CATALOGUE[i][-1]] = True
        if invalidation_after == name:
            out['active'] = False
            return out
    if len(out['completed']) == len(schedule):
        out['published'] = True
        out['result'] = dict(out['working'])
        out['active'] = False
    assert out['fuel'] + out['spent'] == fuel
    return out


def preparation_reference(initial_fuel=122, assemble_reason=True):
    """Actual seven-channel formation word with unchanged source interface."""
    # Free A, free H, resident (0 or A=1), intact, local, common, source.
    s = [0, 0, 0, 0, 0, initial_fuel, 144]
    spent, trace = 0, []
    word = ['form_h'] * 15 + ['form_a'] * 2 + ['bind_a', 'repair']
    word += ['capture', 'copy_a'] * 13 + ['capture']
    assert len(word) == 46
    for event in word:
        a, h, resident, intact, local, common, source = s
        free = 30 - a - h - int(resident != 0)
        if event in ('form_a', 'form_h'):
            assert not intact and free > 0 and common > 0
            s[event == 'form_h'] += 1
            s[5] -= 1
        elif event == 'bind_a':
            assert not resident and a > 0 and common > 0
            s[0] -= 1; s[2] = 1; s[5] -= 1
        elif event == 'repair':
            assert resident == 1 and not intact and common > 0
            s[3] = 1; s[5] -= 1
        elif event == 'capture':
            assert intact and not local and source > 0
            s[4] = 1; s[6] -= 1
        else:
            assert event == 'copy_a' and resident == 1 and local == 1 and free > 0
            s[0] += 1; s[4] = 0
        spent += event != 'capture'
        assert min(s) >= 0 and a + h + int(resident != 0) <= 30
        assert sum(s[4:]) + spent == initial_fuel + 144
        trace.append(dict(event=event, state=list(s), spent=spent))
    assert s == [14, 15, 1, 1, 1, initial_fuel - 19, 130] and spent == 32
    preassembly = list(s)
    assemblies = 13 + int(assemble_reason)
    for _ in range(assemblies):
        assert s[0] > 0 and s[1] > 1 and s[5] > 0
        s[0] -= 1; s[1] -= 1; s[5] -= 1; spent += 1
    free_pairs = int(not assemble_reason)
    assert s[:2] == [free_pairs, free_pairs + 1]
    assert 24 + 2 + 2*assemble_reason + 2 + 2*free_pairs == 30
    assert s[2:5] == [1, 1, 1]
    s[1] -= 1; s[2] = 0
    s[5] += s[4] - 1; s[4] = 0; spent += 1
    assert spent == 47 - free_pairs
    assert s[5] == initial_fuel - 33 + free_pairs
    assert sum(s[4:]) + spent == initial_fuel + 144
    # The omitted assembly's saving remains idle, not new functional capacity.
    extra = initial_fuel - 94
    assert extra >= 0
    routes = dict(working=26, archive=15, original_reader=20,
                  extra=extra, idle=free_pairs)
    assert sum(routes.values()) == s[5]
    return dict(initial_fuel=initial_fuel, preassembly=preassembly, trace=trace,
                state=list(s), spent=spent, free_pairs=free_pairs, routes=routes)


def factual_reference(archive, fuel, context):
    """Cold reading from actual cells, with no copied operational cache."""
    out = dict(fuel=fuel, spent=0, cache=[None]*3, cache_context=None,
               cache_valid=False, read_count=0, completed=[])
    operations = [('activate', 1), ('sense', 1)] + [('read_' + str(i), 4)
                                                         for i in range(3)]
    for name, cost in operations:
        if out['fuel'] < cost:
            break
        out['fuel'] -= cost; out['spent'] += cost
        out['completed'].append(name)
        if name == 'sense':
            out['cache_context'] = context
        elif name.startswith('read_'):
            i = int(name[-1])
            frame, bits = archive['frames'][i], archive['cells'][4*i:4*i+4]
            if (frame['complete'] and frame['valid'] and
                    all(x is not None for x in bits) and bits[0] == context
                    and bits[2] == bits[3] == 1):
                out['cache'][i] = bits[1] == DESIGNATED[i]
            out['read_count'] += 1
    out['cache_valid'] = out['read_count'] == 3
    assert out['fuel'] + out['spent'] == fuel
    return out


def prospective_checks():
    cache_cases = payment_cases = sound_cases = 0
    for cache in product((None, False, True), repeat=3):
        inference = normalize(cache)
        graph_result = closure(inference['facts'])
        for budget in range(25):
            run = reason_reference(cache, budget)
            assert run['published'] == (budget >= 10)
            if run['published']:
                assert run['result'] == graph_result
            else:
                assert run['result'] is None
            assert run['spent'] <= budget
            payment_cases += 1
        for cut in ('activate', 'infer_0', 'infer_1', 'infer_2',
                    'path_0', 'path_1', 'path_2', 'path_3'):
            assert not reason_reference(cache, 10, invalidation_after=cut)['published']
        cache_cases += 1
    for orientation in (False, True):
        truth = tuple(orientation == d for d in DESIGNATED)
        for kept in product((False, True), repeat=3):
            cache = tuple(x if k else None for x, k in zip(truth, kept))
            inference = normalize(cache)
            assert not inference['conflict']
            assert inference['orientation'] is (orientation if any(kept) else None)
            for action in (False, True):
                compatibility = all((availability and action == orientation) == availability
                                    for availability in (False, True))
                assert compatibility == (action == orientation)
            sound_cases += 1
    # Actual opposite-orientation strict cache, including a usable negative fact.
    assert normalize((None, False, True), (2,))['orientation'] is False
    assert normalize((None, False, True), (1, 2))['orientation'] is None
    assert normalize((None, True, True))['conflict']
    assert normalize((None, True, False))['orientation'] is True
    for initial in (97, 98, 121, 122):
        p = preparation_reference(initial)
        reader_after_first_read = 6 + p['routes']['extra']
        first = reason_reference((None, False, True), reader_after_first_read)
        assert first['published'] == (initial >= 98)
        if first['published'] and first['fuel'] >= 14:
            second = reason_reference((None, False, True), first['fuel'] - 14)
            assert second['published'] == (initial >= 122)
    missing = preparation_reference(122, False)
    assert missing['routes']['idle'] == missing['free_pairs'] == 1
    assert not reason_reference((None, False, True), 100, workspace=False)['published']
    assert not reason_reference((None, False, True), 100, current=False)['published']
    return dict(cache_vectors=cache_cases, paid_prefix_cases=payment_cases,
                sound_partial_cache_cases=sound_cases, formation_cases=5,
                actual_negative_complement_checked=True,
                uniform_corruption_can_remain_consistent=True)


def expected_cases():
    base = dict(initial_common=122, cycles=2, parent_case='primary', workspace=True,
                original=False, access=[True]*3, lookup=False, between='cold', during=None)
    modifications = {
        'primary': {},
        'single_min': dict(initial_common=98, cycles=1),
        'single_short': dict(initial_common=97, cycles=1),
        'double_short': dict(initial_common=121),
        'no_workspace': dict(workspace=False),
        'original_endpoint': dict(initial_common=91, original=True, workspace=False, cycles=1),
        'missing_channel': dict(parent_case='missing_channel'),
        'stale_facts': dict(parent_case='stale_context'),
        'partial_archive': dict(parent_case='interrupted_write'),
        'partial_factual_cache': dict(parent_case='reader_short', cycles=1),
        'remove_late_positive': dict(access=[True, True, False]),
        'remove_both_grounds': dict(access=[True, False, False]),
        'disagree_second': dict(between='corrupt_last_action'),
        'consistently_corrupt': dict(parent_case='corrupt_action_tag'),
        'changed_context': dict(between='changed_context'),
        'same_context_reopen': dict(cycles=1, during='after_publication_same_context'),
        'context_during_replay': dict(cycles=1, during='after_first_path_context'),
        'lookup_comparator': dict(lookup=True),
    }
    return {name: dict(base, **change) for name, change in modifications.items()}


def object_hash(value):
    return sha256(stable_key(value).encode()).hexdigest()


def paid_trace_audit(case, predecessor, row):
    """Check each recorded transition against an independently stated event law.

    Costs and enabledness are checked before the mutation.  Actual cache reads
    use inherited physical cells.  Neither truth nor observer success labels
    enters the replay state; they are used separately in metric comparisons.
    """
    p = copy.deepcopy(predecessor)
    extra = 0 if case['original'] else case['initial_common'] - 94
    idle = int(not case['original'] and not case['workspace'])
    s = dict(reader_fuel=p['reader_fuel'], extra_reserve=extra, external_idle=idle,
             decode_spent=p['decode_spent'], reason_spent=0, context=p['context'],
             cache=list(p['cache']), cache_context=p['cache_context'],
             cache_valid=p['cache_valid'], read_count=p['read_count'], phase='handoff',
             active=False, inference_index=0, path_index=0, normalized=[None]*3,
             orientation=None, conflict=False, facts=[None]*3, working=[False]*3,
             publication=None, publication_current=False)
    initial_account = s['reader_fuel'] + s['extra_reserve'] + s['decode_spent'] + idle
    snapshots = []
    audits = []
    def complete():
        return s['cache_valid'] and s['read_count'] == 3 and s['cache_context'] == s['context']
    def spend(amount, account):
        assert s['reader_fuel'] >= amount
        s['reader_fuel'] -= amount
        s[account] += amount
    for j, entry in enumerate(row['runtime_trace']):
        event = entry['event']
        if event == 'actual_factual_handoff_with_retained_frame':
            assert j == 0
        elif event == 'transfer_preexisting_protected_reserve':
            assert j == 1
            s['reader_fuel'] += s['extra_reserve']; s['extra_reserve'] = 0
        elif event == 'cold_operational_turnover':
            audits.append(copy.deepcopy(s))
            s.update(cache=[None]*3, cache_context=None, cache_valid=False, read_count=0,
                     active=False, phase='cold', publication=None, publication_current=False,
                     normalized=[None]*3, orientation=None, conflict=False, facts=[None]*3,
                     working=[False]*3, inference_index=0, path_index=0)
        elif event in ('context_changed_between_cycles', 'context_change_during_paths',
                       'same_context_reopening'):
            assert ((event == 'context_changed_between_cycles' and case['between'] == 'changed_context')
                    or (event == 'context_change_during_paths' and
                        case['during'] == 'after_first_path_context')
                    or (event == 'same_context_reopening' and
                        case['during'] == 'after_publication_same_context'))
            if event != 'same_context_reopening':
                s['context'] = not s['context']
            s.update(cache_valid=False, active=False, phase='invalidated', publication_current=False)
        elif event == 'fault_flip_stored_last_action_bit':
            assert case['between'] == 'corrupt_last_action' and p['frames'][2]['complete']
            p['cells'][9] ^= 1
        elif event == 'factual_activation_unaffordable':
            assert s['reader_fuel'] < 1
            s.update(active=False, phase='factual_reading', publication_current=False)
        elif event == 'factual_activate':
            spend(1, 'decode_spent')
            s.update(active=False, phase='factual_reading', publication_current=False,
                     cache=[None]*3, cache_context=None, cache_valid=False, read_count=0)
        elif event == 'factual_paid_context_sense':
            spend(1, 'decode_spent'); s['cache_context'] = s['context']
        elif event == 'factual_four_cell_read':
            assert s['phase'] == 'factual_reading' and s['read_count'] < 3
            i = s['read_count']
            assert s['cache_context'] == s['context']
            spend(4, 'decode_spent')
            frame, bits = p['frames'][i], p['cells'][4*i:4*i+4]
            value = None
            if (frame['complete'] and frame['valid'] and all(x is not None for x in bits)
                    and bits[0] == s['context'] and bits[2] == bits[3] == 1):
                value = bits[1] == DESIGNATED[i]
            s['cache'][i] = value; s['read_count'] += 1
        elif event == 'factual_read_unaffordable':
            assert s['reader_fuel'] < 4 and s['read_count'] < 3
        elif event == 'factual_complete':
            assert s['read_count'] == 3
            s['cache_valid'] = s['cache_context'] == s['context']
        elif event == 'reason_activation_unavailable':
            assert not case['workspace'] or not complete() or s['reader_fuel'] < 1
        elif event == 'reason_activate_root':
            assert case['workspace'] and complete()
            spend(1, 'reason_spent')
            s.update(active=True, phase='inference', normalized=[None]*3, orientation=None,
                     conflict=False, facts=[None]*3, working=[True, False, False],
                     publication_current=False, inference_index=0, path_index=0)
        elif event.startswith('paid_inference_'):
            i = int(event.rsplit('_', 1)[1])
            assert s['active'] and complete() and i == s['inference_index']
            spend(1, 'reason_spent')
            s['normalized'][i] = normalize(s['cache'],
                    [k for k, access in enumerate(case['access']) if not access])['normalized'][i]
            s['inference_index'] += 1
        elif event == 'inference_unaffordable':
            assert s['reader_fuel'] < 1 and s['inference_index'] < 3
        elif event == 'combine_inference':
            assert s['inference_index'] == 3
            known = {x for x in s['normalized'] if x is not None}
            s['orientation'] = next(iter(known)) if len(known) == 1 else None
            s['conflict'] = len(known) == 2
            z = s['orientation']
            s['facts'] = [None]*3 if z is None else [not z, z, None]
            s['phase'] = 'paths'
        elif event.startswith('paid_path_'):
            i = int(event.rsplit('_', 1)[1]); path = CATALOGUE[i]
            assert not case['lookup'] and s['active'] and complete() and s['path_index'] == i
            spend(len(path)-1, 'reason_spent')
            if path_valid(path, s['facts']):
                s['working'][1 if path[-1] == 'p' else 2] = True
            s['path_index'] += 1
        elif event.startswith('path_unaffordable_'):
            i = int(event.rsplit('_', 1)[1])
            assert s['path_index'] == i and s['reader_fuel'] < len(CATALOGUE[i])-1
        elif event == 'paid_direct_lookup':
            assert case['lookup'] and s['active'] and complete()
            spend(1, 'reason_spent')
            reached = closure(s['facts'])
            s.update(working=[True, reached['p'], reached['q']], path_index=4)
        elif event == 'lookup_unaffordable':
            assert case['lookup'] and s['reader_fuel'] < 1
        elif event == 'publish_completed_reason':
            assert s['active'] and complete() and s['inference_index'] == 3 and s['path_index'] == 4
            reached = closure(s['facts'])
            assert s['working'] == [True, reached['p'], reached['q']]
            s.update(phase='published', active=False, publication_current=True,
                     publication=dict(context=s['context'], mask=list(s['working'])))
        else:
            raise AssertionError(('unknown event', event))
        assert (s['reader_fuel'] + s['extra_reserve'] + s['external_idle']
                + s['decode_spent'] + s['reason_spent']) == initial_account
        if s['publication_current']:
            assert s['phase'] == 'published' and complete()
            assert s['publication']['context'] == s['context']
        assert s == entry['state'], (case, j, event, s, entry['state'])
        snapshots.append(copy.deepcopy(s))
    audits.append(copy.deepcopy(s))
    assert len(audits) == case['cycles'] and audits == row['audits']
    assert s == row['state']
    invariant = row['endpoint_invariants']
    assert invariant['core_sha256'] == object_hash(p['core'])
    assert invariant['frames_sha256'] == object_hash(p['frames'])
    assert invariant['pending'] == p['pending'] and invariant['archive_escrow'] == p['archive_escrow']
    assert invariant['cells'] == p['cells'] and invariant['material'] == (28 if case['original'] else 30)
    return s, audits, len(snapshots)


def whole_schedule_audit(case, predecessor, audits):
    """Check that the saved execution runs the prescribed schedule, not only
    that its individual events are legal.  Uses the preimplementation oracle.
    """
    archive = copy.deepcopy(predecessor)
    fuel = predecessor['reader_fuel'] + (0 if case['original'] else case['initial_common']-94)
    cache, context = list(predecessor['cache']), predecessor['context']
    cache_context = predecessor['cache_context']
    complete = predecessor['cache_valid'] and predecessor['read_count'] == 3 and cache_context == context
    reason_paid, factual_paid = 0, predecessor['decode_spent']
    for cycle, actual in enumerate(audits):
        if cycle:
            if case['between'] == 'changed_context':
                context = not context
            if case['between'] == 'corrupt_last_action' and archive['frames'][2]['complete']:
                archive['cells'][9] ^= 1
            read = factual_reference(archive, fuel, context)
            fuel = read['fuel']; factual_paid += read['spent']
            cache, cache_context = read['cache'], read['cache_context']
            complete = read['cache_valid']
        run = reason_reference(cache, fuel, workspace=case['workspace'], current=complete,
                inaccessible=[i for i, allowed in enumerate(case['access']) if not allowed],
                invalidation_after='path_0' if case['during'] == 'after_first_path_context' else None,
                lookup=case['lookup'])
        fuel = run['fuel']; reason_paid += run['spent']
        assert actual['reader_fuel'] == fuel
        assert actual['reason_spent'] == reason_paid and actual['decode_spent'] == factual_paid
        assert actual['normalized'] == run['normalized'] and actual['facts'] == run['facts']
        assert actual['conflict'] == run['conflict']
        root_seeded = 'activate' in run['completed']
        assert actual['working'] == [root_seeded, run['working']['p'], run['working']['q']]
        expected_publication = run['published'] and case['during'] != 'after_publication_same_context'
        assert actual['publication_current'] == expected_publication
        assert actual['cache'] == cache
        if case['during'] == 'after_first_path_context' and root_seeded:
            context = not context
        assert actual['context'] == context and actual['cache_context'] == cache_context


def audit_saved_results():
    results = json.loads((HERE / 'results.json').read_text())
    fixtures = json.loads((HERE / 'fixtures.json').read_text())['fixtures']
    parent_result = json.loads((HERE.parent / 'results.json').read_text())
    parent_fixture = json.loads((HERE.parent / 'fixtures.json').read_text())['fixtures']
    cases = expected_cases()
    assert set(cases) == set(results['cases'])
    formation_words = 0
    for prep in fixtures['preparations'].values():
        if prep['material'] == 28:
            assert prep['construction_spent'] == 44 and prep['fuel'] == 61 and prep['source'] == 130
            assert prep['reason_parts'] == prep['extra_reserve'] == prep['external_idle'] == 0
            continue
        own = preparation_reference(prep['initial_common'], bool(prep['reason_parts']))
        assert prep['construction_spent'] == own['spent']
        assert [prep['free_a'], prep['free_h']] == own['state'][:2]
        assert [prep['fuel'], prep['source']] == own['state'][5:]
        for expected, actual in zip(own['trace'], prep['trace'][1:47]):
            assert actual == dict(event=expected['event'], plant=expected['state'], spent=expected['spent'])
        assert len(prep['trace']) == 48 + 13 + bool(prep['reason_parts'])
        stock = own['preassembly'][:]
        for i, actual in enumerate(prep['trace'][47:-1]):
            assert stock[0] > 0 and stock[1] > 1 and stock[5] > 0
            stock[0] -= 1; stock[1] -= 1; stock[5] -= 1
            kind = 'assemble_cell' if i < 12 else ('assemble_factual_reader' if i == 12
                                                   else 'assemble_reason_workspace')
            assert actual == dict(event=kind, plant=stock, bound_parts=2*(i+1), spent=33+i)
            assert stock[0]+stock[1]+1+actual['bound_parts'] == 30
            assert sum(stock[4:])+actual['spent'] == prep['initial_common']+144
        assert prep['trace'][-1] == dict(event='existing_adapter', fuel=own['state'][5],
                source=130, free_a=own['free_pairs'], free_h=own['free_pairs'], spent=own['spent'])
        formation_words += 1
    arm_count = path_count = metric_count = microstates = 0
    values = {}
    for name, case in cases.items():
        saved_case = results['cases'][name]
        assert saved_case['law'] == case
        route = fixtures['routes'][name]['route']
        prep = fixtures['preparations'][fixtures['routes'][name]['preparation_key']]
        old_route = parent_fixture['routes'][case['parent_case']]
        assert route['working'] == old_route['working'] == 26
        assert route['archive'] == old_route['archive']
        assert route['original_reader'] == old_route['reader']
        assert route['original_idle'] == old_route['idle']
        assert route['extra_reserve'] == (0 if case['original'] else case['initial_common'] - 94)
        assert route['source'] == 130 and route['common'] == prep['fuel']
        assert sum(route[k] for k in ('working', 'archive', 'original_reader',
                                     'original_idle', 'extra_reserve', 'external_idle')) == prep['fuel']
        for producer, saved_arm in saved_case['producers'].items():
            previous = parent_result['cases'][case['parent_case']]['producers'][producer]['paths']
            assert len(previous) == len(saved_arm['paths'])
            sums = defaultdict(Q)
            for i, (old, row) in enumerate(zip(previous, saved_arm['paths'])):
                reference = row['predecessor']
                assert reference == dict(case=case['parent_case'], producer=producer, path_index=i,
                        prefix_id=old['prefix_id'], state_sha256=object_hash(old['state']),
                        core_history_sha256=object_hash(old['core_history']))
                probability = Q(row['probability'])
                assert probability == Q(old['probability'])
                s, audits, count = paid_trace_audit(case, old['state'], row)
                whole_schedule_audit(case, old['state'], audits)
                microstates += count
                prefix = parent_fixture['prefix_records'][producer][old['prefix_id']]
                marks = prefix['conditional_mean_marks']
                p = old['state']
                core = p['core']
                retained = sum(core[k] for k in ('fuel', 'recipient', 'source', 'escrow'))
                retained += sum(p[k] for k in ('archive_fuel', 'archive_escrow', 'idle_fuel', 'packet_inflight'))
                retained += s['reader_fuel'] + s['extra_reserve'] + s['external_idle']
                observed = dict(final_reader=s['reader_fuel'], final_working=core['fuel'],
                        final_recipient=core['recipient'], final_source=core['source'],
                        reason_spent=s['reason_spent'], factual_spent=s['decode_spent'],
                        construction_spent=prep['construction_spent'], retained=retained,
                        prefix_spent=Q(marks['spent']), prefix_waste=Q(marks['waste']),
                        core_spent=p['core_spent'], core_waste=p['core_waste'],
                        archive_spent=p['archive_spent'], reason_parts=prep['reason_parts'],
                        unbound_reason_parts=prep['unbound_reason_parts'])
                assert sum(observed[k] for k in ('construction_spent', 'prefix_spent', 'prefix_waste',
                      'core_spent', 'core_waste', 'archive_spent', 'factual_spent',
                      'reason_spent', 'retained')) == case['initial_common'] + 144
                truth = not bool(prefix['final_regime'])
                strict = bool(old['metrics']['strict_core_witness'])
                for cycle, audit in enumerate(audits, 1):
                    pub = audit['publication_current']
                    mask = audit['publication']['mask'] if pub else [False]*3
                    observed.update({f'cycle{cycle}_published': int(pub),
                        f'cycle{cycle}_nonroot': int(pub and any(mask[1:])),
                        f'cycle{cycle}_false_route': int(pub and mask[2-int(truth)]),
                        f'cycle{cycle}_conflict': int(audit['conflict']),
                        f'cycle{cycle}_strict_instrumental': int(strict and pub and mask[1+int(truth)]),
                        f'cycle{cycle}_root_only': int(pub and mask == [True, False, False])})
                observed['strict_both_replays'] = int(len(audits) == 2 and strict and
                        all(a['publication_current'] and a['publication']['mask'][1+int(truth)] for a in audits))
                assert {k: Q(v) for k, v in row['metrics'].items()} == observed
                for field, value in observed.items():
                    sums[field] += probability * value
                path_count += 1
            assert sum(Q(r['probability']) for r in saved_arm['paths']) == 1
            assert dict(sums) == {k: Q(v) for k, v in saved_arm['metrics'].items()}
            values[name, producer] = dict(sums)
            metric_count += len(sums)
            arm_count += 1
        assert values[name, 'variable'] == values[name, 'conventional']
        conventional_rows = copy.deepcopy(saved_case['producers']['conventional'])
        variable_rows = copy.deepcopy(saved_case['producers']['variable'])
        for arm in (conventional_rows, variable_rows):
            for row in arm['paths']:
                row['predecessor']['producer'] = 'same_behavior'
        assert conventional_rows == variable_rows
    return dict(arms=arm_count, histories=path_count, exact_metrics=metric_count,
                paid_microstates=microstates, new_formation_words=formation_words,
                primary_strict_both_replays=str(values['primary', 'variable']['strict_both_replays']),
                main_comparisons={name: {k: str(v) for k, v in values[name, 'variable'].items()
                                       if k in ('final_reader', 'reason_spent', 'factual_spent',
                                                'cycle1_nonroot', 'cycle2_nonroot',
                                                'cycle2_conflict', 'cycle2_false_route', 'strict_both_replays')}
                                  for name in cases})


def verify_hashes(mapping):
    for relative, expected in mapping.items():
        assert sha256((ROOT / relative).read_bytes()).hexdigest() == expected, relative


def audit_receipts(manifest):
    producer = json.loads((HERE / 'check.json').read_text())
    assert producer['status'] == 'passed'
    assert producer['checker_sha256'] == sha256((HERE / 'check.py').read_bytes()).hexdigest()
    verify_hashes(producer['source_sha256'])
    for name, expected in producer['data_sha256'].items():
        assert sha256((HERE / name).read_bytes()).hexdigest() == expected
    predecessor = json.loads((HERE.parent / 'independent-check.json').read_text())
    assert predecessor['status'] == 'passed'
    verify_hashes(predecessor['source_sha256'])
    folder = HERE / 'formal'
    report = json.loads((folder / 'verification.json').read_text())
    assert report['status'] == 'passed' and report['source_unchanged_during_check']
    assert report['fresh_temporary_build'] and report['project_objects_only_from_frozen_sources']
    assert report['checker_sha256'] == sha256((folder / 'check.py').read_bytes()).hexdigest()
    assert report['toolchain_sha256'] == sha256((folder / 'lean-toolchain').read_bytes()).hexdigest()
    assert report['compiler_sha256'] == sha256(Path(report['compiler_binary']).read_bytes()).hexdigest()
    new = inherited = 0
    axioms = set()
    for module in report['modules']:
        source = ROOT / module['source']
        output = folder / module['output']
        assert module['exit_code'] == 0 and module['clean_dependency_audit']
        assert sha256(source.read_bytes()).hexdigest() == module['source_sha256']
        assert sha256(output.read_bytes()).hexdigest() == module['output_sha256']
        code, log = source.read_text(), output.read_text()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', code)
        assert 'sorryAx' not in log and 'warning:' not in log
        audited = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[[^\]]*\])", log)
        assert audited == module['audited_declarations']
        assert len(audited) == module['dependency_audits']
        if module['role'] == 'new formalization':
            declared = set(re.findall(r'^theorem\s+(\w+)', code, re.M))
            assert declared == {name.rsplit('.', 1)[-1] for name in audited}
            new += len(audited)
        else:
            inherited += len(audited)
        axioms.update(module['axioms'])
        for path in (source, output):
            manifest[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    assert new == report['new_audited_declarations']
    assert axioms <= {'propext', 'Quot.sound', 'Classical.choice'}
    for path in (folder / 'verification.json', folder / 'check.py', folder / 'lean-toolchain',
                 folder / 'README.md', ROOT / '_process/research/2026-10-05-concern-theory/RECIPIENT-REASONS-MATH.md'):
        assert path.exists(), path
        manifest[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    return dict(status='passed', new_declaration_audits=new,
                inherited_declaration_audits=inherited, modules=len(report['modules']),
                axioms=sorted(axioms), compiler_hash_verified=True,
                source_checker_toolchain_and_log_hashes_verified=True,
                scope='Independent source and fresh-build receipt inspection; no separate Lean rerun or Python-refinement claim.')


def main():
    local = prospective_checks()
    if not (HERE / 'results.json').exists():
        print(json.dumps(local, indent=2)); return
    result_doc = json.loads((HERE / 'results.json').read_text())
    fixture_doc = json.loads((HERE / 'fixtures.json').read_text())
    assert result_doc['source_sha256'] == fixture_doc['source_sha256']
    manifest = dict(result_doc['source_sha256'])
    verify_hashes(manifest)
    result = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  method='No producer imports. Preimplementation truth/paid-prefix/formation references; independent event, schedule, ledger and exact-rational replay of hash-bound actual predecessor records.',
                  scope='Conditional finite construction; supplied objective and functional recipes; inherited conditional-mean prefix accounts; no full stochastic Lean/Python refinement or empirical claim.',
                  reference_contract=local, finite_comparison=audit_saved_results())
    if not (HERE / 'formal/verification.json').exists():
        print(json.dumps(dict(status='numerical_passed_formal_pending',
                              comparison=result['finite_comparison']), indent=2)); return
    result['formal_receipt_inspection'] = audit_receipts(manifest)
    for name in ('independent_check.py', 'fixtures.json', 'results.json', 'PROTOCOL.md',
                 'protocol-freeze.json', 'model.py', 'check.py', 'check.json', 'README.md'):
        path = HERE / name
        manifest[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    for name in ('independent-check.json', 'check.json', 'fixtures.json', 'results.json'):
        path = HERE.parent / name
        manifest[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    verify_hashes(manifest)
    result['source_sha256'] = manifest
    (HERE / 'independent-check.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(status=result['status'], reference_contract=local,
                         finite_comparison=result['finite_comparison'],
                         formal_receipt_inspection=result['formal_receipt_inspection']), indent=2))


if __name__ == '__main__':
    main()
