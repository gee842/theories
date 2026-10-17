import GenerativeCore
import Becoming.Frame
import FallibleInspection

/-!
# Inspection as a process: the fallible witnesses of `FallibleInspection`, inherited

`FallibleInspection.inspect` revises a situation of `EvidenceQualifiedCorrection` by the reports
of fallible witnesses: where queries are allowed and the reserve covers one unit per witness, it
keeps the candidate models some admitted fault set explains (`posterior`) and charges the
inspection; `EvidenceQualifiedCorrection.respond` then executes over the candidates' pooled
envelope, and `FallibleInspection.run` is the two in turn. Both are transitions of one process
of the core on situations, for the roster with or without the fifth witness: an action is a
transcript of reports, whose step goes to the situation `inspect` gives, or the response, whose
step goes to the situation `respond` gives (`audit`). The definitions have non-empty axiom
reports, so this module is in the periphery-join ring.

* **What an inspection step does.** It keeps the actual model and keeps exactly the candidates the
  reports leave compatible (`inspect_some`); a response step keeps both.
* **Candidates only narrow along every run** (`candidates_narrow`, through
  `FallibleInspection.joint_refinement_subset`).
* **Faithful reports keep the actual model.** An inspection step whose reports are faithful
  outside an admitted fault set of the actual model keeps it among the candidates
  (`step_keeps_actual`, through `inspection_keeps_actual_under_admitted_faults`); after such a
  step a certificate accepted over the candidates' pooled envelope is sound for the actual
  arrangement (`step_pool_sound`, through `refined_pool_remains_sound`), and where that envelope
  is separated, faithful responses complete the guarded execution within the mandate
  (`step_then_completes`, through `jointly_inspected_completion`).
* **The module's runs as traces.** The run of `FallibleInspection` is exactly the trace of the
  inspection and the response (`trace_iff_run`), so its outcome is the end of every such trace
  (`outcome_of_trace`). The computed cases are laws of those traces: with the fifth witness the
  shutdown completes (`extended_trace_completes`), with four witnesses the correction stays
  uncertified (`four_witness_trace_uncertified`), and diagnostic success still needs the reserve
  to respond (`extended_trace_short_of_reserve`).
* **Denied inspection is no trace.** From a situation that allows no query there is no
  inspection step followed by a response (`denied_no_trace`, through
  `denied_inspection_does_not_collect_or_execute`).

No ethical predicate or ranking occurs. The module adds no axiom of its own; it inherits
`propext` from `EvidenceQualifiedCorrection.respond`, from `FallibleInspection.run`, `outcome`
and every theorem it uses, `Quot.sound` from `inspection_keeps_actual_under_admitted_faults`,
`refined_pool_remains_sound` and `jointly_inspected_completion`, and `Classical.choice` from
`jointly_inspected_completion`.
-/

namespace Becoming

open Generative FaultTolerantCorrection CorrectionReconfiguration EvidenceQualifiedCorrection
  FallibleInspection

namespace InspectionProcessesInherited

/-- The audit process, for the roster with (`extended`) or without the fifth witness: a
transcript of reports steps to the situation `inspect` gives, the response to the situation
`respond` gives. -/
def audit (extended : Bool) : Process Situation (Option Reports) :=
  ⟨fun s m t => match m with
    | some reports => ∃ c, inspect extended reports s = some c ∧ c.situation = t
    | none => respond s () = some t⟩

/-- **An inspection step keeps the actual model and the compatible candidates.** -/
theorem inspect_some {extended : Bool} {reports : Reports} {s : Situation} {c : Audited}
    (h : inspect extended reports s = some c) :
    c.situation.actual = s.actual ∧
      c.situation.candidates = posterior extended s.candidates reports := by
  unfold inspect at h
  cases hc : !s.queryAllowed with
  | true => rw [hc] at h; exact nomatch h
  | false =>
    rw [hc] at h
    dsimp only at h
    cases hp : EffectiveCommand.spend (auditRoster extended).length (auditRoster extended).length
        s.installation.state with
    | none => rw [hp] at h; exact nomatch h
    | some paid =>
      rw [hp] at h
      have e := congrArg Audited.situation (Option.some.inj h)
      exact ⟨(congrArg Situation.actual e).symm, (congrArg Situation.candidates e).symm⟩

/-- **An inspection step to `t` leaves the candidates the reports leave compatible.** -/
theorem step_candidates {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) :
    t.candidates = posterior extended s.candidates reports :=
  match step with
  | ⟨_, h, same⟩ => Eq.subst (motive := fun x : Situation =>
      x.candidates = posterior extended s.candidates reports) same (inspect_some h).2

