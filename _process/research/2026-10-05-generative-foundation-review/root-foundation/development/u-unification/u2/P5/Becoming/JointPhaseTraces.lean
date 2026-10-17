import Becoming.Assurance
import RelationalReduction

/-!
# The phase and interaction steps of one joint configuration, as traces

`RelationalReduction` states, for a supplied two-part configuration (`OperativeCoherence.Joint`) and
its law of change `RelationalReduction.next` (two moves: the interaction, a controlled-X, and the
phase step), that the phase step changes the joint configuration while both local states and the basis masses
stay fixed, that the same later interaction then gives a different response, and that no update of
the pair of local states gives the control density after the interaction. A law of change is a
process of the spine (`Assurance.ofMap`). This module states those facts of the traces of the
process `Assurance.ofMap RelationalReduction.next` and proves them through the periphery's theorems.

* **A trace of the process ends where the law evolves** along its word (`trace_end`,
  `evolve_trace`).
* **The interaction step forms the joined configuration** from the blank preparation
  (`interaction_forms_joined`).
* **The phase step keeps both local states and the basis masses** (`phase_keeps_local_states`,
  `phase_keeps_masses`), **and changes the retained cross contribution** (`phase_changes_cross`).
* **The same interaction tells the two apart**: after the course `[interact]` from the joined
  configuration the response is `(4, 0, 4)`, after `[shiftPhase, interact]` it is `(0, 4, 4)`
  (`interaction_tells_apart`).
* **No reading of the pair of local states carries the interaction step**: no update of the local
  states gives the control density after every interaction step of the process
  (`no_local_update`).

The configurations, operations and their physical reading are supplied by the periphery; nothing
here derives them. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace JointPhaseTraces

open Generative.OperativeCoherence Generative.RelationalReduction

/-- The law of change of the joint configuration, read as a process. -/
abbrev process : Process Joint Event := Assurance.ofMap RelationalReduction.next

/-- A step of the process is the law of change. -/
theorem step_iff {s t : Joint} {a : Event} : process.step s a t ↔ t = RelationalReduction.next s a :=
  Iff.rfl

/-- **The trace of the process along a word ends where the law evolves along it**
(`SystemsOrganization.evolve`). -/
theorem trace_end : ∀ {v t : Joint} {word : List Event}, Trace process v word t →
    t = SystemsOrganization.evolve RelationalReduction.next v word
  | _, _, _, .nil _ => rfl
  | _, _, _, .cons step rest =>
    (trace_end rest).trans
      (congrArg (fun m => SystemsOrganization.evolve RelationalReduction.next m _) (step_iff.mp step))

/-- **Along every word the process has a trace**, ending where the law evolves along it. -/
theorem evolve_trace : ∀ (v : Joint) (word : List Event),
    Trace process v word (SystemsOrganization.evolve RelationalReduction.next v word)
  | v, [] => .nil v
  | v, a :: rest => .cons (step_iff.mpr rfl) (evolve_trace (RelationalReduction.next v a) rest)

/-- **The interaction step forms the joined configuration from the blank preparation.** -/
theorem interaction_forms_joined :
    process.step (hControl (blankControl basisZero)) .interact joined :=
  step_iff.mpr formation_from_blank.symm

/-- **The phase step from the joined configuration keeps both local states.** -/
theorem phase_keeps_local_states :
    ∀ t, process.step joined .shiftPhase t → localStates t = localStates joined :=
  fun _ step => (congrArg localStates (step_iff.mp step)).trans actual_phase_preserves_both_local_states.2

/-- **The phase step from the joined configuration keeps the basis masses**, which are
`(1, 0, 0, 1)`. -/
theorem phase_keeps_masses :
    ∀ t, process.step joined .shiftPhase t →
      basisMasses t = basisMasses joined ∧ basisMasses joined = (1, 0, 0, 1) :=
  fun _ step =>
    ⟨(congrArg basisMasses (step_iff.mp step)).trans actual_phase_preserves_basis_masses.2,
     actual_phase_preserves_basis_masses.1⟩

/-- **The phase step from the joined configuration changes the retained cross contribution**
from `1` to `-1`. -/
theorem phase_changes_cross :
    ∀ t, process.step joined .shiftPhase t →
      summarize joined = ⟨1, 1, 0, 1⟩ ∧ summarize t = ⟨1, 1, 0, -1⟩ :=
  fun _ step =>
    ⟨retained_cross_distinguishes_change.1,
     (congrArg summarize (step_iff.mp step)).trans retained_cross_distinguishes_change.2⟩

/-- **The same interaction tells the phase-changed configuration apart.** From the joined
configuration, the course `[interact]` ends where the response is `(4, 0, 4)`, and the course
`[shiftPhase, interact]` ends where it is `(0, 4, 4)`. -/
theorem interaction_tells_apart :
    (∀ t, Trace process joined [.interact] t → response (controlDensity t) = (4, 0, 4)) ∧
    (∀ t, Trace process joined [.shiftPhase, .interact] t →
      response (controlDensity t) = (0, 4, 4)) :=
  ⟨fun _ path =>
    (congrArg (fun v => response (controlDensity v)) (step_iff.mp (trace_singleton_iff.mp path))).trans
      same_interaction_distinguishes_relation.1,
   fun _ path => match trace_cons_iff.mp path with
    | ⟨_, first, rest⟩ =>
      have last := step_iff.mp (trace_singleton_iff.mp rest)
      (congrArg (fun v => response (controlDensity v))
          (last.trans (congrArg (fun v => RelationalReduction.next v .interact) (step_iff.mp first)))).trans
        same_interaction_distinguishes_relation.2⟩

/-- **No reading of the pair of local states carries the interaction step**: no update of the
local states gives the control density after every interaction step of the process. -/
theorem no_local_update :
    ¬ ∃ update : Matrix × Matrix → Matrix,
      ∀ v t, process.step v .interact t → update (localStates v) = controlDensity t :=
  fun ⟨update, carries⟩ =>
    no_local_pair_update
      ⟨update, carries joined _ (step_iff.mpr rfl), carries changed _ (step_iff.mpr rfl)⟩

end JointPhaseTraces

end Becoming
