"""Verdict rules of PREDICTIONS-2026-10-20.md, applied to results/. Part of the freeze.

    python3 analyze.py [results_dir]

Writes VERDICTS.json into the results directory and prints a table. Each prediction is
passed, failed, or not testable (a case the rule did not foresee is not testable, never passed).
"""

import json
import math
import os
import statistics
import sys

import garden as G

CENSOR = 10 ** 6


def ks_p(a, b):
    """Two-sample Kolmogorov-Smirnov statistic and asymptotic p-value (Stephens' correction)."""
    a, b = sorted(a), sorted(b)
    n1, n2 = len(a), len(b)
    i = j = 0
    d = 0.0
    while i < n1 and j < n2:
        x = min(a[i], b[j])
        while i < n1 and a[i] == x:
            i += 1
        while j < n2 and b[j] == x:
            j += 1
        d = max(d, abs(i / n1 - j / n2))
    ne = n1 * n2 / (n1 + n2)
    lam = (math.sqrt(ne) + 0.12 + 0.11 / math.sqrt(ne)) * d
    if lam < 1e-9:
        return d, 1.0
    p = 2 * sum((-1) ** (k - 1) * math.exp(-2 * k * k * lam * lam) for k in range(1, 101))
    return d, max(0.0, min(1.0, p))


def mean_se(xs):
    m = statistics.mean(xs)
    se = statistics.stdev(xs) / math.sqrt(len(xs)) if len(xs) > 1 else 0.0
    return m, se


def load(d, name):
    path = os.path.join(d, name)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------- A

def verdict_a1(a1):
    tests = {}
    for key in a1:
        df, hist, kind = key.split("/")
        tests.setdefault((df, kind), {})[hist] = [CENSOR if t is None else t
                                                  for t in a1[key]["taus"]]
    out = {"scalar": {}, "memory": {}}
    for (df, kind), byh in tests.items():
        pairs = [("h_long", "h_short"), ("h_long", "h_below"), ("h_short", "h_below")]
        out[kind][df] = {f"{x}~{y}": ks_p(byh[x], byh[y]) for x, y in pairs}
    scalar_ok = all(p >= 0.01 for d in out["scalar"].values() for (_, p) in d.values())
    memory_ok = all(any(p < 0.001 for (_, p) in d.values()) for d in out["memory"].values())
    return dict(A1=("passed" if scalar_ok else "failed"),
                A1_manipulation=("passed" if memory_ok else "failed"), detail=out)


def verdict_a2(a2):
    cells = {}
    ok = n = 0
    for key, c in a2.items():
        if not c["applicable"]:
            cells[key] = "not applicable (harvest >= margin)"
            continue
        taus = [200 if t is None else t for t in c["taus"]]
        censored = sum(1 for t in c["taus"] if t is None)
        m, se = mean_se(taus)
        lower = c["m0"] / c["harvest"] - 1
        upper = (c["m0"] - c["harvest"]) / (c["harvest"] - c["yield_"]) + 1
        inside = (m >= lower - 2 * se) and (m <= upper + 2 * se)
        pos = (m - lower) / (upper - lower) if upper > lower else None
        cells[key] = dict(mean=m, se=se, lower=lower, upper=upper, inside=inside,
                          position=pos, censored=censored, width_ratio=upper / max(lower, 1e-9))
        n += 1
        ok += inside
    if n == 0:
        return dict(A2="not testable", cells=cells)
    return dict(A2=("passed" if ok >= 0.9 * n else "failed"), inside=ok, cells_tested=n,
                cells=cells)


def verdict_a3(a3):
    cells = {}
    ok = n = 0
    untestable = 0
    for key, c in a3.items():
        if c["point_of_no_return"] is None:
            cells[key] = "not testable (harvest unsustainable from the stable state)"
            untestable += 1
            continue
        excess = c["point_of_no_return"] - (c["need"] + c["harvest"])
        cells[key] = dict(point_of_no_return=c["point_of_no_return"], need=c["need"],
                          harvest=c["harvest"], above_need_plus_harvest=excess,
                          shift=c["point_of_no_return"] - c["need"])
        n += 1
        ok += excess > 0
    if n == 0:
        return dict(A3="not testable", cells=cells)
    return dict(A3=("passed" if ok == n else "failed"), held=ok, cells_tested=n,
                untestable=untestable, cells=cells)


