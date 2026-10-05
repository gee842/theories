import RecipientAction
import SemanticCalibration

/- A supplied exclusive interval and instrumented invalidation interface.
No event in this module grants a fresh acquisition origin. External state
changes, including replay and every instrumented controller write, retire it.
There is no hidden-law argument or live q test in the comparison guard. -/
namespace PaidPreImport

open RecipientCorrection (Laws packedAct lookup)

inductive Phase where
  | fresh | command | candidate | flag | compared | consumed | retired
  deriving DecidableEq, Repr

structure State where
  inner : RecipientAction.State
  module : Bool
  candidateAccess : Bool
  flagAccess : Bool
  reserve : Nat
  spent : Nat
  originUnused : Bool
  phase : Phase
  candidateLatch : Option Bool
  flagLatch : Option Bool
  permit : Option Bool

def initial (s : RecipientAction.State) (reserve : Nat) : State :=
  ⟨s,true,true,true,reserve,0,true,.fresh,none,none,none⟩

def candidate (s : State) := packedAct (RecipientAction.core s.inner).hardware.q .recipient
def qualification (s : State) := (RecipientAction.core s.inner).hardware.last

/- Only paid latches enter this function. Current publication continuity is
supplied by the exclusive event interface, then rechecked by parent install. -/
def decision (s : State) : Option Bool :=
  match s.inner.latch,s.candidateLatch,s.flagLatch with
  | some command,some acquired,some true => if command=acquired then some command else none
  | _,_,_ => none

def pay (s : State) : State := { s with reserve := s.reserve-1, spent := s.spent+1 }

inductive Event where
  | readCommand | readCandidate | readFlag | compare | consume | install
  | damagedCandidate | damagedFlag
  | retire (replacement : RecipientAction.State)

def advance (laws : Laws) (s : State) : Event → State
  | .readCommand => { s with inner := RecipientAction.advance laws s.inner .read, phase := .command }
  | .readCandidate => { pay s with candidateLatch := some (candidate s), phase := .candidate }
  | .readFlag => { pay s with flagLatch := some (qualification s), phase := .flag }
  | .compare => { pay s with permit := decision s, phase := .compared, originUnused := s.originUnused && (decision s).isSome }
  | .consume => { s with originUnused := false, phase := .consumed }
  | .install => { s with inner := RecipientAction.advance laws s.inner .install, originUnused := false, phase := .retired, permit := none }
  | .damagedCandidate => { pay s with originUnused := false, phase := .retired, candidateLatch := none, flagLatch := none, permit := none }
  | .damagedFlag => { pay s with originUnused := false, phase := .retired, flagLatch := none, permit := none }
  | .retire replacement => { s with inner := replacement, originUnused := false, phase := .retired, candidateLatch := none, flagLatch := none, permit := none }

def Ready (s : State) (phase : Phase) :=
  s.originUnused=true ∧ s.phase=phase ∧ s.module=true ∧ 1≤s.reserve

def Enabled (s : State) : Event → Prop
  | .readCommand => s.originUnused=true ∧ s.phase=.fresh ∧ RecipientAction.Enabled s.inner .read
  | .readCandidate => Ready s .command ∧ s.candidateAccess=true
  | .readFlag => Ready s .candidate ∧ s.flagAccess=true
  | .compare => Ready s .flag
  | .damagedCandidate => Ready s .command ∧ s.candidateAccess=false
  | .damagedFlag => Ready s .candidate ∧ s.flagAccess=false
  | .consume => s.originUnused=true ∧ s.phase=.compared
  | .install => s.originUnused=false ∧ s.phase=.consumed ∧
      (∃ b, s.permit=some b ∧ s.inner.latch=some b) ∧ RecipientAction.Enabled s.inner .install
  | .retire _ => True

def Step (laws : Laws) (s : State) (e : Event) (t : State) :=
  Enabled s e ∧ t=advance laws s e

def process (laws : Laws) : Generative.Process State Event := ⟨Step laws⟩

def inspect (laws : Laws) (s : State) :=
  advance laws (advance laws (advance laws s .readCandidate) .readFlag) .compare

theorem inspection_preserves_entire_parent (laws : Laws) (s : State) :
    (inspect laws s).inner=s.inner ∧
    (inspect laws s).candidateLatch=some (candidate s) ∧
    (inspect laws s).flagLatch=some (qualification s) := by
  exact ⟨rfl,rfl,rfl⟩

