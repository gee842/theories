import GenerativeCore
import FormedSelection

namespace ArchivePreparation

set_option maxRecDepth 4000

def start : FormedSelection.State := ⟨0,0,.empty,false,false,91,144⟩
def word : List FormedSelection.Event :=
  List.replicate 14 .formH ++ [.formA,.associateA,.repair] ++
  (List.replicate 13 [.capture,.localCopyA]).flatten ++ [.capture]

def run (s : FormedSelection.State) : List FormedSelection.Event → FormedSelection.State
  | [] => s
  | e::es => run (FormedSelection.advance s e) es

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 28 s e (FormedSelection.advance s e) ∧
      Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _ := runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 28 s e (FormedSelection.advance s e) ∧
        Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 28 s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed : FormedSelection.State := ⟨13,14,.active,true,true,74,130⟩

theorem actual_formation_feasible : Runnable start word := by decide

theorem actual_formation_endpoint : run start word = formed := by decide

theorem actual_formation_trace : FormedSelection.Trace 28 start word formed := by
  rw [← actual_formation_endpoint]
  exact runnable_trace actual_formation_feasible

theorem actual_formation_accounts :
    word.length = 44 ∧ FormedSelection.tally FormedSelection.expenditure word = 30 ∧
    FormedSelection.energy formed + 30 = FormedSelection.energy start ∧
    FormedSelection.population formed = 28 := by decide

structure Assembly where
  plant : FormedSelection.State
  cells : Nat
  readers : Nat
  deriving DecidableEq, Repr

inductive Kind where
  | cell | reader
  deriving DecidableEq, Repr

def material (s : Assembly) : Nat := FormedSelection.population s.plant+2*s.cells+2*s.readers

def enabled (s : Assembly) : Prop := 0 < s.plant.aFree ∧ 0 < s.plant.hFree ∧ 0 < s.plant.fuel

def assemble (s : Assembly) (k : Kind) : Assembly :=
  ⟨{s.plant with aFree := s.plant.aFree-1, hFree := s.plant.hFree-1, fuel := s.plant.fuel-1},
    s.cells+(if k=.cell then 1 else 0),s.readers+(if k=.reader then 1 else 0)⟩

theorem assembly_material (s : Assembly) (k : Kind) (h : enabled s) :
    material (assemble s k) = material s := by
  cases k <;> simp [material,assemble,FormedSelection.population]
  all_goals simp only [enabled] at h; omega

theorem assembly_energy (s : Assembly) (k : Kind) (h : enabled s) :
    FormedSelection.energy (assemble s k).plant+1 = FormedSelection.energy s.plant := by
  simp [assemble,FormedSelection.energy]
  simp only [enabled] at h; omega

def assemblyRun (s : Assembly) : List Kind → Assembly
  | [] => s
  | k::ks => assemblyRun (assemble s k) ks

def AssemblyRunnable (s : Assembly) : List Kind → Prop
  | [] => True
  | k::ks => enabled s ∧ AssemblyRunnable (assemble s k) ks

instance (s : Assembly) : Decidable (enabled s) := by unfold enabled; infer_instance
instance assemblyRunnableDecidable (s : Assembly) (ks : List Kind) : Decidable (AssemblyRunnable s ks) :=
  match ks with
  | [] => isTrue trivial
  | k::ks =>
      let _ := assemblyRunnableDecidable (assemble s k) ks
      inferInstanceAs (Decidable (enabled s ∧ AssemblyRunnable (assemble s k) ks))

def assemblyWord : List Kind := List.replicate 12 .cell ++ [.reader]
def assembled : Assembly := assemblyRun ⟨formed,0,0⟩ assemblyWord

theorem actual_assembly_feasible : AssemblyRunnable ⟨formed,0,0⟩ assemblyWord := by decide

theorem actual_assembly_endpoint :
    assembled = ⟨⟨0,1,.active,true,true,61,130⟩,12,1⟩ ∧ material assembled = 28 := by decide

/- The adapter pays its existing charge and transfers the actual local unit.
The declared freeze prevents bound archive/reader parts reentering formation. -/
def adapterFuel (s : Assembly) : Nat := s.plant.fuel-1+FormedSelection.bit s.plant.localFuel

def workingFuel : Nat := adapterFuel assembled - 15 - 20

theorem original_stocks_partition :
    workingFuel = 26 ∧ adapterFuel assembled = workingFuel+15+20 ∧
    assembled.plant.source = 13*10 ∧ 2*assembled.cells+2*assembled.readers+2=28 := by decide

theorem construction_ledger :
    91+144 = 30+13+1+(workingFuel+15+20+13*10) := by decide

theorem primary_whole_ledger :
    91+144 = 44+78+54+15+14+(4+20+6) := by decide

end ArchivePreparation

#print axioms ArchivePreparation.runnable_trace
#print axioms ArchivePreparation.actual_formation_feasible
#print axioms ArchivePreparation.actual_formation_endpoint
#print axioms ArchivePreparation.actual_formation_trace
#print axioms ArchivePreparation.actual_formation_accounts
#print axioms ArchivePreparation.assembly_material
#print axioms ArchivePreparation.assembly_energy
#print axioms ArchivePreparation.actual_assembly_feasible
#print axioms ArchivePreparation.actual_assembly_endpoint
#print axioms ArchivePreparation.original_stocks_partition
#print axioms ArchivePreparation.construction_ledger
#print axioms ArchivePreparation.primary_whole_ledger
