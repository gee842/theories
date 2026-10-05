#!/usr/bin/env python3
"""Independent explicit-species audit of paid formation and local selection.

No producer imports. States here include damaged sites and precursor explicitly;
exact event recursions and floating uniformization are reconstructed separately.
"""
from collections import deque
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import ceil, exp
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
# C,D,P,freeA,freeH,residentA,residentH,localF,commonF,incidentE
C, D, P, A, H, RA, RH, L, F, E = range(10)
EVENTS = ('form_a', 'form_h', 'bind_a', 'bind_h', 'repair', 'repair_loss',
          'deadrepair', 'deadrepair_loss', 'capture', 'burncapture',
          'copy_a', 'copy_h', 'bulk_a', 'bulk_h', 'wear_a', 'wear_h',
          'wear_res_a', 'wear_res_h', 'damage', 'leak_common', 'leak_local')
EXTRA = ('copy_a_with_h_present', 'copy_h_with_a_present', 'intact_time', 'occupied_time')
REWARDS = EVENTS + EXTRA
RATES = ('mu', 'bind', 'repair', 'capture', 'copy', 'bulk', 'damage', 'wear', 'leak', 'sigma')


def law_from(record):
    return {k: Q(v) if k in RATES else v for k, v in record.items()}


def expand(s, law):
    a, h, resident, c, local, f, e = s
    ra, rh = int(resident == 1), int(resident == 2)
    return c, 1 - c, law['material'] - a - h - ra - rh, a, h, ra, rh, local, f, e


def totals(s):
    return s[A] + s[RA], s[H] + s[RH]


def rank(s):
    # An independent strict rank; the extra occupancy coordinate also decreases.
    return 4 * s[E] + 2 * (s[L] + s[F]) + s[C] + sum(totals(s)) + s[RA] + s[RH]


def outputs(s):
    a, h = totals(s)
    return {'A': Q(a), 'H': Q(h), 'A_minus_H': Q(a - h), 'population': Q(a + h),
            'A_fraction_empty_half': Q(a, a + h) if a + h else Q(1, 2),
            'intact': Q(s[C]), 'occupied': Q(s[RA] + s[RH]), 'local_fuel': Q(s[L]),
            'both_present': Q(a > 0 and h > 0), 'empty': Q(a + h == 0),
            'common_fuel': Q(s[F]), 'source': Q(s[E])}


def channels(s, law):
    """Mass action and explicit stoichiometry; observation functions unused."""
    mode, rows = law['mode'], []

    def event(name, parameter, reactants, change, scale=Q(1)):
        rate = law[parameter] * scale
        for i in reactants:
            rate *= s[i]
        if rate:
            t = list(s)
            for i, delta in change.items():
                t[i] += delta
            rows.append((name, tuple(t), rate))

    if mode != 'noformation':
        event('form_a', 'mu', (D, P, F), {P: -1, A: 1, F: -1})
        event('form_h', 'mu', (D, P, F), {P: -1, H: 1, F: -1})
    if mode != 'noassociation' and not (s[RA] or s[RH]):
        event('bind_a', 'bind', (A, F), {A: -1, RA: 1, F: -1})
        event('bind_h', 'bind', (H, F), {H: -1, RH: 1, F: -1})
    if mode != 'norepair':
        name = 'deadrepair' if mode == 'deadrepair' else 'repair'
        change = {F: -1} if mode == 'deadrepair' else {C: 1, D: -1, F: -1}
        event(name, 'repair', (RA, D, F), change, 1 - law['sigma'])
        event(name + '_loss', 'repair', (RA, D, F), change | {RA: -1, P: 1}, law['sigma'])
    if not s[L] and mode != 'nocapture':
        target = F if mode == 'shared' else L
        name = 'burncapture' if mode == 'burncapture' else 'capture'
        change = {E: -1} if mode == 'burncapture' else {E: -1, target: 1}
        event(name, 'capture', (C, E), change)
    if mode != 'nocopy':
        if mode != 'shared':
            event('copy_a', 'copy', (RA, P, L), {P: -1, L: -1, A: 1})
            event('copy_h', 'copy', (RH, P, L), {P: -1, L: -1, H: 1})
        for name, free, resident in [('bulk_a', A, RA), ('bulk_h', H, RH)]:
            # Separate free and bound templates, then combine identical channels.
            for template in (free, resident):
                rate = (law['bulk'] + (law['copy'] if mode == 'shared' else 0))
                rate *= s[template] * s[P] * s[F]
                if rate:
                    t = list(s)
                    t[free] += 1
                    t[P] -= 1
                    t[F] -= 1
                    rows.append((name, tuple(t), rate))
    for name, i in [('wear_a', A), ('wear_h', H), ('wear_res_a', RA), ('wear_res_h', RH)]:
        event(name, 'wear', (i,), {i: -1, P: 1})
    event('damage', 'damage', (C,), {C: -1, D: 1})
    event('leak_common', 'leak', (F,), {F: -1})
    event('leak_local', 'leak', (L,), {L: -1})
    return rows


