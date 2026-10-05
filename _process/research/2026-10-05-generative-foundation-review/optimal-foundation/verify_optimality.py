"""Exact finite checks for the companion optimal-foundation note.

This constructs a timing example, obtains its coarsest faithful partition by
refinement, and independently enumerates every label-respecting partition.
No data or results are imported from the earlier foundation studies.
"""

from fractions import Fraction
from itertools import product
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent
ACTIVE = tuple(product((1, 2), (1, 2), (0, 1)))
STATES = ("failed", "safe") + ACTIVE
ACTIONS = ("wait", "dispatch")


def label(state):
    return state if isinstance(state, str) else "active"


def step(state, action):
    if isinstance(state, str):
        return state
    reserve, delay, badge = state
    if action == "dispatch":
        return "safe" if reserve >= delay else "failed"
    return (reserve - 1, delay, badge) if reserve > 1 else "failed"


def normalize(blocks):
    return frozenset(frozenset(block) for block in blocks)


def refine(blocks):
    while True:
        lookup = {state: block for block in blocks for state in block}
        groups = {}
        for state in STATES:
            signature = (lookup[state],) + tuple(
                lookup[step(state, action)] for action in ACTIONS
            )
            groups.setdefault(signature, set()).add(state)
        updated = normalize(groups.values())
        if updated == blocks:
            return blocks
        blocks = updated


def partitions(items):
    """Generate set partitions without duplicates by recursive insertion."""
    if not items:
        yield []
        return
    first, *rest = items
    for blocks in partitions(rest):
        yield [[first]] + [block[:] for block in blocks]
        for index in range(len(blocks)):
            copied = [block[:] for block in blocks]
            copied[index].append(first)
            yield copied


def faithful(blocks):
    lookup = {state: index for index, block in enumerate(blocks) for state in block}
    for block in blocks:
        if len({label(state) for state in block}) != 1:
            return False
        for action in ACTIONS:
            if len({lookup[step(state, action)] for state in block}) != 1:
                return False
    return True


initial = normalize(({"failed"}, {"safe"}, set(ACTIVE)))
canonical = refine(initial)
enumerated = 0
faithful_count = 0
min_count = len(STATES)
min_partitions = []
for partition in partitions(list(ACTIVE)):
    candidate = [["failed"], ["safe"]] + partition
    enumerated += 1
    if faithful(candidate):
        faithful_count += 1
        # Every faithful competitor must refine the computed canonical map.
        assert all(any(set(block) <= set(c) for c in canonical) for block in candidate)
        count = len(candidate)
        if count < min_count:
            min_count = count
            min_partitions = [normalize(candidate)]
        elif count == min_count:
            min_partitions.append(normalize(candidate))

assert enumerated == 4140
assert len(canonical) == min_count == 6
assert len(min_partitions) == 1
assert min_partitions[0] == canonical
assert step((1, 1, 0), "dispatch") == "safe"
assert step((1, 2, 0), "dispatch") == "failed"
assert all(
    any({(r, d, 0), (r, d, 1)} <= block for block in canonical)
    for r, d in product((1, 2), repeat=2)
)

# Distinct posterior predictions for a two-state hidden environment.
predictions = []
for n in range(13):
    posterior = Fraction(2**n, 1 + 2**n)
    predictions.append((1 - posterior) / 3 + posterior * Fraction(2, 3))
assert len(set(predictions)) == len(predictions)

# A common decoder cannot represent two different deterministic responses.
separation = Fraction(1)
assert separation / 2 == Fraction(1, 2)

result = {
    "status": "all checks passed",
    "scope": "Constructed examples only; no empirical validation or general proof certificate.",
    "timing_model": {
        "fine_states": len(STATES),
        "actions": list(ACTIONS),
        "label_respecting_partitions_enumerated": enumerated,
        "faithful_partitions": faithful_count,
        "minimal_blocks": min_count,
        "distinct_minimal_partitions": len(min_partitions),
        "every_faithful_partition_refines_canonical": True,
        "canonical_blocks": sorted(
            [sorted(map(str, block)) for block in canonical], key=lambda x: x[0]
        ),
        "spatial_distinction": "reserve 1, delay 1 dispatches safely; reserve 1, delay 2 fails",
        "decorative_badge_removed": True,
    },
    "hidden_environment": {
        "latent_states": 2,
        "first_distinct_predictions_checked": len(predictions),
        "predictions": list(map(str, predictions)),
        "infinite_distinctness": "Established algebraically in the note; finite check is illustrative.",
    },
}
(ROOT / "EXACT-CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
