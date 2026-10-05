import RecipientIdentification

/-!
An acquired controller record can corroborate a separately published command.
The imported updater is the existing positive-receipt qualification mechanism.
Its law is fixed throughout this replay; the stream represents already acquired
receipts, not newly constructed, paid or automatically available observations.
Neither runtime corroboration nor a matching context label reads the hidden law.
-/
namespace SemanticCalibration

open RecipientCorrection (Target Laws lookup packedAct receiptOf)
open RecipientIdentification (Registers candidate Sound feedback)

structure Exposure where
  target : Target
  available : Bool
  channel : Bool
deriving DecidableEq, Repr

def acquire (laws : Laws) (m : Registers) (e : Exposure) : Registers :=
  feedback m e.target (if e.channel then
    some (receiptOf (packedAct m.q e.target) (lookup laws e.target) e.available)
    else none)

def replay (laws : Laws) (m : Registers) (events : List Exposure) : Registers :=
  events.foldl (acquire laws) m

theorem acquired_step_preserves_qualification (laws : Laws) (m : Registers)
    (e : Exposure) (h : Sound m laws.2) : Sound (acquire laws m e) laws.2 := by
  rcases e with ⟨target,available,channel⟩
  cases channel with
  | false => simpa [acquire,RecipientIdentification.missing_feedback_retains] using h
  | true =>
    cases target with
    | actor => simpa [acquire,RecipientIdentification.actor_feedback_is_sham] using h
    | recipient =>
      exact RecipientIdentification.recipient_physical_feedback_sound m laws.2 available h

theorem finite_replay_preserves_qualification (laws : Laws) (m : Registers)
    (events : List Exposure) (h : Sound m laws.2) : Sound (replay laws m events) laws.2 := by
  induction events generalizing m with
  | nil => exact h
  | cons e es ih =>
    exact ih (acquire laws m e) (acquired_step_preserves_qualification laws m e h)

theorem initially_unqualified_replay_is_sound (laws : Laws) (m : Registers)
    (events : List Exposure) (unqualified : m.flag = false) :
    Sound (replay laws m events) laws.2 := by
  apply finite_replay_preserves_qualification
  intro qualified
  rw [unqualified] at qualified
  contradiction

/- `ready` aggregates the checked readable/current/scope/installed/recoded
conditions. It is an observable Boolean, not evidence that target laws stayed
fixed. This output is corroboration, not an action instruction or final veto. -/
def corroborate (ready : Bool) (m : Registers) (claim : Option Bool) : Option Bool :=
  match claim with
  | none => none
  | some command =>
      if ready && m.flag && (command == candidate m) then some command else none

theorem corroboration_exact (ready : Bool) (m : Registers)
    (claim : Option Bool) (command : Bool) :
    corroborate ready m claim = some command ↔
      claim = some command ∧ ready = true ∧ m.flag = true ∧ command = candidate m := by
  cases claim with
  | none => simp [corroborate]
  | some value =>
    cases ready <;> cases hf : m.flag <;> cases hc : candidate m <;>
      cases value <;> cases command <;> simp [corroborate,hf,hc]

theorem grounded_corroboration_is_compatible (oldLaw currentLaw : Bool)
    (m : Registers) (ready : Bool) (claim : Option Bool) (command : Bool)
    (grounded : Sound m oldLaw) (stable : oldLaw = currentLaw)
    (accepted : corroborate ready m claim = some command) :
    ∀ opportunity, receiptOf command currentLaw opportunity = opportunity := by
  have data := (corroboration_exact ready m claim command).mp accepted
  have correct : command = currentLaw := data.2.2.2.trans ((grounded data.2.2.1).trans stable)
  rw [correct]
  intro opportunity
  cases currentLaw <;> cases opportunity <;> rfl

theorem replay_corroboration_is_compatible (laws : Laws) (m : Registers)
    (events : List Exposure) (unqualified : m.flag = false)
    (ready : Bool) (claim : Option Bool) (command : Bool)
    (accepted : corroborate ready (replay laws m events) claim = some command) :
    ∀ opportunity, receiptOf command laws.2 opportunity = opportunity :=
  grounded_corroboration_is_compatible laws.2 laws.2 (replay laws m events)
    ready claim command (initially_unqualified_replay_is_sound laws m events unqualified)
    rfl accepted

