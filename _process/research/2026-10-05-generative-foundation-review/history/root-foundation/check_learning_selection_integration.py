#!/usr/bin/env python3
"""Documentary integrity for the learning/selection composition.

This checks existing successful Lean evidence; it does not substitute for the
fresh compiler run, philosophical review or empirical correspondence.
"""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
FORMAL = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism"
RECORD = ROOT / "theories/becoming/results/records/learned-procedure-transmission.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pointer(document, address):
    for key in address.strip("/").split("/"):
        key = key.replace("~1", "/").replace("~0", "~")
        document = document[int(key)] if isinstance(document, list) else document[key]
    return document


def anchors(path):
    found = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', path.read_text()))
    counts = {}
    for line in path.read_text().splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", match[1]).lower()
        slug = "".join(c for c in title if c.isalnum() or c in " -_").replace(" ", "-")
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        found.add(slug + ("-" + str(n) if n else ""))
    return found


def main():
    record = json.loads(RECORD.read_text())
    checked = []
    for reference in record["references"]:
        path = ROOT / reference["path"]
        assert sha(path) == reference["sha256"], ("record source drift", str(path))
        checked.append(reference["path"])
    for binding in record["proof_bindings"]:
        receipt = json.loads((ROOT / binding["receipt"]).read_text())
        assert pointer(receipt, binding["success_pointer"]) == binding["success_value"]
        assert pointer(receipt, binding["sha256_pointer"]) == sha(ROOT / binding["source"])

    receipt_path = FORMAL / "learned-procedure-transmission-verification.json"
    receipt = json.loads(receipt_path.read_text())
    assert receipt["status"] == "passed"
    assert not receipt["source_changed_during_run"]
    snapshot = ROOT / receipt["snapshot"]
    assert json.loads((snapshot / "verification.json").read_text()) == receipt
    for module in receipt["modules"]:
        assert sha(ROOT / module["source"]) == module["source_sha256"]
        assert sha(snapshot / "sources" / (module["module"] + ".lean")) == module["source_sha256"]
    for name, digest in receipt["log_sha256"].items():
        assert sha(snapshot / name) == digest, name
    checker = FORMAL / "check_learned_procedure_transmission.py"
    assert sha(checker) == receipt["checker_sha256"]
    assert sha(snapshot / checker.name) == receipt["checker_sha256"]
    assert sha(snapshot / "lake-manifest.json") == receipt["manifest_sha256"]

    markdown = [ROOT / name for name in checked if name.endswith(".md")]
    markdown += [ROOT / "sources/15-codex-theory-conversations/2026-10-09-learning-recursive-selection.md"]
    links = []
    for path in dict.fromkeys(markdown):
        for raw in re.findall(r"(?<!!)\[[^\]]*\]\(([^\s)]+)\)", path.read_text()):
            if re.match(r"^[a-zA-Z]+:", raw):
                continue
            name, _, fragment = unquote(raw).partition("#")
            target = (path.parent / name).resolve() if name else path
            assert target.is_file(), (str(path), raw)
            if fragment and target.suffix == ".md":
                assert fragment in anchors(target), (str(path), raw)
            links.append({"source": str(path.relative_to(ROOT)), "target": raw})

    output = {
        "status": "passed",
        "scope": "Owned documentary sources, local links, current/frozen compiler evidence and hashes; no new proof or empirical run by this script.",
        "record": str(RECORD.relative_to(ROOT)),
        "record_sha256": sha(RECORD),
        "source_hashes": {name: sha(ROOT / name) for name in checked},
        "receipt": str(receipt_path.relative_to(ROOT)),
        "receipt_sha256": sha(receipt_path),
        "snapshot": receipt["snapshot"],
        "new_theorems": receipt["new_theorems"],
        "new_audits": receipt["new_audits"],
        "inherited_audits": receipt["total_audits"] - receipt["new_audits"],
        "links_checked": len(links),
        "links": links,
        "checker_sha256": sha(Path(__file__)),
    }
    (HERE / "LEARNING-SELECTION-CHECKS.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: output[key] for key in ["status", "new_theorems", "new_audits", "inherited_audits", "links_checked"]}))


if __name__ == "__main__":
    main()
