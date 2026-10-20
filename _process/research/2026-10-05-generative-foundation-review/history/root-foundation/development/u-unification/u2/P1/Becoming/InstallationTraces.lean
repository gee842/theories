import Becoming.Frame
import EffectiveCommand

/-!
# The installation of `EffectiveCommand` as a process: its courses are traces

`EffectiveCommand` models one installation whose recognition, delivery and actuation are
consecutive changes of one state: an inquiry (`probe`) answers a question about the route and may
spend reserve and time, and the protocol issues, delivers along a route and enacts
(`issue`, `deliver`, `enact`), each step failing (`none`) where its conditions do not hold. Its
interface runs a plan, an inquiry followed by the protocol on the route the answer selects
(`AlignmentInquiry.run`), and selects the first plan of a repertoire that completes from every
listed configuration (`AlignmentInquiry.choose`). The module's results are facts about runs from
named starting configurations, checked by evaluation.

The reading used here: the installation's moves are a process of the spine (`installation`), a
move from `s` to `t` being an inquiry with its answer, an issue, a delivery along a route or an
enactment that takes `s` to `t`. This reading is exact:

* **The protocol is a trace.** The protocol on a route takes `s` to `t` exactly when the
  installation has a trace from `s` to `t` issuing, delivering along that route and enacting
  (`protocol_iff`). Running a plan from `s` ends at `u` exactly when the installation has a trace
  from `s` to `u` along the plan's inquiry with some answer, followed by the protocol on the route
  that answer selects (`run_iff`), and the plan completes from `s` exactly when such a trace ends
  at a completed configuration (`passes_iff`).
* **Choosing a plan.** A plan selected for a list of configurations has, from every one of them, a
  trace ending completed (`chosen_completes`); where no plan is selected, no plan of the
  repertoire has such a trace from every listed configuration (`none_chosen`).

Every fact of the module is then a fact about the installation's traces:

* **Inquiry where the route is unknown.** From the configurations with closed and with open route,
  the route inquiry is the plan selected, and it has a completed trace from both
  (`route_inquiry_completes_both`); where the route is known open, the plan without inquiry has one
  (`known_route_completes`).
* **Paths from each configuration are not a uniform plan.** From each of two configurations a
  trace of the protocol exists on its own route, yet no plan of the repertoire has a completed
  trace from both (`statewise_not_uniform`). A plan selected from a model omitting the open route
  has a completed trace from the configuration it models and no trace at all from the one it
  omits (`omitted_route_fails`).
* **Timing.** With the reserve and time given, the route inquiry has a trace (`timely_trace`) and
  the slow inquiry has none (`late_no_trace`).
* **What enactment does.** The route inquiry has a trace ending completed with the installation
  stopped and its reserve spent, for the shutdown request (`shutdown_trace`), and ending
  completed with the generation or the version advanced by one, for replacement
  (`replacement_trace`) and update (`update_trace`).

The module's lemmas of the installation's single steps (`spend_conserves`, `protocol_exact` and the
failures of `issue` and `enact`) use `propext`; they are stated of the installation's process in
`InstallationTracesInherited`. No ethical predicate,
ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace InstallationTraces

/-! ## Options, lists and truth values -/

/-- A bound option is present exactly when the first is present and the continuation from it is. -/
theorem bind_eq_some {α β : Type} (o : Option α) (f : α → Option β) (b : β) :
    (o >>= f) = some b ↔ ∃ a, o = some a ∧ f a = some b :=
  match o with
  | none => ⟨fun h => (nomatch h), fun ⟨_, h, _⟩ => (nomatch h)⟩
  | some a => ⟨fun h => ⟨a, rfl, h⟩, fun ⟨_, h, h'⟩ => by cases Option.some.inj h; exact h'⟩

/-- A mapped option is present only where the option is. -/
theorem map_eq_some {α β : Type} {f : α → β} {b : β} :
    ∀ {o : Option α}, o.map f = some b → ∃ a, o = some a ∧ f a = b
  | none, h => nomatch h
  | some a, h => ⟨a, rfl, Option.some.inj h⟩

/-- A present option is some value. -/
theorem some_of_isSome {α : Type} : ∀ {o : Option α}, o.isSome = true → ∃ a, o = some a
  | some a, _ => ⟨a, rfl⟩
  | none, h => Bool.noConfusion h

