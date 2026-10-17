import Becoming.Coupling

/-!
# Move runs: where the moves of a run are formed

`Becoming.Coupling` states where a move is formed: through a reading of the configuration where it
goes alike across what the reading lumps (`Learning.Lumped`), by the part, the rest or only their
relation in a coupled whole (`coupled`), and what the record of one course fixes of it. Its record
laws are stated for any sequence of configurations `g` and of moves `m`. A run of any process is
such a pair, its configurations `r.state` and its moves `r.act`, and the course of a coupled whole
is a run of `coupled P Q form` whose move at each step is `form` of the joint configuration
(`Run.part`, `Run.rest`). This module states Coupling's laws of those runs, with no premise beyond
what each theorem names.

* **Formed through a reading, along a run.** Along a run of a coupled whole, its moves are formed
  through its configurations (`coupled_formed`); along a run of any process, moves formed through a
  reading of the configurations are formed through every reading telling apart as much
  (`formed_of_finer`), and through the reading that tells nothing apart exactly where the run takes
  one move throughout (`formed_const_iff`).
* **The part's, the rest's, the relation's, along a run.** Where the move is the part's, every run
  of the coupled whole takes the part's policy at the part's configuration (`part_policy`); where it
  is the rest's, the rest's policy (`rest_policy`); where it is both, every run takes one move at
  every step (`both_one_move`). Along a run of the coupled whole, where the part's configuration
  recurs with the move varied, the rest's configuration differs there (`rest_differs`).
* **What the record of a run fixes.** A run's moves are a law of its configurations exactly where
  some relation giving at most one move at each configuration gives every move of the run
  (`formed_iff_singleValued`); the run's reading is contained in every such relation
  (`reading_le_run`). On its first `N` steps, with equality of configurations decided, a policy of
  the configuration gives the run's moves exactly where they never differ at one configuration
  (`formed_upto_iff`), and, with equality of moves decided too, no policy does exactly where some
  configuration recurs with the move varied (`no_policy_upto_iff`).
* **The counterfactual's supplied moves.** Along a run of the standard model of a course with the
  act formed within (`closedBy` of `ExchangeLaw.stepBy`), the act of a law that reads nothing
  (`ExchangeLaw.ofMoves`) is formed through the stage alone (`ofMoves_formed_stage`).
