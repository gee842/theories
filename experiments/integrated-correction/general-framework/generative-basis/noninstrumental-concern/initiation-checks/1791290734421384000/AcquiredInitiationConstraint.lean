import AcquiredActivityScope

/-!
# Acquired consequences constrain a new initiation

Actual formation and completion occurrences supply channel evidence. The local
rule protecting a specified existing continuation, the transfer family and the
reaction/contact laws remain supplied. Non-initiation is not a promise of later
initiation or a universal ethical priority. Products are never reset for trials.
-/
namespace Generative.AcquiredInitiationConstraint
open AcquiredPurposeCriterion
set_option maxHeartbeats 4000000
set_option maxRecDepth 65536

structure Config where
  formMode : Nat := 0
  finishMode : Nat := 0
  clamp : Bool := false
  deriving DecidableEq, Repr

structure State where
  parent : AcquiredActivityScope.State
  parts : Nat := 0
  trialA : Nat := 0
  newB : Nat := 0
  targetA : Nat := 0
  phase : Nat := 0
  binding : Nat := 0
  pending : Nat := 0
  observed : Nat := 0
  formFamily : Nat := 7
  finishFamily : Nat := 7
  recordB : Nat := 0
  selected : Nat := 0
  pc : Nat := 0
  commonSpent : Nat := 0
  totalSpent : Nat := 0
  deriving DecidableEq, Repr

def plant (s : State) : FormedSelection.State := s.parent.core.plant

def occupied (s : State) : Nat := AcquiredActivityScope.occupied s.parent +
  2 * (s.parts + AcquiredActivityScope.held s.trialA +
    AcquiredActivityScope.held s.newB + AcquiredActivityScope.held s.targetA)

def nativeEnabled (s : State) (e : FormedSelection.Event) : Bool :=
  decide (FormedSelection.Enabled (78 - occupied s) (plant s) e)

def valid (s : State) : Bool :=
  AcquiredActivityScope.valid s.parent && s.parts ≤ 3 &&
    s.trialA < 5 && s.newB < 5 && s.targetA < 5 &&
    FormedSelection.population (plant s) + occupied s ≤ 78 &&
    s.phase < 5 && s.binding < 3 && s.pending < 8 && s.observed < 8 &&
    s.formFamily < 8 && s.finishFamily < 8 && s.recordB < 6

def plantUpdate (s : State) (p : FormedSelection.State) : State :=
  { s with
    parent := {s.parent with core := {s.parent.core with plant := p}},
    commonSpent := s.commonSpent + (plant s).fuel - p.fuel,
    totalSpent := s.totalSpent + FormedSelection.energy (plant s) - FormedSelection.energy p }

def charge (s : State) : State := plantUpdate s {(plant s) with fuel := (plant s).fuel - 1}

def spendChannel (s : Support) (mask : Nat) : Option Support :=
  match mask with
  | 1 => if 0 < s.common then some {s with common := s.common - 1} else none
  | 2 => if 0 < s.localStore then some {s with localStore := s.localStore - 1} else none
  | 4 => if 0 < s.source then some {s with source := s.source - 1} else none
  | _ => none

def identified (mask : Nat) : Bool := mask == 1 || mask == 2 || mask == 4

def selection (s : State) (cfg : Config) : Nat :=
  if s.recordB != 3 then 3
  else if cfg.clamp || !identified s.formFamily || !identified s.finishFamily then 2
  else
    let q := support (plant s)
    let jointly := (spendChannel q s.formFamily).bind (fun r => spendChannel r s.finishFamily)
    if jointly.isSome then 2 else if (spendChannel q s.finishFamily).isSome then 1 else 0

inductive Event where
  | plant (e : FormedSelection.Event)
  | assemble | formTrialA | formNewB | formTargetA | finishOldB
  | primeTrialA | finishTrialA | primeTargetA | finishTargetA
  | primeNewB | finishNewB | dissociateNewB
  | armForm | armFinish | observe | commit | contactNewB | select | act
  deriving DecidableEq, Repr

