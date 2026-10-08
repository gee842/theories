import CollectiveDestruction

/-! Conditional population allocation with an internally financed correction
reserve. Repertoire, realized receipts, response law and renewal remain supplied.
Contracts operate, contribute and affect shared capacity before revisions govern
the next generation. No repeated-game optimality claim is made. -/
namespace PopulationCorrection

structure State where
  renewing : Nat
  reserve : Nat
  capacity : Nat
  deriving DecidableEq, Repr

def funded (fee : Nat) (s : State) : Bool := decide (fee ≤ s.reserve)

def payoff (active : Bool) (others : Int) (race : Bool) : Int :=
  6 + CollectiveDestruction.utility 2 1 (if active then 3 else 0) others race

theorem locally_optimal_revision (active : Bool) (others : Int) (a : Bool) :
    payoff active others a ≤ payoff active others (!active) := by
  cases active <;> cases a <;> simp [payoff, CollectiveDestruction.utility] <;> omega

theorem strict_revision_advantage (active : Bool) (others : Int) :
    payoff active others active < payoff active others (!active) := by
  cases active <;> simp [payoff, CollectiveDestruction.utility] <;> omega

theorem unprotected_collective_loss (N : Nat) (hN : 3 ≤ N) :
    payoff false ((N : Int) - 1) true < payoff false 0 false := by
  simp [payoff, CollectiveDestruction.utility]
  omega

def allocated (N k : Nat) (active : Bool) (r : Nat) : Nat :=
  if active then min N (r + k) else r - k

def inflow (N : Nat) (active : Bool) (r : Nat) : Nat :=
  r + if active then 3 * (N - r) else 0

def next (N fee cap k : Nat) (s : State) : State :=
  let active := funded fee s
  { renewing := allocated N k active s.renewing
    reserve := min fee (s.reserve - (if active then fee else 0) +
      inflow N active s.renewing)
    capacity := min cap (s.capacity + s.renewing - (N - s.renewing)) }

def history (N fee cap : Nat) (k : Nat → Nat) (s : State) : Nat → State
  | 0 => s
  | t + 1 => next N fee cap (k t) (history N fee cap k s t)

theorem unfunded_step (N fee cap k : Nat) (s : State) (h : s.reserve < fee) :
    next N fee cap k s =
      ⟨s.renewing-k, min fee (s.reserve+s.renewing),
        min cap (s.capacity+s.renewing-(N-s.renewing))⟩ := by
  have hn : ¬fee ≤ s.reserve := by omega
  simp [next, funded, hn, allocated, inflow]

theorem funded_step (N fee cap k : Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) (hb : fee ≤ s.reserve) :
    next N fee cap k s =
      ⟨min N (s.renewing+k), fee,
        min cap (s.capacity+s.renewing-(N-s.renewing))⟩ := by
  have hi : fee ≤ s.reserve-fee+s.renewing+3*(N-s.renewing) := by omega
  simp only [next, funded, hb, decide_true, allocated, ↓reduceIte,
    inflow]
  congr 1
  omega

theorem count_bound (N fee cap k : Nat) (s : State) (hr : s.renewing ≤ N) :
    (next N fee cap k s).renewing ≤ N := by
  simp only [next, allocated]
  split <;> omega

theorem count_history (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hr : s.renewing ≤ N) (t : Nat) : (history N fee cap k s t).renewing ≤ N := by
  induction t with
  | zero => exact hr
  | succ t ih => exact count_bound _ _ _ _ _ ih

theorem revision_quota (N k : Nat) (active : Bool) (r : Nat) (hr : r ≤ N) :
    r - k ≤ allocated N k active r ∧ allocated N k active r ≤ r + k := by
  cases active <;> simp [allocated] <;> omega

def slotAction (r i : Nat) : Bool := decide (r ≤ i)

theorem revised_slot_is_optimal (N k r i : Nat) (active : Bool) (others : Int)
    (hi : i < N)
    (changed : slotAction r i ≠ slotAction (allocated N k active r) i) (a : Bool) :
    payoff active others a ≤ payoff active others (slotAction (allocated N k active r) i) := by
  have chosen : slotAction (allocated N k active r) i = !active := by
    cases active <;> simp_all [slotAction,allocated] <;> omega
  rw [chosen]
  exact locally_optimal_revision _ _ _

