#!/usr/bin/env python3
"""Bounded quasi-static contact wrench feasibility. Python 3.11 + SciPy HiGHS.

The LP uses global-coordinate, signed Cartesian box limits. These are declared
contact capacity assumptions, never hardware qualification. Optional fixed-pose
actuator Jacobian rows constrain joint torques; they must be supplied by caller.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from typing import Any

MODEL_VERSION = "contact-box-static/1.0.0"


class InvalidRequest(ValueError):
    pass


def vector(value: Any, name: str) -> list[float]:
    if not isinstance(value, list) or len(value) != 3:
        raise InvalidRequest(f"{name} must be a three-element array")
    if any(isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x) for x in value):
        raise InvalidRequest(f"{name} must contain finite numbers")
    return [float(x) for x in value]


def cross(a: list[float], b: list[float]) -> list[float]:
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def bounds(value: Any, name: str, missing: list[str]) -> tuple[list[float | None], list[float | None]]:
    if value is None:
        missing.append(name)
        return [None] * 3, [None] * 3
    if not isinstance(value, dict):
        raise InvalidRequest(f"{name} must be an object or null")
    result = []
    for side in ("lower", "upper"):
        array = value.get(side)
        if array is None:
            missing.append(f"{name}.{side}")
            result.append([None] * 3)
            continue
        if not isinstance(array, list) or len(array) != 3:
            raise InvalidRequest(f"{name}.{side} must have three entries")
        validated: list[float | None] = []
        for index, item in enumerate(array):
            if item is None:
                missing.append(f"{name}.{side}[{index}]")
                validated.append(None)
            elif isinstance(item, bool) or not isinstance(item, (float, int)) or not math.isfinite(item):
                raise InvalidRequest(f"{name}.{side}[{index}] must be finite or null")
            else:
                validated.append(float(item))
        result.append(validated)
    lower, upper = result
    if any(lo is not None and hi is not None and lo > hi for lo, hi in zip(lower, upper)):
        raise InvalidRequest(f"{name} has a lower bound greater than its upper bound")
    return lower, upper


def check_request(request: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(request, dict) or type(request.get("schema_version")) is not int or request.get("schema_version") != 1:
        raise InvalidRequest("schema_version must be 1")
    if not isinstance(request.get("request_id"), str) or not request["request_id"]:
        raise InvalidRequest("request_id must be a nonempty string")
    revision = request.get("world_revision")
    if isinstance(revision, bool) or not isinstance(revision, int) or revision < 0:
        raise InvalidRequest("world_revision must be a nonnegative integer")
    fingerprint = request.get("input_fingerprint")
    if not isinstance(fingerprint, str) or not fingerprint:
        raise InvalidRequest("input_fingerprint must be a nonempty string supplied by caller")
    gravity = vector(request.get("gravity_m_s2", [0, 0, -9.81]), "gravity_m_s2")
    external = [0.0] * 6
    loads = request.get("loads")
    if not isinstance(loads, list):
        raise InvalidRequest("loads must be an array")
    for index, load in enumerate(loads):
        if not isinstance(load, dict):
            raise InvalidRequest(f"loads[{index}] must be an object")
        mass = load.get("mass_kg", 0)
        if isinstance(mass, bool) or not isinstance(mass, (float, int)) or not math.isfinite(mass) or mass < 0:
            raise InvalidRequest(f"loads[{index}].mass_kg must be finite and nonnegative")
        position = vector(load.get("position_m"), f"loads[{index}].position_m")
        applied = vector(load.get("force_N", [0, 0, 0]), f"loads[{index}].force_N")
        force = [mass * gravity[j] + applied[j] for j in range(3)]
        applied_moment = vector(load.get("moment_Nm", [0, 0, 0]), f"loads[{index}].moment_Nm")
        moment = cross(position, force)
        for j in range(3):
            external[j] += force[j]
            external[j + 3] += moment[j] + applied_moment[j]

    raw_contacts = request.get("contacts")
    if not isinstance(raw_contacts, list) or not raw_contacts:
        raise InvalidRequest("contacts must be a nonempty array")
    if len(raw_contacts) > 32:
        raise InvalidRequest("initial harness supports at most 32 contacts")
    missing: list[str] = []
    contacts = []
    contact_ids = set()
    for index, contact in enumerate(raw_contacts):
        if not isinstance(contact, dict) or not isinstance(contact.get("id"), str) or not contact["id"]:
            raise InvalidRequest(f"contacts[{index}].id must be a nonempty string")
        if contact["id"] in contact_ids:
            raise InvalidRequest("contact IDs must be unique")
        contact_ids.add(contact["id"])
        kind = contact.get("kind")
        if kind not in ("point", "keyed"):
            raise InvalidRequest(f"contacts[{index}].kind must be point or keyed")
        position = vector(contact.get("position_m"), f"contacts[{index}].position_m")
        lo_f, hi_f = bounds(contact.get("force_bounds_N"), f"{contact['id']}.force_bounds_N", missing)
        if kind == "point":
            if contact.get("moment_bounds_Nm") is not None:
                supplied_lo, supplied_hi = bounds(contact["moment_bounds_Nm"], f"{contact['id']}.moment_bounds_Nm", [])
                if supplied_lo != [0, 0, 0] or supplied_hi != [0, 0, 0]:
                    raise InvalidRequest("point contacts have zero couple capacity; omit moment_bounds_Nm or set exact zeros")
            lo_m, hi_m = [0.0] * 3, [0.0] * 3
        else:
            lo_m, hi_m = bounds(contact.get("moment_bounds_Nm"), f"{contact['id']}.moment_bounds_Nm", missing)
        contacts.append({"id": contact["id"], "position": position, "lower": lo_f + lo_m, "upper": hi_f + hi_m, "kind": kind})

    # Split every free wrench coordinate into positive and negative LP variables.
    # Fixed zero dimensions are omitted (including all point-contact moments).
    columns: list[list[float]] = []
    variables: list[tuple[int, int]] = []
    for i, contact in enumerate(contacts):
        for axis in range(6):
            if contact["lower"][axis] == 0 and contact["upper"][axis] == 0:
                continue
            column = [0.0] * 6
            column[axis] = 1.0
            if axis < 3:
                unit = [0.0] * 3
                unit[axis] = 1.0
                column[3:] = cross(contact["position"], unit)
            columns.append(column)
            variables.append((i, axis))
    n = len(columns) * 2
    a: list[list[float]] = []
    b: list[float] = []
    for axis in range(6):
        row = [sign * col[axis] for col in columns for sign in (1, -1)]
        a.extend([row, [-x for x in row]])
        b.extend([-external[axis], external[axis]])
    for j, (i, axis) in enumerate(variables):
        lo, hi = contacts[i]["lower"][axis], contacts[i]["upper"][axis]
        row = [0.0] * n
        row[2 * j], row[2 * j + 1] = 1.0, -1.0
        if hi is not None:
            a.append(row)
            b.append(hi)
        if lo is not None:
            a.append([-x for x in row])
            b.append(-lo)
    raw_actuators = request.get("actuator_constraints", [])
    if not isinstance(raw_actuators, list):
        raise InvalidRequest("actuator_constraints must be an array")
    require_actuators = request.get("require_actuator_limits", False)
    if not isinstance(require_actuators, bool):
        raise InvalidRequest("require_actuator_limits must be boolean")
    if require_actuators and not raw_actuators:
        missing.append("actuator_constraints")
    actuators = []
    actuator_ids = set()
    for index, actuator in enumerate(raw_actuators):
        if not isinstance(actuator, dict) or not isinstance(actuator.get("id"), str) or not actuator["id"]:
            raise InvalidRequest(f"actuator_constraints[{index}].id must be a nonempty string")
        if actuator["id"] in actuator_ids:
            raise InvalidRequest("actuator IDs must be unique")
        actuator_ids.add(actuator["id"])
        gravity_torque = actuator.get("gravity_torque_Nm", 0)
        if isinstance(gravity_torque, bool) or not isinstance(gravity_torque, (int, float)) or not math.isfinite(gravity_torque):
            raise InvalidRequest("gravity_torque_Nm must be finite")
        coefficients = actuator.get("wrench_coefficients")
        if not isinstance(coefficients, list):
            raise InvalidRequest("actuator wrench_coefficients must be an array (empty for a constant free-limb row)")
        coefficient_by_contact = {}
        for coefficient in coefficients:
            if not isinstance(coefficient, dict) or not isinstance(coefficient.get("contact_id"), str) or coefficient.get("contact_id") not in contact_ids:
                raise InvalidRequest("actuator coefficient must reference an existing contact")
            contact_id = coefficient["contact_id"]
            if contact_id in coefficient_by_contact:
                raise InvalidRequest("actuator coefficient contact IDs must be unique per actuator")
            coefficient_by_contact[contact_id] = vector(coefficient.get("force_to_torque_m"), "force_to_torque_m") + vector(coefficient.get("moment_to_torque", [0, 0, 0]), "moment_to_torque")
        torque_bounds = []
        for side in ("lower_Nm", "upper_Nm"):
            value = actuator.get(side)
            if value is None:
                missing.append(f"{actuator['id']}.{side}")
            elif isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise InvalidRequest(f"{actuator['id']}.{side} must be finite or null")
            torque_bounds.append(value)
        lo, hi = torque_bounds
        if lo is not None and hi is not None and lo > hi:
            raise InvalidRequest("actuator lower_Nm must not exceed upper_Nm")
        row = [0.0] * n
        for j, (i, axis) in enumerate(variables):
            value = coefficient_by_contact.get(contacts[i]["id"], [0.0] * 6)[axis]
            row[2 * j], row[2 * j + 1] = value, -value
        if hi is not None:
            a.append(row)
            b.append(hi - gravity_torque)
        if lo is not None:
            a.append([-value for value in row])
            b.append(gravity_torque - lo)
        actuators.append({"id": actuator["id"], "coefficients": coefficient_by_contact, "gravity_torque": gravity_torque, "lower": lo, "upper": hi})
    if not all(math.isfinite(value) for value in external + b):
        raise InvalidRequest("request produced nonfinite wrench values")
    # Dimensionally explicit normalization only selects a witness. It is not a
    # structural objective, hardware design optimum, or individual capacity minimum.
    c = [1.0] * n
    payload = {key: request[key] for key in ("schema_version", "request_id", "world_revision", "input_fingerprint")}
    payload.update({
        "model_version": MODEL_VERSION,
        "request_sha256": hashlib.sha256(json.dumps(request, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest(),
        "scope": "quasi-static global Cartesian box contact wrench equilibrium",
        "solver": {"name": "scipy-highs"},
        "external_wrench": {"force_N": external[:3], "moment_Nm": external[3:]},
        "required_aggregate_support_wrench": {"force_N": [-v for v in external[:3]], "moment_about_origin_Nm": [-v for v in external[3:]]},
        "actuator_status": "included" if actuators else "unverified" if require_actuators else "outside_scope",
        "missing_capacities": missing,
        "limitations": [
            "Capacity numbers remain declared assumptions; no hardware qualification is performed.",
            "Box bounds do not model coupled friction, clamp closure, stiffness or slip.",
            "Actuator torques use supplied fixed-pose Jacobian rows only; absent rows are outside scope or unverified when requested.",
            "Kinematics, collisions, frame reactions adequacy and dynamics are outside this check.",
            "Missing limits are relaxed only to produce a required-wrench witness; they cannot produce a passed result.",
            "Minimum normalized L1 witness uses 1 N and 1 N m scales; it is not a per-contact capacity optimum.",
        ],
    })
    try:
        import numpy as np
        import scipy
        from scipy.optimize import linprog
    except ImportError:
        payload.update({"status": "unverified", "contact_wrenches": [], "equilibrium_residual": None,
                        "reason": "SciPy unavailable; required aggregate wrench reported without a feasibility claim."})
        payload["solver"]["status"] = "unavailable"
        return payload
    payload["solver"].update({"scipy_version": scipy.__version__, "numpy_version": np.__version__})
    if n == 0:
        solver_status = "feasible" if all(rhs >= -1e-9 for rhs in b) else "infeasible"
        x = [] if solver_status == "feasible" else None
    else:
        solution = linprog(c, A_ub=a, b_ub=b, bounds=[(0, None)] * n, method="highs",
                           options={"primal_feasibility_tolerance": 1e-9, "dual_feasibility_tolerance": 1e-9})
        solver_status = "feasible" if solution.success else "infeasible" if solution.status == 2 else "numerical_error"
        x = solution.x.tolist() if solution.success else None
        payload["solver"].update({"highs_status": int(solution.status), "message": solution.message})
    payload["solver"]["status"] = solver_status
    if solver_status != "feasible":
        payload.update({"status": "failed" if solver_status == "infeasible" else "unverified", "contact_wrenches": [], "equilibrium_residual": None,
                        "reason": "No equilibrium exists within declared contact geometry and known bounds." if solver_status == "infeasible" else "Numerical solver did not supply a checked witness."})
        return payload
    assert x is not None
    wrenches = [[0.0] * 6 for _ in contacts]
    for j, (i, axis) in enumerate(variables):
        wrenches[i][axis] = x[2 * j] - x[2 * j + 1]
    residual = external.copy()
    max_violation = 0.0
    actuator_torques = []
    for contact, wrench in zip(contacts, wrenches):
        moment = cross(contact["position"], wrench[:3])
        for j in range(3):
            residual[j] += wrench[j]
            residual[j + 3] += moment[j] + wrench[j + 3]
        for j, value in enumerate(wrench):
            lo, hi = contact["lower"][j], contact["upper"][j]
            max_violation = max(max_violation, (lo - value) if lo is not None else 0, (value - hi) if hi is not None else 0)
    for actuator in actuators:
        torque = actuator["gravity_torque"]
        for contact, wrench in zip(contacts, wrenches):
            coefficients = actuator["coefficients"].get(contact["id"], [0.0] * 6)
            torque += sum(coefficient * value for coefficient, value in zip(coefficients, wrench))
        lo, hi = actuator["lower"], actuator["upper"]
        max_violation = max(max_violation, lo - torque if lo is not None else 0, torque - hi if hi is not None else 0)
        actuator_torques.append({"id": actuator["id"], "torque_Nm": torque, "lower_Nm": lo, "upper_Nm": hi})
    tolerance = 1e-7
    witness_valid = all(math.isfinite(v) and abs(v) <= tolerance for v in residual) and max_violation <= tolerance
    payload.update({
        "status": ("unverified" if missing else "passed") if witness_valid else "unverified",
        "reason": "Equilibrium witness checked under declared limits." if witness_valid and not missing else "Equilibrium witness needs missing capacities." if witness_valid else "Independent residual check rejected the numerical witness.",
        "contact_wrenches": [{"id": contact["id"], "force_N": wrench[:3], "moment_Nm": wrench[3:],
                              "frame_reaction_force_N": [-v for v in wrench[:3]], "frame_reaction_moment_Nm": [-v for v in wrench[3:]]}
                             for contact, wrench in zip(contacts, wrenches)],
        "equilibrium_residual": {"force_N": residual[:3], "moment_Nm": residual[3:], "max_abs": max(abs(v) for v in residual)},
        "max_bound_violation": max_violation,
        "actuator_torques": actuator_torques,
        "numerical_tolerance": {"force_N": tolerance, "moment_Nm": tolerance},
    })
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", nargs="?", help="JSON request file, otherwise stdin")
    parser.add_argument("--output", help="result JSON file, otherwise stdout")
    args = parser.parse_args()
    try:
        if args.request:
            with open(args.request, encoding="utf-8") as source:
                request = json.load(source)
        else:
            request = json.load(sys.stdin)
        result = check_request(request)
        exit_status = 0
    except (InvalidRequest, ValueError, KeyError, ArithmeticError) as error:
        result = {"schema_version": 1, "model_version": MODEL_VERSION, "status": "unverified", "error": str(error)}
        exit_status = 2
    serialized = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as target:
            target.write(serialized)
    else:
        sys.stdout.write(serialized)
    return exit_status


if __name__ == "__main__":
    raise SystemExit(main())
