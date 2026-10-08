import RegimeBoundary

/- Fixed configurations and quantitative local attraction in the existing
   rational market family. The paid operating projection retains its scope. -/
namespace RegimeAttraction
open MarketGenerativity RegimeBoundary

def physical (s : OperatingState) : Prop :=
  0 ≤ s.1 ∧ s.1 ≤ 1 ∧ 0 ≤ s.2.1 ∧ s.2.1 ≤ 1 ∧ 0 ≤ s.2.2 ∧ s.2.2 ≤ 1

def family (beta : Rat) : OperatingState → OperatingState :=
  step (1/4) beta 1 (1/5) 4 (1/4) (3/8)

def high : OperatingState := (1, 1, 0)
def low (beta : Rat) : OperatingState := (0, 1/(1+4*beta), 1)
def middle (beta : Rat) : OperatingState := (1-5/(12*beta), 3/8, 5/(12*beta))

theorem quality_unclipped (beta q w : Rat)
    (hb : 0 ≤ beta) (hb1 : beta ≤ 3/4)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    qualityStep q (1/4) beta w 1 0 = (3/4-beta*w)*q+1/4 := by
  have hbw := Rat.mul_le_mul_of_nonneg_left hw1 hb
  have hc : 0 ≤ 3/4-beta*w := by grind
  have hlo := Rat.mul_nonneg hc hq0
  have hsub := Rat.mul_nonneg (Rat.mul_nonneg hb hw0) hq0
  unfold qualityStep clip01
  grind

theorem fixed_iff_balances (beta : Rat) (s : OperatingState)
    (hb : 0 ≤ beta) (hb1 : beta ≤ 3/4) (hs : physical s) :
    family beta s = s ↔
      (s.1=0 ∨ s.1=1 ∨ s.2.1=3/8) ∧
      (1/4)*(1-s.2.1)=beta*s.2.2*s.2.1 ∧ s.2.2=1-s.1 := by
  rcases s with ⟨x,q,w⟩
  rcases hs with ⟨_hx0,_hx1,hq0,hq1,hw0,hw1⟩
  have hq := quality_unclipped beta q w hb hb1 hq0 hq1 hw0 hw1
  simp only [family, step, hq, shareStep, influenceStep, Prod.mk.injEq]
  constructor
  · intro h
    have hz : x*(1-x)*(q-3/8)=0 := by grind
    simp only [Rat.mul_eq_zero] at hz
    grind
  · rintro ⟨hx,hbalance,hw⟩
    rcases hx with h | h | h <;> simp only [h] <;> grind

theorem high_fixed (beta : Rat) : family beta high = high := by
  unfold family step high shareStep qualityStep influenceStep clip01
  simp
  decide +kernel

theorem low_physical (beta : Rat) (hb : 0 ≤ beta) : physical (low beta) := by
  have hd : 0 < 1+4*beta := by grind
  have he : (1/(1+4*beta))*(1+4*beta)=1 := Rat.div_mul_cancel (by grind)
  have hq0 : 0 < 1/(1+4*beta) := (Rat.lt_div_iff hd).mpr (by grind)
  have hq1 : 1/(1+4*beta) ≤ 1 := by
    have h := Rat.mul_nonneg (show 0 ≤ 4*beta by grind) (show 0 ≤ 1/(1+4*beta) by grind)
    grind
  unfold physical low
  exact ⟨by grind,by grind,by grind,hq1,by grind,by grind⟩

theorem low_fixed (beta : Rat) (hb : 0 ≤ beta) (hb1 : beta ≤ 3/4) :
    family beta (low beta) = low beta := by
  apply (fixed_iff_balances beta (low beta) hb hb1 (low_physical beta hb)).mpr
  have he : (1/(1+4*beta))*(1+4*beta)=1 := Rat.div_mul_cancel (by grind)
  unfold low
  exact ⟨Or.inl rfl,by grind,by grind⟩

