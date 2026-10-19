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

Declarations moved here unchanged, with their names, from `Becoming.Counterfactual` (board item W):
see the sections so headed.
-/

/-! ## Laws of exchange along runs (moved from `Becoming.Counterfactual`) -/

namespace Becoming

open Generative

variable {F C : Type}

section Inputs

/-- **An act not taken is an intervention.** Where a run of the standard model of the course has
not taken the part's move `a` at `x` before `t`, the record up to `t` fixes no outcome of that move
there, while the model fixes it: P53's and P68's laws, read of acts. -/
theorem ExchangeLaw.act_not_taken {law : ExchangeLaw F C} {present : Nat → List F}
    {part : F → Bool} (r : Run (inputs (law.stepBy present part))) {t : Nat}
    {x : Nat × (Nat → C → Nat)} {a : F → C → Nat × Nat} (untaken : ¬ r.Takes t x (a, ())) :
    (¬ ∃ w, r.Fixes t x (a, ()) w) ∧
      (inputs (law.stepBy present part)).step x (a, ()) (law.stepBy present part x a ()) :=
  ⟨inputs_intervention_unfixed r untaken (y := (0, fun _ _ => 0)) (z := (1, fun _ _ => 0))
      fun same => Nat.zero_ne_one (congrArg Prod.fst same),
   (inputs_model_fixes _ x a ()).1⟩

end Inputs

section Unfolding

/-- **It runs by its relata's exchanges.** Under a law of what has stood, the levels of the course
run by the law of exchange (`Becoming.Unfolding`), its moves the relata's exchanges, exactly where
the course is feasible. -/
theorem ExchangeLaw.world_exchange_iff {R : Type} {law : ExchangeLaw R R}
    (na : law.Nonanticipating) (present : Nat → List R) (start : R → Nat) (W : Web R R) :
    (∀ t, (exchange R).step (law.levels present start t) ((law.world present start W).move t)
        (law.levels present start (t + 1))) ↔
      law.Feasible present start :=
  (law.world present start W).balances_iff_exchange.symm.trans
    (ExchangeLaw.course_balances_iff (present := present) (start := start) na W)

/-- The course, where feasible, as a run of the law of exchange. -/
def ExchangeLaw.worldRun {R : Type} {law : ExchangeLaw R R} (na : law.Nonanticipating)
    {present : Nat → List R} {start : R → Nat} (W : Web R R)
    (feasible : law.Feasible present start) : Run (exchange R) :=
  (law.world present start W).exchangeRun
    ((ExchangeLaw.course_balances_iff (present := present) (start := start) na W).mpr feasible)

/-- **What a determined law adds to a history is exactly the moves the history never takes.** A
determined law steps from `s` by `a` beyond what a run of it shows (`Shown`) exactly where it
steps there at all and the run never takes `a` at `s`. -/
theorem Run.beyond_shown_iff {S A : Type} {P : Process S A} (determined : Determined P)
    (r : Run P) {s : S} {a : A} :
    (∃ t, P.step s a t ∧ ¬ (Shown r.state r.act).step s a t) ↔
      (∃ t, P.step s a t) ∧ ¬ ∃ n, r.state n = s ∧ r.act n = a :=
  ⟨fun ⟨t, step, beyond⟩ =>
    ⟨⟨t, step⟩, fun ⟨n, at_s, by_a⟩ =>
      have there : P.step s a (r.state (n + 1)) := at_s ▸ by_a ▸ r.step n
      beyond ⟨n, at_s, by_a, (determined s a t (r.state (n + 1)) step there).symm⟩⟩,
   fun ⟨⟨t, step⟩, untaken⟩ =>
    ⟨t, step, fun ⟨n, at_s, by_a, _⟩ => untaken ⟨n, at_s, by_a⟩⟩⟩

/-- **The counterfactuals of a course are what its law adds to its history.** For a run of the
standard model of the course (the course an act generates is one, `ExchangeLaw.course_trajectory`),
the history shows a determined law (`Consistent`, `exists_law_iff`), and the part's move `a` at
`x` has a step of the model beyond what the history shows exactly where the history never takes
`a` at `x`. -/
theorem ExchangeLaw.counterfactual_beyond_shown {law : ExchangeLaw F C} {present : Nat → List F}
    {part : F → Bool} (r : Run (inputs (law.stepBy present part)))
    (x : Nat × (Nat → C → Nat)) (a : F → C → Nat × Nat) :
    Consistent r.state r.act ∧
      ((∃ t, (inputs (law.stepBy present part)).step x (a, ()) t ∧
          ¬ (Shown r.state r.act).step x (a, ()) t) ↔
        ¬ ∃ n, r.state n = x ∧ r.act n = (a, ())) :=
  ⟨exists_law_iff.mp ⟨_, inputs_determined _, r.step⟩,
   (Run.beyond_shown_iff (inputs_determined _) r).trans
     ⟨fun both => both.2, fun untaken => ⟨⟨_, rfl⟩, untaken⟩⟩⟩

/-- **With the act formed within, the course is the run P69's `closedBy` fixes.** A run of the
standard model of the course whose move is formed by `act` from the configuration, starting at
the starting levels, is at every step the course `law.withAct part act` generates. So two such
runs agree (`closedBy_runs_agree`): with the act formed within, the part acting otherwise is a
law of the part otherwise. -/
theorem ExchangeLaw.closedBy_course {law act : ExchangeLaw F C} {present : Nat → List F}
    {part : F → Bool} {start : C → Nat}
    (r : Run (closedBy (inputs (law.stepBy present part)) act.policy))
    (begins : r.state 0 = ((0, fun _ => start), act.policy (0, fun _ => start))) :
    ∀ n, (r.state n).1 = (n, (law.withAct part act).history present start n)
  | 0 => congrArg Prod.fst begins
  | n + 1 =>
    have formed : (r.state n).2 = act.policy (r.state n).1 :=
      match n with
      | 0 => (congrArg Prod.snd begins).trans (congrArg act.policy (congrArg Prod.fst begins)).symm
      | k + 1 => (r.step k).2
    (r.step n).1.trans
      ((congrArg (fun m => law.stepBy present part (r.state n).1 m.1 m.2) formed).trans
        (congrArg (fun x => law.stepBy present part x (act.policy x).1 ())
          (ExchangeLaw.closedBy_course r begins n)))

end Unfolding

end Becoming


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
