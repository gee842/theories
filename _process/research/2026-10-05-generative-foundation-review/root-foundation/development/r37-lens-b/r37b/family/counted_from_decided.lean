import Becoming.CensusBinding
namespace Becoming.World
open Becoming

theorem t1 (S : Premise → Bool) :
    (∀ w : World, w.Meets S → w.CountsHold fun n _ a => ∀ t, 0 < a t → 0 < n t) ↔
      BindsCounting S :=
  ((counting_under_counted S).symm.trans (counting_under S fun same law t pos =>
    Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2.symm)))
      (Nat.le_of_eq (same t).1))).trans (counting_binds_iff S)

theorem t2 (S : Premise → Bool) (uncounted : S .counted = false) :
    type_of% (finite_binding_joint_iff_counted S uncounted) :=
  ((finite_binding_counting_under_counted S uncounted).symm.trans
    (finite_binding_counting_under S uncounted fun same ⟨t, n, a⟩ =>
      ⟨t, Nat.lt_of_lt_of_le n (Nat.le_of_eq (same t).1),
        Nat.lt_of_lt_of_le a (Nat.le_of_eq (same t).2.2)⟩)).trans
    (finite_binding_joint_iff S uncounted)

theorem t3 (S : Premise → Bool) :
    type_of% (enclosed_binding_activity_iff_counted S) :=
  ((enclosed_binding_counting_under_counted S).symm.trans
    (enclosed_binding_counting_under S fun same ⟨t, pos⟩ =>
      ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).1)⟩)).trans
    (enclosed_binding_activity_iff S)

#print axioms t1
#print axioms t2
#print axioms t3
end Becoming.World
