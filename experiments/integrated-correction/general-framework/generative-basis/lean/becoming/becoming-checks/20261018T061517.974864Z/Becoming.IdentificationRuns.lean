import Becoming.LearningRuns
import Becoming.Courses

/-!
# Identification along runs: the states of a run and what a bounded record fixes

`Becoming.Description` reads states off one registered history (`SameAhead`, `StatesBelow`) and
states what a description of parts keeps and loses (`Separated`, `Rectangular`);
`Becoming.Identification` states what a bound on the states adds: a record of `N + N' - 1` steps
fixes the history, the learner given the bound is right from there, Moore's bound holds within one
history. A course read along a run of any process is its registered course (`Parting.course`),
every course is the registered course of a run of free branching (`Parting.freeRun`), every run of
a determined law is its orbit (`Branching.law_run_state`), and a whole of parts reached by a law's
courses is `Courses.reachedFrom`. This module states those laws of runs and of reached wholes.

* **The states of a run.** Two moments of a run of a determined law are one state exactly where
  their configurations are alike in the frame that registers `reg` (`sameAhead_iff_alike`). A run
  whose start returns has two moments that are one state (`returns_states`); a run registering
  every moment differently has each moment as its own state (`new_each`); a run's registered
  course has finitely many states exactly where it repeats from some step (`states_iff_lasso`).
  Along the run of negation from `true` there are exactly two states (`negation_two_states`), each
  defined through the other (`negation_each_through_other`).
* **A bounded record fixes a run's course, exactly.** Two runs of any process with at most `N` and
  `N'` states that register alike before `N + N' - 1` register alike at every step
  (`prefix_fixes`); for every `T` two runs of free branching with one state and with `T + 1` part
  at `T` (`prefix_short`). Two moments of a run with at most `N` states are one state exactly where
  what is registered from them agrees for `N + N - 1` steps (`sameAhead_iff_below`), and for
  `N - 1` steps, with the values decided (`sameAhead_iff_classes`) or with no premise
  (`sameAhead_iff_within`). Moore's bound is exact on runs: for every `M` two runs of a law on
  `M + 2` positions part at `M` (`classes_exact_runs`); before Moore's step, agreement of two runs
  of a law on a list closed under it is refuted by nothing (`classes_unrefuted_runs`).
* **Learners along runs.** The learner given the bound is refuted at no step of a run with at most
  `N` states (`withBound_accords`); no learner can always speak sooner on runs of free branching
  (`withBound_earliest`), and being given the bound buys silence, not an earlier rest
  (`rest_without_bound_missed`). On a run whose registered course repeats, the learner over the
  lasso hypotheses is right from a step that is found (`rests_of_lasso`), a step no earlier than
  cubic in the bound (`byElimination_rest_cubic`). Along the run of negation from `true` the learner
  given two states is right from step `3` (`negation_derived`). The run of the law answering the
  learner given `N` has more than `N` states (`answer_exceeds_bound`).
