"""Exact finite checks for the composition audit; no empirical experiment."""
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path


def cycle_check(n, edges):
    """Assign signs along a spanning forest, then check all edges."""
    adj = [[] for _ in range(n)]
    for i, j, sign in edges:
        adj[i].append((j, sign))
        adj[j].append((i, sign))
    values = [None] * n
    components = 0
    for root in range(n):
        if values[root] is not None:
            continue
        components += 1
        values[root] = 1
        queue = [root]
        while queue:
            i = queue.pop()
            for j, sign in adj[i]:
                if values[j] is None:
                    values[j] = sign * values[i]
                    queue.append(j)
                elif values[j] != sign * values[i]:
                    return False, components
    return True, components


graph_results = []
for n in range(2, 6):
    pairs = list(combinations(range(n), 2))
    assignments = list(product((-1, 1), repeat=n))
    checked = feasible = impossible = 0
    for labels in product((-1, 0, 1), repeat=len(pairs)):
        edges = [(i, j, label) for (i, j), label in zip(pairs, labels) if label]
        closed, components = cycle_check(n, edges)
        # Independent direct enumeration of every joint assignment.
        direct = sum(all(x[i] * x[j] == sign for i, j, sign in edges) for x in assignments)
        assert direct == (2**components if closed else 0)
        checked += 1
        feasible += bool(direct)
        impossible += not bool(direct)
    graph_results.append(dict(vertices=n, signed_graphs=checked,
                              realizable=feasible, nonrealizable=impossible))


parity_results = []
for n in range(2, 9):
    states = list(product((-1, 1), repeat=n))
    tau_values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    subset_checks = 0
    for tau in tau_values:
        def parity(x):
            answer = 1
            for value in x:
                answer *= value
            return answer
        distribution = {x: (1 + tau * parity(x)) / (2**n) for x in states}
        assert sum(distribution.values()) == 1
        assert min(distribution.values()) >= 0
        assert sum(p * parity(x) for x, p in distribution.items()) == tau
        for size in range(n):
            for indices in combinations(range(n), size):
                marginal = {}
                for x, probability in distribution.items():
                    key = tuple(x[i] for i in indices)
                    marginal[key] = marginal.get(key, F(0)) + probability
                assert set(marginal.values()) == {F(1, 2**size)}
                subset_checks += 1
        # Every nontrivial bipartition has uniform block marginals; their
        # product is the uniform law. Nonzero tau therefore cannot factorize.
        is_uniform = len(set(distribution.values())) == 1
        assert is_uniform == (tau == 0)
    parity_results.append(dict(variables=n, distributions=len(tau_values),
                               proper_subset_marginals_checked=subset_checks))


def marginal(distribution, indices):
    result = {}
    for state, probability in distribution.items():
        key = tuple(state[i] for i in indices)
        result[key] = result.get(key, F(0)) + probability
    return result


# Tree gluing check: a chain and a branching tree, both with four vertices.
# Generate known edge marginals with all rational transition probabilities
# in {0, 1/2, 1}; reconstruct solely from the overlapping edge/node tables.
# Cases include zero-probability parent states and deterministic edges.
tree_results = []
for name, parents in [('chain', [0, 1, 2]), ('branch', [0, 0, 0])]:
    checked = zero_rows = 0
    for values in product((F(0), F(1, 2), F(1)), repeat=7):
        root_one = values[0]
        transitions = [(values[1 + 2*i], values[2 + 2*i]) for i in range(3)]
        original = {}
        for state in product((0, 1), repeat=4):
            p = root_one if state[0] else 1-root_one
            for child, parent in enumerate(parents, start=1):
                one = transitions[child-1][state[parent]]
                p *= one if state[child] else 1-one
            original[state] = p
        nodes = [marginal(original, (i,)) for i in range(4)]
        edges = [marginal(original, (parent, child))
                 for child, parent in enumerate(parents, start=1)]
        recovered = {}
        for state in product((0, 1), repeat=4):
            p = nodes[0][(state[0],)]
            for child, parent in enumerate(parents, start=1):
                denominator = nodes[parent][(state[parent],)]
                if denominator:
                    conditional = edges[child-1][(state[parent], state[child])] / denominator
                else:
                    conditional = F(1, 2)  # Any probability row is allowed.
                p *= conditional
            recovered[state] = p
        assert sum(recovered.values()) == 1
        for child, parent in enumerate(parents, start=1):
            assert marginal(recovered, (parent, child)) == edges[child-1]
        assert recovered == original  # Generated laws already have tree factorization.
        zero_rows += any(probability == 0 for node in nodes for probability in node.values())
        checked += 1
    tree_results.append(dict(tree=name, cases=checked, cases_with_zero_node_probability=zero_rows))

output = {
    'status': 'all assertions passed',
    'scope': 'Exact rational constructed checks, not physical data or a proof of monism.',
    'cycle_consistency': graph_results,
    'parity_family': parity_results,
    'tree_gluing': tree_results,
}
destination = Path(__file__).with_name('composition-checks.json')
destination.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
