"""Exact diagnostic interventions in the unchanged parent model; see protocol."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import replace
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'closure-study' / 'analyze.py'
spec = importlib.util.spec_from_file_location('closure_causal', SOURCE)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
H = 200


def summary(p, initial=None, horizon=H):
    P, R, _ = m.kernel(p)
    alive = np.zeros(m.N) if initial is None else initial.copy()
    if initial is None:
        alive[m.START] = 1.
    dist = alive.copy()
    total = np.zeros(len(m.EVENTS))
    for _ in range(horizon):
        total += dist @ R
        dist = dist @ P
        alive = alive @ P
        alive[~m.SAFE] = 0
    return {'survival': float(alive.sum()),
            'mean_events': dict(zip(m.EVENTS, map(float, total/horizon)))}


def projected_signature(i, p):
    """All projected next states plus task/skill events, not just expectations."""
    keep = ('inquiry', 'training', 'revision', 'beneficial_revision',
            'harmful_revision', 'adequate', 'completed_cases',
            'adequate_cases', 'turnover', 'entry')
    sig = defaultdict(float)
    for j, w, ev in m.branches(m.STATES[i], p):
        key = m.STATES[j][:4] + tuple(ev[k] for k in keep)
        sig[key] += w
    return sig


def equivalence_check(pa, pe):
    pairs = 0
    err = 0.
    ra = m.reachable(m.kernel(pa)[0])
    re = m.reachable(m.kernel(pe)[0])
    for i in ra:
        for j in re:
            if m.STATES[i][:4] != m.STATES[j][:4]:
                continue
            a, e = projected_signature(i, pa), projected_signature(j, pe)
            err = max(err, max(abs(a.get(k, 0)-e.get(k, 0)) for k in a.keys() | e.keys()))
            pairs += 1
    assert pairs > 0 and err < 2e-15
    return {'related_reachable_pairs': pairs, 'maximum_joint_row_difference': err}


def intervention_table(base):
    hypotheses = {
        'baseline': base,
        'admission_blocked': replace(base, admission=False),
        'execution_blocked': replace(base, execution=False),
        'both_blocked': replace(base, admission=False, execution=False),
        'training_blocked': replace(base, training=False),
    }
    interventions = {
        'none': {}, 'admission': {'admission': True},
        'execution': {'execution': True}, 'training': {'training': True},
        'admission_execution': {'admission': True, 'execution': True},
        'all': {'admission': True, 'execution': True, 'training': True},
    }
    return {h: {a: summary(replace(p, **settings))
                for a, settings in interventions.items()} for h, p in hypotheses.items()}


def main():
    base = m.Params()
    table = intervention_table(base)
    nofeedback = intervention_table(replace(base, delta_failure=0))
    known = table['baseline']['none']['survival']
    broken = table['admission_blocked']['none']['survival']
    assert abs(known-.09436917425904776) < 1e-13
    assert abs(broken-.006721822797561353) < 1e-13
    interactions = {}
    for accuracy in (0., .5, .95, 1.):
        outcomes = {f'{a}{e}': summary(replace(base, accuracy=accuracy,
                       admission=bool(a), execution=bool(e))) for a in (0, 1) for e in (0, 1)}
        v = {k: d['survival'] for k, d in outcomes.items()}
        interactions[str(accuracy)] = {
            'arms': outcomes,
            'survival_interaction': v['11']-v['10']-v['01']+v['00'],
        }
        assert max(v['00'], v['01'], v['10'])-min(v['00'], v['01'], v['10']) < 1e-13
    delayed = {}
    for name, p in [('admission_blocked', replace(base, admission=False)),
                    ('execution_blocked', replace(base, execution=False))]:
        P = m.kernel(p)[0]
        dist = np.zeros(m.N); dist[m.START] = 1.
        rows = []
        for t in range(201):
            if t in (0, 25, 100, 200):
                survive_before = float(dist[m.SAFE].sum())
                post = summary(base, initial=dist)
                assert post['survival'] <= survive_before+1e-13
                rows.append({'restoration_time': t, 'endpoint_time': t+H,
                             'survival_before_restoration': survive_before,
                             'survival_through_endpoint': post['survival'],
                             'post_restoration_mean_events': post['mean_events']})
            dist = dist @ P
        delayed[name] = rows
    nofeedvals = [nofeedback[h][a]['survival']
                  for h in ('baseline', 'admission_blocked', 'execution_blocked', 'both_blocked')
                  for a in ('none', 'admission', 'execution', 'admission_execution')]
    nofeed_range = max(nofeedvals)-min(nofeedvals)
    assert nofeed_range < 1e-13
    out = {
        'description': 'Enumerated synthetic probabilities, not empirical effects',
        'horizon': H,
        'parent_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol_sha256': hashlib.sha256((ROOT/'CAUSAL-PROTOCOL.md').read_bytes()).hexdigest(),
        'equivalence': equivalence_check(replace(base, admission=False), replace(base, execution=False)),
        'interventions': table,
        'no_failure_attrition': nofeedback,
        'no_failure_attrition_survival_range': nofeed_range,
        'accuracy_factorial': interactions,
        'delayed_restoration': delayed,
    }
    dest = ROOT/'causal-results.json'
    dest.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'path': str(dest), 'equivalence': out['equivalence'],
                      'interactions': {k: v['survival_interaction'] for k, v in interactions.items()},
                      'delayed': {k: [{x: r[x] for x in ('restoration_time', 'survival_before_restoration',
                                    'survival_through_endpoint')} for r in v] for k, v in delayed.items()}}, indent=2))


if __name__ == '__main__':
    main()
