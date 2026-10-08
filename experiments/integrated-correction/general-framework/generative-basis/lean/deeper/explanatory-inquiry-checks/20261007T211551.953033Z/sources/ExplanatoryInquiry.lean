import ExplanatoryRecovery
import KnowledgeCorrespondence

/-! Acquisition, calibration, revision and reuse within one supported history.
Record consistency is proved from transition rules; it is not a step guard.
The fixed-reference preparation and revision coverage are explicit model laws. -/
namespace Generative.ExplanatoryInquiry

open ExplanatoryVariation
namespace KC := Generative.KnowledgeCorrespondence

structure Receipt where
  epoch : Nat
  bit : Bool
  deriving DecidableEq

structure State where
  gates : GateState
  reversed : Bool
  epoch : Nat
  standard : Option Bool
  targetRead : Option Receipt
  referenceRead : Option Receipt
  judgment : Option Receipt
  fuel : Nat

inductive Event where
  | prepare | readTarget | readReference | judge
  | gate (e : ExplanatoryVariation.Event)
  | reverseChannel

def targetSignal (s : State) : Bool := KC.signal ⟨s.gates.leftOpen, s.reversed⟩
def referenceSignal (s : State) (v : Bool) : Bool := Bool.xor v s.reversed

inductive Step : State → Event → State → Prop where
  | prepare (s : State) (n : Nat) (hf : s.fuel = n + 1) :
      Step s .prepare { s with standard := some false, fuel := n }
  | readTarget (s : State) (n : Nat) (hf : s.fuel = n + 1) :
      Step s .readTarget
        { s with targetRead := some ⟨s.epoch, targetSignal s⟩, fuel := n }
  | readReference (s : State) (n : Nat) (v : Bool)
      (hf : s.fuel = n + 1) (hr : s.standard = some v) :
      Step s .readReference
        { s with referenceRead := some ⟨s.epoch, referenceSignal s v⟩, fuel := n }
  | judge (s : State) (n : Nat) (target reference : Receipt)
      (hf : s.fuel = n + 1)
      (ht : s.targetRead = some target) (hr : s.referenceRead = some reference)
      (et : target.epoch = s.epoch) (er : reference.epoch = s.epoch) :
      Step s .judge { s with judgment := some ⟨s.epoch, Bool.xor target.bit reference.bit⟩,
        fuel := n }
  | gate (s : State) (e : ExplanatoryVariation.Event) (t : GateState)
      (h : GateStep s.gates e t) :
      Step s (.gate e) { s with gates := t, epoch := s.epoch + 1 }
  | reverseChannel (s : State) :
      Step s .reverseChannel { s with reversed := !s.reversed, epoch := s.epoch + 1 }

def inquiry : Process State Event where
  step := Step

def RecordValid (epoch : Nat) (value : Bool) (record : Option Receipt) : Prop :=
  ∀ r, record = some r → r.epoch ≤ epoch ∧ (r.epoch = epoch → r.bit = value)

def Valid (s : State) : Prop :=
  (s.standard = none ∨ s.standard = some false) ∧
  RecordValid s.epoch (targetSignal s) s.targetRead ∧
  RecordValid s.epoch (referenceSignal s false) s.referenceRead ∧
  RecordValid s.epoch s.gates.leftOpen s.judgment

theorem empty_record_valid (epoch : Nat) (value : Bool) : RecordValid epoch value none := by
  intro r h
  cases h

theorem new_record_valid (epoch : Nat) (value : Bool) :
    RecordValid epoch value (some ⟨epoch, value⟩) := by
  intro r h
  cases h
  exact ⟨Nat.le_refl _, fun _ => rfl⟩

theorem revision_invalidates_old {epoch : Nat} {old new : Bool} {record : Option Receipt}
    (h : RecordValid epoch old record) : RecordValid (epoch + 1) new record := by
  intro r hr
  have hv := h r hr
  constructor
  · exact Nat.le_trans hv.1 (Nat.le_succ epoch)
  · intro he
    have bad : epoch + 1 ≤ epoch := he ▸ hv.1
    exact False.elim (Nat.not_succ_le_self epoch bad)

theorem standard_is_false {s : State} (h : Valid s) {v : Bool}
    (hr : s.standard = some v) : v = false := by
  rcases h.1 with hn | hf
  · have bad := hn.symm.trans hr
    cases bad
  · exact Option.some.inj (hr.symm.trans hf)

theorem inherited_pair_decode (value reversed : Bool) :
    Bool.xor (KC.signal ⟨value, reversed⟩) (KC.reference ⟨value, reversed⟩) = value :=
  Option.some.inj (KC.calibrated_pair_exact ⟨value, reversed⟩ True.intro)

