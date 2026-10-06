import EvaluationWitness
import SuccessionPreparation

namespace EvaluativeSuccession

set_option maxRecDepth 16384
set_option maxHeartbeats 4000000

abbrev Records := Nat → Option RecipientArchive.Frame
abbrev Reasons := PaidRecipientReasons.State Unit

def readerUnit (r : PaidRecipientReasons.State W) : Reasons :=
  { r with reader := { r.reader with world := () } }

/-- Transaction completion deliberately does not compare token to current context. -/
def QuietReader (r : PaidRecipientReasons.State W) : Prop :=
  (r.reader.active=false ∧ r.reader.token=none ∧ r.reader.next=0 ∧ r.phase=0 ∧
    r.normalized=RecipientReasons.empty ∧ r.conflict=false ∧
    r.working=ReasonReplay.emptyMask ∧ r.published=none ∧ r.current=false) ∨
  (r.reader.active=true ∧ r.reader.token.isSome=true ∧ r.reader.next=3 ∧
    r.phase=9 ∧ r.published.isSome=true)

instance (r : PaidRecipientReasons.State W) : Decidable (QuietReader r) := by unfold QuietReader; infer_instance

def Admissible (s : AcquiredEvaluation.State) : Prop :=
  (AcquiredEvaluation.core s).phase=.ready ∧ (AcquiredEvaluation.core s).active=true ∧ (AcquiredEvaluation.core s).hardware.q<4 ∧
  (AcquiredEvaluation.core s).escrow=0 ∧ s.count=3 ∧ s.mode=.closed ∧ s.cells=6 ∧ s.adapter=true ∧
  s.opportunity=.finished ∧ (s.port=false ∨ s.portMode=.consumed) ∧
  s.parent.parent.scope=true ∧ s.parent.parent.latch=none ∧ s.parent.parent.imported=none ∧
  s.parent.bank.phase=.idle ∧ s.parent.bank.escrow=0 ∧
  s.parent.parent.reasons.reader.world.phase=.idle ∧
  s.parent.parent.reasons.reader.world.escrow=0 ∧ QuietReader s.parent.parent.reasons

instance (s : AcquiredEvaluation.State) : Decidable (Admissible s) := by unfold Admissible; infer_instance

structure Historical where
  hardware : RecipientIdentification.Boundary
  records0 : Records
  records1 : Records
  next0 : Nat
  next1 : Nat
  context0 : Bool
  current0 : Option Nat
  current1 : Option Nat
  live0 : Bool
  live1 : Bool
  opened : Bool
  reading : Bool
  retiredPorts : Nat
  oldPort : Bool

structure Native where
  n : Nat
  count : Nat
  cells : Nat
  closed : Bool
  source0 : Nat
  source1 : Nat
  source2 : Nat

def Native.energy (n : Native) := n.source0+n.source1+n.source2

inductive Life where | donor | quiesced | committed | bound | child
  deriving DecidableEq, Repr
inductive Port where | idle | read | help | abstain | executing | consumed
  deriving DecidableEq, Repr
inductive Route where | shared | filtered | conventional
  deriving DecidableEq, Repr

structure State where
  core : RecipientIdentification.State
  reader : Reasons
  bank : FreshRevision.Bank
  history : Historical
  native : Native
  commonCustody : List Nat
  sourceCustody : List Nat
  assembly : Nat
  copyFund : Nat
  operationFund : Nat
  writerFund : Nat
  readerFund : Nat
  sourceFund : Nat
  inaccessibleCommon : Nat
  inaccessibleSource : Nat
  held : Nat
  installed : Nat
  cursor : Nat
  eligible : Bool
  life : Life
  copyLatch : Option Nat
  window : Bool
  nAccess : Bool
  scope : Bool
  permission : Bool
  delivery : Bool
  released : Bool
  attempts : Nat
  probing : Bool
  reading : Bool
  port : Port
  closed : Bool
  route : Route

def oldCommon (s : AcquiredEvaluation.State) : List Nat :=
  [s.parent.parent.reasons.reader.world.budget,s.parent.parent.reasons.reader.world.escrow, s.parent.parent.commandReserve,s.parent.parent.readerReserve, s.parent.bank.budget,s.parent.bank.escrow,s.parent.actorReserve,s.parent.readerReserve, s.training,s.later]
