import PhaseCycleDerivation

/-!
# Which period the native activity draws least to use

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
PHASE-PERIOD-SELECTION.md.

`PhaseCycleDerivation` showed that three is the least period admitted by the
requirements R0–R2, and left the choice of the least admissible period supplied.
This module asks whether that choice follows from what the organization must
draw from its sustaining store in order to continue.

1. Native draw. Every completed sensing command (`a`, `read`, `reset`) draws
   exactly the native interface amount `draw`, and leaves that amount unchanged;
   a completed history of such commands draws its length times `draw`. The amount
   grows strictly with retained cells. A retained one-action cycle model of
   period `n` occupies `1 + 2n` cells (`Machine.cells` in the acquisition source;
   this correspondence is supplied, not proved here).
2. Guaranteed knowing arrival. From an unknown phase and an unknown reading
   inversion, how many native commands suffice in the worst case to stand at a
   phase whose contact value is known to be the requested one, for each of the
   two values? A completed command proceeds only when the store covers it, so a
   store that guarantees continuation from every start must cover this
   worst case. On three phases every two-valued pattern needs exactly seven
   commands, which the native profile `read a read a read` plus at most two
   advances realizes. For every period through eight, no pattern manages with
   six. Seven is reached only by patterns that repeat a three-phase pattern.
3. Selection. Combining 1 and 2, for periods three through eight the
   three-phase organization guarantees knowing arrival at both values with
   strictly less drawn activity than any other period, given the same other
   retained cells. Requirements R1 and R2 are not used: this one measure excludes
   periods four and five, and the period-six repetition is excluded only by its
   retention.
4. Counterexamples kept. The selection depends on the worst-case guarantee and on
   requiring both values. Averaged over a uniformly distributed known phase, the
   period-five pattern `00101` aligns with less drawn activity than `001`; for a
   single requested value, period five needs no more commands than period three;
   the period-six repetition ties period three in command count.

Supplied: the requirement to arrive knowingly at each of the two contact values,
the reading inversion being unknown, the retained-cell count of a cycle model,
finiteness, binary contact and one advance. Bounded: the lower bounds are
exhaustive for periods one through eight only.
-/

namespace Generative.InquirySufficiency.PhasePeriodSelection

open Generative
open Generative.NativePacketProcess (State Command execute draw peak enact support
  support_sustained_iff process)
open Generative.InquirySufficiency.PhaseCycleDerivation
  (bitAt allOf anyOf upto patterns bothValuesOccur)

/-! ## 1. What each native sensing command draws -/

/-- Commands that sense or advance the phase without converting source. -/
def sensing : Command → Bool
  | .a => true
  | .reset => true
  | .read => true
  | .probe => false

def sensingOnly : List Command → Bool
  | [] => true
  | command :: rest => sensing command && sensingOnly rest

theorem sensing_command_draws (s t : State) (command : Command)
    (observation : NativePacketProcess.Observation) (isSensing : sensing command = true)
    (actual : execute s command = .complete t observation) :
    t.enacted = s.enacted + draw s ∧ draw t = draw s ∧ t.live = s.live ∧
      t.workspace = s.workspace := by
  unfold execute at actual
  generalize interface : support s = outcome at actual
  cases outcome with
  | capacity => cases actual
  | insufficient => cases actual
  | sustained ready =>
    obtain ⟨_, equality⟩ := (support_sustained_iff s ready).mp interface
    cases equality
    cases command with
    | a => cases actual; exact ⟨rfl, rfl, rfl, rfl⟩
    | reset => cases actual; exact ⟨rfl, rfl, rfl, rfl⟩
    | read => cases actual; exact ⟨rfl, rfl, rfl, rfl⟩
    | probe => cases isSensing

