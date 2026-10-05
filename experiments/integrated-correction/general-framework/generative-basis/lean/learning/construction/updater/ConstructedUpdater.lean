import UpdaterFormation

/-!
Typed consumable backing for the paid updater law. This is a restriction of
UpdaterFormation, not an equivalence with its recyclable two-slot material law.
Every module event is retained, including its paid support transition. Recipes,
wiring and phase separation remain supplied. Bound counters retain spent parts.
-/
namespace ConstructedUpdater

structure Running where
  core : UpdaterFormation.State
  aFree : Nat
  hFree : Nat
  resident : FormedSelection.Resident
  intact : Bool
  boundA : Nat
  boundH : Nat
  precursor : Nat
deriving DecidableEq, Repr

def partCost (kind : Bool) : UpdaterFormation.Event → Nat
  | .formModule _ => 1
  | .formSelector m => if m = kind then 2 else 0
  | _ => 0

def partCostAlong (kind : Bool) : List UpdaterFormation.Event → Nat
  | [] => 0
  | a :: as => partCost kind a + partCostAlong kind as

def matter (r : Running) : Nat :=
  r.aFree + r.hFree + FormedSelection.occupied r.resident + r.boundA + r.boundH

def totalMatter (r : Running) : Nat := matter r + r.precursor

def PartsReady (r : Running) (a : UpdaterFormation.Event) : Prop :=
  partCost false a ≤ r.aFree ∧ partCost true a ≤ r.hFree

def advance (p : UpdaterFormation.Parameters) (r : Running) (a : UpdaterFormation.Event) : Running :=
  { r with
    core := UpdaterFormation.advance p r.core a
    aFree := r.aFree - partCost false a
    hFree := r.hFree - partCost true a
    boundA := r.boundA + partCost false a
    boundH := r.boundH + partCost true a }

def Step (p : UpdaterFormation.Parameters) (r : Running) (a : UpdaterFormation.Event) (t : Running) : Prop :=
  UpdaterFormation.Enabled p r.core a ∧ PartsReady r a ∧ t = advance p r a

instance (r : Running) (a : UpdaterFormation.Event) : Decidable (PartsReady r a) := by
  unfold PartsReady; infer_instance
instance (p : UpdaterFormation.Parameters) (r t : Running) (a : UpdaterFormation.Event) : Decidable (Step p r a t) := by
  unfold Step; infer_instance

def process (p : UpdaterFormation.Parameters) : Generative.Process Running UpdaterFormation.Event := ⟨Step p⟩
def Trace (p : UpdaterFormation.Parameters) := Generative.Trace (process p)

theorem step_projects {p : UpdaterFormation.Parameters} {r t : Running} {a : UpdaterFormation.Event}
    (h : Step p r a t) : UpdaterFormation.Step p r.core a t.core := by
  rcases h with ⟨he, _, rfl⟩
  exact ⟨he, rfl⟩

theorem trace_projects {p : UpdaterFormation.Parameters} {r t : Running} {as : List UpdaterFormation.Event}
    (h : Trace p r as t) : UpdaterFormation.Trace p r.core as t.core := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons (step_projects hs) ih

theorem command_lifts_iff (p : UpdaterFormation.Parameters) (r : Running) (a : UpdaterFormation.Event) :
    (∃ t, Step p r a t) ↔ UpdaterFormation.Enabled p r.core a ∧ PartsReady r a := by
  constructor
  · rintro ⟨t, he, hm, _⟩; exact ⟨he, hm⟩
  · rintro ⟨he, hm⟩; exact ⟨advance p r a, he, hm, rfl⟩

theorem step_part_ledgers {p : UpdaterFormation.Parameters} {r t : Running}
    {a : UpdaterFormation.Event} (h : Step p r a t) :
    t.aFree + partCost false a = r.aFree ∧ t.hFree + partCost true a = r.hFree ∧
    t.boundA = r.boundA + partCost false a ∧ t.boundH = r.boundH + partCost true a := by
  rcases h with ⟨_, hp, rfl⟩
  change r.aFree - partCost false a + partCost false a = r.aFree ∧
    r.hFree - partCost true a + partCost true a = r.hFree ∧
    r.boundA + partCost false a = r.boundA + partCost false a ∧
    r.boundH + partCost true a = r.boundH + partCost true a
  unfold PartsReady at hp
  exact ⟨by omega, by omega, rfl, rfl⟩

