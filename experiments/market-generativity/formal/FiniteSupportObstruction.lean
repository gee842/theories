import RegimeTransition

/-! A finite support obstruction for the existing market, allowing arbitrary
time variation of the quality channel. Renewal and support are coordinates of
the same operating history. There is no external stock injection, direct entry
or change in the inherited share-growth rate. Failure ends this modeled market
organization, not all subsequent reality. -/
namespace FiniteSupportObstruction
open MarketGenerativity RegimeBoundary RegimeAttraction RegimeTransition

def parameters (beta : Rat) : Parameters 1 := { exampleParameters with beta := beta }

def run (beta : Nat → Rat) (d : Nat → Disturbance 1) (initial : State 1) : Nat → State 1
  | 0 => initial
  | n+1 => operatingStep (parameters (beta n)) (run beta d initial n) (d n)

def guarded (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) : Nat → Option (State 1)
  | 0 => some initial
  | n+1 => guardedStep (parameters (beta n)) exampleBounds (d n)
      (guarded beta d initial n)

def PairPhysical (s : State 1) : Prop :=
  0 ≤ s.x ∧ s.x ≤ 1 ∧ 0 ≤ s.q ∧ s.q ≤ 1

theorem next_pair_physical (beta : Rat) (d : Disturbance 1) (s : State 1)
    (hs : PairPhysical s) : PairPhysical (operatingStep (parameters beta) s d) := by
  have hp : physical (s.x,s.q,0) := by unfold physical; grind [PairPhysical]
  have hx := family_physical 0 (s.x,s.q,0) hp
  have hq := clip_bounds ((1-(1/4)*installed s.budget 1-beta*s.w)*s.q+
    (1/4)*installed s.budget 1-d.error)
  have hg := gap_correspondence 4 (3/8) s.q (1/2) 2 (by decide +kernel)
  unfold PairPhysical operatingStep parameters exampleParameters
  simp only [hg]
  exact ⟨hx.1,hx.2.1,hq.1,hq.2⟩

theorem run_pair_physical (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) (hi : PairPhysical initial) :
    ∀ n, PairPhysical (run beta d initial n) := by
  intro n
  induction n with
  | zero => exact hi
  | succ n ih => exact next_pair_physical _ _ _ ih

theorem next_share_upper (beta : Rat) (d : Disturbance 1) (s : State 1)
    (hs : PairPhysical s) : (operatingStep (parameters beta) s d).x ≤ (3/2)*s.x := by
  have hp : physical (s.x,s.q,0) := by unfold physical; grind [PairPhysical]
  have hx := share_growth_upper (s.x,s.q,0) hp
  have hg := gap_correspondence 4 (3/8) s.q (1/2) 2 (by decide +kernel)
  simpa only [operatingStep, parameters, exampleParameters, hg, rescue, family, step] using hx

theorem run_share_upper (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) (hi : PairPhysical initial) :
    ∀ n, (run beta d initial n).x ≤ initial.x*radius (3/2) 1 n := by
  intro n
  induction n with
  | zero => simp only [run, radius]; grind
  | succ n ih =>
    have hx := next_share_upper (beta n) (d n) _ (run_pair_physical beta d initial hi n)
    change (operatingStep _ _ _).x ≤ initial.x*radius (3/2) 1 (n+1)
    simp only [radius]
    grind

theorem growth_factor_mono (i j : Nat) (hij : i ≤ j) :
    radius (3/2) 1 i ≤ radius (3/2) 1 j := by
  induction j with
  | zero =>
    have h : i = 0 := by omega
    subst i
    exact Rat.le_refl
  | succ j ih =>
    by_cases h : i ≤ j
    · have hprev := ih h
      have hlo := (radius_growth_lower (3/2) 1 (by decide +kernel) (by decide +kernel) j).1
      simp only [radius]
      grind
    · have he : i = j+1 := by omega
      subst i
      exact Rat.le_refl

theorem small_seed_prefix (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) (hi : PairPhysical initial) (N : Nat)
    (hsmall : initial.x*radius (3/2) 1 N ≤ 1/6) :
    ∀ t, t ≤ N → (run beta d initial t).x ≤ 1/6 := by
  intro t ht
  have hx := run_share_upper beta d initial hi t
  have hm := Rat.mul_le_mul_of_nonneg_left (growth_factor_mono t N ht) hi.1
  grind

theorem next_support_loss (beta : Rat) (d : Disturbance 1) (s : State 1)
    (hc : 5 ≤ s.stock 0) (hx : s.x ≤ 1/6) (hd : 0 ≤ d.shock 0) :
    (operatingStep (parameters beta) s d).stock 0 ≤ s.stock 0-1 := by
  change supportStep (s.stock 0) (1/10) 2 1 s.x 0 (d.shock 0) ≤ s.stock 0-1
  unfold supportStep
  grind

