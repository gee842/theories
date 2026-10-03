"""Generate the actual A/B fixture geometry, with explicitly assumed mechanics."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
from solver import DOFS, canonical_hash, solve_request, transfer_gate

HERE = Path(__file__).resolve().parent
DEMO = HERE.parent.parent
STUDY_CASES = (("A", None), ("B", None), ("A", "missing-restraint"),
               ("A", "missing-capture-roll"), ("A", "weak-member"))


def rhs(width, height, thickness):
    b, h, t = width, height, thickness
    return {"E_Pa": 200e9, "G_Pa": 200e9/2.6, "A_m2": b*h-(b-2*t)*(h-2*t),
            "Iy_m4": (b*h**3-(b-2*t)*(h-2*t)**3)/12,
            "Iz_m4": (h*b**3-(h-2*t)*(b-2*t)**3)/12,
            "J_m4": 4*((b-t)*(h-t))**2/(2*(b-t)/t+2*(h-t)/t)}


def chs(diameter, thickness):
    D, d = diameter, diameter-2*thickness
    I = math.pi*(D**4-d**4)/64
    return {"E_Pa": 200e9, "G_Pa": 200e9/2.6, "A_m2": math.pi*(D*D-d*d)/4,
            "Iy_m4": I, "Iz_m4": I, "J_m4": 2*I}


def make_fixture(fixture="A", negative=None):
    if fixture not in ("A", "B"):
        raise ValueError("fixture must be A or B")
    y_beam = 0 if fixture == "A" else 3
    source_files = ["src/view/site.ts", "src/connectors/bench.ts", "src/scenarios/beam.ts"]
    source_hashes = {p: hashlib.sha256((DEMO / p).read_bytes()).hexdigest() for p in source_files}
    nodes, members, supports, connections = [], [], [], []
    def node(name, position):
        nodes.append({"id": name, "position_m": position})
        return name
    def post(x, y, z): return f"post-{x}-{y}-{z:g}"
    def member(name, a, b, section, local_y, mass_per_m=None):
        members.append({"id": name, "a": a, "b": b, "section": deepcopy(section), "local_y": local_y,
                        "uniform_load_N_m": [0, 0, -9.81*(section["A_m2"]*7850 if mass_per_m is None else mass_per_m)],
                        "capacity": None})
    post_section, rail_section = rhs(.18, .18, .006), rhs(.15, .17, .006)
    brace_section, beam_section = chs(.11, .004), rhs(.146, .254, .005)
    # Extra nodes put diagonals and robot-load equivalent wrench at real elevations.
    elevations = [0, .15, 1.7, 2.8, 2.85, 3]
    for x in (0, 3):
        for y in (0, 3):
            for z in elevations: node(post(x, y, z), [x, y, z])
            supports.append({"id": f"base-{x}-{y}", "node": post(x, y, 0), "dofs": DOFS.copy(), "capacity": None})
            for lo, hi in zip(elevations, elevations[1:]):
                member(f"column-{x}-{y}-{lo:g}-{hi:g}", post(x,y,lo), post(x,y,hi), post_section, [0,1,0])
        member(f"longitudinal-rail-{x}", post(x,0,3), post(x,3,3), rail_section, [1,0,0])
        member(f"diagonal-rise-{x}", post(x,0,.15), post(x,3,2.85), brace_section, [1,0,0])
        member(f"diagonal-fall-{x}", post(x,3,.15), post(x,0,2.85), brace_section, [1,0,0])
    beam_x = [0, .09, .5, 1, 1.5, 2, 2.5, 2.91, 3]
    for x in beam_x: node(f"beam-{x:g}", [x, y_beam, 3.327])
    for a,b in zip(beam_x,beam_x[1:]):
        member(f"beam-{a:g}-{b:g}", f"beam-{a:g}", f"beam-{b:g}", beam_section, [0,1,0], 93.3/3)
    temporary = [1e7, 1e7, 1e7, 2e4, 0, 0]
    final = [1e8, 1e8, 1e8, 1e6, 1e6, 1e6]
    for x, bx in ((0,.09), (3,2.91)):
        connections.append({"id": f"seat-{x}", "a": post(x,y_beam,3), "b": f"beam-{bx:g}",
                            "stiffness": temporary.copy(), "capacity": None})
    contact_source = json.loads((HERE.parent / "fixtures/robot-task-guide-three-grip.request.json").read_text())
    contact_result = json.loads((HERE.parent / "fixtures/robot-task-guide-three-grip.result.json").read_text())
    if contact_result.get("request_sha256") != canonical_hash(contact_source):
        raise ValueError("representative contact witness is stale relative to its request")
    contacts = {c["id"]: c for c in contact_source["contacts"]}
    robot_loads = []
    # Use the existing admissible witness only as a representative imposed load.
    # Translate it to the second x-end; shift it to B if requested. Each remains 102 kg.
    for x in (0,3):
        for reaction in contact_result["contact_wrenches"]:
            px, py, pz = contacts[reaction["id"]]["position_m"]
            position = [px+x, py+y_beam, pz]
            robot_loads.append({"id": f"robot-at-{x}:"+reaction["id"], "node": post(x,y_beam,2.8 if pz>2 else 1.7),
                                "position_m": position, "force_N": reaction["frame_reaction_force_N"],
                                "moment_Nm": reaction["frame_reaction_moment_Nm"], "kind": "robot_grip_reaction"})
    stages = []
    for name, share, stiffness in (("temporary-capture", .8, temporary), ("final-joint", .8, final),
                                   ("hoist-handoff", .4, final), ("hoist-released", 0, final)):
        loads = deepcopy(robot_loads)
        for x, sign in ((.5,1), (2.5,-1)):
            vertical = 93.3*9.81*share/2
            loads.append({"id": f"sling-{x:g}", "node": f"beam-{x:g}", "position_m": [x,y_beam,3.487],
                          "force_N": [sign*vertical/.9, 0, vertical], "kind": "hoist_on_beam"})
        stages.append({"id": name, "hoist_weight_share": share, "loads": loads,
                       "connection_stiffness": {c["id"]: stiffness.copy() for c in connections}})
    request = {"schema_version": 1, "request_id": f"fixture-{fixture}-{negative or 'nominal'}", "world_revision": 10,
               "input_fingerprint": "pending", "nodes": nodes, "members": members, "supports": supports,
               "connections": connections, "stages": stages, "displacement_limit_m": .01, "rotation_limit_rad": .01,
               "characteristic_length_m": 3,
               "required_evidence": {"sections_and_materials": "assumed", "column_rail_brace_joints": "assumed",
                                     "seat_and_final_connections": "assumed", "foundation_restraint": "assumed",
                                     "robot_rail_local_strength": "unverified",
                                     "robot_actuator_limits": "assumed" if contact_result.get("actuator_status") == "included" else "unverified",
                                     "hoist_rigging_and_gantry": "unverified", "load_case_completeness": "unverified"},
               "fixture_metadata": {"fixture": fixture, "source_sha256": source_hashes,
                                    "contact_request_sha256": canonical_hash(contact_source),
                                    "contact_result_sha256": canonical_hash(contact_result),
                                    "contact_result_status": contact_result["status"],
                                    "contact_actuator_status": contact_result.get("actuator_status", "unverified"),
                                    "contact_actuator_row_count": len(contact_source.get("actuator_constraints", [])),
                                    "contact_capacity_source": contact_source.get("adapter_context", {}).get("capacity_source", "unknown"),
                                    "binding": "Independent numerical study, not bound to visible trace events or current world revision.",
                                    "beam_mass_kg": 93.3, "beam_centerline_z_m": 3.327,
                                    "assumptions": ["Rigid column/rail/brace member joints and fully fixed post bases.",
                                                    "Posts RHS180x180x6; rails RHS150x170x6; diagonals CHS110x4; beam RHS146x254x5, all assumed steel E=200GPa, nu=0.3.",
                                                    "Beam weight is actual scenario 93.3kg; other modeled members use assumed section area times 7850kg/m3. Local rails, heads and hardware weight omitted.",
                                                    "Seat springs use a rigid arm from head center to beam centerline. No seat contact/slip/uplift behavior is modeled.",
                                                    "Temporary capture assumes bilateral translation and a keyed global-X anti-roll spring, with global-Y/Z moments released.",
                                                    "Two copies of the existing 102kg robot grip witness impose frame reactions through rigid offsets; rail flexibility is excluded.",
                                                    "Sling attachment at x=.5/2.5,z=3.487, assumed rise .9m; opposite horizontal force components induce beam compression.",
                                                    "Hoist loads are prescribed, not deformation-dependent cable constraints. Gantry reactions are outside this frame model.",
                                                    "Independent stages are quasi-static snapshots; staged stress history and transient load transfer are excluded.",
                                                    "Displacement/rotation limits 10mm/0.01rad are screening assumptions, not design limits."]}}
    if negative == "missing-restraint": request["supports"] = []
    elif negative == "missing-capture-roll":
        for c in request["stages"][0]["connection_stiffness"].values(): c[3] = 0
    elif negative == "weak-member":
        for m in members:
            if m["id"].startswith("beam-"):
                m["capacity"] = {"provenance": "assumed", "limits": dict(zip(["N","Vy","Vz","T","My","Mz"], [1e6,1e6,1e6,1e6,1.,1e6]))}
    elif negative is not None: raise ValueError("unknown negative case")
    request["input_fingerprint"] = canonical_hash({k:v for k,v in request.items() if k != "input_fingerprint"})
    return request


def write_case(destination, request, result):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for suffix, value in (("request", request), ("result", result)):
        (destination / f"{request['request_id']}.{suffix}.json").write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")


def summarize_case(request, result):
    """Single source of truth for CLI and saved study summaries."""
    metadata = request["fixture_metadata"]
    return {"id": request["request_id"], "fixture": metadata["fixture"], "status": result["status"],
            "world_revision": request["world_revision"], "request_sha256": result["request_sha256"],
            "binding": metadata["binding"],
            "source_sha256": metadata["source_sha256"],
            "contact_request_sha256": metadata["contact_request_sha256"],
            "contact_result_sha256": metadata["contact_result_sha256"],
            "contact_result_status": metadata["contact_result_status"],
            "contact_actuator_status": metadata["contact_actuator_status"],
            "contact_actuator_row_count": metadata["contact_actuator_row_count"],
            "contact_capacity_source": metadata["contact_capacity_source"],
            "stages": [{"id": s["id"], "status": s["status"],
                        "max_nodal_translation_m": s.get("max_nodal_translation_m"),
                        "max_member_translation_m": s.get("max_member_translation_m"),
                        "max_member_rotation_rad": s.get("max_member_rotation_rad"),
                        "stability": {k:v for k,v in s["stability"].items() if k != "diagnostic_mode"},
                        "reason": s.get("reason"),
                        "max_equilibrium_residual": max(map(abs, s["global_equilibrium_residual"])) if "global_equilibrium_residual" in s else None,
                        "failed_capacity_ids": [c["id"] for c in s.get("capacity_checks", []) if c["status"] == "failed"]}
                       for s in result["stages"]],
            "transfer_gate": transfer_gate(request, result, request["world_revision"], request["input_fingerprint"])}


def generate_study(destination):
    """Regenerate every published case, stale gate and summary from current inputs."""
    destination = Path(destination)
    cases = []
    for fixture, negative in STUDY_CASES:
        request = make_fixture(fixture, negative)
        result = solve_request(request)
        summary = summarize_case(request, result)
        if cases:
            for key in ("source_sha256", "contact_request_sha256", "contact_result_sha256"):
                if summary[key] != cases[0][key]:
                    raise ValueError("source inputs changed while generating study; rerun")
        write_case(destination, request, result)
        cases.append(summary)
        if fixture == "A" and negative is None:
            stale = transfer_gate(request, result, request["world_revision"]+1, request["input_fingerprint"])
            (destination / "stale-input.gate.json").write_text(json.dumps(stale, indent=2)+"\n")
    study = {"scope": "Independent 3D beam-column linear-elastic numerical study. No visible trace event binding.",
             "physical_release_authorized": False, "cases": cases}
    (destination / "study-summary.json").write_text(json.dumps(study, indent=2, allow_nan=False)+"\n")
    return study


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", choices=["A", "B"])
    parser.add_argument("--negative", choices=["missing-restraint", "missing-capture-roll", "weak-member"])
    parser.add_argument("--write", help="output directory for generated JSON")
    parser.add_argument("--study", action="store_true", help="regenerate all five cases, stale gate and study-summary; defaults to adjacent fixtures directory")
    args = parser.parse_args()
    if args.study:
        if args.fixture or args.negative:
            parser.error("--study cannot be combined with --fixture or --negative")
        summary = generate_study(args.write or HERE / "fixtures")
    else:
        request = make_fixture(args.fixture or "A", args.negative)
        result = solve_request(request)
        if args.write: write_case(args.write, request, result)
        summary = summarize_case(request, result)
    print(json.dumps(summary, indent=2, allow_nan=False))

if __name__ == "__main__": main()
