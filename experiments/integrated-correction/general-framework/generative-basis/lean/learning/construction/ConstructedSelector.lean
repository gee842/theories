import FormedSelection
import SelectorRevision

/-!
A staged material refinement of the existing selector law. Formation uses the
existing FormedSelection relation. The bookkeeping handoff denominates the
remaining unit source into packets, retaining the remainder. Each operational
assembly consumes two actual free parts of the chosen orientation into retained
incorporated/spent matter. The assembly recipes and their functional wiring are
supplied local laws. The pre-handoff reaction repertoire is suspended afterward.
-/

namespace ConstructedSelector


structure Running where
  plant : SelectorRevision.State
  aFree : Nat
  hFree : Nat
  resident : FormedSelection.Resident
  intact : Bool
  localFuel : Bool
  sourceRemainder : Nat
  boundA : Nat
  boundH : Nat
deriving DecidableEq, Repr

/-- Bound counters include both current and spent modules; no matter disappears
when a lease expires or a different mapping is assembled. -/
def matter (r : Running) : Nat :=
  r.aFree + r.hFree + FormedSelection.occupied r.resident + r.boundA + r.boundH

def energy (p : SelectorRevision.Parameters) (r : Running) : Nat :=
  SelectorRevision.energy p r.plant + r.sourceRemainder + FormedSelection.bit r.localFuel

def PartsReady (r : Running) : SelectorRevision.Event → Prop
  | .assemble false => 2 ≤ r.aFree
  | .assemble true => 2 ≤ r.hFree
  | _ => True

def advance (p : SelectorRevision.Parameters) (r : Running) (a : SelectorRevision.Event) : Running :=
  match a with
  | .assemble false => { r with plant := SelectorRevision.advance p r.plant a, aFree := r.aFree - 2, boundA := r.boundA + 2 }
  | .assemble true => { r with plant := SelectorRevision.advance p r.plant a, hFree := r.hFree - 2, boundH := r.boundH + 2 }
  | _ => { r with plant := SelectorRevision.advance p r.plant a }

def Step (p : SelectorRevision.Parameters) (r : Running) (a : SelectorRevision.Event) (t : Running) : Prop :=
  SelectorRevision.Enabled p r.plant a ∧ PartsReady r a ∧ t = advance p r a

instance (r : Running) (a : SelectorRevision.Event) : Decidable (PartsReady r a) := by
  cases a with
  | assemble b => cases b <;> unfold PartsReady <;> infer_instance
  | trial b => unfold PartsReady; infer_instance
  | reverse => unfold PartsReady; infer_instance
  | expire => unfold PartsReady; infer_instance

instance (p : SelectorRevision.Parameters) (r t : Running) (a : SelectorRevision.Event) :
    Decidable (Step p r a t) := by
  unfold Step
  infer_instance

def process (p : SelectorRevision.Parameters) : Generative.Process Running SelectorRevision.Event := ⟨Step p⟩
def Trace (p : SelectorRevision.Parameters) := Generative.Trace (process p)

def pack (s : FormedSelection.State) (regime : Bool) (packets remainder : Nat) : Running :=
  ⟨⟨s.fuel, packets, false, 0, regime⟩,
    s.aFree, s.hFree, s.resident, s.intact, s.localFuel, remainder, 0, 0⟩

def Packing (p : SelectorRevision.Parameters) (s : FormedSelection.State) (packets remainder : Nat) : Prop :=
  s.source = packets * p.packet + remainder ∧ remainder < p.packet

instance (p : SelectorRevision.Parameters) (s : FormedSelection.State) (packets remainder : Nat) :
    Decidable (Packing p s packets remainder) := by
  unfold Packing
  infer_instance

theorem advance_projects (p : SelectorRevision.Parameters) (r : Running) (a : SelectorRevision.Event) :
    (advance p r a).plant = SelectorRevision.advance p r.plant a := by
  cases a with
  | assemble b => cases b <;> rfl
  | trial b => rfl
  | reverse => rfl
  | expire => rfl

theorem step_projects {p : SelectorRevision.Parameters} {r t : Running} {a : SelectorRevision.Event}
    (h : Step p r a t) : SelectorRevision.Step p r.plant a t.plant := by
  rcases h with ⟨he, _, rfl⟩
  exact ⟨he, advance_projects p r a⟩