def verdict_a4(a4):
    cells = {}
    a_ok = True
    beyond_n = beyond_ok = within_n = within_pos = 0
    additive_frozen = True
    for key, c in a4.items():
        inter = [r["one"] + r["two"] - r["both"] - r["none"] for r in c["rows"]]
        m, se = mean_se(inter)
        harm = {k: statistics.mean(r["none"] - r[k] for r in c["rows"]) for k in ("one", "two",
                                                                                   "both")}
        frozen = [sum(r["takes"]) for r in c["rows"]]   # frozen-rest harm of the joint = sum of takes
        beyond = c["h1"] + c["h2"] > c["yield_"]
        cells[key] = dict(interaction=m, se=se, beyond=beyond, harm=harm,
                          joint_takes_mean=statistics.mean(frozen),
                          collapse_both=sum(1 for r in c["rows"] if r["both"] <= 0) / len(c["rows"]))
        a_ok &= m >= -2 * se
        if beyond:
            beyond_n += 1
            beyond_ok += m > 2 * se
        else:
            within_n += 1
            within_pos += m > 2 * se
    res = dict(A4a=("passed" if a_ok else "failed"),
               A4b=("not testable" if beyond_n == 0 else
                    ("passed" if beyond_ok == beyond_n else "failed")),
               A4c=("not testable" if within_n == 0 else
                    ("passed" if within_pos >= 0.5 * within_n else "failed")),
               counts=dict(beyond=beyond_n, beyond_superadditive=beyond_ok, within=within_n,
                           within_superadditive=within_pos), cells=cells)
    return res


# ---------------------------------------------------------------- B

def records(b):
    for key, v in b["dp"].items():
        yield f"dp/{key}/solo", v["solo"]
        yield f"dp/{key}/joint", v["joint"]
    for key, v in b["q"].items():
        yield f"q/{key}", v
    for key, v in b["q_joint"].items():
        yield f"qjoint/{key}", v


def binding(b):
    """(variant, cell) pairs whose cell the blind best response kills within the horizon."""
    out = set()
    for vn in G.VARIANTS:
        ds = b["dp"][f"blind/{vn}"]["solo"]["death_step"]
        for k in range(2):
            if ds[k] is not None:
                out.add((vn, k))
    return out


def predict(entries, l0, r):
    lower, upper = G.death_band(entries, l0, r)
    if upper is not None:
        return "death", lower, upper
    if lower is None:
        return "survive", lower, upper
    return "undecided", lower, upper


def transfer(ref, target, vn):
    """B4's rule: predict each cell's fate in variant vn from the reference record's entries."""
    v = G.VARIANTS[vn]
    rows = []
    for k in range(2):
        l0, r = v[2 * k], v[2 * k + 1]
        pred, lo, up = predict(ref["entries"][0][k], l0, r)
        obs = target["death_step"][k]
        rows.append(dict(cell=k, pred=pred, lower=lo, upper=up, observed=obs,
                         correct=(None if pred == "undecided" else
                                  (pred == "death") == (obs is not None)),
                         within=(None if not (pred == "death" and obs is not None) else
                                 lo <= obs <= up)))
    return rows


