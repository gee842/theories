import ReasonPreparation

namespace ActionPreparation

set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

def start (fuel source : Nat) : FormedSelection.State := ⟨0,0,.empty,false,false,fuel,source⟩
def word : List FormedSelection.Event := List.replicate 16 .formH ++
  [.formA,.formA,.formA,.associateA,.repair] ++
  (List.replicate 13 [.capture,.localCopyA]).flatten ++ [.capture]

def Runnable (s : FormedSelection.State) : List FormedSelection.Event → Prop
  | [] => True
  | e::es => FormedSelection.Step 32 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es

instance runnableDecidable (s : FormedSelection.State) (es : List FormedSelection.Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es =>
      let _:=runnableDecidable (FormedSelection.advance s e) es
      inferInstanceAs (Decidable (FormedSelection.Step 32 s e (FormedSelection.advance s e) ∧ Runnable (FormedSelection.advance s e) es))

theorem runnable_trace {s : FormedSelection.State} {es : List FormedSelection.Event}
    (h : Runnable s es) : FormedSelection.Trace 32 s es (ArchivePreparation.run s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons h.1 (ih h.2)

def formed (fuel source : Nat) := ArchivePreparation.run (start fuel source) word
def assemblyWord : List ArchivePreparation.Kind := List.replicate 12 .cell ++ [.reader,.reader,.reader]
def prepared (fuel source : Nat) := ArchivePreparation.assemblyRun ⟨formed fuel source,0,0⟩ assemblyWord

def parentProjection (s : ArchivePreparation.Assembly) : ArchivePreparation.Assembly :=
  { s with plant := { s.plant with fuel := s.plant.fuel-30, source := s.plant.source-10 }, readers := s.readers-1 }

theorem actual_formation_feasible : Runnable (start 155 154) word := by decide

theorem actual_formation_trace : FormedSelection.Trace 32 (start 155 154) word (formed 155 154) :=
  runnable_trace actual_formation_feasible

theorem actual_formation_endpoint :
    formed 155 154=⟨15,16,.active,true,true,134,140⟩ ∧ word.length=48 ∧
    FormedSelection.tally FormedSelection.expenditure word=34 := by decide

theorem actual_assemblies_feasible :
    ArchivePreparation.AssemblyRunnable ⟨formed 155 154,0,0⟩ assemblyWord := by decide

theorem actual_material_partition :
    (prepared 155 154).plant=⟨0,1,.active,true,true,119,140⟩ ∧
    (prepared 155 154).cells=12 ∧ (prepared 155 154).readers=3 ∧
    ArchivePreparation.material (prepared 155 154)=32 := by decide

/- A state/resource partition, not erasure of a different-capacity formation trace.
The third pair and protected accounts remain in the extension ledger. -/
theorem exact_parent_prepared_projection :
    parentProjection (prepared 155 154)=ReasonPreparation.prepared 122 := by
  have ext : ∀ s t : ArchivePreparation.Assembly,
      s.plant=t.plant → s.cells=t.cells → s.readers=t.readers → s=t := by
    intro s t
    cases s; cases t; simp_all
  apply ext
  · simp only [parentProjection,actual_material_partition.1,ReasonPreparation.actual_material_partition.1]
  · exact actual_material_partition.2.1.trans ReasonPreparation.actual_material_partition.2.1.symm
  · change (prepared 155 154).readers-1=(ReasonPreparation.prepared 122).readers
    rw [actual_material_partition.2.2.1,ReasonPreparation.actual_material_partition.2.2.1]

theorem original_accounts_partition :
    ArchivePreparation.adapterFuel (prepared 155 154)=89+6+24 ∧
    (prepared 155 154).plant.source=130+10 ∧
    155+154=50+(89+6+24+130+10) := by decide

theorem action_control_preparations_feasible :
    Runnable (start 131 154) word ∧ Runnable (start 130 154) word ∧
    Runnable (start 155 153) word ∧
    ArchivePreparation.AssemblyRunnable ⟨formed 131 154,0,0⟩ assemblyWord ∧
    ArchivePreparation.AssemblyRunnable ⟨formed 130 154,0,0⟩ assemblyWord ∧
    ArchivePreparation.AssemblyRunnable ⟨formed 155 153,0,0⟩ assemblyWord := by decide

theorem exact_control_reserves :
    ArchivePreparation.adapterFuel (prepared 131 154)=89+6 ∧
    ArchivePreparation.adapterFuel (prepared 130 154)=89+5 ∧
    (prepared 155 153).plant.source=130+9 ∧ 9/10=0 ∧ 9%10=9 := by decide

theorem old_material_has_no_free_command_pair :
    ¬ ArchivePreparation.enabled (ReasonPreparation.prepared 122) := by decide

def withoutPort := ArchivePreparation.assemblyRun ⟨formed 155 154,0,0⟩ ReasonPreparation.assemblyWord

theorem omitted_assembly_retains_parts_and_payment :
    withoutPort.plant.aFree=1 ∧ withoutPort.plant.hFree=2 ∧
    withoutPort.plant.fuel=120 ∧ withoutPort.readers=2 ∧
    ArchivePreparation.material withoutPort=32 := by decide

theorem whole_history_accounts :
    131+154=50+78+54+15+48+10+30 ∧
    155+154=50+78+54+15+72+10+30 := by decide

end ActionPreparation

#print axioms ActionPreparation.runnable_trace
#print axioms ActionPreparation.actual_formation_feasible
#print axioms ActionPreparation.actual_formation_trace
#print axioms ActionPreparation.actual_formation_endpoint
#print axioms ActionPreparation.actual_assemblies_feasible
#print axioms ActionPreparation.actual_material_partition
#print axioms ActionPreparation.exact_parent_prepared_projection
#print axioms ActionPreparation.original_accounts_partition
#print axioms ActionPreparation.action_control_preparations_feasible
#print axioms ActionPreparation.exact_control_reserves
#print axioms ActionPreparation.old_material_has_no_free_command_pair
#print axioms ActionPreparation.omitted_assembly_retains_parts_and_payment
#print axioms ActionPreparation.whole_history_accounts
