#!/usr/bin/env python3
"""Exact finite checks of the stated conditional decision procedure."""

from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import json


def preorders(n):
    offdiag = [(i, j) for i in range(n) for j in range(n) if i != j]
    relations = []
    for mask in range(1 << len(offdiag)):
        rel = {(i, i) for i in range(n)}
        rel.update(pair for bit, pair in enumerate(offdiag) if mask & (1 << bit))
        if all((i, k) in rel for i, j in rel for jj, k in rel if j == jj):
            relations.append(frozenset(rel))
    return relations


def robust(models, n):
    return frozenset(
        (a, b) for a in range(n) for b in range(n)
        if all((a, b) in m for m in models)
        and any((b, a) not in m for m in models)
    )


def remainder(dominance, n):
    return frozenset(b for b in range(n) if not any((a, b) in dominance for a in range(n)))


def renamed(rel, perm):
    return frozenset((perm[i], perm[j]) for i, j in rel)


def ranked(scores):
    return frozenset((a, b) for a, av in enumerate(scores) for b, bv in enumerate(scores) if av >= bv)


def main():
    n = 3
    relations = preorders(n)
    assert len(relations) == 29
    model_profiles = 0
    witness_checks = 0
    permutation_checks = 0
    for models in product(relations, repeat=3):
        dom = robust(models, n)
        assert all((a, a) not in dom for a in range(n))
        assert all((a, c) in dom for a, b in dom for bb, c in dom if b == bb)
        rem = remainder(dom, n)
        assert rem
        for b in range(n):
            if b not in rem:
                assert any((a, b) in dom for a in rem)
                witness_checks += 1
        # Generators suffice for the full permutation group, but all are checked.
        for perm in permutations(range(n)):
            transformed_models = tuple(renamed(m, perm) for m in models)
            transformed = robust(transformed_models, n)
            assert transformed == renamed(dom, perm)
            assert remainder(transformed, n) == frozenset(perm[a] for a in rem)
            permutation_checks += 1
        model_profiles += 1

    # Independent coordinate-wise Pareto construction for ordinal witnesses.
    vector_checks = 0
    for coords in product(range(3), repeat=6):
        vectors = [coords[2 * i:2 * i + 2] for i in range(3)]
        models = [ranked([v[d] for v in vectors]) for d in range(2)]
        direct = frozenset(
            (a, b) for a in range(3) for b in range(3)
            if all(x >= y for x, y in zip(vectors[a], vectors[b]))
            and any(x > y for x, y in zip(vectors[a], vectors[b]))
        )
        assert robust(models, 3) == direct
        vector_checks += 1

    # Action 0 is protection, action 1 the harmful option.
    pain = ranked((1, 0))
    no_patient = ranked((0, 0))
    competing_burden = ranked((0, 1))
    assert remainder(robust((pain, no_patient), 2), 2) == {0}
    assert remainder(robust((pain, no_patient, competing_burden), 2), 2) == {0, 1}
    assert remainder(robust((no_patient,), 2), 2) == {0, 1}
    assert remainder(robust((no_patient, pain), 2), 2) == {0}
    assert remainder(robust((pain,), 2), 2) == {0}
    assert remainder(robust((pain, competing_burden), 2), 2) == {0, 1}
    # Impartial indifference stays coherent; it does not supply positive standing.
    indifferent = ranked((0, 0, 0))
    assert robust((indifferent,), 3) == set()
    # Paternalism is no longer dominant when agency and welfare disagree.
    comfort = ranked((1, 0))
    agency = ranked((0, 1))
    assert remainder(robust((comfort, agency), 2), 2) == {0, 1}
    # Two serious claims represented separately do not manufacture a sum.
    claimant_a = ranked((1, 0))
    claimant_b = ranked((0, 1))
    assert remainder(robust((claimant_a, claimant_b), 2), 2) == {0, 1}

    lottery_cases = lottery_marginals = lottery_generator_checks = 0
    for claimants in range(2, 8):
        for slots in range(1, claimants):
            subsets = tuple(frozenset(s) for s in combinations(range(claimants), slots))
            weight = Fraction(1, len(subsets))
            distribution = {s: weight for s in subsets}
            assert sum(distribution.values()) == 1
            for i in range(claimants):
                assert sum(p for s, p in distribution.items() if i in s) == Fraction(slots, claimants)
                lottery_marginals += 1
            # Adjacent transpositions generate every permutation.
            for i in range(claimants - 1):
                perm = list(range(claimants))
                perm[i], perm[i + 1] = perm[i + 1], perm[i]
                moved = {frozenset(perm[j] for j in s): p for s, p in distribution.items()}
                assert moved == distribution
                lottery_generator_checks += 1
            for s in subsets:
                # Every deterministic allocation has a renaming that changes it.
                inside = min(s)
                outside = min(set(range(claimants)) - s)
                moved = (s - {inside}) | {outside}
                assert moved != s
            lottery_cases += 1

    # A common policy distribution cannot meet two disjoint singleton requirements.
    indistinguishable_policy_checks = 0
    for numerator in range(101):
        p = Fraction(numerator, 100)
        safe_state_zero = p
        safe_state_one = 1 - p
        assert not (safe_state_zero == 1 and safe_state_one == 1)
        indistinguishable_policy_checks += 1

    result = {
        "status": "passed",
        "three_action_preorders": len(relations),
        "ordered_three_model_profiles": model_profiles,
        "final_dominating_witness_checks": witness_checks,
        "profile_renaming_checks": permutation_checks,
        "independent_ordinal_vector_comparisons": vector_checks,
        "explicit_boundary_assertions": 9,
        "symmetric_lottery_cases": lottery_cases,
        "exact_marginal_checks": lottery_marginals,
        "lottery_generator_invariance_checks": lottery_generator_checks,
        "indistinguishable_policy_grid_checks": indistinguishable_policy_checks,
        "arithmetic": "integer relations and fractions.Fraction",
        "scope": "Finite implementation checks; general claims rest on proofs. No empirical or normative validation."
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
