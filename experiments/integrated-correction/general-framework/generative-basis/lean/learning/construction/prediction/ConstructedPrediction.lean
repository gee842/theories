import ConstructedUpdater
import PredictionAction

/-!
An actual typed-material entrance to the existing predictive action law. One
free A/H pair is retooled into explicitly retained register backing. Its finite
five-state memory, decoder and functional coupling are declared local recipes,
not consequences of the material count. Writes reuse that register; only later
updater formations consume more free pairs. No old support state is reset.
-/
namespace ConstructedPrediction

structure Running where
  core : PredictionAction.State
  aFree : Nat
  hFree : Nat
  resident : FormedSelection.Resident
  intact : Bool
  boundA : Nat
  boundH : Nat
  registerUnits : Nat
  precursor : Nat
deriving DecidableEq, Repr

/-- A register unit contains one A and one H, separate from the old bound stock. -/
def matter (r : Running) : Nat :=
  r.aFree + r.hFree + FormedSelection.occupied r.resident + r.boundA + r.boundH + 2*r.registerUnits

def totalMatter (r : Running) : Nat := matter r + r.precursor

def partCost : PredictionAction.Event → Nat
  | .formUpdater _ => 1
  | _ => 0

def partCostAlong : List PredictionAction.Event → Nat
  | [] => 0
  | a :: as => partCost a + partCostAlong as

def PartsReady (r : Running) (a : PredictionAction.Event) : Prop :=
  partCost a ≤ r.aFree ∧ partCost a ≤ r.hFree

def advance (p : PredictionAction.Parameters) (r : Running) (a : PredictionAction.Event) : Running :=
  { r with
    core := PredictionAction.advance p r.core a
    aFree := r.aFree - partCost a
    hFree := r.hFree - partCost a
    boundA := r.boundA + partCost a
    boundH := r.boundH + partCost a }

def Step (p : PredictionAction.Parameters) (r : Running) (a : PredictionAction.Event) (t : Running) : Prop :=
  0 < r.registerUnits ∧ PredictionAction.Enabled p r.core a ∧ PartsReady r a ∧ t = advance p r a

instance (r : Running) (a : PredictionAction.Event) : Decidable (PartsReady r a) := by
  unfold PartsReady; infer_instance
instance (p : PredictionAction.Parameters) (r t : Running) (a : PredictionAction.Event) : Decidable (Step p r a t) := by
  unfold Step; infer_instance

def process (p : PredictionAction.Parameters) : Generative.Process Running PredictionAction.Event := ⟨Step p⟩
def Trace (p : PredictionAction.Parameters) := Generative.Trace (process p)

theorem step_projects {p : PredictionAction.Parameters} {r t : Running} {a : PredictionAction.Event}
    (h : Step p r a t) : PredictionAction.Step p r.core a t.core := by
  rcases h with ⟨_, he, _, rfl⟩
  exact ⟨he, rfl⟩

theorem trace_projects {p : PredictionAction.Parameters} {r t : Running} {as : List PredictionAction.Event}
    (h : Trace p r as t) : PredictionAction.Trace p r.core as t.core := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons (step_projects hs) ih

theorem command_lifts_iff (p : PredictionAction.Parameters) (r : Running) (a : PredictionAction.Event) :
    (∃ t, Step p r a t) ↔ 0 < r.registerUnits ∧ PredictionAction.Enabled p r.core a ∧ PartsReady r a := by
  constructor
  · rintro ⟨t, hi, he, hm, _⟩; exact ⟨hi, he, hm⟩
  · rintro ⟨hi, he, hm⟩; exact ⟨advance p r a, hi, he, hm, rfl⟩

theorem step_part_ledgers {p : PredictionAction.Parameters} {r t : Running} {a : PredictionAction.Event}
    (h : Step p r a t) :
    t.aFree + partCost a = r.aFree ∧ t.hFree + partCost a = r.hFree ∧
    t.boundA = r.boundA + partCost a ∧ t.boundH = r.boundH + partCost a := by
  rcases h with ⟨_, _, hp, rfl⟩
  change r.aFree - partCost a + partCost a = r.aFree ∧
    r.hFree - partCost a + partCost a = r.hFree ∧
    r.boundA + partCost a = r.boundA + partCost a ∧
    r.boundH + partCost a = r.boundH + partCost a
  unfold PartsReady at hp
  exact ⟨by omega, by omega, rfl, rfl⟩

