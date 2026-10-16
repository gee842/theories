"""Extract existing method-edge evidence without importing or running a model."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/metarevision/methods/formation"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    results = json.loads((BASE / "results.json").read_text())
    receipt = json.loads((BASE / "independent-check.json").read_text())
    mismatches = [p for p, h in receipt["source_hashes"].items() if digest(ROOT / p) != h]
    assert not mismatches
    assert digest(BASE / "results.json") == receipt["checked_producer_results_sha256"]
    names = ("three_first_0", "three_first_1", "four_first_0", "four_first_1",
             "formation_clamped", "source_port_mismatch", "accepted_edge_broken",
             "first_destination_swapped", "transfer_blocked", "outside_five", "outside_delayed")
    keep = ("status", "receipt", "archive", "method_edge", "edge_retained",
            "accepted_recipe", "trials", "retired_edges", "invocations", "selected",
            "use_confirmed", "use_receipt", "retained", "predictively_equivalent",
            "starting_fuel", "spent", "fuel", "income", "wasted", "source_remaining",
            "live_cells", "peak_cells")
    extracted = {name: {k: results["fixtures"][name][k] for k in keep} for name in names}
    actual = results["fixtures"]["four_first_0"]
    extracted["four_first_0"]["native_trace"] = actual["native_trace"]
    extracted["four_first_0"]["stored_event_counts"] = dict(Counter(e["kind"] for e in actual["events"]))
    assert actual["archive"] == [0, 1, 0, 0, 0, 1]
    assert [i["recipe"] for i in actual["invocations"]] == [0, 1, 1]
    assert actual["retired_edges"] == [[0, 0, 1]]
    assert actual["method_edge"] == [0, 1, 1]
    assert results["fixtures"]["accepted_edge_broken"]["status"] == "no_bound_method_edge"
    assert results["fixtures"]["outside_delayed"]["use_confirmed"] is True
    assert results["fixtures"]["outside_delayed"]["predictively_equivalent"] is False
    report = dict(date="2026-10-06", status="passed",
        scope="Read-only extraction and current-byte binding of accepted source/results; no transition rerun, theorem or empirical result.",
        receipt_bound_sources=len(receipt["source_hashes"]), source_mismatches=mismatches,
        artifact_sha256={str((BASE / name).relative_to(ROOT)): digest(BASE / name)
                         for name in ("model.py", "results.json", "independent-check.json")},
        extractor_sha256=digest(Path(__file__)), inherited_handoff=results["handoff"],
        stored_selected_fixtures=extracted)
    Path(__file__).with_name("METHOD-EVIDENCE.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "passed", "selected_saved_fixtures": len(names),
                      "source_bindings": len(receipt["source_hashes"]), "dynamics_rerun": False}))


if __name__ == "__main__":
    main()
