import RelationalGrounding
open RelationalGrounding GenerativeComparison JointContinuationClassification

-- C is explicit, and the independently checked relational extension feeds it.
example (Better : Regime → Regime → Prop)
    (comparison : ComparisonPrinciple jointInventory Better) :
    Better Regime.released Regime.retained :=
  comparison _ _ joint_bundle_extension

-- A one-valued summary cannot satisfy the strict comparison requirement.
example (r : Unit → Unit → Prop) (strict : ∀ s, ¬ r s s) :
    ¬ ComparisonPrinciple jointInventory (fun _ _ => r () ()) :=
  strict_comparison_cannot_factor_through_marginals (fun _ => ())
    (fun _ _ _ => rfl) r strict

-- Only the full represented bundle is marked generative; one marginal is not.
example : ¬ jointInventory.generative (fun c => c = Claim.leftRealized) := by
  intro h
  have impossible := h Claim.rightRealized
  cases impossible
