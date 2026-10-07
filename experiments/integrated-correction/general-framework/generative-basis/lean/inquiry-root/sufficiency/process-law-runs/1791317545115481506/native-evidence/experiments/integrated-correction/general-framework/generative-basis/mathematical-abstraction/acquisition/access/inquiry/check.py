"""Read-only reconstruction plus finite effectful decision-tree verification."""
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACCESS = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
LABELS = ("A", "B", "C0", "C1")
OUTPUT = (0, 0, 1)
PARAMS = {"A": (0, 0), "B": (1, 0), "C0": (0, 1), "C1": (1, 1)}
SUBSETS = tuple(tuple(xs) for n in range(1, 5) for xs in combinations(LABELS, n))
STATES = tuple(product(SUBSETS, range(3), range(3)))


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def flags(code):
    return code & 1, (code >> 1) & 1, (code >> 2) & 1, (code >> 3) & 1


def initial_label(code):
    tau, sigma, broken, blocked = flags(code)
    return ("C" + str(tau)) if blocked else ("B" if tau else "A")


def target(label, exact):
    return label if exact else label[0]


def terminal(labels, exact):
    return len({target(x, exact) for x in labels}) == 1


def successors(state, action, parity, broken):
    """Explicit native commands; no hidden initial label is exposed."""
    labels, phase, packets = state
    if action == "probe" and packets == 0:
        return None
    outcomes = defaultdict(list)
    for label in labels:
        tau, blocked = PARAMS[label]
        next_phase, next_packets = phase, packets
        if action == "a":
            next_phase, observation = (phase + 1) % 3, ("none",)
        elif action == "reset":
            next_phase = phase if broken else 0
            observation = ("none",)
        elif action == "read":
            observation = ("reading", OUTPUT[phase] ^ parity)
        elif action == "probe":
            arrival = (OUTPUT[phase] ^ tau) & (1 - blocked)
            next_packets -= 1
            # Arrival, source depletion and waste disclose no extra bit.
            observation = ("arrival", arrival, 10 * arrival,
                           next_packets, 10 * (1 - arrival))
        else:
            raise ValueError(action)
        outcomes[(observation, next_phase, next_packets)].append(label)
    return {(obs, p, k): (tuple(xs), p, k)
            for (obs, p, k), xs in outcomes.items()}


def native_fixed_point(parity, broken, exact):
    winning = {s: 0 for s in STATES if terminal(s[0], exact)}
    policy = {}
    while True:
        additions = {}
        for state in STATES:
            if state in winning:
                continue
            choices = []
            for action in ("a", "reset", "read", "probe"):
                outcomes = successors(state, action, parity, broken)
                if outcomes and all(s in winning for s in outcomes.values()):
                    choices.append((1 + max(winning[s] for s in outcomes.values()), action))
            if choices:
                depth, action = min(choices)
                additions[state] = depth
                policy[state] = action
        if not additions:
            return winning, policy
        winning.update(additions)


@lru_cache(None)
def macro_tree(labels, packets, exact):
    """Independent recursion using the explicit two-test response table."""
    if terminal(labels, exact):
        return 0
    if packets == 0:
        return None
    tables = {
        0: {"A": 0, "B": 1, "C0": 0, "C1": 0},
        1: {"A": 1, "B": 0, "C0": 0, "C1": 0},
    }
    candidates = []
    for table in tables.values():
        branches = [tuple(x for x in labels if table[x] == bit) for bit in (0, 1)]
        depths = [macro_tree(branch, packets - 1, exact) for branch in branches if branch]
        if all(d is not None for d in depths):
            candidates.append(1 + max(depths))
    return min(candidates) if candidates else None


