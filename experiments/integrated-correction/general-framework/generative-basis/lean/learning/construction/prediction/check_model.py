#!/usr/bin/env python3
"""Independent finite checks of the declared typed payable-write predictor.

This implements event tables separately; it imports neither Lean conclusions
nor executable producer code. It checks PredictionAction's restricted phases,
not the broader Python model's outages, skipped writes, erasure or rebuilding.
"""

from collections import deque
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
ASSEMBLY, WORK, PACKET, RENEWAL, SELECTOR_LIFETIME = 1, 3, 10, 2, 6
MODULE_ASSEMBLY, MODULE_LIFETIME, ADAPTER, RETROFIT, RENT, WRITE = 2, 2, 1, 3, 1, 1


@dataclass(frozen=True)
class Prep:
    a: int
    h: int
    resident: str
    intact: bool
    local: bool
    fuel: int
    source: int

    def matter(self):
        return self.a + self.h + int(self.resident != "empty")

    def energy(self):
        return self.fuel + self.source + int(self.local)


@dataclass(frozen=True)
class Physical:
    fuel: int
    packets: int
    last: bool
    lease: int
    regime: bool
    fast: bool
    module_lease: int
    seen: bool
    remainder: int
    material: int

    def energy(self):
        return self.fuel + PACKET * self.packets + self.remainder


@dataclass(frozen=True)
class Parts:
    a: int
    h: int
    resident: str
    intact: bool
    bound_a: int
    bound_h: int
    register_units: int
    precursor: int

    def total(self):
        return (self.a + self.h + self.bound_a + self.bound_h + 2 * self.register_units
                + int(self.resident != "empty") + self.precursor)

    def typed_totals(self):
        return self.a + self.bound_a + self.register_units, self.h + self.bound_h + self.register_units

    def bind(self, a, h):
        assert a <= self.a and h <= self.h
        return replace(self, a=self.a - a, h=self.h - h,
                       bound_a=self.bound_a + a, bound_h=self.bound_h + h)


@dataclass(frozen=True)
class Base:
    physical: Physical
    parts: Parts


@dataclass(frozen=True)
class Prediction:
    physical: Physical
    score: int
    receipt: bool
    phase: str


@dataclass(frozen=True)
class Running:
    prediction: Prediction
    parts: Parts


def prep_step(s, event, material):
    assert s.matter() <= material
    if event in ("formA", "formH"):
        assert not s.intact and s.matter() < material and s.fuel > 0
        field = "a" if event == "formA" else "h"
        t, cost = replace(s, **{field: getattr(s, field) + 1}, fuel=s.fuel - 1), 1
    elif event == "associateA":
        assert s.a > 0 and s.resident == "empty" and s.fuel > 0
        t, cost = replace(s, a=s.a - 1, resident="active", fuel=s.fuel - 1), 1
    elif event == "repair":
        assert s.resident == "active" and not s.intact and s.fuel > 0
        t, cost = replace(s, intact=True, fuel=s.fuel - 1), 1
    elif event == "capture":
        assert s.intact and not s.local and s.source > 0
        t, cost = replace(s, local=True, source=s.source - 1), 0
    else:
        raise ValueError(event)
    assert t.energy() + cost == s.energy() and t.matter() <= material
    return t, cost


def handoff(s, material):
    assert s.matter() <= material and s.intact and s.local
    assert s.a >= 1 and s.h >= 1 and s.fuel >= ADAPTER
    packets, remainder = divmod(s.source, PACKET)
    physical = Physical(s.fuel - ADAPTER + 1, packets, False, 0, True, False,
                        0, False, remainder, material)
    parts = Parts(s.a - 1, s.h - 1, s.resident, s.intact, 1, 1, 0, material - s.matter())
    assert physical.energy() + ADAPTER == s.energy() and parts.total() == material
    return Base(physical, parts)


