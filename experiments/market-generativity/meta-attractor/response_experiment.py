#!/usr/bin/env python3
"""Independent finite arithmetic checks; no empirical or proof-substitute claim."""
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def support_trace(initial, repairs, losses):
    states = [max(0, initial)]
    for repair, loss in zip(repairs, losses):
        states.append(max(0, states[-1]+repair-loss) if states[-1] > 0 else 0)
    return states


def step(demand, investment, state):
    response, support = state
    if support == 0:
        return state
    assert investment <= support, 'Only affordable actions in this experiment'
    handled = min(demand, response)
    missed = demand-handled
    # Independent decomposition into responded/unresponded operations.
    assert handled+missed == demand
    assert handled <= response
    return (max(0, response+2*investment-missed),
            max(0, support+handled-missed-investment))


def trace(demand, initial, policy, rounds):
    rows = [initial]
    for t in range(rounds):
        rows.append(step(demand, policy(t, rows[-1]), rows[-1]))
    return rows


def main():
    prefix_cases = 0
    for events in product(tuple(product(range(3), repeat=2)), repeat=4):
        repairs, losses = zip(*events)
        for initial in range(5):
            rows = support_trace(initial, repairs, losses)
            for t in range(5):
                prefix_safe = all(initial+sum(repairs[:j])-sum(losses[:j]) > 0
                                  for j in range(t+1))
                assert (rows[t] > 0) == prefix_safe
            prefix_cases += 1
    viability_cases = recovery_cases = greedy_cases = optimal_live_cases = 0
    for demand, response, support in product(range(13), range(13), range(21)):
        state = (response, support)
        horizon = response+support+response*response+1
        rows = trace(demand, state, lambda t, s: 0, horizon)
        viable = all(v > 0 for _, v in rows)
        assert viable == (support > 0 and demand <= response)
        viability_cases += 1
        for investment in range(support+1):
            new = step(demand, investment, state)
            optimum = step(demand, 0, state)[1]
            assert new[1] <= optimum
            if new[1] == optimum and new[1] > 0:
                assert investment == 0
                optimal_live_cases += 1
            greedy_cases += 1
        if support > 0 and response < demand:
            feasible = any(step(demand, i, state)[0] >= demand and step(demand, i, state)[1] > 0
                           for i in range(support+1))
            gap = demand-response
            assert feasible == (gap <= support and 2*gap < support+response)
            recovery_cases += 1
    examples = {
        'constant_demand_greedy': trace(3, (2,2), lambda t, s: 0, 6),
        'one_initial_investment': trace(3, (2,2), lambda t, s: 1 if t == 0 else 0, 6),
        'reduced_demand': trace(2, (2,2), lambda t, s: 0, 6),
        'greater_response_and_demands': trace(5, (4,2), lambda t, s: 0, 6),
    }
    doubling = [{'time': t, 'demand': 2**t, 'response': t+1,
                 'unmet': max(0, 2**t-(t+1))} for t in range(7)]
    doubling_support = support_trace(10, [0]*7, [row['unmet'] for row in doubling])
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'formal_source_sha256': hashlib.sha256((HERE/'ResponseCapacity.lean').read_bytes()).hexdigest(),
        'prefix_history_cases': prefix_cases, 'viability_cases': viability_cases,
        'affordable_action_comparisons': greedy_cases, 'one_step_recovery_cases': recovery_cases,
        'optimal_live_step_cases': optimal_live_cases,
        'example_columns': ['effective_response', 'operative_support'], 'examples': examples,
        'doubling_load_events': doubling, 'doubling_load_support': doubling_support,
        'scope': 'Finite independent arithmetic and policy checks of the declared models, plus illustrative trajectories. Not empirical data or a substitute for the Lean universal claims.'
    }
    (HERE/'response-experiment.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k.endswith('_cases') or k in ['status','affordable_action_comparisons']}))


if __name__ == '__main__':
    main()
