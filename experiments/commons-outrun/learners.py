"""Tabular Q-learners for CG2, the identity checks, and one training-and-evaluation run.

As CG1 (experiments/commons-gated-renewal/learning.py, round 2): every learner is independent,
its state is the patch's level and the steps left, it is undiscounted within an episode,
alpha = 0.1, epsilon falls linearly from 1 to 0.02 over the first 80% of training, and training
episodes start at a random step with random apples standing (exploring starts).  New here: the
regrowth scale, the reading of the level after each step (v), the shared reward, and the joint
learner (one learner choosing how many of the k requests to make).
"""

import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, "..", "commons-gated-renewal"))
from commons import Commons, isolated_layout  # noqa: E402
from learning import Checks  # noqa: E402

from calibrate import table  # noqa: E402


class Q:
    def __init__(self, n_actions, H, cap, seed, alpha=0.1):
        self.n, self.H, self.alpha = n_actions, H, alpha
        self.q = [0.0] * ((cap + 1) * (H + 1) * n_actions)
        self.rng = random.Random(seed)

    def idx(self, x, tau):
        return (x * (self.H + 1) + tau) * self.n

    def act(self, x, tau, eps):
        if eps > 0 and self.rng.random() < eps:
            return self.rng.randrange(self.n)
        i = self.idx(x, tau)
        vals = self.q[i:i + self.n]
        best = max(vals)
        ties = [a for a, q in enumerate(vals) if q == best]
        return ties[0] if len(ties) == 1 else self.rng.choice(ties)

    def update(self, x, tau, a, target_now, x2, terminal_bonus):
        """target_now: reward of the step; terminal_bonus: added at the last step (tau == 1)."""
        i = self.idx(x, tau) + a
        if tau == 1:
            target = target_now + terminal_bonus
        else:
            j = self.idx(x2, tau - 1)
            target = target_now + max(self.q[j:j + self.n])
        self.q[i] += self.alpha * (target - self.q[i])


class OutrunChecks:
    """Flow.outrun_below with need m = 1, for every member: over every window (T, n) in which the
    takes of the members other than i exceed what is given at each of the n steps from T and
    the level at T is at most n, the level is 0 at every step from T + n to the episode's end.
    And Regulation.accumulates_at read for an emptied course: where the level after the last
    step is 0, everything taken equals the start plus everything given."""

    def __init__(self):
        self.c = dict(windows=0, violations=0, emptied_episodes=0, emptied_violations=0)

    def episode(self, xs, got_by, given, k):
        H = len(given)
        zero_from = H + 1
        for t in range(H, -1, -1):
            if xs[t] == 0:
                zero_from = t
            else:
                break
        for i in range(k):
            rest = [sum(1 for a in got_by[t] if a != i) for t in range(H)]
            run = [0] * (H + 1)
            for t in range(H - 1, -1, -1):
                run[t] = run[t + 1] + 1 if rest[t] > given[t] else 0
            for T in range(H):
                nmin = max(1, xs[T])        # level at T < n + 1
                if run[T] >= nmin:
                    self.c["windows"] += run[T] - nmin + 1
                    if zero_from > T + nmin:
                        self.c["violations"] += 1
        if xs[H] == 0:
            self.c["emptied_episodes"] += 1
            if sum(len(g) for g in got_by) != xs[0] + sum(given):
                self.c["emptied_violations"] += 1


def run_episode(env, agents, cond, H, eps, learn, start=None, checks=None, outrun=None):
    k, v, lam, share, joint = cond["k"], cond["v"], cond["lam"], cond["share"], cond["joint"]
    env.reset(full=True)
    t0 = 0
    if start is not None:
        t0, apples = start
        env.apple = list(apples)
    xs = [env.level(0)]
    taken, given, got_by = [], [], []
    harvest = [0] * k
    for t in range(t0, H):
        tau = H - t
        x = xs[-1]
        if joint:
            a = agents[0].act(x, tau, eps)
            acts = [a]
            req = list(range(a))
        else:
            acts = [ag.act(x, tau, eps) for ag in agents]
            req = [i for i in range(k) if acts[i]]
        tk, gv, got = env.step([req])
        x2 = env.level(0)
        xs.append(x2)
        taken.append(tk[0])
        given.append(gv[0])
        got_by.append(sorted(got))
        for i in got:
            harvest[i] += 1
        if learn:
            if joint:
                agents[0].update(x, tau, acts[0], tk[0], x2, k * lam * x2)
            else:
                for i, ag in enumerate(agents):
                    own = (tk[0] / k) if share else (1.0 if i in got else 0.0)
                    ag.update(x, tau, acts[i], own + v * x2, x2, lam * x2)
    if checks is not None:
        checks.episode(xs, taken, given)
    if outrun is not None and t0 == 0:
        outrun.episode(xs, got_by, given, k)
    return harvest, xs


def train_eval(spec):
    cond, seed, H = spec["cond"], spec["seed"], spec["H"]
    k = cond["k"]
    env = Commons(isolated_layout(1), f"{seed}/train", table=table(cond["s"]))
    if cond["joint"]:
        agents = [Q(k + 1, H, 9, f"{seed}/agent/joint", spec["alpha"])]
    else:
        agents = [Q(2, H, 9, f"{seed}/agent/{i}", spec["alpha"]) for i in range(k)]
    checks, outrun = Checks(), OutrunChecks()
    E = spec["episodes"]
    ramp = max(1, int(spec["eps_frac"] * E))
    starts = random.Random(f"{seed}/starts")
    for e in range(E):
        eps = max(spec["eps_end"], 1.0 - (1.0 - spec["eps_end"]) * e / ramp)
        t0 = starts.randrange(H)
        u = starts.random()
        apples = [1 if starts.random() < u else 0 for _ in range(9)]
        run_episode(env, agents, cond, H, eps, True, start=(t0, apples), checks=checks)
    env_eval = Commons(isolated_layout(1), f"{seed}/eval", table=table(cond["s"]))
    for j, ag in enumerate(agents):
        ag.rng = random.Random(f"{seed}/agent/{j}/eval")
    ev = dict(harvest=[], alive_probe=[], final=[], paths=[])
    for e in range(spec["eval_episodes"]):
        h, xs = run_episode(env_eval, agents, cond, H, 0.0, False, checks=checks, outrun=outrun)
        ev["harvest"].append(h)
        ev["alive_probe"].append(xs[H - spec["probe"]])
        ev["final"].append(xs[H])
        if e < spec.get("keep_paths", 0):
            ev["paths"].append(xs)
    return dict(spec=spec, checks=checks.c, outrun=outrun.c, eval=ev)
