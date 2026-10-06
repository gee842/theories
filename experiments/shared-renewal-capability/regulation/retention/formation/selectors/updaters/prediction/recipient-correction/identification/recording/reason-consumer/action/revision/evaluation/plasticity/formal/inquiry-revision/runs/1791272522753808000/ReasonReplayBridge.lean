import PaidRecipientReasons

namespace ReasonReplayBridge

open PaidRecipientReasons
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

theorem factual_run_reader (s : State W) :
    (run s factualWord).reader=PaidArchiveReader.run s.reader PaidArchiveReader.word := rfl

theorem factual_run_boundary (s : State W) :
    (run s factualWord).phase=0 ∧ (run s factualWord).workspace=s.workspace ∧
    (run s factualWord).reserve=s.reserve ∧
    (run s factualWord).reader.fuel=s.reader.fuel-14 ∧
    PaidArchiveReader.Complete (run s factualWord).reader := by
  simp [run,factualWord,PaidArchiveReader.word,advance,PaidArchiveReader.advance,
    PaidArchiveReader.Complete,Nat.sub_sub]

theorem funded_factual_trace (s : State W) (hf : 14≤s.reader.fuel) :
    Generative.Trace (process W) s factualWord (run s factualWord) := by
  apply Generative.Trace.cons (show Step _ (.reader .activate) _ from ⟨by
    simp_all [Enabled,PaidArchiveReader.Enabled]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.reader .sense) _ from ⟨by
    simp_all [Enabled,advance,PaidArchiveReader.Enabled,PaidArchiveReader.advance]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.reader .read) _ from ⟨by
    simp_all [Enabled,advance,PaidArchiveReader.Enabled,PaidArchiveReader.advance]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.reader .read) _ from ⟨by
    simp_all [Enabled,advance,PaidArchiveReader.Enabled,PaidArchiveReader.advance]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.reader .read) _ from ⟨by
    simp_all [Enabled,advance,PaidArchiveReader.Enabled,PaidArchiveReader.advance]; omega,rfl⟩)
  exact .nil _

theorem funded_cycle_trace (s : State W) (hw : s.workspace=true) (hf : 24≤s.reader.fuel) :
    Generative.Trace (process W) s cycle (run s cycle) := by
  rw [cycle,run_append]
  apply Generative.trace_append_iff.mpr
  refine ⟨run s factualWord,funded_factual_trace s (by omega),?_⟩
  have hb:=factual_run_boundary s
  apply funded_reason_trace _ (hb.2.1.trans hw) hb.1 hb.2.2.2.2
  rw [hb.2.2.2.1]; omega

theorem cycle_run_boundary (s : State W) :
    (run s cycle).reader.fuel=s.reader.fuel-24 ∧
    (run s cycle).reserve=s.reserve ∧
    (run s cycle).workspace=s.workspace ∧ CurrentPublication (run s cycle) := by
  rw [cycle,run_append]
  have hr:=reason_run_normalized (run s factualWord)
  have hf:=factual_run_boundary s
  refine ⟨?_,?_,?_,?_⟩
  · rw [hr.2.2.1,hf.2.2.2.1]; omega
  · exact hr.2.2.2.trans hf.2.2.1
  · simp [run,reasonWord,advance]; exact hf.2.1
  · exact reason_run_complete _ hf.2.2.2.2

def postFund (s : PaidArchiveReader.State W) (reserve : Nat) : State W := advance (initial s reserve) .fund

def firstReason (s : PaidArchiveReader.State W) (reserve : Nat) : State W := run (postFund s reserve) reasonWord

def completionWord : List Event := .fund :: (reasonWord ++ .cold :: cycle)

def final (s : PaidArchiveReader.State W) (reserve : Nat) : State W :=
  run (advance (firstReason s reserve) .cold) cycle

theorem fund_is_transfer (s : PaidArchiveReader.State W) (reserve : Nat) :
    energy (postFund s reserve)=s.fuel+reserve ∧
    (postFund s reserve).reader.cache=s.cache ∧
    (postFund s reserve).reader.world=s.world ∧ (postFund s reserve).reserve=0 := by
  simp [postFund,initial,advance,energy]

theorem first_reason_boundary (s : PaidArchiveReader.State W) (reserve : Nat)
    (hc : PaidArchiveReader.Complete s) :
    (firstReason s reserve).reader.fuel=s.fuel+reserve-10 ∧
    (firstReason s reserve).reserve=0 ∧
    (firstReason s reserve).workspace=true ∧ CurrentPublication (firstReason s reserve) := by
  have h:=reason_run_normalized (postFund s reserve)
  refine ⟨h.2.2.1,h.2.2.2,?_,reason_run_complete _ hc⟩
  simp [firstReason,postFund,initial,run,reasonWord,advance]

