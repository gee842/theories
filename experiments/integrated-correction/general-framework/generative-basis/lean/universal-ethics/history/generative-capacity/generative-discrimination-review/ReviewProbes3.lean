import ProtectionPriorityRival
open GenerativeComparison ProtectionPriorityRival

/-! Probe 9: count the retained basic living condition as generative too (G0 then gives it
positive relevance). The extension shape, hence every downstream result, is unchanged. -/
def inventoryB : Inventory Nat Claim where
  realized := realized
  generative := fun _ => True

theorem extension_shapeB {a b : Nat} (h : GenerativeExtension inventoryB a b) :
    1 ≤ a ∧ a < b := by
  obtain ⟨keeps, claim, _, now, before⟩ := h
  cases claim with
  | basic =>
    have hb : b = 0 := now
    have ha : ¬ a = 0 := before
    -- a has a gain (a ≥ 1) that must survive in b = 0: impossible
    have : 0 < b := keeps (.gain 0) (show 0 < a by omega)
    omega
  | gain i =>
    have hb : i < b := now
    have ha : ¬ i < a := before
    cases a with
    | zero => have : b = 0 := keeps .basic rfl
              omega
    | succ _ => exact ⟨by omega, by omega⟩

theorem every_nat_score_tradesB (score : Nat → Nat)
    (comparison : ComparisonPrinciple inventoryB (fun first second => score first < score second)) :
    score 0 < score (score 0 + 2) := by
  have succ_ext : ∀ k, 1 ≤ k → GenerativeExtension inventoryB k (k + 1) := by
    intro k pos
    refine ⟨?_, .gain k, True.intro, (show k < k + 1 by omega), (show ¬ k < k by omega)⟩
    intro claim held
    cases claim with
    | basic => have : k = 0 := held; omega
    | gain i => have : i < k := held; show i < k + 1; omega
  have climb : ∀ m, score 1 + m ≤ score (1 + m) := by
    intro m
    induction m with
    | zero => exact Nat.le_refl _
    | succ j ih =>
      have := comparison (1 + j) (1 + j + 1) (succ_ext _ (by omega))
      have eq : 1 + (j + 1) = 1 + j + 1 := by omega
      rw [eq]; omega
  have := climb (score 0 + 1)
  have eq : 1 + (score 0 + 1) = score 0 + 2 := by omega
  rw [eq] at this; omega