theorem trace_projects {p : SelectorRevision.Parameters} {r t : Running} {as : List SelectorRevision.Event}
    (h : Trace p r as t) : SelectorRevision.Trace p r.plant as t.plant := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons (step_projects hs) ih

/-- A permitted selector command lifts precisely when its required parts exist. -/
theorem command_lifts_iff (p : SelectorRevision.Parameters) (r : Running) (a : SelectorRevision.Event) :
    (∃ t, Step p r a t) ↔ SelectorRevision.Enabled p r.plant a ∧ PartsReady r a := by
  constructor
  · rintro ⟨t, he, hp, _⟩
    exact ⟨he, hp⟩
  · rintro ⟨he, hp⟩
    exact ⟨advance p r a, he, hp, rfl⟩

theorem commands_do_not_read_regime (p : SelectorRevision.Parameters) (r : Running)
    (z : Bool) (a : SelectorRevision.Event) :
    (SelectorRevision.Enabled p { r.plant with regime := z } a ∧ PartsReady r a) ↔
      (SelectorRevision.Enabled p r.plant a ∧ PartsReady r a) := by
  rw [SelectorRevision.commands_do_not_read_regime]

theorem assembly_recipe_ignores_regime (p : SelectorRevision.Parameters) (r : Running)
    (z m : Bool) :
    (advance p { r with plant := { r.plant with regime := z } } (.assemble m)).plant.selector = m ∧
    (advance p { r with plant := { r.plant with regime := z } } (.assemble m)).aFree =
      (advance p r (.assemble m)).aFree ∧
    (advance p { r with plant := { r.plant with regime := z } } (.assemble m)).hFree =
      (advance p r (.assemble m)).hFree := by
  cases m <;> exact ⟨rfl, rfl, rfl⟩

theorem step_preserves_matter {p : SelectorRevision.Parameters} {r t : Running} {a : SelectorRevision.Event}
    (h : Step p r a t) : matter t = matter r := by
  rcases h with ⟨_, hp, rfl⟩
  cases a with
  | assemble b => cases b <;> simp_all [advance, PartsReady, matter] <;> omega
  | trial b => rfl
  | reverse => rfl
  | expire => rfl

theorem trace_preserves_matter {p : SelectorRevision.Parameters} {r t : Running} {as : List SelectorRevision.Event}
    (h : Trace p r as t) : matter t = matter r := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact ih.trans (step_preserves_matter hs)

theorem step_preserves_side_stores {p : SelectorRevision.Parameters} {r t : Running} {a : SelectorRevision.Event}
    (h : Step p r a t) :
    t.sourceRemainder = r.sourceRemainder ∧ t.localFuel = r.localFuel := by
  rcases h with ⟨_, _, rfl⟩
  cases a with
  | assemble b => cases b <;> exact ⟨rfl, rfl⟩
  | trial b => exact ⟨rfl, rfl⟩
  | reverse => exact ⟨rfl, rfl⟩
  | expire => exact ⟨rfl, rfl⟩

theorem trace_preserves_side_stores {p : SelectorRevision.Parameters} {r t : Running} {as : List SelectorRevision.Event}
    (h : Trace p r as t) :
    t.sourceRemainder = r.sourceRemainder ∧ t.localFuel = r.localFuel := by
  induction h with
  | nil => exact ⟨rfl, rfl⟩
  | cons hs _ ih =>
    have hh := step_preserves_side_stores hs
    exact ⟨ih.1.trans hh.1, ih.2.trans hh.2⟩

theorem trace_energy_ledger {p : SelectorRevision.Parameters} {r t : Running} {as : List SelectorRevision.Event}
    (hp : SelectorRevision.Admissible p) (h : Trace p r as t) :
    energy p t + SelectorRevision.spentAlong p r.plant as = energy p r := by
  have he := SelectorRevision.trace_energy_ledger hp (trace_projects h)
  have hs := trace_preserves_side_stores h
  simp only [energy, hs.1, hs.2]
  omega

theorem packing_preserves_energy {p : SelectorRevision.Parameters} {s : FormedSelection.State}
    {packets remainder : Nat} (regime : Bool) (h : Packing p s packets remainder) :
    energy p (pack s regime packets remainder) = FormedSelection.energy s := by
  have hs := h.1
  simp only [energy, pack, SelectorRevision.energy, FormedSelection.energy]
  omega

