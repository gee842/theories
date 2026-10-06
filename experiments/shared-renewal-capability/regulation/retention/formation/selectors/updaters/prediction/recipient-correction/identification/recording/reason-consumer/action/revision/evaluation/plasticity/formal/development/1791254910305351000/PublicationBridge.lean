import PublicationBudget

namespace PublicationBridge
open PaidRecipientReasons PublicationSafety PublicationBudget

def Assured (z : Bool) (G : Prop) (s : State W) : Prop :=
  s.conflict=false ∧ SelectedFromCurrent s ∧ (s.current=true →
    CurrentPublication s ∧
    s.working=ReasonReplay.closureMask RecipientReasons.star (RecipientReasons.derived s.normalized) ∧
    ∀ v, s.working.has v → RecipientReasons.Meaning G z v)

theorem invariant_assured {z : Bool} {G : Prop} {s : State W}
    (root : G) (hi : Invariant z s) : Assured z G s := by
  refine ⟨invariant_no_conflict hi,hi.selected,?_⟩
  intro hc
  have hp:=hi.publication hc
  exact ⟨hp,invariant_publication_exact hi hp,fun _ hv=>route_meaning root hi.working hv⟩

theorem initialized_trace_assured {z : Bool} {G : Prop}
    {reader : PaidArchiveReader.State W} {reserve : Nat} {t : State W} {es : List Event}
    (root : G) (ha : PaidArchiveReader.CacheAgrees reader) (hf : PaidArchiveReader.Facts z reader)
    (history : Generative.Trace (process W) (initial reader reserve) es t) : Assured z G t :=
  invariant_assured root (trace_invariant (initial_invariant reader reserve ha hf) history)

abbrev ArchiveState := EmissionArchive.State RecipientArchive.World RecipientArchive.Header RecipientArchive.Frame
abbrev ArchiveEvent := EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header

theorem actual_archive_initial_facts {laws : RecipientCorrection.Laws}
    {backing : Nat → Bool} {addresses budget cells : Nat}
    {w : RecipientArchive.World} {a : ArchiveState} {events : List ArchiveEvent}
    (ready : w.core.phase=.ready)
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty w budget cells) events a) (context : Bool) (fuel : Nat) :
    PaidArchiveReader.Facts (RecipientCorrection.lookup laws .recipient)
      (PaidArchiveReader.initial a a.records context fuel) := by
  have ha:=RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws w budget cells (RecipientArchive.ready_sound laws w ready)) history
  intro i r hr hp hrec
  exact RecipientArchive.completed_record_sound ha hr hp hrec

theorem actual_archive_every_unread_trace {laws : RecipientCorrection.Laws}
    {backing : Nat → Bool} {addresses budget cells : Nat}
    {w : RecipientArchive.World} {a : ArchiveState} {events : List ArchiveEvent}
    (ready : w.core.phase=.ready)
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty w budget cells) events a)
    (context : Bool) {G : Prop} (root : G) {fuel reserve : Nat}
    {t : State ArchiveState} {es : List Event}
    (execution : Generative.Trace (process ArchiveState)
      (initial (PaidArchiveReader.initial a a.records context fuel) reserve) es t) :
    Assured (RecipientCorrection.lookup laws .recipient) G t ∧
    24*publications es≤spent es := by
  exact ⟨initialized_trace_assured root
    (PaidArchiveReader.initial_cache_agrees _ _ _ _)
    (actual_archive_initial_facts ready history context fuel) execution,
    unread_count_bound execution⟩

theorem actual_archive_every_handoff_trace {laws : RecipientCorrection.Laws}
    {backing : Nat → Bool} {addresses budget cells : Nat}
    {w : RecipientArchive.World} {a : ArchiveState} {events : List ArchiveEvent}
    (ready : w.core.phase=.ready)
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty w budget cells) events a)
    (context : Bool) {G : Prop} (root : G) {F : Nat} (funding : 94≤F)
    {t : State ArchiveState} {es : List Event}
    (execution : Generative.Trace (process ArchiveState)
      (initial (PaidArchiveReader.run (PaidArchiveReader.initial a a.records context 20)
        PaidArchiveReader.word) (F-94)) es t) :
    Assured (RecipientCorrection.lookup laws .recipient) G t ∧
    24*publications es≤spent es+14 ∧ 74+24*publications es≤F := by
  have hr:=PaidArchiveReader.paid_reader_trace a a.records context
  have hc:=(PaidArchiveReader.paid_reader_complete a a.records context).1
  have fuel:=(PaidArchiveReader.paid_reader_complete a a.records context).2.1
  have ha:=PaidArchiveReader.trace_cache_agrees
    (PaidArchiveReader.initial_cache_agrees a a.records context 20) hr
  have hf:=PaidArchiveReader.trace_preserves_facts
    (actual_archive_initial_facts ready history context 20) hr
  exact ⟨initialized_trace_assured root ha hf execution,
    completed_handoff_count_bound hc execution,inherited_fuel_count_bound funding hc fuel execution⟩

/- A fabricated phase bypasses the paid path schedule. It has a sound empty
archive/cache and backed workspace, yet its publication is false at z=false. -/
def forged : State Unit :=
  { initial { PaidArchiveReader.initial () (fun _=>none) false 0 with
      active:=true,token:=some false,next:=3 } 0 with
    phase:=8,working:=⟨false,true⟩ }

theorem forged_has_sound_inputs : PaidArchiveReader.CacheAgrees forged.reader ∧
    PaidArchiveReader.Facts false forged.reader ∧ forged.workspace=true := by
  simp [forged,initial,PaidArchiveReader.initial,PaidArchiveReader.CacheAgrees,
    PaidArchiveReader.Facts,RecipientArchive.decode]

theorem forged_free_false_publication : Step forged .publish (advance forged .publish) ∧
    charge .publish=0 ∧ CurrentPublication (advance forged .publish) ∧
    (advance forged .publish).working.has .q ∧ ¬ RecipientReasons.Meaning True false .q := by
  simp [Step,Enabled,forged,initial,PaidArchiveReader.initial,PaidArchiveReader.Complete,
    advance,charge,CurrentPublication,ReasonReplay.Mask.has,RecipientReasons.Meaning,
    RecipientReasons.compatible_iff]

end PublicationBridge

#print axioms PublicationBridge.invariant_assured
#print axioms PublicationBridge.initialized_trace_assured
#print axioms PublicationBridge.actual_archive_initial_facts
#print axioms PublicationBridge.actual_archive_every_unread_trace
#print axioms PublicationBridge.actual_archive_every_handoff_trace
#print axioms PublicationBridge.forged_has_sound_inputs
#print axioms PublicationBridge.forged_free_false_publication
