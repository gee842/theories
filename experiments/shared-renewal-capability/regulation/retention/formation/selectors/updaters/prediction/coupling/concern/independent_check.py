"""Independent mutable-ledger suffix and exogenous-draw predecessor audit.

The reference suffix never calls the producer's suffix, eligible, or command.
The predecessor is reconstructed with the independently written event evaluator
in coupling/check.py, not coupling/model.py::advance.
"""
from collections import defaultdict
from dataclasses import asdict, replace
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

import model as producer

HERE = Path(__file__).resolve().parent
c = producer.up
_old_model = sys.modules['model']
sys.modules['model'] = c
_spec = importlib.util.spec_from_file_location('_concern_prior_independent', HERE.parent/'check.py')
prior_check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prior_check)
sys.modules['model'] = _old_model

EXPECTED_MODES = ('shared', 'no_build', 'identity_gate', 'mask', 'temporary_disable',
                  'permanent_disable', 'budget_lock', 'reverse', 'reverse_restore',
                  'cheap_gate', 'free_block')
EXPECTED_CASES = ('primary', 'no_deficit', 'wrong_transfer', 'no_private_opportunity',
                  'patient_source_outage')


def reference(state, regime, mode, case='primary'):
    """Execute the protocol with separate actor, recipient and source purses."""
    assert mode in EXPECTED_MODES and case in EXPECTED_CASES
    x = dict(fuel=state.fuel, patient=0, source=30, spent=0, waste=0,
             live=bool(state.stage == 2 and state.life >= 1 and state.gate_life >= 1
                       and state.coupling_life >= 1 and state.written and state.q in (0, 4)),
             installed=False, coupling=state.coupling)
    original = state.fuel + 30
    trace, issued = [], []
    counts = dict(patient_action=0, patient_capture=0, patient_use=0,
                  actor_captures=0, actor_receipt=0, patient_receipt=0)

    def log(label):
        assert all(x[k] >= 0 for k in ('fuel', 'patient', 'source', 'spent', 'waste'))
        assert sum(x[k] for k in ('fuel', 'patient', 'source', 'spent', 'waste')) == original
        trace.append(dict(event=label, **x))

    def charge(amount, label):
        if amount > x['fuel']:
            log(label+'_unaffordable')
            return False
        x['spent'] += amount
        x['fuel'] -= amount
        log(label)
        return True

    def settle(target, success):
        actor_before = x['fuel']
        x['source'] -= 10
        if success:
            x['patient' if target == 'patient' else 'fuel'] += 10
            counts[target+'_receipt'] += 10
        else:
            x['waste'] += 10
        if target == 'patient':
            assert x['fuel'] == actor_before  # no private receipt from patient success
        log(target+('_capture' if success else '_packet_lost'))

    def select():
        threshold = 0 if state.q < 2 else (1 if state.q > 2 else state.last)
        return threshold if x['coupling'] == 0 else 1-threshold

    log('handoff')
    build = mode != 'no_build' and x['live']
    if build and charge(2, 'target_retrofit'):
        x['installed'] = True
        log('target_enabled')
    else:
        x['live'] = False
        log('no_target_access')

    patient_blocked, switch_changed = False, False
    if x['installed'] and x['live']:
        prices = {'identity_gate': 6, 'cheap_gate': 1}
        if mode in prices:
            patient_blocked = charge(prices[mode], 'identity_gate')
        elif mode == 'free_block':
            patient_blocked = True
            log('free_patient_trigger_block')
        elif mode in ('temporary_disable', 'permanent_disable'):
            x['live'] = False
            log('disabled')
        elif mode == 'budget_lock':
            charge(x['fuel'], 'irreversible_budget_lock')
            x['live'] = False
        elif mode in ('reverse', 'reverse_restore'):
            switch_changed = charge(1, 'switch_retool')
            if switch_changed:
                x['coupling'] = 1-x['coupling']
                log('switch_reversed')

    patient_success = False
    if x['live']:
        held = charge(1, 'patient_phase_retention')
        if not held:
            x['live'] = False
        elif not patient_blocked:
            observed = charge(1, 'patient_observation')
            if observed:
                trigger = case != 'no_deficit'
                if mode == 'mask':
                    if charge(6, 'patient_mask'):
                        trigger = False
                if trigger and charge(3, 'patient_work'):
                    choice = select()
                    issued.append(('patient', choice))
                    counts['patient_action'] = 1
                    patient_success = (choice == (1-regime if case == 'wrong_transfer' else regime)
                                       and case != 'patient_source_outage')
                    counts['patient_capture'] = int(patient_success)
    settle('patient', patient_success)

    if x['installed'] and mode == 'temporary_disable':
        if charge(7, 'restore_escrowed_circuit'):
            x['live'] = True
            log('restored')
    if x['installed'] and mode == 'reverse_restore' and switch_changed:
        if charge(1, 'restore_switch'):
            x['coupling'] = 1-x['coupling']
            log('switch_restored')

    for phase in range(2):
        actor_success = False
        if x['live']:
            if not charge(1, 'actor_retention_'+str(phase)):
                x['live'] = False
            elif charge(3, 'actor_work_'+str(phase)):
                choice = select()
                issued.append(('actor', choice))
                actor_success = choice == regime and case != 'no_private_opportunity'
                counts['actor_captures'] += int(actor_success)
        settle('actor', actor_success)

    if x['patient']:
        x['patient'] -= 1
        x['spent'] += 1
        counts['patient_use'] = 1
        log('patient_use')
    assert x['source'] == 0
    assert counts['actor_receipt'] == 10*counts['actor_captures']
    assert counts['patient_receipt'] == 10*counts['patient_capture']
    assert x['patient'] == counts['patient_receipt']-counts['patient_use']

    # Execute, rather than assume, every finite paid hold in the suffix tail.
    memory = (state.q, state.last, state.written, x['coupling'])
    tail_fuel, tail_spent, holds = x['fuel'], x['spent'], 0
    if x['installed'] and x['live']:
        while tail_fuel >= 1:
            tail_fuel -= 1
            tail_spent += 1
            holds += 1
            assert tail_fuel+x['patient']+tail_spent+x['waste'] == original
            assert memory == (state.q, state.last, state.written, x['coupling'])
    tail = dict(paid_holds=holds, fuel_after=tail_fuel, spent_after=tail_spent,
                patient_after=x['patient'], waste=x['waste'])
    answer = {k: x[k] for k in ('fuel','patient','source','spent','waste','installed','live')}
    answer.update(counts, maintenance_holds=holds, tail=tail, issued=issued, trace=trace)
    return answer


