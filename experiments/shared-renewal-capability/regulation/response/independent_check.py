"""Independent block-exponential audit of the construction response.

Imports the earlier independent reaction reconstruction, never either producer.
Rebuilds exact integer generators on its own state order. No time quadrature is
used. Floating-point agreement is diagnostic, not a rigorous error enclosure.
"""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.sparse import bmat, coo_matrix
from scipy.sparse.linalg import expm_multiply

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ATOL = 1e-10
CAP = 48
HORIZON = 3.0
spec = importlib.util.spec_from_file_location(
    "independent_regulation_network", HERE.parent / "independent_check.py")
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
model.ARMS["conditional_baseline"] = (0, 4, 4)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs():
    primary = json.loads((HERE / "results.json").read_text())
    repair = json.loads((HERE / "protocol-link-repair.json").read_text())
    old = HERE / repair["preserved_original"]
    current = ROOT / repair["source_path_at_run"]
    assert sha(old) == repair["original_sha256"]
    assert sha(current) == repair["current_sha256"]
    before, after = repair["replacement"]["old"], repair["replacement"]["new"]
    assert old.read_bytes().count(before.encode()) == 1
    assert old.read_bytes().replace(before.encode(), after.encode()) == current.read_bytes()
    verified = {}
    for name, recorded in primary["source_sha256"].items():
        actual = ROOT / name
        if actual == current:
            assert recorded == sha(old)
            verified[name] = "as-run archived bytes verified; exact one-link repair verified"
        else:
            assert recorded == sha(actual), name
            verified[name] = "exact current bytes verified"
    assert primary["case"] == {"g": 8, "H": 3, "profile": [1, 1, 1]}
    paths = [HERE / "results.json", HERE / "decompose.py", HERE / "PROTOCOL.md",
             old, HERE / "protocol-link-repair.json", HERE.parent / "independent_check.py",
             HERE.parent / "compare.py", Path(__file__)]
    return primary, verified, {str(p.relative_to(ROOT)): sha(p) for p in paths}


def build_generator(states, index, arm):
    rows, cols, values = [], [], []
    event_count = 0
    for state in states:
        outgoing = defaultdict(int)
        if state is not None:
            for _, target, rate, _, _ in model.jumps(state, 8, arm):
                assert isinstance(rate, int) and rate > 0
                target = None if target[4] + target[6] > CAP else target
                assert target in index
                outgoing[index[target]] += rate
                event_count += 1
        i = index[state]
        assert i not in outgoing
        total = sum(outgoing.values())
        for j, rate in outgoing.items():
            rows.append(i); cols.append(j); values.append(rate)
        rows.append(i); cols.append(i); values.append(-total)
    q = coo_matrix((np.array(values, dtype=np.int64), (rows, cols)),
                   shape=(len(states), len(states))).tocsr()
    assert np.all(np.asarray(q.sum(axis=1)).ravel() == 0)
    return q, event_count


def assay(state):
    return int(state is not None and state[8] == 1 and state[9] == 1
               and state[4] >= 1 and sum(state[:3]) + state[7] >= 1)


def structural_checks(states, index, q0, q1, f):
    rows, cols, values = [], [], []
    src, dst = [], []
    last_plant = dead_face = baseline_events = 0
    for state in states:
        if state is None:
            continue
        r, c, y, d, fuel, gate, bound_fuel, bound_y = state[:8]
        a = r + c + y + bound_y
        regulator = gate + bound_fuel + bound_y
        total_gate_drift = 0
        for _, target, rate, _, _ in model.jumps(state, 8, "conditional_baseline"):
            baseline_events += 1
            total_gate_drift += rate * (target[5] + target[6] + target[7] - regulator)
            if a == 0:
                assert sum(target[:3]) + target[7] == 0
        assert total_gate_drift == -regulator
        if a == 0:
            dead_face += 1
        # Preparation-specific: an assembly or usable precursor must follow recycling.
        assert not state[9] or state[8]
        if r * fuel == 0:
            continue
        assert state[8] == 1
        target = (r-1, c, y, d, fuel-1, gate+1, bound_fuel, bound_y,
                  state[8], state[9], 1)
        assert target in index
        i, j = index[state], index[target]
        assert f[j] - f[i] <= 0
        assert model.dot(model.MATERIAL_WEIGHTS, target) == 3
        assert target[4] + target[6] == fuel + bound_fuel - 1
        assert model.dot(model.WORK_WEIGHTS, target) == model.dot(model.WORK_WEIGHTS, state) - 1
        assert sum(target[:3]) + target[7] == a - 1
        if a == 1:
            last_plant += 1
            assert sum(target[:3]) + target[7] == 0
        src.append(i); dst.append(j)
        rows.extend([i, i]); cols.extend([j, i]); values.extend([r*fuel, -r*fuel])
    b = coo_matrix((np.array(values, dtype=np.int64), (rows, cols)), shape=q0.shape).tocsr()
    difference = q1-q0-b
    difference.eliminate_zeros()
    assert difference.nnz == 0
    assert np.all(np.asarray(b.sum(axis=1)).ravel() == 0)
    return b, np.array(src), np.array(dst), {
        "construction_states": len(src), "last_productive_unit_construction_states": last_plant,
        "dead_plant_face_states": dead_face, "baseline_labeled_events": baseline_events,
        "generator_difference_nonzero_entries": difference.nnz,
        "status": "PASS exact integer generator, ledger, flag, dead-face and no-new-regulator checks"}


