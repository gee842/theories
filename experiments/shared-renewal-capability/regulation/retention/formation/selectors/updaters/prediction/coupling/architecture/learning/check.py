"""Producer witness and algebraic boundaries; independent audit is separate."""
from dataclasses import asdict, replace
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import model as m


def preparation_word(law):
    architecture = m.architecture
    prediction = architecture.upstream.parent.upstream
    old = prediction.old
    parentlaw = law.architecture_law()
    state = (0, 0, 0, 0, 0, parentlaw.initial_common, parentlaw.initial_source)
    specification = prediction.predecessor(parentlaw.upstream_law())
    probability, rows = Q(1), []
    for event in ('form_a', 'form_h', 'bind_a', 'repair', 'capture'):
        channels = old.channels(specification, state)
        successor, rate = next((s, r) for name, s, r in channels if name == event)
        chance = rate/sum(r for _, _, r in channels)
        probability *= chance
        rows.append(dict(event=event, before=state, after=successor,
                         conditional_probability=str(chance), inert_bank=law.initial_bank))
        state = successor
    return state, probability, rows


def prefix_word(law, prep, target, initial_regime):
    coupling = m.architecture.upstream
    active = [(coupling.State(prep['reserve']), Q(1, 2), coupling.ZERO, [])]
    for index in range(8):
        next_active = []
        regime = initial_regime ^ int(index >= 4)
        for state, probability, marks, trace in active:
            for successor, chance, inc in coupling.advance(law.architecture_law().upstream_law(), state, 'variable', regime):
                next_active.append((successor, probability*chance,
                    tuple(a+b for a, b in zip(marks, inc)), trace+[dict(exposure=index,
                    regime=regime, before=asdict(state), after=asdict(successor),
                    conditional_probability=str(chance),
                    marks={name: str(value) for name, value in zip(coupling.MARKS, inc)})]))
        active = next_active
    return next(item for item in active if item[0] == target)


def full_witness():
    law = m.Law()
    _, rows, _ = m.parent_distribution(law)
    row = next(r for r in rows if r['regime'] == 1 and r['state'].fuel == 11
               and r['state'].graph == (1, 5) and r['state'].raw_w == 1)
    raw, prep_probability, prep_trace = preparation_word(law)
    assert tuple(row['prep']['state']) == raw
    donor, prefix_probability, marks, prefix_trace = prefix_word(law, row['prep'], row['coupling_state'], row['initial_regime'])
    old = next(b for b in m.architecture.suffix(law.architecture_law(), donor, row['regime'], 'live') if b.state == row['state'])
    new = m.suffix(law, old.state, row['regime'], 'indexed')[0]
    assert m.strict_witness(new, old.state)
    assert new.state.parent.fuel == 0 and new.state.parent.patient == 30
    assert new.state.parent.q == 2 and new.state.parent.last == 1
    assert new.state.parent.retained == (True, True)
    full_mass = prep_probability*prefix_probability*old.probability*new.probability
    assert full_mass == Q(1, 1080)
    assert row['probability'] == Q(1, 405)
    mark = dict(zip(m.architecture.upstream.MARKS, marks))
    account = dict(initial=195, preparation=row['prep']['preparation_spent'],
        adapter=law.architecture_law().upstream_law().adapter,
        prefix_spent=int(mark['spent']), prefix_waste=int(mark['waste']),
        architecture_spent=old.state.spent, architecture_recipient_operation=old.state.patient_used,
        architecture_damage=old.state.damage, architecture_waste=old.state.waste,
        learning_spent=new.state.spent, learning_waste=new.state.waste,
        learning_recipient_operation=new.state.patient_used, learning_damage=new.state.damage,
        actor_remaining=new.state.parent.fuel, recipient_remaining=new.state.parent.patient)
    assert sum(v for k, v in account.items() if k != 'initial') == account['initial']
    return dict(law=law.record(), single_complete_word_probability=str(full_mass),
        preparation_word_probability=str(prep_probability),
        commissioned_preparation_family_probability=row['prep']['probability'],
        prefix_word_probability_including_regime_prior=str(prefix_probability),
        assembly_word_probability=str(old.probability),
        same_endpoint_preparation_family_probability=str(row['probability']),
        inherited_prior_motor_revision=donor.witness,
        preparation=prep_trace, adapter_endpoint=row['prep'], prefix=prefix_trace,
        architecture=[dict(event=e, state=asdict(s)) for e, s in old.trace],
        learning_entry=asdict(old.state),
        learning=[dict(event=e, state=asdict(s)) for e, s in new.trace],
        energy_account=account)


def boundaries(entry):
    law, results = m.Law(), []
    for fuel in range(4, 16):
        s = replace(entry, fuel=fuel)
        b = m.suffix(law, s, 1, 'indexed')[0]
        names = {name for name, _ in b.trace}
        first_change = 'R1.write.changed' in names
        witness = m.strict_witness(b, s)
        assert first_change == (fuel >= 6)
        assert witness == (fuel >= 11)
        if witness:
            assert b.state.parent.fuel == fuel-11
        results.append(dict(configured_entry_fuel=fuel, first_paid_candidate_change=first_change,
                            strict_witness=witness, final_fuel=b.state.parent.fuel))
    no_part = replace(entry, fuel=13, raw_w=0)
    no_part_b = m.suffix(law, no_part, 1, 'indexed')[0]
    assert not no_part_b.state.wire and not no_part_b.state.indexed
    assert no_part_b.state.recipient_captures == 0
    return dict(fuel_boundaries=results,
        configured_no_spare_connector=dict(entry=asdict(no_part), final=asdict(no_part_b.state)))


if __name__ == '__main__':
    before = m.source_hashes()
    saved = json.loads((m.HERE/'results.json').read_text())
    assert saved['source_sha256'] == before
    record = full_witness()
    entry = m.architecture.State(**{**record['learning_entry'],
        **{k: tuple(record['learning_entry'][k]) for k in ('r_nodes','d_nodes','graph','retained')}})
    record['configured_boundaries'] = boundaries(entry)
    record['source_sha256'] = before
    record['producer_check_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before == m.source_hashes()
    (m.HERE/'witness.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in ('single_complete_word_probability',
        'same_endpoint_preparation_family_probability','energy_account')}, indent=2))
