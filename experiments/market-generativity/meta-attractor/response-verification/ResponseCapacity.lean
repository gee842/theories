import Std

/-! Response deficits, finite support, and investment in response itself.
All flow laws and correspondence to actual harmful demands remain supplied.
The first model permits replenishment before loss in a period. Zero support
ends its represented organization; rebuilding from zero is outside its law. -/
namespace ResponseCapacity

def balance (initial : Int) (repair loss : Nat → Int) : Nat → Int
  | 0 => initial
  | t+1 => balance initial repair loss t + repair t - loss t

def support (initial : Int) (repair loss : Nat → Int) : Nat → Int
  | 0 => max 0 initial
  | t+1 => if support initial repair loss t ≤ 0 then 0
      else max 0 (support initial repair loss t + repair t - loss t)

theorem support_nonnegative (initial : Int) (repair loss : Nat → Int) (t : Nat) :
    0 ≤ support initial repair loss t := by
  cases t with
  | zero => simp only [support]; omega
  | succ t => simp only [support]; split <;> omega

theorem zero_support_stays_zero (initial : Int) (repair loss : Nat → Int) (t : Nat)
    (h : support initial repair loss t = 0) : support initial repair loss (t+1) = 0 := by
  simp [support,h]

theorem positive_support_has_positive_predecessor (initial : Int) (repair loss : Nat → Int) (t : Nat)
    (h : 0 < support initial repair loss (t+1)) : 0 < support initial repair loss t := by
  simp only [support] at h
  split at h <;> omega

theorem positive_support_matches_balance (initial : Int) (repair loss : Nat → Int) (t : Nat)
    (h : 0 < support initial repair loss t) : support initial repair loss t = balance initial repair loss t := by
  induction t with
  | zero => simp only [support,balance] at *; omega
  | succ t ih =>
    have hp := positive_support_has_positive_predecessor initial repair loss t h
    have eq := ih hp
    have hn : ¬ support initial repair loss t ≤ 0 := by omega
    simp only [support,hn,↓reduceIte] at h ⊢
    simp only [balance]
    omega

theorem positive_iff_every_prefix (initial : Int) (repair loss : Nat → Int) (t : Nat) :
    0 < support initial repair loss t ↔ ∀ j, j ≤ t → 0 < balance initial repair loss j := by
  induction t with
  | zero =>
    constructor
    · intro h j hj
      have he : j=0 := by omega
      subst j
      change 0 < initial
      change 0 < max 0 initial at h
      omega
    · intro h
      have hh := h 0 (Nat.le_refl _)
      change 0 < initial at hh
      change 0 < max 0 initial
      omega
  | succ t ih =>
    constructor
    · intro h j hj
      have hp := positive_support_has_positive_predecessor initial repair loss t h
      by_cases he : j = t+1
      · subst j
        rw [←positive_support_matches_balance initial repair loss (t+1) h]
        exact h
      · exact ih.mp hp j (by omega)
    · intro h
      have hp : 0 < support initial repair loss t := ih.mpr (by intro j hj; exact h j (by omega))
      have eq := positive_support_matches_balance initial repair loss t hp
      have hn : ¬support initial repair loss t ≤ 0 := by omega
      have hb := h (t+1) (Nat.le_refl _)
      simp only [support,hn,↓reduceIte,balance] at *
      omega

theorem nonpositive_balance_forces_failure (initial : Int) (repair loss : Nat → Int) (t : Nat)
    (h : balance initial repair loss t ≤ 0) : support initial repair loss t = 0 := by
  have hn := support_nonnegative initial repair loss t
  by_cases hp : 0 < support initial repair loss t
  · have he := positive_support_matches_balance initial repair loss t hp
    omega
  · omega

theorem failed_history_remains_failed (initial : Int) (repair loss : Nat → Int) (t : Nat)
    (h : support initial repair loss t = 0) (u : Nat) : support initial repair loss (t+u) = 0 := by
  induction u with
  | zero => simpa using h
  | succ u ih => exact zero_support_stays_zero initial repair loss (t+u) ih

