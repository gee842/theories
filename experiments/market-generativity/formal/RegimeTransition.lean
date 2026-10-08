import RegimeAttraction

namespace RegimeTransition
open MarketGenerativity RegimeBoundary RegimeAttraction

abbrev rescue := family 0
abbrev trajectory (s : OperatingState) := RegimeBoundary.history rescue s

theorem rescue_coordinates (s : OperatingState) (hs : physical s) :
    rescue s = (s.1+(4/5)*s.1*(1-s.1)*(s.2.1-3/8),
      (3/4)*s.2.1+1/4, (3/4)*s.2.2+(1/4)*(1-s.1)) := by
  have hq := quality_unclipped 0 s.2.1 s.2.2 (by decide +kernel)
    (by decide +kernel) hs.2.2.1 hs.2.2.2.1 hs.2.2.2.2.1 hs.2.2.2.2.2
  unfold rescue family step
  rw [hq]
  unfold shareStep influenceStep
  congr 1 <;> grind

theorem trajectory_physical (s : OperatingState) (hs : physical s) :
    ∀ n, physical (trajectory s n) := by
  intro n
  induction n with
  | zero => exact hs
  | succ n ih => exact family_physical 0 _ ih

theorem positive_share_step (s : OperatingState) (hs : physical s) (hx : 0 < s.1) :
    0 < (rescue s).1 := by
  have he := rescue_coordinates s hs
  rcases hs with ⟨hx0,hx1,hq0,hq1,hw0,hw1⟩
  have hprod := Rat.mul_nonneg (show 0 ≤ 1-s.1 by grind) hq0
  have hprod2 := Rat.mul_nonneg hx0 hprod
  have hsquare := Rat.mul_nonneg hx0 hx0
  have hb : (7/10)*s.1 ≤ (rescue s).1 := by rw [he]; dsimp; grind
  have hp := Rat.mul_pos (show (0 : Rat) < 7/10 by decide +kernel) hx
  grind

theorem positive_share_history (s : OperatingState) (hs : physical s) (hx : 0 < s.1) :
    ∀ n, 0 < (trajectory s n).1 := by
  intro n
  induction n with
  | zero => exact hx
  | succ n ih => exact positive_share_step _ (trajectory_physical s hs n) ih

theorem quality_lower (s : OperatingState) (hs : physical s) :
    ∀ n, 1-radius (3/4) 1 n ≤ (trajectory s n).2.1 := by
  intro n
  induction n with
  | zero => simp only [trajectory, RegimeBoundary.history, radius]; grind [physical]
  | succ n ih =>
    have he := rescue_coordinates _ (trajectory_physical s hs n)
    change 1-radius (3/4) 1 (n+1) ≤ (rescue (trajectory s n)).2.1
    rw [he]
    simp only [radius]
    grind

theorem history_shift (f : OperatingState → OperatingState) (s : OperatingState) (n : Nat) :
    ∀ k, RegimeBoundary.history f s (n+k) =
      RegimeBoundary.history f (RegimeBoundary.history f s n) k := by
  intro k
  induction k with
  | zero => rfl
  | succ k ih => simp [RegimeBoundary.history, ih]

def Ready (s : OperatingState) : Prop := physical s ∧ 1/2 ≤ s.2.1

theorem ready_step (s : OperatingState) (hs : Ready s) :
    Ready (rescue s) ∧ s.1 ≤ (rescue s).1 := by
  have he := rescue_coordinates s hs.1
  have hp := family_physical 0 s hs.1
  have hq := hs.2
  have hx1 := hs.1.2.1
  have hx := share_step_bounds s.1 (1/5) (4*(s.2.1-3/8))
    hs.1.1 hs.1.2.1 (by decide +kernel) (by grind) (by grind [physical, Ready])
  refine ⟨⟨hp,?_⟩,hx.1⟩
  rw [he]; dsimp; grind

