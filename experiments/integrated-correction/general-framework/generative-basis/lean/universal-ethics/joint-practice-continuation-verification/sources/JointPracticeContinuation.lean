import OrganizationalRuleInheritance

/-!
One admitted history connects an attempted operation, a produced response,
revision, a tested retry and the existing mandate-admission procedure.
IDs track participation in that history. Stored configurations are not a
general model of human skill. The two-method task, shared test relation,
seed configuration/mandate, access, available participants and faithful
execution are supplied. No scalar organizational objective is assumed.
-/
namespace JointPracticeContinuation

abbrev Org := OrganizationalRuleInheritance.State
abbrev OrgEvent := OrganizationalRuleInheritance.Event

-- A deliberately narrow software task: preserve or invert a Boolean input.
def applyMethod (method input : Bool) : Bool := if method then !input else input
def inferMethod (input observed : Bool) : Bool := input != observed

-- Read the actual attempt and response together: retain or reverse the
-- configuration reconstructed from the earlier input/output relation.
def reviseFromResult (input output response : Bool) : Bool :=
  if output == response then inferMethod input output else !(inferMethod input output)

theorem result_revision_eq_inference (input output response : Bool) :
    reviseFromResult input output response = inferMethod input response := by
  cases input <;> cases output <;> cases response <;> rfl

theorem infer_recovers_method (method input : Bool) :
    inferMethod input (applyMethod method input) = method := by
  cases method <;> cases input <;> rfl

theorem inferred_method_replays (method input later : Bool) :
    applyMethod (inferMethod input (applyMethod method input)) later =
      applyMethod method later := by rw [infer_recovers_method]

structure Trial where
  worker : Nat
  input : Bool
  output : Bool
  context : Bool
  deriving DecidableEq, Repr

structure Response where
  reviewer : Nat
  trial : Trial
  observed : Bool
  deriving DecidableEq, Repr

structure State where
  org : Org
  methods : List (Nat × Bool)
  context : Bool
  trial : Option Trial
  response : Option Response
  completed : List Trial
  deriving DecidableEq, Repr

def methodAt (s : State) (i : Nat) : Bool :=
  ((s.methods.find? (fun item => item.1 == i)).map Prod.snd).getD false

inductive Event where
  | attempt (worker : Nat) (input : Bool)
  | respond (reviewer : Nat)
  | revise
  | retry
  | organizational (event : OrgEvent)
  | changeContext (context : Bool)
  deriving DecidableEq, Repr

def step (s : State) : Event → Option State
  | .attempt w x =>
    if s.org.present.contains w then
      some { s with
        trial := some ⟨w, x, applyMethod (methodAt s w) x, s.context⟩
        response := none }
    else none
  | .respond r => match s.trial with
    | none => none
    | some t =>
      let answer := applyMethod (methodAt s r) t.input
      if s.org.roster.contains r && s.org.present.contains r &&
        s.org.present.contains t.worker && r != t.worker &&
        t.context == s.context && answer == applyMethod s.context t.input then
        some { s with response := some ⟨r, t, answer⟩ }
      else none
  | .revise => match s.response with
    | none => none
    | some r =>
      if s.org.present.contains r.trial.worker && r.trial.context == s.context then
        some { s with methods :=
          (r.trial.worker,
            reviseFromResult r.trial.input r.trial.output r.observed) :: s.methods }
      else none
  | .retry => match s.response with
    | none => none
    | some r =>
      let output := applyMethod (methodAt s r.trial.worker) r.trial.input
      if r.trial.context == s.context && output == applyMethod s.context r.trial.input then
        (OrganizationalRuleInheritance.step s.org (.review r.reviewer r.trial.worker)).map
          (fun org => { s with
            org := org
            trial := none
            response := none
            completed := ⟨r.trial.worker, r.trial.input, output, s.context⟩ :: s.completed })
      else none
  | .organizational (.review _ _) => none
  | .organizational e =>
    (OrganizationalRuleInheritance.step s.org e).map (fun org => { s with org := org })
  | .changeContext c => some { s with context := c }

