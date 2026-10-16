import ActionWitness
import PublicationBridge
import RevisionPreparation

/- One continuing physical core. Bank is storage and bounded query metadata,
not a second physical world. view is a lens used to reuse the accepted archive
law. The old world's records/context/pointer remain historical backing. -/
namespace FreshRevision

open RecipientAction (Archive)
open RecipientCorrection (Laws lookup packedAct)

structure Bank where
  budget : Nat
  escrow : Nat
  blanks : Nat
  records : Nat → Option RecipientArchive.Frame
  phase : EmissionArchive.Phase RecipientArchive.Header RecipientArchive.Frame
  next : Nat
  current : Option Nat
  live : Bool

structure State where
  parent : RecipientAction.State
  bank : Bank
  adapter : Bool
  cells : Nat
  freeA : Nat
  freeH : Nat
  actorReserve : Nat
  readerReserve : Nat
  sourceReserve : Nat
  opened : Bool
  reading : Bool

def core (s : State) := RecipientAction.core s.parent

def view (s : State) : Archive :=
  ⟨⟨core s,true,s.bank.next,s.bank.current,s.bank.live⟩,
    s.bank.budget,s.bank.escrow,s.bank.blanks,s.bank.records,s.bank.phase⟩

def setView (s : State) (a : Archive) : State :=
  { s with parent := { RecipientAction.setCore s.parent a.world.core with       reasons := { (RecipientAction.setCore s.parent a.world.core).reasons with         reader := { (RecipientAction.setCore s.parent a.world.core).reasons.reader with archive:=a.records } },       latch:=none,imported:=none },     bank:=⟨a.budget,a.escrow,a.blanks,a.records,a.phase,a.world.next,a.world.current,a.world.live⟩ }

def backing : Nat → Bool := fun i=>i=1

def producer (laws : Laws) := RecipientArchive.producer laws backing

def energy (s : State) : Nat := RecipientAction.energy s.parent+s.bank.budget+s.bank.escrow+
  s.actorReserve+s.readerReserve+s.sourceReserve

def material (s : State) : Nat := RecipientAction.material s.parent+2*s.cells+
  2*(if s.adapter then 1 else 0)+s.freeA+s.freeH

def fund (s : State) : State :=
  { s with parent := RecipientAction.setCore s.parent { core s with       hardware := { (core s).hardware with fuel:=(core s).hardware.fuel+s.actorReserve },       packets := (core s).packets+s.sourceReserve/10 },     actorReserve:=0,sourceReserve:=s.sourceReserve%10 }

def Openable (s : State) : Prop := s.adapter=true ∧ s.opened=false ∧
  (core s).phase=.ready ∧ (core s).active=true ∧ s.parent.scope=true ∧ 2≤(core s).hardware.fuel

def opening (s : State) : State :=
  let p:=RecipientAction.setCore s.parent { core s with     hardware:={ (core s).hardware with fuel:=(core s).hardware.fuel-2,last:=false } }
  let r:=PaidRecipientReasons.advance p.reasons .cold
  { s with parent:={ p with reasons:={ r with reader:={ r.reader with       archive:=s.bank.records,currentContext:=true } },latch:=none,imported:=none },     bank:={ s.bank with next:=0,current:=none,live:=true },opened:=true }

/- Funding and reset are one guarded opening transaction. fund is only its
accounting factorization, not an independent enabled event: failed admission
leaves all protected compartments untouched. -/
def OpenStep (s t : State) : Prop := Openable (fund s) ∧ t=opening (fund s)

def BankGuard (s : State) : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header → Prop
  | .bind i _ => i=1 ∧ 4≤s.cells
  | .write => True
  | .core (.contextChange _) _ => False
  | .core (.core e) _ => RecipientAction.RecipientOnly s.parent e ∧
      (RecipientAction.Settlement s.parent e ∨
        (s.parent.scope=true ∧ s.parent.permission=true ∧ s.parent.delivery=true)) ∧
      (e=.sense .recipient → s.bank.next<2)

def bankAdvance (laws : Laws) (s : State)
    (e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header) : State :=
  setView s (EmissionArchive.advance (producer laws) (view s) e)

def BankStep (laws : Laws) (s : State)
    (e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header) (t : State) : Prop :=
  s.opened=true ∧ s.reading=false ∧ BankGuard s e ∧
  EmissionArchive.Step (producer laws) 3 (view s) e (EmissionArchive.advance (producer laws) (view s) e) ∧
  t=bankAdvance laws s e

