import Std

/-!
# Offered-choice bounds for a finite rational paired population

The paired units, conditional probabilities, response gates and covered set
are supplied. No aggregate response difference is treated as a pointwise gate
bound. Real logistic interpretation and empirical identification remain outside
this rational theorem. Sharpness here allows endpoint probabilities zero/one;
finite real logits may only approach those endpoints.
-/

namespace OfferedChoice

structure Pair where
  weight : Rat
  r0 : Rat
  r1 : Rat
  p0 : Rat
  p1 : Rat
  covered : Bool
  deriving DecidableEq, Repr

def Pair.overlap (x : Pair) : Rat := if x.covered then min x.r0 x.r1 else 0
def Pair.bad (x : Pair) : Rat := if x.covered then 0 else 1

def Pair.Valid (m : Rat) (x : Pair) : Prop :=
  0 ≤ x.weight ∧ 0 ≤ x.r0 ∧ x.r0 ≤ 1 ∧ 0 ≤ x.r1 ∧ x.r1 ≤ 1 ∧
  0 ≤ x.p0 ∧ x.p0 ≤ 1 ∧ 0 ≤ x.p1 ∧ x.p1 ≤ 1 ∧
  (x.covered = true → x.p1 - x.p0 ≤ m ∧ x.p0 - x.p1 ≤ m)

def Valid (m : Rat) (rows : List Pair) : Prop := ∀ x ∈ rows, x.Valid m

def total (rows : List Pair) (f : Pair → Rat) : Rat :=
  rows.foldr (fun x tail => x.weight * f x + tail) 0

def R0 (rows : List Pair) := total rows Pair.r0
def R1 (rows : List Pair) := total rows Pair.r1
def L0 (rows : List Pair) := total rows (fun x => x.r0 * x.p0)
def L1 (rows : List Pair) := total rows (fun x => x.r1 * x.p1)

theorem total_add (rows : List Pair) (f g : Pair → Rat) :
    total rows (fun x => f x + g x) = total rows f + total rows g := by
  induction rows with
  | nil => simp only [total, List.foldr_nil]; grind
  | cons x rows ih => simp only [total, List.foldr_cons] at *; grind

theorem total_sub (rows : List Pair) (f g : Pair → Rat) :
    total rows (fun x => f x - g x) = total rows f - total rows g := by
  induction rows with
  | nil => simp only [total, List.foldr_nil]; grind
  | cons x rows ih => simp only [total, List.foldr_cons] at *; grind

theorem total_scale (rows : List Pair) (c : Rat) (f : Pair → Rat) :
    total rows (fun x => c * f x) = c * total rows f := by
  induction rows with
  | nil => simp [total]
  | cons x rows ih => simp only [total, List.foldr_cons] at *; grind

theorem total_mono (rows : List Pair) (f g : Pair → Rat)
    (weights : ∀ x ∈ rows, 0 ≤ x.weight)
    (pointwise : ∀ x ∈ rows, f x ≤ g x) : total rows f ≤ total rows g := by
  induction rows with
  | nil => simp [total]
  | cons x rows ih =>
    have head := Rat.mul_le_mul_of_nonneg_left
      (pointwise x (by simp)) (weights x (by simp))
    have tail := ih (by intro y hy; exact weights y (by simp [hy]))
      (by intro y hy; exact pointwise y (by simp [hy]))
    simp only [total, List.foldr_cons] at *
    grind

theorem overlap_bounds {m : Rat} {x : Pair} (valid : x.Valid m) :
    0 ≤ x.overlap ∧ x.r0 + x.r1 - 1 - x.bad ≤ x.overlap := by
  unfold Pair.overlap Pair.bad
  rcases valid with ⟨_, hr0, hr01, hr1, hr11, _⟩
  split <;> grind

theorem pointwise_gap {m : Rat} {x : Pair} (valid : x.Valid m) :
    x.r1 * x.p1 - x.r0 * x.p0 ≤ x.r1 - (1-m) * x.overlap := by
  rcases valid with ⟨_, hr0, hr01, hr1, hr11, hp0, hp01, hp1, hp11, gap⟩
  unfold Pair.overlap
  split
  · rename_i covered
    have hg := (gap covered).1
    by_cases gates : x.r0 ≤ x.r1
    · have d : 0 ≤ x.r1 - x.r0 := by grind
      have h := Rat.mul_le_mul_of_nonneg_left hp11 d
      have k := Rat.mul_le_mul_of_nonneg_left hg hr0
      grind
    · have gates' : x.r1 ≤ x.r0 := by grind
      have d : 0 ≤ x.r0 - x.r1 := by grind
      have h := Rat.mul_nonneg d hp0
      have k := Rat.mul_le_mul_of_nonneg_left hg hr1
      grind
  · have h := Rat.mul_le_mul_of_nonneg_left hp11 hr1
    have k := Rat.mul_nonneg hr0 hp0
    grind

