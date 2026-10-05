#!/usr/bin/env python3
"""Independent six-species event audit and float uniformization.

This file never imports the producer. Fractions validate complete reaction
ledgers and terminal expectations; floating arithmetic cross-checks the
producer's interval outputs without itself claiming directed enclosures.
"""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import ceil, exp
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
Q = Fraction
EVENTS = ('damage', 'formation', 'repair', 'capture', 'copy', 'wear',
          'leak', 'deadrepair', 'burncapture')
READOUTS = EVENTS + ('intact_time',)
COORDINATES = (0, 3, 4, 5)  # C,G,F,E in the independent C,D,P,G,F,E representation
SPEND = {'formation', 'repair', 'copy', 'leak', 'deadrepair', 'burncapture'}
DROP = {'damage': 1, 'formation': 1, 'repair': 1, 'capture': 2,
        'copy': 1, 'wear': 1, 'leak': 2, 'deadrepair': 2, 'burncapture': 4}
# Species-index reactants are multiplied directly, independent of producer code.
TABLE = {
    'damage':      ((-1, 1, 0, 0, 0, 0), 'alpha',   (0,)),
    'formation':   ((0, 0, -1, 1, -1, 0), 'kappa',  (1, 2, 4)),
    'repair':      ((1, -1, 0, 0, -1, 0), 'rho',    (1, 3, 4)),
    'capture':     ((0, 0, 0, 0, 1, -1), 'capture', (0, 5)),
    'copy':        ((0, 0, -1, 1, -1, 0), 'beta',   (2, 3, 4)),
    'wear':        ((0, 0, 1, -1, 0, 0), 'delta',   (3,)),
    'leak':        ((0, 0, 0, 0, -1, 0), 'leak',    (4,)),
}
RATE_KEYS = ('alpha', 'kappa', 'rho', 'capture', 'beta', 'delta', 'leak')


def decode(record):
    out = dict(record)
    for name in RATE_KEYS:
        out[name] = Q(out[name])
    return out


def expand(state, law):
    c, g, f, e = state
    return c, law['N'] - c, law['M'] - g, g, f, e


def score(state):
    return state[0] + state[3] + 2 * state[4] + 4 * state[5]


def reactions(state, law):
    arm = law['arm']
    result = []
    for original, (change, parameter, reactants) in TABLE.items():
        name, factor = original, Q(1)
        if (original, arm) in {('formation', 'noformation'),
                              ('repair', 'norepair'), ('capture', 'nocapture'),
                              ('copy', 'nocopy')}:
            continue
        if original == 'capture' and state[4] == law['B']:
            continue
        if original == 'formation':
            if arm == 'wrongcue':
                reactants = (0, 2, 4)
            elif arm == 'constitutive':
                reactants, factor = (2, 4), Q(law['N'])
        if original == 'repair' and arm == 'deadrepair':
            name, change = 'deadrepair', (0, 0, 0, 0, -1, 0)
        if original == 'capture' and arm == 'burncapture':
            name, change = 'burncapture', (0, 0, 0, 0, 0, -1)
        hazard = law[parameter] * factor
        for i in reactants:
            hazard *= state[i]
        if hazard:
            successor = tuple(x + dx for x, dx in zip(state, change))
            result.append((name, successor, hazard))
    return result


