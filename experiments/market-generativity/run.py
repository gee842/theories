#!/usr/bin/env python3
"""Exact local checks, disclosed numerical continuations and saved ledgers."""
from dataclasses import fields, replace
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import csv
import hashlib
import json

from model import Parameters, Support, State, validate, step, rectangle_margins, in_rectangle

HERE = Path(__file__).resolve().parent


def decimal(n):
    if isinstance(n, F):
        return Decimal(n.numerator) / Decimal(n.denominator)
    return Decimal(n)


def convert(p, s):
    supports = tuple(Support(*(decimal(getattr(c, a.name))
                               if a.name != 'essential' else c.essential
                               for a in fields(c))) for c in p.supports)
    args = {a.name: decimal(getattr(p, a.name)) for a in fields(p) if a.name != 'supports'}
    args['supports'] = supports
    return Parameters(**args), State(*(decimal(v) for v in
        (s.renewers, s.accountability, s.influence, s.fund)),
        tuple(decimal(v) for v in s.supports), s.operating)


def exact_ledger(p, s, t, ledger):
    assert ledger['receipts'] == sum(ledger[k] for k in
        ('levy', 'restitution', 'political_bill', 'renewal_bill', 'distributed_profit'))
    assert s.fund + ledger['levy'] == (t.fund + ledger['restoration_bill'] + ledger['surplus'])


def exact_checks():
    p = Parameters()
    validate(p)
    margins = rectangle_margins(p, F(3, 4), F(1, 2), F(1, 4), F(1, 20), (F(1, 2),))
    assert margins['selection'] > 0
    assert all(margins[k] >= 0 for k in ('influence', 'accountability', 'funding'))
    assert all(v >= 0 for v in margins['supports'])
    count = 0
    for x, q, w, b, c, e, v in product(
            (F(3, 4), F(7, 8), F(1)), (F(1, 2), F(3, 4), F(1)),
            (F(0), F(1, 8), F(1, 4)), (F(1), F(2), F(3)),
            (F(5), F(8), F(20)), (F(0), F(1, 40), F(1, 20)),
            (F(0), F(1, 4), F(1, 2))):
        s = State(x, q, w, b, (c,))
        t, ledger = step(p, s, e, (v,))
        assert in_rectangle(p, s) and in_rectangle(p, t)
        assert t.renewers >= s.renewers
        exact_ledger(p, s, t, ledger)
        count += 1
    # A collar outside q and influence bounds enters in one paid round.
    collar = State(F(4, 5), F(49, 100), F(13, 50), F(1), (F(5),))
    t, ledger = step(p, collar, F(1, 20), (F(1, 2),))
    assert not in_rectangle(p, collar) and in_rectangle(p, t)
    assert t.accountability == F(2519, 5000) and t.influence == F(49, 200)
    exact_ledger(p, collar, t, ledger)
    # Even a temporarily negative profit gap can be reversed before failure.
    reversal = State(F(4, 5), F(7, 20), F(1, 20), F(1), (F(5),))
    t, ledger = step(p, reversal)
    assert ledger['profit_gap'] == F(-1, 10)
    assert t.renewers < reversal.renewers and in_rectangle(p, t)
    # Profitability and immediate favorable selection do not imply renewal.
    thin = State(F(1, 10), F(1), F(0), F(1), (F(5),))
    t, ledger = step(p, thin)
    assert ledger['profit_gap'] > 0 and not t.operating and t.supports[0] == F(19, 5)
    # Equal eventual funding cannot pay this round's bill.
    no_cash = State(F(3, 4), F(1, 2), F(1, 4), F(0), (F(5),))
    t, ledger = step(p, no_cash)
    assert not ledger['paid'] and t.fund == 1 and t.accountability == F(7, 16)
    # Missing authorization has the same first-round physical repair failure.
    veto = replace(no_cash, fund=F(1))
    t_veto, bill_veto = step(p, veto, authorized=False)
    assert not bill_veto['paid'] and t_veto.accountability == t.accountability
    # If no renewing variant exists, payoff-driven selection creates none.
    absent = State(F(0), F(1), F(0), F(1), (F(100),))
    t, ledger = step(p, absent)
    assert t.renewers == 0
    # A nonessential recipient can be depleted in an economically stable state.
    excluded = Support(F(0), F(0), F(1, 10), F(1), F(5), False)
    pp = replace(p, supports=p.supports + (excluded,))
    ss = State(F(1), F(1), F(0), F(1), (F(20), F(5)))
    tt, ll = step(pp, ss)
    assert tt.operating and tt.supports[0] == 20 and tt.supports[1] == F(7, 2)
    # Rectangle lower-face boundaries tested just beyond the derived limits.
    boundary_failures = {}
    base = State(F(3, 4), F(1, 2), F(1, 4), F(1), (F(5),))
    t, _ = step(p, base, F(1, 16) + F(1, 1000))
    boundary_failures['erosion_above_1_16'] = t.accountability < F(1, 2)
    t, _ = step(p, base, losses=(F(3, 4) + F(1, 1000),))
    boundary_failures['loss_above_3_4'] = t.supports[0] < 5
    t, _ = step(replace(p, levy=F(999, 1000)), base)
    boundary_failures['levy_below_cost'] = t.fund < 1
    bad_influence = State(F(3, 4), F(1, 2), F(249, 1000), F(1), (F(5),))
    t, _ = step(p, bad_influence)
    boundary_failures['influence_bound_below_target'] = t.influence > bad_influence.influence
    threshold = (p.renewal_cost - p.political_cost) / p.liability
    low_q = State(F(3, 4), threshold - F(1, 1000), F(1, 4), F(1), (F(5),))
    t, _ = step(p, low_q)
    boundary_failures['q_below_profit_threshold'] = t.renewers < F(3, 4)
    assert all(boundary_failures.values())
    return {'rational_rectangle_points': count, 'condition_margins': margins,
            'boundary_counterexamples': boundary_failures,
            'exact_examples': ['one_step_recovery', 'initially_negative_gap_recovery',
                'positive_gap_but_support_failure', 'pre_receipt_liquidity',
                'authority_veto', 'absent_variant', 'excluded_recipient'],
            'cash_and_fund_identities': 'exact at every grid point'}


