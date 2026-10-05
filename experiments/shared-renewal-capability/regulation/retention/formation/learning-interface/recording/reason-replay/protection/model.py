"""Independent finite physical and strategic reason-to-protection model.

The predecessor is the independently implemented Python reader, not Lean or the
old settlement game. Cash never changes physical fuel. Dated trustee objectives
and the external commercial ecology are explicit model inputs.
"""

from dataclasses import asdict, dataclass, replace
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("protection_reader_model", HERE.parent / "check_model.py")
rr = module_from_spec(spec)
sys.modules[spec.name] = rr
spec.loader.exec_module(rr)


def members(mask):
    return tuple(i for i in range(2) if mask & (1 << i))


@dataclass(frozen=True)
class State:
    core: rr.State
    gate: bool = False
    lease: object = None
    safe: int = 0
    authority: bool = True
    cuts: int = 0
    episode_open: bool = False
    forced_open: bool = False
    harm: tuple = (0, 0)

    def material(self):
        return self.core.material() + 2 * int(self.gate)

    def energy(self):
        return self.core.energy()

    def valid(self):
        r = self.core.record
        busy = int(r.pending != "idle")
        return (r.slots == r.blank + busy + len(r.records)
                and r.escrow == busy and self.material() <= 17
                and 0 <= self.safe <= 3 and 0 <= self.cuts <= 3)


def fuel(s):
    return s.core.record.plant.fuel


def pay_fuel(s, amount):
    assert fuel(s) >= amount
    return replace(s, core=replace(s.core, record=replace(s.core.record,
                   plant=replace(s.core.record.plant, fuel=fuel(s) - amount))))


def required(s):
    if s.lease is None or not s.authority or not s.core.delivery:
        return 0
    return s.lease[1] & ~s.cuts


def enabled(s, event):
    kind, arg = event
    if kind == "reader":
        return rr.enabled(s.core, arg)
    if kind == "assemble_gate":
        p = s.core.record.plant
        return not s.gate and s.core.record.pending == "idle" and p.a > 0 and p.h > 0 and p.fuel > 0
    if kind == "begin":
        return not s.episode_open and s.core.record.pending == "idle"
    if kind == "arm":
        return (arg in (1, 2, 3) and s.gate and s.episode_open and not s.forced_open
                and s.lease is None and s.authority and s.core.delivery and fuel(s) >= 1)
    if kind == "safeguard":
        return s.gate and s.episode_open and arg in (0, 1) and not s.safe & (1 << arg) and fuel(s) >= 1
    if kind == "release":
        return (s.episode_open and s.lease is not None and s.lease[0] == s.core.context
                and not required(s) & ~s.safe and fuel(s) >= 1)
    if kind == "release_open":
        return s.episode_open and s.lease is None and fuel(s) >= 1
    if kind == "withdraw":
        return s.episode_open and not s.forced_open
    if kind == "refuse":
        return s.episode_open
    if kind == "private":
        return fuel(s) >= 1 and s.episode_open and s.core.record.pending == "idle"
    if kind in ("force_open", "cut"):
        return s.episode_open
    if kind == "authority":
        return True
    raise ValueError(event)


def step(s, event):
    assert s.valid() and enabled(s, event), (event, s)
    kind, arg = event
    cost = 0
    if kind == "reader":
        core, cost = rr.step(s.core, arg)
        retained = arg[0] in ("access", "delivery")
        t = replace(s, core=core, lease=s.lease if retained else None,
                    safe=s.safe if retained else 0)
    elif kind == "assemble_gate":
        p = s.core.record.plant
        core = replace(s.core, record=replace(s.core.record,
                       plant=replace(p, a=p.a - 1, h=p.h - 1, fuel=p.fuel - 1)))
        t, cost = replace(s, core=core, gate=True), 1
    elif kind == "begin":
        t = replace(s, lease=None, safe=0, cuts=0, episode_open=True, forced_open=False)
    elif kind == "arm":
        t, cost = replace(pay_fuel(s, 1), lease=(s.core.context, arg)), 1
    elif kind == "safeguard":
        t, cost = replace(pay_fuel(s, 1), safe=s.safe | (1 << arg)), 1
    elif kind in ("release", "release_open"):
        harm = tuple(s.harm[i] + int(not (s.safe & (1 << i))) for i in range(2))
        t, cost = replace(pay_fuel(s, 1), lease=None, safe=0, episode_open=False, harm=harm), 1
    elif kind in ("withdraw", "refuse"):
        t = replace(s, lease=None, safe=0, episode_open=False)
    elif kind == "private":
        t, cost = pay_fuel(s, 1), 1
    elif kind == "force_open":
        t = replace(s, lease=None, forced_open=True)
    elif kind == "authority":
        t = replace(s, authority=arg)
    elif kind == "cut":
        t = replace(s, cuts=s.cuts | arg)
    else:
        raise ValueError(event)
    assert t.valid() and t.material() == s.material()
    assert t.energy() + cost == s.energy()
    assert t.core.record.plant.source <= s.core.record.plant.source
    if kind != "reader":
        assert t.core.record.records == s.core.record.records
        assert t.core.installed == s.core.installed
    return t, cost


