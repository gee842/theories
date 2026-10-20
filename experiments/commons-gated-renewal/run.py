"""Run the frozen configurations of PREDICTIONS-2026-10-20.md and write results/.

    python3 run.py all            # every experiment (about 15-25 CPU minutes over 12 cores)
    python3 run.py c d1 d2 e ab   # chosen experiments
    python3 run.py smoke          # tiny run of every code path; results not kept

Configurations are in CONFIG below and are part of the freeze.
"""

import json
import os
import sys
import time
from multiprocessing import Pool

from commons import isolated_layout
import learning as L

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

CONFIG = dict(
    H=100,                 # steps in an episode
    lam=2.0,               # coupling: reward lam * level of the patch after the last step
    alpha=0.1,
    eps_end=0.02,
    eps_frac=0.8,
    eval_episodes=200,
    alive_probe=20,        # level read at step H - 20 for the early-collapse check
    c=dict(seeds=20, episodes=20000),
    d1=dict(seeds=10, episodes=10000, keep_paths=50),
    d2=dict(seeds=20, episodes=30000),
    rate=dict(qs=[0.5, 0.7, 1.0], H=5000, runs=1000, seed=0),
    adjoining=dict(gaps=[1, 2], H=300, runs=100, seed=0),
    e=dict(ells=[0, 1, 2, 3], d=1, D=2, x0=30, H=40, seeds=10,
           overseer_episodes=20000, adversary_episodes=5000),
)

D2_CONDITIONS = {
    # name: list of coupled flags, one per agent, all on patch 0
    "own3": [False, False, False],
    "c1own2": [True, False, False],
    "c2own1": [True, True, False],
    "c3": [True, True, True],
    "own2": [False, False],
    "own1": [False],
    "c1": [True],
}


def spec(seed, patches, agents, episodes, **extra):
    s = dict(seed=seed, patches=patches, agents=agents, H=CONFIG["H"], lam=CONFIG["lam"],
             episodes=episodes, eval_episodes=CONFIG["eval_episodes"],
             eps_end=CONFIG["eps_end"], eps_frac=CONFIG["eps_frac"], alpha=CONFIG["alpha"],
             alive_probe=CONFIG["alive_probe"])
    s.update(extra)
    return s


def jobs_c(cfg):
    out = []
    for cond, coupled in (("own", False), ("coupled", True)):
        for s in range(cfg["seeds"]):
            out.append((("c", cond, s), spec(f"c/{cond}/{s}", isolated_layout(1),
                                             [(0, coupled)], cfg["episodes"])))
    return out


def jobs_d1(cfg):
    out = []
    for cond, coupled in (("B_own", False), ("B_coupled", True)):
        for s in range(cfg["seeds"]):
            # the seed string is the same in both conditions: only agent 2's reward differs
            out.append((("d1", cond, s), spec(f"d1/{s}", isolated_layout(2),
                                              [(0, False), (0, False), (1, coupled)],
                                              cfg["episodes"], keep_q=True,
                                              keep_paths=cfg["keep_paths"])))
    return out


def jobs_d2(cfg):
    out = []
    for cond, flags in D2_CONDITIONS.items():
        for s in range(cfg["seeds"]):
            out.append((("d2", cond, s), spec(f"d2/{cond}/{s}", isolated_layout(1),
                                              [(0, f) for f in flags], cfg["episodes"])))
    return out


def run_job(job):
    key, sp = job
    t0 = time.time()
    r = L.train_eval(sp)
    r["seconds"] = round(time.time() - t0, 1)
    return key, r