def scenarios():
    p = Parameters()
    high = State(F(4, 5), F(3, 5), F(1, 5), F(1), (F(8),))
    low = State(F(2, 25), F(7, 20), F(19, 20), F(1), (F(100),))
    excluded = Support(F(0), F(0), F(1, 10), F(1), F(5), False)
    return [
        ('renewal_basin', p, high, {}),
        ('bounded_adverse_shocks', p, high, {'erosion': F(1, 20), 'losses': (F(1, 2),)}),
        ('capture_collapse', p, low, {}),
        ('same_initial_no_capture', replace(p, capture=F(0)), low, {}),
        ('rule_frozen_at_initial', p, low, {'freeze_rule': True}),
        ('ideal_fixed_rule', p, replace(low, accountability=F(1)), {'freeze_rule': True}),
        ('unfunded_initial_round', p, State(F(1, 2), F(1, 2), F(1), F(0), (F(5),)), {}),
        ('permanent_authority_veto', p, high, {'authorized': False}),
        ('levy_below_recurring_cost', replace(p, levy=F(1, 2)), high, {}),
        ('no_renewing_variant', p, replace(low, renewers=F(0)), {}),
        ('recovery_after_initial_negative_gap', p,
         State(F(4, 5), F(7, 20), F(1, 20), F(1), (F(5),)), {}),
        ('excluded_recipient', replace(p, supports=p.supports + (excluded,)),
         State(F(1), F(1), F(0), F(1), (F(20), F(5))), {}),
    ]


