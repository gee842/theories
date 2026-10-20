"""One tabular selector on CG2's gated patch, trained as CG2's learners are (no change to CG2).

The selector chooses how many of at most `m` requests to make at each step (CG2's joint learner
with m = 3); it is rewarded the step's apples, plus `v` x the level after every step, plus `w` x
the level after the last step.  State: the level and the steps left.  Training as CG2 and CG1's
round 2: undiscounted, alpha = 0.1, epsilon from 1 to 0.02 over the first 80% of the episodes,
exploring starts (random step, random apples), H = 100.  `q0` is the initial value of every
action (0 as in CG2; > 0 for optimistic initial values).  CG2's `learners.Q` and CG1's
environment and `Checks` are imported unchanged.  With one selector the part of CG1's joint-excess
check is the selector's own takes over a run of steps: `Flow.joint_excess_ends` read across time.
"""

import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, "..", "commons-outrun"))
sys.path.append(os.path.join(HERE, "..", "commons-gated-renewal"))
import learners as L  # noqa: E402  (CG2)
from calibrate import table  # noqa: E402  (CG2)
from commons import Commons, isolated_layout  # noqa: E402  (CG1)
from learning import Checks  # noqa: E402  (CG1)


def run_episode(env, ag, cond, H, eps, learn, start=None, checks=None, with_given=False):
    m, v, w = cond["m"], cond["v"], cond["w"]
    env.reset(full=True)
    t0 = 0
    if start is not None:
        t0, apples = start
        env.apple = list(apples)
    xs = [env.level(0)]
    taken, given, acts = [], [], []
    for t in range(t0, H):
        tau = H - t
        x = xs[-1]
        a = ag.act(x, tau, eps)
        tk, gv, _ = env.step([list(range(a))])
        x2 = env.level(0)
        xs.append(x2)
        taken.append(tk[0])
        given.append(gv[0])
        acts.append(a)
        if learn:
            ag.update(x, tau, a, tk[0] + v * x2, x2, w * x2)
    if checks is not None:
        checks.episode(xs, taken, given)
    if with_given:
        return xs, taken, acts, given
    return xs, taken, acts


def train_eval(spec):
    cond, seed, H = spec["cond"], spec["seed"], spec["H"]
    m = cond["m"]
    env = Commons(isolated_layout(1), f"{seed}/train", table=table(cond["s"]))
    ag = L.Q(m + 1, H, 9, f"{seed}/agent", spec["alpha"])
    if cond.get("q0", 0.0):
        ag.q = [float(cond["q0"])] * len(ag.q)
    checks = Checks()
    E = spec["episodes"]
    ramp = max(1, int(spec["eps_frac"] * E))
    starts = random.Random(f"{seed}/starts")
    for e in range(E):
        eps = max(spec["eps_end"], 1.0 - (1.0 - spec["eps_end"]) * e / ramp)
        t0 = starts.randrange(H)
        u = starts.random()
        apples = [1 if starts.random() < u else 0 for _ in range(9)]
        run_episode(env, ag, cond, H, eps, True, start=(t0, apples), checks=checks)
    env_eval = Commons(isolated_layout(1), f"{seed}/eval", table=table(cond["s"]))
    ag.rng = random.Random(f"{seed}/agent/eval")
    ev = dict(alive_probe=[], final=[], apples=[], ret=[], paths=[])
    emptied = dict(episodes=0, violations=0)
    for e in range(spec["eval_episodes"]):
        xs, taken, acts, given = run_episode(env_eval, ag, cond, H, 0.0, False, checks=checks,
                                             with_given=True)
        if xs[H] == 0:   # Regulation.accumulates_at on an emptied course
            emptied["episodes"] += 1
            if sum(taken) != xs[0] + sum(given):
                emptied["violations"] += 1
        ev["alive_probe"].append(xs[H - spec["probe"]])
        ev["final"].append(xs[H])
        ev["apples"].append(sum(taken))
        ev["ret"].append(sum(taken) + cond["v"] * sum(xs[1:]) + cond["w"] * xs[H])
        if e < spec.get("keep_paths", 0):
            ev["paths"].append(xs)
    # the greedy action at every (level, steps left), for the diagnosis of what was learned
    greedy = [[max(range(m + 1), key=lambda a: (ag.q[ag.idx(x, tau) + a], -a)) for tau in range(H + 1)]
              for x in range(10)]
    return dict(spec=spec, checks=checks.c, emptied=emptied, eval=ev, greedy=greedy)
