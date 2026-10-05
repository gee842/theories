"""Exact finite-token check of supplied catalytic cascade; no empirical claims."""
import json
from collections import deque
from pathlib import Path

NAMES = ('A', 'B', 'C', 'D', 'F', 'G', 'H', 'W')
# catalyst, feed, product indices. Reactions preserve catalyst and unit mass.
REACTIONS = ((0, 4, 1), (1, 5, 2), (2, 6, 3))
INITIAL = (1, 0, 0, 0, 1, 1, 1, 0)

def reach(initial, blocked=(), remove_b=False):
    seen, queue = {initial}, deque([initial])
    transitions = []
    while queue:
        state = queue.popleft()
        for reaction, (catalyst, feed, product) in enumerate(REACTIONS):
            if reaction in blocked or not state[catalyst] or not state[feed]:
                continue
            nxt = list(state)
            nxt[feed] -= 1
            nxt[product] += 1
            if remove_b and reaction == 0:
                nxt[7] += nxt[1]
                nxt[1] = 0
            nxt = tuple(nxt)
            assert sum(nxt) == sum(state)
            assert all(v >= 0 for v in nxt)
            assert sum(nxt[4:7]) == sum(state[4:7]) - 1
            transitions.append((state, reaction + 1, nxt))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen), transitions

def described(states):
    return [dict(zip(NAMES, state)) for state in states]

scenarios = {}
for name, initial, blocked, remove_b in [
    ('intact', INITIAL, (), False),
    ('remove_B_after_formation', INITIAL, (), True),
    ('isolate_B_from_G', INITIAL, (1,), False),
    ('missing_G', (1,0,0,0,1,0,1,0), (), False),
    ('isolate_C_from_H', INITIAL, (2,), False),
]:
    states, transitions = reach(initial, blocked, remove_b)
    scenarios[name] = {'states': described(states),
                       'transition_count': len(transitions),
                       'C_reachable': any(s[2] for s in states),
                       'D_reachable': any(s[3] for s in states)}

assert scenarios['intact']['C_reachable']
assert scenarios['intact']['D_reachable']
assert len(scenarios['intact']['states']) == 4
for name in ('remove_B_after_formation', 'isolate_B_from_G', 'missing_G'):
    assert not scenarios[name]['C_reachable']
    assert not scenarios[name]['D_reachable']
assert scenarios['isolate_C_from_H']['C_reachable']
assert not scenarios['isolate_C_from_H']['D_reachable']

# Verify mass and strict feed decrease at every edge for all small inventories.
inventories = 0
edge_checks = 0
for a in range(3):
    for f in range(3):
        for g in range(3):
            for h in range(3):
                states, transitions = reach((a,0,0,0,f,g,h,0))
                inventories += 1
                edge_checks += len(transitions)
                for state in states:
                    made = state[1] + state[2] + state[3]
                    assert made == f + g + h - sum(state[4:7])
                    assert made <= f + g + h

result = {
    'status': 'all_exact_checks_passed',
    'scope': 'Supplied discrete unit-mass reaction system; not an energy balance or physical experiment.',
    'scenarios': scenarios,
    'exhaustion_checks': {'initial_inventories': inventories,
                          'conserved_mass_and_decreasing_feed_edges': edge_checks},
    'continuous_derivatives': 'Analytic Taylor calculation in mechanism.md; not numerically inferred.',
}
destination = Path(__file__).with_name('cascade-checks.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'inventories': inventories, 'edges': edge_checks}))
