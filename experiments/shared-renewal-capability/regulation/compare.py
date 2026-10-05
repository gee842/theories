"""Prespecified physical regulator comparison. Numerical, not interval certified."""
from collections import defaultdict, deque
from pathlib import Path
import hashlib
import itertools
import json
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
# r,c,y,d,f,g,gf,yg, recycled, assembled, constructed
INITIAL = (0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
ARMS = {
    'absent': (0, 0, 0), 'burden': (1, 0, 0),
    'buffer': (1, 4, 0), 'inhibitor': (1, 0, 4),
    'responsive': (1, 4, 4),
}
PROFILES = list(itertools.product(range(2), repeat=3))


def events(state, capture, arm):
    if state is None:
        return []
    r, c, y, d, f, g, gf, yg, j, b, z = state
    build, alpha, mu = ARMS[arm]
    out = []

    def add(name, rate, change, flag=None):
        if not rate:
            return
        assert rate > 0
        target = list(state)
        for i, delta in change.items():
            target[i] += delta
        if flag is not None:
            target[flag] = 1
        assert min(target) >= 0, (name, state, target)
        out.append((name, tuple(target), rate))

    add('C assembly', r, {0:-1, 1:1}, 9)
    add('C wear', c, {1:-1, 3:1})
    add('free Y reproduction', r*y, {0:-1, 2:1})
    add('bound Y reproduction', r*yg, {0:-1, 2:1})
    add('free Y wear', y, {2:-1, 3:1})
    add('capture', capture*c, {4:1})
    add('free fuel leak', f, {4:-1})
    add('C recycling', f*d*c, {0:1, 3:-1, 4:-1}, 8)
    add('Y recycling', 4*f*d*y, {0:1, 3:-1, 4:-1}, 8)
    add('G construction', build*r*f, {0:-1, 4:-1, 5:1}, 10)
    add('free G wear', g, {5:-1, 3:1})
    add('fuel binding', alpha*g*f, {5:-1, 4:-1, 6:1})
    add('fuel unbinding', gf, {6:-1, 5:1, 4:1})
    add('bound fuel leak', gf, {6:-1, 5:1})
    add('GF regulator wear', gf, {6:-1, 3:1, 4:1})
    add('Y binding', mu*g*y, {5:-1, 2:-1, 7:1})
    add('Y unbinding', yg, {7:-1, 5:1, 2:1})
    add('YG regulator wear', yg, {7:-1, 2:1, 3:1})
    add('bound Y wear', yg, {7:-1, 5:1, 3:1})
    return out


def material(s):
    return sum(s[i] for i in [0, 1, 2, 3, 5, 6]) + 2*s[7]


def graph(capture, arm, cap):
    states, index, queue = [INITIAL], {INITIAL:0}, deque([INITIAL])
    rows, cols, vals = [], [], []
    while queue:
        state = queue.popleft()
        i = index[state]
        outgoing = defaultdict(int)
        for name, target, rate in events(state, capture, arm):
            assert material(target) == 3
            if target[4] + target[6] > cap:
                target = None
            if target not in index:
                index[target] = len(states)
                states.append(target)
                queue.append(target)
            outgoing[index[target]] += rate
        outgoing[i] -= sum(outgoing.values())
        for dest, rate in outgoing.items():
            if rate:
                rows.append(i); cols.append(dest); vals.append(rate)
    q = coo_matrix((vals, (rows, cols)), shape=(len(states),len(states)), dtype=float).tocsr()
    assert np.max(np.abs(np.asarray(q.sum(axis=1)).ravel())) == 0
    return states, q


def calculate(capture, arm, cap):
    start = time.monotonic()
    states, q = graph(capture, arm, cap)
    initial = np.zeros(len(states)); initial[0] = 1
    # Grid contains all three prespecified horizons, with no adaptive stopping.
    laws = expm_multiply(q.T, initial, start=0, stop=3, num=13, traceA=q.diagonal().sum())
    masks = []
    for jr, ba, fr in PROFILES:
        masks.append(np.array([s is not None and s[8] >= jr and s[9] >= ba
                               and s[4] >= fr and s[0]+s[1]+s[2]+s[7] >= 1
                               for s in states]))
    formed = np.array([s is not None and s[10] == 1 for s in states])
    intact = np.array([s is not None and s[5]+s[6]+s[7] >= 1 for s in states])
    overflow_i = states.index(None) if None in states else None
    cases = []
    for step in [1, 4, 12]:
        p = laws[step]
        overflow = float(p[overflow_i]) if overflow_i is not None else 0
        assays = []
        for profile, mask in zip(PROFILES, masks):
            value = float(p[mask].sum())
            assays.append({'profile':profile, 'finite_success':value,
                           'success_plus_overflow':min(1, value+overflow),
                           'numerical_alpha_half':('reliable' if value >= .5 else
                                  'unreliable' if value+overflow < .5 else 'unresolved')})
        cases.append({'horizon':step/4, 'overflow':overflow, 'mass_error':float(abs(p.sum()-1)),
                      'minimum_mass':float(p.min()), 'assays':assays,
                      'formation_finite_success':float(p[formed].sum()),
                      'intact_regulator_finite_success':float(p[intact].sum())})
    return {'capture':capture,'arm':arm,'cap':cap,'states':len(states),
            'elapsed_seconds':time.monotonic()-start, 'cases':cases}


def main():
    output = {'protocol_sha256':hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),
              'implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'arithmetic':'IEEE float64, scipy expm_multiply; not interval-certified',
              'initial_state':INITIAL,'arms':ARMS,'networks':[]}
    for cap in [32,48]:
        for capture in [4,8]:
            for arm in ARMS:
                result = calculate(capture,arm,cap)
                output['networks'].append(result)
                (HERE/'results.json').write_text(json.dumps(output,indent=2)+'\n')
                print(json.dumps({k:result[k] for k in ['capture','arm','cap','states','elapsed_seconds']}),flush=True)
    pairs = []
    for lo,hi in zip(output['networks'][:10],output['networks'][10:]):
        assert (lo['capture'],lo['arm']) == (hi['capture'],hi['arm'])
        pairs += [abs(a['finite_success']-b['finite_success'])
                  for lc,hc in zip(lo['cases'],hi['cases'])
                  for a,b in zip(lc['assays'],hc['assays'])]
    output['max_cap_sensitivity'] = max(pairs)
    (HERE/'results.json').write_text(json.dumps(output,indent=2)+'\n')


if __name__ == '__main__':
    main()