theorem fixed_classification (beta : Rat) (s : OperatingState)
    (hb : 0 < beta) (hb1 : beta ≤ 3/4) (hs : physical s)
    (h : family beta s = s) :
    s = high ∨ s = low beta ∨ s = middle beta := by
  have hbal := (fixed_iff_balances beta s (by grind) hb1 hs).mp h
  have he : (1/(1+4*beta))*(1+4*beta)=1 := Rat.div_mul_cancel (by grind)
  have hm : (5/(12*beta))*(12*beta)=5 := Rat.div_mul_cancel (by grind)
  rcases s with ⟨x,q,w⟩
  rcases hbal with ⟨hx,hq,hw⟩
  rcases hx with hx | hx | hx
  · right; left
    have hz : (q-1/(1+4*beta))*(1+4*beta)=0 := by grind
    have hh := Rat.mul_eq_zero.mp hz
    unfold low
    simp only [Prod.mk.injEq]
    grind
  · left
    unfold high
    simp only [Prod.mk.injEq]
    grind
  · right; right
    have hz : (w-5/(12*beta))*(12*beta)=0 := by grind
    have hh := Rat.mul_eq_zero.mp hz
    unfold middle
    simp only [Prod.mk.injEq]
    grind

theorem middle_physical_iff (beta : Rat) (hb : 0 < beta) :
    physical (middle beta) ↔ 5/12 ≤ beta := by
  have hd : 0 < 12*beta := by grind
  have hm : (5/(12*beta))*(12*beta)=5 := Rat.div_mul_cancel (by grind)
  have hw : 0 < 5/(12*beta) := (Rat.lt_div_iff hd).mpr (by grind)
  constructor
  · intro h
    have hh := h.1
    have hmul := Rat.mul_le_mul_of_nonneg_right hh (show 0 ≤ 12*beta by grind)
    unfold middle at hmul
    grind
  · intro h
    have hq : 5/(12*beta) ≤ 1 := by
      have hm' := Rat.mul_nonneg (show 0 ≤ 12*beta-5 by grind) (show 0 ≤ 5/(12*beta) by grind)
      grind
    unfold physical middle
    exact ⟨by grind,by grind,by grind,by grind,by grind,hq⟩

theorem middle_fixed (beta : Rat) (hb : 5/12 ≤ beta) (hb1 : beta ≤ 3/4) :
    family beta (middle beta) = middle beta := by
  have hpos : 0 < beta := by grind
  apply (fixed_iff_balances beta (middle beta) (by grind) hb1
    ((middle_physical_iff beta hpos).mpr hb)).mpr
  have hm : (5/(12*beta))*(12*beta)=5 := Rat.div_mul_cancel (by grind)
  unfold middle
  exact ⟨Or.inr (Or.inr rfl),by grind,by grind⟩

theorem collision_at_boundary : middle (5/12) = low (5/12) ∧
    middle (1/2) = (1/6,3/8,5/6) := by
  decide +kernel

theorem low_selection_direction (beta : Rat) (hb : 0 ≤ beta) :
    ((low beta).2.1 < 3/8 ↔ 5/12 < beta) ∧
    (3/8 < (low beta).2.1 ↔ beta < 5/12) := by
  have hd : 0 < 1+4*beta := by grind
  constructor
  · unfold low
    rw [Rat.div_lt_iff hd]
    grind
  · unfold low
    rw [Rat.lt_div_iff hd]
    grind

def HighTube (r : Rat) (s : OperatingState) : Prop :=
  1-r ≤ s.1 ∧ s.1 ≤ 1 ∧ 1-8*r ≤ s.2.1 ∧ s.2.1 ≤ 1 ∧
    0 ≤ s.2.2 ∧ s.2.2 ≤ 2*r

def LowTube (r : Rat) (s : OperatingState) : Prop :=
  0 ≤ s.1 ∧ s.1 ≤ r ∧ 1/3-r ≤ s.2.1 ∧ s.2.1 ≤ 1/3+r ∧
    1-2*r ≤ s.2.2 ∧ s.2.2 ≤ 1

