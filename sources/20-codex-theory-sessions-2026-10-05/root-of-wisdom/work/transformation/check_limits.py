"""Exact checks of the finite partially observed safety fixed point.

Original finite verification; no external package or stochastic simulation.
Unavailable actions are represented by transition to the absorbing failure state.
"""
from itertools import product
import json
from pathlib import Path


def coherent_beliefs(safe, observation):
    xs = tuple(sorted(safe))
    return {frozenset(xs[i] for i in range(len(xs)) if mask >> i & 1)
            for mask in range(1, 1 << len(xs))
            if len({observation[xs[i]] for i in range(len(xs))
                    if mask >> i & 1}) == 1}


def successors(belief, action, transition, observation, safe):
    post = set().union(*(transition[x, action] for x in belief))
    if not post <= safe:
        return None
    return {frozenset(x for x in post if observation[x] == o)
            for o in {observation[x] for x in post}}


def kernel(safe, actions, transition, observation):
    current = coherent_beliefs(safe, observation)
    rounds = 0
    while True:
        nxt = {b for b in current
               if any((ss := successors(b, a, transition, observation, safe))
                      is not None and ss <= current for a in actions)}
        if nxt == current:
            return current, rounds
        current = nxt
        rounds += 1


def brute_stationary(safe, actions, transition, observation):
    beliefs = sorted(coherent_beliefs(safe, observation),
                     key=lambda b: (len(b), tuple(sorted(b))))
    winning = set()
    policies = 0
    for choices in product(actions, repeat=len(beliefs)):
        policy = dict(zip(beliefs, choices))
        policies += 1
        for start in beliefs:
            reached, todo, fails = set(), [start], False
            while todo:
                b = todo.pop()
                if b in reached:
                    continue
                reached.add(b)
                ss = successors(b, policy[b], transition, observation, safe)
                if ss is None:
                    fails = True
                    break
                todo.extend(ss - reached)
            if not fails:
                winning.add(start)
    return winning, policies


def main():
    safe, actions = {0, 1}, (0, 1)
    systems = policy_count = 0
    max_rounds = 0
    for images in product(range(3), repeat=4):
        transition = {(x, a): {images[2*x+a]} for x in safe for a in actions}
        for separated in (False, True):
            observation = {0: 0, 1: int(separated), 2: 2}
            fixed, rounds = kernel(safe, actions, transition, observation)
            brute, count = brute_stationary(safe, actions, transition, observation)
            assert fixed == brute
            systems += 1
            policy_count += count
            max_rounds = max(max_rounds, rounds)

    # Full information permits safety at each individual state, whereas an
    # aliased observation does not allow the required opposite responses.
    opposite = {(0, 0): {0}, (0, 1): {2},
                (1, 0): {2}, (1, 1): {1}}
    aliased = {0: 0, 1: 0, 2: 2}
    full = {0: 0, 1: 1, 2: 2}
    ka, _ = kernel(safe, actions, opposite, aliased)
    kf, _ = kernel(safe, actions, opposite, full)
    assert frozenset({0, 1}) not in ka
    assert frozenset({0}) in kf and frozenset({1}) in kf

    # A safe probe creates a useful observation; prohibit or endanger it and
    # the same initial uncertainty is no longer viable.
    # 0/1: pre-probe worlds, 2/3: revealed worlds, 4: operating sink, 5: failure.
    sp = set(range(5)); ap = (0, 1, 2)
    obs = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    tr = {(x, a): {5} for x in sp for a in ap}
    tr.update({(0, 2): {2}, (1, 2): {3},
               (0, 0): {4}, (1, 1): {4},
               (2, 0): {4}, (3, 1): {4}})
    tr.update({(4, a): {4} for a in ap})
    start = frozenset({0, 1})
    assert start in kernel(sp, ap, tr, obs)[0]
    assert start not in kernel(sp, (0, 1), tr, obs)[0]
    risky = dict(tr); risky[1, 2] = {5}
    assert start not in kernel(sp, ap, risky, obs)[0]

    # Nonempty immediate safe actions at every belief are insufficient: one
    # transition can lead to a safe-looking state whose every action fails.
    doomed = {(0, a): {1} for a in actions}
    doomed.update({(1, a): {2} for a in actions})
    assert successors(frozenset({0}), 0, doomed, full, safe) is not None
    assert kernel(safe, actions, doomed, full)[0] == set()

    # Every action history is considered, with processing assumed perfect
    # whenever the installed type is present (a stronger oracle controller).
    # A stage-1 rebuild has one remaining no-harvest tick and then swaps type.
    # Either initial type is allowed; time 0 begins an A-only phase.
    possible = {(q, 0, 3) for q in (0, 1)}
    first_impossible_tick = None
    reachable_sizes = [len(possible)]
    for tick in range(21):
        mode = (tick // 3) % 2
        after = set()
        for q, rebuilding, reserve in possible:
            if rebuilding:
                if reserve - 1 >= 1:
                    after.add((1-q, 0, reserve-1))
            else:
                # Harvest, including the always-unhelpful absent-input case.
                r_next = min(3, reserve+1) if q == mode else reserve-1
                if r_next >= 1:
                    after.add((q, 0, r_next))
                # Starting a rebuild supplies no harvest.
                if reserve-1 >= 1:
                    after.add((q, 1, reserve-1))
                # Waiting has the same reserve effect as absent harvesting.
                if reserve-1 >= 1:
                    after.add((q, 0, reserve-1))
        possible = after
        reachable_sizes.append(len(possible))
        if not possible:
            first_impossible_tick = tick+1
            break
    assert first_impossible_tick == 14

    result = {
        "exhaustive_deterministic_systems": systems,
        "stationary_belief_policies_checked": policy_count,
        "maximum_elimination_rounds_in_exhaustive_family": max_rounds,
        "exhaustive_fixed_point_matches_brute_force": True,
        "opposite_actions_information_counterexample": True,
        "safe_probe_restores_viability": True,
        "unavailable_or_risky_probe_does_not_restore_viability": True,
        "immediate_safety_is_not_infinite_viability": True,
        "capacity_3_alternating_3_tick_phases": {
            "all_action_histories_considered": True,
            "oracle_processing_on_present_input": True,
            "both_initial_types_considered": True,
            "first_tick_with_no_surviving_history": first_impossible_tick,
            "reachable_state_counts": reachable_sizes,
            "analytical_nonsharp_failure_bound_ticks": 21
        },
        "scope": "Two safe states, two actions, one absorbing failure state; all deterministic transitions and both observation partitions. Three illustrative larger/counterexample systems checked separately. General theorem is proved in limits-audit.md."
    }
    path = Path(__file__).with_name("limits-checks.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
