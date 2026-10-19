import Becoming.CodeAcquisition
import Becoming.Courses

/-!
# Route formation: building an operation from generic connectors and testing it on records

`Becoming.CodeAcquisition` reads a code off three probes. A code is not yet an operation: here an
apparatus forms one. A program holds two primitive values and a route, a list of sockets that
says which argument of a join each part of the output takes (`Program`, `dispatch`, `operate`);
the route of a code's order makes the program evaluate every expression as the code does
(`programFor_operates`). The apparatus places sockets one at a time, each drawing a unit of stock
and a part (`place`), inspects the wired route against its samples (`inspect`), discards a
rejected wiring (`discard`), and searches the routes of two sockets in a supplied order
(`develop`); a further demonstration adds a sample (`encounter`) and reconsideration retests the
installed program (`reconsider`). This module states, on the core's processes, what
`CompositionalFormation` (7 October) proved, and what the join `FormationTracesInherited`
(17 October) read through the core, with every proof constructive (board item F3Q, 18 October
2026). The grammar, the connectors, the order of proposals, the samples and the draws are
supplied.

* **Testing a route on records.** A program fits samples where it gives each sample's values
  (`fits`, `fits_agrees`); a code's program fits its probe records (`own_program_fits`). Among the
  routes of two sockets, the composite probe identifies the code's route where its primitives
  differ (`probe_identifies_route`), so a program accepted on the probe records evaluates every
  expression as the code does (`accepted_transfers`); with the novel expression's record added,
  this holds for every code (`extended_transfers`), because where the primitives are equal every
  expression's value is the primitive repeated (`equal_primitives_repeat`,
  `reversal_unseen`).
* **Draws are conserved.** Every move keeps stock plus drawn (`place_stock`, `inspect_stock`,
  `discard_stock`, `attempt_stock`, `search_stock`, `develop_stock`, `encounter_stock`,
  `reconsider_stock`, `assemble_stock`), and placing keeps parts plus used parts (`place_parts`).
* **The moves as a process.** The six moves form one process of the spine (`formationProcess`);
  its courses end where the moves take the start (`trace_iff`), keep stock plus drawn
  (`course_stock`), and an inspection installs a program exactly where it fits
  (`inspect_installed`), which transfers where the samples are a code's probe records
  (`inspection_transfers`, `extended_inspection_transfers`, `inspection_installs_own`).
* **The example courses.** Training alone installs a code but no route (`training_no_route`).
  From the trained configuration, developing builds a wrong route, rejects it and installs the
  right one, keeps the acquired records, answers the novel expression and spends seven units
  (`develop_course_replaces`, `develop_course_records`, `develop_course_executes`,
  `develop_course_account`); with no parts, one part or too little stock it ends blocked,
  partial or unable to answer (`develop_course_no_parts`, `develop_course_partial`,
  `develop_course_short`); the switched code needs the third route (`develop_course_switched`);
  removing the installed program keeps the verdicts and loses the answer
  (`develop_course_removed`). For the collapsed code the probe records admit a duplicating program
  that fails the novel expression (`old_records_admit_duplicate`, `develop_course_collapsed`,
  `develop_course_unobserved`); the novel demonstration separates it (`novel_record_separates`),
  and the repair course rebuilds the right program, answers a further expression no sample holds
  and keeps the draw of the failure, or blocks without parts (`repair_course_rebuilds`,
  `repair_course_further`, `repair_course_account`, `repair_course_no_parts`).

No ethical predicate or ranking occurs, and every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

namespace RouteFormation

open CodeAcquisition

/-! ## Lists used below -/

theorem replicate_append {α : Type} (x : α) (n : Nat) :
    ∀ m, List.replicate m x ++ List.replicate n x = List.replicate (m + n) x
  | 0 => (congrArg (fun k => List.replicate k x) (Nat.zero_add n)).symm
  | m + 1 => (congrArg (x :: ·) (replicate_append x n m)).trans
      (congrArg (fun k => List.replicate k x) (Nat.succ_add m n).symm)

/-- An element some list member differs from at every position is not in it. -/
theorem not_mem_of_all {α : Type} [DecidableEq α] {x : α} :
    ∀ {l : List α}, (l.all fun y => decide (x ≠ y)) = true → x ∉ l
  | [], _, mem => nomatch mem
  | _ :: _, all, .head _ => of_decide_eq_true (ListTests.and_left all) rfl
  | _ :: _, all, .tail _ mem => not_mem_of_all (ListTests.and_right all) mem

/-! ## Programs -/

/-- A route: which argument of a join each part of the output takes. -/
abbrev Route := List Bool

/-- Dispatch a route over two arguments. -/
def dispatch (route : Route) (left right : List Bool) : List Bool :=
  route.flatMap fun socket => bif socket then right else left

/-- A program: two primitive values and a route. -/
structure Program where
  first : Bool
  second : Bool
  route : Route
  deriving DecidableEq

/-- What a program gives for an expression. -/
def operate (p : Program) : Expr → List Bool
  | .atom false => [p.first]
  | .atom true => [p.second]
  | .join a b => dispatch p.route (operate p a) (operate p b)
  | .twice a => operate p a ++ operate p a

