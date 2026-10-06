#!/usr/bin/env python3
"""Independent finite replay of inquiry revision and its native continuations.

No producer transition function is used. The accepted ancestral initial overlay,
catalog and unchanged physical correspondence are read from the original result.
This is not an independent reconstruction of that earlier ancestral formation.
Native paired encounters, additive operations, assessment and the admitted
positive service are reimplemented below from their declared event laws.
"""
from copy import deepcopy
from pathlib import Path
from itertools import product
import datetime
import gzip
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
REF = 'primary/variable/11/37'
NEW_COSTS = ('inquiry_assembly', 'inquiry_read', 'inquiry_commit')
COUNTS = dict(states=0, event_comparisons=0, traces=0)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def retained(s):
    return (s['accounting']['parent_fixed_retained']
            + sum(s['core'][k] for k in ('fuel', 'recipient', 'source', 'escrow'))
            + sum(s['reserves'].values())
            + sum(sum(v) for v in s['packets'].values()))


def material(s):
    inv = s['inventory']
    free = sum(inv['free_primary']) + int(inv['replacement_free'])
    held = len(s['retired']) + sum(x is not None for x in s['links'])
    installed = inv['memory_cells'] + int(inv['adapter']) + int(s['port']['built'])
    return 42 + 2 * (free + held + installed + inv['omitted_pairs']
                     + int(s['inquiry']['mode'] != 'absent'))


def record(s, name, trace):
    c = s['core']
    assert 0 <= s['native']['n'] <= 7 and 0 <= s['native']['count'] <= 6
    stocks = [c[k] for k in ('fuel', 'recipient', 'source', 'escrow')]
    stocks += list(s['reserves'].values()) + sum(list(s['packets'].values()), [])
    assert min(stocks + list(s['costs'].values()) + [s['waste']]) >= 0
    assert material(s) == 68
    assert retained(s) + sum(s['costs'].values()) + s['waste'] == 118
    assert 351 + 36 + retained(s) + sum(s['costs'].values()) + s['waste'] == 505
    assert len({x['id'] for x in s['links'] if x is not None} |
               {x['id'] for x in s['retired']}) == sum(x is not None for x in s['links']) + len(s['retired'])
    for cell in s['native']['latches'].values():
        assert type(cell['value']) is bool
        if cell['mode'] in ('empty', 'missing'):
            assert cell['value'] is False
    trace.append({'event': name, 'state': deepcopy(s)})
    COUNTS['states'] += 1


def spend(s, bill, amount=1):
    assert s['core']['fuel'] >= amount
    s['core']['fuel'] -= amount
    s['costs'][bill] += amount


def clear(s):
    for cell in s['native']['latches'].values():
        cell['value'], cell['mode'] = False, 'empty'


def release(s):
    if s['inquiry']['mode'] in ('observed', 'missing', 'stale'):
        clear(s)
        s['inquiry']['mode'] = 'idle'


def correspondence(s, catalog):
    """Decode actual publication/context without calling ancestor helpers."""
    p = catalog[s['parent_ref']]['state']
    workspace = p['parent']['parent']
    producer = workspace['producer']
    pub = workspace['publication']
    epoch = p['fresh']['epoch'] if p['selected_bank'] == 'fresh' else producer['context']
    valid = (p['opened'] and p['selected_bank'] == 'fresh' and p['current_new_reason']
             and producer['cache_valid'] and producer['read_count'] == 3
             and producer['cache_context'] == epoch and workspace['publication_current']
             and workspace['phase'] == 'published' and pub and pub['context'] == epoch)
    command = {(True, True, False): 0, (True, False, True): 1}.get(tuple(pub['mask'])) if valid else None
    admitted = bool(valid and s['binding']['scope'] and s['core']['active']
                    and s['physical']['core_phase'] == 'ready'
                    and s['inventory']['memory_cells'] == 8 and s['inventory']['adapter'])
    known = bool(valid and s['binding']['scope'] and command is not None
                 and command == ((s['core']['q'] >> 1) & 1))
    return admitted, known, command


