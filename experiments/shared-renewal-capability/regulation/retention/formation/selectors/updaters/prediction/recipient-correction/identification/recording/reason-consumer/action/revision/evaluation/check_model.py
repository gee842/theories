#!/usr/bin/env python3
"""Independent evaluative-uptake oracle, prospective draft.

Written from DRAFT-PROTOCOL.md and cases.json before inspecting any new
evaluation implementation or outcome.  This initial layer supplies native
state transitions, local payment rules and a separate decision table.  The
concrete snapshot adapter and end-to-end checker will be added after the
protocol/schema freeze, with draft bytes and revisions preserved.

No new producer transitions are imported.  An eventual old-law adapter may
reuse the independently authored and accepted parent checker only.
"""

from copy import deepcopy
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
import importlib.util
import hashlib
import json
import gzip

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
_OLD = None


def old_checker():
    global _OLD
    if _OLD is None:
        spec = importlib.util.spec_from_file_location("accepted_revision_independent_checker", PARENT/"check_model.py")
        _OLD = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_OLD)
    return _OLD


def object_sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def read_json(path):
    path = Path(path)
    with gzip.open(path,"rt") if path.suffix == ".gz" else path.open() as stream:
        return json.load(stream)


@dataclass(frozen=True)
class Native:
    """Projection onto the pair-backed native module and the single core."""
    fuel: int
    reserve: int
    sources: tuple[int, int, int] = (2, 2, 2)
    numerator: int = 0
    completed: int = 0
    mode: str = "ready"
    bit: int = 0
    spent: int = 0


def native_energy(s):
    return s.fuel + s.reserve + sum(s.sources)


def native_check(s):
    assert min(s.fuel, s.reserve, *s.sources, s.spent) >= 0
    assert 0 <= s.numerator <= 7 and 0 <= s.completed <= 3
    assert s.bit in (0, 1)
    assert s.mode in {"ready", "paid", "returned", "read_known", "read_missing", "closed"}
    assert (s.mode == "closed") == (s.completed == 3)


def native_pay(s):
    """Allocate at most four protected units and pay the next operation.

    This projected macro contains the two resource events if the concrete
    producer emits them separately. Existing core fuel remains spendable;
    twelve protected units are not asserted to be a necessary entry threshold.
    """
    native_check(s)
    assert s.mode == "ready" and s.completed < 3
    allocation = min(4, s.reserve)
    assert s.fuel + allocation >= 2
    t = replace(s, fuel=s.fuel + allocation - 2,
                reserve=s.reserve-allocation, mode="paid", spent=s.spent+2)
    assert native_energy(t)+2 == native_energy(s)
    return t


