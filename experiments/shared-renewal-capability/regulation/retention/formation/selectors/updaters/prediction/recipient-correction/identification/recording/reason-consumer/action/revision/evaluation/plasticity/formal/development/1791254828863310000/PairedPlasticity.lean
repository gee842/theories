import RevisionWitness
import PlasticityPreparation

namespace PairedPlasticity
open RecipientCorrection (Laws packedAct)
set_option maxHeartbeats 4000000
set_option maxRecDepth 16384

structure Sources where
  a : Nat
  b : Nat
  c : Nat
  d : Nat
  e : Nat
  f : Nat
  deriving DecidableEq, Repr
namespace Sources
def get (s : Sources) (i : Nat) := if i=0 then s.a else if i=1 then s.b else if i=2 then s.c else if i=3 then s.d else if i=4 then s.e else s.f
def set (s : Sources) (i v : Nat) : Sources := if i=0 then {s with a:=v} else if i=1 then {s with b:=v} else if i=2 then {s with c:=v} else if i=3 then {s with d:=v} else if i=4 then {s with e:=v} else {s with f:=v}
def total (s : Sources) := s.a+s.b+s.c+s.d+s.e+s.f
theorem set_account (s : Sources) (i v : Nat) : (set s i v).total+s.get i=s.total+v := by
  by_cases h0:i=0 <;> by_cases h1:i=1 <;> by_cases h2:i=2 <;> by_cases h3:i=3 <;> by_cases h4:i=4 <;>
    simp [set,get,total,h0,h1,h2,h3,h4] <;> omega
end Sources

inductive Sign where | negative | inert | positive deriving DecidableEq, Repr
def signValue : Sign → Int | .negative => -1 | .inert => 0 | .positive => 1
def conductance : Option Sign → Int | none => 0 | some a => signValue a
def occupied : Option Sign → Nat | none => 0 | some _ => 1
inductive Variant where | active | inert | gated | conventional | frozen deriving DecidableEq, Repr
inductive Phase where
  | ready | ownPaid | ownReturned | recipientPaid | recipientReturned
  | ownKnown | bothKnown | missing | settled | closed
  deriving DecidableEq, Repr
inductive PortMode where | idle | read | help | abstain | executing | consumed deriving DecidableEq, Repr
inductive Channel where | faithful | missing deriving DecidableEq, Repr

/- Exactly two reusable latch values. Phase supplies their validity/meaning.
   No outcome schedule or retained transmitted score is a runtime coordinate. -/
structure State where
  parent : FreshRevision.State
  n : Nat
  count : Nat
  phase : Phase
  ownBit : Bool
  recipientBit : Bool
  cells : Nat
  adapter : Bool
  port : Bool
  portMode : PortMode
  readCommand : Option Bool
  continuation : Bool
  variant : Variant
  updates : Bool
  link0 : Option Sign
  link1 : Option Sign
  blanks : Nat
  replacement : Nat
  retired : Nat
  idleParts : Nat
  training : Nat
  revision : Nat
  idleFuel : Nat
  ownSource : Sources
  recipientSource : Sources
  idleSource : Nat

def core (s : State) := FreshRevision.core s.parent
def setCore (s : State) (c : RecipientIdentification.State) : State :=
  {s with parent:={s.parent with parent:=RecipientAction.setCore s.parent.parent c}}
def fuel (s : State) := (core s).hardware.fuel
def patient (s : State) := (core s).patient
def withBalances (s : State) (f p : Nat) := setCore s {core s with hardware:={(core s).hardware with fuel:=f},patient:=p}
def withFuel (s : State) (f : Nat) := withBalances s f (patient s)
def update (n : Nat) (loss : Bool) := n/2+(if loss then 4 else 0)
def receipt (returns : Bool) : Nat := if returns then 2 else 0
def transfer (s : State) := if s.count<4 then min 6 s.training else if s.count=4 then min 7 s.revision else min 5 s.revision
def limit (s : State) := if s.continuation then 6 else 4
def current (s : State) : Prop := PaidRecipientReasons.CurrentPublication s.parent.parent.reasons
instance (s : State) : Decidable (current s) := by unfold current; infer_instance
def command (s : State) : Option Bool :=
  if current s ∧ s.parent.parent.scope=true then RecipientAction.route s.parent.parent.reasons.working else none
