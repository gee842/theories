import EnactedScene

/-!
Acquired access records participate in selecting subsequent encounters. Fresh
movement/observation revises those records; local naming follows actual access.
The common arrangement, categories, candidate-intersection heuristic, catalogue,
cooperative naming law and charges are supplied. This composes existing learning
mechanisms; it does not derive a universal curiosity objective or intention.
-/
namespace Generative.EncounterChoice
open CompositionalAcquisition CompositionalFormation CompositionalTransmission
open AcquiredSegmentation AcquiredBinding EnactedScene

structure View where
  at : Place
  seen : List Expr
  deriving DecidableEq, Repr

structure Activity where
  situation : Situation
  views : List View
  tried : List Place
  deriving DecidableEq, Repr

def recalled (views : List View) (p : Place) : Option (List Expr) :=
  (views.reverse.find? (fun v => v.at == p)).map View.seen

def observe (s : Activity) : Activity :=
  let m := s.situation.lexicon.percept.machine
  if 1 ≤ m.support then
    {s with
      views := s.views ++ [⟨s.situation.position,visible s.situation⟩]
      situation := {s.situation with lexicon := {s.situation.lexicon with
        percept := {s.situation.lexicon.percept with
          machine := {m with support := m.support-1,spent := m.spent+1}}}}}
  else s

def survey (p : Place) (s : Activity) : Activity :=
  let moved := {s with situation := move p s.situation}
  if moved.situation.position = p then observe moved else moved

-- This naming law concerns actually accessible operations. It does not read the
-- learner's binding or reward a preferred answer. Its cooperative coverage is
-- a substantive social premise, not a consequence of ambiguity reduction.
def speak : List Expr → List Expr → Lexicon → Lexicon
  | [],_,s => s
  | e::rest,offered,s =>
      let next := match nameForm e with
        | none => s
        | some raw => AcquiredBinding.encounter raw offered 0 s
      speak rest offered next

def localNaming (s : Activity) : Activity :=
  let offered := visible s.situation
  {s with situation := {s.situation with
    lexicon := speak offered offered s.situation.lexicon}}

def complete (s : Lexicon) : Bool :=
  (resolve s (word false)).isSome && (resolve s (word true)).isSome

def informative (s : Lexicon) (seen : List Expr) : Bool :=
  [false,true].any fun b =>
    let old := candidates s (word b)
    let remaining := old.filter (fun e => decide (e ∈ seen))
    decide (1 < old.length ∧ 0 < remaining.length ∧ remaining.length < old.length)

-- Choice has no actual sites/position input. It uses retained access reports,
-- current bindings, the explored catalogue and a supplied first-match rule.
def choose (s : Lexicon) (views : List View) (tried catalogue : List Place) : Option Place :=
  if complete s then none else
    let available := catalogue.filter (fun p => decide (p ∉ tried))
    match available.find? (fun p => (recalled views p).any (informative s)) with
    | some p => some p
    | none => available.head?

def visit (p : Place) (s : Activity) : Activity :=
  let acquired := survey p s
  let named := if acquired.situation.position = p then localNaming acquired else acquired
  {named with tried := named.tried ++ [p]}

def step (catalogue : List Place) (s : Activity) : Activity :=
  match choose s.situation.lexicon s.views s.tried catalogue with
  | none => s
  | some p => visit p s

def run : Nat → List Place → Activity → Activity
  | 0,_,s => s
  | n+1,cs,s => run n cs (step cs s)

def account (s : Activity) : Nat :=
  s.situation.lexicon.percept.machine.support+s.situation.lexicon.percept.machine.spent

theorem observation_preserves_account (s : Activity) : account (observe s) = account s := by
  unfold observe
  dsimp only
  split
  · simp only [account]; omega
  · rfl

theorem survey_preserves_account (p : Place) (s : Activity) : account (survey p s) = account s := by
  unfold survey
  dsimp only
  split
  · exact (observation_preserves_account _).trans (moving_preserves_support_account p s.situation)
  · exact moving_preserves_support_account p s.situation

theorem speaking_preserves_account (es offered : List Expr) (s : Lexicon) :
    (speak es offered s).percept.machine.support+(speak es offered s).percept.machine.spent =
      s.percept.machine.support+s.percept.machine.spent := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    simp only [speak]
    cases h : nameForm e with
    | none => exact ih s
    | some raw => exact (ih _).trans (AcquiredBinding.encounter_preserves_account raw offered 0 s)

theorem naming_preserves_account (s : Activity) : account (localNaming s) = account s :=
  speaking_preserves_account _ _ _

theorem visit_preserves_account (p : Place) (s : Activity) : account (visit p s) = account s := by
  unfold visit
  dsimp only
  split
  · exact (naming_preserves_account _).trans (survey_preserves_account p s)
  · exact survey_preserves_account p s

theorem step_preserves_account (cs : List Place) (s : Activity) : account (step cs s) = account s := by
  unfold step
  split
  · rfl
  · exact visit_preserves_account _ _

theorem run_preserves_account (n : Nat) (cs : List Place) (s : Activity) :
    account (run n cs s) = account s := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih => exact (ih (step cs s)).trans (step_preserves_account cs s)

