"""Delivery integrity for the 慧根 continuation; not a scientific revalidation."""

from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAN = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root"
SYM = LEAN.parent.parent / "necessity-symmetry"
RECIPIENT = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction"
SOURCE = ROOT / "sources/15-codex-theory-conversations/2026-10-06-huigen-entire-theory-necessity.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    counts = {}
    result = set()
    for match in re.finditer(r"^#{1,6}\s+(.+)$", path.read_text(), re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", match.group(1))
        slug = re.sub(r"[^\w\-\s]", "", heading.lower()).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug if number == 0 else f"{slug}-{number}")
    return result


def claim_tables(raw):
    """Return raw data rows and one-based lines, excluding every table header."""
    lines = raw.splitlines(keepends=True)
    tables = []
    i = 0
    while i + 1 < len(lines):
        separators = lines[i + 1].strip().strip(b"|").split(b"|")
        if (lines[i].startswith(b"|") and len(separators) > 1
                and all(re.fullmatch(rb":?-{3,}:?", cell.strip()) for cell in separators)):
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith(b"|"):
                rows.append((j + 1, lines[j]))
                j += 1
            tables.append(rows)
            i = j
        else:
            i += 1
    return tables


def main():
    docs = [CAN / "HUIGEN.md", SOURCE, LEAN / "README.md", SYM / "README.md"]
    docs += [HERE / name for name in (
        "HUIGEN-GENERATIVE-CLOSURE.md", "HUIGEN-FULL-THEORY-AUDIT.md",
        "HUIGEN-NECESSITY-ARGUMENTS.md", "HUIGEN-REVIEW.md",
        "HUIGEN-REASON-TRANSPORT.md", "HUIGEN-PRACTICAL-NECESSITY-AUDIT.md",
        "HUIGEN-PRACTICAL-NECESSITY-SOURCES.md", "HUIGEN-SELF-GROUND-AUDIT.md",
        "HUIGEN-GENERATIVE-IDENTITY.md", "HUIGEN-SELF-GROUND-SOURCES.md",
        "HUIGEN-HARM-IDENTIFICATION.md")]
    indexed = [
        (ROOT / "RESEARCH.md", "**慧根 and necessity of the entire theory,"),
        (CAN.parent / "README.md", "**慧根 and the entire necessary foundation,"),
        (CAN / "GENERATIVE-GROUNDING.md", "**Necessary inquiry → entire generative closure"),
        (HERE / "README.md", "**慧根 and whole-theory necessity,"),
        (ROOT / "sources/SOURCES.md", "Recorded 2026-10-06: [慧根 and necessity"),
        (ROOT / "RESEARCH.md", "**Patient significance → shared practical reasons,"),
        (CAN.parent / "README.md", "**From a patient's significance to another actor's reason,"),
        (CAN / "GENERATIVE-GROUNDING.md", "**Patient-ground → cross-deliberator reason"),
        (HERE / "README.md", "**Patient-ground and deliberator scope,"),
        (ROOT / "sources/SOURCES.md", "Research extension recorded 2026-10-06: the [practical-necessity")]
    texts = [(path, path.read_text()) for path in docs]
    for path, prefix in indexed:
        selected = [p for p in path.read_text().split("\n\n") if p.startswith(prefix)]
        assert len(selected) == 1, (path, "missing or duplicate integration paragraph")
        texts.append((path, selected[0]))
    links = []
    for source, content in texts:
        for target in re.findall(r"\[[^\]\n]+\]\(([^\n)]+)\)", content):
            if re.match(r"[a-zA-Z]+:", target):
                continue
            target = unquote(target.strip("<>"))
            filename, _, fragment = target.partition("#")
            path = (source.parent / filename).resolve() if filename else source
            # This report is the output of the check, so its self-link is checked
            # by construction rather than requiring a prior report to exist.
            assert path.exists() or path == HERE / "HUIGEN-CHECKS.json", (source, target)
            if fragment:
                assert fragment in anchors(path), (source, target, "missing anchor")
            links.append({"source": str(source.relative_to(ROOT)), "target": target})

    coverage = json.loads((HERE / "HUIGEN-CLAIM-COVERAGE.json").read_text())
    claim_bytes = (ROOT / coverage["source"]).read_bytes()
    current_claim_hash = hashlib.sha256(claim_bytes).hexdigest()
    # Bind the historical inventory to its immutable Git snapshot, rather than
    # assuming a shared, growing register remains identical to that snapshot.
    original_claim_commit = "2074796603cb8b3b9fbb4adf324ea57c6622e6e6"
    original_claim_bytes = subprocess.run(
        ["git", "show", original_claim_commit + ":" + coverage["source"]],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    assert hashlib.sha256(original_claim_bytes).hexdigest() == coverage["source_sha256"]
    original_rows = [row for table in claim_tables(original_claim_bytes) for _, row in table]
    assert len(original_rows) == len(set(original_rows)) == 55
    original_lines = original_claim_bytes.splitlines()
    for entry, row in zip(coverage["claims"], original_rows):
        expected = "| " + " | ".join(entry[key] for key in (
            "claim", "source_status", "source_conditions", "source_location")) + " |"
        assert row == expected.encode("utf-8") + b"\n", entry["id"]
        assert original_lines[entry["source_line"] - 1] == row.rstrip(b"\n"), entry["id"]
    live_tables = claim_tables(claim_bytes)
    live_rows = [row for table in live_tables for _, row in table]
    assert all(live_rows.count(row) == 1 for row in original_rows), "changed, missing or duplicated original claim row"
    positions = [live_rows.index(row) for row in original_rows]
    assert positions == sorted(positions), "reordered original claim rows"
    claim_extensions = [{
        "table": table_number,
        "current_line": line_number,
        "row": row.decode("utf-8").rstrip("\n"),
        "row_sha256": hashlib.sha256(row).hexdigest(),
        "scope": "Outside the historical inventory; neither its proof nor its role in whole-root necessity is certified here.",
    } for table_number, table in enumerate(live_tables, start=1)
      for line_number, row in table if row not in original_rows]
    current_claim_rows = len(live_rows)
    assert current_claim_rows == 55 + len(claim_extensions)
    assert coverage["row_count"] == len(coverage["claims"]) == 55
    assert sum(coverage["classes"].values()) == 55
    assert all(row["newly_reverified_proof"] is False for row in coverage["claims"])

    proof = json.loads((LEAN / "verification.json").read_text())
    assert proof["status"] == "passed" and proof["fresh_temporary_build"]
    assert proof["source_unchanged_during_check"]
    assert digest(LEAN / "check.py") == proof["checker_sha256"]
    assert digest(LEAN / "lean-toolchain") == proof["toolchain_sha256"]
    for module in proof["modules"]:
        assert module["exit_code"] == 0 and module["clean_dependency_audit"]
        assert digest(LEAN / module["source"]) == module["source_sha256"]
        assert digest(LEAN / module["output"]) == module["output_sha256"]
        assert set(module["axioms"]) <= {"propext", "Classical.choice", "Quot.sound"}
    new_count = sum(len(m["audited_declarations"]) for m in proof["modules"] if not m["inherited"])
    inherited_count = sum(len(m["audited_declarations"]) for m in proof["modules"] if m["inherited"])
    assert new_count == proof["new_audited_declarations"] == 27
    assert inherited_count == proof["inherited_audited_declarations"] == 23

    symmetry = json.loads((SYM / "verification.json").read_text())
    assert symmetry["status"] == "pass" and digest(SYM / "check.py") == symmetry["source_sha256"]
    assert symmetry["total_matrices_enumerated"] == 66066
    assert [r["jointly_invariant_count"] for r in symmetry["results"]] == [2, 4, 4, 4]
    assert [r["positive_self_count"] for r in symmetry["results"]] == [1, 2, 2, 2]
    assert [r["positive_self_and_actor_independent_count"] for r in symmetry["results"]] == [1, 1, 1, 1]

    # Read the inherited fixture and its receipts; do not rerun the model.
    recipient = json.loads((RECIPIENT / "results.json").read_text())
    recipient_review = json.loads((RECIPIENT / "independent-check.json").read_text())
    assert recipient_review["status"] == "passed"
    for receipt, count in ((recipient, 8), (recipient_review, 11)):
        assert len(receipt["source_sha256"]) == count
        for name, expected in receipt["source_sha256"].items():
            assert digest(ROOT / name) == expected, (name, "changed inherited recipient source")
    arms = recipient["cases"]["primary"]["producers"]["variable"]
    for arm in ("indexed", "private_only"):
        metrics = arms[arm]["metrics"]
        assert metrics["final_actor"] == "25/18"
        assert metrics["actor_captures"] == "2/9"
        assert metrics["spent"] == "25/6"
    assert arms["indexed"]["metrics"]["final_recipient"] == "10/9"
    assert arms["private_only"]["metrics"]["final_recipient"] == "0"

    artifacts = docs + [Path(__file__), HERE / "HUIGEN-CLAIM-COVERAGE.json"]
    artifacts += [LEAN / name for name in ("GenerativeClosure.lean", "InquiryFamilies.lean", "check.py", "lean-toolchain", "verification.json")]
    artifacts += sorted((LEAN / "verification").glob("*.txt"))
    artifacts += [SYM / name for name in ("check.py", "verification.json")]
    report = {
        "date": "2026-10-06", "status": "pass",
        "scope": "Local document links and anchors, owned artifact hashes, historical claim inventory with live row-text preservation and explicitly uncovered additions, existing proof/enumeration receipt consistency and stated inherited recipient metrics/source receipts. No certification of the complete current register, rerun of science, empirical validation or completed philosophical foundation.",
        "local_links_checked": len(links),
        "anchors_checked": sum("#" in link["target"] for link in links),
        "claim_rows_inventoried": 55, "new_lean_audits": new_count,
        "claim_register_snapshot": {
            "original_inventory_source_sha256": coverage["source_sha256"],
            "original_source_commit": original_claim_commit,
            "source_line_scope": "Historical coordinates in the original 55-row snapshot, not current line positions.",
            "current_source_sha256": current_claim_hash,
            "current_canonical_rows": current_claim_rows,
            "current_table_row_counts": [len(table) for table in live_tables],
            "later_rows_outside_inventory": claim_extensions,
            "original_snapshot_verified_in_git_byte_for_byte": True,
            "original_row_texts_present_once_in_order": True,
            "live_register_coverage": "Partial: later rows and surrounding revised context are not certified by this historical inventory. They remain within the eventual whole-theory coverage obligation.",
        },
        "inherited_lean_audits": inherited_count, "finite_matrices_enumerated": 66066,
        "practical_necessity_follow_up": {
            "previous_goal_turn": "progress",
            "new_companions": 3,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "evidence": "Displayed hand proofs, primary-source argument inspection and internal cross-review; no claim that propagation justifies the supplied normative inputs.",
            "inspected_reason_interface": "experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean",
            "inspected_reason_interface_sha256": digest(ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean"),
        },
        "self_ground_follow_up": {
            "previous_goal_turn": "progress",
            "new_companions": 4,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "primary_philosophical_works_examined": 2,
            "primary_empirical_reports_examined": 3,
            "empirical_reports_abstract_only": 1,
            "evidence": "Displayed conditional branching and fixed-constituency succession arguments; exact scoped-inheritance condition; selective primary readings and internal cross-review. Does not establish practical congruency, universal standing or whole-root necessity.",
        },
        "practical_congruency_follow_up": {
            "previous_goal_turn": "progress",
            "existing_companions_extended_or_corrected": 5,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 1,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "evidence": "Matched-case normative adjudication, typed assignment/oracle analysis, Williams primary comparison, corrected countermodel capacity scope, and inherited operational evidence. Positive warrant remains distinct from universal necessity.",
            "recipient_receipt_source_hash_counts": [8, 11],
            "recipient_receipt_sha256": {
                name: digest(RECIPIENT / name)
                for name in ("results.json", "independent-check.json")
            },
            "recipient_metric_scope": "Saved primary variable-producer expected values; no inference from equal means alone to equal nonlinear or risk-sensitive evaluations.",
        },
        "perspective_uptake_follow_up": {
            "previous_goal_turn": "progress",
            "existing_companions_extended": 4,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 1,
            "new_primary_empirical_reports_examined": 3,
            "empirical_reports_abstract_or_preview_only": 2,
            "empirical_reports_selected_full_text": 1,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "proposed_discrimination_tests_executed": False,
            "evidence": "Exact typed-frame hand argument, conditional retention of warranted actual-actor reasons, calibrated acquisition route, scoped Sidgwick and empirical readings, and internal cross-review. Recognition and practical grounding remain distinct; full necessity is not established.",
        },
        "epistemic_authority_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 248,
            "previous_receipt_anchors": 68,
            "previous_canonical_and_review_hashes_revalidated": True,
            "existing_companions_extended": 4,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 4,
            "primary_scope": {
                "Kelly2003": "Selected primary manuscript passages and concluding section; journal metadata separately checked.",
                "Cuneo2007": "Publisher abstract and selected primary transcription: introduction, 77–79, 227–235; no complete-book or facsimile verification.",
                "Cowie2014": "Main published argument inspected; reviewers' narrower passages recorded separately.",
                "Cuneo2016": "Supplementary author-hosted chapter through OCR with recorded selective visual and independent checks.",
            },
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "evidence": "Conditional blanket-veto constraint, inquiry safeguard/substitution/claim-revision argument, stronger endpoint counterinterpretation retaining categorical epistemic reasons, comparative positive patient-ground adjudication, and scoped primary/internal reviews. No inference from some normativity to full patient coverage or whole-theory necessity.",
        },
        "assertion_authority_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 272,
            "previous_receipt_anchors": 83,
            "previous_canonical_and_review_hashes_revalidated": True,
            "existing_companions_extended": 4,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 4,
            "primary_scope": {
                "Moran2005": "Selected original official primary text; addressee/overhearer and retraction/repair passages independently checked; original and reprint dates distinguished.",
                "Cuneo2014": "Publisher preview and discontinuous indexed primary passages; no complete chapter or book verification; reason/rule distinction checked directly in preface x.",
                "KolodnyWallace2003": "Author-hosted primary article pp. 119–128 and 145–154; intervening argument not fully inspected.",
                "Gilbert2013": "Publisher abstract and opening excerpt only; full-page access failed; no complete argument verification.",
            },
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "evidence": "Conditional creation and temporal persistence of directed assurance claims, positive invited-dependence argument, distinction between epistemic correction and practical repair, and scoped primary/internal reviews. Moral legitimacy, categorical reason-authority and never-addressed beneficiary scope remain separate obligations; full necessity is not established.",
        },
        "nonparticipating_patient_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 288,
            "previous_receipt_anchors": 94,
            "previous_canonical_and_review_hashes_revalidated": True,
            "existing_companions_extended": 5,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 4,
            "primary_scope": {
                "Shiffrin1999": "Selected official primary text; responsibility assumption at 119/n8 and burden, benefit and justification passages independently inspected.",
                "Shiffrin2012": "Selected author-uploaded FirstView text, with distinct pagination and tentative status; reason versus claim distinction checked.",
                "Singer1972": "Full primary article through web extraction; historical empirical applications not independently verified or adopted as current facts.",
                "ScanlonColloquiumManuscript": "NYU-hosted manuscript pp. 1–5, 24 and 26–40; hosting context not a verified journal publication date.",
            },
            "inherited_empirical_readings_audited_for_scope": 6,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "new_empirical_proposals_executed": False,
            "evidence": "Defended nonimposition ground reaching a nonparticipant, exact Boolean separation of historical authorship from present relief control, distinct baseline/claim/duty rescue arguments, constructive repeated-protection analysis, and bounded empirical completion audit. Normative premises remain substantive; no whole-root necessity or universal ethical progress proof.",
        },
        "experiential_understanding_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 317,
            "previous_receipt_anchors": 111,
            "previous_canonical_and_review_hashes_revalidated": True,
            "existing_companions_extended": 3,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 4,
            "primary_scope": {
                "Bain2013": "Selected author-uploaded 2012 draft passages; final 2013 metadata checked separately; no final-page or full-paper verification.",
                "Bain2019": "Official accepted manuscript pp. 1–5 and 14–20; distinct draft/final pagination; core pp. 17–18 independently inspected.",
                "Mitchell2019": "Selected author-hosted manuscript PDF pp. 1–4 and 17–25; hypothetical cases not empirical evidence.",
                "Gularte2023": "Publisher HTML core sections and selected notes, with independent partial review; image-rendered formulas not independently facsimile-checked.",
            },
            "new_hand_arguments": 2,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "new_empirical_proposals_executed": False,
            "evidence": "Composition distinguishes attributed patient content from observer total affect without certifying phenomenal realization; conditional remedy revision preserves supplied relief while avoiding another patient's burden. Moral authority, permissible intervention, causal relief and whole-root necessity remain separate obligations.",
        },
        "authorship_permission_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 329,
            "previous_receipt_anchors": 120,
            "previous_canonical_and_review_hashes_revalidated": True,
            "existing_companions_extended": 4,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 3,
            "primary_scope": {
                "Shiffrin2000": "Selected official scan through OCR; independent selected readings and visual checks recorded; printed endpoint differs from bibliography.",
                "Darwall2006": "Selected published primary PDF passages; standing/capacity and respect beyond full competence distinctions independently checked; referenced book not read.",
                "Mill1859": "Root investigator's selected chapters III–V through a paginated Gutenberg edition; no full-book or historical empirical validation.",
            },
            "new_hand_arguments": 2,
            "finite_composition_contract_added": True,
            "new_operating_joins_implemented": 0,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "new_empirical_proposals_executed": False,
            "evidence": "Exact finite permission-correspondence and common-choice criteria, plus endpoint nonidentification of prior authorization. Positive authorship argument supports revisable judgment; authority domains, priority, accommodation and whole-root necessity remain substantively open.",
        },
        "evaluative_transfer_contract_follow_up": {
            "previous_receipt_local_links": 358,
            "previous_receipt_anchors": 145,
            "previous_canonical_full_audit_and_review_hashes_revalidated": True,
            "existing_companions_extended": 1,
            "new_companion_files": 0,
            "new_primary_works_examined": 0,
            "new_hand_arguments": 1,
            "finite_interpretation_contract_refined": True,
            "new_operating_joins_implemented": 0,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "evidence": "Positive recipient weight does not determine a costly-choice margin even within a simple scalar model. The finite contract separates patient identification, actor-addressed reason, authority, comparative judgment and actual acquired influence/use. Qualitative dominance or a defended local priority covers the full declared feasible set; isolating evaluative influence requires controlling or excluding evidence, feasibility and private-incentive differences. Supplied transfer machinery and normative interpretation remain explicit; no implemented composition or universal necessity is claimed.",
        },
        "representation_necessity_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 367,
            "previous_receipt_anchors": 152,
            "previous_canonical_full_audit_and_review_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 2,
            "primary_scope": {
                "Newman1928": "Source investigator read original journal article pp137–148 through OCR and visually checked140,144,148; root independently read140,147–148 through the same OCR; no new source-byte import.",
                "BarrettHalvorson2015v1_2016": "Selected arXiv v1 exposition, definitions and theorem/proof passages with separate root and investigator scopes;2016 publication metadata distinguished from2015 inspected preprint; no complete proof or final-edition audit.",
            },
            "new_hand_result_labels": ["H10", "H11", "H12", "H13", "H14"],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Finite-basis joint interpretation and globally sound generation cover an unbounded closure. Isolated inventory matches differ from full-closure pointwise interpretation; an infinite independent-root witness identifies the compactness boundary. Decoder recoding, unknown calibration and matched passive/different intervention examples distinguish representation, anchored meaning and acquired capacity. Interpretive admissibility remains independent of root truth and allows defended reductions. This is hand-reviewed argument and scoped primary reading, not a new formal or empirical validation or a proof of the actual whole root's necessity.",
        },
        "partial_evidence_action_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 381,
            "previous_receipt_anchors": 170,
            "previous_canonical_closure_necessity_and_review_hashes_revalidated": True,
            "existing_companions_extended": 3,
            "new_companion_files": 0,
            "new_primary_works_examined": 1,
            "primary_scope": {
                "Markovits2010": "Selected published PDF pp. 201–214, 224–230, 238 and 240–241, with visual checks of 211 and 229; root separately read selected passages listed in the dossier. MIT manuscript metadata distinguished from the inspected published copy. No full-article audit or empirical validation; inaccessible Jackson comparator not used.",
            },
            "new_hand_result_labels": ["T15", "T16", "T17", "T18"],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Applies inherited inquiry I1–I3 methods to fixed set-valued action requirements: zero-error common choice, an exact identical-law minimax benchmark, a disjoint-requirement total-variation bound and selective-commitment coverage/error bounds. Actual law and requirement coverage remain application premises. Fixed fact-relative achievement, evidence-relative justification and lottery authorization remain distinct. The reason-use audit separates learning origin, present basis and normative warrant, retaining the accepted fixed-ground/acquired-means conditional recognition contract without new completion gates. No universal ethical authority or whole-root necessity is established.",
        },
        "inductive_risk_reporting_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 398,
            "previous_receipt_anchors": 182,
            "previous_canonical_transport_self_audit_sources_and_review_hashes_revalidated": True,
            "existing_companions_extended": 3,
            "new_companion_files": 0,
            "new_primary_works_examined": 4,
            "primary_scope": {
                "Rudner1953": "Full pp. 1–6 primary extraction by source investigator and separate public primary transcription by root; no facsimile audit; p. 3 n. 1 significance-level gloss is not inherited as a posterior or unconditional error probability.",
                "Douglas2000": "Source investigator read published main text559–578 and visually checked563–564; root read563–565,576–578 through extraction. September-revised published version distinguished from inaccessible indexed preprint. Historical toxicology illustrations not independently validated.",
                "Jeffrey1956": "Critic read full237–246 primary text; root separately read237,241–243,245–246. Tables not independently image-audited; probability proposal and its acknowledged difficulties both retained.",
                "Betz2013": "Critic read early-online main textPDF1–13; root readPDF1,6–7,9,13 and checked publisher metadata. No final-version or complete equation audit; IPCC illustration not empirically assessed.",
            },
            "new_hand_result_labels": ["T19", "T20", "T21", "T22"],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Fixed warranted evidence permits different optimal actions under supplied stakes. Common optimality, including lotteries, requires common minimizers. One deterministic cost-independent complete posterior report serves all positive binary loss ratios exactly iff injective; finite-grid approximation gives normalized regret at most1/(2n). Mathematical optimality is conditional on loss and decision premises. Responsible uncertainty reporting remains a serious alternative to categorical action guidance. Consequential scientific roles do not erase an independently applicable responsibility, but uncertainty alone establishes neither universal standing nor whole-root necessity. No new operating witness or scientific rerun is claimed.",
        },
        "naturalistic_patient_good_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 414,
            "previous_receipt_anchors": 193,
            "previous_canonical_transport_self_audit_sources_and_review_hashes_revalidated": True,
            "existing_companions_extended": 3,
            "new_companion_files": 0,
            "new_primary_works_examined": 2,
            "primary_scope": {
                "Railton1986": "Source investigator read complete original article163–207 through extraction and visually checked174,190,201; root independently read165,173–177,188,190–191,194,201–205; mechanism reviewer separately read174–176. Earlier DAO abstract-only scope remains preserved. No empirical-illustration or2003-reprint validation.",
                "Foot1995": "Critic read complete original article1–14 through extraction; root separately read4,6–10,14. No facsimile audit. Natural Goodness book chapter access was limited to publisher abstracts and is not counted as a full primary reading.",
            },
            "new_hand_argument_blocks": 1,
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "An idealized assessment must preserve the actual patient and circumstances. Contextual adjacent-swap invariance characterizes order-independent readout over all permutations; restricted orders require component comparisons. A finite absorbing counterexample shows that all designated facts can be acquired while recommendations remain order-dependent. This is not a fully rational ideal-agent countermodel or a disproof of naturalistic reduction. Joint empirical and evaluative identification remains a positive route from natural patient conditions to warranted good. Personal good, moral obligation and categorical actor-addressed reasons remain distinct; plural good alternatives are allowed. Recipient-action evidence is read only at its existing canonical scope. Whole-root necessity remains open.",
        },
        "creaturely_good_public_authority_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 425,
            "previous_receipt_anchors": 203,
            "previous_canonical_transport_self_audit_sources_and_review_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 3,
            "primary_scope": {
                "Korsgaard2022Reply": "Source investigator read main author manuscript1–33 and visually checked26,31; root read19–33; mechanism reviewer and critic read25–33. Manuscript and final journal pagination distinguished; no final-journal text comparison. Earlier2018 book reading inherited, not recounted.",
                "Schapiro2022": "Complete publisher HTML main text and notes1–7 read by root and critic; no printed-page assignments or facsimile audit.",
                "GodfreySmith2021": "All eight pages of explicitly incomplete March2021 v1 author draft read through extraction by critic, root and source investigator. Separate from2022 symposium; unfinished positive proposal not represented as completed.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Primary objection/reply comparison repairs chronological and separate-inner-animal interpretations. The stronger rival grants public practical reasons while treating rational status as an additional beneficiary condition. Capacity's failure to determine valuable content does not alone establish its irrelevance to standing; creaturely good as a sufficient ground needs independent justification. Existing transport results already state the conditional extension. Independent truth supports scoped noncontradiction; indispensability to scientific inquiry is a further constitutive claim. No new formal theorem, empirical validation or operating gate; whole-root necessity remains open.",
        },
        "capacity_concern_claims_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 430,
            "previous_receipt_anchors": 206,
            "previous_canonical_transport_self_audit_sources_and_review_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 3,
            "primary_scope": {
                "Feinberg1974": "Source investigator read original chapter43–68 through extraction and visually checked50–51. Root read43–51,66–68. Historical legal and clinical illustrations not verified as current facts. Regan exploratory excerpts not counted as a completed argument reading.",
                "Cohen1986": "Critic, root and source investigator read full eight-page Colorado course transcription; original publication metadata checked. No journal-facsimile comparison or validation of biomedical, legal or comparative-capacity claims.",
                "McMahan2005": "Critic and source investigator read353–361, sections1–3, from original journal PDF extraction. Root read353–363 and beginning364; substantive use confined to sections1–3. No full-article or facsimile audit. Intrinsic-property moral individualism not adopted as a neutral premise.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "The actual rational-kind rights restriction retains humane obligations, so rights denial is not a counterexample to every baseline reason. Feinberg separates conceptual eligibility and represented exercise from an actual owed claim. Capacity-change cases discriminate current exercise, disposition, history, potential and kind separately; a disjunction of grounds can support successive accepted cases without making experience alone sufficient. No universal noncauser reason, equal comparative weight, proxy authority or full answerability follows from these distinctions alone. N1 concern and N3 answerability remain distinct tasks within the whole ethical objective. No new theorem, empirical validation or operating gate.",
        },
        "directed_duties_corrective_response_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 440,
            "previous_receipt_anchors": 215,
            "previous_canonical_transport_self_audit_sources_and_review_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 2,
            "primary_scope": {
                "Raz1986_1988Chapter7": "Source investigator read complete chapter165–192 and notes in Oxford export identifying1988 print edition; visually checked exportPDF13. Root read166–172,176–186 and note182; critic read176–186 and note182 through extraction. Gated1984 Mind article not read in full or treated as interchangeable. Historical institutional illustrations not independently verified as current law.",
                "Thompson2004": "Critic read333–352,366–373 through author-hosted published PDF extraction; root separately read339,342,345,347–350,367–371. Truncated346 output excluded. No full-chapter or facsimile audit. Source investigator explicitly records critic scope rather than claiming an additional personal reading.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "A warranted duty owed to a patient can extend through a defended necessary-means principle to feasible permissible correction of a blocking error. Direction is inherited from that premise, not identified by benefit or technical authority. Aggregate protective duties need not give each patient every outcome, while independently justified procedural standing remains possible. Required response, verification, representation and review retain their particular grounds; no automatic personal explanation, veto or separate right to each technical step follows. Universal noncauser concern and broader N3 answerability remain open. This is primary reading and internal argument review, not a new theorem, empirical validation, implementation or operating gate.",
        },
        "procedural_standing_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 447,
            "previous_receipt_anchors": 221,
            "previous_canonical_transport_self_audit_sources_and_review_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 2,
            "primary_scope": {
                "Waldron2011": "Source investigator read complete published NOMOS chapter3–31 through extraction from a public academic repository's volume PDF. Root and critic independently read14–25. No facsimile audit or reading of other volume chapters. Limited2010 draft access not counted separately or assumed equivalent. Forst2010 candidate reached gated publisher metadata only and supplied no argument.",
                "Raz2006": "Critic read1009–1044 through public primary-text transcription after official PDF access failed. Root separately read1014–1019 and1025–1027. No1003–1008 or facsimile reading. Source investigator records supplied critic scope. Historical institutional illustrations not independently verified as current law.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Composes defended responsibility for an imposed restriction with a feasible proportionate route for otherwise unavailable relevant evidence, without assuming a right to a favorable outcome. The baseline, normative direction and absence of actual defeaters remain premises. Genuine consideration may preserve a justified verdict. Competent delegation preserves agency as a serious comparator; participation independent of accuracy needs a further agency or status ground. Knowable authority and personal explanation remain distinct. Broader N3, universal noncauser concern and whole-root necessity remain open. No new theorem, empirical validation, implementation or accepted-finite-application gate.",
        },
        "agency_delegation_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 456,
            "previous_receipt_anchors": 229,
            "previous_canonical_transport_self_audit_sources_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 1,
            "primary_scope": {
                "Shiffrin2022": "Source investigator read complete printed90–116 including notes through official UCLA repository web extraction. Root separately read91–94,104–108 and115n23. No facsimile or local-extraction claim; referenced Democratic Law not read. Prior Shiffrin2000 not counted again. Pettit1996 candidate yielded metadata and an unreadable scan only, not an inspected argument.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Conditional authorship role can require an actual act or valid delegation without improving the underlying assessment; actual authorization can itself create a normative fact. Effective opportunity differs from an unused invitation. Joint N1–N4 dependency audit preserves patient, good, actor reason and authority; sound conditional generation cannot prove an added agency premise necessary. Coauthors, duty-bearers and affected patients remain distinct. No independence theorem for the entire repository is asserted. Universal noncauser concern, broader N3 and whole-root necessity remain open; no accepted-finite-application gate added.",
        },
        "constitutive_agency_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 471,
            "previous_receipt_anchors": 243,
            "previous_canonical_self_audit_sources_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 3,
            "primary_scope": {
                "Enoch2006": "Critic read main argument169–196 via public primary transcription; root selected183–187 and194–196 through its ordinary public-HTML extraction. No facsimile; references197–198 not inspected.",
                "Ferrero2009": "Source investigator read complete manuscript1–38 ofJan12,2009v3.05 uncorrected proof through web extraction. Not final published chapter or facsimile; proof locators retained. Publisher303–334 differs from some bibliographic303–333 listings.",
                "Ferrero2018": "Root read published113–118 via web and127–154 via ordinary official-PDF download/text extraction. No119–126,155–158reference or facsimile reading. Quoted Enoch2011 not independently read.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "Preserves internal vindication as a route beyond voluntary undertakings while distinguishing jurisdiction, normative authority and patient coverage. Three candidate standards are assessed through inherited scoped arguments, not a new full-basis independence proof. A realist comparator can accept moral reasons while denying their proposed constitutive ground. Formation of recognition differs from justification and validity. Next is the sufficiency and addressee scope of the particular patient-ground. Whole-root necessity remains open; no finite-application gate added.",
        },
        "patient_reason_grounding_follow_up": {
            "previous_goal_turn": "progress",
            "previous_receipt_local_links": 482,
            "previous_receipt_anchors": 253,
            "previous_canonical_self_audit_sources_hashes_revalidated": True,
            "existing_companions_extended": 2,
            "new_companion_files": 0,
            "new_primary_works_examined": 2,
            "primary_scope": {
                "Parfit1997": "Source investigator read complete printed99–130 including notes via primary PDF web/local extraction; root selected115–119 and128–130 via PyPDF. No facsimile. File contains Parfit only despite two-author filename; Broome separate contribution and discovered On What Matters draft not read.",
                "Schroeder2007Weighting": "Critic read main110–130 and notes130–131 via public primary transcription; root independently read114–118 through web extraction. No facsimile or local reading. Reasons and Agent-Neutrality metadata/abstract only, not an additional reading.",
            },
            "new_numbered_result_labels": [],
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "new_operating_joins_implemented": 0,
            "inherited_model_reruns": 0,
            "evidence": "An elementary stipulated explanation-cover argument separates universal patient-reason coverage from a single common desire and from desire-independent grounding. Reason content, explanatory grounds and weight remain distinct; q preserves the patient's relief contrast. Next is warranted acquisition and complete explanatory coverage, not behavioral invariance alone. Real overdetermination, normative validity and whole-root necessity remain unproved; no accepted-finite-application gate added.",
        },
        "artifacts": {str(p.relative_to(ROOT)): digest(p) for p in artifacts},
        "shared_index_paragraphs": [str(p.relative_to(ROOT)) for p, _ in indexed],
        "links": links,
    }
    (HERE / "HUIGEN-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    summary = {k: report[k] for k in ("status", "local_links_checked", "anchors_checked", "claim_rows_inventoried")}
    summary.update({
        "inherited_lean_audits_from_closure_round": report["new_lean_audits"],
        "inherited_matrices_enumerated": report["finite_matrices_enumerated"],
        "new_lean_audits_this_round": 0,
        "new_empirical_studies_this_round": 0,
    })
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
