"""Run the frozen configurations of PREDICTIONS-2026-10-20.md and write results/.

    python3 run.py all          # every experiment (CPU, standard library, 12 processes)
    python3 run.py measure a1 a2 a3 a4 b
    python3 run.py smoke        # tiny run of every code path into results/smoke/ (not read)

`measure` must run before a1-a4 (they read results/measure.json). Configurations are in CONFIG
below and are part of the freeze.
"""

import json
import os
import random
import statistics
import sys
import time
from multiprocessing import Pool

import garden as G
import yeast as Y

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

CONFIG = dict(
    dfs=[500, 750, 1000, 1400],
    measure=dict(reps=200, stationary_reps=200, stationary_day=15, pulse_days=20,
                 yield_days=60, seed=1000),
    a1=dict(dfs=[500, 750], reps=400, harvest=1.5, seed=200000),
    a2=dict(x0=["stable", "half"], harvests=[1.25, 1.5, 2.0, 3.0], reps=400, seed=300000),
    a3=dict(harvests=[0.25, 0.5, 0.75], reps=200, days=60, seed=400000),
    a4=dict(dfs=[750, 1400], levels=[0.3, 0.5, 0.7], days=30, reps=400, seed=500000),
    b=dict(seeds=20, episodes=100000, alpha=0.1, eps_end=0.05, explore=0.5, eval_seed=7),
)
SMOKE = dict(
    measure=dict(reps=8, stationary_reps=8, stationary_day=5, pulse_days=5, yield_days=8,
                 seed=1000),
    a1=dict(dfs=[750], reps=8, harvest=1.5, seed=200000),
    a2=dict(x0=["stable"], harvests=[1.5], reps=8, seed=300000),
    a3=dict(harvests=[0.5], reps=8, days=8, seed=400000),
    a4=dict(dfs=[750], levels=[0.3], days=5, reps=8, seed=500000),
    b=dict(seeds=2, episodes=300, alpha=0.1, eps_end=0.05, explore=0.5, eval_seed=7),
)


def out_dir(smoke):
    d = os.path.join(RESULTS, "smoke") if smoke else RESULTS
    os.makedirs(d, exist_ok=True)
    return d


def dump(name, obj, smoke):
    with open(os.path.join(out_dir(smoke), name), "w") as f:
        json.dump(obj, f, indent=1)


def load(name, smoke):
    with open(os.path.join(out_dir(smoke), name)) as f:
        return json.load(f)


# ------------------------------------------------------------------------------ test bed A

def measure_one(args):
    df, cfg = args
    seed = cfg["seed"] + df
    xs = []
    for i in range(cfg["stationary_reps"]):
        v = Y.stationary(df, seed + i, days=cfg["stationary_day"] + 1, burn=cfg["stationary_day"])
        xs.append(v[0])
    alive = [x for x in xs if x > 0]
    x_star = statistics.mean(alive)
    m_star = Y.pulse_margin(df, x_star, seed + 10000, reps=cfg["reps"], days=cfg["pulse_days"])
    need = x_star - m_star
    y_hat = Y.sustained_yield(df, x_star, seed + 20000, reps=cfg["reps"], days=cfg["yield_days"])
    roots = Y.fixed_points(df)
    smax = Y.max_surplus(df, roots[0], roots[-1])
    return str(df), dict(x_star=x_star, stationary_alive=len(alive) / len(xs),
                         margin=m_star, need=need, yield_=y_hat,
                         model=dict(u=roots[0], x_star=roots[-1], max_surplus=smax[0],
                                    argmax=smax[1]))


def run_measure(cfg, pool, smoke):
    res = dict(pool.map(measure_one, [(df, cfg) for df in CONFIG["dfs"]]))
    dump("measure.json", res, smoke)
    return res


def a1_one(args):
    df, history, memory, cfg, m = args
    x0 = m["need"] + 0.5 * m["margin"]
    harvest = cfg["harvest"] * m["yield_"]
    seed0 = cfg["seed"] + df * 10 + {"h_long": 0, "h_short": 1, "h_below": 2}[history] * 100000 \
        + (500000 if memory else 0)
    taus = []
    for i in range(cfg["reps"]):
        _, sat = Y.prepare(df, x0, history, seed0 + i, memory)
        taus.append(Y.break_day(df, x0, harvest, m["need"], seed0 + 7 * cfg["reps"] + i,
                                memory=memory, saturated_days=sat))
    return f"{df}/{history}/{'memory' if memory else 'scalar'}", dict(x0=x0, harvest=harvest,
                                                                      taus=taus)


