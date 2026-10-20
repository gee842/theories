"""Tabular Q-learners in the commons, the identity checks every run passes through, and the
late-reading regulation game.

Every learner is independent: its state is the level of the patch it is assigned to and the
steps left in the episode; its actions are wait (0) and harvest (1).  Its reward is the apple
it harvests at each step, and, where it is coupled, `lam` times the level of its patch after
the last step (a term coupled into the level beyond the episode's harvests).  Undiscounted
within the episode (gamma = 1), learning rate `alpha`, epsilon-greedy with epsilon falling
linearly from 1 to `eps_end` over the first `eps_frac` of the training episodes.
"""

import random

from commons import Commons, isolated_layout


# ---------------------------------------------------------------- identity checks (a), (b)

class Checks:
    """Checks every step of every episode at every patch against balance, the gate (need
    m = 1), the margin (Flow.Balances.retains_iff_within_margin) and joint excess
    (Flow.joint_excess_ends).  `union` lists groups of patches read as one condition."""

    def __init__(self, m=1):
        self.m = m
        self.c = dict(steps=0, balance_viol=0, gate_given_below=0, margin_checked=0,
                      margin_viol=0, je_windows=0, je_viol=0, episodes=0)

    def episode(self, xs, taken, given):
        """xs[t] for t = 0..H (level before step t; xs[H] after the last), taken[t], given[t]."""
        c, m = self.c, self.m
        H = len(taken)
        c["episodes"] += 1
        T_cum = 0
        G_cum = 0
        x0 = xs[0]
        for t in range(H):
            c["steps"] += 1
            if xs[t + 1] != xs[t] - taken[t] + given[t]:
                c["balance_viol"] += 1
            if given[t] > 0 and xs[t] < m:
                c["gate_given_below"] += 1
        for t in range(H + 1):
            # margin, with the part = all harvesters and the rest (regrowth) as recorded:
            # renewal admitted at t (level >= m) iff m + taken so far <= x0 + given so far
            c["margin_checked"] += 1
            if (xs[t] >= m) != (m + T_cum <= x0 + G_cum):
                c["margin_viol"] += 1
            if t < H:
                T_cum += taken[t]
                G_cum += given[t]
        # joint excess: run of excess steps from T of length n with xs[T] < n + m
        # => level < m and nothing given at every step from T + n to the end
        run = [0] * (H + 1)
        for t in range(H - 1, -1, -1):
            run[t] = run[t + 1] + 1 if taken[t] > given[t] else 0
        # suffix: first step from which level < m and nothing is given to the end
        dead_from = H + 1
        for t in range(H, -1, -1):
            ok = xs[t] < m and (t == H or given[t] == 0)
            if ok:
                dead_from = t
            else:
                break
        for T in range(H):
            nmin = max(1, xs[T] - m + 1)  # xs[T] < n + m  <=>  n >= xs[T] - m + 1
            if run[T] >= nmin:
                c["je_windows"] += run[T] - nmin + 1
                if dead_from > T + nmin:
                    c["je_viol"] += 1

    def merge(self, other):
        for k, v in other.items():
            self.c[k] = self.c.get(k, 0) + v


# ---------------------------------------------------------------- learners

class QAgent:
    def __init__(self, ident, patch, H, cap, coupled, lam, seed, alpha=0.1):
        self.id = ident
        self.patch = patch
        self.H = H
        self.cap = cap
        self.coupled = coupled
        self.lam = lam
        self.alpha = alpha
        self.q = [0.0] * ((cap + 1) * (H + 1) * 2)
        self.rng = random.Random(f"{seed}/agent/{ident}")

    def idx(self, x, tau):
        return (x * (self.H + 1) + tau) * 2

    def act(self, x, tau, eps):
        if eps > 0 and self.rng.random() < eps:
            return self.rng.randrange(2)
        i = self.idx(x, tau)
        q0, q1 = self.q[i], self.q[i + 1]
        if q0 == q1:
            return self.rng.randrange(2)
        return 1 if q1 > q0 else 0

    def update(self, x, tau, a, r, x2, terminal):
        i = self.idx(x, tau) + a
        if terminal:
            target = r + (self.lam * x2 if self.coupled else 0.0)
        else:
            j = self.idx(x2, tau - 1)
            target = r + max(self.q[j], self.q[j + 1])
        self.q[i] += self.alpha * (target - self.q[i])