def lattice_audit(law, initial):
    """Check all admissible inventory states, including unreachable ones."""
    total_support, max_incident = initial[2] + initial[3], initial[3]
    states = events = 0
    for c, g, f, e in product(range(law['N'] + 1), range(law['M'] + 1),
                              range(law['B'] + 1), range(max_incident + 1)):
        if f + e > total_support:
            continue
        s = expand((c, g, f, e), law)
        rows = reactions(s, law)
        states += 1
        for name, t, hazard in rows:
            assert hazard > 0 and all(x >= 0 for x in t)
            assert t[0] + t[1] == law['N']
            assert t[2] + t[3] == law['M']
            assert t[4] <= law['B']
            assert s[4] + s[5] == t[4] + t[5] + int(name in SPEND)
            assert s[5] - t[5] == int(name in ('capture', 'burncapture'))
            assert score(s) - score(t) == DROP[name]
            events += 1
        if law['arm'] == 'active':
            drift = [sum(h * (t[i] - s[i]) for _, t, h in rows) for i in (0, 3, 4)]
            c, d, p, g, f, e = s
            expected = [law['rho'] * g * d * f - law['alpha'] * c,
                        law['kappa'] * d * p * f + law['beta'] * g * p * f - law['delta'] * g,
                        law['capture'] * c * e * int(f < law['B'])
                        - law['kappa'] * d * p * f - law['rho'] * g * d * f
                        - law['beta'] * g * p * f - law['leak'] * f]
            assert drift == expected
    return {'inventory_states': states, 'positive_event_channels': events}


def reachable(law, roots):
    pending, seen, graph = list(roots), set(roots), {}
    while pending:
        s = pending.pop()
        rows = reactions(s, law)
        graph[s] = rows
        for _, t, _ in rows:
            if t not in seen:
                seen.add(t)
                pending.append(t)
    return graph


def terminal(law, initial):
    """Bottom-up dynamic programming, unlike the producer's recursion."""
    graph = reachable(law, [initial])
    answer = {}
    for s in sorted(graph, key=score):
        rows = graph[s]
        rate = sum((h for _, _, h in rows), Q(0))
        if not rows:
            answer[s] = [Q(0)] * len(EVENTS) + [Q(s[i]) for i in COORDINATES]
            if all(law[k] > 0 for k in ('alpha', 'delta', 'leak')):
                assert s[0] == s[3] == s[4] == 0
            continue
        moments = [Q(0)] * (len(EVENTS) + 4)
        for name, t, h in rows:
            values = list(answer[t])
            values[EVENTS.index(name)] += 1
            for i, value in enumerate(values):
                moments[i] += h * value / rate
        answer[s] = moments
    names = EVENTS + ('final_C', 'final_G', 'final_F', 'final_E')
    return dict(zip(names, answer[initial])), len(graph)


def float_evolve(law, distribution, horizon):
    """Independent sparse uniformization with short numerical subintervals.

    Full successor distributions are retained. Poisson omissions are bounded
    separately; ordinary float operations are not an interval certificate.
    """
    graph = reachable(law, distribution)
    states = sorted(graph)
    index = {s: i for i, s in enumerate(states)}
    exits = [sum((h for _, _, h in graph[s]), Q(0)) for s in states]
    lam = float(max(exits, default=Q(0)))
    if not lam:
        rewards = {k: 0.0 for k in READOUTS}
        rewards['intact_time'] = float(horizon) * sum(p * s[0] for s, p in distribution.items())
        return dict(distribution), rewards, {'chunks': 0, 'tail_mass_bound': 0.0,
                                             'float_mass_error': abs(sum(distribution.values()) - 1)}
    count = max(1, ceil(lam * float(horizon) / 16))
    step = float(horizon) / count
    theta = lam * step
    links, local = [], []
    for s, total in zip(states, exits):
        rows = [(index[s], 1.0 - float(total) / lam)]
        rates = [0.0] * len(READOUTS)
        for name, t, h in graph[s]:
            rows.append((index[t], float(h) / lam))
            rates[EVENTS.index(name)] += float(h) / lam
        rates[-1] = s[0] / lam
        links.append(rows)
        local.append(rates)
    current = [distribution.get(s, 0.0) for s in states]
    totals = [0.0] * len(READOUTS)
    max_rank = max(map(score, distribution), default=0)
    tail_sum = reward_tail_sum = 0.0
    for _ in range(count):
        p, cumulative = current, [0.0] * len(READOUTS)
        output, increments = [0.0] * len(states), [0.0] * len(READOUTS)
        weight, n = exp(-theta), 0
        while True:
            for i, mass in enumerate(p):
                output[i] += weight * mass
            for k, amount in enumerate(cumulative):
                increments[k] += weight * amount
            next_weight = weight * theta / (n + 1)
            tail = (next_weight / (1 - theta / (n + 2))) if n + 2 > theta else float('inf')
            if tail < 1e-18:
                break
            following = [0.0] * len(states)
            for i, mass in enumerate(p):
                for j, probability in links[i]:
                    following[j] += mass * probability
                for k, rate in enumerate(local[i]):
                    cumulative[k] += mass * rate
            p, weight, n = following, next_weight, n + 1
        current = output
        totals = [a + b for a, b in zip(totals, increments)]
        tail_sum += tail
        reward_tail_sum += max(max_rank * tail, law['N'] * step * (weight + tail))
    return dict(zip(states, current)), dict(zip(READOUTS, totals)), {
        'chunks': count, 'tail_mass_bound': tail_sum,
        'local_poisson_reward_tail_bound': reward_tail_sum,
        'poisson_reward_bound_including_lost_distribution':
            reward_tail_sum + tail_sum * max(max_rank, law['N'] * float(horizon)),
        'float_mass_error': abs(sum(current) - 1),
    }


