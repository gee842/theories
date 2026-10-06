"""Independent current-family semantics, inheritance and charged-prefix checks."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json

import revision as implementation

HERE = Path(__file__).resolve().parent


def generate(model):
    """Reconstruct the supplied graph insertion without calling stutter."""
    start = model['initial']
    order, current = [], start
    while current not in order:
        order.append(current)
        current = model['transitions'][current][0]
    assert len(order) == 3 and current == start
    assert [model['outputs'][q] for q in order] == [0, 0, 1]
    fresh = len(model['outputs'])
    expanded_order = order[:2]+[fresh]+order[2:]
    successors = [None]*(fresh+1)
    for q, target in zip(expanded_order, expanded_order[1:]+expanded_order[:1]):
        successors[q] = (target,)
    return {'alphabet': ('a',), 'outputs': tuple(model['outputs'])+(0,),
            'transitions': tuple(successors), 'initial': start}


def machine(record):
    return implementation.Machine(**record)


def handoffs():
    a = implementation.access.acquisition
    original = a.Machine(('a',), (0, 0, 1), ((1,), (2,), (0,)))
    account = a.Meter(36)
    port = a.TargetPort(original, account)
    learner = a.Learner(original.alphabet, 3, port.query, account)
    learner.run()
    use = port.use(learner.plan_novel_use(), 20)
    assert Q(use['fuel_after_return']) == Q(1030367, 65536) and use['source'] == 10
    H = learner.machine
    four = a.Machine(('a',), (0, 0, 0, 1), ((1,), (2,), (3,), (0,)))
    prior = {}
    for name, kwargs in {'probe': {'sensor_flip': 1},
                         'sensing': {'sensor_flip': 1, 'probe': False},
                         'old_four': {'environment_model': four}}.items():
        result = implementation.access.diagnose(H, Q(use['fuel_after_return']),
                                                use['source'], port.state, **kwargs)
        assert result['retained'] and result['status'] == 'complete'
        prior[name] = result
    assert [(prior[k]['fuel'], prior[k]['events'][-1]['live'], prior[k]['source_remaining'])
            for k in ('probe', 'sensing', 'old_four')] == [
                ('187921/16384', 25, 0), ('88177/32768', 27, 10), ('52327/65536', 25, 0)]
    return H, prior, four


def all_candidates(models):
    return {(k, parity, q) for k, m in enumerate(models)
            for parity in (0, 1) for q in range(len(m['outputs']))}


def update(models, candidates, command, observation):
    result = set()
    for k, parity, q in candidates:
        m = models[k]
        nextq = m['transitions'][q][0] if command == 'a' else q
        expected = m['outputs'][q]^parity if command == 'read' else None
        if expected == observation:
            result.add((k, parity, nextq))
    return result


def encoded(candidates):
    return sorted((2*k+p, q) for k, p, q in candidates)


def reference(H, environment, phase, parity, max_reads=6, switch_after=None):
    models = (H, generate(H))
    candidates = all_candidates(models)
    trace, history = [], []

    def native(command):
        nonlocal phase, parity
        if switch_after is not None and len(trace) == switch_after:
            parity ^= 1
        output = None
        if command == 'a':
            phase = environment['transitions'][phase][0]
        else:
            output = environment['outputs'][phase]^parity
        trace.append({'command': command, 'observation': output})
        return output

    def step(command):
        nonlocal candidates
        observed = native(command)
        candidates = update(models, candidates, command, observed)
        history.append({'command': command, 'observation': observed,
                        'survivors': [list(x) for x in encoded(candidates)]})

    selected, use = None, None
    status = 'current_family_unresolved'
    for i in range(max_reads):
        step('read')
        if not candidates:
            status = 'model_family_inadequate'
            break
        if len(candidates) == 1:
            k, p, q = next(iter(candidates))
            nextq = models[k]['transitions'][q][0]
            prediction = models[k]['outputs'][nextq]^p
            native('a')
            observed = native('read')
            selected = {'machine': models[k], 'family': k, 'parity': p, 'state': nextq}
            use = {'expected': prediction, 'observed': observed}
            status = 'complete' if observed == prediction else 'use_prediction_mismatch'
            break
        if i+1 < max_reads:
            step('a')
    return {'history': history, 'native_trace': trace, 'selected': selected,
            'use_receipt': use, 'status': status, 'physical_phase': phase}


def replay(result, H, prior, tariff, capacity=256):
    models = (H.record(), generate(H.record()))
    candidates = all_candidates(models)
    for entry in result['history']:
        candidates = update(models, candidates, entry['command'], entry['observation'])
        assert encoded(candidates) == sorted(map(tuple, entry['survivors']))
    generated = any(e['kind'] == 'generate_current_family' for e in result['events'])
    if result['selected'] is not None:
        assert len(candidates) == 1 and result['final_belief'] == []
        k, parity, q = next(iter(candidates))
        selected = result['selected']
        assert selected['machine'] == models[k] and selected['family'] == k
        assert selected['parity'] == parity
        cursor_committed = any(e['kind'] == 'commit_use_cursor' for e in result['events'])
        assert selected['state'] == (models[k]['transitions'][q][0] if cursor_committed else q)
    elif generated:
        assert encoded(candidates) == sorted(map(tuple, result['final_belief']))
    else:
        assert result['final_belief'] == []

    stock, spent = Q(result['starting_fuel']), Q(0)
    live, peak = prior['events'][-1]['live'], prior['events'][-1]['live']
    assert result['initial_live'] == live
    base, count, committed = live+8, 0, 0
    for event in result['events']:
        kind, work, new_live = event['kind'], event['work'], event['live']
        assert kind != 'actual_arrival'
        required = max(live, new_live)+event['workspace']+event['temporary']
        assert required == event['peak'] and required <= capacity
        extra = (tariff.interface if kind.startswith('native_') else
                 tariff.installation if kind == 'revision_installation' else
                 tariff.retention*new_live if kind in ('retain_current_model', 'retain_after_use') else Q(0))
        assert extra == Q(event['extra'])
        cost = tariff.scale*(tariff.work*work+tariff.rent*required*(work+1)
                             +tariff.write*(max(0, new_live-live)+event['rewrites'])+extra)
        assert cost == Q(event['bill']) and stock >= cost
        stock -= cost
        spent += cost
        live, peak = new_live, max(peak, required)
        assert stock == Q(event['fuel'])
        if kind == 'revision_installation':
            assert work == 8 and new_live == base and event['temporary'] == 8
        elif kind == 'generate_stutter_model':
            assert work == 12 and new_live == base+9 and event['temporary'] == 9
        elif kind == 'generate_current_family':
            count = 14
            assert work == 28 and new_live == base+9+28 and event['temporary'] == 28
        elif kind.startswith('prepare_'):
            assert work == 2*count+1 and event['temporary'] == 3*count+4
        elif kind.startswith('commit_') and kind != 'commit_use_cursor':
            assert work == 2*count+1 and event['workspace'] == 3*count+4
            entry = result['history'][committed]
            assert kind == 'commit_'+entry['command']
            count = len(entry['survivors'])
            assert new_live == base+9+2*count and event['rewrites'] == 2*count
            committed += 1
        elif kind == 'compact_current_model':
            size = 1+2*len(result['selected']['machine']['outputs'])
            assert new_live == size+26 and work == size+3
            assert event['rewrites'] == event['temporary'] == size+2
        elif kind.startswith('native_'):
            assert event['temporary'] == 2
            assert event['workspace'] in (3, 3*count+4)
    assert committed == len(result['history'])
    assert spent == Q(result['spent']) and stock == Q(result['fuel'])
    assert peak == result['peak_cells'] and live == result['live_cells']
    assert stock+spent == Q(result['starting_fuel'])
    assert result['source_remaining'] == prior['source_remaining']
    return {'spent': str(spent), 'fuel': str(stock), 'peak_cells': peak,
            'live_cells': live, 'source': result['source_remaining']}


def run_one(H, prior, environment, parity, phase=None, fuel=None, **kwargs):
    actual_phase = prior['physical_phase'] if phase is None else phase
    starting = Q(prior['fuel']) if fuel is None else Q(fuel)
    result = implementation.revise(H, prior['final_belief'], starting,
                                  prior['events'][-1]['live'], prior['source_remaining'],
                                  environment, actual_phase, parity, **kwargs)
    ordinary = reference(H.record(), environment.record(), actual_phase, parity,
                         kwargs.get('max_reads', 6), kwargs.get('switch_after'))
    assert result['native_trace'] == ordinary['native_trace'][:len(result['native_trace'])]
    assert len(result['history']) <= len(ordinary['history'])
    for actual, expected in zip(result['history'], ordinary['history']):
        assert actual['command'] == expected['command'] and actual['observation'] == expected['observation']
        assert sorted(map(tuple, actual['survivors'])) == sorted(map(tuple, expected['survivors']))
    if result['status'] in ('complete', 'use_prediction_mismatch', 'model_family_inadequate', 'current_family_unresolved'):
        assert result['status'] == ordinary['status']
    if result['use_receipt'] is not None:
        assert result['use_receipt'] == ordinary['use_receipt']
    if result['retained']:
        assert result['selected'] == ordinary['selected']
        assert result['acquired_retained'] and result['use_confirmed']
        assert result['physical_phase'] == ordinary['physical_phase']
    ledger = replay(result, H, prior, kwargs.get('tariff', implementation.access.Tariff()), kwargs.get('capacity', 256))
    return result, ledger


def main():
    H, prior, historical_four = handoffs()
    G = machine(generate(H.record()))
    assert G.record() == implementation.stutter(H).record()
    p = prior['probe']
    inherited, ample, statuses = [], [], {}
    for k, target in enumerate((H, G)):
        for parity in (0, 1):
            for phase in range(len(target.outputs)):
                result, ledger = run_one(H, p, target, parity, phase=phase)
                statuses[result['status']] = statuses.get(result['status'], 0)+1
                inherited.append({'family': k, 'phase': phase, 'parity': parity,
                                  'status': result['status'], 'retained': result['retained'], 'ledger': ledger})
                result, ledger = run_one(H, p, target, parity, phase=phase, fuel=100)
                assert result['retained'] and result['selected']['family'] == k
                assert result['selected']['parity'] == parity
                ample.append(ledger)
    assert statuses == {'funding:native_read': 4, 'funding:retain_after_use': 2, 'complete': 8}
    assert max(Q(x['spent']) for x in ample) == Q(805831, 65536)
    fixtures = {}
    five = implementation.Machine(('a',), (0,0,0,0,1), ((1,),(2,),(3,),(4,),(0,)))
    alternator = implementation.Machine(('a',), (0,1), ((1,),(0,)))
    cases = {
        'unchanged': (p, H, 1, {}), 'inserted': (p, G, 1, {}),
        'old_four_no_funds': (prior['old_four'], historical_four, 0, {}),
        'sensor_only_no_funds': (prior['sensing'], H, 1, {}),
        'capacity_80': (p, H, 1, {'capacity': 80}),
        'double_prices': (p, G, 1, {'tariff': implementation.access.Tariff(scale=Q(2))}),
        'five_read_limit': (p, H, 0, {'phase': 0, 'max_reads': 5}),
        'outside_five_zero': (p, five, 0, {'phase': 0}),
        'outside_five_one': (p, five, 0, {'phase': 1}),
        'outside_alternator': (p, alternator, 0, {'phase': 0}),
    }
    primary, _ = run_one(H, p, G, 1)
    unchanged, _ = run_one(H, p, H, 1)
    cases['late_parity_change'] = (p, H, 1, {'switch_after': len(unchanged['native_trace'])-1})
    needed = Q(primary['spent'])
    cases['exact_budget'] = (p, G, 1, {'fuel': needed})
    cases['one_quantum_short'] = (p, G, 1, {'fuel': needed-Q(1,65536)})
    # A derived reserve covers the forward action but not its cursor commit.
    through_action = Q(0)
    acquisition_done = False
    for event in primary['events']:
        through_action += Q(event['bill'])
        if event['kind'] == 'retain_current_model':
            acquisition_done = True
        elif acquisition_done and event['kind'] == 'native_a':
            break
    cases['cursor_commit_unfunded'] = (p, G, 1, {'fuel': through_action})
    for name, (old, env, parity, kwargs) in cases.items():
        result, ledger = run_one(H, old, env, parity, **kwargs)
        if name in ('unchanged', 'inserted', 'exact_budget'):
            assert result['retained']
        elif name == 'old_four_no_funds':
            assert result['status'] == 'funding:revision_installation' and Q(result['spent']) == 0
        elif name == 'outside_alternator':
            assert result['status'] == 'model_family_inadequate'
        elif name == 'late_parity_change':
            assert result['status'] == 'use_prediction_mismatch' and not result['retained']
        elif name == 'cursor_commit_unfunded':
            assert result['status'] == 'funding:commit_use_cursor' and result['acquired_retained']
            assert result['selected']['state'] != result['physical_phase'] and not result['retained']
        elif name == 'one_quantum_short':
            assert result['status'] == 'funding:retain_after_use' and result['use_confirmed']
        fixtures[name] = {'status': result['status'], 'retained': result['retained'],
                          'acquired_retained': result['acquired_retained'],
                          'use_confirmed': result['use_confirmed'], 'ledger': ledger}
    for permutation in permutations(range(3)):
        outputs, transitions = [None]*3, [None]*3
        for q in range(3):
            outputs[permutation[q]] = H.outputs[q]
            transitions[permutation[q]] = (permutation[H.transitions[q][0]],)
        renamed = implementation.Machine(('a',), tuple(outputs), tuple(transitions), permutation[H.initial])
        old = dict(p, final_belief=[[c,permutation[q]] for c,q in p['final_belief']],
                   physical_phase=permutation[p['physical_phase']])
        result, _ = run_one(renamed, old, machine(generate(renamed.record())), 1)
        assert result['native_trace'] == primary['native_trace'] and result['spent'] == primary['spent']
    # Reuse only the already-installed old controller for an affordable refutation.
    old = prior['old_four']
    account = implementation.access.Account(Q(old['fuel']), initial_live=25)
    port = implementation.access.Port(historical_four, old['physical_phase'], 0, account)
    controller = implementation.access.Diagnoser(H, port.command, account)
    controller.belief = list(map(tuple, old['final_belief']))
    try:
        controller.step('read')
        raise AssertionError('expected acquired refutation')
    except implementation.Halt as error:
        assert str(error) == 'model_family_inadequate'
    assert not controller.belief and account.fuel == Q(29509,65536) and account.live == 23
    output = {'scope': 'fresh current-family audit; independent semantics and declared-cost replay',
              'family_statuses': statuses, 'inherited_family_runs': inherited,
              'ample_assay': {'fuel': 100, 'cases': 14, 'maximum_spent': str(max(Q(x['spent']) for x in ample))},
              'fixtures': fixtures, 'state_relabellings': 6,
              'old_family_refutation': {'fuel': str(account.fuel), 'live_cells': account.live, 'observation': 0},
              'hashes': {name: sha256((HERE/name).read_bytes()).hexdigest()
                         for name in ('revision.py','PROTOCOL.md','independent_check.py','../diagnosis.py','../../model.py')}}
    (HERE/'independent-check.json').write_text(json.dumps(output, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'family_statuses': statuses, 'ample_cases': 14, 'fixtures': len(fixtures), 'state_relabellings': 6}))


if __name__ == '__main__':
    main()
