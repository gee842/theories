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

* **Amounts.** An addition, associative and commutative with nothing as its unit, and an order
  that addition keeps and that cancels, with nothing least (`Amounts`). Nothing more is asked:
  no amount need be a whole number, and between two amounts there may be a third. The order is a
  preorder, so two representations of one amount are each within the other and no quotient is
  taken.
* **The loss law.** Where across each step from `T` on the amount after the step, with the
  step's loss, is within the amount before, the losses since `T`, added, are within the amount
  at `T` (`Amounts.losses_within`). No least loss is named: in any amounts the losses of a
  falling stock are summable, so a fall at every step does not exhaust the stock unless the
  losses do not shrink.
* **The approach to rest, with no least loss.** Under the same premise, for any `k` steps from `T`
  on each losing at least `ε`, `k` copies of `ε` are within the amount at `T`
  (`Amounts.large_losses_within`); so where `m` copies are not, fewer than `m` steps lose at least
  `ε` (`Amounts.few_large_losses`). In Archimedean amounts this holds for every `ε` above nothing:
  a closed amount comes arbitrarily near rest, and steps losing at least `ε` do not recur
  (`Amounts.few_large_losses_of_archimedean`, `Amounts.approaches_rest`). The Archimedean
  property is the structural premise, and nothing else is asked. In whole numbers, where every
  loss above nothing is at least one, approach is rest: no more steps lose anything than the stock
  at `T` counts (`Amounts.whole_losing_steps`).
* **The least-loss law of rest.** Where an amount does not rise from `T` on and falls by at least
  `ε` across each step at which `P` holds, and `m` copies of `ε` are not within the amount at
  `T`, steps at which `P` holds do not recur (`Amounts.rests`); with every premise read as far
  as can be refuted, it is not the case that after every step from `T` on a later such step stays
  unrefuted (`Amounts.rests_unrefuted`). The two premises are the least loss `ε` and the bound of
  the stock by finitely many least losses. In Archimedean amounts the bound holds for every `ε`
  above nothing, so a least loss alone brings rest (`Amounts.rests_of_archimedean`).
* **A family at rest.** Read a family's stock, uptake and replenishment as amounts: where from
  `T` on the stock after a step with the uptake is within the stock before with the
  replenishment, the replenishment is within the uptake, at each step at which `P` holds the
  replenishment with `ε` is within the uptake, and the stock at `T` lies within fewer than `m`
  copies of `ε`, steps at which `P` holds do not recur (`Amounts.family_rests`, from
  `Amounts.family_still` and `Amounts.family_loses`; in Archimedean amounts
  `Amounts.family_rests_of_archimedean`).
* **Whole numbers are the instance.** In whole-number amounts (`Amounts.whole`, Archimedean,
  `Amounts.whole_archimedean`) the least loss is one and every stock lies within its own count of
  ones, plus one (`Amounts.whole_within`). With these the spine's laws are proved again from the
  least-loss law, their statements unchanged: the two descents (`whole_falls_not_recurring`,
  `whole_falls_stop_unrefuted`); the family laws, each formation taking from a family dissipated
  on losing at least one unit (`Flow.taking_not_recurring_whole` states
  `Flow.taking_not_recurring_from`, through the Archimedean form, and
  `Flow.takers_within_on_whole` states `Flow.takers_within_on`, through the loss law); that
  standing stops changing (`Flow.change_stops_unrefuted_whole` states
  `Flow.change_stops_unrefuted`, each change lowering the total standing by at least one, with no
  decision); and the rest theorem (`World.rests_unrefuted_enclosed_whole` states
  `World.rests_unrefuted_enclosed`).
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

/-- Amounts with their laws: an addition, associative and commutative with nothing as its
unit, and an order that addition keeps and that cancels, with nothing least. No amount is
required to be a whole number, and between two amounts there may be a third. The order is a
preorder: two representations of one amount (`1/2` and `2/4` in `Dyadic`) are each within the
other, so no quotient is taken. -/
structure Amounts (A : Type) where
  zero : A
  add : A → A → A
  le : A → A → Prop
  le_refl : ∀ a, le a a
  le_trans : ∀ {a b c : A}, le a b → le b c → le a c
  add_assoc : ∀ a b c, add (add a b) c = add a (add b c)
  add_comm : ∀ a b, add a b = add b a
  zero_add : ∀ a, add zero a = a
  add_le_add_right : ∀ {a b : A} (c : A), le a b → le (add a c) (add b c)
  le_of_add_le_add_right : ∀ {a b : A} (c : A), le (add a c) (add b c) → le a b
  zero_le : ∀ a, le zero a

