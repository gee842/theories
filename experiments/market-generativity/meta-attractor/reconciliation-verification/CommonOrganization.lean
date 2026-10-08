import UpdaterFormation

/- A paid receipt-sensitive continuation of the existing formation history.
The renewal response and bridge are inherited supplied laws. Receipt retention
costs one unit per trial; its apparatus is included in module formation by this
additional implementation assumption. No stochastic or empirical claim. -/
namespace CommonOrganization

def params := UpdaterFormation.primary
theorem admissible : UpdaterFormation.Admissible params := by
  unfold UpdaterFormation.Admissible SelectorRevision.Admissible
  decide

structure State where
  organization : UpdaterFormation.State
  misses : Nat
deriving DecidableEq, Repr

inductive Event where
  | form | select | trial (signal : Bool) | reverse
deriving DecidableEq, Repr

def proposal (s : State) : Bool := 0 < s.misses
def orientation (s : State) : Bool :=
  if s.organization.directed && s.organization.selectorSeen
  then !s.organization.core.selector else s.organization.core.selector
def command (s : State) : Event → UpdaterFormation.Event
  | .form => .formModule (proposal s)
  | .select => .formSelector (orientation s)
  | .trial b => .trial b
  | .reverse => .reverse
def fee : Event → Nat | .trial _ => 1 | _ => 0
def Enabled (s : State) (a : Event) : Prop :=
  UpdaterFormation.Enabled params s.organization (command s a) ∧
  (a = .trial false ∨ a = .trial true →
    params.selector.trial+1 ≤ s.organization.core.fuel)
def advance (s : State) (a : Event) : State :=
  let next := UpdaterFormation.advance params s.organization (command s a)
  { organization := { next with core := { next.core with fuel := next.core.fuel - fee a } }
    misses := match a with
      | .form => 0
      | .trial _ => if next.core.lease < s.organization.core.lease then s.misses+1 else 0
      | _ => s.misses }
def Step (s : State) (a : Event) (t : State) : Prop :=
  Enabled s a ∧ t = advance s a
instance (s : State) (a : Event) : Decidable (Enabled s a) := by
  unfold Enabled
  infer_instance
instance (s : State) (a : Event) (t : State) : Decidable (Step s a t) := by
  unfold Step
  infer_instance
def process : Generative.Process State Event := ⟨Step⟩
def energy (s : State) := UpdaterFormation.energy params s.organization
def cost (s : State) (a : Event) :=
  UpdaterFormation.expenditure params s.organization (command s a) +
  UpdaterFormation.waste params s.organization (command s a) + fee a
def spent (s : State) : List Event → Nat
  | [] => 0
  | a :: rest => cost s a + spent (advance s a) rest

theorem proposal_does_not_read_regime (s : State) (z : Bool) :
    proposal { s with organization := { s.organization with
      core := { s.organization.core with regime := z } } } = proposal s := rfl

theorem orientation_does_not_read_regime (s : State) (z : Bool) :
    orientation { s with organization := { s.organization with
      core := { s.organization.core with regime := z } } } = orientation s := rfl

theorem failed_trial_is_retained (s : State) (b : Bool)
    (h : s.organization.core.selector ≠ s.organization.core.regime)
    (lease : 0 < s.organization.core.lease) :
    (advance s (.trial b)).misses = s.misses+1 := by
  have hl : s.organization.core.lease-1 < s.organization.core.lease := by omega
  simp [advance,command,UpdaterFormation.advance,SelectorRevision.advance,h,hl]

theorem no_misses_proposes_undirected (s : State) (h : s.misses = 0) :
    proposal s = false := by simp [proposal,h]
theorem misses_propose_directed (s : State) (h : 0 < s.misses) :
    proposal s = true := by simp [proposal,h]

theorem revision_remains_available (s : State)
    (expired : s.organization.moduleLease = 0)
    (funded : params.moduleAssembly ≤ s.organization.core.fuel) :
    Enabled s .form := by
  refine ⟨⟨expired,funded⟩,?_⟩
  intro h
  cases h <;> contradiction

theorem paid_receipt_available (s : State) (a : Event) (h : Enabled s a) :
    fee a ≤ (UpdaterFormation.advance params s.organization (command s a)).core.fuel := by
  cases a with
  | form | select | reverse => simp [fee]
  | trial b =>
    have hf := h.2 (by cases b <;> simp)
    have pp : params.selector.trial = 2 := rfl
    by_cases hm : s.organization.core.selector = s.organization.core.regime <;>
      simp [UpdaterFormation.advance,SelectorRevision.advance,command,params,
        UpdaterFormation.primary,UpdaterFormation.effective,fee,hm] <;> omega

