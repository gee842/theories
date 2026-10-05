import ActionPreparation

namespace InspectionPreparation

set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

def start := ActionPreparation.start
def word : List FormedSelection.Event := List.replicate 17 .formH ++
  [.formA,.formA,.formA,.formA,.associateA,.repair] ++
  (List.replicate 13 [.capture,.localCopyA]).flatten ++ [.capture]

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 34 s e (FormedSelection.advance s e) ∧
      Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) :
    Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _ := runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 34 s e (FormedSelection.advance s e) ∧
        Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 34 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed := ArchivePreparation.run (start 161 154) word
def assemblyWord : List ArchivePreparation.Kind := List.replicate 12 .cell ++
  [.reader,.reader,.reader,.reader]
def prepared := ArchivePreparation.assemblyRun ⟨formed,0,0⟩ assemblyWord

theorem actual_formation_feasible : Runnable (start 161 154) word := by decide

theorem actual_formation_trace : FormedSelection.Trace 34 (start 161 154) word formed :=
  runnable_trace actual_formation_feasible

theorem actual_formation_endpoint : formed=⟨16,17,.active,true,true,138,140⟩ ∧
    word.length=50 ∧ FormedSelection.tally FormedSelection.expenditure word=36 := by decide

theorem actual_assembly_and_material :
    ArchivePreparation.AssemblyRunnable ⟨formed,0,0⟩ assemblyWord ∧
    prepared.plant=⟨0,1,.active,true,true,122,140⟩ ∧ prepared.cells=12 ∧
    prepared.readers=4 ∧ ArchivePreparation.material prepared=34 := by decide

/- Project a prepared state, not an M34 formation trace, onto the M32 parent.
The separately assembled pair and its three operating units remain accounted. -/
def parentProjection (s : ArchivePreparation.Assembly) : ArchivePreparation.Assembly :=
  { s with plant := { s.plant with fuel := s.plant.fuel-3 }, readers := s.readers-1 }

theorem exact_parent_prepared_projection :
    parentProjection prepared=ActionPreparation.prepared 155 154 := by
  have ext : ∀ s t : ArchivePreparation.Assembly,
      s.plant=t.plant → s.cells=t.cells → s.readers=t.readers → s=t := by
    intro s t
    cases s; cases t; simp_all
  apply ext
  · simp only [parentProjection,actual_assembly_and_material.2.1,
      ActionPreparation.actual_material_partition.1]
  · exact actual_assembly_and_material.2.2.1.trans ActionPreparation.actual_material_partition.2.1.symm
  · change prepared.readers-1=(ActionPreparation.prepared 155 154).readers
    rw [actual_assembly_and_material.2.2.2.1,ActionPreparation.actual_material_partition.2.2.1]

theorem original_accounts_partition :
    ArchivePreparation.adapterFuel prepared=89+6+24+3 ∧
    prepared.plant.source=130+10 ∧ 161+154=53+(89+6+24+3+130+10) ∧
    161+154=53+78+54+15+72+3+10+30 := by decide

def withoutInspector := ArchivePreparation.assemblyRun ⟨formed,0,0⟩ ActionPreparation.assemblyWord

theorem omitted_assembly_retains_parts_and_payment :
    withoutInspector.plant.aFree=1 ∧ withoutInspector.plant.hFree=2 ∧
    withoutInspector.plant.fuel=123 ∧ withoutInspector.readers=3 ∧
    ArchivePreparation.material withoutInspector=34 := by decide

end InspectionPreparation

#print axioms InspectionPreparation.runnable_trace
#print axioms InspectionPreparation.actual_formation_feasible
#print axioms InspectionPreparation.actual_formation_trace
#print axioms InspectionPreparation.actual_formation_endpoint
#print axioms InspectionPreparation.actual_assembly_and_material
#print axioms InspectionPreparation.exact_parent_prepared_projection
#print axioms InspectionPreparation.original_accounts_partition
#print axioms InspectionPreparation.omitted_assembly_retains_parts_and_payment