def oldSource (s : AcquiredEvaluation.State) : List Nat :=
  [s.parent.parent.sourceReserve,s.parent.sourceReserve,s.laterSource]

def enter (s : AcquiredEvaluation.State) (route : Route) : State :=
  { core:=AcquiredEvaluation.core s, reader:=readerUnit s.parent.parent.reasons, bank:=⟨0,0,4,fun _=>none,.idle,0,none,false⟩, history:=⟨(AcquiredEvaluation.core s).hardware,s.parent.parent.reasons.reader.world.records, s.parent.bank.records,s.parent.parent.reasons.reader.world.world.next,s.parent.bank.next, s.parent.parent.reasons.reader.world.world.context, s.parent.parent.reasons.reader.world.world.current,s.parent.bank.current, s.parent.parent.reasons.reader.world.world.live,s.parent.bank.live, s.parent.opened,s.parent.reading,s.retired,s.port⟩, native:=⟨s.n,s.count,s.cells,s.mode==.closed,s.source0,s.source1,s.source2⟩, commonCustody:=oldCommon s, sourceCustody:=oldSource s, assembly:=9,copyFund:=2,operationFund:=26,writerFund:=5,readerFund:=24,sourceFund:=30, inaccessibleCommon:=0,inaccessibleSource:=0,held:=9,installed:=0,cursor:=0, eligible:=decide (Admissible s),life:=.donor,copyLatch:=none,window:=false,nAccess:=false, scope:=s.parent.parent.scope,permission:=s.parent.parent.permission,delivery:=s.parent.parent.delivery, released:=false,attempts:=0,probing:=false,reading:=false,port:=.idle,closed:=false,route:=route }

def energy (s : State) := RecipientIdentification.energy s.core+PaidRecipientReasons.energy s.reader+s.bank.budget+s.bank.escrow+
  s.native.energy+s.commonCustody.sum+s.sourceCustody.sum+s.assembly+s.copyFund+
  s.operationFund+s.writerFund+s.readerFund+s.sourceFund+s.inaccessibleCommon+s.inaccessibleSource

def material (s : State) := 60+2*s.held+2*s.installed

def archive (s : State) : RecipientAction.Archive :=
  ⟨⟨s.core,true,s.bank.next,s.bank.current,s.bank.live⟩, s.bank.budget,s.bank.escrow,s.bank.blanks,s.bank.records,s.bank.phase⟩
def setArchive (s : State) (a : RecipientAction.Archive) : State :=
  {s with core:=a.world.core,bank:=⟨a.budget,a.escrow,a.blanks,a.records,a.phase, a.world.next,a.world.current,a.world.live⟩}
def producer (laws : RecipientCorrection.Laws) := RecipientArchive.producer laws (fun i=>i=1)

def Current (s : State) := s.life=.child ∧ s.reading=true ∧ PaidRecipientReasons.CurrentPublication s.reader
instance (s : State) : Decidable (Current s) := by
  unfold Current PaidRecipientReasons.CurrentPublication PaidArchiveReader.Complete; infer_instance

def command (s : State) : Option Bool :=
  if Current s ∧ s.scope=true then RecipientAction.route s.reader.working else none

def Known (s : State) : Prop := s.nAccess=true ∧ s.native.count=3 ∧ s.native.closed=true ∧
  s.native.cells=6 ∧ command s=some (RecipientCorrection.packedAct s.core.hardware.q .recipient)
instance (s : State) : Decidable (Known s) := by unfold Known; infer_instance

def gates (s : State) : Prop := s.scope=true ∧ s.permission=true ∧ s.delivery=true
instance (s : State) : Decidable (gates s) := by unfold gates; infer_instance

def Settlement (s : State) (e : RecipientIdentification.Event) : Prop :=
  match e,s.core.phase with
  | .acquire _,.worked _ _ | .write,.acquired _ _ => True
  | _,_ => False

def RecipientOnly (s : State) : RecipientIdentification.Event → Prop
  | .sense t => t=.recipient
  | .reserve | .work _ | .acquire _ | .write => RecipientIdentification.targetOf s.core.phase=.recipient
  | _ => True

