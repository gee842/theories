"""Validate this contribution's documents, insertions and finite-check bindings."""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
NOTES = Path(__file__).resolve().parent
THEORY = ROOT / "theories/becoming/chapters"
EXPERIMENT = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/identity"


def anchor(heading):
    return re.sub(r"[^\w\s-]", "", heading.strip().lower()).replace(" ", "-")


def main():
    new_documents = [
        THEORY / "IMMANENT-MATHEMATICAL-IDENTITY.md",
        NOTES / "IMMANENT-MATHEMATICAL-IDENTITY-MATH.md",
        NOTES / "IMMANENT-MATHEMATICAL-IDENTITY-REVIEW.md",
        NOTES / "IMMANENT-MATHEMATICAL-IDENTITY-SOURCES.md",
        ROOT / "sources/15-codex-theory-conversations/2026-10-06-mathematical-identity-nondual-continuation.md",
        EXPERIMENT / "README.md",
        EXPERIMENT / "PROTOCOL.md",
    ]
    sections = [(p, p.read_text()) for p in new_documents]
    edits_path = NOTES / "IMMANENT-MATHEMATICAL-IDENTITY-INDEX-EDITS.json"
    for name, inserted in json.loads(edits_path.read_text()).items():
        path = ROOT / name
        assert path.read_text().count(inserted) == 1, (name, "owned insertion changed")
        sections.append((path, inserted))

    links, anchors = 0, 0
    for path, text in sections:
        assert text.count(r"\[") == text.count(r"\]"), path
        assert text.count(r"\(") == text.count(r"\)"), path
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                continue
            destination, sep, fragment = link.partition("#")
            target = (path.parent / destination).resolve() if destination else path
            assert target.exists(), (path, link, target)
            links += 1
            if sep and fragment:
                headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)
                assert fragment in {anchor(h) for h in headings}, (path, link)
                anchors += 1

    results_path = EXPERIMENT / "results.json"
    results = json.loads(results_path.read_text())
    for name, digest in results["sha256"].items():
        assert sha256((EXPERIMENT / name).read_bytes()).hexdigest() == digest, name
    assert results["processes_by_state_count"] == {"1": 8, "2": 324, "3": 32768}
    assert results["total_processes"] == 33100
    assert results["interface_algorithm_comparisons"] == 99300
    assert results["history_operation_counterexample"]["prefixed_outputs"] == [1, 0]

    inherited = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/metarevision/methods/formation/results.json"
    inherited_hash = sha256(inherited.read_bytes()).hexdigest()
    assert inherited_hash == "2b0afb08f3507eaf2de3126dcc43a3dca8dd65ff6603658ee8aae697e42263e4"
    bound = new_documents + [edits_path, results_path, EXPERIMENT / "check.py",
                             Path(__file__).resolve()]
    receipt = {
        "scope": "new documents and exact owned insertions; no old scientific rerun",
        "documents_or_owned_sections": len(sections),
        "local_links": links,
        "anchors": anchors,
        "math_delimiters": "balanced",
        "finite_processes": 33100,
        "finite_interface_comparisons": 99300,
        "inherited_formation_result_sha256": inherited_hash,
        "sha256": {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                   for p in bound},
    }
    (NOTES / "IMMANENT-MATHEMATICAL-IDENTITY-CHECKS.json").write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: receipt[k] for k in (
        "documents_or_owned_sections", "local_links", "anchors",
        "math_delimiters", "finite_processes", "finite_interface_comparisons")}))


if __name__ == "__main__":
    main()
