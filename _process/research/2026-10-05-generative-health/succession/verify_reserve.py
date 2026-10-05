"""Exact finite checks of the paid-succession reserve calculation.

The independent strategy check materializes full contingent policy trees,
rolls every task word through every tree, and computes the largest prefix
draw. It does not use the reserve recursion to score those trees.
No finite check proves the infinite-horizon theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


@dataclass(frozen=True)
class Edge:
    peak: int | Fraction
    net: int | Fraction
    dest: str
    name: str


# Every completed episode receives three work units AFTER its billed work.
# A policy sees the present task before selecting one of these transitions.
GRAPH = {
    "solution": (
        (Edge(2, -1, "solution", "replay"), Edge(6, 3, "kit", "build")),
        (Edge(5, 2, "solution", "scratch"), Edge(7, 4, "kit", "build")),
    ),
    "kit": (
        (Edge(2, -1, "kit", "keep"), Edge(1, -2, "solution", "discard")),
        (Edge(3, 0, "kit", "keep"), Edge(2, -1, "solution", "discard")),
    ),
    "partial": (
        (Edge(2, -1, "partial", "keep"), Edge(4, 1, "kit", "upgrade")),
        (Edge(4, 1, "partial", "keep"), Edge(5, 2, "kit", "upgrade")),
    ),
}


def reserve_layers(graph, horizon):
    layers = [{z: 0 for z in graph}]
    for _ in range(horizon):
        old = layers[-1]
        layers.append({
            z: max(min(max(0, a.peak, a.net + old[a.dest])
                       for a in choices) for choices in tasks)
            for z, tasks in graph.items()
        })
    return layers


def exhaustive_check(graph, maximum_horizon):
    @lru_cache(None)
    def policy_trees(state, horizon):
        if horizon == 0:
            return (None,)
        branches = []
        for choices in graph[state]:
            branches.append(tuple((edge, subtree)
                                  for edge in choices
                                  for subtree in policy_trees(edge.dest, horizon - 1)))
        return tuple(product(*branches))

    def score_tree(tree, task_word):
        cumulative_net = 0
        largest_draw = 0
        for task in task_word:
            edge, tree = tree[task]
            largest_draw = max(largest_draw, cumulative_net + edge.peak)
            cumulative_net += edge.net
        # peak >= max(0, net) means each transition's terminal balance is covered.
        assert largest_draw >= cumulative_net
        return largest_draw

    layers = reserve_layers(graph, maximum_horizon)
    rows = []
    total_trees = 0
    total_rollouts = 0
    for horizon in range(1, maximum_horizon + 1):
        words = tuple(product((0, 1), repeat=horizon))
        for state in graph:
            trees = policy_trees(state, horizon)
            exhaustive = min(max(score_tree(tree, word) for word in words)
                             for tree in trees)
            expected = layers[horizon][state]
            assert exhaustive == expected, (state, horizon, exhaustive, expected)
            rows.append({"state": state, "horizon": horizon,
                         "reserve": str(expected), "policies": len(trees),
                         "task_words_per_policy": len(words)})
            total_trees += len(trees)
            total_rollouts += len(trees) * len(words)
    return {"comparisons": len(rows), "policy_trees_scored": total_trees,
            "task_rollouts": total_rollouts, "results": rows}


def prefix_draw(cost_word, receipt, timing):
    cumulative_draw = 0
    required = 0
    for cost in cost_word:
        if timing == "before":
            cumulative_draw -= receipt
        cumulative_draw += cost
        required = max(required, cumulative_draw)
        if timing == "after":
            cumulative_draw -= receipt
    return required


def verify_stationary():
    comparisons = 0
    task_words = 0
    for c0, c1, receipt, horizon in product(range(1, 6), range(1, 6),
                                           range(7), range(1, 7)):
        cmax = max(c0, c1)
        words = tuple(product((c0, c1), repeat=horizon))
        for timing in ("before", "after"):
            brute = max(prefix_draw(word, receipt, timing) for word in words)
            expected = (horizon * max(cmax - receipt, 0) if timing == "before"
                        else cmax + (horizon - 1) * max(cmax - receipt, 0))
            assert brute == expected, (c0, c1, receipt, horizon, timing)
            comparisons += 1
            task_words += len(words)
    return {"comparisons": comparisons, "task_words_scored": task_words,
            "costs_each_task": "integers 1 through 5",
            "receipt": "integers 0 through 6", "horizons": "1 through 6",
            "timings": ["before episode cost", "after episode cost"]}


def verify_equal_output():
    # Both modes deliver the same correct current answer and charge five units
    # for their first episode. Their delivered productive interfaces differ.
    graph = {
        "rich_start": ((Edge(5, 2, "rich_repeat", "correct"),),) * 2,
        "rich_repeat": ((Edge(5, 2, "rich_repeat", "correct"),),) * 2,
        "generative_start": ((Edge(5, 2, "generative_repeat", "correct"),),) * 2,
        "generative_repeat": ((Edge(2, -1, "generative_repeat", "correct"),),
                              (Edge(3, 0, "generative_repeat", "correct"),)),
    }
    layers = reserve_layers(graph, 12)
    for horizon in range(1, 13):
        assert layers[horizon]["rich_start"] == 5 + 2 * (horizon - 1)
        assert layers[horizon]["generative_start"] == 5
    # The nontrivial finite certificate is checked on every task edge.
    certificate = {"generative_start": 5, "generative_repeat": 3}
    for state, potential in certificate.items():
        for choices in graph[state]:
            assert any(edge.peak <= potential and
                       edge.net + certificate[edge.dest] <= potential
                       for edge in choices)
    opening = 9
    finite_completed = 1 + (opening - 5) // (5 - 3)
    assert finite_completed == 3
    return {"same_current_answer": True, "same_initial_balance": opening,
            "same_first_episode_cost": 5, "same_first_horizon_reserve": 5,
            "external_receipt_after_each_completed_episode": 3,
            "rich_reserve_by_horizon": [layers[n]["rich_start"] for n in range(1, 13)],
            "generative_reserve_by_horizon": [layers[n]["generative_start"] for n in range(1, 13)],
            "rich_completed_episodes_before_worst_case_failure": finite_completed,
            "generative_inductive_certificate": certificate,
            "scope": "The infinite claim uses the checked inductive certificate and theorem; twelve horizons alone do not establish it."}


def verify_task_timing():
    # Action matching the current task costs one; the other costs four.
    # Both receive one afterward. Hidden current tasks cannot guide the action.
    observed = hidden = 0
    rows = []
    for n in range(1, 7):
        observed = max(min(max(1 if a == q else 4,
                               (0 if a == q else 3) + observed)
                           for a in (0, 1)) for q in (0, 1))
        hidden = min(max(max(1 if a == q else 4,
                             (0 if a == q else 3) + hidden)
                         for q in (0, 1)) for a in (0, 1))
        assert observed == 1
        assert hidden == 4 + 3 * (n - 1)
        rows.append({"horizon": n, "announced_before_action": observed,
                     "not_announced_before_action": hidden})
    return rows


def main():
    integer = exhaustive_check(GRAPH, 3)
    half = {z: tuple(tuple(Edge(Fraction(a.peak, 2), Fraction(a.net, 2),
                                a.dest, a.name) for a in choices) for choices in tasks)
            for z, tasks in GRAPH.items()}
    fractional = exhaustive_check(half, 2)
    result = {"status": "all checks passed", "arithmetic": "integers and exact Fraction rationals",
              "contingent_policy_enumeration": integer,
              "fractional_cost_enumeration": fractional,
              "stationary_formula": verify_stationary(),
              "equal_current_output_witness": verify_equal_output(),
              "announcement_order": verify_task_timing(),
              "experiment_timing": "constructive-succession/model.py credits flow before service, target, search, validation, installation, and handoff; use the pre-credit state convention or shift the state to immediately after its inflow.",
              "limitations": "Finite exact toy checks corroborate the formulas. They do not show indefinite success of the finite NAND experiment, empirical validity, or unrestricted generativity."}
    target = Path(__file__).with_name("RESERVE-VERIFICATION.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"],
                      "integer_policy_trees": integer["policy_trees_scored"],
                      "integer_task_rollouts": integer["task_rollouts"],
                      "stationary_comparisons": result["stationary_formula"]["comparisons"],
                      "result": str(target)}, indent=2))


if __name__ == "__main__":
    main()