def plan : Nat → List Event
  | 1 => [.finishNewB]
  | 2 => [.formTargetA, .finishNewB]
  | 3 => [.formTargetA]
  | _ => []

def primitiveEnabled (s : State) (e : Event) : Bool :=
  let p := plant s
  match e with
  | .plant event => nativeEnabled s event
  | .assemble => s.parts < 3 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel && s.trialA == 0
  | e => s.parts == 3 && match e with
      | .formTrialA => s.trialA == 0 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel
      | .formNewB => s.newB == 0 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel
      | .formTargetA => s.targetA == 0 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel
      | .finishOldB => s.parent.b == 2 && 0 < p.fuel
      | .primeTrialA => s.trialA == 1 && p.localFuel
      | .finishTrialA => s.trialA == 2 && p.localFuel
      | .primeTargetA => s.targetA == 1 && p.localFuel
      | .finishTargetA => s.targetA == 2 && p.localFuel
      | .primeNewB => s.newB == 1 && 0 < p.fuel
      | .finishNewB => s.newB == 2 && 0 < p.fuel
      | .dissociateNewB => (s.newB == 1 || s.newB == 2) && 0 < p.fuel
      | .armForm => 0 < p.fuel && (s.phase == 0 || s.phase == 4) && s.trialA == 0
      | .armFinish => 0 < p.fuel && (s.phase == 0 || s.phase == 4) && s.parent.b == 2
      | .observe => 0 < p.fuel && s.phase == 2
      | .commit => 0 < p.fuel && s.phase == 3
      | .contactNewB | .select => 0 < p.fuel
      | _ => false

def enabled (s : State) (_cfg : Config) (e : Event) : Bool :=
  valid s && match e with
  | .act => match (plan s.selected)[s.pc]? with
      | some event => primitiveEnabled s event
      | none => false
  | event => primitiveEnabled s event

def physical : Event → Bool
  | .plant _ | .formTrialA | .formNewB | .formTargetA | .finishOldB
  | .primeTrialA | .finishTrialA | .primeTargetA | .finishTargetA
  | .primeNewB | .finishNewB | .dissociateNewB => true
  | _ => false

def physicalStep (s : State) (cfg : Config) (e : Event) : State :=
  match e with
  | .plant event => plantUpdate s (FormedSelection.advance (plant s) event)
  | .primeTrialA => {plantUpdate s {(plant s) with intact := false, localFuel := false} with trialA := 2}
  | .finishTrialA => {plantUpdate s {(plant s) with intact := false, localFuel := false} with trialA := 3}
  | .primeTargetA => {plantUpdate s {(plant s) with intact := false, localFuel := false} with targetA := 2}
  | .finishTargetA => {plantUpdate s {(plant s) with intact := false, localFuel := false} with targetA := 3}
  | e =>
    let t := charge s
    match e with
    | .assemble => {plantUpdate t {(plant t) with aFree := (plant t).aFree - 1, hFree := (plant t).hFree - 1}
        with parts := t.parts + 1}
    | .formTrialA => {plantUpdate t {(plant t) with aFree := (plant t).aFree - 1, hFree := (plant t).hFree - 1}
        with trialA := 1}
    | .formNewB => {plantUpdate t {(plant t) with aFree := (plant t).aFree - 1, hFree := (plant t).hFree - 1}
        with newB := 1}
    | .formTargetA => {plantUpdate t {(plant t) with aFree := (plant t).aFree - 1, hFree := (plant t).hFree - 1}
        with targetA := 1}
    | .finishOldB => {t with parent := {t.parent with b := 3}}
    | .primeNewB => {t with newB := 2}
    | .finishNewB => {t with newB := 3}
    | .dissociateNewB => {plantUpdate t {(plant t) with aFree := (plant t).aFree + 1, hFree := (plant t).hFree + 1}
        with newB := 4}
    | .armForm => {t with phase := 1, binding := 1, pending := 0, observed := 0}
    | .armFinish => {t with phase := 1, binding := 2, pending := 0, observed := 0}
    | .observe =>
        let mode := if t.binding == 1 then cfg.formMode else cfg.finishMode
        {t with phase := 3, observed := if mode == 0 then t.pending else if mode == 1 then 0 else 4}
    | .commit =>
        if t.binding == 1 then {t with phase := 4, formFamily :=
          if t.observed == 0 then t.formFamily else Nat.land t.formFamily t.observed}
        else {t with phase := 4, finishFamily :=
          if t.observed == 0 then t.finishFamily else Nat.land t.finishFamily t.observed}
    | .contactNewB => {t with recordB := t.newB + 1}
    | .select => {t with selected := selection t cfg, pc := 0}
    | _ => t