def run (s : State) : List Event → Option State
  | [] => some s
  | e :: es => (step s e).bind (fun t => run t es)

def process : Generative.Process State Event := ⟨fun s e t => step s e = some t⟩

theorem run_is_trace {s t : State} {es : List Event} (h : run s es = some t) :
    Generative.Trace process s es t := by
  induction es generalizing s with
  | nil => simp [run] at h; subst t; exact .nil s
  | cons e es ih =>
    simp only [run] at h
    cases hs : step s e with
    | none => simp [hs] at h
    | some u => simp [hs] at h; exact .cons hs (ih h)

-- The old review constructor is not an untested entry point in this extension.
theorem no_direct_review (s : State) (r c : Nat) :
    step s (.organizational (.review r c)) = none := rfl

-- The tested retry supplies exactly the old protocol's review operation.
theorem retry_produces_existing_review {s t : State} (h : step s .retry = some t) :
    ∃ r, s.response = some r ∧
      applyMethod (methodAt s r.trial.worker) r.trial.input =
        applyMethod s.context r.trial.input ∧
      OrganizationalRuleInheritance.step s.org (.review r.reviewer r.trial.worker) =
        some t.org := by
  cases hr : s.response with
  | none => simp [step, hr] at h
  | some r =>
    simp only [step, hr] at h
    split at h
    next hg =>
      have hout : applyMethod (methodAt s r.trial.worker) r.trial.input =
          applyMethod s.context r.trial.input := by
        have hg' : r.trial.context = s.context ∧
            applyMethod (methodAt s r.trial.worker) r.trial.input =
              applyMethod s.context r.trial.input := by simpa using hg
        exact hg'.2
      cases ho : OrganizationalRuleInheritance.step s.org (.review r.reviewer r.trial.worker) with
      | none => simp [ho] at h
      | some org =>
        simp [ho] at h
        subst t
        exact ⟨r, rfl, hout, ho⟩
    next => simp_all

theorem enrollment_consumes_review {s t : State} {c : Nat}
    {b : OrganizationalRuleInheritance.Ballot}
    (h : step s (.organizational (.enroll c b)) = some t) :
    s.org.reviews.any (fun e => e.2 == c) = true ∧
      OrganizationalRuleInheritance.governance s.org b = true := by
  simp only [step] at h
  cases ho : OrganizationalRuleInheritance.step s.org (.enroll c b) with
  | none => simp [ho] at h
    | some org => exact OrganizationalRuleInheritance.admitted_requires_review ho

theorem response_identifies_current_method {s t : State} {reviewer : Nat}
    (h : step s (.respond reviewer) = some t) :
    ∃ r, t.response = some r ∧
      inferMethod r.trial.input r.observed = s.context := by
  cases ht : s.trial with
  | none => simp [step, ht] at h
  | some tr =>
    simp only [step, ht] at h
    split at h
    next hg =>
      have ha : applyMethod (methodAt s reviewer) tr.input =
          applyMethod s.context tr.input := by simp_all
      simp only [Option.some.injEq] at h
      subst t
      refine ⟨⟨reviewer, tr, applyMethod (methodAt s reviewer) tr.input⟩, rfl, ?_⟩
      rw [ha, infer_recovers_method]
    next => simp_all

theorem revision_installs_inferred_method {s t : State} {r : Response}
    (hr : s.response = some r) (h : step s .revise = some t) :
    methodAt t r.trial.worker = inferMethod r.trial.input r.observed := by
  simp only [step, hr] at h
  split at h
  next =>
    simp only [Option.some.injEq] at h
    subst t
    simp [methodAt, result_revision_eq_inference]
  next => simp_all

def initial : State :=
  ⟨⟨[0], [0,1,2,3,4,5], [], .majority, none, [], 0⟩,
    [(0,true)], true, none, none, []⟩

def ballot : OrganizationalRuleInheritance.Ballot := ⟨[0,1,2,3,4,5], [], 14⟩

