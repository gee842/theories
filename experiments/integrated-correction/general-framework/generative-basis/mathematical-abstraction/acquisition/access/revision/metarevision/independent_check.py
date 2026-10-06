"""Independent endpoint reconstruction, use scheduling and information bounds.

The reference below generates its own operation schedule and prices. It does
not use Account, Reviser.use, or the study's retention enumeration to do so.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import copy
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[8]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


implementation = load('_meta_independent_tested', HERE/'check.py')
saved_revision = sys.modules.get('revision')
sys.modules['revision'] = implementation.r
prior = load('_meta_independent_prior', HERE.parent/'independent_check.py')
if saved_revision is None:
    del sys.modules['revision']
else:
    sys.modules['revision'] = saved_revision


def normalized(value):
    return json.loads(json.dumps(value))


def reference_installation(endpoint):
    live, fuel = endpoint['live_cells'], Q(endpoint['fuel'])
    peak = live+16
    bill = Q(1)+Q(16,64)+Q(9*peak,65536)
    event = dict(kind='additional_controller_installation',work=8,live=live+8,
                 temporary=8,workspace=0,peak=peak,rewrites=0,extra='1',
                 bill=str(bill),fuel=str(fuel-bill))
    admitted = fuel >= bill
    return dict(status='complete' if admitted else 'funding:additional_controller_installation',
                required=str(bill),shortfall=str(max(Q(0),bill-fuel)),
                spent=str(bill if admitted else Q(0)),
                fuel=str(fuel-bill if admitted else fuel),
                live_cells=live+8 if admitted else live,events=[event] if admitted else [],
                scope='alternative installation feasibility only; no selector implemented')


def reference_use(endpoint, environment):
    """A separate six-operation state machine, including interrupted writes."""
    start = stock = Q(endpoint['fuel'])
    live = endpoint['live_cells']
    physical, physical_parity = endpoint['physical_phase'], endpoint['physical_parity']
    selected = endpoint['selected']
    model, cursor, parity = selected['machine'], selected['state'], selected['parity']
    events, trace, rounds = [], [], []
    peak = live
    schedule = (
        ('plan_forward_prediction',3,3,0,0,Q(0)),
        ('native_a',0,2,3,0,Q(1,4)),
        ('commit_use_cursor',1,0,3,1,Q(0)),
        ('native_read',0,2,3,0,Q(1,4)),
        ('compare_forward_prediction',1,0,3,1,Q(0)),
        ('retain_after_use',1,0,0,0,Q(live,64)),
    )
    while True:
        beginning, offset = stock, len(events)
        confirmed = retained = False
        receipt, observed = None, None
        next_cursor = model['transitions'][cursor][0]
        expected = model['outputs'][next_cursor]^parity
        status = 'complete'
        for kind, work, temporary, workspace, rewrites, extra in schedule:
            required = live+temporary+workspace
            bill = Q(work+rewrites,64)+Q(required*(work+1),65536)+extra
            if stock < bill:
                status = 'funding:'+kind
                break
            stock -= bill
            peak = max(peak,required)
            events.append(dict(kind=kind,work=work,live=live,temporary=temporary,
                               workspace=workspace,peak=required,rewrites=rewrites,
                               extra=str(extra),bill=str(bill),fuel=str(stock)))
            if kind == 'native_a':
                physical = environment['transitions'][physical][0]
                trace.append(dict(command='a',observation=None))
            elif kind == 'commit_use_cursor':
                cursor = next_cursor
            elif kind == 'native_read':
                observed = environment['outputs'][physical]^physical_parity
                trace.append(dict(command='read',observation=observed))
            elif kind == 'compare_forward_prediction':
                receipt = dict(expected=expected,observed=observed)
                if expected != observed:
                    status = 'use_prediction_mismatch'
                    break
                confirmed = True
            elif kind == 'retain_after_use':
                retained = True
        rounds.append(dict(status=status,new_retention=retained,use_confirmed=confirmed,
                           receipt=receipt,stored_phase=cursor,physical_phase=physical,
                           fuel=str(stock),spent_this_round=str(beginning-stock),
                           event_start=offset,event_end=len(events)))
        if status != 'complete':
            break
        assert len(rounds) <= int(start*2)+1
    return dict(rounds=rounds,completed_rounds=sum(x['new_retention'] for x in rounds),
                confirmed_predictions=sum(x['use_confirmed'] for x in rounds),
                starting_fuel=str(start),spent=str(start-stock),fuel=str(stock),
                source=endpoint['source_remaining'],initial_live=live,live_cells=live,
                peak_cells=peak,events=events,native_trace=trace,
                maximum_native_calls_ignoring_other_costs=int(start*4))


def logical_reference():
    """Integer truth tables, separate from the study's product enumeration."""
    histogram, details = Counter(), {}
    for encoder in range(16):
        for decoder_pair in range(16):
            successes = [0,0]
            dx, dy = decoder_pair&3, decoder_pair>>2
            for history in range(4):
                memory = (encoder>>history)&1
                successes[0] += ((dx>>memory)&1) == ((history>>1)&1)
                successes[1] += ((dy>>memory)&1) == (history&1)
            histogram[tuple(successes)] += 1
            key = (tuple((encoder>>h)&1 for h in range(4)),
                   tuple((dx>>m)&1 for m in range(2)),
                   tuple((dy>>m)&1 for m in range(2)))
            details[key] = tuple(successes)
    assert sum(histogram.values()) == 256 and histogram[4,4] == 0
    assert max(x+y for x,y in histogram) == 6
    return histogram,details


