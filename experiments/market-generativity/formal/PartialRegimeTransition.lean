import RegimeTransition

namespace PartialRegimeTransition
open MarketGenerativity RegimeBoundary RegimeAttraction RegimeTransition

abbrev path (b : Rat) (s : OperatingState) := RegimeBoundary.history (family b) s

theorem path_physical (b : Rat) (s : OperatingState) (hs : physical s) :
    ∀ n, physical (path b s n) := by
  intro n
  induction n with
  | zero => exact hs
  | succ n ih => exact family_physical b _ ih

theorem quality_lower_step (b : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s) :
    (1/3)*s.2.1+1/4 ≤ (family b s).2.1 := by
  rcases hs with ⟨hx0,hx1,hq0,hq1,hw0,hw1⟩
  have hq := quality_unclipped b s.2.1 s.2.2 hb0 (by grind) hq0 hq1 hw0 hw1
  have hbw := Rat.mul_le_mul_of_nonneg_left hw1 hb0
  have hprod := Rat.mul_le_mul_of_nonneg_right (show b*s.2.2 ≤ 5/12 by grind) hq0
  change (1/3)*s.2.1+1/4 ≤ qualityStep s.2.1 (1/4) b s.2.2 1 0
  rw [hq]
  grind

theorem quality_history_lower (b : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s) :
    ∀ n, (3/8)*(1-radius (1/3) 1 n) ≤ (path b s n).2.1 := by
  intro n
  induction n with
  | zero => simp only [path, RegimeBoundary.history, radius]; grind [physical]
  | succ n ih =>
    have h := quality_lower_step b _ hb0 hb1 (path_physical b s hs n)
    change (3/8)*(1-radius (1/3) 1 (n+1)) ≤ (family b (path b s n)).2.1
    simp only [radius]
    grind

theorem share_deficit_step (b d : Rat) (s : OperatingState)
    (hs : physical s) (hd : 0 ≤ d) (hq : (3/8)*(1-d) ≤ s.2.1) :
    (1-(3/10)*d)*s.1 ≤ (family b s).1 := by
  rcases hs with ⟨hx0,hx1,hq0,hq1,hw0,hw1⟩
  have h1 := Rat.mul_le_mul_of_nonneg_left (show -(3/8)*d ≤ s.2.1-3/8 by grind)
    (show 0 ≤ 1-s.1 by grind)
  have h2 := Rat.mul_nonneg hx0 hd
  have h3 := Rat.mul_le_mul_of_nonneg_left h1 hx0
  change (1-(3/10)*d)*s.1 ≤ s.1+(1/5)*s.1*(1-s.1)*(4*(s.2.1-3/8))
  grind

theorem retained_positive_seed (b : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s) :
    ∀ n, s.1*(11/20+(9/20)*radius (1/3) 1 n) ≤ (path b s n).1 := by
  intro n
  induction n with
  | zero => simp only [radius, path, RegimeBoundary.history]; grind
  | succ n ih =>
    let d := radius (1/3) 1 n
    have hd := radius_bounds (1/3) 1 (by decide +kernel) (by decide +kernel) (by decide +kernel) n
    have hx0 := hs.1
    have hstep := share_deficit_step b d _ (path_physical b s hs n) hd.1
      (quality_history_lower b s hb0 hb1 hs n)
    have hmul := Rat.mul_le_mul_of_nonneg_left ih (show 0 ≤ 1-(3/10)*d by dsimp [d]; grind)
    have hquad := Rat.mul_nonneg hd.1 (show 0 ≤ 1-d by dsimp [d]; grind)
    have hquadx := Rat.mul_nonneg hx0 hquad
    change s.1*(11/20+(9/20)*((1/3)*d)) ≤ (family b (path b s n)).1
    change s.1*(11/20+(9/20)*d) ≤ (path b s n).1 at ih
    change 0 ≤ d*(1-d) at hquad
    change 0 ≤ s.1*(d*(1-d)) at hquadx
    change (1-(3/10)*d)*(s.1*(11/20+(9/20)*d)) ≤
      (1-(3/10)*d)*(path b s n).1 at hmul
    grind

