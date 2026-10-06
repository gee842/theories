import Std
import GenerativeCore
import FormedSelection
import SelectorRevision

/- Paid formation of alternative selector-updating modules. The bridge is an
explicit additional retooling law, not an identification of molecular chemistry. -/
namespace UpdaterFormation

structure Parameters where
  selector : SelectorRevision.Parameters
  moduleAssembly : Nat
  moduleRenewal : Nat
  moduleLifetime : Nat
  adapter : Nat
deriving DecidableEq, Repr

def effective (p : Parameters) : SelectorRevision.Parameters :=
  { p.selector with renewal := p.selector.renewal + p.moduleRenewal }

def Admissible (p : Parameters) : Prop :=
  SelectorRevision.Admissible (effective p) ∧
  0 < p.moduleAssembly ∧ 0 < p.moduleRenewal ∧ 0 < p.moduleLifetime ∧ 0 < p.adapter

structure State where
  core : SelectorRevision.State
  directed : Bool
  moduleLease : Nat
  selectorSeen : Bool
  remainder : Nat
  material : Nat
deriving DecidableEq, Repr

inductive Event where
  | formModule (directed : Bool)
  | formSelector (orientation : Bool)
  | trial (signal : Bool)
  | reverse
  | expire
deriving DecidableEq, Repr

def selectorAllowed (s : State) (m : Bool) : Prop :=
  s.directed = false ∨ s.selectorSeen = false ∨ m = !s.core.selector

def Enabled (p : Parameters) (s : State) : Event → Prop
  | .formModule _ => s.moduleLease = 0 ∧ p.moduleAssembly ≤ s.core.fuel
  | .formSelector m => 0 < s.moduleLease ∧ selectorAllowed s m ∧
      SelectorRevision.Enabled (effective p) s.core (.assemble m)
  | .trial b => 0 < s.moduleLease ∧
      SelectorRevision.Enabled (effective p) s.core (.trial b)
  | .reverse => True
  | .expire => SelectorRevision.Enabled (effective p) s.core .expire

def advance (p : Parameters) (s : State) : Event → State
  | .formModule u => { s with directed := u, moduleLease := p.moduleLifetime, core := { s.core with fuel := s.core.fuel - p.moduleAssembly } }
  | .formSelector m => { s with selectorSeen := true, core := SelectorRevision.advance (effective p) s.core (.assemble m) }
  | .trial b => { s with core := SelectorRevision.advance (effective p) s.core (.trial b), moduleLease := if s.core.selector = s.core.regime then p.moduleLifetime else s.moduleLease - 1 }
  | .reverse => { s with core := SelectorRevision.advance (effective p) s.core .reverse }
  | .expire => { s with core := SelectorRevision.advance (effective p) s.core .expire }

def Step (p : Parameters) (s : State) (a : Event) (t : State) : Prop :=
  Enabled p s a ∧ t = advance p s a

instance (p : Parameters) (s : State) (a : Event) : Decidable (Enabled p s a) := by
  cases a <;> unfold Enabled <;> unfold selectorAllowed <;> infer_instance

instance (p : Parameters) (s : State) (a : Event) (t : State) :
    Decidable (Step p s a t) := by unfold Step; infer_instance

def process (p : Parameters) : Generative.Process State Event := ⟨Step p⟩
def Trace (p : Parameters) := Generative.Trace (process p)

def projection : Event → Option SelectorRevision.Event
  | .formModule _ => none
  | .formSelector m => some (.assemble m)
  | .trial b => some (.trial b)
  | .reverse => some .reverse
  | .expire => some .expire

def expenditure (p : Parameters) (s : State) (a : Event) : Nat :=
  match projection a with
  | none => p.moduleAssembly
  | some e => SelectorRevision.expenditure (effective p) s.core e

def waste (p : Parameters) (s : State) (a : Event) : Nat :=
  match projection a with
  | none => 0
  | some e => SelectorRevision.waste (effective p) s.core e

def energy (p : Parameters) (s : State) : Nat :=
  SelectorRevision.energy (effective p) s.core + s.remainder

