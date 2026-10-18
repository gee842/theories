import Becoming.RouteFormation
import Becoming.Segmentation

/-!
# Learned grouping: received transitions form the grouping a formed operation reads through

`Becoming.Segmentation` groups a sequence by a relation between adjacent elements and learns the
relation as the majority of observed transitions (`Segmentation.bond`). Here a formation that has
already formed an operation (`Becoming.RouteFormation`) receives observation slots: receiving a
slot draws one unit and appends it to the log (`receive`), and the log's transitions give the
grouping through which an utterance is read into words, assembled into an expression and answered
by the formed operation (`parse`, `act`). This module states, on the core's processes and traces,
what `AcquiredSegmentation` (8 October) proved, and what the join `ReceptionTracesInherited`
(17 October) and the bridge's grouping section read through the core, with every proof
constructive (board item F3Q, 18 October 2026). The sounds, the slots, the majority threshold, the
decoder, the encounters and the prepared formation are supplied; nothing acoustic, neural or a
general account of language is claimed.

* **The grouping is the core's.** Grouping never changes the sequence (`Segmentation.join_chunks`).
  For every relation, grouping recovers the words of every sequence in the two-word encoding
  exactly when `a→b` and `c→d` are linked and `b→a`, `b→c`, `d→a`, `d→c` are not
  (`two_word_iff`); the ideal relation is an instance (`ideal_two_word`), and the words are read
  as their atoms (`decodes_words`).
* **Reception draws.** Receiving keeps stock plus drawn (`receive_stock`, `expose_stock`,
  `broaden_stock`); without stock it changes nothing (`receive_short`).
* **The supplied context.** After the context, the log's majority bonds are the ideal relation
  (`context_forms_bond`), so every word sequence is grouped into its words
  (`context_groups_words`) and assembled into its message (`context_assembles`); the utterance
  unparsed before parses into the intended form and the formed operation answers it
  (`unexposed_unparsed`, `grouping_reaches_program`), keeping the log and the original
  acquisition (`response_keeps_log`), with the account of the whole history (`history_account`);
  with one unit less the utterance parses without a response (`parsed_short`).
* **Order, not frequency.** A gap breaks a transition (`gap_breaks_edge`); a reordered course with
  every sound as often as the context forms a different bond and leaves the utterance unparsed
  (`counts_agree`, `order_changes_grouping`); repetition can join across the intended words
  (`repetition_joins_words`).
* **Broadening after failure.** After a narrow course the utterance fails and broadening reaches
  the context (`broaden_reaches_context`); a parsed message does not broaden (`parsed_keeps`);
  short stock keeps a prefix (`broaden_prefix`) or parses one form only (`broaden_one_form`).
* **As a process.** Reception is a process whose traces end at the exposure to their slots
  (`reception`, `trace_end`, `expose_trace`); the laws above are stated of every trace
  (`total_kept`, `still_without_support`, `broadening_trace`, `grouping_assembles`,
  `reception_changes_parse`, `response_keeps_history`, `support_used`, `parse_without_support`,
  `order_not_frequency`, `broadening_after_failure`, `parsed_not_broadened`,
  `broadening_keeps_prefix`, `broadening_parses_one_form`).

No ethical predicate or ranking occurs, and every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

namespace LearnedGrouping

open CodeAcquisition RouteFormation Segmentation

/-! ## Sounds, words and the grouping -/

/-- Four elementary sounds. -/
inductive Sound where
  | a | b | c | d
  deriving DecidableEq

/-- A formed apparatus and its log of observation slots; `none` is a slot with no sound. -/
structure State where
  machine : Apparatus
  log : List (Option Sound)
  deriving DecidableEq

/-- The two words. -/
def word : Bool → List Sound
  | false => [.a, .b]
  | true => [.c, .d]

/-- The first sound of each word. -/
def wordFirst : Bool → Sound
  | false => .a
  | true => .c

/-- The rest of each word. -/
def wordRest : Bool → List Sound
  | false => [.b]
  | true => [.d]

theorem spelled : Spelled word wordFirst wordRest
  | false => rfl
  | true => rfl

