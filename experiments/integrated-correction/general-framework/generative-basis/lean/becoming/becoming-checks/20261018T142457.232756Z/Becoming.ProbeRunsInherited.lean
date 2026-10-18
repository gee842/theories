import GenerativeCore
import Becoming.Frame
import EvidenceQualifiedCorrection

/-!
# Probing as runs: the inquiry of `EvidenceQualifiedCorrection`, inherited

`EvidenceQualifiedCorrection` revises a situation (the actual model, the candidate models, the
root faults, the installation) by a costed query that keeps the candidates agreeing with the
answer (`probe`), and responds by guarded execution over the candidates' pooled envelope
(`respond`). Both are transitions of one process of the core on situations: an action is a query,
whose step goes to the situation `probe` gives for some answer, or the response, whose step goes
to the situation `respond` gives (`inquiry`). `probe` and `respond` have non-empty axiom reports,
so this module is in the periphery-join ring.

* **What a step does to the candidates.** A query step keeps the actual model and keeps exactly
  the candidates agreeing with the answer (`probe_some`); a response step keeps both (`respond_some`).
* **The actual model stays a candidate along every run.** Along every run of the process
  beginning with the actual model among the candidates, the actual model is the same at every
  step and stays among the candidates (`actual_kept`, through
  `EvidenceQualifiedCorrection.inspected_actual_model_is_retained`).
* **Candidates only narrow along every run** (`candidates_narrow`, through `retained_subset`), so a
  separated pooled envelope stays separated (`separation_kept`, through
  `refinement_preserves_separation`) and an accepted certificate stays accepted while the pool is
  not empty (`certificate_kept`, through `refinement_preserves_certificate`).
* **A chosen plan completes as a trace.** From every situation a selected plan covers, the query
  and then the response form a trace of the process that ends with the command achieved
  (`chosen_plan_completes`, through `selected_inquiry_actually_completes`).
* **The module's plans as traces.** The run of a plan is exactly the trace of its query and the
  response (`trace_iff_run`), so its final situation is the end of every such trace
  (`final_of_trace`). The computed cases are laws of those traces: inspection completes the
  shutdown (`inspected_trace_completes`), or leaves too little to act (`inspected_trace_short_of_reserve`);
  the slow query misses the deadline (`slow_trace_misses_deadline`); the actual trace completes
  without a uniform pool (`reuse_trace_completes_without_uniform_pool`); no candidates, no
  completion (`empty_candidates_trace_fails`); and the selected plans complete from every listed
  situation (`listed_inspect_traces_complete`, `listed_reuse_traces_complete`). Each computed case
  also states that its trace exists (`trace_of_final_ne`), so none of them holds only because there
  is no such trace.

No ethical predicate or ranking occurs. The module adds no axiom of its own; it inherits
`propext` from `EvidenceQualifiedCorrection.probe`, `respond`, `interface`, `final` and every
theorem it uses, and `Quot.sound` from `inspected_actual_model_is_retained`,
`refinement_preserves_separation`, `refinement_preserves_certificate` and
`selected_inquiry_actually_completes`.
-/

namespace Becoming

open Generative FaultTolerantCorrection CorrectionReconfiguration EvidenceQualifiedCorrection

namespace ProbeRunsInherited

/-- The inquiry process: a query steps to the situation `probe` gives for some answer, the
response to the situation `respond` gives. -/
def inquiry : Process Situation (Option Query) :=
  ⟨fun s m t => match m with
    | some q => ∃ a, probe s q = some (a, t)
    | none => respond s () = some t⟩

/-- **A query step keeps the actual model and the candidates agreeing with the answer.** -/
theorem probe_some {s t : Situation} {q : Query} {a : Bool} (h : probe s q = some (a, t)) :
    a = queryLaw q s.actual ∧ t.actual = s.actual ∧
      t.candidates = retain s.candidates (queryLaw q) a := by
  unfold probe at h
  cases hc : (q != .reuse && !s.queryAllowed) with
  | true => rw [hc] at h; exact nomatch h
  | false =>
    rw [hc] at h
    cases hp : EffectiveCommand.spend (queryCost q) (queryCost q) s.installation.state with
    | none => rw [hp] at h; exact nomatch h
    | some paid =>
      rw [hp] at h
      have e := Option.some.inj h
      have ea := congrArg Prod.fst e
      have et := congrArg Prod.snd e
      exact ⟨ea.symm, (congrArg Situation.actual et).symm,
        (congrArg Situation.candidates et).symm.trans
          (congrArg (retain s.candidates (queryLaw q)) ea)⟩

