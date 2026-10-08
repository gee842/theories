import FormedGrounds
import UnfoldingPreservation

/-!
What a representation must distinguish when its declared target includes the
actual finite unfolding of formed interpretation. Every concrete state below is
reached from FormedGrounds.initial by that module's unchanged step/run, with one
fixed signal convention. The coordinates articulate related effects of this
one execution; they are not separate cognitive and physical starting points.

The chosen reading includes acquired records, signal, judgment, review, access
and remaining inspection support. It omits the presently uninspected specimen
and reference. Native acquisition is totalized: a refused inspection/review is
still an event whose state effects are absent, not an impossible event word.
The original comparison, acquisition, interpretation and revision architecture
remain supplied. No ethical conclusion or unrestricted explanatory necessity
is claimed by these finite witnesses.
-/
namespace Generative.FormedUnfoldingPreservation

open FormedGrounds

set_option synthInstance.maxSize 1024

abbrev Reading :=
  (Option NormativeActivity.Receipt × Option Bool × Bool × Nat × Nat × Nat) ×
  List Evidence × Option Bool × Option Bool × Option Bool × Nat

def reading (s : State) : Reading :=
  (NormativeActivity.view s.native, s.examples, s.signal, s.judgment, s.review, s.incentive)

-- Prefixes are native event words, not independently populated witness states.
def issuedHistory : List Event := training ++ [.setReference 0, .hear, .judge]

def errorHistory : List Event := issuedHistory ++ [.reverseSignal, .judge, .reward 10]

def correctionHistory : List Event := errorHistory ++ [.review]

theorem named_stages_are_native_runs :
    run false issuedHistory initial = issued false ∧
    run false errorHistory initial = mistaken false ∧
    run false correctionHistory initial = corrected false := by
  exact ⟨rfl, rfl, rfl⟩

theorem connected_formation_error_correction :
    (run false training initial).examples.length = 2 ∧
    interpret (observations (run false training initial)) (some true) = some true ∧
    (run false issuedHistory initial).judgment = some false ∧
    (run false errorHistory initial).judgment = some true ∧
    NormativeActivity.target (run false errorHistory initial).native = false ∧
    (run false correctionHistory initial).review = some false ∧
    (run false correctionHistory initial).judgment = some false := by
  decide

theorem calibration_contacts_have_native_provenance :
    AcquiredAlong false training initial ⟨⟨1, 0, false⟩, false⟩ ∧
    AcquiredAlong false training initial ⟨⟨1, 1, true⟩, true⟩ := by
  exact ⟨Or.inl ⟨rfl, rfl, rfl⟩,
    Or.inr (Or.inr (Or.inl ⟨rfl, rfl, rfl⟩))⟩

theorem same_answer_different_review_and_support :
    (issued false).judgment = (corrected false).judgment ∧
    (issued false).review ≠ (corrected false).review ∧
    enabled (issued false) = true ∧ enabled (corrected false) = false ∧
    reading (issued false) ≠ reading (corrected false) := by
  decide

-- Review corrected the judgment, not the disturbed stored signal. Reapplying
-- the learned interpretation therefore restores the error in this architecture.
theorem same_answer_different_rejudgment :
    (issued false).judgment = (corrected false).judgment ∧
    (run false [.judge] (issued false)).judgment = some false ∧
    (run false [.judge] (corrected false)).judgment = some true ∧
    NormativeActivity.target (run false [.judge] (corrected false)).native = false := by
  decide

-- Same native comparison and freshly acquired receipt, different actual use.
theorem record_and_uptake_have_different_outcomes :
    let recorded := run false (errorHistory ++ [.inspectOnly]) initial
    let reviewed := run false correctionHistory initial
    recorded.native = reviewed.native ∧
    recorded.examples = reviewed.examples ∧ recorded.signal = reviewed.signal ∧
    recorded.judgment = some true ∧ reviewed.judgment = some false ∧
    recorded.review = none ∧ reviewed.review = some false ∧
    NormativeActivity.target recorded.native = false := by
  decide

theorem spent_inspection_cannot_be_reused_for_review :
    let recorded := run false (errorHistory ++ [.inspectOnly]) initial
    recorded.native.budget = 0 ∧ recorded.native.inspectionOpen = true ∧
    enabled recorded = false ∧ step false .review recorded = recorded ∧
    recorded.judgment = some true := by
  decide

theorem closed_access_blocks_acquisition_with_support_remaining :
    let closed := run false (errorHistory ++ [.close]) initial
    closed.native.budget = 1 ∧ closed.native.inspectionOpen = false ∧
    enabled closed = false ∧ step false .review closed = closed ∧
    closed.judgment = some true := by
  decide

-- Equal acquired/operative readings can conceal a changed actual comparison.
def changedHistory : List Event := issuedHistory ++ [.setReference 1]

def changed : State := run false changedHistory initial

