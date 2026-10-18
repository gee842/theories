import Becoming.Branching
import Becoming.Learnable
import Becoming.Parting

/-!
# Learnable runs: what a learner reading a run's registration can learn

`Becoming.Learnable` states what a learner reading a registration can learn along the orbit of a
determined law. A determined law is a process of the spine (`Law.process`), and every run of it is
its orbit from where the run begins (`Branching.law_run_state`); configurations of a determined
law are alike in the frame that registers `reg` exactly where their registered futures are the
same (`Law.alike_iff_sameFuture`). This module states the laws of `Becoming.Learnable` about the
runs of the law and the likeness of the frame, and proves them through those laws.

* **A run's registered record is its orbit's.** The record a learner reads along a run is the
  record along the orbit from the run's first configuration (`prefix_eq`), so a learner rests on
  a run exactly where it rests on that orbit (`restsFrom_iff`, `rests_iff`).
* **Alike in the frame, learned alike.** Two runs beginning at configurations alike in the frame
  that registers `reg` give every learner the same record at every step (`prefixes_same`); a
  learner resting on both has targets that agree from some step on (`agree_of_rests_both`), and
  where their targets differ at arbitrarily late steps no learner rests on both
  (`not_rests_on_both`).
* **What is read off the registration is learned along every run a list holds**
  (`rests_through`), by the learner over the lasso hypotheses given nothing.
* **Exactly.** In a world a list holds, some learner rests on the target along every run of the
  law exactly where runs beginning alike in the frame have targets that agree from some step on
  (`learnable_iff`); where the law leaves every configuration unchanged, exactly where the target
  goes alike across the registration (`still_learnable_iff_lumped`).

Readings of this as learning along a course of the unfolding, rather than about a configuration
set apart from it, belong to the study, not to this module. No ethical predicate, ranking or axiom
occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace LearnableRuns

section Along

variable {S : Type u} {R : Type v} {V : Type w} {next : S → S}