def canProbe (s : State) : Prop := s.life=.child ∧ s.released=true ∧ gates s ∧
  s.core.phase=.ready ∧ s.bank.next<2 ∧ 0<s.core.packets ∧ s.reading=false
instance (s : State) : Decidable (canProbe s) := by unfold canProbe; infer_instance

def bankGuard (s : State) : PublicationBridge.ArchiveEvent → Prop
  | .bind i _ => i=1 ∧ s.cursor=8 ∧ s.window=true
  | .write => True
  | .core (.contextChange _) _ => False
  | .core (.core e) _ => RecipientOnly s e ∧ (Settlement s e ∨ gates s) ∧
      (e=.sense .recipient → s.bank.next<2)

def help (s : State) : Bool := match s.route with
  | .shared => 64<10*s.native.n
  | .filtered => false
  | .conventional => s.native.n=7

def cut (p : Port) : Port := match p with
  | .read | .help | .abstain => .consumed
  | _ => p

inductive Event where
  | assemble | omitWindow | copyRead | copyWrite (qualified scope permission delivery : Bool)
  | bindAccess (connected : Bool) | release | probeStart | probeEnd
  | bank (event : PublicationBridge.ArchiveEvent)
  | prepare | reason (event : PaidRecipientReasons.Event) | read | assess | attempt | abstain
  | trial (event : RecipientIdentification.Event)
  | scope (value : Bool) | permission (value : Bool) | delivery (value : Bool) | access (value : Bool)

/-- Physical scope/permission grants are supplied arguments, not ethical conclusions. -/
def advance (laws : RecipientCorrection.Laws) (s : State) : Event → State
  | .assemble => {s with assembly:=s.assembly-1,held:=s.held-1,installed:=s.installed+1, cursor:=s.cursor+1,window:=s.window || s.cursor==6}
  | .omitWindow => {s with cursor:=s.cursor+1,assembly:=s.assembly-1, inaccessibleCommon:=s.inaccessibleCommon+1}
  | .copyRead => {s with copyFund:=s.copyFund-1,copyLatch:=some s.core.hardware.q,life:=.quiesced}
  | .copyWrite q sc pm dl =>
      {s with core:={s.core with hardware:={s.core.hardware with fuel:=0,q:=s.copyLatch.getD 0,last:=q}, packets:=0,escrow:=0,phase:=.ready,active:=true}, reader:={s.reader with reader:={s.reader.reader with fuel:=0},reserve:=0}, commonCustody:=s.commonCustody++[s.core.hardware.fuel,s.reader.reader.fuel,s.reader.reserve], sourceCustody:=s.sourceCustody++[10*s.core.packets], copyFund:=s.copyFund-1,copyLatch:=none,life:=.committed, scope:=s.scope && sc,permission:=s.permission && pm,delivery:=s.delivery && dl}
  | .bindAccess connected => {s with assembly:=s.assembly-1,held:=s.held-1, installed:=s.installed+1,reader:=PaidRecipientReasons.advance s.reader .cold,life:=.bound,nAccess:=connected}
  | .release => {s with core:={s.core with hardware:={s.core.hardware with fuel:=s.core.hardware.fuel+s.operationFund}, packets:=s.core.packets+s.sourceFund/10},operationFund:=0,sourceFund:=s.sourceFund%10, bank:={s.bank with budget:=s.bank.budget+s.writerFund,live:=true},writerFund:=0,released:=true,life:=.child}
  | .probeStart => {s with attempts:=s.attempts+1,probing:=decide (canProbe s)}
  | .probeEnd => {s with probing:=false}
  | .bank e => setArchive s (EmissionArchive.advance (producer laws) (archive s) e)
  | .prepare => {s with reading:=true,reader:=PaidRecipientReasons.initial (PaidArchiveReader.initial () s.bank.records true (s.reader.reader.fuel+s.readerFund)) 0, readerFund:=0}
  | .reason e => {s with reader:=PaidRecipientReasons.advance s.reader e,port:=cut s.port}
  | .read => {s with core:={s.core with hardware:={s.core.hardware with fuel:=s.core.hardware.fuel-1}}, port:=if Known s then .read else .consumed,closed:=if Known s then s.closed else true}
  | .assess => {s with core:={s.core with hardware:={s.core.hardware with fuel:=s.core.hardware.fuel-1}}, port:=if help s then .help else .abstain}
  | .attempt =>
      if Known s ∧ gates s ∧ s.core.phase=.ready ∧ 0<s.core.packets then {s with port:=.executing}
      else {s with port:=.consumed,closed:=true}
  | .abstain => {s with port:=.consumed,closed:=true}
  | .trial e => {s with core:=RecipientIdentification.advance laws s.core e, port:=if e=.write ∨ e=.miss then .consumed else s.port, closed:=if e=.write ∨ e=.miss then true else s.closed}
  | .scope v => {s with scope:=v,port:=cut s.port}
  | .permission v => {s with permission:=v}
  | .delivery v => {s with delivery:=v}
  | .access v => {s with nAccess:=v,port:=cut s.port}

