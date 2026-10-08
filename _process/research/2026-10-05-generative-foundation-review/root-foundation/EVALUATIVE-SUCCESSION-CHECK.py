"""Bind accepted succession receipts and integration documents; no scientific rerun."""
from pathlib import Path
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
STUDY = REPO / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/succession"
CANONICAL = REPO / "theories/becoming/chapters/EVALUATIVE-SUCCESSION.md"
OUTPUT = HERE / "EVALUATIVE-SUCCESSION-INTEGRATION.json"
verified = {}


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def match(path, expected):
    assert path.is_file() and digest(path) == expected, path
    verified[str(path.relative_to(REPO))] = expected


def bind_map(mapping):
    for name, expected in mapping.items():
        match(REPO / name, expected)


def source_receipt(receipt):
    bind_map(receipt["source_sha256"])


freeze = read(STUDY / "protocol-freeze.json")
match(STUDY / "protocol-freeze.json", "6cdbc9ed4a96783e60a196e5970b8e7c9f1872b5c221c7fbfa16c5b6e0dcccc5")
assert len(freeze["source_sha256"]) == 150 and freeze["case_count"] == 29
source_receipt(freeze)
bind_map(freeze["contract_files_sha256"])
bind_map(freeze["preserved_prospective_files_sha256"])
assert freeze["all_accepted_current_bytes_match_parent_commit"]
assert freeze["all_cited_accepted_source_receipts_match"]
accept_freeze = read(STUDY / "root-freeze-acceptance.json")
match(STUDY / "root-freeze-acceptance.json", "39430df628282971b1f52d6260dd541bb5d75f5331c3bf0e02276e144aad3cb0")
assert accept_freeze["status"] == "prospective_freeze_accepted_by_root_before_implementation"
frozen_review = accept_freeze["independent_freeze_verification"]
match(REPO / frozen_review["path"], frozen_review["sha256"])
oracle = freeze["independent_prospective_oracle"]
match(REPO / oracle["preserved_source"], oracle["source_sha256_at_freeze"])
match(REPO / oracle["preserved_receipt"], oracle["preserved_receipt_sha256"])

first = read(STUDY / "first-run-receipt.json")
assert first["status"] == "producer_checks_passed_pending_independent_review"
source_receipt(first)
assert (STUDY / "review-history/first-producer-run/model.py").read_bytes() == (STUDY / "model.py").read_bytes()
files = read(STUDY / "result-files.json")
assert files == first["result_files"]
match(STUDY / files["file"], files["compressed_sha256"])
raw = gzip.decompress((STUDY / files["file"]).read_bytes())
assert len(raw) == files["uncompressed_bytes"]
assert hashlib.sha256(raw).hexdigest() == files["uncompressed_sha256"]
results = json.loads(raw)
source_receipt(results)
serialized = json.dumps(results["cases"], sort_keys=True, separators=(",", ":")).encode()
assert hashlib.sha256(serialized).hexdigest() == files["semantic_cases_sha256"]
cases = read(STUDY / "cases.json")
assert set(results["cases"]) == {x["name"] for x in cases["cases"]}
for item in cases["cases"]:
    result = results["cases"][item["name"]]
    assert result["config"] == item["config"]
    assert set(result["arms"]) == set(cases["arms"])
    for arm in result["arms"].values():
        assert set(arm["producers"]) == set(cases["producers"])

independent = read(STUDY / "model-verification.json")
expected_counts = dict(cases=29, mixtures=261, histories=3306, snapshots=67974,
                       aggregate_values=11223, parent_catalog=114, ancestry_catalog=38,
                       formation_prefixes=372)
assert independent["status"] == "passed" and independent["counts"] == expected_counts
assert independent["comparisons"] == dict(conventional_exact_histories=1102, equal_input_histories=1102)
assert independent["mutation_count"] == len(independent["mutations"]) == 14
assert all(x["rejected"] for x in independent["mutations"])
source_receipt(independent)
acceptance = read(STUDY / "review-acceptance.json")
assert acceptance["status"] == "accepted" and not acceptance["unresolved_material_issues"]
source_receipt(acceptance)

