"""Compute each frozen prediction's verdict from results/ and write results/VERDICTS.json.

The criteria here are those of PREDICTIONS-2026-10-20.md, frozen with this file before any
learning run.  Verdicts: passed, failed, not testable.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, "results")


def load(name):
    p = os.path.join(R, name)
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def add_checks(acc, c):
    for k, v in c.items():
        acc[k] = acc.get(k, 0) + v


def verdict(ok):
    return "passed" if ok else "failed"


def main():
    out = {}
    ab, c, d1, d2, e = (load(n) for n in ("ab.json", "c.json", "d1.json", "d2.json", "e.json"))

    # ---------------- A1 and B1: every logged episode at an isolated patch
    acc = {}
    for blob in (c, d1, d2):
        for r in (blob or {}).get("runs", []):
            add_checks(acc, r["checks"])
    for r in (ab or {}).get("rate", []):
        add_checks(acc, r["checks"])
    for r in (ab or {}).get("adjoining", []):
        if r["spec"]["gap"] >= 2:
            add_checks(acc, r["alone"])
    out["A1"] = dict(
        verdict=verdict(acc.get("je_viol", 1) == 0 and acc.get("balance_viol", 1) == 0
                        and acc.get("gate_given_below", 1) == 0 and acc.get("je_windows", 0) > 0),
        checks=acc)
    out["B1"] = dict(verdict=verdict(acc.get("margin_viol", 1) == 0
                                     and acc.get("margin_checked", 0) > 0),
                     margin_checked=acc.get("margin_checked"), margin_viol=acc.get("margin_viol"))

    # ---------------- A2: the gate's scope
    if ab:
        adj = {r["spec"]["gap"]: r for r in ab["adjoining"]}
        g1, g2 = adj[1], adj[2]
        ok = (g1["alone"]["je_viol"] >= 1 and g1["runs_regrew_after_zero"] >= 1
              and g1["union"]["je_viol"] == 0 and g2["alone"]["je_viol"] == 0
              and g2["runs_regrew_after_zero"] == 0 and g1["crosses"] and not g2["crosses"])
        out["A2"] = dict(verdict=verdict(ok),
                         gap1=dict(crosses=g1["crosses"], alone=g1["alone"], union=g1["union"],
                                   runs_regrew_after_zero=g1["runs_regrew_after_zero"]),
                         gap2=dict(crosses=g2["crosses"], alone=g2["alone"],
                                   runs_regrew_after_zero=g2["runs_regrew_after_zero"]))

        # ---------------- B2: rate form of the margin
        rows = []
        ok = True
        testable = True
        for r in ab["rate"]:
            q = r["spec"]["q"]
            bound = 9 / (q - 0.3)
            mean = sum(r["collapse"]) / len(r["collapse"])
            if r["censored"]:
                testable = False
            ok = ok and mean <= bound
            rows.append(dict(q=q, bound=round(bound, 3), mean_collapse=round(mean, 3),
                             censored=r["censored"], runs=len(r["collapse"])))
        out["B2"] = dict(verdict=(verdict(ok) if testable else "not testable"), rows=rows)

    # ---------------- C: the selection gap at the horizon
    def pooled(blob, cond):
        runs = [r for r in blob["runs"] if r["cond"] == cond]
        last = [a for r in runs for ep in r["eval"]["last_step"] for (_, a) in ep]
        final = [f[0] for r in runs for f in r["eval"]["final"]]
        alive = [x[0] for r in runs for x in r["eval"]["alive_at"]]
        harvest = [sum(h) for r in runs for h in r["eval"]["harvest"]]
        return dict(
            runs=len(runs),
            last_step_decisions=len(last),
            last_step_harvest_rate=(sum(last) / len(last)) if last else None,
            mean_final=sum(final) / len(final),
            dead_rate=sum(1 for x in final if x == 0) / len(final),
            survival=sum(1 for x in final if x >= 1) / len(final),
            alive_at_probe=sum(1 for x in alive if x >= 1) / len(alive),
            mean_eval_harvest=sum(harvest) / len(harvest),
            per_seed_survival=[sum(1 for f in r["eval"]["final"] if f[0] >= 1) / len(r["eval"]["final"])
                               for r in runs],
        )

    if c:
        own, cou = pooled(c, "own"), pooled(c, "coupled")
        cal = load("calibration.json")
        always = [r for r in cal["threshold_policies_H100"] if r["theta"] == 0][0]["mean_harvest"]
        learned = own["mean_eval_harvest"] > always  # better than harvesting at every step
        out["sanity_c"] = dict(own_mean_eval_harvest=own["mean_eval_harvest"],
                               harvest_always_mean=always, learned=learned)
        nt = "not testable"
        out["C1"] = dict(
            verdict=(verdict(own["last_step_harvest_rate"] >= 0.95
                             and cou["last_step_harvest_rate"] <= 0.05) if learned else nt),
            own_last_step_harvest_rate=own["last_step_harvest_rate"],
            coupled_last_step_harvest_rate=cou["last_step_harvest_rate"],
            decisions=(own["last_step_decisions"], cou["last_step_decisions"]))
        out["C2"] = dict(
            verdict=(verdict(cou["mean_final"] - own["mean_final"] >= 2.0
                             and own["dead_rate"] >= 0.5 and cou["survival"] >= 0.9)
                     if learned else nt),
            own=dict(mean_final=own["mean_final"], dead_rate=own["dead_rate"]),
            coupled=dict(mean_final=cou["mean_final"], survival=cou["survival"]))
        out["C3"] = dict(verdict=(verdict(own["alive_at_probe"] >= 0.8) if learned else nt),
                         own_alive_at_H_minus_20=own["alive_at_probe"])
        out["C_detail"] = dict(own=own, coupled=cou)

    # ---------------- D1: pool blindness, bit for bit
    if d1:
        by = {}
        for r in d1["runs"]:
            by.setdefault(r["seed"], {})[r["cond"]] = r
        same = 0
        b_final = {"B_own": [], "B_coupled": []}
        for s, pair in by.items():
            a, b = pair["B_own"], pair["B_coupled"]
            qa = a["q"][:2] == b["q"][:2]
            pa = [p[0] for p in a["eval"]["paths"]] == [p[0] for p in b["eval"]["paths"]]
            ha = [h[:2] for h in a["eval"]["harvest"]] == [h[:2] for h in b["eval"]["harvest"]]
            same += int(qa and pa and ha)
            for cond in b_final:
                b_final[cond] += [f[1] for f in pair[cond]["eval"]["final"]]
        mb = {k: sum(v) / len(v) for k, v in b_final.items()}
        out["D1"] = dict(verdict=verdict(same == len(by) and len(by) > 0
                                         and abs(mb["B_coupled"] - mb["B_own"]) >= 1.0),
                         seeds_identical=same, seeds=len(by), B_mean_final=mb)

    # ---------------- D2: one coupled member in a pool
    if d2:
        P = {cond: pooled(d2, cond) for cond in
             ("own3", "c1own2", "c2own1", "c3", "own2", "own1", "c1")}
        s = {k: v["survival"] for k, v in P.items()}
        out["D2a"] = dict(verdict=verdict(s["c1own2"] <= s["own2"] + 0.10
                                          and s["c2own1"] <= s["own1"] + 0.10),
                          survival=s)
        out["D2b"] = dict(verdict=verdict(s["c3"] >= 0.80 and s["c3"] >= s["c2own1"] + 0.30),
                          survival=s)
        out["D_detail"] = P

    # ---------------- E: late reading
    if e:
        rows = e["rows"]
        e1 = [r for r in rows if r["overseer"] == "late_return" and r["band"] == "wide"]
        out["E1"] = dict(verdict=verdict(len(e1) > 0 and all(
            not r["adversary_exits"] and r["const_exits"] == 0 and r["random_exit_rate"] == 0
            for r in e1)), cells=len(e1))
        out["E2"] = dict(verdict=verdict(len(rows) > 0 and all(
            r["const_spread"] >= r["bound"] for r in rows)),
            min_margin=min(r["const_spread"] - r["bound"] for r in rows))
        e3 = {}
        for r in rows:
            if r["band"] == "narrow":
                e3.setdefault((r["ell"], r["overseer"]), []).append(r["adversary_exits"])
        cells = {f"ell={k[0]},{k[1]}": sum(v) for k, v in sorted(e3.items())}
        out["E3"] = dict(verdict=verdict(len(e3) > 0 and all(sum(v) >= 9 for v in e3.values())),
                         adversary_exit_seeds_of_10=cells)
        desc = {}
        for r in rows:
            k = f"ell={r['ell']},{r['band']},{r['overseer']}"
            desc.setdefault(k, []).append(r["random_exit_rate"])
        out["E_random_rest_exit_rate"] = {k: sum(v) / len(v) for k, v in sorted(desc.items())}

    with open(os.path.join(R, "VERDICTS.json"), "w") as f:
        json.dump(out, f, indent=1)
    for k, v in out.items():
        if isinstance(v, dict) and "verdict" in v:
            print(k, v["verdict"])


if __name__ == "__main__":
    main()