theorem trace_part_ledgers {p : UpdaterFormation.Parameters} {r t : Running}
    {as : List UpdaterFormation.Event} (h : Trace p r as t) :
    t.aFree + partCostAlong false as = r.aFree ∧ t.hFree + partCostAlong true as = r.hFree ∧
    t.boundA = r.boundA + partCostAlong false as ∧ t.boundH = r.boundH + partCostAlong true as := by
  induction h with
  | nil => exact ⟨rfl, rfl, rfl, rfl⟩
  | cons hs _ ih =>
    have hh := step_part_ledgers hs
    simp only [partCostAlong]
    refine ⟨?_, ?_, ?_, ?_⟩ <;> omega

theorem abstract_trace_lifts_with_parts {p : UpdaterFormation.Parameters}
    {s t : UpdaterFormation.State} {as : List UpdaterFormation.Event}
    (h : UpdaterFormation.Trace p s as t) (r : Running) (hr : r.core = s)
    (ha : partCostAlong false as ≤ r.aFree) (hh : partCostAlong true as ≤ r.hFree) :
    ∃ q, Trace p r as q ∧ q.core = t := by
  induction h generalizing r with
  | nil => exact ⟨r, .nil r, hr⟩
  | @cons s u t a as hs ht ih =>
    have hp : PartsReady r a := by
      unfold PartsReady
      simp only [partCostAlong] at ha hh
      exact ⟨by omega, by omega⟩
    have he : UpdaterFormation.Enabled p r.core a := by rw [hr]; exact hs.1
    have hstep : Step p r a (advance p r a) := ⟨he, hp, rfl⟩
    have hproject : (advance p r a).core = u := by
      change UpdaterFormation.advance p r.core a = u
      rw [hr]; exact hs.2.symm
    have hl := step_part_ledgers hstep
    have ha' : partCostAlong false as ≤ (advance p r a).aFree := by
      simp only [partCostAlong] at ha; omega
    have hh' : partCostAlong true as ≤ (advance p r a).hFree := by
      simp only [partCostAlong] at hh; omega
    obtain ⟨q, hq, hqt⟩ := ih (advance p r a) hproject ha' hh'
    exact ⟨q, .cons hstep hq, hqt⟩

/-- Exact feasibility criterion for any finite word, including all paid updater events. -/
theorem material_trace_lift_iff (p : UpdaterFormation.Parameters) (r : Running)
    (as : List UpdaterFormation.Event) (s : UpdaterFormation.State) :
    (∃ q, Trace p r as q ∧ q.core = s) ↔
      UpdaterFormation.Trace p r.core as s ∧
      partCostAlong false as ≤ r.aFree ∧ partCostAlong true as ≤ r.hFree := by
  constructor
  · rintro ⟨q, hq, rfl⟩
    have hl := trace_part_ledgers hq
    exact ⟨trace_projects hq, by omega, by omega⟩
  · rintro ⟨ht, ha, hh⟩
    exact abstract_trace_lifts_with_parts ht r rfl ha hh

theorem step_preserves_side_stores {p : UpdaterFormation.Parameters} {r t : Running}
    {a : UpdaterFormation.Event} (h : Step p r a t) :
    t.resident = r.resident ∧ t.intact = r.intact ∧ t.precursor = r.precursor := by
  rcases h with ⟨_, _, rfl⟩; exact ⟨rfl, rfl, rfl⟩

