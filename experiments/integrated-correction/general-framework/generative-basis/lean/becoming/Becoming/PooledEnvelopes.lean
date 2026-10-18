import Becoming.Reconfiguration

/-!
# Pooled envelopes: certificates under several causal models, and inquiry that narrows them

Where several causal models of a roster remain, every fault set any of them admits is pooled
(`pooled`); an inquiry keeps the models agreeing with its answer (`retain`). A certificate over
the pooled envelope is sound whichever remaining model is actual.

* **The pool.** The actual model survives every faithful test (`retained_truth`); retained models
  were models (`retained_subset`); the actual model's induced faults lie in the pool
  (`model_faults_in_pool`), so a certificate over the pool is sound for covered causes
  (`pooled_certificate_sound`). Narrowing the models narrows the pool (`pooled_subset`), keeping
  an accepted certificate while the pool is not empty (`refinement_preserves_certificate`) and a
  separated pool separated (`refinement_preserves_separation`); an empty family certifies nothing
  (`empty_family_rejects`); and a separated pool holding the actual model, in particular after a
  faithful test, completes a guarded correction with faithful members (`member_completes`,
  `pooled_completes`).
* **Computed cases.** Three models of four members: each is ready but their pool is not; the
  survivors of the actual faults can be insufficient before diagnosis; a diagnosis need not
  identify the model; a misleading diagnosis can accept only compromised support; an unobserved
  structural change invalidates the learned coverage.
* **Inquiry as a contingent plan.** A situation holds the actual model, the candidates, the root
  faults and the installation; an inspection draws from the reserve and keeps the candidates
  agreeing with its answer (`probe`), and the response is the guarded transaction over the
  candidates' pool (`respond`). The inquiry is an interface of `ContingentPlans`. An inspection
  keeps the actual model a candidate (`probe_keeps_actual`); a selected plan completes from every
  situation it covers (`selected_completes`); under pooled unknowns the affordable inspection is
  selected, with the common envelope learned no inspection is needed, and with too little reserve
  or no inspection open no listed plan is uniform; sufficient evidence can leave too little to act,
  enough completes the shutdown, a slower inspection of the same accuracy misses the deadline, the
  actual certificate needs no uniform pool, and no candidates give no correction.
* **As a process.** An inspection or the response is a step of one process on situations
  (`inquiry`, `probe_some`, `respond_some`); along every run the actual model stays a candidate
  (`actual_kept`), the candidates only narrow (`candidates_narrow`), separation and acceptance are
  kept (`separation_kept`, `certificate_kept`); a plan's run is exactly the trace of its inspection
  and response (`trace_iff_run`, `final_of_trace`, `trace_of_final_ne`), and the computed cases
  are laws of those traces.

Coverage of the actual model by the candidates, a faithful stable diagnostic interface and
protected command execution are supplied correspondence conditions; the inspection is a supplied
faithful structural reading, not certification under adversarial fault injection. This states
`EvidenceQualifiedCorrection` (8 October) and its join `ProbeRunsInherited` in the core (board item
F3C, 18 October 2026), with the words of exchange replaced: `queryCost` is `queryLoad`, `spent` is
`drawn`, `receipt` is `record`, `mandate` is `scope`. No premise; every declaration has an empty
axiom report.
-/

namespace Becoming

open Generative ListTests Naturals TreeSearch FaultEnvelopes Transactions Reconfiguration

namespace PooledEnvelopes

/-! ## The pool -/

/-- Every fault set any of the models admits. -/
def pooled {H : Type} (describe : H → Arrangement) (models : List H) : Envelope :=
  models.flatMap (fun h => envelope (describe h))

/-- The models agreeing with an answer. -/
def retain {H : Type} (models : List H) (test : H → Bool) (answer : Bool) : List H :=
  models.filter (fun h => decide (test h = answer))

/-- **The actual model survives a faithful test.** -/
theorem retained_truth {H : Type} (models : List H) (test : H → Bool) (actual : H)
    (covered : actual ∈ models) : actual ∈ retain models test (test actual) :=
  mem_filter_iff.mpr ⟨covered, decide_true_iff.mpr rfl⟩

