"""Independent baseline check from declared period formulas, using JSON only.

Does not import model.py or verify.py. Its oracle is a closed-form description
of one initially defective-evaluator period and subsequent repaired periods.
All 54 admissible four-period law sequences are compared microstep by microstep.
This supplements (and does not replace) the unbounded graph certificate.
"""
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
g = json.loads((HERE / "graph-baseline.json").read_text())
states = {s["id"]: s for s in g["states"]}
edges = {}
for e in g["edges"]:
    edges.setdefault(e["source"], []).append(e)

def response(rule, x):
    # Four explicit functions, independent of the model's bit extraction.
    return ((0, 0), (1, 0), (0, 1), (1, 1))[rule][x]

def oracle(period, phase, laws):
    law = laws[period]
    initial_round = period == 0
    old_program = 0 if initial_round else laws[period - 1]
    funds = [7, 8, 7, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2, 8][phase]
    if initial_round and phase == 0:
        funds = 8
    linked = [response(law, 0) if phase >= 3 else -1, response(law, 1) if phase >= 4 else -1]
    candidate = -1 if phase <= 4 else 0 if initial_round and phase <= 10 else law
    check0 = response(law, 0) if phase in range(6, 11) or phase >= 12 else -1
    check1 = response(law, 1) if phase in range(7, 11) or phase >= 13 else -1
    installed = old_program if phase <= 15 else law
    evaluator = 0 if initial_round and phase <= 9 else 1
    pack = [installed, evaluator, 1, *linked]
    return {
        "phase": phase, "truth": law, "installed": installed, "evaluator": evaluator,
        "guard": 1, "skilled": True, "funds": funds,
        "carrier": (period + int(phase >= 21)) % 2,
        "lease": phase >= 2, "data0": linked[0], "data1": linked[1],
        "candidate": candidate, "check0": check0, "check1": check1,
        "review_failed": initial_round and phase >= 9,
        "certificate": phase >= 14, "active": phase >= 16,
        "archive": pack if phase >= 19 else None,
        "trainee": pack if phase >= 20 else None,
        "bad": False, "protected": True,
    }

def expected_events(period, phase, law):
    result = set()
    if phase in (0, 7, 14, 21):
        result.add("auxiliary_service")
    if phase == 9 and period == 0:
        result.add("evaluator_revised")
    if phase in (4, 10) and law in (1, 2) and (period > 0 or phase == 10):
        result.add("conditional_candidate_constructed")
    if phase == 15:
        result.update(("program_admitted", "corrective_install"))
    if phase in (16, 17):
        result.add("delivered_x" + str(phase - 16))
    if phase == 18:
        result.add("maintained_archive")
    if phase == 19:
        result.add("trained_successor")
    if phase == 20:
        result.add("competent_handoff")
    return result

sequences = [seq for seq in product(range(4), repeat=4)
             if seq[0] in (1, 2) and all(a != b for a, b in zip(seq, seq[1:]))]
covered_states, covered_edges = set(), set()
state_checks = edge_checks = 0
for laws in sequences:
    current = next(i for i in g["initial"] if states[i]["truth"] == laws[0])
    for period in range(4):
        for phase in range(23):
            s = states[current]
            expected = oracle(period, phase, laws)
            assert {k: s[k] for k in expected} == expected, (laws, period, phase, s, expected)
            covered_states.add(current)
            state_checks += 1
            choices = edges[current]
            if phase == 22:
                # Check all environmental branches even after the last inspected round.
                assert {states[e["target"]]["truth"] for e in choices} == set(range(4)) - {laws[period]}
            else:
                assert len(choices) == 1
            for e in choices:
                assert set(e["events"]) == expected_events(period, phase, laws[period])
                assert e["cost"] == 1
                receipt = 7 if phase in (0, 7, 14, 21) else 0
                assert e["receipt"] == receipt
                assert e["spill"] == max(0, expected["funds"] - 1 + receipt - 8)
                covered_edges.add((e["source"], e["target"]))
                edge_checks += 1
            if phase == 22:
                if period < 3:
                    current = next(e["target"] for e in choices if states[e["target"]]["truth"] == laws[period + 1])
            else:
                current = choices[0]["target"]

assert len(covered_states) == len(g["states"]), "Oracle sequences missed a reachable state."
assert len(covered_edges) == len(g["edges"]), "Oracle sequences missed a reachable edge."
result = {"passes": True, "method": "closed-form period oracle; no implementation imports",
          "law_sequences": len(sequences), "periods_per_sequence": 4,
          "state_checks": state_checks, "edge_checks": edge_checks,
          "all_reachable_states_covered": len(covered_states),
          "all_actual_edges_covered": len(covered_edges)}
(HERE / "independent-oracle-results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