theorem ready_history (s : OperatingState) (hs : Ready s) :
    ∀ n, Ready (trajectory s n) ∧ s.1 ≤ (trajectory s n).1 := by
  intro n
  induction n with
  | zero => exact ⟨hs,by change s.1 ≤ s.1; grind⟩
  | succ n ih =>
    have h := ready_step _ ih.1
    refine ⟨h.1,?_⟩
    change s.1 ≤ (rescue (trajectory s n)).1
    grind

theorem ready_after_three (s : OperatingState) (hs : physical s) :
    Ready (trajectory s 3) := by
  have h := quality_lower s hs 3
  have hr : radius (3/4) 1 3 = 27/64 := by decide +kernel
  rw [hr] at h
  exact ⟨trajectory_physical s hs 3,by grind⟩

theorem growth_below_target (s : OperatingState) (hs : Ready s) (hx : s.1 ≤ 7/8) :
    s.1+s.1/80 ≤ (rescue s).1 := by
  have he := rescue_coordinates s hs.1
  have hq := hs.2
  have hx0 := hs.1.1
  have hx1 := hs.1.2.1
  have h1 := Rat.mul_le_mul_of_nonneg_left (show (1/8 : Rat) ≤ 1-s.1 by grind) hs.1.1
  have h2 := Rat.mul_le_mul_of_nonneg_left (show (1/8 : Rat) ≤ s.2.1-3/8 by grind)
    (Rat.mul_nonneg hs.1.1 (show 0 ≤ 1-s.1 by grind))
  rw [he]; dsimp; grind

theorem positive_ready_reaches_target (s : OperatingState) (hs : Ready s) (hx : 0 < s.1) :
    ∃ n, 7/8 ≤ (trajectory s n).1 := by
  by_cases h : ∃ n, 7/8 ≤ (trajectory s n).1
  · exact h
  · have hall : ∀ n, (trajectory s n).1 < 7/8 := by
      intro n
      by_cases hn : 7/8 ≤ (trajectory s n).1
      · exact False.elim (h ⟨n,hn⟩)
      · grind
    have hlin : ∀ n : Nat, s.1+(n : Rat)*(s.1/80) ≤ (trajectory s n).1 := by
      intro n
      induction n with
      | zero => simp [trajectory, RegimeBoundary.history]; grind
      | succ n ih =>
        have hh := ready_history s hs n
        have hg := growth_below_target _ hh.1 (by have := hall n; grind)
        change s.1+((n+1 : Nat) : Rat)*(s.1/80) ≤ (rescue (trajectory s n)).1
        simp only [Rat.natCast_add, Rat.natCast_ofNat]
        grind
    obtain ⟨n,hn⟩ := rational_natural_bound (1/(s.1/80))
    have hlarge := (Rat.div_lt_iff (show 0 < s.1/80 by grind)).mp hn
    have hlo := hlin n
    have hhi := hall n
    grind

theorem influence_relaxes (s : OperatingState) (hs : Ready s) (hx : 7/8 ≤ s.1) :
    ∀ n, (trajectory s n).2.2 ≤ 1/8+radius (3/4) 1 n := by
  intro n
  induction n with
  | zero => simp only [trajectory, RegimeBoundary.history, radius]; grind [Ready, physical]
  | succ n ih =>
    have hh := ready_history s hs n
    have he := rescue_coordinates _ hh.1.1
    change (rescue (trajectory s n)).2.2 ≤ 1/8+radius (3/4) 1 (n+1)
    rw [he]
    simp only [radius]; grind

def Landing (s : OperatingState) : Prop :=
  physical s ∧ 3/4 ≤ s.1 ∧ 1/2 ≤ s.2.1 ∧ s.2.2 ≤ 1/4

