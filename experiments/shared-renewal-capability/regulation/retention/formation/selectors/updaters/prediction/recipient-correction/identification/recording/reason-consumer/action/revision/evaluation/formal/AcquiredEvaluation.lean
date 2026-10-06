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
inductive Opportunity where
  | firstDue | firstClosed | secondDue | finished
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
  opportunity : Opportunity
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
instance (s : State) : Decidable (Current s) := by unfold Current; infer_instance
def command (s : State) : Option Bool :=
  if Current s ∧ s.parent.parent.scope=true then RecipientAction.route s.parent.parent.reasons.working else none
def Known (s : State) : Prop := command s=some (packedAct (core s).hardware.q .recipient)
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
  | read | assess | attempt | abstain | close | replace | suppress
  | trial (e : RecipientIdentification.Event)
  | reason (e : PaidRecipientReasons.Event)
  | scope (v : Bool) | permission (v : Bool) | delivery (v : Bool)
  deriving DecidableEq, Repr

instance (s : State) : Decidable (Known s) := by unfold Known; infer_instance
instance (s : State) : Decidable (CanStart s) := by unfold CanStart; infer_instance

def Due (s : State) : Prop := s.opportunity=.firstDue ∨ s.opportunity=.secondDue
def Readable (s : State) : Prop := Due s ∧ s.count=3 ∧ s.mode=.closed ∧ s.cells=6 ∧ s.adapter=true ∧
  s.port=true ∧ s.portMode=.idle ∧ (core s).phase=.ready ∧ 1≤fuel s
def Assessable (s : State) : Prop := Due s ∧ s.port=true ∧ s.portMode=.read ∧ Known s ∧ 1≤fuel s
def Closeable (s : State) : Prop := Due s ∧ match s.portMode with
  | .idle => ¬Readable s
  | .read => ¬Assessable s
  | .help | .abstain => False
  | .executing | .consumed => True

instance (s : State) : Decidable (Due s) := by unfold Due; infer_instance
instance (s : State) : Decidable (Readable s) := by unfold Readable; infer_instance
instance (s : State) : Decidable (Assessable s) := by unfold Assessable; infer_instance
instance (s : State) : Decidable (Closeable s) := by
  unfold Closeable
  cases s.portMode <;> infer_instance

def old (laws : Laws) (s : State) (e : RecipientAction.Event) : State :=
  { s with parent:=FreshRevision.actionAdvance laws s.parent e }

def advance (laws : Laws) (s : State) : Event → State
  | .pay => {withFuel s (fuel s+transfer s-2) with training:=s.training-transfer s,mode:=.paid,portMode:=.consumed}
  | .returnNative b =>
      let t:=withFuel s (fuel s+returned b)
      {withSource t (source s-returned b) with bit:=b,mode:=.returned}
  | .readNative c => {withFuel s (fuel s-1) with bit:=(if c=.faithful then !s.bit else if c=.missing then false else s.bit), mode:=(if c=.missing then .missing else .known)}
  | .writeNative => {withFuel s (fuel s-1) with n:=(if s.mode=.known ∧ s.updates=true then update s.n s.bit else s.n), count:=s.count+1,mode:=(if s.count+1=3 then .closed else .ready),bit:=false, portMode:=(if s.count+1=3 ∧ s.port=true then .idle else .consumed)}
  | .read => {withFuel s (fuel s-1) with portMode:=(if Known s then .read else .consumed)}
  | .assess => {withFuel s (fuel s-1) with portMode:=(if help s then .help else .abstain)}
  | .attempt => {s with portMode:=(if CanStart s then .executing else .consumed)}
  | .abstain => {s with portMode:=.consumed}
  | .close => {s with opportunity:=(if s.opportunity=.firstDue then .firstClosed else .finished), portMode:=(if s.portMode=.idle then .consumed else s.portMode)}
  | .replace =>
      let t:=setCore s {core s with hardware:={(core s).hardware with fuel:=fuel s+s.later-1}, packets:=(core s).packets+s.laterSource/10}
      {t with later:=0,laterSource:=s.laterSource%10,port:=true,portMode:=.idle,opportunity:=.secondDue, retired:=s.retired+(if s.port then 1 else 0),freeA:=s.freeA-1,freeH:=s.freeH-1}
  | .suppress => {withFuel s (fuel s-1) with suppressed:=true,portMode:=.idle}
  | .trial e =>
      let t:=old laws s (.voluntary e)
      {t with portMode:=(if e=.write ∨ e=.miss then .consumed else s.portMode)}
  | .reason e => {old laws s (.reason e) with portMode:=.consumed}
  | .scope v => {old laws s (.setScope v) with portMode:=.consumed}
  | .permission v => old laws s (.setPermission v)
  | .delivery v => old laws s (.setDelivery v)

