import PhasePeriodSelection

/-!
# Bounded policies are exactly the knowing-arrival search

This bridges the Boolean game to actual finite stop/advance/read policies.
Early stopping is allowed at every budget, and a branch with no candidates
succeeds vacuously. No outcome impossible for the present candidates has to be
realized. The statement is for every belief, including the empty one.

This is not yet first-read normalization or a correspondence between these
policies and the finite Nat-mask language certificate.
-/

namespace Generative.InquirySufficiency.PeriodStrategySemantics

open PhaseCycleDerivation (allOf bitAt)
open PhasePeriodSelection

/-- A policy consumes at most its indexed command budget. -/
inductive Policy : Nat → Type where
  | stop {budget : Nat} : Policy budget
  | advance {budget : Nat} : Policy budget → Policy (budget + 1)
  | read {budget : Nat} : Policy budget → Policy budget → Policy (budget + 1)

def moved (period : Nat) (candidate : Nat × Bool) : Nat × Bool :=
  ((candidate.1 + 1) % period, candidate.2)

/-- Whether this policy ends at the requested actual contact value. The same
policy is tested on every candidate; its read branches depend only on readings. -/
def wins (pattern : List Bool) (period : Nat) (value : Bool) :
    {budget : Nat} → Policy budget → (Nat × Bool) → Bool
  | _, .stop, candidate => bitAt pattern candidate.1 == value
  | _, .advance later, candidate => wins pattern period value later (moved period candidate)
  | _, .read low high, candidate =>
    if bitAt pattern candidate.1 != candidate.2 then wins pattern period value high candidate
    else wins pattern period value low candidate

def Succeeds (pattern : List Bool) (period : Nat) (value : Bool)
    {budget : Nat} (policy : Policy budget) (belief : List (Nat × Bool)) : Prop :=
  ∀ candidate, candidate ∈ belief → wins pattern period value policy candidate = true

theorem all_true_of_members {α : Type} (test : α → Bool) :
    ∀ items : List α, (∀ item, item ∈ items → test item = true) → allOf items test = true
  | [], _ => rfl
  | head :: rest, every => by
    change (test head && allOf rest test) = true
    rw [every head (.head _), all_true_of_members test rest
      (fun item member => every item (.tail _ member))]
    rfl

theorem member_filtered {α : Type} (test : α → Bool) {item : α} :
    ∀ {items : List α}, item ∈ items → test item = true → item ∈ items.filter test
  | [], member, _ => nomatch member
  | head :: rest, member, accepted => by
    cases member with
    | head =>
      rw [List.filter]
      rw [accepted]
      exact .head _
    | tail _ inside =>
      have later := member_filtered test inside accepted
      rw [List.filter]
      cases test head with
      | false => exact later
      | true => exact .tail _ later

theorem filtered_member {α : Type} (test : α → Bool) {item : α} :
    ∀ {items : List α}, item ∈ items.filter test → item ∈ items ∧ test item = true
  | [], member => nomatch member
  | head :: rest, member => by
    rw [List.filter] at member
    cases accepted : test head with
    | false =>
      rw [accepted] at member
      obtain ⟨inside, yes⟩ := filtered_member test member
      exact ⟨.tail _ inside, yes⟩
    | true =>
      rw [accepted] at member
      cases member with
      | head => exact ⟨.head _, accepted⟩
      | tail _ later =>
        obtain ⟨inside, yes⟩ := filtered_member test later
        exact ⟨.tail _ inside, yes⟩

theorem mapped_member {α β : Type} (f : α → β) {item : β} :
    ∀ {items : List α}, item ∈ items.map f → ∃ original, original ∈ items ∧ f original = item
  | [], member => nomatch member
  | head :: rest, member => by
    cases member with
    | head => exact ⟨head, .head _, rfl⟩
    | tail _ later =>
      obtain ⟨original, inside, same⟩ := mapped_member f later
      exact ⟨original, .tail _ inside, same⟩

