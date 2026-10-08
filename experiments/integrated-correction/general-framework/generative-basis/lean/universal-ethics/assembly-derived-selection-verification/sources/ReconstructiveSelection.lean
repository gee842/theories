import Std

/-!
Selection on a transmitted developmental capacity through two census states.
All coefficients are rational expected descendant counts in a fixed resident
context. This is a local, deterministic comparison, not fixation or an origin
of the coefficients. O and P are stages of the same reproductive history;
loss of the visible organization in P need not lose the inherited capacity.
-/
namespace ReconstructiveSelection

structure Kernel where
  a : Rat
  b : Rat
  c : Rat
  d : Rat

def nextO (k : Kernel) (o p : Rat) : Rat := k.a*o + k.b*p
def nextP (k : Kernel) (o p : Rat) : Rat := k.c*o + k.d*p
def value (t o p : Rat) : Rat := o + t*p
def margin (k : Kernel) : Rat := k.b*k.c - (1-k.a)*(1-k.d)
def Expands (k : Kernel) (t : Rat) : Prop :=
  0 < t ∧ 1 < k.a+k.c*t ∧ t < k.b+k.d*t

theorem value_step (k : Kernel) (t o p : Rat) :
    value t (nextO k o p) (nextP k o p) =
      (k.a+k.c*t)*o + (k.b+k.d*t)*p := by
  unfold value nextO nextP
  grind

/-- Exact condition for one positive weighting to increase in both stages.
    The two self-return routes are subcritical; growth must close the loop. -/
theorem loop_criterion (k : Kernel)
    (ha : k.a < 1) (hc : 0 < k.c) (hd : k.d < 1) :
    (∃ t, Expands k t) ↔ 0 < margin k := by
  constructor
  · rintro ⟨t, ht, h1, h2⟩
    unfold margin
    have h3 : (1-k.a)*(1-k.d) < k.c*t*(1-k.d) := by
      apply Rat.mul_lt_mul_of_pos_right _ (by grind)
      grind
    have h4 : k.c*(t*(1-k.d)) < k.c*k.b := by
      apply Rat.mul_lt_mul_of_pos_left _ hc
      grind
    grind
  · intro hm
    let lo := (1-k.a)/k.c
    let hi := k.b/(1-k.d)
    have hcn : k.c ≠ 0 := by grind
    have hdn : 1-k.d ≠ 0 := by grind
    have hlo : 0 < lo := by
      change 0 < (1-k.a)*(k.c)⁻¹
      exact Rat.mul_pos (by grind) (Rat.inv_pos.mpr hc)
    have hli : lo < hi := by
      have hpos : 0 < k.c*(1-k.d) := Rat.mul_pos hc (by grind)
      have heq : (hi-lo)*(k.c*(1-k.d)) = margin k := by
        unfold hi lo margin
        grind
      have hp : 0 < (hi-lo)*(k.c*(1-k.d)) := by rw [heq]; exact hm
      have : 0 < hi-lo := (Rat.mul_pos_iff_of_pos_right hpos).mp hp
      grind
    refine ⟨(lo+hi)/2, ?_, ?_, ?_⟩
    · grind
    · have hmul : k.c*lo < k.c*((lo+hi)/2) := by
        apply Rat.mul_lt_mul_of_pos_left _ hc
        grind
      have heq : k.c*lo = 1-k.a := by unfold lo; grind
      grind
    · have hmul : ((lo+hi)/2)*(1-k.d) < hi*(1-k.d) := by
        apply Rat.mul_lt_mul_of_pos_right _ (by grind)
        grind
      have heq : hi*(1-k.d) = k.b := by unfold hi; grind
      grind

/-- Remove the subcritical O self-return assumption when both return edges
    are positive. No eigenvalue theorem is imported or postulated. -/