theorem correction_stays_funded (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) (hb : fee ≤ s.reserve) (t : Nat) :
    fee ≤ (history N fee cap k s t).reserve := by
  induction t with
  | zero => exact hb
  | succ t ih =>
    rw [history, funded_step _ _ _ _ _ (count_history _ _ _ _ _ hr _) hf ih]
    exact Nat.le_refl _

def triangle : Nat → Nat
  | 0 => 0
  | n+1 => triangle n + (n+1)

theorem triangle_drop (r : Nat) : triangle (r-1) + r = triangle r := by
  cases r <;> simp [triangle]

theorem triangle_monotone (a b : Nat) (h : a ≤ b) : triangle a ≤ triangle b := by
  induction b generalizing a with
  | zero =>
    have ha : a = 0 := by omega
    subst a
    exact Nat.le_refl _
  | succ b ih =>
    cases a with
    | zero => simp [triangle]
    | succ a =>
      have hh := ih a (by omega)
      simp only [triangle]
      omega

theorem contribution_upper_bound (r k : Nat) (hk : 1 ≤ k) :
    r + triangle (r-k) ≤ triangle r := by
  have h := triangle_monotone (r-k) (r-1) (by omega)
  have d := triangle_drop r
  omega

def Doomed (fee : Nat) (s : State) : Prop := s.reserve + triangle s.renewing < fee

theorem doom_step (N fee cap k : Nat) (s : State) (hk : 1 ≤ k)
    (hd : Doomed fee s) : Doomed fee (next N fee cap k s) := by
  have hb : s.reserve < fee := by unfold Doomed at hd; omega
  rw [unfunded_step _ _ _ _ _ hb]
  have ht := contribution_upper_bound s.renewing k hk
  unfold Doomed at *
  simp only
  omega

theorem doom_history (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hk : ∀ t, 1 ≤ k t) (hd : Doomed fee s) (t : Nat) :
    Doomed fee (history N fee cap k s t) := by
  induction t with
  | zero => exact hd
  | succ t ih => exact doom_step _ _ _ _ _ (hk t) ih

theorem doomed_replacement_bound (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hk : ∀ t, 1 ≤ k t) (hd : Doomed fee s) (t : Nat) :
    (history N fee cap k s t).renewing ≤ s.renewing - t := by
  induction t with
  | zero => simp [history]
  | succ t ih =>
    have hh := doom_history N fee cap k s hk hd t
    have hb : (history N fee cap k s t).reserve < fee := by unfold Doomed at hh; omega
    rw [history, unfunded_step _ _ _ _ _ hb]
    have ht := hk t
    simp only
    omega

theorem funded_replacement_bound (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hk : ∀ t, 1 ≤ k t) (hr : s.renewing ≤ N) (hf : fee ≤ N)
    (hb : fee ≤ s.reserve) (t : Nat) :
    min N (s.renewing + t) ≤ (history N fee cap k s t).renewing := by
  induction t with
  | zero => simp [history]; omega
  | succ t ih =>
    rw [history, funded_step _ _ _ _ _ (count_history _ _ _ _ _ hr _) hf
      (correction_stays_funded _ _ _ _ _ hr hf hb _)]
    have ht := hk t
    simp only
    omega

theorem funded_full_population (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hk : ∀ t, 1 ≤ k t) (hr : s.renewing ≤ N) (hf : fee ≤ N)
    (hb : fee ≤ s.reserve) (t : Nat) (ht : N ≤ t) :
    (history N fee cap k s t).renewing = N := by
  have a := funded_replacement_bound N fee cap k s hk hr hf hb t
  have b := count_history N fee cap k s hr t
  omega

theorem potential_preserved_at_unit_speed (N fee cap : Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N)
    (hp : fee ≤ s.reserve + triangle s.renewing) :
    fee ≤ (next N fee cap 1 s).reserve + triangle (next N fee cap 1 s).renewing := by
  by_cases hb : fee ≤ s.reserve
  · rw [funded_step _ _ _ _ _ hr hf hb]
    simp only
    omega
  · rw [unfunded_step _ _ _ _ _ (by omega)]
    have hd := triangle_drop s.renewing
    simp only
    omega

