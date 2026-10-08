import CompositionalTransmission

/-!
Retained encounters change a grouping relation, which is used before an already
formed compositional operation. Elementary event discrimination, observation
slots, the majority threshold, chunk decoder, grouping algorithm and available
additional encounters remain supplied. No acoustic/neural implementation or
universal theory of attention, language or cognitive development is claimed.
-/
namespace Generative.AcquiredSegmentation
open CompositionalAcquisition CompositionalFormation CompositionalTransmission

inductive Sound where
  | a | b | c | d
  deriving DecidableEq, BEq, Repr
open Sound

structure State where
  machine : Frame
  log : List (Option Sound)
  deriving DecidableEq, Repr

def edges : List (Option Sound) → List (Sound × Sound)
  | [] => []
  | [_] => []
  | x::y::rest =>
      match x,y with
      | some u,some v => (u,v)::edges (y::rest)
      | _,_ => edges (y::rest)

def edgeCount (log : List (Option Sound)) (x y : Sound) : Nat := (edges log).count (x,y)
def departures (log : List (Option Sound)) (x : Sound) : Nat :=
  (edges log).countP (fun pair => pair.1 == x)
def bond (log : List (Option Sound)) (x y : Sound) : Bool :=
  decide (departures log x < 2 * edgeCount log x y)

def chunks (r : Sound → Sound → Bool) : List Sound → List (List Sound)
  | [] => []
  | x::xs =>
      match chunks r xs with
      | [] => [[x]]
      | []::rest => [x]::rest
      | (y::ys)::rest =>
          if r x y then (x::y::ys)::rest else [x]::(y::ys)::rest

theorem grouping_preserves_encountered_sequence (r : Sound → Sound → Bool) (xs : List Sound) :
    (chunks r xs).flatten = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
      cases h : chunks r xs with
      | nil => rw [chunks,h]; simpa [h] using congrArg (List.cons x) ih
      | cons ys rest =>
          rw [chunks,h]
          cases ys with
          | nil => simpa [h] using congrArg (List.cons x) ih
          | cons y ys =>
              dsimp only
              split <;> simpa [h,List.cons_append] using congrArg (List.cons x) ih

def decodeChunk : List Sound → Option Expr
  | [.a,.b] => some p0
  | [.c,.d] => some p1
  | _ => none

def decodeChunks : List (List Sound) → Option (List Expr)
  | [] => some []
  | x::xs => do
      let e ← decodeChunk x
      let rest ← decodeChunks xs
      return e::rest

def assembleMessage : List Expr → Option Expr
  | [] => none
  | e::es => some (es.foldl Expr.join e)

def parse (s : State) (raw : List Sound) : Option Expr := do
  let es ← decodeChunks (chunks (bond s.log) raw)
  assembleMessage es

-- Every supplied observation slot is checked at a local charge of one,
-- including a known gap. Gaps do not imply that a sound was identified.
def receive (event : Option Sound) (s : State) : State :=
  if 1 ≤ s.machine.support then
    ⟨{s.machine with support := s.machine.support - 1, spent := s.machine.spent + 1},
      s.log ++ [event]⟩
  else s

def expose : List (Option Sound) → State → State
  | [],s => s
  | x::xs,s => expose xs (receive x s)

def act (raw : List Sound) (s : State) : Option (List Bool × State) := do
  let e ← parse s raw
  let (out,left) ← respond s.machine e
  return (out,⟨{s.machine with support := left, spent := s.machine.spent + (s.machine.support-left)},s.log⟩)

-- A supplied diagnostic policy changes the next sampling scope after failure.
-- The additional encounters are available inputs, not magically generated data.
def broadenAfterFailure (raw : List Sound) (more : List (Option Sound)) (s : State) : State :=
  if (parse s raw).isNone then expose more s else s

theorem receiving_preserves_support (event : Option Sound) (s : State) :
    (receive event s).machine.support + (receive event s).machine.spent =
      s.machine.support + s.machine.spent := by
  unfold receive
  split
  · simp only; omega
  · rfl

theorem exposure_preserves_support (events : List (Option Sound)) (s : State) :
    (expose events s).machine.support + (expose events s).machine.spent =
      s.machine.support + s.machine.spent := by
  induction events generalizing s with
  | nil => rfl
  | cons x xs ih => exact (ih (receive x s)).trans (receiving_preserves_support x s)

theorem insufficient_reception_keeps_actual_record (event : Option Sound) (s : State)
    (short : s.machine.support = 0) : receive event s = s := by
  simp [receive,short]

theorem broadening_preserves_support (raw : List Sound) (more : List (Option Sound)) (s : State) :
    (broadenAfterFailure raw more s).machine.support +
      (broadenAfterFailure raw more s).machine.spent = s.machine.support+s.machine.spent := by
  unfold broadenAfterFailure
  split
  · exact exposure_preserves_support more s
  · rfl

def word : Bool → List Sound
  | false => [.a,.b]
  | true => [.c,.d]
def encode (ws : List Bool) : List Sound := ws.flatMap word

