"""Independent mutable-state implementation of the local assembly protocol.

The public producer dataclasses specify the comparison interface. This reference
does not call its entrance, eligibility, complete, topology, graph traversal or
suffix implementation. The inherited preparation/prefix has a separate helper.
"""
from collections import defaultdict
from copy import deepcopy
from dataclasses import asdict, fields, replace
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import model as producer
import handoff_check

HERE = Path(__file__).resolve().parent
STATE_FIELDS = tuple(field.name for field in fields(producer.State))
ARMS = ('live', 'conventional', 'frozen', 'filter_copy', 'no_build')


def frozen(values):
    data = dict(values)
    for key in ('r_nodes', 'd_nodes', 'graph', 'retained'):
        data[key] = tuple(data[key])
    return producer.State(**data)


def key(state):
    return tuple(getattr(state, field) for field in STATE_FIELDS)


def reference(law, parent, regime, arm):
    """Enumerate microhistories by an independently written event interpreter."""
    assert arm in ARMS
    active = (parent.stage == 2 and parent.life > 0 and parent.gate_life > 0
              and parent.coupling_life > 0 and parent.coupling in (0, 1)
              and parent.written and parent.q in (0, 4))
    values = dict(fuel=parent.fuel, patient=law.patient_initial,
                  source=4*law.packet, active=bool(active), q=parent.q,
                  coupling=parent.coupling, last=parent.last,
                  raw_r=law.receptor_parts, raw_d=law.comparator_parts,
                  raw_w=law.connector_parts, raw_t=law.template_parts,
                  guides_e=0, guides_i=0, inert=0,
                  r_nodes=[False, False], d_nodes=[False, False],
                  graph=[0, 0], retained=[False, False], spent=0,
                  patient_used=0, damage=0, waste=0, actor_attempts=0,
                  recipient_attempts=0, actor_captures=0,
                  recipient_captures=0, copy_events=0, paid_holds=0,
                  rent_events=0, sensed=0)
    total = parent.fuel+law.patient_initial+4*law.packet

    def validate(s):
        assert all(s[v] >= 0 for v in ('fuel', 'patient', 'source', 'spent',
                                      'patient_used', 'damage', 'waste',
                                      'raw_r', 'raw_d', 'raw_w', 'raw_t'))
        assert sum(s[v] for v in ('fuel', 'patient', 'source', 'spent',
                                  'patient_used', 'damage', 'waste')) == total
        assert s['raw_r']+sum(s['r_nodes']) == law.receptor_parts
        assert s['raw_d']+sum(s['d_nodes']) == law.comparator_parts
        assert s['raw_w']+sum(mask.bit_count() for mask in s['graph']) == law.connector_parts
        assert s['raw_t']+s['guides_e']+s['guides_i']+s['inert'] == law.template_parts
        for j, mask in enumerate(s['graph']):
            assert not (mask & 1 and mask & 2)
            assert not (mask & 3) or s['r_nodes'][j]
            assert not (mask & 6) or s['d_nodes'][j]
            assert not s['retained'][j] or (s['active'] and path(s, j))
        assert (s['q'], s['coupling']) == (parent.q, parent.coupling)

    def path(s, j):
        edges = s['graph'][j]
        return bool(edges & 1 or (edges & 2 and edges & 4))

    def emit(branch, event):
        s, probability, trace = branch
        validate(s)
        trace.append((event, frozen(s)))

    def payable(branch, amount):
        s = branch[0]
        if s['fuel'] < amount:
            return False
        s['fuel'] -= amount
        s['spent'] += amount
        return True

    start = (values, F(1), [])
    validate(values)
    if active and arm != 'no_build' and values['raw_t'] and payable(start, law.guide_cost):
        values['raw_t'] -= 1
        values['guides_e'] += 1
        emit(start, 'guide.seed')
    branches = [start]

    for j in range(2):
        constructed = []
        for branch in branches:
            s = branch[0]
            if s['active'] and arm != 'no_build':
                for letter, price in (('r', law.receptor_cost), ('d', law.comparator_cost)):
                    if s['raw_'+letter] and payable(branch, price):
                        s['raw_'+letter] -= 1
                        s[letter+'_nodes'][j] = True
                        emit(branch, f'r{j}.'+('receptor' if letter == 'r' else 'comparator'))
            pending = [branch]
            while pending:
                current = pending.pop()
                x, mass, trace = current
                mask = x['graph'][j]
                candidates = []
                if x['active'] and arm != 'no_build' and x['raw_w'] and not path(x, j):
                    if x['r_nodes'][j] and mask & 3 == 0:
                        candidates.append((1, x['guides_e'], law.bond_cost))
                        if x['d_nodes'][j]:
                            candidates.append((2, law.identity_affinity*(1+x['guides_i']),
                                               law.gate_bond_cost))
                    if x['d_nodes'][j] and mask & 4 == 0:
                        candidates.append((4, x['guides_e'], law.bond_cost))
                candidates = [(edge, F(rate), cost) for edge, rate, cost in candidates
                              if rate > 0 and cost <= x['fuel']]
                if not candidates:
                    constructed.append(current)
                    continue
                rate_total = sum(rate for _, rate, _ in candidates)
                for edge, rate, price in candidates:
                    successor = (deepcopy(x), mass*rate/rate_total, list(trace))
                    y = successor[0]
                    assert payable(successor, price)
                    y['raw_w'] -= 1
                    y['graph'][j] |= edge
                    emit(successor, f'r{j}.bind.'+{1:'RP', 2:'RD', 4:'DP'}[edge])
                    pending.append(successor)

        for branch in constructed:
            s = branch[0]
            for target in ('actor', 'recipient'):
                action = None
                if s['active'] and s['r_nodes'][j]:
                    if payable(branch, law.rent):
                        s['rent_events'] += 1
                        emit(branch, f'r{j}.{target}.rent')
                        if payable(branch, law.sensing):
                            s['sensed'] += 1
                            emit(branch, f'r{j}.{target}.sense')
                            # Traverse node connections and the local comparator.
                            cursor = 'R'
                            while cursor not in ('P', 'blocked'):
                                if cursor == 'R':
                                    cursor = ('P' if s['graph'][j] & 1 else
                                              'D' if s['graph'][j] & 2 else 'blocked')
                                elif cursor == 'D':
                                    cursor = ('P' if target == 'actor' and s['graph'][j] & 4
                                              else 'blocked')
                            if cursor == 'P' and payable(branch, law.work):
                                predicted = 0 if s['q'] < 2 else 1 if s['q'] > 2 else s['last']
                                action = predicted ^ s['coupling']
                                s['last'] = action
                                s[target+'_attempts'] += 1
                                emit(branch, f'r{j}.{target}.work')
                    else:
                        s['active'] = False
                        s['retained'] = [False, False]
                        emit(branch, f'r{j}.{target}.lose_predictor')
                correct = action is not None and action == (regime if target == 'actor'
                                                           else regime ^ law.recipient_flip)
                if target == 'recipient' and action is not None and not correct:
                    loss = min(s['patient'], law.harm)
                    s['patient'] -= loss
                    s['damage'] += loss
                    emit(branch, f'r{j}.{target}.damage')
                actor_before_receipt = s['fuel']
                s['source'] -= law.packet
                if correct:
                    s['fuel' if target == 'actor' else 'patient'] += law.packet
                    s[target+'_captures'] += 1
                else:
                    s['waste'] += law.packet
                if target == 'recipient':
                    assert s['fuel'] == actor_before_receipt
                emit(branch, f'r{j}.{target}.'+('receipt' if correct else 'spill'))
                if target == 'actor' and correct:
                    assert payable(branch, law.route_upkeep)
                    emit(branch, f'r{j}.{target}.route_upkeep')
                    if s['raw_t'] and (arm != 'filter_copy' or any(s['d_nodes'])) and payable(branch, law.copy_cost):
                        s['raw_t'] -= 1
                        product = 'guides_i' if arm == 'filter_copy' else 'inert' if arm == 'frozen' else 'guides_e'
                        s[product] += 1
                        s['copy_events'] += 1
                        emit(branch, f'r{j}.{target}.copy.'+
                             {'guides_e':'P','guides_i':'D','inert':'inert'}[product])
                elif target == 'recipient' and correct:
                    s['patient'] -= law.patient_use
                    s['patient_used'] += law.patient_use
                    emit(branch, f'r{j}.{target}.use')

            for old in range(j+1):
                if s['active'] and (s['retained'][old] or old == j and path(s, old)):
                    if payable(branch, law.hold_cost):
                        s['retained'][old] = True
                        s['paid_holds'] += 1
                        emit(branch, f'r{j}.hold{old}')
                    else:
                        s['retained'][old] = False
                        emit(branch, f'r{j}.lose{old}')
        branches = constructed

    answer = []
    for s, probability, trace in branches:
        validate(s)
        assert s['source'] == 0
        answer.append(producer.Branch(frozen(s), probability, tuple(trace)))
    assert sum(branch.probability for branch in answer) == 1
    return tuple(answer)


