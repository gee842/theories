import GenerativeCore

/-! A conditional witness for recurrent selection-condition reproduction.
The discrete maintenance/selection law, candidate supply, reconstruction rule,
carrier individuation and time unit are supplied. No ethical predicate occurs.
This is a separate minimal model, not a refinement of MarketGenerativity. -/

namespace RecursiveSelection

structure State where
  condition : Nat
  carrier : Nat
  parts : Nat
  deriving DecidableEq, Repr

/-- Organization A is selected exactly when the maintained condition reaches 3.
Organization B is selected otherwise. The threshold is a supplied local law. -/
def selected (q : Nat) : Bool := decide (3 ≤ q)

/-- Wear removes one available unit. A returns two units to the selection
condition. Eight is the local storage capacity. -/
def update (q : Nat) : Nat :=
  if 3 ≤ q then min 8 (q - 1 + 2) else q - 1

/-- A matched intervention disconnecting the output-to-condition route. -/
def severed (q : Nat) : Nat := q - 1

/-- Rival causal implementations of the return, within the represented history. -/
inductive Source where
  | activity
  | substitute
  deriving DecidableEq, Repr

def contribution (q : Nat) : Nat := if 3 ≤ q then 2 else 0

/-- In the substitute implementation the current condition directly controls
a supplied return source. Cutting the activity's return route leaves that route.
The two implementations agree observationally, but differ under the same cut. -/
def sourceReturn (source : Source) (cut : Bool) (q : Nat) : Nat :=
  match source with
  | .activity => if cut then 0 else contribution q
  | .substitute => contribution q

def causalUpdate (source : Source) (cut : Bool) (q : Nat) : Nat :=
  min 8 (q - 1 + sourceReturn source cut q)

def substituted (q : Nat) : Nat := causalUpdate .substitute true q

/-- A general local maintenance law with explicit costs and returned support. -/
def maintained (threshold cap wear returned q : Nat) : Nat :=
  if threshold ≤ q then min cap (q - wear + returned) else q - wear

/-- A completed replacement consumes a part. Supplied arrivals occur after
consumption; an empty beginning inventory cannot spend future arrivals. -/
def cycle (arrivals : Nat) (s : State) : State :=
  if 0 < s.parts then
    ⟨update s.condition, s.carrier + 1, s.parts - 1 + arrivals⟩
  else s

def history (arrivals : Nat) (s : State) : Nat → State
  | 0 => s
  | t + 1 => cycle arrivals (history arrivals s t)

def iterate (f : Nat → Nat) (q : Nat) : Nat → Nat
  | 0 => q
  | t + 1 => f (iterate f q t)

def process (arrivals : Nat) : Generative.Process State Unit where
  step s _ t := 0 < s.parts ∧ t = cycle arrivals s

theorem maintenance_certificate (threshold cap wear returned q : Nat)
    (hq : threshold ≤ q) (hw : wear ≤ threshold)
    (hr : wear ≤ returned) (hc : threshold ≤ cap) :
    threshold ≤ maintained threshold cap wear returned q ∧
    maintained threshold cap wear returned q ≤ cap := by
  simp only [maintained, if_pos hq]
  omega

/-- A changed threshold remains attainable when actual replacement covers its
increase. The threshold-change law remains a supplied input to this theorem. -/
theorem moving_boundary_certificate (threshold nextThreshold cap wear returned q : Nat)
    (hq : threshold ≤ q) (hw : wear ≤ threshold)
    (hr : nextThreshold + wear ≤ threshold + returned)
    (hc : nextThreshold ≤ cap) :
    nextThreshold ≤ maintained threshold cap wear returned q := by
  simp only [maintained, if_pos hq]
  omega

theorem maintenance_history (threshold cap wear returned q t : Nat)
    (hq : threshold ≤ q) (hw : wear ≤ threshold)
    (hr : wear ≤ returned) (hc : threshold ≤ cap) :
    threshold ≤ iterate (maintained threshold cap wear returned) q t := by
  induction t with
  | zero => exact hq
  | succ t ih =>
    exact (maintenance_certificate threshold cap wear returned _ ih hw hr hc).1

