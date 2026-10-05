"""Rerun the independent raw-case audit described in REVIEW.md.

Uses only the Python standard library. Run from any working directory:
    python /absolute/path/to/discrimination/verify_independent.py

The row constructor comes from the separately written formation raw-case
enumerator, not from a production mechanism helper. Exactly one expression is
extended in memory to select the constant-turnover rival. Neither that source
nor the production implementation/results are modified. The production module
is imported only to supply arm settings and actual values for comparison.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
FORMATION = ROOT.parent.parent / 'gap-resolution' / 'formation-coupled'
ENUMERATOR = FORMATION / 'verify_independent.py'
KNOWN_ENUMERATOR_SHA256 = 'fb39a40507661dc3d8ec51e158a4d132d0763d4ffcb065ab4ab0af58e245835f'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_raw_constructor():
    # Fail explicitly if the audited dependency changes; do not silently patch
    # a different constructor or claim that a new version was reviewed.
    assert sha256(ENUMERATOR) == KNOWN_ENUMERATOR_SHA256
    source = ENUMERATOR.read_text()
    original = 'delta = F(1, 20) + F(harms, 5 * cases_per_round)'
    replacement = ('delta = (F(1, 20) + F(harms, 5 * cases_per_round)) '
                   'if arm.feedback else F(3, 20)')
    assert source.count(original) == 1
    namespace = {
        '__name__': 'independent_discrimination_raw_cases',
        '__file__': str(ENUMERATOR),
    }
    # A non-main module name prevents the earlier checker's runner from running.
    exec(compile(source.replace(original, replacement), str(ENUMERATOR), 'exec'), namespace)
    return lru_cache(maxsize=None)(namespace['independent'])


def reduced_row(k, q):
    """Rational skill/practice/event row, derived without production helpers."""
    pre = 2 if (k, q) == (1, 1) else k
    out = defaultdict(F)
    out[(pre, q, 0)] += F(17, 20)
    post = max(0, pre - 1)
    weight = F(4) if q else F(1, 4)
    adaptive = post * weight / (1 + post * weight)
    out[(post, 1, 1)] += F(3, 20) * adaptive
    out[(post, 0, 1)] += F(3, 20) * (1 - adaptive)
    return {key: value for key, value in out.items() if value}


def exact_reduced_survival():
    distribution = {(2, 1): F(1)}
    for _ in range(25):
        nxt = defaultdict(F)
        for state, weight in distribution.items():
            for (k, q, _), probability in reduced_row(*state).items():
                nxt[(k, q)] += weight * probability
        distribution = dict(nxt)
    assert sum(distribution.values()) == 1
    return sum(weight for (k, _), weight in distribution.items() if k > 0)


def main():
    protected_paths = (ROOT / 'analyze.py', ROOT / 'analysis.json',
                       ROOT / 'PROTOCOL.md', FORMATION / 'analyze.py', ENUMERATOR)
    before = {str(path.relative_to(ROOT.parent.parent)): sha256(path)
              for path in protected_paths}
    recorded = json.loads((ROOT / 'analysis.json').read_text())
    assert recorded['code_sha256'] == sha256(ROOT / 'analyze.py')
    assert recorded['source_sha256'] == sha256(FORMATION / 'analyze.py')
    assert recorded['protocol_sha256'] == sha256(ROOT / 'PROTOCOL.md')
    spec = importlib.util.spec_from_file_location('discrimination_for_independent_audit', ROOT / 'analyze.py')
    target = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = target
    spec.loader.exec_module(target)
    independent = load_raw_constructor()
    initial = (2, 1, 0, 0, 0, 0, -1, 0)
    assert target.base.INITIAL == initial and target.base.HORIZON == 25
    checked_rows, maximum_row_error, maximum_reward_error = 0, 0., 0.
    maximum_projection_error, maximum_mass_error = 0., 0.
    results, counts = {}, {}

    for feedback in (True, False):
        for execution in (True, False):
            name = ('feedback' if feedback else 'constant') + ('_enabled' if execution else '_blocked')
            arm = target.Arm(name, feedback=feedback, execution=execution)
            seen, pending = {initial}, [initial]
            while pending:
                state = pending.pop()
                expected, rewards = independent(arm, state)
                branches, actual_rewards = target.transition(arm, state)
                actual, projected = defaultdict(float), defaultdict(float)
                for successor, turnover, probability in branches:
                    actual[successor] += probability
                    projected[(successor[0], successor[1], turnover)] += probability
                assert set(actual) == set(expected), (name, state)
                row_error = max(abs(actual[s] - float(p)) for s, p in expected.items())
                assert row_error < 2e-14, (name, state, row_error)
                maximum_row_error = max(maximum_row_error, row_error)
                for reward_name, value in rewards.items():
                    error = abs(float(value) - actual_rewards[target.base.REWARDS.index(reward_name)])
                    assert error < 2e-14, (name, state, reward_name, error)
                    maximum_reward_error = max(maximum_reward_error, error)
                if not execution or not feedback:
                    reduced = reduced_row(*state[:2])
                    error = max(abs(projected.get(key, 0.) - float(reduced.get(key, 0)))
                                for key in projected.keys() | reduced.keys())
                    assert error < 2e-14, (name, state, error)
                    maximum_projection_error = max(maximum_projection_error, error)
                checked_rows += 1
                for successor in expected:
                    if successor not in seen:
                        seen.add(successor)
                        pending.append(successor)
            counts[name] = len(seen)
            distribution = {initial: 1.}
            for _ in range(25):
                nxt = defaultdict(float)
                for state, weight in distribution.items():
                    for successor, probability in independent(arm, state)[0].items():
                        nxt[successor] += weight * float(probability)
                distribution = dict(nxt)
                mass_error = abs(sum(distribution.values()) - 1.)
                assert mass_error < 2e-12
                maximum_mass_error = max(maximum_mass_error, mass_error)
            results[name] = sum(weight for state, weight in distribution.items() if state[0] > 0)

    endpoint_errors = {
        name: abs(value - recorded['arms'][name]['endpoint']['skill_positive'])
        for name, value in results.items()
    }
    assert max(endpoint_errors.values()) < 2e-12
    exact_survival = exact_reduced_survival()
    for name in ('feedback_blocked', 'constant_blocked', 'constant_enabled'):
        assert abs(results[name] - float(exact_survival)) < 2e-12
    contrasts = {model: results[model + '_enabled'] - results[model + '_blocked']
                 for model in ('feedback', 'constant')}
    primary = contrasts['feedback'] - contrasts['constant']
    saved_primary = (recorded['contrasts']['feedback']['enabled_minus_blocked']['skill_positive']
                     - recorded['contrasts']['constant']['enabled_minus_blocked']['skill_positive'])
    assert abs(primary - saved_primary) < 2e-12
    after = {str(path.relative_to(ROOT.parent.parent)): sha256(path)
             for path in protected_paths}
    assert before == after
    report = {
        'all_checks_passed': True,
        'scope': ('Independent rational raw-case rows for all reachable states in four primary arms; '
                  'floating-point propagation of those rows for round-25 skill; independent rational '
                  'reduced-chain calculation. This verifies supplied models, not empirical truth.'),
        'row_constructor': 'Earlier independent raw-case enumerator, with one in-memory turnover-law extension',
        'source_files_unchanged': before == after,
        'reachable_rows_by_arm': counts,
        'total_raw_case_rows_checked': checked_rows,
        'maximum_row_probability_difference': maximum_row_error,
        'maximum_reward_difference': maximum_reward_error,
        'maximum_reduced_projection_difference': maximum_projection_error,
        'maximum_propagation_mass_error': maximum_mass_error,
        'round25_skill_retention': results,
        'saved_endpoint_differences': endpoint_errors,
        'within_model_execution_effects': contrasts,
        'primary_difference_between_effects': primary,
        'primary_difference_from_saved_result': abs(primary - saved_primary),
        'reduced_chain_exact_survival25': str(exact_survival),
        'reduced_chain_decimal_survival25': float(exact_survival),
        'audited_source_sha256': before,
        'checker_sha256': sha256(Path(__file__)),
    }
    (ROOT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
