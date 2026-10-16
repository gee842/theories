import EvidenceQualifiedCorrection

/-! Joint interpretation of a structural question and its fallible witnesses.
A hypothesis supplies both an answer and possible witness fault sets. Do not
select a hypothesis merely because its own trust assumptions certify it.
Missing reports impose no constraint. No identities, physical source bounds,
authentication, normative authority or stable interval are derived here. -/
namespace FallibleInspection
open FaultTolerantCorrection CorrectionReconfiguration EvidenceQualifiedCorrection

abbrev Reports := Domain → Option Bool

def explains (roster bad : List Domain) (answer : Bool) (reports : Reports) : Bool :=
  roster.all (fun d => (bad.contains d) || (reports d).isNone || reports d == some answer)

def compatible (roster : List Domain) (faults : Envelope) (answer : Bool) (reports : Reports) : Bool :=
  faults.any (fun bad => explains roster bad answer reports)

def refine {H : Type} (roster : List Domain) (faults : H → Envelope) (answer : H → Bool)
    (models : List H) (reports : Reports) : List H :=
  models.filter (fun h => compatible roster (faults h) (answer h) reports)

theorem explains_iff (roster bad : List Domain) (answer : Bool) (reports : Reports) :
    explains roster bad answer reports = true ↔
      ∀ d ∈ roster, d ∉ bad → reports d = none ∨ reports d = some answer := by
  simp only [explains,List.all_eq_true]
  constructor
  · intro h d hd outside
    have one := h d hd
    simpa [outside] using one
  · intro h d hd
    by_cases hb : d ∈ bad
    · simp [hb]
    · rcases h d hd hb with missing | agrees
      · simp [hb,missing]
      · simp [hb,agrees]

theorem compatible_iff (roster : List Domain) (faults : Envelope) (answer : Bool) (reports : Reports) :
    compatible roster faults answer reports = true ↔
      ∃ bad, bad ∈ faults ∧ ∀ d ∈ roster, d ∉ bad → reports d = none ∨ reports d = some answer := by
  simp only [compatible,List.any_eq_true,explains_iff]

theorem joint_refinement_preserves_actual {H : Type} (roster : List Domain)
    (faults : H → Envelope) (answer : H → Bool) (models : List H) (actual : H)
    (known : actual ∈ models) (bad : List Domain) (admitted : bad ∈ faults actual)
    (reports : Reports)
    (faithful : ∀ d ∈ roster, d ∉ bad → reports d = none ∨ reports d = some (answer actual)) :
    actual ∈ refine roster faults answer models reports := by
  apply List.mem_filter.mpr
  exact ⟨known,(compatible_iff roster (faults actual) (answer actual) reports).mpr ⟨bad,admitted,faithful⟩⟩

theorem joint_refinement_subset {H : Type} (roster : List Domain) (faults : H → Envelope)
    (answer : H → Bool) (models : List H) (reports : Reports) :
    ∀ h ∈ refine roster faults answer models reports, h ∈ models := by
  intro h hh
  exact (List.mem_filter.mp hh).1

theorem missing_reports_preserve_each_nonempty_model (roster : List Domain) (faults : Envelope)
    (answer : Bool) : compatible roster faults answer (fun _ => none) = !faults.isEmpty := by
  cases faults <;> simp [compatible,explains]

