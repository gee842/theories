"""Finite checks for formal-core.md; standard library only, no empirical claims."""
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path


def subsets(xs):
    xs = tuple(xs)
    return [frozenset(s) for k in range(1, len(xs)+1) for s in combinations(xs, k)]


def winning(F, h, K, actions):
    @lru_cache(None)
    def W(B, horizon):
        if not B or not B <= K:
            return False
        if horizon == 0:
            return True
        for u in actions:
            succ = frozenset(z for x in B for z in F(x, u))
            branches = [frozenset(z for z in succ if h(z) == y) for y in {h(z) for z in succ}]
            if branches and all(W(b, horizon-1) for b in branches):
                return True
        return False
    return W


actions = ("consume", "charge")
X = tuple((e, c) for e in range(4) for c in range(2))
Z = tuple(range(4))


def concrete(x, u):
    e, c = x
    if e == 0:
        return {(0, c)}
    if u == "consume":
        return {(e-1, c)}
    return {((e+1) % 4, 1-c)}


def abstract(z, u):
    if z == 0:
        return {0}
    return {z-1 if u == "consume" else (z+1) % 4}


q = lambda x: x[0]
h = lambda x: int(x[0] > 0)
hb = lambda z: int(z > 0)
K = frozenset(x for x in X if x[0] > 0)
Kb = frozenset((1, 2, 3))
hom = [(x, u) for x in X for u in actions if {q(z) for z in concrete(x, u)} != abstract(q(x), u)]
assert not hom
W = winning(concrete, h, K, actions)
Wb = winning(abstract, hb, Kb, actions)
Bs = [b for b in subsets(X) if len({h(x) for x in b}) == 1]
checked = 0
for B in Bs:
    for n in range(6):
        assert W(B, n) == Wb(frozenset(map(q, B)), n), (B, n)
        checked += 1
assert Wb(frozenset((1, 2)), 5)
assert Wb(frozenset((2, 3)), 5)
assert not Wb(frozenset((1, 3)), 1)

# Individually viable hidden states, no common safe action.
fault_table = {
    ("L", "L"): {"L"}, ("L", "R"): {"dead"},
    ("R", "L"): {"dead"}, ("R", "R"): {"R"},
    ("dead", "L"): {"dead"}, ("dead", "R"): {"dead"},
}
wf = winning(lambda x, u: fault_table[x, u], lambda x: int(x != "dead"), frozenset(("L", "R")), ("L", "R"))
assert wf(frozenset(("L",)), 5) and wf(frozenset(("R",)), 5)
assert not wf(frozenset(("L", "R")), 1)

# First-order Markov compression fails: same present output, different past.
cycle = {"a": "b", "b": "c", "c": "a"}
obs = {"a": 0, "b": 0, "c": 1}
paths = [(obs[x], obs[cycle[x]], obs[cycle[cycle[x]]]) for x in cycle]
assert (1, 0, 0) in paths and (0, 0, 1) in paths

# Exact transitions do not imply exact safety labels. An optimistic abstract
# label certifies a concrete unsafe initial state, despite full commutation.
health_states = ("healthy", "harmed")
health_F = lambda x, u: {x}
health_q = lambda x: "same"
health_Fbar = lambda z, u: {"same"}
assert all({health_q(y) for y in health_F(x, "stay")} == health_Fbar(health_q(x), "stay") for x in health_states)
health_W = winning(health_F, lambda x: "same", frozenset(("healthy",)), ("stay",))
health_Wbar = winning(health_Fbar, lambda x: "same", frozenset(("same",)), ("stay",))
assert health_Wbar(frozenset(("same",)), 5)
assert not health_W(frozenset(("harmed",)), 5)
assert not health_W(frozenset(health_states), 5)
possible_lifts = [frozenset(), frozenset(health_states)]
assert frozenset(("healthy",)) not in possible_lifts

results = {
    "status": "passed",
    "exact_quotient_transition_checks": len(X)*len(actions),
    "observation_homogeneous_information_sets": len(Bs),
    "exact_safety_equivalences_checked_horizons_0_through_5": checked,
    "abstract_beliefs_1_2_and_2_3_viable_through_5": True,
    "abstract_belief_1_3_not_viable_for_1": True,
    "hidden_fault_individual_viability_but_no_joint_safe_action": True,
    "cycle_observation_triples": paths,
    "exact_dynamics_unsafe_health_quotient_falsely_certifies_safety": True,
    "meaning": "Exact finite toy checks, not empirical validation or a proof for all model classes.",
}
out = Path(__file__).with_name("formal_checks.json")
out.write_text(json.dumps(results, indent=2)+"\n")
print(json.dumps(results, indent=2))
