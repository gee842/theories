"""Independent event interpreter for paid recipient-candidate revision.

Expected transitions are computed directly from the frozen protocol, not from
the producer's suffix, access, command, evidence-update or witness functions.
The producer's dataclasses are public output types. Parent histories are
separately reconstructed by handoff_check, reusing the prior independent law.
"""
from collections import defaultdict
from copy import deepcopy
from dataclasses import asdict, fields, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

import model as producer
import handoff_check

HERE = Path(__file__).resolve().parent
ARMS = ('indexed','conventional','no_feedback','misleading','private_zero','shared_write')
PARENT_FIELDS = tuple(field.name for field in fields(producer.architecture.State))
NEW_FIELDS = tuple(field.name for field in fields(producer.State) if field.name != 'parent')


def freeze(p, x):
    p = dict(p)
    for name in ('r_nodes','d_nodes','graph','retained'):
        p[name] = tuple(p[name])
    return producer.State(parent=producer.architecture.State(**p), **x)


def key(state):
    return (tuple(getattr(state.parent,name) for name in PARENT_FIELDS),
            tuple(getattr(state,name) for name in NEW_FIELDS))


def distribution(branches, traces=False):
    result = defaultdict(F)
    for branch in branches:
        index = tuple((event,key(state)) for event,state in branch.trace) if traces else key(branch.state)
        result[index] += branch.probability
    return dict(result)