namespace Amounts

variable {A : Type} (M : Amounts A)

/-- `n` copies of `a`, added. -/
def times : Nat → A → A
  | 0, _ => M.zero
  | n + 1, a => M.add (times n a) a

/-- The losses `d` of the `n` steps from `S`, added. -/
def sum (d : Nat → A) (S : Nat) : Nat → A
  | 0 => M.zero
  | n + 1 => M.add (sum d S n) (d (S + n))

/-- The amounts are Archimedean: every amount above nothing, taken often enough, is within no
given amount. -/
def Archimedean : Prop :=
  ∀ a e : A, ¬ M.le e M.zero → ∃ m, ¬ M.le (M.times m e) a

variable {M}

theorem add_zero (a : A) : M.add a M.zero = a :=
  (M.add_comm a M.zero).trans (M.zero_add a)

theorem le_of_eq {a b : A} (same : a = b) : M.le a b :=
  same ▸ M.le_refl a

theorem add_le_add_left {a b : A} (c : A) (le : M.le a b) : M.le (M.add c a) (M.add c b) := by
  rw [M.add_comm c a, M.add_comm c b]
  exact M.add_le_add_right c le

theorem le_add_right (a b : A) : M.le a (M.add a b) := by
  have h := add_le_add_left a (M.zero_le b)
  rw [add_zero] at h
  exact h

theorem le_add_left (a b : A) : M.le a (M.add b a) := by
  rw [M.add_comm b a]
  exact le_add_right a b

theorem add_swap (x y z : A) : M.add x (M.add y z) = M.add (M.add x z) y := by
  rw [M.add_comm y z, M.add_assoc]

/-- Copies of a larger amount are larger. -/
theorem times_le {a b : A} (le : M.le a b) : ∀ m, M.le (M.times m a) (M.times m b)
  | 0 => M.le_refl _
  | m + 1 => M.le_trans (M.add_le_add_right a (times_le le m)) (add_le_add_left _ le)

/-- An amount not rising across any step from `T` on, as far as can be refuted, is not refuted
to be within its value at any earlier step from `T` on. -/
theorem still_le {s : Nat → A} {T : Nat} (still : ∀ t, T ≤ t → ¬¬ M.le (s (t + 1)) (s t)) :
    ∀ k u, T ≤ u → ¬¬ M.le (s (u + k)) (s u)
  | 0, _, _ => fun no => no (M.le_refl _)
  | k + 1, u, from_ => fun no => still_le still k u from_ fun earlier =>
      still (u + k) (Nat.le_trans from_ (Nat.le_add_right u k)) fun step =>
        no (M.le_trans step earlier)

/-- The loss law. Where, across each of the `n` steps from `T`, the amount after the step
together with the step's loss `d` is within the amount before, the losses of those steps, added,
are within the amount at `T`, with what remains. No least loss and no unit are named. -/
theorem losses_within {s d : Nat → A} {T : Nat} :
    ∀ n, (∀ t, T ≤ t → t < T + n → M.le (M.add (s (t + 1)) (d t)) (s t)) →
      M.le (M.add (s (T + n)) (M.sum d T n)) (s T)
  | 0, _ => le_of_eq (add_zero (s T))
  | n + 1, falls => M.le_trans (le_of_eq (add_swap _ _ _))
      (M.le_trans
        (M.add_le_add_right _ (falls (T + n) (Nat.le_add_right T n) (Nat.lt_succ_self (T + n))))
        (losses_within n fun t from_ below => falls t from_ (Nat.lt_succ_of_lt below)))

/-- At each recurrence of `P`, the amount loses at least `ε` more: where it does not rise from `T`
on and falls by at least `ε` across each step at which `P` holds, each as far as can be refuted,
and `P` is not refuted to hold after every step from `T` on, then for every `m` it is not refuted
that at some step from `T` on the amount, with `m` copies of `ε`, is within its value at `T`. -/
theorem loses_times {s : Nat → A} {ε : A} {P : Nat → Prop} {T : Nat}
    (still : ∀ t, T ≤ t → ¬¬ M.le (s (t + 1)) (s t))
    (loses : ∀ t, T ≤ t → P t → ¬¬ M.le (M.add (s (t + 1)) ε) (s t))
    (recurs : ∀ N, T ≤ N → ¬¬ ∃ t, N ≤ t ∧ P t) :
    ∀ m, ¬¬ ∃ u, T ≤ u ∧ M.le (M.add (s u) (M.times m ε)) (s T)
  | 0 => fun no => no ⟨T, Nat.le_refl T, le_of_eq (add_zero (s T))⟩
  | m + 1 => fun no => loses_times still loses recurs m fun ⟨u, from_, within⟩ =>
      recurs u from_ fun ⟨t, later, holds⟩ => match Nat.le.dest later with
        | ⟨k, same⟩ =>
          have from_t : T ≤ t := Nat.le_trans from_ later
          still_le still k u from_ fun down =>
            loses t from_t holds fun step =>
              no ⟨t + 1, Nat.le_succ_of_le from_t,
                M.le_trans (le_of_eq (add_swap (s (t + 1)) (M.times m ε) ε))
                  (M.le_trans (M.add_le_add_right _ step)
                    (M.le_trans
                      (M.add_le_add_right _
                        (Eq.subst (motive := fun x => M.le (s x) (s u)) same down))
                      within))⟩

