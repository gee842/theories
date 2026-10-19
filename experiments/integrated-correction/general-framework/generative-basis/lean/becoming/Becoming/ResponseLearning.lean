import Becoming.RouteFormation
import Becoming.Branching

/-!
# Response learning: forming an operation from another formation's actual responses

`Becoming.RouteFormation` forms an operation from samples. Here the samples are another
formation's actual responses: in a teaching pair (`Teaching`), a query sent to the sender takes
its response, at the draw the response makes, and adds it with the query to the receiver's
samples at the draw of one unit (`send`); a lesson sends queries in turn (`lesson`), and learning
develops what a lesson delivered (`learn`). A successor is what a fresh formation learns from a
teacher on the basic lesson (`successor`), so succession is a determined law and its runs are
generations (`cohort`). This module states, on the core's processes and runs, what
`CompositionalTransmission` (7 October) proved, and what the joins `QueryTraces` and
`QueryTracesInherited` (17 October) read through the core, with every proof constructive (board
item F3Q, 18 October 2026). The mature starting programs, the grammar, the search, the schedule,
faithful reception and each fresh formation's stock are supplied; nothing biological or a law of
cultural progress is claimed.

* **One query.** What a response leaves is within the sender's stock (`response_within_stock`);
  a query keeps the pair's stock plus drawn (`send_stock`), and so does a lesson
  (`lesson_stock`). A ready receiver with stock receives the sender's actual response
  (`send_delivers`); without a response no sample is added (`send_no_response`).
* **What the receiver sees.** The receiver sees only responses: two pairs alike in the receiver
  and in the sender's installed program and stock stay alike along every lesson
  (`send_interface`, `lesson_interface`), so learning from a teacher depends only on its installed
  program and stock (`learn_through_interface`).
* **Reconstruction and succession.** From a sender running a program of two sockets with seven
  units, the basic lesson delivers the program's records (`basic_lesson_records`), and the
  learner reconstructs the program, with seven units left, where its primitives differ
  (`reconstructs_program`); so every successor keeps it (`successor_keeps`), every generation
  holds it (`every_cohort_holds`), and every generation's program evaluates every expression
  as the code does (`every_cohort_corresponds`).
* **Faithful is not correct.** A sender ignoring the second argument of each join is reconstructed
  faithfully and loses a distinction the task makes, in every generation, whatever the stock
  (`faithful_loses_distinction`, `stock_keeps_content`, `distinction_lost_every_cohort`); the
  same teacher yields different programs after different lessons (`lessons_change_program`); a
  peer's demonstration repairs a reconstruction or keeps an error (`peer_repairs`,
  `peer_keeps_error_example`); a received disagreement without stock is not repaired
  (`short_receiver_not_repaired`); the collapsed code's limitation changes the program once and
  then stays (`limited_changes_then_stays`, `limited_fails_task`).
* **As processes.** The pair under queries is a process whose courses are exactly the lessons
  (`queryProcess`, `trace_iff`), and succession is `Law.process successor`, whose runs pass
  through the generations (`run_cohort`); the laws above are stated of courses and runs
  (`step_delivers`, `course_stock`, `learned_*`, `succession_*`, `formed_succession_*`,
  `execution_stock_succession_blocked`, `peer_repair`, `peer_keeps_error`).

No ethical predicate or ranking occurs, and every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

namespace ResponseLearning

open CodeAcquisition RouteFormation

/-! ## Arithmetic used below -/

/-! ## Teaching pairs -/

/-- A sender and a receiver. -/
structure Teaching where
  sender : Apparatus
  receiver : Apparatus
  deriving DecidableEq

/-- A fresh formation with a stock and parts. -/
def blank (stock parts : Nat) : Apparatus := fromLearner (initial stock) parts

/-- A mature sender running the program `p`, with a stock; a supplied starting condition. -/
def source (p : Program) (stock : Nat) : Apparatus :=
  { blank stock 0 with wires := p.route, installed := some p }

/-- Send a query given the sender's response `o`: a blocked receiver changes nothing; a receiver
without stock, or a sender without a response, blocks; otherwise the receiver adds the response at
one unit and the sender keeps what its response left. -/
def sendWith (o : Option (List Bool × Nat)) (e : Expr) (x : Teaching) : Teaching :=
  bif x.receiver.blocked then x else
  match x.receiver.stock, o with
  | 0, _ => { x with receiver := { x.receiver with blocked := true } }
  | _ + 1, none => { x with receiver := { x.receiver with blocked := true } }
  | n + 1, some (output, remaining) =>
    ⟨{ x.sender with stock := remaining, drawn := x.sender.drawn + (x.sender.stock - remaining) },
     { x.receiver with
       samples := x.receiver.samples ++ [(e, output)], stock := n, drawn := x.receiver.drawn + 1 }⟩