theorem fresh_pair_decodes {s : State} (h : Valid s) {target reference : Receipt}
    (ht : s.targetRead = some target) (hr : s.referenceRead = some reference)
    (et : target.epoch = s.epoch) (er : reference.epoch = s.epoch) :
    Bool.xor target.bit reference.bit = s.gates.leftOpen := by
  have htarget := (h.2.1 target ht).2 et
  have href := (h.2.2.1 reference hr).2 er
  rw [htarget, href]
  exact inherited_pair_decode _ _

theorem valid_step {s t : State} {e : Event}
    (h : Valid s) (hs : inquiry.step s e t) : Valid t := by
  cases hs with
  | prepare s n hf => exact ⟨Or.inr rfl, h.2⟩
  | readTarget s n hf =>
    exact ⟨h.1, new_record_valid _ _, h.2.2⟩
  | readReference s n v hf hr =>
    have hv := standard_is_false h hr
    subst v
    exact ⟨h.1, h.2.1, new_record_valid _ _, h.2.2.2⟩
  | judge s n target reference hf ht hr et er =>
    have he := fresh_pair_decodes h ht hr et er
    refine ⟨h.1, h.2.1, h.2.2.1, ?_⟩
    change RecordValid s.epoch s.gates.leftOpen
      (some ⟨s.epoch, Bool.xor target.bit reference.bit⟩)
    rw [he]
    exact new_record_valid _ _
  | gate s e g hg =>
    exact ⟨h.1, revision_invalidates_old h.2.1,
      revision_invalidates_old h.2.2.1, revision_invalidates_old h.2.2.2⟩
  | reverseChannel s =>
    exact ⟨h.1, revision_invalidates_old h.2.1,
      revision_invalidates_old h.2.2.1, revision_invalidates_old h.2.2.2⟩

theorem valid_trace {s t : State} {word : List Event}
    (h : Valid s) (ht : Trace inquiry s word t) : Valid t := by
  induction ht with
  | nil => exact h
  | cons hs _ ih => exact ih (valid_step h hs)

def initial (g : GateState) (reversed : Bool) (fuel : Nat) : State :=
  ⟨g, reversed, 0, none, none, none, none, fuel⟩

theorem initial_valid (g : GateState) (reversed : Bool) (fuel : Nat) :
    Valid (initial g reversed fuel) :=
  ⟨Or.inl rfl, empty_record_valid _ _, empty_record_valid _ _, empty_record_valid _ _⟩

theorem current_judgment_correct {s : State} (h : Valid s) {r : Receipt}
    (hr : s.judgment = some r) (he : r.epoch = s.epoch) : r.bit = s.gates.leftOpen :=
  (h.2.2.2 r hr).2 he

theorem current_negative_is_evidence {s : State} (h : Valid s)
    (hr : s.judgment = some ⟨s.epoch, false⟩) : s.gates.leftOpen = false :=
  (current_judgment_correct h hr rfl).symm

theorem current_positive_allows_pass {s : State} (h : Valid s)
    (hr : s.judgment = some ⟨s.epoch, true⟩)
    (right : s.gates.rightOpen = true) (notPassed : s.gates.passed = false) :
    Enabled inquiry s (.gate .pass) := by
  have hl := (current_judgment_correct h hr rfl).symm
  cases s with
  | mk g reversed epoch standard target reference judgment fuel =>
    cases g with
    | mk l r c d =>
      change l = true at hl
      change r = true at right
      change d = false at notPassed
      subst l; subst r; subst d
      exact ⟨_, .gate _ .pass ⟨true, true, c, true⟩ (.pass c)⟩

theorem no_reference_before_preparation (g : GateState) (reversed : Bool) (fuel : Nat) :
    ¬ Enabled inquiry (initial g reversed fuel) .readReference := by
  rintro ⟨t, h⟩
  cases h with
  | readReference s n v hf hr => cases hr

theorem no_judgment_without_readings (g : GateState) (reversed : Bool) (fuel : Nat) :
    ¬ Enabled inquiry (initial g reversed fuel) .judge := by
  rintro ⟨t, h⟩
  cases h with
  | judge s n target reference hf ht hr et er => cases ht

def acquisition : List Event := [.prepare, .readReference, .readTarget, .judge]

def acquired (s : State) (remaining : Nat) : State :=
  { s with standard := some false,
    targetRead := some ⟨s.epoch, targetSignal s⟩,
    referenceRead := some ⟨s.epoch, referenceSignal s false⟩,
    judgment := some ⟨s.epoch, s.gates.leftOpen⟩, fuel := remaining }