theorem positive_seed_finite_landing (s : OperatingState) (hs : physical s) (hx : 0 < s.1) :
    ∃ n, Landing (trajectory s n) := by
  have hr := ready_after_three s hs
  have hp := positive_share_history s hs hx 3
  obtain ⟨n,hn⟩ := positive_ready_reaches_target _ hr hp
  have hready := (ready_history _ hr n).1
  obtain ⟨k,hk⟩ := radius_reaches_small (3/4) 1 (1/8)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)
  have hw := influence_relaxes _ hready hn k
  have hh := ready_history _ hready k
  have hc : Landing (trajectory (trajectory (trajectory s 3) n) k) := by
    exact ⟨hh.1.1,by grind,hh.1.2,by grind⟩
  refine ⟨3+n+k,?_⟩
  simpa only [trajectory, history_shift] using hc

def cover (cost : Rat) : Nat → Rat
  | 0 => 5
  | n+1 => (10/9)*(cover cost n+1+cost)

theorem cover_formula (cost : Rat) : ∀ n,
    cover cost n = (15+10*cost)*radius (10/9) 1 n-10*(1+cost) := by
  intro n
  induction n with
  | zero => simp only [cover, radius]; grind
  | succ n ih => simp only [cover, radius, ih]; grind

theorem cover_floor (cost : Rat) (hc : 0 ≤ cost) : ∀ n, 5 ≤ cover cost n := by
  intro n
  induction n with
  | zero => change (5 : Rat) ≤ 5; decide +kernel
  | succ n ih => simp only [cover]; grind

theorem cover_step (cost stock x : Rat) (n : Nat) (hc : 0 ≤ cost)
    (hx : 0 ≤ x) (hs : cover cost (n+1) ≤ stock) :
    cover cost n ≤ supportStep stock (1/10) 2 1 x 0 cost := by
  have hb := cover_floor cost hc n
  unfold cover at hs
  unfold supportStep
  grind

def pulseStock (cost : Rat) (s : OperatingState) (initial : Rat) : Nat → Rat
  | 0 => initial
  | n+1 => supportStep (pulseStock cost s initial n) (1/10) 2 1 (trajectory s n).1 0 cost

theorem remaining_cover (cost initial : Rat) (s : OperatingState) (N : Nat)
    (hc : 0 ≤ cost) (hs : physical s) (hi : cover cost N ≤ initial) :
    ∀ t, t ≤ N → cover cost (N-t) ≤ pulseStock cost s initial t := by
  intro t
  induction t with
  | zero => intro _; simpa only [Nat.sub_zero, pulseStock] using hi
  | succ t ih =>
    intro ht
    have hprev := ih (by omega)
    have hn : N-t = (N-(t+1))+1 := by omega
    rw [hn] at hprev
    exact cover_step cost _ _ (N-(t+1)) hc (trajectory_physical s hs t).1 hprev

def pulseParameters : Parameters 1 := { exampleParameters with beta := 0 }
def pulseDisturbance (cost : Rat) : Disturbance 1 := ⟨0,fun _ => cost⟩

theorem pulse_coupling_step (cost initial : Rat) (s : OperatingState) :
    operatingStep pulseParameters (lift s initial) (pulseDisturbance cost) =
      lift (rescue s) (supportStep initial (1/10) 2 1 s.1 0 cost) := by
  have hg := gap_correspondence 4 (3/8) s.2.1 (1/2) 2 (by decide +kernel)
  have hi : installed 1 1 = 1 := by decide +kernel
  have hb : reserveStep 1 1 1 3 = 1 := by decide +kernel
  unfold operatingStep pulseParameters exampleParameters lift rescue family step pulseDisturbance
  simp only [hg, hi, hb]

theorem pulse_coupling_history (cost initial : Rat) (s : OperatingState) :
    ∀ n, MarketGenerativity.history pulseParameters (lift s initial)
      (fun _ => pulseDisturbance cost) n = lift (trajectory s n) (pulseStock cost s initial n) := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [MarketGenerativity.history, ih, trajectory, RegimeBoundary.history, pulseStock]
    exact pulse_coupling_step cost _ _