/-- A receipt belongs to this very bound physical occurrence. -/
def primitiveStep (s : State) (cfg : Config) (e : Event) : State :=
  let t := physicalStep s cfg e
  if s.phase == 1 && physical e then
    let matching := e == (if s.binding == 1 then Event.formTrialA else Event.finishOldB)
    {t with
      phase := if matching then 2 else 0,
      pending := if matching then AcquiredPurposeCriterion.Native.emission (plant s) (plant t) else 0,
      binding := if matching then s.binding else 0}
  else t

def advance (s : State) (cfg : Config) (e : Event) : State :=
  match e with
  | .act => match (plan s.selected)[s.pc]? with
      | some event => {primitiveStep s cfg event with pc := s.pc + 1}
      | none => s
  | event => primitiveStep s cfg event

def process (cfg : Config) : Generative.Process State Event where
  step s e t := enabled s cfg e = true ∧ t = advance s cfg e

def run (cfg : Config) : State → List Event → State
  | s, [] => s
  | s, e :: es => run cfg (advance s cfg e) es

def admitted (cfg : Config) : State → List Event → Bool
  | _, [] => true
  | s, e :: es => enabled s cfg e && admitted cfg (advance s cfg e) es

def vector (s : State) : List Nat := AcquiredActivityScope.vector s.parent ++
  [s.parts, s.trialA, s.newB, s.targetA, s.phase, s.binding, s.pending, s.observed,
   s.formFamily, s.finishFamily, s.recordB, s.selected, s.pc, s.commonSpent, s.totalSpent]

def vectors (cfg : Config) : State → List Event → List (List Nat)
  | s, [] => [vector s]
  | s, e :: es => vector s :: vectors cfg (advance s cfg e) es

def inheritedWord : List AcquiredActivityScope.Event := AcquiredActivityScope.formationWord ++
  [.plant .repair, .plant .capture, .finishA]
def initial : State := {parent := AcquiredActivityScope.run {} AcquiredActivityScope.initial inheritedWord}

theorem inherited_scope_is_actual :
    Generative.Trace (AcquiredActivityScope.process {}) AcquiredActivityScope.initial inheritedWord initial.parent ∧
    initial.parent.a = 3 ∧ initial.parent.b = 2 ∧ (plant initial).fuel = 264 := by
  exact ⟨AcquiredActivityScope.admitted_is_actual_trace _ _ _ (by decide), by decide⟩

theorem admitted_is_actual_trace (cfg : Config) (s : State) (events : List Event)
    (h : admitted cfg s events = true) :
    Generative.Trace (process cfg) s events (run cfg s events) := by
  induction events generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    have hh : enabled s cfg e = true ∧ admitted cfg (advance s cfg e) es = true := by
      simpa only [admitted, Bool.and_eq_true] using h
    exact .cons ⟨hh.1, rfl⟩ (ih _ hh.2)