theorem trace_preserves_side_stores {p : UpdaterFormation.Parameters} {r t : Running}
    {as : List UpdaterFormation.Event} (h : Trace p r as t) :
    t.resident = r.resident ∧ t.intact = r.intact ∧ t.precursor = r.precursor := by
  induction h with
  | nil => exact ⟨rfl, rfl, rfl⟩
  | cons hs _ ih =>
    have hh := step_preserves_side_stores hs
    exact ⟨ih.1.trans hh.1, ih.2.1.trans hh.2.1, ih.2.2.trans hh.2.2⟩

theorem trace_preserves_matter {p : UpdaterFormation.Parameters} {r t : Running}
    {as : List UpdaterFormation.Event} (h : Trace p r as t) :
    matter t = matter r ∧ totalMatter t = totalMatter r := by
  have hp := trace_part_ledgers h
  have hs := trace_preserves_side_stores h
  simp only [matter, totalMatter, hs.1, hs.2.2]
  exact ⟨by omega, by omega⟩

theorem trace_energy_ledger {p : UpdaterFormation.Parameters} {r t : Running}
    {as : List UpdaterFormation.Event} (hp : UpdaterFormation.Admissible p) (h : Trace p r as t) :
    UpdaterFormation.energy p t.core + UpdaterFormation.spentAlong p r.core as =
      UpdaterFormation.energy p r.core :=
  UpdaterFormation.trace_energy_ledger hp (trace_projects h)

def BridgeEnabled (p : UpdaterFormation.Parameters) (M : Nat) (s : FormedSelection.State) : Prop :=
  FormedSelection.Valid M s ∧ s.intact = true ∧ 1 ≤ s.aFree ∧ 1 ≤ s.hFree ∧
    s.localFuel = true ∧ p.adapter ≤ s.fuel
instance (p : UpdaterFormation.Parameters) (M : Nat) (s : FormedSelection.State) :
    Decidable (BridgeEnabled p M s) := by unfold BridgeEnabled; infer_instance

/-- One free A and H are permanently incorporated in the adapter; the old local
energy unit is converted once by UF.entrance and is not duplicated here. -/
def entrance (p : UpdaterFormation.Parameters) (M : Nat) (s : FormedSelection.State) (z : Bool) : Running :=
  ⟨UpdaterFormation.entrance p M s z, s.aFree - 1, s.hFree - 1, s.resident,
    s.intact, 1, 1, M - FormedSelection.population s⟩

theorem bridge_projects {p : UpdaterFormation.Parameters} {M : Nat} {s : FormedSelection.State}
    (h : BridgeEnabled p M s) : UpdaterFormation.BridgeEnabled p M s := by
  rcases h with ⟨hv, hi, ha, hh, hl, hf⟩
  refine ⟨hv, hi, ?_, ?_, hl, hf⟩
  · unfold FormedSelection.aCount; omega
  · unfold FormedSelection.hCount; omega

theorem bridge_energy_exact {p : UpdaterFormation.Parameters} {M : Nat} {s : FormedSelection.State}
    (h : BridgeEnabled p M s) (z : Bool) :
    UpdaterFormation.energy p (entrance p M s z).core + p.adapter = FormedSelection.energy s :=
  UpdaterFormation.bridge_energy_exact (bridge_projects h) z

theorem bridge_material_exact {p : UpdaterFormation.Parameters} {M : Nat} {s : FormedSelection.State}
    (h : BridgeEnabled p M s) (z : Bool) :
    matter (entrance p M s z) = FormedSelection.population s ∧
    totalMatter (entrance p M s z) = M := by
  rcases h with ⟨hv, _, ha, hh, _, _⟩
  unfold FormedSelection.Valid at hv
  simp only [matter, totalMatter, entrance, FormedSelection.population] at *
  exact ⟨by omega, by omega⟩

theorem bridge_retains_resident_site (p : UpdaterFormation.Parameters) (M : Nat)
    (s : FormedSelection.State) (z : Bool) :
    (entrance p M s z).resident = s.resident ∧ (entrance p M s z).intact = s.intact :=
  ⟨rfl, rfl⟩