/-- A completed history of sensing commands draws exactly its length times the
native per-command amount, which stays fixed along the history. -/
theorem sensing_history_draws {s t : State} {commands : List Command}
    (trace : Trace process s commands t) (onlySensing : sensingOnly commands = true) :
    t.enacted = s.enacted + commands.length * draw s ∧ draw t = draw s := by
  induction trace with
  | nil =>
    refine ⟨?_, rfl⟩
    show _ = _ + 0 * _
    rw [Nat.zero_mul, Nat.add_zero]
  | @cons s m t command rest step _ ih =>
    obtain ⟨observation, actual⟩ := step
    have firstSensing : sensing command = true := by
      cases first : sensing command with
      | false =>
        change (sensing command && sensingOnly rest) = true at onlySensing
        rw [first] at onlySensing
        cases onlySensing
      | true => rfl
    have restSensing : sensingOnly rest = true := by
      change (sensing command && sensingOnly rest) = true at onlySensing
      rw [firstSensing] at onlySensing
      exact onlySensing
    obtain ⟨drawn, same, _, _⟩ := sensing_command_draws s m command observation firstSensing actual
    obtain ⟨restDrawn, restSame⟩ := ih restSensing
    refine ⟨?_, restSame.trans same⟩
    rw [restDrawn, drawn, same]
    change s.enacted + draw s + rest.length * draw s = s.enacted + (rest.length + 1) * draw s
    rw [Nat.succ_mul, Nat.add_assoc, Nat.add_comm (draw s)]

/-- The per-command amount grows strictly with retained cells. -/
theorem draw_grows_with_live (s t : State) (more : s.live < t.live)
    (workspace : s.workspace = t.workspace) : draw s < draw t := by
  unfold draw peak
  rw [workspace]
  exact Nat.add_lt_add_left (Nat.add_lt_add_right (Nat.add_lt_add_right more _) _) _

/-- Cells of a retained one-action cycle model of the given period
(`Machine.cells = 1 + states * (1 + actions)` in the acquisition source). -/
def retainedCycleCells (period : Nat) : Nat := 1 + period * 2

theorem retained_cells_grow (shorter longer : Nat) (less : shorter < longer) :
    retainedCycleCells shorter < retainedCycleCells longer :=
  Nat.add_lt_add_left (Nat.mul_lt_mul_of_pos_right less (by decide)) 1

/-! ## 2. Knowing arrival at a requested contact value -/

/-- Every remaining candidate (phase, reading inversion) has the requested value. -/
def contactKnown (pattern : List Bool) (value : Bool) (belief : List (Nat × Bool)) : Bool :=
  allOf belief fun candidate => bitAt pattern candidate.1 == value

/-- A native reading is the contact value through the unknown inversion
(`tau` xor sensor parity). -/
def readsAs (pattern : List Bool) (observed : Bool) (candidate : Nat × Bool) : Bool :=
  (bitAt pattern candidate.1 != candidate.2) == observed

def advanceAll (period : Nat) (belief : List (Nat × Bool)) : List (Nat × Bool) :=
  belief.map fun candidate => ((candidate.1 + 1) % period, candidate.2)

/-- Within the given number of native commands (advance or read), some strategy
reaches a belief in which the current contact value is known to be `value`,
whatever reading is returned. -/
def knowsWithin (pattern : List Bool) (period : Nat) (value : Bool) :
    Nat → List (Nat × Bool) → Bool
  | 0, belief => contactKnown pattern value belief
  | commands + 1, belief => contactKnown pattern value belief ||
      knowsWithin pattern period value commands (advanceAll period belief) ||
      (knowsWithin pattern period value commands (belief.filter (readsAs pattern false)) &&
        knowsWithin pattern period value commands (belief.filter (readsAs pattern true)))

/-- Phase and reading inversion both unknown. -/
def unknownStart (period : Nat) : List (Nat × Bool) :=
  (upto period).map (fun phase => (phase, false)) ++
    (upto period).map (fun phase => (phase, true))

def bothKnowableWithin (pattern : List Bool) (period commands : Nat) : Bool :=
  knowsWithin pattern period false commands (unknownStart period) &&
    knowsWithin pattern period true commands (unknownStart period)