def spentAlong (p : Parameters) (s : State) : List Event → Nat
  | [] => 0
  | a :: as => expenditure p s a + waste p s a + spentAlong p (advance p s a) as

theorem event_projection {p : Parameters} {s t : State} {a : Event}
    {e : SelectorRevision.Event} (h : Step p s a t) (he : projection a = some e) :
    SelectorRevision.Step (effective p) s.core e t.core := by
  rcases h with ⟨hg, rfl⟩
  cases a <;> simp only [projection, Option.some.injEq] at he
  · contradiction
  · subst e; exact ⟨hg.2.2, rfl⟩
  · subst e; exact ⟨hg.2, rfl⟩
  · subst e; exact ⟨trivial, rfl⟩
  · subst e; exact ⟨hg, rfl⟩

theorem step_remainder_material {p : Parameters} {s t : State} {a : Event}
    (h : Step p s a t) : t.remainder = s.remainder ∧ t.material = s.material := by
  rcases h with ⟨_, rfl⟩
  cases a <;> exact ⟨rfl, rfl⟩

theorem step_energy_ledger {p : Parameters} {s t : State} {a : Event}
    (hp : Admissible p) (h : Step p s a t) :
    energy p t + expenditure p s a + waste p s a = energy p s := by
  have hm := (step_remainder_material h).1
  cases a with
  | formModule u =>
    rcases h with ⟨hg, rfl⟩
    have hf := hg.2
    simp only [energy, advance, SelectorRevision.energy, expenditure, waste, projection]
    omega
  | formSelector m =>
    have hh := SelectorRevision.step_energy_ledger hp.1 (event_projection h rfl)
    simp only [energy, expenditure, waste, projection]
    omega
  | trial b =>
    have hh := SelectorRevision.step_energy_ledger hp.1 (event_projection h rfl)
    simp only [energy, expenditure, waste, projection]
    omega
  | reverse =>
    have hh := SelectorRevision.step_energy_ledger hp.1 (event_projection h rfl)
    simp only [energy, expenditure, waste, projection]
    omega
  | expire =>
    have hh := SelectorRevision.step_energy_ledger hp.1 (event_projection h rfl)
    simp only [energy, expenditure, waste, projection]
    omega

theorem trace_energy_ledger {p : Parameters} {s t : State} {as : List Event}
    (hp : Admissible p) (h : Trace p s as t) :
    energy p t + spentAlong p s as = energy p s := by
  induction h with
  | nil => simp [spentAlong]
  | @cons s u t a as hs ht ih =>
    have hh := step_energy_ledger hp hs
    have hu : u = advance p s a := hs.2
    subst u
    simp only [spentAlong]
    omega

theorem trace_material_preserved {p : Parameters} {s t : State} {as : List Event}
    (h : Trace p s as t) : t.material = s.material := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact ih.trans (step_remainder_material hs).2

theorem trace_projects_when_no_modules_formed {p : Parameters} {s t : State}
    {as : List Event} (h : Trace p s as t)
    (hn : ∀ a ∈ as, (projection a).isSome = true) :
    SelectorRevision.Trace (effective p) s.core (as.filterMap projection) t.core := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs ht ih =>
    have ha := hn a (by simp)
    cases he : projection a with
    | none => simp [he] at ha
    | some e =>
      simp only [List.filterMap_cons, he]
      apply Generative.Trace.cons (event_projection hs he)
      exact ih (fun b hb => hn b (by simp [hb]))

theorem directed_module_changes_available_assembly (p : Parameters) (s : State)
    (hu : 0 < s.moduleLease) (hs : s.selectorSeen = true)
    (hl : s.core.lease = 0) (hf : p.selector.assembly ≤ s.core.fuel) :
    Enabled p { s with directed := false } (.formSelector s.core.selector) ∧
    ¬ Enabled p { s with directed := true } (.formSelector s.core.selector) := by
  constructor
  · exact ⟨hu, Or.inl rfl, hl, hf⟩
  · intro h
    have hm := h.2.1
    simp [selectorAllowed, hs] at hm