def base_form(s, kind, arg):
    p = s.physical
    if kind == "module":
        assert p.module_lease == 0 and p.fuel >= MODULE_ASSEMBLY
        parts = s.parts.bind(1, 1)
        q = replace(p, fuel=p.fuel - MODULE_ASSEMBLY, fast=arg, module_lease=MODULE_LIFETIME)
        cost = MODULE_ASSEMBLY
    elif kind == "selector":
        assert p.module_lease > 0 and (not p.fast or not p.seen or arg != p.last)
        assert p.lease == 0 and p.fuel >= ASSEMBLY
        parts = s.parts.bind(0, 2) if arg else s.parts.bind(2, 0)
        q = replace(p, fuel=p.fuel - ASSEMBLY, last=arg, lease=SELECTOR_LIFETIME, seen=True)
        cost = ASSEMBLY
    else:
        raise ValueError(kind)
    assert q.energy() + cost == p.energy() and parts.total() == s.parts.total()
    return Base(q, parts), cost


def coarse_retrofit_enabled(s):
    return s.material >= 2 and s.module_lease > 0 and s.lease > 0 and s.seen and s.fuel >= RETROFIT


def retrofit_enabled(s):
    return coarse_retrofit_enabled(s.physical) and s.parts.a >= 1 and s.parts.h >= 1


def retrofit(s):
    assert retrofit_enabled(s) and s.parts.register_units == 0
    prediction = Prediction(replace(s.physical, fuel=s.physical.fuel - RETROFIT), 2, False, "ready")
    parts = replace(s.parts, a=s.parts.a - 1, h=s.parts.h - 1, register_units=1)
    assert parts.total() == s.parts.total() and parts.typed_totals() == s.parts.typed_totals()
    assert prediction.physical.energy() + RETROFIT == s.physical.energy()
    return Running(prediction, parts)


EVENTS = (("updater", False), ("updater", True), ("rent", None), ("work", None),
          ("write", None), ("finish", None), ("reverse", None))
CYCLE = (("rent", None), ("work", None), ("write", None), ("finish", None))
WORD = CYCLE * 6 + (("reverse", None),) + CYCLE * 2 + (("updater", True),) + CYCLE * 2


def command(s):
    return False if s.score < 2 else True if s.score > 2 else s.physical.last


def coarse_enabled(s, event):
    kind, _ = event
    p = s.physical
    if kind == "updater":
        return s.phase == "ready" and p.module_lease == 0 and p.fuel >= MODULE_ASSEMBLY
    if kind == "rent":
        return s.phase == "ready" and p.lease > 0 and p.module_lease > 0 and p.fuel >= RENT
    if kind == "work":
        return s.phase == "rented" and p.lease > 0 and p.module_lease > 0 and p.fuel >= WORK and p.packets > 0
    if kind == "write":
        return s.phase == "observed" and p.fuel >= WRITE
    if kind == "finish":
        return s.phase == "written" and p.lease > 0 and p.module_lease > 0
    if kind == "reverse":
        return s.phase == "ready"
    raise ValueError(event)


def coarse_step(s, event):
    assert coarse_enabled(s, event)
    kind, arg = event
    p = s.physical
    if kind == "updater":
        q = replace(p, fuel=p.fuel - MODULE_ASSEMBLY, fast=arg, module_lease=MODULE_LIFETIME)
        t, loss = replace(s, physical=q), MODULE_ASSEMBLY
    elif kind == "rent":
        t, loss = replace(s, physical=replace(p, fuel=p.fuel - RENT), phase="rented"), RENT
    elif kind == "work":
        action = command(s)
        receipt = action == p.regime
        fuel = p.fuel - WORK + (PACKET - RENEWAL if receipt else 0)
        q = replace(p, fuel=fuel, packets=p.packets - 1, last=action)
        t = replace(s, physical=q, receipt=receipt, phase="observed")
        loss = WORK + (RENEWAL if receipt else PACKET)
        decoded = action if receipt else not action
        assert decoded == p.regime  # Restricted noiseless complementary plant.
    elif kind == "write":
        label = p.last if s.receipt else not p.last
        score = (4 if label else 0) if p.fast else (min(4, s.score + 1) if label else max(0, s.score - 1))
        t, loss = replace(s, physical=replace(p, fuel=p.fuel - WRITE), score=score, phase="written"), WRITE
    elif kind == "finish":
        q = replace(p, lease=SELECTOR_LIFETIME if s.receipt else p.lease - 1,
                    module_lease=MODULE_LIFETIME if s.receipt else p.module_lease - 1)
        t, loss = replace(s, physical=q, receipt=False, phase="ready"), 0
    elif kind == "reverse":
        t, loss = replace(s, physical=replace(p, regime=not p.regime)), 0
    else:
        raise ValueError(event)
    assert t.physical.energy() + loss == p.energy()
    assert (t.physical.remainder, t.physical.material) == (p.remainder, p.material)
    assert 0 <= t.score <= 4
    if kind in ("reverse", "updater"):
        assert t.score == s.score and t.physical.last == p.last
    return t, loss


