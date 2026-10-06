"""Independent bounded result review. Never imports the learner or study.

Reconstruct only the two declared table probes, then check saved full-run
accounting and finite target/model equivalence. This is not a new full learner.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from itertools import product
import json

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").exists())


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def answer(machine, word):
    state = machine["initial"]
    for letter in word:
        state = machine["transitions"][state][machine["alphabet"].index(letter)]
    return machine["outputs"][state]


def reconstruct_table(initial, view):
    out = deepcopy(initial)
    m, port = out["meter"], out["port"]
    tariff = {key: Q(value) for key, value in m["tariff"].items()}
    new_events, new_queries = [], []

    def event(kind, work=0, live=None, temporary=0, extra=Q(0)):
        live = m["live"] if live is None else live
        peak = max(m["live"], live) + m["workspace"] + temporary
        assert peak <= m["capacity"]
        duration = work + 1
        bill = tariff["scale"] * (extra + tariff["work"] * work
                + tariff["rent"] * peak * duration
                + tariff["write"] * max(0, live - m["live"]))
        assert Q(m["fuel"]) >= bill
        m["fuel"] = str(Q(m["fuel"]) - bill)
        m["spent"] = str(Q(m["spent"]) + bill)
        m["live"], m["peak"] = live, max(m["peak"], peak)
        m["totals"][kind] = str(Q(m["totals"].get(kind, "0")) + bill)
        record = dict(kind=kind, work=work, live=live, temporary=temporary,
                      workspace=m["workspace"], peak=peak, duration=duration,
                      bill=str(bill), fuel=m["fuel"])
        m["events"].append(record)
        new_events.append(record)

    def cells(cache):
        candidate = out["machine"]
        machine_cells = (0 if candidate is None else
                         1 + len(candidate["outputs"]) * (1 + len(candidate["alphabet"])))
        return (8 + sum(len(w) + 1 for w in out["S"])
                + sum(len(w) + 1 for w in out["stored_E"])
                + sum(len(w) + 2 for w in cache) + machine_cells)

    histories = sorted(set(out["S"]) | {s + a for s in out["S"]
                      for a in out["alphabet"]}, key=lambda s: (len(s), s))
    view = sorted(view, key=lambda s: (len(s), s))
    k = len(out["S"]) * (len(out["alphabet"]) + 1)
    width = max(map(len, out["S"])) + 1 + max(map(len, view))
    m["workspace"] = k * (width + 1 + len(view)) + (len(out["S"]) + 1) * (len(out["alphabet"]) + 1)
    event("enumerate_table", work=k * k * (width + 1), temporary=k * (width + 1))
    for prefix in histories:
        for suffix in view:
            word = prefix + suffix
            event("cache_lookup", work=1 + len(word) + sum(len(w) + 1 for w in out["cache"]),
                  temporary=len(word) + 2)
            if word in out["cache"]:
                continue
            prior_workspace = m["workspace"]
            m["workspace"] += len(word) + 2
            event("target_reset", extra=tariff["reset"])
            if not port["broken_reset"]:
                port["state"] = port["target"]["initial"]
            for letter in word:
                event("target_action", extra=tariff["action"])
                index = port["target"]["alphabet"].index(letter)
                port["state"] = port["target"]["transitions"][port["state"]][index]
            event("endpoint_read", extra=tariff["read"])
            value = port["target"]["outputs"][port["state"]] ^ int(port["invert"])
            port["queries"].append([word, value])
            new_queries.append({"word": word, "output": value})
            m["workspace"] = prior_workspace
            next_cache = dict(out["cache"], **{word: value})
            event("record_answer", work=len(word) + 2, live=cells(next_cache), temporary=len(word) + 2)
            out["cache"] = next_cache
            out["max_observed_length"] = max(out["max_observed_length"], len(word))
    event("row_scan", work=len(histories) * len(view) + len(out["S"]) ** 2
          * (len(out["alphabet"]) + 1) * (len(view) + 1),
          temporary=len(histories) * len(view) + 2 * width + 2)
    return {"status": "one_table_complete", "T": histories, "read_E": view,
            "stored_E": out["stored_E"],
            "rows": {s: [out["cache"][s + e] for e in view] for s in histories},
            "new_native_queries": new_queries, "new_events": new_events, "after": out}


def review():
    path = HERE / "results.json"
    result_hash = digest(path)
    data = json.loads(path.read_text())
    bound = {}
    for name, expected in data["source_hashes"].items():
        assert digest(ROOT / name) == expected, name
        bound[name] = expected
    for item in data["prior_binding_checks"]:
        assert digest(ROOT / item["path"]) == item["sha256"], item["path"]
        bound[str((ROOT / item["path"]).resolve().relative_to(ROOT))] = item["sha256"]

    old = json.loads((HERE.parent / "results.json").read_text())["cases"]["binary_same_resources"]
    for key, value in data["inherited_36_control"].items():
        assert value == old[key], key
    checkpoint = data["checkpoint"]
    assert data["target"] == {"alphabet": ["a", "b"], "outputs": [0, 0, 1],
                              "transitions": [[1, 0], [2, 0], [0, 0]], "initial": 0}
    assert checkpoint["port"]["target"] == data["target"]
    assert checkpoint["S"] == ["", "a", "aa"]
    assert checkpoint["stored_E"] == ["", "a"]
    assert checkpoint["cache"]["a"] == 0 and checkpoint["cache"]["aa"] == 1
    assert checkpoint["meter"]["events"][-1]["kind"] == "distinguishing_suffix"
    complete = data["supplemental_full"]
    assert complete["events"][:len(checkpoint["meter"]["events"])] == checkpoint["meter"]["events"]
    reconstructed = {}
    for name, view in [("acquired_reader", checkpoint["stored_E"]),
                       ("old_view_reader", data["old_E_view"])]:
        reconstructed[name] = reconstruct_table(checkpoint, view)
        assert reconstructed[name] == data["probes"][name], name

    # Independent accounting of saved completed events; no learning replay.
    t = {k: Q(v) for k, v in checkpoint["meter"]["tariff"].items()}
    accounting_events = 0
    for run in [data["inherited_36_control"], complete]:
        fuel, live, peak, costs = Q(run["initial_fuel"]), 0, 0, {}
        for e in run["events"]:
            extra = {"installation": t["install"], "target_reset": t["reset"],
                     "target_action": t["action"], "endpoint_read": t["read"],
                     "extraction_work": t["read"]}.get(e["kind"], Q(0))
            if e["kind"] == "retention_epoch":
                extra = t["final_rent"] * live
            expected_peak = max(live, e["live"]) + e["workspace"] + e["temporary"]
            assert expected_peak == e["peak"] and e["duration"] == e["work"] + 1
            charge = t["scale"] * (extra + t["work"] * e["work"]
                     + t["rent"] * expected_peak * e["duration"]
                     + t["write"] * max(0, e["live"] - live))
            assert Q(e["bill"]) == charge
            fuel -= charge
            assert fuel >= 0 and Q(e["fuel"]) == fuel
            live, peak = e["live"], max(peak, expected_peak)
            costs[e["kind"]] = costs.get(e["kind"], Q(0)) + charge
            accounting_events += 1
        assert fuel == Q(run["fuel"]) and peak == run["peak_cells"]
        assert Q(run["spent"]) == Q(run["initial_fuel"]) - fuel
        assert costs == {k: Q(v) for k, v in run["costs"].items()}

    target, learned = data["target"], complete["model"]
    assert target["alphabet"] == learned["alphabet"]
    pending, seen = [(target["initial"], learned["initial"])], set()
    while pending:
        pair = pending.pop()
        if pair in seen:
            continue
        seen.add(pair)
        left, right = pair
        assert target["outputs"][left] == learned["outputs"][right]
        pending.extend(zip(target["transitions"][left], learned["transitions"][right]))
    assert sorted(map(list, seen)) == data["external_all_word_equivalence"]["visited_pairs"]
    assert complete["status"] == "complete" and complete["certified"] and complete["retained"]
    queried = {x["word"]: x["output"] for x in complete["queries"]}
    certificate_words = {"".join(w) for n in range(2 * checkpoint["bound"] - 1)
                         for w in product(target["alphabet"], repeat=n)}
    assert certificate_words.issubset(queried)
    assert all(answer(target, w) == y == answer(learned, w) for w, y in queried.items())
    use = complete["use"]
    assert use["word"] not in queried and answer(target, use["word"]) == 1
    assert use["success"] and use["transferred"] == 10 and use["wasted"] == 0 and use["source"] == 10
    assert Q(use["fuel_after_return"]) == Q(complete["fuel"]) + 10
    assert digest(path) == result_hash
    return {"status": "passed", "scope": "Independent reconstruction of two table probes, saved-run accounting, source bindings and finite equivalence; no full learner rerun or new empirical result.",
            "results_sha256": result_hash, "checker_sha256": digest(Path(__file__)),
            "source_hashes": bound, "producer_bound_entries": len(data["source_hashes"]),
            "prior_bound_entries": len(data["prior_binding_checks"]),
            "original_saved_fields": len(data["inherited_36_control"]),
            "fully_reconstructed_probe_events": sum(len(p["new_events"]) for p in reconstructed.values()),
            "saved_accounting_events": accounting_events, "certificate_words": len(certificate_words),
            "equivalence_pairs": sorted(map(list, seen)),
            "acquired_reader_queries": reconstructed["acquired_reader"]["new_native_queries"],
            "masked_reader_queries": reconstructed["old_view_reader"]["new_native_queries"],
            "limits": ["Deepcopy callback/meter identity assertions and instrumentation noninterference were inspected in producer source, not separately rerun.",
                       "The masked arm ends after one table; no masked full-acquisition success or failure was tested.",
                       "The complete assay has supplied fuel10000/capacity4096, separate from the inherited36/256 case."]}


if __name__ == "__main__":
    result = review()
    destination = HERE / "independent-check.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "receipt_sha256": digest(destination),
                      "probe_events": result["fully_reconstructed_probe_events"],
                      "saved_accounting_events": result["saved_accounting_events"]}))
