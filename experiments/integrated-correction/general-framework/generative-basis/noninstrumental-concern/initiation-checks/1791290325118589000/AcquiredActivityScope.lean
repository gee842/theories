import AcquiredPurposeCriterion

/-!
# Formed material activities and acquired operative scope

The existing physical ancestor and repair-channel acquisition are retained.
The new local coupling law, contact encoding and reader recipe are explicit
inputs. No independent actor/patient or ethical Reason primitive is installed.
Product formation and dissolution both end a local pending reaction, with
different material consequences. Acquired pending scope is not an ethical
obligation and its emptiness is not completion of all historical relations.
-/
namespace Generative.AcquiredActivityScope

structure Config where
  contactMode : Nat := 0
  clamp : Bool := false
  deriving DecidableEq, Repr

structure State where
  core : AcquiredPurposeCriterion.Native.State
  readers : Nat := 0
  a : Nat := 0
  b : Nat := 0
  recordA : Nat := 0
  recordB : Nat := 0
  snapshotA : Nat := 0
  snapshotB : Nat := 0
  lastTarget : Nat := 0
  lastPayload : Nat := 0
  selected : Nat := 0
  pc : Nat := 0
  commonSpent : Nat := 0
  totalSpent : Nat := 0
  deriving DecidableEq, Repr

def held (phase : Nat) : Nat := if phase == 1 || phase == 2 || phase == 3 then 1 else 0

def occupied (s : State) : Nat := 2 * (s.core.parts + s.readers + held s.a + held s.b)

def valid (s : State) : Bool :=
  AcquiredPurposeCriterion.Native.valid s.core && s.readers ≤ 3 && s.a < 5 && s.b < 5 &&
    FormedSelection.population s.core.plant + occupied s ≤ 78 &&
    s.recordA < 6 && s.recordB < 6 && s.snapshotA < 6 && s.snapshotB < 6

def nativeEnabled (s : State) (e : FormedSelection.Event) : Bool :=
  decide (FormedSelection.Enabled (78 - occupied s) s.core.plant e)

def plantUpdate (s : State) (p : FormedSelection.State) : State :=
  { s with
    core := {s.core with plant := p},
    commonSpent := s.commonSpent + s.core.plant.fuel - p.fuel,
    totalSpent := s.totalSpent + FormedSelection.energy s.core.plant - FormedSelection.energy p }

def charge (s : State) : State :=
  plantUpdate s {s.core.plant with fuel := s.core.plant.fuel - 1}

def actualPending (s : State) : List Nat :=
  (if s.a == 1 || s.a == 2 then [1] else []) ++
  (if s.b == 1 || s.b == 2 then [2] else [])

def records (s : State) (cfg : Config) : Nat × Nat :=
  if cfg.clamp then (s.snapshotA, s.snapshotB) else (s.recordA, s.recordB)

def acquiredPending (s : State) (cfg : Config) : List Nat :=
  let (ra, rb) := records s cfg
  (if ra == 2 || ra == 3 then [1] else []) ++
  (if rb == 2 || rb == 3 then [2] else [])

inductive Event where
  | plant (e : FormedSelection.Event)
  | assemble | formA | formB | primeA | primeB | finishA | finishB
  | dissociateA | dissociateB | contactA | contactB | refreshA | select | act
  deriving DecidableEq, Repr

def plan : Nat → List Event
  | 1 => [.plant .repair, .plant .capture, .finishA]
  | 2 => [.plant .capture, .finishA]
  | 3 => [.finishA]
  | 4 => [.finishB]
  | _ => []

def selection (s : State) (cfg : Config) : Nat :=
  let (ra, rb) := records s cfg
  let p := s.core.plant
  if ra == 3 && s.core.candidates == 1 && p.localFuel then 3
  else if ra == 3 && s.core.candidates == 1 && 0 < p.source && p.intact then 2
  else if ra == 3 && s.core.candidates == 1 && 0 < p.source &&
      p.resident == .active && 0 < p.fuel then 1
  else if rb == 3 && 0 < p.fuel then 4 else 0

def primitiveEnabled (s : State) (e : Event) : Bool :=
  let p := s.core.plant
  match e with
  | .plant event => nativeEnabled s event
  | .assemble => s.readers < 3 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel && s.a == 0 && s.b == 0
  | e => s.readers == 3 && match e with
      | .formA => s.a == 0 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel
      | .formB => s.b == 0 && 0 < p.aFree && 0 < p.hFree && 0 < p.fuel
      | .primeA => s.a == 1 && p.localFuel
      | .finishA => s.a == 2 && p.localFuel
      | .primeB => s.b == 1 && 0 < p.fuel
      | .finishB => s.b == 2 && 0 < p.fuel
      | .dissociateA => (s.a == 1 || s.a == 2) && 0 < p.fuel
      | .dissociateB => (s.b == 1 || s.b == 2) && 0 < p.fuel
      | .contactA | .contactB | .refreshA | .select => 0 < p.fuel
      | _ => false