-- Distinction requires a received report outside both candidate fault sets.
theorem received_common_survivor_forces_same_answer (roster a b : List Domain)
    (x y : Bool) (reports : Reports) (ha : explains roster a x reports = true)
    (hb : explains roster b y reports = true)
    (witness : ∃ d, d ∈ roster ∧ d ∉ a ∧ d ∉ b ∧ reports d ≠ none) : x = y := by
  obtain ⟨d,hd,na,nb,present⟩ := witness
  have ax := ((explains_iff roster a x reports).mp ha d hd na).resolve_left present
  have by' := ((explains_iff roster b y reports).mp hb d hd nb).resolve_left present
  exact Option.some.inj (ax.symm.trans by')

def CrossSeparated (roster : List Domain) (fa fb : Envelope) : Prop :=
  ∀ a ∈ fa, ∀ b ∈ fb, ∃ d, d ∈ roster ∧ d ∉ a ∧ d ∉ b

theorem cross_separation_excludes_opposite_explanations (roster : List Domain) (fa fb : Envelope)
    (apart : CrossSeparated roster fa fb) (x y : Bool) (different : x ≠ y)
    (reports : Reports) (complete : ∀ d ∈ roster, reports d ≠ none)
    (first : compatible roster fa x reports = true) : compatible roster fb y reports = false := by
  cases second : compatible roster fb y reports
  · rfl
  · obtain ⟨a,ha,ea⟩ := List.any_eq_true.mp first
    obtain ⟨b,hb,eb⟩ := List.any_eq_true.mp second
    obtain ⟨d,hd,na,nb⟩ := apart a ha b hb
    exact False.elim (different (received_common_survivor_forces_same_answer roster a b x y reports ea eb
      ⟨d,hd,na,nb,complete d hd⟩))

theorem responsive_survivors_exclude_opposite (roster bad : List Domain) (alternatives : Envelope)
    (x y : Bool) (different : x ≠ y) (reports : Reports)
    (responses : ∀ d ∈ roster, d ∉ bad → reports d = some x)
    (apart : ∀ b ∈ alternatives, ∃ d, d ∈ roster ∧ d ∉ bad ∧ d ∉ b) :
    compatible roster alternatives y reports = false := by
  cases accepted : compatible roster alternatives y reports
  · rfl
  · obtain ⟨b,hb,explained⟩ := (compatible_iff _ _ _ _).mp accepted
    obtain ⟨d,hd,na,nb⟩ := apart b hb
    have received := responses d hd na
    rcases explained d hd nb with missing | agrees
    · simp [received] at missing
    · exact False.elim (different (Option.some.inj (received.symm.trans agrees)))

def ambiguousReports (a : List Domain) (x y : Bool) : Reports :=
  fun d => if a.contains d then some y else some x

theorem covering_faults_admit_same_complete_transcript (roster a b : List Domain) (x y : Bool)
    (cover : ∀ d ∈ roster, d ∈ a ∨ d ∈ b) :
    explains roster a x (ambiguousReports a x y) = true ∧
    explains roster b y (ambiguousReports a x y) = true ∧
    ∀ d ∈ roster, ambiguousReports a x y d ≠ none := by
  constructor
  · apply (explains_iff _ _ _ _).mpr
    intro d hd na
    exact Or.inr (by simp [ambiguousReports,na])
  constructor
  · apply (explains_iff _ _ _ _).mpr
    intro d hd nb
    have da := (cover d hd).resolve_right nb
    exact Or.inr (by simp [ambiguousReports,da])
  · intro d hd
    by_cases ha : d ∈ a <;> simp [ambiguousReports,ha]

theorem complete_diagnosability_iff_cross_separation (roster : List Domain) (fa fb : Envelope)
    (x y : Bool) (different : x ≠ y) :
    (∀ reports : Reports, (∀ d ∈ roster, reports d ≠ none) →
      compatible roster fa x reports = true → compatible roster fb y reports = false) ↔
    CrossSeparated roster fa fb := by
  constructor
  · intro distinguish a ha b hb
    apply Classical.byContradiction
    intro absent
    have cover : ∀ d ∈ roster, d ∈ a ∨ d ∈ b := by
      intro d hd
      by_cases da : d ∈ a
      · exact Or.inl da
      · have db : d ∈ b := by
          apply Classical.byContradiction
          intro nb
          exact absent ⟨d,hd,da,nb⟩
        exact Or.inr db
    have both := covering_faults_admit_same_complete_transcript roster a b x y cover
    have first : compatible roster fa x (ambiguousReports a x y) = true :=
      List.any_eq_true.mpr ⟨a,ha,both.1⟩
    have second : compatible roster fb y (ambiguousReports a x y) = true :=
      List.any_eq_true.mpr ⟨b,hb,both.2.1⟩
    have impossible := distinguish _ both.2.2 first
    simp [second] at impossible
  · intro apart reports complete first
    exact cross_separation_excludes_opposite_explanations roster fa fb apart x y different reports complete first

theorem refined_pool_remains_sound {H : Type} (roster : List Domain)
    (faults : H → Envelope) (answer : H → Bool) (describe : H → Arrangement)
    (models : List H) (actual : H) (known : actual ∈ models)
    (bad : List Domain) (admitted : bad ∈ faults actual) (reports : Reports)
    (faithful : ∀ d ∈ roster, d ∉ bad → reports d = none ∨ reports d = some (answer actual))
    (roots : List Nat) (covered : Covered (describe actual) roots) (supports : Domain → Bool)
    (P : Prop) (reliable : ∀ d ∈ (describe actual).roster,
      fails ((describe actual).vulnerability d) roots = false → supports d = true → P)
    (accepted : certificate (describe actual).roster
      (pooled describe (refine roster faults answer models reports)) supports = true) : P := by
  exact pooled_certificate_sound describe _ actual
    (joint_refinement_preserves_actual roster faults answer models actual known bad admitted reports faithful)
    roots covered supports P reliable accepted

-- The installation here is the state after paying for inspection. Its remaining
-- budget must still fund evidence collection and execution of the actual command.
theorem jointly_inspected_completion {H : Type} (roster : List Domain)
    (faults : H → Envelope) (answer : H → Bool) (describe : H → Arrangement)
    (models : List H) (actual : H) (known : actual ∈ models)
    (bad : List Domain) (admitted : bad ∈ faults actual) (reports : Reports)
    (faithful : ∀ d ∈ roster, d ∉ bad → reports d = none ∨ reports d = some (answer actual))
    (roots : List Nat) (covered : Covered (describe actual) roots)
    (apart : separated (describe actual).roster
      (pooled describe (refine roster faults answer models reports)))
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (current : fresh w p = true)
    (readResponses : ∀ d ∈ (describe actual).roster,
      fails ((describe actual).vulnerability d) roots = false → reads d = some (expected p))
    (issueResponses : ∀ d ∈ (describe actual).roster,
      fails ((describe actual).vulnerability d) roots = false → approvals d = some p)
    (readFaithful : ∀ d ∈ (describe actual).roster,
      fails ((describe actual).vulnerability d) roots = false →
      ∀ o, reads d = some o → o = observed w p.address)
    (issueFaithful : ∀ d ∈ (describe actual).roster,
      fails ((describe actual).vulnerability d) roots = false →
      approvals d = some p → withinMandate w p = true)
    (funded : (describe actual).roster.length*(p.address.length+2)+3 ≤ w.state.reserve)
    (timely : w.state.time+(describe actual).roster.length*(p.address.length+2)+3 ≤ w.state.deadline) :
    (guardedExecute (describe actual).roster
      (pooled describe (refine roster faults answer models reports))
      (pooled describe (refine roster faults answer models reports)) w p reads approvals).succeeded = true ∧
    (guardedExecute (describe actual).roster
      (pooled describe (refine roster faults answer models reports))
      (pooled describe (refine roster faults answer models reports)) w p reads approvals).installation.state.completed = true ∧
    withinMandate w p = true := by
  have retained := joint_refinement_preserves_actual roster faults answer models actual known bad admitted reports faithful
  have neutral : retain (refine roster faults answer models reports) (fun _ => false) false =
      refine roster faults answer models reports := List.filter_eq_self.mpr (by intros; rfl)
  have result := evidence_qualified_completion describe
    (refine roster faults answer models reports) (fun _ => false) actual retained roots covered
    (by simpa only [neutral] using apart) w p reads approvals current readResponses issueResponses
    readFaithful issueFaithful funded timely
  simpa only [neutral] using result

-- Concrete structural witnesses share the command reviewers' represented
-- causal control; witness 4 has a distinct diagnostic-only support relation.
def auditRoster (extended : Bool) : List Domain := if extended then [0,1,2,3,4] else roster4

def auditArrangement (extended : Bool) (h : Model) : Arrangement :=
  ⟨auditRoster extended,fun d => if d==4 then .cause 4 else (describe h).vulnerability d,
    if extended then [[0],[1],[2],[3],[4]] else [[0],[1],[2],[3]]⟩

def auditFaults (extended : Bool) (h : Model) : Envelope := envelope (auditArrangement extended h)

def splitReports : Reports := fun d => some (decide (2 ≤ d))

def posterior (extended : Bool) (models : List Model) (reports : Reports) : List Model :=
  refine (auditRoster extended) (auditFaults extended) diagnostic models reports

theorem conflicting_models_each_certify_themselves :
    certificate roster4 (auditFaults false .left) (fun d => splitReports d == some true) = true ∧
    certificate roster4 (auditFaults false .right) (fun d => splitReports d == some false) = true ∧
    posterior false hypotheses splitReports = hypotheses := by decide

theorem four_witnesses_cannot_separate_this_transcript :
    explains roster4 [0,1] true splitReports = true ∧
    explains roster4 [2,3] false splitReports = true := by decide

theorem fifth_diagnostic_witness_resolves_relevant_distinction :
    posterior true hypotheses splitReports = [.left,.swapped] ∧
    poolReady (pooled describe (posterior true hypotheses splitReports)) = true := by decide

theorem absent_fifth_report_preserves_uncertainty :
    posterior true hypotheses (fun d => if d==4 then none else splitReports d) = hypotheses := by decide

-- Even this fifth witness is fallible. Coverage permits it alone to be faulty.
def falseFifth : Reports := fun d => some (d != 4)

theorem fifth_witness_is_not_an_infallible_oracle :
    posterior true hypotheses falseFifth = [.left,.swapped] := by decide

theorem duplicated_fifth_support_does_not_repair_diagnosis :
    let dependent : Model → Envelope := fun h => envelope
      {auditArrangement true h with vulnerability := fun d => (describe h).vulnerability (if d==4 then 2 else d)}
    refine [0,1,2,3,4] dependent diagnostic hypotheses splitReports = hypotheses := by decide

def simulationReports (extended : Bool) (h : Model) (roots : List Nat)
    (arbitrary : Reports) : Reports := fun d =>
  if fails ((auditArrangement extended h).vulnerability d) roots then arbitrary d
  else some (diagnostic h)

structure Audited where
  situation : Situation
  transcript : List (Domain × Option Bool)
  deriving DecidableEq, Repr

def inspect (extended : Bool) (reports : Reports) (s : Situation) : Option Audited := do
  if !s.queryAllowed then none else do
    let cost := (auditRoster extended).length
    let paid ← EffectiveCommand.spend cost cost s.installation.state
    return ⟨{s with
      candidates := posterior extended s.candidates reports
      installation := {s.installation with state := paid}},
      (auditRoster extended).map (fun d => (d,reports d))⟩

def run (extended : Bool) (reports : Reports) (s : Situation) : Option Audited := do
  let checked ← inspect extended reports s
  let result ← EvidenceQualifiedCorrection.respond checked.situation ()
  return {checked with situation := result}

theorem inspection_keeps_actual_under_admitted_faults (extended : Bool) (reports : Reports)
    (s : Situation) (out : Audited) (known : s.actual ∈ s.candidates)
    (bad : List Domain) (admitted : bad ∈ auditFaults extended s.actual)
    (faithful : ∀ d ∈ auditRoster extended, d ∉ bad →
      reports d = none ∨ reports d = some (diagnostic s.actual))
    (done : inspect extended reports s = some out) :
    out.situation.actual = s.actual ∧ out.situation.actual ∈ out.situation.candidates ∧
    out.transcript = (auditRoster extended).map (fun d => (d,reports d)) := by
  unfold inspect at done
  split at done
  · simp at done
  · cases hp : EffectiveCommand.spend (auditRoster extended).length (auditRoster extended).length s.installation.state with
    | none => simp [hp] at done
    | some paid =>
      simp [hp] at done
      cases done
      exact ⟨rfl,joint_refinement_preserves_actual _ _ _ _ _ known bad admitted reports faithful,rfl⟩

def outcome (extended : Bool) (reports : Reports) (s : Situation) : Situation :=
  ((run extended reports s).map Audited.situation).getD s

theorem fallible_inspection_then_actual_shutdown :
    let out := outcome true splitReports (initialSituation .left [0] 16 16)
    out.candidates = [.left,.swapped] ∧ achieved out = true ∧
    out.installation.state.spent = 16 ∧ out.installation.state.reserve = 0 ∧
    out.installation.serial = 1 := by decide

theorem inadequate_witnesses_leave_correction_uncertified :
    let out := outcome false splitReports (initialSituation .left [0] 16 16)
    out.candidates = hypotheses ∧ achieved out = false ∧ out.installation.state.spent = 12 := by decide

theorem diagnostic_success_still_requires_response_capacity :
    let out := outcome true splitReports (initialSituation .left [0] 15 15)
    out.candidates = [.left,.swapped] ∧ achieved out = false ∧
    out.installation.state.spent = 13 ∧ out.installation.state.reserve = 2 := by decide

theorem denied_inspection_does_not_collect_or_execute (extended : Bool) (reports : Reports) (s : Situation)
    (denied : s.queryAllowed = false) : run extended reports s = none := by
  simp [run,inspect,denied]

theorem uncovered_correlated_witness_failure_can_delete_actual :
    let reports : Reports := fun d => some (decide (2 ≤ d))
    induced (auditArrangement true .right) [2,4] = [2,3,4] ∧
    posterior true hypotheses reports = [.left,.swapped] := by decide

end FallibleInspection
