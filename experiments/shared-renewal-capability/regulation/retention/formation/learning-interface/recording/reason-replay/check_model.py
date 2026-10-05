#!/usr/bin/env python3
"""Independent deterministic checks for the frozen paid reason-replay protocol.

No producer implementation or Lean theorem is imported. The positive law uses
prebound queries and an explicit sound factual-assay premise. Corruption controls
that violate that premise are labelled separately, never silently made sound.
"""

from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
MATERIAL = 15
PRIMARY_GRAPH = ((0, 1), (1, 2), (0, 2))
PRIMARY_TRUTH = ((True, True, True), (False, True, True))
PATHS = ((0, 1), (0, 2), (0, 1, 2), (0, 2, 1))
AUDIT = (("activate", None), ("sense", None), ("decode", 0), ("decode", 1),
         ("decode", 2), ("replay", 0), ("replay", 1), ("replay", 2),
         ("replay", 3), ("publish", None))


@dataclass(frozen=True)
class Plant:
    a: int
    h: int
    resident: str
    intact: bool
    local: bool
    fuel: int
    source: int

    def population(self):
        return self.a + self.h + int(self.resident != "empty")

    def energy(self):
        return self.fuel + self.source + int(self.local)


@dataclass(frozen=True)
class Record:
    plant: Plant
    slots: int
    blank: int
    pending: str
    latch: object
    escrow: int
    records: tuple

    def material(self):
        return self.plant.population() + 2 * self.slots

    def energy(self):
        return self.plant.energy() + self.escrow

    def valid(self, material=MATERIAL):
        busy = int(self.pending != "idle")
        return (self.slots == self.blank + busy + len(self.records)
                and self.escrow == busy and self.material() <= material)


@dataclass(frozen=True)
class State:
    record: Record
    reader: bool
    context: bool
    phase: int
    sensed: object
    decoded: tuple
    working: int
    installed: object
    access: bool
    delivery: bool

    def material(self):
        return self.record.material() + 2 * int(self.reader)

    def energy(self):
        return self.record.energy()

    def valid(self):
        return self.record.valid() and self.material() <= MATERIAL


def prep_step(s, event):
    assert s.population() <= MATERIAL
    if event in ("formA", "formH"):
        assert not s.intact and s.population() < MATERIAL and s.fuel > 0
        field = "a" if event == "formA" else "h"
        t = replace(s, **{field: getattr(s, field) + 1}, fuel=s.fuel - 1)
    elif event == "associateA":
        assert s.a > 0 and s.resident == "empty" and s.fuel > 0
        t = replace(s, a=s.a - 1, resident="active", fuel=s.fuel - 1)
    elif event == "repair":
        assert s.resident == "active" and not s.intact and s.fuel > 0
        t = replace(s, intact=True, fuel=s.fuel - 1)
    else:
        raise ValueError(event)
    assert t.energy() + 1 == s.energy() and t.population() <= MATERIAL
    return t


def record_enabled(s, event):
    kind, value = event
    p = s.plant
    if kind == "assemble":
        return s.pending == "idle" and p.a > 0 and p.h > 0 and p.fuel > 0
    if kind == "reserve":
        return s.pending == "idle" and s.blank > 0 and p.fuel >= 2 and p.source >= 2
    if kind == "observe":
        return s.pending == "awaiting" and p.source >= 2
    if kind == "commit":
        return s.pending == "latched" and s.latch == value
    raise ValueError(event)


def record_step(s, event):
    assert s.valid() and record_enabled(s, event)
    kind, value = event
    p = s.plant
    if kind == "assemble":
        t = replace(s, plant=replace(p, a=p.a - 1, h=p.h - 1, fuel=p.fuel - 1),
                    slots=s.slots + 1, blank=s.blank + 1)
    elif kind == "reserve":
        t = replace(s, plant=replace(p, fuel=p.fuel - 2), blank=s.blank - 1,
                    pending="awaiting", latch=None, escrow=1)
    elif kind == "observe":
        receipt = 0 if value else 2
        t = replace(s, plant=replace(p, fuel=p.fuel + receipt, source=p.source - receipt),
                    pending="latched", latch=value)
    elif kind == "commit":
        t = replace(s, pending="idle", latch=None, escrow=0, records=s.records + (value,))
    else:
        raise ValueError(event)
    cost = int(kind != "observe")
    assert t.valid() and t.material() == s.material() and t.energy() + cost == s.energy()
    return t, cost