theorem irreversible_failure_even_if_balance_recovers :
    support 1 (fun t => if t=0 then 0 else 3) (fun _ => 2) 2 = 0 ∧
    balance 1 (fun t => if t=0 then 0 else 3) (fun _ => 2) 2 = 0 ∧
    0 < balance 1 (fun t => if t=0 then 0 else 3) (fun _ => 2) 3 := by decide

theorem balance_tail_bound (initial : Int) (repair loss : Nat → Int) (start : Nat)
    (h : ∀ j, repair (start+j)+1 ≤ loss (start+j)) (t : Nat) :
    balance initial repair loss (start+t) ≤ balance initial repair loss start - (t : Int) := by
  induction t with
  | zero => simp
  | succ t ih =>
    have hs := h t
    change balance initial repair loss (start+t) + repair (start+t) - loss (start+t) ≤
      balance initial repair loss start - ((t+1 : Nat) : Int)
    omega

theorem finite_failure_from_persistent_net_loss (initial : Int) (repair loss : Nat → Int) (start : Nat)
    (h : ∀ j, repair (start+j)+1 ≤ loss (start+j)) :
    ∃ t, ∀ u, support initial repair loss (t+u) = 0 := by
  let n := (balance initial repair loss start).toNat
  have hb := balance_tail_bound initial repair loss start h n
  have hi : balance initial repair loss start ≤ (n : Int) := by
    simp only [n]
    omega
  have hz := nonpositive_balance_forces_failure initial repair loss (start+n) (by omega)
  exact ⟨start+n,failed_history_remains_failed initial repair loss (start+n) hz⟩

def missed (demand response : Nat) : Nat := demand-response

theorem growing_raw_demand_with_matching_response (t : Nat) : missed (2^t) (2^t) = 0 := by
  simp [missed]

theorem dyadic_lower_bound (t : Nat) : 2*t+4 ≤ 2^(t+2) := by
  induction t with
  | zero => decide
  | succ t ih =>
    have he : t+1+2 = (t+2)+1 := by omega
    rw [he,Nat.pow_succ]
    omega

theorem exponential_linear_missed_bound (t : Nat) :
    t+1 ≤ missed (2^(t+2)) ((t+2)+1) := by
  have h := dyadic_lower_bound t
  unfold missed
  omega

theorem exponential_load_exceeds_fixed_repair (r t : Nat) :
    (r : Int)+1 ≤ (missed (2^((r+2)+t)) (((r+2)+t)+1) : Int) := by
  have h := exponential_linear_missed_bound (r+t)
  have he : r+t+2 = (r+2)+t := by omega
  rw [he] at h
  omega

theorem exponential_linear_failure (initial : Int) (r : Nat) :
    ∃ t, ∀ u, support initial (fun _ => (r : Int))
      (fun j => (missed (2^j) (j+1) : Int)) (t+u) = 0 := by
  exact finite_failure_from_persistent_net_loss initial _ _ (r+2)
    (exponential_load_exceeds_fixed_repair r)

theorem matched_growth_preserves_support (initial : Int) (hi : 0 < initial) (t : Nat) :
    support initial (fun _ => 0) (fun j => (missed (2^j) (2^j) : Int)) t = initial := by
  induction t with
  | zero => simp [support]; omega
  | succ t ih =>
    rw [support,ih]
    have hm : (missed (2^t) (2^t) : Int) = 0 := by simp [missed]
    rw [hm]
    omega

theorem persistent_misses_with_repair_are_viable (t : Nat) :
    support 1 (fun _ => 1) (fun _ => 1) t = 1 := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [support,ih]; omega

/- The following relations operate together: successful responses replenish
support, deadline misses consume it and impair later response, and investment
uses current support to develop response capacity. Units and conversions are
local model inputs, not a universal measure of intelligence or ethical value. -/
structure State where
  response : Nat
  support : Nat
  deriving DecidableEq, Repr

def step (demand investment : Nat) (s : State) : State :=
  if s.support=0 then s else
  {response := s.response+2*investment-missed demand s.response,
   support := s.support + min demand s.response - (missed demand s.response+investment)}

def run (demand : Nat) (policy : Nat → State → Nat) (s : State) : Nat → State
  | 0 => s
  | t+1 => step demand (policy t (run demand policy s t)) (run demand policy s t)

theorem loss_of_support_absorbing (demand investment : Nat) (s : State) (h : s.support=0) :
    step demand investment s = s := by simp [step,h]

