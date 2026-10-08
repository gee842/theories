import Std

/-! A conditional local-to-collective failure construction. Agent positions,
payoffs, action repertoire and institutional effects are supplied local laws.
No claim about all intelligence, biological viability or real-valued limits. -/

namespace CollectiveDestruction

def utility (benefit harm charge others : Int) (race : Bool) : Int :=
  if race then benefit - harm * (others + 1) - charge else -harm * others

theorem unilateral_gap (b h q others : Int) :
    utility b h q others true - utility b h q others false = b - h - q := by
  simp only [utility, Bool.false_eq_true, ↓reduceIte]
  grind

theorem dilemma_conditions (b h q n : Int)
    (privateGain : h + q < b) (jointLoss : b < h * n + q) :
    (∀ others, utility b h q others false < utility b h q others true) ∧
      utility b h q (n - 1) true < 0 := by
  constructor
  · intro others
    have := unilateral_gap b h q others
    omega
  · simp only [utility, ↓reduceIte]
    grind

def payoff (q : Nat) (own other : Bool) : Int :=
  utility 5 3 (q : Int) (if other then 1 else 0) own

def choose (q : Nat) : Bool := decide (q < 2)

theorem race_strictly_best (q : Nat) (hq : q < 2) (other : Bool) :
    payoff q false other < payoff q true other := by
  have h := unilateral_gap 5 3 (q : Int) (if other then 1 else 0)
  simp only [payoff]
  omega

theorem restraint_best (q : Nat) (hq : 2 ≤ q) (other : Bool) :
    payoff q true other ≤ payoff q false other := by
  have h := unilateral_gap 5 3 (q : Int) (if other then 1 else 0)
  simp only [payoff]
  omega

theorem restraint_strictly_best (q : Nat) (hq : 3 ≤ q) (other : Bool) :
    payoff q true other < payoff q false other := by
  have h := unilateral_gap 5 3 (q : Int) (if other then 1 else 0)
  simp only [payoff]
  omega

theorem exact_local_optimization (q : Nat) (a other : Bool) :
    payoff q a other ≤ payoff q (choose q) other := by
  by_cases h : q < 2
  · simp only [choose, h, decide_true]
    cases a
    · exact Int.le_of_lt (race_strictly_best q h other)
    · exact Int.le_refl _
  · simp only [choose, h, decide_false]
    cases a
    · exact Int.le_refl _
    · exact restraint_best q (by omega) other

theorem joint_race_pareto_inferior (q : Nat) :
    payoff q true true < payoff q false false := by
  simp [payoff, utility]
  omega

theorem threshold_tie : payoff 2 true true = payoff 2 false true := by decide

def BestResponse (q : Nat) (own other : Bool) : Prop :=
  ∀ alternative, payoff q alternative other ≤ payoff q own other

theorem low_best_response_must_race (q : Nat) (hq : q < 2) (a b : Bool)
    (h : BestResponse q a b) : a = true := by
  cases a
  · have hh := h true
    have hs := race_strictly_best q hq b
    omega
  · rfl

theorem high_best_response_must_restrain (q : Nat) (hq : 3 ≤ q) (a b : Bool)
    (h : BestResponse q a b) : a = false := by
  cases a
  · rfl
  · have hh := h false
    have hs := restraint_strictly_best q hq b
    omega

theorem threshold_racing_also_optimal (b : Bool) : BestResponse 2 true b := by
  intro a
  cases a <;> cases b <;> decide

structure State where
  restraint : Nat
  capacity : Nat
  deriving DecidableEq, Repr

/- Capacity is a particular shared capability, not all material support of
operation. Zero capacity therefore does not by itself disable this model. -/
def act (k : Nat) (s : State) (a b : Bool) : State :=
  if a || b then ⟨s.restraint - 1, s.capacity - k⟩ else s

def step (k : Nat) (s : State) : State :=
  act k s (choose s.restraint) (choose s.restraint)

def run (k : Nat → Nat) (s : State) : Nat → State
  | 0 => s
  | t + 1 => step (k t) (run k s t)

theorem low_step (k : Nat) (s : State) (hq : s.restraint < 2) :
    step k s = ⟨s.restraint - 1, s.capacity - k⟩ := by
  simp [step, act, choose, hq]

theorem high_step (k : Nat) (s : State) (hq : 2 ≤ s.restraint) :
    step k s = s := by
  have h : ¬s.restraint < 2 := by omega
  simp [step, act, choose, h]

theorem low_history (k : Nat → Nat) (s : State) (hq : s.restraint < 2)
    (t : Nat) : (run k s t).restraint < 2 := by
  induction t with
  | zero => exact hq
  | succ t ih =>
    simp only [run, low_step _ _ ih]
    omega

theorem high_history (k : Nat → Nat) (s : State) (hq : 2 ≤ s.restraint)
    (t : Nat) : run k s t = s := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [run, ih, high_step _ _ hq]

theorem restraint_bound (k : Nat → Nat) (s : State) (hq : s.restraint < 2)
    (t : Nat) : (run k s t).restraint ≤ s.restraint - t := by
  induction t with
  | zero => simp [run]
  | succ t ih =>
    rw [run, low_step _ _ (low_history k s hq t)]
    simp only
    omega

