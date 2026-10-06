import SuccessionWitness

namespace ApplicationEvidence
open PaidRecipientReasons
set_option maxRecDepth 16384
set_option maxHeartbeats 2000000

/-- A property of accessible archive bytes, not an invented fulfillment flag. -/
def PositiveFrame (reader : PaidArchiveReader.State W) (i : Nat) (r : RecipientArchive.Frame) : Prop :=
  i<3 ∧ reader.archive i=some r ∧ r.context=reader.currentContext ∧
  r.present=true ∧ r.receipt=true

theorem decode_has_positive_frame {x : Option RecipientArchive.Frame} {c d b : Bool}
    (h : RecipientArchive.decode c d x=some b) :
    ∃ r, x=some r ∧ r.context=c ∧ r.present=true ∧ r.receipt=true := by
  cases x with
  | none => cases h
  | some r =>
    simp only [RecipientArchive.decode] at h
    split at h
    · rename_i hp
      simp only [Bool.and_eq_true,beq_iff_eq] at hp
      exact ⟨r,rfl,hp.1.1,hp.1.2,hp.2⟩
    · contradiction

theorem normalize_nonempty {d : Bool} {x : Option Bool}
    (h : RecipientReasons.normalize d x≠none) : ∃ b,x=some b := by
  cases x with
  | none => exact False.elim (h rfl)
  | some b => exact ⟨b,rfl⟩

theorem empty_closure_has_no_command :
    RecipientAction.route (ReasonReplay.closureMask RecipientReasons.star
      (RecipientReasons.derived RecipientReasons.empty))=none := by decide

theorem supported_normalized_nonempty {s : State W} {z command : Bool}
    (hi : PublicationSafety.Invariant z s) (hc : CurrentPublication s)
    (hs : RecipientAction.route s.working=some command) :
    s.normalized.first≠none ∨ s.normalized.second≠none ∨ s.normalized.third≠none := by
  by_cases ha:s.normalized.first=none
  · by_cases hb:s.normalized.second=none
    · by_cases hd:s.normalized.third=none
      · have hn : s.normalized=RecipientReasons.empty := by
          cases he:s.normalized with
          | mk a b c => simp_all [RecipientReasons.empty]
        have hw:=PublicationSafety.invariant_publication_exact hi hc
        rw [hw,hn,empty_closure_has_no_command] at hs
        cases hs
      · exact Or.inr (Or.inr hd)
    · exact Or.inr (Or.inl hb)
  · exact Or.inl ha

theorem normalized_support_has_cache {s : State W} {z command : Bool}
    (hi : PublicationSafety.Invariant z s) (hc : CurrentPublication s)
    (hs : RecipientAction.route s.working=some command) :
    ∃ i, i<3 ∧ ∃ b,s.reader.cache i=some b := by
  have hp:s.phase≠0:=by rw [hc.2.1]; decide
  have hh:=hi.selected hp
  rcases supported_normalized_nonempty hi hc hs with h|h|h
  · rcases hh.1 with bad|good
    · exact False.elim (h bad)
    · exact ⟨0,by decide,normalize_nonempty (good ▸ h)⟩
  · rcases hh.2.1 with bad|good
    · exact False.elim (h bad)
    · exact ⟨1,by decide,normalize_nonempty (good ▸ h)⟩
  · rcases hh.2.2 with bad|good
    · exact False.elim (h bad)
    · exact ⟨2,by decide,normalize_nonempty (good ▸ h)⟩

theorem current_command_has_accessible_positive_frame {s : State W} {z command : Bool}
    (hi : PublicationSafety.Invariant z s) (hc : CurrentPublication s)
    (hs : RecipientAction.route s.working=some command) :
    ∃ i r, PositiveFrame s.reader i r := by
  rcases normalized_support_has_cache hi hc hs with ⟨i,hi3,b,hb⟩
  have hcomplete:=hc.2.2.1
  have hn:=hcomplete.2.2
  have he:=hi.cache hcomplete.1 hcomplete.2.1 i (by omega)
  have hd:RecipientArchive.decode s.reader.currentContext (RecipientArchive.designated i)
      (s.reader.archive i)=some b:=he.symm.trans hb
  rcases decode_has_positive_frame hd with ⟨r,hr,hctx,hp,hrc⟩
  exact ⟨i,r,hi3,hr,hctx,hp,hrc⟩

