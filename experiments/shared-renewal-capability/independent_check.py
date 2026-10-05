"""Independent audit of the installed shared-renewal assay.

Reconstructs the reaction generator from the declared event table; never imports
certify.py. Integer identities are exact. SciPy probabilities are floating-point
cross-checks with an explicit tolerance, not rigorous probability enclosures.
Run with a Python environment containing NumPy and SciPy.
"""
from collections import deque
from decimal import Context, Decimal, ROUND_FLOOR
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys

import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INITIAL = (0, 1, 1, 1, 1, 0, 0)
MATERIAL = 3
NUMERICAL_ATOL = 1e-11
PROFILES = tuple(itertools.product((0, 1), repeat=3))
SOURCE_PATHS = (
    HERE / "PROTOCOL.md",
    HERE / "certify.py",
    HERE / "results.json",
    ROOT / "_process/research/2026-10-05-support-and-shared-generativity/"
           "completion/STOCHASTIC-REALIZATION.md",
)

# Name, material/reserve increment, counter affected, external work increment.
# The increment and kinetic expressions are kept separate from graph assembly.
REACTIONS = (
    ("C_assembly", (-1, 1, 0, 0, 0), 6, 0),
    ("C_wear", (0, -1, 0, 1, 0), None, -1),
    ("Y_assembly", (-1, 0, 1, 0, 0), None, 0),
    ("Y_wear", (0, 0, -1, 1, 0), None, -1),
    ("capture", (0, 0, 0, 0, 1), None, 1),
    ("leak", (0, 0, 0, 0, -1), None, -1),
    ("C_recycling", (1, 0, 0, -1, -1), 5, 0),
    ("Y_recycling", (1, 0, 0, -1, -1), 5, 0),
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reaction_rates(physical, theta):
    r, c, y, d, f = physical
    return (r, c, r * y, y, c, f, c * d * f, theta * y * d * f)


def successors(state, theta):
    """Untruncated, labeled transitions with integer rates."""
    physical = state[:5]
    for reaction, rate in zip(REACTIONS, reaction_rates(physical, theta)):
        if rate == 0:
            continue
        name, change, counter, work_increment = reaction
        target = list(state)
        for i, amount in enumerate(change):
            target[i] += amount
        if counter is not None:
            target[counter] = 1
        yield name, tuple(target), rate, work_increment


def physical_states(cap):
    for r in range(MATERIAL + 1):
        for c in range(MATERIAL - r + 1):
            for y in range(MATERIAL - r - c + 1):
                d = MATERIAL - r - c - y
                for f in range(cap + 1):
                    yield (r, c, y, d, f)


def exact_audit(theta, cap):
    """Check the original generator, including capture beyond the numeric cap."""
    checked_states = checked_events = boundary_states = 0
    for physical in physical_states(cap):
        checked_states += 1
        r, c, y, d, f = physical
        state = physical + (0, 0)
        drift = [0] * 5
        work_drift = 0
        for name, target, rate, work_increment in successors(state, theta):
            checked_events += 1
            assert isinstance(rate, int) and rate > 0
            assert all(v >= 0 for v in target[:5])
            assert sum(target[:4]) == MATERIAL
            change = [target[i] - state[i] for i in range(5)]
            assert sum(change[:4]) == 0
            assert change[4] + sum(change[:3]) == work_increment
            if name in ("C_recycling", "Y_recycling", "leak"):
                assert f >= 1
            if name == "capture":
                assert rate <= MATERIAL  # eta=1, incident I=3, V=epsilon=1.
            if name in ("C_recycling", "Y_recycling"):
                assert d >= 1 and target[5] == 1
            if name == "C_assembly":
                assert r >= 1 and target[6] == 1
            for i in range(5):
                drift[i] += rate * change[i]
            work_drift += rate * work_increment
        recycling_flux = f * d * (c + theta * y)
        expected = [
            recycling_flux - r - r * y,
            r - c,
            r * y - y,
            c + y - recycling_flux,
            c - f - recycling_flux,
        ]
        assert drift == expected, (physical, theta, drift, expected)
        assert work_drift == c - f - c - y == -f - y
        assert drift[4] + sum(drift[:3]) == work_drift
        if r + c + y == 0:
            boundary_states += 1
            assert all(sum(target[:3]) == 0
                       for _, target, _, _ in successors(state, theta))
    return {"theta": theta, "energy_states_through": cap,
            "physical_states": checked_states, "positive_labeled_events": checked_events,
            "all_degraded_face_states": boundary_states,
            "material_conservation": "exact integer PASS",
            "nonnegative_successors_and_input_availability": "exact integer PASS",
            "five_coordinate_drifts": "exact integer PASS",
            "event_work_equivalent_accounting": "exact integer PASS",
            "active_material_face_invariance": "exact integer PASS",
            "scope": "Untruncated local events on every enumerated physical state; "
                     "capture from f=cap is checked at its actual f=cap+1 target."}


def construct_generator(theta, cap):
    """Reachability first; a separate lexicographic ordering builds Q."""
    reachable = {INITIAL}
    pending = deque([INITIAL])
    graph = {}
    while pending:
        state = pending.popleft()
        rates = {}
        if state is not None:
            for _, raw_target, rate, _ in successors(state, theta):
                target = None if raw_target[4] > cap else raw_target
                rates[target] = rates.get(target, 0) + rate
                if target not in reachable:
                    reachable.add(target)
                    pending.append(target)
        graph[state] = rates
    states = sorted(s for s in reachable if s is not None)
    if None in reachable:
        states.append(None)
    positions = {s: i for i, s in enumerate(states)}
    row_indices, columns, values = [], [], []
    exits = []
    for source in states:
        i = positions[source]
        row = graph[source]
        assert source not in row  # Physical events always change a coordinate.
        exit_rate = sum(row.values())
        exits.append(exit_rate)
        exact_row_sum = -exit_rate
        for target, rate in row.items():
            assert rate > 0
            exact_row_sum += rate
            row_indices.append(i)
            columns.append(positions[target])
            values.append(rate)
        assert exact_row_sum == 0
        row_indices.append(i)
        columns.append(i)
        values.append(-exit_rate)
    matrix = coo_matrix((np.asarray(values, dtype=np.int64),
                         (row_indices, columns)),
                        shape=(len(states), len(states))).tocsr()
    assert np.all(np.asarray(matrix.sum(axis=1)).ravel() == 0)
    if None in positions:
        assert matrix.getrow(positions[None]).count_nonzero() == 0
    return states, positions, matrix, max(exits), -sum(exits)


def passes(state, profile):
    if state is None:
        return False
    recycle, assemble, reserve = profile
    return (state[5] >= recycle and state[6] >= assemble
            and state[4] >= reserve and sum(state[:3]) >= 1)


def solve(theta, horizon, cap):
    states, positions, generator, gamma, trace = construct_generator(theta, cap)
    initial = np.zeros(len(states))
    initial[positions[INITIAL]] = 1.0
    duration = float(Fraction(horizon))
    probability = expm_multiply(generator.T * duration, initial,
                               traceA=trace * duration)
    total = float(probability.sum())
    minimum = float(probability.min())
    assert abs(total - 1.0) <= NUMERICAL_ATOL
    assert minimum >= -NUMERICAL_ATOL
    assays = {}
    for profile in PROFILES:
        selected = [i for i, state in enumerate(states) if passes(state, profile)]
        assays[profile] = float(probability[selected].sum())
    overflow = float(probability[positions[None]]) if None in positions else 0.0
    return {"states": len(states), "gamma": gamma, "total_probability": total,
            "minimum_probability": minimum, "overflow": overflow, "assays": assays}


def generator_action(function, state, theta):
    current = function(state)
    return sum(rate * (function(target) - current)
               for _, target, rate, _ in successors(state, theta))


def small_time_audit(theta):
    recycling = lambda s: int(passes(s, (1, 0, 0)))
    reserve = lambda s: int(passes(s, (0, 0, 1)))
    both = lambda s: int(passes(s, (1, 1, 0)))
    first_recycling = generator_action(recycling, INITIAL, theta)
    first_reserve = generator_action(reserve, INITIAL, theta)
    first_both = generator_action(both, INITIAL, theta)
    second_both = generator_action(
        lambda s: generator_action(both, s, theta), INITIAL, theta)
    assert first_recycling == 1 + theta
    assert first_reserve == -(2 + theta)
    assert first_both == 0 and second_both == 1 + theta
    return {"theta": theta, "recycling_first_derivative": first_recycling,
            "reserve_first_derivative": first_reserve,
            "recycling_and_assembly_first_derivative": first_both,
            "recycling_and_assembly_quadratic_coefficient":
                str(Fraction(second_both, 2)), "arithmetic": "exact integer/Fraction"}


def interval_distance(value, lower, upper):
    return max(0.0, lower - value, value - upper)


def main():
    source_hashes = {str(p.relative_to(ROOT)): digest(p) for p in SOURCE_PATHS}
    producer = json.loads((HERE / "results.json").read_text())
    assert producer["protocol_sha256"] == digest(HERE / "PROTOCOL.md")
    assert producer["implementation_sha256"] == digest(HERE / "certify.py")
    assert tuple(producer["initial_state"]) == INITIAL
    expected_cases = {(theta, h, cap) for h, cap in
                      (("0.05", 12), ("0.25", 12), ("1", 24)) for theta in (0, 4)}
    assert {(c["theta"], c["horizon"], c["energy_cap"])
            for c in producer["cases"]} == expected_cases
    assert len(producer["cases"]) == len(expected_cases)
    records, region_sets = [], {}
    maximum_distance = maximum_cap_shift = 0.0
    for case in producer["cases"]:
        theta, horizon, cap = case["theta"], case["horizon"], case["energy_cap"]
        result = solve(theta, horizon, cap)
        larger = solve(theta, horizon, cap + 4)
        assert result["states"] == case["states"]
        assert result["gamma"] == case["uniformization_rate"]
        exact_mean = result["gamma"] * Fraction(horizon)
        decimal_mean = Context(prec=40, rounding=ROUND_FLOOR).multiply(
            Decimal(result["gamma"]), Decimal(horizon))
        assert Fraction(decimal_mean) == exact_mean
        assert {tuple(a["profile"]) for a in case["assays"]} == set(PROFILES)
        assert len(case["assays"]) == len(PROFILES)
        comparisons, reliable = [], []
        for assay in case["assays"]:
            profile = tuple(assay["profile"])
            low_decimal, high_decimal = Decimal(assay["lower"]), Decimal(assay["upper"])
            assert 0 <= low_decimal <= high_decimal <= 1
            interval_class = ("reliable" if low_decimal >= Decimal("0.5") else
                              "unreliable" if high_decimal < Decimal("0.5") else
                              "unresolved")
            assert interval_class == assay["at_alpha_half"]
            central = result["assays"][profile]
            gap = interval_distance(central, float(low_decimal), float(high_decimal))
            assert gap <= NUMERICAL_ATOL
            extended = larger["assays"][profile]
            cap_shift = abs(extended - central)
            assert cap_shift <= float(case["overflow_upper"]) + NUMERICAL_ATOL
            if central > 0.5 + NUMERICAL_ATOL:
                float_class = "reliable"
                reliable.append(profile)
            elif central < 0.5 - NUMERICAL_ATOL:
                float_class = "unreliable"
            else:
                float_class = "unresolved"
            assert float_class == interval_class
            maximum_distance = max(maximum_distance, gap)
            maximum_cap_shift = max(maximum_cap_shift, cap_shift)
            comparisons.append({"profile": list(profile),
                                "scipy_killed_chain_probability": central,
                                "scipy_probability_cap_plus_four": extended,
                                "producer_lower": assay["lower"],
                                "producer_upper": assay["upper"],
                                "distance_from_producer_interval_float": gap,
                                "cap_increase_absolute_difference": cap_shift,
                                "classification_at_half": float_class})
        region_sets[(theta, horizon)] = set(reliable)
        records.append({"theta": theta, "horizon": horizon, "energy_cap": cap,
                        "reachable_states": result["states"],
                        "maximum_exit_rate": result["gamma"],
                        "uniformization_mean_exact": str(exact_mean),
                        "producer_decimal_mean_is_exact": True,
                        "total_probability": result["total_probability"],
                        "minimum_probability": result["minimum_probability"],
                        "scipy_overflow_probability": result["overflow"],
                        "reliable_profiles": [list(p) for p in sorted(reliable)],
                        "assays": comparisons})
    first, second = region_sets[(0, "0.25")], region_sets[(4, "0.25")]
    assert first == {(0, 0, 0), (0, 0, 1)}
    assert second == {(0, 0, 0), (1, 0, 0)}
    assert first - second and second - first
    exact_records = [exact_audit(theta, 24) for theta in (0, 4)]
    for p in SOURCE_PATHS:
        assert digest(p) == source_hashes[str(p.relative_to(ROOT))]
    output = {
        "status": "PASS: exact accounting and independent numerical agreement",
        "not_a_rigorous_numeric_certificate": True,
        "method": "Independent integer reaction generator; scipy.sparse.linalg.expm_multiply",
        "producer_imported": False,
        "source_sha256": source_hashes,
        "checker_sha256": digest(Path(__file__)),
        "git_head_at_check": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "runtime": {"executable": sys.executable, "python": platform.python_version(),
                    "numpy": np.__version__, "scipy": scipy.__version__},
        "absolute_probability_comparison_tolerance": NUMERICAL_ATOL,
        "floating_point_scope": "Tolerance is a disclosed cross-check threshold, not a proved "
                                "roundoff bound. Tiny producer intervals cannot be certified "
                                "by double precision. Their enclosure requires the separate "
                                "directed-arithmetic and overflow argument.",
        "maximum_float_distance_from_reported_interval": maximum_distance,
        "maximum_probability_change_when_cap_increased_by_four": maximum_cap_shift,
        "assay_probabilities_compared": sum(len(c["assays"]) for c in records),
        "exact_generator_audits": exact_records,
        "exact_small_time_derivatives": [small_time_audit(theta) for theta in (0, 4)],
        "fixed_half_reliability_H_quarter": {
            "theta_zero_only": [list(p) for p in sorted(first - second)],
            "theta_four_only": [list(p) for p in sorted(second - first)],
            "conclusion": "Incomparable reliable sets for the singleton installed-run protocol."},
        "cases": records,
    }
    (HERE / "independent-check.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: output[k] for k in
                      ("status", "assay_probabilities_compared",
                       "maximum_float_distance_from_reported_interval",
                       "maximum_probability_change_when_cap_increased_by_four",
                       "fixed_half_reliability_H_quarter")}, indent=2))


if __name__ == "__main__":
    main()
