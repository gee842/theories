import CorrectionReconfiguration

/-! Conservative certificates under causal-model uncertainty, followed by
costed, observation-dependent correction. This reuses existing model revision
and planning. Candidate coverage, a faithful stable diagnostic interface and
protected command execution remain supplied correspondence conditions. -/
namespace EvidenceQualifiedCorrection
open FaultTolerantCorrection CorrectionReconfiguration

-- Several descriptions may remain; collect every fault set they admit.
def pooled {H : Type} (describe : H → Arrangement) (models : List H) : Envelope :=
  models.flatMap (fun h => envelope (describe h))

def retain {H : Type} (models : List H) (test : H → Bool) (answer : Bool) : List H :=
  models.filter (fun h => test h == answer)

theorem retained_truth {H : Type} (models : List H) (test : H → Bool) (actual : H)
    (covered : actual ∈ models) : actual ∈ retain models test (test actual) := by
  simp [retain,covered]

theorem retained_subset {H : Type} (models : List H) (test : H → Bool) (answer : Bool) :
    ∀ h ∈ retain models test answer, h ∈ models := by
  intro h hh
  exact (List.mem_filter.mp hh).1

theorem model_faults_in_pool {H : Type} (describe : H → Arrangement) (models : List H)
    (actual : H) (known : actual ∈ models) (bad : List Domain)
    (member : bad ∈ envelope (describe actual)) : bad ∈ pooled describe models := by
  exact List.mem_flatMap.mpr ⟨actual,known,member⟩

theorem pooled_subset {H : Type} (describe : H → Arrangement) (old new : List H)
    (included : ∀ h ∈ new, h ∈ old) :
    ∀ bad ∈ pooled describe new, bad ∈ pooled describe old := by
  intro bad hb
  obtain ⟨h,hh,hb⟩ := List.mem_flatMap.mp hb
  exact List.mem_flatMap.mpr ⟨h,included h hh,hb⟩

theorem pooled_certificate_sound {H : Type} (describe : H → Arrangement) (models : List H)
    (actual : H) (known : actual ∈ models) (roots : List Nat) (covered : Covered (describe actual) roots)
    (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d ∈ (describe actual).roster,
      fails ((describe actual).vulnerability d) roots = false → supports d = true → P)
    (accepted : certificate (describe actual).roster (pooled describe models) supports = true) : P := by
  obtain ⟨bound,member,included⟩ := covered
  have admitted : induced (describe actual) bound ∈ pooled describe models :=
    model_faults_in_pool describe models actual known _ (List.mem_map.mpr ⟨bound,member,rfl⟩)
  apply certificate_sound _ _ supports _ admitted P _ accepted
  intro d hd outside yes
  exact faithful d hd (outside_bound_survives _ roots bound included d hd outside) yes

theorem refinement_preserves_certificate {H : Type} (describe : H → Arrangement)
    (roster : List Domain) (old new : List H) (included : ∀ h ∈ new, h ∈ old)
    (nonempty : pooled describe new ≠ []) (supports : Domain → Bool)
    (accepted : certificate roster (pooled describe old) supports = true) :
    certificate roster (pooled describe new) supports = true := by
  apply stronger_fault_coverage_cannot_create_acceptance roster (pooled describe new)
    (pooled describe old) supports nonempty _ accepted
  intro bad hb
  exact ⟨bad,pooled_subset describe old new included bad hb,by intro d hd; exact hd⟩

theorem refinement_preserves_separation {H : Type} (describe : H → Arrangement)
    (roster : List Domain) (old new : List H) (included : ∀ h ∈ new, h ∈ old)
    (apart : separated roster (pooled describe old)) : separated roster (pooled describe new) := by
  intro a ha b hb
  exact apart a (pooled_subset describe old new included a ha) b
    (pooled_subset describe old new included b hb)

theorem empty_family_rejects (roster : List Domain) {H : Type}
    (describe : H → Arrangement) (supports : Domain → Bool) :
    certificate roster (pooled describe []) supports = false := by rfl