def native_pair(s, own_loss, affected_loss, trace):
    n, c, inv = s['native'], s['core'], s['inventory']
    j = n['count']
    assert n['phase'] == 'ready' and j < s['controls']['training_limit']
    bank = 'primary' if j < 4 else 'revision'
    grant = min(s['reserves'][bank], 6 if j < 4 else 7 if j == 4 else 5)
    if min(s['packets']['own'][j], s['packets']['recipient'][j], c['recipient'], c['fuel']+grant) < 2:
        record(s, 'pair.prebacking_blocked', trace)
        return False
    s['reserves'][bank] -= grant
    c['fuel'] += grant
    spend(s, 'own_operation', 2)
    n['phase'] = 'own_paid'
    record(s, 'own.pay', trace)
    for target, loss in (('own', own_loss), ('recipient', affected_loss)):
        if target == 'recipient':
            c['recipient'] -= 2
            s['costs']['recipient_operation'] += 2
            n['phase'] = 'recipient_paid'
            record(s, 'recipient.pay', trace)
        if not loss:
            s['packets'][target][j] -= 2
            c['fuel' if target == 'own' else 'recipient'] += 2
        n['latches'][target].update(value=not bool(loss), mode='return')
        n['phase'] = target + '_returned'
        record(s, target + ('.no_return' if loss else '.return'), trace)
    for target in ('own', 'recipient'):
        if c['fuel'] < 1:
            record(s, target + '.read_blocked', trace)
            return False
        spend(s, target + '_read')
        cell = n['latches'][target]
        cell.update(value=not cell['value'], mode='shortfall')
        n['phase'] = target + '_acquired'
        record(s, target + '.read_shortfall', trace)
    if not affected_loss:
        n['phase'] = 'coupling_settled'
        record(s, 'coupling.no_contact', trace)
    else:
        sign = 1 if own_loss else -1
        if s['controls']['link_recipe'] == 'inert':
            sign = 0
        empty = next((i for i, x in enumerate(s['links']) if x is None), None)
        if empty is not None:
            if not (inv['free_primary'][empty] and inv['primary_access'][empty] and c['fuel'] >= 1):
                record(s, 'coupling.bind_blocked', trace)
                return False
            spend(s, 'coupling')
            inv['free_primary'][empty] = False
            s['links'][empty] = {'id': empty, 'sign': sign}
            event = 'coupling.bind'
        else:
            if not (j >= 4 and s['controls']['training_limit'] == 6 and inv['replacement_free']
                    and inv['replacement_access'] and c['fuel'] >= 2):
                record(s, 'coupling.replace_blocked', trace)
                return False
            pos = min(range(2), key=lambda i: s['links'][i]['id'])
            prior = s['links'][pos]
            if s['controls']['replacement_rule'] == 'retired_sign':
                sign = prior['sign']
            spend(s, 'coupling', 2)
            inv['replacement_free'] = False
            s['retired'].append(deepcopy(prior))
            s['links'][pos] = {'id': 2, 'sign': sign}
            s['outcomes']['replacements'] += 1
            event = 'coupling.replace'
        n['phase'] = 'coupling_settled'
        record(s, event, trace)
    if c['fuel'] < 1:
        record(s, 'native.write_blocked', trace)
        return False
    spend(s, 'native_write')
    if s['controls']['native_updates']:
        n['n'] = n['n']//2 + 4*int(n['latches']['own']['value'])
    n['count'] += 1
    n['phase'] = 'ready'
    clear(s)
    record(s, 'native.write', trace)
    return True


def allowed(s, event, catalog):
    admitted, known, _ = correspondence(s, catalog)
    n = s['native']
    base = (admitted and known and s['binding']['permission'] and not s['retired']
            and n['count'] == 4 and n['phase'] == 'ready'
            and s['controls']['training_limit'] == 6 and s['core']['fuel'] >= 1)
    mode = s['inquiry']['mode']
    if event == 'assemble':
        return bool(base and mode == 'absent' and s['inventory']['replacement_free'])
    if event.startswith('inspect:'):
        return bool(base and mode in ('idle', 'missing', 'stale'))
    return bool(base and mode == 'observed' and all(v['value'] for v in n['latches'].values()))


