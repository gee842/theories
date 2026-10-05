"""Small independent check of safe Büchi fixed points against strategy/cycle search.

Zero successor mask is an unavailable action, never a vacuous win.
This is a finite implementation check, not a substitute for the proof.
"""
from itertools import product
import json
from pathlib import Path
import random


def pre(game, safe, target):
    return sum(1 << s for s, acts in enumerate(game)
               if safe >> s & 1 and any(d and d & ~target == 0 for d in acts))


def solve(game, safe, progress, guarded=False):
    z = safe
    while True:
        y = 0
        while True:
            nxt = (progress & pre(game, safe, z)) | (pre(game, safe, y) & (~progress if guarded else -1))
            if nxt == y:
                break
            y = nxt
        if y == z:
            return z
        assert y & ~z == 0
        z = y


def brute(game, safe, progress):
    """Enumerate positional choices; independently inspect each induced graph.

An initial state loses iff a reachable vertex is unsafe/deadlocked, or a
reachable directed cycle can stay entirely outside progress.
    """
    n = len(game)
    win = 0
    for choices in product(*(range(len(acts)) for acts in game)):
        succ = [game[s][choices[s]] for s in range(n)]
        for start in range(n):
            if win >> start & 1:
                continue
            reachable, todo = set(), [start]
            while todo:
                s = todo.pop()
                if s in reachable:
                    continue
                reachable.add(s)
                todo.extend(t for t in range(n) if succ[s] >> t & 1)
            if any(not (safe >> s & 1) or succ[s] == 0 for s in reachable):
                continue
            bad = {s for s in reachable if not (progress >> s & 1)}
            color = {}

            def cycle(s):
                color[s] = 1
                for t in bad:
                    if not (succ[s] >> t & 1):
                        continue
                    if color.get(t) == 1 or (color.get(t, 0) == 0 and cycle(t)):
                        return True
                color[s] = 2
                return False

            if not any(color.get(s, 0) == 0 and cycle(s) for s in bad):
                win |= 1 << start
    return win


def rank_certificate(game, safe, progress, win):
    rank, y = {}, 0
    while y != win:
        nxt = (progress & pre(game, safe, win)) | pre(game, safe, y)
        assert nxt != y and nxt & ~win == 0
        r = max(rank.values(), default=0) + 1
        rank.update((s, r) for s in range(len(game)) if nxt >> s & 1 and not (y >> s & 1))
        y = nxt
    strategy = {}
    for s, r in rank.items():
        target = win if r == 1 else sum(1 << t for t, rt in rank.items() if rt < r)
        strategy[s] = next(a for a, d in enumerate(game[s]) if d and d & ~target == 0)
        assert (r == 1) == bool(progress >> s & 1)
    assert max(rank.values(), default=0) <= win.bit_count()
    return strategy, rank


def check(game, safe, progress):
    answer = solve(game, safe, progress)
    assert answer == brute(game, safe, progress), (game, safe, progress, answer)
    assert answer == solve(game, safe, progress, guarded=True)
    rank_certificate(game, safe, progress, answer)


def main():
    exhaustive = 0
    for flat in product(range(4), repeat=4):
        game = [flat[:2], flat[2:]]
        for safe in range(4):
            for progress in range(4):
                if progress & ~safe:
                    continue
                check(game, safe, progress)
                exhaustive += 1
    sink_class = 0
    for flat in product(range(1, 8), repeat=4):
        game = [flat[:2], flat[2:], (4,)]
        for progress in range(4):
            check(game, 3, progress)
            sink_class += 1
    rng = random.Random(20261005)
    sampled = 0
    for n in range(3, 7):
        for _ in range(125):
            game = [tuple(rng.randrange(1 << n) for _ in range(2)) for _ in range(n)]
            safe = rng.randrange(1 << n)
            progress = rng.randrange(1 << n) & safe
            check(game, safe, progress)
            sampled += 1
    examples = {
        "one_hit_then_stasis": ([[2], [4], [4]], 7, 2, 0),
        "recover_and_reset": ([[1, 2], [1, 1]], 3, 2, 3),
        "adversary_can_delay_forever": ([[3], [1]], 3, 2, 0),
        "progress_deadlock": ([[0]], 1, 1, 0),
    }
    for game, safe, progress, expected in examples.values():
        check(game, safe, progress)
        assert solve(game, safe, progress) == expected
    result = {
        "scope": "Finite fully observed nondeterministic games; sure safe Büchi; empty actions unavailable",
        "exhaustive_two_state_two_action_cases": exhaustive,
        "two_state_class_details": {"plants": 256, "safe_target_pairs_per_plant": 9, "state_verdicts": exhaustive * 2, "policies_per_case": 4, "policy_enumerations": exhaustive * 4},
        "exhaustive_two_safe_states_plus_unsafe_sink_cases": sink_class,
        "sink_class_details": {"plants": 2401, "target_sets_per_plant": 4, "state_verdicts": sink_class * 3, "policies_per_case": 4, "policy_enumerations": sink_class * 4},
        "seeded_three_to_six_state_cases": sampled,
        "sampled_details": {"seed": 20261005, "cases_per_size": 125, "state_verdicts": 2250, "policy_enumerations": 15000},
        "named_examples": len(examples),
        "checks": ["fixed point equals exhaustive positional-policy cycle oracle", "guarded and unguarded formulas agree", "rank controller certificate"],
        "failures": 0,
    }
    Path(__file__).with_name("progress-check-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