* **What a description of parts keeps along courses.** Of the whole a law's courses reach,
  describing each part by itself keeps every reached combination (`separated_of_reached`) and
  adds none exactly where the reached whole is rectangular (`separation_faithful_iff_reached`).
  After one move of copying the first part into the second, the parts always go alike and,
  described separately, could go apart (`copy_separation_admits_extra`). After one move of the law
  setting a third part to the parity of the first two (`parity`), the reached whole is the even
  triples (`parity_reached_iff`): every two parts are free in it and the three are not
  (`parity_whole_not_in_pairs`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace IdentificationRuns

open Learning

/-! ## Moments read through pointwise equal courses -/

section Congr

variable {O : Type u}

theorem sameAhead_congr {o o' : Nat → O} (same : ∀ n, o n = o' n) {t t' : Nat}
    (ahead : SameAhead o t t') : SameAhead o' t t' :=
  fun n => (same (t + n)).symm.trans ((ahead n).trans (same (t' + n)))

theorem statesBelow_congr {o o' : Nat → O} (same : ∀ n, o n = o' n) {N : Nat}
    (bound : StatesBelow o N) : StatesBelow o' N :=
  fun t => match bound t with
    | ⟨i, lt, ahead⟩ => ⟨i, lt, sameAhead_congr same ahead⟩

end Congr

/-! ## Along runs of any process -/

section AnyProcess

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- **Where a run registers every moment differently, each moment is its own state.** -/
theorem new_each {reg : S → R} {r : Run P}
    (new : ∀ t t', reg (r.state t) = reg (r.state t') → t = t') {t t' : Nat}
    (same : SameAhead (Parting.course reg r) t t') : t = t' :=
  SameAhead.new_each new same

/-- **A run's registered course has finitely many states exactly where it repeats from some
step.** -/
theorem states_iff_lasso (reg : S → R) (r : Run P) :
    (∃ L, StatesBelow (Parting.course reg r) L) ↔ ∃ i q, Lasso (Parting.course reg r) i q :=
  finitely_many_states_iff_lasso

/-- **A bounded record fixes a run's course.** Two runs whose registered courses have at most `N`
and `N'` states and which register alike before `N + N' - 1` register alike at every step. -/
theorem prefix_fixes {reg : S → R} {r r' : Run P} {N N' : Nat}
    (bound : StatesBelow (Parting.course reg r) N) (bound' : StatesBelow (Parting.course reg r') N')
    (agree : ∀ n, n < N + N' - 1 → reg (r.state n) = reg (r'.state n)) :
    ∀ n, reg (r.state n) = reg (r'.state n) :=
  Identification.prefix_fixes bound bound' (prefix_congr agree)

/-- **Two moments of a run with at most `N` states are one state exactly where what is
registered from them agrees for `N + N - 1` steps.** -/
theorem sameAhead_iff_below {reg : S → R} {r : Run P} {N : Nat}
    (bound : StatesBelow (Parting.course reg r) N) {t t' : Nat} :
    SameAhead (Parting.course reg r) t t' ↔
      ∀ n, n < N + N - 1 → reg (r.state (t + n)) = reg (r.state (t' + n)) :=
  Identification.sameAhead_iff_below bound

/-- **Moore's bound along a run, the values decided.** Two moments of a run with at most `N`
states are one state exactly where what is registered from them agrees for `N - 1` steps. -/
theorem sameAhead_iff_classes {reg : S → R} {r : Run P} {N : Nat}
    (bound : StatesBelow (Parting.course reg r) N)
    (values : ∀ n m, Decided (reg (r.state n) = reg (r.state m))) {t t' : Nat} :
    SameAhead (Parting.course reg r) t t' ↔
      ∀ n, n < N - 1 → reg (r.state (t + n)) = reg (r.state (t' + n)) :=
  Identification.sameAhead_iff_classes bound values

/-- **Moore's bound along a run, with no premise.** -/
theorem sameAhead_iff_within {reg : S → R} {r : Run P} {N : Nat}
    (bound : StatesBelow (Parting.course reg r) N) {t t' : Nat} :
    SameAhead (Parting.course reg r) t t' ↔
      ∀ n, n < N - 1 → reg (r.state (t + n)) = reg (r.state (t' + n)) :=
  Identification.sameAhead_iff_within bound

/-- **The learner given the bound is refuted at no step of a run with at most `N` states.** -/
theorem withBound_accords [DecidableEq R] {reg : S → R} {r : Run P} {N : Nat}
    (bound : StatesBelow (Parting.course reg r) N) :
    Accords (Identification.withBound N) (Parting.course reg r) :=
  Identification.withBound_accords bound

/-- **On a run whose registered course repeats, the learner over the lasso hypotheses comes to be
right at a step that is found.** -/
theorem rests_of_lasso [DecidableEq R] {reg : S → R} {r : Run P} {i q : Nat}
    (repeats : Lasso (Parting.course reg r) i q) :
    ∃ T, ∀ t, T ≤ t → Parting.RightAt (byElimination lassos) reg r t :=
  Identification.rests_of_lasso repeats

end AnyProcess

/-! ## Runs of free branching: the bounds are exact -/

section Free

variable {O : Type u}

/-- **The record before `T` does not fix a run's course.** Given two values, for every `T` two
runs of free branching, one with one state and one with at most `T + 1`, part at `T`. -/
theorem prefix_short {x y : O} (two : x ≠ y) (T : Nat) :
    ∃ q q' : Run (Parting.free O), StatesBelow (Parting.course id q) 1 ∧
      StatesBelow (Parting.course id q') (T + 1) ∧ Parting.PartAt id q q' T :=
  match Identification.prefix_short two T with
  | ⟨o, o', bound, bound', same, differ⟩ =>
    ⟨Parting.freeRun o, Parting.freeRun o', bound, bound',
     Identification.prefix_eq_iff.mp same, differ⟩

/-- **No learner can always speak sooner.** Given two values, no learner refuted at no step of
every run of free branching with at most `M + 2` states claims at step `M + M + 2` on each. -/
theorem withBound_earliest {x y : O} (two : x ≠ y) (pred : List O → Option O) (M : Nat) :
    ¬ ∀ q : Run (Parting.free O), StatesBelow (Parting.course id q) (M + 2) →
      Accords pred (Parting.course id q) ∧ ∃ w, pred (prefixOf (Parting.course id q) (M + M + 2)) = some w :=
  fun all => Identification.withBound_earliest two pred M fun o bound => all (Parting.freeRun o) bound

/-- **Being given the bound buys silence, not an earlier rest.** Given two values, no learner
right at step `1` on every run of free branching with one state is refuted at no step of every
such run with two states. -/
theorem rest_without_bound_missed {x y : O} (two : x ≠ y) (pred : List O → Option O) :
    ¬ ((∀ q : Run (Parting.free O), StatesBelow (Parting.course id q) 1 →
        Parting.RightAt pred id q 1) ∧
      ∀ q : Run (Parting.free O), StatesBelow (Parting.course id q) 2 →
        Accords pred (Parting.course id q)) :=
  fun ⟨right, holds⟩ => Identification.rest_without_bound_missed two pred
    ⟨fun o bound => right (Parting.freeRun o) bound, fun o bound => holds (Parting.freeRun o) bound⟩

/-- **The learner by refutation rests no earlier than a cubic step.** A step from which the
learner over the lasso hypotheses is right along every run of free branching on two values with
at most `N = 2m + 3` states comes after `(N³ - N) / 4`. -/
theorem byElimination_rest_cubic (m : Nat) {T : Nat}
    (rests : ∀ q : Run (Parting.free Bool), StatesBelow (Parting.course id q) (2 * m + 3) →
      ∀ t, T ≤ t → Parting.RightAt (byElimination lassos) id q t) :
    (2 * m + 3) * ((m + 1) * (m + 2)) < T :=
  Identification.byElimination_rest_cubic m fun o bound t late => rests (Parting.freeRun o) bound t late

/-- **A world answering its own learner exceeds the bound the learner is given.** Where `other`
moves every value, the run of the law answering the learner given `N` registers more than `N`
states. -/
theorem answer_exceeds_bound [DecidableEq O] {other : O → O} (moves : ∀ v, other v ≠ v) (x : O)
    (N : Nat) (r : Run (Law.process (answerStep (Identification.withBound N) other x)))
    (start : r.state 0 = []) :
    ¬ StatesBelow (Parting.course (LearningRuns.answerReg (Identification.withBound N) other x) r) N :=
  fun bound => Identification.answer_exceeds_bound moves x N
    (statesBelow_congr (LearningRuns.answer_course _ other x r start) bound)

end Free

/-! ## Along runs of a determined law -/

section Determined

variable {S : Type u} {R : Type w} {next : S → S}

/-- **Two moments of a run of a determined law are one state exactly where their configurations
are alike in the frame that registers `reg`.** -/
theorem sameAhead_iff_alike (reg : S → R) (r : Run (Law.process next)) {t t' : Nat} :
    SameAhead (Parting.course reg r) t t' ↔
      Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state t) (r.state t') :=
  have along : ∀ n, Parting.course reg r n = reg (Law.orbit next (r.state 0) n) :=
    fun n => congrArg reg (Branching.law_run_state r n)
  have at_t : ∀ n, reg (Law.orbit next (r.state t) n) =
      reg (Law.orbit next (Law.orbit next (r.state 0) t) n) :=
    fun n => congrArg (fun a => reg (Law.orbit next a n)) (Branching.law_run_state r t)
  have at_t' : ∀ n, reg (Law.orbit next (r.state t') n) =
      reg (Law.orbit next (Law.orbit next (r.state 0) t') n) :=
    fun n => congrArg (fun a => reg (Law.orbit next a n)) (Branching.law_run_state r t')
  ⟨fun same => Law.alike_iff_sameFuture.mpr fun n =>
      (at_t n).trans ((sameAhead_orbit_iff.mp (sameAhead_congr along same) n).trans (at_t' n).symm),
   fun alike => sameAhead_congr (fun n => (along n).symm)
      (sameAhead_orbit_iff.mpr fun n =>
        (at_t n).symm.trans ((Law.alike_iff_sameFuture.mp alike n).trans (at_t' n)))⟩

/-- **A run from a configuration that returns has two moments that are one state**, under every
registration. -/
theorem returns_states (r : Run (Law.process next)) (returns : Law.Returns next (r.state 0))
    (reg : S → R) : ∃ i j, i < j ∧ SameAhead (Parting.course reg r) i j :=
  match returns.states reg with
  | ⟨i, j, lt, same⟩ =>
    ⟨i, j, lt, sameAhead_congr (fun n => (congrArg reg (Branching.law_run_state r n)).symm) same⟩

/-- **Moore's bound before its step, refuted by nothing, along runs.** Two runs of a determined
law beginning in a list closed under it, registering alike for `N - 1` steps, `N` the list's
length: that they register alike at a step is refuted by nothing. -/
theorem classes_unrefuted_runs {reg : S → R} {l : List S} (closed : ∀ s, s ∈ l → next s ∈ l)
    {r r' : Run (Law.process next)} (mem : r.state 0 ∈ l) (mem' : r'.state 0 ∈ l)
    (agree : ∀ n, n < l.length - 1 → reg (r.state n) = reg (r'.state n)) (n : Nat) :
    ¬ ¬ reg (r.state n) = reg (r'.state n) :=
  fun differ => Law.sameFuture_classes_unrefuted (o := reg) closed mem mem'
    (fun k early => (congrArg reg (Branching.law_run_state r k)).symm.trans
      ((agree k early).trans (congrArg reg (Branching.law_run_state r' k))))
    n fun same => differ ((congrArg reg (Branching.law_run_state r n)).trans
      (same.trans (congrArg reg (Branching.law_run_state r' n)).symm))

end Determined

/-- **Moore's bound is exact on runs.** Given two values, for every `M` a law on a list of `M + 2`
positions closed under it, and a registration, have two runs, from `0` and from `1`, that part at
`M`. -/
theorem classes_exact_runs {R : Type w} {x y : R} (two : x ≠ y) (M : Nat) :
    ∃ (next : Nat → Nat) (reg : Nat → R) (l : List Nat), l.length = M + 2 ∧
      (∀ p, p ∈ l → next p ∈ l) ∧ 0 ∈ l ∧ 1 ∈ l ∧
      Parting.PartAt reg (Law.run next 0) (Law.run next 1) M :=
  match Law.sameFuture_classes_exact two M with
  | ⟨next, reg, l, length, closed, at0, at1, agree, differ⟩ =>
    ⟨next, reg, l, length, closed, at0, at1, agree, differ⟩

/-! ## The run of negation -/

section Negation

theorem negation_course (r : Run (Law.process not)) (start : r.state 0 = true) (n : Nat) :
    Parting.course id r n = Negation.course n :=
  (Branching.law_run_state r n).trans (congrArg (fun s => Law.orbit not s n) start)

/-- **Exactly two states along the run of negation from `true`.** -/
theorem negation_two_states (r : Run (Law.process not)) (start : r.state 0 = true) :
    (¬ SameAhead (Parting.course id r) 0 1) ∧ SameAhead (Parting.course id r) 0 2 ∧
      ∀ t, SameAhead (Parting.course id r) t 0 ∨ SameAhead (Parting.course id r) t 1 :=
  have along := negation_course r start
  have back : ∀ n, Negation.course n = Parting.course id r n := fun n => (along n).symm
  match Negation.two_states with
  | ⟨apart, same, each⟩ =>
    ⟨fun ahead => apart (sameAhead_congr along ahead), sameAhead_congr back same,
     fun t => match each t with
      | .inl first => .inl (sameAhead_congr back first)
      | .inr second => .inr (sameAhead_congr back second)⟩

/-- **Each state of the run of negation is defined through the other.** One registers `true` and
goes into the other, which registers `false` and goes into the first. -/
theorem negation_each_through_other (r : Run (Law.process not)) (start : r.state 0 = true)
    (t : Nat) :
    (SameAhead (Parting.course id r) t 0 →
        r.state t = true ∧ SameAhead (Parting.course id r) (t + 1) 1) ∧
      (SameAhead (Parting.course id r) t 1 →
        r.state t = false ∧ SameAhead (Parting.course id r) (t + 1) 0) :=
  have along := negation_course r start
  have back : ∀ n, Negation.course n = Parting.course id r n := fun n => (along n).symm
  ⟨fun ahead => match (Negation.each_through_other t).1 (sameAhead_congr along ahead) with
    | ⟨value, next⟩ => ⟨(along t).trans value, sameAhead_congr back next⟩,
   fun ahead => match (Negation.each_through_other t).2 (sameAhead_congr along ahead) with
    | ⟨value, next⟩ => ⟨(along t).trans value, sameAhead_congr back next⟩⟩

/-- **The liar's truth is derived along the run.** Along the run of negation from `true`, the
learner given that there are two states is right at every step from `3` on. -/
theorem negation_derived (r : Run (Law.process not)) (start : r.state 0 = true) :
    ∀ t, 3 ≤ t → Parting.RightAt (Identification.withBound 2) id r t :=
  fun t late =>
    (congrArg (Identification.withBound 2)
        (prefix_congr fun n _ => negation_course r start n)).trans
      ((Identification.negation_derived t late).trans
        (congrArg some (negation_course r start t).symm))

end Negation

/-! ## What a description of parts keeps along courses -/

section Separation

variable {A : Type u} {B : Type v}

theorem separated_congr {whole whole' : A × B → Prop} (same : ∀ p, whole p ↔ whole' p)
    {p : A × B} : Separated whole p → Separated whole' p :=
  fun ⟨⟨b, held⟩, ⟨a, held'⟩⟩ => ⟨⟨b, (same _).mp held⟩, ⟨a, (same _).mp held'⟩⟩

/-- **Describing each part by itself keeps every combination a law's courses reach.** -/
theorem separated_of_reached {next : A × B → A × B} {whole : A × B → Prop} {n : Nat} {p : A × B}
    (reached : Courses.reachedFrom next whole n p) :
    Separated (Courses.reachedFrom next whole n) p :=
  separated_of_whole reached

/-- **Describing the parts separately adds nothing to what a law's courses reach exactly where
the reached whole is rectangular.** -/
theorem separation_faithful_iff_reached {next : A × B → A × B} {whole : A × B → Prop} {n : Nat} :
    (∀ p, Separated (Courses.reachedFrom next whole n) p → Courses.reachedFrom next whole n p) ↔
      Rectangular (Courses.reachedFrom next whole n) :=
  separation_faithful_iff

end Separation

/-- **After copying, two parts that always go alike, described separately, could go apart.** One
move of the law copying the first part into the second reaches only parts going alike, and the
separate descriptions admit `(true, false)`, which is not reached. -/
theorem copy_separation_admits_extra :
    Separated (Courses.reachedFrom (fun p : Bool × Bool => (p.1, p.1)) (fun _ => True) 1)
        (true, false) ∧
      ¬ Courses.reachedFrom (fun p : Bool × Bool => (p.1, p.1)) (fun _ => True) 1 (true, false) :=
  match separation_admits_extra with
  | ⟨separated, apart⟩ =>
    ⟨separated_congr (fun p => (Courses.copy_relates_course.1 p).symm) separated,
     fun reached => apart ((Courses.copy_relates_course.1 _).mp reached)⟩

/-- The law setting the third part to the parity of the first two. -/
def parity (p : Bool × Bool × Bool) : Bool × Bool × Bool := (p.1, p.2.1, flipIf p.1 p.2.1)

/-- An even triple is left as it is by `parity`. -/
theorem parity_fixed : ∀ p : Bool × Bool × Bool, EvenThree p → parity p = p
  | (true, true, true), odd => nomatch odd
  | (true, true, false), _ => rfl
  | (true, false, true), _ => rfl
  | (true, false, false), odd => nomatch odd
  | (false, true, true), _ => rfl
  | (false, true, false), odd => nomatch odd
  | (false, false, true), odd => nomatch odd
  | (false, false, false), _ => rfl

/-- **One move of `parity` reaches exactly the even triples.** -/
theorem parity_reached_iff (p : Bool × Bool × Bool) :
    Courses.reachedFrom parity (fun _ => True) 1 p ↔ EvenThree p :=
  ⟨fun reached => match Courses.reachedFrom_succ.mp reached with
    | ⟨q, _, moved⟩ => Eq.subst (motive := EvenThree) moved (even_first q.1 q.2.1),
   fun even => Courses.reachedFrom_succ.mpr
    ⟨p, Courses.reachedFrom_zero.mpr trivial, parity_fixed p even⟩⟩

/-- **A relation the reached whole holds and no two parts hold.** After one move of `parity`,
every two of the three parts may be anything in the reached whole, and the three may not. -/
theorem parity_whole_not_in_pairs :
    (∀ x y : Bool, ∃ z, Courses.reachedFrom parity (fun _ => True) 1 (x, y, z)) ∧
      (∀ y z : Bool, ∃ x, Courses.reachedFrom parity (fun _ => True) 1 (x, y, z)) ∧
      (∀ x z : Bool, ∃ y, Courses.reachedFrom parity (fun _ => True) 1 (x, y, z)) ∧
      ¬ Courses.reachedFrom parity (fun _ => True) 1 (true, false, false) :=
  match whole_not_in_pairs with
  | ⟨first, second, third, odd⟩ =>
    ⟨fun x y => match first x y with
      | ⟨z, even⟩ => ⟨z, (parity_reached_iff _).mpr even⟩,
     fun y z => match second y z with
      | ⟨x, even⟩ => ⟨x, (parity_reached_iff _).mpr even⟩,
     fun x z => match third x z with
      | ⟨y, even⟩ => ⟨y, (parity_reached_iff _).mpr even⟩,
     fun reached => odd ((parity_reached_iff _).mp reached)⟩

end IdentificationRuns

end Becoming
