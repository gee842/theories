import Becoming.Branching
import ContinuationRenewal

/-!
# Renewal by descent along runs

`ContinuationRenewal` states, for any sequence of configurations, that where every step
without renewal descends a well-founded relation there is no tail without renewal, and that
renewal then recurs arbitrarily late where its occurrence is decided or a rank certifies the
descent; its alternating witness repeats two configurations with one restoring form. This
module reads renewal off the run of a process: renewal at step `n` is the run's step from `n`
belonging to a class of steps `renews`, and the descent is read on the run's configurations.
The alternating witness is the run of the negation law from `true` (`alternation_state`).

* **No run without renewal from some step on.** Where every step of a run outside the class
  descends a well-founded relation, no tail of the run is free of steps of the class
  (`no_renewal_free_tail`); where membership in the class is decided, steps of the class recur
  arbitrarily late (`renewal_arbitrarily_late`); where a rank of configurations falls at every
  other step, a step of the class comes within the rank of the configuration
  (`renewal_within_rank`).
* **The alternation.** The run of the negation law from `true` takes a consuming or a restoring
  step at every step (`actual_steps`), has period two (`period_two`), comes to `false` arbitrarily
  late (`restores_arbitrarily_late`), and every restoration raises the rank from 0 to 1
  (`restoration_raises_rank`); its first step is an actual step without restoration that lowers
  the rank (`unrenewed_first_step`). It passes through no configuration but its first two
  (`no_new_configurations`), so every score of configurations is bounded along it
  (`every_score_bounded`): recurring renewal does not give unbounded novelty.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v

namespace DescentRenewalRuns

section AnyProcess

variable {S : Type u} {A : Type v} {P : Process S A}

/-- **No run has a tail without renewal, where every step without renewal descends a
well-founded relation.** Renewal is the run's step belonging to the class `renews`. -/
theorem no_renewal_free_tail (r : Run P) {renews : S → A → S → Prop}
    {unrenewed : S → S → Prop} (wellFounded : WellFounded unrenewed)
    (decreases : ∀ n, ¬ renews (r.state n) (r.act n) (r.state (n + 1)) →
      unrenewed (r.state (n + 1)) (r.state n)) (start : Nat) :
    ¬ ∀ n, start ≤ n → ¬ renews (r.state n) (r.act n) (r.state (n + 1)) :=
  ContinuationRenewal.no_renewal_free_tail wellFounded r.state
    (fun n => renews (r.state n) (r.act n) (r.state (n + 1))) decreases start

/-- **Renewal recurs arbitrarily late along a run** where membership of a step in the class is
decided and every step outside it descends a well-founded relation. -/
theorem renewal_arbitrarily_late (r : Run P) {renews : S → A → S → Prop}
    (decision : ∀ s a t, Decidable (renews s a t)) {unrenewed : S → S → Prop}
    (wellFounded : WellFounded unrenewed)
    (decreases : ∀ n, ¬ renews (r.state n) (r.act n) (r.state (n + 1)) →
      unrenewed (r.state (n + 1)) (r.state n)) :
    ∀ start, ∃ n, start ≤ n ∧ renews (r.state n) (r.act n) (r.state (n + 1)) :=
  @ContinuationRenewal.renewal_arbitrarily_late_of_decidable S unrenewed wellFounded r.state
    (fun n => renews (r.state n) (r.act n) (r.state (n + 1)))
    (fun n => decision (r.state n) (r.act n) (r.state (n + 1))) decreases

