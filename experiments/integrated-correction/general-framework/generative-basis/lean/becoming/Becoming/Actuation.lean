import Becoming.ContingentPlans
import Becoming.Naturals

/-!
# Actuation: recognition, delivery and enactment as consecutive steps of one installation

One installation is corrected through three consecutive changes of its state: a command is
issued where the request is signed and its credential is the current epoch, delivered along the
route that is open, and enacted where it was delivered and its credential is still current
(`issue`, `deliver`, `enact`, `protocol`). Every step draws one unit from the reserve and one
unit of time before the deadline (`draw`), and fails (`none`) where its conditions do not hold.
An inquiry about the route draws too (`probe`). The epoch is supplied by a process the planner
and its goal cannot rewrite; no cryptographic claim is made.

* **The installation is a process.** Its moves are an inquiry with its answer, issuing,
  delivering along a route and enacting (`installation`). The protocol on a route takes `s` to
  `t` exactly where the installation has a trace of issuing, delivering and enacting
  (`protocol_iff`); a contingent plan's run (`ContingentPlans.run`) is a trace of its inquiry
  followed by the protocol on the route the answer selects (`run_iff`), and it passes exactly
  where such a trace ends completed (`passes_iff`). A plan selected for a belief has a completed
  trace from every configuration of it (`chosen_completes`); where none is selected for two
  configurations, no plan of the repertoire has one from both (`none_chosen`).
* **What a move needs.** An unsigned configuration has no issuing move, nor one whose credential
  is not the epoch (`issue_unsigned`, `issue_stale`, `unsigned_no_issue`, `stale_no_issue`); an
  undelivered configuration has no enacting move, nor one whose credential is no longer the epoch
  (`enact_undelivered`, `enact_revoked`, `undelivered_no_enact`, `revoked_no_enact`).
* **The reserve and what is drawn are conserved.** A draw keeps their sum and keeps time within
  the deadline (`draw_conserves`); every move either leaves the configuration or draws
  (`move_draws`), so their sum is invariant (`conserved_invariant`) along every trace
  (`conserved_trace`).
* **The protocol completes where its conditions hold** (`protocol_exact`,
  `protocol_completes`): signed, credential current, route open, a reserve of three and three
  units of time left give a trace ending completed, three drawn and the epoch unchanged.
* **Computed cases, as runs and as traces.** Where the route is unknown the route inquiry is
  selected and completes from both configurations (`unknown_route_probes`,
  `route_inquiry_completes_both`); where it is known, no inquiry is needed
  (`known_route_no_probe`, `known_route_completes`). Paths from each configuration are not a
  uniform plan (`statewise_not_uniform_run`, `statewise_not_uniform`). A timely inquiry keeps
  the correction possible and an equally accurate but slow one does not (`timely_run`,
  `late_probe_no_run`, `timely_trace`, `late_no_trace`). Shutdown, replacement and update
  complete with the effects they name (`shutdown_run`, `replacement_run`, `update_run`,
  `shutdown_trace`, `replacement_trace`, `update_trace`). A plan selected from a model that omits
  the open route fails where the route is open (`omitted_route_fails_run`, `omitted_route_fails`).

This states `EffectiveCommand` (8 October) and its joins `InstallationTraces` and
`InstallationTracesInherited` in the core (board item F3C, 18 October 2026), with the words of
exchange replaced: the periphery's `spend` is `draw`, `spent` is `drawn`, `authority` is
`epoch`. No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative ListTests Naturals ContingentPlans

namespace Actuation

/-- What may be requested. -/
inductive Command where
  | update | replace | shutdown
  deriving DecidableEq

/-- What may be asked about the route: nothing, the route, or the route more slowly. -/
inductive Query where
  | none | route | slow
  deriving DecidableEq

/-- The installation's state. -/
structure State where
  openRoute : Bool
  epoch : Nat
  credential : Nat
  signed : Bool
  requested : Command
  reserve : Nat
  time : Nat
  deadline : Nat
  issued : Bool := false
  delivered : Bool := false
  completed : Bool := false
  running : Bool := true
  generation : Nat := 0
  version : Nat := 0
  drawn : Nat := 0
  deriving DecidableEq