def run_a1(cfg, pool, smoke):
    m = load("measure.json", smoke)
    jobs = [(df, h, mem, cfg, m[str(df)]) for df in cfg["dfs"]
            for h in ("h_long", "h_short", "h_below") for mem in (False, True)]
    dump("a1.json", dict(pool.map(a1_one, jobs)), smoke)


def a2_one(args):
    df, x0name, mult, cfg, m = args
    x0 = m["x_star"] if x0name == "stable" else m["need"] + 0.5 * m["margin"]
    harvest = mult * m["yield_"]
    m0 = x0 - m["need"]
    seed0 = cfg["seed"] + df * 100 + int(mult * 100) + (50000 if x0name == "half" else 0)
    taus = [Y.break_day(df, x0, harvest, m["need"], seed0 + i) for i in range(cfg["reps"])]
    return f"{df}/{x0name}/{mult}", dict(x0=x0, m0=m0, harvest=harvest, yield_=m["yield_"],
                                         taus=taus, applicable=harvest < m0)


def run_a2(cfg, pool, smoke):
    m = load("measure.json", smoke)
    jobs = [(df, x0, h, cfg, m[str(df)]) for df in CONFIG["dfs"] for x0 in cfg["x0"]
            for h in cfg["harvests"]]
    dump("a2.json", dict(pool.map(a2_one, jobs)), smoke)


def a3_one(args):
    df, mult, cfg, m = args
    harvest = mult * m["yield_"]
    seed0 = cfg["seed"] + df * 100 + int(mult * 100)
    lo, hi = m["need"], m["x_star"]
    frac = lambda x0: Y.survival_fraction(df, x0, seed0, cfg["reps"], harvest_after=harvest,
                                          days=cfg["days"], need=m["need"])
    if frac(hi) < 0.5:
        return f"{df}/{mult}", dict(harvest=harvest, point_of_no_return=None)
    while hi - lo > 0.002 * m["x_star"]:
        mid = 0.5 * (lo + hi)
        if frac(mid) >= 0.5:
            hi = mid
        else:
            lo = mid
    return f"{df}/{mult}", dict(harvest=harvest, point_of_no_return=0.5 * (lo + hi),
                                need=m["need"])


def run_a3(cfg, pool, smoke):
    m = load("measure.json", smoke)
    jobs = [(df, h, cfg, m[str(df)]) for df in CONFIG["dfs"] for h in cfg["harvests"]]
    dump("a3.json", dict(pool.map(a3_one, jobs)), smoke)


def a4_level_after(df, x0, harvests, days, seed):
    """Level after `days` cycles from x0 with harvesters taking their H each day in order;
    returns (final level, takes per harvester)."""
    rng = random.Random(seed)
    c = Y.Culture(df, x0, rng)
    takes = [0.0] * len(harvests)
    for _ in range(days):
        if c.extinct:
            break
        # the harvesters take in order from the grown culture, then one transfer
        left = c.x
        for j, h in enumerate(harvests):
            t = min(h, left)
            takes[j] += t
            left -= t
        c.x = left
        c.day(0.0)
    return max(c.x, 0.0), takes


def a4_one(args):
    df, l1, l2, cfg, m = args
    x0 = m["x_star"]
    h1, h2 = l1 * m["yield_"], l2 * m["yield_"]
    seed0 = cfg["seed"] + df * 1000 + int(l1 * 100) * 10 + int(l2 * 100)
    rows = []
    for i in range(cfg["reps"]):
        s = seed0 * 1000 + i          # common random numbers across the four conditions
        x00, _ = a4_level_after(df, x0, [], cfg["days"], s)
        x1, _ = a4_level_after(df, x0, [h1], cfg["days"], s)
        x2, _ = a4_level_after(df, x0, [h2], cfg["days"], s)
        x12, takes = a4_level_after(df, x0, [h1, h2], cfg["days"], s)
        rows.append(dict(none=x00, one=x1, two=x2, both=x12, takes=takes))
    return f"{df}/{l1}/{l2}", dict(h1=h1, h2=h2, yield_=m["yield_"], x_star=x0, rows=rows)