def episode(env, agents, H, eps, learn, checks=None, log_actions=None):
    """One episode from full patches.  Returns per-agent harvest, final levels, per-patch
    level paths."""
    env.reset(full=True)
    npatch = len(env.patches)
    xs = [[env.level(p)] for p in range(npatch)]
    tk = [[] for _ in range(npatch)]
    gv = [[] for _ in range(npatch)]
    harvest = [0] * len(agents)
    for t in range(H):
        tau = H - t
        levels = [xs[p][-1] for p in range(npatch)]
        acts = []
        req = [[] for _ in range(npatch)]
        for ag in agents:
            a = ag.act(levels[ag.patch], tau, eps)
            acts.append(a)
            if a:
                req[ag.patch].append(ag.id)
        taken, given, got = env.step(req)
        for p in range(npatch):
            tk[p].append(taken[p])
            gv[p].append(given[p])
            xs[p].append(env.level(p))
        for k, ag in enumerate(agents):
            r = 1.0 if ag.id in got else 0.0
            harvest[k] += r
            if learn:
                ag.update(levels[ag.patch], tau, acts[k], r, xs[ag.patch][-1], tau == 1)
            if log_actions is not None:
                log_actions.append((k, tau, levels[ag.patch], acts[k]))
    if checks is not None:
        for p in range(npatch):
            checks.episode(xs[p], tk[p], gv[p])
    return harvest, [xs[p][-1] for p in range(npatch)], xs


def train_eval(spec):
    """spec: dict(seed, patches, agents=[(patch, coupled)], H, lam, episodes, eval_episodes,
    eps_end, eps_frac, alpha)."""
    seed = spec["seed"]
    H = spec["H"]
    env = Commons(spec["patches"], f"{seed}/train")
    cap = max(len(p) for p in env.patches)
    agents = [QAgent(i, p, H, cap, c, spec["lam"], seed, spec.get("alpha", 0.1))
              for i, (p, c) in enumerate(spec["agents"])]
    checks = Checks()
    E = spec["episodes"]
    ramp = max(1, int(spec["eps_frac"] * E))
    train_return = []
    for e in range(E):
        eps = max(spec["eps_end"], 1.0 - (1.0 - spec["eps_end"]) * e / ramp)
        h, _, _ = episode(env, agents, H, eps, True, checks)
        if e >= E - 500:
            train_return.append(sum(h))
    # greedy evaluation on fresh regrowth streams
    env_eval = Commons(spec["patches"], f"{seed}/eval")
    for ag in agents:
        ag.rng = random.Random(f"{seed}/agent/{ag.id}/eval")
    ev = dict(harvest=[], final=[], alive_at=[], last_step=[], paths=[])
    probe = spec.get("alive_probe", 20)
    for e in range(spec["eval_episodes"]):
        log = []
        h, fin, xs = episode(env_eval, agents, H, 0.0, False, checks, log)
        ev["harvest"].append(h)
        ev["final"].append(fin)
        ev["alive_at"].append([xs[p][H - probe] for p in range(len(xs))])
        # final-step decisions where an apple stands
        ev["last_step"].append([(k, a) for (k, tau, x, a) in log if tau == 1 and x >= 1])
        if e < spec.get("keep_paths", 0):
            ev["paths"].append(xs)
    out = dict(spec=spec, checks=checks.c, train_last500_mean_total_harvest=(
        sum(train_return) / len(train_return)), eval=ev)
    if spec.get("keep_q"):
        out["q"] = [ag.q for ag in agents]
    return out


# ---------------------------------------------------------------- scripted runs for (a'), (b)