/-- Draw an amount from the reserve and a delay of time, where both are available. -/
def draw (amount delay : Nat) (s : State) : Option State :=
  if amount ≤ s.reserve ∧ s.time + delay ≤ s.deadline then
    some {s with reserve := s.reserve - amount, time := s.time + delay, drawn := s.drawn + amount}
  else none

/-- Issue the command, where it is signed and its credential is the epoch. -/
def issue (s : State) : Option State := do
  if s.signed && (s.credential == s.epoch) then
    let t ← draw 1 1 s
    pure {t with issued := true}
  else none

/-- Deliver the issued command along a route, where that route is the open one. -/
def deliver (route : Bool) (s : State) : Option State := do
  if s.issued && (route == s.openRoute) then
    let t ← draw 1 1 s
    pure {t with delivered := true}
  else none

/-- Enact the delivered command, where its credential is still the epoch. -/
def enact (s : State) : Option State := do
  if s.delivered && s.signed && (s.credential == s.epoch) then
    let t ← draw 1 1 s
    pure {t with
      completed := true
      running := s.requested != .shutdown
      generation := s.generation + if s.requested == .replace then 1 else 0
      version := s.version + if s.requested == .update then 1 else 0}
  else none

/-- The protocol on a route: issue, deliver along the route, enact. -/
def protocol (route : Bool) (s : State) : Option State :=
  issue s >>= deliver route >>= enact

/-- Inquiry: no question answers `false` and draws nothing; the route question answers whether
the route is open, drawing one unit and one or three units of time. -/
def probe (s : State) (q : Query) : Option (Bool × State) := do
  match q with
  | .none => pure (false, s)
  | .route => let t ← draw 1 1 s; pure (s.openRoute, t)
  | .slow => let t ← draw 1 3 s; pure (s.openRoute, t)

/-- The installation's interface: inquire, run the protocol on the route answered, completion. -/
def interface : Interface State Query Bool := ⟨probe, (fun s a => protocol a s), State.completed⟩

/-- The repertoire of plans: every query and every pair of routes. -/
def plans : List (Plan Query Bool) := repertoire [.none, .route, .slow] [false, true]

/-- A starting state: route, request, reserve and deadline; epoch and credential 7. -/
def start (r : Bool) (c : Command) (fuel limit : Nat) : State :=
  ⟨r, 7, 7, true, c, fuel, 0, limit, false, false, false, true, 0, 0, 0⟩

/-! ## A draw -/

theorem draw_some {amount delay : Nat} {s : State} (within : amount ≤ s.reserve)
    (timely : s.time + delay ≤ s.deadline) :
    draw amount delay s =
      some {s with reserve := s.reserve - amount, time := s.time + delay,
                   drawn := s.drawn + amount} :=
  if_pos ⟨within, timely⟩

theorem draw_none {amount delay : Nat} {s : State}
    (short : ¬ (amount ≤ s.reserve ∧ s.time + delay ≤ s.deadline)) : draw amount delay s = none :=
  if_neg short

/-- What a draw gives: the reserve was enough, time within the deadline, and the state after. -/
theorem draw_eq_some {amount delay : Nat} {s t : State} (h : draw amount delay s = some t) :
    amount ≤ s.reserve ∧ s.time + delay ≤ s.deadline ∧
      t = {s with reserve := s.reserve - amount, time := s.time + delay,
                  drawn := s.drawn + amount} := by
  unfold draw at h
  by_cases yes : amount ≤ s.reserve ∧ s.time + delay ≤ s.deadline
  · rw [if_pos yes] at h
    exact ⟨yes.1, yes.2, (Option.some.inj h).symm⟩
  · rw [if_neg yes] at h
    exact nomatch h

