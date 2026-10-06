#!/usr/bin/env python3
"""Independent evaluative-succession oracle: prospective law layer.

Written from DRAFT-PROTOCOL.md, INTERFACE.md, literal cases.json and the
accepted ancestor laws before any new succession implementation or outcomes.
This initial file specifies the ownership, lifecycle, account and action
guards independently.  A concrete serialization/history adapter will be
added after the agreed schema is available.  Preserve these initial bytes.

Only the already accepted independent revision checker may be loaded for
its RI/record/reader laws.  No new producer transition functions are imported.
No experiments are executed when this file is imported.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, replace
from pathlib import Path
import hashlib
import importlib.util
import json
import gzip
from fractions import Fraction
from datetime import datetime, timezone
import traceback

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
COMPONENTS = ("carrier", "controller", "cell0", "cell1", "cell2", "cell3",
              "window", "port", "access")
INITIAL_ORDER = COMPONENTS[:-1]
COMMON_CAPS = {"assembly": 9, "copy": 2, "actor": 26,
               "writer": 5, "reader": 24}
SOURCE_CAP = 30
_OLD = None


def old_checker():
    """The accepted independent oracle, not an implementation under review."""
    global _OLD
    if _OLD is None:
        filename = PARENT.parent / "check_model.py"
        spec = importlib.util.spec_from_file_location("accepted_revision_oracle", filename)
        _OLD = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_OLD)
    return _OLD


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def object_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def read_json(path):
    path = Path(path)
    with gzip.open(path, "rt") if path.suffix == ".gz" else path.open() as stream:
        return json.load(stream)


def actual_parent(row, accepted_catalog):
    """Lossless accepted evaluator endpoint, reconstructed from old ancestry."""
    s = row["state"]
    full = deepcopy(accepted_catalog[s["parent_ref"]]["state"])
    p = old_checker().pview(full)
    p["core"] = deepcopy(s["core"])
    p.update(deepcopy(s["physical"]))
    full["parent"].update(deepcopy(s["binding"]))
    return full


def old_account_partition(row, accepted_catalog):
    """All accepted unused stocks other than the sole core/native packets.

    The named partition comes from ancestor energy definitions.  It does not
    accept a producer-supplied retained total or an anonymous balancing offset.
    """
    s = row["state"]
    f = actual_parent(row, accepted_catalog)
    a, w, p = f["parent"], old_checker().wview(f), old_checker().pview(f)
    groups = (
        ("old_archive", p, ("archive_fuel", "reader_fuel", "idle_fuel", "archive_escrow", "packet_inflight")),
        ("old_reasons", w, ("extra_reserve", "external_idle")),
        ("old_action", a, ("command_reserve", "later_reserve", "source_reserve", "saved_assembly")),
        ("old_revision", f, ("actor_reserve", "writer_fuel", "writer_escrow", "reader_reserve",
                             "source_reserve", "idle_fuel", "idle_source", "saved_assembly")),
        ("old_evaluation", s["reserves"], ("later_fuel", "later_source", "idle_common", "idle_source", "saved_assembly")),
        ("old_native", s["native"], ("training_reserve",)),
    )
    out = {name+"."+key: obj[key] for name, obj, keys in groups for key in keys}
    assert all(isinstance(x, int) and x >= 0 for x in out.values())
    actual = old_checker().core_energy(s["core"]) + sum(out.values()) + sum(s["native"]["packets"])
    assert actual == row["metrics"]["retained"], "accepted endpoint energy partition"
    return out


def parent_admission(row, accepted_catalog):
    s = row["state"]
    f = actual_parent(row, accepted_catalog)
    p, w = old_checker().pview(f), old_checker().wview(f)
    old_writer_pending = (p["pending"] is not None or p["archive_escrow"] != 0
                          or p["packet_inflight"] != 0
                          or any(r["bound"] is not None and not r["complete"] for r in p["frames"]))
    fresh_writer_pending = (f["fresh"]["pending"] or f["writer_escrow"] != 0
                            or (f["fresh"]["bound"] is not None and not f["fresh"]["complete"]))
    # All frozen configured entrances are actual completed old reader cycles.
    # A future cold entrance must supply its preserved init/cold event proof;
    # this adapter never treats configured cleared bits as that ancestry.
    return Admission(
        phase=s["physical"]["core_phase"], active=s["core"]["active"], q=s["core"]["q"],
        native_count=s["native"]["count"], native_mode=s["native"]["mode"],
        native_cells=s["inventory"]["memory_cells"], opportunity=s["port"]["opportunity_phase"],
        old_port_present=s["port"]["built"], old_port_mode=s["port"]["mode"],
        scope=s["binding"]["scope"], support_present=bool(s["inventory"]["adapter"]),
        native_pending=s["native"]["mode"] not in {"ready", "closed"},
        reader_pending=not reader_quiet(p, w),
        writer_pending=bool(old_writer_pending or fresh_writer_pending),
        assessment_pending=s["port"]["mode"] not in {"idle", "consumed"},
        core_escrow=s["core"]["escrow"], writer_escrows=(p["archive_escrow"], f["writer_escrow"]))


@dataclass(frozen=True)
class Admission:
    """An adapter must establish these from the ACTUAL accepted endpoint.

    Completed old publications need not be absent: they will be invalidated.
    No correctness, supported-command, n threshold, permission or law field
    occurs in the admission predicate.  q bounds are physical, not semantic.
    """
    phase: str
    active: bool
    q: int
    native_count: int
    native_mode: str
    native_cells: int
    opportunity: str
    old_port_present: bool
    old_port_mode: str
    scope: bool
    support_present: bool
    native_pending: bool
    reader_pending: bool
    writer_pending: bool
    assessment_pending: bool
    core_escrow: int
    writer_escrows: tuple[int, ...]


def admitted(d):
    return (d.phase == "ready" and d.active and 0 <= d.q < 4
            and d.native_count == 3 and d.native_mode == "closed"
            and d.native_cells == 6 and d.opportunity == "finished"
            and (not d.old_port_present or d.old_port_mode == "consumed")
            and d.scope and d.support_present
            and not (d.native_pending or d.reader_pending or d.writer_pending
                     or d.assessment_pending)
            and d.core_escrow == 0 and all(x == 0 for x in d.writer_escrows))


def reader_quiet(producer, workspace, *, actual_cold_ancestry=False):
    """Prospectively agreed concrete no-pending predicate, not positivity.

    The accepted numerical reader sets workspace phase=factual_reading before
    activation, distinguishing paid count0 from cold. Cold provenance must be
    established from actual initialization/an explicit old cold operation.
    Completion need not be current or contain any non-root reason.
    """
    complete = (workspace["phase"] == "published" and not workspace["active"]
                and workspace["inference_index"] == 3 and workspace["path_index"] == 4
                and producer["read_count"] == 3 and workspace["publication"] is not None)
    cold = (actual_cold_ancestry and workspace["phase"] == "cold"
            and not workspace["active"] and workspace["publication"] is None
            and not workspace["publication_current"]
            and workspace["inference_index"] == 0 and workspace["path_index"] == 0
            and producer["read_count"] == 0 and producer["cache"] == [None]*3
            and producer["cache_context"] is None and not producer["cache_valid"]
            and workspace["working"] == [False]*3
            and workspace["normalized"] == [None]*3 and workspace["facts"] == [None]*3
            and workspace["orientation"] is None and not workspace["conflict"])
    return bool(complete or cold)


def grants(old, grant, *, same_recipient):
    """New actor gates are conjunctions, never resets to true."""
    return {"scope": bool(old["scope"] and same_recipient and grant["scope"]),
            "permission": bool(old["permission"] and grant["permission"]),
            "delivery": bool(old["delivery"] and grant["delivery"])}


def budgets(cfg):
    key = {"assembly": "assembly_fuel", "copy": "copy_fuel",
           "actor": "actor_fuel", "writer": "writer_fuel", "reader": "reader_fuel"}
    available = {k: cfg[v] for k, v in key.items()}
    assert all(0 <= available[k] <= COMMON_CAPS[k] for k in COMMON_CAPS)
    assert 0 <= cfg["new_source"] <= SOURCE_CAP
    return {"common": available,
            "idle_common": {k: COMMON_CAPS[k] - available[k] for k in COMMON_CAPS},
            "source": cfg["new_source"], "idle_source": SOURCE_CAP-cfg["new_source"]}


def handoff_state(d, donor_core, donor_meta, donor_other_accounts,
                  native_sources, cfg):
    """Normalize ownership without creating a second donor or child balance.

    donor_other_accounts must list every accepted unused compartment except
    the donor core and three native sources.  The future adapter will derive
    that partition from the accepted full history, never trust a producer sum.
    """
    assert donor_core["q"] == d.q and donor_meta["phase"] == d.phase
    assert donor_core["escrow"] == d.core_escrow
    b = budgets(cfg)
    return dict(admitted=admitted(d), lifecycle="donor_live", copy_latch=None,
                initial_cursor=0, held=list(COMPONENTS), built=[], omitted=[],
                donor_core=deepcopy(donor_core), donor_meta=deepcopy(donor_meta),
                retired_donor=None, child=None, child_meta=None,
                old_accounts=deepcopy(donor_other_accounts), native_sources=list(native_sources),
                reserves=b["common"], idle_common=b["idle_common"],
                source_reserve=b["source"], idle_source=b["idle_source"],
                writer_budget=0, writer_escrow=0, reader_fuel=0, reason_reserve=0,
                gates=None, n_access=False, released=False, reader_bound=False,
                bank_id=cfg["child_binding"]["bank_id"], current_bank=None,
                old_publication_current=True, spent=0, waste=0)


def handoff_energy(s):
    """Exactly one live patient account, plus explicit retired custody."""
    core = s["child"] if s["child"] is not None else s["donor_core"]
    # Historical retired_donor is audit data, never summed a second time.
    return (old_checker().core_energy(core) + sum(s["old_accounts"].values())
            + sum(s["native_sources"]) + sum(s["reserves"].values())
            + sum(s["idle_common"].values()) + s["source_reserve"] + s["idle_source"]
            + s["writer_budget"] + s["writer_escrow"]
            + s["reader_fuel"] + s["reason_reserve"])


def material(s):
    assert len(set(s["held"] + s["built"] + s["omitted"])) == 9
    assert set(s["held"] + s["built"] + s["omitted"]) == set(COMPONENTS)
    return 60 + 2*(len(s["held"])+len(s["built"])+len(s["omitted"]))


def ledger(before, after, bill=0, loss=0):
    assert handoff_energy(after)+bill+loss == handoff_energy(before)
    assert after["spent"] == before["spent"]+bill
    assert after["waste"] == before["waste"]+loss
    assert material(before) == material(after) == 78


def initial_assembly(s, component, *, omitted_window=False):
    assert s["admitted"] and s["lifecycle"] == "donor_live"
    assert s["initial_cursor"] < len(INITIAL_ORDER)
    assert component == INITIAL_ORDER[s["initial_cursor"]] and component in s["held"]
    t = deepcopy(s)
    t["held"].remove(component)
    if omitted_window:
        assert component == "window"
        # The specified missing component is held inaccessible, not destroyed.
        t["omitted"].append(component)
        assert t["reserves"]["assembly"] >= 1
        t["reserves"]["assembly"] -= 1
        t["idle_common"]["assembly"] += 1
        bill = 0
    else:
        assert s["reserves"]["assembly"] >= 1
        t["reserves"]["assembly"] -= 1
        t["built"].append(component)
        t["spent"] += 1
        bill = 1
    t["initial_cursor"] += 1
    ledger(s, t, bill)
    return t


def copy_read(s):
    assert s["admitted"] and s["lifecycle"] == "donor_live"
    assert s["initial_cursor"] == len(INITIAL_ORDER)
    assert {"carrier", "controller"} <= set(s["built"])
    assert s["reserves"]["copy"] >= 1 and s["copy_latch"] is None
    t = deepcopy(s)
    t["reserves"]["copy"] -= 1
    t["spent"] += 1
    t["copy_latch"] = s["donor_core"]["q"]
    t["lifecycle"] = "donor_quiesced"
    ledger(s, t, 1)
    return t


def copy_write(s, cfg, old_guards):
    assert s["lifecycle"] == "donor_quiesced" and s["copy_latch"] in range(4)
    assert s["reserves"]["copy"] >= 1 and s["child"] is None
    assert cfg["qualification_recipe"] in {"unknown", "forced_qualified"}
    t = deepcopy(s)
    t["reserves"]["copy"] -= 1
    t["spent"] += 1
    # Retired control is retained as audit data; its cash moves into custody.
    t["retired_donor"] = dict(core=deepcopy(s["donor_core"]), meta=deepcopy(s["donor_meta"]))
    assert s["donor_core"]["escrow"] == 0
    for name in ("fuel", "source"):
        assert "retired_donor_"+name not in t["old_accounts"]
        t["old_accounts"]["retired_donor_"+name] = s["donor_core"][name]
    t["child"] = dict(q=s["copy_latch"], last=int(cfg["qualification_recipe"] == "forced_qualified"),
                      fuel=0, source=0, recipient=s["donor_core"]["recipient"], escrow=0, active=True)
    t["child_meta"] = dict(phase="ready", target=None, action=None, receipt=None, acquired=None)
    t["gates"] = grants(old_guards, cfg["child_grant"],
                         same_recipient=cfg["child_binding"]["physical_same_recipient"])
    t["copy_latch"] = None
    t["lifecycle"] = "child_committed"
    ledger(s, t, 1)
    assert t["child"]["q"] == s["donor_core"]["q"]
    return t


def assemble_access(s, cfg):
    assert s["lifecycle"] == "child_committed" and s["retired_donor"] is not None
    assert {"window", "cell0", "cell1", "cell2", "cell3"} <= set(s["built"])
    assert "access" in s["held"] and s["reserves"]["assembly"] >= 1
    assert not s["reader_bound"]
    t = deepcopy(s)
    t["held"].remove("access")
    t["built"].append("access")
    t["reserves"]["assembly"] -= 1
    t["spent"] += 1
    t["reader_bound"] = True
    t["current_bank"] = s["bank_id"]
    t["old_publication_current"] = False
    t["n_access"] = cfg["n_access"]
    t["lifecycle"] = "child_commissioned"
    ledger(s, t, 1)
    return t


def release_child(s):
    assert s["lifecycle"] == "child_commissioned" and not s["released"]
    t = deepcopy(s)
    amount = (s["source_reserve"] // 10)*10
    t["child"]["fuel"] += s["reserves"]["actor"]
    t["reserves"]["actor"] = 0
    t["child"]["source"] += amount
    t["source_reserve"] -= amount
    t["released"] = True
    ledger(s, t)
    return t


def active_donor_enabled(s):
    return s["lifecycle"] == "donor_live"


def child_query_start(*, commissioned, gates, phase, query, locked, source):
    return (commissioned and all(gates.values()) and phase == "ready"
            and query < 2 and not locked and source >= 10)


def recipient_step(core, meta, event, *, gates, authorized, truth=None,
                   available=True, channel="faithful"):
    """The original RI microstep behind a recipient-only, one-use wrapper.

    Neither choice nor copying receives truth.  Only work may consult it.
    Scope/permission/delivery loss cannot undo already-worked escrow settlement.
    """
    assert authorized
    assert event in {"rent", "sense", "reserve", "work", "acquire", "write", "miss"}
    if event not in {"acquire", "write"}:
        assert all(gates.values())
    if event in {"reserve", "work", "acquire", "write"}:
        assert meta["target"] == "recipient"
    return old_checker().ri_step(core, meta, event, truth=truth,
                                 available=available, channel=channel)


def bind_second(bank, query, meta, core, *, actual_bank, required_bank):
    assert actual_bank == required_bank
    return old_checker().bind_second(bank, query, meta, core, True)


def emitted_frame(bank, query, before, after, *, actual_bank, required_bank):
    assert actual_bank == required_bank
    # An actual acquire, prebound header and query1 are all required.
    return old_checker().acquire_frame(bank, query, before, after, True)


def reader_cycle(bank, fuel, *, locked, actual_bank, required_bank):
    assert locked and bank["phase"] == "idle" and bank["escrow"] == 0
    assert actual_bank == required_bank
    # Same 14+10 tariff and reason word in every evaluation arm.
    return old_checker().paid_reader_cycle(bank, fuel, True, reason=True)


@dataclass(frozen=True)
class Evaluation:
    fuel: int
    mode: str = "idle"
    spent: int = 0
    opportunity: str = "open"


def supported(*, current, same_recipient, scope, n_access, native_count,
              candidate, command):
    return (current and same_recipient and scope and n_access and native_count == 3
            and command in (0, 1) and candidate == command)


def evaluation_read(s, *, built, phase, known):
    """Unknown/inaccessible inputs still incur the enabled one-unit attempt."""
    assert built and s.mode == "idle" and s.opportunity == "open"
    assert phase == "ready" and s.fuel >= 1
    return replace(s, fuel=s.fuel-1, spent=s.spent+1,
                   mode="read" if known else "consumed")


def evaluate(s, n, *, known, arm):
    assert s.mode == "read" and s.fuel >= 1 and known and 0 <= n <= 7
    assert arm in {"shared", "identity_gated", "conventional"}
    if arm == "shared":
        help_now = 10*n > 64
    elif arm == "identity_gated":
        help_now = False
    else:
        help_now = (False, False, False, False, False, False, False, True)[n]
    return replace(s, fuel=s.fuel-1, spent=s.spent+1,
                   mode="help" if help_now else "abstain")


def cut_read_or_assessment(s):
    if s.mode in {"read", "help", "abstain"}:
        return replace(s, mode="consumed")
    return s


def action_start(s, *, known, gates, phase, source):
    """Even a denied start consumes the selected opportunity.

    With a packet, active/fuel subsequently determines original rent vs miss;
    absent source is a closed blocked attempt, never a false receipt.
    """
    assert s.mode == "help" and s.opportunity == "open"
    enabled = known and all(gates.values()) and phase == "ready" and source >= 10
    return replace(s, mode="executing" if enabled else "consumed",
                   opportunity="inflight" if enabled else "closed"), enabled


def action_step_allowed(s, meta, event):
    if s.mode != "executing" or s.opportunity != "inflight":
        return False
    # Once rent has begun, no route returns to rent/miss under this token.
    if event in {"rent", "miss"}:
        return meta["phase"] == "ready"
    return meta["phase"] != "ready"


def action_finished(s, event):
    assert s.mode == "executing" and s.opportunity == "inflight"
    assert event in {"write", "miss"}
    return replace(s, mode="consumed", opportunity="closed")


def selected_step(s, core, meta, event, *, gates, truth=None,
                  available=True, channel="faithful"):
    """Atomic event: settlement retirement cannot be omitted by a caller."""
    assert action_step_allowed(s, meta, event)
    c, m, bill, loss = recipient_step(core, meta, event, gates=gates,
                                     authorized=True, truth=truth,
                                     available=available, channel=channel)
    t = action_finished(s, event) if event in {"write", "miss"} else s
    return t, c, m, bill, loss


def close_without_action(s):
    assert s.mode in {"abstain", "consumed", "idle"}
    return replace(s, mode="consumed", opportunity="closed")


def strict_design_account():
    """A prospective identity, not a claimed reached outcome."""
    return {"original": 590, "old_expense_and_loss": 410,
            "extra_formation": 18, "new_service": 66, "new_packet_loss": 10,
            "recipient": 80, "isolated_native_source": 6,
            "material": 78, "old_material": 60, "new_pairs": 9}


ADVERSARIAL_OBLIGATIONS = (
    "Every child arm uses the same actual parent shared endpoint and original mass.",
    "Incomplete ancestors fail admission before assembly; they retain kit and funds.",
    "All previously unused parent accounts are inert; one patient is counted once.",
    "Read consumes one unit and quiesces donor; missing write cannot reactivate it.",
    "Write consumes latch; failed access leaves donor retired, child unfunded.",
    "No public donor event or second release is enabled after the handoff.",
    "New child q starts from actual donor q; actor bit cannot be retargeted.",
    "Primary qualification is unknown; a true clamp is a distinct declared control.",
    "New-bank provenance requires actual query1 prebinding/acquisition, not a tag.",
    "Old frame substitution must fail even if replacement bits and later cache agree.",
    "Probe work and selected work are distinct reported effects; neither proves need.",
    "Hidden efficacy enters physical work only, never schedule/copy/revision/evaluation.",
    "Source shortage blocks/misses under the exact law, never synthesizes zero feedback.",
    "Three inherited native sources stay isolated and are never consumed for child use.",
    "Writer4 cannot bind; full5 escrow prevents later fabricated writer shortage.",
    "Reader preserves blocked RI phase; unpaid consumer suffix cannot publish.",
    "All arms share fresh facts/n access and fees before post-perception routing.",
    "Missing n pays enabled read1 then consumes; it is not n0 or a fixed constant.",
    "Permission loss preserves facts and evaluation but blocks inquiry/action as timed.",
    "Scope/n loss after read invalidates pending authorization and preserves its bill.",
    "One selected opportunity cannot start a second rent/miss after write or miss.",
    "Scope loss after work permits only charged settlement, not another work.",
    "Actual n0 ancestry is separate from equal-information child-arm comparisons.",
    "No old OpenStep or reset2 is claimed for the declared paid child birth law.",
    "Late law change can defeat action despite a correctly produced earlier certificate.",
)


def expected_schedule(cfg, arm, row, accepted_catalog):
    """Independent complete prescribed continuation of an actual donor.

    Authored after prospective freeze, before inspecting new producer code or
    outcomes. Event spelling and serialization can subsequently be projected;
    these guards, bills, query binding and paid prefixes come from the contract.
    """
    old = old_checker()
    ds = row["state"]
    full = actual_parent(row, accepted_catalog)
    admission = parent_admission(row, accepted_catalog)
    dm = dict(phase=ds["physical"]["core_phase"], target=ds["physical"]["core_target"],
              action=ds["physical"]["core_action"], acquired=ds["physical"]["acquired_record"], receipt=None)
    h = handoff_state(admission, ds["core"], dm, old_account_partition(row, accepted_catalog),
                      ds["native"]["packets"], cfg)
    h["old_publication_current"] = old.wview(full)["publication_current"]
    bank = old.new_bank(True, 0)
    reader = dict(fuel=0, factual=0, reason=0, cache=[None]*3, read_count=0,
                  cache_valid=False, normalized=[None]*3, orientation=None,
                  conflict=False, working=[False]*3, phase="cold", current=False,
                  cache_context=None, active=False, facts=[None]*3,
                  inference_index=0, path_index=0)
    port = Evaluation(0)
    query, locked, current_query = 0, False, None
    outcome = dict(probe_attempts=0, probe_completed=0, probe_captures=0,
                   selected_attempted=False, selected_completed=False, selected_capture=False,
                   assessment=None, commands=[])
    trace = []
    baseline = handoff_energy(h)
    original_actor_bit = ds["core"]["q"] & 1
    probe_law = row["observer"]["actual_work_law"]
    if cfg["efficacy_before_probes"] == "opposite_donor_final_law":
        probe_law = 1-probe_law
    else:
        assert cfg["efficacy_before_probes"] == "same_as_donor_final_law"
    final_law = (1-probe_law if cfg["efficacy_before_final"] == "opposite_probe_law" else probe_law)
    assert cfg["efficacy_before_final"] in {"opposite_probe_law", "unchanged_from_probes"}

    def emit(event):
        h["writer_budget"], h["writer_escrow"] = bank["budget"], bank["escrow"]
        h["reader_fuel"] = reader["fuel"]
        assert handoff_energy(h)+h["spent"]+h["waste"] == baseline
        assert material(h) == 78
        if h["child"] is not None:
            assert h["child"]["q"] & 1 == original_actor_bit
        trace.append(dict(event=event, handoff=deepcopy(h), bank=deepcopy(bank),
                          reader=deepcopy(reader), port=deepcopy(port.__dict__),
                          query=query, current_query=current_query, locked=locked,
                          outcomes=deepcopy(outcome)))

    def finish():
        return dict(trace=trace, admitted=admitted(admission), baseline=baseline,
                    inherited_retained=baseline-96, observer_probe_law=probe_law,
                    observer_final_law=final_law)

    emit("entry")
    if not h["admitted"]:
        emit("admission_blocked")
        return finish()
    for component in INITIAL_ORDER:
        omitted = component == "window" and not cfg["window_present"]
        if not omitted and h["reserves"]["assembly"] < 1:
            emit("assembly_blocked:"+component)
            return finish()
        h = initial_assembly(h, component, omitted_window=omitted)
        emit(("omit:" if omitted else "assemble:")+component)
    if h["reserves"]["copy"] < 1:
        emit("copy_read_blocked")
        return finish()
    h = copy_read(h)
    emit("copy_read")
    if h["reserves"]["copy"] < 1:
        emit("copy_write_blocked")
        return finish()
    h = copy_write(h, cfg, ds["binding"])
    emit("copy_write")
    if "window" not in h["built"] or h["reserves"]["assembly"] < 1:
        emit("access_blocked")
        return finish()
    h = assemble_access(h, cfg)
    emit("access")
    h = release_child(h)
    bank["budget"] = h["reserves"]["writer"]
    h["reserves"]["writer"] = 0
    emit("release_child")

    def trial(which):
        nonlocal h, bank, query, current_query, port
        c, m = h["child"], h["child_meta"]
        selected = which == 2
        label = "selected" if selected else "probe"+str(which)
        if selected:
            cmd = old.route(reader)
            known = supported(current=reader["current"], same_recipient=True,
                              scope=h["gates"]["scope"], n_access=h["n_access"], native_count=ds["native"]["count"],
                              candidate=old.candidate(c), command=cmd)
            port, enabled = action_start(port, known=known, gates=h["gates"],
                                         phase=m["phase"], source=c["source"])
            outcome["selected_attempted"] = True
            emit(label+":initiate")
        else:
            outcome["probe_attempts"] += 1
            enabled = child_query_start(commissioned=True, gates=h["gates"], phase=m["phase"],
                                         query=query, locked=locked, source=c["source"])
        if not enabled:
            emit(label+":blocked")
            return
        first_event = "miss" if not c["active"] or c["fuel"] < 8 else "rent"
        events = ["miss"] if first_event == "miss" else ["rent", "sense", "reserve", "work", "acquire", "write"]
        for event in events:
            if event not in {"acquire", "write"} and not all(h["gates"].values()):
                emit(label+":interrupted")
                return
            before = deepcopy(h["child_meta"])
            if selected:
                port, c, m, bill, loss = selected_step(port, h["child"], h["child_meta"], event,
                    gates=h["gates"], truth=final_law if event == "work" else None,
                    available=cfg["availability"][which], channel=cfg["feedback"][which])
            else:
                c, m, bill, loss = recipient_step(h["child"], h["child_meta"], event,
                    gates=h["gates"], authorized=True, truth=probe_law if event == "work" else None,
                    available=cfg["availability"][which], channel=cfg["feedback"][which])
            h["child"], h["child_meta"] = c, m
            h["spent"] += bill
            h["waste"] += loss
            if event == "sense" and not selected:
                current_query = query
                query += 1
            if event == "work":
                outcome["commands"].append(dict(kind=label, action=m["action"], receipt=m["receipt"]))
                if selected:
                    outcome["selected_capture"] = bool(m["receipt"])
                else:
                    outcome["probe_captures"] += int(m["receipt"])
            if event == "write":
                if selected:
                    outcome["selected_completed"] = True
                else:
                    outcome["probe_completed"] += 1
            emit(label+":"+event)
            if event == "rent" and selected and cfg["scope_cut"] == "after_final_rent":
                h["gates"]["scope"] = False
                emit("scope_cut:after_final_rent")
            if event == "sense" and not selected and current_query == 1:
                if bank["budget"] >= 5 and bank["phase"] == "idle":
                    bank = bind_second(bank, current_query, m, c, actual_bank=h["current_bank"], required_bank=h["bank_id"])
                    h["spent"] += 1
                    emit("bank_bind")
                else:
                    emit("bank_bind_blocked")
            if event == "acquire" and not selected and bank["phase"] == "bound":
                bank = emitted_frame(bank, current_query, before, m,
                                     actual_bank=h["current_bank"], required_bank=h["bank_id"])
                emit("bank_latch")
            # The concrete serialization chooses RI settlement before frame
            # flushing. Both orders are permitted after latching and commute:
            # RI's two-unit escrow and the writer's four-unit escrow are disjoint.
            if event == "write" and not selected:
                while bank["phase"] == "latched":
                    bank = old.write_bit(bank)
                    h["spent"] += 1
                    emit("bank_write:"+str(bank["writes"]-1))

    trial(0)
    trial(1)
    if bank["phase"] != "idle" or bank["escrow"] != 0:
        emit("bank_lock_blocked")
        return finish()
    locked = True
    reader["fuel"] += h["reserves"]["reader"]
    h["reserves"]["reader"] = 0
    emit("lock_and_release_reader")

    def pay_reader(cost, family, event):
        if reader["fuel"] < cost:
            emit(event+":blocked")
            return False
        reader["fuel"] -= cost
        reader[family] += cost
        h["spent"] += cost
        return True

    reader_complete = True
    reader["phase"] = "factual_reading"
    for event in ("reader_activate", "reader_sense"):
        if not pay_reader(1, "factual", event):
            reader_complete = False
            break
        if event == "reader_sense":
            reader["cache_context"] = True
        emit(event)
    if reader_complete:
        for i in range(3):
            if not pay_reader(4, "factual", "reader_decode:"+str(i)):
                reader_complete = False
                break
            reader["cache"][i] = old.sparse_decode(bank, i, True)
            reader["read_count"] += 1
            emit("reader_decode:"+str(i))
        if reader_complete:
            reader["cache_valid"] = True
            emit("reader_complete")
    if reader_complete and pay_reader(1, "reason", "reason_activate"):
        reader["phase"] = "inference"
        reader["active"] = True
        reader["working"] = [True, False, False]
        emit("reason_activate")
        for i, desired in enumerate((0, 1, 0)):
            if not pay_reader(1, "reason", "reason_infer:"+str(i)):
                reader_complete = False
                break
            fact = reader["cache"][i]
            reader["normalized"][i] = None if fact is None else desired if fact else 1-desired
            reader["inference_index"] += 1
            emit("reason_infer:"+str(i))
        if reader_complete:
            known = {x for x in reader["normalized"] if x is not None}
            reader["conflict"] = len(known) > 1
            reader["orientation"] = next(iter(known)) if len(known) == 1 else None
            z = reader["orientation"]
            reader["facts"] = [z == 0, z == 1, None] if z is not None else [None]*3
            reader["phase"] = "paths"
            emit("reason_combine")
            for i, cost in enumerate((1, 1, 2, 2)):
                if not pay_reader(cost, "reason", "reason_path:"+str(i)):
                    reader_complete = False
                    break
                if i < 2 and reader["orientation"] == i:
                    reader["working"][i+1] = True
                reader["path_index"] += 1
                emit("reason_path:"+str(i))
            if reader_complete:
                reader.update(phase="published", current=True, active=False)
                emit("reason_publish")
    if cfg["permission_cut"] == "after_consumer":
        h["gates"]["permission"] = False
        emit("permission_cut:after_consumer")

    c = h["child"]
    port = replace(port, fuel=c["fuel"])
    if h["child_meta"]["phase"] != "ready" or c["fuel"] < 1:
        emit("evaluation_read_blocked")
        port = close_without_action(port)
        emit("complete")
        return finish()
    cmd = old.route(reader)
    known = supported(current=reader["current"], same_recipient=True,
                      scope=h["gates"]["scope"], n_access=h["n_access"], native_count=ds["native"]["count"],
                      candidate=old.candidate(c), command=cmd)
    port = evaluation_read(port, built=True, phase=h["child_meta"]["phase"], known=known)
    h["child"]["fuel"] -= 1
    h["spent"] += 1
    emit("evaluation_read")
    if cfg["scope_cut"] == "after_evaluation_read":
        h["gates"]["scope"] = False
        port = cut_read_or_assessment(port)
        emit("scope_cut:after_evaluation_read")
    if cfg["n_cut"] == "after_evaluation_read":
        h["n_access"] = False
        port = cut_read_or_assessment(port)
        emit("n_cut:after_evaluation_read")
    if port.mode != "read":
        port = close_without_action(port)
        emit("opportunity_closed")
        emit("complete")
        return finish()
    if h["child"]["fuel"] < 1:
        emit("evaluation_write_blocked")
        emit("complete")
        return finish()
    port = evaluate(port, ds["native"]["n"], known=True, arm=arm)
    h["child"]["fuel"] -= 1
    h["spent"] += 1
    outcome["assessment"] = port.mode == "help"
    emit("evaluation_write")
    if port.mode == "help":
        trial(2)
    elif port.mode == "abstain":
        port = close_without_action(port)
        emit("opportunity_closed")
    emit("complete")
    return finish()


def canonical_event(event, state):
    direct = {"extension.at_actual_donor":"entry", "handoff.admission_blocked":"admission_blocked",
              "handoff.read":"copy_read", "handoff.read_blocked":"copy_read_blocked",
              "handoff.write_unknown":"copy_write", "handoff.write_forced_qualified":"copy_write",
              "handoff.write_blocked":"copy_write_blocked", "access.assemble_bind":"access",
              "access.assemble_bind_blocked":"access_blocked", "accounts.release_child":"release_child",
              "bank.prebind_query1":"bank_bind", "bank.prebind_blocked":"bank_bind_blocked",
              "bank.latch_actual_acquisition":"bank_latch", "bank.lock_blocked":"bank_lock_blocked",
              "bank.lock_and_release_reader":"lock_and_release_reader", "factual.activate":"reader_activate",
              "factual.sense_context":"reader_sense", "factual.complete":"reader_complete",
              "reason.activate":"reason_activate", "reason.combine":"reason_combine",
              "reason.publish":"reason_publish", "evaluation.read":"evaluation_read",
              "evaluation.read_blocked":"evaluation_read_blocked", "evaluation.write":"evaluation_write",
              "evaluation.abstain":"opportunity_closed", "continuation.complete":"complete"}
    if event in direct:
        return direct[event]
    if event == "evaluation.write_blocked":
        return "evaluation_write_blocked" if state["port"]["mode"] == "read" else "opportunity_closed"
    if event.startswith("assembly."):
        part = event.split(".")[1]
        if part == "window_omitted":
            return "omit:window"
        if part.endswith("_blocked"):
            return "assembly_blocked:"+part[:-8]
        return "assemble:"+part
    if event.startswith("bank.write_bit"):
        return "bank_write:"+event[-1]
    if event.startswith("factual.read"):
        suffix = ":blocked" if event.endswith("_blocked") else ""
        return "reader_decode:"+event[len("factual.read")]+suffix
    if event.startswith("reason.infer"):
        return "reason_infer:"+event[len("reason.infer")]+(":blocked" if event.endswith("_blocked") else "")
    if event.startswith("reason.path"):
        return "reason_path:"+event[len("reason.path")]+(":blocked" if event.endswith("_blocked") else "")
    if event.startswith("intervention."):
        kind, point = event.split(".",1)[1].split("@")
        return {"scope":"scope_cut", "permission":"permission_cut", "n_access":"n_cut"}[kind]+":"+point
    if event.startswith(("probe0.", "probe1.", "selected.")):
        prefix, name = event.split(".")
        mapped = {"sense_recipient":"sense", "guard_blocked":"blocked", "source_blocked":"blocked",
                  "window_blocked":"blocked", "continuation_blocked":"interrupted"}.get(name,name)
        return prefix+":"+mapped
    raise AssertionError(("unrecognized new emitted event", event))


def eq(actual, expected, context):
    assert actual == expected, (context, actual, expected)


def actual_old_accounts(s):
    mapping = {"record":"old_archive", "reason":"old_reasons", "action":"old_action",
               "revision":"old_revision", "evaluation":"old_evaluation"}
    out = {}
    for k,v in s["old_accounts"].items():
        if k == "evaluation.training_reserve":
            nk = "old_native.training_reserve"
        elif k == "retired.donor_fuel":
            nk = "retired_donor_fuel"
        elif k == "retired.donor_source":
            nk = "retired_donor_source"
        else:
            prefix, tail = k.split(".",1)
            nk = mapping[prefix]+"."+tail
        assert nk not in out
        out[nk] = v
    return out


def physical_retained(s):
    return (sum(s["core"][k] for k in ("fuel","source","recipient","escrow"))
            + sum(s["old_accounts"].values()) + sum(s["native"]["packets"])
            + sum(s["reserves"].values()) + sum(s["idle_common"].values())
            + s["source_reserve"] + s["idle_source"]
            + s["bank"]["budget"] + s["bank"]["escrow"] + s["reader"]["fuel"])


def check_common_snapshot(s, cfg, donor, context):
    assert s["owner"] in {"donor","child"}
    assert set(s["parts"]) == set(COMPONENTS)
    assert all(x in {"held","built","omitted"} for x in s["parts"].values())
    eq(60+2*len(s["parts"]),78,(context,"material"))
    eq(s["core"]["q"] & 1,donor["state"]["core"]["q"] & 1,(context,"historical actor bit"))
    assert s["core"]["recipient"] >= donor["state"]["core"]["recipient"]
    for x in (s["core"][k] for k in ("fuel","source","recipient","escrow")):
        assert x >= 0
    initial = donor["metrics"]["retained"]+96
    eq(physical_retained(s)+sum(s["new_spent"].values())+s["new_waste"],initial,(context,"whole continuation ledger"))
    eq(476-donor["metrics"]["retained"]+18+initial,590,(context,"original endowment"))
    eq(s["bank"]["identity"],cfg["child_binding"]["bank_id"],(context,"physical bank identity"))
    eq(list(old_checker().core_paths(s)),[("core",)],(context,"sole serialized live core"))


def check_projected_snapshot(s, e, cfg, donor, catalog, context):
    h, b, r = e["handoff"],e["bank"],e["reader"]
    check_common_snapshot(s,cfg,donor,context)
    c = h["child"] if h["child"] is not None else h["donor_core"]
    for k,v in c.items():
        eq(s["core"][k],v,(context,"actual core",k))
    if h["child"] is not None:
        recipe = dict(stage=2,life=1,gate_life=1,coupling=0,coupling_life=1,written=True,
                      installed=True,recoded=True,failed_q=-1,qualified_q=-1,witness=False)
        for k,v in recipe.items():
            eq(s["core"][k],v,(context,"declared new child body",k))
    meta = h["child_meta"] if h["child_meta"] is not None else h["donor_meta"]
    eq(s["physical"],dict(core_phase=meta["phase"],core_target=meta["target"],
       core_action=meta["action"],acquired_record=meta["acquired"]),(context,"actual recipient phase"))
    eq(actual_old_accounts(s),h["old_accounts"],(context,"every inherited account custody"))
    for k in ("reserves","idle_common","source_reserve","idle_source","released","copy_latch","n_access"):
        eq(s[k],h[k],(context,k))
    eq(s["assembly_cursor"],h["initial_cursor"],(context,"assembly cursor"))
    eq(s["probe_cursor"],e["outcomes"]["probe_attempts"],(context,"attempt controller"))
    eq(s["admitted"],h["admitted"],(context,"actual admission"))
    eq(s["parts"],{k:"built" if k in h["built"] else "omitted" if k in h["omitted"] else "held" for k in COMPONENTS},(context,"no part reuse"))
    states = {"donor_live":("donor","live","absent"), "donor_quiesced":("donor","quiesced","absent"),
              "child_committed":("child","retired","committed"), "child_commissioned":("child","retired","commissioned")}
    eq((s["owner"],s["donor_status"],s["child_status"]),states[h["lifecycle"]],(context,"distinct lifecycle"))
    eq(s["binding"],h["gates"] if h["gates"] is not None else donor["state"]["binding"],(context,"explicit inherited grants"))
    n = donor["state"]["native"]
    eq(s["native"],dict(n=n["n"],count=n["count"],mode=n["mode"],bit=n["bit"],packets=n["packets"],
       cells=donor["state"]["inventory"]["memory_cells"],support=donor["state"]["inventory"]["adapter"]),(context,"unchanged donor support"))
    if h["retired_donor"] is None:
        eq(s["retired"],None,(context,"no prematurely retired donor"))
    else:
        eq(s["retired"],dict(hardware={k:v for k,v in donor["state"]["core"].items() if k not in {"fuel","source","recipient","escrow"}},
            physical=donor["state"]["physical"],identity=cfg["child_binding"]["donor_id"]),(context,"retired hardware retained"))
    expected_bank = dict(identity=cfg["child_binding"]["bank_id"],owner="child" if h["reader_bound"] else None,
        epoch=True,next=e["query"],current=e["current_query"],live=h["reader_bound"],locked=e["locked"],
        bound=None if b["header"] is None else [1,b["header"]["action"]],latched=b["pending"],cells=b["cells"],
        written=b["writes"],complete=b["record"] is not None,pending=b["phase"] != "idle",budget=b["budget"],escrow=b["escrow"])
    eq(s["bank"],expected_bank,(context,"actual newly acquired bank"))
    if h["reader_bound"]:
        expected_reader = dict(fuel=r["fuel"],owner="child",bank=h["bank_id"],bound=True,
            reason_parts=old_checker().wview(actual_parent(donor,catalog))["reason_parts"],
            cache=r["cache"],cache_context=r["cache_context"],cache_valid=r["cache_valid"],read_count=r["read_count"],
            active=r["active"],phase=r["phase"],normalized=r["normalized"],orientation=r["orientation"],conflict=r["conflict"],
            facts=r["facts"],working=r["working"],inference_index=r["inference_index"],path_index=r["path_index"],
            publication=dict(context=True,mask=r["working"]) if r["current"] else None,publication_current=r["current"])
    else:
        f=actual_parent(donor,catalog);p,w=old_checker().pview(f),old_checker().wview(f)
        expected_reader={k:deepcopy(p[k]) for k in ("cache","cache_context","cache_valid","read_count")}
        expected_reader.update({k:deepcopy(w[k]) for k in ("active","phase","normalized","orientation","conflict","facts","working","inference_index","path_index","publication","publication_current")})
        expected_reader.update(fuel=0,owner="donor",bank=None,bound=False,reason_parts=w["reason_parts"])
    eq(s["reader"],expected_reader,(context,"one reused paid reader"))
    eq(sum(s["new_spent"].values()),h["spent"],(context,"paid service total"))
    eq(s["new_waste"],h["waste"],(context,"actual source loss"))
    pm=e["port"]["mode"]
    expected_mode = ("unbuilt" if "port" not in h["built"] else {"help":"assessed_help","abstain":"assessed_abstain"}.get(pm,pm))
    eq(s["port"]["mode"],expected_mode,(context,"single-use evaluation state"))
    eq(s["port"]["owner"],cfg["child_binding"]["child_id"] if h["child"] is not None else None,(context,"new port owner"))
    eq(s["port"]["bank"],h["bank_id"] if h["reader_bound"] else None,(context,"port bound bank"))
    command = old_checker().route(r)
    eq(s["port"]["read_command"],command if pm in {"read","help","abstain","executing"} else None,(context,"paid finite command latch"))


def check_actual_row(cfg, arm, donor, row, accepted_catalog, context):
    expected=expected_schedule(cfg,arm,donor,accepted_catalog)
    eq(row["probability"],donor["probability"],(context,"original mass"))
    expected_trace=[e for e in expected["trace"] if e["event"] != "selected:initiate"]
    actual_trace=[]
    for i,item in enumerate(row["runtime_trace"]):
        check_common_snapshot(item["state"],cfg,donor,(context,i,item["event"]))
        name=canonical_event(item["event"],item["state"])
        if name == "selected:initiate":
            # An inspectable internal phase marker, not an RI event. It cannot
            # create stock, facts, or authorise work without original RI guards.
            assert i>0
            before=deepcopy(row["runtime_trace"][i-1]["state"])
            after=deepcopy(item["state"])
            after["port"]["mode"]=before["port"]["mode"]
            after["outcomes"]["selected_attempted"]=before["outcomes"]["selected_attempted"]
            eq(after,before,(context,i,"zero-cost initiation marker"))
            continue
        actual_trace.append((i,name,item["state"]))
    eq(len(actual_trace),len(expected_trace),(context,"complete meaningful event word"))
    for (i,name,s),e in zip(actual_trace,expected_trace):
        eq(name,e["event"],(context,i,"independent event"))
        check_projected_snapshot(s,e,cfg,donor,accepted_catalog,(context,i,name))
    eq(row["state"],row["runtime_trace"][-1]["state"],(context,"endpoint is last actual state"))
    return len(row["runtime_trace"])


def independent_metrics(expected, donor):
    e=expected["trace"][-1];h=e["handoff"];c=h["child"] or h["donor_core"];r=e["reader"];o=e["outcomes"]
    bills=dict.fromkeys(("assembly","copy_read","copy_write","probe_services","archive","factual_reading",
                       "reasoning","evaluation_read","evaluation_write","selected_services"),0)
    previous=0
    for item in expected["trace"]:
        amount=item["handoff"]["spent"]-previous;previous=item["handoff"]["spent"]
        if not amount:continue
        event=item["event"]
        if event.startswith("assemble:") or event=="access":key="assembly"
        elif event.startswith("probe"):key="probe_services"
        elif event.startswith("bank_"):key="archive"
        elif event.startswith("reader_"):key="factual_reading"
        elif event.startswith("reason_"):key="reasoning"
        elif event.startswith("selected:"):key="selected_services"
        else:key=event
        assert key in bills,(event,key)
        bills[key]+=amount
    native=donor["state"]["native"]
    out=dict(admitted=int(h["admitted"]),donor_retired=int(h["retired_donor"] is not None),
        born=int(h["child"] is not None),commissioned=int(h["reader_bound"]),n=native["n"],n_access=int(h["n_access"]),
        probes_completed=o["probe_completed"],probe_captures=o["probe_captures"],probe_recipient_gain=10*o["probe_captures"],
        fresh_frame=int(e["bank"]["record"] is not None),factual_complete=int(r["cache_valid"] and r["read_count"]==3 and h["reader_bound"]),
        child_publication=int(h["reader_bound"] and r["current"]),supported_child_command=int(old_checker().route(r) is not None),
        positive_assessment=int(o["assessment"] is True),selected_attempted=int(o["selected_attempted"]),
        selected_completed=int(o["selected_completed"]),selected_capture=int(o["selected_capture"]),selected_recipient_gain=10*int(o["selected_capture"]),
        recipient=c["recipient"],recipient_gain=c["recipient"]-donor["state"]["core"]["recipient"],actor=c["fuel"],source=c["source"],
        native_source=sum(native["packets"]),retired_owned=sum(h["old_accounts"].values()),retained=handoff_energy(h),
        new_spent=h["spent"],new_waste=h["waste"],core_ready=int((h["child_meta"] or h["donor_meta"])["phase"]=="ready"),
        pending_escrow=c["escrow"],pending_copy=int(h["copy_latch"] is not None),pending_read=int(e["port"]["mode"]=="read"),
        changed_candidate=int(h["child"] is not None and old_checker().candidate(c)!=old_checker().candidate(donor["state"]["core"])),
        installed_parts=len(h["built"]))
    out.update({"spent_"+k:v for k,v in bills.items()})
    return out


def check_catalogs(data, accepted, specs):
    entries={};ancestry={}
    for case in sorted({x["config"]["parent_case"] for x in specs["cases"]}):
        for producer in specs["producers"]:
            for i,row in enumerate(accepted["cases"][case]["arms"]["shared"]["producers"][producer]["paths"]):
                s=row["state"];oldref=s["parent_ref"];ref=f"{case}/shared/{producer}/{i}"
                entries[ref]=dict(parent_case=case,parent_arm="shared",producer=producer,path_index=i,
                    probability=row["probability"],donor_state=s,donor_state_sha256=object_sha(s),
                    donor_trace_sha256=object_sha(row["runtime_trace"]),original_parent_ref=oldref,observer=row["observer"])
                ancestry[oldref]=accepted["parent_catalog"][oldref]
    eq(data["parent_catalog"],entries,"all exact accepted donor states/traces/weights")
    eq(data["ancestry_catalog"],ancestry,"lossless older archive ancestry")
    return len(entries),len(ancestry)


def check_preparation(actual, accepted):
    a=h=r=i=l=bound=spent=0;f=360;source=230
    trace=[dict(event="initial",plant=[a,h,r,i,l,f,source],spent=spent)]
    def formed(event):
        nonlocal a,h,r,i,l,f,source,spent
        before=f+source+l;capacity=78-a-h-int(r!=0)-bound
        if event in {"form_a","form_h"}:
            assert not i and capacity>0 and f>=1
            if event=="form_a":a+=1
            else:h+=1
            f-=1
        elif event=="bind_a":
            assert r==0 and a>=1 and f>=1;a-=1;r=1;f-=1
        elif event=="repair":
            assert r==1 and not i and h>=2 and f>=1;i=1;f-=1
        elif event=="capture":
            assert i and not l and source>=1;source-=1;l=1
        elif event=="copy_a":
            assert r==1 and l and capacity>0;a+=1;l=0
        else:raise AssertionError(("unsupported accepted formation event",event))
        spent+=before-f-source-l
        assert f+source+l+spent==590 and a+h+int(r!=0)+bound<=78
        trace.append(dict(event=event,plant=[a,h,r,i,l,f,source],spent=spent))
    for event in ["form_a"]*9+["form_h"]*9:formed(event)
    for row in accepted["trace"][1:]:
        event=row["event"]
        if "plant" in row and event in {"form_a","form_h","bind_a","bind_h","copy_a","copy_h","repair","capture"}:
            formed(event)
            eq([a,h,r,i,l,f,source],[v+d for v,d in zip(row["plant"],(9,9,0,0,0,66,30))],"every accepted formation projection")
        elif event in {"assemble_evaluation_component","old_assembly"}:
            assert a>=1 and h>=1 and f>=1;a-=1;h-=1;f-=1;bound+=2;spent+=1
            eq([a,h,r,i,l,f,source],[v+d for v,d in zip(row["plant"],(9,9,0,0,0,66,30))],"every accepted assembly projection")
            trace.append(dict(event=event,plant=[a,h,r,i,l,f,source],spent=spent))
        elif event=="exact_M42_projection":
            assert r==1 and h>=1 and f>=1;h-=1;r=0;f=f-1+l;l=0;spent+=1;bound+=2
            eq((a-9,h-9,f-66,source-30),(row["free_a"],row["free_h"],row["fuel"],row["source"]),"exact actual M60 handoff")
            trace.append(dict(event="exact_M60_projection",plant=[a,h,r,i,l,f,source],spent=spent,
                held_a=9,held_h=9,protected_common=66,protected_source=30,parent_free_a=a-9,parent_free_h=h-9,
                parent_fuel=f-66,parent_source=source-30))
        assert f+source+l+spent==590 and a+h+int(r!=0)+bound<=78
    eq(actual["trace"],trace,"complete independent M78 preparation")
    eq(actual["accepted_preparation_sha256"],object_sha(accepted),"actual accepted preparation dependency")
    eq((actual["initial_material"],actual["initial_common"],actual["initial_source"],actual["additional_formation_spent"]),(78,360,230,18),"original procurement")
    return len(trace)


def comparison_checks(data, specs):
    matched=equal_inputs=0
    for case in specs["cases"]:
        arms=data["cases"][case["name"]]["arms"]
        for producer in specs["producers"]:
            shared=arms["shared"]["producers"][producer]["paths"]
            conventional=arms["conventional"]["producers"][producer]["paths"]
            gated=arms["identity_gated"]["producers"][producer]["paths"]
            for a,b,c in zip(shared,conventional,gated):
                eq(a,b,(case["name"],producer,"conventional exact full history"));matched+=1
                def before_choice(row):
                    return [x for x in row["runtime_trace"][:next((j for j,x in enumerate(row["runtime_trace"]) if x["event"]=="evaluation.write"),len(row["runtime_trace"]))]]
                eq(before_choice(a),before_choice(c),(case["name"],producer,"equal acquired information/private history before routing"));equal_inputs+=1
    return dict(conventional_exact_histories=matched,equal_input_histories=equal_inputs)


def mutation_checks(data, accepted, specs):
    cfg=next(x["config"] for x in specs["cases"] if x["name"]=="changed")
    donor=accepted["cases"][cfg["parent_case"]]["arms"]["shared"]["producers"]["variable"]["paths"][11]
    original=data["cases"]["changed"]["arms"]["shared"]["producers"]["variable"]["paths"][11]
    results=[]
    def reject(label, mutate):
        row=deepcopy(original);mutate(row)
        row["state"]=deepcopy(row["runtime_trace"][-1]["state"])
        try:check_actual_row(cfg,"shared",donor,row,accepted["parent_catalog"],("mutation",label))
        except AssertionError as ex:results.append(dict(name=label,rejected=True,reason=str(ex)[:1200]));return
        raise AssertionError(("mutant accepted",label))
    def at(row,event):return next(x["state"] for x in row["runtime_trace"] if x["event"]==event)
    reject("free_copy_read",lambda row:at(row,"handoff.read")["reserves"].__setitem__("copy",2))
    reject("copied_false_native_n",lambda row:at(row,"handoff.write_unknown")["native"].__setitem__("n",0))
    reject("hidden_qualification_restoration",lambda row:at(row,"handoff.write_unknown")["core"].__setitem__("last",1))
    reject("native_source_as_actor_fuel",lambda row:(at(row,"accounts.release_child")["native"]["packets"].__setitem__(0,0),at(row,"accounts.release_child")["core"].__setitem__("fuel",28)))
    reject("double_child_release",lambda row:at(row,"accounts.release_child")["core"].__setitem__("source",60))
    reject("retired_donor_reactivated",lambda row:at(row,"access.assemble_bind").__setitem__("donor_status","live"))
    reject("doubled_patient_in_retired_hardware",lambda row:at(row,"handoff.write_unknown")["retired"]["hardware"].__setitem__("recipient",60))
    reject("wrong_recipient_target",lambda row:at(row,"selected.sense_recipient")["physical"].__setitem__("core_target","actor"))
    reject("actor_bit_overwritten",lambda row:at(row,"probe0.write")["core"].__setitem__("q",at(row,"probe0.write")["core"]["q"]^1))
    reject("unearned_positive_feedback",lambda row:at(row,"probe0.acquire")["physical"].__setitem__("acquired_record",True))
    reject("free_record_write",lambda row:at(row,"bank.write_bit0")["bank"].__setitem__("escrow",4))
    reject("reused_selected_authorization",lambda row:row["runtime_trace"][-1]["state"]["port"].update(mode="assessed_help",opportunity="due"))
    def stale_identity(row):
        for x in row["runtime_trace"]:
            s=x["state"]
            if s["reader"]["bound"]:
                s["bank"]["identity"]="old_physical_bank"
                s["reader"]["bank"]="old_physical_bank"
                s["port"]["bank"]="old_physical_bank"
    reject("old_bank_consistently_rebound_as_fresh",stale_identity)
    def stale_pipeline(row):
        for x in row["runtime_trace"]:
            s=x["state"];b=s["bank"];r=s["reader"]
            if b["bound"] is not None:b["bound"][1]^=1
            if b["latched"] is not None:b["latched"][1]^=1
            if b["written"]>=2:b["cells"][1]^=1
            if r["owner"]=="child" and r["cache"][1] is not None:r["cache"][1]=not r["cache"][1]
            if r["owner"]=="child" and r["normalized"][1] is not None:r["normalized"][1]^=1
            if r["owner"]=="child" and r["orientation"] is not None:
                r["orientation"]^=1;r["facts"]=[r["orientation"]==0,r["orientation"]==1,None]
                r["working"]=[True,r["orientation"]==0 and r["path_index"]>=1,r["orientation"]==1 and r["path_index"]>=2]
                if r["publication"] is not None:r["publication"]["mask"]=r["working"][:]
    reject("stale_frame_with_consistently_rewritten_decode_and_publication",stale_pipeline)
    return results


def main():
    started=datetime.now(timezone.utc).isoformat();specs=read_json(HERE/"cases.json")
    data=read_json(HERE/"results.json.gz");accepted=read_json(PARENT/"results.json.gz")
    fixtures=read_json(HERE/"fixtures.json");old_fixtures=read_json(PARENT/"fixtures.json")
    root=next(p for p in HERE.parents if (p/"AGENTS.md").exists())
    for name,h in data["source_sha256"].items():eq(sha(root/name),h,("numerical dependency",name))
    catalog_count,ancestry_count=check_catalogs(data,accepted,specs)
    prep_count=sum(check_preparation(prep,old_fixtures["preparations"][case]) for case,prep in fixtures["preparations"].items())
    counts=dict(cases=len(specs["cases"]),mixtures=0,histories=0,snapshots=0,aggregate_values=0,
                parent_catalog=catalog_count,ancestry_catalog=ancestry_count,formation_prefixes=prep_count)
    for case in specs["cases"]:
        cfg=case["config"];eq(data["cases"][case["name"]]["config"],cfg,"frozen complete configuration")
        for arm in specs["arms"]:
            for producer in specs["producers"]:
                parents=accepted["cases"][cfg["parent_case"]]["arms"]["shared"]["producers"][producer]["paths"]
                group=data["cases"][case["name"]]["arms"][arm]["producers"][producer];rows=group["paths"]
                eq(len(rows),len(parents),"all ancestors retained");totals={};mass=Fraction(0)
                for i,(donor,row) in enumerate(zip(parents,rows)):
                    context=(case["name"],arm,producer,i)
                    eq(row["predecessor_ref"],f"{cfg['parent_case']}/shared/{producer}/{i}",(context,"exact donor identity"))
                    counts["snapshots"]+=check_actual_row(cfg,arm,donor,row,accepted["parent_catalog"],context)
                    expected=expected_schedule(cfg,arm,donor,accepted["parent_catalog"])
                    metrics=independent_metrics(expected,donor);eq(row["metrics"],metrics,(context,"independent metrics"))
                    eq(row["observer"],dict(donor_recipient_law=donor["observer"]["actual_work_law"],
                        probe_law=expected["observer_probe_law"],final_law=expected["observer_final_law"]),(context,"physical law only observer"))
                    weight=Fraction(row["probability"]);mass+=weight
                    for k,v in metrics.items():totals[k]=totals.get(k,Fraction(0))+weight*v
                    counts["histories"]+=1
                eq(mass,Fraction(1),(case["name"],arm,producer,"no survivor normalization"))
                eq(group["metrics"],{k:str(v) for k,v in totals.items()},(case["name"],arm,producer,"all weighted totals"))
                counts["mixtures"]+=1;counts["aggregate_values"]+=len(totals)
    comparisons=comparison_checks(data,specs);mutations=mutation_checks(data,accepted,specs)
    result=dict(status="passed",started_at=started,finished_at=datetime.now(timezone.utc).isoformat(),counts=counts,
                comparisons=comparisons,mutations=mutations,mutation_count=len(mutations),
                source_sha256={str((HERE/f).relative_to(root)):sha(HERE/f) for f in ("check_model.py","model.py","results.json.gz","fixtures.json","reporting.json","protocol-freeze.json","cases.json","INTERFACE.md","DRAFT-PROTOCOL.md")},
                scope="Independent full inherited-history/protocol/resource/data/choice reconstruction. No new producer transition imports. Separate source/API tests and Lean theorem audit have their own scopes.")
    (HERE/"model-verification.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in {"mutations","source_sha256"}},indent=2))


if __name__ == "__main__":
    main()
