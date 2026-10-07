#!/usr/bin/env python3
"""Cross-check the proposed window-language reduction against the old game solver.

The 201 candidate languages in the adjacent receipt are explicit supplied
inputs to this comparison. This independently checks correspondence on periods
1--8, not completeness of their enumeration or the arbitrary-period theorem.
No prior scientific receipt is overwritten.
"""
from datetime import datetime, timezone
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "period-reduction-review.json"
SOLVER = HERE / "check_phase_period.py"
GENERAL_LANGUAGES = HERE / "period-general-languages.json"


def complement(mask):
    return sum(1 << (127 - word) for word in range(128) if mask >> word & 1)


def windows(pattern):
    period = len(pattern)
    words = {sum(pattern[(phase + offset) % period] << offset for offset in range(7))
             for phase in range(period)}
    return sum(1 << word for word in words)


def main():
    previous = json.loads(RECEIPT.read_text())
    languages = tuple(previous["language_masks"])
    assert len(languages) == 201 and len(set(languages)) == 201
    assert all(0 <= mask < 2**128 for mask in languages)
    general = json.loads(GENERAL_LANGUAGES.read_text())
    general_masks = {int(mask, 16) for mask in general["seven_commands"]["languages_hex"]}
    assert general_masks == set(languages), "Preserved proposed language family changed"
    flipped = tuple(complement(mask) for mask in languages)
    spec = spec_from_file_location("retained_period_solver_for_review", SOLVER)
    solver = module_from_spec(spec)
    spec.loader.exec_module(solver)
    rows, mismatches = [], []
    for period in range(1, 9):
        checked = 0
        for pattern in product((0, 1), repeat=period):
            required = windows(pattern)
            for target, family in [(0, flipped), (1, languages)]:
                reduced = any(required & mask == required for mask in family)
                original = solver.least_commands(pattern, target, cap=7) is not None
                if reduced != original:
                    mismatches.append({"pattern": list(pattern), "target": target,
                                       "language_accepts": reduced, "old_solver_accepts": original})
                checked += 1
        rows.append({"period": period, "target_comparisons": checked})
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "passed" if not mismatches else "failed",
              "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "original_solver_sha256": sha256(SOLVER.read_bytes()).hexdigest(),
              "proposed_language_source_sha256": sha256(GENERAL_LANGUAGES.read_bytes()).hexdigest(),
              "matches_preserved_general_language_set": True,
              "language_input_provenance": previous["language_input_provenance"],
              "language_masks": list(languages),
              "language_masks_json_sha256": sha256(json.dumps(list(languages)).encode()).hexdigest(),
              "includes_constant_patterns": True, "depth_limit": 7,
              "comparisons": sum(row["target_comparisons"] for row in rows),
              "rows": rows, "mismatches": mismatches,
              "scope": "Finite semantic cross-check of a supplied 201-language family with the "
                       "retained knowing-arrival solver. Does not independently prove enumeration "
                       "completeness, strategy normalization, or arbitrary-period correspondence."}
    RECEIPT.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in ["status", "comparisons", "mismatches"]}))
    raise SystemExit(0 if not mismatches else 1)


if __name__ == "__main__":
    main()
