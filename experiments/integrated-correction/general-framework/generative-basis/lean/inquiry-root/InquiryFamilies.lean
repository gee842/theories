import GenerativeClosure
import Depletion

/-!
Concrete infinitely indexed constraints for the inherited generative interface.
Different thresholds have different operational capability sets, so this is
not infinity obtained by repeating one proposition with redundant syntax.
Observation and spending laws are explicit local inputs, not universal physics.
-/

namespace InquiryRoot

/-- Capacity n retains exact values below n and merges every value at least n. -/
def clippedObservation (n hidden : Nat) : Nat := min hidden n

/-- One common binary decoder must answer the threshold question at every
    unresolved hidden value. This is existence, not free physical installation. -/
def ThresholdAvailable (n k : Nat) : Prop :=
  ∃ decoder : Nat → Bool,
    ∀ hidden, decoder (clippedObservation n hidden) = decide (hidden ≤ k)

/-- A constructive reproof of the existing Unit-list length fact, used to
avoid extensionality-bearing simplification in the original contracts. -/
theorem unit_replicate_length (n : Nat) : (List.replicate n ()).length = n := by
  induction n with
  | zero => rfl
  | succ n ih => exact congrArg Nat.succ ih

theorem threshold_available_iff (n k : Nat) : ThresholdAvailable n k ↔ k < n := by
  have minRight : ∀ a b : Nat, b ≤ a → min a b = b := by
    intro a b hba
    by_cases hab : a ≤ b
    · exact (Nat.min_eq_left hab).trans (Nat.le_antisymm hab hba)
    · exact if_neg hab
  constructor
  · rintro ⟨decoder, correct⟩
    by_cases hkn : k < n
    · exact hkn
    have hnk : n ≤ k := Nat.le_of_not_gt hkn
    have h0 : decoder n = true :=
      (congrArg decoder (minRight k n hnk)).symm.trans
        ((correct k).trans (decide_eq_true (Nat.le_refl k)))
    have h1 : decoder n = false :=
      (congrArg decoder (minRight (k + 1) n (Nat.le_trans hnk (Nat.le_succ k)))).symm.trans
        ((correct (k + 1)).trans (decide_eq_false (Nat.not_succ_le_self k)))
    exact Bool.noConfusion (h0.symm.trans h1)
  · intro hkn
    refine ⟨fun signal => decide (signal ≤ k), ?_⟩
    intro hidden
    by_cases hhn : hidden ≤ n
    · exact congrArg (fun value => decide (value ≤ k)) (Nat.min_eq_left hhn)
    · have hhk : ¬ hidden ≤ k := fun h => hhn (Nat.le_trans h (Nat.le_of_lt hkn))
      have hnFalse : decide (n ≤ k) = false := decide_eq_false (Nat.not_le_of_gt hkn)
      exact (congrArg (fun value => decide (value ≤ k)) (minRight hidden n
        (Nat.le_of_lt (Nat.lt_of_not_le hhn)))).trans
          (hnFalse.trans (decide_eq_false hhk).symm)

theorem every_threshold_has_a_finite_realization (k : Nat) :
    ThresholdAvailable (k + 1) k :=
  (threshold_available_iff _ _).mpr (Nat.lt_succ_self k)

theorem next_threshold_exceeds_that_realization (k : Nat) :
    ¬ ThresholdAvailable (k + 1) (k + 1) := by
  intro h
  exact Nat.not_succ_le_self (k + 1) ((threshold_available_iff _ _).mp h)

/-- For any two different query thresholds there is a capacity that separates
    their answerability. No assertion that one finite observer answers them all. -/
theorem threshold_capability_sets_pairwise_distinct {k l : Nat} (hkl : k < l) :
    ∃ n, ThresholdAvailable n k ∧ ¬ ThresholdAvailable n l := by
  refine ⟨k + 1, every_threshold_has_a_finite_realization k, ?_⟩
  intro h
  exact Nat.not_succ_le_self l (Nat.le_trans ((threshold_available_iff _ _).mp h) hkl)

def spendingProcess : Generative.Process Nat Unit where
  step s _ t := s = t + 1

theorem spending_trace_iff (s t : Nat) (actions : List Unit) :
    Generative.Trace spendingProcess s actions t ↔ s = t + actions.length := by
  induction actions generalizing s with
  | nil => exact Generative.trace_nil_iff
  | cons a rest ih =>
    constructor
    · intro history
      obtain ⟨middle, hstep, htail⟩ := Generative.trace_cons_iff.mp history
      have hs : s = middle + 1 := hstep
      have hm : middle = t + rest.length := (ih middle).mp htail
      exact hs.trans ((congrArg (fun value => value + 1) hm).trans
        (Nat.add_assoc t rest.length 1))
    · intro h
      exact Generative.Trace.cons
        (m := t + rest.length) (h.trans (Nat.add_assoc t rest.length 1).symm)
        ((ih _).mpr rfl)

theorem spending_feasible_iff (fuel : Nat) (actions : List Unit) :
    Generative.Feasible spendingProcess fuel actions ↔ actions.length ≤ fuel := by
  constructor
  · rintro ⟨remaining, htrace⟩
    exact Generative.trace_length_bound (fun n => n)
      (fun s _ t hs => by
        change s = t + 1 at hs
        exact hs.symm ▸ Nat.lt_succ_self t) htrace
  · intro h
    obtain ⟨remaining, sum⟩ := Nat.le.dest h
    exact ⟨remaining, (spending_trace_iff _ _ _).mpr
      (sum.symm.trans (Nat.add_comm actions.length remaining))⟩