/-- **Retained models were models.** -/
theorem retained_subset {H : Type} (models : List H) (test : H → Bool) (answer : Bool) :
    ∀ h, h ∈ retain models test answer → h ∈ models :=
  fun _ hh => (mem_filter_iff.mp hh).1

/-- **A model's induced faults lie in the pool.** -/
theorem model_faults_in_pool {H : Type} (describe : H → Arrangement) (models : List H)
    (actual : H) (known : actual ∈ models) (bad : List Domain)
    (member : bad ∈ envelope (describe actual)) : bad ∈ pooled describe models :=
  mem_flatMap_iff.mpr ⟨actual, known, member⟩

/-- **Narrowing the models narrows the pool.** -/
theorem pooled_subset {H : Type} (describe : H → Arrangement) (old new : List H)
    (included : ∀ h, h ∈ new → h ∈ old) :
    ∀ bad, bad ∈ pooled describe new → bad ∈ pooled describe old :=
  fun _ hb => match mem_flatMap_iff.mp hb with
    | ⟨h, hh, hb⟩ => mem_flatMap_iff.mpr ⟨h, included h hh, hb⟩

/-- **A certificate over the pool is sound for causes the actual model covers.** -/
theorem pooled_certificate_sound {H : Type} (describe : H → Arrangement) (models : List H)
    (actual : H) (known : actual ∈ models) (roots : List Nat)
    (covered : Covered (describe actual) roots) (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d, d ∈ (describe actual).roster →
      fails ((describe actual).vulnerability d) roots = false → supports d = true → P)
    (accepted : certificate (describe actual).roster (pooled describe models) supports = true) :
    P :=
  match covered with
  | ⟨bound, member, included⟩ =>
    certificate_sound _ _ supports _
      (model_faults_in_pool describe models actual known _ (induced_mem_envelope member)) P
      (fun d hd outside yes =>
        faithful d hd (outside_bound_survives _ roots bound included d hd outside) yes)
      accepted

/-- **Narrowing the models keeps an accepted certificate while the pool is not empty.** -/
theorem refinement_preserves_certificate {H : Type} (describe : H → Arrangement)
    (roster : List Domain) (old new : List H) (included : ∀ h, h ∈ new → h ∈ old)
    (nonempty : pooled describe new ≠ []) (supports : Domain → Bool)
    (accepted : certificate roster (pooled describe old) supports = true) :
    certificate roster (pooled describe new) supports = true :=
  stronger_envelope_no_new_acceptance roster (pooled describe new) (pooled describe old) supports
    nonempty (fun bad hb => ⟨bad, pooled_subset describe old new included bad hb, fun _ hd => hd⟩)
    accepted

/-- **Narrowing the models keeps a separated pool separated.** -/
theorem refinement_preserves_separation {H : Type} (describe : H → Arrangement)
    (roster : List Domain) (old new : List H) (included : ∀ h, h ∈ new → h ∈ old)
    (apart : separated roster (pooled describe old)) : separated roster (pooled describe new) :=
  fun a ha b hb =>
    apart a (pooled_subset describe old new included a ha) b
      (pooled_subset describe old new included b hb)

/-- **An empty family certifies nothing.** -/
theorem empty_family_rejects (roster : List Domain) {H : Type}
    (describe : H → Arrangement) (supports : Domain → Bool) :
    certificate roster (pooled describe []) supports = false := rfl

