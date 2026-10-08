import FormedGrounds

/-!
Selective revision after the previously checked connected calibration history.
The two retained reports, their assessed usability, and a local purpose are roles
within one continuing practice. The state projects that practice; the projection
does not derive assessments of access, independent evidence, or ethical value.
The comparison reuses the same learned decoder and history interface. Its claim
is observational equivalence at this boundary, not semantic or neural identity.
-/
namespace Generative.SelectiveRevision

structure State where
  calibration : List (StandardsBridge.Observation Bool)
  first : Option Bool
  second : Option Bool
  firstUsable : Bool
  secondUsable : Bool
  purpose : Bool
  deriving DecidableEq, Repr

inductive Event where
  | receive (secondSource token : Bool)
  | withdraw (secondSource : Bool)
  | setPurpose (desired : Bool)
  deriving DecidableEq, Repr

def step (e : Event) (s : State) : State :=
  match e with
  | .receive false token => {s with first := some token}
  | .receive true token => {s with second := some token}
  | .withdraw false => {s with firstUsable := false}
  | .withdraw true => {s with secondUsable := false}
  | .setPurpose desired => {s with purpose := desired}

def run : List Event → State → State
  | [], s => s
  | e :: es, s => run es (step e s)

inductive Ground where
  | empty | supported | conflict
  deriving DecidableEq, Repr

inductive Choice where
  | check | select | decline
  deriving DecidableEq, Repr

structure Outcome where
  judgment : Option Bool
  ground : Ground
  choice : Choice
  deriving DecidableEq, Repr

def usableReading (s : State) (secondSource : Bool) : Option Bool :=
  let token := if secondSource then s.second else s.first
  let usable := if secondSource then s.secondUsable else s.firstUsable
  if usable then FormedGrounds.interpret s.calibration token else none

def combine : Option Bool → Option Bool → Option Bool × Ground
  | none, none => (none, .empty)
  | some b, none | none, some b => (some b, .supported)
  | some a, some b => if a == b then (some a, .supported) else (none, .conflict)

-- A disclosed local preference, not a measure of good or an ethical obligation.
def choose (purpose : Bool) : Option Bool → Choice
  | none => .check
  | some b => if b == purpose then .select else .decline

def outcome (s : State) : Outcome :=
  let assessment := combine (usableReading s false) (usableReading s true)
  ⟨assessment.1, assessment.2, choose s.purpose assessment.1⟩

-- Conventional dependency maintenance: retained positive and negative support.
-- No different observations, truth oracle or extra memory are supplied.
def rails (a b : Option Bool) : Option Bool × Ground :=
  let positive := a == some true || b == some true
  let negative := a == some false || b == some false
  match positive, negative with
  | true, true => (none, .conflict)
  | true, false => (some true, .supported)
  | false, true => (some false, .supported)
  | false, false => (none, .empty)

def conventional (s : State) : Outcome :=
  let assessment := rails (usableReading s false) (usableReading s true)
  ⟨assessment.1, assessment.2, choose s.purpose assessment.1⟩

def prepared (reversed : Bool) (a b : Option Bool)
    (firstUsable secondUsable purpose : Bool) : State :=
  ⟨FormedGrounds.observations (FormedGrounds.trained reversed),
    a.map (FormedGrounds.encode reversed), b.map (FormedGrounds.encode reversed),
    firstUsable, secondUsable, purpose⟩

theorem learned_reading (r : Bool) (a : Option Bool) :
    FormedGrounds.interpret (FormedGrounds.observations (FormedGrounds.trained r))
      (a.map (FormedGrounds.encode r)) = a := by
  cases a with
  | none => rfl
  | some b => exact FormedGrounds.training_forms_decoder r b

theorem prepared_outcome (r : Bool) (a b : Option Bool) (u v g : Bool) :
    outcome (prepared r a b u v g) =
      let assessment := combine (if u then a else none) (if v then b else none)
      ⟨assessment.1, assessment.2, choose g assessment.1⟩ := by
  simp only [outcome, usableReading, prepared, Bool.false_eq_true, ↓reduceIte,
    learned_reading]

theorem purpose_preserves_assessment (s : State) (g : Bool) :
    (outcome (step (.setPurpose g) s)).judgment = (outcome s).judgment ∧
    (outcome (step (.setPurpose g) s)).ground = (outcome s).ground := by
  exact ⟨rfl, rfl⟩

