#!/usr/bin/env python3
"""Secondary analysis of deposited human observations; no simulated participants.

The MCOS reader is specific to this deposit, with redundant-table agreement
and experiment-schedule checks. It is not a general MATLAB table decoder.
"""
import hashlib
import io
import itertools
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.io import loadmat
from scipy.io.matlab._mio5 import MatFile5Reader
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").exists())
SOURCE = ROOT / "sources/situated-recovery/heald-2021"
GROUPS = ("spontaneous_recovery", "evoked_recovery")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def read_table(d):
    opaque = d["None"]
    assert opaque["s0"][0] == b"TrialData" and opaque["s2"][0] == b"table"
    workspace = d["__function_workspace__"].tobytes()
    assert workspace[:4] == b"\x00\x01IM"
    reader = MatFile5Reader(io.BytesIO(workspace), byte_order="<",
                           struct_as_record=False, squeeze_me=True)
    reader.initialize_read()
    reader.mat_stream.seek(8)
    header, _ = reader.read_var_header()
    cells = reader.read_var_array(header).MCOS["arr"][0]
    candidates = []
    for i in range(2, len(cells) - 5):
        names, values = cells[i + 5], cells[i]
        if not (isinstance(names, np.ndarray) and names.dtype == object
                and all(isinstance(x, str) for x in names)):
            continue
        if "Adaptation" not in names:
            continue
        assert int(cells[i + 4]) == len(names) == len(values)
        table = dict(zip(names, values))
        assert all(len(v) == int(cells[i + 2]) for v in table.values())
        candidates.append(table)
    assert len(candidates) >= 2
    common = set.intersection(*(set(t) for t in candidates))
    required = {"BlockName", "TrialNumber", "FieldConstants", "FieldType", "MissTrial", "Adaptation"}
    assert required <= common
    for key in common:
        first = candidates[0][key]
        for t in candidates[1:]:
            if first.dtype == object:
                assert np.array_equal(first, t[key]), key
            else:
                np.testing.assert_equal(first, t[key])
    return {k: candidates[0][k] for k in required}, len(candidates)


def extract():
    metadata = json.loads((SOURCE / "selected-files.json").read_text())
    assert len(metadata) == 16
    rows, audits = [], []
    for m in sorted(metadata, key=lambda x: x["path"]):
        path = SOURCE / "originals" / m["path"]
        assert path.stat().st_size == m["size"] and sha(path) == m["digest"]
        group = next(g for g in GROUPS if path.name.startswith(g))
        participant = int(path.stem.split("participant")[1])
        d = loadmat(path, simplify_cells=True)
        t, copies = read_table(d)
        n = len(t["TrialNumber"])
        assert n == len(d["Frames"])
        trials = t["TrialNumber"].astype(int)
        assert np.array_equal(trials, np.arange(1, 341))
        assert not np.any(t["MissTrial"]), "Reconcile missed rows before analysis"
        mask = np.isfinite(t["Adaptation"])
        assert np.array_equal(mask, t["FieldType"] == 2)
        direction = np.sign(t["FieldConstants"][np.flatnonzero(t["BlockName"] == "FieldA")[0], 0])
        assert direction in (-1, 1)
        assert sum(mask) == (167 if group == GROUPS[0] else 165)
        terminal_start = 191 if group == GROUPS[0] else 195
        assert np.all(mask[terminal_start - 1:])
        assert sum(mask & (t["BlockName"] == "Null")) == 5
        errors = []
        for i in range(n):
            adapted = float(t["Adaptation"][i] * direction) if mask[i] else None
            reconstructed = None
            if mask[i]:
                # Exploratory reconstruction: opposite wall force, forward
                # velocity >1 cm/s. The README does not specify every window.
                velocity = d["RobotVelocity"][i, 1]
                valid = (velocity > 1) & np.isfinite(d["RobotForces"][i, 0])
                ideal = .15 * velocity[valid]
                force = -d["RobotForces"][i, 0, valid]
                assert len(ideal) and np.dot(ideal, ideal) > 0
                reconstructed = float(direction * np.dot(force, ideal) / np.dot(ideal, ideal))
                errors.append(reconstructed - adapted)
            rows.append({"group": group, "participant": participant, "trial": int(trials[i]),
                         "block": str(t["BlockName"][i]), "field_type": int(t["FieldType"][i]),
                         "field_gain": float(t["FieldConstants"][i, 0]),
                         "field_a_direction": int(direction), "adaptation": adapted,
                         "forward_velocity_reconstruction": reconstructed})
        audits.append({"file": path.name, "sha256": sha(path), "rows": n,
                       "finite_channel_observations": int(mask.sum()),
                       "serialized_table_copies_agree": copies,
                       "actual_first_17_channel_trials": trials[mask][:17].tolist(),
                       "reconstruction_rmse": float(np.sqrt(np.mean(np.square(errors)))),
                       "reconstruction_max_abs_difference": float(np.max(np.abs(errors)))})
    save("observations.json", rows)
    save("extraction-audit.json", audits)
    return rows, audits


