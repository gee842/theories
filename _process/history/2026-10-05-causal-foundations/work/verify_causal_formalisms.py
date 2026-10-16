"""Exact finite checks plus recorded algebra for causal-formalisms.md."""
from collections import Counter
from itertools import product
from pathlib import Path
import json


def law(model, intervention):
    dist = Counter()
    for ua, u in product((0, 1), repeat=2):
        a = intervention.get("A", ua)
        y = intervention.get("Y", u if model == 1 else a ^ u)
        dist[f"{a},{y}"] += 1
    return dict(sorted(dist.items()))


interventions = ([{}]
                + [{k: v} for k in ("A", "Y") for v in (0, 1)]
                + [{"A": a, "Y": y} for a, y in product((0, 1), repeat=2)])
checked = [{"intervention": i, "M1_counts": law(1, i),
            "M2_counts": law(2, i), "equal": law(1, i) == law(2, i)}
           for i in interventions]
assert all(row["equal"] for row in checked)
cycle_solutions = [(x, y, z) for x, y, z in product(range(-3, 4), repeat=3)
                   if x == y + z and y == x and z == x + 1]
assert cycle_solutions == [(-1, -1, 0)]
result = {
    "interventional_equivalence": checked,
    "number_of_regimes": len(checked),
    "M1_probability_Y0_equals_Y1": 1,
    "M2_probability_Y0_equals_Y1": 0,
    "cyclic_solution_in_integer_check_range": cycle_solutions,
    "global_uniqueness_proof": (
        "Y=X forces Z=0; Z=X+1 then forces X=Y=-1. "
        "do(Z=1) forces X=X+1, impossible."
    ),
}
Path(__file__).with_name("causal-formalisms-checks.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print("Verified all 9 perfect-intervention regimes; counterfactuals differ.")