/-- Once the two actual common-channel debits have been acquired, the new
start is selected jointly with B exactly at the two-unit reserve boundary.
The local non-foreclosure rule itself is not learned by this theorem. -/
theorem learned_joint_reserve_exact {s : State} {cfg : Config}
    (hr : s.recordB = 3) (ha : s.formFamily = 1) (hb : s.finishFamily = 1)
    (hc : cfg.clamp = false) : selection s cfg = 2 ↔ 2 ≤ (plant s).fuel := by
  cases hf : (plant s).fuel with
  | zero => simp [selection, identified, spendChannel, support, hr, ha, hb, hc, hf]
  | succ n =>
    cases n with
    | zero => simp [selection, identified, spendChannel, support, hr, ha, hb, hc, hf]
    | succ n => simp [selection, identified, spendChannel, support, hr, ha, hb, hc, hf]

/-- Instrumenting a bound event changes its record, not its actual plant or
activity phases. These equalities do not pretend observation is free. -/
theorem instrumentation_preserves_effect (s : State) (cfg : Config) (e : Event) :
    plant (primitiveStep s cfg e) = plant (physicalStep s cfg e) ∧
    (primitiveStep s cfg e).newB = (physicalStep s cfg e).newB ∧
    (primitiveStep s cfg e).targetA = (physicalStep s cfg e).targetA := by
  simp only [primitiveStep]
  split <;> exact ⟨rfl, rfl, rfl⟩

/-- Explicit native steps retain the original law at the material capacity
left after all old and new products, activities and recorders are counted. -/
theorem admitted_native_is_original {s t : State} {cfg : Config} {e : FormedSelection.Event}
    (h : (process cfg).step s (.plant e) t) :
    FormedSelection.Step (78 - occupied s) (plant s) e (plant t) := by
  rcases h with ⟨he, rfl⟩
  have hg : valid s = true ∧ nativeEnabled s e = true := Bool.and_eq_true_iff.mp he
  have hv : FormedSelection.population (plant s) + occupied s ≤ 78 := by
    have hh := hg.1
    simp only [valid, Bool.and_eq_true, decide_eq_true_eq] at hh
    omega
  have hn : FormedSelection.Enabled (78 - occupied s) (plant s) e := by
    simpa only [nativeEnabled, decide_eq_true_eq] using hg.2
  refine ⟨by unfold FormedSelection.Valid; omega, hn, ?_⟩
  exact (instrumentation_preserves_effect s cfg (.plant e)).1

theorem primitive_zero_common_retains_B (s : State) (cfg : Config) (e : Event)
    (h : primitiveEnabled s e = true) (hf : (plant s).fuel = 0) (hb : s.newB = 2) :
    (plant (primitiveStep s cfg e)).fuel = 0 ∧ (primitiveStep s cfg e).newB = 2 := by
  rw [(instrumentation_preserves_effect s cfg e).1,
    (instrumentation_preserves_effect s cfg e).2.1]
  cases e with
  | plant event =>
    cases event <;> simp_all [physicalStep, plantUpdate, plant, FormedSelection.advance]
  | _ =>
    simp_all [primitiveEnabled, physicalStep, plantUpdate, plant]
    all_goals repeat (first | split | simp_all)

theorem step_zero_common_retains_B {s t : State} {cfg : Config} {e : Event}
    (h : (process cfg).step s e t) (hf : (plant s).fuel = 0) (hb : s.newB = 2) :
    (plant t).fuel = 0 ∧ t.newB = 2 := by
  rcases h with ⟨he, rfl⟩
  cases e with
  | act =>
    have hh := (Bool.and_eq_true_iff.mp he).2
    cases hw : (plan s.selected)[s.pc]? with
    | none =>
      change (match (plan s.selected)[s.pc]? with | some q => primitiveEnabled s q | none => false) = true at hh
      rw [hw] at hh
      cases hh
    | some event =>
      have hp : primitiveEnabled s event = true := by
        change (match (plan s.selected)[s.pc]? with | some q => primitiveEnabled s q | none => false) = true at hh
        simpa only [hw] using hh
      simpa only [advance, hw, plant] using primitive_zero_common_retains_B s cfg event hp hf hb
  | _ =>
    exact primitive_zero_common_retains_B _ _ _ (Bool.and_eq_true_iff.mp he).2 hf hb

