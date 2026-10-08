#!/usr/bin/env python3
"""Check this continuation's documentary integrity, not its ethical truth."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
spec = importlib.util.spec_from_file_location("chain", BASE / "build_generative_chain.py")
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)


def main():
    report_path = BASE / "CONCERN-DEVELOPMENT-WALL-CHECKS.json"
    report_path.touch(exist_ok=True)
    edits = json.loads((BASE / "CONCERN-DEVELOPMENT-WALL-INDEX-EDITS.json").read_text())
    errors, links, prefixes = [], [], {}

    def check_links(path, content):
        for reference in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in reference:
                continue
            name, _, fragment = unquote(reference).partition("#")
            target = (path.parent / name).resolve() if name else path.resolve()
            if not target.is_file():
                errors.append(f"Missing file from {path.relative_to(ROOT)}: {reference}")
            elif fragment and target.suffix == ".md" and fragment not in chain.heading_ids(target):
                errors.append(f"Missing anchor from {path.relative_to(ROOT)}: {reference}")
            links.append({"source": str(path.relative_to(ROOT)), "reference": reference})

    for name, baseline in edits["baseline_prefixes"].items():
        path = ROOT / name
        prefix = path.read_bytes()[:baseline["byte_length"]]
        prefixes[name] = hashlib.sha256(prefix).hexdigest() == baseline["sha256"]
        if not prefixes[name]:
            errors.append("Earlier checked prefix changed: " + name)
        check_links(path, path.read_text())
    for item in edits["navigation"]:
        path = ROOT / item["path"]
        if item["inserted"] not in path.read_text():
            errors.append("Owned insertion missing: " + item["path"])
        check_links(path, item["inserted"])

    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    expected = edits["entry_after"]
    retained = all(entry[key].startswith(value) for key, value in expected.items()
                   if isinstance(value, str))
    retained = retained and entry["links"][:len(expected["links"])] == expected["links"]
    if not retained:
        errors.append("Owned M20 content changed; inspect before reconciliation")
    canonical = next(x for x in chain.render(data).splitlines() if x.startswith("| M20 |"))
    actual = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| M20 |"))
    if actual != canonical:
        errors.append("M20 differs from canonical rendering")
    for name in edits["reviewed_owned_sources"]:
        if chain.digest(ROOT / name) != data["reviewed_sources"][name]:
            errors.append("Owned source version changed: " + name)

    direction = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md"
    accepted = chain.digest(direction) == "9940ead2d7f06a18ff7f2ec37f27aebd496dde10854d8a11993469a31a7900cd"
    if not accepted:
        errors.append("Accepted direction bytes changed")
    source = ROOT / "sources/15-codex-theory-conversations/2026-10-08-generative-alignment-priority.md"
    latest = source.read_text().split('<a id="continue-until-developmental-wall"></a>', 1)[1]
    if "\n> 继续，直到你hit a wall\n" not in latest:
        errors.append("Latest exact user quotation missing")

    report = {
        "status": "passed" if not errors else "failed",
        "scope": "Documentary consistency only; no ethical proof, empirical validation or independent acceptance.",
        "errors": errors,
        "earlier_prefixes_preserved": prefixes,
        "owned_M20_retained": retained,
        "M20_canonical": canonical == actual,
        "accepted_alignment_direction_preserved": accepted,
        "local_links_checked": len(links),
        "links": links,
        "owned_source_sha256": {p: chain.digest(ROOT / p) for p in edits["reviewed_owned_sources"]},
        "checker_sha256": chain.digest(Path(__file__)),
        "pending_shared_reviews_not_certified": chain.changes(data),
        "global_schema_link_errors_not_full_freshness": chain.validate(data),
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "links": len(links), "prefixes": prefixes,
                      "canonical_M20": canonical == actual, "errors": errors}, ensure_ascii=False))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
