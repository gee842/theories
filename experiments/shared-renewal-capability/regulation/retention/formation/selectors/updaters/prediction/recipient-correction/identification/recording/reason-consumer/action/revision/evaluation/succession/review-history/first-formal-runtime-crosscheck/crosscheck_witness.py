"""Compare selected preserved execution milestones with audited Lean assertions.

Consumes the completed fresh-build receipt; does not recompile Lean, import
the producer, or claim refinement of every configuration or stochastic path.
"""
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def projection(state):
    c, n, b, r, p = (state[k] for k in ("core", "native", "bank", "reader", "port"))
    energy = (sum(c[k] for k in ("fuel", "source", "recipient", "escrow"))
              + sum(n["packets"]) + sum(state["old_accounts"].values())
              + sum(state["reserves"].values()) + sum(state["idle_common"].values())
              + state["source_reserve"] + state["idle_source"]
              + b["budget"] + b["escrow"] + r["fuel"])
    parts = list(state["parts"].values())
    assert set(parts) <= {"held", "built", "omitted"}
    material = 60 + 2 * len(parts)
    pub = r["publication"]
    current = bool(state["owner"] == "child" and r["phase"] == "published"
                   and r["publication_current"] and r["cache_valid"]
                   and r["cache_context"] is True and r["read_count"] == 3
                   and pub == {"context": True, "mask": r["working"]})
    if current:
        assert r["owner"] == b["owner"] == "child" and r["bound"] and b["live"]
        assert r["bank"] == b["identity"] and n["support"]
    command = None
    if current and state["binding"]["scope"]:
        mask = r["working"]
        if mask[1] and not mask[2]:
            command = False
        elif mask[2] and not mask[1]:
            command = True
    known = (state["n_access"] and n["count"] == 3 and n["mode"] == "closed"
             and n["cells"] == 6 and command is not None
             and command == bool((c["q"] >> 1) & 1))
    assert c["source"] % 10 == 0
    return dict(q=c["q"], qualified=bool(c["last"]), fuel=c["fuel"],
                recipient=c["recipient"], packets=c["source"] // 10,
                n=n["n"], native_source=sum(n["packets"]), count=n["count"],
                native_mode=n["mode"], energy=energy, material=material,
                built=parts.count("built"), held=parts.count("held"),
                omitted=parts.count("omitted"), cursor=state["assembly_cursor"],
                donor=state["donor_status"], child=state["child_status"],
                owner=state["owner"], copy_fund=state["reserves"]["copy"],
                bank_budget=b["budget"], bank_escrow=b["escrow"],
                bank_cells=b["cells"], bank_complete=b["complete"], bank_next=b["next"],
                reader_fund=state["reserves"]["reader"], reader_fuel=r["fuel"],
                reader_phase=r["phase"], current=current, command=command, known=known,
                retired_q=None if state["retired"] is None else state["retired"]["hardware"]["q"],
                port={"assessed_help": "help", "assessed_abstain": "abstain"}.get(p["mode"], p["mode"]),
                phase=state["physical"]["core_phase"], opportunity=p["opportunity"],
                n_access=state["n_access"], permission=state["binding"]["permission"],
                service_spent=sum(state["new_spent"].values()), waste=state["new_waste"],
                actor_bit=c["q"] & 1, recipient_bit=(c["q"] >> 1) & 1)


