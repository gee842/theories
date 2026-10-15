import Becoming.Distinguishing

/-!
# Parting: what a record fixes where the course branches

`Becoming.Identification` states what a bounded record fixes under a determined law: the
registered course of a world of `N` configurations is fixed by its record before `N + N - 1`,
and no earlier step serves every such world. A process of the spine fixes only which steps are
admissible, and from one configuration its runs can go different ways. This module states,
with no premise beyond what each law names, what a record fixes along the runs of any process.

* **At a parting no learner is right on both.** Two runs part at a step where they register the
  same before it and differ at it (`PartAt`). Their records before the step are one record, so
  no learner, whatever it is given, the world included, is right at that step on both
  (`not_right_on_both`). A learner right at every step from `T` on, on every run from a
  configuration, leaves no two of those runs parting at any step from `T` on
  (`not_parting_of_right`). With the registered values decided, no two runs from a
  configuration part exactly where all of them register one course (`unparted_iff`).
* **Where runs do not part, the bound carries.** Not parting is kept along runs: from every
  configuration a run from an unparted configuration reaches, no two runs part either
  (`Unparted.along`, by joining runs at a step, `joinAt`). So on a run from a configuration
  from which no two runs part, held by a list of `N` configurations, the registered course has at
  most `N` states (`course_statesBelow`), and the learner by the least bound of
  `Becoming.Identification`, given nothing, is right at every step from `N + N - 1` on
  (`leastBound_right`). No learner is right at step `N + N - 2` on every such run for `N ≥ 2`
  (`rest_earliest_runs`): the step is exact for processes as for laws. A determined process
  with one move parts nowhere (`unparted_of_determined`), so the determined case is the
  instance; a process can branch and part nowhere where its branching does not show in what is
  registered (`free_unparted_const`).
* **Where runs part, nothing bounds the course.** Under free branching, every configuration
  may follow every configuration (`free`), every course is the registered course of a run
  (`freeRun`). So after every record two runs of two configurations part, each with that record
  (`free_parts_after`): no record shows that a world will not part. For every learner and every
  record, a run of free branching on two values has that record and the learner is not right at
  the next step (`free_open`); for every learner, one run is never right at any step
  (`free_never_right`); and a run of free branching on two configurations has a registered course
  with no bound on its states (`free_unbounded`).

So with a bound on configurations a record fixes the registered course exactly as far as the
runs do not part, from `N + N - 1` on; where they part, neither the record nor the law fixes
which way the run goes. Ren, 16 October 2026: "we are describing what everything obeys, but at
every moment, the actual change depends on the situation", and "the situation makes it true".
Read so, a law that branches leaves open what the situation fixes: with the situation as the
move, the law is determined (`Becoming.Situations`). This reading of Ren's words is the AI's,
pending Ren.
-/

namespace Becoming

open Generative

universe u v w

namespace Parting

section Runs

variable {S : Type u} {A : Type v} {P : Process S A}

/-- The run from step `k` on. -/
def after (r : Run P) (k : Nat) : Run P :=
  ⟨fun n => r.state (k + n), fun n => r.act (k + n), fun n => r.step (k + n)⟩

/-- A run preceded by one admissible step into its start. -/
def before (s : S) (a : A) (r : Run P) (into : P.step s a (r.state 0)) : Run P :=
  ⟨fun | 0 => s | t + 1 => r.state t, fun | 0 => a | t + 1 => r.act t,
    fun | 0 => into | t + 1 => r.step t⟩