theorem full_loop_criterion (k : Kernel)
    (hb : 0 < k.b) (hc : 0 < k.c) (hd : k.d < 1) :
    (∃ t, Expands k t) ↔ 0 < margin k := by
  by_cases ha : k.a < 1
  · exact loop_criterion k ha hc hd
  have hdn : 1-k.d ≠ 0 := by grind
  let t := k.b/(2*(1-k.d))
  have ht : 0 < t := by
    exact Rat.mul_pos hb (Rat.inv_pos.mpr (Rat.mul_pos (by decide) (by grind)))
  have heq : 2*t*(1-k.d) = k.b := by unfold t; grind
  have hex : Expands k t := by
    have hct := Rat.mul_pos hc ht
    unfold Expands
    grind
  have hm : 0 < margin k := by
    have hp := Rat.mul_pos hb hc
    have hn := Rat.mul_le_mul_of_nonneg_right
      (show 1-k.a ≤ 0 by grind) (show 0 ≤ 1-k.d by grind)
    unfold margin
    grind
  exact ⟨fun _ => hm, fun _ => ⟨t,hex⟩⟩

/-- Strict weighted gains give a common positive geometric margin. -/
theorem expansion_has_margin (k : Kernel) (t : Rat) (h : Expands k t) :
    ∃ e : Rat, 0 < e ∧ 1+e ≤ k.a+k.c*t ∧ (1+e)*t ≤ k.b+k.d*t := by
  obtain ⟨ht,h1,h2⟩ := h
  let u := k.a+k.c*t-1
  let v := (k.b+k.d*t-t)/t
  have hu : 0 < u := by unfold u; grind
  have hv : 0 < v := Rat.mul_pos (by grind) (Rat.inv_pos.mpr ht)
  have hn : t ≠ 0 := by grind
  have heq : v*t = k.b+k.d*t-t := by unfold v; grind
  refine ⟨min u v, ?_, ?_, ?_⟩
  · grind
  · have hh : min u v ≤ u := by grind
    unfold u at hh
    grind
  · have hh := Rat.mul_le_mul_of_nonneg_right (show min u v ≤ v by grind) (show 0 ≤ t by grind)
    grind

/-- At and below the threshold a positive weighting cannot increase. This
    rules out sustained geometric growth, not every transient count increase. -/
theorem nonexpansion_witness (k : Kernel) (hb : 0 < k.b) (hd : k.d < 1)
    (hm : margin k ≤ 0) :
    ∃ t : Rat, 0 < t ∧ ∀ o p : Rat, 0 ≤ o → 0 ≤ p →
      value t (nextO k o p) (nextP k o p) ≤ value t o p := by
  let t := k.b/(1-k.d)
  have ht : 0 < t := Rat.mul_pos hb (Rat.inv_pos.mpr (by grind))
  have hn : 1-k.d ≠ 0 := by grind
  have heq : t*(1-k.d) = k.b := by unfold t; grind
  have h1 : k.a+k.c*t ≤ 1 := by
    have hh : (k.a+k.c*t-1)*(1-k.d) = margin k := by unfold margin; grind
    have : k.a+k.c*t-1 ≤ 0 := by
      have hx : (k.a+k.c*t-1)*(1-k.d) ≤ 0*(1-k.d) := by grind
      exact Rat.le_of_mul_le_mul_right hx (show 0 < 1-k.d by grind)
    grind
  refine ⟨t, ht, ?_⟩
  intro o p ho _hp
  rw [value_step]
  have h2 : k.b+k.d*t = t := by grind
  rw [h2]
  have hh := Rat.mul_le_mul_of_nonneg_right h1 ho
  unfold value
  grind

def history (ks : Nat → Kernel) (o p : Rat) : Nat → Rat × Rat
  | 0 => (o,p)
  | n+1 => let v := history ks o p n
           (nextO (ks n) v.1 v.2, nextP (ks n) v.1 v.2)

