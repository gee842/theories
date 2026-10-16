"""Check owned document integration and preservation; does not rerun science."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
checks = []


def check(label, condition):
    checks.append({"check": label, "passed": bool(condition)})


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_links(path, text):
    for target in re.findall(r"\]\(([^\n)]+)\)", text):
        target = target.strip("<>")
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        name, _, anchor = target.partition("#")
        destination = (path.parent / unquote(name)).resolve() if name else path
        check(f"link {path.relative_to(ROOT)} -> {target}", destination.is_file())
        if anchor and destination.is_file() and destination.suffix == ".md":
            headings = re.findall(r"^#{1,6}\s+(.+)$", destination.read_text(), re.M)
            slugs = [re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings]
            check(f"anchor {target}", unquote(anchor) in slugs)


for manifest in ("RECIPE-GROUNDING-PRESERVATION.json", "RECIPE-GROUNDING-EVIDENCE.json"):
    data = json.loads((HERE / manifest).read_text())
    for relative, expected in data["sha256"].items():
        path = ROOT / relative
        check(f"preserve {relative}", path.is_file() and digest(path) == expected)

integration = json.loads((HERE / "RECIPE-GROUNDING-DOC-EDITS.json").read_text())
for relative in integration["owned_documents"]:
    path = ROOT / relative
    check(f"document {relative}", path.is_file())
    if path.is_file():
        check_links(path, path.read_text())
for entry in integration["insertions"]:
    path = ROOT / entry["path"]
    check(f"owned insertion {entry['path']}", path.read_text().count(entry["text"]) == 1)
    check_links(path, entry["text"])

report = {
    "scope": "Owned links, inserted prose and accepted evidence preservation only; no scientific rerun or new proof.",
    "passed": all(item["passed"] for item in checks),
    "count": len(checks),
    "checks": checks,
}
(HERE / "RECIPE-GROUNDING-CHECKS.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"passed": report["passed"], "checks": len(checks),
                  "failures": [item for item in checks if not item["passed"]]}, indent=2))
raise SystemExit(0 if report["passed"] else 1)