def distribution(branches):
    out = defaultdict(F)
    for branch in branches:
        out[key(branch.state)] += branch.probability
    return dict(out)


def changed_states(branch):
    """Trace comparison ignores labels and repeated diagnostic-only snapshots."""
    out = []
    for _, state in branch.trace:
        now = key(state)
        if not out or now != out[-1]:
            out.append(now)
    return tuple(out)


def trace_distribution(branches):
    out = defaultdict(F)
    for branch in branches:
        out[changed_states(branch)] += branch.probability
    return dict(out)


def complete_trace_distribution(branches):
    result = defaultdict(F)
    for branch in branches:
        result[tuple((event, key(state)) for event, state in branch.trace)] += branch.probability
    return dict(result)


def compare(law, donor, regime, arm):
    actual = producer.suffix(law, donor, regime, arm)
    expected = reference(law, donor, regime, arm)
    assert distribution(actual) == distribution(expected), ('terminal', law, donor, regime, arm)
    assert complete_trace_distribution(actual) == complete_trace_distribution(expected), (
        'complete_microhistory', law, donor, regime, arm)
    return expected


def first_boundary(branches):
    """Compare matched first-round resources after ignoring guide product type."""
    result = defaultdict(F)
    for branch in branches:
        boundary = None
        for event, state in branch.trace:
            if event.startswith('r1.'):
                break
            boundary = state
        if boundary is None:
            boundary = branch.state
        data = asdict(boundary)
        for name in ('guides_e', 'guides_i', 'inert'):
            data.pop(name)
        result[tuple((name, tuple(value) if isinstance(value, list) else value)
                     for name, value in data.items())] += branch.probability
    return dict(result)


