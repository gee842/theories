"""Exact finite checks of the root-foundation examples, not empirical validation.

Run with Python 3 standard library. Exhaustive checks exercise finite graph
consequences and decision rules; they do not certify the general proofs.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


checks = []


def check(name, condition, detail):
    assert condition, name
    checks.append({"name": name, "passed": True, "detail": detail})


def lifetime_bound(n, edges, lifetimes):
    incoming = [{a for a, b in edges if b == i} for i in range(n)]
    done, deadlines = set(), {}
    while len(done) < n:
        ready = [i for i in range(n) if i not in done and incoming[i] <= done]
        if not ready:
            return None
        for i in ready:
            deadlines[i] = lifetimes[i] + max([0] + [deadlines[j] for j in incoming[i]])
        done.update(ready)
    return deadlines


def path_bound(n, edges, lifetimes):
    outgoing = [{b for a, b in edges if a == i} for i in range(n)]

    def walk(i, seen):
        assert i not in seen
        return lifetimes[i] + max([0] + [walk(j, seen | {i}) for j in outgoing[i]])

    return max(walk(i, set()) for i in range(n))


def reachable(start, n, edges):
    seen = set(start)
    while True:
        expanded = seen | {b for a, b in edges if a in seen}
        if expanded == seen:
            return seen
        seen = expanded


# Exhaust every directed graph without self-loops on four labeled nodes.
n = 4
possible = [(a, b) for a in range(n) for b in range(n) if a != b]
dag_count = 0
for bits in product((0, 1), repeat=len(possible)):
    edges = {e for e, enabled in zip(possible, bits) if enabled}
    deadlines = lifetime_bound(n, edges, [1, 2, 3, 4])
    if deadlines is not None:
        dag_count += 1
        assert max(deadlines.values()) == path_bound(n, edges, [1, 2, 3, 4])
        assert max(deadlines.values()) <= 10
check("all_four_node_acyclic_lifetime_bounds", dag_count == 543,
      {"graphs_enumerated": 4096, "acyclic_graphs": dag_count,
       "independent_longest_path_agreements": dag_count})
d = lifetime_bound(3, {(0, 1), (1, 2)}, [2, 3, 5])
check("ten_time_unit_lifetime_witness", d == {0: 2, 1: 5, 2: 10}, d)
check("cycle_not_treated_as_acyclic", lifetime_bound(2, {(0, 1), (1, 0)}, [2, 2]) is None,
      "A cyclic routing graph has no topological lifetime deadline from this theorem.")

# Graph consequence of recurrent inflow, including self-loops and outside inputs.
n = 3
possible = list(product(range(n), repeat=2))
qualifying = 0
for bits in product((0, 1), repeat=len(possible)):
    edges = {e for e, enabled in zip(possible, bits) if enabled}
    cycle_nodes = {i for i in range(n)
                   if any(b == i and a in reachable({i}, n, edges) for a, b in edges)}
    for ext_bits in product((0, 1), repeat=n):
        external = {i for i, enabled in enumerate(ext_bits) if enabled}
        if all(i in external or any(b == i for a, b in edges) for i in range(n)):
            qualifying += 1
            assert reachable(external | cycle_nodes, n, edges) == set(range(n))
check("recurrent_ancestry_all_three_node_graphs", qualifying == 3375,
      {"graph_and_boundary_configurations": 4096, "qualifying_configurations": qualifying})
edges = {(0, 1), (1, 0), (1, 2)}
check("downstream_support_need_not_be_on_cycle",
      reachable({0, 1}, 3, edges) == {0, 1, 2} and reachable({2}, 3, edges) == {2},
      "The 0↔1→2 witness prevents an inference of full mutual closure.")


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


B = [[F(0), F(1, 2)], [F(1, 2), F(0)]]
IminusB = [[F(1), F(-1, 2)], [F(-1, 2), F(1)]]
inverse = [[F(4, 3), F(2, 3)], [F(2, 3), F(4, 3)]]
check("spectral_inverse_exact", mm(IminusB, inverse) == [[1, 0], [0, 1]],
      "The nonnegative inverse (I−B)^−1 equals [[4/3,2/3],[2/3,4/3]].")
check("two_cycle_radius_one_half", mm(B, B) == [[F(1, 4), 0], [0, F(1, 4)]],
      "Eigenvalues are ±1/2 despite the existence of a routing cycle.")
D = [[F(2), 0], [0, F(3)]]
Dinv = [[F(1, 2), 0], [0, F(1, 3)]]
Bprime = mm(mm(D, B), Dinv)
check("service_unit_similarity", mm(Bprime, Bprime) == [[F(1, 4), 0], [0, F(1, 4)]],
      "Changing service units by diag(2,3) preserves the spectrum.")


def risk(p0, p1, decoder):
    return sum(p0[i] * decoder[i] + p1[i] * (1 - decoder[i]) for i in range(3)) / 2


def tv(p0, p1):
    return sum(abs(a - b) for a, b in zip(p0, p1)) / 2


decoders = list(product((F(0), F(1)), repeat=3))
distributions = [[F(a, 4), F(b, 4), F(4-a-b, 4)]
                 for a in range(5) for b in range(5-a)]
for p0, p1 in product(distributions, repeat=2):
    assert min(risk(p0, p1, d) for d in decoders) == (1-tv(p0, p1))/2
check("finite_binary_testing_bound", len(distributions) == 15,
      {"channel_pairs": 225, "deterministic_decoders_per_pair": 8,
       "justification_for_randomized_rules": "Risk is affine; deterministic vertices attain its minimum."})
for c in [F(i, 10) for i in range(11)] + [F(24, 29)]:
    p0, p1 = [c, F(0), 1-c], [F(0), c, 1-c]
    assert min(risk(p0, p1, d) for d in decoders) == (1-c)/2
    randomized = [F(0), F(1), F(1, 2)]
    assert sum(p0[i]*randomized[i] for i in range(3)) == (1-c)/2
    assert sum(p1[i]*(1-randomized[i]) for i in range(3)) == (1-c)/2
check("erasure_channel_average_and_worst_case", True,
      {"reliability_values": 12, "randomized_erasure_decision": "fair coin"})

alpha, delta, s, q = F(6), F(1), F(4), F(1)
umax = 1-q/s
eps = F(1, 10)
cstar = 1-2*eps
umin = delta*cstar/(alpha*(1-cstar))
check("feasible_allocation_interval", (umin, umax) == (F(2, 3), F(3, 4)),
      "At error 1/10, all constant allocations from 2/3 to 3/4 suffice.")
epsmin = delta/(2*(alpha*umax+delta))
check("minimum_sustainable_error", epsmin == F(1, 11), str(epsmin))
check("accuracy_optimum_is_attained", alpha*umax/(alpha*umax+delta) == 1-2*epsmin,
      "At u=3/4, b is constant and reliability equilibrium is 9/11.")
for numerator in range(1, 50):
    e = F(numerator, 100)
    c = 1-2*e
    required = delta*c/(alpha*(1-c))
    assert (required <= umax) == (e >= epsmin)
check("accuracy_feasibility_classification", True, {"rational_tolerances_checked": 49})

strict_eps = F(5, 58)
strict_c = 1-2*strict_eps
strict_u = delta*strict_c/(alpha*(1-strict_c))
gap = strict_u-umax
deadline = (F(1)/s)/gap
check("strict_accuracy_witness", (strict_c, strict_u) == (F(24, 29), F(4, 5)),
      {"required_reliability": str(strict_c), "required_effort": str(strict_u)})
check("sharp_deadline", deadline == 5, str(deadline))
check("deadline_attained_exactly", alpha*strict_u*(1-strict_c)-delta*strict_c == 0
      and F(1)+(s*(1-strict_u)-q)*deadline == 0,
      "c remains at 24/29 and b(t)=1−t/5. The boundary is allowed at t=5.")
exp7_lower = F(1)+7+F(49,2)
check("scheduled_accuracy_counterexample_exact", exp7_lower > 29
      and F(6,7)*(1-F(1,29)) == strict_c and F(6,7) > strict_c,
      "e^7>1+7+49/2>29 implies every full-maintenance endpoint exceeds 24/29. "
      "The first endpoint rises from c*, and all later ones exceed (6/7)(1−e^−7).")
check("scheduled_execution_counterexample_exact", -q == -1 and s-q == 3
      and -q+(s-q) == 2 and F(6,7)/2 < strict_c,
      "One maintenance interval spends1, the next gains3. e>2 implies the "
      "off-interval reliability is below3/7<c*. Assessments pass while continuous readiness fails.")
check("marginal_risk_not_conditional_guarantee", F(9,10)*0+F(1,10)*F(1,2) == F(1,20)
      and F(1,20) <= F(1,10) and F(0) < F(4,5),
      "A 90% perfect/10% erased channel mixture has marginal error .05, "
      "but its erased-history conditional error .5 violates a .1 guarantee.")
for c, u in product([F(i, 20) for i in range(16, 20)], [F(i, 10) for i in range(11)]):
    cdot = alpha*u*(1-c)-delta*c
    bdot = s*(1-u)-q
    derivative = bdot/s + cdot/(alpha*(1-c))
    assert derivative == umax-delta*c/(alpha*(1-c))
    assert derivative <= umax-umin
check("control_cancels_from_reserve_derivative", True,
      {"exact_state_effort_pairs": 44, "scope": "Finite witnesses of the displayed symbolic identity."})

table = []
for u in [F(1, 2), F(7, 10), F(9, 10)]:
    cinf = alpha*u/(alpha*u+delta)
    table.append((cinf, (1-cinf)/2, s*(1-u)-q))
check("three_allocation_tradeoffs", table == [(F(3, 4),F(1, 8),F(1)),
      (F(21, 26),F(5, 52),F(1, 5)), (F(27, 32),F(5, 64),F(-3, 5))],
      [[str(v) for v in row] for row in table])


def selection_rhs(c, x):
    u = F(1, 2)+x/5
    return alpha*u*(1-c)-c, x*(1-x)*(5*c-4)


equilibria = [(F(3, 4), F(0)), (F(21, 26), F(1)), (F(4, 5), F(5, 6))]
check("selection_equilibria", all(selection_rhs(c, x) == (0,0) for c,x in equilibria),
      [[str(c),str(x)] for c,x in equilibria])
low_eigenvalues = (-4, 5*F(3,4)-4)
high_eigenvalues = (-F(26,5), -(5*F(21,26)-4))
check("stable_boundary_equilibria", low_eigenvalues == (-4,F(-1,4))
      and high_eigenvalues == (F(-26,5),F(-1,26)),
      {"low_eigenvalues": list(map(str,low_eigenvalues)),
       "high_eigenvalues": list(map(str,high_eigenvalues))})
J = [[F(-5),F(6,25)],[F(25,36),F(0)]]
check("interior_saddle", J[0][0]*J[1][1]-J[0][1]*J[1][0] == F(-1,6),
      "Jacobian determinant −1/6 gives eigenvalues of opposite signs.")
for c in [F(i,100) for i in range(101)]:
    assert (selection_rhs(c,F(5,6))[1] <= 0) == (c <= F(4,5))
for x in [F(i,100) for i in range(101)]:
    assert (selection_rhs(F(4,5),x)[0] <= 0) == (x <= F(5,6))
check("selection_rectangle_boundary_signs", True,
      {"rational_boundary_points": 202, "scope": "Signs support the analytic invariant-region proof."})
check("execution_reserve_grows_in_selection_witness", s*(1-F(7,10))-q == F(1,5),
      "ḃ≥1/5 for all x∈[0,1], so (c,x) attractors are not full-state fixed points.")

# Equal outcome capability sets need not preserve fixed action meanings.
grid = [F(i,10) for i in range(11)]
check("capability_not_labeled_causality", set(grid) == {1-p for p in grid} and F(0) != F(1),
      "M: Z=a, N: Z=1−a. Relabeling randomized choices preserves achievable outcome laws; "
      "the physical action a=0 still has opposite effects.")

result = {
    "status": "passed",
    "date": "2026-10-05",
    "check_groups": len(checks),
    "method": "Python standard-library rational arithmetic and exhaustive finite enumeration",
    "scope": "Constructed mathematical examples; no empirical data, no proof assistant, no general proof certification.",
    "checks": checks,
}
output = Path(__file__).with_name("EXACT-CHECKS.json")
output.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
print(json.dumps({"status": result["status"], "check_groups": len(checks), "output": str(output)}, indent=2))
