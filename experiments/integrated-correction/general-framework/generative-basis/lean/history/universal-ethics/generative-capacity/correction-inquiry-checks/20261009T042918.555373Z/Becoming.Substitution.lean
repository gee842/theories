import Becoming.Dependence

/-!
# Substitution: a consumer persists by transforming its dependence

`RelationalRenewal.Law` represents a condition renewed by a formation that depends on
it, while a focal formation draws on it. Drawing beyond renewal ends the renewal, and
the loss does not return within the law (`no_return_below_support`). A focal formation
that depends on the condition then ends itself (`dependent_overdraw_ends_itself`); one
that does not depend on it persists (`independent_overdraw_persists`).

Here the focal formation depends on the shared condition and can substitute another: it
depends on the shared condition while that supports it, and otherwise on an alternative
that does. The shared condition follows the same law, so its levels are unchanged. Read
through dependence that changes:
* the focal formation is active at every step;
* its dependence on the shared condition dissolves, and one on the alternative forms, at
  a step that can be found;
* it is consuming in the run, and the sustaining formation loses its support for ever
  and ends.

On the whole-run reading, substitution preserves the classification: a formation that
survives the loss it took part in, by transforming its dependence, still consumes, and
its own continuation does not certify renewal. This is nearly definitional, since
consuming asks only that the formation once drew on a consumed condition. On the
stepwise reading the substituting consumer is credited before the step at which the
shared condition falls below the sustaining formation's support, and withheld from that
step until it switches to the alternative: one step in `extracting`
(`stepwise_credits_substitution`), two in `slow`, where the shared condition still
supports the consumer for a step after it fails the sustaining formation
(`slow_withheld_two_steps`). With the existing results the law family now realizes
ending and transformation after a loss without return.

No ethical predicate, ranking or axiom occurs. Whether an actual formation can
substitute, and at what cost to the alternative, are application duties.
-/

namespace Becoming

open RelationalRenewal

/-- With a decidable determination, the step at which it ceases can be found. -/
theorem ceasing_step {p : Nat → Prop} [DecidablePred p] {T t : Nat} (le : T ≤ t)
    (holds : p T) (fails : ¬ p t) : ∃ s, T ≤ s ∧ s < t ∧ p s ∧ ¬ p (s + 1) := by
  induction le with
  | refl => exact absurd holds fails
  | @step m within earlier =>
    exact if now : p m then ⟨m, within, Nat.lt_succ_self m, now, fails⟩
      else match earlier now with
        | ⟨s, from_, before, yes, no⟩ => ⟨s, from_, Nat.lt_succ_of_lt before, yes, no⟩

namespace Substitution

/-- The condition the law renews, and an alternative that supports the focal formation. -/
inductive Source where
  | shared
  | alternative

/-- Which condition each formation depends on: the focal formation on the shared
condition while it supports it and on the alternative otherwise; the sustaining
formation on the shared condition. -/
def requires (L : Law) (t : Nat) : Law.Part → Source → Prop
  | .focal, .shared => L.needF ≤ L.level t
  | .focal, .alternative => L.level t < L.needF
  | .sustaining, .shared => True
  | .sustaining, .alternative => False

/-- The focal formation draws on the shared condition while it depends on it. -/
def draws (L : Law) (t : Nat) : Law.Part → Source → Prop
  | .focal, .shared => L.needF ≤ L.level t ∧ 0 < L.draw t
  | .focal, .alternative => False
  | .sustaining, .shared => False
  | .sustaining, .alternative => False

def level (L : Law) (t : Nat) : Source → Nat
  | .shared => L.level t
  | .alternative => L.needF

/-- The focal formation is active throughout; the sustaining formation while supported. -/
def active (L : Law) (t : Nat) : Law.Part → Prop
  | .focal => True
  | .sustaining => L.needG ≤ L.level t

/-- The law read with substitution, as a web whose dependence changes. -/
def web (L : Law) : Web Law.Part Source :=
  ⟨level L, active L, requires L, fun _ p _ => L.need p, draws L⟩

theorem web_dependent (L : Law) : (web L).Dependent
  | _, .focal, _, .shared, depends => depends
  | _, .focal, _, .alternative, _ => Nat.le_refl L.needF
  | _, .sustaining, active, .shared, _ => active
  | _, .sustaining, _, .alternative, depends => False.elim depends

