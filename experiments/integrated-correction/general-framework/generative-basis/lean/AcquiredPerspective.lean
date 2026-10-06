import ConstructedPrediction
import RecipientCorrection

/-!
# Acquired action-effect representation in the existing paid history

This file changes no event law or controller. `effectForecast` exposes the
existing score's two action-conditioned readings; the running command already
consumes that score. The represented effect is the receipt that funds and renews
the same physical organization. This is a functional, partial representation,
not an acquired identity, full self-model, subjective experience or ethical
orientation. Recipient target names and the decoder in the inherited recipient
law remain supplied; their role is separately checked below.
-/
namespace AcquiredPerspective

open PredictionAction

/-- Existing finite score read at an arbitrary candidate action. This readout is
analytical; no new register or new command rule is installed. -/
def effectForecast (s : State) (candidate : Bool) : Nat :=
  if candidate then s.score else 4 - s.score

def effectNumerator (receipt : Bool) : Nat := if receipt then 4 else 0

/-- Exactness concerns both potential action receipts in the supplied noiseless
binary law. The second candidate is a response-function counterfactual; the
inherited work event executes the current command only. -/
def ExactEffects (s : State) : Prop :=
  ∀ candidate, effectForecast s candidate =
    effectNumerator (receiptOf candidate s.physical.core.regime true)

theorem existing_forecast_is_command_readout (s : State) :
    forecastNumerator s = effectForecast s (command s) := rfl

theorem forecast_reads_retained_score (s : State) (candidate : Bool)
    (physical : UpdaterFormation.State) (receipt : Bool) (phase : Phase) :
    effectForecast { s with physical := physical, receipt := receipt, phase := phase } candidate =
      effectForecast s candidate := rfl

theorem command_ignores_unobserved_regime (s : State) (regime : Bool) :
    command { s with physical := { s.physical with core :=
      { s.physical.core with regime := regime } } } = command s := rfl

/-- A correctly action-tagged receipt suffices under the already installed fast
writer. Both antecedents are discharged in the actual history below. -/
theorem fast_receipt_write_models_both_actions (p : Parameters) (s : State)
    (writer : s.physical.directed = true)
    (record : s.receipt = receiptOf s.physical.core.selector s.physical.core.regime true) :
    ExactEffects (advance p s .write) := by
  cases s with
  | mk physical score receipt phase =>
    cases physical with
    | mk core directed lease seen remainder material =>
      cases core with
      | mk fuel packets selector lifetime regime =>
        change directed = true at writer
        change receipt = receiptOf selector regime true at record
        cases writer
        cases record
        intro candidate
        cases selector <;> cases regime <;> cases candidate <;> rfl

/-- The inherited plant supplies the correct action tag and receipt at work;
this theorem does not assume a correct acquired model before acting. -/
theorem work_then_fast_write_models_both_actions (p : Parameters) (s : State)
    (writer : s.physical.directed = true) :
    ExactEffects (advance p (advance p s .work) .write) := by
  apply fast_receipt_write_models_both_actions
  · exact writer
  · rfl

/-- An exact extreme score commands the supported action through the existing
controller, not through an extra evaluator. -/
theorem exact_effects_command_captures (s : State) (exactEffects : ExactEffects s) :
    capture s = true := by
  have score := exactEffects true
  change s.score = effectNumerator (receiptOf true s.physical.core.regime true) at score
  cases s with
  | mk physical q receipt phase =>
    cases physical with
    | mk core directed lease seen remainder material =>
      cases core with
      | mk fuel packets selector lifetime regime =>
        cases regime <;> cases score <;> rfl

/-- Direct trace construction; imported definitions still contribute their
recorded standard proof dependencies. -/
theorem run_trace {p : Parameters} {r : ConstructedPrediction.Running}
    {events : List Event} (paid : ConstructedPrediction.Runnable p r events) :
    ConstructedPrediction.Trace p r events (ConstructedPrediction.run p r events) := by
  induction events generalizing r with
  | nil => exact .nil _
  | cons event events ih =>
    exact .cons ⟨paid.1, paid.2.1, paid.2.2.1, rfl⟩ (ih paid.2.2.2)

