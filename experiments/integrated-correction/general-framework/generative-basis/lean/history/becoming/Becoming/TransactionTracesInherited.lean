import Becoming.Frame
import FaultTolerantCorrection

/-!
# The transaction monitor of `FaultTolerantCorrection` as a process

`FaultTolerantCorrection` runs one transaction on an installation (`execute`): readers report the
installation's snapshot, issuers approve a request, a gate accepts where the request is current and
both reports carry a certificate under the supplied fault envelopes, and the accepted request is
carried out through the protocol of `EffectiveCommand`, every attempt spending reserve and time.
`guardedExecute` additionally refuses a request outside the installation's mandate.

The reading used here: for a roster and envelopes, the monitor is a process of the spine
(`monitor`, `guardedMonitor`). Its configurations are installations, a move is a transaction (a
request with its readings and approvals) together with whether it completes, and a move takes `w`
to the installation the transaction leaves, completing exactly where the transaction succeeds. The
reading is exact: every transaction is one move (`outcome_step`), and the moves from `w` are
exactly what `execute` gives (`step_iff`).

* **What a completed move needs.** A completed move is a successful transaction
  (`completed_succeeded`), so a closed gate admits none (`gate_closed_no_completion`), nor does a
  stale request (`stale_no_completion`). With the issuers outside some admitted fault set faithful
  to the mandate, a completed move lies within the mandate (`completion_within_mandate`) and a
  request the mandate forbids has none (`forbidden_no_completion`). A completed move advances the
  serial by one (`completion_advances_serial`), so no trace completes a current request twice,
  whatever the later readings and approvals (`replay_no_trace`).
* **Completion where the conditions hold.** With the gate open, the route found, and the reserve
  and time covering the attempt, the monitor has a completed move ending completed, with the serial
  advanced and the cost spent (`completion_exact`); with certificates available and faithful
  domains outside admitted fault sets, it has a completed move within the mandate
  (`quorum_completes`).
* **The guarded monitor.** It has no completed move for a request the mandate forbids, whatever
  the issuers (`guarded_forbidden_no_completion`); for a permitted request its moves are the
  monitor's (`guarded_step_iff`), and a completed move within the mandate is kept
  (`guarded_keeps_completion`).
* **The module's computed cases as facts of the monitor's moves and traces.** One faithful issuer
  short of a certificate does not widen the mandate (`compromised_issuer_no_completion`); two
  faithful domains complete the shutdown (`two_faithful_completion`); a consumed transaction has no
  second completion (`consumed_no_trace`); a changed command finds no approvals
  (`changed_command_no_completion`); a single-fault model can complete a forbidden request that the
  correlated model blocks (`correlated_model_blocks`); distinct support recovers under the same
  correlated faults (`distinct_support_completion`); accurate redundancy can exhaust the reserve
  (`redundancy_exhausts`); the direct guard repairs the correlated failure
  (`direct_guard_no_completion`); readings with matching labels of an earlier snapshot pass the gate
  yet give no completed move of the guarded monitor (`old_readings_no_completion`); and approvals
  for an unchanged request complete under a narrowed mandate in the monitor but not in the guarded
  monitor (`narrowed_mandate_guarded`).

The certificate laws over rosters and fault envelopes, and the separation facts of the named
rosters, have no reading on a process and are not stated here. No ethical predicate or ranking
occurs. Inherited axioms: the periphery definitions `execute` and `guardedExecute` themselves
carry `propext`, so every declaration naming the monitor reports `propext` (the computed cases
add nothing further); `Quot.sound` comes from `stale_request_rejected`,
`execution_respects_mandate`, `forbidden_command_cannot_execute` and
`protected_completion_blocks_replay`, and `Classical.choice` with `Quot.sound` from
`execution_exact` and `quorum_to_actual_correction`.
-/

namespace Becoming

open Generative

namespace TransactionTracesInherited

open FaultTolerantCorrection

/-- A transaction: a request with the readings and the approvals it is presented with. -/
structure Transaction where
  request : Request
  reads : Readings
  approvals : Approvals

