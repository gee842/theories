"""Independent exogenous-draw successor and forward preparation checks."""
from collections import defaultdict
from dataclasses import asdict, replace
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import model as m


def independent_events(law, state, arm, regime):
    """Reimplement the protocol; never call model's command/update/advance."""
    answer = defaultdict(Q)
    for initial_bit, new_switch, packet_present in product((0, 1), repeat=3):
        weight = Q(1, 4)*(law.availability if packet_present else 1-law.availability)
        if not weight:
            continue
        s = asdict(state)
        marks = {name: 0 for name in m.MARKS}

        def pay(amount):
            assert s['fuel'] >= amount
            s['fuel'] -= amount
            marks['spent'] += amount

        if s['gate_life'] == 0 and s['fuel'] >= law.gate_assembly:
            pay(law.gate_assembly)
            s['gate_life'] = law.gate_lifetime
            marks['updater_forms'] += 1
        if s['gate_life'] > 0 and s['life'] == 0 and s['stage'] != 1 and s['fuel'] >= law.base:
            pay(law.base)
            s.update(stage=1, life=0, q=2, last=initial_bit, written=False,
                     coupling=-1, coupling_life=0, failed_q=-1, qualified_q=-1)
            marks['base_forms'] += 1
        if s['gate_life'] > 0 and s['stage'] == 1 and s['fuel'] >= law.retrofit:
            pay(law.retrofit)
            s.update(stage=2, life=law.lifetime, q=2)
            marks['predictor_retrofits'] += 1
        if s['stage'] == 2 and s['life'] > 0 and s['coupling_life'] == 0 and s['fuel'] >= law.coupling_assembly:
            kind = 0 if arm == 'fixed_normal' else 1 if arm == 'fixed_inverted' else new_switch
            changed = s['coupling'] != -1 and s['coupling'] != kind
            evidence = changed and s['written'] and s['q'] != 2 and s['q'] == s['failed_q']
            pay(law.coupling_assembly)
            s.update(coupling=kind, coupling_life=law.coupling_lifetime,
                     qualified_q=s['q'] if evidence else -1, failed_q=-1)
            marks['coupler_forms'] += 1
            marks['coupler_changes'] += int(changed)
        capture = False
        if s['stage'] == 2 and s['life'] > 0:
            if s['fuel'] < law.rent:
                s.update(stage=0, life=0, q=2, last=0, written=False,
                         coupling=-1, coupling_life=0, failed_q=-1, qualified_q=-1)
            else:
                pay(law.rent)
                marks['rents'] += 1
                if s['gate_life'] > 0 and s['coupling_life'] > 0 and s['fuel'] >= law.trial:
                    old_q, old_written = s['q'], s['written']
                    threshold = 0 if old_q < 2 else 1 if old_q > 2 else s['last']
                    action = threshold if s['coupling'] == 0 else 1-threshold
                    capture = bool(packet_present and action == regime)
                    forecast = old_q if action == 1 else 4-old_q
                    pay(law.trial)
                    if capture:
                        s['fuel'] += law.packet
                        pay(law.renewal+law.gate_renewal)
                        s['life'], s['gate_life'] = law.lifetime, law.gate_lifetime
                    else:
                        s['life'] -= 1
                        s['gate_life'] -= 1
                    renew = capture or (arm == 'outcome_blind' and s['fuel'] >= law.coupling_renewal)
                    if renew:
                        pay(law.coupling_renewal)
                        s['coupling_life'] = law.coupling_lifetime
                    else:
                        s['coupling_life'] -= 1
                    paid_write = s['fuel'] >= law.write
                    label = action if capture else 1-action
                    if paid_write:
                        pay(law.write)
                        s['q'], s['written'] = 4*label, True
                    if capture and s['qualified_q'] == old_q and old_q in (0, 4):
                        s['witness'] = True
                    if s['q'] != old_q:
                        s['failed_q'] = s['qualified_q'] = -1
                    if not capture and old_written and old_q in (0, 4) and paid_write and s['q'] == old_q:
                        s['failed_q'] = old_q
                    s['last'] = action
                    marks.update(trials=1, captures=int(capture), writes=int(paid_write),
                                 unpaid_writes=int(not paid_write), decoder_errors=int(label != regime),
                                 acquired_uses=int(old_written and old_q != 2),
                                 normal_trials=int(s['coupling'] == 0), inverted_trials=int(s['coupling'] == 1),
                                 coupler_renewals=int(renew), brier16=(forecast-4*int(capture))**2)
        marks['waste'] = 0 if capture else law.packet
        assert state.fuel+law.packet == s['fuel']+marks['spent']+marks['waste']
        key = (m.State(**s), tuple(Q(marks[k]) for k in m.MARKS))
        answer[key] += weight
    assert sum(answer.values()) == 1
    return dict(answer)