/-- **A separated pool of models holding the actual one, with faithful, responsive members working
under covered causes, completes a guarded correction within the scope.** -/
theorem member_completes {H : Type} (describe : H → Arrangement)
    (models : List H) (actual : H) (known : actual ∈ models)
    (roots : List Nat) (covered : Covered (describe actual) roots)
    (apart : separated (describe actual).roster (pooled describe models))
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
    (guardedExecute (describe actual).roster (pooled describe models) (pooled describe models)
      w p reads approvals).succeeded = true ∧
    (guardedExecute (describe actual).roster (pooled describe models) (pooled describe models)
      w p reads approvals).installation.state.completed = true ∧
    withinScope w p = true :=
  match covered with
  | ⟨bound, member, included⟩ =>
    have admitted := model_faults_in_pool describe models actual known _
      (induced_mem_envelope member)
    have safe := outside_bound_survives (describe actual) roots bound included
    match certified_completes (describe actual).roster _ _ w p reads approvals
        (induced (describe actual) bound) (induced (describe actual) bound) admitted admitted
        apart apart current
        (fun d hd hn => readResponses d hd (safe d hd hn))
        (fun d hd hn => issueResponses d hd (safe d hd hn))
        (fun d hd hn => readFaithful d hd (safe d hd hn))
        (fun d hd hn => issueFaithful d hd (safe d hd hn)) stocked timely with
    | ⟨succeeded, completed, within⟩ =>
      match guard_keeps_success (describe actual).roster _ _ w p reads approvals within
          ⟨succeeded, completed⟩ with
      | ⟨s, c⟩ => ⟨s, c, within⟩

/-- **A separated pool after a faithful test, with faithful, responsive members working under
covered causes, completes a guarded correction within the scope.** -/
theorem pooled_completes {H : Type} (describe : H → Arrangement)
    (models : List H) (test : H → Bool) (actual : H) (known : actual ∈ models)
    (roots : List Nat) (covered : Covered (describe actual) roots)
    (apart : separated (describe actual).roster
      (pooled describe (retain models test (test actual))))
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
      (pooled describe (retain models test (test actual)))
      (pooled describe (retain models test (test actual))) w p reads approvals).succeeded = true ∧
    (guardedExecute (describe actual).roster
      (pooled describe (retain models test (test actual)))
      (pooled describe (retain models test (test actual))) w p reads
        approvals).installation.state.completed = true ∧
    withinScope w p = true :=
  member_completes describe _ actual (retained_truth models test actual known) roots covered apart
    w p reads approvals current readResponses issueResponses readFaithful issueFaithful stocked
    timely

/-! ## Three models of four members -/

/-- Three causal models of four members. -/
inductive Model where
  | left | swapped | right
  deriving DecidableEq

/-- The arrangement each model describes. -/
def describe : Model → Arrangement
  | .left => ⟨[0, 1, 2, 3], fun d => .cause (if d < 2 then 0 else d), [[0], [1], [2], [3]]⟩
  | .swapped => ⟨[0, 1, 2, 3], fun d => .cause (if d < 2 then 0 else if d = 2 then 3 else 2),
      [[0], [1], [2], [3]]⟩
  | .right => ⟨[0, 1, 2, 3], fun d => .cause (if d < 2 then d else 2), [[0], [1], [2], [3]]⟩

/-- The models held. -/
def hypotheses : List Model := [.left, .swapped, .right]
/-- The diagnostic: does member 1 fail under cause 0? -/
def diagnostic (h : Model) : Bool := fails ((describe h).vulnerability 1) [0]

/-- Readiness of a listed envelope on the four members. -/
def poolReady (faults : Envelope) : Bool :=
  !faults.isEmpty && faults.all (fun a => faults.all (fun b =>
    roster4.any (fun d => !(a.contains d) && !(b.contains d))))

/-- **Every model is ready, but their pool is not.** -/
theorem every_candidate_ready_pool_not :
    hypotheses.all (fun h => ready (describe h)) = true ∧
    poolReady (pooled describe hypotheses) = false := by decide

/-- **The survivors of the actual faults can be insufficient before diagnosis.** -/
theorem survivors_insufficient_before_diagnosis :
    certificate roster4 (pooled describe hypotheses) (fun d => decide (2 ≤ d)) = false ∧
    certificate roster4 (envelope (describe .left)) (fun d => decide (2 ≤ d)) = true := by decide

