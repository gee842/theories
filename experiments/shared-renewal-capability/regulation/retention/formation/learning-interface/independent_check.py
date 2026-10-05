#!/usr/bin/env python3
"""Independent finite-word and closed-form audit of the declared interfaces.

The producer's graph and probability recursion are comparison targets only.
Gate words are tested against separately stated inventory constraints. Prediction
weights are computed directly from binary innovation words and the first unpaid
round, rather than by calling the producer's transition or moment recurrence.
"""
from collections import defaultdict
from dataclasses import replace
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

import model as producer


HERE = Path(__file__).resolve().parent
ACTIONS = ('probe', 'write', 'repair', 'capture')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def gate_tuple(state):
    # Constructor ordering is part of the audited producer interface.
    flag = getattr(state, 'correct_memory_before_first_repair',
                   getattr(state, 'learned_first_repair', False))
    return (state.source, state.fuel, state.intact, state.record,
            state.weight, state.delivered, flag)


def word_states(theta, fuel, word):
    """A word interpreter with separate expense, conversion and record ledgers."""
    source, spent, converted = theta, 0, 0
    intact, record, weight, memory_before = False, -1, -1, False
    states = [(theta, fuel, intact, record, weight, False, memory_before)]
    for action in word:
        available = fuel + converted - spent
        reference = source + converted
        if action in ('probe', 'write', 'repair') and available < 1:
            return None
        if action == 'probe':
            spent += 1
            record = reference
        elif action == 'write':
            if record < 0:
                return None
            spent += 1
            weight = record
        elif action == 'repair':
            if intact:
                return None
            spent += 1
            intact = True
            memory_before = weight == reference
        elif action == 'capture':
            if not intact or not source:
                return None
            source -= 1
            converted += 1
        else:
            raise AssertionError(action)
        state = (source, fuel + converted - spent, intact, record, weight,
                 bool(converted), memory_before)
        assert state[0] + state[1] + spent == theta + fuel
        assert source + converted == theta
        states.append(state)
    return states


def gate_audit(theta, fuel):
    """Exhaust all complete words up to the independently derived rank bound."""
    nodes, edges = set(), set()
    root = (theta, fuel, False, -1, -1, False, False)
    nodes.add(root)
    # Each expense or source conversion lowers F+2E by exactly one.
    bound = fuel + 2*theta
    for length in range(1, bound+1):
        for word in product(ACTIONS, repeat=length):
            history = word_states(theta, fuel, word)
            if history is None:
                continue
            nodes.update(history)
            for s, action, t in zip(history, word, history[1:]):
                assert 2*t[0]+t[1] == 2*s[0]+s[1]-1
                edges.add((s, action, t))
    actual = producer.gate_graph(producer.Gate(theta, fuel))
    actual_nodes = {gate_tuple(s) for s in actual}
    actual_edges = {(gate_tuple(s), a, gate_tuple(t))
                    for s, out in actual.items() for a, t in out}
    assert actual_nodes == nodes
    assert actual_edges == edges
    observed = {
        'identification_reachable': any(s[3] == theta for s in nodes),
        'write_reachable': any(s[4] == theta for s in nodes),
        'delivery_reachable': any(s[5] for s in nodes),
        'correct_memory_before_delivered_first_repair':
            any(s[5] and s[6] for s in nodes),
    }
    assert observed['identification_reachable'] == (fuel >= 1)
    assert observed['write_reachable'] == (fuel >= 2)
    assert observed['delivery_reachable'] == (theta == 1 and fuel >= 1)
    assert observed['correct_memory_before_delivered_first_repair'] == (theta == 1 and fuel >= 3)
    return {'states': len(nodes), 'edges': len(edges), **observed}


def word_endpoint(word, initial_fuel, eta, decay):
    """Direct finite-series value, after stopping at the first unpayable round."""
    paid, cumulative_loss = 0, 0
    for bit in word:
        if initial_fuel-2*cumulative_loss < 2:
            break
        paid += 1
        cumulative_loss += bit
    r = 1-eta-decay
    weight = eta*sum(Q(word[k])*r**(paid-1-k) for k in range(paid))
    weight *= (1-decay)**(len(word)-paid)
    common = initial_fuel-2*cumulative_loss
    source = 2*len(word)-2*(paid-cumulative_loss)
    assert common+source+2*paid == initial_fuel+2*len(word)
    assert common >= 0 and source >= 0 and 0 <= weight <= 1
    return common, source, weight, paid, cumulative_loss


