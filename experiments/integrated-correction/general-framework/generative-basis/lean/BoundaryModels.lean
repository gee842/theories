import Std -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Readout.no_judge_of_merged`, `Becoming.Pair.own_not_joint` — 是其实例 / an instance of it; MODULE-CLASSIFICATION.md

/-!
# Finite boundary models for the generative candidate

These independent, explicit models establish non-implications. They do not
identify a universal notion of significance, learning, or moral value. The
conditions and transition rules are supplied model data.
-/

namespace GenerativeBoundary

/-! ## A coarse observation can omit a consequential condition -/

namespace ObservationLoss

inductive FuelState where
  | ready
  | spent
  deriving DecidableEq, Repr

inductive Action where
  | operate
  deriving DecidableEq, Repr

def enabled : FuelState → Action → Prop
  | .ready, .operate => True
  | .spent, .operate => False

-- The observer records the same exterior appearance in both fuel conditions.
def observe (_ : FuelState) : Unit := ()

theorem same_observation : observe .ready = observe .spent := rfl

theorem different_enabled_future :
    enabled .ready .operate ∧ ¬ enabled .spent .operate := by
  exact ⟨True.intro, fun h => h⟩

/-- No proposition computed solely from this observation classifies whether
    operation is enabled in both states. This concerns this observation map;
    a richer observation could distinguish the two states. -/
theorem no_observation_only_classifier :
    ¬ ∃ classify : Unit → Prop,
      ∀ s : FuelState, classify (observe s) ↔ enabled s .operate := by
  rintro ⟨classify, h⟩
  have readyClassified : classify (observe .ready) :=
    (h .ready).mpr True.intro
  exact (h .spent).mp readyClassified

end ObservationLoss

/-! ## Separate feasibility need not be joint feasibility -/

namespace SharedResource

inductive Center where
  | left
  | right
  deriving DecidableEq, Repr

-- A single, indivisible resource is allocated once in the current round.
-- `false` allocates it left; `true` allocates it right. There is no second unit,
-- replenishment, or later round in this model.
abbrev Allocation := Bool

def serves : Allocation → Center → Prop
  | a, .left => a = false
  | a, .right => a = true

theorem each_center_individually_feasible :
    ∀ center : Center, ∃ allocation : Allocation, serves allocation center := by
  intro center
  cases center with
  | left => exact ⟨false, rfl⟩
  | right => exact ⟨true, rfl⟩

theorem no_common_allocation :
    ¬ ∃ allocation : Allocation, ∀ center : Center, serves allocation center := by
  rintro ⟨allocation, h⟩
  have hl : allocation = false := h .left
  have hr : allocation = true := h .right
  have impossible : false = true := hl.symm.trans hr
  cases impossible

/-- The quantifier swap fails even for a finite two-center system. -/
theorem individual_feasibility_without_joint_feasibility :
    (∀ center : Center, ∃ allocation : Allocation, serves allocation center) ∧
      ¬ (∃ allocation : Allocation, ∀ center : Center, serves allocation center) :=
  ⟨each_center_individually_feasible, no_common_allocation⟩

end SharedResource

/-! ## Nontrivial recurrence need not change a supplied selector -/

namespace FixedSelector

structure State where
  phase : Bool
  selector : Bool
  deriving DecidableEq, Repr

-- The supplied selector has an operative role: false selects alternation;
-- true selects holding the present phase. The selector itself remains fixed.
def advance (s : State) : State :=
  if s.selector then s else ⟨!s.phase, s.selector⟩

def run : Nat → State → State
  | 0, s => s
  | n + 1, s => advance (run n s)

theorem returns_after_two (s : State) : advance (advance s) = s := by
  cases s with
  | mk phase selector => cases selector <;> cases phase <;> rfl

theorem changes_phase_every_step (s : State) (selectsAlternation : s.selector = false) :
    advance s ≠ s := by
  cases s with
  | mk phase selector =>
    cases selector with
    | false =>
      intro h
      have phaseEquality : (!phase) = phase := congrArg State.phase h
      cases phase <;> cases phaseEquality
    | true => cases selectsAlternation

/-- Holding phase fixed, changing only the selector changes the next phase.
    Thus the preserved selector is causally operative, not an unused field. -/
theorem selector_changes_next_phase (phase : Bool) :
    (advance ⟨phase, false⟩).phase ≠ (advance ⟨phase, true⟩).phase := by
  cases phase <;> decide

theorem selector_preserved_by_step (s : State) : (advance s).selector = s.selector := by
  cases s with
  | mk phase selector => cases selector <;> rfl

theorem selector_unchanged_at_every_time (s : State) (n : Nat) :
    (run n s).selector = s.selector := by
  induction n with
  | zero => rfl
  | succ n ih => exact (selector_preserved_by_step (run n s)).trans ih

/-- A concrete nonconstant recurrent trajectory whose selector never changes.
    This refutes an unconditional implication from recurrence to selector
    revision. It neither defines every kind of learning nor rules out learning
    in a different recurrent process. -/
theorem recurrent_process_with_fixed_selector :
    ∃ s : State, advance (advance s) = s ∧ advance s ≠ s ∧
      ∀ n : Nat, (run n s).selector = s.selector := by
  exact ⟨⟨false, false⟩, returns_after_two _, changes_phase_every_step _ rfl,
    selector_unchanged_at_every_time _⟩

end FixedSelector

#print axioms ObservationLoss.no_observation_only_classifier
#print axioms SharedResource.individual_feasibility_without_joint_feasibility
#print axioms FixedSelector.returns_after_two
#print axioms FixedSelector.changes_phase_every_step
#print axioms FixedSelector.selector_changes_next_phase
#print axioms FixedSelector.selector_preserved_by_step
#print axioms FixedSelector.selector_unchanged_at_every_time
#print axioms FixedSelector.recurrent_process_with_fixed_selector

end GenerativeBoundary