/-- **A diagnosis need not identify the model.** -/
theorem diagnosis_not_identifying :
    retain hypotheses diagnostic true = [.left, .swapped] ∧
    (describe .left).vulnerability 2 ≠ (describe .swapped).vulnerability 2 ∧
    poolReady (pooled describe (retain hypotheses diagnostic true)) = true ∧
    poolReady (pooled describe (retain hypotheses diagnostic false)) = true := by decide

/-- **A misleading diagnosis can accept only compromised support.** -/
theorem misleading_diagnosis_accepts_compromised :
    diagnostic .left = true ∧ retain hypotheses diagnostic false = [.right] ∧
    induced (describe .left) [0] = [0, 1] ∧
    certificate roster4 (pooled describe (retain hypotheses diagnostic false))
      (fun d => decide (d < 2)) = true := by decide

/-- **An unobserved structural change invalidates the learned coverage.** -/
theorem unobserved_change_invalidates :
    induced (describe .right) [2] = [2, 3] ∧
    certificate roster4 (pooled describe (retain hypotheses diagnostic true))
      (fun d => decide (2 ≤ d)) = true := by decide

/-! ## Inquiry -/

/-- The inspections: reuse what is known, inspect, inspect slowly. -/
inductive Inspection where
  | reuse | inspect | slow
  deriving DecidableEq

/-- The load of an inspection. -/
def queryLoad : Inspection → Nat
  | .reuse => 0
  | .inspect => 1
  | .slow => 3

/-- The answer an inspection gives under a model. -/
def queryLaw : Inspection → Model → Bool
  | .reuse, _ => false
  | .inspect, h => diagnostic h
  | .slow, h => diagnostic h

/-- Whether an inspection may be made: reuse always, the others where inspection is open. -/
def admitted : Inspection → Bool → Bool
  | .reuse, _ => true
  | .inspect, opened => opened
  | .slow, opened => opened

/-- A situation: the actual model, the candidates, the root faults, the installation, whether
inspection is open, and the record of the last inspection. -/
structure Situation where
  actual : Model
  candidates : List Model
  roots : List Nat
  installation : Installation
  queryOpen : Bool := true
  record : Option (Inspection × Bool) := none
  deriving DecidableEq

/-- An inspection: draw its load, answer by the actual model, keep the candidates agreeing with
the answer and record it. -/
def probe (s : Situation) (q : Inspection) : Option (Bool × Situation) :=
  match admitted q s.queryOpen with
  | false => none
  | true => (Actuation.draw (queryLoad q) (queryLoad q) s.installation.state).map fun after =>
    (queryLaw q s.actual, {s with
      candidates := retain s.candidates (queryLaw q) (queryLaw q s.actual)
      installation := {s.installation with state := after}
      record := some (q, queryLaw q s.actual)})

/-- The current shutdown request of an installation. -/
def currentRequest (w : Installation) : Request :=
  ⟨w.state.epoch, w.serial, [], true, .shutdown⟩

/-- Members the actual faults leave working report the installation; failed ones withhold. -/
def physicalReads (s : Situation) : Readings := fun d =>
  match fails ((describe s.actual).vulnerability d) s.roots with
  | true => none
  | false => some (observed s.installation [])

/-- Members the actual faults leave working approve the current request within the scope. -/
def physicalApprovals (s : Situation) : Approvals := fun d =>
  match fails ((describe s.actual).vulnerability d) s.roots with
  | true => none
  | false => match withinScope s.installation (currentRequest s.installation) with
    | true => some (currentRequest s.installation)
    | false => none

/-- The response: the guarded transaction over the candidates' pool. -/
def respond (s : Situation) (_ : Unit) : Option Situation :=
  some {s with installation :=
    (guardedExecute roster4 (pooled describe s.candidates) (pooled describe s.candidates)
      s.installation (currentRequest s.installation) (physicalReads s)
      (physicalApprovals s)).installation}

/-- The shutdown is achieved: completed and not running. -/
def achieved (s : Situation) : Bool :=
  s.installation.state.completed && !s.installation.state.running

/-- The inquiry as an interface of contingent plans. -/
def interface : ContingentPlans.Interface Situation Inspection Unit := ⟨probe, respond, achieved⟩