theorem module_change_requires_paid_formation {p : Parameters} {s t : State} {a : Event}
    (h : Step p s a t) (hc : t.directed ≠ s.directed) :
    ∃ u, a = .formModule u ∧ s.moduleLease = 0 ∧
      t.core.fuel + p.moduleAssembly = s.core.fuel := by
  rcases h with ⟨hg, rfl⟩
  cases a with
  | formModule u =>
    have hf : p.moduleAssembly ≤ s.core.fuel := hg.2
    refine ⟨u, rfl, hg.1, ?_⟩
    simp only [advance]; omega
  | formSelector m => exact False.elim (hc rfl)
  | trial b => exact False.elim (hc rfl)
  | reverse => exact False.elim (hc rfl)
  | expire => exact False.elim (hc rfl)

/- A paid interface consumes one previously formed A and H into two reusable
material slots. Other material is retained as an undifferentiated inventory. -/
def BridgeEnabled (p : Parameters) (M : Nat) (s : FormedSelection.State) : Prop :=
  FormedSelection.Valid M s ∧ s.intact = true ∧
  0 < FormedSelection.aCount s ∧ 0 < FormedSelection.hCount s ∧
  s.localFuel = true ∧ p.adapter ≤ s.fuel

def entrance (p : Parameters) (M : Nat) (s : FormedSelection.State) (z : Bool) : State :=
  { core := { fuel := s.fuel - p.adapter + FormedSelection.bit s.localFuel,
              packets := s.source / p.selector.packet, selector := false,
              lease := 0, regime := z },
    directed := false, moduleLease := 0, selectorSeen := false,
    remainder := s.source % p.selector.packet, material := M }

theorem bridge_energy_exact {p : Parameters} {M : Nat} {s : FormedSelection.State}
    (hb : BridgeEnabled p M s) (z : Bool) :
    energy p (entrance p M s z) + p.adapter = FormedSelection.energy s := by
  have hf : p.adapter ≤ s.fuel := hb.2.2.2.2.2
  have he : s.source % p.selector.packet +
      (s.source / p.selector.packet) * p.selector.packet = s.source := by
    simpa [Nat.mul_comm] using Nat.mod_add_div s.source p.selector.packet
  simp only [energy, entrance, SelectorRevision.energy, effective, FormedSelection.energy]
  omega

theorem bridge_has_two_actual_materials {p : Parameters} {M : Nat}
    {s : FormedSelection.State} (hb : BridgeEnabled p M s) : 2 ≤ M := by
  have hh := FormedSelection.population_type_sum s
  have ha := hb.2.2.1
  have hb' := hb.2.2.2.1
  have hv := hb.1
  unfold FormedSelection.Valid at hv
  omega

theorem bridge_material_exact {p : Parameters} {M : Nat} {s : FormedSelection.State}
    (hb : BridgeEnabled p M s) : 2 + (M-2) = M := by
  have hh := bridge_has_two_actual_materials hb
  omega

theorem old_depleted_witness_cannot_pay_bridge {p : Parameters}
    (hp : 0 < p.adapter) : ¬ BridgeEnabled p 3 FormedSelection.copied := by
  intro h
  have hf := h.2.2.2.2.2
  simp [FormedSelection.copied] at hf
  omega

inductive JointState where
  | formation (s : FormedSelection.State)
  | organization (s : State)
deriving DecidableEq, Repr

inductive JointEvent where
  | old (a : FormedSelection.Event)
  | connect
  | run (a : Event)
deriving DecidableEq, Repr

def JointStep (p : Parameters) (M : Nat) (z : Bool) :
    JointState → JointEvent → JointState → Prop
  | .formation s, .old a, .formation t => FormedSelection.Step M s a t
  | .formation s, .connect, .organization t => BridgeEnabled p M s ∧ t = entrance p M s z
  | .organization s, .run a, .organization t => Step p s a t
  | _, _, _ => False

def jointProcess (p : Parameters) (M : Nat) (z : Bool) :
    Generative.Process JointState JointEvent := ⟨JointStep p M z⟩

theorem old_step_preserved_exactly (p : Parameters) (M : Nat) (z : Bool)
    (s t : FormedSelection.State) (a : FormedSelection.Event) :
    JointStep p M z (.formation s) (.old a) (.formation t) ↔
    FormedSelection.Step M s a t := Iff.rfl