def main():
    started = time.monotonic()
    primary, verified_inputs, hashes = inputs()
    states, index, _, _ = model.graph(8, "responsive", CAP)
    q1, count1 = build_generator(states, index, "responsive")
    q0, count0 = build_generator(states, index, "conditional_baseline")
    f = np.array([assay(s) for s in states], dtype=float)
    b, src, dst, exact = structural_checks(states, index, q0, q1, f)
    n, initial = len(states), index[model.INITIAL]
    # Upper-right block of exp(H*A) is the Duhamel operator. A itself is
    # not a Markov generator: B includes negative diagonal entries.
    block = bmat([[q1, b], [None, q0]], format="csr")
    start = np.concatenate([np.zeros(n), f])
    block_result = expm_multiply(HORIZON*block, start,
        traceA=HORIZON*float(q1.diagonal().sum()+q0.diagonal().sum()))
    direct1 = expm_multiply(HORIZON*q1, f,
        traceA=HORIZON*float(q1.diagonal().sum()))
    net = float(block_result[initial])
    endpoint0 = float(block_result[n+initial])
    endpoint1 = float(direct1[initial])
    residual = net-(endpoint1-endpoint0)
    all_state_residual = float(np.max(np.abs(block_result[:n]-(direct1-block_result[n:]))))
    assert abs(residual) < ATOL and all_state_residual < ATOL
    saved = max((r for r in primary["runs"] if r["cap"] == CAP), key=lambda r:r["intervals"])
    assert len(states) == saved["states"] and len(src) == saved["construction_states"]
    comparison = {"endpoint_absent": endpoint0-saved["endpoint_absent"],
                  "endpoint_responsive": endpoint1-saved["endpoint_responsive"],
                  "endpoint_difference": net-saved["endpoint_difference"]}
    assert max(abs(v) for v in comparison.values()) < ATOL

    # One conditional check explains why initial overflow cannot certify a
    # near-cap local advantage. It does not redo the time-quadrature analysis.
    overflow = np.zeros(n); overflow[index[None]] = 1
    boundary_future = expm_multiply(q0, np.column_stack([f, overflow]),
                                  traceA=float(q0.diagonal().sum()))
    conditional_advantage = boundary_future[dst, 0]-boundary_future[src, 0]
    k = int(np.argmax(conditional_advantage))
    origin, target = int(src[k]), int(dst[k])
    delta = float(conditional_advantage[k])
    source_overflow = float(boundary_future[origin, 1])
    target_overflow = float(boundary_future[target, 1])
    local = {"remaining_time": 1., "state": states[origin], "constructed_state": states[target],
             "finite_conditional_advantage": delta,
             "source_conditional_overflow": source_overflow,
             "target_conditional_overflow": target_overflow,
             "untruncated_advantage_bracket_using_float_overflow":
                 [delta-source_overflow, delta+target_overflow],
             "scope": "Exact coupling formula with floating inputs, not a numerical certificate; no sign inferred for original process."}
    assert all(boundary_future[index[s], 0] == 0 for s in states
               if s is not None and sum(s[:3])+s[7] == 0)
    latest = max((r for r in primary["runs"] if r["cap"] == 64), key=lambda r:r["intervals"])
    reported = {"cap64_latest_intervals": latest["intervals"],
        "cap64_endpoint_difference": latest["endpoint_difference"],
        "cap64_integrated_positive": latest["integral_positive"],
        "cap64_quadrature_residual": latest["quadrature_identity_residual"],
        "cap48_primary_integral_minus_independent_block": saved["integral_net"]-net,
        "cap48_to64_endpoint_shift": latest["endpoint_difference"]-saved["endpoint_difference"],
        "last_productive_unit_group_fraction_of_net":
            latest["groups"]["A=1,C_present=0"]["net"]/latest["integral_net"],
        "all_cap64_group_nets_negative": all(v["net"] < 0 for v in latest["groups"].values()),
        "all_cap64_time_bin_nets_negative": all(v["net"] < 0 for v in latest["time_bins"]),
        "scope": "Saved primary decomposition inspected, not independently re-integrated."}
    assert reported["all_cap64_group_nets_negative"] and reported["all_cap64_time_bin_nets_negative"]
    output = {"status": "PASS", "scope": "Independent integer reconstruction and block-exponential net check; no independent sign-separated quadrature or interval arithmetic.",
        "git_head_at_check": subprocess.check_output(["git","rev-parse","HEAD"], cwd=ROOT,text=True).strip(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "source_sha256": hashes, "primary_input_audit": verified_inputs,
        "case": {"g":8,"H":HORIZON,"profile":[1,1,1],"cap":CAP},
        "states":n, "initial_index":initial, "labeled_events_Q0":count0,"labeled_events_Q1":count1,
        "exact_checks":exact,"absolute_comparison_tolerance":ATOL,
        "independent_block": {"baseline_success":endpoint0,"responsive_success":endpoint1,
            "net_Duhamel_response":net,"endpoint_identity_residual":residual,
            "maximum_all_state_identity_residual":all_state_residual,
            "differences_from_primary":comparison},
        "conditional_boundary_check":local,"primary_decomposition_readback":reported,
        "elapsed_seconds":time.monotonic()-started}
    (HERE/"independent-check.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":output["status"],"states":n,"block":output["independent_block"],
                      "boundary":local,"elapsed_seconds":output["elapsed_seconds"]},indent=2),flush=True)


if __name__ == "__main__":
    main()