def component_cost(event):
    return int(event[0] == "updater")


def enabled(s, event):
    n = component_cost(event)
    return (s.parts.register_units > 0 and n <= s.parts.a and n <= s.parts.h
            and coarse_enabled(s.prediction, event))


def run_step(s, event):
    assert enabled(s, event)
    prediction, loss = coarse_step(s.prediction, event)
    n = component_cost(event)
    parts = s.parts.bind(n, n)
    assert parts.total() == s.parts.total() and parts.typed_totals() == s.parts.typed_totals()
    assert parts.register_units == s.parts.register_units
    return Running(prediction, parts), loss


def replay(s, events, typed=True, record=False):
    spent, states = 0, [asdict(s)] if record else []
    for index, event in enumerate(events):
        if not (enabled(s, event) if typed else coarse_enabled(s, event)):
            return None, index, s, spent, states
        s, cost = run_step(s, event) if typed else coarse_step(s, event)
        spent += cost
        if record:
            states.append(asdict(s))
    return s, None, s, spent, states


def prepare(a=5, h=6):
    material = a + h
    initial = Prep(0, 0, "empty", False, False, material + 22, 121)
    word = ("formH",) * h + ("formA",) * a + ("associateA", "repair", "capture")
    s, spent, states = initial, 0, [asdict(initial)]
    for event in word:
        s, cost = prep_step(s, event, material)
        spent += cost
        states.append(asdict(s))
    assert s == Prep(a - 1, h, "active", True, True, 20, 120)
    base = handoff(s, material)
    formed, c1 = base_form(base, "module", False)
    formed, c2 = base_form(formed, "selector", True)
    assert c1 + c2 == 3 and formed.physical.fuel == 17
    return initial, s, base, formed, spent, states


def fixture():
    initial, prepared, base, formed, prep_cost, prep_states = prepare()
    ready = retrofit(formed)
    end, blocked, _, operating_cost, states = replay(ready, WORD, record=True)
    assert end is not None and blocked is None
    p, parts = end.prediction.physical, end.parts
    assert (p.fuel, p.packets, p.last, p.lease, p.regime, p.fast, p.module_lease) == (18, 2, False, 6, False, True, 2)
    assert end.prediction.score == 0 and end.prediction.phase == "ready"
    assert (parts.a, parts.h, parts.bound_a, parts.bound_h, parts.register_units, parts.total()) == (0, 0, 3, 5, 1, 11)
    assert (initial.energy(), prep_cost, ADAPTER, 3, RETROFIT, operating_cost, p.energy()) == (154, 13, 1, 3, 3, 96, 38)
    assert initial.energy() == prep_cost + ADAPTER + 3 + RETROFIT + operating_cost + p.energy()
    # Both the replacement and later corrective write retain the acquired score
    # reference; only the write changes its value and hence the next command.
    prior = replay(ready, WORD[:33])[0]
    assert prior is not None and prior.prediction.score == 2 and prior.prediction.physical.module_lease == 0
    replacement, _ = run_step(prior, ("updater", True))
    assert replacement.prediction.score == 2 and replacement.parts.a == replacement.parts.h == 0
    observed = replay(replacement, CYCLE[:2])[0]
    assert observed is not None and command(observed.prediction)
    written, _ = run_step(observed, ("write", None))
    assert not command(written.prediction) and written.prediction.physical.last == observed.prediction.physical.last
    return ready, end, {"initial": asdict(initial), "prepared": asdict(prepared),
                        "adapter_endpoint": asdict(base), "formed": asdict(formed),
                        "retrofit_endpoint": asdict(ready), "final": asdict(end),
                        "initial_energy": 154, "preparation_expenditure": 13,
                        "adapter_expenditure": 1, "base_assembly_expenditure": 3,
                        "retrofit_expenditure": 3, "predictive_expenditure_and_waste": 96,
                        "final_energy": 38, "preparation_states": prep_states,
                        "predictive_states": states}


