"""Prospectively specified identical-state appointment-policy experiment."""
import csv
import json
import platform
from pathlib import Path

import numpy as np
import scipy

import benchmark as base
from branch_engine import State, run_segment

ROOT = Path(__file__).resolve().parent
INPUTS = ("benchmark.py", "config.json", "branch_engine.py", "branch_experiment.py",
          "branch_config.json", "BRANCH-PROTOCOL.md", "test_branching.py")


def config():
    design = json.loads((ROOT/"branch_config.json").read_text())
    cfg = json.loads((ROOT/"config.json").read_text())
    for key in ("worlds", "seed_start", "analysis_seed", "bootstrap_replicates"):
        cfg[key] = design[key]
    return cfg, design


def summaries(cfg, design, worlds, source, context, arm, h):
    rows = []
    fork, late = design["fork_epoch"], cfg["epochs"]-cfg["evaluation_epochs"]
    for i, seed in enumerate(worlds["seeds"]):
        row = dict(seed=int(seed), source=source, context=context, arm=arm)
        for label, start in (("late", late), ("postfork", fork)):
            for field in ("gross", "net", "hhi", "presentation"):
                row[f"{label}_{field}"] = float(h[field][i, start:].mean())
            for field in ("harmful", "beneficial", "amended", "evidence_valid", "corrected"):
                row[f"{label}_{field}"] = int(h[field][i, start:].sum())
            row[f"{label}_a_rubric"] = float(h["before_rubric"][i, start:, 0].mean())
            governors = h["governor"][i, start:]
            active = governors >= 0
            a_type = worlds["skills"][i, :, 0] > worlds["skills"][i, :, 1]
            row[f"{label}_a_governors"] = float(a_type[governors[active]].mean()) if active.any() else None
            row[f"{label}_a_contracts"] = float((h["shares"][i, start:]*a_type[None, :]).sum(-1).mean())
        rows.append(row)
    return rows


def analyze(rows, cfg, design):
    rng = np.random.default_rng(cfg["analysis_seed"])
    def values(source, context, arm, field):
        selected = sorted((r for r in rows if r["source"] == source and r["context"] == context and r["arm"] == arm), key=lambda r:r["seed"])
        if len(selected) != cfg["worlds"]:
            raise ValueError("Incomplete paired worlds")
        return np.array([r[field] for r in selected])
    def effect(source, context, field="late_gross"):
        return values(source, context, "independent", field)-values(source, context, "endogenous", field)
    raw = [effect("endogenous", "shift"), effect("independent", "shift"),
           np.mean([effect(s, "shift")-effect(s, "stable") for s in design["source_histories"]], axis=0)]
    tests = []
    for label, diff in zip(("B1", "B2", "B3"), raw):
        result = base.contrast(diff, np.zeros_like(diff), cfg, rng)
        tests.append(dict(id=label, predicted_direction=1, **result))
    running = 0.
    for rank, idx in enumerate(sorted(range(3), key=lambda i:tests[i]["p_unadjusted"])):
        running = max(running, min(1., (3-rank)*tests[idx]["p_unadjusted"]))
        tests[idx]["p_holm"] = running
    for test in tests:
        test["verdict"] = ("inconclusive" if test["p_holm"] >= .05 else
                           "supported" if test["mean"] > 0 else "contradicted")
    means, secondary = {}, {}
    for source in design["source_histories"]:
        for context in design["contexts"]:
            for arm in design["branches"]:
                fields = [k for k in rows[0] if k not in ("seed", "source", "context", "arm")]
                means[f"{source}/{context}/{arm}"] = {
                    field:float(np.mean(values(source, context, arm, field)))
                    for field in fields if not field.endswith("a_governors") or arm != "fixed"}
            for field in ("late_gross", "late_net", "postfork_gross", "postfork_net"):
                for arm in ("independent", "protected", "fixed"):
                    secondary[f"{source}/{context}/{arm}-endogenous/{field}"] = base.contrast(
                        values(source, context, arm, field), values(source, context, "endogenous", field), cfg, rng)
    for context in design["contexts"]:
        for field in ("late_gross", "late_net", "postfork_gross", "postfork_net"):
            secondary[f"source-interaction/{context}/{field}"] = base.contrast(
                effect("endogenous", context, field), effect("independent", context, field), cfg, rng)
    return dict(tests=tests, means=means, secondary=secondary)


def run(out=ROOT/"results-v2"):
    cfg, design = config()
    out.mkdir(exist_ok=False)
    manifest = dict(sealed_at=base.now(), kind="Prospective follow-up motivated by v1; not external preregistration",
                    inputs={name:base.digest(ROOT/name) for name in INPUTS},
                    python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                    effective_config=cfg, design=design)
    (out/"input_manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    (out/"sealed-inputs").mkdir()
    for name in INPUTS:
        (out/"sealed-inputs"/name).write_bytes((ROOT/name).read_bytes())
    worlds = base.make_worlds(cfg)
    np.savez_compressed(out/"shared-worlds.npz", **worlds)
    rows, checks = [], []
    for source in design["source_histories"]:
        print(f"Generating common prefix: {source}", flush=True)
        prefix, state = run_segment(cfg, worlds, "stable", source, stop_epoch=design["fork_epoch"])
        checkpoint = out/f"checkpoint-{source}.npz"
        state.save(checkpoint)
        np.savez_compressed(out/f"prefix-{source}.npz", valid_start=0, valid_stop=design["fork_epoch"], **prefix)
        initial_hash = state.fingerprint()
        for context in design["contexts"]:
            first_outputs = first_gross = None
            for arm in design["branches"]:
                print(f"Continuing {source}/{context}/{arm}", flush=True)
                clone = State.load(checkpoint)
                assert clone.fingerprint() == initial_hash
                h, _ = run_segment(cfg, worlds, context, arm, state=clone)
                assert clone.fingerprint() == initial_hash
                t = design["fork_epoch"]
                if first_outputs is None:
                    first_outputs, first_gross = h["frozen_outputs"][:, t].copy(), h["gross"][:, t].copy()
                else:
                    np.testing.assert_array_equal(h["frozen_outputs"][:, t], first_outputs)
                    np.testing.assert_array_equal(h["gross"][:, t], first_gross)
                checks.append(dict(source=source, context=context, arm=arm,
                                   restored_fingerprint=initial_hash, source_unchanged=True, first_production_matched=True))
                np.savez_compressed(out/f"branch-{source}-{context}-{arm}.npz",
                                    valid_start=t, valid_stop=cfg["epochs"], source_state_hash=initial_hash, **h)
                rows.extend(summaries(cfg, design, worlds, source, context, arm, h))
    with (out/"world_summaries.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    analysis = analyze(rows, cfg, design)
    analysis["completed_at"] = base.now()
    analysis["inputs_unchanged"] = all(base.digest(ROOT/name) == value for name, value in manifest["inputs"].items())
    (out/"analysis.json").write_text(json.dumps(analysis, indent=2)+"\n")
    (out/"branch_checks.json").write_text(json.dumps(checks, indent=2)+"\n")
    print(json.dumps({"tests":[{k:v for k,v in t.items() if k!="differences"} for t in analysis["tests"]],
                      "inputs_unchanged":analysis["inputs_unchanged"]}, indent=2))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT/"results-v2")
    run(parser.parse_args().output)