def bankProcess (laws : Laws) := Generative.Process.mk (BankStep laws)

/- Lock the bank before reusing the one existing reader. No world or bank is
copied into a new physical carrier. The equality to initial below requires
that the inherited workspace is actually present. -/
def prepareConsumer (s : State) : State :=
  let r:=PaidRecipientReasons.advance s.parent.reasons .cold
  { s with parent:={s.parent with reasons:={r with reader:={r.reader with       archive:=s.bank.records,currentContext:=true,fuel:=r.reader.fuel+s.readerReserve}},       latch:=none,imported:=none},readerReserve:=0,reading:=true }

def PrepareStep (s t : State) : Prop :=
  s.opened=true ∧ s.reading=false ∧ t=prepareConsumer s

def consumerReader (s : State) : PaidArchiveReader.State Archive :=
  PaidArchiveReader.initial s.parent.reasons.reader.world s.bank.records true
    (s.parent.reasons.reader.fuel+s.readerReserve)

def actionAdvance (laws : Laws) (s : State) (e : RecipientAction.Event) : State :=
  {s with parent:=RecipientAction.advance laws s.parent e}

def ActionStep (laws : Laws) (s : State) (e : RecipientAction.Event) (t : State) : Prop :=
  s.opened=true ∧ s.reading=true ∧ RecipientAction.Step laws s.parent e t.parent ∧
    t=actionAdvance laws s e

def actionProcess (laws : Laws) := Generative.Process.mk (ActionStep laws)

theorem core_is_unique (s : State) : (view s).world.core=RecipientAction.core s.parent := rfl

theorem view_set (s : State) (a : Archive) (hc : a.world.context=true) : view (setView s a)=a := by
  cases s; cases a; rename_i w b e n r p; cases w
  simp_all [view,setView,core,RecipientAction.core,RecipientAction.setCore]

theorem set_preserves_old_backing (s : State) (a : Archive) :
    (setView s a).parent.reasons.reader.world.records=s.parent.reasons.reader.world.records ∧
    (setView s a).parent.reasons.reader.world.world.context=s.parent.reasons.reader.world.world.context ∧
    (setView s a).parent.reasons.reader.world.world.next=s.parent.reasons.reader.world.world.next := ⟨rfl,rfl,rfl⟩

theorem opening_preserves_commands_and_history (s : State) :
    (core (opening s)).hardware.q=(core s).hardware.q ∧
    (core (opening s)).hardware.last=false ∧ (core (opening s)).phase=(core s).phase ∧
    (core (opening s)).escrow=(core s).escrow ∧ (core (opening s)).active=(core s).active ∧
    (opening s).parent.reasons.reader.world.records=s.parent.reasons.reader.world.records ∧
    (opening s).parent.reasons.reader.world.world.next=s.parent.reasons.reader.world.world.next ∧
    (opening s).parent.reasons.current=false ∧ (opening s).parent.latch=none ∧
    (opening s).parent.imported=none := ⟨rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem opening_is_not_repair (s : State) :
    ((core s).active=false → ¬Openable s) ∧ ((core s).phase≠.ready → ¬Openable s) := by
  constructor
  · intro bad h
    exact Bool.noConfusion (bad.symm.trans h.2.2.2.1)
  · intro bad h; exact bad h.2.2.1

theorem funding_conserves (s : State) : energy (fund s)=energy s ∧ material (fund s)=material s := by
  constructor
  · simp [energy,fund,core,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,
      RecipientIdentification.energy,PaidRecipientReasons.energy]; omega
  · rfl

theorem opening_paid (s : State) (h : Openable s) :
    energy (opening s)+2=energy s ∧ material (opening s)=material s := by
  constructor
  · have hf:=h.2.2.2.2.2
    simp [opening,energy,core,RecipientAction.energy,RecipientAction.core,RecipientAction.setCore,
      RecipientIdentification.energy,PaidRecipientReasons.advance,PaidRecipientReasons.energy] at *
    omega
  · rfl

