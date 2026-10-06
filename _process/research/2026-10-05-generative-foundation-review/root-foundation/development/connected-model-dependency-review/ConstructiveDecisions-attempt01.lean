import EvaluativeSuccession

/-!
# Constructive counterparts of existing finite decision functions

The original source functions are unchanged. Exhaustive case analysis avoids
the generated sparse-match proof helpers that introduced propext into those
definitions. Pointwise equivalence is proved over their full input domains.
The equivalence statements still name the original definitions and therefore
retain their original named dependencies. No replacement is installed in the
existing process, and no transition law or ethical ground is added.
-/

namespace Generative.ConstructiveDecisions

open RecipientCorrection (Target Laws lookup packedAct receiptOf)
open RecipientIdentification (Phase Registers State Event)

def route (m : ReasonReplay.Mask) : Option Bool :=
  match m.p with
  | false => match m.q with
    | false => none
    | true => some true
  | true => match m.q with
    | false => some false
    | true => none

def targetOf : Phase → Target
  | .ready => .actor
  | .rented => .actor
  | .sensed target => target
  | .reserved target => target
  | .worked target _ => target
  | .acquired target _ => target

def requiredEscrow : Phase → Nat
  | .ready => 0
  | .rented => 0
  | .sensed _ => 0
  | .reserved _ => 3
  | .worked _ _ => 3
  | .acquired _ _ => 2

def acquiredRecord : Phase → Option Bool
  | .ready => none
  | .rented => none
  | .sensed _ => none
  | .reserved _ => none
  | .worked _ _ => none
  | .acquired _ record => record

def feedback (m : Registers) (target : Target) (record : Option Bool) : Registers :=
  match target with
  | .actor => m
  | .recipient => match record with
    | none => m
    | some received => RecipientIdentification.revise m received

def returned (laws : Laws) (s : State) (available : Bool) : Bool :=
  receiptOf (packedAct s.hardware.q (targetOf s.phase))
    (lookup laws (targetOf s.phase)) available

def identificationAdvance (laws : Laws) (s : State) : Event → State
  | .rent => {s with hardware := {s.hardware with fuel := s.hardware.fuel - 1}, phase := .rented}
  | .sense target => {s with hardware := {s.hardware with fuel := s.hardware.fuel - 1}, phase := .sensed target}
  | .reserve => {s with hardware := {s.hardware with fuel := s.hardware.fuel - 3}, escrow := 3, phase := .reserved (targetOf s.phase)}
  | .work available => {s with
      hardware := {s.hardware with fuel := s.hardware.fuel - 3 + RecipientIdentification.credit (targetOf s.phase) (returned laws s available)},
      patient := s.patient + RecipientIdentification.patientCredit (targetOf s.phase) (returned laws s available),
      packets := s.packets - 1, phase := .worked (targetOf s.phase) (returned laws s available)}
  | .acquire channel => {s with escrow := s.escrow - 1, phase :=
      match s.phase with
      | .ready => s.phase
      | .rented => s.phase
      | .sensed _ => s.phase
      | .reserved _ => s.phase
      | .worked target received => .acquired target (if channel then some received else none)
      | .acquired _ _ => s.phase}
  | .write => {s with
      hardware := RecipientIdentification.setRegisters s.hardware
        (feedback (RecipientIdentification.registers s.hardware) (targetOf s.phase) (acquiredRecord s.phase)),
      escrow := s.escrow - 2, phase := .ready}
  | .miss => {s with active := false, packets := s.packets - 1}

def archiveLatch (p : EmissionArchive.Producer W E H R)
    (s : EmissionArchive.State W H R) (e : E) (w : W) : EmissionArchive.Phase H R :=
  match s.phase with
  | .idle => s.phase
  | .bound i header => match p.emission header s.world e w with
    | none => s.phase
    | some record => .latched i record []
  | .latched _ _ _ => s.phase

def archiveAdvance (p : EmissionArchive.Producer W E H R)
    (s : EmissionArchive.State W H R) : EmissionArchive.Event W E H → EmissionArchive.State W H R
  | .bind i header => {s with budget := s.budget - 5, escrow := 4, blanks := s.blanks - 4, phase := .bound i header}
  | .core e w => {s with world := w, phase := archiveLatch p s e w}
  | .write => match s.phase with
    | .idle => s
    | .bound _ _ => s
    | .latched i record bits =>
        if bits.length = 3 then
          {s with escrow := s.escrow - 1, records := EmissionArchive.put s.records i record, phase := .idle}
        else
          {s with escrow := s.escrow - 1, phase := .latched i record ((p.encode record).take (bits.length + 1))}

