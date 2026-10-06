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
  (r.reader.active=false ∧ r.reader.token=none ∧ r.reader.next=0 ∧ r.reader.cache 0=none ∧ r.reader.cache 1=none ∧ r.reader.cache 2=none ∧ r.phase=0 ∧
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
  probeRunning : Bool
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
  { core:=AcquiredEvaluation.core s, reader:=readerUnit s.parent.parent.reasons, bank:=⟨0,0,4,fun _=>none,.idle,0,none,false⟩, history:=⟨(AcquiredEvaluation.core s).hardware,s.parent.parent.reasons.reader.world.records, s.parent.bank.records,s.parent.parent.reasons.reader.world.world.next,s.parent.bank.next, s.parent.parent.reasons.reader.world.world.context, s.parent.parent.reasons.reader.world.world.current,s.parent.bank.current, s.parent.parent.reasons.reader.world.world.live,s.parent.bank.live, s.parent.opened,s.parent.reading,s.retired,s.port⟩, native:=⟨s.n,s.count,s.cells,s.mode==.closed,s.source0,s.source1,s.source2⟩, commonCustody:=oldCommon s, sourceCustody:=oldSource s, assembly:=9,copyFund:=2,operationFund:=26,writerFund:=5,readerFund:=24,sourceFund:=30, inaccessibleCommon:=0,inaccessibleSource:=0,held:=9,installed:=0,cursor:=0, eligible:=decide (Admissible s),life:=.donor,copyLatch:=none,window:=false,nAccess:=false, scope:=s.parent.parent.scope,permission:=s.parent.parent.permission,delivery:=s.parent.parent.delivery, released:=false,attempts:=0,probeRunning:=false,probing:=false,reading:=false,port:=.idle,closed:=false,route:=route }

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
  | .bind i _ => s.probeRunning=true ∧ i=1 ∧ s.cursor=8 ∧ s.window=true
  | .write => True
  | .core (.contextChange _) _ => False
  | .core (.core e) _ => s.probeRunning=true ∧ RecipientOnly s e ∧ (Settlement s e ∨ gates s) ∧
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
  | .probeStart => {s with attempts:=s.attempts+1,probing:=decide (canProbe s),probeRunning:=decide (canProbe s)}
  | .probeEnd => {s with probing:=false,probeRunning:=false}
  | .bank e =>
      let t:=setArchive s (EmissionArchive.advance (producer laws) (archive s) e)
      match e with
      | .core (.core .write) _ | .core (.core .miss) _ => {t with probeRunning:=false}
      | _ => t
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
  | .scope v | .permission v | .delivery v | .access v => v=false

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

local instance (priority := 1100) (s : RecipientIdentification.State) (e : RecipientIdentification.Event) :
    Decidable (RecipientIdentification.Enabled s e) :=
  decidable_of_iff (ActionWitness.coreCheck s e=true) (ActionWitness.core_check_iff s e)

def settlementCheck (s : State) (e : RecipientIdentification.Event) : Bool :=
  match e,s.core.phase with
  | .acquire _,.worked _ _ | .write,.acquired _ _ => true
  | _,_ => false

theorem settlement_check_iff (s : State) (e : RecipientIdentification.Event) :
    settlementCheck s e=true ↔ Settlement s e := by
  cases e <;> cases hp:s.core.phase <;> simp [settlementCheck,Settlement,hp]

instance (s : State) (e : RecipientIdentification.Event) : Decidable (Settlement s e) :=
  decidable_of_iff (settlementCheck s e=true) (settlement_check_iff s e)

instance (s : State) (e : RecipientIdentification.Event) : Decidable (RecipientOnly s e) := by
  cases e <;> unfold RecipientOnly <;> infer_instance

instance (s : State) (e : PublicationBridge.ArchiveEvent) :
    Decidable (bankGuard s e) := by
  cases e with
  | bind i h => unfold bankGuard; infer_instance
  | write => exact isTrue trivial
  | core e w => cases e <;> unfold bankGuard <;> infer_instance

def writeCheck (s : State) : Bool := match s.bank.phase with
  | .latched _ _ bits => decide (s.bank.live=true ∧ bits.length<4 ∧ 0<s.bank.escrow)
  | _ => false

theorem write_check_iff (laws : RecipientCorrection.Laws) (s : State) :
    writeCheck s=true ↔ EmissionArchive.Enabled (producer laws) 3 (archive s) .write := by
  cases hp:s.bank.phase with
  | idle => simp [writeCheck,EmissionArchive.Enabled,archive,hp]
  | bound i h => simp [writeCheck,EmissionArchive.Enabled,archive,hp]
  | latched i r bits =>
      simp only [writeCheck,hp,decide_eq_true_eq,EmissionArchive.Enabled,archive]
      constructor
      · rintro ⟨hl,hb,he⟩; exact ⟨hl,i,r,bits,rfl,hb,he⟩
      · rintro ⟨hl,j,q,bs,h,hn,he⟩; cases h; exact ⟨hl,hn,he⟩

instance (laws : RecipientCorrection.Laws) (s : State) (e : PublicationBridge.ArchiveEvent) :
    Decidable (EmissionArchive.Enabled (producer laws) 3 (archive s) e) := by
  cases e with
  | bind i h => unfold EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.binding; infer_instance
  | core e w =>
      unfold EmissionArchive.Enabled producer RecipientArchive.producer RecipientArchive.Step
      cases e <;> unfold RecipientIdentification.Step <;> infer_instance
  | write => exact decidable_of_iff (writeCheck s=true) (write_check_iff laws s)

instance (laws : RecipientCorrection.Laws) (s : State) :
    Decidable (EmissionArchive.Valid (producer laws) (archive s)) :=
  decidable_of_iff (RevisionWitness.validCheck laws (archive s)=true)
    (RevisionWitness.valid_check_iff laws (archive s))

instance (s : Reasons) (e : PaidRecipientReasons.Event) : Decidable (PaidRecipientReasons.Enabled s e) := by
  cases e with
  | reader e => cases e <;> unfold PaidRecipientReasons.Enabled PaidArchiveReader.Enabled <;> infer_instance
  | fund | activate | infer i a | path p | publish | cold =>
      unfold PaidRecipientReasons.Enabled PaidArchiveReader.Complete; infer_instance

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
      FreshRevision.energy,RecipientAction.energy,PaidRecipientReasons.energy,AcquiredEvaluation.core,FreshRevision.core]
    omega
  · rfl

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
  | write =>
      exact congrArg (fun w:RecipientArchive.World=>w.context) (EmissionArchive.write_preserves_world (producer laws) (archive s))
  | core e w =>
      cases e with
      | contextChange c => exact False.elim h.2.2.2.1
      | core e =>
          have hw:=h.2.2.2.2.1.2
          rw [hw]
          rfl

