"""Read-only audit, secondary summaries, and scientific figure for the sealed run."""
import csv
import hashlib
import importlib.util
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT/"results-v1"
ARMS = ("fixed", "endogenous", "independent", "rotating", "replay", "protected")
LABELS = {"fixed":"Fixed rules", "endogenous":"Appointed by success",
          "independent":"Independent appointments", "rotating":"Balanced rotation",
          "replay":"Independent replay", "protected":"Protected correction"}
COLORS = {"fixed":"#87929C", "endogenous":"#BB4C35", "independent":"#3177A6",
          "rotating":"#8C6CAB", "replay":"#B58A3B", "protected":"#23836B"}


def main():
    manifest = json.loads((OUT/"input_manifest.json").read_text())
    cfg = manifest["config"]
    hash_checks = {name: hashlib.sha256((OUT/"sealed-inputs"/name).read_bytes()).hexdigest() == value
                   for name, value in manifest["inputs"].items()}
    assert all(hash_checks.values())
    spec = importlib.util.spec_from_file_location("sealed_benchmark", OUT/"sealed-inputs/benchmark.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    archives = {(context, arm):dict(np.load(OUT/f"{context}-{arm}.npz"))
                for context in ("stable", "shift") for arm in ARMS}
    residuals = []
    detail = {}
    for (context, arm), h in archives.items():
        assert np.all(h["before_rubric"] >= -1e-12)
        assert np.allclose(h["before_rubric"].sum(-1), 1)
        assert np.allclose(h["before_rubric"][:, 1:], h["after_rubric"][:, :-1])
        assert not np.any(h["evidence_valid"][:, -1])
        for t in range(cfg["epochs"]-1):
            if arm in ("fixed", "replay"):
                continue
            alpha = .25 if context == "shift" and t >= cfg["epochs"]//2 else .75
            p0, w0, _ = module.evaluate(h["frozen_outputs"][:, t], h["before_rubric"][:, t], alpha, cfg)
            p1, w1, _ = module.evaluate(h["frozen_outputs"][:, t], h["after_rubric"][:, t], alpha, cfg)
            gov = h["governor"][:, t]
            dp = (p1-p0)[np.arange(cfg["worlds"]), gov]
            residuals.extend([float(np.max(np.abs(dp-h["delta_governor"][:, t]))),
                              float(np.max(np.abs(w1-w0-h["delta_value"][:, t])))])
            assert np.allclose(w1-w0, h["delta_value"][:, t], atol=1e-12)
            assert np.allclose(dp, h["delta_governor"][:, t], atol=1e-12)
            assert np.array_equal(h["harmful"][:, t].astype(bool), (dp>1e-9)&(w1-w0 < -1e-9))
        for phase, start, stop in (("all", 0, 159), ("before_shift", 0, 80), ("after_shift", 80, 159)):
            ev = h["evidence_valid"][:, start:stop].sum(-1)
            ok = h["corrected"][:, start:stop].sum(-1)
            eligible = ev > 0
            detail[f"{context}/{arm}/{phase}"] = dict(
                opportunities=int(ev.sum()), corrected=int(ok.sum()),
                worlds_with_opportunities=int(eligible.sum()), worlds_without_opportunities=int((~eligible).sum()),
                mean_world_conditional_response=float(np.mean(ok[eligible]/ev[eligible])) if eligible.any() else None,
                pooled_response=float(ok.sum()/ev.sum()) if ev.sum() else None)
    # Reproduce the first two worlds from sealed source, not new inferential data.
    small = dict(cfg, worlds=2)
    worlds = module.make_worlds(small)
    for context, arm in (("stable", "endogenous"), ("shift", "independent")):
        check = module.run_arm(small, worlds, context, arm)
        for key, value in check.items():
            np.testing.assert_allclose(value, archives[context, arm][key][:2], rtol=0, atol=0, equal_nan=True)
    with (OUT/"world_summaries.csv").open() as f:
        rows = list(csv.DictReader(f))
    def values(context, arm, field):
        selected = sorted((r for r in rows if r["context"] == context and r["arm"] == arm), key=lambda r:int(r["seed"]))
        return np.array([float(r[field]) for r in selected])
    rng = np.random.default_rng(20261004)
    shift_contrast = module.contrast(values("shift", "endogenous", "gross"),
                                     values("shift", "independent", "gross"), cfg, rng)
    interaction = module.contrast(values("shift", "endogenous", "gross")-values("shift", "independent", "gross"),
                                  values("stable", "endogenous", "gross")-values("stable", "independent", "gross"), cfg, rng)
    mechanism = {}
    for arm in ("endogenous", "independent", "rotating", "protected"):
        h = archives["shift", arm]
        is_a = h["skills"][..., 0] > h["skills"][..., 1]
        for phase, start, stop in (("late_before", 40, 80), ("late_after", 120, 160)):
            gov = h["governor"][:, start:stop]
            active = gov >= 0
            governor_a = np.take_along_axis(is_a, np.maximum(gov, 0), axis=1)
            mechanism[f"{arm}/{phase}"] = dict(
                mean_a_rubric=float(h["before_rubric"][:, start:stop, 0].mean()),
                fraction_a_governors=float(governor_a[active].mean()),
                mean_a_contract_share=float((h["shares"][:, start:stop]*is_a[:, None, :]).sum(-1).mean()))
        valid = h["evidence_valid"][:, 80:159].astype(bool)
        gov = h["governor"][:, 80:159]
        governor_a = np.take_along_axis(is_a, np.maximum(gov, 0), axis=1)
        for kind, who in (("a", governor_a), ("b", ~governor_a)):
            mask = valid & who
            dv = h["reference_delta_governor"][:, 80:159] + cfg["common_value_weight"]*h["reference_delta_value"][:, 80:159] - cfg["amendment_cost"]
            mechanism[f"{arm}/postshift_correction_{kind}"] = dict(
                opportunities=int(mask.sum()), corrected=int(h["corrected"][:, 80:159][mask].sum()),
                mean_private_utility_change=float(dv[mask].mean()) if mask.any() else None,
                negative_private_utility_count=int((dv[mask] < 0).sum()))
    audit = dict(input_snapshot_hashes=hash_checks, maximum_rescoring_error=max(residuals),
                 reproduced_worlds="First two worlds exactly reproduced for stable/endogenous and shift/independent; reused validation data only",
                 correction_response=detail,
                 exploratory_mechanism=mechanism,
                 secondary_shift_endogenous_minus_independent=shift_contrast,
                 exploratory_context_interaction=interaction,
                 scope="Secondary shift contrast was allowed by protocol. Interaction and diagnostic summaries were selected after seeing outcomes; no adjusted confirmatory claim.")
    (OUT/"audit-and-secondary.json").write_text(json.dumps(audit, indent=2)+"\n")

    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10,
                         "axes.spines.top":False, "axes.spines.right":False,
                         "axes.spines.left":False, "axes.edgecolor":"#CBD0D6"})
    fig, axes = plt.subplots(2, 2, figsize=(13, 9.2), gridspec_kw={"height_ratios":[1.1, 1]})
    fig.subplots_adjust(left=.20, right=.97, bottom=.21, top=.85, wspace=.40, hspace=.40)
    fig.suptitle("Success-based appointments helped under stable demand,\nbut adapted poorly when demand changed", x=.5, y=.97, fontsize=17, fontweight="bold")
    fig.text(.5, .895, "Synthetic strategic agents • 128 paired worlds • one sealed configuration", ha="center", color="#596675")
    for col, context in enumerate(("stable", "shift")):
        ax = axes[0, col]
        for arm in ("fixed", "endogenous", "independent", "protected"):
            h = archives[context, arm]["gross"]
            mean, se = h.mean(0), h.std(0, ddof=1)/np.sqrt(len(h))
            ax.plot(np.arange(1, 161), mean, lw=1.8, color=COLORS[arm], label=LABELS[arm])
            ax.fill_between(np.arange(1,161), mean-1.96*se, mean+1.96*se, color=COLORS[arm], alpha=.12, linewidth=0)
        ax.set_ylim(.15, .77)
        ax.set_xlim(1, 160)
        ax.set_title("Demand unchanged" if context == "stable" else "Demand changes halfway", loc="left", fontsize=12, fontweight="bold")
        ax.set_xlabel("Epoch")
        ax.set_ylabel("Independent usefulness")
        ax.grid(axis="y", alpha=.15)
        if context == "shift":
            ax.axvline(80.5, color="#75808B", lw=1, ls="--")
        ax.axvspan(120, 160, color="#9BA6B3", alpha=.06)
        ax = axes[1, col]
        for j, arm in enumerate(ARMS):
            x = values(context, arm, "gross")
            se = x.std(ddof=1)/np.sqrt(len(x))
            ax.errorbar(x.mean(), j, xerr=1.96*se, fmt="o", ms=6, capsize=3, color=COLORS[arm])
        ax.set_yticks(range(6), [LABELS[a] for a in ARMS])
        ax.invert_yaxis()
        ax.set_xlim(.25, .75)
        ax.set_xlabel("Mean usefulness in the final 40 epochs")
        ax.grid(axis="x", alpha=.15)
    handles, labels = axes[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(.56,.075), ncol=2, frameon=False, fontsize=9)
    fig.text(.20, .025, "Bands and bars: pointwise 95% normal intervals across worlds. Raw utility units; higher is better.\nTwo primary predictions were contradicted; protected correction assumes an independent, exact evaluator.", fontsize=8.5, color="#596675")
    fig.savefig(OUT/"benchmark-results.png", dpi=180)
    fig.savefig(OUT/"benchmark-results.svg")
    print(json.dumps({"audit_passed":True, "max_rescoring_error":max(residuals),
                      "shift_difference":{k:v for k,v in shift_contrast.items() if k!="differences"},
                      "figure":str(OUT/"benchmark-results.png")}, indent=2))


if __name__ == "__main__":
    main()
