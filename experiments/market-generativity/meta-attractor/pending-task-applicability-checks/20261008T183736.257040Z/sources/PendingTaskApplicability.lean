import CommonTaskRevision

set_option autoImplicit false

/-!
One activity differentiates acquired understanding, delivered work and its effects.
An endpoint retains a delivered task while checking a relevant condition. The
report must cover the actual effect interval, not only its earlier sampling time.
The check consumes one work unit. Refusal retains work and expenditure; waiting
has no outcome law here and is NOT thereby proved harmless. The supplied two
practice laws, cost law, correspondence and authority remain explicit premises.
-/
namespace PendingTaskApplicability
open GoalFormationRevision CommonTaskRevision CorrectionVersioned

/-- Only the loss condition relevant to this delivered practice. This local
    outcome law is supplied, not a learned universal notion of relevance. -/
def relevantRisk (c : Conditions) (value : Bool) : Bool :=
  if value then c.transitionLoss else c.accessLoss

structure Endpoint where
  learning : State
  requested : Bool
  pending : Bool := true
  reports : List (Option Bool) := []

/-- The actual conditions are used by enactment alone. The decision reads a
    report, which may be absent. Denial or exhausted work retains the task. -/
def reviewAndAct (c : Conditions) (report : Option Bool) (e : Endpoint) : Endpoint :=
  if !e.pending then e else
  match charge 1 e.learning.account with
  | none => e
  | some account =>
    let paid : Endpoint := { e with
      learning := {e.learning with account}
      reports := e.reports ++ [report] }
    if report = some false then
      match enact c paid.learning e.requested with
      | none => paid
      | some learning => {paid with learning, pending := false}
    else paid

/-- This relation concerns evidence coverage at the actual effect. It does not
    require the whole context to remain fixed or infer protection from age. -/
def CoversEffect (c : Conditions) (report : Option Bool) (e : Endpoint) : Prop :=
  ∀ b, report = some b → b = relevantRisk c e.requested

