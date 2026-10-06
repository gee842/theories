import FreshRevision

namespace RevisionWitness
open FreshRevision
open RecipientCorrection (Laws packedAct)

set_option maxRecDepth 16384
set_option maxHeartbeats 4000000

/- The accepted conditional action endpoint is retained exactly. The new
reserves were partitioned at the prospective M42 preparation; no recipient
stock is transferred. The full stochastic old commissioning remains a
separately checked finite model, as in ActionWitness. -/
def entry : State :=
  ⟨ActionWitness.final,⟨5,0,4,fun _=>none,.idle,0,none,false⟩,
   true,4,0,0,28,24,30,false,false⟩
def start := opening (fund entry)
def changed : Laws := (false,false)

inductive Command where
  | core (event : RecipientIdentification.Event)
  | bind
  | write
  deriving DecidableEq

def toOld (laws : Laws) (s : State) : Command →
    EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header
  | .core e => .core (.core e) (RecipientArchive.advance laws (view s).world (.core e))
  | .bind => .bind 1 ⟨1,true,packedAct (core s).hardware.q .recipient⟩
  | .write => .write

def advance (laws : Laws) (s : State) (e : Command) := bankAdvance laws s (toOld laws s e)
def Enabled (laws : Laws) (s : State) (e : Command) : Prop :=
  s.opened=true ∧ s.reading=false ∧ BankGuard s (toOld laws s e) ∧
  EmissionArchive.Valid (producer laws) (view s) ∧
  EmissionArchive.Enabled (producer laws) 3 (view s) (toOld laws s e)

local instance (priority := 1100) (s : RecipientIdentification.State) (e : RecipientIdentification.Event) :
    Decidable (RecipientIdentification.Enabled s e) :=
  decidable_of_iff (ActionWitness.coreCheck s e=true) (ActionWitness.core_check_iff s e)

def validCheck (laws : Laws) (s : RecipientAction.Archive) : Bool := match s.phase with
  | .idle => decide (s.escrow=0)
  | .bound i _ => decide (s.records i=none ∧ s.escrow=4)
  | .latched i r bits => decide (s.records i=none ∧ bits.length<4 ∧
      bits=((producer laws).encode r).take bits.length ∧ s.escrow+bits.length=4)

theorem valid_check_iff (laws : Laws) (s : RecipientAction.Archive) :
    validCheck laws s=true ↔ EmissionArchive.Valid (producer laws) s := by
  cases hp:s.phase <;> simp [validCheck,EmissionArchive.Valid,hp]

instance (laws : Laws) (s : RecipientAction.Archive) :
    Decidable (EmissionArchive.Valid (producer laws) s) :=
  decidable_of_iff (validCheck laws s=true) (valid_check_iff laws s)

def writeCheck (s : State) : Bool := match s.bank.phase with
  | .latched _ _ bits => decide (s.bank.live=true ∧ bits.length<4 ∧ 0<s.bank.escrow)
  | _ => false

theorem write_check_iff (laws : Laws) (s : State) : writeCheck s=true ↔
    EmissionArchive.Enabled (producer laws) 3 (view s) (toOld laws s .write) := by
  cases hp:s.bank.phase with
  | idle => simp [writeCheck,toOld,EmissionArchive.Enabled,view,hp]
  | bound i h => simp [writeCheck,toOld,EmissionArchive.Enabled,view,hp]
  | latched i r bits =>
      simp only [writeCheck,hp,decide_eq_true_eq,toOld,EmissionArchive.Enabled,view]
      constructor
      · rintro ⟨hl,hb,he⟩
        exact ⟨hl,i,r,bits,rfl,hb,he⟩
      · rintro ⟨hl,j,q,bs,hb,hlen,he⟩
        cases hb
        exact ⟨hl,hlen,he⟩

instance (laws : Laws) (s : State) (e : Command) : Decidable (Enabled laws s e) := by
  haveI : Decidable (BankGuard s (toOld laws s e)) := by
    cases e with
    | core e => unfold BankGuard toOld; infer_instance
    | bind => unfold BankGuard toOld; infer_instance
    | write => exact isTrue trivial
  haveI : Decidable (EmissionArchive.Enabled (producer laws) 3 (view s) (toOld laws s e)) := by
    cases e with
    | core e =>
        unfold toOld EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.Step RecipientIdentification.Step
        infer_instance
    | bind => unfold toOld EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.binding; infer_instance
    | write => exact decidable_of_iff (writeCheck s=true) (write_check_iff laws s)
  unfold Enabled
  infer_instance

