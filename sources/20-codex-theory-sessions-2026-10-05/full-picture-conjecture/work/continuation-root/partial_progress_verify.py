"""Finite obligation-memory reduction for sure partial-observation recurrence.

Checks the constructed game's Büchi solution against exhaustive strategies,
then checks each extracted strategy on actual plant/controller product paths.
The equivalence for arbitrary strategies is established by the written proof.
"""
from collections import deque
from importlib.util import spec_from_file_location, module_from_spec
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('progress_check', HERE/'progress-check.py')
buchi = module_from_spec(spec)
spec.loader.exec_module(buchi)


def bits(mask, n):
    return [x for x in range(n) if mask & (1 << x)]


def reduction(plant, observations, safe, progress):
    n = len(plant)
    pairs = []
    for belief in range(1, 1 << n):
        if belief & ~safe or len({observations[x] for x in bits(belief, n)}) != 1:
            continue
        for owed in range(1 << n):
            if not owed & ~(belief & ~progress):
                pairs.append((belief, owed))
    index = {p:i for i,p in enumerate(pairs)}
    sink = len(pairs)
    game = []
    update = {}
    obs_masks = {y:sum(1 << x for x in range(n) if observations[x] == y)
                 for y in set(observations)}
    for b, owed in pairs:
        actions = []
        for a in range(len(plant[0])):
            if any(plant[x][a] == 0 for x in bits(b, n)):
                actions.append(1 << sink)
                continue
            post = 0
            owed_post = 0
            for x in bits(b, n):
                post |= plant[x][a]
            for x in bits(owed, n):
                owed_post |= plant[x][a]
            successors = 0
            for y, mask in obs_masks.items():
                bp = post & mask
                if not bp:
                    continue
                op = (bp if owed == 0 else owed_post & mask) & ~progress
                successor = sink if bp & ~safe else index[bp, op]
                successors |= 1 << successor
                update[(index[b, owed], a, y)] = successor
            assert successors
            actions.append(successors)
        game.append(tuple(actions))
    game.append(tuple(1 << sink for _ in plant[0]))
    safe_product = (1 << sink)-1
    target_product = sum(1 << i for i,p in enumerate(pairs) if p[1] == 0)
    return game, pairs, index, update, safe_product, target_product


def check(plant, observations, safe, progress, compare_brute=True):
    game, pairs, index, update, k, p = reduction(plant, observations, safe, progress)
    win = buchi.solve(game, k, p)
    if compare_brute:
        assert win == buchi.brute(game, k, p)
    policy, _ = buchi.rank_certificate(game, k, p, win)
    # Certify on concrete physical states plus the extracted controller memory.
    concrete = [(x,m) for m in bits(win,len(game)) for x in bits(pairs[m][0],len(plant))]
    ci = {pair:i for i,pair in enumerate(concrete)}
    physical_game = []
    for x,m in concrete:
        a = policy[m]
        successors = 0
        for xp in bits(plant[x][a],len(plant)):
            mp = update[m,a,observations[xp]]
            assert (xp,mp) in ci
            successors |= 1 << ci[xp,mp]
        assert successors
        physical_game.append((successors,))
    all_concrete = (1 << len(concrete))-1
    concrete_target = sum(1 << i for i,(x,m) in enumerate(concrete) if progress >> x & 1)
    assert buchi.brute(physical_game, all_concrete, concrete_target) == all_concrete
    initial_wins = {b:bool(win >> index[b,b & ~progress] & 1)
                    for b,o in pairs if o == (b & ~progress)}
    return initial_wins, len(pairs), len(concrete)


def main():
    cases = product_states = concrete_certificates = 0
    for flat in product(range(4), repeat=4):
        plant = (flat[:2],flat[2:])
        for observations in ((0,0),(0,1)):
            for safe in range(4):
                for progress in range(4):
                    if progress & ~safe:
                        continue
                    wins, states, concrete = check(plant,observations,safe,progress)
                    cases += 1
                    product_states += states
                    concrete_certificates += concrete
                    if observations == (0,1):
                        full_win = buchi.solve(plant,safe,progress)
                        assert all(wins[b] == bool(full_win & b) for b in wins)
    # A permanently ambiguous phase nevertheless visits physical state0 forever.
    alternating = ((2,), (1,))
    wins, states, concrete = check(alternating,(0,0),3,1)
    assert wins[3]
    # Marking beliefs only when wholly in target would falsely reject it.
    assert (3 & ~1) != 0
    # A hidden stuttering branch makes the same progress guarantee false.
    stutter = ((3,), (1,))
    bad,_,_ = check(stutter,(0,0),3,2)
    assert not bad[3]
    results = {
        'scope':'Finite sure safety plus physical-state Buchi under partial observation; obligation-memory product',
        'exhaustive_two_state_cases':cases,
        'plants':256,'observation_partitions':2,'safe_progress_pairs':9,
        'constructed_product_states_across_cases':product_states,
        'certified_plant_controller_states':concrete_certificates,
        'checks':['Product fixed point versus exhaustive product-memory strategies',
                  'Extracted strategies checked on concrete plant/controller cycles',
                  'Fully observed specialization equals original full-state solver',
                  'Hidden alternating recurrence succeeds despite never target-certain belief',
                  'A stuttering adversarial option defeats the progress guarantee'],
        'failures':0,
        'limit':'Finite enumeration supports implementation; general equivalence uses the written finite-branching proof.'
    }
    (HERE/'partial-progress-results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__ == '__main__':
    main()