theorem packing_preserves_matter (s : FormedSelection.State) (regime : Bool) (packets remainder : Nat) :
    matter (pack s regime packets remainder) = FormedSelection.population s := by
  simp [matter, pack, FormedSelection.population]

theorem packing_retains_local_conditions (s : FormedSelection.State) (regime : Bool)
    (packets remainder : Nat) :
    (pack s regime packets remainder).plant.fuel = s.fuel ∧
    (pack s regime packets remainder).plant.regime = regime ∧
    (pack s regime packets remainder).localFuel = s.localFuel ∧
    (pack s regime packets remainder).resident = s.resident ∧
    (pack s regime packets remainder).intact = s.intact := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩

/-- A changed response mapping consumes actual parts and actual common fuel. -/
theorem changed_mapping_consumes_parts {p : SelectorRevision.Parameters} {r t : Running} {a : SelectorRevision.Event}
    (h : Step p r a t) (hc : t.plant.selector ≠ r.plant.selector) :
    ∃ m, a = .assemble m ∧ t.plant.fuel + p.assembly = r.plant.fuel ∧
      t.aFree + t.hFree + 2 = r.aFree + r.hFree ∧
      t.boundA + t.boundH = r.boundA + r.boundH + 2 := by
  obtain ⟨m, ha, _, _, hf⟩ := SelectorRevision.changed_selector_requires_paid_assembly (step_projects h) hc
  subst a
  rcases h with ⟨_, hp, ht⟩
  subst t
  refine ⟨m, rfl, hf, ?_, ?_⟩
  all_goals cases m <;> simp_all [advance, PartsReady] <;> omega

inductive Stage where
  | formation (body : FormedSelection.State) (regime : Bool)
  | operation (running : Running)
deriving DecidableEq, Repr

inductive Event where
  | form (event : FormedSelection.Event)
  | handoff (packets remainder : Nat)
  | operate (event : SelectorRevision.Event)
deriving DecidableEq, Repr

def StagedStep (p : SelectorRevision.Parameters) (material : Nat) : Stage → Event → Stage → Prop
  | .formation s z, .form a, .formation t w => FormedSelection.Step material s a t ∧ w = z
  | .formation s z, .handoff packets remainder, .operation t =>
      s.intact = true ∧ Packing p s packets remainder ∧ t = pack s z packets remainder
  | .operation r, .operate a, .operation t => Step p r a t
  | _, _, _ => False

def stagedProcess (p : SelectorRevision.Parameters) (material : Nat) : Generative.Process Stage Event :=
  ⟨StagedStep p material⟩
def StagedTrace (p : SelectorRevision.Parameters) (material : Nat) :=
  Generative.Trace (stagedProcess p material)

theorem formation_trace_lifts {p : SelectorRevision.Parameters} {material : Nat} {s t : FormedSelection.State}
    {xs : List FormedSelection.Event} (z : Bool) (h : FormedSelection.Trace material s xs t) :
    StagedTrace p material (.formation s z) (xs.map Event.form) (.formation t z) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih =>
    apply Generative.Trace.cons (m := Stage.formation u z)
    · exact ⟨hs, rfl⟩
    · exact ih

