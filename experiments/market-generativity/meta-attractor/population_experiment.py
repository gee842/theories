#!/usr/bin/env python3
"""Finite cross-checks and trajectories, supplementary to the Lean proofs."""
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def step(n, fee, cap, k, state):
    r, b, v = state
    active = b >= fee
    return (min(n, r+k) if active else max(0, r-k),
            min(fee, b-(fee if active else 0)+r+(3*(n-r) if active else 0)),
            min(cap, max(0, v+r-(n-r))))


def individual_step(n, fee, cap, k, state):
    r, b, v = state
    active = b >= fee
    old = [False]*r + [True]*(n-r)
    contracts = old.copy()
    # Slots eligible for a strictly beneficial revision; inherited contracts
    # need not be optimal when their revision is not yet available.
    eligible = [i for i, a in enumerate(old) if a == active]
    if not active:
        eligible.reverse()
    for i in eligible[:k]:
        others = sum(old)-old[i]
        utility = lambda a: 6+2*a-(others+a)-(3*a if active else 0)
        contracts[i] = not active
        assert utility(contracts[i]) > utility(old[i])
    public = sum(1 if not a else (3 if active else 0) for a in old)
    gross = sum(7 if not a else 8 for a in old)
    private = sum(6 if not a else (5 if active else 8) for a in old)
    assert gross == public+private
    assert private >= n  # Affordability only; physical availability is separate.
    spent = fee if active else 0
    raw = b-spent+public
    kept, released = min(fee, raw), max(0, raw-fee)
    assert b+public == spent+kept+released
    next_state = (contracts.count(False), kept,
                  min(cap, max(0, v+sum(1 if not a else -1 for a in old))))
    assert sum(a != b for a, b in zip(old, contracts)) <= k
    return next_state


def ledger(r, schedule):
    contributions = 0
    for k in schedule[:r]:
        contributions += r
        r = max(0, r-k)
    return contributions


def trajectory(n, fee, cap, state, schedule, rounds):
    out = [state]
    for t in range(rounds):
        k = schedule[t] if t < len(schedule) else 1
        state = step(n, fee, cap, k, state)
        out.append(state)
    return out


def main():
    micro_cases = 0
    for n in range(1, 9):
        for r, fee, k in product(range(n+1), range(n+1), range(n+2)):
            for b in sorted({0, max(0, fee-1), fee, fee+1}):
                for v in (0, 3, 9):
                    state = (r, b, v)
                    assert step(n, fee, 9, k, state) == individual_step(n, fee, 9, k, state)
                    micro_cases += 1
    boundary_cases = 0
    topup_cases = 0
    for n in range(1, 6):
        for r in range(n+1):
            for schedule in product((1, 2, 3), repeat=r):
                a = ledger(r, schedule)
                for fee in range(n+1):
                    for b in range(fee+1):
                        state = (r, b, 12)
                        rows = trajectory(n, fee, 12, state, schedule, r+n+15)
                        funded = any(x[1] >= fee for x in rows)
                        assert funded == (b+a >= fee)
                        if funded:
                            assert rows[-1] == (n, fee, 12)
                        else:
                            assert rows[-1] == (0, b+a, 0)
                        boundary_cases += 1
                        needed = max(0, fee-(b+a))
                        for extra in sorted({0, max(0, needed-1), needed}):
                            boosted = (r, min(fee, b+extra), 12)
                            rows2 = trajectory(n, fee, 12, boosted, schedule, r+n+15)
                            assert any(x[1] >= fee for x in rows2) == (needed <= extra)
                            topup_cases += 1
    examples = {
        'unit_revision': trajectory(6, 6, 12, (3,0,12), [1]*12, 12),
        'growing_revision': trajectory(6, 6, 12, (3,0,12), list(range(1,13)), 12),
        'growing_with_one_reserve': trajectory(6, 6, 12, (3,1,12), list(range(1,13)), 12),
    }
    assert min(x[2] for x in examples['unit_revision']) == 0
    assert min(x[2] for x in examples['growing_with_one_reserve']) == 4
    report = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'micro_allocation_and_accounting_cases': micro_cases,
        'schedule_boundary_cases': boundary_cases, 'topup_cases': topup_cases,
        'formal_source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in [HERE/'PopulationCorrection.lean', HERE/'PopulationRealization.lean']},
        'example_columns': ['renewing_contracts', 'corrective_reserve', 'shared_capacity'],
        'examples': examples,
        'scope': 'Finite independent implementation cross-check and illustrative trajectories. No proof substitute, observed population data, calibrated parameter estimates or empirical frequency claim.'
    }
    (HERE/'population-experiment.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k.endswith('_cases') or k == 'status'}))


if __name__ == '__main__':
    main()
