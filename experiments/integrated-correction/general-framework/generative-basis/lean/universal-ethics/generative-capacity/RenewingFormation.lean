import GenerativeComparison

/-!
# Renewing and consuming formation within one unfolding

9 October 2026. One continuing activity forms further organization from the
conditions it holds (`stock`). The same unfolding contains an organization that
restores those conditions at a rate (`renew`). Formation pressure (`demand`) is
the activity's draw at each step. These are differentiated aspects of one
history, not independent owners exchanging resources.

The supplied local `WearLaw` states one relation: formation pressure within the
renewal rate leaves the renewing organization intact; pressure beyond it draws
on that organization and reduces its rate. Which real processes satisfy this law
is a correspondence question, not settled here.

Part A contains no normative predicate. It proves that, under the same law,
formation within renewal continues at every step without end, whereas formation
that persistently exceeds renewal has a bounded total over the entire unfolding
and ceases by an explicit time. Co-dependent formation sharing those conditions
ceases with it, whatever the allocation between them. Consuming formation can
nevertheless form more at first: local counts reverse the whole-continuation
comparison.

Part B connects Part A to the explicit premise G0 of `GenerativeComparison`.
Read over every realized formation event, G0 gives positive relevance to the
events of both continuations and so cannot itself separate them. The separation
is the dynamical property proved in Part A. G0 supplies valence; these theorems
supply discriminating content. Ceasing is not thereby shown to be bad: finite
fulfillment, rest and appropriate ending remain within the account. The sharper
relation is the ending of co-dependent formation that did not itself exceed
renewal.
-/

namespace RenewingFormation

/-- Conditions of further formation held now and the current renewal rate. -/
structure Conditions where
  stock : Nat
  renew : Nat
  deriving DecidableEq, Repr

/-- Supplied local law: how formation pressure changes the renewing organization. -/
structure WearLaw where
  degrade : Nat → Nat → Nat
  keep : ∀ r d, d ≤ r → degrade r d = r
  wear : ∀ r d, r < d → 0 < r → degrade r d < r
  bounded : ∀ r d, degrade r d ≤ r

/-- What forms at a step: the pressure, limited by held and renewed conditions. -/
def formedAt (c : Conditions) (d : Nat) : Nat := min d (c.stock + c.renew)

def next (law : WearLaw) (c : Conditions) (d : Nat) : Conditions :=
  ⟨c.stock + c.renew - formedAt c d, law.degrade c.renew d⟩