/-- Reconstruct guards by conjunction introduction and closed arithmetic,
without invoking the inherited compound decidability instances. -/
def acquisitionEvents : List Event :=
  cycles 6 ++ [.reverse] ++ cycles 2 ++ [.formUpdater true, .rent, .work]

def learned : ConstructedPrediction.Running :=
  ConstructedPrediction.run primary ConstructedPrediction.ready (cycles 6)

def shifted : ConstructedPrediction.Running :=
  ConstructedPrediction.advance primary learned .reverse

def recorded : ConstructedPrediction.Running := ConstructedPrediction.correctiveRecord

def revised : ConstructedPrediction.Running :=
  ConstructedPrediction.advance primary recorded .write

def used : ConstructedPrediction.Running :=
  ConstructedPrediction.advance primary
    (ConstructedPrediction.advance primary
      (ConstructedPrediction.advance primary revised .finish) .rent) .work

def retained : ConstructedPrediction.Running :=
  ConstructedPrediction.advance primary
    (ConstructedPrediction.advance primary used .write) .finish

set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem memory_is_acquired_before_reversal :
    ConstructedPrediction.Trace primary ConstructedPrediction.ready (cycles 6) learned ∧
    ConstructedPrediction.ready.core.score = 2 ∧ learned.core.score = 4 ∧
    ExactEffects learned.core := by
  refine ⟨?_, rfl, rfl, ?_⟩
  · apply run_trace
    repeat first | apply And.intro | exact rfl | exact True.intro | decide
  · intro candidate
    cases candidate <;> rfl

theorem dependency_changes_while_memory_is_retained :
    ConstructedPrediction.Step primary learned .reverse shifted ∧
    shifted.core.score = learned.core.score ∧
    command shifted.core = command learned.core ∧
    ¬ ExactEffects shifted.core := by
  refine ⟨?_, rfl, rfl, ?_⟩
  · repeat first | apply And.intro | exact rfl | decide
  · intro exactEffects
    have impossible : (0 : Nat) = 4 := exactEffects false
    exact Nat.noConfusion impossible

set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem actual_acquisition_trace :
    ConstructedPrediction.Trace primary ConstructedPrediction.ready acquisitionEvents recorded := by
  apply run_trace
  change ConstructedPrediction.Runnable primary ConstructedPrediction.ready acquisitionEvents
  repeat first | apply And.intro | exact rfl | exact True.intro | decide

/-- The concrete record is reached from the original absent-parts state using
exactly the already-supplied formation, adapter and register installation. -/
theorem formed_acquired_record :
    ConstructedPrediction.StagedTrace primary 11 true
      (.before (.formation ConstructedPrediction.initial))
      (ConstructedPrediction.precedingEvents.map ConstructedPrediction.Event.before ++
        .retrofit :: acquisitionEvents.map ConstructedPrediction.Event.predict)
      (.prediction recorded) :=
  ConstructedPrediction.compose_actual_state
    ConstructedPrediction.actual_formed_prefix
    ConstructedPrediction.actual_typed_retrofit actual_acquisition_trace

theorem reached_record_conditions :
    recorded.core.physical.directed = true ∧
    recorded.core.receipt = receiptOf recorded.core.physical.core.selector
      recorded.core.physical.core.regime true ∧
    recorded.core.physical.core.selector = true ∧
    recorded.core.receipt = false ∧ recorded.core.score = 2 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

theorem reached_write_is_paid :
    ConstructedPrediction.Step primary recorded .write revised := by
  repeat first | apply And.intro | exact rfl | decide

theorem reached_write_models_both_actions : ExactEffects revised.core :=
  fast_receipt_write_models_both_actions primary recorded.core
    reached_record_conditions.1 reached_record_conditions.2.1

theorem reached_write_corrects_both_forecasts :
    effectForecast recorded.core false = 2 ∧ effectForecast recorded.core true = 2 ∧
    effectForecast revised.core false = 4 ∧ effectForecast revised.core true = 0 :=
  ⟨rfl, rfl, rfl, rfl⟩

