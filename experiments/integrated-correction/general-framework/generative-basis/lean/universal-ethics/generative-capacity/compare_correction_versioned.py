#!/usr/bin/env python3
"""Finite reachable-state and controlled-thread checks of the versioned model.
This is an authored transcription, not extracted Lean or empirical AI validation.
The invariant oracle computes complete actual suffix effects independently of
cached summaries. Thread runs exercise short locks and deliberately broken controls.
"""
from collections import deque
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
from threading import Event, Lock, Thread
import json

HERE = Path(__file__).resolve().parent
BITS = (False, True)
EMPTY = ((), False, False)
OPS = [('reset', b) for b in BITS] + [('append', b, p) for b, p in product(BITS, repeat=2)] + [('certify', b) for b in BITS] + [('publish', b) for b in BITS] + [('begin', r) for r in BITS] + [('tick',), ('pause',)]

def follow(path, payload):
    for bit in path:
        payload = payload != bit
    return payload

def initial(path):
    return (False, ((tuple(path), follow(path, False), True), EMPTY), ())

def replace_bank(state, slot, bank):
    active, banks, packets = state
    new = list(banks)
    new[int(slot)] = bank
    return active, tuple(new), packets

def busy(state, slot):
    return any(p[0] == slot for p in state[2])

def step(span, capacity, state, op):
    active, banks, packets = state
    kind, *args = op
    if kind in ('reset', 'append', 'certify'):
        slot = args[0]
        free = slot != active and not busy(state, slot)
        path, summary, sealed = banks[int(slot)]
        if kind == 'reset' and free:
            state = replace_bank(state, slot, EMPTY)
        elif kind == 'append' and free and not sealed and len(path) < span:
            state = replace_bank(state, slot, (path + (args[1],), summary != args[1], False))
        elif kind == 'certify' and free and len(path) == span:
            state = replace_bank(state, slot, (path, summary, True))
    elif kind == 'publish':
        slot = args[0]
        path, _, sealed = banks[int(slot)]
        if sealed and len(path) == span:
            state = slot, banks, packets
    elif kind == 'begin' and len(packets) < capacity:
        requested = args[0]
        state = active, banks, packets + ((active, 0, requested != banks[int(active)][1], requested),)
    elif kind == 'tick' and packets:
        slot, cursor, payload, requested = packets[0]
        path = banks[int(slot)][0]
        if cursor >= len(path):
            return (active, banks, packets[1:]), (requested, payload)
        new_packet = slot, cursor + 1, payload != path[cursor], requested
        state = active, banks, (new_packet,) + packets[1:]
    return state, None

def invariant(span, capacity, state):
    active, banks, packets = state
    assert len(packets) <= capacity
    for path, summary, _ in banks:
        assert len(path) <= span
        assert follow(path, False) == summary
    assert banks[int(active)][2] and len(banks[int(active)][0]) == span
    for slot, cursor, payload, requested in packets:
        path, _, sealed = banks[int(slot)]
        assert sealed and len(path) == span and 0 <= cursor <= span
        assert follow(path[cursor:], payload) == requested


def explore(span, capacity):
    seeds = [initial(path) for path in product(BITS, repeat=span)]
    seen, queue = set(seeds), deque(seeds)
    edges = outputs = pinned_blocks = 0
    edge_hash = sha256()
    while queue:
        state = queue.popleft()
        invariant(span, capacity, state)
        for op in OPS:
            successor, output = step(span, capacity, state, op)
            invariant(span, capacity, successor)
            if output is not None:
                assert output[0] == output[1]
                outputs += 1
            if op[0] == 'reset' and busy(state, op[1]):
                assert successor == state
                pinned_blocks += 1
            edges += 1
            edge_hash.update(repr((state, op, successor, output)).encode())
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)
    return {'span': span, 'capacity': capacity, 'states': len(seen), 'transitions': edges,
            'correct_output_edges': outputs, 'blocked_pinned_resets': pinned_blocks,
            'state_sha256': sha256(repr(sorted(seen)).encode()).hexdigest(),
            'transition_sha256': edge_hash.hexdigest(), 'closed_reachable_graph': True}


