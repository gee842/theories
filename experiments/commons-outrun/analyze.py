"""Verdicts of CG2 by the rules frozen in PREDICTIONS-2026-10-20.md.

    python3 analyze.py [results_dir]     # writes results_dir/VERDICTS.json and prints a table
"""

import json
import os
import sys

from conditions import CONDITIONS, LOCKED_BELOW, OPEN_FROM

KEEP_FROM = 0.80      # kept: mean over seeds of the share of evaluation episodes alive at H - 20
DEPLETE_TO = 0.20     # depleted: that share at most this


def main(rdir):
    runs = json.load(open(os.path.join(rdir, "runs.json")))["runs"]
    cal = json.load(open(os.path.join(rdir, "calibration.json")))
    by = {}
    for r in runs:
        by.setdefault(r["cond"], []).append(r)
    out = dict(conditions={}, identity={}, contrasts={}, calibration_class={})
    # calibration classes (computed before the freeze): the prediction's premise
    for name, c in CONDITIONS.items():
        g = cal["gain"][name]["gain"]
        cls = "locked" if g < LOCKED_BELOW else ("open" if g >= OPEN_FROM else "between")
        out["calibration_class"][name] = dict(gain=g, cls=cls, as_frozen=(cls == c["lock"]))
    # identity checks
    tot = {}
    for r in runs:
        for key, val in list(r["checks"].items()) + [("outrun_" + k, v) for k, v in r["outrun"].items()]:
            tot[key] = tot.get(key, 0) + val
    ident = dict(
        I1_outrun=dict(windows=tot["outrun_windows"], violations=tot["outrun_violations"]),
        I2_emptied_total=dict(episodes=tot["outrun_emptied_episodes"],
                              violations=tot["outrun_emptied_violations"]),
        I3_cg1_checks=dict(steps=tot["steps"], balance=tot["balance_viol"],
                           gate=tot["gate_given_below"], margin=tot["margin_viol"],
                           joint_excess_windows=tot["je_windows"], joint_excess=tot["je_viol"]))
    ident["I1_outrun"]["verdict"] = ("passed" if ident["I1_outrun"]["windows"] > 0
                                     and ident["I1_outrun"]["violations"] == 0 else "failed")
    ident["I2_emptied_total"]["verdict"] = ("passed" if ident["I2_emptied_total"]["episodes"] > 0
                                            and ident["I2_emptied_total"]["violations"] == 0 else "failed")
    i3 = ident["I3_cg1_checks"]
    i3["verdict"] = "passed" if (i3["balance"] == i3["gate"] == i3["margin"] == i3["joint_excess"] == 0
                                 and i3["joint_excess_windows"] > 0) else "failed"
    out["identity"] = ident
    # per condition
    for name, c in CONDITIONS.items():
        rs = by.get(name, [])
        alive = [sum(1 for x in r["eval"]["alive_probe"] if x >= 1) / len(r["eval"]["alive_probe"]) for r in rs]
        alive_H = [sum(1 for x in r["eval"]["final"] if x >= 1) / len(r["eval"]["final"]) for r in rs]
        harv = [sum(sum(h) for h in r["eval"]["harvest"]) / len(r["eval"]["harvest"]) for r in rs]
        m = sum(alive) / len(alive)
        if c["predicted"] == "kept":
            verdict = "passed" if m >= KEEP_FROM else "failed"
        else:
            verdict = "passed" if m <= DEPLETE_TO else "failed"
        out["conditions"][name] = dict(
            predicted=c["predicted"], verdict=verdict, seeds=len(rs), alive_probe_mean=m,
            alive_probe_by_seed=alive, seeds_at_least_0_8=sum(a >= 0.8 for a in alive),
            seeds_at_most_0_2=sum(a <= 0.2 for a in alive), alive_at_H_mean=sum(alive_H) / len(alive_H),
            total_harvest_mean=sum(harv) / len(harv))
    V = {n: out["conditions"][n]["verdict"] == "passed" for n in CONDITIONS}
    out["contrasts"] = dict(
        X1_boundary_is_the_rest=all(V[n] for n in ("k2s1", "k2s8", "k3s8", "k3s16")),
        X2_end_weight_does_not_open=all(V[n] for n in ("k3s1", "k3s1_lam32")),
        X3_reading_before_the_end_opens_above_vstar=all(V[n] for n in ("k3s1_vlo", "k3s1_vhi")),
        X4_sharing_opens_only_with_renewal=all(V[n] for n in ("k3s1_share", "k3s8_share")),
        X5_joint_reading=V["k3s1_joint"])
    json.dump(out, open(os.path.join(rdir, "VERDICTS.json"), "w"), indent=1)
    print(f"{'condition':14} {'class':7} {'predicted':9} {'alive@H-20':>10} {'>=.8':>5} {'<=.2':>5} {'alive@H':>8} {'harvest':>8}  verdict")
    for name, d in out["conditions"].items():
        print(f"{name:14} {CONDITIONS[name]['lock']:7} {d['predicted']:9} {d['alive_probe_mean']:10.2f} "
              f"{d['seeds_at_least_0_8']:5d} {d['seeds_at_most_0_2']:5d} {d['alive_at_H_mean']:8.2f} "
              f"{d['total_harvest_mean']:8.1f}  {d['verdict']}")
    for k, v in out["identity"].items():
        print(k, v)
    for k, v in out["contrasts"].items():
        print(k, "passed" if v else "failed")
    for k, v in out["calibration_class"].items():
        if not v["as_frozen"]:
            print("calibration class differs from the frozen one:", k, v)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"))
