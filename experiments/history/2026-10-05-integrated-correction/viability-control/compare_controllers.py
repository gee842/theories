"""Exploratory, resource-matched control comparison for a specified model."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
from itertools import product

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit, logit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent / "constitutional-extension/verify_extension.py"
spec = importlib.util.spec_from_file_location("viability_base", BASE)
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
P = base.Parameters()
OUT = ROOT / "results"
R, ALPHA, DELTA, MLOW = .5, 2., .02, .45
INITIAL = np.array([.94, .93, 2.7, 2.4, .5])
POLICIES = ["target", "slow", "fixed", "equilibrium_rule", "cap_0.6",
            "cap_0.7", "cap_0.8", "filtered"]
LABELS = {"target": "Target response", "slow": "Slower response", "fixed": "Fixed initial rule",
          "equilibrium_rule": "Move toward target / 6", "cap_0.6": "Fixed cap .6",
          "cap_0.7": "Fixed cap .7", "cap_0.8": "Fixed cap .8", "filtered": "State constraint filter"}


def plant(state):
    x, h, c, g, m = state
    q = (c / (1 + c)) ** 2
    r = 1 + .8 * q
    d = h * g / (1 + g)
    f = .15 * x * r
    v = .5 * f
    sx = .8 * q * d - .15 * r
    sh = 10 * v * (d - m)
    dx = x * (1 - x) * sx
    dh = h * (1 - h) * sh
    dc = P.eta_c * .5 * f - c
    dg = P.eta_g * m * h * v - g
    dd = g / (1 + g) * dh + h / (1 + g) ** 2 * dg
    return np.array([dx, dh, dc, dg]), sx, sh, d, dd


def margins(state):
    x, h, c, g, m = np.asarray(state)
    return np.array([x - .9, h - .9, c - 2.5, g - 2.1,
                     m - MLOW, h * g / (1 + g) - m - DELTA])


def control(state, policy, target, epsilon):
    _, _, _, d, dd = plant(state)
    m = state[4]
    nominal = epsilon * m * (1 - m) * (target - state[3])
    lo, hi = -R, R
    if policy == "fixed":
        return 0., nominal, lo, hi
    if policy == "slow":
        nominal /= 10
    elif policy == "equilibrium_rule":
        nominal = target / 6 - m
        lo = max(lo, -ALPHA * (m - MLOW))
        hi = min(hi, ALPHA * (1 - m))
    elif policy.startswith("cap_"):
        cap = float(policy.split("_")[1])
        lo = max(lo, -ALPHA * (m - MLOW))
        hi = min(hi, ALPHA * (cap - m))
    elif policy == "filtered":
        lo = max(lo, -ALPHA * (m - MLOW))
        hi = min(hi, dd + ALPHA * (d - m - DELTA))
    if lo > hi + 1e-10:
        raise ValueError(f"Infeasible controller interval {lo} > {hi}")
    return float(np.clip(nominal, lo, hi)), nominal, lo, hi


def decode(z):
    return np.array([expit(z[0]), expit(z[1]), np.exp(z[2]), np.exp(z[3]), z[4]])


def encode(state):
    return np.array([logit(state[0]), logit(state[1]), np.log(state[2]), np.log(state[3]), state[4]])


def simulate(policy, initial=INITIAL, schedule=((600., 4.),), epsilon=1., method="DOP853", step=.2, shock_at=None):
    initial = np.array(initial, dtype=float).copy()
    # Fixed comparator means keep the initial rule in grid comparisons; the
    # reference comparison begins at .5. It never resets m instantaneously.
    z0 = encode(initial)
    times, states, targets, controls, nominal_values = [], [], [], [], []
    offset = 0.
    shocks = []
    for duration, target in schedule:
        if shock_at is not None and abs(offset - shock_at) < 1e-9:
            before = decode(z0)
            z0[1] = min(z0[1], logit(.99))
            after = decode(z0)
            shocks.append({"time": offset, "before_h": float(before[1]), "after_h": float(after[1]),
                           "post_jump_in_certificate": bool(np.min(margins(after)) >= -1e-9)})
        def rhs(_t, z):
            state = decode(z)
            physical, sx, sh, _, _ = plant(state)
            u = control(state, policy, target, epsilon)[0]
            return [sx, sh, physical[2] / state[2], physical[3] / state[3], u]
        sol = solve_ivp(rhs, (0., duration), z0, method=method, rtol=2e-9, atol=2e-11,
                        dense_output=True, max_step=2.)
        if not sol.success:
            raise RuntimeError(sol.message)
        tt = np.linspace(0., duration, int(round(duration / step)) + 1)
        zz = sol.sol(tt)
        ss = decode(zz)
        uu = np.array([control(ss[:, i], policy, target, epsilon)[:2] for i in range(len(tt))])
        # Duplicate timestamps preserve both sides of a target switch; no
        # state or rule is reset at that switch.
        times.extend(tt + offset)
        states.extend(ss.T)
        targets.extend(np.full(len(tt), target))
        controls.extend(uu[:, 0])
        nominal_values.extend(uu[:, 1])
        z0 = sol.y[:, -1]
        offset += duration
    t = np.array(times)
    s = np.array(states).T
    target = np.array(targets)
    u = np.array(controls)
    nominal = np.array(nominal_values)
    mm = margins(s)
    fee = .15 * s[0] * (1 + .8 * (s[2] / (1 + s[2])) ** 2)
    # This is a special forward-invariant collapse box for the target-only
    # controller when every subsequent target is >1. It is not used for caps.
    loss = ((s[0] < 1) & (s[1] <= .1) & (s[2] <= 108 / 29) &
            (s[3] <= 1) & (s[4] >= .9))
    certified = np.flatnonzero(loss) if policy in ("target", "slow") and np.min(target) > 1 else []
    phase_errors = []
    start = 0.
    for duration, value in schedule:
        end = start + duration
        select = (t > end - min(30., duration / 5)) & (t <= end) & (target == value)
        phase_errors.append(float(np.max(np.abs(s[3, select] - value))))
        start = end
    summary = {
        "initial_x_h_C_G_m": initial.tolist(),
        "initial_certified": bool(np.min(margins(initial)) >= -1e-12),
        "final_x_h_C_G_m": s[:, -1].tolist(),
        "minimum_margins_x_h_C_G_m_b": mm.min(axis=1).tolist(),
        "operating_floor_breach": bool(np.min(mm[:4]) < -1e-6),
        "certificate_margin_breach": bool(np.min(mm) < -1e-6),
        "sampled_minimum_h": float(s[1].min()),
        "sampled_minimum_G": float(s[3].min()),
        "maximum_m": float(s[4].max()),
        "final_absolute_target_error": float(abs(s[3, -1] - target[-1])),
        "phase_late_max_target_errors": phase_errors,
        "rule_total_variation": float(np.trapezoid(np.abs(u), t)),
        "actuator_limit": R,
        "integrated_fee_revenue": float(np.trapezoid(fee, t)),
        "integrated_delivered_maintenance_expenditure": float(np.trapezoid(s[4] * s[1] * .5 * fee, t)),
        "imposed_practice_reintroductions": shocks,
        "maximum_absolute_u": float(np.max(np.abs(u))),
        "filter_deviation_integral_from_rate_limited_nominal": float(np.trapezoid(np.abs(u - np.clip(nominal, -R, R)), t)),
        "certified_loss_entry_sample": float(t[certified[0]]) if len(certified) else None,
        "final_operating_depletion_below_1e-6": bool(max(s[0, -1], s[2, -1], s[3, -1]) < 1e-6),
    }
    return {"t": t, "state": s, "target": target, "u": u, "summary": summary}


def algebra_checks():
    rng = np.random.default_rng(20261005)
    mismatch = 0.
    smallest_gap = 1e9
    for _ in range(2000):
        state = [rng.uniform(.9, .999), rng.uniform(.9, .999), rng.uniform(2.5, 10), rng.uniform(2.1, 10), .5]
        d = state[1] * state[3] / (1 + state[3])
        state[4] = rng.uniform(MLOW, d - DELTA)
        p = base.replace(P, work_fraction=state[4])
        mismatch = max(mismatch, float(np.max(np.abs(plant(state)[0] - base.physical_rhs(state[:4], p)))))
        _, _, lo, hi = control(state, "filtered", 10., 100.)
        smallest_gap = min(smallest_gap, hi - lo)
    assert mismatch < 1e-12
    dmin = .9 * 2.1 / 3.1
    x, h, c, g, m = .9, .9, 2.5, 2.1, .45
    pdot, sx, sh, _, _ = plant([x, h, c, g, m])
    gap_bound = -.25 + ALPHA * (dmin - DELTA - MLOW)
    assert min(pdot) > 0 and gap_bound > 0
    # Boundary impossibility: h at its floor and m>D makes hdot<0,
    # irrespective of any finite choice of u. A rate-limited rule cannot
    # prevent immediate exit from that particular h>=.9 requirement.
    outside = [.94, .9, 2.7, 2.4, .8]
    outside_hdot = float(plant(outside)[0][1])
    assert outside_hdot < 0
    # A clearly inconsistent actuator interval outside the sufficient set.
    inconsistent = [.5, .5, .5, .5, .45]
    caught = False
    try:
        control(inconsistent, "filtered", 4., 1.)
    except ValueError:
        caught = True
    assert caught
    upper = ((5 - 6 * DELTA) + np.sqrt((5 - 6 * DELTA) ** 2 - 24 * DELTA)) / 2
    return {"plant_max_difference_from_baseline": mismatch,
            "random_safe_states_checked": 2000, "smallest_sampled_controller_interval_width": smallest_gap,
            "analytical_raw_interval_gap_lower_bound": gap_bound,
            "lower_corner_operating_derivatives": pdot.tolist(),
            "minimum_user_selection_margin": sx,
            "maximum_clean_target_with_declared_buffer": float(upper),
            "boundary_impossibility_state": outside, "boundary_impossibility_hdot": outside_hdot,
            "outside_empty_interval_state": inconsistent, "outside_empty_interval_detected": caught}


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    proof = algebra_checks()
    cases = {"reference": {"schedule": [(600., 4.)], "epsilon": 1.},
             "fast_recovery_control": {"schedule": [(600., 3.6)], "epsilon": 10.},
             "changing_targets": {"schedule": [(150., v) for v in (4., 4.7, 3., 6., 4.)], "epsilon": 1.},
             "exploratory_reintroduction": {"schedule": [(150., v) for v in (4., 4.7, 3., 6., 4.)], "epsilon": 1., "shock_at": 450.}}
    trajectories = {}
    for name, arguments in cases.items():
        trajectories[name] = {}
        for policy in POLICIES:
            tr = simulate(policy, **arguments)
            trajectories[name][policy] = tr
            assert tr["summary"]["maximum_absolute_u"] <= R + 1e-9
            if policy == "filtered":
                assert not tr["summary"]["certificate_margin_breach"], (name, tr["summary"])
        print(json.dumps({"completed_case": name}), flush=True)
    grid = []
    for index, start in enumerate(product((.9, .94, .99), (.9, .95, .99), (2.5, 3.), (2.1, 3.), (.45, .5))):
        assert min(margins(start)) >= -1e-12
        entries = {}
        for policy in POLICIES:
            tr = simulate(policy, start, [(400., 4.7)], step=.5)
            entries[policy] = tr["summary"]
            if policy == "filtered":
                assert not tr["summary"]["certificate_margin_breach"], (start, tr["summary"])
        grid.append({"initial_x_h_C_G_m": list(start), "policies": entries})
        if (index + 1) % 12 == 0:
            print(json.dumps({"completed_grid_starts": index + 1}), flush=True)
    aggregate = {}
    for policy in POLICIES:
        ss = [row["policies"][policy] for row in grid]
        aggregate[policy] = {
            "number_of_starts": len(ss),
            "operating_floor_breaches": sum(v["operating_floor_breach"] for v in ss),
            "certificate_margin_breaches": sum(v["certificate_margin_breach"] for v in ss),
            "operating_depletions": sum(v["final_operating_depletion_below_1e-6"] for v in ss),
            "target_error_under_point_01": sum(v["phase_late_max_target_errors"][0] < .01 for v in ss),
            "worst_sampled_minimum_h": min(v["sampled_minimum_h"] for v in ss),
            "worst_sampled_minimum_G": min(v["sampled_minimum_G"] for v in ss),
            "max_rule_total_variation": max(v["rule_total_variation"] for v in ss),
        }
    independent = {}
    for name, policy in (("reference", "filtered"), ("reference", "target"), ("changing_targets", "filtered"), ("exploratory_reintroduction", "equilibrium_rule")):
        ref = simulate(policy, method="Radau", **cases[name])
        original = trajectories[name][policy]
        error = float(np.max(np.abs(original["state"] - ref["state"])))
        assert error < 2e-5, (name, policy, error)
        independent[f"{name}/{policy}"] = error
    result = {"scope": "Specified deterministic model; declared constraints; illustrative numerical comparisons, no empirical fitting.",
              "algebra_checks": proof, "design": {"rate_limit": R, "alpha": ALPHA, "incentive_buffer": DELTA, "minimum_m": MLOW},
              "cases": {name: {"arguments": cases[name], "policies": {p: tr["summary"] for p, tr in rows.items()}} for name, rows in trajectories.items()},
              "grid_aggregate": aggregate, "independent_solver_max_state_errors": independent,
              "base_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest(),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "protocol_sha256": hashlib.sha256((ROOT / "PROTOCOL.md").read_bytes()).hexdigest()}
    (OUT / "comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    (OUT / "grid.json").write_text(json.dumps(grid, indent=2) + "\n")
    np.savez_compressed(OUT / "trajectories.npz", **{f"{name}_{policy}_{key}": value for name, rows in trajectories.items() for policy, tr in rows.items() for key, value in tr.items() if isinstance(value, np.ndarray)})
    plot(trajectories)
    print(json.dumps({"complete": True, "grid_aggregate": aggregate, "solver_errors": independent}), flush=True)


def plot(trajectories):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout="constrained")
    colors = {"target": "#B24B42", "slow": "#9169A5", "fixed": "#777777", "cap_0.7": "#BB8B2F", "filtered": "#247B64", "equilibrium_rule": "#4267AE"}
    for policy in ("target", "slow", "fixed", "cap_0.7", "filtered"):
        tr = trajectories["reference"][policy]
        axes[0, 0].plot(tr["t"], tr["state"][3], color=colors[policy], label=LABELS[policy], lw=1.8)
        axes[0, 1].plot(tr["t"], tr["state"][1], color=colors[policy], label=LABELS[policy], lw=1.8)
    axes[0, 0].axhline(4, color="black", ls=":", lw=1)
    axes[0, 0].set(xlim=(0, 100), xlabel="Time", ylabel="Verification G", title="A. Recovery alone does not identify the best rule")
    axes[0, 0].legend(frameon=False, fontsize=8)
    axes[0, 1].axhline(.9, color="black", ls=":", lw=1, label="Declared floor")
    axes[0, 1].set(xlim=(0, 100), ylim=(0, 1.02), xlabel="Time", ylabel="Genuine maintenance share h", title="B. Protecting the conditions of maintenance")
    for policy in ("cap_0.7", "equilibrium_rule", "filtered"):
        tr = trajectories["changing_targets"][policy]
        axes[1, 0].plot(tr["t"], tr["state"][3], color=colors[policy], lw=1.8, label=LABELS[policy])
        axes[1, 1].plot(tr["t"], margins(tr["state"])[-1], color=colors[policy], lw=1.8, label=LABELS[policy])
    tr = trajectories["changing_targets"]["filtered"]
    axes[1, 0].plot(tr["t"], tr["target"], color="black", ls=":", lw=1.2, label="Requested target")
    axes[1, 0].set(xlabel="Time", ylabel="Verification G", title="C. Changing targets include an incompatible demand")
    axes[1, 0].legend(frameon=False, fontsize=8, loc="lower right")
    axes[1, 1].axhline(0, color="black", ls=":", lw=1)
    axes[1, 1].set(xlabel="Time", ylabel="Incentive margin above declared buffer", title="D. Target attainment and constraint preservation differ")
    fig.suptitle("Bounded rule revision under separate operating constraints", fontsize=16)
    fig.supxlabel("Specified model · same operating resources and actuator limit · governance and observations unpriced", fontsize=10)
    fig.savefig(OUT / "control-comparison.png", dpi=180)
    fig.savefig(OUT / "control-comparison.svg")
    plt.close(fig)


if __name__ == "__main__":
    run()
