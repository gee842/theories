import Lean
import GenerativeCore
import Becoming.Frame
import InquirySufficiency
import Becoming.Inquiry
import Becoming.Recurrence
import RelationalRenewal
import Becoming.Renewal
import Becoming.Dependence
import Becoming.Return
import Becoming.Horizon
import Becoming.Joint
import Becoming.Experiment
import Becoming.Substitution
import Becoming.Generation
import Becoming.Flow
import Becoming.Change
import Becoming.Population
import Becoming.Identity
import Becoming.Wholes
import Becoming.Dissipation
import Becoming.Locality
import Becoming.Roles
import Becoming.Reserve
import Becoming.Evolution
import Becoming.Space
import Becoming.Premises
import Becoming.Openness
import Becoming.Counting
import Becoming.Standing
import Becoming.Resolution
import Becoming.Entropy
import Becoming.Continuation
import Becoming.Admission
import Becoming.Regions
import Becoming.Metaethics
import Becoming.Ranking
import Becoming.Correspondence
import Becoming.Descent
import Becoming.Standpoints
import Becoming.Significance
import Becoming.Interdependence
import Becoming.Feedback
import Becoming.Testing
import Becoming.Runaway
import Becoming.Boundaries
import Becoming.Relevance
import Becoming
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  for m in [`GenerativeCore, `Becoming.Frame, `InquirySufficiency, `Becoming.Inquiry, `Becoming.Recurrence, `RelationalRenewal, `Becoming.Renewal, `Becoming.Dependence, `Becoming.Return, `Becoming.Horizon, `Becoming.Joint, `Becoming.Experiment, `Becoming.Substitution, `Becoming.Generation, `Becoming.Flow, `Becoming.Change, `Becoming.Population, `Becoming.Identity, `Becoming.Wholes, `Becoming.Dissipation, `Becoming.Locality, `Becoming.Roles, `Becoming.Reserve, `Becoming.Evolution, `Becoming.Space, `Becoming.Premises, `Becoming.Openness, `Becoming.Counting, `Becoming.Standing, `Becoming.Resolution, `Becoming.Entropy, `Becoming.Continuation, `Becoming.Admission, `Becoming.Regions, `Becoming.Metaethics, `Becoming.Ranking, `Becoming.Correspondence, `Becoming.Descent, `Becoming.Standpoints, `Becoming.Significance, `Becoming.Interdependence, `Becoming.Feedback, `Becoming.Testing, `Becoming.Runaway, `Becoming.Boundaries, `Becoming.Relevance, `Becoming] do
    let some index := env.getModuleIdx? m | throwError m!"no module {m}"
    let mut count := 0
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some index then
        count := count + 1
        let axioms ← liftCoreM <| Lean.collectAxioms n
        if axioms.size > 0 then logInfo m!"AXIOMS {n} {axioms.toList}"
    logInfo m!"CONSTANTS {m} {count}"
