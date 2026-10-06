#!/usr/bin/env python3
"""Independent frozen build and finite compiled replay for the nondual extension.

The Python oracle uses sets to identify distinct active nonself predecessors;
Lean computes the declared list-based law. These finite checks are not a general
refinement theorem, an experience assay, or a proof of a nondual ontology.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
BASIS = HERE.parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"
EDGE_MENU = [(0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (3, 3), (4, 4)]
PROBE = r'''import NondualFormation
open NondualCore.Signals

def probeEdges : List (Nat × Nat) :=
  [(0,3),(1,3),(1,4),(2,4),(3,4),(3,3),(4,4)]
def picked (mask bit : Nat) : Bool := (mask / (2 ^ bit)) % 2 == 1
def probeNet (graph activity : Nat) : Net :=
  { edges := ((List.range 7).filter (picked graph)).map (fun i => probeEdges[i]!)
    active := (List.range 5).filter (picked activity) }
def bit (b : Bool) : String := if b then "1" else "0"
def encoded (s : Net) : String :=
  String.intercalate "," (s.edges.map (fun e => toString e.1 ++ ":" ++ toString e.2))
    ++ "|" ++ String.intercalate "," (s.active.map toString)
#eval IO.println ("matrix=" ++ String.intercalate "" ((List.range 128).flatMap
  (fun graph => (List.range 32).flatMap (fun activity =>
    [bit (canPulse (probeNet graph activity) 3), bit (canPulse (probeNet graph activity) 4)]))))
#eval IO.println ("origin=" ++ encoded origin)
#eval IO.println ("formed=" ++ encoded formed)
#eval IO.println ("responded=" ++ encoded responded)
#eval IO.println ("dissolved=" ++ encoded dissolved)
#eval IO.println ("rewired=" ++ encoded rewired)
#eval IO.println ("reresponded=" ++ encoded reresponded)
#eval IO.println ("duplicate=" ++ bit (canPulse ⟨[(0,3),(0,3)], [0]⟩ 3))
#eval IO.println ("self_plus_one=" ++ bit (canPulse ⟨[(3,3),(0,3)], [0,3]⟩ 3))
#eval IO.println ("duplicate_plus_other=" ++ bit (canPulse ⟨[(0,3),(0,3),(1,3)], [0,1]⟩ 3))
'''


def digest(data):
    return sha256(data).hexdigest()


def execute(command, cwd, env):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def support(net, target):
    edges, active = net
    return {source for source, destination in edges
            if destination == target and source != target and source in set(active)}


def enabled(net, target):
    return len(support(net, target)) >= 2


def replay(net, events):
    edges, active = list(net[0]), list(net[1])
    for kind, *args in events:
        if kind == "link":
            edges.append(tuple(args))
        elif kind == "cut":
            edges = [edge for edge in edges if edge != tuple(args)]
        else:
            assert kind == "pulse"
            target = args[0]
            assert enabled((edges, active), target), (edges, active, target)
            active = ([n for n in active if n != target] if target in active
                      else [target] + active)
    return edges, active


def encode(net):
    return ",".join(str(a) + ":" + str(b) for a, b in net[0]) + "|" + ",".join(map(str, net[1]))


def independent_expectations():
    matrix = []
    histogram = {"neither": 0, "only_3": 0, "only_4": 0, "both": 0}
    for graph in range(128):
        edges = [edge for i, edge in enumerate(EDGE_MENU) if graph & (1 << i)]
        for activity in range(32):
            active = [n for n in range(5) if activity & (1 << n)]
            flags = [enabled((edges, active), target) for target in (3, 4)]
            matrix.extend("1" if flag else "0" for flag in flags)
            histogram[["neither", "only_4", "only_3", "both"][2 * flags[0] + flags[1]]] += 1
    origin = ([], [0, 1, 2])
    formation = [("link", 0, 3), ("link", 1, 3), ("link", 1, 4), ("link", 2, 4)]
    response = [("pulse", 3), ("pulse", 4)]
    dissolution = [("cut", 0, 3), ("cut", 1, 3), ("cut", 1, 4), ("cut", 2, 4)]
    rewiring = [("link", 3, 4), ("cut", 2, 4)]
    formed = replay(origin, formation)
    responded = replay(formed, response)
    dissolved = replay(responded, dissolution)
    rewired = replay(responded, rewiring)
    reresponded = replay(rewired, [("pulse", 4)])
    assert replay(origin, formation + response + dissolution) == dissolved
    assert replay(origin, formation + response + rewiring + [("pulse", 4)]) == reresponded
    assert support(formed, 3) == {0, 1} and support(formed, 4) == {1, 2}
    assert support(formed, 3) & support(formed, 4) == {1}
    assert responded[1] == dissolved[1]
    assert all(enabled(responded, n) and not enabled(dissolved, n) for n in (3, 4))
    assert support(rewired, 4) == {1, 3}
    assert 3 not in support(formed, 4) and 3 in support(rewired, 4)
    assert not enabled(replay(rewired, [("cut", 3, 4)]), 4)
    assert not enabled((rewired[0], [n for n in rewired[1] if n != 3]), 4)
    assert 4 in rewired[1] and 4 not in reresponded[1]
    for edge in ((0, 3), (1, 3), (1, 4), (2, 4)):
        assert not enabled(replay(formed, [("cut", *edge)]), edge[1])
    cases = {"origin": origin, "formed": formed, "responded": responded,
             "dissolved": dissolved, "rewired": rewired, "reresponded": reresponded}
    expected = {name: encode(net) for name, net in cases.items()}
    expected.update(matrix="".join(matrix), duplicate="0", self_plus_one="0",
                    duplicate_plus_other="1")
    return expected, dict(finite_graphs=128, activity_masks=32, states=4096,
                          capacity_queries=8192, query_targets=[3, 4],
                          candidate_edges=EDGE_MENU, capacity_histogram=histogram,
                          exact_replayed_states=len(cases),
                          role_change_and_ablation_checks=True,
                          duplicate_and_self_edge_checks=3,
                          scope="All seven-edge and five-activity masks in this declared finite slice; not all unbounded Nat-node networks.")


def main():
    public_receipt_bytes = (HERE / "nondual-model-verification.json").read_bytes()
    public_receipt = json.loads(public_receipt_bytes)
    public_sources = [BASIS / item["source"] for item in public_receipt["modules"]]
    assert public_sources[-1].name == "GenerativeNondualModel.lean"
    # Check this supplied inventory against the actual source-level import
    # closure rather than relying on the prior receipt's pass status.
    public_seen = {"Std"}
    for path in public_sources:
        imported = re.findall(r"^import\s+(\w+)\s*$", path.read_text(), re.M)
        assert all(name in public_seen for name in imported), (path, imported, public_seen)
        assert not any(name in {"GroundingContract", "PatientConcern", "RootGrounding",
                                "NondualConcernAdapter"} for name in imported)
        public_seen.add(path.stem)
    sources = public_sources + [BASIS / "lean/conditional/ResourceContinuation.lean",
                                HERE / "PatientConcern.lean", HERE / "GroundingContract.lean",
                                HERE / "NondualFormation.lean", HERE / "NondualConcernAdapter.lean"]
    frozen = {p: p.read_bytes() for p in sources}
    old_names = ["verification.json", "root-verification.json", "root-independent-review.json",
                 "check.py", "check_root.py", "Cases.lean"]
    preserved = {name: (HERE / name).read_bytes() for name in old_names}
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    version = execute(["lean", "+" + TOOLCHAIN, "--version"], HERE, env)
    assert version.returncode == 0 and "version 4.29.1," in version.stdout
    logs = HERE / "nondual-independent-logs"
    logs.mkdir(exist_ok=True)
    modules = []
    allowed = {"propext", "Quot.sound", "Classical.choice"}
    with tempfile.TemporaryDirectory(prefix="nondual-independent-") as name:
        build = Path(name)
        for path, data in frozen.items():
            assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", data.decode())
            assert not re.search(r"^\s*(axiom|constant)\s", data.decode(), re.M)
            (build / path.name).write_bytes(data)
        build_env = dict(env, LEAN_PATH=str(build))
        for path in sources:
            result = execute(["lean", "+" + TOOLCHAIN, "-o", path.stem + ".olean", path.name], build, build_env)
            log = logs / (path.stem + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", result.stdout)
            expected = len(re.findall(r"^#print axioms ", frozen[path].decode(), re.M))
            axiom_set = {x.strip() for _, xs in audits for x in xs.split(",") if x.strip()}
            clean = (result.returncode == 0 and "warning:" not in result.stdout
                     and "sorryAx" not in result.stdout and len(audits) == expected
                     and expected > 0 and axiom_set <= allowed)
            modules.append(dict(module=path.stem, source=str(path.relative_to(BASIS)),
                                source_sha256=digest(frozen[path]), dependency_audits=len(audits),
                                axioms=sorted(axiom_set), clean=clean,
                                log=str(log.relative_to(HERE)), log_sha256=digest(log.read_bytes())))
            if not clean:
                print(result.stdout)
                raise RuntimeError("Independent build failed: " + path.name)
        (build / "IndependentNondualProbe.lean").write_text(PROBE)
        (logs / "IndependentNondualProbe.lean").write_text(PROBE)
        result = execute(["lean", "+" + TOOLCHAIN, "IndependentNondualProbe.lean"], build, build_env)
        (logs / "IndependentNondualProbe.txt").write_text(result.stdout)
        assert result.returncode == 0 and "error:" not in result.stdout, result.stdout
        observed = dict(line.split("=", 1) for line in result.stdout.strip().splitlines())
        expected, finite = independent_expectations()
        assert observed == expected, {key: (observed.get(key), value) for key, value in expected.items()
                                      if observed.get(key) != value}
    assert all(p.read_bytes() == data for p, data in frozen.items())
    assert all((HERE / name).read_bytes() == data for name, data in preserved.items())
    assert (HERE / "nondual-model-verification.json").read_bytes() == public_receipt_bytes
    new_names = {"NondualCore", "NondualFormation", "NondualConcernAdapter", "GenerativeNondualModel"}
    record = dict(status="passed", checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  independent_frozen_temporary_build=True, toolchain=TOOLCHAIN,
                  lean_version=version.stdout.strip(), sources_unchanged=True,
                  old_records_unchanged=True,
                  public_entry_independently_compiled=True,
                  public_import_closure_role_free=True,
                  public_receipt_sha256=digest(public_receipt_bytes),
                  preserved_sha256={name: digest(data) for name, data in preserved.items()},
                  checker_sha256=digest(Path(__file__).read_bytes()), modules=modules,
                  new_dependency_audits=sum(m["dependency_audits"] for m in modules if m["module"] in new_names),
                  finite_compiled_comparison=finite,
                  probe_source_sha256=digest(PROBE.encode()),
                  probe_output_sha256=digest((logs / "IndependentNondualProbe.txt").read_bytes()),
                  scope="Role-free description and supplied signal-connection formation; independently compiled finite capacity and endpoint replay. No biological organization, consciousness, ethical truth, or assumption-free ontology is inferred.")
    (HERE / "nondual-independent-review.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in ("status", "new_dependency_audits", "finite_compiled_comparison")}, indent=2))


if __name__ == "__main__":
    main()
