import RecipientAction
import ActionPreparation

namespace ActionWitness

open RecipientAction
set_option maxRecDepth 16384
set_option maxHeartbeats 4000000

/- Concrete conditional producer boundary already used by identification. The
upstream eight-opportunity distribution is separately preserved numerically;
this proof does not invent a formal stochastic commissioning history. -/
def laws : RecipientCorrection.Laws := (false,true)
def producer := RecipientArchive.producer laws RecipientArchive.PrimaryBacking

deriving instance DecidableEq for EmissionArchive.Phase

inductive ArchiveEvent where
  | core (e : RecipientIdentification.Event)
  | bind (i : Nat) (command : Bool)
  | write

def toOld (s : Archive) : ArchiveEvent → EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header
  | .core e => .core (.core e) (RecipientArchive.advance laws s.world (.core e))
  | .bind i b => .bind i ⟨i,false,b⟩
  | .write => .write

def archiveAdvance (s : Archive) (e : ArchiveEvent) := EmissionArchive.advance producer s (toOld s e)
def archiveEnabled (s : Archive) (e : ArchiveEvent) :=
  EmissionArchive.Valid producer s ∧ EmissionArchive.Enabled producer 3 s (toOld s e)

/- Executable reflection of the unchanged inherited guard, with an equivalence
proof. Avoids proof-transport reductions in the inherited decision instance. -/
def coreCheck (s : RecipientIdentification.State) : RecipientIdentification.Event → Bool
  | .rent => decide (s.active=true ∧ s.phase=.ready ∧ 0<s.packets ∧ 8≤s.hardware.fuel)
  | .sense _ => decide (s.phase=.rented ∧ 1≤s.hardware.fuel)
  | .reserve => match s.phase with
      | .sensed _ => decide (6≤s.hardware.fuel ∧ 0<s.packets)
      | _ => false
  | .work _ => match s.phase with
      | .reserved _ => decide (3≤s.hardware.fuel ∧ 0<s.packets)
      | _ => false
  | .acquire _ => match s.phase with
      | .worked _ _ => decide (1≤s.escrow)
      | _ => false
  | .write => match s.phase with
      | .acquired _ _ => decide (2≤s.escrow)
      | _ => false
  | .miss => decide (s.phase=.ready ∧ 0<s.packets ∧ (s.active=false ∨ s.hardware.fuel<8))

theorem core_check_iff (s : RecipientIdentification.State) (e : RecipientIdentification.Event) :
    coreCheck s e=true ↔ RecipientIdentification.Enabled s e := by
  cases e <;> cases hp : s.phase <;> simp [coreCheck,RecipientIdentification.Enabled,hp]

local instance (priority := 1100) (s : RecipientIdentification.State) (e : RecipientIdentification.Event) :
    Decidable (RecipientIdentification.Enabled s e) := decidable_of_iff (coreCheck s e=true) (core_check_iff s e)

def validCheck (s : Archive) : Bool := match s.phase with
  | .idle => decide (s.escrow=0)
  | .bound i _ => decide (s.records i=none ∧ s.escrow=4)
  | .latched i r bits => decide (s.records i=none ∧ bits.length<4 ∧
      bits=(producer.encode r).take bits.length ∧ s.escrow+bits.length=4)

theorem valid_check_iff (s : Archive) : validCheck s=true ↔ EmissionArchive.Valid producer s := by
  cases hp : s.phase <;> simp [validCheck,EmissionArchive.Valid,hp]

instance (s : Archive) : Decidable (EmissionArchive.Valid producer s) :=
  decidable_of_iff (validCheck s=true) (valid_check_iff s)

def writeCheck (s : Archive) : Bool := match s.phase with
  | .latched _ _ bits => decide (s.world.live=true ∧ bits.length<4 ∧ 0<s.escrow)
  | _ => false

theorem write_check_iff (s : Archive) : writeCheck s=true ↔
    EmissionArchive.Enabled producer 3 s (toOld s .write) := by
  cases hp : s.phase with
  | idle => simp [writeCheck,toOld,EmissionArchive.Enabled,hp]
  | bound i h => simp [writeCheck,toOld,EmissionArchive.Enabled,hp]
  | latched i r bits =>
      simp only [writeCheck,hp,decide_eq_true_eq,toOld,EmissionArchive.Enabled]
      constructor
      · rintro ⟨hl,hb,he⟩
        exact ⟨hl,i,r,bits,rfl,hb,he⟩
      · rintro ⟨hl,j,q,bs,hb,hlen,he⟩
        cases hb
        exact ⟨hl,hlen,he⟩

