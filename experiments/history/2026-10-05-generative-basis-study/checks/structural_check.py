"""Exact checks of the supplied structural network; standard library only."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NAMES = tuple('c y r k a v m b p j'.split())
INDEX = {name: i for i, name in enumerate(NAMES)}
STATES = tuple(product((0, 1), repeat=10))
INPUTS = tuple(product((0, 1), repeat=4))
NOISE = ((0, 0, Fraction(3, 8)), (0, 1, Fraction(3, 8)),
         (1, 0, Fraction(1, 8)), (1, 1, Fraction(1, 8)))
PARENTS = {
    'c': {'c'}, 'y': {'a', 'v', 'k', 'r', 'y'},
    'r': {'k', 'c', 'r'}, 'k': {'m', 'k'},
    'a': {'p', 'a', 'm', 'v'}, 'v': {'p'},
    'm': {'b', 'r', 'a', 'v'}, 'b': {'y', 'c', 'm'},
    'p': {'p', 'k', 'b'}, 'j': {'j'},
}
SEED = {'b', 'v', 'p'}


def update(state, proposal, disturbance, badge_noise, badge_mode=False):
    c, y, r, k, a, v, m, b, p, j = state
    execute, probe, train, veto = proposal
    authority = p & (a | m) & (1-v)
    if badge_mode:
        authority &= j
    return (
        c ^ disturbance,
        r if a and not v and k and execute else y,
        c ^ disturbance if k and probe else r,
        1 if m and train else k & (1-disturbance),
        authority,
        p & veto,
        (b | r) & a & (1-v),
        (y ^ c) | (m & disturbance),
        p & (k | (1-b)),
        j ^ badge_noise,
    )


def closure(parents):
    trace = [set(SEED)]
    while True:
        expanded = trace[-1] | set().union(*(parents[i] for i in trace[-1]))
        if expanded == trace[-1]:
            return trace
        trace.append(expanded)


def ordered(names):
    return [name for name in NAMES if name in names]


def project(state, retained):
    return tuple(state[INDEX[name]] for name in NAMES if name in retained)


def projected_law(state, proposal, retained, badge_mode=False):
    law = defaultdict(Fraction)
    for e, j, probability in NOISE:
        target = update(state, proposal, e, j, badge_mode)
        law[project(target, retained)] += probability
    return dict(law)


def boolean_dependencies(badge_mode=False):
    # Exhaustively compare every pair differing in exactly one old-state bit.
    dependencies = {name: set() for name in NAMES}
    comparisons = 0
    for source_index, source_name in enumerate(NAMES):
        for state in STATES:
            if state[source_index]:
                continue
            changed = list(state)
            changed[source_index] = 1
            for proposal in INPUTS:
                for e, j, _ in NOISE:
                    left = update(state, proposal, e, j, badge_mode)
                    right = update(changed, proposal, e, j, badge_mode)
                    for target_index, target_name in enumerate(NAMES):
                        if left[target_index] != right[target_index]:
                            dependencies[target_name].add(source_name)
                    comparisons += 1
    return dependencies, comparisons


def state_with(**values):
    return tuple(values.get(name, 0) for name in NAMES)


def event_probability(state, proposal, coordinate, badge_mode=False):
    return sum(probability for e, j, probability in NOISE
               if update(state, proposal, e, j, badge_mode)[INDEX[coordinate]])


def propagate(initial, proposals, badge_mode=False):
    law = {initial: Fraction(1)}
    for proposal in proposals:
        new = defaultdict(Fraction)
        for state, mass in law.items():
            for e, j, probability in NOISE:
                new[update(state, proposal, e, j, badge_mode)] += mass*probability
        law = new
    return dict(law)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    trace = closure(PARENTS)
    assert list(map(len, trace)) == [3, 7, 9]
    retained = trace[-1]
    assert retained == set(NAMES) - {'j'}
    actual_parents, comparisons = boolean_dependencies()
    assert actual_parents == PARENTS

    kernel_pairs = 0
    for state in STATES:
        if state[-1]:
            continue
        changed = state[:-1] + (1,)
        for proposal in INPUTS:
            assert projected_law(state, proposal, retained) == projected_law(changed, proposal, retained)
            kernel_pairs += 1
    assert kernel_pairs == 8192

    no_maintenance, maintenance = state_with(p=1), state_with(p=1, m=1)
    assert project(no_maintenance, SEED) == project(maintenance, SEED)
    maintenance_probabilities = []
    for proposal in INPUTS:
        pair = (event_probability(no_maintenance, proposal, 'b'),
                event_probability(maintenance, proposal, 'b'))
        assert pair == (0, Fraction(1, 4))
        maintenance_probabilities.append(tuple(map(str, pair)))

    expanded_parents = {name: set(parents) for name, parents in PARENTS.items()}
    expanded_parents['a'].add('j')
    expanded_trace = closure(expanded_parents)
    assert list(map(len, expanded_trace)) == [3, 7, 9, 10]
    expanded_actual, expanded_comparisons = boolean_dependencies(badge_mode=True)
    assert expanded_actual == expanded_parents
    left = state_with(p=1, a=1)
    right = state_with(p=1, a=1, j=1)
    proposal = (0, 0, 0, 0)
    authority_probabilities = (event_probability(left, proposal, 'a', True),
                               event_probability(right, proposal, 'a', True))
    assert authority_probabilities == (0, 1)
    assert projected_law(left, proposal, retained, True) != projected_law(right, proposal, retained, True)

    # The internal authority difference also reaches an originally protected
    # output. This fixed witness is checked exactly, not selected by a search.
    # At t=1 authority differs; at t=2 executing the stored record differs;
    # at t=3 the burden reads the previously implemented setting.
    left = state_with(r=1, k=1, a=1, p=1)
    right = state_with(r=1, k=1, a=1, p=1, j=1)
    sequence = ((0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0))
    left_law, right_law = propagate(left, sequence, True), propagate(right, sequence, True)
    burden_probabilities = tuple(sum(mass for state, mass in law.items() if state[INDEX['b']])
                                 for law in (left_law, right_law))
    assert burden_probabilities[0] != burden_probabilities[1]

    result = {
        'scope': 'Exact finite verification of supplied equations; no empirical validation or semantic minimality claim.',
        'state_count': len(STATES), 'proposal_count': len(INPUTS),
        'joint_noise_weights': [str(p) for _, _, p in NOISE],
        'baseline_closure': [ordered(s) for s in trace],
        'retained_coordinate_state_count': 2**len(retained),
        'derived_dependencies_match_listed': True,
        'baseline_single_bit_comparisons': comparisons,
        'projected_kernel_pairs_equal': kernel_pairs,
        'maintenance_witness_next_burden': maintenance_probabilities[0],
        'maintenance_witness_valid_for_all_proposals': True,
        'expanded_closure': [ordered(s) for s in expanded_trace],
        'expanded_single_bit_comparisons': expanded_comparisons,
        'expanded_witness_next_authority': list(map(str, authority_probabilities)),
        'expanded_original_burden_witness': {
            'states': [list(left), list(right)], 'proposals': sequence,
            'horizon': 3, 'final_burden_probabilities': list(map(str, burden_probabilities)),
        },
        'source_sha256': {str(p.relative_to(ROOT)): digest(p) for p in (
            Path(__file__).resolve(), ROOT/'STRUCTURAL-CHECKPLAN.md', ROOT/'formal/STRUCTURAL-CLOSURE.md')},
    }
    destination = ROOT/'checks/structural_results.json'
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