/-- **The least-loss law of rest.** Where an amount does not rise from `T` on, falls by at least
`ε` across each step at which `P` holds, each as far as can be refuted, and `m` copies of `ε` are
not within its value at `T`, it is not the case that after every step from `T` on a later step at
which `P` holds stays unrefuted. Two premises carry the conclusion: the least loss `ε` at each
step at which `P` holds, and the amount at `T` lying within fewer than `m` least losses. -/
theorem rests_unrefuted {s : Nat → A} {ε : A} {P : Nat → Prop} {T m : Nat}
    (still : ∀ t, T ≤ t → ¬¬ M.le (s (t + 1)) (s t))
    (loses : ∀ t, T ≤ t → P t → ¬¬ M.le (M.add (s (t + 1)) ε) (s t))
    (within : ¬ M.le (M.times m ε) (s T)) :
    ¬ ∀ N, T ≤ N → ¬¬ ∃ t, N ≤ t ∧ P t :=
  fun recurs => loses_times still loses recurs m fun ⟨u, _, le⟩ =>
    within (M.le_trans (le_add_left (M.times m ε) (s u)) le)

/-- So, with the premises holding outright, steps at which `P` holds do not recur. -/
theorem rests {s : Nat → A} {ε : A} {P : Nat → Prop} {T m : Nat}
    (still : ∀ t, T ≤ t → M.le (s (t + 1)) (s t))
    (loses : ∀ t, T ≤ t → P t → M.le (M.add (s (t + 1)) ε) (s t))
    (within : ¬ M.le (M.times m ε) (s T)) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ P t :=
  fun recurs => rests_unrefuted (fun t later no => no (still t later))
    (fun t later holds no => no (loses t later holds)) within fun N _ no => no (recurs N)

/-- In Archimedean amounts every amount lies within finitely many copies of a least loss above
nothing, so the least loss alone brings rest. -/
theorem rests_of_archimedean (archimedean : M.Archimedean) {s : Nat → A} {ε : A}
    {P : Nat → Prop} {T : Nat} (positive : ¬ M.le ε M.zero)
    (still : ∀ t, T ≤ t → M.le (s (t + 1)) (s t))
    (loses : ∀ t, T ≤ t → P t → M.le (M.add (s (t + 1)) ε) (s t)) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ P t :=
  match archimedean (s T) ε positive with
  | ⟨_, within⟩ => rests still loses within

/-- Balanced and dissipated on, a family's stock does not rise: the replenishment cancels. -/
theorem family_still {s u r : Nat → A} {T : Nat}
    (balances : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (u t)) (M.add (s t) (r t)))
    (dissipates : ∀ t, T ≤ t → M.le (r t) (u t)) :
    ∀ t, T ≤ t → M.le (s (t + 1)) (s t) :=
  fun t later => M.le_of_add_le_add_right (r t)
    (M.le_trans (add_le_add_left _ (dissipates t later)) (balances t later))

/-- Balanced, a family whose replenishment with `ε` is within its uptake at a step falls by at
least `ε` across it. -/
theorem family_loses {s u r : Nat → A} {ε : A} {P : Nat → Prop} {T : Nat}
    (balances : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (u t)) (M.add (s t) (r t)))
    (least : ∀ t, T ≤ t → P t → M.le (M.add (r t) ε) (u t)) :
    ∀ t, T ≤ t → P t → M.le (M.add (s (t + 1)) ε) (s t) :=
  fun t later holds => M.le_of_add_le_add_right (r t)
    (M.le_trans (le_of_eq (M.add_assoc _ _ _))
      (M.le_trans
        (add_le_add_left _ (M.le_trans (le_of_eq (M.add_comm ε (r t))) (least t later holds)))
        (balances t later)))