theorem sound_qualified_anchor_corroborates_exactly_the_true_command
    (m : Registers) (law command : Bool) (grounded : Sound m law)
    (qualified : m.flag = true) :
    corroborate true m (some command) = some command ↔ command = law := by
  rw [corroboration_exact]
  simp [qualified,grounded qualified]

theorem disagreement_excludes_joint_current_soundness (m : Registers)
    (oldLaw currentLaw claim : Bool) (qualified : m.flag = true)
    (disagree : claim ≠ candidate m) :
    ¬ (Sound m oldLaw ∧ oldLaw = currentLaw ∧ claim = currentLaw) := by
  rintro ⟨grounded,stable,trueClaim⟩
  exact disagree (trueClaim.trans (stable.symm.trans (grounded qualified).symm))

/- Writing an archive command into the retained candidate and setting its flag
before comparing discards the independent acquired anchor. Equality then holds
for every imported command, including one incompatible with the current law. -/
def importClaim (m : Registers) (command : Bool) : Registers :=
  ⟨RecipientCorrection.packedWrite m.q .recipient command,true⟩

theorem self_import_guarantees_agreement_without_calibration (m : Registers) (command : Bool) :
    corroborate true (importClaim m command) (some command) = some command ∧
    ∃ law, receiptOf command law true = false := by
  constructor
  · apply (corroboration_exact true (importClaim m command) (some command) command).mpr
    refine ⟨rfl,rfl,rfl,?_⟩
    exact (RecipientCorrection.packed_write_sets_queried_cell m.q .recipient command).symm
  · exact ⟨!command,by cases command <;> rfl⟩

/- This is the complete observation type of this explicit countermodel. q and
its flag are visible, together with the claimed command and readiness metadata.
The two worlds differ in the uncalibrated law, not in a hidden accessible q. -/
structure Visible where
  registers : Registers
  claim : Option Bool
  ready : Bool
deriving DecidableEq, Repr

structure World where
  visible : Visible
  law : Bool
deriving DecidableEq, Repr

def agreed : Visible := ⟨⟨0,true⟩,some false,true⟩
def world0 : World := ⟨agreed,false⟩
def world1 : World := ⟨agreed,true⟩

theorem common_corruption_agrees_but_is_wrong :
    world0.visible = world1.visible ∧
    corroborate agreed.ready agreed.registers agreed.claim = some false ∧
    receiptOf false world0.law true = true ∧ receiptOf false world1.law true = false := by
  decide

theorem full_visible_state_cannot_identify_both_uncalibrated_worlds :
    ¬ ∃ decode : Visible → Bool,
      decode world0.visible = world0.law ∧ decode world1.visible = world1.law := by
  rintro ⟨decode,h0,h1⟩
  change decode agreed = false at h0
  change decode agreed = true at h1
  rw [h0] at h1
  contradiction

theorem stale_qualification_can_accept_old_error_and_decline_new_truth :
    let old : Registers := ⟨0,true⟩
    Sound old false ∧
    corroborate true old (some false) = some false ∧
    receiptOf false true true = false ∧
    corroborate true old (some true) = none ∧
    receiptOf true true true = true := by
  exact ⟨by intro _; rfl,rfl,rfl,rfl,rfl⟩

end SemanticCalibration

#print axioms SemanticCalibration.acquired_step_preserves_qualification
#print axioms SemanticCalibration.finite_replay_preserves_qualification
#print axioms SemanticCalibration.initially_unqualified_replay_is_sound
#print axioms SemanticCalibration.corroboration_exact
#print axioms SemanticCalibration.grounded_corroboration_is_compatible
#print axioms SemanticCalibration.replay_corroboration_is_compatible
#print axioms SemanticCalibration.sound_qualified_anchor_corroborates_exactly_the_true_command
#print axioms SemanticCalibration.disagreement_excludes_joint_current_soundness
#print axioms SemanticCalibration.self_import_guarantees_agreement_without_calibration
#print axioms SemanticCalibration.common_corruption_agrees_but_is_wrong
#print axioms SemanticCalibration.full_visible_state_cannot_identify_both_uncalibrated_worlds
#print axioms SemanticCalibration.stale_qualification_can_accept_old_error_and_decline_new_truth
