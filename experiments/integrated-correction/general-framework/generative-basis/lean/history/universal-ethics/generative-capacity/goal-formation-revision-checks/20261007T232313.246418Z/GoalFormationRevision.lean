import PracticalJudgment
import KnowledgeCorrespondence

/- A finite joined history, not a definition of intelligence or ethical warrant.
The two practices, feedback law, calibrated reference, protected claims, authority,
costs and deliberative response law are explicit local premises. G0/J1-J4 justify
the interpretation in the companion account, not by being hidden in these types. -/
namespace GoalFormationRevision
open PracticalJudgment

inductive Practice where
  | attendance | learning
  deriving DecidableEq, Repr

inductive Selection where
  | attendance | learning
  deriving DecidableEq, Repr

structure Conditions where
  accessLoss : Bool
  transitionLoss : Bool
  reversed : Bool
  deriving DecidableEq, Repr

structure Outcome where
  access : Bool
  maintenance : Bool
  output : Nat
  deriving DecidableEq, Repr

/-- Quantities describe declared local outcomes, not a universal welfare score. -/
def perform (c : Conditions) : Practice → Outcome
  | .attendance => ⟨!c.accessLoss, true, 2⟩
  | .learning => ⟨true, !c.transitionLoss, 1⟩

def protects (c : Conditions) (p : Practice) (claim : Bool) : Prop :=
  if claim then (perform c p).maintenance = true else (perform c p).access = true

def gains (c : Conditions) (p : Practice) (i : Nat) : Prop := i < (perform c p).output

theorem warranted_revision (c : Conditions) (harm : c.accessLoss = true)
    (retain : c.transitionLoss = false) :
    Better (protects c) (gains c) .learning .attendance := by
  apply protection_anchor (c := false)
  · intro claim h
    cases claim <;> simp_all [protects, perform]
  · simp [protects, perform]
  · simp [protects, perform, harm]

theorem revision_loses_real_output (c : Conditions) :
    gains c .attendance 1 ∧ ¬ gains c .learning 1 := by
  simp [gains, perform]

theorem harmless_attendance_preferred (c : Conditions)
    (harm : c.accessLoss = false) (retain : c.transitionLoss = false) :
    Better (protects c) (gains c) .attendance .learning := by
  apply Or.inr
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro claim h
    cases claim with
    | false => simp [protects, perform, harm]
    | true => simp [protects, perform, retain]
  · intro claim h
    cases claim with
    | false => simp [protects, perform, harm]
    | true => simp [protects, perform, retain]
  · intro i h; simp only [gains, perform] at *; omega
  · intro h
    have bad := h 1 (by simp [gains, perform])
    simp [gains, perform] at bad

theorem crossed_losses_incomparable (c : Conditions)
    (harm : c.accessLoss = true) (loss : c.transitionLoss = true) :
    ¬ Better (protects c) (gains c) .learning .attendance ∧
    ¬ Better (protects c) (gains c) .attendance .learning := by
  constructor
  · apply no_protection_trade_by_count true
    · simp [protects, perform]
    · simp [protects, perform, loss]
  · apply no_protection_trade_by_count false
    · simp [protects, perform]
    · simp [protects, perform, harm]

def feedback : Selection → Practice → Nat
  | .attendance, .attendance => 2
  | .learning, .learning => 2
  | _, _ => 0

/-- Infer a formative rule from two actually acquired feedback observations.
Only this stated two-rule family is identified; ambiguous evidence suspends. -/
def inferFormation (a b : Nat) : Option Selection :=
  if a = 2 ∧ b = 0 then some .attendance
  else if a = 0 ∧ b = 2 then some .learning else none

theorem formation_identified (r : Selection) :
    inferFormation (feedback r .attendance) (feedback r .learning) = some r := by
  cases r <;> decide

theorem ambiguous_formation_suspended : inferFormation 0 0 = none := by decide

def encode (reversed value : Bool) : Bool := Bool.xor value reversed
def decode (signal reference : Bool) : Bool := Bool.xor signal reference

theorem acquired_calibration_correct (value reversed : Bool) :
    decode (encode reversed value) (encode reversed false) = value := by
  cases value <;> cases reversed <;> rfl

/-- Reuse the actual inherited exact-correspondence result, not a new oracle. -/
theorem calibration_consumes_existing_interface :
    Generative.KnowledgeCorrespondence.ExactOn
      Generative.KnowledgeCorrespondence.allHistories
      Generative.KnowledgeCorrespondence.pairedEvidence
      Generative.KnowledgeCorrespondence.target
      Generative.KnowledgeCorrespondence.decodePair :=
  Generative.KnowledgeCorrespondence.calibrated_pair_exact