theorem pulse_prefix_executes (cost initial : Rat) (s : OperatingState) (N : Nat)
    (hc : 0 ≤ cost) (hs : physical s) (hi : cover cost N ≤ initial) :
    ∀ t, t ≤ N → guardedHistory pulseParameters exampleBounds (lift s initial)
      (fun _ => pulseDisturbance cost) t =
        some (MarketGenerativity.history pulseParameters (lift s initial)
          (fun _ => pulseDisturbance cost) t) := by
  have hfloor : ∀ t, t ≤ N → essentialReady pulseParameters exampleBounds
      (MarketGenerativity.history pulseParameters (lift s initial) (fun _ => pulseDisturbance cost) t) := by
    intro t ht j _
    rw [pulse_coupling_history]
    have h := remaining_cover cost initial s N hc hs hi t ht
    have h5 := cover_floor cost hc (N-t)
    change 5 ≤ pulseStock cost s initial t
    grind
  intro t
  induction t with
  | zero => intro _; rfl
  | succ t ih =>
    intro ht
    have hp := ih (by omega)
    have hf := hfloor t (by omega)
    have hn := hfloor (t+1) ht
    simp only [MarketGenerativity.history] at hn
    simp only [guardedHistory, hp, guardedStep, MarketGenerativity.history, hf, hn, and_self, ↓reduceIte]

theorem landing_supplies_safety (s : OperatingState) (stock : Rat)
    (hs : Landing s) (hc : 5 ≤ stock) : Safe exampleParameters exampleBounds (lift s stock) := by
  rcases hs with ⟨⟨hx0,hx1,hq0,hq1,hw0,hw1⟩,hxl,hql,hwu⟩
  constructor
  · exact hxl
  · exact hx1
  · exact hql
  · exact hq1
  · exact hw0
  · exact hwu
  · change (1 : Rat) ≤ 1; decide +kernel
  · change (1 : Rat) ≤ 3; decide +kernel
  · intro _; exact hc

theorem supported_finite_transition (cost : Rat) (s : OperatingState)
    (hc : 0 ≤ cost) (hs : physical s) (hx : 0 < s.1) :
    ∃ N, ∀ initial, cover cost N ≤ initial →
      (∀ t, t ≤ N → guardedHistory pulseParameters exampleBounds (lift s initial)
        (fun _ => pulseDisturbance cost) t =
          some (MarketGenerativity.history pulseParameters (lift s initial)
            (fun _ => pulseDisturbance cost) t)) ∧
      (let arrived := MarketGenerativity.history pulseParameters (lift s initial)
          (fun _ => pulseDisturbance cost) N
       Safe exampleParameters exampleBounds arrived ∧
       ∀ k, guardedHistory exampleParameters exampleBounds arrived (fun _ => noShock) k =
         some (MarketGenerativity.history exampleParameters arrived (fun _ => noShock) k)) := by
  obtain ⟨N,hN⟩ := positive_seed_finite_landing s hs hx
  refine ⟨N,?_⟩
  intro initial hi
  refine ⟨pulse_prefix_executes cost initial s N hc hs hi,?_⟩
  dsimp only
  have hstock := remaining_cover cost initial s N hc hs hi N (by omega)
  have h5 : 5 ≤ pulseStock cost s initial N := by simpa [cover] using hstock
  have hsafe : Safe exampleParameters exampleBounds
      (MarketGenerativity.history pulseParameters (lift s initial) (fun _ => pulseDisturbance cost) N) := by
    rw [pulse_coupling_history]
    exact landing_supplies_safety _ _ hN h5
  refine ⟨hsafe,?_⟩
  apply safe_history_never_fails exampleParameters exampleBounds _ _ example_certificate hsafe
  intro t
  unfold Admissible exampleBounds noShock
  constructor
  · decide +kernel
  · intro _; change (0 : Rat) ≤ 1/2; decide +kernel

theorem zero_seed_never_lands (q w : Rat) :
    ∀ n, (trajectory (0,q,w) n).1 = 0 ∧ ¬ Landing (trajectory (0,q,w) n) := by
  have hz : ∀ n, (trajectory (0,q,w) n).1 = 0 := by
    intro n
    induction n with
    | zero => rfl
    | succ n ih =>
      change (family 0 (trajectory (0,q,w) n)).1 = 0
      unfold family step shareStep
      rw [ih]
      simp
      grind
  intro n
  exact ⟨hz n,by have := hz n; unfold Landing; grind⟩