def run(s, events, capture=False):
    spent, snapshots = 0, []
    for index, event in enumerate(events):
        if not enabled(s, event):
            return s, False, spent, index, snapshots
        s, cost = step(s, event)
        spent += cost
        if capture:
            snapshots.append({"event": event, "cost": cost, "state": asdict(s)})
    return s, True, spent, None, snapshots


def reader_events(events):
    return tuple(("reader", event) for event in events)


AUDIT = reader_events(rr.AUDIT)


def prepare(original_fuel=83, original_source=20, build_gate=True):
    """Actual M17, or an explicitly separate M15 no-spare-gate control."""
    material = 17 if build_gate else 15
    pairs = (material - 1) // 2
    assert original_fuel >= material + 9 + int(build_gate) and original_source >= 0
    p = rr.Plant(0, 0, "empty", False, False, original_fuel, original_source)
    initial = asdict(p)
    snapshots = []
    for event in ("formH",) * pairs + ("formA",) * (pairs+1) + ("associateA", "repair"):
        before = p
        if event in ("formA", "formH"):
            assert not p.intact and p.population() < material and p.fuel > 0
            field = "a" if event == "formA" else "h"
            p = replace(p, **{field: getattr(p, field) + 1}, fuel=p.fuel - 1)
        elif event == "associateA":
            assert p.a > 0 and p.resident == "empty" and p.fuel > 0
            p = replace(p, a=p.a - 1, resident="active", fuel=p.fuel - 1)
        else:
            assert p.resident == "active" and not p.intact and p.fuel > 0
            p = replace(p, intact=True, fuel=p.fuel - 1)
        assert p.energy() + 1 == before.energy()
        snapshots.append({"stage": "formation", "event": event, "plant": asdict(p)})
    assert p.population() == material and p.a == p.h == pairs
    r = rr.Record(p, 0, 0, "idle", None, 0, ())
    for i in range(6):
        p = r.plant
        assert p.a > 0 and p.h > 0 and p.fuel > 0
        r = replace(r, plant=replace(p, a=p.a - 1, h=p.h - 1, fuel=p.fuel - 1),
                    slots=r.slots + 1, blank=r.blank + 1)
        assert r.material() == material
        snapshots.append({"stage": "slot", "record": asdict(r)})
    p = r.plant
    r = replace(r, plant=replace(p, a=p.a - 1, h=p.h - 1, fuel=p.fuel - 1))
    core = rr.State(r, True, False, 0, None, (), 0, None, True, True)
    s = State(core)
    assert s.material() == material and s.valid()
    snapshots.append({"stage": "reader", "state": asdict(s)})
    if build_gate:
        s, cost = step(s, ("assemble_gate", None))
        assert cost == 1 and s.core.valid()
        snapshots.append({"stage": "gate", "state": asdict(s)})
    spent = material + 9 + int(build_gate)
    assert s.energy() + spent == original_fuel + original_source
    return s, {"initial": initial, "material_capacity": material, "steps": snapshots, "spent": spent}


def prelude(s, episode):
    if episode == 0:
        events = reader_events(rr.recording_events((True, True, True)))
    elif episode == 1:
        events = (("reader", ("context", True)),) + reader_events(rr.recording_events((False, True, True)))
    elif episode == 2:
        events = (("reader", ("turnover", None)),)
    else:
        raise ValueError(episode)
    return run(s, events)


def action_word(mask):
    return (("arm", mask),) + tuple(("safeguard", i) for i in members(mask)) + (("release", None),) if mask else (("release_open", None),)


