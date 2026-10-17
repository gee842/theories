import Becoming.Bridge

/-!
# The outcomes of one move from a configuration

`PracticalReach` states laws of a relation from responses to outcomes: which goals a response
guarantees, which goals some response can ensure, and when one relation refines another.
`Becoming.Bridge` proves that a guarantee is one-step completion (`guarantees_iff_completes`):
the relation is the step of a process from a configuration, its responses the labels and its
outcomes the next configurations. This module reads the relation off a process that way. One move
from `s` completes a goal where it is enabled and every next configuration meets it (the core's
`Completes` on a one-move word); `Ensures P s goal` says some move does. The moves of `Q` at `t`
cover those of `P` at `s` where every enabled move of `P` at `s` is matched by an enabled move of
`Q` at `t` whose outcomes are among its own (`Covers`), and they do exactly where every goal that
one move of `P` from `s` completes, one move of `Q` from `t` completes (`covers_iff`).

* **Laws of every process.** Completion by one move carries to every weaker goal
  (`completes_mono`); where some move of `P` is enabled at `s` and `Q` at `t` covers it, some goal
  is ensured by both (`common_goal`); no process ensures every goal that another does not
  (`no_strict_gain_everywhere`); revisions of a process each covering the last cover the first at
  every stage (`covers_along`); a goal on a summary of the outcomes is ensured exactly where its
  pullback is (`summary_iff`).
* **Four processes on two configurations.** The constant law sending every configuration to
  `false` (`toFalse`), the free process whose move may go anywhere (`free`), the setting process
  whose move names the next configuration (`setting`) and the halted process with no move
  (`halted`) witness that more possible outcomes need not cover (`free_wider_not_covering`), that
  covering can remove a possibility (`law_covers_free_and_loses`), that a cover can ensure a new
  goal (`setting_covers_and_gains`) and open what was closed (`setting_covers_and_opens`), that
  goals ensured separately need not be ensured jointly (`setting_separate_not_joint`), that where
  no move is enabled nothing is ensured though every outcome meets every goal
  (`halted_ensures_nothing`), and that a summary can hide a loss (`summary_hides_loss`).
