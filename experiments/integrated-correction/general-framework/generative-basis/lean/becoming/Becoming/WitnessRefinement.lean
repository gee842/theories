import Becoming.PooledEnvelopes
import Becoming.Readout

/-!
# Witness refinement: a structural question read jointly with its fallible witnesses

A model supplies both an answer to a structural question and the fault sets its witnesses may
have. Reports of the witnesses are explained by an answer under a fault set where every witness
outside it is silent or reports that answer (`explains`); a model is compatible where some fault
set it admits explains the reports (`compatible`), and refinement keeps the compatible models
(`refine`). A model is not selected merely because its own fault assumptions certify it, and a
missing report constrains nothing.

* **Refinement.** Faithful witnesses outside an admitted fault set keep the actual model
  (`refine_keeps_actual`); refined models were models (`refine_subset`); silence keeps every model
  with a fault set (`silence_keeps_models`).
* **What distinguishes.** A received report outside both fault sets forces the same answer
  (`common_survivor_same_answer`); cross-separated envelopes exclude opposite explanations of a
  complete transcript (`cross_separation_excludes`), as do responsive survivors outside every
  alternative (`responsive_survivors_exclude`); fault sets covering the roster admit one complete
  transcript for both answers (`covering_faults_same_transcript`); and on complete transcripts,
  opposite answers are always distinguished exactly where the envelopes are cross-separated
  (`complete_diagnosability_iff_cross_separation`), which is the core's
  `Readout.no_common_report_envelopes_iff` read on these reports (`explains_complete_iff`,
  `compatible_complete_iff`).
* **Refined pools.** A certificate over the refined pool is sound for the actual arrangement
  (`refined_pool_sound`) and, separated, completes a guarded correction (`refined_completes`).
* **Computed cases.** Conflicting models each certify themselves; four witnesses cannot separate a
  split transcript, a fifth diagnostic witness resolves the distinction, its absence keeps the
  uncertainty, it is still fallible, and duplicating its support repairs nothing; an inspection
  that draws one unit per witness and then responds completes the shutdown with five witnesses,
  leaves the correction uncertified with four, and needs reserve left to respond; denied
  inspection collects nothing; an uncovered correlated failure of witnesses can delete the actual
  model.
* **As a process.** An inspection by a transcript or the response is a step of one process on
  situations (`audit`): it keeps exactly the compatible candidates (`inspect_some`,
  `step_candidates`), candidates only narrow along every run (`candidates_narrow`), faithful
  reports keep the actual model (`step_keeps_actual`) and make the refined pool sound and, where
  separated, complete (`step_pool_sound`, `step_then_completes`); a run is exactly the trace of an
  inspection and the response (`trace_iff_run`), denied inspection is no trace
  (`denied_no_trace`), and the computed outcomes are laws of the traces.

No identities, physical bounds on sources, authentication, warrant of the question or stable
interval are derived. This states `FallibleInspection` (8 October) and its join
`InspectionProcessesInherited` in the core (board item F3C, 18 October 2026), with the words of
exchange replaced: `spent` is `drawn`, `cost` is the roster's length, `mandate` is `scope`. No
premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative ListTests Naturals FaultEnvelopes Transactions Reconfiguration PooledEnvelopes

namespace WitnessRefinement

/-- Reports of the witnesses: silent, or an answer. -/
abbrev Reports := Domain → Option Bool

/-- One witness's term: in the fault set, silent, or reporting the answer. -/
def witnessed (bad : List Domain) (answer : Bool) (reports : Reports) (d : Domain) : Bool :=
  bad.contains d || (reports d).isNone || decide (reports d = some answer)

/-- An answer under a fault set explains the reports. -/
def explains (roster bad : List Domain) (answer : Bool) (reports : Reports) : Bool :=
  roster.all (witnessed bad answer reports)

/-- Some admitted fault set explains the reports with the answer. -/
def compatible (roster : List Domain) (faults : Envelope) (answer : Bool) (reports : Reports) :
    Bool :=
  faults.any (fun bad => explains roster bad answer reports)

/-- The models the reports leave compatible. -/
def refine {H : Type} (roster : List Domain) (faults : H → Envelope) (answer : H → Bool)
    (models : List H) (reports : Reports) : List H :=
  models.filter (fun h => compatible roster (faults h) (answer h) reports)