theorem changed_updater_consumes_parts {p : UpdaterFormation.Parameters} {r t : Running}
    {a : UpdaterFormation.Event} (h : Step p r a t) (hc : t.core.directed ≠ r.core.directed) :
    ∃ u, a = .formModule u ∧ t.core.core.fuel + p.moduleAssembly = r.core.core.fuel ∧
      t.aFree + 1 = r.aFree ∧ t.hFree + 1 = r.hFree ∧
      t.boundA = r.boundA + 1 ∧ t.boundH = r.boundH + 1 := by
  obtain ⟨u, ha, _, hf⟩ := UpdaterFormation.module_change_requires_paid_formation (step_projects h) hc
  subst a
  have hl := step_part_ledgers h
  exact ⟨u, rfl, hf, hl⟩

def ModuleHardware (r : Running) : Prop :=
  1 ≤ r.boundA ∧ 1 ≤ r.boundH ∧
    (0 < r.core.moduleLease → 2 ≤ r.boundA ∧ 2 ≤ r.boundH)

theorem step_preserves_module_hardware {p : UpdaterFormation.Parameters} {r t : Running}
    {a : UpdaterFormation.Event} (hi : ModuleHardware r) (h : Step p r a t) : ModuleHardware t := by
  rcases h with ⟨he, _, rfl⟩
  rcases hi with ⟨ha, hh, hi⟩
  cases a with
  | formModule u => simp only [ModuleHardware, advance, partCost, UpdaterFormation.advance]; exact ⟨by omega, by omega, fun _ => ⟨by omega, by omega⟩⟩
  | formSelector m =>
    have hm := hi he.1
    simp only [ModuleHardware, advance, UpdaterFormation.advance]
    exact ⟨by omega, by omega, fun _ => ⟨by omega, by omega⟩⟩
  | trial b =>
    have hm := hi he.1
    simp only [ModuleHardware, advance, UpdaterFormation.advance, partCost]
    exact ⟨by omega, by omega, fun _ => ⟨by omega, by omega⟩⟩
  | reverse => simpa [ModuleHardware, advance, UpdaterFormation.advance, partCost] using And.intro ha (And.intro hh hi)
  | expire => simpa [ModuleHardware, advance, UpdaterFormation.advance, partCost] using And.intro ha (And.intro hh hi)

theorem reachable_active_module_has_new_parts {p : UpdaterFormation.Parameters} {M : Nat}
    {s : FormedSelection.State} {z : Bool} {t : Running} {as : List UpdaterFormation.Event}
    (h : Trace p (entrance p M s z) as t) (ha : 0 < t.core.moduleLease) :
    2 ≤ t.boundA ∧ 2 ≤ t.boundH := by
  have hi : ModuleHardware (entrance p M s z) := by simp [ModuleHardware, entrance, UpdaterFormation.entrance]
  have invariant : ∀ {r t : Running} {as : List UpdaterFormation.Event},
      Trace p r as t → ModuleHardware r → ModuleHardware t := by
    intro r t as ht
    induction ht with
    | nil => exact fun hh => hh
    | cons hs _ ih => exact fun hh => ih (step_preserves_module_hardware hh hs)
  exact (invariant h hi).2.2 ha

inductive Stage where
  | formation (body : FormedSelection.State)
  | operation (running : Running)
deriving DecidableEq, Repr
inductive Event where
  | form (event : FormedSelection.Event)
  | handoff
  | operate (event : UpdaterFormation.Event)
deriving DecidableEq, Repr

def StagedStep (p : UpdaterFormation.Parameters) (M : Nat) (z : Bool) : Stage → Event → Stage → Prop
  | .formation s, .form a, .formation t => FormedSelection.Step M s a t
  | .formation s, .handoff, .operation t => BridgeEnabled p M s ∧ t = entrance p M s z
  | .operation r, .operate a, .operation t => Step p r a t
  | _, _, _ => False

def stagedProcess (p : UpdaterFormation.Parameters) (M : Nat) (z : Bool) : Generative.Process Stage Event :=
  ⟨StagedStep p M z⟩
def StagedTrace (p : UpdaterFormation.Parameters) (M : Nat) (z : Bool) :=
  Generative.Trace (stagedProcess p M z)