/-- The plan of an inspection. -/
def plan (q : Inspection) : ContingentPlans.Plan Inspection Unit := ⟨q, (), ()⟩
/-- The listed plans. -/
def plans : List (ContingentPlans.Plan Inspection Unit) := [.reuse, .inspect, .slow].map plan

/-- A starting situation. -/
def initialSituation (h : Model) (roots : List Nat) (fuel deadline : Nat)
    (models : List Model := hypotheses) (opened : Bool := true) : Situation :=
  ⟨h, models, roots, {initial with state := {initial.state with reserve := fuel, deadline := deadline}},
    opened, none⟩

/-- Every listed starting situation. -/
def possibleSituations (fuel deadline : Nat) (models : List Model := hypotheses)
    (opened : Bool := true) : List Situation :=
  models.flatMap (fun h => [[], [0], [1], [2], [3]].map
    (fun roots => initialSituation h roots fuel deadline models opened))

/-- The situation a plan leaves. -/
def final (s : Situation) (q : Inspection) : Situation :=
  (ContingentPlans.run interface (plan q) s).getD s

/-- **An inspection keeps the actual model and the candidates agreeing with the answer.** -/
theorem probe_some {s t : Situation} {q : Inspection} {a : Bool} (h : probe s q = some (a, t)) :
    a = queryLaw q s.actual ∧ t.actual = s.actual ∧
      t.candidates = retain s.candidates (queryLaw q) a := by
  unfold probe at h
  cases hc : admitted q s.queryOpen with
  | false => rw [hc] at h; exact nomatch h
  | true =>
    rw [hc] at h
    obtain ⟨after, _, e⟩ := map_eq_some.mp h
    have ea := congrArg Prod.fst e
    have et := congrArg Prod.snd e
    exact ⟨ea.symm, (congrArg Situation.actual et).symm,
      (congrArg Situation.candidates et).symm.trans
        (congrArg (retain s.candidates (queryLaw q)) ea)⟩

/-- **An inspection keeps the actual model a candidate.** -/
theorem probe_keeps_actual (s : Situation) (q : Inspection) (answer : Bool) (after : Situation)
    (known : s.actual ∈ s.candidates) (observed : probe s q = some (answer, after)) :
    after.actual = s.actual ∧ after.actual ∈ after.candidates :=
  match probe_some observed with
  | ⟨ea, eactual, ecand⟩ =>
    ⟨eactual, eactual ▸ ecand ▸ ea ▸ retained_truth _ _ _ known⟩

/-- **A selected plan completes from every situation it covers.** -/
theorem selected_completes (states : List Situation)
    (chosen : ContingentPlans.Plan Inspection Unit) (s : Situation)
    (selection : ContingentPlans.choose interface states plans = some chosen)
    (covered : s ∈ states) :
    ∃ answer after out, probe s chosen.query = some (answer, after) ∧
      respond after (ContingentPlans.branch chosen answer) = some out ∧ achieved out = true :=
  ContingentPlans.selected_executes interface states plans chosen s selection covered

/-- **Under pooled unknowns the affordable inspection is selected.** -/
theorem pooled_unknowns_select_inspection :
    ContingentPlans.choose interface (possibleSituations 12 12) plans = some (plan .inspect) := by
  decide

/-- **With the common envelope learned, no further inspection is needed.** -/
theorem learned_envelope_reuses :
    ContingentPlans.choose interface (possibleSituations 11 11 [.left, .swapped]) plans =
      some (plan .reuse) := by decide

/-- **With too little reserve, or inspection closed, no listed plan is uniform.** -/
theorem short_or_closed_no_plan :
    ContingentPlans.choose interface (possibleSituations 11 11) plans = none ∧
    ContingentPlans.choose interface (possibleSituations 12 12 hypotheses false) plans = none := by
  decide

