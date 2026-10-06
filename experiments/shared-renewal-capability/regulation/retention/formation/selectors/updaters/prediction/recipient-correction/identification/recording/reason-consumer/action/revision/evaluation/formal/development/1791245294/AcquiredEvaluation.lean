import RevisionWitness
import EvaluationPreparation

/- One continuing recipient core. The six binary data cells and the supplied
finite adapter/port control modes are separate declared capacities. No native
return is a recipient receipt, and no learned number is an ethical ground. -/
namespace AcquiredEvaluation
open RecipientCorrection (Laws lookup packedAct)

inductive NativeMode where
  | ready | paid | returned | known | missing | closed
  deriving DecidableEq, Repr
inductive PortMode where
  | idle | read | help | abstain | executing | consumed
  deriving DecidableEq, Repr
inductive Routing where
  | shared | filtered | inverted | fixed | conventional
  deriving DecidableEq, Repr
inductive Channel where
  | faithful | inverted | missing
  deriving DecidableEq, Repr

structure State where
  parent : FreshRevision.State
  n : Nat
  count : Nat
  mode : NativeMode
  bit : Bool
  cells : Nat
  adapter : Bool
  routing : Routing
  updates : Bool
  suppressed : Bool
  training : Nat
  source0 : Nat
  source1 : Nat
  source2 : Nat
  later : Nat
  laterSource : Nat
  port : Bool
  portMode : PortMode
  retired : Nat
  freeA : Nat
  freeH : Nat

def core (s : State) := FreshRevision.core s.parent
def setCore (s : State) (c : RecipientIdentification.State) : State :=
  { s with parent:={s.parent with parent:=RecipientAction.setCore s.parent.parent c} }
def fuel (s : State) := (core s).hardware.fuel
def withFuel (s : State) (f : Nat) := setCore s {core s with hardware:={(core s).hardware with fuel:=f}}
def source (s : State) := if s.count=0 then s.source0 else if s.count=1 then s.source1 else s.source2
def withSource (s : State) (a : Nat) :=
  if s.count=0 then {s with source0:=a} else if s.count=1 then {s with source1:=a} else {s with source2:=a}
def transfer (s : State) := min 4 s.training
def returned (b : Bool) : Nat := if b then 2 else 0
def update (n : Nat) (loss : Bool) := n/2+(if loss then 4 else 0)

def Current (s : State) : Prop := PaidRecipientReasons.CurrentPublication s.parent.parent.reasons
def command (s : State) : Option Bool :=
  if Current s ∧ s.parent.parent.scope=true then RecipientAction.route s.parent.parent.reasons.working else none
def Known (s : State) : Prop := command s=some (packedAct (core s).hardware.q .recipient) ∧
  (core s).hardware.last=true
def Admitted (s : State) : Prop :=
  s.parent.opened=true ∧ s.parent.reading=true ∧ Current s ∧
  (core s).phase=.ready ∧ (core s).active=true ∧ s.parent.parent.scope=true ∧
  s.cells=6 ∧ s.adapter=true
def CanStart (s : State) : Prop := Known s ∧ s.parent.parent.scope=true ∧
  s.parent.parent.permission=true ∧ s.parent.parent.delivery=true ∧
  (core s).phase=.ready ∧ 0<(core s).packets

def table (n : Nat) : Bool := n=7
def help (s : State) : Bool :=
  if s.suppressed then false else match s.routing with
  | .shared => decide (64<10*s.n)
  | .filtered | .inverted => false
  | .fixed => true
  | .conventional => table s.n

inductive Event where
  | pay | returnNative (returns : Bool) | readNative (channel : Channel) | writeNative
  | read | assess | attempt | abstain | replace | suppress
  | trial (e : RecipientIdentification.Event)
  | voluntary (e : RecipientIdentification.Event)
  | reason (e : PaidRecipientReasons.Event)
  | scope (v : Bool) | permission (v : Bool) | delivery (v : Bool)
  deriving DecidableEq, Repr

instance (s : State) : Decidable (Current s) := by unfold Current; infer_instance
instance (s : State) : Decidable (Known s) := by unfold Known; infer_instance
instance (s : State) : Decidable (CanStart s) := by unfold CanStart; infer_instance

def old (laws : Laws) (s : State) (e : RecipientAction.Event) : State :=
  { s with parent:=FreshRevision.actionAdvance laws s.parent e }