def scripted_rate(spec):
    """One harvester at one isolated patch asks to harvest with probability q at each step.
    Returns collapse times (first step with level 0), censored at H."""
    seed, q, H, runs = spec["seed"], spec["q"], spec["H"], spec["runs"]
    out = []
    checks = Checks()
    for r in range(runs):
        env = Commons(isolated_layout(1), f"{seed}/rate/{q}/{r}")
        rng = random.Random(f"{seed}/rate-agent/{q}/{r}")
        xs, tk, gv = [env.level(0)], [], []
        tc = None
        for t in range(H):
            req = [[0]] if rng.random() < q else [[]]
            taken, given, _ = env.step(req)
            tk.append(taken[0]); gv.append(given[0]); xs.append(env.level(0))
            if tc is None and xs[-1] == 0:
                tc = t + 1
        checks.episode(xs, tk, gv)
        out.append(tc if tc is not None else H)
    return dict(spec=spec, collapse=out, censored=sum(1 for t in out if t >= H), checks=checks.c)


def scripted_adjoining(spec):
    """Two patches; a harvester clears patch 0 (harvests every step while it stands) and
    then stops; patch 1 is untouched.  Checks joint excess with each patch read alone and
    with the two read as one condition."""
    seed, gap, H, runs = spec["seed"], spec["gap"], spec["H"], spec["runs"]
    alone = Checks()
    union = Checks()
    regrew_after_zero = 0
    for r in range(runs):
        env = Commons(isolated_layout(2, gap), f"{seed}/adj/{gap}/{r}")
        xs = [[env.level(0)], [env.level(1)]]
        tk = [[], []]
        gv = [[], []]
        for t in range(H):
            req = [[0] if xs[0][-1] > 0 and t < 30 else [], []]
            taken, given, _ = env.step(req)
            for p in range(2):
                tk[p].append(taken[p]); gv[p].append(given[p]); xs[p].append(env.level(p))
        alone.episode(xs[0], tk[0], gv[0])
        union.episode([a + b for a, b in zip(xs[0], xs[1])],
                      [a + b for a, b in zip(tk[0], tk[1])],
                      [a + b for a, b in zip(gv[0], gv[1])])
        z = [t for t, x in enumerate(xs[0]) if x == 0]
        if z and any(x > 0 for x in xs[0][z[0]:]):
            regrew_after_zero += 1
    return dict(spec=spec, crosses=Commons(isolated_layout(2, gap), 0).crosses(),
                alone=alone.c, union=union.c, runs_regrew_after_zero=regrew_after_zero)


# ---------------------------------------------------------------- (e) late reading

def late_return_action(hist_rest, t, ell):
    """Regulation.lateReturn: at t > ell, move back what the rest did at t - (ell + 1)."""
    if t > ell:
        return -hist_rest[t - (ell + 1)]
    return 0


class LearnedOverseer:
    """Q-learning overseer reading ell late: its state is the level offset it read (level at
    t - ell, from the start x0, clipped) and its own last ell + 1 net moves; it may move the
    level by -D..D a step.  Trained against a random rest moving -d..d, rewarded 1 for each
    step the level is within the band."""

    def __init__(self, ell, D, seed, clip=12):
        self.ell, self.D, self.clip = ell, D, clip
        self.q = {}
        self.rng = random.Random(f"{seed}/overseer")

    def state(self, read, own):
        r = max(-self.clip, min(self.clip, read))
        return (r, tuple(own[-(self.ell + 1):]))

    def qs(self, s):
        v = self.q.get(s)
        if v is None:
            v = [0.0] * (2 * self.D + 1)
            self.q[s] = v
        return v

    def act(self, s, eps):
        if eps > 0 and self.rng.random() < eps:
            return self.rng.randrange(2 * self.D + 1) - self.D
        v = self.qs(s)
        best = max(v)
        choices = [i for i, x in enumerate(v) if x == best]
        return choices[self.rng.randrange(len(choices))] - self.D