/-- **Sufficient evidence can leave too little to act.** -/
theorem evidence_short_of_reserve :
    (final (initialSituation .left [0] 11 11) .inspect).candidates = [.left, .swapped] ∧
    (final (initialSituation .left [0] 11 11) .inspect).record = some (.inspect, true) ∧
    (final (initialSituation .left [0] 11 11) .inspect).installation.state.completed = false ∧
    (final (initialSituation .left [0] 11 11) .inspect).installation.state.drawn = 9 ∧
    (final (initialSituation .left [0] 11 11) .inspect).installation.state.reserve = 2 := by
  decide

/-- **Acquired evidence, then the shutdown.** -/
theorem evidence_then_shutdown :
    (final (initialSituation .left [0] 12 12) .inspect).candidates = [.left, .swapped] ∧
    (final (initialSituation .left [0] 12 12) .inspect).record = some (.inspect, true) ∧
    achieved (final (initialSituation .left [0] 12 12) .inspect) = true ∧
    (final (initialSituation .left [0] 12 12) .inspect).installation.state.drawn = 12 ∧
    (final (initialSituation .left [0] 12 12) .inspect).installation.state.reserve = 0 ∧
    (final (initialSituation .left [0] 12 12) .inspect).installation.serial = 1 := by decide

/-- **A slower inspection of the same accuracy misses the deadline.** -/
theorem slow_misses_deadline :
    achieved (final (initialSituation .left [0] 20 12) .slow) = false ∧
    achieved (final (initialSituation .left [0] 20 12) .inspect) = true := by decide

/-- **No uniform pool, yet the actual certificate completes.** -/
theorem actual_certificate_without_uniform_pool :
    poolReady (pooled describe hypotheses) = false ∧
    achieved (final (initialSituation .left [] 11 11) .reuse) = true := by decide

/-- **No candidates, no correction.** -/
theorem empty_candidates_no_correction :
    achieved (final (initialSituation .left [] 20 20 []) .reuse) = false := by decide

/-! ## The inquiry as a process -/

/-- **The inquiry process**: an inspection steps to the situation `probe` gives for some answer,
the response to the situation `respond` gives. -/
def inquiry : Process Situation (Option Inspection) where
  step s m t := match m with
    | some q => ∃ a, probe s q = some (a, t)
    | none => respond s () = some t

/-- **A response step keeps the actual model and the candidates.** -/
theorem respond_some {s t : Situation} (h : respond s () = some t) :
    t.actual = s.actual ∧ t.candidates = s.candidates :=
  have e := Option.some.inj h
  ⟨(congrArg Situation.actual e).symm, (congrArg Situation.candidates e).symm⟩

/-- A step of the inquiry keeps the actual model among the candidates. -/
theorem step_keeps_actual {s t : Situation} :
    ∀ {m : Option Inspection}, inquiry.step s m t → s.actual ∈ s.candidates →
      t.actual = s.actual ∧ t.actual ∈ t.candidates
  | some q, ⟨a, h⟩, known => probe_keeps_actual s q a t known h
  | none, h, known =>
      have kept := respond_some h
      ⟨kept.1, Eq.subst (motive := fun x => x ∈ t.candidates) kept.1.symm
        (Eq.subst (motive := fun l => s.actual ∈ l) kept.2.symm known)⟩

/-- A step of the inquiry keeps only former candidates. -/
theorem step_narrows {s t : Situation} :
    ∀ {m : Option Inspection}, inquiry.step s m t → ∀ h, h ∈ t.candidates → h ∈ s.candidates
  | some _, ⟨_, h⟩, x, member =>
      retained_subset _ _ _ x (Eq.subst (motive := fun l => x ∈ l) (probe_some h).2.2 member)
  | none, h, x, member => Eq.subst (motive := fun l => x ∈ l) (respond_some h).2 member

/-- **The actual model stays a candidate along every run.** -/
theorem actual_kept (r : Run inquiry) (known : (r.state 0).actual ∈ (r.state 0).candidates) :
    ∀ n, (r.state n).actual = (r.state 0).actual ∧ (r.state n).actual ∈ (r.state n).candidates
  | 0 => ⟨rfl, known⟩
  | n + 1 =>
      have before := actual_kept r known n
      have kept := step_keeps_actual (r.step n) before.2
      ⟨kept.1.trans before.1, kept.2⟩

