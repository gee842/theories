import Std

/-!
Finite phase correspondence, not a proof of biological independence or causality.
`a,b,c,d` are joint, first-only, second-only, neither counts. The empirical
complete-case table is (28,22,130,3). Its one omitted contaminated record is
handled separately by both possible binary completions. Source-to-count and
parent-to-descendant correspondences are checked numerically, not assumed proved
by these identities. No new ethical or evolutionary universality is asserted.
-/
namespace LifecycleCorrespondence

theorem joint_marginal_numerator (a b c d : Rat) :
    a * (a+b+c+d) - (a+b)*(a+c) = a*d-b*c := by grind

theorem numerator_agreement_iff (a b c d : Rat) :
    a*(a+b+c+d) = (a+b)*(a+c) ↔ a*d = b*c := by grind

/-- Valid only when stage-two trials are exactly the survivors of stage one;
    the algebra does not establish that experimental correspondence. -/
theorem conditional_stage_composition (n survivors finalCount : Rat)
    (nonzero : survivors ≠ 0) :
    (survivors/n)*(finalCount/survivors) = finalCount/n := by
  grind

theorem complete_record_product_overstates_joint :
    (50:Rat)/183 * (158/183) > 28/183 := by decide +kernel

theorem both_missing_record_completions_preserve_discrepancy :
    (51:Rat)/184*(158/184) > 28/184 ∧
    (51:Rat)/184*(159/184) > 29/184 := by decide +kernel

theorem linked_assay_counts :
    (47:Rat)/72*(42/47)=42/72 ∧
    (31:Rat)/72*(7/31)=7/72 ∧
    (42:Rat)/72-(7/72)=35/72 ∧
    ((42:Rat)/72)/((7:Rat)/72)=6 := by decide +kernel

end LifecycleCorrespondence
