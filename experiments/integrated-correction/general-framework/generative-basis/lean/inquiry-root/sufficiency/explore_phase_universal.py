#!/usr/bin/env python3
"""Exploration behind PHASE-PERIOD-ASSUMPTIONS.md (not a proof, not a Lean check).

1. For every period 1..MAX_PERIOD (default 16) and every two-valued pattern up to
   rotation, a pattern that does not repeat with step three cannot settle both
   contact values within seven commands from the unsettled start.
2. The local-stretch condition proposed as the finite check: every word u of
   length 14 with (u[4] == u[7] and u[5] != u[8]), or u[j+3] != u[j] for all
   j < 11, or u constant, loses its seven-phase local game (phases 0..6,
   period 14, both inversions) within seven commands for some value. Smaller
   local games (six phases or fewer, any defect offset) have losing failures;
   those counts are printed for comparison.
3. The number of game nodes the Lean `knowsWithin` evaluation of item 2 visits
   (kernel `decide` measured at about 59 s per sixteenth on Lean 4.29.1).

Usage: python3 explore_phase_universal.py [MAX_PERIOD]
"""
from functools import lru_cache
from itertools import product
import sys


def settles(word, period, value, depth, start):
    @lru_cache(None)
    def win(belief, left):
        if all(word[q] == value for q, _ in belief):
            return True
        if left == 0:
            return False
        if win(frozenset(((q + 1) % period, i) for q, i in belief), left - 1):
            return True
        parts = [frozenset(x for x in belief if (word[x[0]] ^ x[1]) == o) for o in (0, 1)]
        return win(parts[0], left - 1) and win(parts[1], left - 1)
    return win(frozenset(start), depth)


def whole(n):
    return [(q, i) for q in range(n) for i in (0, 1)]


def repeats_three(p):
    n = len(p)
    return n % 3 == 0 and all(p[i] == p[(i + 3) % n] for i in range(n))


def periods(max_period):
    for n in range(1, max_period + 1):
        offenders = 0
        for p in product((0, 1), repeat=n):
            if not 0 < sum(p) < n or min(p[k:] + p[:k] for k in range(n)) != p:
                continue
            if repeats_three(p):
                continue
            if all(settles(p, n, v, 7, whole(n)) for v in (0, 1)):
                offenders += 1
        print("period", n, "non-repeating patterns settling both within 7:", offenders)
        assert offenders == 0


def local_condition(u):
    strong = u[4] == u[7] and u[5] != u[8]
    everywhere = all(u[j] != u[j + 3] for j in range(11))
    return strong or everywhere or len(set(u)) == 1


def local_check():
    start = [(s, i) for s in range(7) for i in (0, 1)]
    checked = failures = 0
    for u in product((0, 1), repeat=14):
        if not local_condition(u):
            continue
        checked += 1
        if all(settles(u, 14, v, 7, start) for v in (0, 1)):
            failures += 1
    print("fourteen-value stretches meeting the condition:", checked, "not losing:", failures)
    assert failures == 0
    for phases in range(2, 7):
        worst = None
        for offset in range(1, phases + 1):
            bad = 0
            for u in product((0, 1), repeat=phases + 7):
                if offset + 3 >= len(u) or not (u[offset - 1] == u[offset + 2] and u[offset] != u[offset + 3]):
                    continue
                st = [(s, i) for s in range(phases) for i in (0, 1)]
                if all(settles(u, len(u), v, 7, st) for v in (0, 1)):
                    bad += 1
            worst = bad if worst is None else min(worst, bad)
        print("local game with", phases, "phases: fewest non-losing stretches over offsets:", worst)


if __name__ == "__main__":
    periods(int(sys.argv[1]) if len(sys.argv) > 1 else 16)
    local_check()