/-- **A response step keeps the actual model and the candidates.** -/
theorem respond_some {s t : Situation} (h : respond s () = some t) :
    t.actual = s.actual ∧ t.candidates = s.candidates :=
  have e := Option.some.inj h
  ⟨(congrArg Situation.actual e).symm, (congrArg Situation.candidates e).symm⟩

/-- A step of the inquiry keeps the actual model among the candidates. -/
theorem step_keeps_actual {s t : Situation} :
    ∀ {m : Option Query}, inquiry.step s m t → s.actual ∈ s.candidates →
      t.actual = s.actual ∧ t.actual ∈ t.candidates
  | some q, ⟨a, h⟩, known => inspected_actual_model_is_retained s q a t known h
  | none, h, known =>
      have kept := respond_some h
      ⟨kept.1, Eq.subst (motive := fun x => x ∈ t.candidates) kept.1.symm
        (Eq.subst (motive := fun l => s.actual ∈ l) kept.2.symm known)⟩

/-- A step of the inquiry keeps only former candidates. -/
theorem step_narrows {s t : Situation} :
    ∀ {m : Option Query}, inquiry.step s m t → ∀ h ∈ t.candidates, h ∈ s.candidates
  | some _, ⟨_, h⟩, x, member =>
      retained_subset _ _ _ x (Eq.subst (motive := fun l => x ∈ l) (probe_some h).2.2 member)
  | none, h, x, member => Eq.subst (motive := fun l => x ∈ l) (respond_some h).2 member

/-- **The actual model stays a candidate along every run.** Along every run of the inquiry
beginning with the actual model among the candidates, the actual model is the same at every step
and stays among the candidates. -/
theorem actual_kept (r : Run inquiry) (known : (r.state 0).actual ∈ (r.state 0).candidates) :
    ∀ n, (r.state n).actual = (r.state 0).actual ∧ (r.state n).actual ∈ (r.state n).candidates
  | 0 => ⟨rfl, known⟩
  | n + 1 =>
      have before := actual_kept r known n
      have kept := step_keeps_actual (r.step n) before.2
      ⟨kept.1.trans before.1, kept.2⟩

/-- **Candidates only narrow along every run.** -/
theorem candidates_narrow (r : Run inquiry) (n : Nat) :
    ∀ h ∈ (r.state (n + 1)).candidates, h ∈ (r.state n).candidates :=
  step_narrows (r.step n)

/-- **A separated pooled envelope stays separated along every run.** For any description of the
models by arrangements, where the pooled envelope of the first candidates is separated on a
roster, so is the pooled envelope of the candidates at every step. -/
theorem separation_kept (desc : Model → Arrangement) (roster : List Domain) (r : Run inquiry)
    (apart : separated roster (pooled desc (r.state 0).candidates)) :
    ∀ n, separated roster (pooled desc (r.state n).candidates)
  | 0 => apart
  | n + 1 => refinement_preserves_separation desc roster _ _ (candidates_narrow r n)
      (separation_kept desc roster r apart n)

/-- **An accepted certificate stays accepted along every run while the pool is not empty.** -/
theorem certificate_kept (desc : Model → Arrangement) (roster : List Domain) (r : Run inquiry)
    (supports : Domain → Bool) (n : Nat)
    (accepted : certificate roster (pooled desc (r.state n).candidates) supports = true)
    (nonempty : pooled desc (r.state (n + 1)).candidates ≠ []) :
    certificate roster (pooled desc (r.state (n + 1)).candidates) supports = true :=
  refinement_preserves_certificate desc roster _ _ (candidates_narrow r n) nonempty supports
    accepted

/-- **A chosen plan completes as a trace.** Where the listed plans' selection over a list of
situations is a plan, from every listed situation its query and then the response form a trace
of the inquiry ending at a situation where the command is achieved. -/
theorem chosen_plan_completes (states : List Situation)
    (chosen : AlignmentInquiry.Plan Query Unit) (s : Situation)
    (selection : AlignmentInquiry.choose interface states plans = some chosen)
    (covered : s ∈ states) :
    ∃ out, Trace inquiry s [some chosen.query, none] out ∧ achieved out = true :=
  match selected_inquiry_actually_completes states chosen s selection covered with
  | ⟨answer, after, out, probed, responded, done⟩ =>
      ⟨out, .cons (⟨answer, probed⟩ : inquiry.step s (some chosen.query) after)
        (.cons (responded : inquiry.step after none out) (.nil out)), done⟩

/-! ## The plans of the module as traces -/

