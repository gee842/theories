import Becoming.Assurance
import AcquiredSegmentation

/-!
# Acquired grouping along the traces of reception

`AcquiredSegmentation` states how retained encounters change a grouping relation used before an
already formed compositional operation. A configuration (`AcquiredSegmentation.State`) holds a
formed operation and a log of observation slots; receiving a slot (`receive`) charges one unit of
support and appends the slot to the log, and exposure to a list of slots (`expose`) receives them
in order. Reception is a law of change, so a process of the spine (`reception`, through
`Assurance.ofMap`), and exposure is the end of its trace along the slots (`trace_end`,
`expose_trace`). The periphery's results about exposed configurations are read here as results
about the configurations its traces end at, and proved through the periphery's theorems.

* **Every trace of reception keeps support and spent support together** (`total_kept`); without
  support, reception leaves the configuration as it is along every trace (`still_without_support`);
  broadening after a failed parse reaches its configuration by a trace of reception and keeps the
  total (`broadening_trace`).
* **Along the trace of the supplied context from the prepared configuration** (support 28), the
  learned grouping makes every word sequence assemble into its message (`grouping_assembles`); the
  utterance unparsed at the start parses at the end into the intended form, and the formed
  operation gives `[true, false, true]` (`reception_changes_parse`); the response keeps the
  context's log and the original acquisition (`response_keeps_history`); and support falls from 14
  to 4 (`support_used`). With support 27 the utterance parses but the response lacks support
  (`parse_without_support`).
* **Order, not frequency**: along the reordered course, which holds every sound as often as the
  context, the utterance does not parse (`order_not_frequency`).
* **Broadening after a narrow trace**: after the narrow course the utterance fails, and broadening
  reaches the context's log, the parse and the response (`broadening_after_failure`); a parsed
  message does not trigger broadening (`parsed_not_broadened`); with support 19 broadening keeps
  only a prefix and fails (`broadening_keeps_prefix`), and with support 21 it parses this
  utterance while failing on another form (`broadening_parses_one_form`).

The supplied sounds, slots, majority threshold, decoder and encounters are the periphery's; the
results about the supplied context are facts of one constructed model, read on its traces. This
module belongs to the periphery-join ring. No ethical predicate or ranking occurs. It inherits
`propext` and `Quot.sound` from the periphery's theorems it uses (`broadening_preserves_support`,
`exposure_preserves_support` and `acquired_segmentation_enters_message_assembly` bring `propext`
and `Quot.sound`; the other
periphery theorems used bring `propext`; `equal_event_frequencies_do_not_identify_grouping` brings
none) and adds no axiom of its own.
-/

namespace Becoming

open Generative

namespace ReceptionTracesInherited

open Generative.AcquiredSegmentation Generative.CompositionalAcquisition
  Generative.CompositionalFormation Generative.CompositionalTransmission

/-- Reception of observation slots, read as a process: receiving the slot `e` takes `s` to
`receive e s`. -/
abbrev reception : Process State (Option Sound) := Assurance.ofMap fun s e => receive e s

/-- A step of reception is receiving the slot. -/
theorem step_iff {s t : State} {e : Option Sound} : reception.step s e t ↔ t = receive e s :=
  Iff.rfl

/-- **A trace of reception ends at the exposure to its slots.** -/
theorem trace_end : ∀ {s t : State} {es : List (Option Sound)}, Trace reception s es t →
    t = expose es s
  | _, _, _, .nil _ => rfl
  | _, _, _, .cons step rest => (trace_end rest).trans (congrArg (expose _) (step_iff.mp step))

/-- **Reception has a trace along every list of slots**, ending at the exposure to them. -/
theorem expose_trace : ∀ (es : List (Option Sound)) (s : State), Trace reception s es (expose es s)
  | [], s => .nil s
  | e :: es, s => .cons (step_iff.mpr rfl) (expose_trace es (receive e s))

/-- What holds at the exposure to a list of slots holds where every trace along them ends. -/
theorem along {s : State} {es : List (Option Sound)} {Q : State → Prop} (holds : Q (expose es s)) :
    ∀ t, Trace reception s es t → Q t :=
  fun _ path => Eq.subst (motive := Q) (trace_end path).symm holds

/-! ## Laws of every trace -/