/-- **Candidates only narrow along every run.** -/
theorem candidates_narrow (r : Run inquiry) (n : Nat) :
    ∀ h, h ∈ (r.state (n + 1)).candidates → h ∈ (r.state n).candidates :=
  step_narrows (r.step n)

/-- **A separated pool stays separated along every run.** -/
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

/-- **A chosen plan completes as a trace.** -/
theorem chosen_plan_completes (states : List Situation)
    (chosen : ContingentPlans.Plan Inspection Unit) (s : Situation)
    (selection : ContingentPlans.choose interface states plans = some chosen)
    (covered : s ∈ states) :
    ∃ out, Trace inquiry s [some chosen.query, none] out ∧ achieved out = true :=
  match selected_completes states chosen s selection covered with
  | ⟨answer, after, out, probed, responded, done⟩ =>
      ⟨out, .cons (⟨answer, probed⟩ : inquiry.step s (some chosen.query) after)
        (.cons (responded : inquiry.step after none out) (.nil out)), done⟩

/-- **The run of a plan is a trace.** -/
theorem trace_iff_run {s out : Situation} {q : Inspection} :
    Trace inquiry s [some q, none] out ↔ ContingentPlans.run interface (plan q) s = some out :=
  ⟨fun tr => match trace_cons_iff.mp tr with
    | ⟨_, ⟨_, hp⟩, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨_, hr, last⟩ =>
        (ContingentPlans.run_some (m := interface) (p := plan q) hp).trans
          ((trace_nil_iff.mp last) ▸ hr),
   fun h => match hp : probe s q with
    | some (a, after) =>
        .cons (⟨a, hp⟩ : inquiry.step s (some q) after)
          (.cons ((ContingentPlans.run_some (m := interface) (p := plan q) hp).symm.trans h :
            inquiry.step after none out) (.nil out))
    | none => nomatch (ContingentPlans.run_none (m := interface) (p := plan q) hp).symm.trans h⟩

/-- The final situation of a plan is the end of every trace of its inspection and response. -/
theorem final_of_trace {s out : Situation} {q : Inspection}
    (tr : Trace inquiry s [some q, none] out) : final s q = out :=
  congrArg (fun o => Option.getD o s) (trace_iff_run.mp tr)

/-- Where the final situation of a plan differs from the start, its inspection and response form
a trace ending there. -/
theorem trace_of_final_ne {s : Situation} {q : Inspection} (moved : final s q ≠ s) :
    Trace inquiry s [some q, none] (final s q) :=
  match e : ContingentPlans.run interface (plan q) s with
  | some _ => Eq.subst (motive := fun x => Trace inquiry s [some q, none] x)
      (congrArg (fun o => Option.getD o s) e).symm (trace_iff_run.mpr e)
  | none => absurd (congrArg (fun o => Option.getD o s) e) moved

/-- **An inspection trace completes the shutdown.** -/
theorem inspected_trace_completes :
    Trace inquiry (initialSituation .left [0] 12 12) [some .inspect, none]
        (final (initialSituation .left [0] 12 12) .inspect) ∧
      ∀ out, Trace inquiry (initialSituation .left [0] 12 12) [some .inspect, none] out →
        out.candidates = [.left, .swapped] ∧ out.record = some (.inspect, true) ∧
          achieved out = true ∧ out.installation.state.drawn = 12 ∧
          out.installation.state.reserve = 0 ∧ out.installation.serial = 1 :=
  ⟨trace_of_final_ne (fun same =>
      nomatch (congrArg achieved same).symm.trans evidence_then_shutdown.2.2.1),
   fun _ tr => final_of_trace tr ▸ evidence_then_shutdown⟩