/-- **A draw keeps the reserve plus what is drawn, and keeps time within the deadline.** -/
theorem draw_conserves {s t : State} {c d : Nat} (h : draw c d s = some t) :
    t.reserve + t.drawn = s.reserve + s.drawn ∧ t.time ≤ t.deadline :=
  by
    obtain ⟨within, timely, rfl⟩ := draw_eq_some h
    exact ⟨sub_add_add within, timely⟩

/-! ## What a move needs -/

theorem beq_self {α : Type} [DecidableEq α] (n : α) : (n == n) = true := decide_eq_true rfl

theorem beq_ne {a b : Nat} (h : a ≠ b) : (a == b) = false := beq_false_iff.mpr h

/-- **An unsigned command is not issued.** -/
theorem issue_unsigned (s : State) (h : s.signed = false) : issue s = none := by
  unfold issue
  rw [h]
  rfl

/-- **A command whose credential is not the epoch is not issued.** -/
theorem issue_stale (s : State) (h : s.credential ≠ s.epoch) : issue s = none := by
  unfold issue
  rw [beq_ne h, Bool.and_false]
  rfl

/-- **An undelivered command is not enacted.** -/
theorem enact_undelivered (s : State) (h : s.delivered = false) : enact s = none := by
  unfold enact
  rw [h]
  rfl

/-- **A command whose credential is no longer the epoch is not enacted.** -/
theorem enact_revoked (s : State) (h : s.credential ≠ s.epoch) : enact s = none := by
  unfold enact
  rw [beq_ne h, Bool.and_false]
  rfl

/-! ## The protocol where its conditions hold -/

/-- **The protocol completes where its conditions hold.** A signed command whose credential is
the epoch, on the open route, with a reserve of three and three units of time left, completes:
delivered, issued, three drawn, three units of time used, the epoch unchanged. -/
theorem protocol_exact (s : State) (r : Bool)
    (signed : s.signed = true) (current : s.credential = s.epoch)
    (route : r = s.openRoute) (stocked : 3 ≤ s.reserve)
    (timely : s.time + 3 ≤ s.deadline) :
    ∃ t, protocol r s = some t ∧ t.completed = true ∧ t.delivered = true ∧
      t.issued = true ∧ t.reserve + 3 = s.reserve ∧ t.time = s.time + 3 ∧
      t.drawn = s.drawn + 3 ∧ t.epoch = s.epoch := by
  have r1 : 1 ≤ s.reserve := le_of_add_le_left (b := 1) (a := 2) stocked
  have r2 : 1 ≤ s.reserve - 1 := le_sub_of_add_le (le_of_add_le_right (a := 1 + 1) (b := 1) stocked)
  have r3 : 1 ≤ s.reserve - 1 - 1 :=
    (sub_sub s.reserve 1 1).symm ▸ le_sub_of_add_le (a := 1 + 1) (b := 1) stocked
  have t1 : s.time + 1 ≤ s.deadline :=
    Nat.le_trans (Nat.add_le_add_left (show 1 ≤ 3 by decide) s.time) timely
  have t2 : s.time + 1 + 1 ≤ s.deadline :=
    Nat.le_trans (Nat.add_le_add_left (show 2 ≤ 3 by decide) s.time) timely
  have t3 : s.time + 1 + 1 + 1 ≤ s.deadline := timely
  let s1 : State := {s with reserve := s.reserve - 1, time := s.time + 1, drawn := s.drawn + 1,
                            issued := true}
  let s2 : State := {s1 with reserve := s1.reserve - 1, time := s1.time + 1,
                             drawn := s1.drawn + 1, delivered := true}
  let s3 : State := {s2 with reserve := s2.reserve - 1, time := s2.time + 1,
                             drawn := s2.drawn + 1, completed := true,
                             running := s2.requested != .shutdown,
                             generation := s2.generation + if s2.requested == .replace then 1 else 0,
                             version := s2.version + if s2.requested == .update then 1 else 0}
  have h1 : issue s = some s1 := by
    unfold issue
    rw [signed, current, beq_self, draw_some r1 t1]
    rfl
  have h2 : deliver r s1 = some s2 := by
    unfold deliver
    show (if (true && (r == s.openRoute)) = true then _ else _) = _
    rw [route, beq_self, draw_some (s := s1) r2 t2]
    rfl
  have h3 : enact s2 = some s3 := by
    unfold enact
    show (if (true && s.signed && (s.credential == s.epoch)) = true then _ else _) = _
    rw [signed, current, beq_self, draw_some (s := s2) r3 t3]
    rfl
  refine ⟨s3, ?_, rfl, rfl, rfl, ?_, rfl, ?_, rfl⟩
  · show (issue s >>= deliver r >>= enact) = some s3
    rw [h1]
    show (deliver r s1 >>= enact) = some s3
    rw [h2]
    exact h3
  · show s.reserve - 1 - 1 - 1 + 3 = s.reserve
    rw [sub_sub, sub_sub]
    exact sub_add_cancel stocked
  · show s.drawn + 1 + 1 + 1 = s.drawn + 3
    rfl

