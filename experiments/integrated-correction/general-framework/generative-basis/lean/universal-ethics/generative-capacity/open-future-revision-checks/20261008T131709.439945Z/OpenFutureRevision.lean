import ContinuationRenewal
import PositiveGroundUncertainty

/-!
Composition, not a new proof of renewal or G0: a remaining-step certificate
is handed between revised response rules along ONE actual history. Its rank
measures the stated realization bound, not ethical value or complexity.
The realized generative form may vary. Actual step occurrence, correspondence,
permissible means and continuing historical requirements remain supplied.
-/
namespace OpenFutureRevision
open GenerativeComparison

theorem handed_off_progress {S : Type}
    (states : Nat → S) (rank : Nat → S → Nat) (completed : Nat → Prop)
    (localStep : ∀ n, ¬ completed n →
      rank n (states (n+1)) < rank n (states n))
    (handoff : ∀ n, ¬ completed n →
      rank (n+1) (states (n+1)) ≤ rank n (states (n+1))) :
    ∀ n, ¬ completed n →
      rank (n+1) (states (n+1)) < rank n (states n) := by
  intro n hn
  exact Nat.lt_of_le_of_lt (handoff n hn) (localStep n hn)

/-- The inventory refers to actually formed occurrences within this bound.
An occurrence's meaning, non-duplication and living interpretation are inputs. -/
def boundedInventory {H Q : Type} (appears : H → Nat → Q → Prop)
    (generative : Q → Prop) (bound : Nat) : Inventory H Q where
  realized h q := ∃ n, n ≤ bound ∧ appears h n q
  generative := generative