theorem too_late_even_without_extra_cost :
    physical (1/100,1/3,1) ∧ (0 : Rat) < 1/100 ∧
    guardedHistory pulseParameters exampleBounds (lift (1/100,1/3,1) 5)
      (fun _ => pulseDisturbance 0) 1 = none := by
  refine ⟨?_,by decide +kernel,?_⟩
  · unfold physical; decide +kernel
  · have hb : ¬ essentialReady pulseParameters exampleBounds
        (operatingStep pulseParameters (lift (1/100,1/3,1) 5) (pulseDisturbance 0)) := by
      intro h
      have hh := h 0 (by rfl)
      have he : (operatingStep pulseParameters (lift (1/100,1/3,1) 5)
        (pulseDisturbance 0)).stock 0 = 353/100 := by decide +kernel
      change (5 : Rat) ≤ _ at hh
      rw [he] at hh
      have hn : ¬ (5 : Rat) ≤ 353/100 := by decide +kernel
      exact hn hh
    simp only [guardedHistory, guardedStep]
    simp [hb]

theorem share_growth_upper (s : OperatingState) (hs : physical s) :
    (rescue s).1 ≤ (3/2)*s.1 := by
  rcases hs with ⟨hx0,hx1,hq0,hq1,hw0,hw1⟩
  have h := Rat.mul_le_mul_of_nonneg_left (show s.2.1-3/8 ≤ (5/8 : Rat) by grind)
    (Rat.mul_nonneg hx0 (show 0 ≤ 1-s.1 by grind))
  have hxx := Rat.mul_nonneg hx0 hx0
  change s.1+(1/5)*s.1*(1-s.1)*(4*(s.2.1-3/8)) ≤ (3/2)*s.1
  grind

theorem share_history_upper (s : OperatingState) (hs : physical s) :
    ∀ n, (trajectory s n).1 ≤ s.1*radius (3/2) 1 n := by
  intro n
  induction n with
  | zero => simp only [trajectory, RegimeBoundary.history, radius]; grind
  | succ n ih =>
    have h := share_growth_upper _ (trajectory_physical s hs n)
    change (rescue (trajectory s n)).1 ≤ s.1*radius (3/2) 1 (n+1)
    simp only [radius]
    grind

theorem no_uniform_pulse_duration (N : Nat) :
    ∃ s, physical s ∧ 0 < s.1 ∧ ¬ Landing (trajectory s N) := by
  let a := radius (3/2) 1 N
  have ha : 1 ≤ a := (radius_growth_lower (3/2) 1
    (by decide +kernel) (by decide +kernel) N).1
  have hd : 0 < 4*a := by grind
  have hz : 0 < 1/(4*a) := (Rat.lt_div_iff hd).mpr (by grind)
  have hm : (1/(4*a))*(4*a) = 1 := Rat.div_mul_cancel (show 4*a ≠ 0 by grind)
  have hx' : 1/(4*a) < 1 := (Rat.div_lt_iff hd).mpr (by grind)
  have hx : 1/(4*a) ≤ 1 := by grind
  let s : OperatingState := (1/(4*a),1,1)
  have hp : physical s := by
    change 0 ≤ 1/(4*a) ∧ 1/(4*a) ≤ 1 ∧ (0 : Rat) ≤ 1 ∧ 1 ≤ 1 ∧ 0 ≤ 1 ∧ 1 ≤ 1
    grind
  have hu := share_history_upper s hp N
  have he : (1/(4*a))*a = 1/4 := by grind
  change (trajectory s N).1 ≤ (1/(4*a))*a at hu
  rw [he] at hu
  refine ⟨s,hp,hz,?_⟩
  unfold Landing
  grind

end RegimeTransition