theorem depleted_common_blocks_every_B_completion {s t : State} {cfg : Config} {events : List Event}
    (h : Generative.Trace (process cfg) s events t)
    (hf : (plant s).fuel = 0) (hb : s.newB = 2) :
    (plant t).fuel = 0 ∧ t.newB = 2 := by
  induction h with
  | nil s => exact ⟨hf, hb⟩
  | cons hs _ ih =>
    have hh := step_zero_common_retains_B hs hf hb
    exact ih hh.1 hh.2

/-- At the actual one-unit boundary, a new material formation can remove
an existing completion. This is a fact about two full continuations, not a
preinstalled success bit or a universal priority ordering. -/
theorem one_unit_start_forecloses_B {s : State} {cfg : Config}
    (hf : (plant s).fuel = 1) (hb : s.newB = 2)
    (hStart : enabled s cfg .formTargetA = true)
    (hFinish : enabled s cfg .finishNewB = true) :
    (∃ t, Generative.Trace (process cfg) s [.finishNewB] t ∧ t.newB = 3) ∧
    Generative.Trace (process cfg) s [.formTargetA] (advance s cfg .formTargetA) ∧
    (∀ events t, Generative.Trace (process cfg) (advance s cfg .formTargetA) events t → t.newB = 2) := by
  refine ⟨⟨_, .cons ⟨hFinish, rfl⟩ (.nil _), ?_⟩,
    .cons ⟨hStart, rfl⟩ (.nil _), ?_⟩
  · change (primitiveStep s cfg .finishNewB).newB = 3
    rw [(instrumentation_preserves_effect s cfg .finishNewB).2.1]
    rfl
  · intro events t ht
    have hzero : (plant (advance s cfg .formTargetA)).fuel = 0 := by
      change (plant (primitiveStep s cfg .formTargetA)).fuel = 0
      rw [(instrumentation_preserves_effect s cfg .formTargetA).1]
      change (plant s).fuel - 1 = 0
      simp only [hf, Nat.sub_self]
    have hstill : (advance s cfg .formTargetA).newB = 2 := by
      change (primitiveStep s cfg .formTargetA).newB = 2
      rw [(instrumentation_preserves_effect s cfg .formTargetA).2.1]
      exact hb
    exact (depleted_common_blocks_every_B_completion ht hzero hstill).2

/-- The supposedly ample control can start a new coupling and finish B,
yet leave that new coupling unable even to begin its first reaction. -/
theorem primitive_depletion_blocks_new_A (s : State) (cfg : Config) (e : Event)
    (h : primitiveEnabled s e = true) (hf : (plant s).fuel = 0)
    (hi : (plant s).intact = false) (hl : (plant s).localFuel = false) (ha : s.targetA = 1) :
    (plant (primitiveStep s cfg e)).fuel = 0 ∧
    (plant (primitiveStep s cfg e)).intact = false ∧
    (plant (primitiveStep s cfg e)).localFuel = false ∧ (primitiveStep s cfg e).targetA = 1 := by
  rw [(instrumentation_preserves_effect s cfg e).1,
    (instrumentation_preserves_effect s cfg e).2.2]
  cases e with
  | plant event =>
    cases event <;> simp_all [primitiveEnabled, nativeEnabled, FormedSelection.Enabled,
      physicalStep, plantUpdate, plant, FormedSelection.advance]
  | _ =>
    simp_all [primitiveEnabled, plant]

