"""Independent graph certificate reader. Imports no producer/model code.

Recompute physical event meanings, payment prefixes, reachability, and
event-free DFS cycle witnesses / longest-path ranks from exported records.
Run from any working directory with Python 3.
"""
from collections import defaultdict, deque
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def graph_rank(nodes, edges, event):
    adjacency = defaultdict(list)
    for e in edges:
        if event not in e["events"]:
            adjacency[e["source"]].append(e["target"])
    colour, rank = {}, {}
    for start in nodes:
        if colour.get(start, 0):
            continue
        colour[start] = 1
        stack = [(start, iter(adjacency[start]))]
        while stack:
            node, children = stack[-1]
            nxt = next(children, None)
            if nxt is None:
                rank[node] = max((rank[j] + 1 for j in adjacency[node]), default=0)
                colour[node] = 2
                stack.pop()
            elif colour.get(nxt, 0) == 1:
                path = [p[0] for p in stack]
                return {"sure_recurs": False, "cycle": path[path.index(nxt):] + [nxt]}
            elif not colour.get(nxt, 0):
                colour[nxt] = 1
                stack.append((nxt, iter(adjacency[nxt])))
    assert all(rank[e["target"]] < rank[e["source"]]
               for e in edges if event not in e["events"])
    return {"sure_recurs": True, "maximum_no_event_rank": max(rank.values())}


def check(graph):
    states = {s["id"]: s for s in graph["states"]}
    edges = graph["edges"]
    mode = graph["mode"]
    adjacent = defaultdict(list)
    semantic_checks = 0
    def response(rule, x):
        return (rule // (2 ** x)) % 2
    def payload(s):
        return [s[k] for k in ("installed", "evaluator", "guard", "data0", "data1")]
    for e in edges:
        s, t = states[e["source"]], states[e["target"]]
        adjacent[s["id"]].append(t["id"])
        stop = e["action"] == "resource_stop"
        assert stop == (s["funds"] < 1)
        assert e["cost"] == (0 if stop else 1)
        assert s["funds"] - e["cost"] >= 0
        receipt = 7 if e["action"] == "auxiliary_work" and mode != "no_renewal" else 0
        assert e["receipt"] == receipt
        spill = max(0, s["funds"] - e["cost"] + receipt - 8)
        assert e["spill"] == spill
        assert t["funds"] == s["funds"] - e["cost"] + receipt - spill
        assert 0 <= t["funds"] <= 8
        assert t["phase"] == (s["phase"] if stop else (s["phase"] + 1) % 23)
        if not stop and s["phase"] == 22:
            assert t["truth"] != s["truth"]
        else:
            assert t["truth"] == s["truth"]
        actual_service = (e["action"] == "ordinary_service" and e["argument"] >= 0
                          and s["active"] and s["skilled"] and s["lease"]
                          and mode != "execution_blocked")
        wrong = actual_service and response(s["installed"], e["argument"]) != response(s["truth"], e["argument"])
        assert t["bad"] == (s["bad"] or wrong)
        expected = {
            "corrective_install": e["action"] == "admit" and e["argument"] == 1
                and t["installed"] == s["truth"] and t["installed"] != s["installed"]
                and s["certificate"] and s["guard"] == 1,
            "maintained_archive": e["action"] == "maintain_archive" and t["archive"] is not None,
            "trained_successor": e["action"] == "train_successor" and t["trainee"] is not None,
            "competent_handoff": e["action"] == "handoff" and s["trainee"] is not None
                and s["trainee"] == s["archive"] and s["lease"] and t["skilled"] and t["guard"] == 1,
            "wrong_service": wrong,
        }
        for x in (0, 1):
            expected["delivered_x" + str(x)] = (actual_service and e["argument"] == x
                and response(s["installed"], x) == response(s["truth"], x))
        for event, actual in expected.items():
            assert (event in e["events"]) == bool(actual), (mode, e, event)
            semantic_checks += 1
        if expected["maintained_archive"]:
            assert t["archive"] == payload(s) and s["skilled"] and s["lease"]
        if expected["trained_successor"]:
            assert t["trainee"] == s["archive"] and s["skilled"] and s["lease"]
        if expected["competent_handoff"]:
            assert payload(t) == s["trainee"] and t["carrier"] != s["carrier"]
        if e["action"] == "handoff" and s["trainee"] is None:
            assert not t["skilled"] and t["guard"] == 0
    reached = set(graph["initial"])
    queue = deque(reached)
    while queue:
        i = queue.popleft()
        assert adjacent[i], (mode, "non-total", i)
        for j in adjacent[i]:
            if j not in reached:
                reached.add(j)
                queue.append(j)
    assert reached == set(states)
    unsafe = [i for i, s in states.items() if s["bad"] or not 0 <= s["funds"] <= 8]
    assert all(s["protected"] == (i not in unsafe) for i, s in states.items())
    recurrence = {event: graph_rank(states, edges, event) for event in graph["event_phases"]}
    if mode == "baseline":
        assert not unsafe
        assert all(r["sure_recurs"] and r["maximum_no_event_rank"] == 22 for r in recurrence.values())
        assert all(not s["active"] or s["installed"] == s["truth"] for s in states.values())
        # Mutation check: a recurring phase without actual service does not pass.
        erased = [{**e, "events": [v for v in e["events"] if v != "delivered_x0"]} for e in edges]
        assert not graph_rank(states, erased, "delivered_x0")["sure_recurs"]
    return {"mode": mode, "states": len(states), "edges": len(edges),
            "ledger_reachability_and_semantic_checks": "pass", "event_equivalences_checked": semantic_checks,
            "unsafe_states": len(unsafe), "min_funds": min(s["funds"] for s in states.values()),
            "recurrence": recurrence}


def main():
    results = [check(json.loads(path.read_text())) for path in sorted((HERE / "implementation").glob("graph-*.json"))]
    assert len(results) == 8
    producer = {r["mode"]: r for r in json.loads((HERE / "implementation/results.json").read_text())}
    for r in results:
        p = producer[r["mode"]]
        assert all(r[k] == p[k] for k in ("states", "edges", "unsafe_states", "min_funds"))
        assert all(result["sure_recurs"] == p["recurrence"][event]["sure_recurs"]
                   for event, result in r["recurrence"].items())
    output = {"method": "independent JSON reader; DFS cycle witnesses and computed longest-path ranks; no model imports",
              "total_states": sum(r["states"] for r in results), "total_edges": sum(r["edges"] for r in results),
              "all_agree_with_producer": True, "results": results}
    (HERE / "independent-graph-results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k != "results"}, indent=2))


if __name__ == "__main__":
    main()
