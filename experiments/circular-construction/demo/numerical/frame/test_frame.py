"""Analytical benchmarks and regressions; only synthetic benchmark capacities verified."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import numpy as np
from solver import DOFS, InvalidRequest, canonical_hash, solve_request, transfer_gate
from fixture import DEMO, HERE, STUDY_CASES, generate_study, make_fixture, summarize_case


def capacity(keys):
    return {"provenance":"verified", "limits":dict.fromkeys(keys,1e12)}


def cantilever(force=None, moment=None, uniform=None, points=None):
    return {"schema_version":1, "request_id":"analytic", "world_revision":1, "input_fingerprint":"analytic-v1",
            "nodes":[{"id":"root","position_m": [0,0,0]}, {"id":"tip","position_m":points or [2,0,0]}],
            "members":[{"id":"bar","a":"root","b":"tip","local_y":[0,1,0],
                        "section":{"E_Pa":200e9,"G_Pa":80e9,"A_m2":.01,"Iy_m4":2e-5,"Iz_m4":3e-5,"J_m4":1e-5},
                        "uniform_load_N_m":uniform or [0,0,0],"capacity":capacity(["N","Vy","Vz","T","My","Mz"])}],
            "supports":[{"id":"base","node":"root","dofs":DOFS.copy(),"capacity":capacity(["Fx","Fy","Fz","Mx","My","Mz"])}],
            "stages":[{"id":"hoist-released","loads":[{"node":"tip","force_N":force or [0,0,0],"moment_Nm":moment or [0,0,0]}]}],
            "displacement_limit_m":1., "rotation_limit_rad":1.}


class AnalyticalCases(unittest.TestCase):
    def stage(self, request):
        result = solve_request(request)
        self.assertEqual(result["status"],"passed")
        stage = result["stages"][0]
        self.assertLess(max(map(abs,stage["global_equilibrium_residual"])),1e-6)
        return stage

    def test_cantilever_axial_biaxial_bending_torsion(self):
        # Independent closed-form axial FL/EA, torsion TL/GJ, bending FL³/3EI.
        r = self.stage(cantilever([100,200,-300],[400,0,0]))
        expected = [100*2/(200e9*.01),200*8/(3*200e9*3e-5),-300*8/(3*200e9*2e-5),
                    400*2/(80e9*1e-5),300*4/(2*200e9*2e-5),200*4/(2*200e9*3e-5)]
        np.testing.assert_allclose(r["displacements"]["tip"],expected,rtol=1e-12,atol=1e-15)
        np.testing.assert_allclose(r["support_reactions"][0]["wrench_global"],[-100,-200,300,-400,-600,-400],atol=1e-10)

    def test_cantilever_end_moments(self):
        r = self.stage(cantilever(moment=[0,100,200]))
        expected = [0,200*4/(2*200e9*3e-5),-100*4/(2*200e9*2e-5),0,100*2/(200e9*2e-5),200*2/(200e9*3e-5)]
        np.testing.assert_allclose(r["displacements"]["tip"],expected,atol=1e-15)

    def test_uniform_load_consistent_end_forces_and_deflection(self):
        r = self.stage(cantilever(uniform=[0,0,-1000]))
        self.assertAlmostEqual(r["displacements"]["tip"][2],-1000*2**4/(8*200e9*2e-5),12)
        self.assertAlmostEqual(r["displacements"]["tip"][4],1000*2**3/(6*200e9*2e-5),12)
        np.testing.assert_allclose(r["support_reactions"][0]["wrench_global"],[0,0,2000,0,-2000,0],atol=1e-8)
        self.assertAlmostEqual(r["member_forces"][0]["absolute_section_envelope"]["My"],2000,8)

    def test_simply_supported_uniform_internal_maximum(self):
        request = cantilever(uniform=[0,0,-1000])
        request["supports"][0]["dofs"] = ["ux","uy","uz","rx"]
        request["supports"].append({"id":"right","node":"tip","dofs":["uy","uz"],"capacity":capacity(["Fx","Fy","Fz","Mx","My","Mz"])})
        r = self.stage(request)
        self.assertAlmostEqual(r["member_forces"][0]["absolute_section_envelope"]["My"],1000*2**2/8,8)
        for support in r["support_reactions"]: self.assertAlmostEqual(support["wrench_global"][2],1000,8)
        # Nodes have zero translation, interior displacement must still be checked.
        self.assertEqual(r["max_nodal_translation_m"],0)
        self.assertAlmostEqual(r["max_member_translation_m"],5*1000*2**4/(384*200e9*2e-5),12)
        request["displacement_limit_m"] = r["max_member_translation_m"]*.9
        self.assertEqual(solve_request(request)["status"],"failed")

    def test_oblique_frame_rotation_invariance(self):
        source = cantilever([100,200,-300],[400,50,80],uniform=[0,0,-100])
        before = self.stage(source)
        a = .71; b=.39
        rz=np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1.]])
        ry=np.array([[np.cos(b),0,np.sin(b)],[0,1,0],[-np.sin(b),0,np.cos(b)]])
        Q=rz@ry
        source["nodes"][1]["position_m"]=(Q@np.array([2,0,0])).tolist()
        source["members"][0]["local_y"]=(Q@np.array([0,1,0])).tolist()
        source["members"][0]["uniform_load_N_m"]=(Q@np.array([0,0,-100])).tolist()
        load=source["stages"][0]["loads"][0]
        for k in ("force_N","moment_Nm"): load[k]=(Q@np.array(load[k])).tolist()
        after=self.stage(source)
        for offset in (0,3):
            np.testing.assert_allclose(after["displacements"]["tip"][offset:offset+3],Q@np.array(before["displacements"]["tip"][offset:offset+3]),rtol=1e-10,atol=1e-14)
        np.testing.assert_allclose(after["member_forces"][0]["local_end_wrenches"],before["member_forces"][0]["local_end_wrenches"],atol=1e-7)

    def test_eccentric_applied_force(self):
        source=cantilever([0,0,-100])
        source["stages"][0]["loads"][0]["position_m"]=[2,.5,0]
        r=self.stage(source)
        self.assertAlmostEqual(r["displacements"]["tip"][3],-50*2/(80e9*1e-5),12)

    def test_rigid_offset_connection_load_path(self):
        source=cantilever()
        source["nodes"].append({"id":"offset","position_m":[2,.5,0]})
        source["connections"]=[{"id":"spring","a":"tip","b":"offset","stiffness":[1e7]*6,"capacity":capacity(["Fx","Fy","Fz","Mx","My","Mz"])}]
        source["stages"][0]["loads"]=[{"node":"offset","force_N":[0,0,-100]}]
        r=self.stage(source)
        np.testing.assert_allclose(r["support_reactions"][0]["wrench_global"],[0,0,100,50,-200,0],atol=1e-8)
        self.assertAlmostEqual(r["connection_reactions"][0]["force_on_b_global"][2],100,8)


class SafetyCases(unittest.TestCase):
    def test_actual_fixture_A_and_B(self):
        for fixture in ("A","B"):
            source=make_fixture(fixture); r=solve_request(source)
            self.assertEqual(r["status"],"unverified")
            self.assertEqual(len(r["stages"]),4)
            for stage in r["stages"]:
                self.assertEqual(stage["stability"]["mechanism_or_near_mechanism_count"],0)
                self.assertEqual(stage["equilibrium_status"],"passed")
                self.assertTrue(stage["missing_evidence"])
                self.assertTrue(all(c["status"]=="unverified" for c in stage["capacity_checks"]))
            self.assertTrue(transfer_gate(source,r,source["world_revision"],source["input_fingerprint"])["block_transfer_load"])

    def test_saved_study_hashes_reactions_and_summary_are_current(self):
        contact_source=json.loads((HERE.parent/"fixtures/robot-task-guide-three-grip.request.json").read_text())
        contact_result=json.loads((HERE.parent/"fixtures/robot-task-guide-three-grip.result.json").read_text())
        study=json.loads((HERE/"fixtures/study-summary.json").read_text())
        self.assertEqual(len(study["cases"]),len(STUDY_CASES))
        for (fixture,negative), summary in zip(STUDY_CASES,study["cases"]):
            source=json.loads((HERE/"fixtures"/f"{summary['id']}.request.json").read_text())
            result=json.loads((HERE/"fixtures"/f"{summary['id']}.result.json").read_text())
            self.assertEqual(source,make_fixture(fixture,negative))
            self.assertEqual(result["request_sha256"],canonical_hash(source))
            metadata=source["fixture_metadata"]
            self.assertEqual(metadata["contact_request_sha256"],canonical_hash(contact_source))
            self.assertEqual(metadata["contact_result_sha256"],canonical_hash(contact_result))
            self.assertEqual(metadata["contact_actuator_row_count"],len(contact_source["actuator_constraints"]))
            for path,expected in metadata["source_sha256"].items():
                self.assertEqual(hashlib.sha256((DEMO/path).read_bytes()).hexdigest(),expected)
            self.assertEqual(summary,summarize_case(source,result))
            reactions={r["id"]:r for r in contact_result["contact_wrenches"]}
            for stage in source["stages"]:
                robot_loads=[load for load in stage["loads"] if load.get("kind")=="robot_grip_reaction"]
                self.assertEqual(len(robot_loads),2*len(reactions))
                for load in robot_loads:
                    reaction=reactions[load["id"].split(":",1)[1]]
                    self.assertEqual(load["force_N"],reaction["frame_reaction_force_N"])
                    self.assertEqual(load["moment_Nm"],reaction["frame_reaction_moment_Nm"])

    def test_study_generation_reproduces_all_published_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            study=generate_study(directory)
            generated=Path(directory)
            saved=HERE/"fixtures"
            self.assertEqual(sorted(p.name for p in generated.iterdir()),sorted(p.name for p in saved.glob("*.json")))
            for path in generated.iterdir():
                self.assertEqual(json.loads(path.read_text()),json.loads((saved/path.name).read_text()),path.name)
            self.assertEqual(study,json.loads((generated/"study-summary.json").read_text()))

    def test_no_support_is_mechanism_even_without_load(self):
        source=cantilever(); source["supports"]=[]
        stage=solve_request(source)["stages"][0]
        self.assertEqual(stage["status"],"failed")
        self.assertGreaterEqual(stage["stability"]["mechanism_or_near_mechanism_count"],6)
        self.assertNotIn("displacements",stage)

    def test_actual_missing_restraint_and_capture_roll(self):
        for case in ("missing-restraint","missing-capture-roll"):
            r=solve_request(make_fixture(negative=case))
            self.assertEqual(r["status"],"failed")
            self.assertGreater(r["stages"][0]["stability"]["mechanism_or_near_mechanism_count"],0)

    def test_weak_member_fails_despite_other_unknown_capacity(self):
        r=solve_request(make_fixture(negative="weak-member"))
        self.assertEqual(r["status"],"failed")
        self.assertTrue(any(c["status"]=="failed" for s in r["stages"] for c in s.get("capacity_checks",[])))

    def test_ill_conditioned_refuses_displacement_witness(self):
        source=cantilever([100,0,0]); source["members"][0]["section"]["J_m4"]=1e-15
        r=solve_request(source)
        self.assertNotEqual(r["status"],"passed")
        self.assertNotIn("displacements",r["stages"][0])

    def test_stale_revision_fingerprint_payload_and_stages(self):
        source=cantilever([10,0,0]); result=solve_request(source)
        self.assertTrue(transfer_gate(source,result,1,"analytic-v1")["numerical_gate_passed"])
        self.assertTrue(transfer_gate(source,result,2,"analytic-v1")["block_transfer_load"])
        self.assertTrue(transfer_gate(source,result,1,"changed")["block_transfer_load"])
        changed=deepcopy(source); changed["stages"][0]["loads"][0]["force_N"][0]=20
        self.assertIn("request_changed",transfer_gate(changed,result,1,"analytic-v1")["reasons"])
        missing=deepcopy(result); missing["stages"]=[]
        self.assertIn("stage_set_changed",transfer_gate(source,missing,1,"analytic-v1")["reasons"])

    def test_unknown_and_assumed_capacity_never_pass(self):
        for capacity_value in (None,{"provenance":"assumed","limits":dict.fromkeys(["N","Vy","Vz","T","My","Mz"],1e10)}):
            source=cantilever([1,0,0]); source["members"][0]["capacity"]=capacity_value
            self.assertEqual(solve_request(source)["status"],"unverified")

    def test_invalid_inputs(self):
        for mutation in (lambda r:r["nodes"].append(r["nodes"][0]),
                         lambda r:r["members"][0]["section"].update(E_Pa=-1),
                         lambda r:r["members"][0].update(local_y=[1,0,0]),
                         lambda r:r["supports"].append(deepcopy(r["supports"][0])),
                         lambda r:r["stages"][0]["loads"][0].update(force_N=[float("nan"),0,0])):
            source=cantilever(); mutation(source)
            with self.assertRaises(InvalidRequest): solve_request(source)

    def test_cli_stdin_and_hash_determinism(self):
        source=cantilever([1,0,0])
        process=subprocess.run([sys.executable,str(Path(__file__).with_name("solver.py"))],input=json.dumps(source),text=True,capture_output=True,check=True)
        self.assertEqual(json.loads(process.stdout),solve_request(source))
        self.assertEqual(canonical_hash(source),canonical_hash(dict(reversed(list(source.items())))))

if __name__ == "__main__": unittest.main()
