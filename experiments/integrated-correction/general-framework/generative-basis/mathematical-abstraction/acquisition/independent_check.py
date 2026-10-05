"""Independent observation-table semantics and exact tariff-ledger replay.

The reference learner below never calls model.Learner, Machine.answer, repair,
words, ordered or the model's quotient helpers. It sees only an endpoint
callback. Its unmetered exhaustive runs check mathematics, not affordability.
Ledger replay separately reconstructs every recorded charge from the tariff.
"""
from collections import deque
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import model as implementation


HERE = Path(__file__).resolve().parent


def shortlex(seq):
    return sorted(set(seq), key=lambda s: (len(s), s))


def endpoint(machine, word):
    state = machine['initial']
    for token in word:
        column = tuple(machine['alphabet']).index(token)
        state = machine['transitions'][state][column]
    return machine['outputs'][state]


def finite_words(alphabet, bound):
    layer = ['']
    yield ''
    for _ in range(bound):
        layer = [w+a for w in layer for a in alphabet]
        yield from layer


def ordinary_learner(alphabet, bound, oracle):
    """Plain observation-table algorithm; independent data/control flow."""
    access, suffixes, data = [''], [''], {}
    experiments, hypotheses, changes = [], [], []

    def get(word):
        if word not in data:
            data[word] = oracle(word)
            experiments.append({'word': word, 'output': data[word]})
        return data[word]

    while True:
        while True:
            frontier = shortlex(access + [s+a for s in access for a in alphabet])
            for prefix in frontier:
                for ending in suffixes:
                    get(prefix+ending)
            signatures = {s: tuple(data[s+e] for e in suffixes) for s in frontier}
            old = {signatures[s] for s in access}
            absent = [s for s in frontier if signatures[s] not in old]
            if absent:
                access = shortlex(access+[absent[0]])
                changes.append({'kind': 'closure', 'history': absent[0]})
                continue
            split = None
            for i in range(len(access)):
                for j in range(i+1, len(access)):
                    left, right = access[i], access[j]
                    if signatures[left] != signatures[right]:
                        continue
                    for action in alphabet:
                        for ending in suffixes:
                            if data[left+action+ending] != data[right+action+ending]:
                                split = (left, right, action+ending)
                                break
                        if split is not None:
                            break
                    if split is not None:
                        break
                if split is not None:
                    break
            if split is not None:
                left, right, ending = split
                suffixes = shortlex(suffixes+[ending])
                changes.append({'kind': 'distinction', 'histories': [left, right],
                                'suffix': ending,
                                'observations': [data[left+ending], data[right+ending]]})
                continue
            unique, representatives = [], []
            for prefix in access:
                if signatures[prefix] not in unique:
                    unique.append(signatures[prefix])
                    representatives.append(prefix)
            hypothesis = {
                'alphabet': tuple(alphabet),
                'outputs': tuple(data[s] for s in representatives),
                'transitions': tuple(tuple(unique.index(signatures[s+a]) for a in alphabet)
                                     for s in representatives),
                'initial': unique.index(signatures[''])}
            hypotheses.append(hypothesis)
            assert len(unique) <= bound
            break
        counterexample = None
        for word in finite_words(alphabet, 2*bound-2):
            prediction, actual = endpoint(hypothesis, word), get(word)
            if prediction != actual:
                counterexample = word
                changes.append({'kind': 'prediction_failure', 'word': word,
                                'predicted': prediction, 'observed': actual})
                break
        if counterexample is None:
            return {'model': hypothesis, 'hypotheses': hypotheses,
                    'queries': experiments, 'trace': changes}
        access = shortlex(access+[counterexample[:i]
                                  for i in range(len(counterexample)+1)])


def distinguishing_word(left, right, starts=None):
    """Exhaust the reachable product graph; None means exact equivalence."""
    assert tuple(left['alphabet']) == tuple(right['alphabet'])
    start = starts if starts is not None else (left['initial'], right['initial'])
    queue, seen = deque([(start[0], start[1], '')]), set()
    while queue:
        a, b, word = queue.popleft()
        if (a, b) in seen:
            continue
        seen.add((a, b))
        if left['outputs'][a] != right['outputs'][b]:
            return word
        for column, token in enumerate(left['alphabet']):
            queue.append((left['transitions'][a][column],
                          right['transitions'][b][column], word+token))
    return None