theorem bank_context {laws : Laws} {s t : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (h : BankStep laws s e t) :
    (EmissionArchive.advance (producer laws) (view s) e).world.context=true := by
  cases e with
  | bind i hd => rfl
  | write =>
      exact congrArg (fun w:RecipientArchive.World=>w.context)
        (EmissionArchive.write_preserves_world (producer laws) (view s))
  | core e w =>
      cases e with
      | contextChange c => exact False.elim h.2.2.1
      | core e =>
          have hh:=h.2.2.2.1.2.1.2
          rw [hh]
          rfl

theorem bank_step_projects {laws : Laws} {s t : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (h : BankStep laws s e t) : EmissionArchive.Step (producer laws) 3 (view s) e (view t) := by
  have hc:=bank_context h
  rcases h with ⟨_,_,_,he,rfl⟩
  simpa only [bankAdvance,view_set _ _ hc] using he

theorem bank_trace_projects {laws : Laws} {s t : State}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (h : Generative.Trace (bankProcess laws) s es t) :
    Generative.Trace (EmissionArchive.process (producer laws) 3) (view s) es (view t) := by
  induction h with
  | nil => exact .nil _
  | cons he _ ih => exact .cons (bank_step_projects he) ih

theorem bank_step_pointer {laws : Laws} {s t : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (hn : s.bank.next≤2) (h : BankStep laws s e t) : t.bank.next≤2 := by
  rcases h with ⟨_,_,hg,he,rfl⟩
  cases e with
  | bind i hd => exact hn
  | write =>
      simpa only [bankAdvance,setView,EmissionArchive.write_preserves_world,view] using hn
  | core e w =>
      cases e with
      | contextChange c => exact False.elim hg
      | core e =>
          have hw:=he.2.1.2
          simp only [bankAdvance,EmissionArchive.advance,setView]
          rw [hw]
          by_cases hs:e=.sense .recipient
          · have hh:=hg.2.2 hs
            simp [RecipientArchive.advance,hs,view]; omega
          · simpa [RecipientArchive.advance,hs,view] using hn

theorem bank_trace_pointer {laws : Laws} {s t : State}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (hn : s.bank.next≤2) (h : Generative.Trace (bankProcess laws) s es t) : t.bank.next≤2 := by
  induction h with
  | nil => exact hn
  | cons he _ ih => exact ih (bank_step_pointer hn he)

theorem prepare_conserves (s : State) : energy (prepareConsumer s)=energy s ∧
    material (prepareConsumer s)=material s := by
  constructor
  · simp [prepareConsumer,energy,RecipientAction.energy,RecipientAction.core,
      PaidRecipientReasons.advance,PaidRecipientReasons.energy]; omega
  · rfl

theorem retained_workspace_initialization (s : State) (hw : s.parent.reasons.workspace=true) :
    (prepareConsumer s).parent.reasons=
      PaidRecipientReasons.initial (consumerReader s) s.parent.reasons.reserve := by
  simp [prepareConsumer,consumerReader,PaidRecipientReasons.advance,PaidRecipientReasons.initial,
    PaidArchiveReader.initial,hw]

theorem reader_has_actual_fresh_facts {laws : Laws} {s t : State} {w : RecipientArchive.World}
    {budget cells : Nat}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (empty : view s=EmissionArchive.empty w budget cells) (ready : w.core.phase=.ready)
    (history : Generative.Trace (bankProcess laws) s es t) :
    PaidArchiveReader.Facts (lookup laws .recipient) (consumerReader t) := by
  have hh:=bank_trace_projects history
  rw [empty] at hh
  have hs:=RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws w budget cells (RecipientArchive.ready_sound laws w ready)) hh
  intro i r hr hp hrec
  exact RecipientArchive.completed_record_sound hs hr hp hrec

theorem actual_fresh_archive_every_consumer {laws : Laws} {s t : State} {w : RecipientArchive.World}
    {budget cells : Nat}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (empty : view s=EmissionArchive.empty w budget cells) (ready : w.core.phase=.ready)
    (history : Generative.Trace (bankProcess laws) s es t)
    (workspace : t.parent.reasons.workspace=true) {G : Prop} (root : G)
    {r : PaidRecipientReasons.State Archive} {events : List PaidRecipientReasons.Event}
    (execution : Generative.Trace (PaidRecipientReasons.process Archive)
      (prepareConsumer t).parent.reasons events r) :
    PublicationBridge.Assured (lookup laws .recipient) G r := by
  rw [retained_workspace_initialization t workspace] at execution
  exact PublicationBridge.initialized_trace_assured root
    (PaidArchiveReader.initial_cache_agrees _ _ _ _)
    (reader_has_actual_fresh_facts empty ready history) execution

theorem action_step_projects {laws : Laws} {s t : State} {e : RecipientAction.Event}
    (h : ActionStep laws s e t) : RecipientAction.Step laws s.parent e t.parent := h.2.2.1

theorem action_trace_projects {laws : Laws} {s t : State} {es : List RecipientAction.Event}
    (h : Generative.Trace (actionProcess laws) s es t) :
    Generative.Trace (RecipientAction.process laws) s.parent es t.parent := by
  induction h with
  | nil => exact .nil _
  | cons he _ ih => exact .cons (action_step_projects he) ih


def overhead (s : State) : Nat := s.parent.reasons.reader.world.budget+
  s.parent.reasons.reader.world.escrow+PaidRecipientReasons.energy s.parent.reasons+
  s.parent.commandReserve+s.parent.readerReserve+s.parent.sourceReserve+
  s.actorReserve+s.readerReserve+s.sourceReserve

theorem energy_decomposition (laws : Laws) (s : State) :
    energy s=EmissionArchive.energy (producer laws) (view s)+overhead s := by
  simp [energy,RecipientAction.energy,overhead,EmissionArchive.energy,producer,
    RecipientArchive.producer,view,core]; omega

theorem bank_step_energy {laws : Laws} {s t : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (h : BankStep laws s e t) :
    energy t+EmissionArchive.charge (producer laws) (view s) e=energy s := by
  have hh:=EmissionArchive.step_energy (bank_step_projects h)
  have ho:overhead t=overhead s := by rw [h.2.2.2.2]; rfl
  rw [energy_decomposition laws t,energy_decomposition laws s,ho]
  omega

theorem bank_step_material {laws : Laws} {s t : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (h : BankStep laws s e t) : material t=material s := by rw [h.2.2.2.2]; rfl

theorem bank_trace_keeps_old_backing {laws : Laws} {s t : State}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (h : Generative.Trace (bankProcess laws) s es t) :
    t.parent.reasons.reader.world.records=s.parent.reasons.reader.world.records ∧
    t.parent.reasons.reader.world.world.next=s.parent.reasons.reader.world.world.next ∧
    t.parent.reasons.reader.world.world.context=s.parent.reasons.reader.world.world.context := by
  induction h with
  | nil => exact ⟨rfl,rfl,rfl⟩
  | cons he _ ih =>
      rcases he with ⟨_,_,_,_,rfl⟩
      exact ⟨ih.1,ih.2.1,ih.2.2⟩

theorem action_step_energy {laws : Laws} {s t : State} {e : RecipientAction.Event}
    (h : ActionStep laws s e t) :
    energy t+RecipientAction.charge laws s.parent e=energy s := by
  have hh:=RecipientAction.step_energy h.2.2.1
  rw [h.2.2.2] at hh ⊢
  simp only [energy,actionAdvance] at *
  omega

theorem action_step_material {laws : Laws} {s t : State} {e : RecipientAction.Event}
    (h : ActionStep laws s e t) : material t=material s := by
  have hh:=RecipientAction.step_material h.2.2.1
  rw [h.2.2.2] at hh ⊢
  simp only [material,actionAdvance] at *
  rw [hh]
  rfl

/- The law at the recorded acquisition and the law at later work are separate
parameters. A local opening epoch entails no equality between them. -/
theorem fresh_reason_import_and_actual_use {observed used : Laws} {s t : State}
    {w : RecipientArchive.World} {budget cells : Nat}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (empty : view s=EmissionArchive.empty w budget cells) (ready : w.core.phase=.ready)
    (history : Generative.Trace (bankProcess observed) s es t)
    (workspace : t.parent.reasons.workspace=true) {G : Prop} (root : G)
    {p x u v : RecipientAction.State} {events : List PaidRecipientReasons.Event}
    (consumer : Generative.Trace (PaidRecipientReasons.process Archive)
      (prepareConsumer t).parent.reasons events p.reasons)
    (paidRead : Generative.Trace (RecipientAction.process used) p [.read] x)
    (install : RecipientAction.Step used x .install u) {channel : Bool}
    (execution : Generative.Trace (RecipientAction.process used) u
      ((RecipientIdentification.trial .recipient true channel).map RecipientAction.Event.execute) v)
    (stable : lookup observed .recipient=lookup used .recipient) :
    G ∧ (RecipientAction.core v).patient=(RecipientAction.core x).patient+10 ∧
    RecipientIdentification.actor (RecipientIdentification.registers (RecipientAction.core v).hardware)=
      RecipientIdentification.actor (RecipientIdentification.registers (RecipientAction.core x).hardware) := by
  have assurance:=actual_fresh_archive_every_consumer empty ready history workspace root consumer
  apply RecipientAction.paid_import_and_execution _ install execution
  intro node member
  have rx:x.reasons.working=p.reasons.working := by
    rw [RecipientAction.trace_run paidRead]; rfl
  have currentx:PaidRecipientReasons.CurrentPublication x.reasons := by
    rcases RecipientAction.imported_core_exact install with ⟨b,hb,_⟩
    exact (RecipientAction.supported_is_current hb).1
  have currentp:p.reasons.current=true := by
    rw [RecipientAction.trace_run paidRead] at currentx
    exact currentx.1
  rw [rx] at member
  have meaning:=(assurance.2.2 currentp).2.2 node member
  simpa only [stable] using meaning


theorem bank_trace_energy {laws : Laws} {s t : State}
    {es : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (h : Generative.Trace (bankProcess laws) s es t) :
    energy t+EmissionArchive.spentAlong (producer laws) (view s) es=energy s := by
  induction h with
  | nil => simp [EmissionArchive.spentAlong]
  | cons he _ ih =>
      have hp:=bank_step_projects he
      have hh:=bank_step_energy he
      simp only [EmissionArchive.spentAlong]
      rw [←hp.2.2]
      omega

theorem storage_not_refunded_or_reopened {laws : Laws} {s t : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (h : BankStep laws s e t) :
    t.parent.reasons.reader.world.budget=s.parent.reasons.reader.world.budget ∧
    t.parent.reasons.reader.world.escrow=s.parent.reasons.reader.world.escrow ∧
    t.parent.reasons.reader.world.world.current=s.parent.reasons.reader.world.world.current ∧
    t.parent.reasons.reader.world.world.live=s.parent.reasons.reader.world.world.live := by
  rw [h.2.2.2.2]
  exact ⟨rfl,rfl,rfl,rfl⟩


theorem admitted_opening_paid {s t : State} (h : OpenStep s t) :
    energy t+2=energy s ∧ material t=material s := by
  rcases h with ⟨he,rfl⟩
  have hp:=opening_paid (fund s) he
  have hf:=funding_conserves s
  exact ⟨hp.1.trans hf.1,hp.2.trans hf.2⟩

theorem no_opening_when_inherited_phase_stalled {s t : State} (h : (core s).phase≠.ready) :
    ¬OpenStep s t := by
  intro hs
  exact h hs.1.2.2.1

theorem bank_locked_after_reader_selection {laws : Laws} {s t u : State}
    {e : EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header}
    (h : PrepareStep s t) : ¬BankStep laws t e u := by
  rcases h with ⟨_,_,rfl⟩
  intro hb
  cases hb.2.1

end FreshRevision

#print axioms FreshRevision.core_is_unique
#print axioms FreshRevision.view_set
#print axioms FreshRevision.set_preserves_old_backing
#print axioms FreshRevision.opening_preserves_commands_and_history
#print axioms FreshRevision.opening_is_not_repair
#print axioms FreshRevision.funding_conserves
#print axioms FreshRevision.opening_paid
#print axioms FreshRevision.bank_context
#print axioms FreshRevision.bank_step_projects
#print axioms FreshRevision.bank_trace_projects
#print axioms FreshRevision.bank_step_pointer
#print axioms FreshRevision.bank_trace_pointer
#print axioms FreshRevision.prepare_conserves
#print axioms FreshRevision.retained_workspace_initialization
#print axioms FreshRevision.reader_has_actual_fresh_facts
#print axioms FreshRevision.actual_fresh_archive_every_consumer
#print axioms FreshRevision.action_step_projects
#print axioms FreshRevision.action_trace_projects
#print axioms FreshRevision.energy_decomposition
#print axioms FreshRevision.bank_step_energy
#print axioms FreshRevision.bank_step_material
#print axioms FreshRevision.bank_trace_keeps_old_backing
#print axioms FreshRevision.action_step_energy
#print axioms FreshRevision.action_step_material
#print axioms FreshRevision.fresh_reason_import_and_actual_use
#print axioms FreshRevision.bank_trace_energy
#print axioms FreshRevision.storage_not_refunded_or_reopened
#print axioms FreshRevision.admitted_opening_paid
#print axioms FreshRevision.no_opening_when_inherited_phase_stalled
#print axioms FreshRevision.bank_locked_after_reader_selection