theorem guarded_prefix_sound (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) (hi : 5 ≤ initial.stock 0) :
    ∀ n s, guarded beta d initial n = some s →
      s = run beta d initial n ∧ ∀ t, t ≤ n → 5 ≤ (run beta d initial t).stock 0 := by
  intro n
  induction n with
  | zero =>
    intro s h
    have he : initial = s := Option.some.inj h
    subst s
    refine ⟨rfl,?_⟩
    intro t ht
    have hz : t = 0 := by omega
    subst t
    exact hi
  | succ n ih =>
    intro s h
    cases hp : guarded beta d initial n with
    | none => simp only [guarded, hp, guardedStep] at h; cases h
    | some prev =>
      have hh := ih prev hp
      rw [hh.1] at hp
      simp only [guarded, hp, guardedStep] at h
      split at h
      next ready =>
        have he := Option.some.inj h
        refine ⟨he.symm,?_⟩
        intro t ht
        by_cases htn : t ≤ n
        · exact hh.2 t htn
        · have ht' : t = n+1 := by omega
          subst t
          exact ready.2 0 rfl
      next _ => cases h

theorem support_required_for_small_prefix (beta : Nat → Rat)
    (d : Nat → Disturbance 1) (initial : State 1) (N : Nat)
    (hi : PairPhysical initial) (hc : 5 ≤ initial.stock 0)
    (hd : ∀ n, 0 ≤ (d n).shock 0)
    (hsmall : initial.x*radius (3/2) 1 N ≤ 1/6)
    (hsurvive : guarded beta d initial N ≠ none) :
    5+(N : Rat) ≤ initial.stock 0 := by
  have hall : ∀ t, t ≤ N → 5 ≤ (run beta d initial t).stock 0 := by
    cases hn : guarded beta d initial N with
    | none => exact False.elim (hsurvive hn)
    | some s => exact (guarded_prefix_sound beta d initial hc N s hn).2
  have hbound : ∀ t, t ≤ N →
      (run beta d initial t).stock 0+(t : Rat) ≤ initial.stock 0 := by
    intro t
    induction t with
    | zero => intro _; change initial.stock 0+(0 : Rat) ≤ initial.stock 0; grind
    | succ t ih =>
      intro ht
      have hprev := ih (by omega)
      have hstock := hall t (by omega)
      have hx := small_seed_prefix beta d initial hi N hsmall t (by omega)
      have hnext := next_support_loss (beta t) (d t) _ hstock hx (hd t)
      change (operatingStep _ _ _).stock 0+((t+1 : Nat) : Rat) ≤ initial.stock 0
      simp only [Rat.natCast_add, Rat.natCast_ofNat]
      grind
  have hlast := hbound N (by omega)
  have hfloor := hall N (by omega)
  grind

theorem finite_support_forces_failure (beta : Nat → Rat)
    (d : Nat → Disturbance 1) (initial : State 1) (N : Nat)
    (hi : PairPhysical initial) (hc : 5 ≤ initial.stock 0)
    (hd : ∀ n, 0 ≤ (d n).shock 0)
    (hsmall : initial.x*radius (3/2) 1 N ≤ 1/6)
    (hshort : initial.stock 0 < 5+(N : Rat)) :
    guarded beta d initial N = none := by
  by_cases hf : guarded beta d initial N = none
  · exact hf
  · have hneed := support_required_for_small_prefix beta d initial N hi hc hd hsmall hf
    grind

theorem guarded_failure_persists (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) (N : Nat) (hf : guarded beta d initial N = none) :
    ∀ k, guarded beta d initial (N+k) = none := by
  intro k
  induction k with
  | zero => exact hf
  | succ k ih =>
    change guardedStep _ _ _ (guarded beta d initial (N+k)) = none
    rw [ih]
    rfl

theorem small_seed_prefix_has_no_landing (beta : Nat → Rat)
    (d : Nat → Disturbance 1) (initial : State 1) (hi : PairPhysical initial) (N : Nat)
    (hsmall : initial.x*radius (3/2) 1 N ≤ 1/6) :
    ∀ t, t ≤ N → ¬ Landing ((run beta d initial t).x,
      (run beta d initial t).q, (run beta d initial t).w) := by
  intro t ht hl
  have hx := small_seed_prefix beta d initial hi N hsmall t ht
  have hland := hl.2.1
  grind

def seedLimit (N : Nat) : Rat := 1/(6*radius (3/2) 1 N)