def Enabled (laws : RecipientCorrection.Laws) (s : State) : Event → Prop
  | .assemble => s.eligible=true ∧ s.life=.donor ∧ s.cursor<8 ∧ 0<s.held ∧ 0<s.assembly
  | .omitWindow => s.eligible=true ∧ s.life=.donor ∧ s.cursor=6 ∧ 0<s.assembly
  | .copyRead => s.eligible=true ∧ s.life=.donor ∧ s.cursor=8 ∧ s.copyLatch=none ∧ 0<s.copyFund
  | .copyWrite _ _ _ _ => s.life=.quiesced ∧ s.copyLatch.isSome=true ∧
      s.core.escrow=0 ∧ 0<s.copyFund
  | .bindAccess _ => s.life=.committed ∧ s.window=true ∧ s.cursor=8 ∧ 0<s.held ∧ 0<s.assembly
  | .release => s.life=.bound ∧ s.released=false
  | .probeStart => s.life=.child ∧ s.released=true ∧ s.attempts<2 ∧ s.probing=false ∧ s.reading=false
  | .probeEnd => s.probing=true ∧ s.bank.phase=.idle
  | .bank e => s.life=.child ∧ s.probing=true ∧ s.reading=false ∧ bankGuard s e ∧
      EmissionArchive.Enabled (producer laws) 3 (archive s) e ∧
      EmissionArchive.Valid (producer laws) (archive s)
  | .prepare => s.life=.child ∧ s.attempts=2 ∧ s.probing=false ∧ s.reading=false ∧
      s.bank.phase=.idle ∧ s.reader.reserve=0 ∧ s.reader.workspace=true
  | .reason e => s.life=.child ∧ s.reading=true ∧ PaidRecipientReasons.Enabled s.reader e
  | .read => s.life=.child ∧ s.reading=true ∧ s.closed=false ∧ s.port=.idle ∧
      s.core.phase=.ready ∧ 1≤s.core.hardware.fuel
  | .assess => s.closed=false ∧ s.port=.read ∧ Known s ∧ 1≤s.core.hardware.fuel
  | .attempt => s.closed=false ∧ s.port=.help
  | .abstain => s.closed=false ∧ s.port=.abstain
  | .trial e => s.port=.executing ∧ s.closed=false ∧ RecipientOnly s e ∧
      (Settlement s e ∨ (Known s ∧ gates s)) ∧ RecipientIdentification.Valid s.core ∧ RecipientIdentification.Enabled s.core e
  | .scope _ | .permission _ | .delivery _ | .access _ => True

def Step (laws : RecipientCorrection.Laws) (s : State) (e : Event) (t : State) := Enabled laws s e ∧ t=advance laws s e
def process (laws : RecipientCorrection.Laws) : Generative.Process State Event := ⟨Step laws⟩

def charge (laws : RecipientCorrection.Laws) (s : State) : Event → Nat
  | .assemble | .copyRead | .copyWrite _ _ _ _ | .bindAccess _ | .read | .assess => 1
  | .bank e => EmissionArchive.charge (producer laws) (archive s) e
  | .reason e => PaidRecipientReasons.charge e
  | .trial e => RecipientIdentification.spending e+RecipientIdentification.waste laws s.core e
  | _ => 0

