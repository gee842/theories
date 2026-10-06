"""Actual-history joins, finite behavioral cases and failure controls."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import permutations
import hashlib
import importlib.util
import json
import sys
import revision as r

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[7]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inherited():
    saved = sys.modules.get('diagnosis')
    sys.modules['diagnosis'] = r.access
    spec = importlib.util.spec_from_file_location('_revision_access_check', HERE.parent/'check.py')
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    if saved is None:
        del sys.modules['diagnosis']
    else:
        sys.modules['diagnosis'] = saved
    H, ancestry = parent.actual_handoff()
    args = dict(fuel=Q(ancestry['fuel']), source=ancestry['source'],
                physical_state=ancestry['environment_phase'])
    four = r.Machine(('a',), (0,0,0,1), ((1,),(2,),(3,),(0,)))
    previous = {
        'sensor_probe': r.access.diagnose(H, **args, sensor_flip=1),
        'sensor_only': r.access.diagnose(H, **args, sensor_flip=1, probe=False),
        'historical_four': r.access.diagnose(H, **args, environment_model=four),
    }
    for p in previous.values():
        parent.audit_result(p, ancestry)
        assert p['retained'] and p['status'] == 'complete'
    return H, ancestry, previous, four


def arguments(H, p, environment, parity):
    return dict(H=H, old_belief=p['final_belief'], fuel=Q(p['fuel']),
                initial_live=p['events'][-1]['live'], source=p['source_remaining'],
                environment=environment, physical_state=p['physical_phase'], parity=parity)


def audit(x, p, ancestry, withdrawal=Q(0)):
    assert Q(x['starting_fuel']) == Q(x['spent'])+Q(x['fuel'])
    assert x['source_remaining'] == p['source_remaining']
    assert Q(145) == (89+Q(ancestry['old_acquisition_spent'])+Q(p['spent'])+
                      p['wasted']+withdrawal+Q(x['spent'])+Q(x['fuel'])+x['source_remaining'])
    if x['retained']:
        assert x['status'] == 'complete' and x['acquired_retained'] and x['use_confirmed']


def summary(x):
    return {k:x[k] for k in ('status','retained','acquired_retained','use_confirmed',
                            'selected','spent','fuel','source_remaining','peak_cells')}


def rename(H, permutation):
    n=len(H.outputs)
    outs=[None]*n
    transitions=[None]*n
    for q in range(n):
        outs[permutation[q]]=H.outputs[q]
        transitions[permutation[q]]=(permutation[H.transitions[q][0]],)
    return r.Machine(H.alphabet,tuple(outs),tuple(transitions),permutation[H.initial])


def run():
    H, ancestry, previous, four = inherited()
    p = previous['sensor_probe']
    expanded = r.stutter(H)
    five = r.Machine(('a',), (0,0,0,0,1), ((1,),(2,),(3,),(4,),(0,)))
    alternator = r.Machine(('a',), (0,1), ((1,),(0,)))
    cases = {
        'unchanged_current_model': (p, arguments(H,p,H,1)),
        'declared_phase_insertion': (p, arguments(H,p,expanded,1)),
        'sensor_only_resource_boundary': (previous['sensor_only'],arguments(H,previous['sensor_only'],H,1)),
        'actual_old_four_phase_failure': (previous['historical_four'],arguments(H,previous['historical_four'],four,0)),
        'small_capacity': (p, dict(arguments(H,p,H,1),capacity=80)),
        'doubled_prices': (p, dict(arguments(H,p,expanded,1),tariff=r.access.Tariff(scale=Q(2)))),
        'five_read_limit': (p, dict(arguments(H,p,H,0),physical_state=H.initial,max_reads=5)),
        'outside_family_five_phase_zero': (p, dict(arguments(H,p,five,0),physical_state=0)),
        'outside_family_five_phase_one': (p, dict(arguments(H,p,five,0),physical_state=1)),
        'outside_family_alternator': (p, dict(arguments(H,p,alternator,0),physical_state=0)),
    }
    fixtures={}
    for name,(prior,args) in cases.items():
        x=r.revise(**args)
        audit(x,prior,ancestry)
        fixtures[name]=x
    # A late parity change is declared by native-command count derived from
    # the completed unchanged schedule, not selected by observing the fault.
    count=len(fixtures['unchanged_current_model']['native_trace'])
    x=r.revise(**dict(arguments(H,p,H,1),switch_after=count-1))
    audit(x,p,ancestry)
    fixtures['change_before_forward_read']=x

    family=[]
    for k,target in enumerate((H,expanded)):
        for parity in (0,1):
            for phase in range(len(target.outputs)):
                x=r.revise(**dict(arguments(H,p,target,parity),physical_state=phase))
                audit(x,p,ancestry)
                if x['retained']:
                    assert x['selected']['family']==k
                    assert x['selected']['state']==x['physical_phase']
                    assert x['selected']['parity']==parity
                family.append(dict(family=k,initial_phase=phase,parity=parity,result=summary(x)))
    statuses=dict(Counter(x['result']['status'] for x in family))

    # Semantic all-class assay is independent of inherited affordability.
    ample=[]
    for k,target in enumerate((H,expanded)):
        for parity in (0,1):
            for phase in range(len(target.outputs)):
                x=r.revise(**dict(arguments(H,p,target,parity),fuel=Q(100),physical_state=phase))
                assert x['retained'] and x['selected']['family']==k
                assert x['selected']['state']==x['physical_phase'] and x['selected']['parity']==parity
                ample.append(dict(family=k,initial_phase=phase,parity=parity,result=summary(x)))

    # Derived schedule budget controls withdraw an explicit prior reserve.
    primary=fixtures['declared_phase_insertion']
    need=Q(primary['spent'])
    for name,fuel in (('exact_schedule_budget',need),('one_unit_short',need-Q(1,65536))):
        x=r.revise(**dict(arguments(H,p,expanded,1),fuel=fuel))
        audit(x,p,ancestry,Q(p['fuel'])-fuel)
        fixtures[name]=x
    assert fixtures['exact_schedule_budget']['retained']
    assert not fixtures['one_unit_short']['retained']

    before_cursor = Q(0)
    for event in primary['events']:
        if event['kind']=='commit_use_cursor':
            break
        before_cursor += Q(event['bill'])
    x=r.revise(**dict(arguments(H,p,expanded,1),fuel=before_cursor))
    audit(x,p,ancestry,Q(p['fuel'])-before_cursor)
    assert x['status']=='funding:commit_use_cursor'
    assert x['selected']['state'] != x['physical_phase']
    fixtures['cursor_commit_unfunded']=x

    relabel=[]
    for perm in permutations(range(3)):
        renamed=rename(H,perm)
        old=[(c,perm[q]) for c,q in p['final_belief']]
        x=r.revise(renamed,old,Q(p['fuel']),25,0,r.stutter(renamed),perm[p['physical_phase']],1)
        assert x['native_trace']==primary['native_trace']
        assert x['spent']==primary['spent'] and x['peak_cells']==primary['peak_cells']
        assert x['retained']==primary['retained']
        if x['selected'] is not None:
            actual=x['physical_phase']
            assert x['selected']['state']==actual
        relabel.append(list(perm))

    # Existing installed diagnosis can expose the old out-of-class error,
    # without inventing the funds required for a new revision installation.
    old=previous['historical_four']
    a=r.access.Account(Q(old['fuel']),initial_live=25)
    port=r.access.Port(four,old['physical_phase'],0,a)
    controller=r.access.Diagnoser(H,port.command,a)
    controller.belief=[tuple(x) for x in old['final_belief']]
    challenge_status='complete'
    try:
        controller.step('read')
    except r.Halt as error:
        challenge_status=str(error)
    assert challenge_status=='model_family_inadequate' and not controller.belief
    challenge=dict(status=challenge_status,fuel=str(a.fuel),spent=str(a.spent),
                   live_cells=a.live,final_belief=[],native_trace=port.trace,events=a.events)
    assert Q(old['fuel']) == Q(challenge['fuel'])+Q(challenge['spent'])

    result=dict(scope='conditional fresh current-family revision; historical replay not claimed',
                ancestry=ancestry,prior_access=previous,
                supplied_generated_model=expanded.record(),
                family=family,family_statuses=statuses,fixtures=fixtures,
                ample_assay=dict(fuel='100',cases=ample),relabelings=relabel,
                existing_controller_challenge=challenge,
                source_hashes={name:digest(HERE/name) for name in ('revision.py','check.py','PROTOCOL.md')},
                inherited_hashes={**ancestry['source_hashes'],
                    str((HERE.parent/'diagnosis.py').relative_to(ROOT)):digest(HERE.parent/'diagnosis.py'),
                    str((HERE.parent/'check.py').relative_to(ROOT)):digest(HERE.parent/'check.py')})
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(family_statuses=statuses,fixtures={k:summary(v) for k,v in fixtures.items()},
                         maximum_ample_cost=str(max(Q(x['result']['spent']) for x in ample)),
                         challenge={k:v for k,v in challenge.items() if k not in ('events',)}),indent=2))


if __name__=='__main__':
    run()