theorem witnessed_iff {bad : List Domain} {answer : Bool} {reports : Reports} {d : Domain} :
    witnessed bad answer reports d = true ↔
      (¬ d ∈ bad → reports d = none ∨ reports d = some answer) := by
  unfold witnessed
  cases hc : bad.contains d with
  | true => exact ⟨fun _ nb => absurd (contains_true_iff.mp hc) nb, fun _ => rfl⟩
  | false =>
    have out : ¬ d ∈ bad := contains_false_iff.mp hc
    cases ho : reports d with
    | none => exact ⟨fun _ _ => .inl rfl, fun _ => rfl⟩
    | some v =>
      exact ⟨fun h _ => .inr (decide_true_iff.mp h),
        fun f => match f out with
          | .inl e => nomatch e
          | .inr e => decide_true_iff.mpr e⟩

/-- **What an explanation says.** -/
theorem explains_iff (roster bad : List Domain) (answer : Bool) (reports : Reports) :
    explains roster bad answer reports = true ↔
      ∀ d, d ∈ roster → ¬ d ∈ bad → reports d = none ∨ reports d = some answer :=
  all_true_iff.trans ⟨fun h d m => witnessed_iff.mp (h d m), fun h d m => witnessed_iff.mpr (h d m)⟩

/-- **What compatibility says.** -/
theorem compatible_iff (roster : List Domain) (faults : Envelope) (answer : Bool)
    (reports : Reports) :
    compatible roster faults answer reports = true ↔
      ∃ bad, bad ∈ faults ∧
        ∀ d, d ∈ roster → ¬ d ∈ bad → reports d = none ∨ reports d = some answer :=
  any_true_iff.trans ⟨fun ⟨b, m, e⟩ => ⟨b, m, (explains_iff roster b answer reports).mp e⟩,
    fun ⟨b, m, e⟩ => ⟨b, m, (explains_iff roster b answer reports).mpr e⟩⟩

/-! ## Refinement -/

/-- **Faithful witnesses outside an admitted fault set keep the actual model.** -/
theorem refine_keeps_actual {H : Type} (roster : List Domain)
    (faults : H → Envelope) (answer : H → Bool) (models : List H) (actual : H)
    (known : actual ∈ models) (bad : List Domain) (admitted : bad ∈ faults actual)
    (reports : Reports)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (answer actual)) :
    actual ∈ refine roster faults answer models reports :=
  mem_filter_iff.mpr ⟨known,
    (compatible_iff roster (faults actual) (answer actual) reports).mpr ⟨bad, admitted, faithful⟩⟩

/-- **Refined models were models.** -/
theorem refine_subset {H : Type} (roster : List Domain) (faults : H → Envelope)
    (answer : H → Bool) (models : List H) (reports : Reports) :
    ∀ h, h ∈ refine roster faults answer models reports → h ∈ models :=
  fun _ hh => (mem_filter_iff.mp hh).1

/-- **Silence keeps every model with a fault set.** -/
theorem silence_keeps_models (roster : List Domain) (faults : Envelope) (answer : Bool) :
    compatible roster faults answer (fun _ => none) = !faults.isEmpty :=
  match faults with
  | [] => rfl
  | bad :: _ => or_true_iff.mpr (.inl ((explains_iff roster bad answer _).mpr fun _ _ _ => .inl rfl))

/-! ## What distinguishes -/

/-- **A received report outside both fault sets forces the same answer.** -/
theorem common_survivor_same_answer (roster a b : List Domain)
    (x y : Bool) (reports : Reports) (ha : explains roster a x reports = true)
    (hb : explains roster b y reports = true)
    (witness : ∃ d, d ∈ roster ∧ ¬ d ∈ a ∧ ¬ d ∈ b ∧ reports d ≠ none) : x = y :=
  match witness with
  | ⟨d, hd, na, nb, present⟩ =>
    match (explains_iff roster a x reports).mp ha d hd na,
        (explains_iff roster b y reports).mp hb d hd nb with
    | .inl e, _ => absurd e present
    | .inr _, .inl e => absurd e present
    | .inr ex, .inr ey => Option.some.inj (ex.symm.trans ey)

/-- Every fault set of one envelope and every fault set of another leave a witness outside
both. -/
def CrossSeparated (roster : List Domain) (fa fb : Envelope) : Prop :=
  ∀ a, a ∈ fa → ∀ b, b ∈ fb → Readout.CommonWitness roster a b

/-- **Cross-separated envelopes exclude opposite explanations of a complete transcript.** -/
theorem cross_separation_excludes (roster : List Domain) (fa fb : Envelope)
    (apart : CrossSeparated roster fa fb) (x y : Bool) (different : x ≠ y)
    (reports : Reports) (complete : ∀ d, d ∈ roster → reports d ≠ none)
    (first : compatible roster fa x reports = true) : compatible roster fb y reports = false :=
  false_iff_not.mpr fun second =>
    match any_true_iff.mp first, any_true_iff.mp second with
    | ⟨a, ha, ea⟩, ⟨b, hb, eb⟩ => match apart a ha b hb with
      | ⟨d, hd, na, nb⟩ => different
          (common_survivor_same_answer roster a b x y reports ea eb
            ⟨d, hd, na, nb, complete d hd⟩)