theorem immediate_support_prefers_no_investment (demand investment : Nat) (s : State) :
    (step demand investment s).support ≤ (step demand 0 s).support := by
  simp only [step]
  split <;> simp [missed] <;> omega

theorem investment_has_real_opportunity_cost :
    (step 3 1 ⟨2,2⟩).support < (step 3 0 ⟨2,2⟩).support := by decide

theorem no_investment_response_nonincreasing (demand : Nat) (s : State) :
    (step demand 0 s).response ≤ s.response := by
  simp only [step]
  split <;> simp <;> omega

theorem no_investment_insufficient_response_drop (demand : Nat) (s : State)
    (hv : 0 < s.support) (hc : s.response < demand) :
    (step demand 0 s).response ≤ s.response-1 := by
  have hn : ¬s.support=0 := by omega
  simp [step,hn,missed]
  omega

theorem zero_response_step (demand : Nat) (s : State) (hc : s.response=0) :
    step demand 0 s = ⟨0,s.support-demand⟩ := by
  by_cases hv : s.support=0
  · cases s; simp_all [step]
  · simp [step,hv,missed,hc]

theorem zero_response_history (demand v t : Nat) :
    run demand (fun _ _ => 0) ⟨0,v⟩ t = ⟨0,v-demand*t⟩ := by
  induction t with
  | zero => simp [run]
  | succ t ih =>
    rw [run,ih,zero_response_step _ _ rfl]
    simp [Nat.mul_add]
    omega

theorem response_or_support_exhausted (demand : Nat) (s : State) (hc : s.response < demand) (t : Nat) :
    (run demand (fun _ _ => 0) s t).support=0 ∨
      (run demand (fun _ _ => 0) s t).response ≤ s.response-t := by
  induction t with
  | zero => exact Or.inr (by simp [run])
  | succ t ih =>
    rcases ih with ih | ih
    · rw [run,loss_of_support_absorbing _ _ _ ih]
      exact Or.inl ih
    · by_cases hv : (run demand (fun _ _ => 0) s t).support=0
      · rw [run,loss_of_support_absorbing _ _ _ hv]
        exact Or.inl hv
      · have h := no_investment_insufficient_response_drop demand (run demand (fun _ _ => 0) s t)
          (by omega) (by omega)
        apply Or.inr
        change (step demand 0 (run demand (fun _ _ => 0) s t)).response ≤ _
        omega

theorem constant_demand_greedy_collapse : run 3 (fun _ _ => 0) ⟨2,2⟩ 3 = ⟨0,0⟩ := by decide

theorem full_response_preserved (demand : Nat) (s : State)
    (hv : 0 < s.support) (hc : demand ≤ s.response) :
    step demand 0 s = ⟨s.response,s.support+demand⟩ := by
  have hn : ¬s.support=0 := by omega
  simp [step,hn,missed,Nat.sub_eq_zero_of_le hc,Nat.min_eq_left hc]

theorem full_response_history (demand : Nat) (s : State)
    (hv : 0 < s.support) (hc : demand ≤ s.response) (t : Nat) :
    run demand (fun _ _ => 0) s t = ⟨s.response,s.support+demand*t⟩ := by
  induction t with
  | zero => simp [run]
  | succ t ih =>
    rw [run,ih]
    have hh := full_response_preserved demand ⟨s.response,s.support+demand*t⟩
      (by change 0 < s.support+demand*t; omega) hc
    rw [hh]
    simp [Nat.mul_add]
    omega

theorem one_investment_establishes_viability : step 3 1 ⟨2,2⟩ = ⟨3,2⟩ := by decide

theorem established_response_keeps_working (t : Nat) :
    run 3 (fun _ _ => 0) (step 3 1 ⟨2,2⟩) t = ⟨3,2+3*t⟩ := by
  rw [one_investment_establishes_viability]
  exact full_response_history 3 ⟨3,2⟩ (by decide) (by decide) t

theorem reduced_demand_keeps_working (t : Nat) :
    run 2 (fun _ _ => 0) ⟨2,2⟩ t = ⟨2,2+2*t⟩ := by
  exact full_response_history 2 ⟨2,2⟩ (by decide) (by decide) t

