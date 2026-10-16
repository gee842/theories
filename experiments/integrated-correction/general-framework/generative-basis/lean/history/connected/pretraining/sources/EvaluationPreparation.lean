import RevisionPreparation

namespace EvaluationPreparation

set_option maxRecDepth 16384
set_option maxHeartbeats 4000000

def start (fuel source : Nat) : FormedSelection.State := ⟨0,0,.empty,false,false,fuel,source⟩
def word : List FormedSelection.Event := List.replicate 9 .formA ++
  List.replicate 9 .formH ++ RevisionPreparation.word

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 60 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 60 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 60 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed (fuel source : Nat) := ArchivePreparation.run (start fuel source) word
def assemblyWord : List ArchivePreparation.Kind := List.replicate 6 .cell ++
  [.reader,.reader] ++ RevisionPreparation.assemblyWord
def prepared (fuel source : Nat) := ArchivePreparation.assemblyRun ⟨formed fuel source,0,0⟩ assemblyWord

/- The six data pairs and two supplied finite controller recipes are charged
here. A ninth free pair remains reserved for one later port assembly. -/
def parentProjection (s : ArchivePreparation.Assembly) : ArchivePreparation.Assembly :=
  { s with plant := { s.plant with aFree:=s.plant.aFree-1,hFree:=s.plant.hFree-1, fuel:=s.plant.fuel-23,source:=s.plant.source-16 },cells:=s.cells-6,readers:=s.readers-2 }

theorem prospective_formation_feasible : Runnable (start 276 200) word := by decide
theorem prospective_formation_trace : FormedSelection.Trace 60 (start 276 200) word (formed 276 200) :=
  runnable_trace prospective_formation_feasible

theorem formation_endpoint : formed 276 200=⟨29,30,.active,true,true,227,186⟩ ∧
    word.length=76 ∧ FormedSelection.tally FormedSelection.expenditure word=62 := by decide

theorem assemblies_feasible :
    ArchivePreparation.AssemblyRunnable ⟨formed 276 200,0,0⟩ assemblyWord := by decide

theorem material_partition : (prepared 276 200).plant=⟨1,2,.active,true,true,199,186⟩ ∧
    (prepared 276 200).cells=22 ∧ (prepared 276 200).readers=6 ∧
    ArchivePreparation.material (prepared 276 200)=60 := by decide

theorem exact_parent_prepared_projection :
    parentProjection (prepared 276 200)=RevisionPreparation.prepared 227 184 := by
  have ext : ∀ s t : ArchivePreparation.Assembly, s.plant=t.plant → s.cells=t.cells → s.readers=t.readers → s=t := by
    intro s t; cases s; cases t; simp_all
  apply ext
  · simp only [parentProjection,material_partition.1,RevisionPreparation.material_partition.1]
  · change (prepared 276 200).cells-6=(RevisionPreparation.prepared 227 184).cells
    rw [material_partition.2.1,RevisionPreparation.material_partition.2.1]
  · change (prepared 276 200).readers-2=(RevisionPreparation.prepared 227 184).readers
    rw [material_partition.2.2.1,RevisionPreparation.material_partition.2.2.1]

theorem original_compartments : ArchivePreparation.adapterFuel (prepared 276 200)=176+12+11 ∧
    (prepared 276 200).plant.source=170+6+10 ∧
    276+200=91+(176+170)+(12+11+6+10) ∧ 60=42+12+2+2+2 := by decide

end EvaluationPreparation

#print axioms EvaluationPreparation.runnable_trace
#print axioms EvaluationPreparation.prospective_formation_feasible
#print axioms EvaluationPreparation.prospective_formation_trace
#print axioms EvaluationPreparation.formation_endpoint
#print axioms EvaluationPreparation.assemblies_feasible
#print axioms EvaluationPreparation.material_partition
#print axioms EvaluationPreparation.exact_parent_prepared_projection
#print axioms EvaluationPreparation.original_compartments