/-- **Responsive survivors outside every alternative fault set exclude the opposite answer.** -/
theorem responsive_survivors_exclude (roster bad : List Domain) (alternatives : Envelope)
    (x y : Bool) (different : x ≠ y) (reports : Reports)
    (responses : ∀ d, d ∈ roster → ¬ d ∈ bad → reports d = some x)
    (apart : ∀ b, b ∈ alternatives → ∃ d, d ∈ roster ∧ ¬ d ∈ bad ∧ ¬ d ∈ b) :
    compatible roster alternatives y reports = false :=
  false_iff_not.mpr fun accepted =>
    match (compatible_iff _ _ _ _).mp accepted with
    | ⟨b, hb, explained⟩ => match apart b hb with
      | ⟨d, hd, na, nb⟩ =>
        have received := responses d hd na
        match explained d hd nb with
        | .inl missing => nomatch received.symm.trans missing
        | .inr agrees => different (Option.some.inj (received.symm.trans agrees))

/-- A transcript blaming the first fault set for the second answer. -/
def ambiguousReports (a : List Domain) (x y : Bool) : Reports :=
  fun d => match a.contains d with
    | true => some y
    | false => some x

/-- **Fault sets covering the roster admit one complete transcript for both answers.** -/
theorem covering_faults_same_transcript (roster a b : List Domain) (x y : Bool)
    (cover : ∀ d, d ∈ roster → d ∈ a ∨ d ∈ b) :
    explains roster a x (ambiguousReports a x y) = true ∧
    explains roster b y (ambiguousReports a x y) = true ∧
    ∀ d, d ∈ roster → ambiguousReports a x y d ≠ none :=
  ⟨(explains_iff _ _ _ _).mpr fun d _ na => .inr (by
      show (match a.contains d with | true => some y | false => some x) = some x
      rw [contains_false_iff.mpr na]),
   (explains_iff _ _ _ _).mpr fun d hd nb => .inr (by
      show (match a.contains d with | true => some y | false => some x) = some y
      rw [contains_true_iff.mpr ((cover d hd).resolve_right nb)]),
   fun d _ => by
      show (match a.contains d with | true => some y | false => some x) ≠ none
      cases a.contains d with
      | true => exact fun e => nomatch e
      | false => exact fun e => nomatch e⟩

theorem present_iff {o : Option Bool} {x : Bool} (present : o ≠ none) :
    (o = none ∨ o = some x) ↔ o.getD false = x :=
  match o, present with
  | some _, _ => ⟨fun h => match h with
      | .inl e => nomatch e
      | .inr e => Option.some.inj e, fun e => .inr (congrArg some e)⟩
  | none, absent => absurd rfl absent

/-- **On a complete transcript, an explanation is the core's `Readout.Explains`.** -/
theorem explains_complete_iff {roster bad : List Domain} {x : Bool} {reports : Reports}
    (complete : ∀ d, d ∈ roster → reports d ≠ none) :
    explains roster bad x reports = true ↔
      Readout.Explains roster bad x fun d => (reports d).getD false :=
  (explains_iff roster bad x reports).trans
    ⟨fun h d m nb => (present_iff (complete d m)).mp (h d m nb),
     fun h d m nb => (present_iff (complete d m)).mpr (h d m nb)⟩

/-- On a complete transcript, compatibility is an explanation of the core under an admitted fault
set. -/
theorem compatible_complete_iff {roster : List Domain} {faults : Envelope} {x : Bool}
    {reports : Reports} (complete : ∀ d, d ∈ roster → reports d ≠ none) :
    compatible roster faults x reports = true ↔
      ∃ bad, bad ∈ faults ∧ Readout.Explains roster bad x fun d => (reports d).getD false :=
  any_true_iff.trans
    ⟨fun ⟨b, m, e⟩ => ⟨b, m, (explains_complete_iff complete).mp e⟩,
     fun ⟨b, m, e⟩ => ⟨b, m, (explains_complete_iff complete).mpr e⟩⟩

