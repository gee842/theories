"""Read-only extraction of existing inquiry histories; no model imports or runs.

Run from any directory. Existing result-source bindings are checked before
selected fields are copied. Derived counts summarize saved native events only.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
BASE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_result(directory):
    path = directory / "results.json"
    result = json.loads(path.read_text())
    checks = []
    for name, expected in result["source_hashes"].items():
        source = ROOT / name if name.startswith("experiments/") else directory / name
        actual = sha(source)
        assert actual == expected, (str(source), expected, actual)
        checks.append({"path": str(source.relative_to(ROOT)), "sha256": actual})
    independent_path = directory / "independent-check.json"
    independent = json.loads(independent_path.read_text())
    independent_checks = []
    for name, expected in independent.get("source_hashes", independent.get("hashes", {})).items():
        source = ROOT / name if name.startswith("experiments/") else (directory / name).resolve()
        actual = sha(source)
        assert actual == expected, (str(source), expected, actual)
        independent_checks.append({"path": str(source.relative_to(ROOT)), "sha256": actual})
    if "checked_results_sha256" in independent:
        assert independent["checked_results_sha256"] == sha(path)
    return result, {
        "results": {"path": str(path.relative_to(ROOT)), "sha256": sha(path)},
        "prior_independent_check": {
            "path": str(independent_path.relative_to(ROOT)),
            "sha256": sha(independent_path),
            "scope": independent["scope"],
            "verified_source_bindings": independent_checks,
        },
        "verified_source_bindings": checks,
    }


acquisition, acquisition_binding = read_result(BASE)
access, access_binding = read_result(BASE / "access")
methods, methods_binding = read_result(BASE / "access/revision/metarevision/methods")
ancestry_bindings = []
for name, expected in methods["handoff"]["source_hashes"].items():
    actual = sha(ROOT / name)
    assert actual == expected, (name, expected, actual)
    ancestry_bindings.append({"path": name, "sha256": actual})

selected_methods = {}
for name in ("three_feedback", "three_broad", "three_misleading_receipt",
             "three_misleading_frozen", "four_feedback", "four_frozen"):
    case = methods["fixtures"][name]
    keys = ("status", "retained", "acquired_retained", "use_confirmed",
            "method_bit", "recipe", "generated", "receipt", "plan", "selected",
            "use_receipt", "starting_fuel", "fuel", "spent", "income",
            "source_remaining", "wasted", "physical_phase", "peak_cells",
            "predictively_equivalent", "prior_withdrawal", "native_trace", "history")
    selected = {key: case[key] for key in keys}
    selected["derived_from_saved_events"] = {
        "native_events": len(case["native_trace"]),
        "acquisition_reads": sum(e["command"] == "read" for e in case["history"]),
        "acquisition_readings": [e["observation"] for e in case["history"] if e["command"] == "read"],
        "survivors_after_read": [len(e["survivors"]) for e in case["history"] if e["command"] == "read"],
    }
    selected_methods[name] = selected

updated = selected_methods["three_misleading_receipt"]
frozen = selected_methods["three_misleading_frozen"]
assert updated["native_trace"][:4] == frozen["native_trace"][:4]
assert updated["income"] == frozen["income"] == "10"
assert updated["receipt"] == frozen["receipt"] == 0
assert updated["derived_from_saved_events"]["acquisition_readings"] == [1, 0, 0, 1]
assert frozen["derived_from_saved_events"]["acquisition_readings"] == [1, 0, 0]
assert updated["native_trace"][:len(frozen["native_trace"])] == frozen["native_trace"]
assert updated["native_trace"][len(frozen["native_trace"]):] == [
    {"command": "a", "observation": None}, {"command": "read", "observation": 0}]

selected_acquisition = {}
for name in ("primary_unary", "frozen_first_candidate", "binary_same_resources"):
    case = acquisition["cases"][name]
    selected_acquisition[name] = {key: case[key] for key in
        ("status", "certified", "retained", "model", "hypotheses", "queries", "trace", "use")}
assert [e["word"] for e in selected_acquisition["primary_unary"]["queries"]] == ["a" * n for n in range(5)]

selected_access = {}
for name in ("primary_sensor_flip", "sensor_only_ambiguity", "readiness_change",
             "reset_failure", "factored_access_ambiguity", "inverted_consequence_receipt"):
    case = access["fixtures"][name]
    selected_access[name] = {key: case[key] for key in
        ("status", "retained", "final_belief", "verdict", "history", "native_trace", "income", "source_remaining")}

out = {
    "scope": "New read-only extraction and causal interpretation of prior accepted results. No dynamics, model import, scientific rerun or new theorem.",
    "extractor_sha256": sha(Path(__file__)),
    "bindings": {"acquisition": acquisition_binding, "access": access_binding, "methods": methods_binding},
    "methods_handoff": methods["handoff"],
    "verified_handoff_source_bindings": ancestry_bindings,
    "method_fixtures": selected_methods,
    "acquisition_cases": selected_acquisition,
    "access_fixtures": selected_access,
    "interpretive_limits": [
        "The H3 matched contrast changes inquiry duration within a fixed primitive command and observation interface.",
        "G0's first later-use action/read is physically the same as G1's extra acquisition action/read. Total native traces diverge only after G0's use completes.",
        "The receipt-to-method mapping, candidate generators and singleton stopping rule are supplied.",
        "Primary unary query order also matches fixed bounded enumeration; suffix revision alone does not discriminate adaptive physical sampling.",
        "Diagnoser.run receives probe versus sensor-only choice as an argument; acquired belief controls movement within the selected protocol.",
    ],
}
destination = HERE / "INQUIRY-EVIDENCE.json"
destination.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"output": str(destination.relative_to(ROOT)), "sha256": sha(destination),
                  "source_bindings_verified": sum(len(b["verified_source_bindings"]) for b in out["bindings"].values()) + len(ancestry_bindings),
                  "independent_source_bindings_verified": sum(len(b["prior_independent_check"]["verified_source_bindings"]) for b in out["bindings"].values()),
                  "method_fixtures": len(selected_methods), "acquisition_cases": len(selected_acquisition),
                  "access_fixtures": len(selected_access)}))
