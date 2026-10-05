"""Exact constructed checks of all-boundary balance and local nonautonomy."""
import itertools
import json
from pathlib import Path


def partitions(seq):
    if not seq:
        yield ()
        return
    first, *rest = seq
    for partition in partitions(rest):
        yield ((first,),) + partition
        for k in range(len(partition)):
            yield partition[:k] + ((first,) + partition[k],) + partition[k + 1:]


def divergence(currents):
    return [sum(row) for row in currents]


def coarse(currents, partition):
    return [[sum(currents[i][j] for i in left for j in right)
             for right in partition] for left in partition]


n = 4
vertices = tuple(range(n))
edges = tuple(itertools.combinations(vertices, 2))
all_parts = tuple(partitions(list(vertices)))
assert len(all_parts) == 15
all_sets = tuple(tuple(i for i in vertices if mask & (1 << i))
                 for mask in range(1 << n))
counts = {key: 0 for key in (
    'weighted_graphs', 'connected_graphs', 'basis_states', 'subset_balance_checks',
    'partition_balance_checks', 'nested_partition_checks',
    'local_autonomy_iff_checks', 'connected_nontrivial_cut_checks')}

for weights in itertools.product(range(3), repeat=len(edges)):
    w = [[0] * n for _ in vertices]
    for (i, j), weight in zip(edges, weights):
        w[i][j] = w[j][i] = weight
    counts['weighted_graphs'] += 1
    seen, pending = {0}, [0]
    while pending:
        i = pending.pop()
        for j in vertices:
            if w[i][j] and j not in seen:
                seen.add(j)
                pending.append(j)
    connected = len(seen) == n
    counts['connected_graphs'] += connected

    for subset in all_sets[1:-1]:
        exterior = set(vertices) - set(subset)
        # Matrix coefficients from exterior states are exactly the obstruction.
        crossing = any(w[i][j] for i in subset for j in exterior)
        vector_autonomous = all(w[i][j] == 0 for i in subset for j in exterior)
        total_autonomous = all(sum(w[i][j] for i in subset) == 0 for j in exterior)
        assert vector_autonomous == total_autonomous == (not crossing)
        counts['local_autonomy_iff_checks'] += 1
        if connected:
            assert crossing and not vector_autonomous
            counts['connected_nontrivial_cut_checks'] += 1

    for basis in vertices:
        x = [int(i == basis) for i in vertices]
        currents = [[w[i][j] * (x[j] - x[i]) for j in vertices] for i in vertices]
        dx = divergence(currents)
        assert sum(dx) == 0
        counts['basis_states'] += 1
        for subset in all_sets:
            exterior = set(vertices) - set(subset)
            assert sum(dx[i] for i in subset) == sum(currents[i][j]
                   for i in subset for j in exterior)
            counts['subset_balance_checks'] += 1
        for partition in all_parts:
            block_currents = coarse(currents, partition)
            assert divergence(block_currents) == [sum(dx[i] for i in block)
                                                 for block in partition]
            counts['partition_balance_checks'] += 1
            for upper in partitions(list(range(len(partition)))):
                direct_partition = tuple(tuple(i for block in group
                                                for i in partition[block])
                                         for group in upper)
                assert coarse(block_currents, upper) == coarse(currents, direct_partition)
                counts['nested_partition_checks'] += 1

# A nonzero circulation is invisible to all site derivatives.
cycle = [[0, -3, 3], [3, 0, -3], [-3, 3, 0]]
assert divergence(cycle) == [0, 0, 0]
# Every zero-sum integer derivative tested is realizable on a supplied star.
tree_checks = 0
for prefix in itertools.product(range(-3, 4), repeat=3):
    v = [-sum(prefix), *prefix]
    currents = [[0] * 4 for _ in range(4)]
    for i in range(1, 4):
        currents[i][0], currents[0][i] = v[i], -v[i]
    assert divergence(currents) == v
    tree_checks += 1

result = {
    'status': 'all assertions passed',
    'arithmetic': 'exact integer arithmetic; exhaustive weights 0, 1, 2 on six four-site edges',
    'counts': counts,
    'zero_sum_tree_realizations': tree_checks,
    'cycle_current': {'matrix': cycle, 'divergence': divergence(cycle)},
    'scope': 'Constructed checks support the displayed conditional proofs; no physical, cosmological, or ethical empirical claim is tested.',
}
path = Path(__file__).with_name('formal-checks.json')
path.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
