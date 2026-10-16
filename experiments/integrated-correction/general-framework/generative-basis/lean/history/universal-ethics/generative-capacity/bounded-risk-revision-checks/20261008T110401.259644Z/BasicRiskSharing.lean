import Std

/-
Finite consequences of sharing selection between two supplied risk profiles.
The ethical warrant of equal claims, implementation permission and the risk law
are not supplied by these proofs. Numerators share denominator 10*n for n>0.
The two positions arise in one support arrangement; statistical independence
is a property of the specified joint law, not an ontological assumption.
-/
namespace BasicRiskSharing

def exposureA (n x : Nat) : Nat := x + 4 * (n - x)
def exposureB (n x : Nat) : Nat := 4 * x + (n - x)

def AtMost (n x bound : Nat) : Prop :=
  exposureA n x ≤ bound ∧ exposureB n x ≤ bound

theorem total_exposure (n x : Nat) (h : x ≤ n) :
    exposureA n x + exposureB n x = 5 * n := by
  unfold exposureA exposureB
  omega

theorem balanced_exposure (k : Nat) :
    exposureA (2 * k) k = 5 * k ∧ exposureB (2 * k) k = 5 * k := by
  unfold exposureA exposureB
  omega

theorem equal_exposure_iff (k x : Nat) (h : x ≤ 2 * k) :
    exposureA (2 * k) x = exposureB (2 * k) x ↔ x = k := by
  unfold exposureA exposureB
  omega

/- Exact best common risk bound among every supported ticket allocation. -/
theorem attainable_common_bound_iff (k bound : Nat) :
    (∃ x, x ≤ 2 * k ∧ AtMost (2 * k) x bound) ↔ 5 * k ≤ bound := by
  unfold AtMost exposureA exposureB
  constructor
  · rintro ⟨x, hx, ha, hb⟩
    omega
  · intro h
    exact ⟨k, by omega, by omega, by omega⟩

theorem unique_best_allocation (k x : Nat) (h : x ≤ 2 * k) :
    AtMost (2 * k) x (5 * k) ↔ x = k := by
  unfold AtMost exposureA exposureB
  omega

theorem pure_allocations_miss_best_bound (k : Nat) (h : 0 < k) :
    ¬ AtMost (2 * k) 0 (5 * k) ∧ ¬ AtMost (2 * k) (2 * k) (5 * k) := by
  unfold AtMost exposureA exposureB
  omega

/- Each originally favored position really bears an increased risk. Fair
   sharing is not a Pareto reduction of both individuals' exposures. -/
theorem sharing_retains_the_favored_positions_cost (k : Nat) (h : 0 < k) :
    exposureA (2 * k) (2 * k) < exposureA (2 * k) k ∧
    exposureB (2 * k) 0 < exposureB (2 * k) k := by
  unfold exposureA exposureB
  omega

/- Equality alone cannot justify worsening a genuinely better symmetric plan. -/
theorem lower_equal_profile_remains_better (k : Nat) (h : 0 < k) :
    k < exposureA (2 * k) k ∧ k < exposureB (2 * k) k := by
  unfold exposureA exposureB
  omega

inductive Plan where
  | favorA | favorB
  deriving DecidableEq, Repr

/- Both losses never occur together in this particular one-period law.
   Losing either basic realization is serious and remains a loss. -/
def failures (p : Plan) (event : Nat) : Bool × Bool :=
  match p with
  | .favorA => (decide (event = 9), decide (5 ≤ event ∧ event < 9))
  | .favorB => (decide (event < 4), decide (event = 4))

def countA (xs : List (Bool × Bool)) : Nat := (xs.filter fun p => p.1).length
def countB (xs : List (Bool × Bool)) : Nat := (xs.filter fun p => p.2).length
def countBoth (xs : List (Bool × Bool)) : Nat := (xs.filter fun p => p.1 && p.2).length
def countAny (xs : List (Bool × Bool)) : Nat := (xs.filter fun p => p.1 || p.2).length

def planRecords (p : Plan) : List (Bool × Bool) := (List.range 10).map (failures p)

theorem native_plan_rates :
    countA (planRecords .favorA) = 1 ∧ countB (planRecords .favorA) = 4 ∧
    countA (planRecords .favorB) = 4 ∧ countB (planRecords .favorB) = 1 := by decide

def productRecords : List (Bool × Bool) := planRecords .favorA ++ planRecords .favorB