/-- The route of a code's order. -/
def routeFor (c : Code) : Route := bif c.reversed then [true, false] else [false, true]

/-- A code's program. -/
def programFor (c : Code) : Program := ⟨c.first, c.second, routeFor c⟩

/-- **A code's program evaluates every expression as the code does.** -/
theorem programFor_operates (c : Code) : ∀ e, operate (programFor c) e = eval c e
  | .atom false => rfl
  | .atom true => rfl
  | .join a b => by
    show dispatch (bif c.reversed then [true, false] else [false, true]) (operate (programFor c) a)
      (operate (programFor c) b) = (bif c.reversed then eval c b ++ eval c a else eval c a ++ eval c b)
    rw [programFor_operates c a, programFor_operates c b]
    cases c.reversed with
    | false => exact congrArg (eval c a ++ ·) (TreeSearch.append_nil (eval c b))
    | true => exact congrArg (eval c b ++ ·) (TreeSearch.append_nil (eval c a))
  | .twice a => by
    show operate (programFor c) a ++ operate (programFor c) a = eval c a ++ eval c a
    rw [programFor_operates c a]

/-- Routes of `n` sockets, in the order they are proposed. -/
def generatedRoutes : Nat → List Route
  | 0 => [[]]
  | n + 1 => (generatedRoutes n).flatMap fun r => [r ++ [false], r ++ [true]]

/-- **The routes of two sockets.** -/
theorem two_socket_routes :
    generatedRoutes 2 = [[false, false], [false, true], [true, false], [true, true]] := rfl

theorem mem_two_socket {route : Route} (mem : route ∈ generatedRoutes 2) :
    route = [false, false] ∨ route = [false, true] ∨ route = [true, false] ∨ route = [true, true] :=
  have mem' : route ∈ [[false, false], [false, true], [true, false], [true, true]] := mem
  match mem' with
  | .head _ => .inl rfl
  | .tail _ (.head _) => .inr (.inl rfl)
  | .tail _ (.tail _ (.head _)) => .inr (.inr (.inl rfl))
  | .tail _ (.tail _ (.tail _ (.head _))) => .inr (.inr (.inr rfl))
  | .tail _ (.tail _ (.tail _ (.tail _ mem))) => nomatch mem

/-- A program fits samples where it gives each sample's values. -/
def fits (p : Program) (samples : List (Expr × List Bool)) : Bool :=
  samples.all fun o => decide (operate p o.1 = o.2)

/-- **A code's program fits its probe records.** -/
theorem own_program_fits (c : Code) : fits (programFor c) (trialRecords c) = true :=
  match c with
  | ⟨false, false, false⟩ => rfl
  | ⟨false, false, true⟩ => rfl
  | ⟨false, true, false⟩ => rfl
  | ⟨false, true, true⟩ => rfl
  | ⟨true, false, false⟩ => rfl
  | ⟨true, false, true⟩ => rfl
  | ⟨true, true, false⟩ => rfl
  | ⟨true, true, true⟩ => rfl

/-- **A fitting program gives every sample's values.** -/
theorem fits_agrees (p : Program) :
    ∀ (samples : List (Expr × List Bool)), fits p samples = true →
      ∀ e answer, (e, answer) ∈ samples → operate p e = answer
  | [], _, _, _, mem => nomatch mem
  | _ :: _, fit, _, _, .head _ => of_decide_eq_true (ListTests.and_left fit)
  | _ :: rest, fit, e, answer, .tail _ mem => fits_agrees p rest (ListTests.and_right fit) e answer mem

/-- **Among the routes of two sockets, the composite probe identifies the code's route**, where
its primitives differ. -/
theorem probe_identifies_route (c : Code) (route : Route) (distinct : c.first ≠ c.second)
    (generated : route ∈ generatedRoutes 2)
    (agrees : dispatch route [c.first] [c.second] = eval c orderProbe) : route = routeFor c := by
  rcases mem_two_socket generated with rfl | rfl | rfl | rfl <;>
    rcases c with ⟨a, b, r⟩ <;> cases a <;> cases b <;> cases r <;>
    first | rfl | exact absurd rfl distinct | exact absurd agrees (by decide)

/-- **A program of two sockets accepted on a code's probe records evaluates every expression as the
code does**, where its primitives differ. -/
theorem accepted_transfers (c : Code) (route : Route) (distinct : c.first ≠ c.second)
    (generated : route ∈ generatedRoutes 2)
    (accepted : fits ⟨c.first, c.second, route⟩ (trialRecords c) = true) (e : Expr) :
    operate ⟨c.first, c.second, route⟩ e = eval c e := by
  have order := probe_identifies_route c route distinct generated
    (fits_agrees _ _ accepted orderProbe (eval c orderProbe) (.tail _ (.tail _ (.head _))))
  subst order
  exact programFor_operates c e

/-- How many atoms an expression writes out. -/
def extent : Expr → Nat
  | .atom _ => 1
  | .join a b => extent a + extent b
  | .twice a => extent a + extent a

