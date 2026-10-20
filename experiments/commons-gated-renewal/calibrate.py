"""Scripted calibration, run before the freeze (no learning): the exact maximum expected
regrowth of a 3x3 patch at each level, over all 512 configurations, and the mean harvest
and end state of threshold policies.  Writes results/calibration.json."""

import itertools
import json
import os
import statistics

from commons import Commons, isolated_layout, regrow_prob


def rmax_by_level():
    env = Commons(isolated_layout(1), 0)
    best = {}
    for bits in itertools.product([0, 1], repeat=9):
        env.apple = list(bits)
        x = sum(bits)
        r = sum(regrow_prob(sum(env.apple[j] for j in env.nbrs[i]))
                for i in range(9) if not env.apple[i])
        best[x] = max(best.get(x, 0.0), r)
    return best


def threshold(theta, H, end, eps=200, seed=1):
    """Harvest while the level exceeds theta; with `end`, also whenever steps left <= level."""
    tot, dead = [], []
    for e in range(eps):
        env = Commons(isolated_layout(1), f"calib{seed}/{e}")
        got = 0
        for t in range(H):
            x = env.level(0)
            h = x > theta or (end and H - t <= x)
            tk, _, _ = env.step([[0]] if h else [[]])
            got += tk[0]
        tot.append(got)
        dead.append(env.level(0) == 0)
    return dict(theta=theta, H=H, end_rule=end, mean_harvest=statistics.mean(tot),
                dead_rate=sum(dead) / eps)


if __name__ == "__main__":
    rm = rmax_by_level()
    rows = [threshold(th, 100, end) for th in (9, 8, 7, 6, 5, 4, 3, 0) for end in (True, False)]
    out = dict(rmax_by_level={str(k): round(v, 4) for k, v in sorted(rm.items())},
               rmax=round(max(rm.values()), 4), threshold_policies_H100=rows)
    os.makedirs("results", exist_ok=True)
    with open("results/calibration.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out["rmax_by_level"]), out["rmax"])
    for r in rows:
        print(r)
