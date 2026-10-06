#!/usr/bin/env python3
"""Analyze retained records against continuations of the existing finite predictor.

No event law, reward, updater or observation is added. The operational graph is
the pre-existing independent implementation's four-packet graph. Stable finite
partitions are crosschecked by separate all-pairs shortest-word searches. These
are internal exact checks, not empirical evidence or universal learner claims.
"""

import sys
sys.dont_write_bytecode = True

from collections import defaultdict, deque
from dataclasses import asdict, replace
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
SOURCE = HERE / "check_model.py"
SAVED = HERE / "model-verification.json"
OUTPUT = HERE / "acquired-record-profiles.json"
spec = importlib.util.spec_from_file_location("existing_prediction_profile_input", SOURCE)
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)


def hashes():
    paths = model.source_paths() + [Path(__file__).resolve(), SAVED]
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths}


def graph(initial):
    states, identifiers, histories = [initial], {initial: 0}, {0: ()}
    pending, edges = deque([initial]), {}
    while pending:
        state = pending.popleft()
        i = identifiers[state]
        edges[i] = {}
        for event in model.EVENTS:
            if not model.enabled(state, event):
                continue
            successor, _ = model.run_step(state, event)
            if successor not in identifiers:
                identifiers[successor] = len(states)
                states.append(successor)
                histories[identifiers[successor]] = histories[i] + (event,)
                pending.append(successor)
            edges[i][event] = identifiers[successor]
    return states, edges, histories


def partition(states, edges, output):
    """Moore refinement including refusal, stabilized to a fixed point."""
    labels = {}
    classes = []
    for state in states:
        value = output(state)
        labels.setdefault(value, len(labels))
        classes.append(labels[value])
    rounds = 0
    while True:
        labels, refined = {}, []
        for i, state in enumerate(states):
            signature = (output(state), tuple(classes[edges[i][e]] if e in edges[i] else -1
                                               for e in model.EVENTS))
            labels.setdefault(signature, len(labels))
            refined.append(labels[signature])
        rounds += 1
        if refined == classes:
            return classes, rounds
        classes = refined


def shortest_difference(states, edges, output, left, right):
    """Independent product-graph BFS: None means no finite distinguishing word."""
    pending, visited = deque([(left, right, ())]), {(left, right)}
    while pending:
        a, b, word = pending.popleft()
        if (a is None) != (b is None):
            return word
        if output(states[a]) != output(states[b]):
            return word
        for event in model.EVENTS:
            x, y = edges[a].get(event), edges[b].get(event)
            if (x is not None or y is not None) and (x, y) not in visited:
                visited.add((x, y))
                pending.append((x, y, word + (event,)))
    return None


def next_command(state):
    return model.command(state.prediction)


def work_receipt(state):
    # This is the physical receipt retained after work, before the paid write.
    # None distinguishes every other phase; finish clears the receipt.
    return state.prediction.receipt if state.prediction.phase == "observed" else None


def replay_evidence(state, word):
    end, blocked, current, spent, _ = model.replay(state, word)
    return {"completed": end is not None, "blocked_index": blocked,
            "reached": asdict(current), "expenditure_and_waste": spent}