def run_e(cfg, seed_offset=0):
    """Late reading: for each lateness, the late return and a learned overseer, each against
    a learned adversary, a random rest and the two constant rests, in the narrow band
    (b - a = 2(l+1)d - 1) and the wide band (b - a = 2(l+1)d)."""
    import random
    d, D, x0, H = cfg["d"], cfg["D"], cfg["x0"], cfg["H"]
    out = []
    for ell in cfg["ells"]:
        k = (ell + 1) * d
        bands = dict(narrow=(-k, k - 1), wide=(-k, k))
        for s in range(cfg["seeds"]):
            seed = f"e/{ell}/{s}"
            for bname, band in bands.items():
                ov = L.train_overseer(ell, d, D, band, H, cfg["overseer_episodes"], seed)
                overseers = dict(
                    late_return=lambda read, own, rest, t, ell=ell: L.late_return_action(rest, t, ell),
                    learned=L.overseer_policy(ov),
                )
                for oname, ofn in overseers.items():
                    adv = L.train_adversary(ell, d, band, H, ofn, cfg["adversary_episodes"],
                                            f"{seed}/{bname}/{oname}")
                    ex_adv, offs_adv = L.regulate(x0, H, ell, ofn, adv, band)
                    ex_up, offs_up = L.regulate(x0, H, ell, ofn, lambda o, t: d, band)
                    ex_dn, offs_dn = L.regulate(x0, H, ell, ofn, lambda o, t: -d, band)
                    rr = random.Random(f"{seed}/{bname}/{oname}/random")
                    rand_exits = 0
                    rand_span = []
                    for _ in range(200):
                        ex, offs = L.regulate(x0, H, ell, ofn,
                                              lambda o, t: rr.randrange(2 * d + 1) - d, band)
                        rand_exits += ex
                        rand_span.append(max(offs) - min(offs))
                    out.append(dict(ell=ell, seed=s, band=bname, band_lo=band[0],
                                    band_hi=band[1], bound=2 * k, overseer=oname,
                                    adversary_exits=ex_adv,
                                    adversary_span=max(offs_adv) - min(offs_adv),
                                    const_up_max=max(offs_up), const_down_min=min(offs_dn),
                                    const_spread=max(offs_up) - min(offs_dn),
                                    const_exits=int(ex_up) + int(ex_dn),
                                    random_exit_rate=rand_exits / 200,
                                    random_mean_span=sum(rand_span) / len(rand_span)))
    return out


def run_ab(cfg_rate, cfg_adj):
    rate = [L.scripted_rate(dict(seed=cfg_rate["seed"], q=q, H=cfg_rate["H"],
                                 runs=cfg_rate["runs"])) for q in cfg_rate["qs"]]
    adj = [L.scripted_adjoining(dict(seed=cfg_adj["seed"], gap=g, H=cfg_adj["H"],
                                     runs=cfg_adj["runs"])) for g in cfg_adj["gaps"]]
    return dict(rate=rate, adjoining=adj)


def save(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w") as f:
        json.dump(obj, f, separators=(",", ":"))


def main(argv):
    what = argv or ["all"]
    if what == ["smoke"]:
        cfg = json.loads(json.dumps(CONFIG))
        for k in ("c", "d1", "d2"):
            cfg[k]["seeds"] = 1
            cfg[k]["episodes"] = 3
        jobs = jobs_c(cfg["c"]) + jobs_d1(cfg["d1"]) + jobs_d2(cfg["d2"])
        for j in jobs:
            j[1]["eval_episodes"] = 2
            run_job(j)
        e = dict(cfg["e"], seeds=1, overseer_episodes=3, adversary_episodes=3, ells=[0, 1])
        run_e(e)
        run_ab(dict(cfg["rate"], runs=2, H=50), dict(cfg["adjoining"], runs=2))
        print("smoke ok")
        return
    if "all" in what:
        what = ["ab", "c", "d1", "d2", "e"]
    meta = dict(config=CONFIG, python=sys.version, started=time.strftime("%Y-%m-%dT%H:%M:%S"))
    if "ab" in what:
        t0 = time.time()
        save("ab.json", dict(meta=meta, **run_ab(CONFIG["rate"], CONFIG["adjoining"])))
        print("ab", round(time.time() - t0), "s", flush=True)
    jobs = []
    if "c" in what:
        jobs += jobs_c(CONFIG["c"])
    if "d1" in what:
        jobs += jobs_d1(CONFIG["d1"])
    if "d2" in what:
        jobs += jobs_d2(CONFIG["d2"])
    if jobs:
        t0 = time.time()
        with Pool(min(11, os.cpu_count() or 1)) as pool:
            res = pool.map(run_job, jobs, chunksize=1)
        by = {}
        for key, r in res:
            by.setdefault(key[0], []).append(dict(cond=key[1], seed=key[2], **r))
        for k, v in by.items():
            save(f"{k}.json", dict(meta=meta, runs=v))
        print("learning", round(time.time() - t0), "s", flush=True)
    if "e" in what:
        t0 = time.time()
        with Pool(min(4, os.cpu_count() or 1)) as pool:
            parts = pool.map(_e_one, CONFIG["e"]["ells"])
        save("e.json", dict(meta=meta, rows=[r for p in parts for r in p]))
        print("e", round(time.time() - t0), "s", flush=True)


def _e_one(ell):
    return run_e(dict(CONFIG["e"], ells=[ell]))


if __name__ == "__main__":
    main(sys.argv[1:])