/-- A common certificate applies even when the realized kernel changes. -/
theorem uniform_history_bound (ks : Nat → Kernel) (t e o p : Rat)
    (ho : 0 ≤ o) (hp : 0 ≤ p) (he : 0 ≤ e)
    (hk : ∀ n, 0 ≤ (ks n).a ∧ 0 ≤ (ks n).b ∧
      0 ≤ (ks n).c ∧ 0 ≤ (ks n).d)
    (hw : ∀ n, 1+e ≤ (ks n).a+(ks n).c*t ∧
      (1+e)*t ≤ (ks n).b+(ks n).d*t) :
    ∀ n, 0 ≤ (history ks o p n).1 ∧ 0 ≤ (history ks o p n).2 ∧
      (1+e)^n * value t o p ≤
        value t (history ks o p n).1 (history ks o p n).2 := by
  intro n
  induction n with
  | zero => simp [history, ho, hp]
  | succ n ih =>
    obtain ⟨ha,hb,hc,hd⟩ := hk n
    obtain ⟨h1,h2⟩ := hw n
    have hO := Rat.add_nonneg (Rat.mul_nonneg ha ih.1) (Rat.mul_nonneg hb ih.2.1)
    have hP := Rat.add_nonneg (Rat.mul_nonneg hc ih.1) (Rat.mul_nonneg hd ih.2.1)
    refine ⟨hO,hP,?_⟩
    change (1+e)^(n+1)*value t o p ≤
      value t (nextO (ks n) (history ks o p n).1 (history ks o p n).2)
        (nextP (ks n) (history ks o p n).1 (history ks o p n).2)
    rw [value_step, Rat.pow_succ]
    have hA := Rat.mul_le_mul_of_nonneg_right h1 ih.1
    have hB := Rat.mul_le_mul_of_nonneg_right h2 ih.2.1
    have hC := Rat.mul_le_mul_of_nonneg_left ih.2.2 (show 0 ≤ 1+e by grind)
    unfold value at *
    grind

def developmental (f g q r : Rat) : Kernel :=
  ⟨q*f, r*g, (1-q)*f, (1-r)*g⟩
def returnDen (g r : Rat) : Rat := 1-g+r*g
def returnNumer (g q r : Rat) : Rat := q*(1-g)+r*g
def criticalOutput (g q r : Rat) : Rat := returnDen g r / returnNumer g q r

def finiteReturns (k : Kernel) : Nat → Rat
  | 0 => k.a
  | n+1 => finiteReturns k n + k.b*k.c*k.d^n

/-- Enumerates direct return and return after 0 through n-1 P self-loops.
    Descendants are stopped at their first return, so paths are not counted
    again after they have already re-entered O. -/
theorem finite_return_identity (k : Kernel) : ∀ n,
    (1-k.d)*finiteReturns k n = k.a*(1-k.d)+k.b*k.c*(1-k.d^n) := by
  intro n
  induction n with
  | zero => simp [finiteReturns]; grind
  | succ n ih =>
    simp only [finiteReturns, Rat.pow_succ]
    grind

theorem total_descendants (f g q r o p : Rat) :
    nextO (developmental f g q r) o p +
      nextP (developmental f g q r) o p = f*o+g*p := by
  unfold nextO nextP developmental
  grind

theorem developmental_margin (f g q r : Rat) :
    margin (developmental f g q r) =
      f*returnNumer g q r - returnDen g r := by
  unfold margin developmental returnNumer returnDen
  grind

theorem output_threshold (f g q r : Rat)
    (h : 0 < returnNumer g q r) :
    0 < margin (developmental f g q r) ↔ criticalOutput g q r < f := by
  rw [developmental_margin]
  have hn : returnNumer g q r ≠ 0 := by grind
  have he : criticalOutput g q r * returnNumer g q r = returnDen g r := by
    unfold criticalOutput
    grind
  constructor
  · intro hm
    have hh : criticalOutput g q r * returnNumer g q r < f*returnNumer g q r := by grind
    exact (Rat.mul_lt_mul_right h).mp hh
  · intro hm
    have hh := Rat.mul_lt_mul_of_pos_right hm h
    grind

