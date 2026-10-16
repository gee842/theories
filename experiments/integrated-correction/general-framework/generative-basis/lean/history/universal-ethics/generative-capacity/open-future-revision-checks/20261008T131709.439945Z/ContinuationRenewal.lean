/-!
# Continuation and recurrent renewal: a conditional necessity interface

The states are selected configurations of one continuing process. The relation
`unrenewed` compares successive configurations during activity without renewal;
it does not split an agent from an independent environment. Well-foundedness is
an explicit certificate that such activity cannot continue indefinitely. Its
realization is not proved here. A Nat-valued rank is one possible certificate,
not a universal stock, cost, or ethical measure.

`renewal n` concerns the transition from time n to time n+1. The constructive
positive existence results supply a renewal-or-descent disjunction, or require
decidability of the renewal event. The negative result needs no such decision.

The alternating witness has a real unrenewed step and a restoring step. It
repeats two configurations indefinitely, always using the same restoring form.
It refutes inference of unbounded represented configuration novelty or complexity
measured by a fixed Nat-valued configuration score from renewal recurrence alone,
without purporting to model an organism or humanity.
There is no moral predicate and no claim of universal normative warrant.
-/

namespace ContinuationRenewal

universe u

/-- An accessible configuration admits no infinite unrenewed tail. -/
theorem no_unrenewed_tail_of_accessible {State : Type u}
    {unrenewed : State → State → Prop} {states : Nat → State}
    {a : State} (accessible : Acc unrenewed a) :
    ∀ start, states start = a →
      ¬ (∀ n, start ≤ n → unrenewed (states (n + 1)) (states n)) := by
  induction accessible with
  | intro a _ inductionHypothesis =>
      intro start atStart tail
      have next : unrenewed (states (start + 1)) a :=
        atStart ▸ tail start (Nat.le_refl start)
      apply inductionHypothesis _ next (start + 1) rfl
      intro n afterNext
      exact tail n (Nat.le_trans (Nat.le_succ start) afterNext)

/-- This negative necessity statement does not decide renewal events. -/
theorem no_renewal_free_tail {State : Type u}
    {unrenewed : State → State → Prop} (wellFounded : WellFounded unrenewed)
    (states : Nat → State) (renewal : Nat → Prop)
    (decreases : ∀ n, ¬ renewal n → unrenewed (states (n + 1)) (states n))
    (start : Nat) : ¬ (∀ n, start ≤ n → ¬ renewal n) := by
  intro absent
  apply no_unrenewed_tail_of_accessible (wellFounded.apply (states start)) start rfl
  intro n afterStart
  exact decreases n (absent n afterStart)

/-- The constructive positive result uses the actual renewal-or-descent split. -/
theorem renewal_after_of_accessible {State : Type u}
    {unrenewed : State → State → Prop} {states : Nat → State}
    {renewal : Nat → Prop}
    (step : ∀ n, renewal n ∨ unrenewed (states (n + 1)) (states n))
    {a : State} (accessible : Acc unrenewed a) :
    ∀ start, states start = a → ∃ n, start ≤ n ∧ renewal n := by
  induction accessible with
  | intro a _ inductionHypothesis =>
      intro start atStart
      cases step start with
      | inl renewed => exact ⟨start, Nat.le_refl start, renewed⟩
      | inr descending =>
          have next : unrenewed (states (start + 1)) a := atStart ▸ descending
          obtain ⟨n, afterNext, renewed⟩ :=
            inductionHypothesis _ next (start + 1) rfl
          exact ⟨n, Nat.le_trans (Nat.le_succ start) afterNext, renewed⟩

theorem renewal_arbitrarily_late {State : Type u}
    {unrenewed : State → State → Prop} (wellFounded : WellFounded unrenewed)
    (states : Nat → State) (renewal : Nat → Prop)
    (step : ∀ n, renewal n ∨ unrenewed (states (n + 1)) (states n)) :
    ∀ start, ∃ n, start ≤ n ∧ renewal n := by
  intro start
  exact renewal_after_of_accessible step
    (wellFounded.apply (states start)) start rfl

theorem renewal_arbitrarily_late_of_decidable {State : Type u}
    {unrenewed : State → State → Prop} (wellFounded : WellFounded unrenewed)
    (states : Nat → State) (renewal : Nat → Prop) [DecidablePred renewal]
    (decreases : ∀ n, ¬ renewal n → unrenewed (states (n + 1)) (states n)) :
    ∀ start, ∃ n, start ≤ n ∧ renewal n := by
  apply renewal_arbitrarily_late wellFounded states renewal
  intro n
  by_cases renewed : renewal n
  · exact Or.inl renewed
  · exact Or.inr (decreases n renewed)

/-- The interval includes `start` and `start + bound`: `bound + 1` steps. -/
theorem renewal_within_rank_bound
    (rank : Nat → Nat) (renewal : Nat → Prop) [DecidablePred renewal]
    (decreases : ∀ n, ¬ renewal n → rank (n + 1) < rank n)
    (bound : Nat) :
    ∀ start, rank start ≤ bound →
      ∃ n, start ≤ n ∧ n ≤ start + bound ∧ renewal n := by
  induction bound with
  | zero =>
      intro start rankBound
      by_cases renewed : renewal start
      · exact ⟨start, Nat.le_refl start, Nat.le_refl start, renewed⟩
      · exact False.elim (Nat.not_lt_zero _
          (Nat.lt_of_lt_of_le (decreases start renewed) rankBound))
  | succ bound inductionHypothesis =>
      intro start rankBound
      by_cases renewed : renewal start
      · exact ⟨start, Nat.le_refl start, Nat.le_add_right start (bound + 1), renewed⟩
      · have nextBound : rank (start + 1) ≤ bound :=
          Nat.le_of_lt_succ (Nat.lt_of_lt_of_le (decreases start renewed) rankBound)
        obtain ⟨n, afterNext, within, event⟩ :=
          inductionHypothesis (start + 1) nextBound
        refine ⟨n, Nat.le_trans (Nat.le_succ start) afterNext, ?_, event⟩
        exact (Nat.add_right_comm start 1 bound) ▸ within

