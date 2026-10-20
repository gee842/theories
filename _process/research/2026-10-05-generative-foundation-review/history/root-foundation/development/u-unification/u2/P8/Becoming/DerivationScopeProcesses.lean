import Becoming.Inquiry
import GenerativeClosure

/-!
# Derivation over the scope of an inquiry, with local premises

`GenerativeClosure` judges finite, premise-tracked derivations against a supplied inquiry
predicate: a claim derived under local premises holds wherever the inquiry and the premises do,
premises justified over the inquiry are discharged, a derived lemma added to the basis keeps the
closure where the basis is, and a countermodel excludes a claim from the closure.
`Becoming.Bridge` reads the inquiry as the core's `Scope`, the configurations a policy's actual
executions reach from a belief (`derivation_sound_on_scope`, `closure_over_scope_iff_basis`).
This module states the results with local premises and lemmas on that scope.

* **Relative derivation.** A claim derived from a basis holding over the scope under local
  premises holds at every configuration of the scope where the premises do
  (`relative_on_scope`), and over the whole scope where the premises hold over it
  (`discharged_on_scope`).
* **Derived lemmas.** Adding a claim derived with no premise to the basis keeps every claim of
  the enlarged closure holding over the scope (`lemma_extension_on_scope`).
* **Countermodels.** A configuration of the scope where a claim fails excludes the claim from
  the closure of a basis holding over the scope (`countermodel_on_scope`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace DerivationScopeProcesses

open Generative Generative.InquirySufficiency

variable {S A R Index : Type} {k : Nat} {P : Process S A} {sense : S → A → S → Fin k}
  {response : R → List A} {B : S → Prop} {policy : Policy A R k}
  {basis : Index → InquiryRoot.Formula S}

/-- **A claim derived under local premises holds over the scope wherever its premises hold.** -/
theorem relative_on_scope
    (rootHolds : ∀ i, InquiryRoot.Necessary (Scope P sense response B policy) (basis i))
    {context : List (InquiryRoot.Formula S)} {p : InquiryRoot.Formula S}
    (proof : InquiryRoot.Derives basis context p) :
    ∀ t, Scope P sense response B policy t → InquiryRoot.Holds context t → p t :=
  InquiryRoot.all_relative_descendants_necessary rootHolds proof

/-- **Local premises holding over the scope are discharged**: the claim derived under them holds
over the scope. -/
theorem discharged_on_scope
    (rootHolds : ∀ i, InquiryRoot.Necessary (Scope P sense response B policy) (basis i))
    {context : List (InquiryRoot.Formula S)} {p : InquiryRoot.Formula S}
    (premisesHold : ∀ q, q ∈ context → InquiryRoot.Necessary (Scope P sense response B policy) q)
    (proof : InquiryRoot.Derives basis context p) :
    InquiryRoot.Necessary (Scope P sense response B policy) p :=
  InquiryRoot.local_justification_discharges_context rootHolds premisesHold proof

/-- **A derived lemma added to the basis keeps the closure over the scope.** -/
theorem lemma_extension_on_scope
    (rootHolds : ∀ i, InquiryRoot.Necessary (Scope P sense response B policy) (basis i))
    {lemma : InquiryRoot.Formula S} (lemmaProof : InquiryRoot.Derives basis [] lemma) :
    ∀ p, InquiryRoot.Derives (InquiryRoot.addDerived basis lemma) [] p →
      InquiryRoot.Necessary (Scope P sense response B policy) p :=
  InquiryRoot.derived_lemma_extension_preserves_necessity rootHolds lemmaProof

/-- **A configuration of the scope where a claim fails excludes it from the closure** of a basis
holding over the scope. -/
theorem countermodel_on_scope
    (rootHolds : ∀ i, InquiryRoot.Necessary (Scope P sense response B policy) (basis i))
    {p : InquiryRoot.Formula S}
    (countermodel : ∃ t, Scope P sense response B policy t ∧ ¬ p t) :
    ¬ InquiryRoot.Derives basis [] p :=
  InquiryRoot.countermodel_excludes_derivation rootHolds countermodel

end DerivationScopeProcesses

end Becoming
