"""Check the saved synthesis and refresh its integrity/provenance records."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


original_hash = "91efaed68a9746e8213437a810a6bb9b0864a572467a9956010fe2711cb92460"
assert digest(PACKAGE / "FOUNDATION-ALTERNATIVE-ORIGINAL.md") == original_hash
for name in ("DOCUMENT-CHECKS.json", "MANIFEST.json"):
    if not (HERE / name).exists():
        write_json(HERE / name, {})

documents, links, errors = [], [], []
for path in sorted(HERE.glob("*.md")):
    text = path.read_text()
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    display = [text.count("\\["), text.count("\\]")]
    inline = [text.count("\\("), text.count("\\)")]
    placeholders = re.findall(r"\b(?:TODO|TBD|FIXME)\b", text)
    if display[0] != display[1] or inline[0] != inline[1] or len(tags) != len(set(tags)) or placeholders:
        errors.append({"file": path.name, "error": "delimiter, tag, or placeholder check"})
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"[a-zA-Z]+:", target) or target.startswith("#"):
            continue
        local = unquote(target.split("#", 1)[0]).strip("<>")
        local = re.sub(r":\d+(?::\d+)?$", "", local)
        resolved = (path.parent / local).resolve()
        exists = resolved.exists()
        links.append({"file": path.name, "target": target, "exists": exists})
        if not exists:
            errors.append({"file": path.name, "missing": target})
    documents.append({"file": path.name, "sha256": digest(path), "words": len(text.split()), "lines": len(text.splitlines()), "equation_tags": tags, "unique_tags": len(tags) == len(set(tags)), "display_delimiters": display, "inline_delimiters": inline, "placeholders": placeholders})

report = {"date": "2026-10-05", "primary": "INTEGRATED-THEORY.md", "scope": "Document integrity and checked constructed examples; not empirical validation or proof certification.", "documents": documents, "local_links": links, "errors": errors, "original_preserved_sha256": original_hash, "exact_checks": json.loads((HERE / "EXACT-CHECKS.json").read_text()), "numerical_checks": "NUMERICAL-CHECKS.json", "figure_visually_inspected": True, "full_document_render_audit": False, "review_scope": "Resolved integration cross-review plus mathematical author audit; no completed independent full proof audit or human peer review."}
write_json(HERE / "DOCUMENT-CHECKS.json", report)
assert not errors, errors

input_paths = [PACKAGE / "OPTIMAL-FOUNDATION.md", PACKAGE / "FOUNDATION.md", PACKAGE / "FOUNDATION-ALTERNATIVE-ORIGINAL.md", PACKAGE.parent / "2026-10-04-integrated-evolution/practice-transmission-model.md", PACKAGE.parent / "2026-10-04-integrated-evolution/endogenous-renewal-math.md", PACKAGE.parents[2] / "experiments/integrated-correction/general-framework/reproduction-test/README.md", PACKAGE.parents[2] / "experiments/integrated-correction/general-framework/reproduction-test/design/DESIGN.md"]
assert all(p.exists() for p in input_paths)
manifest = {"date": "2026-10-05", "title": "Integrated theory and four remaining tasks", "primary": "INTEGRATED-THEORY.md", "status": "Conditional mathematical synthesis, constructed checks, and unrun empirical validation specification.", "hash_algorithm": "SHA-256", "self_hash_excluded": True, "files": [{"path": p.name, "sha256": digest(p), "bytes": p.stat().st_size} for p in sorted(HERE.iterdir()) if p.is_file() and p.name != "MANIFEST.json"], "inputs": [{"path": str(p), "sha256": digest(p), "bytes": p.stat().st_size} for p in input_paths]}
write_json(HERE / "MANIFEST.json", manifest)

old_checks = json.loads((PACKAGE / "DOCUMENT-CHECKS.json").read_text())
old_checks["integrated_synthesis"] = {"file": "final-synthesis/INTEGRATED-THEORY.md", "checks": "final-synthesis/DOCUMENT-CHECKS.json", "exact_checks_passed": report["exact_checks"]["passed"], "empirical_validation": "unrun", "review_scope": report["review_scope"]}
write_json(PACKAGE / "DOCUMENT-CHECKS.json", old_checks)
old_manifest = json.loads((PACKAGE / "MANIFEST.json").read_text())
old_manifest["integrated_synthesis"] = "final-synthesis/INTEGRATED-THEORY.md"
old_manifest["integrated_status"] = manifest["status"]
old_manifest["package_files"] = [{"path": str(p.relative_to(PACKAGE)), "sha256": digest(p), "bytes": p.stat().st_size} for p in sorted(PACKAGE.rglob("*")) if p.is_file() and p != PACKAGE / "MANIFEST.json" and "__pycache__" not in p.parts]
write_json(PACKAGE / "MANIFEST.json", old_manifest)
print(json.dumps({"documents": len(documents), "local_links": len(links), "errors": len(errors), "exact_checks_passed": report["exact_checks"]["passed"], "original_preserved": True}))
