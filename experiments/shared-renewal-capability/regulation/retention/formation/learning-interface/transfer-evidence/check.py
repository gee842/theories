#!/usr/bin/env python3
"""Run the prespecified exact comparisons and preserve their source hashes."""
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import comb
from pathlib import Path

import model


ROOT = Path(__file__).resolve().parent


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(item) for item in value]
    return value


def main():
    sources = [ROOT/'model.py', ROOT/'check.py', ROOT/'PROTOCOL.md', model.PARENT_MODEL]
    frozen = {str(p.relative_to(ROOT) if p.parent == ROOT else Path('../model.py')):
              p.read_bytes() for p in sources}
    cases = [model.analyze_case(*args) for args in model.CASES]
    keyed = {case['name']: case for case in cases}
    funded = keyed['funded_half']
    assert funded['all_opportunities_paid_probability'] == 1
    assert funded['terminal_action_affordable_probability'] == 1
    assert funded['mean_ewma'] == Q(1, 2)*(1-Q(3, 4)**16)
    assert funded['mean_count'] == Q(1, 2)
    even, odd = (keyed['stopped_no_action_reserve'], keyed['stopped_with_action_reserve'])
    assert even['mean_paid_observations'] == odd['mean_paid_observations']
    for policy in ('ewma', 'count', 'certificate'):
        assert even['policies'][policy]['strict_preference'] == odd['policies'][policy]['strict_preference']
    assert odd['policies']['certificate']['protect'] > even['policies']['certificate']['protect']
    scarce = keyed['scarce_raw_count_bias']
    assert scarce['policies']['count']['protect'] == 1-Q(7, 8)**3
    assert scarce['policies']['ewma']['protect'] == 0
    assert scarce['policies']['certificate']['protect'] == 0
    boundary = keyed['funded_threshold_boundary']
    assert 0 < boundary['policies']['certificate']['protect'] <= model.ALPHA
    assert boundary['policies']['certificate']['protect'] == boundary['terminal_false_lower_certificate_probability']

    # Small full-word check validates the order-sensitive combinatorial count;
    # primary cases use count/state DP and exact subset bounds instead.
    word_checks = 0
    for n in range(9):
        counts = [0]*(n+1)
        for word in product((0, 1), repeat=n):
            weight = Q(0)
            for outcome in word:
                weight = Q(3, 4)*weight+Q(1, 4)*outcome
            counts[sum(word)] += weight > model.THRESHOLD
        for s, expected in enumerate(counts):
            assert model.ewma_above_word_count(n, s) == expected
            word_checks += 1

    fixed_sample_checks = 0
    previous_grid = {Q(0)}
    for n in range(1, 17):
        current_grid = set(model.grid(n))
        assert previous_grid <= current_grid
        previous_grid = current_grid
        assert all(model.lower_certificate(n, s) <= model.lower_certificate(n, s+1)
                   for s in range(n))
        for p in (Q(0), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            risk = sum((Q(comb(n, s))*p**s*(1-p)**(n-s)
                        for s in range(n+1) if model.lower_certificate(n, s) > p), Q(0))
            assert risk <= model.ALPHA/(n*(n+1))
            fixed_sample_checks += 1

    path = model.actual_path([1]*16+[0]*5, 43, 21)
    assert path[16]['lower'] > model.THRESHOLD
    assert path[-1]['lower'] > model.THRESHOLD
    assert path[-1]['ewma'] <= Q(3, 4)**5 == Q(243, 1024) < model.THRESHOLD
    assert path[-1]['fuel'] >= model.ACTION_BILL
    endpoint = model.Record(path[-1]['paid'], path[-1]['losses'],
                            path[-1]['fuel'], path[-1]['source'])
    after, harm, spent = model.terminal_step(endpoint, True)
    assert spent == 1 and harm == 0
    assert after.fuel+after.source+2*endpoint.paid+spent == 43+42
    all_one_probability_at_boundary = Q(1, 4)**16
    assert all_one_probability_at_boundary > 0
    assert model.lower_certificate(16, 16) > Q(1, 4)

    record = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'source_hashes': {name: hashlib.sha256(content).hexdigest()
                          for name, content in frozen.items()},
        'arithmetic': 'fractions.Fraction; exact finite probabilities',
        'supplied_decision_interface': {'g': 1, 'z': 1, 'b': 0, 'H': 4, 'a': 1,
                                        'strict_threshold': model.THRESHOLD,
                                        'terminal_returns': 0},
        'supplied_memory_interface': {
            'update_bill': 2, 'operation_component': 1, 'write_computation_component': 1,
            'counter_capacity': '0..T per counter, ceil(log2(T+1)) bits each',
            'additional_apparatus': 'Confidence-budget/routing records and a finite certificate '
                                    'table are supplied; memory construction and maintenance '
                                    'are not derived by the common finite-horizon price.'},
        'cases': cases,
        'additional_checks': {'small_full_word_count_checks': word_checks,
                              'fixed_sample_coverage_checks': fixed_sample_checks},
        'negative_witnesses': {
            'paid_sixteen_ones_then_five_zeros': path,
            'five_zero_uniform_ewma_upper_bound': Q(243, 1024),
            'history_probability_under_stationary_half': Q(1, 2)**21,
            'after_drift_current_beta': Q(0),
            'drift_note': 'The same later zero outcomes can follow a switch to beta=0; '
                          'the retained positive certificate is then stale, outside stationary coverage.',
            'certificate_terminal_action_after_path': {'fuel': after.fuel, 'source': after.source,
                                                        'recipient_outcome': harm, 'bill': spent},
            'all_one_probability_under_boundary_beta': all_one_probability_at_boundary,
            'all_one_lower_certificate': model.lower_certificate(16, 16)},
        'scope': 'A finite, supplied counter/certificate circuit on the existing paid teacher '
                 'histories, and a separate affordable next action with supplied g=z=1 and routing. '
                 'Stationary model-score calibration, not phenomenal valence, derived correspondence, '
                 'memory construction, a harmful-action certificate, infinite funded execution, '
                 'or durable concern. Independent review is recorded separately.'}
    assert all(p.read_bytes() == frozen[str(p.relative_to(ROOT) if p.parent == ROOT
                                           else Path('../model.py'))] for p in sources)
    (ROOT/'results.json').write_text(json.dumps(serial(record), indent=2)+'\n')
    print(json.dumps(serial({'status': 'passed', 'cases': [
        {k: case[k] for k in ('name', 'mean_ewma', 'mean_count', 'mean_lower', 'policies')}
        for case in cases], 'negative_endpoint': path[-1]}), indent=2))


if __name__ == '__main__':
    main()
