import Becoming.Amounts
import Becoming.Resolution
import Becoming.Recurrence
import Becoming.Branching

/-!
# Least loss: rest over amounts that may be dense

The spine counts amounts in whole numbers, and its rest laws take their force from them: a
whole number that falls strictly falls by at least one, and no whole number lies beyond its own
count of ones. Every law of the rest family reaches its conclusion through one of two descents
on whole numbers, `falls_not_recurring` (taking from a closed family does not recur,
`Flow.taking_not_recurring_from`, and a continuing family is fed from beyond,
`Flow.fed_from_beyond`) or `falls_stop_unrefuted` (that a world comes to rest cannot be
refuted, `World.rests_unrefuted`, `World.comes_to_rest_unrefuted`,
`World.rests_unrefuted_enclosed`). This module states that descent over amounts that may be
dense, with what the whole numbers supplied named as two premises.

* **Amounts and the least-loss law** are stated in `Becoming.Amounts`, below the rest family,
  which proves its laws as their whole-number instance (`falls_not_recurring` from
  `Amounts.rests`, `falls_stop_unrefuted` from `Amounts.rests_unrefuted`,
  `Flow.taking_not_recurring_from` from `Amounts.family_rests_of_archimedean`,
  `Flow.takers_within_on` from `Amounts.losses_within`, `Flow.change_stops_unrefuted` from
  `Amounts.rests_unrefuted`, and through them `World.rests_unrefuted_enclosed`). This module states
  that each of the two premises is needed, and what rest has to do with return.
* **Each premise is needed.**
  - *Without a least loss.* In dyadic amounts (`Dyadic`, `num / 2 ^ exp`), which are dense
    (`Dyadic.half_below`) and Archimedean (`Dyadic.archimedean`), the stock halves at every step,
    `1 / 2 ^ t`, each step losing `1 / 2 ^ (t + 1)`: every loss is above nothing, no amount above
    nothing is within every loss, and the stock falls at every step, so it never rests
    (`Halving.never_rests`). The losses add to within the stock, as the loss law requires.
  - *Without the bound by least losses.* In layered amounts (`Layered`: a dyadic coarse layer and
    a whole-number fine layer counting only where the coarse layers agree), the stock falls by a
    least loss of one fine unit at every step, and lies beyond every multiple of it, so it never
    rests (`Layered.never_rests`). Layered amounts are not Archimedean (`Layered.not_archimedean`),
    so the approach to rest fails there too.
  - *Approach without rest.* The halving stock comes arbitrarily near rest, as the approach law
    says, and still falls at every step (`Halving.approaches_without_reaching`): with no least
    loss, approach does not become rest, as in exponential relaxation.
  - *Takers without bound, replenishment bounded.* With halving takes, `2 ^ (t + 1)` takers each
    take `1 / 2 ^ (t + 1)` at the step from `t`, one whole in all: the takers are more without
    end, every take is above nothing, and one whole given at each step balances them
    (`Halving.takes_halve`). More without end needs replenishment without bound only with a least
    take (`Amounts.replenishment_unbounded`).
* **Rest and return.** Over finitely many configurations, a law that merges nothing returns every
  configuration (`Law.Lossless.returns`, `Becoming.Recurrence`), so an amount that does not rise
  along an orbit regains its value (`Law.Lossless.regains`) and every loss along it is nothing
  (`Law.Lossless.loses_nothing`). A loss above nothing needs a law that merges
  (`Law.loss_needs_merge`). The same holds along a run of every process
  (`Branching.Lossless.loses_nothing`, `Branching.loss_needs_merge`). Rest is a law of descriptions that lump configurations and dissipate;
  a finite world that merges nothing returns rather than rests.