def reward_rows(s, rows):
    rates = {name: Q(0) for name in REWARDS}
    a, h = totals(s)
    for name, _, rate in rows:
        rates[name] += rate
        if name == 'copy_a' and h:
            rates['copy_a_with_h_present'] += rate
        if name == 'copy_h' and a:
            rates['copy_h_with_a_present'] += rate
    rates['intact_time'], rates['occupied_time'] = Q(s[C]), Q(s[RA] + s[RH])
    return rates


def graph(law, initial):
    todo, seen, result = deque([initial]), {initial}, {}
    while todo:
        s = todo.popleft()
        rows = channels(s, law)
        result[s] = rows
        for _, t, _ in rows:
            if t not in seen:
                todo.append(t)
                seen.add(t)
    return result


def audit_states(law, initial):
    m, support, incident = law['material'], initial[L] + initial[F] + initial[E], initial[E]
    states = events = 0
    for c, resident, a, h, local, f, e in product(range(2), range(3), range(m + 1),
                                                 range(m + 1), range(2), range(support + 1),
                                                 range(incident + 1)):
        if a + h + int(resident != 0) > m or local + f + e > support:
            continue
        s = expand((a, h, resident, c, local, f, e), law)
        rows = channels(s, law)
        states += 1
        for name, t, rate in rows:
            assert rate > 0 and min(t) >= 0
            assert t[C] + t[D] == 1 and t[RA] + t[RH] <= 1 and t[L] <= 1
            assert t[P] + sum(totals(t)) == m
            expected_spend = 0 if name in ('capture', 'wear_a', 'wear_h', 'wear_res_a', 'wear_res_h', 'damage') else 1
            assert sum(s[i] - t[i] for i in (L, F, E)) == expected_spend
            assert s[E] - t[E] == int(name in ('capture', 'burncapture'))
            assert rank(t) < rank(s)
            if name in ('copy_a', 'bulk_a'):
                assert totals(s)[0] > 0
            if name in ('copy_h', 'bulk_h'):
                assert totals(s)[1] > 0
            events += 1
        a, h = totals(s)
        delta = a - h
        observed = sum(rate * ((totals(t)[0] - totals(t)[1]) - delta) for _, t, rate in rows)
        copying = Q(0) if law['mode'] == 'nocopy' else law['bulk']
        if law['mode'] == 'shared':
            copying += law['copy']
        expected = (copying * s[P] * s[F] - law['wear']) * delta
        if law['mode'] not in ('shared', 'nocopy'):
            expected += law['copy'] * s[P] * s[L] * (s[RA] - s[RH])
        if law['mode'] != 'norepair':
            expected -= law['sigma'] * law['repair'] * s[RA] * s[D] * s[F]
        assert observed == expected, (s, observed, expected)
    return {'inventory_states': states, 'separate_template_channels': events}


def exact_terminal(law, initial):
    net = graph(law, initial)
    terminal_names = EVENTS + EXTRA[:2]

    @lru_cache(None)
    def solve(s):
        rows = net[s]
        if not rows:
            return dict.fromkeys(terminal_names, Q(0)) | outputs(s)
        rate = sum(q for _, _, q in rows)
        total = dict.fromkeys(terminal_names + tuple(outputs(s)), Q(0))
        a, h = totals(s)
        for event, t, q in rows:
            future = solve(t)
            for key in total:
                immediate = int(key == event)
                immediate += int(key == EXTRA[0] and event == 'copy_a' and h > 0)
                immediate += int(key == EXTRA[1] and event == 'copy_h' and a > 0)
                total[key] += q * (future[key] + immediate) / rate
        return total
    return solve(initial), net