def finite_retrofits(formed):
    total = admitted = 0
    for a, h, lease, module_lease, seen, fuel in product(range(3), range(3), (0, 1, 6), (0, 1, 2), (False, True), range(6)):
        parts = replace(formed.parts, a=a, h=h)
        physical = replace(formed.physical, lease=lease, module_lease=module_lease, seen=seen,
                           fuel=fuel, material=parts.total())
        s = Base(physical, parts)
        expected = a > 0 and h > 0 and lease > 0 and module_lease > 0 and seen and fuel >= RETROFIT
        assert retrofit_enabled(s) == expected
        if expected:
            r = retrofit(s)
            assert r.parts.register_units == 1 and r.prediction.score == 2
            assert r.prediction.physical.last == physical.last and r.prediction.physical.packets == physical.packets
            admitted += 1
        total += 1
    return {"configurations": total, "admitted": admitted}


def finite_lifts(ready):
    rented = coarse_step(ready.prediction, ("rent", None))[0]
    observed = coarse_step(rented, ("work", None))[0]
    written = coarse_step(observed, ("write", None))[0]
    bases = (ready.prediction, replace(ready.prediction, physical=replace(ready.prediction.physical, fuel=0)),
             replace(ready.prediction, physical=replace(ready.prediction.physical, fuel=4, module_lease=0)),
             rented, observed, written)
    checked = admitted = 0
    for n in range(5):
        for word in product(EVENTS, repeat=n):
            demand = sum(map(component_cost, word))
            for base in bases:
                coarse = replay(base, word, typed=False)[0]
                for a, h, units in product(range(3), range(3), range(2)):
                    parts = replace(ready.parts, a=a, h=h, register_units=units)
                    prediction = replace(base, physical=replace(base.physical, material=parts.total()))
                    s = Running(prediction, parts)
                    actual = replay(s, word)[0]
                    expected = coarse is not None and demand <= a and demand <= h and (not word or units > 0)
                    assert (actual is not None) == expected
                    if actual is not None:
                        assert actual.prediction == replace(coarse, physical=replace(coarse.physical, material=parts.total()))
                        assert (actual.parts.a, actual.parts.h) == (a - demand, h - demand)
                        admitted += 1
                    checked += 1
    prefixes = whole_words = 0
    for a, h in product(range(3), repeat=2):
        parts = replace(ready.parts, a=a, h=h)
        s = replace(ready, prediction=replace(ready.prediction, physical=replace(ready.prediction.physical, material=parts.total())), parts=parts)
        whole_words += replay(s, WORD)[0] is not None
        for n in range(len(WORD) + 1):
            prefix = WORD[:n]
            demand = sum(map(component_cost, prefix))
            assert (replay(s, prefix)[0] is not None) == (demand <= a and demand <= h)
            prefixes += 1
    assert whole_words == 4
    return {"all_words_max_length": 4, "coarse_base_states": len(bases),
            "inventory_and_register_cases_per_word": 18, "cases": checked, "admitted": admitted,
            "full_witness_inventory_pairs": 9, "full_witness_admitted": whole_words,
            "full_witness_prefix_inventory_cases": prefixes}


def complete_graph(ready):
    initial = replace(ready, prediction=replace(ready.prediction, physical=replace(ready.prediction.physical, fuel=15, packets=4)))
    seen, pending, edges, replacements = {initial}, deque([initial]), 0, 0
    while pending:
        s = pending.popleft()
        assert s.parts.total() == 11 and s.parts.typed_totals() == initial.parts.typed_totals()
        assert s.prediction.physical.energy() <= initial.prediction.physical.energy()
        for event in EVENTS:
            changed = replace(s, prediction=replace(s.prediction, physical=replace(s.prediction.physical, regime=not s.prediction.physical.regime)))
            assert enabled(s, event) == enabled(changed, event)
            assert command(s.prediction) == command(changed.prediction)
            if not enabled(s, event):
                continue
            t, _ = run_step(s, event)
            edges += 1
            replacements += event[0] == "updater"
            if t not in seen:
                seen.add(t)
                pending.append(t)
    assert replacements > 0
    return {"initial": asdict(initial), "reachable_states": len(seen),
            "enabled_labelled_edges": edges, "updater_replacement_edges": replacements,
            "exhausted_to_fixed_point": True, "depth_cutoff": None}


