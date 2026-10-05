#!/usr/bin/env python3
"""Independent finite checks of the declared staged component construction.

This file does not import either model implementation or read Lean conclusions.
It separately implements the stated event tables, checks the entire finite
operational graph from the funded fixture, and records input hashes. It is not
a replacement for the quantified Lean proofs or an empirical simulation.
"""

from collections import deque
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
PACKET, ASSEMBLY, TRIAL, RENEWAL, LIFETIME = 4, 1, 2, 1, 2
MATERIAL = 5


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
class Running:
    fuel: int
    packets: int
    mapping: bool
    lease: int
    regime: bool
    a: int
    h: int
    resident: str
    intact: bool
    local: bool
    remainder: int
    bound_a: int = 0
    bound_h: int = 0

    def matter(self):
        return self.a + self.h + int(self.resident != "empty") + self.bound_a + self.bound_h

    def energy(self):
        return self.fuel + PACKET * self.packets + self.remainder + int(self.local)


def prep_step(s, event):
    """Only the preparation events used in the named fixture are implemented."""
    assert s.matter() <= MATERIAL
    if event in ("formA", "formH"):
        assert not s.intact and s.matter() < MATERIAL and s.fuel > 0
        t = replace(s, **({"a": s.a + 1} if event == "formA" else {"h": s.h + 1}),
                    fuel=s.fuel - 1)
        cost = 1
    elif event == "associateA":
        assert s.a > 0 and s.resident == "empty" and s.fuel > 0
        t, cost = replace(s, a=s.a - 1, resident="active", fuel=s.fuel - 1), 1
    elif event == "repair":
        assert s.resident == "active" and not s.intact and s.fuel > 0
        t, cost = replace(s, intact=True, fuel=s.fuel - 1), 1
    elif event == "capture":
        assert s.intact and not s.local and s.source > 0
        t, cost = replace(s, local=True, source=s.source - 1), 0
    elif event == "localCopyA":
        assert s.resident == "active" and s.local and s.matter() < MATERIAL
        t, cost = replace(s, a=s.a + 1, local=False), 1
    else:
        raise ValueError(event)
    assert t.matter() <= MATERIAL and t.energy() + cost == s.energy()
    return t, cost


def handoff(s, regime=False):
    assert s.intact
    packets, remainder = divmod(s.source, PACKET)
    return Running(s.fuel, packets, False, 0, regime, s.a, s.h, s.resident,
                   s.intact, s.local, remainder)


EVENTS = (("assemble", False), ("assemble", True), ("trial", False),
          ("trial", True), ("reverse", None), ("expire", None))


def enabled(s, event):
    kind, arg = event
    if kind == "assemble":
        return s.lease == 0 and s.fuel >= ASSEMBLY and (s.h if arg else s.a) >= 2
    if kind == "trial":
        return s.lease > 0 and s.fuel >= TRIAL and s.packets > 0
    if kind == "reverse":
        return True
    if kind == "expire":
        return s.packets > 0
    raise ValueError(event)


def run_step(s, event):
    assert enabled(s, event)
    kind, arg = event
    if kind == "assemble":
        parts = {"h": s.h - 2, "bound_h": s.bound_h + 2} if arg else {
            "a": s.a - 2, "bound_a": s.bound_a + 2}
        t = replace(s, fuel=s.fuel - ASSEMBLY, mapping=arg, lease=LIFETIME, **parts)
        cost = ASSEMBLY
    elif kind == "trial":
        # The same physical response table is written out independently of the
        # source law's equivalent mapping==regime comparison.
        chosen = bool(arg) ^ s.mapping
        productive = bool(arg) ^ s.regime
        match = chosen == productive
        if match:
            t = replace(s, fuel=s.fuel - TRIAL + PACKET - RENEWAL,
                        packets=s.packets - 1, lease=LIFETIME)
            cost = TRIAL + RENEWAL
        else:
            t = replace(s, fuel=s.fuel - TRIAL, packets=s.packets - 1, lease=s.lease - 1)
            cost = TRIAL + PACKET
    elif kind == "reverse":
        t, cost = replace(s, regime=not s.regime), 0
    elif kind == "expire":
        t, cost = replace(s, packets=s.packets - 1), PACKET
    else:
        raise ValueError(event)
    assert t.energy() + cost == s.energy()
    assert t.matter() == s.matter()
    assert (t.remainder, t.local, t.resident, t.intact) == (
        s.remainder, s.local, s.resident, s.intact)
    assert min(t.fuel, t.packets, t.lease, t.a, t.h, t.bound_a, t.bound_h) >= 0
    if t.mapping != s.mapping:
        assert kind == "assemble"
        assert t.a + t.h + 2 == s.a + s.h
        assert t.bound_a + t.bound_h == s.bound_a + s.bound_h + 2
    for a in EVENTS:
        assert enabled(s, a) == enabled(replace(s, regime=not s.regime), a)
    return t, cost


