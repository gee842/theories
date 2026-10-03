"""Small-displacement 3D Euler–Bernoulli frame experiment, SI / engineering Z-up.

No buckling, geometric nonlinearity, local connection analysis or design-code claim.
All node DOFs: [ux, uy, uz, rx, ry, rz]. Rotations are radians, moments N m.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np

MODEL_VERSION = "linear-frame-1"
DOFS = ["ux", "uy", "uz", "rx", "ry", "rz"]
COMPONENTS = ["N", "Vy", "Vz", "T", "My", "Mz"]
SCOPE = ["Linear elastic Euler–Bernoulli bending, axial extension and Saint-Venant torsion only.",
         "No buckling, P-delta, dynamics, yielding, fatigue, shear deformation or warping torsion.",
         "No local rail, grip, bolt, seat, joint, foundation, soil or code-compliance validation.",
         "Springs are bilateral; loss of seat contact must be rejected by a separate contact validator."]

class InvalidRequest(ValueError):
    pass


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def vector(value, n, name):
    try:
        a = np.asarray(value, dtype=float)
    except (TypeError, ValueError) as exc:
        raise InvalidRequest(name + " must be numeric") from exc
    if a.shape != (n,) or not np.isfinite(a).all():
        raise InvalidRequest(name + f" must contain {n} finite numbers")
    return a


def positive(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise InvalidRequest(name + " must be positive and finite")
    return float(value)


def skew(v):
    x, y, z = v
    return np.array([[0, -z, y], [z, 0, -x], [-y, x, 0.]])


def axes(a, b, local_y):
    delta = b - a
    length = float(np.linalg.norm(delta))
    if length < 1e-8:
        raise InvalidRequest("zero-length frame member")
    x = delta / length
    y = vector(local_y, 3, "local_y")
    y = y - np.dot(x, y) * x
    if np.linalg.norm(y) < 1e-8:
        raise InvalidRequest("local_y parallel to member axis")
    y /= np.linalg.norm(y)
    return length, np.array([x, y, np.cross(x, y)])


def element_stiffness(length, section):
    """Local 12×12 matrix: local y bending uses Iz; local z bending uses Iy."""
    E, G, A, Iy, Iz, J = [positive(section.get(k), k) for k in ("E_Pa", "G_Pa", "A_m2", "Iy_m4", "Iz_m4", "J_m4")]
    L = length
    k = np.zeros((12, 12))
    for ids, rigidity in (([0, 6], E*A/L), ([3, 9], G*J/L)):
        k[np.ix_(ids, ids)] += rigidity * np.array([[1, -1], [-1, 1]])
    bending = np.array([[12, 6*L, -12, 6*L], [6*L, 4*L*L, -6*L, 2*L*L],
                        [-12, -6*L, 12, -6*L], [6*L, 2*L*L, -6*L, 4*L*L]])
    k[np.ix_([1, 5, 7, 11], [1, 5, 7, 11])] += E*Iz/L**3 * bending
    signs = np.diag([1., -1., 1., -1.])  # ry = -dw/dx
    k[np.ix_([2, 4, 8, 10], [2, 4, 8, 10])] += E*Iy/L**3 * signs @ bending @ signs
    return k


def uniform_equivalent(w, L):
    """Consistent local nodal loads for uniform local force/length, no couples."""
    f = np.zeros(12)
    f[:3] = f[6:9] = w*L/2
    f[4], f[10] = -w[2]*L*L/12, w[2]*L*L/12
    f[5], f[11] = w[1]*L*L/12, -w[1]*L*L/12
    return f


def member_envelope(q, w, L):
    # Internal section wrench acting on the left cut, derived by equilibrium.
    # N=-qi_x-wx*s; My=-qi_My-qi_Fz*s-wz*s²/2; Mz=-qi_Mz+qi_Fy*s+wy*s²/2.
    locations = [0., L]
    for force, load in ((q[1], w[1]), (q[2], w[2])):
        if abs(load) > 1e-14 and 0 < -force/load < L:
            locations.append(float(-force/load))
    values = []
    for s in locations:
        values.append([-q[0]-w[0]*s, -q[1]-w[1]*s, -q[2]-w[2]*s,
                       -q[3], -q[4]-q[2]*s-w[2]*s*s/2,
                       -q[5]+q[1]*s+w[1]*s*s/2])
    return dict(zip(COMPONENTS, np.max(np.abs(values), axis=0).tolist()))


def member_deformation(local_u, w, L, section):
    """Exact displacement polynomials for constant distributed loads; extrema of norm."""
    from numpy.polynomial import Polynomial as P
    xi = P([0., 1.]); one = P([1.])
    h1, h2 = 1-3*xi**2+2*xi**3, L*(xi-2*xi**2+xi**3)
    h3, h4 = 3*xi**2-2*xi**3, L*(-xi**2+xi**3)
    bubble = xi**2*(1-xi)**2
    E = section["E_Pa"]
    axial = local_u[0]*(one-xi)+local_u[6]*xi + w[0]*L**2/(2*E*section["A_m2"])*xi*(1-xi)
    v = h1*local_u[1]+h2*local_u[5]+h3*local_u[7]+h4*local_u[11]+w[1]*L**4/(24*E*section["Iz_m4"])*bubble
    z = h1*local_u[2]-h2*local_u[4]+h3*local_u[8]-h4*local_u[10]+w[2]*L**4/(24*E*section["Iy_m4"])*bubble
    twist = local_u[3]*(one-xi)+local_u[9]*xi
    maxima = []
    for polynomials in ([axial,v,z], [twist,-z.deriv()/L,v.deriv()/L]):
        squared = sum((p*p for p in polynomials), P([0.]))
        locations = [0., 1.]
        locations += [float(r.real) for r in squared.deriv().roots() if abs(r.imag)<1e-8 and 0<r.real<1]
        where = max(locations, key=lambda x: squared(x))
        maxima.append({"norm": math.sqrt(max(0., float(squared(where)))), "x_m": where*L})
    return {"translation": maxima[0], "rotation": maxima[1]}


def capacity_check(identifier, demand, capacity):
    """Conservative declared L1 interaction envelope; no inferred hardware strength."""
    missing, ratios = [], []
    limits = capacity.get("limits", {}) if isinstance(capacity, dict) else {}
    for key, value in demand.items():
        cap = limits.get(key)
        if cap is None:
            missing.append(key)
        else:
            ratios.append(abs(value) / positive(cap, identifier + ":" + key))
    utilization = sum(ratios)
    verified = isinstance(capacity, dict) and capacity.get("provenance") == "verified"
    status = "failed" if utilization > 1 + 1e-8 else "unverified" if missing or not verified else "passed"
    return {"id": identifier, "status": status, "known_component_interaction": utilization,
            "missing_components": missing, "capacity_provenance": capacity.get("provenance", "unknown") if capacity else "unknown"}


def validate(source):
    if source.get("schema_version") != 1 or not isinstance(source.get("request_id"), str):
        raise InvalidRequest("schema_version=1 and request_id required")
    if type(source.get("world_revision")) is not int or source["world_revision"] < 0:
        raise InvalidRequest("nonnegative integer world_revision required")
    if not isinstance(source.get("input_fingerprint"), str) or not source["input_fingerprint"]:
        raise InvalidRequest("input_fingerprint required")
    for field in ("nodes", "members", "stages"):
        if not isinstance(source.get(field), list) or not source[field]:
            raise InvalidRequest(field + " must be a nonempty list")
    for field in ("nodes", "members", "connections", "supports", "stages"):
        items = source.get(field, [])
        ids = [item.get("id") for item in items]
        if any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
            raise InvalidRequest(field + " needs unique nonempty IDs")
    node_ids = {n["id"] for n in source["nodes"]}
    connection_ids = {c["id"] for c in source.get("connections", [])}
    for n in source["nodes"]:
        vector(n.get("position_m"), 3, "position_m")
    for item in source["members"] + source.get("connections", []):
        if item.get("a") not in node_ids or item.get("b") not in node_ids or item["a"] == item["b"]:
            raise InvalidRequest("member/connection must reference distinct known nodes")
    restrained = set()
    for s in source.get("supports", []):
        if s.get("node") not in node_ids or not s.get("dofs") or any(d not in DOFS for d in s["dofs"]):
            raise InvalidRequest("invalid support")
        for d in s["dofs"]:
            key = (s["node"], d)
            if key in restrained:
                raise InvalidRequest("duplicate restrained DOF")
            restrained.add(key)
    for stage in source["stages"]:
        if set(stage.get("connection_stiffness", {})) - connection_ids:
            raise InvalidRequest("unknown stage connection")
        for load in stage.get("loads", []):
            if load.get("node") not in node_ids:
                raise InvalidRequest("unknown loaded node")
            vector(load.get("force_N", [0]*3), 3, "force_N")
            vector(load.get("moment_Nm", [0]*3), 3, "moment_Nm")
            if "position_m" in load:
                vector(load["position_m"], 3, "load position_m")
    positive(source.get("displacement_limit_m"), "displacement_limit_m")
    positive(source.get("rotation_limit_rad"), "rotation_limit_rad")
    # Also rejects NaN/Infinity anywhere in metadata and capacities.
    try:
        canonical_hash(source)
    except (ValueError, TypeError) as exc:
        raise InvalidRequest("request must be finite JSON") from exc


def solve_request(source):
    validate(source)
    nodes = {n["id"]: np.array(n["position_m"], dtype=float) for n in source["nodes"]}
    index = {name: np.arange(i*6, i*6+6) for i, name in enumerate(nodes)}
    ndof = 6*len(nodes)
    base_k, base_f = np.zeros((ndof, ndof)), np.zeros(ndof)
    elements = []
    for member in source["members"]:
        a, b = member["a"], member["b"]
        L, R = axes(nodes[a], nodes[b], member["local_y"])
        T = np.kron(np.eye(4), R)
        k = element_stiffness(L, member["section"])
        w = R @ vector(member.get("uniform_load_N_m", [0]*3), 3, "uniform_load_N_m")
        f = uniform_equivalent(w, L)
        ids = np.r_[index[a], index[b]]
        base_k[np.ix_(ids, ids)] += T.T @ k @ T
        base_f[ids] += T.T @ f
        elements.append((member, ids, L, T, k, w, f))
    fixed = sorted(index[s["node"]][DOFS.index(d)] for s in source.get("supports", []) for d in s["dofs"])
    free = np.array(sorted(set(range(ndof)) - set(fixed)), dtype=int)
    # Scale translations by characteristic length to compare rotational and translational DOFs.
    characteristic_length = positive(source.get("characteristic_length_m", 3.), "characteristic_length_m")
    scale = np.tile([characteristic_length]*3 + [1.]*3, len(nodes))
    reports = []
    for stage in source["stages"]:
        K, F = base_k.copy(), base_f.copy()
        springs = []
        for connection in source.get("connections", []):
            a, b = connection["a"], connection["b"]
            stiffness = vector(stage.get("connection_stiffness", {}).get(connection["id"], connection["stiffness"]), 6, "connection stiffness")
            if (stiffness < 0).any():
                raise InvalidRequest("spring stiffness cannot be negative")
            # Rigid offset on node a, global-axis relative spring at node b.
            B = np.zeros((6, 12)); B[:3, :3] = -np.eye(3); B[:3, 3:6] = skew(nodes[b]-nodes[a])
            B[:3, 6:9] = np.eye(3); B[3:, 3:6] = -np.eye(3); B[3:, 9:12] = np.eye(3)
            ids = np.r_[index[a], index[b]]
            C = np.diag(stiffness)
            K[np.ix_(ids, ids)] += B.T @ C @ B
            springs.append((connection, ids, B, C))
        applied = []
        for load in stage.get("loads", []):
            force = vector(load.get("force_N", [0]*3), 3, "force_N")
            position = vector(load.get("position_m", nodes[load["node"]]), 3, "position_m")
            moment = vector(load.get("moment_Nm", [0]*3), 3, "moment_Nm")
            nodal = np.r_[force, moment + np.cross(position-nodes[load["node"]], force)]
            F[index[load["node"]]] += nodal
            applied.append({**load, "equivalent_nodal_wrench": nodal.tolist()})
        report = {"id": stage["id"], "status": "unverified", "applied_loads": applied}
        if len(free):
            scaled = K[np.ix_(free, free)] * np.outer(scale[free], scale[free])
            eigenvalues, modes = np.linalg.eigh(scaled)
            largest = float(eigenvalues[-1]); smallest = float(eigenvalues[0])
            threshold = max(1e-10, largest * 1e-12)
            mechanism_count = int(np.count_nonzero(eigenvalues <= threshold))
            condition = largest/smallest if smallest > 0 else None
            report["stability"] = {"mechanism_or_near_mechanism_count": mechanism_count,
                                   "scaled_min_eigenvalue": smallest, "scaled_max_eigenvalue": largest,
                                   "scaled_condition_number": condition, "characteristic_length_m": characteristic_length,
                                   "rank_relative_tolerance": 1e-12, "condition_limit": 1e10}
            if mechanism_count or condition is None or condition > 1e10:
                mode = np.zeros(ndof); mode[free] = scale[free] * modes[:, 0]
                mode /= max(np.max(np.abs(mode)), 1e-300)
                report["stability"]["diagnostic_mode"] = {name: mode[ids].tolist() for name, ids in index.items()}
                report["status"] = "failed" if mechanism_count else "unverified"
                report["reason"] = "mechanism_or_numerically_unresolved_stiffness" if mechanism_count else "ill_conditioned"
                reports.append(report); continue
            u = np.zeros(ndof)
            u[free] = scale[free] * np.linalg.solve(scaled, F[free]*scale[free])
        else:
            u = np.zeros(ndof)
            report["stability"] = {"mechanism_or_near_mechanism_count": 0, "scaled_condition_number": 1.}
        residual = K @ u - F
        forces, checks, deformation = [], [], []
        for member, ids, L, T, k, w, f in elements:
            local_u = T @ u[ids]
            q = k @ local_u - f
            extrema = member_deformation(local_u, w, L, member["section"])
            deformation.append({"id": member["id"], **extrema})
            envelope = member_envelope(q, w, L)
            forces.append({"id": member["id"], "local_end_wrenches": q.tolist(), "absolute_section_envelope": envelope})
            checks.append(capacity_check("member:"+member["id"], envelope, member.get("capacity")))
        spring_forces = []
        for connection, ids, B, C in springs:
            demand = C @ B @ u[ids]
            spring_forces.append({"id": connection["id"], "relative_displacement": (B @ u[ids]).tolist(),
                                  "force_on_b_global": (-demand).tolist(), "force_on_a_at_a_global": (-B.T @ demand)[:6].tolist()})
            checks.append(capacity_check("connection:"+connection["id"], dict(zip(["Fx","Fy","Fz","Mx","My","Mz"], np.abs(demand))), connection.get("capacity")))
        reactions = []
        for support in source.get("supports", []):
            reaction = np.zeros(6)
            for d in support["dofs"]:
                j = DOFS.index(d); reaction[j] = residual[index[support["node"]][j]]
            reactions.append({"id": support["id"], "node": support["node"], "wrench_global": reaction.tolist()})
            checks.append(capacity_check("support:"+support["id"], dict(zip(["Fx","Fy","Fz","Mx","My","Mz"], np.abs(reaction))), support.get("capacity")))
        total = np.zeros(6)
        for name, ids in index.items():
            wrench = F[ids].copy()
            for j in range(6):
                if ids[j] in fixed:
                    wrench[j] += residual[ids[j]]
            total[:3] += wrench[:3]; total[3:] += wrench[3:] + np.cross(nodes[name], wrench[:3])
        max_disp = max(float(np.linalg.norm(u[ids[:3]])) for ids in index.values())
        max_rot = max(float(np.linalg.norm(u[ids[3:]])) for ids in index.values())
        relative_residual = float(np.max(np.abs(residual[free]*scale[free]), initial=0) / max(1., np.max(np.abs(F*scale))))
        equilibrium_ok = relative_residual < 1e-8 and np.max(np.abs(total)) < 1e-6 * max(1., np.max(np.abs(F)))
        max_member_disp = max(d["translation"]["norm"] for d in deformation)
        max_member_rot = max(d["rotation"]["norm"] for d in deformation)
        deformation_ok = max(max_disp, max_member_disp) <= source["displacement_limit_m"] and max(max_rot, max_member_rot) <= source["rotation_limit_rad"]
        evidence = source.get("required_evidence", {})
        missing_evidence = [key for key, status in evidence.items() if status != "verified"]
        status = "failed" if not deformation_ok or any(c["status"] == "failed" for c in checks) else "passed"
        if status == "passed" and (not equilibrium_ok or missing_evidence or any(c["status"] == "unverified" for c in checks)):
            status = "unverified"
        report.update(status=status, displacements={name: u[ids].tolist() for name, ids in index.items()},
                      max_nodal_translation_m=max_disp, max_nodal_rotation_rad=max_rot,
                      member_deformation_extrema=deformation, max_member_translation_m=max_member_disp, max_member_rotation_rad=max_member_rot,
                      deformation_status="passed" if deformation_ok else "failed", member_forces=forces,
                      connection_reactions=spring_forces, support_reactions=reactions, capacity_checks=checks,
                      missing_evidence=missing_evidence, relative_free_dof_residual=relative_residual,
                      global_equilibrium_residual=total.tolist(), equilibrium_status="passed" if equilibrium_ok else "unverified")
        reports.append(report)
    status = "failed" if any(s["status"] == "failed" for s in reports) else "unverified" if any(s["status"] == "unverified" for s in reports) else "passed"
    return {"schema_version": 1, "model_version": MODEL_VERSION, "request_id": source["request_id"],
            "world_revision": source["world_revision"], "input_fingerprint": source["input_fingerprint"],
            "request_sha256": canonical_hash(source), "status": status, "scope": SCOPE, "stages": reports,
            "numpy_version": np.__version__, "physical_release_authorized": False}


def transfer_gate(source, result, current_revision, current_fingerprint):
    """A necessary numerical gate, never sufficient physical release authorization."""
    reasons = []
    if result.get("request_sha256") != canonical_hash(source): reasons.append("request_changed")
    if result.get("model_version") != MODEL_VERSION: reasons.append("model_version_changed")
    if source.get("world_revision") != current_revision or result.get("world_revision") != current_revision: reasons.append("stale_world_revision")
    if source.get("input_fingerprint") != current_fingerprint or result.get("input_fingerprint") != current_fingerprint: reasons.append("stale_input_fingerprint")
    expected = [s["id"] for s in source["stages"]]
    if [s.get("id") for s in result.get("stages", [])] != expected: reasons.append("stage_set_changed")
    if "hoist-released" not in expected: reasons.append("missing_hoist_released_stage")
    if result.get("status") != "passed" or any(s.get("status") != "passed" for s in result.get("stages", [])): reasons.append("structural_model_not_passed")
    return {"numerical_gate_passed": not reasons, "block_transfer_load": bool(reasons), "reasons": reasons,
            "physical_release_authorized": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", nargs="?", help="JSON request path; stdin if omitted")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        source = json.loads(Path(args.request).read_text() if args.request else sys.stdin.read())
        result = solve_request(source)
    except (InvalidRequest, KeyError, TypeError, ValueError, np.linalg.LinAlgError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)})); return 2
    rendered = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output: Path(args.output).write_text(rendered)
    else: print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
