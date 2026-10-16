import GenerativeComparison
import PracticalJudgment

/-!
# Basic-condition priority against scalar aggregation

9 October 2026. Option `k` of one situation either retains a protected basic
living condition with no secondary gain (`k = 0`) or loses that condition and
realizes `k` secondary generative gains (`k > 0`). The options are differentiated
continuations of the same history; the claims are relations within them, not
holdings of independent owners.

The theorems separate three premises that the alignment direction keeps
distinct. G0 makes each realized gain positively relevant. C favors every no-loss
generative extension. J2 (`PracticalJudgment.Better`) gives a retained basic
condition priority over secondary gains. The checked content is:

* J2's ordering satisfies C here and never trades the protected condition for
  any number of gains, so G0, C and J2 are jointly satisfiable and discriminating;
* a scalar ordering also satisfies C yet trades, so J2 does not follow from G0
  and C;
* every natural-number score that satisfies C trades for some number of gains.
  No such score represents J2's verdict in this situation.

The excluded rival class is uniform-unit aggregation. A rival with bounded,
diminishing sensitivity to further gains (for example real-valued scores
converging below the protected option) is not excluded here and remains a
substantive rival. Whether the condition is basic is a correspondence question.
-/

namespace ProtectionPriorityRival

open GenerativeComparison

/-- The protected basic condition, or the `i`th secondary gain. -/
inductive Claim where
  | basic
  | gain (i : Nat)
  deriving DecidableEq

def realized (k : Nat) : Claim → Prop
  | .basic => k = 0
  | .gain i => i < k

def generative : Claim → Prop
  | .basic => False
  | .gain _ => True

def inventory : Inventory Nat Claim where
  realized := realized
  generative := generative

def protect (k : Nat) (_ : Unit) : Prop := k = 0
def gain (k : Nat) (i : Nat) : Prop := i < k

theorem extension_shape {a b : Nat} (h : GenerativeExtension inventory a b) :
    1 ≤ a ∧ a < b := by
  obtain ⟨keeps, claim, gen, now, before⟩ := h
  cases claim with
  | basic => exact False.elim gen
  | gain i =>
    have hb : i < b := now
    have ha : ¬ i < a := before
    have a_pos : 1 ≤ a := by
      cases a with
      | zero =>
        have : b = 0 := keeps .basic rfl
        omega
      | succ _ => omega
    exact ⟨a_pos, by omega⟩

theorem successor_extends {k : Nat} (pos : 1 ≤ k) :
    GenerativeExtension inventory k (k + 1) := by
  refine ⟨?_, .gain k, True.intro, ?_, ?_⟩
  · intro claim held
    cases claim with
    | basic =>
      have : k = 0 := held
      omega
    | gain i =>
      have : i < k := held
      show i < k + 1
      omega
  · show k < k + 1
    omega
  · show ¬ k < k
    exact Nat.lt_irrefl k

/-- G0 recognizes every realized gain of a protection-losing option. -/
theorem g0_recognizes_traded_gains (PositiveRelevant : Nat → Claim → Prop)
    (g0 : G0 inventory PositiveRelevant) :
    ∀ k i, i < k → PositiveRelevant k (.gain i) :=
  fun k i hi => g0 k (.gain i) True.intro hi

/-- Consistency and discrimination: J2's ordering satisfies C in this situation. -/
theorem priority_satisfies_comparison :
    ComparisonPrinciple inventory
      (fun first second => PracticalJudgment.Better protect gain second first) := by
  intro a b ext
  obtain ⟨a_pos, lt⟩ := extension_shape ext
  refine Or.inr ⟨?_, ?_, ?_, ?_⟩
  · intro _ h
    have : a = 0 := h
    omega
  · intro _ h
    have : b = 0 := h
    omega
  · intro i hi
    show i < b
    have : i < a := hi
    omega
  · intro back
    have := back a lt
    exact Nat.lt_irrefl a this

/-- J2 never trades the protected condition, whatever the number of gains. -/
theorem priority_never_trades :
    ∀ k, 0 < k → ¬ PracticalJudgment.Better protect gain k 0 := by
  intro k pos
  exact PracticalJudgment.no_protection_trade_by_count () rfl
    (by show ¬ k = 0; omega)

/-- Independence: a scalar ordering satisfying C trades the protected condition. -/
def weighted (protectWeight : Nat) (k : Nat) : Nat :=
  (if k = 0 then protectWeight else 0) + k

theorem weighted_satisfies_comparison (protectWeight : Nat) :
    ComparisonPrinciple inventory
      (fun first second => weighted protectWeight first < weighted protectWeight second) := by
  intro a b ext
  obtain ⟨a_pos, lt⟩ := extension_shape ext
  have ha : a ≠ 0 := by omega
  have hb : b ≠ 0 := by omega
  simp [weighted, ha, hb]
  exact lt

theorem weighted_trades (protectWeight : Nat) :
    weighted protectWeight 0 < weighted protectWeight (protectWeight + 1) := by
  simp [weighted]

theorem comparison_does_not_yield_priority :
    ∃ score : Nat → Nat,
      ComparisonPrinciple inventory (fun first second => score first < score second) ∧
      ∃ k, 0 < k ∧ score 0 < score k ∧ ¬ PracticalJudgment.Better protect gain k 0 :=
  ⟨weighted 0, weighted_satisfies_comparison 0, 1, by omega, by simp [weighted],
    priority_never_trades 1 (by omega)⟩

/-- Every natural-number score satisfying C trades for some number of gains. -/
theorem every_scalar_comparison_trades (score : Nat → Nat)
    (comparison : ComparisonPrinciple inventory (fun first second => score first < score second)) :
    0 < score 0 + 2 ∧ score 0 < score (score 0 + 2) := by
  have climb : ∀ m, score 1 + m ≤ score (1 + m) := by
    intro m
    induction m with
    | zero => exact Nat.le_refl _
    | succ j ih =>
      have := comparison (1 + j) (1 + j + 1) (successor_extends (by omega))
      have eq : 1 + (j + 1) = 1 + j + 1 := by omega
      rw [eq]
      omega
  have := climb (score 0 + 1)
  have eq : 1 + (score 0 + 1) = score 0 + 2 := by omega
  rw [eq] at this
  exact ⟨by omega, by omega⟩

theorem no_scalar_represents_priority :
    ¬ ∃ score : Nat → Nat,
      ComparisonPrinciple inventory (fun first second => score first < score second) ∧
      ∀ k, 0 < k → score k ≤ score 0 := by
  rintro ⟨score, comparison, never⟩
  obtain ⟨pos, trade⟩ := every_scalar_comparison_trades score comparison
  have := never (score 0 + 2) pos
  omega

end ProtectionPriorityRival