def boot_mean(values, rng):
    values = np.asarray(values)
    resampled = values[rng.integers(0, len(values), (20000, len(values)))].mean(axis=1)
    return {"mean": float(values.mean()), "ci95": np.quantile(resampled, [.025, .975]).tolist(),
            "n_participants": len(values), "positive_participants": int(sum(values > 0))}


def difference(a, b, rng):
    a, b = np.asarray(a), np.asarray(b)
    samples = (a[rng.integers(0, len(a), (20000, len(a)))].mean(axis=1)
               - b[rng.integers(0, len(b), (20000, len(b)))].mean(axis=1))
    joined = np.concatenate((a, b))
    observed = float(a.mean() - b.mean())
    null = []
    for ix in itertools.combinations(range(16), 8):
        s = joined[list(ix)].sum()
        null.append(s / 8 - (joined.sum() - s) / 8)
    return {"evoked_minus_spontaneous": observed,
            "bootstrap_ci95": np.quantile(samples, [.025, .975]).tolist(),
            "two_sided_exact_permutation_p": float(np.mean(np.abs(null) >= abs(observed) - 1e-14)),
            "permutations": len(null), "interpretation": "exploratory association under group exchangeability"}


def exp_fit(y, free_level):
    t = np.arange(len(y))

    def evaluate(q):
        basis = q ** t
        x = np.column_stack((np.ones(len(t)), basis)) if free_level else basis[:, None]
        coef = np.linalg.lstsq(x, y, rcond=None)[0]
        return float(np.sum((x @ coef - y) ** 2)), coef

    grid = np.unique(np.r_[np.linspace(0, 1, 1001), 1 - np.logspace(-8, -3, 40)])
    loss = np.array([evaluate(q)[0] for q in grid])
    candidates = [(float(q), float(s)) for q, s in zip(grid, loss)]
    # Refine all grid local minima, not a single guessed start.
    for i in range(1, len(grid) - 1):
        if loss[i] <= loss[i - 1] and loss[i] <= loss[i + 1]:
            opt = minimize_scalar(lambda q: evaluate(q)[0], bounds=(grid[i - 1], grid[i + 1]),
                                  method="bounded", options={"xatol": 1e-12})
            candidates.append((float(opt.x), float(opt.fun)))
    q, _ = min(candidates, key=lambda x: x[1])
    objective, coefficients = evaluate(q)
    return {"q": q, "coefficients": coefficients.tolist(), "calibration_sse": objective}


def forecast(segment):
    n = len(segment)
    train, test = segment[:-50], segment[-50:]
    out = {}
    for free, label in [(False, "zero_level_decay"), (True, "fitted_level_relaxation")]:
        fit = exp_fit(train, free)
        a = fit["coefficients"]
        t = np.arange(len(train), n)
        pred = a[0] + a[1] * fit["q"] ** t if free else a[0] * fit["q"] ** t
        out[label] = {**fit, "predictions": pred.tolist(), "rmse": float(np.sqrt(np.mean((pred - test)**2)))}
    for label, value in [("constant_calibration_mean", train.mean()), ("last_observation", train[-1])]:
        pred = np.full(50, value)
        out[label] = {"value": float(value), "predictions": pred.tolist(),
                      "rmse": float(np.sqrt(np.mean((pred - test)**2)))}
    return out


