#!/usr/bin/env python3
"""Independent finite checks of the declared consumable-part updater law.

No Lean conclusions or model implementations are imported. These checks verify
the separately implemented event tables and selected finite domains, not a
chemical realization, stochastic advantage, or the universal Lean theorem.
"""

from collections import deque
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
ASSEMBLY, TRIAL, PACKET, SELECTOR_RENEWAL, SELECTOR_LIFETIME = 1, 2, 6, 1, 2
MODULE_ASSEMBLY, MODULE_RENEWAL, MODULE_LIFETIME, ADAPTER = 2, 1, 4, 1


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
class Core:
    fuel: int
    packets: int
    mapping: bool
    lease: int
    regime: bool
    directed: bool
    module_lease: int
    seen: bool
    remainder: int
    material: int

    def energy(self):
        return self.fuel + PACKET * self.packets + self.remainder


@dataclass(frozen=True)
class Running:
    core: Core
    a: int
    h: int
    resident: str
    intact: bool
    bound_a: int
    bound_h: int
    precursor: int

    def matter(self):
        return self.a + self.h + self.bound_a + self.bound_h + int(self.resident != "empty")

    def total_matter(self):
        return self.matter() + self.precursor


def prep_step(s, event, material):
    """The five preparation event kinds used by the actual witnesses."""
    assert s.matter() <= material
    if event in ("formA", "formH"):
        if s.intact or s.matter() >= material or s.fuel == 0:
            return None
        field = "a" if event == "formA" else "h"
        t, cost = replace(s, **{field: getattr(s, field) + 1}, fuel=s.fuel - 1), 1
    elif event == "associateA":
        if s.a == 0 or s.resident != "empty" or s.fuel == 0:
            return None
        t, cost = replace(s, a=s.a - 1, resident="active", fuel=s.fuel - 1), 1
    elif event == "repair":
        if s.resident != "active" or s.intact or s.fuel == 0:
            return None
        t, cost = replace(s, intact=True, fuel=s.fuel - 1), 1
    elif event == "capture":
        if not s.intact or s.local or s.source == 0:
            return None
        t, cost = replace(s, local=True, source=s.source - 1), 0
    else:
        raise ValueError(event)
    assert t.matter() <= material and t.energy() + cost == s.energy()
    return t, cost


def coarse_bridge_enabled(s, material):
    return (s.matter() <= material and s.intact and s.local and s.fuel >= ADAPTER
            and s.a + int(s.resident == "active") > 0
            and s.h + int(s.resident == "alternative") > 0)


def handoff_enabled(s, material):
    return (s.matter() <= material and s.intact and s.local and s.fuel >= ADAPTER
            and s.a >= 1 and s.h >= 1)


def handoff(s, material, regime=False):
    assert handoff_enabled(s, material)
    packets, remainder = divmod(s.source, PACKET)
    core = Core(s.fuel - ADAPTER + int(s.local), packets, False, 0, regime,
                False, 0, False, remainder, material)
    t = Running(core, s.a - 1, s.h - 1, s.resident, s.intact, 1, 1,
                material - s.matter())
    assert t.core.energy() + ADAPTER == s.energy()
    assert t.matter() == s.matter() and t.total_matter() == material
    assert t.a + t.bound_a == s.a and t.h + t.bound_h == s.h
    return t


EVENTS = (("module", False), ("module", True), ("selector", False),
          ("selector", True), ("trial", False), ("trial", True),
          ("reverse", None), ("expire", None))


def component_cost(event):
    kind, arg = event
    if kind == "module":
        return 1, 1
    if kind == "selector":
        return (0, 2) if arg else (2, 0)
    return 0, 0


def coarse_enabled(s, event):
    kind, arg = event
    if kind == "module":
        return s.module_lease == 0 and s.fuel >= MODULE_ASSEMBLY
    if kind == "selector":
        allowed = not s.directed or not s.seen or arg != s.mapping
        return s.module_lease > 0 and allowed and s.lease == 0 and s.fuel >= ASSEMBLY
    if kind == "trial":
        return s.module_lease > 0 and s.lease > 0 and s.fuel >= TRIAL and s.packets > 0
    if kind == "reverse":
        return True
    if kind == "expire":
        return s.packets > 0
    raise ValueError(event)