def assert_minimal(machine):
    reachable, todo = set(), [machine['initial']]
    while todo:
        state = todo.pop()
        if state in reachable:
            continue
        reachable.add(state)
        todo.extend(machine['transitions'][state])
    assert reachable == set(range(len(machine['outputs'])))
    witnesses = {}
    for a in sorted(reachable):
        for b in sorted(reachable):
            if a < b:
                word = distinguishing_word(machine, machine, (a, b))
                assert word is not None
                witnesses[f'{a},{b}'] = word
    return witnesses


def replay_ledger(result, tariff, capacity, source=20):
    """Check every successful event without calling Meter.pay."""
    stock, live, high = Q(result['initial_fuel']), 0, 0
    totals, spent = {}, Q(0)
    special = {'installation': tariff.install, 'target_reset': tariff.reset,
               'target_action': tariff.action, 'endpoint_read': tariff.read,
               'extraction_work': tariff.read}
    for event in result['events']:
        work, new_live = event['work'], event['live']
        peak = max(live, new_live)+event['workspace']+event['temporary']
        assert peak == event['peak'] and peak <= capacity
        assert event['duration'] == work+1
        extra = special.get(event['kind'], Q(0))
        if event['kind'] == 'retention_epoch':
            extra = tariff.final_rent*new_live
        charge = tariff.scale*(extra + tariff.work*work + tariff.rent*peak*(work+1)
                               + tariff.write*max(0, new_live-live))
        assert charge == Q(event['bill']) and stock >= charge
        stock -= charge
        spent += charge
        totals[event['kind']] = totals.get(event['kind'], Q(0))+charge
        assert stock == Q(event['fuel'])
        live, high = new_live, max(high, peak)
    assert spent == Q(result['spent']) and stock == Q(result['fuel'])
    assert high == result['peak_cells']
    assert totals == {key: Q(value) for key, value in result['costs'].items()}
    assert stock+spent == Q(result['initial_fuel'])
    use = result['use']
    if use is not None:
        assert source >= 10 and use['source'] == source-10
        assert use['transferred']+use['wasted'] == 10
        assert use['transferred'] == 10*int(use['success'])
        assert Q(use['fuel_after_return']) == stock+use['transferred']
        assert Q(result['initial_fuel'])+source == (spent+Q(use['fuel_after_return'])
                                                  +use['source']+use['wasted'])
    return {'events': len(result['events']), 'spent': str(spent),
            'fuel_before_return': str(stock), 'peak_cells': high}


def fixture_checks():
    unary = implementation.Machine(('a',), (0, 0, 1), ((1,), (2,), (0,)))
    binary = implementation.Machine(('a', 'b'), (0, 0, 1), ((1, 0), (2, 0), (0, 0)))
    # Derived sharp-budget sensitivity checks, not prespecified population arms.
    exact_bill = Q(implementation.acquisition(unary)['spent'])
    cases = {
        'primary': (unary, {}),
        'binary': (binary, {}),
        'fourfold_tariffs': (unary, {'tariff': implementation.Tariff(scale=Q(4))}),
        'small_capacity': (unary, {'capacity': 48}),
        'installation_denied': (unary, {'fuel': 5}),
        'retention_denied': (unary, {'tariff': implementation.Tariff(final_rent=Q(100))}),
        'false_bound': (unary, {'bound': 1}),
        'inverted_sensor': (unary, {'invert': True}),
        'broken_reset': (unary, {'broken_reset': True}),
        'frozen': (unary, {'frozen': True}),
        'exact_budget': (unary, {'fuel': exact_bill}),
        'one_tick_short': (unary, {'fuel': exact_bill-Q(1, 65536)}),
    }
    records = {}
    for name, (target, kwargs) in cases.items():
        result = implementation.acquisition(target, **kwargs)
        tariff = kwargs.get('tariff', implementation.Tariff())
        ledger = replay_ledger(result, tariff, kwargs.get('capacity', 256))
        witness = (None if result['model'] is None else
                   distinguishing_word(target.record(), result['model']))
        records[name] = {'status': result['status'], 'certified': result['certified'],
                         'retained': result['retained'], 'ledger': ledger,
                         'physical_counterexample': witness, 'use': result['use']}
        if name == 'primary':
            assert result['status'] == 'complete' and result['certified'] and result['retained']
            assert witness is None and result['use']['success']
            assert len(result['use']['word']) > result['max_observed_length']
            assert result['use']['word'] not in {q['word'] for q in result['queries']}
            ordinary = ordinary_learner(('a',), 3, lambda w: endpoint(target.record(), w))
            for key in ('model', 'hypotheses', 'queries', 'trace'):
                assert result[key] == ordinary[key], key
            records[name]['state_pair_witnesses'] = assert_minimal(result['model'])
            # Complete old preparation/prediction prefix plus the new phase law.
            assert Q(145) == (Q(4+1+74+10) + Q(result['spent'])
                             + Q(result['use']['fuel_after_return'])
                             + result['use']['source']+result['use']['wasted'])
        elif name in ('binary', 'fourfold_tariffs', 'small_capacity', 'installation_denied'):
            assert result['status'] != 'complete' and not result['retained']
        elif name == 'retention_denied':
            assert result['status'] == 'funding:retention_epoch' and not result['retained']
            assert result['use'] is None
        elif name in ('false_bound', 'broken_reset'):
            assert witness is not None and result['use'] is None
        elif name == 'inverted_sensor':
            inverted = dict(target.record(), outputs=tuple(1-x for x in target.outputs))
            assert distinguishing_word(inverted, result['model']) is None
            assert witness is not None
            assert result['use'] is not None and not result['use']['success']
        elif name == 'frozen':
            assert not result['certified'] and not result['retained']
            assert result['status'] == 'frozen_after_prediction_failure'
        elif name == 'exact_budget':
            assert result['status'] == 'complete' and result['retained']
            assert Q(result['fuel']) == 0 and Q(result['spent']) == exact_bill
            assert result['use']['success'] and Q(result['use']['fuel_after_return']) == 10
        elif name == 'one_tick_short':
            assert result['status'] == 'funding:extraction_work'
            assert result['retained'] and result['use'] is None
    return records