theorem every_budget_excludes_a_different_horizon (fuel : Nat) :
    Generative.Feasible spendingProcess fuel (List.replicate fuel ()) ∧
    ¬ Generative.Feasible spendingProcess fuel (List.replicate (fuel + 1) ()) := by
  constructor
  · apply (spending_feasible_iff _ _).mpr
    exact Eq.mp (congrArg (fun length => length ≤ fuel)
      (unit_replicate_length fuel).symm) (Nat.le_refl fuel)
  · intro h
    have bound := (spending_feasible_iff _ _).mp h
    exact Nat.not_succ_le_self fuel (Eq.mp
      (congrArg (fun length => length ≤ fuel) (unit_replicate_length (fuel + 1))) bound)

structure InquiryScenario where
  capacity : Nat
  threshold : Nat
  fuel : Nat
  horizon : Nat

def observationTask (w : InquiryScenario) : Prop :=
  ThresholdAvailable w.capacity w.threshold

def repeatedTask (w : InquiryScenario) : Prop :=
  Generative.Feasible spendingProcess w.fuel (List.replicate w.horizon ())

def localBasis : Bool → Formula InquiryScenario
  | false => fun w => observationTask w → w.threshold < w.capacity
  | true => fun w => repeatedTask w → w.horizon ≤ w.fuel

theorem local_basis_valid (i : Bool) (w : InquiryScenario) : localBasis i w := by
  cases i with
  | false => exact (threshold_available_iff _ _).mp
  | true =>
    intro h
    exact Eq.mp (congrArg (fun length => length ≤ w.fuel)
      (unit_replicate_length w.horizon))
      ((spending_feasible_iff w.fuel (List.replicate w.horizon ())).mp h)

/-- The inherited closed theory propagates both informative local constraints
    through every finite descendant, not just the particular examples below. -/
theorem entire_local_closure_valid {p : Formula InquiryScenario}
    (proof : Derives localBasis [] p) : ∀ w, p w := by
  intro w
  exact all_closed_descendants_necessary
    (inquiry := fun _ => True) (fun i w _ => local_basis_valid i w) p proof w True.intro

theorem combined_capability_descendant : Derives localBasis
    [observationTask, repeatedTask]
    (fun w => w.threshold < w.capacity ∧ w.horizon ≤ w.fuel) := by
  apply Derives.andIntro
  · exact .impElim (.base false) (.assumption (.head _))
  · exact .impElim (.base true) (.assumption (.tail _ (.head _)))

theorem combined_capability_implication_in_closed_theory : Derives localBasis []
    (fun w => observationTask w → repeatedTask w →
      w.threshold < w.capacity ∧ w.horizon ≤ w.fuel) := by
  apply Derives.impIntro
  apply Derives.impIntro
  apply Derives.andIntro
  · exact .impElim (.base false) (.assumption (.tail _ (.head _)))
  · exact .impElim (.base true) (.assumption (.head _))

/-- Two finite formulas contain uniformly quantified operational law contracts.
    Their instances below are derived by a finite quantifier-elimination rule. -/
def uniformBasis : Bool → Formula InquiryScenario
  | false => fun w => ∀ k, ThresholdAvailable w.capacity k → k < w.capacity
  | true => fun w => ∀ n, Generative.Feasible spendingProcess w.fuel
      (List.replicate n ()) → n ≤ w.fuel

theorem uniform_basis_valid (i : Bool) (w : InquiryScenario) : uniformBasis i w := by
  cases i with
  | false => exact fun _ => (threshold_available_iff _ _).mp
  | true =>
    intro n h
    exact Eq.mp (congrArg (fun length => length ≤ w.fuel)
      (unit_replicate_length n)) ((spending_feasible_iff _ _).mp h)

theorem entire_uniform_closure_valid {p : Formula InquiryScenario}
    (proof : Derives uniformBasis [] p) : ∀ w, p w := by
  intro w
  exact all_closed_descendants_necessary
    (inquiry := fun _ => True) (fun i w _ => uniform_basis_valid i w) p proof w True.intro

theorem every_threshold_contract_is_a_descendant (k : Nat) :
    Derives uniformBasis []
      (fun w => ThresholdAvailable w.capacity k → k < w.capacity) :=
  .allNatElim (p := fun (k : Nat) (w : InquiryScenario) =>
    ThresholdAvailable w.capacity k → k < w.capacity)
    k (.base false)

theorem every_support_contract_is_a_descendant (n : Nat) :
    Derives uniformBasis [] (fun w => Generative.Feasible spendingProcess w.fuel
      (List.replicate n ()) → n ≤ w.fuel) :=
  .allNatElim (p := fun (n : Nat) (w : InquiryScenario) => Generative.Feasible spendingProcess w.fuel
    (List.replicate n ()) → n ≤ w.fuel) n (.base true)

#print axioms InquiryRoot.unit_replicate_length
#print axioms InquiryRoot.threshold_available_iff
#print axioms InquiryRoot.every_threshold_has_a_finite_realization
#print axioms InquiryRoot.next_threshold_exceeds_that_realization
#print axioms InquiryRoot.threshold_capability_sets_pairwise_distinct
#print axioms InquiryRoot.spending_trace_iff
#print axioms InquiryRoot.spending_feasible_iff
#print axioms InquiryRoot.every_budget_excludes_a_different_horizon
#print axioms InquiryRoot.local_basis_valid
#print axioms InquiryRoot.entire_local_closure_valid
#print axioms InquiryRoot.combined_capability_descendant
#print axioms InquiryRoot.combined_capability_implication_in_closed_theory
#print axioms InquiryRoot.uniform_basis_valid
#print axioms InquiryRoot.entire_uniform_closure_valid
#print axioms InquiryRoot.every_threshold_contract_is_a_descendant
#print axioms InquiryRoot.every_support_contract_is_a_descendant

end InquiryRoot