def interval_distance(value, bounds):
    lo, hi = float(bounds['lower']), float(bounds['upper'])
    return max(lo - value, value - hi, 0.0)


def compare_numeric(rewards, distribution, record):
    differences = {k: interval_distance(v, record['event_counts'][k])
                   for k, v in rewards.items()}
    for name, i in zip(('C', 'G', 'F', 'E'), COORDINATES):
        value = sum(mass * state[i] for state, mass in distribution.items())
        differences[name] = interval_distance(value, record['endpoint'][name])
    assert max(differences.values()) < 1e-10, differences
    return max(differences.values())


def audit_certificates():
    from math import prod
    bound = Q(2, 5) * prod(1 - Q(1, 7**q) for q in (6, 5))
    bound += Q(4, 15) * prod(1 - Q(1, 7**q) for q in (6, 5, 2, 3, 1, 2))
    assert bound == Q(35259954180435648, 56994475926865715) and bound > Q(3, 5)
    positive = Q(1, 10) - 2 * 4 * 6 * Q(1, 10000) * 12
    adverse = Q(9, 100) - 2 * 2 * 6 * Q(1, 10000) * 12
    assert positive == Q(53, 1250) and adverse == Q(153, 2500)
    assert Q(1, 2) * (1 - Q(1, 7**18)) * (1 - Q(1, 7**12)) > Q(49, 100)
    for a, h in product(range(1, 15), repeat=2):
        n, p = a + h, Q(a, a + h)
        assert p * Q(a + 1, n + 1) + (1 - p) * Q(a, n + 1) == p
        assert p * Q(a - 1, n - 1) + (1 - p) * Q(a, n - 1) == p
    return {'positive_lower': str(positive), 'adverse_lower': str(adverse),
            'path_lower': str(bound), 'neutral_variant_rational_checks': 196}