def independent_prefix(law, arm, reserve):
    distribution = {(z, c.State(reserve)): (F(1, 2), c.ZERO) for z in (0, 1)}
    evaluated = 0
    for t in range(8):
        following = {}
        for (z, state), (mass, marked_mass) in distribution.items():
            hidden = z ^ (sum(v <= t for v in law.reversals) % 2)
            events = prior_check.independent_events(law, state, arm, hidden)
            evaluated += 1
            for (new_state, marks), chance in events.items():
                key = (z, new_state)
                old_mass, old_marks = following.get(key, (F(0), c.ZERO))
                following[key] = (old_mass+mass*chance,
                    tuple(old+chance*(acc+mass*increment)
                          for old, acc, increment in zip(old_marks, marked_mass, marks)))
        distribution = following
        assert sum(mass for mass, _ in distribution.values()) == 1
    return distribution, evaluated


def source_hashes():
    paths = [HERE/'independent_check.py', HERE/'model.py', HERE/'PROTOCOL.md', HERE.parent/'check.py']
    # Track the entire imported chain of local model modules and original process.
    paths += [p/'model.py' for p in HERE.parents if (p/'model.py').is_file()]
    paths += [p/'process.py' for p in HERE.parents if (p/'process.py').is_file()]
    root = next(p for p in HERE.parents if (p/'RESEARCH.md').is_file())
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths))}