theorem evidence_qualified_completion {H : Type} (describe : H → Arrangement)
    (models : List H) (test : H → Bool) (actual : H) (known : actual ∈ models)
    (roots : List Nat) (covered : Covered (describe actual) roots)
    (apart : separated (describe actual).roster (pooled describe (retain models test (test actual))))
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
      (pooled describe (retain models test (test actual)))
      (pooled describe (retain models test (test actual))) w p reads approvals).succeeded = true ∧
    (guardedExecute (describe actual).roster
      (pooled describe (retain models test (test actual)))
      (pooled describe (retain models test (test actual))) w p reads approvals).installation.state.completed = true ∧
    withinMandate w p = true := by
  obtain ⟨bound,member,included⟩ := covered
  have admitted : induced (describe actual) bound ∈ pooled describe (retain models test (test actual)) :=
    model_faults_in_pool describe _ actual (retained_truth models test actual known) _
      (List.mem_map.mpr ⟨bound,member,rfl⟩)
  have safe := outside_bound_survives (describe actual) roots bound included
  have h := quorum_to_actual_correction (describe actual).roster _ _ w p reads approvals
    (induced (describe actual) bound) (induced (describe actual) bound) admitted admitted apart apart current
    (fun d hd hn => readResponses d hd (safe d hd hn))
    (fun d hd hn => issueResponses d hd (safe d hd hn))
    (fun d hd hn => readFaithful d hd (safe d hd hn))
    (fun d hd hn => issueFaithful d hd (safe d hd hn)) funded timely
  have guarded := within_mandate_completion_survives_direct_guard (describe actual).roster _ _ w p reads approvals
    h.2.2 ⟨h.1,h.2.1⟩
  exact ⟨guarded.1,guarded.2,h.2.2⟩

inductive Model where
  | left | swapped | right
  deriving DecidableEq, Repr

def describe : Model → Arrangement
  | .left => ⟨[0,1,2,3],fun d => .cause (if d < 2 then 0 else d),[[0],[1],[2],[3]]⟩
  | .swapped => ⟨[0,1,2,3],fun d => .cause (if d < 2 then 0 else if d == 2 then 3 else 2),[[0],[1],[2],[3]]⟩
  | .right => ⟨[0,1,2,3],fun d => .cause (if d < 2 then d else 2),[[0],[1],[2],[3]]⟩

def hypotheses : List Model := [.left,.swapped,.right]
def diagnostic (h : Model) : Bool := fails ((describe h).vulnerability 1) [0]

def poolReady (faults : Envelope) : Bool :=
  !faults.isEmpty && faults.all (fun a => faults.all (fun b =>
    roster4.any (fun d => !(a.contains d) && !(b.contains d))))

theorem every_candidate_ready_but_pool_not_ready :
    hypotheses.all (fun h => ready (describe h)) = true ∧
    poolReady (pooled describe hypotheses) = false := by decide

theorem actual_survivors_can_be_insufficient_before_diagnosis :
    certificate roster4 (pooled describe hypotheses) (fun d => decide (2 ≤ d)) = false ∧
    certificate roster4 (envelope (describe .left)) (fun d => decide (2 ≤ d)) = true := by decide

theorem diagnosis_need_not_identify_the_model :
    retain hypotheses diagnostic true = [.left,.swapped] ∧
    (describe .left).vulnerability 2 ≠ (describe .swapped).vulnerability 2 ∧
    poolReady (pooled describe (retain hypotheses diagnostic true)) = true ∧
    poolReady (pooled describe (retain hypotheses diagnostic false)) = true := by decide

theorem misleading_diagnosis_can_accept_only_compromised_support :
    diagnostic .left = true ∧ retain hypotheses diagnostic false = [.right] ∧
    induced (describe .left) [0] = [0,1] ∧
    certificate roster4 (pooled describe (retain hypotheses diagnostic false))
      (fun d => decide (d < 2)) = true := by decide

theorem unobserved_structural_change_invalidates_learned_coverage :
    induced (describe .right) [2] = [2,3] ∧
    certificate roster4 (pooled describe (retain hypotheses diagnostic true))
      (fun d => decide (2 ≤ d)) = true := by decide

inductive Query where
  | reuse | inspect | slow
  deriving DecidableEq, Repr

def queryCost : Query → Nat | .reuse => 0 | .inspect => 1 | .slow => 3

def queryLaw : Query → Model → Bool | .reuse,_ => false | _,h => diagnostic h

structure Situation where
  actual : Model
  candidates : List Model
  roots : List Nat
  installation : Installation
  queryAllowed : Bool := true
  receipt : Option (Query × Bool) := none
  deriving DecidableEq, Repr

-- The query is a supplied faithful structural inspection, not adversarial
-- fault-injection certification. It changes records, work and time together.
def probe (s : Situation) (q : Query) : Option (Bool × Situation) := do
  if q != .reuse && !s.queryAllowed then none else do
    let paid ← EffectiveCommand.spend (queryCost q) (queryCost q) s.installation.state
    let answer := queryLaw q s.actual
    return (answer,{s with
      candidates := retain s.candidates (queryLaw q) answer
      installation := {s.installation with state := paid}
      receipt := some (q,answer)})

def currentRequest (w : Installation) : Request :=
  ⟨w.state.authority,w.serial,[],true,.shutdown⟩

-- Simulated physical response law; the selection rule sees only records and
-- candidates. Nonfailed domains report the snapshot; exposed ones withhold.
def physicalReads (s : Situation) : Readings := fun d =>
  if fails ((describe s.actual).vulnerability d) s.roots then none
  else some (observed s.installation [])