def prediction_audit(rounds, fuel, p=Q(1, 2), eta=Q(1, 4), decay=Q(0)):
    distribution = defaultdict(Q)
    for word in product((0, 1), repeat=rounds):
        probability = p**sum(word)*(1-p)**(rounds-sum(word))
        if probability:
            distribution[word_endpoint(word, fuel, eta, decay)] += probability
    assert sum(distribution.values()) == 1
    mean = sum(m*s[2] for s, m in distribution.items())
    reserve = sum(m for s, m in distribution.items() if s[0] >= 2)
    live_sum = sum(m*s[2] for s, m in distribution.items() if s[0] >= 2)
    all_paid = sum(m for s, m in distribution.items() if s[3] == rounds)
    completed = sum(m*s[3] for s, m in distribution.items())
    independent = {
        'mean_retained_weight': str(mean),
        'operating_reserve_probability': str(reserve),
        'mean_weight_given_operating_reserve': str(live_sum/reserve) if reserve else None,
        'mean_completed_rounds': str(completed),
        'all_rounds_paid_probability': str(all_paid),
        'endpoint_count': len(distribution),
    }
    actual = producer.exact_prediction(rounds, fuel, p, eta, decay)
    for key, value in independent.items():
        assert actual[key] == value, (rounds, fuel, p, eta, decay, key, value, actual[key])
    for time, moment in enumerate(actual['moments']):
        ew = eu = euw = after = Q(0)
        for prefix in product((0, 1), repeat=time):
            mass = p**sum(prefix)*(1-p)**(time-sum(prefix))
            state = word_endpoint(prefix, fuel, eta, decay)
            ew += mass*state[2]
            eu += mass*int(state[0] >= 2)
            euw += mass*int(state[0] >= 2)*state[2]
            for bit, probability in ((0, 1-p), (1, p)):
                after += mass*probability*word_endpoint(prefix+(bit,), fuel, eta, decay)[2]
        expected = {'before_mean': str(ew), 'paid_probability': str(eu),
                    'paid_target_mean': str(p*eu), 'paid_weight_mean': str(euw),
                    'after_mean': str(after)}
        assert moment == expected
    # Held-out fresh Bernoulli outcome is an analyst score, not runtime reward.
    parameter_error = sum(m*(s[2]-p)**2 for s, m in distribution.items())
    heldout_error = sum(m*((1-p)*s[2]**2+p*(1-s[2])**2)
                       for s, m in distribution.items())
    assert heldout_error == p*(1-p)+parameter_error
    threshold = sum(m for s, m in distribution.items() if s[2] > Q(1, 4))
    assert actual['parameter_squared_error'] == str(parameter_error)
    assert actual['held_out_squared_loss'] == str(heldout_error)
    assert actual['strictly_above_quarter_probability'] == str(threshold)
    independent.update({'rounds': rounds, 'fuel': fuel, 'loss_probability': str(p),
                        'gain': str(eta), 'decay': str(decay),
                        'parameter_squared_error': str(parameter_error),
                        'fresh_outcome_squared_error': str(heldout_error),
                        'strictly_above_quarter_probability': str(threshold),
                        'source_exhausted_probability': str(sum(m for s, m in distribution.items() if s[1] == 0))})
    return independent


def controller_audit():
    declarations = (
        ('memory_positive', 1, 3, 'memory', ('probe', 'write', 'repair', 'capture'), 'stopped'),
        ('memory_insufficient', 1, 2, 'memory', ('probe', 'write'), 'disabled'),
        ('memory_absent', 0, 3, 'memory', ('probe', 'write'), 'stopped'),
        ('direct_less_fuel', 1, 2, 'direct', ('probe', 'repair', 'capture', 'write'), 'stopped'),
        ('inverse_positive', 1, 3, 'inverse', ('probe', 'write'), 'stopped'),
        ('inverse_absent', 0, 3, 'inverse', ('probe', 'write', 'repair'), 'disabled'),
    )
    report = {}
    for name, theta, fuel, route, word, status in declarations:
        states, actions, actual_status = producer.gate_controlled_path(producer.Gate(theta, fuel), route)
        assert tuple(actions) == word and actual_status == status
        assert list(map(gate_tuple, states)) == word_states(theta, fuel, word)
        report[name] = {'actions': actions, 'status': actual_status,
                        'endpoint': gate_tuple(states[-1])}
    learned = producer.gate_path(producer.Gate(1, 3), ('probe', 'write'))[-1]
    assert producer.gate_controller(producer.gate_observation(learned)) == 'repair'
    assert producer.gate_controller(producer.gate_observation(replace(learned, weight=0))) is None
    assert producer.gate_controller(producer.gate_observation(learned), 'inverse') is None
    # The same accessible state always produces the same command, even when
    # hidden source differs. The true feasibility of capture can still differ.
    for theta in (0, 1):
        root = producer.Gate(theta, 3)
        for state in producer.gate_graph(root):
            hidden_changed = replace(state, source=1-state.source)
            assert producer.gate_observation(state) == producer.gate_observation(hidden_changed)
            for route in ('memory', 'direct', 'inverse'):
                assert producer.gate_controller(producer.gate_observation(state), route) == producer.gate_controller(producer.gate_observation(hidden_changed), route)
    report['clamps'] = {'correct_memory_command': 'repair', 'zero_memory_command': None,
                        'same_memory_inverse_command': None,
                        'hidden_source_not_read_by_controller': True}
    return report


