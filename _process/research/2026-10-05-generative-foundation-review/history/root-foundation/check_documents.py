"""Record document integrity and provenance without revising historical results."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+"\n")


original_hash = "91efaed68a9746e8213437a810a6bb9b0864a572467a9956010fe2711cb92460"
assert digest(PACKAGE/"FOUNDATION-ALTERNATIVE-ORIGINAL.md") == original_hash
for name in ("DOCUMENT-CHECKS.json", "MANIFEST.json"):
    if not (HERE/name).exists():
        write_json(HERE/name, {})


def inspect(path):
    text = path.read_text()
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    display = [text.count("\\["), text.count("\\]")]
    inline = [text.count("\\("), text.count("\\)")]
    placeholders = re.findall(r"\b(?:TODO|TBD|FIXME)\b", text)
    links, errors = [], []
    if display[0] != display[1] or inline[0] != inline[1] or len(tags) != len(set(tags)) or placeholders:
        errors.append({"file":path.name,"error":"delimiter, equation identifier, or placeholder"})
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)",text):
        if re.match(r"[a-zA-Z]+:",target) or target.startswith("#"):
            continue
        local = unquote(target.split("#",1)[0]).strip("<>")
        local = re.sub(r":\d+(?::\d+)?$","",local)
        exists = (path.parent/local).resolve().exists()
        links.append({"file":path.name,"target":target,"exists":exists})
        if not exists:
            errors.append({"file":path.name,"missing":target})
    document = {"file":path.name,"sha256":digest(path),"words":len(text.split()),
        "lines":len(text.splitlines()),"equation_tags":tags,"unique_tags":len(tags)==len(set(tags)),
        "display_delimiters":display,"inline_delimiters":inline,"placeholders":placeholders}
    return document,links,errors


documents,links,errors = [],[],[]
for path in sorted(HERE.glob("*.md")):
    d,l,e = inspect(path)
    documents.append(d)
    links.extend(l)
    errors.extend(e)
exact = json.loads((HERE/"EXACT-CHECKS.json").read_text())
assert exact["status"] == "passed" and exact["check_groups"] == 28
report = {"date":"2026-10-05","primary":"ROOT-FOUNDATION.md",
    "scope":"Document integrity and constructed examples; not empirical validation or general proof certification.",
    "documents":documents,"local_links":links,"errors":errors,
    "original_preserved_sha256":original_hash,"exact_check_groups_passed":exact["check_groups"],
    "exact_check_record":"EXACT-CHECKS.json","analytic_figure_checks":"FIGURE-CHECKS.json",
    "figure_visually_inspected":True,"full_document_render_audit":False,
    "review_scope":"Three internal AI cross-reviews with reported scope corrections resolved; no human peer review or novelty certification.",
    "new_empirical_validation":False}
write_json(HERE/"DOCUMENT-CHECKS.json",report)
assert not errors,errors

inputs = [PACKAGE/"OPTIMAL-FOUNDATION.md",PACKAGE/"FOUNDATION.md",
          PACKAGE/"FOUNDATION-ALTERNATIVE-ORIGINAL.md",
          PACKAGE/"final-synthesis/INTEGRATED-THEORY.md",
          PACKAGE/"final-synthesis/ADAPTIVE-OPTIMUM.md"]
manifest = {"date":"2026-10-05","title":"The root of alignment as continuing realizability",
    "primary":"ROOT-FOUNDATION.md","status":"Conditional mathematical development with resolved internal cross-reviews and constructed checks.",
    "hash_algorithm":"SHA-256","self_hash_excluded":True,
    "files":[{"path":p.name,"sha256":digest(p),"bytes":p.stat().st_size}
             for p in sorted(HERE.iterdir()) if p.is_file() and p.name!="MANIFEST.json"],
    "inputs":[{"path":str(p),"sha256":digest(p),"bytes":p.stat().st_size} for p in inputs]}
write_json(HERE/"MANIFEST.json",manifest)

# Refresh only the changed entry document and add the new package status.
old_checks = json.loads((PACKAGE/"DOCUMENT-CHECKS.json").read_text())
review_doc,review_links,review_errors = inspect(PACKAGE/"REVIEW.md")
assert not review_errors,review_errors
old_checks["documents"] = [d for d in old_checks["documents"] if d["file"]!="REVIEW.md"]+[review_doc]
if "local_links" in old_checks:
    old_checks["local_links"] = [l for l in old_checks["local_links"] if l.get("file")!="REVIEW.md"]+review_links
old_checks["root_foundation"] = {"file":"root-foundation/ROOT-FOUNDATION.md",
    "checks":"root-foundation/DOCUMENT-CHECKS.json","exact_check_groups_passed":28,
    "review_scope":report["review_scope"],"new_empirical_validation":False}
write_json(PACKAGE/"DOCUMENT-CHECKS.json",old_checks)
old_manifest = json.loads((PACKAGE/"MANIFEST.json").read_text())
old_manifest["root_foundation"] = "root-foundation/ROOT-FOUNDATION.md"
old_manifest["root_status"] = manifest["status"]
old_manifest["package_files"] = [{"path":str(p.relative_to(PACKAGE)),"sha256":digest(p),"bytes":p.stat().st_size}
    for p in sorted(PACKAGE.rglob("*")) if p.is_file() and p!=PACKAGE/"MANIFEST.json" and "__pycache__" not in p.parts]
write_json(PACKAGE/"MANIFEST.json",old_manifest)
print(json.dumps({"documents":len(documents),"local_links":len(links),"errors":len(errors),
                  "exact_check_groups_passed":28,"original_preserved":True}))
