"""Exact quantities for one selector on CG2's gated 3x3 patch (no learning).

One selector chooses how many of at most `m` requests to make at each step; it is rewarded
the step's apples, plus `v` x the level after every step, plus `w` x the level after the last
step.  Over the patch's 512 configurations and the H = 100 steps, under the environment's exact
dynamics (CG2's calibrate.py, imported unchanged):

- `optimum`: the best value from a full patch, and the probability that the best policy leaves
  the patch standing at step H - 20 (the measure of CG2 and of this test);
- `full_draw`: the value of making all m requests at every step;
- `sweeps`: policy iteration started from the full draw (the policy a learner whose immediate
  apples are learned first holds early in training).  Each sweep evaluates the current policy
  exactly and takes the greedy policy against that evaluation, so the value of restraint at a
  step is read through the selector's own later acts as they then stand.  `n_keep` is the
  number of sweeps after which the policy leaves the patch standing at step H - 20 with
  probability at least 0.5; `n_opt` the number after which the policy's value is optimal.
  `reach[i]` is the earliest step at which the policy after sweep i withholds a request at a
  full patch (H if it never does): how far the end reading has reached back.

    python3 exact.py            # writes results/exact.json (a few minutes per condition)
"""

import json
import os
import sys
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, "..", "commons-outrun"))
import calibrate as C  # noqa: E402

H, POP, FULL = C.H, C.POP, 511
PROBE = H - 20


def harvest_outcomes(x, a):
    """(apples, [configurations after harvest], uniform) for a requests at configuration x."""
    m = min(a, POP[x])
    ss = C.subsets(x, m)
    return m, [x & ~t for t in ss]


def regrow_dist(P):
    """D[y] = list of (z, prob): the distribution of the configuration after regrowth from y."""
    D = []
    for y in range(512):
        empty = [i for i in range(9) if not y >> i & 1]
        p = P[y]
        out = {}
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
                out[z] = out.get(z, 0.0) + pr
        D.append(list(out.items()))
    return D


class Problem:
    def __init__(self, m, s, w, v):
        self.m, self.s, self.w, self.v = m, s, w, v
        self.P = C.regrowth_probs(s)
        self.D = regrow_dist(self.P)
        self.out = [[harvest_outcomes(x, a) for a in range(m + 1)] for x in range(512)]

    def backup(self, Vnext):
        """Q[x][a] at one step, given the value Vnext over configurations at the next step."""
        W = [sum(pr * (Vnext[z] + self.v * POP[z]) for z, pr in self.D[y]) for y in range(512)]
        Q = []
        for x in range(512):
            row = []
            for a in range(self.m + 1):
                n, ys = self.out[x][a]
                row.append(n + sum(W[y] for y in ys) / len(ys))
            Q.append(row)
        return Q

    def terminal(self):
        return [self.w * POP[z] for z in range(512)]

    def evaluate(self, pol):
        """pol[tau][x] -> action; returns Qs[tau] (tau = steps left, 1..H) under pol later."""
        V = self.terminal()
        Qs = [None] * (H + 1)
        for tau in range(1, H + 1):
            Q = self.backup(V)
            Qs[tau] = Q
            V = [Q[x][pol[tau][x]] for x in range(512)]
        return Qs, V

    def optimal(self):
        V = self.terminal()
        pol = [None] * (H + 1)
        for tau in range(1, H + 1):
            Q = self.backup(V)
            pol[tau] = [max(range(self.m + 1), key=lambda a: (Q[x][a], -a)) for x in range(512)]
            V = [Q[x][pol[tau][x]] for x in range(512)]
        return pol, V

    def alive_at(self, pol, step=PROBE):
        dist = {FULL: 1.0}
        for t in range(step):
            tau = H - t
            nd = {}
            for x, p in dist.items():
                _, ys = self.out[x][pol[tau][x]]
                q = p / len(ys)
                for y in ys:
                    for z, pr in self.D[y]:
                        nd[z] = nd.get(z, 0.0) + q * pr
            dist = nd
        return sum(p for x, p in dist.items() if POP[x] >= 1)

    def alive_curve(self, probs):
        """P(level >= 1) after each step from a full patch, where probs[a] is the chance of a
        requests at every step (a fixed mixture; the full draw is probs = [0, ..., 0, 1])."""
        dist, curve = {FULL: 1.0}, []
        for _t in range(H):
            nd = {}
            for x, p in dist.items():
                for a, pa in enumerate(probs):
                    if not pa:
                        continue
                    _, ys = self.out[x][a]
                    q = p * pa / len(ys)
                    for y in ys:
                        for z, pr in self.D[y]:
                            nd[z] = nd.get(z, 0.0) + q * pr
            dist = nd
            curve.append(sum(p for x, p in dist.items() if POP[x] >= 1))
        return curve

    def reach(self, pol):
        for t in range(H):
            if pol[H - t][FULL] < self.m:
                return t
        return H


