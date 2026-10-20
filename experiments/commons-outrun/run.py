"""Run the frozen configuration of CG2 (PREDICTIONS-2026-10-20.md) and write results/.

    python3 run.py all        # every condition (about 10-20 minutes over 12 cores)
    python3 run.py smoke      # every code path with a few episodes; results not kept
"""

import json
import os
import sys
import time
from multiprocessing import Pool

import learners as L
from conditions import CONDITIONS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

CONFIG = dict(H=100, alpha=0.1, eps_end=0.02, eps_frac=0.8, episodes=30000, seeds=20,
              eval_episodes=200, probe=20, keep_paths=5)


def jobs(cfg):
    out = []
    for name, cond in CONDITIONS.items():
        for s in range(cfg["seeds"]):
            spec = dict(cond=cond, seed=f"cg2/{name}/{s}", H=cfg["H"], alpha=cfg["alpha"],
                        eps_end=cfg["eps_end"], eps_frac=cfg["eps_frac"],
                        episodes=cfg["episodes"], eval_episodes=cfg["eval_episodes"],
                        probe=cfg["probe"], keep_paths=cfg["keep_paths"])
            out.append(((name, s), spec))
    return out


def work(job):
    key, spec = job
    t = time.time()
    r = L.train_eval(spec)
    r["seconds"] = time.time() - t
    return key, r


def main(argv):
    mode = argv[1] if len(argv) > 1 else "all"
    cfg = dict(CONFIG)
    if mode == "smoke":
        cfg.update(episodes=30, seeds=1, eval_episodes=3)
    js = jobs(cfg)
    t = time.time()
    with Pool(int(os.environ.get("CG2_JOBS", os.cpu_count() or 4))) as pool:
        res = pool.map(work, js, chunksize=1)
    print(f"{len(res)} runs in {time.time() - t:.0f} s", flush=True)
    if mode == "smoke":
        for (name, s), r in res:
            print(name, r["checks"]["je_viol"], r["outrun"], r["eval"]["final"])
        return
    os.makedirs(RESULTS, exist_ok=True)
    out = dict(config=cfg, runs=[dict(cond=name, seed=s, **r) for (name, s), r in res])
    with open(os.path.join(RESULTS, "runs.json"), "w") as f:
        json.dump(out, f)


if __name__ == "__main__":
    main(sys.argv)