theorem initialized_paid_command_has_positive_frame
    {w : W} {records : Nat→Option RecipientArchive.Frame} {c : Bool} {fuel reserve : Nat}
    {z command : Bool} {t : State W} {es : List Event}
    (hf : PaidArchiveReader.Facts z (PaidArchiveReader.initial w records c fuel))
    (history : Generative.Trace (process W)
      (initial (PaidArchiveReader.initial w records c fuel) reserve) es t)
    (current : CurrentPublication t) (supported : RecipientAction.route t.working=some command) :
    (∃ i r, PositiveFrame t.reader i r) ∧ energy t+spent es=fuel+reserve := by
  have hi:=PublicationSafety.trace_invariant
    (PublicationSafety.initial_invariant _ reserve (PaidArchiveReader.initial_cache_agrees _ _ _ _) hf) history
  exact ⟨current_command_has_accessible_positive_frame hi current supported,trace_ledger history⟩

/-- Reading/reasoning may spend fuel and revise working memory; it does not replace its archive. -/
theorem paid_trace_preserves_archive {s t : State W} {es : List Event}
    (h : Generative.Trace (process W) s es t) : t.reader.archive=s.reader.archive := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact ih.trans (step_preserves_archive hs)

/-- An origin located in the actual path, with its exact before/after states. -/
def LocatedOrigin (p : EmissionArchive.Producer W E H R) (n : Nat)
    (s t : EmissionArchive.State W H R) (es : List (EmissionArchive.Event W E H))
    (i : Nat) (r : R) : Prop :=
  ∃ pre e post before after, es=pre++e::post ∧
    Generative.Trace (EmissionArchive.process p n) s pre before ∧
    EmissionArchive.Step p n before e after ∧
    Generative.Trace (EmissionArchive.process p n) after post t ∧
    (i,r)∈EmissionArchive.origin p before e

theorem trace_origin_located {p : EmissionArchive.Producer W E H R} {n : Nat}
    {s t : EmissionArchive.State W H R} {es : List (EmissionArchive.Event W E H)}
    {i : Nat} {r : R} (h : Generative.Trace (EmissionArchive.process p n) s es t)
    (ho : (i,r)∈EmissionArchive.originsAlong p s es) : LocatedOrigin p n s t es i r := by
  induction h with
  | nil => simp [EmissionArchive.originsAlong] at ho
  | @cons s m t e es hs ht ih =>
    change (i,r)∈EmissionArchive.origin p s e ++ EmissionArchive.originsAlong p (EmissionArchive.advance p s e) es at ho
    rcases List.mem_append.mp ho with now|later
    · exact ⟨[],e,es,s,m,rfl,.nil s,hs,ht,now⟩
    · have he : m=EmissionArchive.advance p s e:=hs.2.2
      rw [←he] at later
      rcases ih later with ⟨pre,f,post,before,after,hword,hpre,hstep,hpost,horigin⟩
      exact ⟨e::pre,f,post,before,after,by simp [hword],.cons hs hpre,hstep,hpost,horigin⟩

theorem stored_from_empty_has_located_origin {p : EmissionArchive.Producer W E H R}
    {n b c i : Nat} {w : W} {t : EmissionArchive.State W H R}
    {es : List (EmissionArchive.Event W E H)} {r : R}
    (h : Generative.Trace (EmissionArchive.process p n) (EmissionArchive.empty w b c) es t)
    (hs : EmissionArchive.stored t i r) :
    LocatedOrigin p n (EmissionArchive.empty w b c) t es i r :=
  trace_origin_located h (EmissionArchive.empty_trace_provenance h hs)

