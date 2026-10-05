"""Frozen-law continuation assay; floating-point, not interval certified."""
from collections import defaultdict, deque
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = HERE.parent / 'regulation/compare.py'
spec = importlib.util.spec_from_file_location('frozen_regulator', SOURCE)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
PROFILES = tuple(itertools.product((0, 1), repeat=4))
PREFIXES = tuple(itertools.product((0, 1), repeat=3))
CASES = [(1, 0, 'absent'), (1, 4, 'absent')]
CASES += [(g, 4, arm) for g in (4, 8) for arm in model.ARMS]
TOL = 1e-10


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def events(state, capture, theta, arm):
    for name, target, rate in model.events(state, capture, arm):
        if name == 'Y recycling':
            rate = rate * theta / 4
        if rate:
            yield name, target, rate


def active(s):
    return s is not None and s[0] + s[1] + s[2] + s[7] >= 1


def graph(capture, theta, arm, cap):
    states = [model.INITIAL]
    index = {model.INITIAL: 0}
    queue = deque(states)
    rows, cols, vals, crows, ccols, cvals = [], [], [], [], [], []
    while queue:
        state = queue.popleft()
        i = index[state]
        outgoing = defaultdict(float)
        for name, target, rate in events(state, capture, theta, arm):
            assert model.material(target) == 3
            assert active(state) or not active(target), 'A=0 must be invariant'
            if target[4] + target[6] > cap:
                target = None
            if target not in index:
                index[target] = len(states)
                states.append(target)
                queue.append(target)
            dest = index[target]
            outgoing[dest] += rate
            if name == 'C assembly':
                assert target is not None and dest != i
                crows.append(i); ccols.append(dest); cvals.append(rate)
        outgoing[i] -= sum(outgoing.values())
        for dest, rate in outgoing.items():
            if rate:
                rows.append(i); cols.append(dest); vals.append(rate)
    shape = (len(states), len(states))
    q = coo_matrix((vals, (rows, cols)), shape=shape).tocsr()
    assembly = coo_matrix((cvals, (crows, ccols)), shape=shape).tocsr()
    killed = q - assembly
    assert np.max(np.abs(np.asarray(q.sum(axis=1)).ravel())) == 0
    assert np.max(np.abs(assembly.diagonal())) == 0
    assert np.max(np.abs(q.diagonal() - killed.diagonal())) == 0
    hazard = np.array([s[0] if s is not None else 0 for s in states])
    assert np.max(np.abs(np.asarray(killed.sum(axis=1)).ravel() + hazard)) == 0
    return states, q, killed


def classification(value, overflow):
    if value >= .5 + TOL:
        return 'numerically reliable'
    if value + overflow < .5 - TOL:
        return 'numerically unreliable'
    return 'numerically unresolved'


def calculate(capture, theta, arm, cap):
    start = time.monotonic()
    states, q, killed = graph(capture, theta, arm, cap)
    initial = np.zeros(len(states)); initial[0] = 1
    h = np.array([active(s) for s in states], dtype=float)
    forward = expm_multiply(q.T, initial, start=0, stop=6, num=25,
                           traceA=q.diagonal().sum())
    backward = expm_multiply(q, h, start=0, stop=3, num=13,
                            traceA=q.diagonal().sum())
    no_assembly = expm_multiply(killed, h, start=0, stop=3, num=13,
                               traceA=killed.diagonal().sum())
    masks = {p: np.array([active(s) and s[8] >= p[0] and s[9] >= p[1]
                          and s[4] >= p[2] for s in states]) for p in PREFIXES}
    zero_fuel = np.array([s is not None and s[4] == 0 for s in states])
    overflow_i = states.index(None) if None in states else None
    cases = []
    for step in (1, 4, 12):
        p = forward[step]
        later = backward[step] - no_assembly[step]
        assert later.min() >= -TOL
        assert later.max() <= 1 + TOL
        assert np.max(no_assembly[step] - backward[step]) <= TOL
        overflow = float(forward[2*step, overflow_i]) if overflow_i is not None else 0.
        assays = []
        for j, b, f, n in PROFILES:
            selected = p * masks[(j, b, f)]
            outcome = later if n else backward[step]
            value = float(selected @ outcome)
            prefix_mass = float(selected.sum())
            assert -TOL <= value <= prefix_mass + TOL
            assays.append({'profile':[j,b,f,n], 'prefix_mass':prefix_mass,
                           'finite_success':value, 'success_plus_overflow':min(1.,value+overflow),
                           'classification_alpha_half':classification(value, overflow)})
        parts = []
        for name, mask in [('zero',masks[(1,1,0)] & zero_fuel),
                           ('positive',masks[(1,1,1)])]:
            selected = p * mask
            entry = float(selected.sum())
            joint = float(selected @ later)
            parts.append({'fuel_at_H':name, 'entry_mass':entry,
                          'joint_success':joint,
                          'conditional_success_in_stopped_chain':joint/entry if entry > 0 else None})
        primary = next(x for x in assays if x['profile'] == [1,1,0,1])['finite_success']
        partition_residual = sum(x['joint_success'] for x in parts)-primary
        assert abs(partition_residual) <= TOL
        cases.append({'H':step/4, 'tau':step/4, 'total_horizon':step/2,
                      'overflow_by_total_horizon':overflow,
                      'assays':assays, 'primary_fuel_strata':parts,
                      'fuel_partition_residual':partition_residual,
                      'minimum_subtracted_continuation_value':float(later.min()),
                      'maximum_subtracted_continuation_value':float(later.max())})
    return {'capture':capture,'theta':theta,'arm':arm,'cap':cap,'states':len(states),
            'elapsed_seconds':time.monotonic()-start,
            'forward_mass_error_max':float(np.max(np.abs(forward.sum(axis=1)-1))),
            'minimum_forward_mass':float(forward.min()), 'cases':cases}


def main():
    sources = [HERE/'PROTOCOL.md',Path(__file__),SOURCE,HERE.parent/'regulation/PROTOCOL.md']
    output = {'scope':'Fixed prospective follow-up to known model outcomes; numerical, not empirical or interval certified',
              'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in sources},
              'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
              'initial_state':model.INITIAL,'comparison_tolerance_not_error_bound':TOL,
              'networks':[]}
    destination = HERE/'results.json'
    for cap in (48,64):
        for capture,theta,arm in CASES:
            result=calculate(capture,theta,arm,cap)
            output['networks'].append(result)
            destination.write_text(json.dumps(output,indent=2)+'\n')
            print(json.dumps({k:result[k] for k in ['capture','theta','arm','cap','states','elapsed_seconds']}),flush=True)
    changes=[]
    for low,high in zip(output['networks'][:12],output['networks'][12:]):
        assert (low['capture'],low['theta'],low['arm']) == (high['capture'],high['theta'],high['arm'])
        for left,right in zip(low['cases'],high['cases']):
            changes += [abs(x['finite_success']-y['finite_success']) for x,y in zip(left['assays'],right['assays'])]
    output['max_cap_sensitivity']=max(changes)
    output['status']='all prespecified cases completed'
    destination.write_text(json.dumps(output,indent=2)+'\n')


if __name__ == '__main__':
    main()
