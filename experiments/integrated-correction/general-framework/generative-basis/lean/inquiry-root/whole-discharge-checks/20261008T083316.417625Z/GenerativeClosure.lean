import Std

/-!
Necessity propagates through every finite, premise-tracked derivation.
The inquiry predicate and the necessity of the basis are supplied hypotheses.
The rules below do not erase local premises. No empirical or ethical sentence
is installed by a definition of inquiry or of the generative foundation.
-/

namespace InquiryRoot

universe u v

abbrev Formula (World : Type u) := World → Prop

def Holds {World : Type u} (context : List (Formula World)) (w : World) : Prop :=
  ∀ p, p ∈ context → p w

def Necessary {World : Type u} (inquiry p : Formula World) : Prop :=
  ∀ w, inquiry w → p w

/-- Finite proof trees. Basis formulas and local assumptions remain different
    constructors. Implication introduction discharges one named assumption. -/
inductive Derives {World : Type u} {Index : Type v}
    (basis : Index → Formula World) : List (Formula World) → Formula World → Prop where
  | base {context : List (Formula World)} (i : Index) : Derives basis context (basis i)
  | assumption {context : List (Formula World)} {p : Formula World} :
      p ∈ context → Derives basis context p
  | impIntro {context : List (Formula World)} {p q : Formula World} :
      Derives basis (p :: context) q →
      Derives basis context (fun w => p w → q w)
  | impElim {context : List (Formula World)} {p q : Formula World} :
      Derives basis context (fun w => p w → q w) →
      Derives basis context p → Derives basis context q
  | andIntro {context : List (Formula World)} {p q : Formula World} :
      Derives basis context p → Derives basis context q →
      Derives basis context (fun w => p w ∧ q w)
  | andLeft {context : List (Formula World)} {p q : Formula World} :
      Derives basis context (fun w => p w ∧ q w) →
      Derives basis context p
  | andRight {context : List (Formula World)} {p q : Formula World} :
      Derives basis context (fun w => p w ∧ q w) →
      Derives basis context q
  | allNatElim {context : List (Formula World)} {p : Nat → Formula World}
      (n : Nat) : Derives basis context (fun w => ∀ k, p k w) →
      Derives basis context (p n)

theorem derivation_sound {World : Type u} {Index : Type v}
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
    cases List.mem_cons.mp hr with
    | inl heq => exact heq ▸ hp
    | inr ht => exact hc r ht
  | impElim _ _ ihf ihp => exact fun w hb hc => ihf w hb hc (ihp w hb hc)
  | andIntro _ _ ihp ihq => exact fun w hb hc => ⟨ihp w hb hc, ihq w hb hc⟩
  | andLeft _ ih => exact fun w hb hc => (ih w hb hc).1
  | andRight _ ih => exact fun w hb hc => (ih w hb hc).2
  | allNatElim n _ ih => exact fun w hb hc => ih w hb hc n

theorem all_closed_descendants_necessary {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry : Formula World}
    (rootNecessary : ∀ i, Necessary inquiry (basis i)) :
    ∀ p, Derives basis [] p → Necessary inquiry p := by
  intro p proof w hi
  apply derivation_sound proof w (fun i => rootNecessary i w hi)
  intro q hq
  exact False.elim (List.not_mem_nil hq)

theorem all_relative_descendants_necessary {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry : Formula World}
    (rootNecessary : ∀ i, Necessary inquiry (basis i))
    {context : List (Formula World)} {p : Formula World}
    (proof : Derives basis context p) :
    Necessary inquiry (fun w => Holds context w → p w) := by
  intro w hi hc
  exact derivation_sound proof w (fun i => rootNecessary i w hi) hc

/-- A whole possibly infinite generated theory is necessary exactly when its
    starting basis is necessary. The reverse direction prevents certification
    of an unsupported basis by appealing to its productive closure. -/
theorem entire_closure_necessary_iff_basis {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry : Formula World} :
    (∀ p, Derives basis [] p → Necessary inquiry p) ↔
    (∀ i, Necessary inquiry (basis i)) := by
  constructor
  · intro allNecessary i
    exact allNecessary (basis i) (.base i)
  · exact all_closed_descendants_necessary