theorem archive_bank_advance (laws : RecipientCorrection.Laws) (s : State) (e : PublicationBridge.ArchiveEvent) :
    archive (advance laws s (.bank e))=archive (setArchive s (EmissionArchive.advance (producer laws) (archive s) e)) := by
  cases e with
  | bind i h | write => rfl
  | core e w => cases e with
    | contextChange c => rfl
    | core e => cases e <;> rfl

theorem bank_step_projects {laws : RecipientCorrection.Laws} {s t : State}
    {e : PublicationBridge.ArchiveEvent} (h : Step laws s (.bank e) t) :
    EmissionArchive.Step (producer laws) 3 (archive s) e (archive t) := by
  rcases h with ⟨he,rfl⟩
  have hc:=bank_successor_context he
  refine ⟨he.2.2.2.2.2,he.2.2.2.2.1,?_⟩
  rw [archive_bank_advance]
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

def overhead (s : State) := PaidRecipientReasons.energy s.reader+s.native.energy+
  s.commonCustody.sum+s.sourceCustody.sum+s.assembly+s.copyFund+s.operationFund+
  s.writerFund+s.readerFund+s.sourceFund+s.inaccessibleCommon+s.inaccessibleSource

theorem energy_decomposition (laws : RecipientCorrection.Laws) (s : State) :
    energy s=EmissionArchive.energy (producer laws) (archive s)+overhead s := by
  simp [energy,EmissionArchive.energy,producer,RecipientArchive.producer,archive,overhead]
  omega

