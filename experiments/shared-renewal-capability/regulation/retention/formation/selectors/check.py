#!/usr/bin/env python3
"""Run the prespecified exact comparisons and discrete recovery diagnostics."""
import hashlib
import json
from dataclasses import replace
from fractions import Fraction as Q
from pathlib import Path
from model import Law, State, POLICIES, cases, distribution, metrics, recovery_bound

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    before = {name: digest(ROOT/name) for name in ('model.py', 'check.py', 'PROTOCOL.md')}
    comparisons = {}
    for name, law in cases().items():
        arms = {}
        reference = None
        for policy in POLICIES:
            dist, sizes = distribution(law, policy)
            if policy == 'material':
                reference = dist
            if policy == 'automaton':
                assert dist == reference, (name, 'conventional distribution mismatch')
            values = metrics(law, dist)
            arms[policy] = {
                'exact': {k: str(v) for k, v in values.items()},
                'decimal': {k: float(v) for k, v in values.items()},
                'state_counts_by_exposure': sizes,
            }
            print(name, policy, 'capture=', float(values['captures']),
                  'witness=', float(values['p_revision_witness']),
                  'ready=', float(values['p_ready']), flush=True)
        comparisons[name] = {'law': law.record(), 'arms': arms}

    diagnostic_rows = []
    # Known obsolete orientation; no reset assertion about unconditional runs.
    for lifetime in (1, 2, 3):
        for residual in range(lifetime+1):
            for fuel in range(0, 21):
                for horizon in (0, 1, 3, 6, 9):
                    law = Law(initial_fuel=fuel, lifetime=lifetime,
                              horizon=horizon, reversals=())
                    start = State(fuel, mode=0, lease=residual)
                    dist, _ = distribution(law, 'material', start,
                                           initial_modes=((1, Q(1)),))
                    actual = sum((p for (_, s), p in dist.items() if s.captures), Q(0))
                    slots, bound = recovery_bound(fuel, residual, horizon,
                                                 lifetime=lifetime)
                    assert actual == bound, (lifetime, residual, fuel, horizon, actual, bound)
                    diagnostic_rows.append((lifetime, residual, fuel, horizon,
                                            slots, str(actual)))
    assert all(digest(ROOT/name) == h for name, h in before.items())
    result = {'status': 'passed', 'arithmetic': 'exact fractions; no Monte Carlo',
              'source_sha256': before, 'cases': comparisons,
              'recovery_diagnostics': {'count': len(diagnostic_rows), 'rows': diagnostic_rows},
              'scope': 'finite declared model; no empirical identification or historical priority'}
    (ROOT/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('Passed', len(comparisons), 'cases and', len(diagnostic_rows), 'recovery diagnostics.')


if __name__ == '__main__':
    main()
