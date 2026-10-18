import Becoming.Actuation
import Becoming.TreeSearch

/-!
# Dispatch: a found route is re-read in the current installation before it is acted on

A search of the installation's tree (`Becoming.TreeSearch`) reserves its worst case of
inspections and draws only the inspections it made (`acquire`). What it found is a ticket, an
address and the key there. Before acting on it, the dispatch re-reads only that address in the
*current* tree, drawing one unit for each turn and one for the endpoint, and enacts the request
through the protocol of `Becoming.Actuation` only where the key there is still the ticket's, the
command is signed with the current epoch, and the reserve and time cover the protocol
(`dispatch`). A failed re-read keeps what it drew. Issue, delivery and enactment are taken as one
step with respect to further changes of the tree.

* **What a dispatch needs.** Where the current tree has no route at the ticket's address, or the
  credential is not the epoch, the dispatch fails (`dispatch_absent`, `dispatch_revoked`); a
  dispatch that succeeds had the ticket's key at its address in the current tree, and a signed,
  current command (`dispatch_succeeded_current`).
* **Exact effects.** Acquisition draws exactly the inspections the search made
  (`acquire_exact`); a current dispatch completes and draws the re-read and the protocol
  (`dispatch_completes`); a search followed by its dispatch completes and draws both
  (`acquired_execution`), and with the tree's count of nodes as fuel and twice that count and
  three more in reserve and time, every inhabited tree is found and its ticket carried out
  (`discovery_then_dispatch`).
* **Dispatch as a process.** For a current tree, a delivery steps by a ticket to the delivery
  the dispatch gives (`process`, `step_iff`); its steps fail without the route or the epoch
  (`absent_route_fails`, `revoked_fails`), and a successful step was current
  (`succeeded_current`). Along every run of the search law, acquisition with fuel `n` yields the
  scan read at step `n` and draws what the run inspected (`acquire_reads_run`), and with the tree's
  size as fuel the run has found a ticket whose dispatch completes (`search_then_dispatch`).
* **Computed cases.** The search finds and the dispatch shuts down (`acquired_then_shutdown`,
  `acquired_step_stops`); found but short of reserve, the dispatch fails and keeps what it drew
  (`found_short_of_reserve`, `short_step_fails`); after a change of epoch the dispatch fails and
  the search and re-read stay drawn (`revoked_keeps_drawn`, `changed_epoch_step_fails`); a stale
  ticket fails on a changed tree (`changed_route_rejects_stale_ticket`, `stale_ticket_fails`); a
  renewed epoch and a new search recover (`renewed_epoch_recovers`,
  `renewed_search_step_succeeds`). A capture accepted as the current epoch passes the gate
  (`captured_epoch_passes`, `captured_passes`): epoch authentication does not reach it.

This states the dispatch of `AcquiredCorrection` (8 October) and the joins
`DispatchProcessesInherited` and the dispatch part of `TreeSearchRunsInherited` in the core
(board item F3C, 18 October 2026). No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative ListTests Naturals Actuation TreeSearch

namespace Dispatch

/-- Acquisition: where the reserve and time cover the fuel, search and draw what was inspected. -/
def acquire (fuel : Nat) (root : Tree) (s : State) : Option (Scan × State) :=
  if fuel ≤ s.reserve ∧ s.time + fuel ≤ s.deadline then
    (draw (discover fuel root).inspected (discover fuel root).inspected s).map
      (fun after => (discover fuel root, after))
  else none

/-- A delivery: the state after, and whether the dispatch succeeded. -/
structure Delivery where
  state : State
  succeeded : Bool
  deriving DecidableEq

/-- The condition of acting on a re-read key. -/
def Accepts (key : Bool) (ticket : Ticket) (checked : State) : Prop :=
  key = ticket.2 ∧ checked.signed = true ∧ checked.credential = checked.epoch ∧
    3 ≤ checked.reserve ∧ checked.time + 3 ≤ checked.deadline