/-- An option holds a value meeting a test exactly when it is that value and the value meets it. -/
theorem any_eq_true {α : Type} (f : α → Bool) :
    ∀ o : Option α, o.any f = true ↔ ∃ a, o = some a ∧ f a = true
  | none => ⟨fun h => Bool.noConfusion h, fun ⟨_, h, _⟩ => (nomatch h)⟩
  | some a => ⟨fun h => ⟨a, rfl, h⟩, fun ⟨_, h, h'⟩ => by cases Option.some.inj h; exact h'⟩

theorem and_left : ∀ {a b : Bool}, (a && b) = true → a = true
  | true, _, _ => rfl
  | false, _, h => h

theorem and_right : ∀ {a b : Bool}, (a && b) = true → b = true
  | true, _, h => h
  | false, _, h => Bool.noConfusion h

/-- Every member of a list all of whose members meet a test meets it. -/
theorem all_mem {α : Type} {f : α → Bool} : ∀ {l : List α}, l.all f = true → ∀ x, x ∈ l → f x = true
  | [], _, _, m => nomatch m
  | _ :: _, h, _, .head _ => and_left h
  | _ :: _, h, x, .tail _ m => all_mem (and_right h) x m

/-- What a search finds meets the test searched for. -/
theorem find_some {α : Type} {p : α → Bool} : ∀ {l : List α} {a : α}, l.find? p = some a → p a = true
  | [], _, h => nomatch h
  | b :: l, _, h =>
    have h' : (match p b with | true => some b | false => l.find? p) = _ := h
    match hb : p b, h' with
    | true, h' => (Option.some.inj h') ▸ hb
    | false, h' => find_some h'

/-- Where a search finds nothing, no member meets the test. -/
theorem find_none {α : Type} {p : α → Bool} : ∀ {l : List α}, l.find? p = none → ∀ x, x ∈ l → p x = false
  | [], _, _, m => nomatch m
  | b :: l, h, _, .head _ =>
    have h' : (match p b with | true => some b | false => l.find? p) = none := h
    match p b, h' with
    | true, h' => nomatch h'
    | false, _ => rfl
  | b :: l, h, x, .tail _ m =>
    have h' : (match p b with | true => some b | false => l.find? p) = none := h
    match p b, h' with
    | true, h' => nomatch h'
    | false, h' => find_none h' x m

/-- An absent option is no value. -/
theorem none_ne_some {α : Type} {a : α} : (none : Option α) ≠ some a := fun e => nomatch e

/-! ## The installation as a process -/

/-- The installation's moves: an inquiry with its answer, issuing, delivering along a route, and
enacting. -/
inductive Move where
  | probe (q : EffectiveCommand.Query) (answer : Bool)
  | issue
  | deliver (route : Bool)
  | enact

/-- **The installation as a process**: each move takes a configuration to what the installation's
step of that move gives. -/
def installation : Process EffectiveCommand.State Move where
  step s m t := match m with
    | .probe q o => EffectiveCommand.probe s q = some (o, t)
    | .issue => EffectiveCommand.issue s = some t
    | .deliver r => EffectiveCommand.deliver r s = some t
    | .enact => EffectiveCommand.enact s = some t

/-- The protocol's moves on a route. -/
def protocolMoves (r : Bool) : List Move := [.issue, .deliver r, .enact]

/-- A plan's moves with a given answer: its inquiry, then the protocol on the route the answer
selects. -/
def planMoves (p : AlignmentInquiry.Plan EffectiveCommand.Query Bool) (o : Bool) : List Move :=
  .probe p.query o :: protocolMoves (AlignmentInquiry.branch p o)

/-- **The protocol on a route takes `s` to `t` exactly when the installation has a trace from `s`
to `t` issuing, delivering along that route and enacting.** -/
theorem protocol_iff (r : Bool) (s t : EffectiveCommand.State) :
    EffectiveCommand.protocol r s = some t ↔ Trace installation s (protocolMoves r) t :=
  ⟨fun h =>
    match (bind_eq_some _ _ _).mp h with
    | ⟨_, h12, h3⟩ => match (bind_eq_some _ _ _).mp h12 with
      | ⟨_, h1, h2⟩ => .cons h1 (.cons h2 (.cons h3 (.nil t))),
   fun tr =>
    match trace_cons_iff.mp tr with
    | ⟨_, h1, tr⟩ => match trace_cons_iff.mp tr with
      | ⟨_, h2, tr⟩ => match trace_cons_iff.mp tr with
        | ⟨_, h3, tr⟩ => (bind_eq_some _ _ _).mpr ⟨_, (bind_eq_some _ _ _).mpr ⟨_, h1, h2⟩,
            (trace_nil_iff.mp tr) ▸ h3⟩⟩

