import EvaluationPreparation

namespace SuccessionPreparation

set_option maxRecDepth 16384
set_option maxHeartbeats 4000000

def start (fuel source : Nat) : FormedSelection.State := ⟨0,0,.empty,false,false,fuel,source⟩
def word : List FormedSelection.Event := List.replicate 9 .formA ++
  List.replicate 9 .formH ++ EvaluationPreparation.word

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 78 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 78 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 78 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed (fuel source : Nat) := ArchivePreparation.run (start fuel source) word
def assemblyWord : List ArchivePreparation.Kind := EvaluationPreparation.assemblyWord
def prepared (fuel source : Nat) := ArchivePreparation.assemblyRun ⟨formed fuel source,0,0⟩ assemblyWord

/- Nine NEW pairs stay held through the accepted donor history. -/
def parentProjection (s : ArchivePreparation.Assembly) : ArchivePreparation.Assembly :=
  { s with plant := { s.plant with aFree:=s.plant.aFree-9,hFree:=s.plant.hFree-9, fuel:=s.plant.fuel-66,source:=s.plant.source-30 } }

theorem prospective_formation_feasible : Runnable (start 360 230) word := by decide
theorem prospective_formation_trace : FormedSelection.Trace 78 (start 360 230) word (formed 360 230) :=
  runnable_trace prospective_formation_feasible

theorem formation_endpoint : formed 360 230=⟨38,39,.active,true,true,293,216⟩ ∧
    word.length=94 ∧ FormedSelection.tally FormedSelection.expenditure word=80 := by decide

theorem assemblies_feasible :
    ArchivePreparation.AssemblyRunnable ⟨formed 360 230,0,0⟩ assemblyWord := by decide

theorem material_partition : (prepared 360 230).plant=⟨10,11,.active,true,true,265,216⟩ ∧
    (prepared 360 230).cells=22 ∧ (prepared 360 230).readers=6 ∧
    ArchivePreparation.material (prepared 360 230)=78 := by decide

theorem exact_parent_prepared_projection :
    parentProjection (prepared 360 230)=EvaluationPreparation.prepared 276 200 := by
  have ext : ∀ s t : ArchivePreparation.Assembly, s.plant=t.plant → s.cells=t.cells → s.readers=t.readers → s=t := by
    intro s t; cases s; cases t; simp_all
  apply ext
  · simp only [parentProjection,material_partition.1,EvaluationPreparation.material_partition.1]
  · change (prepared 360 230).cells=(EvaluationPreparation.prepared 276 200).cells
    rw [material_partition.2.1,EvaluationPreparation.material_partition.2.1]
  · change (prepared 360 230).readers=(EvaluationPreparation.prepared 276 200).readers
    rw [material_partition.2.2.1,EvaluationPreparation.material_partition.2.2.1]

theorem original_compartments : ArchivePreparation.adapterFuel (prepared 360 230)=199+66 ∧
    (prepared 360 230).plant.source=186+30 ∧
    360+230=276+200+18+66+30 ∧ 78=60+18 := by decide

end SuccessionPreparation

#print axioms SuccessionPreparation.runnable_trace
#print axioms SuccessionPreparation.prospective_formation_feasible
#print axioms SuccessionPreparation.prospective_formation_trace
#print axioms SuccessionPreparation.formation_endpoint
#print axioms SuccessionPreparation.assemblies_feasible
#print axioms SuccessionPreparation.material_partition
#print axioms SuccessionPreparation.exact_parent_prepared_projection
#print axioms SuccessionPreparation.original_compartments