/-- Send a query: the sender's actual response is delivered. -/
def send (e : Expr) (x : Teaching) : Teaching := sendWith (respond x.sender e) e x

/-- Send queries in turn. -/
def lesson : List Expr → Teaching → Teaching
  | [], x => x
  | e :: es, x => lesson es (send e x)

/-- The basic queries: the three probes. -/
def basic : List Expr := [p0, p1, orderProbe]
/-- The basic queries and the novel expression. -/
def extended : List Expr := basic ++ [novel]

/-- What a fresh formation learns from a teacher: develop what the lesson delivered. -/
def learn (teacher : Apparatus) (stock parts : Nat) (queries : List Expr := basic) : Apparatus :=
  develop (lesson queries ⟨teacher, blank stock parts⟩).receiver

/-- A program's records on the three probes. -/
def programRecords (p : Program) : List (Expr × List Bool) :=
  [(p0, operate p p0), (p1, operate p p1), (orderProbe, operate p orderProbe)]

/-! ## One query -/

/-- **What a response leaves is within the sender's stock.** -/
theorem response_within_stock (s : Apparatus) (e : Expr) {out : List Bool} {left : Nat}
    (h : respond s e = some (out, left)) : left ≤ s.stock := by
  unfold respond at h
  cases hi : s.installed with
  | none => rw [hi] at h; exact nomatch h
  | some p =>
    rw [hi] at h
    dsimp only at h
    rcases Nat.lt_or_ge s.stock (1 + (operate p e).length) with short | enough
    · rw [if_neg (Nat.not_le_of_lt short)] at h
      exact nomatch h
    · rw [if_pos enough] at h
      have same : s.stock - (1 + (operate p e).length) = left := congrArg Prod.snd (Option.some.inj h)
      exact same ▸ Nat.sub_le _ _

/-- The pair's stock plus drawn. -/
def joint (x : Teaching) : Nat := x.sender.stock + x.sender.drawn + x.receiver.stock + x.receiver.drawn

theorem sender_kept {rem ss ds : Nat} (le : rem ≤ ss) : rem + (ds + (ss - rem)) = ss + ds := by
  rw [Nat.add_left_comm, add_sub_of_le le, Nat.add_comm]

theorem regroup (a b c d : Nat) : a + b + c + d = (a + b) + (c + d) := Nat.add_assoc (a + b) c d

/-- **A query given a response within the sender's stock keeps the pair's stock plus drawn.** -/
theorem sendWith_stock (e : Expr) :
    ∀ (o : Option (List Bool × Nat)) (x : Teaching),
      (∀ out rem, o = some (out, rem) → rem ≤ x.sender.stock) → joint (sendWith o e x) = joint x
  | _, ⟨_, ⟨_, _, _, _, _, _, true, _, _⟩⟩, _ => rfl
  | _, ⟨_, ⟨_, _, 0, _, _, _, false, _, _⟩⟩, _ => rfl
  | none, ⟨_, ⟨_, _, _ + 1, _, _, _, false, _, _⟩⟩, _ => rfl
  | some (out, rem), ⟨⟨w, i, ss, ds, pa, u, b, sa, at_⟩, ⟨_, _, n + 1, dr, _, _, false, _, _⟩⟩, bound => by
    show rem + (ds + (ss - rem)) + n + (dr + 1) = ss + ds + (n + 1) + dr
    rw [regroup, regroup, sender_kept (bound out rem rfl), Nat.add_succ n dr, Nat.succ_add n dr]

/-- **A query keeps the pair's stock plus drawn.** -/
theorem send_stock (e : Expr) (x : Teaching) : joint (send e x) = joint x :=
  sendWith_stock e (respond x.sender e) x fun _ _ h => response_within_stock x.sender e h

/-- **A lesson keeps the pair's stock plus drawn.** -/
theorem lesson_stock : ∀ (es : List Expr) (x : Teaching), joint (lesson es x) = joint x
  | [], _ => rfl
  | e :: es, x => (lesson_stock es (send e x)).trans (send_stock e x)