theorem operation_without_relevant_loss (c : Conditions) (l l' : State) (value : Bool)
    (risk : relevantRisk c value = false) (h : enact c l value = some l') :
    l'.losses = l.losses ∧ l'.archive.length = l.archive.length + 1 ∧
      total l'.account = total l.account := by
  cases hc : cycle l.selector (meansFor (bitGoal value)) l.account with
  | none => simp [enact, operate, hc] at h
  | some a =>
    simp [enact, operate, hc] at h
    cases h
    have safe : (perform c (meansFor (bitGoal value))).access &&
        (perform c (meansFor (bitGoal value))).maintenance = true := by
      cases value <;> simp_all [relevantRisk, bitGoal, meansFor, perform]
    exact ⟨by simp [safe], by simp, cycle_conserves hc⟩

theorem funded_operation_exists (c : Conditions) (l : State) (value : Bool)
    (work : 2 ≤ l.account.work) : ∃ l', enact c l value = some l' := by
  by_cases eligible : feedback l.selector (meansFor (bitGoal value)) = 2 ∧
      2 ≤ l.account.reserve
  · simp [enact, operate, cycle, charge, work, eligible]
  · simp [enact, operate, cycle, charge, work, eligible]

/-- The paid check and an actual completed operation need three current units;
    later reimbursement cannot fund the earlier check or the initial act. -/
theorem funded_covered_review (c : Conditions) (l : State) (value : Bool)
    (work : 3 ≤ l.account.work) (risk : relevantRisk c value = false) :
    let e : Endpoint := ⟨l, value, true, []⟩
    let out := reviewAndAct c (some false) e
    out.pending = false ∧ out.learning.losses = l.losses ∧
      out.learning.archive.length = l.archive.length + 1 ∧
      total out.learning.account = total l.account := by
  let a : Account := { l.account with
    work := l.account.work - 1
    spent := l.account.spent + 1 }
  have hc : charge 1 l.account = some a := by
    simp [charge, a, show 1 ≤ l.account.work by omega]
  have wa : 2 ≤ a.work := by dsimp [a]; omega
  obtain ⟨l', he⟩ := funded_operation_exists c {l with account := a} value wa
  have hs := operation_without_relevant_loss c {l with account := a} l' value risk he
  have ht := charge_conserves hc
  simp only [reviewAndAct, Bool.not_true, Bool.false_eq_true, ↓reduceIte, hc, he]
  exact ⟨rfl, hs.1, hs.2.1, hs.2.2.trans ht⟩

theorem covered_review_adds_no_practice_loss (c : Conditions) (report : Option Bool)
    (e : Endpoint) (cover : CoversEffect c report e) :
    (reviewAndAct c report e).learning.losses = e.learning.losses := by
  unfold reviewAndAct
  split
  · rfl
  · cases hc : charge 1 e.learning.account with
    | none => rfl
    | some a =>
      simp only []
      split
      · rename_i accepted
        have risk : relevantRisk c e.requested = false := (cover false accepted).symm
        cases he : enact c {e.learning with account := a} e.requested with
        | none => rfl
        | some l => exact (operation_without_relevant_loss c _ l _ risk he).1
      · rfl

theorem review_retains_request (c : Conditions) (report : Option Bool) (e : Endpoint) :
    (reviewAndAct c report e).requested = e.requested := by
  unfold reviewAndAct
  split
  · rfl
  · cases charge 1 e.learning.account with
    | none => rfl
    | some a =>
      simp only []
      split
      · cases enact c {e.learning with account := a} e.requested <;> rfl
      · rfl

/-- Delivery removes the queue head but retains its actual value at the endpoint.
    Refusal is not queue deletion or completion. -/
def deliverReview (c : Conditions) (report : Option Bool) (l : State)
    (s : Installation) : Option (Installation × Endpoint) := do
  let p ← s.packets.head?
  let result := drain (((s.banks p.slot).path.drop p.cursor).length + 1) s
  let output ← result.2.head?
  pure (result.1, reviewAndAct c report ⟨l, output.2, true, []⟩)

theorem revised_delivery_enters_review (span : Nat) (s : Installation)
    (h : Invariant span s) (p : Packet) (ps : List Packet)
    (hp : s.packets = p :: ps) (next : Bool)
    (c : Conditions) (report : Option Bool) (l : State) :
    (deliverReview c report l (retargetHead s next)).map (fun out =>
      (out.1.packets, out.1.banks, out.1.active, out.2)) =
      some (ps, s.banks, s.active, reviewAndAct c report ⟨l, next, true, []⟩) := by
  have r := revised_head_completes span s h p ps hp next
  simp only [retargetHead, hp, retarget] at r
  simp [deliverReview, retargetHead, hp, retarget,
    r.1, r.2.1, r.2.2.1, r.2.2.2]

/-- A covered learning action requires no fixed access-loss or channel-reversal
    bit. This is action safety, not renewed comparative or ethical sufficiency. -/
theorem learning_review_covers_changed_context (c : Conditions) (l : State)
    (work : 3 ≤ l.account.work) (retain : c.transitionLoss = false) :
    let out := reviewAndAct c (some false) ⟨l, true, true, []⟩
    out.pending = false ∧ out.learning.losses = l.losses ∧
      out.learning.archive.length = l.archive.length + 1 ∧
      total out.learning.account = total l.account :=
  funded_covered_review c l true work (by simpa [relevantRisk] using retain)

/-- The weaker action-safety condition cannot silently replace the old reason
    for preferring this practice. Both claims use exactly the inherited laws. -/
theorem safe_change_can_remove_comparative_warrant :
    relevantRisk safe true = false ∧
    ¬ PracticalJudgment.Better (protects safe) (gains safe) .learning .attendance :=
  ⟨rfl, (harmless_practices_incomparable safe rfl rfl).2⟩

def continueReviewed (c : Conditions) (report : Option Bool) (l : State)
    (s : Installation) : Option (Installation × Endpoint) := do
  let adapted ← paidRetarget true l s
  deliverReview c report adapted.1 adapted.2

/-- One extra current work unit is a supplied resource, not inferred from the
    reserve or created by checking. Its total is 19, versus the inherited 18. -/
def withHeadroom : State := {formed with account := ⟨4,8,7⟩}

def summarize (out : Installation × Endpoint) :=
  (out.1.packets.length, out.2.pending, out.2.requested,
    out.2.learning.losses, out.2.learning.archive.length,
    out.2.learning.account.work, out.2.learning.account.reserve,
    out.2.learning.account.spent, out.2.reports)

theorem check_can_exhaust_action_support :
    (continueReviewed harmful (some false) formed pending).map summarize =
      some (0, true, true, 1, 2, 1, 8, 9, [some false]) := by decide

theorem additional_current_support_completes :
    (continueReviewed harmful (some false) withHeadroom pending).map summarize =
      some (0, false, true, 1, 3, 2, 6, 11, [some false]) := by decide

theorem irrelevant_context_change_can_still_complete :
    (continueReviewed ⟨false,false,true⟩ (some false) withHeadroom pending).map summarize =
      some (0, false, true, 1, 3, 2, 6, 11, [some false]) := by decide

theorem relevant_change_retains_unfinished_task :
    (continueReviewed conflict (some true) withHeadroom pending).map summarize =
      some (0, true, true, 1, 2, 2, 8, 9, [some true]) := by decide

theorem missing_report_retains_unfinished_task :
    (continueReviewed harmful none withHeadroom pending).map summarize =
      some (0, true, true, 1, 2, 2, 8, 9, [none]) := by decide

theorem report_not_covering_effect_can_still_fail :
    (continueReviewed conflict (some false) withHeadroom pending).map summarize =
      some (0, false, true, 2, 3, 2, 6, 11, [some false]) := by decide

end PendingTaskApplicability