theorem run_add (demand : Nat) (s : State) (t u : Nat) :
    run demand (fun _ _ => 0) s (t+u) =
      run demand (fun _ _ => 0) (run demand (fun _ _ => 0) s t) u := by
  induction u with
  | zero => simp [run]
  | succ u ih =>
    change step demand 0 (run demand (fun _ _ => 0) s (t+u)) =
      step demand 0 (run demand (fun _ _ => 0) (run demand (fun _ _ => 0) s t) u)
    rw [ih]

theorem halted_run (demand : Nat) (s : State) (hv : s.support=0) (t : Nat) :
    run demand (fun _ _ => 0) s t = s := by
  induction t with
  | zero => rfl
  | succ t ih => rw [run,ih,loss_of_support_absorbing _ _ _ hv]

theorem no_investment_insufficient_response_eventually_halts (demand : Nat) (s : State)
    (hc : s.response < demand) :
    ∃ t, ∀ u, (run demand (fun _ _ => 0) s (t+u)).support=0 := by
  let t := s.response
  let z := run demand (fun _ _ => 0) s t
  have h := response_or_support_exhausted demand s hc t
  rcases h with h | h
  · refine ⟨t,?_⟩
    intro u
    rw [run_add,halted_run demand z h]
    exact h
  · have hz : z.response=0 := by
      change z.response ≤ s.response-s.response at h
      omega
    have hd : 1 ≤ demand := by omega
    have hm := Nat.mul_le_mul_right z.support hd
    have hm' : z.support ≤ demand*z.support := by simpa using hm
    have he : z = ⟨0,z.support⟩ := by
      calc z = ⟨z.response,z.support⟩ := rfl
           _ = ⟨0,z.support⟩ := by rw [hz]
    have stop : (run demand (fun _ _ => 0) z z.support).support=0 := by
      rw [he,zero_response_history]
      simp only
      omega
    refine ⟨t+z.support,?_⟩
    intro u
    rw [Nat.add_assoc,run_add,run_add,halted_run _ _ stop]
    exact stop

theorem exact_no_investment_viability (demand : Nat) (s : State) :
    (∀ t, 0 < (run demand (fun _ _ => 0) s t).support) ↔
      0 < s.support ∧ demand ≤ s.response := by
  constructor
  · intro h
    have hv : 0 < s.support := h 0
    constructor
    · exact hv
    · by_cases hc : demand ≤ s.response
      · exact hc
      · obtain ⟨t,ht⟩ := no_investment_insufficient_response_eventually_halts demand s (by omega)
        have hzero := ht 0
        have hpos := h t
        simp only [Nat.add_zero] at hzero
        omega
  · rintro ⟨hv,hc⟩ t
    rw [full_response_history demand s hv hc t]
    simp only
    omega

theorem next_support_positive_iff (demand investment : Nat) (s : State) (hv : 0 < s.support) :
    0 < (step demand investment s).support ↔
      missed demand s.response+investment < s.support+min demand s.response := by
  have hn : ¬s.support=0 := by omega
  simp only [step,hn,↓reduceIte]
  omega

theorem one_step_recovery_iff (demand : Nat) (s : State)
    (hv : 0 < s.support) (hc : s.response < demand) :
    (∃ investment, investment ≤ s.support ∧
      0 < (step demand investment s).support ∧
      demand ≤ (step demand investment s).response) ↔
    missed demand s.response ≤ s.support ∧
      2*missed demand s.response < s.support+s.response := by
  have hn : ¬s.support=0 := by omega
  have hmin : min demand s.response=s.response := by omega
  simp only [step,hn,↓reduceIte,hmin,missed]
  constructor
  · rintro ⟨i,hi,hv',hc'⟩
    omega
  · rintro ⟨hi,hbudget⟩
    refine ⟨demand-s.response,hi,?_⟩
    constructor <;> omega

theorem initial_investment_is_affordable : 1 ≤ (⟨2,2⟩ : State).support := by decide

theorem greedy_example_halted_forever (t : Nat) :
    run 3 (fun _ _ => 0) ⟨2,2⟩ (3+t) = ⟨0,0⟩ := by
  rw [run_add,constant_demand_greedy_collapse]
  exact halted_run 3 ⟨0,0⟩ rfl t