/-- **Running a plan from `s` ends at `u` exactly when the installation has a trace from `s` to `u`
along the plan's inquiry with some answer, then the protocol on the route that answer selects.** -/
theorem run_iff (p : AlignmentInquiry.Plan EffectiveCommand.Query Bool) (s u : EffectiveCommand.State) :
    AlignmentInquiry.run EffectiveCommand.interface p s = some u ↔
      ∃ o, Trace installation s (planMoves p o) u :=
  ⟨fun h =>
    match (bind_eq_some _ _ _).mp h with
    | ⟨(o, _), probed, rest⟩ => ⟨o, .cons probed ((protocol_iff _ _ _).mp rest)⟩,
   fun ⟨o, tr⟩ =>
    match trace_cons_iff.mp tr with
    | ⟨m, probed, rest⟩ => (bind_eq_some _ _ _).mpr ⟨(o, m), probed, (protocol_iff _ _ _).mpr rest⟩⟩

/-- **A plan completes from `s` exactly when the installation has a trace along it from `s` ending
at a completed configuration.** -/
theorem passes_iff (p : AlignmentInquiry.Plan EffectiveCommand.Query Bool) (s : EffectiveCommand.State) :
    AlignmentInquiry.passes EffectiveCommand.interface p s = true ↔
      ∃ o u, Trace installation s (planMoves p o) u ∧ u.completed = true :=
  ⟨fun h => match (any_eq_true _ _).mp h with
    | ⟨u, ran, done⟩ => match (run_iff p s u).mp ran with
      | ⟨o, tr⟩ => ⟨o, u, tr, done⟩,
   fun ⟨o, u, tr, done⟩ => (any_eq_true _ _).mpr ⟨u, (run_iff p s u).mpr ⟨o, tr⟩, done⟩⟩

/-- **A plan selected for a list of configurations has, from every one of them, a trace of the
installation ending completed.** -/
theorem chosen_completes {states : List EffectiveCommand.State}
    {plans : List (AlignmentInquiry.Plan EffectiveCommand.Query Bool)}
    {p : AlignmentInquiry.Plan EffectiveCommand.Query Bool}
    (chosen : AlignmentInquiry.choose EffectiveCommand.interface states plans = some p) :
    ∀ s, s ∈ states → ∃ o u, Trace installation s (planMoves p o) u ∧ u.completed = true :=
  have valid : (!states.isEmpty && states.all (AlignmentInquiry.passes EffectiveCommand.interface p)) =
      true := find_some (p := AlignmentInquiry.valid EffectiveCommand.interface states) chosen
  fun s member => (passes_iff p s).mp (all_mem (and_right valid) s member)

/-- **Where no plan is selected for two configurations, no plan of the repertoire has a completed
trace of the installation from both.** -/
theorem none_chosen {s₁ s₂ : EffectiveCommand.State}
    {plans : List (AlignmentInquiry.Plan EffectiveCommand.Query Bool)}
    (absent : AlignmentInquiry.choose EffectiveCommand.interface [s₁, s₂] plans = none) :
    ∀ p, p ∈ plans →
      ¬ ((∃ o u, Trace installation s₁ (planMoves p o) u ∧ u.completed = true) ∧
        ∃ o u, Trace installation s₂ (planMoves p o) u ∧ u.completed = true) :=
  fun p member ⟨first, second⟩ =>
    have one := (passes_iff p s₁).mpr first
    have two := (passes_iff p s₂).mpr second
    have valid : AlignmentInquiry.valid EffectiveCommand.interface [s₁, s₂] p = true := by
      show (true && (AlignmentInquiry.passes EffectiveCommand.interface p s₁ &&
        (AlignmentInquiry.passes EffectiveCommand.interface p s₂ && true))) = true
      rw [one, two]
      exact rfl
    Bool.noConfusion ((find_none absent p member).symm.trans valid)

/-! ## The installation's facts as facts of its traces -/

open EffectiveCommand AlignmentInquiry in
/-- **Where the route is unknown, the route inquiry is the plan selected, and it has a completed
trace from the configurations with closed and with open route.** -/
theorem route_inquiry_completes_both :
    choose interface [start false .update 4 4, start true .update 4 4] plans =
        some ⟨.route, false, true⟩ ∧
      ∀ s, s ∈ [start false .update 4 4, start true .update 4 4] →
        ∃ o u, Trace installation s (planMoves ⟨.route, false, true⟩ o) u ∧ u.completed = true :=
  ⟨unknown_route_selects_inquiry, chosen_completes unknown_route_selects_inquiry⟩

