import GenerativeCore
import AcquiredCorrection

/-!
# Dispatch as a process: the delivery step of `AcquiredCorrection`, inherited

`AcquiredCorrection.dispatch current ticket s` re-reads the ticket's address in the current tree,
charging one unit per address component and endpoint, and carries out the command where the key
there is the ticket's, the state is signed and its credential is the current epoch, and reserve
and time allow it; it returns the state after and whether it succeeded. A total transition is a
process of the core: for a current tree, the configurations are deliveries (a state and whether
the last dispatch succeeded), the actions are tickets, and a step by a ticket goes to the
delivery `dispatch` gives from the configuration's state (`process`, `step_iff`). `dispatch` and
the module's laws of it have non-empty axiom reports, so this module is in the periphery-join
ring.

* **Where the current tree has no route at the address, no step succeeds** (`absent_route_fails`,
  through `AcquiredCorrection.absent_current_route_rejects`), and **from a state whose credential
  is not the current epoch, no step succeeds** (`revoked_fails`, through
  `current_revocation_rejects`).
* **A successful step was current.** A step that succeeds had the ticket's key at its address in
  the current tree, and a signed state with the current credential (`succeeded_current`, through
  `successful_dispatch_is_current`).
* **The module's computed cases as steps.** A stale ticket on a changed tree fails
  (`stale_ticket_fails`); a state whose captured credential is the epoch passes
  (`captured_passes`); after acquisition on the example tree a step by the found ticket succeeds
  and stops the installation (`acquired_step_stops`), fails without the reserve for it
  (`unfunded_step_fails`) or after a change of epoch (`changed_epoch_step_fails`), and on the
  changed tree with a renewed epoch a step by the newly found ticket succeeds
  (`renewed_search_step_succeeds`).

No ethical predicate or ranking occurs. The module adds no axiom of its own; it inherits
`propext` from `AcquiredCorrection.dispatch` (through every statement about it) and from
`absent_current_route_rejects` and the computed cases, and `Quot.sound` from
`current_revocation_rejects` and `successful_dispatch_is_current`.
-/

namespace Becoming

open Generative AcquiredCorrection

namespace DispatchProcessesInherited

/-- The dispatch process of a current tree: a delivery steps by a ticket to the delivery
`dispatch` gives from its state. -/
def process (current : Tree) : Process Delivery Ticket :=
  ⟨fun d t e => e = dispatch current t d.state⟩

/-- **The steps of the process are the deliveries of `dispatch`.** -/
theorem step_iff {current : Tree} {d e : Delivery} {t : Ticket} :
    (process current).step d t e ↔ e = dispatch current t d.state :=
  Iff.rfl

/-- **Where the current tree has no route at the ticket's address, no step succeeds.** -/
theorem absent_route_fails {current : Tree} {d e : Delivery} {t : Ticket}
    (step : (process current).step d t e) (absent : locate current t.1 = none) :
    e.succeeded = false :=
  (congrArg Delivery.succeeded step).trans (absent_current_route_rejects current t d.state absent)

/-- **From a state whose credential is not the current epoch, no step succeeds.** -/
theorem revoked_fails {current : Tree} {d e : Delivery} {t : Ticket}
    (step : (process current).step d t e) (revoked : d.state.credential ≠ d.state.authority) :
    e.succeeded = false :=
  (congrArg Delivery.succeeded step).trans (current_revocation_rejects current t d.state revoked)

/-- **A successful step was current.** A step that succeeds had the ticket's key at the ticket's
address in the current tree, and a signed state whose credential is the current epoch. -/
theorem succeeded_current {current : Tree} {d e : Delivery} {t : Ticket}
    (step : (process current).step d t e) (success : e.succeeded = true) :
    locate current t.1 = some t.2 ∧ d.state.signed = true ∧
      d.state.credential = d.state.authority :=
  successful_dispatch_is_current current t d.state
    ((congrArg Delivery.succeeded step).symm.trans success)

/-! ## The computed cases as steps -/

/-- The example tree with the key at its address changed. -/
def changedTree : Tree := .fork .closed (.fork (.endpoint false) .closed)

/-- The initial state with epoch and credential both 99. -/
def capturedState : EffectiveCommand.State := {AcquiredCorrection.initial with authority := 99, credential := 99}

/-- The initial state with epoch and credential both renewed to 8. -/
def renewedState : EffectiveCommand.State := {AcquiredCorrection.initial with authority := 8, credential := 8}

/-- An option whose image is `some b` is `some a` for an `a` with image `b`. -/
theorem map_some {α β : Type} {f : α → β} : ∀ {o : Option α} {b : β}, o.map f = some b →
    ∃ a, o = some a ∧ f a = b
  | some a, _, h => ⟨a, rfl, Option.some.inj h⟩
  | none, _, h => nomatch h