What the whole numbers carry in the rest family is exactly these two premises: a least loss at
each change, and every stock within finitely many least losses. Approach to rest needs no least
loss, only Archimedean amounts; rest, the change counted not recurring, needs the least loss as
well. Physics supplies amounts of energy in real numbers, and the second law, a non-negative production of entropy, names no least
loss per step; so in a continuous reading the rest laws hold where some least loss per change is
given (a least gap between the levels of a bounded quantised system, a threshold of detection,
Landauer's bound `kT ln 2` per erased bit at a temperature bounded below are candidates), and
fail, as in `Halving`, where losses shrink without a floor. Which physical systems have a least
loss is not settled here. `Flow`, `Web` and `World` still read their levels in whole numbers;
this module states the step on which the rest laws turn for any amounts, not those structures
over any amounts. `Becoming.Resolution` reads the same boundary at a unit that may split, and its
`Asymptote` and `Dwindle` are halving at a refining unit. Real numbers are not constructed in the
core; dyadic amounts witness that density alone does not break the law. No ethical predicate,
ranking or axiom occurs.
-/

namespace Becoming

/-! ## Dyadic amounts: dense, Archimedean, and without a least loss -/

/-- A dyadic amount, `num / 2 ^ exp`. -/
structure Dyadic where
  num : Nat
  exp : Nat

namespace Dyadic

theorem ext' : ∀ {a b : Dyadic}, a.num = b.num → a.exp = b.exp → a = b
  | ⟨_, _⟩, ⟨_, _⟩, rfl, rfl => rfl

/-- Dyadic amounts added. -/
def add (a b : Dyadic) : Dyadic := ⟨a.num * 2 ^ b.exp + b.num * 2 ^ a.exp, a.exp + b.exp⟩

/-- One dyadic amount within another. -/
def le (a b : Dyadic) : Prop := a.num * 2 ^ b.exp ≤ b.num * 2 ^ a.exp

/-- Nothing. -/
def zero : Dyadic := ⟨0, 0⟩

theorem le_trans' {a b c : Dyadic} (ab : le a b) (bc : le b c) : le a c :=
  Nat.le_of_mul_le_mul_right
    (calc a.num * 2 ^ c.exp * 2 ^ b.exp
        = a.num * 2 ^ b.exp * 2 ^ c.exp := Naturals.mul_right_comm _ _ _
      _ ≤ b.num * 2 ^ a.exp * 2 ^ c.exp := Nat.mul_le_mul_right _ ab
      _ = b.num * 2 ^ c.exp * 2 ^ a.exp := Naturals.mul_right_comm _ _ _
      _ ≤ c.num * 2 ^ b.exp * 2 ^ a.exp := Nat.mul_le_mul_right _ bc
      _ = c.num * 2 ^ a.exp * 2 ^ b.exp := Naturals.mul_right_comm _ _ _)
    (Nat.two_pow_pos _)

theorem add_assoc' (a b c : Dyadic) : add (add a b) c = add a (add b c) :=
  ext' (by
    show (a.num * 2 ^ b.exp + b.num * 2 ^ a.exp) * 2 ^ c.exp + c.num * 2 ^ (a.exp + b.exp)
      = a.num * 2 ^ (b.exp + c.exp) + (b.num * 2 ^ c.exp + c.num * 2 ^ b.exp) * 2 ^ a.exp
    rw [add_mul_split, add_mul_split, Naturals.pow_add 2 a.exp b.exp, Naturals.pow_add 2 b.exp c.exp,
      mul_assoc_nat a.num, Naturals.mul_right_comm b.num (2 ^ a.exp) (2 ^ c.exp),
      mul_assoc_nat c.num (2 ^ b.exp) (2 ^ a.exp), Nat.mul_comm (2 ^ b.exp) (2 ^ a.exp),
      Nat.add_assoc])
    (Nat.add_assoc _ _ _)

theorem add_comm' (a b : Dyadic) : add a b = add b a :=
  ext' (Nat.add_comm _ _) (Nat.add_comm _ _)

theorem zero_add' (a : Dyadic) : add zero a = a :=
  ext' ((congrArg (· + a.num * 1) (Nat.zero_mul _)).trans ((Nat.zero_add _).trans (Nat.mul_one _)))
    (Nat.zero_add _)

theorem expand (x y e f g : Nat) :
    (x * 2 ^ g + y * 2 ^ e) * 2 ^ (f + g) = x * 2 ^ f * (2 ^ g * 2 ^ g) + y * (2 ^ e * 2 ^ f * 2 ^ g) := by
  rw [add_mul_split, Naturals.pow_add, mul_assoc_nat x, mul_turn (2 ^ g) (2 ^ f), ← mul_assoc_nat x,
    mul_assoc_nat y, ← mul_assoc_nat (2 ^ e)]