def primary_history():
    s, formation = prepare()
    checkpoints, total = [], 0
    for t, mask in enumerate((3, 2, 2)):
        s, completed, cost, blocked, _ = prelude(s, t)
        assert completed, blocked
        total += cost
        s, _ = step(s, ("begin", None))
        s, completed, cost, _, _ = run(s, AUDIT)
        assert completed and s.core.installed == (s.core.context, mask)
        total += cost
        before = fuel(s)
        s, completed, cost, _, events = run(s, action_word(mask), capture=True)
        assert completed and cost == 2 + len(members(mask))
        total += cost
        checkpoints.append({"episode": t, "mask": mask, "action_spending": cost,
                            "before_action_fuel": before, "state": asdict(s), "action_events": events})
    assert fuel(s) == 3 and s.core.record.plant.source == 18 and s.harm == (2, 0)
    assert s.energy() == 21 and formation["spent"] + total + s.energy() == 103
    return s, {"formation": formation, "checkpoints": checkpoints,
               "account": {"initial": 103, "preparation": 19, "slots": 6, "reader": 1,
                           "gate": 1, "recording": 12, "audits": 33, "actions": 10, "final": 21}}


@dataclass(frozen=True)
class Params:
    original_fuel: int = 83
    original_source: int = 20
    cash: int = 5
    upkeep: int = 2
    outside: int = 20
    private_fee: int = 1
    private_receipt: int = 2
    audit_fee: int = 2
    audit_receipt: int = 4
    durable_fee: int = 3
    durable_receipt: int = 12
    filter_fee: int = 5
    force_fee: int = 5
    concern: int = 5
    trade: int = 7
    outside_option: int = 1
    operator_trade: int = 7
    safeguard_cash: int = 2
    suppression: int = 5
    shared_cut: int = 5
    leaf_cut: int = 3
    authority: bool = True
    delivery: bool = True
    access: bool = True
    context_interrupt: bool = False
    gate: bool = True


def gate_price(mask):
    return 0 if not mask else 2 + len(members(mask))


def cuts(params):
    return tuple((i, (params.shared_cut if i & 1 else 0)
                  + params.leaf_cut * ((bool(i & 2)) + (bool(i & 4))),
                  3 if i & 1 else (int(bool(i & 2)) | (2 * int(bool(i & 4)))))
                 for i in range(8))


