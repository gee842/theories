#!/usr/bin/env python3
"""Exact constructed response-law checks. No empirical measurements are used."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def matmul(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def response(a, b, c, count=32):
    # x_0 = 0, u_0 = 1, all later inputs = 0.
    # h[k] = C A^k B is y_{k+1}, not y_k.
    state = b
    result = []
    for _ in range(count):
        result.append(matmul(c, state)[0][0])
        state = matmul(a, state)
    return result


def main():
    values = [F(-1), F(-1, 2), F(0), F(1, 4), F(1, 2), F(1), F(2)]
    couplings = [F(-1), F(-1, 8), F(0), F(1, 8), F(1)]
    bvec, cvec = [[F(0)], [F(1)]], [[F(1), F(0)]]
    transform = [[F(1), F(1)], [F(0), F(1)]]
    inverse = [[F(1), F(-1)], [F(0), F(1)]]
    cases = []
    for a, b, gamma in product(values, values, couplings):
        matrix = [[a, gamma], [F(0), b]]
        h = response(matrix, bvec, cvec)
        determinant = h[0] * h[2] - h[1] ** 2
        assert h[:4] == [F(0), gamma, gamma * (a + b),
                         gamma * (a * a + a * b + b * b)]
        assert determinant == -gamma * gamma
        changed = response(matmul(matmul(transform, matrix), inverse),
                           matmul(transform, bvec), matmul(cvec, inverse))
        assert changed == h
        record = {"a": str(a), "b": str(b), "gamma": str(gamma),
                  "hankel_determinant": str(determinant),
                  "similarity_preserves_response": changed == h}
        if gamma:
            s = h[2] / h[1]
            p = s * s - h[3] / h[1]
            assert s == a + b and p == a * b
            prediction = h[:4]
            for k in range(4, len(h)):
                prediction.append(s * prediction[k - 1] - p * prediction[k - 2])
            assert prediction[4:] == h[4:]
            # Every scalar linear state has h1 = alpha*h0.
            # Here h0=0 and h1!=0, excluding every such alpha.
            assert h[0] == 0 and h[1] != 0
            record.update({"inferred_s": str(s), "inferred_p": str(p),
                           "unseen_terms_match": len(h) - 4,
                           "one_state_excluded": True})
        else:
            assert all(v == 0 for v in h)
            record.update({"zero_start_input_response_zero": True,
                           "note": "Other preparations or channels can still matter."})
        cases.append(record)
    results = {"status": "constructed exact-rational model verification",
               "empirical_observations": False,
               "total_cases": len(cases),
               "nonzero_coupling_cases": sum(bool(gamma) for _, _, gamma in
                                              product(values, values, couplings)),
               "zero_coupling_controls": sum(not gamma for _, _, gamma in
                                              product(values, values, couplings)),
               "terms_per_case": 32,
               "fit_terms": [0, 1, 2, 3],
               "timing": "h[k] = y[k+1] following u[0]=1, x[0]=0, later u=0",
               "scope": "finite-dimensional linear time-invariant realizations",
               "critical_limit": "Finite data force the dimension lower bound; an infinite recurrence or matching upper bound requires mechanism or order assumptions.",
               "cases": cases}
    output = Path(__file__).with_name("distinctions-grid-checks.json")
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({k: v for k, v in results.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