def decode_at(context, records, edge_index):
    if edge_index not in range(3):
        return None
    index = 3 * int(context) + edge_index
    return records[index] if index < len(records) else None


def has_edge(graph, decoded, source, target):
    return any(edge == (source, target) and i < len(decoded) and decoded[i] is True
               for i, edge in enumerate(graph))


def check_path(graph, decoded, path_index):
    path = PATHS[path_index]
    return all(has_edge(graph, decoded, a, b) for a, b in zip(path, path[1:]))


def closure_oracle(graph, certs):
    """Separate work-list reachability; never read by the physical controller."""
    reached, pending = {0}, [0]
    while pending:
        at = pending.pop()
        for i, (source, target) in enumerate(graph):
            if source == at and i < len(certs) and certs[i] is True and target not in reached:
                reached.add(target)
                pending.append(target)
    return sum(1 << (i - 1) for i in reached if i > 0)


def enabled(s, event, truth=PRIMARY_TRUTH):
    kind, arg = event
    p, r = s.record.plant, s.record
    if kind == "record":
        if s.phase != 0 or not record_enabled(r, arg):
            return False
        operation, value = arg
        if operation in ("reserve", "observe"):
            index = len(r.records)
            if index >= 6 or (index >= 3) != s.context:
                return False
            if operation == "observe" and value != truth[int(s.context)][index % 3]:
                return False
        return True
    if kind == "assemble_reader":
        return s.phase == 0 and not s.reader and r.pending == "idle" and p.a >= 1 and p.h >= 1 and p.fuel >= 1
    if kind == "activate":
        return s.phase == 0 and s.reader and r.pending == "idle" and p.fuel >= 1
    if kind == "sense":
        return s.phase == 1 and s.access and p.fuel >= 1
    if kind == "decode":
        return s.phase == 2 + arg and arg in range(3) and s.access and p.fuel >= 1
    if kind == "replay":
        return s.phase == 5 + arg and p.fuel >= len(PATHS[arg]) - 1
    if kind == "publish":
        return s.phase == 9 and s.sensed is not None
    if kind in ("context", "turnover"):
        return r.pending == "idle"
    if kind in ("access", "delivery"):
        return True
    raise ValueError(event)


def debit(s, cost):
    assert s.record.plant.fuel >= cost
    return replace(s.record, plant=replace(s.record.plant, fuel=s.record.plant.fuel - cost))


def step(s, event, graph=PRIMARY_GRAPH, truth=PRIMARY_TRUTH):
    assert s.valid() and enabled(s, event, truth)
    kind, arg = event
    if kind == "record":
        record, cost = record_step(s.record, arg)
        t = replace(s, record=record)
    elif kind == "assemble_reader":
        p = s.record.plant
        t = replace(s, record=replace(s.record, plant=replace(p, a=p.a - 1, h=p.h - 1, fuel=p.fuel - 1)), reader=True)
        cost = 1
    elif kind == "activate":
        cost = 1
        t = replace(s, record=debit(s, cost), phase=1, sensed=None, decoded=(), working=0)
    elif kind == "sense":
        cost = 1
        t = replace(s, record=debit(s, cost), phase=2, sensed=s.context)
    elif kind == "decode":
        cost = 1
        value = None if s.sensed is None else decode_at(s.sensed, s.record.records, arg)
        t = replace(s, record=debit(s, cost), phase=s.phase + 1, decoded=s.decoded + (value,))
    elif kind == "replay":
        cost = len(PATHS[arg]) - 1
        mask = s.working
        if check_path(graph, s.decoded, arg):
            mask |= 1 << (PATHS[arg][-1] - 1)
        t = replace(s, record=debit(s, cost), phase=s.phase + 1, working=mask)
    elif kind == "publish":
        t, cost = replace(s, phase=10, installed=(s.sensed, s.working)), 0
    elif kind == "context":
        t, cost = replace(s, context=arg, phase=0, sensed=None), 0
    elif kind == "turnover":
        t, cost = replace(s, phase=0, sensed=None, decoded=(), working=0, installed=None), 0
    elif kind == "access":
        t, cost = replace(s, access=arg), 0
    elif kind == "delivery":
        t, cost = replace(s, delivery=arg), 0
    else:
        raise ValueError(event)
    assert t.valid() and t.material() == s.material() and t.energy() + cost == s.energy()
    assert t.record.plant.source <= s.record.plant.source
    assert 0 <= t.working <= 3
    if kind != "record":
        assert t.record.records == s.record.records and t.record.pending == s.record.pending
        assert t.record.slots == s.record.slots and t.record.blank == s.record.blank
    return t, cost


