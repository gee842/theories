#!/usr/bin/env python3
"""One checker for the Becoming package: the formal core and its bridge.

The package names modules by path (`Becoming/Frame.lean` is `Becoming.Frame`); other
modules are found by file name under the Lean root. The checker resolves the import
closure, requires every inherited module's current bytes to match a passed receipt,
compiles the closure in dependency order with Lean 4.29.1 and audits the axioms of
every declaration. Inherited reports are recorded, not changed.

The core is pure: its import closure is exactly the foundation and the core modules,
every declaration in that closure has an empty axiom report, and the closure compiles
from Lean's prelude alone (the foundation's `import Std` line is removed for that run).
The bridge imports existing modules to show that their interfaces are the core's;
nothing in the core imports it, and its declarations also have empty axiom reports.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LEAN_ROOT = HERE.parent
sys.path.insert(0, str(LEAN_ROOT / "universal-ethics" / "generative-capacity"))
import check as audit_support  # noqa: E402

# The foundation the core builds on (L0 and its two direct companions).
FOUNDATION = ["GenerativeCore", "InquirySufficiency", "RelationalRenewal"]
# The package, in layer order: the four core layers and their root, then the bridge.
CORE = ["Becoming.Frame", "Becoming.Inquiry", "Becoming.Renewal", "Becoming.Dependence",
        "Becoming.Return", "Becoming.Horizon", "Becoming.Joint", "Becoming.Substitution",
        "Becoming.Metaethics", "Becoming"]
BRIDGE = ["Becoming.Bridge"]
SPINE = CORE + BRIDGE
PURE = FOUNDATION + CORE
RECEIPT = HERE / "becoming-verification.json"
RETAINED = HERE / "becoming-checks"

SCOPE = (
    "Spine: a Frame is the core Process with realized claims; runs, reachability, invariants and new "
    "realization are defined through the core Trace; the visible scope of an inquiry is the set of "
    "configurations its actual executions reach, and a sound policy secures its goal there. "
    "Renewal: a run read through observables of conditions is one relational unfolding; an observable "
    "that never rises from some step on falls only finitely often, with depletion, recurrent renewal "
    "under a natural-number rank and unrenewed drawdown as its cases; in one process from one "
    "configuration one run renews and another consumes. "
    "Dependence: which conditions a formation depends on, at what level, and which it draws on may "
    "change from step to step; constant dependence recovers the static reading exactly; every met "
    "dependence is kept or broken across each step; consumption as inherited admits a requirement "
    "never met, which consumes its condition with no break; where activity needs current support, a "
    "formation still active after a loss without return has weakened or dissolved its dependence, and "
    "with fixed dependence it is no longer active, both contrapositives of that premise; these "
    "outcomes are neither exhaustive nor exclusive, and in one process from one configuration a break "
    "of the same dependence, read at the start of its step, is followed by an ending, a transformation "
    "and a restoration; an event is within renewal when its step keeps every dependence on the "
    "conditions it participates in, breaking when it draws on a condition at a step that breaks a "
    "dependence on it, and undermining when it draws on a condition at a step after which a "
    "dependence on it, met then or before, is unmet; breaking is undermining, and drawing after a "
    "loss can undermine without breaking while it keeps the condition from returning; the stepwise "
    "and whole-run readings credit different events in both directions. "
    "Return: a dependence returns within p steps when it is met at one of the next p; renewal, "
    "renewal within one step, within p, return and non-consumption are ordered, and consumption is "
    "exactly a dependence that never returns; a seasonal condition is renewed within two steps and "
    "not one; a recovery can slow without bound, returning always while no cycle bounds it; over "
    "cycles of two a dip is credited, and an escalation undermines for every cycle. "
    "Horizon: for every horizon two runs of one process agree up to it, drawing beyond renewal with "
    "every event within renewal, and afterwards one renews and the other consumes; a reading decided "
    "by a finite prefix that credits every renewing run credits a consuming one. "
    "Joint activity: withholding a formation's part, the rest as it was, the loss is kept or broken; "
    "when withholding any single part still breaks, no part alone makes the difference; in one "
    "process a drawer's part makes the difference with one other drawer and not with two, while the "
    "relational reading counts it consuming in both; drawing beyond renewal at every step consumes "
    "the condition, the first event undermines for no cycle, and with any single event's draw withheld "
    "the condition is still consumed. "
    "Substitution: in the support-gated law, a focal formation that can substitute an alternative "
    "condition stays active, transforms its dependence at a step that can be found, and consumes, "
    "while the sustaining formation ends; a concrete law meets the premises. "
    "Metaethical core: on a connected whole with some living claim, significance of every living claim "
    "from every standpoint (G0 at claim level) is equivalent to a seed together with relational and "
    "standpoint neutrality; the positioned articulation D follows from the articulation premise A; a "
    "sound inquiry for new living content gives every position with access a contributory reason; "
    "G0, C, D and the secured positive ground are stated in the core, which imports no ethics module. "
    "Each of seed, relational neutrality, standpoint neutrality, connection and A has a consistent "
    "countermodel, and each rival satisfies the same rule inside a formed boundary. The lifting rule L "
    "is transitive only through a live middle response. No premise is proved, no rejecting position is "
    "bound, and no duty, ranking, recognition or compliance is inferred. On a run read relationally, "
    "a condition in which every living formation participates discharges connection, and without one "
    "connection can fail; a consuming formation and one losing its support co-participate in the "
    "drawn condition, so under N_rel valuing the consumer's activity reaches the living events of the "
    "formation losing support. Read stepwise, an event is living when active and not undermining; the "
    "same discharge holds, an event drawing at a step that breaks a dependence is related to the "
    "broken formation, so under N_rel valuing it reaches that formation's living events, and both "
    "readings credit the broken formation's own event. Read through relations, the stepwise reading "
    "of an event is the conjunction of the reading of its relations, and one event can have a living "
    "relation and an undermining one. "
    "Instances: the core's G0, C, D, secured ground and relational living are by definition those of "
    "the existing modules, and J1/J2 on configurations is PracticalJudgment.Better; "
    "seed-edge closures and evaluator chains are reachability on the edge process; a "
    "frame's reachable configurations form a joint-continuation space whose bundles step-preserving "
    "maps carry and lifting summaries reflect; robust responses, guarantees, live steps and evidence "
    "narrowing by a rule list are common responses, one-step completion, enabledness and After on a "
    "pure observation; the functional articulation of a situation is exactly the deterministic case "
    "of the articulation under L, and the lifted comparison, reason, survival and continual-improvement "
    "results hold on every frame. A countermodel shows that L is substantive: a response with one "
    "better and one worse outcome is comparable in neither direction."
)


# Directories holding retained runs, frozen copies and development attempts.
ARCHIVE = re.compile(r"(-checks|-runs|-history|-development|verification.*)$"
                     r"|^(checks|runs|sources|revalidation|retained.*|history|archive.*)$")


def module_index():
    index = {}
    for path in LEAN_ROOT.rglob("*.lean"):
        if any(ARCHIVE.search(part) for part in path.relative_to(LEAN_ROOT).parts[:-1]):
            continue
        name = ".".join(path.relative_to(HERE).with_suffix("").parts) if HERE in path.parents else path.stem
        index.setdefault(name, []).append(path)
    return index


def source_file(name):
    """Where a module sits in the compile directory: `Becoming.Frame` → `Becoming/Frame.lean`."""
    return name.replace(".", "/") + ".lean"


def imports_of(data):
    code = audit_support.code_only(data.decode())
    return [m.strip() for m in re.findall(r"^import\s+(.+)$", code, re.M) if m.strip() != "Std"]


def closure(index, roots=SPINE):
    order, seen = [], set()

    def visit(name, stack):
        assert name not in stack, ("import cycle", stack + [name])
        if name in seen:
            return
        paths = index.get(name, [])
        assert len(paths) == 1, (name, [str(p) for p in paths])
        for dependency in imports_of(paths[0].read_bytes()):
            visit(dependency, stack + [name])
        seen.add(name)
        order.append(name)

    for name in roots:
        visit(name, [])
    return order


def passed_receipts():
    receipts = []
    for path in LEAN_ROOT.rglob("*.json"):
        if path == RECEIPT or RETAINED in path.parents:
            continue
        relative = path.relative_to(LEAN_ROOT)
        text = path.read_text(errors="replace")
        if '"passed"' in text:
            receipts.append((str(relative), text))
    return receipts


def declarations(data):
    # A root module only imports and documents; it declares nothing.
    if not re.sub(r"^import .+$", "", audit_support.code_only(data.decode()), flags=re.M).strip():
        return []
    # The inherited scanner accepts only Std/GenerativeCore imports; it reads a copy
    # with imports replaced. Compilation uses the unchanged bytes.
    return audit_support.declarations(re.sub(r"^import .+$", "import Std", data.decode(), flags=re.M))


CONTROLS = """import Becoming.Bridge
open Becoming Generative Generative.InquirySufficiency