def assembly_formulas():
    """Closed-form checks independent of both recursive assembly algorithms."""
    checks = 0
    for e in range(1, 7):
        for i in range(4):
            for affinity in (F(1, 2), F(1), F(3), F(8)):
                law = replace(producer.Law(), identity_affinity=affinity,
                              template_parts=e+i, connector_parts=2)
                donor = producer.upstream.State(20)
                initial = dict(fuel=20, patient=4, source=40, active=True,
                               q=4, coupling=0, last=1, raw_r=1, raw_d=1,
                               raw_w=2, raw_t=0, guides_e=e, guides_i=i,
                               r_nodes=(True,False), d_nodes=(True,False))
                state = producer.State(**initial)
                branches = producer.assemble(law, producer.Branch(state), 0)
                totals = defaultdict(F)
                for branch in branches:
                    totals[branch.state.graph[0]] += branch.probability
                c = affinity*(1+i)
                assert totals == {1:F(e, 2*e+c),
                                  5:F(e*e, (2*e+c)*(e+c)),
                                  6:F(c, e+c)}
                assert totals[1]+totals[5] == F(e, e+c)
                assert sum(branch.probability*branch.state.graph[0].bit_count()
                           for branch in branches) == 2-F(e, 2*e+c)
                for changed in (replace(state, fuel=1), replace(state, raw_w=1)):
                    constrained = producer.assemble(law, producer.Branch(changed), 0)
                    assert sum(branch.probability for branch in constrained
                               if branch.state.graph[0] == 1) == F(e, 2*e+c)
                    assert all(branch.state.graph[0] in (1,2,4) for branch in constrained)
                    checks += 1
                checks += 1
    return checks


