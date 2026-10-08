import RenewingFormation
import ProtectionPriorityRival
open RenewingFormation GenerativeComparison

/-! Probe 1: BeyondRenewal can be weakened to excess over the *current* rate. -/
def BeyondCurrent (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, (path law c0 demand n).renew < demand n

theorem beyond_initial_implies_current (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (b : BeyondRenewal c0 demand) : BeyondCurrent law c0 demand :=
  fun n => Nat.lt_of_le_of_lt (renewal_never_grows law c0 demand n) (b n)

theorem current_invariant (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondCurrent law c0 demand) :
    ∀ n, cumulative law c0 demand n + budget (path law c0 demand n) ≤ budget c0 := by
  intro n
  induction n with
  | zero => simp [cumulative, path]
  | succ k ih =>
    have := (beyond_step law (path law c0 demand k) (demand k) (beyond k)).1
    show cumulative law c0 demand k + formed law c0 demand k +
      budget (next law (path law c0 demand k) (demand k)) ≤ budget c0
    unfold formed
    omega

-- The weaker hypothesis is strictly weaker: demand 2 after renewal has worn to 1 is
-- beyond the current rate but not beyond the initial rate 2.
example : BeyondCurrent unitWear ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) ∧
    ¬ BeyondRenewal ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) := by
  constructor
  · intro n
    induction n with
    | zero => decide
    | succ k ih =>
      -- renewal is 1 at step 1 and stays ≤ 1 afterwards
      have h : ∀ m, (path unitWear ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) (m + 1)).renew ≤ 1 := by
        intro m
        induction m with
        | zero => decide
        | succ j ihj =>
          show unitWear.degrade _ _ ≤ 1
          have := unitWear.bounded (path unitWear ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) (j + 1)).renew
            ((fun n => if n = 0 then 3 else 2) (j + 1))
          omega
      have := h k
      show _ < (if k + 1 = 0 then 3 else 2)
      simp; omega
  · intro b; have := b 1; simp at this

/-! Probe 2: under the Part B event inventory, C is silent between sustained and surge
(neither is a generative extension of the other), for the control instance. -/
def sustained : Nat → Nat := fun _ => 2
def surge : Nat → Nat := fun _ => 5

example : ¬ GenerativeExtension (eventInventory unitWear ⟨3, 2⟩) sustained surge ∧
    ¬ GenerativeExtension (eventInventory unitWear ⟨3, 2⟩) surge sustained := by
  constructor
  · intro h
    -- event (7,0) realized by sustained but not by surge
    have := h.1 (7, 0) (show 0 < formed unitWear ⟨3, 2⟩ sustained 7 by decide)
    have : ¬ (0 < formed unitWear ⟨3, 2⟩ surge 7) := by decide
    contradiction
  · intro h
    have := h.1 (0, 4) (show 4 < formed unitWear ⟨3, 2⟩ surge 0 by decide)
    have : ¬ (4 < formed unitWear ⟨3, 2⟩ sustained 0) := by decide
    contradiction

/-! Probe 3: under the same event inventory, a continuation that rests one step is a
strict generative sub-history of the sustained one, so C ranks rest strictly lower.
`Ceaseless` likewise classifies rest as not ceaseless. -/
def restOnce : Nat → Nat := fun n => if n = 0 then 0 else 2

example : GenerativeExtension (eventInventory unitWear ⟨3, 2⟩) restOnce sustained := by
  refine ⟨?_, (0, 0), True.intro, (show 0 < formed unitWear ⟨3, 2⟩ sustained 0 by decide),
    (show ¬ (0 < formed unitWear ⟨3, 2⟩ restOnce 0) by decide)⟩
  rintro ⟨n, i⟩ h
  have hw : WithinRenewal ⟨3, 2⟩ sustained := fun _ => ⟨Nat.le_succ 1, Nat.le_refl 2⟩
  show i < formed unitWear ⟨3, 2⟩ sustained n
  rw [(within_renewal_invariant unitWear ⟨3, 2⟩ sustained hw n).2.2]
  -- restOnce never forms more than 2 at any step: renewal stays 2 and demand ≤ 2
  have hf : formed unitWear ⟨3, 2⟩ restOnce n ≤ restOnce n := Nat.min_le_left _ _
  have hr : restOnce n ≤ 2 := by unfold restOnce; split <;> omega
  have : i < formed unitWear ⟨3, 2⟩ restOnce n := h
  show i < 2; omega

example : ¬ Ceaseless unitWear ⟨3, 2⟩ restOnce := by
  intro h; have := h 0; revert this; decide

/-! Probe 4: a capacity reading tolerates rest and separates at step 1, not at the budget. -/
def KeepsCapacity (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, (path law c0 demand n).renew = c0.renew

theorem within_keeps_capacity (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (within : ∀ n, demand n ≤ c0.renew) : KeepsCapacity law c0 demand := by
  intro n
  induction n with
  | zero => rfl
  | succ k ih =>
    show law.degrade (path law c0 demand k).renew (demand k) = c0.renew
    rw [ih]; exact law.keep _ _ (within k)

theorem beyond_loses_capacity_at_once (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (positive : 1 ≤ c0.renew) (beyond : BeyondRenewal c0 demand) :
    (path law c0 demand 1).renew < c0.renew :=
  law.wear c0.renew (demand 0) (beyond 0) positive

/-! Probe 5: sustained comparison generalizes to every within-renewal continuation. -/
theorem every_within_eventually_exceeds_every_beyond (law : WearLaw) (c0 : Conditions)
    (own demand : Nat → Nat) (within : WithinRenewal c0 own) (beyond : BeyondRenewal c0 demand) :
    ∀ n, budget c0 < n → cumulative law c0 demand n < cumulative law c0 own n := by
  intro n late
  have := beyond_renewal_bounded law c0 demand beyond n
  have := within_renewal_grows law c0 own within n
  omega

/-! Probe 6: WearLaw instances where excess wears renewal to zero in one step. -/
def collapse : WearLaw where
  degrade := fun r d => if d ≤ r then r else 0
  keep := by intro r d h; simp [h]
  wear := by intro r d h hr; simp [Nat.not_le.mpr h]; omega
  bounded := by intro r d; by_cases h : d ≤ r <;> simp [h]

/-! Probe 7: G0 places no constraint on the ordering in ProtectionPriorityRival; the
trivial PositiveRelevant satisfies G0 jointly with the trading score and C. -/
open ProtectionPriorityRival in
example : G0 inventory (fun _ _ => True) ∧
    ComparisonPrinciple inventory (fun a b => weighted 0 a < weighted 0 b) ∧
    weighted 0 0 < weighted 0 1 :=
  ⟨fun _ _ _ _ => True.intro, weighted_satisfies_comparison 0, by decide⟩
