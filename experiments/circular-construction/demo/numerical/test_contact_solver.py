"""Analytical contact cases, interface behavior and independently checked witnesses."""
import json
import math
from pathlib import Path
import subprocess
import sys
import unittest

from contact_solver import InvalidRequest, check_request


def contact(identifier, position, capacity=1000, kind="point", moment_capacity=0):
    result = {"id": identifier, "position_m": position, "kind": kind,
              "force_bounds_N": {"lower": [-capacity] * 3, "upper": [capacity] * 3}}
    if kind == "keyed":
        result["moment_bounds_Nm"] = {"lower": [-moment_capacity] * 3, "upper": [moment_capacity] * 3}
    return result


def request(contacts, mass=10, position=None):
    return {"schema_version": 1, "request_id": "analytic-case", "world_revision": 7, "input_fingerprint": "analytic-case-inputs-v1",
            "gravity_m_s2": [0, 0, -10],
            "loads": [{"id": "robot", "mass_kg": mass, "position_m": position or [0, 0, 0]}], "contacts": contacts}


class ContactCases(unittest.TestCase):
    def assert_equilibrium(self, source, result):
        # Intentionally separate implementation, moments expanded algebraically.
        totals = [0.0] * 6
        for load in source["loads"]:
            force = [load.get("mass_kg", 0) * source["gravity_m_s2"][j] + load.get("force_N", [0, 0, 0])[j] for j in range(3)]
            px, py, pz = load["position_m"]
            fx, fy, fz = force
            values = force + [py * fz - pz * fy, pz * fx - px * fz, px * fy - py * fx]
            for j in range(6):
                totals[j] += values[j] + (load.get("moment_Nm", [0, 0, 0])[j - 3] if j >= 3 else 0)
        by_id = {item["id"]: item for item in result["contact_wrenches"]}
        for anchor in source["contacts"]:
            item = by_id[anchor["id"]]
            fx, fy, fz = item["force_N"]
            mx, my, mz = item["moment_Nm"]
            px, py, pz = anchor["position_m"]
            contributions = [fx, fy, fz, py * fz - pz * fy + mx, pz * fx - px * fz + my, px * fy - py * fx + mz]
            for j in range(6):
                totals[j] += contributions[j]
            for component, reaction in zip(item["force_N"], item["frame_reaction_force_N"]):
                self.assertAlmostEqual(component, -reaction)
        self.assertLess(max(abs(value) for value in totals), 1e-6)

    def test_symmetric_vertical_reactions(self):
        source = request([contact("left", [-1, 0, 0]), contact("right", [1, 0, 0])])
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        self.assert_equilibrium(source, result)
        for item in result["contact_wrenches"]:
            self.assertAlmostEqual(item["force_N"][2], 50)

    def test_offset_tool_load_beam_reactions(self):
        source = request([contact("left", [-1, 0, 0]), contact("right", [1, 0, 0])], mass=0)
        source["loads"].append({"id": "tool", "mass_kg": 12, "position_m": [0.5, 0, 0]})
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        # Fleft+Fright=120; Fright-Fleft=60 => 30,90 N.
        self.assertAlmostEqual(result["contact_wrenches"][0]["force_N"][2], 30)
        self.assertAlmostEqual(result["contact_wrenches"][1]["force_N"][2], 90)
        self.assert_equilibrium(source, result)

    def test_signed_tension_needed(self):
        source = request([contact("left", [-1, 0, 0]), contact("right", [1, 0, 0])], position=[2, 0, 0])
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        self.assertAlmostEqual(result["contact_wrenches"][0]["force_N"][2], -50)
        self.assertAlmostEqual(result["contact_wrenches"][1]["force_N"][2], 150)
        self.assert_equilibrium(source, result)
        for item in source["contacts"]:
            item["force_bounds_N"]["lower"][2] = 0
        self.assertEqual(check_request(source)["status"], "failed")

    def test_aggregate_vertical_capacity(self):
        source = request([contact("left", [-1, 0, 0], capacity=49), contact("right", [1, 0, 0], capacity=49)])
        self.assertEqual(check_request(source)["status"], "failed")

    def test_three_collinear_point_anchors_cannot_resist_roll(self):
        source = request([contact(str(x), [x, 0, 0]) for x in (-1, 0, 1)], position=[0, 0.2, 0])
        # Any force at y=z=0 produces Mx=0. Robot weight produces -20 Nm.
        self.assertEqual(check_request(source)["status"], "failed")
        # Even infinite/unknown force capacity cannot remove the geometric mechanism.
        for item in source["contacts"]:
            item.pop("force_bounds_N")
        self.assertEqual(check_request(source)["status"], "failed")

    def test_keyed_couple_changes_geometric_result(self):
        source = request([contact(str(x), [x, 0, 0], kind="keyed", moment_capacity=10) for x in (-1, 0, 1)], position=[0, 0.2, 0])
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        self.assert_equilibrium(source, result)
        self.assertAlmostEqual(sum(x["moment_Nm"][0] for x in result["contact_wrenches"]), 20)
        for item in source["contacts"]:
            item["moment_bounds_Nm"]["upper"][0] = 6
        self.assertEqual(check_request(source)["status"], "failed")

    def test_triangle_with_noncollinear_anchors(self):
        source = request([contact("A", [0, 0, 0]), contact("B", [1, 0, 0]), contact("C", [0, 1, 0])], position=[0.25, 0.25, 0])
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        verticals = [item["force_N"][2] for item in result["contact_wrenches"]]
        self.assertEqual([round(x) for x in verticals], [50, 25, 25])
        self.assert_equilibrium(source, result)

    def test_unknown_capacity_never_passes(self):
        source = request([contact("left", [-1, 0, 0]), contact("right", [1, 0, 0])])
        source["contacts"][0]["force_bounds_N"]["upper"][2] = None
        result = check_request(source)
        self.assertEqual(result["status"], "unverified")
        self.assertIn("left.force_bounds_N.upper[2]", result["missing_capacities"])
        self.assert_equilibrium(source, result)

    def test_actuator_force_jacobian_and_gravity(self):
        source = request([contact("dock", [0, 0, 0])])
        source["require_actuator_limits"] = True
        source["actuator_constraints"] = [{"id": "shoulder", "gravity_torque_Nm": 3,
            "wrench_coefficients": [{"contact_id": "dock", "force_to_torque_m": [0, 0, 0.4]}], "lower_Nm": -50, "upper_Nm": 50}]
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        self.assertAlmostEqual(result["actuator_torques"][0]["torque_Nm"], 43)
        source["actuator_constraints"][0]["upper_Nm"] = 42
        self.assertEqual(check_request(source)["status"], "failed")

    def test_free_limb_constant_torque_rows(self):
        source = request([contact("dock", [0, 0, 0])])
        source["require_actuator_limits"] = True
        source["actuator_constraints"] = [{"id": "free-shoulder-x", "gravity_torque_Nm": 12,
            "wrench_coefficients": [], "lower_Nm": -15, "upper_Nm": 15}]
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        self.assertAlmostEqual(result["actuator_torques"][0]["torque_Nm"], 12)
        # No redistribution of support reactions can rescue an overloaded free arm.
        source["actuator_constraints"][0]["upper_Nm"] = 11
        self.assertEqual(check_request(source)["status"], "failed")
        source["actuator_constraints"][0]["upper_Nm"] = None
        self.assertEqual(check_request(source)["status"], "unverified")

    def test_robot_fixture_torque_norms_and_free_tool_arm(self):
        path = Path(__file__).with_name("fixtures") / "robot-task-guide-three-grip.request.json"
        source = json.loads(path.read_text())
        result = check_request(source)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(len(result["actuator_torques"]), 24)
        wrenches = {item["id"]: item for item in result["contact_wrenches"]}
        groups = {}
        for row in source["actuator_constraints"]:
            torque = row["gravity_torque_Nm"]
            for coefficient in row["wrench_coefficients"]:
                wrench = wrenches[coefficient["contact_id"]]
                torque += sum(a*b for a, b in zip(coefficient["force_to_torque_m"], wrench["force_N"]))
                torque += sum(a*b for a, b in zip(coefficient["moment_to_torque"], wrench["moment_Nm"]))
            groups.setdefault(row["id"].rsplit(":", 1)[0], []).append(torque)
            returned = next(item for item in result["actuator_torques"] if item["id"] == row["id"])
            self.assertAlmostEqual(torque, returned["torque_Nm"])
        for identifier, components in groups.items():
            limit = source["adapter_context"]["declared_shoulder_torque_limit_Nm" if identifier.endswith("shoulder") else "declared_elbow_torque_limit_Nm"]
            self.assertLessEqual(math.sqrt(sum(value*value for value in components)), limit + 1e-7)
        free_rows = [row for row in source["actuator_constraints"] if not row["wrench_coefficients"]]
        self.assertEqual(len(free_rows), 6)
        self.assertTrue(any(abs(row["gravity_torque_Nm"]) > 1 for row in free_rows))
        free_row = max(free_rows, key=lambda row: abs(row["gravity_torque_Nm"]))
        free_row["lower_Nm"], free_row["upper_Nm"] = -0.01, 0.01
        self.assertEqual(check_request(source)["status"], "failed")

    def test_missing_requested_actuator_limits(self):
        source = request([contact("dock", [0, 0, 0])])
        source["require_actuator_limits"] = True
        result = check_request(source)
        self.assertEqual(result["status"], "unverified")
        self.assertEqual(result["actuator_status"], "unverified")

    def test_zero_capacity_edge_case(self):
        source = request([contact("dock", [0, 0, 0], capacity=0)], mass=0)
        self.assertEqual(check_request(source)["status"], "passed")
        source["loads"][0]["mass_kg"] = 1
        self.assertEqual(check_request(source)["status"], "failed")

    def test_payload_digest_and_revision(self):
        source = request([contact("dock", [0, 0, 0])])
        first = check_request(source)
        self.assertEqual(first["request_id"], source["request_id"])
        self.assertEqual(first["world_revision"], 7)
        self.assertEqual(first["input_fingerprint"], source["input_fingerprint"])
        source["loads"][0]["mass_kg"] = 11
        self.assertNotEqual(check_request(source)["request_sha256"], first["request_sha256"])

    def test_invalid_point_couple_and_nonfinite_data(self):
        source = request([contact("dock", [0, 0, 0])])
        source["contacts"][0]["moment_bounds_Nm"] = {"lower": [-1] * 3, "upper": [1] * 3}
        with self.assertRaises(InvalidRequest):
            check_request(source)
        source["contacts"][0].pop("moment_bounds_Nm")
        source["loads"][0]["mass_kg"] = math.nan
        with self.assertRaises(InvalidRequest):
            check_request(source)

    def test_cli_stdin_stdout(self):
        source = request([contact("dock", [0, 0, 0])])
        completed = subprocess.run([sys.executable, str(Path(__file__).with_name("contact_solver.py"))], input=json.dumps(source), text=True, capture_output=True, check=True)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(completed.stderr, "")

    def test_cli_without_scipy_reports_unverified(self):
        source = request([contact("dock", [0, 0, 0])])
        completed = subprocess.run([sys.executable, "-S", str(Path(__file__).with_name("contact_solver.py"))], input=json.dumps(source), text=True, capture_output=True, check=True)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "unverified")
        self.assertEqual(result["solver"]["status"], "unavailable")
        self.assertEqual(result["required_aggregate_support_wrench"]["force_N"], [0, 0, 100])

    def test_invalid_cli_emits_json_and_nonzero(self):
        completed = subprocess.run([sys.executable, str(Path(__file__).with_name("contact_solver.py"))], input='{"schema_version":9}', text=True, capture_output=True)
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json.loads(completed.stdout)["status"], "unverified")

    def test_recorded_fixture_outcomes(self):
        root = Path(__file__).with_name("fixtures")
        for source_file in root.glob("*.request.json"):
            with self.subTest(fixture=source_file.name):
                source = json.loads(source_file.read_text())
                recorded = json.loads(source_file.with_name(source_file.name.replace(".request.", ".result.")).read_text())
                fresh = check_request(source)
                self.assertEqual(fresh["status"], recorded["status"])
                self.assertEqual(fresh["request_sha256"], recorded["request_sha256"])
                if fresh["contact_wrenches"]:
                    self.assert_equilibrium(source, fresh)


if __name__ == "__main__":
    unittest.main()
