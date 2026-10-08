import Std

/-
Finite joint risk in a changing support arrangement. Natural counts represent
weights on one supplied finite outcome space, NOT measured frequencies that
automatically certify future probabilities. No independence is assumed.
The routes are differentiated responses within one arrangement. The primitive
local inputs are its modes, event weights, failure law and continuation target.
-/
namespace JointRiskRevision

structure Table where
  neither : Nat
  leftOnly : Nat
  rightOnly : Nat
  both : Nat
  deriving DecidableEq, Repr

def mass (t : Table) : Nat := t.neither + t.leftOnly + t.rightOnly + t.both
def leftRisk (t : Table) : Nat := t.leftOnly + t.both
def rightRisk (t : Table) : Nat := t.rightOnly + t.both
def anyLoss (t : Table) : Nat := t.leftOnly + t.rightOnly + t.both

def Compatible (n l r b : Nat) : Prop :=
  ∃ t : Table, mass t = n ∧ leftRisk t = l ∧ rightRisk t = r ∧ t.both = b

theorem joint_bounds (t : Table) :
    t.both ≤ leftRisk t ∧ t.both ≤ rightRisk t ∧
    leftRisk t + rightRisk t ≤ mass t + t.both := by
  simp only [leftRisk, rightRisk, mass]
  omega

/- Every integer in the stated interval is actually attainable. This is not
   merely a conservative upper bound; it gives exact finite identification. -/
theorem compatible_iff (n l r b : Nat) :
    Compatible n l r b ↔ b ≤ l ∧ b ≤ r ∧ l + r ≤ n + b := by
  constructor
  · rintro ⟨t, hn, hl, hr, hb⟩
    have h := joint_bounds t
    omega
  · rintro ⟨hl, hr, hn⟩
    refine ⟨⟨n + b - (l + r), l - b, r - b, b⟩, ?_, ?_, ?_, rfl⟩
    all_goals simp only [mass, leftRisk, rightRisk]; omega

def WithinJointBound (t : Table) (budget : Nat) : Prop := t.both ≤ budget

theorem left_bound_suffices (t : Table) (budget : Nat)
    (h : leftRisk t ≤ budget) : WithinJointBound t budget := by
  have hb := (joint_bounds t).1
  exact Nat.le_trans hb h

theorem right_bound_suffices (t : Table) (budget : Nat)
    (h : rightRisk t ≤ budget) : WithinJointBound t budget := by
  have hb := (joint_bounds t).2.1
  exact Nat.le_trans hb h

theorem sound_drift_transfer (before after : Table) (allowance budget : Nat)
    (hDrift : after.both ≤ before.both + allowance)
    (hRoom : before.both + allowance ≤ budget) :
    WithinJointBound after budget := by
  exact Nat.le_trans hDrift hRoom

inductive Mode where
  | dispersed | shared | revised
  deriving DecidableEq, Repr

/- Ten equally weighted possibilities. In dispersed mode the two routes have
   distinct two-event vulnerabilities. Shared mode improves each marginal by
   assigning both to one common vulnerability. Revised mode changes the right
   support route to a different one-event vulnerability. No claim that the
   change is free, licensed or generally available is made. -/
def reading (m : Mode) (event : Nat) : Bool × Bool :=
  match m with
  | .dispersed => (decide (event < 2), decide (2 ≤ event ∧ event < 4))
  | .shared => (decide (event = 0), decide (event = 0))
  | .revised => (decide (event = 0), decide (event = 1))

def tally : List (Bool × Bool) → Table
  | [] => ⟨0, 0, 0, 0⟩
  | (false, false) :: xs => let t := tally xs; {t with neither := t.neither + 1}
  | (true, false) :: xs => let t := tally xs; {t with leftOnly := t.leftOnly + 1}
  | (false, true) :: xs => let t := tally xs; {t with rightOnly := t.rightOnly + 1}
  | (true, true) :: xs => let t := tally xs; {t with both := t.both + 1}

def record (m : Mode) : Table := tally ((List.range 10).map (reading m))

theorem dispersed_record : record .dispersed = ⟨6, 2, 2, 0⟩ := by decide
theorem shared_record : record .shared = ⟨9, 0, 0, 1⟩ := by decide
theorem revised_record : record .revised = ⟨8, 1, 1, 0⟩ := by decide

theorem same_mass (m : Mode) : mass (record m) = 10 := by
  cases m <;> decide

theorem better_marginals_worse_joint :
    leftRisk (record .shared) < leftRisk (record .dispersed) ∧
    rightRisk (record .shared) < rightRisk (record .dispersed) ∧
    (record .dispersed).both < (record .shared).both := by decide

theorem repair_preserves_marginals_and_reduces_joint :
    leftRisk (record .revised) = leftRisk (record .shared) ∧
    rightRisk (record .revised) = rightRisk (record .shared) ∧
    (record .revised).both < (record .shared).both := by decide

theorem joint_improvement_can_increase_any_loss :
    (record .revised).both < (record .shared).both ∧
    anyLoss (record .shared) < anyLoss (record .revised) := by decide

/- Retained joint observations have content omitted by the two marginal
   totals. Fresh jointly indexed observations can distinguish these modes. -/
theorem no_marginal_only_joint_estimator :
    ¬ ∃ f : Nat → Nat → Nat,
      ∀ m : Mode, f (leftRisk (record m)) (rightRisk (record m)) = (record m).both := by
  rintro ⟨f, hf⟩
  have hs := hf .shared
  have hr := hf .revised
  rw [shared_record] at hs
  rw [revised_record] at hr
  simp only [leftRisk, rightRisk, Nat.zero_add, Nat.add_zero] at hs hr
  omega

theorem fresh_joint_reading_distinguishes :
    reading .shared 0 ≠ reading .revised 0 := by decide

theorem positive_joint_risk_can_meet_bound :
    0 < (record .shared).both ∧ WithinJointBound (record .shared) 1 := by
  unfold WithinJointBound
  decide

theorem marginal_information_leaves_exact_two_options (b : Nat) :
    Compatible 10 1 1 b ↔ b = 0 ∨ b = 1 := by
  rw [compatible_iff]
  omega

/- These scores diagnose a tradeoff; they are not the ethical ordering of the
   theory and do not prove normative admissibility or defeat J2. -/
def diagnosticLoss (jointWeight : Nat) (t : Table) : Nat :=
  leftRisk t + rightRisk t + jointWeight * t.both

theorem diagnostic_choice_changes_with_joint_weight :
    diagnosticLoss 1 (record .shared) < diagnosticLoss 1 (record .dispersed) ∧
    diagnosticLoss 3 (record .dispersed) < diagnosticLoss 3 (record .shared) := by decide

theorem diagnostic_shared_preferred_iff (jointWeight : Nat) :
    diagnosticLoss jointWeight (record .shared) <
      diagnosticLoss jointWeight (record .dispersed) ↔ jointWeight < 2 := by
  rw [shared_record, dispersed_record]
  simp only [diagnosticLoss, leftRisk, rightRisk, Nat.mul_one, Nat.mul_zero]
  omega

end JointRiskRevision