formal = read(STUDY / "formal/verification.json")
assert formal["status"] == "passed" and formal["source_unchanged_during_check"]
assert formal["fresh_temporary_build"] and formal["project_objects_only_from_frozen_sources"]
assert formal["protocol_frozen_predecessors_match"]
assert len(formal["all_inherited_lean_match_parent_commit"]) == 26
assert all(formal["all_inherited_lean_match_parent_commit"].values())
assert len(formal["modules"]) == 29
new_modules = {"SuccessionPreparation", "EvaluativeSuccession", "SuccessionWitness"}
assert {m["module"] for m in formal["modules"] if m["role"] == "new formalization"} == new_modules
assert formal["new_audited_declarations"] == sum(m["dependency_audits"] for m in formal["modules"] if m["module"] in new_modules)
match(STUDY / "formal/check.py", formal["checker_sha256"])
match(STUDY / "formal/lean-toolchain", formal["toolchain_sha256"])
for module in formal["modules"]:
    assert module["exit_code"] == 0 and module["clean_dependency_audit"]
    assert set(module["axioms"]) <= {"propext", "Quot.sound", "Classical.choice"}
    match(REPO / module["source"], module["source_sha256"])
    match(STUDY / "formal" / module["output"], module["output_sha256"])

crosscheck = read(STUDY / "formal-runtime-crosscheck.json")
assert crosscheck["status"] == "passed"
assert crosscheck["formal_new_declarations"] == formal["new_audited_declarations"]
assert len(crosscheck["milestone_comparisons"]) == 14
source_receipt(crosscheck)
bind_map(crosscheck["formal_sources_sha256"])
producer = read(STUDY / "producer-check.json")
assert producer["status"] == "passed"
assert producer["counts"] == dict(exact_shared_conventional_histories=1102,
                                 shared_gated_equal_preassessment_histories=1102,
                                 guard_and_custody_controls=16)
source_receipt(producer)
reporting = read(STUDY / "reporting.json")
source_receipt(reporting)
assert reporting["result_files"] == files
for case in results["cases"]:
    for arm in results["cases"][case]["arms"]:
        for name, result in results["cases"][case]["arms"][arm]["producers"].items():
            assert reporting["cases"][case][arm][name] == result["metrics"]
for arm in ("shared", "conventional"):
    m = reporting["cases"]["changed"][arm]["variable"]
    assert m["selected_capture"] == m["probe_captures"] == "1/4"
    assert m["selected_recipient_gain"] == m["probe_recipient_gain"] == "5/2"
assert reporting["cases"]["changed"]["identity_gated"]["variable"]["selected_capture"] == "0"

documents = [CANONICAL, STUDY / "README.md", STUDY / "formal/README.md",
             STUDY / "DRAFT-PROTOCOL.md", STUDY / "INTERFACE.md",
             HERE / "EVALUATIVE-SUCCESSION-SCOPE.md", HERE / "EVALUATIVE-SUCCESSION-MATH.md",
             HERE / "EVALUATIVE-SUCCESSION-REVIEW.md"]
links = 0
for path in documents:
    content = path.read_text()
    targets = re.findall(r"\]\(([^)]+)\)", content)
    targets += re.findall(r"^\[[^]]+\]:\s*(\S+)", content, re.M)
    for link in targets:
        if link.startswith(("http:", "https:", "#")):
            continue
        target = (path.parent / link.split("#")[0]).resolve()
        assert target == OUTPUT or target.exists(), (path, link)
        links += 1
    verified[str(path.relative_to(REPO))] = digest(path)
for name in ("protocol-freeze.json", "root-freeze-acceptance.json", "first-run-receipt.json",
             "result-files.json", "model-verification.json", "review-acceptance.json",
             "producer-check.json", "formal-runtime-crosscheck.json",
             "formal/verification.json", "reporting.json"):
    p = STUDY / name
    verified[str(p.relative_to(REPO))] = digest(p)
verified[str(Path(__file__).relative_to(REPO))] = digest(Path(__file__))
report = dict(
    status="passed", scope="Receipt, preservation and document integration; no scientific rerun.",
    counts=expected_counts, new_lean_audits=formal["new_audited_declarations"],
    formal_modules=29, independent_mutation_rejections=14, selected_milestones=14,
    unchanged_first_numerical_outputs=True, unchanged_parent_sources=150, relative_links=links,
    verified_sha256=verified,
    limitations="Finite staged preparation and selected actual Lean witness; no all-case stochastic refinement. "
                "Recipes, inquiry schedule, funding, transfer and observation laws remain explicit. "
                "No ethical ground, fulfilled-claim application revision, self-financing ecology or indefinite "
                "succession is established. This closes the named finite causal bridge, not the unified foundation.")
OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({k:v for k,v in report.items() if k != "verified_sha256"}, indent=2))
