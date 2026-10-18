import Becoming.Dephasing
import Becoming.ProjectedLaws

/-!
# A joint relation that changes while both local states stay fixed

On the two-part configuration of `Becoming.Dephasing` (a control and a register), a phase step
changes the joint configuration while both local states (`localStates`: the control and the
register density) and the basis masses stay fixed; the same later interaction (a controlled X)
then gives a different response. So no reading of the local pair carries the interaction
(`Becoming.Readout`), and a reduced description that keeps one cross contribution more does. The
law of change of the configuration (`next`, two moves) is a process of the spine
(`Assurance.ofMap`). Board item F3R (18 October 2026) states here, on core types and with
constructive proofs, what `RelationalReduction` (8 October) proved and what the joins
`JointPhaseTraces` and `JointPhaseTracesInherited` (17 October) read of its traces.

* **The phase step keeps both local states and the basis masses** and changes the retained
  cross contribution (`actual_phase_preserves_both_local_states`,
  `actual_phase_preserves_basis_masses`, `retained_cross_distinguishes_change`); **the same
  interaction tells the two apart** (`same_interaction_distinguishes_relation`).
* **No reading of the local pair carries the interaction**: no update of the local states gives
  the control after it (`no_local_pair_update`, an instance of `Readout.decoder_pair_iff`), and no
  determined law on local states carries the configuration's law (`local_pair_carries_no_law`, an
  instance of `Readout.law_through_iff`).
* **A summary that keeps the cross contribution is exact.** The summary recovers the control
  (`summary_recovers_control`) and commutes with the law (`summary_update_exact`), so it is exact
  along every finite word (`every_finite_word_exact`, `Readout.foldl_semiconj`) and gives the
  control's response at the end of every trace (`summary_response`); it still omits the register
  (`summary_omits_other_relations`, `summary_omits_register`).

The configurations, operations and their physical reading are supplied; nothing here derives
them. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Integers Dephasing ProjectedLaws

namespace JointPhase

/-- Exchange the roles of the two coordinates, to compute the other partial trace. -/
def exchangeCoordinates (v : Joint) : Joint :=
  ⟨⟨v.zero.zero, v.one.zero⟩, ⟨v.zero.one, v.one.one⟩⟩

/-- The register's density. -/
def registerDensity (v : Joint) : Matrix := controlDensity (exchangeCoordinates v)

/-- Both local states. -/
def localStates (v : Joint) : Matrix × Matrix := (controlDensity v, registerDensity v)

/-- Z on the first coordinate. -/
def phase (v : Joint) : Joint := ⟨v.zero, negVec v.one⟩

def joined : Joint := recordBranch (withBlank ⟨1, 1⟩)
def changed : Joint := phase joined

/-- The computational-basis distribution. -/
def basisMasses (v : Joint) : Int × Int × Int × Int :=
  (v.zero.zero * v.zero.zero, v.zero.one * v.zero.one,
   v.one.zero * v.one.zero, v.one.one * v.one.one)

/-- The cross contribution that enters the control after the interaction. -/
def coupledCross (v : Joint) : Int := v.zero.zero * v.one.one + v.zero.one * v.one.zero

/-- The two branch weights and the two cross contributions. -/
structure Summary where
  zeroMass : Int
  oneMass : Int
  localCross : Int
  jointCross : Int
  deriving DecidableEq

def summarize (v : Joint) : Summary := ⟨norm v.zero, norm v.one, inner v.zero v.one, coupledCross v⟩

def decodeControl (s : Summary) : Matrix := ⟨s.zeroMass, s.localCross, s.localCross, s.oneMass⟩

/-- The interaction and the phase step. -/
inductive Event where
  | interact
  | shiftPhase
  deriving DecidableEq

/-- The law of change of the configuration. -/
def next (v : Joint) : Event → Joint
  | .interact => recordBranch v
  | .shiftPhase => phase v

/-- Interaction exchanges the two cross contributions; the phase step changes both signs. -/
def reducedNext (s : Summary) : Event → Summary
  | .interact => ⟨s.zeroMass, s.oneMass, s.jointCross, s.localCross⟩
  | .shiftPhase => ⟨s.zeroMass, s.oneMass, -s.localCross, -s.jointCross⟩

/-- The law read as a process. -/
abbrev process : Process Joint Event := Assurance.ofMap next

/-! ## The witnesses -/

theorem formation_from_blank : recordBranch (hControl (blankControl basisZero)) = joined := by decide

theorem actual_phase_preserves_both_local_states :
    localStates joined = (⟨1, 0, 0, 1⟩, ⟨1, 0, 0, 1⟩) ∧ localStates changed = localStates joined := by
  decide