theorem route_eq (m : ReasonReplay.Mask) : route m = RecipientAction.route m := by
  cases m with
  | mk p q => cases p <;> cases q <;> rfl

theorem targetOf_eq (phase : Phase) : targetOf phase = RecipientIdentification.targetOf phase := by
  cases phase <;> rfl

theorem requiredEscrow_eq (phase : Phase) : requiredEscrow phase = RecipientIdentification.requiredEscrow phase := by
  cases phase <;> rfl

theorem acquiredRecord_eq (phase : Phase) : acquiredRecord phase = RecipientIdentification.acquiredRecord phase := by
  cases phase <;> rfl

theorem feedback_eq (m : Registers) (target : Target) (record : Option Bool) :
    feedback m target record = RecipientIdentification.feedback m target record := by
  cases target <;> cases record <;> rfl

theorem returned_eq (laws : Laws) (s : State) (available : Bool) :
    returned laws s available = RecipientIdentification.returned laws s available := by
  unfold returned RecipientIdentification.returned RecipientIdentification.issued
  rw [targetOf_eq]

theorem identificationAdvance_eq (laws : Laws) (s : State) (e : Event) :
    identificationAdvance laws s e = RecipientIdentification.advance laws s e := by
  cases e with
  | rent | sense target | miss => rfl
  | reserve => simp only [identificationAdvance, RecipientIdentification.advance, targetOf_eq]
  | work available => simp only [identificationAdvance, RecipientIdentification.advance, targetOf_eq, returned_eq]
  | acquire channel => cases hp : s.phase <;> simp only [identificationAdvance, RecipientIdentification.advance, hp]
  | write => simp only [identificationAdvance, RecipientIdentification.advance, targetOf_eq, acquiredRecord_eq, feedback_eq]

theorem archiveLatch_eq (p : EmissionArchive.Producer W E H R)
    (s : EmissionArchive.State W H R) (e : E) (w : W) :
    archiveLatch p s e w = EmissionArchive.latch p s e w := by
  cases hp : s.phase <;> simp only [archiveLatch, EmissionArchive.latch, hp]

theorem archiveAdvance_eq (p : EmissionArchive.Producer W E H R)
    (s : EmissionArchive.State W H R) (e : EmissionArchive.Event W E H) :
    archiveAdvance p s e = EmissionArchive.advance p s e := by
  cases e with
  | bind i header => rfl
  | core event successor => simp only [archiveAdvance, EmissionArchive.advance, archiveLatch_eq]
  | write => cases hp : s.phase <;> simp only [archiveAdvance, EmissionArchive.advance, hp]

end Generative.ConstructiveDecisions

#print axioms Generative.ConstructiveDecisions.route
#print axioms Generative.ConstructiveDecisions.targetOf
#print axioms Generative.ConstructiveDecisions.requiredEscrow
#print axioms Generative.ConstructiveDecisions.acquiredRecord
#print axioms Generative.ConstructiveDecisions.feedback
#print axioms Generative.ConstructiveDecisions.returned
#print axioms Generative.ConstructiveDecisions.identificationAdvance
#print axioms Generative.ConstructiveDecisions.archiveLatch
#print axioms Generative.ConstructiveDecisions.archiveAdvance
#print axioms Generative.ConstructiveDecisions.route_eq
#print axioms Generative.ConstructiveDecisions.targetOf_eq
#print axioms Generative.ConstructiveDecisions.requiredEscrow_eq
#print axioms Generative.ConstructiveDecisions.acquiredRecord_eq
#print axioms Generative.ConstructiveDecisions.feedback_eq
#print axioms Generative.ConstructiveDecisions.returned_eq
#print axioms Generative.ConstructiveDecisions.identificationAdvance_eq
#print axioms Generative.ConstructiveDecisions.archiveLatch_eq
#print axioms Generative.ConstructiveDecisions.archiveAdvance_eq