theorem trace_part_ledgers {p : PredictionAction.Parameters} {r t : Running}
    {as : List PredictionAction.Event} (h : Trace p r as t) :
    t.aFree + partCostAlong as = r.aFree ∧ t.hFree + partCostAlong as = r.hFree ∧
    t.boundA = r.boundA + partCostAlong as ∧ t.boundH = r.boundH + partCostAlong as := by
  induction h with
  | nil => exact ⟨rfl, rfl, rfl, rfl⟩
  | cons hs _ ih =>
    have hh := step_part_ledgers hs
    simp only [partCostAlong]
    refine ⟨?_, ?_, ?_, ?_⟩ <;> omega

theorem abstract_trace_lifts_with_parts {p : PredictionAction.Parameters}
    {s t : PredictionAction.State} {as : List PredictionAction.Event}
    (h : PredictionAction.Trace p s as t) (r : Running) (hr : r.core = s)
    (hi : 0 < r.registerUnits) (ha : partCostAlong as ≤ r.aFree) (hh : partCostAlong as ≤ r.hFree) :
    ∃ q, Trace p r as q ∧ q.core = t := by
  induction h generalizing r with
  | nil => exact ⟨r, .nil r, hr⟩
  | @cons s u t a as hs ht ih =>
    have hp : PartsReady r a := by
      unfold PartsReady
      simp only [partCostAlong] at ha hh
      exact ⟨by omega, by omega⟩
    have he : PredictionAction.Enabled p r.core a := by rw [hr]; exact hs.1
    have hstep : Step p r a (advance p r a) := ⟨hi, he, hp, rfl⟩
    have hproject : (advance p r a).core = u := by
      change PredictionAction.advance p r.core a = u
      rw [hr]; exact hs.2.symm
    have hl := step_part_ledgers hstep
    have ha' : partCostAlong as ≤ (advance p r a).aFree := by simp only [partCostAlong] at ha; omega
    have hh' : partCostAlong as ≤ (advance p r a).hFree := by simp only [partCostAlong] at hh; omega
    obtain ⟨q, hq, hqt⟩ := ih (advance p r a) hproject hi ha' hh'
    exact ⟨q, .cons hstep hq, hqt⟩

/-- On an installed register, only actual future module formations add component demand. -/
theorem material_trace_lift_iff (p : PredictionAction.Parameters) (r : Running)
    (hi : 0 < r.registerUnits) (as : List PredictionAction.Event) (s : PredictionAction.State) :
    (∃ q, Trace p r as q ∧ q.core = s) ↔
      PredictionAction.Trace p r.core as s ∧ partCostAlong as ≤ r.aFree ∧ partCostAlong as ≤ r.hFree := by
  constructor
  · rintro ⟨q, hq, rfl⟩
    have hl := trace_part_ledgers hq
    exact ⟨trace_projects hq, by omega, by omega⟩
  · rintro ⟨ht, ha, hh⟩
    exact abstract_trace_lifts_with_parts ht r rfl hi ha hh

theorem trace_preserves_backing {p : PredictionAction.Parameters} {r t : Running}
    {as : List PredictionAction.Event} (h : Trace p r as t) :
    t.resident = r.resident ∧ t.intact = r.intact ∧ t.precursor = r.precursor ∧ t.registerUnits = r.registerUnits := by
  induction h with
  | nil => exact ⟨rfl, rfl, rfl, rfl⟩
  | cons hs _ ih => rcases hs with ⟨_, _, _, rfl⟩; exact ih

theorem trace_preserves_matter {p : PredictionAction.Parameters} {r t : Running}
    {as : List PredictionAction.Event} (h : Trace p r as t) :
    matter t = matter r ∧ totalMatter t = totalMatter r := by
  have hp := trace_part_ledgers h
  have hs := trace_preserves_backing h
  simp only [matter, totalMatter, hs.1, hs.2.2.1, hs.2.2.2]
  exact ⟨by omega, by omega⟩

theorem finite_stock_bounds_updater_replacements {p : PredictionAction.Parameters} {r t : Running}
    {as : List PredictionAction.Event} (h : Trace p r as t) :
    partCostAlong as ≤ r.aFree ∧ partCostAlong as ≤ r.hFree := by
  have hl := trace_part_ledgers h
  exact ⟨by omega, by omega⟩