theorem potential_unit_history (N fee cap : Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N)
    (hp : fee ≤ s.reserve + triangle s.renewing) (t : Nat) :
    fee ≤ (history N fee cap (fun _ => 1) s t).reserve +
      triangle (history N fee cap (fun _ => 1) s t).renewing := by
  induction t with
  | zero => exact hp
  | succ t ih =>
    exact potential_preserved_at_unit_speed _ _ _ _ (count_history _ _ _ _ _ hr _) hf ih

theorem funded_or_replacement_bound (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hk : ∀ t, 1 ≤ k t) (hr : s.renewing ≤ N) (hf : fee ≤ N) (t : Nat) :
    fee ≤ (history N fee cap k s t).reserve ∨
      (history N fee cap k s t).renewing ≤ s.renewing-t := by
  induction t with
  | zero => exact Or.inr (by simp [history])
  | succ t ih =>
    by_cases hb : fee ≤ (history N fee cap k s t).reserve
    · rw [history, funded_step _ _ _ _ _ (count_history _ _ _ _ _ hr _) hf hb]
      exact Or.inl (Nat.le_refl _)
    · have h := ih.resolve_left hb
      rw [history, unfunded_step _ _ _ _ _ (by omega)]
      have hh := hk t
      exact Or.inr (by simp only; omega)

theorem unit_speed_activation (N fee cap : Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N)
    (hp : fee ≤ s.reserve + triangle s.renewing) :
    fee ≤ (history N fee cap (fun _ => 1) s s.renewing).reserve := by
  have h := funded_or_replacement_bound N fee cap (fun _ => 1) s (by intro t; exact Nat.le_refl 1) hr hf s.renewing
  rcases h with h | h
  · exact h
  · have hz : (history N fee cap (fun _ => 1) s s.renewing).renewing = 0 := by omega
    have hp := potential_unit_history N fee cap s hr hf hp s.renewing
    simpa [hz, triangle] using hp

theorem exact_unit_speed_activation_boundary (N fee cap : Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) :
    (∃ t, fee ≤ (history N fee cap (fun _ => 1) s t).reserve) ↔
      fee ≤ s.reserve + triangle s.renewing := by
  constructor
  · rintro ⟨t,ht⟩
    by_cases hp : fee ≤ s.reserve + triangle s.renewing
    · exact hp
    · have hd : Doomed fee s := by unfold Doomed; omega
      have hh := doom_history N fee cap (fun _ => 1) s (by intro t; exact Nat.le_refl 1) hd t
      unfold Doomed at hh
      omega
  · intro hp
    exact ⟨s.renewing, unit_speed_activation N fee cap s hr hf hp⟩

def topup (fee extra : Nat) (s : State) : State :=
  {s with reserve := min fee (s.reserve+extra)}

theorem exact_unit_speed_topup (N fee cap extra : Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) :
    (∃ t, fee ≤ (history N fee cap (fun _ => 1) (topup fee extra s) t).reserve) ↔
      fee - (s.reserve + triangle s.renewing) ≤ extra := by
  rw [exact_unit_speed_activation_boundary N fee cap (topup fee extra s) hr hf]
  simp only [topup]
  omega

theorem history_add (N fee cap : Nat) (k : Nat → Nat) (s : State) (t u : Nat) :
    history N fee cap k s (t+u) =
      history N fee cap (fun j => k (t+j)) (history N fee cap k s t) u := by
  induction u with
  | zero => simp [history]
  | succ u ih => simp [history, ih]

theorem extinct_unfunded_history (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hr : s.renewing = 0) (hb : s.reserve < fee) (t : Nat) :
    (history N fee cap k s t).renewing = 0 ∧
    (history N fee cap k s t).reserve = s.reserve ∧
    (history N fee cap k s t).capacity ≤ s.capacity-t := by
  induction t with
  | zero => simp [history, hr]
  | succ t ih =>
    have hh : (history N fee cap k s t).reserve < fee := by omega
    rw [history, unfunded_step _ _ _ _ _ hh]
    simp only [ih.1, Nat.zero_sub, Nat.add_zero, Nat.sub_zero]
    constructor
    · trivial
    constructor
    · omega
    · have := ih.2.2
      omega

