import Becoming.Testing

/-! Probe G: the two arithmetic witnesses, and whether core already has these names. -/

namespace Becoming.Review47

theorem one_ne_two' : (1 : Nat) ≠ 2 := fun same => nomatch same
theorem two_ne_three' : (2 : Nat) ≠ 3 := fun same => nomatch same
theorem one_ne_two'' : (1 : Nat) ≠ 2 := by decide

end Becoming.Review47

#print axioms Becoming.Review47.one_ne_two'
#print axioms Becoming.Review47.two_ne_three'
#print axioms Becoming.Review47.one_ne_two''
-- Do core names already exist?
#check @Nat.succ_ne_self
#check @Nat.one_ne_two
#check @one_ne_two
#check @Becoming.one_ne_two