theorem capacity_bound (k : Nat → Nat) (s : State) (hq : s.restraint < 2)
    (hk : ∀ t, 1 ≤ k t) (t : Nat) :
    (run k s t).capacity ≤ s.capacity - t := by
  induction t with
  | zero => simp [run]
  | succ t ih =>
    rw [run, low_step _ _ (low_history k s hq t)]
    simp only
    have := hk t
    omega

theorem finite_destructive_entry (k : Nat → Nat) (s : State)
    (hq : s.restraint < 2) (hk : ∀ t, 1 ≤ k t) (t : Nat)
    (ht : s.restraint + s.capacity ≤ t) : run k s t = ⟨0, 0⟩ := by
  have a := restraint_bound k s hq t
  have b := capacity_bound k s hq hk t
  have ha : (run k s t).restraint = 0 := by omega
  have hb : (run k s t).capacity = 0 := by omega
  cases he : run k s t with
  | mk q c => simp_all

theorem destructive_absorbing (k : Nat) : step k ⟨0, 0⟩ = ⟨0, 0⟩ := by
  simp [step, act, choose]

theorem exact_basin (k : Nat → Nat) (s : State) (hk : ∀ t, 1 ≤ k t) :
    (∃ t, run k s t = ⟨0, 0⟩) ↔ s.restraint < 2 := by
  constructor
  · rintro ⟨t, ht⟩
    by_cases h : s.restraint < 2
    · exact h
    · have hh := high_history k s (by omega) t
      have hs : s = ⟨0, 0⟩ := hh.symm.trans ht
      subst s
      simp at h
  · intro h
    exact ⟨s.restraint + s.capacity, finite_destructive_entry k s h hk _ (by omega)⟩

theorem growing_capability_enters (s : State) (hq : s.restraint < 2) :
    run (fun t => t + 1) s (s.restraint + s.capacity) = ⟨0, 0⟩ :=
  finite_destructive_entry _ s hq (by intro t; omega) _ (by omega)

theorem greater_capability_depletes_faster (k l : Nat → Nat) (s : State)
    (hq : s.restraint < 2) (hkl : ∀ t, k t ≤ l t) (t : Nat) :
    (run l s t).capacity ≤ (run k s t).capacity := by
  induction t with
  | zero => simp [run]
  | succ t ih =>
    rw [run, run, low_step _ _ (low_history l s hq t),
      low_step _ _ (low_history k s hq t)]
    simp only
    have := hkl t
    omega

theorem zero_throughput_preserves_capacity (s : State)
    (hq : s.restraint < 2) (t : Nat) :
    (run (fun _ => 0) s t).capacity = s.capacity := by
  induction t with
  | zero => rfl
  | succ t ih =>
    rw [run, low_step _ _ (low_history _ s hq t)]
    simp only [Nat.sub_zero]
    exact ih

def protect (s : State) : State := ⟨max 3 s.restraint, s.capacity⟩

theorem protection_for_any_best_responses (k : Nat) (s : State) (a b : Bool)
    (ha : BestResponse (protect s).restraint a b)
    (hb : BestResponse (protect s).restraint b a) :
    act k (protect s) a b = protect s := by
  have hq : 3 ≤ (protect s).restraint := by
    simp only [protect]
    omega
  have h := high_best_response_must_restrain _ hq a b ha
  have j := high_best_response_must_restrain _ hq b a hb
  subst a
  subst b
  simp [act]

theorem protection_preserves (k : Nat → Nat) (s : State) (t : Nat) :
    run k (protect s) t = protect s := by
  apply high_history
  simp only [protect]
  omega

theorem late_protection_does_not_restore :
    (protect ⟨0, 0⟩).capacity = 0 := rfl

theorem unilateral_restraint_does_not_stop_pressure (k : Nat) (s : State) :
    act k s false true = act k s true true := by simp [act]

theorem joint_restraint_preserves (k : Nat) (s : State) :
    act k s false false = s := by simp [act]

theorem threshold_race_enters_basin (k c : Nat) :
    (act k ⟨2, c⟩ true true).restraint < 2 := by simp [act]

theorem separate_safety_checks_do_not_compose :
    (0 + 1 ≤ (1 : Nat)) ∧ (0 + 1 ≤ (1 : Nat)) ∧ ¬(0 + 1 + 1 ≤ (1 : Nat)) := by
  decide

/- A trajectory certificate with no particular payoff or institutional law.
Its hypotheses are obligations for a proposed mechanism, not discoveries. -/
theorem rank_entry {S : Type} (x : Nat → S) (D : S → Prop) (rank : S → Nat)
    (closed : ∀ t, D (x t) → D (x (t + 1)))
    (descent : ∀ t, ¬D (x t) → rank (x (t + 1)) < rank (x t)) :
    D (x (rank (x 0) + 1)) := by
  have bound : ∀ t, D (x t) ∨ rank (x t) + t ≤ rank (x 0) := by
    intro t
    induction t with
    | zero => exact Or.inr (by omega)
    | succ t ih =>
      by_cases h : D (x t)
      · exact Or.inl (closed t h)
      · have hr := descent t h
        have hb := ih.resolve_left h
        exact Or.inr (by omega)
  have h := bound (rank (x 0) + 1)
  rcases h with h | h
  · exact h
  · omega

theorem invariant_history {S : Type} (x : Nat → S) (K : S → Prop)
    (initial : K (x 0)) (preserved : ∀ t, K (x t) → K (x (t + 1))) :
    ∀ t, K (x t) := by
  intro t
  induction t with
  | zero => exact initial
  | succ t ih => exact preserved t ih

end CollectiveDestruction