def catalogue : List Place := [(1,0),(0,1),(2,2)]
def initial (n : Nat) : Activity := ⟨EnactedScene.start n,[],[]⟩
def calibrated (n : Nat) : Activity := survey (2,2) (survey (0,1) (survey (1,0) (initial n)))
def first (n : Nat) : Activity := step catalogue (calibrated n)
def second (n : Nat) : Activity := step catalogue (first n)
def acquired (n : Nat) : Activity := run 3 catalogue (calibrated n)

theorem calibration_records_actual_access :
    (calibrated 51).views = [⟨(1,0),[p0,p1]⟩,⟨(0,1),[p0,extra]⟩,⟨(2,2),[p1,extra]⟩] ∧
    (calibrated 51).situation.lexicon.records = [] := by decide

theorem binding_changes_which_scene_is_chosen :
    choose (calibrated 51).situation.lexicon (calibrated 51).views [] catalogue = some (1,0) ∧
    choose (first 51).situation.lexicon (first 51).views (first 51).tried catalogue = some (0,1) ∧
    choose (second 51).situation.lexicon (second 51).views (second 51).tried catalogue = some (2,2) := by decide

theorem selected_encounters_supply_previous_interpretation_inputs :
    interpretationInputs (acquired 51).situation.lexicon = interpretationInputs (coordinated 37).lexicon := by decide

theorem selected_encounters_transfer_to_all_sequences (ws : List Bool) :
    interpret (acquired 51).situation.lexicon (encode ws) = assembleMessage (ws.map Expr.atom) := by
  rw [same_inputs_preserve_interpretation _ _ selected_encounters_supply_previous_interpretation_inputs]
  exact enacted_access_enters_all_sequence_interpretation ws

theorem selected_history_reaches_actual_response :
    (execute utterance (acquired 51).situation.lexicon).map
      (fun r => (r.1,r.2.percept.machine.support,r.2.percept.machine.spent)) =
      some ([true,false,true],0,44) := by decide

theorem history_accounts_for_survey_and_use :
    (acquired 51).situation.lexicon.percept.machine.support = 4 ∧
    (acquired 51).views.length = 6 ∧
    (acquired 51).tried = catalogue ∧ 7+7+10+8+3+5+3+4+4 = 51 := by decide

-- An actual earlier arrangement made this location show both atoms. Changing
-- the arrangement leaves that truthful historical report stale; survey replaces
-- its predictive use without deleting the earlier report.
def earlierArrangement : Activity :=
  {initial 60 with situation := { (initial 60).situation with
    sites := [((0,0),p0),((0,2),p1),((4,4),extra)] }}
def olderView : Activity := survey (0,1) earlierArrangement

def staleChoice : Activity :=
  {first 60 with views := (first 60).views ++ olderView.views}

theorem changed_arrangement_can_leave_an_accurate_old_record_stale :
    olderView.views = [⟨(0,1),[p0,p1]⟩] ∧
    recalled staleChoice.views (0,1) = some [p0,p1] ∧
    visible (move (0,1) staleChoice.situation) = [p0,extra] := by decide

theorem stale_prediction_changes_choice_before_reobservation :
    choose staleChoice.situation.lexicon staleChoice.views staleChoice.tried catalogue = some (2,2) := by decide

theorem reobservation_revises_the_access_model_and_next_choice :
    recalled (survey (0,1) staleChoice).views (0,1) = some [p0,extra] ∧
    (survey (0,1) staleChoice).views.take staleChoice.views.length = staleChoice.views ∧
    choose (survey (0,1) staleChoice).situation.lexicon
      (survey (0,1) staleChoice).views staleChoice.tried catalogue = some (0,1) := by decide

theorem survey_without_names_does_not_supply_bindings :
    (calibrated 51).situation.lexicon.records = [] ∧
    interpret (calibrated 51).situation.lexicon utterance = none := by decide

theorem poor_catalogue_leaves_ambiguity :
    complete (run 3 [(1,0)] (calibrated 51)).situation.lexicon = false ∧
    choose (run 3 [(1,0)] (calibrated 51)).situation.lexicon
      (run 3 [(1,0)] (calibrated 51)).views [(1,0)] [(1,0)] = none := by decide

theorem acquired_binding_can_exhaust_response_support :
    interpret (acquired 50).situation.lexicon utterance = some intended ∧
    execute utterance (acquired 50).situation.lexicon = none := by decide

theorem known_access_does_not_execute_an_unaffordable_visit :
    (visit (0,1) (first 38)).situation.position = (1,0) ∧
    (visit (0,1) (first 38)).situation.lexicon.records = (first 38).situation.lexicon.records := by decide

theorem local_naming_does_not_name_an_absent_atom :
    (localNaming (survey (0,1) (initial 40))).situation.lexicon.records.map Encounter.form = [word false] := by decide

theorem removing_coverage_can_make_the_stopping_rule_wrong :
    complete (mistimed 51).lexicon = true ∧
    choose (mistimed 51).lexicon (calibrated 51).views [] catalogue = none ∧
    (execute utterance (mistimed 51).lexicon).map Prod.fst = some [false,true,false] := by decide

end Generative.EncounterChoice
