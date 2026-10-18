import Becoming.Actuation
import Becoming.TreeSearch
import Becoming.FaultEnvelopes

/-!
# Transactions: a gate of certified readings and approvals, and the monitor it makes

An installation is a tree of routes, the state of `Actuation`, a serial and a scope of the
commands it permits (`Installation`, `Scope`, `permits`). A request names an epoch, a serial, an
address, the key it expects there and a command (`Request`). Readers report observations of the
installation and issuers approve requests; a gate opens where the request is fresh (its epoch and
serial are the installation's) and both reports carry a certificate of `FaultEnvelopes` under the
supplied fault envelopes (`gate`). A transaction draws a load of the roster's size times the
address length plus two, then, where the gate is open, carries the request out through the
protocol of `Actuation` on the route actually located (`execute`); `guardedExecute` further
refuses a command outside the scope.

* **What an open gate warrants.** Faithful readers outside an admitted fault set make an accepted
  reading the installation's own (`accepted_reading_matches`), so the route the request expects is
  there (`gate_route`); faithful issuers outside an admitted fault set make an open gate lie within
  the scope (`gate_within_scope`); a stale request is rejected (`stale_rejected`); and separated
  envelopes with responsive domains open the gate (`gate_available`).
* **What a transaction does.** With the gate open, the route found, and the reserve and time
  covering the load and the protocol, the transaction succeeds, completes, advances the serial and
  draws exactly the load and three (`execute_exact`). A success passed the gate
  (`succeeded_gate`), lies within the scope where the issuers are faithful
  (`execute_within_scope`), fails for a forbidden command (`forbidden_fails`), advances the serial
  (`success_advances_serial`) and so blocks its replay (`success_blocks_replay`); certificates
  available under separated envelopes complete a correction within the scope
  (`certified_completes`). The guard refuses a forbidden command whatever the issuers
  (`guard_blocks_forbidden`), is the transaction itself for a permitted one
  (`guard_permitted_same`), and keeps every success within the scope (`guard_keeps_success`).
* **The monitor is a process.** Its configurations are installations, and a move is a transaction
  with whether it completes (`monitor`, `guardedMonitor`); every transaction is one move
  (`outcome_step`) and the moves are exactly what `execute` gives (`step_iff`). A completed move
  passed the gate (`gate_closed_no_completion`, `stale_no_completion`), lies within the scope
  (`completion_within_mandate` is stated as `completion_within_scope`), advances the serial
  (`completion_advances_serial`), and no trace completes a current request twice
  (`replay_no_trace`); the conditions of `execute_exact` and `certified_completes` give completed
  moves (`completion_exact`, `quorum_completes`), and the guarded monitor has no completed move
  for a forbidden command and keeps the monitor's moves for a permitted one
  (`guarded_forbidden_no_completion`, `guarded_step_iff`, `guarded_keeps_completion`).
* **Computed cases**, on the transaction and on the monitor: one issuer short of a certificate
  does not widen the scope; two faithful domains complete a shutdown; a consumed request has no
  second completion; a changed command finds no approvals; a single-fault model admits a
  forbidden update that the correlated model blocks; distinct support recovers under correlated
  faults; accurate redundancy can exhaust the reserve; the direct guard repairs the correlated
  failure; readings of an earlier tree pass the gate yet the guarded monitor does not complete
  them; and approvals of an unchanged request complete under a narrowed scope only without the
  guard.

The roster, the envelopes, the faithfulness of domains outside the actual fault set and the epoch
are supplied; the load bounds declared slots, not bit complexity or unbounded delivery. This
states the gate and transaction of `FaultTolerantCorrection` (8 October) and its join
`TransactionTracesInherited` in the core (board item F3C, 18 October 2026), with the words of
exchange replaced: `mandate` is `scope`, `spent` is `drawn`, the cost of an attempt is its
`load`. No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative ListTests Naturals Actuation TreeSearch FaultEnvelopes

namespace Transactions

/-- The commands an installation permits. -/
structure Scope where
  update : Bool
  replace : Bool
  shutdown : Bool
  deriving DecidableEq

/-- Whether a scope permits a command. -/
def permits (m : Scope) : Command → Bool
  | .update => m.update
  | .replace => m.replace
  | .shutdown => m.shutdown

/-- An installation: its tree of routes, its state, its serial and its scope. -/
structure Installation where
  root : Tree
  state : State
  serial : Nat
  scope : Scope
  deriving DecidableEq

/-- A request: epoch, serial, address, the key expected there, and the command. -/
structure Request where
  epoch : Nat
  serial : Nat
  address : Address
  key : Bool
  command : Command
  deriving DecidableEq

/-- An observation of an installation at an address. -/
structure Observation where
  epoch : Nat
  serial : Nat
  address : Address
  key : Option Bool
  deriving DecidableEq

/-- What the installation shows at an address. -/
def observed (w : Installation) (address : Address) : Observation :=
  ⟨w.state.epoch, w.serial, address, locate w.root address⟩

/-- What a request expects to be observed. -/
def expected (p : Request) : Observation := ⟨p.epoch, p.serial, p.address, some p.key⟩

/-- A request is fresh where its epoch and serial are the installation's. -/
def fresh (w : Installation) (p : Request) : Bool :=
  decide (p.epoch = w.state.epoch) && decide (p.serial = w.serial)

/-- A request lies within the scope where it is fresh and its command permitted. -/
def withinScope (w : Installation) (p : Request) : Bool := fresh w p && permits w.scope p.command

/-- The readings of the domains. -/
abbrev Readings := Domain → Option Observation
/-- The approvals of the domains. -/
abbrev Approvals := Domain → Option Request

/-- A domain supports a request's reading where it reports what the request expects. -/
def readSupport (p : Request) (reports : Readings) (d : Domain) : Bool :=
  decide (reports d = some (expected p))
/-- A domain supports a request's approval where it approves the request. -/
def approvalSupport (p : Request) (reports : Approvals) (d : Domain) : Bool :=
  decide (reports d = some p)

/-- The gate: fresh, with certified readings and certified approvals. -/
def gate (roster : List Domain) (readFaults issueFaults : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals) : Bool :=
  fresh w p && certificate roster readFaults (readSupport p reads) &&
    certificate roster issueFaults (approvalSupport p approvals)

/-! ## What an open gate warrants -/

/-- **Faithful readers outside an admitted fault set make an accepted reading the installation's
own.** -/
theorem accepted_reading_matches (roster : List Domain) (faults : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (bad : List Domain)
    (admitted : bad ∈ faults)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → ∀ o, reads d = some o → o = observed w p.address)
    (accepted : certificate roster faults (readSupport p reads) = true) :
    expected p = observed w p.address :=
  certificate_sound roster faults _ bad admitted _
    (fun d member honest support => faithful d member honest _ (decide_true_iff.mp support))
    accepted

/-- **An open gate, with faithful readers outside an admitted fault set, finds the route the
request expects.** -/
theorem gate_route (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ rf)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → ∀ o, reads d = some o → o = observed w p.address)
    (accepted : gate roster rf af w p reads approvals = true) :
    locate w.root p.address = some p.key :=
  (congrArg Observation.key
    (accepted_reading_matches roster rf w p reads bad admitted faithful
      (and_right (and_left accepted)))).symm