theorem generation_by_bound {H S Q : Type}
    (admitted : H → Prop) (states : H → Nat → S)
    (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h, DecidablePred (completed h))
    (appears : H → Nat → Q → Prop) (generative : Q → Prop)
    (before : H → Q → Prop) (bound : Nat)
    (initial : ∀ h, admitted h → rank h 0 (states h 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n (states h (n+1)) < rank h n (states h n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n+1) (states h (n+1)) ≤ rank h n (states h (n+1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, generative q ∧ appears h n q ∧ ¬ before h q) :
    ∀ h, admitted h → ∃ q, (boundedInventory appears generative bound).generative q ∧
      (boundedInventory appears generative bound).realized h q ∧ ¬ before h q := by
  intro h allowed
  letI : DecidablePred (completed h) := decideEvent h
  have decrease := handed_off_progress (states h) (rank h) (completed h)
    (localStep h allowed) (handoff h allowed)
  obtain ⟨n, _, within, finished⟩ := ContinuationRenewal.renewal_within_rank_bound
    (fun n => rank h n (states h n)) (completed h) decrease bound 0 (initial h allowed)
  obtain ⟨q, gen, actual, fresh⟩ := correspondence h allowed n finished
  exact ⟨q, gen, ⟨n, within, actual⟩, fresh⟩

/-- Producer output is the exact formation premise of the inherited positive
ground theorem. This does not establish all-things permission or a duty. -/
theorem positive_ground_by_bound {H Q : Type}
    (admitted : H → Prop) (appears : H → Nat → Q → Prop)
    (generative : Q → Prop) (before : H → Q → Prop) (bound : Nat)
    (positive : H → Q → Prop)
    (g0 : G0 (boundedInventory appears generative bound) positive)
    (formed : ∀ h, admitted h → ∃ q,
      (boundedInventory appears generative bound).generative q ∧
      (boundedInventory appears generative bound).realized h q ∧ ¬ before h q) :
    ∀ h, admitted h → ∃ q, positive h q ∧ ¬ before h q :=
  PositiveGroundUncertainty.contingent_generation_has_positive_ground
    admitted before (boundedInventory appears generative bound) positive g0 formed

/- The local arrangement has two unfinished configurations and two formed
outcomes. These are stages of shared activity, not independent value owners. -/
inductive Stage where
  | leftReady | rightReady | formedLeft | formedRight
  deriving DecidableEq
inductive Rule where
  | left | right | directRight
  deriving DecidableEq

def completed (s : Stage) : Prop := s = .formedLeft ∨ s = .formedRight
def advance (p : Rule) (s : Stage) : Stage :=
  match s with
  | .formedLeft | .formedRight => s
  | .leftReady => if p = .left then .rightReady else .formedRight
  | .rightReady => if p = .right then .leftReady
      else if p = .left then .formedLeft else .formedRight

def remaining (p : Rule) (s : Stage) : Nat :=
  match s with
  | .formedLeft | .formedRight => 0
  | .leftReady => if p = .left then 2 else 1
  | .rightReady => if p = .right then 2 else 1

theorem each_fixed_rule_finishes (p : Rule) (s : Stage) :
    completed (advance p (advance p s)) := by
  cases p <;> cases s <;> decide

theorem each_rule_local_progress (p : Rule) (s : Stage)
    (unfinished : ¬ completed (advance p s)) :
    remaining p (advance p s) < remaining p s := by
  cases p <;> cases s <;> simp_all [completed, advance, remaining]

def restartChoice : Stage → Rule
  | .leftReady => .left
  | .rightReady => .right
  | .formedLeft | .formedRight => .directRight

def revisingRun : Nat → Stage
  | 0 => .leftReady
  | n+1 => advance (restartChoice (revisingRun n)) (revisingRun n)

theorem revising_run_stays_unfinished (n : Nat) :
    revisingRun n = .leftReady ∨ revisingRun n = .rightReady := by
  induction n with
  | zero => exact Or.inl rfl
  | succ n ih =>
    rcases ih with h | h
    · exact Or.inr (by simp [revisingRun, h, restartChoice, advance])
    · exact Or.inl (by simp [revisingRun, h, restartChoice, advance])

/-- Every executed step belongs to a rule that finishes when retained, and
strictly improves that rule's own remaining-step certificate. Yet no outcome
ever forms. This strengthens the previously known idle-opportunity control. -/
theorem revised_rules_can_fail_forever :
    (∀ n, completed (advance (restartChoice (revisingRun n))
      (advance (restartChoice (revisingRun n)) (revisingRun n)))) ∧
    (∀ n, remaining (restartChoice (revisingRun n)) (revisingRun (n+1)) <
      remaining (restartChoice (revisingRun n)) (revisingRun n)) ∧
    (∀ n, ¬ completed (revisingRun n)) := by
  have unfinished : ∀ n, ¬ completed (revisingRun n) := by
    intro n
    rcases revising_run_stays_unfinished n with h | h <;> simp [h, completed]
  refine ⟨fun _ => each_fixed_rule_finishes _ _, ?_, unfinished⟩
  intro n
  exact each_rule_local_progress _ _ (unfinished (n+1))

theorem revision_resets_remaining (n : Nat) :
    remaining (restartChoice (revisingRun n)) (revisingRun (n+1)) = 1 ∧
    remaining (restartChoice (revisingRun (n+1))) (revisingRun (n+1)) = 2 := by
  rcases revising_run_stays_unfinished n with h | h <;>
    simp [revisingRun, h, restartChoice, advance, remaining]

/-- A real revision changes the ensuing formed outcome and still meets the
handoff bound: after the first left-rule step, directRight completes instead.
This is not permission to replace a specifically owed left outcome. -/
theorem changed_form_with_valid_handoff :
    advance .left .leftReady = .rightReady ∧
    remaining .directRight .rightReady ≤ remaining .left .rightReady ∧
    advance .directRight .rightReady = .formedRight ∧
    advance .left .rightReady = .formedLeft := by decide

def realizes (s : Stage) (q : Bool) : Prop :=
  if q then s = .formedRight else s = .formedLeft

theorem realized_form_need_not_be_fixed :
    (∀ p : Bool, ∃ q, realizes
      (advance (if p then .directRight else .left) .rightReady) q) ∧
    ¬ ∃ q, ∀ p : Bool, realizes
      (advance (if p then .directRight else .left) .rightReady) q := by
  constructor
  · intro p
    exact ⟨p, by cases p <;> rfl⟩
  · rintro ⟨q, h⟩
    cases q
    · have impossible := h true; cases impossible
    · have impossible := h false; cases impossible

end OpenFutureRevision
