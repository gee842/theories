import RenewalComparison
open GenerativeComparison RenewalComparison
example (Better : Growth → Growth → Prop)
    (c : ComparisonPrinciple (relationalInventory tumor) Better) : Better .occurs .absent :=
  (relational_comparison_ranks Better c).1
example : ¬ GenerativeExtension (broadInventory tumor) .occurs .absent :=
  fun ext => tumor_broad_incomparable.1 ext.1
example : ∃ Better : Growth → Growth → Prop,
    ComparisonPrinciple (broadInventory tumor) Better ∧ Better .absent .occurs :=
  ⟨preferMalignant, broad_comparison_admits_malignant.1, broad_comparison_admits_malignant.2.1⟩
example (PositiveRelevant : Contest → RelationalRenewal.Law.Part × Nat → Prop)
    (g0 : G0 (relationalInventory contest) PositiveRelevant) (t : Nat) :
    PositiveRelevant .shares (.sustaining, t) :=
  g0 _ _ trivial (sharing_grounds _)
