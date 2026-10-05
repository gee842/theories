"""Independent reason/action oracle, authored from frozen protocol and parent laws.

The oracle below was written before inspecting action/model.py.  It neither
imports that implementation nor asks its event functions for expected states.
Saved parent histories are inputs, not newly generated observations.  Hidden
orientation is used only by physical receipt/evaluation, never command selection.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import gzip
import json

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ARCHIVE = PARENT.parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
DESIGN = (0, 1, 0)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def object_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def read_json(path):
    path = existing_path(path)
    if path.suffix == ".gz":
        with gzip.open(path, "rt") as stream:
            return json.load(stream)
    return json.loads(path.read_text())


def existing_path(path):
    path = Path(path)
    return path if path.exists() else path.with_suffix(path.suffix + ".gz")


def check_receipt_hashes(receipt):
    for rel, expected in receipt["source_sha256"].items():
        assert digest(REPO / rel) == expected, ("input changed", rel)


def independent_preparation(common=155, source=154, port=True):
    """Run the declared word with original formation guards, not a final formula."""
    a = h = resident = intact = local = bound = spent = 0
    f, e, material = common, source, 32
    trace = []

    def emit(event):
        assert min(a, h, resident, local, f, e, bound, spent) >= 0
        assert a + h + resident + bound <= material
        assert local + f + e + spent == common + source
        trace.append(dict(event=event, plant=[a, h, resident, intact, local, f, e],
                          bound=bound, spent=spent))

    emit("initial")
    word = (["form_h"] * 16 + ["form_a"] * 3 + ["bind_a", "repair"]
            + ["capture", "copy_a"] * 13 + ["capture"])
    for event in word:
        precursor = material - a - h - resident - bound
        if event in ("form_a", "form_h"):
            assert not intact and precursor > 0 and f > 0
            a += event == "form_a"
            h += event == "form_h"
            f -= 1
            spent += 1
        elif event == "bind_a":
            assert resident == 0 and a > 0 and f > 0
            a -= 1
            resident = 1
            f -= 1
            spent += 1
        elif event == "repair":
            assert resident == 1 and not intact and f > 0
            intact = 1
            f -= 1
            spent += 1
        elif event == "capture":
            assert intact and not local and e > 0
            e -= 1
            local = 1
        elif event == "copy_a":
            assert resident == 1 and local and precursor > 0
            a += 1
            local = 0
            spent += 1
        emit(event)
    assert (a, h, resident, intact, local) == (15, 16, 1, 1, 1)
    for i in range(14 + int(port)):
        assert min(a, h, f) > 0
        a -= 1
        h -= 1
        bound += 2
        f -= 1
        spent += 1
        emit("cell" if i < 12 else "reader" if i == 12 else "reason" if i == 13 else "port")
    assert resident and h > 0 and local == 1 and f > 0
    h -= 1
    resident = 0
    bound += 2
    f = f - 1 + local
    local = 0
    spent += 1
    emit("adapter")
    assert a == h == int(not port)
    assert a + h + bound == 32
    assert spent == 49 + int(port)
    return dict(material=material, common=f, source=e, free_a=a, free_h=h,
                bound=bound, spent=spent, trace=trace)


@lru_cache(maxsize=1)
def parent_inputs():
    reason = read_json(PARENT / "results.json")
    recorded = read_json(ARCHIVE / "results.json")
    fixtures = read_json(ARCHIVE / "fixtures.json")["fixtures"]
    return reason, recorded, fixtures


def actual_parent(case, producer, index, unaudited=False):
    """Recover full continuing state directly from saved archive and reason bytes."""
    reason, recorded, fixtures = parent_inputs()
    row = reason["cases"][case]["producers"][producer]["paths"][index]
    ref = row["predecessor"]
    old = recorded["cases"][ref["case"]]["producers"][producer]["paths"][ref["path_index"]]
    assert object_hash(old["state"]) == ref["state_sha256"]
    assert object_hash(old["core_history"]) == ref["core_history_sha256"]
    assert row["probability"] == old["probability"]
    p = deepcopy(old["state"])
    snap = deepcopy(row["runtime_trace"][0]["state"] if unaudited else row["state"])
    if not unaudited:
        p["cells"] = deepcopy(row["endpoint_invariants"]["cells"])
    for key in ("reader_fuel", "decode_spent", "context", "cache", "cache_context",
                "cache_valid", "read_count"):
        p[key] = deepcopy(snap[key])
    assert object_hash(p["core"]) == row["endpoint_invariants"]["core_sha256"]
    assert object_hash(p["frames"]) == row["endpoint_invariants"]["frames_sha256"]
    prefix = fixtures["prefix_records"][producer][old["prefix_id"]]
    return dict(producer=p, reason=snap, probability=Q(row["probability"]),
                recipient_law=prefix["final_regime"] ^ 1,
                prefix_spent=Q(prefix["conditional_mean_marks"]["spent"]),
                prefix_waste=Q(prefix["conditional_mean_marks"]["waste"]),
                strict=bool(old["metrics"]["strict_core_witness"]),
                parent_row=row, old_row=old, lineage=(case, producer, index))


def current_command(reason):
    publication = reason.get("publication")
    if not (reason.get("publication_current") and reason.get("phase") == "published"
            and reason.get("cache_valid") and reason.get("read_count") == 3
            and reason.get("cache_context") == reason.get("context")
            and publication and publication["context"] == reason["context"]):
        return None
    mask = publication["mask"]
    if mask == [True, True, False]:
        return 0
    if mask == [True, False, True]:
        return 1
    return None


def core_trial(core, orientation, available=True, channel=True):
    """Independent original RI event law, including enabled miss and escrow."""
    c = deepcopy(core)
    trace = []
    spent = waste = 0

    def emit(event):
        assert min(c["fuel"], c["recipient"], c["source"], c["escrow"]) >= 0
        assert sum(core[k] for k in ("fuel", "recipient", "source", "escrow")) == (
            sum(c[k] for k in ("fuel", "recipient", "source", "escrow")) + spent + waste)
        trace.append(dict(event=event, core=deepcopy(c), spent=spent, waste=waste))

    if c["source"] < 10:
        return c, trace, spent, waste, False, False, None
    if not c["active"] or c["fuel"] < 8:
        c["source"] -= 10
        c["active"] = False
        waste += 10
        emit("miss")
        return c, trace, spent, waste, False, False, None
    assert c["escrow"] == 0
    c["fuel"] -= 1
    spent += 1
    emit("rent")
    c["fuel"] -= 1
    spent += 1
    emit("sense_recipient")
    command = (c["q"] >> 1) & 1
    c["fuel"] -= 3
    c["escrow"] += 3
    emit("reserve")
    capture = bool(available and command == orientation)
    c["fuel"] -= 3
    c["source"] -= 10
    spent += 3
    if capture:
        c["recipient"] += 10
    else:
        waste += 10
    emit("work")
    c["escrow"] -= 1
    spent += 1
    emit("acquire")
    if channel and not c["last"]:
        if capture:
            c["last"] = 1
        else:
            c["q"] = (c["q"] & 1) + 2 * (1 - command)
    c["escrow"] -= 2
    spent += 2
    emit("write")
    assert (core["q"] & 1) == (c["q"] & 1)
    return c, trace, spent, waste, True, capture, command


def decoded_frame(p, address, desired):
    f = p["frames"][address]
    if not f["complete"] or not f["valid"]:
        return None
    ctx, action, present, receipt = p["cells"][4 * address:4 * address + 4]
    if None in (ctx, action, present, receipt) or ctx != int(p["context"]) or not present or not receipt:
        return None
    return action == desired


def paid_reconstruction(p, reason, reserve, changed_context=False, access=(True, True, True)):
    """Cold reconstruction from old cells only; no additional recording event."""
    p, reason = deepcopy(p), deepcopy(reason)
    p["reader_fuel"] += reserve
    reserve = 0
    if changed_context:
        p["context"] = not p["context"]
    p.update(cache=[None] * 3, cache_context=None, cache_valid=False, read_count=0)
    reason.update(publication=None, publication_current=False, phase="cold", active=False,
                  normalized=[None] * 3, orientation=None, conflict=False, facts=[None] * 3,
                  working=[False] * 3, inference_index=0, path_index=0)
    trace = []

    def pay(n, bill, event):
        if p["reader_fuel"] < n:
            return False
        p["reader_fuel"] -= n
        if bill == "factual":
            p["decode_spent"] += n
        else:
            reason["reason_spent"] += n
        trace.append(dict(event=event, reader=p["reader_fuel"], factual=p["decode_spent"],
                          reasons=reason["reason_spent"]))
        return True

    if not pay(1, "factual", "activate"):
        return p, reason, reserve, trace
    if not pay(1, "factual", "context"):
        return p, reason, reserve, trace
    p["cache_context"] = p["context"]
    for i, desired in enumerate(DESIGN):
        if not pay(4, "factual", "decode"):
            return p, reason, reserve, trace
        p["cache"][i] = decoded_frame(p, i, desired)
        p["read_count"] += 1
    p["cache_valid"] = True
    if not pay(1, "reason", "reason_activate"):
        return p, reason, reserve, trace
    reason.update(phase="inference", active=True, working=[True, False, False])
    for i, desired in enumerate(DESIGN):
        if not pay(1, "reason", "infer"):
            return p, reason, reserve, trace
        fact = p["cache"][i] if access[i] else None
        reason["normalized"][i] = None if fact is None else desired if fact else 1 - desired
        reason["inference_index"] += 1
    known = {x for x in reason["normalized"] if x is not None}
    reason["conflict"] = len(known) > 1
    z = next(iter(known)) if len(known) == 1 else None
    reason["orientation"] = z
    reason["facts"] = [z == 0, z == 1, None] if z is not None else [None] * 3
    reason["phase"] = "paths"
    # The fixed star has only root->route0/root->route1; two-hop paths fail.
    for i, cost in enumerate((1, 1, 2, 2)):
        if not pay(cost, "reason", "path"):
            return p, reason, reserve, trace
        if i < 2 and reason["facts"][i] is True:
            reason["working"][i + 1] = True
        reason["path_index"] += 1
    reason.update(phase="published", active=False, publication_current=True,
                  publication=dict(context=p["context"], mask=reason["working"][:]))
    return p, reason, reserve, trace


def retained(p, reason):
    c = p["core"]
    return sum(c[k] for k in ("fuel", "recipient", "source", "escrow")) + sum(
        p[k] for k in ("reader_fuel", "archive_fuel", "idle_fuel", "archive_escrow", "packet_inflight")) + sum(
        reason[k] for k in ("extra_reserve", "external_idle"))


def inherited_spent(p, reason):
    return sum(p[k] for k in ("core_spent", "core_waste", "archive_spent", "decode_spent")) + reason["reason_spent"]


def oracle_outcome(case, producer, index):
    """Independent scheduled outcome, using the pre-authored physical oracle."""
    origin = actual_parent(case["parent_case"], producer, index, case["mode"] == "unaudited")
    p, r = deepcopy(origin["producer"]), deepcopy(origin["reason"])
    c = p["core"]
    if case["old_endpoint"]:
        construction, command_reserve, later, source, saved = 47, 0, 0, 0, 0
        material = 30
    else:
        formation = independent_preparation(case["common"], case["source"], case["port"])
        construction = formation["spent"]
        command_reserve = case["common"] - 125 - case["later"]
        later, source, saved = case["later"], case["source"] - 144, int(not case["port"])
        material = 32
    initial_total = retained(p, r) + inherited_spent(p, r) + command_reserve + later + source + saved
    c["fuel"] += command_reserve
    c["source"] += 10 * (source // 10)
    source %= 10
    binding_spent = action_spent = action_waste = 0
    imported = False
    scope = True
    generation = 0
    attempted = completed = captured = False
    action = receipt = None
    physical_trace = []
    selected = current_command(r)
    latched = False
    intervention = case["intervention"]
    point = intervention.split(":")[1] if intervention else None
    intervention_kind = intervention.split(":")[0] if intervention else None

    def invalidate(kind):
        nonlocal scope, generation, latched, imported, selected
        if kind == "foreign_token":
            # It is live in a different actual lineage, never this destination.
            latched = False
            return
        generation += 1
        latched = imported = False
        if kind in ("same_context", "changed_context", "publication_replace"):
            if kind != "publication_replace":
                if kind == "changed_context":
                    p["context"] = not p["context"]
                p["cache_valid"] = False
            r.update(active=False, phase="invalidated", publication_current=False)
            selected = None
        else:
            scope = False

    direct = case["mode"] in ("learned", "unaudited")
    if not direct:
        if case["port"] and p["core_phase"] == "ready" and c["fuel"] >= 1:
            c["fuel"] -= 1
            binding_spent += 1
            latched = selected is not None and case["permission"]
        if point == "after_read":
            invalidate(intervention_kind)
        if latched and scope and case["permission"] and c["fuel"] >= 1 and p["core_phase"] == "ready":
            c["fuel"] -= 1
            binding_spent += 1
            c["q"] = (c["q"] & 1) + 2 * (selected ^ int(case["inverted"]))
            c["last"] = 1
            imported = True
        if point == "after_import":
            invalidate(intervention_kind)

    authorized = scope and case["permission"] and case["delivery"] and (direct or imported)
    trial_start = deepcopy(c)
    if authorized and p["core_phase"] == "ready" and c["source"] >= 10:
        attempted = True
        if point == "after_rent" and c["active"] and c["fuel"] >= 8:
            c["fuel"] -= 1
            action_spent = 1
            p["core_phase"] = "rented"
            invalidate(intervention_kind)
            physical_trace = [dict(event="rent", core=deepcopy(c), spent=1, waste=0)]
        else:
            result = core_trial(c, origin["recipient_law"], case["available"])
            new_core, physical_trace, action_spent, action_waste, completed, captured, action = result
            p["core"] = c = new_core
            if completed:
                receipt = captured
                p.update(core_phase="ready", core_target=None, core_action=None, acquired_record=None)
                if point in ("after_work", "after_acquire"):
                    invalidate(intervention_kind)

    before_replay = deepcopy(p), deepcopy(r)
    replay_trace = []
    if later:
        access = parent_inputs()[0]["cases"][case["parent_case"]]["law"]["access"]
        p, r, later, replay_trace = paid_reconstruction(p, r, later, case["later_context"], access)
        c = p["core"]
        generation += 1
    for key in ("reader_fuel", "decode_spent", "context", "cache", "cache_context", "cache_valid", "read_count"):
        r[key] = deepcopy(p[key])
    remaining = retained(p, r) + later + source + saved
    assert remaining + inherited_spent(p, r) + binding_spent + action_spent + action_waste == initial_total
    original_fuel = 266 if case["old_endpoint"] else case["common"] + case["source"]
    assert construction + origin["prefix_spent"] + origin["prefix_waste"] + initial_total == original_fuel
    metrics = dict(final_actor=c["fuel"], final_recipient=c["recipient"], final_source=c["source"],
        source_remainder=source, final_reader=p["reader_fuel"], retained=remaining,
        construction_spent=construction, prefix_spent=origin["prefix_spent"], prefix_waste=origin["prefix_waste"],
        inherited_core_spent=p["core_spent"], inherited_core_waste=p["core_waste"],
        archive_spent=p["archive_spent"], factual_spent=p["decode_spent"], reason_spent=r["reason_spent"],
        binding_spent=binding_spent, action_spent=action_spent, action_waste=action_waste,
        delivered=c["recipient"] - origin["producer"]["core"]["recipient"], attempted=int(attempted),
        completed=int(completed), captured=int(captured), strict_action_capture=int(origin["strict"] and captured),
        later_reconstruction=int(bool(replay_trace)), later_current=int(bool(replay_trace) and r["publication_current"]),
        later_nonroot=int(bool(replay_trace) and current_command(r) is not None))
    return dict(producer=p, reason=r, source_reserve=source, later_reserve=later,
        saved_assembly=saved, material=material, generation=generation, scope=scope,
        metrics=metrics, physical_trace=physical_trace, replay_trace=replay_trace,
        action=action, receipt=receipt, trial_start=trial_start, before_replay=before_replay,
        original=origin, initial_total=initial_total)


def assert_equal(actual, expected, context):
    assert actual == expected, (context, actual, expected)


def reason_view(w):
    view = {k: deepcopy(v) for k, v in w.items() if k != "producer"}
    for k in ("reader_fuel", "decode_spent", "context", "cache", "cache_context", "cache_valid", "read_count"):
        view[k] = deepcopy(w["producer"][k])
    return view


def token_for(state):
    w = state["parent"]
    command = current_command(reason_view(w))
    if command is None:
        return None
    return dict(command=command, lineage=state["lineage"], generation=state["generation"],
        context=w["producer"]["context"], publication_sha256=object_hash(w["publication"]),
        recipient=state["destination_recipient"], destination_lineage=state["destination_lineage"],
        request=state["command_request"])


ARCHIVE_UNCHANGED = ("cells", "frames", "query_pointer", "pending", "archive_escrow", "archive_fuel",
                     "core_spent", "core_waste", "archive_spent", "cell_count", "free_a", "free_h")
REASON_FIELDS = ("extra_reserve", "external_idle", "reason_spent", "phase", "active", "normalized",
                 "orientation", "conflict", "facts", "working", "inference_index", "path_index",
                 "publication", "publication_current")
PHYSICAL_NAMES = {"ri_rent": "rent", "ri_sense_recipient": "sense_recipient",
                  "ri_reserve_feedback": "reserve", "ri_work_actual_receipt": "work",
                  "ri_paid_acquire": "acquire", "ri_paid_write": "write", "ri_miss": "miss"}


def check_row(case, producer, index, row):
    expected = oracle_outcome(case, producer, index)
    origin = expected["original"]
    assert Q(row["probability"]) == origin["probability"]
    assert row["observer"]["recipient_law"] == origin["recipient_law"]
    actual = row["state"]
    assert_equal(actual["parent"]["producer"], expected["producer"], (producer, index, "full producer"))
    for k in REASON_FIELDS:
        assert_equal(actual["parent"][k], expected["reason"][k], (producer, index, "reason", k))
    for k in ("source_reserve", "later_reserve", "saved_assembly", "material", "generation", "scope", "action", "receipt"):
        assert_equal(actual[k], expected[k], (producer, index, k))
    assert actual["command_reserve"] == 0
    assert actual["initial_extension_total"] == expected["initial_total"]
    assert_equal({k: Q(v) for k, v in row["metrics"].items()},
                 {k: Q(v) for k, v in expected["metrics"].items()}, (producer, index, "metrics"))
    assert_equal(row["runtime_trace"][-1]["state"], actual, (producer, index, "trace endpoint"))
    first = row["runtime_trace"][0]["state"]
    assert_equal(first["parent"]["producer"], origin["producer"], (producer, index, "original actual producer"))
    for k in REASON_FIELDS:
        assert_equal(first["parent"][k], origin["reason"][k], (producer, index, "original reason", k))

    physical = []
    previous = None
    reader_payments = []
    expected_identity = dict(lineage=f"{case['parent_case']}/{producer}/{index}", generation=0,
        destination_recipient="recipient", destination_lineage="fixed-recipient-lineage",
        command_request="recipient-command", scope=True)
    expected_phase = {k: deepcopy(origin["producer"][k]) for k in
                      ("core_phase", "core_target", "core_action", "acquired_record")}
    for item in row["runtime_trace"]:
        event, state = item["event"], item["state"]
        p, r = state["parent"]["producer"], reason_view(state["parent"])
        core = p["core"]
        if event.startswith("invalidate_"):
            kind = event[len("invalidate_"):]
            expected_identity["generation"] += 1
            assert state["latch"] is None and state["imported"] is None
            if kind in ("destination_recipient", "destination_lineage", "command_request"):
                expected_identity[kind] = "replaced-" + expected_identity[kind]
                expected_identity["scope"] = False
                assert state["parent"] == previous["parent"]
            else:
                assert not r["publication_current"] and not r["active"] and r["phase"] == "invalidated"
                if kind != "publication_replace":
                    assert not p["cache_valid"]
                    before_context = previous["parent"]["producer"]["context"]
                    assert p["context"] == (not before_context if kind == "changed_context" else before_context)
        elif event == "cold_reason_and_factual_turnover":
            expected_identity["generation"] += 1
        for key, value in expected_identity.items():
            assert_equal(state[key], value, (event, "independently bound identity", key))
        assert state["permission"] == case["permission"] and state["delivery"] == case["delivery"]
        assert state["mode"] == case["mode"] and state["port"] == case["port"]
        if event == "ri_rent":
            expected_phase["core_phase"] = "rented"
        elif event == "ri_sense_recipient":
            expected_phase.update(core_phase="sensed", core_target="recipient")
        elif event == "ri_reserve_feedback":
            expected_phase["core_phase"] = "reserved"
        elif event == "ri_work_actual_receipt":
            expected_phase.update(core_phase="worked", core_action=(core["q"] >> 1) & 1)
        elif event == "ri_paid_acquire":
            expected_phase.update(core_phase="acquired", acquired_record=expected["receipt"])
        elif event == "ri_paid_write":
            expected_phase.update(core_phase="ready", core_target=None, core_action=None, acquired_record=None)
        for key, value in expected_phase.items():
            assert_equal(p[key], value, (event, "physical phase/target/action", key))
        for field in ARCHIVE_UNCHANGED:
            assert_equal(p[field], origin["producer"][field], (event, "unchanged", field))
        assert core["q"] & 1 == origin["producer"]["core"]["q"] & 1
        assert min(core[k] for k in ("fuel", "recipient", "source", "escrow")) >= 0
        total = (retained(p, r) + inherited_spent(p, r)
                 + sum(state[k] for k in ("command_reserve", "later_reserve", "source_reserve", "saved_assembly",
                                         "binding_spent", "action_spent", "action_waste")))
        assert total == expected["initial_total"], (event, "prefix total", total, expected["initial_total"])
        if event in PHYSICAL_NAMES:
            physical.append(dict(event=PHYSICAL_NAMES[event], core=deepcopy(core),
                                 spent=state["action_spent"], waste=state["action_waste"]))
        if previous:
            before = previous["parent"]["producer"]
            oldcore = before["core"]
            if event == "paid_read_publication":
                assert previous["port"] and before["core_phase"] == "ready" and oldcore["fuel"] >= 1
                wanted = deepcopy(oldcore)
                wanted["fuel"] -= 1
                assert core == wanted and state["binding_spent"] == previous["binding_spent"] + 1
                wanted_token = token_for(previous) if previous["scope"] and previous["permission"] else None
                assert state["latch"] == wanted_token and state["imported"] is None
            elif event in ("paid_import_recipient_only", "paid_import_inverted"):
                assert previous["port"] and previous["permission"] and previous["scope"]
                assert previous["latch"] == token_for(previous) and previous["latch"] is not None
                wanted = deepcopy(oldcore)
                wanted["fuel"] -= 1
                command = previous["latch"]["command"] ^ (event == "paid_import_inverted")
                wanted["q"] = (wanted["q"] & 1) + 2 * command
                wanted["last"] = 1
                assert core == wanted and state["binding_spent"] == previous["binding_spent"] + 1
                assert state["imported"] == previous["latch"]
            elif event in ("read_unavailable", "import_blocked", "action_not_authorized", "no_complete_packet"):
                assert core == oldcore
                assert state["binding_spent"] == previous["binding_spent"]
                assert state["action_spent"] == previous["action_spent"]
            if event.startswith("later_") and (p["reader_fuel"] != before["reader_fuel"]):
                charge = before["reader_fuel"] - p["reader_fuel"]
                assert charge > 0
                delta_f = p["decode_spent"] - before["decode_spent"]
                delta_r = state["parent"]["reason_spent"] - previous["parent"]["reason_spent"]
                assert charge == delta_f + delta_r
                reader_payments.append((charge, bool(delta_r)))
        previous = state
    assert_equal(physical, expected["physical_trace"], (producer, index, "all physical prefixes"))
    expected_reader_payments = ([(1, False), (1, False)] + [(4, False)] * 3
                               + [(1, True)] * 4 + [(n, True) for n in (1, 1, 2, 2)]) if case["later"] else []
    assert_equal(reader_payments, expected_reader_payments, (producer, index, "all replay payments"))
    return len(row["runtime_trace"]), len(physical), len(reader_payments)


def expected_cases():
    """Pin the named interventions to the frozen protocol, not reported laws."""
    base = dict(parent_case="primary", common=155, source=154, port=True, later=24,
                mode="reason", permission=True, delivery=True, intervention=None,
                available=True, inverted=False, old_endpoint=False, later_context=False)
    changes = {
        "primary": {}, "no_later": dict(common=131, later=0),
        "command_short": dict(common=130, later=0), "source_none": dict(source=144),
        "source_partial": dict(source=153), "no_extension": dict(old_endpoint=True, later=0, port=False),
        "no_command_pair": dict(port=False), "permission_lost": dict(permission=False),
        "delivery_lost": dict(delivery=False), "inverted_import": dict(inverted=True),
        "no_opportunity": dict(available=False), "learned_register": dict(mode="learned", port=False),
        "unaudited_voluntary": dict(mode="unaudited", port=False, later=0, common=131),
        "unaudited_then_first_replay": dict(mode="unaudited", port=False),
        "conventional_command": dict(mode="conventional"), "later_changed_context": dict(later_context=True),
        "foreign_live_token": dict(intervention="foreign_token:after_read")}
    for name in ("consistently_corrupt", "changed_context", "same_context_reopen", "remove_both_grounds", "remove_late_positive"):
        changes["parent_" + name] = dict(parent_case=name)
    for kind in ("same_context", "changed_context", "publication_replace", "destination_recipient", "destination_lineage", "command_request"):
        for point in ("after_read", "after_import"):
            changes[kind + "_" + point] = dict(intervention=kind + ":" + point)
    for point in ("after_rent", "after_work", "after_acquire"):
        changes["scope_loss_" + point] = dict(intervention="destination_lineage:" + point)
    return {name: dict(base, **change) for name, change in changes.items()}


def assert_frozen_case(name, case):
    assert_equal(case, expected_cases()[name], (name, "frozen named-case configuration"))


def checker_fault_sensitivity(results):
    """Post-baseline checker review controls; not new scientific model arms."""
    group = results["cases"]["primary"]["producers"]["variable"]
    index = group["witness_path_index"]
    original = group["paths"][index]
    rejected = []
    for mutation in ("consistent_actor_destination", "actor_intermediate_target"):
        bad = deepcopy(original)
        states = [x["state"] for x in bad["runtime_trace"]] + [bad["state"]]
        for state in states:
            if mutation == "consistent_actor_destination":
                state["destination_recipient"] = "actor"
                for k in ("latch", "imported"):
                    if state[k] is not None:
                        state[k]["recipient"] = "actor"
            elif state["parent"]["producer"]["core_target"] == "recipient":
                state["parent"]["producer"]["core_target"] = "actor"
        try:
            check_row(expected_cases()["primary"], "variable", index, bad)
        except AssertionError:
            rejected.append(mutation)
        else:
            raise AssertionError(("checker accepted semantic mutation", mutation))
    bad_case = dict(results["cases"]["command_short"]["law"], common=131)
    try:
        assert_frozen_case("command_short", bad_case)
    except AssertionError:
        rejected.append("named_shortage_relabelled_as_funded")
    else:
        raise AssertionError("checker accepted a relabelled named shortage")
    return rejected


def check_foreign_tokens(fixtures, results):
    count = 0
    donors_by_ref = {}
    for producer, donors in fixtures["fixtures"]["foreign_tokens"].items():
        for donor in donors:
            ref = donor["predecessor"]
            origin = actual_parent("primary", producer, ref["path_index"])
            source_command = current_command(origin["reason"])
            assert source_command is not None
            trace = donor["trace"]
            assert [x["event"] for x in trace] == ["transfer_original_action_reserves", "paid_read_publication"]
            final = trace[-1]["state"]
            wanted = deepcopy(origin["producer"]["core"])
            wanted["fuel"] += 5  # Original command reserve6, separately paid donor read1.
            wanted["source"] += 10
            assert final["parent"]["producer"]["core"] == wanted
            assert final["binding_spent"] == 1 and final["action_spent"] == 0
            assert final["latch"] == donor["token"] == token_for(final)
            assert final["lineage"] == f"primary/{producer}/{ref['path_index']}"
            assert (final["destination_recipient"], final["destination_lineage"], final["command_request"],
                    final["generation"], final["scope"]) == ("recipient", "fixed-recipient-lineage", "recipient-command", 0, True)
            for k in ARCHIVE_UNCHANGED:
                assert final["parent"]["producer"][k] == origin["producer"][k]
            donors_by_ref[object_hash(ref)] = donor["token"]
            count += 1
    for group in results["cases"]["foreign_live_token"]["producers"].values():
        for row in group["paths"]:
            donor = row["foreign_donor"]
            if donor is None:
                continue
            supplied = donors_by_ref[object_hash(donor)]
            assert supplied["lineage"] != row["lineage"]
            presented = [x for x in row["runtime_trace"] if x["event"] == "present_token_from_other_actual_history"]
            assert len(presented) == 1 and presented[0]["state"]["latch"] == supplied
            assert row["metrics"]["completed"] == "0"
    return count


def main():
    for name in ("protocol-freeze.json", "clarifications-freeze.json"):
        receipt = read_json(HERE / name)
        if "source_sha256" in receipt:
            check_receipt_hashes(receipt)
        if "clarifications_sha256" in receipt:
            assert digest(HERE / "PROSPECTIVE-CLARIFICATIONS.md") == receipt["clarifications_sha256"]
    results = read_json(HERE / "results.json")
    fixtures = read_json(HERE / "fixtures.json")
    assert results["source_sha256"] == fixtures["source_sha256"]
    check_receipt_hashes(results)
    if (HERE / "result-files.json").exists():
        packaging = read_json(HERE / "result-files.json")
        archive_path = HERE / packaging["file"]
        assert digest(archive_path) == packaging["compressed_sha256"]
        assert archive_path.stat().st_size == packaging["compressed_bytes"]
        raw = gzip.decompress(archive_path.read_bytes())
        assert hashlib.sha256(raw).hexdigest() == packaging["uncompressed_sha256"]
        assert len(raw) == packaging["uncompressed_bytes"]
        assert object_hash(results["cases"]) == packaging["semantic_cases_sha256"]
        first = read_json(HERE / "first-run-receipt.json")
        # Producer metadata exposes this independently preserved pre-review value.
        first_hashes = [v for k, v in first.items() if "cases" in k and "sha256" in k]
        assert packaging["semantic_cases_sha256"] in first_hashes
        del raw
    contracts = expected_cases()
    assert set(results["cases"]) == set(contracts)
    totals = defaultdict(int)
    totals["paid_foreign_donor_histories"] = check_foreign_tokens(fixtures, results)
    checked = {}
    for name, bundle in results["cases"].items():
        case = bundle["law"]
        assert_frozen_case(name, case)
        prep = fixtures["fixtures"]["preparations"][name]
        if not case["old_endpoint"]:
            own = independent_preparation(case["common"], case["source"], case["port"])
            assert (prep["fuel"], prep["source"], prep["construction_spent"], prep["free_a"], prep["free_h"]) == (
                own["common"], own["source"], own["spent"], own["free_a"], own["free_h"])
            assert len(prep["trace"]) == len(own["trace"])
            for actual, expected in zip(prep["trace"][:-1], own["trace"][:-1]):
                assert actual["plant"] == expected["plant"] and actual["spent"] == expected["spent"]
        checked[name] = {}
        for producer, group in bundle["producers"].items():
            aggregate = defaultdict(Q)
            parent_rows = parent_inputs()[0]["cases"][case["parent_case"]]["producers"][producer]["paths"]
            assert len(group["paths"]) == len(parent_rows)
            assert sum(Q(row["probability"]) for row in group["paths"]) == 1
            for i, row in enumerate(group["paths"]):
                prefixes, physical, replay = check_row(case, producer, i, row)
                totals["continuing_histories"] += 1
                totals["prefix_states"] += prefixes
                totals["physical_prefixes"] += physical
                totals["reader_payments"] += replay
                for k, v in row["metrics"].items():
                    aggregate[k] += Q(row["probability"]) * Q(v)
            assert dict(aggregate) == {k: Q(v) for k, v in group["metrics"].items()}
            totals["aggregate_metrics"] += len(aggregate)
            checked[name][producer] = dict(histories=len(group["paths"]), metrics=len(aggregate))
        totals["comparison_arms"] += len(bundle["producers"])
        print("checked", name, flush=True)
    # All same-current publication dispatches use the same exact budgets/effects.
    for producer in results["cases"]["primary"]["producers"]:
        a = results["cases"]["primary"]["producers"][producer]
        b = results["cases"]["conventional_command"]["producers"][producer]
        assert a["metrics"] == b["metrics"]
    check_receipt_hashes(results)
    supplemental = checker_fault_sensitivity(results)
    inputs = {str(existing_path(HERE / n).relative_to(REPO)): digest(existing_path(HERE / n)) for n in
              ("model.py", "check_model.py", "results.json", "fixtures.json", "PROTOCOL.md",
               "PROSPECTIVE-CLARIFICATIONS.md", "protocol-freeze.json", "clarifications-freeze.json",
               "result-files.json", "first-run-receipt.json")}
    receipt = dict(status="passed", author="separate collaborating AI reviewer",
        oracle_origin="Primitives authored from frozen protocol and parent laws before action/model.py inspection.",
        initial_oracle_sha256="6ee3ffd7d2ac9f65078a07c26effcfffb66ddc6be052ee4745011c3bba06721a",
        imports_model_transition_functions=False, source_sha256=inputs, inherited_source_sha256=results["source_sha256"],
        totals=dict(totals), cases=checked,
        supplemental_checker_review=supplemental,
        limits=["Finite constructed interface; no new empirical observations or normative grounding.",
                "Inactive unindexed producer rows remain in the numerical mixture; RI.Valid formal scope is separate.",
                "Voluntary permission/scheduling is supplied; no enforcement mechanism is ablated.",
                "Later reconstruction reads old records; the new physical action creates no fourth archive frame."])
    (HERE / "model-verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(dict(totals), sort_keys=True))


if __name__ == "__main__":
    main()
