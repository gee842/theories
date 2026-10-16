"""Exact finite-horizon checks for observability-and-correction.md.

Run with Python 3 (standard library only):
    python3 verify_observability.py

Writes observability-checks.json alongside this script. These are checks of
explicit illustrative models, not empirical validation of a domain mapping.
"""

from dataclasses import dataclass, replace
from functools import lru_cache
import json
from pathlib import Path


def information_safety_solver(actions, successors, observation, protected):
    """Backward recursion on full-history information supports.

    A successor relation can return several states per state/action. Every
    possible next observation must permit safety for the remaining horizon.
    Finite-state examples below use deterministic individual transitions.
    """
    def partition(states):
        groups = {}
        for state in states:
            groups.setdefault(observation(state), set()).add(state)
        return tuple(frozenset(group) for group in groups.values())

    def update(support, action):
        possible = set()
        for state in support:
            possible.update(successors(state, action))
        return partition(possible)

    @lru_cache(None)
    def winning(support, remaining):
        if not support or not all(protected(state) for state in support):
            return False
        if remaining == 0:
            return True
        return any(
            all(winning(next_support, remaining - 1)
                for next_support in update(support, action))
            for action in actions
        )

    def safe_actions(support, remaining):
        if remaining < 1 or not all(protected(state) for state in support):
            return frozenset()
        return frozenset(
            action for action in actions
            if all(winning(next_support, remaining - 1)
                   for next_support in update(support, action))
        )

    return winning, safe_actions, update, partition


@dataclass(frozen=True)
class RepairState:
    fault: int
    time: int = 0
    recipe: int = 0
    completion_time: int = -1
    status: str = "running"


class RepairModel:
    """Unit reserve loss; irreversible recipe; delayed perfect diagnosis.

    Actions -1 and +1 start a recipe, and action 0 waits. A second initiation
    while a recipe is pending is invalid and causes absorbing failure. A
    correct completion exactly when reserve reaches zero is accepted; a
    completion after that deadline is not. Diagnosis continues to update
    observations during a pending repair but cannot reverse its initiation.
    """
    actions = (-1, 0, 1)

    def __init__(self, reveal=8, reserve=10, lag=3):
        if min(reveal, reserve) < 0 or lag < 1:
            raise ValueError("This check uses nonnegative integer times and lag >= 1")
        self.reveal, self.initial_reserve, self.lag = reveal, reserve, lag

    def observation(self, state):
        visible_fault = state.fault if state.time >= self.reveal else None
        return (state.time, state.recipe, state.completion_time,
                state.status, visible_fault)

    @staticmethod
    def protected(state):
        return state.status != "failed"

    def reserve(self, state):
        loss_time = (state.completion_time if state.status == "safe"
                     else state.time)
        return self.initial_reserve - loss_time

    def step(self, state, action):
        if state.status in ("safe", "failed"):
            return replace(state, time=state.time + 1)
        recipe, completion = state.recipe, state.completion_time
        if recipe == 0 and action in (-1, 1):
            recipe, completion = action, state.time + self.lag
        elif recipe != 0 and action != 0:
            return replace(state, time=state.time + 1, status="failed")
        time = state.time + 1
        status = "running"
        if time > self.initial_reserve:
            status = "failed"
        elif completion == time:
            status = "safe" if recipe == state.fault else "failed"
        return RepairState(state.fault, time, recipe, completion, status)

    def successors(self, state, action):
        return frozenset((self.step(state, action),))

    def solver(self):
        return information_safety_solver(
            self.actions, self.successors, self.observation, self.protected)

    def guaranteed_safe(self, horizon=12):
        winning, _, _, partition = self.solver()
        starts = (RepairState(-1), RepairState(1))
        answer = all(winning(group, horizon) for group in partition(starts))
        return answer, winning.cache_info().currsize


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def delayed_ambiguity_model(reveal_after_advance=False):
    """Common feasible first action, then incompatible hidden responses."""
    actions = ("advance", "left", "right")

    def successors(state, action):
        if state in ("safe", "failed"):
            result = state
        elif state.endswith("0"):
            result = state[0] + "1" if action == "advance" else "failed"
        else:
            correct = "left" if state == "a1" else "right"
            result = "safe" if action == correct else "failed"
        return frozenset((result,))

    def observation(state):
        if state in ("safe", "failed"):
            return state
        if state.endswith("1") and reveal_after_advance:
            return state
        return "stage" + state[-1]

    protected = lambda state: state != "failed"
    return actions, successors, observation, protected