def sequential_handoffs(rounds=100):
    state = initial((False, False))
    histories = []
    for iteration in range(rounds):
        old = state[0]
        new = not old
        path = ((iteration % 2) == 0, (iteration % 3) == 0)
        requested = (iteration % 2) == 1
        ops = [('begin', requested), ('tick',), ('reset', new)]
        ops += [('append', new, bit) for bit in path]
        ops += [('certify', new), ('publish', new), ('reset', old), ('tick',), ('tick',), ('reset', old)]
        output = []
        for op in ops:
            before = state
            state, result = step(2, 2, state, op)
            invariant(2, 2, state)
            if op == ('reset', old) and busy(before, old):
                assert state == before
            if result is not None:
                output.append(result)
        assert output == [(requested, requested)]
        assert state[0] == new and state[1][int(old)] == EMPTY and not state[2]
        histories.append({'iteration': iteration, 'new_slot': new, 'new_path': path, 'output': output})
    return histories


def threaded_trial(mode, index):
    lock = Lock()
    state = initial((True, True))
    reached, changed, finished = Event(), Event(), Event()
    history, errors, output = [], [], []

    def act(op, validate=True):
        nonlocal state
        with lock:
            state, result = step(2, 2, state, op)
            if validate:
                invariant(2, 2, state)
            history.append((op, state, result))
            if result is not None:
                output.append(result)
            return state

    def reader():
        nonlocal state
        try:
            if mode == 'split_capture':
                with lock:
                    captured = (state[0], 0, True != state[1][int(state[0])][1], True)
            else:
                act(('begin', True))
                act(('tick',))
            reached.set()
            assert changed.wait(5), 'updater timeout'
            if mode == 'split_capture':
                with lock:
                    state = state[0], state[1], (captured,)
                    history.append(('late_registration', state))
            elif mode == 'read_active_again':
                with lock:
                    state = state[0], state[1], tuple((state[0], *p[1:]) for p in state[2])
                    history.append(('changed_packet_slot', state))
            for _ in range(3 if mode == 'split_capture' else 2):
                act(('tick',), validate=(mode == 'versioned'))
            finished.set()
        except BaseException as exc:
            errors.append(repr(exc)); reached.set(); finished.set()

    def updater():
        nonlocal state
        try:
            assert reached.wait(5), 'reader timeout'
            for op in [('reset', True), ('append', True, False), ('append', True, False),
                       ('certify', True), ('publish', True)]:
                act(op)
            if mode == 'split_capture':
                for op in [('reset', False), ('append', False, True), ('append', False, False), ('certify', False)]:
                    act(op)
            elif mode == 'premature_reuse':
                with lock:
                    state = replace_bank(state, False, ((False, False), False, True))
                    history.append(('forced_reuse', state))
            else:
                before = state
                assert act(('reset', False)) == before
            changed.set()
            assert finished.wait(5), 'completion timeout'
            if mode == 'versioned':
                after = act(('reset', False))
                assert after[1][0] == EMPTY and not after[2]
        except BaseException as exc:
            errors.append(repr(exc)); changed.set()

    threads = [Thread(target=reader), Thread(target=updater)]
    for thread in threads: thread.start()
    for thread in threads: thread.join(10)
    assert not any(t.is_alive() for t in threads), 'thread did not terminate'
    assert not errors, errors
    expected = [(True, mode == 'versioned')]
    assert output == expected, (mode, output)
    return {'mode': mode, 'trial': index, 'output': output, 'history': history}


def main():
    graphs = [explore(span, capacity) for span in range(3) for capacity in (1, 2)]
    handoffs = sequential_handoffs()
    trials = [threaded_trial(mode, i) for mode in ('versioned', 'read_active_again', 'premature_reuse', 'split_capture') for i in range(20)]
    sources = {name: sha256((HERE/name).read_bytes()).hexdigest() for name in ('CorrectionVersioned.lean', 'CorrectionRelations.lean', 'CorrectionHandoff.lean')}
    record = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'status': 'passed',
              'sources': sources, 'runner_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'graphs': graphs, 'total_states': sum(g['states'] for g in graphs),
              'total_transitions': sum(g['transitions'] for g in graphs),
              'repeated_handoffs': handoffs, 'thread_trials': trials,
              'thread_summary': {'versioned_correct':20, 'mixed_version_wrong':20,
                                 'premature_reuse_wrong':20, 'split_capture_wrong':20},
              'scope': 'Complete reachable finite Python models, 100 serial handoffs and 80 controlled shared-memory thread trials. Same-author transcription, not extracted-code refinement or empirical AI validation.'}
    (HERE/'correction-versioned-model-checks.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','total_states','total_transitions','thread_summary')}))
    print(json.dumps(graphs))

if __name__ == '__main__':
    main()
