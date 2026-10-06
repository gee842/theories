"""Validate owned inquiry documents, integration text and unchanged evidence."""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
NOTES = Path(__file__).resolve().parent
THEORY = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"
EXPERIMENT = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/inquiry"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def anchor(heading):
    return re.sub(r"[^\w\s-]", "", heading.strip().lower()).replace(" ", "-")


def main():
    documents = [
        THEORY / "INQUIRY-AND-MATHEMATICAL-IDENTITY.md",
        NOTES / "INQUIRY-CONTINUATION-MATH.md",
        NOTES / "INQUIRY-CONTINUATION-REVIEW.md",
        NOTES / "INQUIRY-CONTINUATION-SOURCES.md",
        ROOT / "sources/15-codex-theory-conversations/2026-10-06-inquiry-and-mathematical-identity-continuation.md",
        EXPERIMENT / "README.md", EXPERIMENT / "PROTOCOL.md",
    ]
    sections = [(path, path.read_text()) for path in documents]
    edits_path = NOTES / "INQUIRY-CONTINUATION-INDEX-EDITS.json"
    for relative, inserted in json.loads(edits_path.read_text()).items():
        path = ROOT / relative
        assert path.read_text().count(inserted) == 1, relative
        sections.append((path, inserted))
    links = anchors = 0
    for path, content in sections:
        for opening, closing in ((r"\[", r"\]"), (r"\(", r"\)")):
            assert content.count(opening) == content.count(closing), path
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", link):
                continue
            destination, sep, fragment = link.partition("#")
            target = (path.parent / destination).resolve() if destination else path
            assert target.exists(), (path, link, target)
            links += 1
            if sep and fragment:
                headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)
                assert fragment in {anchor(h) for h in headings}, (path, link)
                anchors += 1

    results_path, review_path = EXPERIMENT / "results.json", EXPERIMENT / "review-check.json"
    result, review = json.loads(results_path.read_text()), json.loads(review_path.read_text())
    assert result["checker_sha256"] == digest(EXPERIMENT / "check.py")
    assert result["protocol_sha256"] == digest(EXPERIMENT / "PROTOCOL.md")
    assert review["producer_results_sha256"] == digest(results_path)
    assert review["review_checker_sha256"] == digest(EXPERIMENT / "review_check.py")
    assert result["target_specific_comparisons"] == review["checked_decisions"] == 1080
    assert result["matched_sensor_groups"] == 12
    assert review["retained_original_probe_records"] == 36
    assert review["original_probe_retention_failures"] == 12
    assert review["original_experiments_executed"] is False
    for relative, expected in result["source_bindings"].items():
        assert digest(ROOT / relative) == expected, relative
    bound = documents + [edits_path, results_path, review_path,
                         EXPERIMENT / "check.py", EXPERIMENT / "review_check.py",
                         Path(__file__).resolve()]
    receipt = {
        "scope": "owned documents and insertions; source preservation; no old scientific rerun",
        "documents_or_owned_sections": len(sections),
        "local_links": links, "anchors": anchors, "math_delimiters": "balanced",
        "validated_saved_decisions": 1080,
        "unchanged_source_bindings": len(result["source_bindings"]),
        "sha256": {str(p.relative_to(ROOT)): digest(p) for p in bound},
    }
    (NOTES / "INQUIRY-CONTINUATION-CHECKS.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in (
        "documents_or_owned_sections", "local_links", "anchors", "math_delimiters",
        "validated_saved_decisions", "unchanged_source_bindings")}))


if __name__ == "__main__":
    main()
