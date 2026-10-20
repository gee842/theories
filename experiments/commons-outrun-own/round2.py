"""Round 2 of CG3 (PREDICTIONS-ROUND2-2026-10-20.md): conditions, training with an optional
early-weighted start distribution, the run and the verdict rules.  Round 1's files are not changed.

Account under test (two quantities, both exact, from exact.Problem.alive_curve):
  cov   steps (of 100) a full patch stands under uniform requests 0..m (the behaviour early in
        training): whether restraint is learned in mid-course;
  full  steps a full patch stands under the full draw (m requests every step): whether a course
        from the start, where the learner's values are least trained and its greedy act is the
        full draw, reaches the region where restraint is learned.
Kept where cov >= 20 and (full >= 9 or the start region is trained); depleted where full <= 5.5
and the start region is untrained, or where cov <= 10.

    python3 round2.py exact    # writes results/round2-exact.json (before the freeze)
    python3 round2.py smoke    # every code path, a few episodes, nothing kept
    python3 round2.py all      # 20 seeds per condition, writes results/round2-runs.json
    python3 round2.py analyze  # writes results/round2-VERDICTS.json
"""

import json
import os
import random
import sys
import time
from multiprocessing import Pool

import exact
import own
from run import CONFIG

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
COV_LEARNED, COV_UNLEARNED = 20.0, 10.0
FULL_REACHES, FULL_ENDS = 9.0, 5.5
EARLY = (0.5, 10)   # with probability 0.5 a training episode starts at a step uniform in [0, 10)


def cond(m, s, w=6.0, early=False, predicted=None):
    return dict(m=m, s=s, w=w, v=0.0, q0=0.0, early=early, predicted=predicted)


CONDITIONS = {
    "R3s10": cond(3, 10, predicted="depleted"),
    "R2s4": cond(2, 4, predicted="depleted"),
    "R3s14": cond(3, 14, predicted="kept"),
    "R2s8": cond(2, 8, predicted="kept"),
    "R3s8early": cond(3, 8, early=True, predicted="kept"),
    "R3early": cond(3, 1, early=True, predicted="depleted"),
}


def train_eval(spec):
    """own.train_eval with the start distribution of `early` (round 1's otherwise)."""
    cond, seed, H = spec["cond"], spec["seed"], spec["H"]
    m = cond["m"]
    env = own.Commons(own.isolated_layout(1), f"{seed}/train", table=own.table(cond["s"]))
    ag = own.L.Q(m + 1, H, 9, f"{seed}/agent", spec["alpha"])
    checks = own.Checks()
    E = spec["episodes"]
    ramp = max(1, int(spec["eps_frac"] * E))
    starts = random.Random(f"{seed}/starts")
    for e in range(E):
        eps = max(spec["eps_end"], 1.0 - (1.0 - spec["eps_end"]) * e / ramp)
        if cond["early"] and starts.random() < EARLY[0]:
            t0 = starts.randrange(EARLY[1])
        else:
            t0 = starts.randrange(H)
        u = starts.random()
        apples = [1 if starts.random() < u else 0 for _ in range(9)]
        own.run_episode(env, ag, cond, H, eps, True, start=(t0, apples), checks=checks)
    env_eval = own.Commons(own.isolated_layout(1), f"{seed}/eval", table=own.table(cond["s"]))
    ag.rng = random.Random(f"{seed}/agent/eval")
    ev = dict(alive_probe=[], final=[], apples=[], ret=[])
    emptied = dict(episodes=0, violations=0)
    for e in range(spec["eval_episodes"]):
        xs, taken, acts, given = own.run_episode(env_eval, ag, cond, H, 0.0, False, checks=checks,
                                                 with_given=True)
        if xs[H] == 0:
            emptied["episodes"] += 1
            if sum(taken) != xs[0] + sum(given):
                emptied["violations"] += 1
        ev["alive_probe"].append(xs[H - spec["probe"]])
        ev["final"].append(xs[H])
        ev["apples"].append(sum(taken))
        ev["ret"].append(sum(taken) + cond["w"] * xs[H])
    greedy = [[max(range(m + 1), key=lambda a: (ag.q[ag.idx(x, tau) + a], -a)) for tau in range(H + 1)]
              for x in range(10)]
    return dict(spec=spec, checks=checks.c, emptied=emptied, eval=ev, greedy=greedy)


def work(job):
    key, spec = job
    t = time.time()
    r = train_eval(spec)
    r["seconds"] = time.time() - t
    return key, r


def exact_one(name, m, s, w):
    pr = exact.Problem(m, s, w, 0.0)
    pol, V = pr.optimal()
    full = [None] + [[m] * 512 for _ in range(exact.H)]
    return name, dict(cov=sum(pr.alive_curve([1.0 / (m + 1)] * (m + 1))),
                      full=sum(pr.alive_curve([0.0] * m + [1.0])), optimum=V[exact.FULL],
                      alive_opt=pr.alive_at(pol), alive_full=pr.alive_at(full))


