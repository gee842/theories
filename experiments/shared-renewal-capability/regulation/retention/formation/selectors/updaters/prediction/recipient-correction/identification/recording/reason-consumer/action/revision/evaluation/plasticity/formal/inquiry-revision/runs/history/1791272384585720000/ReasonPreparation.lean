import ArchivePreparation

namespace ReasonPreparation

set_option maxRecDepth 8192

def start (fuel : Nat) : FormedSelection.State := ⟨0,0,.empty,false,false,fuel,144⟩
def word : List FormedSelection.Event := List.replicate 15 .formH ++
  [.formA,.formA,.associateA,.repair] ++
  (List.replicate 13 [.capture,.localCopyA]).flatten ++ [.capture]

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | []=>True
  | e::es=>FormedSelection.Step 30 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | []=>isTrue trivial
  | e::es=>
      let _:=runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 30 s e (FormedSelection.advance s e) ∧
        Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 30 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed (fuel : Nat) := ArchivePreparation.run (start fuel) word

def assemblyWord : List ArchivePreparation.Kind := List.replicate 12 .cell ++ [.reader,.reader]
def prepared (fuel : Nat) := ArchivePreparation.assemblyRun ⟨formed fuel,0,0⟩ assemblyWord

def common (fuel : Nat) : Nat := ArchivePreparation.adapterFuel (prepared fuel)
def protectedReserve (fuel : Nat) : Nat := common fuel-26-15-20

theorem actual_formation_feasible : Runnable (start 122) word := by decide

theorem actual_formation_trace : FormedSelection.Trace 30 (start 122) word (formed 122) :=
  runnable_trace actual_formation_feasible

theorem actual_formation_endpoint :
    formed 122=⟨14,15,.active,true,true,103,130⟩ ∧ word.length=46 ∧
    FormedSelection.tally FormedSelection.expenditure word=32 := by decide

theorem actual_assemblies_feasible :
    ArchivePreparation.AssemblyRunnable ⟨formed 122,0,0⟩ assemblyWord := by decide

theorem actual_material_partition :
    (prepared 122).plant=⟨0,1,.active,true,true,89,130⟩ ∧
    (prepared 122).cells=12 ∧ (prepared 122).readers=2 ∧
    ArchivePreparation.material (prepared 122)=30 := by decide

theorem original_energy_partition :
    common 122=26+15+20+28 ∧ (prepared 122).plant.source=13*10 ∧
    122+144=47+(26+15+20+28+13*10) := by decide

theorem boundary_preparations_feasible :
    Runnable (start 97) word ∧ Runnable (start 98) word ∧ Runnable (start 121) word ∧
    ArchivePreparation.AssemblyRunnable ⟨formed 97,0,0⟩ assemblyWord ∧
    ArchivePreparation.AssemblyRunnable ⟨formed 98,0,0⟩ assemblyWord ∧
    ArchivePreparation.AssemblyRunnable ⟨formed 121,0,0⟩ assemblyWord := by decide

theorem exact_paid_capacity_boundaries :
    protectedReserve 97=3 ∧ protectedReserve 98=4 ∧
    protectedReserve 121=27 ∧ protectedReserve 122=28 ∧
    6+protectedReserve 97<10 ∧ 6+protectedReserve 98=10 ∧
    6+protectedReserve 121<10+24 ∧ 6+protectedReserve 122=10+24 := by decide

theorem primary_whole_ledger_arithmetic :
    122+144=47+78+54+15+28+20+24 := by decide

end ReasonPreparation

#print axioms ReasonPreparation.runnable_trace
#print axioms ReasonPreparation.actual_formation_feasible
#print axioms ReasonPreparation.actual_formation_trace
#print axioms ReasonPreparation.actual_formation_endpoint
#print axioms ReasonPreparation.actual_assemblies_feasible
#print axioms ReasonPreparation.actual_material_partition
#print axioms ReasonPreparation.original_energy_partition
#print axioms ReasonPreparation.boundary_preparations_feasible
#print axioms ReasonPreparation.exact_paid_capacity_boundaries
#print axioms ReasonPreparation.primary_whole_ledger_arithmetic
