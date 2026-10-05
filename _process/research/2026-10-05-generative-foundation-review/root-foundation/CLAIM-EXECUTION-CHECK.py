#!/usr/bin/env python3
"""Inspect the saved claim-execution build/review and local links; no reruns."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
PACKAGE = REPO / "experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/protection/claims"
FORMAL = PACKAGE / "formal"
verified = {}


def inspect(path, expected=None):
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert expected is None or digest == expected, str(path)
    verified[str(path.relative_to(REPO))] = digest
    return raw


def main():
    build = json.loads(inspect(FORMAL / "verification.json"))
    assert build["status"] == "passed"
    assert build["fresh_temporary_build"] and build["source_unchanged_during_check"]
    assert build["new_audited_declarations"] == 45
    inspect(FORMAL / "check.py", build["checker_sha256"])
    inspect(FORMAL / "lean-toolchain", build["toolchain_sha256"])
    inherited = json.loads(inspect(PACKAGE.parent / "formal/verification.json"))
    expected_parent = {m["module"]: m["source_sha256"] for m in inherited["modules"]}
    for module in build["modules"]:
        assert module["exit_code"] == 0 and module["clean_dependency_audit"]
        inspect((FORMAL / module["source"]).resolve(), module["source_sha256"])
        inspect(FORMAL / module["output"], module["output_sha256"])
        if module["module"] in expected_parent:
            assert module["source_sha256"] == expected_parent[module["module"]]
    assert len(build["modules"]) == len(expected_parent) + 2
    review = inspect(HERE / "CLAIM-EXECUTION-REVIEW.md").decode()
    assert "**Status: accepted" in review, "Final independent review pending"
    output = HERE / "CLAIM-EXECUTION-INTEGRATION.json"
    documents = [
        HERE / "CLAIM-EXECUTION-MATH.md", HERE / "CLAIM-EXECUTION-REVIEW.md",
        PACKAGE / "README.md", PACKAGE / "PROTOCOL.md",
        REPO / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CLAIMS-AND-PAID-ACTION.md",
    ]
    checked_links = 0
    for path in documents:
        text = inspect(path).decode()
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in link or link.startswith("#"):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            # This check creates its own receipt after all other checks pass.
            assert target == output or target.exists(), (path, link)
            checked_links += 1
    inspect(Path(__file__).resolve())
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed", "new_lean_audits": build["new_audited_declarations"],
        "new_empty_axiom_audits": build["new_empty_axiom_audits"],
        "unchanged_parent_modules": len(expected_parent), "relative_links": checked_links,
        "verified_sha256": verified,
        "scope": "Inspection of fresh Lean receipt, unchanged parent identities, internal review and local file links. No experiment or compiler rerun. Partial-evidence action certificate and temporal protection composition; verification ledger only.",
        "limitations": "Actual-world membership, factual law, chosen action, admitted grounds and permission supplied. No new physical recorder, choice mechanism, concern formation, empirical evidence or complete Python refinement.",
    }
    output.write_text(json.dumps(result, indent=2) + "\n")
    assert output.exists()
    print(json.dumps({k: v for k, v in result.items() if k != "verified_sha256"}, indent=2))


if __name__ == "__main__":
    main()