def idealBond (x y : Sound) : Bool :=
  (x == .a && y == .b) || (x == .c && y == .d)

theorem ideal_grouping_recovers_words (ws : List Bool) :
    chunks idealBond (encode ws) = ws.map word := by
  induction ws with
  | nil => rfl
  | cons w ws ih =>
      cases ws with
      | nil => cases w <;> decide
      | cons v vs =>
          cases w <;> cases v <;>
            simp only [encode,List.flatMap_cons,word,List.cons_append,List.nil_append] at ih ⊢
          all_goals rw [chunks,chunks,ih]
          all_goals rfl

theorem decoded_word_sequence (ws : List Bool) :
    decodeChunks (ws.map word) = some (ws.map Expr.atom) := by
  induction ws with
  | nil => rfl
  | cons w ws ih =>
      cases w <;> simp [word,decodeChunks,decodeChunk,p0,p1,ih]

def context : List Sound := [.a,.b,.a,.b,.c,.d,.c,.d,.a,.b]
def additional : List Sound := [.c,.d,.c,.d,.a,.b]
def utterance : List Sound := [.c,.d,.a,.b,.c,.d]
def intended : Expr := .join (.join p1 p0) p1

def ready (n : Nat) : State := ⟨develop (prepared n 4),[]⟩
def experienced (n : Nat) : State := expose (context.map some) (ready n)
def narrow (n : Nat) : State := expose ([.a,.b,.a,.b].map some) (ready n)
def broadened (n : Nat) : State := broadenAfterFailure utterance (additional.map some) (narrow n)

theorem actual_exposure_forms_the_grouping_relation (x y : Sound) :
    bond (experienced 28).log x y = idealBond x y := by
  cases x <;> cases y <;> decide

theorem learned_grouping_transfers_to_every_word_sequence (ws : List Bool) :
    chunks (bond (experienced 28).log) (encode ws) = ws.map word := by
  have same : bond (experienced 28).log = idealBond := by
    funext x y
    exact actual_exposure_forms_the_grouping_relation x y
  rw [same]
  exact ideal_grouping_recovers_words ws

theorem acquired_segmentation_enters_message_assembly (ws : List Bool) :
    parse (experienced 28) (encode ws) = assembleMessage (ws.map Expr.atom) := by
  simp only [parse,learned_grouping_transfers_to_every_word_sequence,decoded_word_sequence]
  rfl

theorem no_experience_leaves_the_message_unparsed :
    parse (ready 28) utterance = none ∧ act utterance (ready 28) = none := by decide

theorem new_grouping_reaches_the_existing_formed_operation :
    parse (experienced 28) utterance = some intended ∧
    (act utterance (experienced 28)).map (fun r => (r.1,r.2.machine.support,r.2.machine.spent)) =
      some ([true,false,true],0,21) := by decide

theorem response_retains_training_history_and_original_acquisition :
    (act utterance (experienced 28)).map (fun r => (r.2.log,r.2.machine.samples)) =
      some (context.map some,trialRecords usual) := by decide

theorem exact_whole_history_account :
    (ready 28).machine.support = 14 ∧ (experienced 28).machine.support = 4 ∧
    7 + 7 + 10 + 4 = 28 := by decide

theorem grouped_message_can_lack_execution_support :
    parse (experienced 27) utterance = some intended ∧ act utterance (experienced 27) = none := by decide

theorem missing_observation_slots_preserve_the_absence_of_an_edge :
    edges [some .a,none,some .b] = [] ∧
    bond [some .a,none,some .b] .a .b = false ∧
    bond [some .a,some .b] .a .b = true := by decide

def reordered : List Sound := [.a,.a,.a,.b,.b,.b,.c,.c,.d,.d]

theorem equal_event_frequencies_do_not_identify_grouping (x : Sound) :
    context.count x = reordered.count x := by cases x <;> decide

theorem encounter_relations_change_grouping_and_use :
    bond (context.map some) .a .b = true ∧ bond (reordered.map some) .a .b = false ∧
    parse (expose (reordered.map some) (ready 28)) utterance = none := by decide

theorem diagnostic_failure_changes_further_acquisition :
    parse (narrow 28) utterance = none ∧
    (broadened 28).log = context.map some ∧
    parse (broadened 28) utterance = some intended ∧
    (act utterance (broadened 28)).map Prod.fst = some [true,false,true] := by decide

theorem recognized_message_does_not_trigger_broadening :
    broadenAfterFailure [.a,.b] (additional.map some) (narrow 28) = narrow 28 := by decide

theorem insufficient_further_acquisition_keeps_a_prefix :
    (broadened 19).log = ([.a,.b,.a,.b,.c].map some) ∧
    parse (broadened 19) utterance = none := by decide

def learnerFavored : List Sound := [.a,.b,.a,.b]

theorem recurrence_can_join_across_the_intended_units :
    chunks (bond (learnerFavored.map some)) learnerFavored = [learnerFavored] ∧
    decodeChunk learnerFavored = none := by decide

end Generative.AcquiredSegmentation