def whole_balance(endpoint, continuation, access):
    assert Q(145) == (89+Q(1984289,65536)+Q(access['spent'])+access['wasted']
                      +Q(endpoint['spent'])+Q(continuation['spent'])+
                      Q(continuation['fuel'])+endpoint['source_remaining'])


def main():
    saved = json.loads((HERE/'results.json').read_text())
    for name,digest in saved['source_hashes'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == digest
    for name,digest in saved['inherited_hashes'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest() == digest

    H,access,_ = prior.handoffs()
    p = access['probe']
    G = prior.machine(prior.generate(H.record()))
    indexed = {x['label']:x for x in saved['endpoints']}
    verified, excluded = [], []
    primary = {}
    for family,environment in enumerate((H,G)):
        for parity in (0,1):
            for phase in range(len(environment.outputs)):
                endpoint,_ = prior.run_one(H,p,environment,parity,phase=phase)
                label = f'family{family}_parity{parity}_phase{phase}'
                if not endpoint['retained']:
                    excluded.append(dict(label=label,status=endpoint['status'],
                                         fuel=endpoint['fuel'],source=endpoint['source_remaining']))
                    continue
                row = indexed[label]
                assert normalized(endpoint) == row['endpoint']
                installed = reference_installation(endpoint)
                assert installed == implementation.installation(endpoint) == row['installation']
                continued = reference_use(endpoint,environment.record())
                assert continued == implementation.continued_use(endpoint,environment) == row['continued_use']
                whole_balance(endpoint,installed,p)
                whole_balance(endpoint,continued,p)
                assert len(continued['native_trace']) <= continued['maximum_native_calls_ignoring_other_costs']
                verified.append(dict(label=label,starting_fuel=endpoint['fuel'],
                                     installation=installed['status'],
                                     completed=continued['completed_rounds'],
                                     confirmed=continued['confirmed_predictions'],
                                     final_status=continued['rounds'][-1]['status'],
                                     spent=continued['spent'],fuel=continued['fuel']))
                if parity == 1 and phase == 2:
                    primary[family] = (endpoint,environment,continued)
    assert len(verified) == 8 and len(excluded) == 6
    assert excluded == saved['nonterminal_exclusions']
    assert Counter(x['completed'] for x in verified) == {0:6,1:2}
    assert Counter(x['installation'] for x in verified) == {
        'funding:additional_controller_installation':6,'complete':2}

    # Derived withdrawal-only controls stop immediately before each of the
    # six charged steps. These are not extra resource-bearing histories.
    denials=[]
    for family,(endpoint,environment,_) in primary.items():
        # Enough funds only for constructing the complete reference schedule;
        # this mathematical schedule is never used as an inherited resource.
        ample = copy.deepcopy(endpoint)
        ample['fuel'] = '10'
        events = reference_use(ample,environment.record())['events'][:6]
        cumulative = Q(0)
        for event in events:
            cumulative += Q(event['bill'])
            assert cumulative-Q(1,65536) <= Q(endpoint['fuel']) or event['kind']=='retain_after_use'
            fixture = copy.deepcopy(endpoint)
            # Retention boundary exceeds the true reserve at both endpoints:
            # withdraw a quantum there too, never top up a denial control.
            fixture['fuel'] = str(min(Q(endpoint['fuel']),cumulative)-Q(1,65536))
            expected = reference_use(fixture,environment.record())
            actual = implementation.continued_use(fixture,environment)
            assert actual == expected
            assert expected['rounds'][-1]['status'] == 'funding:'+event['kind']
            assert not expected['rounds'][-1]['new_retention']
            denials.append(dict(family=family,starting_fuel=fixture['fuel'],
                               withdrawal=str(Q(endpoint['fuel'])-Q(fixture['fuel'])),
                               status=expected['rounds'][-1]['status'],
                               confirmed=expected['rounds'][-1]['use_confirmed'],
                               native_trace=expected['native_trace']))

    five = implementation.r.Machine(('a',),(0,0,0,0,1),((1,),(2,),(3,),(4,),(0,)))
    wrong,_ = prior.run_one(H,p,five,0,phase=1)
    assert wrong['retained'] and wrong['selected']['family'] == 1
    continued = reference_use(wrong,five.record())
    assert normalized(wrong) == saved['wrong_accepted_continuation']['endpoint']
    assert continued == implementation.continued_use(wrong,five) == saved['wrong_accepted_continuation']['continued_use']
    whole_balance(wrong,continued,p)
    assert continued['completed_rounds'] == 1 and continued['confirmed_predictions'] == 2
    assert continued['rounds'][-1]['status'] == 'funding:retain_after_use'

    hist,designs = logical_reference()
    reported = saved['logical_retention']
    assert reported['histogram'] == {f'{x},{y}':n for (x,y),n in sorted(hist.items())}
    assert reported['designs'] == len(designs) == 256
    assert reported['exact_joint_designs'] == 0 and reported['maximum_correct_pairs'] == 6
    assert len(reported['designs_data']) == len(designs)
    for row in reported['designs_data']:
        key = tuple(map(tuple,(row['encoder'],row['decoder_x'],row['decoder_y'])))
        assert designs.pop(key) == (row['correct_x'],row['correct_y'])
    assert not designs

    signatures=[]
    for family,environment in enumerate((H,G)):
        for parity in (0,1):
            for phase in range(len(environment.outputs)):
                states=[phase]
                for _ in range(5):
                    states.append(environment.transitions[states[-1]][0])
                bits=[environment.outputs[q]^parity for q in states]
                signatures.append(dict(family=family,parity=parity,phase=phase,bits=bits))
    assert signatures == saved['restricted_signatures']
    assert len({tuple(x['bits']) for x in signatures}) == 14
    assert len({tuple(x['bits'][:5]) for x in signatures}) == 12

    paths=[HERE/'independent_check.py',HERE/'check.py',HERE/'PROTOCOL.md',
           HERE.parent/'revision.py',HERE.parent/'independent_check.py',
           HERE.parent.parent/'diagnosis.py',HERE.parent.parent.parent/'model.py']
    receipt=dict(scope='independent actual endpoint reconstruction and complete continuation schedule/pricing; separate logical countermodel',
                 endpoints=verified,excluded_unretained=excluded,
                 withdrawal_only_controls=denials,
                 wrong_model=dict(completed=continued['completed_rounds'],
                                  confirmed=continued['confirmed_predictions'],
                                  terminal=continued['rounds'][-1]['status']),
                 logical_designs=256,logical_histogram=reported['histogram'],
                 joint_exact=0,maximum_correct_answer_pairs=6,
                 distinct_six_read_signatures=14,distinct_five_read_signatures=12,
                 source_hashes={str(path.relative_to(ROOT)):sha256(path.read_bytes()).hexdigest() for path in paths},
                 checked_results_sha256=sha256((HERE/'results.json').read_bytes()).hexdigest())
    (HERE/'independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in
                     ('source_hashes','withdrawal_only_controls','excluded_unretained')},indent=2))


if __name__ == '__main__':
    main()