/-- **A family at rest, in any amounts.** Read a family's stock `s`, its uptake `u` and its
replenishment `r` across each step as amounts. Where from `T` on the stock after the step with the
uptake is within the stock before with the replenishment (balance), the replenishment is within
the uptake (dissipation), at each step at which `P` holds the replenishment with a least loss `ε`
is within the uptake, and the stock at `T` lies within fewer than `m` least losses, steps at which
`P` holds do not recur. -/
theorem family_rests {s u r : Nat → A} {ε : A} {P : Nat → Prop} {T m : Nat}
    (balances : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (u t)) (M.add (s t) (r t)))
    (dissipates : ∀ t, T ≤ t → M.le (r t) (u t))
    (least : ∀ t, T ≤ t → P t → M.le (M.add (r t) ε) (u t))
    (within : ¬ M.le (M.times m ε) (s T)) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ P t :=
  rests (family_still balances dissipates) (family_loses balances least) within

/-- In Archimedean amounts, a family balanced and dissipated on with a least loss above nothing
comes to rest. -/
theorem family_rests_of_archimedean (archimedean : M.Archimedean) {s u r : Nat → A} {ε : A}
    {P : Nat → Prop} {T : Nat} (positive : ¬ M.le ε M.zero)
    (balances : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (u t)) (M.add (s t) (r t)))
    (dissipates : ∀ t, T ≤ t → M.le (r t) (u t))
    (least : ∀ t, T ≤ t → P t → M.le (M.add (r t) ε) (u t)) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ P t :=
  rests_of_archimedean archimedean positive (family_still balances dissipates)
    (family_loses balances least)

/-! ### The approach to rest: no least loss -/

/-- An amount that does not rise across any step from `T` on is, at every later step, within its
value at every earlier step from `T` on. -/
theorem still_within {s : Nat → A} {T : Nat} (still : ∀ t, T ≤ t → M.le (s (t + 1)) (s t)) :
    ∀ k u, T ≤ u → M.le (s (u + k)) (s u)
  | 0, _, _ => M.le_refl _
  | k + 1, u, from_ => M.le_trans (still (u + k) (Nat.le_trans from_ (Nat.le_add_right u k)))
      (still_within still k u from_)

/-- An amount that, with each step's loss, is within its value before the step does not rise. -/
theorem still_of_falls {s d : Nat → A} {T : Nat}
    (falls : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (d t)) (s t)) :
    ∀ t, T ≤ t → M.le (s (t + 1)) (s t) :=
  fun t later => M.le_trans (le_add_right _ (d t)) (falls t later)

/-- Along `k` steps `f 0 < f 1 < ⋯` from `T` on, each losing at least `ε`, the amount after the
last of them, with `k` copies of `ε`, is within the amount at `T`. -/
theorem large_losses_from {s d : Nat → A} {ε : A} {T : Nat}
    (falls : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (d t)) (s t))
    {f : Nat → Nat} (start : T ≤ f 0) (rising : ∀ i, f i < f (i + 1)) :
    ∀ k, (∀ i, i < k → M.le ε (d (f i))) →
      ∃ u, T ≤ u ∧ u ≤ f k ∧ M.le (M.add (s u) (M.times k ε)) (s T)
  | 0, _ => ⟨T, Nat.le_refl T, start, le_of_eq (add_zero (s T))⟩
  | k + 1, large =>
    match large_losses_from falls start rising k
        (fun i below => large i (Nat.lt_succ_of_lt below)) with
    | ⟨u, from_, below, within⟩ =>
      match Nat.le.dest below with
      | ⟨j, same⟩ =>
        have from_f : T ≤ f k := Nat.le_trans from_ below
        have down : M.le (s (f k)) (s u) :=
          Eq.subst (motive := fun x => M.le (s x) (s u)) same
            (still_within (still_of_falls falls) j u from_)
        ⟨f k + 1, Nat.le_succ_of_le from_f, rising k,
          M.le_trans (le_of_eq (add_swap (s (f k + 1)) (M.times k ε) ε))
            (M.le_trans
              (M.add_le_add_right _
                (M.le_trans (add_le_add_left _ (large k (Nat.lt_succ_self k)))
                  (falls (f k) from_f)))
              (M.le_trans (M.add_le_add_right _ down) within))⟩

