"""Producer-side artifact/account/source checks; independent review is separate."""
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())


def run():
    data = json.loads((HERE/'results.json').read_text())
    bindings = {}
    for name, expected in data['source_hashes'].items():
        actual = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        assert actual == expected, name
        bindings[name] = actual
    count = event_count = 0
    all_cases = [('ordinary' if name != 'inverted_prefix' else 'inverted', case)
                 for name, case in data['cases'].items()]
    all_cases += [(case['prefix'], case) for case in data['grid']]
    for label, case in all_cases:
        prefix, result = data['prefixes'][label], case['result']
        boundary = case['trace'][0]
        held_fuel = Q(boundary['details']['withheld_fuel'])
        held_source = boundary['details']['withheld_source']
        assert held_fuel >= 0 and held_source >= 0
        assert Q(145) == (89 + Q(prefix['spent']) + held_fuel + Q(result['spent'])
                         + Q(result['fuel']) + result['source'] + result['wasted'] + held_source)
        assert Q(prefix['fuel']) == Q(36)-Q(prefix['spent'])
        previous_spent = previous_income = Q(0)
        for event in case['trace']:
            state, a = event['state'], event['state']['account']
            p, c = state['physical'], state['controller']
            assert Q(a['fuel']) + Q(a['spent']) == Q(a['start']) + Q(a['income'])
            assert Q(a['fuel']) >= 0 and a['workspace'] >= 0
            assert Q(a['spent']) >= previous_spent and Q(a['income']) >= previous_income
            assert p['source'] + p['wasted'] + p['transferred'] + held_source == 20
            assert p['transferred'] == Q(a['income'])
            assert c['H'] == prefix['model']
            previous_spent, previous_income = Q(a['spent']), Q(a['income'])
            event_count += 1
        assert result['retained'] == (case['trace'][-1]['event'] == 'interpretation_retained')
        if result['status'] != 'complete':
            assert not result['retained']
        count += 1
    cases = data['cases']
    primary, clamp, stable = [cases[k] for k in ('primary_changed', 'primary_reader_clamped', 'stable')]
    assert primary['checkpoint'] == clamp['checkpoint']
    assert primary['checkpoint']['controller']['candidates'] == [1, 2]
    assert primary['checkpoint']['controller']['record'] == dict(sensor=1, receipt=0, valid=True)
    assert not primary['checkpoint']['controller']['retained']
    assert primary['result']['candidates'] == [1] and primary['result']['word'] == ''
    assert primary['result']['income'] == '10' and primary['result']['wasted'] == 10
    assert clamp['result']['candidates'] == [1, 2] and clamp['result']['income'] == '0'
    assert clamp['result']['wasted'] == 20
    assert stable['result']['actual_attempts'] == 1 and stable['result']['source'] == 10
    assert stable['result']['candidates'] == [0]
    assert cases['blocked']['result']['candidates'] == [2]
    assert cases['blocked']['result']['income'] == '0'
    for name in ('missing_receipt', 'interrupted_first_write'):
        assert cases[name]['result']['candidates'] == [0, 1, 2]
        assert cases[name]['result']['record'] is None
        assert cases[name]['result']['actual_attempts'] == 1
    assert cases['misleading_receipt']['result']['record']['receipt'] == 1
    assert cases['misleading_receipt']['result']['income'] == '0'
    assert cases['interrupted_final_retention']['result']['income'] == '10'
    assert not cases['interrupted_final_retention']['result']['retained']
    for name in ('sensor_mismatch', 'reset_mismatch', 'outside_family'):
        assert cases[name]['result']['status'] == 'sensory_prediction_mismatch'
        assert cases[name]['result']['source'] == 20
    assert cases['one_packet']['result']['status'] == 'source_unavailable'
    assert cases['source_exhausted']['result']['status'] == 'source_unavailable'
    assert cases['inverted_prefix']['result']['word'] == 'aa'
    assert cases['inverted_prefix']['result']['candidates'] == [1]
    assert cases['inverted_prefix']['result']['income'] == '10'
    assert len(data['grid']) == 48 and count == 65
    for case in data['grid']:
        cfg, out = case['config'], case['result']
        if cfg['tau'] != cfg['sigma']:
            assert out['status'] == 'sensory_prediction_mismatch'
            assert out['actual_attempts'] == 0
        elif cfg['receipt_mode'] == 'missing':
            assert out['status'] == 'receipt_missing'
            assert out['candidates'] == [0, 1, 2]
        elif cfg['receipt_mode'] == 'faithful':
            assert out['status'] == 'complete'
            expected = 2 if cfg['blocked'] else cfg['tau'] ^ int(case['prefix'] == 'inverted')
            assert out['candidates'] == [expected]
    return dict(status='passed', scope='producer artifact assertions; no independent implementation',
                named_cases=len(cases), grid_cases=len(data['grid']), traces=count,
                event_states=event_count, bound_sources=bindings,
                grid_statuses=dict(Counter(c['result']['status'] for c in data['grid'])),
                result_sha256=hashlib.sha256((HERE/'results.json').read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


if __name__ == '__main__':
    receipt = run()
    (HERE/'checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'bound_sources'}, indent=2))
