"""Finite-choice evaluator succession experiment. No trained AI models are used."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy import stats

ROOT = Path(__file__).resolve().parent
ARMS = ("fixed", "endogenous", "independent", "rotating", "replay", "protected")
ACTIONS = np.array([(a / 4, b / 4, (4-a-b) / 4)
                    for a in range(5) for b in range(5-a)])
TRANSFERS = [(i, j) for i in range(3) for j in range(3) if i != j]


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def softmax(x, axis=-1):
    v = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return v / v.sum(axis=axis, keepdims=True)


def choose(probs, uniforms):
    return np.minimum((uniforms[..., None] > np.cumsum(probs, axis=-1)).sum(-1),
                      probs.shape[-1] - 1)


def stream(seed, purpose):
    return np.random.default_rng(np.random.SeedSequence([int(seed), purpose]))


def make_worlds(cfg, donor=False):
    seeds = np.arange(cfg["seed_start"], cfg["seed_start"] + cfg["worlds"])
    if donor:
        seeds += cfg["donor_seed_offset"]
    n, t, r = cfg["agents"], cfg["epochs"], cfg["rounds_per_epoch"]
    skills, prod, appointment, amendment, rotation = [], [], [], [], []
    for seed in seeds:
        rng = stream(seed, 1)
        s = np.array([[1., .6]] * (n//2) + [[.6, 1.]] * (n//2))
        s *= rng.uniform(1-cfg["skill_jitter"], 1+cfg["skill_jitter"], s.shape)
        skills.append(s[rng.permutation(n)])
        prod.append(stream(seed, 2).random((t, r, n)))
        appointment.append(stream(seed, 3).random(t))
        amendment.append(stream(seed, 4).random(t))
        rr = stream(seed, 5)
        rotation.append(np.concatenate([rr.permutation(n) for _ in range((t+n-1)//n)])[:t])
    skills = np.array(skills)
    features = np.empty((len(seeds), n, len(ACTIONS), 3))
    features[..., :2] = skills[:, :, None, :] * np.sqrt(ACTIONS[None, None, :, :2])
    features[..., 2] = ACTIONS[None, None, :, 2]
    return dict(seeds=seeds, skills=skills, features=features,
                prod=np.array(prod), appointment=np.array(appointment),
                amendment=np.array(amendment), rotation=np.array(rotation))


def evaluate(outputs, rubric, alpha, cfg):
    scores = np.einsum("bnd,bd->bn", outputs, rubric)
    shares = cfg["allocation_floor"]/cfg["agents"] + (1-cfg["allocation_floor"])*softmax(
        cfg["score_temperature"] * scores)
    true = alpha * outputs[..., 0] + (1-alpha) * outputs[..., 1]
    return shares, (shares * true).sum(-1), true


def production(outputs, rubric, alpha, worlds, uniforms, cfg):
    """Simultaneous logit responses against previous rival submissions."""
    f = worlds["features"]
    prev_score = np.einsum("bnd,bd->bn", outputs, rubric)
    prev_exp = np.exp(cfg["score_temperature"] * prev_score)
    old_true = alpha*outputs[..., 0] + (1-alpha)*outputs[..., 1]
    alt_score = np.einsum("bnad,bd->bna", f, rubric)
    alt_exp = np.exp(cfg["score_temperature"] * alt_score)
    alt_true = alpha*f[..., 0] + (1-alpha)*f[..., 1]
    other_exp = prev_exp.sum(1)[:, None] - prev_exp
    denom = other_exp[..., None] + alt_exp
    floor = cfg["allocation_floor"]/cfg["agents"]
    alt_share = floor + (1-cfg["allocation_floor"])*alt_exp/denom
    other_true = old_true.sum(1)[:, None] - old_true
    other_weighted = (prev_exp*old_true).sum(1)[:, None] - prev_exp*old_true
    alt_w = floor*(other_true[..., None]+alt_true) + (1-cfg["allocation_floor"])*(
        other_weighted[..., None]+alt_exp*alt_true)/denom
    value = alt_share + cfg["common_value_weight"]*alt_w
    choices = choose(softmax(cfg["production_temperature"]*value), uniforms)
    return f[np.arange(len(f))[:, None], np.arange(cfg["agents"])[None, :], choices]


def candidates(rubric, alpha, evidence_day, cfg):
    result = np.repeat(rubric[:, None, :], 8, axis=1)
    valid = np.ones(result.shape[:2], dtype=bool)
    for k, (dest, src) in enumerate(TRANSFERS, start=1):
        result[:, k, dest] += cfg["rubric_step"]
        result[:, k, src] -= cfg["rubric_step"]
        valid[:, k] = result[:, k, src] >= -cfg["numeric_tolerance"]
    result[:, 7, :] = [alpha, 1-alpha, 0.]
    valid[:, 7] = evidence_day
    return result, valid


def run_arm(cfg, worlds, context, arm, replay=None):
    b, n, tmax = cfg["worlds"], cfg["agents"], cfg["epochs"]
    bi = np.arange(b)
    rubric = np.tile(cfg["initial_rubric"], (b, 1))
    # Common neutral initialization: useful effort split evenly.
    initial_action = int(np.flatnonzero(np.all(ACTIONS == [.5, .5, 0.], axis=1))[0])
    outputs = worlds["features"][:, :, initial_action].copy()
    authority = np.full((b, n), 1/n)
    hist = {k: np.zeros((b, tmax)) for k in (
        "gross", "net", "hhi", "presentation", "harmful", "beneficial",
        "amended", "veto", "evidence_valid", "corrected", "delta_governor",
        "delta_value", "pre_governor_share", "admin_cost", "reference_delta_value",
        "reference_delta_governor")}
    hist["governor"] = np.full((b, tmax), -1, dtype=int)
    hist["proposed_option"] = np.full((b, tmax), -1, dtype=int)
    hist["implemented_option"] = np.full((b, tmax), -1, dtype=int)
    hist["shares"] = np.zeros((b, tmax, n))
    hist["appointment_probabilities"] = np.zeros((b, tmax, n))
    hist["frozen_outputs"] = np.zeros((b, tmax, n, 3))
    hist["candidate_values"] = np.full((b, tmax, 8), np.nan)
    hist["candidate_valid"] = np.zeros((b, tmax, 8), dtype=bool)
    hist["before_rubric"] = np.zeros((b, tmax, 3))
    hist["after_rubric"] = np.zeros((b, tmax, 3))
    hist["proposed_rubric"] = np.zeros((b, tmax, 3))
    for epoch in range(tmax):
        alpha = .25 if context == "shift" and epoch >= tmax//2 else .75
        if arm == "replay":
            rubric = replay["before_rubric"][:, epoch].copy()
        hist["before_rubric"][:, epoch] = rubric
        w_rounds, p_rounds = [], []
        for rnd in range(cfg["rounds_per_epoch"]):
            outputs = production(outputs, rubric, alpha, worlds,
                                 worlds["prod"][:, epoch, rnd], cfg)
            p, w, true = evaluate(outputs, rubric, alpha, cfg)
            w_rounds.append(w)
            p_rounds.append(p)
        mean_p = np.mean(p_rounds, axis=0)
        hist["gross"][:, epoch] = np.mean(w_rounds, axis=0)
        hist["shares"][:, epoch] = mean_p
        hist["frozen_outputs"][:, epoch] = outputs
        hist["hhi"][:, epoch] = (mean_p**2).sum(-1)
        hist["presentation"][:, epoch] = rubric[:, 2]
        authority = (1-cfg["authority_memory"])*authority + cfg["authority_memory"]*mean_p
        if arm in ("fixed", "replay") or epoch == tmax-1:
            if arm == "replay":
                rubric = replay["after_rubric"][:, epoch].copy()
                hist["admin_cost"][:, epoch] = replay["admin_cost"][:, epoch]
            hist["after_rubric"][:, epoch] = rubric
            hist["proposed_rubric"][:, epoch] = rubric
            hist["net"][:, epoch] = hist["gross"][:, epoch] - hist["admin_cost"][:, epoch]
            continue
        if arm == "rotating":
            governor = worlds["rotation"][:, epoch]
            appointment_probs = np.eye(n)[governor]
        elif arm == "independent":
            appointment_probs = np.full((b, n), 1/n)
            governor = choose(appointment_probs, worlds["appointment"][:, epoch])
        else:
            appointment_probs = authority**cfg["authority_power"]
            appointment_probs /= appointment_probs.sum(-1, keepdims=True)
            governor = choose(appointment_probs, worlds["appointment"][:, epoch])
        hist["appointment_probabilities"][:, epoch] = appointment_probs
        evidence_day = (epoch+1) % cfg["correction_every"] == 0
        proposals, valid = candidates(rubric, alpha, evidence_day, cfg)
        scores = np.einsum("bnd,bkd->bkn", outputs, proposals)
        alt_p = cfg["allocation_floor"]/n + (1-cfg["allocation_floor"])*softmax(
            cfg["score_temperature"]*scores)
        alt_w = (alt_p*true[:, None, :]).sum(-1)
        changed = np.max(np.abs(proposals-rubric[:, None, :]), axis=-1) > cfg["numeric_tolerance"]
        governor_p = alt_p[bi[:, None], np.arange(8)[None, :], governor[:, None]]
        value = governor_p + cfg["common_value_weight"]*alt_w - cfg["amendment_cost"]*changed
        value[~valid] = -np.inf
        hist["candidate_values"][:, epoch] = value
        hist["candidate_valid"][:, epoch] = valid
        picked = choose(softmax(cfg["governance_temperature"]*value), worlds["amendment"][:, epoch])
        hist["proposed_option"][:, epoch] = picked
        hist["proposed_rubric"][:, epoch] = proposals[bi, picked]
        valid_evidence = evidence_day & ((alt_w[:, 7]-alt_w[:, 0]) > cfg["evidence_threshold"])
        veto = np.zeros(b, dtype=bool)
        if arm == "protected":
            veto = alt_w[bi, picked] < alt_w[:, 0]-cfg["numeric_tolerance"]
            picked[veto] = 0
            picked[valid_evidence] = 7
        next_rubric = proposals[bi, picked].copy()
        # Only tiny floating-point residuals are removed, never substantive invalid weights.
        next_rubric[np.abs(next_rubric) < cfg["numeric_tolerance"]] = 0
        adopted = changed[bi, picked]
        dp = governor_p[bi, picked]-governor_p[:, 0]
        dw = alt_w[bi, picked]-alt_w[:, 0]
        tol = cfg["numeric_tolerance"]
        hist["governor"][:, epoch] = governor
        hist["implemented_option"][:, epoch] = picked
        hist["reference_delta_value"][:, epoch] = alt_w[:, 7]-alt_w[:, 0]
        hist["reference_delta_governor"][:, epoch] = governor_p[:, 7]-governor_p[:, 0]
        hist["pre_governor_share"][:, epoch] = p[bi, governor]
        hist["amended"][:, epoch] = adopted
        hist["veto"][:, epoch] = veto
        hist["delta_governor"][:, epoch] = dp
        hist["delta_value"][:, epoch] = dw
        hist["harmful"][:, epoch] = adopted & (dp > tol) & (dw < -tol)
        hist["beneficial"][:, epoch] = adopted & (dw > tol)
        hist["evidence_valid"][:, epoch] = valid_evidence
        hist["corrected"][:, epoch] = valid_evidence & (alt_w[bi, picked] >= alt_w[:, 7]-tol)
        hist["admin_cost"][:, epoch] = cfg["amendment_cost"]*adopted + cfg["audit_cost"]*(arm == "protected")
        hist["net"][:, epoch] = hist["gross"][:, epoch]-hist["admin_cost"][:, epoch]
        hist["after_rubric"][:, epoch] = next_rubric
        rubric = next_rubric
    return hist


def summarize(cfg, worlds, context, arm, h):
    rows = []
    start = cfg["epochs"]-cfg["evaluation_epochs"]
    for b, seed in enumerate(worlds["seeds"]):
        row = dict(seed=int(seed), context=context, arm=arm)
        for key in ("gross", "net", "hhi", "presentation"):
            row[key] = float(h[key][b, start:].mean())
        for key in ("harmful", "beneficial", "amended", "veto", "evidence_valid", "corrected"):
            row[key] = int(h[key][b, start:].sum())
        governors = h["governor"][b, start:]
        counts = np.bincount(governors[governors >= 0], minlength=cfg["agents"])
        row["authority_hhi"] = float(((counts / counts.sum())**2).sum()) if counts.sum() else None
        eligible, persistent = 0, 0
        horizon = cfg["persistence_epochs"]
        for epoch in range(start, cfg["epochs"]-horizon):
            if h["harmful"][b, epoch]:
                eligible += 1
                g = h["governor"][b, epoch]
                future = h["shares"][b, epoch+1:epoch+1+horizon, g].mean()
                persistent += int(future > h["pre_governor_share"][b, epoch]+1e-4)
        row["persistence_eligible"] = eligible
        row["persistent_advantage"] = persistent
        rows.append(row)
    return rows


def contrast(a, b, cfg, rng):
    diff = np.asarray(a)-np.asarray(b)
    mean = float(diff.mean())
    boot = diff[rng.integers(0, len(diff), (cfg["bootstrap_replicates"], len(diff)))].mean(1)
    p = float(stats.ttest_1samp(diff, 0).pvalue) if diff.std() else (1. if mean == 0 else 0.)
    return dict(mean=mean, ci95=[float(x) for x in np.quantile(boot, [.025, .975])],
                p_unadjusted=p, differences=diff.tolist())


def analyze(rows, cfg):
    index = {}
    for row in rows:
        index.setdefault((row["context"], row["arm"]), []).append(row)
    def vals(context, arm, field):
        return [r[field] for r in sorted(index[context, arm], key=lambda r:r["seed"])]
    definitions = [
        ("H1", "stable", "endogenous", "independent", "gross", -1),
        ("H2", "stable", "endogenous", "independent", "harmful", 1),
        ("H3", "shift", "independent", "fixed", "gross", 1),
        ("H4", "stable", "protected", "endogenous", "gross", 1)]
    rng = np.random.default_rng(cfg["analysis_seed"])
    tests = []
    for label, context, a, b, field, direction in definitions:
        result = contrast(vals(context, a, field), vals(context, b, field), cfg, rng)
        tests.append(dict(id=label, context=context, a=a, b=b, field=field,
                          predicted_direction=direction, **result))
    running = 0.
    for rank, idx in enumerate(sorted(range(len(tests)), key=lambda k:tests[k]["p_unadjusted"])):
        running = max(running, min(1., (len(tests)-rank)*tests[idx]["p_unadjusted"]))
        tests[idx]["p_holm"] = running
    for test in tests:
        test["verdict"] = ("inconclusive" if test["p_holm"] >= .05 else
                           "supported" if test["mean"]*test["predicted_direction"] > 0 else "contradicted")
    means = {f"{context}/{arm}": {field: float(np.mean(vals(context, arm, field)))
              for field in ("gross", "net", "hhi", "presentation", "harmful", "beneficial", "amended",
                            "evidence_valid", "corrected", "persistence_eligible", "persistent_advantage")}
             for context in ("stable", "shift") for arm in ARMS}
    secondary = {}
    for context in ("stable", "shift"):
        for a, b in (("endogenous", "replay"), ("endogenous", "fixed"),
                     ("protected", "independent"), ("protected", "endogenous"),
                     ("endogenous", "rotating"), ("rotating", "independent")):
            for field in ("gross", "net"):
                secondary[f"{context}/{a}-{b}/{field}"] = contrast(
                    vals(context, a, field), vals(context, b, field), cfg, rng)
    return dict(tests=tests, means=means, secondary=secondary)


def run(cfg, out):
    out.mkdir(exist_ok=False)
    manifest = dict(sealed_at=now(), kind="prospective local input seal, not external preregistration",
                    inputs={p:digest(ROOT/p) for p in ("benchmark.py", "config.json", "PROTOCOL.md", "test_benchmark.py")},
                    python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, config=cfg)
    (out/"input_manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    (out/"sealed-inputs").mkdir()
    for name in manifest["inputs"]:
        (out/"sealed-inputs"/name).write_bytes((ROOT/name).read_bytes())
    worlds, donors = make_worlds(cfg), make_worlds(cfg, donor=True)
    rows = []
    for context in ("stable", "shift"):
        print(f"Running independent donor worlds: {context}", flush=True)
        donor = run_arm(cfg, donors, context, "endogenous")
        np.savez_compressed(out/f"{context}-donors.npz", seeds=donors["seeds"], **donor)
        for arm in ARMS:
            print(f"Running {context}: {arm}", flush=True)
            h = run_arm(cfg, worlds, context, arm, replay=donor if arm == "replay" else None)
            np.savez_compressed(out/f"{context}-{arm}.npz", seeds=worlds["seeds"], skills=worlds["skills"], **h)
            rows.extend(summarize(cfg, worlds, context, arm, h))
    with (out/"world_summaries.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    analysis = analyze(rows, cfg)
    analysis["completed_at"] = now()
    analysis["inputs_unchanged"] = all(digest(ROOT/p) == value for p, value in manifest["inputs"].items())
    (out/"analysis.json").write_text(json.dumps(analysis, indent=2)+"\n")
    print(json.dumps({"tests":[{k:v for k,v in t.items() if k != "differences"} for t in analysis["tests"]],
                      "inputs_unchanged":analysis["inputs_unchanged"]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT/"results-v1")
    args = parser.parse_args()
    run(json.loads((ROOT/"config.json").read_text()), args.output)