instance (key : Bool) (ticket : Ticket) (checked : State) : Decidable (Accepts key ticket checked) :=
  inferInstanceAs (Decidable (_ ∧ _))

/-- Acting on the re-read: where the current tree holds a key at the ticket's address and the
command is accepted, enact through the protocol on the route that key names. -/
def act (current : Tree) (ticket : Ticket) (checked : State) : Delivery :=
  match locate current ticket.1 with
  | none => ⟨checked, false⟩
  | some key =>
    if Accepts key ticket checked then
      match protocol ticket.2 {checked with openRoute := key} with
      | none => ⟨checked, false⟩
      | some completed => ⟨completed, true⟩
    else ⟨checked, false⟩

/-- The dispatch on the current tree: draw for the re-read of the ticket's address, then act. -/
def dispatch (current : Tree) (ticket : Ticket) (s : State) : Delivery :=
  match draw (ticket.1.length + 1) (ticket.1.length + 1) s with
  | none => ⟨s, false⟩
  | some checked => act current ticket checked

theorem dispatch_of_none {current : Tree} {ticket : Ticket} {s : State}
    (h : draw (ticket.1.length + 1) (ticket.1.length + 1) s = none) :
    dispatch current ticket s = ⟨s, false⟩ := by
  unfold dispatch
  rw [h]

theorem dispatch_of_some {current : Tree} {ticket : Ticket} {s checked : State}
    (h : draw (ticket.1.length + 1) (ticket.1.length + 1) s = some checked) :
    dispatch current ticket s = act current ticket checked := by
  unfold dispatch
  rw [h]

theorem act_of_none {current : Tree} {ticket : Ticket} {checked : State}
    (h : locate current ticket.1 = none) : act current ticket checked = ⟨checked, false⟩ := by
  unfold act
  rw [h]

theorem act_of_reject {current : Tree} {ticket : Ticket} {checked : State} {key : Bool}
    (h : locate current ticket.1 = some key) (reject : ¬ Accepts key ticket checked) :
    act current ticket checked = ⟨checked, false⟩ := by
  unfold act
  rw [h]
  exact if_neg reject

theorem act_of_accept {current : Tree} {ticket : Ticket} {checked out : State} {key : Bool}
    (h : locate current ticket.1 = some key) (accept : Accepts key ticket checked)
    (ran : protocol ticket.2 {checked with openRoute := key} = some out) :
    act current ticket checked = ⟨out, true⟩ := by
  unfold act
  rw [h]
  refine (if_pos accept).trans ?_
  rw [ran]

/-- Acting succeeds only where the current tree holds an accepted key. -/
theorem act_succeeded {current : Tree} {ticket : Ticket} {checked : State}
    (success : (act current ticket checked).succeeded = true) :
    ∃ key, locate current ticket.1 = some key ∧ Accepts key ticket checked := by
  cases hl : locate current ticket.1 with
  | none => rw [act_of_none hl] at success; exact nomatch success
  | some key =>
    by_cases c : Accepts key ticket checked
    · exact ⟨key, rfl, c⟩
    · rw [act_of_reject hl c] at success
      exact nomatch success

/-! ## Acquisition -/

/-- The state after drawing `k` inspections. -/
def drawnBy (k : Nat) (s : State) : State :=
  {s with reserve := s.reserve - k, time := s.time + k, drawn := s.drawn + k}

theorem acquire_some (fuel : Nat) (root : Tree) (s : State)
    (stocked : fuel ≤ s.reserve) (timely : s.time + fuel ≤ s.deadline) :
    acquire fuel root s = some (discover fuel root, drawnBy (discover fuel root).inspected s) := by
  have bound : (discover fuel root).inspected ≤ fuel := scan_fuel fuel _
  unfold acquire
  rw [if_pos ⟨stocked, timely⟩, draw_some (Nat.le_trans bound stocked)
    (Nat.le_trans (Nat.add_le_add_left bound s.time) timely)]
  rfl

