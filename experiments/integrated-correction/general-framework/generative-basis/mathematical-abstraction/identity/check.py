"""Finite mathematical verification; run with PYTHONDONTWRITEBYTECODE=1."""
from collections import deque
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def refinement(n, delta, actions, observation):
    relation = {(s, t) for s in range(n) for t in range(n)
                if observation[s] == observation[t]}
    while True:
        revised = set()
        for s, t in relation:
            good = True
            for a in actions:
                x, y = delta[s][a], delta[t][a]
                if (x == -1) != (y == -1):
                    good = False
                    break
                if x != -1 and (x, y) not in relation:
                    good = False
                    break
            if good:
                revised.add((s, t))
        if revised == relation:
            return revised
        relation = revised


def pair_search(n, delta, actions, observation):
    equivalent = set()
    for s in range(n):
        for t in range(n):
            todo, seen, distinguishable = deque([(s, t)]), set(), False
            while todo and not distinguishable:
                x, y = todo.popleft()
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                if observation[x] != observation[y]:
                    distinguishable = True
                    break
                for a in actions:
                    u, v = delta[x][a], delta[y][a]
                    if (u == -1) != (v == -1):
                        distinguishable = True
                        break
                    if u != -1:
                        todo.append((u, v))
            if not distinguishable:
                equivalent.add((s, t))
    return equivalent


def partitions(n):
    """Restricted growth strings enumerate every set partition once."""
    def extend(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for label in range(max(prefix) + 2):
            yield from extend(prefix + [label])
    yield from extend([0])


def is_congruence(n, delta, actions, observation, partition):
    for s in range(n):
        for t in range(n):
            if partition[s] != partition[t]:
                continue
            if observation[s] != observation[t]:
                return False
            for a in actions:
                x, y = delta[s][a], delta[t][a]
                if (x == -1) != (y == -1):
                    return False
                if x != -1 and partition[x] != partition[y]:
                    return False
    return True


def class_labels(n, relation):
    return tuple(min(t for t in range(n) if (s, t) in relation)
                 for s in range(n))


def verify_factor(n, delta, common_actions, old, new):
    assert new <= old
    coarse, fine = class_labels(n, old), class_labels(n, new)
    factor = {}
    for s in range(n):
        if fine[s] in factor:
            assert factor[fine[s]] == coarse[s]
        factor[fine[s]] = coarse[s]
    assert set(factor.values()) == set(coarse)
    for s in range(n):
        for a in common_actions:
            x = delta[s][a]
            if x != -1:
                assert factor[fine[x]] == coarse[x]


def main():
    counts, strict_actions, strict_questions = {}, 0, 0
    new_action_failure = None
    for n in range(1, 4):
        count = 0
        all_partitions = tuple(partitions(n))
        for entries in product(range(-1, n), repeat=2*n):
            delta = tuple(tuple(entries[2*s:2*s+2]) for s in range(n))
            for output in product((0, 1), repeat=n):
                richer = tuple((output[s], s % 2) for s in range(n))
                interfaces = [((0,), output), ((0, 1), output),
                              ((0, 1), richer)]
                relations = []
                for actions, observation in interfaces:
                    eq = refinement(n, delta, actions, observation)
                    assert eq == pair_search(n, delta, actions, observation)
                    labels = class_labels(n, eq)
                    assert is_congruence(n, delta, actions, observation, labels)
                    for partition in all_partitions:
                        if is_congruence(n, delta, actions, observation, partition):
                            assert all((s, t) in eq for s in range(n)
                                       for t in range(n)
                                       if partition[s] == partition[t])
                    relations.append(eq)
                old, middle, fine = relations
                verify_factor(n, delta, (0,), old, middle)
                verify_factor(n, delta, (0, 1), middle, fine)
                strict_actions += middle != old
                strict_questions += fine != middle
                if new_action_failure is None and not is_congruence(
                        n, delta, (0, 1), output, class_labels(n, old)):
                    new_action_failure = {
                        "states": n, "delta": delta, "output": output,
                        "old_classes": class_labels(n, old),
                        "expanded_classes": class_labels(n, middle),
                        "undefined_entry": -1,
                    }
                count += 1
        counts[str(n)] = count
    assert counts == {"1": 8, "2": 324, "3": 32768}

    # Total DFA: empty prefix, a, ab, and the dead state.
    language_delta = ((1, 3), (3, 2), (3, 3), (3, 3))
    language_output = (0, 0, 1, 0)
    def endpoint(word):
        s = 0
        for a in word:
            s = language_delta[s]["ab".index(a)]
        return s
    assert endpoint("b") == endpoint("aa") == 3
    assert language_output[endpoint("ab")] == 1
    assert language_output[endpoint("aaa")] == 0

    # Finite illustration only; the general empty-intersection proof is in prose.
    for k in range(13):
        for n in range(26):
            assert min(n + 1, k) == min(min(n, k) + 1, k)
        for j in range(k + 1):
            assert min(k, j) == j
    for cutoff in range(13):
        assert all(min(cutoff, k) == k for k in range(cutoff + 1))
        assert min(cutoff, cutoff + 1) != cutoff + 1

    here = Path(__file__).resolve().parent
    result = {
        "scope": "finite mathematical checks, not empirical identification",
        "processes_by_state_count": counts,
        "total_processes": sum(counts.values()),
        "interface_algorithm_comparisons": 3 * sum(counts.values()),
        "strict_action_refinements": strict_actions,
        "strict_question_refinements": strict_questions,
        "coarsest_congruence_exhaustively_checked": True,
        "new_action_on_old_quotient_counterexample": new_action_failure,
        "history_operation_counterexample": {
            "language": "exactly ab", "history_pair": ["b", "aa"],
            "equal_reached_dead_state": 3,
            "prefix": "a", "prefixed_outputs": [1, 0]},
        "completion_illustration": {
            "stages": [0, 12], "sampled_states": [0, 25],
            "universal_nonrealization": "hand proof, not finite execution"},
        "sha256": {name: sha256((here / name).read_bytes()).hexdigest()
                   for name in ("check.py", "PROTOCOL.md")},
    }
    (here / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "total_processes", "interface_algorithm_comparisons",
        "strict_action_refinements", "strict_question_refinements")}))


if __name__ == "__main__":
    main()
