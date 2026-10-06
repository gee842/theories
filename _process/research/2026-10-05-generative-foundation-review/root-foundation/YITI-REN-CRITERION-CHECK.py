"""Check integration, owned edits and existing verification bindings; no rerun."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
FORMAL = ROOT / "experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern"
NATIVE = ROOT / ("experiments/shared-renewal-capability/regulation/retention/formation/"
                 "learning-interface/recording/continuing-dependency")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_hash(path):
    return digest(path.read_bytes())


def anchors(path):
    counts, out = {}, set()
    for line in path.read_text().splitlines():
        m = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if m:
            slug = "".join(c for c in m[1].lower().replace("`", "")
                           if c.isalnum() or c in "_ -").replace(" ", "-")
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            out.add(slug + (f"-{count}" if count else ""))
    return out


def main():
    ledger = json.loads((HERE / "YITI-REN-CRITERION-EDITS.json").read_text())
    edits, new_files = ledger["edits"], ledger["new_files"]
    errors, links, recovery, bindings = [], [], [], []
    texts = [(e["path"], e["new"]) for e in edits]
    texts += [(p, (ROOT / p).read_text()) for p in new_files if p.endswith(".md")]
    seen = set()
    for source, text in texts:
        for link in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
            u = urlsplit(link.strip("<>"))
            if u.scheme or link.startswith("//") or (source, link) in seen:
                continue
            seen.add((source, link))
            target = (ROOT / source).parent / unquote(u.path) if u.path else ROOT / source
            valid = target.is_file()
            if valid and u.fragment:
                valid = unquote(u.fragment) in anchors(target)
            links.append(dict(source=source, target=link, valid=valid))
            if not valid:
                errors.append(["link", source, link])
        if any(line.rstrip() != line for line in text.splitlines()):
            errors.append(["owned_whitespace", source])
    for path in sorted({e["path"] for e in edits}):
        current = (ROOT / path).read_text()
        reverse = current
        owned = [e for e in edits if e["path"] == path]
        valid = True
        for e in reversed(owned):
            if reverse.count(e["new"]) != 1:
                valid = False
                break
            reverse = reverse.replace(e["new"], e["old"], 1)
        recovery.append(dict(path=path, reversible_owned_fragments=valid,
                             baseline_matches=valid and digest(reverse.encode()) == owned[0]["baseline_sha256"]))
        if not valid:
            errors.append(["owned_fragment", path])
    first = edits[0]
    source_bytes = (ROOT / first["path"]).read_bytes()
    prefix_preserved = digest(source_bytes[:first["baseline_bytes"]]) == first["baseline_sha256"]
    if not prefix_preserved:
        errors.append(["source_prefix"])

    def bind(path, expected, label):
        valid = path.is_file() and file_hash(path) == expected
        bindings.append(dict(label=label, path=str(path), valid=valid))
        if not valid:
            errors.append(["binding", label, str(path)])

    result_path = NATIVE / "criterion-results.json"
    independent_path = NATIVE / "criterion-independent-check.json"
    proof_path = FORMAL / "criterion-verification.json"
    result, independent, proof = [json.loads(p.read_text()) for p in
                                  (result_path, independent_path, proof_path)]
    for name, receipt in (("native", result), ("independent", independent), ("formal", proof)):
        if receipt["status"] != "passed":
            errors.append(["receipt_status", name])
    for name, receipt, key in (("native", result, "source_hashes"),
                               ("independent", independent, "source_hashes"),
                               ("formal", proof, "native_source_bindings")):
        for path, sha in receipt[key].items():
            bind(ROOT / path, sha, name)
    bind(result_path, independent["producer_result_sha256"], "independent result")
    bind(NATIVE / "criterion_independent_check.py", independent["checker_sha256"], "independent checker")
    bind(ROOT / proof["native_results"], proof["native_results_sha256"], "formal native result")
    bind(Path(proof["compiler"]), proof["compiler_sha256"], "compiler")
    bind(FORMAL / "check_criterion.py", proof["checker_sha256"], "formal checker")
    bind(FORMAL / "check_purpose.py", proof["checker_helper_sha256"], "formal checker helper")
    for module in proof["modules"]:
        bind(ROOT / module["source"], module["sha256"], module["module"] + " source")
        bind(FORMAL / module["log"], module["log_sha256"], module["module"] + " log")
    files = sorted({e["path"] for e in edits} | set(new_files))
    record = dict(status="failed" if errors else "passed",
        checked_at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=file_hash(Path(__file__)),
        files={p: file_hash(ROOT / p) for p in files}, links=links,
        owned_edits=len(edits), edit_recovery=recovery, source_prefix_preserved=prefix_preserved,
        verification_bindings=bindings, receipts={str(p.relative_to(ROOT)): file_hash(p)
            for p in (result_path, independent_path, proof_path)},
        scope="Owned-fragment, local-link and saved verification binding check; no new scientific or compiler run.",
        recovery_scope="In-memory only; concurrent edits outside owned fragments are preserved and may change whole-file baseline hashes.",
        universal_proof_completed=False, errors=errors)
    (HERE / "YITI-REN-CRITERION-CHECKS.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(status=record["status"], files=len(files), links=len(links),
        owned_edits=len(edits), bindings=len(bindings), source_prefix_preserved=prefix_preserved,
        matched_baselines=sum(r["baseline_matches"] for r in recovery), errors=errors), ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