/-- Full biological parameter domain for the two-way developmental cycle. -/
theorem developmental_expansion_criterion (f g q r : Rat)
    (hf : 0 < f) (hg : 0 < g) (hg1 : g < 1)
    (hq0 : 0 ≤ q) (hq1 : q < 1) (hr0 : 0 < r) (_hr1 : r ≤ 1) :
    (∃ t, Expands (developmental f g q r) t) ↔ criticalOutput g q r < f := by
  have hb := Rat.mul_pos hr0 hg
  have hc := Rat.mul_pos (show 0 < 1-q by grind) hf
  have hd : (1-r)*g < 1 := by
    have hh := Rat.mul_le_mul_of_nonneg_right (show 1-r ≤ 1 by grind) (show 0 ≤ g by grind)
    grind
  have hn : 0 < returnNumer g q r := by
    have hh := Rat.mul_nonneg hq0 (show 0 ≤ 1-g by grind)
    unfold returnNumer
    grind
  exact (full_loop_criterion (developmental f g q r) hb hc hd).trans
    (output_threshold f g q r hn)

theorem developmental_nonnegative (f g q r : Rat)
    (hf : 0 ≤ f) (hg : 0 ≤ g) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1) :
    0 ≤ (developmental f g q r).a ∧ 0 ≤ (developmental f g q r).b ∧
    0 ≤ (developmental f g q r).c ∧ 0 ≤ (developmental f g q r).d := by
  exact ⟨Rat.mul_nonneg hq0 hf, Rat.mul_nonneg hr0 hg,
    Rat.mul_nonneg (by grind) hf, Rat.mul_nonneg (by grind) hg⟩

/-- The threshold supplies a common positive certificate for all initial
    nonnegative abundances and all finite times, under the fixed recurrence. -/
theorem developmental_growth_certificate (f g q r : Rat)
    (hf : 0 < f) (hg : 0 < g) (hg1 : g < 1)
    (hq0 : 0 ≤ q) (hq1 : q < 1) (hr0 : 0 < r) (hr1 : r ≤ 1)
    (hgain : criticalOutput g q r < f) :
    ∃ t e : Rat, 0 < t ∧ 0 < e ∧
      ∀ o p : Rat, 0 ≤ o → 0 ≤ p → ∀ n,
        (1+e)^n*value t o p ≤
          value t (history (fun _ => developmental f g q r) o p n).1
            (history (fun _ => developmental f g q r) o p n).2 := by
  obtain ⟨t,ht⟩ := (developmental_expansion_criterion f g q r hf hg hg1 hq0 hq1 hr0 hr1).mpr hgain
  obtain ⟨e,he,h1,h2⟩ := expansion_has_margin _ t ht
  refine ⟨t,e,ht.1,he,?_⟩
  intro o p ho hp n
  have hk := developmental_nonnegative f g q r (by grind) (by grind) hq0 (by grind) (by grind) hr1
  exact (uniform_history_bound (fun _ => developmental f g q r) t e o p ho hp
    (by grind) (fun _ => hk) (fun _ => ⟨h1,h2⟩) n).2.2

theorem uniform_nonexpansion (ks : Nat → Kernel) (t o p : Rat)
    (ho : 0 ≤ o) (hp : 0 ≤ p)
    (hk : ∀ n, 0 ≤ (ks n).a ∧ 0 ≤ (ks n).b ∧ 0 ≤ (ks n).c ∧ 0 ≤ (ks n).d)
    (hv : ∀ n o p, 0 ≤ o → 0 ≤ p →
      value t (nextO (ks n) o p) (nextP (ks n) o p) ≤ value t o p) :
    ∀ n, 0 ≤ (history ks o p n).1 ∧ 0 ≤ (history ks o p n).2 ∧
      value t (history ks o p n).1 (history ks o p n).2 ≤ value t o p := by
  intro n
  induction n with
  | zero => simp [history, ho, hp]
  | succ n ih =>
    obtain ⟨ha,hb,hc,hd⟩ := hk n
    refine ⟨Rat.add_nonneg (Rat.mul_nonneg ha ih.1) (Rat.mul_nonneg hb ih.2.1),
      Rat.add_nonneg (Rat.mul_nonneg hc ih.1) (Rat.mul_nonneg hd ih.2.1), ?_⟩
    exact Rat.le_trans (hv n _ _ ih.1 ih.2.1) ih.2.2

