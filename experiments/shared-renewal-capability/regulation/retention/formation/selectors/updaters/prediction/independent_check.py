#!/usr/bin/env python3
"""Independent formed-prediction audit; no producer transition imports."""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent

def preparation(initial_fuel: int, initial_source: int, adapter_cost: int = 1):
    """Explicit-species reconstruction of the M=2 predecessor preparation.

    State uses free precursor, free A/H, resident A/H, intact/damaged site,
    local fuel, common fuel and source. Productive old reactions have unit rate
    coefficients; nuisance channels are absent, as in the proposed bridge.
    """
    state_count = 0
    edge_count = 0

    def channels(state):
        nonlocal edge_count
        p, a, h, ra, rh, intact, damaged, local, common, source = state
        assert p + a + h + ra + rh == 2
        assert intact + damaged == 1 and ra + rh <= 1 and local in (0, 1)
        out = []

        def add(rate, change, expenditure):
            nonlocal edge_count
            if not rate:
                return
            successor = tuple(v + change.get(i, 0) for i, v in enumerate(state))
            assert min(successor) >= 0
            assert common + local + source - sum(successor[i] for i in (7, 8, 9)) == expenditure
            out.append((successor, Fraction(rate)))
            edge_count += 1

        add(damaged * p * common, {0: -1, 1: 1, 8: -1}, 1)
        add(damaged * p * common, {0: -1, 2: 1, 8: -1}, 1)
        if ra + rh == 0:
            add(a * common, {1: -1, 3: 1, 8: -1}, 1)
            add(h * common, {2: -1, 4: 1, 8: -1}, 1)
        add(ra * damaged * common, {5: 1, 6: -1, 8: -1}, 1)
        add(intact * (1 - local) * source, {7: 1, 9: -1}, 0)
        add(ra * p * local, {0: -1, 1: 1, 7: -1}, 1)
        add(rh * p * local, {0: -1, 2: 1, 7: -1}, 1)
        return out

    @lru_cache(None)
    def recurse(state):
        nonlocal state_count
        state_count += 1
        p, a, h, ra, rh, intact, damaged, local, common, source = state
        enabled = channels(state)
        entrance = bool(intact and local and a + ra and h + rh and common >= adapter_cost)
        if entrance:
            assert not enabled, "Primary adapter entrance suppresses an old channel"
        if entrance or not enabled:
            return {(entrance, state): Fraction(1)}
        total_rate = sum(rate for _, rate in enabled)
        answer = defaultdict(Fraction)
        for successor, rate in enabled:
            for terminal, probability in recurse(successor).items():
                answer[terminal] += rate * probability / total_rate
        assert sum(answer.values()) == 1
        return dict(answer)

    initial = (2, 0, 0, 0, 0, 0, 1, 0, initial_fuel, initial_source)
    distribution = recurse(initial)
    return distribution, {"states": state_count, "positive_channels": edge_count}
