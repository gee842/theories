import Std

/-!
# Mutual constraints, implicit meaning and factual warrant

A small mutually constrained interpretation can have a unique truth profile
without a separately supplied atomic truth assignment. This is positive credit
for whole-account determination. The constraints and the ambient logic remain
specified, so this does not establish an assumption-free ontology.

The second result identifies a precise conservativity boundary: when every old
case admits an extension satisfying new constraints, those constraints establish
an old-language claim uniformly exactly when it already held on every old case.
Uniqueness is not needed for that result. This is not a rejection of causal or
philosophical reciprocal grounding, and it does not treat the formal case range
as the actual universe without a correspondence argument.
-/

namespace Generative.MutualGrounding

def Coupled (P Q : Prop) : Prop := (P ↔ ¬ Q) ∧ (Q ↔ (P ∧ Q))

theorem coupled_determines {P Q : Prop} (h : Coupled P Q) : P ∧ ¬ Q := by
  have nq : ¬ Q := by
    intro q
    have p := (h.2.mp q).1
    exact h.1.mp p q
  exact ⟨h.1.mpr nq, nq⟩

theorem coupled_from_profile {P Q : Prop} (h : P ∧ ¬ Q) : Coupled P Q := by
  constructor
  · exact ⟨fun _ => h.2, fun _ => h.1⟩
  · exact ⟨fun q => ⟨h.1, q⟩, fun pq => pq.2⟩

theorem coupled_iff_profile (P Q : Prop) : Coupled P Q ↔ P ∧ ¬ Q :=
  ⟨coupled_determines, coupled_from_profile⟩

theorem coupled_realized : Coupled True False :=
  coupled_from_profile ⟨True.intro, fun f => f⟩

/-- Pointwise equivalence of truth profiles avoids an unnecessary appeal to
propositional extensionality. It is not identity of physical realizations. -/
theorem coupled_profile_unique {P Q P' Q' : Prop}
    (h : Coupled P Q) (h' : Coupled P' Q') : (P ↔ P') ∧ (Q ↔ Q') := by
  obtain ⟨p, nq⟩ := coupled_determines h
  obtain ⟨p', nq'⟩ := coupled_determines h'
  exact ⟨⟨fun _ => p', fun _ => p⟩,
    ⟨fun q => False.elim (nq q), fun q' => False.elim (nq' q')⟩⟩

universe u v

/-- Adding solvable implicit constraints for new descriptions does not alone
restrict old cases. The total-extension premise is exposed, not assumed away. -/
theorem total_extension_conservative {Old : Type u} {New : Type v}
    (constraint : Old → New → Prop)
    (extension : ∀ old, ∃ new, constraint old new) (claim : Old → Prop) :
    (∀ old new, constraint old new → claim old) ↔ ∀ old, claim old := by
  constructor
  · intro all old
    obtain ⟨new, h⟩ := extension old
    exact all old new h
  · intro all old _ _
    exact all old

/-- A case-dependent uniquely specified Boolean addition is still compatible
with every old case. This instance is inhabited without an existence postulate. -/
theorem canonical_extension_total {Old : Type u} (meaning : Old → Bool) :
    ∀ old, ∃ new, new = meaning old :=
  fun old => ⟨meaning old, rfl⟩

theorem canonical_extension_unique {Old : Type u} (meaning : Old → Bool)
    (old : Old) {x y : Bool} (hx : x = meaning old) (hy : y = meaning old) :
    x = y := hx.trans hy.symm

/-- Even uniquely fixed added meanings leave actual old-world claims to their
own grounds. No implication from uniqueness alone to actuality is installed. -/
theorem canonical_extension_conservative {Old : Type u}
    (meaning : Old → Bool) (claim : Old → Prop) :
    (∀ old new, new = meaning old → claim old) ↔ ∀ old, claim old :=
  total_extension_conservative (fun old new => new = meaning old)
    (canonical_extension_total meaning) claim

end Generative.MutualGrounding

#print axioms Generative.MutualGrounding.coupled_determines
#print axioms Generative.MutualGrounding.coupled_from_profile
#print axioms Generative.MutualGrounding.coupled_iff_profile
#print axioms Generative.MutualGrounding.coupled_realized
#print axioms Generative.MutualGrounding.coupled_profile_unique
#print axioms Generative.MutualGrounding.total_extension_conservative
#print axioms Generative.MutualGrounding.canonical_extension_total
#print axioms Generative.MutualGrounding.canonical_extension_unique
#print axioms Generative.MutualGrounding.canonical_extension_conservative