theorem knows_one_more (pattern : List Bool) (period : Nat) (value : Bool) :
    ∀ (commands : Nat) (belief : List (Nat × Bool)),
      knowsWithin pattern period value commands belief = true →
        knowsWithin pattern period value (commands + 1) belief = true
  | 0, belief, known => by
    change (contactKnown pattern value belief || _ || _) = true
    change contactKnown pattern value belief = true at known
    rw [known]
    rfl
  | commands + 1, belief, known => by
    change (contactKnown pattern value belief ||
      knowsWithin pattern period value commands (advanceAll period belief) ||
      (knowsWithin pattern period value commands (belief.filter (readsAs pattern false)) &&
        knowsWithin pattern period value commands
          (belief.filter (readsAs pattern true)))) = true at known
    change (contactKnown pattern value belief ||
      knowsWithin pattern period value (commands + 1) (advanceAll period belief) ||
      (knowsWithin pattern period value (commands + 1) (belief.filter (readsAs pattern false)) &&
        knowsWithin pattern period value (commands + 1)
          (belief.filter (readsAs pattern true)))) = true
    cases current : contactKnown pattern value belief with
    | true => rfl
    | false =>
      rw [current] at known
      cases advanced : knowsWithin pattern period value commands (advanceAll period belief) with
      | true =>
        rw [knows_one_more pattern period value commands _ advanced]
        rfl
      | false =>
        rw [advanced] at known
        cases low : knowsWithin pattern period value commands
            (belief.filter (readsAs pattern false)) with
        | false => rw [low] at known; cases known
        | true =>
          cases high : knowsWithin pattern period value commands
              (belief.filter (readsAs pattern true)) with
          | false => rw [low, high] at known; cases known
          | true =>
            rw [knows_one_more pattern period value commands _ low,
              knows_one_more pattern period value commands _ high]
            cases knowsWithin pattern period value (commands + 1) (advanceAll period belief) <;>
              rfl

theorem knows_later (pattern : List Bool) (period : Nat) (value : Bool)
    (commands extra : Nat) (belief : List (Nat × Bool))
    (known : knowsWithin pattern period value commands belief = true) :
    knowsWithin pattern period value (commands + extra) belief = true := by
  induction extra with
  | zero => exact known
  | succ extra ih => exact knows_one_more pattern period value (commands + extra) belief ih

theorem both_knowable_later (pattern : List Bool) (period commands extra : Nat)
    (known : bothKnowableWithin pattern period commands = true) :
    bothKnowableWithin pattern period (commands + extra) = true := by
  unfold bothKnowableWithin at known ⊢
  cases low : knowsWithin pattern period false commands (unknownStart period) with
  | false => rw [low] at known; cases known
  | true =>
    cases high : knowsWithin pattern period true commands (unknownStart period) with
    | false => rw [low, high] at known; cases known
    | true =>
      rw [knows_later pattern period false commands extra _ low,
        knows_later pattern period true commands extra _ high]
      rfl

/-- The native contact `(0,0,1)`: both values knowable within seven commands
(the profile `read a read a read`, then at most two advances), not within six. -/
theorem native_cycle_knowable_in_seven_not_six :
    bothKnowableWithin [false, false, true] 3 7 = true ∧
      bothKnowableWithin [false, false, true] 3 6 = false := by
  decide +kernel

/-- Each value separately: the zero value needs four commands, the one value seven. -/
theorem native_cycle_per_value :
    knowsWithin [false, false, true] 3 false 4 (unknownStart 3) = true ∧
      knowsWithin [false, false, true] 3 false 3 (unknownStart 3) = false ∧
      knowsWithin [false, false, true] 3 true 7 (unknownStart 3) = true ∧
      knowsWithin [false, false, true] 3 true 6 (unknownStart 3) = false := by
  decide +kernel

theorem every_two_valued_three_cycle_needs_exactly_seven :
    allOf (patterns 3) (fun pattern => !bothValuesOccur pattern ||
      (bothKnowableWithin pattern 3 7 && !bothKnowableWithin pattern 3 6)) = true := by
  decide +kernel

/-- Exhaustive for periods one through eight: no pattern lets both values be
known within six commands. -/
theorem no_period_through_eight_within_six :
    allOf (upto 8) (fun index => allOf (patterns (index + 1)) fun pattern =>
      !bothKnowableWithin pattern (index + 1) 6) = true := by
  decide +kernel

/-- The pattern repeats with step three around the cycle. -/
def repeatsEveryThree (pattern : List Bool) (period : Nat) : Bool :=
  period % 3 == 0 && allOf (upto period) fun index =>
    bitAt pattern index == bitAt pattern ((index + 3) % period)

/-- Exhaustive for periods one through eight: seven commands suffice only for
patterns that repeat a three-phase pattern. -/
theorem seven_only_by_repeating_three :
    allOf (upto 8) (fun index => allOf (patterns (index + 1)) fun pattern =>
      !bothKnowableWithin pattern (index + 1) 7 ||
        repeatsEveryThree pattern (index + 1)) = true := by
  decide +kernel

/-- A six-phase cycle repeating `001` ties the three-phase cycle in commands. -/
theorem six_cycle_repetition_ties_in_commands :
    bothKnowableWithin [false, false, true, false, false, true] 6 7 = true ∧
      repeatsEveryThree [false, false, true, false, false, true] 6 = true := by
  decide +kernel