PREPARATION = ("formH", "formH", "formA", "associateA", "repair", "capture",
               "localCopyA", "capture", "localCopyA")
OPERATION = (("assemble", False), ("trial", False), ("reverse", None),
             ("trial", False), ("trial", True), ("assemble", True), ("trial", True))


def fixture(source=18):
    initial = Prep(0, 0, "empty", False, False, 12, source)
    s, spent = initial, 0
    prep_states = [asdict(s)]
    for event in PREPARATION:
        s, cost = prep_step(s, event)
        spent += cost
        prep_states.append(asdict(s))
    assert s == Prep(2, 2, "active", True, False, 7, source - 2)
    ready = handoff(s)
    assert ready.energy() + spent == initial.energy()
    t, operating_spent = ready, 0
    operating_states = [asdict(t)]
    for event in OPERATION:
        t, cost = run_step(t, event)
        operating_spent += cost
        operating_states.append(asdict(t))
    assert t.fuel == 3 and t.packets == 0 and t.mapping and t.regime and t.lease == 2
    assert t.a == t.h == 0 and t.bound_a == t.bound_h == 2 and t.matter() == 5
    assert spent == 7 and operating_spent == 20
    assert t.energy() + spent + operating_spent == initial.energy()
    return ready, {
        "initial_energy": initial.energy(), "preparation_cost": spent,
        "operating_cost_including_waste": operating_spent,
        "final_energy": t.energy(), "final_state": asdict(t),
        "preparation_states": prep_states, "operating_states": operating_states,
    }