def run (laws : RecipientCorrection.Laws) : State → List Event → State
  | s,[] => s
  | s,e::es => run laws (advance laws s e) es

def Runnable (laws : RecipientCorrection.Laws) : State → List Event → Prop
  | _,[] => True
  | s,e::es => Enabled laws s e ∧ Runnable laws (advance laws s e) es

instance (s : State) (e : RecipientIdentification.Event) : Decidable (Settlement s e) := by
  cases e <;> cases s.core.phase <;> unfold Settlement <;> infer_instance
instance (s : State) (e : RecipientIdentification.Event) : Decidable (RecipientOnly s e) := by
  cases e <;> unfold RecipientOnly <;> infer_instance

instance (laws : RecipientCorrection.Laws) (s : State) (e : PublicationBridge.ArchiveEvent) :
    Decidable (bankGuard s e) := by
  cases e with
  | bind i h => unfold bankGuard; infer_instance
  | write => exact isTrue trivial
  | core e w => cases e <;> unfold bankGuard <;> infer_instance

instance (laws : RecipientCorrection.Laws) (s : State) (e : PublicationBridge.ArchiveEvent) :
    Decidable (EmissionArchive.Enabled (producer laws) 3 (archive s) e) := by
  cases e with
  | bind i h => unfold EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.binding; infer_instance
  | core e w =>
      unfold EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.Step
      cases e <;> unfold RecipientIdentification.Step <;> infer_instance
  | write =>
      cases hp:s.bank.phase <;> simp [EmissionArchive.Enabled,producer,RecipientArchive.producer,archive,hp] <;> infer_instance

instance (laws : RecipientCorrection.Laws) (s : State) :
    Decidable (EmissionArchive.Valid (producer laws) (archive s)) := by
  cases hp:s.bank.phase <;> simp [EmissionArchive.Valid,archive,hp] <;> infer_instance

instance (laws : RecipientCorrection.Laws) (s : State) (e : Event) : Decidable (Enabled laws s e) := by
  cases e <;> unfold Enabled <;> infer_instance

instance runnableDecidable (laws : RecipientCorrection.Laws) (s : State) (es : List Event) :
    Decidable (Runnable laws s es) := match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable laws (advance laws s e) es
      inferInstanceAs (Decidable (Enabled laws s e ∧ Runnable laws (advance laws s e) es))

theorem runnable_trace {laws : RecipientCorrection.Laws} {s : State} {es : List Event}
    (h : Runnable laws s es) : Generative.Trace (process laws) s es (run laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih h.2)

theorem entry_accounts (s : AcquiredEvaluation.State) (route : Route) :
    energy (enter s route)=AcquiredEvaluation.energy s+96 ∧ material (enter s route)=78 := by
  constructor
  · simp [energy,enter,oldCommon,oldSource,readerUnit,Native.energy,AcquiredEvaluation.energy,
      FreshRevision.energy,RecipientAction.energy,PaidRecipientReasons.energy]
    omega
  · rfl

theorem old_money_has_no_subsidy_event {laws : RecipientCorrection.Laws} {s t : State} {e : Event}
    (h : Step laws s e t) (ne : ∀ q sc pm dl, e≠.copyWrite q sc pm dl) :
    t.commonCustody=s.commonCustody ∧ t.sourceCustody=s.sourceCustody := by
  rcases h with ⟨_,rfl⟩
  cases e <;> try exact ⟨rfl,rfl⟩
  case copyWrite q sc pm dl => exact False.elim (ne q sc pm dl rfl)
  case attempt => unfold advance; split <;> exact ⟨rfl,rfl⟩

theorem actual_candidate_commit (laws : RecipientCorrection.Laws) (s : State)
    (q : Nat) (h : s.copyLatch=some q) :
    (advance laws s (.copyWrite false true true true)).core.hardware.q=q ∧
    (advance laws s (.copyWrite false true true true)).core.hardware.last=false ∧
    (advance laws s (.copyWrite false true true true)).history=s.history ∧
    (advance laws s (.copyWrite false true true true)).native=s.native ∧
    (advance laws s (.copyWrite false true true true)).core.patient=s.core.patient := by
  simp [advance,h]