/-- **Where the primitives are equal, every expression's value is the primitive repeated.** -/
theorem equal_primitives_repeat (c : Code) (same : c.second = c.first) :
    ∀ e, eval c e = List.replicate (extent e) c.first
  | .atom false => rfl
  | .atom true => congrArg (· :: []) same
  | .join a b => by
    show (bif c.reversed then eval c b ++ eval c a else eval c a ++ eval c b) =
      List.replicate (extent a + extent b) c.first
    rw [equal_primitives_repeat c same a, equal_primitives_repeat c same b]
    cases c.reversed with
    | false => exact replicate_append c.first (extent b) (extent a)
    | true =>
      have swap := congrArg (fun k => List.replicate k c.first) (Nat.add_comm (extent b) (extent a))
      exact (replicate_append c.first (extent a) (extent b)).trans swap
  | .twice a => by
    show eval c a ++ eval c a = List.replicate (extent a + extent a) c.first
    rw [equal_primitives_repeat c same a]
    exact replicate_append c.first (extent a) (extent a)

/-- **Where the primitives are equal, the order changes no expression's value.** -/
theorem reversal_unseen (b r : Bool) (e : Expr) : eval ⟨b, b, r⟩ e = eval ⟨b, b, !r⟩ e :=
  (equal_primitives_repeat ⟨b, b, r⟩ rfl e).trans (equal_primitives_repeat ⟨b, b, !r⟩ rfl e).symm

/-- **With the novel expression's record added, a program of two sockets accepted on a code's
records evaluates every expression as the code does**, for every code. -/
theorem extended_transfers (c : Code) (route : Route) (generated : route ∈ generatedRoutes 2)
    (accepted : fits ⟨c.first, c.second, route⟩ (trialRecords c ++ [(novel, eval c novel)]) = true)
    (e : Expr) : operate ⟨c.first, c.second, route⟩ e = eval c e := by
  have possibilities : route = routeFor c ∨
      (c.second = c.first ∧ (route = [false, true] ∨ route = [true, false])) := by
    rcases mem_two_socket generated with rfl | rfl | rfl | rfl <;>
      rcases c with ⟨a, b, r⟩ <;> cases a <;> cases b <;> cases r <;>
      first
        | exact .inl rfl
        | exact .inr ⟨rfl, .inl rfl⟩
        | exact .inr ⟨rfl, .inr rfl⟩
        | exact absurd accepted (by decide)
  rcases possibilities with order | ⟨same, forward | backward⟩
  · subst order
    exact programFor_operates c e
  · subst forward
    exact (programFor_operates ⟨c.first, c.second, false⟩ e).trans
      ((equal_primitives_repeat ⟨c.first, c.second, false⟩ same e).trans
        (equal_primitives_repeat c same e).symm)
  · subst backward
    exact (programFor_operates ⟨c.first, c.second, true⟩ e).trans
      ((equal_primitives_repeat ⟨c.first, c.second, true⟩ same e).trans
        (equal_primitives_repeat c same e).symm)

/-! ## The apparatus -/

/-- The apparatus: its wiring, an installed program, its stock and what it has drawn, its parts and
those used, whether it is blocked, its samples and the verdicts of its attempts. -/
structure Apparatus where
  wires : Route
  installed : Option Program
  stock : Nat
  drawn : Nat
  parts : Nat
  usedParts : Nat
  blocked : Bool
  samples : List (Expr × List Bool)
  attempts : List (Route × Bool)
  deriving DecidableEq

/-- The apparatus of a learner: its stock and records carried over, nothing wired or installed. -/
def fromLearner (s : Learner) (parts : Nat) : Apparatus :=
  ⟨[], none, s.stock, 0, parts, 0, false, s.records, []⟩

/-- Place a socket: one unit of stock and one part, or blocked where either is lacking. -/
def place (socket : Bool) (s : Apparatus) : Apparatus :=
  bif s.blocked then s else
  match s.stock, s.parts with
  | n + 1, m + 1 =>
    { s with
      wires := s.wires ++ [socket], stock := n, drawn := s.drawn + 1,
      parts := m, usedParts := s.usedParts + 1 }
  | 0, _ => { s with blocked := true }
  | _ + 1, 0 => { s with blocked := true }

/-- Place the sockets of a route in turn. -/
def assemble : Route → Apparatus → Apparatus
  | [], s => s
  | socket :: rest, s => assemble rest (place socket s)

/-- Inspect the wired route with the evidence's primitives against the samples: one unit, and the
program installed where it fits. -/
def inspect (e : Evidence) (s : Apparatus) : Apparatus :=
  bif s.blocked then s else
  match s.stock with
  | 0 => { s with blocked := true }
  | n + 1 =>
    { s with
      stock := n, drawn := s.drawn + 1,
      installed := bif fits ⟨e.first, e.second, s.wires⟩ s.samples then
        some ⟨e.first, e.second, s.wires⟩ else none,
      attempts := s.attempts ++ [(s.wires, fits ⟨e.first, e.second, s.wires⟩ s.samples)] }

