"""Read-only evidence audit. Does not generate responses or rewrite source files."""
from pathlib import Path
from collections import defaultdict
import hashlib
import itertools
import json

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists() and (p / "RESEARCH.md").exists())
SOURCE = REPO / "sources/20-codex-theory-sessions-2026-10-05/sin/work/package-reproduction/live"


def read(path):
    return json.loads(path.read_text())


def predict(row, rule):
    if rule is None:
        return row[0]
    i, j, x, y = rule
    return int(row[0] != (row[i] == x and row[j] == y))


def score(response, rows, rule):
    values = response.get("answers", [])
    return sum(i < len(values) and type(values[i]) is int
               and values[i] in (0, 1) and values[i] == predict(row, rule)
               for i, row in enumerate(rows))


def main():
    assignments = read(SOURCE / "assignments.json")
    seats = {(r["id"], r["replica"]): r["B"] for r in read(SOURCE / "successor-assignments.json")}
    hypotheses = [None] + [(i, j, x, y) for i, j in itertools.combinations(range(1, 5), 2)
                            for x, y in itertools.product((0, 1), repeat=2)]
    groups = defaultdict(list)
    hashes = {}
    for path in sorted((SOURCE / "lineages").glob("*/private.json")):
        case = read(path)
        folder = path.parent
        for name in ("private.json", "baseline-response.json", "maintenance-response.json", "r0-response.json", "r1-response.json"):
            p = folder / name
            hashes[str(p.relative_to(REPO))] = hashlib.sha256(p.read_bytes()).hexdigest()
        maintenance = read(folder / "maintenance-response.json")
        packet = maintenance.get("packet", "")
        valid = maintenance.get("maintenance_slots") == 1 and isinstance(packet, str) and 0 < len(packet.split()) <= 120
        scores = {seats[(case["id"], replica)]: score(read(folder / f"{replica}-response.json"), case["test"], case["truth"])
                  for replica in ("r0", "r1")}
        labels = [predict(x, case["truth"]) for x in case["baseline"]]
        survivors = [h for h in hypotheses if [predict(x, h) for x in case["baseline"]] == labels]
        assert len(survivors) == 1
        conventional = sum(predict(x, survivors[0]) == predict(x, case["truth"]) for x in case["test"])
        assert conventional == 16
        groups[(case["stratum"], assignments[case["id"]])].append({
            "id": case["id"], "maintenance": int(valid), "access_score": scores[1],
            "blocked_score": scores[0], "conventional_full_report_score": conventional})
    summary = []
    for (stratum, timing), rows in sorted(groups.items()):
        n = len(rows)
        summary.append({"stratum": stratum, "timely_feedback": timing, "lineages": n,
                        "valid_packets": sum(r["maintenance"] for r in rows),
                        "access_accuracy": sum(r["access_score"] for r in rows) / (16*n),
                        "blocked_accuracy": sum(r["blocked_score"] for r in rows) / (16*n),
                        "conventional_full_report_accuracy": sum(r["conventional_full_report_score"] for r in rows) / (16*n)})
    assert sum(len(x) for x in groups.values()) == 32
    output = {"status": "passed", "new_empirical_observations": 0,
              "source_files_hashed": len(hashes), "lineages": 32, "successor_contexts": 64,
              "successor_answers": 1024, "cluster_unit": "founder lineage",
              "summaries": summary, "hashes": hashes,
              "inference": "Recorded task supports feedback and handoff effects; complete-report candidate elimination matches all test labels. This comparator is not cost matched. No human concern, subjective experience, natural prevalence, or theoretical superiority result follows."}
    (HERE / "existing-evidence-audit.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k != "hashes"}, indent=2))


if __name__ == "__main__":
    main()
