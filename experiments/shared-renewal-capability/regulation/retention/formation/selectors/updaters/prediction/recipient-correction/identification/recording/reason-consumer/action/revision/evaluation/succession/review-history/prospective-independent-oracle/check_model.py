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