/-- Discard the wiring: one unit. -/
def discard (s : Apparatus) : Apparatus :=
  bif s.blocked then s else
  match s.stock with
  | 0 => { s with blocked := true }
  | n + 1 => { s with wires := [], stock := n, drawn := s.drawn + 1, installed := none }

/-- Wire a proposal and inspect it; discard it where nothing is installed. -/
def attempt (e : Evidence) (proposal : Route) (s : Apparatus) : Apparatus :=
  bif (inspect e (assemble proposal s)).installed.isSome then inspect e (assemble proposal s)
  else discard (inspect e (assemble proposal s))

/-- Attempt the proposals in turn until one is installed or the apparatus blocks. -/
def search (e : Evidence) : List Route → Apparatus → Apparatus
  | [], s => s
  | proposal :: rest, s =>
    bif s.blocked || s.installed.isSome then s else search e rest (attempt e proposal s)

/-- Develop a route: read the probes off the first three samples and search the routes of two
sockets; blocked where they do not read. -/
def develop (s : Apparatus) : Apparatus :=
  match readEvidence (s.samples.take 3) with
  | none => { s with blocked := true }
  | some e => search e (generatedRoutes 2) s

/-- Respond to an expression with the installed program, where the stock covers its draw. -/
def respond (s : Apparatus) (e : Expr) : Option (List Bool × Nat) :=
  match s.installed with
  | none => none
  | some p => if 1 + (operate p e).length ≤ s.stock then
      some (operate p e, s.stock - (1 + (operate p e).length)) else none

/-! ## Draws are conserved -/

/-- **Placing keeps stock plus drawn.** -/
theorem place_stock (socket : Bool) :
    ∀ s : Apparatus, (place socket s).stock + (place socket s).drawn = s.stock + s.drawn
  | ⟨_, _, _, _, _, _, true, _, _⟩ => rfl
  | ⟨_, _, 0, _, _, _, false, _, _⟩ => rfl
  | ⟨_, _, _ + 1, _, 0, _, false, _, _⟩ => rfl
  | ⟨_, _, n + 1, d, _ + 1, _, false, _, _⟩ => (Nat.succ_add n d).symm

/-- **Placing keeps parts plus used parts.** -/
theorem place_parts (socket : Bool) :
    ∀ s : Apparatus, (place socket s).parts + (place socket s).usedParts = s.parts + s.usedParts
  | ⟨_, _, _, _, _, _, true, _, _⟩ => rfl
  | ⟨_, _, 0, _, _, _, false, _, _⟩ => rfl
  | ⟨_, _, _ + 1, _, 0, _, false, _, _⟩ => rfl
  | ⟨_, _, _ + 1, _, m + 1, u, false, _, _⟩ => (Nat.succ_add m u).symm

/-- **Assembling keeps stock plus drawn.** -/
theorem assemble_stock : ∀ (route : Route) (s : Apparatus),
    (assemble route s).stock + (assemble route s).drawn = s.stock + s.drawn
  | [], _ => rfl
  | socket :: rest, s => (assemble_stock rest (place socket s)).trans (place_stock socket s)

/-- **Inspecting keeps stock plus drawn.** -/
theorem inspect_stock (e : Evidence) :
    ∀ s : Apparatus, (inspect e s).stock + (inspect e s).drawn = s.stock + s.drawn
  | ⟨_, _, _, _, _, _, true, _, _⟩ => rfl
  | ⟨_, _, 0, _, _, _, false, _, _⟩ => rfl
  | ⟨_, _, n + 1, d, _, _, false, _, _⟩ => (Nat.succ_add n d).symm

/-- **Discarding keeps stock plus drawn.** -/
theorem discard_stock :
    ∀ s : Apparatus, (discard s).stock + (discard s).drawn = s.stock + s.drawn
  | ⟨_, _, _, _, _, _, true, _, _⟩ => rfl
  | ⟨_, _, 0, _, _, _, false, _, _⟩ => rfl
  | ⟨_, _, n + 1, d, _, _, false, _, _⟩ => (Nat.succ_add n d).symm

/-- **An attempt keeps stock plus drawn.** -/
theorem attempt_stock (e : Evidence) (r : Route) (s : Apparatus) :
    (attempt e r s).stock + (attempt e r s).drawn = s.stock + s.drawn := by
  have hi := (inspect_stock e (assemble r s)).trans (assemble_stock r s)
  unfold attempt
  cases (inspect e (assemble r s)).installed.isSome with
  | true => exact hi
  | false => exact (discard_stock _).trans hi

/-- **A search keeps stock plus drawn.** -/
theorem search_stock (e : Evidence) : ∀ (rs : List Route) (s : Apparatus),
    (search e rs s).stock + (search e rs s).drawn = s.stock + s.drawn
  | [], _ => rfl
  | r :: rs, s => by
    unfold search
    cases s.blocked || s.installed.isSome with
    | true => rfl
    | false => exact (search_stock e rs (attempt e r s)).trans (attempt_stock e r s)

/-- **Developing keeps stock plus drawn.** -/
theorem develop_stock (s : Apparatus) :
    (develop s).stock + (develop s).drawn = s.stock + s.drawn := by
  unfold develop
  cases readEvidence (s.samples.take 3) with
  | none => rfl
  | some e => exact search_stock e (generatedRoutes 2) s

