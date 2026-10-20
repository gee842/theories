import Becoming.CensusBinding
namespace Becoming.World
open Becoming
theorem famTest (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
      (∀ p, S p = true → p.Binds w) → w.CountsObey fun n _ _ => ∃ t, 0 < n t) ↔
      S .dependent = true ∨ S .acting = true ∨ S .taking = true ∨ S .embodied = true :=
  ((binding_counting_under S fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).1)⟩).symm.trans
    (binding_counting_under_counted S)).trans (binding_activity_iff_counted S)
#print axioms famTest
end Becoming.World