def enabled (s : State) (_cfg : Config) (e : Event) : Bool :=
  valid s && match e with
  | .act => match (plan s.selected)[s.pc]? with
      | some event => primitiveEnabled s event
      | none => false
  | event => primitiveEnabled s event

def primitiveStep (s : State) (cfg : Config) (e : Event) : State :=
  match e with
  | .plant event => plantUpdate s (FormedSelection.advance s.core.plant event)
  | .primeA => {plantUpdate s {s.core.plant with localFuel := false, intact := false} with a := 2}
  | .finishA => {plantUpdate s {s.core.plant with localFuel := false, intact := false} with a := 3}
  | e =>
    let t := charge s
    match e with
    | .assemble => {plantUpdate t {t.core.plant with
        aFree := t.core.plant.aFree - 1, hFree := t.core.plant.hFree - 1} with readers := t.readers + 1}
    | .formA => {plantUpdate t {t.core.plant with
        aFree := t.core.plant.aFree - 1, hFree := t.core.plant.hFree - 1} with a := 1}
    | .formB => {plantUpdate t {t.core.plant with
        aFree := t.core.plant.aFree - 1, hFree := t.core.plant.hFree - 1} with b := 1}
    | .primeB => {t with b := 2}
    | .finishB => {t with b := 3}
    | .dissociateA => {plantUpdate t {t.core.plant with
        aFree := t.core.plant.aFree + 1, hFree := t.core.plant.hFree + 1} with a := 4}
    | .dissociateB => {plantUpdate t {t.core.plant with
        aFree := t.core.plant.aFree + 1, hFree := t.core.plant.hFree + 1} with b := 4}
    | .contactA | .contactB | .refreshA =>
        let isA := e != .contactB
        let phasePayload := (if isA then t.a else t.b) + 1
        let payload := if e == .refreshA then
          if cfg.contactMode == 1 then 0 else
          if cfg.contactMode == 2 then t.snapshotA else
          if cfg.contactMode == 3 then 1 else phasePayload
          else phasePayload
        let u := {t with lastTarget := if isA then 1 else 2, lastPayload := payload}
        if payload == 0 then u else
          if isA then {u with recordA := payload, snapshotA :=
            if payload == 3 && t.snapshotA == 0 then 3 else t.snapshotA}
          else {u with recordB := payload, snapshotB :=
            if payload == 3 && t.snapshotB == 0 then 3 else t.snapshotB}
    | .select => {t with selected := selection t cfg, pc := 0}
    | _ => t

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

def vector (s : State) : List Nat := AcquiredPurposeCriterion.Native.vector s.core ++
  [s.readers, s.a, s.b, s.recordA, s.recordB, s.snapshotA, s.snapshotB,
   s.lastTarget, s.lastPayload, s.selected, s.pc, s.commonSpent, s.totalSpent]

def vectors (cfg : Config) : State → List Event → List (List Nat)
  | s, [] => [vector s]
  | s, e :: es => vector s :: vectors cfg (advance s cfg e) es

def initial : State := {core := AcquiredPurposeCriterion.Native.trained {laterRepair := false}}

theorem inherited_training_is_actual :
    Generative.Trace (AcquiredPurposeCriterion.Native.process {laterRepair := false}) AcquiredPurposeCriterion.Native.initial AcquiredPurposeCriterion.Native.training initial.core ∧
    initial.core.criterionActive = false ∧ initial.core.candidates = 1 := by
  exact ⟨AcquiredPurposeCriterion.Native.admitted_is_actual_trace _ _ _ (by decide), by decide, by decide⟩

theorem admitted_is_actual_trace (cfg : Config) (s : State) (events : List Event)
    (h : admitted cfg s events = true) :
    Generative.Trace (process cfg) s events (run cfg s events) := by
  induction events generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    have hh : enabled s cfg e = true ∧ admitted cfg (advance s cfg e) es = true := by
      simpa only [admitted, Bool.and_eq_true] using h
    exact .cons ⟨hh.1, rfl⟩ (ih _ hh.2)

/-- The old activation bit is not an input to the newly operative selection. -/
theorem legacy_activation_does_not_choose (s : State) (cfg : Config) (value : Bool) :
    selection {s with core := {s.core with criterionActive := value}} cfg = selection s cfg := by
  rfl

