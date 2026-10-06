#!/usr/bin/env python3
"""Independent reconstruction from the frozen event specification.

The reviewer wrote the immutable reference below from PatientConcern.lean and
the agreed event contract before inspecting the producer's function bodies.
Producer functions are called only as the objects compared with this reference.
This is a finite correspondence audit, not arbitrary-code refinement, evidence
of experience, or a proof of the C1/C2 normative contracts.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import copy
import importlib.util
import json
import sys
import heapq
import os
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("noninstrumental_producer", HERE / "model.py")
producer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = producer
spec.loader.exec_module(producer)


@dataclass(frozen=True)
class Person:
    amount: int
    episode: int
    version: int
    route: bool
    permission: bool


@dataclass(frozen=True)
class Record:
    who: str
    episode: int
    version: int
    amount: int
    route: bool


@dataclass(frozen=True)
class Situation:
    persons: tuple[Person, Person]
    stock: int
    formed: bool
    observed: Record | None
    chosen: Record | None
    reward: int
    role: bool
    adoption: bool

    def person(self, who):
        return self.persons[0 if who == "p" else 1]

    def update_person(self, who, person):
        return replace(self, persons=(person, self.persons[1]) if who == "p"
                       else (self.persons[0], person))


def record(s, who):
    p = s.person(who)
    return Record(who, p.episode, p.version, p.amount, p.route)


def valid_record(s, rec):
    return rec is not None and rec == record(s, rec.who)


def actionable_record(s, rec, who=None):
    return (valid_record(s, rec) and rec.amount > 0
            and s.person(rec.who).permission and (who is None or rec.who == who))


def suffix(s, who):
    # A pre-existing paid record/selection shortens the actual remaining path.
    if not s.formed:
        return 6
    if actionable_record(s, s.chosen, who):
        return 2
    if actionable_record(s, s.observed, who):
        return 3
    return 4


def eligible(s, who):
    p = s.person(who)
    return p.amount > 0 and p.permission and s.stock >= suffix(s, who)


def reference_step(s, ev):
    k = ev["kind"]
    if k == "form":
        return replace(s, formed=True, stock=s.stock - 2) if not s.formed and s.stock >= 2 else None
    if k == "read":
        return replace(s, observed=record(s, ev["patient"]), chosen=None, stock=s.stock - 1) if s.formed and s.stock >= 1 else None
    if k == "select":
        return replace(s, chosen=s.observed, stock=s.stock - 1) if s.formed and s.stock >= 1 and actionable_record(s, s.observed) else None
    if k == "act":
        if not (s.formed and s.stock >= 2 and actionable_record(s, s.chosen)
                and ev["command"] == s.chosen.route):
            return None
        who = s.chosen.who
        out = s.update_person(who, replace(s.person(who), amount=0))
        return replace(out, stock=s.stock - 2, chosen=None, observed=None)
    if k == "refuse":
        return replace(s, chosen=None)
    if k in ("reward", "role", "adopt"):
        return replace(s, **{{"reward": "reward", "role": "role", "adopt": "adoption"}[k]: ev["value"]})
    who = ev["patient"]
    p = s.person(who)
    if k == "means":
        p = replace(p, version=p.version + 1, route=ev["command"])
    elif k == "episode":
        p = replace(p, episode=p.episode + 1, amount=ev["burden"])
    elif k == "permission":
        p = replace(p, permission=ev["allowed"])
    else:
        raise ValueError(k)
    return replace(s.update_person(who, p), chosen=None)


def record_json(r):
    return None if r is None else dict(patient=r.who, episode=r.episode,
                                      version=r.version, burden=r.amount, route=r.route)


def encode(s):
    d = dict(fuel=s.stock, carrier=s.formed, evidence=record_json(s.observed),
             selected=record_json(s.chosen), privateReward=s.reward,
             priorRole=s.role, adoptedConcern=s.adoption)
    for who in ("p", "q"):
        p = s.person(who)
        d[who] = dict(burden=p.amount, episode=p.episode, version=p.version,
                      route=p.route, permitted=p.permission)
    return d


def decode(d):
    def packet(r):
        return None if r is None else Record(r["patient"], r["episode"], r["version"], r["burden"], r["route"])
    def person(r):
        return Person(r["burden"], r["episode"], r["version"], r["route"], r["permitted"])
    return Situation(tuple(person(d[who]) for who in ("p", "q")), d["fuel"],
                     d["carrier"], packet(d["evidence"]), packet(d["selected"]),
                     d["privateReward"], d["priorRole"], d["adoptedConcern"])


def reference_case(case):
    s = decode(case["initial"])
    states = [encode(s)]
    failure = None
    for n, ev in enumerate(case["events"]):
        nxt = reference_step(s, ev)
        if nxt is None:
            failure = n
            break
        s = nxt
        states.append(encode(s))
    return dict(states=states, failed_index=failure, final=encode(s),
                eligibility=[{who: eligible(decode(x), who) for who in ("p", "q")} for x in states],
                remaining_costs=[{who: suffix(decode(x), who) for who in ("p", "q")} for x in states])


def events():
    out = [dict(kind=k) for k in ("form", "select", "refuse")]
    out += [dict(kind="act", command=b) for b in (False, True)]
    out += [dict(kind="read", patient=p) for p in ("p", "q")]
    out += [dict(kind="reward", value=n) for n in (0, 7)]
    out += [dict(kind=k, value=b) for k in ("role", "adopt") for b in (False, True)]
    out += [dict(kind="means", patient=p, command=b) for p in ("p", "q") for b in (False, True)]
    out += [dict(kind="permission", patient=p, allowed=b) for p in ("p", "q") for b in (False, True)]
    out += [dict(kind="episode", patient=p, burden=n) for p in ("p", "q") for n in (0, 3)]
    return out


def generated_states():
    # Complete Cartesian product on these declared finite domains, including
    # legal typed states without reachable acquisition provenance.
    worlds = [Person(amount, 0, 0, route, permission)
              for amount, route, permission in product((0, 2), (False, True), (False, True))]
    for p, q, funds, formed in product(worlds, worlds, range(11), (False, True)):
        s = Situation((p, q), funds, formed, None, None, 0, False, False)
        a, b = record(s, "p"), record(s, "q")
        memories = [(None, None), (a, None), (b, None), (a, a), (b, b),
                    (replace(a, version=1), None), (replace(a, amount=a.amount + 1), None),
                    (a, replace(a, route=not a.route)), (b, a), (None, a)]
        for observed, chosen in memories:
            yield replace(s, observed=observed, chosen=chosen)


def compare_step(s, ev):
    before = encode(s)
    passed = copy.deepcopy(before)
    expected = reference_step(s, ev)
    actual = producer.step(passed, copy.deepcopy(ev))
    assert passed == before, ("producer mutated its input", ev)
    assert actual == (None if expected is None else encode(expected)), (before, ev, actual, expected)
    if expected is not None:
        cost = {"form": 2, "read": 1, "select": 1, "act": 2}.get(ev["kind"], 0)
        assert expected.stock == s.stock - cost
        if ev["kind"] == "act":
            who = s.chosen.who
            other = "q" if who == "p" else "p"
            assert expected.person(other) == s.person(other)
            assert expected.person(who) == replace(s.person(who), amount=0)
        if ev["kind"] in ("reward", "role", "adopt"):
            for who in ("p", "q"):
                assert eligible(expected, who) == eligible(s, who)
    return expected


def minimum_service_cost(s, who):
    """Dijkstra over the event relation; does not use the suffix formula."""
    start = replace(s, stock=6)
    agenda, seen, serial = [(0, 0, start)], set(), 0
    menu = [dict(kind=k) for k in ("form", "select", "refuse")]
    menu += [dict(kind="read", patient=p) for p in ("p", "q")]
    menu += [dict(kind="act", command=b) for b in (False, True)]
    while agenda:
        paid, _, here = heapq.heappop(agenda)
        if here in seen:
            continue
        seen.add(here)
        if here.person(who).amount == 0:
            return paid
        for ev in menu:
            there = reference_step(here, ev)
            if there is not None and there not in seen:
                serial += 1
                heapq.heappush(agenda, (6 - there.stock, serial, there))
    return None


def independent_compile():
    """Fresh dependency build, without calling the producer's check.py."""
    compiler = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
    assert compiler.is_file(), "Required existing Lean 4.29.1 compiler is unavailable"
    inputs = [HERE.parent / "lean/GenerativeCore.lean",
              HERE.parent / "lean/conditional/ResourceContinuation.lean",
              HERE / "PatientConcern.lean", HERE / "GroundingContract.lean", HERE / "Cases.lean"]
    results = []
    with tempfile.TemporaryDirectory(prefix="noninstrumental-independent-") as dirname:
        tmp = Path(dirname)
        frozen = {}
        for source in inputs:
            frozen[source.name] = source.read_bytes()
            (tmp / source.name).write_bytes(frozen[source.name])
        env = dict(os.environ, LEAN_PATH=str(tmp))
        for source in inputs:
            result = subprocess.run([str(compiler), "-o", source.with_suffix(".olean").name,
                                     source.name], cwd=tmp, env=env, text=True, capture_output=True)
            output = result.stdout + result.stderr
            assert result.returncode == 0, (source.name, output)
            assert not re.search(r"\b(?:error|warning|sorryAx)\b", output), (source.name, output)
            expected_audits = len(re.findall(rb"^#print axioms ", frozen[source.name], re.M))
            actual_audits = len(re.findall(r"depends on axioms|does not depend on any axioms", output))
            assert actual_audits == expected_audits, (source.name, expected_audits, actual_audits)
            for group in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", output):
                assert set(x.strip() for x in group.split(",") if x.strip()) <= {"propext", "Classical.choice", "Quot.sound"}, (source.name, group)
            results.append(dict(module=source.name, sha256=sha256(frozen[source.name]).hexdigest(),
                                declarations_audited=actual_audits, output=output))
        # The compiled bytes must still be the reviewed bytes after the build.
        for source in inputs:
            assert source.read_bytes() == frozen[source.name], ("source changed during independent build", source.name)
    return dict(compiler=subprocess.check_output([str(compiler), "--version"], text=True).strip(),
                fresh_temporary_build=True, modules=results,
                new_declarations_audited=sum(x["declarations_audited"] for x in results[2:]))


