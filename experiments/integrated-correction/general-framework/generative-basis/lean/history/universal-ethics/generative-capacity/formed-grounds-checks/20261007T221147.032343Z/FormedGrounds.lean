import NormativeActivity
import StandardsBridge

/-!
One connected calibration, interpretation, error and review history. The binary
signal convention is not preloaded into the answer procedure: actual paired
contacts constrain it. The physical comparison law, retention/review architecture,
question scope and availability of direct comparison are local inputs. This is
not a definition or proof of consciousness, all intentional content, normative
understanding or ethical authority. Native inspection and candidate learning are
imported from the earlier constructions rather than counted as new results.
-/
namespace Generative.FormedGrounds


structure Evidence where
  receipt : NormativeActivity.Receipt
  token : Bool
  deriving DecidableEq, Repr

structure State where
  native : NormativeActivity.State
  examples : List Evidence
  signal : Option Bool
  judgment : Option Bool
  review : Option Bool
  incentive : Nat
  deriving DecidableEq, Repr

def encode (reversed b : Bool) : Bool := if reversed then !b else b

def observations (s : State) : List (StandardsBridge.Observation Bool) :=
  s.examples.map (fun e => (e.token, e.receipt.report))

def hypotheses (s : State) : List (StandardsBridge.Rule Bool) :=
  StandardsBridge.learn StandardsBridge.repertoire (observations s)

-- No actual target, convention bit or reward is an input to interpretation.
def interpret (evidence : List (StandardsBridge.Observation Bool)) (signal : Option Bool) : Option Bool :=
  signal.bind (StandardsBridge.answer (StandardsBridge.learn StandardsBridge.repertoire evidence))

def enabled (s : State) : Bool := s.native.inspectionOpen && decide (0 < s.native.budget)

def contact (reversed : Bool) (s : State) : Evidence :=
  ⟨NormativeActivity.sample s.native, encode reversed (NormativeActivity.target s.native)⟩

inductive Event where
  | calibrate
  | hear
  | judge
  | inspectOnly
  | review
  | setReference (r : Nat)
  | close
  | reverseSignal
  | reward (n : Nat)
  deriving DecidableEq, Repr

def step (reversed : Bool) (e : Event) (s : State) : State :=
  match e with
  | .calibrate =>
      if enabled s then
        {s with native := NormativeActivity.inspect s.native,
                examples := s.examples ++ [contact reversed s]}
      else s
  | .hear =>
      if enabled s then
        {s with native := NormativeActivity.inspect s.native,
                signal := some (encode reversed (NormativeActivity.target s.native))}
      else s
  | .judge => {s with judgment := interpret (observations s) s.signal}
  | .inspectOnly => {s with native := NormativeActivity.inspect s.native}
  | .review =>
      if enabled s then
        let receipt := NormativeActivity.sample s.native
        {s with native := NormativeActivity.inspect s.native,
                review := s.judgment.map (fun b => b == receipt.report),
                judgment := some receipt.report}
      else s
  | .setReference r => {s with native := NormativeActivity.step (.changeReference r) s.native}
  | .close => {s with native := NormativeActivity.step .close s.native}
  | .reverseSignal => {s with signal := s.signal.map Bool.not}
  | .reward n => {s with incentive := s.incentive + n}

def run (reversed : Bool) : List Event → State → State
  | [], s => s
  | e :: es, s => run reversed es (step reversed e s)

def initial : State := ⟨{NormativeActivity.initial with budget := 4}, [], none, none, none, 0⟩

def training : List Event := [.calibrate, .setReference 1, .calibrate]

def trained (reversed : Bool) : State := run reversed training initial

def issued (reversed : Bool) : State :=
  run reversed [.setReference 0, .hear, .judge] (trained reversed)

def mistaken (reversed : Bool) : State :=
  run reversed [.reverseSignal, .judge, .reward 10] (issued reversed)

def corrected (reversed : Bool) : State := step reversed .review (mistaken reversed)

-- A trace-level origin predicate; provenance is not merely a consistent record.
def AcquiredAlong (reversed : Bool) : List Event → State → Evidence → Prop
  | [], _, _ => False
  | e :: es, s, r =>
      (e = .calibrate ∧ enabled s = true ∧ contact reversed s = r) ∨
      AcquiredAlong reversed es (step reversed e s) r

theorem run_append (reversed : Bool) (xs ys : List Event) (s : State) :
    run reversed (xs ++ ys) s = run reversed ys (run reversed xs s) := by
  induction xs generalizing s with
  | nil => rfl
  | cons x xs ih => exact ih (step reversed x s)

theorem encode_involutive (reversed b : Bool) :
    encode reversed (encode reversed b) = b := by cases reversed <;> cases b <;> rfl

theorem interpretation_depends_on_acquired_view (s t : State)
    (sameEvidence : observations s = observations t) (sameSignal : s.signal = t.signal)
    (r u : Bool) :
    (step r .judge s).judgment = (step u .judge t).judgment := by
  simp only [step, sameEvidence, sameSignal]

theorem step_evidence_origin (reversed : Bool) (e : Event) (s : State) (r : Evidence)
    (retained : r ∈ (step reversed e s).examples) :
    r ∈ s.examples ∨ (e = .calibrate ∧ enabled s = true ∧ contact reversed s = r) := by
  cases e <;> simp only [step] at retained
  case calibrate =>
    split at retained
    · rename_i active
      simp only [List.mem_append, List.mem_cons, List.not_mem_nil, or_false] at retained
      rcases retained with old | fresh
      · exact Or.inl old
      · exact Or.inr ⟨rfl, active, fresh.symm⟩
    · exact Or.inl retained
  case hear => split at retained <;> exact Or.inl retained
  case review => split at retained <;> exact Or.inl retained
  all_goals exact Or.inl retained