/-- A step of the audit keeps only former candidates. -/
theorem step_narrows {extended : Bool} {s t : Situation} :
    ∀ {m : Option Reports}, (audit extended).step s m t → ∀ h ∈ t.candidates, h ∈ s.candidates
  | some _, step, x, member =>
      joint_refinement_subset _ _ _ _ _ x
        (Eq.subst (motive := fun l => x ∈ l) (step_candidates step) member)
  | none, h, x, member => Eq.subst (motive := fun l => x ∈ l)
      (congrArg Situation.candidates (Option.some.inj h)).symm member

/-- **Candidates only narrow along every run of the audit.** -/
theorem candidates_narrow {extended : Bool} (r : Run (audit extended)) (n : Nat) :
    ∀ h ∈ (r.state (n + 1)).candidates, h ∈ (r.state n).candidates :=
  step_narrows (r.step n)

/-- **Faithful reports keep the actual model.** An inspection step whose reports agree with the
actual model's diagnostic answer, or are missing, at every witness outside an admitted fault set
of the actual model, keeps the actual model and keeps it among the candidates. -/
theorem step_keeps_actual {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) (known : s.actual ∈ s.candidates)
    (bad : List Domain) (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d ∈ auditRoster extended, d ∉ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual)) :
    t.actual = s.actual ∧ t.actual ∈ t.candidates :=
  match step with
  | ⟨c, h, same⟩ =>
      Eq.subst (motive := fun x : Situation => x.actual = s.actual ∧ x.actual ∈ x.candidates) same
        (match inspection_keeps_actual_under_admitted_faults extended reports s c known bad
            admitted faithful h with
          | ⟨kept, member, _⟩ => ⟨kept, member⟩)

/-- **After a faithful inspection step, an accepted pooled certificate is sound.** For any
description of the models by arrangements, after an inspection step whose reports are faithful
outside an admitted fault set of the actual model, a certificate accepted over the pooled
envelope of the candidates gives every claim that each working, supporting member of the actual
arrangement gives, for root faults that arrangement covers. -/
theorem step_pool_sound {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) (desc : Model → Arrangement)
    (known : s.actual ∈ s.candidates) (bad : List Domain)
    (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d ∈ auditRoster extended, d ∉ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual))
    (roots : List Nat) (covered : Covered (desc s.actual) roots) (supports : Domain → Bool)
    (P : Prop) (reliable : ∀ d ∈ (desc s.actual).roster,
      fails ((desc s.actual).vulnerability d) roots = false → supports d = true → P)
    (accepted : certificate (desc s.actual).roster (pooled desc t.candidates) supports = true) :
    P :=
  refined_pool_remains_sound (auditRoster extended) (auditFaults extended) diagnostic desc
    s.candidates s.actual known bad admitted reports faithful roots covered supports P reliable
    (Eq.subst (motive := fun l => certificate (desc s.actual).roster (pooled desc l) supports = true)
      (step_candidates step) accepted)

/-- **After a faithful inspection step, faithful responses complete.** For any description of the
models by arrangements, after an inspection step whose reports are faithful outside an admitted
fault set of the actual model, where the candidates' pooled envelope is separated on the actual
roster and an installation (the one left after paying for the inspection) holds a current
request, faithful, responsive readings and approvals of the members the actual root faults leave
working, with reserve and time for the response, the guarded execution over that envelope
succeeds, completes, and is within the mandate. -/
theorem step_then_completes {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) (desc : Model → Arrangement)
    (known : s.actual ∈ s.candidates) (bad : List Domain)
    (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d ∈ auditRoster extended, d ∉ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual))
    (roots : List Nat) (covered : Covered (desc s.actual) roots)
    (apart : separated (desc s.actual).roster (pooled desc t.candidates))
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (current : fresh w p = true)
    (readResponses : ∀ d ∈ (desc s.actual).roster,
      fails ((desc s.actual).vulnerability d) roots = false → reads d = some (expected p))
    (issueResponses : ∀ d ∈ (desc s.actual).roster,
      fails ((desc s.actual).vulnerability d) roots = false → approvals d = some p)
    (readFaithful : ∀ d ∈ (desc s.actual).roster,
      fails ((desc s.actual).vulnerability d) roots = false →
      ∀ o, reads d = some o → o = observed w p.address)
    (issueFaithful : ∀ d ∈ (desc s.actual).roster,
      fails ((desc s.actual).vulnerability d) roots = false →
      approvals d = some p → withinMandate w p = true)
    (funded : (desc s.actual).roster.length * (p.address.length + 2) + 3 ≤ w.state.reserve)
    (timely : w.state.time + (desc s.actual).roster.length * (p.address.length + 2) + 3 ≤
      w.state.deadline) :
    (guardedExecute (desc s.actual).roster (pooled desc t.candidates) (pooled desc t.candidates)
      w p reads approvals).succeeded = true ∧
    (guardedExecute (desc s.actual).roster (pooled desc t.candidates) (pooled desc t.candidates)
      w p reads approvals).installation.state.completed = true ∧
    withinMandate w p = true :=
  have e := step_candidates step
  Eq.subst (motive := fun l =>
      (guardedExecute (desc s.actual).roster (pooled desc l) (pooled desc l)
        w p reads approvals).succeeded = true ∧
      (guardedExecute (desc s.actual).roster (pooled desc l) (pooled desc l)
        w p reads approvals).installation.state.completed = true ∧
      withinMandate w p = true) e.symm
    (jointly_inspected_completion (auditRoster extended) (auditFaults extended) diagnostic desc
      s.candidates s.actual known bad admitted reports faithful roots covered
      (Eq.subst (motive := fun l => separated (desc s.actual).roster (pooled desc l)) e apart)
      w p reads approvals current readResponses issueResponses readFaithful issueFaithful funded
      timely)

