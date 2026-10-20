"""Verdicts of CG3 by the rules frozen in PREDICTIONS-2026-10-20.md.

    python3 analyze.py [results_dir]     # writes results_dir/VERDICTS.json and prints a table
"""

import json
import os
import sys

from conditions import CONDITIONS

KEEP_FROM = 0.80      # kept: mean over seeds of the share of evaluation episodes alive at H - 20
DEPLETE_TO = 0.20     # depleted: that share at most this


def main(rdir):
    runs = json.load(open(os.path.join(rdir, "runs.json")))["runs"]
    by = {}
    for r in runs:
        by.setdefault(r["cond"], []).append(r)
    out = dict(conditions={}, identity={}, contrasts={})
    tot = {}
    for r in runs:
        for key, val in list(r["checks"].items()) + [("emptied_" + k, v) for k, v in r["emptied"].items()]:
            tot[key] = tot.get(key, 0) + val
    i1 = dict(steps=tot["steps"], balance=tot["balance_viol"], gate=tot["gate_given_below"],
              margin=tot["margin_viol"], own_excess_windows=tot["je_windows"], own_excess=tot["je_viol"])
    i1["verdict"] = "passed" if (i1["balance"] == i1["gate"] == i1["margin"] == i1["own_excess"] == 0
                                 and i1["own_excess_windows"] > 0) else "failed"
    i2 = dict(episodes=tot["emptied_episodes"], violations=tot["emptied_violations"])
    i2["verdict"] = "passed" if i2["episodes"] > 0 and i2["violations"] == 0 else "failed"
    out["identity"] = dict(I1_cg1_checks_own_part=i1, I2_emptied_total=i2)
    mean = {}
    for name, c in CONDITIONS.items():
        rs = by.get(name, [])
        alive = [sum(1 for x in r["eval"]["alive_probe"] if x >= 1) / len(r["eval"]["alive_probe"]) for r in rs]
        alive_H = [sum(1 for x in r["eval"]["final"] if x >= 1) / len(r["eval"]["final"]) for r in rs]
        ret = [sum(r["eval"]["ret"]) / len(r["eval"]["ret"]) for r in rs]
        m = sum(alive) / len(alive)
        mean[name] = m
        if c["predicted"] == "kept":
            verdict = "passed" if m >= KEEP_FROM else "failed"
        elif c["predicted"] == "depleted":
            verdict = "passed" if m <= DEPLETE_TO else "failed"
        else:
            verdict = None   # J2: judged by the order (Y4)
        out["conditions"][name] = dict(
            predicted=c["predicted"], verdict=verdict, seeds=len(rs), alive_probe_mean=m,
            alive_probe_by_seed=alive, seeds_at_least_0_8=sum(a >= 0.8 for a in alive),
            seeds_at_most_0_2=sum(a <= 0.2 for a in alive), alive_at_H_mean=sum(alive_H) / len(alive_H),
            return_mean=sum(ret) / len(ret))
    order = mean["J3"] <= mean["J2"] <= mean["J1"]
    out["conditions"]["J2"]["verdict"] = "passed" if order else "failed"
    V = {n: out["conditions"][n]["verdict"] == "passed" for n in CONDITIONS}
    out["contrasts"] = dict(
        Y1_coverage_not_the_draw_cap=all(V[n] for n in ("J3", "J3s8", "J3s16")),
        Y2_not_the_end_weight=all(V[n] for n in ("J3", "J3w48")),
        Y3_not_the_end_reading=all(V[n] for n in ("J3w0", "J1w0")),
        Y4_order_in_the_draw_cap=all(V[n] for n in ("J1", "J2", "J3")),
        Y5_optimism_opens_it=V["J3opt"])
    json.dump(out, open(os.path.join(rdir, "VERDICTS.json"), "w"), indent=1)
    print(f"{'condition':8} {'predicted':9} {'alive@H-20':>10} {'>=.8':>5} {'<=.2':>5} {'alive@H':>8} {'return':>8}  verdict")
    for name, d in out["conditions"].items():
        print(f"{name:8} {d['predicted']:9} {d['alive_probe_mean']:10.2f} {d['seeds_at_least_0_8']:5d} "
              f"{d['seeds_at_most_0_2']:5d} {d['alive_at_H_mean']:8.2f} {d['return_mean']:8.1f}  {d['verdict']}")
    for k, v in out["identity"].items():
        print(k, v)
    for k, v in out["contrasts"].items():
        print(k, "passed" if v else "failed")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"))
