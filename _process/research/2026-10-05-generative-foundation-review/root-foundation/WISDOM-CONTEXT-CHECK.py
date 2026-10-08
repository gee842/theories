#!/usr/bin/env python3
"""Bind the owned wisdom study to checked proofs, links and paired index rows.

Documentary verification only. Does not rerun Lean or certify concurrent work.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/deeper"
OUTPUT = HERE / "WISDOM-CONTEXT-CHECKS.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "WISDOM-CONTEXT-INDEX-EDITS.json").read_text())
    pointer = json.loads((LEAN / "contextual-wisdom-verification.json").read_text())
    receipt_path = ROOT / pointer["receipt"]
    receipt = json.loads(receipt_path.read_text())
    checks = []

    def check(label, condition):
        checks.append({"check": label, "passed": bool(condition)})

    check("successful Lean receipt and fifty audited declarations",
          receipt["passed"] and receipt["total_audits"] == 50
          and receipt["total_empty_axiom_audits"] == 44
          and receipt["total_standard_dependency_audits"] == 6)
    for module in receipt["modules"]:
        live = ROOT / module["source"]
        frozen = receipt_path.parent / "sources" / live.name
        check("live/frozen source " + live.name,
              sha(live) == sha(frozen) == module["sha256"])
        log = (receipt_path.parent / (live.stem + ".log")).read_text()
        empty = re.findall(r"'([^']+)' does not depend on any axioms", log)
        standard = {name: [x.strip() for x in body.split(",") if x.strip()]
                    for name, body in re.findall(
                        r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        check("reported dependency binding " + live.name,
              empty == module["empty_axiom_audits"]
              and standard == module["standard_dependency_audits"]
              and "sorryAx" not in log and "error:" not in log)
    check("checker source preserved",
          sha(LEAN / "check_contextual_wisdom.py")
          == sha(receipt_path.parent / "check_contextual_wisdom.py")
          == receipt["checker_sha256"])
    source = (LEAN / "ContextualWisdom.lean").read_text()
    check("eleven declared and audited new theorems",
          len(re.findall(r"^theorem ", source, re.M)) == 11
          and len(re.findall(r"^#print axioms ", source, re.M)) == 11)

    data = chain.read_data()
    entries = {e["id"]: e for section in data["sections"] for e in section["entries"]}
    canonical = chain.render(data).splitlines()
    actual = chain.OUTPUT.read_text().splitlines()
    for eid in edits["owned_ids"]:
        # Permit later additive work while requiring all this study's content.
        owned = edits["entries"][eid]["after"]
        current = entries[eid]
        check("owned bilingual content retained " + eid,
              all(owned[field] in current[field]
                  for field in ["claim_zh", "claim_en", "scope_zh", "scope_en"])
              and all(link in current["links"] for link in owned["links"]))
        prefix = "| " + eid + " |"
        check("canonical rendered row " + eid,
              [x for x in actual if x.startswith(prefix)]
              == [x for x in canonical if x.startswith(prefix)])
    for name in edits["reviewed_owned_sources"]:
        check("reviewed owned source " + name,
              sha(ROOT / name) == data["reviewed_sources"].get(name))
    check("only owned discovery pages recorded",
          all(p in data["known_discovery_paths"] for p in edits["owned_discovery_added"]))
    check("prior entries and table lines preserved at mutation",
          edits["other_entries_unchanged"] and edits["other_table_lines_unchanged"])
    nav = json.loads((HERE / "WISDOM-CONTEXT-NAVIGATION-EDITS.json").read_text())
    for insertion in nav:
        check("owned navigation retained " + insertion["path"],
              insertion["insertion"] in (ROOT / insertion["path"]).read_text()
              and insertion["all_prior_bytes_preserved"])

    link_count = 0
    for name in edits["reviewed_owned_sources"]:
        path = ROOT / name
        if path.suffix != ".md":
            continue
        for ref in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if re.match(r"[a-z]+://", ref):
                continue
            local, _, fragment = unquote(ref).partition("#")
            target = (path.parent / local).resolve() if local else path
            exists = target.exists() or target == OUTPUT
            valid_anchor = not fragment or (exists and fragment in chain.heading_ids(target))
            check("local link " + name + " -> " + ref, exists and valid_anchor)
            link_count += 1
    report = {"scope": "owned study, direct proof bindings and M15/F01; not whole-table freshness",
              "passed": all(c["passed"] for c in checks),
              "checks": checks, "local_links_checked": link_count,
              "concurrent_index_changes": chain.changes(data),
              "lean_receipt": pointer["receipt"]}
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"passed": report["passed"], "checks": len(checks),
                      "local_links": link_count,
                      "pending_source_reviews": len(report["concurrent_index_changes"]["modified_sources"]),
                      "pending_discovery_pages": len(report["concurrent_index_changes"]["new_pages"]),
                      "failures": [c for c in checks if not c["passed"]]}, ensure_ascii=False))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
