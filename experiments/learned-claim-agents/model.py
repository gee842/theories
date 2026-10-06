"""Learned agents, fulfillment and other centers' claims (PROTOCOL.md).

numpy only. Trains shared per-recipient Q networks under four signal
regimes, evaluates them and a hand-written record rule on seven tests, and
writes results.json plus a first-run receipt. Metrics come from the actual
environment, never from records.
"""
from multiprocessing import Pool
from pathlib import Path
import datetime
import hashlib
import json
import traceback

import numpy as np

HERE = Path(__file__).resolve().parent
FREEZE = json.loads((HERE / 'protocol-freeze.json').read_text())
assert hashlib.sha256((HERE / 'PROTOCOL.md').read_bytes()).hexdigest() == FREEZE['protocol_sha256']

IDS = ('A', 'B', 'C')
REGIMES = ('self', 'proxy', 'access', 'access_identity_only')
SEEDS = range(10)
TRAIN_EPISODES = 20000
TEST_EPISODES = 2000
STEPS = 4
HIDDEN = 32
LR = 0.01
SUCCESS = 0.9
RESERVE_WEIGHT = 0.25
TESTS = ('train', 'new_claimant', 'large_claims', 'missing_records', 'forged_records',
         'scarce_symmetric', 'scarce_symmetric_swapped')


# ------------------------------------------------------------- environment

class Episode:
    def __init__(self, rng, ids, claims, pool, missing=0.0, forged=0.0):
        self.rng, self.ids, self.k = rng, list(ids), list(claims)
        self.pool, self.missing, self.forged = pool, missing, forged
        self.actual = [0, 0]          # actual deliveries (observer)
        self.c = [0, 0]               # certified positive records
        self.u = [0, 0]               # unknown records
        self.t = 0

    def observe(self, identity_only=False):
        recs = []
        for i in range(2):
            onehot = [1.0 if self.ids[i] == x else 0.0 for x in IDS]
            feats = [0.0, 0.0, 0.0] if identity_only else [self.k[i] / 2, self.c[i] / 2, self.u[i] / 2]
            recs.append(onehot + feats)
        glob = [self.pool / 4, self.t / 4]
        return np.array(recs), np.array(glob)

    def step(self, action):
        """action: 0/1 serve that slot, 2 withhold. Returns signal components."""
        out = dict(receipt=0, met_unit=0, excess=0, served=False)
        if action < 2 and self.pool > 0:
            self.pool -= 1; out['served'] = True
            ok = self.rng.random() < SUCCESS
            if ok:
                if self.actual[action] < self.k[action]:
                    out['met_unit'] = 1
                else:
                    out['excess'] = 1
                self.actual[action] += 1
            if self.rng.random() < self.missing:
                self.u[action] += 1
            else:
                recorded = ok or (self.rng.random() < self.forged)
                if recorded:
                    self.c[action] += 1; out['receipt'] = 1
        self.t += 1
        return out

    def done(self):
        return self.t >= STEPS


def signal(regime, out, terminal, pool):
    r = 0.0
    if regime == 'proxy':
        r += out['receipt']
    if regime in ('access', 'access_identity_only'):
        r += out['met_unit']
    if terminal:
        r += RESERVE_WEIGHT * pool
    return r


# ------------------------------------------------------------- agent

class Agent:
    def __init__(self, rng, identity_only):
        din = 6 + 2
        s = 0.3
        self.W1 = rng.normal(0, s, (din, HIDDEN)); self.b1 = np.zeros(HIDDEN)
        self.W2 = rng.normal(0, s, HIDDEN); self.b2 = 0.0
        self.V1 = rng.normal(0, s, (2, HIDDEN)); self.c1 = np.zeros(HIDDEN)
        self.V2 = rng.normal(0, s, HIDDEN); self.c2 = 0.0
        self.identity_only = identity_only

    def q(self, recs, glob):
        x = np.concatenate([recs, np.tile(glob, (2, 1))], axis=1)
        h = np.tanh(x @ self.W1 + self.b1)
        qs = h @ self.W2 + self.b2
        hw = np.tanh(glob @ self.V1 + self.c1)
        qw = hw @ self.V2 + self.c2
        return np.append(qs, qw), (x, h, hw, glob)

    def update(self, cache, action, error):
        x, h, hw, glob = cache
        if action < 2:
            hi = h[action]; xi = x[action]
            gW2 = error * hi; gb2 = error
            dh = error * self.W2 * (1 - hi ** 2)
            self.W2 += LR * gW2; self.b2 += LR * gb2
            self.W1 += LR * np.outer(xi, dh); self.b1 += LR * dh
        else:
            gV2 = error * hw
            dh = error * self.V2 * (1 - hw ** 2)
            self.V2 += LR * gV2; self.c2 += LR * error
            self.V1 += LR * np.outer(glob, dh); self.c1 += LR * dh


def train_claims(rng):
    return [int(rng.choice(3, p=[0.25, 0.5, 0.25])) for _ in range(2)]


