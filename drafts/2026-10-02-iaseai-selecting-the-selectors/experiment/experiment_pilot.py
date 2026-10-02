#!/usr/bin/env python3
"""Rubric-editing experiment for "Selecting the Selectors" (predictions fixed in PREDICTIONS.md).

Pure Python 3, no dependencies.  Run:  python3 experiment.py   (writes experiment.log, fig-experiment.tex)

Lineages compete for shares of decisions under an evaluation rubric. Lineage k has a true quality
theta_k, a heritable capacity q_k and a distinctive feature that only it carries. Its score is
theta_k + w_k + w_g, where w_k is the rubric weight on its own feature and w_g a generic weight that
every lineage receives (it cancels from selection). Each round lineage k spends effort q_k * s_k on
editing the rubric: a fraction chi raises w_k (appropriable), the rest raises w_g (shared). Weights
decay at rate delta (correction). Capacity costs gamma * q_k per decision; it never raises scores
directly. Selection: s_k' is proportional to s_k * exp(kappa * (theta_k + w_k - gamma q_k)), plus
Wright-Fisher noise of variance s(1-s)/M. New lineages enter at rate p_entry with share s_entry and a
capacity inherited (with mutation) from a share-weighted parent; lineages below `extinct` die out.

Arms: FIXED (rubric frozen at zero), REPLAY (weights replayed from an independent closed-loop run,
assigned at random within size class, so rule changes happen but are not caused by own capacity),
CLOSED (chi = 0.8), PUBLIC (chi = 0), FAST (delta = 0.5), FRAGMENTED start, RARE and LARGE entrant.
The analytic size threshold is s* = gamma * delta / (a * b * chi), 0.1 at the baseline.
"""
import math
import random
import statistics

QGRID = [0.0, 0.25, 0.5, 0.75, 1.0]
BASE = dict(a=1.0, b=0.01, chi=0.8, delta=0.05, gamma=0.016, kappa=1.0, sigma_theta=0.02,
            M=20000, p_entry=0.05, s_entry=0.002, mut=0.5, T=600, extinct=1e-4)
SEEDS = list(range(20))


def threshold(p):
    return p["gamma"] * p["delta"] / (p["a"] * p["b"] * p["chi"]) if p["chi"] > 0 else float("inf")


# ---------------------------------------------------------------------------
def init_structure(kind):
    """Return list of (share, q, size_class)."""
    if kind == "conc":
        L = [(0.16, q, "large") for q in QGRID]
        L += [(0.01, q, "small") for q in QGRID for _ in range(4)]
    elif kind == "frag":
        L = [(0.02, q, "small") for q in QGRID for _ in range(10)]
    elif kind == "rare":
        L = [(0.99 / 4, 0.0, "large") for _ in range(4)] + [(0.01, 1.0, "focal")]
    elif kind == "large":
        L = [(0.25, 0.0, "large") for _ in range(3)] + [(0.25, 1.0, "focal")]
    else:
        raise ValueError(kind)
    return L


