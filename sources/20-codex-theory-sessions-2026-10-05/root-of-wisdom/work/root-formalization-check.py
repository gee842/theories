"""Exact finite checks of a scoped observation-based acceptability theorem.

Acceptability and normative constraints are supplied inputs, not moral facts
established by this script. Policies are deterministic and terminate in one action.
"""
from itertools import product
from pathlib import Path
import json


def partitions(n):
    # Canonical restricted-growth labels enumerate each set partition once.
    result = []
    def add(labels):
        if len(labels) == n:
            result.append(tuple(labels))
            return
        upper = 0 if not labels else max(labels) + 1
        for label in range(upper + 1):
            add(labels + [label])
    add([])
    return result


def policy_witness(acceptable, labels, actions):
    # This enumeration does not use the intersection criterion.
    nclasses = max(labels) + 1
    for policy in product(actions, repeat=nclasses):
        if all(policy[labels[world]] in acceptable[world] for world in range(len(labels))):
            return policy
    return None


def intersection_certificate(acceptable, labels):
    classes = [tuple(i for i, label in enumerate(labels) if label == c)
               for c in range(max(labels) + 1)]
    intersections = []
    for members in classes:
        common = set(acceptable[members[0]])
        for world in members[1:]:
            common.intersection_update(acceptable[world])
        intersections.append(common)
    return all(intersections), intersections


worlds = range(3)
actions = tuple(range(3))
world_partitions = partitions(3)
assert world_partitions == [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 1, 2)]
tested = positive = negative = enumerated_policy_candidates = 0
by_partition = []
for labels in world_partitions:
    successes = 0
    for mask in range(1 << 9):
        acceptable = [set(a for a in actions if mask & (1 << (3 * w + a))) for w in worlds]
        witness = policy_witness(acceptable, labels, actions)
        predicted, intersections = intersection_certificate(acceptable, labels)
        actual = witness is not None
        assert actual == predicted, (labels, mask, acceptable, witness, intersections)
        if predicted:
            # Independently verify the constructive witness chosen from intersections.
            constructed = tuple(min(s) for s in intersections)
            assert all(constructed[labels[w]] in acceptable[w] for w in worlds)
        else:
            assert any(not s for s in intersections)
        tested += 1
        positive += actual
        negative += not actual
        successes += actual
        enumerated_policy_candidates += len(actions) ** (max(labels) + 1)
    by_partition.append({'labels': labels, 'matrices_checked': 512, 'policy_exists': successes})
assert tested == 2560


def query_plan_exists(acceptable, budget, deadline, query_labels=(0, 1),
                      query_cost=1, query_duration=1, query_permission=True):
    """Declared two-stage policy class: act directly, or query once then act.

    Every terminal action costs one unit and takes one time step. The initial
    observation is the same in both worlds. No implicit free query is admitted.
    """
    if budget >= 1 and deadline >= 1:
        if policy_witness(acceptable, (0, 0), (0, 1)) is not None:
            return True
    if query_permission and budget >= query_cost + 1 and deadline >= query_duration + 1:
        if policy_witness(acceptable, query_labels, (0, 1)) is not None:
            return True
    return False


query_records = []
unique = [{0}, {1}]
common = [{0}, {0}]
for budget, deadline in product(range(4), repeat=2):
    specifications = [
        ('distinct_required_actions', unique, {}, budget >= 2 and deadline >= 2),
        ('common_action', common, {}, budget >= 1 and deadline >= 1),
        ('query_permission_absent', unique, {'query_permission': False}, False),
        ('query_is_uninformative', unique, {'query_labels': (0, 0)}, False),
        ('slower_query', unique, {'query_duration': 2}, budget >= 2 and deadline >= 3),
    ]
    for name, acceptable, settings, expected in specifications:
        actual = query_plan_exists(acceptable, budget, deadline, **settings)
        assert actual == expected, (name, budget, deadline, actual, expected)
        query_records.append({'case': name, 'budget': budget, 'deadline': deadline, 'policy_exists': actual})
assert len(query_records) == 80

result = {
    'status': 'all exact checks passed',
    'scope': 'finite deterministic one-step policies and an explicitly bounded one-query extension',
    'normative_status': 'acceptable sets are stipulated; these checks do not justify the standards or prove wisdom',
    'terminal_theorem': {
        'worlds': 3,
        'actions': 3,
        'acceptability_matrices': 512,
        'observation_partitions': 5,
        'instances_checked': tested,
        'instances_with_policy': positive,
        'instances_without_policy': negative,
        'full_policy_space_sizes_summed': enumerated_policy_candidates,
        'meaning_of_previous_field': 'sum of candidate policy class sizes; search may stop after finding a witness',
        'by_partition': by_partition,
    },
    'query_extension': {
        'instances_checked': len(query_records),
        'terminal_action_cost': 1,
        'terminal_action_duration': 1,
        'normal_query_cost': 1,
        'normal_query_duration': 1,
        'records': query_records,
    },
}
Path('work/root-formalization-check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({
    'status': result['status'],
    'terminal_instances': tested,
    'policy_exists': positive,
    'no_policy': negative,
    'query_extension_instances': len(query_records),
    'by_partition': by_partition,
}, indent=2))