def train(regime, seed):
    rng = np.random.default_rng(1000 + seed)
    ident = regime == 'access_identity_only'
    agent = Agent(rng, ident)
    for ep in range(TRAIN_EPISODES):
        eps = max(0.05, 1.0 - ep / (0.8 * TRAIN_EPISODES))
        env = Episode(rng, ('A', 'B'), train_claims(rng), 3)
        recs, glob = env.observe(ident)
        qv, cache = agent.q(recs, glob)
        while True:
            a = int(rng.integers(3)) if rng.random() < eps else int(np.argmax(qv))
            out = env.step(a)
            term = env.done()
            r = signal(regime, out, term, env.pool)
            if term:
                target = r; nq, ncache = None, None
            else:
                recs2, glob2 = env.observe(ident)
                nq, ncache = agent.q(recs2, glob2)
                target = r + float(np.max(nq))
            agent.update(cache, a, target - qv[a])
            if term:
                break
            qv, cache = agent.q(recs2, glob2)
    return agent


# ------------------------------------------------------------- policies

def record_rule(env):
    need = [env.k[i] - env.c[i] - env.u[i] for i in range(2)]
    best = max(need)
    if best <= 0 or env.pool <= 0:
        return 2
    cands = [i for i in range(2) if need[i] == best]
    return min(cands, key=lambda i: IDS.index(env.ids[i]))


def test_episode(test, rng):
    if test == 'train':
        return Episode(rng, ('A', 'B'), train_claims(rng), 3)
    if test == 'new_claimant':
        return Episode(rng, ('A', 'C'), train_claims(rng), 3)
    if test == 'large_claims':
        return Episode(rng, ('A', 'B'), [int(rng.choice([1, 2], p=[0.25, 0.75])) for _ in range(2)], 4)
    if test == 'missing_records':
        return Episode(rng, ('A', 'B'), train_claims(rng), 3, missing=0.5)
    if test == 'forged_records':
        return Episode(rng, ('A', 'B'), train_claims(rng), 3, forged=0.5)
    if test == 'scarce_symmetric':
        return Episode(rng, ('A', 'B'), [1, 1], 1)
    if test == 'scarce_symmetric_swapped':
        return Episode(rng, ('B', 'A'), [1, 1], 1)
    raise ValueError(test)


def evaluate(policy, test, seed, ident=False):
    rng = np.random.default_rng(50000 + 97 * seed + TESTS.index(test))
    met = denom = excess = retained = withheld_unmet = 0
    first_a = first_n = 0
    for _ in range(TEST_EPISODES):
        env = test_episode(test, rng)
        denom += min(sum(env.k), env.pool)
        first = None
        while not env.done():
            unmet = any(env.actual[i] < env.k[i] for i in range(2)) and env.pool > 0
            a = policy(env)
            if a == 2 and unmet:
                withheld_unmet += 1
            if a < 2 and env.pool > 0 and first is None:
                first = env.ids[a]
            out = env.step(a)
            met += out['met_unit']; excess += out['excess']
        retained += env.pool
        if first is not None:
            first_n += 1; first_a += int(first == 'A')
    n = TEST_EPISODES
    return dict(met=met / denom if denom else 1.0, excess=excess / n, retained=retained / n,
                withheld_unmet=withheld_unmet / n,
                first_choice_A=(first_a / first_n) if first_n else None, first_served_episodes=first_n)


def agent_policy(agent, ident):
    def policy(env):
        recs, glob = env.observe(ident)
        qv, _ = agent.q(recs, glob)
        return int(np.argmax(qv))
    return policy


def run_one(args):
    regime, seed = args
    agent = train(regime, seed)
    ident = regime == 'access_identity_only'
    pol = agent_policy(agent, ident)
    return regime, seed, {t: evaluate(pol, t, seed, ident) for t in TESTS}


def main():
    jobs = [(r, s) for r in REGIMES for s in SEEDS]
    with Pool(4) as pool:
        rows = pool.map(run_one, jobs)
    results = {r: {} for r in REGIMES}
    for regime, seed, res in rows:
        results[regime][str(seed)] = res
    results['record_rule'] = {str(s): {t: evaluate(record_rule, t, s) for t in TESTS} for s in SEEDS}
    out = dict(protocol_sha256=FREEZE['protocol_sha256'],
               producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               numpy=np.__version__, results=results)
    raw = json.dumps(out, indent=1, sort_keys=True) + '\n'
    (HERE / 'results.json').write_text(raw)
    return dict(status='run_complete_pending_checks', results_sha256=hashlib.sha256(raw.encode()).hexdigest(),
                jobs=len(jobs))


if __name__ == '__main__':
    receipt = HERE / 'first-run-receipt.json'
    assert not receipt.exists(), 'Preserve the first run.'
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        res = main(); res['started_utc'] = started
        res['finished_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        receipt.write_text(json.dumps(res, indent=2) + '\n')
    except BaseException:
        receipt.write_text(json.dumps(dict(status='failed', started_utc=started, error=traceback.format_exc()), indent=2) + '\n')
        raise
