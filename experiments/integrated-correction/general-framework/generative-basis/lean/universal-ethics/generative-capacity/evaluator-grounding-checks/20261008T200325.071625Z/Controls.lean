import EvaluatorGrounding
open EvaluatorGrounding GenerativeComparison

-- With tolerance, the finite standpoint's self-good yields G0 for its reachable inventory.
example (val : Nat → Prop) (self : SelfGood (standpoint val)) (tol : Tolerant val adjacent)
    (chain : ∀ g', (standpoint val).reach g' → (standpoint val).living g' →
      ∃ g, (standpoint val).own g ∧ (standpoint val).living g ∧
        Chain adjacent ((standpoint val).prof g) ((standpoint val).prof g')) :
    G0 (reachableInventory (standpoint val)) (fun _ g => (standpoint val).sig g) :=
  self_good_derives_reachable_g0 (standpoint val) val adjacent (fun _ _ => Iff.rfl) self tol chain

-- The threshold rival is exactly where the tolerance-free step stops: formed other yes, stranger no.
example : (standpoint (4 ≤ ·)).sig .formedOther ∧ ¬ (standpoint (4 ≤ ·)).sig .stranger :=
  ⟨threshold_rival_is_consistent_without_tolerance.2.2.2.1,
   threshold_rival_is_consistent_without_tolerance.2.2.2.2.1⟩

-- The strictly own-only rival fails in the finite unfolding once self-good and monotonicity hold.
example (val : Nat → Prop) (self : SelfGood (standpoint val))
    (mono : Monotone (standpoint val) (· ≤ ·))
    (onlyOwn : ∀ g, (standpoint val).sig g → (standpoint val).own g) : False :=
  strict_indexed_rival_inconsistent (standpoint val) (· ≤ ·) self mono onlyOwn
    ⟨.changedSelf, .formedOther, trivial, trivial, trivial, id, show 4 ≤ 5 by decide⟩
