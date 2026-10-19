import Becoming.Weighted
import Becoming.Loops

/-!
# Routes: the orders of a carried difference as a sum over histories

On 12 October 2026 Ren asked of laws that are not determined, comparing them with Feynman diagrams,
how "we can still find a way to to integrate so we can still calculate this effects but how how
accurate can we do that uh what is the limitation do we have losses". Two answers stood apart.
`Becoming.Weighted` (P82) sums over histories: the weight of a course is composed of the weights of
its steps, alternatives add, and its losses are truncation, cancellation, memory and loops.
`Becoming.Loops` (P118) expands the carried difference of `Becoming.Propagation` by order: order
`j` is what routes of at most `j` responses carry. Ren took the reading that the two are of the
same structural kind and not yet joined, and asked on 16 October for the join. This module gives
it, within the theory without axiom and with no premise beyond what each statement names.

* **The carried amount is a sum over histories.** Trace a difference back in time. From the level
  of `c` at step `τ` (`RoutePoint.level`), a step is one response: the level of `d` at an earlier
  step `s`, with the weight the strengths give it summed over every step at which the response can
  occur, the level holding between responses (`responseWeight`); or an end at a source, the
  starting gap and the part's gaps held (`RoutePoint.source`, weighed by order `0`). A source stays
  a source. These are counting weights of steps (`routeWeight`), and the transfer of `Becoming.Weighted`
  over the listed route points (`routeSum`) of horizon `j + 1` is order `j` of `Becoming.Loops` at
  every condition and step (`routeSum_eq_carriedWithin`). So by `Weights.sum_courses` each order is
  the sum over every course of `j + 1` steps of the composed weights of its steps
  (`carriedWithin_eq_courses`), and the carried amount at step `t` the sum over every course of
  `t + 1` steps (`carried_eq_courses`). The order of `Becoming.Loops` is the horizon of
  `Becoming.Weighted`: a cut at order `j` is a truncation at horizon `j + 1`, exact from horizon
  `t + 1` on at step `t` (`routeSum_exact`) and rising to it (`routeSum_mono`,
  `routeSum_le_carried`).
* **Loops where both multiply.** Read through this, P118's loop theorems are theorems of the sum
  over histories. With stationary strengths and the same formations at every step, a finite horizon
  of the sum over routes is exact at a condition at every step, from every starting gap, exactly
  where no loop lies upstream of it (`finite_horizon_iff_no_loop`), and where the strengths into
  each condition sum to at most `M` and the starting gaps are at most `D`, a horizon of `j + 1`
  misses at most `Loops.missBound M D j t` (`carried_le_routeSum_add`). P82's loss by loops,
  courses that multiply around a loop so that no horizon is enough, is P118's runaway.
* **Every sum over histories expands by order.** For every weighting, split each step's weight into
  a ground part and a response part. Order `j` of the transfer (`Weights.within`) has, across each
  step, the ground part reading order `j` and the response part reading order `j - 1`, as
  `carriedWithin` does; it is exact at every horizon up to `j` (`Weights.within_exact`), since a
  course of `n` steps has at most `n` responses. A reading that keeps the laws of the weights can
  be taken order by order (`Weights.Hom.within`). For counting the orders rise
  (`counting_within_le_succ`) to the sum over histories (`counting_within_le_transfer`).
* **The time orderings of P118 are the orders of P82.** With one configuration, ground weight one
  and response weight `M`, order `j` at horizon `n` is `Loops.orderSum M j n`, the sum over
  `i ≤ j` of `Loops.binom n i * M ^ i` (`SelfLoop.within_eq`), while the whole sum is
  `(1 + M) ^ n` (`SelfLoop.transfer_eq`): the self-loop of `Becoming.Loops`, and P82's courses that
  double around a loop where `M` is one.

