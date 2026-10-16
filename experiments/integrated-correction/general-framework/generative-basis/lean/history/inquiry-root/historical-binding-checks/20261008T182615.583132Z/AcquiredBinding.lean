import AcquiredSegmentation

/-!
Learned bindings replace the preceding fixed chunk decoder. Encountered forms
and co-present known operations constrain candidates; unresolved or conflicting
records suspend decoding. Categories, known operations, scene coverage, the
intersection rule and judgments excluding a source remain supplied.
This is not a reduction of all meaning or a model of infant neural mechanisms.
-/
namespace Generative.AcquiredBinding
open CompositionalAcquisition CompositionalFormation CompositionalTransmission
open AcquiredSegmentation

structure Encounter where
  form : List Sound
  offered : List Expr
  origin : Nat
  deriving DecidableEq, Repr

structure Lexicon where
  percept : State
  repertoire : List Expr
  records : List Encounter
  excluded : List Nat
  deriving DecidableEq, Repr

def compatible (s : Lexicon) (form : List Sound) (meaning : Expr) : Bool :=
  s.records.all fun r =>
    decide (r.origin ∈ s.excluded ∨ r.form ≠ form ∨ meaning ∈ r.offered)

def candidates (s : Lexicon) (form : List Sound) : List Expr :=
  s.repertoire.filter (compatible s form)

def resolve (s : Lexicon) (form : List Sound) : Option Expr :=
  match candidates s form with
  | [e] => some e
  | _ => none

theorem candidate_characterization (s : Lexicon) (form : List Sound) (meaning : Expr) :
    meaning ∈ candidates s form ↔ meaning ∈ s.repertoire ∧
      ∀ r ∈ s.records, r.origin ∉ s.excluded → r.form = form → meaning ∈ r.offered := by
  simp only [candidates,List.mem_filter,compatible,List.all_eq_true,decide_eq_true_eq]
  constructor
  · intro h
    refine ⟨h.1, ?_⟩
    intro r hr ha hf
    rcases h.2 r hr with h | h | h
    · exact False.elim (ha h)
    · exact False.elim (h hf)
    · exact h
  · intro h
    refine ⟨h.1, ?_⟩
    intro r hr
    by_cases ha : r.origin ∈ s.excluded
    · exact Or.inl ha
    · by_cases hf : r.form = form
      · exact Or.inr (Or.inr (h.2 r hr ha hf))
      · exact Or.inr (Or.inl hf)

theorem resolution_is_a_unique_candidate (s : Lexicon) (form : List Sound) (e : Expr) :
    resolve s form = some e ↔ candidates s form = [e] := by
  unfold resolve
  cases h : candidates s form with
  | nil => simp
  | cons x xs =>
      cases xs with
      | nil => simp
      | cons y ys => simp

theorem adequate_evidence_preserves_target (s : Lexicon) (form : List Sound) (target : Expr)
    (available : target ∈ s.repertoire)
    (sound : ∀ r ∈ s.records, r.origin ∉ s.excluded → r.form = form → target ∈ r.offered) :
    target ∈ candidates s form := (candidate_characterization s form target).mpr ⟨available,sound⟩

theorem unique_resolution_is_correct_under_coverage
    (s : Lexicon) (form : List Sound) (target e : Expr)
    (available : target ∈ s.repertoire)
    (sound : ∀ r ∈ s.records, r.origin ∉ s.excluded → r.form = form → target ∈ r.offered)
    (resolved : resolve s form = some e) : e = target := by
  have mem := adequate_evidence_preserves_target s form target available sound
  rw [(resolution_is_a_unique_candidate s form e).mp resolved] at mem
  have same : target = e := by simpa using mem
  exact same.symm

-- One encountered naming situation has a declared charge of one.
-- Only a single currently recognized chunk enters this local binding interface.
def encounter (raw : List Sound) (offered : List Expr) (origin : Nat) (s : Lexicon) : Lexicon :=
  if 1 ≤ s.percept.machine.support then
    let recorded := match chunks (bond s.percept.log) raw with
      | [form] => s.records ++ [⟨form,offered,origin⟩]
      | _ => s.records
    {s with
      percept := {s.percept with machine := {s.percept.machine with
        support := s.percept.machine.support-1, spent := s.percept.machine.spent+1}}
      records := recorded}
  else s

-- Exclusion is a supplied, fallible access judgment, not automatic truth detection.
-- Original records remain in the retained history.
def excludeSource (origin : Nat) (s : Lexicon) : Lexicon :=
  if 1 ≤ s.percept.machine.support then
    {s with
      percept := {s.percept with machine := {s.percept.machine with
        support := s.percept.machine.support-1, spent := s.percept.machine.spent+1}}
      excluded := origin :: s.excluded}
  else s

theorem encounter_preserves_account (raw : List Sound) (offered : List Expr) (origin : Nat) (s : Lexicon) :
    (encounter raw offered origin s).percept.machine.support +
      (encounter raw offered origin s).percept.machine.spent =
      s.percept.machine.support+s.percept.machine.spent := by
  unfold encounter
  split
  · simp only; omega
  · rfl

theorem exclusion_preserves_original_records (origin : Nat) (s : Lexicon) :
    (excludeSource origin s).records = s.records := by
  unfold excludeSource
  split <;> rfl

theorem no_support_keeps_binding_evidence (raw : List Sound) (offered : List Expr) (origin : Nat)
    (s : Lexicon) (h : s.percept.machine.support = 0) : encounter raw offered origin s = s := by
  simp [encounter,h]