theorem step_accounting (s t : State) (a : Event) (h : Step s a t) :
    energy t + cost s a = energy s := by
  rcases h with ⟨he,rfl⟩
  have ledger := UpdaterFormation.step_energy_ledger admissible
    (show UpdaterFormation.Step params s.organization (command s a)
      (UpdaterFormation.advance params s.organization (command s a)) from ⟨he.1,rfl⟩)
  have reserve := paid_receipt_available s a he
  simp only [advance,energy,cost,UpdaterFormation.energy,SelectorRevision.energy] at *
  omega

theorem trace_accounting {s t : State} {as : List Event}
    (h : Generative.Trace process s as t) : energy t + spent s as = energy s := by
  induction h with
  | nil => simp [spent]
  | @cons s u t a as hs ht ih =>
    have ledger := step_accounting s u a hs
    have hu : u = advance s a := hs.2
    subst u
    simp only [spent]
    omega

def receipts : List Event → Nat
  | [] => 0
  | a::as => fee a + receipts as

theorem receipts_are_paid (s : State) (as : List Event) :
    receipts as ≤ spent s as := by
  induction as generalizing s with
  | nil => simp [receipts,spent]
  | cons a as ih =>
    have h := ih (advance s a)
    simp only [receipts,spent,cost]
    omega

theorem finite_support_bounds_trials {s t : State} {as : List Event}
    (h : Generative.Trace process s as t) : receipts as ≤ energy s := by
  have paid := receipts_are_paid s as
  have ledger := trace_accounting h
  omega

def run : State → List Event → Option State
  | s, [] => some s
  | s, a::as => if Enabled s a then run (advance s a) as else none

theorem run_sound (s : State) (as : List Event) (t : State)
    (h : run s as = some t) : Generative.Trace process s as t := by
  induction as generalizing s with
  | nil => simp [run] at h; subst t; exact .nil _
  | cons a as ih =>
    by_cases he : Enabled s a
    · simp [run,he] at h
      exact .cons ⟨he,rfl⟩ (ih _ h)
    · simp [run,he] at h

def entrance : State := ⟨UpdaterFormation.primaryEntrance,0⟩
def preparation : List Event := [.form,.select] ++ List.replicate 8 (.trial false)
def failure : List Event := [.reverse,.trial false,.trial true,.select,.trial false,.trial true]
def replacement : List Event := [.form,.select,.trial false]
def furtherChange : List Event :=
  List.replicate 6 (.trial false) ++ [.reverse,.trial false,.trial true,.select,.trial false]
def history := preparation ++ failure ++ replacement ++ furtherChange

def beforeReplacement : State :=
  ⟨UpdaterFormation.exampleState 6 4 false 0 true false 0,4⟩
def recovered : State :=
  ⟨UpdaterFormation.exampleState 4 3 true 2 true true 4,0⟩

-- The longer history uses the same material formation with more finite source.
def oldInitial : FormedSelection.State :=
  { UpdaterFormation.oldInitial with source := 193 }
def oldEntrance : FormedSelection.State :=
  { UpdaterFormation.oldEntrance with source := 192 }
def fundedEntrance : State :=
  ⟨{ UpdaterFormation.primaryEntrance with core :=
    { UpdaterFormation.primaryEntrance.core with packets := 32 } },0⟩
def waiting : State :=
  { beforeReplacement with organization := { beforeReplacement.organization with
    core := { beforeReplacement.organization.core with packets := 20 } } }
def restored : State :=
  { recovered with organization := { recovered.organization with
    core := { recovered.organization.core with packets := 19 } } }
def finalState : State := ⟨UpdaterFormation.exampleState 4 10 false 2 false true 4,0⟩

theorem actual_failure_record : run fundedEntrance (preparation ++ failure) = some waiting := by decide
theorem acquired_replacement : run waiting replacement = some restored := by decide
theorem successful_response_can_be_revised_again :
    run restored furtherChange = some finalState := by decide
theorem whole_regulation_history : Generative.Trace process fundedEntrance history finalState := by
  apply run_sound
  decide