def run(s, events, graph=PRIMARY_GRAPH, truth=PRIMARY_TRUTH, record=False):
    spent, states = 0, [asdict(s)] if record else []
    for index, event in enumerate(events):
        if not enabled(s, event, truth):
            return None, index, s, spent, states
        s, cost = step(s, event, graph, truth)
        spent += cost
        if record:
            states.append(asdict(s))
    return s, None, s, spent, states


def recording_events(word):
    return tuple(event for bit in word for event in
                 (("record", ("reserve", None)), ("record", ("observe", bit)), ("record", ("commit", bit))))


def prepare(initial_fuel=80):
    initial = Plant(0, 0, "empty", False, False, initial_fuel, 20)
    p, plants = initial, [asdict(initial)]
    for event in ("formH",) * 7 + ("formA",) * 8 + ("associateA", "repair"):
        p = prep_step(p, event)
        plants.append(asdict(p))
    assert p == Plant(7, 7, "active", True, False, initial_fuel - 17, 20)
    state = State(Record(p, 0, 0, "idle", None, 0, ()), False, False, 0,
                  None, (), 0, None, True, True)
    state, blocked, _, apparatus_cost, apparatus_states = run(
        state, (("record", ("assemble", None)),) * 6 + (("assemble_reader", None),), record=True)
    assert blocked is None and state is not None and apparatus_cost == 7
    assert (state.record.plant.a, state.record.plant.h, state.record.slots) == (0, 0, 6)
    assert state.material() == 15 and state.energy() + 24 == initial.energy()
    return initial, state, plants, apparatus_states


def whole_history():
    initial, ready, prep_states, apparatus_states = prepare()
    stages = (("record_first", recording_events((True, True, True))),
              ("audit_first", AUDIT), ("context_change", (("context", True),)),
              ("record_second", recording_events((False, True, True))),
              ("audit_second", AUDIT), ("successor", (("turnover", None),)),
              ("audit_successor", AUDIT))
    s, spent, checkpoints, state_traces = ready, 0, {}, {}
    for name, events in stages:
        previous = s
        end, blocked, _, cost, states = run(s, events, record=True)
        assert end is not None and blocked is None
        s, spent = end, spent + cost
        checkpoints[name] = {"cost": cost, "state": asdict(s)}
        state_traces[name] = states
        if name == "audit_first":
            assert s.installed == (False, 3) and s.record.records == (True, True, True)
        elif name == "context_change":
            assert s.installed == previous.installed and s.record.records == previous.record.records
            assert s.installed[0] != s.context and s.phase == 0
        elif name == "audit_second":
            assert s.installed == (True, 2) and s.decoded == (False, True, True)
        elif name == "successor":
            assert s.installed is None and s.working == 0 and s.decoded == ()
            assert s.reader == previous.reader and s.record == previous.record
        elif name == "audit_successor":
            assert s.installed == (True, 2)
    assert s.record.records == (True, True, True, False, True, True)
    assert (s.record.plant.fuel, s.record.plant.source, s.energy()) == (13, 18, 31)
    assert spent == 45 and initial.energy() == 17 + 6 + 1 + 12 + 33 + s.energy()
    return ready, s, {"initial": asdict(initial), "initial_energy": 100,
                      "preparation_cost": 17, "slot_assembly_cost": 6, "reader_cost": 1,
                      "recording_cost": 12, "audit_cost": 33, "final_energy": 31,
                      "checkpoints": checkpoints, "preparation_states": prep_states,
                      "apparatus_states": apparatus_states, "operational_states": state_traces}


def graph_checks():
    choices = tuple((u, v) for u in range(3) for v in range(3) if u != v)
    checked = 0
    for graph in product(choices, repeat=3):
        for certs in product((False, True), repeat=3):
            mask = 0
            for i, path in enumerate(PATHS):
                if check_path(graph, certs, i):
                    mask |= 1 << (path[-1] - 1)
            assert mask == closure_oracle(graph, certs)
            checked += 1
    assert closure_oracle(((1, 2), (2, 1), (1, 2)), (True,) * 3) == 0
    assert closure_oracle(PRIMARY_GRAPH, (True, True, True)) == 3
    assert closure_oracle(PRIMARY_GRAPH, (False, True, True)) == 2
    assert closure_oracle(PRIMARY_GRAPH, (False, True, False)) == 0
    return {"ordered_candidate_graphs": len(choices) ** 3, "certificate_assignments_per_graph": 8,
            "cases": checked, "includes_distinct_parallel_certificate_identities": True}


