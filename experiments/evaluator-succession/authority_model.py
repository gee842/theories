#!/usr/bin/env python3
"""Deterministic checks of an illustrative endogenous-authority model.

These checks concern the specified equations, not observed institutions or the
evaluator-succession benchmark. No third-party packages are required. Results
are written only after every verification check succeeds.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import hashlib
import json
import math
from pathlib import Path
from typing import Callable


State = tuple[float, ...]
RHS = Callable[[float, State], State]


@dataclass(frozen=True)
class Parameters:
    C: float = 1.0
    K: float = 1.0
    D: float = 1.6
    rho: float = 1.0
    kappa: float = 0.4

    def __post_init__(self) -> None:
        if min(self.C, self.K, self.D, self.rho) <= 0 or self.kappa < 0:
            raise ValueError("C, K, D, rho must be positive; kappa nonnegative")

    @property
    def base_threshold(self) -> float:
        return math.sqrt(self.K * self.C)

    @property
    def reserve(self) -> float:
        return self.kappa * self.C / self.rho

    @property
    def authority_equilibrium(self) -> float:
        return 1.0 - self.reserve / self.D

    def selected_capacity(self, ell: float) -> float:
        if ell <= 0:
            raise ValueError("The selected-capacity model requires ell > 0")
        return self.C / (self.D * ell)

    def gain(self, ell: float, q: float) -> float:
        return self.K * q / (self.D * ell)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rk4(rhs: RHS, initial: State, horizon: float, step: float) -> list[State]:
    """Classical RK4, fixed step, no projection or clipping of states."""
    count = round(horizon / step)
    require(count > 0 and abs(count * step - horizon) < 1e-10,
            "horizon must be a positive integer multiple of step")
    trajectory = [tuple(initial)]
    y = tuple(initial)
    for n in range(count):
        t = n * step
        k1 = rhs(t, y)
        k2 = rhs(t + step / 2, tuple(a + step * b / 2 for a, b in zip(y, k1)))
        k3 = rhs(t + step / 2, tuple(a + step * b / 2 for a, b in zip(y, k2)))
        k4 = rhs(t + step, tuple(a + step * b for a, b in zip(y, k3)))
        y = tuple(a + step * (b + 2 * c + 2 * d + e) / 6
                  for a, b, c, d, e in zip(y, k1, k2, k3, k4))
        require(all(math.isfinite(value) for value in y), "nonfinite RK4 state")
        trajectory.append(y)
    return trajectory


def paired_run(rhs: RHS, initial: State, horizon: float, step: float = 0.02
               ) -> tuple[list[State], float]:
    coarse = rk4(rhs, initial, horizon, step)
    fine = rk4(rhs, initial, horizon, step / 2)
    error = max(abs(a - b) for yc, yf in zip(coarse, fine[::2])
                for a, b in zip(yc, yf))
    require(error < 1e-5, f"step-halving disagreement too large: {error}")
    return fine, error


def authority_rhs(p: Parameters, rate: float) -> RHS:
    require(rate >= 0, "adjustment rate must be nonnegative")

    def rhs(_t: float, y: State) -> State:
        ell, q = y
        return (p.rho * (1 - ell) - p.kappa * q * ell,
                rate * (p.selected_capacity(ell) - q))

    return rhs


def summary(p: Parameters, trajectory: list[State], step: float) -> dict:
    gains = [p.gain(ell, q) for ell, q in trajectory]
    first_crossing = next((i * step for i, g in enumerate(gains) if g >= 1), None)
    return {
        "initial": list(trajectory[0]),
        "final": list(trajectory[-1]),
        "minimum_authority": min(y[0] for y in trajectory),
        "maximum_authority": max(y[0] for y in trajectory),
        "minimum_capacity": min(y[1] for y in trajectory),
        "maximum_capacity": max(y[1] for y in trajectory),
        "initial_gain": gains[0],
        "maximum_gain": max(gains),
        "final_gain": gains[-1],
        "first_sample_at_gain_at_least_one": first_crossing,
    }


def correction_dose(D: float, rho: float, ell_start: float, elapsed: float) -> float:
    require(D > 0 and rho > 0 and 0 <= ell_start <= 1 and elapsed >= 0,
            "invalid correction-dose parameters")
    return D * (elapsed + (1 - ell_start) * math.expm1(-rho * elapsed) / rho)


def verify() -> dict:
    result: dict = {
        "status": "verified",
        "interpretation": "Simulation and algebra checks for an illustrative model; not empirical evidence, a proof by simulation, or a novelty claim.",
        "state_order": ["independent_authority_ell", "influence_capacity_q"],
        "integration": {"method": "RK4 without state clipping", "coarse_step": 0.02,
                        "fine_step": 0.01, "maximum_allowed_pair_disagreement": 1e-5},
    }

    # Independent analytic check of the quasi-static reduction.
    analytic_cases = []
    for D in (1.3, 1.4, 1.6):
        p = Parameters(D=D)
        ell0 = 1.0
        exact = lambda t: p.authority_equilibrium + (ell0 - p.authority_equilibrium) * math.exp(-p.rho * t)
        rhs = lambda _t, y: (p.rho * (1 - y[0]) - p.kappa * p.C / p.D,)
        coarse = rk4(rhs, (ell0,), 10, 0.02)
        fine = rk4(rhs, (ell0,), 10, 0.01)
        coarse_error = max(abs(y[0] - exact(i * 0.02)) for i, y in enumerate(coarse))
        fine_error = max(abs(y[0] - exact(i * 0.01)) for i, y in enumerate(fine))
        require(fine_error < 1e-10 and 12 < coarse_error / fine_error < 20,
                "quasi-static analytic verification or RK4 convergence failed")
        analytic_cases.append({"parameters": asdict(p), "coarse_exact_error": coarse_error,
                               "fine_exact_error": fine_error, "error_ratio": coarse_error / fine_error,
                               "limiting_effective_correction": p.D - p.reserve,
                               "limiting_gain": p.base_threshold ** 2 / (p.D - p.reserve) ** 2})
    result["quasi_static_analytic_checks"] = analytic_cases
    result["quasi_static_below_threshold_crossing_time"] = math.log(4)
    p_edge = Parameters(D=1.4)
    edge_gains = [p_edge.base_threshold ** 2 / (p_edge.D * (p_edge.authority_equilibrium
                    + (1 - p_edge.authority_equilibrium) * math.exp(-t))) ** 2 for t in (1, 5, 10)]
    require(all(g < 1 for g in edge_gains), "equality-case finite-time certificate failed")
    result["threshold_equality"] = {"times": [1, 5, 10], "gains": edge_gains,
                                    "limiting_gain": 1.0,
                                    "meaning": "Strict at each finite time from ell0=1, but no uniform strict margin."}

    # Boundary/corner checks of the proven invariant rectangle at several speeds.
    p = Parameters()
    ell_min = 0.7
    q_max = p.C / (p.D * ell_min)
    gain_bound = p.K * p.C / (p.D ** 2 * ell_min ** 2)
    require(p.base_threshold / p.D < ell_min <= p.authority_equilibrium,
            "invalid invariant rectangle")
    invariant_runs = []
    for rate in (0.05, 1.0, 10.0):
        for initial in ((ell_min, 0.0), (ell_min, q_max), (1.0, 0.0), (1.0, q_max)):
            trajectory, error = paired_run(authority_rhs(p, rate), initial, 20)
            row = summary(p, trajectory, 0.01)
            require(row["minimum_authority"] >= ell_min - 1e-10, "authority left certified rectangle")
            require(row["maximum_authority"] <= 1 + 1e-10, "authority exceeds one")
            require(row["minimum_capacity"] >= -1e-10 and row["maximum_capacity"] <= q_max + 1e-10,
                    "capacity left certified rectangle")
            require(row["maximum_gain"] <= gain_bound + 1e-10 < 1,
                    "gain exceeded invariant bound")
            invariant_runs.append({"adjustment_rate": rate, "h_vs_half_h_disagreement": error, **row})
    result["invariant_rectangle"] = {"parameters": asdict(p), "authority_floor": ell_min,
                                     "capacity_ceiling": q_max, "gain_bound": gain_bound,
                                     "runs": invariant_runs}

    # Failure below the reserve threshold with ordinary selected-level tracking.
    p_low = Parameters(D=1.3)
    trajectory, error = paired_run(authority_rhs(p_low, 1.0), (1.0, p_low.C / p_low.D), 40)
    low = summary(p_low, trajectory, 0.01)
    require(low["initial_gain"] < 1 < low["final_gain"], "below-threshold example did not cross")
    require(abs(low["final_gain"] - 1 / 0.9 ** 2) < 1e-6, "incorrect positive equilibrium")
    result["below_threshold_tracking"] = {"parameters": asdict(p_low), "adjustment_rate": 1.0,
                                          "h_vs_half_h_disagreement": error, **low}

    # The reserve threshold is not necessary for arbitrary nontracking trajectories.
    p_stalled = Parameters(D=0.8)
    trajectory, error = paired_run(authority_rhs(p_stalled, 0), (0.8, 0.0), 20)
    stalled = summary(p_stalled, trajectory, 0.01)
    require(stalled["maximum_gain"] == 0, "stalled-capacity counterexample failed")
    result["below_threshold_without_tracking"] = {"parameters": asdict(p_stalled),
        "adjustment_rate": 0.0, "h_vs_half_h_disagreement": error, **stalled}

    # A valid initial row gain is weaker than the invariant initial-stock conditions.
    p_large = Parameters(D=1.6)
    trajectory, error = paired_run(authority_rhs(p_large, 0.001), (1.0, 1.5), 20)
    large = summary(p_large, trajectory, 0.01)
    require(large["initial_gain"] < 1 < large["maximum_gain"], "oversized-stock counterexample failed")
    result["oversized_initial_stock"] = {"parameters": asdict(p_large), "adjustment_rate": 0.001,
                                        "h_vs_half_h_disagreement": error, **large}

    p_zero = Parameters(D=1.2, kappa=0)
    trajectory, error = paired_run(authority_rhs(p_zero, 1), (0.9, 1 / 1.08), 20)
    zero = summary(p_zero, trajectory, 0.01)
    require(p_zero.reserve == 0 and zero["maximum_gain"] < 1, "zero-erosion reduction failed")
    result["zero_erosion"] = {"parameters": asdict(p_zero), "adjustment_rate": 1.0,
                              "h_vs_half_h_disagreement": error, **zero}

    # The best-case dose bound is attained with no incoming support and no erosion.
    D, rho, ell_start, s_start, epsilon = 1.6, 1.0, 0.2, 4.0, 1.0
    neutral_support = 1.0  # c/a
    required_dose = math.log(s_start / neutral_support) / epsilon

    def deadline_rhs(incoming: float) -> RHS:
        def rhs(_t: float, y: State) -> State:
            ell, support, dose = y
            return rho * (1 - ell), epsilon * (incoming - D * ell * support), D * ell
        return rhs

    deadline_runs = []
    for elapsed in (1.0, 2.0):
        trajectory, error = paired_run(deadline_rhs(0), (ell_start, s_start, 0.0), elapsed)
        delivered = correction_dose(D, rho, ell_start, elapsed)
        exact_support = s_start * math.exp(-epsilon * delivered)
        require(abs(trajectory[-1][2] - delivered) < 1e-9, "dose integration disagrees with exact bound")
        require(abs(trajectory[-1][1] - exact_support) < 1e-8, "support solution disagrees with exact bound")
        require((delivered < required_dose) == (trajectory[-1][1] > neutral_support),
                "deadline direction mismatch")
        deadline_runs.append({"elapsed": elapsed, "maximum_dose": delivered,
                              "exact_best_case_final_support": exact_support,
                              "rk4_final_support": trajectory[-1][1],
                              "h_vs_half_h_disagreement": error,
                              "necessary_dose_met": delivered >= required_dose})
    incoming_trajectory, incoming_error = paired_run(deadline_rhs(10), (ell_start, s_start, 0), 2)
    require(correction_dose(D, rho, ell_start, 2) > required_dose
            and incoming_trajectory[-1][1] > neutral_support,
            "positive-input counterexample to sufficiency failed")
    low_time, high_time = 0.0, 10.0
    for _ in range(80):
        middle = (low_time + high_time) / 2
        if correction_dose(D, rho, ell_start, middle) < required_dose:
            low_time = middle
        else:
            high_time = middle
    removal_support = 0.5
    require(removal_support < neutral_support, "direct-removal escape did not remove advantage")
    result["deadline_bound"] = {
        "D": D, "rho": rho, "authority_at_intervention": ell_start,
        "support_at_intervention": s_start, "epsilon": epsilon,
        "neutral_support": neutral_support, "required_dose": required_dose,
        "earliest_best_case_neutralization_elapsed": high_time,
        "runs": deadline_runs,
        "positive_incoming_support": {"incoming": 10, "elapsed": 2,
                                      "final_support": incoming_trajectory[-1][1],
                                      "h_vs_half_h_disagreement": incoming_error,
                                      "meaning": "Passing the dose test alone is not sufficient."},
        "direct_removal_escape": {"support_immediately_after_removal": removal_support,
                                  "meaning": "An intervention outside damping-only control removes the current advantage immediately; it does not establish lasting safety."},
    }
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write verified results to this JSON path")
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "invariant_runs": len(result["invariant_rectangle"]["runs"]),
                      "below_threshold_crossing": result["below_threshold_tracking"]["first_sample_at_gain_at_least_one"],
                      "oversized_stock_crossing": result["oversized_initial_stock"]["first_sample_at_gain_at_least_one"],
                      "output": str(args.output) if args.output else None}, indent=2))


if __name__ == "__main__":
    main()