def joined_rows(laws, cache):
    """Independently weight every new suffix by retained preparation/prefix mass."""
    rows = {}
    for case, law in laws.items():
        preparation, _ = handoff_check.independent_preparation(law.upstream_law())
        report = producer.compare(law)
        for arm in ARMS:
            out = defaultdict(F)
            expected_metrics = defaultdict(F)
            expected_terminal = defaultdict(F)
            for row in preparation:
                preparation_mass = F(row['probability'])
                out['preparation_spent'] += preparation_mass*row['preparation_spent']
                expected_metrics['preparation_spent'] += preparation_mass*row['preparation_spent']
                if not row['commissioned']:
                    # Old source stays in its original physical form on these paths.
                    out['uncommissioned_energy'] += preparation_mass*row['remaining_energy']
                    out['uncommissioned_patient'] += preparation_mass*law.patient_initial
                    expected_metrics['uncommissioned_energy'] += preparation_mass*row['remaining_energy']
                    expected_metrics['patient'] += preparation_mass*law.patient_initial
                    for part, count in (('raw_r',law.receptor_parts),('raw_d',law.comparator_parts),
                                        ('raw_w',law.connector_parts),('raw_t',law.template_parts)):
                        expected_metrics[part] += preparation_mass*count
                    continue
                out['p_prepared'] += preparation_mass
                out['adapter_spent'] += preparation_mass*law.upstream_law().adapter
                expected_metrics['p_commissioned'] += preparation_mass
                expected_metrics['adapter_spent'] += preparation_mass*law.upstream_law().adapter
                expected_metrics['source_remainder'] += preparation_mass*(row['remainder']+(row['packets']-12)*law.packet)
                table = cache[(law.initial_common, row['reserve'])]
                for (z, donor), (mass, marked_mass) in table.items():
                    out['prefix_spent'] += preparation_mass*marked_mass[producer.upstream.MARKS.index('spent')]
                    out['prefix_waste'] += preparation_mass*marked_mass[producer.upstream.MARKS.index('waste')]
                    for charge in ('spent','waste'):
                        expected_metrics['prefix_'+charge] += preparation_mass*marked_mass[producer.upstream.MARKS.index(charge)]
                    admitted = (donor.stage == 2 and donor.life > 0 and donor.gate_life > 0
                                and donor.coupling_life > 0 and donor.coupling in (0,1)
                                and donor.written and donor.q in (0,4))
                    expected_metrics['p_eligible'] += preparation_mass*mass*int(admitted)
                    current_regime = z ^ (sum(step < law.prefix_steps
                                             for step in law.upstream_law().reversals) % 2)
                    for branch in reference(law, donor, current_regime, arm):
                        weight = preparation_mass*mass*branch.probability
                        state = branch.state
                        expected_terminal[(z,tuple(asdict(donor).items()),key(state))] += weight
                        for name,value in independent_metrics(branch).items():
                            expected_metrics[name] += weight*value
                        expected_metrics['p_prior_revision_and_recipient_use'] += weight*int(donor.witness and state.recipient_captures > 0)
                        for name in ('fuel','patient','source','spent','patient_used',
                                     'damage','waste','actor_attempts','recipient_attempts',
                                     'actor_captures','recipient_captures','copy_events','paid_holds'):
                            out[name] += weight*getattr(state, name)
                        out['p_recipient_use'] += weight*int(state.recipient_captures > 0)
                        out['p_prior_revision_and_recipient_use'] += weight*int(
                            donor.witness and state.recipient_captures > 0)
                        out['final_retained_graphs'] += weight*sum(state.retained)
                        out['p_both_retained'] += weight*int(all(state.retained))
                        for j, mask in enumerate(state.graph):
                            kind = ('direct' if mask & 1 else 'filtered' if mask & 2 and mask & 4
                                    else 'partial')
                            out[f'round{j}_{kind}'] += weight
                            out[f'round{j}_retained_{kind}'] += weight*state.retained[j]
            energy_terms = ('preparation_spent','adapter_spent','prefix_spent','prefix_waste',
                            'uncommissioned_energy','uncommissioned_patient',
                            'fuel','patient','source','spent','patient_used','damage','waste')
            assert sum(out[name] for name in energy_terms) == law.initial_common+law.initial_source+law.patient_initial
            observed = {name:F(value) for name,value in report['arms'][arm]['metrics'].items()}
            assert dict(expected_metrics) == observed, ('joined_metrics',case,arm,
                {name:(expected_metrics.get(name),observed.get(name)) for name in set(expected_metrics)|set(observed)
                 if expected_metrics.get(name) != observed.get(name)})
            observed_terminal = {}
            for row in report['arms'][arm]['terminal_rows']:
                assert row['final_regime'] == row['initial_regime'] ^ 1
                observed_terminal[(row['initial_regime'],tuple(row['parent_state'].items()),
                                   key(frozen(row['state'])))] = F(row['probability'])
            assert dict(expected_terminal) == observed_terminal, ('joined_terminal',case,arm)
            rows[(case,arm)] = dict(out)
        assert rows[(case,'live')] == rows[(case,'conventional')]
    return rows


