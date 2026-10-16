import Lean
import GenerativeCore
import Becoming.Frame
import InquirySufficiency
import Becoming.Inquiry
import Becoming.Recurrence
import Becoming.Diagonal
import Becoming.Context
import Becoming.Quantum
import RelationalRenewal
import Becoming.Renewal
import Becoming.Dependence
import Becoming.Return
import Becoming.Horizon
import Becoming.Joint
import Becoming.Experiment
import Becoming.Mechanism
import Becoming.Generation
import Becoming.Flow
import Becoming.Change
import Becoming.Evolution
import Becoming.Population
import Becoming.Dissipation
import Becoming.Locality
import Becoming.Roles
import Becoming.Reserve
import Becoming.Space
import Becoming.Unfolding
import Becoming.Histories
import Becoming.Attraction
import Becoming.Capture
import Becoming.Branching
import Becoming.Decidedness
import Becoming.Premises
import Becoming.Sampling
import Becoming.Openness
import Becoming.Resolution
import Becoming.Listing
import Becoming.Order
import Becoming.OrderNormal
import Becoming.Counting
import Becoming.OneStep
import Becoming.Weighted
import Becoming.Transmission
import Becoming.Continuation
import Becoming.Succession
import Becoming.Substitution
import Becoming.Identity
import Becoming.Persistence
import Becoming.Wholes
import Becoming.Seeking
import Becoming.Tower
import Becoming.Standing
import Becoming.Entropy
import Becoming.Units
import Becoming.Imbalance
import Becoming.Admission
import Becoming.Regions
import Becoming.Metaethics
import Becoming.Ranking
import Becoming.Correspondence
import Becoming.Descent
import Becoming.Standpoints
import Becoming.Significance
import Becoming.Interdependence
import Becoming.Feeding
import Becoming.Feedback
import Becoming.Testing
import Becoming.Runaway
import Becoming.Response
import Becoming.Counterfactual
import Becoming.Selection
import Becoming.Learning
import Becoming.Revision
import Becoming.ReferencePlan
import Becoming.ContinuingRevision
import Becoming.Description
import Becoming.Identification
import Becoming.Boundaries
import Becoming.Relevance
import Becoming
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  for m in [`GenerativeCore, `Becoming.Frame, `InquirySufficiency, `Becoming.Inquiry, `Becoming.Recurrence, `Becoming.Diagonal, `Becoming.Context, `Becoming.Quantum, `RelationalRenewal, `Becoming.Renewal, `Becoming.Dependence, `Becoming.Return, `Becoming.Horizon, `Becoming.Joint, `Becoming.Experiment, `Becoming.Mechanism, `Becoming.Generation, `Becoming.Flow, `Becoming.Change, `Becoming.Evolution, `Becoming.Population, `Becoming.Dissipation, `Becoming.Locality, `Becoming.Roles, `Becoming.Reserve, `Becoming.Space, `Becoming.Unfolding, `Becoming.Histories, `Becoming.Attraction, `Becoming.Capture, `Becoming.Branching, `Becoming.Decidedness, `Becoming.Premises, `Becoming.Sampling, `Becoming.Openness, `Becoming.Resolution, `Becoming.Listing, `Becoming.Order, `Becoming.OrderNormal, `Becoming.Counting, `Becoming.OneStep, `Becoming.Weighted, `Becoming.Transmission, `Becoming.Continuation, `Becoming.Succession, `Becoming.Substitution, `Becoming.Identity, `Becoming.Persistence, `Becoming.Wholes, `Becoming.Seeking, `Becoming.Tower, `Becoming.Standing, `Becoming.Entropy, `Becoming.Units, `Becoming.Imbalance, `Becoming.Admission, `Becoming.Regions, `Becoming.Metaethics, `Becoming.Ranking, `Becoming.Correspondence, `Becoming.Descent, `Becoming.Standpoints, `Becoming.Significance, `Becoming.Interdependence, `Becoming.Feeding, `Becoming.Feedback, `Becoming.Testing, `Becoming.Runaway, `Becoming.Response, `Becoming.Counterfactual, `Becoming.Selection, `Becoming.Learning, `Becoming.Revision, `Becoming.ReferencePlan, `Becoming.ContinuingRevision, `Becoming.Description, `Becoming.Identification, `Becoming.Boundaries, `Becoming.Relevance, `Becoming] do
    let some index := env.getModuleIdx? m | throwError m!"no module {m}"
    let mut count := 0
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some index then
        count := count + 1
        let axioms ← liftCoreM <| Lean.collectAxioms n
        if axioms.size > 0 then logInfo m!"AXIOMS {n} {axioms.toList}"
    logInfo m!"CONSTANTS {m} {count}"
