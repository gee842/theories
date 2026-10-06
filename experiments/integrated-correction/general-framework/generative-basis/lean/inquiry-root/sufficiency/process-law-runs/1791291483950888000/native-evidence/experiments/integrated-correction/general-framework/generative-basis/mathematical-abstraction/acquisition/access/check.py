"""Actual acquisition handoff, diagnostic families and boundary controls."""
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json
import sys
import diagnosis as d

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def actual_handoff():
    # Load the unchanged predecessor producer under its own original dependency.
    saved = sys.modules.get('model')
    sys.modules['model'] = d.acquisition
    spec = importlib.util.spec_from_file_location('_access_prior_check',HERE.parent/'check.py')
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    if saved is None:
        del sys.modules['model']
    else:
        sys.modules['model'] = saved
    original = parent.inherited_history()
    target = d.acquisition.Machine(('a',),(0,0,1),((1,),(2,),(0,)))
    meter = d.acquisition.Meter(original['fuel'])
    port = d.acquisition.TargetPort(target,meter)
    learner = d.acquisition.Learner(target.alphabet,3,port.query,meter)
    learner.run()
    used = port.use(learner.plan_novel_use(),original['source'])
    assert learner.retained and not learner.cache and not learner.S and not learner.E
    assert meter.live == 15 and port.state == 2 and used['source'] == 10
    fuel = Q(used['fuel_after_return'])
    assert fuel == Q(1030367,65536)
    assert Q(145) == 89+meter.spent+fuel+used['source']
    return learner.machine, dict(original_history=original,old_acquisition_spent=str(meter.spent),
        fuel=str(fuel),source=used['source'],environment_phase=port.state,
        learned_machine=learner.machine.record(),live_cells=meter.live,capacity=256,
        old_discarded_archive_sizes=[len(learner.S),len(learner.E),len(learner.cache)],
        source_hashes={**original['source_hashes'],
                      str((HERE.parent/'model.py').relative_to(ROOT)):digest(HERE.parent/'model.py'),
                      str((HERE.parent/'check.py').relative_to(ROOT)):digest(HERE.parent/'check.py')})


def event_capital(events):
    spent = received = threshold = Q(0)
    for event in events:
        if event['kind'] == 'actual_arrival':
            received += event['amount']
        else:
            spent += Q(event['bill'])
            threshold = max(threshold,spent-received)
    return threshold


def audit_result(r,handoff,withdrawal=Q(0)):
    assert Q(r['starting_fuel'])+Q(r['income']) == Q(r['spent'])+Q(r['fuel'])
    assert Q(r['income'])+r['wasted']+r['source_remaining'] == 10
    assert Q(145) == (89+Q(handoff['old_acquisition_spent'])+withdrawal+
                      Q(r['spent'])+Q(r['fuel'])+r['source_remaining']+r['wasted'])
    if r['status'] != 'complete':
        assert not r['retained'] and r['verdict'] is None


def summarize(r):
    return {k:r[k] for k in ('status','retained','verdict','spent','fuel','income',
                              'source_remaining','wasted','peak_cells')}