def coarse_step(s, event):
    assert coarse_enabled(s, event)
    kind, arg = event
    if kind == "module":
        t = replace(s, fuel=s.fuel - MODULE_ASSEMBLY, directed=arg,
                    module_lease=MODULE_LIFETIME)
        cost = MODULE_ASSEMBLY
    elif kind == "selector":
        t = replace(s, fuel=s.fuel - ASSEMBLY, mapping=arg,
                    lease=SELECTOR_LIFETIME, seen=True)
        cost = ASSEMBLY
    elif kind == "trial":
        response, productive_response = bool(arg) ^ s.mapping, bool(arg) ^ s.regime
        if response == productive_response:
            cost = TRIAL + SELECTOR_RENEWAL + MODULE_RENEWAL
            t = replace(s, fuel=s.fuel - TRIAL + PACKET - SELECTOR_RENEWAL - MODULE_RENEWAL,
                        packets=s.packets - 1, lease=SELECTOR_LIFETIME,
                        module_lease=MODULE_LIFETIME)
        else:
            cost = TRIAL + PACKET
            t = replace(s, fuel=s.fuel - TRIAL, packets=s.packets - 1,
                        lease=s.lease - 1, module_lease=s.module_lease - 1)
    elif kind == "reverse":
        t, cost = replace(s, regime=not s.regime), 0
    elif kind == "expire":
        t, cost = replace(s, packets=s.packets - 1), PACKET
    else:
        raise ValueError(event)
    assert t.energy() + cost == s.energy()
    assert (t.remainder, t.material) == (s.remainder, s.material)
    assert min(t.fuel, t.packets, t.lease, t.module_lease) >= 0
    return t, cost


def enabled(s, event):
    a, h = component_cost(event)
    return coarse_enabled(s.core, event) and a <= s.a and h <= s.h


def run_step(s, event):
    assert enabled(s, event)
    core, cost = coarse_step(s.core, event)
    a, h = component_cost(event)
    t = replace(s, core=core, a=s.a - a, h=s.h - h,
                bound_a=s.bound_a + a, bound_h=s.bound_h + h)
    assert t.total_matter() == s.total_matter()
    assert t.a + t.bound_a == s.a + s.bound_a
    assert t.h + t.bound_h == s.h + s.bound_h
    return t, cost


def replay(s, events, typed=True):
    states, spent = [asdict(s)], 0
    for index, event in enumerate(events):
        if not (enabled(s, event) if typed else coarse_enabled(s, event)):
            return None, index, s, spent, states
        s, cost = run_step(s, event) if typed else coarse_step(s, event)
        spent += cost
        states.append(asdict(s))
    return s, None, s, spent, states


WORD = (("module", False), ("selector", False), ("trial", False), ("trial", True),
        ("trial", False), ("trial", True), ("reverse", None), ("trial", False),
        ("trial", True), ("selector", False), ("trial", False), ("trial", True),
        ("module", True), ("selector", True), ("trial", False))


def prepare(a=8, h=5):
    material = a + h
    initial = Prep(0, 0, "empty", False, False, material + 16, 97)
    events = ("formH",) * h + ("formA",) * a + ("associateA", "repair", "capture")
    s, spent, states = initial, 0, [asdict(initial)]
    for event in events:
        result = prep_step(s, event, material)
        assert result is not None
        s, cost = result
        spent += cost
        states.append(asdict(s))
    assert s == Prep(a - 1, h, "active", True, True, 14, 96)
    return initial, s, handoff(s, material), spent, states


def fixture():
    initial, prepared, ready, prep_cost, prep_states = prepare()
    end, blocked, _, op_cost, run_states = replay(ready, WORD)
    assert blocked is None and end is not None
    assert (end.core.fuel, end.core.packets, end.core.mapping, end.core.regime,
            end.core.lease, end.core.module_lease, end.core.directed) == (9, 7, True, True, 2, 4, True)
    assert (end.a, end.h, end.bound_a, end.bound_h, end.total_matter()) == (0, 0, 7, 5, 13)
    assert (initial.energy(), prep_cost, ADAPTER, op_cost, end.core.energy()) == (126, 15, 1, 59, 51)
    assert initial.energy() == prep_cost + ADAPTER + op_cost + end.core.energy()
    assert sum(component_cost(e)[0] for e in WORD) == 6
    assert sum(component_cost(e)[1] for e in WORD) == 4
    return ready, end, {
        "initial": asdict(initial), "prepared": asdict(prepared), "entrance": asdict(ready),
        "final": asdict(end), "initial_energy": 126, "preparation_expenditure": prep_cost,
        "adapter_expenditure": ADAPTER, "operation_expenditure_and_waste": op_cost,
        "final_energy": end.core.energy(), "operational_component_demand": {"A": 6, "H": 4},
        "preparation_states": prep_states, "operation_states": run_states,
    }