theorem uniform_seed_floor (b : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s) :
    ∀ n, s.1/2 ≤ (path b s n).1 := by
  intro n
  have h := retained_positive_seed b s hb0 hb1 hs n
  have hd := radius_bounds (1/3) 1 (by decide +kernel) (by decide +kernel) (by decide +kernel) n
  have hp := Rat.mul_nonneg hs.1 hd.1
  have hx := hs.1
  grind

theorem eventual_floor (f : Nat → Rat) (target gain : Rat) (start : Nat)
    (hg : 0 < gain) (bounded : ∀ n, f n ≤ 1)
    (rise : ∀ n, start ≤ n → f n < target → f n+gain ≤ f (n+1))
    (keep : ∀ n, start ≤ n → target ≤ f n → target ≤ f (n+1)) :
    ∃ N, start ≤ N ∧ ∀ n, N ≤ n → target ≤ f n := by
  by_cases h : ∃ N, start ≤ N ∧ target ≤ f N
  · obtain ⟨N,hN,ht⟩ := h
    have hall : ∀ k, target ≤ f (N+k) := by
      intro k
      induction k with
      | zero => simpa using ht
      | succ k ih => exact keep (N+k) (by omega) ih
    exact ⟨N,hN,by intro n hn; have hh := hall (n-N); simpa [Nat.add_sub_of_le hn] using hh⟩
  · have hlo : ∀ n, start ≤ n → f n < target := by
      intro n hn
      by_cases hh : target ≤ f n
      · exact False.elim (h ⟨n,hn,hh⟩)
      · grind
    have lin : ∀ k : Nat, f start+(k : Rat)*gain ≤ f (start+k) := by
      intro k
      induction k with
      | zero => simp; grind
      | succ k ih =>
        have hh := rise (start+k) (by omega) (hlo (start+k) (by omega))
        simp only [Rat.natCast_add, Rat.natCast_ofNat]
        grind
    obtain ⟨k,hk⟩ := rational_natural_bound ((1-f start)/gain)
    have hh := (Rat.div_lt_iff hg).mp hk
    have hl := lin k
    have hu := bounded (start+k)
    grind

theorem influence_from_share_floor (b a : Rat) (s : OperatingState) (start : Nat)
    (hs : physical s) (ha : 0 ≤ a) (hshare : ∀ n, start ≤ n → a ≤ (path b s n).1) :
    ∀ k, (path b s (start+k)).2.2 ≤ 1-a+radius (3/4) 1 k := by
  intro k
  induction k with
  | zero =>
    have hp := path_physical b s hs start
    have hx := hshare start (by omega)
    simp only [Nat.add_zero, radius]
    grind [physical]
  | succ k ih =>
    have hx := hshare (start+k) (by omega)
    change influenceStep (path b s (start+k)).2.2 (1/4) 1 (path b s (start+k)).1 ≤
      1-a+radius (3/4) 1 (k+1)
    unfold influenceStep
    simp only [radius]
    grind

theorem eventual_influence (b a epsilon : Rat) (s : OperatingState) (start : Nat)
    (hs : physical s) (ha : 0 ≤ a) (he : 0 < epsilon)
    (hshare : ∀ n, start ≤ n → a ≤ (path b s n).1) :
    ∃ N, start ≤ N ∧ ∀ n, N ≤ n → (path b s n).2.2 ≤ 1-a+epsilon := by
  obtain ⟨k,hk⟩ := radius_eventually_small (3/4) 1 epsilon
    (by decide +kernel) (by decide +kernel) (by decide +kernel) he
  refine ⟨start+k,by omega,?_⟩
  intro n hn
  have h := influence_from_share_floor b a s start hs ha hshare (n-start)
  have hr := hk (n-start) (by omega)
  have heq : start+(n-start) = n := by omega
  rw [heq] at h
  grind

