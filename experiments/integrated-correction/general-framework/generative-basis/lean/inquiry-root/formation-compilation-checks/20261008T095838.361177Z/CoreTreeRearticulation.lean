import GenerativeClosure

/-!
# Core and generated branches as rearticulations of one derivational practice

The existing Derives calculus distinguishes a chosen reusable basis from local
assumptions and generated proof branches. This module shows that the basis can
be replaced by all its closed derived branches without changing any derivable
conclusion, even in arbitrary local contexts. Reused branches are expanded into
their original derivations; they do not become an independently justified layer.

This is a conservative proof-level result within the existing rules. It does
not identify deduction with all generative activity, prove nondual ontology,
derive the rules or physical occurrence, or perform empirical theory revision.
Two equivalent presentations need not have equal types, proof sizes or costs.
The final criterion preserves the difference between rearticulation and adding
a genuinely new premise. A locally assumed conclusion cannot be promoted to a
closed basis merely by calling it a branch of the tree.
-/

namespace InquiryRoot.CoreTree

universe u v w

variable {World : Type u} {Index : Type v} {OtherIndex : Type w}

/-- A derivation remains usable in a larger local context. The context is
transported through implication introduction without discarding its premises. -/
theorem context_weaken {basis : Index → Formula World}
    {context larger : List (Formula World)} {p : Formula World}
    (proof : Derives basis context p)
    (hincludes : ∀ q, q ∈ context → q ∈ larger) : Derives basis larger p := by
  induction proof generalizing larger with
  | base i => exact .base i
  | assumption hm => exact .assumption (hincludes _ hm)
  | impIntro _ ih =>
    apply Derives.impIntro
    apply ih
    intro q hq
    cases hq with
    | head => exact .head _
    | tail _ htail => exact .tail _ (hincludes q htail)
  | impElim _ _ ihf ihp => exact .impElim (ihf hincludes) (ihp hincludes)
  | andIntro _ _ ihp ihq => exact .andIntro (ihp hincludes) (ihq hincludes)
  | andLeft _ ih => exact .andLeft (ih hincludes)
  | andRight _ ih => exact .andRight (ih hincludes)
  | allNatElim n _ ih => exact .allNatElim n (ih hincludes)

/-- Expand each reusable basis occurrence into an existing closed derivation.
Local assumptions remain local throughout the expansion. -/
theorem substitute_derived_basis
    {basis : Index → Formula World} {replacement : OtherIndex → Formula World}
    (hderived : ∀ i, Derives replacement [] (basis i))
    {context : List (Formula World)} {p : Formula World}
    (proof : Derives basis context p) : Derives replacement context p := by
  induction proof with
  | base i =>
    exact context_weaken (hderived i) (fun _ hnil => by cases hnil)
  | assumption hm => exact .assumption hm
  | impIntro _ ih => exact .impIntro ih
  | impElim _ _ ihf ihp => exact .impElim ihf ihp
  | andIntro _ _ ihp ihq => exact .andIntro ihp ihq
  | andLeft _ ih => exact .andLeft ih
  | andRight _ ih => exact .andRight ih
  | allNatElim n _ ih => exact .allNatElim n ih

/-- Mutual generation, rather than equality of presentation or a privileged
list of root names, characterizes the same contextual derivational content. -/
theorem same_derivations_iff_mutual_generation
    (basis : Index → Formula World) (replacement : OtherIndex → Formula World) :
    (∀ context p, Derives basis context p ↔ Derives replacement context p) ↔
      (∀ i, Derives replacement [] (basis i)) ∧
      (∀ j, Derives basis [] (replacement j)) := by
  constructor
  · intro hequivalent
    exact ⟨fun i => (hequivalent [] (basis i)).mp (.base i),
      fun j => (hequivalent [] (replacement j)).mpr (.base j)⟩
  · rintro ⟨hforward, hbackward⟩ context p
    exact ⟨substitute_derived_basis hforward, substitute_derived_basis hbackward⟩

/-- Each index retains the existing proof of its branch; no independent truth
or necessity premise is attached when that branch is reused. -/
def DerivedBranch (basis : Index → Formula World) :=
  {p : Formula World // Derives basis [] p}

def branchBasis (basis : Index → Formula World) : DerivedBranch basis → Formula World :=
  fun branch => branch.val

/-- The complete generated tree can serve as the reusable core articulation
without enlarging its conclusions, including conclusions with local premises.
This exact content identity does not assert equality of proof histories. -/
theorem whole_tree_rearticulation (basis : Index → Formula World)
    (context : List (Formula World)) (p : Formula World) :
    Derives (branchBasis basis) context p ↔ Derives basis context p := by
  constructor
  · exact substitute_derived_basis (fun branch => branch.property)
  · exact substitute_derived_basis (basis := basis) (replacement := branchBasis basis)
      (fun i => Derives.base (basis := branchBasis basis)
        (⟨basis i, .base i⟩ : DerivedBranch basis))

/-- Calling an arbitrary claim a reusable branch is conservative exactly when
the existing practice already derives it without additional local assumptions.
An unsupported addition changes the theory; renaming cannot hide that change. -/
theorem added_branch_conservative_iff (basis : Index → Formula World)
    (branch : Formula World) :
    (∀ context p, Derives (addDerived basis branch) context p ↔ Derives basis context p) ↔
      Derives basis [] branch := by
  constructor
  · intro hconservative
    exact (hconservative [] branch).mp (.base none)
  · intro hbranch context p
    constructor
    · apply substitute_derived_basis
      intro i
      cases i with
      | none => exact hbranch
      | some j => exact .base j
    · exact substitute_derived_basis (basis := basis) (replacement := addDerived basis branch)
        (fun i => Derives.base (some i))

end InquiryRoot.CoreTree

#print axioms InquiryRoot.CoreTree.context_weaken
#print axioms InquiryRoot.CoreTree.substitute_derived_basis
#print axioms InquiryRoot.CoreTree.same_derivations_iff_mutual_generation
#print axioms InquiryRoot.CoreTree.whole_tree_rearticulation
#print axioms InquiryRoot.CoreTree.added_branch_conservative_iff