theorem old_trace_embeds {p : Parameters} {M : Nat} {z : Bool}
    {s t : FormedSelection.State} {as : List FormedSelection.Event}
    (h : FormedSelection.Trace M s as t) :
    Generative.Trace (jointProcess p M z) (.formation s)
      (as.map JointEvent.old) (.formation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs ht ih =>
    apply Generative.Trace.cons (m := .formation u)
    · exact hs
    · exact ih

theorem organization_trace_embeds {p : Parameters} {M : Nat} {z : Bool}
    {s t : State} {as : List Event} (h : Trace p s as t) :
    Generative.Trace (jointProcess p M z) (.organization s)
      (as.map JointEvent.run) (.organization t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs ht ih =>
    apply Generative.Trace.cons (m := .organization u)
    · exact hs
    · exact ih

theorem actual_formation_bridge_continuation {p : Parameters} {M : Nat} {z : Bool}
    {s e : FormedSelection.State} {t : State}
    {as : List FormedSelection.Event} {bs : List Event}
    (hOld : FormedSelection.Trace M s as e) (hBridge : BridgeEnabled p M e)
    (hNew : Trace p (entrance p M e z) bs t) :
    Generative.Trace (jointProcess p M z) (.formation s)
      (as.map JointEvent.old ++ .connect :: bs.map JointEvent.run) (.organization t) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.formation e, old_trace_embeds hOld, ?_⟩
  apply Generative.Trace.cons (m := .organization (entrance p M e z))
  · exact ⟨hBridge, rfl⟩
  · exact organization_trace_embeds hNew

theorem joined_energy_ledger {p : Parameters} {M : Nat} {z : Bool}
    {s e : FormedSelection.State} {t : State}
    {as : List FormedSelection.Event} {bs : List Event}
    (hp : Admissible p) (hOld : FormedSelection.Trace M s as e)
    (hBridge : BridgeEnabled p M e) (hNew : Trace p (entrance p M e z) bs t) :
    energy p t + spentAlong p (entrance p M e z) bs + p.adapter +
      FormedSelection.tally FormedSelection.expenditure as = FormedSelection.energy s := by
  have h1 := FormedSelection.trace_energy_ledger hOld
  have h2 := bridge_energy_exact hBridge z
  have h3 := trace_energy_ledger hp hNew
  omega

/- Exact synchronized-expiry diagnostic: new module and selector are both paid.
The independent random choice probabilities are established analytically. -/
def bundleRecoveryCost (g c d L k j : Nat) : Nat :=
  k*d+g+c+d+j*(g+c+L*d)

theorem synchronized_prefix_affordable_iff (g c d L k j F : Nat) :
    (∃ x, SelectorRevision.Paid F
      (SelectorRevision.recoveryCosts (g+c) d L k j) x) ↔
    bundleRecoveryCost g c d L k j ≤ F := by
  rw [SelectorRevision.recovery_prefix_affordable_iff]
  simp only [SelectorRevision.recoveryCost, bundleRecoveryCost]
  omega

theorem new_module_budget_obstruction (g c d F : Nat) (h : F < g+c+d) :
    ¬ ∃ x, SelectorRevision.Paid F [g,c,d] x := by
  rw [SelectorRevision.paid_exists_iff]
  simp only [List.sum_cons, List.sum_nil]
  omega

def primary : Parameters := ⟨⟨1, 2, 1, 6, 2⟩, 2, 1, 4, 1⟩
def oldInitial : FormedSelection.State := ⟨0, 0, .empty, false, false, 18, 97⟩
def oldEntrance : FormedSelection.State := ⟨0, 1, .active, true, true, 14, 96⟩
def oldPreparation : List FormedSelection.Event :=
  [.formH, .formA, .associateA, .repair, .capture]

theorem actual_old_preparation : FormedSelection.Trace 2 oldInitial oldPreparation oldEntrance := by
  apply FormedSelection.Trace.cons (u := ⟨0, 1, .empty, false, false, 17, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 1, .empty, false, false, 16, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 1, .active, false, false, 15, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 1, .active, true, false, 14, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := oldEntrance) (by decide)
  exact .nil _

theorem actual_old_entrance_enabled : BridgeEnabled primary 2 oldEntrance := by
  unfold BridgeEnabled
  decide

def exampleState (F H : Nat) (m : Bool) (ell : Nat) (z u : Bool) (J : Nat)
    (seen : Bool := true) : State := ⟨⟨F,H,m,ell,z⟩,u,J,seen,0,2⟩

def primaryEntrance : State := exampleState 14 16 false 0 false false 0 false
def finalWitness : State := exampleState 9 7 true 2 true true 4
def updaterWitness : List Event :=
  [.formModule false, .formSelector false,
   .trial false, .trial true, .trial false, .trial true, .reverse,
   .trial false, .trial true, .formSelector false, .trial false, .trial true,
   .formModule true, .formSelector true, .trial false]

theorem entrance_is_actual_paid_state : entrance primary 2 oldEntrance false = primaryEntrance := by
  decide

theorem paid_updater_revision_witness : Trace primary primaryEntrance updaterWitness finalWitness := by
  apply Generative.Trace.cons (m := exampleState 12 16 false 0 false false 4 false) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 11 16 false 2 false false 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 13 15 false 2 false false 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 15 14 false 2 false false 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 17 13 false 2 false false 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 19 12 false 2 false false 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 19 12 false 2 true false 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 17 11 false 1 true false 3) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 15 10 false 0 true false 2) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 14 10 false 2 true false 2) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 12 9 false 1 true false 1) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 10 8 false 0 true false 0) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 8 8 false 0 true true 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleState 7 8 true 2 true true 4) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := finalWitness) (by change Step _ _ _ _; decide)
  exact .nil _