/-! ## The installation as a process -/

/-- The installation's moves: an inquiry with its answer, issuing, delivering along a route, and
enacting. -/
inductive Move where
  | probe (q : Query) (answer : Bool)
  | issue
  | deliver (route : Bool)
  | enact

/-- **The installation as a process**: each move takes a configuration to what the
installation's step of that move gives. -/
def installation : Process State Move where
  step s m t := match m with
    | .probe q o => probe s q = some (o, t)
    | .issue => issue s = some t
    | .deliver r => deliver r s = some t
    | .enact => enact s = some t

/-- The protocol's moves on a route. -/
def protocolMoves (r : Bool) : List Move := [.issue, .deliver r, .enact]

/-- A plan's moves with a given answer: its inquiry, then the protocol on the route the answer
selects. -/
def planMoves (p : Plan Query Bool) (o : Bool) : List Move :=
  .probe p.query o :: protocolMoves (branch p o)

/-- **The protocol on a route is a trace of issuing, delivering along that route and
enacting.** -/
theorem protocol_iff (r : Bool) (s t : State) :
    protocol r s = some t ↔ Trace installation s (protocolMoves r) t :=
  ⟨fun h =>
    match bind_eq_some.mp h with
    | ⟨_, h12, h3⟩ => match bind_eq_some.mp h12 with
      | ⟨_, h1, h2⟩ => .cons h1 (.cons h2 (.cons h3 (.nil t))),
   fun tr =>
    match trace_cons_iff.mp tr with
    | ⟨_, h1, tr⟩ => match trace_cons_iff.mp tr with
      | ⟨_, h2, tr⟩ => match trace_cons_iff.mp tr with
        | ⟨_, h3, tr⟩ => bind_eq_some.mpr ⟨_, bind_eq_some.mpr ⟨_, h1, h2⟩,
            (trace_nil_iff.mp tr) ▸ h3⟩⟩

/-- **A plan's run is a trace of its inquiry, then the protocol on the route the answer
selects.** -/
theorem run_iff (p : Plan Query Bool) (s u : State) :
    run interface p s = some u ↔ ∃ o, Trace installation s (planMoves p o) u :=
  ⟨fun h =>
    match bind_eq_some.mp h with
    | ⟨(o, _), probed, rest⟩ => ⟨o, .cons probed ((protocol_iff _ _ _).mp rest)⟩,
   fun ⟨o, tr⟩ =>
    match trace_cons_iff.mp tr with
    | ⟨m, probed, rest⟩ => bind_eq_some.mpr ⟨(o, m), probed, (protocol_iff _ _ _).mpr rest⟩⟩

/-- **A plan passes exactly where the installation has a trace along it ending completed.** -/
theorem passes_iff (p : Plan Query Bool) (s : State) :
    passes interface p s = true ↔ ∃ o u, Trace installation s (planMoves p o) u ∧ u.completed = true :=
  (passes_iff_run interface p s).trans
    ⟨fun ⟨u, ran, done⟩ => match (run_iff p s u).mp ran with
      | ⟨o, tr⟩ => ⟨o, u, tr, done⟩,
     fun ⟨o, u, tr, done⟩ => ⟨u, (run_iff p s u).mpr ⟨o, tr⟩, done⟩⟩