theorem formation_trace_embeds {p : UpdaterFormation.Parameters} {M : Nat} {z : Bool}
    {s t : FormedSelection.State} {as : List FormedSelection.Event} (h : FormedSelection.Trace M s as t) :
    StagedTrace p M z (.formation s) (as.map Event.form) (.formation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih =>
    exact Generative.Trace.cons (m := Stage.formation u) hs ih

theorem operational_trace_embeds {p : UpdaterFormation.Parameters} {M : Nat} {z : Bool}
    {r t : Running} {as : List UpdaterFormation.Event} (h : Trace p r as t) :
    StagedTrace p M z (.operation r) (as.map Event.operate) (.operation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih =>
    exact Generative.Trace.cons (m := Stage.operation u) hs ih

theorem actual_formation_bridge_continuation {p : UpdaterFormation.Parameters} {M : Nat} {z : Bool}
    {s e : FormedSelection.State} {t : Running}
    {as : List FormedSelection.Event} {bs : List UpdaterFormation.Event}
    (hOld : FormedSelection.Trace M s as e) (hBridge : BridgeEnabled p M e)
    (hNew : Trace p (entrance p M e z) bs t) :
    StagedTrace p M z (.formation s)
      (as.map Event.form ++ .handoff :: bs.map Event.operate) (.operation t) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.formation e, formation_trace_embeds hOld, ?_⟩
  apply Generative.Trace.cons (m := .operation (entrance p M e z))
  · exact ⟨hBridge, rfl⟩
  · exact operational_trace_embeds hNew

theorem joined_energy_ledger {p : UpdaterFormation.Parameters} {M : Nat} {z : Bool}
    {s e : FormedSelection.State} {t : Running}
    {as : List FormedSelection.Event} {bs : List UpdaterFormation.Event}
    (hp : UpdaterFormation.Admissible p) (hOld : FormedSelection.Trace M s as e)
    (hBridge : BridgeEnabled p M e) (hNew : Trace p (entrance p M e z) bs t) :
    UpdaterFormation.energy p t.core + UpdaterFormation.spentAlong p (entrance p M e z).core bs +
      p.adapter + FormedSelection.tally FormedSelection.expenditure as = FormedSelection.energy s := by
  have h1 := FormedSelection.trace_energy_ledger hOld
  have h2 := bridge_energy_exact hBridge z
  have h3 := trace_energy_ledger hp hNew
  omega

theorem joined_material_ledger {p : UpdaterFormation.Parameters} {M : Nat} {z : Bool}
    {e : FormedSelection.State} {t : Running} {bs : List UpdaterFormation.Event}
    (hBridge : BridgeEnabled p M e) (hNew : Trace p (entrance p M e z) bs t) :
    matter t = FormedSelection.population e ∧ totalMatter t = M ∧ t.core.material = M := by
  have h1 := bridge_material_exact hBridge z
  have h2 := trace_preserves_matter hNew
  have h3 := UpdaterFormation.trace_material_preserved (trace_projects hNew)
  exact ⟨h2.1.trans h1.1, h2.2.trans h1.2, h3⟩

/-- UF's inert capacity label may be changed without changing its dynamics. -/
theorem core_material_relabel_trace {p : UpdaterFormation.Parameters}
    {s t : UpdaterFormation.State} {as : List UpdaterFormation.Event}
    (h : UpdaterFormation.Trace p s as t) (M : Nat) :
    UpdaterFormation.Trace p {s with material := M} as {t with material := M} := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih =>
    apply Generative.Trace.cons (m := {u with material := M})
    · rcases hs with ⟨he, rfl⟩
      constructor
      · cases a <;> exact he
      · cases a <;> rfl
    · exact ih

/-- Actual construction counts share each typed stock; they are not independent budgets. -/
def moduleCount : List UpdaterFormation.Event → Nat
  | [] => 0
  | .formModule _ :: as => 1 + moduleCount as
  | _ :: as => moduleCount as

def selectorCount (m : Bool) : List UpdaterFormation.Event → Nat
  | [] => 0
  | .formSelector k :: as => (if k = m then 1 else 0) + selectorCount m as
  | _ :: as => selectorCount m as

theorem cost_decomposes (m : Bool) (as : List UpdaterFormation.Event) :
    partCostAlong m as = moduleCount as + 2 * selectorCount m as := by
  induction as with
  | nil => rfl
  | cons a as ih =>
    cases a with
    | formModule u => simp only [partCostAlong, partCost, moduleCount, selectorCount]; omega
    | formSelector k =>
      simp only [partCostAlong, partCost, moduleCount, selectorCount]
      split <;> omega
    | trial b => simp only [partCostAlong, partCost, moduleCount, selectorCount]; omega
    | reverse => simp only [partCostAlong, partCost, moduleCount, selectorCount]; omega
    | expire => simp only [partCostAlong, partCost, moduleCount, selectorCount]; omega

theorem competing_construction_budgets {p : UpdaterFormation.Parameters} {r t : Running}
    {as : List UpdaterFormation.Event} (h : Trace p r as t) :
    moduleCount as + 2 * selectorCount false as ≤ r.aFree ∧
    moduleCount as + 2 * selectorCount true as ≤ r.hFree := by
  have hl := trace_part_ledgers h
  rw [cost_decomposes, cost_decomposes] at hl
  exact ⟨by omega, by omega⟩

theorem finite_stock_bounds_updater_formations {p : UpdaterFormation.Parameters} {r t : Running}
    {as : List UpdaterFormation.Event} (h : Trace p r as t) :
    moduleCount as ≤ r.aFree ∧ moduleCount as ≤ r.hFree := by
  have hl := competing_construction_budgets h
  exact ⟨by omega, by omega⟩

def initial : FormedSelection.State := ⟨0, 0, .empty, false, false, 29, 97⟩
def prepared : FormedSelection.State := ⟨7, 5, .active, true, true, 14, 96⟩
def formationEvents : List FormedSelection.Event :=
  [.formH, .formH, .formH, .formH, .formH,
   .formA, .formA, .formA, .formA, .formA, .formA, .formA, .formA,
   .associateA, .repair, .capture]

theorem actual_part_preparation : FormedSelection.Trace 13 initial formationEvents prepared := by
  apply FormedSelection.Trace.cons (u := ⟨0, 1, .empty, false, false, 28, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .empty, false, false, 27, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 3, .empty, false, false, 26, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 4, .empty, false, false, 25, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 5, .empty, false, false, 24, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 5, .empty, false, false, 23, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨2, 5, .empty, false, false, 22, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨3, 5, .empty, false, false, 21, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨4, 5, .empty, false, false, 20, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨5, 5, .empty, false, false, 19, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨6, 5, .empty, false, false, 18, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨7, 5, .empty, false, false, 17, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨8, 5, .empty, false, false, 16, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨7, 5, .active, false, false, 15, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨7, 5, .active, true, false, 14, 97⟩) (by decide)
  apply FormedSelection.Trace.cons (u := prepared) (by decide)
  exact .nil _

def ready : Running := entrance UpdaterFormation.primary 13 prepared false

def final : Running :=
  ⟨{ UpdaterFormation.finalWitness with material := 13 }, 0, 0, .active, true, 7, 5, 0⟩

theorem actual_typed_bridge : BridgeEnabled UpdaterFormation.primary 13 prepared := by decide

theorem inherited_entrance_exact :
    ready.core = { UpdaterFormation.primaryEntrance with material := 13 } ∧
    ready.aFree = 6 ∧ ready.hFree = 4 ∧ ready.boundA = 1 ∧ ready.boundH = 1 := by decide

/-- Pure evaluation helpers carry every real successor, never resetting fuel or parts. -/
def run (p : UpdaterFormation.Parameters) : Running → List UpdaterFormation.Event → Running
  | r, [] => r
  | r, a :: as => run p (advance p r a) as

def Runnable (p : UpdaterFormation.Parameters) : Running → List UpdaterFormation.Event → Prop
  | _, [] => True
  | r, a :: as => UpdaterFormation.Enabled p r.core a ∧ PartsReady r a ∧ Runnable p (advance p r a) as

def runnableDecidable (p : UpdaterFormation.Parameters) :
    (r : Running) → (as : List UpdaterFormation.Event) → Decidable (Runnable p r as)
  | _, [] => isTrue trivial
  | r, a :: as => by
    haveI : Decidable (Runnable p (advance p r a) as) := runnableDecidable p (advance p r a) as
    unfold Runnable
    infer_instance

instance (p : UpdaterFormation.Parameters) (r : Running) (as : List UpdaterFormation.Event) :
    Decidable (Runnable p r as) := runnableDecidable p r as

theorem runnable_trace {p : UpdaterFormation.Parameters} {r : Running}
    {as : List UpdaterFormation.Event} (h : Runnable p r as) : Trace p r as (run p r as) := by
  induction as generalizing r with
  | nil => exact .nil _
  | cons a as ih =>
    exact .cons ⟨h.1, h.2.1, rfl⟩ (ih h.2.2)

theorem actual_updater_revision : Trace UpdaterFormation.primary ready UpdaterFormation.updaterWitness final := by
  have h : Runnable UpdaterFormation.primary ready UpdaterFormation.updaterWitness := by decide
  have hh : run UpdaterFormation.primary ready UpdaterFormation.updaterWitness = final := by decide
  rw [← hh]
  exact runnable_trace h

theorem full_formation_to_updater_revision :
    StagedTrace UpdaterFormation.primary 13 false (.formation initial)
      (formationEvents.map Event.form ++ .handoff :: UpdaterFormation.updaterWitness.map Event.operate)
      (.operation final) :=
  actual_formation_bridge_continuation actual_part_preparation actual_typed_bridge actual_updater_revision

theorem whole_witness_accounting :
    FormedSelection.Absent initial ∧ FormedSelection.energy initial = 126 ∧
    FormedSelection.tally FormedSelection.expenditure formationEvents = 15 ∧
    UpdaterFormation.primary.adapter = 1 ∧
    UpdaterFormation.spentAlong UpdaterFormation.primary ready.core UpdaterFormation.updaterWitness = 59 ∧
    UpdaterFormation.energy UpdaterFormation.primary final.core = 51 ∧
    moduleCount UpdaterFormation.updaterWitness = 2 ∧
    selectorCount false UpdaterFormation.updaterWitness = 2 ∧ selectorCount true UpdaterFormation.updaterWitness = 1 ∧
    partCostAlong false UpdaterFormation.updaterWitness = 6 ∧ partCostAlong true UpdaterFormation.updaterWitness = 4 ∧
    totalMatter final = 13 ∧ final.boundA = 7 ∧ final.boundH = 5 ∧
    final.core.directed = true ∧ final.core.core.selector = true ∧ final.core.core.regime = true := by
  unfold FormedSelection.Absent
  decide

theorem old_two_material_bridge_is_insufficient :
    UpdaterFormation.BridgeEnabled UpdaterFormation.primary 2 UpdaterFormation.oldEntrance ∧
    ¬ BridgeEnabled UpdaterFormation.primary 2 UpdaterFormation.oldEntrance := by
  exact ⟨UpdaterFormation.actual_old_entrance_enabled, by decide⟩

/-- Configured counterexample, with all unavailable free parts retained as bound
material. No formation history is claimed for this fixture; exhausted below is
the corresponding obstruction reached by an actual paid history. -/
def noParts : Running := { ready with aFree := 0, hFree := 0, boundA := 7, boundH := 5 }
def noFuel : Running := { ready with core := { ready.core with core := { ready.core.core with fuel := 0 } } }

theorem fuel_does_not_substitute_for_parts :
    UpdaterFormation.Enabled UpdaterFormation.primary noParts.core (.formModule true) ∧
    ¬ ∃ t, Step UpdaterFormation.primary noParts (.formModule true) t := by
  constructor
  · decide
  · rw [command_lifts_iff]; decide

theorem parts_do_not_substitute_for_fuel :
    PartsReady noFuel (.formModule true) ∧
    ¬ ∃ t, Step UpdaterFormation.primary noFuel (.formModule true) t := by
  constructor
  · decide
  · rw [command_lifts_iff]; decide

/-- A second reversal spends existing fuel and exposes exhausted component stocks. -/
def exhaustionEvents : List UpdaterFormation.Event := [.reverse, .trial false, .trial true]
def exhausted : Running :=
  { final with core := { final.core with core := ⟨5,5,true,0,false⟩, moduleLease := 2 } }

theorem actual_post_revision_exhaustion : Trace UpdaterFormation.primary final exhaustionEvents exhausted := by
  have h : Runnable UpdaterFormation.primary final exhaustionEvents := by decide
  have hh : run UpdaterFormation.primary final exhaustionEvents = exhausted := by decide
  rw [← hh]
  exact runnable_trace h

theorem coarse_continuation_blocked_by_spent_parts :
    UpdaterFormation.Enabled UpdaterFormation.primary exhausted.core (.formSelector false) ∧
    0 < exhausted.core.core.fuel ∧ 0 < exhausted.core.core.packets ∧
    ¬ ∃ t, Step UpdaterFormation.primary exhausted (.formSelector false) t := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  rw [command_lifts_iff]; decide

end ConstructedUpdater

#print axioms ConstructedUpdater.step_projects
#print axioms ConstructedUpdater.trace_projects
#print axioms ConstructedUpdater.command_lifts_iff
#print axioms ConstructedUpdater.step_part_ledgers
#print axioms ConstructedUpdater.trace_part_ledgers
#print axioms ConstructedUpdater.abstract_trace_lifts_with_parts
#print axioms ConstructedUpdater.material_trace_lift_iff
#print axioms ConstructedUpdater.step_preserves_side_stores
#print axioms ConstructedUpdater.trace_preserves_side_stores
#print axioms ConstructedUpdater.trace_preserves_matter
#print axioms ConstructedUpdater.trace_energy_ledger
#print axioms ConstructedUpdater.bridge_projects
#print axioms ConstructedUpdater.bridge_energy_exact
#print axioms ConstructedUpdater.bridge_material_exact
#print axioms ConstructedUpdater.bridge_retains_resident_site
#print axioms ConstructedUpdater.changed_updater_consumes_parts
#print axioms ConstructedUpdater.step_preserves_module_hardware
#print axioms ConstructedUpdater.reachable_active_module_has_new_parts
#print axioms ConstructedUpdater.formation_trace_embeds
#print axioms ConstructedUpdater.operational_trace_embeds
#print axioms ConstructedUpdater.actual_formation_bridge_continuation
#print axioms ConstructedUpdater.joined_energy_ledger
#print axioms ConstructedUpdater.joined_material_ledger
#print axioms ConstructedUpdater.core_material_relabel_trace
#print axioms ConstructedUpdater.cost_decomposes
#print axioms ConstructedUpdater.competing_construction_budgets
#print axioms ConstructedUpdater.finite_stock_bounds_updater_formations
#print axioms ConstructedUpdater.actual_part_preparation
#print axioms ConstructedUpdater.actual_typed_bridge
#print axioms ConstructedUpdater.inherited_entrance_exact
#print axioms ConstructedUpdater.runnable_trace
#print axioms ConstructedUpdater.actual_updater_revision
#print axioms ConstructedUpdater.full_formation_to_updater_revision
#print axioms ConstructedUpdater.whole_witness_accounting
#print axioms ConstructedUpdater.old_two_material_bridge_is_insufficient
#print axioms ConstructedUpdater.fuel_does_not_substitute_for_parts
#print axioms ConstructedUpdater.parts_do_not_substitute_for_fuel
#print axioms ConstructedUpdater.actual_post_revision_exhaustion
#print axioms ConstructedUpdater.coarse_continuation_blocked_by_spent_parts