def Enabled (s : State) : Event → Prop
  | .pay => Admitted s ∧ s.mode=.ready ∧ s.count<3 ∧ 2≤fuel s+transfer s
  | .returnNative b => s.mode=.paid ∧ returned b≤source s
  | .readNative _ => s.mode=.returned ∧ 1≤fuel s
  | .writeNative => (s.mode=.known ∨ s.mode=.missing) ∧ s.count<3 ∧ 1≤fuel s
  | .read => Readable s
  | .assess => Assessable s
  | .attempt => Due s ∧ s.port=true ∧ s.portMode=.help
  | .abstain => Due s ∧ s.portMode=.abstain
  | .close => Closeable s
  | .replace => s.opportunity=.firstClosed ∧ s.count=3 ∧ s.mode=.closed ∧ s.portMode=.consumed ∧
      (core s).phase=.ready ∧ 1≤s.freeA ∧ 1≤s.freeH ∧ 1≤s.later
  | .suppress => s.count=3 ∧ s.mode=.closed ∧ s.portMode=.idle ∧
      (core s).phase=.ready ∧ 1≤fuel s
  | .trial e => RecipientAction.Enabled s.parent.parent (.voluntary e) ∧
      (RecipientAction.Settlement s.parent.parent e ∨ (s.portMode=.executing ∧ Due s ∧ Known s))
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
  | .trial e => RecipientAction.charge laws s.parent.parent (.voluntary e)
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
  · simp [RecipientAction.Settlement] at hs
  · rw [h] at hs; cases hs.1

theorem pending_port_not_replaceable {s : State} (h : s.portMode=.read ∨ s.portMode=.help ∨ s.portMode=.abstain) :
    ¬Enabled s .replace := by
  intro he
  unfold Enabled at he
  rcases h with h|h|h <;> rw [h] at he <;> cases he.2.2.2.1

theorem energy_with_fuel (s : State) (f : Nat) :
    energy (withFuel s f)+fuel s=energy s+f := by
  simp [energy,withFuel,setCore,core,fuel,FreshRevision.energy,FreshRevision.core,
    RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,
    RecipientIdentification.energy,PaidRecipientReasons.energy]
  omega

theorem old_energy {laws : Laws} {s : State} {e : RecipientAction.Event}
    (h : RecipientAction.Enabled s.parent.parent e) :
    energy (old laws s e)+RecipientAction.charge laws s.parent.parent e=energy s := by
  have hh:=RecipientAction.step_energy (show RecipientAction.Step laws s.parent.parent e _ from ⟨h,rfl⟩)
  simp only [energy,old,FreshRevision.actionAdvance,FreshRevision.energy]
  omega

