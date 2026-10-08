import GenerativeClosure

/-!
# One interpretation for an entire finitely based theory

Migration of HUIGEN-GENERATIVE-CLOSURE.md H10-H12 into the existing calculus.
Candidate interpretations are the semantic carrier; their admissibility is
explicit and is not defined to make the basis true. The proof uses the derived
conjunction of a covering list of basis indices, not a choice of a witness for
each descendant. It also covers an empty basis via a derived tautology.

This does not supply an actual interpretation, its admissibility, root truth,
or a necessary generative process law. It reduces a coherence obligation when
the stated full-closure coverage has already been warranted.
-/

namespace InquiryRoot.JointInterpretation

universe u v
variable {World : Type u} {Index : Type v}

/-- The empty package is a derivable implication, not an added truth rule. -/
def package (basis : Index → Formula World) : List Index → Formula World
  | [] => fun _ => True → True
  | i :: rest => fun w => basis i w ∧ package basis rest w

theorem package_derivable (basis : Index → Formula World) (indices : List Index) :
    Derives basis [] (package basis indices) := by
  induction indices with
  | nil => exact .impIntro (.assumption (List.mem_cons_self))
  | cons i rest ih => exact .andIntro (.base i) ih

theorem package_iff_list (basis : Index → Formula World)
    (indices : List Index) (w : World) :
    package basis indices w ↔ ∀ i, i ∈ indices → basis i w := by
  induction indices with
  | nil =>
    constructor
    · intro _ i hi
      exact False.elim (List.not_mem_nil hi)
    · intro _ h
      exact h
  | cons i rest ih =>
    constructor
    · intro h j hj
      cases hj with
      | head => exact h.1
      | tail _ ht => exact ih.mp h.2 j ht
    · intro h
      exact ⟨h i (List.mem_cons_self), ih.mpr (fun j hj => h j (List.mem_cons_of_mem i hj))⟩

theorem package_iff_basis (basis : Index → Formula World)
    (indices : List Index) (covers : ∀ i, i ∈ indices) (w : World) :
    package basis indices w ↔ ∀ i, basis i w := by
  constructor
  · intro h i
    exact (package_iff_list basis indices w).mp h i (covers i)
  · intro h
    exact (package_iff_list basis indices w).mpr (fun i _ => h i)

/-- Soundness at one interpretation, including all retained local premises. -/
theorem basis_iff_relative_closure (basis : Index → Formula World) (w : World) :
    (∀ i, basis i w) ↔
      ∀ context p, Derives basis context p → Holds context w → p w := by
  constructor
  · intro hb context p proof hc
    exact derivation_sound proof w hb hc
  · intro all i
    exact all [] (basis i) (.base i) (fun _ h => False.elim (List.not_mem_nil h))

theorem common_basis_iff_common_closure (basis : Index → Formula World)
    (admissible : World → Prop) :
    (∃ w, admissible w ∧ ∀ i, basis i w) ↔
      ∃ w, admissible w ∧ ∀ p, Derives basis [] p → p w := by
  constructor
  · rintro ⟨w, ha, hb⟩
    exact ⟨w, ha, fun _ proof => derivation_sound proof w hb
      (fun _ h => False.elim (List.not_mem_nil h))⟩
  · rintro ⟨w, ha, all⟩
    exact ⟨w, ha, fun i => all (basis i) (.base i)⟩

/-- Full pointwise coverage supplies a single witness through the package.
    Checking only separate basis rows is a strictly weaker antecedent. -/
theorem pointwise_closure_iff_common (basis : Index → Formula World)
    (indices : List Index) (covers : ∀ i, i ∈ indices)
    (admissible : World → Prop) :
    (∀ p, Derives basis [] p → ∃ w, admissible w ∧ p w) ↔
      ∃ w, admissible w ∧ ∀ p, Derives basis [] p → p w := by
  constructor
  · intro each
    obtain ⟨w, ha, hp⟩ := each (package basis indices) (package_derivable basis indices)
    exact (common_basis_iff_common_closure basis admissible).mp
      ⟨w, ha, (package_iff_basis basis indices covers w).mp hp⟩
  · rintro ⟨w, ha, all⟩ p proof
    exact ⟨w, ha, all p proof⟩

/-- The witness also supports every local derivation conditionally. Local
    hypotheses are preserved, not made true by the interpretation theorem. -/
theorem pointwise_closure_gives_common_relative
    (basis : Index → Formula World) (indices : List Index)
    (covers : ∀ i, i ∈ indices) (admissible : World → Prop)
    (each : ∀ p, Derives basis [] p → ∃ w, admissible w ∧ p w) :
    ∃ w, admissible w ∧
      ∀ context p, Derives basis context p → Holds context w → p w := by
  obtain ⟨w, ha, all⟩ := (pointwise_closure_iff_common basis indices covers admissible).mp each
  exact ⟨w, ha, (basis_iff_relative_closure basis w).mp (fun i => all (basis i) (.base i))⟩

/-- An inference control, not two physical worlds or a proposed foundation. -/
def incompatibleRows (b : Bool) : Formula Bool := fun w => b = w

theorem separate_basis_rows_fit :
    ∀ b, ∃ w, incompatibleRows b w := fun b => ⟨b, rfl⟩

theorem separate_rows_have_no_common_interpretation :
    ¬ ∃ w, ∀ b, incompatibleRows b w := by
  rintro ⟨w, h⟩
  exact Bool.noConfusion ((h false).trans (h true).symm)

theorem separate_rows_do_not_cover_full_closure :
    ¬ (∀ p, Derives incompatibleRows [] p → ∃ w, True ∧ p w) := by
  intro each
  have covers : ∀ b : Bool, b ∈ [false, true] := by
    intro b
    cases b with
    | false => exact List.mem_cons_self
    | true => exact List.mem_cons_of_mem false List.mem_cons_self
  obtain ⟨w, _, all⟩ :=
    (pointwise_closure_iff_common incompatibleRows [false, true] covers (fun _ => True)).mp each
  exact separate_rows_have_no_common_interpretation ⟨w, fun b => all _ (.base b)⟩

#print axioms package
#print axioms package_derivable
#print axioms package_iff_list
#print axioms package_iff_basis
#print axioms basis_iff_relative_closure
#print axioms common_basis_iff_common_closure
#print axioms pointwise_closure_iff_common
#print axioms pointwise_closure_gives_common_relative
#print axioms incompatibleRows
#print axioms separate_basis_rows_fit
#print axioms separate_rows_have_no_common_interpretation
#print axioms separate_rows_do_not_cover_full_closure

end InquiryRoot.JointInterpretation