theorem same_present_reading_different_native_continuation :
    reading (issued false) = reading changed ∧
    enabled (issued false) = true ∧ enabled changed = true ∧
    (run false [.review] (issued false)).judgment = some false ∧
    (run false [.review] changed).judgment = some true ∧
    reading (run false [.review] (issued false)) ≠
      reading (run false [.review] changed) := by
  decide

theorem distinguishing_continuations_are_reachable :
    run false (issuedHistory ++ [.review]) initial =
      run false [.review] (issued false) ∧
    run false (changedHistory ++ [.review]) initial =
      run false [.review] changed := by
  exact ⟨rfl, rfl⟩

-- Neither hidden comparison is read by the judge: only subsequent acquisition
-- differentiates the equal readings. It consumes the last inspection unit.
theorem judging_again_cannot_perform_the_distinguishing_inspection :
    reading (step false .judge (issued false)) = reading (step false .judge changed) ∧
    (step false .judge changed).judgment = some false ∧
    (step false .review changed).native.budget = 0 := by
  decide

-- Two actual acquired records are overwritten before the same final state.
def lowHistory : List Event :=
  [.setReference 0, .inspectOnly, .setReference 0, .inspectOnly]

def highHistory : List Event :=
  [.setReference 1, .inspectOnly, .setReference 0, .inspectOnly]

theorem same_endpoint_different_acquired_history :
    run false lowHistory initial = run false highHistory initial ∧
    (run false [.inspectOnly] initial).native.receipt =
      some ⟨1, 0, false⟩ ∧
    (run false [.setReference 1, .inspectOnly] initial).native.receipt =
      some ⟨1, 1, true⟩ ∧
    reading (run false [.inspectOnly] initial) ≠
      reading (run false [.setReference 1, .inspectOnly] initial) := by
  decide

-- Recording all actual intermediate readings retains the previous witness.
def readings : List Event → State → List Reading
  | [], s => [reading s]
  | e :: es, s => reading s :: readings es (step false e s)

theorem endpoint_equality_does_not_preserve_acquired_path :
    run false lowHistory initial = run false highHistory initial ∧
    lowHistory.length = highHistory.length ∧
    readings lowHistory initial ≠ readings highHistory initial := by
  decide

theorem no_endpoint_decoder_recovers_all_acquired_paths
    (decode : State → List Reading)
    (recovers : ∀ word, decode (run false word initial) = readings word initial) : False := by
  have same := congrArg decode endpoint_equality_does_not_preserve_acquired_path.1
  exact endpoint_equality_does_not_preserve_acquired_path.2.2
    ((recovers lowHistory).symm.trans (same.trans (recovers highHistory)))

-- This relation packages, without weakening or supplementing it, the original
-- total native transition. Acquisition refusal remains its original no-op.
def nativeProcess : Process State Event where
  step s e t := t = step false e s

theorem native_run_has_trace (word : List Event) (s : State) :
    Trace nativeProcess s word (run false word s) := by
  induction word generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons rfl (ih (step false e s))

theorem native_trace_ends_at_run {s t : State} {word : List Event}
    (h : Trace nativeProcess s word t) : t = run false word s := by
  induction h with
  | nil => rfl
  | @cons s m t e es first later ih =>
    change m = step false e s at first
    exact ih.trans (congrArg (run false es) first)

theorem native_trace_iff_run (word : List Event) (s t : State) :
    Trace nativeProcess s word t ↔ t = run false word s := by
  constructor
  · exact native_trace_ends_at_run
  · intro h
    cases h
    exact native_run_has_trace word s

open UnfoldingPreservation

theorem native_answer_iff_run {Outcome : Type} (observe : State → Outcome)
    (s : State) (word : List Event) (outcome : Outcome) :
    NativeAnswer nativeProcess observe s (word, outcome) ↔
      observe (run false word s) = outcome := by
  constructor
  · rintro ⟨t, ht, ho⟩
    exact (congrArg observe (native_trace_ends_at_run ht)).symm.trans ho
  · intro h
    exact ⟨run false word s, native_run_has_trace word s, h⟩

-- This interface asks only selected native outcomes, not full-state identity.
theorem exact_account_separates_native_outcomes {Outcome Code : Type}
    {observe : State → Outcome} {p : Account State Event Outcome Code}
    (hp : ExactAccount nativeProcess observe p)
    {s t : State} {word : List Event}
    (different : observe (run false word s) ≠ observe (run false word t)) :
    p.encode s ≠ p.encode t := by
  apply outcome_difference_separates hp (native_run_has_trace word s) rfl
  intro other ht same
  have endpoint := congrArg observe (native_trace_ends_at_run ht)
  exact different (same.symm.trans endpoint)

theorem exact_future_judgment_separates_equal_current_answers {Code : Type}
    {p : Account State Event (Option Bool) Code}
    (hp : ExactAccount nativeProcess (fun s => s.judgment) p) :
    p.encode (issued false) ≠ p.encode (corrected false) := by
  apply exact_account_separates_native_outcomes hp (word := [.judge])
  decide