/-- A positive archive payload can only be emitted by actual recipient acquisition,
not by an arbitrary write or by a missing/zero observation. -/
theorem positive_emission_is_recipient_acquisition
    {h : RecipientArchive.Header} {s t : RecipientArchive.World}
    {e : RecipientArchive.Event} {r : RecipientArchive.Frame}
    (he : RecipientArchive.emission h s e t=some r)
    (hp : r.present=true) (hr : r.receipt=true) :
    e=.core (.acquire true) ∧ s.core.phase=.worked .recipient true ∧ r.context=s.context := by
  unfold RecipientArchive.emission at he
  split at he
  · rename_i guard
    simp only [Bool.and_eq_true,beq_iff_eq] at guard
    cases e with
    | contextChange c => contradiction
    | core e =>
      cases e <;> try contradiction
      case acquire channel =>
        cases hs:s.core.phase <;> simp only [hs] at he <;> try contradiction
        case worked target received =>
          cases target <;> try contradiction
          case recipient =>
            cases channel <;> cases received <;> simp_all <;> cases he <;> simp_all
  · contradiction

/-- The producer binding and positive payload have the same archived index. -/
theorem positive_origin_shape {laws : RecipientCorrection.Laws} {backing : Nat→Bool}
    {s : RecipientAction.Archive} {e : PublicationBridge.ArchiveEvent}
    {i : Nat} {r : RecipientArchive.Frame}
    (ho : (i,r)∈EmissionArchive.origin (RecipientArchive.producer laws backing) s e)
    (hp : r.present=true) (hr : r.receipt=true) :
    ∃ w h, e=.core (.core (.acquire true)) w ∧ s.phase=.bound i h ∧
      s.world.core.phase=.worked .recipient true ∧
      RecipientArchive.emission h s.world (.core (.acquire true)) w=some r ∧
      r.context=s.world.context := by
  cases e with
  | bind _ _ => simp [EmissionArchive.origin] at ho
  | write => simp [EmissionArchive.origin] at ho
  | core e w =>
    cases hs:s.phase with
    | idle => simp [EmissionArchive.origin,hs] at ho
    | latched _ _ _ => simp [EmissionArchive.origin,hs] at ho
    | bound j h =>
      simp only [EmissionArchive.origin,hs,RecipientArchive.producer] at ho
      cases he:RecipientArchive.emission h s.world e w with
      | none => simp [he] at ho
      | some x =>
        simp [he] at ho
        rcases ho with ⟨rfl,rfl⟩
        have hh:=positive_emission_is_recipient_acquisition he hp hr
        rcases hh with ⟨rfl,hphase,hctx⟩
        exact ⟨w,h,rfl,rfl,hphase,he,hctx⟩

/-- The same positive frame is accessible after the paid consumer and was actually
emitted in the separately supplied, empty-bank production history. No current
publication, assay correctness or ethical warrant is assumed at the entrance. -/
theorem initialized_production_and_publication_has_positive_origin
    {laws : RecipientCorrection.Laws} {backing : Nat→Bool} {addresses budget cells : Nat}
    {start : RecipientArchive.World} {bank : RecipientAction.Archive}
    {produced : List PublicationBridge.ArchiveEvent}
    {w : W} {context : Bool} {fuel reserve : Nat} {command : Bool}
    {t : State W} {read : List Event}
    (ready : start.core.phase=.ready)
    (production : Generative.Trace
      (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty start budget cells) produced bank)
    (consumer : Generative.Trace (process W)
      (initial (PaidArchiveReader.initial w bank.records context fuel) reserve) read t)
    (current : CurrentPublication t) (supported : RecipientAction.route t.working=some command) :
    (∃ i r, PositiveFrame t.reader i r ∧ EmissionArchive.stored bank i r ∧
      LocatedOrigin (RecipientArchive.producer laws backing) addresses
        (EmissionArchive.empty start budget cells) bank produced i r) ∧
    energy t+spent read=fuel+reserve := by
  have sound:=RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws start budget cells
      (RecipientArchive.ready_sound laws start ready)) production
  have facts : PaidArchiveReader.Facts (RecipientCorrection.lookup laws .recipient)
      (PaidArchiveReader.initial w bank.records context fuel) := by
    intro i r hr hp hrec
    exact RecipientArchive.completed_record_sound sound hr hp hrec
  rcases initialized_paid_command_has_positive_frame facts consumer current supported with ⟨⟨i,r,hp⟩,bill⟩
  have preserved:=paid_trace_preserves_archive consumer
  have stored:EmissionArchive.stored bank i r:=by
    change bank.records i=some r
    have hr:=hp.2.1
    rw [preserved] at hr
    exact hr
  exact ⟨⟨i,r,hp,stored,stored_from_empty_has_located_origin production stored⟩,bill⟩

