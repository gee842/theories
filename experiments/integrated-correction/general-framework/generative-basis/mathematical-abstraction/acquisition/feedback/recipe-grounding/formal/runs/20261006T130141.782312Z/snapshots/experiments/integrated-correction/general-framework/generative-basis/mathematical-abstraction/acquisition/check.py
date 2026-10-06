"""Joined history, acquired model, adverse controls and finite enumeration."""
from collections import deque, Counter
from dataclasses import asdict, replace
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import model as m

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def from_record(record):
    return m.Machine(tuple(record['alphabet']), tuple(record['outputs']),
                     tuple(tuple(t) for t in record['transitions']), record['initial'])


def distinguishing_word(first, second):
    """Independent full product graph, used only after learning has ended."""
    todo = deque([(first.initial, second.initial, '')])
    seen = set()
    while todo:
        s,t,w = todo.popleft()
        if (s,t) in seen:
            continue
        seen.add((s,t))
        if first.outputs[s] != second.outputs[t]:
            return w
        for j,a in enumerate(first.alphabet):
            todo.append((first.transitions[s][j], second.transitions[t][j], w+a))
    return None


def minimal(machine):
    reachable = {machine.initial}
    while True:
        nxt = reachable | {t for s in reachable for t in machine.transitions[s]}
        if nxt == reachable:
            break
        reachable = nxt
    if len(reachable) != len(machine.outputs):
        return False
    return all(distinguishing_word(replace(machine,initial=s), replace(machine,initial=t))
               is not None for s in reachable for t in reachable if s < t)


def inherited_history():
    path = ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/model.py'
    spec = importlib.util.spec_from_file_location('_abstraction_prediction', path)
    pred = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = pred
    spec.loader.exec_module(pred)
    law = pred.Law()
    preparations, _ = pred.prepare(law)
    p = next(r for r in preparations if r['commissioned'])
    assert p['reserve'] == 20 and Q(p['probability']) == Q(2,9)
    s = pred.State(p['reserve'])
    weight = Q(p['probability']) / 2  # initial hidden orientation 1
    counts = {k: 0 for k in pred.MOMENTS}
    history = []
    for t in range(10):
        branches = pred.advance(law,s,'variable',int(t < 6),t >= 6)
        if t == 0:
            branches = [b for b in branches if b[0].gate == 1 and b[0].last == 1]
        assert len(branches) == 1
        s,prob,inc = branches[0]
        weight *= prob
        for k,v in zip(pred.MOMENTS,inc):
            counts[k] += v
        history.append(dict(exposure=t+1, state=asdict(s), probability=str(prob)))
    source = p['remainder'] + (p['packets']-10)*law.packet
    assert (s.fuel, source, counts['spent'], counts['waste'], weight) == (36,20,74,10,Q(1,36))
    assert s.witness and s.stage == 2 and s.q == 0 and s.life == 6
    assert 145 == p['preparation_spent']+law.adapter+counts['spent']+counts['waste']+s.fuel+source
    return dict(original_energy=145, preparation_spent=p['preparation_spent'],
                old_adapter_spent=law.adapter, operational_spent=counts['spent'],
                waste=counts['waste'], fuel=s.fuel, source=source,
                probability=str(weight), commissioning_probability='2/9',
                unsuccessful_preparation_probability='7/9',
                initial_blank_workspace_cartridges=1, inherited_state=asdict(s),
                preparation_record=p, path=history,
                source_hashes={str(Path(mod.__file__).relative_to(ROOT)):digest(Path(mod.__file__))
                               for mod in (pred,pred.upstream,pred.upstream.old,
                                           pred.upstream.old.arithmetic)})


def classify(result, target):
    result['analyst_distinguishing_word'] = (None if result['model'] is None else
        distinguishing_word(target, from_record(result['model'])))
    result['analyst_model_exact'] = result['model'] is not None and result['analyst_distinguishing_word'] is None
    result['analyst_model_minimal'] = result['model'] is not None and minimal(from_record(result['model']))
    return result


