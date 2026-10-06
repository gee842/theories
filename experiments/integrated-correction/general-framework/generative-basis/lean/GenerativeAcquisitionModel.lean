import GenerativeOutcomeModel
import AcquiredPerspective

/-!
# The acquired representation in the existing generative model

ConstructedPrediction already uses Generative.Process and Generative.Trace.
This entry composes its actual acquisition, correction and paid use without
adding a second process, physical law, controller or primitive subject. The
inherited local recipes and initial resources are still supplied. This proves
a partial action/support representation, not a generated body boundary,
phenomenal experience or an ethical conclusion.

The separate acquired-perspective checker preserves the structural entry's
strict proof-dependency policy and checks the inherited physical chain against
its original source and per-declaration dependency receipts.
-/

namespace Generative.Model.Acquisition

open AcquiredPerspective
open PredictionAction

/-- Every event in the correction/use suffix is enabled at its actual predecessor.
The final state is the previously established material-backed final state. -/
theorem correction_and_use_trace :
    Generative.Trace (ConstructedPrediction.process primary) recorded
      [.write, .finish, .rent, .work, .write, .finish]
      ConstructedPrediction.final := by
  have suffix : ConstructedPrediction.Trace primary revised
      ([.finish, .rent, .work] ++ [.write, .finish]) retained :=
    Generative.trace_append_iff.mpr
      ⟨used, corrected_command_is_actually_used, corrected_use_then_paid_retention.1⟩
  have whole := Generative.Trace.cons reached_write_is_paid suffix
  exact corrected_use_then_paid_retention.2 ▸ whole

/-- Formation, acquisition, correction and use share their actual boundary states.
No support stock or learned record is reset at the composition points. -/
theorem formed_acquisition_and_use :
    ConstructedPrediction.StagedTrace primary 11 true
      (.before (.formation ConstructedPrediction.initial))
      (ConstructedPrediction.precedingEvents.map ConstructedPrediction.Event.before ++
        .retrofit ::
          (acquisitionEvents ++
            ([.write, .finish, .rent, .work, .write, .finish] : List PredictionAction.Event)).map
            ConstructedPrediction.Event.predict)
      (.prediction ConstructedPrediction.final) := by
  apply ConstructedPrediction.compose_actual_state
    ConstructedPrediction.actual_formed_prefix ConstructedPrediction.actual_typed_retrofit
  exact Generative.trace_append_iff.mpr
    ⟨recorded, actual_acquisition_trace, correction_and_use_trace⟩

/-- The acquired representation has a checked response-function meaning, changes
the actual next command, and is used in the same paid generative history.
Candidate-action exactness is conditional on the inherited response law;
it is not a claim that both alternatives are executable from the same state. -/
theorem acquired_representation_and_actual_use :
    ExactEffects revised.core ∧
    command recorded.core = true ∧ command revised.core = false ∧
    Generative.Trace (ConstructedPrediction.process primary) recorded
      [.write, .finish, .rent, .work, .write, .finish]
      ConstructedPrediction.final ∧
    used.core.receipt = true ∧ used.core.physical.core.fuel = 19 :=
  ⟨reached_write_models_both_actions,
    reached_write_changes_only_future_action.1,
    reached_write_changes_only_future_action.2.1,
    correction_and_use_trace,
    corrected_action_supports_same_organization.1,
    corrected_action_supports_same_organization.2.2.1⟩

end Generative.Model.Acquisition

#print axioms Generative.Model.Acquisition.correction_and_use_trace
#print axioms Generative.Model.Acquisition.formed_acquisition_and_use
#print axioms Generative.Model.Acquisition.acquired_representation_and_actual_use