theorem high_tube_step (r : Rat) (s : OperatingState)
    (_hr0 : 0 ≤ r) (hr1 : r ≤ 1/32) (hs : HighTube r s) :
    HighTube ((7/8)*r) (family (1/2) s) := by
  rcases s with ⟨x,q,w⟩
  rcases hs with ⟨hxl,hx1,hql,hq1,hw0,hwr⟩
  have hx0 : 0 ≤ x := by grind
  have hq0 : 0 ≤ q := by grind
  have hw1 : w ≤ 1 := by grind
  have hqraw := quality_unclipped (1/2) q w (by decide +kernel)
    (by decide +kernel) hq0 hq1 hw0 hw1
  have hxhi := (share_step_bounds x (1/5) (4*(q-3/8)) hx0 hx1
    (by decide +kernel) (by grind) (by grind)).2
  have hprod := Rat.mul_le_mul_of_nonneg_left (show 3/8 ≤ q-3/8 by grind) hx0
  have hcoef : 1-(4/5)*x*(q-3/8) ≤ 7/8 := by grind
  have hdec := Rat.mul_le_mul_of_nonneg_right hcoef (show 0 ≤ 1-x by grind)
  have hdx : 1-(7/8)*r ≤ shareStep x (1/5) (4*(q-3/8)) := by
    unfold shareStep
    grind
  have hwq := Rat.mul_le_mul_of_nonneg_left hq1 hw0
  have hqw0 := Rat.mul_nonneg hw0 hq0
  unfold HighTube family step
  simp only [hqraw]
  refine ⟨hdx,hxhi,?_,?_,?_,?_⟩
  · grind
  · grind
  · unfold influenceStep; grind
  · unfold influenceStep; grind

theorem low_tube_step (r : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/48) (hs : LowTube r s) :
    LowTube ((79/80)*r) (family (1/2) s) := by
  rcases s with ⟨x,q,w⟩
  rcases hs with ⟨hx0,hxr,hql,hqu,hwl,hw1⟩
  have hx1 : x ≤ 1 := by grind
  have hq0 : 0 ≤ q := by grind
  have hq1 : q ≤ 1 := by grind
  have hw0 : 0 ≤ w := by grind
  have hqraw := quality_unclipped (1/2) q w (by decide +kernel)
    (by decide +kernel) hq0 hq1 hw0 hw1
  have hxlo := (low_share_step x (1/5) 4 q (3/8) hx0 hx1
    (by decide +kernel) (by decide +kernel) hq0 (by grind) (by decide +kernel)).1
  have hprod := Rat.mul_le_mul_of_nonneg_left (show 1/48 ≤ 3/8-q by grind)
    (show 0 ≤ 1-x by grind)
  have hcoef : 1-(4/5)*(1-x)*(3/8-q) ≤ 79/80 := by grind
  have hdx := Rat.mul_le_mul_of_nonneg_right hcoef hx0
  have hxhi : shareStep x (1/5) (4*(q-3/8)) ≤ (79/80)*r := by
    unfold shareStep
    grind
  have hA0 : 0 ≤ 1/4+(1/2)*(1-w) := by grind
  have hA1 : 1/4+(1/2)*(1-w) ≤ 13/48 := by grind
  have hbhi := Rat.mul_le_mul_of_nonneg_left (show q-1/3 ≤ r by grind) hA0
  have hblo := Rat.mul_le_mul_of_nonneg_left (show -r ≤ q-1/3 by grind) hA0
  have hAr := Rat.mul_le_mul_of_nonneg_right hA1 hr0
  unfold LowTube family step
  simp only [hqraw]
  refine ⟨hxlo,hxhi,?_,?_,?_,?_⟩
  · grind
  · grind
  · unfold influenceStep; grind
  · unfold influenceStep; grind

def radius (rho r : Rat) : Nat → Rat
  | 0 => r
  | n+1 => rho*radius rho r n

