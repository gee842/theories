import RelationalRenewal
open RelationalRenewal RelationalRenewal.Law
example : ¬ RenewingIn fluctuating () ∧ ¬ ConsumingIn fluctuating () := fluctuating_neither
example : ¬ ConsumingIn cultivation.unfolding .focal :=
  renewing_not_consuming formation_does_not_decide.2.1.1
example : ¬ RenewingIn winning.unfolding .focal := fun renewing =>
  renewing_not_consuming renewing own_trajectory_does_not_decide.2.2.2
example : ∀ t, winning.formed t = t :=
  (independent_overdraw_persists winning rfl (Nat.succ_pos 0) (T0 := 0)
    (fun _ _ => Nat.lt_succ_self 1)).2.1