theorem funded_two_cycle_tail (s : PaidArchiveReader.State W)
    (hc : PaidArchiveReader.Complete s) (hf : s.fuel=6) :
    Generative.Trace (process W) (initial s 28) completionWord (final s 28) := by
  apply Generative.Trace.cons (show Step _ .fund _ from ⟨⟨rfl,hc⟩,rfl⟩)
  apply Generative.trace_append_iff.mpr
  refine ⟨firstReason s 28,?_,?_⟩
  · exact funded_reason_trace _ rfl rfl hc (by simp [initial,advance,hf])
  · apply Generative.Trace.cons (show Step _ .cold _ from ⟨trivial,rfl⟩)
    apply funded_cycle_trace _
    · exact (first_reason_boundary s 28 hc).2.2.1
    · simp only [advance]
      rw [(first_reason_boundary s 28 hc).1,hf]
      decide

theorem final_has_no_added_fuel (s : PaidArchiveReader.State W)
    (hc : PaidArchiveReader.Complete s) (hf : s.fuel=6) :
    (final s 28).reader.fuel=0 ∧ (final s 28).reserve=0 ∧ CurrentPublication (final s 28) := by
  have h:=cycle_run_boundary (advance (firstReason s 28) .cold)
  refine ⟨?_,?_,h.2.2.2⟩
  · change (run (advance (firstReason s 28) .cold) cycle).reader.fuel=0
    rw [h.1]
    simp only [advance]
    rw [(first_reason_boundary s 28 hc).1,hf]
  · exact h.2.1.trans (first_reason_boundary s 28 hc).2.1

theorem one_short_cannot_complete (s : PaidArchiveReader.State W) (hf : s.fuel=6)
    (t : State W) : ¬ Generative.Trace (process W) (initial s 27) completionWord t := by
  intro ht
  have hh:=trace_ledger ht
  have hc : spent completionWord=34 := by decide
  rw [hc] at hh
  simp [energy,initial,hf] at hh

theorem one_cycle_short_cannot_complete (s : PaidArchiveReader.State W) (hf : s.fuel=6)
    (t : State W) : ¬ Generative.Trace (process W) (initial s 3) (.fund::reasonWord) t := by
  intro ht
  have hh:=trace_ledger ht
  have hc : spent (.fund::reasonWord)=10 := by decide
  rw [hc] at hh
  simp [energy,initial,hf] at hh

/- Semantic bridge from a genuine empty archive history and the unchanged
paid factual reader. It does not infer authenticity from a publication flag. -/
theorem actual_archive_to_paid_reasons {laws : RecipientCorrection.Laws}
    {backing : Nat → Bool} {addresses budget cells : Nat}
    {w : RecipientArchive.World} {a : EmissionArchive.State RecipientArchive.World RecipientArchive.Header RecipientArchive.Frame}
    {events : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (ready : w.core.phase=.ready)
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty w budget cells) events a)
    (context : Bool) {G : Prop} (root : G) {v : ReasonReplay.Node}
    (hm : (firstReason (PaidArchiveReader.run (PaidArchiveReader.initial a a.records context 20)
      PaidArchiveReader.word) 28).working.has v) :
    RecipientReasons.Meaning G (RecipientCorrection.lookup laws .recipient) v := by
  have ha:=RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws w budget cells (RecipientArchive.ready_sound laws w ready)) history
  have ht:=PaidArchiveReader.paid_reader_trace a a.records context
  have hc:=(PaidArchiveReader.paid_reader_complete a a.records context).1
  have hcache:=PaidArchiveReader.trace_cache_agrees
    (PaidArchiveReader.initial_cache_agrees a a.records context 20) ht
  have hfacts : PaidArchiveReader.Facts (RecipientCorrection.lookup laws .recipient)
      (PaidArchiveReader.run (PaidArchiveReader.initial a a.records context 20) PaidArchiveReader.word) := by
    apply PaidArchiveReader.trace_preserves_facts _ ht
    intro i r hr hp hrec
    exact RecipientArchive.completed_record_sound ha hr hp hrec
  let observed := PaidArchiveReader.run (PaidArchiveReader.initial a a.records context 20) PaidArchiveReader.word
  have hc' : PaidArchiveReader.Complete (postFund observed 28).reader := hc
  have ha' : PaidArchiveReader.CacheAgrees (postFund observed 28).reader := hcache
  have hf' : PaidArchiveReader.Facts (RecipientCorrection.lookup laws .recipient) (postFund observed 28).reader := hfacts
  exact actual_cache_reason_sound (s:=postFund observed 28) root hc' ha' hf' hm

