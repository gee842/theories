import PredictionAction

/-!
# What the existing action/receipt law identifies when availability is unknown

This module tests the existing Boolean receiptOf relation; it adds no process,
sensor, policy law or persistence premise. Compatibility asks whether some
availability value could produce an observed action/receipt pair. A candidate
fixed regime for a finite record is tested, never asserted to be the real law.

Success identifies the regime at that observation. Failure permits both regimes
when availability is unknown. A mathematical partial decoder reports exactly
the uniquely identified candidate; it is not an installed replacement controller.
Action choices in a record are unrestricted, including choices made from earlier
receipts. Without a success this relation alone eliminates neither candidate,
even after repetition; likelihood claims require a specified stochastic model.
-/

namespace ReceiptIdentification

open PredictionAction

/-- The already executed action and its retained Boolean receipt. -/
abbrev Observation := Bool × Bool

def Compatible (observation : Observation) (regime : Bool) : Prop :=
  ∃ available, receiptOf observation.1 regime available = observation.2

theorem receipt_success_identifies (action regime available : Bool)
    (hsuccess : receiptOf action regime available = true) : regime = action := by
  cases action <;> cases regime <;> cases available <;> cases hsuccess <;> rfl

theorem compatible_success_iff (action regime : Bool) :
    Compatible (action, true) regime ↔ regime = action := by
  constructor
  · rintro ⟨available, h⟩
    exact receipt_success_identifies action regime available h
  · intro h
    subst regime
    exact ⟨true, by cases action <;> rfl⟩

/-- All-unavailable is a witness for either candidate after a failed receipt. -/
theorem failure_compatible (action regime : Bool) : Compatible (action, false) regime := by
  exact ⟨false, by cases action <;> cases regime <;> rfl⟩

theorem compatible_iff_success_matches (action receipt regime : Bool) :
    Compatible (action, receipt) regime ↔ (receipt = true → regime = action) := by
  cases receipt with
  | false =>
    exact ⟨fun _ h => Bool.noConfusion h, fun _ => failure_compatible action regime⟩
  | true =>
    exact ⟨fun h _ => (compatible_success_iff action regime).mp h,
      fun h => (compatible_success_iff action regime).mpr (h rfl)⟩

/-- The original complete decoder errs exactly when the action matched the
regime but availability was absent. No new outage dynamics is used. -/
theorem complete_decoder_correct_iff (action regime available : Bool) :
    decode action (receiptOf action regime available) = regime ↔
      available = true ∨ action ≠ regime := by
  cases action <;> cases regime <;> cases available <;> decide

/-- Availability supplied by the existing paid-work law recovers its original
complete decoder; unknown availability does not justify that specialization. -/
theorem available_complete_decoder_recovered (action regime : Bool) :
    decode action (receiptOf action regime true) = regime :=
  (complete_decoder_correct_iff action regime true).mpr (Or.inl rfl)

def StableCompatible (history : List Observation) (regime : Bool) : Prop :=
  ∀ observation, observation ∈ history → Compatible observation regime

def SuccessesMatch (history : List Observation) (regime : Bool) : Prop :=
  ∀ action, (action, true) ∈ history → regime = action

/-- Under the tested fixed-regime interpretation, failures eliminate neither
candidate; all candidate-eliminating content is the observed successful actions. -/
theorem stable_compatible_iff_successes_match (history : List Observation) (regime : Bool) :
    StableCompatible history regime ↔ SuccessesMatch history regime := by
  constructor
  · intro h action hmem
    exact (compatible_success_iff action regime).mp (h (action, true) hmem)
  · intro h observation hmem
    rcases observation with ⟨action, receipt⟩
    cases receipt with
    | false => exact failure_compatible action regime
    | true => exact (compatible_success_iff action regime).mpr (h action hmem)

/-- The witnesses are all unavailable, regardless of how the actions were chosen. -/
theorem all_failure_records_compatible (history : List Observation)
    (hfailure : ∀ observation, observation ∈ history → observation.2 = false) (regime : Bool) :
    StableCompatible history regime := by
  intro observation hmem
  rcases observation with ⟨action, receipt⟩
  have h : receipt = false := hfailure (action, receipt) hmem
  cases h
  exact failure_compatible action regime

theorem all_failure_records_do_not_identify (history : List Observation)
    (hfailure : ∀ observation, observation ∈ history → observation.2 = false) :
    StableCompatible history false ∧ StableCompatible history true :=
  ⟨all_failure_records_compatible history hfailure false,
    all_failure_records_compatible history hfailure true⟩

/-- Opposed successes refute this fixed-regime interpretation of the record;
they do not refute a changing regime or establish which observation was wrong. -/
theorem opposed_successes_refute_fixed_regime (history : List Observation)
    (hfalse : (false, true) ∈ history) (htrue : (true, true) ∈ history) :
    ¬ ∃ regime, StableCompatible history regime := by
  rintro ⟨regime, hcompatible⟩
  have h := (stable_compatible_iff_successes_match history regime).mp hcompatible
  have impossible : false = true := (h false hfalse).symm.trans (h true htrue)
  cases impossible

