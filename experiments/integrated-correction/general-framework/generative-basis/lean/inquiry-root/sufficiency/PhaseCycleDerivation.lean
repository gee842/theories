import PacketLawDerivation

/-!
# What the native three-phase cycle is accountable for

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
PHASE-CYCLE-DERIVATION.md.

The native port (`NativePacketProcess`) supplies `Phase`, `nextPhase` and the
contact reading `output = (0, 0, 1)`. This module does not replace them. It asks
which more primitive organization yields such a cycle and what the number three
is accountable for in the downstream alignment and diagnosis.

1. Orbit. The three phases are exactly the orbit of one primitive advance, which
   retains distinctions (is injective) and returns after three and no fewer
   steps. On every finite carrier through four configurations, a
   distinction-retaining primitive change returns every configuration; a merging
   change leaves a transient that never returns.
2. Accountability. For a binary contact read around a cycle of a given period,
   three requirements are named: both contact values occur; the phase is
   recoverable from one full round of readings although the reading inversion is
   unknown (the diagnosis `move` halts otherwise); and both values are reachable
   within a stated number of advances. Period three is the least period meeting
   the first two; periods one and two fail. Every two-valued pattern on three
   phases meets all three with the two-advance bound, and is the native pattern
   up to rotation and global inversion. Period four admits none with the
   two-advance bound; period five admits some. One-advance reach admits none up
   to period six. Thus three is the least admissible period, not the only one.
3. Recurrence within non-recurring activity. Three paid advances restore the
   phase, while no nonempty sequence of completed advances restores the whole
   native configuration: each draws on the sustaining store.

Still supplied: the existence of one injective primitive advance, finiteness,
the binary contact reading, the three requirements (taken from the downstream
diagnosis), and selection of the least admissible period. No physical or
universal necessity of three is claimed.
-/

namespace Generative.InquirySufficiency.PhaseCycleDerivation

open Generative.NativePacketProcess (Phase output nextPhase bill peak)
open Generative.InquirySufficiency.PacketLawDerivation
  (Native phaseAfter rotations RotationsReady rotation_fields rotation_fuel
    rotations_ready_implies_budget sub_add_cancel_constructive)

/-! ## 1. The native phases are the orbit of one primitive advance -/

theorem phase_is_orbit_of_advance (phase : Phase) :
    phase = .p0 ∨ phase = nextPhase .p0 ∨ phase = nextPhase (nextPhase .p0) := by
  cases phase
  · exact Or.inl rfl
  · exact Or.inr (Or.inl rfl)
  · exact Or.inr (Or.inr rfl)

theorem advance_retains_distinctions (left right : Phase)
    (same : nextPhase left = nextPhase right) : left = right := by
  cases left <;> cases right
  all_goals solve
    | rfl
    | cases same

theorem advance_returns_after_three (phase : Phase) :
    nextPhase (nextPhase (nextPhase phase)) = phase := by
  cases phase <;> rfl

theorem advance_no_shorter_return (phase : Phase) :
    nextPhase phase ≠ phase ∧ nextPhase (nextPhase phase) ≠ phase := by
  cases phase <;> constructor <;> intro h <;> cases h

theorem phaseAfter_three (phase : Phase) : phaseAfter 3 phase = phase := by
  cases phase <;> rfl

/-! ## Finite primitive changes, as executable tables -/

def nth : List Nat → Nat → Nat
  | [], _ => 0
  | value :: _, 0 => value
  | _ :: rest, index + 1 => nth rest index

def upto : Nat → List Nat
  | 0 => []
  | count + 1 => upto count ++ [count]

def allOf {α : Type} : List α → (α → Bool) → Bool
  | [], _ => true
  | item :: rest, test => test item && allOf rest test

def anyOf {α : Type} : List α → (α → Bool) → Bool
  | [], _ => false
  | item :: rest, test => test item || anyOf rest test

/-- Apply a primitive change, given as a table, a number of times. -/
def advanceBy (change : List Nat) : Nat → Nat → Nat
  | 0, configuration => configuration
  | steps + 1, configuration => advanceBy change steps (nth change configuration)