def Known (s : State) : Prop := command s=some (packedAct (core s).hardware.q .recipient)
def Admitted (s : State) : Prop := s.parent.opened=true ∧ s.parent.reading=true ∧ current s ∧
  (core s).phase=.ready ∧ (core s).active=true ∧ s.parent.parent.scope=true ∧ s.cells=8 ∧ s.adapter=true
def CanStart (s : State) : Prop := Known s ∧ s.parent.parent.scope=true ∧
  s.parent.parent.permission=true ∧ s.parent.parent.delivery=true ∧ (core s).phase=.ready ∧ 0<(core s).packets
instance (s : State) : Decidable (Known s) := by unfold Known; infer_instance
instance (s : State) : Decidable (Admitted s) := by unfold Admitted; infer_instance
instance (s : State) : Decidable (CanStart s) := by unfold CanStart; infer_instance

def learnedSign (s : State) : Sign := if s.variant=.inert then .inert else if s.ownBit then .positive else .negative
def replacementSign (s : State) : Sign := if s.variant=.frozen then s.link0.getD .inert else learnedSign s
def rawTransmission (s : State) : Int := (s.n:Int)*(conductance s.link0+conductance s.link1)
def transmission (s : State) : Int := if s.variant=.gated then 0 else rawTransmission s
def help (s : State) : Bool := decide (64<10*transmission s)
def conventional (s : State) : Bool := decide (64<10*(s.n:Int)*(conductance s.link0+conductance s.link1))
def invalidate (s : State) : State := {s with portMode:=.consumed,readCommand:=none}
def old (laws : Laws) (s : State) (e : RecipientAction.Event) : State :=
  {s with parent:=FreshRevision.actionAdvance laws s.parent e}

inductive Event where
  | ownPay | ownReturn (returns : Bool) | recipientPay | recipientReturn (returns : Bool)
  | ownRead (channel : Channel) | recipientRead (channel : Channel)
  | skip | bind | replace | nativeWrite | close
  | read | assess | attempt | abstain
  | trial (e : RecipientIdentification.Event)
  | reason (e : PaidRecipientReasons.Event)
  | scope (v : Bool) | permission (v : Bool) | delivery (v : Bool)
  deriving DecidableEq, Repr

def advance (laws : Laws) (s : State) : Event → State
  | .ownPay =>
      let t:=withFuel s (fuel s+transfer s-2)
      {t with training:=(if s.count<4 then s.training-transfer s else s.training), revision:=(if s.count<4 then s.revision else s.revision-transfer s),phase:=.ownPaid, portMode:=.idle,readCommand:=none}
  | .ownReturn b => {withFuel s (fuel s+receipt b) with ownSource:=s.ownSource.set s.count (s.ownSource.get s.count-receipt b),ownBit:=b,phase:=.ownReturned}
  | .recipientPay => {withBalances s (fuel s) (patient s-2) with phase:=.recipientPaid}
  | .recipientReturn b => {withBalances s (fuel s) (patient s+receipt b) with recipientSource:=s.recipientSource.set s.count (s.recipientSource.get s.count-receipt b),recipientBit:=b,phase:=.recipientReturned}
  | .ownRead c => {withFuel s (fuel s-1) with ownBit:=(if c=.faithful then !s.ownBit else false),phase:=(if c=.faithful then .ownKnown else .missing)}
  | .recipientRead c => {withFuel s (fuel s-1) with recipientBit:=(if c=.faithful then !s.recipientBit else false),phase:=(if c=.faithful then .bothKnown else .missing)}
  | .skip => {s with phase:=.settled}
  | .bind => {withFuel s (fuel s-1) with link0:=(if s.link0=none then some (learnedSign s) else s.link0),link1:=(if s.link0=none then s.link1 else some (learnedSign s)),blanks:=s.blanks-1,phase:=.settled}
  | .replace => {withFuel s (fuel s-2) with link0:=some (replacementSign s),replacement:=s.replacement-1,retired:=s.retired+1,phase:=.settled}
  | .nativeWrite => {withFuel s (fuel s-1) with n:=(if s.updates then update s.n s.ownBit else s.n),count:=s.count+1,ownBit:=false,recipientBit:=false,phase:=.ready}
  | .close => {s with phase:=.closed}
  | .read => {withFuel s (fuel s-1) with readCommand:=(if Known s then command s else none),portMode:=(if Known s then .read else .consumed)}
  | .assess => {withFuel s (fuel s-1) with portMode:=(if help s then .help else .abstain)}
  | .attempt => {s with portMode:=(if CanStart s then .executing else .consumed)}
  | .abstain => invalidate s
  | .trial e => let t:=old laws s (.voluntary e)
                if e=.write ∨ e=.miss then invalidate t else t
  | .reason e => {old laws s (.reason e) with portMode:=(if s.portMode=.idle then .idle else .consumed),readCommand:=none}
  | .scope v => {old laws s (.setScope v) with portMode:=(if s.portMode=.idle then .idle else .consumed),readCommand:=none}
  | .permission v => old laws s (.setPermission v)
  | .delivery v => old laws s (.setDelivery v)