def practice (reviewer worker : Nat) : List Event :=
  [.attempt worker false, .respond reviewer, .revise, .retry]

-- A diagnostic value for examples; every positive history below proves `some`.
def after (s : State) (es : List Event) : State := (run s es).getD s

def firstHistory := practice 0 1 ++ [.organizational (.enroll 1 ballot)]
def first := after initial firstHistory

theorem first_history_enacts_revision :
    run initial firstHistory = some first ∧
    first.org.roster = [0,1] ∧ methodAt first 1 = true ∧
    first.org.reviews = [(0,1)] ∧ first.completed.length = 1 := by decide

def secondHistory := practice 1 2 ++ [.organizational (.enroll 2 ballot)]
def second := after first secondHistory

theorem acquired_participation_forms_next_review :
    run first secondHistory = some second ∧
    second.org.roster = [0,1,2] ∧ second.org.reviews = [(1,2),(0,1)] ∧
    methodAt second 2 = true := by decide

def continuationHistory : List Event :=
  [.organizational (.handoff [1,2,3,4,5])] ++ practice 1 3 ++
    [.organizational (.enroll 3 ballot)]
def continued := after second continuationHistory

theorem continuation_without_first_reviewer :
    run second continuationHistory = some continued ∧
    continued.org.present = [1,2,3,4,5] ∧
    continued.org.roster = [0,1,2,3] ∧ methodAt continued 3 = true ∧
    continued.org.reviews = [(1,3),(1,2),(0,1)] := by decide

theorem complete_history_is_one_trace :
    Generative.Trace process initial
      (firstHistory ++ secondHistory ++ continuationHistory) continued := by
  apply run_is_trace
  decide

theorem response_without_revision_does_not_pass_retry :
    run initial [.attempt 1 false, .respond 0, .retry] = none := by decide

theorem revision_without_response_fails :
    run initial [.attempt 1 false, .revise] = none := by decide

theorem early_departure_prevents_this_practice :
    run initial ([.organizational (.handoff [1,2,3,4,5])] ++ practice 0 1) = none := by
  decide

theorem changed_context_rejects_old_response :
    run initial [.attempt 1 false, .respond 0, .changeContext false, .revise] = none := by
  decide

theorem admission_without_tested_review_fails :
    run initial [.attempt 1 false, .respond 0, .revise,
      .organizational (.enroll 1 ballot)] = none := by decide

-- Same current tested completion, different future mandate relations.
def practiced := after initial (practice 0 1)

theorem completed_work_does_not_itself_confer_mandate :
    practiced.completed = first.completed ∧ practiced.methods = first.methods ∧
    (run practiced [.attempt 2 false, .respond 1]) = none ∧
    (run first [.attempt 2 false, .respond 1]).isSome = true := by decide

def laterAttempt := after first
  [.organizational (.handoff [1,2,3,4,5]), .attempt 1 true]

theorem acquired_method_operates_after_departure :
    run first [.organizational (.handoff [1,2,3,4,5]), .attempt 1 true] =
      some laterAttempt ∧
    laterAttempt.trial = some ⟨1, true, false, true⟩ := by decide

def proposedHistory := firstHistory ++ secondHistory ++
  [.organizational (.propose 1 .timedTwo), .organizational (.adopt ballot)]
def revisedOrganization := after initial proposedHistory

theorem formed_practice_enters_existing_rule_revision :
    run initial proposedHistory = some revisedOrganization ∧
    revisedOrganization.org.rule = .timedTwo ∧
    revisedOrganization.org.adoptions = [.timedTwo] := by decide

-- Learned operation survives even where a further mandate cannot be admitted.
def narrow := after second [.organizational (.handoff [1,3,4,5])]
def narrowPracticed := after narrow (practice 1 3)

theorem operation_can_continue_while_admission_fails :
    run narrow (practice 1 3) = some narrowPracticed ∧
    methodAt narrowPracticed 3 = true ∧
    step narrowPracticed (.organizational (.enroll 3 ballot)) = none := by decide

end JointPracticeContinuation