def complete_graph(initial):
    """Full finite reachability, including reversal loops, not a depth cutoff."""
    seen, pending, edges = {initial}, deque([initial]), 0
    max_modules = 0
    while pending:
        s = pending.popleft()
        assert s.energy() <= initial.energy() and s.matter() == initial.matter()
        assert s.bound_a + s.a == initial.a and s.bound_h + s.h == initial.h
        max_modules = max(max_modules, (s.bound_a + s.bound_h) // 2)
        for event in EVENTS:
            if not enabled(s, event):
                continue
            t, _ = run_step(s, event)
            edges += 1
            if t not in seen:
                seen.add(t)
                pending.append(t)
    assert max_modules == 2
    return {"reachable_states": len(seen), "enabled_labelled_edges": edges,
            "maximum_assemblies": max_modules, "exhausted_to_fixed_point": True}


def finite_handoff_checks():
    count = 0
    for a, h, resident, local, fuel, source, regime in product(
            range(3), range(3), ("empty", "active", "alternative"), (False, True),
            range(5), range(12), (False, True)):
        s = Prep(a, h, resident, True, local, fuel, source)
        r = handoff(s, regime)
        assert r.energy() == s.energy() and r.matter() == s.matter()
        assert r.packets * PACKET + r.remainder == source and 0 <= r.remainder < PACKET
        assert r.fuel == fuel and r.regime == regime and not r.mapping
        assert not enabled(r, ("trial", False))
        for event in EVENTS:
            if enabled(r, event):
                run_step(r, event)
        count += 1
    return count


def counterchecks(ready):
    exhausted = handoff(Prep(1, 1, "active", True, False, 0, 0))
    assert not any(enabled(exhausted, e) for e in EVENTS if e[0] != "reverse")
    missing_a = replace(ready, a=0, h=4)
    assert missing_a.matter() == ready.matter() and missing_a.energy() == ready.energy()
    assert not enabled(missing_a, ("assemble", False))
    assert enabled(missing_a, ("assemble", True))
    no_fuel = replace(ready, fuel=0, packets=100)
    assert not enabled(no_fuel, ("assemble", False))
    wrongly_built, _ = run_step(ready, ("assemble", True))
    failed, failed_cost = run_step(wrongly_built, ("trial", False))
    assert failed.lease == 1 and failed.fuel == 4 and failed_cost == 6
    rightly_built, _ = run_step(ready, ("assemble", False))
    succeeded, good_cost = run_step(rightly_built, ("trial", False))
    assert succeeded.lease == 2 and succeeded.fuel == 7 and good_cost == 3
    wrong_first = ready
    for event in (("assemble", True), ("trial", False), ("trial", True), ("assemble", False)):
        wrong_first, _ = run_step(wrong_first, event)
    assert wrong_first.fuel == 1 and wrong_first.packets == 2
    assert wrong_first.mapping == wrong_first.regime and wrong_first.lease == 2
    assert not enabled(wrong_first, ("trial", False)) and not enabled(wrong_first, ("trial", True))
    damaged = Prep(2, 2, "active", False, False, 7, 16)
    try:
        handoff(damaged)
    except AssertionError:
        pass
    else:
        raise AssertionError("Damaged access site incorrectly admitted to handoff")
    return {
        "exhausted_formation_cannot_start_operation": True,
        "equal_matter_and_energy_wrong_part_type_obstructs_assembly": True,
        "source_cannot_replace_upfront_fuel": True,
        "constructible_wrong_mapping_fails_to_renew": True,
        "wrong_first_then_correct_mapping_strands_two_packets": True,
        "damaged_site_blocks_handoff": True,
    }


def threshold_grid():
    """Check all named-word payment prefixes, including spending before capture."""
    count, executable = 0, 0
    for fuel, source in product(range(19), range(24)):
        s = Prep(0, 0, "empty", False, False, fuel, source)
        admitted = True
        try:
            for event in PREPARATION:
                s, _ = prep_step(s, event)
            r = handoff(s)
            for event in OPERATION:
                r, _ = run_step(r, event)
        except AssertionError:
            admitted = False
        assert admitted == (fuel >= 12 and source >= 18)
        count += 1
        executable += admitted
    return {"initial_fuel": [0, 18], "initial_unit_source": [0, 23], "cases": count,
            "executable_cases": executable,
            "criterion_on_checked_grid": "initial fuel >= 12 and unit source >= 18"}


def main():
    ready, main_case = fixture()
    _, remainder_case = fixture(source=19)
    inputs = [HERE / "ConstructedSelector.lean", HERE / "check_model.py",
              ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
              ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/SelectorRevision.lean"]
    out = {
        "scope": "Independent exact finite arithmetic checks of a declared synthetic staged law; no empirical claim.",
        "checks_passed": True,
        "handoff_domain": {"a_h": [0, 2], "fuel": [0, 4], "source": [0, 11],
                            "resident": "all 3 values", "local_and_regime": "both values", "intact": True},
        "handoff_cases": finite_handoff_checks(),
        "main_fixture": main_case,
        "nonzero_remainder_fixture": remainder_case,
        "complete_operational_graph": complete_graph(ready),
        "counterchecks": counterchecks(ready),
        "fixed_word_threshold_grid": threshold_grid(),
        "source_hashes": {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in inputs},
    }
    (HERE / "model-verification.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("checks_passed", "handoff_cases", "complete_operational_graph", "counterchecks")}, indent=2))


if __name__ == "__main__":
    main()