theorem paid_inspection_trace (laws : Laws) (s : State)
    (origin : s.originUnused=true) (phase : s.phase=.command)
    (module : s.module=true) (ca : s.candidateAccess=true)
    (fa : s.flagAccess=true) (funded : 3≤s.reserve) :
    Generative.Trace (process laws) s [.readCandidate,.readFlag,.compare] (inspect laws s) ∧
    (inspect laws s).reserve+3=s.reserve ∧ (inspect laws s).spent=s.spent+3 := by
  constructor
  · apply Generative.Trace.cons (show Step laws s .readCandidate _ from ⟨⟨⟨origin,phase,module,by omega⟩,ca⟩,rfl⟩)
    apply Generative.Trace.cons
      (show Step laws (advance laws s .readCandidate) .readFlag _ from
        ⟨by simp only [Enabled,Ready,advance,pay]; exact ⟨⟨origin,trivial,module,by omega⟩,fa⟩,rfl⟩)
    apply Generative.Trace.cons
      (show Step laws (advance laws (advance laws s .readCandidate) .readFlag) .compare _ from
        ⟨by simp only [Enabled,Ready,advance,pay]; exact ⟨origin,trivial,module,by omega⟩,rfl⟩)
    exact .nil _
  · change (s.reserve-1-1-1)+3=s.reserve ∧ s.spent+1+1+1=s.spent+3
    constructor <;> omega

theorem paid_comparison_exact (laws : Laws) (s : State) (b : Bool) :
    (inspect laws s).permit=some b ↔
      s.inner.latch=some b ∧ qualification s=true ∧ b=candidate s := by
  cases hl : s.inner.latch with
  | none => simp [inspect,advance,pay,decision,hl]
  | some c =>
      cases hq : qualification s <;> cases hc : candidate s <;> cases c <;> cases b <;>
        simp [inspect,advance,pay,decision,qualification,candidate] at hq hc ⊢ <;>
        simp_all

theorem inspection_trace_exact_and_paid {laws : Laws} {s t : State}
    (trace : Generative.Trace (process laws) s [.readCandidate,.readFlag,.compare] t) :
    t=inspect laws s ∧ t.reserve+3=s.reserve ∧ t.spent=s.spent+3 := by
  cases trace with
  | cons he h =>
    rcases he with ⟨_,rfl⟩
    cases h with
    | cons he h =>
      rcases he with ⟨_,rfl⟩
      cases h with
      | cons he h =>
        rcases he with ⟨funded,rfl⟩
        cases h
        have enough := funded.2.2.2
        change 1≤s.reserve-1-1 at enough
        refine ⟨rfl,?_,?_⟩
        · change s.reserve-1-1-1+3=s.reserve
          omega
        · change s.spent+1+1+1=s.spent+3
          omega

theorem parent_command_read_is_paid (laws : Laws) (s : State)
    (enabled : Enabled s .readCommand) :
    RecipientAction.energy (advance laws s .readCommand).inner+1=RecipientAction.energy s.inner := by
  exact RecipientAction.step_energy (show RecipientAction.Step laws s.inner .read _ from ⟨enabled.2.2,rfl⟩)

theorem consume_retires_even_without_import_money (laws : Laws) (s : State)
    (origin : s.originUnused=true) (phase : s.phase=.compared) :
    Step laws s .consume (advance laws s .consume) ∧
    (advance laws s .consume).originUnused=false ∧
    (advance laws s .consume).inner=s.inner := by
  exact ⟨⟨⟨origin,phase⟩,rfl⟩,rfl,rfl⟩

theorem no_event_rearms_origin (laws : Laws) (s : State) (e : Event)
    (used : s.originUnused=false) : (advance laws s e).originUnused=false := by
  cases e <;> simp [advance,pay,used]

theorem no_trace_rearms_origin {laws : Laws} {s t : State} {es : List Event}
    (trace : Generative.Trace (process laws) s es t) (used : s.originUnused=false) :
    t.originUnused=false := by
  induction trace with
  | nil => exact used
  | cons he _ ih =>
      rcases he with ⟨_,rfl⟩
      exact ih (no_event_rearms_origin _ _ _ used)

theorem consumed_origin_blocks_new_reads (s : State) (used : s.originUnused=false) :
    ¬ Enabled s .readCommand ∧ ¬ Enabled s .readCandidate ∧ ¬ Enabled s .readFlag ∧
    ¬ Enabled s .compare := by simp [Enabled,Ready,used]

theorem instrumented_intervention_retires (laws : Laws) (s : State)
    (replacement : RecipientAction.State) :
    (advance laws s (.retire replacement)).originUnused=false ∧
    (advance laws s (.retire replacement)).permit=none ∧
    ¬ Enabled (advance laws s (.retire replacement)) .install := by
  simp [advance,Enabled]

theorem damaged_read_charges_and_retires (laws : Laws) (s : State)
    (funded : 1≤s.reserve) :
    let t := advance laws s .damagedCandidate
    t.inner=s.inner ∧ t.reserve+1=s.reserve ∧ t.spent=s.spent+1 ∧
    t.originUnused=false ∧ t.candidateLatch=none ∧ t.permit=none := by
  refine ⟨rfl,?_,rfl,rfl,rfl,rfl⟩
  change s.reserve-1+1=s.reserve
  omega