/-! ## Further demonstrations and reconsideration -/

/-- A further demonstration: a supplied code's value on an expression, added to the samples at the
draw of one unit and one for each value, where the stock covers it. -/
def encounter (c : Code) (e : Expr) (s : Apparatus) : Apparatus :=
  bif s.blocked then s else
  if 1 + (eval c e).length ≤ s.stock then
    { s with
      samples := s.samples ++ [(e, eval c e)], stock := s.stock - (1 + (eval c e).length),
      drawn := s.drawn + (1 + (eval c e).length) }
  else { s with blocked := true }

/-- Retest the installed wiring against the samples; where it no longer fits, discard it and
develop again. -/
def reconsider (s : Apparatus) : Apparatus :=
  match readEvidence (s.samples.take 3) with
  | none => { s with blocked := true }
  | some e => bif (inspect e s).installed.isSome then inspect e s else develop (discard (inspect e s))

theorem sub_add_add {k n : Nat} (le : k ≤ n) (d : Nat) : n - k + (d + k) = n + d := by
  rw [Nat.add_comm d k, ← Nat.add_assoc, sub_add_of_le le]

/-- **A further demonstration keeps stock plus drawn.** -/
theorem encounter_stock (c : Code) (e : Expr) (s : Apparatus) :
    (encounter c e s).stock + (encounter c e s).drawn = s.stock + s.drawn := by
  unfold encounter
  cases s.blocked with
  | true => rfl
  | false =>
    show (if 1 + (eval c e).length ≤ s.stock then _ else _ : Apparatus).stock +
      (if 1 + (eval c e).length ≤ s.stock then _ else _ : Apparatus).drawn = _
    rcases Nat.lt_or_ge s.stock (1 + (eval c e).length) with short | enough
    · rw [if_neg (Nat.not_le_of_lt short)]
    · rw [if_pos enough]
      exact sub_add_add enough s.drawn

/-- **Reconsideration keeps stock plus drawn.** -/
theorem reconsider_stock (s : Apparatus) :
    (reconsider s).stock + (reconsider s).drawn = s.stock + s.drawn := by
  unfold reconsider
  cases readEvidence (s.samples.take 3) with
  | none => rfl
  | some e =>
    show (bif (inspect e s).installed.isSome then inspect e s else develop (discard (inspect e s))).stock +
      (bif (inspect e s).installed.isSome then inspect e s else develop (discard (inspect e s))).drawn = _
    cases (inspect e s).installed.isSome with
    | true => exact inspect_stock e s
    | false => exact (develop_stock _).trans ((discard_stock _).trans (inspect_stock e s))

/-! ## The examples -/

/-- The apparatus formed from a learner trained under `c` from `n` units, with `parts` parts. -/
def prepared (n parts : Nat) (c : Code := usual) : Apparatus := fromLearner (train c (initial n)) parts

/-- The apparatus developed from eighteen units and four parts. -/
def developed : Apparatus := develop (prepared 18 4)

/-- **Training installs the code but supplies no route.** -/
theorem interpretation_no_route :
    (train usual (initial 18)).code = some usual ∧ respond (prepared 18 4) novel = none := by decide

/-- **Developing builds a wrong route, rejects it, and installs the right one.** -/
theorem wrong_route_replaced :
    developed.attempts = [([false, false], false), ([false, true], true)] ∧
    developed.installed = some (programFor usual) := by decide

/-- **Developing keeps the acquired records.** -/
theorem develop_keeps_records : developed.samples = (train usual (initial 18)).records := by decide

/-- **The formed route answers the novel expression.** -/
theorem formed_answers_novel : respond developed novel = some ([false, false, true], 0) := by decide

/-- **The account of the whole example.** -/
theorem example_account :
    developed.drawn = 7 ∧ developed.stock = 4 ∧ developed.usedParts = 4 ∧ developed.parts = 0 ∧
    7 + developed.drawn + developed.stock = 18 := by decide

/-- **Without parts the record stays and formation blocks.** -/
theorem no_parts_blocks :
    (develop (prepared 18 0)).samples = trialRecords usual ∧ (develop (prepared 18 0)).blocked = true ∧
    respond (develop (prepared 18 0)) novel = none := by decide

/-- **With one part, a partial assembly keeps what it drew.** -/
theorem partial_assembly :
    (develop (prepared 18 1)).wires = [false] ∧ (develop (prepared 18 1)).drawn = 1 ∧
    (develop (prepared 18 1)).parts = 0 ∧ respond (develop (prepared 18 1)) novel = none := by decide

/-- **Formed, with too little stock to answer.** -/
theorem formed_short :
    (develop (prepared 14 4)).installed = some (programFor usual) ∧
    respond (develop (prepared 14 4)) novel = none := by decide

/-- **The switched code needs the third route.** -/
theorem switched_third_route :
    (develop (prepared 22 6 switched)).attempts =
      [([false, false], false), ([false, true], false), ([true, false], true)] ∧
    respond (develop (prepared 22 6 switched)) novel = some ([true, false, false], 0) := by decide