theorem whole_preparation_to_changed_updater_witness :
    Generative.Trace (jointProcess primary 2 false) (.formation oldInitial)
      (oldPreparation.map JointEvent.old ++ .connect :: updaterWitness.map JointEvent.run)
      (.organization finalWitness) := by
  apply actual_formation_bridge_continuation actual_old_preparation actual_old_entrance_enabled
  rw [entrance_is_actual_paid_state]
  exact paid_updater_revision_witness

theorem whole_witness_accounting :
    FormedSelection.energy oldInitial = 115 ∧
    FormedSelection.tally FormedSelection.expenditure oldPreparation = 4 ∧
    primary.adapter = 1 ∧ spentAlong primary primaryEntrance updaterWitness = 59 ∧
    energy primary finalWitness = 51 ∧ finalWitness.material = 2 := by decide

end UpdaterFormation

#print axioms UpdaterFormation.event_projection
#print axioms UpdaterFormation.step_remainder_material
#print axioms UpdaterFormation.step_energy_ledger
#print axioms UpdaterFormation.trace_energy_ledger
#print axioms UpdaterFormation.trace_material_preserved
#print axioms UpdaterFormation.trace_projects_when_no_modules_formed
#print axioms UpdaterFormation.directed_module_changes_available_assembly
#print axioms UpdaterFormation.module_change_requires_paid_formation
#print axioms UpdaterFormation.bridge_energy_exact
#print axioms UpdaterFormation.bridge_has_two_actual_materials
#print axioms UpdaterFormation.bridge_material_exact
#print axioms UpdaterFormation.old_depleted_witness_cannot_pay_bridge
#print axioms UpdaterFormation.old_step_preserved_exactly
#print axioms UpdaterFormation.old_trace_embeds
#print axioms UpdaterFormation.organization_trace_embeds
#print axioms UpdaterFormation.actual_formation_bridge_continuation
#print axioms UpdaterFormation.joined_energy_ledger
#print axioms UpdaterFormation.synchronized_prefix_affordable_iff
#print axioms UpdaterFormation.new_module_budget_obstruction
#print axioms UpdaterFormation.actual_old_preparation
#print axioms UpdaterFormation.actual_old_entrance_enabled
#print axioms UpdaterFormation.entrance_is_actual_paid_state
#print axioms UpdaterFormation.paid_updater_revision_witness
#print axioms UpdaterFormation.whole_preparation_to_changed_updater_witness
#print axioms UpdaterFormation.whole_witness_accounting
