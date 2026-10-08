import GenerativeComparison
import PracticalJudgment

/-!
# Basic-condition priority against score aggregation

9 October 2026. Option `k` of one situation either retains a protected basic
living condition with no secondary gain (`k = 0`) or loses that condition and
realizes `k` secondary generative gains (`k > 0`). The options are differentiated
continuations of the same history; the claims are relations within them, not
holdings of independent owners.

The theorems separate three premises that the alignment direction keeps
distinct. G0 makes each realized gain positively relevant. C favors every no-loss
generative extension. J2 (`PracticalJudgment.Better`) gives a retained basic
condition priority over secondary gains. The checked content, for this one
constructed situation, is:

* G0, C and J2's ordering hold together, and J2 never trades the protected
  condition for any number of gains;
* G0 constrains positive relevance, not ordering: it holds equally alongside a
  trading ordering that satisfies C, so J2 does not follow from G0 and C;
* every natural-number score satisfying C trades for some number of gains, so no
  such score represents J2's verdict here. The force is the unit step of a
  strictly increasing natural-number score;
* a bounded rational score (`1` for protection, `k / (k + 1)` for `k` gains)
  satisfies C, never trades and agrees with J2 on every pair of options.

So this situation separates J2 from unit-step aggregation only. Bounded,
diminishing sensitivity to further gains represents J2 exactly here and remains a
substantive rival; separating them needs other situations. That J2 does not
follow from C instances the earlier point that C is silent on trade-offs
(`GenerativeComparison.tradeoff_has_opposite_strict_appraisals`,
`GenerativeLossComparison.loss_sensitivity_alone_supplies_no_cutoff`). Whether the
condition is basic is a correspondence question.
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

/-- J2's ordering satisfies C in this situation. -/
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
theorem every_nat_score_trades (score : Nat → Nat)
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

theorem no_nat_score_represents_priority :
    ¬ ∃ score : Nat → Nat,
      ComparisonPrinciple inventory (fun first second => score first < score second) ∧
      ∀ k, 0 < k → score k ≤ score 0 := by
  rintro ⟨score, comparison, never⟩
  obtain ⟨pos, trade⟩ := every_nat_score_trades score comparison
  have := never (score 0 + 2) pos
  omega

/-- G0, C and J2 hold together. G0 places no constraint on ordering: it holds
equally alongside a trading ordering that also satisfies C. -/
theorem g0_leaves_ordering_open :
    G0 inventory (fun _ _ => True) ∧
      ComparisonPrinciple inventory
        (fun first second => PracticalJudgment.Better protect gain second first) ∧
      (∀ k, 0 < k → ¬ PracticalJudgment.Better protect gain k 0) ∧
      ComparisonPrinciple inventory (fun first second => weighted 0 first < weighted 0 second) ∧
      weighted 0 0 < weighted 0 1 :=
  ⟨fun _ _ _ _ => True.intro, priority_satisfies_comparison, priority_never_trades,
    weighted_satisfies_comparison 0, by decide⟩

/-- J2's ordering in this situation: protection is better than any gains, and among
protection-losing options more gains are better. -/
theorem priority_iff (a b : Nat) :
    PracticalJudgment.Better protect gain a b ↔ (a = 0 ∧ b ≠ 0) ∨ (b ≠ 0 ∧ b < a) := by
  constructor
  · rintro (⟨_, notback⟩ | ⟨keeps, _, _, notback⟩)
    · left
      have : ∃ u, protect a u ∧ ¬ protect b u :=
        Classical.byContradiction fun none => notback fun u h =>
          Classical.byContradiction fun nb => none ⟨u, h, nb⟩
      obtain ⟨_, ha, hb⟩ := this
      exact ⟨ha, hb⟩
    · right
      have : ∃ i, gain a i ∧ ¬ gain b i :=
        Classical.byContradiction fun none => notback fun i h =>
          Classical.byContradiction fun nb => none ⟨i, h, nb⟩
      obtain ⟨i, ha, hb⟩ := this
      have ha : i < a := ha
      have hb : ¬ i < b := hb
      refine ⟨fun b0 => ?_, by omega⟩
      have : a = 0 := keeps () b0
      omega
  · rintro (⟨a0, b0⟩ | ⟨b0, lt⟩)
    · refine Or.inl ⟨fun _ h => absurd h b0, fun back => b0 (back () a0)⟩
    · have a0 : a ≠ 0 := by omega
      refine Or.inr ⟨fun _ h => absurd h b0, fun _ h => absurd h a0, ?_, ?_⟩
      · intro i hi
        show i < a
        have : i < b := hi
        omega
      · intro back
        have := back b lt
        exact Nat.lt_irrefl b this

/-- A bounded rival: score `1` for protection and `k / (k + 1)` for `k` gains, with
values in `[0, 1]`, compared by cross-multiplication. -/
def num (k : Nat) : Nat := if k = 0 then 1 else k
def den (k : Nat) : Nat := if k = 0 then 1 else k + 1

/-- `ratioBetter first second`: the second option's bounded score is strictly higher. -/
def ratioBetter (first second : Nat) : Prop := num first * den second < num second * den first

theorem ratio_bounded (k : Nat) : num k ≤ den k := by
  unfold num den; split <;> omega

/-- The bounded score agrees with J2 on every pair of options in this situation. -/
theorem ratio_agrees_with_priority (a b : Nat) :
    ratioBetter b a ↔ PracticalJudgment.Better protect gain a b := by
  rw [priority_iff]
  unfold ratioBetter num den
  by_cases ha : a = 0 <;> by_cases hb : b = 0
  · subst ha; subst hb; simp
  · subst ha; simp [hb]
  · subst hb; simp [ha]
  · simp only [if_neg ha, if_neg hb]
    rw [Nat.mul_add, Nat.mul_add, Nat.mul_one, Nat.mul_one, Nat.mul_comm b a]
    constructor
    · intro h; right; exact ⟨hb, by omega⟩
    · rintro (⟨h, _⟩ | ⟨_, h⟩)
      · exact absurd h ha
      · omega

/-- Hence a bounded score satisfies C and never trades: the exclusion above depends on
natural-number values, and bounded sensitivity is not excluded in this situation. -/
theorem bounded_score_represents_priority :
    ComparisonPrinciple inventory ratioBetter ∧ ∀ k, 0 < k → ¬ ratioBetter 0 k :=
  ⟨fun a b ext => (ratio_agrees_with_priority b a).mpr (priority_satisfies_comparison a b ext),
    fun k pos h => priority_never_trades k pos ((ratio_agrees_with_priority k 0).mp h)⟩

end ProtectionPriorityRival
