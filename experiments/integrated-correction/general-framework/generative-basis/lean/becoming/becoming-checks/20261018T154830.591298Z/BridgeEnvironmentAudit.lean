import Lean
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
import Becoming.ContextArrivalTraces
import Becoming.CouplingHistoryFrames
import Becoming.CourseExtensionFrames
import Becoming.DerivationScopeProcesses
import Becoming.DescentRenewalRuns
import Becoming.FeasibleProfileTraces
import Becoming.RuleRevisionTraces
import Becoming.SupportGatedWebs
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  for m in [`Becoming.Bridge, `Becoming.CompositionBridge, `Becoming.JoiningBridge, `Becoming.GranularityBridge, `Becoming.RepairComparison, `Becoming.Instances, `Becoming.RenewalBridge, `Becoming.CoursesBridge, `Becoming.GuardHorizonProcesses, `Becoming.InstallationTraces, `Becoming.ReconfigurationProcesses, `Becoming.TreeSearchRuns, `Becoming.QueryTraces, `Becoming.DephasingRuns, `Becoming.DrawnAmountProcesses, `Becoming.ProjectedLawTraces, `Becoming.RuleHandoffTraces, `Becoming.ExactRecordRuns, `Becoming.JoiningCodeFrames, `Becoming.JointPhaseTraces, `Becoming.TestCodeFrames, `Becoming.UnitTraces, `Becoming.MoveOutcomeProcesses, `Becoming.RuleNarrowingProcesses, `Becoming.SeedReachProcesses, `Becoming.ExtendedClaimFrames, `Becoming.ExtensionFrames, `Becoming.InterfaceTraces, `Becoming.ReachableFrames, `Becoming.StrictTransportRuns, `Becoming.ContextArrivalTraces, `Becoming.CouplingHistoryFrames, `Becoming.CourseExtensionFrames, `Becoming.DerivationScopeProcesses, `Becoming.DescentRenewalRuns, `Becoming.FeasibleProfileTraces, `Becoming.RuleRevisionTraces, `Becoming.SupportGatedWebs] do
    let some index := env.getModuleIdx? m | throwError m!"no module {m}"
    let mut count := 0
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some index then
        count := count + 1
        let axioms ← liftCoreM <| Lean.collectAxioms n
        if axioms.size > 0 then logInfo m!"AXIOMS {n} {axioms.toList}"
    logInfo m!"CONSTANTS {m} {count}"