/-- **A plan selected for a list of configurations has, from every one of them, a trace ending
completed.** -/
theorem chosen_completes {states : List State} {ps : List (Plan Query Bool)} {p : Plan Query Bool}
    (chosen : choose interface states ps = some p) :
    ∀ s, s ∈ states → ∃ o u, Trace installation s (planMoves p o) u ∧ u.completed = true :=
  fun s member => (passes_iff p s).mp ((valid_iff_passes interface states p).mp (find_some chosen) |>.2 s member)

/-- **Where no plan is selected for two configurations, no plan of the repertoire has a completed
trace from both.** -/
theorem none_chosen {s₁ s₂ : State} {ps : List (Plan Query Bool)}
    (absent : choose interface [s₁, s₂] ps = none) :
    ∀ p, p ∈ ps →
      ¬ ((∃ o u, Trace installation s₁ (planMoves p o) u ∧ u.completed = true) ∧
        ∃ o u, Trace installation s₂ (planMoves p o) u ∧ u.completed = true) :=
  fun p member ⟨first, second⟩ =>
    have valid : valid interface [s₁, s₂] p = true :=
      (valid_iff_passes interface [s₁, s₂] p).mpr ⟨fun e => (nomatch e), fun s m =>
        match s, m with
        | _, .head _ => (passes_iff p s₁).mpr first
        | _, .tail _ (.head _) => (passes_iff p s₂).mpr second⟩
    Bool.noConfusion ((find_none_iff.mp absent p member).symm.trans valid)

/-! ## What a move needs, as moves of the process -/

/-- **An unsigned configuration has no issuing move.** -/
theorem unsigned_no_issue {s : State} (unsigned : s.signed = false) :
    ¬ Enabled installation s .issue :=
  fun ⟨_, h⟩ => none_ne_some ((issue_unsigned s unsigned).symm.trans h)

/-- **A configuration whose credential is not the epoch has no issuing move.** -/
theorem stale_no_issue {s : State} (stale : s.credential ≠ s.epoch) :
    ¬ Enabled installation s .issue :=
  fun ⟨_, h⟩ => none_ne_some ((issue_stale s stale).symm.trans h)

/-- **An undelivered configuration has no enacting move.** -/
theorem undelivered_no_enact {s : State} (undelivered : s.delivered = false) :
    ¬ Enabled installation s .enact :=
  fun ⟨_, h⟩ => none_ne_some ((enact_undelivered s undelivered).symm.trans h)

/-- **A configuration whose credential is no longer the epoch has no enacting move.** -/
theorem revoked_no_enact {s : State} (revoked : s.credential ≠ s.epoch) :
    ¬ Enabled installation s .enact :=
  fun ⟨_, h⟩ => none_ne_some ((enact_revoked s revoked).symm.trans h)

/-! ## The reserve and what is drawn are conserved -/

/-- A step that draws and then sets other fields keeps what the draw keeps. -/
theorem draws_then {s t : State} {c d : Nat} {f : State → State}
    (keeps : ∀ u, (f u).reserve = u.reserve ∧ (f u).drawn = u.drawn ∧ (f u).time = u.time ∧
      (f u).deadline = u.deadline)
    (h : (draw c d s >>= fun u => some (f u)) = some t) :
    t.reserve + t.drawn = s.reserve + s.drawn ∧ t.time ≤ t.deadline :=
  match bind_eq_some.mp h with
  | ⟨u, drew, e⟩ =>
    have e' : f u = t := Option.some.inj e
    match draw_conserves drew, keeps u with
    | ⟨sum, timely⟩, ⟨r, dr, tm, dl⟩ =>
      e' ▸ ⟨r.symm ▸ dr.symm ▸ sum, tm.symm ▸ dl.symm ▸ timely⟩