theorem acquisition_realized (s : State) (n : Nat) (hf : s.fuel = n + 4) :
    Trace inquiry s acquisition (acquired s n) := by
  have decode := inherited_pair_decode s.gates.leftOpen s.reversed
  have hp : inquiry.step s .prepare {s with standard := some false, fuel := n + 3} :=
    .prepare s (n + 3) hf
  apply Trace.cons hp
  apply Trace.cons (Step.readReference _ (n + 2) false rfl rfl)
  apply Trace.cons (Step.readTarget _ (n + 1) rfl)
  have hj := Step.judge
    {s with standard := some false, fuel := n + 1,
      referenceRead := some ⟨s.epoch, referenceSignal s false⟩,
      targetRead := some ⟨s.epoch, targetSignal s⟩}
    n ⟨s.epoch, targetSignal s⟩ ⟨s.epoch, referenceSignal s false⟩ rfl rfl rfl rfl rfl
  change Bool.xor (targetSignal s) (referenceSignal s false) = s.gates.leftOpen at decode
  rw [decode] at hj
  exact Trace.cons hj (.nil _)

theorem acquired_record_exact (s : State) (n : Nat) :
    (acquired s n).judgment = some ⟨s.epoch, s.gates.leftOpen⟩ := rfl

def eventCost : Event → Nat
  | .prepare | .readTarget | .readReference | .judge => 1
  | .gate _ | .reverseChannel => 0

def cost : List Event → Nat
  | [] => 0
  | a :: rest => eventCost a + cost rest

theorem fuel_step {s t : State} {e : Event} (h : inquiry.step s e t) :
    t.fuel + eventCost e = s.fuel := by
  cases h with
  | prepare s n hf => exact hf.symm
  | readTarget s n hf => exact hf.symm
  | readReference s n v hf hr => exact hf.symm
  | judge s n tr rr hf ht hr et er => exact hf.symm
  | gate => exact Nat.add_zero _
  | reverseChannel => exact Nat.add_zero _

theorem fuel_trace {s t : State} {word : List Event} (h : Trace inquiry s word t) :
    t.fuel + cost word = s.fuel := by
  induction h with
  | nil s => exact Nat.add_zero _
  | @cons s m t a rest hs ht ih =>
    have he := fuel_step hs
    change t.fuel + (eventCost a + cost rest) = s.fuel
    calc
      t.fuel + (eventCost a + cost rest) = t.fuel + (cost rest + eventCost a) :=
        congrArg (fun n => t.fuel + n) (Nat.add_comm _ _)
      _ = (t.fuel + cost rest) + eventCost a := (Nat.add_assoc _ _ _).symm
      _ = m.fuel + eventCost a := congrArg (fun n => n + eventCost a) ih
      _ = s.fuel := he

theorem acquisition_requires_four {s t : State} (h : Trace inquiry s acquisition t) :
    4 ≤ s.fuel := by
  have he := fuel_trace h
  change t.fuel + 4 = s.fuel at he
  exact he ▸ Nat.le_add_left 4 t.fuel

theorem insufficient_fuel_blocks_acquisition {s : State} (h : s.fuel < 4) :
    ¬ Feasible inquiry s acquisition := by
  rintro ⟨t, ht⟩
  exact Nat.not_le_of_gt h (acquisition_requires_four ht)

end Generative.ExplanatoryInquiry

#print axioms Generative.KnowledgeCorrespondence.calibrated_pair_exact

#print axioms Generative.ExplanatoryInquiry.empty_record_valid
#print axioms Generative.ExplanatoryInquiry.new_record_valid
#print axioms Generative.ExplanatoryInquiry.revision_invalidates_old
#print axioms Generative.ExplanatoryInquiry.standard_is_false
#print axioms Generative.ExplanatoryInquiry.inherited_pair_decode
#print axioms Generative.ExplanatoryInquiry.fresh_pair_decodes
#print axioms Generative.ExplanatoryInquiry.valid_step
#print axioms Generative.ExplanatoryInquiry.valid_trace
#print axioms Generative.ExplanatoryInquiry.initial_valid
#print axioms Generative.ExplanatoryInquiry.current_judgment_correct
#print axioms Generative.ExplanatoryInquiry.current_negative_is_evidence
#print axioms Generative.ExplanatoryInquiry.current_positive_allows_pass
#print axioms Generative.ExplanatoryInquiry.no_reference_before_preparation
#print axioms Generative.ExplanatoryInquiry.no_judgment_without_readings
#print axioms Generative.ExplanatoryInquiry.acquisition_realized
#print axioms Generative.ExplanatoryInquiry.acquired_record_exact
#print axioms Generative.ExplanatoryInquiry.fuel_step
#print axioms Generative.ExplanatoryInquiry.fuel_trace
#print axioms Generative.ExplanatoryInquiry.acquisition_requires_four
#print axioms Generative.ExplanatoryInquiry.insufficient_fuel_blocks_acquisition