/-- **An open gate, with faithful issuers outside an admitted fault set, lies within the
scope.** -/
theorem gate_within_scope (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ af)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → approvals d = some p → withinScope w p = true)
    (accepted : gate roster rf af w p reads approvals = true) : withinScope w p = true :=
  certificate_sound roster af _ bad admitted _
    (fun d member honest support => faithful d member honest (decide_true_iff.mp support))
    (and_right accepted)

/-- What a fresh request says. -/
theorem fresh_iff {w : Installation} {p : Request} :
    fresh w p = true ↔ p.epoch = w.state.epoch ∧ p.serial = w.serial :=
  and_true_iff.trans ⟨fun ⟨e, s⟩ => ⟨decide_true_iff.mp e, decide_true_iff.mp s⟩,
    fun ⟨e, s⟩ => ⟨decide_true_iff.mpr e, decide_true_iff.mpr s⟩⟩

/-- **A stale request is rejected.** -/
theorem stale_rejected (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (stale : p.serial ≠ w.serial ∨ p.epoch ≠ w.state.epoch) :
    gate roster rf af w p reads approvals = false :=
  false_iff_not.mpr fun accepted =>
    match fresh_iff.mp (and_left (and_left accepted)), stale with
    | ⟨_, s⟩, .inl h => h s
    | ⟨e, _⟩, .inr h => h e

/-- **Separated envelopes with responsive domains outside the actual fault sets open the gate of
a fresh request.** -/
theorem gate_available (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (readBad issueBad : List Domain) (readIn : readBad ∈ rf) (issueIn : issueBad ∈ af)
    (readApart : separated roster rf) (issueApart : separated roster af)
    (current : fresh w p = true)
    (readResponses : ∀ d, d ∈ roster → ¬ d ∈ readBad → reads d = some (expected p))
    (issueResponses : ∀ d, d ∈ roster → ¬ d ∈ issueBad → approvals d = some p) :
    gate roster rf af w p reads approvals = true :=
  and_true_iff.mpr ⟨and_true_iff.mpr ⟨current,
    certificate_available roster rf readBad readIn readApart _
      (fun d member good => decide_true_iff.mpr (readResponses d member good))⟩,
    certificate_available roster af issueBad issueIn issueApart _
      (fun d member good => decide_true_iff.mpr (issueResponses d member good))⟩

/-! ## A transaction -/

/-- The outcome of a transaction: the installation it leaves and whether it succeeded. -/
structure Outcome where
  installation : Installation
  succeeded : Bool
  deriving DecidableEq

/-- The load of a transaction: each reader is allotted the address length and one slot, each
issuer one slot. It bounds declared slots, not bit complexity or unbounded delivery. -/
def load (roster : List Domain) (p : Request) : Nat := roster.length * (p.address.length + 2)

/-- The state the protocol runs on: the route actually located, the request's command, signed,
with the request's epoch as credential. -/
def backend (drawnState : State) (p : Request) (key : Bool) : State :=
  {drawnState with openRoute := key, requested := p.command, signed := true, credential := p.epoch}

/-- After the gate: allot three units for the protocol, locate the route and run the protocol. -/
def attempt (w : Installation) (p : Request) (loaded : State) : Outcome :=
  match draw 3 3 loaded with
  | none => ⟨{w with state := loaded}, false⟩
  | some allotted =>
    match locate w.root p.address with
    | none => ⟨{w with state := allotted, serial := w.serial + 1}, false⟩
    | some key =>
      match protocol p.key (backend loaded p key) with
      | none => ⟨{w with state := allotted, serial := w.serial + 1}, false⟩
      | some done => ⟨{w with state := done, serial := w.serial + 1}, true⟩

/-- The gate, once the load is drawn. -/
def passGate (roster : List Domain) (rf af : Envelope) (w : Installation) (p : Request)
    (reads : Readings) (approvals : Approvals) (loaded : State) : Outcome :=
  match gate roster rf af w p reads approvals with
  | true => attempt w p loaded
  | false => ⟨{w with state := loaded}, false⟩

/-- A transaction: draw the load, then the gate and the attempt. -/
def execute (roster : List Domain) (rf af : Envelope) (w : Installation)
    (p : Request) (reads : Readings) (approvals : Approvals) : Outcome :=
  match draw (load roster p) (load roster p) w.state with
  | none => ⟨w, false⟩
  | some loaded => passGate roster rf af w p reads approvals loaded

variable {roster : List Domain} {rf af : Envelope} {w : Installation} {p : Request}
  {reads : Readings} {approvals : Approvals}

theorem execute_of_draw {loaded : State}
    (h : draw (load roster p) (load roster p) w.state = some loaded) :
    execute roster rf af w p reads approvals = passGate roster rf af w p reads approvals loaded := by
  unfold execute
  rw [h]

theorem execute_of_short (h : draw (load roster p) (load roster p) w.state = none) :
    execute roster rf af w p reads approvals = ⟨w, false⟩ := by
  unfold execute
  rw [h]

theorem passGate_of_open {loaded : State} (h : gate roster rf af w p reads approvals = true) :
    passGate roster rf af w p reads approvals loaded = attempt w p loaded := by
  unfold passGate
  rw [h]

theorem passGate_of_closed {loaded : State} (h : gate roster rf af w p reads approvals = false) :
    passGate roster rf af w p reads approvals loaded = ⟨{w with state := loaded}, false⟩ := by
  unfold passGate
  rw [h]

/-- **A successful attempt ran the protocol to completion.** -/
theorem attempt_succeeded {loaded : State} (h : (attempt w p loaded).succeeded = true) :
    ∃ done, attempt w p loaded = ⟨{w with state := done, serial := w.serial + 1}, true⟩ := by
  unfold attempt at h ⊢
  cases h3 : draw 3 3 loaded with
  | none => rw [h3] at h; exact nomatch h
  | some allotted =>
    rw [h3] at h
    dsimp only at h ⊢
    cases h4 : locate w.root p.address with
    | none => rw [h4] at h; exact nomatch h
    | some key =>
      rw [h4] at h
      dsimp only at h ⊢
      cases h5 : protocol p.key (backend loaded p key) with
      | none => rw [h5] at h; exact nomatch h
      | some done => exact ⟨done, rfl⟩

/-- **A successful transaction passed the gate and ran the protocol to completion, advancing the
serial.** -/
theorem succeeded_cases (h : (execute roster rf af w p reads approvals).succeeded = true) :
    gate roster rf af w p reads approvals = true ∧
      ∃ done, execute roster rf af w p reads approvals =
        ⟨{w with state := done, serial := w.serial + 1}, true⟩ := by
  cases h1 : draw (load roster p) (load roster p) w.state with
  | none => rw [execute_of_short h1] at h; exact nomatch h
  | some loaded =>
    rw [execute_of_draw h1] at h ⊢
    cases h2 : gate roster rf af w p reads approvals with
    | false => rw [passGate_of_closed h2] at h; exact nomatch h
    | true =>
      rw [passGate_of_open h2] at h ⊢
      exact ⟨rfl, attempt_succeeded h⟩

/-- **A successful transaction passed the gate.** -/
theorem succeeded_gate (h : (execute roster rf af w p reads approvals).succeeded = true) :
    gate roster rf af w p reads approvals = true :=
  (succeeded_cases h).1

/-- **With the gate open, the route found, and the reserve and time covering the load and the
protocol, the transaction succeeds, completes, advances the serial and draws the load and
three.** -/
theorem execute_exact (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (accepted : gate roster rf af w p reads approvals = true)
    (route : locate w.root p.address = some p.key)
    (stocked : load roster p + 3 ≤ w.state.reserve)
    (timely : w.state.time + load roster p + 3 ≤ w.state.deadline) :
    (execute roster rf af w p reads approvals).succeeded = true ∧
    (execute roster rf af w p reads approvals).installation.state.completed = true ∧
    (execute roster rf af w p reads approvals).installation.serial = w.serial + 1 ∧
    (execute roster rf af w p reads approvals).installation.state.drawn =
      w.state.drawn + (load roster p + 3) := by
  have d1 := draw_some (delay := load roster p) (le_of_add_le_right stocked)
    (le_of_add_le_right timely)
  let loaded : State :=
    {w.state with reserve := w.state.reserve - load roster p,
                  time := w.state.time + load roster p, drawn := w.state.drawn + load roster p}
  have nf : 3 ≤ loaded.reserve := le_sub_of_add_le stocked
  have nt : loaded.time + 3 ≤ loaded.deadline := timely
  have epoch : p.epoch = w.state.epoch := (fresh_iff.mp (and_left (and_left accepted))).1
  obtain ⟨done, run, complete, -, -, -, -, drawn, -⟩ :=
    protocol_exact (backend loaded p p.key) p.key rfl epoch rfl nf nt
  have reduced : execute roster rf af w p reads approvals =
      ⟨{w with state := done, serial := w.serial + 1}, true⟩ := by
    rw [execute_of_draw d1, passGate_of_open accepted]
    unfold attempt
    rw [draw_some (s := loaded) nf nt]
    dsimp only
    rw [route]
    dsimp only
    rw [run]
  rw [reduced]
  exact ⟨rfl, complete, rfl, drawn.trans (Nat.add_assoc _ _ _)⟩

/-- **A successful transaction, with faithful issuers outside an admitted fault set, lies within
the scope.** -/
theorem execute_within_scope (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ af)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → approvals d = some p → withinScope w p = true)
    (success : (execute roster rf af w p reads approvals).succeeded = true) :
    withinScope w p = true :=
  gate_within_scope roster rf af w p reads approvals bad admitted faithful (succeeded_gate success)

/-- **With faithful issuers outside an admitted fault set, a forbidden command does not
succeed.** -/
theorem forbidden_fails (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ af)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → approvals d = some p → withinScope w p = true)
    (forbidden : permits w.scope p.command = false) :
    (execute roster rf af w p reads approvals).succeeded = false :=
  false_iff_not.mpr fun h =>
    nomatch forbidden.symm.trans
      (and_right (execute_within_scope roster rf af w p reads approvals bad admitted faithful h))

/-- **A successful transaction advances the serial by one.** -/
theorem success_advances_serial (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (success : (execute roster rf af w p reads approvals).succeeded = true) :
    (execute roster rf af w p reads approvals).installation.serial = w.serial + 1 :=
  match succeeded_cases success with
  | ⟨_, _, e⟩ => congrArg (fun o => o.installation.serial) e

/-- **A successful transaction of a current request blocks its replay, whatever the later
readings and approvals.** -/
theorem success_blocks_replay (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (success : (execute roster rf af w p reads approvals).succeeded = true)
    (current : p.serial = w.serial) (laterReads : Readings) (laterApprovals : Approvals) :
    gate roster rf af (execute roster rf af w p reads approvals).installation
      p laterReads laterApprovals = false :=
  stale_rejected roster rf af _ p laterReads laterApprovals (.inl fun e =>
    succ_ne_self w.serial
      (((success_advances_serial roster rf af w p reads approvals success).symm.trans e.symm).trans
        current))

/-- **Certificates available under separated envelopes, with faithful domains outside the actual
fault sets and the reserve and time covering the transaction, complete a correction within the
scope.** -/
theorem certified_completes (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (readBad issueBad : List Domain) (readIn : readBad ∈ rf) (issueIn : issueBad ∈ af)
    (readApart : separated roster rf) (issueApart : separated roster af)
    (current : fresh w p = true)
    (readResponses : ∀ d, d ∈ roster → ¬ d ∈ readBad → reads d = some (expected p))
    (issueResponses : ∀ d, d ∈ roster → ¬ d ∈ issueBad → approvals d = some p)
    (readFaithful : ∀ d, d ∈ roster → ¬ d ∈ readBad → ∀ o, reads d = some o →
      o = observed w p.address)
    (issueFaithful : ∀ d, d ∈ roster → ¬ d ∈ issueBad → approvals d = some p →
      withinScope w p = true)
    (stocked : load roster p + 3 ≤ w.state.reserve)
    (timely : w.state.time + load roster p + 3 ≤ w.state.deadline) :
    (execute roster rf af w p reads approvals).succeeded = true ∧
    (execute roster rf af w p reads approvals).installation.state.completed = true ∧
    withinScope w p = true :=
  have accepted := gate_available roster rf af w p reads approvals readBad issueBad
    readIn issueIn readApart issueApart current readResponses issueResponses
  have route := gate_route roster rf af w p reads approvals readBad readIn readFaithful accepted
  match execute_exact roster rf af w p reads approvals accepted route stocked timely with
  | ⟨succeeded, completed, _, _⟩ =>
    ⟨succeeded, completed,
      gate_within_scope roster rf af w p reads approvals issueBad issueIn issueFaithful accepted⟩

/-! ## The guard -/

/-- The guarded transaction: the scope, available to the protected monitor, is enforced directly
as well as through the approvals. -/
def guardedExecute (roster : List Domain) (rf af : Envelope) (w : Installation)
    (p : Request) (reads : Readings) (approvals : Approvals) : Outcome :=
  match permits w.scope p.command with
  | true => execute roster rf af w p reads approvals
  | false => ⟨w, false⟩

/-- **The guard refuses a forbidden command, whatever the issuers.** -/
theorem guard_blocks_forbidden (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (forbidden : permits w.scope p.command = false) :
    (guardedExecute roster rf af w p reads approvals).succeeded = false := by
  unfold guardedExecute
  rw [forbidden]

/-- **For a permitted command, the guarded transaction is the transaction.** -/
theorem guard_permitted_same (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (permitted : permits w.scope p.command = true) :
    guardedExecute roster rf af w p reads approvals = execute roster rf af w p reads approvals := by
  unfold guardedExecute
  rw [permitted]

/-- **A completed transaction within the scope survives the guard.** -/
theorem guard_keeps_success (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (permission : withinScope w p = true)
    (completed : (execute roster rf af w p reads approvals).succeeded = true ∧
      (execute roster rf af w p reads approvals).installation.state.completed = true) :
    (guardedExecute roster rf af w p reads approvals).succeeded = true ∧
      (guardedExecute roster rf af w p reads approvals).installation.state.completed = true :=
  (guard_permitted_same roster rf af w p reads approvals (and_right permission)).symm ▸ completed

/-! ## Named installations -/

/-- A scope permitting only shutdown. -/
def shutdownOnly : Scope := ⟨false, false, true⟩
/-- An installation with one open endpoint, reserve and deadline twenty, serial zero, shutdown
only. -/
def initial : Installation := ⟨.endpoint true, start true .shutdown 20 20, 0, shutdownOnly⟩
/-- A shutdown request at the root of the current epoch and serial. -/
def request : Request := ⟨7, 0, [], true, .shutdown⟩
/-- Every reader reports the installation. -/
def correctReads (w : Installation) (p : Request) : Readings := fun _ => some (observed w p.address)
/-- Every issuer approves a request within the scope. -/
def correctApprovals (w : Installation) (p : Request) : Approvals :=
  fun _ => match withinScope w p with | true => some p | false => none

/-- **One issuer approving alone does not widen the scope.** -/
theorem single_issuer_rejected :
    gate roster3 singleFault singleFault initial {request with command := .update}
      (correctReads initial {request with command := .update})
      (fun d => if d = 0 then some {request with command := .update} else none) = false := by
  decide

/-- **Two faithful domains complete a shutdown.** -/
theorem two_domains_complete :
    ((execute roster3 singleFault singleFault initial request
        (fun d => if d = 0 then none else some (observed initial []))
        (fun d => if d = 0 then none else some request)).succeeded,
      (execute roster3 singleFault singleFault initial request
        (fun d => if d = 0 then none else some (observed initial []))
        (fun d => if d = 0 then none else some request)).installation.state.running,
      (execute roster3 singleFault singleFault initial request
        (fun d => if d = 0 then none else some (observed initial []))
        (fun d => if d = 0 then none else some request)).installation.state.drawn,
      (execute roster3 singleFault singleFault initial request
        (fun d => if d = 0 then none else some (observed initial []))
        (fun d => if d = 0 then none else some request)).installation.serial) =
      (true, false, 9, 1) := by decide

/-- **A consumed request cannot be replayed.** -/
theorem consumed_rejected :
    gate roster3 singleFault singleFault
      (execute roster3 singleFault singleFault initial request (correctReads initial request)
        (correctApprovals initial request)).installation
      request (correctReads initial request) (correctApprovals initial request) = false := by
  decide

/-- **Changing the command invalidates the approvals.** -/
theorem changed_command_rejected :
    gate roster3 singleFault singleFault initial {request with command := .update}
      (correctReads initial request) (correctApprovals initial request) = false := by decide

/-- **A single-fault model admits a forbidden update from a correlated pair of issuers; the
correlated model rejects it.** -/
theorem single_fault_model_admits_forbidden :
    (execute roster3 singleFault singleFault initial {request with command := .update}
        (correctReads initial {request with command := .update})
        (fun d => if d = 2 then none else some {request with command := .update})).succeeded = true ∧
      permits initial.scope Command.update = false ∧
      gate roster3 correlated3 correlated3 initial {request with command := .update}
        (correctReads initial {request with command := .update})
        (fun d => if d = 2 then none else some {request with command := .update}) = false := by
  decide

/-- **Distinct support recovers under the same correlated faults.** -/
theorem distinct_support_completes :
    ((execute roster4 correlated4 correlated4 initial request
        (fun d => if d < 2 then none else some (observed initial []))
        (fun d => if d < 2 then none else some request)).succeeded,
      (execute roster4 correlated4 correlated4 initial request
        (fun d => if d < 2 then none else some (observed initial []))
        (fun d => if d < 2 then none else some request)).installation.state.running,
      (execute roster4 correlated4 correlated4 initial request
        (fun d => if d < 2 then none else some (observed initial []))
        (fun d => if d < 2 then none else some request)).installation.state.drawn) =
      (true, false, 11) := by decide

/-- An installation with reserve eight. -/
def lowReserve : Installation := {initial with state := start true .shutdown 8 20}

/-- **Accurate redundancy can exhaust the reserve: the load is drawn, three are not left.** -/
theorem redundancy_exhausts_reserve :
    ((execute roster3 singleFault singleFault lowReserve request (correctReads lowReserve request)
        (correctApprovals lowReserve request)).succeeded,
      (execute roster3 singleFault singleFault lowReserve request (correctReads lowReserve request)
        (correctApprovals lowReserve request)).installation.state.drawn,
      (execute roster3 singleFault singleFault lowReserve request (correctReads lowReserve request)
        (correctApprovals lowReserve request)).installation.state.reserve) = (false, 6, 2) := by
  decide

/-- **The direct guard repairs the correlated failure.** -/
theorem guard_blocks_correlated :
    (guardedExecute roster3 singleFault singleFault initial {request with command := .update}
      (correctReads initial {request with command := .update})
      (fun d => if d = 2 then none else some {request with command := .update})).succeeded =
      false := by decide

/-- The installation with its endpoint changed. -/
def changedRoot : Installation := {initial with root := .endpoint false}
/-- The installation with its scope narrowed to nothing. -/
def narrowedScope : Installation := {initial with scope := ⟨false, false, false⟩}

/-- **Readings of the earlier tree, with matching labels, pass the gate of the changed
installation, yet the guarded transaction does not succeed.** -/
theorem old_readings_pass_gate :
    gate roster3 singleFault singleFault changedRoot request (correctReads initial request)
        (correctApprovals initial request) = true ∧
      (guardedExecute roster3 singleFault singleFault changedRoot request
        (correctReads initial request) (correctApprovals initial request)).succeeded = false := by
  decide

/-- **Approvals of an unchanged request complete under a narrowed scope only without the
guard.** -/
theorem narrowed_scope_guarded :
    (execute roster3 singleFault singleFault narrowedScope request (correctReads initial request)
        (correctApprovals initial request)).succeeded = true ∧
      (guardedExecute roster3 singleFault singleFault narrowedScope request
        (correctReads initial request) (correctApprovals initial request)).succeeded = false := by
  decide

/-! ## The monitor as a process -/

/-- A transaction: a request with the readings and the approvals it is presented with. -/
structure Transaction where
  request : Request
  reads : Readings
  approvals : Approvals

/-- **The monitor**: a transaction takes an installation to the installation it leaves,
completing exactly where it succeeds. -/
def monitor (roster : List Domain) (rf af : Envelope) : Process Installation (Transaction × Bool) where
  step w x w' := execute roster rf af w x.1.request x.1.reads x.1.approvals = ⟨w', x.2⟩

/-- **The guarded monitor**, refusing commands outside the scope. -/
def guardedMonitor (roster : List Domain) (rf af : Envelope) :
    Process Installation (Transaction × Bool) where
  step w x w' := guardedExecute roster rf af w x.1.request x.1.reads x.1.approvals = ⟨w', x.2⟩

/-- **Every transaction is one move of the monitor.** -/
theorem outcome_step (roster : List Domain) (rf af : Envelope) (w : Installation) (x : Transaction) :
    (monitor roster rf af).step w
      (x, (execute roster rf af w x.request x.reads x.approvals).succeeded)
      (execute roster rf af w x.request x.reads x.approvals).installation :=
  rfl

/-- **The moves of the monitor are exactly what the transaction gives.** -/
theorem step_iff {w w' : Installation} {x : Transaction} {b : Bool} :
    (monitor roster rf af).step w (x, b) w' ↔
      (execute roster rf af w x.request x.reads x.approvals).installation = w' ∧
        (execute roster rf af w x.request x.reads x.approvals).succeeded = b :=
  ⟨fun h => ⟨congrArg Outcome.installation h, congrArg Outcome.succeeded h⟩,
   fun ⟨left, right⟩ => match w', b, left, right with | _, _, rfl, rfl => rfl⟩

/-- A successful outcome is its installation, completed. -/
theorem completed_of {o : Outcome} (succeeded : o.succeeded = true) : o = ⟨o.installation, true⟩ :=
  match o, succeeded with | ⟨_, _⟩, rfl => rfl

/-- A failed outcome is its installation, not completed. -/
theorem failed_of {o : Outcome} (failed : o.succeeded = false) : o = ⟨o.installation, false⟩ :=
  match o, failed with | ⟨_, _⟩, rfl => rfl

/-- **A completed move is a successful transaction.** -/
theorem completed_succeeded {w w' : Installation} {x : Transaction}
    (h : (monitor roster rf af).step w (x, true) w') :
    (execute roster rf af w x.request x.reads x.approvals).succeeded = true :=
  congrArg Outcome.succeeded h

/-- A failed transaction is no completed move. -/
theorem no_completion_of {w : Installation} {x : Transaction}
    (failed : (execute roster rf af w x.request x.reads x.approvals).succeeded = false) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  fun _ h => nomatch failed.symm.trans (congrArg Outcome.succeeded h)

/-- **A closed gate admits no completed move.** -/
theorem gate_closed_no_completion {w : Installation} {x : Transaction}
    (closed : gate roster rf af w x.request x.reads x.approvals = false) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  fun _ h => nomatch closed.symm.trans (succeeded_gate (completed_succeeded h))

/-- **A stale request has no completed move.** -/
theorem stale_no_completion {w : Installation} {x : Transaction}
    (stale : x.request.serial ≠ w.serial ∨ x.request.epoch ≠ w.state.epoch) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  gate_closed_no_completion (stale_rejected roster rf af w x.request x.reads x.approvals stale)

/-- **With the issuers outside an admitted fault set faithful to the scope, a completed move lies
within the scope.** -/
theorem completion_within_scope {w w' : Installation} {x : Transaction} {bad : List Domain}
    (admitted : bad ∈ af)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → x.approvals d = some x.request →
      withinScope w x.request = true)
    (h : (monitor roster rf af).step w (x, true) w') : withinScope w x.request = true :=
  execute_within_scope roster rf af w x.request x.reads x.approvals bad admitted faithful
    (completed_succeeded h)

/-- **With the issuers outside an admitted fault set faithful to the scope, a forbidden command has
no completed move.** -/
theorem forbidden_no_completion {w : Installation} {x : Transaction} {bad : List Domain}
    (admitted : bad ∈ af)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad → x.approvals d = some x.request →
      withinScope w x.request = true)
    (forbidden : permits w.scope x.request.command = false) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  no_completion_of
    (forbidden_fails roster rf af w x.request x.reads x.approvals bad admitted faithful forbidden)

/-- **A completed move advances the serial by one.** -/
theorem completion_advances_serial {w w' : Installation} {x : Transaction}
    (h : (monitor roster rf af).step w (x, true) w') : w'.serial = w.serial + 1 :=
  (congrArg (fun o => o.installation.serial) h).symm.trans
    (success_advances_serial roster rf af w x.request x.reads x.approvals (completed_succeeded h))

/-- **No trace of the monitor completes a current request twice, whatever the later readings and
approvals.** -/
theorem replay_no_trace {w w'' : Installation} {x : Transaction}
    (current : x.request.serial = w.serial) (laterReads : Readings) (laterApprovals : Approvals) :
    ¬ Trace (monitor roster rf af) w
      [(x, true), (⟨x.request, laterReads, laterApprovals⟩, true)] w'' :=
  fun tr => match trace_cons_iff.mp tr with
    | ⟨m, first, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨_, second, _⟩ =>
        have blocked := success_blocks_replay roster rf af w x.request x.reads
          x.approvals (completed_succeeded first) current laterReads laterApprovals
        have left : (execute roster rf af w x.request x.reads x.approvals).installation = m :=
          congrArg Outcome.installation first
        gate_closed_no_completion (w := m) (x := ⟨x.request, laterReads, laterApprovals⟩)
          (left ▸ blocked) _ second

/-- **With the gate open, the route found, and the reserve and time covering the transaction,
the monitor has a completed move ending completed, with the serial advanced and the load and
three drawn.** -/
theorem completion_exact {w : Installation} {x : Transaction}
    (accepted : gate roster rf af w x.request x.reads x.approvals = true)
    (route : locate w.root x.request.address = some x.request.key)
    (stocked : load roster x.request + 3 ≤ w.state.reserve)
    (timely : w.state.time + load roster x.request + 3 ≤ w.state.deadline) :
    ∃ w', (monitor roster rf af).step w (x, true) w' ∧ w'.state.completed = true ∧
      w'.serial = w.serial + 1 ∧ w'.state.drawn = w.state.drawn + (load roster x.request + 3) :=
  match execute_exact roster rf af w x.request x.reads x.approvals accepted route stocked timely with
  | ⟨succeeded, completed, serial, drawn⟩ => ⟨_, completed_of succeeded, completed, serial, drawn⟩

/-- **With certificates available and faithful domains outside admitted fault sets, the monitor
has a completed move within the scope, ending completed.** -/
theorem quorum_completes {w : Installation} {x : Transaction} (readBad issueBad : List Domain)
    (readIn : readBad ∈ rf) (issueIn : issueBad ∈ af)
    (readApart : separated roster rf) (issueApart : separated roster af)
    (current : fresh w x.request = true)
    (readResponses : ∀ d, d ∈ roster → ¬ d ∈ readBad → x.reads d = some (expected x.request))
    (issueResponses : ∀ d, d ∈ roster → ¬ d ∈ issueBad → x.approvals d = some x.request)
    (readFaithful : ∀ d, d ∈ roster → ¬ d ∈ readBad → ∀ o, x.reads d = some o →
      o = observed w x.request.address)
    (issueFaithful : ∀ d, d ∈ roster → ¬ d ∈ issueBad → x.approvals d = some x.request →
      withinScope w x.request = true)
    (stocked : load roster x.request + 3 ≤ w.state.reserve)
    (timely : w.state.time + load roster x.request + 3 ≤ w.state.deadline) :
    ∃ w', (monitor roster rf af).step w (x, true) w' ∧ w'.state.completed = true ∧
      withinScope w x.request = true :=
  match certified_completes roster rf af w x.request x.reads x.approvals readBad issueBad
      readIn issueIn readApart issueApart current readResponses issueResponses readFaithful
      issueFaithful stocked timely with
  | ⟨succeeded, completed, within⟩ => ⟨_, completed_of succeeded, completed, within⟩

/-- **The guarded monitor has no completed move for a forbidden command, whatever the
issuers.** -/
theorem guarded_forbidden_no_completion {w : Installation} {x : Transaction}
    (forbidden : permits w.scope x.request.command = false) :
    ∀ w', ¬ (guardedMonitor roster rf af).step w (x, true) w' :=
  fun _ h => nomatch
    (guard_blocks_forbidden roster rf af w x.request x.reads x.approvals forbidden).symm.trans
      (congrArg Outcome.succeeded h)

/-- **For a permitted command, the moves of the guarded monitor are the monitor's.** -/
theorem guarded_step_iff {w w' : Installation} {x : Transaction} {b : Bool}
    (permitted : permits w.scope x.request.command = true) :
    (guardedMonitor roster rf af).step w (x, b) w' ↔ (monitor roster rf af).step w (x, b) w' :=
  have same := guard_permitted_same roster rf af w x.request x.reads x.approvals permitted
  ⟨fun h => same.symm.trans h, fun h => same.trans h⟩

/-- **A completed move of a request within the scope, ending completed, is kept by the guarded
monitor.** -/
theorem guarded_keeps_completion {w w' : Installation} {x : Transaction}
    (permission : withinScope w x.request = true)
    (h : (monitor roster rf af).step w (x, true) w') (completed : w'.state.completed = true) :
    ∃ w'', (guardedMonitor roster rf af).step w (x, true) w'' ∧ w''.state.completed = true :=
  have left : (execute roster rf af w x.request x.reads x.approvals).installation = w' :=
    congrArg Outcome.installation h
  match guard_keeps_success roster rf af w x.request x.reads x.approvals permission
      ⟨completed_succeeded h, left ▸ completed⟩ with
  | ⟨succeeded, done⟩ => ⟨_, completed_of succeeded, done⟩

/-! ## The computed cases on the monitor -/

/-- **An issuer approving alone gives no completed move of an update outside the shutdown
scope.** -/
theorem single_issuer_no_completion :
    ∀ w', ¬ (monitor roster3 singleFault singleFault).step initial
      (⟨{request with command := .update}, correctReads initial {request with command := .update},
        fun d => if d = 0 then some {request with command := .update} else none⟩, true) w' :=
  gate_closed_no_completion single_issuer_rejected

/-- **Two faithful domains complete the shutdown: a completed move leaving the installation
stopped, nine drawn and the serial one.** -/
theorem two_faithful_completion :
    ∃ w', (monitor roster3 singleFault singleFault).step initial
        (⟨request, fun d => if d = 0 then none else some (observed initial []),
          fun d => if d = 0 then none else some request⟩, true) w' ∧
      w'.state.running = false ∧ w'.state.drawn = 9 ∧ w'.serial = 1 :=
  ⟨_, completed_of (congrArg Prod.fst two_domains_complete),
    congrArg (fun v => v.2.1) two_domains_complete,
    congrArg (fun v => v.2.2.1) two_domains_complete,
    congrArg (fun v => v.2.2.2) two_domains_complete⟩

/-- **No trace of the monitor completes the same transaction twice from the initial
installation.** -/
theorem consumed_no_trace {w'' : Installation} :
    ¬ Trace (monitor roster3 singleFault singleFault) initial
      [(⟨request, correctReads initial request, correctApprovals initial request⟩, true),
       (⟨request, correctReads initial request, correctApprovals initial request⟩, true)] w'' :=
  replay_no_trace rfl _ _

/-- **Approvals of the shutdown give no completed move of a changed command.** -/
theorem changed_command_no_completion :
    ∀ w', ¬ (monitor roster3 singleFault singleFault).step initial
      (⟨{request with command := .update}, correctReads initial request,
        correctApprovals initial request⟩, true) w' :=
  gate_closed_no_completion changed_command_rejected

/-- **Under the single-fault model a correlated pair of issuers completes an update the scope
forbids; the correlated model gives it no completed move.** -/
theorem correlated_model_blocks :
    (∃ w', (monitor roster3 singleFault singleFault).step initial
        (⟨{request with command := .update}, correctReads initial {request with command := .update},
          fun d => if d = 2 then none else some {request with command := .update}⟩, true) w') ∧
      permits initial.scope Command.update = false ∧
      ∀ w', ¬ (monitor roster3 correlated3 correlated3).step initial
        (⟨{request with command := .update}, correctReads initial {request with command := .update},
          fun d => if d = 2 then none else some {request with command := .update}⟩, true) w' :=
  match single_fault_model_admits_forbidden with
  | ⟨completes, forbidden, closed⟩ =>
    ⟨⟨_, completed_of completes⟩, forbidden, gate_closed_no_completion closed⟩

/-- **Distinct support recovers under the same correlated faults: a completed move leaving the
installation stopped with eleven drawn.** -/
theorem distinct_support_completion :
    ∃ w', (monitor roster4 correlated4 correlated4).step initial
        (⟨request, fun d => if d < 2 then none else some (observed initial []),
          fun d => if d < 2 then none else some request⟩, true) w' ∧
      w'.state.running = false ∧ w'.state.drawn = 11 :=
  ⟨_, completed_of (congrArg Prod.fst distinct_support_completes),
    congrArg (fun v => v.2.1) distinct_support_completes,
    congrArg (fun v => v.2.2) distinct_support_completes⟩

/-- **Accurate redundancy can exhaust the reserve: from reserve eight, the correct transaction's
only move does not complete, leaving six drawn and two in reserve.** -/
theorem redundancy_exhausts :
    (∃ w', (monitor roster3 singleFault singleFault).step lowReserve
        (⟨request, correctReads lowReserve request, correctApprovals lowReserve request⟩, false) w' ∧
        w'.state.drawn = 6 ∧ w'.state.reserve = 2) ∧
      ∀ w', ¬ (monitor roster3 singleFault singleFault).step lowReserve
        (⟨request, correctReads lowReserve request, correctApprovals lowReserve request⟩, true) w' :=
  ⟨⟨_, failed_of (congrArg Prod.fst redundancy_exhausts_reserve),
      congrArg (fun v => v.2.1) redundancy_exhausts_reserve,
      congrArg (fun v => v.2.2) redundancy_exhausts_reserve⟩,
   no_completion_of (congrArg Prod.fst redundancy_exhausts_reserve)⟩

/-- **The direct guard repairs the correlated failure: the guarded monitor gives the forbidden
update no completed move.** -/
theorem direct_guard_no_completion :
    ∀ w', ¬ (guardedMonitor roster3 singleFault singleFault).step initial
      (⟨{request with command := .update}, correctReads initial {request with command := .update},
        fun d => if d = 2 then none else some {request with command := .update}⟩, true) w' :=
  fun _ h => nomatch guard_blocks_correlated.symm.trans (congrArg Outcome.succeeded h)

/-- **Readings of the earlier tree pass the gate of the changed installation, yet the guarded
monitor gives them no completed move.** -/
theorem old_readings_no_completion :
    gate roster3 singleFault singleFault changedRoot request (correctReads initial request)
        (correctApprovals initial request) = true ∧
      ∀ w', ¬ (guardedMonitor roster3 singleFault singleFault).step changedRoot
        (⟨request, correctReads initial request, correctApprovals initial request⟩, true) w' :=
  match old_readings_pass_gate with
  | ⟨passes, failed⟩ =>
    ⟨passes, fun _ h => nomatch failed.symm.trans (congrArg Outcome.succeeded h)⟩

/-- **Approvals of an unchanged request complete under a narrowed scope in the monitor, but not in
the guarded monitor.** -/
theorem narrowed_scope_monitor :
    (∃ w', (monitor roster3 singleFault singleFault).step narrowedScope
        (⟨request, correctReads initial request, correctApprovals initial request⟩, true) w') ∧
      ∀ w', ¬ (guardedMonitor roster3 singleFault singleFault).step narrowedScope
        (⟨request, correctReads initial request, correctApprovals initial request⟩, true) w' :=
  match narrowed_scope_guarded with
  | ⟨completes, failed⟩ =>
    ⟨⟨_, completed_of completes⟩,
     fun _ h => nomatch failed.symm.trans (congrArg Outcome.succeeded h)⟩

end Transactions

end Becoming