def account(c, q):
    if q["cov"] <= COV_UNLEARNED:
        return "depleted"
    if q["cov"] >= COV_LEARNED and (q["full"] >= FULL_REACHES or c["early"]):
        return "kept"
    if q["full"] <= FULL_ENDS and not c["early"]:
        return "depleted"
    return "between"


def main(mode):
    if mode == "exact":
        with Pool(len(CONDITIONS)) as p:
            res = dict(p.starmap(exact_one, [(n, c["m"], c["s"], c["w"]) for n, c in CONDITIONS.items()]))
        for n, q in res.items():
            q["account"] = account(CONDITIONS[n], q)
            print(n, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in q.items()},
                  "frozen:", CONDITIONS[n]["predicted"])
        json.dump(res, open(os.path.join(RESULTS, "round2-exact.json"), "w"), indent=1)
        return
    if mode == "analyze":
        return analyze()
    cfg = dict(CONFIG)
    if mode == "smoke":
        cfg.update(episodes=30, seeds=1, eval_episodes=3)
    js = [((n, s), dict(cond=c, seed=f"cg3r2/{n}/{s}", H=cfg["H"], alpha=cfg["alpha"],
                        eps_end=cfg["eps_end"], eps_frac=cfg["eps_frac"], episodes=cfg["episodes"],
                        eval_episodes=cfg["eval_episodes"], probe=cfg["probe"]))
          for n, c in CONDITIONS.items() for s in range(cfg["seeds"])]
    t = time.time()
    with Pool(int(os.environ.get("CG3_JOBS", 8))) as pool:
        res = pool.map(work, js, chunksize=1)
    print(f"{len(res)} runs in {time.time() - t:.0f} s, "
          f"{sum(r['seconds'] for _, r in res) / 60:.1f} CPU-minutes", flush=True)
    if mode == "smoke":
        for (n, s), r in res:
            print(n, r["checks"]["je_viol"], r["emptied"], r["eval"]["final"])
        return
    json.dump(dict(config=cfg, runs=[dict(cond=n, seed=s, **r) for (n, s), r in res]),
              open(os.path.join(RESULTS, "round2-runs.json"), "w"))


KEEP_FROM, DEPLETE_TO = 0.80, 0.20


def analyze(rdir=RESULTS):
    runs = json.load(open(os.path.join(rdir, "round2-runs.json")))["runs"]
    by = {}
    for r in runs:
        by.setdefault(r["cond"], []).append(r)
    tot = {}
    for r in runs:
        for key, val in list(r["checks"].items()) + [("emptied_" + k, v) for k, v in r["emptied"].items()]:
            tot[key] = tot.get(key, 0) + val
    out = dict(conditions={}, contrasts={}, identity=dict(
        I1_cg1_checks_own_part=dict(steps=tot["steps"], violations=tot["balance_viol"] + tot["gate_given_below"]
                                    + tot["margin_viol"] + tot["je_viol"], own_excess_windows=tot["je_windows"]),
        I2_emptied_total=dict(episodes=tot["emptied_episodes"], violations=tot["emptied_violations"])))
    for v in out["identity"].values():
        v["verdict"] = "passed" if v["violations"] == 0 and (v.get("own_excess_windows", v.get("episodes"))) > 0 else "failed"
    for n, c in CONDITIONS.items():
        alive = [sum(1 for x in r["eval"]["alive_probe"] if x >= 1) / len(r["eval"]["alive_probe"]) for r in by[n]]
        m = sum(alive) / len(alive)
        ok = m >= KEEP_FROM if c["predicted"] == "kept" else m <= DEPLETE_TO
        out["conditions"][n] = dict(predicted=c["predicted"], verdict="passed" if ok else "failed",
                                    alive_probe_mean=m, alive_probe_by_seed=alive,
                                    seeds_at_least_0_8=sum(a >= 0.8 for a in alive),
                                    seeds_at_most_0_2=sum(a <= 0.2 for a in alive),
                                    alive_at_H_mean=sum(sum(1 for x in r["eval"]["final"] if x >= 1) / len(r["eval"]["final"]) for r in by[n]) / len(by[n]),
                                    return_mean=sum(sum(r["eval"]["ret"]) / len(r["eval"]["ret"]) for r in by[n]) / len(by[n]))
    V = {n: out["conditions"][n]["verdict"] == "passed" for n in CONDITIONS}
    out["contrasts"] = dict(
        Z1_coverage_is_not_enough=V["R3s10"] and V["R2s4"],
        Z2_full_draw_reaches_the_learned_region=V["R3s14"] and V["R2s8"],
        Z3_training_the_start_rescues_only_where_mid_course_is_learned=V["R3s8early"] and V["R3early"])
    json.dump(out, open(os.path.join(rdir, "round2-VERDICTS.json"), "w"), indent=1)
    for n, d in out["conditions"].items():
        print(f"{n:10} {d['predicted']:9} {d['alive_probe_mean']:6.2f} {d['seeds_at_least_0_8']:3d} "
              f"{d['seeds_at_most_0_2']:3d} {d['alive_at_H_mean']:6.2f} {d['return_mean']:7.1f}  {d['verdict']}")
    for k, v in list(out["identity"].items()) + list(out["contrasts"].items()):
        print(k, v)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "all")