/-- **A stale ticket fails on a changed tree.** On the changed tree, a step by the example ticket
from a state with reserve and deadline 6 does not succeed. -/
theorem stale_ticket_fails {d e : Delivery}
    (from_ : d.state = EffectiveCommand.start false .shutdown 6 6)
    (step : (process changedTree).step d exampleTicket e) : e.succeeded = false :=
  (congrArg Delivery.succeeded step).trans
    (Eq.subst (motive := fun x => (dispatch changedTree exampleTicket x).succeeded = false)
      from_.symm changed_route_rejects_stale_ticket)

/-- **A captured credential that is the epoch passes.** On the single-endpoint tree, a step by the
empty address from the state whose epoch and credential are both 99 succeeds. -/
theorem captured_passes {d e : Delivery} (from_ : d.state = capturedState)
    (step : (process (.endpoint true)).step d ([], true) e) : e.succeeded = true :=
  (congrArg Delivery.succeeded step).trans
    (Eq.subst (motive := fun x => (dispatch (.endpoint true) ([], true) x).succeeded = true)
      from_.symm captured_current_authority_passes_technical_gate)

/-- **After acquisition, the step by the found ticket stops the installation.** Acquisition with
budget 4 on the example tree gives a state from which every step by the example ticket succeeds,
stops the installation, and leaves 10 spent, reserve 0 and time 10. -/
theorem acquired_step_stops :
    ∃ pair, acquire 4 exampleTree AcquiredCorrection.initial = some pair ∧
      ∀ d e, d.state = pair.2 → (process exampleTree).step d exampleTicket e →
        (e.succeeded, e.state.running, e.state.spent, e.state.reserve, e.state.time) =
          (true, false, 10, 0, 10) :=
  match map_some acquired_then_actual_shutdown with
  | ⟨pair, acquired, out⟩ => ⟨pair, acquired, fun _ e from_ step =>
      Eq.subst (motive := fun x : Delivery =>
          (x.succeeded, x.state.running, x.state.spent, x.state.reserve, x.state.time) =
            (true, false, 10, 0, 10))
        (Eq.subst (motive := fun y => dispatch exampleTree exampleTicket y = e) from_
          step.symm) out⟩

/-- **Found but without the reserve, the step fails.** Acquisition with budget 4 on the example
tree from a state with reserve 9 finds the example ticket, and every step by it from the state
after does not succeed, leaving 7 spent and reserve 2. -/
theorem unfunded_step_fails :
    ∃ pair, acquire 4 exampleTree (EffectiveCommand.start false .shutdown 9 10) = some pair ∧
      ∀ d e, d.state = pair.2 → (process exampleTree).step d exampleTicket e →
        (pair.1.verdict, e.succeeded, e.state.spent, e.state.reserve) =
          (.found exampleTicket, false, 7, 2) :=
  match map_some found_but_unaffordable with
  | ⟨pair, acquired, out⟩ => ⟨pair, acquired, fun _ e from_ step =>
      Eq.subst (motive := fun x : Delivery =>
          (pair.1.verdict, x.succeeded, x.state.spent, x.state.reserve) =
            (.found exampleTicket, false, 7, 2))
        (Eq.subst (motive := fun y => dispatch exampleTree exampleTicket y = e) from_
          step.symm) out⟩

/-- **After a change of epoch, the step fails and the search and recheck stay charged.**
Acquisition with budget 4 on the example tree gives a state; with its epoch changed to 8, every
step by the example ticket does not succeed and leaves 7 spent and reserve 3. -/
theorem changed_epoch_step_fails :
    ∃ pair, acquire 4 exampleTree AcquiredCorrection.initial = some pair ∧
      ∀ d e, d.state = {pair.2 with authority := 8} →
        (process exampleTree).step d exampleTicket e →
        (e.succeeded, e.state.spent, e.state.reserve) = (false, 7, 3) :=
  match map_some revocation_keeps_search_and_recheck_cost with
  | ⟨pair, acquired, out⟩ => ⟨pair, acquired, fun _ e from_ step =>
      Eq.subst (motive := fun x : Delivery => (x.succeeded, x.state.spent, x.state.reserve) =
          (false, 7, 3))
        (Eq.subst (motive := fun y => dispatch exampleTree exampleTicket y = e) from_
          step.symm) out⟩

/-- **A renewed epoch and a new search recover.** On the changed tree, acquisition with budget 4
from the state with epoch and credential renewed to 8 finds a ticket, and every step by it from
the state after succeeds. -/
theorem renewed_search_step_succeeds :
    ∃ pair t, acquire 4 changedTree renewedState = some pair ∧ pair.1.verdict = .found t ∧
      ∀ d e, d.state = pair.2 → (process changedTree).step d t e → e.succeeded = true :=
  match map_some renewed_authority_and_new_observation_recover with
  | ⟨pair, acquired, out⟩ =>
    match v : pair.1.verdict, out with
    | .found t, out => ⟨pair, t, acquired, v, fun _ e from_ step =>
        (congrArg Delivery.succeeded
          (Eq.subst (motive := fun y => dispatch changedTree t y = e) from_ step.symm)).symm.trans
          out⟩
    | .exhausted, out => nomatch out
    | .pending, out => nomatch out

end DispatchProcessesInherited

end Becoming
