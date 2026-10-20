"""Exact best responses in the commons, no learning (the only computation run before the freeze).

For one member against a rest of always-harvesters, a dynamic programme over the full
configuration of the 3x3 patch (512 configurations) and the steps left gives the member's best
value and the value of harvesting at every step, under the environment's exact dynamics
(commons.py of CG1: harvest first, a uniformly random standing cell per granted request,
requests beyond what stands go unmet at random; then each empty cell regrows independently
with the Perolat probability, scaled by `s` and capped at 1).  `gain` is how much the best
response beats harvesting at every step: where it is about zero, harvesting at every step is a
mutual best response (the depletion profile is an equilibrium); where it is large, it is not.

Also: the probability that c always-harvesters alone leave the patch standing at step 100, and
their mean emptying time (scripted, 400 runs each), and the exact maximum expected regrowth.

    python3 calibrate.py      # writes results/calibration.json (a few minutes, one core)
"""

import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, "..", "commons-gated-renewal"))
from commons import Commons, isolated_layout, PEROLAT  # noqa: E402

H = 100
_env = Commons(isolated_layout(1), 0)
NB = [sum(1 << j for j in _env.nbrs[i]) for i in range(9)]
POP = [bin(x).count("1") for x in range(512)]
_SUBS = {}


def table(s):
    return tuple(min(1.0, p * s) for p in PEROLAT)


def subsets(mask, m):
    key = (mask, m)
    if key not in _SUBS:
        bits = [i for i in range(9) if mask >> i & 1]
        _SUBS[key] = [sum(1 << i for i in c) for c in itertools.combinations(bits, m)]
    return _SUBS[key]


def regrowth_probs(s):
    tab = table(s)
    return [[0.0 if y >> i & 1 else tab[min(POP[y & NB[i]], 5)] for i in range(9)]
            for y in range(512)]


def expect_regrowth(V, P):
    """W[y] = E[V(y + cells regrown)] for every configuration y after harvest."""
    W = [0.0] * 512
    for y in range(512):
        empty = [i for i in range(9) if not y >> i & 1]
        p = P[y]
        acc = 0.0
        for bits in range(1 << len(empty)):
            pr, z = 1.0, y
            for j, i in enumerate(empty):
                if bits >> j & 1:
                    pr *= p[i]
                    z |= 1 << i
                else:
                    pr *= 1.0 - p[i]
                if pr == 0.0:
                    break
            if pr:
                acc += pr * V[z]
        W[y] = acc
    return W


def value(rest, s, lam=0.0, v=0.0, share=False, joint=0, policy=None):
    """Value at the full patch.  Member mode (joint = 0): one member against `rest`
    always-harvesters; its reward is its own apples (or, with share, the step's apples / (rest +
    1)), plus v * level after each step, plus lam * level after the last step.  Joint mode
    (joint = k): one selector choosing how many of k requests to make each step, rewarded the
    step's apples, plus k * lam * level after the last step.  policy: None (best), 'harvest'
    (every request every step)."""
    P = regrowth_probs(s)
    k = joint if joint else rest + 1
    end = (k * lam) if joint else lam
    V = [end * POP[z] for z in range(512)]
    acts = range(joint + 1) if joint else (0, 1)
    for _tau in range(H):
        W = expect_regrowth([V[z] + v * POP[z] for z in range(512)], P)
        NV = [0.0] * 512
        for x in range(512):
            n = POP[x]
            best = None
            for a in acts:
                if policy == "harvest" and a != acts[-1]:
                    continue
                r = a if joint else rest + a
                m = min(r, n)
                if joint or share:
                    rew = m if joint else m / k
                else:
                    rew = m / r if (a and r) else 0.0
                ss = subsets(x, m)
                q = rew + sum(W[x & ~t] for t in ss) / len(ss)
                if best is None or q > best:
                    best = q
            NV[x] = best
        V = NV
    return V[511]


def rmax(s):
    tab = table(s)
    best = 0.0
    for y in range(512):
        e = sum(tab[min(POP[y & NB[i]], 5)] for i in range(9) if not y >> i & 1)
        best = max(best, e)
    return best


def scripted_alive(s, c, runs=400):
    alive, times = 0, []
    for r in range(runs):
        env = Commons(isolated_layout(1), f"cal/{s}/{c}/{r}", table=table(s))
        end = None
        for t in range(H):
            env.step([list(range(c))])
            if env.level(0) == 0:
                end = t + 1
                break
        if end is None:
            alive += 1
        else:
            times.append(end)
    return dict(alive_at_H=alive / runs, mean_emptying_time=(sum(times) / len(times)) if times else None)


VSTAR_BRACKET = (0.2, 0.5)


def vstar(rest=2, s=1, iters=14):
    lo, hi = VSTAR_BRACKET
    for _ in range(iters):
        mid = (lo + hi) / 2
        g = value(rest, s, v=mid) - value(rest, s, v=mid, policy="harvest")
        if g < 1e-9:
            lo = mid
        else:
            hi = mid
    return lo, hi


if __name__ == "__main__":
    from conditions import CONDITIONS
    out = dict(rmax={s: rmax(s) for s in (1, 8, 16)},
               scripted={f"s{s}c{c}": scripted_alive(s, c) for s in (1, 8, 16) for c in (1, 2, 3)})
    lo, hi = vstar()
    out["vstar_k3_s1"] = [lo, hi]
    print("v*", lo, hi, flush=True)
    out["gain"] = {}
    for name, cond in CONDITIONS.items():
        kw = dict(rest=cond["k"] - 1, s=cond["s"], lam=cond["lam"], v=cond["v"],
                  share=cond["share"], joint=cond["k"] if cond["joint"] else 0)
        ah = value(policy="harvest", **kw)
        br = value(**kw)
        out["gain"][name] = dict(harvest_every_step=ah, best_response=br, gain=br - ah)
        print(name, round(ah, 4), round(br, 4), round(br - ah, 4), flush=True)
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    with open(os.path.join(HERE, "results", "calibration.json"), "w") as f:
        json.dump(out, f, indent=1)
