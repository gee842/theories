#!/usr/bin/env python3
"""Independent physical-word reference for the recipient recording interface.

No producer is imported. Potential opportunity words are drawn in advance;
an imperative actor and separate archive execute each physical history. The
formation reference checks guards and conservation without importing the old
event table. Saved predecessor rows remain an inherited, hash-bound input.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import copy
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
DESIRED = (0, 1, 0)


def key(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'))


def formation_reference(cell_count=12):
    # a, h, resident, intact, local, common, incident source
    s = [0, 0, 0, 0, 0, 91, 144]
    trace, spent = [], 0
    word = ['form_h']*14+['form_a', 'bind_a', 'repair']
    word += ['capture', 'copy_a']*13+['capture']
    assert len(word) == 44
    for event in word:
        a, h, r, c, local, f, e = s
        precursor = 28-a-h-int(r != 0)
        if event in ('form_a', 'form_h'):
            assert c == 0 and precursor > 0 and f > 0
            s[int(event == 'form_h')] += 1
            s[5] -= 1
        elif event == 'bind_a':
            assert r == 0 and a > 0 and f > 0
            s[0] -= 1; s[2] = 1; s[5] -= 1
        elif event == 'repair':
            assert r == 1 and c == 0 and f > 0
            s[3] = 1; s[5] -= 1
        elif event == 'capture':
            assert c == 1 and local == 0 and e > 0
            s[4] = 1; s[6] -= 1
        else:
            assert event == 'copy_a' and r == 1 and precursor > 0 and local == 1
            s[0] += 1; s[4] = 0
        spent += int(event != 'capture')
        assert min(s) >= 0 and s[0]+s[1]+int(s[2] != 0) <= 28
        assert sum(s[4:])+spent == 235
        trace.append(dict(event=event, state=list(s), spent=spent))
    assert s == [13, 14, 1, 1, 1, 74, 130] and spent == 30
    assert 0 <= cell_count <= 12
    # Separate new assembly phase: bound matter is never fresh precursor.
    for _ in range(cell_count+1):
        assert s[0] > 0 and s[1] > 1 and s[5] > 0
        s[0] -= 1; s[1] -= 1; s[5] -= 1; spent += 1
    free_pairs = 12-cell_count
    assert s[0] == free_pairs and s[1] == free_pairs+1
    assert 2*cell_count+2+2+2*free_pairs == 28
    # Project only the remaining resident A/free H/local unit to the old adapter.
    assert s[2:5] == [1, 1, 1]
    s[5] += s[4]-1; s[4] = 0; spent += 1
    assert s[5] == 61+free_pairs and s[6] == 130
    assert spent == 44-free_pairs and sum(s[4:])+spent == 235
    return dict(trace=trace, state=s, spent=spent, free_pairs=free_pairs)


def eligible(s):
    return (s['stage'] == 2 and s['life'] > 0 and s['gate_life'] > 0
            and s['coupling_life'] > 0 and s['coupling'] == 0
            and s['written'] and s['q'] in (0, 4))


def frame_certificate(bits, *, desired, current, complete=True, valid=True):
    if not complete or not valid or len(bits) != 4 or any(x is None for x in bits):
        return None
    context, action, present, receipt = bits
    if context != current or present != 1 or receipt != 1:
        return None
    return action == desired


def local_contract_checks():
    checked = 0
    for bits in product((0, 1), repeat=4):
        for context, desired, complete, valid in product((0, 1), repeat=4):
            result = frame_certificate(bits, desired=desired, current=context,
                                       complete=complete, valid=valid)
            expected = bits[1] == desired if (complete and valid and bits[0] == context
                                             and bits[2] == bits[3] == 1) else None
            assert result is expected
            checked += 1
    # Paid pending state: no record is usable until all four distinct writes.
    cells, escrow, spent = [None]*4, 4, 1
    frame = [0, 1, 1, 1]
    for position in range(4):
        assert frame_certificate(cells, desired=0, current=0,
                                 complete=False) is None
        assert cells[position] is None and escrow > 0
        cells[position] = frame[position]; escrow -= 1; spent += 1
        assert escrow+spent == 5
        assert all(cells[i] is not None for i in range(position+1))
    assert frame_certificate(cells, desired=0, current=0) is False
    assert escrow == 0 and all(x is not None for x in cells)
    # A duplicate commit has neither a blank cell nor remaining write escrow.
    duplicate_enabled = escrow > 0 and cells[3] is None
    assert not duplicate_enabled
    # Fixed holes do not shift a later query's designated predicate/address.
    frames = [None, [0, 1, 1, 1], [0, 1, 1, 0]]
    decoded = [None if row is None else frame_certificate(row, desired=DESIRED[i], current=0)
               for i, row in enumerate(frames)]
    assert decoded == [None, True, None]
    return dict(frame_truth_table_cases=checked, distinct_paid_writes=4,
                duplicate_commit_disabled=True, fixed_hole_decoding=decoded)


def case_parameters(name):
    assert name in ('primary', 'archive_short', 'cell_short', 'reader_short',
                    'missing_channel', 'no_opportunity', 'actor_charged',
                    'interrupted_write', 'context_during_binding',
                    'stale_context', 'corrupt_action_tag')
    return dict(archive=14 if name == 'archive_short' else 15,
                reader=13 if name == 'reader_short' else 20,
                cell_count=11 if name == 'cell_short' else 12,
                channel=name != 'missing_channel',
                availability=Q(0) if name == 'no_opportunity' else Q(3, 4))


def run_word(name, inherited, actor_truth, word):
    """Independent core and sidecar execution for one exogenous word."""
    p = case_parameters(name)
    core = dict(inherited, recipient=0, source=50, active=False,
                installed=False, recoded=False, escrow=0)
    side = dict(archive_fuel=p['archive'], reader_fuel=p['reader'],
                idle_fuel=15-p['archive']+20-p['reader']+12-p['cell_count'],
                archive_escrow=0, cells=[None]*12, frames=[None]*3,
                pending=None, query_pointer=0, context=False, cache=[None]*3,
                cache_context=None, cache_valid=False, read_count=0,
                archive_spent=0, decode_spent=0)
    costs = dict(core_spent=0, core_waste=0)
    trace, history = [], []
    initial_energy = inherited['fuel']+50+35+12-p['cell_count']

    def snapshot(event, inflight=0):
        total = sum(core[x] for x in ('fuel', 'recipient', 'source', 'escrow'))
        total += sum(side[x] for x in ('archive_fuel', 'reader_fuel', 'idle_fuel', 'archive_escrow'))
        total += sum(costs.values())+side['archive_spent']+side['decode_spent']+inflight
        assert total == initial_energy, (name, event, total, initial_energy)
        assert min(core[x] for x in ('fuel', 'recipient', 'source', 'escrow')) >= 0
        trace.append(dict(event=event, core=copy.deepcopy(core), archive=copy.deepcopy(side),
                          costs=dict(costs), inflight=inflight))

    if eligible(inherited) and core['fuel'] >= 4:
        core['fuel'] -= 4; costs['core_spent'] += 4
        bit = inherited['q']//4
        core.update(q=3*bit, last=0, active=True, installed=True, recoded=True)
    snapshot('setup')
    for exposure in range(5):
        recipient = exposure % 2 == 0
        before = dict(core)
        event = dict(target='recipient' if recipient else 'actor', action=None,
                     capture=None, receipt=None, before=before, status='completed')
        core['source'] -= 10
        bill = 13 if recipient and name == 'actor_charged' else 8
        if not core['active'] or core['fuel'] < bill:
            event['status'] = 'unaffordable' if core['active'] else 'inactive'
            core['active'] = False
            costs['core_waste'] += 10
            snapshot('miss')
            event['after'] = dict(core); history.append(event)
            continue
        action = core['q']//2 if recipient else core['q'] % 2
        event['action'] = action
        actor_cell = core['q'] % 2
        core['fuel'] -= 2; costs['core_spent'] += 2
        snapshot('paid_sense', 10)
        address = side['query_pointer'] if recipient else None
        admitted = False
        if recipient:
            side['query_pointer'] += 1
            enough_cells = address < 3 and 4*(address+1) <= p['cell_count']
            bank = core['fuel'] if name == 'actor_charged' else side['archive_fuel']
            admitted = enough_cells and side['pending'] is None and bank >= 5
            if admitted:
                if name == 'actor_charged':
                    core['fuel'] -= 5
                else:
                    side['archive_fuel'] -= 5
                side['archive_spent'] += 1; side['archive_escrow'] = 4
                side['pending'] = address
                side['frames'][address] = dict(context=int(side['context']), action=action,
                    bound=True, latched=False, written=0, complete=False, valid=True)
                snapshot('bind', 10)
                if name == 'context_during_binding' and address == 0:
                    side['context'] = True
                    side['frames'][address]['valid'] = False
                    side['cache_valid'] = False
                    snapshot('context_change', 10)
        core['fuel'] -= 3; core['escrow'] = 3
        snapshot('core_reserve', 10)
        core['fuel'] -= 3; costs['core_spent'] += 3
        snapshot('work', 10)
        capture = bool(action == (actor_truth ^ int(recipient))
                       and (word[exposure//2] if recipient else True))
        if capture:
            core['recipient' if recipient else 'fuel'] += 10
        else:
            costs['core_waste'] += 10
        snapshot('receipt')
        receipt = capture if not recipient or p['channel'] else None
        event.update(capture=capture, receipt=receipt)
        core['escrow'] -= 1; costs['core_spent'] += 1
        if admitted:
            frame = side['frames'][address]
            frame['latched'] = True
            frame['bits'] = [frame['context'], action, int(receipt is not None), int(bool(receipt))]
            if name == 'corrupt_action_tag':
                frame['bits'][1] ^= 1
        snapshot('acquire')
        if recipient and receipt is not None and not core['last']:
            if receipt:
                core['last'] = 1
            else:
                action = 1-action
            core['q'] = actor_cell+2*action
        core['escrow'] -= 2; costs['core_spent'] += 2
        snapshot('core_write')
        if admitted and side['frames'][address]['valid']:
            frame = side['frames'][address]
            n = 2 if name == 'interrupted_write' and address == 0 else 4
            for index in range(n):
                cell = 4*address+index
                assert side['cells'][cell] is None and side['archive_escrow'] > 0
                bit = frame['bits'][index]
                side['cells'][cell] = bit
                side['archive_escrow'] -= 1; side['archive_spent'] += 1
                frame['written'] += 1
                if frame['written'] == 4:
                    frame['complete'] = True; side['pending'] = None
                snapshot('bit_write')
            if n == 4:
                frame['complete'] = True; side['pending'] = None
                snapshot('frame_complete')
        event['after'] = dict(core); history.append(event)
    if name == 'stale_context':
        side['context'] = True; side['cache_valid'] = False
        snapshot('context_change')
    if side['reader_fuel'] >= 1:
        side['reader_fuel'] -= 1; side['decode_spent'] += 1
        side['cache'] = [None]*3; side['cache_valid'] = False
        snapshot('activate')
        if side['reader_fuel'] >= 1:
            side['reader_fuel'] -= 1; side['decode_spent'] += 1
            side['cache_context'] = side['context']
            snapshot('sense_context')
            for address in range(3):
                if side['reader_fuel'] < 4:
                    break
                side['reader_fuel'] -= 4; side['decode_spent'] += 4
                frame = side['frames'][address]
                side['cache'][address] = None if frame is None else frame_certificate(
                    side['cells'][4*address:4*address+4], desired=DESIRED[address],
                    current=side['cache_context'], complete=frame['complete'], valid=frame['valid'])
                side['read_count'] += 1
                snapshot('read_frame')
            side['cache_valid'] = side['read_count'] == 3
    snapshot('finish')
    return dict(core=core, **side), costs, trace, history


def normalize_reference(s, costs, inflight=0):
    result = copy.deepcopy(s)
    frames = []
    for frame in result['frames']:
        if frame is None:
            frames.append(dict(bound=None, latched=None, written=0, complete=False, valid=False))
        else:
            frames.append(dict(bound=[frame['context'], frame['action']],
                               latched=frame.get('bits'), written=frame['written'],
                               complete=frame['complete'], valid=frame['valid']))
    result['frames'] = frames
    result.update(costs, packet_inflight=inflight)
    return result


def restrict_saved(s, reference):
    # Extra producer phase registers are separately audited below.
    return {k:s[k] for k in reference}


def metrics_for(s, costs, history, truth):
    r1, a1, r2, a2, r3 = history
    strict = int(r1['capture'] is False and r1['after']['last'] == 0
        and r1['after']['q'] != r1['before']['q'] and r2['capture'] is True
        and r2['after']['last'] == 1 and r3['before']['last'] == 1
        and r3['capture'] is True and a1['capture'] is True and a2['capture'] is True)
    known = sum(x is not None for x in s['cache'])
    wrong = sum(x is not None and x != (truth == DESIRED[i])
                for i, x in enumerate(s['cache']))
    complete = sum(x is not None and x['complete'] for x in s['frames'])
    recorded = int(strict and complete == 3)
    result = dict(costs, archive_spent=s['archive_spent'], decode_spent=s['decode_spent'],
        final_working=s['core']['fuel'], final_recipient=s['core']['recipient'],
        final_source=s['core']['source'], final_archive=s['archive_fuel'],
        final_reader=s['reader_fuel'], final_idle=s['idle_fuel'],
        final_archive_escrow=s['archive_escrow'], complete_frames=complete,
        written_cells=sum(x is not None for x in s['cells']),
        cache_complete=int(s['cache_valid']), known_certificates=known,
        usable_certificates=known if s['cache_valid'] and s['cache_context'] == s['context'] else 0,
        false_cache_entries=wrong, strict_core_witness=strict,
        strict_recorded_witness=recorded,
        strict_factual_witness=int(recorded and s['cache_valid'] and
            s['cache'][1] is not None and s['cache'][2] is not None and wrong == 0))
    return result


def audit_saved_microstates(path, name):
    """Check every saved physical snapshot, including phases omitted by DP."""
    count = 0
    previous = None
    for row in path['runtime_trace']:
        s, event = row['state'], row['event']
        c = s['core']
        stored = sum(c[k] for k in ('fuel', 'recipient', 'source', 'escrow'))
        stored += sum(s[k] for k in ('archive_fuel', 'reader_fuel', 'idle_fuel', 'archive_escrow', 'packet_inflight'))
        assert stored+s['core_spent']+s['core_waste']+s['archive_spent']+s['decode_spent'] == s['initial_energy']
        assert 2*s['cell_count']+2+2+s['free_a']+s['free_h'] == 28
        assert s['free_a'] == s['free_h'] == 12-s['cell_count']
        assert all(x is None for x in s['cells'][s['cell_count']:])
        assert 0 <= s['query_pointer'] <= 3
        if event == 'archive_latch_from_paid_acquisition':
            assert s['core_phase'] == 'acquired' and s['core_target'] == 'recipient'
            frame = s['frames'][s['pending']]
            receipt = s['acquired_record']
            expected = [frame['bound'][0], s['core_action'], int(receipt is not None), int(bool(receipt))]
            if name == 'corrupt_action_tag':
                expected[1] ^= 1
            assert frame['latched'] == expected
        if event == 'archive_write_bit':
            assert previous is not None and previous['pending'] is not None
            i = previous['pending']; old, new = previous['frames'][i], s['frames'][i]
            assert old['latched'] is not None and old['written'] < 4
            assert new['written'] == old['written']+1
            assert s['pending'] == (None if new['written'] == 4 else i)
            position = 4*i+old['written']
            assert previous['cells'][position] is None
            assert s['cells'][position] == new['latched'][old['written']]
            assert s['archive_escrow']+1 == previous['archive_escrow']
            assert s['archive_spent'] == previous['archive_spent']+1
            assert all(s['cells'][j] == previous['cells'][j] for j in range(12) if j != position)
            assert c == previous['core']
        if event == 'core_commit':
            assert s['core_phase'] == 'ready' and s['acquired_record'] is None
            assert s['core_target'] is None and s['core_action'] is None
        for i, frame in enumerate(s['frames']):
            assert 0 <= frame['written'] <= 4
            if frame['complete']:
                assert frame['written'] == 4 and s['cells'][4*i:4*i+4] == frame['latched']
            if previous and previous['frames'][i]['complete']:
                assert frame == previous['frames'][i]
                assert s['cells'][4*i:4*i+4] == previous['cells'][4*i:4*i+4]
        previous = s
        count += 1
    return count


def compare_trace(reference, actual):
    # Compare independently reached milestone states as an ordered subsequence;
    # producer-only snapshots are checked individually by audit_saved_microstates.
    names = {'setup':('identification_setup',), 'miss':('core_opportunity_missed',),
        'paid_sense':('core_target_sense_actor','core_target_sense_recipient'),
        'bind':('archive_bind_and_reserve',),
        'context_change':('context_change_invalidates_pending','context_change_before_decode'),
        'core_reserve':('core_reserve_feedback',), 'work':('core_work',),
        'receipt':('actual_receipt',),
        'acquire':('core_paid_acquire','archive_latch_from_paid_acquisition'),
        'core_write':('core_commit',), 'bit_write':('archive_write_bit',),
        'frame_complete':('archive_frame_complete',), 'activate':('reader_activate',),
        'sense_context':('reader_sense_context',), 'read_frame':('reader_four_cell_decode',),
        'finish':('factual_cache_complete','reader_unaffordable')}
    cursor = 0
    for row in reference:
        state = normalize_reference(dict(core=row['core'], **row['archive']), row['costs'], row['inflight'])
        while cursor < len(actual):
            candidate = actual[cursor]; cursor += 1
            if candidate['event'] in names[row['event']] and restrict_saved(candidate['state'],state) == state:
                break
        else:
            raise AssertionError(('reference microstate absent',row['event'],state))


def audit_fixture(f):
    assert f['working_reserve'] == 26 and f['prefix_packets'] == 8 and f['suffix_packets'] == 5
    previous = json.loads((HERE.parent/'fixtures.json').read_text())['fixtures']['30']
    receipt = json.loads((HERE.parent/'independent-check.json').read_text())
    assert receipt['status'] == 'passed'
    for path in (HERE.parent/'fixtures.json', HERE.parent/'model.py'):
        relative = str(path.relative_to(ROOT))
        assert sha256(path.read_bytes()).hexdigest() == receipt['source_hashes'][relative]
    commissioned = [p for p in previous['preparations'] if p['commissioned']]
    assert len(commissioned) == 1 and commissioned[0]['state'] == [0,1,1,1,1,26,130]
    assert commissioned[0]['reserve'] == 26
    for size, prep in f['preparations'].items():
        ref = formation_reference(int(size))
        assert prep['construction_spent'] == ref['spent']
        assert (prep['fuel'],prep['source']) == (ref['state'][5],ref['state'][6])
        assert prep['free_a'] == prep['free_h'] == ref['free_pairs']
        assert prep['trace'][0]['plant'] == [0,0,0,0,0,91,144]
        for expected, actual in zip(ref['trace'], prep['trace'][1:45]):
            assert expected['event'] == actual['event'] and expected['state'] == actual['plant']
            assert expected['spent'] == actual['spent']
        a,h,fuel=13,14,74
        for index, row in enumerate(prep['trace'][45:-1]):
            a-=1;h-=1;fuel-=1
            assert row['plant']==[a,h,1,1,1,fuel,130]
            assert row['bound_parts']==2*(index+1) and row['spent']==31+index
            assert a+h+1+row['bound_parts']==28
        assert len(prep['trace'])==47+int(size)
        last=prep['trace'][-1]
        assert last['event']=='existing_adapter' and last['controller_parts']==last['reader_parts']==2
        assert last['cell_parts']==2*int(size) and last['spent']==ref['spent']
    for name, route in f['routes'].items():
        p=case_parameters(name)
        assert (route['working'],route['archive'],route['reader'],route['source'])==(
            26,p['archive'],p['reader'],130)
        assert route['before_common']==61+12-p['cell_count']
        assert route['idle']==35-p['archive']-p['reader']+12-p['cell_count']
        assert route['working']+route['archive']+route['reader']+route['idle']==route['before_common']
    for producer, rows in f['prefix_records'].items():
        assert rows == previous['prefix_records'][producer]['26']
        assert sum(Q(r['probability']) for r in rows) == 1
        for r in rows:
            assert r['state']['fuel']+Q(r['conditional_mean_marks']['spent'])+Q(r['conditional_mean_marks']['waste']) == 106


def compare_all(f, results):
    summary = dict(comparison_arms=0, prefix_cases=0, distinct_histories=0,
                   microstates_checked=0, metric_comparisons=0)
    core_distributions = {}
    for name, case in results.items():
        params = case_parameters(name)
        law = case['law']
        assert (law['archive_budget'],law['reader_budget'],law['cell_count'],law['channel'],Q(law['availability'])) == (
            params['archive'],params['reader'],params['cell_count'],params['channel'],params['availability'])
        for producer, saved in case['producers'].items():
            totals, dist, core_dist = defaultdict(Q), defaultdict(Q), defaultdict(Q)
            totals['construction_spent'] = Q(44-(12-params['cell_count']))
            rows = f['prefix_records'][producer]
            saved_paths = defaultdict(list)
            for path in saved['paths']:
                saved_paths[path['prefix_id']].append(path)
            for prefix_id, row in enumerate(rows):
                prefix_mass = Q(row['probability'])
                totals['prefix_spent'] += prefix_mass*Q(row['conditional_mean_marks']['spent'])
                totals['prefix_waste'] += prefix_mass*Q(row['conditional_mean_marks']['waste'])
                histories = {}
                for word in product((0,1),repeat=3):
                    beta=params['availability']; weight=beta**sum(word)*(1-beta)**(3-sum(word))
                    if not weight:
                        continue
                    state,costs,trace,history=run_word(name,row['state'],row['final_regime'],word)
                    normalized=normalize_reference(state,costs)
                    signature=key([normalized,history])
                    if signature not in histories:
                        histories[signature]=[Q(0),state,costs,trace,history]
                    histories[signature][0]+=weight
                assert sum(x[0] for x in histories.values()) == 1
                actual_by_signature={}
                for path in saved_paths[prefix_id]:
                    # Compare all declared archive/core fields, allowing extra
                    # explicit runtime phase registers that are separately audited.
                    fields=normalize_reference(next(iter(histories.values()))[1],next(iter(histories.values()))[2])
                    signature=key([restrict_saved(path['state'],fields),path['core_history']])
                    assert signature not in actual_by_signature
                    actual_by_signature[signature]=path
                assert set(histories) == set(actual_by_signature), (name,producer,prefix_id,'history signatures')
                for signature,(weight,state,costs,trace,history) in histories.items():
                    path=actual_by_signature[signature]
                    assert Q(path['conditional_probability']) == weight
                    assert Q(path['probability']) == prefix_mass*weight
                    metrics=metrics_for(state,costs,history,1-row['final_regime'])
                    assert metrics == path['metrics'], (name,producer,prefix_id,'metrics',metrics,path['metrics'])
                    try:
                        compare_trace(trace,path['runtime_trace'])
                    except AssertionError as error:
                        raise AssertionError((name,producer,prefix_id,signature[:100])) from error
                    summary['microstates_checked']+=audit_saved_microstates(path,name)
                    for k,v in metrics.items():totals[k]+=prefix_mass*weight*v
                    dist[key(path['state'])]+=prefix_mass*weight
                    core_dist[key(state['core'])]+=prefix_mass*weight
                summary['prefix_cases']+=1;summary['distinct_histories']+=len(histories)
            assert dict(totals)=={k:Q(v) for k,v in saved['metrics'].items()},(name,producer,'aggregate metrics')
            assert dict(dist)=={key(r['state']):Q(r['probability']) for r in saved['distribution']}
            assert sum(totals[k] for k in ('construction_spent','prefix_spent','prefix_waste',
                'core_spent','core_waste','archive_spent','decode_spent','final_working',
                'final_recipient','final_source','final_archive','final_reader','final_idle','final_archive_escrow'))==235
            core_distributions[name,producer]=dict(core_dist)
            summary['comparison_arms']+=1;summary['metric_comparisons']+=len(totals)
    for producer in f['prefix_records']:
        for name in results:
            if name not in ('missing_channel','no_opportunity','actor_charged'):
                assert core_distributions[name,producer]==core_distributions['primary',producer]
    return summary


def audit_receipts(manifest):
    producer=json.loads((HERE/'check.json').read_text())
    assert producer['status']=='passed'
    assert producer['checker_sha256']==sha256((HERE/'check.py').read_bytes()).hexdigest()
    for name,digest in producer['data_sha256'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest()==digest
    for relative,digest in producer['source_sha256'].items():
        assert sha256((ROOT/relative).read_bytes()).hexdigest()==digest
    folder=HERE/'formal'
    formal=json.loads((folder/'verification.json').read_text())
    assert formal['status']=='passed' and formal['source_unchanged_during_check']
    assert formal['fresh_temporary_build'] and formal['project_objects_only_from_frozen_sources']
    assert formal['checker_sha256']==sha256((folder/'check.py').read_bytes()).hexdigest()
    assert formal['toolchain_sha256']==sha256((folder/'lean-toolchain').read_bytes()).hexdigest()
    assert formal['compiler_sha256']==sha256(Path(formal['compiler_binary']).read_bytes()).hexdigest()
    new=old=0;axioms=set()
    for module in formal['modules']:
        source=ROOT/module['source'];output=folder/module['output']
        assert module['exit_code']==0 and module['clean_dependency_audit']
        assert sha256(source.read_bytes()).hexdigest()==module['source_sha256']
        assert sha256(output.read_bytes()).hexdigest()==module['output_sha256']
        text=source.read_text();log=output.read_text()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b',text)
        assert 'sorryAx' not in log and 'warning:' not in log
        audited=re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[[^\]]*\])",log)
        assert audited==module['audited_declarations']
        assert len(audited)==module['dependency_audits']
        if module['role']=='new formalization':
            names=set(re.findall(r'^theorem\s+(\w+)',text,re.M))
            assert names=={x.rsplit('.',1)[-1] for x in audited}
            new+=len(audited)
        else:old+=len(audited)
        axioms.update(module['axioms'])
        for path in (source,output):manifest[str(path.relative_to(ROOT))]=sha256(path.read_bytes()).hexdigest()
    assert new==formal['new_audited_declarations']==67 and old==142
    assert axioms <= {'propext','Quot.sound','Classical.choice'}
    for name in ('verification.json','check.py','lean-toolchain','README.md'):
        path=folder/name
        if path.exists():manifest[str(path.relative_to(ROOT))]=sha256(path.read_bytes()).hexdigest()
    math=ROOT/'_process/research/2026-10-05-concern-theory/RECIPIENT-RECORDING-MATH.md'
    if math.exists():manifest[str(math.relative_to(ROOT))]=sha256(math.read_bytes()).hexdigest()
    return dict(status='passed',new_declaration_audits=new,inherited_declaration_audits=old,
                axioms=sorted(axioms),compiler_hash_verified=True,
                source_checker_toolchain_and_log_hashes_verified=True,
                scope='Inspection of frozen fresh-build receipt and sources; no independent Lean rerun or Python refinement claim.')


def main():
    fixture_doc=json.loads((HERE/'fixtures.json').read_text())
    result_doc=json.loads((HERE/'results.json').read_text())
    assert fixture_doc['source_sha256']==result_doc['source_sha256']
    manifest=dict(result_doc['source_sha256'])
    for relative,digest in manifest.items():
        assert sha256((ROOT/relative).read_bytes()).hexdigest()==digest,relative
    audit_fixture(fixture_doc['fixtures'])
    local=local_contract_checks()
    summary=compare_all(fixture_doc['fixtures'],result_doc['cases'])
    formal=audit_receipts(manifest)
    for relative,digest in manifest.items():
        assert sha256((ROOT/relative).read_bytes()).hexdigest()==digest,('changed during run',relative)
    files=[HERE/'independent_check.py',HERE/'fixtures.json',HERE/'results.json',HERE/'PROTOCOL.md',
           HERE.parent/'fixtures.json',HERE.parent/'independent-check.json']
    files += [p for p in (HERE/'check.py',HERE/'check.json',HERE/'README.md') if p.exists()]
    for path in files:manifest[str(path.relative_to(ROOT))]=sha256(path.read_bytes()).hexdigest()
    record=dict(status='passed',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        method='No producer imports; independent formation guards and exogenous-word physical replay; exact rational comparison.',
        scope='Conditional on the specified actual construction. Inherited prefix rows are hash-bound and compared to the accepted fixture; no new preparation probability or full Lean/Python refinement claim.',
        summary=summary,local_contract_checks=local,source_sha256=manifest)
    record['formal_receipt_inspection']=formal
    (HERE/'independent-check.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,sort_keys=True))


if __name__=='__main__':main()
