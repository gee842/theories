#!/usr/bin/env python3
"""Check owned source preservation and navigation, not empirical or ethical truth."""
import hashlib
import importlib.util
import json
import re
from pathlib import Path
from urllib.parse import unquote

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
spec = importlib.util.spec_from_file_location(
    "chain", BASE.parent / "root-foundation" / "build_generative_chain.py")
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)


def main():
    edits = json.loads((BASE / "MARKET-INTERNET-DEGENERATION-EDITS.json").read_text())
    out = BASE / "MARKET-INTERNET-DEGENERATION-CHECKS.json"
    out.touch(exist_ok=True)
    errors, links, prefixes = [], [], {}

    def check_links(path, text):
        for reference in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in reference:
                continue
            name, _, fragment = unquote(reference).partition("#")
            target = (path.parent / name).resolve() if name else path.resolve()
            if not target.is_file():
                errors.append(f"Missing file: {path.relative_to(ROOT)} -> {reference}")
            elif fragment and target.suffix == ".md" and fragment not in chain.heading_ids(target):
                errors.append(f"Missing anchor: {path.relative_to(ROOT)} -> {reference}")
            links.append({"source": str(path.relative_to(ROOT)), "reference": reference})

    for name, before in edits["baseline_prefixes"].items():
        content = (ROOT / name).read_bytes()
        prefixes[name] = hashlib.sha256(content[:before["byte_length"]]).hexdigest() == before["sha256"]
        if not prefixes[name]:
            errors.append("Earlier content changed: " + name)
        check_links(ROOT / name, content.decode())
    new = ROOT / edits["new_study"]
    check_links(new, new.read_text())
    for item in edits["navigation"]:
        p = ROOT / item["path"]
        if item["inserted"] not in p.read_text():
            errors.append("Missing owned navigation: " + item["path"])
        check_links(p, item["inserted"])

    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    expected = edits["entry_after"]
    retained = all(entry.get(k, "").startswith(v) for k, v in expected.items() if isinstance(v, str))
    retained &= entry["links"][:len(expected["links"])] == expected["links"]
    if not retained:
        errors.append("Owned M20 content changed; reconcile without overwriting concurrent work")
    canonical = next(l for l in chain.render(data).splitlines() if l.startswith("| M20 |"))
    actual = next(l for l in chain.OUTPUT.read_text().splitlines() if l.startswith("| M20 |"))
    if canonical != actual:
        errors.append("M20 is not canonically rendered")
    for name in edits["reviewed_owned_sources"]:
        if chain.digest(ROOT / name) != data["reviewed_sources"].get(name):
            errors.append("Owned reviewed version differs: " + name)
    source = ROOT / "sources/15-codex-theory-conversations/2026-10-08-generative-alignment-priority.md"
    quotation = "> 其实当下的市场和互联网的演化，都能给你足够的验证检验\n> enshitification 其实就是degeneration"
    if quotation not in source.read_text():
        errors.append("Exact user quotation missing")
    direction = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md"
    accepted = chain.digest(direction) == "9940ead2d7f06a18ff7f2ec37f27aebd496dde10854d8a11993469a31a7900cd"
    if not accepted:
        errors.append("Accepted alignment direction changed")
    schema_errors = chain.validate(data)
    report = {
        "status": "passed" if not errors else "failed",
        "scope": "Documentary integrity only; no new proof, experiment, independent acceptance or full-table freshness certification.",
        "errors": errors,
        "earlier_prefixes_preserved": prefixes,
        "owned_M20_retained": retained,
        "M20_canonical": canonical == actual,
        "accepted_alignment_direction_preserved": accepted,
        "local_links_checked": len(links),
        "links": links,
        "owned_source_sha256": {n: chain.digest(ROOT / n) for n in edits["reviewed_owned_sources"]},
        "checker_sha256": chain.digest(Path(__file__)),
        "pending_shared_reviews_not_certified": chain.changes(data),
        "global_schema_link_errors_not_full_freshness": schema_errors,
    }
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "links": len(links), "prefixes_preserved": all(prefixes.values()),
                      "M20_canonical": canonical == actual, "errors": errors,
                      "global_schema_link_errors": schema_errors}, ensure_ascii=False))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
