import Becoming.MoveOutcomeProcesses
import Becoming.Bridge

/-!
# The outcomes of one move: `PracticalReach` read off a process, and the lost goal of a failed cover

`Becoming.MoveOutcomeProcesses` states, in the core, the laws of covering one move's outcomes.
`PracticalReach` states the same laws of a relation from responses to outcomes, and
`Becoming.Bridge` proves that a guarantee is one-step completion (`guarantees_iff_completes`):
the relation is the step of a process from a configuration, its responses the labels and its
outcomes the next configurations. This module reads `PracticalReach` that way, with the full
names it had when the join held it, and states through `PracticalReach` the one law the core
proves only in its constructive form.

* **Readings.** What some response of the step relation can ensure is what one move completes
  (`MoveOutcomeProcesses.canEnsure_iff`); a goal on a summary of the outcomes is ensured exactly
  where its pullback is (`MoveOutcomeProcesses.summary_iff`); the four processes' step relations
  are `PracticalReach`'s four relations (`MoveOutcomeProcesses.steps_eq`).
* **A failed cover loses a goal.** Where the moves of `Q` at `t` do not cover those of `P` at `s`,
  some goal one move of `P` from `s` completes no move of `Q` from `t` completes
  (`lost_goal_of_not_covers`).

No ethical predicate or ranking occurs. The readings have empty axiom reports. The axioms
`propext`, `Classical.choice` and `Quot.sound` of `lost_goal_of_not_covers` are inherited from
`PracticalReach.failed_refinement_has_lost_goal`; no axiom is added here.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

namespace MoveOutcomeProcesses

variable {S A : Type}

/-- What some response of the step relation from `s` can ensure is what one move completes. -/
theorem canEnsure_iff {P : Process S A} {s : S} {goal : S → Prop} :
    PracticalReach.CanEnsure (fun a o => P.step s a o) goal ↔ Ensures P s goal :=
  ⟨fun ⟨a, g⟩ => ⟨a, (guarantees_iff_completes P s a goal).mp g⟩,
   fun ⟨a, c⟩ => ⟨a, (guarantees_iff_completes P s a goal).mpr c⟩⟩

/-- **A goal on a summary of the outcomes is ensured exactly where its pullback is.** -/
theorem summary_iff {T : Type} (f : S → T) (P : Process S A) (s : S) (goal : T → Prop) :
    PracticalReach.CanEnsure (PracticalReach.Project f (fun a o => P.step s a o)) goal ↔
      Ensures P s (fun o => goal (f o)) :=
  (PracticalReach.projected_goal_iff f _ goal).trans canEnsure_iff

/-- The step relations of the four processes, from every configuration, are the relations
`fixed`, `uncontrolled`, `selectable` and `absent` of `PracticalReach`. -/
theorem steps_eq (s : Bool) :
    (fun a o => toFalse.step s a o) = PracticalReach.fixed ∧
      (fun a o => free.step s a o) = PracticalReach.uncontrolled ∧
      (fun a o => setting.step s a o) = PracticalReach.selectable ∧
      (fun a o => halted.step s a o) = PracticalReach.absent :=
  ⟨rfl, rfl, rfl, rfl⟩

end MoveOutcomeProcesses

namespace MoveOutcomeProcessesInherited

open MoveOutcomeProcesses

variable {S A B : Type}

/-- **A failed cover loses a goal.** Where the moves of `Q` at `t` do not cover those of `P` at
`s`, some goal one move of `P` from `s` completes no move of `Q` from `t` completes. -/
theorem lost_goal_of_not_covers {P : Process S A} {s : S} {Q : Process S B} {t : S}
    (fails : ¬ MoveOutcomeProcesses.Covers P s Q t) :
    ∃ goal, MoveOutcomeProcesses.Ensures P s goal ∧ ¬ MoveOutcomeProcesses.Ensures Q t goal :=
  match PracticalReach.failed_refinement_has_lost_goal fails with
  | ⟨goal, here, lacks⟩ => ⟨goal, canEnsure_iff.mp here, fun e => lacks (canEnsure_iff.mpr e)⟩

end MoveOutcomeProcessesInherited

end Becoming
