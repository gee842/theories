#!/usr/bin/env python3
"""Exact finite construction, microstate, projection and censoring checks."""
from datetime import datetime, timezone
from dataclasses import asdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from math import comb
import os
from pathlib import Path

import model


HERE = Path(__file__).resolve().parent


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(item) for item in value]
    return value


def blocked(function, *args):
    try:
        function(*args)
    except AssertionError:
        return True
    raise AssertionError('A forbidden event was permitted')


def main():
    sources = [HERE/'model.py', HERE/'check.py', HERE/'PROTOCOL.md',
               model.FORMATION_SOURCE, model.formation.ARITHMETIC,
               model.TEACHER_SOURCE, model.CERTIFICATE_SOURCE]
    frozen = {str(Path(os.path.relpath(path, HERE))): path.read_bytes() for path in sources}

    primary, primary_setup = model.prepared_recorder(2, 12, 18)
    assert primary.fuel == 5 and primary.source == 16
    assert primary.slots == primary.blank == 2
    assert primary.a_free == primary.h_free == 0
    assert primary_setup['formation_spent'] == 7 and primary_setup['assembly_spent'] == 2
    assert primary_setup['formation_trace'][-1]['state'] == (2, 2, 1, 1, 0, 7, 16)
    words = []
    for word in product((0, 1), repeat=2):
        final, audit, trace = model.run_word(primary, word, setup=primary_setup)
        assert final.records == word and audit.outcomes == audit.writes == 2
        assert final.fuel == 5-2*sum(word)
        assert final.source == 16-2*(2-sum(word))
        assert model.energy(final)+7+2+4 == 30
        words.append(trace)

    full, capacity_audit, _ = model.run_word(primary, (0, 1), setup=primary_setup)
    parent_next, target = model.teacher.prediction_step(model.project_teacher(full), 0)
    assert target == 0 and parent_next.paid == 3
    assert (full.fuel, full.source, full.blank) == (3, 14, 0)
    assert not model.admission_enabled(full) and not model.assembly_enabled(full)
    assert blocked(model.reserve, full, capacity_audit)
    assert blocked(model.assemble, full)

    # Each obstruction has actual preparation, not an injected depleted state.
    no_fuel, no_fuel_setup = model.prepared_recorder(2, 7, 18)
    assert no_fuel.fuel == 0 and no_fuel.blank == 2 and no_fuel.source == 16
    assert not model.admission_enabled(no_fuel)
    no_source, no_source_setup = model.prepared_recorder(2, 12, 2)
    assert no_source.source == 0 and no_source.fuel == 5 and no_source.blank == 2
    assert not model.admission_enabled(no_source)
    loss_only, loss_bit = model.teacher.prediction_step(model.project_teacher(no_source), 1)
    assert loss_bit == 1 and loss_only.source == 0
    # The one realized parent loss branch is not enough to support its full
    # Bernoulli kernel. Our source guard is an intentional restriction.

    tight, tight_setup = model.prepared_recorder(1, 7, 3)
    assert tight.fuel == tight.source == 2
    awaiting, a1 = model.reserve(tight, model.Audit())
    model.check_audit(awaiting, a1, tight_setup, 'full')
    assert awaiting.fuel == 0 and awaiting.escrow == 1
    assert blocked(model.reserve, awaiting, a1)
    assert blocked(model.commit, awaiting, a1)
    latched, a2 = model.observe(awaiting, a1, 1)
    model.check_audit(latched, a2, tight_setup, 'full')
    assert blocked(model.observe, latched, a2, 0)
    assert blocked(model.reserve, latched, a2)
    written, a3 = model.commit(latched, a2)
    model.check_audit(written, a3, tight_setup, 'full')
    assert written.fuel == 0 and written.escrow == 0 and written.records == (1,)
    assert blocked(model.commit, written, a3)

    # Same first two physical outcomes distinguish interior omission from
    # terminal omission. Both omissions still consume their write escrow.
    local_controls = []
    for policy in model.POLICIES:
        endpoint, audit, trace = model.run_word(primary, (0, 1), policy, primary_setup)
        local_controls.append({'policy': policy, **trace})
        if policy == 'full':
            assert endpoint.records == (0, 1) and audit.outcomes == 2
        elif policy == 'drop_zero':
            assert endpoint.records == (1,) and audit.outcomes == 2 and audit.writes == 2
        else:
            assert endpoint.records == () and endpoint.halted
            assert trace['raw_word'] == [0] and audit.writes == 1

    stress_initial, stress_setup = model.prepared_recorder(8, 84, 72)
    assert (stress_initial.fuel, stress_initial.source) == (65, 64)
    assert stress_setup['initial_energy'] == 156
    assert stress_setup['formation_spent']+stress_setup['assembly_spent'] == 27
    arms = [model.stress(policy, stress_initial, stress_setup) for policy in model.POLICIES]
    keyed = {arm['policy']: arm for arm in arms}
    full_risk = Q(1, 4)**8
    drop_risk = sum((Q(comb(32, s))*Q(1, 4)**s*Q(3, 4)**(32-s)
                     for s in range(8, 33)), Q(0))
    assert full_risk == Q(1, 65536)
    assert drop_risk == Q(10469065127243216839, 18446744073709551616)
    for policy in ('full', 'halt_zero'):
        assert keyed[policy]['final_false_certificate_probability'] == full_risk
        assert keyed[policy]['ever_false_certificate_probability'] == full_risk
        assert full_risk <= model.certificate.ALPHA
    assert keyed['drop_zero']['final_false_certificate_probability'] == drop_risk
    assert keyed['drop_zero']['ever_false_certificate_probability'] == drop_risk
    assert drop_risk > model.certificate.ALPHA
    assert keyed['full']['mean_raw_attempts'] == keyed['full']['mean_retained_records'] == 8
    assert keyed['drop_zero']['mean_raw_attempts'] > 8
    assert keyed['halt_zero']['mean_raw_attempts'] < 8

    record = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'source_hashes': {name: sha256(content).hexdigest() for name, content in frozen.items()},
        'arithmetic': 'fractions.Fraction; exact finite dynamic programming',
        'formation_status': 'Named feasible paths checked against the existing event table; '
                            'no unconditional stochastic formation probability is assigned.',
        'primary': {'setup': primary_setup, 'words': words,
                    'capacity_counterexample': {
                        'state': asdict(full), 'audit': asdict(capacity_audit),
                        'old_teacher_next_is_enabled': True,
                        'recorder_reserve_is_enabled': False,
                        'new_assembly_is_enabled': False},
                    'local_controls': local_controls},
        'guard_and_escrow_checks': {
            'no_fuel': {'setup': no_fuel_setup, 'state': asdict(no_fuel)},
            'no_source': {'setup': no_source_setup, 'state': asdict(no_source),
                          'parent_loss_branch_exists': True, 'recorder_admission': False},
            'write_without_remaining_common_fuel': {'setup': tight_setup,
                'states': [asdict(x) for x in (tight, awaiting, latched, written)],
                'audits': [asdict(x) for x in (model.Audit(), a1, a2, a3)]},
            'second_admission_before_commit_blocked': True,
            'observe_before_admission_blocked': blocked(model.observe, tight, model.Audit(), 0),
            'write_before_outcome_blocked': True,
            'repeat_observation_or_write_blocked': True},
        'stress': {'setup': stress_setup, 'horizon': 32, 'beta': Q(1, 4),
                   'alpha': model.certificate.ALPHA, 'arms': arms,
                   'reference_full_and_halt_probability': full_risk,
                   'reference_drop_probability': drop_risk},
        'scope': 'Finite formed record slots and prepaid commitment; exact old paid-teacher '
                 'projection for full-recorder admitted macros; physical accounting includes '
                 'formation, slot assembly, escrow, all attempted outcomes and all write bills. '
                 'No record renewal, infinite retained stream, constructed counter/certificate '
                 'computer, universal decoder impossibility, final action, or derived concern.'}
    assert all(path.read_bytes() == frozen[str(Path(os.path.relpath(path, HERE)))]
               for path in sources)
    (HERE/'results.json').write_text(json.dumps(serial(record), indent=2)+'\n')
    print(json.dumps(serial({'status': 'passed', 'primary_words': len(words),
                            'stress': [{key: arm[key] for key in
                                ('policy', 'final_false_certificate_probability',
                                 'mean_raw_attempts', 'mean_retained_records',
                                 'mean_operation_and_write_bill', 'mean_fuel', 'mean_source')}
                                for arm in arms]}), indent=2))


if __name__ == '__main__':
    main()