* **The witnesses as runs.** A history is a run of the law it shows (`Shown.run`). The run of the
  part held still while the move alternates (`stillRun`) has moves formed through the rest's count
  and not through the part (`still_driven`); the run of period four (`parityRun`) has moves formed
  through neither side's configuration alone and through the joint configuration
  (`parity_neither_alone`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w u'

namespace MoveRuns

section Coupled

variable {S : Type u} {E : Type v} {A : Type w} {P : Process S A} {Q : Process E A}
  {form : S × E → A}

/-- **Along a run of a coupled whole, its moves are formed through its configurations.** -/
theorem coupled_formed (r : Run (coupled P Q form)) : Learning.Lumped r.state r.part.act :=
  fun i j same => lumped_id form (r.state i) (r.state j) same

/-- **Where the move is the part's, every run of the coupled whole takes the part's policy**: at
each step the move is `form` of the part's configuration with any one configuration of the rest. -/
theorem part_policy (own : PartForms form) (e₀ : E) (r : Run (coupled P Q form)) (n : Nat) :
    r.part.act n = form (r.part.state n, e₀) :=
  (partForms_iff e₀).mp own (r.state n)

/-- **Where the move is the rest's, every run of the coupled whole takes the rest's policy.** -/
theorem rest_policy (driven : RestForms form) (s₀ : S) (r : Run (coupled P Q form)) (n : Nat) :
    r.rest.act n = form (s₀, r.rest.state n) :=
  (restForms_iff s₀).mp driven (r.state n)

/-- **Where the move is both the part's and the rest's, the coupled whole takes one move**: every
two steps of every two runs take the same move. -/
theorem both_one_move (both : PartForms form ∧ RestForms form) (r r' : Run (coupled P Q form))
    (i j : Nat) : r.part.act i = r'.part.act j :=
  partForms_and_restForms_iff.mp both (r.state i) (r'.state j)

/-- **Along a run of the coupled whole, a move varied at one configuration of the part is varied
by the rest.** -/
theorem rest_differs (r : Run (coupled P Q form)) {i j : Nat}
    (same : r.part.state i = r.part.state j) (varied : r.part.act i ≠ r.part.act j) :
    r.rest.state i ≠ r.rest.state j :=
  rest_differs_of_varied (form := form) (p := r.part.state) (e := r.rest.state)
    (fun _ => rfl) same varied

end Coupled

section AnyProcess

variable {S : Type u} {A : Type w} {K : Type v} {K' : Type u'} {P : Process S A}

/-- **Along a run, moves formed through a reading are formed through every reading telling apart
at least as much.** -/
theorem formed_of_finer (r : Run P) {π : S → K} {π' : S → K'}
    (formed : Learning.Lumped (fun n => π (r.state n)) r.act)
    (finer : ∀ x x', π' x = π' x' → π x = π x') :
    Learning.Lumped (fun n => π' (r.state n)) r.act :=
  lumped_of_finer formed fun i j same => finer (r.state i) (r.state j) same

/-- **Along a run, through the reading that tells nothing apart, the moves are formed exactly where
the run takes one move throughout.** -/
theorem formed_const_iff (r : Run P) (k : K) :
    Learning.Lumped (fun _ => k) r.act ↔ ∀ i j, r.act i = r.act j :=
  lumped_const_iff k

/-- **A run's moves are a law of its configurations exactly where some relation giving at most one
move at each configuration gives every move of the run.** -/
theorem formed_iff_singleValued (r : Run P) :
    Learning.Lumped r.state r.act ↔
      ∃ R : S → A → Prop, Readout.SingleValued R ∧ ∀ n, R (r.state n) (r.act n) :=
  lumped_iff_singleValued

/-- **The reading of a run is contained in every relation giving its moves.** -/
theorem reading_le_run (r : Run P) {R : S → A → Prop} (gives : ∀ n, R (r.state n) (r.act n))
    {s : S} {a : A} : Readout.Reading r.state r.act s a → R s a :=
  reading_le gives

/-- **On the first `N` steps of a run, a policy of the configuration gives its moves exactly where
they never differ at one configuration**, with equality of configurations decided. -/
theorem formed_upto_iff [DecidableEq S] (r : Run P) (N : Nat) :
    (∀ i j, i < N → j < N → r.state i = r.state j → r.act i = r.act j) ↔
      ∃ policy : S → A, ∀ n, n < N → r.act n = policy (r.state n) :=
  lumped_upto_iff N

/-- **The record of a run excludes every policy exactly where a configuration recurs with the move
varied**, with equality of configurations and of moves decided. -/
theorem no_policy_upto_iff [DecidableEq S] [DecidableEq A] (r : Run P) (N : Nat) :
    (¬ ∃ policy : S → A, ∀ n, n < N → r.act n = policy (r.state n)) ↔
      ∃ i j, i < N ∧ j < N ∧ r.state i = r.state j ∧ r.act i ≠ r.act j :=
  Becoming.no_policy_upto_iff N

end AnyProcess

section Supplied

variable {F C : Type} {law : ExchangeLaw F C} {present : Nat → List F} {part : F → Bool}
  {u : Nat → F → C → Nat × Nat}

/-- **Along a run of the standard model of a course, moves supplied as a sequence are formed
through the stage alone.** With the act formed within by a law that reads nothing, two steps of
the run at the same stage take the same move. -/
theorem ofMoves_formed_stage
    (r : Run (closedBy (inputs (law.stepBy present part)) (ExchangeLaw.ofMoves u).policy)) :
    Learning.Lumped (fun n => (r.state (n + 1)).1.1) (fun n => (r.state (n + 1)).2) :=
  fun i j same =>
    (r.step i).2.trans
      ((ExchangeLaw.ofMoves_lumped_stage u (r.state (i + 1)).1 (r.state (j + 1)).1 same).trans
        (r.step j).2.symm)

end Supplied

/-! ## The witnesses as runs -/

/-- The run of a part held still while the rest counts and the move alternates. -/
def stillRun : Run (Shown (fun n : Nat => ((), n)) Coupling.alt) :=
  Shown.run (fun n : Nat => ((), n)) Coupling.alt

/-- **Along the run of a part held still while the move alternates, the moves are formed through
the rest's count and not through the part.** -/
theorem still_driven :
    ¬ Learning.Lumped (fun n => (stillRun.state n).1) stillRun.act ∧
      Learning.Lumped (fun n => (stillRun.state n).2) stillRun.act :=
  Still.driven

/-- The run of period four whose move is whether the part and the rest differ. -/
def parityRun : Run (Shown (fun n => (Parity.partCourse n, Parity.restCourse n)) Parity.move) :=
  Shown.run (fun n => (Parity.partCourse n, Parity.restCourse n)) Parity.move

/-- **Along the run of period four, the move is formed through neither side's configuration alone
and through the joint configuration.** -/
theorem parity_neither_alone :
    ¬ Learning.Lumped (fun n => (parityRun.state n).1) parityRun.act ∧
      ¬ Learning.Lumped (fun n => (parityRun.state n).2) parityRun.act ∧
      Learning.Lumped parityRun.state parityRun.act :=
  ⟨Parity.neither_alone.1, Parity.neither_alone.2.1, Parity.neither_alone.2.2.1⟩

end MoveRuns

end Becoming