def finite_handoffs():
    checked = rejected = 0
    for a, h, resident, intact, local, fuel, source, extra, regime in product(
            range(3), range(3), ("empty", "active", "alternative"), (False, True),
            (False, True), range(3), range(13), range(2), (False, True)):
        s = Prep(a, h, resident, intact, local, fuel, source)
        material = s.matter() + extra
        if not handoff_enabled(s, material):
            rejected += 1
            continue
        assert coarse_bridge_enabled(s, material)
        r = handoff(s, material, regime)
        assert r.core.packets * PACKET + r.core.remainder == source
        assert r.core.regime == regime and r.core.material == material
        checked += 1
    return {"enabled_handoffs_checked": checked, "disabled_handoffs_checked": rejected}


def finite_lift_criterion(ready):
    """All event words of length <=4, four base states, 16 initial inventories."""
    bases = (ready.core, replace(ready.core, fuel=0, packets=0),
             replace(ready.core, fuel=2, packets=1),
             replace(ready.core, fuel=6, packets=2, directed=True, seen=True,
                     module_lease=4, regime=True))
    checked = admitted = 0
    for length in range(5):
        for word in product(EVENTS, repeat=length):
            need_a = sum(component_cost(e)[0] for e in word)
            need_h = sum(component_cost(e)[1] for e in word)
            for core in bases:
                coarse_end = replay(core, word, typed=False)[0]
                for a, h in product(range(4), repeat=2):
                    s = replace(ready, core=replace(core, material=a + h + 3), a=a, h=h)
                    actual = replay(s, word)[0]
                    expected = coarse_end is not None and need_a <= a and need_h <= h
                    assert (actual is not None) == expected
                    if actual is not None:
                        assert actual.core == replace(coarse_end, material=a + h + 3)
                        assert (actual.a, actual.h) == (a - need_a, h - need_h)
                        admitted += 1
                    checked += 1
    # The longer named witness reaches the second formed updater; its material
    # criterion is checked separately over a grid containing the exact boundary.
    word_cases = word_admitted = prefix_cases = 0
    for a, h in product(range(8), range(6)):
        s = replace(ready, core=replace(ready.core, material=a + h + 3), a=a, h=h)
        end = replay(s, WORD)[0]
        assert (end is not None) == (a >= 6 and h >= 4)
        word_cases += 1
        word_admitted += end is not None
        for n in range(len(WORD) + 1):
            word = WORD[:n]
            ca, ch = map(sum, zip(*(component_cost(e) for e in word))) if word else (0, 0)
            assert (replay(s, word)[0] is not None) == (ca <= a and ch <= h)
            prefix_cases += 1
    return {"all_words_max_length": 4, "base_states": len(bases),
            "inventory_pairs_per_word": 16, "cases": checked, "admitted": admitted,
            "whole_revision_word_stock_pairs": word_cases, "whole_revision_word_admitted": word_admitted,
            "revision_prefix_stock_cases": prefix_cases}


def complete_graph(ready):
    """A full fixed point from a smaller funded state, including reverse loops."""
    initial = replace(ready, core=replace(ready.core, fuel=8, packets=3, material=9), a=3, h=3)
    seen, pending, edges = {initial}, deque([initial]), 0
    while pending:
        s = pending.popleft()
        assert s.core.energy() <= initial.core.energy() and s.total_matter() == 9
        assert s.a + s.bound_a == 4 and s.h + s.bound_h == 4
        for event in EVENTS:
            assert enabled(s, event) == enabled(replace(s, core=replace(s.core, regime=not s.core.regime)), event)
            if not enabled(s, event):
                continue
            t, _ = run_step(s, event)
            edges += 1
            assert t.core == coarse_step(s.core, event)[0]
            if event[0] == "module":
                assert t.bound_a >= 2 and t.bound_h >= 2
            if t not in seen:
                seen.add(t)
                pending.append(t)
    return {"initial_state": asdict(initial), "reachable_states": len(seen),
            "enabled_labelled_edges": edges, "exhausted_to_fixed_point": True,
            "depth_cutoff": None}