theorem add_le_add_right' {a b : Dyadic} (c : Dyadic) (h : le a b) : le (add a c) (add b c) := by
  show (a.num * 2 ^ c.exp + c.num * 2 ^ a.exp) * 2 ^ (b.exp + c.exp)
    ≤ (b.num * 2 ^ c.exp + c.num * 2 ^ b.exp) * 2 ^ (a.exp + c.exp)
  rw [expand, expand, Nat.mul_comm (2 ^ b.exp) (2 ^ a.exp)]
  exact Nat.add_le_add_right (Nat.mul_le_mul_right _ h) _

theorem le_of_add_le_add_right' {a b : Dyadic} (c : Dyadic) (h : le (add a c) (add b c)) :
    le a b := by
  have h' : (a.num * 2 ^ c.exp + c.num * 2 ^ a.exp) * 2 ^ (b.exp + c.exp)
      ≤ (b.num * 2 ^ c.exp + c.num * 2 ^ b.exp) * 2 ^ (a.exp + c.exp) := h
  rw [expand, expand, Nat.mul_comm (2 ^ b.exp) (2 ^ a.exp)] at h'
  exact Nat.le_of_mul_le_mul_right (le_of_add_le_add_right _ h')
    (Nat.mul_pos (Nat.two_pow_pos _) (Nat.two_pow_pos _))

theorem zero_le' (a : Dyadic) : le zero a :=
  Nat.le_trans (Nat.le_of_eq (Nat.zero_mul _)) (Nat.zero_le _)

/-- Dyadic amounts with their laws. -/
def amounts : Amounts Dyadic where
  zero := zero
  add := add
  le := le
  le_refl := fun _ => Nat.le_refl _
  le_trans := le_trans'
  add_assoc := add_assoc'
  add_comm := add_comm'
  zero_add := zero_add'
  add_le_add_right := add_le_add_right'
  le_of_add_le_add_right := le_of_add_le_add_right'
  zero_le := zero_le'

/-- An amount above nothing has a positive numerator. -/
theorem num_pos {a : Dyadic} (positive : ¬ le a zero) : 0 < a.num :=
  Nat.pos_of_ne_zero fun none_ => positive (Nat.le_of_eq
    ((congrArg (· * 2 ^ 0) none_).trans ((Nat.zero_mul _).trans (Nat.zero_mul _).symm)))

/-- Dense: below every amount above nothing lies another above nothing, its half. -/
theorem half_below {a : Dyadic} (positive : ¬ le a zero) :
    ¬ le ⟨a.num, a.exp + 1⟩ zero ∧ ¬ le a ⟨a.num, a.exp + 1⟩ :=
  ⟨fun le => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (num_pos positive)
      (Nat.le_trans (Nat.le_of_eq (Nat.mul_one _).symm) (Nat.le_trans le (Nat.le_of_eq (Nat.zero_mul _))))),
   fun le => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le (Nat.pow_lt_pow_succ (Nat.lt_succ_self 1))
      (Nat.le_of_mul_le_mul_left le (num_pos positive)))⟩