/-- **A ready receiver with stock receives the sender's actual response**, and the sender keeps what
its response left. -/
theorem send_delivers (e : Expr) (x : Teaching) (ready : x.receiver.blocked = false)
    (stock : 1 ≤ x.receiver.stock) (out : List Bool) (remaining : Nat)
    (actual : respond x.sender e = some (out, remaining)) :
    (send e x).receiver.samples = x.receiver.samples ++ [(e, out)] ∧
      (send e x).sender.stock = remaining := by
  unfold send
  rw [actual]
  rcases x with ⟨xs, ⟨w, i, st, d, pa, u, bl, sa, at_⟩⟩
  cases ready
  cases st with
  | zero => exact absurd stock (Nat.not_succ_le_zero 0)
  | succ n => exact ⟨rfl, rfl⟩

/-- **Without a response, no sample is added.** -/
theorem send_no_response (e : Expr) (x : Teaching) (absent : respond x.sender e = none) :
    (send e x).receiver.samples = x.receiver.samples := by
  unfold send
  rw [absent]
  rcases x with ⟨xs, ⟨w, i, st, d, pa, u, bl, sa, at_⟩⟩
  cases bl with
  | true => rfl
  | false =>
    cases st with
    | zero => rfl
    | succ n => rfl

/-! ## What the receiver sees -/

/-- Two pairs alike in the receiver, and in the sender's installed program and stock. -/
def SameInterface (x y : Teaching) : Prop :=
  x.receiver = y.receiver ∧ x.sender.installed = y.sender.installed ∧ x.sender.stock = y.sender.stock