/-- **On complete transcripts, opposite answers are always distinguished exactly where the
envelopes are cross-separated**: `Readout.no_common_report_envelopes_iff` on these reports. -/
theorem complete_diagnosability_iff_cross_separation (roster : List Domain) (fa fb : Envelope)
    (x y : Bool) (different : x ≠ y) :
    (∀ reports : Reports, (∀ d, d ∈ roster → reports d ≠ none) →
      compatible roster fa x reports = true → compatible roster fb y reports = false) ↔
    CrossSeparated roster fa fb :=
  Iff.trans
    ⟨fun apart (report : Domain → Bool) first second =>
      have complete : ∀ d, d ∈ roster → (fun d => some (report d)) d ≠ none :=
        fun d _ (h : some (report d) = none) => nomatch h
      (nomatch (apart _ complete ((compatible_complete_iff complete).mpr first)).symm.trans
        ((compatible_complete_iff complete).mpr second)),
     fun apart _ complete first =>
      false_iff_not.mpr fun second =>
        apart _ ((compatible_complete_iff complete).mp first)
          ((compatible_complete_iff complete).mp second)⟩
    (Readout.no_common_report_envelopes_iff different)

/-! ## Refined pools -/

/-- **A certificate over the refined pool is sound for the actual arrangement.** -/
theorem refined_pool_sound {H : Type} (roster : List Domain)
    (faults : H → Envelope) (answer : H → Bool) (describe : H → Arrangement)
    (models : List H) (actual : H) (known : actual ∈ models)
    (bad : List Domain) (admitted : bad ∈ faults actual) (reports : Reports)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (answer actual))
    (roots : List Nat) (covered : Covered (describe actual) roots) (supports : Domain → Bool)
    (P : Prop) (reliable : ∀ d, d ∈ (describe actual).roster →
      fails ((describe actual).vulnerability d) roots = false → supports d = true → P)
    (accepted : certificate (describe actual).roster
      (pooled describe (refine roster faults answer models reports)) supports = true) : P :=
  pooled_certificate_sound describe _ actual
    (refine_keeps_actual roster faults answer models actual known bad admitted reports faithful)
    roots covered supports P reliable accepted

/-- **A separated refined pool, with faithful, responsive members, completes a guarded
correction within the scope.** The installation is the one left after the inspection; its
reserve must still cover the response. -/
theorem refined_completes {H : Type} (roster : List Domain)
    (faults : H → Envelope) (answer : H → Bool) (describe : H → Arrangement)
    (models : List H) (actual : H) (known : actual ∈ models)
    (bad : List Domain) (admitted : bad ∈ faults actual) (reports : Reports)
    (faithful : ∀ d, d ∈ roster → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (answer actual))
    (roots : List Nat) (covered : Covered (describe actual) roots)
    (apart : separated (describe actual).roster
      (pooled describe (refine roster faults answer models reports)))
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (current : fresh w p = true)
    (readResponses : ∀ d, d ∈ (describe actual).roster →
      fails ((describe actual).vulnerability d) roots = false → reads d = some (expected p))
    (issueResponses : ∀ d, d ∈ (describe actual).roster →
      fails ((describe actual).vulnerability d) roots = false → approvals d = some p)
    (readFaithful : ∀ d, d ∈ (describe actual).roster →
      fails ((describe actual).vulnerability d) roots = false →
      ∀ o, reads d = some o → o = observed w p.address)
    (issueFaithful : ∀ d, d ∈ (describe actual).roster →
      fails ((describe actual).vulnerability d) roots = false →
      approvals d = some p → withinScope w p = true)
    (stocked : load (describe actual).roster p + 3 ≤ w.state.reserve)
    (timely : w.state.time + load (describe actual).roster p + 3 ≤ w.state.deadline) :
    (guardedExecute (describe actual).roster
      (pooled describe (refine roster faults answer models reports))
      (pooled describe (refine roster faults answer models reports)) w p reads
        approvals).succeeded = true ∧
    (guardedExecute (describe actual).roster
      (pooled describe (refine roster faults answer models reports))
      (pooled describe (refine roster faults answer models reports)) w p reads
        approvals).installation.state.completed = true ∧
    withinScope w p = true :=
  member_completes describe _ actual
    (refine_keeps_actual roster faults answer models actual known bad admitted reports faithful)
    roots covered apart w p reads approvals current readResponses issueResponses readFaithful
    issueFaithful stocked timely

/-! ## Computed cases -/

/-- The roster of witnesses, with or without the fifth. -/
def auditRoster : Bool → List Domain
  | true => [0, 1, 2, 3, 4]
  | false => roster4

/-- The arrangement of the witnesses under a model: the four reviewers as the model has them, the
fifth with its own cause. -/
def auditArrangement (extended : Bool) (h : Model) : Arrangement :=
  ⟨auditRoster extended, fun d => if d = 4 then .cause 4 else (describe h).vulnerability d,
    match extended with
    | true => [[0], [1], [2], [3], [4]]
    | false => [[0], [1], [2], [3]]⟩

/-- The fault sets of the witnesses under a model. -/
def auditFaults (extended : Bool) (h : Model) : Envelope := envelope (auditArrangement extended h)