def boundaries(ready):
    shortage = []
    for a, h in ((4, 6), (5, 5)):
        initial, _, _, formed, prep_cost, _ = prepare(a, h)
        s = retrofit(formed)
        assert replay(s.prediction, WORD, typed=False)[0] is not None
        end, index, blocked, spent, _ = replay(s, WORD)
        assert end is None and index == 33 and WORD[index] == ("updater", True)
        assert coarse_enabled(blocked.prediction, WORD[index])
        assert (blocked.prediction.physical.fuel, blocked.prediction.physical.packets, blocked.prediction.score) == (22, 4, 2)
        assert initial.energy() == prep_cost + ADAPTER + 3 + RETROFIT + spent + blocked.prediction.physical.energy()
        shortage.append({"initial": asdict(initial), "predictor_entrance": asdict(s), "blocked": asdict(blocked)})
    retrofit_shortage = []
    for a, h in ((3, 6), (5, 4)):
        initial, _, _, formed, _, _ = prepare(a, h)
        assert coarse_retrofit_enabled(formed.physical) and not retrofit_enabled(formed)
        assert formed.physical.fuel == 17 and formed.physical.packets == 12 and formed.physical.material == 9
        retrofit_shortage.append({"initial": asdict(initial), "formed": asdict(formed)})
    # Support cannot be borrowed from future packets to fund a present write.
    low = replace(ready, prediction=replace(ready.prediction, physical=replace(ready.prediction.physical, fuel=4, regime=False)))
    observed = replay(low, CYCLE[:2])[0]
    assert observed is not None and observed.prediction.phase == "observed"
    assert observed.prediction.physical.fuel == 0 and observed.prediction.physical.packets == 11
    assert not enabled(observed, ("write", None)) and observed.prediction.score == ready.prediction.score
    assert not any(enabled(observed, e) for e in EVENTS)
    # In this restricted relation an unaffordable rent blocks; it does not model
    # the separate numerical law's erasure, skipped writes or reconstruction.
    no_rent = replace(ready, prediction=replace(ready.prediction, physical=replace(ready.prediction.physical, fuel=0)))
    assert not enabled(no_rent, ("rent", None)) and no_rent.prediction.score == 2
    absent = replace(ready, parts=replace(ready.parts, register_units=0, bound_a=ready.parts.bound_a + 1, bound_h=ready.parts.bound_h + 1))
    assert absent.parts.total() == ready.parts.total()
    assert coarse_enabled(absent.prediction, ("rent", None)) and not enabled(absent, ("rent", None))
    return {"checks": 7, "actual_replacement_shortage_histories": shortage,
            "actual_retrofit_shortage_histories": retrofit_shortage,
            "unaffordable_write_after_paid_work": asdict(observed),
            "unaffordable_rent_is_blockage_not_erasure": True,
            "coarse_scalar_material_does_not_certify_installed_register": True}


def source_paths():
    return [Path(__file__).resolve(),
            ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
            ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/SelectorRevision.lean",
            ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/formal/UpdaterFormation.lean",
            ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/formal/PredictionAction.lean",
            HERE.parent / "updater/ConstructedUpdater.lean", HERE / "ConstructedPrediction.lean"]


def hashes():
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in source_paths() if p.is_file()}


def main():
    before = hashes()
    ready, _, witness = fixture()
    formed = prepare()[3]
    result = {"scope": "Independent finite checks of the typed deterministic payable-write subprocess; no Python refinement or empirical claim",
              "fixture": witness, "retrofit_grid": finite_retrofits(formed),
              "finite_lift_criterion": finite_lifts(ready),
              "complete_operational_graph": complete_graph(ready), "boundaries": boundaries(ready)}
    after = hashes()
    assert before == after, "Sources changed during the check; retain no mismatched result."
    result["source_hashes"] = after
    result["all_checks_passed"] = True
    (HERE / "model-verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("retrofit_grid", "finite_lift_criterion", "complete_operational_graph")}, indent=2))
    print("Seven boundaries passed. Exact history:154 =13 +1 +3 +3 +96 +38.")


if __name__ == "__main__":
    main()
