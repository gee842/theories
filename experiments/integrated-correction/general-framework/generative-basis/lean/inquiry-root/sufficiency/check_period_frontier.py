#!/usr/bin/env python3
"""Search the unresolved period frontier; this is not an unbounded proof.

Reuse the retained Python knowing-arrival solver without rewriting its receipt.
Exhaust periods 9--14 up to cyclic rotation and global bit complement. Rotation
permutes the unknown starting phases. Complement permutes unknown inversion and
exchanges the two requested values. Both preserve their worst-case maximum.
"""

from datetime import datetime, timezone
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOLVER = HERE / "check_phase_period.py"


def representatives(period):
    for tail in product((0, 1), repeat=period - 1):
        pattern = (0,) + tail
        if not any(pattern):
            continue
        complement = tuple(1 - value for value in pattern)
        if any(pattern > word[offset:] + word[:offset]
               for word in (pattern, complement) for offset in range(period)):
            continue
        yield pattern


def main():
    spec = spec_from_file_location("retained_period_solver", SOLVER)
    solver = module_from_spec(spec)
    spec.loader.exec_module(solver)
    rows = []
    for period in range(9, 15):
        count = 0
        within_seven = []
        counterexamples = []
        for pattern in representatives(period):
            count += 1
            depths = [solver.least_commands(pattern, value, cap=7)
                      for value in (0, 1)]
            if None in depths:
                continue
            result = {"pattern": "".join(map(str, pattern)),
                      "least_commands_by_requested_value": depths}
            within_seven.append(result)
            repeats_three = period % 3 == 0 and all(
                pattern[i] == pattern[(i + 3) % period] for i in range(period))
            if max(depths) < 7 or not repeats_three:
                counterexamples.append(result)
        rows.append({"period": period, "rotation_complement_classes": count,
                     "within_seven": within_seven,
                     "counterexamples_to_candidate": counterexamples})
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "solver_sha256": sha256(SOLVER.read_bytes()).hexdigest(),
        "search_completed": True,
        "scope": "Periods 9--14, depth at most 7, binary cycles, unknown phase "
                 "and inversion, both requested values; rotation/complement "
                 "quotient. A None solver answer means no guarantee by depth 7, "
                 "not impossibility at every depth. No new Lean theorem.",
        "rows": rows,
        "counterexample_found": any(row["counterexamples_to_candidate"] for row in rows),
    }
    target = HERE / "period-frontier-verification.json"
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"periods": [9, 14],
                      "classes": sum(row["rotation_complement_classes"] for row in rows),
                      "counterexample_found": report["counterexample_found"]}))


if __name__ == "__main__":
    main()