/-- **The approach to rest, counted.** Where across each step from `T` on the amount after the
step, with the step's loss, is within the amount before, then for any `k` steps
`f 0 < f 1 < ⋯` from `T` on, each losing at least `ε`, `k` copies of `ε` are within the amount
at `T`. No least loss is asked: `ε` is any amount, and the law bounds how many steps lose at
least `ε`. -/
theorem large_losses_within {s d : Nat → A} {ε : A} {T : Nat}
    (falls : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (d t)) (s t))
    {f : Nat → Nat} (start : T ≤ f 0) (rising : ∀ i, f i < f (i + 1)) (k : Nat)
    (large : ∀ i, i < k → M.le ε (d (f i))) :
    M.le (M.times k ε) (s T) :=
  match large_losses_from falls start rising k large with
  | ⟨u, _, _, within⟩ => M.le_trans (le_add_left (M.times k ε) (s u)) within

/-- So where `m` copies of `ε` are not within the amount at `T`, no `m` steps from `T` on each
lose at least `ε`: fewer than `m` do. -/
theorem few_large_losses {s d : Nat → A} {ε : A} {T m : Nat}
    (falls : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (d t)) (s t))
    (within : ¬ M.le (M.times m ε) (s T)) :
    ¬ ∃ f : Nat → Nat, T ≤ f 0 ∧ (∀ i, f i < f (i + 1)) ∧ ∀ i, i < m → M.le ε (d (f i)) :=
  fun ⟨_, start, rising, large⟩ => within (large_losses_within falls start rising m large)

/-- **The approach to rest.** In Archimedean amounts, an amount that, with each step's loss, is
within its value before the step comes arbitrarily near rest: for every `ε` above nothing there is
a count `m` such that no `m` steps from `T` on each lose at least `ε`. Only the Archimedean
property of the amounts is asked, no least loss. -/
theorem few_large_losses_of_archimedean (archimedean : M.Archimedean) {s d : Nat → A} {ε : A}
    {T : Nat} (falls : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (d t)) (s t))
    (positive : ¬ M.le ε M.zero) :
    ∃ m, ¬ ∃ f : Nat → Nat, T ≤ f 0 ∧ (∀ i, f i < f (i + 1)) ∧ ∀ i, i < m → M.le ε (d (f i)) :=
  match archimedean (s T) ε positive with
  | ⟨m, within⟩ => ⟨m, few_large_losses falls within⟩

/-- So, in Archimedean amounts, steps losing at least a given `ε` above nothing do not recur. -/
theorem approaches_rest (archimedean : M.Archimedean) {s d : Nat → A} {ε : A} {T : Nat}
    (falls : ∀ t, T ≤ t → M.le (M.add (s (t + 1)) (d t)) (s t))
    (positive : ¬ M.le ε M.zero) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ M.le ε (d t) :=
  rests_of_archimedean archimedean positive (still_of_falls falls)
    (fun t later large => M.le_trans (add_le_add_left _ large) (falls t later))

end Amounts

/-! ## Whole-number amounts: the spine's case -/

/-- Whole-number amounts, the spine's. -/
def Amounts.whole : Amounts Nat where
  zero := 0
  add := (· + ·)
  le := (· ≤ ·)
  le_refl := Nat.le_refl
  le_trans := Nat.le_trans
  add_assoc := Nat.add_assoc
  add_comm := Nat.add_comm
  zero_add := Nat.zero_add
  add_le_add_right := fun c le => Nat.add_le_add_right le c
  le_of_add_le_add_right := fun c le => _root_.Becoming.le_of_add_le_add_right c le
  zero_le := Nat.zero_le

namespace Amounts

theorem whole_times_one : ∀ n, Amounts.whole.times n 1 = n
  | 0 => rfl
  | n + 1 => congrArg (· + 1) (whole_times_one n)

/-- In whole numbers every stock lies within its own count of least losses of one, plus one. -/
theorem whole_within (a : Nat) : ¬ Amounts.whole.le (Amounts.whole.times (a + 1) 1) a :=
  fun le => Nat.not_succ_le_self a (Eq.subst (motive := fun x => x ≤ a) (whole_times_one (a + 1)) le)

/-- Whole-number amounts are Archimedean. -/
theorem whole_archimedean : Amounts.whole.Archimedean :=
  fun a e positive =>
    have one : 1 ≤ e := Nat.pos_of_ne_zero fun zero => positive (Nat.le_of_eq zero)
    ⟨a + 1, fun le => whole_within a (Nat.le_trans (times_le (M := Amounts.whole) one (a + 1)) le)⟩