/-- A transcript splitting the witnesses: the first two answer false, the rest true. -/
def splitReports : Reports := fun d => some (decide (2 ≤ d))

/-- The models a transcript leaves. -/
def posterior (extended : Bool) (models : List Model) (reports : Reports) : List Model :=
  refine (auditRoster extended) (auditFaults extended) diagnostic models reports

/-- **Conflicting models each certify themselves.** -/
theorem conflicting_models_self_certify :
    certificate roster4 (auditFaults false .left) (fun d => decide (splitReports d = some true))
      = true ∧
    certificate roster4 (auditFaults false .right) (fun d => decide (splitReports d = some false))
      = true ∧
    posterior false hypotheses splitReports = hypotheses := by decide

/-- **Four witnesses cannot separate this transcript.** -/
theorem four_witnesses_inseparable :
    explains roster4 [0, 1] true splitReports = true ∧
    explains roster4 [2, 3] false splitReports = true := by decide

/-- **A fifth diagnostic witness resolves the distinction that matters.** -/
theorem fifth_witness_resolves :
    posterior true hypotheses splitReports = [.left, .swapped] ∧
    poolReady (pooled describe (posterior true hypotheses splitReports)) = true := by decide

/-- **An absent fifth report keeps the uncertainty.** -/
theorem absent_fifth_keeps_uncertainty :
    posterior true hypotheses (fun d => if d = 4 then none else splitReports d) = hypotheses := by
  decide

/-- A transcript whose fifth witness alone is wrong. -/
def falseFifth : Reports := fun d => some (decide (d ≠ 4))

/-- **The fifth witness is not an infallible oracle**: coverage permits it alone to be faulty. -/
theorem fifth_witness_fallible : posterior true hypotheses falseFifth = [.left, .swapped] := by
  decide

/-- The fault sets where the fifth witness shares the third's cause. -/
def dependentFaults (h : Model) : Envelope :=
  envelope {auditArrangement true h with
    vulnerability := fun d => (describe h).vulnerability (if d = 4 then 2 else d)}

/-- **Duplicating the fifth witness's support repairs nothing.** -/
theorem duplicated_fifth_no_repair :
    refine [0, 1, 2, 3, 4] dependentFaults diagnostic hypotheses splitReports = hypotheses := by
  decide

/-- The reports a simulated physical response gives: working witnesses report the model's answer,
failed ones report arbitrarily. -/
def simulationReports (extended : Bool) (h : Model) (roots : List Nat)
    (arbitrary : Reports) : Reports := fun d =>
  match fails ((auditArrangement extended h).vulnerability d) roots with
  | true => arbitrary d
  | false => some (diagnostic h)

/-- A situation after an inspection, with the transcript collected. -/
structure Audited where
  situation : Situation
  transcript : List (Domain × Option Bool)
  deriving DecidableEq

/-- An inspection: where inspection is open, draw one unit per witness, keep the compatible
candidates and collect the transcript. -/
def inspect (extended : Bool) (reports : Reports) (s : Situation) : Option Audited :=
  match s.queryOpen with
  | false => none
  | true =>
    (Actuation.draw (auditRoster extended).length (auditRoster extended).length
      s.installation.state).map fun after =>
      ⟨{s with
        candidates := posterior extended s.candidates reports
        installation := {s.installation with state := after}},
        (auditRoster extended).map (fun d => (d, reports d))⟩

/-- An inspection, then the response. -/
def run (extended : Bool) (reports : Reports) (s : Situation) : Option Audited :=
  match inspect extended reports s with
  | none => none
  | some checked => (respond checked.situation ()).map fun result => {checked with situation := result}

/-- **An inspection whose reports are faithful outside an admitted fault set keeps the actual
model a candidate and collects the transcript.** -/
theorem inspection_keeps_actual (extended : Bool) (reports : Reports)
    (s : Situation) (out : Audited) (known : s.actual ∈ s.candidates)
    (bad : List Domain) (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d, d ∈ auditRoster extended → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual))
    (done : inspect extended reports s = some out) :
    out.situation.actual = s.actual ∧ out.situation.actual ∈ out.situation.candidates ∧
    out.transcript = (auditRoster extended).map (fun d => (d, reports d)) := by
  unfold inspect at done
  cases hq : s.queryOpen with
  | false => rw [hq] at done; exact nomatch done
  | true =>
    rw [hq] at done
    obtain ⟨after, _, e⟩ := map_eq_some.mp done
    subst e
    exact ⟨rfl, refine_keeps_actual _ _ _ _ _ known bad admitted reports faithful, rfl⟩

/-- The situation the reports leave. -/
def outcome (extended : Bool) (reports : Reports) (s : Situation) : Situation :=
  ((run extended reports s).map Audited.situation).getD s

