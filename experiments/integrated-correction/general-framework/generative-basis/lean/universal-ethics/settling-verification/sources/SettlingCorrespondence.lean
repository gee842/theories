import Std

/-!
Algebra for declared settling correspondences, 8 October 2026.
Volumes, density contrasts and drag proxies are local descriptions of one
material/fluid configuration. This module proves rational algebra only. It does
not derive Stokes drag, a hydrodynamic radius, permeability, fracture or fitness.
Physical positivity/packing conditions belong to the correspondence audit;
algebraic identities may hold on a larger rational domain.
-/
namespace SettlingCorrespondence

def bulkMass (solid envelope cellDensity fluidDensity : Rat) : Rat :=
  solid * cellDensity + (envelope - solid) * fluidDensity

theorem excess_mass_from_constituents (solid envelope cellDensity fluidDensity : Rat) :
    bulkMass solid envelope cellDensity fluidDensity - envelope * fluidDensity =
      solid * (cellDensity - fluidDensity) := by
  unfold bulkMass
  grind

theorem effective_contrast_accounts_for_volume (solid envelope contrast : Rat)
    (nonzero : envelope ≠ 0) :
    ((solid * contrast) / envelope) * envelope = solid * contrast :=
  Rat.div_mul_cancel nonzero

/-- Common positive dimensional factors are omitted from these two scores.
The coefficient c represents the envelope-volume factor, e.g. 4*pi/3 in a
real-valued spherical correspondence; no claim that pi is rational is made. -/
def uniformScore (radius coefficient : Rat) : Rat := coefficient * radius * radius
def materialScore (solid radius : Rat) : Rat := solid / radius

theorem sphere_density_correction (solid radius coefficient : Rat)
    (radius_ne : radius ≠ 0) (coefficient_ne : coefficient ≠ 0) :
    (solid / (coefficient * radius * radius * radius)) *
        uniformScore radius coefficient = materialScore solid radius := by
  unfold uniformScore materialScore
  have hd : coefficient * radius * radius * radius ≠ 0 := by
    simp [Rat.mul_eq_zero, coefficient_ne, radius_ne]
  have h1 := Rat.div_mul_cancel (a := solid) hd
  have h2 := Rat.div_mul_cancel (a := solid) radius_ne
  have h3 : ((solid / (coefficient * radius * radius * radius)) *
      (coefficient * radius * radius) - solid / radius) * radius = 0 := by grind
  rcases Rat.mul_eq_zero.mp h3 with h | h
  · grind
  · exact False.elim (radius_ne h)

theorem agreement_requires_filled_envelope (solid radius coefficient : Rat)
    (radius_ne : radius ≠ 0) :
    uniformScore radius coefficient = materialScore solid radius ↔
      solid = coefficient * radius * radius * radius := by
  unfold uniformScore materialScore
  have h2 := Rat.div_mul_cancel (a := solid) radius_ne
  constructor
  · intro h; grind
  · intro h
    have hh : (coefficient * radius * radius - solid / radius) * radius = 0 := by grind
    rcases Rat.mul_eq_zero.mp hh with hz | hz
    · grind
    · exact False.elim (radius_ne hz)

/-- Relative drag is an additional physical input, not set by a density audit.
If its reduction equals the solid fraction, the two speed scores agree. -/
def relativeDragScore (solidFraction relativeDrag uniform : Rat) : Rat :=
  (solidFraction / relativeDrag) * uniform

theorem permeability_can_offset_density (fraction uniform : Rat)
    (nonzero : fraction ≠ 0) : relativeDragScore fraction fraction uniform = uniform := by
  unfold relativeDragScore
  have h : fraction / fraction = 1 := by
    rw [Rat.div_def, Rat.mul_inv_cancel fraction nonzero]
  rw [h, Rat.one_mul]

/-- Both example solid volumes fit inside their c=1 envelopes. This is an
idealized conditional witness, not an observed yeast pair. -/
theorem equal_material_larger_radius_reverses_order :
    (100 : Rat) < 5 * 5 * 5 ∧ (100 : Rat) < 6 * 6 * 6 ∧
    uniformScore 5 1 < uniformScore 6 1 ∧
    materialScore 100 6 < materialScore 100 5 := by decide +kernel

/-- Exact squared radius proxies from Day 2022 coordinate files 01 and 04.
The decimal-coordinate and radius-gyration extraction is checked separately. -/
def radiusSquared01 : Rat := 1698677849312322677 / 9830400000000000
def radiusSquared04 : Rat := 1024674525495734117 / 6482700000000000

/-- Compare squared material scores N^2/R^2, with common positive cell volume
and dimensional constants omitted. The formal scope is these rational scores,
not a theorem that either velocity approximation is physically accurate. -/
theorem measured_geometry_scores_reverse :
    0 < radiusSquared04 ∧ radiusSquared04 < radiusSquared01 ∧
    (128 : Rat) * 128 / radiusSquared01 <
      (147 : Rat) * 147 / radiusSquared04 := by decide +kernel

end SettlingCorrespondence