theorem threshold_exceeds_one (g q r : Rat) (hg : g < 1) (hq : q < 1)
    (hn : 0 < returnNumer g q r) : 1 < criticalOutput g q r := by
  have hp := Rat.mul_pos (show 0 < 1-q by grind) (show 0 < 1-g by grind)
  have hid : returnDen g r-returnNumer g q r = (1-q)*(1-g) := by
    unfold returnDen returnNumer
    grind
  have hne : returnNumer g q r ≠ 0 := by grind
  have heq : criticalOutput g q r * returnNumer g q r = returnDen g r := by
    unfold criticalOutput
    grind
  have hh : 1*returnNumer g q r < criticalOutput g q r*returnNumer g q r := by grind
  exact (Rat.mul_lt_mul_right hn).mp hh

theorem first_return_balance (f g q r o p : Rat) (h : returnDen g r ≠ 0) :
    value (r*g/returnDen g r) (nextO (developmental f g q r) o p)
      (nextP (developmental f g q r) o p) - value (r*g/returnDen g r) o p =
        (f*returnNumer g q r-returnDen g r)/returnDen g r*o := by
  unfold value nextO nextP developmental returnDen returnNumer at *
  grind

/-- A cost is paid in actual offspring production, not an analyst's reward. -/
theorem cost_ceiling (gross cost g q r : Rat)
    (h : 0 < returnNumer g q r) :
    0 < margin (developmental (gross-cost) g q r) ↔
      cost < gross-criticalOutput g q r := by
  rw [output_threshold (gross-cost) g q r h]
  grind

theorem reconstruction_threshold_identity (g q r₁ r₂ : Rat) :
    returnDen g r₁ * returnNumer g q r₂ -
      returnDen g r₂ * returnNumer g q r₁ =
        g*(1-g)*(1-q)*(r₂-r₁) := by
  unfold returnDen returnNumer
  grind

theorem reconstruction_lowers_threshold (g q r₁ r₂ : Rat)
    (hg : 0 < g) (hg1 : g < 1) (hq : q < 1) (hr : r₁ < r₂)
    (hn1 : 0 < returnNumer g q r₁) (hn2 : 0 < returnNumer g q r₂) :
    criticalOutput g q r₂ < criticalOutput g q r₁ := by
  have hp := Rat.mul_pos (Rat.mul_pos (Rat.mul_pos hg
    (show 0 < 1-g by grind)) (show 0 < 1-q by grind)) (show 0 < r₂-r₁ by grind)
  have he := reconstruction_threshold_identity g q r₁ r₂
  have hneq1 : returnNumer g q r₁ ≠ 0 := by grind
  have hneq2 : returnNumer g q r₂ ≠ 0 := by grind
  have hh : (criticalOutput g q r₁-criticalOutput g q r₂)*
      (returnNumer g q r₁*returnNumer g q r₂) =
      returnDen g r₁*returnNumer g q r₂-returnDen g r₂*returnNumer g q r₁ := by
    unfold criticalOutput
    grind
  have hpos : 0 < criticalOutput g q r₁-criticalOutput g q r₂ := by
    apply (Rat.mul_pos_iff_of_pos_right (Rat.mul_pos hn1 hn2)).mp
    grind
  grind

