"""Actual endpoint limits and a separate finite retention countermodel."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import product
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[8]
spec=importlib.util.spec_from_file_location('_meta_revision_impl',HERE.parent/'revision.py')
r=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=r
spec.loader.exec_module(r)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def previous_module():
    saved=sys.modules.get('revision')
    sys.modules['revision']=r
    spec=importlib.util.spec_from_file_location('_meta_previous_check',HERE.parent/'check.py')
    previous=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(previous)
    if saved is None:
        del sys.modules['revision']
    else:
        sys.modules['revision']=saved
    return previous


def from_record(record):
    return r.Machine(tuple(record['alphabet']),tuple(record['outputs']),
                     tuple(tuple(row) for row in record['transitions']),record['initial'])


def installation(endpoint):
    a=r.access.Account(Q(endpoint['fuel']),initial_live=endpoint['live_cells'])
    live=a.live+8
    peak=live+8
    t=a.tariff
    bill=t.scale*(8*t.work+t.rent*peak*9+t.write*8+t.installation)
    status='complete'
    try:
        a.pay('additional_controller_installation',work=8,live=live,temporary=8,
              extra=t.installation)
    except r.Halt as error:
        status=str(error)
    return dict(status=status,required=str(bill),shortfall=str(max(Q(0),bill-a.start)),
                spent=str(a.spent),fuel=str(a.fuel),live_cells=a.live,events=a.events,
                scope='alternative installation feasibility only; no selector implemented')


def continued_use(endpoint,environment):
    a=r.access.Account(Q(endpoint['fuel']),initial_live=endpoint['live_cells'])
    port=r.Port(environment,endpoint['physical_phase'],endpoint['physical_parity'],
                endpoint['source_remaining'],a)
    # Bind the already-retained payload to its installed use entrypoint. This
    # does not call install/acquire or provide the port's target/state to it.
    s=endpoint['selected']
    controller=r.Reviser(None,(),port.command,a)
    controller.selected=dict(machine=from_record(s['machine']),parity=s['parity'],
                             state=s['state'],family=s['family'])
    controller.acquired_retained=True  # Explicitly historical at this boundary.
    rounds=[]
    while True:
        controller.retained=False
        controller.use_confirmed=False
        controller.use_receipt=None
        offset=len(a.events)
        status='complete'
        try:
            controller.use()
        except r.Halt as error:
            status=str(error)
        rounds.append(dict(status=status,new_retention=controller.retained,
                           use_confirmed=controller.use_confirmed,
                           receipt=controller.use_receipt,
                           stored_phase=controller.selected['state'],physical_phase=port._state,
                           fuel=str(a.fuel),spent_this_round=str(sum(Q(e['bill']) for e in a.events[offset:])),
                           event_start=offset,event_end=len(a.events)))
        if status!='complete':
            break
        assert len(rounds)<=int(a.start/Q(1,2))+1
    assert a.start==a.fuel+a.spent and port._source==endpoint['source_remaining']
    return dict(rounds=rounds,completed_rounds=sum(x['new_retention'] for x in rounds),
                confirmed_predictions=sum(x['use_confirmed'] for x in rounds),
                starting_fuel=str(a.start),spent=str(a.spent),fuel=str(a.fuel),
                source=port._source,initial_live=endpoint['live_cells'],live_cells=a.live,
                peak_cells=a.peak,events=a.events,native_trace=port.trace,
                maximum_native_calls_ignoring_other_costs=int(a.start/Q(1,4)))


def logical_retention():
    histories=list(product((0,1),repeat=2))
    encoders=list(product((0,1),repeat=4))
    decoders=list(product((0,1),repeat=2))
    rows=[]
    for encoder in encoders:
        for dx in decoders:
            for dy in decoders:
                correct_x=sum(dx[encoder[i]]==x for i,(x,y) in enumerate(histories))
                correct_y=sum(dy[encoder[i]]==y for i,(x,y) in enumerate(histories))
                rows.append(dict(encoder=list(encoder),decoder_x=list(dx),decoder_y=list(dy),
                                 correct_x=correct_x,correct_y=correct_y))
    assert len(rows)==256
    assert all((x['correct_x'],x['correct_y'])!=(4,4) for x in rows)
    histogram=Counter((x['correct_x'],x['correct_y']) for x in rows)
    return dict(scope='logical answer coverage only; no native reward or physical selector',
                histories=[list(h) for h in histories],encoders=len(encoders),designs=len(rows),
                exact_joint_designs=0,maximum_correct_pairs=max(x['correct_x']+x['correct_y'] for x in rows),
                histogram={f'{x},{y}':n for (x,y),n in sorted(histogram.items())},
                designs_data=rows)


def run():
    prior=previous_module()
    H,ancestry,access,four=prior.inherited()
    p=access['sensor_probe']
    H4=r.stutter(H)
    endpoints=[]
    unretained=[]
    for k,environment in enumerate((H,H4)):
        for parity in (0,1):
            for phase in range(len(environment.outputs)):
                e=r.revise(**dict(prior.arguments(H,p,environment,parity),physical_state=phase))
                prior.audit(e,p,ancestry)
                label=f'family{k}_parity{parity}_phase{phase}'
                if not e['retained']:
                    unretained.append(dict(label=label,status=e['status'],fuel=e['fuel'],
                                           source=e['source_remaining']))
                    continue
                i=installation(e)
                u=continued_use(e,environment)
                for branch in (i,u):
                    assert Q(145)==(89+Q(ancestry['old_acquisition_spent'])+Q(p['spent'])+
                        p['wasted']+Q(e['spent'])+Q(branch['spent'])+Q(branch['fuel'])+
                        e['source_remaining'])
                endpoints.append(dict(label=label,family=k,parity=parity,boundary_phase=phase,
                                      endpoint=e,installation=i,continued_use=u))
    assert len(endpoints)==8 and len(unretained)==6
    named={name:next(x for x in endpoints if x['label']==label) for name,label in {
        'actual_unchanged_H3':'family0_parity1_phase2',
        'declared_insertion_H4':'family1_parity1_phase2'}.items()}
    for row in named.values():
        assert row['installation']['status']=='funding:additional_controller_installation'
        assert row['continued_use']['completed_rounds']==0
        assert row['continued_use']['confirmed_predictions']==1
        assert row['continued_use']['rounds'][-1]['status']=='funding:retain_after_use'

    five=r.Machine(('a',),(0,0,0,0,1),((1,),(2,),(3,),(4,),(0,)))
    e=r.revise(**dict(prior.arguments(H,p,five,0),physical_state=1))
    prior.audit(e,p,ancestry)
    assert e['retained'] and e['selected']['family']==1
    u=continued_use(e,five)
    assert Q(e['fuel'])==Q(u['spent'])+Q(u['fuel'])
    wrong=dict(scope='actual previous outside-family false acceptance, supplied boundarycase',
               endpoint=e,continued_use=u)

    signatures=[]
    for k,m in enumerate((H,H4)):
        for parity in (0,1):
            for phase in range(len(m.outputs)):
                q=phase
                bits=[]
                for _ in range(6):
                    bits.append(m.outputs[q]^parity)
                    q=m.transitions[q][0]
                signatures.append(dict(family=k,parity=parity,phase=phase,bits=bits))
    assert len({tuple(s['bits']) for s in signatures})==14
    assert len({tuple(s['bits'][:5]) for s in signatures})<14
    parent_results=json.loads((HERE.parent/'results.json').read_text())
    inherited_hashes={**parent_results['inherited_hashes'],
        **{str((HERE.parent/name).relative_to(ROOT)):digest(HERE.parent/name)
           for name in ('revision.py','check.py')}}
    out=dict(scope='recipe-relative resource boundary and separate information countermodel; no metaselector',
             ancestry=ancestry,prior_access=p,endpoints=endpoints,nonterminal_exclusions=unretained,
             named_endpoints={k:v['label'] for k,v in named.items()},
             wrong_accepted_continuation=wrong,logical_retention=logical_retention(),
             restricted_signatures=signatures,
             source_hashes={name:digest(HERE/name) for name in ('check.py','PROTOCOL.md')},
             inherited_hashes=inherited_hashes)
    (HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(named={k:dict(fuel=v['endpoint']['fuel'],
        install_required=v['installation']['required'],
        rounds=v['continued_use']['rounds']) for k,v in named.items()},
        family=[dict(label=x['label'],install=x['installation']['status'],
                     repetitions=x['continued_use']['completed_rounds'],
                     terminal=x['continued_use']['rounds'][-1]['status']) for x in endpoints],
        logical=out['logical_retention']['histogram'],wrong=u['rounds']),indent=2))


if __name__=='__main__':
    run()
