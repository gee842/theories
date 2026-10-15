import Becoming.Typicality

/-!
# Situations: what natural weights count

Ren, 16 October 2026: "we are describing what everything obeys, but at every moment, the actual
change depends on the situation", and "just saying we are all one doesn't make it true, the
situation makes it true". `Becoming.Weighted` leaves open where weights come from;
`Becoming.Typicality` counts courses by natural weights and does not derive that the course
which happens is typical. This module states, with no premise, what natural weights are when
each step is taken in situations that each fix it.

* **With the situation as the move, the law is determined.** A step weighing `k` is taken in `k`
  situations. The law whose moves are the situations (`finerLaw`) is determined
  (`finerLaw_determined`). It takes a step exactly where that step has a situation, that is,
  positive weight (`finerLaw_step_iff`). A law whose steps are those of positive weight is this
  determined law with the situation forgotten.
* **Natural weights count situations.** Each finer course (`finer`) takes the course it forgets to
  (`coarse`). For every process with listed moves and configurations and every natural weighting
  of its steps, summing any reading of the courses over the finer courses of `n` steps is summing
  it over the courses, each counted by its weight (`sum_finer`). So the finer courses number the
  sum over histories (`finer_count`, through `Weights.sum_courses`). Nothing is assumed beyond
  the weighting.