theorem respond_congr {s s' : Apparatus} (e : Expr) (hi : s.installed = s'.installed)
    (hs : s.stock = s'.stock) : respond s e = respond s' e := by
  unfold respond
  rw [hi, hs]

theorem sendWith_interface (e : Expr) (o : Option (List Bool × Nat)) (x y : Teaching)
    (same : SameInterface x y) : SameInterface (sendWith o e x) (sendWith o e y) := by
  rcases x with ⟨xs, xr⟩
  rcases y with ⟨ys, yr⟩
  obtain ⟨hr, hi, hs⟩ := same
  change xr = yr at hr
  subst hr
  rcases xr with ⟨w, i, st, d, pa, u, bl, sa, at_⟩
  cases bl with
  | true => exact ⟨rfl, hi, hs⟩
  | false =>
    cases st with
    | zero => exact ⟨rfl, hi, hs⟩
    | succ n =>
      cases o with
      | none => exact ⟨rfl, hi, hs⟩
      | some r => exact ⟨rfl, hi, rfl⟩

/-- **A query keeps two pairs alike in what the receiver sees.** -/
theorem send_interface (e : Expr) (x y : Teaching) (same : SameInterface x y) :
    SameInterface (send e x) (send e y) := by
  have answer : respond x.sender e = respond y.sender e := respond_congr e same.2.1 same.2.2
  show SameInterface (sendWith (respond x.sender e) e x) (sendWith (respond y.sender e) e y)
  rw [answer]
  exact sendWith_interface e _ x y same

/-- **A lesson keeps two pairs alike in what the receiver sees.** -/
theorem lesson_interface : ∀ (es : List Expr) (x y : Teaching), SameInterface x y →
    SameInterface (lesson es x) (lesson es y)
  | [], _, _, same => same
  | e :: es, x, y, same => lesson_interface es _ _ (send_interface e x y same)

/-- **Learning from a teacher depends only on its installed program and stock.** -/
theorem learn_through_interface (t : Apparatus) (p : Program) (installed : t.installed = some p)
    (stock parts : Nat) (es : List Expr) :
    learn t stock parts es = learn (source p t.stock) stock parts es :=
  congrArg develop (lesson_interface es ⟨t, blank stock parts⟩ ⟨source p t.stock, blank stock parts⟩
    ⟨rfl, installed, rfl⟩).1

/-! ## Reconstruction and succession -/

/-- **From a sender running a program of two sockets with at least seven units, the basic lesson
delivers the program's records.** -/
theorem basic_lesson_records (p : Program) (n : Nat) (routes : p.route ∈ generatedRoutes 2)
    (enough : 7 ≤ n) :
    (lesson basic ⟨source p n, blank 25 8⟩).receiver =
      { blank 22 8 with drawn := 3, samples := programRecords p } := by
  obtain ⟨m, rfl⟩ := exists_add_of_le enough
  rcases p with ⟨a, b, r⟩
  rcases mem_two_socket routes with rfl | rfl | rfl | rfl <;> cases a <;> cases b <;> rfl

/-- **The learner reconstructs the sender's program, with seven units left**, where its primitives
differ. -/
theorem reconstructs_program (p : Program) (n : Nat) (routes : p.route ∈ generatedRoutes 2)
    (distinct : p.first ≠ p.second) (enough : 7 ≤ n) :
    (learn (source p n) 25 8).installed = some p ∧ 7 ≤ (learn (source p n) 25 8).stock := by
  show (develop (lesson basic ⟨source p n, blank 25 8⟩).receiver).installed = some p ∧
    7 ≤ (develop (lesson basic ⟨source p n, blank 25 8⟩).receiver).stock
  rw [basic_lesson_records p n routes enough]
  rcases p with ⟨a, b, r⟩
  rcases mem_two_socket routes with rfl | rfl | rfl | rfl <;> cases a <;> cases b <;>
    first | exact absurd rfl distinct | decide

/-- What a fresh formation with twenty-five units and eight parts learns from a teacher. -/
def successor (t : Apparatus) : Apparatus := learn t 25 8

/-- **A successor keeps an installed program** of two sockets with distinct primitives, where the
teacher has seven units; the successor again has seven. -/
theorem successor_keeps (t : Apparatus) (p : Program) (installed : t.installed = some p)
    (routes : p.route ∈ generatedRoutes 2) (distinct : p.first ≠ p.second) (enough : 7 ≤ t.stock) :
    (successor t).installed = some p ∧ 7 ≤ (successor t).stock := by
  show (learn t 25 8).installed = some p ∧ 7 ≤ (learn t 25 8).stock
  rw [learn_through_interface t p installed 25 8 basic]
  exact reconstructs_program p t.stock routes distinct enough

/-- The generations from a teacher running `p` with seven units. -/
def cohort (p : Program) : Nat → Apparatus
  | 0 => source p 7
  | n + 1 => successor (cohort p n)

/-- **Every generation holds the program**, with seven units. -/
theorem every_cohort_holds (p : Program) (routes : p.route ∈ generatedRoutes 2)
    (distinct : p.first ≠ p.second) : ∀ n, (cohort p n).installed = some p ∧ 7 ≤ (cohort p n).stock
  | 0 => ⟨rfl, Nat.le_refl 7⟩
  | n + 1 => match every_cohort_holds p routes distinct n with
    | ⟨installed, enough⟩ => successor_keeps _ p installed routes distinct enough

theorem routeFor_generated (c : Code) : routeFor c ∈ generatedRoutes 2 :=
  match c with
  | ⟨_, _, false⟩ => .tail _ (.head _)
  | ⟨_, _, true⟩ => .tail _ (.tail _ (.head _))

/-- **Every generation's program evaluates every expression as the code does.** -/
theorem every_cohort_corresponds (c : Code) (distinct : c.first ≠ c.second) (n : Nat) (e : Expr) :
    ∃ p, (cohort (programFor c) n).installed = some p ∧ operate p e = eval c e :=
  ⟨programFor c, (every_cohort_holds _ (routeFor_generated c) distinct n).1, programFor_operates c e⟩

/-! ## The examples -/

/-- A program ignoring the second argument of each join. -/
def selective : Program := ⟨false, true, [false, false]⟩
/-- The first atom joined to itself. -/
def joint00 : Expr := .join p0 p0

/-- What a fresh formation learns from the developed apparatus. -/
def firstLearner : Apparatus := learn developed 25 8

/-- **A formed teacher teaches after a covered preparation.** -/
theorem formed_teacher_teaches :
    (develop (prepared 25 4)).installed = some (programFor usual) ∧
    (learn (develop (prepared 25 4)) 25 8).installed = some (programFor usual) := by decide

/-- **A teacher with stock only for executing can interrupt teaching.** -/
theorem execution_stock_interrupts :
    (lesson basic ⟨developed, blank 25 8⟩).receiver.samples = [(p0, [false]), (p1, [true])] ∧
    firstLearner.installed = none ∧ firstLearner.blocked = true := by decide

/-- **The teacher's program changes the received evidence.** -/
theorem teacher_changes_evidence :
    (lesson basic ⟨source selective 7, blank 25 8⟩).receiver.samples = programRecords selective ∧
    programRecords selective ≠ trialRecords usual := by decide

/-- **A faithfully reconstructed program can lose a distinction the task makes.** -/
theorem faithful_loses_distinction :
    (learn (source selective 7) 25 8).installed = some selective ∧
    operate selective joint00 = operate selective orderProbe ∧
    eval usual joint00 ≠ eval usual orderProbe := by decide

/-- **More stock does not change the transmitted content.** -/
theorem stock_keeps_content : (learn (source selective 70) 100 80).installed = some selective := by
  decide

/-- **The same teacher, different lessons, different programs.** -/
theorem lessons_change_program :
    (learn (source (programFor collapsed) 11) 25 8 basic).installed = some duplicated ∧
    (learn (source (programFor collapsed) 11) 25 8 extended).installed = some (programFor collapsed) := by
  decide

/-- A peer that learned the duplicating program. -/
def misleadingPeer : Apparatus := learn (source (programFor collapsed) 11) 25 8 basic
/-- The peer after one demonstration of the novel expression and reconsideration. -/
def revisedPeer : Apparatus :=
  reconsider (send novel ⟨source (programFor collapsed) 4, misleadingPeer⟩).receiver

/-- **A peer's demonstration can repair without a new generation.** -/
theorem peer_repairs :
    misleadingPeer.installed = some duplicated ∧ revisedPeer.installed = some (programFor collapsed) ∧
    respond revisedPeer further = some ([false, false, false], 5) := by decide

/-- **An erroneous peer's demonstration can keep the error.** -/
theorem peer_keeps_error_example :
    (reconsider (send novel ⟨source duplicated 5, misleadingPeer⟩).receiver).installed =
      some duplicated := by decide

/-- **A received disagreement is not repaired without stock.** -/
theorem short_receiver_not_repaired :
    (learn (source (programFor collapsed) 11) 5 8 extended).installed = none := by decide

/-- **The lost distinction recurs in every generation.** -/
theorem distinction_lost_every_cohort (n : Nat) :
    (cohort selective n).installed = some selective ∧
    operate selective joint00 = operate selective orderProbe ∧
    eval usual joint00 ≠ eval usual orderProbe :=
  ⟨(every_cohort_holds selective (.head _) Bool.noConfusion n).1, by decide, by decide⟩

/-- **A successful reconstruction can teach a later formation.** -/
theorem reconstruction_teaches_later :
    (successor (learn (develop (prepared 25 4)) 25 8)).installed = some (programFor usual) := by decide

/-- **The duplicating program is reconstructed after an actual lesson.** -/
theorem duplicate_reconstructed (t : Apparatus) (installed : t.installed = some duplicated)
    (enough : 7 ≤ t.stock) :
    (successor t).installed = some duplicated ∧ 7 ≤ (successor t).stock := by
  show (learn t 25 8 basic).installed = some duplicated ∧ 7 ≤ (learn t 25 8 basic).stock
  rw [learn_through_interface t duplicated installed 25 8 basic]
  show (develop (lesson basic ⟨source duplicated t.stock, blank 25 8⟩).receiver).installed =
      some duplicated ∧ 7 ≤ (develop (lesson basic ⟨source duplicated t.stock, blank 25 8⟩).receiver).stock
  rw [basic_lesson_records duplicated t.stock (.head _) enough]
  decide

/-- The generations from the collapsed code's teacher. -/
def limitedCohort : Nat → Apparatus
  | 0 => source (programFor collapsed) 7
  | n + 1 => successor (limitedCohort n)

/-- **The initial limitation changes the program once, and then it stays.** -/
theorem limited_changes_then_stays :
    ∀ n, (limitedCohort (n + 1)).installed = some duplicated ∧ 7 ≤ (limitedCohort (n + 1)).stock
  | 0 => by decide
  | n + 1 => match limited_changes_then_stays n with
    | ⟨installed, enough⟩ => duplicate_reconstructed _ installed enough

/-- **The stabilized program fails the original task.** -/
theorem limited_fails_task (n : Nat) :
    (limitedCohort (n + 1)).installed = some duplicated ∧ operate duplicated novel ≠ eval collapsed novel :=
  ⟨(limited_changes_then_stays n).1, by decide⟩

/-! ## The pair under queries as a process -/

/-- A query takes a pair to the pair after the query is sent. -/
def deliver (x : Teaching) (e : Expr) : Teaching := send e x

/-- The pair read as a process: configurations are pairs, moves are queries. -/
def queryProcess : Process Teaching Expr := Assurance.ofMap deliver

/-- **A lesson is the fold of its queries.** -/
theorem lesson_foldl : ∀ (es : List Expr) (x : Teaching), lesson es x = es.foldl deliver x
  | [], _ => rfl
  | e :: es, x => lesson_foldl es (send e x)

/-- Every lesson is a course of the query process. -/
theorem lesson_trace : ∀ (es : List Expr) (x : Teaching), Trace queryProcess x es (lesson es x)
  | [], x => .nil x
  | e :: es, x => .cons (rfl : send e x = deliver x e) (lesson_trace es (send e x))

/-- **The courses of the query process are exactly the lessons.** -/
theorem trace_iff {x y : Teaching} {es : List Expr} : Trace queryProcess x es y ↔ y = lesson es x :=
  ⟨fun course => (ReducedRuns.trace_foldl course).trans (lesson_foldl es x).symm,
   fun ends => ends ▸ lesson_trace es x⟩

/-- **The record follows the sender's program**, which is not the usual code's. -/
theorem course_records_follow_sender {y : Teaching}
    (course : Trace queryProcess ⟨source selective 7, blank 25 8⟩ basic y) :
    y.receiver.samples = programRecords selective ∧ programRecords selective ≠ trialRecords usual :=
  (trace_iff.mp course) ▸ teacher_changes_evidence

/-- **From the collapsed code's teacher, the basic course delivers the code's probe records.** -/
theorem basic_course_records {y : Teaching}
    (course : Trace queryProcess ⟨source (programFor collapsed) 7, blank 25 8⟩ basic y) :
    y.receiver.samples = trialRecords collapsed :=
  (trace_iff.mp course) ▸ (by decide :
    (lesson basic ⟨source (programFor collapsed) 7, blank 25 8⟩).receiver.samples = trialRecords collapsed)

/-- **A delivered record can fit a departing program.** -/
theorem course_record_fits_departing {y : Teaching}
    (course : Trace queryProcess ⟨source (programFor collapsed) 7, blank 25 8⟩ basic y) :
    fits duplicated y.receiver.samples = true ∧ operate duplicated novel ≠ eval collapsed novel :=
  (basic_course_records course) ▸ old_records_admit_duplicate

/-- **The extended course delivers the probe records and the novel response.** -/
theorem extended_course_records {y : Teaching}
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ extended y) :
    y.receiver.samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] :=
  (trace_iff.mp course) ▸ (by decide :
    (lesson extended ⟨source (programFor collapsed) 11, blank 25 8⟩).receiver.samples =
      trialRecords collapsed ++ [(novel, eval collapsed novel)])

