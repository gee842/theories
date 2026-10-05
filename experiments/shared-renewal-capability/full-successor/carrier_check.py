#!/usr/bin/env python3
"""Exact one-step carrier refinement of the 42-channel N=4 CF process.

This is an exhaustive finite material-skeleton check, not CTMC propagation.
Free fuel is symbolic: every propensity is an exact affine polynomial in F.
The reference channels are read from the frozen full-entry producer by AST;
its numerical imports, graph construction and propagation are not executed.
"""
from collections import Counter
from datetime import datetime, timezone
import ast
import hashlib
import importlib.util
from functools import lru_cache
from itertools import permutations, product
import json
from pathlib import Path
import sys
import time
from typing import NamedTuple


HERE = Path(__file__).resolve().parent
REFERENCE = HERE.parent / "full-entry" / "compute.py"
TYPED = HERE.parent / "formal" / "TypedRenewal.lean"
ROOT_MODEL = HERE / "model.py"
sys.dont_write_bytecode = True
SINGLES = ("R", "C", "CF", "Y", "D", "A0", "A1", "G0", "G1", "GF0", "GF1")
BOUND = ("BG0", "BG1", "BY")
ORIGINAL_ROLES = ("A", "C", "G", "Y")
SPECIES = ("R", "C", "CF", "Y", "D", "F", "A0", "A1", "G0", "G1", "GF0", "GF1", "YG0", "YG1")
IX = {s: i for i, s in enumerate(SPECIES)}


class Skeleton(NamedTuple):
    forms: tuple
    partners: tuple


class Transition(NamedTuple):
    channel: str
    target: Skeleton
    fuel_delta: int
    constant: int
    fuel_coefficient: int
    worn_slot: object
    worn_role: object


def signature(form):
    if form in ("A0", "A1"):
        return "A", int(form[-1])
    if form in ("C", "CF"):
        return "C", None
    if form in ("G0", "G1", "GF0", "GF1", "BG0", "BG1"):
        return "G", int(form[-1])
    if form in ("Y", "BY"):
        return "Y", None
    return None, None


def valid(s):
    assert len(s.forms) == len(s.partners) == 4
    for i, (form, mate) in enumerate(zip(s.forms, s.partners)):
        if form in SINGLES:
            assert mate == -1
        else:
            assert form in BOUND and 0 <= mate < 4 and mate != i
            assert s.partners[mate] == i
            assert (form in ("BG0", "BG1") and s.forms[mate] == "BY") or (
                form == "BY" and s.forms[mate] in ("BG0", "BG1"))


def project(s, fuel=0):
    out = [0] * len(SPECIES)
    out[IX["F"]] = fuel
    for form in s.forms:
        if form in SINGLES:
            out[IX[form]] += 1
        elif form in ("BG0", "BG1"):
            out[IX["YG" + form[-1]]] += 1
        else:
            assert form == "BY"
    return tuple(out)


def initial(a, g):
    return Skeleton((f"A{a}", "CF", f"BG{g}", "BY"), (-1, -1, 3, 2))


def mark(mask, worn_slot):
    return mask if worn_slot is None else mask | (1 << worn_slot)


def compatible(s, mask):
    return all(mask & (1 << i) or signature(form)[0] == ORIGINAL_ROLES[i]
               for i, form in enumerate(s.forms))


def skeletons():
    # No G-Y complex.
    for forms in product(SINGLES, repeat=4):
        yield Skeleton(forms, (-1, -1, -1, -1))
    # One directed G-Y complex: choose the G and Y slots, then the gate type.
    for g in range(4):
        for y in range(4):
            if y == g:
                continue
            rest = [i for i in range(4) if i not in (g, y)]
            for typ in (0, 1):
                for other in product(SINGLES, repeat=2):
                    forms = [None] * 4
                    forms[g], forms[y] = f"BG{typ}", "BY"
                    for i, form in zip(rest, other):
                        forms[i] = form
                    mates = [-1] * 4
                    mates[g], mates[y] = y, g
                    yield Skeleton(tuple(forms), tuple(mates))
    # Two complexes: three pairings, two directions and two types per pair.
    for pairing in (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))):
        for directions in product((0, 1), repeat=2):
            for types in product((0, 1), repeat=2):
                forms, mates = [None] * 4, [-1] * 4
                for pair, reverse, typ in zip(pairing, directions, types):
                    g, y = pair[::-1] if reverse else pair
                    forms[g], forms[y] = f"BG{typ}", "BY"
                    mates[g], mates[y] = y, g
                yield Skeleton(tuple(forms), tuple(mates))