open EffectiveCommand in
/-- **Where the route is known open, the plan without inquiry is selected and has a completed
trace.** -/
theorem known_route_completes :
    ∃ o u, Trace installation (start true .update 3 3) (planMoves ⟨.none, true, false⟩ o) u ∧
      u.completed = true :=
  chosen_completes known_route_needs_no_probe _ (.head _)

open EffectiveCommand in
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
  match sufficient_statewise_paths_not_uniform with
  | ⟨first, second, absent⟩ =>
    ⟨match some_of_isSome first with | ⟨t, h⟩ => ⟨t, (protocol_iff _ _ _).mp h⟩,
     match some_of_isSome second with | ⟨t, h⟩ => ⟨t, (protocol_iff _ _ _).mp h⟩,
     none_chosen absent⟩

open EffectiveCommand in
/-- **A plan selected from a model omitting the open route has a completed trace from the
configuration it models and no trace from the configuration it omits.** -/
theorem omitted_route_fails :
    (∃ o u, Trace installation (start false .update 3 3) (planMoves ⟨.none, false, false⟩ o) u ∧
      u.completed = true) ∧
    ¬ ∃ o u, Trace installation (start true .update 3 3) (planMoves ⟨.none, false, false⟩ o) u :=
  match omitted_route_model_can_fail with
  | ⟨chosen, fails⟩ =>
    ⟨chosen_completes chosen _ (.head _),
     fun ⟨o, u, tr⟩ => none_ne_some (fails.symm.trans ((run_iff _ _ u).mpr ⟨o, tr⟩))⟩

open EffectiveCommand in
/-- **With the reserve and time given, the route inquiry has a trace.** -/
theorem timely_trace :
    ∃ o u, Trace installation (start true .update 4 4) (planMoves ⟨.route, false, true⟩ o) u :=
  match some_of_isSome timely_inquiry_retains_correction with
  | ⟨u, h⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr⟩

open EffectiveCommand in
/-- **With the same reserve and time, the slow inquiry has no trace.** -/
theorem late_no_trace :
    ¬ ∃ o u, Trace installation (start true .update 4 4) (planMoves ⟨.slow, false, true⟩ o) u :=
  fun ⟨o, u, tr⟩ =>
    none_ne_some (accurate_but_late_probe_fails.symm.trans ((run_iff _ _ u).mpr ⟨o, tr⟩))

open EffectiveCommand in
/-- **For the shutdown request, the route inquiry has a trace ending completed, with the
installation stopped and its reserve of four spent.** -/
theorem shutdown_trace :
    ∃ o u, Trace installation (start true .shutdown 4 4) (planMoves ⟨.route, false, true⟩ o) u ∧
      u.completed = true ∧ u.running = false ∧ u.reserve = 0 ∧ u.spent = 4 :=
  match map_eq_some actual_shutdown_completes with
  | ⟨u, h, values⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr, congrArg Prod.fst values, congrArg (fun x => x.2.1) values,
        congrArg (fun x => x.2.2.1) values, congrArg (fun x => x.2.2.2) values⟩

open EffectiveCommand in
/-- **For the replacement request, the route inquiry has a trace ending completed with the
generation advanced by one and the version unchanged.** -/
theorem replacement_trace :
    ∃ o u, Trace installation (start false .replace 4 4) (planMoves ⟨.route, false, true⟩ o) u ∧
      u.completed = true ∧ u.generation = 1 ∧ u.version = 0 :=
  match map_eq_some actual_replacement_completes with
  | ⟨u, h, values⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr, congrArg Prod.fst values, congrArg (fun x => x.2.1) values,
        congrArg (fun x => x.2.2) values⟩

open EffectiveCommand in
/-- **For the update request, the route inquiry has a trace ending completed with the version
advanced by one and the generation unchanged.** -/
theorem update_trace :
    ∃ o u, Trace installation (start true .update 4 4) (planMoves ⟨.route, false, true⟩ o) u ∧
      u.completed = true ∧ u.generation = 0 ∧ u.version = 1 :=
  match map_eq_some actual_update_completes with
  | ⟨u, h, values⟩ => match (run_iff _ _ u).mp h with
    | ⟨o, tr⟩ => ⟨o, u, tr, congrArg Prod.fst values, congrArg (fun x => x.2.1) values,
        congrArg (fun x => x.2.2) values⟩

end InstallationTraces

end Becoming