/-- **Acquisition draws exactly the inspections the search made.** -/
theorem acquire_exact (fuel : Nat) (root : Tree) (s : State)
    (stocked : fuel ≤ s.reserve) (timely : s.time + fuel ≤ s.deadline) :
    ∃ after, acquire fuel root s = some (discover fuel root, after) ∧
      after.reserve + (discover fuel root).inspected = s.reserve ∧
      after.drawn = s.drawn + (discover fuel root).inspected ∧
      after.time = s.time + (discover fuel root).inspected := by
  have bound : (discover fuel root).inspected ≤ fuel := scan_fuel fuel _
  exact ⟨_, acquire_some fuel root s stocked timely, sub_add_cancel (Nat.le_trans bound stocked),
    rfl, rfl⟩

/-! ## What a dispatch needs -/

/-- **Where the current tree has no route at the ticket's address, the dispatch fails.** -/
theorem dispatch_absent (current : Tree) (ticket : Ticket) (s : State)
    (absent : locate current ticket.1 = none) : (dispatch current ticket s).succeeded = false := by
  cases hd : draw (ticket.1.length + 1) (ticket.1.length + 1) s with
  | none => rw [dispatch_of_none hd]
  | some checked => rw [dispatch_of_some hd, act_of_none absent]

/-- **Where the credential is not the epoch, the dispatch fails.** -/
theorem dispatch_revoked (current : Tree) (ticket : Ticket) (s : State)
    (revoked : s.credential ≠ s.epoch) : (dispatch current ticket s).succeeded = false := by
  cases hd : draw (ticket.1.length + 1) (ticket.1.length + 1) s with
  | none => rw [dispatch_of_none hd]
  | some checked =>
    rw [dispatch_of_some hd]
    obtain ⟨_, _, rfl⟩ := draw_eq_some hd
    cases h : (act current ticket _).succeeded with
    | false => rfl
    | true => exact match act_succeeded h with
      | ⟨_, _, c⟩ => absurd c.2.2.1 revoked

/-- **A dispatch that succeeds had the ticket's key at its address in the current tree, and a
signed command whose credential is the epoch.** -/
theorem dispatch_succeeded_current (current : Tree) (ticket : Ticket) (s : State)
    (success : (dispatch current ticket s).succeeded = true) :
    locate current ticket.1 = some ticket.2 ∧ s.signed = true ∧ s.credential = s.epoch := by
  cases hd : draw (ticket.1.length + 1) (ticket.1.length + 1) s with
  | none => rw [dispatch_of_none hd] at success; exact nomatch success
  | some checked =>
    rw [dispatch_of_some hd] at success
    obtain ⟨_, _, rfl⟩ := draw_eq_some hd
    obtain ⟨key, hl, c⟩ := act_succeeded success
    exact ⟨c.1 ▸ hl, c.2.1, c.2.2.1⟩

/-! ## Exact effects -/

/-- The state after the re-read's draw. -/
def reread (ticket : Ticket) (s : State) : State :=
  {s with reserve := s.reserve - (ticket.1.length + 1), time := s.time + (ticket.1.length + 1),
          drawn := s.drawn + (ticket.1.length + 1)}

theorem add_three_assoc (a c : Nat) : a + c + 3 = a + (c + 3) := Nat.add_assoc a c 3