-- The full premise set is consistent: the model satisfies seed, both neutralities and connection.
example : (Model.valuation Model.linked (fun _ _ => True)).Grounds :=
  ((Model.valuation Model.linked (fun _ _ => True)).significant_iff
    (Model.linked_connected _) .evaluator (c₀ := .self) trivial).mp (fun _ _ _ => trivial)

-- The headline theorem has a nonvacuous instance: one step forms a new living claim.
def grow : Frame Bool Unit Unit := ⟨⟨fun s _ t => s = false ∧ t = true⟩, fun s _ => s = true⟩
def everyone : Valuation Model.Who Unit :=
  ⟨fun _ => True, fun _ _ => True, fun _ _ => True, fun _ _ => True⟩
def zero : Fin 2 := ⟨0, Nat.zero_lt_succ 1⟩
def sense0 : Bool → Unit → Bool → Fin 2 := fun _ _ _ => zero
def respondOnce : Unit → List Unit := fun _ => [()]
def believed : Bool → Prop := fun s => s = false
def access : Model.Who → Policy Unit Unit 2 → Prop := fun _ _ => True
def nothingBefore : Bool → Unit → Prop := fun _ _ => False

/-- The least reason satisfying A. -/
def routeReason (p : Model.Who) (r : Policy Unit Unit 2) : Prop :=
  access p r ∧ SecuresPositiveGround (Scope grow.P sense0 respondOnce believed) nothingBefore
    (fun _ c => everyone.sig p c) r

