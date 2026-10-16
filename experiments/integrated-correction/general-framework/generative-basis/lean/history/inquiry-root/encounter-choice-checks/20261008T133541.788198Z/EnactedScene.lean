import AcquiredBinding

/-!
Positions and naming participate in one local encounter history. Accessible
alternatives are computed from the current relational arrangement, then enter
the existing acquired binding mechanism. This geometric projection supplies
its range, categories, movement law, naming convention and movement schedule.
It does not derive bodies, attention, intentions or their evolutionary origins.
-/
namespace Generative.EnactedScene
open CompositionalAcquisition CompositionalFormation CompositionalTransmission
open AcquiredSegmentation AcquiredBinding

abbrev Place := Nat × Nat

def distance (p q : Place) : Nat :=
  (p.1-q.1)+(q.1-p.1)+(p.2-q.2)+(q.2-p.2)

structure Situation where
  lexicon : Lexicon
  position : Place
  sites : List (Place × Expr)
  deriving DecidableEq, Repr

def visible (s : Situation) : List Expr :=
  (s.sites.filter (fun item => decide (distance s.position item.1 ≤ 2))).map Prod.snd

def move (destination : Place) (s : Situation) : Situation :=
  let cost := distance s.position destination
  if cost ≤ s.lexicon.percept.machine.support then
    {s with
      position := destination
      lexicon := {s.lexicon with
        percept := {s.lexicon.percept with
          machine := {s.lexicon.percept.machine with
            support := s.lexicon.percept.machine.support-cost
            spent := s.lexicon.percept.machine.spent+cost}}}}
  else s

-- The naming convention is supplied. Its target is a site in this same
-- situation, not the learner's currently preferred binding or visible list.
def nameForm : Expr → Option (List Sound)
  | .atom b => some (word b)
  | _ => none

def naming (site : Nat) (s : Situation) (retain : Bool := true) : Situation :=
  match s.sites[site]? with
  | none => s
  | some item =>
      match nameForm item.2 with
      | none => s
      | some raw =>
          let updated := encounter raw (visible s) 0 s.lexicon
          {s with lexicon := if retain then updated
            else {updated with records := s.lexicon.records}}

theorem moving_preserves_binding_records (p : Place) (s : Situation) :
    (move p s).lexicon.records = s.lexicon.records := by
  unfold move
  dsimp only
  split <;> rfl

theorem moving_preserves_support_account (p : Place) (s : Situation) :
    (move p s).lexicon.percept.machine.support + (move p s).lexicon.percept.machine.spent =
      s.lexicon.percept.machine.support+s.lexicon.percept.machine.spent := by
  unfold move
  dsimp only
  split
  · simp only; omega
  · rfl

theorem unaffordable_movement_preserves_actual_position (p : Place) (s : Situation)
    (short : s.lexicon.percept.machine.support < distance s.position p) : move p s = s := by
  simp [move,Nat.not_le.mpr short]

def start (n : Nat) : Situation :=
  ⟨emptyBinding n,(1,0),[((0,0),p0),((2,0),p1),((0,2),extra)]⟩

def coordinated (n : Nat) (retain : Bool := true) : Situation :=
  naming 1 (move (2,2) (naming 0 (move (0,1)
    (naming 1 (naming 0 (start n) retain) retain)) retain)) retain

def stationary (n : Nat) : Situation :=
  naming 1 (naming 0 (naming 1 (naming 0 (start n))))

def mistimed (n : Nat) : Situation :=
  naming 0 (move (2,2) (naming 1 (move (0,1)
    (naming 1 (naming 0 (start n))))))

-- Exactly the inputs used by grouping and binding, not an identity of whole
-- states or their histories of resource expenditure.
def interpretationInputs (s : Lexicon) :=
  (s.percept.log,s.repertoire,s.records,s.excluded)