/-- Where the query of a plan is answered, the plan's run is the response from the situation
after. -/
theorem run_answered {s after : Situation} {q : Query} {a : Bool}
    (hp : interface.probe s (plan q).query = some (a, after)) :
    AlignmentInquiry.run interface (plan q) s =
      interface.respond after (AlignmentInquiry.branch (plan q) a) := by
  unfold AlignmentInquiry.run
  rw [hp]
  rfl

/-- Where the query of a plan is not answered, the plan has no run. -/
theorem run_unanswered {s : Situation} {q : Query} (hp : interface.probe s (plan q).query = none) :
    AlignmentInquiry.run interface (plan q) s = none := by
  unfold AlignmentInquiry.run
  rw [hp]
  rfl

/-- **The run of a plan is a trace.** The run of the plan with query `q` ends at `out` exactly
where the query and then the response form a trace of the inquiry from `s` to `out`. -/
theorem trace_iff_run {s out : Situation} {q : Query} :
    Trace inquiry s [some q, none] out ↔ AlignmentInquiry.run interface (plan q) s = some out :=
  ⟨fun tr => match tr with
    | .cons ⟨_, hp⟩ (.cons hr (.nil _)) => (run_answered hp).trans hr,
   fun h => match hp : probe s q with
    | some (a, after) =>
        .cons (⟨a, hp⟩ : inquiry.step s (some q) after)
          (.cons ((run_answered hp).symm.trans h : inquiry.step after none out) (.nil out))
    | none => nomatch (run_unanswered hp).symm.trans h⟩

/-- The final situation of a plan is the end of every trace of its query and response. -/
theorem final_of_trace {s out : Situation} {q : Query} (tr : Trace inquiry s [some q, none] out) :
    final s q = out :=
  congrArg (fun o => Option.getD o s) (trace_iff_run.mp tr)

/-- Where the final situation of a plan differs from the start, its query and response form a
trace ending there. -/
theorem trace_of_final_ne {s : Situation} {q : Query} (moved : final s q ≠ s) :
    Trace inquiry s [some q, none] (final s q) :=
  match e : AlignmentInquiry.run interface (plan q) s with
  | some _ => Eq.subst (motive := fun x => Trace inquiry s [some q, none] x)
      (congrArg (fun o => Option.getD o s) e).symm (trace_iff_run.mpr e)
  | none => absurd (congrArg (fun o => Option.getD o s) e) moved

/-- **An inspection trace completes the shutdown.** From the left model with root fault 0 and
reserve and deadline 12, the inspection query and the response form a trace, and every such trace
ends with the left and swapped models as candidates, the inspection recorded with answer true,
the command achieved, 12 spent, reserve 0 and serial 1. -/
theorem inspected_trace_completes :
    Trace inquiry (initialSituation .left [0] 12 12) [some .inspect, none]
        (final (initialSituation .left [0] 12 12) .inspect) ∧
      ∀ out, Trace inquiry (initialSituation .left [0] 12 12) [some .inspect, none] out →
        out.candidates = [.left, .swapped] ∧ out.receipt = some (.inspect, true) ∧
          achieved out = true ∧ out.installation.state.spent = 12 ∧
          out.installation.state.reserve = 0 ∧ out.installation.serial = 1 :=
  ⟨trace_of_final_ne (fun same =>
      nomatch (congrArg achieved same).symm.trans acquired_evidence_then_real_shutdown.2.2.1),
   fun _ tr => Eq.subst (motive := fun x : Situation =>
      x.candidates = [.left, .swapped] ∧ x.receipt = some (.inspect, true) ∧ achieved x = true ∧
        x.installation.state.spent = 12 ∧ x.installation.state.reserve = 0 ∧
        x.installation.serial = 1)
    (final_of_trace tr) acquired_evidence_then_real_shutdown⟩

/-- **Sufficient evidence can leave too little to act.** From the left model with reserve and
deadline 11, the inspection query and the response form a trace, and every such trace ends with
the left and swapped models as candidates and the inspection recorded, but the command not
completed, 9 spent and reserve 2. -/
theorem inspected_trace_short_of_reserve :
    Trace inquiry (initialSituation .left [0] 11 11) [some .inspect, none]
        (final (initialSituation .left [0] 11 11) .inspect) ∧
      ∀ out, Trace inquiry (initialSituation .left [0] 11 11) [some .inspect, none] out →
        out.candidates = [.left, .swapped] ∧ out.receipt = some (.inspect, true) ∧
          out.installation.state.completed = false ∧ out.installation.state.spent = 9 ∧
          out.installation.state.reserve = 2 :=
  ⟨trace_of_final_ne (fun same =>
      nomatch (congrArg Situation.receipt same).symm.trans sufficient_evidence_can_leave_too_little_to_act.2.1),
   fun _ tr => Eq.subst (motive := fun x : Situation =>
      x.candidates = [.left, .swapped] ∧ x.receipt = some (.inspect, true) ∧
        x.installation.state.completed = false ∧ x.installation.state.spent = 9 ∧
        x.installation.state.reserve = 2)
    (final_of_trace tr) sufficient_evidence_can_leave_too_little_to_act⟩