def main():
    formal = json.loads((HERE / "formal/verification.json").read_text())
    assert formal["status"] == "passed" and formal["source_unchanged_during_check"]
    assert formal["fresh_temporary_build"] and formal["project_objects_only_from_frozen_sources"]
    assert formal["protocol_frozen_predecessors_match"]
    assert all(formal["all_inherited_lean_match_parent_commit"].values())
    assert digest(HERE / "formal/check.py") == formal["checker_sha256"]
    for name, expected in formal["protocol_sources_sha256"].items():
        assert digest(REPO / name) == expected
    audited, formal_sources = set(), {}
    for module in formal["modules"]:
        assert module["clean_dependency_audit"]
        assert digest(REPO / module["source"]) == module["source_sha256"]
        assert digest(HERE / "formal" / module["output"]) == module["output_sha256"]
        audited.update(module["audited_declarations"])
        formal_sources[module["source"]] = module["source_sha256"]

    independent = json.loads((HERE / "model-verification.json").read_text())
    assert independent["status"] == "passed"
    for name, expected in independent["source_sha256"].items():
        assert digest(REPO / name) == expected, name
    files = json.loads((HERE / "result-files.json").read_text())
    assert digest(HERE / files["file"]) == files["compressed_sha256"]
    raw = gzip.decompress((HERE / files["file"]).read_bytes())
    assert hashlib.sha256(raw).hexdigest() == files["uncompressed_sha256"]
    data = json.loads(raw)

    def path(case, arm="shared", index=11):
        rows = data["cases"][case]["arms"][arm]["producers"]["variable"]["paths"]
        return next(r for r in rows if r["predecessor_ref"] == f"signals_111/shared/variable/{index}")

    main_path = path("changed")
    donor = data["parent_catalog"][main_path["predecessor_ref"]]
    assert donor["original_parent_ref"] == "primary/variable/11/37"
    assert donor["donor_state"]["native"]["n"] == 7
    assert donor["donor_state"]["core"]["recipient"] == 60
    comparisons = []

    def check(row, event, theorem, expected):
        name = "SuccessionWitness." + theorem
        assert name in audited, name
        matching = [e for e in row["runtime_trace"] if e["event"] == event]
        assert len(matching) == 1, (event, len(matching))
        actual = projection(matching[0]["state"])
        assert all(actual[k] == v for k, v in expected.items()), (theorem, actual, expected)
        comparisons.append(dict(theorem=name, parent_ref=row["predecessor_ref"],
                                event=event, expected=expected, actual_projection=actual))

    check(main_path, "extension.at_actual_donor", "actual_entry",
          dict(q=0, fuel=0, recipient=60, n=7, native_source=6, energy=162, material=78))
    check(main_path, "assembly.port", "eight_assemblies",
          dict(built=8, held=1, cursor=8, energy=154))
    check(main_path, "handoff.write_unknown", "paid_actual_copy",
          dict(donor="retired", child="committed", q=0, qualified=False, recipient=60,
               fuel=0, copy_fund=0, energy=152, retired_q=0))
    check(main_path, "accounts.release_child", "paid_binding_release",
          dict(owner="child", child="commissioned", built=9, held=0, fuel=26,
               packets=3, recipient=60, bank_budget=5, reader_fund=24, energy=151,
               current=False, reader_phase="cold"))
    check(main_path, "probe0.write", "first_probe_actual",
          dict(q=2, qualified=False, fuel=18, packets=2, recipient=60,
               bank_next=1, bank_complete=False, energy=133))
    check(main_path, "bank.write_bit3", "fresh_acquisition",
          dict(bank_cells=[1,1,1,1], bank_complete=True, bank_next=2,
               bank_budget=0, bank_escrow=0, q=2, qualified=True, fuel=10,
               packets=1, recipient=70, retired_q=0, energy=120))
    check(main_path, "reason.publish", "actual_new_publication",
          dict(q=2, fuel=10, recipient=70, reader_fuel=0, reader_fund=0,
               current=True, command=True, known=True, energy=96))
    check(main_path, "evaluation.write", "acquired_assessment",
          dict(port="help", fuel=8, recipient=70, n=7, known=True, energy=94))
    check(main_path, "selected.write", "actual_selected_action",
          dict(q=2, qualified=True, fuel=0, packets=0, recipient=80, n=7,
               native_source=6, port="consumed", energy=86, material=78, phase="ready"))
    check(main_path, "continuation.complete", "complete_accounts",
          dict(service_spent=66, waste=10, energy=86, material=78))

    filtered = path("changed", "identity_gated")
    check(filtered, "continuation.complete", "equal_information_filter",
          dict(recipient=70, fuel=8, packets=1, energy=94, current=True, n=7))
    def at(row, event):
        return next(x["state"] for x in row["runtime_trace"] if x["event"] == event)
    for key in ("reader", "core", "native"):
        assert at(main_path, "reason.publish")[key] == at(filtered, "reason.publish")[key]
    check(path("permission_cut_before_evaluation"), "selected.guard_blocked",
          "permission_does_not_remove_reason",
          dict(known=True, permission=False, port="consumed", recipient=70, fuel=8))
    check(path("n_disconnected"), "evaluation.read", "unavailable_influence_attempt_is_paid",
          dict(n_access=False, port="consumed", fuel=9, n=7, current=True))
    check(path("n_cut_after_read"), "intervention.n_access@after_evaluation_read",
          "access_cut_invalidates_pending_read",
          dict(n_access=False, port="consumed", fuel=9, n=7))

    required = {"actual_new_facts", "actual_fresh_reasons", "selected_current_reason",
                "actual_effect_from_fresh_evidence", "whole_actual_trace",
                "actual_staged_composition", "finite_successor_capacity"}
    assert {"SuccessionWitness." + n for n in required} <= audited
    fixture = json.loads((HERE / "fixtures.json").read_text())["preparations"]["signals_111"]
    formation = fixture["trace"][94]
    assert formation["plant"] == [38,39,1,1,1,293,216] and formation["spent"] == 80
    assembled = fixture["trace"][-2]
    assert assembled["plant"] == [10,11,1,1,1,265,216] and assembled["spent"] == 108
    endpoint = fixture["trace"][-1]
    assert endpoint == dict(event="exact_M60_projection", plant=[10,10,0,1,0,265,216],
                           spent=109, held_a=9, held_h=9, protected_common=66,
                           protected_source=30, parent_free_a=1, parent_free_h=1,
                           parent_fuel=199, parent_source=186)
    for name in ("formation_endpoint", "material_partition", "exact_parent_prepared_projection",
                 "original_compartments"):
        assert "SuccessionPreparation." + name in audited

    mirror = projection(path("changed", index=4)["state"])
    assert {k: mirror[k] for k in ("q", "recipient", "fuel", "energy", "native_source")} == dict(
        q=1, recipient=80, fuel=0, energy=86, native_source=6)
    final = projection(main_path["state"])
    assert 590 == 410 + 18 + final["service_spent"] + final["waste"] + final["energy"]
    receipt = dict(
        status="passed",
        scope="Selected actual command-zero donor and changed-command successor milestones, "
              "named controls and staged preparation, compared with audited Lean assertions. "
              "No new compiler run or all-case stochastic refinement.",
        source_sha256={str((HERE / f).relative_to(REPO)): digest(HERE / f) for f in (
            "crosscheck_witness.py", "model.py", "results.json.gz", "result-files.json",
            "first-run-receipt.json", "fixtures.json", "model-verification.json",
            "formal/verification.json")},
        formal_sources_sha256=formal_sources,
        formal_new_declarations=formal["new_audited_declarations"],
        milestone_comparisons=comparisons, concrete_preparation_endpoint=endpoint,
        mirror_actual_history=dict(parent_ref="signals_111/shared/variable/4", projection=mirror),
        representation_map=[
            "One live recipient core and one paid reader; retired hardware and old account custody are inert.",
            "Lean packet count equals numerical core source/10 at these selected boundaries.",
            "Lean formal donor q0 changes to child q2; the numerical mirror q1 history is saved evidence, not another concrete Lean witness.",
            "Runtime child committed/commissioned map to Lean committed/child; port idle before actual assembly is an inaccessible formal placeholder.",
            "Lean keeps separate factual-reader and reason-workspace flags; the numerical phase records their completed sequence.",
            "Current/Known are compared only at these selected reachable boundaries, with reader/bank ownership checked; this is not a generic equivalence of all public runtime guards.",
            "Formal probeStart/probeEnd are zero-cost admission-window markers; runtime probe_cursor and per-call phases implement this schedule.",
            "Both selected words settle the core acquisition before flushing four bank bits; binding and latching precede outcome retention.",
            "Formal bank record1 is the complete numerical four-cell frame; record0 is absent and no third acquisition is claimed.",
            "The inherited resident-H/local-fuel adapter accounts for the final preparation plant conversion; staged isolation is not a stochastic M78 erasure theorem.",
            "Numerical permission cut occurs before evaluation and formal specimen after assessment; both reached blocked-action states retain the same facts/n/fuel since permission is an action guard.",
            "Numerical n_disconnected starts with disconnected access; the formal specimen cuts access at the reached publication. Their known-false paid read states agree because inquiry and reading do not depend on n access.",
            "The continuation.complete marker denotes exhausted test scheduling, not settlement of interrupted operations; selected positive and filtered specimens are compared at their stated settled boundaries.",
            "Fresh-fact soundness and the physical effect proof retain calibration and observation-to-use stability. The separate instrumental corollary assumes G; no ethical ground or fulfillment revision is inferred."])
    (HERE / "formal-runtime-crosscheck.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"Matched {len(comparisons)} selected milestones, staged preparation and saved mirror history.")


if __name__ == "__main__":
    main()
