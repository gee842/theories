import GenerativeCore

/-!
# Joint descriptions of successive occurrences

The existing Trace already requires actual intermediate states. This interface
makes a selected joint description of each transition explicit in its label.
It changes neither states nor underlying transitions. Descriptions are analyst
readouts, not newly installed records, experiences or response mechanisms.

A joint report may contain several before/after readings. Their values must
come from the same occurrence; separately possible marginal reports cannot be
combined by these constructors. Reading a whole occurrence also allows real
changes in the described condition, rather than requiring a fixed target value.
-/

namespace Generative.CoupledOccurrence

universe u v w x

variable {State : Type u} {Event : Type v} {Report : Type w} {View : Type x}

/-- Conservative event decoration, with no additional physical transition. -/
def described (P : Process State Event) (report : State → Event → State → Report) :
    Process State (Event × Report) where
  step s label t := P.step s label.1 t ∧ label.2 = report s label.1 t

variable {P : Process State Event} {report : State → Event → State → Report}

theorem erase_described_trace {s t : State} {occurrences : List (Event × Report)}
    (h : Trace (described P report) s occurrences t) :
    Trace P s (occurrences.map Prod.fst) t := by
  induction h with
  | nil s => exact .nil s
  | cons hstep _ ih => exact .cons hstep.1 ih

/-- A particular underlying trace admits a joint description without selecting
different executions for its different reported dimensions. -/
theorem describe_actual_trace {s t : State} {events : List Event}
    (h : Trace P s events t) :
    ∃ occurrences, Trace (described P report) s occurrences t ∧
      occurrences.map Prod.fst = events := by
  induction h with
  | nil s => exact ⟨[], .nil s, rfl⟩
  | @cons s m t e es hs ht ih =>
    obtain ⟨tail, htail, hword⟩ := ih
    exact ⟨(e, report s e m) :: tail, .cons ⟨hs, rfl⟩ htail,
      congrArg (List.cons e) hword⟩

theorem described_trace_exact {s t : State} {events : List Event} :
    (∃ occurrences, Trace (described P report) s occurrences t ∧
      occurrences.map Prod.fst = events) ↔ Trace P s events t := by
  constructor
  · rintro ⟨occurrences, h, hevents⟩
    exact hevents ▸ erase_described_trace h
  · exact describe_actual_trace

/-- Both described segments meet at the same full state. Equality of one
reported quantity is not a replacement for this boundary condition. -/
theorem described_append_actual_iff {s t : State}
    {past future : List (Event × Report)} :
    Trace (described P report) s (past ++ future) t ↔
      ∃ current, Trace (described P report) s past current ∧
        Trace (described P report) current future t := trace_append_iff

/-- Coarser descriptions can be read from one joint history. The converse,
combining independently witnessed views into a joint history, is not asserted. -/
theorem map_described_trace (view : Report → View)
    {s t : State} {occurrences : List (Event × Report)}
    (h : Trace (described P report) s occurrences t) :
    Trace (described P (fun s e t => view (report s e t))) s
      (occurrences.map (fun item => (item.1, view item.2))) t := by
  induction h with
  | nil s => exact .nil s
  | cons hstep _ ih =>
    exact .cons ⟨hstep.1, congrArg view hstep.2⟩ ih

/-- A later actual continuation preserves the description of an earlier
occurrence even when current endpoint readings have since changed. This is
retention in the audit description, not guaranteed internal memory. -/
theorem actual_continuation_retains_occurrence
    {s current t : State} {past future : List (Event × Report)}
    {occurrence : Event × Report}
    (hpast : Trace (described P report) s past current)
    (hfuture : Trace (described P report) current future t)
    (occurred : occurrence ∈ past) :
    Trace (described P report) s (past ++ future) t ∧ occurrence ∈ past ++ future := by
  exact ⟨trace_append_iff.mpr ⟨current, hpast, hfuture⟩,
    List.mem_append.mpr (Or.inl occurred)⟩

/-- Deterministic replay constructs the descriptions; lawfulness still needs a
separate trace proof. This function alone grants no event admissibility. -/
def replay (advance : State → Event → State)
    (report : State → Event → State → Report) : State → List Event → List (Event × Report)
  | _, [] => []
  | s, e :: es => (e, report s e (advance s e)) :: replay advance report (advance s e) es

theorem replay_append (advance : State → Event → State)
    (report : State → Event → State → Report)
    (run : State → List Event → State)
    (run_nil : ∀ s, run s [] = s)
    (run_cons : ∀ s e es, run s (e :: es) = run (advance s e) es)
    (s : State) (past future : List Event) :
    replay advance report s (past ++ future) =
      replay advance report s past ++ replay advance report (run s past) future := by
  induction past generalizing s with
  | nil => simp only [List.nil_append, replay, run_nil]
  | cons e es ih =>
    simp only [List.cons_append, replay, run_cons]
    exact congrArg (List.cons (e, report s e (advance s e))) (ih (advance s e))

end Generative.CoupledOccurrence

#print axioms Generative.CoupledOccurrence.erase_described_trace
#print axioms Generative.CoupledOccurrence.describe_actual_trace
#print axioms Generative.CoupledOccurrence.described_trace_exact
#print axioms Generative.CoupledOccurrence.described_append_actual_iff
#print axioms Generative.CoupledOccurrence.map_described_trace
#print axioms Generative.CoupledOccurrence.actual_continuation_retains_occurrence
#print axioms Generative.CoupledOccurrence.replay_append