/-- **A longer course separates the programs.** -/
theorem extended_course_separates {y : Teaching}
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ extended y) :
    fits duplicated y.receiver.samples = false ∧ fits (programFor collapsed) y.receiver.samples = true :=
  (extended_course_records course) ▸ novel_record_separates

/-- **A query step delivers the sender's actual response.** -/
theorem step_delivers {x y : Teaching} {e : Expr} (step : queryProcess.step x e y)
    (ready : x.receiver.blocked = false) (stock : 1 ≤ x.receiver.stock) {out : List Bool}
    {remaining : Nat} (actual : respond x.sender e = some (out, remaining)) :
    y.receiver.samples = x.receiver.samples ++ [(e, out)] ∧ y.sender.stock = remaining :=
  step ▸ send_delivers e x ready stock out remaining actual

/-- **Without a response, a query step adds no sample.** -/
theorem step_no_response {x y : Teaching} {e : Expr} (step : queryProcess.step x e y)
    (absent : respond x.sender e = none) : y.receiver.samples = x.receiver.samples :=
  step ▸ send_no_response e x absent

/-- **Every course of queries keeps the pair's stock plus drawn.** -/
theorem course_stock {x y : Teaching} {es : List Expr} (course : Trace queryProcess x es y) :
    joint y = joint x :=
  (trace_iff.mp course) ▸ lesson_stock es x