/-- Drawing beyond renewal from the start, a focal formation that can substitute stays
active at every step, transforms its dependence at a step that can be found, and is
consuming; the sustaining formation ends. -/
theorem persists_consuming (L : Law) (gPositive : 0 < L.needG) (fPositive : 0 < L.needF)
    (fWithin : L.needF ≤ L.needG) (fStart : L.needF ≤ L.start)
    (over : ∀ t, L.renew + L.contrib t < L.draw t) :
    (web L).Dependent ∧ (∀ t, (web L).active t .focal) ∧
    (∃ s, (web L).Dissolves s .focal .shared ∧ (web L).Forms s .focal .alternative) ∧
    (web L).ConsumingIn .focal ∧
    ∃ T, ∀ t, T ≤ t → ¬ (web L).active t .sustaining := by
  have overFrom : ∀ t, 0 ≤ t → L.renew + L.contrib t < L.draw t := fun t _ => over t
  obtain ⟨T, _, _, low⟩ := L.overdraw_crosses_support gPositive fWithin overFrom
  have noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t := fun t _ =>
    Nat.le_of_lt (Nat.lt_of_le_of_lt (Nat.le_add_left _ _) (over t))
  have lost := L.permanently_below noRestore low (Nat.le_refl _)
  obtain ⟨E, ended, _⟩ := L.dependent_overdraw_ends_itself fPositive fWithin overFrom
  obtain ⟨s, _, _, held, gone⟩ :=
    ceasing_step (p := fun t => L.needF ≤ L.level t) (Nat.zero_le E) fStart
      (ended E (Nat.le_refl E))
  refine ⟨web_dependent L, fun _ => trivial,
    ⟨s, ⟨held, gone⟩, ⟨fun below => Nat.not_le_of_gt below held, Nat.gt_of_not_le gone⟩⟩,
    ⟨0, .shared, ⟨fStart, Nat.lt_of_le_of_lt (Nat.zero_le _) (over 0)⟩,
      .sustaining, T, trivial, fun t later => lost t (Nat.le_of_lt later)⟩,
    T, fun t later active => Nat.not_le_of_gt (lost t later) active⟩

/-- Extraction: a focal formation that depends on the shared condition at the sustaining
formation's level draws two units a step where one is renewed. -/
def extracting : Law := ⟨3, 1, 1, 1, fun _ => 2, fun _ => 0⟩

theorem extracting_persists_consuming :
    (web extracting).Dependent ∧ (∀ t, (web extracting).active t .focal) ∧
    (∃ s, (web extracting).Dissolves s .focal .shared ∧
      (web extracting).Forms s .focal .alternative) ∧
    (web extracting).ConsumingIn .focal ∧
    ∃ T, ∀ t, T ≤ t → ¬ (web extracting).active t .sustaining :=
  persists_consuming extracting Nat.zero_lt_one Nat.zero_lt_one (Nat.le_refl 1)
    (Nat.le_succ_of_le (Nat.le_succ 1)) (fun _ => Nat.lt_succ_self 1)

/-- Under extraction the shared condition is empty from step three on. -/
theorem extracting_low : ∀ n, Law.level extracting (n + 3) = 0
  | 0 => rfl
  | n + 1 => by
    show Law.level extracting (n + 3 + 1) = 0
    rw [Law.level_succ, extracting_low n]
    rfl

/-- The stepwise reading credits the consumer that substitutes: its event undermines only
at step 2, after which the shared condition falls below the sustaining formation's
support. -/
theorem stepwise_credits_substitution :
    (web extracting).ConsumingIn .focal ∧
    (∀ t, t ≠ 2 → (web extracting).active t .focal ∧
      ¬ (web extracting).UnderminingAt t .focal) ∧
    (web extracting).UnderminingAt 2 .focal :=
  ⟨extracting_persists_consuming.2.2.2.1, fun t other => ⟨trivial, fun ⟨c, drawn, g, _, _, fell⟩ =>
    match t, other, c, drawn, g, fell with
    | 0, _, .shared, _, .focal, fell => absurd fell (by decide)
    | 0, _, .shared, _, .sustaining, fell => absurd fell (by decide)
    | 1, _, .shared, _, .focal, fell => absurd fell (by decide)
    | 1, _, .shared, _, .sustaining, fell => absurd fell (by decide)
    | 2, other, _, _, _, _ => absurd rfl other
    | n + 3, _, .shared, drawn, _, _ =>
      Nat.not_succ_le_zero 0 (Nat.le_trans drawn.1 (Nat.le_of_eq (extracting_low n)))
    | _, _, .alternative, drawn, _, _ => drawn⟩,
   ⟨.shared, ⟨Nat.le_refl 1, Nat.zero_lt_two⟩, .sustaining, trivial,
     ⟨0, Nat.zero_le 2, fun _ _ _ => trivial, Nat.le_succ_of_le (Nat.le_succ 1), Nat.le_refl _⟩,
     Nat.zero_lt_one⟩⟩

/-- Start 5, renewal 1, sustaining need 3, focal need 1, two units drawn a step. -/
def slow : Law := ⟨5, 1, 3, 1, fun _ => 2, fun _ => 0⟩

/-- In `slow` the shared condition falls below the sustaining need at step 2 (3 to 2) but
still supports the consumer, which keeps drawing on it at step 3 (2 to 0): it is
withheld at steps 2 and 3. -/
theorem slow_withheld_two_steps :
    (web slow).ConsumingIn .focal ∧ (web slow).UnderminingAt 2 .focal ∧
    (web slow).UnderminingAt 3 .focal :=
  ⟨(persists_consuming slow (Nat.zero_lt_succ 2) Nat.zero_lt_one
      (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.le_succ_of_le (Nat.le_succ_of_le
        (Nat.le_succ_of_le (Nat.le_succ 1)))) (fun _ => Nat.lt_succ_self 1)).2.2.2.1,
   ⟨.shared, ⟨by decide, Nat.zero_lt_two⟩, .sustaining, trivial,
     ⟨0, Nat.zero_le 2, fun _ _ _ => trivial, by decide, by decide⟩, by decide⟩,
   ⟨.shared, ⟨by decide, Nat.zero_lt_two⟩, .sustaining, trivial,
     ⟨0, Nat.zero_le 3, fun _ _ _ => trivial, by decide, by decide⟩, by decide⟩⟩

end Substitution

end Becoming