/-- Full event-level certificate: a successful recipient acquisition, located in
its actual trace, carrying the exact frame later used by the current publication.
The preceding receipt is a physical state, not a utility or fulfillment label. -/
def AcquiredOnTrace (laws : RecipientCorrection.Laws) (backing : Nat→Bool) (addresses : Nat)
    (s t : RecipientAction.Archive) (es : List PublicationBridge.ArchiveEvent)
    (i : Nat) (r : RecipientArchive.Frame) : Prop :=
  ∃ pre post before after successor header,
    es=pre++(.core (.core (.acquire true)) successor)::post ∧
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) s pre before ∧
    EmissionArchive.Step (RecipientArchive.producer laws backing) addresses before
      (.core (.core (.acquire true)) successor) after ∧
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) after post t ∧
    before.phase=.bound i header ∧ before.world.core.phase=.worked .recipient true ∧
    RecipientArchive.emission header before.world (.core (.acquire true)) successor=some r ∧
    r.context=before.world.context

theorem located_positive_origin_is_actual_acquisition
    {laws : RecipientCorrection.Laws} {backing : Nat→Bool} {addresses i : Nat}
    {s t : RecipientAction.Archive} {es : List PublicationBridge.ArchiveEvent}
    {r : RecipientArchive.Frame}
    (origin : LocatedOrigin (RecipientArchive.producer laws backing) addresses s t es i r)
    (hp : r.present=true) (hr : r.receipt=true) :
    AcquiredOnTrace laws backing addresses s t es i r := by
  rcases origin with ⟨pre,e,post,before,after,word,hpre,step,hpost,he⟩
  rcases positive_origin_shape he hp hr with ⟨w,header,rfl,hbound,hworked,hem,hctx⟩
  exact ⟨pre,post,before,after,w,header,word,hpre,step,hpost,hbound,hworked,hem,hctx⟩

/-- A real recipient-directed work event credited ten physical units in this
producer trace. This does not yet identify an episode, service or ethical good. -/
def DeliveredOnTrace (laws : RecipientCorrection.Laws) (backing : Nat→Bool) (addresses : Nat)
    (s t : RecipientAction.Archive) (es : List PublicationBridge.ArchiveEvent) : Prop :=
  ∃ pre post before after av successor,
    es=pre++(.core (.core (.work av)) successor)::post ∧
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) s pre before ∧
    EmissionArchive.Step (RecipientArchive.producer laws backing) addresses before
      (.core (.core (.work av)) successor) after ∧
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) after post t ∧
    successor.core.patient=before.world.core.patient+10

theorem worked_step_has_delivery_or_predecessor
    {laws : RecipientCorrection.Laws} {backing : Nat→Bool} {addresses : Nat}
    {s t : RecipientAction.Archive} {e : PublicationBridge.ArchiveEvent}
    (step : EmissionArchive.Step (RecipientArchive.producer laws backing) addresses s e t)
    (worked : t.world.core.phase=.worked .recipient true) :
    s.world.core.phase=.worked .recipient true ∨
    ∃ av successor,e=.core (.core (.work av)) successor ∧
      successor.core.patient=s.world.core.patient+10 := by
  rcases step with ⟨_,hen,rfl⟩
  cases e with
  | bind i h => exact Or.inl worked
  | write =>
    rw [EmissionArchive.write_preserves_world] at worked
    exact Or.inl worked
  | core e successor =>
    change RecipientArchive.Step laws s.world e successor at hen
    rcases hen with ⟨hen,rfl⟩
    cases e with
    | contextChange c => exact Or.inl worked
    | core e =>
      rcases hen.1 with ⟨_,he,_⟩
      cases e with
      | rent => contradiction
      | sense target => contradiction
      | reserve => contradiction
      | write => contradiction
      | miss => exact Or.inl worked
      | acquire channel =>
        rcases he with ⟨⟨target,r,hphase⟩,_⟩
        simp [EmissionArchive.advance,RecipientArchive.advance,RecipientIdentification.advance,hphase] at worked
      | work av =>
        rcases he with ⟨⟨target,hphase⟩,_,_⟩
        cases target with
        | actor => simp [EmissionArchive.advance,RecipientArchive.advance,RecipientIdentification.advance,hphase,RecipientIdentification.targetOf] at worked
        | recipient =>
          have returned : RecipientIdentification.returned laws s.world.core av=true := by
            simpa [EmissionArchive.advance,RecipientArchive.advance,RecipientIdentification.advance,hphase,RecipientIdentification.targetOf] using worked
          refine Or.inr ⟨av,_,rfl,?_⟩
          simp [RecipientArchive.advance,RecipientIdentification.advance,hphase,RecipientIdentification.targetOf,
            returned,RecipientIdentification.patientCredit]