def main():
    rows, audits = extract()
    participants = []
    for group in GROUPS:
        for p in range(1, 9):
            selected = [r for r in rows if r["group"] == group and r["participant"] == p]
            measured = [r for r in selected if r["adaptation"] is not None]
            baseline = np.mean([r["adaptation"] for r in measured if r["block"] == "Null"])
            last = np.array([r["adaptation"] for r in measured if r["trial"] >= 291])
            start = 191 if group == GROUPS[0] else 195
            terminal = np.array([r["adaptation"] for r in measured if r["trial"] >= start])
            assert len(last) == 50 and len(terminal) == (150 if group == GROUPS[0] else 146)
            participants.append({"group": group, "participant": p,
                                 "baseline": float(baseline), "terminal_count": len(terminal),
                                 "late_raw": float(last.mean()), "late_baseline_corrected": float(last.mean()-baseline),
                                 "early_raw": float(terminal[:10].mean()),
                                 "late_minus_early": float(last.mean()-terminal[:10].mean()),
                                 "forecast_raw": forecast(terminal),
                                 "forecast_baseline_corrected": forecast(terminal-baseline)})
    rng = np.random.default_rng(20261008)
    groups = {}
    metrics = ("late_raw", "late_baseline_corrected", "early_raw", "late_minus_early")
    for group in GROUPS:
        selected = [p for p in participants if p["group"] == group]
        groups[group] = {key: boot_mean([p[key] for p in selected], rng) for key in metrics}
        for scale in ("forecast_raw", "forecast_baseline_corrected"):
            models = selected[0][scale]
            rmse = {m: np.array([p[scale][m]["rmse"] for p in selected]) for m in models}
            groups[group][scale] = {m: {"mean_participant_rmse": float(v.mean()),
                                        "participant_rmse": v.tolist()} for m, v in rmse.items()}
            groups[group][scale]["fitted_vs_zero"] = {
                "rmse_difference_fitted_minus_zero": boot_mean(rmse["fitted_level_relaxation"]-rmse["zero_level_decay"], rng),
                "fitted_better_count": int(np.sum(rmse["fitted_level_relaxation"] < rmse["zero_level_decay"]))}
    contrasts = {key: difference([p[key] for p in participants if p["group"] == GROUPS[1]],
                                [p[key] for p in participants if p["group"] == GROUPS[0]], rng)
                 for key in ("late_raw", "late_baseline_corrected")}
    result = {"study": "Heald et al. 2021, recovery experiments", "analysis": "exploratory secondary analysis",
              "participants": participants, "groups": groups, "between_group_contrasts": contrasts,
              "original_files": len(audits), "all_trial_records": len(rows),
              "measured_channel_observations": sum(a["finite_channel_observations"] for a in audits),
              "held_out_observations": 16*50, "bootstrap_replicates": 20000, "seed": 20261008,
              "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
              "bindings": {"analysis_sha256": sha(Path(__file__)), "plan_sha256": sha(HERE / "ANALYSIS-PLAN.md"),
                           "observations_sha256": sha(HERE / "observations.json"),
                           "extraction_audit_sha256": sha(HERE / "extraction-audit.json")},
              "new_experiments": 0, "new_theorems": 0, "published_COIN_model_refit": False,
              "infinite_time_limit_established": False, "complete_awareness_established": False}
    save("results.json", result)
    print(json.dumps({"files": len(audits), "observations": result["measured_channel_observations"],
                      "contrasts": contrasts,
                      "group_late": {g: groups[g]["late_baseline_corrected"] for g in GROUPS},
                      "forecast_raw_rmse": {g: {m: v.get("mean_participant_rmse", v) for m,v in groups[g]["forecast_raw"].items()} for g in GROUPS}}, indent=2))


if __name__ == "__main__":
    main()
