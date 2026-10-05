"""Independent preparation and coupling-prefix handoff for architecture formation.

The preparation is enumerated from seven local reactions below. The operational
prefix uses coupling/check.py::independent_events, never production advance.
This file owns no reference implementation of the new architecture suffix.
"""
from collections import defaultdict
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
_REFERENCES = {}


def reference_module(coupling):
    key = id(coupling)
    if key not in _REFERENCES:
        old = sys.modules.get('model')
        sys.modules['model'] = coupling
        try:
            spec = importlib.util.spec_from_file_location(
                '_architecture_prefix_reference_'+str(key), HERE.parent/'check.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        finally:
            if old is None:
                del sys.modules['model']
            else:
                sys.modules['model'] = old
        _REFERENCES[key] = module
    return _REFERENCES[key]


def independent_preparation(law):
    """Absorbing distribution and conversion, without production preparation."""
    initial = (0, 0, 0, 0, 0, law.initial_common, law.initial_source)
    waiting, terminal, visited = {initial: Q(1)}, defaultdict(Q), set()

    def rank(s):
        return 4*s[6]+2*(s[4]+s[5])+s[3]+s[0]+s[1]+int(s[2] != 0)

    while waiting:
        state = max(waiting, key=rank)
        mass = waiting.pop(state)
        visited.add(state)
        a, h, resident, intact, local, fuel, source = state
        free = 2-a-h-int(resident != 0)
        events = []

        def append(rate, **changes):
            if rate <= 0:
                return
            fields = dict(zip(('a','h','resident','intact','local','fuel','source'), state))
            fields.update(changes)
            successor = tuple(fields.values())
            assert rank(successor) < rank(state)
            events.append((Q(rate), successor))

        append((1-intact)*free*fuel, a=a+1, fuel=fuel-1)
        append((1-intact)*free*fuel, h=h+1, fuel=fuel-1)
        if resident == 0:
            append(a*fuel, a=a-1, resident=1, fuel=fuel-1)
            append(h*fuel, h=h-1, resident=2, fuel=fuel-1)
        if resident == 1 and not intact:
            append(fuel, intact=1, fuel=fuel-1)
        if intact and local == 0:
            append(source, source=source-1, local=1)
        if resident in (1, 2):
            append(free*local, local=0, **({'a': a+1} if resident == 1 else {'h': h+1}))
        if not events:
            terminal[state] += mass
        else:
            total = sum(rate for rate, _ in events)
            for rate, successor in events:
                waiting[successor] = waiting.get(successor, Q(0))+mass*rate/total
    assert sum(terminal.values()) == 1
    records = []
    for state, mass in sorted(terminal.items()):
        a, h, resident, intact, local, fuel, source = state
        energy = local+fuel+source
        ready = (a+int(resident == 1) == h+int(resident == 2) == 1
                 and intact == local == 1 and fuel >= law.adapter)
        row = dict(state=list(state), probability=str(mass), commissioned=ready,
                   preparation_spent=law.initial_common+law.initial_source-energy,
                   remaining_energy=energy)
        if ready:
            packets, remainder = divmod(source, law.packet)
            row.update(reserve=fuel-law.adapter+local, packets=packets,
                       remainder=remainder, transformed_A=1, transformed_H=1,
                       backing_slots=2)
            assert row['reserve']+packets*law.packet+remainder+law.adapter == energy
        assert row['preparation_spent'] >= 0
        records.append(row)
    return records, len(visited)


def independent_prefix(coupling, law, arm, reserve, steps=8):
    """Return ((initial regime, actual State) -> (mass, marked mass), counts)."""
    reference = reference_module(coupling)
    table = {(z, coupling.State(reserve)): (Q(1, 2), coupling.ZERO) for z in (0, 1)}
    counts = []
    for step in range(steps):
        following = {}
        events_count = 0
        for (z, state), (mass, marked_mass) in table.items():
            regime = z ^ (sum(t <= step for t in law.reversals) % 2)
            events = reference.independent_events(law, state, arm, regime)
            events_count += len(events)
            for (out, increment), probability in events.items():
                key = (z, out)
                old_mass, old_marks = following.get(key, (Q(0), coupling.ZERO))
                following[key] = (
                    old_mass+mass*probability,
                    tuple(a+probability*(b+mass*c)
                          for a, b, c in zip(old_marks, marked_mass, increment)))
        counts.append(dict(step=step, incoming_states=len(table), events=events_count,
                           outgoing_states=len(following)))
        table = following
        assert sum(mass for mass, _ in table.values()) == 1
        for (_, state), (mass, marks) in table.items():
            assert (mass*state.fuel+marks[coupling.MARKS.index('spent')]
                    +marks[coupling.MARKS.index('waste')]
                    == mass*(reserve+(step+1)*law.packet))
    return table, counts


def normalized(table):
    return {(z, tuple(asdict(state).items())): value
            for (z, state), value in table.items()}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes():
    root = HERE.parents[9]
    paths = {Path(__file__).resolve(), HERE/'PROTOCOL.md',
             HERE.parent/'check.py', HERE.parent/'PROTOCOL.md'}
    for module in tuple(sys.modules.values()):
        name = getattr(module, '__file__', None)
        if name:
            path = Path(name).resolve()
            if path.suffix == '.py' and path.is_relative_to(root):
                paths.add(path)
    return {str(path.relative_to(root)): digest(path) for path in sorted(paths)}


def audit_saved_results(producer, handoffs):
    """Check joined caller parity and mass/account preservation in saved output."""
    path = HERE/'results.json'
    frozen_result_hash = digest(path)
    saved = json.loads(path.read_text())
    root = HERE.parents[9]
    assert all(digest(root/name) == checksum
               for name, checksum in saved['source_sha256'].items())
    comparisons, terminal_count = 0, 0
    for case, law in producer.cases().items():
        result = saved['cases'][case]
        handoff = handoffs[case+'/'+result['prefix_arm']]
        expected = {(row['initial_regime'], tuple(row['inherited_state'].items())):
                    Q(row['unconditional_probability']) for row in handoff['branches']}
        preps, _ = independent_preparation(law.upstream_law())
        assert result['preparations'] == preps
        failed_mass = Q(handoff['failed_preparation_mass'])
        expected_prep_spent = sum(Q(row['probability'])*row['preparation_spent'] for row in preps)
        expected_failed_energy = sum(Q(row['probability'])*row['remaining_energy']
                                    for row in preps if not row['commissioned'])
        expected_prefix = {metric: sum(Q(row['unconditional_probability'])
            *Q(row['conditional_mean_marks'][metric]) for row in handoff['branches'])
            for metric in ('spent', 'waste')}
        for arm, output in result['arms'].items():
            observed = defaultdict(Q)
            totals = defaultdict(Q)
            for row in output['terminal_rows']:
                expected_regime = row['initial_regime'] ^ (
                    sum(t < law.prefix_steps for t in law.upstream_law().reversals) % 2)
                assert row['final_regime'] == expected_regime
                probability = Q(row['probability'])
                observed[row['initial_regime'], tuple(row['parent_state'].items())] += probability
                for field in ('fuel','patient','raw_r','raw_d','raw_w','raw_t'):
                    totals[field] += probability*row['state'][field]
                terminal_count += 1
            assert dict(observed) == expected
            assert sum(observed.values())+failed_mass == 1
            metrics = {key: Q(value) for key, value in output['metrics'].items()}
            assert metrics['preparation_spent'] == expected_prep_spent
            assert metrics['uncommissioned_energy'] == expected_failed_energy
            assert metrics['adapter_spent'] == (1-failed_mass)*law.upstream_law().adapter
            for field, initial in (('patient',law.patient_initial),
                    ('raw_r',law.receptor_parts), ('raw_d',law.comparator_parts),
                    ('raw_w',law.connector_parts), ('raw_t',law.template_parts)):
                assert metrics[field] == totals[field]+failed_mass*initial
            assert metrics['fuel'] == totals['fuel']
            assert metrics['prefix_spent'] == expected_prefix['spent']
            assert metrics['prefix_waste'] == expected_prefix['waste']
            expected_remainder = sum(Q(row['probability'])*(row['remainder']+
                (row['packets']-law.prefix_steps-2*law.rounds)*law.packet)
                for row in preps if row['commissioned'])
            assert metrics['source_remainder'] == expected_remainder
            fields = ('fuel','patient','spent','patient_used','damage','waste',
                      'prefix_spent','prefix_waste','preparation_spent','adapter_spent',
                      'uncommissioned_energy','source_remainder')
            assert sum(metrics[field] for field in fields) == handoff['full_initial_energy']
            comparisons += 1
    assert digest(path) == frozen_result_hash, 'Saved results changed during audit.'
    return dict(saved_case_suffix_arm_comparisons=comparisons,
                saved_terminal_rows_checked=terminal_count,
                failed_preparation_side_stocks_preserved=True,
                every_parent_mass_preserved=True, current_regime_parity_verified=True,
                production_results_sha256=frozen_result_hash)


def audit(producer):
    coupling = producer.upstream
    reference_module(coupling)
    before = source_hashes()
    cache, rows, failed_rows = {}, {}, {}
    eligibility_probes = 0
    for case, law in producer.cases().items():
        old_law = law.upstream_law()
        key = repr(old_law.record())
        if key not in cache:
            preps, visited = independent_preparation(old_law)
            cache[key] = {'preparation': (preps, visited), 'prefixes': {}}
        preps, visited = cache[key]['preparation']
        assert (preps, visited) == producer.preparation(law)
        assert old_law.initial_source == law.initial_source
        assert old_law.horizon == law.prefix_steps+2*law.rounds
        commissioned = sum(Q(row['probability']) for row in preps if row['commissioned'])
        failed_rows[case] = [row for row in preps if not row['commissioned']]
        for arm in producer.PREFIX_ARMS:
            output, starts, ends = [], 0, 0
            full_mass, expected_energy = 1-commissioned, Q(0)
            start_total = law.initial_common+law.initial_source+law.patient_initial
            for prep in preps:
                prep_mass = Q(prep['probability'])
                if not prep['commissioned']:
                    expected_energy += prep_mass*(prep['remaining_energy']
                        +prep['preparation_spent']+law.patient_initial)
                    continue
                cache_key = (arm, prep['reserve'], law.prefix_steps)
                if cache_key not in cache[key]['prefixes']:
                    cache[key]['prefixes'][cache_key] = independent_prefix(
                        coupling, old_law, arm, prep['reserve'], law.prefix_steps)
                independent, counts = cache[key]['prefixes'][cache_key]
                actual, _ = producer.prefix_distribution(law, arm, prep['reserve'])
                assert normalized(independent) == normalized(actual)
                starts += sum(row['incoming_states'] for row in counts)
                ends += len(independent)
                remainder = prep['remainder']+(prep['packets']-law.prefix_steps)*law.packet
                assert remainder == 2*law.rounds*law.packet
                for (z, state), (mass, marks) in sorted(independent.items(),
                        key=lambda item: (item[0][0], tuple(asdict(item[0][1]).values()))):
                    full_mass += prep_mass*mass
                    used = marks[coupling.MARKS.index('spent')]
                    lost = marks[coupling.MARKS.index('waste')]
                    ledger = mass*(prep['preparation_spent']+old_law.adapter
                                  +state.fuel+remainder+law.patient_initial)+used+lost
                    assert ledger == mass*start_total
                    expected_energy += prep_mass*ledger
                    expected_active = bool(state.stage == 2 and state.life > 0
                        and state.gate_life > 0 and state.coupling_life > 0
                        and state.coupling in (0, 1) and state.written
                        and state.q in (0, 4))
                    assert producer.eligible(state) == expected_active
                    if expected_active:
                        # Altered-state probes, not extra claimed upstream histories.
                        for q in (0, 4):
                            for orientation in (0, 1):
                                probe = coupling.State(**dict(asdict(state),
                                    q=q, coupling=orientation, witness=False))
                                assert producer.eligible(probe)
                                projected = producer.entrance(law, probe)
                                assert projected.active and projected.q == q
                                assert projected.coupling == orientation
                                eligibility_probes += 1
                    entered = producer.entrance(law, state)
                    expected = dict(fuel=state.fuel, patient=law.patient_initial,
                        source=remainder, active=expected_active, q=state.q,
                        coupling=state.coupling, last=state.last,
                        raw_r=law.receptor_parts, raw_d=law.comparator_parts,
                        raw_w=law.connector_parts, raw_t=law.template_parts)
                    assert all(getattr(entered, field) == value
                               for field, value in expected.items())
                    assert entered.spent == entered.waste == entered.damage == 0
                    assert entered.guides_e == entered.guides_i == entered.inert == 0
                    assert not any(entered.r_nodes+entered.d_nodes+entered.graph+entered.retained)
                    output.append(dict(initial_regime=z,
                        suffix_regime=z^(sum(t < law.prefix_steps for t in old_law.reversals) % 2),
                        preparation=prep, inherited_state=asdict(state),
                        conditional_probability=str(mass),
                        unconditional_probability=str(prep_mass*mass),
                        conditional_mean_marks={name: str(value/mass)
                            for name, value in zip(coupling.MARKS, marks)},
                        entrance=asdict(entered)))
                assert sum(mass for mass, _ in independent.values()) == 1
            assert full_mass == 1 and expected_energy == start_total
            rows[case+'/'+arm] = dict(preparation_visited=visited,
                preparation_terminals=len(preps), commissioned_mass=str(commissioned),
                failed_preparation_mass=str(1-commissioned),
                independent_prefix_states_evaluated=starts, terminal_prefix_states=ends,
                total_mass=str(full_mass), full_initial_energy=start_total,
                full_handoff_energy=str(expected_energy), branches=output)
    saved_checks = audit_saved_results(producer, rows)
    assert source_hashes() == before, 'Dependency changed during handoff audit.'
    return dict(status='pass', scope='Preparation, eight-slot coupling prefix and architecture entrance only; not new suffix.',
        independent_event_reference='coupling/check.py::independent_events',
        compared_case_producer_pairs=len(rows), unique_preparation_laws=len(cache),
        altered_state_eligibility_probes=eligibility_probes,
        eligibility_probe_scope='Counterfactual q/coupling combinations and witness=False; not additional realized histories.',
        rows=rows, failed_preparation_records=failed_rows,
        saved_result_checks=saved_checks, source_sha256=before)


if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('_architecture_handoff_producer', HERE/'model.py')
    producer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = producer
    spec.loader.exec_module(producer)
    result = audit(producer)
    (HERE/'handoff-check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in
                     ('status','compared_case_producer_pairs','unique_preparation_laws')}))