theorem grow_sound :
    Sound grow.P (fun _ _ _ => True) (Novel grow everyone.living nothingBefore)
      sense0 respondOnce (.respond ()) believed :=
  ⟨⟨false, rfl⟩, fun s held => by
    cases held
    exact ⟨⟨true, rfl, rfl⟩, fun t step => ⟨trivial, by
      cases step.2
      exact ⟨(), trivial, rfl, id⟩⟩⟩⟩

theorem grow_reason : ∀ p, access p (.respond ()) → routeReason p (.respond ()) :=
  universal_reason grow everyone nothingBefore access routeReason
    ⟨⟨.evaluator, (), trivial, trivial⟩, fun ⟨_, _, _⟩ _ _ _ => trivial,
      fun ⟨_, _, _⟩ _ _ => trivial⟩
    (fun _ _ _ _ => Reach.refl _ _)
    (fun ⟨_, _⟩ available secured => ⟨available, secured⟩)
    (.respond ()) grow_sound

-- The continuation instance is nonvacuous: a reached configuration realizes the living claim.
example : JointContinuationClassification.Jointly (grow.continuations false) (fun _ => True) :=
  ⟨true, Reach.of_step (a := ()) ⟨rfl, rfl⟩, fun _ _ => rfl⟩

-- The common-condition discharge is nonvacuous: in the commons, every formation participates.
example : (Commons.conditions.valuation Commons.sharing (fun (_ : Unit) _ => True)
    (fun _ _ => True)).Connected :=
  Commons.conditions.connected_of_common Commons.sharing _ _ ()
    (fun e _ => match e with
      | (.focal, _) => Or.inr trivial
      | (.sustaining, _) => Or.inl trivial)

-- The stepwise discharge is nonvacuous: its first event is living in the escalating run.
example : ((Commons.conditions.dependence.along Commons.escalating).valuation
    (fun (_ : Unit) _ => True) (fun _ _ => True)).Connected ∧
    ((Commons.conditions.dependence.along Commons.escalating).valuation
      (fun (_ : Unit) _ => True) (fun _ _ => True)).living (.focal, 0) :=
  ⟨Web.connected_of_common _ _ _ ()
    (fun e _ => match e with
      | (.focal, _) => Or.inr trivial
      | (.sustaining, _) => Or.inl trivial),
   ⟨trivial, Commons.stepwise_credits_before_escalation.2.1.not_undermining⟩⟩