/-! ## Finite-list membership, without extensionality axioms -/

theorem allOf_member {α : Type} (test : α → Bool) :
    ∀ (items : List α) (item : α), allOf items test = true → item ∈ items → test item = true
  | [], _, _, member => nomatch member
  | head :: rest, item, all, member => by
    change (test head && allOf rest test) = true at all
    cases first : test head with
    | false => rw [first] at all; cases all
    | true =>
      rw [first] at all
      cases member with
      | head => exact first
      | tail _ later => exact allOf_member test rest item all later

theorem member_append_left {α : Type} {item : α} {left : List α} (right : List α)
    (member : item ∈ left) : item ∈ left ++ right := by
  induction member with
  | head => exact .head _
  | tail _ _ ih => exact .tail _ ih

theorem member_append_right {α : Type} {item : α} (left : List α) {right : List α}
    (member : item ∈ right) : item ∈ left ++ right := by
  induction left with
  | nil => exact member
  | cons _ _ ih => exact .tail _ ih

theorem member_map {α β : Type} (f : α → β) {item : α} {items : List α}
    (member : item ∈ items) : f item ∈ items.map f := by
  induction member with
  | head => exact .head _
  | tail _ _ ih => exact .tail _ ih

theorem member_upto : ∀ (count index : Nat), index < count → index ∈ upto count
  | 0, _, less => nomatch less
  | count + 1, index, less => by
    change index ∈ upto count ++ [count]
    cases Nat.lt_or_eq_of_le (Nat.le_of_lt_succ less) with
    | inl smaller => exact member_append_left _ (member_upto count index smaller)
    | inr same => rw [same]; exact member_append_right _ (.head _)

theorem member_patterns : ∀ (pattern : List Bool), pattern ∈ patterns pattern.length
  | [] => .head _
  | value :: rest => by
    change value :: rest ∈ (patterns rest.length).map (fun tail => false :: tail) ++
      (patterns rest.length).map (fun tail => true :: tail)
    cases value with
    | false => exact member_append_left _ (member_map (fun tail => false :: tail)
        (member_patterns rest))
    | true => exact member_append_right _ (member_map (fun tail => true :: tail)
        (member_patterns rest))

theorem at_least_seven (pattern : List Bool) (commands : Nat)
    (bounded : pattern.length ≤ 8) (positive : 1 ≤ pattern.length)
    (known : bothKnowableWithin pattern pattern.length commands = true) : 7 ≤ commands := by
  cases Nat.lt_or_ge commands 7 with
  | inr enough => exact enough
  | inl fewer =>
    obtain ⟨extra, sum⟩ := Nat.le.dest (Nat.le_of_lt_succ fewer)
    have six := both_knowable_later pattern pattern.length commands extra known
    rw [sum] at six
    have index : pattern.length - 1 < 8 :=
      Nat.lt_of_lt_of_le (Nat.sub_lt positive (by decide)) bounded
    have restored : pattern.length - 1 + 1 = pattern.length :=
      Generative.InquirySufficiency.PacketLawDerivation.sub_add_cancel_constructive
        pattern.length 1 positive
    have forPeriod := allOf_member _ (upto 8) (pattern.length - 1)
      no_period_through_eight_within_six (member_upto 8 _ index)
    rw [restored] at forPeriod
    have forPattern := allOf_member _ (patterns pattern.length) pattern forPeriod
      (member_patterns pattern)
    rw [six] at forPattern
    cases forPattern

/-! ## 3. Selection of the least period by guaranteed drawn activity -/

