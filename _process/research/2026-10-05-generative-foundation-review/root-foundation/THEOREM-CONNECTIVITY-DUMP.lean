import Lean
import Becoming
import Becoming.Bridge
import Becoming.CompositionBridge
import Becoming.JoiningBridge
import Becoming.GranularityBridge
import Becoming.RepairComparison
import Becoming.Instances
import Becoming.RenewalBridge
import Becoming.CoursesBridge
import Becoming.GuardHorizonProcesses
import Becoming.InstallationTraces
import Becoming.ReconfigurationProcesses
import Becoming.TreeSearchRuns
import Becoming.QueryTraces
import Becoming.DephasingRuns
import Becoming.DrawnAmountProcesses
import Becoming.ProjectedLawTraces
import Becoming.RuleHandoffTraces
import Becoming.ExactRecordRuns
import Becoming.JoiningCodeFrames
import Becoming.JointPhaseTraces
import Becoming.TestCodeFrames
import Becoming.UnitTraces
import Becoming.MoveOutcomeProcesses
import Becoming.RuleNarrowingProcesses
import Becoming.SeedReachProcesses
import Becoming.ExtendedClaimFrames
import Becoming.ExtensionFrames
import Becoming.InterfaceTraces
import Becoming.ReachableFrames
import Becoming.StrictTransportRuns
import Becoming.ClassifiedBeliefProcesses
import Becoming.ContextArrivalTraces
import Becoming.CouplingHistoryFrames
import Becoming.CourseExtensionFrames
import Becoming.DerivationScopeProcesses
import Becoming.DescentRenewalRuns
import Becoming.FeasibleProfileTraces
import Becoming.RuleRevisionTraces
import Becoming.SupportGatedWebs
open Lean

/-!
# Theorem-level dependencies of the Becoming spine run

Run by `THEOREM-CONNECTIVITY.py` against the spine's compiled modules restored from the
checker's cache; it reads the environment and declares nothing.

Every constant of every tracked module (the modules of the spine run: foundation, core, bridge
and the inherited modules the bridge imports; that is, every module not rooted at `Init`, `Std`,
`Lean` or `Lake`) is written as one JSON line to the file named by `THEOREM_CONNECTIVITY_OUT`:
its name `n`, module `m`, kind `k`, the tracked constants its type uses `t`, and `v`, the tracked
constants its value uses (for an inductive, its constructors; for a constructor, its inductive).
-/

/-- Modules supplied by the toolchain, not by the run. -/
def toolchainRoots : List Name := [`Init, `Std, `Lean, `Lake]

#eval show CoreM Unit from do
  let env ← getEnv
  let some out ← IO.getEnv "THEOREM_CONNECTIVITY_OUT"
    | throwError "THEOREM_CONNECTIVITY_OUT is not set"
  let mut home : Std.HashMap Name Name := {}
  let mut idxs : Array Nat := #[]
  for i in [0:env.header.moduleNames.size] do
    let m := env.header.moduleNames[i]!
    if !toolchainRoots.contains m.getRoot then
      idxs := idxs.push i
      for n in env.header.moduleData[i]!.constNames do
        home := home.insert n m
  let keep (ns : Array Name) : Array Json :=
    (ns.filter (fun n => home.contains n)).map (fun n => toJson n.toString)
  IO.FS.withFile out .write fun h => do
    for i in idxs do
      let m := env.header.moduleNames[i]!
      for ci in env.header.moduleData[i]!.constants do
        let (kind, val) : String × Array Name := match ci with
          | .thmInfo v => ("thm", v.value.getUsedConstants)
          | .defnInfo v => ("def", v.value.getUsedConstants)
          | .opaqueInfo v => ("opaque", v.value.getUsedConstants)
          | .inductInfo v => ("ind", v.ctors.toArray)
          | .ctorInfo v => ("ctor", #[v.induct])
          | .recInfo _ => ("rec", #[])
          | .axiomInfo _ => ("axiom", #[])
          | .quotInfo _ => ("quot", #[])
        let line := Json.mkObj [("n", toJson ci.name.toString), ("m", toJson m.toString),
          ("k", toJson kind), ("t", Json.arr (keep ci.type.getUsedConstants)),
          ("v", Json.arr (keep val))]
        h.putStrLn line.compress
  IO.println s!"tracked modules {idxs.size}"