theorem product_law_realizes_balanced_rates :
    productRecords.length = 20 ∧ countA productRecords = 5 ∧ countB productRecords = 5 ∧
    countA productRecords = exposureA 2 1 ∧ countB productRecords = exposureB 2 1 := by decide

theorem complete_joint_profile_preserved :
    countBoth (planRecords .favorA) = 0 ∧ countBoth (planRecords .favorB) = 0 ∧
    countBoth productRecords = 0 ∧
    countAny (planRecords .favorA) = 5 ∧ countAny (planRecords .favorB) = 5 ∧
    countAny productRecords = 10 := by decide

/- Equal plan frequencies can coexist with dependence on the danger itself.
   This is a second supplied joint law, not a frequency-based inference. -/
def coupledPlan (event : Nat) : Plan := if event < 5 then .favorB else .favorA
def coupledRecords : List (Bool × Bool) :=
  (List.range 10).map fun e => failures (coupledPlan e) e

theorem coupled_selection_has_equal_plan_frequencies :
    ((List.range 10).filter fun e => decide (coupledPlan e = .favorA)).length = 5 ∧
    ((List.range 10).filter fun e => decide (coupledPlan e = .favorB)).length = 5 := by decide

theorem coupled_law_doubles_each_risk :
    coupledRecords.length = 10 ∧ countA coupledRecords = 5 ∧ countB coupledRecords = 5 ∧
    2 * countA coupledRecords > countA productRecords ∧
    2 * countB coupledRecords > countB productRecords := by decide

theorem coupled_joint_profile_worsens :
    countBoth coupledRecords = 0 ∧ countAny coupledRecords = 10 ∧
    2 * countAny coupledRecords > countAny productRecords := by decide

/- A later observation may justify a substantive priority that defeats the
   initial symmetric rule. Continuing to mix ignores the new circumstance. -/
theorem informed_selection_can_avoid_this_law_of_loss :
    (∀ e : Fin 10, failures (if e.val < 5 then .favorA else .favorB) e.val =
      (false, false)) := by decide

/- Same gravity of loss but unequal protection technology: the second plan
   now exposes A at 8/10, while its B risk remains 1/10. A random mixture's
   denominators are 10*n. No ethical permission or scalar welfare follows. -/
def asymmetricA (n x : Nat) : Nat := x + 8 * (n - x)
def asymmetricB (n x : Nat) : Nat := 4 * x + (n - x)

theorem asymmetric_unique_best_bound (k x : Nat) (h : x ≤ 10 * k) :
    (asymmetricA (10 * k) x ≤ 31 * k ∧ asymmetricB (10 * k) x ≤ 31 * k)
      ↔ x = 7 * k := by
  unfold asymmetricA asymmetricB
  omega

theorem asymmetric_bound_is_least (k bound : Nat) :
    (∃ x, x ≤ 10 * k ∧ asymmetricA (10 * k) x ≤ bound ∧
      asymmetricB (10 * k) x ≤ bound) ↔ 31 * k ≤ bound := by
  unfold asymmetricA asymmetricB
  constructor
  · rintro ⟨x, hx, ha, hb⟩
    omega
  · intro h
    exact ⟨7 * k, by omega, by omega, by omega⟩

theorem fairer_bound_can_increase_total_exposure (k : Nat) (h : 0 < k) :
    asymmetricA (10 * k) (7 * k) = 31 * k ∧
    asymmetricB (10 * k) (7 * k) = 31 * k ∧
    asymmetricA (10 * k) (10 * k) = 10 * k ∧
    asymmetricB (10 * k) (10 * k) = 40 * k ∧
    31 * k < 40 * k ∧ 50 * k < 62 * k := by
  unfold asymmetricA asymmetricB
  omega

def asymmetricFailures (p : Plan) (event : Nat) : Bool × Bool :=
  match p with
  | .favorA => failures .favorA event
  | .favorB => (decide (event < 8), decide (event = 8))

def asymmetricRecords : List (Bool × Bool) :=
  (List.range 100).map fun e =>
    asymmetricFailures (if e / 10 < 7 then .favorA else .favorB) (e % 10)

theorem asymmetric_native_profile :
    asymmetricRecords.length = 100 ∧
    countA asymmetricRecords = 31 ∧ countB asymmetricRecords = 31 ∧
    countBoth asymmetricRecords = 0 ∧ countAny asymmetricRecords = 62 := by decide

end BasicRiskSharing
