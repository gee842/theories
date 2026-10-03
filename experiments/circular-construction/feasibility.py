#!/usr/bin/env python3
"""Reproducible sensitivity arithmetic, NOT a simulation or structural proof.

Run: python3 feasibility.py --check
Runs hand-computable checks, writes results.json beside this file, and prints a
summary. Without --check it writes the same deterministic results. Standard
library only. Scenario inputs are illustrative assumptions, not measurements.
"""

import argparse
import json
import math
from pathlib import Path


GRAVITY_M_S2 = 9.81  # Rounded Earth-gravity assumption, not a site measurement.
SECTION_MASS_KG_M = 31.1
SECTION_SOURCE = (
    "https://www.britishsteel.co.uk/wp-content/uploads/2025/07/"
    "british-steel-product-brochure-14012025-compressed-1.pdf"
)


def positive(**values):
    for name, value in values.items():
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be finite and positive")


def probability(value):
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("probability/fraction must be in [0, 1]")


def count(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("count must be a nonnegative integer")


def beam_loads(length_m, kg_m=SECTION_MASS_KG_M, gravity=GRAVITY_M_S2):
    """Uniform horizontal beam; endpoint support cases are alternatives."""
    positive(length_m=length_m, kg_m=kg_m, gravity=gravity)
    mass = length_m * kg_m
    weight = mass * gravity
    return {
        "length_m": length_m,
        "mass_per_m_kg": kg_m,
        "mass_kg": mass,
        "gravity_force_N": weight,
        "one_end_fixed_hold_required_force_N": weight,
        "one_end_fixed_hold_required_moment_Nm": weight * length_m / 2,
        "two_endpoint_support_reactions_N": [weight / 2, weight / 2],
    }


def anchor_wrench(robot_kg, robot_offset_m, beam_kg, beam_offset_m,
                  gravity=GRAVITY_M_S2):
    """Gravity loads at one reference; horizontal offsets on the same side."""
    positive(robot_kg=robot_kg, beam_kg=beam_kg, gravity=gravity)
    for offset in (robot_offset_m, beam_offset_m):
        if not math.isfinite(offset) or offset < 0:
            raise ValueError("offsets must be finite and nonnegative")
    force = (robot_kg + beam_kg) * gravity
    moment = gravity * (robot_kg * robot_offset_m + beam_kg * beam_offset_m)
    return {
        "inputs": {
            "robot_mass_kg": robot_kg,
            "robot_COM_horizontal_offset_m": robot_offset_m,
            "beam_mass_kg": beam_kg,
            "beam_COM_horizontal_offset_m": beam_offset_m,
        },
        "external_downward_force_N": force,
        "external_overturning_moment_Nm": moment,
        "required_aggregate_upward_reaction_N": force,
        "required_aggregate_counter_moment_Nm": moment,
        "interpretation": (
            "Net gravity wrench only; aggregate reactions must balance it. "
            "This does not allocate loads to anchors or test their feasibility. "
            "The 1 m beam offset is an assumed COM location relative to the "
            "anchor reference, not a claim that its COM is 1 m from a beam end."
        ),
    }


def throughput_bounds(placements, cells, cycle_min, utilization,
                      supply_members_h, supply_tonnes_h, mean_member_kg,
                      critical_path_h, climbers_per_cell=2):
    count(placements)
    count(cells)
    count(climbers_per_cell)
    positive(placements=placements, cells=cells, cycle_min=cycle_min,
             climbers_per_cell=climbers_per_cell, utilization=utilization,
             supply_members_h=supply_members_h, supply_tonnes_h=supply_tonnes_h,
             mean_member_kg=mean_member_kg)
    if utilization > 1 or not math.isfinite(critical_path_h) or critical_path_h < 0:
        raise ValueError("utilization must be <= 1; critical path must be >= 0")
    bounds = {
        "work_capacity": placements * cycle_min / (60 * cells * utilization),
        "member_supply": placements / supply_members_h,
        "mass_supply": placements * mean_member_kg / (1000 * supply_tonnes_h),
        "critical_path": critical_path_h,
    }
    bound = max(bounds.values())
    return {
        "inputs": {
            "placements": placements, "cells": cells,
            "climbers_per_cell": climbers_per_cell,
            "complete_placement_cycle_min": cycle_min,
            "cell_utilization": utilization,
            "supply_members_per_h": supply_members_h,
            "supply_metric_tonnes_per_h": supply_tonnes_h,
            "mean_member_mass_kg": mean_member_kg,
            "assumed_critical_path_h": critical_path_h,
        },
        "total_climbers": cells * climbers_per_cell,
        "assumed_total_member_mass_tonnes": placements * mean_member_kg / 1000,
        "bounds_hours": bounds,
        "lower_bound_hours": bound,
        "lower_bound_continuous_24h_days": bound / 24,
        "limiting_bounds": [key for key, value in bounds.items()
                            if math.isclose(value, bound, rel_tol=1e-12)],
    }


def retention(fraction, cycles):
    probability(fraction)
    count(cycles)
    remaining = fraction ** cycles
    return {"retained_fraction_per_cycle": fraction, "cycles": cycles,
            "fraction_of_original_stock_remaining": remaining,
            "cumulative_fraction_lost": 1 - remaining}


def unresolved_events(per_task_probability, tasks):
    probability(per_task_probability)
    count(tasks)
    if tasks == 0:
        no_event = 1.0
    elif per_task_probability == 1:
        no_event = 0.0
    else:
        no_event = math.exp(tasks * math.log1p(-per_task_probability))
    return {"independent_unresolved_event_probability_per_task": per_task_probability,
            "tasks": tasks, "expected_unresolved_events": tasks * per_task_probability,
            "probability_of_no_unresolved_event": no_event,
            "probability_of_at_least_one_unresolved_event": 1 - no_event}


def check():
    """Check conservation, units and limiting cases with simple exact inputs."""
    beam = beam_loads(4, kg_m=2, gravity=10)
    assert beam["mass_kg"] == 8
    assert beam["gravity_force_N"] == 80
    assert beam["one_end_fixed_hold_required_moment_Nm"] == 160
    assert beam["two_endpoint_support_reactions_N"] == [40, 40]
    assert sum(beam["two_endpoint_support_reactions_N"]) == beam["gravity_force_N"]
    wrench = anchor_wrench(2, 1, 3, 2, gravity=10)
    assert wrench["external_downward_force_N"] == 50
    assert wrench["external_overturning_moment_Nm"] == 80
    scenario = throughput_bounds(120, 2, 1, 0.5, 60, 6, 100, 1)
    assert scenario["bounds_hours"] == {
        "work_capacity": 2, "member_supply": 2, "mass_supply": 2, "critical_path": 1}
    assert scenario["limiting_bounds"] == ["work_capacity", "member_supply", "mass_supply"]
    assert scenario["total_climbers"] == 4  # A two-robot cell is one work server.
    assert retention(0.5, 2)["fraction_of_original_stock_remaining"] == 0.25
    assert retention(1, 100)["fraction_of_original_stock_remaining"] == 1
    assert retention(0.5, 0)["fraction_of_original_stock_remaining"] == 1
    events = unresolved_events(0.5, 2)
    assert events["expected_unresolved_events"] == 1
    assert math.isclose(events["probability_of_no_unresolved_event"], 0.25)
    assert unresolved_events(1, 0)["probability_of_no_unresolved_event"] == 1
    assert unresolved_events(1, 2)["probability_of_no_unresolved_event"] == 0
    assert unresolved_events(0, 2)["probability_of_no_unresolved_event"] == 1
    for invalid in (-0.1, 1.1, float("nan")):
        try:
            retention(invalid, 100)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid retention fraction was accepted")


def results():
    beams = [beam_loads(length) for length in (3, 6)]
    scenarios = []
    for cells in (10, 20, 40):
        scenarios.append({"id": f"baseline_{cells}_cells", **throughput_bounds(
            10000, cells, 12, 0.65, 100, 5, 100, 72)})
    scenarios.append({"id": "40_cells_improved_supply", **throughput_bounds(
        10000, 40, 12, 0.65, 200, 20, 100, 72)})
    scenarios.append({
        "id": "48_cells_improved_supply",
        "additional_assumption": "Cell count increased from 40 to 48; unvalidated sensitivity only.",
        **throughput_bounds(10000, 48, 12, 0.65, 200, 20, 100, 72),
    })
    return {
        "title": "Circular construction: arithmetic sensitivity calculations",
        "schema_version": 1,
        "status": "NOT a simulation, structural proof, design specification or schedule forecast",
        "provenance": {
            "catalog_input": {
                "section": "British Steel UB 254 x 146 x 31",
                "mass_per_m_kg": SECTION_MASS_KG_M,
                "source_title": "British Steel Product Range, section 3.1 UK Sections",
                "source_url": SECTION_SOURCE,
                "verified_date": "2026-09-30",
                "scope": "Catalog mass only; no section selection or adequacy claim.",
            },
            "scenario_inputs": (
                "All lengths, robot values, offsets, operation counts, cycle times, "
                "utilization, logistics capacities, mean member mass, critical-path "
                "duration, retention and event probabilities are hypothetical inputs. "
                "They are not measurements or quantities from a designed building."
            ),
            "constants": {"rounded_gravity_m_s2": GRAVITY_M_S2,
                          "kg_per_metric_tonne": 1000, "minutes_per_hour": 60},
        },
        "assumptions_and_limitations": [
            "No building floor area, building height, member design, site or assembly plan is implied.",
            "Beam examples are uniform and horizontal; self-weight only, no fittings or payloads. "
            "One-end holding assumes an ideal moment-resisting support. Two-support reactions "
            "assume supports exactly at the two endpoints; the cases are alternatives.",
            "Anchor wrench is aggregate static external gravity demand only. No contact-force "
            "distribution, friction, force closure, actuator limits, anchor capacity, stiffness, "
            "buckling, wind, dynamics, tool loads, safety factors or partial-frame stability is tested.",
            "Throughput treats each cell of two climbers as one placement server. A cycle completes "
            "one member including both ends; it is not a per-bolt or per-robot cycle. Logistics "
            "equipment is additional and has no assumed fleet count here.",
            "T >= max(N*c/(60*cells*u), N/member_supply, N*mean_mass/(1000*mass_supply), "
            "critical_path). This optimistic bound assumes effective overlap, steady supply and "
            "available work fronts. Queueing, precedence-resource interactions, start-up, "
            "weather, recovery and other non-overlapping work can increase elapsed time.",
            "Supply rates and utilization are averages over the same elapsed-time horizon. "
            "Days mean continuous 24-hour days. The 72-hour critical path is assumed, not computed.",
            "The throughput mean mass of 100 kg is independent of the illustrative UB beam masses.",
            "Improved supply alone leaves the 40-cell 12-minute case work-limited at 76.923 hours. "
            "Only the separate 48-cell sensitivity becomes critical-path-limited at 72 hours.",
            "Retention compounds a fixed per-cycle fraction of original stock, with no top-up. "
            "It does not estimate actual reuse yield or ecological regeneration.",
            "Event calculations assume independent identical per-task unresolved-event probabilities. "
            "An unresolved event is not automatically a structural failure. Correlations, recovery, "
            "duration and severity are unmodeled; probabilities are not observed reliability data.",
        ],
        "beam_self_weight_examples": beams,
        "robot_plus_6m_beam_aggregate_gravity_wrench": anchor_wrench(100, 0.5, beams[1]["mass_kg"], 1),
        "throughput_sensitivities": scenarios,
        "work_capacity_only_reference": {
            "inputs": {"operations": 3500, "cells": 12, "cycle_min": 10, "utilization": 0.5},
            "raw_work_lower_bound_h": 3500 * 10 / (60 * 12 * 0.5),
            "scope": "Separate abstract operations example; omits supply and critical-path bounds.",
        },
        "repeated_cycle_retention": [retention(fraction, 100) for fraction in (0.99, 0.999)],
        "independent_event_sensitivities": [unresolved_events(p, 10000) for p in (0.001, 0.0001)],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run hand-computable checks before writing")
    args = parser.parse_args()
    if args.check:
        check()
        print("Checks passed: units, equilibrium, bottleneck ties, probability boundaries and input validation.")
    output = Path(__file__).with_name("results.json")
    data = results()
    output.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    for scenario in data["throughput_sensitivities"]:
        print(f"{scenario['id']}: {scenario['lower_bound_hours']:.3f} h lower bound "
              f"({', '.join(scenario['limiting_bounds'])})")


if __name__ == "__main__":
    main()