class Run:
    def __init__(self, kind, seed, p, mode="closed", replay=None):
        self.p = dict(p)
        self.mode = mode
        rng_init = random.Random(1000 + seed)          # same qualities across arms for a seed
        self.rng = random.Random(hash((seed, mode, kind, p["chi"], p["delta"])) & 0xFFFFFFFF)
        struct = init_structure(kind)
        self.s = [x[0] for x in struct]
        self.q = [x[1] for x in struct]
        self.cls = [x[2] for x in struct]
        self.theta = [rng_init.gauss(0.0, p["sigma_theta"]) for _ in struct]
        self.w = [0.0] * len(struct)
        self.wg = 0.0
        self.alive = [True] * len(struct)
        self.n0 = len(struct)
        self.replay = replay                            # list over initial lineages of weight paths
        if replay is not None:
            # permute within size class so that replayed boosts are uncorrelated with own capacity
            perm = list(range(self.n0))
            for c in set(self.cls):
                idx = [i for i in range(self.n0) if self.cls[i] == c]
                shuffled = idx[:]
                self.rng.shuffle(shuffled)
                for i, j in zip(idx, shuffled):
                    perm[i] = j
            self.perm = perm
        self.trace = []

    def step(self, t):
        p = self.p
        n = len(self.s)
        # rubric edits (closed loop) or replay or frozen
        if self.mode in ("closed",):
            for k in range(n):
                if self.alive[k]:
                    e = self.q[k] * self.s[k]
                    self.w[k] = (1 - p["delta"]) * self.w[k] + p["b"] * p["chi"] * e
                else:
                    self.w[k] *= (1 - p["delta"])
            self.wg = (1 - p["delta"]) * self.wg + p["b"] * (1 - p["chi"]) * sum(
                self.q[k] * self.s[k] for k in range(n) if self.alive[k])
        elif self.mode == "replay":
            for k in range(n):
                self.w[k] = self.replay[self.perm[k]][t] if k < self.n0 else 0.0
        # frozen: weights stay at zero
        # selection
        fit = [p["kappa"] * (self.theta[k] + p["a"] * self.w[k] - p["gamma"] * self.q[k]) if self.alive[k]
               else 0.0 for k in range(n)]
        m = max(fit[k] for k in range(n) if self.alive[k])
        raw = [self.s[k] * math.exp(fit[k] - m) if self.alive[k] else 0.0 for k in range(n)]
        Z = sum(raw)
        new = []
        for k in range(n):
            if not self.alive[k]:
                new.append(0.0)
                continue
            mean = raw[k] / Z
            sd = math.sqrt(max(mean * (1 - mean), 0.0) / p["M"])
            new.append(max(0.0, mean + sd * self.rng.gauss(0.0, 1.0)))
        Z = sum(new)
        self.s = [v / Z for v in new]
        for k in range(n):
            if self.alive[k] and self.s[k] < p["extinct"]:
                self.alive[k] = False
                self.s[k] = 0.0
        Z = sum(self.s)
        self.s = [v / Z for v in self.s]
        # entry with inherited, mutated capacity
        if self.rng.random() < p["p_entry"]:
            r, acc, parent = self.rng.random(), 0.0, 0
            for k in range(n):
                acc += self.s[k]
                if acc >= r:
                    parent = k
                    break
            gi = QGRID.index(self.q[parent])
            if self.rng.random() < p["mut"]:
                gi = min(len(QGRID) - 1, max(0, gi + self.rng.choice((-1, 1))))
            self.s = [v * (1 - p["s_entry"]) for v in self.s]
            self.s.append(p["s_entry"])
            self.q.append(QGRID[gi])
            self.cls.append("entrant")
            self.theta.append(self.rng.gauss(0.0, p["sigma_theta"]))
            self.w.append(0.0)
            self.alive.append(True)

    def stats(self):
        n = len(self.s)
        qbar = sum(self.s[k] * self.q[k] for k in range(n))
        hhi = sum(v * v for v in self.s)
        tbar = sum(self.s[k] * self.theta[k] for k in range(n))
        lead = max(range(n), key=lambda k: self.s[k])
        return qbar, hhi, tbar, lead

    def run(self, record=False):
        T = self.p["T"]
        paths = [[] for _ in range(self.n0)] if record else None
        for t in range(T):
            if t % 10 == 0:
                self.trace.append((t,) + self.stats()[:3])
            self.step(t)
            if record:
                for k in range(self.n0):
                    paths[k].append(self.w[k])
        self.trace.append((T,) + self.stats()[:3])
        return paths


# ---------------------------------------------------------------------------
def mean_ci(xs):
    m = statistics.mean(xs)
    if len(xs) < 2:
        return m, 0.0
    se = statistics.stdev(xs) / math.sqrt(len(xs))
    return m, 1.96 * se


LOG = []


def say(s=""):
    print(s, flush=True)
    LOG.append(s)


