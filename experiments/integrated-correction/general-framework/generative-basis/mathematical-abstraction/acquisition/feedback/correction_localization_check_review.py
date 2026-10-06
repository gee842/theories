"""Independent reconstruction of the fixed seven-request contact comparison.

Only standard-library imports. Original and new producers are never imported.
The retained old endpoint is source-bound to its previous independent receipt.
"""
from copy import deepcopy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file()
            and (p / "RESEARCH.md").is_file())
RESULT = HERE / "correction-localization-results.json"
RECEIPT = HERE / "correction-localization-independent-check.json"
OLD_RESULT = HERE / "remaining-dependency-results.json"
OLD_RECEIPT = HERE / "remaining-dependency-independent-check.json"
PROTOCOL = HERE / "CORRECTION-LOCALIZATION-PROTOCOL.md"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def equal(actual, expected, label):
    assert actual == expected, (label, actual, expected)


def verify_account(state, original):
    a, n = state["account"], state["native"]
    assert Q(a["fuel"]) >= 0
    equal(Q(a["fuel"]) + Q(a["spent"]), Q(a["start"]), "actor account")
    equal(Q(a["income"]), Q(0), "actor income")
    equal(a["workspace"], 0, "workspace")
    equal(state["inherited"], original["inherited"], "retained ancestry")
    for field in ("source", "load", "waste", "test_law", "full_law", "context"):
        equal(n[field], original["native"][field], "native " + field)
    inherited = Q(145) - Q(a["start"]) - sum(original["native"][k]
                                                for k in ("source", "load", "waste"))
    whole = inherited + Q(a["spent"]) + Q(a["fuel"]) + sum(n[k]
                                                for k in ("source", "load", "waste"))
    equal(whole, Q(145), "conserved original account")
    equal(Q(state["whole_account"]), whole, "reported original account")


def charged(state, kind, work, temporary, extra, rewrites):
    a = state["account"]
    live = a["live"]
    peak = live + temporary
    bill = Q(work + rewrites, 64) + Q(peak * (work + 1), 65536) + extra
    assert peak <= a["capacity"] and Q(a["fuel"]) >= bill, (kind, "unfunded")
    a["fuel"] = str(Q(a["fuel"]) - bill)
    a["spent"] = str(Q(a["spent"]) + bill)
    a["peak"] = max(a["peak"], peak)
    return dict(kind=kind, work=work, live=live, temporary=temporary,
                workspace=0, peak=peak, rewrites=rewrites, extra=str(extra),
                bill=str(bill), fuel=a["fuel"])


def expected_suffix(old_case, selector):
    """Translate seven explicit semantic operations, without producer dispatch."""
    state = deepcopy(old_case["final"])
    initial = deepcopy(state)
    verify_account(state, initial)
    n, c = state["native"], state["controller"]
    equal(n["context"], 1, "context needed for correctly bound write")
    equal(n["source"], 0, "source exhausted before inquiry")
    equal(c["installed"], True, "existing reader")
    equal(c["values"], [0, 1], "old records")
    events = []

    def record(kind, detail, work=1, temporary=2, extra=Q(0), rewrites=0,
               effect=lambda: None):
        charge = charged(state, kind, work, temporary, extra, rewrites)
        effect()
        verify_account(state, initial)
        events.append(dict(kind=kind, detail=detail, charge=charge,
                           state=deepcopy(state)))

    record("relay_command", {"setting": 1}, extra=Q(1, 4),
           effect=lambda: n.update(relay=1, held=False))
    record("weak_challenge", {}, extra=Q(1, 4),
           effect=lambda: n.update(pending=[n["context"], n["relay"],
                                            n["test_law"][n["relay"]]]))

    def contact():
        datum = n["pending"]
        n["pending"] = None
        fault = old_case["parameters"]["fault"]
        if datum is not None and fault is not None:
            kind, at = fault
            if at in (selector, "both"):
                if kind == "missing":
                    datum = None
                elif kind == "context":
                    datum[0] = 2
                elif kind == "setting":
                    datum[1] = 1 - datum[1]
                elif kind == "flip":
                    datum[2] = 1 - datum[2]
                else:
                    raise AssertionError(("unsupported contact fault", fault))
        c["contact"] = datum

    record("dependency_contact", {"probe": selector}, work=0, extra=Q(1, 4),
           effect=contact)

    def write():
        d = c["contact"]
        if d is not None and d[0] == 1 and d[1] == 1 and d[2] in (0, 1):
            c["values"][1], c["tags"][1] = d[2], 1
        else:
            c["values"][1], c["tags"][1] = None, None
        c["contact"] = None

    record("dependency_slot_write", {"setting": 1}, rewrites=2, effect=write)

    def read():
        values = c["values"]
        if None in values:
            candidate, mode = None, "unresolved"
        elif values[0] == 1:
            candidate, mode = 0, "selected_bypass"
        elif values[1] == 1:
            candidate, mode = 1, "selected_relay"
        else:
            candidate, mode = None, "no_supported_route"
        c.update(candidate=candidate, read_mode=mode)

    record("dependency_read", {}, work=2, effect=read)
    assert old_case["parameters"]["policy"] == "learned"
    record("dependency_commit", {}, rewrites=2,
           effect=lambda: c.update(selected=c["candidate"], mode=c["read_mode"]))
    record("dependency_retention", {}, temporary=0,
           extra=Q(state["account"]["live"], 64),
           effect=lambda: c.update(retained=True))
    equal(Q(initial["account"]["fuel"]) - Q(state["account"]["fuel"]),
          Q(95732, 65536), "complete seven-request bill")
    equal(Q(state["account"]["fuel"]), Q(166143, 32768), "final fuel")
    equal(Q(state["account"]["spent"]), Q(190363, 32768), "final expenditure")
    return initial, events, state