**Readings (the AI's, taken by Ren on 16 October 2026).**
- The join makes the structural match exact. A route back in time is a history in P82's sense: its
  steps are responses, the vertices of a diagram, and between them the level holds, summed over the
  steps at which a response can occur, as a propagator sums over intermediate times. Its order is
  its number of vertices. So "the integration" Ren asked about is one integration: P118's orders
  are P82's sum over histories, organized by horizon, and its losses meet. A truncation of the sum
  is a cut of the expansion; a loop, which multiplies courses in P82, is what makes the difference
  run away in P118.
- The match stays structural, not physical. The weights are counts of strengths, not amplitudes;
  nothing cancels, since counting weights do not (`Interference.unseen` in `Becoming.Weighted`).

What is not derived: the strengths, which are supplied as in `Becoming.Propagation`; signed or
complex weights for carried differences; an order expansion that groups courses by exactly `i`
responses for every weighting (which needs alternatives that commute); sums over infinitely many
route points or an unbounded horizon. The representation commits to discrete steps and natural
amounts. No ethical predicate, ranking or axiom occurs.

**Classical sources.** The sum over routes is the walk-sum (path-sum) expansion of a matrix power,
the transfer over `n` steps summed over every course of `n` steps; ordering it by the number of
responses is the truncated Neumann series `Σ K^j` read as a sum over walks, and the self-loop's `Σ_{i ≤ j} binom n i · M ^ i`
against `(1 + M) ^ n` is the binomial theorem cut at order `j`. The structural match with Feynman
diagrams is a reading, not a physical claim.
-/

namespace Becoming

universe u v w x

/-! ## Every sum over histories expands by order -/

section Orders

variable {R : Type w} {W : Weights R} {S : Type u} {A : Type v}

/-- **The orders of a sum over histories.** Each step's weight split into a ground part and a
response part: order `j` reads, across each step, order `j` through the ground part and order
`j - 1` through the response part, and order `0` reads the ground part only. -/
def Weights.within (W : Weights R) (ground response : S → A → S → R) (moves : List A)
    (all : List S) (f : S → R) : Nat → Nat → S → R
  | _, 0, s => f s
  | 0, n + 1, s => W.sum (openSteps moves all) fun p =>
      W.mul (ground s p.1 p.2) (Weights.within W ground response moves all f 0 n p.2)
  | j + 1, n + 1, s => W.sum (openSteps moves all) fun p =>
      W.add (W.mul (ground s p.1 p.2) (Weights.within W ground response moves all f (j + 1) n p.2))
        (W.mul (response s p.1 p.2) (Weights.within W ground response moves all f j n p.2))

/-- **Each order is exact up to its own horizon.** For every weighting, a course of `n` steps has
at most `n` responses, so order `j` of the sum over histories is the whole sum at every horizon up
to `j`. -/
theorem Weights.within_exact (ground response : S → A → S → R) (moves : List A) (all : List S)
    (f : S → R) :
    ∀ j n, n ≤ j → ∀ s, W.within ground response moves all f j n s =
      W.transfer (fun s a t => W.add (ground s a t) (response s a t)) moves all f n s
  | _, 0, _, _ => rfl
  | 0, n + 1, le, _ => absurd le (Nat.not_succ_le_zero n)
  | j + 1, n + 1, le, _ =>
    Weights.sum_congr _ fun p _ =>
      (congrArg (fun y => W.add y _)
          (congrArg (W.mul _) (Weights.within_exact ground response moves all f (j + 1) n
            (Nat.le_succ_of_le (Nat.le_of_succ_le_succ le)) p.2))).trans
        ((congrArg (W.add _) (congrArg (W.mul _) (Weights.within_exact ground response moves all f
            j n (Nat.le_of_succ_le_succ le) p.2))).trans
          (W.right_distrib _ _ _).symm)

variable {T : Type x} {V : Weights T}

/-- **A reading that keeps the laws can be taken order by order.** -/
theorem Weights.Hom.within (h : Weights.Hom W V) (ground response : S → A → S → R) (moves : List A)
    (all : List S) (f : S → R) :
    ∀ j n s, h.map (W.within ground response moves all f j n s) =
      V.within (fun s a t => h.map (ground s a t)) (fun s a t => h.map (response s a t)) moves all
        (fun s => h.map (f s)) j n s
  | _, 0, _ => rfl
  | 0, n + 1, _ => (Weights.Hom.sum h _ _).trans (Weights.sum_congr _ fun p _ =>
      (h.map_mul _ _).trans (congrArg (V.mul _) (Weights.Hom.within h ground response moves all f
        0 n p.2)))
  | j + 1, n + 1, _ => (Weights.Hom.sum h _ _).trans (Weights.sum_congr _ fun p _ =>
      (h.map_add _ _).trans
        ((congrArg (fun y => V.add y _) ((h.map_mul _ _).trans (congrArg (V.mul _)
            (Weights.Hom.within h ground response moves all f (j + 1) n p.2)))).trans
          (congrArg (V.add _) ((h.map_mul _ _).trans (congrArg (V.mul _)
            (Weights.Hom.within h ground response moves all f j n p.2))))))

end Orders

/-! ## Orders for counting -/

section Counting

variable {S A : Type}

namespace Routes

/-- A counting sum is a total. -/
theorem counting_sum {α : Type} (f : α → Nat) : ∀ l : List α, counting.sum l f = total l f
  | [] => rfl
  | a :: l => congrArg (f a + ·) (counting_sum f l)

end Routes

/-- **For counting the orders rise.** -/
theorem counting_within_le_succ (ground response : S → A → S → Nat) (moves : List A)
    (all : List S) (f : S → Nat) :
    ∀ j n s, counting.within ground response moves all f j n s ≤
      counting.within ground response moves all f (j + 1) n s
  | _, 0, _ => Nat.le_refl _
  | 0, n + 1, s =>
    Nat.le_trans (Nat.le_of_eq (Routes.counting_sum _ _))
      (Nat.le_trans (total_le _ fun p _ =>
          Nat.le_trans (Nat.mul_le_mul_left (ground s p.1 p.2)
              (counting_within_le_succ ground response moves all f 0 n p.2))
            (Nat.le_add_right _ _))
        (Nat.le_of_eq (Routes.counting_sum _ _).symm))
  | j + 1, n + 1, s =>
    Nat.le_trans (Nat.le_of_eq (Routes.counting_sum _ _))
      (Nat.le_trans (total_le _ fun p _ =>
          Nat.add_le_add
            (Nat.mul_le_mul_left (ground s p.1 p.2)
              (counting_within_le_succ ground response moves all f (j + 1) n p.2))
            (Nat.mul_le_mul_left (response s p.1 p.2)
              (counting_within_le_succ ground response moves all f j n p.2)))
        (Nat.le_of_eq (Routes.counting_sum _ _).symm))

/-- **For counting every order is at most the sum over histories.** -/
theorem counting_within_le_transfer (ground response : S → A → S → Nat) (moves : List A)
    (all : List S) (f : S → Nat) :
    ∀ j n s, counting.within ground response moves all f j n s ≤
      counting.transfer (fun s a t => ground s a t + response s a t) moves all f n s
  | _, 0, _ => Nat.le_refl _
  | 0, n + 1, s =>
    Nat.le_trans (Nat.le_of_eq (Routes.counting_sum _ _))
      (Nat.le_trans (total_le _ fun p _ =>
          Nat.le_trans (Nat.mul_le_mul_left (ground s p.1 p.2)
              (counting_within_le_transfer ground response moves all f 0 n p.2))
            (Nat.le_trans (Nat.le_add_right _ _)
              (Nat.le_of_eq (add_mul_split _ _ _).symm)))
        (Nat.le_of_eq (Routes.counting_sum _ _).symm))
  | j + 1, n + 1, s =>
    Nat.le_trans (Nat.le_of_eq (Routes.counting_sum _ _))
      (Nat.le_trans (total_le _ fun p _ =>
          Nat.le_trans
            (Nat.add_le_add
              (Nat.mul_le_mul_left (ground s p.1 p.2)
                (counting_within_le_transfer ground response moves all f (j + 1) n p.2))
              (Nat.mul_le_mul_left (response s p.1 p.2)
                (counting_within_le_transfer ground response moves all f j n p.2)))
            (Nat.le_of_eq (add_mul_split _ _ _).symm))
        (Nat.le_of_eq (Routes.counting_sum _ _).symm))

end Counting

/-! ## The time orderings of P118 are the orders of P82 -/

namespace Routes.SelfLoop

/-- **Order `j` of one configuration is P118's order sum.** Ground weight one and response weight
`M`: order `j` at horizon `n` is the sum over `i ≤ j` of the ways to place `i` responses among `n`
steps times `M ^ i`. -/
theorem within_eq (M : Nat) : ∀ j n,
    counting.within (fun _ _ _ => 1) (fun _ _ _ => M) [()] [()] (fun _ => 1) j n () =
      Loops.orderSum M j n
  | j, 0 => (Loops.orderSum_start M j).symm
  | 0, n + 1 =>
    (Nat.add_zero _).trans ((Nat.one_mul _).trans ((within_eq M 0 n).trans
      ((Loops.orderSum_zero M n).trans (Loops.orderSum_zero M (n + 1)).symm)))
  | j + 1, n + 1 =>
    (Nat.add_zero _).trans
      ((Naturals.add_congr ((Nat.one_mul _).trans (within_eq M (j + 1) n))
          (congrArg (M * ·) (within_eq M j n))).trans
        (Loops.orderSum_step M j n).symm)

/-- **The whole sum is a power.** With both parts, the sum over histories of one configuration is
`(1 + M) ^ n`: where `M` is one, the courses that double around P82's loop. -/
theorem transfer_eq (M : Nat) : ∀ n,
    counting.transfer (fun _ _ _ => 1 + M) [()] [()] (fun _ => 1) n () = (1 + M) ^ n
  | 0 => rfl
  | n + 1 => (Nat.add_zero _).trans ((congrArg ((1 + M) * ·) (transfer_eq M n)).trans
      (Nat.mul_comm _ _))

/-- Each order of one configuration is at most the power, and the order `n` is all of it. -/
theorem within_exact (M n : Nat) : Loops.orderSum M n n = (1 + M) ^ n :=
  (within_eq M n n).symm.trans ((Weights.within_exact (W := counting) (fun _ _ _ => 1)
    (fun _ _ _ => M) [()] [()] (fun _ => 1) n n (Nat.le_refl n) ()).trans (transfer_eq M n))

end Routes.SelfLoop

/-! ## The carried amount as a sum over histories -/

/-- **A point of a route traced back in time:** the level of a condition at a step, or a source,
where the route ends at a starting gap or a gap of the part. -/
inductive RoutePoint (C : Type) where
  | level (t : Nat) (c : C)
  | source

section Routes

variable {F C : Type}

/-- What the formations present outside the part respond with at step `t`, from the level of `d`
at `s` into `c`. -/
def respondAt (part : F → Bool) (k : Nat → F → C → Nat → C → Nat) (present : Nat → List F)
    (t : Nat) (c : C) (s : Nat) (d : C) : Nat :=
  total (present t) fun h => bif part h then 0 else k t h c s d

/-- **The weight of one response.** From the level of `c` at `τ` back to the level of `d` at `s`:
the strengths summed over every step before `τ`, from `s` on, at which the response can occur, the
level holding between. -/
def responseWeight (part : F → Bool) (k : Nat → F → C → Nat → C → Nat) (present : Nat → List F) :
    Nat → C → Nat → C → Nat
  | 0, _, _, _ => 0
  | τ + 1, c, s, d => responseWeight part k present τ c s d +
      bif Nat.ble s τ then respondAt part k present τ c s d else 0

/-- **The weights of a step back.** A response to an earlier level; an end at a source, with what
routes of no response carry; a source stays a source. -/
def routeWeight (cs : List C) (part : F → Bool) (σ : Nat → F → C → Nat)
    (k : Nat → F → C → Nat → C → Nat) (present : Nat → List F) (δ : C → Nat) :
    RoutePoint C → Unit → RoutePoint C → Nat
  | .level τ c, _, .level s d => responseWeight part k present τ c s d
  | .level τ c, _, .source => carriedWithin cs part σ k present δ 0 τ c
  | .source, _, .source => 1
  | .source, _, .level _ _ => 0

/-- What is read at the end of a course: whether it has reached a source. -/
def routeRead : RoutePoint C → Nat
  | .level _ _ => 0
  | .source => 1

/-- The levels of the listed conditions at the steps before `T`. -/
def routeCells (cs : List C) (T : Nat) : List (RoutePoint C) :=
  joinMap (fun s => cs.map (RoutePoint.level s)) (steps 0 T)

/-- The route points listed: the source and the levels before `T`. -/
def routePoints (cs : List C) (T : Nat) : List (RoutePoint C) := .source :: routeCells cs T

/-- **The sum over routes.** P82's transfer of the route weights over the listed route points. -/
def routeSum (cs : List C) (part : F → Bool) (σ : Nat → F → C → Nat)
    (k : Nat → F → C → Nat → C → Nat) (present : Nat → List F) (δ : C → Nat) (T : Nat) :
    Nat → RoutePoint C → Nat :=
  counting.transfer (routeWeight cs part σ k present δ) [()] (routePoints cs T) routeRead

namespace Routes

theorem total_joinMap {α β : Type} (g : α → List β) (q : β → Nat) :
    ∀ l : List α, total (joinMap g l) q = total l fun a => total (g a) q
  | [] => rfl
  | a :: l => (total_append q (joinMap g l) (g a)).trans (congrArg (_ + ·) (total_joinMap g q l))

theorem total_routeCells (cs : List C) (T : Nat) (q : RoutePoint C → Nat) :
    total (routeCells cs T) q = total (steps 0 T) fun s => total cs fun d => q (.level s d) :=
  (total_joinMap _ q _).trans (total_congr (fun s => total_map (RoutePoint.level s) q cs) _)

/-- One step of a counting transfer with one move. -/
theorem transfer_unit {S : Type} (weight : S → Unit → S → Nat) (all : List S) (f : S → Nat)
    (n : Nat) (x : S) :
    counting.transfer weight [()] all f (n + 1) x =
      total all fun m => weight x () m * counting.transfer weight [()] all f n m :=
  (counting_sum (fun p : Unit × S => weight x p.1 p.2 * counting.transfer weight [()] all f n p.2)
      (openSteps [()] all)).trans
    ((total_append _ [] (all.map fun m => ((), m))).trans
      ((Nat.add_zero _).trans (total_map (fun m => ((), m)) _ all)))

/-- Totals of a quantity that is either a total or nothing. -/
theorem total_cond {α : Type} (b : Bool) (q : α → Nat) (as : List α) :
    total as (fun a => bif b then q a else 0) = bif b then total as q else 0 := by
  cases b with
  | true => rfl
  | false => exact total_zero as

theorem cond_mul (b : Bool) (r l : Nat) : (bif b then r else 0) * l = bif b then r * l else 0 := by
  cases b with
  | true => rfl
  | false => exact Nat.zero_mul l

theorem cond_zero_mul (b : Bool) (r l : Nat) :
    (bif b then 0 else r) * l = bif b then 0 else r * l := by
  cases b with
  | true => exact Nat.zero_mul l
  | false => rfl

theorem total_mul_right {α : Type} (q : α → Nat) (g : Nat) (as : List α) :
    total as (fun a => q a * g) = total as q * g :=
  (total_congr (fun a => Nat.mul_comm (q a) g) as).trans ((total_mul g q as).trans (Nat.mul_comm _ _))

/-- Restricting the steps before `τ + 1 + m` to those up to `τ`. -/
theorem total_upto (g : Nat → Nat) (τ : Nat) :
    ∀ m, total (steps 0 (τ + 1 + m)) (fun s => bif Nat.ble s τ then g s else 0) =
      total (steps 0 (τ + 1)) g
  | 0 => total_congr_on fun s mem =>
      congrArg (fun b => bif b then g s else 0)
        (Nat.ble_eq_true_of_le (Propagation.le_of_mem_steps_upto mem))
  | m + 1 =>
    (steps_last (fun s => bif Nat.ble s τ then g s else 0) 0 (τ + 1 + m)).trans
      ((congrArg (· + _) (total_upto g τ m)).trans
        ((congrArg (fun b => total (steps 0 (τ + 1)) g + bif b then g (0 + (τ + 1 + m)) else 0)
          (Naturals.ble_false_of_lt (Nat.lt_of_lt_of_le (Nat.lt_succ_self τ)
            (Nat.le_trans (Nat.le_add_right (τ + 1) m) (Nat.le_of_eq (Nat.zero_add _).symm))))).trans
          (Nat.add_zero _)))

theorem total_upto_of_le (g : Nat → Nat) {τ T : Nat} (le : τ + 1 ≤ T) :
    total (steps 0 T) (fun s => bif Nat.ble s τ then g s else 0) = total (steps 0 (τ + 1)) g :=
  match gap_of_le le with
  | ⟨m, split⟩ => (congrArg (fun T => total (steps 0 T) _) split).trans (total_upto g τ m)

end Routes

variable {cs : List C} {part : F → Bool} {σ : Nat → F → C → Nat}
  {k : Nat → F → C → Nat → C → Nat} {present : Nat → List F} {δ : C → Nat}

/-- **What the formations give across a step, by order.** From levels `l`, the formations present
give what they give from no levels, with each response's strength times the level it reads. -/
theorem give_split (l : Nat → C → Nat) (t : Nat) (c : C) :
    total (present t) (fun h => carriedGive cs part σ k t h c l) =
      total (present t) (fun h => carriedGive cs part σ k t h c fun _ _ => 0) +
        total (steps 0 (t + 1)) fun s => total cs fun d => respondAt part k present t c s d * l s d :=
  have each : ∀ h, carriedGive cs part σ k t h c l = carriedGive cs part σ k t h c (fun _ _ => 0) +
      bif part h then 0 else total (steps 0 (t + 1)) fun s => total cs fun d => k t h c s d * l s d := by
    intro h
    cases hp : part h with
    | true => rw [carriedGive_of_part hp, carriedGive_of_part hp]; rfl
    | false =>
      rw [carriedGive_of_rest hp, carriedGive_of_rest hp]
      exact ((Nat.zero_add _).symm.trans (congrArg (· + _) (total_eq_zero fun _ _ =>
        total_eq_zero fun _ _ => Nat.mul_zero _).symm))
  have spread : ∀ h, (bif part h then 0 else total (steps 0 (t + 1)) fun s => total cs fun d =>
      k t h c s d * l s d) = total (steps 0 (t + 1)) fun s => total cs fun d =>
        (bif part h then 0 else k t h c s d) * l s d := by
    intro h
    cases part h with
    | true => exact (total_eq_zero fun _ _ => total_eq_zero fun _ _ => Nat.zero_mul _).symm
    | false => rfl
  (total_congr each _).trans ((total_add _ _ _).trans (congrArg (_ + ·)
    ((total_congr spread _).trans
      ((total_swap (fun h s => total cs fun d => (bif part h then 0 else k t h c s d) * l s d)
          (steps 0 (t + 1)) (present t)).trans
        (total_congr (fun s =>
          (total_swap (fun h d => (bif part h then 0 else k t h c s d) * l s d) cs (present t)).trans
            (total_congr (fun d => Routes.total_mul_right
              (fun h => bif part h then 0 else k t h c s d) (l s d) (present t)) cs)) _)))))

/-- **What is carried from given levels is linear in them.** Up to `T`, what the strengths carry
from levels `l` is what routes of no response carry, with each response's weight times the level
it reads. -/
theorem carriedFrom_eq_routes (l : Nat → C → Nat) {T : Nat} :
    ∀ τ, τ ≤ T → ∀ c, carriedFrom cs part σ k present δ l τ c =
      carriedWithin cs part σ k present δ 0 τ c +
        total (steps 0 T) fun s => total cs fun d => responseWeight part k present τ c s d * l s d
  | 0, _, c =>
    (Nat.add_zero (δ c)).symm.trans (congrArg (δ c + ·)
      (total_eq_zero fun _ _ => total_eq_zero fun _ _ => Nat.zero_mul _).symm)
  | τ + 1, le, c =>
    have restrict : (total (steps 0 T) fun s => total cs fun d =>
        (bif Nat.ble s τ then respondAt part k present τ c s d else 0) * l s d) =
          total (steps 0 (τ + 1)) fun s => total cs fun d => respondAt part k present τ c s d * l s d :=
      (total_congr (fun s => (total_congr (fun d => Routes.cond_mul (Nat.ble s τ)
          (respondAt part k present τ c s d) (l s d)) cs).trans
          (Routes.total_cond (Nat.ble s τ) (fun d => respondAt part k present τ c s d * l s d) cs))
        (steps 0 T)).trans
        (Routes.total_upto_of_le (fun s => total cs fun d => respondAt part k present τ c s d * l s d)
          le)
    (Naturals.add_congr (carriedFrom_eq_routes l τ (Nat.le_of_succ_le le) c)
        (give_split l τ c)).trans
      ((Nat.add_add_add_comm _ _ _ _).trans (congrArg (_ + ·)
        ((congrArg (_ + ·) restrict.symm).trans
          ((total_add _ _ _).symm.trans (total_congr (fun s =>
            (total_add _ _ cs).symm.trans (total_congr (fun d =>
              (add_mul_split (responseWeight part k present τ c s d)
                (bif Nat.ble s τ then respondAt part k present τ c s d else 0) (l s d)).symm) cs)) _)))))

/-- What a source gives: one, at every horizon. -/
theorem routeSum_source (T : Nat) :
    ∀ n, routeSum cs part σ k present δ T n .source = 1
  | 0 => rfl
  | n + 1 =>
    (Routes.transfer_unit _ _ _ n _).trans
      ((congrArg (· + _) ((Nat.one_mul _).trans (routeSum_source T n))).trans
        ((congrArg (1 + ·) ((Routes.total_routeCells cs T _).trans (total_eq_zero fun _ _ =>
          total_eq_zero fun _ _ => Nat.zero_mul _))).trans (Nat.add_zero 1)))

/-- One step back from a level. -/
theorem routeSum_level (T n τ : Nat) (c : C) :
    routeSum cs part σ k present δ T (n + 1) (.level τ c) =
      carriedWithin cs part σ k present δ 0 τ c +
        total (steps 0 T) fun s => total cs fun d =>
          responseWeight part k present τ c s d * routeSum cs part σ k present δ T n (.level s d) :=
  (Routes.transfer_unit _ _ _ n _).trans (Naturals.add_congr
    ((congrArg (_ * ·) (routeSum_source T n)).trans (Nat.mul_one _))
    (Routes.total_routeCells cs T _))

/-- **Each order of the carried amount is a sum over histories.** Up to `T`, the sum over routes
of horizon `j + 1` is the order `j` of the carried amount at every condition: P118's order is
P82's horizon. -/
theorem routeSum_eq_carriedWithin {T : Nat} :
    ∀ j τ, τ ≤ T → ∀ c, routeSum cs part σ k present δ T (j + 1) (.level τ c) =
      carriedWithin cs part σ k present δ j τ c
  | 0, τ, _, c =>
    (routeSum_level T 0 τ c).trans ((congrArg (_ + ·) (total_eq_zero fun _ _ =>
      total_eq_zero fun _ _ => Nat.mul_zero _)).trans (Nat.add_zero _))
  | j + 1, τ, le, c =>
    (routeSum_level T (j + 1) τ c).trans
      ((congrArg (_ + ·) (total_congr_on fun s mem => total_congr (fun d =>
          congrArg (responseWeight part k present τ c s d * ·) (routeSum_eq_carriedWithin j s
            (Nat.le_of_lt (Nat.lt_of_lt_of_le (Propagation.between_of_mem_steps mem).2
              (Nat.le_of_eq (Nat.zero_add T)))) d)) cs)).trans
        (carriedFrom_eq_routes (carriedWithin cs part σ k present δ j) τ le c).symm)

/-- **Each order is the sum over every course of its horizon.** -/
theorem carriedWithin_eq_courses {T : Nat} (j τ : Nat) (le : τ ≤ T) (c : C) :
    carriedWithin cs part σ k present δ j τ c =
      counting.sum (courses [()] (routePoints cs T) (j + 1))
        (counting.along (routeWeight cs part σ k present δ) routeRead (.level τ c)) :=
  (routeSum_eq_carriedWithin j τ le c).symm.trans
    (Weights.sum_courses (routeWeight cs part σ k present δ) [()] (routePoints cs T) routeRead
      (j + 1) (.level τ c)).symm

/-- **The carried amount is a sum over histories.** At step `t`, it is the sum over every course of
`t + 1` steps back through the route points before `t`. -/
theorem carried_eq_courses (t : Nat) (c : C) :
    carried cs part σ k present δ t c =
      counting.sum (courses [()] (routePoints cs t) (t + 1))
        (counting.along (routeWeight cs part σ k present δ) routeRead (.level t c)) :=
  (carried_eq_carriedWithin t c).trans (carriedWithin_eq_courses t t (Nat.le_refl t) c)

/-- **A horizon past the step is exact.** -/
theorem routeSum_exact {T : Nat} (j τ : Nat) (le : τ ≤ T) (within : τ ≤ j) (c : C) :
    routeSum cs part σ k present δ T (j + 1) (.level τ c) = carried cs part σ k present δ τ c :=
  (routeSum_eq_carriedWithin j τ le c).trans (carriedWithin_exact j τ within c)

/-- **Longer horizons carry more.** -/
theorem routeSum_mono {T j j' : Nat} (le' : j ≤ j') (τ : Nat) (le : τ ≤ T) (c : C) :
    routeSum cs part σ k present δ T (j + 1) (.level τ c) ≤
      routeSum cs part σ k present δ T (j' + 1) (.level τ c) :=
  Nat.le_trans (Nat.le_of_eq (routeSum_eq_carriedWithin j τ le c))
    (Nat.le_trans (carriedWithin_mono le' τ c) (Nat.le_of_eq (routeSum_eq_carriedWithin j' τ le c).symm))

/-- **Every horizon is at most the carried amount.** -/
theorem routeSum_le_carried {T : Nat} (j τ : Nat) (le : τ ≤ T) (c : C) :
    routeSum cs part σ k present δ T (j + 1) (.level τ c) ≤ carried cs part σ k present δ τ c :=
  Nat.le_trans (Nat.le_of_eq (routeSum_eq_carriedWithin j τ le c)) (carriedWithin_le_carried j τ c)

/-- **What a horizon misses.** With the part giving no gap, starting gaps at most `D` and the
strengths into each condition summing to at most `M` at each step, a horizon of `j + 1` misses at
most `Loops.missBound M D j t`. -/
theorem carried_le_routeSum_add {M D T : Nat} (start : ∀ c, δ c ≤ D)
    (into : ∀ t c, inflow cs part k present t c ≤ M) (j t : Nat) (le : t ≤ T) (c : C) :
    carried cs part (fun _ _ _ => 0) k present δ t c ≤
      routeSum cs part (fun _ _ _ => 0) k present δ T (j + 1) (.level t c) + Loops.missBound M D j t :=
  Nat.le_trans (carried_le_carriedWithin_add start into j t c)
    (Nat.le_of_eq (congrArg (· + _) (routeSum_eq_carriedWithin j t le c).symm))

/-- **A finite horizon is exact exactly where no loop lies upstream.** With every condition listed,
stationary strengths and the same formations at every step, some horizon of the sum over routes is
exact at `c` at every step from every starting gap exactly where no loop lies upstream of `c`. -/
theorem finite_horizon_iff_no_loop (every : ∀ c, c ∈ cs) (K : F → C → C → Nat) (hs : List F)
    (c : C) :
    (∀ δ : C → Nat, ∃ j, ∀ t, routeSum cs part σ (stationary K) (fun _ => hs) δ t (j + 1)
        (.level t c) = carried cs part σ (stationary K) (fun _ => hs) δ t c) ↔
      ∀ e, Upstream cs part (stationary K) (fun _ => hs) e c →
        ¬ OnLoop cs part (stationary K) (fun _ => hs) e :=
  have same : ∀ δ j t, routeSum cs part σ (stationary K) (fun _ => hs) δ t (j + 1) (.level t c) =
      carriedWithin cs part σ (stationary K) (fun _ => hs) δ j t c :=
    fun _ j t => routeSum_eq_carriedWithin j t (Nat.le_refl t) c
  ⟨fun exact => (finite_order_iff_no_loop_stationary every K hs c).mp fun δ =>
      match exact δ with
      | ⟨j, all⟩ => ⟨j, fun t => (same δ j t).symm.trans (all t)⟩,
   fun noLoop δ =>
      match (finite_order_iff_no_loop_stationary every K hs c).mpr noLoop δ with
      | ⟨j, all⟩ => ⟨j, fun t => (same δ j t).trans (all t)⟩⟩

end Routes

end Becoming