theorem expansion_margin (demand addedDemand addedResponse : Nat) (s : State)
    (hv : 0 < s.support) (hc : demand ≤ s.response) :
    (∀ t, 0 < (run (demand+addedDemand) (fun _ _ => 0)
      ⟨s.response+addedResponse,s.support⟩ t).support) ↔
      addedDemand ≤ (s.response-demand)+addedResponse := by
  rw [exact_no_investment_viability]
  simp only
  omega

theorem greater_response_with_greater_demands_can_halt :
    (∀ t, 0 < (run 3 (fun _ _ => 0) ⟨3,2⟩ t).support) ∧
    (∃ t, ∀ u, (run 5 (fun _ _ => 0) ⟨4,2⟩ (t+u)).support=0) := by
  constructor
  · exact (exact_no_investment_viability 3 ⟨3,2⟩).mpr (by decide)
  · exact no_investment_insufficient_response_eventually_halts 5 ⟨4,2⟩ (by decide)

def LocallyOptimal (demand : Nat) (policy : Nat → State → Nat) (s : State) : Prop :=
  ∀ t, let x := run demand policy s t
    policy t x ≤ x.support ∧ ∀ i, i ≤ x.support →
      (step demand i x).support ≤ (step demand (policy t x) x).support

theorem no_investment_locally_optimal (demand : Nat) (s : State) :
    LocallyOptimal demand (fun _ _ => 0) s := by
  intro t
  constructor
  · exact Nat.zero_le _
  · intro i _
    exact immediate_support_prefers_no_investment _ _ _

theorem optimal_live_step_uses_zero_investment (demand investment : Nat) (s : State)
    (hv : 0 < (step demand investment s).support)
    (hbest : (step demand 0 s).support ≤ (step demand investment s).support) :
    investment=0 := by
  by_cases hz : s.support=0
  · simp [step,hz] at hv
  · simp only [step,hz,↓reduceIte] at hv hbest
    omega

theorem optimal_live_history_matches_greedy (demand : Nat) (policy : Nat → State → Nat) (s : State)
    (hopt : LocallyOptimal demand policy s) (t : Nat)
    (hv : 0 < (run demand policy s t).support) :
    run demand policy s t = run demand (fun _ _ => 0) s t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    let x := run demand policy s t
    have hbest := (hopt t).2 0 (Nat.zero_le _)
    have hi := optimal_live_step_uses_zero_investment demand (policy t x) x hv hbest
    have hx : 0 < x.support := by
      by_cases hz : x.support=0
      · change 0 < (step demand (policy t x) x).support at hv
        rw [loss_of_support_absorbing demand (policy t x) x hz] at hv
        omega
      · omega
    have he := ih hx
    change step demand (policy t x) x = step demand 0 (run demand (fun _ _ => 0) s t)
    rw [hi]
    exact congrArg (step demand 0) he

theorem any_policy_failure_persists (demand : Nat) (policy : Nat → State → Nat) (s : State)
    (t : Nat) (hv : (run demand policy s t).support=0) (u : Nat) :
    run demand policy s (t+u) = run demand policy s t := by
  induction u with
  | zero => simp
  | succ u ih =>
    change step demand (policy (t+u) (run demand policy s (t+u)))
      (run demand policy s (t+u)) = run demand policy s t
    rw [ih,loss_of_support_absorbing _ _ _ hv]

theorem all_locally_optimal_policies_eventually_halt (demand : Nat)
    (policy : Nat → State → Nat) (s : State)
    (hopt : LocallyOptimal demand policy s) (hc : s.response < demand) :
    ∃ t, ∀ u, (run demand policy s (t+u)).support=0 := by
  obtain ⟨t,ht⟩ := no_investment_insufficient_response_eventually_halts demand s hc
  have hz : (run demand policy s t).support=0 := by
    by_cases hv : 0 < (run demand policy s t).support
    · have he := optimal_live_history_matches_greedy demand policy s hopt t hv
      have hh := ht 0
      rw [he] at hv
      simp only [Nat.add_zero] at hh
      omega
    · omega
  refine ⟨t,?_⟩
  intro u
  rw [any_policy_failure_persists demand policy s t hz u]
  exact hz

end ResponseCapacity