theorem renewal_within_rank_plus_one_steps
    (rank : Nat → Nat) (renewal : Nat → Prop) [DecidablePred renewal]
    (decreases : ∀ n, ¬ renewal n → rank (n + 1) < rank n) (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + rank start ∧ renewal n :=
  renewal_within_rank_bound rank renewal decreases (rank start) start (Nat.le_refl _)

theorem rank_renewal_arbitrarily_late
    (rank : Nat → Nat) (renewal : Nat → Prop) [DecidablePred renewal]
    (decreases : ∀ n, ¬ renewal n → rank (n + 1) < rank n) :
    ∀ start, ∃ n, start ≤ n ∧ renewal n := by
  intro start
  obtain ⟨n, afterStart, _, renewed⟩ :=
    renewal_within_rank_plus_one_steps rank renewal decreases start
  exact ⟨n, afterStart, renewed⟩

/-- `true` has one available activity step; `false` requires restoration. -/
def alternatingState : Nat → Bool
  | 0 => true
  | n + 1 => !(alternatingState n)

def alternatingRank (n : Nat) : Nat := if alternatingState n then 1 else 0

def alternatingRenewal (n : Nat) : Prop := alternatingState n = false

instance alternatingRenewalDecidable : DecidablePred alternatingRenewal := fun n =>
  inferInstanceAs (Decidable (alternatingState n = false))

/-- Both edges are part of one fixed process: consumption and restoration. -/
def alternatingStep (before after : Bool) : Prop :=
  (before = true ∧ after = false) ∨ (before = false ∧ after = true)

theorem alternating_actual_steps (n : Nat) :
    alternatingStep (alternatingState n) (alternatingState (n + 1)) := by
  change alternatingStep (alternatingState n) (!(alternatingState n))
  cases alternatingState n
  · exact Or.inr ⟨rfl, rfl⟩
  · exact Or.inl ⟨rfl, rfl⟩

theorem alternating_nonrenewal_decreases (n : Nat)
    (absent : ¬ alternatingRenewal n) : alternatingRank (n + 1) < alternatingRank n := by
  unfold alternatingRenewal at absent
  unfold alternatingRank
  change (if !(alternatingState n) then 1 else 0) <
    (if alternatingState n then 1 else 0)
  cases state : alternatingState n
  · exact False.elim (absent state)
  · exact Nat.zero_lt_succ 0

theorem alternating_renews_arbitrarily_late :
    ∀ start, ∃ n, start ≤ n ∧ alternatingRenewal n :=
  rank_renewal_arbitrarily_late alternatingRank alternatingRenewal
    alternating_nonrenewal_decreases

theorem alternating_period_two (n : Nat) :
    alternatingState (n + 2) = alternatingState n := by
  change Bool.not (Bool.not (alternatingState n)) = alternatingState n
  cases alternatingState n <;> rfl

/-- Every restoration has exactly the same before/after form. -/
theorem alternating_one_restoring_form (n : Nat) (renewed : alternatingRenewal n) :
    alternatingState n = false ∧ alternatingState (n + 1) = true := by
  refine ⟨renewed, ?_⟩
  change Bool.not (alternatingState n) = true
  exact congrArg Bool.not renewed

theorem alternating_restoration_raises_rank (n : Nat) (renewed : alternatingRenewal n) :
    alternatingRank n = 0 ∧ alternatingRank (n + 1) = 1 := by
  obtain ⟨before, after⟩ := alternating_one_restoring_form n renewed
  constructor
  · exact congrArg (fun b : Bool => if b then 1 else 0) before
  · exact congrArg (fun b : Bool => if b then 1 else 0) after

/-- The descent condition is used on an actual edge, not made vacuous by
    declaring every transition a renewal event. -/
theorem alternating_has_actual_unrenewed_step :
    ¬ alternatingRenewal 0 ∧ alternatingRank 1 < alternatingRank 0 := by
  constructor
  · intro impossible
    cases impossible
  · exact Nat.zero_lt_succ 0

/-- All represented configurations recur among the initial two. -/
theorem alternating_no_new_configurations (n : Nat) :
    alternatingState n = alternatingState 0 ∨
      alternatingState n = alternatingState 1 := by
  cases state : alternatingState n
  · exact Or.inr rfl
  · exact Or.inl rfl

/-- For *any* configuration-based Nat score, there is a fixed global bound.
    This score is arbitrary; the theorem introduces no metric of life's worth. -/
theorem alternating_every_configuration_score_bounded (score : Bool → Nat) :
    ∃ bound, ∀ n, score (alternatingState n) ≤ bound := by
  refine ⟨score false + score true, ?_⟩
  intro n
  cases alternatingState n
  · exact Nat.le_add_right _ _
  · exact Nat.le_add_left _ _

end ContinuationRenewal
