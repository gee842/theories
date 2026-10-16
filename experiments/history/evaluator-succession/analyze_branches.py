"""Audit and plot the sealed matched-state follow-up; does not generate new worlds."""
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import benchmark as base
from branch_engine import State

ROOT = Path(__file__).resolve().parent
OUT = ROOT/"results-v2"


def main():
    manifest = json.loads((OUT/"input_manifest.json").read_text())
    cfg, design = manifest["effective_config"], manifest["design"]
    checks = {}
    for name, expected in manifest["inputs"].items():
        checks[f"snapshot_hash/{name}"] = hashlib.sha256((OUT/"sealed-inputs"/name).read_bytes()).hexdigest() == expected
        checks[f"current_hash/{name}"] = base.digest(ROOT/name) == expected
    assert all(checks.values())
    worlds = dict(np.load(OUT/"shared-worlds.npz"))
    diagnostics, archives = {}, {}
    max_error = 0.
    for source in design["source_histories"]:
        prefix = np.load(OUT/f"prefix-{source}.npz")
        state = State.load(OUT/f"checkpoint-{source}.npz")
        ema = np.full((cfg["worlds"], cfg["agents"]), 1/cfg["agents"])
        for t in range(80):
            ema = (1-cfg["authority_memory"])*ema + cfg["authority_memory"]*prefix["shares"][:, t]
        assert ema.tobytes() == state.authority.tobytes()
        assert prefix["after_rubric"][:, 79].tobytes() == state.rubric.tobytes()
        assert prefix["frozen_outputs"][:, 79].tobytes() == state.outputs.tobytes()
        checks[f"prefix_restoration/{source}"] = True
        for context in design["contexts"]:
            first = None
            for arm in design["branches"]:
                key = f"{source}/{context}/{arm}"
                h = dict(np.load(OUT/f"branch-{source}-{context}-{arm}.npz"))
                archives[key] = h
                assert int(h["valid_start"]) == 80 and int(h["valid_stop"]) == 160
                assert str(h["source_state_hash"]) == state.fingerprint()
                assert h["before_rubric"][:, 80].tobytes() == state.rubric.tobytes()
                if first is None:
                    first = h
                for field in ("frozen_outputs", "gross", "shares"):
                    assert h[field][:, 80].tobytes() == first[field][:, 80].tobytes()
                np.testing.assert_array_equal(h["before_rubric"][:, 81:], h["after_rubric"][:, 80:-1])
                np.testing.assert_allclose(h["before_rubric"][:, 80:].sum(-1), 1)
                assert (h["before_rubric"][:, 80:] >= -1e-12).all()
                assert (h["governor"][:, 159] == -1).all()
                np.testing.assert_allclose(h["net"][:,80:], h["gross"][:,80:]-h["admin_cost"][:,80:])
                if arm != "fixed":
                    for t in range(80,159):
                        alpha = .25 if context == "shift" else .75
                        p0,w0,_ = base.evaluate(h["frozen_outputs"][:,t],h["before_rubric"][:,t],alpha,cfg)
                        p1,w1,_ = base.evaluate(h["frozen_outputs"][:,t],h["after_rubric"][:,t],alpha,cfg)
                        g=h["governor"][:,t]
                        dp=(p1-p0)[np.arange(cfg["worlds"]),g]
                        max_error=max(max_error,float(np.max(np.abs(dp-h["delta_governor"][:,t]))),
                                      float(np.max(np.abs(w1-w0-h["delta_value"][:,t]))))
                        np.testing.assert_allclose(w1-w0,h["delta_value"][:,t],atol=1e-12)
                        np.testing.assert_allclose(dp,h["delta_governor"][:,t],atol=1e-12)
                ev = h["evidence_valid"][:,80:].sum(-1)
                ok = h["corrected"][:,80:].sum(-1)
                nonzero = ev>0
                g=h["governor"][:,120:159]
                a_type=worlds["skills"][...,0]>worlds["skills"][...,1]
                diagnostics[key]=dict(opportunities=int(ev.sum()),corrections=int(ok.sum()),
                    worlds_without_opportunities=int((~nonzero).sum()),
                    mean_world_response=float(np.mean(ok[nonzero]/ev[nonzero])) if nonzero.any() else None,
                    late_a_governor_fraction=float(np.take_along_axis(a_type,g,axis=1).mean()) if arm!="fixed" else None,
                    late_a_rubric=float(h["before_rubric"][:,120:,0].mean()))
                checks[f"branch_receipts/{key}"]=True
    analysis=json.loads((OUT/"analysis.json").read_text())
    def values(source,context,arm):
        return archives[f"{source}/{context}/{arm}"]["gross"][:,120:].mean(-1)
    def delta(source,context):
        return values(source,context,"independent")-values(source,context,"endogenous")
    primary=[delta("endogenous","shift"),delta("independent","shift"),
             np.mean([delta(s,"shift")-delta(s,"stable") for s in design["source_histories"]],axis=0)]
    for test,diff in zip(analysis["tests"],primary):
        np.testing.assert_array_equal(test["differences"],diff)
        checks[f"primary_receipts/{test['id']}"]=True
    with (OUT/"world_summaries.csv").open() as f:
        rows=list(csv.DictReader(f))
    for row in rows:
        i=int(row["seed"])-cfg["seed_start"]
        h=archives[f"{row['source']}/{row['context']}/{row['arm']}"]
        for label,start in (("late",120),("postfork",80)):
            assert float(row[f"{label}_gross"])==h["gross"][i,start:].mean()
            assert float(row[f"{label}_net"])==h["net"][i,start:].mean()
    checks["csv_means_match_2048_world_branches"]=True
    audit=dict(checks=checks,maximum_frozen_rescoring_error=max_error,
               descriptive_correction_and_specialization=diagnostics,
               warning="Later correction opportunities are treatment-dependent; their conditional rates are descriptive.")
    (OUT/"audit.json").write_text(json.dumps(audit,indent=2)+"\n")

    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,
                         "axes.spines.top":False,"axes.spines.right":False,
                         "axes.spines.left":False,"axes.edgecolor":"#CCD3D8"})
    fig,axes=plt.subplots(1,2,figsize=(11,5.8),sharey=True)
    fig.subplots_adjust(left=.10,right=.96,top=.71,bottom=.24,wspace=.27)
    fig.suptitle("Changing appointments from the same inherited state",fontsize=17,fontweight="bold",y=.97)
    fig.text(.5,.875,"Success-based appointments retained a stable-demand advantage;\nindependent appointments adapted better after demand changed.",ha="center",fontsize=11,color="#4D5D6C")
    for ax,source in zip(axes,design["source_histories"]):
        for arm,color,label in (("endogenous","#BB4C35","Appointments based on success"),
                                ("independent","#3177A6","Independent appointments")):
            means=[]; errors=[]
            for context in ("stable","shift"):
                v=values(source,context,arm)
                means.append(v.mean());errors.append(1.96*v.std(ddof=1)/np.sqrt(len(v)))
            ax.errorbar([0,1],means,yerr=errors,color=color,lw=2,marker="o",capsize=4,label=label)
        ax.set_xticks([0,1],["Demand unchanged","Demand changed"])
        ax.set_xlim(-.18,1.18);ax.set_ylim(.25,.75)
        ax.set_title("History: success-based appointments" if source=="endogenous" else "History: independent appointments",fontsize=11,pad=16)
        ax.grid(axis="y",alpha=.18)
        ax.set_ylabel("Late independent usefulness")
    handles,labels=axes[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc="lower center",bbox_to_anchor=(.53,.11),ncol=2,frameon=False)
    fig.text(.10,.045,"128 fresh paired worlds • same snapshot within each history • final 40 epochs\nBars: 95% normal intervals across worlds. Synthetic agents; one configuration; immediate policy reform assumed.",fontsize=8.5,color="#596675")
    fig.savefig(OUT/"matched-state-results.png",dpi=180)
    fig.savefig(OUT/"matched-state-results.svg")
    print(json.dumps({"all_checks_passed":all(checks.values()),"checks":len(checks),
                      "maximum_rescoring_error":max_error,"figure":str(OUT/"matched-state-results.png")},indent=2))


if __name__=="__main__":
    main()
