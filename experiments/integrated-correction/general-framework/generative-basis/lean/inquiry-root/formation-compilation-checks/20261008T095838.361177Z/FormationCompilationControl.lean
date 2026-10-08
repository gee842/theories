import FormedSelection

namespace FormationCompilationControl
open FormedSelection
set_option backward.match.sparseCases true
namespace Legacy

def bit : Bool → Nat | false => 0 | true => 1

def occupied : Resident → Nat | .empty => 0 | _ => 1

def activeResident : Resident → Nat | .active => 1 | _ => 0

def alternativeResident : Resident → Nat | .alternative => 1 | _ => 0

def population (s : State) : Nat := s.aFree + s.hFree + occupied s.resident

def aCount (s : State) : Nat := s.aFree + activeResident s.resident

def hCount (s : State) : Nat := s.hFree + alternativeResident s.resident

def precursor (material : Nat) (s : State) : Nat := material - population s

def Valid (material : Nat) (s : State) : Prop := population s ≤ material

def Enabled (material : Nat) (s : State) : Event → Prop
  | .formA | .formH => s.intact = false ∧ population s < material ∧ 0 < s.fuel
  | .associateA => 0 < s.aFree ∧ s.resident = .empty ∧ 0 < s.fuel
  | .associateH => 0 < s.hFree ∧ s.resident = .empty ∧ 0 < s.fuel
  | .repair => s.resident = .active ∧ s.intact = false ∧ 0 < s.fuel
  | .capture => s.intact = true ∧ s.localFuel = false ∧ 0 < s.source
  | .localCopyA => s.resident = .active ∧ s.localFuel = true ∧ population s < material
  | .localCopyH => s.resident = .alternative ∧ s.localFuel = true ∧ population s < material
  | .bulkCopyA => 0 < aCount s ∧ population s < material ∧ 0 < s.fuel
  | .bulkCopyH => 0 < hCount s ∧ population s < material ∧ 0 < s.fuel
  | .wearFreeA => 0 < s.aFree
  | .wearFreeH => 0 < s.hFree
  | .wearResident => s.resident ≠ .empty
  | .damage => s.intact = true
  | .leakCommon => 0 < s.fuel
  | .leakLocal => s.localFuel = true

def advance (s : State) : Event → State
  | .formA => { s with aFree := s.aFree + 1, fuel := s.fuel - 1 }
  | .formH => { s with hFree := s.hFree + 1, fuel := s.fuel - 1 }
  | .associateA => { s with aFree := s.aFree - 1, resident := .active, fuel := s.fuel - 1 }
  | .associateH => { s with hFree := s.hFree - 1, resident := .alternative, fuel := s.fuel - 1 }
  | .repair => { s with intact := true, fuel := s.fuel - 1 }
  | .capture => { s with localFuel := true, source := s.source - 1 }
  | .localCopyA => { s with aFree := s.aFree + 1, localFuel := false }
  | .localCopyH => { s with hFree := s.hFree + 1, localFuel := false }
  | .bulkCopyA => { s with aFree := s.aFree + 1, fuel := s.fuel - 1 }
  | .bulkCopyH => { s with hFree := s.hFree + 1, fuel := s.fuel - 1 }
  | .wearFreeA => { s with aFree := s.aFree - 1 }
  | .wearFreeH => { s with hFree := s.hFree - 1 }
  | .wearResident => { s with resident := .empty }
  | .damage => { s with intact := false }
  | .leakCommon => { s with fuel := s.fuel - 1 }
  | .leakLocal => { s with localFuel := false }

def Step (material : Nat) (s : State) (a : Event) (t : State) : Prop :=
  Valid material s ∧ Enabled material s a ∧ t = advance s a

def expenditure : Event → Nat
  | .capture | .wearFreeA | .wearFreeH | .wearResident | .damage => 0
  | _ => 1

def commonExpenditure : Event → Nat
  | .formA | .formH | .associateA | .associateH | .repair
  | .bulkCopyA | .bulkCopyH | .leakCommon => 1
  | _ => 0

def copyIncrement : Event → Nat
  | .localCopyA | .localCopyH | .bulkCopyA | .bulkCopyH => 1
  | _ => 0

def eventIndicator (target : Event) (a : Event) : Nat := if a = target then 1 else 0

def tally (weight : Event → Nat) : List Event → Nat
  | [] => 0
  | a :: as => weight a + tally weight as

def energy (s : State) : Nat := s.fuel + s.source + bit s.localFuel

def rank (s : State) : Nat :=
  4 * s.source + 2 * s.fuel + 2 * bit s.localFuel + bit s.intact + population s