/-- Formation has a real continuation cost: the first A reaction leaves the
site damaged and empty, disabling capture as well as direct product formation. -/
theorem priming_changes_actual_continuation {s t : State} {cfg : Config}
    (h : (process cfg).step s .primeA t) :
    t.a = 2 ∧ t.core.plant.intact = false ∧ t.core.plant.localFuel = false ∧
    primitiveEnabled t .finishA = false ∧ nativeEnabled t .capture = false := by
  rcases h with ⟨_, rfl⟩
  simp [advance, primitiveStep, plantUpdate, primitiveEnabled, nativeEnabled,
    FormedSelection.Enabled]

/-- A single ending leaves the other material reaction and its record intact. -/
theorem ending_A_preserves_B (s : State) (cfg : Config) :
    (advance s cfg .finishA).b = s.b ∧
    (advance s cfg .finishA).recordB = s.recordB ∧
    (advance s cfg .dissociateA).b = s.b ∧
    (advance s cfg .dissociateA).recordB = s.recordB := by
  exact ⟨rfl, rfl, rfl, rfl⟩

/-- A native step cannot use material already occupied by readers or activities. -/
theorem admitted_native_is_original {cfg : Config} {s t : State}
    {e : FormedSelection.Event} (h : (process cfg).step s (.plant e) t) :
    FormedSelection.Step (78 - occupied s) s.core.plant e t.core.plant := by
  rcases h with ⟨hguard, rfl⟩
  have hg : valid s = true ∧ nativeEnabled s e = true := by
    simpa only [enabled, primitiveEnabled, Bool.and_eq_true] using hguard
  have hv : FormedSelection.population s.core.plant + occupied s ≤ 78 := by
    have hh := hg.1
    simp only [valid, Bool.and_eq_true, decide_eq_true_eq] at hh
    exact hh.1.1.1.1.2
  have he : FormedSelection.Enabled (78 - occupied s) s.core.plant e := by
    simpa only [nativeEnabled, decide_eq_true_eq] using hg.2
  exact ⟨by unfold FormedSelection.Valid; omega, he, rfl⟩

/-- Existing historical completion records are never rewritten by scope events. -/
theorem primitive_history_preserved (s : State) (cfg : Config) (e : Event) :
    (primitiveStep s cfg e).core.historical = s.core.historical := by
  cases e <;> simp [primitiveStep, charge, plantUpdate]
  all_goals repeat (first | split | simp_all)

/-- Product phases are absorbing only under admitted physical reactions. -/
theorem primitive_products_preserved (s : State) (cfg : Config) (e : Event)
    (h : primitiveEnabled s e = true) :
    (s.a = 3 → (primitiveStep s cfg e).a = 3) ∧
    (s.b = 3 → (primitiveStep s cfg e).b = 3) := by
  constructor <;> intro hp <;> cases e <;>
    simp_all [primitiveEnabled, primitiveStep, charge, plantUpdate]
  all_goals repeat (first | split | simp_all)

/-- Scope changes do not erase acquired products or the earlier completion record. -/
theorem step_preserves_history_and_products {s t : State} {cfg : Config} {e : Event}
    (h : (process cfg).step s e t) :
    t.core.historical = s.core.historical ∧
    (s.a = 3 → t.a = 3) ∧ (s.b = 3 → t.b = 3) := by
  rcases h with ⟨he, rfl⟩
  cases e with
  | act =>
    simp only [enabled, Bool.and_eq_true] at he
    cases hw : (plan s.selected)[s.pc]? with
    | none => simp [hw] at he
    | some event =>
      have hh : primitiveEnabled s event = true := by simpa [hw] using he.2
      simpa only [advance, hw] using
        And.intro (primitive_history_preserved s cfg event) (primitive_products_preserved s cfg event hh)
  | _ =>
    simp only [enabled, Bool.and_eq_true] at he
    exact ⟨primitive_history_preserved _ _ _, primitive_products_preserved _ _ _ he.2⟩

theorem trace_preserves_history_and_products {s t : State} {cfg : Config} {events : List Event}
    (h : Generative.Trace (process cfg) s events t) :
    t.core.historical = s.core.historical ∧
    (s.a = 3 → t.a = 3) ∧ (s.b = 3 → t.b = 3) := by
  induction h with
  | nil s => exact ⟨rfl, id, id⟩
  | cons hs _ ih =>
    have hh := step_preserves_history_and_products hs
    exact ⟨ih.1.trans hh.1, fun h => ih.2.1 (hh.2.1 h), fun h => ih.2.2 (hh.2.2 h)⟩