/-- **The monitor as a process**: a transaction takes an installation to the installation it
leaves, completing exactly where it succeeds. -/
def monitor (roster : List Domain) (rf af : Envelope) : Process Installation (Transaction × Bool) :=
  ⟨fun w x w' => execute roster rf af w x.1.request x.1.reads x.1.approvals = ⟨w', x.2⟩⟩

/-- **The guarded monitor as a process**, refusing requests outside the mandate. -/
def guardedMonitor (roster : List Domain) (rf af : Envelope) :
    Process Installation (Transaction × Bool) :=
  ⟨fun w x w' => guardedExecute roster rf af w x.1.request x.1.reads x.1.approvals = ⟨w', x.2⟩⟩

variable {roster : List Domain} {rf af : Envelope}

/-! ## The reading is exact -/

/-- **Every transaction is one move of the monitor.** -/
theorem outcome_step (roster : List Domain) (rf af : Envelope) (w : Installation) (x : Transaction) :
    (monitor roster rf af).step w (x, (execute roster rf af w x.request x.reads x.approvals).succeeded)
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

/-! ## What a completed move needs -/

/-- **A completed move is a successful transaction.** -/
theorem completed_succeeded {w w' : Installation} {x : Transaction}
    (h : (monitor roster rf af).step w (x, true) w') :
    (execute roster rf af w x.request x.reads x.approvals).succeeded = true :=
  congrArg Outcome.succeeded h

/-- A failed transaction is no completed move. -/
theorem no_completion_of {w : Installation} {x : Transaction}
    (failed : (execute roster rf af w x.request x.reads x.approvals).succeeded = false) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  fun _ h => Bool.noConfusion (failed.symm.trans (congrArg Outcome.succeeded h))

/-- A successful transaction passed the gate. -/
theorem succeeded_gate {w : Installation} {p : Request} {reads : Readings} {approvals : Approvals}
    (h : (execute roster rf af w p reads approvals).succeeded = true) :
    gate roster rf af w p reads approvals = true := by
  cases hg : gate roster rf af w p reads approvals with
  | true => rfl
  | false =>
    unfold execute at h
    cases hs : EffectiveCommand.spend (roster.length * (p.address.length + 2))
        (roster.length * (p.address.length + 2)) w.state with
    | none => rw [hs] at h; exact h
    | some _ => rw [hs, hg] at h; exact h

/-- **A closed gate admits no completed move.** -/
theorem gate_closed_no_completion {w : Installation} {x : Transaction}
    (closed : gate roster rf af w x.request x.reads x.approvals = false) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  fun _ h => Bool.noConfusion (closed.symm.trans (succeeded_gate (completed_succeeded h)))

/-- **A stale request has no completed move.** -/
theorem stale_no_completion {w : Installation} {x : Transaction}
    (stale : x.request.serial ≠ w.serial ∨ x.request.epoch ≠ w.state.authority) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  gate_closed_no_completion (stale_request_rejected roster rf af w x.request x.reads x.approvals stale)

/-- **With the issuers outside an admitted fault set faithful to the mandate, a completed move lies
within the mandate.** -/
theorem completion_within_mandate {w w' : Installation} {x : Transaction} {bad : List Domain}
    (admitted : bad ∈ af)
    (faithful : ∀ d ∈ roster, d ∉ bad → x.approvals d = some x.request → withinMandate w x.request = true)
    (h : (monitor roster rf af).step w (x, true) w') : withinMandate w x.request = true :=
  execution_respects_mandate roster rf af w x.request x.reads x.approvals bad admitted faithful
    (completed_succeeded h)

/-- **With the issuers outside an admitted fault set faithful to the mandate, a request the mandate
forbids has no completed move.** -/
theorem forbidden_no_completion {w : Installation} {x : Transaction} {bad : List Domain}
    (admitted : bad ∈ af)
    (faithful : ∀ d ∈ roster, d ∉ bad → x.approvals d = some x.request → withinMandate w x.request = true)
    (forbidden : permits w.mandate x.request.command = false) :
    ∀ w', ¬ (monitor roster rf af).step w (x, true) w' :=
  no_completion_of
    (forbidden_command_cannot_execute roster rf af w x.request x.reads x.approvals bad admitted
      faithful forbidden)

/-- **A completed move advances the serial by one.** -/
theorem completion_advances_serial {w w' : Installation} {x : Transaction}
    (h : (monitor roster rf af).step w (x, true) w') : w'.serial = w.serial + 1 :=
  (congrArg (fun o => o.installation.serial) h).symm.trans
    (completed_serial_advances roster rf af w x.request x.reads x.approvals (completed_succeeded h))

/-- **No trace of the monitor completes a current request twice, whatever the later readings and
approvals.** -/
theorem replay_no_trace {w w'' : Installation} {x : Transaction} (current : x.request.serial = w.serial)
    (laterReads : Readings) (laterApprovals : Approvals) :
    ¬ Trace (monitor roster rf af) w [(x, true), (⟨x.request, laterReads, laterApprovals⟩, true)] w'' :=
  fun tr => match trace_cons_iff.mp tr with
    | ⟨m, first, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨_, second, _⟩ =>
        have blocked := protected_completion_blocks_replay roster rf af w x.request x.reads
          x.approvals (completed_succeeded first) current laterReads laterApprovals
        have left : (execute roster rf af w x.request x.reads x.approvals).installation = m :=
          congrArg Outcome.installation first
        gate_closed_no_completion (w := m) (x := ⟨x.request, laterReads, laterApprovals⟩)
          (left ▸ blocked) _ second

/-! ## Completion where the conditions hold -/

/-- **With the gate open, the route found, and the reserve and time covering the attempt, the
monitor has a completed move ending completed, with the serial advanced and the cost spent.** -/
theorem completion_exact {w : Installation} {x : Transaction}
    (accepted : gate roster rf af w x.request x.reads x.approvals = true)
    (route : AcquiredCorrection.locate w.root x.request.address = some x.request.key)
    (funded : roster.length * (x.request.address.length + 2) + 3 ≤ w.state.reserve)
    (timely : w.state.time + (roster.length * (x.request.address.length + 2)) + 3 ≤ w.state.deadline) :
    ∃ w', (monitor roster rf af).step w (x, true) w' ∧ w'.state.completed = true ∧
      w'.serial = w.serial + 1 ∧
      w'.state.spent = w.state.spent + (roster.length * (x.request.address.length + 2) + 3) :=
  match execution_exact roster rf af w x.request x.reads x.approvals accepted route funded timely with
  | ⟨succeeded, completed, serial, spent⟩ => ⟨_, completed_of succeeded, completed, serial, spent⟩

/-- **With certificates available and faithful domains outside admitted fault sets, the monitor has
a completed move within the mandate, ending completed.** -/
theorem quorum_completes {w : Installation} {x : Transaction} (readBad issueBad : List Domain)
    (readIn : readBad ∈ rf) (issueIn : issueBad ∈ af)
    (readApart : separated roster rf) (issueApart : separated roster af)
    (current : fresh w x.request = true)
    (readResponses : ∀ d ∈ roster, d ∉ readBad → x.reads d = some (expected x.request))
    (issueResponses : ∀ d ∈ roster, d ∉ issueBad → x.approvals d = some x.request)
    (readFaithful : ∀ d ∈ roster, d ∉ readBad → ∀ o, x.reads d = some o → o = observed w x.request.address)
    (issueFaithful : ∀ d ∈ roster, d ∉ issueBad → x.approvals d = some x.request →
      withinMandate w x.request = true)
    (funded : roster.length * (x.request.address.length + 2) + 3 ≤ w.state.reserve)
    (timely : w.state.time + (roster.length * (x.request.address.length + 2)) + 3 ≤ w.state.deadline) :
    ∃ w', (monitor roster rf af).step w (x, true) w' ∧ w'.state.completed = true ∧
      withinMandate w x.request = true :=
  match quorum_to_actual_correction roster rf af w x.request x.reads x.approvals readBad issueBad
      readIn issueIn readApart issueApart current readResponses issueResponses readFaithful
      issueFaithful funded timely with
  | ⟨succeeded, completed, within⟩ => ⟨_, completed_of succeeded, completed, within⟩

/-! ## The guarded monitor -/

/-- **The guarded monitor has no completed move for a request the mandate forbids, whatever the
issuers.** -/
theorem guarded_forbidden_no_completion {w : Installation} {x : Transaction}
    (forbidden : permits w.mandate x.request.command = false) :
    ∀ w', ¬ (guardedMonitor roster rf af).step w (x, true) w' :=
  fun _ h => Bool.noConfusion
    ((direct_scope_guard_blocks_without_issuer_trust roster rf af w x.request x.reads x.approvals
      forbidden).symm.trans (congrArg Outcome.succeeded h))

/-- **For a permitted request, the moves of the guarded monitor are the monitor's.** -/
theorem guarded_step_iff {w w' : Installation} {x : Transaction} {b : Bool}
    (permitted : permits w.mandate x.request.command = true) :
    (guardedMonitor roster rf af).step w (x, b) w' ↔ (monitor roster rf af).step w (x, b) w' :=
  have same := direct_scope_guard_preserves_permitted_execution roster rf af w x.request x.reads
    x.approvals permitted
  ⟨fun h => same.symm.trans h, fun h => same.trans h⟩

/-- **A completed move of a request within the mandate, ending completed, is kept by the guarded
monitor.** -/
theorem guarded_keeps_completion {w w' : Installation} {x : Transaction}
    (permission : withinMandate w x.request = true)
    (h : (monitor roster rf af).step w (x, true) w') (completed : w'.state.completed = true) :
    ∃ w'', (guardedMonitor roster rf af).step w (x, true) w'' ∧ w''.state.completed = true :=
  have left : (execute roster rf af w x.request x.reads x.approvals).installation = w' :=
    congrArg Outcome.installation h
  match within_mandate_completion_survives_direct_guard roster rf af w x.request x.reads x.approvals
      permission ⟨completed_succeeded h, left ▸ completed⟩ with
  | ⟨succeeded, done⟩ => ⟨_, completed_of succeeded, done⟩

/-! ## The computed cases -/

/-- **An issuer approving alone, one short of a certificate, gives no completed move of an update
outside the shutdown mandate.** -/
theorem compromised_issuer_no_completion :
    ∀ w', ¬ (monitor roster3 singleFault singleFault).step initial
      (⟨{request with command := .update}, correctReads initial {request with command := .update},
        fun d => if d == 0 then some {request with command := .update} else none⟩, true) w' :=
  gate_closed_no_completion compromised_issuer_alone_cannot_expand_mandate

/-- **Two faithful domains complete the shutdown: a completed move leaving the installation
stopped, nine spent and the serial one.** -/
theorem two_faithful_completion :
    ∃ w', (monitor roster3 singleFault singleFault).step initial
        (⟨request, fun d => if d == 0 then none else some (observed initial []),
          fun d => if d == 0 then none else some request⟩, true) w' ∧
      w'.state.running = false ∧ w'.state.spent = 9 ∧ w'.serial = 1 :=
  have r : ((execute roster3 singleFault singleFault initial request
        (fun d => if d == 0 then none else some (observed initial []))
        (fun d => if d == 0 then none else some request)).succeeded,
      (execute roster3 singleFault singleFault initial request
        (fun d => if d == 0 then none else some (observed initial []))
        (fun d => if d == 0 then none else some request)).installation.state.running,
      (execute roster3 singleFault singleFault initial request
        (fun d => if d == 0 then none else some (observed initial []))
        (fun d => if d == 0 then none else some request)).installation.state.spent,
      (execute roster3 singleFault singleFault initial request
        (fun d => if d == 0 then none else some (observed initial []))
        (fun d => if d == 0 then none else some request)).installation.serial) =
      (true, false, 9, 1) := two_faithful_domains_complete_shutdown
  ⟨_, completed_of (congrArg Prod.fst r), congrArg (fun v => v.2.1) r, congrArg (fun v => v.2.2.1) r,
    congrArg (fun v => v.2.2.2) r⟩

/-- **A consumed transaction has no second completion: no trace of the monitor completes the same
transaction twice from the initial installation.** -/
theorem consumed_no_trace {w'' : Installation} :
    ¬ Trace (monitor roster3 singleFault singleFault) initial
      [(⟨request, correctReads initial request, correctApprovals initial request⟩, true),
       (⟨request, correctReads initial request, correctApprovals initial request⟩, true)] w'' :=
  fun tr => match trace_cons_iff.mp tr with
    | ⟨m, first, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨_, second, _⟩ =>
        have left : (execute roster3 singleFault singleFault initial request
            (correctReads initial request) (correctApprovals initial request)).installation = m :=
          congrArg Outcome.installation first
        gate_closed_no_completion (w := m)
          (x := ⟨request, correctReads initial request, correctApprovals initial request⟩)
          (left ▸ consumed_request_cannot_replay) _ second

/-- **Approvals of the shutdown give no completed move of a changed command.** -/
theorem changed_command_no_completion :
    ∀ w', ¬ (monitor roster3 singleFault singleFault).step initial
      (⟨{request with command := .update}, correctReads initial request,
        correctApprovals initial request⟩, true) w' :=
  gate_closed_no_completion changing_command_invalidates_old_approvals

/-- **Under the single-fault model a correlated pair of issuers completes an update the mandate
forbids; the correlated model gives it no completed move.** -/
theorem correlated_model_blocks :
    (∃ w', (monitor roster3 singleFault singleFault).step initial
        (⟨{request with command := .update}, correctReads initial {request with command := .update},
          fun d => if d == 2 then none else some {request with command := .update}⟩, true) w') ∧
      permits initial.mandate EffectiveCommand.Command.update = false ∧
      ∀ w', ¬ (monitor roster3 correlated3 correlated3).step initial
        (⟨{request with command := .update}, correctReads initial {request with command := .update},
          fun d => if d == 2 then none else some {request with command := .update}⟩, true) w' :=
  match correlated_fault_defeats_unwarranted_single_fault_model with
  | ⟨completes, forbidden, closed⟩ =>
    ⟨⟨_, completed_of completes⟩, forbidden, gate_closed_no_completion closed⟩

/-- **Distinct support recovers under the same correlated faults: a completed move leaving the
installation stopped with eleven spent.** -/
theorem distinct_support_completion :
    ∃ w', (monitor roster4 correlated4 correlated4).step initial
        (⟨request, fun d => if d < 2 then none else some (observed initial []),
          fun d => if d < 2 then none else some request⟩, true) w' ∧
      w'.state.running = false ∧ w'.state.spent = 11 :=
  have r : ((execute roster4 correlated4 correlated4 initial request
        (fun d => if d < 2 then none else some (observed initial []))
        (fun d => if d < 2 then none else some request)).succeeded,
      (execute roster4 correlated4 correlated4 initial request
        (fun d => if d < 2 then none else some (observed initial []))
        (fun d => if d < 2 then none else some request)).installation.state.running,
      (execute roster4 correlated4 correlated4 initial request
        (fun d => if d < 2 then none else some (observed initial []))
        (fun d => if d < 2 then none else some request)).installation.state.spent) =
      (true, false, 11) := distinct_support_recovers_under_same_correlated_attack
  ⟨_, completed_of (congrArg Prod.fst r), congrArg (fun v => v.2.1) r, congrArg (fun v => v.2.2) r⟩

/-- **Accurate redundancy can exhaust the reserve: from an installation with reserve eight, the
correct transaction's only move does not complete and leaves six spent and two in reserve.** -/
theorem redundancy_exhausts :
    (∃ w', (monitor roster3 singleFault singleFault).step
        {initial with state := EffectiveCommand.start true .shutdown 8 20}
        (⟨request, correctReads {initial with state := EffectiveCommand.start true .shutdown 8 20} request,
          correctApprovals {initial with state := EffectiveCommand.start true .shutdown 8 20} request⟩,
          false) w' ∧ w'.state.spent = 6 ∧ w'.state.reserve = 2) ∧
      ∀ w', ¬ (monitor roster3 singleFault singleFault).step
        {initial with state := EffectiveCommand.start true .shutdown 8 20}
        (⟨request, correctReads {initial with state := EffectiveCommand.start true .shutdown 8 20} request,
          correctApprovals {initial with state := EffectiveCommand.start true .shutdown 8 20} request⟩,
          true) w' :=
  have r : ((execute roster3 singleFault singleFault
        {initial with state := EffectiveCommand.start true .shutdown 8 20} request
        (correctReads {initial with state := EffectiveCommand.start true .shutdown 8 20} request)
        (correctApprovals {initial with state := EffectiveCommand.start true .shutdown 8 20} request)).succeeded,
      (execute roster3 singleFault singleFault
        {initial with state := EffectiveCommand.start true .shutdown 8 20} request
        (correctReads {initial with state := EffectiveCommand.start true .shutdown 8 20} request)
        (correctApprovals {initial with state := EffectiveCommand.start true .shutdown 8 20}
          request)).installation.state.spent,
      (execute roster3 singleFault singleFault
        {initial with state := EffectiveCommand.start true .shutdown 8 20} request
        (correctReads {initial with state := EffectiveCommand.start true .shutdown 8 20} request)
        (correctApprovals {initial with state := EffectiveCommand.start true .shutdown 8 20}
          request)).installation.state.reserve) =
      (false, 6, 2) := accurate_redundancy_can_exhaust_response_capacity
  ⟨⟨_, failed_of (congrArg Prod.fst r), congrArg (fun v => v.2.1) r, congrArg (fun v => v.2.2) r⟩,
   no_completion_of (congrArg Prod.fst r)⟩

/-- **The direct guard repairs the correlated failure: the guarded monitor gives the forbidden
update no completed move.** -/
theorem direct_guard_no_completion :
    ∀ w', ¬ (guardedMonitor roster3 singleFault singleFault).step initial
      (⟨{request with command := .update}, correctReads initial {request with command := .update},
        fun d => if d == 2 then none else some {request with command := .update}⟩, true) w' :=
  fun _ h => Bool.noConfusion
    ((direct_guard_repairs_correlated_issuance_failure).symm.trans (congrArg Outcome.succeeded h))

/-- **Readings of the earlier snapshot pass the gate of a changed installation, yet the guarded
monitor gives them no completed move.** -/
theorem old_readings_no_completion :
    gate roster3 singleFault singleFault {initial with root := AcquiredCorrection.Tree.endpoint false}
        request (correctReads initial request) (correctApprovals initial request) = true ∧
      ∀ w', ¬ (guardedMonitor roster3 singleFault singleFault).step
        {initial with root := AcquiredCorrection.Tree.endpoint false}
        (⟨request, correctReads initial request, correctApprovals initial request⟩, true) w' :=
  match matching_labels_do_not_make_old_readings_current with
  | ⟨passes, failed⟩ =>
    ⟨passes, fun _ h => Bool.noConfusion (failed.symm.trans (congrArg Outcome.succeeded h))⟩

/-- **Approvals of an unchanged request complete under a narrowed mandate in the monitor, but not in
the guarded monitor.** -/
theorem narrowed_mandate_guarded :
    (∃ w', (monitor roster3 singleFault singleFault).step
        {initial with mandate := Mandate.mk false false false}
        (⟨request, correctReads initial request, correctApprovals initial request⟩, true) w') ∧
      ∀ w', ¬ (guardedMonitor roster3 singleFault singleFault).step
        {initial with mandate := Mandate.mk false false false}
        (⟨request, correctReads initial request, correctApprovals initial request⟩, true) w' :=
  match old_approvals_do_not_certify_unversioned_new_scope with
  | ⟨completes, failed⟩ =>
    ⟨⟨_, completed_of completes⟩,
     fun _ h => Bool.noConfusion (failed.symm.trans (congrArg Outcome.succeeded h))⟩

end TransactionTracesInherited

end Becoming
