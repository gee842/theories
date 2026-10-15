import BoundaryModels -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.same_steps_iff_traces`, `Becoming.same_steps_iff_endpoint_traces_by_core` — 同一陈述 / the same statement; MODULE-CLASSIFICATION.md
import Depletion
import RootRealization
import ProductTower
import GeneratedPaths
import HistoryRealization
import DynamicClassification
import GeneratedSelf
import EthicalOrientation

/-!
# Integrated entry point for the existing generative model

The original Process and Trace remain unchanged. The results below connect
the deeper law classification, history-conditioned representation contracts and
orientation limits to the same finite-history semantics and synchronous
composition used by the model. No primitive physical law, acquired self-model,
normative direction or globally asserted property of every process is introduced.
-/

namespace Generative.Model

open Deeper
universe u v w

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

/-- The public model can test a proposed record's exact continuation contract.
Neither the record nor its interpreter is asserted to be physically acquired. -/
theorem history_record_exactness_iff
    {State : Type u} {Action : Type v} {Summary : Type w}
    (P : Process State Action) (initial : State)
    (record : List Action → Summary) :
    (∃ accept, SelfFormation.ExactSummary P initial record accept) ↔
      ∀ past other, record past = record other →
        SelfFormation.SameProfile P initial past other :=
  SelfFormation.exact_summary_exists_iff record

/-- An existing actual change can be invisible to all feasible-future profiles.
The excluded decoder recovers current phase; not every usable self-model needs
that exact task, and no universal impossibility of self formation follows. -/
theorem changed_endpoint_with_no_profile_only_decoder :
    (Trace toggle false [] false ∧ Trace toggle false [()] true ∧
      false ≠ true ∧ SelfFormation.SameProfile toggle false [] [()]) ∧
    ¬ ∃ readout : List Unit → Bool,
      (∀ past other, SelfFormation.SameProfile toggle false past other →
        readout past = readout other) ∧
      (∀ past current, Trace toggle false past current → readout past = current) :=
  ⟨SelfFormation.toggle_states_differ_profiles_agree,
    SelfFormation.no_profile_only_toggle_state_decoder⟩

/-- The same actual histories instantiate the representation and orientation
interfaces. Removing annotation dependence and demanding a coherent order do
not choose whether the longer history is preferred. No claim that these weak
conditions exhaust ethical justification or constitute selfhood is made. -/
theorem history_profiles_and_invariance_do_not_select_orientation :
    (Trace toggle false [] false ∧ Trace toggle false [(), ()] false) ∧
    SelfFormation.SameProfile toggle false [] [(), ()] ∧
    ¬ (∀ R : (List Unit × Bool) → (List Unit × Bool) → Prop,
      EthicalOrientation.PreorderLaws R →
      EthicalOrientation.FiberInvariant Prod.fst R →
      R ([], false) ([(), ()], true)) :=
  EthicalOrientation.actual_histories_with_unselected_orientation

end Generative.Model

#print axioms Generative.Model.laws_iff_endpoint_histories
#print axioms Generative.Model.boolean_symmetry_iff_history_classes
#print axioms Generative.Model.reduced_boolean_properties_iff_history_classes
#print axioms Generative.Model.symmetric_laws_same_words_different_histories
#print axioms Generative.Model.synchronized_word_constraints_preserve_feasibility_agreement

#print axioms Generative.Model.history_record_exactness_iff
#print axioms Generative.Model.changed_endpoint_with_no_profile_only_decoder
#print axioms Generative.Model.history_profiles_and_invariance_do_not_select_orientation