theorem good_overlap_lower {m epsilon : Rat} {rows : List Pair}
    (valid : Valid m rows) (normalized : total rows (fun _ => 1) = 1)
    (uncovered : total rows Pair.bad ≤ epsilon) :
    max 0 (R0 rows + R1 rows - 1 - epsilon) ≤ total rows Pair.overlap := by
  have weights : ∀ x ∈ rows, 0 ≤ x.weight := fun x hx => (valid x hx).1
  have positive := total_mono rows (fun _ => 0) Pair.overlap weights
    (fun x hx => (overlap_bounds (valid x hx)).1)
  have lower := total_mono rows (fun x => x.r0+x.r1-1-x.bad) Pair.overlap weights
    (fun x hx => (overlap_bounds (valid x hx)).2)
  have zero : total rows (fun _ => 0) = 0 := by
    have h := total_scale rows 0 (fun _ => 1)
    simpa using h
  rw [total_sub, total_sub, total_add] at lower
  change R0 rows + R1 rows - total rows (fun _ => 1) - total rows Pair.bad ≤ _ at lower
  rw [zero] at positive
  rw [normalized] at lower
  grind

/-- Signed frontier using marginal gate means and a paired covered set. -/
theorem signed_population_bound {m epsilon : Rat} {rows : List Pair}
    (valid : Valid m rows) (_hm0 : 0 ≤ m) (hm1 : m ≤ 1)
    (normalized : total rows (fun _ => 1) = 1)
    (uncovered : total rows Pair.bad ≤ epsilon) :
    L1 rows - L0 rows ≤
      R1 rows - (1-m) * max 0 (R0 rows + R1 rows - 1 - epsilon) := by
  have pointwise := total_mono rows (fun x => x.r1*x.p1-x.r0*x.p0)
    (fun x => x.r1-(1-m)*x.overlap)
    (fun x hx => (valid x hx).1) (fun x hx => pointwise_gap (valid x hx))
  rw [total_sub, total_sub, total_scale] at pointwise
  have lower := good_overlap_lower valid normalized uncovered
  have product := Rat.mul_le_mul_of_nonneg_left lower (show 0 ≤ 1-m by grind)
  change L1 rows - L0 rows ≤ R1 rows - (1-m)*total rows Pair.overlap at pointwise
  grind

def Pair.swap (x : Pair) : Pair :=
  { x with r0 := x.r1, r1 := x.r0, p0 := x.p1, p1 := x.p0 }

theorem swap_valid {m : Rat} {x : Pair} (valid : x.Valid m) : x.swap.Valid m := by
  unfold Pair.Valid Pair.swap at *
  grind

theorem total_map_swap (rows : List Pair) (f : Pair → Rat) :
    total (rows.map Pair.swap) f = total rows (fun x => f x.swap) := by
  induction rows with
  | nil => simp [total]
  | cons x rows ih => simpa [total, Pair.swap] using congrArg (fun z => x.weight*f x.swap+z) ih

/-- The negative side uses R0; it is not obtained by assuming equal response. -/
theorem mirrored_population_bound {m epsilon : Rat} {rows : List Pair}
    (valid : Valid m rows) (hm0 : 0 ≤ m) (hm1 : m ≤ 1)
    (normalized : total rows (fun _ => 1) = 1)
    (uncovered : total rows Pair.bad ≤ epsilon) :
    L0 rows - L1 rows ≤
      R0 rows - (1-m) * max 0 (R0 rows + R1 rows - 1 - epsilon) := by
  have sv : Valid m (rows.map Pair.swap) := by
    intro x hx
    obtain ⟨y, hy, rfl⟩ := List.mem_map.mp hx
    exact swap_valid (valid y hy)
  have sn : total (rows.map Pair.swap) (fun _ => 1) = 1 := by
    simpa only [total_map_swap] using normalized
  have su : total (rows.map Pair.swap) Pair.bad ≤ epsilon := by
    simpa only [total_map_swap, Pair.bad, Pair.swap] using uncovered
  have h := signed_population_bound sv hm0 hm1 sn su
  simp only [L0, L1, R0, R1, total_map_swap, Pair.swap] at h ⊢
  grind

