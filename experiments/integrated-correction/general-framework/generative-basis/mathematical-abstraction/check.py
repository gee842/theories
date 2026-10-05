#!/usr/bin/env python3
"""Finite checks accompanying MATHEMATICS-STRUCTURAL-RESULTS.md.

Exhaustive finite model checks, not a proof assistant, physical experiment,
or an implementation of an independently acquired learning interface.
Only Python's standard library is used. Run from any working directory.
"""

from collections import deque
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent
COUNTS = {}


def require(condition, name):
    COUNTS[name] = COUNTS.get(name, 0) + 1
    if not condition:
        raise AssertionError(name)


def normalize(items):
    labels = {}
    return tuple(labels.setdefault(item, len(labels)) for item in items)


def refinement(delta, output):
    """Simultaneous refinement; labels are canonical in state order."""
    classes = normalize(output)
    rounds = [classes]
    while True:
        refined = normalize(
            (output[s], tuple(classes[t] for t in delta[s]))
            for s in range(len(delta))
        )
        if refined == classes:
            return classes, rounds
        rounds.append(refined)
        classes = refined


def witness(delta, output, start, other_delta=None, other_output=None):
    """Independent product-graph breadth-first search for a shortest word."""
    if other_delta is None:
        other_delta, other_output = delta, output
    queue = deque([(start, ())])
    seen = {start}
    while queue:
        (s, t), word = queue.popleft()
        if output[s] != other_output[t]:
            return word
        for a in range(len(delta[s])):
            pair = delta[s][a], other_delta[t][a]
            if pair not in seen:
                seen.add(pair)
                queue.append((pair, word + (a,)))
    return None


def words(alphabet, horizon):
    return tuple(
        word
        for length in range(horizon + 1)
        for word in product(range(alphabet), repeat=length)
    )


def response(delta, output, start, word):
    for a in word:
        start = delta[start][a]
    return output[start]


