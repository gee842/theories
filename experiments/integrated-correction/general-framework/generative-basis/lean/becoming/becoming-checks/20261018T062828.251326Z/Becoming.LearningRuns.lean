import Becoming.LearnableRuns
import Becoming.Parting

/-!
# Learning along runs: what a run's registered record fixes and what a learner reaching it does

`Becoming.Learning` states, of any course of registered values, what a record fixes, what a
learner by refutation does on it, what the course answering a learner is, and what training
through data selects; `Becoming.Learnable` states what a learner reading a registration learns
along a determined law's orbit. A course read along a run of any process is its registered course
(`Parting.course`), every course is the registered course of a run of free branching
(`Parting.freeRun`), and every run of a determined law is its orbit
(`Branching.law_run_state`, `LearnableRuns`). This module states those laws of runs.

* **No record fixes the next value.** At a step where two runs of any process part (they register
  alike before it and apart at it, `Parting.PartAt`), a claim made from the record, the values
  decided, is refuted on one of them (`missed_on_one_of_part`). Every run's record is shared by
  two runs of free branching that repeat from that step on and register two given values there,
  and no claim from the record is right on both (`prefix_fixes_no_next`).
* **The answering law.** The course answering every claim of a learner is the registered course
  of a run of a determined law that keeps its record (`answerReg`, `answer_course`); no list holds
  its configurations (`answer_open`); with two values told apart every claim made along it is
  refuted (`answer_misses`); and the learner over every merging of classes of hypotheses never
  comes to rest along it (`merged_unrested`).
* **Learning by refutation along a run.** The learner is through the run's record
  (`byElimination_through_prefix`); every hypothesis it passed was refuted at an earlier step of the run
  (`missed_before`); over merged classes it holds no hypothesis beyond the place of one that
  holds along the run (`merged_bound`); where it is right from some step on along a run, the
  run's registered course repeats from some step (`lasso_of_right`).
* **Induction along a run held by a list.** On a run of a determined law whose configurations a
  list holds, the learner over the lasso hypotheses is refuted fewer than `tri l.length` times,
  claims from `l.length` on and is not refuted at arbitrarily late steps
  (`held_byElimination_bounded`); that it rests is unrefuted (`held_rest_unrefuted`). Along the run of
  negation from `false` it rests from step `3` (`alternate_rests`); negation never rests
  (`negation_never_rests`).
* **Generalization from a run.** Within the targets that go alike across a registration, their
  values at the configurations a run passed before `t` fix the value at a configuration exactly
  where it registers like one of them (`determines_iff_lumped_alike`); the value carried over
  is right exactly where the world takes one value at the two (`carried_right_iff`), as it does
  for a world going alike across the registration (`world_carried_right`).
* **Training on runs' records.** Read the registered courses of a process's runs as the class
  (`Courses`) and the moments before `t` as the data. A loss computed from the record selects
  alike runs registering alike before `t` (`loss_through_prefix`); within a class free beyond the
  record, a selection through it leaves the value at a later moment as free as the class does
  (`unselected_beyond_prefix`); and a fit to the record is right at a moment on every run exactly
  where the record determines it there (`fit_right_iff_runs`). Where runs branch freely, the
  record fixes no later value (`free_prefix_fixes_nothing`).