instance (s : Archive) (e : ArchiveEvent) : Decidable (archiveEnabled s e) := by
  haveI : Decidable (EmissionArchive.Enabled producer 3 s (toOld s e)) := by
    cases e with
    | core e =>
        unfold toOld EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.Step RecipientIdentification.Step
        infer_instance
    | bind i b =>
        unfold toOld EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.binding
        infer_instance
    | write => exact decidable_of_iff (writeCheck s=true) (write_check_iff s)
  unfold archiveEnabled
  infer_instance

def archiveRun (s : Archive) : List ArchiveEvent → Archive
  | [] => s
  | e::es => archiveRun (archiveAdvance s e) es

def oldWord (s : Archive) : List ArchiveEvent → List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)
  | [] => []
  | e::es => toOld s e::oldWord (archiveAdvance s e) es

def ArchiveRunnable (s : Archive) : List ArchiveEvent → Prop
  | [] => True
  | e::es => archiveEnabled s e ∧ ArchiveRunnable (archiveAdvance s e) es

instance archiveRunnableDecidable (s : Archive) (es : List ArchiveEvent) : Decidable (ArchiveRunnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=archiveRunnableDecidable (archiveAdvance s e) es
      inferInstanceAs (Decidable (archiveEnabled s e ∧ ArchiveRunnable (archiveAdvance s e) es))

theorem archive_runnable_trace {s : Archive} {es : List ArchiveEvent} (h : ArchiveRunnable s es) :
    Generative.Trace (EmissionArchive.process producer 3) s (oldWord s es) (archiveRun s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1.1,h.1.2,rfl⟩ (ih h.2)

def recordedTrial (i : Nat) (b : Bool) : List ArchiveEvent :=
  [.core .rent,.core (.sense .recipient),.bind i b,.core .reserve,
   .core (.work true),.core (.acquire true),.core .write,.write,.write,.write,.write]
def actorTrial := (RecipientIdentification.trial .actor true true).map ArchiveEvent.core
def archiveWord := recordedTrial 0 false++actorTrial++recordedTrial 1 true++actorTrial++recordedTrial 2 true

def originalWorld : RecipientArchive.World := ⟨RecipientIdentification.exampleStart 28,false,0,none,true⟩
def archiveStart : Archive := EmissionArchive.empty originalWorld 15 12
def archiveEnd := archiveRun archiveStart archiveWord

theorem genuine_archive_runnable : ArchiveRunnable archiveStart archiveWord := by decide

theorem genuine_archive_trace :
    Generative.Trace (EmissionArchive.process producer 3) archiveStart
      (oldWord archiveStart archiveWord) archiveEnd := archive_runnable_trace genuine_archive_runnable

theorem archive_endpoint :
    archiveEnd.world.core.hardware.fuel=4 ∧ archiveEnd.world.core.patient=20 ∧
    archiveEnd.world.core.packets=0 ∧ archiveEnd.world.next=3 ∧
    archiveEnd.world.core.phase=.ready ∧ archiveEnd.world.core.hardware.last=true ∧
    archiveEnd.records 0=some ⟨false,false,true,false⟩ ∧
    archiveEnd.records 1=some ⟨false,true,true,true⟩ ∧
    archiveEnd.records 2=some ⟨false,true,true,true⟩ := by decide

def observed := PaidArchiveReader.run (PaidArchiveReader.initial archiveEnd archiveEnd.records false 20) PaidArchiveReader.word

def parentReasons := ReasonReplayBridge.final observed 28

theorem actual_parent_two_cycle_trace :
    Generative.Trace (PaidRecipientReasons.process Archive)
      (PaidRecipientReasons.initial observed 28) ReasonReplayBridge.completionWord parentReasons :=
  ReasonReplayBridge.funded_two_cycle_tail observed
    (PaidArchiveReader.paid_reader_complete archiveEnd archiveEnd.records false).1
    (PaidArchiveReader.paid_reader_complete archiveEnd archiveEnd.records false).2.1

def entry : State := ⟨parentReasons,true,0,0,6,24,10,none,none,true,true,true⟩

instance (m : RecipientIdentification.Registers) (z : Bool) : Decidable (RecipientIdentification.Sound m z) := by
  unfold RecipientIdentification.Sound
  infer_instance

instance (s : State) : Decidable (ReadyImport s) := by unfold ReadyImport; infer_instance
instance (s : State) : Decidable (Authorized s) := by unfold Authorized; infer_instance
def settlementCheck (s : State) (e : RecipientIdentification.Event) : Bool :=
  match e,(core s).phase with
  | .acquire _,.worked _ _ | .write,.acquired _ _ => true
  | _,_ => false

theorem settlement_check_iff (s : State) (e : RecipientIdentification.Event) :
    settlementCheck s e=true ↔ Settlement s e := by
  cases e <;> cases hp : (core s).phase <;> simp [settlementCheck,Settlement,hp]

instance (s : State) (e : RecipientIdentification.Event) : Decidable (Settlement s e) :=
  decidable_of_iff (settlementCheck s e=true) (settlement_check_iff s e)
instance (s : PaidRecipientReasons.State Archive) (e : PaidRecipientReasons.Event) :
    Decidable (PaidRecipientReasons.Enabled s e) := by
  cases e with
  | reader e => cases e <;> unfold PaidRecipientReasons.Enabled PaidArchiveReader.Enabled <;> infer_instance
  | _ => unfold PaidRecipientReasons.Enabled PaidArchiveReader.Complete; infer_instance
instance (s : State) (e : RecipientIdentification.Event) : Decidable (RecipientOnly s e) := by
  cases e <;> unfold RecipientOnly <;> infer_instance
instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled <;> infer_instance

def Runnable (s : State) : List Event → Prop
  | [] => True
  | e::es => Enabled s e ∧ Runnable (advance laws s e) es

instance runnableDecidable (s : State) (es : List Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable (advance laws s e) es
      inferInstanceAs (Decidable (Enabled s e ∧ Runnable (advance laws s e) es))

theorem runnable_trace {s : State} {es : List Event} (h : Runnable s es) :
    Generative.Trace (process laws) s es (run laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih h.2)

def bindingWord : List Event := [.fund,.read,.install]
def actionWord := bindingWord++(RecipientIdentification.trial .recipient true true).map Event.execute
def afterAction := run laws entry actionWord
def replayWord : List Event := [.reason .cold,.fundReader]++PaidRecipientReasons.cycle.map Event.reason

def final := run laws afterAction replayWord

theorem actual_entry_accounts :
    (core entry).hardware.fuel=4 ∧ (core entry).patient=20 ∧ (core entry).packets=0 ∧
    entry.reasons.reader.fuel=0 ∧ material entry=32 ∧ energy entry=64 ∧
    PaidRecipientReasons.CurrentPublication entry.reasons ∧ supported entry=some true := by decide

theorem actual_action_runnable : Runnable entry actionWord := by decide

theorem actual_action_trace : Generative.Trace (process laws) entry actionWord afterAction :=
  runnable_trace actual_action_runnable

theorem actual_recipient_effect :
    (core afterAction).patient=30 ∧ (core afterAction).hardware.fuel=0 ∧
    (core afterAction).packets=0 ∧ afterAction.readerReserve=24 ∧
    spent laws entry actionWord=10 ∧ energy afterAction=54 ∧ material afterAction=32 := by decide

theorem actual_later_replay_runnable : Runnable afterAction replayWord := by decide

theorem actual_later_replay_trace : Generative.Trace (process laws) afterAction replayWord final :=
  runnable_trace actual_later_replay_runnable

theorem actual_final_accounts :
    (core final).patient=30 ∧ (core final).hardware.fuel=0 ∧ (core final).packets=0 ∧
    final.reasons.reader.fuel=0 ∧ final.readerReserve=0 ∧ final.sourceReserve=0 ∧
    energy final=30 ∧ material final=32 ∧ spent laws afterAction replayWord=24 ∧
    PaidRecipientReasons.CurrentPublication final.reasons ∧ supported final=some true := by decide

theorem later_replay_has_no_new_archive : final.reasons.reader.archive=entry.reasons.reader.archive := by
  exact (trace_archive_bytes actual_later_replay_trace).trans (trace_archive_bytes actual_action_trace)

def installed := run laws entry bindingWord

theorem binding_is_paid_and_qualified :
    (core installed).hardware.fuel=8 ∧ (core installed).packets=1 ∧
    (core installed).hardware.last=true ∧
    RecipientIdentification.Sound (RecipientIdentification.registers (core installed).hardware) true ∧
    spent laws entry bindingWord=2 := by decide

def shortEntry : State := { entry with commandReserve:=5 }
def shortBound := run laws shortEntry bindingWord

theorem short_import_retains_charge_then_misses :
    Runnable shortEntry bindingWord ∧ (core shortBound).hardware.fuel=7 ∧
    ¬ Enabled shortBound (.execute .rent) ∧ Enabled shortBound (.execute .miss) ∧
    spent laws shortEntry (bindingWord++[.execute .miss])=12 ∧
    (core (advance laws shortBound (.execute .miss))).patient=20 ∧
    (core (advance laws shortBound (.execute .miss))).packets=0 := by decide

def partialEntry : State := { entry with sourceReserve:=9 }
def partialBound := run laws partialEntry bindingWord

theorem partial_packet_does_not_start_opportunity :
    Runnable partialEntry bindingWord ∧ partialBound.sourceReserve=9 ∧
    (core partialBound).packets=0 ∧ (core partialBound).hardware.fuel=8 ∧
    ¬ Enabled partialBound (.execute .rent) ∧ ¬ Enabled partialBound (.execute .miss) ∧
    spent laws partialEntry bindingWord=2 := by decide

def readState := run laws entry [.fund,.read]

theorem same_label_reopening_rejects_old_import_and_use :
    ¬ Enabled (advance laws readState (.reason (.reader (.contextChange false)))) .install ∧
    ¬ Enabled (advance laws installed (.reason (.reader (.contextChange false)))) (.execute .rent) ∧
    (core (advance laws readState (.reason (.reader (.contextChange false))))).hardware.fuel=9 ∧
    (core (advance laws installed (.reason (.reader (.contextChange false))))).hardware.fuel=8 := by decide

def outageWord := bindingWord++(RecipientIdentification.trial .recipient false true).map Event.execute

theorem compatible_command_without_available_source_receipt :
    Runnable entry outageWord ∧ (core (run laws entry outageWord)).patient=20 ∧
    (core (run laws entry outageWord)).hardware.fuel=0 ∧
    (core (run laws entry outageWord)).hardware.last=true ∧
    RecipientCorrection.packedAct (core (run laws entry outageWord)).hardware.q .recipient=true ∧
    spent laws entry outageWord=20 := by decide

/- This is a configured integrity violation, not a claimed genuine publication
history. It demonstrates why CurrentPublication alone cannot prove sound import. -/
def forged : State := { entry with reasons := { entry.reasons with
  working := ⟨true,false⟩, published := some (false,⟨true,false⟩) } }

theorem forged_current_flag_can_import_wrong_command :
    PaidRecipientReasons.CurrentPublication forged.reasons ∧
    Runnable forged actionWord ∧
    ¬ RecipientIdentification.Sound
      (RecipientIdentification.registers (core (run laws forged bindingWord)).hardware) true ∧
    (core (run laws forged actionWord)).patient=20 ∧ spent laws forged actionWord=20 := by decide

/- Genuine earlier factual-cache boundary: both instrumental reason cycles are
skipped, so the six reader units and original reserve28 remain unspent. -/
def unaudited : State := { entry with reasons:=PaidRecipientReasons.initial observed 28 }
def voluntaryWord : List Event := [.fund]++(RecipientIdentification.trial .recipient true true).map Event.voluntary

theorem unaudited_voluntary_alternative :
    ¬ PaidRecipientReasons.CurrentPublication unaudited.reasons ∧
    Runnable unaudited voluntaryWord ∧
    (core (run laws unaudited voluntaryWord)).patient=30 ∧
    (core (run laws unaudited voluntaryWord)).hardware.fuel=2 ∧
    (run laws unaudited voluntaryWord).reasons.reader.fuel=6 ∧
    (run laws unaudited voluntaryWord).reasons.reserve=28 ∧
    spent laws unaudited voluntaryWord=8 ∧ energy (run laws unaudited voluntaryWord)=90 := by decide

theorem voluntary_start_does_not_require_command_port :
    Enabled { advance laws unaudited .fund with port:=false } (.voluntary .rent) ∧
    ¬ Enabled { advance laws unaudited .fund with port:=false } .read := by decide

def rented := advance laws installed (.execute .rent)
def cutRented := advance laws rented (.setScope false)

theorem before_work_cut_keeps_sunk_bill_and_packet :
    (core cutRented).phase=.rented ∧ (core cutRented).hardware.fuel=7 ∧
    (core cutRented).packets=1 ∧ ¬ Enabled cutRented (.execute (.sense .recipient)) := by decide

def throughWork : List Event := [.execute .rent,.execute (.sense .recipient),.execute .reserve,.execute (.work true)]
def cutWorked := advance laws (run laws installed throughWork) (.setScope false)
def settlementWord : List Event := [.execute (.acquire true),.execute .write]

theorem after_work_cut_settles_without_undoing_receipt :
    Runnable installed throughWork ∧ (core cutWorked).patient=30 ∧
    (core cutWorked).packets=0 ∧ (core cutWorked).escrow=3 ∧
    Runnable cutWorked settlementWord ∧
    (core (run laws cutWorked settlementWord)).patient=30 ∧
    (core (run laws cutWorked settlementWord)).phase=.ready ∧
    (core (run laws cutWorked settlementWord)).escrow=0 ∧
    spent laws cutWorked settlementWord=3 := by decide

def changedReplayWord : List Event := [.reason .cold,.reason (.reader (.contextChange true)),.fundReader]++
  PaidRecipientReasons.cycle.map Event.reason

theorem later_changed_context_pays_and_loses_available_ground :
    Runnable afterAction changedReplayWord ∧
    PaidRecipientReasons.CurrentPublication (run laws afterAction changedReplayWord).reasons ∧
    supported (run laws afterAction changedReplayWord)=none ∧
    (core (run laws afterAction changedReplayWord)).patient=30 ∧
    spent laws afterAction changedReplayWord=24 := by decide

theorem genuine_reason_and_actual_recipient_credit {G : Prop} (root : G) :
    RecipientReasons.Meaning G true .q ∧ (core afterAction).patient=30 := by
  constructor
  · exact ReasonReplayBridge.actual_archive_to_cold_replayed_reasons
      (laws:=laws) (by decide) genuine_archive_trace false root (by change parentReasons.working.q=true; decide)
  · exact actual_recipient_effect.1

end ActionWitness

#print axioms ActionWitness.core_check_iff
#print axioms ActionWitness.valid_check_iff
#print axioms ActionWitness.write_check_iff
#print axioms ActionWitness.archive_runnable_trace
#print axioms ActionWitness.genuine_archive_runnable
#print axioms ActionWitness.genuine_archive_trace
#print axioms ActionWitness.archive_endpoint
#print axioms ActionWitness.actual_parent_two_cycle_trace
#print axioms ActionWitness.settlement_check_iff
#print axioms ActionWitness.runnable_trace
#print axioms ActionWitness.actual_entry_accounts
#print axioms ActionWitness.actual_action_runnable
#print axioms ActionWitness.actual_action_trace
#print axioms ActionWitness.actual_recipient_effect
#print axioms ActionWitness.actual_later_replay_runnable
#print axioms ActionWitness.actual_later_replay_trace
#print axioms ActionWitness.actual_final_accounts
#print axioms ActionWitness.later_replay_has_no_new_archive
#print axioms ActionWitness.binding_is_paid_and_qualified
#print axioms ActionWitness.short_import_retains_charge_then_misses
#print axioms ActionWitness.partial_packet_does_not_start_opportunity
#print axioms ActionWitness.same_label_reopening_rejects_old_import_and_use
#print axioms ActionWitness.compatible_command_without_available_source_receipt
#print axioms ActionWitness.forged_current_flag_can_import_wrong_command
#print axioms ActionWitness.unaudited_voluntary_alternative
#print axioms ActionWitness.voluntary_start_does_not_require_command_port
#print axioms ActionWitness.before_work_cut_keeps_sunk_bill_and_packet
#print axioms ActionWitness.after_work_cut_settles_without_undoing_receipt
#print axioms ActionWitness.later_changed_context_pays_and_loses_available_ground
#print axioms ActionWitness.genuine_reason_and_actual_recipient_credit