theorem reached_write_changes_only_future_action :
    command recorded.core = true ∧ command revised.core = false ∧
    revised.core.physical.core.selector = recorded.core.physical.core.selector ∧
    revised.core.physical.core.regime = recorded.core.physical.core.regime ∧
    revised.registerUnits = recorded.registerUnits ∧
    revised.resident = recorded.resident ∧ revised.intact = recorded.intact ∧
    revised.core.physical.core.fuel + primary.writing = recorded.core.physical.core.fuel :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem corrected_command_is_actually_used :
    ConstructedPrediction.Trace primary revised [.finish, .rent, .work] used := by
  apply run_trace
  repeat first | apply And.intro | exact rfl | exact True.intro | decide

theorem corrected_use_then_paid_retention :
    ConstructedPrediction.Trace primary used [.write, .finish] retained ∧
    retained = ConstructedPrediction.final := by
  constructor
  · apply run_trace
    repeat first | apply And.intro | exact rfl | exact True.intro | decide
  · rfl

/-- The predicted receipt actually replenishes the same actor's fuel; a further
paid write and finish renew both support leases under the inherited law. -/
theorem corrected_action_supports_same_organization :
    used.core.receipt = true ∧ used.core.physical.core.selector = false ∧
    used.core.physical.core.fuel = 19 ∧
    retained.core.physical.core.lease =
      primary.base.selector.lifetime ∧
    retained.core.physical.moduleLease =
      primary.base.moduleLifetime :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

/-- Own effects and recipient effects are different inherited receipt functions.
This comparison does not manufacture a new target identity or join their laws. -/
theorem own_model_does_not_determine_recipient_effect :
    ExactEffects revised.core ∧
    effectForecast revised.core false = 4 ∧
    RecipientCorrection.receiptOf false false true = true ∧
    RecipientCorrection.receiptOf false true true = false ∧
    RecipientCorrection.actorCreditFromRecipient false false true =
      RecipientCorrection.actorCreditFromRecipient false true true :=
  ⟨reached_write_models_both_actions, rfl, rfl, rfl, rfl⟩

/-- Existing target-indexed acquisition can keep the acquired actor relation
while learning an opposite recipient relation. Target calibration and this
packed recoding already belong to RecipientCorrection, not to this bridge. -/
theorem recipient_acquisition_retains_actor_distinction :
    let actor := command revised.core
    let inherited := RecipientCorrection.pack (actor, actor)
    let updated := RecipientCorrection.packedWrite inherited .recipient
      (RecipientCorrection.decode actor (RecipientCorrection.receiptOf actor true true))
    RecipientCorrection.packedAct updated .actor = false ∧
    RecipientCorrection.packedAct updated .recipient = true ∧
    RecipientCorrection.packedAct inherited .recipient = false :=
  ⟨rfl, rfl, rfl⟩

end AcquiredPerspective

#print axioms AcquiredPerspective.existing_forecast_is_command_readout
#print axioms AcquiredPerspective.forecast_reads_retained_score
#print axioms AcquiredPerspective.command_ignores_unobserved_regime
#print axioms AcquiredPerspective.fast_receipt_write_models_both_actions
#print axioms AcquiredPerspective.work_then_fast_write_models_both_actions
#print axioms AcquiredPerspective.exact_effects_command_captures
#print axioms AcquiredPerspective.run_trace
#print axioms AcquiredPerspective.memory_is_acquired_before_reversal
#print axioms AcquiredPerspective.dependency_changes_while_memory_is_retained
#print axioms AcquiredPerspective.actual_acquisition_trace
#print axioms AcquiredPerspective.formed_acquired_record
#print axioms AcquiredPerspective.reached_record_conditions
#print axioms AcquiredPerspective.reached_write_is_paid
#print axioms AcquiredPerspective.reached_write_models_both_actions
#print axioms AcquiredPerspective.reached_write_corrects_both_forecasts
#print axioms AcquiredPerspective.reached_write_changes_only_future_action
#print axioms AcquiredPerspective.corrected_command_is_actually_used
#print axioms AcquiredPerspective.corrected_use_then_paid_retention
#print axioms AcquiredPerspective.corrected_action_supports_same_organization
#print axioms AcquiredPerspective.own_model_does_not_determine_recipient_effect
#print axioms AcquiredPerspective.recipient_acquisition_retains_actor_distinction
