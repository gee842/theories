import Becoming.Runs

/-!
# The course of an act on runs of the standard model and on the course world

`Becoming.Counterfactual` states that the history a law of exchange generates where a part makes
given moves is the trajectory of the standard causal model whose input is the part's move
(`ExchangeLaw.course_trajectory`), and that the generated levels begin at the starting levels
(`ExchangeLaw.levels_zero`). The standard model is a process of the spine (`inputs`), and the
course a law of exchange generates is a world (`ExchangeLaw.courseWorld`, `Becoming.Runs`). This
module states those laws of the runs of the standard model and of the course world.

* **A run of the standard model is the trajectory of its moves** (`inputs_run_state`).
* **Every run of the standard model of the course is the generated history.** A run of the
  standard model of a course from the start is, at every stage, the history generated where the
  part makes the moves the run takes and the rest exchanges by the law (`course_runs`).
* **The course world begins at the starting levels** (`courseWorld_level_zero`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace CounterfactualRuns

/-- **A run of the standard model is the trajectory of its moves**: of its inputs and its noise,
from where it begins. -/
theorem inputs_run_state {X : Type u} {U : Type v} {E : Type w} {F : X → U → E → X}
    (r : Run (inputs F)) :
    ∀ n, r.state n = trajectory F (r.state 0) (fun k => (r.act k).1) (fun k => (r.act k).2) n
  | 0 => rfl
  | n + 1 => (r.step n).trans
      (congrArg (fun x => F x (r.act n).1 (r.act n).2) (inputs_run_state r n))

variable {F C : Type}

/-- **Every run of the standard model of a course is the generated history.** A run of the
standard model whose input is the part's move, from stage `0` at the starting levels, is at stage
`n` the history generated where the part makes the moves the run takes and the rest exchanges by
`law`. -/
theorem course_runs (law : ExchangeLaw F C) (present : Nat → List F) (part : F → Bool)
    {start : C → Nat} (r : Run (inputs (law.stepBy present part)))
    (begins : r.state 0 = (0, fun _ => start)) (n : Nat) :
    r.state n =
      (n, (law.withAct part (ExchangeLaw.ofMoves fun k => (r.act k).1)).history present start n) :=
  (inputs_run_state r n).trans
    ((congrArg (fun x => trajectory (law.stepBy present part) x (fun k => (r.act k).1)
        (fun k => (r.act k).2) n) begins).trans
      (ExchangeLaw.course_trajectory law present part start (fun k => (r.act k).1) n))

/-- **The course world begins at the starting levels.** -/
theorem courseWorld_level_zero {law : ExchangeLaw F C} {present : Nat → List F}
    {start : C → Nat} {W : Web F C} (c : C) :
    (law.courseWorld present start W).web.level 0 (.inr c) = start c :=
  (ExchangeLaw.courseWorld_level 0 c).trans (ExchangeLaw.levels_zero c)

end CounterfactualRuns

end Becoming
