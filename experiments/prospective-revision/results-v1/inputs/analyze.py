"""Preserve exhaustive finite workflow comparisons, controls, and a figure."""
import hashlib
import json
import platform
import shutil
from collections import Counter
from dataclasses import asdict, fields, replace
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from model import (WORLDS, World, Params, eligibility, audit_power, validation_power,
                   workflows, loss_matrix, prior_grid, minimax_regret)

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"


def world_summaries(cfg):
    return {w.name: {"q": w.q, "p": w.p, "eligibility": eligibility(w.q),
                     "gross_gain_per_decision": eligibility(w.q)*(w.p-cfg.response_cost),
                     "net_gain_per_decision": eligibility(w.q)*(w.p-cfg.response_cost)-cfg.running_fee,
                     "validation_power": validation_power(w, cfg)} for w in WORLDS}


def solve(cfg, denominator):
    rows = workflows(cfg)
    losses = loss_matrix(rows)
    decisions = []
    for prior in prior_grid(denominator):
        risks = losses@prior
        i = int(np.argmin(risks))
        decisions.append({"prior_E_P_T_U": prior.tolist(), "workflow": rows[i]["name"],
                          "incremental_loss": float(risks[i]),
                          "ties": [rows[j]["name"] for j in np.flatnonzero(np.abs(risks-risks[i])<1e-10)]})
    return {"parameters": asdict(cfg), "worlds": world_summaries(cfg), "workflows": rows,
            "prior_decisions": decisions,
            "winner_counts": dict(Counter("audit" if d["workflow"].startswith("audit-") else d["workflow"]
                                         for d in decisions)),
            "minimax_regret": minimax_regret(rows)}


def plot(result):
    base = result["base"]
    rows = base["workflows"]
    audits = [r for r in rows if r["eta"] == 0]
    quotas = [r["m"] for r in audits]
    direct = next(r for r in rows if r["name"] == "direct")
    colors = {"E": "#527693", "P": "#147d70", "T": "#cc6a39", "U": "#8c59a5"}
    labels = {"E": "E: no structure, no benefit", "P": "P: structure + benefit",
              "T": "T: structure, no benefit", "U": "U: benefit without anomaly"}
    fig, axes = plt.subplots(2, 2, figsize=(13.4, 9.6), layout="constrained")
    ax = axes[0,0]
    for w in ("P", "U"):
        ax.plot(quotas, [r["worlds"][w]["audit_probability"] for r in audits],
                color=colors[w], label="P/T: clustered records" if w=="P" else "E/U: exchangeable records", lw=2.3)
    ax.axhline(.05, color="#555555", ls=":", label="Audit error ceiling: 5%")
    ax.set(title="Historical audit cannot distinguish E from U", xlabel="Raw windows retained before the question", ylabel="Probability validation is opened", ylim=(-.015, 1.04))
    ax.legend(fontsize=9, loc="center right")
    ax = axes[0,1]
    x = np.arange(4)
    ax.bar(x-.17, [base["worlds"][w]["validation_power"] for w in ("E","P","T","U")], .34,
           label="Direct validation", color="#455f72")
    at28 = next(r for r in audits if r["m"] == 28)
    ax.bar(x+.17, [at28["worlds"][w]["adopt_probability_given_question"] for w in ("E","P","T","U")],
           .34, label="28-window audit first", color="#c3944b")
    ax.set(xticks=x, xticklabels=["E\nno benefit", "P\nbenefit", "T\nno benefit", "U\nbenefit"],
           ylim=(0,1.07), ylabel="Adoption probability, given later question", title="Fresh order–outcome evidence tests usefulness")
    ax.legend(fontsize=9)
    ax = axes[1,0]
    for w in ("E","P","T","U"):
        ax.plot(quotas, [r["worlds"][w]["incremental_loss"] for r in audits], color=colors[w], lw=2, label=labels[w])
        ax.scatter([133], [direct["worlds"][w]["incremental_loss"]], marker="D", color=colors[w], s=33)
    ax.axhline(0, color="#777777", lw=.8)
    ax.axvline(130, color="#aaaaaa", ls=":", lw=.8)
    ax.set(title="Research costs can reverse the choice", xlabel="Audit quota                         ◆ Direct validation", ylabel="Expected extra loss (lower is better)", xlim=(-2,138))
    ax.legend(fontsize=8, loc="lower left")
    ax = axes[1,1]
    policies = [next(r for r in rows if r["name"] == "none"), at28, direct]
    c = loss_matrix(rows)
    best = c.min(axis=0)
    mm = base["minimax_regret"]
    grouped = [[p["worlds"][w]["incremental_loss"]-best[j] for j,w in enumerate(("E","P","T","U"))] for p in policies]
    grouped.append([mm["world_regrets"][w] for w in ("E","P","T","U")])
    for i,(name, values, color) in enumerate(zip(("No inquiry", "Audit 28", "Direct", "Minimax lottery"), grouped,
                                               ("#b6bdc3", "#c3944b", "#455f72", "#358475"))):
        ax.bar(x+(i-1.5)*.2, values, .2, label=name, color=color)
    ax.set(xticks=x, xticklabels=["E","P","T","U"], title="Robust choice depends on the declared criterion", ylabel="Regret versus best workflow for that world")
    ax.legend(fontsize=8, ncol=2)
    for ax in axes.flat:
        ax.spines[["top","right"]].set_visible(False)
        ax.grid(axis="y", alpha=.14)
    fig.suptitle("Preserving a route to questions that current records cannot settle", fontsize=16)
    fig.supxlabel("Exact finite calculations • supplied four-world family • later continuation question probability 0.5\nCosts include all screened validation records and future order collection; no empirical data or universal optimum", fontsize=10)
    fig.savefig(OUT/"prospective-revision.png", dpi=170)
    fig.savefig(OUT/"prospective-revision.svg")
    plt.close(fig)