def inquiry(s, event, catalog, trace):
    if not allowed(s, event, catalog):
        record(s, 'inquiry.'+event+'.blocked', trace)
        return False
    if event == 'assemble':
        spend(s, 'inquiry_assembly')
        s['inventory']['replacement_free'] = False
        s['inquiry']['mode'] = 'idle'
    elif event.startswith('inspect:'):
        spend(s, 'inquiry_read')
        channel = event.partition(':')[2]
        count = sum(x is not None for x in s['links'])
        if channel == 'faithful':
            bits, mode = (count > 0, count > 1), 'observed'
        elif channel == 'falsePositive':
            bits, mode = (True, True), 'observed'
        elif channel in ('zero', 'missing', 'wrongBinding'):
            bits, mode = (False, False), {'zero':'observed','missing':'missing','wrongBinding':'stale'}[channel]
        else:
            raise AssertionError(channel)
        for key, bit in zip(('own', 'recipient'), bits):
            s['native']['latches'][key].update(value=bit, mode='occupancy')
        s['inquiry']['mode'] = mode
    else:
        assert event in ('commit', 'shamCommit')
        spend(s, 'inquiry_commit')
        clear(s)
        s['inquiry']['mode'] = 'committed' if event == 'commit' else 'idle'
        if event == 'commit':
            s['controls']['training_limit'] = 4
    record(s, 'inquiry.'+event, trace)
    return True


def cut(s, kind, value, trace):
    release(s)
    s['binding'][kind] = value
    s['port']['read_command'] = None
    if s['port']['mode'] != 'idle':
        s['port']['mode'] = 'consumed'
    record(s, 'inherited.'+kind+':'+str(value).lower(), trace)