/-- In whole numbers the approach to rest is rest: from `T` on, no more steps lose anything than
the amount at `T` counts. -/
theorem whole_losing_steps {s d : Nat → Nat} {T : Nat}
    (falls : ∀ t, T ≤ t → s (t + 1) + d t ≤ s t) {f : Nat → Nat} (start : T ≤ f 0)
    (rising : ∀ i, f i < f (i + 1)) (k : Nat) (losing : ∀ i, i < k → 1 ≤ d (f i)) : k ≤ s T :=
  Eq.subst (motive := fun x => x ≤ s T) (whole_times_one k)
    (large_losses_within (M := Amounts.whole) (ε := 1) falls start rising k losing)

end Amounts

/-- The spine's descent is the least-loss law at whole-number amounts: a strict fall of a whole
number is a fall by at least one, and every whole number lies within its own count of ones plus
one. `falls_not_recurring` restated. -/
theorem whole_falls_not_recurring (rank : Nat → Nat) (T : Nat)
    (noRise : ∀ n, T ≤ n → rank (n + 1) ≤ rank n) :
    ¬ ∀ N, ∃ n, N ≤ n ∧ rank (n + 1) < rank n :=
  Amounts.rests (M := Amounts.whole) (s := rank) (ε := 1) (P := fun n => rank (n + 1) < rank n)
    (m := rank T + 1) noRise (fun _ _ falls => falls) (Amounts.whole_within (rank T))

/-- `falls_stop_unrefuted` restated, the least-loss law at whole-number amounts with no
decidedness. -/
theorem whole_falls_stop_unrefuted {q : Nat → Nat} {T : Nat}
    (still : ∀ n, T ≤ n → q (n + 1) ≤ q n) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t, M ≤ t ∧ q (t + 1) < q t :=
  Amounts.rests_unrefuted (M := Amounts.whole) (s := q) (ε := 1) (P := fun t => q (t + 1) < q t)
    (m := q T + 1) (fun t later no => no (still t later)) (fun _ _ falls no => no falls)
    (Amounts.whole_within (q T))

/-- `Flow.taking_not_recurring_from` restated, the family law at whole-number amounts: each
formation taking from a family dissipated on loses at least one unit. -/
theorem Flow.taking_not_recurring_whole {F C : Type} {L : Flow F C} {W : Web F C} {cs : List C}
    {T : Nat} (balances : ∀ t, T ≤ t → L.BalancesOn W cs t)
    (dissipates : ∀ t, T ≤ t → L.DissipatesOn cs t) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  Amounts.family_rests_of_archimedean Amounts.whole_archimedean (s := W.stock cs)
    (u := L.uptake cs) (r := L.replenishment cs) (ε := 1) (P := fun t => 0 < L.takers cs t)
    (Nat.not_succ_le_zero 0)
    (fun t later => Nat.le_of_eq (balances t later).over)
    (fun t later => Nat.le_trans (Nat.le_add_right _ _) (dissipates t later).replenishment_takers)
    (fun t later takes =>
      Nat.le_trans (Nat.add_le_add_left takes _) (dissipates t later).replenishment_takers)

/-- Losses of whole-number amounts added over a stretch are the spine's total over its steps. -/
theorem Amounts.whole_sum (d : Nat → Nat) : ∀ n S, Amounts.whole.sum d S n = total (steps S n) d
  | 0, _ => rfl
  | n + 1, S =>
    (congrArg (· + d (S + n)) (Amounts.whole_sum d n S)).trans (total_steps_last d n S).symm
where
  total_steps_last (d : Nat → Nat) : ∀ n S, total (steps S (n + 1)) d = total (steps S n) d + d (S + n)
    | 0, S => (Nat.add_zero (d S)).trans (Nat.zero_add (d S)).symm
    | n + 1, S =>
      (congrArg (d S + ·) ((total_steps_last d n (S + 1)).trans
        (congrArg (fun k => total (steps (S + 1) n) d + d k) (Nat.succ_add S n)))).trans
        (Nat.add_assoc _ _ _).symm

/-- `Flow.takers_within_on` restated, the loss law at whole-number amounts: balanced and
dissipated on across each step of a stretch, the formations taking from a family over the
stretch number at most its stock at the start. -/
theorem Flow.takers_within_on_whole {F C : Type} {L : Flow F C} {W : Web F C} {cs : List C} :
    ∀ S N, (∀ t, S ≤ t → t < S + N → L.BalancesOn W cs t) →
      (∀ t, S ≤ t → t < S + N → L.DissipatesOn cs t) →
      W.stock cs (S + N) + total (steps S N) (L.takers cs) ≤ W.stock cs S :=
  fun S N balances dissipates =>
    Eq.subst (motive := fun x => W.stock cs (S + N) + x ≤ W.stock cs S)
      (Amounts.whole_sum (L.takers cs) N S)
      (Amounts.losses_within (M := Amounts.whole) (s := W.stock cs) (d := L.takers cs) N
        fun t from_ below => (balances t from_ below).runs_down (dissipates t from_ below))