/-- **Denied inspection is no trace.** From a situation that allows no query, no inspection step
is followed by a response step. -/
theorem denied_no_trace {extended : Bool} {reports : Reports} {s : Situation}
    (denied : s.queryAllowed = false) :
    ¬ ∃ t u, (audit extended).step s (some reports) t ∧ (audit extended).step t none u :=
  fun ⟨t, u, ⟨c, h, same⟩, responded⟩ =>
    have responded' : respond c.situation () = some u :=
      Eq.subst (motive := fun x => respond x () = some u) same.symm responded
    have ran : FallibleInspection.run extended reports s = some { c with situation := u } := by
      unfold FallibleInspection.run
      rw [h]
      show (respond c.situation () >>= fun result => pure ({ c with situation := result } : Audited))
        = _
      rw [responded']
      rfl
    nomatch (denied_inspection_does_not_collect_or_execute extended reports s denied).symm.trans ran

/-! ## The module's runs as traces -/

/-- Where inspection gives an audit, the run of `FallibleInspection` is the response from its
situation. -/
theorem run_inspected {extended : Bool} {reports : Reports} {s : Situation} {c : Audited}
    (h : inspect extended reports s = some c) :
    FallibleInspection.run extended reports s =
      (respond c.situation () >>= fun result => pure ({ c with situation := result } : Audited)) := by
  unfold FallibleInspection.run
  rw [h]
  rfl

/-- Where inspection gives no audit, there is no run. -/
theorem run_uninspected {extended : Bool} {reports : Reports} {s : Situation}
    (h : inspect extended reports s = none) : FallibleInspection.run extended reports s = none := by
  unfold FallibleInspection.run
  rw [h]
  rfl

/-- **The run of `FallibleInspection` is a trace.** Its run ends at a situation `u` exactly where
the inspection by the reports and then the response form a trace of the audit from `s` to `u`. -/
theorem trace_iff_run {extended : Bool} {reports : Reports} {s u : Situation} :
    Trace (audit extended) s [some reports, none] u ↔
      (FallibleInspection.run extended reports s).map Audited.situation = some u :=
  ⟨fun tr => match tr with
    | .cons ⟨c, h, same⟩ (.cons responded (.nil _)) =>
        (congrArg (Option.map Audited.situation) (run_inspected h)).trans
          (congrArg (fun o => Option.map Audited.situation
              (o >>= fun result => pure ({ c with situation := result } : Audited)))
            (Eq.subst (motive := fun x => respond x () = some u) same.symm responded)),
   fun h => by
    cases hi : inspect extended reports s with
    | none => rw [run_uninspected hi] at h; exact nomatch h
    | some c =>
      rw [run_inspected hi] at h
      cases hr : respond c.situation () with
      | none => rw [hr] at h; exact nomatch h
      | some v =>
        rw [hr] at h
        exact .cons (⟨c, hi, rfl⟩ : (audit extended).step s (some reports) c.situation)
          (.cons (hr.trans (congrArg some (Option.some.inj h))) (.nil u))⟩

/-- The outcome of the reports is the end of every trace of the inspection and the response. -/
theorem outcome_of_trace {extended : Bool} {reports : Reports} {s u : Situation}
    (tr : Trace (audit extended) s [some reports, none] u) : outcome extended reports s = u :=
  congrArg (fun o => Option.getD o s) (trace_iff_run.mp tr)

/-- Where the outcome differs from the start, the inspection and the response form a trace
ending there. -/
theorem trace_of_outcome_ne {extended : Bool} {reports : Reports} {s : Situation}
    (moved : outcome extended reports s ≠ s) :
    Trace (audit extended) s [some reports, none] (outcome extended reports s) :=
  match e : (FallibleInspection.run extended reports s).map Audited.situation with
  | some _ => Eq.subst (motive := fun x => Trace (audit extended) s [some reports, none] x)
      (congrArg (fun o => Option.getD o s) e).symm (trace_iff_run.mpr e)
  | none => absurd (congrArg (fun o => Option.getD o s) e) moved

/-- **With the fifth witness, fallible inspection then shutdown.** From the left model with root
fault 0 and reserve and deadline 16, inspection by the split reports on the five-witness roster
and the response form a trace, and every such trace ends with the left and swapped models as
candidates, the command achieved, 16 spent, reserve 0 and serial 1. -/
theorem extended_trace_completes :
    Trace (audit true) (initialSituation .left [0] 16 16) [some splitReports, none]
        (outcome true splitReports (initialSituation .left [0] 16 16)) ∧
      ∀ u, Trace (audit true) (initialSituation .left [0] 16 16) [some splitReports, none] u →
        u.candidates = [.left, .swapped] ∧ achieved u = true ∧
          u.installation.state.spent = 16 ∧ u.installation.state.reserve = 0 ∧
          u.installation.serial = 1 :=
  ⟨trace_of_outcome_ne (fun same =>
      nomatch (congrArg achieved same).symm.trans fallible_inspection_then_actual_shutdown.2.1),
   fun _ tr => Eq.subst (motive := fun x : Situation =>
      x.candidates = [.left, .swapped] ∧ achieved x = true ∧ x.installation.state.spent = 16 ∧
        x.installation.state.reserve = 0 ∧ x.installation.serial = 1)
    (outcome_of_trace tr) fallible_inspection_then_actual_shutdown⟩

/-- **Four witnesses leave the correction uncertified.** From the left model with reserve and
deadline 16, inspection by the split reports on the four-witness roster and the response form a
trace, and every such trace ends with all three models still candidates, the command not
achieved, and 12 spent. -/
theorem four_witness_trace_uncertified :
    Trace (audit false) (initialSituation .left [0] 16 16) [some splitReports, none]
        (outcome false splitReports (initialSituation .left [0] 16 16)) ∧
      ∀ u, Trace (audit false) (initialSituation .left [0] 16 16) [some splitReports, none] u →
        u.candidates = hypotheses ∧ achieved u = false ∧ u.installation.state.spent = 12 :=
  ⟨trace_of_outcome_ne (fun same => nomatch
      (congrArg (fun x : Situation => x.installation.state.spent) same).symm.trans
        inadequate_witnesses_leave_correction_uncertified.2.2),
   fun _ tr => Eq.subst (motive := fun x : Situation =>
      x.candidates = hypotheses ∧ achieved x = false ∧ x.installation.state.spent = 12)
    (outcome_of_trace tr) inadequate_witnesses_leave_correction_uncertified⟩

/-- **Diagnostic success still needs the reserve to respond.** From the left model with reserve
and deadline 15, inspection by the split reports on the five-witness roster and the response form
a trace, and every such trace ends with the left and swapped models as candidates but the command
not achieved, 13 spent and reserve 2. -/
theorem extended_trace_short_of_reserve :
    Trace (audit true) (initialSituation .left [0] 15 15) [some splitReports, none]
        (outcome true splitReports (initialSituation .left [0] 15 15)) ∧
      ∀ u, Trace (audit true) (initialSituation .left [0] 15 15) [some splitReports, none] u →
        u.candidates = [.left, .swapped] ∧ achieved u = false ∧
          u.installation.state.spent = 13 ∧ u.installation.state.reserve = 2 :=
  ⟨trace_of_outcome_ne (fun same => nomatch
      (congrArg (fun x : Situation => x.installation.state.spent) same).symm.trans
        diagnostic_success_still_requires_response_capacity.2.2.1),
   fun _ tr => Eq.subst (motive := fun x : Situation =>
      x.candidates = [.left, .swapped] ∧ achieved x = false ∧ x.installation.state.spent = 13 ∧
        x.installation.state.reserve = 2)
    (outcome_of_trace tr) diagnostic_success_still_requires_response_capacity⟩

end InspectionProcessesInherited

end Becoming