/-- **For every grouping relation, grouping recovers the words of every sequence in the two-word
encoding exactly when `a→b` and `c→d` are linked and `b→a`, `b→c`, `d→a`, `d→c` are not.** -/
theorem two_word_iff (r : Sound → Sound → Bool) :
    (∀ ws, chunks r (encode word ws) = ws.map word) ↔
      r .a .b = true ∧ r .c .d = true ∧ r .b .a = false ∧ r .b .c = false ∧
        r .d .a = false ∧ r .d .c = false :=
  have core := encode_iff r spelled
  ⟨fun every => match core.mp every with
    | ⟨inside, between⟩ =>
      ⟨(inside false).1, (inside true).1, between false false, between false true,
       between true false, between true true⟩,
   fun ⟨ab, cd, ba, bc, da, dc⟩ =>
    have inside : ∀ w, LinkedFrom r (wordFirst w) (wordRest w) := fun
      | false => ⟨ab, trivial⟩
      | true => ⟨cd, trivial⟩
    have between : ∀ w v, r (lastOf (wordFirst w) (wordRest w)) (wordFirst v) = false := fun
      | false, false => ba
      | false, true => bc
      | true, false => da
      | true, true => dc
    core.mpr ⟨inside, between⟩⟩

/-- The ideal relation: `a→b` and `c→d`. -/
def idealBond : Sound → Sound → Bool
  | .a, .b => true
  | .c, .d => true
  | .a, .a => false
  | .a, .c => false
  | .a, .d => false
  | .b, _ => false
  | .c, .a => false
  | .c, .b => false
  | .c, .c => false
  | .d, _ => false

/-- **The ideal relation recovers the words of every sequence.** -/
theorem ideal_two_word (ws : List Bool) : chunks idealBond (encode word ws) = ws.map word :=
  (two_word_iff idealBond).mpr ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩ ws

/-- Read two sounds as an atom: `a b` and `c d`. -/
def decodePair (x y : Sound) : Option Expr :=
  if x = .a ∧ y = .b then some p0 else if x = .c ∧ y = .d then some p1 else none

/-- Read a group of sounds: only a pair is read. -/
def decodeChunk : List Sound → Option Expr
  | [] => none
  | [_] => none
  | [x, y] => decodePair x y
  | _ :: _ :: _ :: _ => none

/-- **The words are read as their atoms.** -/
theorem decodes_words (ws : List Bool) :
    readAll decodeChunk (ws.map word) = some (ws.map Expr.atom) :=
  (readAll_map_iff decodeChunk word Expr.atom ws).mpr fun
    | false, _ => rfl
    | true, _ => rfl

/-- Assemble read atoms into one expression, joining from the left. -/
def assembleMessage : List Expr → Option Expr
  | [] => none
  | e :: es => some (es.foldl Expr.join e)

/-- Group by the log's majority bonds, read each group, and assemble. -/
def parse (s : State) (raw : List Sound) : Option Expr :=
  (readAll decodeChunk (chunks (bond s.log) raw)).bind assembleMessage

/-! ## Reception -/

/-- Receive a slot: one unit is drawn and the slot is logged; without stock nothing changes. -/
def receive (event : Option Sound) (s : State) : State :=
  match s.machine.stock with
  | 0 => s
  | n + 1 => ⟨{ s.machine with stock := n, drawn := s.machine.drawn + 1 }, s.log ++ [event]⟩

/-- Receive slots in turn. -/
def expose : List (Option Sound) → State → State
  | [], s => s
  | x :: xs, s => expose xs (receive x s)

/-- Parse an utterance and answer it with the formed operation, drawing what the response draws. -/
def act (raw : List Sound) (s : State) : Option (List Bool × State) :=
  (parse s raw).bind fun e => (respond s.machine e).bind fun r =>
    some (r.1, ⟨{ s.machine with stock := r.2, drawn := s.machine.drawn + (s.machine.stock - r.2) },
      s.log⟩)

/-- A supplied policy: where the utterance does not parse, receive further slots. -/
def broadenAfterFailure (raw : List Sound) (more : List (Option Sound)) (s : State) : State :=
  bif (parse s raw).isNone then expose more s else s

/-- **Receiving keeps stock plus drawn.** -/
theorem receive_stock (event : Option Sound) (s : State) :
    (receive event s).machine.stock + (receive event s).machine.drawn =
      s.machine.stock + s.machine.drawn := by
  rcases s with ⟨⟨w, i, st, d, pa, u, bl, sa, at_⟩, log⟩
  cases st with
  | zero => rfl
  | succ n => exact (Nat.add_succ n d).trans (Nat.succ_add n d).symm

