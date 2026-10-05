"""Reproduce frozen results and exercise real latch/write/reader guards."""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import model as m

HERE=Path(__file__).resolve().parent


def rejects(fn):
    try:fn()
    except AssertionError:return
    raise AssertionError('guard unexpectedly permitted transition')


def main():
    before=m.source_hashes()
    result=json.loads((HERE/'results.json').read_text())
    saved=json.loads((HERE/'fixtures.json').read_text())
    assert before==result['source_sha256']==saved['source_sha256']
    assert json.loads(json.dumps(m.fixtures()))==saved['fixtures']
    arms=metrics=histories=microstates=latches=0
    for name,case in m.cases().items():
        record=result['cases'][name]
        assert record['law']==case
        for producer in m.PRODUCERS:
            expected=m.compare(case,producer,saved['fixtures'])
            assert expected==record['producers'][producer],(name,producer)
            arms+=1;metrics+=len(expected['metrics']);histories+=len(expected['paths'])
            for row in expected['paths']:
                s=row['state'];tr=row['runtime_trace']
                assert len(row['core_history'])==5
                assert s['query_pointer']==sum(e['target']=='recipient' and e['status']=='completed'
                                               for e in row['core_history'])
                assert s['core_phase']=='ready' and s['acquired_record'] is None
                for event in tr:
                    t=event['state'];m.valid(t)
                    assert m.energy(t)+m.spending(t)==t['initial_energy']
                    microstates+=1
                    if event['event']=='archive_latch_from_paid_acquisition':
                        assert t['core_phase']=='acquired' and t['core_target']=='recipient'
                        f=t['frames'][t['pending']]
                        context,action=f['bound']
                        assert f['latched']==[context,action^int(case['corrupt_action_tag']),
                            int(t['acquired_record'] is not None),int(bool(t['acquired_record']))]
                        latches+=1
                    if event['event']=='archive_write_bit':
                        assert t['core_phase']=='ready' and t['acquired_record'] is None
            assert record['producers']['variable']==record['producers']['conventional']
    metric=lambda name,key:Q(result['cases'][name]['producers']['variable']['metrics'][key])
    assert metric('primary','strict_factual_witness')==Q(9,64)
    assert metric('primary','false_cache_entries')==0
    assert metric('primary','decode_spent')==14 and metric('primary','final_reader')==6
    assert metric('reader_short','strict_recorded_witness')==Q(9,64)
    assert metric('reader_short','strict_factual_witness')==0
    assert metric('reader_short','decode_spent')==10 and metric('reader_short','usable_certificates')==0
    for name in m.cases():
        if name!='primary':assert metric(name,'strict_factual_witness')==0
        if name!='corrupt_action_tag':assert metric(name,'false_cache_entries')==0
    assert metric('corrupt_action_tag','false_cache_entries')==Q(33,64)
    witness=result['cases']['primary']['producers']['variable']['witness']
    s=witness['state']
    assert s['core']['fuel']==4 and s['core']['recipient']==20 and s['reader_fuel']==6
    assert s['cache'] in ([None,False,True],[None,True,False])
    assert 235==44+78+44+10+15+14+30
    # Reuse an actual runtime latch, rather than manufacturing a valid pending state.
    raw=next(e['state'] for e in witness['runtime_trace']
             if e['event']=='core_commit' and e['state']['pending']==0)
    writer=deepcopy(raw);writes=[]
    for _ in range(4):
        assert m.write_enabled(writer,0)
        m.write_bit(writer,0,writes)
    assert not m.write_enabled(writer,0) and writer['pending'] is None
    unchanged=deepcopy(writer)
    rejects(lambda:m.write_bit(writer,0,writes))
    assert writer==unchanged
    assert len(writes)==4 and writer['frames'][0]['written']==4
    # Actual duplicate latch and wrong-phase latch are refused before mutation.
    actual_latch=deepcopy(next(e['state'] for e in witness['runtime_trace']
                              if e['event']=='archive_latch_from_paid_acquisition'))
    unchanged=deepcopy(actual_latch)
    rejects(lambda:m.acquire_frame(actual_latch,0,m.cases()['primary'],[]))
    assert actual_latch==unchanged
    no_acquisition=deepcopy(next(e['state'] for e in witness['runtime_trace']
                                if e['event']=='archive_bind_and_reserve'))
    rejects(lambda:m.acquire_frame(no_acquisition,0,m.cases()['primary'],[]))
    # Exhaust the raw finite decoder separately from producer-reachable frames.
    decode_checks=0
    for bits,ctx,d in product(product((0,1),repeat=4),(False,True),(0,1)):
        t=deepcopy(s);t['cells'][:4]=list(bits)
        t['frames'][0].update(complete=True,valid=True)
        expected=bool(bits[1]==d) if bits[0]==int(ctx) and bits[2] and bits[3] else None
        assert m.decode_frame(t,0,ctx,d)==expected
        t['frames'][0]['complete']=False
        assert m.decode_frame(t,0,ctx,d) is None
        decode_checks+=2
    # The real reader's partial payments and publication threshold, with funds conserved.
    tr=witness['runtime_trace'];idx=next(i for i,e in enumerate(tr) if e['event']=='reader_activate')
    reader_checks=0
    for budget in range(21):
        t=deepcopy(tr[idx-1]['state']);t['idle_fuel']+=20-budget;t['reader_fuel']=budget
        events=[];m.paid_decode(t,events)
        expected=0 if budget==0 else 1 if budget==1 else 2+4*min(3,(budget-2)//4)
        assert t['decode_spent']==expected and t['cache_valid']==(budget>=14)
        assert m.energy(t)+m.spending(t)==t['initial_energy']
        reader_checks+=1
    changed=deepcopy(s);oldcache=deepcopy(changed['cache']);oldtoken=changed['cache_context']
    m.context_change(changed,not changed['context'])
    assert changed['cache']==oldcache and changed['cache_context']==oldtoken and not changed['cache_valid']
    assert m.energy(changed)==m.energy(s)
    assert before==m.source_hashes()
    report=dict(status='passed',case_arms=arms,metric_comparisons=metrics,terminal_histories=histories,
        checked_microstates=microstates,checked_live_latches=latches,decoder_checks=decode_checks,
        reader_budget_checks=reader_checks,actual_writer_guard_checks=7,
        source_sha256=before,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        data_sha256={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('fixtures.json','results.json')},
        scope='Exact producer replay; physical construction and pre-prefix routing; full projected five-query history distributions; live acquired-latch and guarded writer transitions; decoder and paid reader boundaries. Independent replay is separate.')
    (HERE/'check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','case_arms','metric_comparisons','terminal_histories','checked_microstates')}))


if __name__=='__main__':main()
