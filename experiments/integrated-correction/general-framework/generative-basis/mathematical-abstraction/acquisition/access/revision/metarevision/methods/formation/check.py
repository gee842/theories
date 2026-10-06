"""Actual-history joins, paid formation witnesses and preserved failure controls."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product, permutations
from collections import Counter
import importlib.util
import hashlib
import json
import sys
import model as m

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())


def inherited():
    saved = sys.modules.get('model')
    sys.modules['model'] = m.methods
    spec = importlib.util.spec_from_file_location('_formation_parent_check', HERE.parent/'check.py')
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    if saved is None:
        del sys.modules['model']
    else:
        sys.modules['model'] = saved
    H, handoff = parent.inherited()
    return H, handoff, parent


def equivalent(x, environment, parity):
    if x['selected'] is None:
        return None
    selected = x['selected']
    model = selected['machine']
    q, physical, seen = selected['state'], x['physical_phase'], set()
    while (q, physical) not in seen:
        seen.add((q, physical))
        if model['outputs'][q]^selected['parity'] != environment.outputs[physical]^parity:
            return False
        q = model['transitions'][q][0]
        physical = environment.transitions[physical][0]
    return True


def threshold(events):
    costs = income = bound = Q(0)
    for event in events:
        if event['kind'] == 'actual_arrival':
            income += Q(event['amount'])
        else:
            costs += Q(event['bill'])
            bound = max(bound, costs-income)
    return bound


def compact(x):
    keys = ('status','retained','acquired_retained','use_confirmed','selected',
            'receipt','archive','archive_retained','method_edge','edge_retained',
            'accepted_recipe','tried','trials','retired_edges','invocations',
            'spent','fuel','income','wasted','source_remaining','peak_cells',
            'live_cells','predictively_equivalent')
    return {k:x[k] for k in keys}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    H, handoff, parent = inherited()
    starting = Q(handoff['fuel'])
    H4 = m.r.stutter(H)

    def trial(**overrides):
        args = dict(fuel=starting, source=10, physical_state=handoff['environment_phase'])
        args.update(overrides)
        x = m.run(H, **args)
        withdrawal = starting-Q(args['fuel'])+(10-args['source'])
        x['prior_withdrawal'] = str(withdrawal)
        x['predictively_equivalent'] = equivalent(
            x, args.get('environment',H),
            args.get('target_flip',0)^args.get('sensor_flip',0))
        assert Q(x['starting_fuel'])+Q(x['income']) == Q(x['spent'])+Q(x['fuel'])
        assert Q(x['income'])+x['wasted']+x['source_remaining'] == args['source']
        assert Q(145) == (89+Q(handoff['old_acquisition_spent'])+withdrawal+
                          Q(x['spent'])+Q(x['fuel'])+x['wasted']+x['source_remaining'])
        if x['retained']:
            assert x['status'] == 'complete' and x['use_confirmed'] and x['acquired_retained']
            assert x['archive_retained'] and x['edge_retained']
        return x

    fixtures = {}
    for name, environment in (('three',H),('four',H4)):
        for first in (0,1):
            key = name+'_first_'+str(first)
            fixtures[key] = trial(environment=environment, first_proposal=first)
            assert fixtures[key]['retained'] and fixtures[key]['predictively_equivalent']
    witness = fixtures['four_first_0']
    assert [x['recipe'] for x in witness['trials']] == [0,1]
    assert witness['trials'][0]['survivor'] is None
    assert witness['retired_edges'] == [[0,0,1]]
    assert witness['method_edge'] == [0,1,1]
    assert witness['invocations'][-1] == dict(stage='later_use',source=0,recipe=1)

    fixtures['formation_clamped'] = trial(environment=H4,clamp_formation=True)
    fixtures['source_port_mismatch'] = trial(environment=H4,mismatch_first_source=True)
    fixtures['accepted_edge_broken'] = trial(environment=H4,break_after_accept=True)
    fixtures['first_destination_swapped'] = trial(environment=H4,swap_first_destination=True)
    assert fixtures['formation_clamped']['status'] == 'no_bound_method_edge'
    assert not fixtures['formation_clamped']['invocations']
    assert fixtures['source_port_mismatch']['status'] == 'method_edge_receipt_mismatch'
    assert fixtures['accepted_edge_broken']['status'] == 'no_bound_method_edge'
    assert fixtures['first_destination_swapped']['invocations'][0]['recipe'] == 1
    for name,kwargs in (
        ('receipt_inverted',dict(receipt_flip=1)),
        ('sensor_inverted',dict(sensor_flip=1)),
        ('reset_broken',dict(broken_reset=1)),
        ('transfer_blocked',dict(blocked=1)),
        ('receipt_read_unfunded',dict(tariff=m.access.Tariff(receipt=Q(100)))),
        ('small_capacity',dict(capacity=47)),
        ('source_withdrawn',dict(source=0)),
    ):
        fixtures[name] = trial(**kwargs)

    five = m.Machine(('a',),(0,0,0,0,1),((1,),(2,),(3,),(4,),(0,)))
    delayed = m.Machine(('a',),(0,0,1,0,0,1,0,0,1,1),
                        tuple(((q+1)%10,) for q in range(10)))
    fixtures['outside_five'] = trial(environment=five)
    fixtures['outside_delayed'] = trial(environment=delayed)
    assert fixtures['outside_delayed']['retained']
    assert fixtures['outside_delayed']['predictively_equivalent'] is False

    # Derived exact-budget tests preserve the original tariffs and schedule.
    thresholds = {}
    for name,environment in (('three',H),('four',H4)):
        for first in (0,1):
            key = name+'_first_'+str(first)
            bound = threshold(fixtures[key]['events'])
            thresholds[key] = str(bound)
            exact = trial(environment=environment,first_proposal=first,fuel=bound)
            short = trial(environment=environment,first_proposal=first,
                          fuel=bound-Q(1,65536))
            assert exact['retained']
            assert not short['retained']
            fixtures[key+'_exact_budget'] = exact
            fixtures[key+'_one_quantum_short'] = short

    # An income-free witness permits exact denial immediately before each
    # selected event, exposing paid physical prefixes without borrowing income.
    deny_kinds = (
        'store_receipt','append_archive_bit','retain_acquired_record',
        'form_method_edge','remove_contradicted_edge','retain_accepted_edge',
        'compact_formed_method_result','retain_formed_method_result',
        'commit_use_cursor','retain_after_use',
    )
    for kind in deny_kinds:
        paid = Q(0)
        for event in witness['events']:
            assert event['kind'] != 'actual_arrival'
            if event['kind'] == kind:
                break
            paid += Q(event['bill'])
        else:
            raise AssertionError('missing witness stage '+kind)
        denied = trial(environment=H4,fuel=paid)
        assert denied['status'] == 'funding:'+kind
        fixtures['denied_'+kind] = denied
    cursor_denied = fixtures['denied_commit_use_cursor']
    assert cursor_denied['selected']['state'] != cursor_denied['physical_phase']

    family = []
    for family_id, environment in enumerate((H,H4)):
        for phase in range(len(environment.outputs)):
            for flags in product((0,1), repeat=5):
                tau,sigma,broken,blocked,receipt_flip = flags
                for first in (0,1):
                    x = trial(environment=environment,physical_state=phase,
                              first_proposal=first,target_flip=tau,sensor_flip=sigma,
                              broken_reset=broken,blocked=blocked,receipt_flip=receipt_flip)
                    if x['retained']:
                        assert x['predictively_equivalent']
                    family.append(dict(environment_family=family_id,
                                       initial_phase=phase,first_proposal=first,
                                       target_flip=tau,sensor_flip=sigma,
                                       broken_reset=broken,blocked=blocked,
                                       receipt_flip=receipt_flip,result=compact(x)))

    renamings = []
    for labels in permutations(range(3)):
        renamed = parent.rename(H,labels)
        for family_id, environment in enumerate((renamed,m.r.stutter(renamed))):
            for first in (0,1):
                x = m.run(renamed,starting,10,labels[handoff['environment_phase']],
                          environment=environment,first_proposal=first)
                reference = fixtures[('three' if family_id==0 else 'four')+'_first_'+str(first)]
                assert x['native_trace'] == reference['native_trace']
                assert x['spent'] == reference['spent']
                assert x['peak_cells'] == reference['peak_cells']
                assert x['retained'] and equivalent(x,environment,0)
                renamings.append(dict(labels=list(labels),family=family_id,first=first))

    summary = dict(cases=len(family),
                   statuses=dict(Counter(x['result']['status'] for x in family)),
                   retained=sum(x['result']['retained'] for x in family),
                   rejected_and_replaced=sum(bool(x['result']['retired_edges']) for x in family))
    result = dict(scope='conditional local formation from absent connection, no recipe-origin theorem',
                  handoff=handoff,fixtures=fixtures,family=family,summary=summary,
                  thresholds=thresholds,renamings=renamings,
                  first_proposal_law={'0':'1/2','1':'1/2'},
                  source_hashes={name:digest(HERE/name) for name in ('model.py','check.py','PROTOCOL.md')},
                  inherited_hashes={str((HERE.parent/'model.py').relative_to(ROOT)):digest(HERE.parent/'model.py'),
                                    str((HERE.parent/'check.py').relative_to(ROOT)):digest(HERE.parent/'check.py')})
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(summary=summary,thresholds=thresholds,
                          fixtures={k:compact(v) for k,v in fixtures.items()},
                          renamings=len(renamings)),indent=2))


if __name__ == '__main__':
    run()
