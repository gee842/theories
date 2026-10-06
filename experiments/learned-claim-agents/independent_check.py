"""Independent reconstruction of the learned-claim-agents environment, metrics
and record_rule, written from PROTOCOL.md alone (before reading model.py or
check.py). Evaluates record_rule on all seven tests with its own RNG and
compares with results.json. Run: python -I independent_check.py [--out PATH]
"""
import json, sys, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = {"A": 0, "B": 1, "C": 2}
N_EP = 20000
HORIZON = 4
P_SUCCESS = 0.9

TESTS = {
    "train": dict(ids=("A", "B"), kdist=((0, 1, 2), (0.25, 0.5, 0.25)), pool=3, record="faithful"),
    "new_claimant": dict(ids=("A", "C"), kdist=((0, 1, 2), (0.25, 0.5, 0.25)), pool=3, record="faithful"),
    "large_claims": dict(ids=("A", "B"), kdist=((1, 2), (0.25, 0.75)), pool=4, record="faithful"),
    "missing_records": dict(ids=("A", "B"), kdist=((0, 1, 2), (0.25, 0.5, 0.25)), pool=3, record="missing"),
    "forged_records": dict(ids=("A", "B"), kdist=((0, 1, 2), (0.25, 0.5, 0.25)), pool=3, record="forged"),
    "scarce_symmetric": dict(ids=("A", "B"), kdist=((1,), (1.0,)), pool=1, record="faithful"),
    "scarce_symmetric_swapped": dict(ids=("B", "A"), kdist=((1,), (1.0,)), pool=1, record="faithful"),
}


def record_rule(obs):
    """obs: list of per-recipient dicts with id, k, c, u (records only)."""
    best, best_need = None, 0
    for slot, r in enumerate(obs):
        need = r["k"] - r["c"] - r["u"]
        if need > best_need or (need == best_need and best is not None and need > 0
                                and IDX[r["id"]] < IDX[obs[best]["id"]]):
            best, best_need = slot, need
    return best  # None = withhold


def run_episode(rng, cfg):
    ks = [int(rng.choice(cfg["kdist"][0], p=cfg["kdist"][1])) for _ in cfg["ids"]]
    actual = [0, 0]           # actual successful deliveries (observer fact)
    c = [0, 0]; u = [0, 0]    # records
    pool = cfg["pool"]
    withheld_unmet = 0
    first = None
    for step in range(HORIZON):
        obs = [dict(id=cfg["ids"][i], k=ks[i], c=c[i], u=u[i]) for i in range(2)]
        a = record_rule(obs)  # sees records, pool, step only
        if a is None:
            if pool > 0 and any(actual[i] < ks[i] for i in range(2)):
                withheld_unmet += 1
            continue
        if pool <= 0:
            continue  # serving with empty pool does nothing
        if first is None:
            first = a
        pool -= 1
        ok = rng.random() < P_SUCCESS
        if ok:
            actual[a] += 1
        mode = cfg["record"]
        if mode == "faithful":
            c[a] += int(ok)
        elif mode == "missing":
            if rng.random() < 0.5:
                u[a] += 1
            else:
                c[a] += int(ok)
        elif mode == "forged":
            if ok or rng.random() < 0.5:
                c[a] += 1
    met_units = sum(min(actual[i], ks[i]) for i in range(2))
    denom = min(sum(ks), cfg["pool"])
    excess = sum(max(0, actual[i] - ks[i]) for i in range(2))
    firstA = None if first is None else int(cfg["ids"][first] == "A")
    return met_units, denom, excess, pool, withheld_unmet, firstA


def evaluate(cfg, seed):
    rng = np.random.default_rng(seed)
    rows = np.array([[np.nan if v is None else v for v in run_episode(rng, cfg)] for _ in range(N_EP)], float)
    met_u, den, exc, ret, wu, fa = rows.T
    pos = den > 0
    ratio = met_u[pos] / den[pos]
    fa_ok = fa[~np.isnan(fa)]
    se = lambda x: float(np.std(x, ddof=1) / np.sqrt(len(x))) if len(x) > 1 else 0.0
    return {
        "met_ratio_of_sums": float(met_u.sum() / den.sum()),
        "met_mean_of_ratios_excl_zero": float(ratio.mean()), "met_mean_of_ratios_se": se(ratio),
        "excess": float(exc.mean()), "excess_se": se(exc),
        "retained": float(ret.mean()), "retained_se": se(ret),
        "withheld_unmet": float(wu.mean()), "withheld_unmet_se": se(wu),
        "first_choice_A": float(fa_ok.mean()) if len(fa_ok) else None, "first_choice_A_se": se(fa_ok),
        "first_served_fraction": float(len(fa_ok) / N_EP),
        # approximate SE of ratio-of-sums by delta method
        "met_ratio_of_sums_se": float(np.std(met_u - (met_u.sum() / den.sum()) * den, ddof=1)
                                      / (den.mean() * np.sqrt(N_EP))),
    }


def main():
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "/tmp/claude-0/indep2/step1.json"
    res = json.load(open(os.path.join(HERE, "results.json")))["results"]["record_rule"]
    comp = {}
    for t, (name, cfg) in enumerate(TESTS.items()):
        mine = evaluate(cfg, 900_000 + t)
        seeds = sorted(res.keys(), key=int)
        theirs = {m: float(np.mean([res[s][name][m] for s in seeds])) for m in
                  ("met", "excess", "retained", "withheld_unmet", "first_choice_A")}
        theirs["first_served_fraction"] = float(np.mean([res[s][name]["first_served_episodes"] for s in seeds]) / 2000)
        n_theirs = 2000 * len(seeds)
        rows = {}
        for m, mk in (("met", "met_ratio_of_sums"), ("excess", "excess"), ("retained", "retained"),
                      ("withheld_unmet", "withheld_unmet"), ("first_choice_A", "first_choice_A")):
            se_m = mine.get(mk + "_se", 0.0)
            se_comb = float(np.sqrt(se_m ** 2 + se_m ** 2 * N_EP / n_theirs))  # their n=20000 too
            d = mine[mk] - theirs[m]
            rows[m] = dict(mine=mine[mk], results_json=theirs[m], diff=d, approx_se_diff=se_comb,
                           z=(d / se_comb) if se_comb > 0 else (0.0 if abs(d) < 1e-12 else float("inf")))
        rows["met_alt_mean_of_ratios"] = mine["met_mean_of_ratios_excl_zero"]
        rows["first_served_fraction"] = dict(mine=mine["first_served_fraction"], results_json=theirs["first_served_fraction"])
        comp[name] = rows
    json.dump(comp, open(out, "w"), indent=1)
    for n, r in comp.items():
        print(n, {m: (round(v["diff"], 4), round(v["approx_se_diff"], 4)) for m, v in r.items() if isinstance(v, dict) and "diff" in v},
              "alt_met", round(r["met_alt_mean_of_ratios"], 4))


if __name__ == "__main__":
    main()
