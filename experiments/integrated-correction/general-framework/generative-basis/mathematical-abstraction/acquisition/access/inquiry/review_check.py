"""Independent closed-form/status and depth-certificate review of saved results.

This does not import the producer or execute the original access experiments.
"""
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").exists())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def key(row):
    return (tuple(row["labels"]), row["phase"], row["packets"],
            row["parity"], row["broken_reset"], row["target"])


def expected(labels, packets, exact):
    # The two blocked causes never separate. Otherwise each pair separates
    # with one probe, and all three behavioral classes require two probes.
    if exact and "C0" in labels and "C1" in labels:
        return None
    classes = {label if exact else label[0] for label in labels}
    probes = len(classes) - 1
    return probes if packets >= probes else None


def children(k, command):
    labels, phase, packets, parity, broken, target = k
    if command == "probe":
        if packets == 0:
            return None
        positive = "A" if phase == 2 else "B"
        buckets = [tuple(x for x in labels if (x == positive) == result)
                   for result in (False, True)]
        return [(bucket, phase, packets - 1, parity, broken, target)
                for bucket in buckets if bucket]
    newphase = ((phase + 1) % 3 if command == "a" else
                (phase if broken else 0) if command == "reset" else phase)
    return [(labels, newphase, packets, parity, broken, target)]


def main():
    path = HERE / "results.json"
    report = json.loads(path.read_text())
    assert report["checker_sha256"] == digest(HERE / "check.py")
    assert report["protocol_sha256"] == digest(HERE / "PROTOCOL.md")
    for relative, value in report["source_bindings"].items():
        assert digest(ROOT / relative) == value
    rows = {key(row): row for row in report["decisions"]}
    assert len(rows) == len(report["decisions"]) == 1080
    for k, row in rows.items():
        labels, phase, packets, parity, broken, target = k
        needed = expected(labels, packets, target == "four_causes")
        assert row["macro_probes"] == needed
        assert (row["native_depth"] is None) == (needed is None)
        target_values = {x if target == "four_causes" else x[0] for x in labels}
        if len(target_values) == 1:
            assert row["native_depth"] == 0 and row["first_action"] is None
            continue
        possible_depths = []
        for command in ("a", "reset", "read", "probe"):
            nextkeys = children(k, command)
            if nextkeys is not None:
                depths = [rows[c]["native_depth"] for c in nextkeys]
                if all(d is not None for d in depths):
                    possible_depths.append((1 + max(depths), command))
        if needed is None:
            assert not possible_depths
        else:
            assert row["native_depth"] == min(d for d, _ in possible_depths)
            assert (row["native_depth"], row["first_action"]) in possible_depths
    allprobe = [p for g in report["extracted_groups"] for p in g["probe_endpoints"]]
    assert len(allprobe) == 48
    assert sum(p["retained"] for p in allprobe) == 36
    assert sum(p["status"] == "funding:retain_diagnosis" for p in allprobe) == 12
    receipt = {
        "scope": "independent closed-form and Bellman-certificate check of saved finite decisions",
        "checked_decisions": len(rows),
        "checked_source_bindings": len(report["source_bindings"]),
        "original_experiments_executed": False,
        "retained_original_probe_records": 36,
        "original_probe_retention_failures": 12,
        "producer_results_sha256": digest(path),
        "review_checker_sha256": digest(Path(__file__)),
    }
    (HERE / "review-check.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
