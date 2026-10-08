import GoalFormationRevision

/- Reform changes both operative conditions and what the selected reporting route
transmits. These are explicit local laws within one retained history. Normative
classification, authority, reliable direct access and affordable repair are
application premises, not consequences of a Boolean name. -/
namespace ReformEvidence
open GoalFormationRevision

inductive Route where
  | selected | direct
  deriving DecidableEq, Repr

/-- The selected report includes maintenance losses under the old arrangement,
but excludes that constituency after the selector changes. Direct access reads
the retained consequence before this exclusion; its fidelity is supplied. -/
def transmit (route : Route) (selector : Selection) (loss : Bool) : Bool :=
  if route = .selected ∧ selector = .learning then false else loss

theorem old_route_calibration (loss : Bool) :
    transmit .selected .attendance loss = loss := by simp [transmit]

theorem direct_access_preserves_loss (selector : Selection) (loss : Bool) :
    transmit .direct selector loss = loss := by simp [transmit]

theorem old_calibration_does_not_transport :
    transmit .selected .attendance true = true ∧
    transmit .selected .learning true = false := by decide

structure Field where
  core : State
  transfersBurden : Bool
  provisioned : Bool := false
  reports : List Bool := []
  deriving DecidableEq, Repr

/-- The actual selector change activates a previously absent maintenance burden.
Provisioning changes its causal condition; it does not rewrite a report. -/
def conditions (s : Field) : Conditions :=
  ⟨true, s.transfersBurden && (s.core.selector == .learning) && !s.provisioned, false⟩

def prepare : Option State := do
  let a ← experience harmful .attendance {start .attendance with account := ⟨14,12,0⟩}
  let b ← experience harmful .learning a
  let c ← calibrate harmful b
  let d ← assess c
  reviseGoal true d

def beforeReform (transfer : Bool) : Option Field :=
  prepare.map (fun s => ⟨s,transfer,false,[]⟩)

def changeRule (s : Field) : Option Field := do
  let core ← reform true s.core
  pure {s with core}

def begun (transfer : Bool) : Option Field := beforeReform transfer >>= changeRule

def advance (s : Field) : Option Field := do
  let core ← operate (conditions s) s.core
  pure {s with core}

/-- Consume the actual last operation's maintenance record through the selected
route, then reassess. Formative feedback and its historical origin are retained.
This is a maintenance recheck, not a fresh exhaustive audit of every condition. -/
def inspect (route : Route) (s : Field) : Option Field := do
  let last ← s.core.archive.getLast?
  if last.practice != .learning then none else do
    let account ← charge 1 s.core.account
    let report := transmit route s.core.selector (!last.outcome.maintenance)
    let core ← assess {s.core with
      account := account
      evidence := {s.core.evidence with learningSignal := some report}
      ground := none}
    pure {s with core := core, reports := s.reports ++ [report]}

def approves (s : Field) : Bool :=
  match s.core.ground with
  | none => false
  | some g => callsForRevision g

/-- An intervention consumes work plus two units of the existing reserve to
establish maintenance provision. The standing goal and selector are unchanged.
Its applicability verdict is invalidated until the new conditions are checked. -/
def repair (authorized : Bool) (s : Field) : Option Field := do
  if !authorized then none else do
    let g ← s.core.ground
    if !g.transitionLoss then none else do
      let a ← charge 1 s.core.account
      if 2 ≤ a.reserve then
        pure {s with
          core := {s.core with account := ⟨a.work,a.reserve-2,a.spent+2⟩, ground := none}
          provisioned := true}
      else none

theorem repair_requires_authority (s : Field) : repair false s = none := by
  simp [repair]

theorem repair_conserves {s t : Field} {authorized : Bool}
    (h : repair authorized s = some t) : total t.core.account = total s.core.account := by
  unfold repair at h
  split at h
  · cases h
  · cases hg : s.core.ground with
    | none => simp [hg] at h
    | some g =>
      simp only [hg] at h
      change (if !g.transitionLoss then none else _) = some t at h
      split at h
      · cases h
      · cases hc : charge 1 s.core.account with
        | none => simp [hc] at h
        | some a =>
          simp only [hc] at h
          change (if 2 ≤ a.reserve then some _ else none) = some t at h
          split at h
          · rename_i enough
            cases h
            have accounted := charge_conserves hc
            simp only [total] at *
            omega
          · cases h

def post (transfer : Bool) : Option Field := begun transfer >>= advance
def masked (transfer : Bool) : Option Field := post transfer >>= inspect .selected
def exposed : Option Field := masked true >>= inspect .direct
def restored : Option Field := exposed >>= repair true
def rechecked : Option Field := restored >>= advance >>= inspect .direct

theorem old_conditions_agree :
    (beforeReform true).map conditions = (beforeReform false).map conditions := by decide

