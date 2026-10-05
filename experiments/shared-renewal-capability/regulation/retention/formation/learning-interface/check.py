#!/usr/bin/env python3
"""Exact finite checks, including failed and unfunded histories."""
from dataclasses import asdict, replace
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
from model import (Gate, gate_observation, gate_target, gate_current_contrast,
                   gate_graph, gate_path, exact_prediction, exact_teacher_exists,
                   gate_controller, gate_controlled_path)

HERE = Path(__file__).resolve().parent


def run():
    inputs = {name: sha256((HERE/name).read_bytes()).hexdigest()
              for name in ('model.py', 'check.py', 'PROTOCOL.md')}
    gate_cases = {}
    for theta in (0, 1):
        for fuel in range(6):
            root = Gate(theta, fuel)
            net = gate_graph(root)
            delivered_after_learned_action = any(s.delivered and s.correct_memory_before_first_repair for s in net)
            identified = any(s.record == theta for s in net)
            written = any(s.weight == theta for s in net)
            delivered = any(s.delivered for s in net)
            assert identified == (fuel >= 1)
            assert written == (fuel >= 2)
            assert delivered == (theta == 1 and fuel >= 1)
            assert delivered_after_learned_action == (theta == 1 and fuel >= 3)
            gate_cases[f'source_{theta}_fuel_{fuel}'] = {
                'states': len(net), 'edges': sum(map(len, net.values())),
                'identification_reachable': identified, 'write_reachable': written,
                'delivery_reachable': delivered,
                'delivery_after_correct_memory_before_first_repair': delivered_after_learned_action,
            }
    worlds = [Gate(theta, 3) for theta in (0, 1)]
    assert not exact_teacher_exists(worlds, gate_observation, gate_target)
    probed = [gate_path(s, ['probe'])[-1] for s in worlds]
    assert exact_teacher_exists(probed, gate_observation, gate_target)
    paths = {}
    declarations = [('primary', 3, ['probe', 'write', 'repair', 'capture']),
                    ('record_driven_then_write', 2, ['probe', 'repair', 'capture', 'write']),
                    ('blind_then_measure', 2, ['repair', 'capture', 'probe', 'write'])]
    for name, fuel, actions in declarations:
        states = gate_path(Gate(1, fuel), actions)
        assert states is not None and states[-1].weight == 1 and states[-1].delivered
        assert states[-1].correct_memory_before_first_repair == (name == 'primary')
        assert gate_target(states[-1]) == 1 and gate_current_contrast(states[-1]) == 0
        paths[name] = {'actions': actions, 'states': [asdict(s) for s in states]}
    assert gate_path(Gate(1, 2), ['probe', 'write', 'repair', 'capture']) is None
    controlled = {}
    for theta in (0, 1):
        for fuel in (2, 3):
            for routing in ('memory', 'direct', 'inverse'):
                states, actions, stop = gate_controlled_path(Gate(theta, fuel), routing)
                controlled[f'source_{theta}_fuel_{fuel}_{routing}'] = {
                    'actions': actions, 'states': [asdict(s) for s in states], 'stop': stop}
                if routing == 'memory':
                    assert states[-1].delivered == (theta == 1 and fuel == 3)
                if routing == 'direct':
                    assert states[-1].delivered == (theta == 1)
                if routing == 'inverse':
                    assert not states[-1].delivered
    calibrated = gate_path(Gate(1, 3), ['probe', 'write'])[-1]
    assert gate_controller(gate_observation(calibrated)) == 'repair'
    assert gate_controller(gate_observation(replace(calibrated, weight=0))) is None
    cases = {
        'funded': exact_prediction(3, 6),
        'scarce': exact_prediction(3, 2),
        'funded_decay': exact_prediction(3, 6, decay=Q(1, 8)),
        'unfunded': exact_prediction(3, 1),
    }
    assert Q(cases['funded']['mean_retained_weight']) == Q(37, 128)
    assert Q(cases['scarce']['mean_retained_weight']) == Q(7, 32)
    assert Q(cases['funded_decay']['mean_retained_weight']) == Q(129, 512)
    assert Q(cases['funded']['parameter_squared_error']) == Q(605, 8192)
    assert Q(cases['funded']['held_out_squared_loss']) == Q(2653, 8192)
    assert Q(cases['scarce']['parameter_squared_error']) == Q(11, 128)
    assert Q(cases['scarce']['held_out_squared_loss']) == Q(43, 128)
    # A mean above a downstream strict-choice threshold is not a pathwise claim.
    assert Q(cases['funded']['mean_retained_weight']) > Q(1, 4)
    assert Q(cases['funded']['strictly_above_quarter_probability']) == Q(1, 2)
    assert Q(cases['scarce']['strictly_above_quarter_probability']) == 0
    assert Q(cases['scarce']['operating_reserve_probability']) == Q(1, 8)
    assert Q(cases['scarce']['mean_weight_given_operating_reserve']) == 0
    assert Q(cases['funded']['all_rounds_paid_probability']) == 1
    assert Q(cases['scarce']['all_rounds_paid_probability']) == Q(1, 4)
    audited = 0
    for n in range(7):
        for p in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            for eta in (Q(1, 4), Q(1, 2), Q(1)):
                for fuel in sorted({0, 1, 2, 2*n}):
                    r = exact_prediction(n, fuel, p, eta)
                    if fuel >= 2*n:
                        assert Q(r['mean_retained_weight']) == p*(1-(1-eta)**n)
                        assert Q(r['all_rounds_paid_probability']) == 1
                    if fuel == 2:
                        assert Q(r['mean_retained_weight']) == eta*(1-(1-p)**n)
                        assert Q(r['operating_reserve_probability']) == (1-p)**n
                    audited += 1
    assert all(sha256((HERE/k).read_bytes()).hexdigest() == v for k, v in inputs.items())
    report = {'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'source_hashes': inputs, 'unchanged_inputs': True,
              'scope': 'Exact finite declared laws and moment identities; no empirical calibration, learner-origin, valence, ethical or universal advantage claim.',
              'gate_cases': gate_cases, 'paths': paths, 'controllers': controlled, 'prediction_cases': cases,
              'additional_parameter_cases': audited}
    (HERE/'results.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'gate_cases': len(gate_cases),
                      'prediction_cases': len(cases), 'parameter_cases': audited}, indent=2))


if __name__ == '__main__':
    run()