def aggregate(events):
    result = defaultdict(Q)
    for s, probability, marks in events:
        result[s, marks] += probability
    return dict(result)


def independent_preparation(law):
    """The reference's seven positive-rate old reactions, directly enumerated."""
    start = (0, 0, 0, 0, 0, law.initial_common, law.initial_source)
    pending, terminal, visited = {start: Q(1)}, defaultdict(Q), set()

    def rank(s):
        return 4*s[6]+2*(s[4]+s[5])+s[3]+s[0]+s[1]+int(s[2] != 0)

    while pending:
        s = max(pending, key=rank)
        mass = pending.pop(s)
        visited.add(s)
        a, h, resident, intact, local, fuel, source = s
        free_parts = 2-a-h-int(resident != 0)
        channels = []

        def append(rate, **change):
            if rate <= 0:
                return
            values = dict(zip(('a', 'h', 'resident', 'intact', 'local', 'fuel', 'source'), s))
            values.update(change)
            t = tuple(values.values())
            assert rank(t) < rank(s)
            channels.append((Q(rate), t))

        append((1-intact)*free_parts*fuel, a=a+1, fuel=fuel-1)
        append((1-intact)*free_parts*fuel, h=h+1, fuel=fuel-1)
        if resident == 0:
            append(a*fuel, a=a-1, resident=1, fuel=fuel-1)
            append(h*fuel, h=h-1, resident=2, fuel=fuel-1)
        if resident == 1 and not intact:
            append(fuel, intact=1, fuel=fuel-1)
        if intact and not local:
            append(source, source=source-1, local=1)
        if resident in (1, 2):
            append(free_parts*local, local=0, **({'a': a+1} if resident == 1 else {'h': h+1}))
        if not channels:
            terminal[s] += mass
        else:
            total = sum(rate for rate, _ in channels)
            for rate, t in channels:
                pending[t] = pending.get(t, Q(0))+mass*rate/total
    assert sum(terminal.values()) == 1
    originals, count = m.prepare(law)
    assert {tuple(row['state']): Q(row['probability']) for row in originals} == dict(terminal)
    assert count == len(visited)
    for row in originals:
        s = row['state']
        assert row['remaining_energy'] == s[4]+s[5]+s[6]
        assert row['preparation_spent']+row['remaining_energy'] == law.initial_common+law.initial_source
        expected = (s[0]+int(s[2] == 1) == 1 and s[1]+int(s[2] == 2) == 1
                    and s[3] == s[4] == 1 and s[5] >= law.adapter)
        assert expected == row['commissioned']
        if expected:
            assert row['reserve'] == s[5]-law.adapter+s[4]
            assert row['packets']*law.packet+row['remainder'] == s[6]
    return len(visited), len(terminal)