/-- **Joining runs at a step.** The run `r` up to step `k`, then the run `r'` from where `r` is
at `k`; it begins where `r` begins. -/
def joinAt : (k : Nat) → (r r' : Run P) → r'.state 0 = r.state k →
    {q : Run P // q.state 0 = r.state 0}
  | 0, _, r', meet => ⟨r', meet⟩
  | k + 1, r, r', meet =>
    let q := joinAt k (after r 1) r' (meet.trans (congrArg r.state (Nat.add_comm k 1)))
    ⟨before (r.state 0) (r.act 0) q.1
      (Eq.subst (motive := fun x => P.step (r.state 0) (r.act 0) x) q.2.symm (r.step 0)), rfl⟩

/-- Up to step `k` the joined run is `r`. -/
theorem joinAt_before : ∀ (k : Nat) (r r' : Run P) (meet : r'.state 0 = r.state k) (n : Nat),
    n ≤ k → (joinAt k r r' meet).1.state n = r.state n
  | 0, _, _, meet, 0, _ => meet
  | 0, _, _, _, _ + 1, le => absurd le (Nat.not_succ_le_zero _)
  | _ + 1, _, _, _, 0, _ => rfl
  | k + 1, r, r', meet, n + 1, le =>
    (joinAt_before k (after r 1) r' (meet.trans (congrArg r.state (Nat.add_comm k 1))) n
      (Nat.le_of_succ_le_succ le)).trans (congrArg r.state (Nat.add_comm 1 n))

/-- From step `k` on the joined run is `r'`. -/
theorem joinAt_after : ∀ (k : Nat) (r r' : Run P) (meet : r'.state 0 = r.state k) (n : Nat),
    (joinAt k r r' meet).1.state (k + n) = r'.state n
  | 0, _, r', _, n => congrArg r'.state (Nat.zero_add n)
  | k + 1, r, r', meet, n =>
    (congrArg (joinAt (k + 1) r r' meet).1.state (Nat.succ_add k n)).trans
      (joinAt_after k (after r 1) r' (meet.trans (congrArg r.state (Nat.add_comm k 1))) n)

end Runs

/-! ## At a parting no learner is right on both -/

section Part

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- What the registration registers along a run. -/
def course (reg : S → R) (r : Run P) : Nat → R := fun n => reg (r.state n)

/-- Two runs part at step `t`: they register the same before `t` and differ at `t`. -/
def PartAt (reg : S → R) (r r' : Run P) (t : Nat) : Prop :=
  (∀ n, n < t → reg (r.state n) = reg (r'.state n)) ∧ reg (r.state t) ≠ reg (r'.state t)

/-- No two runs from `s` part: every two runs from `s` register one course. -/
def Unparted (P : Process S A) (reg : S → R) (s : S) : Prop :=
  ∀ r r' : Run P, r.state 0 = s → r'.state 0 = s → ∀ n, reg (r.state n) = reg (r'.state n)

/-- The learner `pred`, reading the record of what is registered along `r` before `t`, claims
what is registered at `t`. -/
def RightAt (pred : List R → Option R) (reg : S → R) (r : Run P) (t : Nat) : Prop :=
  pred (Learning.record (course reg r) t) = some (reg (r.state t))

/-- **At a parting no learner is right on both.** The two records before the step are one
record, whatever the learner is given. -/
theorem not_right_on_both (pred : List R → Option R) {reg : S → R} {r r' : Run P} {t : Nat}
    (part : PartAt reg r r' t) : ¬ (RightAt pred reg r t ∧ RightAt pred reg r' t) :=
  fun ⟨right, right'⟩ =>
    have same : Learning.record (course reg r) t = Learning.record (course reg r') t :=
      Learning.record_congr part.1
    part.2 (Option.some.inj (right.symm.trans ((congrArg pred same).trans right')))

/-- A learner right at every step from `T` on, on every run from `s`, leaves no two of those
runs parting at any step from `T` on. -/
theorem not_parting_of_right {pred : List R → Option R} {reg : S → R} {s : S} {T : Nat}
    (right : ∀ r : Run P, r.state 0 = s → ∀ t, T ≤ t → RightAt pred reg r t)
    (r r' : Run P) (start : r.state 0 = s) (start' : r'.state 0 = s) {t : Nat} (late : T ≤ t) :
    ¬ PartAt reg r r' t :=
  fun part => not_right_on_both pred part ⟨right r start t late, right r' start' t late⟩

/-- **No two runs from a configuration part exactly where all of them register one course.** -/
theorem unparted_iff [DecidableEq R] {reg : S → R} {s : S} :
    Unparted P reg s ↔
      ∀ r r' : Run P, r.state 0 = s → r'.state 0 = s → ∀ t, ¬ PartAt reg r r' t :=
  ⟨fun unparted r r' start start' t part => part.2 (unparted r r' start start' t),
   fun none r r' start start' =>
     Identification.below_all fun m agree =>
       match decEq (reg (r.state m)) (reg (r'.state m)) with
       | isTrue same => same
       | isFalse differ => absurd ⟨agree, differ⟩ (none r r' start start' m)⟩

end Part

/-! ## Where runs do not part, the bound carries -/

section Carries

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- **Not parting is kept along runs.** From every configuration that a run from an unparted
configuration reaches, no two runs part either. -/
theorem Unparted.along {reg : S → R} {s : S} (unparted : Unparted P reg s) {r : Run P}
    (start : r.state 0 = s) (k : Nat) : Unparted P reg (r.state k) :=
  fun q q' from_q from_q' n =>
    have agree := unparted (joinAt k r q from_q).1 (joinAt k r q' from_q').1
      ((joinAt k r q from_q).2.trans start) ((joinAt k r q' from_q').2.trans start) (k + n)
    ((congrArg reg (joinAt_after k r q from_q n)).symm.trans agree).trans
      (congrArg reg (joinAt_after k r q' from_q' n))

/-- **Where runs do not part, the course has at most as many states as there are
configurations.** On a run from a configuration from which no two runs part, held by a list,
the registered course has at most as many states as the list has members. -/
theorem course_statesBelow {reg : S → R} {s : S} (unparted : Unparted P reg s) {r : Run P}
    (start : r.state 0 = s) {l : List S} (held : ∀ n, r.state n ∈ l) :
    StatesBelow (course reg r) l.length :=
  match revisits_within l r.state (fun n _ => held n) with
  | ⟨i, j, lt, within, same⟩ =>
    have ahead : SameAhead (course reg r) i j :=
      unparted.along start i (after r i) (after r j) rfl same.symm
    Identification.statesBelow_mono (statesBelow_of_same lt ahead) within

/-- **The learner given nothing rests from `N + N - 1` on.** On a run from a configuration from
which no two runs part, held by a list of `N` configurations, the learner by the least bound is
right at every step from `N + N - 1` on. -/
theorem leastBound_right [DecidableEq R] {reg : S → R} {s : S} (unparted : Unparted P reg s)
    {r : Run P} (start : r.state 0 = s) {l : List S} (held : ∀ n, r.state n ∈ l) {t : Nat}
    (late : l.length + l.length - 1 ≤ t) : RightAt Identification.leastBound reg r t :=
  Identification.leastBound_exact (course_statesBelow unparted start held) late

/-- Two runs of a determined process with one move from one configuration are one course of
configurations. -/
theorem states_agree {P : Process S Unit} (determined : Determined P) {r r' : Run P}
    (start : r.state 0 = r'.state 0) : ∀ n, r.state n = r'.state n
  | 0 => start
  | n + 1 =>
    determined (r.state n) () (r.state (n + 1)) (r'.state (n + 1)) (r.step n)
      (Eq.subst (motive := fun x => P.step x () (r'.state (n + 1)))
        (states_agree determined start n).symm (r'.step n))

/-- **A determined process with one move parts nowhere.** -/
theorem unparted_of_determined {P : Process S Unit} (determined : Determined P) (reg : S → R)
    (s : S) : Unparted P reg s :=
  fun _ _ start start' n => congrArg reg (states_agree determined (start.trans start'.symm) n)

/-- **The step is exact for processes.** Given two values, no learner is right at step
`N + N - 2` on every run, from a configuration from which no two runs part, of every process of
`N = M + 2` configurations. -/
theorem rest_earliest_runs {x y : R} (two : x ≠ y) (pred : List R → Option R) (M : Nat) :
    ¬ ∀ (P : Process (Fin (M + 2)) Unit) (reg : Fin (M + 2) → R) (r : Run P),
      Unparted P reg (r.state 0) → RightAt pred reg r (M + M + 2) :=
  fun all => Identification.rest_earliest two pred M fun _ bound =>
    match Law.realized_within bound with
    | ⟨next, reg, s, reads⟩ =>
      have right := all (Law.process next) reg
        ⟨Law.orbit next s, fun _ => (), fun _ => rfl⟩
        (unparted_of_determined (show Determined (Law.process next) from
          fun s _ t t' (first : t = next s) (second : t' = next s) => first.trans second.symm)
          reg _)
      (congrArg pred (Learning.record_congr fun n _ => (reads n).symm)).trans
        (right.trans (congrArg some (reads (M + M + 2))))

end Carries

/-! ## Where runs part, nothing bounds the course -/

section Free

variable {V : Type w}

/-- **Free branching**: every configuration may follow every configuration. -/
def free (V : Type w) : Process V Unit := ⟨fun _ _ _ => True⟩

/-- Every course is a run of free branching, registered as it is. -/
def freeRun (o : Nat → V) : Run (free V) := ⟨o, fun _ => (), fun _ => trivial⟩

theorem freeRun_course (o : Nat → V) : course id (freeRun o) = o := rfl

/-- **Free branching parts nowhere where the registration does not show it.** -/
theorem free_unparted_const {R : Type u} (x : R) (s : V) :
    Unparted (free V) (fun _ => x) s :=
  fun _ _ _ _ _ => rfl

/-- **No record shows that a world will not part.** Given two values, after every record two
runs of free branching, each with that record, part. -/
theorem free_parts_after {x y : V} (two : x ≠ y) (o : Nat → V) (t : Nat) :
    ∃ r r' : Run (free V), Learning.record (course id r) t = Learning.record o t ∧
      Learning.record (course id r') t = Learning.record o t ∧ PartAt id r r' t :=
  ⟨freeRun (Learning.holdFrom o t x), freeRun (Learning.holdFrom o t y),
   Learning.record_congr fun _ early => Learning.holdFrom_before o x early,
   Learning.record_congr fun _ early => Learning.holdFrom_before o y early,
   fun _ early => (Learning.holdFrom_before o x early).trans
     (Learning.holdFrom_before o y early).symm,
   fun same => two ((Learning.holdFrom_after o x (Nat.le_refl t)).symm.trans
     (same.trans (Learning.holdFrom_after o y (Nat.le_refl t))))⟩

/-- **After every record, every learner is open to error.** Given two values, for every learner
and every record, a run of free branching has that record and the learner is not right at the
next step. -/
theorem free_open [DecidableEq V] {x y : V} (two : x ≠ y) (pred : List V → Option V)
    (o : Nat → V) (t : Nat) :
    ∃ r : Run (free V), Learning.record (course id r) t = Learning.record o t ∧
      ¬ RightAt pred id r t :=
  match free_parts_after two o t with
  | ⟨r, r', same, same', part⟩ =>
    match decEq (pred (Learning.record (course id r) t)) (some (r.state t)) with
    | isFalse wrong => ⟨r, same, wrong⟩
    | isTrue right => ⟨r', same', fun right' => not_right_on_both pred part ⟨right, right'⟩⟩

/-- **Every learner has a run of free branching on which it is never right.** -/
theorem free_never_right (pred : List Bool → Option Bool) :
    ∃ r : Run (free Bool), ∀ t, ¬ RightAt pred id r t :=
  ⟨freeRun (Learning.diagonal pred (fun b => !b) false), fun _ right =>
    match Learning.diagonal_refutes pred Identification.not_ne_bool false right with
    | ⟨_, made, differs⟩ => differs (Option.some.inj (made.symm.trans right))⟩

/-- Free branching on two values is held by a list of two configurations. -/
theorem free_held (r : Run (free Bool)) (n : Nat) : r.state n ∈ [true, false] :=
  match r.state n with
  | true => List.Mem.head _
  | false => List.Mem.tail _ (List.Mem.head _)

/-- **Where runs part, two configurations bound nothing.** A run of free branching on two
configurations has a registered course with no bound on its states. -/
theorem free_unbounded :
    ∃ r : Run (free Bool), ∀ N, ¬ StatesBelow (course id r) N :=
  ⟨freeRun (Learning.diagonal (Learning.learner Learning.lassos) (fun b => !b) false),
   fun _ bound => match Identification.statesBelow_iff_lasso.mp bound with
     | ⟨_, _, _, lasso⟩ => Learning.diagonal_not_lasso Identification.not_ne_bool false lasso⟩

end Free

end Parting

end Becoming