theorem withdrawal_retains_claim_records (s : State) (source : Bool) :
    (step (.withdraw source) s).first = s.first ∧
    (step (.withdraw source) s).second = s.second ∧
    (step (.withdraw source) s).calibration = s.calibration ∧
    (step (.withdraw source) s).purpose = s.purpose := by
  cases source <;> exact ⟨rfl, rfl, rfl, rfl⟩

theorem sole_ground_withdrawn (r b g : Bool) :
    outcome (step (.withdraw false) (prepared r (some b) none true true g)) =
      ⟨none, .empty, .check⟩ := by
  change outcome (prepared r (some b) none false true g) = _
  rw [prepared_outcome]; rfl

theorem redundant_ground_survives (r b g : Bool) :
    outcome (step (.withdraw false) (prepared r (some b) (some b) true true g)) =
      ⟨some b, .supported, choose g (some b)⟩ := by
  change outcome (prepared r (some b) (some b) false true g) = _
  rw [prepared_outcome]; rfl

theorem contrary_reports_conflict (r b g : Bool) :
    outcome (prepared r (some b) (some (!b)) true true g) =
      ⟨none, .conflict, .check⟩ := by
  rw [prepared_outcome]; cases b <;> rfl

theorem withdrawing_conflicting_ground (r b g : Bool) :
    outcome (step (.withdraw false) (prepared r (some b) (some (!b)) true true g)) =
      ⟨some (!b), .supported, choose g (some (!b))⟩ := by
  change outcome (prepared r (some b) (some (!b)) false true g) = _
  rw [prepared_outcome]; rfl

theorem changed_purpose_changes_choice (r b : Bool) :
    outcome (prepared r (some b) none true true b) = ⟨some b, .supported, .select⟩ ∧
    outcome (step (.setPurpose (!b)) (prepared r (some b) none true true b)) =
      ⟨some b, .supported, .decline⟩ := by
  change outcome (prepared r (some b) none true true b) = _ ∧
    outcome (prepared r (some b) none true true (!b)) = _
  rw [prepared_outcome, prepared_outcome]
  cases b <;> exact ⟨rfl, rfl⟩

theorem joint_recoding_preserves_outcome (r : Bool) (a b : Option Bool) (u v g : Bool) :
    outcome (prepared r a b u v g) = outcome (prepared (!r) a b u v g) := by
  rw [prepared_outcome, prepared_outcome]

theorem rails_equal_combine (a b : Option Bool) : rails a b = combine a b := by
  cases a with
  | none => cases b with
    | none => rfl
    | some b => cases b <;> rfl
  | some a => cases b with
    | none => cases a <;> rfl
    | some b => cases a <;> cases b <;> rfl

theorem conventional_matches_all_states (s : State) : conventional s = outcome s := by
  simp only [conventional, outcome, rails_equal_combine]

theorem conventional_matches_every_history (events : List Event) (s : State) :
    conventional (run events s) = outcome (run events s) :=
  conventional_matches_all_states (run events s)

theorem suspension_hides_different_grounds (r g : Bool) :
    (outcome (prepared r none none true true g)).judgment =
      (outcome (prepared r (some true) (some false) true true g)).judgment ∧
    (outcome (prepared r none none true true g)).ground ≠
      (outcome (prepared r (some true) (some false) true true g)).ground := by
  rw [prepared_outcome, prepared_outcome]
  exact ⟨rfl, by decide⟩

-- Two records copied from the earlier physically false signal do not establish
-- truth or independent corroboration, even with perfect support bookkeeping.
def copiedMistake (r g : Bool) : State :=
  let m := FormedGrounds.mistaken r
  ⟨FormedGrounds.observations m, m.signal, m.signal, true, true, g⟩

theorem supported_copied_mistake (r g : Bool) :
    (outcome (copiedMistake r g)).judgment = some true ∧
    (outcome (copiedMistake r g)).ground = .supported ∧
    NormativeActivity.target (FormedGrounds.mistaken r).native = false := by
  cases r <;> cases g <;> decide

-- Diagnostic ablation: assign content from token shape and ignore acquisition.
def rawShape (s : State) : Option Bool := s.first

theorem raw_shape_fails_recoding (b g : Bool) :
    rawShape (prepared true (some b) none true true g) ≠
      (outcome (prepared true (some b) none true true g)).judgment := by
  rw [prepared_outcome]
  cases b <;> decide

end Generative.SelectiveRevision