theorem retained_evidence_origin (reversed : Bool) (es : List Event) (s : State)
    (r : Evidence) (retained : r ∈ (run reversed es s).examples) :
    r ∈ s.examples ∨ AcquiredAlong reversed es s r := by
  induction es generalizing s with
  | nil => exact Or.inl retained
  | cons e es ih =>
    rcases ih (step reversed e s) retained with old | later
    · rcases step_evidence_origin reversed e s r old with original | acquired
      · exact Or.inl original
      · exact Or.inr (Or.inl acquired)
    · exact Or.inr (Or.inr later)

theorem from_initial_evidence_is_acquired (reversed : Bool) (es : List Event)
    (r : Evidence) (retained : r ∈ (run reversed es initial).examples) :
    AcquiredAlong reversed es initial r := by
  rcases retained_evidence_origin reversed es initial r retained with empty | acquired
  · cases empty
  · exact acquired

theorem contact_has_physical_correspondence (reversed : Bool) (s : State) :
    (contact reversed s).receipt.report =
      decide ((contact reversed s).receipt.specimen ≤ (contact reversed s).receipt.reference) ∧
    encode reversed (contact reversed s).token = (contact reversed s).receipt.report := by
  exact ⟨rfl, encode_involutive reversed (NormativeActivity.target s.native)⟩

theorem before_calibration_no_definite_interpretation (b : Bool) :
    interpret (observations initial) (some b) = none := by cases b <;> decide

theorem one_contact_leaves_unseen_signal_unsettled (reversed : Bool) :
    interpret (observations (step reversed .calibrate initial))
      (some (encode reversed true)) = none := by cases reversed <;> decide

theorem training_forms_decoder (reversed b : Bool) :
    interpret (observations (trained reversed)) (some (encode reversed b)) = some b := by
  cases reversed <;> cases b <;> decide

theorem training_uses_real_contrasts (reversed : Bool) :
    (trained reversed).examples.length = 2 ∧
    (trained reversed).native.budget = 2 ∧
    (trained reversed).judgment = none := by cases reversed <;> decide

theorem token_shape_does_not_fix_content :
    interpret (observations (trained false)) (some true) = some true ∧
    interpret (observations (trained true)) (some true) = some false := by decide

theorem joint_recoding_preserves_interpreted_content (reversed b : Bool) :
    interpret (observations (trained reversed)) (some (encode reversed b)) =
      interpret (observations (trained (!reversed))) (some (encode (!reversed) b)) := by
  rw [training_forms_decoder, training_forms_decoder]

theorem learned_interpretation_is_used (reversed : Bool) :
    (issued reversed).judgment = some (NormativeActivity.target (issued reversed).native) ∧
    (issued reversed).judgment = some false ∧ (issued reversed).native.budget = 1 := by
  cases reversed <;> decide

theorem same_formed_interpretation_can_be_false (reversed : Bool) :
    observations (mistaken reversed) = observations (issued reversed) ∧
    (mistaken reversed).judgment = some true ∧
    NormativeActivity.target (mistaken reversed).native = false ∧
    (mistaken reversed).incentive = 10 := by cases reversed <;> decide

theorem new_record_without_review_does_not_correct (reversed : Bool) :
    let s := step reversed .inspectOnly (mistaken reversed)
    s.native.receipt = some (NormativeActivity.sample (mistaken reversed).native) ∧
    s.judgment = some true ∧ NormativeActivity.target s.native = false := by cases reversed <;> decide

theorem acquired_review_refutes_and_corrects (reversed : Bool) :
    (corrected reversed).review = some false ∧
    (corrected reversed).judgment = some false ∧
    (corrected reversed).judgment = some (NormativeActivity.target (corrected reversed).native) ∧
    (corrected reversed).incentive = 10 ∧ (corrected reversed).native.budget = 0 := by
  cases reversed <;> decide

theorem review_preserves_meaning_and_compared_relation (reversed : Bool) :
    observations (corrected reversed) = observations (mistaken reversed) ∧
    (corrected reversed).native.specimen = (mistaken reversed).native.specimen ∧
    (corrected reversed).native.reference = (mistaken reversed).native.reference := by
  cases reversed <;> decide

theorem correct_prior_judgment_is_confirmed (reversed : Bool) :
    (step reversed .review (issued reversed)).review = some true := by
  cases reversed <;> decide

theorem closed_review_cannot_claim_confirmation (reversed : Bool) :
    let s := step reversed .review (step reversed .close (mistaken reversed))
    s.review = none ∧ s.judgment = some true := by cases reversed <;> decide

theorem exhausted_review_does_not_acquire_a_ground (reversed : Bool) :
    let s := step reversed .inspectOnly (mistaken reversed)
    step reversed .review s = s := by cases reversed <;> decide

theorem reward_alone_cannot_repair_interpretation (reversed : Bool) (n : Nat) :
    (step reversed (.reward n) (mistaken reversed)).judgment = some true := by
  cases reversed <;> rfl

theorem full_history_is_one_reachable_execution (reversed : Bool) :
    corrected reversed = run reversed
      (training ++ [.setReference 0, .hear, .judge, .reverseSignal, .judge,
                    .reward 10, .review]) initial := by
  cases reversed <;> rfl

-- A review relation can concern historical content without certifying later use.
theorem later_change_retains_review_but_defeats_current_accuracy (reversed : Bool) :
    let s := step reversed (.setReference 1) (corrected reversed)
    s.review = some false ∧ s.judgment = some false ∧ NormativeActivity.target s.native = true := by
  cases reversed <;> decide

end Generative.FormedGrounds