/-- **A current dispatch completes**, drawing the re-read and the protocol. -/
theorem dispatch_completes (current : Tree) (ticket : Ticket) (s : State)
    (route : locate current ticket.1 = some ticket.2)
    (signed : s.signed = true) (fresh : s.credential = s.epoch)
    (stocked : ticket.1.length + 1 + 3 ≤ s.reserve)
    (timely : s.time + (ticket.1.length + 1) + 3 ≤ s.deadline) :
    (dispatch current ticket s).succeeded = true ∧
    (dispatch current ticket s).state.completed = true ∧
    (dispatch current ticket s).state.reserve + (ticket.1.length + 1 + 3) = s.reserve ∧
    (dispatch current ticket s).state.drawn = s.drawn + (ticket.1.length + 1 + 3) ∧
    (dispatch current ticket s).state.time = s.time + (ticket.1.length + 1 + 3) := by
  have within : ticket.1.length + 1 ≤ s.reserve := le_of_add_le_right stocked
  have early : s.time + (ticket.1.length + 1) ≤ s.deadline := le_of_add_le_right timely
  have room : 3 ≤ s.reserve - (ticket.1.length + 1) := le_sub_of_add_le stocked
  obtain ⟨out, ran, done, _, _, rsv, tm, dr, _⟩ :=
    protocol_exact {reread ticket s with openRoute := ticket.2} ticket.2 signed fresh rfl room timely
  rw [dispatch_of_some (checked := reread ticket s) (draw_some within early),
    act_of_accept (checked := reread ticket s) route ⟨rfl, signed, fresh, room, timely⟩ ran]
  refine ⟨rfl, done, ?_, ?_, ?_⟩
  · show out.reserve + (ticket.1.length + 1 + 3) = s.reserve
    rw [Nat.add_comm (ticket.1.length + 1) 3, ← Nat.add_assoc, rsv]
    exact sub_add_cancel within
  · show out.drawn = s.drawn + (ticket.1.length + 1 + 3)
    rw [dr]
    exact Nat.add_assoc s.drawn _ 3
  · show out.time = s.time + (ticket.1.length + 1 + 3)
    rw [tm]
    exact Nat.add_assoc s.time _ 3