def returnsWithin (change : List Nat) (size configuration : Nat) : Bool :=
  anyOf (upto size) fun steps => advanceBy change (steps + 1) configuration == configuration

/-- No two configurations are merged by the change. -/
def retainsDistinctions (change : List Nat) (size : Nat) : Bool :=
  allOf (upto size) fun left => allOf (upto size) fun right =>
    !(nth change left == nth change right) || left == right

def prependEach (values : List Nat) (tails : List (List Nat)) : List (List Nat) :=
  match values with
  | [] => []
  | value :: rest => tails.map (fun tail => value :: tail) ++ prependEach rest tails

/-- Every change table of the given length over a carrier of the given size. -/
def changesOn (size : Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | length + 1 => prependEach (upto size) (changesOn size length)

/-- Exhaustive for carriers of one through four configurations. The general
statement is the standard finite-permutation fact, argued in the study note. -/
theorem retaining_change_closes_into_cycles :
    allOf (upto 4) (fun index =>
      allOf (changesOn (index + 1) (index + 1)) fun change =>
        !retainsDistinctions change (index + 1) ||
          allOf (upto (index + 1)) (returnsWithin change (index + 1))) = true := by
  decide +kernel

/-- A merging change: configuration 0 is never revisited, while 2 is fixed. -/
theorem merging_change_leaves_transient :
    retainsDistinctions [1, 2, 2] 3 = false ∧ returnsWithin [1, 2, 2] 3 0 = false ∧
      returnsWithin [1, 2, 2] 3 2 = true := by
  decide

def phaseIndex : Phase → Nat
  | .p0 => 0
  | .p1 => 1
  | .p2 => 2

def nativeAdvance : List Nat := [1, 2, 0]

theorem native_advance_represented (phase : Phase) :
    phaseIndex (nextPhase phase) = nth nativeAdvance (phaseIndex phase) := by
  cases phase <;> rfl

theorem native_advance_single_cycle :
    retainsDistinctions nativeAdvance 3 = true ∧
      advanceBy nativeAdvance 1 0 = 1 ∧ advanceBy nativeAdvance 2 0 = 2 ∧
      advanceBy nativeAdvance 3 0 = 0 := by
  decide

/-! ## 2. What a binary contact over a cycle must support -/

def bitAt : List Bool → Nat → Bool
  | [], _ => false
  | value :: _, 0 => value
  | _ :: rest, index + 1 => bitAt rest index

def patterns : Nat → List (List Bool)
  | 0 => [[]]
  | length + 1 => (patterns length).map (fun tail => false :: tail) ++
      (patterns length).map (fun tail => true :: tail)

/-- Requirement R0: both contact values occur on the cycle. -/
def bothValuesOccur (pattern : List Bool) : Bool :=
  anyOf pattern (fun value => value) && anyOf pattern (fun value => !value)

def reading (pattern : List Bool) (period phase offset : Nat) (inversion : Bool) : Bool :=
  bitAt pattern ((phase + offset) % period) != inversion

def sameReadings (pattern : List Bool) (period left right : Nat)
    (leftInversion rightInversion : Bool) : Bool :=
  allOf (upto period) fun offset =>
    reading pattern period left offset leftInversion ==
      reading pattern period right offset rightInversion

/-- Requirement R1: one full round of readings fixes the phase, although the
reading inversion is not known in advance. -/
def phaseRecoverable (pattern : List Bool) (period : Nat) : Bool :=
  allOf (upto period) fun left => allOf (upto period) fun right =>
    allOf [false, true] fun leftInversion => allOf [false, true] fun rightInversion =>
      !sameReadings pattern period left right leftInversion rightInversion || left == right

/-- Requirement R2: from every phase, each contact value is met within `bound`
advances. -/
def bothValuesWithin (pattern : List Bool) (period bound : Nat) : Bool :=
  allOf (upto period) fun phase => allOf [false, true] fun value =>
    anyOf (upto (bound + 1)) fun steps => bitAt pattern ((phase + steps) % period) == value

def supportsAlignment (pattern : List Bool) (period bound : Nat) : Bool :=
  bothValuesOccur pattern && phaseRecoverable pattern period &&
    bothValuesWithin pattern period bound

def admittedAt (period bound : Nat) : List (List Bool) :=
  (patterns period).filter fun pattern => supportsAlignment pattern period bound

def rotationOf (pattern base : List Bool) (period : Nat) : Bool :=
  anyOf (upto period) fun shift => allOf (upto period) fun index =>
    bitAt pattern ((index + shift) % period) == bitAt base index

theorem native_contact_pattern :
    [output .p0, output .p1, output .p2] = [false, false, true] := rfl

theorem native_pattern_supports_alignment :
    supportsAlignment [false, false, true] 3 2 = true := by
  decide

/-- Periods one and two cannot meet R0 and R1 together, whatever the bound. -/
theorem no_shorter_cycle_recovers_phase :
    allOf (patterns 1) (fun pattern =>
        !(bothValuesOccur pattern && phaseRecoverable pattern 1)) = true ∧
      allOf (patterns 2) (fun pattern =>
        !(bothValuesOccur pattern && phaseRecoverable pattern 2)) = true := by
  decide

/-- On three phases every two-valued contact meets R0, R1 and R2 with bound two. -/
theorem every_two_valued_three_cycle_supports_alignment :
    allOf (patterns 3) (fun pattern =>
      !bothValuesOccur pattern || supportsAlignment pattern 3 2) = true := by
  decide

theorem three_cycle_admits_six : (admittedAt 3 2).length = 6 := by
  decide

/-- Up to rotation and global inversion, the native pattern is the only one. -/
theorem three_cycle_pattern_unique_up_to_rotation_and_inversion :
    allOf (patterns 3) (fun pattern => !bothValuesOccur pattern ||
      rotationOf pattern [false, false, true] 3 ||
        rotationOf (pattern.map (fun value => !value)) [false, false, true] 3) = true := by
  decide

theorem period_four_admits_none : (admittedAt 4 2).length = 0 := by
  decide +kernel

/-- Period four is excluded by the reach bound, not by phase recovery. -/
theorem period_four_fails_only_by_reach :
    (bothValuesOccur [false, false, false, true] &&
        phaseRecoverable [false, false, false, true] 4) = true ∧
      bothValuesWithin [false, false, false, true] 4 2 = false := by
  decide

/-- Counterexample to "three is forced": a five-phase cycle also qualifies. -/
theorem period_five_also_supports_alignment :
    supportsAlignment [false, false, true, false, true] 5 2 = true := by
  decide

/-- With one-advance reach, no period from one through six qualifies. -/
theorem one_advance_reach_never_recovers_phase :
    allOf (upto 6) (fun index => (admittedAt (index + 1) 1).length == 0) = true := by
  decide +kernel

/-! ## Phase recovery on the native cycle, and a two-phase rival -/

/-- Three readings around the native cycle fix both the phase and the reading
inversion. Native readings use inversion `tau ^^ sigma` (`native_read_uses_parity`). -/
theorem native_readings_recover_phase_and_inversion (left right : Phase)
    (leftInversion rightInversion : Bool)
    (first : (output left != leftInversion) = (output right != rightInversion))
    (second : (output (nextPhase left) != leftInversion) =
      (output (nextPhase right) != rightInversion))
    (third : (output (nextPhase (nextPhase left)) != leftInversion) =
      (output (nextPhase (nextPhase right)) != rightInversion)) :
    left = right ∧ leftInversion = rightInversion := by
  cases left <;> cases right <;> cases leftInversion <;> cases rightInversion
  all_goals solve
    | exact ⟨rfl, rfl⟩
    | cases first
    | cases second
    | cases third

inductive TwoPhase where
  | q0 | q1

def twoAdvance : TwoPhase → TwoPhase
  | .q0 => .q1
  | .q1 => .q0

def twoContact : TwoPhase → Bool
  | .q0 => false
  | .q1 => true

def twoAfter : Nat → TwoPhase → TwoPhase
  | 0, phase => phase
  | steps + 1, phase => twoAfter steps (twoAdvance phase)

theorem twoAfter_advance (steps : Nat) (phase : TwoPhase) :
    twoAfter steps (twoAdvance phase) = twoAdvance (twoAfter steps phase) := by
  induction steps generalizing phase with
  | zero => rfl
  | succ steps ih => exact ih (twoAdvance phase)

theorem two_contact_shift (phase : TwoPhase) :
    (twoContact phase != false) = (twoContact (twoAdvance phase) != true) := by
  cases phase <;> rfl

theorem two_cycle_phases_distinct : TwoPhase.q0 ≠ TwoPhase.q1 := fun h => by cases h

/-- In the two-phase rival, a phase shift and an inverted reading produce the
same readings after every number of advances: phase is not recoverable. -/
theorem two_cycle_confounds_phase_with_inversion (steps : Nat) :
    (twoContact (twoAfter steps .q0) != false) =
      (twoContact (twoAfter steps .q1) != true) := by
  have shifted : twoAfter steps TwoPhase.q1 = twoAdvance (twoAfter steps TwoPhase.q0) :=
    twoAfter_advance steps TwoPhase.q0
  rw [shifted]
  exact two_contact_shift (twoAfter steps TwoPhase.q0)

/-! ## 3. The phase recurs; the whole native configuration does not -/

/-- Each completed native call draws at least one unit from the sustaining
store (the inherited `bill` is at least 16384). -/
theorem activity_drawn_positive (s : Native) : 1 ≤ bill s :=
  Nat.le_trans (by decide : 1 ≤ 16384) (Nat.le_add_right 16384 (peak s))

theorem rotations_never_restore_whole (count : Nat) (s : Native)
    (ready : RotationsReady (count + 1) s) : rotations (count + 1) s ≠ s := by
  intro same
  have remaining := rotation_fuel (count + 1) s
  rw [same] at remaining
  have restored := sub_add_cancel_constructive s.fuel ((count + 1) * bill s)
    (rotations_ready_implies_budget (count + 1) s ready)
  rw [← remaining] at restored
  have positive : 1 ≤ (count + 1) * bill s := by
    rw [Nat.succ_mul]
    exact Nat.le_trans (activity_drawn_positive s) (Nat.le_add_left _ _)
  exact Nat.lt_irrefl s.fuel
    (Nat.le_trans (Nat.add_le_add_left positive s.fuel) (Nat.le_of_eq restored))

theorem phase_recurs_whole_does_not (s : Native) (ready : RotationsReady 3 s) :
    (rotations 3 s).phase = s.phase ∧ rotations 3 s ≠ s :=
  ⟨(rotation_fields 3 s).1.trans (phaseAfter_three s.phase),
    rotations_never_restore_whole 2 s ready⟩

end Generative.InquirySufficiency.PhaseCycleDerivation

#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.phase_is_orbit_of_advance
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.advance_retains_distinctions
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.advance_returns_after_three
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.advance_no_shorter_return
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.phaseAfter_three
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.nth
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.upto
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.allOf
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.anyOf
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.advanceBy
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.returnsWithin
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.retainsDistinctions
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.prependEach
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.changesOn
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.retaining_change_closes_into_cycles
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.merging_change_leaves_transient
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.phaseIndex
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.nativeAdvance
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.native_advance_represented
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.native_advance_single_cycle
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.bitAt
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.patterns
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.bothValuesOccur
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.reading
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.sameReadings
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.phaseRecoverable
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.bothValuesWithin
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.supportsAlignment
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.admittedAt
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.rotationOf
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.native_contact_pattern
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.native_pattern_supports_alignment
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.no_shorter_cycle_recovers_phase
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.every_two_valued_three_cycle_supports_alignment
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.three_cycle_admits_six
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.three_cycle_pattern_unique_up_to_rotation_and_inversion
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.period_four_admits_none
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.period_four_fails_only_by_reach
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.period_five_also_supports_alignment
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.one_advance_reach_never_recovers_phase
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.native_readings_recover_phase_and_inversion
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.TwoPhase
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.twoAdvance
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.twoContact
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.twoAfter
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.twoAfter_advance
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.two_contact_shift
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.two_cycle_phases_distinct
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.two_cycle_confounds_phase_with_inversion
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.activity_drawn_positive
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.rotations_never_restore_whole
#print axioms Generative.InquirySufficiency.PhaseCycleDerivation.phase_recurs_whole_does_not