theorem actual_phase_preserves_basis_masses :
    basisMasses joined = (1, 0, 0, 1) ∧ basisMasses changed = basisMasses joined := by decide

theorem same_interaction_distinguishes_relation :
    response (controlDensity (recordBranch joined)) = (4, 0, 4) ∧
      response (controlDensity (recordBranch changed)) = (0, 4, 4) := by decide

/-- **No update of the local states gives the control after the interaction**: the local pair
merges `joined` and `changed`, which the interaction separates (`Readout.decoder_pair_iff`). -/
theorem no_local_pair_update :
    ¬ ∃ update : (Matrix × Matrix) → Matrix,
      update (localStates joined) = controlDensity (recordBranch joined) ∧
      update (localStates changed) = controlDensity (recordBranch changed) :=
  fun found =>
    (by decide : controlDensity (recordBranch joined) ≠ controlDensity (recordBranch changed))
      ((Readout.decoder_pair_iff (f := fun v => controlDensity (recordBranch v))
        (by decide : localStates joined = localStates changed)).mp found)

/-- **No determined law on the local pair carries the configuration's law**
(`Readout.law_through_iff`). -/
theorem local_pair_carries_no_law :
    ¬ ∃ Q : Process (Matrix × Matrix) Event, Determined Q ∧
      FactorsThrough (Assurance.ofMap next) localStates Q :=
  fun found =>
    (by decide : localStates (next joined .interact) ≠ localStates (next changed .interact))
      (((Readout.law_through_iff next localStates).mp found) joined changed .interact (by decide))

theorem retained_cross_distinguishes_change :
    summarize joined = ⟨1, 1, 0, 1⟩ ∧ summarize changed = ⟨1, 1, 0, -1⟩ := by decide

/-- The summary keeps less than the whole configuration or both local states. -/
theorem summary_omits_other_relations :
    summarize (⟨⟨1, 0⟩, ⟨0, 0⟩⟩ : Joint) = summarize ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ ∧
      registerDensity (⟨⟨1, 0⟩, ⟨0, 0⟩⟩ : Joint) ≠ registerDensity ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ := by decide

/-! ## The exact summary -/

/-- **The summary recovers the control.** -/
theorem summary_recovers_control : ∀ v : Joint, decodeControl (summarize v) = controlDensity v
  | ⟨⟨a₀, a₁⟩, ⟨b₀, b₁⟩⟩ =>
    show (⟨a₀ * a₀ + a₁ * a₁, a₀ * b₀ + a₁ * b₁, a₀ * b₀ + a₁ * b₁, b₀ * b₀ + b₁ * b₁⟩ : Matrix) =
        ⟨a₀ * a₀ + a₁ * a₁, a₀ * b₀ + a₁ * b₁, b₀ * a₀ + b₁ * a₁, b₀ * b₀ + b₁ * b₁⟩ by
      rw [mul_comm b₀ a₀, mul_comm b₁ a₁]

/-- **The summary commutes with the law.** -/
theorem summary_update_exact : Commuting next reducedNext summarize
  | ⟨⟨a₀, a₁⟩, ⟨b₀, b₁⟩⟩, .interact =>
    show (⟨a₀ * a₀ + a₁ * a₁, b₁ * b₁ + b₀ * b₀, a₀ * b₁ + a₁ * b₀, a₀ * b₀ + a₁ * b₁⟩ : Summary) =
        ⟨a₀ * a₀ + a₁ * a₁, b₀ * b₀ + b₁ * b₁, a₀ * b₁ + a₁ * b₀, a₀ * b₀ + a₁ * b₁⟩ by
      rw [add_comm (b₁ * b₁) (b₀ * b₀)]
  | ⟨⟨a₀, a₁⟩, ⟨b₀, b₁⟩⟩, .shiftPhase =>
    show (⟨a₀ * a₀ + a₁ * a₁, -b₀ * -b₀ + -b₁ * -b₁, a₀ * -b₀ + a₁ * -b₁,
          a₀ * -b₁ + a₁ * -b₀⟩ : Summary) =
        ⟨a₀ * a₀ + a₁ * a₁, b₀ * b₀ + b₁ * b₁, -(a₀ * b₀ + a₁ * b₁), -(a₀ * b₁ + a₁ * b₀)⟩ by
      rw [neg_mul_neg b₀ b₀, neg_mul_neg b₁ b₁, mul_neg a₀ b₀, mul_neg a₁ b₁, mul_neg a₀ b₁,
        mul_neg a₁ b₀, neg_add (a₀ * b₀) (a₁ * b₁), neg_add (a₀ * b₁) (a₁ * b₀)]

/-- **The summary is exact along every finite word** (`Readout.foldl_semiconj`). -/
theorem every_finite_word_exact (v : Joint) (word : List Event) :
    summarize (word.foldl next v) = word.foldl reducedNext (summarize v) :=
  Readout.foldl_semiconj next summarize reducedNext summary_update_exact word v