/-- **A course omitting the composite query gives no code.** -/
theorem course_without_composite {y : Teaching}
    (course : Trace queryProcess ⟨source (programFor usual) 4, blank 25 8⟩ [p0, p1] y) :
    interpretationFromRecords y.receiver.samples = none :=
  (trace_iff.mp course) ▸ (by decide :
    interpretationFromRecords (lesson [p0, p1] ⟨source (programFor usual) 4, blank 25 8⟩).receiver.samples =
      none)

/-- **A sender with a reversed composite response gives the switched code.** -/
theorem course_reversed_composite {y : Teaching}
    (course : Trace queryProcess ⟨source ⟨false, true, [true, false]⟩ 7, blank 25 8⟩ basic y) :
    interpretationFromRecords y.receiver.samples = some switched :=
  (trace_iff.mp course) ▸ (by decide :
    interpretationFromRecords
        (lesson basic ⟨source ⟨false, true, [true, false]⟩ 7, blank 25 8⟩).receiver.samples =
      some switched)

section Learning

variable {y y' : Teaching} {z z' : Apparatus}

/-- **More stock does not change what is reconstructed** after a course. -/
theorem learned_selective_stock (course : Trace queryProcess ⟨source selective 70, blank 100 80⟩ basic y)
    (formed : Trace formationProcess y.receiver [.develop] z) : z.installed = some selective :=
  (RouteFormation.trace_iff.mp formed) ▸ (trace_iff.mp course) ▸ stock_keeps_content