/-- Given the same other retained cells and workspace, a three-phase organization
guarantees knowing arrival at both contact values with no more drawn activity
than any organization of period three through eight, and strictly less unless
the period is three. `threeState` and `otherState` stand for the native
configurations retaining the respective cycle models. -/
theorem three_phase_least_guaranteed_draw (pattern : List Bool) (commands rest : Nat)
    (threeState otherState : State)
    (three : 3 ≤ pattern.length) (bounded : pattern.length ≤ 8)
    (known : bothKnowableWithin pattern pattern.length commands = true)
    (threeLive : threeState.live = rest + retainedCycleCells 3)
    (otherLive : otherState.live = rest + retainedCycleCells pattern.length)
    (workspace : threeState.workspace = otherState.workspace) :
    7 * draw threeState ≤ commands * draw otherState ∧
      (pattern.length ≠ 3 → 7 * draw threeState < commands * draw otherState) := by
  have seven := at_least_seven pattern commands bounded
    (Nat.le_trans (by decide) three) known
  have perCommand : draw threeState ≤ draw otherState := by
    cases Nat.lt_or_eq_of_le three with
    | inl longer =>
      exact Nat.le_of_lt (draw_grows_with_live threeState otherState
        (by rw [threeLive, otherLive]
            exact Nat.add_lt_add_left (retained_cells_grow 3 _ longer) rest) workspace)
    | inr same =>
      unfold draw peak
      rw [threeLive, otherLive, workspace, ← same]
      exact Nat.le_refl _
  refine ⟨Nat.mul_le_mul seven perCommand, fun different => ?_⟩
  have longer : 3 < pattern.length := by
    cases Nat.lt_or_eq_of_le three with
    | inl longer => exact longer
    | inr same => exact absurd same.symm different
  have strictly : draw threeState < draw otherState :=
    draw_grows_with_live threeState otherState
      (by rw [threeLive, otherLive]
          exact Nat.add_lt_add_left (retained_cells_grow 3 _ longer) rest) workspace
  exact Nat.mul_lt_mul_of_le_of_lt seven strictly (Nat.lt_of_lt_of_le (by decide) seven)

/-! ## 4. Measures that do not select three -/

/-- Advances from a known phase until the requested value is met (at most `period`). -/
def waitFor (pattern : List Bool) (period phase : Nat) (value : Bool) : Nat :=
  ((upto period).filter fun steps => bitAt pattern ((phase + steps) % period) == value).headD period

def totalWait (pattern : List Bool) (period : Nat) : Nat :=
  ((upto period).map fun phase => waitFor pattern period phase false +
    waitFor pattern period phase true).foldl (· + ·) 0

def worstWait (pattern : List Bool) (period : Nat) : Nat :=
  ((upto period).map fun phase => max (waitFor pattern period phase false)
    (waitFor pattern period phase true)).foldl max 0

/-- With a known phase, worst-case alignment ties at two advances, while the
average over phase and requested value favours the five-phase pattern `00101`
(6/10 < 4/6), even after its two extra retained phases raise the per-command
amount from 16384 + 7 to 16384 + 11 (other cells omitted). -/
theorem average_alignment_favours_period_five :
    worstWait [false, false, true] 3 = 2 ∧
      worstWait [false, false, true, false, true] 5 = 2 ∧
      totalWait [false, false, true] 3 = 4 ∧
      totalWait [false, false, true, false, true] 5 = 6 ∧
      6 * (16384 + retainedCycleCells 5) * (2 * 3) <
        4 * (16384 + retainedCycleCells 3) * (2 * 5) := by
  decide

/-- One requested value alone does not select three: a five-phase pattern needs
no more commands for the zero value than the native three-phase pattern. -/
theorem single_value_does_not_select :
    knowsWithin [false, false, false, false, true] 5 false 4 (unknownStart 5) = true ∧
      knowsWithin [false, false, true] 3 false 3 (unknownStart 3) = false := by
  decide +kernel

end Generative.InquirySufficiency.PhasePeriodSelection

#print axioms Generative.InquirySufficiency.PhasePeriodSelection.sensing
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.sensingOnly
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.sensing_command_draws
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.sensing_history_draws
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.draw_grows_with_live
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.retainedCycleCells
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.retained_cells_grow
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.contactKnown
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.readsAs
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.advanceAll
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.knowsWithin
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.unknownStart
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.bothKnowableWithin
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.knows_one_more
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.knows_later
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.both_knowable_later
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.native_cycle_knowable_in_seven_not_six
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.native_cycle_per_value
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.every_two_valued_three_cycle_needs_exactly_seven
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.no_period_through_eight_within_six
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.repeatsEveryThree
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.seven_only_by_repeating_three
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.six_cycle_repetition_ties_in_commands
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.allOf_member
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.member_append_left
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.member_append_right
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.member_map
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.member_upto
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.member_patterns
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.at_least_seven
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.three_phase_least_guaranteed_draw
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.waitFor
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.totalWait
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.worstWait
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.average_alignment_favours_period_five
#print axioms Generative.InquirySufficiency.PhasePeriodSelection.single_value_does_not_select
