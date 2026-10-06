import BoundaryModels
import Depletion
import RootRealization
import ProductTower
import GeneratedPaths
import HistoryRealization
import DynamicClassification

/-!
# Integrated entry point for the existing generative model

The original Process and Trace remain unchanged. The results below connect
the deeper law classification to the same finite-history semantics and
synchronous composition used by the model. No primitive physical law or
globally asserted property of every process is introduced.
-/

namespace Generative.Model

open Deeper
universe u v

theorem laws_iff_endpoint_histories
    {State : Type u} {Action : Type v} (P Q : Process State Action) :
    SameSteps P Q ↔
      ∀ s (word : List Action) t, Trace P s word t ↔ Trace Q s word t :=
  same_steps_iff_endpoint_traces P Q

/-- The previously defined property package has exactly two endpoint-history descriptions. -/
theorem boolean_symmetry_iff_history_classes (P : Process Bool Unit) :
    SymmetryCandidate P ↔
      (∀ s (word : List Unit) t, Trace P s word t ↔ Trace static s word t) ∨
      (∀ s (word : List Unit) t, Trace P s word t ↔ Trace toggle s word t) := by
  constructor
  · intro h
    cases (symmetry_candidate_iff_descriptions P).mp h with
    | inl hs => exact Or.inl ((same_steps_iff_endpoint_traces P static).mp hs)
    | inr ht => exact Or.inr ((same_steps_iff_endpoint_traces P toggle).mp ht)
  · intro h
    apply (symmetry_candidate_iff_descriptions P).mpr
    cases h with
    | inl hs => exact Or.inl ((same_steps_iff_endpoint_traces P static).mpr hs)
    | inr ht => exact Or.inr ((same_steps_iff_endpoint_traces P toggle).mpr ht)

/-- Reversal and unique predecessors are derived in this Boolean characterization. -/
theorem reduced_boolean_properties_iff_history_classes (P : Process Bool Unit) :
    (StepTotal P ∧ StepDeterministic P ∧ BoolRenamingInvariant P) ↔
      (∀ s (word : List Unit) t, Trace P s word t ↔ Trace static s word t) ∨
      (∀ s (word : List Unit) t, Trace P s word t ↔ Trace toggle s word t) :=
  (symmetry_candidate_iff_reduced_properties P).symm.trans
    (boolean_symmetry_iff_history_classes P)

/-- The actual model API retains a closed distinction that word feasibility erases. -/
theorem symmetric_laws_same_words_different_histories :
    ∃ P Q : Process Bool Unit,
      SymmetryCandidate P ∧ SymmetryCandidate Q ∧
      (∀ s (word : List Unit), Feasible P s word ↔ Feasible Q s word) ∧
      Trace P false [()] false ∧ ¬ Trace Q false [()] false := by
  exact ⟨static, toggle, static_symmetry_candidate, toggle_symmetry_candidate,
    static_toggle_same_feasible, static_toggle_singleton_endpoints_differ⟩

/-- Synchronizing on action words alone does not recover the erased state difference.
This is the core's defined synchronous product, not every possible coupling. -/
theorem synchronized_word_constraints_preserve_feasibility_agreement
    {Other : Type u} (Q : Process Other Unit)
    (s : Bool) (q : Other) (word : List Unit) :
    Feasible (productProcess static Q) (s, q) word ↔
      Feasible (productProcess toggle Q) (s, q) word := by
  constructor
  · intro h
    obtain ⟨hs, hq⟩ := feasible_product_iff.mp h
    exact feasible_product_iff.mpr
      ⟨(static_toggle_same_feasible s word).mp hs, hq⟩
  · intro h
    obtain ⟨ht, hq⟩ := feasible_product_iff.mp h
    exact feasible_product_iff.mpr
      ⟨(static_toggle_same_feasible s word).mpr ht, hq⟩

end Generative.Model

#print axioms Generative.Model.laws_iff_endpoint_histories
#print axioms Generative.Model.boolean_symmetry_iff_history_classes
#print axioms Generative.Model.reduced_boolean_properties_iff_history_classes
#print axioms Generative.Model.symmetric_laws_same_words_different_histories
#print axioms Generative.Model.synchronized_word_constraints_preserve_feasibility_agreement
