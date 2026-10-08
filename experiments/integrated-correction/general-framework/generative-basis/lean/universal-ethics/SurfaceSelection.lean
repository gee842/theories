import Std

/-!
Rational local-balance correspondence to Karita et al. (2026), supplement C.
This is algebra for a specified conventional model, not an ODE existence,
trajectory, fixation or empirical calibration proof. Surface/bulk roles refer
to locations differentiated in one material history. `rs,rw,ds,dw` are supplied
rates; the saturated slice has zero immigration and zero mutation unless an
explicit flux is added. The source notebook's `switch` is fixed at 1.
-/
namespace SurfaceSelection

def denominator (s w ds dw : Rat) : Rat := ds*s + dw*w
def births (s w rs rw : Rat) : Rat := rs*s + rw*w
def sNet (s w rs rw ds dw : Rat) : Rat :=
  rs*s - ds*s / denominator s w ds dw * births s w rs rw
def wNet (s w rs rw ds dw : Rat) : Rat :=
  rw*w - dw*w / denominator s w ds dw * births s w rs rw

/-- Surface loss arrives in the bulk; mutation and migration redistribute cells.
    None of these fluxes becomes extra total production. -/
theorem four_location_balance
    (gsA gwA gsB gwB ds dw ms mw mutA mutB : Rat) :
    (gsA-ds+ms-mutA) + (gwA-dw+mw+mutA) +
    (gsB+ds-ms-mutB) + (gwB+dw-mw+mutB) = gsA+gwA+gsB+gwB := by
  grind

theorem saturation_balance (s w rs rw ds dw : Rat)
    (hd : denominator s w ds dw ≠ 0) :
    sNet s w rs rw ds dw + wNet s w rs rw ds dw = 0 := by
  unfold sNet wNet births denominator at *
  grind

theorem retained_growth_identity (s w rs rw ds dw : Rat)
    (hd : denominator s w ds dw ≠ 0) :
    wNet s w rs rw ds dw = s*w*(rw*ds-rs*dw) / denominator s w ds dw := by
  unfold wNet births denominator at *
  grind

/-- Includes an explicitly supplied net mutation flux in the surface slice.
    With mutation, the retention contrast alone no longer gives the sign. -/
theorem mutation_adjusted_balance (s w rs rw ds dw flux : Rat)
    (hd : denominator s w ds dw ≠ 0) :
    (wNet s w rs rw ds dw + flux) * denominator s w ds dw =
    s*w*(rw*ds-rs*dw) + flux*denominator s w ds dw := by
  unfold wNet births denominator at *
  grind

theorem gain_criterion (s w rs rw ds dw : Rat)
    (hs : 0 < s) (hw : 0 < w) (hd : 0 < denominator s w ds dw) :
    0 < wNet s w rs rw ds dw ↔ rs*dw < rw*ds := by
  have hn : denominator s w ds dw ≠ 0 := by grind
  rw [retained_growth_identity s w rs rw ds dw hn]
  change 0 < (s*w*(rw*ds-rs*dw)) * (denominator s w ds dw)⁻¹ ↔ rs*dw < rw*ds
  rw [Rat.mul_pos_iff_of_pos_right (Rat.inv_pos.mpr hd),
      Rat.mul_pos_iff_of_pos_left (Rat.mul_pos hs hw)]
  exact (Rat.lt_iff_sub_pos (rs*dw) (rw*ds)).symm

/-- Exact source-rate slice at equal positive abundances; no empirical estimate. -/
theorem source_rates_allow_slow_growth_gain :
    (17:Rat)/20 < 1 ∧
    wNet 1 1 1 (17/20) (1/500) (1/1000) = 7/30 := by
  decide +kernel

/-- Lower dispersal alone does not guarantee gain when the growth loss is larger. -/
theorem lower_dispersal_can_still_lose :
    (1:Rat)/1000 < 1/500 ∧
    wNet 1 1 1 (1/4) (1/500) (1/1000) = -(1/6) := by
  decide +kernel

end SurfaceSelection