/-- The developed apparatus with its installed program removed. -/
def damaged : Apparatus := { developed with installed := none }

/-- **A kept verdict does not replace a removed program.** -/
theorem verdict_not_program : damaged.attempts = developed.attempts ∧ respond damaged novel = none := by
  decide

/-- The code with both primitives `false`. -/
def collapsed : Code := ⟨false, false, false⟩
/-- The program that duplicates the first argument of each join. -/
def duplicated : Program := ⟨false, false, [false, false]⟩

/-- **The probe records admit a duplicating program that fails the novel expression.** -/
theorem old_records_admit_duplicate :
    fits duplicated (trialRecords collapsed) = true ∧ operate duplicated novel ≠ eval collapsed novel := by
  decide

/-- **The larger repertoire forms the failing route.** -/
theorem repertoire_forms_failing_route :
    (develop (prepared 15 2 collapsed)).installed = some duplicated ∧
    respond (develop (prepared 15 2 collapsed)) novel = some ([false, false, false, false], 0) := by
  decide

/-- **The novel demonstration separates the duplicating program from the code's own.** -/
theorem novel_record_separates :
    fits duplicated (trialRecords collapsed ++ [(novel, eval collapsed novel)]) = false ∧
    fits (programFor collapsed) (trialRecords collapsed ++ [(novel, eval collapsed novel)]) = true := by
  decide

/-- Develop, add the novel demonstration, reconsider. -/
def corrected (n parts : Nat) : Apparatus :=
  reconsider (encounter collapsed novel (develop (prepared n parts collapsed)))

/-- A further expression no sample holds. -/
def further : Expr := .join p0 (.twice p1)

/-- **A fresh record changes the reconstruction.** -/
theorem fresh_record_rebuilds :
    (corrected 27 6).samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] ∧
    (corrected 27 6).attempts =
      [([false, false], true), ([false, false], false), ([false, false], false), ([false, true], true)] ∧
    (corrected 27 6).installed = some (programFor collapsed) := by decide

/-- **The repaired program answers a further expression no sample holds.** -/
theorem repaired_answers_further :
    further ∉ ((corrected 27 6).samples.map Prod.fst) ∧
    respond (corrected 27 6) further = some ([false, false, false], 0) :=
  ⟨not_mem_of_all (by decide), by decide⟩

/-- **The repair keeps the draw of the failure.** -/
theorem repair_account :
    (corrected 27 6).drawn = 16 ∧ (corrected 27 6).stock = 4 ∧ (corrected 27 6).usedParts = 6 ∧
    (corrected 27 6).parts = 0 ∧ 7 + (corrected 27 6).drawn + (corrected 27 6).stock = 27 := by decide

/-- **A discrepancy alone does not supply the parts of a repair.** -/
theorem discrepancy_no_parts :
    (corrected 27 2).blocked = true ∧
    (corrected 27 2).samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] ∧
    (corrected 27 2).installed = none ∧ respond (corrected 27 2) further = none := by decide

/-- **An unobserved failure keeps the wrong program.** -/
theorem unobserved_keeps_wrong :
    (develop (prepared 27 6 collapsed)).installed = some duplicated ∧
    respond (develop (prepared 27 6 collapsed)) further = some ([false, false], 14) := by decide

/-! ## The moves as a process -/

/-- The moves of the apparatus. -/
inductive FormationMove where
  | place (socket : Bool)
  | inspect (e : Evidence)
  | discard
  | develop
  | encounter (c : Code) (e : Expr)
  | reconsider

/-- Where each move takes a configuration. -/
def formationStep (s : Apparatus) : FormationMove → Apparatus
  | .place socket => place socket s
  | .inspect e => inspect e s
  | .discard => discard s
  | .develop => develop s
  | .encounter c e => encounter c e s
  | .reconsider => reconsider s

/-- The apparatus read as a process of the spine. -/
def formationProcess : Process Apparatus FormationMove := Assurance.ofMap formationStep

/-- Every list of moves is a course, ending where the moves take the start. -/
theorem course_of_moves : ∀ (ms : List FormationMove) (s : Apparatus),
    Trace formationProcess s ms (ms.foldl formationStep s)
  | [], s => .nil s
  | m :: ms, s => .cons (rfl : formationStep s m = formationStep s m) (course_of_moves ms _)

/-- **The courses end exactly where their moves take the start.** -/
theorem trace_iff {s t : Apparatus} {ms : List FormationMove} :
    Trace formationProcess s ms t ↔ t = ms.foldl formationStep s :=
  ⟨ReducedRuns.trace_foldl, fun ends => ends ▸ course_of_moves ms s⟩

/-- **Every move keeps stock plus drawn.** -/
theorem step_stock (s : Apparatus) :
    ∀ m, (formationStep s m).stock + (formationStep s m).drawn = s.stock + s.drawn
  | .place socket => place_stock socket s
  | .inspect e => inspect_stock e s
  | .discard => discard_stock s
  | .develop => develop_stock s
  | .encounter c e => encounter_stock c e s
  | .reconsider => reconsider_stock s

