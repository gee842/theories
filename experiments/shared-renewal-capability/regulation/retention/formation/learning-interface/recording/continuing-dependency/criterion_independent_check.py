"""Independent replay of saved acquired-criterion histories.

No producer, process, or transition implementation is imported. Native rules
below are reconstructed from FormedSelection.lean; wrapper rules are separately
implemented from the prospective protocol. The check covers the saved finite
histories and their intervention comparisons, not arbitrary future executions.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
RESULT = HERE / "criterion-results.json"
COLUMNS = ["freeA", "freeH", "resident", "intact", "local", "common", "source",
           "parts", "targetA", "episode", "historical", "closed", "finished",
           "blockedSeen", "restoredSeen", "phase", "pending", "observed",
           "candidates", "criterionActive", "selected", "commonSpent", "totalSpent"]
NATIVE = ["form_a", "form_h", "bind_a", "bind_h", "repair", "capture",
          "copy_a", "copy_h", "bulk_a", "bulk_h", "wear_a", "wear_h",
          "wear_res_a", "wear_res_h", "damage", "leak_common", "leak_local"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unpack(vector):
    assert len(vector) == len(COLUMNS)
    return dict(zip(COLUMNS, vector))


def pack(s):
    return [s[k] for k in COLUMNS]


def population(s):
    return s["freeA"] + s["freeH"] + (s["resident"] != 0)


def acount(s):
    return s["freeA"] + (s["resident"] == 1)


def energy(s):
    return s["common"] + s["local"] + s["source"]


def valid(s):
    assert all(isinstance(v, int) and v >= 0 for v in s.values())
    assert s["resident"] in (0, 1, 2)
    assert 0 <= s["parts"] <= 9
    assert population(s) + 2*s["parts"] <= 78
    for key in ("intact", "local", "closed", "finished", "blockedSeen",
                "restoredSeen", "criterionActive"):
        assert s[key] in (0, 1)


def native_guard(s, e):
    a, h, r = s["freeA"], s["freeH"], s["resident"]
    f, q, local = s["common"], s["source"], s["local"]
    room = population(s) < 78 - 2*s["parts"]
    if e in ("form_a", "form_h"):
        return not s["intact"] and room and f > 0
    if e in ("bind_a", "bind_h"):
        return (a if e == "bind_a" else h) > 0 and r == 0 and f > 0
    if e == "repair":
        return r == 1 and not s["intact"] and f > 0
    if e == "capture":
        return bool(s["intact"] and not local and q > 0)
    if e in ("copy_a", "copy_h"):
        return r == (1 if e == "copy_a" else 2) and bool(local) and room
    if e in ("bulk_a", "bulk_h"):
        count = a + (r == 1) if e == "bulk_a" else h + (r == 2)
        return count > 0 and room and f > 0
    if e == "wear_a": return a > 0
    if e == "wear_h": return h > 0
    if e == "wear_res_a": return r == 1
    if e == "wear_res_h": return r == 2
    if e == "damage": return s["intact"] == 1
    if e == "leak_common": return f > 0
    if e == "leak_local": return local == 1
    return False


def native_apply(s, e):
    assert native_guard(s, e), (e, pack(s))
    t = dict(s)
    if e in ("form_a", "bulk_a", "copy_a"):
        t["freeA"] += 1
    elif e in ("form_h", "bulk_h", "copy_h"):
        t["freeH"] += 1
    elif e in ("bind_a", "bind_h"):
        t["freeA" if e == "bind_a" else "freeH"] -= 1
        t["resident"] = 1 if e == "bind_a" else 2
    elif e == "repair": t["intact"] = 1
    elif e == "capture":
        t["local"] = 1
        t["source"] -= 1
    elif e == "wear_a": t["freeA"] -= 1
    elif e == "wear_h": t["freeH"] -= 1
    elif e in ("wear_res_a", "wear_res_h"): t["resident"] = 0
    elif e == "damage": t["intact"] = 0
    if e in ("copy_a", "copy_h", "leak_local"):
        t["local"] = 0
    if e in ("form_a", "form_h", "bulk_a", "bulk_h", "bind_a", "bind_h",
             "repair", "leak_common"):
        t["common"] -= 1
    t["commonSpent"] += s["common"] - t["common"]
    t["totalSpent"] += energy(s) - energy(t)
    if s["phase"] == 1:
        t["phase"], t["pending"] = 0, 0
        if e == "repair":
            t["phase"] = 2
            difference = [s[k]-t[k] for k in ("common", "local", "source")]
            t["pending"] = sum(bit for i, bit in enumerate((1, 2, 4))
                               if difference == [int(i == j) for j in range(3)])
    return t


def spend(s):
    assert s["common"] > 0
    t = dict(s)
    t["common"] -= 1
    t["commonSpent"] += 1
    t["totalSpent"] += 1
    return t


def completion(s, cfg):
    # A funded handoff remains part of the work even for the count-only reader.
    if acount(s) < s["targetA"] or s["common"] < 1:
        return False
    if not s["criterionActive"] or cfg["clamp"]:
        return True
    after_handoff = spend(s)
    channel = {1: "common", 2: "local", 4: "source"}.get(s["candidates"])
    return channel is not None and after_handoff[channel] >= 1


def plans(s, cfg):
    found = []
    for code, sequence in ((1, ["bulk_a"]), (2, ["capture", "copy_a"])):
        t = dict(s)
        for event in sequence:
            if not native_guard(t, event):
                break
            t = native_apply(t, event)
        else:
            if t["common"] > 0:
                found.append((code, completion(spend(t), cfg)))
    return found


def guard(s, cfg, event):
    if event.startswith("native:"):
        return native_guard(s, event[7:])
    if s["common"] < 1: return False
    if event == "finish": return bool(s["closed"] and not s["finished"])
    if event == "assemble":
        return s["parts"] < 9 and s["freeA"] > 0 and s["freeH"] > 0 and s["episode"] == 0
    if s["parts"] != 9: return False
    if event == "admit": return s["episode"] == 0
    if event == "openEpisode": return s["episode"] == 1 and s["phase"] == 5 and not s["finished"]
    if event in ("judge", "probeCapture"): return s["episode"] == 1 and not s["finished"]
    if event == "armRepair": return s["blockedSeen"] and s["phase"] == 0 and not s["finished"]
    if event == "observe": return s["phase"] == 2
    if event == "commit": return s["phase"] == 3
    if event == "compileCriterion": return s["phase"] == 4 and s["restoredSeen"]
    if event == "select": return s["episode"] == 2 and not s["closed"] and not s["finished"]
    if event == "judgeAfter": return s["episode"] == 2 and not s["finished"]
    return False


def step(s, cfg, event):
    valid(s)
    assert guard(s, cfg, event), (event, pack(s))
    if event.startswith("native:"):
        t = native_apply(s, event[7:])
    else:
        t = spend(s)
        if event == "finish": t["finished"] = 1
        elif event == "assemble":
            t["freeA"] -= 1
            t["freeH"] -= 1
            t["parts"] += 1
        elif event == "admit":
            t.update(targetA=acount(t), episode=1, closed=0)
        elif event == "openEpisode": t.update(episode=2, closed=0, selected=0)
        elif event in ("judge", "judgeAfter"):
            if acount(t) >= t["targetA"]:
                t["historical"] |= 1 if t["episode"] == 1 else 2
            t["closed"] = int(completion(t, cfg))
        elif event == "probeCapture":
            if native_guard(t, "capture"):
                t = native_apply(t, "capture")
                t["restoredSeen"] = int(bool(t["restoredSeen"] or t["blockedSeen"]))
            else: t.update(blockedSeen=1, closed=0)
        elif event == "armRepair": t.update(phase=1, pending=0)
        elif event == "observe":
            modes = {0: t["pending"], 1: 0, 2: 4}
            t.update(phase=3, observed=modes[cfg["receipt_mode"]])
        elif event == "commit":
            if t["observed"]: t["candidates"] &= t["observed"]
            t["phase"] = 4
        elif event == "compileCriterion":
            t["criterionActive"] = int(bool(cfg["later_repair"] and t["blockedSeen"]
                and t["restoredSeen"] and t["candidates"] in (1, 2, 4)))
            t["phase"] = 5
        elif event == "select":
            t["selected"] = 0
            for code, adequate in plans(t, cfg):
                if (cfg["force_bulk"] and code == 1) or (not cfg["force_bulk"] and adequate):
                    t["selected"] = code
                    break
        else: raise AssertionError(event)
    valid(t)
    assert energy(t) + t["totalSpent"] == energy(s) + s["totalSpent"]
    assert t["common"] + t["commonSpent"] == s["common"] + s["commonSpent"]
    assert t["parts"] >= s["parts"]
    return t


def expected_ancestor():
    word = ["form_h"]*16 + ["form_a"]*3 + ["bind_a", "repair"]
    word += ["capture", "copy_a"]*13 + ["capture"]
    for n in (5, 9, 9): word = ["form_a"]*n + ["form_h"]*n + word
    assert len(word) == 94
    return word


def check_ancestor_definitions(paths):
    # Verify the actual source words before expanding their shared ancestry.
    definitions = {
        "ActionPreparation.lean": """List.replicate 16 .formH ++
          [.formA,.formA,.formA,.associateA,.repair] ++
          (List.replicate 13 [.capture,.localCopyA]).flatten ++ [.capture]""",
        "RevisionPreparation.lean": """List.replicate 5 .formA ++
          List.replicate 5 .formH ++ ActionPreparation.word""",
        "EvaluationPreparation.lean": """List.replicate 9 .formA ++
          List.replicate 9 .formH ++ RevisionPreparation.word""",
        "SuccessionPreparation.lean": """List.replicate 9 .formA ++
          List.replicate 9 .formH ++ EvaluationPreparation.word""",
    }
    found = set()
    for source in paths:
        path = ROOT/source
        if path.name in definitions:
            match = re.search(r"def word\s*:.*?:=\s*(.*?)\n\ndef ", path.read_text(), re.S)
            assert match is not None, path
            assert "".join(match.group(1).split()) == "".join(definitions[path.name].split()), path
            found.add(path.name)
    assert found == set(definitions)


def inspect(data):
    assert data["status"] == "passed" and data["vector_columns"] == COLUMNS
    ancestor = data["ancestry"]
    assert ancestor["initial"] == [0, 0, 0, 0, 0, 360, 230]
    assert ancestor["events"] == expected_ancestor()
    state = unpack(ancestor["initial"] + [0]*16)
    for event, row in zip(ancestor["events"], ancestor["steps"]):
        assert row["event"] == event and row["before"] == pack(state)[:7]
        state = native_apply(state, event)
        assert row["after"] == pack(state)[:7]
    assert len(ancestor["steps"]) == 94
    assert ancestor["final"] == pack(state)[:7] == [38, 39, 1, 1, 1, 293, 216]
    assert state["totalSpent"] == 80
    rows = {c["name"]: c for c in data["cases"]}
    assert set(rows) == {"faithful", "clamped", "missing", "wrong_source",
        "count_only_scope", "source_exhausted", "forced_bulk_faithful_judge"}
    expected_configs = {
        "faithful": (0, False, True, False),
        "clamped": (0, True, True, False),
        "missing": (1, False, True, False),
        "wrong_source": (2, False, True, False),
        "count_only_scope": (0, False, False, False),
        "source_exhausted": (0, False, True, False),
        "forced_bulk_faithful_judge": (0, False, True, True),
    }
    count = 0
    native_count = 94
    for name, case in rows.items():
        cfg = case["config"]
        assert set(cfg) == {"receipt_mode", "clamp", "later_repair", "force_bulk"}
        assert tuple(cfg[k] for k in ("receipt_mode", "clamp", "later_repair", "force_bulk")) == expected_configs[name]
        assert case["source_exhaustion_history"] == (name == "source_exhausted")
        initial = ancestor["final"] + [0]*16
        initial[COLUMNS.index("candidates")] = 7
        assert case["initial"] == initial
        s = unpack(initial)
        visited = [pack(s)]
        assert case["events"] == [row["event"] for row in case["steps"]]
        for row in case["steps"]:
            assert row["before"] == pack(s), (name, row["event"], "before")
            s = step(s, cfg, row["event"])
            assert row["after"] == pack(s), (name, row["event"], "after")
            visited.append(pack(s))
            count += 1
            native_count += int(row["event"].startswith("native:"))
        assert case["final"] == pack(s)
        assert energy(s) + s["totalSpent"] + 80 == 590
        assert case["count_completed"] == bool(s["historical"] & 2)
        assert case["criterion_active"] == bool(s["criterionActive"])
        assert case["selected"] == s["selected"]
        assert case["returned"] == bool(s["finished"])
        assert case["later_repair"] == bool(s["intact"])
        for label, milestone in case["milestones"].items():
            assert milestone in visited, (name, label)
        for denied in case["denied"]:
            assert denied["state"] in visited
            assert not guard(unpack(denied["state"]), cfg, denied["event"])
        trained = unpack(case["milestones"]["trained"])
        assert pack(trained)[:7] == [29, 30, 1, 1, 1, 274, 215]
        assert trained["parts"] == 9 and trained["historical"] == 1
        assert trained["pending"] == 1 and trained["phase"] == 5
        if name == "missing":
            assert trained["candidates"] == 7 and not trained["criterionActive"]
        elif name == "wrong_source":
            assert trained["candidates"] == 4 and trained["criterionActive"]
        else:
            assert trained["candidates"] == 1
        assert trained["criterionActive"] == int(name not in ("missing", "count_only_scope"))
    main, old, forced = (rows[n] for n in ("faithful", "clamped", "forced_bulk_faithful_judge"))
    assert main["milestones"]["decision_before_read"] == old["milestones"]["decision_before_read"]
    a, b = main["steps"], old["steps"]
    shared = 0
    for x, y in zip(a, b):
        if x != y: break
        shared += 1
    assert shared and a[shared]["event"] == b[shared]["event"] == "select"
    assert old["milestones"]["reconstruction"] == forced["milestones"]["reconstruction"]
    assert main["selected"] == 2 and main["returned"] and main["later_repair"]
    assert old["selected"] == 1 and old["returned"] and not old["later_repair"]
    assert forced["selected"] == 1 and forced["count_completed"] and not forced["returned"] and forced["later_repair"]
    fo = unpack(forced["milestones"]["judged"])
    oo = unpack(old["milestones"]["judged"])
    assert fo["common"] == oo["common"] == 1
    assert not fo["closed"] and oo["closed"]
    assert all(fo[k] == oo[k] for k in COLUMNS if k != "closed")
    assert not guard(fo, forced["config"], "finish") and guard(oo, old["config"], "finish")
    assert rows["source_exhausted"]["selected"] == 0 and not rows["source_exhausted"]["returned"]
    assert not rows["source_exhausted"]["count_completed"]
    rival = data["hidden_fallback_countermodel"]
    assert rival["original_training_channel"] == rival["alternative_training_channel"] == 1
    assert rival["common_at_bulk_endpoint"] == 0 and rival["source_at_bulk_endpoint"] > 0
    assert not rival["original_later_repair"] and rival["alternative_later_repair"]
    return dict(cases=len(rows), extension_events=count, native_events_including_ancestry=native_count,
                ancestry_events=94, primary_clamp_matched_prefix=shared,
                no_producer_import=True, whole_history_initial_energy=590)


def main():
    source_bytes = RESULT.read_bytes()
    data = json.loads(source_bytes)
    hashes = {p: sha(ROOT/p) for p in data["source_hashes"]}
    assert hashes == data["source_hashes"]
    check_ancestor_definitions(hashes)
    result = inspect(data)
    mutations = []
    for kind in ("plant_source", "occupied_parts", "acquired_channel", "completion", "historical_completion"):
        changed = deepcopy(data)
        case = changed["cases"][0]
        if kind == "plant_source": case["steps"][0]["after"][6] += 1
        elif kind == "occupied_parts": case["steps"][0]["after"][7] = 0
        elif kind == "acquired_channel": case["milestones"]["acquired_record"][18] = 4
        elif kind == "completion": case["milestones"]["judged"][11] = 0
        elif kind == "historical_completion": case["count_completed"] = False
        try:
            inspect(changed)
        except AssertionError:
            mutations.append(kind)
        else:
            raise AssertionError((kind, "undetected mutation"))
    assert source_bytes == RESULT.read_bytes()
    assert hashes == {p: sha(ROOT/p) for p in hashes}
    receipt = dict(status="passed", checked_at_utc=datetime.now(timezone.utc).isoformat(),
        **result, detected_mutations=mutations, producer_result_sha256=sha(RESULT),
        checker_sha256=sha(Path(__file__)), source_hashes=hashes,
        scope="Independent finite replay of saved native and wrapper events, material/support, "
              "actual/acquired receipts and operative criterion controls. Supplied law, model family, "
              "ongoing undertaking, copy recipes and sensor access are not derived or ethically certified.")
    (HERE/"criterion-independent-check.json").write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps({k:v for k,v in receipt.items() if k != "source_hashes"}, indent=2))


if __name__ == "__main__":
    main()