theorem no_creation_from_routing (f g q r o p : Rat)
    (hf : f ≤ 1) (hg : g ≤ 1) (ho : 0 ≤ o) (hp : 0 ≤ p) :
    nextO (developmental f g q r) o p +
      nextP (developmental f g q r) o p ≤ o+p := by
  rw [total_descendants]
  have h1 := Rat.mul_le_mul_of_nonneg_right hf ho
  have h2 := Rat.mul_le_mul_of_nonneg_right hg hp
  grind

/-- A census immediately after an O-only start contains no information about
    reconstruction from P, even if the whole two-state output is observed. -/
theorem first_census_nonidentification (f g q r₁ r₂ o : Rat) :
    nextO (developmental f g q r₁) o 0 = nextO (developmental f g q r₂) o 0 ∧
    nextP (developmental f g q r₁) o 0 = nextP (developmental f g q r₂) o 0 := by
  unfold nextO nextP developmental
  grind

theorem second_census_contrast (f g q r₁ r₂ o : Rat) :
    (history (fun _ => developmental f g q r₂) o 0 2).1 -
      (history (fun _ => developmental f g q r₁) o 0 2).1 =
        g*(1-q)*f*o*(r₂-r₁) := by
  simp only [history, nextO, nextP, developmental]
  grind

theorem second_census_identifies_reconstruction (f g q r₁ r₂ o : Rat)
    (hf : 0 < f) (hg : 0 < g) (hq : q < 1) (ho : 0 < o)
    (heq : (history (fun _ => developmental f g q r₂) o 0 2).1 =
      (history (fun _ => developmental f g q r₁) o 0 2).1) : r₂ = r₁ := by
  have hh := second_census_contrast f g q r₁ r₂ o
  have hp := Rat.mul_pos (Rat.mul_pos (Rat.mul_pos hg (show 0 < 1-q by grind)) hf) ho
  have hn : g*(1-q)*f*o ≠ 0 := by grind
  have hzero : g*(1-q)*f*o*(r₂-r₁) = 0 := by grind
  have he := (Rat.mul_eq_zero.mp hzero).resolve_left hn
  grind

theorem indistinguishable_first_census_opposite_margins :
    nextO (developmental (3/2) (1/2) (2/5) 0) 1 0 =
      nextO (developmental (3/2) (1/2) (2/5) 1) 1 0 ∧
    nextP (developmental (3/2) (1/2) (2/5) 0) 1 0 =
      nextP (developmental (3/2) (1/2) (2/5) 1) 1 0 ∧
    margin (developmental (3/2) (1/2) (2/5) 0) < 0 ∧
    0 < margin (developmental (3/2) (1/2) (2/5) 1) := by
  decide +kernel

/-- Direct resemblance can be zero while the two-stage lineage expands. -/
theorem reconstruction_without_direct_copy :
    Expands (developmental 3 (1/2) 0 1) (2/5) := by
  unfold Expands
  decide +kernel

/-- Less direct resemblance and a fecundity cost can accompany a gaining rule.
    The comparison is against the supplied resident factor 1, not pairwise
    competitive exclusion in an independently changing ecology. -/
theorem costly_reconstruction_can_cross_threshold :
    margin (developmental (8/5) (1/2) (1/2) 0) < 0 ∧
    3/2 < (8:Rat)/5 ∧
    (2:Rat)/5 < 1/2 ∧
    Expands (developmental (3/2) (1/2) (2/5) 1) (17/36) := by
  unfold Expands
  decide +kernel

theorem reconstruction_can_be_too_costly :
    margin (developmental 1 (1/2) (2/5) 1) < 0 := by
  decide +kernel

theorem lost_return_prevents_this_gain :
    ¬ ∃ t, Expands (developmental 3 (1/2) 0 0) t := by
  intro ⟨t,ht,h1,h2⟩
  change t < (0:Rat)*(1/2)+(1-0)*(1/2)*t at h2
  grind

end ReconstructiveSelection