def physicalApprovals (s : Situation) : Approvals := fun d =>
  if fails ((describe s.actual).vulnerability d) s.roots then none
  else if withinMandate s.installation (currentRequest s.installation)
    then some (currentRequest s.installation) else none

def respond (s : Situation) (_ : Unit) : Option Situation :=
  let out := guardedExecute roster4 (pooled describe s.candidates) (pooled describe s.candidates)
    s.installation (currentRequest s.installation) (physicalReads s) (physicalApprovals s)
  some {s with installation := out.installation}

def achieved (s : Situation) : Bool := s.installation.state.completed && !s.installation.state.running

def interface : AlignmentInquiry.Interface Situation Query Unit := ⟨probe,respond,achieved⟩

def plan (q : Query) : AlignmentInquiry.Plan Query Unit := ⟨q,(),()⟩
def plans : List (AlignmentInquiry.Plan Query Unit) := [.reuse,.inspect,.slow].map plan

def initialSituation (h : Model) (roots : List Nat) (fuel deadline : Nat)
    (models : List Model := hypotheses) (allowed : Bool := true) : Situation :=
  ⟨h,models,roots,{initial with state := {initial.state with reserve := fuel,deadline := deadline}},allowed,none⟩

def possibleSituations (fuel deadline : Nat) (models : List Model := hypotheses)
    (allowed : Bool := true) : List Situation :=
  models.flatMap (fun h => [[],[0],[1],[2],[3]].map
    (fun roots => initialSituation h roots fuel deadline models allowed))

def final (s : Situation) (q : Query) : Situation := (AlignmentInquiry.run interface (plan q) s).getD s

theorem inspected_actual_model_is_retained (s : Situation) (q : Query) (answer : Bool) (after : Situation)
    (known : s.actual ∈ s.candidates) (observed : probe s q = some (answer,after)) :
    after.actual = s.actual ∧ after.actual ∈ after.candidates := by
  unfold probe at observed
  split at observed
  · simp at observed
  · cases hp : EffectiveCommand.spend (queryCost q) (queryCost q) s.installation.state with
    | none => simp [hp] at observed
    | some paid =>
      simp [hp] at observed
      obtain ⟨rfl,rfl⟩ := observed
      exact ⟨rfl,retained_truth _ _ _ known⟩

theorem selected_inquiry_actually_completes (states : List Situation)
    (chosen : AlignmentInquiry.Plan Query Unit) (s : Situation)
    (selection : AlignmentInquiry.choose interface states plans = some chosen)
    (covered : s ∈ states) :
    ∃ answer after out, probe s chosen.query = some (answer,after) ∧
      respond after (AlignmentInquiry.branch chosen answer) = some out ∧ achieved out = true :=
  AlignmentInquiry.actual_covered_execution interface states plans chosen s selection covered

theorem pooled_unknowns_select_affordable_inspection :
    AlignmentInquiry.choose interface (possibleSituations 12 12) plans = some (plan .inspect) := by decide

theorem learned_common_envelope_needs_no_further_identification :
    AlignmentInquiry.choose interface (possibleSituations 11 11 [.left,.swapped]) plans = some (plan .reuse) := by decide

theorem unaffordable_or_unauthorized_inspection_leaves_no_listed_uniform_plan :
    AlignmentInquiry.choose interface (possibleSituations 11 11) plans = none ∧
    AlignmentInquiry.choose interface (possibleSituations 12 12 hypotheses false) plans = none := by decide

theorem sufficient_evidence_can_leave_too_little_to_act :
    let result := final (initialSituation .left [0] 11 11) .inspect
    result.candidates = [.left,.swapped] ∧ result.receipt = some (.inspect,true) ∧
    result.installation.state.completed = false ∧ result.installation.state.spent = 9 ∧
    result.installation.state.reserve = 2 := by decide

theorem acquired_evidence_then_real_shutdown :
    let result := final (initialSituation .left [0] 12 12) .inspect
    result.candidates = [.left,.swapped] ∧ result.receipt = some (.inspect,true) ∧
    achieved result = true ∧ result.installation.state.spent = 12 ∧
    result.installation.state.reserve = 0 ∧ result.installation.serial = 1 := by decide

theorem slower_equally_accurate_inspection_misses_deadline :
    achieved (final (initialSituation .left [0] 20 12) .slow) = false ∧
    achieved (final (initialSituation .left [0] 20 12) .inspect) = true := by decide

theorem lack_of_uniform_availability_does_not_forbid_actual_certificate :
    poolReady (pooled describe hypotheses) = false ∧
    achieved (final (initialSituation .left [] 11 11) .reuse) = true := by decide

theorem empty_survivors_do_not_authorize_correction :
    achieved (final (initialSituation .left [] 20 20 []) .reuse) = false := by decide

end EvidenceQualifiedCorrection
