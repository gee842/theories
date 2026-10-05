"""Exact finite institutional model. Read PROTOCOL.md for claims and assumptions."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass, replace
from itertools import product
from pathlib import Path
import hashlib
import json
import platform

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

ROOT = Path(__file__).resolve().parent
STATES = list(product(range(2), range(2), range(2), range(3), (-1, 0, 1)))
INDEX = {s: i for i, s in enumerate(STATES)}
START = INDEX[(0, 0, 1, 2, 0)]
SAFE = np.array([s[3] > 0 for s in STATES])
N = len(STATES)
EVENTS = (
    'inquiry', 'admission', 'discrepant_admission', 'training',
    'revision', 'beneficial_revision', 'harmful_revision',
    'adequate', 'completed_cases', 'adequate_cases', 'turnover', 'entry',
)


@dataclass(frozen=True)
class Params:
    hazard: float = .05
    accuracy: float = .95
    delta_base: float = .05
    delta_failure: float = .20
    forget: float = .10
    entry: float = 0.
    w_volume: float = .25
    w_adaptive: float = 4.
    admission: bool = True
    execution: bool = True
    training: bool = True
    succession: str = 'endogenous'


def coin(p):
    for outcome, weight in ((False, 1-p), (True, p)):
        if weight > 0:
            yield outcome, weight


def care_probability(k, q, p):
    if k == 0 or p.succession == 'volume':
        return 0.
    if p.succession == 'protected':
        return 1.
    w = p.w_adaptive if q else p.w_volume
    return k*w/(1+k*w)


def decision(r, q, k, record, observation, p):
    """No hidden environment argument: the installed policy is nonanticipating."""
    plan = 'F' if q == 0 or k == 0 else ('T' if k == 1 else 'Q')
    admitted = observation is not None and p.admission
    new_record = observation if admitted else record
    new_r = new_record if q and k and p.execution and new_record != -1 else r
    return plan, new_record, new_r, admitted


def branches(s, p):
    e, r, q, k, b = s
    for switch, w0 in coin(p.hazard):
        en = e ^ switch
        for enters, w1 in coin(p.entry if k == 0 else 0):
            ka, qa = (1, 1) if enters else (k, q)
            plan0 = 'F' if qa == 0 or ka == 0 else ('T' if ka == 1 else 'Q')
            reports = [(None, 1.)] if plan0 != 'Q' else [
                (en, p.accuracy), (1-en, 1-p.accuracy)]
            for obs, w2 in reports:
                if w2 == 0:
                    continue
                plan, bn, rn, admitted = decision(r, qa, ka, b, obs, p)
                adequate = int(rn == en)
                taught = int(plan == 'T' and p.training)
                pre_k = min(2, ka+taught)
                base_events = {
                    'inquiry': int(plan == 'Q'),
                    'admission': int(admitted),
                    'discrepant_admission': int(admitted and obs != r),
                    'training': taught,
                    'revision': int(rn != r),
                    'beneficial_revision': int(rn != r and rn == en),
                    'harmful_revision': int(rn != r and rn != en),
                    'adequate': adequate,
                    'completed_cases': 2 if plan == 'F' else 1,
                    'adequate_cases': adequate*(2 if plan == 'F' else 1),
                    'entry': int(enters),
                }
                delta = p.delta_base+p.delta_failure*(1-adequate)
                for turn, w3 in coin(delta):
                    kn = max(0, pre_k-int(turn))
                    appointees = coin(care_probability(kn, qa, p)) if turn else [(bool(qa), 1.)]
                    for qn, w4 in appointees:
                        for lost, w5 in coin(p.forget if turn else 0):
                            dest = (int(en), int(rn), int(qn), kn, -1 if lost else bn)
                            events = dict(base_events, turnover=int(turn))
                            yield INDEX[dest], w0*w1*w2*w3*w4*w5, events


def kernel(p):
    P = np.zeros((N, N))
    R = np.zeros((N, len(EVENTS)))
    event_edges = {name: np.zeros((N, N), dtype=bool) for name in EVENTS}
    for i, s in enumerate(STATES):
        for j, weight, events in branches(s, p):
            P[i, j] += weight
            for c, name in enumerate(EVENTS):
                R[i, c] += weight*events[name]
                if weight > 0 and events[name] > 0:
                    event_edges[name][i, j] = True
    assert np.min(P) >= 0
    assert np.max(np.abs(P.sum(axis=1)-1)) < 2e-14
    return P, R, event_edges


def reachable(P):
    found = {START}
    stack = [START]
    while stack:
        i = stack.pop()
        for j in np.flatnonzero(P[i] > 0):
            if int(j) not in found:
                found.add(int(j))
                stack.append(int(j))
    return sorted(found)


def closed_core(P):
    keep = SAFE.copy()
    while True:
        new = keep & ~np.any((P > 0)[:, ~keep], axis=1)
        if np.array_equal(new, keep):
            return np.flatnonzero(keep).tolist()
        keep = new


def recurrent_classes(P):
    _, labels = connected_components(csr_matrix(P > 0), directed=True,
                                    connection='strong')
    reach = set(reachable(P))
    classes = []
    for label in np.unique(labels):
        idx = np.flatnonzero(labels == label)
        outside = np.flatnonzero(labels != label)
        if not np.any(P[np.ix_(idx, outside)] > 0) and any(int(i) in reach for i in idx):
            classes.append(idx)
    return classes


def stationary_in_class(P, idx):
    block = P[np.ix_(idx, idx)]
    A = np.vstack((block.T-np.eye(len(idx)), np.ones(len(idx))))
    rhs = np.r_[np.zeros(len(idx)), 1.]
    v = np.linalg.lstsq(A, rhs, rcond=None)[0]
    assert v.min() > -1e-10
    v = np.maximum(v, 0)
    v /= v.sum()
    assert np.max(np.abs(v @ block-v)) < 1e-10
    return v


def limiting_summary(P, R, edges):
    classes = recurrent_classes(P)
    rec = set(int(i) for cl in classes for i in cl)
    transient = [i for i in reachable(P) if i not in rec]
    weights = []
    for cl in classes:
        if START in cl:
            w = 1.
        else:
            Q = P[np.ix_(transient, transient)]
            rhs = P[np.ix_(transient, cl)].sum(axis=1)
            h = np.linalg.solve(np.eye(len(Q))-Q, rhs)
            w = float(h[transient.index(START)])
        weights.append(w)
    assert abs(sum(weights)-1) < 1e-7
    total = np.zeros(len(EVENTS))
    positive_k = 0.
    details = []
    for cl, w in zip(classes, weights):
        stat = stationary_in_class(P, cl)
        ev = stat @ R[cl]
        total += w*ev
        positive_k += w*float(stat @ SAFE[cl])
        details.append({
            'states': len(cl), 'probability': w,
            'all_have_capacity': bool(SAFE[cl].all()),
            'has_capacity_somewhere': bool(SAFE[cl].any()),
            'recurrent_events': [name for name in EVENTS if edges[name][np.ix_(cl, cl)].any()],
        })
    return {'positive_capacity_fraction': positive_k,
            'event_rates': dict(zip(EVENTS, map(float, total))), 'classes': details}


def evaluate(p, horizon=2000):
    P, R, edges = kernel(p)
    core = closed_core(P)
    d = np.zeros(N); d[START] = 1
    alive = d.copy()
    event_sum = np.zeros(len(EVENTS))
    curves = {'survival': [1.], 'capacity_occupancy': [1.], 'adequacy': []}
    checkpoints = {}
    for t in range(1, horizon+1):
        events = d @ R
        event_sum += events
        curves['adequacy'].append(float(events[EVENTS.index('adequate')]))
        d = d @ P
        alive = alive @ P
        alive[~SAFE] = 0
        curves['survival'].append(float(alive.sum()))
        curves['capacity_occupancy'].append(float(d[SAFE].sum()))
        if t in (200, 2000):
            checkpoints[str(t)] = {
                'never_lost_capacity': float(alive.sum()),
                'currently_has_capacity': float(d[SAFE].sum()),
                'average_events': dict(zip(EVENTS, map(float, event_sum/t))),
            }
    expected_loss = None
    residual = None
    safe_reach = [i for i in reachable(P) if SAFE[i]]
    if not core and safe_reach:
        Q = P[np.ix_(safe_reach, safe_reach)]
        tau = np.linalg.solve(np.eye(len(Q))-Q, np.ones(len(Q)))
        expected_loss = float(tau[safe_reach.index(START)])
        residual = float(np.max(np.abs((np.eye(len(Q))-Q) @ tau-1)))
        assert expected_loss >= sum(curves['survival'][:-1])-1e-7
    result = {
        'parameters': asdict(p), 'reachable_states': len(reachable(P)),
        'closed_safe_states': len(core), 'initial_in_closed_safe_core': START in core,
        'checkpoints': checkpoints, 'expected_first_loss_time': expected_loss,
        'linear_solve_residual': residual,
        'limiting': limiting_summary(P, R, edges),
        'max_row_sum_error': float(np.max(np.abs(P.sum(axis=1)-1))),
    }
    return result, curves, P, R


def sample_events(p, n=30000, horizon=200, seed=6065):
    """Independent event sampler; does not call branches, decision, or kernel."""
    rng = np.random.default_rng(seed)
    e = np.zeros(n, dtype=int); r = e.copy(); b = e.copy()
    q = np.ones(n, dtype=int); k = np.full(n, 2, dtype=int)
    alive = np.ones(n, dtype=bool)
    for _ in range(horizon):
        e ^= (rng.random(n) < p.hazard)
        incoming = (k == 0) & (rng.random(n) < p.entry)
        k[incoming] = 1; q[incoming] = 1
        querying = (q == 1) & (k == 2)
        teaching = (q == 1) & (k == 1)
        obs = np.where(rng.random(n) < p.accuracy, e, 1-e)
        if p.admission:
            b[querying] = obs[querying]
        if p.execution:
            acting = (q == 1) & (k > 0) & (b >= 0)
            r[acting] = b[acting]
        good = r == e
        if p.training:
            k += teaching.astype(int)
        turnover = rng.random(n) < p.delta_base+p.delta_failure*(~good)
        k = np.maximum(0, k-turnover.astype(int))
        if p.succession == 'protected':
            prob = (k > 0).astype(float)
        elif p.succession == 'volume':
            prob = np.zeros(n)
        else:
            weights = np.where(q == 1, p.w_adaptive, p.w_volume)
            prob = k*weights/(1+k*weights)
        new_q = (rng.random(n) < prob).astype(int)
        q[turnover] = new_q[turnover]
        b[turnover & (rng.random(n) < p.forget)] = -1
        alive &= k > 0
    return {
        'n': n, 'horizon': horizon,
        'survival': float(alive.mean()),
        'capacity_occupancy': float((k > 0).mean()),
    }


def checks(arms, results, matrices):
    records = []
    def record(name, condition, details=None):
        assert condition, (name, details)
        records.append({'check': name, 'passed': True, 'details': details})
    for name, (P, R) in matrices.items():
        record('stochastic rows '+name, np.max(np.abs(P.sum(axis=1)-1)) < 2e-14)
    for name in ('endogenous', 'rare_adverse', 'perfect_inquiry', 'no_training'):
        record('empty safe core '+name, results[name]['closed_safe_states'] == 0)
    record('protected initial safe core', results['protected']['initial_in_closed_safe_core'])
    record('protected has actual recurrent training and inquiry', all(
        {'training', 'inquiry', 'beneficial_revision'} <= set(c['recurrent_events'])
        for c in results['protected']['limiting']['classes']))
    p = replace(arms['protected'], training=False)
    P, _, _ = kernel(p)
    record('protected succession cannot replace absent training', len(closed_core(P)) == 0)
    # Hidden environments cannot affect a decision when the available report is fixed.
    for r, q, k, b in product(range(2), range(2), range(3), (-1, 0, 1)):
        for report in (None, 0, 1):
            plan, bn, rn, admitted = decision(r, q, k, b, report, arms['endogenous'])
            record_ok = rn in (r, b, report) and not (plan == 'Q' and k != 2)
            assert record_ok
    record('policy reads only available memory or admitted report', True)
    # Exact marginal comparisons on (e,r,q,k), not hidden memories.
    def distributions(p, steps, projection):
        P, _, _ = kernel(p)
        d = np.zeros(N); d[START] = 1
        out = []
        keys = sorted(set(projection(s) for s in STATES))
        proj = np.zeros((N, len(keys)))
        ki = {v: i for i, v in enumerate(keys)}
        for i, s in enumerate(STATES): proj[i, ki[projection(s)]] = 1
        for _ in range(steps):
            d = d @ P
            out.append(d @ proj)
        return np.array(out)
    da = distributions(arms['no_admission'], 200, lambda s: s[:4])
    dx = distributions(arms['no_execution'], 200, lambda s: s[:4])
    err = float(np.max(np.abs(da-dx)))
    record('admission and execution obstruction same observable path law', err < 2e-13, err)
    base0 = replace(arms['endogenous'], delta_failure=0)
    d0 = distributions(base0, 200, lambda s: (s[2], s[3]))
    for gate in ('admission', 'execution'):
        dg = distributions(replace(base0, **{gate: False}), 200, lambda s: (s[2], s[3]))
        err = float(np.max(np.abs(d0-dg)))
        record('removing outcome feedback separates '+gate, err < 2e-13, err)
    for name in ('endogenous', 'protected', 'no_training', 'reentry', 'rare_adverse'):
        mc = sample_events(arms[name])
        exact = results[name]['checkpoints']['200']
        for observed, field in [('survival', 'never_lost_capacity'), ('capacity_occupancy', 'currently_has_capacity')]:
            value = exact[field]
            tol = 6*np.sqrt(value*(1-value)/mc['n'])+2/mc['n']
            record('independent sampler '+name+' '+observed,
                   abs(mc[observed]-value) <= tol,
                   {'exact': value, 'sample': mc[observed], 'tolerance': tol, 'n': mc['n']})
    # The uniform two-period bound is checked for every safe state, not just START.
    for name in ('endogenous', 'perfect_inquiry', 'rare_adverse'):
        p = arms[name]
        P = matrices[name][0]
        Q = P[np.ix_(SAFE, SAFE)]
        loss = 1-Q@Q@np.ones(SAFE.sum())
        bound = p.delta_base**2/(1+max(p.w_adaptive, p.w_volume))
        record('uniform two-step loss bound '+name, float(loss.min()) >= bound-2e-14,
               {'minimum': float(loss.min()), 'bound': bound})
    return records


def main():
    primary = Params()
    arms = {
        'endogenous': primary,
        'protected': replace(primary, succession='protected'),
        'volume_only': replace(primary, succession='volume'),
        'no_admission': replace(primary, admission=False),
        'no_execution': replace(primary, execution=False),
        'no_training': replace(primary, training=False),
        'fixed_criterion': replace(primary, w_volume=1., w_adaptive=1.),
        'perfect_inquiry': replace(primary, accuracy=1.),
        'reentry': replace(primary, entry=.01),
        'rare_adverse': replace(primary, w_adaptive=10000.),
    }
    results, curves, matrices = {}, {}, {}
    for name, p in arms.items():
        result, curve, P, R = evaluate(p)
        results[name] = result; curves[name] = curve; matrices[name] = (P, R)
    verified = checks(arms, results, matrices)
    sensitivity = []
    for hazard, pressure, bias in product((.01, .05, .20), (0., .20, .50), (1., 4., 16.)):
        p = replace(primary, hazard=hazard, delta_failure=pressure, w_adaptive=bias)
        result, _, _, _ = evaluate(p, horizon=200)
        sensitivity.append({'hazard': hazard, 'pressure': pressure, 'adaptive_bias': bias,
                            'survival_200': result['checkpoints']['200']['never_lost_capacity'],
                            'mean_first_loss': result['expected_first_loss_time']})
    metadata = {
        'python': platform.python_version(), 'numpy': np.__version__,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol_sha256': hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
    }
    out = ROOT/'results'
    out.mkdir(exist_ok=True)
    (out/'analysis.json').write_text(json.dumps({'metadata': metadata, 'arms': results,
                                               'checks': verified, 'sensitivity': sensitivity}, indent=2)+'\n')
    np.savez_compressed(out/'curves.npz', **{
        name+'_'+kind: values for name, curve in curves.items() for kind, values in curve.items()})
    print(json.dumps({'checks_passed': len(verified), 'arms': {
        name: {'survival200': val['checkpoints']['200']['never_lost_capacity'],
               'expected_loss': val['expected_first_loss_time'],
               'limiting_capacity': val['limiting']['positive_capacity_fraction']}
        for name, val in results.items()}}, indent=2))


if __name__ == '__main__':
    main()