def deterministic_witness():
    law = m.Law()
    preparation = next(p for p in m.prepare(law)[0] if p['commissioned'])
    s = m.State(preparation['reserve'])
    states, marks, probability = [s], m.ZERO, Q(preparation['probability'])*Q(1, 2)
    for index in range(3):
        options = m.advance(law, s, 'variable', 1)
        selected = [(t, p, inc) for t, p, inc in options
                    if t.coupling == (1 if index < 2 else 0) and t.q == 4
                    and t.last == (0 if index < 2 else 1)]
        assert len(selected) == 1
        s, chance, inc = selected[0]
        probability *= chance
        marks = tuple(a+b for a, b in zip(marks, inc))
        states.append(s)
    assert s.witness and s.fuel == 8 and probability == Q(1, 72)
    assert states[1].written and states[1].q == states[2].q == states[3].q == 4
    assert m.command('variable', 4, states[2].last, 0) != m.command('variable', 4, states[2].last, 1)
    spent, lost = marks[m.MARKS.index('spent')], marks[m.MARKS.index('waste')]
    assert spent == 28 and lost == 20
    remaining_packets = preparation['packets']-3
    assert (preparation['preparation_spent']+law.adapter+spent+lost+s.fuel
            +remaining_packets*law.packet+preparation['remainder']) == law.initial_common+law.initial_source
    # Immediately before fresh updater/coupler formation: 2+1+1+3 = 7.
    ready = states[2]
    thresholds = {}
    for fuel in (6, 7):
        branch = m.advance(law, replace(ready, fuel=fuel), 'variable', 1)
        capture = sum(p for _, p, inc in branch if inc[m.MARKS.index('captures')])
        assert capture == (Q(0) if fuel == 6 else Q(1, 2))
        thresholds[str(fuel)] = str(capture)
    return {'unconditional_prefix_probability': str(probability),
            'preparation': preparation, 'states': [asdict(s) for s in states],
            'marks': dict(zip(m.MARKS, map(str, marks))), 'remaining_packets': remaining_packets,
            'initial_energy': law.initial_common+law.initial_source,
            'next_opportunity_liquidity': thresholds}


def recovery_formula(law, fuel, trials, circuit_life, updater_life, obsolete_life):
    """Stable, noiseless confident record; no whole-circuit replacement counts."""
    count = 0
    while True:
        failed = obsolete_life+count*law.coupling_lifetime
        updater_forms = 0 if failed < updater_life else 1+(failed-updater_life)//law.gate_lifetime
        cost = failed*(law.rent+law.trial+law.write)+(count+1)*law.coupling_assembly
        cost += updater_forms*law.gate_assembly+law.rent+law.trial
        if failed >= circuit_life or failed+1 > trials or cost > fuel:
            return Q(1)-Q(1, 2)**count
        count += 1


def recovery_check():
    law = m.Law(reversals=(), availability=Q(1))
    checked = 0
    # Primary unit write price prevents an omitted unaffordable write funding
    # a later paid assembly. Arbitrary write-price extensions need rechecking.
    for fuel, trials, life, gate, obsolete in product(range(41), range(1, 9), (2, 4, 6), (1, 2), (1, 2)):
        frontier = {m.State(fuel, gate_life=gate, stage=2, life=life, q=4,
                            last=0, written=True, coupling=1, coupling_life=obsolete): Q(1)}
        success = Q(0)
        for _ in range(trials):
            nxt = defaultdict(Q)
            for state, mass in frontier.items():
                if state.life == 0 or state.stage != 2:
                    continue
                for new, p, marks in m.advance(law, state, 'variable', 1):
                    if marks[m.MARKS.index('captures')]:
                        success += mass*p
                    elif new.life > 0 and new.stage == 2:
                        nxt[new] += mass*p
            frontier = dict(nxt)
        predicted = recovery_formula(law, fuel, trials, life, gate, obsolete)
        assert success == predicted, (fuel, trials, life, gate, obsolete, success, predicted)
        checked += 1
    return checked


if __name__ == '__main__':
    before = m.source_hashes()
    results = json.loads((m.HERE/'results.json').read_text())
    assert results['source_sha256'] == before
    checked, transition_branches = set(), 0

    def verify(law, state, arm, regime, events):
        global transition_branches
        key = law, state, arm, regime
        if key in checked:
            return
        reference = independent_events(law, state, arm, regime)
        assert aggregate(events) == reference, key
        checked.add(key)
        transition_branches += len(reference)

    preparation_counts = {}
    for name, law in m.cases().items():
        preparation_counts[name] = independent_preparation(law)
        assert json.loads(json.dumps(m.compare(law, verify))) == results['cases'][name]
    witness = deterministic_witness()
    recovery_cases = recovery_check()
    assert before == m.source_hashes(), 'Sources changed while checking; rerun.'
    record = {'source_sha256': before,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'case_arm_count': len(m.cases())*len(m.ARMS),
              'independent_marked_kernels': len(checked), 'marked_branches': transition_branches,
              'independent_preparations': preparation_counts,
              'recovery_configurations': recovery_cases, 'witness': witness,
              'scope': 'Independent protocol successor and predecessor enumeration; same forward summation driver, not empirical validation or a Lean certificate.'}
    (m.HERE/'verification.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in ('case_arm_count', 'independent_marked_kernels', 'marked_branches', 'recovery_configurations')}))