/-- The registered course of a run: what the registration registers at each of its steps
(`Parting.course` on a run of the law's process). -/
def course (reg : S → R) (r : Run (Law.process next)) : Nat → R := Parting.course reg r

/-- The learner `pred`, reading the registered record of the run, claims the target at every step
from `T` on. -/
def RestsFrom (reg : S → R) (val : S → V) (pred : List R → Option V) (r : Run (Law.process next))
    (T : Nat) : Prop :=
  ∀ t, T ≤ t → pred (Learning.prefixOf (course reg r) t) = some (val (r.state t))

/-- The learner comes to rest on the target along the run. -/
def Rests (reg : S → R) (val : S → V) (pred : List R → Option V) (r : Run (Law.process next)) :
    Prop :=
  ∃ T, RestsFrom reg val pred r T

/-- **A run's registered record is the record along the orbit from where it begins.** -/
theorem prefix_eq (reg : S → R) (r : Run (Law.process next)) (t : Nat) :
    Learning.prefixOf (course reg r) t = Learning.prefixOf (Learnable.course next reg (r.state 0)) t :=
  Learning.prefix_congr fun n _ => congrArg reg (Branching.law_run_state r n)

/-- **A learner rests on a run from `T` exactly where it rests from `T` on the orbit from where
the run begins.** -/
theorem restsFrom_iff {reg : S → R} {val : S → V} {pred : List R → Option V}
    (r : Run (Law.process next)) (T : Nat) :
    RestsFrom reg val pred r T ↔ Learnable.RestsFrom next reg val pred (r.state 0) T :=
  ⟨fun rests t late =>
    (congrArg pred (prefix_eq reg r t)).symm.trans
      ((rests t late).trans (congrArg (fun x => some (val x)) (Branching.law_run_state r t))),
   fun rests t late =>
    (congrArg pred (prefix_eq reg r t)).trans
      ((rests t late).trans (congrArg (fun x => some (val x)) (Branching.law_run_state r t)).symm)⟩

theorem rests_iff {reg : S → R} {val : S → V} {pred : List R → Option V}
    (r : Run (Law.process next)) :
    Rests reg val pred r ↔ Learnable.Rests next reg val pred (r.state 0) :=
  ⟨fun ⟨T, rests⟩ => ⟨T, (restsFrom_iff r T).mp rests⟩,
   fun ⟨T, rests⟩ => ⟨T, (restsFrom_iff r T).mpr rests⟩⟩

/-- Runs beginning alike in the frame that registers `reg` have the same registered future along
the runs. -/
theorem course_same {reg : S → R} {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    (n : Nat) : reg (r.state n) = reg (r'.state n) :=
  (congrArg reg (Branching.law_run_state r n)).trans
    ((Law.alike_iff_sameFuture.mp alike n).trans
      (congrArg reg (Branching.law_run_state r' n)).symm)

/-- **Runs beginning alike in the frame give every learner the same record.** -/
theorem prefixes_same {reg : S → R} {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    (t : Nat) : Learning.prefixOf (course reg r) t = Learning.prefixOf (course reg r') t :=
  Learning.prefix_congr fun n _ => course_same alike n

/-- **A learner resting on two runs beginning alike in the frame has targets that agree from some
step on.** -/
theorem agree_of_rests_both {reg : S → R} {val : S → V} {pred : List R → Option V}
    {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    {T T' : Nat} (rests : RestsFrom reg val pred r T) (rests' : RestsFrom reg val pred r' T') :
    ∀ t, T + T' ≤ t → val (r.state t) = val (r'.state t) :=
  fun t late =>
    (congrArg val (Branching.law_run_state r t)).trans
      ((Learnable.agree_of_rests_both (Law.alike_iff_sameFuture.mp alike)
          ((restsFrom_iff r T).mp rests) ((restsFrom_iff r' T').mp rests') t late).trans
        (congrArg val (Branching.law_run_state r' t)).symm)

/-- **Where the targets of two runs beginning alike in the frame differ at arbitrarily late steps,
no learner rests on both.** -/
theorem not_rests_on_both {reg : S → R} {val : S → V} (pred : List R → Option V)
    {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    (differ : ∀ T, ∃ t, T ≤ t ∧ val (r.state t) ≠ val (r'.state t)) :
    ¬ (Rests reg val pred r ∧ Rests reg val pred r') :=
  fun ⟨rests, rests'⟩ =>
    Learnable.not_rests_on_both pred (Law.alike_iff_sameFuture.mp alike)
      (fun T => match differ T with
        | ⟨t, late, ne⟩ => ⟨t, late, fun same => ne
            ((congrArg val (Branching.law_run_state r t)).trans
              (same.trans (congrArg val (Branching.law_run_state r' t)).symm))⟩)
      ⟨(rests_iff r).mp rests, (rests_iff r').mp rests'⟩

end Along

section Through

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

/-- **What is read off the registration is learned along every run a list holds**, by the learner
over the lasso hypotheses on the registered values, given nothing, from `Becoming.Identification`'s
bound on. -/
theorem rests_through (r : Run (Law.process next)) {l : List S} (held : ∀ n, r.state n ∈ l)
    {reg : S → R} {val : S → V} {g : R → V} (factors : ∀ s, val s = g (reg s)) :
    RestsFrom reg val (fun x => (Learning.byElimination Learning.lassos x).map g) r
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  (restsFrom_iff r _).mpr
    (Learnable.rests_through
      (fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state r n) (held n))
      factors)

end Through

section Exactly

variable {S : Type} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

/-- **Exactly.** In a world a list holds, some learner rests on the target along every run of the
law exactly where runs beginning alike in the frame that registers `reg` have targets that agree
from some step on. -/
theorem learnable_iff {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Rests reg val pred r) ↔
      ∀ r r' : Run (Law.process next),
        Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0) →
          ∃ T, ∀ t, T ≤ t → val (r.state t) = val (r'.state t) :=
  ⟨fun ⟨_, rests⟩ r r' alike =>
    match rests r, rests r' with
    | ⟨_, at_r⟩, ⟨_, at_r'⟩ => ⟨_, agree_of_rests_both alike at_r at_r'⟩,
   fun agree =>
    match (Learnable.learnable_iff (next := next) (reg := reg) (val := val) world).mpr
        (fun s s' same => agree (Law.run next s) (Law.run next s')
          (Law.alike_iff_sameFuture.mpr same)) with
    | ⟨pred, rests⟩ => ⟨pred, fun r => (rests_iff r).mpr (rests (r.state 0))⟩⟩

/-- **Where the law leaves every configuration unchanged, a target is learnable along every run
exactly where it goes alike across the registration.** -/
theorem still_learnable_iff_lumped (still : ∀ s, next s = s) {reg : S → R} {val : S → V}
    {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Rests reg val pred r) ↔
      Learning.Lumped reg val :=
  ⟨fun ⟨pred, rests⟩ => (Learnable.still_learnable_iff_lumped still world).mp
      ⟨pred, fun s => (rests_iff (Law.run next s)).mp (rests (Law.run next s))⟩,
   fun lumped => match (Learnable.still_learnable_iff_lumped still world).mpr lumped with
    | ⟨pred, rests⟩ => ⟨pred, fun r => (rests_iff r).mpr (rests (r.state 0))⟩⟩

end Exactly

end LearnableRuns

end Becoming