structure Account where
  work : Nat
  reserve : Nat
  spent : Nat
  deriving DecidableEq, Repr

def total (a : Account) : Nat := a.work + a.reserve + a.spent

def charge (n : Nat) (a : Account) : Option Account :=
  if n ≤ a.work then some { a with work := a.work - n, spent := a.spent + n }
  else none

theorem charge_conserves {n : Nat} {a b : Account} (h : charge n a = some b) :
    total b = total a := by
  unfold charge at h
  split at h
  · cases h
    simp only [total]
    omega
  · cases h

theorem insufficient_work_blocks {n : Nat} {a : Account} (h : a.work < n) :
    charge n a = none := by simp [charge, show ¬n ≤ a.work by omega]

structure Evidence where
  attendanceSignal : Option Bool := none
  learningSignal : Option Bool := none
  reference : Option Bool := none
  attendanceFeedback : Option Nat := none
  learningFeedback : Option Nat := none
  deriving DecidableEq, Repr

structure Ground where
  formation : Selection
  accessLoss : Bool
  transitionLoss : Bool
  deriving DecidableEq, Repr

def interpret (e : Evidence) : Option Ground := do
  let a ← e.attendanceFeedback
  let b ← e.learningFeedback
  let origin ← inferFormation a b
  let sa ← e.attendanceSignal
  let sb ← e.learningSignal
  let ref ← e.reference
  pure ⟨origin, decode sa ref, decode sb ref⟩

def callsForRevision (g : Ground) : Bool := g.accessLoss && !g.transitionLoss

/-- A model of own formation has counterfactual predictions and targeted use. -/
def predictFeedback (g : Ground) (rule : Selection) (p : Practice) : Nat :=
  if rule = g.formation then feedback g.formation p else feedback rule p

theorem formation_model_predicts_intervention (g : Ground) (r : Selection) (p : Practice) :
    predictFeedback g r p = feedback r p := by
  simp only [predictFeedback]
  split
  · rename_i h; rw [h]
  · rfl

def proposedSelector (g : Ground) : Option Selection :=
  if predictFeedback g g.formation .learning = 2 then none else some .learning

theorem acquired_grounds_warrant_comparison (c : Conditions) (r : Selection)
    (h : callsForRevision ⟨r,c.accessLoss,c.transitionLoss⟩ = true) :
    Better (protects c) (gains c) .learning .attendance := by
  have a : c.accessLoss = true := by
    cases c with
    | mk a b rev => cases a <;> cases b <;> simp_all [callsForRevision]
  have b : c.transitionLoss = false := by
    cases c with
    | mk a b rev => cases a <;> cases b <;> simp_all [callsForRevision]
  exact warranted_revision c a b

structure Record where
  practice : Practice
  outcome : Outcome
  feedback : Nat
  deriving DecidableEq, Repr

structure State where
  account : Account
  selector : Selection
  attendanceScore : Nat := 0
  learningScore : Nat := 0
  goal : Option Practice := none
  evidence : Evidence := {}
  ground : Option Ground := none
  archive : List Record := []
  losses : Nat := 0
  reformed : Bool := false
  deriving DecidableEq, Repr

def learnedGoal (a b : Nat) : Option Practice :=
  if a > b then some .attendance else if b > a then some .learning else none

/-- Practice and formative feedback occur in the same charged transition.
The selected trial schedule is supplied; it is not autonomous experiment design. -/
def experience (c : Conditions) (p : Practice) (s : State) : Option State := do
  let account ← charge 1 s.account
  let o := perform c p
  let f := feedback s.selector p
  let a := s.attendanceScore + (if p = .attendance then f else 0)
  let b := s.learningScore + (if p = .learning then f else 0)
  let e := match p with
    | .attendance => { s.evidence with attendanceSignal := some (encode c.reversed (!o.access)), attendanceFeedback := some f }
    | .learning => { s.evidence with learningSignal := some (encode c.reversed (!o.maintenance)), learningFeedback := some f }
  pure { s with
    account := account
    attendanceScore := a
    learningScore := b
    goal := learnedGoal a b
    evidence := e
    ground := none
    archive := s.archive ++ [⟨p, o, f⟩]
    losses := s.losses + (if o.access && o.maintenance then 0 else 1) }

def calibrate (c : Conditions) (s : State) : Option State := do
  let account ← charge 1 s.account
  pure { s with account, evidence := { s.evidence with reference := some (encode c.reversed false) }, ground := none }

