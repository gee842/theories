"""Independent finite safety-game solver and concrete policy-tree oracle.

No imports from the root solver.  The fixed-point solver uses belief bitsets;
the oracle searches observation-consistent policies over explicit state paths.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json


def members(mask, n):
    return tuple(x for x in range(n) if mask & (1 << x))


def safety_solve(transitions, observations, safe):
    n = len(observations)
    actions = range(len(transitions[0]))
    safe_mask = sum(1 << x for x in safe)
    obs_masks = {}
    for x, y in enumerate(observations):
        obs_masks[y] = obs_masks.get(y, 0) | (1 << x)
    universe = {
        b for b in range(1, 1 << n)
        if b & ~safe_mask == 0 and len({observations[x] for x in members(b, n)}) == 1
    }

    def successors(b, action):
        post = 0
        for x in members(b, n):
            for xp in transitions[x][action]:
                post |= 1 << xp
        return tuple((y, post & block) for y, block in sorted(obs_masks.items()) if post & block)

    successor_table = {(b, a): successors(b, a) for b in universe for a in actions}
    layers = [set(universe)]
    rank = {}
    while True:
        current = layers[-1]
        nxt = {
            b for b in universe
            if any(all(bp in current for _, bp in successor_table[b, a]) for a in actions)
        }
        assert nxt <= current
        for b in current - nxt:
            rank[b] = len(layers)
        layers.append(nxt)
        if nxt == current:
            break
    winning = layers[-1]
    policy = {
        b: next(a for a in actions if all(bp in winning for _, bp in successor_table[b, a]))
        for b in winning
    }
    return universe, layers, rank, policy, successors


def concrete_policy_tree_oracle(transitions, observations, safe, initial, horizon):
    """Exhaust all action assignments to currently reached observation histories.

    It retains concrete state paths rather than invoking a belief predecessor,
    and assigns one action per observation-and-own-action history at each depth.
    """
    actions = range(len(transitions[0]))
    initial_paths = tuple(((x,), ()) for x in initial)

    def search(paths, remaining):
        if any(xs[-1] not in safe for xs, _ in paths):
            return False
        if remaining == 0:
            return True
        keys = tuple(sorted({(tuple(observations[x] for x in xs), acts) for xs, acts in paths}))
        for choices in product(actions, repeat=len(keys)):
            choice = dict(zip(keys, choices))
            next_paths = []
            bad = False
            for xs, acts in paths:
                key = (tuple(observations[x] for x in xs), acts)
                action = choice[key]
                for xp in transitions[xs[-1]][action]:
                    if xp not in safe:
                        bad = True
                        break
                    next_paths.append((xs + (xp,), acts + (action,)))
                if bad:
                    break
            if not bad and search(tuple(next_paths), remaining - 1):
                return True
        return False

    return search(initial_paths, horizon)


def certify(transitions, observations, safe, solution):
    universe, layers, rank, policy, successors = solution
    winning = layers[-1]
    n = len(observations)
    # Check the extracted controller on concrete plant/controller products.
    pairs = {(x, b) for b in winning for x in members(b, n)}
    edges = 0
    for x, b in pairs:
        assert x in safe
        action = policy[b]
        by_observation = dict(successors(b, action))
        for xp in transitions[x][action]:
            bp = by_observation[observations[xp]]
            assert (xp, bp) in pairs
            edges += 1
    # Every rejected action has a strictly lower-rank observation successor.
    rank_witnesses = 0
    for b, r in rank.items():
        for action in range(len(transitions[0])):
            candidates = successors(b, action)
            assert any(bp not in universe or rank.get(bp, float("inf")) < r for _, bp in candidates)
            rank_witnesses += 1
    return len(pairs), edges, rank_witnesses


def serialize_example(name, transitions, observations, safe, initials):
    solution = safety_solve(transitions, observations, safe)
    universe, layers, rank, policy, successors = solution
    certify(transitions, observations, safe, solution)
    n = len(observations)
    show = lambda b: list(members(b, n))
    return {
        "name": name, "transitions": transitions, "observations": observations,
        "safe_states": sorted(safe), "winning_beliefs": [show(b) for b in sorted(layers[-1])],
        "controller": [{"belief": show(b), "action": a} for b, a in sorted(policy.items())],
        "losing_ranks": [{"belief": show(b), "rank": r} for b, r in sorted(rank.items())],
        "initials": [{"belief": list(b), "winning": sum(1 << x for x in b) in layers[-1]} for b in initials],
        "strict_fixed_point_iterations": sum(layers[j] != layers[j + 1] for j in range(len(layers) - 1)),
    }


def main():
    nonempty = tuple(tuple(x for x in range(3) if mask & (1 << x)) for mask in range(1, 8))
    partitions = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 1, 2))
    safe = {0, 1}
    games = queries = product_edges = rank_edges = 0
    winning_initials = 0
    max_rank = 0
    for entries in product(nonempty, repeat=4):
        transitions = ((entries[0], entries[1]), (entries[2], entries[3]), ((2,), (2,)))
        for observations in partitions:
            games += 1
            solution = safety_solve(transitions, observations, safe)
            universe, layers, ranks, policy, _ = solution
            _, checked_edges, checked_ranks = certify(transitions, observations, safe, solution)
            product_edges += checked_edges
            rank_edges += checked_ranks
            max_rank = max(max_rank, max(ranks.values(), default=0))
            for b in universe:
                winning_initials += int(b in layers[-1])
                for horizon in range(len(universe) + 1):
                    oracle = concrete_policy_tree_oracle(
                        transitions, observations, safe, members(b, 3), horizon)
                    expected = b in layers[min(horizon, len(layers) - 1)]
                    assert oracle == expected, (transitions, observations, b, horizon)
                    queries += 1
                # At most |universe| strict deletions reach the fixed point.
                assert (b in layers[min(len(universe), len(layers) - 1)]) == (b in layers[-1])

    alternating = (((1,), (2,)), ((2,), (0,)), ((2,), (2,)))
    examples = [
        serialize_example("hidden alternating phase requires two-state memory", alternating, (0, 0, 1), safe, ((0,), (1,), (0, 1))),
        serialize_example("full observation resolves the hidden-phase conflict", alternating, (0, 1, 2), safe, ((0,), (1,))),
        serialize_example("safe stuttering does not imply progress", (((0,),),), (0,), {0}, ((0,),)),
        serialize_example("hidden-phase recurrence can occur without target-certain belief", (((1,),), ((0,),)), (0, 0), {0, 1}, ((0, 1),)),
        serialize_example("countdown loses at a finite elimination rank", (((1,),), ((2,),), ((2,),)), (0, 0, 0), safe, ((0,),)),
    ]
    # In the alternating example, each observation-only constant action fails.
    for action in (0, 1):
        x = 0
        for _ in range(2):
            x = alternating[x][action][0]
        assert x == 2
    assert examples[0]["initials"][0]["winning"]
    assert not examples[0]["initials"][2]["winning"]
    assert examples[4]["losing_ranks"][0] == {"belief": [0], "rank": 2}

    results = {
        "method": "Belief greatest fixed point cross-checked against exhaustive concrete observation-policy trees; extracted controller and losing-rank certificates checked independently.",
        "exhaustive_games": games,
        "transition_tables": 7 ** 4,
        "observation_partitions": len(partitions),
        "finite_horizon_policy_tree_queries": queries,
        "winning_initial_beliefs": winning_initials,
        "checked_controller_product_edges": product_edges,
        "checked_losing_rank_action_obligations": rank_edges,
        "largest_observed_losing_rank": max_rank,
        "examples": examples,
        "scope": "All two-safe-state plus absorbing-unsafe-state, two-action nondeterministic transition tables, all observation partitions; examples and exact finite verification, not empirical evidence."
    }
    out = Path(__file__).with_name("formal_continuation_checks.json")
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in results.items() if k != "examples"}, indent=2))


if __name__ == "__main__":
    main()
