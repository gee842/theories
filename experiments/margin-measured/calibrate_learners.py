"""MQ1 round 2 calibration of the learners (H2) on the reference variant V0 only, blind and end
rewards (in V0 nothing dies and both rewards have the same best response, 9 deliveries). No other
variant is run. Output: results/round2/calibration_learners.json."""
import json, os, statistics, sys, random
from multiprocessing import Pool
import garden as G

SETTINGS = {
    "r1": dict(episodes=100000, alpha=0.1, eps_end=0.05, explore=0.5),
    "visits_0.6": dict(episodes=100000, eps_end=0.02, explore=0.5, visit_power=0.6, alpha_min=0.01),
    "visits_0.8": dict(episodes=100000, eps_end=0.02, explore=0.5, visit_power=0.8, alpha_min=0.0),
    "visits_0.6_200k": dict(episodes=200000, eps_end=0.02, explore=0.5, visit_power=0.6, alpha_min=0.01),
    "visits_0.6_explore0.9": dict(episodes=100000, eps_end=0.02, explore=0.9, visit_power=0.6, alpha_min=0.01),
    "visits_0.6_explore0.9_300k": dict(episodes=300000, eps_end=0.02, explore=0.9, visit_power=0.6, alpha_min=0.01),
}
DONE = ("r1", "visits_0.6", "visits_0.8", "visits_0.6_200k")

def one(args):
    name, kind, seed = args
    Qt = G.q_learn(kind, G.VARIANTS["V0"], seed, **SETTINGS[name])
    rng = random.Random(7000 + seed)
    rec = G.run_episode([G.table_policy(Qt, rng)], G.VARIANTS["V0"], kind)
    return name, kind, seed, rec["deliveries"][0]

if __name__ == "__main__":
    os.makedirs("results/round2", exist_ok=True)
    prev = json.load(open("results/round2/calibration_learners.json"))["results"] \
        if os.path.exists("results/round2/calibration_learners.json") else {}
    jobs = [(n, k, s) for n in SETTINGS if n not in DONE or not prev
            for k in ("blind", "end") for s in range(100, 106)]
    out = {k: v["deliveries"] for k, v in prev.items()}
    with Pool(12) as p:
        for n, k, s, d in p.imap_unordered(one, jobs):
            out.setdefault(f"{n}/{k}", []).append(d)
    summary = {k: dict(deliveries=sorted(v), mean=statistics.mean(v)) for k, v in sorted(out.items())}
    json.dump(dict(settings=SETTINGS, best_response=9, results=summary),
              open("results/round2/calibration_learners.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))