theorem knows_has_policy (pattern : List Bool) (period : Nat) (value : Bool) :
    ∀ budget belief, knowsWithin pattern period value budget belief = true →
      ∃ policy : Policy budget, Succeeds pattern period value policy belief
  | 0, belief, known =>
    ⟨.stop, fun candidate member => allOf_member _ _ _ known member⟩
  | budget + 1, belief, known => by
    change (contactKnown pattern value belief ||
      knowsWithin pattern period value budget (advanceAll period belief) ||
      (knowsWithin pattern period value budget (belief.filter (readsAs pattern false)) &&
        knowsWithin pattern period value budget (belief.filter (readsAs pattern true)))) = true at known
    cases current : contactKnown pattern value belief with
    | true => exact ⟨.stop, fun candidate member => allOf_member _ _ _ current member⟩
    | false =>
      rw [current] at known
      cases advanced : knowsWithin pattern period value budget (advanceAll period belief) with
      | true =>
        obtain ⟨later, succeeds⟩ := knows_has_policy pattern period value budget _ advanced
        exact ⟨.advance later, fun candidate member =>
          succeeds (moved period candidate) (member_map (moved period) member)⟩
      | false =>
        rw [advanced] at known
        cases low : knowsWithin pattern period value budget (belief.filter (readsAs pattern false)) with
        | false => rw [low] at known; cases known
        | true =>
          cases high : knowsWithin pattern period value budget (belief.filter (readsAs pattern true)) with
          | false => rw [low, high] at known; cases known
          | true =>
            obtain ⟨lower, lowerWorks⟩ := knows_has_policy pattern period value budget _ low
            obtain ⟨higher, higherWorks⟩ := knows_has_policy pattern period value budget _ high
            refine ⟨.read lower higher, fun candidate member => ?_⟩
            unfold wins
            cases reading : (bitAt pattern candidate.1 != candidate.2) with
            | false =>
              have accepted : readsAs pattern false candidate = true := by
                unfold readsAs
                rw [reading]
                rfl
              exact lowerWorks candidate (member_filtered _ member accepted)
            | true =>
              have accepted : readsAs pattern true candidate = true := by
                unfold readsAs
                rw [reading]
                rfl
              exact higherWorks candidate (member_filtered _ member accepted)

theorem policy_implies_knows (pattern : List Bool) (period : Nat) (value : Bool)
    {budget : Nat} (policy : Policy budget) (belief : List (Nat × Bool))
    (succeeds : Succeeds pattern period value policy belief) :
    knowsWithin pattern period value budget belief = true := by
  induction policy generalizing belief with
  | @stop budget =>
    have current : contactKnown pattern value belief = true :=
      all_true_of_members _ _ succeeds
    cases budget with
    | zero => exact current
    | succ budget =>
      unfold knowsWithin
      rw [current]
      rfl
  | @advance budget later ih =>
    have laterWorks : Succeeds pattern period value later (advanceAll period belief) := by
      intro candidate member
      obtain ⟨original, inside, same⟩ := mapped_member (moved period) member
      rw [← same]
      exact succeeds original inside
    have advanced := ih _ laterWorks
    unfold knowsWithin
    rw [advanced]
    cases contactKnown pattern value belief <;> rfl
  | @read budget lower higher lowIH highIH =>
    have lowerWorks : Succeeds pattern period value lower (belief.filter (readsAs pattern false)) := by
      intro candidate member
      obtain ⟨inside, accepted⟩ := filtered_member _ member
      have actual := succeeds candidate inside
      unfold readsAs at accepted
      unfold wins at actual
      cases reading : (bitAt pattern candidate.1 != candidate.2) with
      | false => rw [reading] at actual; exact actual
      | true => rw [reading] at accepted; cases accepted
    have higherWorks : Succeeds pattern period value higher (belief.filter (readsAs pattern true)) := by
      intro candidate member
      obtain ⟨inside, accepted⟩ := filtered_member _ member
      have actual := succeeds candidate inside
      unfold readsAs at accepted
      unfold wins at actual
      cases reading : (bitAt pattern candidate.1 != candidate.2) with
      | false => rw [reading] at accepted; cases accepted
      | true => rw [reading] at actual; exact actual
    have low := lowIH _ lowerWorks
    have high := highIH _ higherWorks
    unfold knowsWithin
    rw [low, high]
    cases contactKnown pattern value belief <;>
      cases knowsWithin pattern period value budget (advanceAll period belief) <;> rfl

theorem knows_iff_policy (pattern : List Bool) (period : Nat) (value : Bool)
    (budget : Nat) (belief : List (Nat × Bool)) :
    knowsWithin pattern period value budget belief = true ↔
      ∃ policy : Policy budget, Succeeds pattern period value policy belief :=
  ⟨knows_has_policy pattern period value budget belief,
    fun ⟨policy, succeeds⟩ => policy_implies_knows pattern period value policy belief succeeds⟩

end Generative.InquirySufficiency.PeriodStrategySemantics

#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.Policy
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.moved
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.wins
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.Succeeds
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.all_true_of_members
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.member_filtered
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.filtered_member
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.mapped_member
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.knows_has_policy
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.policy_implies_knows
#print axioms Generative.InquirySufficiency.PeriodStrategySemantics.knows_iff_policy