def serialize(v):
    if isinstance(v, (F, Decimal)):
        return str(v)
    if hasattr(v, '__dataclass_fields__'):
        return {f.name: serialize(getattr(v, f.name)) for f in fields(v)}
    if isinstance(v, dict):
        return {k: serialize(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)):
        return [serialize(x) for x in v]
    return v


def numerical_runs(precision=80, horizon=800, save=True):
    result = {}
    rows = []
    with localcontext() as ctx:
        ctx.prec = precision
        for name, rp, rs, options in scenarios():
            validate(rp)
            p, s = convert(rp, rs)
            opts = {k: (tuple(decimal(v) for v in val) if k == 'losses' else
                         val if isinstance(val, bool) else decimal(val)) for k, val in options.items()}
            first_failure = None
            first_support_violation = None
            minimum = list(s.supports)
            paid_rounds = 0
            max_cash_residual = Decimal(0)
            for t in range(horizon + 1):
                if any(v < c.floor for v, c in zip(s.supports, p.supports)) and first_support_violation is None:
                    first_support_violation = t
                if not s.operating and first_failure is None:
                    first_failure = t
                minimum = [min(a, b) for a, b in zip(minimum, s.supports)]
                rows.append({'scenario': name, 't': t, 'operating': s.operating,
                    'x': str(s.renewers), 'q': str(s.accountability), 'w': str(s.influence),
                    'B': str(s.fund), 'C': str(s.supports[0]),
                    'recipient': str(s.supports[1]) if len(s.supports) > 1 else ''})
                if t == horizon:
                    break
                nxt, ledger = step(p, s, **opts)
                paid_rounds += int(ledger['paid'])
                residual = abs(ledger['receipts'] - sum(ledger[k] for k in
                    ('levy', 'restitution', 'political_bill', 'renewal_bill', 'distributed_profit')))
                max_cash_residual = max(max_cash_residual, residual,
                    abs(s.fund + ledger['levy'] - nxt.fund - ledger['restoration_bill'] - ledger['surplus']))
                s = nxt
            result[name] = {'parameters': serialize(rp), 'initial': serialize(rs), 'options': serialize(options),
                'final': serialize(s), 'first_economic_failure': first_failure,
                'first_any_support_violation': first_support_violation,
                'minimum_supports': serialize(minimum), 'paid_rounds': paid_rounds,
                'max_cash_residual': str(max_cash_residual)}
            assert max_cash_residual < Decimal('1e-' + str(precision - 8))
        assert result['renewal_basin']['first_economic_failure'] is None
        assert result['bounded_adverse_shocks']['first_any_support_violation'] is None
        assert result['capture_collapse']['first_economic_failure'] is not None
        assert result['same_initial_no_capture']['first_economic_failure'] is None
        assert result['excluded_recipient']['first_economic_failure'] is None
        assert result['excluded_recipient']['first_any_support_violation'] == 1
        assert result['recovery_after_initial_negative_gap']['first_economic_failure'] is None
        if save:
            out = HERE / 'results'
            out.mkdir(exist_ok=True)
            with (out / 'trajectories.csv').open('w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
    return result


def main():
    checks = exact_checks()
    numerical = numerical_runs()
    report = {'scope': 'Exact rational one-step checks; 80-digit Decimal finite continuations. Not empirical data.',
              'horizon': 800, 'precision': 80, 'exact_checks': serialize(checks), 'scenarios': numerical,
              'source_sha256': {f: hashlib.sha256((HERE / f).read_bytes()).hexdigest()
                                for f in ('model.py', 'run.py')}}
    out = HERE / 'results'
    out.mkdir(exist_ok=True)
    (out / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'exact_grid_checks': checks['rational_rectangle_points'],
                     'scenarios': {n: {'failure': r['first_economic_failure'],
                                      'any_support_violation': r['first_any_support_violation']}
                                   for n, r in numerical.items()}}, indent=2))


if __name__ == '__main__':
    main()