theorem trace_energy_ledger {p : PredictionAction.Parameters} {r t : Running}
    {as : List PredictionAction.Event} (hp : UpdaterFormation.Admissible p.base) (h : Trace p r as t) :
    PredictionAction.energy p t.core + PredictionAction.spentAlong p r.core as = PredictionAction.energy p r.core :=
  PredictionAction.trace_energy_ledger hp (trace_projects h)

theorem trace_score_bounded {p : PredictionAction.Parameters} {r t : Running}
    {as : List PredictionAction.Event} (h : Trace p r as t) (hq : r.core.score ≤ 4) : t.core.score ≤ 4 :=
  PredictionAction.trace_score_bounded (trace_projects h) hq

theorem updater_replacement_retains_memory_and_backing (p : PredictionAction.Parameters)
    (r : Running) (fast : Bool) :
    (advance p r (.formUpdater fast)).core.score = r.core.score ∧
    (advance p r (.formUpdater fast)).registerUnits = r.registerUnits := ⟨rfl, rfl⟩

def RetrofitEnabled (p : PredictionAction.Parameters) (r : ConstructedUpdater.Running) : Prop :=
  PredictionAction.RetrofitEnabled p r.core ∧ 1 ≤ r.aFree ∧ 1 ≤ r.hFree
instance (p : PredictionAction.Parameters) (r : ConstructedUpdater.Running) : Decidable (RetrofitEnabled p r) := by
  unfold RetrofitEnabled PredictionAction.RetrofitEnabled; infer_instance

/-- New five-state register begins neutral once, and all inherited leases, stores,
and last-action reference are exactly those of the old paid retrofit. -/
def retrofit (p : PredictionAction.Parameters) (r : ConstructedUpdater.Running) : Running :=
  ⟨PredictionAction.retrofit p r.core, r.aFree-1, r.hFree-1, r.resident, r.intact,
    r.boundA, r.boundH, 1, r.precursor⟩

theorem retrofit_energy_exact {p : PredictionAction.Parameters} {r : ConstructedUpdater.Running}
    (h : RetrofitEnabled p r) :
    PredictionAction.energy p (retrofit p r).core + p.retrofit = UpdaterFormation.energy p.base r.core :=
  PredictionAction.paid_retrofit_energy h.1

theorem retrofit_material_exact {p : PredictionAction.Parameters} {r : ConstructedUpdater.Running}
    (h : RetrofitEnabled p r) :
    matter (retrofit p r) = ConstructedUpdater.matter r ∧
    totalMatter (retrofit p r) = ConstructedUpdater.totalMatter r := by
  have ha := h.2.1
  have hh := h.2.2
  simp only [matter, totalMatter, retrofit, ConstructedUpdater.matter, ConstructedUpdater.totalMatter]
  exact ⟨by omega, by omega⟩

theorem retrofit_keeps_actual_memory_reference (p : PredictionAction.Parameters) (r : ConstructedUpdater.Running) :
    (retrofit p r).core.physical.core.selector = r.core.core.selector ∧
    (retrofit p r).core.physical.core.packets = r.core.core.packets ∧
    (retrofit p r).core.physical.core.lease = r.core.core.lease ∧
    (retrofit p r).core.physical.moduleLease = r.core.moduleLease ∧
    (retrofit p r).core.score = 2 ∧ (retrofit p r).registerUnits = 1 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

inductive Stage where
  | before (s : ConstructedUpdater.Stage)
  | prediction (r : Running)
deriving DecidableEq, Repr
inductive Event where
  | before (a : ConstructedUpdater.Event)
  | retrofit
  | predict (a : PredictionAction.Event)
deriving DecidableEq, Repr

def StagedStep (p : PredictionAction.Parameters) (M : Nat) (z : Bool) : Stage → Event → Stage → Prop
  | .before s, .before a, .before t => ConstructedUpdater.StagedStep p.base M z s a t
  | .before (.operation r), .retrofit, .prediction t => RetrofitEnabled p r ∧ t = retrofit p r
  | .prediction r, .predict a, .prediction t => Step p r a t
  | _, _, _ => False

def stagedProcess (p : PredictionAction.Parameters) (M : Nat) (z : Bool) : Generative.Process Stage Event :=
  ⟨StagedStep p M z⟩
