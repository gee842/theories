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
on that organization and reduces its rate, which never recovers. Which real
processes satisfy this law is a correspondence question, not settled here.

Part A contains no normative predicate. It proves that, under the same law,
formation within renewal continues at every step without end, whereas formation
whose pressure persistently exceeds the current renewal rate has a bounded total
over the entire unfolding and ceases by an explicit time. Shared formation ends
with it, whatever the allocation, including when two parts are each within
renewal and only jointly exceed it. Consuming formation can nevertheless form
more at first: a one-step count reverses the later comparison. These are
consequences of the supplied no-recovery law, which carries much of the content.

Two formal readings are kept distinct. `Ceaseless` (some formation at every step)
captures 不息, but a single rest falsifies it and it misses a one-off permanent
loss of renewal. `KeepsCapacity` (the renewing organization keeps its rate)
tolerates rest and fails at the first step beyond renewal. Neither captures 更多
or rising complexity, which the law excludes by never letting renewal grow, and
neither is identified here with Ren's whole-direction criterion.

Part B connects Part A to the explicit premise G0 of `GenerativeComparison`.
With a broad inventory in which every realized formation event counts as
generative, formal G0 gives positive relevance to the events of both
continuations, and the no-loss comparison C does not apply between them: neither
is a generative extension of the other. That broad reading is the AI's
formalization, not Ren's G0, whose object is 生生 (Ren's follow-up of 9 October
2026: generative and degenerate relations do not overlap). Part A supplies
descriptive content for recognizing that object without a prior goodness filter;
that these formal readings capture 生生 is a reading and correspondence question,
and that consuming is worse is a comparison carried by C. Ceasing is
not thereby shown to be bad: finite fulfillment, rest and appropriate ending
remain within the account, although this representation omits rest's restorative
role. The sharper relation is the ending of shared formation that did not itself
exceed renewal.
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

