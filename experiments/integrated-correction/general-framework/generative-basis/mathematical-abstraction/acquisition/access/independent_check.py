"""Independent chronological belief semantics and rational resource replay.

The reference policy and update below use explicit Boolean tuples and sets,
never Diagnoser, flags, its transition evaluator or its selection methods.
The tariff replay validates the implementation's declared macro schedule;
it is not an independent physical cost model or hardware measurement.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path

import diagnosis as implementation


HERE = Path(__file__).resolve().parent


def inherited_state():
    """Execute the real preceding learner and its one productive use."""
    m = implementation.acquisition
    target = m.Machine(('a',), (0, 0, 1), ((1,), (2,), (0,)))
    meter = m.Meter(36)
    port = m.TargetPort(target, meter)
    learner = m.Learner(target.alphabet, 3, port.query, meter)
    learner.run()
    plan = learner.plan_novel_use()
    result = port.use(plan, 20)
    assert learner.retained and learner.machine.cells == 7 and meter.live == 15
    assert not learner.S and not learner.E and not learner.cache
    assert plan == 'aaaaa' and port.state == 2 and result['source'] == 10
    assert Q(result['fuel_after_return']) == Q(1030367, 65536)
    assert Q(meter.spent) == Q(1984289, 65536)
    assert Q(145) == 89 + meter.spent + Q(result['fuel_after_return']) + result['source']
    return learner.machine, Q(result['fuel_after_return']), result['source'], port.state


def encode(world):
    tau, sigma, broken, blocked, phase = world
    return (tau + 2*sigma + 4*broken + 8*blocked, phase)


def initial_worlds(machine, expanded=False):
    return set(product((0, 1), (0, 1), (0, 1),
                       (0, 1) if expanded else (0,), range(len(machine['outputs']))))


def successor(machine, world, command):
    tau, sigma, broken, blocked, phase = world
    output = None
    if command == 'a':
        phase = machine['transitions'][phase][0]
    elif command == 'reset':
        phase = phase if broken else machine['initial']
    elif command == 'read':
        output = machine['outputs'][phase] ^ tau ^ sigma
    elif command == 'probe':
        output = int(not blocked) * (machine['outputs'][phase] ^ tau)
    else:
        raise AssertionError(command)
    return (tau, sigma, broken, blocked, phase), output


def update(machine, worlds, command, observation):
    after = [successor(machine, world, command) for world in worlds]
    return {world for world, predicted in after if predicted == observation}


def represented_pairs(pairs, factor=None):
    """Interpret the public compressed archive independently of its updater."""
    if factor is None:
        return sorted(map(tuple, pairs))
    assert factor == [0, 1]
    return sorted((code+8*blocked, phase) for code, phase in pairs for blocked in factor)


def reference_policy(machine, actual, expanded=False, probe=True, receipt_flip=False):
    """Unmetered conventional consistency policy with independent transitions."""
    worlds = initial_worlds(machine, expanded)
    actual = tuple(actual)
    history, native = [], []

    def step(command):
        nonlocal actual, worlds
        actual, observed = successor(machine, actual, command)
        if command == 'probe' and receipt_flip:
            observed ^= 1
        native.append({'command': command, 'observation': observed})
        worlds = update(machine, worlds, command, observed)
        history.append({'command': command, 'observation': observed,
                        'survivors': [list(encode(w)) for w in sorted(worlds, key=encode)]})
        assert worlds

    def go_to(goal):
        phases = {world[-1] for world in worlds}
        assert len(phases) == 1
        current = next(iter(phases))
        for _ in range(len(machine['outputs'])):
            if current == goal:
                return
            step('a')
            current = machine['transitions'][current][0]
        raise AssertionError('unreachable phase')

    for command in ('read', 'a', 'read', 'a', 'read'):
        step(command)
    go_to(machine['transitions'][machine['initial']][0])
    for command in ('reset', 'a', 'read'):
        step(command)
    sensor_worlds = set(worlds)
    if probe:
        go_to(next(q for q, value in enumerate(machine['outputs']) if value == 1))
        step('probe')
    return {'history': history, 'native_trace': native,
            'final_belief': [list(encode(w)) for w in sorted(worlds, key=encode)],
            'sensor_belief': [list(encode(w)) for w in sorted(sensor_worlds, key=encode)]}


def replay_beliefs(result, machine, expanded=False):
    """Replay only committed observations; a denied commit may leave stale data."""
    worlds = initial_worlds(machine, expanded)
    for entry in result['history']:
        worlds = update(machine, worlds, entry['command'], entry['observation'])
        assert sorted(map(encode, worlds)) == represented_pairs(entry['survivors'], entry.get('blocked_factor'))
    if any(event['kind'] == 'generate_candidate_family' for event in result['events']):
        assert sorted(map(encode, worlds)) == represented_pairs(result['final_belief'], result.get('blocked_factor'))
    else:
        assert result['final_belief'] == []
    return len(result['history'])


def replay_ledger(result, tariff, capacity=256, initial_live=15, initial_source=10):
    stock, live, peak, spent, income = Q(result['starting_fuel']), initial_live, initial_live, Q(0), Q(0)
    for event in result['events']:
        if event['kind'] == 'actual_arrival':
            assert event['amount'] == 10
            stock += 10
            income += 10
            assert stock == Q(event['fuel'])
            continue
        work, new_live = event['work'], event['live']
        assert work >= 0 and event['rewrites'] >= 0
        required = max(live, new_live) + event['workspace'] + event['temporary']
        assert required == event['peak'] and required <= capacity
        extra = Q(0)
        if event['kind'].startswith('native_'):
            extra = tariff.interface
        elif event['kind'] == 'arrival_receipt':
            extra = tariff.receipt
        elif event['kind'] == 'diagnostic_installation':
            extra = tariff.installation
        elif event['kind'] == 'retain_diagnosis':
            extra = tariff.retention*new_live
        assert extra == Q(event['extra'])
        charge = tariff.scale*(tariff.work*work + tariff.rent*required*(work+1)
                               + tariff.write*(max(0, new_live-live)+event['rewrites']) + extra)
        assert charge == Q(event['bill']) and stock >= charge
        stock -= charge
        spent += charge
        live, peak = new_live, max(peak, required)
        assert stock == Q(event['fuel'])
        assert stock+spent == Q(result['starting_fuel'])+income
    assert stock == Q(result['fuel']) and spent == Q(result['spent'])
    assert income == Q(result['income']) and peak == result['peak_cells']
    assert initial_source-result['source_remaining'] == income+result['wasted']
    assert Q(result['starting_fuel'])+initial_source == (stock+spent
                                                        +result['source_remaining']+result['wasted'])
    return {'events': len(result['events']), 'spent': str(spent), 'income': str(income),
            'fuel': str(stock), 'source': result['source_remaining'],
            'wasted': result['wasted'], 'peak_cells': peak}


def check_candidate_schedule(result, expanded=False, factored=False):
    """Tie charged storage/work to separately verified committed row counts."""
    base, count, committed = 23+int(factored), 0, 0
    for event in result['events']:
        kind = event['kind']
        if kind == 'diagnostic_installation':
            assert event['live'] == base and event['work'] == 8
        elif kind == 'generate_candidate_family':
            count = 48 if expanded and not factored else 24
            assert event['live'] == base+2*count
            assert event['work'] == event['temporary'] == 2*count
        elif kind == 'expand_transfer_factor':
            assert factored and count == 2
            assert event['work'] == 4*count+1 and event['temporary'] == 4*count
            assert event['rewrites'] == 2*count
            count *= 2
            assert event['live'] == base+2*count
        elif kind.startswith('prepare_'):
            assert event['work'] == 2*count+1 and event['temporary'] == 3*count+4
        elif kind.startswith('native_') or kind == 'arrival_receipt':
            assert event['workspace'] == 3*count+4 and event['temporary'] == 2
        elif kind.startswith('commit_'):
            assert event['work'] == 2*count+1 and event['workspace'] == 3*count+4
            entry = result['history'][committed]
            assert kind == 'commit_'+entry['command']
            count = len(entry['survivors'])
            assert event['live'] == base+2*count and event['rewrites'] == 2*count
            committed += 1
    assert committed == len(result['history'])


def compare_reference(result, reference):
    assert result['native_trace'] == reference['native_trace']
    assert len(result['history']) == len(reference['history'])
    for actual, expected in zip(result['history'], reference['history']):
        assert actual['command'] == expected['command'] and actual['observation'] == expected['observation']
        assert represented_pairs(actual['survivors'], actual.get('blocked_factor')) == sorted(map(tuple, expected['survivors']))
    assert represented_pairs(result['final_belief'], result.get('blocked_factor')) == sorted(map(tuple, reference['final_belief']))
    sensed = result['sensor_verdict']
    assert represented_pairs(sensed['alternatives'], sensed.get('blocked_factor')) == sorted(map(tuple, reference['sensor_belief']))


def all_primary_worlds(model, fuel, source):
    records, count = {}, 0
    for tau, sigma, broken, phase in product((0, 1), (0, 1), (0, 1), range(3)):
        actual = (tau, sigma, broken, 0, phase)
        label = f'{tau}{sigma}{broken}@{phase}'
        records[label] = {}
        for probe in (False, True):
            result = implementation.diagnose(model, fuel, source, phase,
                                            target_flip=tau, sensor_flip=sigma,
                                            broken_reset=broken, probe=probe)
            assert result['status'] == 'complete' and result['retained'], (label, probe, result['status'])
            reference = reference_policy(model.record(), actual, probe=probe)
            compare_reference(result, reference)
            replay_beliefs(result, model.record())
            check_candidate_schedule(result)
            ledger = replay_ledger(result, implementation.Tariff())
            assert len(result['sensor_verdict']['alternatives']) == 2
            assert len(result['final_belief']) == (1 if probe else 2)
            assert result['source_remaining'] == (0 if probe else 10)
            if probe:
                assert result['final_belief'][0][0] == encode(actual)[0]
                assert Q(result['income']) == 10*(1-tau)
            assert Q(145) == (89+Q(1984289, 65536)+Q(result['spent'])+Q(result['fuel'])
                              +result['source_remaining']+result['wasted'])
            records[label]['probe' if probe else 'sensor_only'] = {
                'ledger': ledger, 'native_trace': result['native_trace'],
                'final_belief': result['final_belief']}
            count += 1
    for tau, sigma, broken, phase in product((0, 1), (0, 1), (0, 1), range(3)):
        left, right = f'{tau}{sigma}{broken}@{phase}', f'{1-tau}{1-sigma}{broken}@{phase}'
        assert records[left]['sensor_only']['native_trace'] == records[right]['sensor_only']['native_trace']
        assert records[left]['sensor_only']['ledger'] == records[right]['sensor_only']['ledger']
        # All choices and readings agree up to the last productive consequence.
        assert records[left]['probe']['native_trace'][:-1] == records[right]['probe']['native_trace'][:-1]
    return {'runs': count, 'worlds': 24, 'independent_policy_and_update_matches': count,
            'replayed_resource_ledgers': count, 'records': records,
            'scope': 'same inherited stocks; alternate physical phases are explicit boundary perturbations'}


def expanded_assay(model):
    counts = {'unique_after_arrival': 0, 'three_after_nonarrival': 0}
    for tau, sigma, broken, blocked, phase in product((0, 1), (0, 1), (0, 1), (0, 1), range(3)):
        result = implementation.diagnose(model, 10000, 10, phase, target_flip=tau,
                                        sensor_flip=sigma, broken_reset=broken,
                                        blocked=blocked, expanded=True, capacity=512)
        assert result['status'] == 'complete' and result['retained']
        reference = reference_policy(model.record(), (tau, sigma, broken, blocked, phase), expanded=True)
        compare_reference(result, reference)
        replay_beliefs(result, model.record(), expanded=True)
        check_candidate_schedule(result, expanded=True)
        replay_ledger(result, implementation.Tariff(), capacity=512)
        assert len(result['sensor_verdict']['alternatives']) == 4
        assert [encode((tau, sigma, broken, blocked, result['physical_phase']))[0], result['physical_phase']] in result['final_belief']
        if Q(result['income']):
            assert len(result['final_belief']) == 1
            counts['unique_after_arrival'] += 1
        else:
            assert len(result['final_belief']) == 3
            counts['three_after_nonarrival'] += 1
    assert counts == {'unique_after_arrival': 12, 'three_after_nonarrival': 36}
    return {'worlds': 48, **counts,
            'scope': 'explicit mathematical assay funds10000/capacity512, not inherited affordable continuation'}


def factored_continuation(model, fuel, source):
    counts = {'sensor_complete': 0, 'probe_complete': 0, 'probe_retention_unfunded': 0}
    states, maximum_peak = {}, 0
    for tau, sigma, broken, blocked, phase in product((0, 1), (0, 1), (0, 1), (0, 1), range(3)):
        for probe in (False, True):
            result = implementation.diagnose(model, fuel, source, phase, target_flip=tau,
                                            sensor_flip=sigma, broken_reset=broken,
                                            blocked=blocked, factored_access=True, probe=probe)
            reference = reference_policy(model.record(), (tau, sigma, broken, blocked, phase),
                                         expanded=True, probe=probe)
            compare_reference(result, reference)
            replay_beliefs(result, model.record(), expanded=True)
            check_candidate_schedule(result, expanded=True, factored=True)
            replay_ledger(result, implementation.Tariff())
            maximum_peak = max(maximum_peak, result['peak_cells'])
            if not probe:
                assert result['status'] == 'complete' and result['retained']
                assert result['blocked_factor'] == [0, 1]
                assert len(represented_pairs(result['final_belief'], result['blocked_factor'])) == 4
                assert result['source_remaining'] == 10
                counts['sensor_complete'] += 1
            else:
                assert result['blocked_factor'] is None
                assert len(result['final_belief']) == (1 if Q(result['income']) else 3)
                assert result['source_remaining'] == 0
                if result['status'] == 'complete':
                    assert result['retained']
                    counts['probe_complete'] += 1
                else:
                    assert result['status'] == 'funding:retain_diagnosis'
                    assert not result['retained'] and result['verdict'] is None
                    counts['probe_retention_unfunded'] += 1
                states[f'{tau}{sigma}{broken}{blocked}@{phase}'] = {
                    'status': result['status'], 'retained': result['retained'],
                    'belief': result['final_belief'], 'spent': result['spent'],
                    'fuel': result['fuel'], 'income': result['income']}
    assert counts == {'sensor_complete': 48, 'probe_complete': 36, 'probe_retention_unfunded': 12}
    return {'worlds': 48, 'runs': 96, **counts, 'maximum_peak_cells': maximum_peak,
            'scope': 'paid factor representation of full48 class; same actual inherited stocks',
            'probe_records': states}


def adverse_cases(model, fuel, source, phase):
    fourth = implementation.acquisition.Machine(('a',), (0, 0, 0, 1), ((1,), (2,), (3,), (0,)))
    cases = {
        'installation_unfunded': {'fuel': Q(1, 2)},
        'capacity_64': {'capacity': 64},
        'fourfold_tariffs': {'tariff': implementation.Tariff(scale=Q(4))},
        'expanded_inherited_capacity': {'expanded': True},
        'fourth_phase_detected': {'environment_model': fourth, 'physical_state': 0},
        'fourth_phase_undetected': {'environment_model': fourth},
        'inverted_receipt': {'receipt_flip': 1},
        'unmodeled_blocked_transfer': {'blocked': 1},
    }
    # Controlled budget withdrawals are derived diagnostics, not new reserves.
    negative = implementation.diagnose(model, 10000, source, phase, target_flip=1)
    before_receipt = Q(0)
    for event in negative['events']:
        if 'bill' in event:
            before_receipt += Q(event['bill'])
        if event['kind'] == 'native_probe':
            break
    cases['no_arrival_receipt_unfunded'] = {'fuel': before_receipt, 'target_flip': 1}
    cases['actual_arrival_funds_receipt'] = {'fuel': before_receipt, 'sensor_flip': 1}
    output = {}
    for name, supplied in cases.items():
        kwargs = dict(supplied)
        starting = kwargs.pop('fuel', fuel)
        initial_phase = kwargs.pop('physical_state', phase)
        result = implementation.diagnose(model, starting, source, initial_phase, **kwargs)
        replay_beliefs(result, model.record(), expanded=kwargs.get('expanded', False))
        check_candidate_schedule(result, expanded=kwargs.get('expanded', False))
        ledger = replay_ledger(result, kwargs.get('tariff', implementation.Tariff()),
                               capacity=kwargs.get('capacity', 256))
        if name == 'installation_unfunded':
            assert result['status'] == 'funding:diagnostic_installation' and Q(result['spent']) == 0
        elif name in ('capacity_64', 'expanded_inherited_capacity'):
            assert result['status'].startswith('capacity:') and not result['retained']
        elif name == 'fourfold_tariffs':
            assert result['status'].startswith('funding:') and not result['retained']
        elif name == 'fourth_phase_detected':
            assert result['status'] == 'model_family_inadequate' and result['final_belief'] == []
        elif name in ('inverted_receipt', 'unmodeled_blocked_transfer', 'fourth_phase_undetected'):
            assert result['status'] == 'complete' and result['retained']
            assert result['final_belief'][0][0] == 3  # falsely infers both complements
        elif name == 'no_arrival_receipt_unfunded':
            assert result['status'] == 'funding:arrival_receipt'
            assert result['wasted'] == 10 and result['source_remaining'] == 0
            assert Q(result['fuel']) == 0 and not result['retained']
            assert not any(h['command'] == 'probe' for h in result['history'])
        elif name == 'actual_arrival_funds_receipt':
            assert result['status'] == 'complete' and result['retained']
            assert Q(result['income']) == 10 and result['source_remaining'] == 0
        output[name] = {'status': result['status'], 'retained': result['retained'],
                        'belief': result['final_belief'], 'ledger': ledger}
    return output


def relabelled_retained_models(model, fuel, source, phase):
    """Learned state names must not be secretly replaced by target phase IDs."""
    baseline = implementation.diagnose(model, fuel, source, phase, sensor_flip=1)
    for renaming in permutations(range(3)):
        outputs, transitions = [None]*3, [None]*3
        for old in range(3):
            outputs[renaming[old]] = model.outputs[old]
            transitions[renaming[old]] = (renaming[model.transitions[old][0]],)
        renamed = implementation.acquisition.Machine(('a',), tuple(outputs), tuple(transitions),
                                                    initial=renaming[model.initial])
        result = implementation.diagnose(renamed, fuel, source, renaming[phase], sensor_flip=1)
        assert result['status'] == 'complete' and result['retained']
        assert result['native_trace'] == baseline['native_trace']
        assert result['spent'] == baseline['spent']
        assert result['final_belief'] == [[2, renaming[2]]]
        compare_reference(result, reference_policy(renamed.record(), (0, 1, 0, 0, renaming[phase])))
        replay_beliefs(result, renamed.record())
        replay_ledger(result, implementation.Tariff())
        check_candidate_schedule(result)
    return {'state_renamings': 6, 'native_traces_and_costs_preserved': True}


def main():
    model, fuel, source, phase = inherited_state()
    output = {'primary_class': all_primary_worlds(model, fuel, source),
              'expanded_assay': expanded_assay(model),
              'factored_continuation': factored_continuation(model, fuel, source),
              'adverse_cases': adverse_cases(model, fuel, source, phase),
              'retained_model_relabelling': relabelled_retained_models(model, fuel, source, phase),
              'inherited': {'model': model.record(), 'fuel': str(fuel), 'source': source,
                            'physical_phase_environment_only': phase, 'initial_live_cells': 15},
              'hashes': {name: sha256((HERE/name).read_bytes()).hexdigest()
                         for name in ('diagnosis.py', 'PROTOCOL.md', 'independent_check.py', '../model.py')},
              'scope': 'independent consistency policy and state update; replay of stipulated macro-operation charges'}
    (HERE/'independent-check.json').write_text(json.dumps(output, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'primary_runs': output['primary_class']['runs'],
                      'expanded': output['expanded_assay'],
                      'factored': {k: v for k,v in output['factored_continuation'].items() if k != 'probe_records'},
                      'adverse_cases': len(output['adverse_cases'])}))


if __name__ == '__main__':
    main()