def run():
    inherited = inherited_history()
    unary = m.Machine(('a',),(0,0,1),((1,),(2,),(0,)))
    binary = m.Machine(('a','b'),(0,0,1),((1,0),(2,0),(0,0)))
    scenarios = {
        'primary_unary': (unary, {}),
        'binary_same_resources': (binary, {}),
        'fourfold_tariffs': (unary, {'tariff': m.Tariff(scale=Q(4))}),
        'capacity_48': (unary, {'capacity':48}),
        'installation_unfunded': (unary, {'fuel':5}),
        'retention_unfunded': (unary, {'tariff':replace(m.Tariff(),final_rent=Q(100))}),
        'frozen_first_candidate': (unary, {'frozen':True}),
        'false_bound_one': (unary, {'bound':1}),
        'inverted_sensor': (unary, {'invert':True}),
        'broken_reset': (unary, {'broken_reset':True}),
    }
    results = {}
    for name,(target,kw) in scenarios.items():
        results[name] = classify(m.acquisition(target, **kw), target)
    primary = results['primary_unary']
    assert primary['status'] == 'complete' and primary['retained'] and primary['analyst_model_exact']
    assert primary['analyst_model_minimal']
    assert [len(h['outputs']) for h in primary['hypotheses']] == [1,3]
    assert primary['trace'] == [dict(kind='prediction_failure',word='aa',predicted=0,observed=1),
                                dict(kind='distinction',histories=['','a'],suffix='a',observations=[0,1])]
    assert primary['use']['word'] == 'aaaaa' and primary['max_observed_length'] == 4
    assert primary['use']['success'] and primary['use']['source'] == 10
    assert primary['use']['word'] not in [q['word'] for q in primary['queries']]
    assert Q(primary['spent'])+Q(primary['fuel']) == 36
    assert 145 == 4+1+74+10+Q(primary['spent'])+Q(primary['use']['fuel_after_return'])+10
    assert not results['binary_same_resources']['certified']
    assert not results['fourfold_tariffs']['retained']
    assert not results['capacity_48']['retained']
    assert results['installation_unfunded']['spent'] == '0'
    assert results['retention_unfunded']['certified'] and not results['retention_unfunded']['retained']
    assert results['frozen_first_candidate']['status'] == 'frozen_after_prediction_failure'
    assert results['false_bound_one']['certified'] and not results['false_bound_one']['analyst_model_exact']
    assert results['inverted_sensor']['certified'] and not results['inverted_sensor']['analyst_model_exact']
    assert not results['inverted_sensor']['use']['success']

    # Sharp liquidity boundary for this fixed completed schedule. These are
    # controlled prior-withdrawal counterfactuals, not new source credit.
    needed = Q(primary['spent'])
    for name,fuel in [('exact_schedule_budget',needed),('one_tick_short',needed-Q(1,65536))]:
        r = classify(m.acquisition(unary,fuel=fuel),unary)
        r['prior_withdrawal'] = str(36-fuel)
        results[name] = r
    assert results['exact_schedule_budget']['status'] == 'complete'
    assert results['exact_schedule_budget']['fuel'] == '0'
    assert results['one_tick_short']['status'] == 'funding:extraction_work'
    assert results['one_tick_short']['use'] is None

    # Mathematical runs with separately declared large laboratory provision,
    # distinct from the inherited36-unit actual-join runs. No hidden table is
    # given to a learner, only TargetPort.query; full tables are analyst checks.
    exhaustive = Counter()
    maximum = dict(spent=Q(0), peak=0)
    for n in range(1,4):
        for successors in product(range(n),repeat=n):
            for outputs in product((0,1),repeat=n):
                target = m.Machine(('a',),outputs,tuple((s,) for s in successors))
                r = m.acquisition(target,fuel=10000,capacity=4096,bound=3,use=False,audit=False)
                assert r['certified'] and r['retained'], r['status']
                learned = from_record(r['model'])
                assert distinguishing_word(target,learned) is None
                assert minimal(learned)
                assert all(len(b['outputs']) > len(a['outputs']) for a,b in zip(r['hypotheses'],r['hypotheses'][1:]))
                exhaustive[f'states_{n}'] += 1
                if Q(r['spent']) <= 36 and r['peak_cells'] <= 256:
                    exhaustive['fits_inherited_acquisition_budget'] += 1
                maximum['spent'] = max(maximum['spent'],Q(r['spent']))
                maximum['peak'] = max(maximum['peak'],r['peak_cells'])
    assert [exhaustive[f'states_{n}'] for n in range(1,4)] == [2,16,216]
    return dict(scope='synthetic conditional resource join and standard mathematical learner',
                inherited=inherited, tariffs={k:str(v) for k,v in asdict(m.Tariff()).items()},
                cases=results, exhaustive=dict(exhaustive),
                exhaustive_maximum={k:str(v) for k,v in maximum.items()},
                primary_target=unary.record(), binary_target=binary.record(),
                binary_observation_lower_bound='40',
                source_hashes={p.name:digest(p) for p in [HERE/'model.py',HERE/'check.py',HERE/'PROTOCOL.md']})


if __name__ == '__main__':
    result = run()
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(cases={k:{q:v[q] for q in ('status','certified','retained','spent','peak_cells')}
                                     for k,v in result['cases'].items()},
                          exhaustive=result['exhaustive'],maximum=result['exhaustive_maximum']),indent=2))
