"""Producer-side exact examples; independent_check.py is the separate audit."""
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import model as m


def preparation_word(law):
    parent = m.upstream.parent.upstream
    old = parent.old
    state = (0, 0, 0, 0, 0, law.initial_common, law.initial_source)
    specification = parent.predecessor(law.upstream_law())
    probability, rows = Q(1), []
    for event in ('form_a', 'form_h', 'bind_a', 'repair', 'capture'):
        channels = old.channels(specification, state)
        chosen = [(s, rate) for name, s, rate in channels if name == event]
        assert len(chosen) == 1
        successor, rate = chosen[0]
        probability *= rate/sum(r for _, _, r in channels)
        rows.append({'event': event, 'before': list(state), 'after': list(successor),
                     'conditional_probability': str(rate/sum(r for _, _, r in channels))})
        state = successor
    assert probability == Q(1, 12)
    assert parent.eligible(state, law.upstream_law())
    return state, probability, rows


def witness():
    law = m.Law()
    preps = m.preparation(law)[0]
    prep = next(p for p in preps if p['commissioned'])
    raw, preparation_probability, preparation_rows = preparation_word(law)
    assert tuple(prep['state']) == raw
    s = m.upstream.State(prep['reserve'])
    probability, prefix_marks, prefix_rows = Q(1, 2), m.upstream.ZERO, []
    original = law.upstream_law()
    for exposure in range(8):
        z = int(exposure >= 4)
        events = m.upstream.advance(original, s, 'variable', z)
        choices = [(t, p, inc) for t, p, inc in events
                   if t.coupling == 0 and (exposure != 0 or (t.last == 1 and t.q == 0))]
        assert len(choices) == 1
        t, p, inc = choices[0]
        prefix_rows.append({'exposure': exposure, 'regime': z, 'before': asdict(s),
                            'after': asdict(t), 'conditional_probability': str(p),
                            'marks': {k: str(v) for k, v in zip(m.upstream.MARKS, inc)}})
        s = t
        probability *= p
        prefix_marks = tuple(a+b for a, b in zip(prefix_marks, inc))
    assert s.fuel == 21 and s.q == 4 and probability == Q(1, 8)
    branches = m.suffix(law, s, 1, 'live')
    selected = [b for b in branches if b.state.graph == (m.RP, m.RP)]
    assert len(selected) == 1
    b = selected[0]
    assert b.probability == Q(2, 15)
    assert b.state.fuel == 5 and b.state.patient == 22 and b.state.retained == (True, True)
    assert b.state.guides_e == 3 and b.state.raw_t == 0 and b.state.raw_w == 2
    assert b.state.spent == 36 and b.state.patient_used == 2
    whole_probability = preparation_probability*probability*b.probability
    family_probability = Q(prep['probability'])*probability*b.probability
    assert whole_probability == Q(1, 720) and family_probability == Q(1, 270)
    account = {'initial': law.initial_common+law.initial_source+law.patient_initial,
               'preparation': prep['preparation_spent'], 'adapter': law.upstream_law().adapter,
               'prefix_spent': int(prefix_marks[m.upstream.MARKS.index('spent')]),
               'prefix_lost_source': int(prefix_marks[m.upstream.MARKS.index('waste')]),
               'suffix_spent': b.state.spent, 'recipient_operation': b.state.patient_used,
               'actor_remaining': b.state.fuel, 'recipient_remaining': b.state.patient}
    assert account['initial'] == 155 == sum(v for k, v in account.items() if k != 'initial')
    return {'law': law.record(), 'specified_preparation_word_probability': str(preparation_probability),
            'preparation_word': preparation_rows, 'commissioned_preparation_family_probability': prep['probability'],
            'paid_adapter_endpoint': prep, 'specified_prefix_probability_given_preparation': str(probability),
            'prefix': prefix_rows, 'suffix_probability': str(b.probability),
            'single_complete_word_probability': str(whole_probability),
            'same_endpoint_preparation_family_probability': str(family_probability),
            'suffix': [{'event': event, 'state': asdict(state)} for event, state in b.trace],
            'energy_account': account}


def generator_pair(law, actor):
    result = {}
    for arm in ('live', 'frozen', 'filter_copy'):
        branches = m.suffix(law, actor, 1, arm)
        # The same first construction word RP is chosen before any generator
        # intervention differs. Inspect actual second construction entrances.
        matched = [b for b in branches if b.state.graph[0] == m.RP]
        entry = next(state for event, state in matched[0].trace if event == 'r1.comparator')
        assert all(next(state for event, state in b.trace if event == 'r1.comparator') == entry for b in matched)
        local = m.assemble(law, m.Branch(entry), 1)
        direct = sum(b.probability for b in local if m.topology(b.state.graph[1]) == 'direct')
        result[arm] = {'actual_second_assembly_entrance': asdict(entry),
                       'conditional_direct_probability': str(direct),
                       'local_path_count': len(local)}
    assert result['live']['conditional_direct_probability'] == '2/3'
    assert result['frozen']['conditional_direct_probability'] == '1/2'
    assert result['filter_copy']['conditional_direct_probability'] == '1/3'
    # Exactly equal funds and total template material; only product identity differs.
    states = [r['actual_second_assembly_entrance'] for r in result.values()]
    assert len({s['fuel'] for s in states}) == 1
    assert len({s['spent'] for s in states}) == 1
    assert len({s['raw_t'] for s in states}) == 1
    return result


if __name__ == '__main__':
    before = m.source_hashes()
    old = json.loads((m.HERE/'results.json').read_text())
    assert old['source_sha256'] == before
    record = witness()
    law = m.Law()
    parent_state = m.upstream.State(**record['prefix'][-1]['after'])
    record['matched_generator_interventions'] = generator_pair(law, parent_state)
    record['source_sha256'] = before
    record['producer_check_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before == m.source_hashes()
    (m.HERE/'witness.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'full_word_probability': record['single_complete_word_probability'],
                      'family_probability': record['same_endpoint_preparation_family_probability'],
                      'energy_account': record['energy_account'],
                      'second_assembly_direct': {arm: row['conditional_direct_probability']
                         for arm, row in record['matched_generator_interventions'].items()}}))