theorem worked_trace_has_delivery_or_initial_receipt
    {laws : RecipientCorrection.Laws} {backing : Nat→Bool} {addresses : Nat}
    {s t : RecipientAction.Archive} {es : List PublicationBridge.ArchiveEvent}
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) s es t)
    (worked : t.world.core.phase=.worked .recipient true) :
    s.world.core.phase=.worked .recipient true ∨ DeliveredOnTrace laws backing addresses s t es := by
  induction history with
  | nil => exact Or.inl worked
  | @cons s m t e es hs ht ih =>
    rcases ih worked with hm|later
    · rcases worked_step_has_delivery_or_predecessor hs hm with before|now
      · exact Or.inl before
      · rcases now with ⟨av,w,rfl,hcredit⟩
        exact Or.inr ⟨[],es,s,m,av,w,rfl,.nil s,hs,ht,hcredit⟩
    · rcases later with ⟨pre,post,before,after,av,w,hword,hpre,hstep,hpost,hcredit⟩
      exact Or.inr ⟨e::pre,post,before,after,av,w,by simp [hword],.cons hs hpre,hstep,hpost,hcredit⟩

/-- The identified frame's acquisition has an actual credited work event in its
own prefix. The order is explicit; a later unrelated delivery cannot fill it. -/
def AcquiredAfterDelivery (laws : RecipientCorrection.Laws) (backing : Nat→Bool) (addresses : Nat)
    (s t : RecipientAction.Archive) (es : List PublicationBridge.ArchiveEvent)
    (i : Nat) (r : RecipientArchive.Frame) : Prop :=
  ∃ pre post before after successor header,
    es=pre++(.core (.core (.acquire true)) successor)::post ∧
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) s pre before ∧
    EmissionArchive.Step (RecipientArchive.producer laws backing) addresses before
      (.core (.core (.acquire true)) successor) after ∧
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses) after post t ∧
    before.phase=.bound i header ∧ before.world.core.phase=.worked .recipient true ∧
    RecipientArchive.emission header before.world (.core (.acquire true)) successor=some r ∧
    r.context=before.world.context ∧ DeliveredOnTrace laws backing addresses s before pre

theorem ready_acquisition_has_prior_delivery
    {laws : RecipientCorrection.Laws} {backing : Nat→Bool} {addresses i : Nat}
    {s t : RecipientAction.Archive} {es : List PublicationBridge.ArchiveEvent}
    {r : RecipientArchive.Frame} (ready : s.world.core.phase=.ready)
    (acquired : AcquiredOnTrace laws backing addresses s t es i r) :
    AcquiredAfterDelivery laws backing addresses s t es i r := by
  rcases acquired with ⟨pre,post,before,after,w,h,word,hpre,step,hpost,bound,worked,emitted,context⟩
  rcases worked_trace_has_delivery_or_initial_receipt hpre worked with bad|delivered
  · rw [ready] at bad; cases bad
  · exact ⟨pre,post,before,after,w,h,word,hpre,step,hpost,bound,worked,emitted,context,delivered⟩

