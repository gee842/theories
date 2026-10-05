"""Exact rational verification of the new four-site illustration.

All generator, eigenmode, projection, limiting-case, and irreducibility
checks use Fraction. Logarithmic window examples are explicitly numerical
illustrations of the analytically derived formula, not exact certificates.
"""
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path


def generator(k, eps):
    return [
        [-k-eps, k, eps/2, eps/2],
        [k, -k-eps, eps/2, eps/2],
        [eps/2, eps/2, -k-eps, k],
        [eps/2, eps/2, k, -k-eps],
    ]


def mv(A, x):
    return [sum(a*b for a, b in zip(row, x)) for row in A]


def mm(A, B):
    return [[sum(A[i][r]*B[r][j] for r in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def eq(x, y):
    assert x == y, (x, y)


def connected(G):
    seen = {0}
    while True:
        new = seen | {j for i in seen for j in range(4)
                      if i != j and G[j][i] > 0}
        if new == seen:
            return len(seen) == 4
        seen = new


Q = [[F(1, 2), F(1, 2), F(0), F(0)],
     [F(0), F(0), F(1, 2), F(1, 2)]]
modes = [[F(1)]*4, [F(1), F(1), F(-1), F(-1)],
         [F(1), F(-1), F(0), F(0)],
         [F(0), F(0), F(1), F(-1)]]
params = [F(0), F(1, 10), F(1, 2), F(1), F(2), F(10), F(100)]
rows = []
for k, eps in product(params, repeat=2):
    G = generator(k, eps)
    assert all(G[i][j] >= 0 for i in range(4) for j in range(4) if i != j)
    assert all(sum(G[i][j] for i in range(4)) == 0 for j in range(4))
    assert all(G[i][j] == G[j][i] for i in range(4) for j in range(4))
    rates = [F(0), 2*eps, 2*k+eps, 2*k+eps]
    for v, rate in zip(modes, rates):
        eq(mv(G, v), [-rate*u for u in v])
    coarse = [[-eps, eps], [eps, -eps]]
    eq(mm(Q, G), mm(coarse, Q))
    # Test derivatives of pair and internal contrasts as row functionals.
    for contrast, rate in zip(modes[1:], rates[1:]):
        eq(mm([contrast], G)[0], [-rate*u for u in contrast])
    eq(connected(G), eps > 0)
    if eps == 0:
        eq(mm(Q, G), [[F(0)]*4, [F(0)]*4])
    if k == eps/2:
        edges = [G[i][j] for i in range(4) for j in range(i+1, 4)]
        assert len(set(edges)) == 1
        eq(rates[1], rates[2])
    if eps > 0:
        eq(rates[1] < rates[2], k > eps/2)
        # Each alternative balanced pair partition is also an eigenmode,
        # but it decays at the internal rate, so closure alone is not unique.
        for alternative in [[F(1), F(-1), F(1), F(-1)],
                            [F(1), F(-1), F(-1), F(1)]]:
            eq(mv(G, alternative), [-(2*k+eps)*u for u in alternative])
    rows.append({'k': str(k), 'epsilon': str(eps),
                 'decay_rates': [str(r) for r in rates],
                 'connected': connected(G), 'all_edges_equal': k == eps/2,
                 'all_exact_checks_pass': True})

# Verify full mode decomposition with rational example states: the formulas
# reconstruct every tested state, so mode propagation gives a full solution.
states = list(product([F(0), F(1, 3), F(2)], repeat=4))
for x in states:
    g = sum(x)/4
    d = (x[0]+x[1]-x[2]-x[3])/4
    u = (x[0]-x[1])/2
    v = (x[2]-x[3])/2
    eq([g+d+u, g+d-u, g-d+v, g-d-v], list(x))


def window(k, eps, delta):
    fast = 2*k+eps
    lower = math.log(1/delta)/fast if fast > 0 else None
    upper = -math.log(1-delta)/(2*eps) if eps > 0 else None
    feasible = lower is not None and (upper is None or lower <= upper)
    middle = ((lower+upper)/2 if feasible and upper is not None
              else lower if feasible else None)
    record = {'k': k, 'epsilon': eps, 'relative_tolerance': delta,
              'lower_time': lower, 'upper_time': upper,
              'nonempty_window': feasible, 'chosen_time': middle,
              'numeric_not_exact': True}
    if middle is not None:
        record['internal_remaining_fraction'] = math.exp(-fast*middle)
        record['pair_contrast_remaining_fraction'] = math.exp(-2*eps*middle)
        assert record['internal_remaining_fraction'] <= delta*(1+1e-12)
        assert record['pair_contrast_remaining_fraction'] >= (1-delta)*(1-1e-12)
    return record


windows = [window(100, 1, .05), window(1, 0, .05),
           window(0, 1, .05), window(.5, 1, .05),
           window(0, 0, .05)]
result = {
    'status': 'passed',
    'scope': 'New constructed mathematical example; no empirical experiment.',
    'rational_parameter_pairs': len(rows),
    'rational_states_reconstructed': len(states),
    'exact_properties': [
        'nonnegative off-diagonal generator entries', 'mass conservation',
        'symmetric generator', 'four independent eigenmodes with claimed rates',
        'exact two-dimensional pair-mean closure',
        'exact pair-contrast and internal-difference derivative identities',
        'connected precisely when epsilon is positive',
        'zero-coupling conservation of each pair mean',
        'all-six-equal edge degeneracy at k=epsilon/2',
        'simple slowest nonconstant mode exactly when k>epsilon/2 for epsilon>0',
        'alternative balanced pair partitions relax at the faster rate when k>epsilon/2',
        'full mode reconstruction on 81 rational states',
    ],
    'parameter_checks': rows,
    'time_window_examples': windows,
    'qualifiers': [
        'The coupling matrix is supplied; its historical formation is not derived.',
        'The zero generator has no relaxation; already coherent preparations are special cases.',
        'Nonzero initial pair contrast or a preparation exciting it is needed to observe its retention.',
        'A time-scale separation warrants this approximation; it does not prove a unique ontology.',
        'The pair labels are not uniquely favored at equal six-edge rates.',
        'Invariance under all unrestricted changes of basis is not claimed.',
    ],
}
path = Path(__file__).with_name('pair-emergence-checks.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: result[k] for k in ['status', 'rational_parameter_pairs',
                                       'rational_states_reconstructed']}, indent=2))
