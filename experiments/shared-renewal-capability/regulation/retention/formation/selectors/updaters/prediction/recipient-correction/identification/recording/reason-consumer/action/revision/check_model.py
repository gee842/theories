"""Independent fresh-evidence/revision oracle.

The initial law oracle is authored from PROTOCOL.md and the committed ancestor
laws BEFORE inspecting revision/model.py or any new numerical result.  It never
imports new transition functions.  Its initial bytes and timestamp are retained
in review-history.  Output-schema adapters may be added after that freeze.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
DESIGNATED = (0, 1, 0)
CORE_FUNDS = ("fuel", "recipient", "source", "escrow")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def object_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def read_json(path):
    path = Path(path)
    if not path.exists():
        path = path.with_suffix(path.suffix + ".gz")
    if path.suffix == ".gz":
        with gzip.open(path, "rt") as f:
            return json.load(f)
    return json.loads(path.read_text())


def eq(actual, expected, context):
    assert actual == expected, (context, actual, expected)


def candidate(core):
    return (core["q"] >> 1) & 1


def core_energy(core):
    return sum(core[k] for k in CORE_FUNDS)


def ri_step(core, meta, event, truth=None, available=True, channel="faithful"):
    """One original identification microstep, never using truth to choose q.

    meta uses phase, target, action, receipt, acquired.  The assay-fault control
    is explicitly separate from ordinary missing feedback.  Its physical receipt
    remains unchanged.  A new law is consulted only at actual physical work.
    """
    c, m = deepcopy(core), deepcopy(meta)
    bill = loss = 0
    phase = m["phase"]
    if event == "rent":
        assert c["active"] and phase == "ready" and c["source"] >= 10 and c["fuel"] >= 8
        c["fuel"] -= 1
        bill = 1
        m["phase"] = "rented"
    elif event == "sense":
        assert phase == "rented" and c["fuel"] >= 1
        c["fuel"] -= 1
        bill = 1
        m.update(phase="sensed", target="recipient")
    elif event == "reserve":
        assert phase == "sensed" and m["target"] == "recipient"
        assert c["fuel"] >= 6 and c["source"] >= 10 and c["escrow"] == 0
        c["fuel"] -= 3
        c["escrow"] = 3
        m["phase"] = "reserved"
    elif event == "work":
        assert phase == "reserved" and m["target"] == "recipient"
        assert c["fuel"] >= 3 and c["source"] >= 10 and c["escrow"] == 3
        assert truth in (0, 1)
        action = candidate(c)
        receipt = bool(available and action == truth)
        c["fuel"] -= 3
        c["source"] -= 10
        bill = 3
        if receipt:
            c["recipient"] += 10
        else:
            loss = 10
        m.update(phase="worked", action=action, receipt=receipt)
    elif event == "acquire":
        assert phase == "worked" and m["target"] == "recipient" and c["escrow"] == 3
        assert channel in ("faithful", "missing", "inverted")
        observed = (None if channel == "missing" else
                    bool(m["receipt"]) ^ (channel == "inverted"))
        c["escrow"] -= 1
        bill = 1
        m.update(phase="acquired", acquired=observed)
    elif event == "write":
        assert phase == "acquired" and m["target"] == "recipient" and c["escrow"] == 2
        observed = m["acquired"]
        if observed is not None and not c["last"]:
            if observed:
                c["last"] = 1
            else:
                c["q"] = (c["q"] & 1) + 2 * (1 - candidate(c))
        c["escrow"] -= 2
        bill = 2
        m.update(phase="ready", target=None, action=None, receipt=None, acquired=None)
    elif event == "miss":
        assert phase == "ready" and c["source"] >= 10
        assert not c["active"] or c["fuel"] < 8
        c["source"] -= 10
        c["active"] = False
        loss = 10
    else:
        raise AssertionError(("unknown RI event", event))
    assert min(c[k] for k in CORE_FUNDS) >= 0
    eq(core_energy(c) + bill + loss, core_energy(core), (event, "RI ledger"))
    eq(c["q"] & 1, core["q"] & 1, (event, "actor bit"))
    return c, m, bill, loss


def paid_reset(core, meta, *, adapter, scope, parent_pointer):
    """The supplied two-unit reset, with no truth/change parameter."""
    assert adapter and scope and core["active"] and meta["phase"] == "ready"
    assert core["fuel"] >= 2
    c = deepcopy(core)
    c["fuel"] -= 2
    c["last"] = 0
    eq(c["q"], core["q"], "reset preserves both command bits")
    eq(core_energy(c) + 2, core_energy(core), "reset payment")
    return c, dict(query_pointer=0, old_pointer=parent_pointer,
                   selected_bank="fresh", publication_current=False,
                   latch=None, imported=None)


def new_bank(cells=True, writer=5):
    return dict(cells=[None] * 4 if cells else [], blanks=4 if cells else 0,
                budget=writer, escrow=0, phase="idle", header=None,
                pending=None, record=None, writes=0, spent=0)


def bind_second(bank, query, meta, core, context):
    """Prebind second query before work; not a post-outcome selected frame."""
    assert query == 1 and meta["phase"] == "sensed" and meta["target"] == "recipient"
    assert bank["phase"] == "idle" and bank["record"] is None
    assert bank["blanks"] >= 4 and bank["budget"] >= 5
    b = deepcopy(bank)
    b.update(budget=b["budget"] - 5, escrow=4, blanks=b["blanks"] - 4,
             phase="bound", header=dict(address=1, context=context, action=candidate(core)),
             spent=b["spent"] + 1)
    return b


def acquire_frame(bank, query, before_meta, after_meta, context):
    """Only the actual acquire of the already-bound second query emits."""
    b = deepcopy(bank)
    if b["phase"] != "bound":
        return b
    h = b["header"]
    assert query == h["address"] == 1 and h["context"] == context
    assert before_meta["phase"] == "worked" and before_meta["target"] == "recipient"
    assert after_meta["phase"] == "acquired" and after_meta["target"] == "recipient"
    assert h["action"] == before_meta["action"]
    r = after_meta["acquired"]
    b.update(phase="latched", pending=[int(context), h["action"], int(r is not None), int(bool(r))])
    return b


def write_bit(bank):
    b = deepcopy(bank)
    assert b["phase"] == "latched" and b["escrow"] > 0 and b["writes"] < 4
    i = b["writes"]
    b["cells"][i] = b["pending"][i]
    b["escrow"] -= 1
    b["spent"] += 1
    b["writes"] += 1
    if b["writes"] == 4:
        b["record"] = b["pending"][:]
        b["phase"] = "idle"
    return b


def sparse_decode(bank, address, context):
    """Only physical slot1 exists.  Empty supported addresses are not cells."""
    if address != 1 or bank["record"] is None:
        return None
    recorded_context, action, present, receipt = bank["record"]
    if recorded_context != int(context) or not present or not receipt:
        return None
    return action == DESIGNATED[address]


def paid_reader_cycle(bank, fuel, context, access=(True, True, True), reason=True, decode=None):
    """The unchanged 14+10 paid schedule, retaining interrupted prefixes."""
    r = dict(fuel=fuel, factual=0, reason=0, cache=[None] * 3, read_count=0,
             cache_valid=False, normalized=[None] * 3, orientation=None,
             conflict=False, working=[False] * 3, phase="cold", current=False)
    trace = []

    def pay(n, kind, event):
        if r["fuel"] < n:
            return False
        r["fuel"] -= n
        r[kind] += n
        trace.append(dict(event=event, fuel=r["fuel"], factual=r["factual"], reason=r["reason"]))
        return True

    for event in ("activate", "sense"):
        if not pay(1, "factual", event):
            return r, trace
    for i in range(3):
        if not pay(4, "factual", "decode"):
            return r, trace
        r["cache"][i] = (sparse_decode(bank, i, context) if decode is None else decode(i, context))
        r["read_count"] += 1
    r["cache_valid"] = True
    if not reason:
        # Separate conventional current-cache authority, NOT an unpaid reason
        # publication.  Its direct finite decoder retains the skipped ten units.
        xs = [None if x is None else DESIGNATED[i] if x else 1 - DESIGNATED[i]
              for i, x in enumerate(r["cache"])]
        known = {x for x in xs if x is not None}
        r.update(phase="cache_complete", orientation=next(iter(known)) if len(known) == 1 else None,
                 conflict=len(known) > 1)
        return r, trace
    if not pay(1, "reason", "activate_reason"):
        return r, trace
    r.update(phase="inference", working=[True, False, False])
    for i, desired in enumerate(DESIGNATED):
        if not pay(1, "reason", "infer"):
            return r, trace
        fact = r["cache"][i] if access[i] else None
        r["normalized"][i] = None if fact is None else desired if fact else 1 - desired
    known = set(v for v in r["normalized"] if v is not None)
    r["conflict"] = len(known) > 1
    r["orientation"] = next(iter(known)) if len(known) == 1 else None
    r["phase"] = "paths"
    for i, price in enumerate((1, 1, 2, 2)):
        if not pay(price, "reason", "path"):
            return r, trace
        if i < 2 and r["orientation"] == i:
            r["working"][i + 1] = True
    r.update(phase="published", current=True)
    eq(r["fuel"] + r["factual"] + r["reason"], fuel, "reader ledger")
    return r, trace


def route(reader):
    if not (reader["current"] and reader["phase"] == "published" and reader["cache_valid"]):
        return None
    return { (True, True, False): 0, (True, False, True): 1 }.get(tuple(reader["working"]))


def import_command(core, command):
    assert command in (0, 1) and core["fuel"] >= 1
    c = deepcopy(core)
    c["fuel"] -= 1
    c["q"] = (c["q"] & 1) + 2 * command
    c["last"] = 1
    eq(c["q"] & 1, core["q"] & 1, "import actor bit")
    return c


def precursor(common=227, source=184, adapter=True, cells=True):
    """Actual M42 formation with protected parts; old projection is M32.

    Aggregate extra assembly placement is independent of its ordinal placement
    among the disjoint supplied assemblies.  Every formation transition below
    still checks finite free capacity and fuel; protected parts are not inputs
    to the old reaction's guard or its projected precursor capacity.
    """
    p = dict(a=0, h=0, resident=0, intact=0, local=0, fuel=common,
             source=source, protected_a=0, protected_h=0, bound=0, spent=0)
    trace = []

    def emit(event):
        matter = sum(p[k] for k in ("a", "h", "resident", "protected_a", "protected_h", "bound"))
        assert 0 <= matter <= 42
        eq(p["fuel"] + p["source"] + p["local"] + p["spent"], common + source, "formation energy")
        trace.append(dict(event=event, state=deepcopy(p)))

    emit("initial")
    for kind in ("h",) * 5 + ("a",) * 5:
        assert p["fuel"] > 0 and not p["intact"]
        p["protected_" + kind] += 1
        p["fuel"] -= 1
        p["spent"] += 1
        emit("form_extra_" + kind)
    word = ["h"] * 16 + ["a"] * 3 + ["associate", "repair"] + ["capture", "copy"] * 13 + ["capture"]
    for event in word:
        capacity = 32 - p["a"] - p["h"] - p["resident"] - p["bound"]
        if event in ("a", "h"):
            assert capacity > 0 and not p["intact"] and p["fuel"] > 0
            p[event] += 1
            p["fuel"] -= 1
            p["spent"] += 1
        elif event == "associate":
            assert p["a"] > 0 and not p["resident"] and p["fuel"] > 0
            p["a"] -= 1
            p["resident"] = 1
            p["fuel"] -= 1
            p["spent"] += 1
        elif event == "repair":
            assert p["resident"] and not p["intact"] and p["h"] >= 2 and p["fuel"] > 0
            p["intact"] = 1
            p["fuel"] -= 1
            p["spent"] += 1
        elif event == "capture":
            assert p["intact"] and not p["local"] and p["source"] > 0
            p["source"] -= 1
            p["local"] = 1
        elif event == "copy":
            assert p["resident"] and p["local"] and capacity > 0
            p["a"] += 1
            p["local"] = 0
            p["spent"] += 1
        emit("old_" + event)
    for _ in range(15):
        assert p["a"] > 0 and p["h"] > 0 and p["fuel"] > 0
        p["a"] -= 1
        p["h"] -= 1
        p["bound"] += 2
        p["fuel"] -= 1
        p["spent"] += 1
        emit("old_pair")
    assert p["resident"] == 1 and p["h"] == 1 and p["local"] == 1
    p.update(resident=0, h=0, bound=p["bound"] + 2,
             fuel=p["fuel"] - 1 + p["local"], local=0, spent=p["spent"] + 1)
    emit("old_adapter")
    for _ in range(4 * int(cells) + int(adapter)):
        assert p["protected_a"] and p["protected_h"] and p["fuel"] > 0
        p["protected_a"] -= 1
        p["protected_h"] -= 1
        p["bound"] += 2
        p["fuel"] -= 1
        p["spent"] += 1
        emit("new_pair")
    eq(p["bound"] + p["protected_a"] + p["protected_h"], 42, "all material retained")
    eq(p["spent"], 60 + 4 * int(cells) + int(adapter), "construction bill")
    return p, trace


def prescribed_cases():
    """Independent prospective named-case specification, not result-provided laws."""
    base = dict(parent_case="primary", mode="reason", adapter=True, cells=4,
                recording=True, reader_route=True, import_route=True, flip=True,
                flip_between=False, flip_late=False, availability=[True] * 3,
                channels=["faithful"] * 2, actor=28, writer=5, reader=24, source=30)
    changes = {
        "primary": {}, "no_change": {"flip": False},
        "locked_qualification": {"mode": "locked"},
        "old_archive_replay": {"mode": "old_replay"},
        "attempt_fourth_old_query": {"mode": "fourth_query"},
        "no_adapter": {"adapter": False}, "no_fresh_cells": {"cells": 0},
        "recording_disabled": {"recording": False},
        "reader_route_missing": {"reader_route": False},
        "import_route_missing": {"import_route": False},
        "first_outage": {"availability": [False, True, True]},
        "second_outage": {"availability": [True, False, True]},
        "final_outage": {"availability": [True, True, False]},
        "first_acquisition_missing": {"channels": ["missing", "faithful"]},
        "second_acquisition_missing": {"channels": ["faithful", "missing"]},
        "no_change_first_outage": {"flip": False, "availability": [False, True, True]},
        "change_between_probes": {"flip": False, "flip_between": True},
        "change_before_final_work": {"flip_late": True},
        "false_fresh_channel": {"channels": ["inverted", "inverted"]},
        "actor_short": {"actor": 27}, "writer_short": {"writer": 4},
        "reader_short": {"reader": 23}, "source_none": {"source": 0},
        "source_partial": {"source": 9}, "conventional": {"mode": "conventional"},
        "voluntary_learned_register": {"mode": "voluntary"},
        "parent_consistently_corrupt": {"parent_case": "parent_consistently_corrupt"},
        "parent_scope_loss_after_rent": {"parent_case": "scope_loss_after_rent"},
    }
    return {name: dict(deepcopy(base), **patch) for name, patch in changes.items()}


def parent_states():
    # Committed accepted output is an input, not a regenerated or filtered trial.
    receipt = read_json(PARENT / "model-verification.json")
    for rel, expected in receipt["source_sha256"].items():
        eq(sha(REPO / rel), expected, ("accepted parent input hash", rel))
    return read_json(PARENT / "results.json.gz")


def fresh_schedule(case, parent_row):
    """Independent primary/comparator schedule from the prospective contract.

    This canonical result is deliberately independent of the producer's JSON
    layout.  The history adapter below must compare that layout to these fields.
    Legacy replay/fourth-query alternatives have separate inherited contracts.
    """
    assert case["mode"] in ("reason", "locked", "conventional", "voluntary")
    inherited = parent_row["state"]
    oldp = inherited["parent"]["producer"]
    c = deepcopy(oldp["core"])
    m = dict(phase=oldp["core_phase"], target=oldp["core_target"],
             action=oldp["core_action"], acquired=oldp["acquired_record"], receipt=None)
    bank = new_bank(case["cells"] == 4, case["writer"])
    actor_reserve, source_reserve = case["actor"], case["source"]
    reader_reserve = case["reader"]
    reader_fuel = oldp["reader_fuel"]
    context = True  # prospective adapter's fixed local opening marker
    query_pointer = 0
    services = dict(reset=0, physical=0, binding=0, factual=0, reason=0)
    loss = 0
    reader = None
    physical = []
    probes = []
    final = dict(attempted=False, completed=False, captured=False, action=None, receipt=None)
    z0 = parent_row["observer"]["recipient_law"]
    laws = [z0 ^ case["flip"], z0 ^ case["flip"] ^ case["flip_between"],
            z0 ^ case["flip"] ^ case["flip_between"] ^ case["flip_late"]]
    allowed = inherited["scope"] and inherited["permission"] and inherited["delivery"]
    opened = bool(case["adapter"] and c["active"] and m["phase"] == "ready"
                  and inherited["scope"] and c["fuel"] + actor_reserve >= 2)

    def trial(which, recorded=False):
        nonlocal c, m, bank, query_pointer, loss
        result = dict(attempted=False, completed=False, captured=False, action=None, receipt=None)
        if not allowed or m["phase"] != "ready" or c["source"] < 10:
            return result
        result["attempted"] = True
        events = ["miss"] if not c["active"] or c["fuel"] < 8 else ["rent", "sense", "reserve", "work", "acquire", "write"]
        query = None
        for event in events:
            before = deepcopy(m)
            c, m, bill, waste = ri_step(c, m, event, laws[which], case["availability"][which],
                                       case["channels"][which] if which < 2 else "faithful")
            services["physical"] += bill
            loss += waste
            if event == "sense" and which < 2:
                query = query_pointer
                query_pointer += 1
                if (recorded and query == 1 and case["recording"] and bank["blanks"] >= 4
                        and bank["budget"] >= 5):
                    bank = bind_second(bank, query, m, c, context)
            if event == "work":
                result.update(action=m["action"], receipt=m["receipt"], captured=m["receipt"])
            if event == "acquire" and recorded and bank["phase"] == "bound":
                bank = acquire_frame(bank, query, before, m, context)
                for _ in range(4):
                    bank = write_bit(bank)
            if event == "write":
                result["completed"] = True
            physical.append(dict(trial=which, event=event, core=deepcopy(c), meta=deepcopy(m),
                                 spent=services["physical"], waste=loss))
        return result

    if opened:
        c["fuel"] += actor_reserve
        actor_reserve = 0
        c["source"] += 10 * (source_reserve // 10)
        source_reserve %= 10
        old_flag = c["last"]
        c, _ = paid_reset(c, m, adapter=True, scope=True, parent_pointer=oldp["query_pointer"])
        if case["mode"] == "locked":
            c["last"] = old_flag
        services["reset"] = 2
        probes = [trial(0), trial(1, recorded=True)]
        if case["mode"] == "voluntary":
            final = trial(2)
        else:
            if case["reader_route"]:
                reader_fuel += reader_reserve
                reader_reserve = 0
                reader, _ = paid_reader_cycle(bank, reader_fuel, context,
                                               reason=case["mode"] != "conventional")
                reader_fuel = reader["fuel"]
                services["factual"], services["reason"] = reader["factual"], reader["reason"]
            command = None if reader is None else (reader["orientation"] if case["mode"] == "conventional" and reader["cache_valid"] else route(reader))
            if m["phase"] == "ready" and c["fuel"] >= 1 and inherited["port"]:
                c["fuel"] -= 1
                services["binding"] += 1
                if command is not None and inherited["scope"] and inherited["permission"] and case["import_route"] and c["fuel"] >= 1:
                    c = import_command(c, command)
                    services["binding"] += 1
                    final = trial(2)
    return dict(core=c, meta=m, opened=opened, bank=bank, reader=reader,
                reader_fuel=reader_fuel, actor_reserve=actor_reserve,
                source_reserve=source_reserve, reader_reserve=reader_reserve,
                query_pointer=query_pointer, services=services, loss=loss,
                physical=physical, probes=probes, final=final, laws=laws)


def historical_schedule(case, parent_row):
    """Separately declared old-bank and disabled-fourth-query comparators."""
    assert case["mode"] in ("old_replay", "fourth_query")
    inherited = parent_row["state"]
    oldp = inherited["parent"]["producer"]
    c = deepcopy(oldp["core"])
    m = dict(phase=oldp["core_phase"], target=oldp["core_target"],
             action=oldp["core_action"], acquired=oldp["acquired_record"], receipt=None)
    actor_reserve, source_reserve, reader_reserve = case["actor"], case["source"], case["reader"]
    reader_fuel = oldp["reader_fuel"]
    bank = new_bank(case["cells"] == 4, case["writer"])
    services = dict(reset=0, physical=0, binding=0, factual=0, reason=0)
    loss = 0
    physical = []
    reader = None
    final = dict(attempted=False, completed=False, captured=False, action=None, receipt=None)
    law = parent_row["observer"]["recipient_law"] ^ case["flip"]
    allowed = inherited["scope"] and inherited["permission"] and inherited["delivery"] and m["phase"] == "ready"
    if allowed:
        c["fuel"] += actor_reserve
        actor_reserve = 0
        c["source"] += 10 * (source_reserve // 10)
        source_reserve %= 10
    if case["mode"] == "fourth_query":
        if allowed and c["active"] and c["fuel"] >= 8 and c["source"] >= 10:
            c, m, bill, waste = ri_step(c, m, "rent")
            services["physical"] += bill
            loss += waste
            physical.append(dict(trial="old_fourth", event="rent", core=deepcopy(c), meta=deepcopy(m), spent=bill, waste=loss))
            assert oldp["query_pointer"] >= 3, "old recorder sense blocked only by its actual pointer"
    else:
        def historical_decode(i, context):
            frame = oldp["frames"][i]
            if not frame["complete"] or not frame["valid"]:
                return None
            tag, action, present, receipt = oldp["cells"][4*i:4*i+4]
            if None in (tag, action, present, receipt) or tag != int(context) or not present or not receipt:
                return None
            return action == DESIGNATED[i]
        reader_fuel += reader_reserve
        reader_reserve = 0
        reader, _ = paid_reader_cycle(bank, reader_fuel, oldp["context"], decode=historical_decode)
        reader_fuel = reader["fuel"]
        services["factual"], services["reason"] = reader["factual"], reader["reason"]
        command = route(reader)
        if m["phase"] == "ready" and c["fuel"] >= 1 and inherited["port"]:
            c["fuel"] -= 1
            services["binding"] += 1
            if command is not None and inherited["scope"] and inherited["permission"] and c["fuel"] >= 1:
                c = import_command(c, command)
                services["binding"] += 1
                if allowed and c["source"] >= 10:
                    final["attempted"] = True
                    events = ["miss"] if not c["active"] or c["fuel"] < 8 else ["rent", "sense", "reserve", "work", "acquire", "write"]
                    for event in events:
                        c, m, bill, waste = ri_step(c, m, event, law, case["availability"][2])
                        services["physical"] += bill
                        loss += waste
                        if event == "work":
                            final.update(action=m["action"], receipt=m["receipt"], captured=m["receipt"])
                        if event == "write":
                            final["completed"] = True
                        physical.append(dict(trial=2, event=event, core=deepcopy(c), meta=deepcopy(m),
                                             spent=services["physical"], waste=loss))
    return dict(core=c, meta=m, opened=False, bank=bank, reader=reader,
                reader_fuel=reader_fuel, actor_reserve=actor_reserve,
                source_reserve=source_reserve, reader_reserve=reader_reserve,
                query_pointer=0, services=services, loss=loss,
                physical=physical, probes=[], final=final, laws=[law]*3)


# Producer-schema adapter.  Added only after the prospective oracle snapshots.
# This section imports no producer module or new transition function.
def pview(s):
    return s["parent"]["parent"]["producer"]


def wview(s):
    return s["parent"]["parent"]


def retained(s):
    a, p, w = s["parent"], pview(s), wview(s)
    return (core_energy(p["core"]) + sum(p[k] for k in
            ("archive_fuel", "reader_fuel", "idle_fuel", "archive_escrow", "packet_inflight"))
            + w["extra_reserve"] + w["external_idle"]
            + sum(a[k] for k in ("command_reserve", "later_reserve", "source_reserve", "saved_assembly"))
            + sum(s[k] for k in ("actor_reserve", "writer_fuel", "writer_escrow", "reader_reserve",
                                "source_reserve", "idle_fuel", "idle_source", "saved_assembly")))


def core_paths(value, prefix=()):
    if isinstance(value, dict):
        for k, v in value.items():
            if k == "core":
                yield prefix + (k,)
            yield from core_paths(v, prefix + (k,))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from core_paths(v, prefix + (i,))


def selected_context(s):
    return True if s["selected_bank"] == "fresh" else pview(s)["context"]


def snapshot_command(s, mode):
    p, w = pview(s), wview(s)
    if not (p["cache_valid"] and p["read_count"] == 3 and p["cache_context"] == selected_context(s)):
        return None
    if mode == "conventional":
        values = {DESIGNATED[i] if b else 1-DESIGNATED[i] for i, b in enumerate(p["cache"]) if b is not None}
        return next(iter(values)) if len(values) == 1 else None
    pub = w["publication"]
    if not (w["phase"] == "published" and w["publication_current"] and pub and pub["context"] == selected_context(s)):
        return None
    return {(True, True, False): 0, (True, False, True): 1}.get(tuple(pub["mask"]))


def expected_token(s, mode):
    cmd = snapshot_command(s, mode)
    a = s["parent"]
    if cmd is None or not a["scope"] or not a["permission"]:
        return None
    # Destination values are pinned against the actual parent at every prefix;
    # they are not trusted merely because an incoming token repeats them.
    return dict(command=cmd, bank=s["selected_bank"], epoch=selected_context(s),
                generation=a["generation"], destination="recipient",
                lineage="fixed-recipient-lineage", request="recipient-command")


def check_prefixes(cfg, oldrow, row):
    origin = oldrow["state"]
    oldp = origin["parent"]["producer"]
    rows = row["runtime_trace"]
    eq(rows[0]["event"], "actual_parent_with_protected_extension", "initial event")
    first = rows[0]["state"]
    eq(first["parent"], origin, "exact continuing parent")
    bank = new_bank(cfg["cells"] == 4, cfg["writer"])
    bank_context = True  # predeclared local window marker, not hidden truth
    query, current = 0, None
    meta = dict(phase=oldp["core_phase"], target=oldp["core_target"],
                action=oldp["core_action"], acquired=oldp["acquired_record"], receipt=None)
    extra_pairs = cfg["cells"] + int(cfg["adapter"])
    saved = 5-extra_pairs
    eq(first["extra_construction_spent"], 10+extra_pairs, "extra construction")
    eq(first["fresh"], dict(cells=[None]*4, bound=None, latched=None, written=0, complete=False,
                            valid=True, pending=False, next=0, current=None, epoch=True), "empty new physical bank")
    for key, wanted in dict(actor_reserve=cfg["actor"], writer_fuel=cfg["writer"],
                           writer_escrow=0, reader_reserve=cfg["reader"], source_reserve=cfg["source"],
                           idle_fuel=57-cfg["actor"]-cfg["writer"]-cfg["reader"],
                           idle_source=30-cfg["source"], saved_assembly=saved,
                           free_a=saved, free_h=saved, material=42,
                           cell_count=cfg["cells"], adapter=cfg["adapter"]).items():
        eq(first[key], wanted, ("initial protected resource", key))
    eq(first["initial_continuation_energy"], retained(first), "initial continuation energy")
    initial_energy = retained(first)
    z = oldrow["observer"]["recipient_law"]
    laws = [z ^ cfg["flip"], z ^ cfg["flip"] ^ cfg["flip_between"],
            z ^ cfg["flip"] ^ cfg["flip_between"] ^ cfg["flip_late"]]
    operational = {k: deepcopy(oldp[k]) for k in ("cache", "cache_context", "cache_valid", "read_count")}
    charges = dict(opening=0, trial=0, archive=0, decode=0, reason=0, binding=0)
    waste = 0
    physical = []
    allowed_changes = {"core", "core_phase", "core_target", "core_action", "acquired_record", "reader_fuel",
                       "cache", "cache_context", "cache_valid", "read_count"}
    parent_changes = {"parent", "generation", "latch", "imported"}
    wchanges = {"producer", "active", "phase", "normalized", "orientation", "conflict", "facts",
                "inference_index", "path_index", "working", "publication", "publication_current"}
    generation = origin["generation"]
    selected_bank, opened = "old", False
    for pos, item in enumerate(rows):
        event, s = item["event"], item["state"]
        p, w, a, f = pview(s), wview(s), s["parent"], s["fresh"]
        eq(list(core_paths(s)), [("parent", "parent", "producer", "core")], (event, "one physical core"))
        for k in oldp:
            if k not in allowed_changes:
                eq(p[k], oldp[k], (event, "immutable physical backing", k))
        for k in origin:
            if k not in parent_changes:
                eq(a[k], origin[k], (event, "inherited action fields", k))
        for k in origin["parent"]:
            if k not in wchanges:
                eq(w[k], origin["parent"][k], (event, "inherited workspace/account", k))
        eq(a["destination_recipient"], "recipient", (event, "actual destination"))
        eq(a["destination_lineage"], origin["destination_lineage"], (event, "actual inherited lineage"))
        if a["scope"]:
            eq(a["destination_lineage"], "fixed-recipient-lineage", (event, "authorized lineage"))
        else:
            assert not s["opened"], "the saved identity cut cannot be repaired by opening"
        eq(a["command_request"], "recipient-command", (event, "request"))
        eq(p["core"]["q"] & 1, oldp["core"]["q"] & 1, (event, "actor bit preserved"))
        for k in ("free_a", "free_h", "saved_assembly", "idle_fuel", "idle_source", "material", "cell_count", "adapter"):
            eq(s[k], first[k], (event, "protected unused matter/funds", k))
        eq(32+2*s["cell_count"]+2*int(s["adapter"])+s["free_a"]+s["free_h"], 42, "material")
        if pos:
            prev = rows[pos-1]["state"]
            bp, bw = pview(prev), wview(prev)
            expected_core = deepcopy(bp["core"])
            expected_funds = {k: prev[k] for k in ("actor_reserve", "writer_fuel", "writer_escrow", "reader_reserve", "source_reserve")}
            expected_reader_fuel = bp["reader_fuel"]
            if event == "transfer_protected_actor_and_complete_packets":
                assert bp["core_phase"] == "ready" and prev["parent"]["scope"]
                if cfg["mode"] not in ("old_replay", "fourth_query"):
                    assert cfg["adapter"] and bp["core"]["active"] and bp["core"]["fuel"]+prev["actor_reserve"] >= 2
                expected_core["fuel"] += prev["actor_reserve"]
                expected_core["source"] += 10*(prev["source_reserve"]//10)
                expected_funds.update(actor_reserve=0, source_reserve=prev["source_reserve"]%10)
            elif event in ("paid_open_reset_unknown", "paid_open_locked_qualification"):
                expected_core, _ = paid_reset(bp["core"], meta, adapter=cfg["adapter"], scope=prev["parent"]["scope"], parent_pointer=oldp["query_pointer"])
                if event == "paid_open_locked_qualification":
                    assert cfg["mode"] == "locked"
                    expected_core["last"] = bp["core"]["last"]
                else:
                    assert cfg["mode"] != "locked"
                charges["opening"] += 2
                generation += 1
                selected_bank, opened = "fresh", True
                operational.update(cache=[None]*3, cache_context=None, cache_valid=False, read_count=0)
                assert s["opened"] and s["selected_bank"] == "fresh"
                assert not w["publication_current"] and w["publication"] is None
                assert a["latch"] is None and a["imported"] is None and s["latch"] is None and s["imported"] is None
            elif "_ri_" in event or event == "old_recorder_rent":
                kind, raw = ("old_fourth", "rent") if event == "old_recorder_rent" else event.split("_ri_", 1)
                which = {"probe0": 0, "probe1": 1, "final": 2, "old_fourth": 2}[kind]
                ri_event = {"sense_recipient": "sense", "reserve_feedback": "reserve"}.get(raw, raw)
                assert a["scope"] and a["permission"] and a["delivery"]
                if kind == "final" and cfg["mode"] != "voluntary":
                    assert prev["imported"] == expected_token(prev, cfg["mode"]) and prev["imported"] is not None
                    eq(candidate(bp["core"]), prev["imported"]["command"], "imported command actually issued")
                before_meta = deepcopy(meta)
                expected_core, meta, bill, lost = ri_step(bp["core"], meta, ri_event, laws[which], cfg["availability"][which], cfg["channels"][which] if which < 2 else "faithful")
                charges["trial"] += bill
                waste += lost
                if ri_event == "sense" and which < 2:
                    assert query < 2
                    current, query = query, query+1
                if ri_event == "acquire" and which < 2:
                    # Emission is checked by the following explicit latch event.
                    pending_before_acquire = before_meta
                if kind == "final" and ri_event in ("write","miss"):
                    assert s["latch"] is None and s["imported"] is None, "finished action retires live command authorization"
                    assert a["latch"] is None and a["imported"] is None
                physical.append(dict(trial="old_fourth" if kind == "old_fourth" else which,
                                     event=ri_event, core=deepcopy(expected_core), meta=deepcopy(meta),
                                     spent=charges["trial"], waste=waste))
            elif event == "fresh_prebind_second_query":
                assert cfg["recording"] and cfg["cells"] == 4
                bank = bind_second(bank, current, meta, bp["core"], bank_context)
                expected_funds.update(writer_fuel=bank["budget"], writer_escrow=bank["escrow"])
                charges["archive"] = bank["spent"]
            elif event == "fresh_latch_actual_acquisition":
                bank = acquire_frame(bank, current, pending_before_acquire, meta, bank_context)
            elif event == "fresh_paid_bit_write":
                bank = write_bit(bank)
                expected_funds["writer_escrow"] = bank["escrow"]
                charges["archive"] = bank["spent"]
            elif event == "transfer_protected_reader_reserve":
                assert cfg["reader_route"]
                expected_reader_fuel += prev["reader_reserve"]
                expected_funds["reader_reserve"] = 0
            elif event == "factual_activate":
                assert expected_reader_fuel >= 1
                expected_reader_fuel -= 1
                charges["decode"] += 1
                operational.update(cache=[None]*3, cache_context=None, cache_valid=False, read_count=0)
                assert not w["publication_current"]
            elif event == "factual_paid_epoch_sense":
                assert expected_reader_fuel >= 1 and operational["read_count"] == 0
                expected_reader_fuel -= 1
                charges["decode"] += 1
                operational["cache_context"] = selected_context(prev)
            elif event.startswith("factual_four_cell_read_"):
                i = int(event.rsplit("_", 1)[1])
                eq(i, operational["read_count"], "bounded ordered factual read")
                assert expected_reader_fuel >= 4 and operational["cache_context"] == selected_context(prev)
                expected_reader_fuel -= 4
                charges["decode"] += 4
                if prev["selected_bank"] == "fresh":
                    bit = sparse_decode(bank, i, bank_context)
                else:
                    frame = oldp["frames"][i]
                    tag, action, presence, receipt = oldp["cells"][4*i:4*i+4]
                    bit = (action == DESIGNATED[i]) if frame["complete"] and frame["valid"] and None not in (tag,action,presence,receipt) and tag == int(oldp["context"]) and presence and receipt else None
                operational["cache"][i] = bit
                operational["read_count"] += 1
            elif event == "factual_complete":
                assert operational["read_count"] == 3
                operational["cache_valid"] = operational["cache_context"] == selected_context(prev)
            elif event == "reason_activate_root":
                assert cfg["mode"] != "conventional" and operational["cache_valid"] and expected_reader_fuel >= 1
                expected_reader_fuel -= 1
                charges["reason"] += 1
                eq(w["normalized"], [None]*3, "initial normalized cache")
                eq(w["working"], [True,False,False], "supplied root")
                assert not w["publication_current"]
            elif event.startswith("paid_reason_inference_"):
                i = int(event.rsplit("_",1)[1])
                assert expected_reader_fuel >= 1 and bw["phase"] == "inference" and bw["inference_index"] == i
                expected_reader_fuel -= 1
                charges["reason"] += 1
                normalized = deepcopy(bw["normalized"])
                x = operational["cache"][i]
                normalized[i] = None if x is None else DESIGNATED[i] if x else 1-DESIGNATED[i]
                eq(w["normalized"], normalized, "inference uses actual accessed cache")
                eq(w["inference_index"], i+1, "inference progress")
            elif event == "combine_reasons":
                assert bw["inference_index"] == 3
                known = {x for x in bw["normalized"] if x is not None}
                orientation = next(iter(known)) if len(known) == 1 else None
                eq(w["orientation"], orientation, "evidence-only orientation")
                eq(w["conflict"], len(known)>1, "conflict")
                eq(w["facts"], [orientation == 0,orientation == 1,None] if orientation is not None else [None]*3, "derived facts")
            elif event.startswith("paid_reason_path_"):
                i = int(event.rsplit("_",1)[1]); price=(1,1,2,2)[i]
                assert bw["path_index"] == i and expected_reader_fuel >= price and bw["phase"] == "paths"
                expected_reader_fuel -= price
                charges["reason"] += price
                mask = deepcopy(bw["working"])
                if i < 2 and bw["facts"][i] is True:
                    mask[i+1] = True
                eq(w["working"], mask, "actual rooted path prefix")
                eq(w["path_index"], i+1, "path progress")
            elif event == "publish_current_reason":
                assert bw["path_index"] == 4 and bw["phase"] == "paths" and operational["cache_valid"]
                eq(w["publication"], dict(context=selected_context(prev), mask=bw["working"]), "publication from paid closure")
                assert w["publication_current"] and w["phase"] == "published"
            elif event == "paid_command_read":
                assert a["port"] and meta["phase"] == "ready" and expected_core["fuel"] >= 1
                expected_core["fuel"] -= 1
                charges["binding"] += 1
                eq(s["latch"], expected_token(prev,cfg["mode"]), "actual typed current command")
                assert s["imported"] is None
            elif event == "paid_command_import":
                assert cfg["import_route"] and a["scope"] and a["permission"] and meta["phase"] == "ready"
                eq(prev["latch"], expected_token(prev,cfg["mode"]), "import live identity")
                assert prev["latch"] is not None
                expected_core = import_command(bp["core"],prev["latch"]["command"])
                charges["binding"] += 1
                eq(s["imported"],prev["latch"],"installed provenance")
                assert s["latch"] is None, "import consumes the pre-import latch"
            elif event in ("opening_blocked", "fresh_admission_unavailable", "reader_route_unavailable",
                           "command_read_unavailable", "command_import_blocked", "old_recorder_fourth_sense_blocked",
                           "old_recorder_rent_unavailable", "old_recorder_scope_or_phase_blocked",
                           "old_replay_scope_or_phase_blocked", "voluntary_actual_register_without_reader_or_import",
                           "continuation_complete") or event.endswith(("_unaffordable", "_scope_or_phase_blocked", "_no_complete_packet")):
                if event == "opening_blocked":
                    assert not (cfg["adapter"] and bp["core"]["active"] and meta["phase"] == "ready" and a["scope"] and bp["core"]["fuel"]+prev["actor_reserve"] >= 2)
                if event == "old_recorder_fourth_sense_blocked":
                    assert meta["phase"] == "rented" and oldp["query_pointer"] == 3
                if event.endswith("_no_complete_packet"):
                    assert bp["core"]["source"] < 10
            else:
                raise AssertionError(("unrecognized prefix event", event))
            eq(p["core"], expected_core, (event,"complete core successor"))
            eq(p["reader_fuel"], expected_reader_fuel, (event,"single reader payment"))
            for k,v in expected_funds.items():
                eq(s[k],v,(event,"fund successor",k))
        for k,v in operational.items():
            eq(p[k],v,(event,"actual cache",k))
        for key,mkey in (("core_phase","phase"),("core_target","target"),("core_action","action"),("acquired_record","acquired")):
            eq(p[key],meta[mkey],(event,"recipient physical phase",key))
        eq(f["next"],query,(event,"new query pointer"))
        eq(f["current"],current,(event,"actual new query"))
        eq(f["epoch"],True,(event,"fixed local marker, not truth"))
        eq(f["cells"],bank["cells"] if cfg["cells"] else [None]*4,(event,"actual written cells"))
        eq(f["written"],bank["writes"],(event,"paid written prefix"))
        eq(f["complete"],bank["record"] is not None,(event,"record completeness"))
        eq(f["bound"],None if bank["header"] is None else [int(bank["header"]["context"]),bank["header"]["action"]],(event,"prebound identity"))
        eq(f["latched"],bank["pending"],(event,"actual acquisition frame"))
        eq(s["new_spent"],charges,(event,"new charges"))
        eq(s["new_waste"],waste,(event,"actual packet losses"))
        eq(a["generation"],generation,(event,"opening generation"))
        eq(s["selected_bank"],selected_bank,(event,"only paid opening selects fresh bank"))
        eq(s["opened"],opened,(event,"opening cannot be forged or undone"))
        eq(retained(s)+sum(charges.values())+waste,initial_energy,(event,"prefix conservation"))
    eq(rows[-1]["state"],row["state"],"endpoint equals final prefix")
    return physical


def check_preparation(cfg, result, oldprep):
    expected, _ = precursor(adapter=cfg["adapter"], cells=cfg["cells"] == 4)
    saved = 5-cfg["cells"]-int(cfg["adapter"])
    for k,v in dict(material=42, initial_common=227, initial_source=184,
                    construction_spent=expected["spent"], extra_construction_spent=15-saved,
                    free_a=saved, free_h=saved, saved_assembly=saved,
                    bound_fresh_cells=cfg["cells"], adapter=cfg["adapter"],
                    old_preparation_sha256=object_sha(oldprep)).items():
        eq(result[k],v,("preparation endpoint",k))
    oldword=[x for x in oldprep["trace"][1:] if "bound_parts" not in x and x["event"] != "existing_adapter"]
    expected_names=(["initial"]+["form_a"]*5+["form_h"]*5+[x["event"] for x in oldword]
                    +["assemble_fresh_cell"]*cfg["cells"]+["assemble_window_adapter"]*int(cfg["adapter"])
                    +["old_assembly"]*15+["old_adapter_and_exact_projection"])
    eq([r["event"] for r in result["trace"]],expected_names,"fixed preparation word")
    a=h=resident=intact=local=bound=spent=0
    fuel,source=227,184
    for i,r in enumerate(result["trace"]):
        e=r["event"]
        if e in ("form_a","form_h"):
            assert not intact and a+h+resident+bound<42 and fuel>0
            a+=e=="form_a";h+=e=="form_h";fuel-=1;spent+=1
        elif e=="bind_a":
            assert a>0 and not resident and fuel>0
            a-=1;resident=1;fuel-=1;spent+=1
        elif e=="repair":
            assert resident and not intact and h>=2 and fuel>0
            intact=1;fuel-=1;spent+=1
        elif e=="capture":
            assert intact and local==0 and source>0
            source-=1;local=1
        elif e=="copy_a":
            assert resident and local and a+h+resident+bound<42
            a+=1;local=0;spent+=1
        elif e.startswith("assemble_") or e=="old_assembly":
            assert a>0 and h>0 and fuel>0
            a-=1;h-=1;bound+=2;fuel-=1;spent+=1
        elif e=="old_adapter_and_exact_projection":
            assert resident and h>0 and local==1 and fuel>0
            h-=1;resident=0;bound+=2;fuel=fuel-1+local;local=0;spent+=1
            eq(r["parent_fuel"],fuel-57-saved,"old fuel projection")
            eq(r["parent_source"],source-30,"old source projection")
            eq(r["parent_fuel"],oldprep["fuel"],"actual saved old preparation")
            eq(r["parent_source"],oldprep["source"],"actual saved old source")
        elif e!="initial":
            raise AssertionError(e)
        if "plant" in r:
            eq(r["plant"],[a,h,resident,intact,local,fuel,source],("actual formation",i))
        eq(r["spent"],spent,("actual formation charges",i))
        eq(fuel+source+local+spent,411,"formation conservation")
        assert a+h+resident+bound<=42
    for old,new in zip(oldword,result["trace"][11:11+len(oldword)]):
        a,h,r,i,l,f,s=old["plant"]
        eq(new["plant"],[a+5,h+5,r,i,l,f+62,s+30],"every old formation state's additive projection")
    return len(result["trace"])


def row_expected_metrics(cfg,oldrow,e,state):
    old=oldrow["state"];op=old["parent"]["producer"]
    c=e["core"];bank=e["bank"];reader=e["reader"]
    services=e["services"]
    spent=dict(opening=services["reset"],trial=services["physical"],archive=bank["spent"],
               decode=services["factual"],reason=services["reason"],binding=services["binding"])
    saved=5-cfg["cells"]-int(cfg["adapter"])
    # Use an authenticated old state only when the new opening never happened.
    if reader is not None:
        cmd=reader["orientation"] if cfg["mode"]=="conventional" and reader["cache_valid"] else route(reader)
    elif e["opened"]:
        cmd=None
    else:
        original=dict(parent=old,selected_bank="old",fresh={"epoch":True})
        cmd=snapshot_command(original,cfg["mode"])
    oldretained=Fraction(oldrow["metrics"]["retained"])
    initial=oldretained+87+saved
    rem=initial-sum(spent.values())-e["loss"]
    f=e["final"]
    frame=bank["record"]
    metrics=dict(final_actor=c["fuel"],final_recipient=c["recipient"],final_source=c["source"],
        final_reader=e["reader_fuel"],retained=rem,delivered=c["recipient"]-op["core"]["recipient"],
        source_remainder=e["source_reserve"],new_spent=sum(spent.values()),new_waste=e["loss"],
        extra_construction_spent=15-saved,opened=int(e["opened"]),
        probes_completed=sum(x["completed"] for x in e["probes"]),
        probe_captures=sum(x["captured"] for x in e["probes"]),
        fresh_complete=int(frame is not None),fresh_positive=int(frame is not None and frame[2] and frame[3]),
        supported_command=int(cmd is not None),supported_wrong=int(cmd is not None and cmd!=e["laws"][2]),
        final_attempted=int(f["attempted"]),final_completed=int(f["completed"]),
        final_captured=int(f["captured"]),final_wrong=int(f["action"] is not None and f["action"]!=e["laws"][2]),
        new_reason_publication=int(e["opened"] and reader is not None and reader["current"]),
        idle_fuel=57-cfg["actor"]-cfg["writer"]-cfg["reader"],idle_source=30-cfg["source"],
        saved_assembly=saved,actor_reserve=e["actor_reserve"],writer_fuel=bank["budget"],reader_reserve=e["reader_reserve"])
    metrics.update({k+"_spent":v for k,v in spent.items()})
    return metrics


def check_row(cfg,producer,index,oldrow,row):
    eq(row["predecessor"],dict(case=cfg["parent_case"],producer=producer,path_index=index,
                               state_sha256=object_sha(oldrow["state"])),"actual parent reference")
    eq(row["probability"],oldrow["probability"],"unfiltered inherited mass")
    e=(historical_schedule if cfg["mode"] in ("old_replay","fourth_query") else fresh_schedule)(cfg,oldrow)
    s=row["state"];p=pview(s)
    eq(p["core"],e["core"],"independent complete endpoint core")
    for key,mkey in (("core_phase","phase"),("core_target","target"),("core_action","action"),("acquired_record","acquired")):
        eq(p[key],e["meta"][mkey],("endpoint metadata",key))
    for key in ("actor_reserve","reader_reserve","source_reserve","opened"):
        eq(s[key],e[key],("endpoint control/resource",key))
    eq(p["reader_fuel"],e["reader_fuel"],"endpoint reader")
    eq(s["fresh"]["next"],e["query_pointer"],"endpoint local pointer")
    eq(row["observer"],dict(old_law=oldrow["observer"]["recipient_law"],probe_laws=e["laws"][:2],final_law=e["laws"][2],
                            strict_parent=bool(oldrow["observer"]["strict_parent"] and oldrow["state"]["captured"])),"observer diagnostics independent from runtime")
    physical=check_prefixes(cfg,oldrow,row)
    eq(physical,e["physical"],"complete independently reconstructed physical word")
    metrics=row_expected_metrics(cfg,oldrow,e,s)
    eq({k:Fraction(v) for k,v in row["metrics"].items()},
       {k:Fraction(v) for k,v in metrics.items()},"every endpoint metric")
    oldbill=sum(Fraction(oldrow["metrics"][k]) for k in
        ("construction_spent","prefix_spent","prefix_waste","inherited_core_spent","inherited_core_waste",
         "archive_spent","factual_spent","reason_spent","binding_spent","action_spent","action_waste"))
    eq(oldbill+metrics["extra_construction_spent"]+metrics["new_spent"]+metrics["new_waste"]+metrics["retained"],411,"whole actual history ledger")
    if e["reader"] is not None:
        r=e["reader"];w=wview(s)
        eq(p["cache"],r["cache"],"complete endpoint factual cache")
        eq(p["cache_valid"],r["cache_valid"],"endpoint factual validity")
        if cfg["mode"] != "conventional":
            eq(w["normalized"],r["normalized"],"complete normalized evidence")
            eq(w["working"],r["working"],"complete rooted result")
            eq(w["publication_current"],r["current"],"current publication iff paid completion")
        else:
            assert not w["publication_current"],"conventional lookup is not unpaid reason publication"
    return dict(metrics=metrics,prefixes=len(row["runtime_trace"]),physical=len(physical))


def check_supersession(data):
    directory=HERE/"review-history/retire-command-token"
    preservation=read_json(directory/"preservation.json")
    for filename,h in preservation["files_sha256"].items():eq(sha(directory/filename),h,("preserved rejected artifact",filename))
    first=read_json(directory/"results.json.gz")
    firstreceipt=read_json(directory/"first-run-receipt.json")
    eq(object_sha(first["cases"]),firstreceipt["cases_sha256"],"preserved first semantic cases")
    eq(sha(HERE/"first-run-receipt.json"),sha(directory/"first-run-receipt.json"),"first receipt not rewritten")
    expected=deepcopy(first["cases"])
    changed=0
    for case in expected.values():
        for arm in case["producers"].values():
            for row in arm["paths"]:
                consumed=retired=False
                for item in row["runtime_trace"]:
                    event,s=item["event"],item["state"]
                    original=deepcopy(s)
                    if event=="paid_command_import":consumed=True
                    if event in ("final_ri_write","final_ri_miss"):retired=True
                    if consumed:s["latch"]=None
                    if retired:
                        s["latch"]=s["imported"]=None
                        s["parent"]["latch"]=s["parent"]["imported"]=None
                    changed+=original!=s
                row["state"]=deepcopy(row["runtime_trace"][-1]["state"])
    eq(expected,data["cases"],"only justified token retirement changes across all saved cases")
    supersession=read_json(HERE/"supersession.json")
    eq(changed,supersession["changed_trace_snapshots"],"token-only changed snapshot count")
    eq(object_sha(data["cases"]),read_json(HERE/"reviewed-run-receipt.json")["cases_sha256"],"reviewed semantics")
    return dict(preserved_files=len(preservation["files_sha256"]),changed_snapshots=changed,
                physical_cost_probability_and_metric_fields_unchanged=True)


def check_reporting(data):
    report=read_json(HERE/"reporting.json")
    for rel,h in report["source_sha256"].items():
        actual=hashlib.sha256(gzip.decompress((HERE/"results.json.gz").read_bytes())).hexdigest() if rel=="decompressed_results" else sha(HERE/rel)
        eq(actual,h,("report provenance",rel))
    checked=0
    for name,c in data["cases"].items():
        for producer,arm in c["producers"].items():
            sums={}
            for row in arm["paths"]:
                s=row["state"];p,w=pview(s),wview(s)
                fresh=s["opened"] and s["selected_bank"]=="fresh"
                cmd=snapshot_command(s,c["law"]["mode"])
                cache=bool(p["cache_valid"] and p["read_count"]==3 and p["cache_context"]==selected_context(s))
                pub=bool(cache and w["publication_current"] and w["phase"]=="published" and w["publication"] and w["publication"]["context"]==selected_context(s))
                wrong=cmd is not None and cmd!=row["observer"]["final_law"]
                values=dict(fresh_supported_command=int(fresh and cmd is not None),
                    historical_supported_command=int(not fresh and cmd is not None),
                    fresh_wrong_at_final_law=int(fresh and wrong),
                    historical_wrong_at_final_law=int(not fresh and wrong),
                    fresh_completed_publication=int(fresh and pub),
                    fresh_rootonly_publication=int(fresh and pub and w["publication"]["mask"]==[True,False,False]),
                    fresh_completed_fact_cache=int(fresh and cache))
                eq(values["fresh_supported_command"]+values["historical_supported_command"],int(row["metrics"]["supported_command"]),"support partition")
                eq(values["fresh_wrong_at_final_law"]+values["historical_wrong_at_final_law"],int(row["metrics"]["supported_wrong"]),"wrong-command partition")
                for k,v in values.items():sums[k]=sums.get(k,Fraction(0))+Fraction(row["probability"])*v
            eq(sums,{k:Fraction(v) for k,v in report["cases"][name][producer].items()},("independent reporting",name,producer))
            checked+=len(sums)
    return checked


def check_formal_receipt():
    directory=HERE/"formal";receipt=read_json(directory/"verification.json")
    assert receipt["status"]=="passed" and receipt["fresh_temporary_build"] and receipt["source_unchanged_during_check"]
    eq(receipt["toolchain"],"leanprover/lean4:v4.29.1","pinned Lean")
    eq(sha(directory/"check.py"),receipt["checker_sha256"],"formal checker")
    eq(sha(directory/"lean-toolchain"),receipt["toolchain_sha256"],"toolchain file")
    eq(sha(receipt["compiler_binary"]),receipt["compiler_sha256"],"actual compiler binary")
    for rel,h in receipt["protocol_sources_sha256"].items():eq(sha(REPO/rel),h,("formal frozen interface",rel))
    new=empty=total=inherited=0
    for item in receipt["modules"]:
        source=REPO/item["source"];output=directory/item["output"]
        eq(sha(source),item["source_sha256"],("formal source",item["module"]))
        eq(sha(output),item["output_sha256"],("compiler log",item["module"]))
        assert item["exit_code"]==0 and item["clean_dependency_audit"]
        audits=re.findall(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",output.read_text())
        eq([name for name,_ in audits],item["audited_declarations"],("actual compiler audits",item["module"]))
        for _,axioms in audits:
            assert set(x.strip() for x in axioms.split(",") if x.strip()) <= {"propext","Quot.sound","Classical.choice"}
        total+=len(audits)
        if item["module"] in ("RevisionPreparation","FreshRevision","RevisionWitness"):
            new+=len(audits);empty+=sum(not axioms for _,axioms in audits)
        else:
            original=subprocess.check_output(["git","show",f"12cfd21:{item['source']}"],cwd=REPO)
            eq(hashlib.sha256(original).hexdigest(),item["source_sha256"],("unchanged inherited formal source",item["module"]))
            inherited+=1
    eq(new,receipt["new_audited_declarations"],"new audit count")
    return dict(modules=len(receipt["modules"]),new_declarations=new,total_declarations=total,
                new_axiom_free=empty,new_standard_only=new-empty,inherited_sources_at_parent_commit=inherited)


def adversarial_checks(data,parents):
    """Post-baseline mutation tests; not extra prospective experiment arms."""
    cfg=prescribed_cases()["primary"];producer="variable"
    arm=data["cases"]["primary"]["producers"][producer]
    i=arm["witness_path_index"];row=arm["paths"][i]
    oldrow=parents["cases"]["primary"]["producers"][producer]["paths"][i]
    assert row["state"]["fresh"]["complete"] and row["state"]["final_completed"]
    out={}
    def rejects(name,mutate,whole=False):
        bad=deepcopy(row);mutate(bad)
        try:
            if whole:check_row(cfg,producer,i,oldrow,bad)
            else:check_prefixes(cfg,oldrow,bad)
        except AssertionError as exc:
            out[name]=dict(rejected=True,reason=str(exc)[:450])
        else:raise AssertionError(("mutation survived",name))
    def from_event(bad,label,fn):
        live=False
        for item in bad["runtime_trace"]:
            if item["event"]==label:live=True
            if live:fn(item["state"],item["event"])
        bad["state"]=deepcopy(bad["runtime_trace"][-1]["state"])
    def stale_pipeline(bad):
        oldp=oldrow["state"]["parent"]["producer"]
        frames=[oldp["cells"][j:j+4] for j in range(0,12,4)]
        historical=next(x for x in frames if None not in x and x[2] and x[3])
        stale=[1,historical[1],1,1]  # relabel historical content as the new local epoch
        assert stale[1]!=row["state"]["fresh"]["cells"][1]
        def replace(s,event):
            f=s["fresh"];p,w=pview(s),wview(s)
            f["bound"]=stale[:2]
            if f["latched"] is not None:f["latched"]=stale[:]
            f["cells"]=stale[:f["written"]]+[None]*(4-f["written"])
            if p["read_count"]>1:p["cache"][1]=bool(stale[1])
            if w["inference_index"]>1:w["normalized"][1]=stale[1]
            if w["phase"] in ("paths","published"):
                w["orientation"]=stale[1];w["facts"]=[stale[1]==0,stale[1]==1,None]
                w["working"]=[True,w["path_index"]>0 and stale[1]==0,w["path_index"]>1 and stale[1]==1]
                if w["publication"]:w["publication"]["mask"]=w["working"][:]
            for key in ("latch","imported"):
                if s[key] is not None:s[key]["command"]=stale[1]
        from_event(bad,"fresh_prebind_second_query",replace)
    rejects("old_positive_relabelled_fresh_through_all_storage_and_inference_stages",stale_pipeline)
    def free_reset(bad):
        def f(s,event):pview(s)["core"]["fuel"]+=2;s["new_spent"]["opening"]-=2
        from_event(bad,"paid_open_reset_unknown",f)
    rejects("free_reset_with_balanced_refund",free_reset)
    def truth_leak(bad):
        x=next(x for x in bad["runtime_trace"] if x["event"]=="paid_open_reset_unknown")
        c=pview(x["state"])["core"];c["q"]=(c["q"]&1)+2*bad["observer"]["probe_laws"][0]
    rejects("hidden_law_writes_candidate_during_reset",truth_leak)
    rejects("second_counted_core",lambda b:b["runtime_trace"][1]["state"].update(duplicate={"core":deepcopy(pview(b["runtime_trace"][1]["state"])["core"])}))
    rejects("actor_destination_instead_of_recipient",lambda b:from_event(b,"paid_open_reset_unknown",lambda s,e:s["parent"].update(destination_recipient="actor")))
    rejects("actor_target_in_intermediate_physical_phase",lambda b:next(x for x in b["runtime_trace"] if x["event"]=="probe1_ri_sense_recipient")["state"]["parent"]["parent"]["producer"].update(core_target="actor"))
    rejects("old_full_pointer_reset",lambda b:from_event(b,"paid_open_reset_unknown",lambda s,e:pview(s).update(query_pointer=0)))
    rejects("retain_old_qualification_in_reset_mode",lambda b:next(x for x in b["runtime_trace"] if x["event"]=="paid_open_reset_unknown")["state"]["parent"]["parent"]["producer"]["core"].update(last=1))
    def refund_bit(bad):
        live=False
        for item in bad["runtime_trace"]:
            s=item["state"]
            if item["event"]=="fresh_paid_bit_write" and s["fresh"]["written"]==4:live=True
            if live:s["writer_fuel"]+=1;s["new_spent"]["archive"]-=1
        bad["state"]=deepcopy(bad["runtime_trace"][-1]["state"])
    rejects("unpaid_last_bit_with_balanced_refund",refund_bit)
    def restore_latch(bad):
        for item in bad["runtime_trace"]:
            if item["event"]=="paid_command_import":item["state"]["latch"]=deepcopy(item["state"]["imported"])
    rejects("reusable_preimport_latch",restore_latch)
    def restore_authorization(bad):
        token=next(x["state"]["imported"] for x in bad["runtime_trace"] if x["event"]=="paid_command_import")
        from_event(bad,"final_ri_write",lambda s,e:s.update(imported=deepcopy(token)))
    rejects("postwrite_authorization_reanimated",restore_authorization)
    rejects("silently_conditioned_probability",lambda b:b.update(probability=str(Fraction(b["probability"])/2)),whole=True)
    # Actual funded endpoint, not an injected favorable fixture.
    repeat=data["cases"]["primary"]["producers"]["variable"]["paths"][6]["state"]
    c=pview(repeat)["core"]
    assert c["active"] and c["fuel"]>=8 and c["source"]>=10 and pview(repeat)["core_phase"]=="ready"
    assert repeat["parent"]["scope"] and repeat["parent"]["permission"] and repeat["parent"]["delivery"]
    assert repeat["imported"] is None and snapshot_command(repeat,"reason") is not None
    out["actual_funded_repeat_requires_new_paid_import"]=dict(passed=True,case="primary",producer="variable",path_index=6,
        fuel=c["fuel"],source=c["source"],authorization=None)
    imports=[x["state"] for x in row["runtime_trace"] if x["event"]=="paid_command_import"]
    assert imports and all(s["latch"] is None for s in imports)
    out["actual_import_cannot_reimport_consumed_latch"]=dict(passed=True,count=len(imports))
    return out


def main():
    before={str(p.relative_to(REPO)):sha(p) for p in
            [HERE/"check_model.py",HERE/"model.py",HERE/"PROTOCOL.md",HERE/"PROSPECTIVE-CLARIFICATIONS.md",
             HERE/"cases.json",HERE/"protocol-freeze.json",HERE/"results.json.gz",HERE/"fixtures.json",
             HERE/"first-run-receipt.json",HERE/"reviewed-run-receipt.json",HERE/"supersession.json",
             HERE/"result-files.json",HERE/"reporting.py",HERE/"reporting.json",HERE/"formal/verification.json"]}
    cases=prescribed_cases()
    eq(read_json(HERE/"cases.json")["cases"],cases,"independent28-case protocol table")
    freeze=read_json(HERE/"protocol-freeze.json")
    for rel,h in freeze["source_sha256"].items():eq(sha(REPO/rel),h,("frozen dependency",rel))
    data=read_json(HERE/"results.json.gz");parents=parent_states()
    for rel,h in data["source_sha256"].items():eq(sha(REPO/rel),h,("numerical dependency",rel))
    files=read_json(HERE/"result-files.json")
    raw=gzip.decompress((HERE/"results.json.gz").read_bytes())
    eq(hashlib.sha256(raw).hexdigest(),files["uncompressed_sha256"],"exact JSON bytes")
    eq(sha(HERE/"results.json.gz"),files["compressed_sha256"],"gzip bytes")
    supersession=check_supersession(data)
    fixtures=read_json(HERE/"fixtures.json");oldprep=read_json(PARENT/"fixtures.json")["fixtures"]["preparations"]["primary"]
    count=dict(cases=0,arms=0,histories=0,prefixes=0,physical_microsteps=0,formation_prefixes=0,metrics=0)
    eq(set(data["cases"]),set(cases),"every prescribed case")
    for name,cfg in cases.items():
        count["cases"]+=1
        count["formation_prefixes"]+=check_preparation(cfg,fixtures["preparations"][name],oldprep)
        d=data["cases"][name];eq(d["law"],cfg,(name,"case law"))
        oldprods=parents["cases"][cfg["parent_case"]]["producers"]
        eq(set(d["producers"]),set(oldprods),(name,"all inherited producers"))
        for producer,arm in d["producers"].items():
            count["arms"]+=1;oldrows=oldprods[producer]["paths"]
            eq(len(arm["paths"]),len(oldrows),(name,producer,"every inherited path"))
            total={};mass=Fraction(0)
            for i,(oldrow,row) in enumerate(zip(oldrows,arm["paths"])):
                try:r=check_row(cfg,producer,i,oldrow,row)
                except AssertionError as err:raise AssertionError((name,producer,i,*err.args)) from err
                q=Fraction(row["probability"]);mass+=q
                for k,v in r["metrics"].items():total[k]=total.get(k,Fraction(0))+q*v
                count["histories"]+=1;count["prefixes"]+=r["prefixes"];count["physical_microsteps"]+=r["physical"]
            eq(mass,1,(name,producer,"exact mass"))
            eq({k:Fraction(v) for k,v in arm["metrics"].items()},total,(name,producer,"weighted metrics"))
            count["metrics"]+=len(total)
    report_count=check_reporting(data)
    formal=check_formal_receipt()
    adversarial=adversarial_checks(data,parents)
    for rel,h in before.items():eq(sha(REPO/rel),h,("changed during independent check",rel))
    receipt=dict(status="passed",scope="Independent prospective law/schedule oracle and every saved continuing prefix; finite declared cases, not empirical evidence.",
                 counts=count,source_sha256={**data["source_sha256"],**before},
                 prospective_oracle_sha256="244b2cb971c9a5c2caf60aeae5e0e881f856f780b96640b6266728fdb984446a",
                 prospective_complete_schedule_sha256="53054110b05776e8dda850df33ffd20feb5eb40e4eeea3b747579c086633cfca",
                 supersession=supersession,reporting_metrics=report_count,formal_receipt_checks=formal,
                 post_baseline_adversarial_tests=adversarial)
    (HERE/"model-verification.json").write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(count,sort_keys=True))


if __name__ == "__main__":
    main()