theorem prior_delivery_is_full_delivery
    {laws : RecipientCorrection.Laws} {backing : Nat→Bool} {addresses i : Nat}
    {s t : RecipientAction.Archive} {es : List PublicationBridge.ArchiveEvent}
    {r : RecipientArchive.Frame}
    (h : AcquiredAfterDelivery laws backing addresses s t es i r) :
    DeliveredOnTrace laws backing addresses s t es := by
  rcases h with ⟨pre,post,before,after,w,header,word,_,step,hpost,_,_,_,_,delivered⟩
  rcases delivered with ⟨preWork,postWork,beforeWork,afterWork,av,wWork,workword,first,work,rest,credit⟩
  refine ⟨preWork,postWork++(.core (.core (.acquire true)) w)::post,
    beforeWork,afterWork,av,wWork,?_,first,work,?_,credit⟩
  · simp [word,workword,List.append_assoc]
  · exact Generative.trace_append_iff.mpr ⟨before,rest,.cons step hpost⟩

/-- A bundle of genuine physical and consumer histories. No efficacy-correct
command, current publication or evidence is supplied before those histories. -/
structure ReceiptOnlyEntrance (W : Type) where
  laws : RecipientCorrection.Laws
  backing : Nat→Bool
  addresses : Nat
  budget : Nat
  cells : Nat
  start : RecipientArchive.World
  bank : RecipientAction.Archive
  produced : List PublicationBridge.ArchiveEvent
  readerWorld : W
  context : Bool
  fuel : Nat
  reserve : Nat
  final : State W
  read : List Event
  command : Bool
  ready : start.core.phase=.ready
  production : Generative.Trace
    (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
    (EmissionArchive.empty start budget cells) produced bank
  consumer : Generative.Trace (process W)
    (initial (PaidArchiveReader.initial readerWorld bank.records context fuel) reserve) read final
  current : CurrentPublication final
  supported : RecipientAction.route final.working=some command

theorem entrance_has_receipt_with_prior_delivery (a : ReceiptOnlyEntrance W) :
    (∃ i r,PositiveFrame a.final.reader i r ∧ EmissionArchive.stored a.bank i r ∧
      AcquiredAfterDelivery a.laws a.backing a.addresses
        (EmissionArchive.empty a.start a.budget a.cells) a.bank a.produced i r) ∧
    energy a.final+spent a.read=a.fuel+a.reserve := by
  rcases initialized_production_and_publication_has_positive_origin a.ready a.production
    a.consumer a.current a.supported with ⟨⟨i,r,hp,stored,origin⟩,bill⟩
  have acquired:=located_positive_origin_is_actual_acquisition origin hp.2.2.2.1 hp.2.2.2.2
  exact ⟨⟨i,r,hp,stored,ready_acquisition_has_prior_delivery a.ready acquired⟩,bill⟩

/-- Externally justified temporal/address/recipient binding of the declared bank's
work events to one fixed episode. The prefix is part of this predicate; context
bit equality is deliberately insufficient. This is not stored runtime metadata. -/
def EpisodeBound (a : ReceiptOnlyEntrance W)
    (InEpisode : List PublicationBridge.ArchiveEvent→RecipientAction.Archive→RecipientArchive.World→Prop) : Prop :=
  ∀ pre post before after av successor,
    a.produced=pre++(.core (.core (.work av)) successor)::post →
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer a.laws a.backing) a.addresses)
      (EmissionArchive.empty a.start a.budget a.cells) pre before →
    EmissionArchive.Step (RecipientArchive.producer a.laws a.backing) a.addresses before
      (.core (.core (.work av)) successor) after →
    Generative.Trace (EmissionArchive.process (RecipientArchive.producer a.laws a.backing) a.addresses)
      after post a.bank → InEpisode pre before successor

/-- A predeclared single-service interpretation. A credited physical packet is
not intrinsically fulfillment, welfare, ethical standing or a reason to act. -/
def ServiceMeaning
    (InEpisode : List PublicationBridge.ArchiveEvent→RecipientAction.Archive→RecipientArchive.World→Prop)
    (Met : Prop) : Prop :=
  ∀ pre before successor,InEpisode pre before successor →
    successor.core.patient=before.world.core.patient+10 → Met

theorem current_command_implies_interpreted_service_met (a : ReceiptOnlyEntrance W)
    {InEpisode : List PublicationBridge.ArchiveEvent→RecipientAction.Archive→RecipientArchive.World→Prop}
    {Met : Prop} (bound : EpisodeBound a InEpisode) (meaning : ServiceMeaning InEpisode Met) : Met := by
  rcases (entrance_has_receipt_with_prior_delivery a).1 with ⟨i,r,_,_,h⟩
  rcases prior_delivery_is_full_delivery h with ⟨pre,post,before,after,av,w,word,hpre,step,hpost,credit⟩
  exact meaning pre before w (bound pre post before after av w word hpre step hpost) credit