theorem exact_future_reading_separates_equal_current_readings {Code : Type}
    {p : Account State Event Reading Code}
    (hp : ExactAccount nativeProcess reading p) :
    p.encode (issued false) ≠ p.encode changed := by
  apply exact_account_separates_native_outcomes hp (word := [.review])
  decide

theorem exact_future_judgment_separates_closed_acquisition {Code : Type}
    {p : Account State Event (Option Bool) Code}
    (hp : ExactAccount nativeProcess (fun s => s.judgment) p) :
    p.encode (run false errorHistory initial) ≠
      p.encode (run false (errorHistory ++ [.close]) initial) := by
  apply exact_account_separates_native_outcomes hp (word := [.review])
  decide

theorem exact_future_judgment_separates_exhausted_acquisition {Code : Type}
    {p : Account State Event (Option Bool) Code}
    (hp : ExactAccount nativeProcess (fun s => s.judgment) p) :
    p.encode (run false errorHistory initial) ≠
      p.encode (run false (errorHistory ++ [.inspectOnly]) initial) := by
  apply exact_account_separates_native_outcomes hp (word := [.review])
  decide

theorem current_answer_alone_is_not_an_exact_future_account
    (reader : Option Bool → List Event × Option Bool → Prop) :
    ¬ ExactAccount nativeProcess (fun s => s.judgment)
      ⟨(fun s => s.judgment), reader⟩ := by
  intro exactAccount
  exact exact_future_judgment_separates_equal_current_answers exactAccount rfl

theorem current_reading_alone_is_not_an_exact_future_account
    (reader : Reading → List Event × Reading → Prop) :
    ¬ ExactAccount nativeProcess reading ⟨reading, reader⟩ := by
  intro exactAccount
  exact exact_future_reading_separates_equal_current_readings exactAccount
    same_present_reading_different_native_continuation.1

end Generative.FormedUnfoldingPreservation

#print axioms Generative.FormedUnfoldingPreservation.Reading
#print axioms Generative.FormedUnfoldingPreservation.reading
#print axioms Generative.FormedUnfoldingPreservation.issuedHistory
#print axioms Generative.FormedUnfoldingPreservation.errorHistory
#print axioms Generative.FormedUnfoldingPreservation.correctionHistory
#print axioms Generative.FormedUnfoldingPreservation.named_stages_are_native_runs
#print axioms Generative.FormedUnfoldingPreservation.connected_formation_error_correction
#print axioms Generative.FormedUnfoldingPreservation.calibration_contacts_have_native_provenance
#print axioms Generative.FormedUnfoldingPreservation.same_answer_different_review_and_support
#print axioms Generative.FormedUnfoldingPreservation.same_answer_different_rejudgment
#print axioms Generative.FormedUnfoldingPreservation.record_and_uptake_have_different_outcomes
#print axioms Generative.FormedUnfoldingPreservation.spent_inspection_cannot_be_reused_for_review
#print axioms Generative.FormedUnfoldingPreservation.closed_access_blocks_acquisition_with_support_remaining
#print axioms Generative.FormedUnfoldingPreservation.changedHistory
#print axioms Generative.FormedUnfoldingPreservation.changed
#print axioms Generative.FormedUnfoldingPreservation.same_present_reading_different_native_continuation
#print axioms Generative.FormedUnfoldingPreservation.distinguishing_continuations_are_reachable
#print axioms Generative.FormedUnfoldingPreservation.judging_again_cannot_perform_the_distinguishing_inspection
#print axioms Generative.FormedUnfoldingPreservation.lowHistory
#print axioms Generative.FormedUnfoldingPreservation.highHistory
#print axioms Generative.FormedUnfoldingPreservation.same_endpoint_different_acquired_history
#print axioms Generative.FormedUnfoldingPreservation.readings
#print axioms Generative.FormedUnfoldingPreservation.endpoint_equality_does_not_preserve_acquired_path
#print axioms Generative.FormedUnfoldingPreservation.no_endpoint_decoder_recovers_all_acquired_paths
#print axioms Generative.FormedUnfoldingPreservation.nativeProcess
#print axioms Generative.FormedUnfoldingPreservation.native_run_has_trace
#print axioms Generative.FormedUnfoldingPreservation.native_trace_ends_at_run
#print axioms Generative.FormedUnfoldingPreservation.native_trace_iff_run
#print axioms Generative.FormedUnfoldingPreservation.native_answer_iff_run
#print axioms Generative.FormedUnfoldingPreservation.exact_account_separates_native_outcomes
#print axioms Generative.FormedUnfoldingPreservation.exact_future_judgment_separates_equal_current_answers
#print axioms Generative.FormedUnfoldingPreservation.exact_future_reading_separates_equal_current_readings
#print axioms Generative.FormedUnfoldingPreservation.exact_future_judgment_separates_closed_acquisition
#print axioms Generative.FormedUnfoldingPreservation.exact_future_judgment_separates_exhausted_acquisition
#print axioms Generative.FormedUnfoldingPreservation.current_answer_alone_is_not_an_exact_future_account
#print axioms Generative.FormedUnfoldingPreservation.current_reading_alone_is_not_an_exact_future_account