/-- **A faithful reconstruction after a course can lose a distinction of the task.** -/
theorem learned_selective_loses_distinction
    (course : Trace queryProcess ⟨source selective 7, blank 25 8⟩ basic y)
    (formed : Trace formationProcess y.receiver [.develop] z) :
    z.installed = some selective ∧ operate selective joint00 = operate selective orderProbe ∧
      eval usual joint00 ≠ eval usual orderProbe :=
  (RouteFormation.trace_iff.mp formed) ▸ (trace_iff.mp course) ▸ faithful_loses_distinction

/-- **The same teacher, different courses, different reconstructions.** -/
theorem learned_depends_on_course
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ basic y)
    (formed : Trace formationProcess y.receiver [.develop] z)
    (course' : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ extended y')
    (formed' : Trace formationProcess y'.receiver [.develop] z') :
    z.installed = some duplicated ∧ z'.installed = some (programFor collapsed) :=
  (RouteFormation.trace_iff.mp formed) ▸ (trace_iff.mp course) ▸
    (RouteFormation.trace_iff.mp formed') ▸ (trace_iff.mp course') ▸ lessons_change_program

/-- **A received disagreement is not repaired without stock.** -/
theorem learned_blocked_short
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 5 8⟩ extended y)
    (formed : Trace formationProcess y.receiver [.develop] z) : z.installed = none :=
  (RouteFormation.trace_iff.mp formed) ▸ (trace_iff.mp course) ▸ short_receiver_not_repaired

end Learning

section Succession

/-- **A succession step keeps an installed program** of two sockets with distinct primitives,
where the stock is at least seven. -/
theorem succession_step_keeps (r : Run (Law.process successor)) {p : Program} (n : Nat)
    (installed : (r.state n).installed = some p) (routes : p.route ∈ generatedRoutes 2)
    (distinct : p.first ≠ p.second) (enough : 7 ≤ (r.state n).stock) :
    (r.state (n + 1)).installed = some p ∧ 7 ≤ (r.state (n + 1)).stock :=
  (r.step n : r.state (n + 1) = successor (r.state n)) ▸
    successor_keeps (r.state n) p installed routes distinct enough

/-- The generations from a teacher are the orbit of succession from it. -/
theorem orbit_cohort (p : Program) : ∀ n, Law.orbit successor (source p 7) n = cohort p n
  | 0 => rfl
  | n + 1 => congrArg successor (orbit_cohort p n)

/-- The limited generations are the orbit of succession from the collapsed code's teacher. -/
theorem orbit_limited : ∀ n, Law.orbit successor (source (programFor collapsed) 7) n = limitedCohort n
  | 0 => rfl
  | n + 1 => congrArg successor (orbit_limited n)

/-- **Every run of succession from a teacher passes through the generations from it.** -/
theorem run_cohort {p : Program} {r : Run (Law.process successor)} (start : r.state 0 = source p 7)
    (n : Nat) : r.state n = cohort p n :=
  (Branching.law_run_state r n).trans
    ((congrArg (fun s => Law.orbit successor s n) start).trans (orbit_cohort p n))

/-- **Succession keeps the correspondence**: every run from a teacher running a code's program
holds at every date a program evaluating every expression as the code does. -/
theorem succession_keeps_correspondence {c : Code} {r : Run (Law.process successor)}
    (start : r.state 0 = source (programFor c) 7) (distinct : c.first ≠ c.second) (n : Nat) (e : Expr) :
    ∃ p, (r.state n).installed = some p ∧ operate p e = eval c e :=
  (run_cohort start n).symm ▸ every_cohort_corresponds c distinct n e