def reference(law, parent, regime, arm):
    """Enumerate the two independent source-availability draws in advance."""
    assert arm in ARMS and regime in (0,1)
    initial_parent = asdict(parent)
    total = parent.fuel+parent.patient+law.initial_bank
    immutable = {name:value for name,value in initial_parent.items()
                 if name not in ('fuel','patient','active','q','last','raw_w','retained')}
    results = []
    for draws in product((False,True),repeat=2):
        probability = F(1)
        for available in draws:
            probability *= law.availability if available else 1-law.availability
        if not probability:
            continue
        p = deepcopy(initial_parent)
        p['retained'] = list(p['retained'])
        x = {field.name:field.default for field in fields(producer.State)
             if field.name not in ('parent','bank')}
        x['bank'] = law.initial_bank
        trace = []

        def access():
            return bool(p['active'] and p['retained'][1])

        def validate():
            assert all(x[name] >= 0 for name in NEW_FIELDS if name not in ('wire','indexed'))
            assert p['fuel'] >= 0 and p['patient'] >= 0 and p['raw_w'] >= 0
            assert p['fuel']+p['patient']+sum(x[name] for name in
                   ('bank','escrow','spent','waste','patient_used','damage')) == total
            assert p['raw_w']+int(x['wire']) == parent.raw_w
            assert x['indexed'] <= x['wire']
            assert all(p[name] == value for name,value in immutable.items())
            if x['indexed']:
                assert 0 <= p['q'] < 4 and p['last'] in (0,1)
                if arm != 'shared_write':
                    assert p['q']//2 == parent.q//4
            assert not any(p['retained']) or p['active']

        def emit(event):
            validate()
            trace.append((event,freeze(p,x)))

        def pay(amount):
            if p['fuel'] < amount:
                return False
            p['fuel'] -= amount
            x['spent'] += amount
            return True

        def transmits(target):
            # A node interpreter, independent of the producer's Boolean/table forms.
            node = 'R' if p['r_nodes'][1] else None
            while node is not None and node != 'P':
                if node == 'R':
                    node = 'P' if p['graph'][1] & 1 else 'D' if p['graph'][1] & 2 else None
                elif node == 'D':
                    node = 'P' if target == 'actor' and p['graph'][1] & 4 else None
            return node == 'P'

        def command(target):
            if x['indexed']:
                bit = p['q']//2 if target == 'actor' else p['q']%2
            else:
                bit = 0 if p['q'] < 2 else 1 if p['q'] > 2 else p['last']
            return bit ^ p['coupling']

        validate()
        for index,target in enumerate(('actor','recipient','actor','recipient')):
            label = ('A0','R1','A1','R2')[index]
            action, learning = None, False
            if access():
                if pay(law.rent):
                    emit(label+'.rent')
                    if pay(law.sensing):
                        emit(label+'.sense')
                        if transmits(target):
                            learning = bool(target == 'recipient' and x['wire'] and x['indexed'])
                            escrow = law.observation+law.write if learning else 0
                            if p['fuel'] >= law.work+escrow:
                                if escrow:
                                    p['fuel'] -= escrow
                                    x['escrow'] += escrow
                                    emit(label+'.escrow')
                                action = command(target)
                                assert pay(law.work)
                                x[target+'_attempts'] += 1
                                if not x['indexed']:
                                    p['last'] = action
                                emit(label+'.work.'+str(action))
                else:
                    p['active'] = False
                    p['retained'] = [False,False]
                    emit(label+'.lose_predictor')

            target_regime = regime
            if target == 'recipient':
                target_regime ^= law.recipient_flip ^ int(index == 3 and law.reverse_after_first)
            available = True if target == 'actor' else draws[(index-1)//2]
            correct_command = action is not None and action == target_regime
            captured = bool(correct_command and available)
            if target == 'recipient' and action is not None and not correct_command:
                loss = min(law.harm,p['patient'])
                p['patient'] -= loss
                x['damage'] += loss
                emit(label+'.damage')
            x['bank'] -= law.packet
            if captured:
                p['fuel' if target == 'actor' else 'patient'] += law.packet
                x[target+'_captures'] += 1
                emit(label+'.receipt')
                if target == 'actor':
                    assert pay(law.upkeep)
                    emit(label+'.upkeep')
                else:
                    p['patient'] -= law.patient_use
                    x['patient_used'] += law.patient_use
                    emit(label+'.patient_use')
            else:
                x['waste'] += law.packet
                emit(label+'.spill')

            if target == 'recipient':
                if action is not None and learning:
                    assert x['escrow'] == law.observation+law.write
                    x['escrow'] -= law.observation
                    x['spent'] += law.observation
                    x['observations'] += 1
                    observation = (None if arm == 'no_feedback' else
                                   not captured if arm == 'misleading' else
                                   False if arm == 'private_zero' else captured)
                    faithful = arm in ('indexed','conventional','shared_write')
                    if observation is None:
                        x['absent_feedback'] += 1
                    elif faithful:
                        x['real_positive' if observation else 'real_zero'] += 1
                    provenance = 'real' if faithful else arm
                    emit(label+'.observe.'+provenance+'.'+
                         ('absent' if observation is None else 'positive' if observation else 'zero'))
                    a, r, qualified = p['q']//2, p['q']%2, p['last']
                    old_a, old_r = a,r
                    if observation is not None:
                        if observation:
                            r = action ^ p['coupling']
                            qualified = 1
                        elif not qualified:
                            r ^= 1
                        if arm == 'shared_write':
                            a = r
                    x['escrow'] -= law.write
                    x['spent'] += law.write
                    x['writes'] += 1
                    x['changed_writes'] += int(r != old_r)
                    x['actor_changes'] += int(a != old_a)
                    p['q'],p['last'] = 2*a+r,qualified
                    emit(label+'.write.'+('changed' if r != old_r else 'unchanged'))
                else:
                    x['absent_feedback'] += 1
                    emit(label+'.feedback.unavailable')

            if index == 0 and access():
                if p['raw_w'] > 0 and pay(law.wire_cost):
                    p['raw_w'] -= 1
                    x['wire'] = True
                    emit('wire.attach')
                if x['wire'] and pay(law.recode_cost):
                    bit = p['q']//4
                    p['q'],p['last'] = 3*bit,0
                    x['indexed'] = True
                    emit('memory.recode')

        for index in (0,1):
            if p['active'] and p['retained'][index]:
                if pay(law.hold):
                    x['holds'] += 1
                    emit('hold.'+str(index))
                else:
                    p['retained'][index] = False
                    emit('lose.'+str(index))
        validate()
        assert x['bank'] == x['escrow'] == 0
        results.append(producer.Branch(freeze(p,x),probability,tuple(trace)))
    assert sum(branch.probability for branch in results) == 1
    return tuple(results)


def strict_reference(branch, entry):
    """Require the ordered physical/evidence history, not an input witness flag."""
    stages = {}
    actions = {}
    actor_bit = entry.q//4
    for index,(event,state) in enumerate(branch.trace):
        if state.indexed and state.parent.q//2 != actor_bit:
            return False
        if '.work.' in event:
            actions[event.split('.')[0]] = int(event.rsplit('.',1)[1])
        if event in ('R1.observe.real.zero','R1.write.changed','A1.receipt',
                     'R2.observe.real.positive','hold.1'):
            stages[event] = index,state
    ordered = ('R1.observe.real.zero','R1.write.changed','A1.receipt',
               'R2.observe.real.positive','hold.1')
    if any(event not in stages for event in ordered):
        return False
    positions = [stages[event][0] for event in ordered]
    if positions != sorted(positions):
        return False
    old = stages['R1.observe.real.zero'][1]
    changed = stages['R1.write.changed'][1]
    final = branch.state
    return bool(old.parent.q%2 != changed.parent.q%2
                and actions.get('A1') == actor_bit ^ entry.coupling
                and actions.get('R2') == (changed.parent.q%2) ^ entry.coupling
                and actions.get('R1') != actions.get('R2')
                and final.indexed and final.parent.last == 1
                and final.parent.retained[1])


def independent_metrics(branch, entry):
    state = branch.state
    data = {name:getattr(state,name) for name in
            ('bank','spent','waste','patient_used','damage','actor_attempts','recipient_attempts',
             'actor_captures','recipient_captures','observations','writes','real_positive',
             'real_zero','absent_feedback','changed_writes','actor_changes','holds')}
    data.update(fuel=state.parent.fuel,patient=state.parent.patient,raw_w=state.parent.raw_w,
                p_wire=int(state.wire),p_indexed=int(state.indexed),
                p_qualified=int(state.indexed and state.parent.last == 1),
                p_actor_preserved=int(state.indexed and state.parent.q//2 == entry.q//4),
                p_site_retained=int(state.parent.retained[1]),
                retained_graphs=sum(state.parent.retained),
                p_strict_witness=int(strict_reference(branch,entry)))
    events=[event for event,_ in branch.trace]
    data['p_first_candidate_change']=int('R1.write.changed' in events)
    data['p_positive_then_zero_preserved']=int(all(event in events for event in
        ('R1.observe.real.positive','R2.observe.real.zero','R2.write.unchanged')))
    return data


def compare(law, entry, regime, arm):
    expected=reference(law,entry,regime,arm)
    observed=producer.suffix(law,entry,regime,arm)
    assert distribution(expected)==distribution(observed), ('terminal',law,entry,regime,arm)
    assert distribution(expected,True)==distribution(observed,True), ('trace',law,entry,regime,arm)
    for branch in expected:
        assert strict_reference(branch,entry)==producer.strict_witness(branch,entry)
    return expected


def parent_key(state):
    return tuple(getattr(state,name) for name in PARENT_FIELDS)


def thaw_parent(data):
    data=dict(data)
    for name in ('r_nodes','d_nodes','graph','retained'):
        data[name]=tuple(data[name])
    return producer.architecture.State(**data)


def thaw(data):
    data=dict(data)
    data['parent']=thaw_parent(data['parent'])
    return producer.State(**data)


def joined(law, preps, rows):
    report=producer.compare(law)
    saved={}
    failed=sum(F(row['probability']) for row in preps if not row['commissioned'])
    for arm in ARMS:
        totals=defaultdict(F)
        terminal=defaultdict(F)
        for row in rows:
            entry,mass=row['state'],row['probability']
            for branch in reference(law,entry,row['regime'],arm):
                weight=mass*branch.probability
                for name,value in independent_metrics(branch,entry).items():
                    totals[name]+=weight*value
                totals['p_prior_motor_revision_and_strict_witness']+=weight*int(
                    row['coupling_state'].witness and strict_reference(branch,entry))
                terminal[(row['initial_regime'],tuple(asdict(row['coupling_state']).items()),
                          parent_key(entry),key(branch.state))]+=weight
            past=row['historic_energy']+sum(getattr(entry,name) for name in
                ('spent','patient_used','damage','waste','source'))
            totals['historical_energy']+=mass*past
        old=law.architecture_law()
        totals['bank']+=failed*law.initial_bank
        totals['patient']+=failed*old.patient_initial
        totals['raw_w']+=failed*old.connector_parts
        totals['uncommissioned_energy']=sum(F(row['probability'])*row['remaining_energy']
                                            for row in preps if not row['commissioned'])
        totals['failed_preparation_spent']=sum(F(row['probability'])*row['preparation_spent']
                                               for row in preps if not row['commissioned'])
        totals['p_commissioned']=1-failed
        observed={name:F(value) for name,value in report['arms'][arm]['metrics'].items()}
        assert dict(totals)==observed, ('aggregate',arm,
            {name:(totals.get(name),observed.get(name)) for name in set(totals)|set(observed)
             if totals.get(name)!=observed.get(name)})
        observed_terminal={}
        for row in report['arms'][arm]['terminal_rows']:
            assert row['regime']==row['initial_regime'] ^ 1
            observed_terminal[(row['initial_regime'],tuple(row['coupling_state'].items()),
                               parent_key(thaw_parent(row['entry'])),key(thaw(row['state'])))]=F(row['probability'])
        assert dict(terminal)==observed_terminal, ('unconditional_terminal',arm)
        assert sum(totals[name] for name in ('fuel','patient','bank','spent','waste','patient_used',
            'damage','historical_energy','uncommissioned_energy','failed_preparation_spent')) == (
            old.initial_common+old.initial_source+old.patient_initial+law.initial_bank)
        saved[arm]={name:str(value) for name,value in sorted(totals.items())}
    assert saved['indexed']==saved['conventional']
    return saved


def run():
    before=source_hashes()
    assert producer.ARMS==ARMS
    expected_cases=('primary','same_law','recipient_outages','no_recipient_source',
                    'same_law_outages','reversal_after_positive','expensive_write',
                    'expensive_observation','no_original_connector','low_original_reserve',
                    'filter_copy_formation','no_build_formation')
    assert tuple(producer.cases())==expected_cases
    parents, counts, saved={},defaultdict(int),{}
    for case,law in producer.cases().items():
        cache_key=(law.initial_common,law.connector_parts,law.formation_arm)
        if cache_key not in parents:
            parents[cache_key]=handoff_check.independent_parent(
                producer.architecture,law.architecture_law(),law.formation_arm)
        preps,rows,_=parents[cache_key]
        for row in rows:
            outcomes={}
            for arm in ARMS:
                outcomes[arm]=compare(law,row['state'],row['regime'],arm)
                counts['reachable_comparisons']+=1
                counts['reachable_exogenous_draw_branches']+=len(outcomes[arm])
            assert distribution(outcomes['indexed'],True)==distribution(outcomes['conventional'],True)
        saved[case]=joined(law,preps,rows)
        counts['unconditional_metric_and_terminal_laws']+=len(ARMS)

    # Configured donors are not asserted reachable under the primary parent law.
    architecture=producer.architecture
    base=architecture.State(fuel=12,patient=20,source=0,active=True,q=4,coupling=0,last=1,
        raw_r=0,raw_d=0,raw_w=2,raw_t=0,guides_e=3,r_nodes=(True,True),
        d_nodes=(True,True),graph=(1,1),retained=(True,True))
    laws=[producer.Law(),replace(producer.Law(),recipient_flip=0),
          replace(producer.Law(),availability=F(1,2)),
          replace(producer.Law(),recipient_flip=0,availability=F(1,2)),
          replace(producer.Law(),recipient_flip=0,reverse_after_first=True),
          replace(producer.Law(),availability=F(0)),
          replace(producer.Law(),observation=5),replace(producer.Law(),write=5),
          replace(producer.Law(),recode_cost=10),replace(producer.Law(),hold=4)]
    for law in laws:
        for fuel in range(21):
            for mask in (1,5,6):
                for coupling in (0,1):
                    for regime in (0,1):
                        entry=replace(base,fuel=fuel,coupling=coupling,graph=(1,mask),
                                      raw_w=4-1-mask.bit_count())
                        for arm in ARMS:
                            compare(law,entry,regime,arm)
                            counts['configured_comparisons']+=1
    for change in (dict(raw_w=0,graph=(6,5)),dict(retained=(True,False)),
                   dict(active=False,retained=(False,False)),dict(patient=0)):
        for arm in ARMS:
            compare(producer.Law(),replace(base,**change),1,arm)
            counts['missing_interface_comparisons']+=1
    for fuel in range(21):
        branches=reference(producer.Law(),replace(base,fuel=fuel),1,'indexed')
        assert sum(branch.probability for branch in branches if strict_reference(branch,replace(base,fuel=fuel))) == int(fuel>=11)
        assert int(any('R1.write.changed' in {event for event,_ in branch.trace} for branch in branches)) == int(fuel>=6)
        counts['sharp_fuel_thresholds']+=1

    assert F(saved['primary']['indexed']['p_strict_witness'])==F(11,405)
    assert F(saved['primary']['indexed']['p_prior_motor_revision_and_strict_witness'])==0
    after=source_hashes()
    assert before==after, ('scientific sources changed during check',
                          [name for name in set(before)|set(after) if before.get(name)!=after.get(name)])
    receipt=dict(status='passed',counts=dict(counts),source_hashes=after,
        scope='Independent protocol-based learning transitions and ordered provenance witness; exact full event/state distributions and unconditional laws. Parent reconstruction reuses separately independent architecture and coupling interpreters. Configured donors are not asserted reachable.',
        independently_reconstructed_rows=saved)
    (HERE/'independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(status='passed',counts=dict(counts)),indent=2))
    return receipt


def source_hashes():
    root = next(path for path in HERE.parents if (path/'RESEARCH.md').is_file())
    paths = [HERE/'independent_check.py',HERE/'handoff_check.py',HERE/'model.py',HERE/'PROTOCOL.md',
             HERE.parent/'independent_check.py',HERE.parent/'handoff_check.py',HERE.parent.parent/'check.py']
    paths += [path/'model.py' for path in HERE.parents if (path/'model.py').is_file()]
    paths += [path/'process.py' for path in HERE.parents if (path/'process.py').is_file()]
    return {str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(set(paths))}


if __name__ == '__main__':
    run()