def Enabled (s : State) : Event → Prop
  | .ownPay => Admitted s ∧ s.phase=.ready ∧ s.count<limit s ∧ s.count<6 ∧
      2≤s.ownSource.get s.count ∧ 2≤s.recipientSource.get s.count ∧ 2≤patient s ∧ 2≤fuel s+transfer s
  | .ownReturn b => s.phase=.ownPaid ∧ receipt b≤s.ownSource.get s.count
  | .recipientPay => s.phase=.ownReturned ∧ 2≤patient s
  | .recipientReturn b => s.phase=.recipientPaid ∧ receipt b≤s.recipientSource.get s.count
  | .ownRead _ => s.phase=.recipientReturned ∧ 1≤fuel s
  | .recipientRead _ => s.phase=.ownKnown ∧ 1≤fuel s
  | .skip => s.phase=.bothKnown ∧ s.recipientBit=false
  | .bind => s.phase=.bothKnown ∧ s.recipientBit=true ∧ s.count<4 ∧
      (s.link0=none ∨ s.link1=none) ∧ 1≤s.blanks ∧ 1≤fuel s
  | .replace => s.phase=.bothKnown ∧ s.recipientBit=true ∧ 4≤s.count ∧ s.count<6 ∧
      s.continuation=true ∧ s.link0≠none ∧ s.link1≠none ∧ 1≤s.replacement ∧ 2≤fuel s
  | .nativeWrite => s.phase=.settled ∧ s.count<limit s ∧ s.count<6 ∧ 1≤fuel s
  | .close => s.phase=.ready ∧ s.count=limit s
  | .read => s.phase=.closed ∧ s.port=true ∧ s.portMode=.idle ∧ s.cells=8 ∧ s.adapter=true ∧
      (core s).phase=.ready ∧ 1≤fuel s
  | .assess => s.portMode=.read ∧ Known s ∧ s.readCommand=command s ∧ 1≤fuel s
  | .attempt => s.port=true ∧ s.portMode=.help
  | .abstain => s.portMode=.abstain
  | .trial e => RecipientAction.Enabled s.parent.parent (.voluntary e) ∧
      (RecipientAction.Settlement s.parent.parent e ∨ (s.portMode=.executing ∧ Known s))
  | .reason e => RecipientAction.Enabled s.parent.parent (.reason e)
  | .scope _ | .permission _ | .delivery _ => True
instance (s : State) (e : Event) : Decidable (Enabled s e) := by cases e <;> unfold Enabled <;> infer_instance

def Step (laws : Laws) (s : State) (e : Event) (t : State) := Enabled s e ∧ t=advance laws s e
def process (laws : Laws) : Generative.Process State Event := ⟨Step laws⟩
def energy (s : State) := FreshRevision.energy s.parent+s.training+s.revision+s.idleFuel+s.ownSource.total+s.recipientSource.total+s.idleSource
def material (s : State) := FreshRevision.material s.parent+2*s.cells+
  2*(if s.adapter then 1 else 0)+2*(if s.port then 1 else 0)+
  2*(occupied s.link0+occupied s.link1+s.blanks+s.replacement+s.retired+s.idleParts)