def regulate(x0, H, ell, overseer_fn, rest_fn, band):
    """Run one course.  overseer_fn(read_offset_or_None, own_hist, rest_hist, t) -> net move;
    rest_fn(level_offset, t) -> net move in -d..d.  The overseer at t reads the level at
    t - ell (None before it exists).  Returns (exited, offsets)."""
    lo, hi = band
    x = x0
    offs = [0]
    own, rest = [], []
    exited = False
    for t in range(H):
        read = offs[t - ell] if t - ell >= 0 else None
        o = overseer_fn(read, own, rest, t)
        r = rest_fn(x - x0, t)
        own.append(o)
        rest.append(r)
        x = x + o + r
        offs.append(x - x0)
        if not (lo <= x - x0 <= hi):
            exited = True
    return exited, offs


def train_overseer(ell, d, D, band, H, episodes, seed, eps_end=0.02, alpha=0.1):
    ov = LearnedOverseer(ell, D, seed)
    rrng = random.Random(f"{seed}/rest-train")
    lo, hi = band
    for e in range(episodes):
        eps = max(eps_end, 1.0 - e / (0.8 * episodes))
        offs = [0]
        own = []
        x = 0
        prev = None
        for t in range(H):
            read = offs[t - ell] if t - ell >= 0 else 0
            s = ov.state(read, [0] * (ell + 1) + own)
            if prev is not None:
                ps, pa, pr = prev
                v = ov.qs(ps)
                v[pa + D] += alpha * (pr + max(ov.qs(s)) - v[pa + D])
            o = ov.act(s, eps)
            r = rrng.randrange(2 * d + 1) - d
            own.append(o)
            x = x + o + r
            offs.append(x)
            reward = 1.0 if lo <= x <= hi else 0.0
            prev = (s, o, reward)
        ps, pa, pr = prev
        v = ov.qs(ps)
        v[pa + D] += alpha * (pr - v[pa + D])
    return ov


def overseer_policy(ov):
    def fn(read, own, rest, t):
        s = ov.state(read if read is not None else 0, [0] * (ov.ell + 1) + own)
        v = ov.qs(s)
        best = max(v)
        return v.index(best) - ov.D  # deterministic at evaluation: first best
    return fn


def train_adversary(ell, d, band, H, overseer_fn, episodes, seed, eps_end=0.02, alpha=0.2,
                    clip=None):
    """Q-learning rest that sees the current offset and the step, moves -d..d, and is
    rewarded 1 when the level leaves the band (the episode then ends)."""
    lo, hi = band
    clip = clip or (abs(lo) + abs(hi) + 4)
    q = {}
    rng = random.Random(f"{seed}/adversary")

    def qs(s):
        v = q.get(s)
        if v is None:
            v = [0.0] * (2 * d + 1)
            q[s] = v
        return v

    def key(off, t):
        return (max(-clip, min(clip, off)), t)

    for e in range(episodes):
        eps = max(eps_end, 1.0 - e / (0.8 * episodes))
        x = 0
        offs = [0]
        own, rest = [], []
        for t in range(H):
            s = key(x, t)
            if rng.random() < eps:
                a = rng.randrange(2 * d + 1) - d
            else:
                v = qs(s)
                best = max(v)
                ch = [i for i, z in enumerate(v) if z == best]
                a = ch[rng.randrange(len(ch))] - d
            read = offs[t - ell] if t - ell >= 0 else None
            o = overseer_fn(read, own, rest, t)
            own.append(o)
            rest.append(a)
            x = x + o + a
            offs.append(x)
            out = not (lo <= x <= hi)
            v = qs(s)
            if out or t == H - 1:
                v[a + d] += alpha * ((1.0 if out else 0.0) - v[a + d])
                break
            v[a + d] += alpha * (max(qs(key(x, t + 1))) - v[a + d])

    def policy(off, t):
        v = qs(key(off, t))
        best = max(v)
        return v.index(best) - d
    return policy