theorem supplied_return_shortfall : maintained 3 8 1 0 3 = 2 := by decide

theorem core_enabled_iff (a : Nat) (s : State) :
    Generative.Enabled (process a) s () ↔ 0 < s.parts := by
  constructor
  · rintro ⟨t, h, _⟩
    exact h
  · intro h
    exact ⟨cycle a s, h, rfl⟩

theorem output_changes_condition (q : Nat) (h : 3 ≤ q) (hu : q ≤ 8) :
    severed q < update q := by
  simp only [severed, update, if_pos h]
  omega

theorem high_step (q : Nat) (h : 3 ≤ q) :
    update q = min 8 (q + 1) := by
  simp only [update, if_pos h]
  congr 1
  omega

theorem high_invariant (q : Nat) (h : 3 ≤ q) :
    3 ≤ update q ∧ update q ≤ 8 := by
  rw [high_step q h]
  omega

theorem low_step (q : Nat) (h : q < 3) : update q = q - 1 := by
  simp only [update, if_neg (by omega : ¬ 3 ≤ q)]

theorem low_invariant (q : Nat) (h : q < 3) : update q < 3 := by
  rw [low_step q h]
  omega

theorem high_history (q t : Nat) (hq : 3 ≤ q) (hu : q ≤ 8) :
    iterate update q t = min 8 (q + t) := by
  induction t with
  | zero => simp only [iterate, Nat.add_zero]; omega
  | succ t ih =>
    simp only [iterate, ih]
    rw [high_step _ (by omega)]
    omega

theorem low_history (q t : Nat) (hq : q < 3) :
    iterate update q t = q - t := by
  induction t with
  | zero => simp [iterate]
  | succ t ih =>
    simp only [iterate, ih]
    rw [low_step _ (by omega)]
    omega

theorem exact_basin (q : Nat) (hu : q ≤ 8) :
    (∃ t, iterate update q t = 8) ↔ 3 ≤ q := by
  constructor
  · rintro ⟨t, ht⟩
    by_cases h : 3 ≤ q
    · exact h
    · rw [low_history q t (by omega)] at ht
      omega
  · intro h
    exact ⟨8, by rw [high_history q 8 h hu]; omega⟩

theorem carrier_supply (s : State) (h : 0 < s.parts) :
    (cycle 1 s).parts = s.parts ∧
    (cycle 1 s).carrier = s.carrier + 1 ∧
    (cycle 1 s).condition = update s.condition := by
  simp only [cycle, if_pos h]
  constructor
  · omega
  · exact ⟨True.intro, True.intro⟩

theorem complete_turnover (s : State) (t : Nat) (h : 0 < s.parts) :
    (history 1 s t).parts = s.parts ∧
    (history 1 s t).carrier = s.carrier + t ∧
    (history 1 s t).condition = iterate update s.condition t := by
  induction t with
  | zero => simp [history, iterate]
  | succ t ih =>
    have hp : 0 < (history 1 s t).parts := by omega
    have hc := carrier_supply (history 1 s t) hp
    simp only [history, iterate]
    constructor
    · omega
    constructor
    · omega
    · rw [hc.2.2, ih.2.2]

theorem carriers_distinct (s : State) (t u : Nat) (h : 0 < s.parts)
    (htu : t ≠ u) : (history 1 s t).carrier ≠ (history 1 s u).carrier := by
  have ht := (complete_turnover s t h).2.1
  have hu := (complete_turnover s u h).2.1
  omega

theorem every_cycle_enabled (s : State) (t : Nat) (h : 0 < s.parts) :
    Generative.Enabled (process 1) (history 1 s t) () := by
  apply (core_enabled_iff 1 _).mpr
  have := (complete_turnover s t h).1
  omega