def main():
    cases_path = HERE / "cases.json"
    cases = json.loads(cases_path.read_text())["cases"]
    fixture_fields = 0
    for case in cases:
        rebuilt = reference_case(case)
        for key, value in rebuilt.items():
            assert case[key] == value, (case["name"], key)
            fixture_fields += 1

    es = events()
    state_count = edge_count = allowed_count = 0
    for s in generated_states():
        state_count += 1
        d = encode(s)
        for who in ("p", "q"):
            assert producer.remaining_cost(d, who) == suffix(s, who)
            assert producer.eligible(d, who) == eligible(s, who)
        for ev in es:
            edge_count += 1
            allowed_count += compare_step(s, ev) is not None

    # Valid histories from an actually empty carrier/memory. Environmental
    # episode resets are omitted from this bounded reachability search so a
    # new burden cannot masquerade as a second paid relief or a resource source.
    start = decode(cases[0]["initial"])
    trace_events = [ev for ev in es if ev["kind"] in ("form", "read", "select", "act", "refuse", "permission", "means")]
    frontier, reached = {start}, {start}
    trace_edges = 0
    for depth in range(6):
        upcoming = set()
        for s in frontier:
            if s.chosen is not None:
                assert s.observed == s.chosen
            for ev in trace_events:
                nxt = compare_step(s, ev)
                trace_edges += 1
                if nxt is not None and nxt not in reached:
                    upcoming.add(nxt)
        reached |= upcoming
        frontier = upcoming

    # Packet corruption must not silently pass as valid acquired evidence.
    ready = reference_step(reference_step(start, {"kind": "form"}), {"kind": "read", "patient": "p"})
    original = ready.observed
    alterations = [replace(original, episode=1), replace(original, version=1),
                   replace(original, amount=0), replace(original, amount=4),
                   replace(original, route=not original.route), replace(original, who="q")]
    corruptions = 0
    for bad in alterations:
        assert compare_step(replace(ready, observed=bad), {"kind": "select"}) is None
        assert compare_step(replace(ready, chosen=bad), {"kind": "act", "command": bad.route}) is None
        corruptions += 2

    # A raw constructed selected packet can execute without past acquisition;
    # this is intentionally recorded, not passed off as a provenance theorem.
    forged = replace(start, formed=True, chosen=record(start, "p"), stock=2)
    assert reference_step(forged, {"kind": "act", "command": False}) is not None

    # Independently derive shortest physical continuations instead of comparing
    # two copies of a cost formula. Ghost packets before formation are typed
    # but violate the actual empty-initialization provenance invariant.
    minimum_cases = minimum_matches = 0
    ghost_gap_count = 0
    seen_shapes = set()
    for s in generated_states():
        shape = replace(s, stock=6)
        if shape in seen_shapes:
            continue
        seen_shapes.add(shape)
        for who in ("p", "q"):
            p = s.person(who)
            if not (p.amount > 0 and p.permission):
                continue
            minimum_cases += 1
            actual_min = minimum_service_cost(shape, who)
            if s.formed or (s.observed is None and s.chosen is None):
                assert actual_min == suffix(s, who), (s, who, actual_min, suffix(s, who))
                minimum_matches += 1
            elif actual_min != suffix(s, who):
                ghost_gap_count += 1
    assert ghost_gap_count > 0

    # Unrelated context updates conservatively revoke all selected authority.
    # Factual identity is retained, but its reuse can become unaffordable.
    chosen = reference_step(ready, {"kind": "select"})
    changed_other = compare_step(chosen, {"kind": "permission", "patient": "q", "allowed": False})
    assert eligible(chosen, "p") and not eligible(changed_other, "p")
    assert changed_other.observed == chosen.observed
    assert changed_other.person("p") == chosen.person("p")
    assert suffix(chosen, "p") == 2 and suffix(changed_other, "p") == 3

    compilation = independent_compile()
    report = dict(schema=1, status="passed", scope="finite independent transition reconstruction and fresh Lean build",
                  fixture_count=len(cases), fixture_fields=fixture_fields,
                  cartesian_states=state_count, event_menu=len(es), transition_comparisons=edge_count,
                  allowed_transition_comparisons=allowed_count, reachable_states_depth_6=len(reached),
                  reachable_transition_comparisons=trace_edges, packet_corruptions_rejected=corruptions,
                  arbitrary_current_packet_is_not_acquisition_provenance=True,
                  shortest_service_searches=minimum_cases,
                  shortest_service_equal_on_formation_consistent_states=minimum_matches,
                  typed_preformation_ghost_states_with_cheaper_continuation=ghost_gap_count,
                  unrelated_change_can_revoke_affordable_selection=True,
                  independent_compilation=compilation,
                  sources={p.name: sha256(p.read_bytes()).hexdigest()
                           for p in (HERE / "model.py", cases_path, HERE / "PatientConcern.lean",
                                     HERE / "GroundingContract.lean", Path(__file__))},
                  limitations=["No machine refinement of arbitrary Python histories.",
                               "Current-state equality is a supplied faithful interlock.",
                               "No experiential identification, normative C1/C2 proof, or empirical observation.",
                               "Typed unreachable states test guards but do not gain a paid acquisition history."])
    (HERE / "independent-review.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