theorem seed_limit_bounds (N : Nat) :
    0 < seedLimit N ∧ seedLimit N ≤ 1/6 ∧
      seedLimit N*radius (3/2) 1 N = 1/6 := by
  have ha := (radius_growth_lower (3/2) 1 (by decide +kernel) (by decide +kernel) N).1
  have hd : 0 < 6*radius (3/2) 1 N := by grind
  have hz := (Rat.lt_div_iff hd).mpr (show (0 : Rat)*(6*radius (3/2) 1 N) < 1 by grind)
  have hm : (1/(6*radius (3/2) 1 N))*(6*radius (3/2) 1 N) = 1 :=
    Rat.div_mul_cancel (by grind)
  have hprod := Rat.mul_nonneg (show 0 ≤ radius (3/2) 1 N-1 by grind)
    (show 0 ≤ 1/(6*radius (3/2) 1 N) by grind)
  have hu : 1/(6*radius (3/2) 1 N) ≤ 1/6 := by grind
  unfold seedLimit
  exact ⟨hz,hu,by grind⟩

theorem every_finite_stock_has_obstructed_positive_seeds (stock : Rat) (hc : 5 ≤ stock) :
    ∃ N, 0 < N ∧ 0 < seedLimit N ∧ ∀ x q w,
      0 < x → x ≤ seedLimit N → 0 ≤ q → q ≤ 1 →
      ∀ beta d, (∀ n, 0 ≤ (d n).shock 0) →
        guarded beta d (lift (x,q,w) stock) N = none := by
  obtain ⟨N,hN⟩ := rational_natural_bound (stock-5)
  have hn0 : 0 < N := by
    by_cases h : N = 0
    · subst N; change stock-5 < (0 : Rat) at hN; grind
    · omega
  refine ⟨N,hn0,(seed_limit_bounds N).1,?_⟩
  intro x q w hx hxsmall hq0 hq1 beta d hd
  have hp : PairPhysical (lift (x,q,w) stock) := by
    have hlim := (seed_limit_bounds N).2.1
    unfold PairPhysical lift
    grind
  have hm := Rat.mul_le_mul_of_nonneg_right hxsmall
    (show 0 ≤ radius (3/2) 1 N by
      have := (radius_growth_lower (3/2) 1 (by decide +kernel) (by decide +kernel) N).1
      grind)
  rw [(seed_limit_bounds N).2.2] at hm
  exact finite_support_forces_failure beta d _ N hp hc hd hm (by change stock < 5+(N : Rat); grind)

theorem zero_schedule_is_original_pulse (initial : State 1) :
    ∀ n, guarded (fun _ => 0) (fun _ => pulseDisturbance 0) initial n =
      guardedHistory pulseParameters exampleBounds initial (fun _ => pulseDisturbance 0) n := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih => simp only [guarded, guardedHistory, ih]; rfl

/-- The very same positive operating state eventually reaches protection when
its support coordinate is omitted, yet its full funded history terminates. -/
theorem projected_recovery_and_actual_failure (stock : Rat) (hc : 5 ≤ stock) :
    ∃ s : OperatingState, physical s ∧ 0 < s.1 ∧
      (∃ T, Landing (trajectory s T)) ∧
      (∃ N, guardedHistory pulseParameters exampleBounds (lift s stock)
        (fun _ => pulseDisturbance 0) N = none) := by
  obtain ⟨N,_hn,hpos,hfail⟩ := every_finite_stock_has_obstructed_positive_seeds stock hc
  let s : OperatingState := (seedLimit N,1,0)
  have hp : physical s := by
    have hu := (seed_limit_bounds N).2.1
    unfold physical s
    grind
  refine ⟨s,hp,hpos,positive_seed_finite_landing s hp hpos, N,?_⟩
  rw [← zero_schedule_is_original_pulse]
  exact hfail (seedLimit N) 1 0 hpos Rat.le_refl (by decide +kernel)
    (by decide +kernel) (fun _ => 0) (fun _ => pulseDisturbance 0)
    (fun _ => by change (0 : Rat) ≤ 0; decide +kernel)

theorem same_stock_can_support_high_seed (stock : Rat) (hc : 5 ≤ stock) :
    ∀ n, guardedHistory exampleParameters exampleBounds (lift (1,1,0) stock)
      (fun _ => noShock) n =
      some (MarketGenerativity.history exampleParameters (lift (1,1,0) stock)
        (fun _ => noShock) n) := by
  have hs : Safe exampleParameters exampleBounds (lift (1,1,0) stock) := by
    constructor
    · change (3/4 : Rat) ≤ 1; decide +kernel
    · exact Rat.le_refl
    · change (1/2 : Rat) ≤ 1; decide +kernel
    · exact Rat.le_refl
    · exact Rat.le_refl
    · change (0 : Rat) ≤ 1/4; decide +kernel
    · exact Rat.le_refl
    · change (1 : Rat) ≤ 3; decide +kernel
    · intro _; exact hc
  exact safe_history_never_fails exampleParameters exampleBounds _ _ example_certificate hs
    (fun _ => ⟨by change (0 : Rat) ≤ 1/20; decide +kernel,
      fun _ => by change (0 : Rat) ≤ 1/2; decide +kernel⟩)

end FiniteSupportObstruction