/-- **Exposure keeps stock plus drawn.** -/
theorem expose_stock : ∀ (events : List (Option Sound)) (s : State),
    (expose events s).machine.stock + (expose events s).machine.drawn =
      s.machine.stock + s.machine.drawn
  | [], _ => rfl
  | x :: xs, s => (expose_stock xs (receive x s)).trans (receive_stock x s)

/-- **Without stock, receiving changes nothing.** -/
theorem receive_short (event : Option Sound) (s : State) (short : s.machine.stock = 0) :
    receive event s = s := by
  unfold receive
  rw [short]

/-- **Broadening keeps stock plus drawn.** -/
theorem broaden_stock (raw : List Sound) (more : List (Option Sound)) (s : State) :
    (broadenAfterFailure raw more s).machine.stock + (broadenAfterFailure raw more s).machine.drawn =
      s.machine.stock + s.machine.drawn := by
  unfold broadenAfterFailure
  cases (parse s raw).isNone with
  | true => exact expose_stock more s
  | false => rfl

/-! ## The supplied context -/

/-- The context received. -/
def context : List Sound := [.a, .b, .a, .b, .c, .d, .c, .d, .a, .b]
/-- Further encounters available after a failure. -/
def additional : List Sound := [.c, .d, .c, .d, .a, .b]
/-- The utterance: second word, first word, second word. -/
def utterance : List Sound := [.c, .d, .a, .b, .c, .d]
/-- What the utterance means. -/
def intended : Expr := .join (.join p1 p0) p1

/-- The formation developed from `n` units and four parts, with an empty log. -/
def ready (n : Nat) : State := ⟨develop (prepared n 4), []⟩
/-- After the context. -/
def experienced (n : Nat) : State := expose (context.map some) (ready n)
/-- After two encounters of the first word. -/
def narrow (n : Nat) : State := expose ([.a, .b, .a, .b].map some) (ready n)
/-- After broadening from the narrow course. -/
def broadened (n : Nat) : State := broadenAfterFailure utterance (additional.map some) (narrow n)

/-- **After the context, the log's majority bonds are the ideal relation.** -/
theorem context_forms_bond (x y : Sound) : bond (experienced 28).log x y = idealBond x y := by
  cases x <;> cases y <;> decide

/-- **After the context, every word sequence is grouped into its words.** -/
theorem context_groups_words (ws : List Bool) :
    chunks (bond (experienced 28).log) (encode word ws) = ws.map word :=
  (two_word_iff _).mpr ⟨context_forms_bond .a .b, context_forms_bond .c .d,
    context_forms_bond .b .a, context_forms_bond .b .c, context_forms_bond .d .a,
    context_forms_bond .d .c⟩ ws

/-- **After the context, every word sequence is assembled into its message.** -/
theorem context_assembles (ws : List Bool) :
    parse (experienced 28) (encode word ws) = assembleMessage (ws.map Expr.atom) := by
  unfold parse
  rw [context_groups_words ws, decodes_words ws]
  rfl

/-- **Before any encounter the utterance is not parsed or answered.** -/
theorem unexposed_unparsed : parse (ready 28) utterance = none ∧ act utterance (ready 28) = none := by
  decide

/-- **After the context the utterance parses into the intended form and the formed operation
answers it**, drawing the rest of the stock. -/
theorem grouping_reaches_program :
    parse (experienced 28) utterance = some intended ∧
    (act utterance (experienced 28)).map (fun r => (r.1, r.2.machine.stock, r.2.machine.drawn)) =
      some ([true, false, true], 0, 21) := by decide

/-- **The response keeps the context's log and the original acquisition.** -/
theorem response_keeps_log :
    (act utterance (experienced 28)).map (fun r => (r.2.log, r.2.machine.samples)) =
      some (context.map some, trialRecords usual) := by decide

/-- **The account of the whole history.** -/
theorem history_account :
    (ready 28).machine.stock = 14 ∧ (experienced 28).machine.stock = 4 ∧ 7 + 7 + 10 + 4 = 28 := by
  decide

/-- **With one unit less, the utterance parses but is not answered.** -/
theorem parsed_short :
    parse (experienced 27) utterance = some intended ∧ act utterance (experienced 27) = none := by
  decide

