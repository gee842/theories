#!/usr/bin/env python3
"""Independent exact paid-prefix enumeration and certificate inversion audit.

No producer module is imported. Every acquired outcome word is enumerated,
including its stopped physical leaf; the producer instead uses a count-state
dynamic program and weighted-subset pruning. Binomial tails below are generated
by integer polynomial multiplication, not the producer's binomial-sum formula.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ALPHA = Q(1, 10)
CASES = (
    ('funded_half', 16, 33, Q(1, 2)),
    ('stopped_no_action_reserve', 16, 16, Q(1, 2)),
    ('stopped_with_action_reserve', 16, 17, Q(1, 2)),
    ('funded_threshold_boundary', 16, 33, Q(1, 4)),
    ('scarce_raw_count_bias', 16, 3, Q(1, 8)),
)


@lru_cache(None)
def polynomial_probabilities(n, q):
    a, d = q.numerator, q.denominator
    coefficients = [1]
    for _ in range(n):
        extended = [0]*(len(coefficients)+1)
        for k, coefficient in enumerate(coefficients):
            extended[k] += (d-a)*coefficient
            extended[k+1] += a*coefficient
        coefficients = extended
    assert sum(coefficients) == d**n
    return tuple(Q(c, d**n) for c in coefficients)


@lru_cache(None)
def lower_row(n, alpha=ALPHA):
    """Invert count cutoffs for candidate nulls, then assemble lower bounds."""
    if not n:
        return (Q(0),)
    d = 1
    while 2*d <= n:
        d *= 2
    bounds = [Q(0)]*(n+1)
    allowance = alpha/(n*(n+1))
    for numerator in range(d+1):
        q = Q(numerator, d)
        probabilities = polynomial_probabilities(n, q)
        tails = [Q(0)]*(n+1)
        running = Q(0)
        for s in range(n, -1, -1):
            running += probabilities[s]
            tails[s] = running
        cutoff = next((s for s in range(n+1) if tails[s] <= allowance), n+1)
        for s in range(cutoff, n+1):
            bounds[s] = max(bounds[s], q)
    assert all(bounds[s] <= bounds[s+1] for s in range(n))
    return tuple(bounds)


def enumerate_case(name, horizon, initial_fuel, beta):
    a, d = beta.numerator, beta.denominator
    denominator = d**horizon
    weight_denominator = 4**horizon
    endpoints = defaultdict(lambda: {'mass': 0, 'weight': 0, 'ewma_passes': 0})
    edges = set()
    ever_false_mass = 0
    leaves = 0

    def visit(n, s, fuel, source, ewma_numerator, probability_numerator, ever_false):
        nonlocal ever_false_mass, leaves
        assert fuel == initial_fuel-2*s
        assert source == 2*horizon-2*(n-s)
        assert fuel+source+2*n == initial_fuel+2*horizon
        assert min(fuel, source) >= 0
        if n == horizon or fuel < 2:
            leaves += 1
            mass = probability_numerator*d**(horizon-n)
            row = endpoints[n, s, fuel, source]
            row['mass'] += mass
            row['weight'] += mass*ewma_numerator*4**(horizon-n)
            row['ewma_passes'] += mass*int(4*ewma_numerator > 4**n)
            ever_false_mass += mass*ever_false
            return
        for bit, factor in ((0, d-a), (1, a)):
            if not factor:
                continue
            successor = (n+1, s+bit, fuel-2*bit, source-2*(1-bit))
            assert successor[2]+successor[3]+2 == fuel+source
            edges.add(((n, s, fuel, source), bit, successor))
            violation = lower_row(n+1)[s+bit] > beta
            visit(*successor, 3*ewma_numerator+bit*4**n,
                  probability_numerator*factor, ever_false or violation)

    visit(0, 0, initial_fuel, 2*horizon, 0, 1, False)
    assert sum(row['mass'] for row in endpoints.values()) == denominator
    policies = {policy: {'strict_preference': Q(0), 'protect': Q(0),
                         'unfunded_preference': Q(0)}
                for policy in ('ewma', 'count', 'certificate')}
    mean_ewma = mean_count = mean_lower = Q(0)
    completed = affordable = paid_mean = final_false = Q(0)
    rows = []
    for (n, s, fuel, source), data in sorted(endpoints.items()):
        mass = Q(data['mass'], denominator)
        empirical = Q(s, n) if n else Q(0)
        lower = lower_row(n)[s]
        ewma_passes = Q(data['ewma_passes'], data['mass'])
        can_pay = fuel >= 1
        scores = {'ewma': ewma_passes, 'count': Q(int(4*s > n)),
                  'certificate': Q(int(lower > Q(1, 4)))}
        for policy, fraction in scores.items():
            policies[policy]['strict_preference'] += mass*fraction
            policies[policy]['protect'] += mass*fraction*can_pay
            policies[policy]['unfunded_preference'] += mass*fraction*(not can_pay)
            for passed in (False, True):
                bill = int(passed and can_pay)
                after = fuel-bill
                harm = 4*(1-bill)
                assert after >= 0
                assert after+source+2*n+bill == initial_fuel+2*horizon
                assert (harm == 0) == bool(bill)
        mean_ewma += Q(data['weight'], denominator*weight_denominator)
        mean_count += mass*empirical
        mean_lower += mass*lower
        completed += mass*(n == horizon)
        affordable += mass*can_pay
        paid_mean += mass*n
        final_false += mass*(lower > beta)
        rows.append({'paid': n, 'losses': s, 'fuel': fuel, 'source': source,
                     'probability': mass, 'count': empirical, 'lower': lower,
                     'ewma_strict_fraction': ewma_passes, 'action_affordable': can_pay})
    for data in policies.values():
        data['expected_terminal_recipient_outcome'] = 4*(1-data['protect'])
        data['expected_terminal_bill'] = data['protect']
        data['action_when_true_score_not_strict'] = data['protect'] if beta <= Q(1, 4) else Q(0)
    assert Q(ever_false_mass, denominator) <= ALPHA
    return {'name': name, 'horizon': horizon, 'initial_fuel': initial_fuel,
            'initial_source': 2*horizon, 'beta': beta, 'alpha': ALPHA,
            'counter_bits_each': horizon.bit_length(),
            'mean_paid_observations': paid_mean,
            'all_opportunities_paid_probability': completed,
            'terminal_action_affordable_probability': affordable,
            'mean_ewma': mean_ewma, 'mean_count': mean_count, 'mean_lower': mean_lower,
            'ever_false_lower_certificate_probability': Q(ever_false_mass, denominator),
            'terminal_false_lower_certificate_probability': final_false,
            'policies': policies, 'reachable_endpoints': len(endpoints),
            'checked_acquired_edges': len(edges), 'endpoints': rows,
            'independently_enumerated_paid_words': leaves}


def coverage_audit():
    checks = []
    for streams in (1, 3):
        for n in range(1, 21):
            row = lower_row(n, ALPHA/streams)
            allowance = ALPHA/(streams*n*(n+1))
            assert all(row[s] <= row[s+1] for s in range(n))
            for numerator in range(17):
                p = Q(numerator, 16)
                mass = sum((prob for s, prob in enumerate(polynomial_probabilities(n, p))
                            if row[s] > p), Q(0))
                assert mass <= allowance
                checks.append({'streams': streams, 'n': n, 'true_parameter': p,
                               'violation_probability': mass, 'allowance': allowance})
    return checks


def independent_path(outcomes, fuel, horizon):
    initial_fuel = fuel
    source, losses, numerator = 2*horizon, 0, 0
    states = [{'paid': 0, 'losses': 0, 'fuel': fuel, 'source': source,
               'ewma': Q(0), 'lower': Q(0)}]
    for n, bit in enumerate(outcomes, 1):
        assert fuel >= 2
        fuel -= 2*bit
        source -= 2*(1-bit)
        losses += bit
        numerator = 3*numerator+bit*4**(n-1)
        assert fuel+source+2*n == initial_fuel+2*horizon
        states.append({'paid': n, 'losses': losses, 'fuel': fuel, 'source': source,
                       'ewma': Q(numerator, 4**n), 'lower': lower_row(n)[losses]})
    return states


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(item) for item in value]
    return value


def run():
    names = ('model.py', 'check.py', 'PROTOCOL.md', 'README.md', 'results.json',
             '../model.py', 'independent_check.py')
    hashes = {name: sha256((HERE/name).read_bytes()).hexdigest() for name in names}
    saved = json.loads((HERE/'results.json').read_text())
    assert saved['status'] == 'passed'
    assert saved['source_hashes'] == {name: hashes[name]
                                     for name in ('model.py', 'check.py', 'PROTOCOL.md', '../model.py')}
    cases = {args[0]: enumerate_case(*args) for args in CASES}
    # The producing record's exact case schema is checked below; extra
    # independent enumeration counts are intentionally outside that schema.
    saved_cases = saved['cases']
    if isinstance(saved_cases, list):
        saved_cases = {case['name']: case for case in saved_cases}
    for name, case in cases.items():
        comparison = {key: value for key, value in case.items()
                      if key != 'independently_enumerated_paid_words'}
        assert serial(comparison) == saved_cases[name], name
    sparse = cases['scarce_raw_count_bias']
    assert sparse['policies']['count']['protect'] == Q(169, 512)
    assert sparse['policies']['ewma']['protect'] == 0
    assert sparse['policies']['certificate']['protect'] == 0
    stopped = cases['stopped_no_action_reserve']
    reserved = cases['stopped_with_action_reserve']
    for key in ('mean_paid_observations', 'all_opportunities_paid_probability',
                'mean_ewma', 'mean_count', 'mean_lower',
                'ever_false_lower_certificate_probability'):
        assert stopped[key] == reserved[key]
    for policy in ('ewma', 'count', 'certificate'):
        assert stopped['policies'][policy]['strict_preference'] == reserved['policies'][policy]['strict_preference']
        assert stopped['policies'][policy]['protect'] <= reserved['policies'][policy]['protect']
    coverage = coverage_audit()
    path = independent_path([1]*16+[0]*5, 43, 21)
    assert path[-1]['ewma'] <= Q(243, 1024) < Q(1, 4)
    assert path[-1]['lower'] > Q(1, 4)
    assert path[-1]['fuel'] >= 1
    assert path[-1]['losses'] == 16 and path[-1]['paid'] == 21
    assert serial(path) == saved['negative_witnesses']['paid_sixteen_ones_then_five_zeros']
    assert path[-1]['fuel'] == 11 and path[-1]['source'] == 32
    assert path[-1]['lower'] == Q(5, 16)
    # One admissible finite certificate remains possible in the boundary world.
    all_one = independent_path([1]*16, 33, 16)
    assert all_one[-1]['lower'] > Q(1, 4)
    assert Q(1, 4)**16 > 0
    assert all_one[-1]['lower'] == Q(9, 16)
    assert str(all_one[-1]['lower']) == saved['negative_witnesses']['all_one_lower_certificate']
    for name, old in hashes.items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == old, name
    report = {'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'source_hashes': hashes, 'unchanged_inputs': True,
              'scope': 'Exact finite paid-word, terminal-action and discrete certificate checks; no empirical calibration, infinite-support or shared-routing-origin claim.',
              'cases': cases, 'coverage_checks': coverage,
              'coverage_case_count': len(coverage),
              'negative_path': path,
              'boundary_all_one_certificate_probability': Q(1, 4)**16,
              'total_paid_words': sum(case['independently_enumerated_paid_words'] for case in cases.values())}
    (HERE/'independent-check.json').write_text(json.dumps(serial(report), indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'cases': len(cases),
                      'coverage_cases': len(coverage), 'paid_words': report['total_paid_words']}, indent=2))


if __name__ == '__main__':
    run()