/-- **Every trace of reception keeps support and spent support together.** -/
theorem total_kept {s t : State} {es : List (Option Sound)} (path : Trace reception s es t) :
    t.machine.support + t.machine.spent = s.machine.support + s.machine.spent :=
  along (Q := fun t => t.machine.support + t.machine.spent = s.machine.support + s.machine.spent)
    (exposure_preserves_support es s) t path

/-- **Without support, reception leaves the configuration as it is along every trace.** -/
theorem still_without_support : ∀ {s t : State} {es : List (Option Sound)},
    Trace reception s es t → s.machine.support = 0 → t = s
  | _, _, _, .nil _, _ => rfl
  | _, _, _, .cons step rest, short =>
    have kept := (step_iff.mp step).trans (insufficient_reception_keeps_actual_record _ _ short)
    (still_without_support rest
      ((congrArg (fun m : State => m.machine.support) kept).trans short)).trans kept

/-- **Broadening after a failed parse reaches its configuration by a trace of reception, and keeps
support and spent support together.** -/
theorem broadening_trace (raw : List Sound) (more : List (Option Sound)) (s : State) :
    ∃ es, Trace reception s es (broadenAfterFailure raw more s) ∧
      (broadenAfterFailure raw more s).machine.support +
        (broadenAfterFailure raw more s).machine.spent = s.machine.support + s.machine.spent :=
  have path : ∃ es, Trace reception s es (broadenAfterFailure raw more s) := by
    unfold broadenAfterFailure
    cases (parse s raw).isNone with
    | true => exact ⟨more, expose_trace more s⟩
    | false => exact ⟨[], .nil s⟩
  match path with
  | ⟨es, path⟩ => ⟨es, path, broadening_preserves_support raw more s⟩

/-! ## The supplied context, on its traces -/

/-- **Along the trace of the context, the learned grouping makes every word sequence assemble into
its message.** -/
theorem grouping_assembles :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      ∀ ws, parse t (encode ws) = assembleMessage (ws.map Expr.atom) :=
  along (Q := fun t => ∀ ws, parse t (encode ws) = assembleMessage (ws.map Expr.atom))
    acquired_segmentation_enters_message_assembly

/-- **Reception along the context changes the parse of the utterance**: unparsed and without
response at the start of the trace, it parses at the end into the intended form, and the formed
operation gives `[true, false, true]`, spending the rest of the support. -/
theorem reception_changes_parse :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      (parse (ready 28) utterance = none ∧ act utterance (ready 28) = none) ∧
      (parse t utterance = some intended ∧
        (act utterance t).map (fun r => (r.1, r.2.machine.support, r.2.machine.spent)) =
          some ([true, false, true], 0, 21)) :=
  fun t path => ⟨no_experience_leaves_the_message_unparsed,
    along (Q := fun t => parse t utterance = some intended ∧
        (act utterance t).map (fun r => (r.1, r.2.machine.support, r.2.machine.spent)) =
          some ([true, false, true], 0, 21))
      new_grouping_reaches_the_existing_formed_operation t path⟩

/-- **The response at the end of the trace of the context keeps the context's log and the original
acquisition.** -/
theorem response_keeps_history :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      (act utterance t).map (fun r => (r.2.log, r.2.machine.samples)) =
        some (context.map some, trialRecords usual) :=
  along (Q := fun t => (act utterance t).map (fun r => (r.2.log, r.2.machine.samples)) =
      some (context.map some, trialRecords usual))
    response_retains_training_history_and_original_acquisition

/-- **Along the trace of the context, support falls from 14 to 4**, the ten slots received, with
the periphery's account `7 + 7 + 10 + 4 = 28` of the whole history. -/
theorem support_used :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      (ready 28).machine.support = 14 ∧ t.machine.support = 4 ∧ 7 + 7 + 10 + 4 = 28 :=
  fun t path =>
    ⟨exact_whole_history_account.1,
     along (Q := fun t => t.machine.support = 4) exact_whole_history_account.2.1 t path,
     exact_whole_history_account.2.2⟩

/-- **With support 27, the utterance parses at the end of the trace of the context, but the
response lacks support.** -/
theorem parse_without_support :
    ∀ t, Trace reception (ready 27) (context.map some) t →
      parse t utterance = some intended ∧ act utterance t = none :=
  along (Q := fun t => parse t utterance = some intended ∧ act utterance t = none)
    grouped_message_can_lack_execution_support