theorem guarded_import_is_paid {laws : Laws} {s t : State}
    (step : Step laws s .install t) :
    RecipientAction.Step laws s.inner .install t.inner ∧
    RecipientAction.energy t.inner+1=RecipientAction.energy s.inner ∧ t.originUnused=false := by
  rcases step with ⟨enabled,rfl⟩
  have parent : RecipientAction.Step laws s.inner .install (RecipientAction.advance laws s.inner .install) :=
    ⟨enabled.2.2.2,rfl⟩
  exact ⟨parent,RecipientAction.step_energy parent,rfl⟩

theorem accepted_command_correct (laws : Laws) (s : State) (oldLaw b : Bool)
    (sound : RecipientIdentification.Sound
      (RecipientIdentification.registers (RecipientAction.core s.inner).hardware) oldLaw)
    (stable : oldLaw=lookup laws .recipient)
    (accepted : (inspect laws s).permit=some b) : b=lookup laws .recipient := by
  have h := (paid_comparison_exact laws s b).mp accepted
  exact h.2.2.trans ((sound h.2.1).trans stable)

/- Import is still charged by the parent, with no post-write live q guard.
This theorem is explicitly restricted to that faithful transition. -/
theorem faithful_import_after_acceptance (laws : Laws) (s : State) (b : Bool)
    (accepted : (inspect laws s).permit=some b) :
    RecipientAction.core (advance laws (advance laws (inspect laws s) .consume) .install).inner =
      RecipientAction.importCore s.inner b := by
  have h := (paid_comparison_exact laws s b).mp accepted
  simp [advance,inspect,pay,RecipientAction.advance,h.1,RecipientAction.core,RecipientAction.setCore]

theorem stable_anchor_then_faithful_recipient_receipt (laws : Laws) (s : State) (oldLaw b : Bool)
    (sound : RecipientIdentification.Sound
      (RecipientIdentification.registers (RecipientAction.core s.inner).hardware) oldLaw)
    (stable : oldLaw=lookup laws .recipient)
    (accepted : (inspect laws s).permit=some b)
    (inspection : Generative.Trace (process laws) s [.readCandidate,.readFlag,.compare] (inspect laws s))
    (importEnabled : Enabled (advance laws (inspect laws s) .consume) .install)
    {t : RecipientIdentification.State} {channel : Bool}
    (trial : Generative.Trace (RecipientIdentification.process laws)
      (RecipientAction.core (advance laws (advance laws (inspect laws s) .consume) .install).inner)
      (RecipientIdentification.trial .recipient true channel) t) :
    t.patient=(RecipientAction.core s.inner).patient+10 ∧
    RecipientIdentification.actor (RecipientIdentification.registers t.hardware)=
      RecipientIdentification.actor (RecipientIdentification.registers (RecipientAction.core s.inner).hardware) ∧
    RecipientAction.energy (advance laws (advance laws (inspect laws s) .consume) .install).inner+1=
      RecipientAction.energy s.inner ∧ (inspect laws s).reserve+3=s.reserve := by
  have correct := accepted_command_correct laws s oldLaw b sound stable accepted
  have compatible : RecipientReasons.Compatible (lookup laws .recipient) b := by
    rw [correct]
    intro opportunity
    cases hz : lookup laws .recipient <;> cases opportunity <;> rfl
  rw [faithful_import_after_acceptance laws s b accepted] at trial
  have consequence := (RecipientAction.semantic_import_then_receipt s.inner b ⟨True.intro,compatible⟩ trial).2
  exact ⟨consequence.1,consequence.2,
    (guarded_import_is_paid (show Step laws _ .install _ from ⟨importEnabled,rfl⟩)).2.1,
    (inspection_trace_exact_and_paid inspection).2.1⟩

end PaidPreImport

#print axioms PaidPreImport.inspection_preserves_entire_parent
#print axioms PaidPreImport.paid_inspection_trace
#print axioms PaidPreImport.paid_comparison_exact
#print axioms PaidPreImport.inspection_trace_exact_and_paid
#print axioms PaidPreImport.parent_command_read_is_paid
#print axioms PaidPreImport.consume_retires_even_without_import_money
#print axioms PaidPreImport.no_event_rearms_origin
#print axioms PaidPreImport.no_trace_rearms_origin
#print axioms PaidPreImport.consumed_origin_blocks_new_reads
#print axioms PaidPreImport.instrumented_intervention_retires
#print axioms PaidPreImport.damaged_read_charges_and_retires
#print axioms PaidPreImport.guarded_import_is_paid
#print axioms PaidPreImport.accepted_command_correct
#print axioms PaidPreImport.faithful_import_after_acceptance
#print axioms PaidPreImport.stable_anchor_then_faithful_recipient_receipt