theorem issue_conserves {s t : State} (h : issue s = some t) :
    t.reserve + t.drawn = s.reserve + s.drawn ∧ t.time ≤ t.deadline := by
  unfold issue at h
  by_cases c : (s.signed && (s.credential == s.epoch)) = true
  · rw [if_pos c] at h
    exact draws_then (f := fun u => {u with issued := true}) (fun _ => ⟨rfl, rfl, rfl, rfl⟩) h
  · rw [if_neg c] at h
    exact nomatch h

theorem deliver_conserves {r : Bool} {s t : State} (h : deliver r s = some t) :
    t.reserve + t.drawn = s.reserve + s.drawn ∧ t.time ≤ t.deadline := by
  unfold deliver at h
  by_cases c : (s.issued && (r == s.openRoute)) = true
  · rw [if_pos c] at h
    exact draws_then (f := fun u => {u with delivered := true}) (fun _ => ⟨rfl, rfl, rfl, rfl⟩) h
  · rw [if_neg c] at h
    exact nomatch h

theorem enact_conserves {s t : State} (h : enact s = some t) :
    t.reserve + t.drawn = s.reserve + s.drawn ∧ t.time ≤ t.deadline := by
  unfold enact at h
  by_cases c : (s.delivered && s.signed && (s.credential == s.epoch)) = true
  · rw [if_pos c] at h
    exact draws_then (f := fun u => {u with
                           completed := true
                           running := s.requested != .shutdown
                           generation := s.generation + if s.requested == .replace then 1 else 0
                           version := s.version + if s.requested == .update then 1 else 0}) (fun _ => ⟨rfl, rfl, rfl, rfl⟩) h
  · rw [if_neg c] at h
    exact nomatch h

/-- **Every move leaves the configuration as it is or draws**, keeping the reserve plus what is
drawn, and time within the deadline where it draws. -/
theorem move_draws : ∀ (m : Move) {s t : State}, installation.step s m t →
    t = s ∨ (t.reserve + t.drawn = s.reserve + s.drawn ∧ t.time ≤ t.deadline)
  | .probe .none _, _, _, h => .inl (congrArg Prod.snd (Option.some.inj h)).symm
  | .probe .route _, s, t, h => .inr (match bind_eq_some.mp (show (draw 1 1 s >>= fun u =>
        some (s.openRoute, u)) = some _ from h) with
      | ⟨u, drew, e⟩ =>
        have same : u = t := congrArg Prod.snd (Option.some.inj e)
        same ▸ draw_conserves drew)
  | .probe .slow _, s, t, h => .inr (match bind_eq_some.mp (show (draw 1 3 s >>= fun u =>
        some (s.openRoute, u)) = some _ from h) with
      | ⟨u, drew, e⟩ =>
        have same : u = t := congrArg Prod.snd (Option.some.inj e)
        same ▸ draw_conserves drew)
  | .issue, _, _, h => .inr (issue_conserves h)
  | .deliver _, _, _, h => .inr (deliver_conserves h)
  | .enact, _, _, h => .inr (enact_conserves h)

/-- **The reserve plus what is drawn is invariant under every move.** -/
theorem conserved_invariant (c : Nat) :
    Invariant installation (fun s => s.reserve + s.drawn = c) :=
  fun _ _ _ step held => match move_draws _ step with
    | .inl same => same ▸ held
    | .inr ⟨sum, _⟩ => sum.trans held

/-- **Every trace ends with the reserve plus what is drawn with which it began.** -/
theorem conserved_trace {s t : State} {ms : List Move} (tr : Trace installation s ms t) :
    t.reserve + t.drawn = s.reserve + s.drawn :=
  (conserved_invariant (s.reserve + s.drawn)).trace tr rfl