def rankDrop : Event → Nat
  | .associateA | .associateH | .capture | .leakCommon | .leakLocal => 2
  | _ => 1

def phase (s : State) : Nat :=
  if s.intact then 3 else
    match s.resident with
    | .empty => min 1 (s.aFree + s.hFree)
    | _ => 2

def Absent (s : State) : Prop :=
  s.aFree = 0 ∧ s.hFree = 0 ∧ s.resident = .empty

def mixedPhase (s : State) : Nat :=
  (if s.intact then 3 else
    match s.resident with
    | .active => 2
    | _ => min 1 (aCount s)) + min 1 (hCount s)

def SupportOwned (s : State) : Prop :=
  s.resident ≠ .active → s.intact = false ∧ s.localFuel = false

def initial : State := ⟨0, 0, .empty, false, false, 4, 1⟩

def formedH : State := ⟨0, 1, .empty, false, false, 3, 1⟩

def formed : State := ⟨1, 1, .empty, false, false, 2, 1⟩

def associated : State := ⟨0, 1, .active, false, false, 1, 1⟩

def repaired : State := ⟨0, 1, .active, true, false, 0, 1⟩

def captured : State := ⟨0, 1, .active, true, true, 0, 0⟩

def copied : State := ⟨1, 1, .active, true, false, 0, 0⟩

def witnessEvents : List Event := [.formH, .formA, .associateA, .repair, .capture, .localCopyA]

def inheritanceInitial : State := ⟨0, 0, .empty, false, false, 5, 1⟩

def inheritanceFinal : State := ⟨0, 1, .alternative, true, false, 0, 0⟩

def inheritanceEvents : List Event :=
  [.formA, .formH, .associateA, .repair, .wearResident, .associateH, .capture, .localCopyH]

end Legacy
set_option backward.match.sparseCases false

theorem enabled_same (material : Nat) (s : State) (a : Event) :
    Legacy.Enabled material s a ↔ FormedSelection.Enabled material s a := by
  cases s with
  | mk af hf resident intact localFuel fuel source =>
    cases a <;> cases resident <;> rfl

theorem advance_same (s : State) (a : Event) :
    Legacy.advance s a = FormedSelection.advance s a := by
  cases a <;> rfl

theorem step_same (material : Nat) (s t : State) (a : Event) :
    Legacy.Step material s a t ↔ FormedSelection.Step material s a t := by
  cases s with
  | mk af hf resident intact localFuel fuel source =>
    cases a <;> cases resident <;> rfl

theorem expenditure_same (a : Event) :
    Legacy.expenditure a = FormedSelection.expenditure a := by
  cases a <;> rfl

theorem common_expenditure_same (a : Event) :
    Legacy.commonExpenditure a = FormedSelection.commonExpenditure a := by
  cases a <;> rfl

theorem copy_increment_same (a : Event) :
    Legacy.copyIncrement a = FormedSelection.copyIncrement a := by
  cases a <;> rfl

theorem rank_drop_same (a : Event) :
    Legacy.rankDrop a = FormedSelection.rankDrop a := by
  cases a <;> rfl

#print axioms Legacy.bit
#print axioms Legacy.occupied
#print axioms Legacy.activeResident
#print axioms Legacy.alternativeResident
#print axioms Legacy.population
#print axioms Legacy.aCount
#print axioms Legacy.hCount
#print axioms Legacy.precursor
#print axioms Legacy.Valid
#print axioms Legacy.Enabled
#print axioms Legacy.advance
#print axioms Legacy.Step
#print axioms Legacy.expenditure
#print axioms Legacy.commonExpenditure
#print axioms Legacy.copyIncrement
#print axioms Legacy.eventIndicator
#print axioms Legacy.tally
#print axioms Legacy.energy
#print axioms Legacy.rank
#print axioms Legacy.rankDrop
#print axioms Legacy.phase
#print axioms Legacy.Absent
#print axioms Legacy.mixedPhase
#print axioms Legacy.SupportOwned
#print axioms Legacy.initial
#print axioms Legacy.formedH
#print axioms Legacy.formed
#print axioms Legacy.associated
#print axioms Legacy.repaired
#print axioms Legacy.captured
#print axioms Legacy.copied
#print axioms Legacy.witnessEvents
#print axioms Legacy.inheritanceInitial
#print axioms Legacy.inheritanceFinal
#print axioms Legacy.inheritanceEvents
#print axioms enabled_same
#print axioms advance_same
#print axioms step_same
#print axioms expenditure_same
#print axioms common_expenditure_same
#print axioms copy_increment_same
#print axioms rank_drop_same
end FormationCompilationControl