def main():
    if OUT.exists():
        raise SystemExit("results already exists; preserve it or choose a new output directory")
    OUT.mkdir()
    config = json.loads((HERE/"config.json").read_text())
    cfg = Params(**{f.name: config[f.name] for f in fields(Params)})
    base = solve(cfg, config["prior_grid_denominator"])
    question_cases = [solve(replace(cfg, question_probability=lam), config["prior_grid_denominator"])
                      for lam in config["question_grid"] if lam != cfg.question_probability]
    controls = []
    for q in (1/3, 2/3, 1.):
        for kind,p in (("true net-zero",cfg.response_cost+cfg.running_fee/eligibility(q)),
                       ("test threshold", cfg.threshold)):
            w = World(kind, q, p)
            controls.append({"q":q, "kind":kind, "p":p,
                             "net_gain_per_decision":eligibility(q)*(p-cfg.response_cost)-cfg.running_fee,
                             "validation_accept_probability":validation_power(w,cfg)})
    sensitivity = []
    choices = {"audit_fee":[.005,.08], "validation_fee":[.0005,.01],
               "running_fee":[0.,.01], "validation_size":[256,2048],
               "deployment_size":[100,1000], "expense_cap":[1.,3.],
               "question_probability":[0.]}
    for field, values in choices.items():
        for value in values:
            varied = replace(cfg, **{field:value})
            item = solve(varied, config["prior_grid_denominator"])
            item["changed"] = {field:value}
            sensitivity.append(item)
    result = {"status":"exploratory exact finite calculation, not empirical or held-out",
              "runtime":{"python":platform.python_version(),"numpy":np.__version__,
                         "scipy":scipy.__version__,"matplotlib":matplotlib.__version__},
              "world_order":[w.name for w in WORLDS], "net_validation_threshold":cfg.threshold,
              "base":base, "question_cases":question_cases, "boundary_controls":controls,
              "sensitivity":sensitivity}
    (OUT/"results.json").write_text(json.dumps(result, indent=2)+"\n")
    snapshots = OUT/"inputs"
    snapshots.mkdir()
    manifest = {}
    for name in ("model.py","test_model.py","analyze.py","config.json","PROTOCOL.md"):
        data = (HERE/name).read_bytes()
        (snapshots/name).write_bytes(data)
        manifest[name] = hashlib.sha256(data).hexdigest()
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    plot(result)
    report = {"threshold":cfg.threshold, "worlds":base["worlds"],
              "audit28":next(r for r in base["workflows"] if r["name"]=="audit-28"),
              "minimax":base["minimax_regret"], "winner_counts":base["winner_counts"],
              "question_winners":[{"lambda":c["parameters"]["question_probability"],
                                    "counts":c["winner_counts"]} for c in question_cases],
              "boundary_controls":controls}
    (OUT/"summary.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
