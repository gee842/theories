/-!
# One-generation coupling of shared support and relative transmission

Two collectives are differentiated reproducing configurations within one
declared process, not independent substances. The support-producing structure
is identified by its contribution to shared support before descendant counts
are compared. The other structure shares access but has a higher per-carrier
descendant rate. Neither structure is assigned an ethical predicate.

The support law, initial compositions, faithful transmission, equal access,
integer conversion factors and one-generation timing are supplied. The model
does not derive biology, group formation, long-run evolution or moral warrant.
No division is used: positive-total frequencies are compared by cross products.
-/

namespace RecursiveGenerativeSelection

/-- Constructive arithmetic helpers avoid standard library lemmas whose proof
    implementations carry additional axioms. They add no biological premises. -/
theorem mul_assoc_eq (a b : Nat) : ∀ c : Nat, a * b * c = a * (b * c)
  | 0 => rfl
  | c + 1 => by rw [Nat.mul_succ, Nat.mul_succ, Nat.mul_add, mul_assoc_eq a b c]

theorem add_mul_eq (a b c : Nat) : (a + b) * c = a * c + b * c := by
  rw [Nat.mul_comm, Nat.mul_add, Nat.mul_comm c a, Nat.mul_comm c b]

theorem strict_mul_cancel_right {a b factor : Nat}
    (comparison : a * factor < b * factor) : a < b := by
  cases Nat.lt_or_ge a b with
  | inl smaller => exact smaller
  | inr larger =>
      exact False.elim (Nat.not_lt_of_ge (Nat.mul_le_mul_right factor larger) comparison)

/-- Actual shared support in this supplied law. A supporter contributes
    `strength`; no term is defined by eventual reproductive success. -/
def support (base strength supporters : Nat) : Nat := base + strength * supporters

/-- Descendants faithfully carry the parental response structure. Support
    multiplies both channels; the specified within-collective rates are 2, 3. -/
def descendants (base strength supporters others : Nat) : Nat × Nat :=
  (support base strength supporters * (2 * supporters),
   support base strength supporters * (3 * others))

/-- Both collectives initially contain four carriers, with compositions 3:1
    and 1:3. Pooling introduces no further mutation, sorting or loss. -/
def pooled (base strength : Nat) : Nat × Nat :=
  ((descendants base strength 3 1).1 + (descendants base strength 1 3).1,
   (descendants base strength 3 1).2 + (descendants base strength 1 3).2)

/-- Generic cancellation of shared products. Fraction interpretation requires
    the two population totals to be positive, separately from this identity. -/
theorem cross_compare_iff (a h afterA afterH : Nat) :
    a * (afterA + afterH) < afterA * (a + h) ↔ a * afterH < afterA * h := by
  rw [Nat.mul_add, Nat.mul_add, Nat.mul_comm afterA a]
  constructor
  · exact Nat.lt_of_add_lt_add_left
  · exact fun comparison => Nat.add_lt_add_left comparison _

theorem more_supporters_produce_more_support (base strength a b : Nat)
    (productive : 0 < strength) (more : a < b) :
    support base strength a < support base strength b :=
  Nat.add_lt_add_left (Nat.mul_lt_mul_of_pos_left more productive) base

/-- A productive shared consequence does not remove the relative transmission
    disadvantage within this collective. Both types and actual support exist. -/
theorem supporter_share_falls_within (base strength a h : Nat)
    (supportExists : 0 < support base strength a) (aExists : 0 < a) (hExists : 0 < h) :
    (descendants base strength a h).1 * (a + h) <
      a * ((descendants base strength a h).1 + (descendants base strength a h).2) := by
  apply (cross_compare_iff (descendants base strength a h).1
    (descendants base strength a h).2 a h).mpr
  change (support base strength a * (2 * a)) * h <
    a * (support base strength a * (3 * h))
  calc
    (support base strength a * (2 * a)) * h =
        2 * (support base strength a * a * h) := by
          rw [← mul_assoc_eq (support base strength a) 2 a,
            Nat.mul_comm (support base strength a) 2,
            mul_assoc_eq 2 (support base strength a) a,
            mul_assoc_eq 2 (support base strength a * a) h]
    _ < 3 * (support base strength a * a * h) :=
      Nat.mul_lt_mul_of_pos_right (by decide)
        (Nat.mul_pos (Nat.mul_pos supportExists aExists) hExists)
    _ = a * (support base strength a * (3 * h)) := by
      rw [← mul_assoc_eq 3 (support base strength a * a) h,
        Nat.mul_comm 3 (support base strength a * a),
        mul_assoc_eq (support base strength a * a) 3 h,
        Nat.mul_comm (support base strength a) a,
        mul_assoc_eq a (support base strength a) (3 * h)]

theorem descendant_totals_positive (base strength a h : Nat)
    (supportExists : 0 < support base strength a) (aExists : 0 < a) :
    0 < (descendants base strength a h).1 + (descendants base strength a h).2 :=
  Nat.lt_of_lt_of_le
    (Nat.mul_pos supportExists (Nat.mul_pos (by decide) aExists))
    (Nat.le_add_right _ _)

