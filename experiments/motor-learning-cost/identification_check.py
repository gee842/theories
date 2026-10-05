#!/usr/bin/env python3
"""Exact synthetic identification counterexamples; never reads empirical data.

No producer analysis, workbook values, fitted parameters or imported local
modules enter these checks. Numerical constants specify counterexamples, not
estimates for the PNAS source participants. The hand argument is in
UPDATER-IDENTIFICATION-MATH.md; finite enumeration is not its universal proof.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
RETENTION = F(3, 4)
FIXED_GAIN = F(1, 2)
GAINS = (F(1, 8), F(1, 2))


def gain_update(memory, error, condition, noise):
    return RETENTION * memory + GAINS[condition] * error + noise


def encode_error(error, condition):
    return GAINS[condition] / FIXED_GAIN * error


def fixed_update(memory, delivered_input, noise):
    return RETENTION * memory + FIXED_GAIN * delivered_input + noise


def exact_input_equality():
    histories = states = 0
    noise_words = ((F(0),) * 5,
                   tuple(F((-1)**i, 16) for i in range(5)),
                   tuple(F((-1)**(i+1), 16) for i in range(5)))
    for condition_word in product((0, 1), repeat=5):
        for displacement_word in product((F(-1), F(1)), repeat=5):
            for initial in (F(-1, 2), F(0), F(1, 2)):
                for noises in noise_words:
                    for clamped in (False, True):
                        x = z = initial
                        for condition, displacement, noise in zip(
                                condition_word, displacement_word, noises):
                            ex = displacement if clamped else displacement - x
                            ez = displacement if clamped else displacement - z
                            x = gain_update(x, ex, condition, noise)
                            z = fixed_update(z, encode_error(ez, condition), noise)
                            assert x == z
                            states += 1
                        histories += 1
    return {"histories": histories, "successor_equalities": states,
            "horizon": 5, "conditions": [0, 1],
            "displacements": ["-1", "1"],
            "initial_memory": ["-1/2", "0", "1/2"],
            "noise_words": [[str(n) for n in ns] for ns in noise_words],
            "error_modes": ["closed_loop_displacement_minus_memory", "externally_clamped"]}


def gate_mean_equality():
    schedules = checks = 0
    for conditions in product((0, 1), repeat=5):
        for initial in (F(-1, 2), F(0), F(1, 2)):
            distribution = {initial: F(1)}
            mean_model = initial
            for index, condition in enumerate(conditions):
                displacement = F((-1)**index)
                probability_write = GAINS[condition] / FIXED_GAIN
                following = {}
                for x, mass in distribution.items():
                    for writable, probability in ((0, 1-probability_write),
                                                   (1, probability_write)):
                        if not probability:
                            continue
                        after = RETENTION*x + FIXED_GAIN*writable*(displacement-x)
                        following[after] = following.get(after, F(0)) + mass*probability
                distribution = following
                mean_model = gain_update(mean_model, displacement-mean_model, condition, F(0))
                assert sum(distribution.values()) == 1
                assert sum(x*mass for x, mass in distribution.items()) == mean_model
                checks += 1
            schedules += 1
    probability = F(1, 4)
    gate_variance = FIXED_GAIN**2 * probability*(1-probability)
    assert gate_variance == F(3, 64) > 0
    return {"schedules": schedules, "exact_mean_equalities": checks,
            "distribution_equality_claimed": False,
            "one_step_gate_variance_at_memory0_error1": str(gate_variance),
            "deterministic_effective_gain_variance_same_case": "0"}


def exclusions_and_intervention_preservation():
    # Delivering the same signal *after* encoding separates the models in (4).
    variable_gain = gain_update(F(0), F(1), 0, F(0))
    matched_fixed = fixed_update(F(0), F(1), F(0))
    assert variable_gain == F(1, 8) and matched_fixed == F(1, 2)

    # Same current response, different fixed fast/slow hidden memory.
    fast_retention, slow_retention = F(1, 2), F(9, 10)
    after_equal_output_state0 = F(0)
    after_equal_output_state1 = fast_retention - slow_retention
    assert after_equal_output_state1 == F(-2, 5) != after_equal_output_state0

    # A task-relative causal update effect, not a constructed physical device.
    # r=0 holds memory; r=1 writes delivered evidence when W=1.
    def update(q, r, u, writable):
        return u if r and writable else q

    def encode(q, r):
        return (1-q, 1-r)

    def encoded_update(state, input_label, write_label):
        q, r = 1-state[0], 1-state[1]
        return encode(update(q, r, input_label, write_label), r)

    preserved = 0
    for q, u, writable, intervened_r in product((0, 1), repeat=4):
        # Intervention labels refer to the original physical setting. The map
        # changes its encoded value as well; merely keeping the same numeral
        # would not preserve the intervention.
        raw = update(q, intervened_r, u, writable)
        transformed = encoded_update(encode(q, intervened_r), u, writable)
        assert 1-transformed[0] == raw
        preserved += 1
    assert update(0, 0, 1, 1) == 0 and update(0, 1, 1, 1) == 1
    assert update(0, 0, 1, 0) == update(0, 1, 1, 0)
    return {"matched_delivered_input_outcomes": {
                "variable_gain": str(variable_gain), "fixed_gain": str(matched_fixed)},
            "equal_current_output_hidden_memory_next_outputs": [
                str(after_equal_output_state0), str(after_equal_output_state1)],
            "intervention_preserving_reencoding_cases": preserved,
            "effect_with_write": [0, 1], "effect_without_write": [0, 0]}


def main():
    result = {
        "status": "passed",
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Synthetic exact-rational countermodels only; no empirical data, model fit, physical intervention or new Lean claim.",
        "parameters": {"retention": str(RETENTION), "fixed_gain": str(FIXED_GAIN),
                       "effective_gains": [str(g) for g in GAINS]},
        "input_encoding": exact_input_equality(),
        "binary_write_gate": gate_mean_equality(),
        "exclusion_witnesses": exclusions_and_intervention_preservation(),
    }
    path = ROOT / "identification-results.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "output": str(path),
                      "input_histories": result["input_encoding"]["histories"],
                      "gate_mean_checks": result["binary_write_gate"]["exact_mean_equalities"]}))


if __name__ == "__main__":
    main()