/-- This excludes the declared comparator entrance. It constructs no withdrawal
policy, and says nothing about distinct services or independent grounds. -/
theorem no_sound_pending_one_service_entrance (a : ReceiptOnlyEntrance W)
    {InEpisode : List PublicationBridge.ArchiveEvent→RecipientAction.Archive→RecipientArchive.World→Prop}
    {Met Pending : Prop} (bound : EpisodeBound a InEpisode) (meaning : ServiceMeaning InEpisode Met)
    (pending_sound : Pending→¬Met) : ¬Pending := by
  intro pending
  exact pending_sound pending (current_command_implies_interpreted_service_met a bound meaning)

/-- The accepted successor's actual new-bank query and actual paid consumer,
cut before its later selected use. The old donor archives are not substituted. -/
def actualEntrance : ReceiptOnlyEntrance Unit where
  laws:=SuccessionWitness.changed
  backing:=fun i=>i=1
  addresses:=3
  budget:=5
  cells:=4
  start:=(EvaluativeSuccession.archive SuccessionWitness.secondStart).world
  bank:=EvaluativeSuccession.archive SuccessionWitness.bankEnd
  produced:=SuccessionWitness.bankWord SuccessionWitness.changed SuccessionWitness.secondStart SuccessionWitness.secondWord
  readerWorld:=()
  context:=true
  fuel:=24
  reserve:=0
  final:=SuccessionWitness.consumed.reader
  read:=PaidRecipientReasons.cycle
  command:=true
  ready:=by decide
  production:=by
    have h:=EvaluativeSuccession.bank_trace_projects SuccessionWitness.second_probe_trace
    exact h
  consumer:=by
    have h:=EvaluativeSuccession.reader_trace_projects SuccessionWitness.actual_consumer_trace
    rw [SuccessionWitness.reading_reader_exact] at h
    exact h
  current:=SuccessionWitness.actual_new_publication.2.2.2.2.2.1.2.2
  supported:=by
    have h:=SuccessionWitness.actual_new_publication.2.2.2.2.2.2.1
    unfold EvaluativeSuccession.command at h
    split at h
    · exact h
    · contradiction

theorem actual_publication_has_prior_paid_delivery :
    (∃ i r,PositiveFrame SuccessionWitness.consumed.reader.reader i r ∧
      EmissionArchive.stored (EvaluativeSuccession.archive SuccessionWitness.bankEnd) i r ∧
      AcquiredAfterDelivery SuccessionWitness.changed (fun j=>j=1) 3
        (EmissionArchive.empty (EvaluativeSuccession.archive SuccessionWitness.secondStart).world 5 4)
        (EvaluativeSuccession.archive SuccessionWitness.bankEnd)
        (SuccessionWitness.bankWord SuccessionWitness.changed SuccessionWitness.secondStart SuccessionWitness.secondWord) i r) ∧
    energy SuccessionWitness.consumed.reader+spent PaidRecipientReasons.cycle=24 :=
  entrance_has_receipt_with_prior_delivery actualEntrance

theorem actual_credit_precedes_selected_use :
    SuccessionWitness.bankEnd.core.patient=SuccessionWitness.firstEnd.core.patient+10 ∧
    SuccessionWitness.consumed.core.patient=SuccessionWitness.bankEnd.core.patient ∧
    SuccessionWitness.consumed.core.hardware.fuel=10 ∧ SuccessionWitness.consumed.core.packets=1 ∧
    spent PaidRecipientReasons.cycle=24 := by decide

theorem actual_no_sound_pending_one_service
    {InEpisode : List PublicationBridge.ArchiveEvent→RecipientAction.Archive→RecipientArchive.World→Prop}
    {Met Pending : Prop} (bound : EpisodeBound actualEntrance InEpisode)
    (meaning : ServiceMeaning InEpisode Met) (pending_sound : Pending→¬Met) : ¬Pending :=
  no_sound_pending_one_service_entrance actualEntrance bound meaning pending_sound

end ApplicationEvidence
