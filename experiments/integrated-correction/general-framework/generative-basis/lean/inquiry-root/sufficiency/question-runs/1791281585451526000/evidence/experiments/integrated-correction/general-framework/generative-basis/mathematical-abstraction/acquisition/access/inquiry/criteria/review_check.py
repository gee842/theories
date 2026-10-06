"""Independent question-partition and native-depth review.

Reads preserved results only; imports neither producer nor native graph module.
"""
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
LABELS = ("A", "B", "C0", "C1")
INDEX = {label: i for i, label in enumerate(LABELS)}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def canonical(values):
    seen, result = {}, []
    for value in values:
        if value not in seen:
            seen[value] = len(seen)
        result.append(seen[value])
    return tuple(result)


PARTITIONS = {canonical(values) for values in product(range(4), repeat=4)}


def blocks(partition):
    return {frozenset(i for i, value in enumerate(partition) if value == target)
            for target in set(partition)}


def coarser(p, q):
    return all(any(block <= larger for larger in blocks(p)) for block in blocks(q))


def join(p, q):
    intersections = {b & c for b in blocks(p) for c in blocks(q) if b & c}
    return canonical(next(block for block in intersections if i in block) for i in range(4))


@lru_cache(None)
def probe_tree(partition, labels, packets):
    if len({partition[INDEX[x]] for x in labels}) == 1:
        return 0
    if packets == 0:
        return None
    possible = []
    # Each informative test has exactly one positive initial label.
    for positive in ("A", "B"):
        branches = [tuple(x for x in labels if (x == positive) == bit)
                    for bit in (False, True)]
        depths = [probe_tree(partition, branch, packets - 1)
                  for branch in branches if branch]
        if all(depth is not None for depth in depths):
            possible.append(1 + max(depths))
    return min(possible) if possible else None


def rowkey(row):
    return (tuple(row["partition"]), tuple(row["labels"]), row["phase"],
            row["packets"], row["parity"], row["broken_reset"])


def native_children(key, action):
    partition, labels, phase, packets, parity, broken = key
    if action == "probe":
        if not packets:
            return None
        positive = "A" if phase == 2 else "B"
        return [(partition, branch, phase, packets - 1, parity, broken)
                for bit in (False, True)
                if (branch := tuple(x for x in labels if (x == positive) == bit))]
    newphase = ((phase + 1) % 3 if action == "a" else
                (phase if broken else 0) if action == "reset" else phase)
    return [(partition, labels, newphase, packets, parity, broken)]


def main():
    path = HERE / "results.json"
    report = json.loads(path.read_text())
    assert report["checker_sha256"] == digest(HERE / "check.py")
    assert report["protocol_sha256"] == digest(HERE / "PROTOCOL.md")
    assert not report["original_experiments_executed"]
    for relative, expected in report["source_bindings"].items():
        assert digest(ROOT / relative) == expected
    assert len(PARTITIONS) == 15
    assert {tuple(p) for p in report["partitions"]} == PARTITIONS
    rows = {rowkey(row): row for row in report["decisions"]}
    assert len(rows) == len(report["decisions"]) == 8100
    labelsets = [tuple(label for i, label in enumerate(LABELS) if mask & (1 << i))
                 for mask in range(1, 16)]
    assert set(rows) == set(product(PARTITIONS, labelsets, range(3), range(3), range(2), range(2)))
    for key, row in rows.items():
        partition, labels, phase, packets, parity, broken = key
        macro = probe_tree(partition, labels, packets)
        assert (macro is None) == (row["native_depth"] is None)
        if macro == 0:
            assert row["native_depth"] == 0 and row["first_action"] is None
            continue
        available = []
        for action in ("a", "reset", "read", "probe"):
            successors = native_children(key, action)
            if successors is not None:
                depths = [rows[child]["native_depth"] for child in successors]
                if all(depth is not None for depth in depths):
                    available.append((1 + max(depths), action))
        if macro is None:
            assert not available
        else:
            assert row["native_depth"] == min(depth for depth, _ in available)
            assert (row["native_depth"], row["first_action"]) in available

    expected_families = {
        0: {(0, 0, 0, 0)},
        1: {(0, 0, 0, 0), (0, 1, 1, 1), (0, 1, 0, 0)},
        2: {p for p in PARTITIONS if p[2] == p[3]},
    }
    familykeys = set()
    for family in report["families"]:
        phase, packets, parity, broken = (family[x] for x in
                                         ("phase", "packets", "parity", "broken_reset"))
        familykeys.add((phase, packets, parity, broken))
        attained = {p for p in PARTITIONS if probe_tree(p, LABELS, packets) is not None}
        assert attained == expected_families[packets]
        assert {tuple(p) for p in family["attainable"]} == attained
        maximal = {p for p in attained if not any(p != q and coarser(p, q) for q in attained)}
        greatest = {p for p in attained if all(coarser(q, p) for q in attained)}
        assert {tuple(p) for p in family["maximal"]} == maximal
        assert {tuple(p) for p in family["greatest"]} == greatest
        assert all(q in attained for p in attained for q in PARTITIONS if coarser(q, p))
        missing = {(p, q, join(p, q)) for p in attained for q in attained
                   if p < q and join(p, q) not in attained}
        assert {tuple(tuple(p) for p in item) for item in family["missing_joins"]} == missing
        for p in PARTITIONS:
            assert (rows[(p, LABELS, phase, packets, parity, broken)]["native_depth"] is not None) == (p in attained)
    assert len(report["families"]) == len(familykeys) == 36

    parent = json.loads((HERE.parent / "results.json").read_text())
    for row in parent["decisions"]:
        partition = (0, 1, 2, 3) if row["target"] == "four_causes" else (0, 1, 2, 2)
        key = (partition, tuple(row["labels"]), row["phase"], row["packets"],
               row["parity"], row["broken_reset"])
        assert rows[key]["native_depth"] == row["native_depth"]
    assert len(parent["decisions"]) == report["parent_decisions_preserved"] == 1080
    assert report["inherited_retained_probes"] == 36
    assert report["inherited_retention_failures"] == 12
    assert len(report["delayed_demand_witnesses"]) == 2
    for witness in report["delayed_demand_witnesses"]:
        positive = "A" if witness["first_probe_output"] == 1 else "B"
        survivors = tuple(x for x in LABELS if x != positive)
        assert tuple(witness["surviving_labels"]) == survivors
        requested = "B" if positive == "A" else "A"
        partition = canonical(x == requested for x in LABELS)
        assert probe_tree(partition, survivors, 0) is None
        assert probe_tree(partition, LABELS, 1) == 1
        assert witness["observed_arrival"] == witness["packets_remaining"] == 0
    receipt = {
        "scope": "independent probe recursion and native Bellman-depth certificates for saved partition decisions",
        "original_experiments_executed": False,
        "checked_decisions": len(rows),
        "checked_partitions": len(PARTITIONS),
        "checked_full_belief_families": len(familykeys),
        "parent_decisions_preserved": 1080,
        "source_bindings_verified": len(report["source_bindings"]),
        "attainable_partition_counts": {str(k): len(v) for k, v in expected_families.items()},
        "delayed_demand_witnesses_checked": 2,
        "producer_results_sha256": digest(path),
        "review_checker_sha256": digest(Path(__file__)),
    }
    (HERE / "review-check.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
