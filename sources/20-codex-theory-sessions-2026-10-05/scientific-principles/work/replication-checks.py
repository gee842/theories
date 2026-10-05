"""Exact toy checks for replication-memo.md; no empirical claims."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

q, r = F(1, 10), F(1, 5)
rows = []
for k in (1, 2, 5, 10):
    # Independent enumeration of the common-failure/residual-miss model.
    total = F(0)
    for common, residuals in product((0, 1), product((0, 1), repeat=k)):
        probability = q if common else 1-q
        for missed in residuals:
            probability *= r if missed else 1-r
        if common or all(residuals):
            total += probability
    closed = q + (1-q)*r**k
    assert total == closed
    rows.append({'checks': k, 'miss_probability_exact': str(total),
                 'miss_probability': float(total)})

# Equal-prior binary diagnostic: accuracy .9 reduces 0-1 Bayes risk .5 -> .1.
joint = {(theta, y): F(1, 2)*(F(9, 10) if theta == y else F(1, 10))
         for theta, y in product((0, 1), repeat=2)}
risk_before = min(sum(p*(action != theta) for (theta, _), p in joint.items())
                  for action in (0, 1))
risk_after = sum(min(sum(joint[theta, y]*(action != theta) for theta in (0, 1))
                     for action in (0, 1)) for y in (0, 1))
assert (risk_before, risk_after) == (F(1, 2), F(1, 10))

# Rejection if any one of 20 independent size-.05 null tests rejects.
family_error = 1-(1-F(1,20))**20

# Random effects: shared calibration variance .04, measurement variance 1.
variance = {str(n): float(F(1,25)+F(1,n)) for n in (1,10,100,10000)}

# If tests cost at least two units, budget ten supports at most five.
assert F(10,1)//F(2,1) == 5

out = {'scope': 'Exact checks of supplied toy models, not empirical estimates',
       'common_failure_checks': rows,
       'binary_information': {'before': float(risk_before), 'after': float(risk_after),
                              'gross_value': float(risk_before-risk_after)},
       'twenty_size_point05_tests_family_error': float(family_error),
       'shared_calibration_mean_square_error': variance}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