def main():
    say(f"Parameters: {BASE}")
    say(f"Analytic size threshold s* = gamma delta/(a b chi) = {threshold(BASE):.3f}; seeds = {len(SEEDS)}")
    arms = {}

    def collect(name, kind, p, mode, replay_from=None):
        res = []
        for seed in SEEDS:
            replay = None
            if mode == "replay":
                src = Run(kind, 10_000 + seed, p, mode="closed")   # independent closed-loop run
                replay = src.run(record=True)
            R = Run(kind, seed, p, mode=mode, replay=replay)
            R.run()
            res.append(R)
        arms[name] = res
        q0 = [r.trace[0][1] for r in res]
        qT = [r.trace[-1][1] for r in res]
        hT = [r.trace[-1][2] for r in res]
        m0 = statistics.mean(q0)
        mq, cq = mean_ci(qT)
        mh, ch = mean_ci(hT)
        up = sum(1 for a, b in zip(q0, qT) if b > a)
        say(f"{name:12s} mean capacity {m0:.3f} -> {mq:.3f} +/- {cq:.3f} (rose in {up}/{len(res)} runs); "
            f"HHI at T {mh:.3f} +/- {ch:.3f}")
        return res

    collect("FIXED", "conc", BASE, "frozen")
    collect("REPLAY", "conc", BASE, "replay")
    collect("CLOSED", "conc", BASE, "closed")
    collect("PUBLIC", "conc", dict(BASE, chi=0.0), "closed")
    collect("FAST", "conc", dict(BASE, delta=0.5), "closed")
    collect("FRAGMENTED", "frag", BASE, "closed")
    rare = collect("RARE", "rare", BASE, "closed")
    large = collect("LARGE", "large", BASE, "closed")

    def focal_share(r):
        return r.s[r.n0 - 1]
    fr = [focal_share(r) for r in rare]
    fl = [focal_share(r) for r in large]
    say(f"RARE  focal q=1 lineage: share 0.01 -> mean {statistics.mean(fr):.3f}; took over (>0.5) in "
        f"{sum(1 for v in fr if v > 0.5)}/{len(fr)} runs; extinct in {sum(1 for r in rare if not r.alive[r.n0 - 1])}")
    say(f"LARGE focal q=1 lineage: share 0.25 -> mean {statistics.mean(fl):.3f}; took over (>0.5) in "
        f"{sum(1 for v in fl if v > 0.5)}/{len(fl)} runs")

    # P4: true quality, paired by seed (same initial qualities across arms)
    dq = [c.trace[-1][3] - f.trace[-1][3] for c, f in zip(arms["CLOSED"], arms["FIXED"])]
    m, ci = mean_ci(dq)
    worse = sum(1 for v in dq if v < 0)
    say(f"True quality at T, CLOSED minus FIXED (paired by seed): {m:+.4f} +/- {ci:.4f}; lower in {worse}/{len(dq)}")
    best_won_fixed = sum(1 for r in arms["FIXED"] if r.stats()[3] == max(range(r.n0), key=lambda k: r.theta[k]))
    best_won_closed = sum(1 for r in arms["CLOSED"] if r.stats()[3] == max(range(r.n0), key=lambda k: r.theta[k]))
    say(f"Highest-quality initial lineage leads at T: FIXED {best_won_fixed}/{len(SEEDS)}, CLOSED {best_won_closed}/{len(SEEDS)}")
    lead_q = [r.q[r.stats()[3]] for r in arms["CLOSED"]]
    say(f"Capacity of the leading lineage at T in CLOSED: mean {statistics.mean(lead_q):.2f}")

    # prediction verdicts
    def rose(name):
        return statistics.mean(r.trace[-1][1] for r in arms[name]) > statistics.mean(r.trace[0][1] for r in arms[name])
    v1 = rose("CLOSED") and not any(rose(a) for a in ("FIXED", "REPLAY", "PUBLIC", "FAST"))
    v2 = not rose("FRAGMENTED")
    v3 = statistics.mean(fr) < 0.5 and statistics.mean(fl) > 0.5
    v4 = m < 0
    say(f"Verdicts: P1 {'holds' if v1 else 'FAILS'}; P2 {'holds' if v2 else 'FAILS'}; "
        f"P3 {'holds' if v3 else 'FAILS'}; P4 {'holds' if v4 else 'FAILS'}")
    open("experiment.log", "w").write("\n".join(LOG) + "\n")

    # figure: mean capacity over time by arm (mean over seeds)
    styles = {"CLOSED": ("cD", "very thick"), "REPLAY": ("cE", "thick, densely dashed"),
              "FIXED": ("black", "thick, dotted"), "PUBLIC": ("cS", "thick, dashdotted"),
              "FAST": ("cF", "thick, loosely dashed"), "FRAGMENTED": ("cI", "thick, densely dotted")}
    out = [r"\begin{tikzpicture}",
           r"\begin{axis}[width=0.92\columnwidth, height=3.6cm, xmin=0, xmax=600, ymin=-0.03, ymax=1.03,",
           r"  xtick={0,200,400,600}, ytick={0,0.5,1}, xlabel={round}, ylabel={mean capacity},",
           r"  tick label style={font=\scriptsize}, label style={font=\scriptsize}]"]
    for name, (col, sty) in styles.items():
        res = arms[name]
        npts = len(res[0].trace)
        pts = []
        for i in range(npts):
            t = res[0].trace[i][0]
            pts.append((t, statistics.mean(r.trace[i][1] for r in res)))
        out.append(r"\addplot[%s, %s] coordinates {%s};" % (col, sty, " ".join(f"({t},{v:.4f})" for t, v in pts)))
        out.append(r"\label{pl:x%s}" % name.lower())
    out += [r"\end{axis}", r"\end{tikzpicture}"]
    open("fig-experiment.tex", "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