/-- **The protocol completes as a trace where its conditions hold.** -/
theorem protocol_completes (s : State) (r : Bool)
    (signed : s.signed = true) (current : s.credential = s.epoch)
    (route : r = s.openRoute) (stocked : 3 ≤ s.reserve) (timely : s.time + 3 ≤ s.deadline) :
    ∃ t, Trace installation s (protocolMoves r) t ∧ t.completed = true ∧ t.delivered = true ∧
      t.issued = true ∧ t.reserve + 3 = s.reserve ∧ t.time = s.time + 3 ∧
      t.drawn = s.drawn + 3 ∧ t.epoch = s.epoch :=
  match protocol_exact s r signed current route stocked timely with
  | ⟨t, h, rest⟩ => ⟨t, (protocol_iff r s t).mp h, rest⟩

/-! ## Computed cases as runs -/

/-- **Where the route is unknown, the route inquiry is selected.** -/
theorem unknown_route_probes :
    choose interface [start false .update 4 4, start true .update 4 4] plans =
      some ⟨.route, false, true⟩ := by decide

/-- **Where the route is known open, the plan without inquiry is selected.** -/
theorem known_route_no_probe :
    choose interface [start true .update 3 3] plans = some ⟨.none, true, false⟩ := by decide

/-- **Paths from each configuration are not a uniform plan.** -/
theorem statewise_not_uniform_run :
    (protocol false (start false .update 3 3)).isSome = true ∧
    (protocol true (start true .update 3 3)).isSome = true ∧
    choose interface [start false .update 3 3, start true .update 3 3] plans = none := by decide

/-- **A timely inquiry keeps the correction possible.** -/
theorem timely_run : (run interface ⟨.route, false, true⟩ (start true .update 4 4)).isSome = true := by
  decide

/-- **An equally accurate but slow inquiry misses the deadline.** -/
theorem late_probe_no_run : run interface ⟨.slow, false, true⟩ (start true .update 4 4) = none := by
  decide

/-- **Shutdown completes, stops the installation and draws the reserve.** -/
theorem shutdown_run :
    (run interface ⟨.route, false, true⟩ (start true .shutdown 4 4)).map
      (fun s => (s.completed, s.running, s.reserve, s.drawn)) = some (true, false, 0, 4) := by
  decide

/-- **Replacement completes and advances the generation.** -/
theorem replacement_run :
    (run interface ⟨.route, false, true⟩ (start false .replace 4 4)).map
      (fun s => (s.completed, s.generation, s.version)) = some (true, 1, 0) := by decide

/-- **Update completes and advances the version.** -/
theorem update_run :
    (run interface ⟨.route, false, true⟩ (start true .update 4 4)).map
      (fun s => (s.completed, s.generation, s.version)) = some (true, 0, 1) := by decide

/-- **A plan selected from a model omitting the open route fails where the route is open.** -/
theorem omitted_route_fails_run :
    choose interface [start false .update 3 3] plans = some ⟨.none, false, false⟩ ∧
    run interface ⟨.none, false, false⟩ (start true .update 3 3) = none := by decide

/-! ## Computed cases as traces -/

/-- **Where the route is unknown, the route inquiry is selected and has a completed trace from
the configurations with closed and with open route.** -/
theorem route_inquiry_completes_both :
    choose interface [start false .update 4 4, start true .update 4 4] plans =
        some ⟨.route, false, true⟩ ∧
      ∀ s, s ∈ [start false .update 4 4, start true .update 4 4] →
        ∃ o u, Trace installation s (planMoves ⟨.route, false, true⟩ o) u ∧ u.completed = true :=
  ⟨unknown_route_probes, chosen_completes unknown_route_probes⟩

/-- **Where the route is known open, the plan without inquiry has a completed trace.** -/
theorem known_route_completes :
    ∃ o u, Trace installation (start true .update 3 3) (planMoves ⟨.none, true, false⟩ o) u ∧
      u.completed = true :=
  chosen_completes known_route_no_probe _ (.head _)