def exhaustive_unary():
    count, state_histogram, fitting = 0, {}, 0
    maximum_spent, maximum_peak = Q(0), 0
    for n in range(1, 4):
        for outputs in product((0, 1), repeat=n):
            for successors in product(range(n), repeat=n):
                target = implementation.Machine(('a',), outputs, tuple((x,) for x in successors))
                # Supplemental mathematical validation with generous explicit
                # test stocks; not an additional affordable inherited history.
                result = implementation.acquisition(target, fuel=1000000,
                                                     capacity=50000, bound=3, use=False)
                assert result['status'] == 'complete' and result['retained']
                conventional = ordinary_learner(('a',), 3,
                                               lambda w, t=target.record(): endpoint(t, w))
                for key in ('model', 'hypotheses', 'queries', 'trace'):
                    assert result[key] == conventional[key], (n, outputs, successors, key)
                assert distinguishing_word(target.record(), result['model']) is None
                assert_minimal(result['model'])
                replay_ledger(result, implementation.Tariff(), 50000)
                spent = Q(result['spent'])
                fitting += int(spent <= 36 and result['peak_cells'] <= 256)
                maximum_spent = max(maximum_spent, spent)
                maximum_peak = max(maximum_peak, result['peak_cells'])
                k = str(len(result['model']['outputs']))
                state_histogram[k] = state_histogram.get(k, 0)+1
                count += 1
    assert count == 234
    assert fitting == 222 and maximum_spent == Q(735947, 16384) and maximum_peak == 168
    return {'targets': count, 'matched_query_hypothesis_and_refinement_traces': count,
            'equivalent_and_minimal_models': count, 'replayed_ledgers': count,
            'learned_state_histogram': state_histogram,
            'fixed_supplied_bound': 3,
            'acquisition_and_retention_fit_36_fuel_256_cells': fitting,
            'maximum_acquisition_and_retention_spent': str(maximum_spent),
            'maximum_peak_cells': maximum_peak,
            'scope': 'mathematical validation with supplemental test stocks, not physical population success'}


def main():
    output = {'fixtures': fixture_checks(), 'exhaustive_unary': exhaustive_unary(),
              'scope': 'independent semantic comparator, product graph/minimality and tariff replay; not empirical calibration',
              'hashes': {name: sha256((HERE/name).read_bytes()).hexdigest()
                         for name in ('model.py', 'PROTOCOL.md', 'independent_check.py')}}
    (HERE/'independent-check.json').write_text(json.dumps(output, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'fixtures': len(output['fixtures']), **output['exhaustive_unary']}))


if __name__ == '__main__':
    main()
