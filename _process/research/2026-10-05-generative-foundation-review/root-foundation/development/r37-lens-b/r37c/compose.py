#!/usr/bin/env python3
"""R37c: replace each counted corollary's proof by the composition of the counted law, the
decided law (with a pointwise proof for its property) and the decided corollary.

usage: python3 -B compose.py PACKAGE_DIR
Rewrites Becoming/CensusCounts.lean and Becoming/CensusBinding.lean in place; statements kept.
"""
import re
import sys
from pathlib import Path

ACTIVE = """fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).1)⟩"""
ARISING = """fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2)⟩"""
JOINT = """fun same ⟨t, active, arising⟩ => ⟨t,
        Nat.lt_of_lt_of_le active (Nat.le_of_eq (same t).1),
        Nat.lt_of_lt_of_le arising (Nat.le_of_eq (same t).2.2)⟩"""
QUIET = """fun same law t pos =>
        Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2.symm)))
          (Nat.le_of_eq (same t).1)"""
# A change bound respects the counts' values at each step.
BOUND = """fun t later => Nat.le_trans (Nat.le_of_eq
          (congr (congrArg (· + ·) (same t).1.symm) (TallyWorlds.occurrences_congr (fun s =>
            congr (congrArg (· + ·) (same s).2.1.symm) (same s).2.2.symm) t)))
          (bound t later)"""


def compose(counted, decided, corollary, pointwise, extra=""):
    return (f"  (({counted} S{extra}).symm.trans\n"
            f"    ({decided} S{extra}\n      ({pointwise}))).trans\n"
            f"    ({corollary} S{extra})\n")


BODIES = {
    "CensusCounts": {
        "counting_binds_iff_counted": compose(
            "counting_under_counted", "counting_under", "counting_binds_iff", QUIET),
        "enclosed_change_bound_iff_counted": compose(
            "enclosed_counting_under_counted", "enclosed_counting_under",
            "enclosed_change_bound_iff",
            "fun same ⟨T, B, bound⟩ => ⟨T, B, " + BOUND + "⟩"),
        "finite_counting_binds_iff_counted": compose(
            "finite_counting_under_counted", "finite_counting_under",
            "finite_counting_binds_iff", QUIET),
        "finite_change_bound_iff_counted": compose(
            "finite_counting_under_counted", "finite_counting_under", "finite_change_bound_iff",
            "fun same ⟨B, bound⟩ => ⟨B, " + BOUND + "⟩"),
    },
    "CensusBinding": {},
}
for prefix, extra in (("", ""), ("finite_", " uncounted"), ("enclosed_", "")):
    for kind, pw in (("activity", ACTIVE), ("arising", ARISING), ("joint", JOINT)):
        BODIES["CensusBinding"][f"{prefix}binding_{kind}_iff_counted"] = compose(
            f"{prefix}binding_counting_under_counted", f"{prefix}binding_counting_under",
            f"{prefix}binding_{kind}_iff", pw, extra)


def rewrite(path, bodies):
    lines = path.read_text().split("\n")
    out, i, done = [], 0, set()
    while i < len(lines):
        m = re.match(r"theorem (\S+)", lines[i])
        if m and m.group(1) in bodies:
            name = m.group(1)
            while not lines[i].endswith(":="):
                out.append(lines[i])
                i += 1
            out.append(lines[i])
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("/--", "theorem ", "end ")):
                i += 1
            out.extend(bodies[name].rstrip("\n").split("\n"))
            done.add(name)
            continue
        out.append(lines[i])
        i += 1
    assert done == set(bodies), set(bodies) - done
    path.write_text("\n".join(out))


package = Path(sys.argv[1])
for module, bodies in BODIES.items():
    rewrite(package / "Becoming" / f"{module}.lean", bodies)
    print(module, len(bodies))