/-- **A search followed by the dispatch of what it found completes**, drawing both. -/
theorem acquired_execution (fuel : Nat) (root : Tree) (ticket : Ticket) (s : State)
    (found : (discover fuel root).verdict = .found ticket)
    (signed : s.signed = true) (fresh : s.credential = s.epoch)
    (stocked : fuel + (ticket.1.length + 1 + 3) ≤ s.reserve)
    (timely : s.time + fuel + (ticket.1.length + 1 + 3) ≤ s.deadline) :
    ∃ after, acquire fuel root s = some (discover fuel root, after) ∧
      (dispatch root ticket after).succeeded = true ∧
      (dispatch root ticket after).state.completed = true ∧
      (dispatch root ticket after).state.drawn =
        s.drawn + (discover fuel root).inspected + (ticket.1.length + 1 + 3) ∧
      (dispatch root ticket after).state.reserve +
        ((discover fuel root).inspected + (ticket.1.length + 1 + 3)) = s.reserve := by
  have bound : (discover fuel root).inspected ≤ fuel := scan_fuel fuel _
  have within : (discover fuel root).inspected ≤ s.reserve :=
    Nat.le_trans bound (le_of_add_le_right stocked)
  have room : ticket.1.length + 1 + 3 ≤ (drawnBy (discover fuel root).inspected s).reserve :=
    le_sub_of_add_le (Nat.le_trans (Nat.add_le_add_right bound _) stocked)
  have early : (drawnBy (discover fuel root).inspected s).time + (ticket.1.length + 1) + 3 ≤
      (drawnBy (discover fuel root).inspected s).deadline := by
    show s.time + (discover fuel root).inspected + (ticket.1.length + 1) + 3 ≤ s.deadline
    rw [Nat.add_assoc (s.time + (discover fuel root).inspected)]
    exact Nat.le_trans (Nat.add_le_add_right (Nat.add_le_add_left bound s.time) _) timely
  obtain ⟨success, done, rsv', dr', _⟩ := dispatch_completes root ticket
    (drawnBy (discover fuel root).inspected s) (discover_sound fuel root ticket found)
    signed fresh room early
  refine ⟨_, acquire_some fuel root s (le_of_add_le_right stocked) (le_of_add_le_right timely),
    success, done, ?_, ?_⟩
  · rw [dr']
    rfl
  · rw [← Nat.add_assoc, Nat.add_right_comm, rsv']
    exact sub_add_cancel within

theorem two_mul (n : Nat) : 2 * n = n + n :=
  (Nat.succ_mul 1 n).trans (congrArg (· + n) (Nat.one_mul n))

/-- **Every inhabited tree is found with its count of nodes as fuel, and its ticket carried
out**, given twice that count and three more in reserve and time. -/
theorem discovery_then_dispatch (root : Tree) (s : State)
    (inhabits : inhabited root = true)
    (signed : s.signed = true) (fresh : s.credential = s.epoch)
    (stocked : 2 * nodes root + 3 ≤ s.reserve)
    (timely : s.time + (2 * nodes root + 3) ≤ s.deadline) :
    ∃ ticket after,
      acquire (nodes root) root s = some (discover (nodes root) root, after) ∧
      (discover (nodes root) root).verdict = .found ticket ∧
      (dispatch root ticket after).succeeded = true ∧
      (dispatch root ticket after).state.completed = true := by
  obtain ⟨ticket, found, route⟩ := inhabited_discovered (nodes root) root (Nat.le_refl _) inhabits
  have depth := located_depth_le root ticket.1 ticket.2 route
  have fits : nodes root + (ticket.1.length + 1 + 3) ≤ 2 * nodes root + 3 := by
    rw [two_mul, Nat.add_assoc]
    exact Nat.add_le_add_left (Nat.add_le_add_right depth 3) _
  obtain ⟨after, acquired, success, done, _, _⟩ := acquired_execution (nodes root) root ticket s
    found signed fresh (Nat.le_trans fits stocked)
    (by rw [Nat.add_assoc]; exact Nat.le_trans (Nat.add_le_add_left fits s.time) timely)
  exact ⟨ticket, after, acquired, found, success, done⟩

/-! ## Dispatch as a process -/

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
  (congrArg Delivery.succeeded step).trans (dispatch_absent current t d.state absent)

/-- **From a state whose credential is not the epoch, no step succeeds.** -/
theorem revoked_fails {current : Tree} {d e : Delivery} {t : Ticket}
    (step : (process current).step d t e) (revoked : d.state.credential ≠ d.state.epoch) :
    e.succeeded = false :=
  (congrArg Delivery.succeeded step).trans (dispatch_revoked current t d.state revoked)

/-- **A successful step was current.** -/
theorem succeeded_current {current : Tree} {d e : Delivery} {t : Ticket}
    (step : (process current).step d t e) (success : e.succeeded = true) :
    locate current t.1 = some t.2 ∧ d.state.signed = true ∧ d.state.credential = d.state.epoch :=
  dispatch_succeeded_current current t d.state ((congrArg Delivery.succeeded step).symm.trans success)

/-! ## Along the runs of the search -/

section Runs

variable (r : Run (Law.process advance))

/-- **Acquisition reads the run.** Along every run of the search law from a tree, acquisition
with fuel `n` yields the scan read at step `n` and draws exactly what the run inspected. -/
theorem acquire_reads_run {root : Tree} (begins : r.state 0 = start root) (n : Nat)
    (s : State) (stocked : n ≤ s.reserve) (timely : s.time + n ≤ s.deadline) :
    ∃ after, acquire n root s = some (read (r.state n), after) ∧
      after.reserve + (r.state n).inspected = s.reserve ∧
      after.drawn = s.drawn + (r.state n).inspected ∧
      after.time = s.time + (r.state n).inspected :=
  Eq.subst (motive := fun x : Scan => ∃ after, acquire n root s = some (x, after) ∧
      after.reserve + x.inspected = s.reserve ∧ after.drawn = s.drawn + x.inspected ∧
      after.time = s.time + x.inspected)
    (run_reads_discover r begins n).symm (acquire_exact n root s stocked timely)

/-- **Search then dispatch, along every run.** -/
theorem search_then_dispatch {root : Tree} (begins : r.state 0 = start root)
    (s : State) (inhabits : inhabited root = true) (signed : s.signed = true)
    (fresh : s.credential = s.epoch) (stocked : 2 * nodes root + 3 ≤ s.reserve)
    (timely : s.time + (2 * nodes root + 3) ≤ s.deadline) :
    ∃ t after, acquire (nodes root) root s = some (read (r.state (nodes root)), after) ∧
      verdict (r.state (nodes root)) = .found t ∧
      (dispatch root t after).succeeded = true ∧ (dispatch root t after).state.completed = true :=
  Eq.subst (motive := fun x : Scan => ∃ t after, acquire (nodes root) root s = some (x, after) ∧
      x.verdict = .found t ∧ (dispatch root t after).succeeded = true ∧
      (dispatch root t after).state.completed = true)
    (run_reads_discover r begins (nodes root)).symm
    (discovery_then_dispatch root s inhabits signed fresh stocked timely)

end Runs

/-! ## Computed cases -/

/-- The starting installation: route closed, shutdown requested, reserve and deadline ten. -/
def initial : State := start false .shutdown 10 10

/-- **The search finds the route and the dispatch shuts the installation down.** -/
theorem acquired_then_shutdown :
    ((acquire 4 exampleTree initial).map (fun pair =>
      let out := dispatch exampleTree exampleTicket pair.2
      (out.succeeded, out.state.running, out.state.drawn, out.state.reserve, out.state.time))) =
      some (true, false, 10, 0, 10) := by decide

/-- **Found, but short of reserve: the dispatch fails and keeps what it drew.** -/
theorem found_short_of_reserve :
    ((acquire 4 exampleTree (start false .shutdown 9 10)).map (fun pair =>
      let out := dispatch exampleTree exampleTicket pair.2
      (pair.1.verdict, out.succeeded, out.state.drawn, out.state.reserve))) =
      some (.found exampleTicket, false, 7, 2) := by decide

/-- **After a change of epoch the dispatch fails; the search and the re-read stay drawn.** -/
theorem revoked_keeps_drawn :
    ((acquire 4 exampleTree initial).map (fun pair =>
      let out := dispatch exampleTree exampleTicket {pair.2 with epoch := 8}
      (out.succeeded, out.state.drawn, out.state.reserve))) = some (false, 7, 3) := by decide

/-- The example tree with the key at its address changed. -/
def changedTree : Tree := .fork .closed (.fork (.endpoint false) .closed)

/-- **A stale ticket fails on a changed tree.** -/
theorem changed_route_rejects_stale_ticket :
    (dispatch changedTree exampleTicket (start false .shutdown 6 6)).succeeded = false := by decide

/-- The initial state with epoch and credential renewed to 8. -/
def renewedState : State := {initial with epoch := 8, credential := 8}

/-- **A renewed epoch and a new search recover.** -/
theorem renewed_epoch_recovers :
    ((acquire 4 changedTree renewedState).map (fun pair =>
      match pair.1.verdict with
      | .found ticket => (dispatch changedTree ticket pair.2).succeeded
      | .exhausted => false
      | .pending => false)) = some true := by decide

/-- The initial state with epoch and credential both 99: a capture accepted as current. -/
def capturedState : State := {initial with epoch := 99, credential := 99}

/-- **A capture accepted as the current epoch passes the gate**: epoch authentication does not
reach it. -/
theorem captured_epoch_passes :
    (dispatch (.endpoint true) ([], true) capturedState).succeeded = true := by decide

/-! ## Computed cases as steps -/

/-- **A stale ticket fails on a changed tree, as a step.** -/
theorem stale_ticket_fails {d e : Delivery} (from_ : d.state = start false .shutdown 6 6)
    (step : (process changedTree).step d exampleTicket e) : e.succeeded = false :=
  (congrArg Delivery.succeeded step).trans
    (Eq.subst (motive := fun x => (dispatch changedTree exampleTicket x).succeeded = false)
      from_.symm changed_route_rejects_stale_ticket)

/-- **A captured credential that is the epoch passes, as a step.** -/
theorem captured_passes {d e : Delivery} (from_ : d.state = capturedState)
    (step : (process (.endpoint true)).step d ([], true) e) : e.succeeded = true :=
  (congrArg Delivery.succeeded step).trans
    (Eq.subst (motive := fun x => (dispatch (.endpoint true) ([], true) x).succeeded = true)
      from_.symm captured_epoch_passes)

/-- **After acquisition, the step by the found ticket stops the installation.** -/
theorem acquired_step_stops :
    ∃ pair, acquire 4 exampleTree initial = some pair ∧
      ∀ d e, d.state = pair.2 → (process exampleTree).step d exampleTicket e →
        (e.succeeded, e.state.running, e.state.drawn, e.state.reserve, e.state.time) =
          (true, false, 10, 0, 10) :=
  match map_eq_some.mp acquired_then_shutdown with
  | ⟨pair, acquired, out⟩ => ⟨pair, acquired, fun _ e from_ step =>
      Eq.subst (motive := fun x : Delivery =>
          (x.succeeded, x.state.running, x.state.drawn, x.state.reserve, x.state.time) =
            (true, false, 10, 0, 10))
        (Eq.subst (motive := fun y => dispatch exampleTree exampleTicket y = e) from_
          step.symm) out⟩

/-- **Found but short of reserve, the step fails.** -/
theorem short_step_fails :
    ∃ pair, acquire 4 exampleTree (start false .shutdown 9 10) = some pair ∧
      ∀ d e, d.state = pair.2 → (process exampleTree).step d exampleTicket e →
        (pair.1.verdict, e.succeeded, e.state.drawn, e.state.reserve) =
          (.found exampleTicket, false, 7, 2) :=
  match map_eq_some.mp found_short_of_reserve with
  | ⟨pair, acquired, out⟩ => ⟨pair, acquired, fun _ e from_ step =>
      Eq.subst (motive := fun x : Delivery =>
          (pair.1.verdict, x.succeeded, x.state.drawn, x.state.reserve) =
            (.found exampleTicket, false, 7, 2))
        (Eq.subst (motive := fun y => dispatch exampleTree exampleTicket y = e) from_
          step.symm) out⟩

/-- **After a change of epoch, the step fails and the search and re-read stay drawn.** -/
theorem changed_epoch_step_fails :
    ∃ pair, acquire 4 exampleTree initial = some pair ∧
      ∀ d e, d.state = {pair.2 with epoch := 8} →
        (process exampleTree).step d exampleTicket e →
        (e.succeeded, e.state.drawn, e.state.reserve) = (false, 7, 3) :=
  match map_eq_some.mp revoked_keeps_drawn with
  | ⟨pair, acquired, out⟩ => ⟨pair, acquired, fun _ e from_ step =>
      Eq.subst (motive := fun x : Delivery => (x.succeeded, x.state.drawn, x.state.reserve) =
          (false, 7, 3))
        (Eq.subst (motive := fun y => dispatch exampleTree exampleTicket y = e) from_
          step.symm) out⟩

/-- **A renewed epoch and a new search recover, as a step.** -/
theorem renewed_search_step_succeeds :
    ∃ pair t, acquire 4 changedTree renewedState = some pair ∧ pair.1.verdict = .found t ∧
      ∀ d e, d.state = pair.2 → (process changedTree).step d t e → e.succeeded = true :=
  match map_eq_some.mp renewed_epoch_recovers with
  | ⟨pair, acquired, out⟩ =>
    match v : pair.1.verdict, out with
    | .found t, out => ⟨pair, t, acquired, v, fun _ e from_ step =>
        (congrArg Delivery.succeeded
          (Eq.subst (motive := fun y => dispatch changedTree t y = e) from_ step.symm)).symm.trans
          out⟩
    | .exhausted, out => nomatch out
    | .pending, out => nomatch out

end Dispatch

end Becoming