/-- Mathematical partial identification, without installing a new controller. -/
def partialDecode (action receipt : Bool) : Option Bool :=
  match receipt with
  | false => none
  | true => some action

def Identifies (observation : Observation) (target : Bool) : Prop :=
  Compatible observation target ∧
    ∀ regime, Compatible observation regime → regime = target

def SoundDecoder (decoder : Bool → Bool → Option Bool) : Prop :=
  ∀ action receipt target, decoder action receipt = some target →
    ∀ regime, Compatible (action, receipt) regime → regime = target

theorem partial_decode_sound : SoundDecoder partialDecode := by
  intro action receipt target hdecode regime hcompatible
  cases receipt with
  | false => cases hdecode
  | true =>
    have htarget : action = target := Option.some.inj hdecode
    exact ((compatible_success_iff action regime).mp hcompatible).trans htarget

/-- Responding is equivalent to there being exactly one compatible candidate. -/
theorem partial_decode_exact (action receipt target : Bool) :
    partialDecode action receipt = some target ↔ Identifies (action, receipt) target := by
  constructor
  · intro hdecode
    cases receipt with
    | false => cases hdecode
    | true =>
      have htarget : action = target := Option.some.inj hdecode
      exact ⟨(compatible_success_iff action target).mpr htarget.symm,
        partial_decode_sound action true target hdecode⟩
  · rintro ⟨hcompatible, hunique⟩
    cases receipt with
    | false =>
      have hf := hunique false (failure_compatible action false)
      have ht := hunique true (failure_compatible action true)
      have impossible : false = true := hf.trans ht.symm
      cases impossible
    | true =>
      exact congrArg some ((compatible_success_iff action target).mp hcompatible).symm

/-- Any decoder sound for every permitted availability must abstain on failure. -/
theorem sound_decoder_abstains_on_failure {decoder : Bool → Bool → Option Bool}
    (hsound : SoundDecoder decoder) (action : Bool) : decoder action false = none := by
  cases hdecode : decoder action false with
  | none => rfl
  | some target =>
    have hf := hsound action false target hdecode false (failure_compatible action false)
    have ht := hsound action false target hdecode true (failure_compatible action true)
    have impossible : false = true := hf.trans ht.symm
    cases impossible

/-- Maximal informativeness is pointwise: any sound answer is this answer.
A sound decoder is still free to abstain unnecessarily after a success. -/
theorem every_sound_answer_is_partial_answer {decoder : Bool → Bool → Option Bool}
    (hsound : SoundDecoder decoder) (action receipt target : Bool)
    (hdecode : decoder action receipt = some target) : partialDecode action receipt = some target := by
  cases receipt with
  | false =>
    have impossible : (none : Option Bool) = some target :=
      (sound_decoder_abstains_on_failure hsound action).symm.trans hdecode
    cases impossible
  | true =>
    have htarget := hsound action true target hdecode action
      ((compatible_success_iff action action).mpr rfl)
    exact congrArg some htarget

/-- Among sound decoders that answer every identifiable observation, the
pointwise behavior is unique. This does not assume physical implementability. -/
theorem sound_complete_decoder_unique {decoder : Bool → Bool → Option Bool}
    (hsound : SoundDecoder decoder)
    (hcomplete : ∀ action receipt target, Identifies (action, receipt) target →
      decoder action receipt = some target) (action receipt : Bool) :
    decoder action receipt = partialDecode action receipt := by
  cases receipt with
  | false => exact sound_decoder_abstains_on_failure hsound action
  | true =>
    exact hcomplete action true action ((partial_decode_exact action true action).mp rfl)

end ReceiptIdentification

#print axioms ReceiptIdentification.receipt_success_identifies
#print axioms ReceiptIdentification.compatible_success_iff
#print axioms ReceiptIdentification.failure_compatible
#print axioms ReceiptIdentification.compatible_iff_success_matches
#print axioms ReceiptIdentification.complete_decoder_correct_iff
#print axioms ReceiptIdentification.available_complete_decoder_recovered
#print axioms ReceiptIdentification.stable_compatible_iff_successes_match
#print axioms ReceiptIdentification.all_failure_records_compatible
#print axioms ReceiptIdentification.all_failure_records_do_not_identify
#print axioms ReceiptIdentification.opposed_successes_refute_fixed_regime
#print axioms ReceiptIdentification.partial_decode_sound
#print axioms ReceiptIdentification.partial_decode_exact
#print axioms ReceiptIdentification.sound_decoder_abstains_on_failure
#print axioms ReceiptIdentification.every_sound_answer_is_partial_answer
#print axioms ReceiptIdentification.sound_complete_decoder_unique