def labelled_events(s):
    """Each yielded assignment has rate 1 or F; duplicate targets are retained."""
    sites = {form: [i for i, f in enumerate(s.forms) if f == form]
             for form in SINGLES + BOUND}

    def emit(name, changes=None, df=0, uses_fuel=False, worn=None, split=None, bond=None):
        forms, mates = list(s.forms), list(s.partners)
        if changes:
            for i, form in changes.items():
                forms[i] = form
        if split is not None:
            mate = mates[split]
            assert mate >= 0 and mates[mate] == split
            mates[split] = mates[mate] = -1
        if bond is not None:
            g, y = bond
            assert mates[g] == mates[y] == -1
            mates[g], mates[y] = y, g
        role = None if worn is None else signature(s.forms[worn])[0]
        assert worn is None or role in ORIGINAL_ROLES
        return Transition(name, Skeleton(tuple(forms), tuple(mates)), df,
                          int(not uses_fuel), int(uses_fuel), worn, role)

    for r in sites["R"]:
        yield emit("assembly", {r: "C"})
        for y in sites["Y"]:
            yield emit("free_Y_reproduction", {r: "Y"})
    for c in sites["C"]:
        yield emit("C_wear", {c: "D"}, worn=c)
        yield emit("capture", {c: "CF"})
        for d in sites["D"]:
            yield emit("C_recycling", {d: "R"}, df=-1, uses_fuel=True)
    for y in sites["Y"]:
        yield emit("Y_wear", {y: "D"}, worn=y)
        for d in sites["D"]:
            yield emit("Y_recycling", {d: "R"}, df=-1, uses_fuel=True)
    yield emit("free_leak", df=-1, uses_fuel=True)
    for c in sites["CF"]:
        yield emit("CF_leak", {c: "C"})
        yield emit("CF_wear", {c: "D"}, df=1, worn=c)
        for d in sites["D"]:
            yield emit("paid_recycling", {d: "R", c: "C"})
    for typ in (0, 1):
        a, g, gf, bg, yg = (f"{kind}{typ}" for kind in ("A", "G", "GF", "BG", "YG"))
        for r in sites["R"]:
            yield emit(f"{a}_formation", {r: a}, df=-1, uses_fuel=True)
            for ai in sites[a]:
                yield emit(f"{a}_copying", {r: a}, df=-1, uses_fuel=True)
                yield emit(f"{g}_fabrication", {r: g}, df=-1, uses_fuel=True)
                for c in sites["CF"]:
                    yield emit(f"{g}_paid_fabrication", {r: g, c: "C"})
            for c in sites["CF"]:
                yield emit(f"{a}_paid_formation", {r: a, c: "C"})
        for ai in sites[a]:
            yield emit(f"{a}_wear", {ai: "D"}, worn=ai)
        for gi in sites[g]:
            yield emit(f"{g}_wear", {gi: "D"}, worn=gi)
            yield emit(f"{g}_F_binding", {gi: gf}, df=-1, uses_fuel=True)
            for y in sites["Y"]:
                yield emit(f"{g}_Y_binding", {gi: bg, y: "BY"}, bond=(gi, y))
        for gi in sites[gf]:
            yield emit(f"{gf}_dissociation", {gi: g}, df=1)
            yield emit(f"{gf}_leak", {gi: g})
            yield emit(f"{gf}_wear", {gi: "D"}, df=1, worn=gi)
        for gi in sites[bg]:
            y = s.partners[gi]
            yield emit(f"{yg}_dissociation", {gi: g, y: "Y"}, split=gi)
            yield emit(f"{yg}_G_wear", {gi: "D", y: "Y"}, worn=gi, split=gi)
            yield emit(f"{yg}_Y_wear", {gi: g, y: "D"}, worn=y, split=gi)
            if typ == 1:
                for r in sites["R"]:
                    yield emit("bound_Y_reproduction", {r: "Y"})


def reference_channels():
    """Execute only the reference's channel declarations, without imports/main."""
    tree = ast.parse(REFERENCE.read_text(), filename=str(REFERENCE))
    declarations = [n for n in tree.body if isinstance(n, ast.FunctionDef)
                    and n.name in ("vector", "channels")]
    assert {n.name for n in declarations} == {"vector", "channels"}
    species_node = next(n for n in tree.body if isinstance(n, ast.Assign)
                        and any(isinstance(t, ast.Name) and t.id == "SPECIES" for t in n.targets))
    assert ast.literal_eval(species_node.value) == SPECIES
    weights = tuple(0 if s == "F" else 2 if s.startswith("YG") else 1 for s in SPECIES)
    work = tuple(w - int(s == "D") + int(s in ("F", "CF", "GF0", "GF1"))
                 for s, w in zip(SPECIES, weights))
    namespace = {"SPECIES": SPECIES, "WEIGHTS": weights, "WORK": work}
    exec(compile(ast.Module(body=declarations, type_ignores=[]), str(REFERENCE), "exec"), namespace)
    channels = namespace["channels"]()
    assert len(channels) == 42 and len({row[0] for row in channels}) == 42
    return {name: (inputs, delta) for name, inputs, delta in channels}