def response(s, catalog, trace):
    n, c, port, physical = s['native'], s['core'], s['port'], s['physical']
    if not (n['phase'] == 'ready' and n['count'] == s['controls']['training_limit']
            and s['inventory']['memory_cells'] == 8 and port['built'] and port['mode'] == 'idle'
            and physical['core_phase'] == 'ready' and c['fuel'] >= 1):
        record(s, 'evaluation.read_blocked', trace)
        return
    release(s)
    spend(s, 'evaluation_read')
    _, known, command = correspondence(s, catalog)
    port.update(mode='read' if known else 'consumed', read_command=command if known else None)
    record(s, 'evaluation.read', trace)
    if not known or c['fuel'] < 1:
        record(s, 'evaluation.assessment_blocked', trace)
        return
    raw = n['n'] * sum(x['sign'] for x in s['links'] if x is not None)
    transmission = 0 if s['controls']['recipient_filter'] else raw
    decision = transmission*10 > 64
    spend(s, 'assessment')
    port['mode'] = 'assessed_help' if decision else 'assessed_abstain'
    s['outcomes'].update(assessment=decision, raw_transmission=raw, transmission=transmission)
    record(s, 'evaluation.assess', trace)
    if not decision:
        port['mode'] = 'consumed'
        record(s, 'evaluation.abstain', trace)
        return
    s['outcomes']['attempted'] = True
    if not (all(s['binding'].values()) and known and physical['core_phase'] == 'ready'):
        port['mode'] = 'consumed'
        record(s, 'service.guard_blocked', trace)
        return
    port['mode'] = 'executing'
    record(s, 'service.initiate', trace)
    if c['source'] < 10:
        port['mode'] = 'consumed'
        record(s, 'service.source_blocked', trace)
        return
    if not c['active'] or c['fuel'] < 8:
        c['source'] -= 10
        c['active'] = False
        s['waste'] += 10
        port['mode'] = 'consumed'
        record(s, 'service.miss', trace)
        return
    spend(s, 'service'); physical['core_phase'] = 'rented'
    record(s, 'service.rent', trace)
    spend(s, 'service'); physical.update(core_phase='sensed',core_target='recipient')
    record(s, 'service.sense', trace)
    c['fuel'] -= 3; c['escrow'] = 3; physical['core_phase'] = 'reserved'
    record(s, 'service.reserve', trace)
    action = (c['q'] >> 1) & 1
    capture = action == catalog[s['parent_ref']]['observer']['final_law']
    spend(s, 'service', 3); c['source'] -= 10
    physical.update(core_phase='worked',core_action=action)
    if capture:
        c['recipient'] += 10
    else:
        s['waste'] += 10
    s['outcomes']['captured'] = capture
    record(s, 'service.work', trace)
    c['escrow'] -= 1; s['costs']['service'] += 1
    physical.update(core_phase='acquired',acquired_record=capture)
    record(s, 'service.acquire', trace)
    # All saved admitted services have this unchanged acquired correspondence.
    # The broader negative-efficacy update law is not claimed reconstructed.
    assert capture and c['last'] == 1
    c['escrow'] -= 2; s['costs']['service'] += 2
    physical.update(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
    port['mode'] = 'consumed'; s['outcomes']['completed'] = True
    record(s, 'service.write', trace)


def summary(s):
    return dict(n=s['native']['n'], count=s['native']['count'], fuel=s['core']['fuel'],
                affected=s['core']['recipient'], energy=retained(s), material=material(s),
                limit=s['controls']['training_limit'], mode=s['inquiry']['mode'],
                occupied=sum(x is not None for x in s['links']),
                signs=[None if x is None else x['sign'] for x in s['links']],
                service=s['outcomes']['completed'], captured=s['outcomes']['captured'],
                assessment=s['outcomes']['assessment'], costs=deepcopy(s['costs']))


def start(initial, own, affected):
    s = deepcopy(initial); trace = []
    record(s, 'extension.at_actual_parent_prefix', trace)
    complete = True
    for y, x in zip(own, affected):
        if not native_pair(s, y, x, trace):
            complete = False
            break
    return s, trace, complete


def compare(expected, actual, label):
    assert len(expected) == len(actual), (label, 'trace length', len(expected), len(actual))
    for i, (a, b) in enumerate(zip(expected, actual)):
        if a != b:
            differences = [k for k in a['state'] if a['state'][k] != b['state'][k]]
            raise AssertionError((label, i, a['event'], b['event'], differences))
    COUNTS['event_comparisons'] += len(actual)
    COUNTS['traces'] += 1


def main():
    paths = [HERE/'model.py',HERE/'PROTOCOL.md',HERE/'results.json.gz',HERE/'reporting.json',
             BASE/'model.py',BASE/'results.json.gz',BASE/'cases.json',
             BASE/'formal/PairedPlasticity.lean',BASE/'formal/PlasticityWitness.lean',Path(__file__)]
    before = {str(p.relative_to(REPO)):sha(p) for p in paths}
    output = read(HERE/'results.json.gz'); ancestor = read(BASE/'results.json.gz')
    for name, digest in output['source_sha256'].items():
        assert sha(REPO/name) == digest, name
        before[name] = digest
    catalog = ancestor['parent_catalog']
    actual = next(r for r in ancestor['cases']['aligned_revision']['variants']['active']['producers']['variable']['paths']
                  if r['predecessor_ref'] == REF)
    initial = deepcopy(actual['runtime_trace'][0]['state'])
    initial['inquiry'] = {'mode':'absent'}
    initial['costs'].update({k:0 for k in NEW_COSTS})
    assert initial['core'] == catalog[REF]['state']['parent']['parent']['producer']['core']
    assert initial['controls']['training_limit'] == 6
    faithful_prefix, prefix_trace, _ = start(initial,(1,0,0,1),(1,0,0,1))
    for a,b in zip(actual['runtime_trace'][:33],prefix_trace):
        projected = deepcopy(b['state']); del projected['inquiry']
        for k in NEW_COSTS: del projected['costs'][k]
        assert a == {'event':b['event'],'state':projected}
    assert len(prefix_trace) == 33
    for name, h in output['histories'].items():
        s, tr, complete = start(initial,h['own'],h['affected'])
        assert complete and h['entry_index'] == len(tr)-1
        mutation = h['mutation']
        if mutation == 'no_part':
            s['inventory']['replacement_free'] = False; s['inventory']['omitted_pairs'] += 1
            record(s, 'fixture.withheld_spare_pair', tr)
        elif mutation:
            amount = int(mutation.split(':')[1]); assert 0 <= amount <= s['core']['fuel']
            s['reserves']['idle_common'] += s['core']['fuel']-amount; s['core']['fuel'] = amount
            record(s, 'fixture.withheld_fuel', tr)
        cut_kind = h['cut']
        if cut_kind in ('before_scope','before_permission'):
            cut(s,cut_kind[7:],False,tr)
        inquiry(s,'assemble',catalog,tr)
        if not h['omit_read']:
            inquiry(s,'inspect:'+h['channel'],catalog,tr)
        if cut_kind in ('scope','permission','delivery','noop','restore'):
            kind = cut_kind if cut_kind in ('scope','permission','delivery') else 'scope'
            cut(s,kind,cut_kind == 'noop',tr)
            if cut_kind == 'restore': cut(s,'scope',True,tr)
            if h['reacquire']: inquiry(s,'inspect:faithful',catalog,tr)
        if h.get('extra_inquiry'):
            if h['sham']: inquiry(s,'shamCommit',catalog,tr)
            release(s)
            assert not native_pair(s,False,True,tr)
            inquiry(s,'commit',catalog,tr)
        else:
            inquiry(s,'shamCommit' if h['sham'] else 'commit',catalog,tr)
        response(s,catalog,tr)
        compare(h['trace'],tr,name)
        assert h['result'] == summary(s), name
    complete_count = revisions = 0
    expected_pairs = set(product(product((0,1),repeat=4),repeat=2))
    seen = set()
    for item in output['enumeration']:
        pair = (tuple(item['own']),tuple(item['affected'])); assert pair not in seen; seen.add(pair)
        s,tr,complete = start(initial,*pair)
        assert item['complete'] == complete and item['before'] == summary(s)
        did = False
        if complete:
            complete_count += 1
            assert s['core']['recipient'] + 2*sum(x is not None for x in s['links']) == 40
            inquiry(s,'assemble',catalog,tr); inquiry(s,'inspect:faithful',catalog,tr)
            did = inquiry(s,'commit',catalog,tr)
            response(s,catalog,tr)
        assert item['revised'] == did and item['after'] == summary(s)
        revisions += did
        compare(item['trace'],tr,str(pair))
    assert seen == expected_pairs and (complete_count,revisions) == (176,96)
    h = output['histories']
    assert h['faithful']['result']['fuel'] == 1 and h['faithful']['result']['affected'] == 46
    assert h['faithful']['result']['mode'] == 'committed'
    for name in ('opposed','mixed'):
        assert h[name]['result']['limit'] == 4 and h[name]['result']['assessment'] is False
    for name in ('zero_history','one_history','missing','zero','wrongBinding','sham','omitted_read','no_part'):
        assert h[name]['result']['limit'] == 6 and not h[name]['result']['service']
    assert h['false_positive_zero_history']['result']['limit'] == 4
    assert not h['false_positive_zero_history']['result']['occupied']
    assert h['reacquired']['result']['costs']['inquiry_read'] == 2
    assert h['fuel_12']['trace'][-1]['event'] == 'service.miss'
    for name in ('interleaved_inquiry','sham_then_inquiry'):
        assert h[name]['result']['affected'] == 34 and h[name]['result']['limit'] == 6
        assert any(r['event'] == 'coupling.replace_blocked' for r in h[name]['trace'])
    # Differential guard/step checks use the producer only as the implementation
    # under test, never to compute a reference successor or the saved replay.
    spec = importlib.util.spec_from_file_location('_inquiry_producer_under_test', HERE/'model.py')
    producer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = producer
    spec.loader.exec_module(producer)
    reachable = {}
    for group in (list(h.values()), output['enumeration']):
        for history in group:
            for row in history['trace']:
                s = row['state']
                if s['native']['count'] == 4:
                    reachable[json.dumps(s,sort_keys=True)] = s
    operations = ('assemble','inspect:faithful','inspect:missing','inspect:zero',
                  'inspect:falsePositive','inspect:wrongBinding','commit','shamCommit')
    differential = 0
    for source in reachable.values():
        for event in operations:
            assert producer.enabled(source,event,catalog) == allowed(source,event,catalog)
            ours, theirs = deepcopy(source), deepcopy(source)
            ot, tt = [], []
            a = inquiry(ours,event,catalog,ot)
            b = producer.step(theirs,event,catalog,tt)
            assert a == b and ours == theirs and ot == tt, ('differential',event)
            differential += 1
    # Precisely funded primary route requires three revision units plus the
    # inherited two-unit assessment and eight-unit executed service.
    liquidity = []
    for fuel in range(15):
        s = deepcopy(faithful_prefix)
        s['reserves']['idle_common'] += s['core']['fuel']-fuel
        s['core']['fuel'] = fuel
        tr = []
        for event in ('assemble','inspect:faithful','commit'):
            inquiry(s,event,catalog,tr)
        response(s,catalog,tr)
        assert s['outcomes']['completed'] == (fuel >= 13)
        assert s['outcomes']['captured'] == (fuel >= 13)
        liquidity.append(dict(initial_fuel=fuel,terminal=summary(s)))
    # Guard boundaries on independently reached acquired evidence: no event is
    # permitted by a hidden truth check; technical binding/means still matters.
    observed = deepcopy(h['faithful']['trace'][34]['state'])
    assert allowed(observed,'commit',catalog)
    guard_probes = 0
    for key in ('fuel','n','count','phase','limit','scope','permission','active','q','retired','mode'):
        t = deepcopy(observed)
        if key == 'fuel': t['core']['fuel']=0
        elif key == 'n': t['native']['n']=0
        elif key == 'count': t['native']['count']=5
        elif key == 'phase': t['native']['phase']='recipient_paid'
        elif key == 'limit': t['controls']['training_limit']=4
        elif key in ('scope','permission'): t['binding'][key]=False
        elif key == 'active': t['core']['active']=False
        elif key == 'q': t['core']['q'] ^= 2
        elif key == 'retired': t['retired']=[{'id':99,'sign':1}]
        else: t['inquiry']['mode']='idle'
        assert allowed(t,'commit',catalog) == (key == 'n'), key
        assert producer.enabled(t,'commit',catalog) == allowed(t,'commit',catalog)
        guard_probes += 1
    for change in ('publication_context','cache_context','publication_mask'):
        changed = deepcopy(catalog)
        parent = changed[REF]['state']; workspace = parent['parent']['parent']
        if change == 'publication_context': workspace['publication']['context'] += 1
        elif change == 'cache_context': workspace['producer']['cache_context'] += 1
        else: workspace['publication']['mask'] = [True,False,True]
        assert not allowed(observed,'commit',changed)
        assert not producer.enabled(observed,'commit',changed)
        guard_probes += 1
    # Mutation detection: equality/conservation checks reject substantive bad
    # saved continuations; these are validator tests, not producer reruns.
    mutations = {}
    original = h['faithful']['trace']
    for kind in ('unpaid_commit','unchanged_limit','recipient_reset','absent_evidence','wrong_sign'):
        damaged = deepcopy(original)
        s = damaged[35]['state']
        if kind == 'unpaid_commit': s['core']['fuel'] += 1; s['costs']['inquiry_commit'] -= 1
        elif kind == 'unchanged_limit': s['controls']['training_limit']=6
        elif kind == 'recipient_reset': s['core']['recipient']=40
        elif kind == 'absent_evidence': damaged[34]['state']['native']['latches']['recipient']['value']=False
        else: s['links'][0]['sign']=-1
        try:
            compare(original,damaged,kind)
        except AssertionError:
            mutations[kind]='detected'
        else:
            raise AssertionError(('mutation escaped',kind))
    assert before == {name:sha(REPO/name) for name in before}
    report = dict(status='accepted_independent_finite_replay',
                  scope='Independent new operations, native paired prefix and admitted positive services; trusted saved ancestral initial overlay/catalog, not full ancestry reconstruction.',
                  source_sha256=before, histories=len(h), schedules=len(seen), completed=complete_count,
                  blocked=len(seen)-complete_count, revised=revisions, inherited_prefix_states=33,
                  guard_probes=guard_probes, differential_step_checks=differential,
                  reached_guard_states=len(reachable), liquidity=liquidity,
                  mutation_checks=mutations, counts=COUNTS,
                  primary=h['faithful']['result'], scientific_scope='No ethical or empirical certification; no second Lean build.')
    (HERE/'independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('source_sha256','primary','liquidity')}))


if __name__ == '__main__':
    main()