def run():
    H,handoff = actual_handoff()
    fuel = Q(handoff['fuel'])
    family = []
    for factored,count in ((False,8),(True,16)):
        for probe in (False,True):
            for code in range(count):
                tau,sigma,broken,blocked = d.flags(code)
                for phase in range(3):
                    r=d.diagnose(H,fuel,10,phase,target_flip=tau,sensor_flip=sigma,
                        broken_reset=broken,blocked=blocked,probe=probe,factored_access=factored)
                    audit_result(r,handoff)
                    expected=(code,r['physical_phase'])
                    effective={(c,q) for c,q in r['final_belief']}
                    if r['blocked_factor'] is not None:
                        effective={(c+8*b,q) for c,q in effective for b in (0,1)}
                    # Only failures after the final fully committed update
                    # occur in this particular family sweep (retention).
                    assert expected in effective,(code,phase,r['status'])
                    if r['retained']:
                        if not probe:
                            assert r['verdict']['status']=='ambiguous'
                            assert len(effective)==(4 if factored else 2)
                            assert r['source_remaining']==10
                        elif not factored:
                            assert r['verdict']['status']=='unique' and len(effective)==1
                        elif Q(r['income'])>0:
                            assert r['verdict']['status']=='unique' and len(effective)==1
                        else:
                            assert r['verdict']['status']=='ambiguous' and len(effective)==3
                    family.append(dict(factored=factored,probe=probe,template=code,
                                       initial_phase=phase,result=summarize(r)))
    summaries={}
    for factored in (False,True):
        for probe in (False,True):
            rows=[r['result'] for r in family if r['factored']==factored and r['probe']==probe]
            name=('factored_48' if factored else 'base_24')+('_probe' if probe else '_sensor_only')
            summaries[name]=dict(cases=len(rows),statuses=dict(Counter(r['status'] for r in rows)),
                                 maximum_spent=str(max(Q(r['spent']) for r in rows)),
                                 maximum_peak=max(r['peak_cells'] for r in rows))
    assert summaries['base_24_probe']['statuses']=={'complete':24}
    assert summaries['base_24_sensor_only']['statuses']=={'complete':24}
    assert summaries['factored_48_probe']['statuses']=={'complete':36,'funding:retain_diagnosis':12}

    four=d.acquisition.Machine(('a',),(0,0,0,1),((1,),(2,),(3,),(0,)))
    scenarios={
      'primary_sensor_flip':dict(sensor_flip=1),
      'sensor_only_ambiguity':dict(sensor_flip=1,probe=False),
      'readiness_change':dict(target_flip=1),
      'reset_failure':dict(broken_reset=1),
      'combined_faults':dict(target_flip=1,sensor_flip=1,broken_reset=1),
      'literal_expanded_capacity_failure':dict(expanded=True,blocked=1),
      'factored_access_ambiguity':dict(factored_access=True,blocked=1),
      'factored_positive_receipt':dict(factored_access=True,sensor_flip=1),
      'omitted_transfer_blockage':dict(blocked=1),
      'inverted_consequence_receipt':dict(receipt_flip=1),
      'fourth_phase_detected':dict(environment_model=four,physical_state=0),
      'fourth_phase_not_rejected':dict(environment_model=four),
      'installation_unfunded':dict(fuel=1),
      'small_capacity':dict(capacity=100),
      'double_prices':dict(tariff=d.Tariff(scale=Q(2))),
      'receipt_unfunded_after_transfer':dict(tariff=d.Tariff(receipt=Q(100))),
    }
    fixtures={}
    for name,kwargs in scenarios.items():
        arguments=dict(fuel=fuel,source=10,physical_state=handoff['environment_phase'])
        arguments.update(kwargs)
        r=d.diagnose(H,**arguments)
        withdrawal=fuel-Q(arguments['fuel'])
        audit_result(r,handoff,withdrawal)
        r['prior_withdrawal']=str(withdrawal)
        fixtures[name]=r
    primary=fixtures['primary_sensor_flip']
    assert primary['retained'] and primary['verdict']['agrees']['sensor_flip']==[1]
    assert primary['verdict']['agrees']['readiness_flip']==[0]
    assert primary['spent']=='934043/65536' and primary['source_remaining']==0
    assert fixtures['readiness_change']['wasted']==10
    assert fixtures['sensor_only_ambiguity']['source_remaining']==10
    assert fixtures['literal_expanded_capacity_failure']['status']=='capacity:prepare_read'
    assert len(fixtures['factored_access_ambiguity']['verdict']['alternatives'])==3
    assert fixtures['fourth_phase_detected']['status']=='model_family_inadequate'
    assert fixtures['fourth_phase_not_rejected']['retained']
    for name in ('omitted_transfer_blockage','inverted_consequence_receipt'):
        assert fixtures[name]['verdict']['agrees']['readiness_flip']==[1]
        assert fixtures[name]['verdict']['agrees']['sensor_flip']==[1]
    unreceived=fixtures['receipt_unfunded_after_transfer']
    assert unreceived['status']=='funding:arrival_receipt' and unreceived['source_remaining']==0
    assert unreceived['income']=='10' and unreceived['native_trace'][-1]['observation']=='receipt_not_acquired'
    assert not unreceived['retained'] and len(unreceived['final_belief'])==2

    needed=event_capital(primary['events'])
    for name,budget in [('exact_prefix_budget',needed),('one_unit_short',needed-Q(1,65536))]:
        r=d.diagnose(H,budget,10,2,sensor_flip=1)
        r['prior_withdrawal']=str(fuel-budget)
        audit_result(r,handoff,fuel-budget)
        fixtures[name]=r
    assert fixtures['exact_prefix_budget']['retained']
    assert fixtures['one_unit_short']['status']=='funding:native_probe'
    assert fixtures['one_unit_short']['source_remaining']==10
    return dict(scope='conditional synthetic access diagnosis; declared fault family and tariffs',
      handoff=handoff,family_summaries=summaries,family=family,fixtures=fixtures,
      primary_minimum_initial_fuel=str(needed),
      source_hashes={p.name:digest(p) for p in (HERE/'diagnosis.py',HERE/'check.py',HERE/'PROTOCOL.md')})


if __name__=='__main__':
    result=run()
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(families=result['family_summaries'],fixtures={name:r['status'] for name,r in result['fixtures'].items()},
                         primary_minimum_initial_fuel=result['primary_minimum_initial_fuel']),indent=2))