def partitions(n):
    """Every equivalence relation, represented by a restricted-growth word."""
    if n == 0:
        yield ()
        return

    def extend(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for block in range(max(prefix) + 2):
            yield from extend(prefix + [block])

    yield from extend([0])


def canonical_reachable(delta, output, classes):
    """BFS serialization of the reachable behavioral quotient from state 0."""
    representatives = {}
    for s, block in enumerate(classes):
        representatives.setdefault(block, s)
    order = [classes[0]]
    index = {classes[0]: 0}
    serialized = []
    for block in order:
        s = representatives[block]
        destinations = []
        for t in delta[s]:
            target = classes[t]
            if target not in index:
                index[target] = len(order)
                order.append(target)
            destinations.append(index[target])
        serialized.append((output[s], tuple(destinations)))
    return tuple(serialized)


def check_machine(delta, output, all_partitions):
    n = len(delta)
    classes, rounds = refinement(delta, output)
    bound = n - len(set(output))
    require(len(rounds) - 1 <= bound, "refinement_bound")
    alphabet = len(delta[0])
    for k, relation in enumerate(rounds):
        prefixes = words(alphabet, k)
        profiles = [
            tuple(response(delta, output, s, word) for word in prefixes)
            for s in range(n)
        ]
        require(normalize(profiles) == relation, "finite_profile_equals_refinement")
    for s in range(n):
        for t in range(n):
            distinguishing = witness(delta, output, (s, t))
            equivalent = classes[s] == classes[t]
            require(equivalent == (distinguishing is None), "independent_product_graph")
            if distinguishing is not None:
                require(len(distinguishing) <= bound, "shortest_witness_bound")
            if equivalent:
                require(output[s] == output[t], "quotient_output")
                require(
                    all(classes[delta[s][a]] == classes[delta[t][a]] for a in range(alphabet)),
                    "quotient_transition",
                )
    for candidate in all_partitions:
        is_congruence = all(
            candidate[s] != candidate[t]
            or (
                output[s] == output[t]
                and all(candidate[delta[s][a]] == candidate[delta[t][a]] for a in range(alphabet))
            )
            for s in range(n)
            for t in range(n)
        )
        if is_congruence:
            require(
                all(candidate[s] != candidate[t] or classes[s] == classes[t] for s in range(n) for t in range(n)),
                "every_exact_congruence_refines_canonical",
            )
    return classes


def exhaustive_models():
    cases = []
    evidence_to_quotient = {}
    quotient_to_evidence = {}
    # All labeled Boolean-output machines with 1--3 states and two actions,
    # plus all such four-state unary machines. No random sampling.
    for n, alphabet in [(1, 2), (2, 2), (3, 2), (4, 1)]:
        total = 0
        all_partitions = tuple(partitions(n))
        test_words = words(alphabet, 4) if alphabet == 2 else None
        for transitions in product(range(n), repeat=n * alphabet):
            delta = tuple(tuple(transitions[s * alphabet:(s + 1) * alphabet]) for s in range(n))
            for output in product(range(2), repeat=n):
                classes = check_machine(delta, output, all_partitions)
                total += 1
                if alphabet == 2:
                    # N=3: all exact observations through 2N-2 = 4 suffice.
                    evidence = tuple(response(delta, output, 0, word) for word in test_words)
                    quotient = canonical_reachable(delta, output, classes)
                    require(
                        evidence_to_quotient.setdefault(evidence, quotient) == quotient,
                        "bounded_queries_determine_entire_behavior",
                    )
                    require(
                        quotient_to_evidence.setdefault(quotient, evidence) == evidence,
                        "same_behavior_same_bounded_queries",
                    )
        cases.append({"states": n, "actions": alphabet, "outputs": 2, "machines": total})
    return {
        "classes": cases,
        "total_machines": sum(case["machines"] for case in cases),
        "bounded_identification": {
            "maximum_states": 3,
            "maximum_word_length": 4,
            "queried_words": len(words(2, 4)),
            "distinct_initial_behaviors": len(evidence_to_quotient),
        },
    }


def boundary_witnesses():
    sharp = []
    for n in range(2, 13):
        delta = tuple((min(s + 1, n - 1),) for s in range(n))
        output = tuple(int(s == n - 1) for s in range(n))
        classes, rounds = refinement(delta, output)
        word = witness(delta, output, (0, 1))
        require(len(rounds) - 1 == n - 2, "sharp_refinement_family")
        require(word is not None and len(word) == n - 2, "sharp_word_family")
        sharp.append({"states": n, "initial_output_classes": 2, "strict_refinements": n - 2, "shortest_word": len(word)})

    delayed = []
    for horizon in range(13):
        delta = tuple((min(s + 1, horizon + 1),) for s in range(horizon + 2))
        output = tuple(int(s == horizon + 1) for s in range(horizon + 2))
        zero_delta, zero_output = ((0,),), (0,)
        require(
            all(response(delta, output, 0, word) == 0 for word in words(1, horizon)),
            "finite_data_counterexample_agrees",
        )
        word = witness(delta, output, (0, 0), zero_delta, zero_output)
        require(word is not None and len(word) == horizon + 1, "finite_data_counterexample_diverges")
        delayed.append({"observed_horizon": horizon, "delayed_machine_states": horizon + 2, "first_difference": horizon + 1})

    # Two two-state unary machines agree on empty and one-letter words,
    # but not on aa. Both satisfy the same independently given state bound.
    toggler, latch = ((1,), (0,)), ((1,), (1,))
    require(witness(toggler, (0, 1), (0, 0), latch, (0, 1)) == (0, 0), "too_short_bounded_test")

    # Correct present output alone is insufficient for recursive use.
    delta, output = ((1,), (2,), (2,)), (0, 0, 1)
    require(output[0] == output[1], "current_output_merges")
    require(response(delta, output, 0, (0,)) != response(delta, output, 1, (0,)), "current_output_loses_future")

    # The same process with a richer question needs a finer abstraction.
    cycle = ((1,), (2,), (0,))
    coarse, _ = refinement(cycle, (0, 0, 0))
    fine, _ = refinement(cycle, (0, 1, 2))
    require(len(set(coarse)) == 1 and len(set(fine)) == 3, "question_expansion")

    # An epsilon-nearness relation cannot in general be used as a quotient.
    require(abs(0 - 1) <= 1 and abs(1 - 2) <= 1 and not abs(0 - 2) <= 1, "approximation_not_transitive")
    return {"sharp_bounds": sharp, "delayed_disagreements": delayed}


def syntax_checks():
    # All binary terms of height at most three over two variables and a
    # constant. Interpret them in Z/6Z and Z/3Z, and test transport by mod 3.
    # This checks a meaningful finite family, not the general induction proof.
    terms = {("var", "x"), ("var", "y"), ("const",)}
    for _ in range(3):
        previous = tuple(terms)
        terms.update(("add", left, right) for left in previous for right in previous)

    def evaluate(term, modulus, env):
        if term[0] == "var":
            return env[term[1]] % modulus
        if term[0] == "const":
            return 0
        return (evaluate(term[1], modulus, env) + evaluate(term[2], modulus, env)) % modulus

    for term in sorted(terms, key=repr):
        for x, y in product(range(6), repeat=2):
            env = {"x": x, "y": y}
            require(
                evaluate(term, 6, env) % 3 == evaluate(term, 3, env),
                "term_interpretation_commutes_with_homomorphism",
            )
    # Composition permits noncommutative interpretations as well.
    require("a" + "b" != "b" + "a", "syntax_does_not_force_commutativity")
    return {"term_height": 3, "distinct_terms": len(terms), "valuations_per_term": 36}


def main():
    results = {
        "status": "passed",
        "scope": "Exhaustive finite checks and explicit boundary witnesses; hand proofs are separate. No Lean, physical, or empirical validation is claimed.",
        "model_checks": exhaustive_models(),
        "boundaries": boundary_witnesses(),
        "syntax_transport": syntax_checks(),
        "assertion_counts": COUNTS,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    path = ROOT / "verification.json"
    path.write_text(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": results["status"], "machines": results["model_checks"]["total_machines"], "assertions": sum(COUNTS.values()), "report": str(path)}, indent=2))


if __name__ == "__main__":
    main()