theorem radius_bounds (rho r : Rat) (hp0 : 0 ≤ rho) (hp1 : rho ≤ 1) (hr : 0 ≤ r) :
    ∀ n, 0 ≤ radius rho r n ∧ radius rho r n ≤ r := by
  intro n
  induction n with
  | zero => exact ⟨hr,by grind [radius]⟩
  | succ n ih =>
    have hlo := Rat.mul_nonneg hp0 ih.1
    have hhi := Rat.mul_le_mul_of_nonneg_left ih.2 hp0
    have hpr := Rat.mul_le_mul_of_nonneg_right hp1 hr
    simp only [radius]
    exact ⟨hlo,by grind⟩

theorem radius_formula (rho r : Rat) : ∀ n, radius rho r n = r*rho^n := by
  intro n
  induction n with
  | zero => simp [radius]
  | succ n ih => simp only [radius, ih, Rat.pow_succ]; grind

theorem high_tube_history (r : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/32) (hs : HighTube r s) :
    ∀ n, HighTube (radius (7/8) r n) (RegimeBoundary.history (family (1/2)) s n) := by
  intro n
  induction n with
  | zero => exact hs
  | succ n ih =>
    have hb := radius_bounds (7/8) r (by decide +kernel) (by decide +kernel) hr0 n
    exact high_tube_step _ _ hb.1 (by grind) ih

theorem low_tube_history (r : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/48) (hs : LowTube r s) :
    ∀ n, LowTube (radius (79/80) r n) (RegimeBoundary.history (family (1/2)) s n) := by
  intro n
  induction n with
  | zero => exact hs
  | succ n ih =>
    have hb := radius_bounds (79/80) r (by decide +kernel) (by decide +kernel) hr0 n
    exact low_tube_step _ _ hb.1 (by grind) ih