/-- Copies of an amount are at least the amount with its numerator multiplied. -/
theorem times_ge (n k : Nat) : ∀ m, le ⟨m * n, k⟩ (amounts.times m ⟨n, k⟩)
  | 0 => Nat.le_of_eq ((congrArg (· * 2 ^ 0) (Nat.zero_mul n)).trans
      ((Nat.zero_mul _).trans (Nat.zero_mul _).symm))
  | m + 1 => le_trans' (b := add ⟨m * n, k⟩ ⟨n, k⟩)
      (show (m + 1) * n * 2 ^ (k + k) ≤ (m * n * 2 ^ k + n * 2 ^ k) * 2 ^ k from by
        rw [← add_mul_split, Nat.succ_mul, Naturals.pow_add, mul_assoc_nat]
        exact Nat.le_refl _)
      (add_le_add_right' ⟨n, k⟩ (times_ge n k m))

/-- Dyadic amounts are Archimedean. -/
theorem archimedean : amounts.Archimedean :=
  fun a e positive => ⟨a.num * 2 ^ e.exp + 1, fun le =>
    have lower := le_trans' (times_ge e.num e.exp (a.num * 2 ^ e.exp + 1)) le
    Nat.lt_irrefl _ (Nat.lt_of_lt_of_le (Nat.lt_succ_self (a.num * 2 ^ e.exp))
      (Nat.le_trans (Nat.le_mul_of_pos_right _ (num_pos positive))
        (Nat.le_trans (Nat.le_mul_of_pos_right _ (Nat.two_pow_pos a.exp)) lower)))⟩

end Dyadic

/-! ## Halving: a loss at every step and no rest -/

namespace Halving

/-- The stock halves at every step: `1 / 2 ^ t`. -/
def stock (t : Nat) : Dyadic := ⟨1, t⟩

/-- The loss of the step from `t`, half the stock: `1 / 2 ^ (t + 1)`. -/
def loss (t : Nat) : Dyadic := ⟨1, t + 1⟩

theorem falls (t : Nat) : Dyadic.amounts.le (Dyadic.amounts.add (stock (t + 1)) (loss t)) (stock t) := by
  show (1 * 2 ^ (t + 1) + 1 * 2 ^ (t + 1)) * 2 ^ t ≤ 1 * 2 ^ ((t + 1) + (t + 1))
  rw [Nat.one_mul, Nat.one_mul, ← Nat.mul_two, Naturals.pow_add 2 (t + 1) (t + 1),
    mul_assoc_nat, Nat.mul_comm 2 (2 ^ t)]
  exact Nat.le_refl _

theorem loss_positive (t : Nat) : ¬ Dyadic.amounts.le (loss t) Dyadic.amounts.zero :=
  fun le => Nat.not_succ_le_zero 0 (Nat.le_trans le (Nat.le_of_eq (Nat.zero_mul _)))

/-- No amount above nothing is within every loss. -/
theorem no_least_loss (ε : Dyadic) (positive : ¬ Dyadic.amounts.le ε Dyadic.amounts.zero) :
    ¬ ∀ t, Dyadic.amounts.le ε (loss t) :=
  fun least => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le (Nat.pow_lt_pow_succ (Nat.lt_succ_self 1))
    (Nat.le_trans (Nat.le_mul_of_pos_left _ (Dyadic.num_pos positive))
      (Nat.le_trans (least ε.exp) (Nat.le_of_eq (Nat.one_mul _)))))

theorem falls_strictly (t : Nat) : ¬ Dyadic.amounts.le (stock t) (stock (t + 1)) :=
  fun le => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le (Nat.pow_lt_pow_succ (Nat.lt_succ_self 1))
    (Nat.le_trans (Nat.le_of_eq (Nat.one_mul _).symm) (Nat.le_trans le (Nat.le_of_eq (Nat.one_mul _)))))

/-- **The geometric counterexample.** In dyadic amounts, dense and Archimedean, the stock halves
at every step: across each step it falls by its loss, every loss is above nothing, no amount above
nothing is within every loss, and the stock falls at every step, so it never rests. Every premise
of `Amounts.rests` holds for the steps at which the stock falls except the least loss. -/
theorem never_rests :
    (∀ t, Dyadic.amounts.le (Dyadic.amounts.add (stock (t + 1)) (loss t)) (stock t)) ∧
    (∀ t, Dyadic.amounts.le (stock (t + 1)) (stock t)) ∧
    (∀ t, ¬ Dyadic.amounts.le (loss t) Dyadic.amounts.zero) ∧
    (∀ ε, ¬ Dyadic.amounts.le ε Dyadic.amounts.zero → ¬ ∀ t, Dyadic.amounts.le ε (loss t)) ∧
    Dyadic.amounts.Archimedean ∧
    ∀ N, ∃ t, N ≤ t ∧ ¬ Dyadic.amounts.le (stock t) (stock (t + 1)) :=
  ⟨falls, fun t => Dyadic.amounts.le_trans (Amounts.le_add_right _ _) (falls t), loss_positive,
   no_least_loss, Dyadic.archimedean, fun N => ⟨N, Nat.le_refl N, falls_strictly N⟩⟩