/-- **The summary gives the control's response after every finite word.** -/
theorem every_finite_control_response_exact (v : Joint) (word : List Event) :
    response (decodeControl (word.foldl reducedNext (summarize v))) =
      response (controlDensity (word.foldl next v)) :=
  congrArg response ((congrArg decodeControl (every_finite_word_exact v word)).symm.trans
    (summary_recovers_control _))

/-! ## On the traces of the law -/

theorem step_iff {s t : Joint} {a : Event} : process.step s a t ↔ t = next s a := Iff.rfl

/-- **A trace of the process ends where the law takes it along its word.** -/
theorem trace_end {v t : Joint} {word : List Event} (path : Trace process v word t) :
    t = word.foldl next v :=
  ProjectedLaws.trace_iff.mp path

/-- **Along every word the process has a trace.** -/
theorem evolve_trace (v : Joint) (word : List Event) : Trace process v word (word.foldl next v) :=
  ProjectedLaws.trace_iff.mpr rfl

theorem interaction_forms_joined : process.step (hControl (blankControl basisZero)) .interact joined :=
  step_iff.mpr formation_from_blank.symm

theorem phase_keeps_local_states :
    ∀ t, process.step joined .shiftPhase t → localStates t = localStates joined :=
  fun _ step => (congrArg localStates (step_iff.mp step)).trans
    actual_phase_preserves_both_local_states.2

theorem phase_keeps_masses :
    ∀ t, process.step joined .shiftPhase t →
      basisMasses t = basisMasses joined ∧ basisMasses joined = (1, 0, 0, 1) :=
  fun _ step =>
    ⟨(congrArg basisMasses (step_iff.mp step)).trans actual_phase_preserves_basis_masses.2,
     actual_phase_preserves_basis_masses.1⟩

theorem phase_changes_cross :
    ∀ t, process.step joined .shiftPhase t →
      summarize joined = ⟨1, 1, 0, 1⟩ ∧ summarize t = ⟨1, 1, 0, -1⟩ :=
  fun _ step =>
    ⟨retained_cross_distinguishes_change.1,
     (congrArg summarize (step_iff.mp step)).trans retained_cross_distinguishes_change.2⟩

/-- **The same interaction tells the phase-changed configuration apart.** -/
theorem interaction_tells_apart :
    (∀ t, Trace process joined [.interact] t → response (controlDensity t) = (4, 0, 4)) ∧
    (∀ t, Trace process joined [.shiftPhase, .interact] t →
      response (controlDensity t) = (0, 4, 4)) :=
  ⟨fun _ path => (congrArg (fun v => response (controlDensity v)) (trace_end path)).trans
      same_interaction_distinguishes_relation.1,
   fun _ path => (congrArg (fun v => response (controlDensity v)) (trace_end path)).trans
      same_interaction_distinguishes_relation.2⟩

/-- **No reading of the local pair carries the interaction step.** -/
theorem no_local_update :
    ¬ ∃ update : Matrix × Matrix → Matrix,
      ∀ v t, process.step v .interact t → update (localStates v) = controlDensity t :=
  fun ⟨update, carries⟩ =>
    no_local_pair_update ⟨update, carries joined _ (step_iff.mpr rfl), carries changed _ (step_iff.mpr rfl)⟩

/-- **The summary gives the response at the end of every trace of the process.** -/
theorem summary_response {v t : Joint} {word : List Event} (path : Trace process v word t) :
    response (decodeControl (word.foldl reducedNext (summarize v))) = response (controlDensity t) :=
  (every_finite_control_response_exact v word).trans
    (congrArg (fun m => response (controlDensity m)) (trace_end path).symm)

/-- **The summary omits the register.** Two configurations with one summary keep one summary at
the ends of their traces along every common word, yet their register densities differ. -/
theorem summary_omits_register :
    registerDensity (⟨⟨1, 0⟩, ⟨0, 0⟩⟩ : Joint) ≠ registerDensity ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ ∧
    ∀ (word : List Event) (t t' : Joint), Trace process ⟨⟨1, 0⟩, ⟨0, 0⟩⟩ word t →
      Trace process ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ word t' → summarize t = summarize t' :=
  ⟨summary_omits_other_relations.2, fun word _ _ path path' =>
    (congrArg summarize (trace_end path)).trans
      ((every_finite_word_exact _ word).trans
        ((congrArg (fun q => word.foldl reducedNext q) summary_omits_other_relations.1).trans
          ((every_finite_word_exact _ word).symm.trans
            (congrArg summarize (trace_end path')).symm)))⟩

end JointPhase

end Becoming
