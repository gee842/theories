import RevisionPreparation

namespace PlasticityPreparation
set_option maxRecDepth 16384
set_option maxHeartbeats 4000000

def start : FormedSelection.State := ⟨0,0,.empty,false,false,297,208⟩
def word : List FormedSelection.Event := List.replicate 13 .formA ++
  List.replicate 13 .formH ++ RevisionPreparation.word

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 68 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es
instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => let _:=runnableDecidable (FormedSelection.advance s e) es
            inferInstanceAs (Decidable (FormedSelection.Step 68 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es))
theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 68 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)
def formed := ArchivePreparation.run start word
def assemblyWord : List ArchivePreparation.Kind := List.replicate 8 .cell ++
  [.reader,.reader] ++ RevisionPreparation.assemblyWord
def prepared := ArchivePreparation.assemblyRun ⟨formed,0,0⟩ assemblyWord
/- The new bound hardware and three free pairs are real retained inventory;
   the projection removes their isolated accounts, not their physical history. -/
def parentProjection (s : ArchivePreparation.Assembly) : ArchivePreparation.Assembly :=
  { s with plant:={s.plant with aFree:=s.plant.aFree-3,hFree:=s.plant.hFree-3, fuel:=s.plant.fuel-34,source:=s.plant.source-24},cells:=s.cells-8,readers:=s.readers-2 }
theorem formation_feasible : Runnable start word := by decide
theorem formation_trace : FormedSelection.Trace 68 start word formed := runnable_trace formation_feasible
theorem formation_endpoint : formed=⟨33,34,.active,true,true,240,194⟩ ∧
    FormedSelection.tally FormedSelection.expenditure word=70 := by decide
theorem assembly_feasible : ArchivePreparation.AssemblyRunnable ⟨formed,0,0⟩ assemblyWord := by decide
theorem material_partition : prepared.plant=⟨3,4,.active,true,true,210,194⟩ ∧
    prepared.cells=24 ∧ prepared.readers=6 ∧ ArchivePreparation.material prepared=68 := by decide
theorem exact_parent_preparation : parentProjection prepared=RevisionPreparation.prepared 227 184 := by
  have ext : ∀ s t : ArchivePreparation.Assembly, s.plant=t.plant → s.cells=t.cells → s.readers=t.readers → s=t := by
    intro s t; cases s; cases t; simp_all
  apply ext
  · simp only [parentProjection,material_partition.1,RevisionPreparation.material_partition.1]
  · change prepared.cells-8=(RevisionPreparation.prepared 227 184).cells
    rw [material_partition.2.1,RevisionPreparation.material_partition.2.1]
  · change prepared.readers-2=(RevisionPreparation.prepared 227 184).readers
    rw [material_partition.2.2.1,RevisionPreparation.material_partition.2.2.1]
theorem protected_accounts : ArchivePreparation.adapterFuel prepared=176+22+12 ∧
    prepared.plant.source=170+12+12 ∧ 505=101+176+170+22+12+24 ∧
    68=42+16+2+2+4+2 := by decide
end PlasticityPreparation

#print axioms PlasticityPreparation.runnable_trace
#print axioms PlasticityPreparation.formation_feasible
#print axioms PlasticityPreparation.formation_trace
#print axioms PlasticityPreparation.formation_endpoint
#print axioms PlasticityPreparation.assembly_feasible
#print axioms PlasticityPreparation.material_partition
#print axioms PlasticityPreparation.exact_parent_preparation
#print axioms PlasticityPreparation.protected_accounts