def reference_polynomial(inputs, x):
    coefficient, fuel_power = 1, 0
    for i, n in inputs:
        assert n == 1  # Every reactant species appears once in this exact vocabulary.
        if i == IX["F"]:
            fuel_power += 1
        else:
            coefficient *= x[i]
    assert fuel_power <= 1
    return (0, coefficient) if fuel_power else (coefficient, 0)


def root_encoding(s, mask):
    roles, bonds = [], []
    for slot, form in enumerate(s.forms):
        if form in SINGLES:
            roles.append(SINGLES.index(form))
        elif form == "BY":
            roles.append(SINGLES.index("Y"))
        else:
            roles.append(SINGLES.index("G" + form[-1]))
            bonds.append((slot, s.partners[slot]))
    return tuple(roles), tuple(bonds), mask


@lru_cache(None)
def independently_canonical(raw):
    """Minimize an orbit by pulling source slots into dead target positions."""
    roles, bonds, mask = raw
    dead = tuple(i for i in range(4) if mask & (1 << i))
    candidates = []
    for sources in permutations(dead):
        target_roles = list(roles)
        inverse = dict(zip(sources, dead))
        for destination, source in zip(dead, sources):
            target_roles[destination] = roles[source]
        target_bonds = tuple(sorted((inverse.get(g, g), inverse.get(y, y)) for g, y in bonds))
        candidates.append((tuple(target_roles), target_bonds, mask))
    return min(candidates)