def run_a4(cfg, pool, smoke):
    m = load("measure.json", smoke)
    lv = cfg["levels"]
    pairs = [(a, b) for i, a in enumerate(lv) for b in lv[i:]]
    jobs = [(df, a, b, cfg, m[str(df)]) for df in cfg["dfs"] for a, b in pairs]
    dump("a4.json", dict(pool.map(a4_one, jobs)), smoke)


# ------------------------------------------------------------------------------ test bed B

def summarize(rec, kind, variant):
    return dict(deliveries=rec["deliveries"], rewards=rec["rewards"],
                entries=rec["entries"], takes=rec["takes"], death_step=rec["death_step"],
                end_levels=list(rec["levels"][-1]), levels=[list(l) for l in rec["levels"]],
                accounting_mismatch=rec["accounting_mismatch"], actions=rec["actions"],
                coupling=[G.reward_coupling(kind, variant, acts) for acts in rec["actions"]])


def b_dp_one(args):
    kind, vname = args
    v = G.VARIANTS[vname]
    _, Q = G.solve(kind, v)
    pol = G.dp_policy(Q)
    solo = summarize(G.run_episode([pol], v, kind), kind, v)
    joint = summarize(G.run_episode([pol, pol], v, kind), kind, v)
    return f"{kind}/{vname}", dict(solo=solo, joint=joint)


def b_q_one(args):
    kind, vname, seed, cfg = args
    v = G.VARIANTS[vname]
    Qt = G.q_learn(kind, v, seed, episodes=cfg["episodes"], alpha=cfg["alpha"],
                   eps_end=cfg["eps_end"], explore=cfg["explore"])
    rng = random.Random(cfg["eval_seed"] * 1000 + seed)
    solo = summarize(G.run_episode([G.table_policy(Qt, rng)], v, kind), kind, v)
    return f"{kind}/{vname}/{seed}", solo


def b_joint_one(args):
    """B7: two end-coupled learners trained alone (seeds 2i, 2i+1, the same training as in
    b_q_one, so the same tables), deployed together in the same variant."""
    vname, i, cfg = args
    v = G.VARIANTS[vname]
    tabs = [G.q_learn("end", v, s, episodes=cfg["episodes"], alpha=cfg["alpha"],
                      eps_end=cfg["eps_end"], explore=cfg["explore"]) for s in (2 * i, 2 * i + 1)]
    rng = random.Random(cfg["eval_seed"] * 7919 + i)
    rec = G.run_episode([G.table_policy(tabs[0], rng), G.table_policy(tabs[1], rng)], v, "end")
    return f"end/{vname}/{i}", summarize(rec, "end", v)


def run_b(cfg, pool, smoke):
    dp = dict(pool.map(b_dp_one, [(k, vn) for k in G.REWARDS for vn in G.VARIANTS]))
    jobs = [(k, vn, s, cfg) for k in G.REWARDS for vn in G.VARIANTS for s in range(cfg["seeds"])]
    q = dict(pool.imap_unordered(b_q_one, jobs))
    joint = dict(pool.imap_unordered(
        b_joint_one, [(vn, i, cfg) for vn in G.VARIANTS for i in range(cfg["seeds"] // 2)]))
    dump("b.json", dict(dp=dp, q=q, q_joint=joint, H=G.H), smoke)


STEPS = dict(measure=run_measure, a1=run_a1, a2=run_a2, a3=run_a3, a4=run_a4, b=run_b)


def main(argv):
    smoke = "smoke" in argv
    names = [a for a in argv if a in STEPS]
    if "all" in argv or (smoke and not names):
        names = list(STEPS)
    cfgs = SMOKE if smoke else CONFIG
    log = []
    with Pool(12) as pool:
        for n in names:
            t0 = time.time()
            STEPS[n](cfgs[n], pool, smoke)
            log.append(f"{n}: {time.time() - t0:.1f} s")
            print(log[-1], flush=True)
    with open(os.path.join(out_dir(smoke), "run.log"), "a") as f:
        f.write("\n".join(log) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