/-- **Succession keeps a lost distinction.** -/
theorem succession_keeps_lost_distinction {r : Run (Law.process successor)}
    (start : r.state 0 = source selective 7) (n : Nat) :
    (r.state n).installed = some selective ∧ operate selective joint00 = operate selective orderProbe ∧
      eval usual joint00 ≠ eval usual orderProbe :=
  (run_cohort start n).symm ▸ distinction_lost_every_cohort n

/-- **Succession stabilizes a change.** -/
theorem succession_stabilizes_change {r : Run (Law.process successor)}
    (start : r.state 0 = source (programFor collapsed) 7) (n : Nat) :
    (r.state (n + 1)).installed = some duplicated ∧ operate duplicated novel ≠ eval collapsed novel :=
  ((Branching.law_run_state r (n + 1)).trans
    ((congrArg (fun s => Law.orbit successor s (n + 1)) start).trans (orbit_limited (n + 1)))).symm ▸
    limited_fails_task n

/-- **The formed teacher teaches**: where the run starts where the course `[develop]` from the
prepared configuration ends, the teacher and its successor hold the usual program. -/
theorem formed_succession_teaches {r : Run (Law.process successor)}
    (start : Trace formationProcess (prepared 25 4) [.develop] (r.state 0)) :
    (r.state 0).installed = some (programFor usual) ∧ (r.state 1).installed = some (programFor usual) := by
  have h0 := RouteFormation.trace_iff.mp start
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  rw [h1, h0]
  exact formed_teacher_teaches

/-- **A reconstruction teaches a later formation**: on the same run, date two holds the usual
program. -/
theorem formed_succession_second {r : Run (Law.process successor)}
    (start : Trace formationProcess (prepared 25 4) [.develop] (r.state 0)) :
    (r.state 2).installed = some (programFor usual) := by
  have h0 := RouteFormation.trace_iff.mp start
  have h2 : r.state 2 = successor (successor (r.state 0)) := (r.step 1).trans (congrArg successor (r.step 0))
  rw [h2, h0]
  exact reconstruction_teaches_later

/-- **A teacher with stock only for executing interrupts teaching**: the basic course delivers
only the two primitive records, and the successor is blocked with nothing installed. -/
theorem execution_stock_succession_blocked {r : Run (Law.process successor)} {y : Teaching}
    (start : Trace formationProcess (prepared 18 4) [.develop] (r.state 0))
    (course : Trace queryProcess ⟨r.state 0, blank 25 8⟩ basic y) :
    y.receiver.samples = [(p0, [false]), (p1, [true])] ∧
      (r.state 1).installed = none ∧ (r.state 1).blocked = true := by
  have h0 := RouteFormation.trace_iff.mp start
  have hy := trace_iff.mp course
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  subst hy
  rw [h1, h0]
  exact execution_stock_interrupts

/-- **A peer's demonstration can repair without a new generation.** -/
theorem peer_repair {r : Run (Law.process successor)} {y : Teaching} {z : Apparatus}
    (start : r.state 0 = source (programFor collapsed) 11)
    (course : Trace queryProcess ⟨source (programFor collapsed) 4, r.state 1⟩ [novel] y)
    (revised : Trace formationProcess y.receiver [.reconsider] z) :
    (r.state 1).installed = some duplicated ∧ z.installed = some (programFor collapsed) ∧
      respond z further = some ([false, false, false], 5) := by
  have hz := RouteFormation.trace_iff.mp revised
  have hy := trace_iff.mp course
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  subst hz
  subst hy
  rw [h1, start]
  exact peer_repairs

/-- **An erroneous peer's demonstration keeps the error.** -/
theorem peer_keeps_error {r : Run (Law.process successor)} {y : Teaching} {z : Apparatus}
    (start : r.state 0 = source (programFor collapsed) 11)
    (course : Trace queryProcess ⟨source duplicated 5, r.state 1⟩ [novel] y)
    (revised : Trace formationProcess y.receiver [.reconsider] z) :
    z.installed = some duplicated := by
  have hz := RouteFormation.trace_iff.mp revised
  have hy := trace_iff.mp course
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  subst hz
  subst hy
  rw [h1, start]
  exact peer_keeps_error_example

end Succession

end ResponseLearning

end Becoming
