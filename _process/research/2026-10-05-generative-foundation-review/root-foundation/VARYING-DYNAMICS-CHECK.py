#!/usr/bin/env python3
"""Check this integration's links and frozen proof evidence, without rerunning Lean."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PACKAGE = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity"
ANALYSIS = PACKAGE / "analysis"
THEORY = REPO / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"
DOCS = [
    HERE / "VARYING-DYNAMICS-INTEGRATION.md",
    HERE / "VARYING-DYNAMICS-MECHANISM.md",
    HERE / "VARYING-DYNAMICS-REVIEW.md",
    HERE / "SYSTEMS-HIGHER-DYNAMICS.md",
    THEORY / "SYSTEMS-COMPLEXITY-CHAOS.md",
    PACKAGE / "README.md",
    REPO / "sources/15-codex-theory-conversations/2026-10-06-systems-complexity-chaos-integration.md",
]
INDEXES = {
    REPO / "RESEARCH.md": "**Recurrent revision and regulation completed locally,",
    REPO / "theories/shengsheng-buxi-generative-existence/README.md": "**Recurrent revision and regulation now formalized,",
    THEORY / "GENERATIVE-GROUNDING.md": "**Recurrent revision → supported regulation,",
    HERE / "README.md": "**Recurrent dynamics completed locally,",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    found = set()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", path.read_text(), re.M):
        heading = re.sub(r"[^\w\s-]", "", heading.lower())
        found.add(re.sub(r"\s", "-", heading))
    return found


def main():
    failures = []
    checked_links = 0
    for path in DOCS + list(INDEXES):
        source = path.read_text()
        if path in INDEXES:
            lines = [line for line in source.splitlines() if line.startswith(INDEXES[path])]
            if len(lines) != 1:
                failures.append(f"Missing or duplicate integration index: {path}")
            source = "\n".join(lines)
        for raw in re.findall(r"\]\(([^)]+)\)", source):
            if raw.startswith(("https://", "http://", "mailto:")):
                continue
            raw = unquote(raw.strip("<>"))
            target, _, anchor = raw.partition("#")
            resolved = (path.parent / target).resolve() if target else path
            checked_links += 1
            if not resolved.exists():
                failures.append(f"Missing link {path.relative_to(REPO)}: {raw}")
            elif anchor and resolved.suffix == ".md" and anchor not in anchors(resolved):
                failures.append(f"Missing anchor {path.relative_to(REPO)}: {raw}")

    receipt_path = ANALYSIS / "adaptive-verification.json"
    receipt = json.loads(receipt_path.read_text())
    if receipt["status"] != "passed" or not receipt["inputs_unchanged"]:
        failures.append("Combined fresh proof receipt is not an unchanged-input pass")
    if receipt["new_audits"] != 58 or receipt["replayed_inherited_audits"] != 143:
        failures.append("Unexpected theorem accounting")
    current_sources = {
        "GenerativeCore": PACKAGE.parent / "GenerativeCore.lean",
        "ResourceContinuation": PACKAGE.parent / "conditional/ResourceContinuation.lean",
        **{n: PACKAGE / f"{n}.lean" for n in
           ["SystemsOrganization", "FeedbackDynamics", "SymbolicDynamics", "SystemsComplexity"]},
        **{n: ANALYSIS / f"{n}.lean" for n in
           ["RealFeedback", "AdaptiveCore", "VaryingFeedback", "ShrinkingGain", "SupportedRevision"]},
    }
    for module in receipt["modules"]:
        name = module["module"]
        for path in [current_sources[name], ANALYSIS / "adaptive-verification/sources" / f"{name}.lean"]:
            if sha(path) != module["source_sha256"]:
                failures.append(f"Changed proof source: {path}")
        if sha(ANALYSIS / "adaptive-verification" / f"{name}.txt") != module["output_sha256"]:
            failures.append(f"Changed proof log: {name}")
    if sha(ANALYSIS / "check_adaptive.py") != receipt["checker_sha256"]:
        failures.append("Changed adaptive checker")
    if sha(ANALYSIS / "lean-toolchain") != receipt["toolchain_sha256"]:
        failures.append("Changed analytic toolchain")
    inherited = json.loads((ANALYSIS / "verification.json").read_text())
    for module in inherited["modules"]:
        if sha(current_sources[module["module"]]) != module["source_sha256"]:
            failures.append(f"Prior analytic source changed: {module['module']}")
    for parent, filename in [(PACKAGE, "check.py"), (ANALYSIS, "check.py")]:
        old = json.loads((parent / "verification.json").read_text())
        if sha(parent / filename) != old["checker_sha256"]:
            failures.append(f"Prior checker changed: {parent / filename}")
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if not failures else "failed",
        "scope": "Local Markdown targets/anchors, new index entries, frozen Lean sources/logs/checker and inherited source/checker preservation. No scientific rerun or external URL check.",
        "local_links_checked": checked_links,
        "new_theorem_audits": receipt["new_audits"],
        "replayed_inherited_audits": receipt["replayed_inherited_audits"],
        "proof_receipt_sha256": sha(receipt_path),
        "proof_checked_at_utc": receipt["checked_at_utc"],
        "files": {str(p.relative_to(REPO)): sha(p)
                  for p in DOCS + list(INDEXES) + [Path(__file__).resolve()]},
        "failures": failures,
    }
    (HERE / "VARYING-DYNAMICS-CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "local_links_checked", "failures"]}))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
