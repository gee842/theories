#!/usr/bin/env python3
"""Exact rational finite-register succession experiment. Standard library only.

Public architecture, timing, and fees are fixed before payload observation.
No controller transcript exists: the final decoder receives only the actual
physical register. Every deterministic 3-symbol encoder/decoder is enumerated.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import csv
import json


SYMBOLS = (None, 0, 1)
ENCODERS = tuple(product(SYMBOLS, repeat=2))
DECODERS = tuple(product((0, 1), repeat=3))


def stale_error(eta, age):
    assert F(0) <= eta <= F(1, 2) and age >= 0
    return (1 - (1 - 2 * eta) ** age) / 2


def matrix_error(eta, age):
    p0, p1 = F(1), F(0)
    for _ in range(age):
        p0, p1 = p0 * (1 - eta) + p1 * eta, p0 * eta + p1 * (1 - eta)
    return p1


def decode(d, symbol):
    return d[SYMBOLS.index(symbol)]


def register_protocol(source_bit, encoder, archive_alive=True, access=True, keep=True):
    archive = encoder[source_bit]  # material write, billed independently of value
    if not archive_alive:
        archive = None
    successor = None  # real controller reset, with no transcript argument
    if access:
        successor = archive
    if not keep:
        successor = None
    return successor


@lru_cache(None)
def optimize_payload(eta, age, archive_alive=True, access=True, keep=True):
    q = stale_error(eta, age)
    best = None
    witness = None
    checked = 0
    for encoder in ENCODERS:
        for decoder in DECODERS:
            error = F(0)
            for source, target in product((0, 1), repeat=2):
                probability = F(1, 2) * ((1 - q) if source == target else q)
                register = register_protocol(source, encoder, archive_alive, access, keep)
                error += probability * (decode(decoder, register) != target)
            checked += 1
            if best is None or error < best:
                best, witness = error, {"encoder": encoder, "decoder": decoder}
    expected = q if archive_alive and access and keep else F(1, 2)
    assert best == expected
    return best, witness, checked


@dataclass(frozen=True)
class Case:
    name: str
    eta: F = F(1, 10)
    gap: int = 1
    handoff_latency: int = 1
    fresh_latency: int = 1
    action_delay: int = 1
    storage_per_slot: F = F(1, 10)
    handoff_fee: F = F(1, 2)
    fresh_fee: F = F(4)
    register_per_slot: F = F(1, 5)
    early_budget: F = F(10)
    handoff_budget: F = F(0)
    deadline: int = 5
    error_weight: F = F(20)
    handoff_access: bool = True
    archive_alive: bool = True
    local_retention: bool = True
    existing_archive: bool = False  # already paid before this comparison


def options(c):
    local_fee = c.register_per_slot * c.action_delay if c.local_retention else F(0)
    effective_keep = c.local_retention or c.action_delay == 0
    archive_fee = F(0) if c.existing_archive else c.storage_per_slot * c.gap
    total_budget = c.early_budget + c.handoff_budget
    rows = []
    for route in ("none", "inherit", "reacquire"):
        if route == "none":
            pre, late, duration, age, error = F(0), F(0), 0, None, F(1, 2)
            payload_witness = {"decoder": (0, 0, 0)}
            gate = True
        elif route == "inherit":
            pre, late = archive_fee, c.handoff_fee + local_fee
            duration = c.handoff_latency + c.action_delay
            age = c.gap + duration
            gate = c.handoff_access and c.archive_alive
            error, payload_witness, _ = optimize_payload(
                c.eta, age, c.archive_alive, c.handoff_access, effective_keep)
        else:
            pre, late = F(0), c.fresh_fee + local_fee
            duration = c.fresh_latency + c.action_delay
            age = duration
            gate = True
            error, payload_witness, _ = optimize_payload(c.eta, age, True, True, effective_keep)
        cost = pre + late
        feasible = gate and pre <= c.early_budget and cost <= total_budget and duration <= c.deadline
        rows.append({"route": route, "prepayment": pre, "later_payment": late,
                     "cost": cost, "duration": duration, "evidence_age": age,
                     "error": error, "expected_criterion": cost + c.error_weight * error,
                     "feasible": feasible, "payload_witness": payload_witness})
    return rows


def solve_case(c):
    rows = options(c)
    feasible = [r for r in rows if r["feasible"]]
    criterion_choice = min(feasible, key=lambda r: r["expected_criterion"])
    quality = {}
    for tolerance in (F(0), F(1, 10), F(1, 5), F(1, 4), F(1, 2)):
        eligible = [r for r in feasible if r["error"] <= tolerance]
        winner = min(eligible, key=lambda r: r["cost"]) if eligible else None
        quality[str(tolerance)] = None if winner is None else {
            "route": winner["route"], "cost": winner["cost"], "error": winner["error"]}
    return {"case": c.__dict__, "routes": rows, "criterion_choice": criterion_choice["route"],
            "minimum_criterion": criterion_choice["expected_criterion"],
            "least_cost_by_error_tolerance": quality}


def primitive(value):
    if isinstance(value, F):
        return {"exact": str(value), "decimal": float(value)}
    if isinstance(value, dict):
        return {str(k): primitive(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [primitive(v) for v in value]
    return value


def main():
    rates = (F(0), F(1, 1000), F(1, 20), F(1, 10), F(1, 4), F(1, 2))
    formula_checks = 0
    register_checks = 0
    for eta, age in product(rates, range(51)):
        assert stale_error(eta, age) == matrix_error(eta, age)
        formula_checks += 1
        for alive, access, keep in product((False, True), repeat=3):
            _, _, count = optimize_payload(eta, age, alive, access, keep)
            register_checks += count
    scale_checks = 0
    for eta, block, blocks in product(rates, range(1, 6), range(11)):
        assert stale_error(eta, block * blocks) == stale_error(stale_error(eta, block), blocks)
        scale_checks += 1

    base = Case("short_gap_preserve")
    cases = [base,
             replace(base, name="long_gap_reacquire", gap=8),
             replace(base, name="persistent_long_gap_preserve", eta=F(1, 1000), gap=8),
             replace(base, name="stable_but_costly_storage", eta=F(0), gap=50),
             replace(base, name="independent_next_bit", eta=F(1, 2)),
             replace(base, name="static_unknown_bit", eta=F(0)),
             replace(base, name="register_erased", local_retention=False),
             replace(base, name="raw_archive_destroyed", archive_alive=False),
             replace(base, name="late_financing", early_budget=F(0), handoff_budget=F(10)),
             replace(base, name="existing_record_open", existing_archive=True, fresh_latency=3, deadline=2),
             replace(base, name="existing_record_blocked", existing_archive=True,
                     fresh_latency=3, deadline=2, handoff_access=False),
             replace(base, name="fresh_zero_delay", eta=F(1, 2), fresh_latency=0,
                     action_delay=0, handoff_latency=1),
             replace(base, name="tight_budget", early_budget=F(1)),
             replace(base, name="tight_quality_deadline", fresh_latency=3, deadline=2)]
    results = [solve_case(c) for c in cases]
    expected = {"short_gap_preserve": "inherit", "long_gap_reacquire": "reacquire",
                "persistent_long_gap_preserve": "inherit", "stable_but_costly_storage": "reacquire",
                "independent_next_bit": "none", "static_unknown_bit": "inherit",
                "register_erased": "none", "raw_archive_destroyed": "reacquire",
                "late_financing": "reacquire", "existing_record_open": "inherit",
                "existing_record_blocked": "none", "fresh_zero_delay": "reacquire",
                "tight_budget": "inherit", "tight_quality_deadline": "inherit"}
    for r in results:
        assert r["criterion_choice"] == expected[r["case"]["name"]]

    # The exact tolerance frontier is distinct from a supplied aggregate score.
    short = results[0]
    assert short["least_cost_by_error_tolerance"]["1/5"]["route"] == "reacquire"
    tight = results[-1]
    assert tight["least_cost_by_error_tolerance"]["1/5"] is None

    # Robust constant-bit special case; arbitrary randomized response p after
    # erasure has worst success min(p,1-p)<=1/2, attained by p=1/2.
    random_grid = [F(k, 20) for k in range(21)]
    erased_maximin = max(min(p, 1 - p) for p in random_grid)
    assert erased_maximin == F(1, 2)
    assert optimize_payload(F(0), 50, True, True, True)[0] == 0

    # Side-channel countermodel: visible paid balance can preserve the bit even
    # when the named report register is erased. This is NOT allowed implicitly
    # in the main model: it is a distinct, explicitly modeled memory channel.
    for bit in (0, 1):
        cash_after = 1 - bit
        named_register = None
        decoded_from_cash = 1 - cash_after
        assert named_register is None and decoded_from_cash == bit

    archive_after_read_control = []
    for bit in (0, 1):
        archive = bit
        successor_register = archive
        archive = None
        action = successor_register
        assert archive is None and action == bit
        archive_after_read_control.append({"source_bit": bit, "archive_after_copy": archive,
                                           "paid_successor_register": successor_register,
                                           "action": action})

    frontier = []
    for eta, gap in product(rates, range(1, 51)):
        c = replace(base, name="frontier", eta=eta, gap=gap)
        r = solve_case(c)
        by_route = {x["route"]: x for x in r["routes"]}
        frontier.append({"eta": str(eta), "gap": gap, "choice": r["criterion_choice"],
                         "inherit_cost": float(by_route["inherit"]["cost"]),
                         "inherit_error": float(by_route["inherit"]["error"]),
                         "inherit_criterion": float(by_route["inherit"]["expected_criterion"]),
                         "fresh_cost": float(by_route["reacquire"]["cost"]),
                         "fresh_error": float(by_route["reacquire"]["error"]),
                         "fresh_criterion": float(by_route["reacquire"]["expected_criterion"])})

    report = {"status": "all assertions passed", "date": "2026-10-05",
              "formula_checks": formula_checks, "deterministic_register_policies_checked": register_checks,
              "exact_time_coarsening_checks": scale_checks,
              "encoder_count": len(ENCODERS), "decoder_count": len(DECODERS),
              "cases": results, "frontier_points": len(frontier),
              "erased_register_randomized_maximin_success": erased_maximin,
              "side_channel_control": {"named_register": None,
                                       "balance_after_encoding_0": 1,
                                       "balance_after_encoding_1": 0,
                                       "decoding": "bit = 1 - balance"},
              "archive_erased_after_acquisition_control": archive_after_read_control,
              "limits": ["Restricted paid architecture chosen before hidden payload",
                         "Only physical register and declared public constants reach final actuator",
                         "Clock, program, and phase are free but payload-independent",
                         "No stochastic probabilities imply a sure-safety guarantee",
                         "Repeated use assumes a reliable external allotment each epoch"]}
    directory = Path(__file__).parent
    (directory / "paid-memory-results.json").write_text(json.dumps(primitive(report), indent=2) + "\n")
    with (directory / "paid-memory-frontier.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(frontier[0]))
        writer.writeheader()
        writer.writerows(frontier)
    print(json.dumps({"status": report["status"], "formula_checks": formula_checks,
                      "policies_checked": register_checks, "frontier_points": len(frontier),
                      "cases": [{"name": r["case"]["name"], "choice": r["criterion_choice"],
                                 "criterion": float(r["minimum_criterion"])} for r in results]}, indent=2))


if __name__ == "__main__":
    main()