def main():
    cases = []
    for reveal, reserve, lag, expected in (
        (8, 10, 3, False), (7, 10, 3, True), (8, 11, 3, True),
        (8, 10, 2, True), (0, 10, 3, True),
    ):
        model = RepairModel(reveal, reserve, lag)
        actual, information_states_checked = model.guaranteed_safe()
        require(actual == expected, "Listed repair case disagrees with recursion")
        require(actual == (reveal + lag <= reserve),
                "Recursion disagrees with this model's analytic criterion")
        cases.append({
            "revelation_time": reveal, "initial_reserve": reserve,
            "completion_latency": lag, "horizon": 12,
            "guaranteed_safe": actual, "expected": expected,
            "information_states_checked": information_states_checked,
        })

    model = RepairModel()
    boundary = RepairState(1)
    for _ in range(7):
        boundary = model.step(boundary, 0)
    boundary = model.step(boundary, 1)
    boundary = model.step(model.step(boundary, 0), 0)
    require(boundary.time == 10 and boundary.status == "safe",
            "Correct completion at the floor must be accepted")
    require(model.reserve(boundary) == 0, "Completion must be exactly at the floor")
    require(model.step(boundary, 0).status == "safe" and
            model.reserve(model.step(boundary, 0)) == 0,
            "Correct repair must halt subsequent reserve loss")

    late = RepairState(1, time=8)
    late = model.step(late, 1)
    at_floor_pending = model.step(late, 0)
    late = model.step(at_floor_pending, 0)
    require(at_floor_pending.time == 10 and at_floor_pending.status == "running",
            "Touching the protected floor is allowed before subsequent loss")
    require(late.time == 11 and late.status == "failed",
            "Correct completion one unit after the deadline must fail")

    wrong = model.step(RepairState(1), -1)
    require(model.step(wrong, 1).status == "failed",
            "An initiated recipe cannot be reversed")
    wrong = model.step(model.step(wrong, 0), 0)
    require(wrong.time == 3 and wrong.status == "failed",
            "The wrong irreversible recipe must fail on completion")

    early_sensor = RepairModel(reveal=1)
    pending = early_sensor.step(RepairState(1), -1)
    require(early_sensor.observation(pending)[-1] == 1,
            "Ongoing observations must reveal the fault during pending repair")
    require(early_sensor.step(pending, 1).status == "failed",
            "Later information must not silently undo irreversible commitment")

    _, _, update, _ = model.solver()
    before_revelation = frozenset((RepairState(-1, time=7), RepairState(1, time=7)))
    after_revelation = update(before_revelation, 0)
    require(len(after_revelation) == 2 and all(len(b) == 1 for b in after_revelation),
            "Waiting across diagnosis must split the information set")

    delayed = delayed_ambiguity_model(False)
    winning, safe_actions, _, _ = information_safety_solver(*delayed)
    initial = frozenset(("a0", "b0"))
    full = information_safety_solver(
        delayed[0], delayed[1], lambda state: state, delayed[3])
    full_first_sets = [full[1](frozenset((state,)), 2) for state in initial]
    common_first = frozenset.intersection(*full_first_sets)
    require(common_first == frozenset(("advance",)),
            "Individually viable states must have a common full-information first action")
    require(all(full[0](frozenset((state,)), 2) for state in initial),
            "Each underlying state must be individually viable")
    require(not winning(initial, 2) and not safe_actions(initial, 2),
            "Common full-information first action must not imply observation-based safety")
    revealed_winning, _, _, _ = information_safety_solver(*delayed_ambiguity_model(True))
    require(revealed_winning(initial, 2),
            "Adequate continuing observations must restore a safe conditional policy")

    result = {
        "status": "passed",
        "scope": "Exact finite illustrative models; not empirical validation",
        "method": "Finite-horizon backward recursion on information supports",
        "standard_library_only": True,
        "repair_cases": cases,
        "timing_and_observation_checks": {
            "correct_completion_at_floor_is_safe": True,
            "successful_repair_halts_reserve_loss": True,
            "completion_after_floor_deadline_fails": True,
            "recipe_initiation_is_irreversible": True,
            "wrong_recipe_fails_on_completion": True,
            "diagnosis_updates_observations_during_pending_repair": True,
            "later_information_does_not_reverse_commitment": True,
            "diagnosis_splits_information_support": True,
        },
        "first_action_overlap_counterexample": {
            "horizon": 2,
            "each_state_individually_viable": True,
            "common_full_information_first_actions": sorted(common_first),
            "observation_based_guarantee_without_later_revelation": False,
            "observation_based_guarantee_with_later_revelation": True,
        },
    }
    output = Path(__file__).resolve().with_name("observability-checks.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "output": str(output),
                      "repair_cases": len(cases),
                      "timing_and_observation_checks": 8,
                      "first_action_overlap_counterexample": "verified"}))


if __name__ == "__main__":
    main()
