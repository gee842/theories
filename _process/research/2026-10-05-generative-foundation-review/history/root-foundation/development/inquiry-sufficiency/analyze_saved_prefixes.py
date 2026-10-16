"""Evaluate finite predictions at saved prefixes; do not import/run old models.

This analyzes the archived candidate tables and histories. It is a new bounded
calculation about existing records, not a newly executed physical continuation.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
BASE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_bound(directory):
    results_path = directory / "results.json"
    check_path = directory / "independent-check.json"
    results = json.loads(results_path.read_text())
    check = json.loads(check_path.read_text())
    bindings = {}
    for label, hashes in (("producer", results["source_hashes"]),
                          ("independent", check.get("source_hashes", check.get("hashes", {})))):
        bindings[label] = []
        for name, expected in hashes.items():
            source = ROOT / name if name.startswith("experiments/") else (directory / name).resolve()
            actual = sha(source)
            assert actual == expected, (source, expected, actual)
            bindings[label].append({"path": str(source.relative_to(ROOT)), "sha256": actual})
    if "checked_results_sha256" in check:
        assert check["checked_results_sha256"] == sha(results_path)
    bindings["results"] = {"path": str(results_path.relative_to(ROOT)), "sha256": sha(results_path)}
    bindings["prior_check"] = {"path": str(check_path.relative_to(ROOT)), "sha256": sha(check_path)}
    return results, bindings


def predict_readings(machine, phase, parity, count):
    answers = []
    for _ in range(count):
        phase = machine["transitions"][phase][0]
        answers.append(machine["outputs"][phase] ^ parity)
    return answers


methods, method_bindings = load_bound(BASE / "access/revision/metarevision/methods")
access, access_bindings = load_bound(BASE / "access")
case = methods["fixtures"]["four_feedback"]
models = case["generated"]["machines"]
commits = [(i, e) for i, e in enumerate(case["events"]) if e["kind"] == "commit_read"]
prefixes = []
for read_number, history_index in ((3, 4), (4, 6), (5, 8)):
    item = case["history"][history_index]
    predictions = [{"candidate": candidate,
                    "next_two_readings": predict_readings(models[candidate[0] // 2],
                                                           candidate[1], candidate[0] % 2, 2)}
                   for candidate in item["survivors"]]
    event_index, event = commits[read_number - 1]
    prefixes.append({"acquisition_read_number": read_number, "history_index": history_index,
                     "saved_history_prefix": case["history"][:history_index + 1],
                     "survivors": item["survivors"], "predictions": predictions,
                     "next_read_agreement": len({p["next_two_readings"][0] for p in predictions}) == 1,
                     "next_two_agreement": len({tuple(p["next_two_readings"]) for p in predictions}) == 1,
                     "saved_commit_event_index": event_index, "saved_commit_event": event})
assert prefixes[0]["survivors"] == [[0, 0], [2, 0]]
assert prefixes[1]["survivors"] == [[0, 1], [2, 1]]
assert prefixes[2]["survivors"] == [[2, 3]]
assert [p["next_read_agreement"] for p in prefixes] == [True, False, True]
assert [p["next_two_agreement"] for p in prefixes] == [False, False, True]
assert [p["next_two_readings"] for p in prefixes[0]["predictions"]] == [[0, 1], [0, 0]]

endpoints = {}
for name in ("four_exact_budget", "four_one_quantum_short", "four_frozen"):
    x = methods["fixtures"][name]
    endpoints[name] = {key: x[key] for key in
        ("status", "retained", "acquired_retained", "selected", "use_confirmed", "use_receipt",
         "fuel", "source_remaining", "physical_phase", "predictively_equivalent", "history")}
    endpoints[name]["last_events"] = x["events"][-3:]
assert Fraction(endpoints["four_exact_budget"]["fuel"]) == 0
assert endpoints["four_exact_budget"]["retained"]
assert endpoints["four_exact_budget"]["predictively_equivalent"]
assert endpoints["four_one_quantum_short"]["status"] == "funding:retain_after_use"
assert Fraction(endpoints["four_one_quantum_short"]["fuel"]) + Fraction(1, 65536) == Fraction(4745, 8192)
assert endpoints["four_frozen"]["use_confirmed"] and not endpoints["four_frozen"]["predictively_equivalent"]

sensor = access["fixtures"]["sensor_only_ambiguity"]
H = methods["handoff"]["learned_machine"]
sensor_predictions = []
for code, phase in sensor["final_belief"]:
    tau, sigma, broken, blocked = (code >> i & 1 for i in range(4))
    next_phase = H["transitions"][phase][0]
    sensor_predictions.append({"candidate": [code, phase],
                               "next_three_sensor_readings": predict_readings(H, phase, tau ^ sigma, 3),
                               "arrival_after_one_a_if_remaining_source_is_probed":
                               (H["outputs"][next_phase] ^ tau) & (1 - blocked)})
assert sensor["final_belief"] == [[1, 1], [2, 1]]
assert [x["next_three_sensor_readings"] for x in sensor_predictions] == [[0, 1, 1], [0, 1, 1]]
assert [x["arrival_after_one_a_if_remaining_source_is_probed"] for x in sensor_predictions] == [0, 1]

out = {"scope": "Finite prediction calculations at saved prefixes; no model import, native dynamics rerun, new controller, or formal theorem.",
       "script_sha256": sha(Path(__file__)),
       "bindings": {"methods": method_bindings, "access": access_bindings},
       "source_machines": models,
       "four_feedback_prefixes": prefixes,
       "method_endpoints": endpoints,
       "sensor_only_saved": {key: sensor[key] for key in ("final_belief", "history", "native_trace", "source_remaining", "fuel", "verdict")},
       "sensor_prediction_comparison": sensor_predictions,
       "limits": ["Candidate agreement is conditional on class adequacy and the query's stated horizon.",
                  "Advancing from q0 to q1 changes the rolling next-event question; disagreement is not forgetting a past correct prediction.",
                  "The current MethodLearner still requires a singleton. An early robust-prediction routine is not installed.",
                  "Zero fuel excludes additional native commands under the supplied positive tariff, not passive persistence or all real-world continuation.",
                  "No sufficiency criterion or reason for its horizon has been acquired by this analysis."]}
destination = HERE / "PREFIX-EVIDENCE.json"
destination.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"output": str(destination.relative_to(ROOT)), "sha256": sha(destination),
                  "producer_bindings": sum(len(b["producer"]) for b in out["bindings"].values()),
                  "independent_bindings": sum(len(b["independent"]) for b in out["bindings"].values()),
                  "prefixes": len(prefixes), "endpoints": len(endpoints)}))