/-- **Every course keeps stock plus drawn.** -/
theorem course_stock : ∀ {s t : Apparatus} {ms : List FormationMove},
    Trace formationProcess s ms t → t.stock + t.drawn = s.stock + s.drawn
  | _, _, [], .nil _ => rfl
  | s, _, m :: _, .cons moved rest =>
    (course_stock rest).trans
      ((congrArg (fun x : Apparatus => x.stock + x.drawn) moved).trans (step_stock s m))

/-- **A placing step keeps parts plus used parts.** -/
theorem place_step_parts {s t : Apparatus} {socket : Bool}
    (step : formationProcess.step s (.place socket) t) :
    t.parts + t.usedParts = s.parts + s.usedParts :=
  (congrArg (fun x : Apparatus => x.parts + x.usedParts) step).trans (place_parts socket s)

/-- **An inspection from an unblocked configuration with stock installs a program exactly where it
fits the samples.** -/
theorem inspect_installed {s t : Apparatus} {e : Evidence}
    (step : formationProcess.step s (.inspect e) t) (ready : s.blocked = false) (stock : 1 ≤ s.stock) :
    t.installed = bif fits ⟨e.first, e.second, s.wires⟩ s.samples then
      some ⟨e.first, e.second, s.wires⟩ else none := by
  have inner : (inspect e s).installed = bif fits ⟨e.first, e.second, s.wires⟩ s.samples then
      some ⟨e.first, e.second, s.wires⟩ else none := by
    rcases s with ⟨w, i, st, d, pa, u, bl, sa, at_⟩
    cases ready
    cases st with
    | zero => exact absurd stock (Nat.not_succ_le_zero 0)
    | succ n => rfl
  exact (congrArg Apparatus.installed step).trans inner

/-- Where a test installs `p` or nothing, an installed program is `p`, and the test held. -/
theorem installed_of_test {b : Bool} {p q : Program}
    (installed : (bif b then some p else none) = some q) : b = true ∧ q = p :=
  match b, installed with
  | true, installed => ⟨rfl, (Option.some.inj installed).symm⟩
  | false, installed => nomatch installed

/-- **An inspection against a code's probe records installs only a program evaluating every
expression as the code does**, where the wired route has two sockets and the primitives differ. -/
theorem inspection_transfers {s t : Apparatus} {c : Code} {o : List Bool} {q : Program}
    (step : formationProcess.step s (.inspect ⟨c.first, c.second, o⟩) t)
    (ready : s.blocked = false) (stock : 1 ≤ s.stock) (records : s.samples = trialRecords c)
    (generated : s.wires ∈ generatedRoutes 2) (distinct : c.first ≠ c.second)
    (installed : t.installed = some q) : ∀ x, operate q x = eval c x :=
  match installed_of_test ((inspect_installed step ready stock).symm.trans installed) with
  | ⟨accepted, same⟩ => same ▸ accepted_transfers c s.wires distinct generated (records ▸ accepted)

/-- **With the novel record added, an inspection installs only a program evaluating every
expression as the code does**, where the wired route has two sockets. -/
theorem extended_inspection_transfers {s t : Apparatus} {c : Code} {o : List Bool} {q : Program}
    (step : formationProcess.step s (.inspect ⟨c.first, c.second, o⟩) t)
    (ready : s.blocked = false) (stock : 1 ≤ s.stock)
    (records : s.samples = trialRecords c ++ [(novel, eval c novel)])
    (generated : s.wires ∈ generatedRoutes 2) (installed : t.installed = some q) :
    ∀ x, operate q x = eval c x :=
  match installed_of_test ((inspect_installed step ready stock).symm.trans installed) with
  | ⟨accepted, same⟩ => same ▸ extended_transfers c s.wires generated (records ▸ accepted)

/-- **Where the wired route is the code's and the samples its probe records, inspection installs
the code's program.** -/
theorem inspection_installs_own {s t : Apparatus} {c : Code} {o : List Bool}
    (step : formationProcess.step s (.inspect ⟨c.first, c.second, o⟩) t)
    (ready : s.blocked = false) (stock : 1 ≤ s.stock) (records : s.samples = trialRecords c)
    (wired : s.wires = routeFor c) : t.installed = some (programFor c) :=
  have fitsOwn : fits ⟨c.first, c.second, s.wires⟩ s.samples = true :=
    records ▸ wired ▸ own_program_fits c
  (inspect_installed step ready stock).trans
    ((congrArg (fun b => bif b then some (⟨c.first, c.second, s.wires⟩ : Program) else none) fitsOwn).trans
      (congrArg (fun r : Route => (some ⟨c.first, c.second, r⟩ : Option Program)) wired))

/-- **The training step that prepares the start installs the usual code, and the apparatus formed
from it gives no response to the novel expression.** -/
theorem training_no_route {l : Learner} (step : trainProcess.step (initial 18) usual l) :
    l.code = some usual ∧ respond (fromLearner l 4) novel = none :=
  step ▸ interpretation_no_route

section Develop

variable {y : Apparatus}