theorem bank_overhead (laws : RecipientCorrection.Laws) (s : State) (e : PublicationBridge.ArchiveEvent) :
    overhead (advance laws s (.bank e))=overhead s := by
  cases e with
  | bind i h | write => rfl
  | core e w => cases e with
    | contextChange c => rfl
    | core e => cases e <;> rfl

theorem step_energy {laws : RecipientCorrection.Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : energy t+charge laws s e=energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | bank e =>
      have hh:=EmissionArchive.step_energy (bank_step_projects (show Step laws s (.bank e) _ from ⟨he,rfl⟩))
      rw [energy_decomposition laws,energy_decomposition laws,bank_overhead]
      change EmissionArchive.energy (producer laws) (archive (advance laws s (.bank e)))+overhead s+
        EmissionArchive.charge (producer laws) (archive s) e=_
      omega
  | reason e =>
      have hh:=PaidRecipientReasons.step_ledger (show PaidRecipientReasons.Step s.reader e _ from ⟨he.2.2,rfl⟩)
      simp only [advance,energy,charge]
      omega
  | trial e =>
      have hh:=RecipientIdentification.step_energy
        (show RecipientIdentification.Step laws s.core e _ from ⟨he.2.2.2.2.1,he.2.2.2.2.2,rfl⟩)
      simp only [advance,energy,charge]
      omega
  | attempt => simp only [advance]; split <;> rfl
  | assemble => have hf:=he.2.2.2.2; simp only [advance,energy,charge]; omega
  | omitWindow => have hf:=he.2.2.2; simp only [advance,energy,charge]; omega
  | copyRead => have hf:=he.2.2.2.2; simp only [advance,energy,charge]; omega
  | copyWrite q sc pm dl =>
      have hz:=he.2.2.1
      have hf:=he.2.2.2
      simp only [advance,energy,charge,RecipientIdentification.energy,PaidRecipientReasons.energy,
        List.sum_append,List.sum_cons,List.sum_nil]
      omega
  | bindAccess v =>
      have hf:=he.2.2.2.2
      simp only [advance,energy,charge,PaidRecipientReasons.advance,PaidRecipientReasons.energy]
      omega
  | release =>
      simp only [advance,energy,charge,RecipientIdentification.energy]
      omega
  | prepare =>
      have hz:=he.2.2.2.2.2.1
      simp only [advance,energy,charge,PaidRecipientReasons.initial,PaidRecipientReasons.energy,
        PaidArchiveReader.initial]
      omega
  | read =>
      have hf:=he.2.2.2.2.2
      simp only [advance,energy,charge,RecipientIdentification.energy]
      omega
  | assess =>
      have hf:=he.2.2.2
      simp only [advance,energy,charge,RecipientIdentification.energy]
      omega
  | probeStart | probeEnd | abstain | scope v | permission v | delivery v | access v => rfl

def spent (laws : RecipientCorrection.Laws) : State → List Event → Nat
  | _,[] => 0
  | s,e::es => charge laws s e+spent laws (advance laws s e) es

theorem trace_run {laws : RecipientCorrection.Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : run laws s es=t := by
  induction h with
  | nil => rfl
  | cons he _ ih => simp only [run]; rw [←he.2]; exact ih

theorem trace_energy {laws : RecipientCorrection.Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : energy t+spent laws s es=energy s := by
  induction h with
  | nil => rfl
  | cons he _ ih =>
      have hh:=step_energy he
      simp only [spent]
      rw [←he.2]
      omega

theorem step_material {laws : RecipientCorrection.Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : material t=material s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | assemble => have hm:=he.2.2.2.1; simp only [advance,material]; omega
  | bindAccess v => have hm:=he.2.2.2.1; simp only [advance,material]; omega
  | bank e => cases e with
    | bind i hd | write => rfl
    | core e w => cases e with
      | contextChange c => rfl
      | core e => cases e <;> rfl
  | attempt => simp only [advance]; split <;> rfl
  | _ => rfl

theorem trace_material {laws : RecipientCorrection.Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : material t=material s := by
  induction h with
  | nil => rfl
  | cons he _ ih => exact ih.trans (step_material he)

theorem step_retains_native_and_history {laws : RecipientCorrection.Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : t.native=s.native ∧ t.history=s.history := by
  rcases h with ⟨_,rfl⟩
  cases e with
  | bank e => cases e with
    | bind i hd | write => exact ⟨rfl,rfl⟩
    | core e w => cases e with
      | contextChange c => exact ⟨rfl,rfl⟩
      | core e => cases e <;> exact ⟨rfl,rfl⟩
  | attempt => simp only [advance]; split <;> exact ⟨rfl,rfl⟩
  | _ => exact ⟨rfl,rfl⟩

theorem trace_retains_native_and_history {laws : RecipientCorrection.Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : t.native=s.native ∧ t.history=s.history := by
  induction h with
  | nil => exact ⟨rfl,rfl⟩
  | cons he _ ih =>
      have hh:=step_retains_native_and_history he
      exact ⟨ih.1.trans hh.1,ih.2.trans hh.2⟩

theorem no_free_guard_repair (laws : RecipientCorrection.Laws) (s : State) :
    ¬Enabled laws s (.scope true) ∧ ¬Enabled laws s (.permission true) ∧
    ¬Enabled laws s (.delivery true) ∧ ¬Enabled laws s (.access true) := by
  simp [Enabled]

theorem completed_probe_cannot_start_another_core_event (laws : RecipientCorrection.Laws)
    (s : State) (w : RecipientArchive.World) (e : RecipientIdentification.Event) :
    ¬Enabled laws (advance laws s (.bank (.core (.core .write) w)))
      (.bank (.core (.core e) w)) := by
  simp [Enabled,advance,bankGuard]

theorem selected_write_retires_token (laws : RecipientCorrection.Laws) (s : State) :
    (advance laws s (.trial .write)).port=.consumed ∧
    ¬Enabled laws (advance laws s (.trial .write)) (.trial .rent) := by
  simp [advance,Enabled]

theorem no_recipient_target_substitution (laws : RecipientCorrection.Laws) (s : State) :
    ¬Enabled laws s (.trial (.sense .actor)) := by
  simp [Enabled,RecipientOnly]

theorem unknown_read_is_paid_and_consumed {laws : RecipientCorrection.Laws} {s t : State}
    (h : Step laws s .read t) (unknown : ¬Known s) :
    t.core.hardware.fuel+1=s.core.hardware.fuel ∧ t.port=.consumed ∧ t.closed=true := by
  rcases h with ⟨he,rfl⟩
  have hf:=he.2.2.2.2.2
  constructor
  · change s.core.hardware.fuel-1+1=s.core.hardware.fuel
    omega
  · simp [advance,unknown]

theorem assessment_uses_retained_data {laws : RecipientCorrection.Laws} {s t : State}
    (h : Step laws s .assess t) : Known s ∧ t.native=s.native ∧
    t.core.hardware.q=s.core.hardware.q ∧ t.reader=s.reader ∧
    t.port=(if help s then .help else .abstain) ∧
    t.core.hardware.fuel+1=s.core.hardware.fuel := by
  rcases h with ⟨he,rfl⟩
  exact ⟨he.2.2.1,rfl,rfl,rfl,rfl,by have hf:=he.2.2.2; change _-1+1=_;omega⟩

theorem conventional_same_on_capacity (s : State) (h : s.native.n≤7) :
    help {s with route:=.shared}=help {s with route:=.conventional} := by
  simp only [help,AcquiredEvaluation.shared_threshold h]

theorem actual_fresh_publication {laws : RecipientCorrection.Laws} {s t : State}
    {w : RecipientArchive.World} {budget cells : Nat} {es : List PublicationBridge.ArchiveEvent}
    (empty : archive s=EmissionArchive.empty w budget cells) (ready : w.core.phase=.ready)
    (history : Generative.Trace (process laws) s (es.map Event.bank) t)
    {G : Prop} (root : G) {r : Reasons} {events : List PaidRecipientReasons.Event}
    (consumer : Generative.Trace (PaidRecipientReasons.process Unit)
      (PaidRecipientReasons.initial (PaidArchiveReader.initial () t.bank.records true 24) 0) events r) :
    PublicationBridge.Assured (RecipientCorrection.lookup laws .recipient) G r :=
  PublicationBridge.initialized_trace_assured root
    (PaidArchiveReader.initial_cache_agrees _ _ _ _) (fresh_bank_facts empty ready history) consumer

theorem current_command_meaning {s : State} {z : Bool} {G : Prop}
    (assured : PublicationBridge.Assured z G s.reader) (known : Known s) :
    G ∧ RecipientReasons.Compatible z (RecipientCorrection.packedAct s.core.hardware.q .recipient) := by
  have hc:=known.2.2.2.2
  unfold command at hc
  split at hc
  · rename_i hh
    have hp:PaidRecipientReasons.CurrentPublication s.reader:=hh.1.2.2
    have hm:=(assured.2.2 hp.1).2.2 _ (RecipientAction.route_is_member hc)
    exact RecipientAction.command_meaning.mp hm
  · cases hc

theorem selected_step_projects {laws : RecipientCorrection.Laws} {s t : State}
    {e : RecipientIdentification.Event} (h : Step laws s (.trial e) t) :
    RecipientIdentification.Step laws s.core e t.core := by
  rcases h with ⟨he,rfl⟩
  exact ⟨he.2.2.2.2.1,he.2.2.2.2.2,rfl⟩

theorem selected_trace_projects {laws : RecipientCorrection.Laws} {s t : State}
    {es : List RecipientIdentification.Event}
    (h : Generative.Trace (process laws) s (es.map Event.trial) t) :
    Generative.Trace (RecipientIdentification.process laws) s.core es t.core := by
  induction es generalizing s with
  | nil => cases h;exact .nil _
  | cons e es ih => cases h with
    | cons he ht => exact .cons (selected_step_projects he) (ih ht)

/-- Physical delivery uses calibrated facts and stability; no ethical G is a premise. -/
theorem selected_physical_effect {observed used : RecipientCorrection.Laws} {s t : State}
    (assured : PublicationBridge.Assured (RecipientCorrection.lookup observed .recipient) True s.reader)
    (known : Known s)
    (stable : RecipientCorrection.lookup observed .recipient=RecipientCorrection.lookup used .recipient)
    {channel : Bool}
    (history : Generative.Trace (process used) s
      ((RecipientIdentification.trial .recipient true channel).map Event.trial) t) :
    t.core.patient=s.core.patient+10 ∧
    RecipientCorrection.packedAct t.core.hardware.q .actor=RecipientCorrection.packedAct s.core.hardware.q .actor := by
  have meaning:=current_command_meaning assured known
  have hc:RecipientCorrection.packedAct s.core.hardware.q .recipient=RecipientCorrection.lookup used .recipient:=
    ((RecipientReasons.compatible_iff _ _).mp meaning.2).trans stable
  have ht:=selected_trace_projects history
  constructor
  · rw [RecipientIdentification.trace_run ht]
    simp [RecipientIdentification.run,RecipientIdentification.trial,RecipientIdentification.advance,
      RecipientIdentification.targetOf,RecipientIdentification.returned,RecipientIdentification.issued,
      RecipientCorrection.lookup,RecipientCorrection.receiptOf,RecipientIdentification.patientCredit] at hc ⊢
    simp [hc]
  · have ha:=RecipientIdentification.trial_actor_preserved used s.core .recipient true channel
    rw [←RecipientIdentification.trace_run ht] at ha
    exact ha

/-- The independently warranted ground is attached separately to instrumental meaning. -/
theorem warranted_instrumental_meaning {s : State} {z : Bool} {G : Prop}
    (assured : PublicationBridge.Assured z G s.reader) (known : Known s) :
    G ∧ RecipientReasons.Meaning G z (RecipientAction.commandNode (RecipientCorrection.packedAct s.core.hardware.q .recipient)) := by
  have hm:=current_command_meaning assured known
  exact ⟨hm.1,RecipientAction.command_meaning.mpr hm⟩

theorem run_append (laws : RecipientCorrection.Laws) (s : State) (xs ys : List Event) :
    run laws s (xs++ys)=run laws (run laws s xs) ys := by
  induction xs generalizing s with
  | nil => rfl
  | cons e es ih => exact ih _

end EvaluativeSuccession