theorem rational_natural_bound (z : Rat) : ∃ n : Nat, z < (n : Rat) := by
  by_cases hz : z < 0
  · exact ⟨0,by simpa using hz⟩
  · have hf : 0 ≤ z.floor := (Rat.le_floor_iff).mpr (by grind)
    have hi : ((z.floor+1).toNat : Int) = z.floor+1 := Int.toNat_of_nonneg (by omega)
    have hc := congrArg (fun k : Int => (k : Rat)) hi
    have hh := Rat.lt_floor_add_one z
    refine ⟨(z.floor+1).toNat,?_⟩
    have hc' : ((z.floor+1).toNat : Rat) = ((z.floor+1 : Int) : Rat) := by
      simpa only [Rat.intCast_natCast] using hc
    rw [hc']
    exact hh

theorem radius_reaches_small (rho r epsilon : Rat)
    (hp0 : 0 ≤ rho) (hp1 : rho < 1) (hr : 0 ≤ r) (he : 0 < epsilon) :
    ∃ n, radius rho r n < epsilon := by
  by_cases h : ∃ n, radius rho r n < epsilon
  · exact h
  · have hall : ∀ n, epsilon ≤ radius rho r n := by
      intro n
      by_cases hn : radius rho r n < epsilon
      · exact False.elim (h ⟨n,hn⟩)
      · grind
    have hd : 0 < (1-rho)*epsilon := Rat.mul_pos (by grind) he
    have hlin : ∀ n, radius rho r n ≤ r-(n : Rat)*((1-rho)*epsilon) := by
      intro n
      induction n with
      | zero => simp only [radius]; grind
      | succ n ih =>
        have hs := Rat.mul_le_mul_of_nonneg_left (hall n) (show 0 ≤ 1-rho by grind)
        simp only [radius, Rat.natCast_add, Rat.natCast_ofNat]
        grind
    obtain ⟨n,hn⟩ := rational_natural_bound (r/((1-rho)*epsilon))
    have hlarge := (Rat.div_lt_iff hd).mp hn
    have hlo := (radius_bounds rho r hp0 (by grind) hr n).1
    have hhi := hlin n
    grind

theorem radius_shift (rho r : Rat) (n : Nat) :
    ∀ k, radius rho r (n+k) = radius rho (radius rho r n) k := by
  intro k
  induction k with
  | zero => simp [radius]
  | succ k ih => simp [radius, ih]

theorem radius_eventually_small (rho r epsilon : Rat)
    (hp0 : 0 ≤ rho) (hp1 : rho < 1) (hr : 0 ≤ r) (he : 0 < epsilon) :
    ∃ n, ∀ m, n ≤ m → radius rho r m < epsilon := by
  obtain ⟨n,hn⟩ := radius_reaches_small rho r epsilon hp0 hp1 hr he
  refine ⟨n,?_⟩
  intro m hnm
  have hlo := (radius_bounds rho r hp0 (by grind) hr n).1
  have hb := (radius_bounds rho (radius rho r n) hp0 (by grind) hlo (m-n)).2
  rw [← radius_shift rho r n (m-n)] at hb
  have hnm' : n+(m-n)=m := by omega
  rw [hnm'] at hb
  grind

theorem high_approaches (r : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/32) (hs : HighTube r s)
    (epsilon : Rat) (he : 0 < epsilon) :
    ∃ n, ∀ m, n ≤ m →
      HighTube epsilon (RegimeBoundary.history (family (1/2)) s m) := by
  obtain ⟨n,hn⟩ := radius_eventually_small (7/8) r epsilon
    (by decide +kernel) (by decide +kernel) hr0 he
  refine ⟨n,?_⟩
  intro m hm
  have hsmall := hn m hm
  have ht := high_tube_history r s hr0 hr1 hs m
  unfold HighTube at *
  grind

theorem low_approaches (r : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/48) (hs : LowTube r s)
    (epsilon : Rat) (he : 0 < epsilon) :
    ∃ n, ∀ m, n ≤ m →
      LowTube epsilon (RegimeBoundary.history (family (1/2)) s m) := by
  obtain ⟨n,hn⟩ := radius_eventually_small (79/80) r epsilon
    (by decide +kernel) (by decide +kernel) hr0 he
  refine ⟨n,?_⟩
  intro m hm
  have hsmall := hn m hm
  have ht := low_tube_history r s hr0 hr1 hs m
  unfold LowTube at *
  grind

theorem family_physical (beta : Rat) (s : OperatingState) (hs : physical s) :
    physical (family beta s) := by
  rcases s with ⟨x,q,w⟩
  rcases hs with ⟨hx0,hx1,hq0,hq1,hw0,hw1⟩
  have hq := clip_bounds ((1-(1/4)*1-beta*w)*q+(1/4)*1-0)
  have hx : 0 ≤ shareStep x (1/5) (4*(q-3/8)) ∧
      shareStep x (1/5) (4*(q-3/8)) ≤ 1 := by
    by_cases hh : q ≤ 3/8
    · have h := low_share_step x (1/5) 4 q (3/8) hx0 hx1
        (by decide +kernel) (by decide +kernel) hq0 hh (by decide +kernel)
      exact ⟨h.1,by grind⟩
    · have h := share_step_bounds x (1/5) (4*(q-3/8)) hx0 hx1
        (by decide +kernel) (by grind) (by grind)
      exact ⟨by grind,h.2⟩
  unfold physical family step qualityStep influenceStep
  exact ⟨hx.1,hx.2,hq.1,hq.2,by grind,by grind⟩

def UpperCone (d : Rat) (s : OperatingState) : Prop :=
  physical s ∧ 1/6+d ≤ s.1 ∧ 3/8+d/8 ≤ s.2.1 ∧ s.2.2 ≤ 5/6-3*d/4

theorem upper_cone_step (d : Rat) (s : OperatingState)
    (hd : 0 ≤ d) (hs : UpperCone d s) (hxsmall : s.1 ≤ 1/4) :
    UpperCone ((81/80)*d) (family (1/2) s) := by
  have hphysical := family_physical (1/2) s hs.1
  rcases s with ⟨x,q,w⟩
  rcases hs with ⟨⟨hx0,hx1,hq0,hq1,hw0,hw1⟩,hxd,hqd,hwd⟩
  have hqraw := quality_unclipped (1/2) q w (by decide +kernel)
    (by decide +kernel) hq0 hq1 hw0 hw1
  have hxx := Rat.mul_nonneg hx0 (show 0 ≤ 1-x by grind)
  have hxxlo := Rat.mul_le_mul_of_nonneg_right (show 1/6 ≤ x by grind)
    (show 0 ≤ 1-x by grind)
  have hxxlower : 1/8 ≤ x*(1-x) := by grind
  have hgain0 := Rat.mul_le_mul_of_nonneg_right hxxlower (show 0 ≤ d/8 by grind)
  have hgain1 := Rat.mul_le_mul_of_nonneg_left (show d/8 ≤ q-3/8 by grind) hxx
  have hxnext : 1/6+(81/80)*d ≤ shareStep x (1/5) (4*(q-3/8)) := by
    unfold shareStep
    grind
  have hcoef : 0 ≤ 3/4-(1/2)*w := by grind
  have hqcorner := Rat.mul_le_mul_of_nonneg_left hqd hcoef
  have hwcorner := Rat.mul_le_mul_of_nonneg_right hwd (show 0 ≤ 3/8+d/8 by grind)
  have hdsq := Rat.mul_nonneg hd hd
  unfold UpperCone family step
  simp only [hqraw]
  refine ⟨?_,hxnext,by grind,by unfold influenceStep; grind⟩
  simpa only [family, step, hqraw] using hphysical

theorem radius_growth_lower (rho d : Rat) (hp : 1 ≤ rho) (hd : 0 ≤ d) :
    ∀ n, d ≤ radius rho d n ∧ d+(n : Rat)*((rho-1)*d) ≤ radius rho d n := by
  intro n
  induction n with
  | zero => simp only [radius]; constructor <;> grind
  | succ n ih =>
    have hlo := Rat.mul_nonneg (show 0 ≤ rho-1 by grind) (show 0 ≤ radius rho d n by grind)
    have hg := Rat.mul_nonneg (show 0 ≤ rho-1 by grind) (show 0 ≤ radius rho d n-d by grind)
    simp only [radius, Rat.natCast_add, Rat.natCast_ofNat]
    constructor <;> grind

theorem middle_upper_escape (d : Rat) (s : OperatingState)
    (hd : 0 < d) (hs : UpperCone d s) :
    ∃ n, 1/4 < (RegimeBoundary.history (family (1/2)) s n).1 := by
  by_cases h : ∃ n, 1/4 < (RegimeBoundary.history (family (1/2)) s n).1
  · exact h
  · have hall : ∀ n, (RegimeBoundary.history (family (1/2)) s n).1 ≤ 1/4 := by
      intro n
      by_cases hn : 1/4 < (RegimeBoundary.history (family (1/2)) s n).1
      · exact False.elim (h ⟨n,hn⟩)
      · grind
    have hc : ∀ n, UpperCone (radius (81/80) d n)
        (RegimeBoundary.history (family (1/2)) s n) := by
      intro n
      induction n with
      | zero => exact hs
      | succ n ih =>
        have hg := (radius_growth_lower (81/80) d (by decide +kernel) (by grind) n).1
        exact upper_cone_step _ _ (by grind) ih (hall n)
    have hd80 : 0 < d/80 := by grind
    obtain ⟨n,hn⟩ := rational_natural_bound ((1/12)/(d/80))
    have hlarge := (Rat.div_lt_iff hd80).mp hn
    have hg := (radius_growth_lower (81/80) d (by decide +kernel) (by grind) n).2
    have hupper := hall n
    have hlower := (hc n).2.1
    grind

def perturbMiddle (d : Rat) : OperatingState :=
  (1/6+d,3/8+d/8,5/6-3*d/4)

def MiddleTube (r : Rat) (s : OperatingState) : Prop :=
  1/6-r ≤ s.1 ∧ s.1 ≤ 1/6+r ∧ 3/8-r ≤ s.2.1 ∧ s.2.1 ≤ 3/8+r ∧
    5/6-r ≤ s.2.2 ∧ s.2.2 ≤ 5/6+r

theorem perturbation_certificate (d : Rat) (hd0 : 0 ≤ d) (hd1 : d ≤ 1/12) :
    UpperCone d (perturbMiddle d) ∧ MiddleTube d (perturbMiddle d) := by
  unfold UpperCone physical MiddleTube perturbMiddle
  constructor <;> repeat' constructor <;> grind

theorem middle_unstable (epsilon : Rat) (he : 0 < epsilon) :
    ∃ s, physical s ∧ MiddleTube epsilon s ∧
      ∃ n, 1/4 < (RegimeBoundary.history (family (1/2)) s n).1 := by
  let d : Rat := min epsilon (1/12)
  have hd0 : 0 < d := by
    change 0 < min epsilon (1/12)
    have h12 : (0 : Rat) < 1/12 := by decide +kernel
    grind
  have hd1 : d ≤ 1/12 := by dsimp [d]; grind
  have hde : d ≤ epsilon := by dsimp [d]; grind
  have hc := perturbation_certificate d (by grind) hd1
  refine ⟨perturbMiddle d,hc.1.1,?_,middle_upper_escape d _ hd0 hc.1⟩
  have hm := hc.2
  unfold MiddleTube at *
  grind

def stockHistory (s : OperatingState) (initial : Rat) : Nat → Rat
  | 0 => initial
  | n+1 => supportStep (stockHistory s initial n) (1/10) 2 1
      (RegimeBoundary.history (family (1/2)) s n).1 0 0

theorem low_stock_loss (stock x : Rat) (hc : 5 ≤ stock) (hx0 : 0 ≤ x) (hx1 : x ≤ 1/48) :
    supportStep stock (1/10) 2 1 x 0 0 ≤ stock-15/16 := by
  unfold supportStep
  grind

theorem low_support_fails_finitely (r initial : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/48) (hs : LowTube r s) :
    ∃ n, stockHistory s initial n < 5 := by
  by_cases h : ∃ n, stockHistory s initial n < 5
  · exact h
  · have hall : ∀ n, 5 ≤ stockHistory s initial n := by
      intro n
      by_cases hn : stockHistory s initial n < 5
      · exact False.elim (h ⟨n,hn⟩)
      · grind
    have hlin : ∀ n, stockHistory s initial n ≤ initial-(n : Rat)*(15/16) := by
      intro n
      induction n with
      | zero => simp only [stockHistory]; grind
      | succ n ih =>
        have ht := low_tube_history r s hr0 hr1 hs n
        have hr := (radius_bounds (79/80) r (by decide +kernel) (by decide +kernel) hr0 n).2
        have hx : (RegimeBoundary.history (family (1/2)) s n).1 ≤ 1/48 := by
          have hxr := ht.2.1
          grind
        have hh := low_stock_loss _ _ (hall n) ht.1 hx
        simp only [stockHistory, Rat.natCast_add, Rat.natCast_ofNat]
        grind
    obtain ⟨n,hn⟩ := rational_natural_bound ((initial-5)/(15/16))
    have hlarge := (Rat.div_lt_iff (show (0 : Rat) < 15/16 by decide +kernel)).mp hn
    have hhi := hlin n
    have hlo := hall n
    grind

def lift (s : OperatingState) (stock : Rat) : State 1 :=
  { x := s.1, q := s.2.1, w := s.2.2, budget := 1, stock := fun _ => stock }

def noShock : Disturbance 1 := ⟨0,fun _ => 0⟩

theorem coupled_operating_step (s : OperatingState) (stock : Rat) :
    operatingStep exampleParameters (lift s stock) noShock =
      lift (family (1/2) s) (supportStep stock (1/10) 2 1 s.1 0 0) := by
  have hg := gap_correspondence 4 (3/8) s.2.1 (1/2) 2 (by decide +kernel)
  have hi : installed 1 1 = 1 := by decide +kernel
  have hb : reserveStep 1 1 1 3 = 1 := by decide +kernel
  unfold operatingStep exampleParameters lift family step noShock
  simp only [hg, hi, hb]

theorem coupled_histories (s : OperatingState) (initial : Rat) :
    ∀ n, MarketGenerativity.history exampleParameters (lift s initial) (fun _ => noShock) n =
      lift (RegimeBoundary.history (family (1/2)) s n) (stockHistory s initial n) := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [MarketGenerativity.history, ih, RegimeBoundary.history, stockHistory]
    exact coupled_operating_step _ _

theorem coupled_eventual_floor_breach (r initial : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/48) (hs : LowTube r s) :
    ∃ n, (MarketGenerativity.history exampleParameters (lift s initial) (fun _ => noShock) n).stock 0 < 5 := by
  obtain ⟨n,hn⟩ := low_support_fails_finitely r initial s hr0 hr1 hs
  refine ⟨n,?_⟩
  rw [coupled_histories]
  exact hn

theorem high_tube_supplies_old_safety (r stock : Rat) (s : OperatingState)
    (hr : r ≤ 1/32) (hs : HighTube r s) (hc : 5 ≤ stock) :
    Safe exampleParameters exampleBounds (lift s stock) := by
  rcases hs with ⟨hxl,hx1,hql,hq1,hw0,hwr⟩
  constructor
  · unfold exampleBounds lift; grind
  · exact hx1
  · unfold exampleBounds lift; grind
  · exact hq1
  · exact hw0
  · unfold exampleBounds lift; grind
  · change (1 : Rat) ≤ 1; decide +kernel
  · change (1 : Rat) ≤ 3; decide +kernel
  · intro j; exact hc

theorem high_coupled_history_never_fails (r stock : Rat) (s : OperatingState)
    (hr : r ≤ 1/32) (hs : HighTube r s) (hc : 5 ≤ stock) :
    ∀ n, guardedHistory exampleParameters exampleBounds (lift s stock) (fun _ => noShock) n =
      some (MarketGenerativity.history exampleParameters (lift s stock) (fun _ => noShock) n) := by
  apply safe_history_never_fails exampleParameters exampleBounds _ _ example_certificate
    (high_tube_supplies_old_safety r stock s hr hs hc)
  intro t
  unfold Admissible exampleBounds noShock
  constructor
  · decide +kernel
  · intro j; change (0 : Rat) ≤ 1/2; decide +kernel

theorem guarded_trace (s : OperatingState) (stock : Rat) :
    ∀ n, guardedHistory exampleParameters exampleBounds (lift s stock) (fun _ => noShock) n = none ∨
      guardedHistory exampleParameters exampleBounds (lift s stock) (fun _ => noShock) n =
        some (MarketGenerativity.history exampleParameters (lift s stock) (fun _ => noShock) n) := by
  intro n
  induction n with
  | zero => exact Or.inr rfl
  | succ n ih =>
    rcases ih with h | h
    · left
      simp only [guardedHistory, h, guardedStep]
    · simp only [guardedHistory, h, guardedStep, MarketGenerativity.history]
      split <;> simp

theorem low_guarded_history_fails (r stock : Rat) (s : OperatingState)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1/48) (hs : LowTube r s) :
    ∃ n, guardedHistory exampleParameters exampleBounds (lift s stock) (fun _ => noShock) n = none := by
  obtain ⟨n,hn⟩ := coupled_eventual_floor_breach r stock s hr0 hr1 hs
  rcases guarded_trace s stock n with h | h
  · exact ⟨n,h⟩
  · have hnot : ¬ essentialReady exampleParameters exampleBounds
        (MarketGenerativity.history exampleParameters (lift s stock) (fun _ => noShock) n) := by
      intro hh
      have hfloor := hh 0 (by rfl)
      change 5 ≤ (MarketGenerativity.history exampleParameters (lift s stock) (fun _ => noShock) n).stock 0 at hfloor
      grind
    refine ⟨n+1,?_⟩
    simp only [guardedHistory, h, guardedStep]
    simp [hnot]

theorem zero_share_remains_zero (beta q w : Rat) :
    (family beta (0,q,w)).1 = 0 := by
  unfold family step shareStep
  simp
  grind

end RegimeAttraction
