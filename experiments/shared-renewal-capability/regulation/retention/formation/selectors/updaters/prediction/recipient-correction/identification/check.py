"""Exact producer replay and focused identification/price/escrow checks."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import model as m

HERE = Path(__file__).resolve().parent


def observed(event):
    """Accessible record; omit analyst truth and branch probability."""
    return tuple(event[k] for k in ('target','report','action','capture','receipt',
                                  'q_before','flag_before','q_after','flag_after'))


def main():
    result = json.loads((HERE/'results.json').read_text())
    saved = json.loads((HERE/'fixtures.json').read_text())
    before = m.source_hashes()
    assert result['source_sha256'] == saved['source_sha256'] == before
    assert json.loads(json.dumps(m.fixtures())) == saved['fixtures']
    arms = metrics = microsteps = 0
    for name, case in m.cases().items():
        got = result['cases'][name]
        assert got['law'] == case
        for producer in m.PRODUCERS:
            outputs = got['producers'][producer]
            for arm in m.ARMS:
                expected = m.compare(case, arm, producer, saved['fixtures'][str(case['initial_common'])])
                assert outputs[arm] == expected, (name,producer,arm)
                arms += 1; metrics += len(expected['metrics'])
                for path in expected['paths']:
                    for event in path['trace']:
                        steps = event['microstates']
                        if event['status'] != 'completed':
                            assert not steps and event['before']['fuel'] == event['after']['fuel']
                            continue
                        assert [x['phase'] for x in steps] == [
                            'rent','target_observation','reserve_feedback','work','receipt','acquire','commit']
                        assert event['before']['fuel'] >= 6+case['write']
                        assert steps[2]['escrow'] == steps[3]['escrow'] == steps[4]['escrow'] == 1+case['write']
                        assert steps[3]['fuel'] == event['before']['fuel']-(6+case['write'])
                        assert steps[5]['escrow'] == case['write'] and steps[6]['escrow'] == 0
                        assert all(x['fuel'] >= 0 and x['escrow'] >= 0 for x in steps)
                        assert (event['q_after'] & 1) == (event['q_before'] & 1)
                        if event['target'] == 'recipient':
                            assert event['after']['fuel'] == steps[3]['fuel']
                        else:
                            assert event['q_before'] == event['q_after'] and event['flag_before'] == event['flag_after']
                        microsteps += len(steps)
            assert outputs['positive'] == outputs['conventional']
        assert got['producers']['variable'] == got['producers']['conventional']
    metric = lambda case, arm, key: Q(result['cases'][case]['producers']['variable'][arm]['metrics'][key])
    assert metric('primary','positive','strict_witness') == Q(1,32)
    assert metric('noiseless','positive','strict_witness') == Q(1,18)
    assert metric('primary','positive','recipient_captures') == metric('primary','failure_label','recipient_captures') == Q(11,96)
    assert metric('primary','failure_label','final_false_qualified') == Q(7,288)
    assert metric('primary','failure_label','false_qualified_commands') == Q(1,72)
    for name in m.cases():
        if name != 'target_change':
            for k in ('false_qualification_writes','false_qualified_commands','final_false_qualified'):
                assert metric(name,'positive',k) == 0
    for name in ('no_opportunity','missing_channel','low_reserve','expensive_write','target_change'):
        assert metric(name,'positive','strict_witness') == 0
    assert metric('target_change','positive','false_qualified_commands') == Q(1,24)
    assert metric('expensive_write','positive','final_qualified') == Q(1,24)
    assert metric('expensive_write','positive','qualified_recipient_trials') == 0
    assert metric('same_law','no_exploration','recipient_captures') > metric('same_law','positive','recipient_captures')
    witness = result['cases']['primary']['producers']['variable']['positive']['witness']
    assert witness['predecessor']['state']['fuel'] == 28
    assert [e['after']['fuel'] for e in witness['trace']] == [16,18,10,12,4]
    assert [e['capture'] for e in witness['trace']] == [False,True,True,True,True]
    assert witness['predecessor']['conditional_mean_marks']['spent'] == '68'
    assert witness['predecessor']['conditional_mean_marks']['waste'] == '10'
    assert 161 == 4+1+68+10+44+10+4+20
    boundary = 0
    for bit in (0,1):
        for fuel in range(51):
            initial = dict(witness['predecessor']['state'], fuel=fuel, q=4*bit, last=bit)
            [(mass,state,c,tr)] = m.suffix(m.cases()['noiseless'],'positive',initial,bit)
            assert mass == 1
            assert bool(c['strict_witness']) == (fuel >= 26)
            assert c['trials'] == 5 if fuel >= 26 else c['trials'] < 5
            if fuel >= 26:
                assert state['fuel'] == fuel-24 and state['recipient'] == 20
            if fuel == 25:
                assert [e['status'] for e in tr] == ['completed']*3+['unaffordable','inactive']
                assert state['fuel'] == 7 and state['recipient'] == 10
            if fuel < 4:
                assert not state['installed'] and state['fuel'] == fuel and c['spent'] == 0
            if 4 <= fuel < 12:
                assert state['installed'] and c['trials'] == 0 and c['spent'] == 4
            boundary += 1
    # Same physical controller observation from a wrong action versus outage.
    initial = dict(witness['predecessor']['state'], q=0, last=0)
    wrong = m.suffix(m.cases()['noiseless'],'positive',initial,0)[0][3][0]
    outage_case = dict(m.cases()['no_opportunity'], opposite=False)
    outage = m.suffix(outage_case,'positive',initial,0)[0][3][0]
    assert wrong['true_law'] != outage['true_law']
    assert observed(wrong) == observed(outage)
    assert wrong['flag_after'] == outage['flag_after'] == 0
    assert wrong['after'] == outage['after']
    # Unknown is distinct from missing channel, and no actor bit is repaired.
    missing = m.suffix(m.cases()['missing_channel'],'positive',initial,0)[0][3][0]
    assert missing['receipt'] is None and missing['q_after'] == missing['q_before']
    update_checks = 0
    for q in range(4):
        for flag in (0,1):
            for receipt in (None,False,True):
                for target in ('actor','recipient'):
                    a = m.update('positive',q,flag,target,receipt)
                    assert a == m.update('conventional',q,flag,target,receipt)
                    assert a[0]&1 == q&1
                    if target == 'actor' or receipt is None:
                        assert a == (q,flag)
                    if target == 'recipient' and receipt is False and not flag:
                        assert a == (q^2,0)
                    if target == 'recipient' and receipt is True:
                        assert a == (q,1)
                    update_checks += 1
    # Private ledger is identical across response rules: recipient gains cannot pay it.
    private_checks = 0
    for name,data in result['cases'].items():
        for producer in m.PRODUCERS:
            baseline = data['producers'][producer]['positive']['metrics']
            for arm in m.ARMS:
                other = data['producers'][producer][arm]['metrics']
                for key in ('trials','actor_captures','spent','final_actor','unaffordable'):
                    assert baseline[key] == other[key]
                    private_checks += 1
    assert before == m.source_hashes()
    record = dict(status='passed', case_arms=arms, metric_comparisons=metrics,
                  checked_microstates=microsteps, boundary_checks=boundary,
                  update_checks=update_checks, private_account_checks=private_checks,
                  source_sha256=before,
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  data_sha256={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                               for n in ('fixtures.json','results.json')},
                  scope='Producer replay, actual imported fixture equality, full suffix paths and distributions, escrow phases, actor ledger separation, finite-state equivalence, ambiguity and price boundaries. Independent replay is separate.')
    (HERE/'check.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','case_arms','metric_comparisons','boundary_checks','update_checks')}))


if __name__ == '__main__':
    main()