/-- **A slower query of the same accuracy misses the deadline.** From the left model with reserve
20 and deadline 12, the slow query and the response form a trace, and every such trace ends without
the command achieved, while the inspection query and the response form a trace, and every such
trace ends with it achieved. -/
theorem slow_trace_misses_deadline :
    Trace inquiry (initialSituation .left [0] 20 12) [some .slow, none]
        (final (initialSituation .left [0] 20 12) .slow) ∧
      (∀ out, Trace inquiry (initialSituation .left [0] 20 12) [some .slow, none] out →
        achieved out = false) ∧
      Trace inquiry (initialSituation .left [0] 20 12) [some .inspect, none]
        (final (initialSituation .left [0] 20 12) .inspect) ∧
      ∀ out, Trace inquiry (initialSituation .left [0] 20 12) [some .inspect, none] out →
        achieved out = true :=
  ⟨trace_of_final_ne (fun same => nomatch congrArg Situation.receipt same),
   fun _ tr => Eq.subst (motive := fun x => achieved x = false) (final_of_trace tr)
      slower_equally_accurate_inspection_misses_deadline.1,
   trace_of_final_ne (fun same =>
      nomatch (congrArg achieved same).symm.trans slower_equally_accurate_inspection_misses_deadline.2),
   fun _ tr => Eq.subst (motive := fun x => achieved x = true) (final_of_trace tr)
      slower_equally_accurate_inspection_misses_deadline.2⟩

/-- **No uniform pool, yet the actual trace completes.** The pooled envelope of the three models is
not ready, yet from the left model with no root fault and reserve and deadline 11, the reuse query
and the response form a trace, and every such trace ends with the command achieved. -/
theorem reuse_trace_completes_without_uniform_pool :
    poolReady (pooled describe hypotheses) = false ∧
      Trace inquiry (initialSituation .left [] 11 11) [some .reuse, none]
        (final (initialSituation .left [] 11 11) .reuse) ∧
      ∀ out, Trace inquiry (initialSituation .left [] 11 11) [some .reuse, none] out →
        achieved out = true :=
  ⟨lack_of_uniform_availability_does_not_forbid_actual_certificate.1,
   trace_of_final_ne (fun same => nomatch (congrArg achieved same).symm.trans
      lack_of_uniform_availability_does_not_forbid_actual_certificate.2),
   fun _ tr => Eq.subst (motive := fun x => achieved x = true) (final_of_trace tr)
      lack_of_uniform_availability_does_not_forbid_actual_certificate.2⟩

/-- **No candidates, no completion.** From the left model with no candidates, the reuse query and
the response form a trace, and every such trace ends without the command achieved. -/
theorem empty_candidates_trace_fails :
    Trace inquiry (initialSituation .left [] 20 20 []) [some .reuse, none]
        (final (initialSituation .left [] 20 20 []) .reuse) ∧
      ∀ out, Trace inquiry (initialSituation .left [] 20 20 []) [some .reuse, none] out →
        achieved out = false :=
  ⟨trace_of_final_ne (fun same => nomatch congrArg Situation.receipt same),
   fun _ tr => Eq.subst (motive := fun x => achieved x = false) (final_of_trace tr)
    empty_survivors_do_not_authorize_correction⟩

/-- **Under pooled unknowns, the inspection traces complete.** From every listed situation with
reserve and deadline 12, the inspection query and the response form a trace ending with the
command achieved. -/
theorem listed_inspect_traces_complete :
    ∀ s ∈ possibleSituations 12 12,
      ∃ out, Trace inquiry s [some .inspect, none] out ∧ achieved out = true :=
  fun s covered => chosen_plan_completes _ (plan .inspect) s
    pooled_unknowns_select_affordable_inspection covered

/-- **With the common envelope learned, the reuse traces complete.** From every listed situation
whose candidates are the left and swapped models, with reserve and deadline 11, the reuse query
and the response form a trace ending with the command achieved. -/
theorem listed_reuse_traces_complete :
    ∀ s ∈ possibleSituations 11 11 [.left, .swapped],
      ∃ out, Trace inquiry s [some .reuse, none] out ∧ achieved out = true :=
  fun s covered => chosen_plan_completes _ (plan .reuse) s
    learned_common_envelope_needs_no_further_identification covered

end ProbeRunsInherited

end Becoming