/-- **A gap breaks a transition.** -/
theorem gap_breaks_edge :
    edges [some Sound.a, none, some .b] = [] ∧
    bond [some Sound.a, none, some .b] .a .b = false ∧
    bond [some Sound.a, some .b] .a .b = true := by decide

/-- A course with every sound as often as the context, in another order. -/
def reordered : List Sound := [.a, .a, .a, .b, .b, .b, .c, .c, .d, .d]

/-- **The reordered course holds every sound as often as the context.** -/
theorem counts_agree (x : Sound) :
    countIf (fun y => decide (y = x)) context = countIf (fun y => decide (y = x)) reordered := by
  cases x <;> decide

/-- **The order of encounters changes the grouping and its use.** -/
theorem order_changes_grouping :
    bond (context.map some) .a .b = true ∧ bond (reordered.map some) .a .b = false ∧
    parse (expose (reordered.map some) (ready 28)) utterance = none := by decide

/-- **After a narrow course the utterance fails, and broadening reaches the context.** -/
theorem broaden_reaches_context :
    parse (narrow 28) utterance = none ∧
    (broadened 28).log = context.map some ∧
    parse (broadened 28) utterance = some intended ∧
    (act utterance (broadened 28)).map Prod.fst = some [true, false, true] := by decide

/-- **A parsed message does not broaden.** -/
theorem parsed_keeps : broadenAfterFailure [.a, .b] (additional.map some) (narrow 28) = narrow 28 := by
  decide

/-- **With short stock, broadening keeps only a prefix and the utterance still fails.** -/
theorem broaden_prefix :
    (broadened 19).log = ([.a, .b, .a, .b, .c] : List Sound).map some ∧
    parse (broadened 19) utterance = none := by decide

/-- **With a little more stock, broadening parses this utterance unanswered while failing on
another form.** -/
theorem broaden_one_form :
    (broadened 21).log = ([.a, .b, .a, .b, .c, .d, .c] : List Sound).map some ∧
    parse (broadened 21) utterance = some intended ∧
    act utterance (broadened 21) = none ∧
    parse (broadened 21) [.c, .d, .c, .d] = none := by decide

/-- Two encounters of the first word. -/
def learnerFavored : List Sound := [.a, .b, .a, .b]

/-- **Repetition can join across the intended words.** -/
theorem repetition_joins_words :
    chunks (bond (learnerFavored.map some)) learnerFavored = [learnerFavored] ∧
    decodeChunk learnerFavored = none := by decide

/-! ## Reception as a process -/

/-- Reception of observation slots, as a process: receiving `e` takes `s` to `receive e s`. -/
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

/-- **Every trace of reception keeps stock plus drawn.** -/
theorem total_kept {s t : State} {es : List (Option Sound)} (path : Trace reception s es t) :
    t.machine.stock + t.machine.drawn = s.machine.stock + s.machine.drawn :=
  along (Q := fun t => t.machine.stock + t.machine.drawn = s.machine.stock + s.machine.drawn)
    (expose_stock es s) t path

/-- **Without stock, reception leaves the configuration as it is along every trace.** -/
theorem still_without_support : ∀ {s t : State} {es : List (Option Sound)},
    Trace reception s es t → s.machine.stock = 0 → t = s
  | _, _, _, .nil _, _ => rfl
  | _, _, _, .cons step rest, short =>
    have kept := (step_iff.mp step).trans (receive_short _ _ short)
    (still_without_support rest
      ((congrArg (fun m : State => m.machine.stock) kept).trans short)).trans kept

/-- **Broadening reaches its configuration by a trace of reception, keeping stock plus drawn.** -/
theorem broadening_trace (raw : List Sound) (more : List (Option Sound)) (s : State) :
    ∃ es, Trace reception s es (broadenAfterFailure raw more s) ∧
      (broadenAfterFailure raw more s).machine.stock +
        (broadenAfterFailure raw more s).machine.drawn = s.machine.stock + s.machine.drawn :=
  have path : ∃ es, Trace reception s es (broadenAfterFailure raw more s) := by
    unfold broadenAfterFailure
    cases (parse s raw).isNone with
    | true => exact ⟨more, expose_trace more s⟩
    | false => exact ⟨[], .nil s⟩
  match path with
  | ⟨es, path⟩ => ⟨es, path, broaden_stock raw more s⟩

