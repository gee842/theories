import RelationalBecoming
open RelationalBecoming Generative JointContinuationClassification

example : Eventually process realized .initial both :=
  ⟨2, actual_preparation_changes_effective_capacity.2.2.2⟩

example : ¬ ∃ bundle, Eventually process realized .coupled bundle ∧
    ¬ Eventually process realized .initial bundle :=
  no_new_eventual_bundle (trace_singleton_iff.mpr Step.retainCoupling)
