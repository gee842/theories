#!/usr/bin/env python3
"""Check this round's owned texts and bindings to its actual Lean run."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = HERE / "LIANGZHI-DEVELOPMENT-EDITS.json"
OUTPUT = HERE / "LIANGZHI-DEVELOPMENT-CHECKS.json"
PACKAGE = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/evolution/development"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(text):
    text = re.sub(r"[`*_]", "", text.lower())
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s", "-", text.strip())


ledger = json.loads(LEDGER.read_text())
checks = []
link_count = 0


def check(name, ok, detail=None):
    checks.append({"name": name, "passed": bool(ok), "detail": detail})


def links(path, text):
    global link_count
    for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
        target = target.strip("<>")
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        link_count += 1
        raw, _, fragment = target.partition("#")
        destination = (path.parent / unquote(raw)).resolve() if raw else path
        ok = destination.exists()
        if ok and fragment and destination.suffix == ".md":
            content = destination.read_text()
            anchors = {slug(h) for h in re.findall(r"^#{1,6}\s+(.+)$", content, re.M)}
            anchors.update(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)', content))
            ok = unquote(fragment) in anchors
        check("local_link", ok, {"from": str(path.relative_to(ROOT)), "target": target})


for entry in ledger["insertions"]:
    path = ROOT / entry["path"]
    check("owned_shared_fragment", path.read_text().count(entry["text"]) == 1, entry["path"])
    links(path, entry["text"])

for entry in ledger["owned_files"]:
    path = ROOT / entry["path"]
    check("owned_file_hash", path.exists() and digest(path) == entry["sha256"], entry["path"])
    if path.suffix == ".md":
        links(path, path.read_text())

receipt = json.loads((PACKAGE / "verification.json").read_text())
check("lean_passed_fresh_build", receipt["status"] == "passed"
      and receipt["fresh_temporary_build"] and receipt["inputs_unchanged"])
check("compiler_binding", digest(Path(receipt["compiler"])) == receipt["compiler_sha256"])
check("lean_checker_binding", digest(PACKAGE / "check.py") == receipt["checker_sha256"])
audits, new_audits = {}, {}
for module in receipt["modules"]:
    check("lean_source_binding", digest(ROOT / module["source"]) == module["sha256"], module["module"])
    check("lean_log_binding", digest(PACKAGE / module["log"]) == module["log_sha256"], module["module"])
    check("lean_module_passed", module["passed"] and module["exit_code"] == 0, module["module"])
    audits.update(module["axioms_by_declaration"])
    if module["new"]:
        new_audits.update(module["axioms_by_declaration"])
expected = ledger["expected_audits"]
check("audit_counts", len(audits) == expected["total"] and len(new_audits) == expected["new"]
      and sum(not deps for deps in new_audits.values()) == expected["new_empty"])
check("new_dependencies", sorted({d for ds in new_audits.values() for d in ds}) == expected["new_dependencies"])

result = {
    "status": "passed" if all(c["passed"] for c in checks) else "failed",
    "scope": "Exact owned fragments, hashes, local links and bindings to the completed Lean run. This is not another proof or empirical run.",
    "ledger_sha256": digest(LEDGER),
    "checker_sha256": digest(Path(__file__)),
    "local_links_checked": link_count,
    "checks": checks,
}
OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"status": result["status"], "checks": len(checks),
                  "local_links_checked": link_count,
                  "failures": [c for c in checks if not c["passed"]]}, ensure_ascii=False))
sys.exit(result["status"] != "passed")