def charge (laws : Laws) (s : State) : Event → Nat
  | .ownPay | .recipientPay | .replace => 2
  | .ownRead _ | .recipientRead _ | .bind | .nativeWrite | .read | .assess => 1
  | .trial e => RecipientAction.charge laws s.parent.parent (.voluntary e)
  | .reason e => RecipientAction.charge laws s.parent.parent (.reason e)
  | _ => 0
def run (laws : Laws) (s : State) : List Event → State
  | [] => s
  | e::es => run laws (advance laws s e) es
def spent (laws : Laws) (s : State) : List Event → Nat
  | [] => 0
  | e::es => charge laws s e+spent laws (advance laws s e) es
def Runnable (laws : Laws) (s : State) : List Event → Prop
  | [] => True
  | e::es => Enabled s e ∧ Runnable laws (advance laws s e) es
instance runnableDecidable (laws : Laws) (s : State) (es : List Event) : Decidable (Runnable laws s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => let _:=runnableDecidable laws (advance laws s e) es
            inferInstanceAs (Decidable (Enabled s e ∧ Runnable laws (advance laws s e) es))

theorem runnable_trace {laws : Laws} {s : State} {es : List Event} (h : Runnable laws s es) :
    Generative.Trace (process laws) s es (run laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih h.2)
theorem update_bounded {n : Nat} (h : n≤7) (b : Bool) : update n b≤7 := by
  cases b <;> simp [update] <;> omega
theorem transmission_bounded {s : State} (h : s.n≤7) : -14≤rawTransmission s ∧ rawTransmission s≤14 := by
  cases h0:s.link0 with
  | none => cases h1:s.link1 with
    | none => simp [rawTransmission,h0,h1,conductance]
    | some a => cases a <;> simp [rawTransmission,h0,h1,conductance,signValue] <;> omega
  | some a => cases a <;> cases h1:s.link1 with
    | none => simp [rawTransmission,h0,h1,conductance,signValue] <;> omega
    | some b => cases b <;> simp [rawTransmission,h0,h1,conductance,signValue] <;> omega

theorem conventional_equality (s : State) : help {s with variant:=.conventional}=conventional s := by
  simp [help,transmission,rawTransmission,conventional,Int.mul_assoc]

theorem balances_account (s : State) (f p : Nat) :
    energy (withBalances s f p)+fuel s+patient s=energy s+f+p := by
  simp [energy,withBalances,setCore,core,fuel,patient,FreshRevision.energy,FreshRevision.core,
    RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,RecipientIdentification.energy,PaidRecipientReasons.energy]
  omega

theorem old_account {laws : Laws} {s : State} {e : RecipientAction.Event}
    (h : RecipientAction.Enabled s.parent.parent e) :
    energy (old laws s e)+RecipientAction.charge laws s.parent.parent e=energy s := by
  have hh:=RecipientAction.step_energy (show RecipientAction.Step laws s.parent.parent e _ from ⟨h,rfl⟩)
  simp only [energy,old,FreshRevision.actionAdvance,FreshRevision.energy]
  omega

theorem fuel_account (s : State) (f : Nat) : energy (withFuel s f)+fuel s=energy s+f := by
  have h:=balances_account s f (patient s)
  change energy (withFuel s f)+fuel s+patient s=energy s+f+patient s at h
  omega

theorem step_energy {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : energy t+charge laws s e=energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | ownPay =>
      have hb:=fuel_account s (fuel s+transfer s-2)
      have hf:=he.2.2.2.2.2.2.2
      have ht : (if s.count<4 then transfer s≤s.training else transfer s≤s.revision) := by
        by_cases h : s.count<4
        · simp only [transfer,h,ite_true]; exact Nat.min_le_right _ _
        · simp only [transfer,h,ite_false]; split <;> exact Nat.min_le_right _ _
      by_cases hc:s.count<4
      all_goals simp only [advance,energy,charge,withFuel,hc,ite_true,ite_false] at hb ht ⊢
      all_goals omega
  | ownReturn b =>
      have hs:=Sources.set_account s.ownSource s.count (s.ownSource.get s.count-receipt b)
      have hb:=fuel_account s (fuel s+receipt b)
      have hf:=he.2
      simp only [advance,energy,charge,withFuel] at hb ⊢
      omega
  | recipientReturn b =>
      have hs:=Sources.set_account s.recipientSource s.count (s.recipientSource.get s.count-receipt b)
      have hb:=balances_account s (fuel s) (patient s+receipt b)
      have hf:=he.2
      simp only [advance,energy,charge] at hb ⊢
      omega
  | recipientPay =>
      have hb:=balances_account s (fuel s) (patient s-2)
      have hf:=he.2
      simp only [advance,energy,charge] at hb ⊢
      omega
  | ownRead c | recipientRead c | bind | nativeWrite | read | assess =>
      have hb:=fuel_account s (fuel s-1)
      simp only [Enabled] at he
      simp only [advance,energy,charge,withFuel] at hb ⊢
      all_goals omega
  | replace =>
      have hb:=fuel_account s (fuel s-2)
      have hf:=he.2.2.2.2.2.2.2.2
      simp only [advance,energy,charge,withFuel] at hb ⊢
      omega
  | trial e =>
      have hh:=old_account (laws:=laws) he.1
      simp only [advance,charge]
      split <;> exact hh
  | reason e => exact old_account he
  | scope v => exact old_account (e:=.setScope v) trivial
  | permission v => exact old_account (e:=.setPermission v) trivial
  | delivery v => exact old_account (e:=.setDelivery v) trivial
  | skip | close | attempt | abstain => rfl

theorem trace_energy {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : energy t+spent laws s es=energy s := by
  induction h with
  | nil => simp [spent]
  | cons he _ ih =>
      have hh:=step_energy he
      rcases he with ⟨_,rfl⟩
      simp only [spent]; omega

theorem step_material {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : material t=material s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | bind =>
      have hf:=he.2.2.2.2.1
      have hole:=he.2.2.2.1
      cases h0:s.link0 <;> cases h1:s.link1 <;>
        simp [advance,material,withFuel,withBalances,setCore,FreshRevision.material,RecipientAction.material,RecipientAction.setCore,occupied,h0,h1] at * <;> omega
  | replace =>
      have hf:=he.2.2.2.2.2.2.2.1
      have hl:=he.2.2.2.2.2.1
      cases h0:s.link0 <;>
        simp [advance,material,withFuel,withBalances,setCore,FreshRevision.material,RecipientAction.material,RecipientAction.setCore,occupied,h0] at * <;> omega
  | trial e => cases e <;> rfl
  | _ => rfl

theorem trace_material {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : material t=material s := by
  induction h with
  | nil => rfl
  | cons he _ ih => exact ih.trans (step_material he)

theorem step_capacity {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) (hn : s.n≤7) (hc : s.count≤6) : t.n≤7 ∧ t.count≤6 := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | nativeWrite =>
      simp only [advance,withFuel,withBalances,setCore]
      constructor
      · split <;> first | exact update_bounded hn _ | exact hn
      · have hh:=he.2.2.1; omega
  | trial e => cases e <;> exact ⟨hn,hc⟩
  | _ => exact ⟨hn,hc⟩

theorem trace_capacity {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) (hn : s.n≤7) (hc : s.count≤6) : t.n≤7 ∧ t.count≤6 := by
  induction h with
  | nil => exact ⟨hn,hc⟩
  | cons he _ ih => have hh:=step_capacity he hn hc; exact ih hh.1 hh.2

theorem binding_uses_acquired_pair {s : State} (h : Enabled s .bind) :
    s.phase=.bothKnown ∧ s.recipientBit=true ∧
    (learnedSign {s with variant:=.active}=.positive ↔ s.ownBit=true) := by
  refine ⟨h.1,h.2.1,?_⟩
  cases s.ownBit <;> simp [learnedSign]
theorem no_second_binding (laws : Laws) (s : State) :
    ¬Enabled (advance laws s .bind) .bind ∧ ¬Enabled (advance laws s .replace) .replace := by
  constructor <;> intro h <;> cases h.1

theorem missing_is_not_acquired {s : State} (h : s.phase=.missing) :
    ¬Enabled s .bind ∧ ¬Enabled s .nativeWrite := by
  constructor <;> intro he <;> have hh:=he.1 <;> rw [h] at hh <;> cases hh

theorem no_recipient_actor_source_credit (laws : Laws) (s : State) (b : Bool) :
    fuel (advance laws s (.recipientReturn b))=fuel s ∧
    (advance laws s (.recipientReturn b)).ownSource=s.ownSource := ⟨rfl,rfl⟩

theorem trial_projects {laws : Laws} {s t : State} {e : RecipientIdentification.Event}
    (h : Step laws s (.trial e) t) : RecipientIdentification.Step laws (core s) e (core t) := by
  rcases h with ⟨he,rfl⟩
  have hh:=RecipientAction.voluntary_projects (laws:=laws) (show RecipientAction.Step laws s.parent.parent (.voluntary e) _ from ⟨he.1,rfl⟩)
  cases e <;> exact hh

theorem no_new_rent_after_consumption {s : State} (h : s.portMode=.consumed) :
    ¬Enabled s (.trial .rent) := by
  rintro ⟨_,hs|hs⟩
  · simp [RecipientAction.Settlement] at hs
  · rw [h] at hs; cases hs.1

theorem settlement_survives_scope_cut {s : State} {channel : Bool}
    (hv : RecipientIdentification.Valid (core s))
    (he : RecipientIdentification.Enabled (core s) (.acquire channel))
    (hr : RecipientIdentification.targetOf (core s).phase=.recipient) :
    Enabled s (.trial (.acquire channel)) := by
  have hs : RecipientAction.Settlement s.parent.parent (.acquire channel) := by
    rcases he with ⟨⟨target,r,hp⟩,_⟩
    have hp2 : (RecipientAction.core s.parent.parent).phase=.worked target r := hp
    simp [RecipientAction.Settlement,hp2]
  exact ⟨⟨hv,he,hr,Or.inl hs⟩,Or.inl hs⟩

theorem scope_cut_invalidates_only_application (laws : Laws) (s : State) :
    (advance laws s (.scope false)).n=s.n ∧ (advance laws s (.scope false)).link0=s.link0 ∧
    (advance laws s (.scope false)).link1=s.link1 ∧
    (advance laws s (.scope false)).parent.parent.reasons=s.parent.parent.reasons ∧
    command (advance laws s (.scope false))=none := by
  simp [advance,old,FreshRevision.actionAdvance,RecipientAction.advance,RecipientAction.clear,command]

end PairedPlasticity

#print axioms PairedPlasticity.Sources.set_account
#print axioms PairedPlasticity.runnable_trace
#print axioms PairedPlasticity.update_bounded
#print axioms PairedPlasticity.transmission_bounded
#print axioms PairedPlasticity.conventional_equality
#print axioms PairedPlasticity.balances_account
#print axioms PairedPlasticity.old_account
#print axioms PairedPlasticity.fuel_account
#print axioms PairedPlasticity.step_energy
#print axioms PairedPlasticity.trace_energy
#print axioms PairedPlasticity.step_material
#print axioms PairedPlasticity.trace_material
#print axioms PairedPlasticity.step_capacity
#print axioms PairedPlasticity.trace_capacity
#print axioms PairedPlasticity.binding_uses_acquired_pair
#print axioms PairedPlasticity.no_second_binding
#print axioms PairedPlasticity.missing_is_not_acquired
#print axioms PairedPlasticity.no_recipient_actor_source_credit
#print axioms PairedPlasticity.trial_projects
#print axioms PairedPlasticity.no_new_rent_after_consumption
#print axioms PairedPlasticity.settlement_survives_scope_cut
#print axioms PairedPlasticity.scope_cut_invalidates_only_application
