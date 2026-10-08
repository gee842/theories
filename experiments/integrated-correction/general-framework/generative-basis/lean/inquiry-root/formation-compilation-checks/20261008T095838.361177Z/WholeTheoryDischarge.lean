import CoreTreeRearticulation

/-!
# Discharging the reusable basis through a developed proof family

The existing core/tree calculus is unchanged. Each candidate root is derived
using only roots lower in a supplied well-founded proof-dependency relation.
Substitution recursively constructs a derivation over the EMPTY basis. No
semantic truth or necessity of the roots is supplied as a hypothesis.

This is proof-level discharge, not a generative ontology. Well-foundedness
concerns instantiated proof obligations, not time, physical causation or a
mandatory ordering of the parts of reality. It is a sufficient proof procedure,
not a completeness theorem for all cyclic or holistic justifications. Its
local proof terms and the well-foundedness proof must actually be supplied.
-/

namespace InquiryRoot.WholeDischarge

universe u v

def emptyBasis (World : Type u) : Empty → Formula World := Empty.elim

def lowerBasis {World : Type u} {Index : Type v}
    (basis : Index → Formula World) (before : Index → Index → Prop)
    (i : Index) : {j : Index // before j i} → Formula World :=
  fun j => basis j.val

/-- Same soundness proposition as the inherited calculus, proved by direct
membership cases to avoid its extensionality-bearing library lemma. -/
theorem derivation_sound_constructively {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {context : List (Formula World)}
    {p : Formula World} (proof : Derives basis context p) :
    ∀ w, (∀ i, basis i w) → Holds context w → p w := by
  induction proof with
  | base i => exact fun _ hb _ => hb i
  | assumption hm => exact fun _ _ hc => hc _ hm
  | impIntro _ ih =>
    intro w hb hc hp
    apply ih w hb
    intro r hr
    cases hr with
    | head => exact hp
    | tail _ ht => exact hc r ht
  | impElim _ _ ihf ihp => exact fun w hb hc => ihf w hb hc (ihp w hb hc)
  | andIntro _ _ ihp ihq => exact fun w hb hc => ⟨ihp w hb hc, ihq w hb hc⟩
  | andLeft _ ih => exact fun w hb hc => (ih w hb hc).1
  | andRight _ ih => exact fun w hb hc => (ih w hb hc).2
  | allNatElim n _ ih => exact fun w hb hc => ih w hb hc n

/-- Construct closed proofs by expanding local derivations. This removes basis
uses rather than reclassifying them as independently warranted branches. -/
theorem roots_discharged {World : Type u} {Index : Type v}
    (basis : Index → Formula World) (before : Index → Index → Prop)
    (wellFounded : WellFounded before)
    (localProof : ∀ i, Derives (lowerBasis basis before i) [] (basis i)) :
    ∀ i, Derives (emptyBasis World) [] (basis i) := by
  intro i
  apply wellFounded.induction i
  intro current smaller
  apply CoreTree.substitute_derived_basis
    (basis := lowerBasis basis before current)
    (replacement := emptyBasis World) _ (localProof current)
  intro prior
  exact smaller prior.val prior.property

/-- Every old derivation can now be expanded over the empty basis. Local
context assumptions remain local and are not discarded by this operation. -/
theorem whole_derivation_discharged {World : Type u} {Index : Type v}
    (basis : Index → Formula World) (before : Index → Index → Prop)
    (wellFounded : WellFounded before)
    (localProof : ∀ i, Derives (lowerBasis basis before i) [] (basis i))
    {context : List (Formula World)} {p : Formula World}
    (proof : Derives basis context p) :
    Derives (emptyBasis World) context p :=
  CoreTree.substitute_derived_basis
    (roots_discharged basis before wellFounded localProof) proof

/-- Closed descendants are valid at every supplied interpretation without a
root-truth hypothesis. The calculus, interpretation and proof certificates
remain explicit; no actual-world correspondence is inferred here. -/
theorem closed_whole_valid {World : Type u} {Index : Type v}
    (basis : Index → Formula World) (before : Index → Index → Prop)
    (wellFounded : WellFounded before)
    (localProof : ∀ i, Derives (lowerBasis basis before i) [] (basis i))
    {p : Formula World} (proof : Derives basis [] p) : ∀ w, p w := by
  intro w
  apply derivation_sound_constructively
    (whole_derivation_discharged basis before wellFounded localProof proof) w
  · intro empty
    exact Empty.elim empty
  · intro q absent
    cases absent

/-- A root's derivability from itself is not a uniform discharge certificate.
This tests that specific inference policy, not all mutually grounded theories. -/
theorem self_use_is_not_uniform_discharge :
    ¬ (∀ p : Formula Unit,
      Derives (fun (_ : Unit) => p) [] p →
      Derives (emptyBasis Unit) [] p) := by
  intro discharge
  have impossible := discharge (fun _ => False) (.base ())
  apply derivation_sound_constructively impossible ()
  · intro empty
    exact Empty.elim empty
  · intro q absent
    cases absent

end InquiryRoot.WholeDischarge

#print axioms InquiryRoot.WholeDischarge.emptyBasis
#print axioms InquiryRoot.WholeDischarge.lowerBasis
#print axioms InquiryRoot.WholeDischarge.derivation_sound_constructively
#print axioms InquiryRoot.WholeDischarge.roots_discharged
#print axioms InquiryRoot.WholeDischarge.whole_derivation_discharged
#print axioms InquiryRoot.WholeDischarge.closed_whole_valid
#print axioms InquiryRoot.WholeDischarge.self_use_is_not_uniform_discharge
