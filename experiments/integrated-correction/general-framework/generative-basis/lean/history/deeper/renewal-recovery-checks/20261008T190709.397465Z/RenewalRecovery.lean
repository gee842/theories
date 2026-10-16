import Std
import RelationalRenewal

/-!
Recovery within the existing support-gated renewal law. One activity sustains
a shared condition while supported; another can draw or contribute while its
own support remains. These are roles within the same unfolding. The inherited
law supplies amounts, thresholds and the contribution schedule; no source of
those inputs or ethical direction is inferred here.

The delta is a bounded recovery window, its bootstrap obstruction, and actual
input histories crossing opposite sides of that boundary. Earlier material
repair, recovery-basin and renewal results retain their independent credit.
-/
namespace RenewalRecovery

open RelationalRenewal RelationalRenewal.Law

/-- If both activities lose their support, later nominal contribution inputs
are inactive. The inherited law has no third route able to inject support. -/
theorem inactive_pair_absorbs (L : Law) (T : Nat)
    (fOff : L.level T < L.needF) (gOff : L.level T < L.needG) :
    ∀ n, L.level (T + n) = L.level T := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
      rw [Nat.add_succ, L.level_succ, ih,
        if_neg (Nat.not_le.mpr gOff), if_neg (Nat.not_le.mpr fOff)]

/-- Supported positive net repair raises the condition even if its ordinary
sustaining activity is presently inactive. -/
theorem supported_repair_step (L : Law) (t : Nat)
    (fOn : L.needF ≤ L.level t) (surplus : L.draw t < L.contrib t) :
    L.level t + 1 ≤ L.level (t + 1) := by
  rw [L.level_succ]
  split <;> rw [if_pos fOn] <;> omega

/-- Only the stated finite window needs positive net repair. Support for the
repairing activity persists because the reached level never falls in that window. -/
theorem repair_window_progress (L : Law) (T N : Nat)
    (fOn : L.needF ≤ L.level T)
    (surplus : ∀ d, d < N → L.draw (T + d) < L.contrib (T + d)) :
    ∀ d, d ≤ N → L.level T + d ≤ L.level (T + d) := by
  intro d
  induction d with
  | zero => intro _; exact Nat.le_refl _
  | succ d ih =>
      intro bound
      have prior := ih (show d ≤ N by omega)
      have active : L.needF ≤ L.level (T + d) := by omega
      have step := supported_repair_step L (T + d) active (surplus d (by omega))
      rw [Nat.add_succ]
      omega

/-- Recovery by the deficit bound, given an active repair route and its actual
net contribution throughout that many subsequent steps. -/
theorem repair_restores_sustaining_support (L : Law) (T : Nat)
    (fOn : L.needF ≤ L.level T)
    (surplus : ∀ d, d < L.needG - L.level T →
      L.draw (T + d) < L.contrib (T + d)) :
    L.needG ≤ L.level (T + (L.needG - L.level T)) := by
  have progress := repair_window_progress L T (L.needG - L.level T)
    fOn surplus (L.needG - L.level T) (Nat.le_refl _)
  omega

/-- Both histories start at level 2. Only the first draw differs; the same
later contribution of one unit is gated by actual support in each history. -/
def pulse (firstDraw : Nat) : Law :=
  ⟨2, 1, 2, 1, (fun t => if t = 0 then firstDraw else 0),
    (fun t => if t = 0 then 0 else 1)⟩

theorem same_future_inputs (n : Nat) :
    (pulse 2).draw (n + 1) = (pulse 3).draw (n + 1) ∧
    (pulse 2).contrib (n + 1) = (pulse 3).contrib (n + 1) := by
  simp [pulse]

theorem two_actual_pulses :
    (pulse 2).level 0 = 2 ∧ (pulse 3).level 0 = 2 ∧
    (pulse 2).level 1 = 1 ∧ (pulse 3).level 1 = 0 ∧
    (pulse 2).level 2 = 2 := by decide

theorem supported_pulse_recovers (n : Nat) :
    2 ≤ (pulse 2).level (2 + n) := by
  have grow := repair_window_progress (pulse 2) 1 (n + 1)
    (by decide : (pulse 2).needF ≤ (pulse 2).level 1)
    (by intro d _; simp [pulse]) (n + 1) (Nat.le_refl _)
  have reached : (pulse 2).level 1 = 1 := by decide
  rw [reached] at grow
  have same : 1 + (n + 1) = 2 + n := by omega
  rw [same] at grow
  omega

theorem unsupported_pulse_never_recovers (n : Nat) :
    (pulse 3).level (1 + n) = 0 :=
  inactive_pair_absorbs (pulse 3) 1 (by decide) (by decide) n

/-- A temporary loss followed by permanent restoration is neither class in
the inherited all-time / permanent-loss classification. This does not alter
the classification; it states its scope when explaining change over time. -/
theorem recovered_history_neither_global_class :
    ¬ RenewingIn (pulse 2).unfolding .focal ∧
    ¬ ConsumingIn (pulse 2).unfolding .focal := by
  constructor
  · intro renewing
    have bad := renewing () (Or.inl (by decide)) 1 .sustaining trivial
    have : (2 : Nat) ≤ 1 := bad
    omega
  · rintro ⟨c, _, g, T, _, lost⟩
    cases c
    have low := lost (2 + T) (by omega)
    have high := supported_pulse_recovers T
    cases g <;> change (pulse 2).level (2 + T) < _ at low <;>
      simp only [Law.unfolding, Law.need, pulse] at low <;> omega

end RenewalRecovery
