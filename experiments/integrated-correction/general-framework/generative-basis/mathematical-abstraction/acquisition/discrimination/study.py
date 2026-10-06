"""Scoped acquired-discriminator probe; original module bytes stay unchanged.

The full run is the ancestor learner. Only audit checkpoint capture is added.
The one-table reader mask is an external intervention, not a native event.
"""
from copy import deepcopy
from dataclasses import asdict
from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(value):
    return json.loads(json.dumps(value, default=lambda x: str(x) if isinstance(x, Fraction) else sorted(x)))


def load_model(name):
    spec = importlib.util.spec_from_file_location(name, BASE / "model.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def all_word_equivalence(target, learned):
    """External finite pair traversal, never passed to the learner."""
    assert target["alphabet"] == learned["alphabet"]
    todo = [(target["initial"], learned["initial"], "")]
    seen = set()
    while todo:
        left, right, word = todo.pop(0)
        if (left, right) in seen:
            continue
        seen.add((left, right))
        if target["outputs"][left] != learned["outputs"][right]:
            return {"equivalent": False, "distinguishing_word": word, "visited_pairs": sorted(seen)}
        for i, action in enumerate(target["alphabet"]):
            todo.append((target["transitions"][left][i], learned["transitions"][right][i], word + action))
    return {"equivalent": True, "distinguishing_word": None, "visited_pairs": sorted(seen)}


def checkpoint_record(learner):
    port = learner.query.__self__
    meter = learner.meter
    assert port.meter is meter
    return normalized({
        "S": sorted(learner.S), "stored_E": sorted(learner.E), "cache": learner.cache,
        "alphabet": learner.A, "bound": learner.N, "frozen": learner.frozen,
        "machine": None if learner.machine is None else learner.machine.record(),
        "trace": learner.trace, "hypotheses": learner.hypotheses,
        "certified": learner.certified, "retained": learner.retained,
        "max_observed_length": learner.max_observed_length,
        "meter": {"initial": meter.initial, "fuel": meter.fuel, "capacity": meter.capacity,
                  "tariff": asdict(meter.tariff), "live": meter.live, "peak": meter.peak,
                  "workspace": meter.workspace, "spent": meter.spent, "totals": meter.totals,
                  "events": meter.events},
        "port": {"target": port._target.record(), "state": port.state, "invert": port.invert,
                 "broken_reset": port.broken_reset, "queries": port.queries},
    })


def run():
    sources = [BASE / "model.py", BASE / "check.py", BASE / "PROTOCOL.md",
               BASE / "results.json", BASE / "independent-check.json", BASE / "independent_check.py",
               HERE / "PROTOCOL.md", Path(__file__)]
    before_hashes = {str(p.relative_to(ROOT)): digest(p) for p in sources}
    saved = json.loads((BASE / "results.json").read_text())
    prior_check = json.loads((BASE / "independent-check.json").read_text())
    binding_checks = []
    for label, hashes in (("producer", saved["source_hashes"]), ("independent", prior_check["hashes"])):
        for name, expected in hashes.items():
            path = BASE / name
            assert digest(path) == expected, (path, expected)
            binding_checks.append({"record": label, "path": str(path.relative_to(ROOT)), "sha256": expected})

    original = load_model("_discrimination_original")
    target = original.Machine(("a", "b"), (0, 0, 1), ((1, 0), (2, 0), (0, 0)))
    inherited = normalized(original.acquisition(target))
    prior_binary = saved["cases"]["binary_same_resources"]
    assert inherited == {key: prior_binary[key] for key in inherited}
    assert inherited["status"] == "funding:cache_lookup" and not inherited["certified"]

    supplemental = normalized(original.acquisition(target, fuel=10000, capacity=4096))
    assert supplemental["status"] == "complete" and supplemental["certified"] and supplemental["retained"]
    assert supplemental["use"]["success"]
    equivalence = all_word_equivalence(normalized(target.record()), supplemental["model"])
    assert equivalence["equivalent"]

    instrumented = load_model("_discrimination_instrumented")
    captured = []

    class SnapshotLearner(instrumented.Learner):
        reader_old_E = None

        def revise_set(self, kind, addition, is_suffix=False):
            old_E = set(self.E)
            super().revise_set(kind, addition, is_suffix)
            if is_suffix and not captured:
                copy = deepcopy(self)
                copy.pre_write_E = old_E
                captured.append(copy)

        def table(self):
            if self.reader_old_E is None:
                return super().table()
            # External reader disconnection. Stored E and its accounting stay
            # intact; only the view consumed by this table calculation differs.
            view = self.reader_old_E
            k = len(self.S) * (len(self.A) + 1)
            maxlen = max(map(len, self.S)) + 1 + max(map(len, view))
            self.meter.workspace = k * (maxlen + 1 + len(view)) + (len(self.S) + 1) * (len(self.A) + 1)
            self.meter.pay("enumerate_table", work=k * k * (maxlen + 1), temporary=k * (maxlen + 1))
            T = instrumented.ordered(self.S | {s + a for s in self.S for a in self.A})
            E = instrumented.ordered(view)
            for s in T:
                for e in E:
                    self.observe(s + e)
            self.meter.pay("row_scan", work=len(T) * len(E) + len(self.S) ** 2 *
                           (len(self.A) + 1) * (len(E) + 1),
                           temporary=len(T) * len(E) + 2 * maxlen + 2)
            return T, E, {s: tuple(self.cache[s + e] for e in E) for s in T}

    instrumented.Learner = SnapshotLearner
    other_target = instrumented.Machine(("a", "b"), (0, 0, 1), ((1, 0), (2, 0), (0, 0)))
    audited = normalized(instrumented.acquisition(other_target, fuel=10000, capacity=4096))
    assert audited == supplemental, "audit-only checkpoint capture changed the original full run"
    assert len(captured) == 1
    checkpoint = captured[0]
    common = checkpoint_record(checkpoint)
    assert checkpoint.pre_write_E == {""} and checkpoint.E == {"", "a"}
    assert checkpoint.cache["a"] == 0 and checkpoint.cache["aa"] == 1
    assert common["meter"]["events"][-1]["kind"] == "distinguishing_suffix"
    assert common["S"] == ["", "a", "aa"]

    probes = {}
    for label, masked in (("acquired_reader", False), ("old_view_reader", True)):
        arm = deepcopy(checkpoint)
        assert checkpoint_record(arm) == common
        port = arm.query.__self__
        query_start, event_start = len(port.queries), len(arm.meter.events)
        if masked:
            arm.reader_old_E = set(arm.pre_write_E)
        T, E, rows = arm.table()
        assert arm.E == checkpoint.E, "reader intervention changed retained suffix storage"
        assert all(arm.cache[k] == v for k, v in checkpoint.cache.items())
        probes[label] = normalized({
            "status": "one_table_complete", "T": T, "read_E": E, "stored_E": sorted(arm.E),
            "rows": rows, "new_native_queries": [{"word": w, "output": o} for w, o in port.queries[query_start:]],
            "new_events": arm.meter.events[event_start:], "after": checkpoint_record(arm),
        })
    ordinary, masked = probes["acquired_reader"], probes["old_view_reader"]
    assert ordinary["T"] == masked["T"]
    assert ordinary["rows"][""] != ordinary["rows"]["a"]
    assert masked["rows"][""] == masked["rows"]["a"]
    assert "ba" in [q["word"] for q in ordinary["new_native_queries"]]
    assert masked["new_native_queries"] == []
    assert ordinary["stored_E"] == masked["stored_E"] == ["", "a"]

    after_hashes = {str(p.relative_to(ROOT)): digest(p) for p in sources}
    assert before_hashes == after_hashes
    return {"scope": "New scoped execution under preserved ancestor laws plus an external matched-checkpoint table-reader intervention; standard observation-table mechanism, no new native controller.",
            "source_hashes": before_hashes, "prior_binding_checks": binding_checks,
            "target": normalized(target.record()), "inherited_36_control": inherited,
            "inherited_control_matches_saved_fields": len(inherited),
            "supplemental_provision": {"fuel": 10000, "capacity": 4096, "source": 20,
                                       "status": "separately supplied mathematical assay; not inherited36 history"},
            "supplemental_full": supplemental, "instrumented_full_exact_match": audited == supplemental,
            "external_all_word_equivalence": equivalence,
            "checkpoint": common, "old_E_view": sorted(checkpoint.pre_write_E), "probes": probes,
            "limits": ["The masked reader is an external causal probe, not a realized internal revision event.",
                       "Both table probes start from independent copies; neither refunds the first suffix write or shares a spent account.",
                       "The original all-word contract and state bound remain fixed. E changes its operative discriminating contexts.",
                       "Fresh ba uses the learned context; cached a versus aa supplied the original discrepancy.",
                       "The full certificate can eventually query ba anyway; this probe identifies generated use and timing, not a new action repertoire.",
                       "Prior false-bound, sensor, reset and resource failures remain unchanged."]}


if __name__ == "__main__":
    try:
        result = run()
        output = HERE / "results.json"
        output.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"status": "passed", "results_sha256": digest(output),
                          "supplemental_spent": result["supplemental_full"]["spent"],
                          "supplemental_peak_cells": result["supplemental_full"]["peak_cells"],
                          "acquired_reader_queries": result["probes"]["acquired_reader"]["new_native_queries"],
                          "old_view_reader_queries": result["probes"]["old_view_reader"]["new_native_queries"]}))
    except Exception:
        # Unique failed code/protocol/log records are preserved before repair.
        attempts = HERE / "attempts"
        attempts.mkdir(exist_ok=True)
        index = 1 + len(list(attempts.glob("attempt-*.log")))
        stem = attempts / f"attempt-{index:02d}"
        stem.with_suffix(".py").write_bytes(Path(__file__).read_bytes())
        stem.with_suffix(".protocol.md").write_bytes((HERE / "PROTOCOL.md").read_bytes())
        stem.with_suffix(".log").write_text(traceback.format_exc())
        raise
