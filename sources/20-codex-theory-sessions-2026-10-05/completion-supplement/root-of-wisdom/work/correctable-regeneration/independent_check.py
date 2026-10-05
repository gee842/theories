"""Independent exact recurrence check; does not import construction code.

The modeled protocol has a prefunded maintained claim gate, a delayed
protective interval, and compulsory release at the participant reserve cap.
These are supplied transition rules, not strategic-equilibrium claims.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def run(*, ceiling=6, threshold=4, filing_cost=1, delay=2,
        funding=F(11, 9), cap=F(3), initial_q=F(3), rounds=100):
    b, q = F(ceiling), F(initial_q)
    state = 'extract'
    remaining = 0
    rows = []
    for t in range(rounds):
        # An unavailable maintained carrier is a stopping event for this
        # independent check; no post-failure resurrection is assumed.
        if q < 1:
            return rows, 'carrier_unfunded'
        pbill = qbill = 0
        requested = state == 'extract' and b <= threshold
        if requested and q >= 3 and b >= filing_cost:
            pbill, qbill = filing_cost, 2
            state, remaining = 'pending', delay
        mode = 'F' if state == 'protect' else 'X'
        a = 3 if mode == 'F' else 1
        bnext = min(F(ceiling), b - pbill + a - 2)
        qgross = q - 1 - qbill + funding
        qnext = min(cap, qgross)
        row = dict(t=t + 1, b=b, q=q, mode=mode, requested=requested,
                   pbill=pbill, qbill=qbill, bnext=bnext, qnext=qnext,
                   spill=max(F(0), qgross-cap))
        rows.append(row)
        b, q = bnext, qnext
        if b < 1:
            return rows, 'participant_floor'
        if state == 'pending':
            remaining -= 1
            if remaining == 0:
                state = 'protect'
        elif state == 'protect' and b == ceiling:
            state = 'extract'
    return rows, 'horizon'


def main():
    rows, status = run(rounds=45)
    assert status == 'horizon'
    assert [r['bnext'] for r in rows[:9]] == [5, 4, 2, 1, 2, 3, 4, 5, 6]
    assert [r['mode'] for r in rows[:9]] == ['X'] * 4 + ['F'] * 5
    assert rows[8]['qnext'] == F(23, 9)
    assert min(r['bnext'] for r in rows) == 1
    assert sum(r['qbill'] for r in rows[:9]) == 2
    assert sum(r['pbill'] for r in rows[:9]) == 1
    assert sum(r['spill'] for r in rows[:9]) == F(4, 9)
    # Compare the periodic sections after the initial filling transient.
    canonical = lambda rs: [{k: v for k, v in r.items() if k != 't'} for r in rs]
    assert canonical(rows[9:18]) == canonical(rows[18:27])

    family = 0
    for m in range(3, 11):
        for d in range(1, 4):
            for c in range(1, 3):
                for h in range(c + d + 1, m + 1):
                    length = 2 * (m - h) + c + 2 * d
                    rs, st = run(ceiling=m, threshold=h, filing_cost=c,
                                 delay=d, funding=1+F(2, length), rounds=length * 4)
                    assert st == 'horizon'
                    assert min(r['bnext'] for r in rs) == h - c - d
                    assert [r['t'] for r in rs if r['qbill']] == [m-h+1 + j*length for j in range(4)]
                    assert canonical(rs[length:2*length]) == canonical(rs[2*length:3*length])
                    family += 1

    failures = {}
    for name, args in {
        'less_than_claim_capacity': dict(cap=F(299, 100), initial_q=F(299, 100)),
        'upkeep_only_funding': dict(funding=F(1)),
        'below_recurrent_funding_with_extra_initial_stock': dict(funding=F(11, 9)-F(1, 90), cap=F(5), initial_q=F(5), rounds=500),
        'late_trigger': dict(threshold=3),
        'extra_delay': dict(delay=3),
    }.items():
        rs, st = run(**args)
        assert st != 'horizon', name
        failures[name] = dict(first_failure_round=len(rs), kind=st)

    early, early_status = run(threshold=5, funding=F(9, 7), rounds=28)
    assert early_status == 'horizon'
    assert min(r['bnext'] for r in early) == 2
    assert [r['t'] for r in early if r['qbill']] == [2, 9, 16, 23]

    output = dict(status='all_exact_independent_checks_passed',
                  method='Fraction recurrence independent of author code',
                  generalized_safe_parameter_cases=family,
                  initial_nine_rounds=rows[:9],
                  steady_nine_rounds=rows[9:18],
                  failures=failures,
                  earlier_trigger=dict(threshold=5, minimum_b=2, length=7,
                                       funding_minimum=F(9, 7)),
                  scope='A supplied delayed temporary-gate protocol; no optimality across other protocols.')
    path = Path(__file__).with_name('independent-results.json')
    path.write_text(json.dumps(output, default=str, indent=2) + '\n')
    print(json.dumps({k: v for k, v in output.items() if k not in ('initial_nine_rounds', 'steady_nine_rounds')}, default=str, indent=2))


if __name__ == '__main__':
    main()
