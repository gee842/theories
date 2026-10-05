import ActionPreparation

namespace RevisionPreparation

set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

def start (fuel source : Nat) : FormedSelection.State := ⟨0,0,.empty,false,false,fuel,source⟩
def word : List FormedSelection.Event := List.replicate 5 .formA ++
  List.replicate 5 .formH ++ ActionPreparation.word

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 42 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 42 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 42 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed (fuel source : Nat) := ArchivePreparation.run (start fuel source) word
def assemblyWord : List ArchivePreparation.Kind := List.replicate 4 .cell ++ [.reader] ++ ActionPreparation.assemblyWord
def prepared (fuel source : Nat) := ArchivePreparation.assemblyRun ⟨formed fuel source,0,0⟩ assemblyWord


def parentProjection (s : ArchivePreparation.Assembly) : ArchivePreparation.Assembly :=
  { s with plant := { s.plant with fuel := s.plant.fuel-57, source := s.plant.source-30 }, cells := s.cells-4, readers := s.readers-1 }

theorem prospective_formation_feasible : Runnable (start 227 184) word := by decide

theorem prospective_formation_trace : FormedSelection.Trace 42 (start 227 184) word (formed 227 184) :=
  runnable_trace prospective_formation_feasible

theorem formation_endpoint : formed 227 184=⟨20,21,.active,true,true,196,170⟩ ∧
    word.length=58 ∧ FormedSelection.tally FormedSelection.expenditure word=44 := by decide

theorem assemblies_feasible :
    ArchivePreparation.AssemblyRunnable ⟨formed 227 184,0,0⟩ assemblyWord := by decide

theorem material_partition : (prepared 227 184).plant=⟨0,1,.active,true,true,176,170⟩ ∧
    (prepared 227 184).cells=16 ∧ (prepared 227 184).readers=4 ∧
    ArchivePreparation.material (prepared 227 184)=42 := by decide

theorem exact_parent_prepared_projection :
    parentProjection (prepared 227 184)=ActionPreparation.prepared 155 154 := by
  have ext : ∀ s t : ArchivePreparation.Assembly,
      s.plant=t.plant → s.cells=t.cells → s.readers=t.readers → s=t := by
    intro s t; cases s; cases t; simp_all
  apply ext
  · simp only [parentProjection,material_partition.1,ActionPreparation.actual_material_partition.1]
  · change (prepared 227 184).cells-4=(ActionPreparation.prepared 155 154).cells
    rw [material_partition.2.1,ActionPreparation.actual_material_partition.2.1]
  · change (prepared 227 184).readers-1=(ActionPreparation.prepared 155 154).readers
    rw [material_partition.2.2.1,ActionPreparation.actual_material_partition.2.2.1]

theorem original_accounts : ArchivePreparation.adapterFuel (prepared 227 184)=119+28+5+24 ∧
    (prepared 227 184).plant.source=140+30 ∧ 227+184=65+(119+28+5+24+140+30) := by decide

theorem inherited_full_bank_has_no_spare_cells :
    (ActionPreparation.prepared 155 154).plant.aFree=0 ∧
    ¬ ArchivePreparation.enabled (ActionPreparation.prepared 155 154) := by decide

theorem prospective_whole_accounts :
    411=65+78+54+15+72+10+57+10+50 := by decide

end RevisionPreparation

#print axioms RevisionPreparation.runnable_trace
#print axioms RevisionPreparation.prospective_formation_feasible
#print axioms RevisionPreparation.prospective_formation_trace
#print axioms RevisionPreparation.formation_endpoint
#print axioms RevisionPreparation.assemblies_feasible
#print axioms RevisionPreparation.material_partition
#print axioms RevisionPreparation.exact_parent_prepared_projection
#print axioms RevisionPreparation.original_accounts
#print axioms RevisionPreparation.inherited_full_bank_has_no_spare_cells
#print axioms RevisionPreparation.prospective_whole_accounts