class Game:
    """Finite perfect-information game; exact integer utility scaled by four.

    At episode t the operator's cash flow is weighted by 2**(2-t), so all
    comparisons implement discount 1/2 without floating-point arithmetic.
    Trustee selves value their own episode only. Full physical states are
    retained in the recursion. A declared deterministic tie policy selects one
    subgame-perfect continuation; tied actions are reported, not called unique.
    """

    def __init__(self, params=Params(), conventional=False, quotient=True):
        assert all(value >= 0 for value in asdict(params).values())
        self.p = params
        self.conventional = conventional
        self.quotient = quotient
        self.bank_bound = params.suppression + params.shared_cut + 2*params.leaf_cut + 2*params.safeguard_cash
        self.bank_saturated = params.outside >= self.bank_bound
        self.counts = {k: 0 for k in ("states", "cold_options", "warm_options", "operator_options", "ties")}
        self.opening_attempts = {}
        self.decide = lru_cache(None)(self._decide)
        self.task = lru_cache(None)(self._task)
        self.responses = lru_cache(None)(self._responses)

    def choose(self, options, key):
        assert options
        best = max(key(x) for x in options)
        tied = [x for x in options if key(x) == best]
        self.counts["ties"] += int(len(tied) > 1)
        labels = [{k: x[-1].get(k) for k in
                   ("route", "suppression", "gate", "protected", "cut", "response", "cash", "harm_delta")}
                  for x in tied]
        return tied[0], labels

    def next_value(self, t, state, cash, bank):
        return 0 if t == 2 else self.solve(t + 1, state, cash, bank)[0]

    def product(self, s, name):
        return self.task(s, name if name in ("none", "private") else "audit")

    def _task(self, s, name):
        if name == "none":
            return s, True, 0, None
        if name == "private":
            end, complete, spent, blocked, _ = run(s, (("private", None),))
            return end, complete, spent, blocked
        events = AUDIT
        if self.p.context_interrupt:
            events = AUDIT[:1] + (("reader", ("context", not s.core.context)),) + AUDIT[1:]
        end, complete, spent, blocked, _ = run(s, events)
        return end, complete, spent, blocked

    def _responses(self, armed):
        """Cache exact physical words, independently of monetary balances."""
        rows = []
        for cut_index, attack_fee, excluded in cuts(self.p):
            attacked = step(armed, ("cut", excluded))[0]
            for protected in range(4):
                guarded, ok, _, _, _ = run(attacked, tuple(("safeguard", i) for i in members(protected)))
                if not ok:
                    continue
                for produce in (False, True):
                    event = ("release" if guarded.lease is not None else "release_open", None) if produce else ("refuse", None)
                    if enabled(guarded, event):
                        end = step(guarded, event)[0]
                        rows.append((cut_index, attack_fee, protected, produce, end))
        return tuple(rows)

    def solve(self, t, state, cash, bank):
        assert cash >= 0 and bank >= 0
        opening = state
        state, complete, pre_spent, blocked, _ = prelude(state, t)
        if not complete or cash < self.p.upkeep:
            return 0, {"episode": t, "route": "terminal_failure", "reason": "acquisition" if not complete else "cash_upkeep",
                       "state": state, "cash": cash, "bank": bank, "prelude_spent": pre_spent,
                       "blocked_prelude_event": blocked, "production": False, "harm_delta": (0, 0), "end": True}
        state, _ = step(state, ("begin", None))
        # Exact payoff quotient, not a physical event: old cumulative harms do
        # not enter guards and each dated utility uses only this episode's
        # increment. A bank offset is irrelevant only when the next external
        # inflow alone funds suppression + every cut + both safeguards. The
        # operator evaluates flows, not the absolute bank level. Fuel, source,
        # cash, reader fields and every physical alternative remain in the key.
        old_harm = state.harm if self.quotient else (0, 0)
        bank_offset = bank if self.quotient and self.bank_saturated else 0
        representative = replace(state, harm=(0, 0)) if self.quotient else state
        value, record = self.decide(t, representative, cash, bank-bank_offset)
        actual_end = replace(record["state"], harm=tuple(record["state"].harm[i] + old_harm[i] for i in range(2)))
        return value, dict(record, state=actual_end, bank=record["bank"]+bank_offset,
                           prelude_spent=pre_spent, start_fuel=fuel(opening))

    def _decide(self, t, state, cash, bank):
        self.counts["states"] += 1
        available = cash - self.p.upkeep
        funded_bank = bank + self.p.outside
        p = self.p
        route_menu = (("none", 0, 0, 0), ("private", p.private_fee, p.private_receipt, 0),
                      ("audit_only", p.audit_fee, p.audit_receipt, 0),
                      ("durable", p.durable_fee, p.durable_receipt, 0),
                      ("filter", p.durable_fee, p.durable_receipt, p.filter_fee),
                      ("forced", p.durable_fee, p.durable_receipt, p.force_fee))
        suppression_options = []
        for suppression in (False, True):
            suppression_cost = p.suppression if suppression else 0
            if funded_bank < suppression_cost:
                continue
            current_bank = funded_bank - suppression_cost
            cold = []
            for name, fee, receipt, insulation in route_menu:
                if available < fee:
                    continue
                if name != "none":
                    first_event = ("private", None) if name == "private" else AUDIT[0]
                    if not enabled(state, first_event):
                        continue
                after, product_complete, work_spent, product_blocked = self.product(state, name)
                gained = receipt if product_complete else 0
                product_cash = available - fee + gained
                service_installed = name in ("filter", "forced") and product_complete and product_cash >= insulation
                product_cash -= insulation if service_installed else 0
                if name == "forced" and service_installed:
                    after, _ = step(after, ("force_open", None))
                audited = name not in ("none", "private") and product_complete
                current = audited and after.core.phase == 10 and after.core.installed is not None and after.core.installed[0] == after.core.context
                admitted = after.core.installed[1] if current else 0
                if self.conventional and current:
                    conventional = rr.closure_oracle(rr.PRIMARY_GRAPH, after.core.decoded)
                    assert conventional == admitted
                    admitted = conventional
                learned = admitted if current and not suppression and not (name == "filter" and service_installed) else 0
                warm = []
                base = {"episode": t, "route": name, "suppression": suppression,
                        "start_cash": cash, "after_upkeep": available, "after_fee": available-fee,
                        "after_receipt": available-fee+gained, "after_insulation": product_cash,
                        "product_complete": product_complete, "product_blocked": product_blocked,
                        "post_task_service_installed": service_installed,
                        "product_fuel_spent": work_spent,
                        "admitted": admitted, "uptake": learned,
                        "before_product_fuel": fuel(state), "after_product_fuel": fuel(after)}
                if t == 0 and not suppression:
                    self.opening_attempts[name] = dict(base, state_before_warm=asdict(after))
                if enabled(after, ("withdraw", None)):
                    withdrawn, _ = step(after, ("withdraw", None))
                    end_cash = product_cash + p.outside_option
                    flow = p.outside - suppression_cost
                    value = (1 << (2-t))*flow + self.next_value(t, withdrawn, end_cash, current_bank)
                    record = dict(base, gate=0, protected=0, cut=0, attack_fee=0,
                                  production=False, response="withdrawal", harm_delta=(0, 0),
                                  state=withdrawn, cash=end_cash, bank=current_bank, operator_flow=flow)
                    warm.append((end_cash, end_cash, value, record))
                for guarded in range(4):
                    if after.forced_open and guarded:
                        continue
                    price = gate_price(guarded)
                    if product_cash < price or (guarded and not enabled(after, ("arm", guarded))):
                        continue
                    armed = step(after, ("arm", guarded))[0] if guarded else after
                    paid = product_cash - price
                    responses = []
                    # No-work refusal is first; later rows also include legal
                    # sunk safeguards followed by refusal, whose fuel can matter.
                    for cut_index, attack_fee, protected, produce, end in self.responses(armed):
                        safeguard_bill = p.safeguard_cash * len(members(protected))
                        if current_bank < attack_fee + safeguard_bill:
                            continue
                        spent_bank = current_bank - attack_fee - safeguard_bill
                        end_cash = paid + (p.trade if produce else p.outside_option)
                        end_bank = spent_bank + (p.operator_trade if produce else 0)
                        flow = p.outside - suppression_cost - attack_fee - safeguard_bill + (p.operator_trade if produce else 0)
                        value = (1 << (2-t))*flow + self.next_value(t, end, end_cash, end_bank)
                        harm = tuple(end.harm[i] - after.harm[i] for i in range(2))
                        record = dict(base, gate=guarded, gate_price=price, protected=protected,
                                      cut=cut_index, attack_fee=attack_fee, production=produce,
                                      response="production" if produce else "refusal", harm_delta=harm,
                                      state=end, cash=end_cash, bank=end_bank, operator_flow=flow)
                        responses.append((value, end_cash, harm, record))
                        self.counts["operator_options"] += 1
                    chosen, ties = self.choose(responses, lambda x: x[0])
                    value, end_cash, harm, record = chosen
                    record["operator_ties"] = len(ties)
                    record["operator_tied_alternatives"] = ties
                    score = end_cash - p.concern * sum(harm[i] for i in members(learned))
                    warm.append((score, end_cash, value, record))
                chosen, ties = self.choose(warm, lambda x: x[0])
                score, end_cash, value, record = chosen
                record = dict(record, warm_score=score, warm_ties=len(ties), warm_tied_alternatives=ties)
                cold.append((end_cash, value, record))
                self.counts["warm_options"] += len(warm)
                self.counts["cold_options"] += 1
            chosen, ties = self.choose(cold, lambda x: x[0])
            _, value, record = chosen
            record = dict(record, cold_ties=len(ties), cold_tied_alternatives=ties)
            suppression_options.append((value, record))
        chosen, ties = self.choose(suppression_options, lambda x: x[0])
        value, record = chosen
        record = dict(record, suppression_ties=len(ties), suppression_tied_alternatives=ties)
        return value, record

    def evaluate(self):
        state, formation = prepare(self.p.original_fuel, self.p.original_source, self.p.gate)
        state = replace(state, authority=self.p.authority,
                        core=replace(state.core, delivery=self.p.delivery, access=self.p.access))
        value, _ = self.solve(0, state, self.p.cash, 0)
        cash, bank, trace = self.p.cash, 0, []
        for t in range(3):
            _, result = self.solve(t, state, cash, bank)
            trace.append({k: asdict(v) if k == "state" else v for k, v in result.items()})
            state, cash, bank = result["state"], result["cash"], result["bank"]
            if result.get("end"):
                break
        return {"params": asdict(self.p), "conventional": self.conventional,
                "memoization": {"past_harm_offset": self.quotient, "bank_offset": self.quotient and self.bank_saturated,
                                "maximum_current_operator_bill": self.bank_bound, "outside_inflow": self.p.outside,
                                "exact_fuel_source_reader_and_trustee_cash_retained": True},
                "operator_value_scaled4": value, "trace": trace,
                "final_cash": cash, "final_operator_bank": bank,
                "final_fuel": fuel(state), "final_source": state.core.record.plant.source,
                "harm": state.harm, "counts": dict(self.counts),
                "opening_product_attempts": self.opening_attempts,
                "cache_states": self.decide.cache_info().currsize,
                "formation_spent": formation["spent"]}