def independent_metrics(branch):
    state = branch.state
    result = {name:getattr(state,name) for name in
              ('fuel','patient','spent','patient_used','damage','waste','actor_attempts',
               'recipient_attempts','actor_captures','recipient_captures','copy_events',
               'paid_holds','rent_events','sensed','guides_e','guides_i','inert',
               'raw_r','raw_d','raw_w','raw_t')}
    result.update(p_active_predictor=int(state.active),p_recipient_use=int(state.recipient_captures>0),
                  p_both_actor_captures=int(state.actor_captures==2),
                  p_both_recipient_captures=int(state.recipient_captures==2))
    for j,mask in enumerate(state.graph):
        direct=bool(mask & 1)
        filtered=bool(mask & 2 and mask & 4)
        result.update({f'r{j}_receptor':int(state.r_nodes[j]),f'r{j}_comparator':int(state.d_nodes[j]),
                       f'r{j}_complete':int(direct or filtered),f'r{j}_direct':int(direct),
                       f'r{j}_filtered':int(filtered),f'r{j}_unused_DP':int(bool(direct and mask & 4)),
                       f'r{j}_retained':int(state.retained[j]),
                       f'r{j}_retained_direct':int(state.retained[j] and direct),
                       f'r{j}_retained_filtered':int(state.retained[j] and filtered)})
        events=[event for event,_ in branch.trace]
        for target in ('actor','recipient'):
            result[f'r{j}_{target}_used']=int(f'r{j}.{target}.work' in events)
            result[f'r{j}_{target}_capture']=int(f'r{j}.{target}.receipt' in events)
        result[f'r{j}_immediate_hold']=int(f'r{j}.hold{j}' in events)
    return result