* **Alike in the frame, learned alike.** On runs of a determined law beginning alike in the frame
  that registers `reg`, a claim at a step where the targets differ is right on at most one
  (`claim_not_right_on_both`); with the targets decided it is refuted on one, the records equal at
  every step (`missed_on_one`). Along the runs of the law leaving two coordinates unchanged, no
  learner reading the first rests on the second at both `(true, false)` and `(true, true)`
  (`pair_first_not_rests`), none rests on it along every run (`pair_not_learnable`), and reading
  both, the learner over the lasso hypotheses rests on the second from step `2`
  (`pair_whole_rests`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w x

namespace LearningRuns

open Learning

/-! ## Refutation read through equal records -/

section Transport

variable {O : Type u}

/-- A refutation carries to an equal claim and an equal value. -/
theorem missed_congr {c c' : Option O} {w w' : O} (claim : c = c') (value : w = w') :
    Misses c w → Misses c' w' :=
  fun ⟨v, made, differs⟩ => ⟨v, claim.symm.trans made, fun same => differs (same.trans value.symm)⟩

/-- A refutation at a step carries to a course with the same record and value there. -/
theorem missedAt_of_same {V : Type v} {pred : List O → Option V} {o : Nat → O} {o' : Nat → O}
    {val val' : V} {t : Nat} (same : prefixOf o t = prefixOf o' t) (now : val = val') :
    Misses (pred (prefixOf o t)) val → Misses (pred (prefixOf o' t)) val' :=
  missed_congr (congrArg pred same) now

/-- Held from `t` at the value of `o'`, a course agreeing with `o'` before `t` is refuted at `t`
only where `o'` is. -/
theorem holdFrom_missed {pred : List O → Option O} {o o' : Nat → O} {t : Nat}
    (same : ∀ n, n < t → o n = o' n) :
    MissesAt pred (holdFrom o t (o' t)) t → MissesAt pred o' t :=
  missedAt_of_same
    (prefix_congr fun n before => (holdFrom_before o (o' t) before).trans (same n before))
    (holdFrom_after o (o' t) (Nat.le_refl t))

end Transport

/-! ## Along runs of any process -/

section AnyProcess

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- **At a parting, a claim from the record is refuted on one of the two runs.** With the
registered values decided, where two runs register alike before `t` and apart at `t`, a claim
made at `t` from the record is refuted on one of them. -/
theorem missed_on_one_of_part [DecidableEq R] (pred : List R → Option R) {reg : S → R}
    {r r' : Run P} {t : Nat} (part : Parting.PartAt reg r r' t) {w : R}
    (claims : pred (prefixOf (Parting.course reg r) t) = some w) :
    MissesAt pred (Parting.course reg r) t ∨ MissesAt pred (Parting.course reg r') t :=
  match claim_missed_on_one pred (Parting.course reg r) t part.2 claims with
  | .inl refuted => .inl (holdFrom_missed (fun _ _ => rfl) refuted)
  | .inr refuted => .inr (holdFrom_missed part.1 refuted)

/-- **No record of a run fixes the next value, not even among finite worlds.** Given two values,
the record of every run before `t` is the record of two runs of free branching that repeat from
`t` on, one registering each value at `t`; a claim made from the record is not right on both. -/
theorem prefix_fixes_no_next (pred : List R → Option R) (reg : S → R) (r : Run P) (t : Nat)
    {x y : R} (two : x ≠ y) {w : R} (claims : pred (prefixOf (Parting.course reg r) t) = some w) :
    ∃ q q' : Run (Parting.free R), Lasso (Parting.course id q) t 0 ∧
      Lasso (Parting.course id q') t 0 ∧
      prefixOf (Parting.course id q) t = prefixOf (Parting.course reg r) t ∧
      prefixOf (Parting.course id q') t = prefixOf (Parting.course reg r) t ∧
      q.state t = x ∧ q'.state t = y ∧
      ¬ (¬ MissesAt pred (Parting.course id q) t ∧ ¬ MissesAt pred (Parting.course id q') t) :=
  match no_prefix_fixes_next_finite pred (Parting.course reg r) t two claims with
  | ⟨lasso, lasso', same, same', one⟩ =>
    ⟨Parting.freeRun (holdFrom (Parting.course reg r) t x),
     Parting.freeRun (holdFrom (Parting.course reg r) t y), lasso, lasso', same, same',
     holdFrom_after _ x (Nat.le_refl t), holdFrom_after _ y (Nat.le_refl t), one⟩

/-- **The learner by refutation is through the run's record.** On two runs registering alike
before `t`, it holds the same hypothesis and makes the same claim at `t`. -/
theorem byElimination_through_prefix [DecidableEq R] (H : Nat → List R → Option R) {reg : S → R}
    {r r' : Run P} {t : Nat} (same : ∀ n, n < t → reg (r.state n) = reg (r'.state n)) :
    index H (Parting.course reg r) t = index H (Parting.course reg r') t ∧
      byElimination H (prefixOf (Parting.course reg r) t) = byElimination H (prefixOf (Parting.course reg r') t) :=
  Learning.byElimination_through_prefix (prefix_congr same)

/-- **Every hypothesis the learner passed along a run was refuted at an earlier step of the
run.** -/
theorem missed_before [DecidableEq R] {H : Nat → List R → Option R} {reg : S → R} {r : Run P}
    (t k : Nat) (below : k < index H (Parting.course reg r) t) :
    ∃ s, s < t ∧ index H (Parting.course reg r) s = k ∧ MissesAt (H k) (Parting.course reg r) s :=
  Learning.missed_before t k below

/-- **Learning over classes along a run.** Where hypothesis `j` of class `c` is refuted at no
step of the run's registered course, the learner over the merged classes holds no hypothesis
beyond place `tri (c + j) + j`. -/
theorem merged_bound [DecidableEq R] (G : Nat → Nat → List R → Option R) {reg : S → R}
    {r : Run P} {c j : Nat} (holds : Accords (G c j) (Parting.course reg r)) :
    ∀ t, index (merged G) (Parting.course reg r) t ≤ tri (c + j) + j :=
  Learning.merged_bound G holds

/-- **Where the learner over the lasso hypotheses is right from some step on along a run, the
run's registered course repeats from some step.** -/
theorem lasso_of_right [DecidableEq R] {reg : S → R} {r : Run P} {T : Nat}
    (right : ∀ t, T ≤ t → Parting.RightAt (byElimination lassos) reg r t) :
    ∃ i q, Lasso (Parting.course reg r) i q :=
  lasso_of_rest right

/-- **Generalization from a run.** Within the targets that go alike across the registration, the
values at the configurations a run passed before `t` fix the value at `s` exactly where `s`
registers like one of them, given two values. -/
theorem determines_iff_lumped_alike [DecidableEq R] {V : Type x} {reg : S → R} (r : Run P)
    (t : Nat) {s : S} {y z : V} (two : y ≠ z) :
    Determines (Lumped (V := V) reg) (· ∈ prefixOf r.state t) s ↔
      ∃ d, d ∈ prefixOf r.state t ∧ reg d = reg s :=
  determines_lumped_iff two

/-- **The value carried over from a run is right exactly where the world takes one value at the
two.** A target going alike across the registration and fitting the world `f` at the
configurations a run passed before `t` takes at `s` its value at a passed configuration `d`
registering like `s`; it is right at `s` exactly where `f` takes one value at `d` and `s`. -/
theorem carried_right_iff {V : Type x} {reg : S → R} {r : Run P} {t : Nat} {f g : S → V}
    {s d : S} (lumped : Lumped reg g) (fits : ∀ c, c ∈ prefixOf r.state t → g c = f c)
    (passed : d ∈ prefixOf r.state t) (same : reg d = reg s) : g s = f s ↔ f d = f s :=
  lumped_right_iff lumped fits passed same

/-- **A world going alike across the registration is learned from a run at every configuration
registering like one the run passed.** -/
theorem world_carried_right {V : Type x} {reg : S → R} {r : Run P} {t : Nat} {f g : S → V}
    {s d : S} (world : Lumped reg f) (lumped : Lumped reg g)
    (fits : ∀ c, c ∈ prefixOf r.state t → g c = f c) (passed : d ∈ prefixOf r.state t)
    (same : reg d = reg s) : g s = f s :=
  lumped_world_right world lumped fits passed same

end AnyProcess

/-! ## Training on the records of runs -/

section Training

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- The registered courses of the runs of `P`: the class a learner reading `reg` along the runs
can meet. -/
def Courses (P : Process S A) (reg : S → R) (g : Nat → R) : Prop :=
  ∃ r : Run P, ∀ n, g n = reg (r.state n)

/-- The registered course of every run is one of them. -/
theorem course_mem (reg : S → R) (r : Run P) : Courses P reg (Parting.course reg r) :=
  ⟨r, fun _ => rfl⟩

/-- **A loss computed from the record selects alike runs registering alike before `t`.** -/
theorem loss_through_prefix {L : Type x} {t : Nat} (loss : (Nat → R) → L)
    (on_data : ∀ g g', Training.AgreeOn (· < t) g g' → loss g = loss g') (choose : L → Prop)
    {reg : S → R} {r r' : Run P} (same : ∀ n, n < t → reg (r.state n) = reg (r'.state n)) :
    choose (loss (Parting.course reg r)) ↔ choose (loss (Parting.course reg r')) :=
  Training.loss_through loss on_data choose (Parting.course reg r) (Parting.course reg r') same

/-- **Training through the record leaves the later value as free as the runs leave it.** Where
the registered courses of `P` are free at `x` beyond the record before `t`, for every run whose
course a selection through the record selects and every run, a selected course of a run agrees
with the first on the record and takes the second's value at `x`. -/
theorem unselected_beyond_prefix {reg : S → R} {t x : Nat} {select : (Nat → R) → Prop}
    (through : Training.Through (Training.AgreeOn (· < t)) select)
    (free : Free (Courses P reg) (· < t) x) {r r' : Run P}
    (chosen : select (Parting.course reg r)) :
    ∃ h, Courses P reg h ∧ select h ∧ Training.AgreeOn (· < t) h (Parting.course reg r) ∧
      h x = reg (r'.state x) :=
  Training.unselected_beyond_data through free (course_mem reg r) (course_mem reg r') chosen

/-- **A fit to the record is right at a moment on every run exactly where the record determines
it.** Every two runs registering alike before `t` register alike at `x` exactly where, within the
registered courses of `P`, the record before `t` determines the value at `x`. -/
theorem fit_right_iff_runs {reg : S → R} {t x : Nat} :
    (∀ r r' : Run P, (∀ n, n < t → reg (r'.state n) = reg (r.state n)) →
      reg (r'.state x) = reg (r.state x)) ↔ Determines (Courses P reg) (· < t) x :=
  have to_runs : (∀ f g, Courses P reg f → Courses P reg g → Training.AgreeOn (· < t) g f →
      g x = f x) → ∀ r r' : Run P, (∀ n, n < t → reg (r'.state n) = reg (r.state n)) →
        reg (r'.state x) = reg (r.state x) :=
    fun right r r' agree => right _ _ (course_mem reg r) (course_mem reg r') agree
  have of_runs : (∀ r r' : Run P, (∀ n, n < t → reg (r'.state n) = reg (r.state n)) →
      reg (r'.state x) = reg (r.state x)) → ∀ f g, Courses P reg f → Courses P reg g →
        Training.AgreeOn (· < t) g f → g x = f x :=
    fun right _ _ ⟨r, at_f⟩ ⟨r', at_g⟩ agree =>
      (at_g x).trans ((right r r' fun n before =>
        (at_g n).symm.trans ((agree n before).trans (at_f n))).trans (at_f x).symm)
  ⟨fun right => Training.fit_right_iff.mp (of_runs right),
   fun determines => to_runs (Training.fit_right_iff.mpr determines)⟩

/-- **Where runs branch freely, the record fixes no later value.** Given two values, within the
registered courses of the runs of free branching the record before `t` fixes the value at no
moment from `t` on. -/
theorem free_prefix_fixes_nothing {V : Type w} {t x : Nat} (late : t ≤ x) {y z : V}
    (two : y ≠ z) : ¬ Determines (Courses (Parting.free V) id) (· < t) x :=
  fun determines => every_determines_nothing (D := (· < t))
    (fun early => Nat.lt_irrefl x (Nat.lt_of_lt_of_le early late)) two
    fun g g' _ _ agree => determines g g' ⟨Parting.freeRun g, fun _ => rfl⟩
      ⟨Parting.freeRun g', fun _ => rfl⟩ agree

end Training

/-! ## The answering law -/

section Answer

variable {O : Type u}

/-- The registration of the law that answers `pred`: the answer to the claim made from the record
the law keeps. -/
def answerReg (pred : List O → Option O) (other : O → O) (x : O) (l : List O) : O :=
  answerTo other x (pred l)

/-- **The answering course is the registered course of a run of the answering law.** Along every
run of `answerStep` from the empty record, what `answerReg` registers is the diagonal course. -/
theorem answer_course (pred : List O → Option O) (other : O → O) (x : O)
    (r : Run (Law.process (answerStep pred other x))) (start : r.state 0 = []) (n : Nat) :
    Parting.course (answerReg pred other x) r n = diagonal pred other x n :=
  congrArg (answerReg pred other x)
    ((Branching.law_run_state r n).trans
      (congrArg (fun s => Law.orbit (answerStep pred other x) s n) start))

theorem answer_prefix (pred : List O → Option O) (other : O → O) (x : O)
    (r : Run (Law.process (answerStep pred other x))) (start : r.state 0 = []) (t : Nat) :
    prefixOf (Parting.course (answerReg pred other x) r) t = prefixOf (diagonal pred other x) t :=
  prefix_congr fun n _ => answer_course pred other x r start n

/-- **The answering world is open.** No list holds the configurations of a run of the answering
law from the empty record. -/
theorem answer_open (pred : List O → Option O) (other : O → O) (x : O)
    (r : Run (Law.process (answerStep pred other x))) (start : r.state 0 = []) :
    ¬ ∃ l : List (List O), ∀ n, r.state n ∈ l :=
  fun ⟨l, held⟩ => diagonal_open pred other x ⟨l, fun n =>
    Eq.subst (motive := fun s => s ∈ l)
      ((Branching.law_run_state r n).trans
        (congrArg (fun s => Law.orbit (answerStep pred other x) s n) start)) (held n)⟩

/-- **With two values told apart, every claim made along the answering run is refuted.** -/
theorem answer_misses [DecidableEq O] (pred : List O → Option O) {a b : O} (two : a ≠ b)
    (r : Run (Law.process (answerStep pred (swapTo a b) a))) (start : r.state 0 = []) {t : Nat}
    {w : O} (claims : pred (prefixOf (Parting.course (answerReg pred (swapTo a b) a) r) t) = some w) :
    MissesAt pred (Parting.course (answerReg pred (swapTo a b) a) r) t :=
  missedAt_of_same (answer_prefix pred (swapTo a b) a r start t).symm
    (answer_course pred (swapTo a b) a r start t).symm
    (diagonal_misses pred (swapTo_moves two) a
      ((congrArg pred (answer_prefix pred (swapTo a b) a r start t)).symm.trans claims))

/-- **The learner over every merging never rests along its answering run.** However classes of
hypotheses are chosen and merged, the learner over them is right from no step on along the run
of the law that answers it. -/
theorem merged_unrested [DecidableEq O] (G : Nat → Nat → List O → Option O) {other : O → O}
    (moves : ∀ v, other v ≠ v) (x : O) (r : Run (Law.process (answerStep (byElimination (merged G)) other x)))
    (start : r.state 0 = []) :
    ¬ ∃ T, ∀ t, T ≤ t → Parting.RightAt (byElimination (merged G)) (answerReg (byElimination (merged G)) other x)
      r t :=
  fun ⟨T, right⟩ => Learning.merged_unrested G moves x ⟨T, fun t late =>
    (congrArg (byElimination (merged G)) (answer_prefix (byElimination (merged G)) other x r start t)).symm.trans
      ((right t late).trans (congrArg some (answer_course (byElimination (merged G)) other x r start t)))⟩

end Answer

/-! ## Along runs of a determined law -/

section Determined

variable {S : Type u} {R : Type w} {next : S → S}

/-- **Induction along a run held by a list: the refutations are bounded.** On a run of a
determined law whose configurations a list `l` holds, the learner over the lasso hypotheses,
reading the registration and knowing neither the configurations nor how many there are, is
refuted fewer than `tri l.length` times, claims at every step from `l.length` on, and is not
refuted at arbitrarily late steps. -/
theorem held_byElimination_bounded [DecidableEq R] (r : Run (Law.process next)) {l : List S}
    (held : ∀ n, r.state n ∈ l) (reg : S → R) :
    (∀ t, index lassos (LearnableRuns.course reg r) t < tri l.length) ∧
      (∀ t, l.length ≤ t → ∃ v, byElimination lassos (prefixOf (LearnableRuns.course reg r) t) = some v) ∧
      ¬ ∀ T, ∃ t, T ≤ t ∧ MissesAt (byElimination lassos) (LearnableRuns.course reg r) t :=
  have held' : ∀ n, Law.orbit next (r.state 0) n ∈ l := fun n =>
    Eq.subst (motive := fun s => s ∈ l) (Branching.law_run_state r n) (held n)
  match Learning.held_byElimination_bounded held' reg with
  | ⟨bound, claims, stops⟩ =>
    ⟨fun t => Nat.lt_of_le_of_lt
        (Nat.le_of_eq (congrArg (indexOn lassos) (LearnableRuns.prefix_eq reg r t))) (bound t),
     fun t late => match claims t late with
      | ⟨v, made⟩ => ⟨v, (congrArg (byElimination lassos) (LearnableRuns.prefix_eq reg r t)).trans made⟩,
     fun late => stops fun T => match late T with
      | ⟨t, after, refuted⟩ => ⟨t, after, missedAt_of_same (LearnableRuns.prefix_eq reg r t)
          (congrArg reg (Branching.law_run_state r t)) refuted⟩⟩

/-- **Induction along a run held by a list: that the learner rests is unrefuted.** -/
theorem held_rest_unrefuted [DecidableEq R] (r : Run (Law.process next)) {l : List S}
    (held : ∀ n, r.state n ∈ l) (reg : S → R) :
    ¬ ¬ LearnableRuns.Rests reg reg (byElimination lassos) r :=
  fun never => Learning.held_rest_unrefuted
    (fun n => Eq.subst (motive := fun s => s ∈ l) (Branching.law_run_state r n) (held n)) reg
    fun ⟨T, rests⟩ => never ⟨T, (LearnableRuns.restsFrom_iff r T).mpr rests⟩

/-- **A claim finer than the registration is right on at most one of two runs beginning alike.**
On runs of a determined law beginning alike in the frame that registers `reg`, at a step where the
targets differ, a learner's claim is not right on both. -/
theorem claim_not_right_on_both {V : Type x} {reg : S → R} {val : S → V} (pred : List R → Option V)
    {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    {t : Nat} (differ : val (r.state t) ≠ val (r'.state t)) :
    ¬ (pred (prefixOf (LearnableRuns.course reg r) t) = some (val (r.state t)) ∧
      pred (prefixOf (LearnableRuns.course reg r') t) = some (val (r'.state t))) :=
  fun ⟨right, right'⟩ =>
    Learnable.claim_not_right_on_both pred (Law.alike_iff_sameFuture.mp alike)
      (fun same => differ ((congrArg val (Branching.law_run_state r t)).trans
        (same.trans (congrArg val (Branching.law_run_state r' t)).symm)))
      ⟨(congrArg pred (LearnableRuns.prefix_eq reg r t)).symm.trans
          (right.trans (congrArg (fun s => some (val s)) (Branching.law_run_state r t))),
       (congrArg pred (LearnableRuns.prefix_eq reg r' t)).symm.trans
          (right'.trans (congrArg (fun s => some (val s)) (Branching.law_run_state r' t)))⟩

/-- **With the targets decided, the claim is refuted on one of two runs beginning alike, and their
records are equal at every step.** -/
theorem missed_on_one {V : Type x} [DecidableEq V] {reg : S → R} {val : S → V}
    (pred : List R → Option V) {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    {t : Nat} (differ : val (r.state t) ≠ val (r'.state t)) {w : V}
    (claims : pred (prefixOf (LearnableRuns.course reg r) t) = some w) :
    (Misses (pred (prefixOf (LearnableRuns.course reg r) t)) (val (r.state t)) ∨
      Misses (pred (prefixOf (LearnableRuns.course reg r') t)) (val (r'.state t))) ∧
    ∀ n, prefixOf (LearnableRuns.course reg r) n = prefixOf (LearnableRuns.course reg r') n :=
  match Learnable.missed_on_one pred (Law.alike_iff_sameFuture.mp alike)
      (fun same => differ ((congrArg val (Branching.law_run_state r t)).trans
        (same.trans (congrArg val (Branching.law_run_state r' t)).symm)))
      ((congrArg pred (LearnableRuns.prefix_eq reg r t)).symm.trans claims) with
  | ⟨one, records⟩ =>
    ⟨match one with
     | .inl refuted => .inl (missedAt_of_same (LearnableRuns.prefix_eq reg r t).symm
         (congrArg val (Branching.law_run_state r t)).symm refuted)
     | .inr refuted => .inr (missedAt_of_same (LearnableRuns.prefix_eq reg r' t).symm
         (congrArg val (Branching.law_run_state r' t)).symm refuted),
     fun n => (LearnableRuns.prefix_eq reg r n).trans
       ((records n).trans (LearnableRuns.prefix_eq reg r' n).symm)⟩

end Determined

/-! ## Witnesses on runs -/

/-- **Negation never rests.** Along every run of the law of negation, each configuration differs
from the one before. -/
theorem negation_never_rests (r : Run (Law.process not)) (n : Nat) :
    r.state (n + 1) ≠ r.state n :=
  fun same => not_moves (r.state n) ((r.step n).symm.trans same)

/-- **Two refutations, then rest.** Along every run of negation from `false`, the learner over
the lasso hypotheses reading the configuration claims each value right from step `3` on. -/
theorem alternate_rests (r : Run (Law.process not)) (start : r.state 0 = false) :
    LearnableRuns.RestsFrom id id (byElimination lassos) r 3 :=
  (LearnableRuns.restsFrom_iff r 3).mpr
    (Eq.subst (motive := fun s => Learnable.RestsFrom not id id (byElimination lassos) s 3) start.symm
      Alternate.rests)

/-- The four configurations of two coordinates. -/
theorem pair_world : ∀ s : Bool × Bool, s ∈ [(true, true), (true, false), (false, true), (false, false)]
  | (true, true) => List.Mem.head _
  | (true, false) => List.Mem.tail _ (List.Mem.head _)
  | (false, true) => List.Mem.tail _ (List.Mem.tail _ (List.Mem.head _))
  | (false, false) => List.Mem.tail _ (List.Mem.tail _ (List.Mem.tail _ (List.Mem.head _)))

/-- **Registering the first coordinate, no learner rests on the second along the runs from both
`(true, false)` and `(true, true)`** of the law leaving each configuration unchanged. -/
theorem pair_first_not_rests (pred : List Bool → Option Bool) :
    ¬ (LearnableRuns.Rests Prod.fst Prod.snd pred (Law.run Learnable.Pair.still (true, false)) ∧
      LearnableRuns.Rests Prod.fst Prod.snd pred (Law.run Learnable.Pair.still (true, true))) :=
  fun ⟨rests, rests'⟩ => Learnable.Pair.first_not_rests pred
    ⟨(LearnableRuns.rests_iff _).mp rests, (LearnableRuns.rests_iff _).mp rests'⟩

/-- **Registering the first coordinate, no learner rests on the second along every run.** -/
theorem pair_not_learnable :
    ¬ ∃ pred : List Bool → Option Bool, ∀ r : Run (Law.process Learnable.Pair.still),
      LearnableRuns.Rests Prod.fst Prod.snd pred r :=
  fun learnable => Learnable.Pair.not_lumped
    ((LearnableRuns.still_learnable_iff_lumped (fun _ => rfl) pair_world).mp learnable)

/-- **Registering both, the learner over the lasso hypotheses rests on the second along every
run from step `2`.** -/
theorem pair_whole_rests (r : Run (Law.process Learnable.Pair.still)) :
    LearnableRuns.RestsFrom id Prod.snd (fun l => (byElimination lassos l).map Prod.snd) r 2 :=
  (LearnableRuns.restsFrom_iff r 2).mpr (Learnable.Pair.whole_rests (r.state 0))

end LearningRuns

end Becoming