/-- **Fallible inspection, then the shutdown.** -/
theorem inspection_then_shutdown :
    (outcome true splitReports (initialSituation .left [0] 16 16)).candidates = [.left, .swapped] ∧
    achieved (outcome true splitReports (initialSituation .left [0] 16 16)) = true ∧
    (outcome true splitReports (initialSituation .left [0] 16 16)).installation.state.drawn = 16 ∧
    (outcome true splitReports (initialSituation .left [0] 16 16)).installation.state.reserve = 0 ∧
    (outcome true splitReports (initialSituation .left [0] 16 16)).installation.serial = 1 := by
  decide

/-- **Inadequate witnesses leave the correction uncertified.** -/
theorem inadequate_witnesses_uncertified :
    (outcome false splitReports (initialSituation .left [0] 16 16)).candidates = hypotheses ∧
    achieved (outcome false splitReports (initialSituation .left [0] 16 16)) = false ∧
    (outcome false splitReports (initialSituation .left [0] 16 16)).installation.state.drawn = 12 := by
  decide

/-- **Diagnostic success still needs reserve to respond.** -/
theorem diagnosis_needs_response_reserve :
    (outcome true splitReports (initialSituation .left [0] 15 15)).candidates = [.left, .swapped] ∧
    achieved (outcome true splitReports (initialSituation .left [0] 15 15)) = false ∧
    (outcome true splitReports (initialSituation .left [0] 15 15)).installation.state.drawn = 13 ∧
    (outcome true splitReports (initialSituation .left [0] 15 15)).installation.state.reserve = 2 := by
  decide

/-- **Denied inspection neither collects nor executes.** -/
theorem denied_no_run (extended : Bool) (reports : Reports) (s : Situation)
    (denied : s.queryOpen = false) : run extended reports s = none := by
  unfold run inspect
  rw [denied]

/-- **An uncovered correlated failure of witnesses can delete the actual model.** -/
theorem uncovered_correlation_deletes_actual :
    induced (auditArrangement true .right) [2, 4] = [2, 3, 4] ∧
    posterior true hypotheses (fun d => some (decide (2 ≤ d))) = [.left, .swapped] := by decide

/-! ## Inspection as a process -/

/-- **The audit process**, for the roster with or without the fifth witness: a transcript steps
to the situation `inspect` gives, the response to the situation `respond` gives. -/
def audit (extended : Bool) : Process Situation (Option Reports) where
  step s m t := match m with
    | some reports => ∃ c, inspect extended reports s = some c ∧ c.situation = t
    | none => respond s () = some t

/-- **An inspection keeps the actual model and exactly the compatible candidates.** -/
theorem inspect_some {extended : Bool} {reports : Reports} {s : Situation} {c : Audited}
    (h : inspect extended reports s = some c) :
    c.situation.actual = s.actual ∧
      c.situation.candidates = posterior extended s.candidates reports := by
  unfold inspect at h
  cases hq : s.queryOpen with
  | false => rw [hq] at h; exact nomatch h
  | true =>
    rw [hq] at h
    obtain ⟨after, _, e⟩ := map_eq_some.mp h
    subst e
    exact ⟨rfl, rfl⟩

/-- **An inspection step leaves the candidates the reports leave compatible.** -/
theorem step_candidates {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) :
    t.candidates = posterior extended s.candidates reports :=
  match step with
  | ⟨_, h, same⟩ => same ▸ (inspect_some h).2

/-- A step of the audit keeps only former candidates. -/
theorem step_narrows {extended : Bool} {s t : Situation} :
    ∀ {m : Option Reports}, (audit extended).step s m t →
      ∀ h, h ∈ t.candidates → h ∈ s.candidates
  | some _, step, x, member =>
      refine_subset _ _ _ _ _ x (Eq.subst (motive := fun l => x ∈ l) (step_candidates step) member)
  | none, h, x, member => Eq.subst (motive := fun l => x ∈ l) (respond_some h).2 member

/-- **Candidates only narrow along every run of the audit.** -/
theorem candidates_narrow {extended : Bool} (r : Run (audit extended)) (n : Nat) :
    ∀ h, h ∈ (r.state (n + 1)).candidates → h ∈ (r.state n).candidates :=
  step_narrows (r.step n)

/-- **Faithful reports keep the actual model.** -/
theorem step_keeps_actual {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) (known : s.actual ∈ s.candidates)
    (bad : List Domain) (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d, d ∈ auditRoster extended → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual)) :
    t.actual = s.actual ∧ t.actual ∈ t.candidates :=
  match step with
  | ⟨c, h, same⟩ =>
    match inspection_keeps_actual extended reports s c known bad admitted faithful h with
    | ⟨kept, member, _⟩ => same ▸ ⟨kept, member⟩