def run():
    before = source_hashes()
    assert producer.ARMS == ARMS
    laws = producer.cases()
    assert tuple(laws) == ('primary','cheap_gate','gate_affinity_only','gate_price_only',
                          'harmful_transfer','low_original_reserve','expensive_receptor',
                          'one_connector','no_copy_material','costly_retention')
    cache, counts = {}, defaultdict(int)
    for case, law in laws.items():
        preparation, _ = handoff_check.independent_preparation(law.upstream_law())
        for row in preparation:
            if not row['commissioned']:
                continue
            k = (law.initial_common, row['reserve'])
            if k not in cache:
                cache[k], _ = handoff_check.independent_prefix(
                    producer.upstream, law.upstream_law(), 'variable', row['reserve'])
            for (z, donor), (mass, marks) in cache[k].items():
                results = {}
                for arm in ARMS:
                    results[arm] = compare(law, donor, z ^ 1, arm)
                    counts['reachable_comparisons'] += 1
                    counts['reachable_branches'] += len(results[arm])
                assert complete_trace_distribution(results['live']) == complete_trace_distribution(results['conventional'])
                assert first_boundary(results['live']) == first_boundary(results['frozen']) == first_boundary(results['filter_copy'])
                counts['matched_first_round_controls'] += 1

    # Configured interventions are deliberately separate from reachable histories.
    configured_laws = dict(laws)
    for name, update in (('no_receptor',dict(receptor_parts=0)),
                         ('no_comparator',dict(comparator_parts=0)),
                         ('no_connector',dict(connector_parts=0)),
                         ('no_initial_guide',dict(template_parts=0)),
                         ('no_patient_stock',dict(patient_initial=0)),
                         ('high_hold_bill',dict(hold_cost=20))):
        configured_laws[name] = replace(producer.Law(), **update)
    for law in configured_laws.values():
        for fuel in range(31):
            for coupling in (0,1):
                for regime in (0,1):
                    donor = producer.upstream.State(fuel, gate_life=2, stage=2, life=6,
                                                   q=4, last=0, written=True,
                                                   coupling=coupling, coupling_life=2)
                    for arm in ARMS:
                        compare(law, donor, regime, arm)
                        counts['configured_comparisons'] += 1
    for missing in ('life','gate_life','coupling_life','stage','written'):
        donor = producer.upstream.State(25,gate_life=2,stage=2,life=6,q=0,last=1,
                                       written=True,coupling=1,coupling_life=2)
        donor = replace(donor, **{missing:0})
        for arm in ARMS:
            compare(producer.Law(),donor,1,arm)
            counts['ineligible_comparisons'] += 1
    counts['assembly_formula_comparisons'] = assembly_formulas()
    rows = joined_rows(laws,cache)
    counts['unconditional_aggregate_and_terminal_laws'] = len(rows)
    assert rows['primary','live']['recipient_captures'] == F(17,108)
    assert rows['primary','live']['p_recipient_use'] == F(13,108)
    assert rows['primary','live']['p_prior_revision_and_recipient_use'] == F(1,36)
    assert rows['primary','frozen']['recipient_captures'] == F(5,36)
    assert rows['primary','filter_copy']['recipient_captures'] == F(13,108)
    for arm in ('live','conventional','frozen','filter_copy'):
        assert rows['primary',arm]['final_retained_graphs'] == F(2,9)
    after = source_hashes()
    assert before == after, ('scientific source changed during independent check',
                            [name for name in set(before)|set(after)
                             if before.get(name) != after.get(name)])
    output = dict(status='passed', counts=dict(counts),
                  scope='Independent suffix event interpreter; exact complete event/state traces, terminal distributions, physical prefix invariants and unconditional accounts. Existing independent coupling-event evaluator reused for the inherited prefix. Configured diagnostics are not claimed reachable.',
                  source_hashes=after,
                  independently_reconstructed_rows={case+'::'+arm:{name:str(value) for name,value in row.items()}
                                                    for (case,arm),row in rows.items()})
    (HERE/'independent-check.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(status='passed',counts=dict(counts)),indent=2))
    return output


def source_hashes():
    root = next(path for path in HERE.parents if (path/'RESEARCH.md').is_file())
    paths = [HERE/'independent_check.py', HERE/'model.py', HERE/'PROTOCOL.md',
             HERE/'handoff_check.py', HERE.parent/'check.py']
    paths += [path/'model.py' for path in HERE.parents if (path/'model.py').is_file()]
    paths += [path/'process.py' for path in HERE.parents if (path/'process.py').is_file()]
    return {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(set(paths))}


if __name__ == '__main__':
    run()