def run (laws : Laws) (s : State) : List Command → State
  | [] => s
  | e::es => run laws (advance laws s e) es

def word (laws : Laws) (s : State) : List Command →
    List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)
  | [] => []
  | e::es => toOld laws s e::word laws (advance laws s e) es

def Runnable (laws : Laws) (s : State) : List Command → Prop
  | [] => True
  | e::es => Enabled laws s e ∧ Runnable laws (advance laws s e) es

instance runnableDecidable (laws : Laws) (s : State) (es : List Command) : Decidable (Runnable laws s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable laws (advance laws s e) es
      inferInstanceAs (Decidable (Enabled laws s e ∧ Runnable laws (advance laws s e) es))

theorem runnable_trace {laws : Laws} {s : State} {es : List Command}
    (h : Runnable laws s es) : Generative.Trace (bankProcess laws) s (word laws s es) (run laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih =>
      exact .cons ⟨h.1.1,h.1.2.1,h.1.2.2.1,⟨h.1.2.2.2.1,h.1.2.2.2.2,rfl⟩,rfl⟩ (ih h.2)

def trial (available channel : Bool) :=
  (RecipientIdentification.trial .recipient available channel).map Command.core

def recordedTrial (available channel : Bool) : List Command :=
  [.core .rent,.core (.sense .recipient),.bind,.core .reserve,
   .core (.work available),.core (.acquire channel),.core .write,.write,.write,.write,.write]

def queryWord := trial true true++recordedTrial true true

def bankEnd := run changed start queryWord

def reading := prepareConsumer bankEnd

def actionRun (laws : Laws) (s : State) : List RecipientAction.Event → State
  | []=>s
  | e::es=>actionRun laws (actionAdvance laws s e) es

def ActionRunnable (laws : Laws) (s : State) : List RecipientAction.Event → Prop
  | [] => True
  | e::es => s.opened=true ∧ s.reading=true ∧ RecipientAction.Enabled s.parent e ∧
      ActionRunnable laws (actionAdvance laws s e) es

instance actionRunnableDecidable (laws : Laws) (s : State) (es : List RecipientAction.Event) :
    Decidable (ActionRunnable laws s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=actionRunnableDecidable laws (actionAdvance laws s e) es
      inferInstanceAs (Decidable (s.opened=true ∧ s.reading=true ∧ RecipientAction.Enabled s.parent e ∧
        ActionRunnable laws (actionAdvance laws s e) es))

theorem action_runnable_trace {laws : Laws} {s : State} {es : List RecipientAction.Event}
    (h : ActionRunnable laws s es) :
    Generative.Trace (actionProcess laws) s es (actionRun laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1,h.2.1,⟨h.2.2.1,rfl⟩,rfl⟩ (ih h.2.2.2)

def consumerWord := PaidRecipientReasons.cycle.map RecipientAction.Event.reason

def consumed := actionRun changed reading consumerWord

def useWord : List RecipientAction.Event := [.read,.install]++
  (RecipientIdentification.trial .recipient true true).map RecipientAction.Event.execute

def final := actionRun changed consumed useWord

theorem actual_original_boundary : entry.parent=ActionWitness.final ∧
    (core entry).hardware.fuel=0 ∧ (core entry).patient=30 ∧
    energy entry=117 ∧ material entry=42 := by
  constructor
  · rfl
  · decide

theorem funded_reset_enabled : Openable (fund entry) := by unfold Openable; decide

theorem actual_reset_boundary : (core start).hardware.q=(core entry).hardware.q ∧
    (core start).hardware.last=false ∧ (core start).hardware.fuel=26 ∧
    (core start).packets=3 ∧ (core start).patient=30 ∧
    energy start=115 ∧ material start=42 ∧
    start.parent.reasons.reader.world.world.next=3 ∧ (view start).world.next=0 ∧
    start.parent.reasons.current=false := by decide

theorem actual_queries_runnable : Runnable changed start queryWord := by decide

theorem actual_queries_trace :
    Generative.Trace (bankProcess changed) start (word changed start queryWord) bankEnd :=
  runnable_trace actual_queries_runnable

theorem actual_new_acquisition : bankEnd.bank.records 0=none ∧
    bankEnd.bank.records 1=some ⟨true,false,true,true⟩ ∧ bankEnd.bank.records 2=none ∧
    bankEnd.bank.next=2 ∧ bankEnd.bank.budget=0 ∧ bankEnd.bank.escrow=0 ∧ bankEnd.bank.blanks=0 ∧
    (core bankEnd).hardware.fuel=10 ∧ (core bankEnd).patient=40 ∧
    (core bankEnd).packets=1 ∧ (core bankEnd).hardware.last=true ∧
    packedAct (core bankEnd).hardware.q .recipient=false ∧
    energy bankEnd=84 ∧ material bankEnd=42 := by decide

theorem old_backing_unchanged :
    bankEnd.parent.reasons.reader.world.records=entry.parent.reasons.reader.world.records ∧
    bankEnd.parent.reasons.reader.world.world.next=3 ∧
    bankEnd.parent.reasons.reader.world.world.context=false := by
  have h:=bank_trace_keeps_old_backing actual_queries_trace
  exact ⟨h.1,by rw [h.2.1]; decide,by rw [h.2.2]; decide⟩

theorem actual_consumer_runnable : ActionRunnable changed reading consumerWord := by decide

theorem actual_consumer_trace : Generative.Trace (actionProcess changed) reading consumerWord consumed :=
  action_runnable_trace actual_consumer_runnable

theorem actual_reason_revision : PaidRecipientReasons.CurrentPublication consumed.parent.reasons ∧
    RecipientAction.supported consumed.parent=some false ∧
    consumed.parent.reasons.reader.fuel=0 ∧ consumed.readerReserve=0 ∧
    energy consumed=60 ∧ material consumed=42 := by decide

theorem actual_use_runnable : ActionRunnable changed consumed useWord := by decide

theorem actual_use_trace : Generative.Trace (actionProcess changed) consumed useWord final :=
  action_runnable_trace actual_use_runnable

theorem actual_same_recipient_effect : (core final).patient=50 ∧
    (core final).hardware.fuel=0 ∧ (core final).packets=0 ∧
    packedAct (core final).hardware.q .recipient=false ∧
    packedAct (core final).hardware.q .actor=packedAct (core entry).hardware.q .actor ∧
    energy final=50 ∧ material final=42 ∧
    RecipientAction.spent changed consumed.parent useWord=10 := by decide


theorem paid_consumer_same_hardware :
    Generative.Trace (PaidRecipientReasons.process RecipientAction.Archive)
      reading.parent.reasons PaidRecipientReasons.cycle consumed.parent.reasons := by
  change Generative.Trace _ reading.parent.reasons _
    (PaidRecipientReasons.run reading.parent.reasons PaidRecipientReasons.cycle)
  exact ReasonReplayBridge.funded_cycle_trace _ (by decide) (by decide)

theorem actual_warranted_revision {G : Prop} (root : G) :
    PublicationBridge.Assured false G consumed.parent.reasons := by
  exact actual_fresh_archive_every_consumer (s:=start) (t:=bankEnd)
    (w:=(view start).world) (budget:=5) (cells:=4) rfl (by decide)
    actual_queries_trace (by decide) root paid_consumer_same_hardware

theorem genuine_revision_and_effect {G : Prop} (root : G) :
    G ∧ (core final).patient=50 ∧
    RecipientReasons.Meaning G false .p := by
  have assured:=actual_warranted_revision root
  have current:=actual_reason_revision.1.1
  have meaning:=(assured.2.2 current).2.2 .p (by change consumed.parent.reasons.working.p=true; decide)
  exact ⟨root,actual_same_recipient_effect.1,meaning⟩

theorem exact_new_service_and_loss_account :
    EmissionArchive.spentAlong (producer changed) (view start) (word changed start queryWord)=31 ∧
    PaidRecipientReasons.spent PaidRecipientReasons.cycle=24 ∧
    RecipientAction.spent changed consumed.parent useWord=10 ∧
    energy entry=2+31+24+10+energy final ∧ 2+16+5+24+2+8=57 := by decide

/- Controlled omission of qualification reset after the same paid opening. -/
def lockedStart := { core start with hardware:={ (core start).hardware with last:=true } }
def lockedCore := RecipientIdentification.run changed lockedStart
  (RecipientIdentification.trial .recipient true true++RecipientIdentification.trial .recipient true true)

theorem old_qualification_does_not_revise_under_zeros :
    packedAct lockedCore.hardware.q .recipient=true ∧ lockedCore.hardware.last=true ∧
    lockedCore.patient=30 ∧ lockedCore.hardware.fuel=10 ∧ lockedCore.packets=1 := by decide

def late := actionRun ActionWitness.laws consumed useWord

theorem hidden_late_change_is_not_detected_by_epoch :
    ActionRunnable ActionWitness.laws consumed useWord ∧
    RecipientAction.supported consumed.parent=some false ∧
    (core late).patient=40 ∧ (core late).hardware.fuel=0 ∧ (core late).packets=0 ∧
    (core late).hardware.last=true ∧ energy late=40 ∧
    RecipientAction.spent ActionWitness.laws consumed.parent useWord=20 := by decide

def zeroBank := run changed start (trial true true++recordedTrial false true)
def zeroRead := prepareConsumer zeroBank
def zeroConsumed := actionRun changed zeroRead consumerWord

theorem new_zero_does_not_refute_or_support :
    Runnable changed start (trial true true++recordedTrial false true) ∧
    zeroBank.bank.records 1=some ⟨true,false,true,false⟩ ∧
    ActionRunnable changed zeroRead consumerWord ∧
    PaidRecipientReasons.CurrentPublication zeroConsumed.parent.reasons ∧
    RecipientAction.supported zeroConsumed.parent=none ∧
    ¬RecipientAction.Enabled (RecipientAction.advance changed zeroConsumed.parent .read) .install := by decide

theorem bounded_window_no_third_query :
    Enabled changed bankEnd (.core .rent) ∧
    RecipientIdentification.Enabled (core (advance changed bankEnd (.core .rent))) (.sense .recipient) ∧
    ¬Enabled changed (advance changed bankEnd (.core .rent)) (.core (.sense .recipient)) ∧
    (core (advance changed bankEnd (.core .rent))).hardware.fuel=9 := by decide

theorem old_archive_cannot_supply_current_facts :
    entry.parent.reasons.reader.world.records 1=some ⟨false,true,true,true⟩ ∧
    bankEnd.bank.records 1=some ⟨true,false,true,true⟩ ∧
    ¬PaidArchiveReader.Facts false (PaidArchiveReader.initial ()
      entry.parent.reasons.reader.world.records true 24) := by
  refine ⟨by decide,by decide,?_⟩
  intro hf
  have bad:=hf 1 ⟨false,true,true,true⟩ (by decide) rfl rfl
  cases bad


theorem actual_composed_history : OpenStep entry start ∧
    Generative.Trace (bankProcess changed) start (word changed start queryWord) bankEnd ∧
    PrepareStep bankEnd reading ∧
    Generative.Trace (actionProcess changed) reading consumerWord consumed ∧
    Generative.Trace (actionProcess changed) consumed useWord final :=
  ⟨⟨funded_reset_enabled,rfl⟩,actual_queries_trace,⟨by decide,by decide,rfl⟩,
    actual_consumer_trace,actual_use_trace⟩

end RevisionWitness

#print axioms RevisionWitness.valid_check_iff
#print axioms RevisionWitness.write_check_iff
#print axioms RevisionWitness.runnable_trace
#print axioms RevisionWitness.action_runnable_trace
#print axioms RevisionWitness.actual_original_boundary
#print axioms RevisionWitness.funded_reset_enabled
#print axioms RevisionWitness.actual_reset_boundary
#print axioms RevisionWitness.actual_queries_runnable
#print axioms RevisionWitness.actual_queries_trace
#print axioms RevisionWitness.actual_new_acquisition
#print axioms RevisionWitness.old_backing_unchanged
#print axioms RevisionWitness.actual_consumer_runnable
#print axioms RevisionWitness.actual_consumer_trace
#print axioms RevisionWitness.actual_reason_revision
#print axioms RevisionWitness.actual_use_runnable
#print axioms RevisionWitness.actual_use_trace
#print axioms RevisionWitness.actual_same_recipient_effect
#print axioms RevisionWitness.paid_consumer_same_hardware
#print axioms RevisionWitness.actual_warranted_revision
#print axioms RevisionWitness.genuine_revision_and_effect
#print axioms RevisionWitness.exact_new_service_and_loss_account
#print axioms RevisionWitness.old_qualification_does_not_revise_under_zeros
#print axioms RevisionWitness.hidden_late_change_is_not_detected_by_epoch
#print axioms RevisionWitness.new_zero_does_not_refute_or_support
#print axioms RevisionWitness.bounded_window_no_third_query
#print axioms RevisionWitness.old_archive_cannot_supply_current_facts
#print axioms RevisionWitness.actual_composed_history