/-- **Approaching rest without reaching it.** The halving stock comes arbitrarily near rest, as
every stock with summable losses in Archimedean amounts does: for every `ε` above nothing there is
a count `m` such that no `m` steps each lose at least `ε`, and steps losing at least `ε` do not
recur. Yet it falls at every step. With no least loss, approach does not become rest, as in
exponential relaxation. -/
theorem approaches_without_reaching :
    (∀ ε, ¬ Dyadic.amounts.le ε Dyadic.amounts.zero →
      (∃ m, ¬ ∃ f : Nat → Nat, 0 ≤ f 0 ∧ (∀ i, f i < f (i + 1)) ∧
        ∀ i, i < m → Dyadic.amounts.le ε (loss (f i))) ∧
      ¬ ∀ N, ∃ t, N ≤ t ∧ Dyadic.amounts.le ε (loss t)) ∧
    ∀ t, ¬ Dyadic.amounts.le (stock t) (stock (t + 1)) :=
  ⟨fun _ positive =>
    ⟨Amounts.few_large_losses_of_archimedean Dyadic.archimedean (fun t _ => falls t) positive,
     Amounts.approaches_rest (T := 0) Dyadic.archimedean (fun t _ => falls t) positive⟩,
   falls_strictly⟩

/-- Copies of an amount are at most the amount with its numerator multiplied. -/
theorem times_le_num (n k : Nat) : ∀ m, Dyadic.le (Dyadic.amounts.times m ⟨n, k⟩) ⟨m * n, k⟩
  | 0 => Dyadic.zero_le' _
  | m + 1 => Dyadic.le_trans' (Dyadic.add_le_add_right' ⟨n, k⟩ (times_le_num n k m))
      (show (m * n * 2 ^ k + n * 2 ^ k) * 2 ^ k ≤ (m + 1) * n * 2 ^ (k + k) from by
        rw [← add_mul_split, Nat.succ_mul, Naturals.pow_add, mul_assoc_nat]
        exact Nat.le_refl _)

theorem le_two_pow : ∀ K, K ≤ 2 ^ K
  | 0 => Nat.zero_le _
  | K + 1 => Nat.le_trans (Nat.add_le_add (le_two_pow K) (Nat.two_pow_pos K))
      (Nat.le_of_eq ((Nat.mul_two _).symm.trans (Nat.pow_succ 2 K).symm))

/-- One whole. -/
def one : Dyadic := ⟨1, 0⟩

/-- At the step from `t`, `2 ^ (t + 1)` takers take `loss t` each, `1 / 2 ^ (t + 1)`: one whole
in all. -/
theorem takes_within_one (t : Nat) :
    Dyadic.amounts.le (Dyadic.amounts.times (2 ^ (t + 1)) (loss t)) one :=
  Dyadic.le_trans' (times_le_num 1 (t + 1) (2 ^ (t + 1)))
    (Nat.le_of_eq ((Nat.mul_one _).trans ((Nat.mul_one _).trans (Nat.one_mul _).symm)))

/-- **The counterexample to replenishment without bound, with no least take.** In dyadic amounts,
dense and Archimedean, a family keeps a stock of one whole and is given one whole at every step;
at the step from `t`, `2 ^ (t + 1)` takers take `1 / 2 ^ (t + 1)` each. The family is balanced
(its stock after a step with the uptake is within its stock before with the replenishment), each
take is above nothing, the takers are more without end (for every number, from some step on at
least that many take), and the replenishment is one whole at every step; what fails is
the least take: no amount above nothing is within every take. So the whole-number law
`Flow.More.replenishment_unbounded` needs that each taker takes at least a least amount, as
`Amounts.replenishment_unbounded` states. -/
theorem takes_halve :
    (∀ t, Dyadic.amounts.le
      (Dyadic.amounts.add one (Dyadic.amounts.times (2 ^ (t + 1)) (loss t)))
      (Dyadic.amounts.add one one)) ∧
    (∀ t, ¬ Dyadic.amounts.le (loss t) Dyadic.amounts.zero) ∧
    (∀ K, ∃ T, ∀ t, T ≤ t → K ≤ 2 ^ (t + 1)) ∧
    ∀ ε, ¬ Dyadic.amounts.le ε Dyadic.amounts.zero → ¬ ∀ t, Dyadic.amounts.le ε (loss t) :=
  ⟨fun t => Amounts.add_le_add_left one (takes_within_one t), loss_positive,
   fun K => ⟨K, fun _ later => Nat.le_trans (le_two_pow K)
     (Nat.pow_le_pow_right (Nat.succ_pos 1) (Nat.le_succ_of_le later))⟩,
   no_least_loss⟩