/-- **Order, not frequency.** The reordered course holds every sound as often as the context, and
yet the utterance parses at the end of the trace of the context and not at the end of the trace of
the reordered course. -/
theorem order_not_frequency :
    (∀ x, context.count x = reordered.count x) ∧
    ∀ t t', Trace reception (ready 28) (context.map some) t →
      Trace reception (ready 28) (reordered.map some) t' →
        parse t utterance = some intended ∧ parse t' utterance = none :=
  ⟨equal_event_frequencies_do_not_identify_grouping,
   fun t t' path path' =>
    ⟨along (Q := fun t => parse t utterance = some intended)
        new_grouping_reaches_the_existing_formed_operation.1 t path,
     along (Q := fun t => parse t utterance = none)
        encounter_relations_change_grouping_and_use.2.2 t' path'⟩⟩

/-- The narrow course: two encounters of the first word. -/
abbrev narrowCourse : List (Option Sound) := ([Sound.a, .b, .a, .b] : List Sound).map some

/-- **Broadening after a narrow trace.** At the end of the narrow course the utterance fails; the
broadening it triggers reaches the context's log, the parse into the intended form and the
response `[true, false, true]`. -/
theorem broadening_after_failure :
    ∀ t, Trace reception (ready 28) narrowCourse t →
      parse t utterance = none ∧
      (broadenAfterFailure utterance (additional.map some) t).log = context.map some ∧
      parse (broadenAfterFailure utterance (additional.map some) t) utterance = some intended ∧
      (act utterance (broadenAfterFailure utterance (additional.map some) t)).map Prod.fst =
        some [true, false, true] :=
  along (Q := fun t => parse t utterance = none ∧
      (broadenAfterFailure utterance (additional.map some) t).log = context.map some ∧
      parse (broadenAfterFailure utterance (additional.map some) t) utterance = some intended ∧
      (act utterance (broadenAfterFailure utterance (additional.map some) t)).map Prod.fst =
        some [true, false, true])
    diagnostic_failure_changes_further_acquisition

/-- **A parsed message does not trigger broadening** at the end of the narrow course. -/
theorem parsed_not_broadened :
    ∀ t, Trace reception (ready 28) narrowCourse t →
      broadenAfterFailure [.a, .b] (additional.map some) t = t :=
  along (Q := fun t => broadenAfterFailure [.a, .b] (additional.map some) t = t)
    recognized_message_does_not_trigger_broadening

/-- **With support 19, broadening after the narrow course keeps only a prefix of the further
encounters, and the utterance still fails.** -/
theorem broadening_keeps_prefix :
    ∀ t, Trace reception (ready 19) narrowCourse t →
      (broadenAfterFailure utterance (additional.map some) t).log =
          ([Sound.a, .b, .a, .b, .c] : List Sound).map some ∧
        parse (broadenAfterFailure utterance (additional.map some) t) utterance = none :=
  along (Q := fun t => (broadenAfterFailure utterance (additional.map some) t).log =
          ([Sound.a, .b, .a, .b, .c] : List Sound).map some ∧
        parse (broadenAfterFailure utterance (additional.map some) t) utterance = none)
    insufficient_further_acquisition_keeps_a_prefix

/-- **With support 21, broadening after the narrow course parses the utterance without a response,
while failing on another form.** -/
theorem broadening_parses_one_form :
    ∀ t, Trace reception (ready 21) narrowCourse t →
      (broadenAfterFailure utterance (additional.map some) t).log =
          ([Sound.a, .b, .a, .b, .c, .d, .c] : List Sound).map some ∧
        parse (broadenAfterFailure utterance (additional.map some) t) utterance = some intended ∧
        act utterance (broadenAfterFailure utterance (additional.map some) t) = none ∧
        parse (broadenAfterFailure utterance (additional.map some) t) [.c, .d, .c, .d] = none :=
  along (Q := fun t => (broadenAfterFailure utterance (additional.map some) t).log =
          ([Sound.a, .b, .a, .b, .c, .d, .c] : List Sound).map some ∧
        parse (broadenAfterFailure utterance (additional.map some) t) utterance = some intended ∧
        act utterance (broadenAfterFailure utterance (additional.map some) t) = none ∧
        parse (broadenAfterFailure utterance (additional.map some) t) [.c, .d, .c, .d] = none)
    partial_experience_can_parse_one_form_without_general_grouping

end ReceptionTracesInherited

end Becoming