def run():
    names = ('model.py', 'check.py', 'PROTOCOL.md', 'results.json', 'independent_check.py')
    inputs = {name: digest(HERE/name) for name in names}
    saved_producer = json.loads((HERE/'results.json').read_text())
    assert saved_producer['status'] == 'passed'
    assert saved_producer['source_hashes'] == {name: inputs[name]
                                             for name in ('model.py', 'check.py', 'PROTOCOL.md')}
    gates = {f'source_{theta}_fuel_{fuel}': gate_audit(theta, fuel)
             for theta in (0, 1) for fuel in range(6)}
    paths = {}
    for name, fuel, word in (
            ('primary', 3, ('probe', 'write', 'repair', 'capture')),
            ('probe_then_retrospective_write', 2, ('probe', 'repair', 'capture', 'write')),
            ('blind_then_retrospective_write', 2, ('repair', 'capture', 'probe', 'write'))):
        history = word_states(1, fuel, word)
        assert history is not None and history[-1][4:6] == (1, True)
        assert history[-1][6] == (name == 'primary')
        assert [gate_tuple(s) for s in producer.gate_path(producer.Gate(1, fuel), word)] == history
        paths[name] = {'fuel': fuel, 'actions': word, 'states': history}
    assert word_states(1, 2, ('probe', 'write', 'repair', 'capture')) is None
    controllers = controller_audit()
    primary = {
        'funded': prediction_audit(3, 6),
        'scarce': prediction_audit(3, 2),
        'funded_decay': prediction_audit(3, 6, decay=Q(1, 8)),
        'unfunded': prediction_audit(3, 1),
    }
    assert primary['funded']['mean_retained_weight'] == '37/128'
    assert primary['scarce']['mean_retained_weight'] == '7/32'
    assert primary['funded']['fresh_outcome_squared_error'] == '2653/8192'
    assert primary['scarce']['fresh_outcome_squared_error'] == '43/128'
    assert primary['scarce']['operating_reserve_probability'] == '1/8'
    assert primary['scarce']['all_rounds_paid_probability'] == '1/4'
    assert primary['funded']['strictly_above_quarter_probability'] == '1/2'
    assert primary['scarce']['strictly_above_quarter_probability'] == '0'
    for name, independently in primary.items():
        for key in ('mean_retained_weight', 'parameter_squared_error',
                    'strictly_above_quarter_probability', 'operating_reserve_probability',
                    'mean_weight_given_operating_reserve', 'all_rounds_paid_probability'):
            assert saved_producer['prediction_cases'][name][key] == independently[key]
    for name, independently in gates.items():
        for key in ('states', 'edges', 'identification_reachable', 'write_reachable', 'delivery_reachable'):
            assert saved_producer['gate_cases'][name][key] == independently[key]
    worlds = [producer.Gate(theta, 3) for theta in (0, 1)]
    assert producer.gate_observation(worlds[0]) == producer.gate_observation(worlds[1])
    assert producer.gate_target(worlds[0]) != producer.gate_target(worlds[1])
    observed = [producer.gate_path(s, ('probe',))[-1] for s in worlds]
    assert producer.gate_observation(observed[0]) != producer.gate_observation(observed[1])
    assert not producer.exact_teacher_exists(worlds, producer.gate_observation, producer.gate_target)
    assert producer.exact_teacher_exists(observed, producer.gate_observation, producer.gate_target)
    extra = 0
    for rounds in range(7):
        for p in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            for eta in (Q(1, 4), Q(1, 2), Q(1)):
                for fuel in sorted({0, 1, 2, 2*rounds}):
                    prediction_audit(rounds, fuel, p, eta)
                    extra += 1
    # Additional rational decay cases exercise unpaid decay and finite sums.
    decay_cases = 0
    for rounds in range(5):
        for fuel in (1, 2, 2*rounds):
            for p in (Q(1, 4), Q(1, 2), Q(3, 4)):
                prediction_audit(rounds, fuel, p, Q(1, 4), Q(1, 8))
                decay_cases += 1
    assert all(digest(HERE/name) == value for name, value in inputs.items())
    report = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'source_hashes': inputs, 'unchanged_inputs': True,
        'scope': 'Independent exact finite-word and closed-form checks of supplied laws; no empirical, origin-of-architecture, ethics or formal refinement claim.',
        'gate_cases': gates, 'paths': paths, 'prediction_cases': primary,
        'controller_cases': controllers,
        'additional_parameter_cases': extra, 'additional_decay_cases': decay_cases,
    }
    (HERE/'independent-check.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'gate_cases': len(gates),
                      'additional_parameter_cases': extra,
                      'additional_decay_cases': decay_cases}, indent=2))


if __name__ == '__main__':
    run()