def StagedTrace (p : PredictionAction.Parameters) (M : Nat) (z : Bool) := Generative.Trace (stagedProcess p M z)

theorem old_construction_trace_embeds {p : PredictionAction.Parameters} {M : Nat} {z : Bool}
    {s t : ConstructedUpdater.Stage} {as : List ConstructedUpdater.Event}
    (h : ConstructedUpdater.StagedTrace p.base M z s as t) :
    StagedTrace p M z (.before s) (as.map Event.before) (.before t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih => exact Generative.Trace.cons (m := Stage.before u) hs ih

theorem prediction_trace_embeds {p : PredictionAction.Parameters} {M : Nat} {z : Bool}
    {r t : Running} {as : List PredictionAction.Event} (h : Trace p r as t) :
    StagedTrace p M z (.prediction r) (as.map Event.predict) (.prediction t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih => exact Generative.Trace.cons (m := Stage.prediction u) hs ih

theorem compose_actual_state {p : PredictionAction.Parameters} {M : Nat} {z : Bool}
    {s : ConstructedUpdater.Stage} {u : ConstructedUpdater.Running} {t : Running}
    {as : List ConstructedUpdater.Event} {bs : List PredictionAction.Event}
    (hOld : ConstructedUpdater.StagedTrace p.base M z s as (.operation u))
    (hRetro : RetrofitEnabled p u) (hNew : Trace p (retrofit p u) bs t) :
    StagedTrace p M z (.before s)
      (as.map Event.before ++ .retrofit :: bs.map Event.predict) (.prediction t) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.before (.operation u), old_construction_trace_embeds hOld, ?_⟩
  apply Generative.Trace.cons (m := .prediction (retrofit p u))
  · exact ⟨hRetro, rfl⟩
  · exact prediction_trace_embeds hNew

theorem whole_history_energy_ledger {p : PredictionAction.Parameters} {M : Nat} {z : Bool}
    {s e : FormedSelection.State} {u : ConstructedUpdater.Running} {t : Running}
    {as : List FormedSelection.Event} {bs : List UpdaterFormation.Event} {cs : List PredictionAction.Event}
    (hp : UpdaterFormation.Admissible p.base) (hOld : FormedSelection.Trace M s as e)
    (hBridge : ConstructedUpdater.BridgeEnabled p.base M e)
    (hMachinery : ConstructedUpdater.Trace p.base (ConstructedUpdater.entrance p.base M e z) bs u)
    (hRetro : RetrofitEnabled p u) (hNew : Trace p (retrofit p u) cs t) :
    PredictionAction.energy p t.core + PredictionAction.spentAlong p (retrofit p u).core cs + p.retrofit +
      UpdaterFormation.spentAlong p.base (ConstructedUpdater.entrance p.base M e z).core bs +
      p.base.adapter + FormedSelection.tally FormedSelection.expenditure as = FormedSelection.energy s := by
  have h1 := ConstructedUpdater.joined_energy_ledger hp hOld hBridge hMachinery
  have h2 := retrofit_energy_exact hRetro
  have h3 := trace_energy_ledger hp hNew
  omega

theorem whole_history_material_ledger {p : PredictionAction.Parameters} {M : Nat} {z : Bool}
    {e : FormedSelection.State} {u : ConstructedUpdater.Running} {t : Running}
    {bs : List UpdaterFormation.Event} {cs : List PredictionAction.Event}
    (hBridge : ConstructedUpdater.BridgeEnabled p.base M e)
    (hMachinery : ConstructedUpdater.Trace p.base (ConstructedUpdater.entrance p.base M e z) bs u)
    (hRetro : RetrofitEnabled p u) (hNew : Trace p (retrofit p u) cs t) :
    totalMatter t = M ∧ t.core.physical.material = M := by
  have hm := ConstructedUpdater.joined_material_ledger hBridge hMachinery
  have hr := retrofit_material_exact hRetro
  have hn := trace_preserves_matter hNew
  have hc := PredictionAction.trace_material_preserved (trace_projects hNew)
  exact ⟨hn.2.trans (hr.2.trans hm.2.1), hc.trans hm.2.2⟩

/-- Material is an inert label in the inherited prediction law, not a free reset. -/
theorem core_material_relabel_trace {p : PredictionAction.Parameters}
    {s t : PredictionAction.State} {as : List PredictionAction.Event}
    (h : PredictionAction.Trace p s as t) (M : Nat) :
    PredictionAction.Trace p {s with physical := {s.physical with material := M}} as
      {t with physical := {t.physical with material := M}} := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih =>
    apply Generative.Trace.cons (m := {u with physical := {u.physical with material := M}})
    · rcases hs with ⟨he, rfl⟩
      constructor
      · cases a <;> exact he
      · cases a <;> rfl
    · exact ih

def initial : FormedSelection.State := ⟨0,0,.empty,false,false,33,121⟩
def prepared : FormedSelection.State := ⟨4,6,.active,true,true,20,120⟩
def formationEvents : List FormedSelection.Event :=
  [.formH,.formH,.formH,.formH,.formH,.formH,
   .formA,.formA,.formA,.formA,.formA,.associateA,.repair,.capture]

theorem actual_part_preparation : FormedSelection.Trace 11 initial formationEvents prepared := by
  apply FormedSelection.Trace.cons (u := ⟨0,1,.empty,false,false,32,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,2,.empty,false,false,31,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,3,.empty,false,false,30,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,4,.empty,false,false,29,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,5,.empty,false,false,28,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,6,.empty,false,false,27,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1,6,.empty,false,false,26,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨2,6,.empty,false,false,25,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨3,6,.empty,false,false,24,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨4,6,.empty,false,false,23,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨5,6,.empty,false,false,22,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨4,6,.active,false,false,21,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨4,6,.active,true,false,20,121⟩) (by decide)
  apply FormedSelection.Trace.cons (u := prepared) (by decide)
  exact .nil _

def machineEntrance : ConstructedUpdater.Running :=
  ConstructedUpdater.entrance PredictionAction.primary.base 11 prepared true

def machine : ConstructedUpdater.Running :=
  ⟨{ PredictionAction.formed with material := 11 },2,2,.active,true,2,4,0⟩

def ready : Running := retrofit PredictionAction.primary machine

def final : Running :=
  ⟨{ PredictionAction.finalState with physical := { PredictionAction.finalState.physical with material := 11 } },
    0,0,.active,true,3,5,1,0⟩

theorem actual_typed_adapter : ConstructedUpdater.BridgeEnabled PredictionAction.primary.base 11 prepared := by decide

theorem actual_typed_machinery :
    ConstructedUpdater.Trace PredictionAction.primary.base machineEntrance PredictionAction.formationOps machine := by
  apply Generative.Trace.cons (m := ⟨⟨⟨18,12,false,0,true⟩,false,2,false,0,11⟩,2,4,.active,true,2,2,0⟩)
    (by change ConstructedUpdater.Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := machine) (by change ConstructedUpdater.Step _ _ _ _; decide)
  exact .nil _

def precedingEvents : List ConstructedUpdater.Event :=
  formationEvents.map ConstructedUpdater.Event.form ++
    .handoff :: PredictionAction.formationOps.map ConstructedUpdater.Event.operate

theorem actual_formed_prefix :
    ConstructedUpdater.StagedTrace PredictionAction.primary.base 11 true
      (.formation initial) precedingEvents (.operation machine) :=
  ConstructedUpdater.actual_formation_bridge_continuation actual_part_preparation actual_typed_adapter actual_typed_machinery

theorem actual_typed_retrofit : RetrofitEnabled PredictionAction.primary machine := by decide

theorem inherited_predictive_entrance_exact :
    ready.core = { PredictionAction.beginning with physical := { PredictionAction.beginning.physical with material := 11 } } ∧
    ready.aFree = 1 ∧ ready.hFree = 1 ∧ ready.registerUnits = 1 ∧ totalMatter ready = 11 := by decide

/-- Evaluation helpers retain all intermediate physical and memory states. -/
def run (p : PredictionAction.Parameters) : Running → List PredictionAction.Event → Running
  | r, [] => r
  | r, a :: as => run p (advance p r a) as

def Runnable (p : PredictionAction.Parameters) : Running → List PredictionAction.Event → Prop
  | _, [] => True
  | r, a :: as => 0 < r.registerUnits ∧ PredictionAction.Enabled p r.core a ∧
      PartsReady r a ∧ Runnable p (advance p r a) as

def runnableDecidable (p : PredictionAction.Parameters) :
    (r : Running) → (as : List PredictionAction.Event) → Decidable (Runnable p r as)
  | _, [] => isTrue trivial
  | r, a :: as => by
    haveI : Decidable (Runnable p (advance p r a) as) := runnableDecidable p (advance p r a) as
    unfold Runnable
    infer_instance

instance (p : PredictionAction.Parameters) (r : Running) (as : List PredictionAction.Event) :
    Decidable (Runnable p r as) := runnableDecidable p r as

theorem runnable_trace {p : PredictionAction.Parameters} {r : Running}
    {as : List PredictionAction.Event} (h : Runnable p r as) : Trace p r as (run p r as) := by
  induction as generalizing r with
  | nil => exact .nil _
  | cons a as ih => exact .cons ⟨h.1,h.2.1,h.2.2.1,rfl⟩ (ih h.2.2.2)

set_option maxRecDepth 4096 in
theorem actual_acquired_corrected_action : Trace PredictionAction.primary ready PredictionAction.witnessEvents final := by
  have h : Runnable PredictionAction.primary ready PredictionAction.witnessEvents := by decide
  have hh : run PredictionAction.primary ready PredictionAction.witnessEvents = final := by decide
  rw [← hh]
  exact runnable_trace h

theorem full_formation_prediction_corrected_action :
    StagedTrace PredictionAction.primary 11 true (.before (.formation initial))
      (precedingEvents.map Event.before ++ .retrofit :: PredictionAction.witnessEvents.map Event.predict)
      (.prediction final) :=
  compose_actual_state actual_formed_prefix actual_typed_retrofit actual_acquired_corrected_action

theorem whole_witness_accounting :
    FormedSelection.Absent initial ∧ FormedSelection.energy initial = 154 ∧
    FormedSelection.tally FormedSelection.expenditure formationEvents = 13 ∧
    PredictionAction.primary.base.adapter = 1 ∧
    UpdaterFormation.spentAlong PredictionAction.primary.base machineEntrance.core PredictionAction.formationOps = 3 ∧
    PredictionAction.primary.retrofit = 3 ∧
    PredictionAction.spentAlong PredictionAction.primary ready.core PredictionAction.witnessEvents = 96 ∧
    PredictionAction.energy PredictionAction.primary final.core = 38 ∧
    final.core.physical.core.fuel = 18 ∧ final.core.physical.core.packets = 2 ∧
    partCostAlong PredictionAction.witnessEvents = 1 ∧
    final.core.score = 0 ∧ final.core.physical.core.selector = false ∧
    final.core.physical.core.regime = false ∧ totalMatter final = 11 := by
  unfold FormedSelection.Absent
  decide

/-- Identical acquired score survives a paid change of update mechanism. -/
def beforeFast : Running := run PredictionAction.primary ready
  (PredictionAction.cycles 6 ++ [.reverse] ++ PredictionAction.cycles 2)

theorem actual_replacement_retains_acquired_memory :
    Trace PredictionAction.primary ready
      (PredictionAction.cycles 6 ++ [.reverse] ++ PredictionAction.cycles 2) beforeFast ∧
    beforeFast.core.score = 2 ∧ beforeFast.core.physical.core.fuel = 22 ∧
    Step PredictionAction.primary beforeFast (.formUpdater true)
      (advance PredictionAction.primary beforeFast (.formUpdater true)) ∧
    (advance PredictionAction.primary beforeFast (.formUpdater true)).core.score = beforeFast.core.score ∧
    (advance PredictionAction.primary beforeFast (.formUpdater true)).aFree = 0 ∧
    (advance PredictionAction.primary beforeFast (.formUpdater true)).hFree = 0 := by
  refine ⟨runnable_trace (by decide), by decide, by decide, by decide, rfl, by decide, by decide⟩

/-- The actual corrective write changes the next command, not the already issued action. -/
def correctiveRecord : Running :=
  advance PredictionAction.primary
    (advance PredictionAction.primary
      (advance PredictionAction.primary beforeFast (.formUpdater true)) .rent) .work

theorem material_backed_write_changes_future_command :
    PredictionAction.command correctiveRecord.core = true ∧
    PredictionAction.command (advance PredictionAction.primary correctiveRecord .write).core = false ∧
    (advance PredictionAction.primary correctiveRecord .write).core.physical.core.selector =
      correctiveRecord.core.physical.core.selector ∧
    (advance PredictionAction.primary correctiveRecord .write).registerUnits = 1 := by decide

/-- This earlier actually reachable construction exhausts all free components;
its original physical parameters are retained rather than switched to PA.primary. -/
def legacyParameters : PredictionAction.Parameters :=
  { PredictionAction.primary with base := UpdaterFormation.primary }

theorem actual_prior_revision_cannot_supply_register :
    ConstructedUpdater.StagedTrace legacyParameters.base 13 false
      (.formation ConstructedUpdater.initial)
      (ConstructedUpdater.formationEvents.map ConstructedUpdater.Event.form ++
        .handoff :: UpdaterFormation.updaterWitness.map ConstructedUpdater.Event.operate)
      (.operation ConstructedUpdater.final) ∧
    PredictionAction.RetrofitEnabled legacyParameters ConstructedUpdater.final.core ∧
    ¬ RetrofitEnabled legacyParameters ConstructedUpdater.final := by
  exact ⟨ConstructedUpdater.full_formation_to_updater_revision, by unfold PredictionAction.RetrofitEnabled; decide, by decide⟩

/-- Configured fixture, not a claimed reachable handoff: its unavailable register
pair remains physically counted in bound material. The preceding theorem gives
a reached obstruction in the actual earlier construction. -/
def noRegister : Running := { ready with registerUnits := 0, boundA := ready.boundA+1, boundH := ready.boundH+1 }

theorem coarse_capacity_does_not_supply_register :
    totalMatter noRegister = 11 ∧
    PredictionAction.Enabled PredictionAction.primary noRegister.core .rent ∧
    ¬ ∃ t, Step PredictionAction.primary noRegister .rent t := by
  refine ⟨by decide, by decide, ?_⟩
  rw [command_lifts_iff]
  decide

end ConstructedPrediction

#print axioms ConstructedPrediction.step_projects
#print axioms ConstructedPrediction.trace_projects
#print axioms ConstructedPrediction.command_lifts_iff
#print axioms ConstructedPrediction.step_part_ledgers
#print axioms ConstructedPrediction.trace_part_ledgers
#print axioms ConstructedPrediction.abstract_trace_lifts_with_parts
#print axioms ConstructedPrediction.material_trace_lift_iff
#print axioms ConstructedPrediction.trace_preserves_backing
#print axioms ConstructedPrediction.trace_preserves_matter
#print axioms ConstructedPrediction.finite_stock_bounds_updater_replacements
#print axioms ConstructedPrediction.trace_energy_ledger
#print axioms ConstructedPrediction.trace_score_bounded
#print axioms ConstructedPrediction.updater_replacement_retains_memory_and_backing
#print axioms ConstructedPrediction.retrofit_energy_exact
#print axioms ConstructedPrediction.retrofit_material_exact
#print axioms ConstructedPrediction.retrofit_keeps_actual_memory_reference
#print axioms ConstructedPrediction.old_construction_trace_embeds
#print axioms ConstructedPrediction.prediction_trace_embeds
#print axioms ConstructedPrediction.compose_actual_state
#print axioms ConstructedPrediction.whole_history_energy_ledger
#print axioms ConstructedPrediction.whole_history_material_ledger
#print axioms ConstructedPrediction.core_material_relabel_trace
#print axioms ConstructedPrediction.actual_part_preparation
#print axioms ConstructedPrediction.actual_typed_adapter
#print axioms ConstructedPrediction.actual_typed_machinery
#print axioms ConstructedPrediction.actual_formed_prefix
#print axioms ConstructedPrediction.actual_typed_retrofit
#print axioms ConstructedPrediction.inherited_predictive_entrance_exact
#print axioms ConstructedPrediction.runnable_trace
#print axioms ConstructedPrediction.actual_acquired_corrected_action
#print axioms ConstructedPrediction.full_formation_prediction_corrected_action
#print axioms ConstructedPrediction.whole_witness_accounting
#print axioms ConstructedPrediction.actual_replacement_retains_acquired_memory
#print axioms ConstructedPrediction.material_backed_write_changes_future_command
#print axioms ConstructedPrediction.actual_prior_revision_cannot_supply_register
#print axioms ConstructedPrediction.coarse_capacity_does_not_supply_register