def configured_archive(ready, word, count, context, fuel, access=True):
    # Explicit configured-state grid; the joined witness and low-fuel histories
    # below separately establish actual predecessors. This is not a free reset.
    record = replace(ready.record, plant=replace(ready.record.plant, fuel=fuel),
                     blank=6 - count, records=word[:count])
    return replace(ready, record=record, context=context, access=access)


def finite_audit_grid(ready):
    checked = completed = unknown_completed = 0
    for word, count, context, access, fuel in product(
            tuple(product((False, True), repeat=6)), range(7), (False, True), (False, True), range(13)):
        s = configured_archive(ready, word, count, context, fuel, access)
        certs = tuple(decode_at(context, s.record.records, i) for i in range(3))
        end, _, stopped, spent, _ = run(s, AUDIT, truth=(word[:3], word[3:]))
        assert (end is not None) == (access and fuel >= 11)
        assert stopped.record.records == s.record.records and stopped.record.plant.source == s.record.plant.source
        assert stopped.record.plant.fuel + spent == fuel
        if end is not None:
            assert end.decoded == certs and end.installed == (context, closure_oracle(PRIMARY_GRAPH, certs))
            assert spent == 11 and end.record.plant.fuel == fuel - 11
            completed += 1
            unknown_completed += None in certs
        checked += 1
    return {"six_bit_words": 64, "prefix_lengths": 7, "contexts": 2,
            "access_settings": 2, "common_fuel_values": 13,
            "configurations": checked, "completed": completed,
            "completed_with_unknown_current_certificate": unknown_completed,
            "configured_states_not_all_claimed_reachable": True}


def actual_liquidity_grid():
    rows = []
    for initial_fuel in range(30, 44):
        initial, ready, _, _ = prepare(initial_fuel)
        recorded = run(ready, recording_events((True,) * 3))[0]
        assert recorded is not None and recorded.record.plant.fuel == initial_fuel - 30
        end, index, stopped, spent, _ = run(recorded, AUDIT)
        assert (end is not None) == (initial_fuel >= 41)
        assert stopped.record.plant.source == 20
        assert initial.energy() == 17 + 6 + 1 + 6 + spent + stopped.energy()
        assert closure_oracle(PRIMARY_GRAPH, (True,) * 3) == 3
        rows.append({"original_common_fuel": initial_fuel,
                     "inherited_common_fuel": recorded.record.plant.fuel,
                     "completed": end is not None, "stopped_before_event": index,
                     "actual_audit_spent": spent, "stopped_common_fuel": stopped.record.plant.fuel,
                     "source_retained": 20, "oracle_admitted_mask": 3,
                     "actual_installed": stopped.installed})
    return {"actual_preparation_histories": len(rows), "rows": rows}


def visible_metadata_decode(records, address, requested, declared_slot):
    """Auxiliary mismatch diagnostic, outside the immutable positive slot plan."""
    if requested != declared_slot or address >= len(records):
        return None
    return records[address]