theorem traced_reason_tail_sound {s u t : State W} {preEvents : List Event} {z : Bool} {G : Prop}
    (root : G) (ha : PaidArchiveReader.CacheAgrees s.reader) (hf : PaidArchiveReader.Facts z s.reader)
    (hp : Generative.Trace (process W) s preEvents u)
    (hr : Generative.Trace (process W) u reasonWord t)
    {v : ReasonReplay.Node} (hm : t.working.has v) : RecipientReasons.Meaning G z v := by
  have ht:=trace_run hr
  have hc : PaidArchiveReader.Complete u.reader := by
    cases hr with
    | cons hs _ => exact hs.1.2.2.1
  rw [ht] at hm
  exact actual_cache_reason_sound root hc (trace_cache_agrees ha hp) (trace_preserves_facts hf hp) hm

theorem cold_replay_reason_sound (s : PaidArchiveReader.State W) {z : Bool} {G : Prop}
    (root : G) (hc : PaidArchiveReader.Complete s) (hfu : s.fuel=6)
    (ha : PaidArchiveReader.CacheAgrees s) (hf : PaidArchiveReader.Facts z s)
    {v : ReasonReplay.Node} (hm : (final s 28).working.has v) : RecipientReasons.Meaning G z v := by
  have ht:=funded_two_cycle_tail s hc hfu
  have splitWord : completionWord=(.fund::reasonWord++[.cold]++factualWord)++reasonWord := by decide
  rw [splitWord] at ht
  rcases Generative.trace_append_iff.mp ht with ⟨u,hp,hr⟩
  exact traced_reason_tail_sound root ha hf hp hr hm

theorem actual_archive_to_cold_replayed_reasons {laws : RecipientCorrection.Laws}
    {backing : Nat → Bool} {addresses budget cells : Nat}
    {w : RecipientArchive.World} {a : EmissionArchive.State RecipientArchive.World RecipientArchive.Header RecipientArchive.Frame}
    {events : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (ready : w.core.phase=.ready)
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty w budget cells) events a)
    (context : Bool) {G : Prop} (root : G) {v : ReasonReplay.Node}
    (hm : (final (PaidArchiveReader.run (PaidArchiveReader.initial a a.records context 20)
      PaidArchiveReader.word) 28).working.has v) :
    RecipientReasons.Meaning G (RecipientCorrection.lookup laws .recipient) v := by
  have ha:=RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws w budget cells (RecipientArchive.ready_sound laws w ready)) history
  have ht:=PaidArchiveReader.paid_reader_trace a a.records context
  have hc:=(PaidArchiveReader.paid_reader_complete a a.records context).1
  have hfu:=(PaidArchiveReader.paid_reader_complete a a.records context).2.1
  apply cold_replay_reason_sound _ root hc hfu
    (PaidArchiveReader.trace_cache_agrees (PaidArchiveReader.initial_cache_agrees _ _ _ _) ht) _ hm
  apply PaidArchiveReader.trace_preserves_facts _ ht
  intro i r hr hp hrec
  exact RecipientArchive.completed_record_sound ha hr hp hrec

end ReasonReplayBridge

#print axioms ReasonReplayBridge.factual_run_reader
#print axioms ReasonReplayBridge.factual_run_boundary
#print axioms ReasonReplayBridge.funded_factual_trace
#print axioms ReasonReplayBridge.funded_cycle_trace
#print axioms ReasonReplayBridge.cycle_run_boundary
#print axioms ReasonReplayBridge.fund_is_transfer
#print axioms ReasonReplayBridge.first_reason_boundary
#print axioms ReasonReplayBridge.funded_two_cycle_tail
#print axioms ReasonReplayBridge.final_has_no_added_fuel
#print axioms ReasonReplayBridge.one_short_cannot_complete
#print axioms ReasonReplayBridge.one_cycle_short_cannot_complete
#print axioms ReasonReplayBridge.actual_archive_to_paid_reasons
#print axioms ReasonReplayBridge.traced_reason_tail_sound
#print axioms ReasonReplayBridge.cold_replay_reason_sound
#print axioms ReasonReplayBridge.actual_archive_to_cold_replayed_reasons