def verdict_b(b):
    H = b["H"]
    res = {}
    # B1 accounting
    mism = sum(r["accounting_mismatch"] for _, r in records(b))
    nrec = sum(1 for _ in records(b))
    res["B1"] = dict(verdict="passed" if mism == 0 else "failed", mismatches=mism, records=nrec)
    # B2 coupling by intervention
    blind_zero = all(all(c == 0 for c in agent) for key, r in records(b) if "blind" in key
                     for agent in r["coupling"])
    other_pos = all(all(c > 0 for c in agent) for key, r in records(b)
                    if ("end" in key or "step" in key) for agent in r["coupling"])
    res["B2"] = dict(verdict="passed" if blind_zero and other_pos else "failed",
                     blind_zero=blind_zero, coupled_positive=other_pos)
    # B3 blind behaviour does not depend on the margin
    dp_same = len({json.dumps(b["dp"][f"blind/{vn}"]["solo"]["actions"]) for vn in G.VARIANTS}) == 1
    seeds = sorted({int(k.split("/")[2]) for k in b["q"]})
    means = {}
    for vn in G.VARIANTS:
        means[vn] = [statistics.mean(len(b["q"][f"blind/{vn}/{s}"]["entries"][0][k]) for s in seeds)
                     for k in range(2)]
    rel = {vn: [abs(means[vn][k] - means["V0"][k]) / max(means["V0"][k], 1e-9) for k in range(2)]
           for vn in G.VARIANTS}
    q_ok = all(x <= 0.10 for vn in rel for x in rel[vn])
    res["B3"] = dict(dp=("passed" if dp_same else "failed"), q=("passed" if q_ok else "failed"),
                     mean_entries=means, relative_difference=rel)
    # B4 side effects from blind draw vs margin, transferred from the ample-margin reference
    def b4(rows_list):
        dec = [r for r in rows_list if r["correct"] is not None]
        corr = sum(r["correct"] for r in dec)
        wb = [r for r in rows_list if r["within"] is not None]
        within = sum(r["within"] for r in wb)
        base = sum((r["observed"] is None) for r in dec)    # V0-outcome predictor: no deaths
        return dict(decided=len(dec), correct=corr, undecided=len(rows_list) - len(dec),
                    death_cases=len(wb), within_band=within, baseline_correct=base)
    dp_rows = []
    for vn in G.VARIANTS:
        if vn == "V0":
            continue
        dp_rows += transfer(b["dp"]["blind/V0"]["solo"], b["dp"][f"blind/{vn}"]["solo"], vn)
    q_rows = []
    for s in seeds:
        for vn in G.VARIANTS:
            if vn == "V0":
                continue
            q_rows += transfer(b["q"][f"blind/V0/{s}"], b["q"][f"blind/{vn}/{s}"], vn)
    dps, qs = b4(dp_rows), b4(q_rows)
    dp_pass = dps["decided"] > 0 and dps["correct"] == dps["decided"] and \
        dps["within_band"] == dps["death_cases"]
    q_pass = qs["decided"] > 0 and qs["correct"] >= 0.9 * qs["decided"] and \
        (qs["death_cases"] == 0 or qs["within_band"] >= 0.9 * qs["death_cases"])
    res["B4"] = dict(dp=("passed" if dp_pass else "failed"), q=("passed" if q_pass else "failed"),
                     dp_stats=dps, q_stats=qs)
    # B5 coupled draw adapts: end coupling
    bind = binding(b)
    dp_alive = all(min(b["dp"][f"end/{vn}"]["solo"]["end_levels"]) >= 1 for vn in G.VARIANTS)
    dp_spent = all(b["dp"][f"end/{vn}"]["solo"]["end_levels"][k] <= 2 for vn, k in bind)
    q_bind = [(vn, k, s) for vn, k in bind for s in seeds]
    q_alive = sum(b["q"][f"end/{vn}/{s}"]["end_levels"][k] >= 1 for vn, k, s in q_bind)
    pred_death = obs_death = 0
    for vn, k, s in q_bind:
        row = transfer(b["q"][f"end/V0/{s}"], b["q"][f"end/{vn}/{s}"], vn)[k]
        pred_death += row["pred"] == "death"
        obs_death += row["observed"] is not None
    nb = len(q_bind)
    res["B5"] = dict(
        dp=("not testable" if not bind else
            ("passed" if dp_alive and dp_spent else "failed")),
        q=("not testable" if nb == 0 else
           ("passed" if q_alive >= 0.8 * nb and pred_death >= 0.8 * nb and obs_death <= 0.2 * nb
            else "failed")),
        binding=sorted(bind), dp_all_alive=dp_alive, dp_binding_end_levels={
            f"{vn}/{k}": b["dp"][f"end/{vn}"]["solo"]["end_levels"][k] for vn, k in bind},
        q_cases=nb, q_alive=q_alive, transfer_predicted_death=pred_death, observed_death=obs_death)
    # B6 step coupling: blind draw where the coupling's remaining reach is small
    dp_deaths = [(vn, k, b["dp"][f"step/{vn}"]["solo"]["death_step"][k]) for vn in G.VARIANTS
                 for k in range(2) if b["dp"][f"step/{vn}"]["solo"]["death_step"][k] is not None]
    dp6 = ("failed (vacuous: no death)" if not dp_deaths else
           ("passed" if all(t >= H - 5 for _, _, t in dp_deaths) else "failed"))
    q_early = sum(1 for vn, k, s in q_bind
                  if (b["q"][f"step/{vn}/{s}"]["death_step"][k] is not None and
                      b["q"][f"step/{vn}/{s}"]["death_step"][k] < H - 6))
    q_deaths = [b["q"][f"step/{vn}/{s}"]["death_step"][k] for vn, k, s in q_bind
                if b["q"][f"step/{vn}/{s}"]["death_step"][k] is not None]
    res["B6"] = dict(dp=dp6, q=("not testable" if nb == 0 else
                                ("passed" if q_early <= 0.2 * nb else "failed")),
                     dp_deaths=dp_deaths, q_cases=nb, q_early_deaths=q_early,
                     q_death_steps=sorted(q_deaths))
    # B7 two end-coupled agents trained alone, together
    bind_vars = sorted({vn for vn, _ in bind})
    dp_joint = sum(1 for vn in bind_vars if min(b["dp"][f"end/{vn}"]["joint"]["end_levels"]) == 0)
    pairs = sorted({int(k.split("/")[2]) for k in b["q_joint"]})
    qj = [(vn, i) for vn in bind_vars for i in pairs]
    qj_dead = sum(1 for vn, i in qj if min(b["q_joint"][f"end/{vn}/{i}"]["end_levels"]) == 0)
    band_cases = band_in = 0
    for vn in bind_vars:
        v = G.VARIANTS[vn]
        sources = [("dp", b["dp"][f"end/{vn}"]["joint"],
                    [b["dp"][f"end/{vn}"]["solo"]] * 2)]
        sources += [("q", b["q_joint"][f"end/{vn}/{i}"],
                     [b["q"][f"end/{vn}/{2 * i}"], b["q"][f"end/{vn}/{2 * i + 1}"]]) for i in pairs]
        for _, jrec, solos in sources:
            for k in range(2):
                obs = jrec["death_step"][k]
                if obs is None:
                    continue
                merged = sorted(solos[0]["entries"][0][k] + solos[1]["entries"][0][k])
                lo, up = G.death_band(merged, v[2 * k], v[2 * k + 1])
                band_cases += 1
                band_in += (lo is not None and up is not None and lo <= obs <= up)
    res["B7"] = dict(
        dp=("not testable" if not bind_vars else
            ("passed" if dp_joint >= 0.5 * len(bind_vars) else "failed")),
        q=("not testable" if not qj else ("passed" if qj_dead >= 0.5 * len(qj) else "failed")),
        band=("not testable" if band_cases == 0 else
              ("passed" if band_in >= 0.5 * band_cases else "failed")),
        dp_joint_deaths=dp_joint, binding_variants=bind_vars, q_pairs=len(qj),
        q_joint_deaths=qj_dead, band_cases=band_cases, band_within=band_in,
        solo_end_levels={vn: b["dp"][f"end/{vn}"]["solo"]["end_levels"] for vn in G.VARIANTS})
    return res


def main(d):
    out = {}
    for name, fn in (("a1.json", verdict_a1), ("a2.json", verdict_a2), ("a3.json", verdict_a3),
                     ("a4.json", verdict_a4), ("b.json", verdict_b)):
        data = load(d, name)
        out[name.split(".")[0]] = fn(data) if data is not None else "not run"
    m = load(d, "measure.json")
    if m is not None:
        out["measure"] = m
    with open(os.path.join(d, "VERDICTS.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    for part, v in out.items():
        if isinstance(v, dict):
            short = {k: (x if isinstance(x, str) else x.get("verdict", x.get("dp", ""))
                         if isinstance(x, dict) else x)
                     for k, x in v.items() if k[0] in "AB" or k in ("dp", "q", "band")}
            print(part, json.dumps(short, default=str)[:600])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "results"))