def main():
    inputs = ('model.py', 'check.py', 'PROTOCOL.md', 'results.json')
    hashes = {name: sha256((HERE / name).read_bytes()).hexdigest() for name in inputs}
    primary = json.loads((HERE / 'results.json').read_text())
    assert primary['status'] == 'passed'
    assert all(primary['source_hashes'][name] == hashes[name] for name in inputs[:3])
    reports, max_distance = {}, 0.0
    for key, record in primary['cases'].items():
        law = decode(record['law'])
        preparation, arm = key.split('__') if '__' in key else ('main', key)
        fixtures = {'main': (0, 0, 2, 2), 'source_absent': (0, 0, 2, 0),
                    'fuel_zero': (0, 0, 0, 2), 'fuel_one': (0, 0, 1, 2),
                    'initially_intact': (1, 0, 2, 2)}
        assert tuple(record['initial']) == fixtures[preparation]
        assert law['arm'] == arm and (law['N'], law['M'], law['B']) == (1, 3, 2)
        assert all(law[k] == Q(1) for k in ('kappa', 'rho', 'capture', 'beta'))
        assert all(law[k] == Q(1, 10000) for k in ('alpha', 'delta', 'leak'))
        assert Q(record['horizon']) == 12
        initial = expand(record['initial'], law)
        audit = lattice_audit(law, record['initial'])
        exact, nstates = terminal(law, initial)
        assert exact == {k: Q(v) for k, v in record['terminal_exact'].items()}, key
        assert nstates == record['graph_audit']['states'], key
        end, rewards, diagnostic = float_evolve(law, {initial: 1.0}, Q(record['horizon']))
        deviation = compare_numeric(rewards, end, record)
        max_distance = max(max_distance, deviation)
        reports[key] = {**audit, 'reachable_states': nstates,
                        'max_interval_distance': deviation, 'numerics': diagnostic,
                        'independent_copy_expectation': rewards['copy'],
                        'terminal_exact_matches': True}
    sequences = {}
    for key, record in primary['successor_interventions'].items():
        expected_stages = {
            'capture_break_restore': [('nocapture', 4), ('active', 8)],
            'capture_broken': [('nocapture', 12)],
            'capture_continuous': [('active', 12)],
            'cue_break_restore': [('wrongcue', 4), ('active', 8)],
            'cue_broken': [('wrongcue', 12)],
        }
        assert [(s['law']['arm'], Q(s['horizon'])) for s in record['stages']] == expected_stages[key]
        assert tuple(record['initial']) == ((1, 1, 0, 2) if key.startswith('capture_') else (0, 0, 2, 2))
        initial = expand(record['initial'], decode(record['stages'][0]['law']))
        distribution, total = {initial: 1.0}, {k: 0.0 for k in READOUTS}
        stages = []
        for stage in record['stages']:
            law = decode(stage['law'])
            distribution, added, diagnostic = float_evolve(law, distribution, Q(stage['horizon']))
            total = {name: total[name] + added[name] for name in total}
            stages.append(diagnostic)
        deviation = compare_numeric(total, distribution, record)
        max_distance = max(max_distance, deviation)
        sequences[key] = {'max_interval_distance': deviation, 'numerics': stages,
                          'independent_copy_expectation': total['copy']}
    zero = decode(primary['cases']['active']['law'])
    zero.update(alpha=Q(0), delta=Q(0), leak=Q(0))
    references = {}
    for arm, expected in primary['zero_loss_reference'].items():
        law = {**zero, 'arm': arm}
        exact, _ = terminal(law, expand((0, 0, 2, 2), law))
        assert exact == {k: Q(v) for k, v in expected.items()}
        references[arm] = str(exact['copy'])
    assert references == {'active': '4/5', 'norepair': '1/2', 'deadrepair': '2/5'}
    assert all(sha256((HERE / name).read_bytes()).hexdigest() == value
               for name, value in hashes.items()), 'Producer changed during independent audit'
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'status': 'passed',
              'producer_hashes': hashes,
              'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Independent six-species stoichiometry, complete-inventory exact audits, exact terminal DAG calculations, separate float uniformization and true-successor composition. Float agreement is not a new outward-rounding certificate or Python/Lean refinement proof.',
              'float_comparison_tolerance': 1e-10,
              'maximum_distance_from_producer_intervals': max_distance,
              'cases': reports, 'successor_interventions': sequences,
              'zero_loss_copy_expectations': references,
              'analytical_certificates': audit_certificates()}
    (HERE / 'independent-check.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'cases': len(reports), 'sequences': len(sequences),
                      'max_interval_distance': max_distance,
                      'inventory_states': sum(r['inventory_states'] for r in reports.values()),
                      'event_channels': sum(r['positive_event_channels'] for r in reports.values())}, indent=2))


if __name__ == '__main__':
    main()
