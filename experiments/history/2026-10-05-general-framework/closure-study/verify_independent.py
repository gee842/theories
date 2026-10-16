"""Independent rational event enumeration and graph audit of analyze.py.

This checker deliberately does not call the production event builder, decision
rule, coin helper, or appointment helper to construct its own transitions.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

import numpy as np


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'analyze.py'
STATES = list(product(range(2), range(2), range(2), range(3), (-1, 0, 1)))
INDEX = {s: i for i, s in enumerate(STATES)}
SAFE = np.array([s[3] > 0 for s in STATES])
START = INDEX[(0, 0, 1, 2, 0)]


def chance(bit, probability):
    return probability if bit else 1 - probability


def independent_kernel(p):
    hazard, accuracy, base, failure, forget, entry, wv, wa = (
        F(str(value)) for value in (
            p.hazard, p.accuracy, p.delta_base, p.delta_failure,
            p.forget, p.entry, p.w_volume, p.w_adaptive))
    rows = []
    for e, r, q, k, b in STATES:
        row = defaultdict(F)
        for flip, enter, wrong, turn, appointee, lost in product((0, 1), repeat=6):
            probability = chance(flip, hazard) * chance(enter, entry if k == 0 else F(0))
            if not probability:
                continue
            en = e ^ flip
            ka, qa = (1, 1) if enter else (k, q)
            inquiry = qa == 1 and ka == 2
            teaching = qa == 1 and ka == 1
            probability *= chance(wrong, 1 - accuracy if inquiry else F(0))
            if not probability:
                continue
            bn = en ^ wrong if inquiry and p.admission else b
            rn = bn if qa == 1 and ka > 0 and p.execution and bn != -1 else r
            kn = ka + int(teaching and p.training)
            probability *= chance(turn, base + failure * int(rn != en))
            if not probability:
                continue
            kn = max(0, kn - turn)
            if not turn:
                adaptive_probability = F(qa)
            elif kn == 0 or p.succession == 'volume':
                adaptive_probability = F(0)
            elif p.succession == 'protected':
                adaptive_probability = F(1)
            else:
                weight = wa if qa else wv
                adaptive_probability = kn * weight / (1 + kn * weight)
            probability *= chance(appointee, adaptive_probability)
            probability *= chance(lost, forget if turn else F(0))
            if probability:
                dest = (en, rn, appointee, kn, -1 if lost else bn)
                row[INDEX[dest]] += probability
        assert sum(row.values(), F(0)) == 1
        assert all(value > 0 for value in row.values())
        rows.append(dict(row))
    return rows


def graph_properties(rows):
    adjacency = np.array([[j in rows[i] for j in range(len(STATES))]
                          for i in range(len(STATES))])
    reach = adjacency.copy()
    np.fill_diagonal(reach, True)
    for k in range(len(STATES)):
        reach |= reach[:, k, None] & reach[k, None, :]
    core = [i for i in range(len(STATES)) if SAFE[i] and not reach[i, ~SAFE].any()]
    done, bottom = set(), []
    for i in range(len(STATES)):
        if i in done:
            continue
        component = np.flatnonzero(reach[i] & reach[:, i])
        done.update(component.tolist())
        outside = np.ones(len(STATES), dtype=bool)
        outside[component] = False
        exits = adjacency[np.ix_(component, np.flatnonzero(outside))].any()
        if not exits and reach[START, component].any():
            bottom.append(tuple(component.tolist()))
    return adjacency, core, sorted(bottom)


def rational_survival(rows, horizon):
    distribution = {START: F(1)}
    for _ in range(horizon):
        updated = defaultdict(F)
        for i, probability in distribution.items():
            for j, weight in rows[i].items():
                if SAFE[j]:
                    updated[j] += probability * weight
        distribution = dict(updated)
    return sum(distribution.values(), F(0))


def main():
    spec = importlib.util.spec_from_file_location('closure_production_for_audit', SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    assert STATES == module.STATES
    primary = module.Params()
    arms = {
        'endogenous': primary,
        'protected': module.replace(primary, succession='protected'),
        'no_admission': module.replace(primary, admission=False),
        'no_execution': module.replace(primary, execution=False),
        'no_training': module.replace(primary, training=False),
        'rare_adverse': module.replace(primary, w_adaptive=10000.),
        'reentry': module.replace(primary, entry=.01),
    }
    recorded = json.loads((ROOT / 'results' / 'analysis.json').read_text())
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert source_hash == recorded['metadata']['source_sha256']
    report = {}
    for name, params in arms.items():
        rows = independent_kernel(params)
        matrix = np.array([[float(rows[i].get(j, 0)) for j in range(len(STATES))]
                           for i in range(len(STATES))])
        production = module.kernel(params)[0]
        adjacency, core, classes = graph_properties(rows)
        assert np.array_equal(adjacency, production > 0)
        assert core == module.closed_core(production)
        assert classes == sorted(tuple(c.tolist()) for c in module.recurrent_classes(production))
        difference = float(np.max(np.abs(matrix - production)))
        assert difference < 2e-15
        result = {
            'rational_stochastic_rows': len(rows),
            'maximum_probability_difference': difference,
            'same_support': True, 'same_safe_core': True, 'same_bottom_classes': True,
            'safe_core_state_indices': core,
            'reachable_bottom_class_indices': classes,
        }
        if name in ('endogenous', 'rare_adverse'):
            value = rational_survival(rows, 200)
            recorded_value = recorded['arms'][name]['checkpoints']['200']['never_lost_capacity']
            assert abs(float(value) - recorded_value) < 2e-12
            result['survival_200_exact_fraction'] = str(value)
            result['survival_200_decimal'] = float(value)
            result['difference_from_recorded_survival'] = float(value) - recorded_value
        report[name] = result
    output = {
        'scope': 'Independent rational branch enumeration and graph audit of the seven stated arms.',
        'production_source_sha256': source_hash,
        'checker_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol_sha256': hashlib.sha256((ROOT / 'PROTOCOL.md').read_bytes()).hexdigest(),
        'all_checks_passed': True,
        'arms': report,
    }
    destination = ROOT / 'results' / 'independent_verification.json'
    destination.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({'all_checks_passed': True, 'arms': len(arms),
                      'report': str(destination), 'source_sha256': source_hash}))


if __name__ == '__main__':
    main()