theorem quality_progress (b W T g : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s)
    (hw : s.2.2 ≤ W) (hW : 0 ≤ W) (hT : 0 ≤ T) (hq : s.2.1 ≤ T)
    (hm : g ≤ (1/4)*(1-T)-b*W*T) : s.2.1+g ≤ (family b s).2.1 := by
  rcases hs with ⟨hx0,hx1,hq0,hq1,hw0,hw1⟩
  have he := quality_unclipped b s.2.1 s.2.2 hb0 (by grind) hq0 hq1 hw0 hw1
  have hbW := Rat.mul_le_mul_of_nonneg_left hw hb0
  have hqprod := Rat.mul_le_mul_of_nonneg_right hbW hq0
  have hbW0 := Rat.mul_nonneg hb0 hW
  have htprod := Rat.mul_le_mul_of_nonneg_left hq hbW0
  change s.2.1+g ≤ qualityStep s.2.1 (1/4) b s.2.2 1 0
  rw [he]
  grind

theorem quality_keeps (b W T : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s)
    (hW : W ≤ 1) (hw : s.2.2 ≤ W) (hT0 : 0 ≤ T) (hT1 : T ≤ 1)
    (hq : T ≤ s.2.1) (hm : b*W*T ≤ (1/4)*(1-T)) :
    T ≤ (family b s).2.1 := by
  exact (quality_preserves_floor s.2.1 (1/4) b s.2.2 T W 0 0 hq hT0 hT1
    (by decide +kernel) hb0 (by grind) hs.2.2.2.2.1 hw hs.2.2.2.2.2
    (by decide +kernel) (by grind)).1

theorem partial_positive_margin (b a : Rat) (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12)
    (ha0 : 0 ≤ a) (ha1 : a ≤ 1/2) :
    a/32 ≤ (1/4)*(1-(3/8+a/16))-b*(1-a/2)*(3/8+a/16) := by
  have hprod := Rat.mul_nonneg (show 0 ≤ 1-a/2 by grind) (show 0 ≤ 3/8+a/16 by grind)
  have h := Rat.mul_le_mul_of_nonneg_right hb1 hprod
  have hsq := Rat.mul_nonneg ha0 ha0
  grind

theorem eventual_positive_gap (b : Rat) (s : OperatingState)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 5/12) (hs : physical s) (hx : 0 < s.1) :
    ∃ N, ∀ n, N ≤ n → 3/8+s.1/32 ≤ (path b s n).2.1 := by
  let a := s.1/2
  have ha0 : 0 < a := by dsimp [a]; grind
  have ha1 : a ≤ 1/2 := by have := hs.2.1; dsimp [a]; grind
  have hshare : ∀ n, 0 ≤ n → a ≤ (path b s n).1 := by
    intro n _; exact uniform_seed_floor b s hb0 hb1 hs n
  obtain ⟨N,_hN,hw⟩ := eventual_influence b a (a/2) s 0 hs (by grind) (by grind) hshare
  have hm := partial_positive_margin b a hb0 hb1 (by grind) ha1
  obtain ⟨K,_hK,hKall⟩ := eventual_floor (fun n => (path b s n).2.1) (3/8+a/16) (a/32) N
    (by grind) (fun n => (path_physical b s hs n).2.2.2.1)
    (by intro n hn hq
        apply quality_progress b (1-a/2) (3/8+a/16) (a/32) _ hb0 hb1
          (path_physical b s hs n) (by have := hw n hn; grind) (by grind) (by grind) (by grind) hm)
    (by intro n hn hq
        apply quality_keeps b (1-a/2) (3/8+a/16) _ hb0 hb1 (path_physical b s hs n)
          (by grind) (by have := hw n hn; grind) (by grind) (by grind) hq
        grind)
  refine ⟨K,?_⟩
  intro n hn
  have h := hKall n hn
  dsimp [a] at h
  grind

end PartialRegimeTransition