theorem operational_trace_lifts {p : SelectorRevision.Parameters} {material : Nat} {r t : Running}
    {ys : List SelectorRevision.Event} (h : Trace p r ys t) :
    StagedTrace p material (.operation r) (ys.map Event.operate) (.operation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih =>
    apply Generative.Trace.cons (m := Stage.operation u)
    · exact hs
    · exact ih

/-- This joins the actual boundary state; resources are never reset. -/
theorem formation_assembly_composition {p : SelectorRevision.Parameters} {material : Nat}
    {s u : FormedSelection.State} {z : Bool} {packets remainder : Nat} {t : Running}
    {xs : List FormedSelection.Event} {ys : List SelectorRevision.Event}
    (hf : FormedSelection.Trace material s xs u) (hi : u.intact = true)
    (hp : Packing p u packets remainder)
    (ho : Trace p (pack u z packets remainder) ys t) :
    StagedTrace p material (.formation s z)
      (xs.map Event.form ++ .handoff packets remainder :: ys.map Event.operate)
      (.operation t) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.formation u z, formation_trace_lifts z hf, ?_⟩
  apply Generative.Trace.cons (m := Stage.operation (pack u z packets remainder))
  · exact ⟨hi, hp, rfl⟩
  · exact operational_trace_lifts ho

theorem composed_energy_ledger {p : SelectorRevision.Parameters} {material : Nat}
    {s u : FormedSelection.State} {z : Bool} {packets remainder : Nat} {t : Running}
    {xs : List FormedSelection.Event} {ys : List SelectorRevision.Event}
    (ha : SelectorRevision.Admissible p) (hf : FormedSelection.Trace material s xs u)
    (hp : Packing p u packets remainder)
    (ho : Trace p (pack u z packets remainder) ys t) :
    energy p t + FormedSelection.tally FormedSelection.expenditure xs +
      SelectorRevision.spentAlong p (pack u z packets remainder).plant ys = FormedSelection.energy s := by
  have hfuel := FormedSelection.trace_energy_ledger hf
  have hop := trace_energy_ledger ha ho
  have hpack := packing_preserves_energy z hp
  omega

theorem composed_material_ledger {p : SelectorRevision.Parameters} {material : Nat}
    {s u : FormedSelection.State} {z : Bool} {packets remainder : Nat} {t : Running}
    {xs : List FormedSelection.Event} {ys : List SelectorRevision.Event}
    (hv : FormedSelection.Valid material s) (hf : FormedSelection.Trace material s xs u)
    (ho : Trace p (pack u z packets remainder) ys t) :
    matter t + FormedSelection.precursor material u = material := by
  have hm := trace_preserves_matter ho
  have hp := packing_preserves_matter u z packets remainder
  have hl := FormedSelection.material_ledger (FormedSelection.trace_valid hv hf)
  have ht := FormedSelection.population_type_sum u
  omega

/-- Actual old-law capture and local copying produce assembly parts. -/
def initial : FormedSelection.State := ⟨0, 0, .empty, false, false, 12, 18⟩
def formed : FormedSelection.State := ⟨2, 2, .active, true, false, 7, 16⟩
def formationEvents : List FormedSelection.Event :=
  [.formH, .formH, .formA, .associateA, .repair,
   .capture, .localCopyA, .capture, .localCopyA]

theorem paid_formation_of_parts : FormedSelection.Trace 5 initial formationEvents formed := by
  apply FormedSelection.Trace.cons (u := ⟨0, 1, .empty, false, false, 11, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .empty, false, false, 10, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 2, .empty, false, false, 9, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .active, false, false, 8, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .active, true, false, 7, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .active, true, true, 7, 17⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 2, .active, true, false, 7, 17⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 2, .active, true, true, 7, 16⟩) (by decide)
  apply FormedSelection.Trace.cons (u := formed) (by decide)
  exact .nil _

def ready : Running := pack formed false 4 0
def final : Running := ⟨SelectorRevision.exampleFinal, 0, 0, .active, true, false, 0, 2, 2⟩

theorem handoff_is_actual_old_selector_initial :
    Packing SelectorRevision.exampleParameters formed 4 0 ∧ ready.plant = SelectorRevision.exampleInitial := by
  decide

theorem paid_material_selector_revision : Trace SelectorRevision.exampleParameters ready SelectorRevision.exampleEvents final := by
  apply Generative.Trace.cons (m := ⟨⟨6,4,false,2,false⟩,0,2,.active,true,false,0,2,0⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨7,3,false,2,false⟩,0,2,.active,true,false,0,2,0⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨7,3,false,2,true⟩,0,2,.active,true,false,0,2,0⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨5,2,false,1,true⟩,0,2,.active,true,false,0,2,0⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨3,1,false,0,true⟩,0,2,.active,true,false,0,2,0⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨2,1,true,2,true⟩,0,0,.active,true,false,0,2,2⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := final) (by change Step _ _ _ _; decide)
  exact .nil _

theorem complete_formation_to_revision :
    StagedTrace SelectorRevision.exampleParameters 5 (.formation initial false)
      (formationEvents.map Event.form ++ .handoff 4 0 :: SelectorRevision.exampleEvents.map Event.operate)
      (.operation final) :=
  formation_assembly_composition paid_formation_of_parts (by decide)
    handoff_is_actual_old_selector_initial.1 paid_material_selector_revision

theorem full_witness_accounting :
    FormedSelection.Absent initial ∧ FormedSelection.energy initial = 30 ∧ FormedSelection.tally FormedSelection.expenditure formationEvents = 7 ∧
    energy SelectorRevision.exampleParameters ready = 23 ∧
    SelectorRevision.spentAlong SelectorRevision.exampleParameters ready.plant SelectorRevision.exampleEvents = 20 ∧
    energy SelectorRevision.exampleParameters final = 3 ∧ matter final = 5 ∧
    final.boundA = 2 ∧ final.boundH = 2 ∧
    SelectorRevision.response ready.plant false ≠ SelectorRevision.response final.plant false := by
  unfold FormedSelection.Absent
  decide

/-- Both mapping recipes are available from the same actual stock and regime. -/
theorem two_assembled_mappings :
    Step SelectorRevision.exampleParameters ready (.assemble false) (advance SelectorRevision.exampleParameters ready (.assemble false)) ∧
    Step SelectorRevision.exampleParameters ready (.assemble true) (advance SelectorRevision.exampleParameters ready (.assemble true)) ∧
    SelectorRevision.response (advance SelectorRevision.exampleParameters ready (.assemble false)).plant false ≠
      SelectorRevision.response (advance SelectorRevision.exampleParameters ready (.assemble true)).plant false := by
  decide

def noParts : Running := ⟨⟨100,1,false,0,true⟩,0,0,.active,true,false,0,2,2⟩

theorem fuel_does_not_substitute_for_parts :
    SelectorRevision.Enabled SelectorRevision.exampleParameters noParts.plant (.assemble true) ∧
    ¬ ∃ t, Step SelectorRevision.exampleParameters noParts (.assemble true) t := by
  constructor
  · decide
  · rw [command_lifts_iff]
    decide

theorem exhausted_old_witness_cannot_assemble (z m : Bool) :
    ¬ ∃ t, Step SelectorRevision.exampleParameters (pack FormedSelection.copied z 0 0) (.assemble m) t := by
  rw [command_lifts_iff]
  cases z <;> cases m <;> decide

/-- Two free parts are consumed on each assembly of that orientation. -/
def partCost (orientation : Bool) : SelectorRevision.Event → Nat
  | .assemble m => if m = orientation then 2 else 0
  | _ => 0

def partCostAlong (orientation : Bool) : List SelectorRevision.Event → Nat
  | [] => 0
  | a :: as => partCost orientation a + partCostAlong orientation as

theorem step_part_ledgers {p : SelectorRevision.Parameters} {r t : Running}
    {a : SelectorRevision.Event} (h : Step p r a t) :
    t.aFree + partCost false a = r.aFree ∧
    t.hFree + partCost true a = r.hFree ∧
    t.boundA = r.boundA + partCost false a ∧
    t.boundH = r.boundH + partCost true a := by
  rcases h with ⟨_, hp, rfl⟩
  cases a with
  | assemble m => cases m <;> simp_all [advance, PartsReady, partCost] <;> omega
  | trial b => exact ⟨rfl, rfl, rfl, rfl⟩
  | reverse => exact ⟨rfl, rfl, rfl, rfl⟩
  | expire => exact ⟨rfl, rfl, rfl, rfl⟩

theorem trace_part_ledgers {p : SelectorRevision.Parameters} {r t : Running}
    {as : List SelectorRevision.Event} (h : Trace p r as t) :
    t.aFree + partCostAlong false as = r.aFree ∧
    t.hFree + partCostAlong true as = r.hFree ∧
    t.boundA = r.boundA + partCostAlong false as ∧
    t.boundH = r.boundH + partCostAlong true as := by
  induction h with
  | nil => exact ⟨rfl, rfl, rfl, rfl⟩
  | cons hs _ ih =>
    have hh := step_part_ledgers hs
    simp only [partCostAlong]
    refine ⟨?_, ?_, ?_, ?_⟩ <;> omega

theorem abstract_trace_lifts_with_parts {p : SelectorRevision.Parameters}
    {s t : SelectorRevision.State} {as : List SelectorRevision.Event}
    (h : SelectorRevision.Trace p s as t)
    (r : Running) (hr : r.plant = s)
    (ha : partCostAlong false as ≤ r.aFree)
    (hh : partCostAlong true as ≤ r.hFree) :
    ∃ q, Trace p r as q ∧ q.plant = t := by
  induction h generalizing r with
  | nil => exact ⟨r, .nil r, hr⟩
  | @cons s u t a as hs ht ih =>
    have hp : PartsReady r a := by
      cases a with
      | assemble m => cases m <;> simp_all [partCostAlong, partCost, PartsReady] <;> omega
      | trial b => trivial
      | reverse => trivial
      | expire => trivial
    have he : SelectorRevision.Enabled p r.plant a := by rw [hr]; exact hs.1
    have hstep : Step p r a (advance p r a) := ⟨he, hp, rfl⟩
    have hproject : (advance p r a).plant = u := by
      rw [advance_projects, hr]
      exact hs.2.symm
    have hledger := step_part_ledgers hstep
    have ha' : partCostAlong false as ≤ (advance p r a).aFree := by
      simp only [partCostAlong] at ha
      omega
    have hh' : partCostAlong true as ≤ (advance p r a).hFree := by
      simp only [partCostAlong] at hh
      omega
    obtain ⟨q, hq, hqt⟩ := ih (advance p r a) hproject ha' hh'
    exact ⟨q, .cons hstep hq, hqt⟩

/-- The old selector trace is realizable with actual parts exactly when its
cumulative demands for each orientation fit the inherited inventories. -/
theorem material_trace_lift_iff (p : SelectorRevision.Parameters) (r : Running)
    (as : List SelectorRevision.Event) (s : SelectorRevision.State) :
    (∃ q, Trace p r as q ∧ q.plant = s) ↔
      SelectorRevision.Trace p r.plant as s ∧
      partCostAlong false as ≤ r.aFree ∧ partCostAlong true as ≤ r.hFree := by
  constructor
  · rintro ⟨q, hq, rfl⟩
    have hl := trace_part_ledgers hq
    exact ⟨trace_projects hq, by omega, by omega⟩
  · rintro ⟨ht, ha, hh⟩
    exact abstract_trace_lifts_with_parts ht r rfl ha hh

theorem no_trial_before_initial_assembly (p : SelectorRevision.Parameters)
    (s : FormedSelection.State) (z b : Bool) (packets remainder : Nat) :
    ¬ ∃ t, Step p (pack s z packets remainder) (.trial b) t := by
  rw [command_lifts_iff]
  simp [SelectorRevision.Enabled, pack]

def HardwarePresent (r : Running) : Prop :=
  0 < r.plant.lease → 2 ≤ r.boundA + r.boundH

theorem step_preserves_hardware {p : SelectorRevision.Parameters} {r t : Running}
    {a : SelectorRevision.Event} (hi : HardwarePresent r) (h : Step p r a t) :
    HardwarePresent t := by
  rcases h with ⟨he, hp, rfl⟩
  cases a with
  | assemble m => cases m <;> simp [HardwarePresent, advance] <;> omega
  | trial b =>
    have hb : 2 ≤ r.boundA + r.boundH := hi he.1
    simp only [HardwarePresent, advance]
    intro _
    exact hb
  | reverse => exact hi
  | expire => exact hi

theorem trace_preserves_hardware {p : SelectorRevision.Parameters} {r t : Running}
    {as : List SelectorRevision.Event} (hi : HardwarePresent r) (h : Trace p r as t) :
    HardwarePresent t := by
  induction h with
  | nil => exact hi
  | cons hs _ ih => exact ih (step_preserves_hardware hi hs)

theorem active_reachable_selector_has_consumed_parts {p : SelectorRevision.Parameters}
    {s : FormedSelection.State} {z : Bool} {packets remainder : Nat} {t : Running}
    {as : List SelectorRevision.Event}
    (h : Trace p (pack s z packets remainder) as t) (ha : 0 < t.plant.lease) :
    2 ≤ t.boundA + t.boundH := by
  have hi : HardwarePresent (pack s z packets remainder) := by
    simp [HardwarePresent, pack]
  exact trace_preserves_hardware hi h ha

/-- Part availability cannot pay the energetic assembly obligation. -/
def noFuel : Running := { ready with plant := { ready.plant with fuel := 0 } }

theorem parts_do_not_substitute_for_fuel :
    PartsReady noFuel (.assemble false) ∧
    ¬ ∃ t, Step SelectorRevision.exampleParameters noFuel (.assemble false) t := by
  constructor
  · decide
  · rw [command_lifts_iff]
    decide

/-- After consumption, expiration of the lease does not release spent parts. -/
def afterFailedModule : Running :=
  ⟨⟨100,1,false,0,true⟩,0,2,.active,true,false,0,2,0⟩

theorem old_mapping_cannot_be_reassembled_from_spent_parts :
    SelectorRevision.Enabled SelectorRevision.exampleParameters afterFailedModule.plant (.assemble false) ∧
    ¬ (∃ t, Step SelectorRevision.exampleParameters afterFailedModule (.assemble false) t) ∧
    (∃ t, Step SelectorRevision.exampleParameters afterFailedModule (.assemble true) t) := by
  constructor
  · decide
  · constructor
    · rw [command_lifts_iff]; decide
    · exact ⟨advance SelectorRevision.exampleParameters afterFailedModule (.assemble true), by decide⟩

/-- The same constructed alternatives also allow a costly wrong-first path. -/
def wrongFirstEvents : List SelectorRevision.Event :=
  [.assemble true, .trial false, .trial true, .assemble false]

def wrongFirstFinal : Running :=
  ⟨⟨1,2,false,2,false⟩,0,0,.active,true,false,0,2,2⟩

theorem wrong_first_construction_history :
    Trace SelectorRevision.exampleParameters ready wrongFirstEvents wrongFirstFinal := by
  apply Generative.Trace.cons (m := ⟨⟨6,4,true,2,false⟩,2,0,.active,true,false,0,0,2⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨4,3,true,1,false⟩,2,0,.active,true,false,0,0,2⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨⟨2,2,true,0,false⟩,2,0,.active,true,false,0,0,2⟩)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := wrongFirstFinal) (by change Step _ _ _ _; decide)
  exact .nil _