theorem paid_read_is_actual_candidate (laws : RecipientCorrection.Laws) (s : State) :
    (advance laws s .copyRead).copyLatch=some s.core.hardware.q ∧
    (advance laws s .copyRead).life=.quiesced := ⟨rfl,rfl⟩

theorem no_second_copy {laws : RecipientCorrection.Laws} {s : State}
    (h : s.life≠.donor) : ¬Enabled laws s .copyRead := by
  intro he; exact h he.2.1

theorem archive_set (s : State) (a : RecipientAction.Archive) (hc : a.world.context=true) :
    archive (setArchive s a)=a := by
  cases a; rename_i w b e n r p; cases w
  simp_all [archive,setArchive]

theorem bank_successor_context {laws : RecipientCorrection.Laws} {s : State}
    {e : PublicationBridge.ArchiveEvent} (h : Enabled laws s (.bank e)) :
    (EmissionArchive.advance (producer laws) (archive s) e).world.context=true := by
  cases e with
  | bind i hd => rfl
  | write => exact congrArg (fun w:RecipientArchive.World=>w.context)
      (EmissionArchive.write_preserves_world (producer laws) (archive s))
  | core e w =>
      cases e with
      | contextChange c => exact False.elim h.2.2.2.1
      | core e =>
          have hw:=h.2.2.2.2.1.2
          rw [hw]
          rfl

theorem bank_step_projects {laws : RecipientCorrection.Laws} {s t : State}
    {e : PublicationBridge.ArchiveEvent} (h : Step laws s (.bank e) t) :
    EmissionArchive.Step (producer laws) 3 (archive s) e (archive t) := by
  rcases h with ⟨he,rfl⟩
  have hc:=bank_successor_context he
  refine ⟨he.2.2.2.2.2,he.2.2.2.2.1,?_⟩
  exact archive_set _ _ hc

theorem bank_trace_projects {laws : RecipientCorrection.Laws} {s t : State}
    {es : List PublicationBridge.ArchiveEvent}
    (h : Generative.Trace (process laws) s (es.map Event.bank) t) :
    Generative.Trace (EmissionArchive.process (producer laws) 3) (archive s) es (archive t) := by
  induction es generalizing s with
  | nil => cases h; exact .nil _
  | cons e es ih => cases h with
    | cons he ht => exact .cons (bank_step_projects he) (ih ht)

theorem reader_step_projects {laws : RecipientCorrection.Laws} {s t : State} {e : PaidRecipientReasons.Event}
    (h : Step laws s (.reason e) t) : PaidRecipientReasons.Step s.reader e t.reader := by
  rcases h with ⟨he,rfl⟩; exact ⟨he.2.2,rfl⟩

theorem reader_trace_projects {laws : RecipientCorrection.Laws} {s t : State}
    {es : List PaidRecipientReasons.Event}
    (h : Generative.Trace (process laws) s (es.map Event.reason) t) :
    Generative.Trace (PaidRecipientReasons.process Unit) s.reader es t.reader := by
  induction es generalizing s with
  | nil => cases h; exact .nil _
  | cons e es ih => cases h with
    | cons he ht => exact .cons (reader_step_projects he) (ih ht)

/-- Derived from actual production into the NEW bank, never from an old publication. -/
theorem fresh_bank_facts {laws : RecipientCorrection.Laws} {s t : State}
    {w : RecipientArchive.World} {budget cells : Nat} {es : List PublicationBridge.ArchiveEvent}
    (empty : archive s=EmissionArchive.empty w budget cells) (ready : w.core.phase=.ready)
    (history : Generative.Trace (process laws) s (es.map Event.bank) t) :
    PaidArchiveReader.Facts (RecipientCorrection.lookup laws .recipient)
      (PaidArchiveReader.initial () t.bank.records true 24) := by
  have ht:=bank_trace_projects history
  rw [empty] at ht
  have hs:=RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws w budget cells (RecipientArchive.ready_sound laws w ready)) ht
  intro i r hr hp hrec
  exact RecipientArchive.completed_record_sound hs hr hp hrec

end EvaluativeSuccession