def main():
    before = hashes()
    saved = json.loads(SAVED.read_text())
    for path, digest in saved["source_hashes"].items():
        assert before[path] == digest, f"Preserved source changed: {path}"
    ready, _, witness = model.fixture()
    assert witness == saved["fixture"], "Existing full operational witness changed"
    initial = replace(ready, prediction=replace(ready.prediction,
                      physical=replace(ready.prediction.physical, fuel=15, packets=4)))
    states, edges, histories = graph(initial)
    assert len(states) == saved["complete_operational_graph"]["reachable_states"] == 180
    assert sum(map(len, edges.values())) == saved["complete_operational_graph"]["enabled_labelled_edges"] == 222
    assert asdict(initial) == saved["complete_operational_graph"]["initial"]
    ready_ids = [i for i, s in enumerate(states) if s.prediction.phase == "ready"]
    outputs = {"feasibility": lambda _: None,
               "next_command": next_command, "work_receipt": work_receipt}
    profiles, pair_words, summaries = {}, {}, {}
    for name, output in outputs.items():
        classes, rounds = partition(states, edges, output)
        pairs = {}
        for left in range(len(states)):
            for right in range(left + 1, len(states)):
                word = shortest_difference(states, edges, output, left, right)
                assert (classes[left] == classes[right]) == (word is None)
                pairs[left, right] = word
        profiles[name], pair_words[name] = classes, pairs
        summaries[name] = {"classes": len(set(classes)), "refinement_rounds": rounds,
                           "ready_classes": len({classes[i] for i in ready_ids}),
                           "independent_pair_comparisons": len(pairs)}

    def certificate(left, right, profile, word):
        return {"left": {"id": left, "past": histories[left], "state": asdict(states[left])},
                "right": {"id": right, "past": histories[right], "state": asdict(states[right])},
                "profile": profile, "shortest_distinguishing_word": word,
                "left_continuation": replay_evidence(states[left], word),
                "right_continuation": replay_evidence(states[right], word)}

    records = {"score": lambda s: s.prediction.score,
               "score_and_last": lambda s: (s.prediction.score, s.prediction.physical.last),
               "command": next_command}
    comparisons = {}
    for name, record in records.items():
        groups = defaultdict(list)
        for i in ready_ids:
            groups[record(states[i])].append(i)
        same_record = [(a, b) for group in groups.values()
                       for offset, a in enumerate(group) for b in group[offset + 1:]]
        result = {"record_values": len(groups), "ready_pairs_with_equal_record": len(same_record),
                  "different_immediate_command_pairs": sum(next_command(states[a]) != next_command(states[b])
                                                            for a, b in same_record), "continuation_tests": {}}
        for profile in outputs:
            failures = [(a, b, pair_words[profile][a, b]) for a, b in same_record
                        if profiles[profile][a] != profiles[profile][b]]
            item = {"different_profile_pairs": len(failures)}
            if failures:
                a, b, word = min(failures, key=lambda p: (len(p[2]), len(histories[p[0]]) + len(histories[p[1]]), p[0], p[1]))
                item["shortest_counterexample"] = certificate(a, b, profile, word)
            result["continuation_tests"][profile] = item
        comparisons[name] = result
    # An existing functional sufficiency result, not a learned full-state model.
    assert comparisons["score_and_last"]["different_immediate_command_pairs"] == 0

    same_language = [(a, b) for offset, a in enumerate(ready_ids) for b in ready_ids[offset + 1:]
                     if profiles["feasibility"][a] == profiles["feasibility"][b]]
    command_pairs = [(a, b) for a, b in same_language if next_command(states[a]) != next_command(states[b])]
    receipt_pairs = []
    for a, b in same_language:
        x = model.replay(states[a], model.CYCLE[:2])[0]
        y = model.replay(states[b], model.CYCLE[:2])[0]
        if x is not None and y is not None and x.prediction.receipt != y.prediction.receipt:
            receipt_pairs.append((a, b))
    a, b = min(command_pairs, key=lambda p: (len(histories[p[0]]) + len(histories[p[1]]), p))
    command_example = certificate(a, b, "next_command", ())
    three_cycles = model.replay(initial, model.CYCLE * 3)[0]
    reversed_state = model.run_step(three_cycles, ("reverse", None))[0]
    a, b = states.index(three_cycles), states.index(reversed_state)
    assert profiles["feasibility"][a] == profiles["feasibility"][b]
    assert (three_cycles.prediction.score, three_cycles.prediction.physical.fuel,
            three_cycles.prediction.physical.packets) == (4, 24, 1)
    receipt_word = pair_words["work_receipt"][min(a, b), max(a, b)]
    assert receipt_word == model.CYCLE[:2]
    receipt_example = certificate(a, b, "work_receipt", receipt_word)

    # Replay only actual paid writes of the preserved 42-event witness.
    recorded_score, transcript = ready.prediction.score, []
    current = ready
    for index, event in enumerate(model.WORD):
        successor, cost = model.run_step(current, event)
        if event[0] == "write":
            p = current.prediction
            target = p.physical.last if p.receipt else not p.physical.last
            old = recorded_score
            recorded_score = ((4 if target else 0) if p.physical.fast else
                              min(4, recorded_score + 1) if target else max(0, recorded_score - 1))
            transcript.append({"index": index, "executed_action": p.physical.last,
                               "actual_receipt": p.receipt, "fast_updater": p.physical.fast,
                               "inferred_target": target, "score_before": old,
                               "score_after": recorded_score, "paid_write": cost,
                               "next_command": next_command(successor)})
        assert successor.prediction.score == recorded_score
        assert asdict(successor) == witness["predictive_states"][index + 1]
        current = successor

    assert hashes() == before, "Inputs changed during this check"
    result = {"scope": "Exact internal analysis of the existing finite typed payable-write predictor; no new law, empirical result, selfhood or ethical ground",
              "source_hashes": before, "existing_fixture_replayed_unchanged": True,
              "graph": {"states": len(states), "edges": sum(map(len, edges.values())),
                        "ready_states": len(ready_ids), "closed_to_fixed_point": True, "depth_cutoff": None,
                        "initial": asdict(initial), "all_states": [asdict(s) for s in states],
                        "edges_by_state": {str(i): [{"event": e, "next": j} for e, j in row.items()] for i, row in edges.items()}},
              "profiles": summaries, "profile_class_by_state": profiles,
              "record_comparisons": comparisons,
              "same_feasibility_profile": {"different_immediate_command_pairs": len(command_pairs),
                    "different_receipt_after_rent_work_pairs": len(receipt_pairs),
                    "command_counterexample": command_example, "receipt_counterexample": receipt_example},
              "actual_paid_write_transcript": transcript,
              "analytical_classifier_is_not_an_operational_input": True, "all_checks_passed": True}
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"graph": {k: result["graph"][k] for k in ("states", "edges", "ready_states")},
                      "profiles": summaries, "paid_writes": len(transcript),
                      "same_language_different_commands": len(command_pairs),
                      "same_language_different_receipts": len(receipt_pairs), "output": str(OUTPUT.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
