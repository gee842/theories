#!/usr/bin/env python3
"""Read-only document and historical-proof binding checks; no compilation."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = HERE / "LIANGZHI-CALIBRATION-EDITS.json"
OUTPUT = HERE / "LIANGZHI-CALIBRATION-CHECKS.json"
checks = []
link_count = 0


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, ok, detail=None):
    checks.append({"name": name, "passed": bool(ok), "detail": detail})


def slug(text):
    text = re.sub(r"[`*_]", "", text.lower())
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s", "-", text.strip())


def links(path, text):
    global link_count
    for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
        target = target.strip("<>")
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        link_count += 1
        raw, _, fragment = target.partition("#")
        dest = (path.parent / unquote(raw)).resolve() if raw else path
        ok = dest.exists()
        if ok and fragment and dest.suffix == ".md":
            content = dest.read_text()
            anchors = {slug(h) for h in re.findall(r"^#{1,6}\s+(.+)$", content, re.M)}
            anchors.update(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)', content))
            ok = unquote(fragment) in anchors
        check("local_link", ok, {"from": str(path.relative_to(ROOT)), "target": target})


ledger = json.loads(LEDGER.read_text())
for entry in ledger["insertions"]:
    path = ROOT / entry["path"]
    check("owned_shared_fragment", path.read_text().count(entry["text"]) == 1, entry["path"])
    links(path, entry["text"])
for entry in ledger["owned_files"]:
    path = ROOT / entry["path"]
    check("owned_file_hash", path.exists() and digest(path) == entry["sha256"], entry["path"])
    if path.suffix == ".md":
        links(path, path.read_text())

module_occurrences = 0
for entry in ledger["inherited_receipts"]:
    path = ROOT / entry["path"]
    check("historical_receipt_binding", digest(path) == entry["sha256"], entry["path"])
    receipt = json.loads(path.read_text())
    check("historical_status", receipt["status"] == "passed", entry["path"])
    compiler = Path(receipt.get("compiler", receipt.get("compiler_binary")))
    check("historical_compiler_binding", digest(compiler) == receipt["compiler_sha256"], entry["path"])
    for module in receipt["modules"]:
        module_occurrences += 1
        src = ROOT / module["source"]
        log = path.parent / module.get("log", module.get("output"))
        check("historical_source_binding", digest(src) == module.get("sha256", module.get("source_sha256")), module["source"])
        check("historical_log_binding", digest(log) == module.get("log_sha256", module.get("output_sha256")), str(log.relative_to(ROOT)))
        check("historical_module_exit", module["exit_code"] == 0, module["module"])
check("historical_module_occurrences", module_occurrences == 11, "3+4+4 includes repeated core; no new modules")

result = {
    "status": "passed" if all(c["passed"] for c in checks) else "failed",
    "scope": "Owned text, links, and read-only source/log/compiler bindings of three prior Lean receipts. No new theorem, compilation or empirical run.",
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
