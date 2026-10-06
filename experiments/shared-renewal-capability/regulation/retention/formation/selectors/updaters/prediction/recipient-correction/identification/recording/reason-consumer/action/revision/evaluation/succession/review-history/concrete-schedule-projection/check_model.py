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
        return finish()
    if h["child"]["fuel"] < 1:
        emit("evaluation_write_blocked")
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
