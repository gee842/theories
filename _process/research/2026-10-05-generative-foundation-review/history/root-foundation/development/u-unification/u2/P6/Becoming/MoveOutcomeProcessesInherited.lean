import Becoming.MoveOutcomeProcesses

/-!
# The outcomes of one move: the lost goal of a failed cover

`Becoming.MoveOutcomeProcesses` reads `PracticalReach`'s response relations off the step of a
process from a configuration and states its laws there with empty axiom reports. The converse
direction of its exact characterization, that a failed cover loses a goal, is proved in
`PracticalReach` by classical contradiction; this module states it of processes through that
theorem.

* **A failed cover loses a goal.** Where the moves of `Q` at `t` do not cover those of `P` at `s`,
  some goal one move of `P` from `s` completes no move of `Q` from `t` completes
  (`lost_goal_of_not_covers`).

No ethical predicate or ranking occurs. The axioms `propext`, `Classical.choice` and `Quot.sound` are
inherited from `PracticalReach.failed_refinement_has_lost_goal`; no axiom is added here.
-/

namespace Becoming

open Generative

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