def assess (s : State) : Option State := do
  let account ← charge 1 s.account
  let ground ← interpret s.evidence
  pure { s with account, ground := some ground }

/-- Receptivity is an explicit implementation parameter. Truth does not force motivation. -/
def reviseGoal (responsive : Bool) (s : State) : Option State := do
  let account ← charge 1 s.account
  let g ← s.ground
  pure { s with account, goal := if responsive && callsForRevision g then some .learning else s.goal }

/-- Authority is supplied. Inference alone does not create permission. -/
def reform (authorized : Bool) (s : State) : Option State := do
  if !authorized then none else do
    let g ← s.ground
    if s.goal != some .learning || !callsForRevision g then none else do
      let selector ← proposedSelector g
      let account ← charge 2 s.account
      pure { s with account, selector, reformed := true }

theorem no_authority_no_reform (s : State) : reform false s = none := by
  simp [reform]

/-- Support is transferred from an actual finite reserve after work is performed.
An unselected goal can still operate using its own remaining work. -/
def cycle (r : Selection) (p : Practice) (a : Account) : Option Account := do
  let b ← charge 2 a
  if feedback r p = 2 ∧ 2 ≤ b.reserve then
    pure { b with work := b.work + 2, reserve := b.reserve - 2 }
  else pure b

theorem cycle_conserves {r : Selection} {p : Practice} {a b : Account}
    (h : cycle r p a = some b) : total b = total a := by
  unfold cycle at h
  cases hc : charge 2 a with
  | none => simp [hc] at h
  | some x =>
    simp only [hc] at h
    change (if feedback r p = 2 ∧ 2 ≤ x.reserve then
      some { x with work := x.work + 2, reserve := x.reserve - 2 }
      else some x) = some b at h
    split at h
    · rename_i eligible
      cases h
      have conserved := charge_conserves hc
      simp only [total] at *
      omega
    · cases h
      exact charge_conserves hc

def cycles (r : Selection) (p : Practice) : Nat → Account → Option Account
  | 0, a => some a
  | n + 1, a => do
    let b ← cycle r p a
    cycles r p n b

/-- Actual continuation consumes the retained goal, runs its outcome law and
keeps its consequences and record; no externally selected replacement goal. -/
def operate (c : Conditions) (s : State) : Option State := do
  let p ← s.goal
  let account ← cycle s.selector p s.account
  let o := perform c p
  pure { s with
    account := account
    archive := s.archive ++ [⟨p,o,feedback s.selector p⟩]
    losses := s.losses + (if o.access && o.maintenance then 0 else 1) }

def operateMany (c : Conditions) : Nat → State → Option State
  | 0, s => some s
  | n+1, s => operate c s >>= operateMany c n

theorem supported_cycle (w q z : Nat) (hw : 2 ≤ w) (hq : 2 ≤ q) :
    cycle .learning .learning ⟨w,q,z⟩ = some ⟨w,q-2,z+2⟩ := by
  simp [cycle, charge, hw, feedback, hq]

theorem supported_finite_continuation (n w q z : Nat)
    (hw : 2 ≤ w) (hq : 2*n ≤ q) :
    cycles .learning .learning n ⟨w,q,z⟩ = some ⟨w,q-2*n,z+2*n⟩ := by
  induction n generalizing q z with
  | zero => simp [cycles]
  | succ n ih =>
    have hq2 : 2 ≤ q := by omega
    have hn : 2*n ≤ q-2 := by omega
    simp only [cycles, supported_cycle w q z hw hq2]
    change cycles .learning .learning n ⟨w,q-2,z+2⟩ = _
    rw [ih (q-2) (z+2) hn]
    congr 1 <;> omega

def start (r : Selection) : State :=
  { account := ⟨10,8,0⟩, selector := r }

def acquire (c : Conditions) (r : Selection) : Option State := do
  let a ← experience c .attendance (start r)
  let b ← experience c .learning a
  let d ← calibrate c b
  assess d

def revised (c : Conditions) (responsive : Bool := true) : Option State := do
  let s ← acquire c .attendance
  reviseGoal responsive s

def completed (c : Conditions) : Option State := do
  let s ← revised c
  reform true s

def harmful : Conditions := ⟨true,false,false⟩
def safe : Conditions := ⟨false,false,false⟩
def conflict : Conditions := ⟨true,true,false⟩

theorem acquired_history_identifies_origin (c : Conditions) (r : Selection) :
    (acquire c r).map State.ground = some (some ⟨r,c.accessLoss,c.transitionLoss⟩) := by
  cases c with
  | mk a b rev => cases a <;> cases b <;> cases rev <;> cases r <;> decide