/-- Depleted common support cannot be restored by any supplied reaction,
and the unfinished B coupling cannot be completed or erased for free. -/
theorem primitive_zero_common_retains_B (s : State) (cfg : Config) (e : Event)
    (h : primitiveEnabled s e = true) (hf : s.core.plant.fuel = 0) (hb : s.b = 2) :
    (primitiveStep s cfg e).core.plant.fuel = 0 ∧ (primitiveStep s cfg e).b = 2 := by
  cases e with
  | plant event =>
    cases event <;> simp [primitiveStep, plantUpdate, FormedSelection.advance, hf, hb]
  | _ =>
    simp_all [primitiveEnabled, primitiveStep, plantUpdate]
    all_goals repeat (first | split | simp_all)

theorem step_zero_common_retains_B {s t : State} {cfg : Config} {e : Event}
    (h : (process cfg).step s e t) (hf : s.core.plant.fuel = 0) (hb : s.b = 2) :
    t.core.plant.fuel = 0 ∧ t.b = 2 := by
  rcases h with ⟨he, rfl⟩
  cases e with
  | act =>
    simp only [enabled, Bool.and_eq_true] at he
    cases hw : (plan s.selected)[s.pc]? with
    | none => simp [hw] at he
    | some event =>
      have hh : primitiveEnabled s event = true := by simpa [hw] using he.2
      simpa only [advance, hw] using primitive_zero_common_retains_B s cfg event hh hf hb
  | _ =>
    simp only [enabled, Bool.and_eq_true] at he
    exact primitive_zero_common_retains_B _ _ _ he.2 hf hb

theorem depleted_common_blocks_every_B_completion {s t : State} {cfg : Config} {events : List Event}
    (h : Generative.Trace (process cfg) s events t)
    (hf : s.core.plant.fuel = 0) (hb : s.b = 2) :
    t.core.plant.fuel = 0 ∧ t.b = 2 := by
  induction h with
  | nil s => exact ⟨hf, hb⟩
  | cons hs _ ih =>
    have hh := step_zero_common_retains_B hs hf hb
    exact ih hh.1 hh.2

/-- Two additional Lean histories retain sufficient support for the final
contact. They are not claimed to be among the nine saved Python fixtures. -/
def formationWord : List Event := List.replicate 3 .assemble ++
  [.contactA, .formA, .primeA, .contactA, .formB, .primeB, .contactB]
def completedWord : List Event := formationWord ++
  [.plant .repair, .plant .capture, .finishA, .refreshA, .select, .act, .contactB]
def dissolvedWord : List Event := formationWord ++
  [.dissociateA, .refreshA, .select, .act, .contactB]
def completed : State := run {} initial completedWord
def dissolved : State := run {} initial dissolvedWord

theorem actual_empty_scope_has_different_products :
    Generative.Trace (process {}) initial completedWord completed ∧
    Generative.Trace (process {}) initial dissolvedWord dissolved ∧
    actualPending completed = [] ∧ acquiredPending completed {} = [] ∧
    actualPending dissolved = [] ∧ acquiredPending dissolved {} = [] ∧
    completed.a = 3 ∧ dissolved.a = 4 ∧ completed.b = 3 ∧ dissolved.b = 3 ∧
    completed.core.historical = 1 ∧ dissolved.core.historical = 1 ∧
    completed.core.plant.intact = false ∧ dissolved.core.plant.intact = false ∧
    dissolved.core.plant.aFree = completed.core.plant.aFree + 1 ∧
    dissolved.core.plant.hFree = completed.core.plant.hFree + 1 := by
  exact ⟨admitted_is_actual_trace _ _ _ (by decide),
    admitted_is_actual_trace _ _ _ (by decide), by decide⟩

end Generative.AcquiredActivityScope

#print axioms Generative.AcquiredActivityScope.inherited_training_is_actual
#print axioms Generative.AcquiredActivityScope.admitted_is_actual_trace
#print axioms Generative.AcquiredActivityScope.legacy_activation_does_not_choose
#print axioms Generative.AcquiredActivityScope.priming_changes_actual_continuation
#print axioms Generative.AcquiredActivityScope.ending_A_preserves_B
#print axioms Generative.AcquiredActivityScope.admitted_native_is_original

#print axioms Generative.AcquiredActivityScope.primitive_history_preserved
#print axioms Generative.AcquiredActivityScope.primitive_products_preserved
#print axioms Generative.AcquiredActivityScope.step_preserves_history_and_products
#print axioms Generative.AcquiredActivityScope.trace_preserves_history_and_products
#print axioms Generative.AcquiredActivityScope.actual_empty_scope_has_different_products

#print axioms Generative.AcquiredActivityScope.primitive_zero_common_retains_B
#print axioms Generative.AcquiredActivityScope.step_zero_common_retains_B
#print axioms Generative.AcquiredActivityScope.depleted_common_blocks_every_B_completion
