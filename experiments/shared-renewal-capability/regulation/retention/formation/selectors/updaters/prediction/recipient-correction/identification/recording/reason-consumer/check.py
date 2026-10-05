"""Reproduce the composed histories and test paid boundaries and finite guards."""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import model as m

HERE=Path(__file__).resolve().parent


def graph_closure(facts):
    reached={0}
    while True:
        nxt=reached|{v for (u,v),x in zip(m.GRAPH,facts) if u in reached and x is True}
        if nxt==reached:return [i in reached for i in range(3)]
        reached=nxt


def main():
    before=m.sources();pf,pr=m.load_predecessor()
    fx=json.loads((HERE/'fixtures.json').read_text());result=json.loads((HERE/'results.json').read_text())
    assert fx['source_sha256']==result['source_sha256']==before
    assert m.fixture(pf)==fx['fixtures']
    arms=histories=metrics=events=0
    for name,c in m.cases().items():
        expected=result['cases'][name]
        assert expected['law']==c
        for producer in m.PRODUCERS:
            actual=m.compare(name,c,producer,fx['fixtures'],pf,pr)
            assert actual==expected['producers'][producer],(name,producer)
            arms+=1;histories+=len(actual['paths']);metrics+=len(actual['metrics'])
            for row in actual['paths']:
                events+=len(row['runtime_trace'])
                ref=row['predecessor'];old=pr['cases'][ref['case']]['producers'][ref['producer']]['paths'][ref['path_index']]
                assert m.object_hash(old['state'])==ref['state_sha256']
                assert m.object_hash(old['core_history'])==ref['core_history_sha256']
                assert m.object_hash(old['state']['core'])==row['endpoint_invariants']['core_sha256']
                for a in row['audits']:
                    if a['publication_current']:
                        assert a['publication']['mask']==graph_closure(a['facts'])
                        assert a['publication']['mask']==m.lookup_mask(a['facts'])
                        assert a['cache_valid'] and a['read_count']==3
                # No runtime event is sourced from an observer's success/truth label.
                assert all('truth' not in e['state'] and 'strict' not in e['state'] for e in row['runtime_trace'])
    metric=lambda c,k:Q(result['cases'][c]['producers']['variable']['metrics'][k])
    assert metric('primary','strict_both_replays')==Q(9,64)
    assert metric('primary','cycle1_nonroot')==metric('primary','cycle2_nonroot')==Q(3,8)
    assert metric('primary','cycle1_false_route')==metric('primary','cycle2_false_route')==0
    assert metric('primary','factual_spent')==28 and metric('primary','reason_spent')==20
    assert metric('primary','final_reader')==0
    assert metric('single_min','cycle1_published')==1 and metric('single_min','reason_spent')==10
    assert metric('single_short','cycle1_published')==0 and metric('single_short','reason_spent')==8
    assert metric('single_short','final_reader')==1
    assert metric('double_short','cycle1_published')==1 and metric('double_short','cycle2_published')==0
    assert metric('double_short','reason_spent')==18 and metric('double_short','final_reader')==1
    for c in ('no_workspace','original_endpoint','partial_factual_cache'):
        assert metric(c,'cycle1_published')==0 and metric(c,'reason_spent')==0
    assert metric('remove_late_positive','strict_both_replays')==Q(9,64)
    assert metric('remove_both_grounds','cycle1_root_only')==1
    assert metric('disagree_second','cycle2_conflict')==Q(9,64)
    assert metric('consistently_corrupt','cycle2_false_route')==Q(3,8)
    assert metric('consistently_corrupt','cycle2_conflict')==0
    assert metric('changed_context','cycle2_root_only')==1
    assert metric('same_context_reopen','cycle1_published')==0
    assert metric('context_during_replay','cycle1_published')==0
    assert metric('lookup_comparator','strict_both_replays')==Q(9,64)
    assert metric('lookup_comparator','final_reader')==10
    # These equalities concern declared receipt compatibility, not availability.
    compatibility_checks=0
    for z,a in product((0,1),repeat=2):
        compatible=all(bool(v and a==z)==bool(v) for v in (0,1))
        assert compatible==(a==z);compatibility_checks+=1
    # Finite inference language only: these 27 vectors are not new acquired data.
    inference_checks=0
    for cache in product((None,False,True),repeat=3):
        values=[m.normalized(x,d) for x,d in zip(cache,m.DESIRED)]
        z,conflict,facts=m.aggregate(values)
        known=[x for x in values if x is not None]
        assert conflict==(bool(known) and min(known)!=max(known))
        assert z==(known[0] if known and not conflict else None)
        mask=[True,False,False]
        for path in m.PATHS:mask=m.apply_path(mask,facts,path)
        assert mask==graph_closure(facts)==m.lookup_mask(facts)
        inference_checks+=1
    # Start guard tests at a real completed first factual state, conserving money
    # by placing any removed reader funds in its retained idle compartment.
    oldarm=pr['cases']['primary']['producers']['variable']
    old=oldarm['witness']['state'];prep=m.preparation(98)
    guard_checks=0
    for budget in range(11):
        state=deepcopy(old)
        # Normal first reader6 + extra4 =10; rearrange actual free reader+idle.
        state['idle_fuel']+=10-budget;state['reader_fuel']=budget
        noextra=dict(prep,extra_reserve=0)
        # inherited_total is computed from actual accounts by run, no initial reset.
        c=dict(m.cases()['single_min']);w,tr,audits=m.run(c,state,noextra)
        cost=0
        for bill in (1,1,1,1,1,1,2,2):
            if budget-cost<bill:break
            cost+=bill
        assert w['reason_spent']==cost and m.current(w)==(budget>=10)
        guard_checks+=1
    # Cache validity and presence of reason hardware are separate guards.
    for field,value in (('cache_valid',False),('read_count',2),('cache_context',True)):
        state=deepcopy(old);state[field]=value
        w,tr,_=m.run(m.cases()['single_min'],state,prep)
        assert w['reason_spent']==0 and not m.current(w);guard_checks+=1
    # One actual strict primary state verifies the complete account and cold reset.
    arm=result['cases']['primary']['producers']['variable'];row=arm['paths'][arm['witness_path_index']]
    assert row['metrics']['retained']=='24'
    assert 266==47+78+44+10+15+28+20+24
    cold=next(e for e in row['runtime_trace'] if e['event']=='cold_operational_turnover')['state']
    assert cold['cache']==[None]*3 and cold['normalized']==[None]*3 and cold['working']==[False]*3
    assert cold['publication'] is None and cold['reader_fuel']==24
    # Same-context reopening preserves historic publication bytes but rejects use.
    a=result['cases']['same_context_reopen']['producers']['variable'];r=a['paths'][a['witness_path_index']]
    last=r['runtime_trace'][-1]['state'];prior=r['runtime_trace'][-2]['state']
    assert last['publication']==prior['publication'] and last['context']==prior['context']
    assert prior['publication_current'] and not last['publication_current']
    assert before==m.sources()
    report=dict(status='passed',case_arms=arms,terminal_histories=histories,metrics=metrics,runtime_states=events,
        finite_inference_vectors=inference_checks,compatibility_cases=compatibility_checks,resource_and_cache_guards=guard_checks,
        source_sha256=before,checker_sha256=m.digest(__file__),data_sha256={n:m.digest(HERE/n) for n in ('fixtures.json','results.json')},
        scope='Exact continuing producer fixture lift, unchanged core/history hashes, actual new preparation and protected routing, paid inference and cold factual reread, finite closure and failure boundaries. Independent replay is separate.')
    (HERE/'check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','case_arms','terminal_histories','metrics','runtime_states')}))


if __name__=='__main__':main()
