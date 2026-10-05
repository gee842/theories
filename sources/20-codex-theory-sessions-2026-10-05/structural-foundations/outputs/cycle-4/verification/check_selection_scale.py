#!/usr/bin/env python3
"""Actual selection, paid transmission, and exact closed-loop projection.

All arithmetic is rational; all finite kernels are checked state by state.
This script checks examples, not the general mathematical transport proof.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


DEAD = ("D", 0, -1, 0)


@dataclass(frozen=True)
class Model:
    unit: int = 1
    reserve_code: int = 0
    consume_code: int = 1
    tags: int = 1
    mutation: F = F(0)

    def states(self):
        return [DEAD] + [(phase, self.unit*b, rule, tag)
                         for phase, b, rule, tag in product(
                             ("O", "S", "T"), range(3),
                             (self.reserve_code, self.consume_code), range(self.tags))]

    def initial(self, reserve=True):
        return ("O", 2*self.unit,
                self.reserve_code if reserve else self.consume_code, 0)

    def kernel(self, state):
        if state == DEAD:
            return {(("dead", 0, 0, 0), DEAD): F(1)}
        phase, cash, rule, tag = state
        tag = (tag+1) % self.tags
        if phase == "O":
            consume = rule == self.consume_code
            fee = self.unit if consume else 0
            event = ("consume" if consume else "reserve", fee, 0, 2 if consume else 1)
            if cash < fee:
                return {(("blocked_operation", 0, 0, 0), DEAD): F(1)}
            return {(event, ("S", cash-fee, rule, tag)): F(1)}
        if cash < self.unit:
            return {(("blocked_"+phase, 0, 0, 0), DEAD): F(1)}
        if phase == "S":
            return {(("service", self.unit, 0, 0),
                     ("T", cash-self.unit, rule, tag)): F(1)}
        assert phase == "T"
        # Transmission fee is prepaid. Only afterward does the external
        # receipt replenish the carried reserve, capped at two units.
        cash = min(2*self.unit, cash-self.unit+2*self.unit)
        event = ("transmit", self.unit, 2*self.unit, 0)
        if rule == self.consume_code:
            return {(event, ("O", cash, rule, tag)): F(1)}
        result = {}
        for next_rule, probability in ((self.reserve_code, 1-self.mutation),
                                       (self.consume_code, self.mutation)):
            if probability:
                result[(event, ("O", cash, next_rule, tag))] = probability
        return result


def map_state(state, source, target):
    if state == DEAD:
        return DEAD
    phase, cash, rule, tag = state
    assert cash % source.unit == 0 and source.tags % target.tags == 0
    target_rule = (target.reserve_code if rule == source.reserve_code
                   else target.consume_code)
    return phase, cash//source.unit*target.unit, target_rule, tag % target.tags


def map_event(event, source, target):
    action, fee, receipt, output = event
    assert fee % source.unit == 0 and receipt % source.unit == 0
    return action, fee//source.unit*target.unit, receipt//source.unit*target.unit, output


def projected_kernel(state, source, target):
    out = defaultdict(F)
    for (event, nxt), probability in source.kernel(state).items():
        out[(map_event(event, source, target), map_state(nxt, source, target))] += probability
    return dict(out)


def check_intertwining(source, target):
    checked = 0
    for state in source.states():
        row = source.kernel(state)
        assert sum(row.values()) == 1 and all(p > 0 for p in row.values())
        assert projected_kernel(state, source, target) == target.kernel(map_state(state, source, target))
        checked += 1
    return checked


def advance_distribution(model, distribution):
    out = defaultdict(F)
    for state, mass in distribution.items():
        for (_, nxt), probability in model.kernel(state).items():
            out[nxt] += mass*probability
    return dict(out)


def survival(model, cycles, reserve=True):
    distribution = {model.initial(reserve): F(1)}
    for _ in range(3*cycles):
        distribution = advance_distribution(model, distribution)
    return 1-distribution.get(DEAD, F(0))


def trace_law(model, steps, target):
    law = {((), model.initial()): F(1)}
    for _ in range(steps):
        out = defaultdict(F)
        for (trace, state), mass in law.items():
            for (event, nxt), probability in model.kernel(state).items():
                emission = (map_event(event, model, target), map_state(nxt, model, target))
                out[(trace+(emission,), nxt)] += mass*probability
        law = dict(out)
    result = defaultdict(F)
    for (trace, _), probability in law.items():
        result[trace] += probability
    return dict(result)


def physical_capacity():
    """Greatest safe set of the shared controlled cash/phase plant."""
    states = [(phase, cash) for phase, cash in product(("O", "S", "T"), range(3))]
    def choices(state):
        phase, cash = state
        if phase == "O":
            return [("S", cash)] + ([("S", cash-1)] if cash else [])
        if cash < 1:
            return []
        if phase == "S":
            return [("T", cash-1)]
        return [("O", min(2, cash-1+2))]
    winning = set(states)
    while True:
        updated = {s for s in winning if any(nxt in winning for nxt in choices(s))}
        if updated == winning:
            return sorted(winning)
        winning = updated


def plain(value):
    if isinstance(value, F):
        return {"exact": str(value), "decimal": float(value)}
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    return value


def main():
    winning = physical_capacity()
    assert winning == [("O", 2), ("S", 2), ("T", 1), ("T", 2)]
    stable = Model()
    assert survival(stable, 30) == 1
    assert survival(stable, 1, reserve=False) == 0
    corrupt = Model(mutation=F(1))
    assert survival(corrupt, 1) == 1 and survival(corrupt, 2) == 0
    # Same initial state and selection, different update/transmission law.
    assert stable.kernel(stable.initial()) == corrupt.kernel(corrupt.initial())
    transmission = ("T", 1, stable.reserve_code, 0)
    assert stable.kernel(transmission) != corrupt.kernel(transmission)

    kernel_rows = path_laws = composition_rows = 0
    for mutation in (F(0), F(1, 4), F(1, 2), F(1)):
        high = Model(mutation=mutation)
        middle = Model(2, 1, 0, 2, mutation)
        low = Model(6, 7, 9, 6, mutation)
        kernel_rows += check_intertwining(middle, high)
        kernel_rows += check_intertwining(low, middle)
        kernel_rows += check_intertwining(low, high)
        for state in low.states():
            direct = map_state(state, low, high)
            composed = map_state(map_state(state, low, middle), middle, high)
            assert direct == composed
            composition_rows += 1
        for steps in range(13):
            expected = trace_law(high, steps, high)
            assert trace_law(middle, steps, high) == expected
            assert trace_law(low, steps, high) == expected
            path_laws += 2

    survival_rows = []
    for mutation, cycles in product((F(0), F(1, 4), F(1, 2), F(1)), range(1, 21)):
        actual = survival(Model(mutation=mutation), cycles)
        expected = (1-mutation)**(cycles-1)
        assert actual == expected
        survival_rows.append({"mutation": mutation, "cycles": cycles, "survival": actual})

    # Same positive support at two mutation rates does not fix probabilities.
    p, q = Model(mutation=F(1, 4)), Model(mutation=F(1, 2))
    assert all(set(p.kernel(s)) == set(q.kernel(s)) for s in p.states())
    assert survival(p, 4) == F(27, 64) and survival(q, 4) == F(1, 8)
    assert projected_kernel(transmission, q, p) != p.kernel(transmission)

    # Uniform local total-variation error bounds finite-horizon error.
    # The worst row difference here is exactly |1/4 - 1/2| = 1/4.
    epsilon = F(1, 4)
    tv_checks = 0
    for steps in range(13):
        lp, lq = trace_law(p, steps, p), trace_law(q, steps, p)
        tv = sum(abs(lp.get(t, F(0))-lq.get(t, F(0))) for t in lp.keys() | lq.keys())/2
        assert tv <= min(F(1), steps*epsilon)
        tv_checks += 1

    # Matching one-time marginals is weaker than matching temporal joint law.
    persistent_coin = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    fresh_coins = {pair: F(1, 4) for pair in product((0, 1), repeat=2)}
    for index in (0, 1):
        for bit in (0, 1):
            assert sum(v for pair, v in persistent_coin.items() if pair[index] == bit) == F(1, 2)
            assert sum(v for pair, v in fresh_coins.items() if pair[index] == bit) == F(1, 2)
    assert sum(v for (a,b),v in persistent_coin.items() if a==b) == 1
    assert sum(v for (a,b),v in fresh_coins.items() if a==b) == F(1, 2)

    report = {"status": "all assertions passed", "safe_physical_states": winning,
              "reserve_selector_survival_30_cycles": survival(stable, 30),
              "consume_selector_survival_one_cycle": survival(stable, 1, reserve=False),
              "corrupt_transmission_survival_two_cycles": survival(corrupt, 2),
              "exact_kernel_rows_checked": kernel_rows,
              "composed_state_maps_checked": composition_rows,
              "finite_path_law_equalities_checked": path_laws,
              "survival_formula_checks": len(survival_rows),
              "finite_horizon_tv_checks": tv_checks,
              "same_support_different_laws": {"mu_quarter_survival_four_cycles": F(27,64),
                                                "mu_half_survival_four_cycles": F(1,8)},
              "survival_rows": survival_rows,
              "limits": ["Supplied finite rules, not an optimizer or adoption model",
                         "Renewal receipt is external and arrives after transmission payment",
                         "Kernel and trace tests are finite checks, not a machine proof of the general theorem",
                         "Physical plant capacity is relative to the declared solvency test",
                         "No empirical or normative conclusion"]}
    path = Path(__file__).with_name("selection-scale-results.json")
    path.write_text(json.dumps(plain(report), indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status", "exact_kernel_rows_checked",
                     "composed_state_maps_checked", "finite_path_law_equalities_checked",
                     "survival_formula_checks", "finite_horizon_tv_checks")}, indent=2))


if __name__ == "__main__":
    main()