def run(name, m, s, w, v, max_sweeps=H + 5):
    pr = Problem(m, s, w, v)
    opt_pol, Vopt = pr.optimal()
    full = [None] + [[m] * 512 for _ in range(H)]
    _, Vfull = pr.evaluate(full)
    out = dict(name=name, m=m, s=s, w=w, v=v, optimum=Vopt[FULL], full_draw=Vfull[FULL],
               gain=Vopt[FULL] - Vfull[FULL], alive_opt=pr.alive_at(opt_pol),
               alive_full=pr.alive_at(full), reach_opt=pr.reach(opt_pol))
    uni = pr.alive_curve([1.0 / (m + 1)] * (m + 1))
    fd = pr.alive_curve([0.0] * m + [1.0])
    out.update(alive_steps_uniform=sum(uni), alive_steps_full=sum(fd))
    pol, sweeps, n_keep, n_opt = full, 0, None, None
    reach, alive, value = [pr.reach(full)], [out["alive_full"]], [Vfull[FULL]]
    while sweeps < max_sweeps:
        Qs, V = pr.evaluate(pol)
        value[-1] = V[FULL]
        if V[FULL] >= Vopt[FULL] - 1e-9:
            n_opt = sweeps
            break
        pol = [None] + [[max(range(m + 1), key=lambda a: (Qs[tau][x][a], a == pol[tau][x], -a))
                         for x in range(512)] for tau in range(1, H + 1)]
        sweeps += 1
        al = pr.alive_at(pol)
        reach.append(pr.reach(pol))
        alive.append(al)
        value.append(None)
        if n_keep is None and al >= 0.5:
            n_keep = sweeps
    out.update(n_keep=n_keep, n_opt=n_opt, reach_by_sweep=reach, alive_by_sweep=alive,
               value_by_sweep=value)
    print(name, {k: (round(v_, 4) if isinstance(v_, float) else v_) for k, v_ in out.items()
                 if not k.endswith("by_sweep")}, flush=True)
    return out


def keeping_threshold(m, s, lo=0.0, hi=1.0, iters=14):
    """Least per-step weight v (no end reading) at which the best policy leaves the patch
    standing at step H - 20 with probability at least 0.9 (bisection)."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        pr = Problem(m, s, 0.0, mid)
        pol, _ = pr.optimal()
        if pr.alive_at(pol) >= 0.9:
            hi = mid
        else:
            lo = mid
    return lo, hi


def max_value(m, s, w, v):
    """The largest exact optimal value over every configuration and number of steps left (the
    bound an optimistic initial value has to exceed)."""
    pr = Problem(m, s, w, v)
    V, best = pr.terminal(), max(pr.terminal())
    for _tau in range(1, H + 1):
        Q = pr.backup(V)
        V = [max(r) for r in Q]
        best = max(best, max(V))
    return best


if __name__ == "__main__":
    from conditions import CONDITIONS, COV_DEPLETE, COV_KEEP
    jobs = [(n, c["m"], c["s"], c["w"], c["v"]) for n, c in CONDITIONS.items()]
    jobs.append(("CG2_control", 1, 1, 2.0, 0.0))   # CG2's post hoc control: one coupled member
    with Pool(min(len(jobs), int(os.environ.get("CG3_JOBS", 8)))) as p:
        res = p.starmap(run, jobs)
    out = dict(conditions={r["name"]: r for r in res})
    out["emptying_time_full_draw_scripted"] = {
        f"m{m}s{s}": C.scripted_alive(s, m) for m, s in sorted({(c["m"], c["s"]) for c in CONDITIONS.values()})}
    out["max_exact_value"] = {n: max_value(c["m"], c["s"], c["w"], c["v"])
                              for n, c in CONDITIONS.items() if c["q0"]}
    out["account_class"] = {}
    for n, c in CONDITIONS.items():
        cov = out["conditions"][n]["alive_steps_uniform"]
        cls = "kept" if cov >= COV_KEEP else ("depleted" if cov <= COV_DEPLETE else "between")
        if c["q0"]:
            cls = "kept (optimistic: early greedy acts withhold)"
        out["account_class"][n] = dict(cov=cov, cls=cls)
        print(n, round(cov, 2), cls, "frozen:", c["predicted"])
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, "results", "exact.json"), "w"), indent=1)