def path (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Nat → Conditions
  | 0 => c0
  | n + 1 => next law (path law c0 demand n) (demand n)

def formed (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) (n : Nat) : Nat :=
  formedAt (path law c0 demand n) (demand n)

def cumulative (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => cumulative law c0 demand n + formed law c0 demand n

/-- Further formation at every step of the represented continuation. -/
def Ceaseless (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, 0 < formed law c0 demand n

/-- Pressure within the renewal rate, and never empty. -/
def WithinRenewal (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, 1 ≤ demand n ∧ demand n ≤ c0.renew

/-- Pressure persistently beyond the initial renewal rate. -/
def BeyondRenewal (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, c0.renew < demand n

/-- Triangular number: the most renewal a rate can still supply while it wears. -/
def tri : Nat → Nat
  | 0 => 0
  | r + 1 => tri r + (r + 1)

theorem tri_mono {a b : Nat} (h : a ≤ b) : tri a ≤ tri b := by
  induction b with
  | zero => have : a = 0 := by omega
            subst this; exact Nat.le_refl _
  | succ k ih =>
    by_cases hk : a ≤ k
    · have := ih hk
      simp only [tri]; omega
    · have : a = k + 1 := by omega
      subst this; exact Nat.le_refl _

theorem tri_zero_iff (r : Nat) : tri r = 0 ↔ r = 0 := by
  cases r with
  | zero => simp [tri]
  | succ k => simp [tri]

theorem tri_wear {a b : Nat} (h : a < b) : tri a + b ≤ tri b := by
  cases b with
  | zero => omega
  | succ k =>
    have := tri_mono (show a ≤ k by omega)
    simp only [tri]; omega

/-- Whole budget of further formation available to pressure beyond renewal. -/
def budget (c : Conditions) : Nat := c.stock + tri c.renew

/-! ## Part A: the dynamics, without any normative predicate -/

theorem renewal_never_grows (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) :
    ∀ n, (path law c0 demand n).renew ≤ c0.renew := by
  intro n
  induction n with
  | zero => exact Nat.le_refl _
  | succ k ih => exact Nat.le_trans (law.bounded _ _) ih

/-- Within renewal: the renewing organization stays intact, held conditions do not
fall, and the whole pressure is realized at every step. -/
theorem within_renewal_invariant (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (within : WithinRenewal c0 demand) :
    ∀ n, (path law c0 demand n).renew = c0.renew ∧
      c0.stock ≤ (path law c0 demand n).stock ∧
      formed law c0 demand n = demand n := by
  have step : ∀ n, (path law c0 demand n).renew = c0.renew ∧
      c0.stock ≤ (path law c0 demand n).stock := by
    intro n
    induction n with
    | zero => exact ⟨rfl, Nat.le_refl _⟩
    | succ k ih =>
      obtain ⟨hr, hs⟩ := ih
      obtain ⟨_, hd⟩ := within k
      refine ⟨?_, ?_⟩
      · show law.degrade (path law c0 demand k).renew (demand k) = c0.renew
        rw [hr]; exact law.keep _ _ hd
      · show c0.stock ≤ (path law c0 demand k).stock + (path law c0 demand k).renew -
          min (demand k) ((path law c0 demand k).stock + (path law c0 demand k).renew)
        rw [hr]; omega
  intro n
  obtain ⟨hr, hs⟩ := step n
  refine ⟨hr, hs, ?_⟩
  obtain ⟨_, hd⟩ := within n
  show min (demand n) ((path law c0 demand n).stock + (path law c0 demand n).renew) = demand n
  rw [hr]; omega

/-- 生生不息 in the represented scope: formation within renewal never ceases. -/
theorem within_renewal_ceaseless (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (within : WithinRenewal c0 demand) : Ceaseless law c0 demand := by
  intro n
  rw [(within_renewal_invariant law c0 demand within n).2.2]
  exact (within n).1

theorem within_renewal_grows (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (within : WithinRenewal c0 demand) : ∀ n, n ≤ cumulative law c0 demand n := by
  intro n
  induction n with
  | zero => exact Nat.le_refl _
  | succ k ih =>
    have := within_renewal_ceaseless law c0 demand within k
    simp only [cumulative]; omega

/-- One step beyond renewal: what forms plus the remaining budget never exceeds the
budget before, and the budget strictly falls unless it is already exhausted. -/
theorem beyond_step (law : WearLaw) (c : Conditions) (d : Nat) (beyond : c.renew < d) :
    formedAt c d + budget (next law c d) ≤ budget c ∧
      (0 < budget c → 0 < formedAt c d) := by
  have hf : formedAt c d ≤ c.stock + c.renew := Nat.min_le_right _ _
  refine ⟨?_, ?_⟩
  · show formedAt c d + ((c.stock + c.renew - formedAt c d) + tri (law.degrade c.renew d))
      ≤ c.stock + tri c.renew
    by_cases hr : c.renew = 0
    · have h0 : law.degrade c.renew d = 0 := by
        have := law.bounded c.renew d; omega
      rw [h0, hr]; simp [tri]; omega
    · have hw := tri_wear (law.wear c.renew d beyond (by omega))
      omega
  · intro positive
    unfold budget at positive
    have hpos : 0 < c.stock + c.renew := by
      by_cases hr : c.renew = 0
      · rw [hr] at positive; simp [tri] at positive; omega
      · omega
    show 0 < min d (c.stock + c.renew)
    omega

/-- Beyond renewal, the entire unfolding's formation is bounded by the initial budget. -/
theorem beyond_renewal_invariant (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, cumulative law c0 demand n + budget (path law c0 demand n) ≤ budget c0 := by
  intro n
  induction n with
  | zero => simp [cumulative, path]
  | succ k ih =>
    have hb : (path law c0 demand k).renew < demand k :=
      Nat.lt_of_le_of_lt (renewal_never_grows law c0 demand k) (beyond k)
    have := (beyond_step law (path law c0 demand k) (demand k) hb).1
    show cumulative law c0 demand k + formed law c0 demand k +
      budget (next law (path law c0 demand k) (demand k)) ≤ budget c0
    unfold formed
    omega

theorem beyond_renewal_bounded (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, cumulative law c0 demand n ≤ budget c0 := fun n =>
  Nat.le_trans (Nat.le_add_right _ _) (beyond_renewal_invariant law c0 demand beyond n)

theorem beyond_renewal_budget_falls (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, budget (path law c0 demand n) ≤ budget c0 - n := by
  intro n
  induction n with
  | zero => simp [path]
  | succ k ih =>
    have hb : (path law c0 demand k).renew < demand k :=
      Nat.lt_of_le_of_lt (renewal_never_grows law c0 demand k) (beyond k)
    obtain ⟨h1, h2⟩ := beyond_step law (path law c0 demand k) (demand k) hb
    show budget (next law (path law c0 demand k) (demand k)) ≤ budget c0 - (k + 1)
    by_cases hz : budget (path law c0 demand k) = 0
    · omega
    · have := h2 (by omega)
      omega

/-- Explicit cessation: from the time equal to the initial budget, nothing forms. -/
theorem beyond_renewal_ceases (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, budget c0 ≤ n → formed law c0 demand n = 0 := by
  intro n late
  have h := beyond_renewal_budget_falls law c0 demand beyond n
  have hz : budget (path law c0 demand n) = 0 := by omega
  unfold budget at hz
  have hs : (path law c0 demand n).stock = 0 := by omega
  have hr : (path law c0 demand n).renew = 0 :=
    (tri_zero_iff _).mp (by omega)
  show min (demand n) ((path law c0 demand n).stock + (path law c0 demand n).renew) = 0
  rw [hs, hr]; simp

theorem beyond_renewal_not_ceaseless (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) : ¬ Ceaseless law c0 demand := by
  intro ceaseless
  have := ceaseless (budget c0)
  rw [beyond_renewal_ceases law c0 demand beyond (budget c0) (Nat.le_refl _)] at this
  exact Nat.lt_irrefl 0 this

/-- Co-dependent formation drawing on the same conditions, under any allocation of
what forms, is bounded and ceases with the consuming part. -/
theorem shared_formation_ceases (law : WearLaw) (c0 : Conditions)
    (own other : Nat → Nat) (share : Nat → Nat)
    (consuming : ∀ n, c0.renew < other n)
    (allocated : ∀ n, share n ≤ formed law c0 (fun k => own k + other k) n) :
    (∀ n, budget c0 ≤ n → share n = 0) ∧
    (∀ n, (List.range n).foldr (fun k acc => share k + acc) 0 ≤ budget c0) := by
  have beyond : BeyondRenewal c0 (fun k => own k + other k) := by
    intro n; have := consuming n; show c0.renew < own n + other n; omega
  refine ⟨?_, ?_⟩
  · intro n late
    have := allocated n
    rw [beyond_renewal_ceases law c0 _ beyond n late] at this
    omega
  · intro n
    have bound := beyond_renewal_bounded law c0 _ beyond n
    have shares : ∀ m, (List.range m).foldr (fun k acc => share k + acc) 0 ≤
        cumulative law c0 (fun k => own k + other k) m := by
      intro m
      induction m with
      | zero => simp [cumulative]
      | succ k ih =>
        rw [List.range_succ, List.foldr_append]
        simp only [List.foldr_cons, List.foldr_nil, Nat.add_zero, cumulative]
        have hk := allocated k
        have fold_shift : ∀ (xs : List Nat) (a : Nat),
            xs.foldr (fun k acc => share k + acc) a =
              xs.foldr (fun k acc => share k + acc) 0 + a := by
          intro xs a
          induction xs with
          | nil => simp
          | cons x xs ihx => simp only [List.foldr_cons, ihx]; omega
        rw [fold_shift]
        omega
    exact Nat.le_trans (shares n) bound

/-- Without the consuming part, the same co-dependent formation never ceases. -/
theorem without_consuming_part_ceaseless (law : WearLaw) (c0 : Conditions)
    (own : Nat → Nat) (within : WithinRenewal c0 own) :
    Ceaseless law c0 own ∧ ∀ n, formed law c0 own n = own n :=
  ⟨within_renewal_ceaseless law c0 own within,
    fun n => (within_renewal_invariant law c0 own within n).2.2⟩

/-- The same co-dependent formation: ceaseless on its own within renewal, yet ending
by the budget time once another differentiated part persistently exceeds renewal. -/
theorem consuming_part_ends_otherwise_ceaseless_formation (law : WearLaw) (c0 : Conditions)
    (own other share : Nat → Nat) (within : WithinRenewal c0 own)
    (consuming : ∀ n, c0.renew < other n)
    (allocated : ∀ n, share n ≤ formed law c0 (fun k => own k + other k) n) :
    Ceaseless law c0 own ∧ ∀ n, budget c0 ≤ n → share n = 0 :=
  ⟨(without_consuming_part_ceaseless law c0 own within).1,
    (shared_formation_ceases law c0 own other share consuming allocated).1⟩

/-- Sustained formation at the full renewal rate realizes exactly that rate each step. -/
theorem sustained_cumulative (law : WearLaw) (c0 : Conditions) (positive : 1 ≤ c0.renew) :
    ∀ n, cumulative law c0 (fun _ => c0.renew) n = n * c0.renew := by
  have within : WithinRenewal c0 (fun _ => c0.renew) := fun _ => ⟨positive, Nat.le_refl _⟩
  intro n
  induction n with
  | zero => simp [cumulative]
  | succ k ih =>
    simp only [cumulative, ih, (within_renewal_invariant law c0 _ within k).2.2]
    rw [Nat.succ_mul]

/-- Whole comparison: after the budget, sustained formation exceeds every consuming one. -/
theorem sustained_eventually_exceeds_every_consuming (law : WearLaw) (c0 : Conditions)
    (positive : 1 ≤ c0.renew) (demand : Nat → Nat) (beyond : BeyondRenewal c0 demand) :
    ∀ n, budget c0 < n →
      cumulative law c0 demand n < cumulative law c0 (fun _ => c0.renew) n := by
  intro n late
  rw [sustained_cumulative law c0 positive n]
  have := beyond_renewal_bounded law c0 demand beyond n
  have : n ≤ n * c0.renew := Nat.le_mul_of_pos_right n positive
  omega

/-- Local reversal: with any held stock, a consuming pressure forms more at first. -/
theorem consuming_forms_more_first (law : WearLaw) (c0 : Conditions)
    (held : 1 ≤ c0.stock) (positive : 1 ≤ c0.renew) :
    let surge : Nat → Nat := fun _ => c0.stock + c0.renew
    BeyondRenewal c0 surge ∧
      cumulative law c0 (fun _ => c0.renew) 1 < cumulative law c0 surge 1 ∧
      ∀ n, budget c0 < n →
        cumulative law c0 surge n < cumulative law c0 (fun _ => c0.renew) n := by
  intro surge
  have beyond : BeyondRenewal c0 surge := fun _ => by show c0.renew < c0.stock + c0.renew; omega
  refine ⟨beyond, ?_, sustained_eventually_exceeds_every_consuming law c0 positive surge beyond⟩
  rw [sustained_cumulative law c0 positive 1]
  show 1 * c0.renew < 0 + min (c0.stock + c0.renew) (c0.stock + c0.renew)
  omega

/-- The law class is inhabited: excess pressure wears one unit of renewal per step. -/
def unitWear : WearLaw where
  degrade := fun r d => if d ≤ r then r else r - 1
  keep := by intro r d h; simp [h]
  wear := by intro r d h hr; simp [Nat.not_le.mpr h]; omega
  bounded := by intro r d; by_cases h : d ≤ r <;> simp [h]

/-! ## Part B: what G0 contributes, and what it cannot by itself separate -/

open GenerativeComparison

/-- Each realized formation event `(step, index)` of a continuation, read in the
broad scope where every newly formed organization counts as generative. -/
def eventInventory (law : WearLaw) (c0 : Conditions) :
    Inventory (Nat → Nat) (Nat × Nat) where
  realized := fun demand e => e.2 < formed law c0 demand e.1
  generative := fun _ => True

/-- Read event by event, G0 gives positive relevance to both continuations'
formation, including the consuming continuation's larger first-step formation. -/
theorem event_reading_favors_both (law : WearLaw) (c0 : Conditions)
    (held : 1 ≤ c0.stock) (positive : 1 ≤ c0.renew)
    (PositiveRelevant : (Nat → Nat) → Nat × Nat → Prop)
    (g0 : G0 (eventInventory law c0) PositiveRelevant) :
    let surge : Nat → Nat := fun _ => c0.stock + c0.renew
    let sustained : Nat → Nat := fun _ => c0.renew
    PositiveRelevant surge (0, c0.renew) ∧
      ¬ (eventInventory law c0).realized sustained (0, c0.renew) ∧
      (∀ n i, i < formed law c0 sustained n → PositiveRelevant sustained (n, i)) := by
  intro surge sustained
  have within : WithinRenewal c0 sustained := fun _ => ⟨positive, Nat.le_refl _⟩
  refine ⟨?_, ?_, ?_⟩
  · apply g0 surge (0, c0.renew) True.intro
    show c0.renew < min (c0.stock + c0.renew) (c0.stock + c0.renew)
    omega
  · show ¬ c0.renew < formed law c0 sustained 0
    rw [(within_renewal_invariant law c0 sustained within 0).2.2]
    exact Nat.lt_irrefl _
  · intro n i hi
    exact g0 sustained (n, i) True.intro hi

/-- The whole-direction reading separates them: under the same law and the same
initial conditions, formation within renewal is ceaseless, consuming formation is
not, and co-dependent formation ends with it. This is decided by Part A. -/
theorem whole_direction_separates (law : WearLaw) (c0 : Conditions)
    (positive : 1 ≤ c0.renew) (demand : Nat → Nat) (beyond : BeyondRenewal c0 demand) :
    Ceaseless law c0 (fun _ => c0.renew) ∧ ¬ Ceaseless law c0 demand :=
  ⟨within_renewal_ceaseless law c0 _ (fun _ => ⟨positive, Nat.le_refl _⟩),
    beyond_renewal_not_ceaseless law c0 demand beyond⟩

end RenewingFormation
