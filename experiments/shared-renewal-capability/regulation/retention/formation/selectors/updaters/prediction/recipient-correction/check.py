"""Check current saved distributions, exact interventions and affordability limits."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import model as m

HERE = Path(__file__).resolve().parent


def main():
    result = json.loads((HERE/'results.json').read_text())
    saved_fixture = json.loads((HERE/'fixtures.json').read_text())
    before = m.source_hashes()
    assert result['source_sha256'] == saved_fixture['source_sha256'] == before
    assert json.loads(json.dumps(m.fixtures())) == saved_fixture['fixtures']
    arms = metrics = 0
    for name, case in m.cases().items():
        current = result['cases'][name]
        assert current['law'] == case
        for producer in m.PRODUCERS:
            outputs = current['producers'][producer]
            for arm in m.ARMS:
                expected = m.compare(case, arm, producer, saved_fixture['fixtures'][str(case['initial_common'])])
                assert outputs[arm] == expected, (name, producer, arm)
                arms += 1; metrics += len(expected['metrics'])
            assert outputs['indexed'] == outputs['conventional']
        assert current['producers']['variable'] == current['producers']['conventional']
    primary = result['cases']['primary']['producers']['variable']
    metric = lambda case, arm, name: Q(result['cases'][case]['producers']['variable'][arm]['metrics'][name])
    assert metric('primary','indexed','strict_witness') == Q(1,9)
    assert metric('primary','shared','recipient_captures') == 0
    assert metric('primary','shared_cheap','actor_captures') == 0
    for a in ('private_only','private_as_recipient','frozen'):
        assert metric('primary',a,'final_actor') == metric('primary','indexed','final_actor')
        assert metric('primary',a,'spent') == metric('primary','indexed','spent')
    assert metric('primary','private_only','recipient_captures') == 0
    assert metric('primary','private_as_recipient','recipient_correction') == Q(1,9)
    assert metric('primary','private_as_recipient','strict_witness') == 0
    assert metric('primary','private_as_recipient','decoder_errors') == Q(1,9)
    assert metric('same_law','private_as_recipient','recipient_captures') < metric('same_law','indexed','recipient_captures')
    assert metric('same_law','shared_cheap','final_actor') > metric('same_law','indexed','final_actor')
    for a in m.ARMS:
        assert result['cases']['primary']['producers']['variable'][a]['metrics'] == result['cases']['target_swapped']['producers']['variable'][a]['metrics']
    for name in ('missing_channel','target_alias','low_reserve','expensive_write'):
        assert metric(name,'indexed','strict_witness') == 0
    assert metric('recipient_outage','indexed','strict_witness') == Q(1,12)
    assert metric('recipient_outage','indexed','decoder_errors') == Q(1,36)
    assert metric('expensive_write','indexed','recipient_correction') == Q(1,9)
    witness = primary['indexed']['witness']
    assert witness['predecessor']['state']['fuel'] == 21
    assert [e['capture'] for e in witness['trace']] == [False,True,True,True]
    assert witness['state']['fuel'] == 9 and witness['state']['recipient'] == 10
    assert 151 == 4+1+65+20+32+10+9+10
    private_account_checks = 0
    fs = saved_fixture['fixtures']['30']
    for producer in m.PRODUCERS:
        for rows in fs['prefix_records'][producer].values():
            for row in rows:
                [(p1, informed, cm1, _)] = m.suffix(m.cases()['primary'], 'indexed', row['state'], row['final_regime'])
                for other in ('private_only', 'frozen'):
                    [(p2, blind, cm2, _)] = m.suffix(m.cases()['primary'], other, row['state'], row['final_regime'])
                    assert p1 == p2 == 1
                    assert (informed['fuel'], informed['active']) == (blind['fuel'], blind['active'])
                    for name in ('spent', 'actor_captures', 'trials', 'evidence', 'writes'):
                        assert cm1[name] == cm2[name], (producer, other, name)
                    private_account_checks += 1
    boundary_checks = 0
    law = m.cases()['primary']
    for bit in (0,1):
        for fuel in range(51):
            state = dict(witness['predecessor']['state'], fuel=fuel, q=4*bit, last=bit)
            [(p, out, counts, trace)] = m.suffix(law, 'indexed', state, bit)
            assert p == 1
            assert bool(counts['strict_witness']) == (fuel >= 20)
            if fuel >= 20:
                assert out['fuel'] == fuel-12 and out['recipient'] == 10
                assert counts['actor_command_changed'] == 0
            if fuel == 3:
                assert out['fuel'] == 1 and not out['installed'] and counts['spent'] == 2
            if fuel == 4:
                assert not out['active'] and counts['trials'] == 0
            if fuel == 9:
                assert trace[0]['action'] is not None and trace[0]['label'] is None
            if fuel == 10:
                assert trace[0]['label'] is not None and not trace[0]['paid_write']
                assert trace[0]['q_after'] == trace[0]['q_before']
            if fuel == 11:
                assert trace[0]['paid_write'] and trace[0]['q_after'] != trace[0]['q_before']
            boundary_checks += 1
    assert m.source_hashes() == before
    record = dict(status='passed', case_arms=arms, metric_comparisons=metrics,
                  boundary_checks=boundary_checks, private_account_checks=private_account_checks, source_sha256=before,
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  data_sha256={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('fixtures.json','results.json')},
                  scope='Producer replay, original-preparation fixture equality, full final distributions, exact conventional equality, interferences and explicit price/channel countercases; independent check is separate.')
    (HERE/'check.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k: record[k] for k in ('status','case_arms','metric_comparisons','boundary_checks')}))


if __name__ == '__main__':
    main()