def run():
    before = source_hashes()
    assert producer.MODES == EXPECTED_MODES and producer.CASES == EXPECTED_CASES
    law = c.Law(horizon=11, reversals=(4,))
    prep_count, terminal_count = prior_check.independent_preparation(law)
    preparation, _ = c.prepare(law)
    commissioned = sum(F(r['probability']) for r in preparation if r['commissioned'])
    assert commissioned == F(2, 9)
    tables, prefix_checks, suffix_checks = {}, 0, 0
    for arm in producer.ARMS:
        for reserve in sorted({r['reserve'] for r in preparation if r['commissioned']}):
            table, count = independent_prefix(law, arm, reserve)
            assert table == producer.prefix(law, arm, reserve), ('prefix', arm, reserve)
            tables[arm, reserve] = table
            prefix_checks += count
            for (z0, state), (mass, _) in table.items():
                assert mass > 0
                regime = z0 ^ 1
                original_state = asdict(state)
                for mode in EXPECTED_MODES:
                    for case in EXPECTED_CASES:
                        actual = producer.suffix(state, regime, mode, case)
                        expected = reference(state, regime, mode, case)
                        assert actual == expected, ('suffix', state, regime, mode, case, actual, expected)
                        assert asdict(state) == original_state
                        suffix_checks += 1
    for record in preparation:
        if record['commissioned']:
            assert tables['variable', record['reserve']] == tables['conventional', record['reserve']]

    # Independently reconstruct every unconditional output and the whole history ledger.
    metrics = ('fuel','patient','spent','waste','patient_action','patient_capture',
               'patient_use','actor_receipt','patient_receipt','maintenance_holds')
    rows = {}
    for arm in producer.ARMS:
        for mode in EXPECTED_MODES:
            for case in EXPECTED_CASES:
                out = defaultdict(F)
                for r in preparation:
                    p = F(r['probability'])
                    out['preparation_spent'] += p*r['preparation_spent']
                    if not r['commissioned']:
                        out['uncommissioned_energy'] += p*r['remaining_energy']
                        continue
                    out['adapter_spent'] += p*law.adapter
                    out['p_prepared'] += p
                    for (z0, state), (mass, mark_mass) in tables[arm,r['reserve']].items():
                        result = reference(state, z0 ^ 1, mode, case)
                        out['prefix_spent'] += p*mark_mass[c.MARKS.index('spent')]
                        out['prefix_waste'] += p*mark_mass[c.MARKS.index('waste')]
                        for key in metrics:
                            out[key] += p*mass*result[key]
                        out['p_revised_coupling_and_patient_use'] += p*mass*int(state.witness and result['patient_use'])
                        out['p_interface'] += p*mass*int(result['installed'])
                        out['source_remainder'] += p*mass*r['remainder']
                balance = sum(out[k] for k in ('fuel','patient','spent','waste','preparation_spent',
                    'adapter_spent','uncommissioned_energy','prefix_spent','prefix_waste','source_remainder'))
                assert balance == law.initial_common+law.initial_source
                out['original_energy'] = balance
                rows[f'{arm}/{mode}/{case}'] = {k:str(v) for k,v in sorted(out.items())}
    produced = producer.run()
    assert rows == produced['rows']

    # Actual reachable witness, then separate interventions; low reserves are
    # hypothetical perturbations and never presented as extra observed histories.
    witness = produced['witness']
    s = c.State(**witness['state'])
    z = witness['regime']
    assert s.witness
    assert any((z^1, s) in table for (arm,_),table in tables.items() if arm == 'variable')
    tests = {mode: reference(s,z,mode) for mode in EXPECTED_MODES}
    shared = tests['shared']
    assert shared['fuel'] == s.fuel+5 and shared['patient'] == 9
    assert shared['actor_receipt'] == 20 and shared['patient_receipt'] == 10
    assert shared['maintenance_holds'] == shared['fuel']
    for mode in EXPECTED_MODES:
        if mode not in ('shared','cheap_gate','free_block'):
            assert shared['fuel'] > tests[mode]['fuel']
    assert tests['cheap_gate']['fuel'] > shared['fuel']
    assert tests['free_block']['fuel'] > shared['fuel']
    assert reference(s,z,'shared','no_private_opportunity')['fuel'] < reference(s,z,'no_build','no_private_opportunity')['fuel']
    nod = reference(s,z,'shared','no_deficit')
    assert nod['patient_action'] == 0 and nod['actor_receipt'] == shared['actor_receipt']
    assert nod['fuel'] == shared['fuel']+3
    for case in ('wrong_transfer','patient_source_outage'):
        value = reference(s,z,'shared',case)
        assert value['patient_action'] == 1 and value['patient_use'] == value['patient_receipt'] == 0
        assert value['fuel'] == shared['fuel'] and value['actor_receipt'] == shared['actor_receipt']
    liquidity_checks = 0
    for fuel in range(31):
        perturbed = replace(s, fuel=fuel)
        for mode in EXPECTED_MODES:
            for case in EXPECTED_CASES:
                assert reference(perturbed,z,mode,case) == producer.suffix(perturbed,z,mode,case)
                liquidity_checks += 1
    assert reference(replace(s,fuel=6),z,'shared')['patient_action'] == 0
    assert reference(replace(s,fuel=7),z,'shared')['patient_use'] == 1
    assert reference(replace(s,fuel=10),z,'shared')['actor_receipt'] == 0
    assert reference(replace(s,fuel=11),z,'shared')['actor_receipt'] == 20

    assert before == source_hashes(), 'Substantive source changed during independent audit'
    return dict(status='pass', source_hashes=before,
                preparation_states=prep_count, preparation_terminals=terminal_count,
                preparation_probability=str(commissioned), prefix_event_states=prefix_checks,
                inherited_state_counts={str(key):len(table) for key,table in tables.items()},
                reachable_suffix_comparisons=suffix_checks, unconditional_rows=len(rows),
                low_fuel_intervention_comparisons=liquidity_checks,
                exact_trace_comparison=True, conventional_distribution_equal=True,
                patient_receipt_never_actor_receipt=True,
                finite_paid_holds_executed=True,
                witness=dict(state=asdict(s), regime=z, unconditional_mass=witness['unconditional_mass'],
                             shared_reserve=shared['fuel'], shared_patient=shared['patient'],
                             cheap_gate_reserve=tests['cheap_gate']['fuel'],
                             free_block_reserve=tests['free_block']['fuel']),
                scope='Independent finite-model check; no empirical or universal-direction claim.')


if __name__ == '__main__':
    result = run()
    (HERE/'independent-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','inherited_state_counts')}))
