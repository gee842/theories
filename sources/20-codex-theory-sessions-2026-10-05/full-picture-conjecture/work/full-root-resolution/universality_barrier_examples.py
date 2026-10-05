"""Finite illustrations only; the written reduction supplies the general proof."""

from __future__ import annotations

import json
from pathlib import Path


def forever_step(state: int | None) -> int | None:
    return None if state is None else state + 1


def cutoff_step(state: int | None, cutoff: int) -> int | None:
    return None if state is None or state >= cutoff else state + 1


def prefix_checks() -> dict:
    observations_checked = 0
    for cutoff in range(201):
        left = right = 0
        for instant in range(cutoff + 1):
            assert left == right == instant
            observations_checked += 1
            left = forever_step(left)
            right = cutoff_step(right, cutoff)
        assert left == cutoff + 1 and right is None
        assert cutoff_step(right, cutoff) is None
    return {
        "cutoffs_checked": 201,
        "matching_prefix_observations_checked": observations_checked,
        "divergent_next_states_checked": 201,
        "all_passed": True,
    }


def wrapper_step(state, program):
    if state is None:
        return None, None
    configuration, next_output = state
    if program["halted"](configuration):
        return None, None
    return (program["step"](configuration), next_output + 1), next_output + 1


def wrapper_checks() -> dict:
    programs = []
    for stop in (0, 1, 2, 7, 31, 63):
        programs.append({
            "name": f"halts_after_{stop}_steps",
            "halt_after": stop,
            "initial": 0,
            "halted": lambda c, bound=stop: c == bound,
            "step": lambda c: c + 1,
        })
    programs.extend([
        {"name": "one_state_loop", "halt_after": None, "initial": 0,
         "halted": lambda c: False, "step": lambda c: c},
        {"name": "two_state_loop", "halt_after": None, "initial": 0,
         "halted": lambda c: False, "step": lambda c: 1 - c},
    ])
    state_checks = output_checks = 0
    for program in programs:
        state = (program["initial"], 0)
        outputs = []
        stop = program["halt_after"]
        for instant in range(129):
            assert (state is not None) == (stop is None or instant <= stop)
            state_checks += 1
            expected_outputs = instant if stop is None else min(instant, stop)
            assert outputs == list(range(1, expected_outputs + 1))
            output_checks += 1
            state, output = wrapper_step(state, program)
            if output is not None:
                outputs.append(output)
    return {
        "toy_programs_checked": len(programs),
        "state_checks": state_checks,
        "output_prefix_checks": output_checks,
        "all_passed": True,
        "qualification": "Finite wrapper checks; these toy programs are not a universal-machine implementation.",
    }


def main():
    results = {
        "status": "Finite illustrations, not a proof of undecidability or empirical universality.",
        "finite_prefix": prefix_checks(),
        "wrapper": wrapper_checks(),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
