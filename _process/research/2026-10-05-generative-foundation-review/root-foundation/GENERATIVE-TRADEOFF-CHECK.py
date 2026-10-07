#!/usr/bin/env python3
"""Bind the mixed-comparison integration to already compiled proof snapshots.

This checks preservation, receipts and new local links. It does not rerun Lean
or treat either K's ethical priority or real-world correspondence as proved.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PACKAGE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"
THEORY = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"


def digest(data):
    return sha256(data).hexdigest()


def section(text, heading):
    assert text.count(heading) == 1, heading
    tail = text.split(heading, 1)[1]
    return heading + tail.split("\n## ", 1)[0]


def anchors(text):
    result = set(re.findall(r'<a\s+[^>]*id="([^"]+)"', text))
    for line in text.splitlines():
        if re.match(r"^#{1,6} ", line):
            label = re.sub(r"^#{1,6} +", "", line).strip().lower()
            label = re.sub(r"[^\w\s\-]", "", label)
            result.add(re.sub(r"\s", "-", label))
    return result


def main():
    baseline = json.loads((HERE / "GENERATIVE-TRADEOFF-BASELINE.json").read_text())
    for name, expected in baseline["unchanged"].items():
        assert digest((ROOT / name).read_bytes()) == expected, name
    for name, expected in baseline["preserved_prefixes"].items():
        data = (ROOT / name).read_bytes()
        assert digest(data[:expected["length"]]) == expected["sha256"], name

    proof_path = PACKAGE / "tradeoff-verification.json"
    proof = json.loads(proof_path.read_text())
    assert proof["status"] == "passed" and proof["source_unchanged_during_check"]
    assert "4.29.1" in proof["lean_version"]
    retained = PACKAGE / proof["retained_run"]
    assert (retained / "verification.json").read_bytes() == proof_path.read_bytes()
    for name, expected in proof["source_sha256"].items():
        assert digest((PACKAGE / (name + ".lean")).read_bytes()) == expected, name
    for name, expected in proof["checker_sha256"].items():
        assert digest((PACKAGE / name).read_bytes()) == expected, name
    for name, expected in proof["artifact_sha256"].items():
        assert digest((retained / name).read_bytes()) == expected, name
    module, = proof["modules"]
    assert module["module"] == "GenerativeTradeoff" and module["kernel_checked"]
    assert module["theorems"] == 11 and len(module["declarations"]) == 28
    assert all(not dep for dep in module["axiom_dependencies"].values())
    signatures = (retained / "GenerativeTradeoffSignatures.log").read_text()
    for decl in module["declarations"]:
        if decl["kind"] == "theorem":
            assert decl["name"] in signatures, decl["name"]

    docs = [HERE / ("GENERATIVE-TRADEOFF-" + suffix + ".md")
            for suffix in ["INTEGRATION", "ARGUMENT", "REVIEW", "SOURCES"]]
    texts = {p: p.read_text() for p in docs}
    shared = [ROOT / "README.md", ROOT / "RESEARCH.md", ROOT / "_process/BRIEF.md",
              ROOT / "theories/shengsheng-buxi-generative-existence/README.md",
              THEORY / "GENERATIVE-GROUNDING.md", HERE / "README.md",
              HERE / "GENERATIVE-PREMISE-INTEGRATION.md"]
    for path in shared:
        paragraphs = [p for p in path.read_text().split("\n\n")
                      if "GENERATIVE-TRADEOFF" in p]
        assert paragraphs, path
        texts[path] = "\n\n".join(paragraphs)
    for path, heading in [
        (THEORY / "UNIFIED-ETHICAL-GROUNDING.md", "## Mixed generative comparisons and revisable loss judgments"),
        (HERE / "UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md", "## 19. Mixed comparisons and truth-retaining loss identification"),
    ]:
        texts[path] = section(path.read_text(), heading)
    package_readme = PACKAGE / "README.md"
    marker = "GenerativeTradeoff"
    # Only the added module section, not other sessions' historical descriptions.
    content = package_readme.read_text()
    headings = [h for h in re.findall(r"^## .+$", content, re.M)
                if marker in section(content, h)]
    assert headings, "Missing package correspondence section"
    texts[package_readme] = section(content, headings[-1])

    links = []
    for path, content in texts.items():
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = raw.strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            filepart, _, fragment = unquote(target).partition("#")
            dest = (path.parent / filepart).resolve() if filepart else path
            assert dest.exists(), (path, target)
            if fragment and dest.suffix == ".md":
                assert fragment in anchors(dest.read_text()), (path, target, "anchor")
            links.append({"from": str(path.relative_to(ROOT)), "target": target})

    result = {
        "status": "passed", "utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Document/receipt/preservation check; no additional compilation or ethical proof.",
        "new_theorems": 11, "new_declaration_audits": 28,
        "axiom_dependencies": [], "frozen_artifacts_verified": len(proof["artifact_sha256"]),
        "formal_receipt_sha256": digest(proof_path.read_bytes()),
        "baseline_sha256": digest((HERE / "GENERATIVE-TRADEOFF-BASELINE.json").read_bytes()),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "unchanged_files": len(baseline["unchanged"]),
        "historical_prefixes": len(baseline["preserved_prefixes"]),
        "documents_sha256": {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in docs},
        "integrated_section_sha256": {str(p.relative_to(ROOT)): digest(t.encode()) for p, t in texts.items()},
        "local_links_checked": len(links), "links": links,
    }
    (HERE / "GENERATIVE-TRADEOFF-CHECKS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "new_theorems", "new_declaration_audits", "local_links_checked", "unchanged_files", "historical_prefixes"]}))


if __name__ == "__main__":
    main()