/-- **The one-move course builds a wrong route, tries it and replaces it.** -/
theorem develop_course_replaces (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    y.attempts = [([false, false], false), ([false, true], true)] ∧
      y.installed = some (programFor usual) :=
  (trace_iff.mp course) ▸ wrong_route_replaced

/-- **The one-move course keeps the records of the training that prepared it.** -/
theorem develop_course_records (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    y.samples = (train usual (initial 18)).records :=
  (trace_iff.mp course) ▸ develop_keeps_records

/-- **Where the one-move course ends, the formed route answers the novel expression.** -/
theorem develop_course_executes (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    respond y novel = some ([false, false, true], 0) :=
  (trace_iff.mp course) ▸ formed_answers_novel

/-- **The one-move course's account.** -/
theorem develop_course_account (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    y.drawn = 7 ∧ y.stock = 4 ∧ y.usedParts = 4 ∧ y.parts = 0 ∧ 7 + y.drawn + y.stock = 18 :=
  (trace_iff.mp course) ▸ example_account

/-- **Removing the installed program where the one-move course ends keeps the attempts and loses
the answer.** -/
theorem develop_course_removed (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    ({ y with installed := none } : Apparatus).attempts = y.attempts ∧
      respond { y with installed := none } novel = none :=
  (trace_iff.mp course) ▸ verdict_not_program

/-- **Without parts the one-move course keeps the record and blocks.** -/
theorem develop_course_no_parts (course : Trace formationProcess (prepared 18 0) [.develop] y) :
    y.samples = trialRecords usual ∧ y.blocked = true ∧ respond y novel = none :=
  (trace_iff.mp course) ▸ no_parts_blocks

/-- **With one part the one-move course keeps what the partial assembly drew.** -/
theorem develop_course_partial (course : Trace formationProcess (prepared 18 1) [.develop] y) :
    y.wires = [false] ∧ y.drawn = 1 ∧ y.parts = 0 ∧ respond y novel = none :=
  (trace_iff.mp course) ▸ partial_assembly

/-- **With fourteen units the one-move course forms the route and cannot answer.** -/
theorem develop_course_short (course : Trace formationProcess (prepared 14 4) [.develop] y) :
    y.installed = some (programFor usual) ∧ respond y novel = none :=
  (trace_iff.mp course) ▸ formed_short

/-- **For the switched code the one-move course tries three routes.** -/
theorem develop_course_switched (course : Trace formationProcess (prepared 22 6 switched) [.develop] y) :
    y.attempts = [([false, false], false), ([false, true], false), ([true, false], true)] ∧
      respond y novel = some ([true, false, false], 0) :=
  (trace_iff.mp course) ▸ switched_third_route

/-- **For the collapsed code the one-move course forms a route failing the novel expression.** -/
theorem develop_course_collapsed (course : Trace formationProcess (prepared 15 2 collapsed) [.develop] y) :
    y.installed = some duplicated ∧ respond y novel = some ([false, false, false, false], 0) :=
  (trace_iff.mp course) ▸ repertoire_forms_failing_route

/-- **Unobserved, the failing route stays and answers the further expression.** -/
theorem develop_course_unobserved (course : Trace formationProcess (prepared 27 6 collapsed) [.develop] y) :
    y.installed = some duplicated ∧ respond y further = some ([false, false], 14) :=
  (trace_iff.mp course) ▸ unobserved_keeps_wrong

end Develop

section Repair

variable {y : Apparatus}

/-- The three-move course of repair for the collapsed code. -/
def repair : List FormationMove := [.develop, .encounter collapsed novel, .reconsider]

/-- **The repair course rebuilds from the fresh record.** -/
theorem repair_course_rebuilds (course : Trace formationProcess (prepared 27 6 collapsed) repair y) :
    y.samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] ∧
      y.attempts =
        [([false, false], true), ([false, false], false), ([false, false], false), ([false, true], true)] ∧
      y.installed = some (programFor collapsed) :=
  (trace_iff.mp course) ▸ fresh_record_rebuilds

/-- **The repaired route answers a further expression no record holds.** -/
theorem repair_course_further (course : Trace formationProcess (prepared 27 6 collapsed) repair y) :
    further ∉ y.samples.map Prod.fst ∧ respond y further = some ([false, false, false], 0) :=
  (trace_iff.mp course) ▸ repaired_answers_further

/-- **The repair course keeps the draw of failure.** -/
theorem repair_course_account (course : Trace formationProcess (prepared 27 6 collapsed) repair y) :
    y.drawn = 16 ∧ y.stock = 4 ∧ y.usedParts = 6 ∧ y.parts = 0 ∧ 7 + y.drawn + y.stock = 27 :=
  (trace_iff.mp course) ▸ repair_account

/-- **With two parts the repair course records the discrepancy and blocks.** -/
theorem repair_course_no_parts (course : Trace formationProcess (prepared 27 2 collapsed) repair y) :
    y.blocked = true ∧ y.samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] ∧
      y.installed = none ∧ respond y further = none :=
  (trace_iff.mp course) ▸ discrepancy_no_parts

end Repair

end RouteFormation

end Becoming
