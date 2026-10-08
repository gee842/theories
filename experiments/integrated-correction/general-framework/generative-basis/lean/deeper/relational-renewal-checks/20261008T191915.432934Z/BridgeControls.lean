import RenewalComparison
open GenerativeComparison RenewalComparison RelationalRenewal.Law
example (Better : Growth → Growth → Prop)
    (c : ComparisonPrinciple (relationalInventory (course malignant)) Better) :
    Better .occurs .absent :=
  malignant_comparison.1 Better c
example : ¬ GenerativeExtension (broadInventory (course winning)) .occurs .absent :=
  fun ext => (overdraw_broad_incomparable winning (Nat.succ_pos 0) (Nat.zero_le 1)
    (Nat.le_succ_of_le (Nat.le_succ 1)) (T0 := 0) (fun _ _ => Nat.lt_succ_self 1)).1 ext.1
example : ∃ Better : Growth → Growth → Prop,
    ComparisonPrinciple (broadInventory (course malignant)) Better ∧ Better .absent .occurs :=
  ⟨preferOccurs malignant, malignant_comparison.2.1, malignant_comparison.2.2.1⟩
example (PositiveRelevant : Contest → Part × Nat → Prop)
    (g0 : G0 (relationalInventory contest) PositiveRelevant) (t : Nat) :
    PositiveRelevant .shares (.sustaining, t) :=
  g0 _ _ trivial (sharing_grounds _)
