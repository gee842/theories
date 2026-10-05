"""Rational interior and boundary checks for A15/A16 using the separate game reference."""
from fractions import Fraction as Q
from pathlib import Path
import json
import random
from independent_game_check import reference

rng = random.Random(130005)
checks = 0
for i in range(150):
    ell = Q(rng.randrange(1, 20), rng.randrange(1, 8))
    K = Q(rng.randrange(1, 15), rng.randrange(1, 8))
    m = Q(rng.randrange(1, 15), rng.randrange(1, 8))
    h = K + m + Q(rng.randrange(1, 15), rng.randrange(1, 8))
    c = Q(rng.randrange(1, 15), rng.randrange(1, 8))
    chi = c * (1 + Q(rng.randrange(1, 10), 10))
    rent = chi + Q(rng.randrange(1, 15), rng.randrange(1, 8))
    b = ell + h
    o = ell + m + (b - ell - m) * Q(rng.randrange(0, 10), 10)
    p = {"T": 2, "b": b, "x": ell, "o": o, "o0": ell / 3, "ell": ell,
         "m": m, "K": K, "c": c, "r": rent, "chi": chi, "discount": Q(1),
         "handoff_at": (), "J": 0, "successor_at": -1, "successor_chi": chi}
    wa, wr = K + m + ell, K + 2*m + ell
    cashes = [ell, (ell + wa)/2, wa, wa + m/7, wa + 6*m/7, wr, wr + m/3]
    for cash in cashes:
        for persistent in (False, True):
            outcome = reference(p, cash, persistent=persistent)
            if cash < wa:
                expected, pattern = 0, (False, False)
            elif persistent and cash < wr:
                expected, pattern = h-K-m, (False, True)
            else:
                expected, pattern = 2*h-K-2*m, (True, True)
            assert outcome[0] == expected, (i, cash, persistent, outcome, expected)
            assert tuple(z[5] for z in outcome[2]) == pattern
            assert all(z[6] == "safeguard" for z in outcome[2] if z[5])
            checks += 1

report = {"status": "PASS", "rational_dynamic_cases": checks, "parameter_families": 150,
          "seed": 130005, "cash_locations": ["ell", "between ell and W_aff", "W_aff",
          "W_aff+m/7", "W_aff+6m/7", "W_res", "W_res+m/3"],
          "note": "Supplemental finite rational checks for A15/A16, using independent reference; proof reviewed separately."}
Path(__file__).with_name("formal-adversarial-checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report))
