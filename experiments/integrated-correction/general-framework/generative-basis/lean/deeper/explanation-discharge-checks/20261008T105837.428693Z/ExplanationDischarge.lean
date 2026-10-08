import Init

/-!
An audit of reasoning from requirements on explanations to a target claim.
`admitted` is an explicitly supplied interface, not a definition of adequate
explanation or a representation of all actual systems. The theorems assess
this inference route; they do not refute a generative ontology.
-/

namespace ExplanationDischarge

universe u v

/-- Requiring every admitted explanation to yield a claim has precisely
    conditional force on the existence of an admitted explanation. -/
theorem consequence_iff_witness_implication {E : Type u}
    (admitted : E → Prop) (claim : Prop) :
    (∀ e, admitted e → claim) ↔ ((∃ e, admitted e) → claim) := by
  constructor
  · intro consequence witness
    obtain ⟨e, he⟩ := witness
    exact consequence e he
  · intro consequence e he
    exact consequence ⟨e, he⟩

/-- A uniform rule that removes this condition for arbitrary claims has
    exactly the strength of an admitted witness. This does not impose a
    witness requirement on a particular claim proved by another route. -/
theorem uniform_discharge_iff_witness {E : Type u}
    (admitted : E → Prop) :
    (∀ claim : Prop, (∀ e, admitted e → claim) → claim) ↔
      (∃ e, admitted e) := by
  constructor
  · intro discharge
    exact discharge (∃ e, admitted e) (fun e he => ⟨e, he⟩)
  · intro witness claim consequence
    obtain ⟨e, he⟩ := witness
    exact consequence e he

/-- A requirement over an empty admitted interface can hold for any claim.
    This is a logical scope control, not a physical countermodel. -/
theorem empty_interface_satisfies_every_requirement {E : Type u}
    (admitted : E → Prop) (absent : ∀ e, ¬ admitted e) :
    ∀ claim : Prop, ∀ e, admitted e → claim := by
  intro claim e he
  exact False.elim (absent e he)

/-- The positive route keeps target coverage and the substantive consequence
    separately visible. Neither premise is supplied by the theorem. -/
theorem covered_targets_inherit_consequence {T : Type u} {E : T → Type v}
    (inScope : T → Prop) (admitted : (t : T) → E t → Prop)
    (claim : T → Prop)
    (coverage : ∀ t, inScope t → ∃ e, admitted t e)
    (consequence : ∀ t, inScope t → ∀ e, admitted t e → claim t) :
    ∀ t, inScope t → claim t := by
  intro t ht
  obtain ⟨e, he⟩ := coverage t ht
  exact consequence t ht e he

#print axioms consequence_iff_witness_implication
#print axioms uniform_discharge_iff_witness
#print axioms empty_interface_satisfies_every_requirement
#print axioms covered_targets_inherit_consequence

end ExplanationDischarge
