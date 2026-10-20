import Becoming.Inquiry

/-!
# Classified beliefs after observation on a process

`InquirySufficiency` narrows a belief about a process's configuration by an action and its
observation (`After`), and recovers the usual implication form of bounded sufficient inquiry
where every narrowed belief is classified as empty or inhabited to the declared depth
(`ClassifiedThrough`, `sufficiency_iff_implication_form`). It shows that a decided belief is
empty or inhabited (`empty_or_inhabited_of_decidable`). This module states that law of the
beliefs a process's steps and observations produce.

* **A decided narrowed belief is classified**: after an action and an observation of the
  process, a belief whose inhabitation is decided is empty or inhabited
  (`after_empty_or_inhabited`).
* **Decided narrowing classifies at every depth**: where the inhabitation of every belief
  narrowed by the process is decided, every belief is classified through every depth
  (`classified_of_decidable`), so bounded sufficiency is the implication form there
  (`sufficiency_iff_implication_of_decidable`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace ClassifiedBeliefProcesses

open Generative Generative.InquirySufficiency

universe u v w

variable {S : Type u} {A : Type v} {k : Nat} {P : Process S A} {sense : S → A → S → Fin k}

/-- **A narrowed belief whose inhabitation is decided is empty or inhabited.** -/
theorem after_empty_or_inhabited {B : S → Prop} {a : A} {o : Fin k}
    (decision : Decidable (InhabitedBelief (After P sense B a o))) :
    EmptyBelief (After P sense B a o) ∨ InhabitedBelief (After P sense B a o) :=
  empty_or_inhabited_of_decidable decision

/-- **Where the inhabitation of every narrowed belief is decided, every belief is classified
through every depth.** -/
theorem classified_of_decidable
    (decision : ∀ B a o, Decidable (InhabitedBelief (After P sense B a o))) :
    ∀ n B, ClassifiedThrough P sense n B
  | 0, _ => trivial
  | n + 1, B => fun a o =>
    ⟨after_empty_or_inhabited (decision B a o), classified_of_decidable decision n _⟩

/-- **Bounded sufficiency is the implication form where narrowing is decided.** -/
theorem sufficiency_iff_implication_of_decidable {R : Type w}
    {safe : S → A → S → Prop} {goal : S → Prop} {response : R → List A}
    (decision : ∀ B a o, Decidable (InhabitedBelief (After P sense B a o))) (n : Nat)
    (B : S → Prop) :
    Sufficient P safe goal sense response n B ↔ ImplicationSufficient P safe goal sense response n B :=
  sufficiency_iff_implication_form n B (classified_of_decidable decision n B)

end ClassifiedBeliefProcesses

end Becoming