theorem rule_change_activates_real_burden :
    (beforeReform true).map (fun s => (conditions s).transitionLoss) = some false ∧
    (begun true).map (fun s => (conditions s).transitionLoss) = some true := by decide

theorem actual_burden_differs_after_reform :
    (post true).map (fun s => s.core.losses) = some 2 ∧
    (post false).map (fun s => s.core.losses) = some 1 := by decide

/-- Only the specified judgment inputs are indistinguishable. The whole histories
are different; other accessible evidence can and does distinguish them. -/
def judgmentInput (s : Field) : Evidence × List Bool := (s.core.evidence, s.reports)

theorem filtered_judgment_inputs_agree :
    (masked true).map judgmentInput = (masked false).map judgmentInput := by decide

theorem every_decider_shares_filtered_answer {A : Type}
    (decideFrom : Option (Evidence × List Bool) → A) :
    decideFrom ((masked true).map judgmentInput) = decideFrom ((masked false).map judgmentInput) := by
  rw [filtered_judgment_inputs_agree]

theorem repetition_of_filtered_report_does_not_separate (n : Nat) :
    List.replicate n (transmit .selected .learning true) =
    List.replicate n (transmit .selected .learning false) := by rfl

theorem self_approval_coexists_with_actual_loss :
    (masked true).map approves = some true ∧
    (masked true).map (fun s => s.core.losses) = some 2 ∧
    (masked true).map (fun s => feedback s.core.selector .learning) = some 2 := by decide

theorem approved_continuation_repeats_real_loss :
    (masked true >>= advance >>= inspect .selected).map approves = some true ∧
    (masked true >>= advance >>= inspect .selected).map (fun s => s.core.losses) = some 3 := by decide

theorem direct_observation_changes_judgment :
    exposed.map approves = some false ∧
    exposed.map (fun s => s.core.ground.map Ground.transitionLoss) = some (some true) ∧
    exposed.map Field.reports = some [false,true] := by decide

theorem supported_reform_survives_direct_check :
    (masked false >>= inspect .direct).map approves = some true ∧
    (masked false >>= inspect .direct).map Field.reports = some [false,false] := by decide

theorem repair_preserves_revised_goal_and_selection :
    restored.map (fun s => s.core.goal) = some (some .learning) ∧
    restored.map (fun s => s.core.selector) = some .learning ∧
    restored.map (fun s => s.core.ground) = some none := by decide

theorem actual_repaired_continuation_and_recheck :
    rechecked.map approves = some true ∧
    rechecked.map (fun s => s.core.losses) = some 2 ∧
    rechecked.map Field.reports = some [false,true,false] ∧
    rechecked.map (fun s => s.core.archive.length) = some 4 := by decide

theorem all_stages_account_for_the_same_support :
    (masked true).map (fun s => s.core.account) = some ⟨5,10,11⟩ ∧
    exposed.map (fun s => s.core.account) = some ⟨3,10,13⟩ ∧
    restored.map (fun s => s.core.account) = some ⟨2,8,16⟩ ∧
    rechecked.map (fun s => s.core.account) = some ⟨0,6,20⟩ ∧
    rechecked.map (fun s => total s.core.account) = some 26 := by decide

theorem depleted_work_blocks_further_operation : rechecked >>= advance = none := by decide

theorem unavailable_inquiry_is_not_a_pass :
    (masked true >>= fun s => inspect .direct {s with core := {s.core with account := ⟨1,10,15⟩}}) = none := by decide

theorem insufficient_repair_reserve_blocks_action :
    (exposed >>= fun s => repair true {s with core := {s.core with account := ⟨3,1,22⟩}}) = none := by decide

def protectionAfter (provided : Bool) (claim : Bool) : Prop :=
  protects ⟨true,!provided,false⟩ .learning claim

def gainsAfter (provided : Bool) (i : Nat) : Prop :=
  gains ⟨true,!provided,false⟩ .learning i

/-- Uses the inherited explicit J2 comparator. Real repair costs are represented
above; their non-basic classification is an additional correspondence premise. -/
theorem restoring_maintenance_is_favored :
    PracticalJudgment.Better protectionAfter gainsAfter true false := by
  apply PracticalJudgment.protection_anchor (c := true)
  · intro i h; cases i <;> simp [protectionAfter, protects, perform]
  · simp [protectionAfter, protects, perform]
  · simp [protectionAfter, protects, perform]

theorem unrepaired_shift_has_real_basic_conflict :
    ¬ PracticalJudgment.Better (protects ⟨true,true,false⟩) (gains ⟨true,true,false⟩) .learning .attendance ∧
    ¬ PracticalJudgment.Better (protects ⟨true,true,false⟩) (gains ⟨true,true,false⟩) .attendance .learning :=
  crossed_losses_incomparable _ rfl rfl

end ReformEvidence