def readForms (s : Lexicon) : List (List Sound) → Option (List Expr)
  | [] => some []
  | f::fs => do
      let e ← resolve s f
      let es ← readForms s fs
      return e::es

def interpret (s : Lexicon) (raw : List Sound) : Option Expr := do
  let es ← readForms s (chunks (bond s.percept.log) raw)
  assembleMessage es

def execute (raw : List Sound) (s : Lexicon) : Option (List Bool × Lexicon) := do
  let e ← interpret s raw
  let (out,left) ← respond s.percept.machine e
  return (out,{s with percept := {s.percept with machine := {s.percept.machine with
    support := left, spent := s.percept.machine.spent+(s.percept.machine.support-left)}}})

def extra : Expr := .twice p0
def emptyBinding (n : Nat) : Lexicon := ⟨experienced n,[p0,p1,extra],[],[]⟩

def teach (s : Lexicon) : Lexicon :=
  encounter (word true) [p1,extra] 0
    (encounter (word false) [p0,extra] 0
      (encounter (word true) [p0,p1] 0
        (encounter (word false) [p0,p1] 0 s)))

def learned (n : Nat) : Lexicon := teach (emptyBinding n)

theorem segmentation_without_binding_cannot_interpret :
    chunks (bond (emptyBinding 32).percept.log) utterance = ( [true,false,true].map word ) ∧
    interpret (emptyBinding 32) utterance = none := by decide

theorem single_ambiguous_encounter_does_not_choose_a_meaning :
    candidates (encounter (word false) [p0,p1] 0 (emptyBinding 32)) (word false) = [p0,p1] ∧
    resolve (encounter (word false) [p0,p1] 0 (emptyBinding 32)) (word false) = none := by decide

theorem actual_encounters_acquire_both_bindings (b : Bool) :
    resolve (learned 32) (word b) = some (.atom b) := by cases b <;> decide

theorem learned_bindings_decode_every_encoded_sequence (ws : List Bool) :
    readForms (learned 32) (ws.map word) = some (ws.map Expr.atom) := by
  induction ws with
  | nil => rfl
  | cons b bs ih =>
      simp only [List.map_cons,readForms,actual_encounters_acquire_both_bindings,ih]
      rfl

theorem acquired_binding_and_grouping_compose (ws : List Bool) :
    interpret (learned 32) (encode ws) = assembleMessage (ws.map Expr.atom) := by
  have grouping : bond (learned 32).percept.log = idealBond := by
    funext x y
    cases x <;> cases y <;> decide
  simp only [interpret,grouping,ideal_grouping_recovers_words,
    learned_bindings_decode_every_encoded_sequence]
  rfl

theorem acquired_bindings_reach_actual_compositional_response :
    (execute utterance (learned 32)).map (fun r => (r.1,r.2.percept.machine.support,
      r.2.percept.machine.spent,r.2.records.length)) = some ([true,false,true],0,25,4) := by decide

theorem actual_binding_history_retains_prior_learning :
    (learned 32).percept.log = context.map some ∧
    (learned 32).percept.machine.samples = trialRecords usual ∧
    (learned 32).records.all (fun r => r.offered.length == 2) = true := by decide

theorem interpretation_can_outlast_affordable_execution :
    interpret (learned 31) utterance = some intended ∧ execute utterance (learned 31) = none := by decide

def repeatedAmbiguity : Lexicon :=
  encounter (word false) [p0,p1] 0 (encounter (word false) [p0,p1] 0 (emptyBinding 32))

theorem repeated_ambiguity_does_not_resolve_reference :
    candidates repeatedAmbiguity (word false) = [p0,p1] ∧
    resolve repeatedAmbiguity (word false) = none := by decide

def misbound : Lexicon := encounter (word false) [p1] 9 (emptyBinding 35)
def conflicted : Lexicon := teach misbound
def repaired : Lexicon := excludeSource 9 conflicted

theorem omitted_target_can_produce_a_wrong_unique_binding :
    resolve misbound (word false) = some p1 ∧
    (execute (word false) misbound).map Prod.fst = some [true] := by decide

theorem contrary_encounters_suspend_instead_of_silently_relabeling :
    resolve conflicted (word false) = none ∧
    resolve conflicted (word true) = some p1 ∧
    conflicted.records.length = 5 := by decide

theorem corrected_admission_repairs_use_without_erasing_history :
    repaired.records = conflicted.records ∧
    resolve repaired (word false) = some p0 ∧
    (execute utterance repaired).map Prod.fst = some [true,false,true] := by decide

theorem excluding_the_sound_encounters_preserves_the_wrong_binding :
    resolve (excludeSource 0 conflicted) (word false) = some p1 := by decide

theorem insufficient_binding_experience_preserves_partial_learning :
    (learned 27).records.length = 3 ∧
    resolve (learned 27) (word false) = some p0 ∧
    resolve (learned 27) (word true) = none := by decide

theorem supplied_repertoire_can_exclude_the_intended_content :
    resolve (encounter (word false) [p0] 0
      {emptyBinding 32 with repertoire := [p1,extra]}) (word false) = none := by decide

theorem failed_grouping_prevents_binding_record_formation :
    (encounter (word false) [p0] 0
      {emptyBinding 32 with percept := ready 32}).records = [] := by decide

end Generative.AcquiredBinding