def numeric(law, initial, horizon):
    net = graph(law, initial)
    states = sorted(net)
    indices = {s: i for i, s in enumerate(states)}
    lam = max(1.0, max(float(sum(q for _, _, q in rows)) for rows in net.values()))
    steps = max(1, ceil(lam * float(horizon) / 16))
    dt, theta = float(horizon) / steps, lam * float(horizon) / steps
    current = [float(s == initial) for s in states]
    links, local_rates = [], []
    for s in states:
        rows = net[s]
        probs = [(indices[s], 1 - float(sum(q for _, _, q in rows)) / lam)]
        probs += [(indices[t], float(q) / lam) for _, t, q in rows]
        links.append(probs)
        local_rates.append([(REWARDS.index(k), float(v) / lam)
                            for k, v in reward_rows(s, rows).items() if v])
    cumulative = [0.0] * len(REWARDS)
    tail_sum = 0.0
    for _ in range(steps):
        p, running = current, [0.0] * len(REWARDS)
        end, rewards = [0.0] * len(states), [0.0] * len(REWARDS)
        weight, n = exp(-theta), 0
        while True:
            for i, mass in enumerate(p):
                end[i] += weight * mass
            for k, value in enumerate(running):
                rewards[k] += weight * value
            next_weight = weight * theta / (n + 1)
            tail = next_weight / (1 - theta / (n + 2)) if n + 2 > theta else float('inf')
            if tail < 1e-18:
                break
            following = [0.0] * len(states)
            for i, mass in enumerate(p):
                if not mass:
                    continue
                for j, probability in links[i]:
                    following[j] += mass * probability
                for k, value in local_rates[i]:
                    running[k] += mass * value
            p, weight, n = following, next_weight, n + 1
        current = end
        cumulative = [a + b for a, b in zip(cumulative, rewards)]
        tail_sum += tail
    endpoint = {k: sum(mass * float(outputs(s)[k]) for s, mass in zip(states, current))
                for k in outputs(initial)}
    return dict(zip(REWARDS, cumulative)), endpoint, {
        'chunks': steps, 'omitted_poisson_mass_estimate': tail_sum,
        'float_mass_error': abs(sum(current) - 1),
        'scope': 'Ordinary floating arithmetic, not outward enclosures; tolerance includes arithmetic error.'}


def distance(value, interval):
    return max(float(interval['lower']) - value, value - float(interval['upper']), 0.0)


