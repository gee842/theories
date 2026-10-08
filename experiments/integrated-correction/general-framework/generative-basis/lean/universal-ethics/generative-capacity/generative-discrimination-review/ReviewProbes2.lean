import RenewingFormation
open RenewingFormation

/-! Probe 8: a continuation that DOES wear the renewing organization (once) and then
continues within the reduced rate is ceaseless. "Formation that wears the renewing
organization ... ceases" (README) is broader than BeyondRenewal. -/
def surgeThenSettle : Nat → Nat := fun n => if n = 0 then 3 else 1

theorem settle_path : ∀ n, (path unitWear ⟨0, 2⟩ surgeThenSettle (n + 1)).renew = 1 := by
  intro n
  induction n with
  | zero => decide
  | succ k ih =>
    show unitWear.degrade (path unitWear ⟨0, 2⟩ surgeThenSettle (k + 1)).renew
      (surgeThenSettle (k + 1)) = 1
    rw [ih]
    show (if (if k + 1 = 0 then 3 else 1) ≤ 1 then 1 else 1 - 1) = 1
    simp

theorem wears_yet_ceaseless :
    (path unitWear ⟨0, 2⟩ surgeThenSettle 1).renew < 2 ∧
    Ceaseless unitWear ⟨0, 2⟩ surgeThenSettle := by
  refine ⟨by decide, ?_⟩
  intro n
  cases n with
  | zero => decide
  | succ k =>
    show 0 < min (surgeThenSettle (k + 1))
      ((path unitWear ⟨0, 2⟩ surgeThenSettle (k + 1)).stock +
        (path unitWear ⟨0, 2⟩ surgeThenSettle (k + 1)).renew)
    rw [settle_path k]
    show 0 < min 1 (_ + 1)
    omega