* **Common responses.** A common response for a belief completes from every configuration the
  belief holds (`common_completes`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

namespace MoveOutcomeProcesses

section Laws

variable {S A B : Type}

/-- Some one move of `P` from `s` completes `goal`. -/
def Ensures (P : Process S A) (s : S) (goal : S → Prop) : Prop :=
  ∃ a, Completes P (fun _ _ _ => True) goal s [a]

/-- The moves of `Q` at `t` cover those of `P` at `s`: every enabled move of `P` at `s` is matched
by an enabled move of `Q` at `t` whose outcomes are among its own. -/
def Covers (P : Process S A) (s : S) (Q : Process S B) (t : S) : Prop :=
  PracticalReach.Refines (fun a o => P.step s a o) (fun b o => Q.step t b o)

/-- What some response of the step relation from `s` can ensure is what one move completes. -/
theorem canEnsure_iff {P : Process S A} {s : S} {goal : S → Prop} :
    PracticalReach.CanEnsure (fun a o => P.step s a o) goal ↔ Ensures P s goal :=
  ⟨fun ⟨a, g⟩ => ⟨a, (guarantees_iff_completes P s a goal).mp g⟩,
   fun ⟨a, c⟩ => ⟨a, (guarantees_iff_completes P s a goal).mpr c⟩⟩

/-- The cover in the core's terms: every enabled move of `P` at `s` has an enabled move of `Q` at
`t` with no further outcome. -/
theorem covers_iff_moves {P : Process S A} {s : S} {Q : Process S B} {t : S} :
    Covers P s Q t ↔
      ∀ a, Enabled P s a → ∃ b, Enabled Q t b ∧ ∀ o, Q.step t b o → P.step s a o :=
  Iff.rfl

/-- **Exactly.** The moves of `Q` at `t` cover those of `P` at `s` exactly where every goal one move
of `P` from `s` completes, one move of `Q` from `t` completes. -/
theorem covers_iff {P : Process S A} {s : S} {Q : Process S B} {t : S} :
    Covers P s Q t ↔ ∀ goal, Ensures P s goal → Ensures Q t goal :=
  (PracticalReach.refinement_iff_all_goal_preservation _ _).trans
    ⟨fun all goal ensured => canEnsure_iff.mp (all goal (canEnsure_iff.mpr ensured)),
     fun all goal ensured => canEnsure_iff.mpr (all goal (canEnsure_iff.mp ensured))⟩

/-- **A move completing a goal completes every weaker goal.** -/
theorem completes_mono {P : Process S A} {s : S} {a : A} {g h : S → Prop}
    (completes : Completes P (fun _ _ _ => True) g s [a]) (weaker : ∀ o, g o → h o) :
    Completes P (fun _ _ _ => True) h s [a] :=
  (guarantees_iff_completes P s a h).mp
    (PracticalReach.guarantee_mono ((guarantees_iff_completes P s a g).mpr completes) weaker)

/-- **Where some move is enabled and another process's moves cover it, some goal is ensured by
both.** -/
theorem common_goal {P : Process S A} {s : S} {Q : Process S B} {t : S}
    (enabled : ∃ a, Enabled P s a) (covers : Covers P s Q t) :
    ∃ goal, Ensures P s goal ∧ Ensures Q t goal :=
  match PracticalReach.common_goal_prevents_everywhere_strict enabled covers with
  | ⟨goal, here, there⟩ => ⟨goal, canEnsure_iff.mp here, canEnsure_iff.mp there⟩

/-- **No process ensures every goal that another does not.** -/
theorem no_strict_gain_everywhere (P : Process S A) (s : S) (Q : Process S B) (t : S) :
    ¬ ∀ goal, Ensures Q t goal ∧ ¬ Ensures P s goal :=
  fun all => PracticalReach.no_strict_improvement_for_every_goal
    (fun a o => P.step s a o) (fun b o => Q.step t b o)
    (fun goal => ⟨canEnsure_iff.mpr (all goal).1, fun e => (all goal).2 (canEnsure_iff.mp e)⟩)

/-- **Revisions of a process, each covering the last, cover the first at every stage.** The labels
may change at every revision. -/
theorem covers_along {L : Nat → Type} (P : (n : Nat) → Process S (L n)) (s : Nat → S)
    (each : ∀ n, Covers (P n) (s n) (P (n + 1)) (s (n + 1))) :
    ∀ n, Covers (P 0) (s 0) (P n) (s n) :=
  PracticalReach.finite_revisions_preserve (fun n a o => (P n).step (s n) a o) each

/-- **A goal on a summary of the outcomes is ensured exactly where its pullback is.** -/
theorem summary_iff {T : Type} (f : S → T) (P : Process S A) (s : S) (goal : T → Prop) :
    PracticalReach.CanEnsure (PracticalReach.Project f (fun a o => P.step s a o)) goal ↔
      Ensures P s (fun o => goal (f o)) :=
  (PracticalReach.projected_goal_iff f _ goal).trans canEnsure_iff

/-- **A common response for a belief completes from every configuration the belief holds.** -/
theorem common_completes {R : Type} {P : Process S A} {safe : S → A → S → Prop}
    {goal : S → Prop} {response : R → List A} {belief : S → Prop} {r : R} {s : S}
    (common : CommonResponse P safe goal response belief r) (held : belief s) :
    Completes P safe goal s (response r) :=
  PracticalJudgment.robust_at_actual held ((commonResponse_is_robust P safe goal response belief r).mp common)

end Laws

/-! ## Four processes on two configurations -/

/-- The constant law: every configuration goes to `false`. -/
abbrev toFalse : Process Bool Unit := Law.process (fun _ => false)

/-- The free process: a move may go to any configuration. -/
def free : Process Bool Unit := ⟨fun _ _ _ => True⟩

/-- The setting process: a move names the next configuration. -/
def setting : Process Bool Bool := ⟨fun _ a o => o = a⟩

/-- The halted process: no move is enabled. -/
def halted : Process Bool Unit := ⟨fun _ _ _ => False⟩

/-- The step relations of the four processes, from every configuration, are the relations
`fixed`, `uncontrolled`, `selectable` and `absent` of `PracticalReach`. -/
theorem steps_eq (s : Bool) :
    (fun a o => toFalse.step s a o) = PracticalReach.fixed ∧
      (fun a o => free.step s a o) = PracticalReach.uncontrolled ∧
      (fun a o => setting.step s a o) = PracticalReach.selectable ∧
      (fun a o => halted.step s a o) = PracticalReach.absent :=
  ⟨rfl, rfl, rfl, rfl⟩

/-- **More possible outcomes need not cover.** From every configuration, every configuration the
constant law can go to the free process can go to, and the free process can go to `true`, which
the law cannot, yet the free process's moves do not cover the law's. -/
theorem free_wider_not_covering (s : Bool) :
    (∀ o, (∃ a, toFalse.step s a o) → ∃ a, free.step s a o) ∧
      ((∃ a, free.step s a true) ∧ ¬ ∃ a, toFalse.step s a true) ∧ ¬ Covers toFalse s free s :=
  PracticalReach.possible_enlargement_without_control

/-- **Covering can remove a possibility.** From every configuration, the constant law's moves cover
the free process's, and the free process can go to `true`, which the law cannot. -/
theorem law_covers_free_and_loses (s : Bool) :
    Covers free s toFalse s ∧ (∃ a, free.step s a true) ∧ ¬ ∃ a, toFalse.step s a true :=
  PracticalReach.guaranteed_control_can_remove_possibility

/-- **A cover can ensure a new goal.** From every configuration, the setting process's moves cover
the constant law's, and one of its moves completes reaching `true`, which no move of the law does. -/
theorem setting_covers_and_gains (s : Bool) :
    Covers toFalse s setting s ∧ Ensures setting s (fun o => o = true) ∧
      ¬ Ensures toFalse s (fun o => o = true) :=
  match PracticalReach.retained_control_and_strict_new_goal with
  | ⟨covers, gains, lacks⟩ =>
    ⟨covers, canEnsure_iff.mp gains, fun e => lacks (canEnsure_iff.mpr e)⟩

/-- **A cover can open what was closed.** From every configuration, the setting process's moves
cover the constant law's; the law cannot go to `true`, and that the setting process cannot is
refuted. -/
theorem setting_covers_and_opens (s : Bool) :
    Covers toFalse s setting s ∧ (¬ ∃ a, toFalse.step s a true) ∧
      ¬ ¬ ∃ a, setting.step s a true :=
  PracticalReach.outcome_goal_preservation_can_defeat_closure_goal

/-- **Goals ensured separately need not be ensured jointly.** From every configuration, one move of
the setting process completes reaching `false` and one reaching `true`, and no move completes
both. -/
theorem setting_separate_not_joint (s : Bool) :
    Ensures setting s (fun o => o = false) ∧ Ensures setting s (fun o => o = true) ∧
      ¬ Ensures setting s (fun o => o = false ∧ o = true) :=
  match PracticalReach.separate_guarantees_not_joint with
  | ⟨first, second, both⟩ =>
    ⟨canEnsure_iff.mp first, canEnsure_iff.mp second, fun e => both (canEnsure_iff.mpr e)⟩

/-- **Where no move is enabled, nothing is ensured.** At every configuration of the halted process
every outcome of its move meets the goal `false`, and no move completes it. -/
theorem halted_ensures_nothing (s : Bool) :
    (∀ o, halted.step s () o → o = false) ∧ ¬ Ensures halted s (fun o => o = false) :=
  match PracticalReach.empty_response_does_not_guarantee with
  | ⟨vacuous, lacks⟩ => ⟨vacuous, fun e => lacks (canEnsure_iff.mpr e)⟩

/-- **A summary can hide a loss.** From every configuration, read through the summary sending every
configuration to `false`, one move of the free process meets `false`; read whole, no move
completes `false`. -/
theorem summary_hides_loss (s : Bool) :
    Ensures free s (fun o => (fun _ : Bool => false) o = false) ∧
      ¬ Ensures free s (fun o => o = false) :=
  match PracticalReach.projection_can_hide_loss with
  | ⟨summary, lacks⟩ =>
    ⟨(summary_iff (fun _ : Bool => false) free s (fun o => o = false)).mp summary,
     fun e => lacks (canEnsure_iff.mpr e)⟩

end MoveOutcomeProcesses

end Becoming
