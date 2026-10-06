import DynamicConsequences

/-!
# Exact classification of the existing Boolean dynamics package

For the existing Bool states and Unit actions, totality, determinism and
invariance under every Boolean renaming already force the step relation to
have exactly the static description or exactly the toggle description.
Both descriptions satisfy the existing stronger SymmetryCandidate package.

The characterizations below quantify over processes rather than assert that
an actual system satisfies either package. They add no primitive event law,
physical identification, axiom or choice of one of the two descriptions.
Pointwise equivalence avoids equating functions or propositions by extensionality.
-/

namespace Generative.Deeper

/-- A complete step description transports the existing property package. -/
theorem symmetry_candidate_of_step_description
    {P Q : Process Bool Unit} (hdescription : SameSteps P Q)
    (hQ : SymmetryCandidate Q) : SymmetryCandidate P := by
  obtain ⟨htotal, hdet, hreverse, hpredecessor, hrename⟩ := hQ
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro s a
    obtain ⟨t, ht⟩ := htotal s a
    exact ⟨t, (hdescription s a t).mpr ht⟩
  · intro s a t r ht hr
    exact hdet s a t r ((hdescription s a t).mp ht)
      ((hdescription s a r).mp hr)
  · intro s a t ht
    exact (hdescription t a s).mpr
      (hreverse s a t ((hdescription s a t).mp ht))
  · intro t a
    obtain ⟨s, hs, hunique⟩ := hpredecessor t a
    refine ⟨s, (hdescription s a t).mpr hs, ?_⟩
    intro r hr
    exact hunique r ((hdescription r a t).mp hr)
  · intro f hf s a t
    constructor
    · intro ht
      exact (hdescription (f s) a (f t)).mpr
        ((hrename f hf s a t).mp ((hdescription s a t).mp ht))
    · intro ht
      exact (hdescription s a t).mpr
        ((hrename f hf s a t).mpr ((hdescription (f s) a (f t)).mp ht))

/-- The smaller existing property package has only these two step descriptions. -/
theorem total_deterministic_renaming_descriptions
    (P : Process Bool Unit) (htotal : StepTotal P)
    (hdet : StepDeterministic P) (hrename : BoolRenamingInvariant P) :
    SameSteps P static ∨ SameSteps P toggle := by
  obtain ⟨next, hnext⟩ := htotal false ()
  cases next
  · have htrue : P.step true () true :=
      (hrename Bool.not negation_bool_bijection false () false).mp hnext
    have hloop : ∀ s, P.step s () s := by
      intro s
      cases s
      · exact hnext
      · exact htrue
    left
    intro s a t
    cases a
    constructor
    · intro ht
      exact hdet s () s t (hloop s) ht
    · intro ht
      change s = t at ht
      cases ht
      exact hloop s
  · have htrue : P.step true () false :=
      (hrename Bool.not negation_bool_bijection false () true).mp hnext
    have hchange : ∀ s, P.step s () (!s) := by
      intro s
      cases s
      · exact hnext
      · exact htrue
    right
    intro s a t
    cases a
    constructor
    · intro ht
      exact hdet s () t (!s) ht (hchange s)
    · intro ht
      change t = !s at ht
      cases ht
      exact hchange s

/-- A closed characterization, not an assertion that every process has these properties. -/
theorem total_deterministic_renaming_iff_descriptions (P : Process Bool Unit) :
    (StepTotal P ∧ StepDeterministic P ∧ BoolRenamingInvariant P) ↔
      SameSteps P static ∨ SameSteps P toggle := by
  constructor
  · rintro ⟨htotal, hdet, hrename⟩
    exact total_deterministic_renaming_descriptions P htotal hdet hrename
  · intro hdescription
    have hcandidate : SymmetryCandidate P := by
      cases hdescription with
      | inl h => exact symmetry_candidate_of_step_description h static_symmetry_candidate
      | inr h => exact symmetry_candidate_of_step_description h toggle_symmetry_candidate
    exact ⟨hcandidate.1, hcandidate.2.1, hcandidate.2.2.2.2⟩

/-- Exact classification of the already defined complete finite constraint package. -/
theorem symmetry_candidate_iff_descriptions (P : Process Bool Unit) :
    SymmetryCandidate P ↔
      SameSteps P static ∨ SameSteps P toggle := by
  constructor
  · intro h
    exact total_deterministic_renaming_descriptions P h.1 h.2.1 h.2.2.2.2
  · intro h
    cases h with
    | inl hs => exact symmetry_candidate_of_step_description hs static_symmetry_candidate
    | inr ht => exact symmetry_candidate_of_step_description ht toggle_symmetry_candidate

/-- In this two-state package, reversal and unique predecessors need not be additional premises. -/
theorem symmetry_candidate_iff_reduced_properties (P : Process Bool Unit) :
    SymmetryCandidate P ↔
      StepTotal P ∧ StepDeterministic P ∧ BoolRenamingInvariant P := by
  constructor
  · intro h
    exact ⟨h.1, h.2.1, h.2.2.2.2⟩
  · intro h
    exact (symmetry_candidate_iff_descriptions P).mpr
      ((total_deterministic_renaming_iff_descriptions P).mp h)

/-- The two descriptions are disjoint, including when used for another process. -/
theorem static_toggle_descriptions_exclusive (P : Process Bool Unit) :
    ¬ (SameSteps P static ∧ SameSteps P toggle) := by
  rintro ⟨hstatic, htoggle⟩
  have hP : P.step false () false :=
    (hstatic false () false).mpr (static_event false)
  have htoggle_loop := (htoggle false () false).mp hP
  exact toggle_always_changes htoggle_loop rfl

end Generative.Deeper

#print axioms Generative.Deeper.symmetry_candidate_of_step_description
#print axioms Generative.Deeper.total_deterministic_renaming_descriptions
#print axioms Generative.Deeper.total_deterministic_renaming_iff_descriptions
#print axioms Generative.Deeper.symmetry_candidate_iff_descriptions
#print axioms Generative.Deeper.symmetry_candidate_iff_reduced_properties
#print axioms Generative.Deeper.static_toggle_descriptions_exclusive