* **The law of large numbers counts situations.** On two values, with `p` situations for one and
  `q` for the other at each step (`Typicality.stepWeight`), there are `(p + q) ^ n` finer courses
  of `n` steps (`situations_count`), and the weight of a course is the number of them that take
  it (`situations_of_course`, each course occurring once, `total_only`). Those whose course
  deviates by at least `d` number, times `d`, at most `n·p·q·(p + q)^n` (`situations_typical`,
  from `Typicality.typical`, through `sum_courses_values`, which reads Weighted's courses of free
  branching as Typicality's).
  Most situations of a kind give frequencies near the ratio of the weights. Which situation is
  the one that happens is not a count, and nothing here fixes it.

The arithmetic uses the core's `mul_assoc_nat`, since the prelude's associativity of
multiplication uses propositional extensionality.

What is not derived: which situation is actual; weights that are not natural numbers. Signed
weights cancel, and a count of situations does not (`Interference.cancels`,
`counting_transfer_iff`). No ethical predicate, ranking or axiom occurs. Ren took the AI's readings of their words on
16 October 2026 ("yes, i take those readings"): the core states what every situation obeys,
the situation makes the actual change true, and a chance is a number of situations of a kind.
-/

namespace Becoming

open Generative

namespace Situations

universe u v

/-! ## Counting the first `k` numbers -/

/-- The first `k` numbers, the last first. -/
def upto : Nat → List Nat
  | 0 => []
  | k + 1 => k :: upto k

/-- A reading constant over the first `k` numbers sums to `k` times it. -/
theorem sum_upto (c : Nat) : ∀ k, counting.sum (upto k) (fun _ => c) = k * c
  | 0 => (Nat.zero_mul c).symm
  | k + 1 => by
    show c + counting.sum (upto k) (fun _ => c) = (k + 1) * c
    rw [sum_upto c k, Nat.succ_mul, Nat.add_comm]

/-- Counting ones over a list gives its length. -/
theorem sum_one {α : Type u} : ∀ l : List α, counting.sum l (fun _ => 1) = l.length
  | [] => rfl
  | _ :: l => by
    show 1 + counting.sum l (fun _ => 1) = l.length + 1
    rw [sum_one l, Nat.add_comm]

/-! ## The law with the situation as the move -/

section Finer

variable {S : Type u} {A : Type v}

/-- The law whose moves are situations: the situation `(a, m, k)` takes a configuration `s` to
`m`, where it is one of the `weight s a m` situations of the step by `a` to `m`. -/
def finerLaw (weight : S → A → S → Nat) : Process S (A × S × Nat) :=
  ⟨fun s x t => t = x.2.1 ∧ x.2.2 < weight s x.1 x.2.1⟩

/-- **With the situation as the move, the law is determined.** -/
theorem finerLaw_determined (weight : S → A → S → Nat) : Determined (finerLaw weight) :=
  fun _ _ _ _ first second => first.1.trans second.1.symm

/-- **The finer law takes a step exactly where the step has a situation.** -/
theorem finerLaw_step_iff (weight : S → A → S → Nat) {s m : S} {a : A} :
    (∃ k, (finerLaw weight).step s (a, m, k) m) ↔ 0 < weight s a m :=
  ⟨fun ⟨_, _, within⟩ => Nat.lt_of_le_of_lt (Nat.zero_le _) within,
   fun positive => ⟨0, rfl, positive⟩⟩

/-- The situations of the open steps from `s`: each open step `(a, m)` once for each of the
`weight s a m` situations taking it. -/
def finerSteps (weight : S → A → S → Nat) (moves : List A) (all : List S) (s : S) :
    List (A × S × Nat) :=
  joinMap (fun p => (upto (weight s p.1 p.2)).map fun k => (p.1, p.2, k)) (openSteps moves all)

/-- The finer courses of `n` steps from `s`: every sequence of situations, each taken from where
the one before leads. -/
def finer (weight : S → A → S → Nat) (moves : List A) (all : List S) : Nat → S →
    List (List (A × S × Nat))
  | 0, _ => [[]]
  | n + 1, s => joinMap (fun x => (finer weight moves all n x.2.1).map fun h => x :: h)
      (finerSteps weight moves all s)

/-- The course a finer course takes: its steps with the situation forgotten. -/
def coarse : List (A × S × Nat) → List (A × S)
  | [] => []
  | x :: h => (x.1, x.2.1) :: coarse h

/-- **Natural weights count situations.** For every natural weighting of the steps, summing any
reading of the courses over the finer courses of `n` steps is summing it over the courses of
`n` steps, each counted by its weight. -/
theorem sum_finer (weight : S → A → S → Nat) (moves : List A) (all : List S) :
    ∀ (n : Nat) (s : S) (g : List (A × S) → Nat),
      counting.sum (finer weight moves all n s) (fun h => g (coarse h)) =
        counting.sum (courses moves all n)
          (fun c => counting.along weight (fun _ => 1) s c * g c)
  | 0, _, g => by
    show g [] + 0 = 1 * g [] + 0
    rw [Nat.one_mul]
  | n + 1, s, g =>
    have inner : ∀ x : A × S × Nat,
        counting.sum ((finer weight moves all n x.2.1).map fun h => x :: h)
            (fun h => g (coarse h)) =
          counting.sum (courses moves all n)
            (fun c => counting.along weight (fun _ => 1) x.2.1 c * g ((x.1, x.2.1) :: c)) :=
      fun x => (Weights.sum_map _ _ _).trans
        (sum_finer weight moves all n x.2.1 fun c => g ((x.1, x.2.1) :: c))
    have each : ∀ p : A × S,
        counting.sum ((upto (weight s p.1 p.2)).map fun k => (p.1, p.2, k))
            (fun x => counting.sum (courses moves all n)
              (fun c => counting.along weight (fun _ => 1) x.2.1 c * g ((x.1, x.2.1) :: c))) =
          counting.sum (courses moves all n)
            (fun c => counting.along weight (fun _ => 1) s (p :: c) * g (p :: c)) :=
      fun p => (Weights.sum_map _ _ _).trans
        ((sum_upto (counting.sum (courses moves all n)
            (fun c => counting.along weight (fun _ => 1) p.2 c * g (p :: c))) _).trans
          ((Weights.mul_sum (W := counting) (weight s p.1 p.2) _ _).trans
            (Weights.sum_congr _ fun c _ => (mul_assoc_nat _ _ _).symm)))
    have whole : counting.sum (courses moves all (n + 1))
          (fun c => counting.along weight (fun _ => 1) s c * g c) =
        counting.sum (openSteps moves all) (fun p => counting.sum (courses moves all n)
          (fun c => counting.along weight (fun _ => 1) s (p :: c) * g (p :: c))) :=
      (Weights.sum_joinMap _ _ _).trans (Weights.sum_congr _ fun _ _ => Weights.sum_map _ _ _)
    (Weights.sum_joinMap _ _ _).trans <|
      (Weights.sum_congr _ fun x _ => inner x).trans <|
      (Weights.sum_joinMap _ _ _).trans <|
      (Weights.sum_congr _ fun p _ => each p).trans whole.symm

/-- **The finer courses number the sum over histories.** -/
theorem finer_count (weight : S → A → S → Nat) (moves : List A) (all : List S) (n : Nat)
    (s : S) :
    (finer weight moves all n s).length = counting.transfer weight moves all (fun _ => 1) n s :=
  (sum_one _).symm.trans <|
    (sum_finer weight moves all n s fun _ => 1).trans <|
    (Weights.sum_congr _ fun _ _ => Nat.mul_one _).trans
      (Weights.sum_courses weight moves all (fun _ => 1) n s)

end Finer

/-! ## Two values -/

/-- **Free branching on two values has Typicality's courses.** Summing a reading of the values
over the histories of `n` steps is summing it over the courses of `n` steps. -/
theorem sum_courses_values (F : List Bool → Nat) : ∀ n,
    counting.sum (Becoming.courses [()] [true, false] n) (fun c => F (c.map Prod.snd)) =
      Typicality.total (Typicality.courses n) F
  | 0 => rfl
  | n + 1 =>
    have each : ∀ b : Bool,
        counting.sum ((Becoming.courses [()] [true, false] n).map fun h => ((), b) :: h)
            (fun c => F (c.map Prod.snd)) =
          Typicality.total (Typicality.courses n) (fun w => F (b :: w)) :=
      fun b => (Weights.sum_map _ _ _).trans (sum_courses_values (fun w => F (b :: w)) n)
    (Weights.sum_joinMap _ _ _).trans <| by
      show counting.sum ((Becoming.courses [()] [true, false] n).map fun h => ((), true) :: h)
            (fun c => F (c.map Prod.snd)) +
          (counting.sum ((Becoming.courses [()] [true, false] n).map fun h => ((), false) :: h)
            (fun c => F (c.map Prod.snd)) + 0) =
        Typicality.total (Typicality.extend (Typicality.courses n)) F
      rw [each true, each false, Nat.add_zero, Typicality.total_extend, Typicality.total_add]

/-- **There are `(p + q) ^ n` finer courses of `n` steps.** With `p` situations for one value
and `q` for the other at each step. -/
theorem situations_count (p q n : Nat) (s : Bool) :
    (finer (Typicality.stepWeight p q) [()] [true, false] n s).length = (p + q) ^ n :=
  (finer_count _ _ _ n s).trans (Typicality.transfer_weight p q n s)

/-- Multiplying by one where a condition holds and by nothing otherwise. -/
theorem mul_indicator (x : Nat) (c : Prop) [Decidable c] :
    x * (if c then 1 else 0) = if c then x else 0 :=
  if holds : c then by rw [if_pos holds, if_pos holds, Nat.mul_one]
  else by rw [if_neg holds, if_neg holds, Nat.mul_zero]

/-- Each course of `n` steps occurs once among the courses: a reading kept at `w` alone sums
to its value at `w`. -/
theorem total_only (f : List Bool → Nat) : ∀ (n : Nat) (w : List Bool), w.length = n →
    Typicality.total (Typicality.courses n) (fun v => if v = w then f v else 0) = f w
  | 0, [], _ => by
    show (if ([] : List Bool) = [] then f [] else 0) + 0 = f []
    rw [if_pos rfl, Nat.add_zero]
  | 0, _ :: _, len => nomatch len
  | _ + 1, [], len => nomatch len
  | n + 1, b :: w, len => by
    have same : ∀ v, (if true :: v = b :: w then f (true :: v) else 0) +
        (if false :: v = b :: w then f (false :: v) else 0) =
          (if v = w then f (b :: v) else 0) := fun v =>
      if here : v = w then
        match b with
        | true => by
          rw [if_pos (congrArg _ here), if_neg (fun e => Bool.noConfusion (List.cons.inj e).1),
            if_pos here, Nat.add_zero]
        | false => by
          rw [if_neg (fun e => Bool.noConfusion (List.cons.inj e).1),
            if_pos (congrArg _ here), if_pos here, Nat.zero_add]
      else by
        rw [if_neg (fun e => here (List.cons.inj e).2), if_neg (fun e => here (List.cons.inj e).2),
          if_neg here]
    show Typicality.total (Typicality.extend (Typicality.courses n)) _ = _
    rw [Typicality.total_extend, Typicality.total_congr same]
    exact total_only (fun v => f (b :: v)) n w (Nat.succ.inj len)

/-- **The weight of a course is the number of situations that take it.** With `p` situations
for one value and `q` for the other at each step, the finer courses taking a course with `a`
ones and `b` zeros number `p ^ a · q ^ b`, its weight. -/
theorem situations_of_course (p q : Nat) (s : Bool) (w : List Bool) :
    counting.sum (finer (Typicality.stepWeight p q) [()] [true, false] w.length s)
        (fun h => if (coarse h).map Prod.snd = w then 1 else 0) = Typicality.weight p q w :=
  (sum_finer _ _ _ w.length s fun c => if c.map Prod.snd = w then 1 else 0).trans <|
    (Weights.sum_congr _ fun c _ =>
      congrArg (· * (if c.map Prod.snd = w then 1 else 0)) (Typicality.along_weight p q s c)).trans <|
    (sum_courses_values (fun v => Typicality.weight p q v * (if v = w then 1 else 0))
      w.length).trans <|
    (Typicality.total_congr (fun v => mul_indicator (Typicality.weight p q v) (v = w)) _).trans
      (total_only (Typicality.weight p q) w.length w rfl)

/-- One where a course deviates by at least `d`, and nothing otherwise. -/
def far (p q d : Nat) (w : List Bool) : Nat :=
  if d + Typicality.cross p q w ≤ Typicality.square p q w then 1 else 0

theorem weight_far (p q d : Nat) (w : List Bool) :
    Typicality.weight p q w * far p q d w = Typicality.offBy p q d w :=
  mul_indicator _ _

/-- **The law of large numbers counts situations.** Of the `(p + q) ^ n` finer courses of `n`
steps, those whose course deviates by at least `d` number, times `d`, at most
`n·p·q·(p + q)^n`. -/
theorem situations_typical (p q n d : Nat) (s : Bool) :
    counting.sum (finer (Typicality.stepWeight p q) [()] [true, false] n s)
        (fun h => far p q d ((coarse h).map Prod.snd)) * d ≤ n * (p * q * (p + q) ^ n) := by
  have count : counting.sum (finer (Typicality.stepWeight p q) [()] [true, false] n s)
        (fun h => far p q d ((coarse h).map Prod.snd)) =
      Typicality.total (Typicality.courses n) (Typicality.offBy p q d) :=
    (sum_finer _ _ _ n s fun c => far p q d (c.map Prod.snd)).trans <|
      (Weights.sum_congr _ fun c _ =>
        congrArg (· * far p q d (c.map Prod.snd)) (Typicality.along_weight p q s c)).trans <|
      (sum_courses_values (fun w => Typicality.weight p q w * far p q d w) n).trans
        (Typicality.total_congr (weight_far p q d) _)
  rw [count]
  exact Typicality.typical p q n d

end Situations

end Becoming