theorem pooled_counts (base strength : Nat) :
    pooled base strength = (8 * base + 20 * strength, 12 * base + 18 * strength) := by
  apply Prod.ext
  · change (base + strength * 3) * 6 + (base + strength * 1) * 2 =
      8 * base + 20 * strength
    calc
      _ = (base * 6 + strength * 18) + (base * 2 + strength * 2) := by
        rw [add_mul_eq, add_mul_eq, mul_assoc_eq, Nat.mul_one]
      _ = base * 8 + strength * 20 := by
        rw [show base * 8 = base * 6 + base * 2 from Nat.mul_add base 6 2,
            show strength * 20 = strength * 18 + strength * 2 from
              Nat.mul_add strength 18 2]
        exact Nat.add_add_add_comm _ _ _ _
      _ = 8 * base + 20 * strength := by
        rw [Nat.mul_comm base 8, Nat.mul_comm strength 20]
  · change (base + strength * 3) * 3 + (base + strength * 1) * 9 =
      12 * base + 18 * strength
    calc
      _ = (base * 3 + strength * 9) + (base * 9 + strength * 9) := by
        rw [add_mul_eq, add_mul_eq, mul_assoc_eq, Nat.mul_one]
      _ = base * 12 + strength * 18 := by
        rw [show base * 12 = base * 3 + base * 9 from Nat.mul_add base 3 9,
            show strength * 18 = strength * 9 + strength * 9 from
              Nat.mul_add strength 9 9]
        exact Nat.add_add_add_comm _ _ _ _
      _ = 12 * base + 18 * strength := by
        rw [Nat.mul_comm base 12, Nat.mul_comm strength 18]

/-- The contribution due to support generation must overcome the specified
    within-collective disadvantage, not merely be positive. -/
theorem support_contribution_threshold (base strength : Nat) :
    12 * base + 18 * strength < 8 * base + 20 * strength ↔ 2 * base < strength := by
  have left : 12 * base + 18 * strength =
      (8 * base + 18 * strength) + (2 * base) * 2 := by
    have doubled : (2 * base) * 2 = 4 * base := by
      calc
        (2 * base) * 2 = 2 * (base * 2) := mul_assoc_eq 2 base 2
        _ = 2 * (2 * base) := congrArg (fun n => 2 * n) (Nat.mul_comm base 2)
        _ = (2 * 2) * base := (mul_assoc_eq 2 2 base).symm
    rw [show 12 * base = 8 * base + 4 * base from add_mul_eq 8 4 base, doubled]
    exact Nat.add_right_comm _ _ _
  have right : 8 * base + 20 * strength =
      (8 * base + 18 * strength) + strength * 2 := by
    rw [show 20 * strength = 18 * strength + 2 * strength from
      add_mul_eq 18 2 strength, Nat.mul_comm strength 2]
    exact (Nat.add_assoc _ _ _).symm
  rw [left, right]
  constructor
  · intro comparison
    exact strict_mul_cancel_right (Nat.lt_of_add_lt_add_left comparison)
  · intro comparison
    exact Nat.add_lt_add_left (Nat.mul_lt_mul_of_pos_right comparison (by decide)) _

/-- Exact global frequency criterion for this matched family. The algebra also
    holds when all output is zero; frequency language then does not apply. -/
theorem global_supporter_share_rises_iff (base strength : Nat) :
    4 * ((pooled base strength).1 + (pooled base strength).2) <
      (pooled base strength).1 * 8 ↔ 2 * base < strength := by
  change 4 * ((pooled base strength).1 + (pooled base strength).2) <
      (pooled base strength).1 * (4 + 4) ↔ _
  apply (cross_compare_iff 4 4 (pooled base strength).1 (pooled base strength).2).trans
  rw [pooled_counts, Nat.mul_comm (8 * base + 20 * strength) 4]
  change 4 * (12 * base + 18 * strength) < 4 * (8 * base + 20 * strength) ↔ _
  constructor
  · intro comparison
    rw [Nat.mul_comm 4 (12 * base + 18 * strength),
      Nat.mul_comm 4 (8 * base + 20 * strength)] at comparison
    exact (support_contribution_threshold base strength).mp
      (strict_mul_cancel_right comparison)
  · intro comparison
    exact Nat.mul_lt_mul_of_pos_left
      ((support_contribution_threshold base strength).mpr comparison) (by decide)

/-- Weak coupling: the support-rich collective contributes more descendants;
    producers lose share in each collective AND in the pooled continuation. -/
theorem weak_coupling_witness :
    let rich := descendants 1 1 3 1
    let poor := descendants 1 1 1 3
    let total := pooled 1 1
    support 1 1 1 < support 1 1 3 ∧
    rich = (24, 12) ∧ poor = (4, 18) ∧ total = (28, 30) ∧
    0 < rich.1 + rich.2 ∧ 0 < poor.1 + poor.2 ∧
    poor.1 + poor.2 < rich.1 + rich.2 ∧
    rich.1 * 4 < 3 * (rich.1 + rich.2) ∧
    poor.1 * 4 < 1 * (poor.1 + poor.2) ∧
    total.1 * 8 < 4 * (total.1 + total.2) := by
  decide

/-- Stronger coupling under the same timing, transmission, initial assortment
    and relative rates: within-group loss coexists with pooled increase. -/
theorem strong_coupling_witness :
    let rich := descendants 1 3 3 1
    let poor := descendants 1 3 1 3
    let total := pooled 1 3
    support 1 3 1 < support 1 3 3 ∧
    rich = (60, 30) ∧ poor = (8, 36) ∧ total = (68, 66) ∧
    0 < rich.1 + rich.2 ∧ 0 < poor.1 + poor.2 ∧
    poor.1 + poor.2 < rich.1 + rich.2 ∧
    rich.1 * 4 < 3 * (rich.1 + rich.2) ∧
    poor.1 * 4 < 1 * (poor.1 + poor.2) ∧
    4 * (total.1 + total.2) < total.1 * 8 := by
  decide

end RecursiveGenerativeSelection