/-- **Renewal comes within the rank of the configuration**: where membership in the class is
decided and a rank of configurations falls at every step outside it, a step of the class comes
from `start` within `rank (r.state start)` further steps. -/
theorem renewal_within_rank (r : Run P) {renews : S → A → S → Prop}
    (decision : ∀ s a t, Decidable (renews s a t)) (rank : S → Nat)
    (decreases : ∀ n, ¬ renews (r.state n) (r.act n) (r.state (n + 1)) →
      rank (r.state (n + 1)) < rank (r.state n)) (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + rank (r.state start) ∧
      renews (r.state n) (r.act n) (r.state (n + 1)) :=
  @ContinuationRenewal.renewal_within_rank_plus_one_steps (fun n => rank (r.state n))
    (fun n => renews (r.state n) (r.act n) (r.state (n + 1)))
    (fun n => decision (r.state n) (r.act n) (r.state (n + 1))) decreases start

end AnyProcess

/-! ## The alternation as a run -/

/-- The run of the negation law from `true`. -/
def alternation : Run (Law.process Bool.not) :=
  Law.run Bool.not true

/-- The rank of a configuration of the alternation: one available step at `true`. -/
def rank (b : Bool) : Nat := if b then 1 else 0

/-- The alternating sequence of `ContinuationRenewal` is the run of the negation law from
`true`. -/
theorem alternation_state : ∀ n, alternation.state n = ContinuationRenewal.alternatingState n
  | 0 => rfl
  | n + 1 => congrArg Bool.not (alternation_state n)

/-- The rank of `ContinuationRenewal` is the rank of the run's configuration. -/
theorem alternatingRank_eq (n : Nat) :
    ContinuationRenewal.alternatingRank n = rank (alternation.state n) :=
  congrArg rank (alternation_state n).symm

/-- **Every step of the alternation is a consuming or a restoring step.** -/
theorem actual_steps (n : Nat) :
    ContinuationRenewal.alternatingStep (alternation.state n) (alternation.state (n + 1)) :=
  Eq.mpr (congr (congrArg ContinuationRenewal.alternatingStep (alternation_state n))
    (alternation_state (n + 1))) (ContinuationRenewal.alternating_actual_steps n)

/-- **The alternation has period two.** -/
theorem period_two (n : Nat) : alternation.state (n + 2) = alternation.state n :=
  (alternation_state (n + 2)).trans
    ((ContinuationRenewal.alternating_period_two n).trans (alternation_state n).symm)

/-- **The alternation restores arbitrarily late**: it comes to `false` after every step. -/
theorem restores_arbitrarily_late : ∀ start, ∃ n, start ≤ n ∧ alternation.state n = false :=
  fun start => match ContinuationRenewal.alternating_renews_arbitrarily_late start with
    | ⟨n, after, renewed⟩ => ⟨n, after, (alternation_state n).trans renewed⟩

/-- **Every restoration of the alternation raises the rank from 0 to 1.** -/
theorem restoration_raises_rank (n : Nat) (restoring : alternation.state n = false) :
    rank (alternation.state n) = 0 ∧ rank (alternation.state (n + 1)) = 1 :=
  match ContinuationRenewal.alternating_restoration_raises_rank n
      ((alternation_state n).symm.trans restoring) with
  | ⟨before, after⟩ => ⟨(alternatingRank_eq n).symm.trans before,
      (alternatingRank_eq (n + 1)).symm.trans after⟩

/-- **The first step of the alternation is an actual step without restoration, and it lowers
the rank.** -/
theorem unrenewed_first_step :
    alternation.state 0 ≠ false ∧ rank (alternation.state 1) < rank (alternation.state 0) :=
  match ContinuationRenewal.alternating_has_actual_unrenewed_step with
  | ⟨notRenewed, lowers⟩ => ⟨fun restoring => notRenewed ((alternation_state 0).symm.trans restoring),
      Eq.mp (congr (congrArg LT.lt (alternatingRank_eq 1)) (alternatingRank_eq 0)) lowers⟩

/-- **The alternation passes through no configuration but its first two.** -/
theorem no_new_configurations (n : Nat) :
    alternation.state n = alternation.state 0 ∨ alternation.state n = alternation.state 1 :=
  match ContinuationRenewal.alternating_no_new_configurations n with
  | .inl first => .inl ((alternation_state n).trans (first.trans (alternation_state 0).symm))
  | .inr second => .inr ((alternation_state n).trans (second.trans (alternation_state 1).symm))

/-- **Every score of configurations is bounded along the alternation.** -/
theorem every_score_bounded (score : Bool → Nat) :
    ∃ bound, ∀ n, score (alternation.state n) ≤ bound :=
  match ContinuationRenewal.alternating_every_configuration_score_bounded score with
  | ⟨bound, below⟩ => ⟨bound, fun n =>
      Nat.le_trans (Nat.le_of_eq (congrArg score (alternation_state n))) (below n)⟩

end DescentRenewalRuns

end Becoming