theorem local_justification_discharges_context {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry : Formula World}
    (rootNecessary : ∀ i, Necessary inquiry (basis i))
    {context : List (Formula World)} {p : Formula World}
    (localNecessary : ∀ q, q ∈ context → Necessary inquiry q)
    (proof : Derives basis context p) : Necessary inquiry p := by
  intro w hi
  exact derivation_sound proof w (fun i => rootNecessary i w hi)
    (fun q hq => localNecessary q hq w hi)

theorem no_counterexample_to_closed_descendant {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry p : Formula World}
    (rootNecessary : ∀ i, Necessary inquiry (basis i))
    (proof : Derives basis [] p) : ¬ ∃ w, inquiry w ∧ ¬ p w := by
  rintro ⟨w, hi, hn⟩
  exact hn (all_closed_descendants_necessary rootNecessary p proof w hi)

/-- An actual countermodel rules out membership in the closed generated theory;
    disagreement cannot be rescued by producing a longer valid derivation. -/
theorem countermodel_excludes_derivation {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry p : Formula World}
    (rootNecessary : ∀ i, Necessary inquiry (basis i))
    (countermodel : ∃ w, inquiry w ∧ ¬ p w) : ¬ Derives basis [] p := by
  intro proof
  exact no_counterexample_to_closed_descendant rootNecessary proof countermodel

def addDerived {World : Type u} {Index : Type v}
    (basis : Index → Formula World) (lemma : Formula World) : Option Index → Formula World
  | none => lemma
  | some i => basis i

/-- A proved descendant can become a reusable rule premise without losing the
    necessity guarantee for the whole subsequently generated theory. -/
theorem derived_lemma_extension_preserves_necessity {World : Type u} {Index : Type v}
    {basis : Index → Formula World} {inquiry lemma : Formula World}
    (rootNecessary : ∀ i, Necessary inquiry (basis i))
    (lemmaProof : Derives basis [] lemma) :
    ∀ p, Derives (addDerived basis lemma) [] p → Necessary inquiry p := by
  apply all_closed_descendants_necessary
  intro i
  cases i with
  | none => exact all_closed_descendants_necessary rootNecessary lemma lemmaProof
  | some i => exact rootNecessary i

def weakBasis : Unit → Formula Bool := fun _ _ => True
def unrestrictedInquiry : Formula Bool := fun _ => True
def extraClaim : Formula Bool := fun w => w = true

theorem extra_claim_derives_with_one_local_premise :
    Derives weakBasis [extraClaim] extraClaim :=
  .assumption (List.mem_cons_self)

theorem extra_claim_not_necessary : ¬ Necessary unrestrictedInquiry extraClaim := by
  intro hn
  have h := hn false True.intro
  cases h

theorem extra_claim_not_closed_derivable : ¬ Derives weakBasis [] extraClaim := by
  apply countermodel_excludes_derivation (fun _ _ _ => True.intro)
    (inquiry := unrestrictedInquiry)
  exact ⟨false, True.intro, Bool.false_ne_true⟩

theorem one_local_premise_becomes_an_implication :
    Derives weakBasis [] (fun w => extraClaim w → extraClaim w) :=
  .impIntro extra_claim_derives_with_one_local_premise

#print axioms InquiryRoot.derivation_sound
#print axioms InquiryRoot.all_closed_descendants_necessary
#print axioms InquiryRoot.all_relative_descendants_necessary
#print axioms InquiryRoot.entire_closure_necessary_iff_basis
#print axioms InquiryRoot.local_justification_discharges_context
#print axioms InquiryRoot.no_counterexample_to_closed_descendant
#print axioms InquiryRoot.countermodel_excludes_derivation
#print axioms InquiryRoot.derived_lemma_extension_preserves_necessity
#print axioms InquiryRoot.extra_claim_derives_with_one_local_premise
#print axioms InquiryRoot.extra_claim_not_necessary
#print axioms InquiryRoot.extra_claim_not_closed_derivable
#print axioms InquiryRoot.one_local_premise_becomes_an_implication

end InquiryRoot