def frozenReceipt : State := { waiting with misses := 0 }
theorem receipt_changes_replacement :
    (advance waiting .form).organization.directed = true ∧
    (advance frozenReceipt .form).organization.directed = false := by decide
theorem frozen_receipt_repeats_failed_orientation :
    (advance (advance frozenReceipt .form) .select).organization.core.selector = false ∧
    (advance (advance waiting .form) .select).organization.core.selector = true := by decide
theorem no_funds_blocks_even_informed_revision :
    ¬ Enabled { waiting with organization := { waiting.organization with
      core := { waiting.organization.core with fuel := 1 } } } .form := by decide

/-- A rival receipt implementation: same costs, but every stored reading is erased. -/
def blindRun : State → List Event → Option State
  | s, [] => some s
  | s, a::as => if Enabled s a then
      blindRun { advance s a with misses := 0 } as else none
theorem blind_prefix_has_same_organization :
    blindRun fundedEntrance (preparation ++ failure) = some frozenReceipt := by decide
theorem blind_replacement_fails_again :
    blindRun frozenReceipt replacement = some
      ⟨UpdaterFormation.exampleState 0 19 false 1 true false 3,0⟩ := by decide

inductive JointState where
  | formation (s : FormedSelection.State)
  | regulation (s : State)
deriving DecidableEq, Repr
inductive JointEvent where
  | old (a : FormedSelection.Event) | connect | regulate (a : Event)
deriving DecidableEq, Repr
def JointStep : JointState → JointEvent → JointState → Prop
  | .formation s, .old a, .formation t => FormedSelection.Step 2 s a t
  | .formation s, .connect, .regulation t =>
    UpdaterFormation.BridgeEnabled params 2 s ∧
    t = ⟨UpdaterFormation.entrance params 2 s false,0⟩
  | .regulation s, .regulate a, .regulation t => Step s a t
  | _,_,_ => False
def jointProcess : Generative.Process JointState JointEvent := ⟨JointStep⟩

theorem lift_regulation {s t : State} {as : List Event}
    (h : Generative.Trace process s as t) :
    Generative.Trace jointProcess (.regulation s) (as.map JointEvent.regulate) (.regulation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs ht ih =>
    apply Generative.Trace.cons (m := .regulation u)
    · exact hs
    · exact ih

theorem formed_preparation :
    Generative.Trace jointProcess (.formation oldInitial)
      (UpdaterFormation.oldPreparation.map JointEvent.old) (.formation oldEntrance) := by
  apply Generative.Trace.cons (m := .formation ⟨0,1,.empty,false,false,17,193⟩) (by change FormedSelection.Step 2 _ _ _; decide)
  apply Generative.Trace.cons (m := .formation ⟨1,1,.empty,false,false,16,193⟩) (by change FormedSelection.Step 2 _ _ _; decide)
  apply Generative.Trace.cons (m := .formation ⟨0,1,.active,false,false,15,193⟩) (by change FormedSelection.Step 2 _ _ _; decide)
  apply Generative.Trace.cons (m := .formation ⟨0,1,.active,true,false,14,193⟩) (by change FormedSelection.Step 2 _ _ _; decide)
  apply Generative.Trace.cons (m := .formation oldEntrance) (by change FormedSelection.Step 2 _ _ _; decide)
  exact .nil _

theorem actual_connection :
    JointStep (.formation oldEntrance) .connect (.regulation fundedEntrance) := by
  change UpdaterFormation.BridgeEnabled params 2 oldEntrance ∧ _
  constructor
  · unfold UpdaterFormation.BridgeEnabled; decide
  · decide

theorem formation_regulation_revision_in_one_history :
    Generative.Trace jointProcess (.formation oldInitial)
      (UpdaterFormation.oldPreparation.map JointEvent.old ++
        .connect :: history.map JointEvent.regulate) (.regulation finalState) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.formation oldEntrance,formed_preparation,?_⟩
  apply Generative.Trace.cons (m := .regulation fundedEntrance)
  · exact actual_connection
  · exact lift_regulation whole_regulation_history

theorem full_accounting :
    FormedSelection.energy oldInitial = 211 ∧
    FormedSelection.tally FormedSelection.expenditure UpdaterFormation.oldPreparation = 4 ∧
    params.adapter = 1 ∧ energy fundedEntrance = 206 ∧
    spent fundedEntrance history = 142 ∧ energy finalState = 64 ∧
    finalState.organization.material = 2 := by decide

end CommonOrganization
