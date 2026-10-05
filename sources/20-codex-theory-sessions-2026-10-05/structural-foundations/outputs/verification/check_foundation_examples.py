"""Exact finite checks for formal-foundations.md; Python standard library only."""
from functools import lru_cache
import json
from pathlib import Path


def complete_traces(graph, initial):
    def paths(q, prefix):
        if not graph.get(q):
            return {prefix}
        return set().union(*(
            paths(q2, prefix + (a,))
            for a, successors in graph[q].items()
            for q2 in successors
        ))
    return sorted(''.join(t) for t in paths(initial, ()))


def full_information_can_force(graph, initial, target, horizon):
    @lru_cache(None)
    def win(q, remaining):
        if q in target:
            return True
        if remaining == 0:
            return False
        return any(
            bool(successors) and all(win(q2, remaining - 1) for q2 in successors)
            for successors in graph.get(q, {}).values()
        )
    return win(initial, horizon)


h = {'h0': {'a': {'h1'}}, 'h1': {'b': {'B'}, 'c': {'C'}}}
l = {'l0': {'a': {'lb', 'lc'}}, 'lb': {'b': {'B'}}, 'lc': {'c': {'C'}}}
ht = complete_traces(h, 'h0')
lt = complete_traces(l, 'l0')
hw = full_information_can_force(h, 'h0', {'B'}, 2)
lw = full_information_can_force(l, 'l0', {'B'}, 2)
assert ht == lt == ['ab', 'ac']
assert hw and not lw

# A fair bit is revealed, then the only permitted retained register is erased.
# No intermediate choices or other carriers are available to encode the bit.
# A current-information deterministic decoder is a constant; a perfect-recall
# decoder can select an action independently after each earlier signal.
current_scores = [sum(a == theta for theta in (0, 1)) / 2 for a in (0, 1)]
history_scores = [
    sum(actions[theta] == theta for theta in (0, 1)) / 2
    for actions in ((0, 0), (0, 1), (1, 0), (1, 1))
]
assert max(current_scores) == 0.5
assert max(history_scores) == 1.0

out = {
    'ordinary_trace_counterexample': {
        'abstract_complete_traces': ht,
        'concrete_complete_traces': lt,
        'abstract_can_force_b_in_two_steps': hw,
        'concrete_can_force_b_in_two_steps': lw,
        'check_uses_full_observation': True,
    },
    'memory_interface_counterexample': {
        'best_success_current_erased_information': max(current_scores),
        'best_success_perfect_recall': max(history_scores),
        'world_prior': [0.5, 0.5],
        'randomization_improves_current_score': False,
    },
    'shared_reserve_counterexample': {
        'reserve': 1,
        'cost_per_task': 1,
        'number_simultaneous_tasks': 2,
        'each_task_separately_feasible': True,
        'jointly_feasible': 2 <= 1,
    },
}
Path(__file__).with_name('foundation-example-results.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
