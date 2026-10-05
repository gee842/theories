#!/usr/bin/env python3
"""Run prespecified comparisons and preserve exact/enclosed results."""
from dataclasses import replace
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction as Q
from hashlib import sha256
from math import prod
from pathlib import Path
import json

from model import (Law, ARMS, EVENTS, I, ONE, graph, rank, finite, exact_terminal,
                   succession, endpoint_means, evolve)

HERE = Path(__file__).resolve().parent


def audit_graph(law, initial):
    net = graph(law, [initial])
    events = 0
    for s, rows in net.items():
        c, g, f, e = s
        for event, t, rate in rows:
            cc, gg, ff, ee = t
            paid = event in ('formation', 'repair', 'copy', 'deadrepair', 'leak')
            burned = event == 'burncapture'
            assert ff+ee+int(paid)+int(burned) == f+e
            assert ee == e-int(event in ('capture', 'burncapture'))
            assert gg-g == int(event in ('formation', 'copy'))-int(event == 'wear')
            assert cc-c == int(event == 'repair')-int(event == 'damage')
            assert rank(t) < rank(s)
            events += 1
    if initial[0] == initial[1] == 0 and initial[2] < 2 and law.arm != 'wrongcue':
        # Constitutionally supplied formation changes no site or fuel debit.
        assert all(s[0] == 0 and s[1]+s[2] <= 1 for s in net)
    return {'states': len(net), 'event_channels': events, 'initial_rank': rank(initial)}


def lower(case, name):
    return Decimal(case['event_counts'][name]['lower'])


def upper(case, name):
    return Decimal(case['event_counts'][name]['upper'])


def run():
    base = Law()
    zero = replace(base, alpha=Q(0), delta=Q(0), leak=Q(0))
    x0 = (0, 0, 2, 2)
    initial_hashes = {name: sha256((HERE/name).read_bytes()).hexdigest()
                      for name in ('model.py', 'check.py', 'PROTOCOL.md')}
    cases = {}
    for arm in ARMS:
        print('Checking primary arm:', arm, flush=True)
        law = replace(base, arm=arm)
        cases[arm] = finite(law, x0)
        cases[arm]['graph_audit'] = audit_graph(law, x0)
    for name, state in [('source_absent', (0, 0, 2, 0)),
                        ('fuel_zero', (0, 0, 0, 2)),
                        ('fuel_one', (0, 0, 1, 2)),
                        ('initially_intact', (1, 0, 2, 2))]:
        for arm in ('active', 'norepair', 'constitutive'):
            key = name+'__'+arm
            print('Checking diagnostic:', key, flush=True)
            law = replace(base, arm=arm)
            cases[key] = finite(law, state)
            cases[key]['graph_audit'] = audit_graph(law, state)
    references = {arm: {k: str(v) for k, v in exact_terminal(replace(zero, arm=arm), x0).items()}
                  for arm in ('active', 'norepair', 'deadrepair')}
    assert [Q(references[a]['copy']) for a in references] == [Q(4, 5), Q(1, 2), Q(2, 5)]
    path = ['formation', 'repair', 'capture', 'copy', 'capture', 'copy']
    s = x0
    path_record = []
    for event in path:
        rows = graph(zero, [s])[s]
        matching = [(t, rate) for name, t, rate in rows if name == event]
        assert len(matching) == 1
        t, rate = matching[0]
        path_record.append({'from': s, 'event': event, 'to': t,
                            'rate': str(rate), 'exit_rate': str(sum(r for _, _, r in rows))})
        s = t
    L = Q(2, 5)*prod(1-Q(1, 7**q) for q in (6, 5))
    L += Q(4, 15)*prod(1-Q(1, 7**q) for q in (6, 5, 2, 3, 1, 2))
    assert L > Q(3, 5)
    assert Q(1, 10)-2*4*6*Q(1, 10000)*12 == Q(53, 1250)
    assert Q(1, 2)*(1-Q(1, 7**18))*(1-Q(1, 7**12)) > Q(49, 100)
    assert Q(9, 100)-2*2*6*Q(1, 10000)*12 == Q(153, 2500)
    # Compare separate endpoints with conservative margins; no fitted thresholds.
    assert lower(cases['active'], 'copy')-upper(cases['norepair'], 'copy') > Decimal('0.0424')
    assert lower(cases['source_absent__norepair'], 'copy')-upper(cases['source_absent__active'], 'copy') > Decimal('0.0612')
    assert lower(cases['active'], 'capture') > upper(cases['deadrepair'], 'capture')
    assert upper(cases['noformation'], 'copy') < Decimal('1e-18')
    assert upper(cases['wrongcue'], 'copy') < Decimal('1e-18')
    assert upper(cases['nocopy'], 'copy') < Decimal('1e-18')
    for prep in ('fuel_zero', 'fuel_one'):
        assert upper(cases[prep+'__active'], 'capture') < Decimal('1e-18')
    # Numerical ledger enclosure: each true expectation satisfies the identity.
    for case in cases.values():
        initial_fuel = case['initial'][2]+case['initial'][3]
        names = ('formation', 'repair', 'copy', 'deadrepair', 'leak', 'burncapture')
        lo = sum(lower(case, k) for k in names)
        hi = sum(upper(case, k) for k in names)
        for k in ('F', 'E'):
            lo += Decimal(case['endpoint'][k]['lower'])
            hi += Decimal(case['endpoint'][k]['upper'])
        # This diagnostic sum uses Decimal's default precision; enclosures themselves
        # are computed with explicit outward rounding in model.py.
        assert lo-Decimal('1e-24') <= initial_fuel <= hi+Decimal('1e-24')
    post = (1, 1, 0, 2)
    sequences = {
        'capture_break_restore': succession([replace(base, arm='nocapture'), base], post, [4, 8]),
        'capture_broken': succession([replace(base, arm='nocapture')], post, [12]),
        'capture_continuous': succession([base], post, [12]),
        'cue_break_restore': succession([replace(base, arm='wrongcue'), base], x0, [4, 8]),
        'cue_broken': succession([replace(base, arm='wrongcue')], x0, [12]),
    }
    assert lower(sequences['capture_break_restore'], 'copy') > upper(sequences['capture_broken'], 'copy')
    assert lower(sequences['cue_break_restore'], 'formation') > upper(sequences['cue_broken'], 'formation')
    # Split integration must enclose the same law's unsplit expectation.
    split = succession([base, base], x0, [4, 8])
    for name in EVENTS+('intact_time',):
        assert max(lower(split, name), lower(cases['active'], name)) <= min(upper(split, name), upper(cases['active'], name))
    result = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'passed', 'source_hashes': initial_hashes,
        'scope': 'Finite declared chemical event law. Exact terminal expectations and outward-enclosed finite-time expectations; no calibration, molecular validation, adaptive selection, or universal direction.',
        'cases': cases, 'zero_loss_reference': references, 'constructive_path': path_record,
        'analytic_certificates': {'path_lower_bound': str(L), 'positive_gap_lower': '53/1250',
                                  'source_absent_reverse_gap_lower': '153/2500'},
        'successor_interventions': sequences, 'split_semigroup_check': 'passed',
    }
    assert all(sha256((HERE/name).read_bytes()).hexdigest() == digest for name, digest in initial_hashes.items())
    (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('All declared checks passed; results.json saved.', flush=True)


if __name__ == '__main__':
    run()
