#!/usr/bin/env python3
"""Finite trajectory exploration; this is not a substitute for Lean proof.

Enumerates represented initial stock vectors in four explicitly fixed networks.
Cycle catalogues are exploratory implementation outputs. Only the statements
named in ReproductionNetwork.lean have the accompanying formal proof scope.
"""
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPLIT = {(0,1),(1,0),(2,3),(3,2)}
NETWORKS = {'separate':SPLIT, 'bridge':SPLIT|{(1,2)},
            'ring':{(0,1),(1,2),(2,3),(3,0)}, 'broken':set()}


def step(stock, edges):
    return tuple(min(3, max(0, stock[j]-1)+sum(
        2 for i in range(4) if (i,j) in edges and stock[i]>=2)) for j in range(4))


def main():
    outputs = {}
    for name, edges in NETWORKS.items():
        cycles = Counter()
        longest_prefix = 0
        for seed in product(range(4), repeat=4):
            seen, history, state = {}, [], seed
            while state not in seen:
                assert all(0 <= x <= 3 for x in state)
                seen[state] = len(history)
                history.append(state)
                state = step(state, edges)
            longest_prefix = max(longest_prefix, seen[state])
            cycle = history[seen[state]:]
            key = min(tuple(cycle[i:]+cycle[:i]) for i in range(len(cycle)))
            cycles[key] += 1
        example = [(3,3,0,0)]
        for _ in range(6):
            example.append(step(example[-1], edges))
        outputs[name] = {'initial_vectors':256, 'longest_observed_prefix':longest_prefix,
                         'example_history':example,
                         'cycles':[{'states':cycle,'initial_vectors':count}
                                   for cycle,count in sorted(cycles.items())]}
    result = {'status':'completed', 'scope':'Exploratory finite trajectory outputs, not additional Lean theorems',
              'initial_vector_network_pairs':1024,
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'lean_source_sha256':hashlib.sha256((HERE/'ReproductionNetwork.lean').read_bytes()).hexdigest(),
              'networks':outputs}
    (HERE/'reproduction-exploration.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':'completed', 'initial_vector_network_pairs':1024,
                      'scope':result['scope']}))


if __name__ == '__main__':
    main()