def projection(event):
    return {k: deepcopy(event[k]) for k in ("kind", "detail", "charge")} | {
        "state": {k: deepcopy(event["state"][k])
                  for k in ("account", "inherited", "controller")}}


def check_case(case, originals):
    source = originals[case["source_case"]]
    selector = case["contact_selector"]
    assert selector in (0, 1)
    equal(case["name"], source["name"] + "_contact_" + str(selector), "case name")
    equal(case["inherited_consumption"], source["inherited_consumption"], "old consumption")
    equal(case["original_prefix_records"], len(source["trace"]), "old prefix length")
    equal(case["original_prefix_verified"], True, "producer prefix assertion")
    initial, events, final = expected_suffix(source, selector)
    equal(case["old_endpoint"], initial, "exact old endpoint")
    equal(case["trace"], events, "all independent suffix events")
    equal(case["final"], final, "full independent final state")
    return dict(source_case=source["name"], contact_selector=selector,
                state_points=8, charged_events=7,
                suffix_bill="23933/16384", fuel=final["account"]["fuel"],
                spent=final["account"]["spent"],
                values=final["controller"]["values"],
                selected=final["controller"]["selected"],
                mode=final["controller"]["mode"],
                stocks={k: final["native"][k] for k in ("source", "load", "waste")})


def rejection_controls(case, originals):
    mutations = {}
    x = deepcopy(case)
    x["old_endpoint"]["account"]["fuel"] = "7"
    mutations["hidden_boundary_fuel_reset"] = x
    x = deepcopy(case)
    x["trace"][2]["state"]["controller"]["contact"][1] = 0
    mutations["contact_tag_misbound"] = x
    x = deepcopy(case)
    x["trace"][3]["state"]["controller"]["values"][1] = 1
    mutations["corrected_value_replaced"] = x
    x = deepcopy(case)
    x["trace"][5]["state"]["controller"]["selected"] = 1
    mutations["consumer_not_revised"] = x
    x = deepcopy(case)
    x["trace"][6]["state"]["native"]["source"] = 10
    mutations["packet_replenished"] = x
    x = deepcopy(case)
    x["trace"][0]["state"]["inherited"]["H"]["outputs"][0] = 0
    mutations["inherited_model_overwritten"] = x
    x = deepcopy(case)
    x["trace"][0]["charge"]["bill"] = "0"
    mutations["uncharged_command"] = x
    rejected = []
    for name, changed in mutations.items():
        try:
            check_case(changed, originals)
        except AssertionError:
            rejected.append(name)
        else:
            raise AssertionError(("missed corrupted artifact", name))
    return rejected