"""


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = RETAINED / stamp
    retained.mkdir(parents=True, exist_ok=False)
    index = module_index()
    order = closure(index)
    core_closure = closure(index, CORE)
    paths = {name: index[name][0] for name in order}
    sources = {name: paths[name].read_bytes() for name in order}
    helpers = {p.name: p.read_bytes() for p in [Path(__file__), LEAN_ROOT / "universal-ethics" / "generative-capacity" / "check.py"]}
    for name, data in helpers.items():
        (retained / name).write_bytes(data)
    for name, data in sources.items():
        (retained / (name + ".lean")).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": audit_support.TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "spine_modules": SPINE,
        "core_modules": CORE, "foundation_modules": FOUNDATION, "bridge_modules": BRIDGE,
        "core_closure": core_closure,
        "compile_order": order,
        "source_paths": {name: str(paths[name].relative_to(LEAN_ROOT)) for name in order},
        "source_sha256": {name: audit_support.digest(data) for name, data in sources.items()},
        "checker_sha256": {name: audit_support.digest(data) for name, data in helpers.items()},
        "scope": SCOPE,
    }
    try:
        assert sorted(core_closure) == sorted(PURE), ("core imports outside the core", core_closure)
        inherited = [name for name in order if name not in SPINE]
        receipts = passed_receipts()
        matches = {}
        for name in inherited:
            found = sorted(path for path, text in receipts if receipt["source_sha256"][name] in text)
            assert found, ("inherited module has no passed receipt for its current bytes", name)
            matches[name] = found
        receipt["inherited_receipts"] = matches
        registry = {name: declarations(data) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="becoming-spine-lean-") as scratch:
            work = Path(scratch)

            def run(args, log, where=work):
                env = {**os.environ, "LEAN_PATH": str(where)}
                p = subprocess.run(command + args, cwd=where, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, p.stdout
                assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
                return p.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            for name, data in sources.items():
                target = work / source_file(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            for name in order:
                flat = name.replace(".", "")
                run(["-o", source_file(name)[:-5] + ".olean", source_file(name)], name + ".log")
                audit = "import " + name + "\n" + "\n".join(
                    "#print axioms " + item["name"] for item in registry[name]) + "\n"
                (work / (flat + "AxiomAudit.lean")).write_text(audit)
                (retained / (flat + "AxiomAudit.lean")).write_text(audit)
                output = run([flat + "AxiomAudit.lean"], flat + "AxiomAudit.log")
                dependencies = {}
                for item in registry[name]:
                    full = item["name"]
                    if "'" + full + "' does not depend on any axioms" in output:
                        axioms = []
                    else:
                        match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                        assert match, (full, output)
                        axioms = [a.strip() for a in match[1].split(",") if a.strip()]
                    assert set(axioms) <= {"propext", "Quot.sound", "Classical.choice"}, (full, axioms)
                    assert name not in SPINE + PURE or not axioms, (full, axioms)
                    dependencies[full] = axioms
                if name in SPINE:
                    signatures = "import " + name + "\n" + "\n".join(
                        "#check @" + item["name"] for item in registry[name] if item["kind"] == "theorem") + "\n"
                    (work / (flat + "Signatures.lean")).write_text(signatures)
                    (retained / (flat + "Signatures.lean")).write_text(signatures)
                    run([flat + "Signatures.lean"], flat + "Signatures.log")
                records.append({
                    "module": name, "spine": name in SPINE,
                    "layer": ("foundation" if name in FOUNDATION else "core" if name in CORE
                              else "bridge" if name in BRIDGE else "inherited"),
                    "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                    "declarations": registry[name], "axiom_dependencies": dependencies,
                    "kernel_checked": True,
                })
            (work / "Controls.lean").write_text(CONTROLS)
            (retained / "Controls.lean").write_text(CONTROLS)
            run(["Controls.lean"], "Controls.log")
            # The core needs nothing beyond Lean's prelude.
            bare = work / "prelude-only"
            bare.mkdir()
            for name in core_closure:
                target = bare / source_file(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(re.sub(r"^import Std\n", "", sources[name].decode(), flags=re.M))
                run(["-o", source_file(name)[:-5] + ".olean", source_file(name)], name + ".PreludeOnly.log", bare)
            receipt["core_compiles_from_prelude"] = True
            receipt["checked_application_examples"] = [
                {"claim": "the full premise set has a model", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "universal_reason has a nonvacuous instance on a one-step frame", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "a frame's continuation space has a reached configuration realizing a living claim", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "a run with a common condition is connected under the relational reading", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "the stepwise reading is connected by a common condition and credits a living event", "kernel_checked": True, "counted_as_new_theorem": False},
            ]
        receipt["source_unchanged_during_check"] = all(
            paths[name].read_bytes() == data for name, data in sources.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        assert all((retained / name).read_bytes() == data for name, data in helpers.items())
        receipt["modules"] = records
        receipt["artifact_sha256"] = {
            p.name: audit_support.digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()
        }
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        serialized = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
        (retained / "verification.json").write_text(serialized)
        RECEIPT.write_text(serialized)
    spine = [r for r in records if r["spine"]]
    print(json.dumps({
        "status": receipt["status"],
        "core_closure": core_closure,
        "core_axioms": sorted({a for r in records if r["layer"] in ("foundation", "core")
                               for aa in r["axiom_dependencies"].values() for a in aa}),
        "spine_theorems": {r["module"]: r["theorems"] for r in spine},
        "spine_declaration_audits": sum(len(r["declarations"]) for r in spine),
        "inherited_modules": len(records) - len(spine),
        "inherited_axioms": sorted({a for r in records if not r["spine"]
                                    for aa in r["axiom_dependencies"].values() for a in aa}),
        "receipt": str(RECEIPT),
    }))


if __name__ == "__main__":
    main()