theorem destructive_region_reached (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hk : ∀ t, 1 ≤ k t) (hd : Doomed fee s) :
    ∃ t, ∀ u, (history N fee cap k s (t+u)).renewing = 0 ∧
      (history N fee cap k s (t+u)).reserve < fee ∧
      (history N fee cap k s (t+u)).capacity = 0 := by
  let t := s.renewing
  let z := history N fee cap k s t
  have hz : z.renewing = 0 := by
    have := doomed_replacement_bound N fee cap k s hk hd t
    change z.renewing ≤ s.renewing - t at this
    have htt : t = s.renewing := rfl
    omega
  have hb : z.reserve < fee := by
    have hh := doom_history N fee cap k s hk hd t
    change z.reserve + triangle z.renewing < fee at hh
    omega
  refine ⟨t+z.capacity, ?_⟩
  intro u
  rw [Nat.add_assoc, history_add]
  have h := extinct_unfunded_history N fee cap (fun j => k (t+j)) z hN hz hb (z.capacity+u)
  have hb2 : (history N fee cap (fun j => k (t+j)) z (z.capacity+u)).reserve < fee := by
    rw [h.2.1]
    exact hb
  have hv : (history N fee cap (fun j => k (t+j)) z (z.capacity+u)).capacity = 0 := by
    have := h.2.2
    omega
  exact ⟨h.1,hb2,hv⟩

theorem full_renewing_history (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hf : fee ≤ N) (hr : s.renewing = N)
    (hb : fee ≤ s.reserve) (t : Nat) :
    (history N fee cap k s t).renewing = N ∧
    fee ≤ (history N fee cap k s t).reserve ∧
    min cap (s.capacity+t) ≤ (history N fee cap k s t).capacity := by
  induction t with
  | zero => simp [history,hr]; omega
  | succ t ih =>
    rw [history, funded_step _ _ _ _ _ (by omega) hf ih.2.1]
    simp only [ih.1, Nat.sub_self, Nat.sub_zero]
    constructor
    · omega
    constructor
    · exact Nat.le_refl _
    · have := ih.2.2
      omega

theorem funded_constructive_region_reached (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hf : fee ≤ N) (hr : s.renewing ≤ N)
    (hk : ∀ t, 1 ≤ k t) (hb : fee ≤ s.reserve) :
    ∃ t, ∀ u, (history N fee cap k s (t+u)).renewing = N ∧
      fee ≤ (history N fee cap k s (t+u)).reserve ∧
      cap ≤ (history N fee cap k s (t+u)).capacity := by
  let z := history N fee cap k s N
  have hz : z.renewing = N := funded_full_population N fee cap k s hk hr hf hb N (by omega)
  have hbz : fee ≤ z.reserve := correction_stays_funded N fee cap k s hr hf hb N
  refine ⟨N+cap, ?_⟩
  intro u
  rw [Nat.add_assoc, history_add]
  have h := full_renewing_history N fee cap (fun j => k (N+j)) z hN hf hz hbz (cap+u)
  have hv : cap ≤ (history N fee cap (fun j => k (N+j)) z (cap+u)).capacity := by
    have := h.2.2
    omega
  exact ⟨h.1,h.2.1,hv⟩

def exampleStart : State := ⟨3, 0, 12⟩

theorem slow_bootstraps : (history 6 6 12 (fun _ => 1) exampleStart 3).reserve = 6 := by decide

theorem growth_closes_bootstrap :
    history 6 6 12 (fun t => t+1) exampleStart 2 = ⟨0,5,10⟩ := by decide

theorem growth_eventually_destructive :
    ∀ u, (history 6 6 12 (fun t => t+1) exampleStart (4+u)).renewing = 0 ∧
      (history 6 6 12 (fun t => t+1) exampleStart (4+u)).capacity = 0 := by
  intro u
  have h4 : history 6 6 12 (fun t => t+1) exampleStart 4 = ⟨0,5,0⟩ := by decide
  rw [history_add, h4]
  have h := extinct_unfunded_history 6 6 12 (fun j => 4+j+1) ⟨0,5,0⟩
    (by decide) rfl (by decide) u
  have hv : (history 6 6 12 (fun j => 4+j+1) ⟨0,5,0⟩ u).capacity = 0 := by
    have hc := h.2.2
    change _ ≤ 0-u at hc
    omega
  exact ⟨h.1,hv⟩