/-- Minimal binary-gate intersection, with uncovered mass placed there first. -/
def sharpPopulation (u v epsilon m : Rat) : List Pair :=
  let intersection := max 0 (u+v-1)
  let bad := min epsilon intersection
  [⟨intersection-bad, 1, 1, (1-m)/2, (1+m)/2, true⟩,
   ⟨bad, 1, 1, 0, 1, false⟩,
   ⟨v-intersection, 0, 1, 1, 1, true⟩,
   ⟨u-intersection, 1, 0, 0, 0, true⟩,
   ⟨1-u-v+intersection, 0, 0, 0, 0, true⟩]

theorem sharp_population_valid {u v epsilon m : Rat}
    (hu0 : 0 ≤ u) (hu1 : u ≤ 1) (hv0 : 0 ≤ v) (hv1 : v ≤ 1)
    (he : 0 ≤ epsilon) (hm0 : 0 ≤ m) (hm1 : m ≤ 1) :
    Valid m (sharpPopulation u v epsilon m) := by
  intro x hx
  simp only [sharpPopulation, List.mem_cons, List.not_mem_nil, or_false] at hx
  rcases hx with rfl | rfl | rfl | rfl | rfl <;> simp only [Pair.Valid] <;> grind

theorem sharp_population_account {u v epsilon m : Rat} :
    let rows := sharpPopulation u v epsilon m
    total rows (fun _ => 1) = 1 ∧ R0 rows = u ∧ R1 rows = v ∧
      total rows Pair.bad ≤ epsilon := by
  simp only [sharpPopulation, total, List.foldr_cons, List.foldr_nil, R0, R1, Pair.bad]
  grind

/-- Attainment for the probability-gap class, including fractional gate means.
Finite-logit models require endpoint limits for some of these strata. -/
theorem sharp_population_attains {u v epsilon m : Rat}
    (he : 0 ≤ epsilon) :
    let rows := sharpPopulation u v epsilon m
    L1 rows - L0 rows = v-(1-m)*max 0 (u+v-1-epsilon) := by
  have overlap : max 0 (u+v-1) - min epsilon (max 0 (u+v-1)) =
      max 0 (u+v-1-epsilon) := by grind
  simp only [sharpPopulation, total, List.foldr_cons, List.foldr_nil, L0, L1]
  grind

/-- Equal response fractions alone do not identify matched response gates. -/
theorem disjoint_gate_counterexample :
    let rows := sharpPopulation (1/2) (1/2) 0 0
    Valid 0 rows ∧ total rows (fun _ => 1) = 1 ∧
      R0 rows = 1/2 ∧ R1 rows = 1/2 ∧ total rows Pair.bad = 0 ∧
      L1 rows - L0 rows = 1/2 := by
  constructor
  · exact sharp_population_valid (by grind) (by grind) (by grind) (by grind)
      (by grind) (by grind) (by grind)
  · simp only [sharpPopulation, total, List.foldr_cons, List.foldr_nil, R0, R1, L0, L1, Pair.bad]
    grind

/-- m=1/3 is attained by the logistic odds pair 1/2 and 2 (ratio four). -/
theorem rational_frontier_example :
    let rows := sharpPopulation (3/4) (4/5) (1/10) (1/3)
    Valid (1/3) rows ∧ total rows (fun _ => 1) = 1 ∧
      R0 rows = 3/4 ∧ R1 rows = 4/5 ∧ total rows Pair.bad = 1/10 ∧
      L1 rows - L0 rows = 1/2 := by
  constructor
  · exact sharp_population_valid (by grind) (by grind) (by grind) (by grind)
      (by grind) (by grind) (by grind)
  · simp only [sharpPopulation, total, List.foldr_cons, List.foldr_nil, R0, R1, L0, L1, Pair.bad]
    grind

end OfferedChoice

#print axioms OfferedChoice.total_add
#print axioms OfferedChoice.total_sub
#print axioms OfferedChoice.total_scale
#print axioms OfferedChoice.total_mono
#print axioms OfferedChoice.overlap_bounds
#print axioms OfferedChoice.pointwise_gap
#print axioms OfferedChoice.good_overlap_lower
#print axioms OfferedChoice.signed_population_bound
#print axioms OfferedChoice.swap_valid
#print axioms OfferedChoice.total_map_swap
#print axioms OfferedChoice.mirrored_population_bound
#print axioms OfferedChoice.sharp_population_valid
#print axioms OfferedChoice.sharp_population_account
#print axioms OfferedChoice.sharp_population_attains
#print axioms OfferedChoice.disjoint_gate_counterexample
#print axioms OfferedChoice.rational_frontier_example