def load_root_model():
    spec = importlib.util.spec_from_file_location("carrier_reference_root_model", ROOT_MODEL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert tuple(module.NAMES) == SINGLES
    return module


def main():
    started = time.monotonic()
    reference = reference_channels()
    states = tuple(skeletons())
    assert len(states) == len(set(states)) == 11**4 + 4*3*2*11**2 + 3*4*4 == 17593
    state_set = set(states)
    root_hash = hashlib.sha256(ROOT_MODEL.read_bytes()).hexdigest()
    model = load_root_model()
    counts = Counter()
    seen = set()
    examples = {}
    for mask in range(16):
        for worn in (None, 0, 1, 2, 3):
            after = mark(mask, worn)
            assert after | mask == after
            assert mark(after, worn) == after
            assert (after ^ mask) in (0, 0 if worn is None else 1 << worn)
            counts["mask_algebra_cases"] += 1
    for s in states:
        valid(s)
        x = project(s)
        assert sum((0 if name == "F" else 2 if name.startswith("YG") else 1)*n
                   for name, n in zip(SPECIES, x)) == 4
        masks = tuple(mask for mask in range(16) if compatible(s, mask))
        counts["compatible_skeleton_mask_pairs"] += len(masks)
        actual = {name: [0, 0] for name in reference}
        events = tuple(labelled_events(s))
        for event in events:
            counts["labelled_assignment_cases"] += 1
            seen.add(event.channel)
            assert event.channel in reference and event.target in state_set
            valid(event.target)
            inputs, delta = reference[event.channel]
            projected = project(event.target, event.fuel_delta)
            expected = tuple(a+b for a, b in zip(x, delta))
            assert projected == expected, (s, event, projected, expected)
            assert event.fuel_delta >= 0 or (event.constant == 0 and event.fuel_coefficient > 0)
            actual[event.channel][0] += event.constant
            actual[event.channel][1] += event.fuel_coefficient
            # An unworn active carrier keeps its role and type except at its wear.
            for slot, form in enumerate(s.forms):
                if signature(form)[0] is not None and slot != event.worn_slot:
                    assert signature(event.target.forms[slot]) == signature(form)
            if event.worn_slot is not None:
                assert event.target.forms[event.worn_slot] == "D"
                assert event.worn_role == signature(s.forms[event.worn_slot])[0]
            for mask in masks:
                after = mark(mask, event.worn_slot)
                assert compatible(event.target, after)
                fresh = after & ~mask
                if fresh:
                    assert fresh == 1 << event.worn_slot
                    assert event.worn_role == ORIGINAL_ROLES[event.worn_slot]
                counts["compatible_mask_transition_cases"] += 1
        for name, (inputs, _) in reference.items():
            assert tuple(actual[name]) == reference_polynomial(inputs, x), (s, name, actual[name])
            counts["channel_polynomial_equalities"] += 1
        # Independently compare the root's already-worn-slot quotient on every
        # compatible mask and every material skeleton, not only its reachable graph.
        for mask in masks:
            raw = root_encoding(s, mask)
            canonical = independently_canonical(raw)
            assert model.canonical(*raw) == canonical
            assert model.valid(canonical)
            counted = model.count(canonical, 0)
            assert tuple(counted.get(name, 0) for name in SPECIES) == x
            expected_edges = {}
            for event in events:
                nm = mark(mask, event.worn_slot)
                target = independently_canonical(root_encoding(event.target, nm))
                key = event.channel, target, event.fuel_delta
                coefficients = expected_edges.setdefault(key, [0, 0])
                coefficients[0] += event.constant
                coefficients[1] += event.fuel_coefficient
            actual_edges = {}
            for name, target, df, a, b in model.events(canonical):
                coefficients = actual_edges.setdefault((name, target, df), [0, 0])
                coefficients[0] += a
                coefficients[1] += b
            assert expected_edges == actual_edges, (s, mask, expected_edges, actual_edges)
            counts["root_model_state_comparisons"] += 1
            counts["root_model_edge_coefficient_comparisons"] += len(expected_edges)
    assert seen == set(reference)
    # Bond constituent wear is separate, and initially every role is marked intact.
    for a, g in product((0, 1), repeat=2):
        s = initial(a, g)
        assert compatible(s, 0)
        assert project(s)[IX[f"A{a}"]] == project(s)[IX[f"YG{g}"]] == project(s)[IX["CF"]] == 1
        events = list(labelled_events(s))
        gw = next(e for e in events if e.channel == f"YG{g}_G_wear")
        yw = next(e for e in events if e.channel == f"YG{g}_Y_wear")
        assert mark(0, gw.worn_slot) == 4 and gw.target.forms[3] == "Y"
        assert mark(0, yw.worn_slot) == 8 and yw.target.forms[2] == f"G{g}"
        # Later wear of the same material does not clear a bit or become failure.
        assert mark(15, gw.worn_slot) == mark(15, yw.worn_slot) == 15
    # Two catalysts can yield the same labelled successor: both assignments count.
    s = Skeleton(("A0", "A0", "R", "D"), (-1, -1, -1, -1))
    copies = [e for e in labelled_events(s) if e.channel == "A0_copying"]
    assert len(copies) == 2 and copies[0].target == copies[1].target
    examples["same_target_copying_assignments"] = 2
    examples["same_target_copying_total_propensity"] = "2 F"
    # A recycled original-A material slot can become the other type. Its old
    # identity stays gone, and the new carrier's later wear remains an event.
    s, mask, fuel = initial(0, 0), 0, 0
    path = ("A0_wear", "paid_recycling", "capture", "A1_paid_formation", "capture")
    for name in path:
        chosen = [e for e in labelled_events(s) if e.channel == name]
        assert len(chosen) == 1
        event = chosen[0]
        assert event.constant + event.fuel_coefficient*fuel > 0
        s, mask, fuel = event.target, mark(mask, event.worn_slot), fuel + event.fuel_delta
        assert mask == 1 and fuel >= 0
    assert s.forms[0] == "A1" and s == initial(1, 0)
    later = next(e for e in labelled_events(s) if e.channel == "A1_wear")
    assert mark(mask, later.worn_slot) == 1 and later.target.forms[0] == "D"
    examples["reused_material_type_switch_path"] = list(path)
    examples["original_wear_mask_after_type_switch_and_later_wear"] = 1
    assert hashlib.sha256(ROOT_MODEL.read_bytes()).hexdigest() == root_hash, "Root source changed during check"
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "all_exact_assertions_passed",
        "method": "Exhaustive N=4 material skeletons; exact integer coefficients of affine polynomials in free F; no probability propagation",
        "material_skeletons": len(states), "channel_count": len(reference),
        "counts": dict(sorted(counts.items())), "examples": examples,
        "free_fuel_scope": "Every nonnegative integer F, by coefficient equality; no fuel cap",
        "mask_scope": "All 16 masks checked algebraically; every original-role-compatible skeleton/mask event checked; types preserved before wear",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "reference_source": str(REFERENCE.relative_to(HERE.parent.parent.parent)),
        "reference_source_sha256": hashlib.sha256(REFERENCE.read_bytes()).hexdigest(),
        "typed_source_sha256": hashlib.sha256(TYPED.read_bytes()).hexdigest(),
        "root_model_source_sha256": root_hash,
        "root_model_scope": "Every compatible labelled state checked against independently canonicalized per-channel target and affine rate coefficients; graph construction and probability propagation not run",
        "python_version": sys.version, "elapsed_seconds": time.monotonic()-started,
        "scope_limits": ["Not a Lean proof or Python-to-Lean equivalence theorem", "Root model's one-step quotient checked, but not graph stopping, fuel boundaries, propagation or probability certification", "No probability computation or comparison", "Material slots are declared carrier bookkeeping, not a calibrated molecular atom map"],
    }
    (HERE / "carrier-check.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