/-- **After a faithful inspection step, an accepted pooled certificate is sound.** -/
theorem step_pool_sound {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) (desc : Model → Arrangement)
    (known : s.actual ∈ s.candidates) (bad : List Domain)
    (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d, d ∈ auditRoster extended → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual))
    (roots : List Nat) (covered : Covered (desc s.actual) roots) (supports : Domain → Bool)
    (P : Prop) (reliable : ∀ d, d ∈ (desc s.actual).roster →
      fails ((desc s.actual).vulnerability d) roots = false → supports d = true → P)
    (accepted : certificate (desc s.actual).roster (pooled desc t.candidates) supports = true) :
    P :=
  refined_pool_sound (auditRoster extended) (auditFaults extended) diagnostic desc
    s.candidates s.actual known bad admitted reports faithful roots covered supports P reliable
    (Eq.subst (motive := fun l => certificate (desc s.actual).roster (pooled desc l) supports = true)
      (step_candidates step) accepted)

/-- **After a faithful inspection step, faithful responses complete within the scope.** -/
theorem step_then_completes {extended : Bool} {reports : Reports} {s t : Situation}
    (step : (audit extended).step s (some reports) t) (desc : Model → Arrangement)
    (known : s.actual ∈ s.candidates) (bad : List Domain)
    (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d, d ∈ auditRoster extended → ¬ d ∈ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual))
    (roots : List Nat) (covered : Covered (desc s.actual) roots)
    (apart : separated (desc s.actual).roster (pooled desc t.candidates))
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (current : fresh w p = true)
    (readResponses : ∀ d, d ∈ (desc s.actual).roster →
      fails ((desc s.actual).vulnerability d) roots = false → reads d = some (expected p))
    (issueResponses : ∀ d, d ∈ (desc s.actual).roster →
      fails ((desc s.actual).vulnerability d) roots = false → approvals d = some p)
    (readFaithful : ∀ d, d ∈ (desc s.actual).roster →
      fails ((desc s.actual).vulnerability d) roots = false →
      ∀ o, reads d = some o → o = observed w p.address)
    (issueFaithful : ∀ d, d ∈ (desc s.actual).roster →
      fails ((desc s.actual).vulnerability d) roots = false →
      approvals d = some p → withinScope w p = true)
    (stocked : load (desc s.actual).roster p + 3 ≤ w.state.reserve)
    (timely : w.state.time + load (desc s.actual).roster p + 3 ≤ w.state.deadline) :
    (guardedExecute (desc s.actual).roster (pooled desc t.candidates) (pooled desc t.candidates)
      w p reads approvals).succeeded = true ∧
    (guardedExecute (desc s.actual).roster (pooled desc t.candidates) (pooled desc t.candidates)
      w p reads approvals).installation.state.completed = true ∧
    withinScope w p = true :=
  have e := step_candidates step
  Eq.subst (motive := fun l =>
      (guardedExecute (desc s.actual).roster (pooled desc l) (pooled desc l)
        w p reads approvals).succeeded = true ∧
      (guardedExecute (desc s.actual).roster (pooled desc l) (pooled desc l)
        w p reads approvals).installation.state.completed = true ∧
      withinScope w p = true) e.symm
    (refined_completes (auditRoster extended) (auditFaults extended) diagnostic desc
      s.candidates s.actual known bad admitted reports faithful roots covered
      (Eq.subst (motive := fun l => separated (desc s.actual).roster (pooled desc l)) e apart)
      w p reads approvals current readResponses issueResponses readFaithful issueFaithful stocked
      timely)

/-- Where inspection gives an audit, the run is the response from its situation. -/
theorem run_inspected {extended : Bool} {reports : Reports} {s : Situation} {c : Audited}
    (h : inspect extended reports s = some c) :
    run extended reports s = (respond c.situation ()).map fun result => {c with situation := result} := by
  unfold run
  rw [h]

/-- Where inspection gives no audit, there is no run. -/
theorem run_uninspected {extended : Bool} {reports : Reports} {s : Situation}
    (h : inspect extended reports s = none) : run extended reports s = none := by
  unfold run
  rw [h]

/-- **Denied inspection is no trace**: no inspection step is followed by a response step. -/
theorem denied_no_trace {extended : Bool} {reports : Reports} {s : Situation}
    (denied : s.queryOpen = false) :
    ¬ ∃ t u, (audit extended).step s (some reports) t ∧ (audit extended).step t none u :=
  fun ⟨_, _, ⟨_, h, _⟩, _⟩ =>
    nomatch (run_inspected h).symm.trans (denied_no_run extended reports s denied)