theorem step_depletion_blocks_new_A {s t : State} {cfg : Config} {e : Event}
    (h : (process cfg).step s e t) (hf : (plant s).fuel = 0)
    (hi : (plant s).intact = false) (hl : (plant s).localFuel = false) (ha : s.targetA = 1) :
    (plant t).fuel = 0 ∧ (plant t).intact = false ∧ (plant t).localFuel = false ∧ t.targetA = 1 := by
  rcases h with ⟨he, rfl⟩
  cases e with
  | act =>
    have hh := (Bool.and_eq_true_iff.mp he).2
    cases hw : (plan s.selected)[s.pc]? with
    | none =>
      change (match (plan s.selected)[s.pc]? with | some q => primitiveEnabled s q | none => false) = true at hh
      rw [hw] at hh
      cases hh
    | some event =>
      have hp : primitiveEnabled s event = true := by
        change (match (plan s.selected)[s.pc]? with | some q => primitiveEnabled s q | none => false) = true at hh
        simpa only [hw] using hh
      simpa only [advance, hw, plant] using primitive_depletion_blocks_new_A s cfg event hp hf hi hl ha
  | _ =>
    exact primitive_depletion_blocks_new_A _ _ _ (Bool.and_eq_true_iff.mp he).2 hf hi hl ha

theorem depletion_blocks_every_new_A_continuation {s t : State} {cfg : Config} {events : List Event}
    (h : Generative.Trace (process cfg) s events t) (hf : (plant s).fuel = 0)
    (hi : (plant s).intact = false) (hl : (plant s).localFuel = false) (ha : s.targetA = 1) :
    (plant t).fuel = 0 ∧ (plant t).intact = false ∧ (plant t).localFuel = false ∧ t.targetA = 1 := by
  induction h with
  | nil s => exact ⟨hf, hi, hl, ha⟩
  | cons hs _ ih =>
    have hh := step_depletion_blocks_new_A hs hf hi hl ha
    exact ih hh.1 hh.2.1 hh.2.2.1 hh.2.2.2

def training : List Event := List.replicate 3 .assemble ++
  [.armForm, .formTrialA, .observe, .commit, .armFinish, .finishOldB, .observe, .commit,
   .plant .repair, .plant .capture, .primeTrialA, .plant .repair, .plant .capture, .finishTrialA,
   .formNewB, .primeNewB, .contactNewB]
def trained : State := run {} initial training

theorem actual_training_acquires_costs_and_retains_products :
    Generative.Trace (process {}) initial training trained ∧
    trained.formFamily = 1 ∧ trained.finishFamily = 1 ∧ trained.recordB = 3 ∧
    trained.parent.a = 3 ∧ trained.parent.b = 3 ∧ trained.trialA = 3 ∧
    trained.newB = 2 ∧ trained.targetA = 0 ∧ (plant trained).fuel = 248 := by
  exact ⟨admitted_is_actual_trace _ _ _ (by decide), by decide⟩

end Generative.AcquiredInitiationConstraint

#print axioms Generative.AcquiredInitiationConstraint.inherited_scope_is_actual
#print axioms Generative.AcquiredInitiationConstraint.admitted_is_actual_trace
#print axioms Generative.AcquiredInitiationConstraint.learned_joint_reserve_exact
#print axioms Generative.AcquiredInitiationConstraint.instrumentation_preserves_effect
#print axioms Generative.AcquiredInitiationConstraint.actual_training_acquires_costs_and_retains_products

#print axioms Generative.AcquiredInitiationConstraint.admitted_native_is_original
#print axioms Generative.AcquiredInitiationConstraint.primitive_zero_common_retains_B
#print axioms Generative.AcquiredInitiationConstraint.step_zero_common_retains_B
#print axioms Generative.AcquiredInitiationConstraint.depleted_common_blocks_every_B_completion

#print axioms Generative.AcquiredInitiationConstraint.primitive_depletion_blocks_new_A
#print axioms Generative.AcquiredInitiationConstraint.step_depletion_blocks_new_A
#print axioms Generative.AcquiredInitiationConstraint.depletion_blocks_every_new_A_continuation

#print axioms Generative.AcquiredInitiationConstraint.one_unit_start_forecloses_B