def boundaries(ready, final):
    checks = {}
    first = run(ready, recording_events((True,) * 3))[0]
    assert first is not None
    audited = run(first, AUDIT)[0]
    assert audited is not None and audited.installed == (False, 3)
    # New context alone leaves the old archive and installed tag as history.
    changed, _ = step(audited, ("context", True))
    assert changed.installed == (False, 3) and changed.record.records == first.record.records
    missing = run(changed, AUDIT)[0]
    assert missing is not None and missing.decoded == (None, None, None) and missing.installed == (True, 0)
    checks["new_context_without_new_records_is_unknown_not_negative"] = True
    assert final.decoded[0] is False and missing.decoded[0] is None
    checks["actual_current_negative_is_distinct_from_missing"] = True
    # Existing positive support for q survives an independent defeated premise.
    assert closure_oracle(PRIMARY_GRAPH, (False, True, True)) == 2
    assert closure_oracle(PRIMARY_GRAPH, (False, True, False)) == 0
    checks["independent_ground_survives_while_unsupported_descendants_retract"] = True
    cycle = ((1, 2), (2, 1), (1, 2))
    assert run(first, AUDIT, graph=cycle)[0].installed == (False, 0)
    checks["disconnected_positive_cycle_never_bootstraps"] = True
    # No context relabelling of a reserved or latched pending observation.
    reserved, _ = step(ready, ("record", ("reserve", None)))
    assert not enabled(reserved, ("context", True)) and not enabled(reserved, ("turnover", None))
    latched, _ = step(reserved, ("record", ("observe", True)))
    assert not enabled(latched, ("context", True))
    checks["context_and_turnover_blocked_during_recording"] = True
    # The interlock stops use of an in-progress old-context audit.
    partial = run(first, AUDIT[:5])[0]
    assert partial is not None
    interrupted, _ = step(partial, ("context", True))
    assert interrupted.phase == 0 and interrupted.decoded == partial.decoded
    assert not enabled(interrupted, ("replay", 0)) and not enabled(interrupted, ("publish", None))
    checks["context_change_invalidates_partial_replay_without_erasing_archive"] = True
    # Cutting delivery cannot revise a cached or published reason.
    delivery_cut, _ = step(audited, ("delivery", False))
    assert delivery_cut.installed == audited.installed and delivery_cut.record == audited.record
    checks["delivery_cut_does_not_refute_warrant"] = True
    # A blocked cold successor retains the evidence but cannot decode it.
    cold, _ = step(final, ("turnover", None))
    blocked, _ = step(cold, ("access", False))
    end, index, stopped, spent, _ = run(blocked, AUDIT)
    assert end is None and index == 1 and spent == 1 and stopped.decoded == ()
    assert stopped.record.records == final.record.records and stopped.installed is None
    checks["blocked_archive_access_does_not_create_negative_certificates"] = True
    # Access can be removed after complete decoding; cache-only replay still works.
    decoded = run(first, AUDIT[:5])[0]
    closed, _ = step(decoded, ("access", False))
    cached = run(closed, AUDIT[5:])[0]
    assert cached is not None and cached.installed == (False, 3)
    checks["cached_replay_does_not_secretly_requery_world_or_archive"] = True
    # Current factual false never means the target reason is logically false.
    assert closure_oracle(((0, 1), (0, 1), (1, 2)), (False, True, True)) == 3
    checks["parallel_positive_ground_can_survive_negative_edge_premise"] = True
    # These visible metadata mismatches are diagnostics, not events of the
    # immutable positive protocol. The four tags are edge/context/assay/polarity.
    request = (0, True, "assay0", "positive")
    mismatch_cases = ((0, False, "assay0", "positive"), (1, True, "assay0", "positive"),
                      (0, True, "other-assay", "positive"), (0, True, "assay0", "negative"))
    assert all(visible_metadata_decode(final.record.records, 3, request, tag) is None for tag in mismatch_cases)
    checks["visible_context_edge_assay_or_polarity_mismatch_is_unknown"] = True
    # Undetectably replacing a trusted factual bit is NOT repaired by spending.
    forged = replace(final.record, records=(True, True, True, True, True, True))
    forged_cold = replace(cold, record=forged)
    forged_result = run(forged_cold, AUDIT)[0]
    assert forged_result is not None and forged_result.installed == (True, 3)
    assert closure_oracle(PRIMARY_GRAPH, PRIMARY_TRUTH[1]) == 2
    checks["corrupted_trusted_binding_or_bit_can_mislead_when_assay_premise_fails"] = True
    # Once all slots are used, old recorder admission remains impossible.
    assert final.record.blank == 0
    assert not record_enabled(final.record, ("reserve", None))
    checks["new_context_has_no_free_overwrite_or_slot_reclamation"] = True
    # The restricted assay guard removes old nondeterministic observation paths.
    assert record_enabled(reserved.record, ("observe", False))
    assert not enabled(reserved, ("record", ("observe", False)))
    checks["old_record_events_project_but_arbitrary_old_words_need_not_lift"] = True
    # Retain the original recorder's spent-component obstruction explicitly.
    old = Record(Plant(0, 0, "active", True, False, 3, 14), 2, 0, "idle", None, 0, (False, True))
    old_state = State(old, False, False, 0, None, (), 0, None, True, True)
    assert old.valid() and not enabled(old_state, ("assemble_reader", None))
    checks["old_two_slot_endpoint_does_not_supply_new_reader_pair"] = True
    # Actual end of three audits has13fuel: one more costs11; a subsequentcold
    # successor inherits2fuel and cannot complete. No free refill at turnover.
    fourth = run(cold, AUDIT)[0]
    assert fourth is not None and fourth.record.plant.fuel == 2
    next_cold, _ = step(fourth, ("turnover", None))
    assert run(next_cold, AUDIT)[0] is None and next_cold.record.plant.source == 18
    checks["finite_successor_replay_does_not_imply_indefinite_funding"] = True
    return {"checks": len(checks), "results": checks,
            "corruption_control_outside_sound_positive_protocol": True}