def run():
    primary_path = HERE / 'results.json'
    inputs = [HERE / 'process.py', HERE / 'check.py', HERE / 'PROTOCOL.md',
              HERE.parent / 'model.py', primary_path]
    hashes = {str(p.relative_to(HERE)) if p.is_relative_to(HERE) else '../model.py':
              sha256(p.read_bytes()).hexdigest() for p in inputs}
    primary = json.loads(primary_path.read_text())
    assert primary['status'] == 'passed'
    assert all(primary['source_hashes'][k] == hashes[k] for k in ('process.py', 'check.py', 'PROTOCOL.md'))
    assert primary['arithmetic_dependency']['sha256'] == hashes['../model.py']
    records, worst = {}, 0.0
    for name, result in primary['cases'].items():
        law = law_from(result['law'])
        if name in ('active', 'noformation', 'noassociation', 'norepair', 'deadrepair',
                    'nocapture', 'burncapture', 'nocopy', 'shared'):
            assert law['mode'] == name and law['material'] == 3 and law['sigma'] == 0
            assert tuple(result['initial']) == (0, 0, 0, 0, 0, 4, 1)
            assert Q(result['horizon']) == 12
            assert all(law[k] == 1 for k in ('mu', 'bind', 'repair', 'capture', 'copy'))
            assert all(law[k] == Q(1, 1000000) for k in ('bulk', 'damage', 'wear', 'leak'))
        initial = expand(result['initial'], law)
        complete = audit_states(law, initial)
        exact, net = exact_terminal(law, initial)
        for key, value in result['terminal_exact'].items():
            assert exact[key] == Q(value), (name, key, exact[key], value)
        assert len(net) == result['certificate']['states']
        if initial[C] == initial[RA] == initial[RH] == initial[A] == initial[H] == initial[L] == 0:
            if initial[F] < 3:
                assert all(s[C] == 0 for s in net)
            if initial[F] < 4 and law['mode'] != 'shared':
                assert all(not (s[C] and totals(s)[1]) for s in net)
            if law['mode'] == 'noformation':
                assert all(sum(totals(s)) == 0 for s in net)
        rewards, endpoint, diagnostics = numeric(law, initial, Q(result['horizon']))
        discrepancies = [distance(rewards[k], v) for k, v in result['events'].items()]
        discrepancies += [distance(endpoint[k], v) for k, v in result['endpoint'].items()]
        worst_case = max(discrepancies)
        assert worst_case < 1e-10, (name, worst_case)
        worst = max(worst, worst_case)
        records[name] = complete | {'reachable_states': len(net), 'terminal_exact_matches': True,
                                   'maximum_interval_distance': worst_case, 'numerics': diagnostics,
                                   'independent_endpoint': endpoint,
                                   'independent_mixed_a_copy': rewards[EXTRA[0]]}
    zero = law_from(primary['cases']['active']['law'])
    zero.update(bulk=Q(0), damage=Q(0), wear=Q(0), leak=Q(0), sigma=Q(0))
    references = {}
    for material, fuel in [(2, 3), (3, 4)]:
        for mode in ('active', 'shared', 'norepair', 'deadrepair'):
            law = zero | {'material': material, 'mode': mode}
            initial = expand((0, 0, 0, 0, 0, fuel, 1), law)
            exact, _ = exact_terminal(law, initial)
            key = f'M{material}_{mode}'
            references[key] = {'A_minus_H': str(exact['A_minus_H']),
                               'copy_a_with_h_present': str(exact[EXTRA[0]])}
    assert references['M2_active'] == {'A_minus_H': '1/18', 'copy_a_with_h_present': '0'}
    assert references['M2_shared']['A_minus_H'] == '1/48'
    assert references['M3_active'] == {'A_minus_H': '17/150', 'copy_a_with_h_present': '7/150'}
    assert references['M3_shared']['A_minus_H'] == '4/147'
    assert all(references[f'M{m}_{mode}']['A_minus_H'] == '0'
               for m in (2, 3) for mode in ('norepair', 'deadrepair'))
    analytical = Q(1, 60) * Q(6, 7)**6 - 2 * 6 * 19 * Q(1, 1000000) * 12
    assert analytical > Q(387, 100000)
    mixed_bound = Q(1, 60) * Q(6, 7)**6 - 19 * Q(1, 1000000) * 12
    assert mixed_bound == Q(187694007, 29412250000) and mixed_bound > Q(638, 100000)
    work_positive = Q(17, 150) * Q(6, 7)**6 - 6 * Q(1, 10000) - 1368 * Q(1, 1000000000)
    work_negative = Q(1, 10000) * Q(17, 150) * Q(6, 7)**4 - 1152 * Q(1, 1000000000)
    assert work_positive > Q(443, 10000) and work_negative > Q(496, 100000000)
    # A paid historical takeover, outside the primary four-common-fuel fixture.
    takeover_law = law_from(primary['cases']['active']['law']) | {'material': 2}
    s = expand((0, 0, 0, 0, 0, 5, 1), takeover_law)
    takeover, probability = [], Q(1)
    for event in ('form_a', 'form_h', 'bind_a', 'repair', 'wear_res_a', 'bind_h', 'capture', 'copy_h'):
        rows = channels(s, takeover_law)
        matches = [(t, q) for name, t, q in rows if name == event]
        assert len(matches) == 1
        t, q = matches[0]
        total = sum(rate for _, _, rate in rows)
        probability *= q / total
        takeover.append({'event': event, 'before_explicit_species': s,
                         'after_explicit_species': t, 'rate': str(q), 'exit_rate': str(total)})
        s = t
    assert totals(s) == (0, 2) and s[F] == s[E] == s[L] == 0
    assert probability > 0
    assert all(sha256(p.read_bytes()).hexdigest() == hashes[
        str(p.relative_to(HERE)) if p.is_relative_to(HERE) else '../model.py'] for p in inputs)
    report = {'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'source_hashes': hashes, 'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Independent explicit-species stoichiometry and signed-abundance generator identity; exact terminal recursion; separate float uniformization. No calibration, novelty, stochastic Lean, or Python refinement claim.',
              'numerical_tolerance': 1e-10, 'maximum_interval_distance': worst,
              'cases': records, 'exact_reference_values': references,
              'analytical_mixed_path_gain_lower': str(analytical),
              'analytical_mixed_copy_lower': str(mixed_bound),
              'analytical_work_source_positive_lower': str(work_positive),
              'analytical_work_no_source_negative_magnitude_lower': str(work_negative),
              'paid_takeover': {'initial_material': 2, 'initial_common_fuel': 5,
                                'eventual_exact_path_probability': str(probability),
                                'events': takeover,
                                'scope': 'Positive-probability path with extra common fuel; no finite-deadline reliability claim.'}}
    (HERE / 'independent-check.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'cases': len(records), 'max_distance': worst,
                      'inventory_states': sum(r['inventory_states'] for r in records.values()),
                      'separate_template_channels': sum(r['separate_template_channels'] for r in records.values())}, indent=2))


if __name__ == '__main__':
    run()