/-- **From each of two configurations the protocol has a trace on its own route, yet no plan of
the repertoire has a completed trace from both.** -/
theorem statewise_not_uniform :
    (∃ t, Trace installation (start false .update 3 3) (protocolMoves false) t) ∧
    (∃ t, Trace installation (start true .update 3 3) (protocolMoves true) t) ∧
    ∀ p, p ∈ plans →
      ¬ ((∃ o u, Trace installation (start false .update 3 3) (planMoves p o) u ∧
            u.completed = true) ∧
          ∃ o u, Trace installation (start true .update 3 3) (planMoves p o) u ∧
            u.completed = true) :=
  match statewise_not_uniform_run with
  | ⟨first, second, absent⟩ =>
    ⟨match isSome_iff.mp first with | ⟨t, h⟩ => ⟨t, (protocol_iff _ _ _).mp h⟩,
     match isSome_iff.mp second with | ⟨t, h⟩ => ⟨t, (protocol_iff _ _ _).mp h⟩,
     none_chosen absent⟩

/-- **A plan selected from a model omitting the open route has a completed trace from the
configuration it models and no trace from the configuration it omits.** -/
theorem omitted_route_fails :
    (∃ o u, Trace installation (start false .update 3 3) (planMoves ⟨.none, false, false⟩ o) u ∧
      u.completed = true) ∧
    ¬ ∃ o u, Trace installation (start true .update 3 3) (planMoves ⟨.none, false, false⟩ o) u :=
  match omitted_route_fails_run with
  | ⟨chosen, fails⟩ =>
    ⟨chosen_completes chosen _ (.head _),
     fun ⟨o, u, tr⟩ => none_ne_some (fails.symm.trans ((run_iff _ _ u).mpr ⟨o, tr⟩))⟩

/-- **With the reserve and time given, the route inquiry has a trace.** -/
theorem timely_trace :
    ∃ o u, Trace installation (start true .update 4 4) (planMoves ⟨.route, false, true⟩ o) u :=
  match isSome_iff.mp timely_run with
  | ⟨u, h⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr⟩

/-- **With the same reserve and time, the slow inquiry has no trace.** -/
theorem late_no_trace :
    ¬ ∃ o u, Trace installation (start true .update 4 4) (planMoves ⟨.slow, false, true⟩ o) u :=
  fun ⟨o, u, tr⟩ => none_ne_some (late_probe_no_run.symm.trans ((run_iff _ _ u).mpr ⟨o, tr⟩))

/-- **For the shutdown request, the route inquiry has a trace ending completed, with the
installation stopped and its reserve of four drawn.** -/
theorem shutdown_trace :
    ∃ o u, Trace installation (start true .shutdown 4 4) (planMoves ⟨.route, false, true⟩ o) u ∧
      u.completed = true ∧ u.running = false ∧ u.reserve = 0 ∧ u.drawn = 4 :=
  match map_eq_some.mp shutdown_run with
  | ⟨u, h, values⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr, congrArg Prod.fst values, congrArg (fun x => x.2.1) values,
        congrArg (fun x => x.2.2.1) values, congrArg (fun x => x.2.2.2) values⟩

/-- **For the replacement request, the route inquiry has a trace ending completed with the
generation advanced by one and the version unchanged.** -/
theorem replacement_trace :
    ∃ o u, Trace installation (start false .replace 4 4) (planMoves ⟨.route, false, true⟩ o) u ∧
      u.completed = true ∧ u.generation = 1 ∧ u.version = 0 :=
  match map_eq_some.mp replacement_run with
  | ⟨u, h, values⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr, congrArg Prod.fst values, congrArg (fun x => x.2.1) values,
        congrArg (fun x => x.2.2) values⟩

/-- **For the update request, the route inquiry has a trace ending completed with the version
advanced by one and the generation unchanged.** -/
theorem update_trace :
    ∃ o u, Trace installation (start true .update 4 4) (planMoves ⟨.route, false, true⟩ o) u ∧
      u.completed = true ∧ u.generation = 0 ∧ u.version = 1 :=
  match map_eq_some.mp update_run with
  | ⟨u, h, values⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr, congrArg Prod.fst values, congrArg (fun x => x.2.1) values,
        congrArg (fun x => x.2.2) values⟩

end Actuation

end Becoming