def advance (laws : Laws) (s : State) : Event → State
  | .pay => {withFuel s (fuel s+transfer s-2) with training:=s.training-transfer s,mode:=.paid,portMode:=.consumed}
  | .returnNative b =>
      let t:=withFuel s (fuel s+returned b)
      {withSource t (source s-returned b) with bit:=b,mode:=.returned}
  | .readNative c => {withFuel s (fuel s-1) with bit:=(if c=.faithful then !s.bit else s.bit), mode:=(if c=.missing then .missing else .known)}
  | .writeNative => {withFuel s (fuel s-1) with n:=(if s.mode=.known ∧ s.updates=true then update s.n s.bit else s.n), count:=s.count+1,mode:=(if s.count+1=3 then .closed else .ready),bit:=false, portMode:=(if s.count+1=3 ∧ s.port=true then .idle else .consumed)}
  | .read => {withFuel s (fuel s-1) with portMode:=(if Known s then .read else .consumed)}
  | .assess => {withFuel s (fuel s-1) with portMode:=(if help s then .help else .abstain)}
  | .attempt => {s with portMode:=(if CanStart s then .executing else .consumed)}
  | .abstain => {s with portMode:=.consumed}
  | .replace =>
      let t:=setCore s {core s with hardware:={(core s).hardware with fuel:=fuel s+s.later-1}, packets:=(core s).packets+s.laterSource/10}
      {t with later:=0,laterSource:=s.laterSource%10,port:=true,portMode:=.idle, retired:=s.retired+(if s.port then 1 else 0),freeA:=s.freeA-1,freeH:=s.freeH-1}
  | .suppress => {withFuel s (fuel s-1) with suppressed:=true,portMode:=.idle}
  | .trial e =>
      let t:=old laws s (.voluntary e)
      {t with portMode:=(if e=.write ∨ e=.miss then .consumed else s.portMode)}
  | .voluntary e => {old laws s (.voluntary e) with portMode:=.consumed}
  | .reason e => {old laws s (.reason e) with portMode:=.consumed}
  | .scope v => {old laws s (.setScope v) with portMode:=.consumed}
  | .permission v => old laws s (.setPermission v)
  | .delivery v => old laws s (.setDelivery v)

def Enabled (s : State) : Event → Prop
  | .pay => Admitted s ∧ s.mode=.ready ∧ s.count<3 ∧ 2≤fuel s+transfer s
  | .returnNative b => s.mode=.paid ∧ returned b≤source s
  | .readNative _ => s.mode=.returned ∧ 1≤fuel s
  | .writeNative => (s.mode=.known ∨ s.mode=.missing) ∧ s.count<3 ∧ 1≤fuel s
  | .read => s.count=3 ∧ s.mode=.closed ∧ s.cells=6 ∧ s.adapter=true ∧
      s.port=true ∧ s.portMode=.idle ∧ (core s).phase=.ready ∧ 1≤fuel s
  | .assess => s.port=true ∧ s.portMode=.read ∧ Known s ∧ 1≤fuel s
  | .attempt => s.port=true ∧ s.portMode=.help
  | .abstain => s.portMode=.abstain
  | .replace => s.count=3 ∧ s.mode=.closed ∧ s.portMode=.consumed ∧
      (core s).phase=.ready ∧ 1≤s.freeA ∧ 1≤s.freeH ∧ 1≤s.later
  | .suppress => s.count=3 ∧ s.mode=.closed ∧ s.portMode=.idle ∧
      (core s).phase=.ready ∧ 1≤fuel s
  | .trial e => RecipientAction.Enabled s.parent.parent (.voluntary e) ∧
      (RecipientAction.Settlement s.parent.parent e ∨ (s.portMode=.executing ∧ Known s))
  | .voluntary e => RecipientAction.Enabled s.parent.parent (.voluntary e)
  | .reason e => RecipientAction.Enabled s.parent.parent (.reason e)
  | .scope _ | .permission _ | .delivery _ => True

instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled Admitted <;> infer_instance

def Step (laws : Laws) (s : State) (e : Event) (t : State) := Enabled s e ∧ t=advance laws s e
def process (laws : Laws) : Generative.Process State Event := ⟨Step laws⟩
def energy (s : State) := FreshRevision.energy s.parent+s.training+s.source0+s.source1+s.source2+s.later+s.laterSource
def material (s : State) := FreshRevision.material s.parent+2*s.cells+
  2*(if s.adapter then 1 else 0)+2*(if s.port then 1 else 0)+2*s.retired+s.freeA+s.freeH