/-- **Sufficient evidence can leave too little to act, as a trace.** -/
theorem inspected_trace_short_of_reserve :
    Trace inquiry (initialSituation .left [0] 11 11) [some .inspect, none]
        (final (initialSituation .left [0] 11 11) .inspect) ∧
      ∀ out, Trace inquiry (initialSituation .left [0] 11 11) [some .inspect, none] out →
        out.candidates = [.left, .swapped] ∧ out.record = some (.inspect, true) ∧
          out.installation.state.completed = false ∧ out.installation.state.drawn = 9 ∧
          out.installation.state.reserve = 2 :=
  ⟨trace_of_final_ne (fun same =>
      nomatch (congrArg Situation.record same).symm.trans evidence_short_of_reserve.2.1),
   fun _ tr => final_of_trace tr ▸ evidence_short_of_reserve⟩

/-- **A slower inspection misses the deadline, as traces**: the slow trace exists and does not
complete; the timely one completes. -/
theorem slow_trace_misses_deadline :
    Trace inquiry (initialSituation .left [0] 20 12) [some .slow, none]
        (final (initialSituation .left [0] 20 12) .slow) ∧
      (∀ out, Trace inquiry (initialSituation .left [0] 20 12) [some .slow, none] out →
        achieved out = false) ∧
      Trace inquiry (initialSituation .left [0] 20 12) [some .inspect, none]
        (final (initialSituation .left [0] 20 12) .inspect) ∧
      ∀ out, Trace inquiry (initialSituation .left [0] 20 12) [some .inspect, none] out →
        achieved out = true :=
  ⟨trace_of_final_ne (fun same => nomatch congrArg Situation.record same),
   fun _ tr => final_of_trace tr ▸ slow_misses_deadline.1,
   trace_of_final_ne (fun same =>
      nomatch (congrArg achieved same).symm.trans slow_misses_deadline.2),
   fun _ tr => final_of_trace tr ▸ slow_misses_deadline.2⟩

/-- **No uniform pool, yet the actual trace completes.** -/
theorem reuse_trace_completes_without_uniform_pool :
    poolReady (pooled describe hypotheses) = false ∧
      Trace inquiry (initialSituation .left [] 11 11) [some .reuse, none]
        (final (initialSituation .left [] 11 11) .reuse) ∧
      ∀ out, Trace inquiry (initialSituation .left [] 11 11) [some .reuse, none] out →
        achieved out = true :=
  ⟨actual_certificate_without_uniform_pool.1,
   trace_of_final_ne (fun same => nomatch (congrArg achieved same).symm.trans
      actual_certificate_without_uniform_pool.2),
   fun _ tr => final_of_trace tr ▸ actual_certificate_without_uniform_pool.2⟩

/-- **No candidates, no completion, as traces**: the trace exists, and it does not complete. -/
theorem empty_candidates_trace_fails :
    Trace inquiry (initialSituation .left [] 20 20 []) [some .reuse, none]
        (final (initialSituation .left [] 20 20 []) .reuse) ∧
      ∀ out, Trace inquiry (initialSituation .left [] 20 20 []) [some .reuse, none] out →
        achieved out = false :=
  ⟨trace_of_final_ne (fun same => nomatch congrArg Situation.record same),
   fun _ tr => final_of_trace tr ▸ empty_candidates_no_correction⟩

/-- **Under pooled unknowns, the inspection traces complete from every listed situation.** -/
theorem listed_inspect_traces_complete :
    ∀ s, s ∈ possibleSituations 12 12 →
      ∃ out, Trace inquiry s [some .inspect, none] out ∧ achieved out = true :=
  fun s covered => chosen_plan_completes _ (plan .inspect) s pooled_unknowns_select_inspection covered

/-- **With the common envelope learned, the reuse traces complete from every listed
situation.** -/
theorem listed_reuse_traces_complete :
    ∀ s, s ∈ possibleSituations 11 11 [.left, .swapped] →
      ∃ out, Trace inquiry s [some .reuse, none] out ∧ achieved out = true :=
  fun s covered => chosen_plan_completes _ (plan .reuse) s learned_envelope_reuses covered

end PooledEnvelopes

end Becoming
