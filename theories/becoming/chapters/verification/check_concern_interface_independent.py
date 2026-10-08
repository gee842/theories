"""Independent static reconstruction of the concern/alternative interface.

Uses only the Python standard library and imports no code from either model.
Writes concern-interface-independent-checks.json beside this script.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def best(r, c, chi, v, H, z, active):
    """Compare economic receipts and a distinct patient's realized losses."""
    economies = [r - c, r - chi, 0 if active else r]
    losses = [(1 - z) * H, H, 0 if active else H]
    scores = [F(m) - F(v) * F(d) for m, d in zip(economies, losses)]
    return (
        [a for a, s in zip(["S", "B", "H"], scores) if s == max(scores)],
        list(map(str, scores)),
    )


witnesses = {}
for label, parameters in {
    "concern_only": (4, 2, 1, F(3, 2), 1, 1, False),
    "alternative_only": (4, 2, 1, 0, 1, 1, True),
    "together": (4, 2, 1, F(3, 2), 1, 1, True),
    "substitution_inactive": (4, 2, 1, 3, 1, 1, False),
    "substitution_active": (4, 2, 1, 3, 1, 1, True),
    "imperfect_moderate": (4, 2, 1, 3, 1, F(1, 2), True),
    "imperfect_high": (4, 2, 1, 5, 1, F(1, 2), True),
}.items():
    winners, scores = best(*parameters)
    witnesses[label] = {"winners": winners, "S_B_H_scores": scores}

assert witnesses["concern_only"]["winners"] == ["H"]
assert witnesses["alternative_only"]["winners"] == ["B"]
assert witnesses["together"]["winners"] == ["S"]
assert (
    witnesses["substitution_inactive"]["winners"]
    == ["S"]
    == witnesses["substitution_active"]["winners"]
)
assert witnesses["imperfect_moderate"]["winners"] == ["S"]
assert witnesses["imperfect_high"]["winners"] == ["H"]

count = 0
for r, c, chi, v, ls, lb, le in product(
    [F(1), F(3)],
    [F(1), F(2)],
    [F(1), F(2)],
    [F(0), F(1), F(3)],
    [F(0), F(1), F(2)],
    [F(0), F(1), F(2)],
    [F(0), F(1), F(2)],
):
    scores = {"S": r - c - v * ls, "B": r - chi - v * lb, "H": -v * le}
    unique = scores["S"] > scores["B"] and scores["S"] > scores["H"]
    assert unique == (c < chi + v * (lb - ls) and c < r + v * (le - ls))
    count += 1

result = {
    "status": "passed",
    "named_witnesses": witnesses,
    "general_harm_cases": count,
    "scope": "Independent static decision reconstruction. No joint learning/strategic dynamics tested.",
}
Path(__file__).with_name("concern-interface-independent-checks.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result))