end Halving

/-! ## Layered amounts: a least loss, and a stock beyond every multiple of it -/

/-- A layered amount: a coarse dyadic amount and a fine whole-number one, the fine layer counting
only where the coarse layers are each within the other. -/
structure Layered where
  coarse : Dyadic
  fine : Nat

namespace Layered

theorem ext' : ∀ {a b : Layered}, a.coarse = b.coarse → a.fine = b.fine → a = b
  | ⟨_, _⟩, ⟨_, _⟩, rfl, rfl => rfl

/-- Layered amounts added, layer by layer. -/
def add (a b : Layered) : Layered := ⟨Dyadic.add a.coarse b.coarse, a.fine + b.fine⟩

/-- One layered amount within another: the coarse layer within, and where the coarse layers are
each within the other, the fine layer within. -/
def le (a b : Layered) : Prop :=
  Dyadic.le a.coarse b.coarse ∧ (Dyadic.le b.coarse a.coarse → a.fine ≤ b.fine)

/-- Nothing. -/
def zero : Layered := ⟨Dyadic.zero, 0⟩

theorem le_trans' {a b c : Layered} (ab : le a b) (bc : le b c) : le a c :=
  ⟨Dyadic.le_trans' ab.1 bc.1, fun ca =>
    Nat.le_trans (ab.2 (Dyadic.le_trans' bc.1 ca)) (bc.2 (Dyadic.le_trans' ca ab.1))⟩

