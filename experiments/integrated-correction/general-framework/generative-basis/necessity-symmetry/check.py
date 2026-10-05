"""Finite exhaustive audit of the actor/patient symmetry bridge.

AI-authored research, 6 October 2026. This enumerates stipulated binary
reason-relevance relations; it is not a measurement of human moral judgment.
The universal orbit argument is in HUIGEN-FULL-THEORY-AUDIT.md.
"""

from itertools import permutations
from pathlib import Path
import hashlib
import json


def matrix_from_bits(bits, n):
    return tuple(tuple((bits >> (a * n + i)) & 1 for i in range(n))
                 for a in range(n))


def invariant_under_joint_renaming(matrix, relabelings):
    n = len(matrix)
    return all(matrix[p[a]][p[i]] == matrix[a][i]
               for p in relabelings for a in range(n) for i in range(n))


def actor_independent(matrix):
    n = len(matrix)
    return all(matrix[a][i] == matrix[b][i]
               for a in range(n) for b in range(n) for i in range(n))


def run_case(n):
    relabelings = list(permutations(range(n)))
    admitted = []
    for bits in range(1 << (n * n)):
        matrix = matrix_from_bits(bits, n)
        if invariant_under_joint_renaming(matrix, relabelings):
            admitted.append(matrix)
    self_positive = [m for m in admitted if all(m[a][a] == 1 for a in range(n))]
    independent = [m for m in admitted if actor_independent(m)]
    positive_independent = [m for m in self_positive if actor_independent(m)]
    predicted = {
        tuple(tuple(alpha if a == i else beta for i in range(n))
              for a in range(n))
        for alpha in (0, 1) for beta in (0, 1)
    }
    # The checker above tests every relabeling directly. This comparison tests
    # the separate orbit characterization, including n=1's missing off-diagonal.
    assert set(admitted) == predicted
    assert len(admitted) == (2 if n == 1 else 4)
    assert len(self_positive) == (1 if n == 1 else 2)
    assert len(independent) == 2
    assert len(positive_independent) == 1
    assert all(x == 1 for row in positive_independent[0] for x in row)
    if n >= 2:
        self_only = tuple(tuple(int(a == i) for i in range(n)) for a in range(n))
        assert self_only in self_positive
        assert not actor_independent(self_only)
    return {
        "centers": n,
        "matrices_enumerated": 1 << (n * n),
        "permutations_per_matrix_available": len(relabelings),
        "jointly_invariant_count": len(admitted),
        "jointly_invariant_matrices": admitted,
        "positive_self_count": len(self_positive),
        "actor_independent_count": len(independent),
        "positive_self_and_actor_independent_count": len(positive_independent),
        "self_only_counterexample_exists": n >= 2,
    }


if __name__ == "__main__":
    source = Path(__file__)
    results = [run_case(n) for n in range(1, 5)]
    report = {
        "date": "2026-10-06",
        "status": "pass",
        "scope": "Exhaustive binary relevance matrices for 1–4 centers; no empirical or universal proof claim.",
        "definitions": {
            "joint_renaming": "r(p(a), p(i)) = r(a, i) for every permutation p",
            "positive_self": "r(a, a) = 1 for every actor a",
            "actor_independence": "r(a, i) = r(b, i) for every a, b, i",
            "interpretation": "These are declared abstract relevance conditions, not definitions of scientific legitimacy or moral truth.",
        },
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "total_matrices_enumerated": sum(r["matrices_enumerated"] for r in results),
        "results": results,
    }
    target = source.with_name("verification.json")
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"],
                      "matrices": report["total_matrices_enumerated"],
                      "invariant_counts": [r["jointly_invariant_count"] for r in results]}, indent=2))
