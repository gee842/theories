"""Independent dense, case-by-case recursion; does not import the study code."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parent
saved = json.loads((ROOT / 'analysis.json').read_text())
checks = []


def compare(name, actual, expected):
    assert abs(actual - expected) < 3e-12, (name, actual, expected)
    checks.append({'check': name, 'actual': float(actual), 'expected': float(expected)})


def exact_ml_accuracy(n):
    answer = Fraction(0)
    for a in range(n + 1):
        for b in range(n + 1):
            errors = [a, n-a, b, n-b]
            best = min(errors)
            if a == best:
                answer += Fraction(comb(n, a) * 9**(n-a) * comb(n, b), 10**n * 2**n * errors.count(best))
    return answer


p5 = exact_ml_accuracy(5)
compare('exact five-case ML accuracy', float(p5), saved['scenarios']['stationary']['latest_replacement']['endpoint']['correct'])
compare('exact independent-batch lifetime error', float(1-p5**12), saved['scenarios']['stationary']['latest_replacement']['endpoint']['ever_wrong_declaration'])
compare('exact sixty-case stationary ML accuracy', float(exact_ml_accuracy(60)), saved['scenarios']['stationary']['cumulative_replacement']['endpoint']['correct'])

for changed in [False, True]:
    scenario = 'changed' if changed else 'stationary'
    # Axes: held expression (4 denotes none), X1 mismatch, X2 mismatch.
    total = np.zeros((5, 61, 61))
    clean = total.copy()  # mass with no false declaration so far
    total[4, 0, 0] = clean[4, 0, 0] = 1.
    for n in range(1, 61):
        truth = int(changed and n > 30)
        noise = .9 if truth else .1
        updates = []
        for current in (total, clean):
            after = np.zeros_like(current)
            for da, db, weight in [(0, 0, (1-noise)/2), (0, 1, (1-noise)/2), (1, 0, noise/2), (1, 1, noise/2)]:
                after[:, da:n+da, db:n+db] += weight * current[:, :n, :n]
            updates.append(after)
        total, clean = updates
        if n % 5:
            continue
        i, j = np.indices((n+1, n+1))
        errors = np.stack([i, n-i, j, n-j])
        order = np.sort(errors, axis=0)
        qualified = order[1] - order[0] >= 2
        winner = errors.argmin(axis=0)
        before = total.sum(axis=0)
        clean_before = clean.sum(axis=0)
        fresh_wrong = float(before[:n+1, :n+1][qualified & (winner != truth)].sum())
        for h in range(4):
            mask = qualified & (winner == h)
            for held in range(5):
                total[held, :n+1, :n+1][mask] = 0.
                clean[held, :n+1, :n+1][mask] = 0.
            total[h, :n+1, :n+1][mask] = before[:n+1, :n+1][mask]
            if h == truth:
                clean[h, :n+1, :n+1][mask] = clean_before[:n+1, :n+1][mask]
        row = saved['scenarios'][scenario]['cumulative_certificate']['curve'][n//5-1]
        compare(f'{scenario} n={n} mass', total.sum(), 1.)
        compare(f'{scenario} n={n} certificate correct', total[truth].sum(), row['correct'])
        compare(f'{scenario} n={n} certificate undeclared', total[4].sum(), row['undeclared'])
        compare(f'{scenario} n={n} certificate ever false', 1-clean.sum(), row['ever_wrong_declaration'])
        compare(f'{scenario} n={n} certificate fresh false', fresh_wrong, row['new_wrong_declaration'])
        # Independently integrate the ML rule against the marginal count law.
        ties = errors == errors.min(axis=0)
        ml_accuracy = (before[:n+1, :n+1] * ties[truth] / ties.sum(axis=0)).sum()
        compare(f'{scenario} n={n} ML marginal accuracy', ml_accuracy,
                saved['scenarios'][scenario]['cumulative_replacement']['curve'][n//5-1]['correct'])

output = {'method': 'independent dense per-case recursion and exact rational marginal calculations',
          'checks_passed': len(checks), 'max_difference': max(abs(x['actual']-x['expected']) for x in checks),
          'five_case_accuracy_exact': str(p5), 'checks': checks}
(ROOT / 'independent-check.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({k: v for k, v in output.items() if k != 'checks'}))
