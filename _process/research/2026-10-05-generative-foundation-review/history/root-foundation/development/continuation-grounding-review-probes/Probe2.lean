import Becoming.Standpoints

namespace Becoming
namespace Review

/-! ## R10. S0 ranges over *living* claims only. The keeper is active at step 1 and its
event there is its own, but that event is not living (it undermines), so S0 says nothing
about it: the `living` filter (the weak form's "not harm") sits inside the seed. -/
theorem keeper_active_not_living :
    Totalizer.web.active 1 .keeper ∧ Totalizer.own .keeper (.keeper, 1) ∧
      ¬ Totalizer.valuation.living (.keeper, 1) :=
  ⟨trivial, rfl, fun ⟨_, notUndermining⟩ =>
    notUndermining (match Totalizer.careful with
      | ⟨_, _, _, _, _, _, _, _, undermining, _⟩ => undermining)⟩

end Review
end Becoming

#print axioms Becoming.Review.keeper_active_not_living
