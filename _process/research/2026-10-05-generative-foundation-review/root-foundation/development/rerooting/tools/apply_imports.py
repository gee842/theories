"""Rewrite the import lines of Lean modules to a planned set.

usage: apply_imports.py PACKAGE PLAN

PLAN is w2_plan.py's output; for each module in its "import_changes" the import block at the top of
the module (which must hold exactly the planned "before" set) keeps the imports in "after" in their
order and gains the rest of "after" below them.
"""
import json
import sys
from pathlib import Path

package, plan_path = Path(sys.argv[1]), sys.argv[2]
plan = json.loads(Path(plan_path).read_text())
for module, change in plan["import_changes"].items():
    path = package / (module.replace(".", "/") + ".lean")
    lines = path.read_text().splitlines(keepends=True)
    idx = [i for i, line in enumerate(lines) if line.startswith("import ")]
    assert all(not lines[i].strip() or lines[i].startswith("import ") for i in range(idx[0], idx[-1] + 1)), module
    current = [lines[i].split()[1] for i in idx]
    assert sorted(current) == sorted(change["before"]), (module, current, change["before"])
    kept = [m for m in current if m in change["after"]]
    added = [m for m in change["after"] if m not in current]
    path.write_text("".join(lines[:idx[0]] + [f"import {m}\n" for m in kept + added] + lines[idx[-1] + 1:]))
print("imports rewritten:", len(plan["import_changes"]))