theorem wrong_first_strands_available_source (b : Bool) :
    wrongFirstFinal.plant.packets = 2 ∧
    wrongFirstFinal.plant.selector = wrongFirstFinal.plant.regime ∧
    ¬ ∃ t, Step SelectorRevision.exampleParameters wrongFirstFinal (.trial b) t := by
  refine ⟨rfl, rfl, ?_⟩
  rw [command_lifts_iff]
  cases b <;> decide

end ConstructedSelector

#print axioms ConstructedSelector.advance_projects
#print axioms ConstructedSelector.step_projects
#print axioms ConstructedSelector.trace_projects
#print axioms ConstructedSelector.command_lifts_iff
#print axioms ConstructedSelector.commands_do_not_read_regime
#print axioms ConstructedSelector.assembly_recipe_ignores_regime
#print axioms ConstructedSelector.step_preserves_matter
#print axioms ConstructedSelector.trace_preserves_matter
#print axioms ConstructedSelector.step_preserves_side_stores
#print axioms ConstructedSelector.trace_preserves_side_stores
#print axioms ConstructedSelector.trace_energy_ledger
#print axioms ConstructedSelector.packing_preserves_energy
#print axioms ConstructedSelector.packing_preserves_matter
#print axioms ConstructedSelector.packing_retains_local_conditions
#print axioms ConstructedSelector.changed_mapping_consumes_parts
#print axioms ConstructedSelector.formation_trace_lifts
#print axioms ConstructedSelector.operational_trace_lifts
#print axioms ConstructedSelector.formation_assembly_composition
#print axioms ConstructedSelector.composed_energy_ledger
#print axioms ConstructedSelector.composed_material_ledger
#print axioms ConstructedSelector.paid_formation_of_parts
#print axioms ConstructedSelector.handoff_is_actual_old_selector_initial
#print axioms ConstructedSelector.paid_material_selector_revision
#print axioms ConstructedSelector.complete_formation_to_revision
#print axioms ConstructedSelector.full_witness_accounting
#print axioms ConstructedSelector.two_assembled_mappings
#print axioms ConstructedSelector.fuel_does_not_substitute_for_parts
#print axioms ConstructedSelector.exhausted_old_witness_cannot_assemble
#print axioms ConstructedSelector.step_part_ledgers
#print axioms ConstructedSelector.trace_part_ledgers
#print axioms ConstructedSelector.abstract_trace_lifts_with_parts
#print axioms ConstructedSelector.material_trace_lift_iff
#print axioms ConstructedSelector.no_trial_before_initial_assembly
#print axioms ConstructedSelector.step_preserves_hardware
#print axioms ConstructedSelector.trace_preserves_hardware
#print axioms ConstructedSelector.active_reachable_selector_has_consumed_parts
#print axioms ConstructedSelector.parts_do_not_substitute_for_fuel
#print axioms ConstructedSelector.old_mapping_cannot_be_reassembled_from_spent_parts
#print axioms ConstructedSelector.wrong_first_construction_history
#print axioms ConstructedSelector.wrong_first_strands_available_source