/-- `Flow.change_stops_unrefuted` restated, the least-loss law at whole-number amounts with every
premise read as far as can be refuted: where what stands is listed and across every step from `T`
on it is not refuted that what stands runs down, it is not the case that after every step from `T`
on a later change of some standing stays unrefuted. Each change lowers the total standing by at
least one, and nothing is decided. -/
theorem Flow.change_stops_unrefuted_whole {F C : Type} {L : Flow F C} {W : Web F C}
    {stand : Nat → List C} (census : W.StandingCensus stand) {T : Nat}
    (runs : ∀ t, T ≤ t → ¬¬ L.RunsDown W t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t c, M ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  fun changing => Amounts.rests_unrefuted (M := Amounts.whole)
    (s := fun t => W.stock (stand t) t) (ε := 1) (P := fun t => ∃ c, W.Rises t c ∨ W.Falls t c)
    (m := W.stock (stand T) T + 1)
    (fun t later no => runs t later fun down => no (down.standing_le census))
    (fun t later changes no => runs t later fun down => no ((down.changes_iff census).mp changes))
    (Amounts.whole_within _)
    fun M from_ none_ => changing M from_ fun ⟨t, c, later, changes⟩ => none_ ⟨t, later, c, changes⟩

/-- `World.rests_unrefuted_enclosed` restated through the least-loss law at whole-number amounts:
in a world with a census whose relata are embodied, with a balanced, dissipative flow, in which
every step from some step on is enclosed, that it rests from some step on cannot be refuted. -/
theorem World.rests_unrefuted_enclosed_whole {w : World} (counted : w.Counted)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) : ¬ ¬ ∃ N, w.RestsFrom N :=
  match counted with
  | ⟨alive, census⟩ =>
    have standing := World.standingCensus census embodied
    have still := Flow.change_stops_unrefuted_whole standing fun t later unmet =>
      (enclosed t later).aroundStanding_not_not alive fun around =>
        unmet (around.runsDownClosed balanced dissipative standing).runsDown
    World.rests_unrefuted_iff.mpr
    ⟨fun arising => still fun M _ none_ => arising M fun ⟨t, x, later, arises⟩ =>
        none_ ⟨t, x, later, .inl (World.rises_of_arises embodied arises)⟩,
     fun ceasing => still fun M _ none_ => ceasing M fun ⟨t, x, later, ceases⟩ =>
        none_ ⟨t, x, later, .inr (World.falls_of_ceases embodied ceases)⟩⟩

/-! ## Dyadic amounts: dense, Archimedean, and without a least loss -/

/-- A dyadic amount, `num / 2 ^ exp`. -/
structure Dyadic where
  num : Nat
  exp : Nat

namespace Dyadic