/-- **Along the trace of the context, every word sequence is assembled into its message.** -/
theorem grouping_assembles :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      ∀ ws, parse t (encode word ws) = assembleMessage (ws.map Expr.atom) :=
  along (Q := fun t => ∀ ws, parse t (encode word ws) = assembleMessage (ws.map Expr.atom))
    context_assembles

/-- **Reception along the context changes the parse of the utterance.** -/
theorem reception_changes_parse :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      (parse (ready 28) utterance = none ∧ act utterance (ready 28) = none) ∧
      (parse t utterance = some intended ∧
        (act utterance t).map (fun r => (r.1, r.2.machine.stock, r.2.machine.drawn)) =
          some ([true, false, true], 0, 21)) :=
  fun t path => ⟨unexposed_unparsed,
    along (Q := fun t => parse t utterance = some intended ∧
        (act utterance t).map (fun r => (r.1, r.2.machine.stock, r.2.machine.drawn)) =
          some ([true, false, true], 0, 21))
      grouping_reaches_program t path⟩

/-- **The response at the end of the trace of the context keeps its log and the original
acquisition.** -/
theorem response_keeps_history :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      (act utterance t).map (fun r => (r.2.log, r.2.machine.samples)) =
        some (context.map some, trialRecords usual) :=
  along (Q := fun t => (act utterance t).map (fun r => (r.2.log, r.2.machine.samples)) =
      some (context.map some, trialRecords usual))
    response_keeps_log

/-- **Along the trace of the context, stock falls from 14 to 4.** -/
theorem support_used :
    ∀ t, Trace reception (ready 28) (context.map some) t →
      (ready 28).machine.stock = 14 ∧ t.machine.stock = 4 ∧ 7 + 7 + 10 + 4 = 28 :=
  fun t path =>
    ⟨history_account.1, along (Q := fun t => t.machine.stock = 4) history_account.2.1 t path,
     history_account.2.2⟩

/-- **With 27 units, the utterance parses at the end of the trace of the context unanswered.** -/
theorem parse_without_support :
    ∀ t, Trace reception (ready 27) (context.map some) t →
      parse t utterance = some intended ∧ act utterance t = none :=
  along (Q := fun t => parse t utterance = some intended ∧ act utterance t = none) parsed_short

/-- **Order, not frequency.** -/
theorem order_not_frequency :
    (∀ x, countIf (fun y => decide (y = x)) context = countIf (fun y => decide (y = x)) reordered) ∧
    ∀ t t', Trace reception (ready 28) (context.map some) t →
      Trace reception (ready 28) (reordered.map some) t' →
        parse t utterance = some intended ∧ parse t' utterance = none :=
  ⟨counts_agree, fun t t' path path' =>
    ⟨along (Q := fun t => parse t utterance = some intended) grouping_reaches_program.1 t path,
     along (Q := fun t => parse t utterance = none) order_changes_grouping.2.2 t' path'⟩⟩

/-- The narrow course: two encounters of the first word. -/
abbrev narrowCourse : List (Option Sound) := ([Sound.a, .b, .a, .b] : List Sound).map some

/-- **Broadening after a narrow trace reaches the context, the parse and the response.** -/
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
    broaden_reaches_context

/-- **A parsed message does not broaden** at the end of the narrow course. -/
theorem parsed_not_broadened :
    ∀ t, Trace reception (ready 28) narrowCourse t →
      broadenAfterFailure [.a, .b] (additional.map some) t = t :=
  along (Q := fun t => broadenAfterFailure [.a, .b] (additional.map some) t = t) parsed_keeps

/-- **With 19 units, broadening after the narrow course keeps a prefix and still fails.** -/
theorem broadening_keeps_prefix :
    ∀ t, Trace reception (ready 19) narrowCourse t →
      (broadenAfterFailure utterance (additional.map some) t).log =
          ([Sound.a, .b, .a, .b, .c] : List Sound).map some ∧
        parse (broadenAfterFailure utterance (additional.map some) t) utterance = none :=
  along (Q := fun t => (broadenAfterFailure utterance (additional.map some) t).log =
          ([Sound.a, .b, .a, .b, .c] : List Sound).map some ∧
        parse (broadenAfterFailure utterance (additional.map some) t) utterance = none)
    broaden_prefix

/-- **With 21 units, broadening after the narrow course parses the utterance unanswered while
failing on another form.** -/
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
    broaden_one_form

end LearnedGrouping

end Becoming