theorem add_le_add_right' {a b : Layered} (c : Layered) (h : le a b) : le (add a c) (add b c) :=
  ⟨Dyadic.add_le_add_right' c.coarse h.1, fun ba =>
    Nat.add_le_add_right (h.2 (Dyadic.le_of_add_le_add_right' c.coarse ba)) _⟩

theorem le_of_add_le_add_right' {a b : Layered} (c : Layered) (h : le (add a c) (add b c)) :
    le a b :=
  ⟨Dyadic.le_of_add_le_add_right' c.coarse h.1, fun ba =>
    _root_.Becoming.le_of_add_le_add_right _ (h.2 (Dyadic.add_le_add_right' c.coarse ba))⟩

/-- Layered amounts with their laws. They are not Archimedean: a fine amount above nothing,
taken any number of times, stays within every coarse amount above nothing. -/
def amounts : Amounts Layered where
  zero := zero
  add := add
  le := le
  le_refl := fun _ => ⟨Nat.le_refl _, fun _ => Nat.le_refl _⟩
  le_trans := le_trans'
  add_assoc := fun _ _ _ => ext' (Dyadic.add_assoc' _ _ _) (Nat.add_assoc _ _ _)
  add_comm := fun _ _ => ext' (Dyadic.add_comm' _ _) (Nat.add_comm _ _)
  zero_add := fun _ => ext' (Dyadic.zero_add' _) (Nat.zero_add _)
  add_le_add_right := add_le_add_right'
  le_of_add_le_add_right := le_of_add_le_add_right'
  zero_le := fun _ => ⟨Dyadic.zero_le' _, fun _ => Nat.zero_le _⟩

/-- The stock: the coarse layer halving at every step, nothing in the fine layer. -/
def stock (t : Nat) : Layered := ⟨Halving.stock t, 0⟩

/-- The least loss: one fine unit, nothing coarse. -/
def least : Layered := ⟨Dyadic.zero, 1⟩

theorem least_positive : ¬ amounts.le least amounts.zero :=
  fun le => Nat.not_succ_le_zero 0 (le.2 (Nat.le_refl _))

/-- Across every step the stock falls by at least the least loss. -/
theorem loses (t : Nat) : amounts.le (amounts.add (stock (t + 1)) least) (stock t) :=
  ⟨Eq.subst (motive := fun x => Dyadic.le x (Halving.stock t))
      (Amounts.add_zero (M := Dyadic.amounts) (Halving.stock (t + 1))).symm
      (Halving.never_rests.2.1 t),
   fun back => absurd (Eq.subst (motive := fun x => Dyadic.le (Halving.stock t) x)
      (Amounts.add_zero (M := Dyadic.amounts) (Halving.stock (t + 1))) back)
      (Halving.falls_strictly t)⟩

/-- Copies of the least loss stay coarse nothing. -/
theorem times_coarse : ∀ m, Dyadic.le (amounts.times m least).coarse Dyadic.zero
  | 0 => Nat.le_refl _
  | m + 1 => Eq.subst (motive := fun x => Dyadic.le x Dyadic.zero)
      (Amounts.add_zero (M := Dyadic.amounts) (amounts.times m least).coarse).symm
      (times_coarse m)

/-- The stock at the start lies beyond every multiple of the least loss. -/
theorem beyond_every_multiple (m : Nat) : amounts.le (amounts.times m least) (stock 0) :=
  ⟨Dyadic.le_trans' (times_coarse m) (Dyadic.zero_le' _), fun above =>
    False.elim (Nat.not_succ_le_zero 0 (Nat.le_trans (Dyadic.le_trans' above (times_coarse m))
      (Nat.le_of_eq (Nat.zero_mul _))))⟩

/-- **The counterexample to rest without the stock's bound.** In layered amounts the stock falls
by at least a least loss above nothing across every step and never rests: it changes at every
step. What fails is the second premise of `Amounts.rests`: the stock at the start lies beyond every
multiple of the least loss. -/
theorem never_rests :
    (∀ t, amounts.le (stock (t + 1)) (stock t)) ∧
    (∀ t, amounts.le (amounts.add (stock (t + 1)) least) (stock t)) ∧
    ¬ amounts.le least amounts.zero ∧
    (∀ m, amounts.le (amounts.times m least) (stock 0)) ∧
    ∀ N, ∃ t, N ≤ t ∧ ¬ amounts.le (stock t) (stock (t + 1)) :=
  ⟨fun t => amounts.le_trans (Amounts.le_add_right _ _) (loses t), loses, least_positive,
   beyond_every_multiple, fun N => ⟨N, Nat.le_refl N, fun le => Halving.falls_strictly N le.1⟩⟩

/-- Layered amounts are not Archimedean: every multiple of the least loss, above nothing, is within
the stock at the start. So the approach to rest needs the Archimedean property: here a bounded
stock loses at least the least loss at every step. -/
theorem not_archimedean : ¬ amounts.Archimedean :=
  fun archimedean => match archimedean (stock 0) least least_positive with
    | ⟨m, within⟩ => within (beyond_every_multiple m)

end Layered

/-! ## Rest and return: dissipation needs a law that merges -/

namespace Branching

open Generative

variable {S : Type} {Act : Type} {P : Process S Act} {A : Type} {M : Amounts A}

/-- **Merging nothing, a run loses nothing**, for every process. Where `P` merges nothing and a
list holds every configuration of a run, an amount that, with each step's loss, is within its
value before the step along the run loses nothing at any step: the run comes back to each of its
configurations (`Branching.Lossless.recurs`), so what it lost it has again. -/
theorem Lossless.loses_nothing (lossless : Lossless P) (r : Run P) {l : List S}
    (held : ∀ n, r.state n ∈ l) {q : S → A} {d : Nat → A}
    (falls : ∀ n, M.le (M.add (q (r.state (n + 1))) (d n)) (q (r.state n))) (n : Nat) :
    M.le (d n) M.zero :=
  match lossless.recurs r held n with
  | ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
  | ⟨e + 1, _, back⟩ =>
    have same : r.state (n + 1 + e) = r.state n :=
      (congrArg r.state (Nat.succ_add n e)).trans back
    have up : M.le (q (r.state n)) (q (r.state (n + 1))) :=
      Eq.subst (motive := fun x => M.le (q x) (q (r.state (n + 1)))) same
        (Amounts.still_within (T := 0) (s := fun k => q (r.state k))
          (fun t _ => M.le_trans (Amounts.le_add_right _ (d t)) (falls t)) e (n + 1)
          (Nat.zero_le _))
    M.le_of_add_le_add_right (q (r.state (n + 1)))
      (M.le_trans (Amounts.le_of_eq (M.add_comm (d n) _))
        (M.le_trans (falls n) (M.le_trans up (Amounts.le_of_eq (M.zero_add _).symm))))

/-- **A loss along a run needs a merge**, for every process: where a list holds every
configuration of a run and an amount, with each step's loss, is within its value before the step
along it, a loss above nothing at some step means the process merges configurations. -/
theorem loss_needs_merge (r : Run P) {l : List S} (held : ∀ n, r.state n ∈ l) {q : S → A}
    {d : Nat → A} (falls : ∀ n, M.le (M.add (q (r.state (n + 1))) (d n)) (q (r.state n)))
    {n : Nat} (positive : ¬ M.le (d n) M.zero) : ¬ Lossless P :=
  fun lossless => positive (lossless.loses_nothing r held falls n)

end Branching

namespace Law

variable {S : Type} {A : Type} {M : Amounts A}

/-- **A law that merges nothing regains its amounts.** Where a list holds every configuration
and the law merges nothing, an amount that does not rise along an orbit is, at its start, within
its value at every step of the orbit: the orbit returns to its start, so nothing it lost stays
lost. -/
theorem Lossless.regains {next : S → S} (lossless : Lossless next) {all : List S}
    (every : ∀ s, s ∈ all) {q : S → A} {s : S}
    (still : ∀ n, M.le (q (orbit next s (n + 1))) (q (orbit next s n))) (n : Nat) :
    M.le (q s) (q (orbit next s n)) :=
  match returns_iff.mp (lossless.returns every s) with
  | ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
  | ⟨p + 1, _, back⟩ =>
    have whole : orbit next s (n + p * n) = s :=
      (congrArg (orbit next s) ((Nat.add_comm n (p * n)).trans (Nat.succ_mul p n).symm)).trans
        (orbit_mul back n)
    Eq.subst (motive := fun x => M.le (q x) (q (orbit next s n))) whole
      (Amounts.still_within (s := fun k => q (orbit next s k)) (fun t _ => still t) (p * n) n
        (Nat.zero_le n))

/-- **Losing nothing, a law loses nothing.** Where a list holds every configuration and the law
merges nothing, an amount that, with each step's loss, is within its value before the step loses
nothing at any step: every loss is within nothing. The law of every process
(`Branching.Lossless.loses_nothing`) along the law's run from `s`. -/
theorem Lossless.loses_nothing {next : S → S} (lossless : Lossless next) {all : List S}
    (every : ∀ s, s ∈ all) {q : S → A} {d : Nat → A} {s : S}
    (falls : ∀ n, M.le (M.add (q (orbit next s (n + 1))) (d n)) (q (orbit next s n)))
    (n : Nat) : M.le (d n) M.zero :=
  Branching.Lossless.loses_nothing lossless (run next s) (fun _ => every _) falls n

/-- **A loss needs a merge.** Where a list holds every configuration and an amount, with each
step's loss, is within its value before the step along an orbit, a loss above nothing at some
step means the law merges configurations: the law of every process (`Branching.loss_needs_merge`)
along the law's run from `s`. The least loss on which the rest laws turn is a premise of laws that
merge: of descriptions that lump configurations, not of a law over finitely many configurations
that merges nothing, which returns rather than rests. -/
theorem loss_needs_merge {next : S → S} {all : List S} (every : ∀ s, s ∈ all) {q : S → A}
    {d : Nat → A} {s : S}
    (falls : ∀ n, M.le (M.add (q (orbit next s (n + 1))) (d n)) (q (orbit next s n)))
    {n : Nat} (positive : ¬ M.le (d n) M.zero) : ¬ Lossless next :=
  Branching.loss_needs_merge (run next s) (fun _ => every _) falls positive

end Law


end Becoming
