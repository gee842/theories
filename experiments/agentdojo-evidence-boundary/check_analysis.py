#!/usr/bin/env python3
"""Independent, offline reconstruction from the preserved AgentDojo originals.

No producer or replay imports. This checks saved labels and trace properties,
not the historical evaluator or the behavior of a newly run language model.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "sources/28-agentdojo-evidence-2026-10-06"
COMMIT = "089ed468cf3ed0322acc66b0211f26d9d90dbf60"
PROTOCOL_SHA256 = "d910e7ab54f1155f995807bddca5f5e1dd481a989ab01ccafb45b3033c2120b8"
BASE = "gpt-4o-2024-05-13"
REPEAT = BASE + "-repeat_user_prompt"
PIPELINES = (BASE, REPEAT)
OUTCOMES = ("utility", "attack_success", "secure_utility")


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def object_digest(value):
    return digest(canonical(value).encode("utf-8"))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def strict_label(record, name):
    value = record.get(name)
    need(value is None or type(value) is bool, f"Non-Boolean {name}: {value!r}")
    return value


def expected_path(pipeline, task, injection):
    ending = ("none/none.json" if injection is None else
              f"important_instructions/injection_task_{injection}.json")
    return f"runs/{pipeline}/banking/user_task_{task}/{ending}"


def expected_grid():
    return [(p, t, i, expected_path(p, t, i))
            for p in PIPELINES for t in range(16) for i in [None, *range(9)]]


def verify_sources():
    protocol_bytes = (HERE / "PROTOCOL.md").read_bytes()
    need(digest(protocol_bytes) == PROTOCOL_SHA256, "Frozen protocol changed")
    freeze = read_json(HERE / "protocol-freeze.json")
    need(freeze["sha256"] == PROTOCOL_SHA256, "Wrong protocol receipt")
    tree = read_json(SOURCE / "metadata/tree.json")
    need(not tree.get("truncated"), "Incomplete Git tree")
    tree_entries = {entry["path"]: entry for entry in tree["tree"]}
    need(len(tree_entries) == len(tree["tree"]), "Duplicate tree paths")
    manifest = read_json(SOURCE / "manifest.json")
    need(manifest["commit"] == COMMIT, "Unexpected source commit")
    commit_metadata = read_json(SOURCE / "metadata/commit.json")
    need(commit_metadata["sha"] == COMMIT, "Wrong preserved commit metadata")
    need(manifest["root_tree_sha"] == commit_metadata["tree"]["sha"],
         "Commit's root tree identity mismatch")
    # The preserved recursive-tree response identifies its requested commit in
    # sha/url; bind the actual root tree through Git commit metadata instead.
    need(tree["sha"] in (COMMIT, commit_metadata["tree"]["sha"]),
         "Unexpected recursive-tree request identity")
    entries = {entry["upstream_path"]: entry for entry in manifest["files"]}
    need(len(entries) == len(manifest["files"]), "Duplicate manifest paths")
    for upstream, entry in entries.items():
        need(entry["path"] == "original/" + upstream, f"Nonliteral source path {upstream}")
        data = (SOURCE / entry["path"]).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        need(digest(data) == entry["sha256"], f"Source SHA256 mismatch {upstream}")
        need(blob == entry["git_blob_sha1"], f"Manifest Git identity mismatch {upstream}")
        need(tree_entries[upstream]["sha"] == blob, f"Pinned tree mismatch {upstream}")
        need(tree_entries[upstream]["type"] == "blob", f"Not a blob {upstream}")
        need(len(data) == entry["bytes"], f"Byte count mismatch {upstream}")
    paths = {x[3] for x in expected_grid()}
    need(len(paths) == 320 and paths <= entries.keys(), "Incomplete expected grid")
    selected = {p for p in entries if p.startswith("runs/")}
    need(selected == paths, "Unexpected or missing trajectory selection")
    need(manifest["trajectory_files"] == 320, "Wrong manifest trajectory count")
    need(sum(entries[p]["bytes"] for p in paths) == manifest["trajectory_bytes"],
         "Wrong manifest trajectory byte count")
    return entries, {
        "manifest_sha256": digest((SOURCE / "manifest.json").read_bytes()),
        "tree_sha256": digest((SOURCE / "metadata/tree.json").read_bytes()),
        "protocol_sha256": PROTOCOL_SHA256,
        "commit": COMMIT,
        "verified_source_files": len(entries),
        "verified_trajectory_files": len(paths),
    }


def extract_row(pipeline, task, injection, upstream, entry):
    record = read_json(SOURCE / entry["path"])
    need(record["pipeline_name"] == pipeline, f"Pipeline mismatch {upstream}")
    need(record["suite_name"] == "banking", f"Suite mismatch {upstream}")
    need(record["user_task_id"] == f"user_task_{task}", f"Task mismatch {upstream}")
    expected_injection = None if injection is None else f"injection_task_{injection}"
    need(record["injection_task_id"] == expected_injection, f"Injection mismatch {upstream}")
    expected_attack = None if injection is None else "important_instructions"
    need(record["attack_type"] == expected_attack, f"Attack mismatch {upstream}")
    messages = record["messages"]
    need(type(messages) is list, f"Invalid messages {upstream}")
    users = [m["content"] for m in messages if m["role"] == "user"]
    systems = [m["content"] for m in messages if m["role"] == "system"]
    tools = [m for m in messages if m["role"] == "tool"]
    need(users and systems, f"Missing initial request or system text {upstream}")
    injections = record.get("injections")
    need(type(injections) is dict, f"Invalid injection mapping {upstream}")
    need(all(type(v) is str for v in injections.values()), f"Nontext payload {upstream}")
    need(injection is not None or not injections, f"Injected clean trace {upstream}")
    utility = strict_label(record, "utility")
    security = strict_label(record, "security")
    attack_success = None if injection is None else security
    secure = None if injection is None or utility is None or security is None else utility and not security
    validity_names = sorted(k for k in record if "valid" in k.lower())
    validity = {k: record[k] for k in validity_names}
    # Current archived schema lacks validity. A new field needs semantic review,
    # rather than choosing its polarity by its name or silently using truthiness.
    need(not validity, f"Unreviewed validity schema in {upstream}: {validity_names}")
    assistant_calls = [call for m in messages if m["role"] == "assistant"
                       for call in (m.get("tool_calls") or [])]
    exposed = {k: sum(type(m.get("content")) is str and value in m["content"]
                      for m in tools) for k, value in injections.items()}
    normalized_exposed = {
        k: sum(type(m.get("content")) is str and
               " ".join(value.split()) in " ".join(m["content"].split()) for m in tools)
        for k, value in injections.items()
    }
    return {
        "upstream_path": upstream, "source_sha256": entry["sha256"],
        "pipeline": pipeline, "task": task, "injection": injection,
        "stratum": "clean" if injection is None else "attacked",
        "utility": utility, "raw_security": security, "attack_success": attack_success,
        "secure_utility": secure, "validity": None, "error": record.get("error"),
        "benchmark_version": record.get("benchmark_version"),
        "messages": len(messages), "user_messages": len(users),
        "assistant_messages": sum(m["role"] == "assistant" for m in messages),
        "tool_calls": len(assistant_calls), "tool_responses": len(tools),
        "tool_errors": sum(m.get("error") is not None for m in tools),
        "call_names": dict(sorted(Counter(c["function"] for c in assistant_calls).items())),
        "duration": record.get("duration"),
        "first_user_sha256": object_digest(users[0]),
        "system_messages_sha256": object_digest(systems),
        "payload_sha256": object_digest(injections),
        "payload_keys": sorted(injections),
        "payload_occurrences_in_tool_text": exposed,
        "payload_whitespace_normalized_occurrences": normalized_exposed,
        "repeated_user_messages": sum(u == users[0] for u in users[1:]),
        "nonoriginal_user_messages": sum(u != users[0] for u in users[1:]),
        "environment_metadata_present": any("environment" in k for k in record),
    }


def label_counts(rows, field):
    values = [r[field] for r in rows]
    return {"true": values.count(True), "false": values.count(False),
            "unknown": values.count(None), "selected": len(values)}


def marginal(rows):
    counts = {field: label_counts(rows, field) for field in OUTCOMES}
    joint = Counter((r["utility"], r["attack_success"]) for r in rows)
    counts["joint"] = {f"u{u}_a{a}": joint.get((u, a), 0)
                       for u in (True, False, None) for a in (True, False, None)}
    counts["error_count"] = sum(r["error"] is not None for r in rows)
    counts["validity_unknown"] = len(rows)
    counts["total_messages"] = sum(r["messages"] for r in rows)
    counts["total_tool_calls"] = sum(r["tool_calls"] for r in rows)
    counts["total_tool_errors"] = sum(r["tool_errors"] for r in rows)
    counts["error_by_outcome"] = {
        field: label_counts([r for r in rows if r["error"] is not None], field)
        for field in OUTCOMES
    }
    return counts


def fraction(numerator, denominator):
    return None if not denominator else str(Fraction(numerator, denominator))


def paired_summary(pairs):
    result = {"selected_pairs": len(pairs)}
    for field in OUTCOMES:
        complete = [(left[field], right[field]) for left, right in pairs
                    if left[field] is not None and right[field] is not None]
        cells = Counter(complete)
        difference = sum(int(b) - int(a) for a, b in complete)
        result[field] = {
            "both_false": cells[(False, False)], "both_true": cells[(True, True)],
            "baseline_only": cells[(True, False)], "repeat_only": cells[(False, True)],
            "complete_pairs": len(complete), "unresolved_pairs": len(pairs)-len(complete),
            "repeat_minus_baseline_count": difference,
            "repeat_minus_baseline_rate": fraction(difference, len(complete)),
        }
    result["same_payload"] = sum(a["payload_sha256"] == b["payload_sha256"] for a, b in pairs)
    result["same_initial_request"] = sum(a["first_user_sha256"] == b["first_user_sha256"] for a, b in pairs)
    result["same_system_messages"] = sum(a["system_messages_sha256"] == b["system_messages_sha256"] for a, b in pairs)
    result["both_payload_literal_match"] = sum(
        bool(a["payload_occurrences_in_tool_text"]) and
        all(a["payload_occurrences_in_tool_text"].values()) and
        all(b["payload_occurrences_in_tool_text"].values()) for a, b in pairs)
    result["both_payload_whitespace_match"] = sum(
        bool(a["payload_whitespace_normalized_occurrences"]) and
        all(a["payload_whitespace_normalized_occurrences"].values()) and
        all(b["payload_whitespace_normalized_occurrences"].values()) for a, b in pairs)
    return result


def reconstruct():
    entries, provenance = verify_sources()
    rows = [extract_row(p, t, i, path, entries[path]) for p, t, i, path in expected_grid()]
    lookup = {(r["pipeline"], r["task"], r["injection"]): r for r in rows}
    need(len(lookup) == 320, "Duplicate extracted identities")
    pairs = [(lookup[BASE, t, i], lookup[REPEAT, t, i])
             for t in range(16) for i in range(9)]
    clean_pairs = [(lookup[BASE, t, None], lookup[REPEAT, t, None]) for t in range(16)]
    return {
        "provenance": provenance,
        "scope": "Independently reconstructed reported labels and trace metadata; no model or evaluator replay.",
        "rows": rows,
        "marginals": {p: {s: marginal([r for r in rows if r["pipeline"] == p and r["stratum"] == s])
                          for s in ("clean", "attacked")} for p in PIPELINES},
        "paired_attacked": paired_summary(pairs),
        "paired_clean": paired_summary(clean_pairs),
        "by_task": {str(t): paired_summary([(a,b) for a,b in pairs if a["task"] == t]) for t in range(16)},
        "by_injection": {str(i): paired_summary([(a,b) for a,b in pairs if a["injection"] == i]) for i in range(9)},
        "leave_one_task_out": {str(t): paired_summary([(a,b) for a,b in pairs if a["task"] != t]) for t in range(16)},
        "leave_one_injection_out": {str(i): paired_summary([(a,b) for a,b in pairs if a["injection"] != i]) for i in range(9)},
        "valid_only": {"status": "Unavailable: no recorded validity field; no valid-only estimate manufactured.",
                       "common_valid_pairs": None},
    }


FIELD_MAP = {"utility": "utility", "attack_success": "reported_attacker_success",
             "secure_utility": "reported_joint_task_success"}
PIPELINE_MAP = {BASE: "baseline", REPEAT: "repeat"}


def producer_row(row):
    """Format independently extracted facts in the declared producer schema."""
    task, injection = row["task"], row["injection"]
    return {
        "pipeline": PIPELINE_MAP[row["pipeline"]], "task": task, "injection": injection,
        "case_key": f"u{task:02d}/" + ("clean" if injection is None else f"i{injection}"),
        "source": "sources/28-agentdojo-evidence-2026-10-06/original/" + row["upstream_path"],
        "source_sha256": row["source_sha256"], "request_sha256": row["first_user_sha256"],
        "injections_sha256": row["payload_sha256"],
        "system_messages_sha256": row["system_messages_sha256"],
        "utility": row["utility"], "reported_attacker_success": row["attack_success"],
        "reported_joint_task_success": row["secure_utility"],
        "error_present": row["error"] is not None, "error": row["error"],
        "attack_validity": None, "validity_status": "not_recorded",
        "recorded_message_count": row["messages"], "recorded_user_messages": row["user_messages"],
        "recorded_assistant_messages": row["assistant_messages"],
        "recorded_tool_call_count": row["tool_calls"], "recorded_tool_result_count": row["tool_responses"],
        "recorded_tool_error_count": row["tool_errors"], "recorded_call_names": row["call_names"],
        "recorded_duration": row["duration"],
    }


def producer_counts(rows, field):
    own = label_counts(rows, field)
    known = own["true"] + own["false"]
    return {"true": own["true"], "false": own["false"], "unknown": own["unknown"],
            "known_denominator": known, "true_fraction_among_known": fraction(own["true"], known)}


def producer_summary(rows, attacked):
    output = {"row_count": len(rows), "recorded_errors": sum(r["error"] is not None for r in rows),
              "utility": producer_counts(rows, "utility"),
              "recorded_tool_calls": sum(r["tool_calls"] for r in rows),
              "recorded_tool_results": sum(r["tool_responses"] for r in rows),
              "recorded_tool_errors": sum(r["tool_errors"] for r in rows)}
    if attacked:
        output.update({FIELD_MAP[f]: producer_counts(rows, f) for f in OUTCOMES[1:]})
        output["attack_validity"] = producer_counts(rows, "validity")
        known = [r for r in rows if r["utility"] is not None and r["attack_success"] is not None]
        output["joint"] = {f"u{u}_a{a}": sum(r["utility"] == bool(u) and
                               r["attack_success"] == bool(a) for r in known)
                           for u in (0, 1) for a in (0, 1)}
        output["joint"]["unknown"] = len(rows) - len(known)
    return output


def producer_paired(summary):
    output = {"pair_count": summary["selected_pairs"]}
    for field in OUTCOMES:
        own = summary[field]
        output[FIELD_MAP[field]] = {
            "known_pairs": own["complete_pairs"], "unknown_pairs": own["unresolved_pairs"],
            "changes": {"0->0": own["both_false"], "0->1": own["repeat_only"],
                        "1->0": own["baseline_only"], "1->1": own["both_true"]},
            "repeat_minus_baseline_sum": own["repeat_minus_baseline_count"],
            "repeat_minus_baseline_mean": own["repeat_minus_baseline_rate"],
        }
    return output


def assert_same(expected, actual, path="root"):
    """Return checked scalar count, fail on omitted/extra fields or type drift."""
    need(type(expected) is type(actual), f"Type mismatch at {path}")
    if isinstance(expected, dict):
        need(expected.keys() == actual.keys(),
             f"Key mismatch at {path}: missing {list(expected.keys()-actual.keys())[:5]}, "
             f"unexpected {list(actual.keys()-expected.keys())[:5]}")
        return sum(assert_same(v, actual[k], f"{path}.{k}") for k,v in expected.items())
    if isinstance(expected, list):
        need(len(expected) == len(actual), f"Length mismatch at {path}")
        return sum(assert_same(v, actual[i], f"{path}[{i}]") for i,v in enumerate(expected))
    need(expected == actual, f"Value mismatch at {path}: {expected!r} != {actual!r}")
    return 1


def compare_primary(own, primary):
    need(primary["commit"] == COMMIT, "Primary source commit changed")
    need(primary["protocol_sha256"] == PROTOCOL_SHA256, "Primary protocol identity changed")
    need(primary["manifest_sha256"] == own["provenance"]["manifest_sha256"], "Primary manifest identity changed")
    need(primary["analysis_sha256"] == digest((HERE / "analysis.py").read_bytes()), "Primary producer identity changed")
    need(primary["new_model_calls"] == 0 and primary["real_tool_actions"] == 0, "Unexpected new actions claim")
    expected_rows = {(r["pipeline"], r["case_key"]): r for r in map(producer_row, own["rows"])}
    actual_rows = {(r["pipeline"], r["case_key"]): r for r in primary["rows"]}
    need(len(primary["rows"]) == len(actual_rows) == 320, "Missing/duplicate primary rows")
    checked = assert_same(expected_rows, actual_rows, "rows")
    summary = {}
    lookup = {(r["pipeline"], r["task"], r["injection"]): r for r in own["rows"]}
    for pipeline in PIPELINES:
        rr = [r for r in own["rows"] if r["pipeline"] == pipeline]
        clean = [r for r in rr if r["injection"] is None]
        attacked = [r for r in rr if r["injection"] is not None]
        summary[PIPELINE_MAP[pipeline]] = {
            "clean": producer_summary(clean, False),
            "attacked_all_recorded_labels": producer_summary(attacked, True),
            "attacked_without_recorded_error": producer_summary([r for r in attacked if r["error"] is None], True),
            "attacked_recorded_valid_only": producer_summary([], True),
        }
    checked += assert_same(summary, primary["summaries"], "summaries")
    all_pairs = [(lookup[BASE,t,i], lookup[REPEAT,t,i]) for t in range(16) for i in [None,*range(9)]]
    attack_pairs = [(a,b) for a,b in all_pairs if a["injection"] is not None]
    case_name = lambda r: producer_row(r)["case_key"]
    matching = {"paired_cases": 160, "paired_attacked_cases": 144,
                "request_mismatches": [case_name(a) for a,b in all_pairs if a["first_user_sha256"] != b["first_user_sha256"]],
                "payload_mismatches": [case_name(a) for a,b in all_pairs if a["payload_sha256"] != b["payload_sha256"]],
                "recorded_system_mismatches": [case_name(a) for a,b in all_pairs if a["system_messages_sha256"] != b["system_messages_sha256"]],
                "common_recorded_valid_pairs": 0,
                "initial_environment_per_run_verified": False, "paired_random_seeds_verified": False,
                "transient_model_input_completeness_verified": False}
    checked += assert_same(matching, primary["matching"], "matching")
    for field in ("paired_clean", "paired_attacked"):
        checked += assert_same(producer_paired(own[field]), primary[field], field)
    same_inputs = [(a,b) for a,b in attack_pairs if all(a[k] == b[k] for k in
                   ("first_user_sha256", "payload_sha256", "system_messages_sha256"))]
    no_error = [(a,b) for a,b in attack_pairs if a["error"] is None and b["error"] is None]
    checked += assert_same(producer_paired(paired_summary(same_inputs)), primary["paired_same_recorded_input"], "paired_same_recorded_input")
    checked += assert_same(producer_paired(paired_summary(no_error)), primary["paired_without_recorded_error"], "paired_without_recorded_error")
    for local_name, primary_name in (("by_task", "task_level"), ("by_injection", "injection_level"),
            ("leave_one_task_out", "leave_one_task_out"), ("leave_one_injection_out", "leave_one_injection_out")):
        checked += assert_same({k: producer_paired(v) for k,v in own[local_name].items()}, primary[primary_name], primary_name)
    return checked


def mutation_checks(own, primary):
    def missing_row(x): x["rows"].pop()
    def false_label(x): x["rows"][0]["utility"] = not x["rows"][0]["utility"]
    def clean_attack(x): x["rows"][0]["reported_attacker_success"] = True
    def payload(x): x["rows"][0]["injections_sha256"] = "0"*64
    def validity(x): x["rows"][0]["attack_validity"] = True
    def pairing(x): x["paired_attacked"]["utility"]["known_pairs"] -= 1
    def denominator(x): x["summaries"]["baseline"]["clean"]["utility"]["known_denominator"] *= 9
    def leaveout(x): x["leave_one_task_out"]["0"]["reported_attacker_success"]["repeat_minus_baseline_sum"] += 1
    mutations = {"missing_row": missing_row, "changed_source_label": false_label,
                 "clean_placeholder_as_attack": clean_attack, "wrong_payload_hash": payload,
                 "invented_validity": validity, "wrong_pair_count": pairing,
                 "duplicated_clean_denominator": denominator, "wrong_leaveout": leaveout}
    rejected = {}
    for name, mutate in mutations.items():
        candidate = deepcopy(primary)
        mutate(candidate)
        try:
            compare_primary(own, candidate)
        except AssertionError as error:
            rejected[name] = str(error)
        else:
            raise AssertionError(f"Checker failed to reject mutation {name}")
    return rejected


def exposure_audit(own):
    rows = []
    for row in own["rows"]:
        if row["injection"] is None:
            continue
        literal = row["payload_occurrences_in_tool_text"]
        normalized = row["payload_whitespace_normalized_occurrences"]
        rows.append({"upstream_path": row["upstream_path"], "source_sha256": row["source_sha256"],
                     "pipeline": row["pipeline"], "task": row["task"], "injection": row["injection"],
                     "literal_occurrences_by_payload": literal,
                     "whitespace_normalized_occurrences_by_payload": normalized,
                     "all_payloads_literal_match": bool(literal) and all(literal.values()),
                     "all_payloads_whitespace_match": bool(normalized) and all(normalized.values()),
                     "reported_attack_success": row["attack_success"],
                     "reported_utility": row["utility"]})
    index = {(r["pipeline"], r["task"], r["injection"]): r for r in rows}
    paired = [(index[BASE,t,i], index[REPEAT,t,i]) for t in range(16) for i in range(9)]
    summary = {}
    for pipeline in PIPELINES:
        rr = [r for r in rows if r["pipeline"] == pipeline]
        summary[pipeline] = {"selected_attacked_rows": len(rr)}
        for method in ("literal", "whitespace"):
            matched = [r for r in rr if r[f"all_payloads_{method}_match"]]
            unmatched = [r for r in rr if not r[f"all_payloads_{method}_match"]]
            summary[pipeline][method] = {
                "all_payloads_matched_rows": len(matched), "not_found_rows": len(unmatched),
                "reported_attacker_success_in_matched": sum(r["reported_attack_success"] is True for r in matched),
                "reported_attacker_success_in_not_found": sum(r["reported_attack_success"] is True for r in unmatched),
            }
    pairs = {}
    for method in ("literal", "whitespace"):
        field = f"all_payloads_{method}_match"
        pairs[method] = {f"baseline{a}_repeat{b}": sum(x[field] == bool(a) and y[field] == bool(b)
                                                     for x,y in paired)
                         for a in (0,1) for b in (0,1)}
    return {
        "status": "auxiliary descriptive text audit, not injection-validity or causal exposure inference",
        "source_manifest_sha256": own["provenance"]["manifest_sha256"],
        "method_sha256": digest(Path(__file__).read_bytes()),
        "method": {"messages_examined": "Only role=tool, string content, from original saved JSON.",
                   "literal": "Each entire stored injection value is tested as a literal substring of each tool content.",
                   "whitespace": "str.split() followed by single-space join is applied independently to both strings before the same substring test.",
                   "count": "Number of matching tool messages per stored payload key; empty mappings do not count as matches.",
                   "negative": "Not found by this exact method; this does not prove no exposure. Formatting, escaping, truncation or a different delivered payload can defeat the text match.",
                   "positive": "The saved tool message contains this text under the stated normalization. This is not a validity certificate or proof of a complete transient model input.",
                   "conditioning": "Outcome counts within matching strata condition on recorded execution. They are descriptive and not a randomized defended-versus-unexposed causal contrast."},
        "rows": rows, "summaries": summary, "paired_match_categories": pairs,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "independent-reconstruction.json")
    parser.add_argument("--primary", type=Path, default=HERE / "results.json")
    args = parser.parse_args()
    result = reconstruct()
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    primary = read_json(args.primary)
    checked = compare_primary(result, primary)
    rejected = mutation_checks(result, primary)
    exposure_path = HERE / "exposure-audit.json"
    exposure_path.write_text(json.dumps(exposure_audit(result), indent=2, ensure_ascii=False) + "\n")
    receipt = {"status": "passed", "checked_utc": datetime.now(timezone.utc).isoformat(),
               "scope": result["scope"], "rows": len(result["rows"]), "checked_scalar_fields": checked,
               "provenance": result["provenance"], "mutations_rejected": rejected,
               "checker_sha256": digest(Path(__file__).read_bytes()),
               "primary_results_sha256": digest(args.primary.read_bytes()),
               "exposure_audit_sha256": digest(exposure_path.read_bytes()),
               "independent_reconstruction_sha256": digest(args.output.read_bytes())}
    destination = HERE / "independent-verification.json"
    destination.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "passed", "rows": len(result["rows"]),
                      "checked_scalar_fields": checked, "mutations_rejected": len(rejected),
                      "receipt": str(destination.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