def extract_sources():
    saved_path, independent_path = ACCESS / "results.json", ACCESS / "independent-check.json"
    saved, independent = json.loads(saved_path.read_text()), json.loads(independent_path.read_text())
    bound = {str(p.relative_to(ROOT)): digest(p) for p in (saved_path, independent_path)}
    for manifest in (saved["source_hashes"], independent["hashes"]):
        for name, expected in manifest.items():
            path = (ACCESS / name).resolve()
            assert digest(path) == expected, name
            bound[str(path.relative_to(ROOT))] = expected
    sensor = [x for x in saved["family"] if x["factored"] and not x["probe"]]
    probe = [x for x in saved["family"] if x["factored"] and x["probe"]]
    assert len(sensor) == len(probe) == 48
    groups = defaultdict(list)
    for record in sensor:
        tau, sigma, broken, blocked = flags(record["template"])
        groups[(record["initial_phase"], tau ^ sigma, broken)].append(record)
    extracted = []
    for (phase, parity, broken), group in sorted(groups.items()):
        assert len(group) == 4
        assert {initial_label(x["template"]) for x in group} == set(LABELS)
        first = group[0]["result"]
        for record in group:
            result = record["result"]
            assert result == first  # Full saved summary, including fuel and verdict.
            assert result["status"] == "complete" and result["retained"]
            assert result["source_remaining"] == 10 and result["income"] == "0"
        verdict = first["verdict"]
        assert verdict["blocked_factor"] == [0, 1]
        expanded = [(code + 8 * blocked, q)
                    for code, q in verdict["alternatives"] for blocked in (0, 1)]
        assert len({q for _, q in expanded}) == 1
        assert {initial_label(code) for code, _ in expanded} == set(LABELS)
        assert all(flags(code)[0] ^ flags(code)[1] == parity for code, _ in expanded)
        assert all(flags(code)[2] == broken for code, _ in expanded)
        matched = [x for x in probe if x["initial_phase"] == phase
                   and (flags(x["template"])[0] ^ flags(x["template"])[1]) == parity
                   and flags(x["template"])[2] == broken]
        assert len(matched) == 4
        outcomes = []
        for record in matched:
            result, label = record["result"], initial_label(record["template"])
            arrived = int(label == "A")
            assert result["income"] == str(10 * arrived)
            assert result["source_remaining"] == 0
            assert result["wasted"] == 10 * (1 - arrived)
            if result["verdict"] is not None:
                assert len(result["verdict"]["alternatives"]) == (1 if arrived else 3)
            else:
                assert result["status"] == "funding:retain_diagnosis"
                assert not result["retained"] and arrived == 0
            outcomes.append({"initial_label": label, **result})
        negatives = [x for x in matched if initial_label(x["template"]) != "A"]
        assert all(x["result"] == negatives[0]["result"] for x in negatives)
        extracted.append({"initial_phase": phase, "parity": parity,
                          "broken_reset": broken, "sensor_endpoint": first,
                          "expanded_templates": expanded, "probe_endpoints": outcomes})
    assert len(extracted) == 12
    return bound, extracted


def main():
    source_bindings, extracted = extract_sources()
    records, summaries = [], []
    comparisons = 0
    for parity, broken, exact in product((0, 1), repeat=3):
        winning, policy = native_fixed_point(parity, broken, exact)
        for labels, phase, packets in STATES:
            state = labels, phase, packets
            macro_depth = macro_tree(labels, packets, exact)
            assert (state in winning) == (macro_depth is not None)
            comparisons += 1
            if state in winning and winning[state]:
                children = successors(state, policy[state], parity, broken)
                assert all(winning[c] < winning[state] for c in children.values())
            records.append({"labels": labels, "phase": phase, "packets": packets,
                            "parity": parity, "broken_reset": broken,
                            "target": "four_causes" if exact else "three_behaviors",
                            "native_depth": winning.get(state),
                            "first_action": policy.get(state), "macro_probes": macro_depth})
        summaries.append({"parity": parity, "broken_reset": broken,
                          "target": "four_causes" if exact else "three_behaviors",
                          "winning_by_packets": {str(k): sum(s in winning for s in STATES if s[2] == k)
                                                 for k in range(3)},
                          "full_belief_native_depths": {str(k): [winning.get((LABELS, q, k))
                                                                for q in range(3)] for k in range(3)}})
    assert comparisons == 1080
    for pair in combinations(("A", "B", "C0"), 2):
        assert macro_tree(pair, 1, False) == 1
    assert macro_tree(LABELS, 1, False) is None
    assert macro_tree(LABELS, 2, False) == 2
    assert macro_tree(LABELS, 2, True) is None
    report = {
        "scope": "finite mathematical abstraction; read-only original evidence; no new learner",
        "source_bindings": source_bindings,
        "original_sensor_cases": 48, "original_probe_cases": 48,
        "matched_sensor_groups": len(extracted),
        "extracted_groups": extracted,
        "finite_belief_states": 540, "target_specific_comparisons": comparisons,
        "probe_responses": {"learned_output_0": [0, 1, 0, 0],
                            "learned_output_1": [1, 0, 0, 0], "labels": LABELS},
        "summaries": summaries, "decisions": records,
        "checker_sha256": digest(Path(__file__)), "protocol_sha256": digest(HERE / "PROTOCOL.md"),
    }
    (HERE / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("original_sensor_cases", "original_probe_cases",
        "matched_sensor_groups", "finite_belief_states", "target_specific_comparisons")}))


if __name__ == "__main__":
    main()