theorem speed_one_eventually_constructive :
    ∃ t, ∀ u, (history 6 6 12 (fun _ => 1) exampleStart (t+u)).renewing = 6 ∧
      12 ≤ (history 6 6 12 (fun _ => 1) exampleStart (t+u)).capacity := by
  let z := history 6 6 12 (fun _ => 1) exampleStart 3
  have hz : z.renewing ≤ 6 := count_history _ _ _ _ _ (by decide) _
  obtain ⟨t,ht⟩ := funded_constructive_region_reached 6 6 12 (fun _ => 1) z
    (by decide) (by decide) hz (by intro t; exact Nat.le_refl 1) (by change 6 ≤ (history 6 6 12 (fun _ => 1) exampleStart 3).reserve; rw [slow_bootstraps]; exact Nat.le_refl 6)
  refine ⟨3+t, ?_⟩
  intro u
  rw [Nat.add_assoc, history_add]
  exact ⟨(ht u).1,(ht u).2.2⟩

/- The unprotected continuation is a counterfactual ledger, not an additional
physical process. It determines how much can reach the first funding event. -/
def offCount (k : Nat → Nat) (r : Nat) : Nat → Nat
  | 0 => r
  | t+1 => offCount k r t - k t

def available (k : Nat → Nat) (r : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => available k r t + offCount k r t

theorem faster_replacement_reduces_contributors (slow fast : Nat → Nat) (r t : Nat)
    (hk : ∀ j, slow j ≤ fast j) : offCount fast r t ≤ offCount slow r t := by
  induction t with
  | zero => exact Nat.le_refl _
  | succ t ih =>
    have h := hk t
    simp only [offCount]
    omega

theorem faster_replacement_reduces_available (slow fast : Nat → Nat) (r t : Nat)
    (hk : ∀ j, slow j ≤ fast j) : available fast r t ≤ available slow r t := by
  induction t with
  | zero => exact Nat.le_refl _
  | succ t ih =>
    have h := faster_replacement_reduces_contributors slow fast r t hk
    simp only [available]
    omega

theorem off_count_bound (k : Nat → Nat) (r : Nat) (hk : ∀ t, 1 ≤ k t) (t : Nat) :
    offCount k r t ≤ r-t := by
  induction t with
  | zero => simp [offCount]
  | succ t ih => have h := hk t; simp only [offCount]; omega

theorem unit_count (r t : Nat) : offCount (fun _ => 1) r t = r-t := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [offCount,ih]; omega

theorem unit_ledger_conservation (r t : Nat) :
    available (fun _ => 1) r t + triangle (offCount (fun _ => 1) r t) = triangle r := by
  induction t with
  | zero => simp [available,offCount]
  | succ t ih =>
    have h := triangle_drop (offCount (fun _ => 1) r t)
    simp only [available,offCount]
    omega

theorem unit_available_is_triangle (r : Nat) :
    available (fun _ => 1) r r = triangle r := by
  have h := unit_ledger_conservation r r
  simpa [unit_count,triangle] using h

theorem available_monotone (k : Nat → Nat) (r a b : Nat) (h : a ≤ b) :
    available k r a ≤ available k r b := by
  induction b generalizing a with
  | zero =>
    have ha : a = 0 := by omega
    subst a
    exact Nat.le_refl _
  | succ b ih =>
    by_cases he : a = b+1
    · subst a; exact Nat.le_refl _
    · have hh := ih a (by omega)
      simp only [available]
      omega

theorem contributions_stop (k : Nat → Nat) (r : Nat) (hk : ∀ t, 1 ≤ k t) (u : Nat) :
    available k r (r+u) = available k r r := by
  induction u with
  | zero => simp
  | succ u ih =>
    have hz : offCount k r (r+u) = 0 := by
      have := off_count_bound k r hk (r+u)
      omega
    simp [available,ih,hz]

theorem contributions_bounded (k : Nat → Nat) (r : Nat) (hk : ∀ t, 1 ≤ k t) (t : Nat) :
    available k r t ≤ available k r r := by
  by_cases h : t ≤ r
  · exact available_monotone k r t r h
  · have he : t = r+(t-r) := by omega
    rw [he,contributions_stop k r hk (t-r)]
    exact Nat.le_refl _

theorem actual_or_unfunded_ledger (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) (t : Nat) :
    (fee ≤ (history N fee cap k s t).reserve ∧ fee ≤ s.reserve+available k s.renewing t) ∨
    ((history N fee cap k s t).reserve = s.reserve+available k s.renewing t ∧
     (history N fee cap k s t).renewing = offCount k s.renewing t ∧
     s.reserve+available k s.renewing t < fee) := by
  induction t with
  | zero =>
    by_cases h : fee ≤ s.reserve
    · exact Or.inl (by simpa [history,available] using And.intro h h)
    · exact Or.inr (by simp [history,available,offCount]; omega)
  | succ t ih =>
    rcases ih with h | h
    · rw [history,funded_step _ _ _ _ _ (count_history _ _ _ _ _ hr _) hf h.1]
      apply Or.inl
      constructor
      · exact Nat.le_refl _
      · simp only [available]
        omega
    · have hb : (history N fee cap k s t).reserve < fee := by omega
      rw [history,unfunded_step _ _ _ _ _ hb]
      simp only [h.1,h.2.1,available,offCount]
      by_cases enough : fee ≤ s.reserve+available k s.renewing t+offCount k s.renewing t
      · apply Or.inl
        constructor <;> omega
      · apply Or.inr
        constructor
        · omega
        constructor
        · trivial
        · omega

theorem funding_iff_ledger (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) (t : Nat) :
    fee ≤ (history N fee cap k s t).reserve ↔ fee ≤ s.reserve+available k s.renewing t := by
  have h := actual_or_unfunded_ledger N fee cap k s hr hf t
  rcases h with h | h
  · constructor <;> intro; exact h.2; exact h.1
  · constructor <;> intro hh <;> omega

theorem exact_schedule_activation_boundary (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) (hk : ∀ t, 1 ≤ k t) :
    (∃ t, fee ≤ (history N fee cap k s t).reserve) ↔
      fee ≤ s.reserve+available k s.renewing s.renewing := by
  constructor
  · rintro ⟨t,ht⟩
    have hl := (funding_iff_ledger N fee cap k s hr hf t).mp ht
    have hu := contributions_bounded k s.renewing hk t
    omega
  · intro h
    exact ⟨s.renewing,(funding_iff_ledger N fee cap k s hr hf s.renewing).mpr h⟩

theorem exact_schedule_topup (N fee cap extra : Nat) (k : Nat → Nat) (s : State)
    (hr : s.renewing ≤ N) (hf : fee ≤ N) (hk : ∀ t, 1 ≤ k t) :
    (∃ t, fee ≤ (history N fee cap k (topup fee extra s) t).reserve) ↔
      fee-(s.reserve+available k s.renewing s.renewing) ≤ extra := by
  rw [exact_schedule_activation_boundary N fee cap k (topup fee extra s) hr hf hk]
  simp only [topup]
  omega

theorem schedule_shortfall_is_destructive (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hr : s.renewing ≤ N) (hf : fee ≤ N) (hk : ∀ t, 1 ≤ k t)
    (shortfall : s.reserve+available k s.renewing s.renewing < fee) :
    ∃ t, ∀ u, (history N fee cap k s (t+u)).renewing = 0 ∧
      (history N fee cap k s (t+u)).reserve < fee ∧
      (history N fee cap k s (t+u)).capacity = 0 := by
  let start := s.renewing
  let z := history N fee cap k s start
  have hl := actual_or_unfunded_ledger N fee cap k s hr hf start
  have low : z.reserve = s.reserve+available k s.renewing start ∧
      z.renewing = offCount k s.renewing start ∧
      s.reserve+available k s.renewing start < fee := by
    rcases hl with h | h
    · have hs : s.reserve+available k s.renewing start < fee := shortfall
      omega
    · exact h
  have hz : z.renewing = 0 := by
    have h := off_count_bound k s.renewing hk start
    have he : start = s.renewing := rfl
    omega
  have hb : z.reserve < fee := by omega
  have hd : Doomed fee z := by unfold Doomed; simp [hz,triangle]; exact hb
  obtain ⟨t,ht⟩ := destructive_region_reached N fee cap (fun j => k (start+j)) z
    hN (by intro j; exact hk (start+j)) hd
  refine ⟨start+t, ?_⟩
  intro u
  rw [Nat.add_assoc,history_add]
  exact ht u

theorem schedule_sufficiency_is_constructive (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hr : s.renewing ≤ N) (hf : fee ≤ N) (hk : ∀ t, 1 ≤ k t)
    (enough : fee ≤ s.reserve+available k s.renewing s.renewing) :
    ∃ t, ∀ u, (history N fee cap k s (t+u)).renewing = N ∧
      fee ≤ (history N fee cap k s (t+u)).reserve ∧
      cap ≤ (history N fee cap k s (t+u)).capacity := by
  let start := s.renewing
  let z := history N fee cap k s start
  have hz : z.renewing ≤ N := count_history N fee cap k s hr start
  have hb : fee ≤ z.reserve := (funding_iff_ledger N fee cap k s hr hf start).mpr enough
  obtain ⟨t,ht⟩ := funded_constructive_region_reached N fee cap (fun j => k (start+j)) z
    hN hf hz (by intro j; exact hk (start+j)) hb
  refine ⟨start+t, ?_⟩
  intro u
  rw [Nat.add_assoc,history_add]
  exact ht u

theorem post_step_bounds (N fee cap : Nat) (k : Nat → Nat) (s : State) (t : Nat) :
    (history N fee cap k s (t+1)).reserve ≤ fee ∧
    (history N fee cap k s (t+1)).capacity ≤ cap := by
  simp only [history,next]
  constructor <;> exact Nat.min_le_left _ _

theorem schedule_sufficiency_reaches_full_state (N fee cap : Nat) (k : Nat → Nat) (s : State)
    (hN : 1 ≤ N) (hr : s.renewing ≤ N) (hf : fee ≤ N) (hk : ∀ t, 1 ≤ k t)
    (enough : fee ≤ s.reserve+available k s.renewing s.renewing) :
    ∃ t, ∀ u, history N fee cap k s (t+u) = ⟨N,fee,cap⟩ := by
  obtain ⟨t,ht⟩ := schedule_sufficiency_is_constructive N fee cap k s hN hr hf hk enough
  refine ⟨t+1, ?_⟩
  intro u
  have h := ht (u+1)
  have b := post_step_bounds N fee cap k s (t+u)
  have e : t+(u+1) = (t+u)+1 := by omega
  rw [e] at h
  have br : (history N fee cap k s ((t+u)+1)).reserve = fee := by omega
  have bc : (history N fee cap k s ((t+u)+1)).capacity = cap := by omega
  have e2 : t+1+u = (t+u)+1 := by omega
  rw [e2]
  cases hs : history N fee cap k s ((t+u)+1) with
  | mk r B v => simp_all

theorem destructive_region_absorbing (N fee cap k B : Nat) (hb : B < fee) :
    next N fee cap k ⟨0,B,0⟩ = ⟨0,B,0⟩ := by
  rw [unfunded_step _ _ _ _ _ hb]
  simp
  omega

theorem slow_recovery_has_real_loss :
    (history 6 6 12 (fun _ => 1) exampleStart 4).capacity = 0 := by decide

theorem boosted_growth_preserves_floor (t : Nat) :
    4 ≤ (history 6 6 12 (fun j => j+1) (topup 6 1 exampleStart) t).capacity := by
  by_cases h : t < 4
  · have ht : t=0 ∨ t=1 ∨ t=2 ∨ t=3 := by omega
    rcases ht with h | h | h | h <;> subst t <;> decide
  · have h4 : history 6 6 12 (fun j => j+1) (topup 6 1 exampleStart) 4 = ⟨6,6,4⟩ := by decide
    have ht : t = 4+(t-4) := by omega
    rw [ht,history_add,h4]
    have hh := full_renewing_history 6 6 12 (fun j => 4+j+1) ⟨6,6,4⟩
      (by decide) (by decide) rfl (by decide) (t-4)
    have hc := hh.2.2
    change min 12 (4+(t-4)) ≤ _ at hc
    omega

def grossReceipts (N r : Nat) : Nat := 7*r + 8*(N-r)
def privateReceipts (N r : Nat) (active : Bool) : Nat :=
  6*r + (if active then 5 else 8)*(N-r)
def expenditure (fee : Nat) (s : State) : Nat := if funded fee s then fee else 0
def released (N fee : Nat) (s : State) : Nat :=
  (s.reserve-expenditure fee s+inflow N (funded fee s) s.renewing)-fee

theorem operating_receipts_accounted (N r : Nat) (active : Bool) :
    grossReceipts N r = privateReceipts N r active + inflow N active r := by
  cases active <;> simp [grossReceipts,privateReceipts,inflow] <;> omega

theorem private_receipts_cover_reconstruction (N r : Nat) (active : Bool) (hr : r ≤ N) :
    N ≤ privateReceipts N r active := by
  cases active <;> simp [privateReceipts] <;> omega

theorem treasury_accounted (N fee cap k : Nat) (s : State) :
    s.reserve + inflow N (funded fee s) s.renewing =
      expenditure fee s + (next N fee cap k s).reserve + released N fee s := by
  by_cases hb : fee ≤ s.reserve
  · simp [next,released,expenditure,funded,hb]
    omega
  · simp [next,released,expenditure,funded,hb]
    omega

def leakingNext (N fee cap k leak : Nat) (s : State) : State :=
  {next N fee cap k s with
    reserve := min fee (s.reserve-expenditure fee s+
      inflow N (funded fee s) s.renewing-leak)}

theorem exact_funded_leak_tolerance (N fee cap k leak : Nat) (s : State)
    (hfee : 0 < fee) (hb : s.reserve = fee) :
    fee ≤ (leakingNext N fee cap k leak s).reserve ↔
      fee + leak ≤ inflow N true s.renewing := by
  simp [leakingNext,expenditure,funded,hb]
  omega

theorem all_renewing_leak_tolerance (N fee cap k leak : Nat) (s : State)
    (hfee : 0 < fee) (hb : s.reserve = fee) (hr : s.renewing = N) :
    fee ≤ (leakingNext N fee cap k leak s).reserve ↔ fee + leak ≤ N := by
  rw [exact_funded_leak_tolerance N fee cap k leak s hfee hb]
  simp [inflow,hr]

theorem one_unit_diversion_breaks_zero_margin :
    (leakingNext 6 6 12 1 1 ⟨6,6,12⟩).reserve = 5 := by decide

/- Clearing the treasury is a matched alternative transition, not a theorem
that aligned controllers necessarily choose diversion. -/
def drainedNext (N fee cap k : Nat) (s : State) : State :=
  {next N fee cap k s with reserve := 0}

theorem identical_local_ordering_different_funding :
    (next 6 6 12 1 ⟨6,6,12⟩).renewing = (drainedNext 6 6 12 1 ⟨6,6,12⟩).renewing ∧
    (next 6 6 12 1 ⟨6,6,12⟩).reserve = 6 ∧
    (drainedNext 6 6 12 1 ⟨6,6,12⟩).reserve = 0 := by decide

def weightedDefectionValue : List Nat → List Bool → Int
  | [], _ => 0
  | w::ws, a::as => (w : Int)*CollectiveDestruction.payoff 0 a true + weightedDefectionValue ws as
  | _::_, [] => 0

theorem arbitrary_finite_horizon_defection (weights : List Nat) (actions : List Bool)
    (h : actions.length = weights.length) :
    weightedDefectionValue weights actions ≤
      weightedDefectionValue weights (List.replicate weights.length true) := by
  induction weights generalizing actions with
  | nil => simp [weightedDefectionValue]
  | cons w ws ih =>
    cases actions with
    | nil => simp at h
    | cons a as =>
      have hl : as.length = ws.length := by simpa using h
      have ht := ih as hl
      cases a <;>
        simp [weightedDefectionValue,CollectiveDestruction.payoff,
          CollectiveDestruction.utility,List.replicate_succ] at * <;>
        omega

end PopulationCorrection