/-- Continuing renewal capacity: the renewing organization keeps its initial rate. -/
def KeepsCapacity (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, (path law c0 demand n).renew = c0.renew

/-- Pressure within the renewal rate, and never empty. -/
def WithinRenewal (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, 1 ≤ demand n ∧ demand n ≤ c0.renew

/-- Pressure persistently beyond the initial renewal rate. -/
def BeyondRenewal (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, c0.renew < demand n

/-- Pressure persistently beyond the current renewal rate; weaker than `BeyondRenewal`. -/
def BeyondCurrent (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat) : Prop :=
  ∀ n, (path law c0 demand n).renew < demand n

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

/-- A rate once lost is never regained under this law. -/
theorem renewal_loss_persists (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (n : Nat) : ∀ k, (path law c0 demand (n + k)).renew ≤ (path law c0 demand n).renew := by
  intro k
  induction k with
  | zero => exact Nat.le_refl _
  | succ j ih => exact Nat.le_trans (law.bounded _ _) ih

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

/-- 不息 in the represented scope: formation within renewal never ceases. -/
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

/-- Excess over the initial rate is excess over every later rate. -/
theorem beyond_initial_implies_current (law : WearLaw) (c0 : Conditions)
    (demand : Nat → Nat) (beyond : BeyondRenewal c0 demand) : BeyondCurrent law c0 demand :=
  fun n => Nat.lt_of_le_of_lt (renewal_never_grows law c0 demand n) (beyond n)

/-- Beyond the current rate, the entire unfolding's formation is bounded by the
initial budget. -/
theorem beyond_current_invariant (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
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

theorem beyond_current_bounded (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondCurrent law c0 demand) :
    ∀ n, cumulative law c0 demand n ≤ budget c0 := fun n =>
  Nat.le_trans (Nat.le_add_right _ _) (beyond_current_invariant law c0 demand beyond n)

theorem beyond_current_budget_falls (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondCurrent law c0 demand) :
    ∀ n, budget (path law c0 demand n) ≤ budget c0 - n := by
  intro n
  induction n with
  | zero => simp [path]
  | succ k ih =>
    obtain ⟨h1, h2⟩ := beyond_step law (path law c0 demand k) (demand k) (beyond k)
    show budget (next law (path law c0 demand k) (demand k)) ≤ budget c0 - (k + 1)
    by_cases hz : budget (path law c0 demand k) = 0
    · omega
    · have := h2 (by omega)
      omega

/-- Explicit cessation: from the time equal to the initial budget, nothing forms. -/
theorem beyond_current_ceases (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondCurrent law c0 demand) :
    ∀ n, budget c0 ≤ n → formed law c0 demand n = 0 := by
  intro n late
  have h := beyond_current_budget_falls law c0 demand beyond n
  have hz : budget (path law c0 demand n) = 0 := by omega
  unfold budget at hz
  have hs : (path law c0 demand n).stock = 0 := by omega
  have hr : (path law c0 demand n).renew = 0 :=
    (tri_zero_iff _).mp (by omega)
  show min (demand n) ((path law c0 demand n).stock + (path law c0 demand n).renew) = 0
  rw [hs, hr]; simp

theorem beyond_current_not_ceaseless (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondCurrent law c0 demand) : ¬ Ceaseless law c0 demand := by
  intro ceaseless
  have := ceaseless (budget c0)
  rw [beyond_current_ceases law c0 demand beyond (budget c0) (Nat.le_refl _)] at this
  exact Nat.lt_irrefl 0 this

/-! Results stated with the initial rate, as corollaries. -/

theorem beyond_renewal_invariant (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, cumulative law c0 demand n + budget (path law c0 demand n) ≤ budget c0 :=
  beyond_current_invariant law c0 demand (beyond_initial_implies_current law c0 demand beyond)

theorem beyond_renewal_bounded (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, cumulative law c0 demand n ≤ budget c0 :=
  beyond_current_bounded law c0 demand (beyond_initial_implies_current law c0 demand beyond)

theorem beyond_renewal_budget_falls (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, budget (path law c0 demand n) ≤ budget c0 - n :=
  beyond_current_budget_falls law c0 demand (beyond_initial_implies_current law c0 demand beyond)

theorem beyond_renewal_ceases (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) :
    ∀ n, budget c0 ≤ n → formed law c0 demand n = 0 :=
  beyond_current_ceases law c0 demand (beyond_initial_implies_current law c0 demand beyond)

theorem beyond_renewal_not_ceaseless (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (beyond : BeyondRenewal c0 demand) : ¬ Ceaseless law c0 demand :=
  beyond_current_not_ceaseless law c0 demand (beyond_initial_implies_current law c0 demand beyond)

/-- Shared formation under joint excess: whatever the allocation of what forms, each
share is bounded in total and ends by the budget time. -/
theorem joint_excess_ends_shared_formation (law : WearLaw) (c0 : Conditions)
    (total share : Nat → Nat) (joint : BeyondCurrent law c0 total)
    (allocated : ∀ n, share n ≤ formed law c0 total n) :
    (∀ n, budget c0 ≤ n → share n = 0) ∧
    (∀ n, (List.range n).foldr (fun k acc => share k + acc) 0 ≤ budget c0) := by
  refine ⟨?_, ?_⟩
  · intro n late
    have := allocated n
    rw [beyond_current_ceases law c0 _ joint n late] at this
    omega
  · intro n
    have bound := beyond_current_bounded law c0 _ joint n
    have shares : ∀ m, (List.range m).foldr (fun k acc => share k + acc) 0 ≤
        cumulative law c0 total m := by
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

/-- Co-dependent formation drawing on the same conditions, under any allocation of
what forms, is bounded and ceases once another part persistently exceeds renewal. -/
theorem shared_formation_ceases (law : WearLaw) (c0 : Conditions)
    (own other : Nat → Nat) (share : Nat → Nat)
    (consuming : ∀ n, c0.renew < other n)
    (allocated : ∀ n, share n ≤ formed law c0 (fun k => own k + other k) n) :
    (∀ n, budget c0 ≤ n → share n = 0) ∧
    (∀ n, (List.range n).foldr (fun k acc => share k + acc) 0 ≤ budget c0) := by
  have beyond : BeyondRenewal c0 (fun k => own k + other k) := by
    intro n; have := consuming n; show c0.renew < own n + other n; omega
  exact joint_excess_ends_shared_formation law c0 _ share
    (beyond_initial_implies_current law c0 _ beyond) allocated

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

/-- Joint consumption: two parts, each within renewal and each ceaseless on its own,
end every share of their joint formation once together they persistently exceed
renewal. Neither part need exceed renewal for the shared formation to end. -/
theorem jointly_exceeding_parts_end_shared_formation (law : WearLaw) (c0 : Conditions)
    (own other share : Nat → Nat)
    (ownWithin : WithinRenewal c0 own) (otherWithin : WithinRenewal c0 other)
    (joint : BeyondRenewal c0 (fun k => own k + other k))
    (allocated : ∀ n, share n ≤ formed law c0 (fun k => own k + other k) n) :
    Ceaseless law c0 own ∧ Ceaseless law c0 other ∧ ∀ n, budget c0 ≤ n → share n = 0 :=
  ⟨within_renewal_ceaseless law c0 own ownWithin,
    within_renewal_ceaseless law c0 other otherWithin,
    (joint_excess_ends_shared_formation law c0 _ share
      (beyond_initial_implies_current law c0 _ joint) allocated).1⟩

/-- The joint case is inhabited: two parts at the full rate 2 jointly draw 4. -/
theorem joint_consumption_inhabited :
    WithinRenewal ⟨0, 2⟩ (fun _ => 2) ∧
      BeyondRenewal ⟨0, 2⟩ (fun k => (fun _ => 2) k + (fun _ => 2) k) :=
  ⟨fun _ => ⟨show 1 ≤ 2 by decide, show 2 ≤ 2 by decide⟩, fun _ => show 2 < 2 + 2 by decide⟩

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

/-- More generally: after the budget, every continuation within renewal has formed
more in total than every continuation beyond the current rate. -/
theorem within_eventually_exceeds_every_beyond (law : WearLaw) (c0 : Conditions)
    (own demand : Nat → Nat) (within : WithinRenewal c0 own)
    (beyond : BeyondCurrent law c0 demand) :
    ∀ n, budget c0 < n → cumulative law c0 demand n < cumulative law c0 own n := by
  intro n late
  have := beyond_current_bounded law c0 demand beyond n
  have := within_renewal_grows law c0 own within n
  omega

/-- Local reversal: with any held stock, a consuming pressure forms more at first; the
one-step cumulative count ranks it above sustained formation. -/
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

/-- The current-rate hypothesis is strictly weaker: pressure that exceeds renewal
only after it has worn is covered by the results above. -/
theorem beyond_current_strictly_weaker :
    BeyondCurrent unitWear ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) ∧
      ¬ BeyondRenewal ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) := by
  constructor
  · intro n
    induction n with
    | zero => decide
    | succ k ih =>
      have h : ∀ m, (path unitWear ⟨0, 2⟩ (fun n => if n = 0 then 3 else 2) (m + 1)).renew
          ≤ 1 := by
        intro m
        induction m with
        | zero => decide
        | succ j ihj =>
          have := renewal_loss_persists unitWear ⟨0, 2⟩
            (fun n => if n = 0 then 3 else 2) (j + 1) 1
          omega
      have := h k
      show _ < (if k + 1 = 0 then 3 else 2)
      simp; omega
  · intro b; have := b 1; simp at this

/-! ### Capacity: a second formal reading -/

theorem keeps_capacity_of_within (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (within : ∀ n, demand n ≤ c0.renew) : KeepsCapacity law c0 demand := by
  intro n
  induction n with
  | zero => rfl
  | succ k ih =>
    show law.degrade (path law c0 demand k).renew (demand k) = c0.renew
    rw [ih]; exact law.keep _ _ (within k)

/-- With a positive rate, capacity is kept exactly when no step's pressure exceeds it;
rest (zero pressure) is allowed. -/
theorem keeps_capacity_iff (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (positive : 1 ≤ c0.renew) :
    KeepsCapacity law c0 demand ↔ ∀ n, demand n ≤ c0.renew := by
  refine ⟨?_, keeps_capacity_of_within law c0 demand⟩
  intro keeps n
  by_cases h : demand n ≤ c0.renew
  · exact h
  · exfalso
    have hw := law.wear c0.renew (demand n) (by omega) positive
    have hk : law.degrade (path law c0 demand n).renew (demand n) = c0.renew := keeps (n + 1)
    rw [keeps n] at hk
    omega

/-- Pressure beyond renewal at the first step loses capacity at once, and permanently. -/
theorem beyond_loses_capacity_at_once (law : WearLaw) (c0 : Conditions) (demand : Nat → Nat)
    (positive : 1 ≤ c0.renew) (excess : c0.renew < demand 0) :
    ∀ k, (path law c0 demand (1 + k)).renew < c0.renew := by
  intro k
  have first : (path law c0 demand 1).renew < c0.renew :=
    law.wear c0.renew (demand 0) excess positive
  have := renewal_loss_persists law c0 demand 1 k
  omega

def restOnce : Nat → Nat := fun n => if n = 0 then 0 else 2
def surgeThenSettle : Nat → Nat := fun n => if n = 0 then 3 else 1

/-- The readings differ: resting one step keeps capacity yet is not ceaseless. -/
theorem rest_keeps_capacity_not_ceaseless :
    KeepsCapacity unitWear ⟨3, 2⟩ restOnce ∧ ¬ Ceaseless unitWear ⟨3, 2⟩ restOnce := by
  refine ⟨keeps_capacity_of_within unitWear ⟨3, 2⟩ restOnce
    (fun n => show restOnce n ≤ 2 by unfold restOnce; split <;> omega), ?_⟩
  intro h; have := h 0; revert this; decide

theorem settle_path :
    ∀ n, (path unitWear ⟨0, 2⟩ surgeThenSettle (n + 1)).renew = 1 := by
  intro n
  induction n with
  | zero => decide
  | succ k ih =>
    show unitWear.degrade (path unitWear ⟨0, 2⟩ surgeThenSettle (k + 1)).renew
      (surgeThenSettle (k + 1)) = 1
    rw [ih]
    show (if (if k + 1 = 0 then 3 else 1) ≤ 1 then 1 else 1 - 1) = 1
    simp

/-- The readings differ the other way: surging once and then settling within the
reduced rate permanently loses capacity yet remains ceaseless. -/
theorem wears_yet_ceaseless :
    ¬ KeepsCapacity unitWear ⟨0, 2⟩ surgeThenSettle ∧
      Ceaseless unitWear ⟨0, 2⟩ surgeThenSettle := by
  refine ⟨fun h => by have := h 1; revert this; decide, ?_⟩
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

/-! ## Part B: what G0 and C contribute, and what they cannot by themselves separate -/

open GenerativeComparison

/-- Each realized formation event `(step, index)` of a continuation, read in the
broad scope where every newly formed organization counts as generative. This broad
reading is the AI's formalization, used to show what it cannot separate; it is not
Ren's G0, whose object is 生生. -/
def eventInventory (law : WearLaw) (c0 : Conditions) :
    Inventory (Nat → Nat) (Nat × Nat) where
  realized := fun demand e => e.2 < formed law c0 demand e.1
  generative := fun _ => True

/-- Read event by event in the broad scope, formal G0 gives positive relevance to
both continuations' formation, including the consuming continuation's larger
first-step formation. -/
theorem event_reading_recognizes_both (law : WearLaw) (c0 : Conditions)
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

/-- The no-loss comparison C does not apply between them: neither continuation is a
generative extension of the other, under any law in the class. -/
theorem comparison_does_not_apply (law : WearLaw) (c0 : Conditions)
    (held : 1 ≤ c0.stock) (positive : 1 ≤ c0.renew) :
    let surge : Nat → Nat := fun _ => c0.stock + c0.renew
    let sustained : Nat → Nat := fun _ => c0.renew
    ¬ GenerativeExtension (eventInventory law c0) sustained surge ∧
      ¬ GenerativeExtension (eventInventory law c0) surge sustained := by
  intro surge sustained
  have within : WithinRenewal c0 sustained := fun _ => ⟨positive, Nat.le_refl _⟩
  have beyond : BeyondRenewal c0 surge := fun _ => by
    show c0.renew < c0.stock + c0.renew; omega
  refine ⟨?_, ?_⟩
  · rintro ⟨keeps, _⟩
    have now : 0 < formed law c0 sustained (budget c0) := by
      rw [(within_renewal_invariant law c0 sustained within _).2.2]; exact positive
    have later : 0 < formed law c0 surge (budget c0) := keeps (budget c0, 0) now
    have gone : formed law c0 surge (budget c0) = 0 :=
      beyond_renewal_ceases law c0 surge beyond _ (Nat.le_refl _)
    omega
  · rintro ⟨keeps, _⟩
    have first : (eventInventory law c0).realized surge (0, c0.renew) := by
      show c0.renew < min (c0.stock + c0.renew) (c0.stock + c0.renew)
      omega
    have h : c0.renew < formed law c0 sustained 0 := keeps (0, c0.renew) first
    rw [(within_renewal_invariant law c0 sustained within 0).2.2] at h
    exact Nat.lt_irrefl _ h

/-- A representational limit, not a refutation: in this event reading C ranks a
single rest strictly below sustained formation, because the law omits rest's
restorative role (renewal never grows). -/
theorem event_comparison_ranks_rest_below :
    GenerativeExtension (eventInventory unitWear ⟨3, 2⟩) restOnce (fun _ => 2) := by
  refine ⟨?_, (0, 0), True.intro, (show 0 < formed unitWear ⟨3, 2⟩ (fun _ => 2) 0 by decide),
    (show ¬ (0 < formed unitWear ⟨3, 2⟩ restOnce 0) by decide)⟩
  rintro ⟨n, i⟩ h
  have hw : WithinRenewal ⟨3, 2⟩ (fun _ => 2) := fun _ => ⟨Nat.le_succ 1, Nat.le_refl 2⟩
  show i < formed unitWear ⟨3, 2⟩ (fun _ => 2) n
  rw [(within_renewal_invariant unitWear ⟨3, 2⟩ (fun _ => 2) hw n).2.2]
  have hf : formed unitWear ⟨3, 2⟩ restOnce n ≤ restOnce n := Nat.min_le_left _ _
  have hr : restOnce n ≤ 2 := by unfold restOnce; split <;> omega
  have : i < formed unitWear ⟨3, 2⟩ restOnce n := h
  show i < 2; omega

/-- `Ceaseless` separates them: under the same law and initial conditions, formation
within renewal is ceaseless and formation beyond the current rate is not. -/
theorem ceaseless_separates (law : WearLaw) (c0 : Conditions)
    (positive : 1 ≤ c0.renew) (demand : Nat → Nat) (beyond : BeyondCurrent law c0 demand) :
    Ceaseless law c0 (fun _ => c0.renew) ∧ ¬ Ceaseless law c0 demand :=
  ⟨within_renewal_ceaseless law c0 _ (fun _ => ⟨positive, Nat.le_refl _⟩),
    beyond_current_not_ceaseless law c0 demand beyond⟩

/-- `KeepsCapacity` separates them too, allowing rest and deciding at the first step. -/
theorem capacity_separates (law : WearLaw) (c0 : Conditions)
    (positive : 1 ≤ c0.renew) (own demand : Nat → Nat) (rest : ∀ n, own n ≤ c0.renew)
    (excess : c0.renew < demand 0) :
    KeepsCapacity law c0 own ∧ ¬ KeepsCapacity law c0 demand := by
  refine ⟨keeps_capacity_of_within law c0 own rest, fun keeps => ?_⟩
  have := beyond_loses_capacity_at_once law c0 demand positive excess 0
  have := keeps (1 + 0)
  omega

end RenewingFormation