def charge (laws : Laws) (s : State) : Event → Nat
  | .pay => 2
  | .readNative _ | .writeNative | .read | .assess | .replace | .suppress => 1
  | .trial e | .voluntary e => RecipientAction.charge laws s.parent.parent (.voluntary e)
  | .reason e => RecipientAction.charge laws s.parent.parent (.reason e)
  | _ => 0
def spent (laws : Laws) (s : State) : List Event → Nat
  | [] => 0
  | e::es => charge laws s e+spent laws (advance laws s e) es
def run (laws : Laws) (s : State) : List Event → State
  | [] => s
  | e::es => run laws (advance laws s e) es
def Runnable (laws : Laws) (s : State) : List Event → Prop
  | [] => True
  | e::es => Enabled s e ∧ Runnable laws (advance laws s e) es
instance runnableDecidable (laws : Laws) (s : State) (es : List Event) : Decidable (Runnable laws s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable laws (advance laws s e) es
      inferInstanceAs (Decidable (Enabled s e ∧ Runnable laws (advance laws s e) es))

theorem runnable_trace {laws : Laws} {s : State} {es : List Event} (h : Runnable laws s es) :
    Generative.Trace (process laws) s es (run laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih h.2)

theorem update_bounded {n : Nat} (h : n≤7) (b : Bool) : update n b≤7 := by
  cases b <;> simp [update] <;> omega

theorem shared_threshold {n : Nat} (h : n≤7) : 64<10*n ↔ n=7 := by omega

theorem three_losses : update (update (update 0 true) true) true=7 ∧
    update (update (update 0 false) false) false=0 := by decide

theorem conventional_same_on_capacity {s : State} (h : s.n≤7) :
    help {s with routing:=.shared}=help {s with routing:=.conventional} := by
  simp [help,table,shared_threshold h]

theorem permission_cut_retains_evaluation (laws : Laws) (s : State) (v : Bool) :
    command (advance laws s (.permission v))=command s ∧
    (advance laws s (.permission v)).n=s.n ∧
    (advance laws s (.permission v)).portMode=s.portMode := ⟨rfl,rfl,rfl⟩

theorem trial_projects {laws : Laws} {s t : State} {e : RecipientIdentification.Event}
    (h : Step laws s (.trial e) t) : RecipientIdentification.Step laws (core s) e (core t) := by
  rcases h with ⟨he,rfl⟩
  exact RecipientAction.voluntary_projects ⟨he.1,rfl⟩

theorem recipient_only (s : State) : ¬Enabled s (.trial (.sense .actor)) := by
  intro h
  exact (RecipientAction.recipient_port_cannot_sense_actor s.parent.parent).2 h.1

theorem writes_consume_assessment (laws : Laws) (s : State) :
    (advance laws s (.trial .write)).portMode=.consumed ∧
    (advance laws s (.trial .miss)).portMode=.consumed := by simp [advance]

theorem no_new_trial_after_consumption {s : State} (h : s.portMode=.consumed) :
    ¬Enabled s (.trial .rent) := by
  rintro ⟨_,hs|hs⟩
  · cases (core s).phase <;> simp [RecipientAction.Settlement,core,FreshRevision.core] at hs
  · rw [h] at hs; cases hs.1

theorem pending_port_not_replaceable {s : State} (h : s.portMode=.read ∨ s.portMode=.help ∨ s.portMode=.abstain) :
    ¬Enabled s .replace := by
  intro he
  rcases h with h|h|h <;> rw [h] at he <;> cases he.2.2.1

end AcquiredEvaluation

#print axioms AcquiredEvaluation.runnable_trace
#print axioms AcquiredEvaluation.update_bounded
#print axioms AcquiredEvaluation.shared_threshold
#print axioms AcquiredEvaluation.three_losses
#print axioms AcquiredEvaluation.conventional_same_on_capacity
#print axioms AcquiredEvaluation.permission_cut_retains_evaluation
#print axioms AcquiredEvaluation.trial_projects
#print axioms AcquiredEvaluation.recipient_only
#print axioms AcquiredEvaluation.writes_consume_assessment
#print axioms AcquiredEvaluation.no_new_trial_after_consumption
#print axioms AcquiredEvaluation.pending_port_not_replaceable