theorem actual_core_history (s : State) (t : Nat) (h : 0 < s.parts) :
    Generative.Trace (process 1) s (List.replicate t ()) (history 1 s t) := by
  induction t with
  | zero => exact .nil s
  | succ t ih =>
    have hp : 0 < (history 1 s t).parts := by
      have := (complete_turnover s t h).1
      omega
    have hs : (process 1).step (history 1 s t) () (history 1 s (t+1)) :=
      ⟨hp, rfl⟩
    have hh : Generative.Trace (process 1) s
        (List.replicate t () ++ [()]) (history 1 s (t+1)) :=
      Generative.trace_append_iff.mpr
        ⟨history 1 s t, ih, Generative.trace_singleton_iff.mpr hs⟩
    rw [← List.replicate_succ'] at hh
    exact hh

theorem recurrent_across_carriers (s : State) (t : Nat)
    (hp : 0 < s.parts) (hq : 3 ≤ s.condition) (hu : s.condition ≤ 8) :
    selected (history 1 s t).condition = true ∧
    (history 1 s t).carrier = s.carrier + t := by
  have ht := complete_turnover s t hp
  constructor
  · rw [ht.2.2, high_history s.condition t hq hu]
    simp only [selected, decide_eq_true_eq]
    omega
  · exact ht.2.1

/-- The attracting object is a region of organized relations, not a fixed full
state: carrier identity keeps changing after the condition reaches capacity. -/
theorem saturated_turnover (s : State) (t : Nat) (hp : 0 < s.parts)
    (hq : 3 ≤ s.condition) (hu : s.condition ≤ 8) (ht : 8 ≤ t) :
    (history 1 s t).condition = 8 ∧
    (history 1 s (t+1)).carrier ≠ (history 1 s t).carrier := by
  have hc := complete_turnover s t hp
  constructor
  · rw [hc.2.2, high_history s.condition t hq hu]
    omega
  · exact carriers_distinct s (t+1) t hp (by omega)

theorem finite_parts (s : State) (t : Nat) :
    (history 0 s t).parts = s.parts - t := by
  induction t with
  | zero => simp [history]
  | succ t ih =>
    by_cases hp : 0 < (history 0 s t).parts
    · simp only [history, cycle, if_pos hp]
      change (history 0 s t).parts - 1 + 0 = s.parts - (t+1)
      omega
    · simp only [history, cycle, if_neg hp]
      omega

theorem finite_supply_stops (s : State) :
    ¬ Generative.Enabled (process 0) (history 0 s s.parts) () := by
  rw [core_enabled_iff, finite_parts]
  omega

theorem invariant_without_activity :
    cycle 1 ⟨8, 0, 0⟩ = ⟨8, 0, 0⟩ ∧
    ¬ Generative.Enabled (process 1) ⟨8, 0, 0⟩ () := by
  constructor
  · decide
  · rw [core_enabled_iff]; decide

theorem severed_history (q t : Nat) : iterate severed q t = q - t := by
  induction t with
  | zero => simp [iterate]
  | succ t ih => simp only [iterate, severed, ih]; omega

theorem severance_breaks_reproduction (q : Nat) :
    selected (iterate severed q q) = false := by
  rw [severed_history]
  simp [selected]

/-- Required impulse is state dependent, even with an unchanged basin. -/
theorem escape_budget (q budget : Nat) (hq : 3 ≤ q) :
    (∃ u, u ≤ budget ∧ q - u < 3) ↔ q - 2 ≤ budget := by
  constructor
  · rintro ⟨u, hb, he⟩; omega
  · intro hb
    exact ⟨q-2, hb, by omega⟩

theorem recoverability_contracts :
    (∃ u, u ≤ 1 ∧ 3-u < 3) ∧ ¬ (∃ u, u ≤ 1 ∧ 8-u < 3) := by
  constructor
  · exact ⟨1, by decide, by decide⟩
  · omega

theorem passive_causal_steps (q : Nat) :
    causalUpdate .activity false q = update q ∧ substituted q = update q := by
  simp only [causalUpdate, sourceReturn, Bool.false_eq_true, ↓reduceIte,
    substituted, contribution, update]
  split <;> omega

/-- Identical passive histories under different causal sources. -/
theorem passive_histories_equal (q t : Nat) :
    iterate update q t = iterate substituted q t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    simp only [iterate, ← ih, (passive_causal_steps _).2]

theorem intervention_separates :
    causalUpdate .activity true 3 = 2 ∧ causalUpdate .substitute true 3 = 4 := by decide

/-- A label inferred solely from this passive condition history cannot identify
which of the two causal source models generated it. -/
theorem no_passive_classifier
    (classifier : (Nat → Nat) → Bool) :
    ¬ (classifier (iterate update 3) = true ∧
       classifier (iterate substituted 3) = false) := by
  have he : iterate update 3 = iterate substituted 3 :=
    funext (passive_histories_equal 3)
  rw [← he]
  intro h
  have hf : true = false := h.1.symm.trans h.2
  cases hf

theorem delayed_escape_budget (q t budget : Nat) (hq : 3 ≤ q) (hu : q ≤ 8) :
    (∃ u, u ≤ budget ∧ iterate update q t - u < 3) ↔
      min 8 (q+t) - 2 ≤ budget := by
  rw [high_history q t hq hu]
  exact escape_budget _ budget (by omega)

theorem escape_stays_out (q u t : Nat) (he : q-u < 3) :
    iterate update (q-u) t < 3 := by
  rw [low_history _ t he]
  omega

theorem one_round_closes_budget :
    (∃ u, u ≤ 1 ∧ iterate update 3 0 - u < 3) ∧
    ¬ (∃ u, u ≤ 1 ∧ iterate update 3 1 - u < 3) := by
  constructor
  · exact ⟨1, by decide, by decide⟩
  · change ¬ (∃ u, u ≤ 1 ∧ 4-u < 3)
    omega

def disturbed (shock : Nat → Nat) (q : Nat) : Nat → Nat
  | 0 => q
  | t+1 => update (disturbed shock q t) - shock t

theorem robust_step (q shock : Nat) (hq : 3 ≤ q) (hs : shock ≤ 1) :
    3 ≤ update q - shock ∧ update q - shock ≤ 8 := by
  rw [high_step q hq]
  omega

theorem robust_recurrence (q : Nat) (shock : Nat → Nat) (hq : 3 ≤ q)
    (hs : ∀ t, shock t ≤ 1) (t : Nat) : 3 ≤ disturbed shock q t := by
  induction t with
  | zero => exact hq
  | succ t ih => exact (robust_step _ _ ih (hs t)).1

theorem excessive_shock_breaks : update 3 - 2 = 2 := by decide

/-- One impulse works for every state in a calibrated interval after a known
unforced delay exactly when the budget covers the worst endpoint. -/
theorem uniform_delayed_escape (lo hi delay budget : Nat)
    (hl : 3 ≤ lo) (horder : lo ≤ hi) (hu : hi ≤ 8) :
    (∃ impulse, impulse ≤ budget ∧ ∀ q, lo ≤ q → q ≤ hi →
      iterate update q delay - impulse < 3) ↔
      min 8 (hi+delay) - 2 ≤ budget := by
  constructor
  · rintro ⟨u, hb, he⟩
    have h := he hi horder (by omega)
    rw [high_history hi delay (by omega) hu] at h
    omega
  · intro hb
    refine ⟨budget, Nat.le_refl _, ?_⟩
    intro q hql hqh
    rw [high_history q delay (by omega) (by omega)]
    omega

theorem interval_uncertainty_can_close_exit :
    (∃ u, u ≤ 1 ∧ iterate update 3 0 - u < 3) ∧
    ¬ (∃ u, u ≤ 1 ∧ ∀ q, 3 ≤ q → q ≤ 4 → iterate update q 0 - u < 3) := by
  constructor
  · exact ⟨1, by decide, by decide⟩
  · rw [uniform_delayed_escape 3 4 0 1 (by decide) (by decide) (by decide)]
    decide

end RecursiveSelection