theorem mul_assoc' (a b : Nat) : ∀ c, a * b * c = a * (b * c)
  | 0 => rfl
  | c + 1 => (congrArg (· + a * b) (mul_assoc' a b c)).trans (Nat.left_distrib a (b * c) b).symm

theorem right_distrib' (a b c : Nat) : (a + b) * c = a * c + b * c := by
  rw [Nat.mul_comm, Nat.left_distrib, Nat.mul_comm c a, Nat.mul_comm c b]

theorem mul_right_comm' (a b c : Nat) : a * b * c = a * c * b := by
  rw [mul_assoc', Nat.mul_comm b c, ← mul_assoc']

theorem mul_left_comm' (a b c : Nat) : a * (b * c) = b * (a * c) := by
  rw [← mul_assoc', Nat.mul_comm a b, mul_assoc']

theorem pow_add' (b x : Nat) : ∀ y, b ^ (x + y) = b ^ x * b ^ y
  | 0 => (Nat.mul_one _).symm
  | y + 1 => (congrArg (· * b) (pow_add' b x y)).trans (mul_assoc' _ _ _)

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
        = a.num * 2 ^ b.exp * 2 ^ c.exp := mul_right_comm' _ _ _
      _ ≤ b.num * 2 ^ a.exp * 2 ^ c.exp := Nat.mul_le_mul_right _ ab
      _ = b.num * 2 ^ c.exp * 2 ^ a.exp := mul_right_comm' _ _ _
      _ ≤ c.num * 2 ^ b.exp * 2 ^ a.exp := Nat.mul_le_mul_right _ bc
      _ = c.num * 2 ^ a.exp * 2 ^ b.exp := mul_right_comm' _ _ _)
    (Nat.two_pow_pos _)

theorem add_assoc' (a b c : Dyadic) : add (add a b) c = add a (add b c) :=
  ext' (by
    show (a.num * 2 ^ b.exp + b.num * 2 ^ a.exp) * 2 ^ c.exp + c.num * 2 ^ (a.exp + b.exp)
      = a.num * 2 ^ (b.exp + c.exp) + (b.num * 2 ^ c.exp + c.num * 2 ^ b.exp) * 2 ^ a.exp
    rw [right_distrib', right_distrib', pow_add' 2 a.exp b.exp, pow_add' 2 b.exp c.exp,
      mul_assoc' a.num, mul_right_comm' b.num (2 ^ a.exp) (2 ^ c.exp),
      mul_assoc' c.num (2 ^ b.exp) (2 ^ a.exp), Nat.mul_comm (2 ^ b.exp) (2 ^ a.exp),
      Nat.add_assoc])
    (Nat.add_assoc _ _ _)

theorem add_comm' (a b : Dyadic) : add a b = add b a :=
  ext' (Nat.add_comm _ _) (Nat.add_comm _ _)

theorem zero_add' (a : Dyadic) : add zero a = a :=
  ext' ((congrArg (· + a.num * 1) (Nat.zero_mul _)).trans ((Nat.zero_add _).trans (Nat.mul_one _)))
    (Nat.zero_add _)

theorem expand (x y e f g : Nat) :
    (x * 2 ^ g + y * 2 ^ e) * 2 ^ (f + g) = x * 2 ^ f * (2 ^ g * 2 ^ g) + y * (2 ^ e * 2 ^ f * 2 ^ g) := by
  rw [right_distrib', pow_add', mul_assoc' x, mul_left_comm' (2 ^ g) (2 ^ f), ← mul_assoc' x,
    mul_assoc' y, ← mul_assoc' (2 ^ e)]

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
        rw [← right_distrib', Nat.succ_mul, pow_add', mul_assoc']
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
  rw [Nat.one_mul, Nat.one_mul, ← Nat.mul_two, Dyadic.pow_add' 2 (t + 1) (t + 1),
    Dyadic.mul_assoc', Nat.mul_comm 2 (2 ^ t)]
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
nothing at any step: every loss is within nothing. -/
theorem Lossless.loses_nothing {next : S → S} (lossless : Lossless next) {all : List S}
    (every : ∀ s, s ∈ all) {q : S → A} {d : Nat → A} {s : S}
    (falls : ∀ n, M.le (M.add (q (orbit next s (n + 1))) (d n)) (q (orbit next s n)))
    (n : Nat) : M.le (d n) M.zero :=
  have still : ∀ n, M.le (q (orbit next s (n + 1))) (q (orbit next s n)) :=
    fun n => M.le_trans (Amounts.le_add_right _ (d n)) (falls n)
  have down : M.le (q (orbit next s n)) (q s) :=
    Eq.subst (motive := fun x => M.le (q (orbit next s x)) (q s)) (Nat.zero_add n)
      (Amounts.still_within (s := fun k => q (orbit next s k)) (fun t _ => still t) n 0
        (Nat.le_refl 0))
  have back : M.le (q (orbit next s n)) (q (orbit next s (n + 1))) :=
    M.le_trans down (lossless.regains every still (n + 1))
  M.le_of_add_le_add_right (q (orbit next s (n + 1)))
    (M.le_trans (Amounts.le_of_eq (M.add_comm (d n) _))
      (M.le_trans (falls n)
        (M.le_trans back (Amounts.le_of_eq (M.zero_add _).symm))))

/-- **A loss needs a merge.** Where a list holds every configuration and an amount, with each
step's loss, is within its value before the step along an orbit, a loss above nothing at some
step means the law merges configurations. The least loss on which the rest laws turn is a premise
of laws that merge: of descriptions that lump configurations, not of a law over finitely many
configurations that merges nothing, which returns rather than rests. -/
theorem loss_needs_merge {next : S → S} {all : List S} (every : ∀ s, s ∈ all) {q : S → A}
    {d : Nat → A} {s : S}
    (falls : ∀ n, M.le (M.add (q (orbit next s (n + 1))) (d n)) (q (orbit next s n)))
    {n : Nat} (positive : ¬ M.le (d n) M.zero) : ¬ Lossless next :=
  fun lossless => positive (lossless.loses_nothing every falls n)

end Law

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

end Becoming