def native_return(s, actual_return):
    """Only the plant event receives an actual return, not a desired weight."""
    native_check(s)
    assert s.mode == "paid" and actual_return in (0, 2)
    assert s.sources[s.completed] >= actual_return
    stocks = list(s.sources)
    stocks[s.completed] -= actual_return
    t = replace(s, fuel=s.fuel+actual_return, sources=tuple(stocks),
                bit=actual_return//2, mode="returned")
    assert native_energy(t) == native_energy(s)
    return t


def native_read(s, channel="faithful"):
    native_check(s)
    assert s.mode == "returned" and s.fuel >= 1
    assert channel in {"faithful", "missing", "inverted"}
    # The physical bit encodes actual return presence until this paid read.
    observed = 1-s.bit
    if channel == "inverted":
        observed = 1-observed
    t = replace(s, fuel=s.fuel-1, spent=s.spent+1,
                bit=0 if channel == "missing" else observed,
                mode="read_missing" if channel == "missing" else "read_known")
    assert native_energy(t)+1 == native_energy(s)
    return t


def native_write(s, learning="acquire"):
    native_check(s)
    assert s.mode in {"read_known", "read_missing"} and s.fuel >= 1
    assert learning in {"acquire", "update_disabled"}
    n = s.numerator
    if learning == "update_disabled":
        n = 0
    elif s.mode == "read_known":
        n = n//2+4*s.bit
    count = s.completed+1
    t = replace(s, fuel=s.fuel-1, spent=s.spent+1, numerator=n,
                completed=count, bit=0, mode="closed" if count == 3 else "ready")
    native_check(t)
    assert native_energy(t)+1 == native_energy(s)
    return t


def exact_three_bit_estimate(bits):
    """Closed-form oracle for three honest acquired bits from zero."""
    assert len(bits) == 3 and all(b in (0, 1) for b in bits)
    return bits[0]+2*bits[1]+4*bits[2]


def decision(n, *, arm, transfer="positive", valuation="learned", surcharge=0, suppressed=False):
    """Choice oracle contains no physical truth or private-return parameter."""
    assert 0 <= n <= 7 and surcharge >= 0
    assert arm in {"shared", "identity_gated", "conventional"}
    assert transfer in {"positive", "absent", "inverted"}
    assert valuation in {"learned", "fixed7"}
    if arm == "identity_gated" or transfer != "positive" or suppressed:
        return False
    value = 7 if valuation == "fixed7" else n
    if arm == "conventional":
        # Explicit independent table for the frozen tariffs 8 and 9.
        if surcharge == 0:
            return (False, False, False, False, False, False, False, True)[value]
        if surcharge == 1:
            return False
    return Fraction(5*value, 4) > 8+surcharge


def read_enabled(*, port_mode, native_count, core_phase, fuel):
    return port_mode == "idle" and native_count == 3 and core_phase == "ready" and fuel >= 1


def assessment_enabled(*, port_mode, native_count, current, same_destination,
                       scope, candidate, supported, fuel):
    # Factual eligibility and evaluation survive permission/delivery loss.
    # Those interventions block action, rather than refute the reason.
    return (port_mode == "read" and native_count == 3 and current and same_destination
            and scope and candidate == supported and supported in (0, 1)
            and fuel >= 1)


def use_start_enabled(*, port_mode, current, same_destination, scope,
                      permission, delivery, core_phase, source, candidate, supported):
    # Original RI rent/miss separately checks active state and available fuel.
    return (port_mode == "assessed_help" and current and same_destination
            and scope and permission and delivery and core_phase == "ready" and source >= 10
            and candidate == supported and supported in (0, 1))


def replacement_enabled(*, native_count, first_closed, old_port_present, old_port_mode,
                        core_phase, spare_accessible, spare_used, reserve):
    return (native_count == 3 and first_closed and core_phase == "ready"
            and (not old_port_present or old_port_mode == "consumed")
            and spare_accessible and not spare_used and reserve >= 1)


def strict_design_account():
    """Prospective identity only; not an executed witness or a validation run."""
    return dict(initial=476, parent_prefix=351, new_construction=26,
                native_service=12, first_service=10, later_service=11,
                recipient=60, isolated_native_source=6)


def inherited_prefix(row):
    trace = row["runtime_trace"]
    for i,item in enumerate(trace):
        if item["event"] in ("paid_command_read","command_read_unavailable"):
            assert i > 0
            return i-1,deepcopy(trace[i-1]["state"])
    eligible = [(i,item["state"]) for i,item in enumerate(trace)
                if item["event"] != "continuation_complete"]
    assert eligible
    i,state = eligible[-1]
    return i,deepcopy(state)


def current_publication(parent):
    old = old_checker()
    p,w = old.pview(parent),old.wview(parent)
    pub = w["publication"]
    return bool(parent["opened"] and parent["selected_bank"] == "fresh"
                and p["cache_valid"] and p["read_count"] == 3 and p["cache_context"] is True
                and w["phase"] == "published" and w["publication_current"]
                and pub and pub["context"] is True and pub["mask"][0])


def expected_schedule(cfg, arm, oldrow):
    """Independent prescribed history; authored before reading new producer.

    This oracle stores a full inherited parent for meaning-preserving state
    replacement. Concrete serialized catalogs may factor immutable backing
    out, but must reconstruct this same parent with one live core.
    """
    old = old_checker()
    index,parent = inherited_prefix(oldrow)
    p,a = old.pview(parent),parent["parent"]
    native = Native(p["core"]["fuel"],cfg["training_reserve"],tuple(cfg["native_packets"]))
    spent = {key:0 for key in ("native_operation","native_read","native_write","evaluation_read",
                              "evaluation_write","replacement","suppression","surcharge","recipient_services")}
    built = cfg["initial_port"]
    port_mode = "idle"  # ignored when no port exists; no extra absent-state bit
    generation = 0
    opportunity_phase = "first_due"
    first_closed = False
    spare_used = False
    later_fuel,later_source = cfg["later_reserve"],cfg["later_packet"]
    suppressed = False
    waste = 0
    trace = []
    outcomes = []
    meta = dict(phase=p["core_phase"],target=p["core_target"],action=p["core_action"],
                acquired=p["acquired_record"],receipt=None)
    use_law = oldrow["observer"]["final_law"] ^ bool(cfg["late_law_flip"])

    def emit(event):
        trace.append(dict(event=event,core=deepcopy(p["core"]),meta=deepcopy(meta),
                          native=dict(n=native.numerator,count=native.completed,mode=native.mode,
                                      bit=native.bit,packets=list(native.sources),training_reserve=native.reserve),
                          scope=a["scope"],permission=a["permission"],delivery=a["delivery"],
                          port_mode=port_mode,port_built=built,generation=generation,
                          opportunity_phase=opportunity_phase,
                          first_closed=first_closed,spare_used=spare_used,later_fuel=later_fuel,
                          later_source=later_source,suppressed=suppressed,spent=dict(spent),waste=waste))

    def store_core(c,m):
        p["core"] = c
        p.update(core_phase=m["phase"],core_target=m["target"],core_action=m["action"],acquired_record=m["acquired"])

    def intervene(at):
        nonlocal port_mode
        for cut in cfg["interventions"]:
            if cut["at"] != at:
                continue
            if cut["kind"] == "scope_loss":
                a["scope"] = False
                if port_mode in ("read","assessed_help","assessed_abstain"):
                    port_mode = "consumed"
            elif cut["kind"] == "permission_loss":
                a["permission"] = False
            elif cut["kind"] == "delivery_loss":
                a["delivery"] = False
            else:
                raise AssertionError(cut)
            emit("intervention:"+cut["kind"]+":"+at)

    def eligible():
        supported = old.snapshot_command(parent,"reason")
        return (current_publication(parent) and a["scope"] and supported is not None
                and old.candidate(p["core"]) == supported)

    def opportunity(which):
        nonlocal port_mode,native,meta,waste
        prefix = "first" if which == 0 else "second"
        result = dict(read=False,assessed=False,help=False,attempted=False,completed=False,captured=False)
        if not built or not read_enabled(port_mode=port_mode,native_count=native.completed,
                                         core_phase=meta["phase"],fuel=p["core"]["fuel"]):
            emit(prefix+":read_blocked")
            outcomes.append(result)
            return
        p["core"]["fuel"] -= 1
        spent["evaluation_read"] += 1
        port_mode = "read" if eligible() else "consumed"
        result["read"] = True
        emit(prefix+":read")
        if which == 0:
            intervene("after_first_evaluation_read")
        if port_mode != "read" or not eligible() or p["core"]["fuel"] < 1:
            emit(prefix+":assessment_blocked")
            outcomes.append(result)
            return
        p["core"]["fuel"] -= 1
        spent["evaluation_write"] += 1
        help_now = decision(native.numerator,arm=arm,transfer=cfg["transfer"],valuation=cfg["valuation"],
                            surcharge=cfg["trial_surcharge"],suppressed=suppressed)
        port_mode = "assessed_help" if help_now else "assessed_abstain"
        result.update(assessed=True,help=help_now)
        emit(prefix+":assess")
        if not help_now:
            port_mode = "consumed"
            emit(prefix+":abstain")
            outcomes.append(result)
            return
        result["attempted"] = True
        if not (eligible() and a["permission"] and a["delivery"]):
            port_mode = "consumed"
            emit(prefix+":action_blocked")
            outcomes.append(result)
            return
        port_mode = "executing"
        emit(prefix+":initiate")
        if p["core"]["source"] < 10:
            port_mode = "consumed"
            emit(prefix+":source_blocked")
            outcomes.append(result)
            return
        fee = cfg["trial_surcharge"]
        if p["core"]["fuel"] < fee:
            port_mode = "consumed"
            emit(prefix+":surcharge_blocked")
            outcomes.append(result)
            return
        if fee:
            p["core"]["fuel"] -= fee
            spent["surcharge"] += fee
            emit(prefix+":surcharge")
        events = (["miss"] if not p["core"]["active"] or p["core"]["fuel"] < 8
                  else ["rent","sense","reserve","work","acquire","write"])
        for event in events:
            if event not in ("acquire","write") and not (eligible() and a["permission"] and a["delivery"]):
                emit(prefix+":interrupted")
                break
            c,m,bill,lost = old.ri_step(p["core"],meta,event,use_law,True,"faithful")
            meta = m
            store_core(c,m)
            spent["recipient_services"] += bill
            waste += lost
            if event == "work":
                result["captured"] = bool(m["receipt"])
            if event == "write":
                result["completed"] = True
            if event in ("write","miss"):
                port_mode = "consumed"
            emit(prefix+":ri_"+event)
            if which == 0 and event == "rent":
                intervene("after_first_rent")
            if which == 0 and event == "work":
                intervene("after_first_work")
        outcomes.append(result)

    emit("entry")
    admitted = (current_publication(parent) and meta["phase"] == "ready" and p["core"]["active"]
                and a["scope"] and cfg["memory_cells"] == 6 and cfg["adapter"])
    if admitted:
        for j in range(3):
            native = replace(native,fuel=p["core"]["fuel"])
            try:
                native = native_pay(native)
            except AssertionError:
                emit("native:pay_blocked")
                break
            p["core"]["fuel"] = native.fuel
            spent["native_operation"] += 2
            emit("native:pay")
            actual_return = 2*(1-cfg["native_signals"][j])
            if native.sources[j] < actual_return:
                emit("native:return_blocked")
                break
            native = native_return(native,actual_return)
            p["core"]["fuel"] = native.fuel
            emit("native:return")
            if native.fuel < 1:
                emit("native:read_blocked")
                break
            native = native_read(native,cfg["native_meter"][j])
            p["core"]["fuel"] = native.fuel
            spent["native_read"] += 1
            emit("native:read")
            if native.fuel < 1:
                emit("native:write_blocked")
                break
            native = native_write(native,cfg["learning"])
            p["core"]["fuel"] = native.fuel
            spent["native_write"] += 1
            emit("native:write")
        if native.completed == 3:
            fee = cfg["suppression_cost"]
            if fee is not None and p["core"]["fuel"] >= fee:
                p["core"]["fuel"] -= fee
                spent["suppression"] += fee
                suppressed = True
                emit("suppression")
            intervene("before_first_evaluation")
            opportunity(0)
            first_closed = True
            if port_mode == "idle":
                port_mode = "consumed"
            opportunity_phase = "first_closed"
            emit("first:closed")
            if replacement_enabled(native_count=native.completed,first_closed=first_closed,
                                   old_port_present=built,old_port_mode=port_mode,core_phase=meta["phase"],
                                   spare_accessible=cfg["spare_pair_accessible"],spare_used=spare_used,reserve=later_fuel):
                later_fuel -= 1
                spent["replacement"] += 1
                spare_used = True
                built,port_mode,generation = True,"idle",1
                opportunity_phase = "second_due"
                emit("replacement")
                p["core"]["fuel"] += later_fuel
                p["core"]["source"] += 10*(later_source//10)
                later_fuel,later_source = 0,later_source%10
                emit("later:release")
                opportunity(1)
                if port_mode == "idle":
                    port_mode = "consumed"
                opportunity_phase = "finished"
                emit("second:closed")
            else:
                emit("replacement:blocked")
    else:
        emit("admission:blocked")
    emit("complete")
    return dict(prefix_index=index,parent=parent,trace=trace,outcomes=outcomes,admitted=admitted)


def eq(actual,expected,label):
    assert actual == expected,(label,actual,expected)


def canonical_event(event,cfg):
    direct={"extension.at_actual_parent_prefix":"entry","native.admission_blocked":"admission:blocked",
            "continuation.complete":"complete","continuation.stopped":"complete",
            "suppression.paid":"suppression","suppression.blocked":"suppression:blocked",
            "replacement.assemble":"replacement","replacement.release_later_accounts":"later:release",
            "replacement.blocked":"replacement:blocked"}
    if event in direct:return direct[event]
    if event.startswith("intervention."):
        kind=event.split(".",1)[1]
        cuts=[x for x in cfg["interventions"] if x["kind"]==kind]
        assert len(cuts)==1
        return "intervention:"+kind+":"+cuts[0]["at"]
    family,kind=event.split(".",1)
    if family=="native":
        return "native:"+("read" if kind in ("read_known","read_missing") else kind)
    which="first" if family.endswith("1") else "second"
    if family.startswith("evaluation"):
        return which+":"+{"write":"assess","write_blocked":"assessment_blocked"}.get(kind,kind)
    if family.startswith("recipient"):
        if kind in ("rent","sense","reserve","work","acquire","write","miss"):
            return which+":ri_"+kind
        return which+":"+{"guard_blocked":"action_blocked","continuation_blocked":"interrupted"}.get(kind,kind)
    if family.startswith("opportunity"):return which+":"+kind
    raise AssertionError(("unknown emitted event",event))


def current_parent(s,catalog):
    out=deepcopy(catalog[s["parent_ref"]]["state"])
    p=old_checker().pview(out)
    p["core"]=deepcopy(s["core"])
    p.update(deepcopy(s["physical"]))
    out["parent"].update(deepcopy(s["binding"]))
    return out


def independent_retained(s,catalog):
    # Resolve every old account from the exact inherited prefix, rather than
    # trusting the producer's accounting offsets.
    return (old_checker().retained(current_parent(s,catalog))+
            s["native"]["training_reserve"]+sum(s["native"]["packets"])+sum(s["reserves"].values()))


def snapshot_projection(s):
    physical=s["physical"]
    return dict(core=s["core"],meta=dict(phase=physical["core_phase"],target=physical["core_target"],
               action=physical["core_action"],acquired=physical["acquired_record"]),native=s["native"],
               scope=s["binding"]["scope"],permission=s["binding"]["permission"],delivery=s["binding"]["delivery"],
               port_mode=s["port"]["mode"],port_built=s["port"]["built"],generation=s["port"]["generation"],
               opportunity_phase=s["port"]["opportunity_phase"],
               first_closed=s["port"]["opportunity_phase"] in ("first_closed","second_due","finished"),
               spare_used=s["inventory"]["held_a"]==0,later_fuel=s["reserves"]["later_fuel"],
               later_source=s["reserves"]["later_source"],suppressed=s["port"]["suppressed"],
               spent=s["new_spent"],waste=s["new_waste"])


def check_catalog(catalog,old_data,specs):
    expected={}
    for case in {c["config"]["parent_revision_case"] for c in specs["cases"]}:
        for producer in specs["parent_producers"]:
            rows=old_data["cases"][case]["producers"][producer]["paths"]
            for i,row in enumerate(rows):
                j,state=inherited_prefix(row)
                ref=f"{case}/{producer}/{i}/{j}"
                expected[ref]=dict(parent_case=case,producer=producer,path_index=i,prefix_index=j,
                    probability=row["probability"],prefix_event=row["runtime_trace"][j]["event"],
                    state_sha256=object_sha(state),state=state,observer=row["observer"],parent_predecessor=row["predecessor"])
    eq(catalog,expected,"complete actual parent catalog/ancestry")


def check_snapshot(s,e,cfg,catalog,base,context):
    old=old_checker()
    projected=snapshot_projection(s)
    wanted={k:v for k,v in e.items() if k!="event"}
    wanted["meta"]={k:v for k,v in wanted["meta"].items() if k!="receipt"}
    eq(projected,wanted,(context,"independent event state"))
    eq(list(old.core_paths(s)),[("core",)],(context,"one active serialized core"))
    full=current_parent(s,catalog)
    eq(list(old.core_paths(full)),[("parent","parent","producer","core")],(context,"one reconstructed core"))
    eq(s["core"]["q"]&1,old.pview(base)["core"]["q"]&1,(context,"same actor bit"))
    assert s["core"]["recipient"]>=old.pview(base)["core"]["recipient"],"recipient cannot finance actor"
    omitted=8-cfg["memory_cells"]-int(cfg["adapter"])-int(cfg["initial_port"])
    eq(s["inventory"],dict(memory_cells=cfg["memory_cells"],adapter=cfg["adapter"],
       held_a=int(not e["spare_used"]),held_h=int(not e["spare_used"]),held_accessible=cfg["spare_pair_accessible"],
       retired_ports=int(cfg["initial_port"]) if e["spare_used"] else 0,omitted_pairs=omitted),(context,"typed inventory"))
    eq(s["port"]["route"],cfg["transfer"],(context,"supplied route fixed"))
    eq(s["reserves"]["idle_common"],23-cfg["training_reserve"]-cfg["later_reserve"],(context,"idle common"))
    eq(s["reserves"]["idle_source"],16-sum(cfg["native_packets"])-cfg["later_packet"],(context,"idle source"))
    eq(s["reserves"]["saved_assembly"],omitted,(context,"omitted assembly bill"))
    parent_energy=old.retained(base)
    retained=independent_retained(s,catalog)
    expected_initial=parent_energy+39+omitted
    eq(s["accounting"],dict(parent_retained=parent_energy,parent_spent=411-parent_energy,
        parent_fixed_retained=parent_energy-old.core_energy(old.pview(base)["core"]),
        extra_construction_spent=26-omitted,initial_retained=expected_initial),(context,"actual baseline accounts"))
    eq(retained+sum(s["new_spent"].values())+s["new_waste"],expected_initial,(context,"continuing energy"))
    eq((411-parent_energy)+(26-omitted)+retained+sum(s["new_spent"].values())+s["new_waste"],476,(context,"whole original energy"))
    i=s["inventory"]
    eq(42+2*(i["memory_cells"]+int(i["adapter"])+int(s["port"]["built"])+i["retired_ports"]+i["omitted_pairs"])+i["held_a"]+i["held_h"],60,(context,"whole material"))
    for k in ("fuel","source","recipient","escrow"):assert s["core"][k]>=0


def expected_metrics(e,base,final,catalog):
    tail=e["trace"][-1]
    first=e["outcomes"][0] if e["outcomes"] else {}
    second=e["outcomes"][1] if len(e["outcomes"])>1 else {}
    c,n,b=tail["core"],tail["native"],tail["spent"]
    out=dict(native_complete=int(n["count"]==3),n=n["n"],
        actual_operation_loss=b["native_operation"]-(6-sum(n["packets"])),
        first_assessment=int(first.get("help",False)),second_assessment=int(second.get("help",False)),
        first_attempted=int(first.get("attempted",False)),second_attempted=int(second.get("attempted",False)),
        first_completed=int(first.get("completed",False)),second_completed=int(second.get("completed",False)),
        first_capture=int(first.get("captured",False)),second_capture=int(second.get("captured",False)),
        replaced=int(tail["spare_used"]),actor=c["fuel"],recipient=c["recipient"],
        recipient_gain=c["recipient"]-old_checker().pview(base)["core"]["recipient"],
        native_source=sum(n["packets"]),source=c["source"],retained=independent_retained(final,catalog),
        new_spent=sum(b.values()),new_waste=tail["waste"],pending_escrow=c["escrow"],
        held_pair=int(not tail["spare_used"]),core_ready=int(tail["meta"]["phase"]=="ready"))
    out.update({"spent_"+k:v for k,v in b.items()})
    return out


def check_row(cfg,arm,oldrow,row,catalog,context):
    e=expected_schedule(cfg,arm,oldrow)
    base=catalog[row["predecessor_ref"]]["state"]
    eq(row["probability"],oldrow["probability"],(context,"ancestral mass"))
    eq(row["observer"],dict(parent=oldrow["observer"],native_signals=cfg["native_signals"],
        actual_work_law=oldrow["observer"]["final_law"]^cfg["late_law_flip"]),(context,"observer separated"))
    expected=e["trace"]
    if not e["admitted"]:
        expected=expected[:-1]  # producer returns after the unchanged blocked marker
    actual=row["runtime_trace"]
    eq(len(actual),len(expected),(context,"complete event word length"))
    for j,(a,b) in enumerate(zip(actual,expected)):
        eq(canonical_event(a["event"],cfg),b["event"],(context,j,"event"))
        eq(a["state"]["parent_ref"],row["predecessor_ref"],(context,j,"same history throughout"))
        check_snapshot(a["state"],b,cfg,catalog,base,(context,j,a["event"]))
    eq(row["state"],actual[-1]["state"],(context,"actual endpoint"))
    metrics=expected_metrics(e,base,row["state"],catalog)
    eq(row["metrics"],metrics,(context,"independent metrics"))
    return len(actual),metrics


def check_preparation(cfg,actual,oldprep):
    a=h=r=i=l=0;f=276;source=200;spent=0;bound=0
    trace=[dict(event="initial",plant=[a,h,r,i,l,f,source],spent=spent)]
    def perform(event):
        nonlocal a,h,r,i,l,f,source,spent
        before=f+source+l
        capacity=60-a-h-int(r!=0)-bound
        if event in ("form_a","form_h"):
            assert not i and f>=1 and capacity>0
            if event=="form_a":a+=1
            else:h+=1
            f-=1
        elif event=="bind_a":
            assert r==0 and a>=1 and f>=1
            a-=1;r=1;f-=1
        elif event=="repair":
            assert r==1 and not i and h>=2 and f>=1
            i=1;f-=1
        elif event=="capture":
            assert i and not l and source>=1
            source-=1;l=1
        elif event=="copy_a":
            assert r==1 and l and capacity>0
            a+=1;l=0
        else:raise AssertionError(("unexpected old formation event",event))
        spent+=before-f-source-l
        assert f+source+l+spent==476
        assert a+h+int(r!=0)+bound<=60
        trace.append(dict(event=event,plant=[a,h,r,i,l,f,source],spent=spent))
    for event in ["form_a"]*9+["form_h"]*9:perform(event)
    allowed={"form_a","form_h","bind_a","bind_h","copy_a","copy_h","repair","capture"}
    oldword=[x for x in oldprep["trace"][1:] if "plant" in x and x["event"] in allowed]
    for row in oldword:
        perform(row["event"])
        pa,ph,pr,pi,pl,pf,ps=row["plant"]
        eq([a,h,r,i,l,f,source],[pa+9,ph+9,pr,pi,pl,pf+31,ps+16],"exact old formation projection")
    eq([a,h,r,i,l,f,source],[29,30,1,1,1,227,186],"formed M60")
    assemblies=cfg["memory_cells"]+int(cfg["adapter"])+int(cfg["initial_port"])
    for j in range(assemblies+20):
        assert a>=1 and h>=1 and f>=1
        a-=1;h-=1;f-=1;spent+=1;bound+=2
        kind="assemble_evaluation_component" if j<assemblies else "old_assembly"
        ordinal=j if j<assemblies else j-assemblies
        trace.append(dict(event=kind,index=ordinal,plant=[a,h,r,i,l,f,source],spent=spent))
    assert r==1 and h>=1 and l==1 and f>=1
    h-=1;r=0;f=f-1+l;l=0;spent+=1;bound+=2
    omitted=8-assemblies
    eq([a,h,f,source,spent,bound],[1+omitted,1+omitted,199+omitted,186,91-omitted,58-2*omitted],"prepared M60")
    trace.append(dict(event="exact_M42_projection",fuel=f,source=source,free_a=a,free_h=h,spent=spent,
                      parent_fuel=f-23-omitted,parent_source=source-16))
    expected=dict(material=60,construction_spent=spent,extra_construction_spent=26-omitted,
                  omitted_pairs=omitted,saved_assembly=omitted,trace=trace,parent_preparation_sha256=object_sha(oldprep))
    eq(actual,expected,"complete independent preparation")
    return len(trace)


def comparison_checks(data,specs):
    matched=0
    for item in specs["cases"]:
        case=data["cases"][item["name"]]
        for producer in specs["parent_producers"]:
            groups=[case["arms"][arm]["producers"][producer]["paths"] for arm in specs["principal_arms"]]
            for rows in zip(*groups):
                cuts=[]
                for row in rows:
                    t=row["runtime_trace"]
                    cut=next((j for j,x in enumerate(t) if x["event"]=="evaluation1.write"),len(t))
                    cuts.append(t[:cut])
                # If there is no first assessment, a later assessment can be
                # the first policy-dependent event after hardware replacement.
                if any(not any(x["event"]=="evaluation1.write" for x in r["runtime_trace"]) for r in rows):
                    cuts=[]
                    for row in rows:
                        t=row["runtime_trace"]
                        cut=next((j for j,x in enumerate(t) if x["event"] in ("evaluation1.write","evaluation2.write")),len(t))
                        cuts.append(t[:cut])
                eq(cuts[0],cuts[1],(item["name"],producer,"same perception/training before policy"))
                eq(cuts[0],cuts[2],(item["name"],producer,"conventional same acquired input"))
                matched+=1
    fixed_contrasts=permission_boundaries=retired_boundaries=0
    for producer in specs["parent_producers"]:
        baseline=data["cases"]["signals_000"]["arms"]["shared"]["producers"][producer]["paths"]
        fixed=data["cases"]["fixed_coefficient"]["arms"]["shared"]["producers"][producer]["paths"]
        for zero,constant in zip(baseline,fixed):
            eq(zero["predecessor_ref"],constant["predecessor_ref"],"fixed000 same origin")
            z,c=zero["state"],constant["state"]
            eq(z["native"],c["native"],"fixed000 identical actually acquired coefficient")
            if c["outcomes"]["first_assessment"] is True:
                assert z["native"]["n"]==0 and z["outcomes"]["first_assessment"] is False
                fixed_contrasts+=1
        for row in data["cases"]["permission_loss"]["arms"]["shared"]["producers"][producer]["paths"]:
            s=row["state"]
            if s["outcomes"]["first_assessment"] is True:
                assert s["native"]["n"]==7 and not s["binding"]["permission"]
                assert s["outcomes"]["first_attempted"] and not s["outcomes"]["first_completed"]
                assert not s["outcomes"]["first_capture"] and not s["outcomes"]["second_capture"]
                permission_boundaries+=1
        for row in data["cases"]["signals_111"]["arms"]["identity_gated"]["producers"][producer]["paths"]:
            s=row["state"]
            if (s["native"]["n"]==7 and s["core"]["active"] and s["core"]["fuel"]>=8 and
                s["core"]["source"]>=10 and all(s["binding"].values()) and
                s["physical"]["core_phase"]=="ready" and s["port"]["mode"]=="consumed"):
                assert not read_enabled(port_mode=s["port"]["mode"],native_count=3,core_phase="ready",fuel=s["core"]["fuel"])
                cmd=old_checker().snapshot_command(current_parent(s,data["parent_catalog"]),"reason")
                assert cmd==old_checker().candidate(s["core"])
                assert not use_start_enabled(port_mode=s["port"]["mode"],current=True,same_destination=True,
                    scope=True,permission=True,delivery=True,core_phase="ready",source=s["core"]["source"],candidate=cmd,supported=cmd)
                assert not replacement_enabled(native_count=3,first_closed=True,old_port_present=True,
                    old_port_mode="consumed",core_phase="ready",spare_accessible=True,spare_used=True,reserve=11)
                retired_boundaries+=1
    assert fixed_contrasts and permission_boundaries and retired_boundaries
    return dict(matched_input_histories=matched,fixed000_contrasts=fixed_contrasts,
                permission_preserves_assessment=permission_boundaries,actual_funded_retired_port_boundaries=retired_boundaries)


def mutation_checks(data,specs,old_data):
    configs={x["name"]:x["config"] for x in specs["cases"]}
    results=[]
    def select(case,arm="shared",positive=True):
        for producer in specs["parent_producers"]:
            for index,row in enumerate(data["cases"][case]["arms"][arm]["producers"][producer]["paths"]):
                if row["state"]["native"]["count"]==3 and (not positive or row["state"]["outcomes"]["first_capture"]):
                    return producer,index,row
        raise AssertionError(("no real mutation fixture",case,arm))
    def rejected(name,case,arm,change,positive=True):
        producer,index,row=select(case,arm,positive)
        mutant=deepcopy(row)
        change(mutant)
        cfg=configs[case]
        original=old_data["cases"][cfg["parent_revision_case"]]["producers"][producer]["paths"][index]
        try:check_row(cfg,arm,original,mutant,data["parent_catalog"],("mutation",name))
        except AssertionError as error:
            results.append(dict(name=name,status="rejected",case=case,producer=producer,path_index=index,
                                reason=str(error)[:350]))
        else:raise AssertionError(("mutation survived",name))
    rejected("initial_unacquired_weight", "signals_111","shared",
             lambda r:r["runtime_trace"][0]["state"]["native"].update(n=7))
    def whole_lesson_window(r):
        n=0
        for item in r["runtime_trace"]:
            if item["event"]=="native.read_known":item["state"]["native"]["bit"]=True
            if item["event"]=="native.write":n=n//2+4
            item["state"]["native"]["n"]=n
        r["state"]=deepcopy(r["runtime_trace"][-1]["state"])
        r["metrics"]["n"]=n
    rejected("complete_wrong_loss_window_keeps_private_payments", "signals_000","identity_gated",whole_lesson_window,False)
    def source_destroy(r):
        used=set()
        for item in r["runtime_trace"]:
            s=item["state"]
            if item["event"]=="native.return":used.add(s["native"]["count"])
            for index in used:s["native"]["packets"][index]=0
            s["new_waste"]+=2*len(used)
        r["state"]=deepcopy(r["runtime_trace"][-1]["state"])
        r["metrics"].update(native_source=0,new_waste=r["metrics"]["new_waste"]+6,retained=r["metrics"]["retained"]-6)
    rejected("complete_unavailable_source_dissipation_preserves_energy", "signals_111","shared",source_destroy)
    def redirect(r):
        moved=0
        for item in r["runtime_trace"]:
            if item["event"] in ("recipient1.work","recipient2.work"):
                moved+=10
            item["state"]["core"]["fuel"]+=moved
            item["state"]["core"]["recipient"]-=moved
        r["state"]=deepcopy(r["runtime_trace"][-1]["state"])
    rejected("complete_recipient_receipts_redirected_to_actor", "signals_111","shared",redirect)
    def reset_qualification(r):
        item=next(x for x in r["runtime_trace"] if x["event"]=="native.write")
        item["state"]["core"]["last"]=False
    rejected("native_training_rewrites_unrelated_qualification", "signals_111","shared",reset_qualification)
    def clone_core(r):r["runtime_trace"][0]["state"]["native"]["core"]=deepcopy(r["state"]["core"])
    rejected("duplicate_active_core", "signals_111","shared",clone_core)
    def free_replace(r):
        item=next(x for x in r["runtime_trace"] if x["event"]=="replacement.assemble")
        item["state"]["inventory"]["held_a"]=1
        item["state"]["inventory"]["held_h"]=1
    rejected("replacement_reuses_held_pair", "signals_111","shared",free_replace)
    def prepay_source(r):
        item=next(x for x in r["runtime_trace"] if x["event"]=="native.pay")
        item["state"]["native"]["packets"][0]-=2
        item["state"]["core"]["fuel"]+=2
    rejected("native_source_finances_before_return", "signals_111","shared",prepay_source)
    def q_mismatch(r):
        item=next(x for x in r["runtime_trace"] if x["event"]=="evaluation1.write")
        item["state"]["core"]["q"]^=2
    rejected("recipient_q_mismatches_current_fact", "signals_111","shared",q_mismatch)
    def actor_sense(r):
        item=next(x for x in r["runtime_trace"] if x["event"]=="recipient1.sense")
        item["state"]["physical"]["core_target"]="actor"
    rejected("actor_target_substituted", "signals_111","shared",actor_sense)
    def repeat_read(r):
        s=deepcopy(r["state"])
        s["core"]["fuel"]-=1;s["new_spent"]["evaluation_read"]+=1;s["port"]["mode"]="read"
        r["runtime_trace"].append(dict(event="evaluation2.read",state=s));r["state"]=s
    rejected("funded_retired_port_reads_again", "signals_111","identity_gated",repeat_read,False)
    # Provenance test repairs the forged local hash too; the independently
    # retained accepted history still defeats substitution.
    forged=deepcopy(data["parent_catalog"])
    ref=next(k for k,v in forged.items() if v["state"]["opened"])
    forged[ref]["state"]["selected_bank"]="old"
    forged[ref]["state_sha256"]=object_sha(forged[ref]["state"])
    try:check_catalog(forged,old_data,specs)
    except AssertionError:results.append(dict(name="historical_bank_substitution_with_recomputed_local_hash",status="rejected",parent_ref=ref))
    else:raise AssertionError("forged ancestry survived")
    # Boundary-only guard controls do not pretend to be additional runs.
    for label,call in [
        ("repeat_native_write",lambda:native_write(Native(10,0,numerator=7,completed=3,mode="closed"))),
        ("return_again",lambda:native_return(Native(10,4,mode="returned"),2)),
        ("missing_source_cannot_fabricate_return",lambda:native_return(Native(10,4,sources=(0,2,2),mode="paid"),2))]:
        try:call()
        except AssertionError:results.append(dict(name=label,status="rejected",scope="independent guard boundary, not extra experiment arm"))
        else:raise AssertionError((label,"guard survived"))
    return results


def main():
    repo=next(p for p in HERE.parents if (p/"AGENTS.md").exists())
    freeze=read_json(HERE/"protocol-freeze.json")
    for name,sha in freeze["parent_source_sha256"].items():
        eq(hashlib.sha256((repo/name).read_bytes()).hexdigest(),sha,("frozen predecessor",name))
    specs=read_json(HERE/"cases.json")
    files=read_json(HERE/"result-files.json")
    compressed=(HERE/files["file"]).read_bytes()
    eq(hashlib.sha256(compressed).hexdigest(),files["compressed_sha256"],"result compressed bytes")
    raw=gzip.decompress(compressed)
    eq(hashlib.sha256(raw).hexdigest(),files["uncompressed_sha256"],"result exact JSON bytes")
    data=json.loads(raw)
    for name,sha in data["source_sha256"].items():
        eq(hashlib.sha256((repo/name).read_bytes()).hexdigest(),sha,("current numerical source",name))
    old_data=read_json(PARENT/"results.json.gz")
    old_fixtures=read_json(PARENT/"fixtures.json")
    fixtures=read_json(HERE/"fixtures.json")
    check_catalog(data["parent_catalog"],old_data,specs)
    histories=prefixes=metrics_count=preparation_prefixes=0
    for case in specs["cases"]:
        name,cfg=case["name"],case["config"]
        actualcase=data["cases"][name]
        eq(actualcase["config"],cfg,(name,"frozen configuration"))
        preparation_prefixes+=check_preparation(cfg,fixtures["preparations"][name],old_fixtures["preparations"][cfg["parent_revision_case"]])
        for arm in specs["principal_arms"]:
            for producer in specs["parent_producers"]:
                group=actualcase["arms"][arm]["producers"][producer]
                oldrows=old_data["cases"][cfg["parent_revision_case"]]["producers"][producer]["paths"]
                eq(len(group["paths"]),len(oldrows),(name,arm,producer,"all histories"))
                totals={};mass=Fraction(0)
                for index,(oldrow,row) in enumerate(zip(oldrows,group["paths"])):
                    prefix_index,_=inherited_prefix(oldrow)
                    eq(row["predecessor_ref"],f'{cfg["parent_revision_case"]}/{producer}/{index}/{prefix_index}',"exact row ancestry")
                    number,m=check_row(cfg,arm,oldrow,row,data["parent_catalog"],(name,arm,producer,index))
                    probability=Fraction(row["probability"]);mass+=probability
                    prefixes+=number;histories+=1
                    for key,value in m.items():totals[key]=totals.get(key,Fraction(0))+probability*value
                eq(mass,Fraction(1),(name,arm,producer,"unconditional mass"))
                eq(group["metrics"],{k:str(v) for k,v in sorted(totals.items())},(name,arm,producer,"exact aggregates"))
                metrics_count+=len(totals)
        print(name,"independently reconstructed",flush=True)
    counts=dict(cases=len(specs["cases"]),mixtures=len(specs["cases"])*len(specs["principal_arms"])*len(specs["parent_producers"]),
                histories=histories,prefixes=prefixes,aggregate_metrics=metrics_count,
                preparation_prefix_comparisons=preparation_prefixes,catalog_entries=len(data["parent_catalog"]))
    comparisons=comparison_checks(data,specs)
    mutations=mutation_checks(data,specs,old_data)
    reporting=read_json(HERE/"reporting.json")
    eq(reporting["source_sha256"],data["source_sha256"],"report source metadata")
    eq(reporting["result_files"],files,"report result identity")
    wanted_report={name:{arm:{producer:group["metrics"] for producer,group in bundle["producers"].items()}
                        for arm,bundle in case["arms"].items()} for name,case in data["cases"].items()}
    eq(reporting["cases"],wanted_report,"all reported metrics independently reconstructed")
    eq(reporting["counts"],{k:counts[k] for k in ("cases","histories","prefixes")},"report exact counts")
    inputs=[HERE/x for x in ("check_model.py","model.py","DRAFT-PROTOCOL.md","cases.json","INTERFACE.md",
          "protocol-freeze.json","results.json.gz","result-files.json","fixtures.json","reporting.json","first-run-receipt.json")]
    inputs.extend([PARENT/"check_model.py",PARENT/"results.json.gz",PARENT/"fixtures.json"])
    report=dict(status="passed",counts=counts,comparisons=comparisons,mutations=mutations,
        mutation_count=len(mutations),source_sha256={str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        independence="Prospective native and full schedule bytes are preserved in review-history. No new producer transitions are imported; only accepted old independent RI/account helpers.",
        scope="Exact finite inherited-history reconstruction and supplemental adversarial checks. Formal law and ethical applicability are separate reviews; no new empirical test.")
    (HERE/"model-verification.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","counts","comparisons","mutation_count")},indent=2))
    return data,counts


if __name__=="__main__":
    main()