theorem step_energy {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : energy t+charge laws s e=energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | pay =>
      have ht:transfer s≤s.training:=Nat.min_le_right _ _
      have hf:=he.2.2.2
      simp only [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | returnNative b =>
      have hf:=he.2
      by_cases h0:s.count=0 <;> by_cases h1:s.count=1 <;>
        simp [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge,withSource,source,h0,h1] at * <;> omega
  | readNative c =>
      have hf:=he.2
      simp only [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | writeNative =>
      have hf:=he.2.2
      simp only [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | read =>
      have hf:=he.2.2.2.2.2.2.2.2
      simp only [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | assess =>
      have hf:=he.2.2.2.2
      simp only [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | suppress =>
      have hf:=he.2.2.2.2
      simp only [advance,energy,withFuel,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | replace =>
      have hf:=he.2.2.2.2.2.2.2
      simp only [advance,energy,setCore,core,fuel,FreshRevision.core,FreshRevision.energy,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy,charge] at *
      omega
  | trial e =>
      have hh:=old_energy (laws:=laws) he.1
      simp only [advance,charge,energy] at *
      exact hh
  | reason e => exact old_energy he
  | permission v => exact old_energy (e:=.setPermission v) trivial
  | delivery v => exact old_energy (e:=.setDelivery v) trivial
  | scope v => exact old_energy (e:=.setScope v) trivial
  | attempt | abstain | close => rfl

theorem trace_energy {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : energy t+spent laws s es=energy s := by
  induction h with
  | nil => simp [spent]
  | cons he _ ih =>
      have hh:=step_energy he
      rcases he with ⟨_,rfl⟩
      simp only [spent]
      omega

theorem step_material {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : material t=material s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | returnNative b =>
      by_cases h0:s.count=0 <;> by_cases h1:s.count=1 <;>
        simp [advance,withSource,material,withFuel,setCore,core,FreshRevision.material,
          RecipientAction.material,RecipientAction.setCore,h0,h1]
  | replace =>
      have ha:=he.2.2.2.2.2.1
      have hb:=he.2.2.2.2.2.2.1
      cases hp:s.port <;>
        simp [advance,material,setCore,FreshRevision.material,RecipientAction.material,
          RecipientAction.setCore,hp]
      all_goals omega
  | trial e => cases e <;> rfl
  | _ => rfl

theorem trace_material {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : material t=material s := by
  induction h with
  | nil => rfl
  | cons he _ ih => exact ih.trans (step_material he)

theorem native_operation_shortfall (s : State) (b : Bool) (h : 2≤fuel s+transfer s) :
    fuel s+transfer s-(fuel (advance (false,false) (advance (false,false) s .pay) (.returnNative b)))=
      (if b then 0 else 2) := by
  cases b <;> by_cases h0:s.count=0 <;> by_cases h1:s.count=1 <;>
    simp [advance,withFuel,setCore,core,fuel,FreshRevision.core,
      RecipientAction.core,RecipientAction.setCore,withSource,source,returned,h0,h1] at * <;> omega

theorem known_command_meaning {s : State} {z : Bool} {G : Prop}
    (assured : PublicationBridge.Assured z G s.parent.parent.reasons) (hk : Known s) :
    G ∧ RecipientReasons.Compatible z (packedAct (core s).hardware.q .recipient) := by
  have hc:=hk
  unfold Known command at hc
  split at hc
  · rename_i hh
    have hm:=(assured.2.2 hh.1.1).2.2 _ (RecipientAction.route_is_member hc)
    exact RecipientAction.command_meaning.mp hm
  · cases hc

theorem trace_trial_projects {laws : Laws} {s t : State} {es : List RecipientIdentification.Event}
    (h : Generative.Trace (process laws) s (es.map Event.trial) t) :
    Generative.Trace (RecipientIdentification.process laws) (core s) es (core t) := by
  induction es generalizing s with
  | nil => cases h; exact .nil _
  | cons e es ih =>
      cases h with
      | cons he ht => exact .cons (trial_projects he) (ih ht)

/- The ethical G and the observation-to-work law agreement remain separate
premises. Acquired valuation controls selection; it creates no factual truth. -/
theorem current_selected_trial_effect {observed used : Laws} {s t : State} {G : Prop}
    (assured : PublicationBridge.Assured (lookup observed .recipient) G s.parent.parent.reasons)
    (known : Known s) (stable : lookup observed .recipient=lookup used .recipient)
    {channel : Bool}
    (history : Generative.Trace (process used) s
      ((RecipientIdentification.trial .recipient true channel).map Event.trial) t) :
    G ∧ (core t).patient=(core s).patient+10 ∧
    packedAct (core t).hardware.q .actor=packedAct (core s).hardware.q .actor := by
  have meaning:=known_command_meaning assured known
  have hc : packedAct (core s).hardware.q .recipient=lookup used .recipient :=
    ((RecipientReasons.compatible_iff _ _).mp meaning.2).trans stable
  have ht:=trace_trial_projects history
  have hp : (core t).patient=(core s).patient+10 := by
    rw [RecipientIdentification.trace_run ht]
    simp [RecipientIdentification.run,RecipientIdentification.trial,RecipientIdentification.advance,
      RecipientIdentification.targetOf,RecipientIdentification.returned,RecipientIdentification.issued,
      lookup,RecipientCorrection.receiptOf,RecipientIdentification.patientCredit] at hc ⊢
    simp [hc]
  have ha:=RecipientIdentification.trial_actor_preserved used (core s) .recipient true channel
  rw [←RecipientIdentification.trace_run ht] at ha
  exact ⟨meaning.1,hp,ha⟩

theorem assessment_exact {laws : Laws} {s t : State} (h : Step laws s .assess t) :
    Known s ∧ t.portMode=(if help s then .help else .abstain) ∧
    t.n=s.n ∧ (core t).hardware.q=(core s).hardware.q ∧
    t.parent.parent.reasons.reader.archive=s.parent.parent.reasons.reader.archive ∧
    t.parent.parent.reasons.working=s.parent.parent.reasons.working ∧
    fuel t+1=fuel s := by
  rcases h with ⟨he,rfl⟩
  refine ⟨he.2.2.2.1,rfl,rfl,rfl,rfl,rfl,?_⟩
  have hf:=he.2.2.2.2
  change fuel s-1+1=fuel s
  omega

theorem unsupported_blocks_assessment {s : State} (h : command s=none) : ¬Enabled s .assess := by
  intro he
  have hk:=he.2.2.2.1
  unfold Known at hk
  rw [h] at hk
  cases hk

theorem mismatched_command_blocks_assessment {s : State}
    (h : command s≠some (packedAct (core s).hardware.q .recipient)) : ¬Enabled s .assess := by
  intro he
  exact h he.2.2.2.1

theorem started_command_is_current {laws : Laws} {s t : State}
    (h : Step laws s .attempt t) (started : t.portMode=.executing) :
    Current s ∧ s.parent.parent.scope=true ∧ s.parent.parent.permission=true ∧
    s.parent.parent.delivery=true ∧
    RecipientAction.route s.parent.parent.reasons.working=some (packedAct (core s).hardware.q .recipient) := by
  rcases h with ⟨_,rfl⟩
  simp only [advance] at started
  split at started
  · rename_i hc
    have hk:=hc.1
    unfold Known command at hk
    split at hk
    · rename_i hp
      exact ⟨hp.1,hp.2,hc.2.2.1,hc.2.2.2.1,hk⟩
    · cases hk
  · cases started

theorem context_interleaving_does_not_close (laws : Laws) (s : State) (v : Bool) :
    (advance laws s (.scope v)).opportunity=s.opportunity ∧
    (advance laws s (.scope v)).portMode=.consumed := ⟨rfl,rfl⟩

theorem replacement_cannot_repeat (laws : Laws) (s : State) :
    ¬Enabled (advance laws s .replace) .replace := by
  intro h
  cases h.1

theorem completed_opportunity_no_new_read {s : State} (h : s.opportunity=.finished) :
    ¬Enabled s .read ∧ ¬Enabled s .assess ∧ ¬Enabled s .attempt := by
  have hd:¬Due s:=by simp [Due,h]
  exact ⟨fun he=>hd he.1,fun he=>hd he.1,fun he=>hd he.1⟩

theorem close_preserves_pending (laws : Laws) (s : State)
    (h : s.portMode=.read ∨ s.portMode=.executing) :
    (advance laws s .close).portMode=s.portMode ∧
    core (advance laws s .close)=core s ∧
    energy (advance laws s .close)=energy s := by
  rcases h with h|h <;> simp [advance,h,core,energy]

def nativeWord (r : Bool) (c : Channel) : List Event :=
  [.pay,.returnNative r,.readNative c,.writeNative]

theorem faithful_native_update (laws : Laws) (s : State) (r : Bool) :
    (run laws s (nativeWord r .faithful)).n=(if s.updates then update s.n (!r) else s.n) ∧
    (run laws s (nativeWord r .faithful)).count=s.count+1 := by
  by_cases h0:s.count=0 <;> by_cases h1:s.count=1 <;>
    simp [run,nativeWord,advance,withSource,withFuel,setCore,source,h0,h1]

theorem missing_is_not_false_update (laws : Laws) (s : State) (r : Bool) :
    (run laws s (nativeWord r .missing)).n=s.n ∧
    (run laws s (nativeWord r .missing)).count=s.count+1 := by
  by_cases h0:s.count=0 <;> by_cases h1:s.count=1 <;>
    simp [run,nativeWord,advance,withSource,withFuel,setCore,source,h0,h1]

theorem native_word_charge (laws : Laws) (s : State) (r : Bool) (c : Channel) :
    spent laws s (nativeWord r c)=4 := by rfl

theorem paid_native_word_ledger {laws : Laws} {s t : State} {r : Bool} {c : Channel}
    (h : Generative.Trace (process laws) s (nativeWord r c) t) : energy t+4=energy s := by
  have hh:=trace_energy h
  rw [native_word_charge] at hh
  exact hh

theorem step_capacity {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) (hn : s.n≤7) (hc : s.count≤3) : t.n≤7 ∧ t.count≤3 := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | writeNative =>
      have hb:=he.2.1
      constructor
      · simp only [advance]
        split
        · exact update_bounded hn _
        · exact hn
      · change s.count+1≤3
        omega
  | returnNative b =>
      by_cases h0:s.count=0 <;> by_cases h1:s.count=1 <;>
        simp [advance,withSource,withFuel,setCore,h0,h1,hn,hc]
  | _ => exact ⟨hn,hc⟩

theorem trace_capacity {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) (hn : s.n≤7) (hc : s.count≤3) : t.n≤7 ∧ t.count≤3 := by
  induction h with
  | nil => exact ⟨hn,hc⟩
  | cons he _ ih =>
      have hh:=step_capacity he hn hc
      exact ih hh.1 hh.2

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

#print axioms AcquiredEvaluation.energy_with_fuel
#print axioms AcquiredEvaluation.old_energy
#print axioms AcquiredEvaluation.step_energy
#print axioms AcquiredEvaluation.trace_energy
#print axioms AcquiredEvaluation.step_material
#print axioms AcquiredEvaluation.trace_material
#print axioms AcquiredEvaluation.native_operation_shortfall
#print axioms AcquiredEvaluation.known_command_meaning
#print axioms AcquiredEvaluation.trace_trial_projects
#print axioms AcquiredEvaluation.current_selected_trial_effect

#print axioms AcquiredEvaluation.assessment_exact
#print axioms AcquiredEvaluation.unsupported_blocks_assessment
#print axioms AcquiredEvaluation.mismatched_command_blocks_assessment
#print axioms AcquiredEvaluation.started_command_is_current
#print axioms AcquiredEvaluation.context_interleaving_does_not_close
#print axioms AcquiredEvaluation.replacement_cannot_repeat
#print axioms AcquiredEvaluation.completed_opportunity_no_new_read
#print axioms AcquiredEvaluation.close_preserves_pending
#print axioms AcquiredEvaluation.faithful_native_update
#print axioms AcquiredEvaluation.missing_is_not_false_update
#print axioms AcquiredEvaluation.native_word_charge
#print axioms AcquiredEvaluation.paid_native_word_ledger
#print axioms AcquiredEvaluation.step_capacity
#print axioms AcquiredEvaluation.trace_capacity