def boundaries(ready, end):
    old = Prep(0, 1, "active", True, True, 14, 96)
    assert coarse_bridge_enabled(old, 2) and not handoff_enabled(old, 2)
    no_fuel = replace(ready, core=replace(ready.core, fuel=1))
    assert ready.a >= 1 and ready.h >= 1
    assert not coarse_enabled(no_fuel.core, ("module", False))
    no_a = replace(ready, a=0)
    assert coarse_enabled(no_a.core, ("module", False)) and not enabled(no_a, ("module", False))
    competition = []
    for a, h, expected_index in ((7, 5, 12), (8, 4, 13)):
        initial, prepared, s, prep_cost, _ = prepare(a, h)
        assert replay(s.core, WORD, typed=False)[0] is not None
        typed_end, index, blocked_state, spent, _ = replay(s, WORD)
        assert typed_end is None and index == expected_index
        assert coarse_enabled(blocked_state.core, WORD[index])
        assert initial.energy() == prep_cost + ADAPTER + spent + blocked_state.core.energy()
        competition.append({"initial": asdict(initial), "prepared": asdict(prepared),
                            "entrance": asdict(s), "blocked_event_index_zero_based": index,
                            "blocked_event": WORD[index], "blocked_state": asdict(blocked_state)})
    # Modules alone demand2A2H, selectors alone demand4A2H: each fits5A4H,
    # whereas their joint demand6A4H does not. This is an inventory comparison,
    # not a claim that either isolated construction subword is executable.
    # Competition is sequential: their formation guards are mutually exclusive.
    assert 2 <= 5 and 4 <= 5 and 2 <= 4 and 2 + 4 > 5
    extension = (("reverse", None), ("trial", False), ("trial", True), ("selector", False))
    assert replay(end.core, extension, typed=False)[0] is not None
    typed_end, index, blocked_state, _, _ = replay(end, extension)
    assert typed_end is None and index == 3
    assert (blocked_state.core.fuel, blocked_state.core.packets) == (5, 5)
    assert coarse_enabled(blocked_state.core, extension[index])
    # Updater type causally changes permitted reconstruction, without a hidden
    # regime argument to its assembly guard. Fresh seen=false remains separate.
    u = replace(ready.core, module_lease=4, seen=True, directed=False)
    assert coarse_enabled(u, ("selector", False))
    assert not coarse_enabled(replace(u, directed=True), ("selector", False))
    assert coarse_enabled(replace(u, directed=True), ("selector", True))
    return {"checked": 7, "old_two_material_coarse_bridge_blocked": True,
            "sufficient_parts_insufficient_fuel": True,
            "sufficient_fuel_missing_A": True,
            "actual_preparation_competition_witnesses": competition,
            "coarse_only_extension": {"events": extension, "blocked_state": asdict(blocked_state)},
            "updater_type_changes_reconstruction_guard": True}


def main():
    ready, end, main_fixture = fixture()
    result = {"scope": "Independent finite checks of declared staged consumable-part laws; no empirical claim",
              "fixture": main_fixture, "handoff_grid": finite_handoffs(),
              "finite_trace_lift_criterion": finite_lift_criterion(ready),
              "complete_operational_graph": complete_graph(ready),
              "counterchecks": boundaries(ready, end)}
    paths = [Path(__file__).resolve(),
             ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
             ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/SelectorRevision.lean",
             ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/formal/UpdaterFormation.lean",
             HERE / "ConstructedUpdater.lean"]
    result["source_hashes"] = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                               for p in paths if p.is_file()}
    result["all_checks_passed"] = True
    (HERE / "model-verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("handoff_grid", "finite_trace_lift_criterion", "complete_operational_graph")}, indent=2))
    print("All seven boundary checks passed; exact witness energy126 =15 +1 +59 +51.")


if __name__ == "__main__":
    main()