def main():
    result_hash = sha(RESULT)
    result = json.loads(RESULT.read_text())
    old = json.loads(OLD_RESULT.read_text())
    old_receipt = json.loads(OLD_RECEIPT.read_text())
    assert old_receipt["status"] == "passed"
    equal(old_receipt["results_sha256"], sha(OLD_RESULT), "prior result binding")
    equal(old_receipt["check_source_sha256"], sha(HERE / "remaining_dependency_check_review.py"),
          "prior independent checker binding")
    equal(result["protocol_sha256"], sha(PROTOCOL), "new protocol binding")
    bindings = result["source_bindings"]
    equal(len(bindings), 22, "prospective source-binding count")
    for path, digest in bindings.items():
        equal(sha(ROOT / path), digest, "bound source " + path)
    for path, digest in old["source_hashes"].items():
        equal(bindings[path], digest, "unchanged original source")
    equal(len(old["source_hashes"]), 14, "inherited original-source count")

    originals = {c["name"]: c for c in old["cases"]}
    names = ("law_01_learned", "calibration_break", "false_dependence")
    selected = {name: originals[name] for name in names}
    old_projections = [[projection(e) for e in selected[name]["trace"]] for name in names]
    assert all(len(p) == 16 for p in old_projections)
    equal(old_projections[0], old_projections[1], "old success/calibration collision")
    equal(old_projections[1], old_projections[2], "old failure-cause collision")
    cases = result["cases"]
    equal(result["case_count"], 6, "case count")
    equal(len(cases), 6, "case list length")
    equal(result["suffix_event_count"], 42, "suffix count")
    equal({(c["source_case"], c["contact_selector"]) for c in cases},
          {(name, i) for name in names for i in (0, 1)}, "fixed six comparisons")
    checked = {c["name"]: check_case(c, selected) for c in cases}
    indexed = {(c["source_case"], c["contact_selector"]): c for c in cases}
    for selector in (0, 1):
        p = [[projection(e) for e in indexed[name, selector]["trace"]] for name in names]
        equal(p[0], p[1], "success/calibration remain indistinguishable")
        if selector == 1:
            equal(p[1], p[2], "same-channel control remains indistinguishable")
        else:
            equal(p[0][:2], p[2][:2], "no split before alternate contact")
            assert p[0][2:] != p[2][2:]
            equal(p[2][3]["state"]["controller"]["values"], [0, 0], "acquired split")
            equal(p[2][5]["state"]["controller"]["selected"], None, "operative split")
    # Within each source, pre-contact activity/cost is matched. At contact only
    # the supplied selector changes; subsequent native stocks stay matched.
    for name in names:
        a, b = indexed[name, 1], indexed[name, 0]
        equal(a["old_endpoint"], b["old_endpoint"], "matched exact start")
        equal(a["trace"][:2], b["trace"][:2], "matched pre-contact history")
        equal([e["charge"] for e in a["trace"]], [e["charge"] for e in b["trace"]],
              "matched complete charges")
    rejected = rejection_controls(indexed["false_dependence", 0], selected)
    for path, digest in bindings.items():
        equal(sha(ROOT / path), digest, "postcheck source stability")
    equal(sha(RESULT), result_hash, "result stability")
    receipt = dict(
        status="passed",
        scope="Independent seven-request semantic replay from six exact saved endpoints; no producer imports",
        results_sha256=result_hash, check_source_sha256=sha(Path(__file__)),
        protocol_sha256=sha(PROTOCOL), source_bindings=bindings,
        source_binding_count=len(bindings), inherited_original_source_bindings=14,
        prior_independent_receipt_sha256=sha(OLD_RECEIPT),
        case_count=6, independently_reconstructed_suffix_events=42,
        suffix_state_points_including_exact_starts=48,
        independently_compared_old_projection_records=48,
        independently_reconstructed_charges=42,
        prefix_guard_failures=0, original_account_conserved=145,
        bill_ticks=[17480, 17480, 16420, 3144, 2156, 3144, 35908],
        suffix_bill_ticks=95732, final_fuel_ticks=332286,
        matched_pre_contact_pairs=3, source_interface_fault_split=True,
        ordinary_vs_calibration_still_indistinguishable=True,
        rejected_mutations=rejected, cases=checked,
        limitations=[
            "Old ancestry is bound to its prior independent receipt, not rerun here.",
            "Projection equality contains every demonstrated reader input but includes external audit fields.",
            "Alternate contact selector is supplied API/event-law semantics, not newly formed physical access.",
            "The diagnostic word is prescribed; the old executor does not autonomously choose it.",
            "No final full-load receipt, additional packet or restored load service occurs.",
            "No new Lean build, universal implementation equivalence or ethical warrant is established.",
        ])
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(status="passed", cases=6, events=42, state_points=48,
                          bindings=22, rejected_mutations=len(rejected),
                          checker_sha256=sha(Path(__file__)), receipt_sha256=sha(RECEIPT)),
                     sort_keys=True))


if __name__ == "__main__":
    main()
