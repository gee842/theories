"""Read-only extraction from accepted records; no model import or rerun.

This checks the current source hashes against saved receipts and identifies
matched saved outcomes at the complete witness's actual learning entrance.
It does not independently reconstruct the underlying transition law.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/coupling/architecture/learning"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records = {name: json.loads((BASE / name).read_text()) for name in
               ("witness.json", "results.json", "independent-check.json", "handoff-check.json")}
    bindings = []
    for name, key in (("witness.json", "source_sha256"),
                      ("independent-check.json", "source_hashes"),
                      ("handoff-check.json", "source_sha256")):
        hashes = records[name][key]
        mismatches = [p for p, h in hashes.items() if digest(ROOT / p) != h]
        assert not mismatches, (name, mismatches)
        bindings.append(dict(receipt=name, checked_sources=len(hashes), mismatches=mismatches))

    witness = records["witness.json"]
    entry = witness["learning_entry"]
    contrasts = {}
    for arm in ("indexed", "no_feedback", "misleading", "private_zero", "shared_write"):
        rows = [r for r in records["results.json"]["cases"]["primary"]["arms"][arm]["terminal_rows"]
                if r["entry"] == entry and r["regime"] == 1]
        assert len(rows) == 1
        row = rows[0]
        state, parent = row["state"], row["state"]["parent"]
        contrasts[arm] = dict(probability=row["probability"],
            parent={k: parent[k] for k in ("fuel", "patient", "q", "last", "coupling", "graph", "retained")},
            learning={k: state[k] for k in ("wire", "indexed", "spent", "recipient_captures", "real_positive", "real_zero", "changed_writes", "damage", "patient_used")})

    stable = ("graph", "coupling", "guides_e", "guides_i", "r_nodes", "d_nodes")
    trace = []
    for row in witness["learning"]:
        s, p = row["state"], row["state"]["parent"]
        assert all(p[k] == entry[k] for k in stable)
        trace.append(dict(event=row["event"], fuel=p["fuel"], patient=p["patient"],
                          q=p["q"], qualification=p["last"] if s["indexed"] else None,
                          escrow=s["escrow"], bank=s["bank"]))
    assert witness["inherited_prior_motor_revision"] is False
    assert sum(v for k, v in witness["energy_account"].items() if k != "initial") == 195

    aggregate_keys = ("recipient_captures", "p_strict_witness", "p_site_retained", "fuel",
                      "actor_captures", "p_prior_motor_revision_and_strict_witness")
    selected_aggregates = {
        case: {arm: {k: records["results.json"]["cases"][case]["arms"][arm]["metrics"][k]
                     for k in aggregate_keys}
               for arm in ("indexed", "no_feedback", "private_zero", "shared_write")}
        for case in ("primary", "same_law", "same_law_outages", "reversal_after_positive")}

    report = dict(status="passed", date="2026-10-06",
        scope="Read-only saved-record extraction and preservation checks; no transition rerun, new theorem, or empirical result.",
        source_bindings=bindings,
        inspected_artifact_sha256={str((BASE / name).relative_to(ROOT)): digest(BASE / name) for name in records},
        extractor_sha256=digest(Path(__file__)),
        learning_entry=entry,
        single_complete_word_probability=witness["single_complete_word_probability"],
        same_endpoint_preparation_family_probability=witness["same_endpoint_preparation_family_probability"],
        inherited_prior_motor_revision=witness["inherited_prior_motor_revision"],
        preserved_topology_fields=list(stable),
        actual_learning_trace=trace, matched_saved_outcomes=contrasts,
        saved_unconditional_aggregate_metrics=selected_aggregates,
        whole_history_energy_account=witness["energy_account"])
    destination = Path(__file__).with_name("EXTRACTED-EVIDENCE.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "bindings": bindings,
                      "saved_trace_events": len(trace), "matched_arms": len(contrasts)}))


if __name__ == "__main__":
    main()