theorem goal_depends_on_actual_formative_rule (c : Conditions) :
    (acquire c .attendance).map State.goal = some (some .attendance) ∧
    (acquire c .learning).map State.goal = some (some .learning) := by
  cases c with
  | mk a b rev => cases a <;> cases b <;> cases rev <;> decide

theorem revised_goal_with_old_metric_still_successful :
    (revised harmful).map State.goal = some (some .learning) ∧
    (revised harmful).map State.attendanceScore = some 2 ∧
    (revised harmful).map State.learningScore = some 0 ∧
    (perform harmful .attendance).output > (perform harmful .learning).output := by decide

theorem calibration_handles_reversed_channel :
    (revised ⟨true,false,true⟩).map State.goal = some (some .learning) := by decide

theorem no_harm_no_revision :
    (revised safe).map State.goal = some (some .attendance) := by decide

theorem crossed_loss_blocks_simple_revision :
    (revised conflict).map State.goal = some (some .attendance) ∧ completed conflict = none := by decide

theorem recognition_does_not_force_revision :
    (revised harmful false).map State.ground = (revised harmful true).map State.ground ∧
    (revised harmful false).map State.goal = some (some .attendance) ∧
    (revised harmful true).map State.goal = some (some .learning) := by decide

theorem reform_changes_the_formative_relation :
    (completed harmful).map State.selector = some .learning ∧
    (completed harmful).map (fun s => feedback s.selector .attendance) = some 0 ∧
    (completed harmful).map (fun s => feedback s.selector .learning) = some 2 := by decide

theorem acquired_intervention_prediction_realized :
    (acquire harmful .attendance).map (fun s => s.ground.map (fun g => predictFeedback g .learning .learning)) = some (some 2) ∧
    (completed harmful).map (fun s => feedback s.selector .learning) = some 2 := by decide

theorem revision_preserves_formation_and_losses :
    (completed harmful).map State.archive = (acquire harmful .attendance).map State.archive ∧
    (completed harmful).map State.losses = some 1 ∧
    (completed harmful).map State.attendanceScore = some 2 := by decide

theorem complete_history_account :
    (completed harmful).map State.account = some ⟨3,8,7⟩ ∧
    (completed harmful).map (fun s => total s.account) = some 18 := by decide

theorem actual_reformed_continuation :
    (completed harmful >>= operateMany harmful 5).map State.account = some ⟨1,0,17⟩ := by decide

theorem continued_practice_preserves_actual_consequences :
    (completed harmful >>= operateMany harmful 5).map (fun s => s.archive.length) = some 7 ∧
    (completed harmful >>= operateMany harmful 5).map State.losses = some 1 ∧
    (completed harmful >>= operateMany harmful 5).map State.goal = some (some .learning) := by decide

theorem unchanged_selection_exhausts_revised_practice :
    (revised harmful >>= operateMany harmful 3) = none := by decide

theorem reform_does_not_make_support_infinite :
    (completed harmful >>= operateMany harmful 6) = none := by decide

theorem reform_with_insufficient_work_fails :
    (revised harmful >>= fun s => reform true {s with account := ⟨1,8,9⟩}) = none := by decide

theorem missing_reference_prevents_assessment :
    (experience harmful .attendance (start .attendance) >>= experience harmful .learning >>= assess) = none := by decide

theorem false_reference_can_hide_real_loss :
    (acquire harmful .attendance >>= fun s =>
      assess {s with evidence := {s.evidence with reference := some true}} >>= reviseGoal true).map State.goal
       = some (some .attendance) := by decide

theorem erased_formation_evidence_blocks_deliberation :
    (acquire harmful .attendance >>= fun s =>
      assess {s with evidence := {s.evidence with attendanceFeedback := none}}) = none := by decide

theorem wrong_formation_model_prevents_needed_reform :
    (revised harmful >>= fun s => reform true
      {s with ground := some ⟨.learning,true,false⟩}) = none := by decide

theorem stale_grounds_can_leave_new_loss_unaddressed :
    (revised safe >>= operate harmful).map State.goal = some (some .attendance) ∧
    (revised safe >>= operate harmful).map State.losses = some 1 := by decide

theorem changed_goal_is_consumed_by_operation :
    (revised harmful false >>= operate harmful).map State.losses = some 2 ∧
    (revised harmful true >>= operate harmful).map State.losses = some 1 := by decide

end GoalFormationRevision
