#!/usr/bin/env python3
"""Prespecified formation-to-retention comparisons with exact path audits."""
from dataclasses import replace
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

from process import (Law, EVENTS, MODES, MARKS, ARITHMETIC, counts, fuel, rank,
                     graph, finite, terminal, channels)

HERE = Path(__file__).resolve().parent
INITIAL = (0, 0, 0, 0, 0, 4, 1)
SPENDS = set(EVENTS)-{'capture', 'wear_a', 'wear_h', 'wear_res_a', 'wear_res_h', 'damage'}


def audit(law, initial):
    net = graph(law, [initial])
    for s, rows in net.items():
        a, h = counts(s)
        for event, t, rate in rows:
            aa, hh = counts(t)
            assert fuel(t)+int(event in SPENDS) == fuel(s)
            assert rank(t) < rank(s)
            assert aa-a == int(event in ('form_a', 'copy_a', 'bulk_a'))-int(event in ('wear_a', 'wear_res_a', 'repair_loss', 'deadrepair_loss'))
            assert hh-h == int(event in ('form_h', 'copy_h', 'bulk_h'))-int(event in ('wear_h', 'wear_res_h'))
            if event == 'copy_a':
                assert s[2] == 1 and s[4] == 1
            if event == 'copy_h':
                assert s[2] == 2 and s[4] == 1
        if law.mode == 'active' and law.wear == law.sigma == 0:
            if s[2] != 1:
                assert s[3] == s[4] == 0
            assert all(event != 'copy_h' for event, _, _ in rows)
        if initial[5] < 3 and law.mode != 'shared':
            assert s[3] == 0
        if initial[5] < 4 and law.mode != 'shared':
            assert not (s[3] and h > 0)
        if law.mode == 'noformation':
            assert a == h == 0
    return {'states': len(net), 'channels': sum(map(len, net.values())),
            'max_history_bound': rank(initial)}


def lo(case, family, name):
    return Decimal(case[family][name]['lower'])


def hi(case, family, name):
    return Decimal(case[family][name]['upper'])