def supplemental_publication_freshness(ready):
    """Added after the baseline computation; not part of its prespecified grid."""
    prefix = run(ready, recording_events((True,)))[0]
    assert prefix is not None
    published = run(prefix, AUDIT)[0]
    assert published is not None and published.installed == (False, 1)
    assert published.decoded == (True, None, None) and published.phase == 10
    assert not enabled(published, ("record", ("reserve", None)))
    reopened, _ = step(published, ("context", False))
    assert reopened.installed == published.installed and reopened.phase == 0
    extended = run(reopened, recording_events((True,)))[0]
    assert extended is not None and extended.record.records == (True, True)
    current_certs = tuple(decode_at(False, extended.record.records, i) for i in range(3))
    current_closure = closure_oracle(PRIMARY_GRAPH, current_certs)
    assert current_certs == (True, True, None) and current_closure == 3
    assert extended.installed == (extended.context, 1) and extended.phase == 0
    assert extended.installed[1] & current_closure == extended.installed[1]
    assert extended.installed[1] != current_closure
    assert not enabled(extended, ("publish", None))
    refreshed = run(extended, AUDIT)[0]
    assert refreshed is not None and refreshed.phase == 10 and refreshed.installed == (False, 3)
    assert refreshed.record.records == extended.record.records
    assert refreshed.record.plant.fuel + 11 == extended.record.plant.fuel
    return {"checks": 1, "passed": True,
            "origin": "Supplemental root/reviewer diagnostic after the original 16-boundary run; event law unchanged",
            "old_published_mask": published.installed[1],
            "available_closure_after_same_context_append": current_closure,
            "old_installed_tag_still_matches": True,
            "old_installed_is_sound_but_incomplete": True,
            "completed_flag_after_reopening": False,
            "new_paid_audit_cost": 11,
            "refreshed_published_mask": refreshed.installed[1]}


def source_hashes():
    sources = [HERE / "PROTOCOL.md", HERE / "check_model.py", HERE / "protocol-freeze.json",
               HERE / "formal/ReasonReplay.lean", HERE.parent / "formal/RecordedEvidence.lean",
               ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean",
               ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
               ROOT / "_process/research/2026-10-05-revisable-concern/settlement/formal/check_process.py",
               ROOT / "_process/research/2026-10-05-revisable-concern/settlement/formal/REPORT.md",
               HERE / "development/publication-freshness-review/PROTOCOL.md",
               HERE / "development/publication-freshness-review/protocol-freeze.json",
               HERE / "development/publication-freshness-review/first-run-receipt.json"]
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in sources if p.is_file()}


def main():
    freeze = json.loads((HERE / "protocol-freeze.json").read_text())
    assert sha256((HERE / "PROTOCOL.md").read_bytes()).hexdigest() == freeze["sha256"]
    before = source_hashes()
    ready, final, history = whole_history()
    result = {"scope": "Independent finite deterministic checks; supplied factual assay, relevance, positive root and finite circuit recipe",
              "whole_history": history, "graph_closure": graph_checks(),
              "finite_audit_grid": finite_audit_grid(ready),
              "actual_liquidity_grid": actual_liquidity_grid(),
              "boundaries": boundaries(ready, final),
              "supplemental_publication_freshness": supplemental_publication_freshness(ready)}
    after = source_hashes()
    assert before == after, "A frozen input changed during computation; do not accept this result."
    result["source_hashes"] = after
    result["all_checks_passed"] = True
    (HERE / "model-verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("graph_closure", "finite_audit_grid", "boundaries")}, indent=2))
    print("14 actual liquidity histories passed. Whole account:100 =17 +6 +1 +12 +33 +31.")


if __name__ == "__main__":
    main()