theorem same_inputs_preserve_interpretation (s t : Lexicon)
    (h : interpretationInputs s = interpretationInputs t) (raw : List Sound) :
    interpret s raw = interpret t raw := by
  simp only [interpretationInputs,Prod.mk.injEq] at h
  have binding : ∀ f, resolve s f = resolve t f := by
    intro f
    have comp : compatible s f = compatible t f := by
      funext e
      simp only [compatible,h.2.2.1,h.2.2.2]
    simp only [resolve,candidates,h.2.1,comp]
  have reading : ∀ fs, readForms s fs = readForms t fs := by
    intro fs
    induction fs with
    | nil => rfl
    | cons f fs ih => simp only [readForms,binding,ih]
  simp only [interpret,h.1,reading]

theorem movement_changes_accessible_alternatives :
    visible (start 37) = [p0,p1] ∧
    visible (move (0,1) (start 37)) = [p0,extra] ∧
    visible (move (2,2) (move (0,1) (start 37))) = [p1,extra] := by decide

theorem enacted_scenes_supply_the_previous_binding_inputs :
    interpretationInputs (coordinated 37).lexicon = interpretationInputs (learned 32) := by decide

theorem enacted_access_enters_all_sequence_interpretation (ws : List Bool) :
    interpret (coordinated 37).lexicon (encode ws) = assembleMessage (ws.map Expr.atom) := by
  rw [same_inputs_preserve_interpretation _ _ enacted_scenes_supply_the_previous_binding_inputs]
  exact acquired_binding_and_grouping_compose ws

theorem enacted_access_reaches_actual_response :
    (execute utterance (coordinated 37).lexicon).map
      (fun r => (r.1,r.2.percept.machine.support,r.2.percept.machine.spent)) =
      some ([true,false,true],0,30) := by decide

theorem movement_is_in_the_same_support_history :
    (coordinated 37).lexicon.percept.machine.support = 4 ∧
    (coordinated 37).lexicon.percept.machine.spent = 26 ∧
    7+7+10+5+4+4 = 37 := by decide

theorem stationary_repetition_leaves_both_bindings_ambiguous :
    (stationary 37).lexicon.records.length = 4 ∧
    resolve (stationary 37).lexicon (word false) = none ∧
    resolve (stationary 37).lexicon (word true) = none := by decide

theorem access_without_recording_does_not_acquire_the_bindings :
    (coordinated 37 false).position = (coordinated 37).position ∧
    (coordinated 37 false).lexicon.percept.machine = (coordinated 37).lexicon.percept.machine ∧
    (coordinated 37 false).lexicon.records = [] ∧
    interpret (coordinated 37 false).lexicon utterance = none := by decide

theorem unchanged_position_and_name_counts_do_not_establish_coordination :
    (mistimed 37).position = (coordinated 37).position ∧
    (mistimed 37).lexicon.percept.machine = (coordinated 37).lexicon.percept.machine ∧
    ((mistimed 37).lexicon.records.map Encounter.form).count (word false) = 2 ∧
    ((mistimed 37).lexicon.records.map Encounter.form).count (word true) = 2 ∧
    resolve (mistimed 37).lexicon (word false) = some p1 ∧
    resolve (mistimed 37).lexicon (word true) = some p0 := by decide

theorem mistimed_naming_produces_an_actual_inverted_response :
    (execute utterance (mistimed 37).lexicon).map Prod.fst = some [false,true,false] := by decide

def narrowWrong : Situation := naming 0 (move (0,3) (start 32))

theorem a_clear_view_can_omit_the_named_target :
    visible narrowWrong = [extra] ∧
    resolve narrowWrong.lexicon (word false) = some extra ∧
    (execute (word false) narrowWrong.lexicon).map Prod.fst = some [false,false] := by decide

theorem movement_support_can_run_out_before_a_response :
    interpret (coordinated 36).lexicon utterance = some intended ∧
    execute utterance (coordinated 36).lexicon = none := by decide

theorem impossible_movement_does_not_invent_a_new_scene :
    (move (2,2) (start 24)).position = (1,0) ∧
    visible (move (2,2) (start 24)) = [p0,p1] := by decide

end Generative.EnactedScene