def run():
    source_hashes = {name: sha256((HERE/name).read_bytes()).hexdigest()
                     for name in ('process.py', 'check.py', 'PROTOCOL.md')}
    arithmetic_hash = sha256(ARITHMETIC.read_bytes()).hexdigest()
    base = Law()
    zero = replace(base, bulk=Q(0), damage=Q(0), wear=Q(0), leak=Q(0))
    references = {}
    for mode in ('active', 'shared', 'norepair', 'deadrepair'):
        law = replace(zero, mode=mode)
        references[mode] = {k: str(v) for k, v in terminal(law, INITIAL).items()}
        audit(law, INITIAL)
    assert [Q(references[m]['A_minus_H']) for m in references] == [Q(17, 150), Q(4, 147), Q(0), Q(0)]
    assert Q(references['active'][MARKS[0]]) == Q(7, 150)
    # Establish the actual mixed-history entrance before querying comparisons.
    path = ('form_h', 'form_a', 'bind_a', 'repair', 'capture', 'copy_a')
    s, probability, path_record = INITIAL, Q(1), []
    for event in path:
        rows = channels(zero, s)
        matches = [(t, rate) for name, t, rate in rows if name == event]
        assert len(matches) == 1
        t, rate = matches[0]
        total = sum(q for _, _, q in rows)
        probability *= rate/total
        path_record.append({'state': s, 'event': event, 'next': t, 'rate': str(rate), 'exit_rate': str(total)})
        s = t
    assert probability == Q(1, 60) and counts(s) == (2, 1)
    assert [Q(r['exit_rate']) for r in path_record] == [24, 15, 8, 3, 1, 1]
    path_lower = Q(1, 60)*Q(6, 7)**6
    contrast_bound = path_lower-2*6*19*Q(1, 1000000)*12
    mixed_bound = path_lower-19*Q(1, 1000000)*12
    assert contrast_bound > 0 and mixed_bound > 0
    cases = {}
    for mode in MODES:
        print('Primary:', mode, flush=True)
        law = replace(base, mode=mode)
        cases[mode] = finite(law, INITIAL)
        cases[mode]['audit'] = audit(law, INITIAL)
    for f in (0, 1, 2, 3):
        print('Bootstrap fuel:', f, flush=True)
        initial = INITIAL[:5]+(f, 1)
        cases['fuel_'+str(f)] = finite(base, initial)
        cases['fuel_'+str(f)]['audit'] = audit(base, initial)
    # Preserve the narrower clonal fixture as a boundary, not the primary proof.
    clonal = replace(base, material=2)
    clonal_state = INITIAL[:5]+(3, 1)
    print('Clonal diagnostic', flush=True)
    cases['clonal_only'] = finite(clonal, clonal_state)
    cases['clonal_only']['audit'] = audit(clonal, clonal_state)
    assert hi(cases['clonal_only'], 'events', MARKS[0]) < Decimal('1e-3')
    work = replace(base, sigma=Q(1, 10000), bulk=Q(1, 1000000000),
                   damage=Q(1, 1000000000), wear=Q(1, 1000000000), leak=Q(1, 1000000000))
    for e in (1, 0):
        print('Work-cost source:', e, flush=True)
        initial = INITIAL[:6]+(e,)
        key = 'work_source_'+str(e)
        cases[key] = finite(work, initial)
        cases[key]['audit'] = audit(work, initial)
    def dec(q):
        return Decimal(q.numerator)/Decimal(q.denominator)
    for mode in ('norepair', 'deadrepair'):
        assert lo(cases['active'], 'endpoint', 'A_minus_H')-hi(cases[mode], 'endpoint', 'A_minus_H') > dec(contrast_bound)
    assert lo(cases['active'], 'events', MARKS[0]) > dec(mixed_bound)
    assert lo(cases['norepair'], 'endpoint', 'A_minus_H') <= 0 <= hi(cases['norepair'], 'endpoint', 'A_minus_H')
    assert lo(cases['work_source_1'], 'endpoint', 'A_minus_H') > 0
    assert hi(cases['work_source_0'], 'endpoint', 'A_minus_H') < 0
    assert hi(cases['noformation'], 'endpoint', 'population') < Decimal('1e-18')
    assert hi(cases['noassociation'], 'events', 'capture') < Decimal('1e-18')
    assert hi(cases['nocopy'], 'events', MARKS[0]) < Decimal('1e-18')
    for f in (0, 1, 2):
        assert hi(cases['fuel_'+str(f)], 'events', 'capture') < Decimal('1e-18')
    # Equal formation propensities imply equal expected counts, although their
    # total depends on all earlier repairs, copies and losses.
    for case in cases.values():
        assert max(lo(case, 'events', 'form_a'), lo(case, 'events', 'form_h')) <= min(hi(case, 'events', 'form_a'), hi(case, 'events', 'form_h'))
    result = {'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'source_hashes': source_hashes,
              'arithmetic_dependency': {'path': str(ARITHMETIC.relative_to(HERE.parents[4])), 'sha256': arithmetic_hash},
              'cases': cases, 'zero_loss_reference': references, 'mixed_path': path_record,
              'analytical_bounds': {'mixed_reference_path': str(path_lower),
                                    'positive_two_arm_abundance_gap': str(contrast_bound),
                                    'mixed_copy_count': str(mixed_bound)},
              'scope': 'Declared finite formed-variant law. Unconditional counts and marked mixed copying; no survivor conditioning, empirical identification, individual learning or selector revision.'}
    assert all(sha256((HERE/name).read_bytes()).hexdigest() == digest for name, digest in source_hashes.items())
    assert sha256(ARITHMETIC.read_bytes()).hexdigest() == arithmetic_hash
    (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('All formation, ancestry, mixed-return and source-sign checks passed.', flush=True)


if __name__ == '__main__':
    run()