/-- **A run is a trace.** The run ends at `u` exactly where the inspection by the reports and then
the response form a trace of the audit from `s` to `u`. -/
theorem trace_iff_run {extended : Bool} {reports : Reports} {s u : Situation} :
    Trace (audit extended) s [some reports, none] u ↔
      (run extended reports s).map Audited.situation = some u := by
  constructor
  · intro tr
    obtain ⟨t, ⟨c, h, same⟩, rest⟩ := trace_cons_iff.mp tr
    obtain ⟨v, responded, last⟩ := trace_cons_iff.mp rest
    have ev : v = u := trace_nil_iff.mp last
    subst same
    subst ev
    rw [run_inspected h, responded]
    rfl
  · intro h
    cases hi : inspect extended reports s with
    | none => rw [run_uninspected hi] at h; exact nomatch h
    | some c =>
      rw [run_inspected hi] at h
      cases hr : respond c.situation () with
      | none => rw [hr] at h; exact nomatch h
      | some v =>
        rw [hr] at h
        exact .cons (⟨c, hi, rfl⟩ : (audit extended).step s (some reports) c.situation)
          (.cons (hr.trans (congrArg some (Option.some.inj h))) (.nil u))

/-- The outcome of the reports is the end of every trace of the inspection and the response. -/
theorem outcome_of_trace {extended : Bool} {reports : Reports} {s u : Situation}
    (tr : Trace (audit extended) s [some reports, none] u) : outcome extended reports s = u :=
  congrArg (fun o => Option.getD o s) (trace_iff_run.mp tr)

/-- Where the outcome differs from the start, the inspection and the response form a trace ending
there. -/
theorem trace_of_outcome_ne {extended : Bool} {reports : Reports} {s : Situation}
    (moved : outcome extended reports s ≠ s) :
    Trace (audit extended) s [some reports, none] (outcome extended reports s) :=
  match e : (run extended reports s).map Audited.situation with
  | some _ => Eq.subst (motive := fun x => Trace (audit extended) s [some reports, none] x)
      (congrArg (fun o => Option.getD o s) e).symm (trace_iff_run.mpr e)
  | none => absurd (congrArg (fun o => Option.getD o s) e) moved

/-- **With the fifth witness, the inspection trace completes the shutdown.** -/
theorem extended_trace_completes :
    Trace (audit true) (initialSituation .left [0] 16 16) [some splitReports, none]
        (outcome true splitReports (initialSituation .left [0] 16 16)) ∧
      ∀ u, Trace (audit true) (initialSituation .left [0] 16 16) [some splitReports, none] u →
        u.candidates = [.left, .swapped] ∧ achieved u = true ∧
          u.installation.state.drawn = 16 ∧ u.installation.state.reserve = 0 ∧
          u.installation.serial = 1 :=
  ⟨trace_of_outcome_ne (fun same =>
      nomatch (congrArg achieved same).symm.trans inspection_then_shutdown.2.1),
   fun _ tr => outcome_of_trace tr ▸ inspection_then_shutdown⟩

/-- **Four witnesses leave the correction uncertified, as traces.** -/
theorem four_witness_trace_uncertified :
    Trace (audit false) (initialSituation .left [0] 16 16) [some splitReports, none]
        (outcome false splitReports (initialSituation .left [0] 16 16)) ∧
      ∀ u, Trace (audit false) (initialSituation .left [0] 16 16) [some splitReports, none] u →
        u.candidates = hypotheses ∧ achieved u = false ∧ u.installation.state.drawn = 12 :=
  ⟨trace_of_outcome_ne (fun same => nomatch
      (congrArg (fun x : Situation => x.installation.state.drawn) same).symm.trans
        inadequate_witnesses_uncertified.2.2),
   fun _ tr => outcome_of_trace tr ▸ inadequate_witnesses_uncertified⟩

/-- **Diagnostic success still needs the reserve to respond, as traces.** -/
theorem extended_trace_short_of_reserve :
    Trace (audit true) (initialSituation .left [0] 15 15) [some splitReports, none]
        (outcome true splitReports (initialSituation .left [0] 15 15)) ∧
      ∀ u, Trace (audit true) (initialSituation .left [0] 15 15) [some splitReports, none] u →
        u.candidates = [.left, .swapped] ∧ achieved u = false ∧
          u.installation.state.drawn = 13 ∧ u.installation.state.reserve = 2 :=
  ⟨trace_of_outcome_ne (fun same => nomatch
      (congrArg (fun x : Situation => x.installation.state.drawn) same).symm.trans
        diagnosis_needs_response_reserve.2.2.1),
   fun _ tr => outcome_of_trace tr ▸ diagnosis_needs_response_reserve⟩

end WitnessRefinement

end Becoming
