import GenerativeCore
import FormedSelection

/-!
Acquiring a differentiated support requirement from an actual repair occurrence.
The declared candidate family contains single-channel one-unit consumption laws.
The broader maintenance undertaking, channel correspondence and acquiring law
remain supplied. A successful sample cannot exclude an unrepresented fallback.
-/

namespace Generative.AcquiredPurposeCriterion

set_option maxRecDepth 16384
set_option maxHeartbeats 8000000

inductive Channel where
  | common | local | source
  deriving DecidableEq, Repr

structure Support where
  common : Nat
  localStore : Nat
  source : Nat
  deriving DecidableEq, Repr

def support (s : FormedSelection.State) : Support :=
  ⟨s.fuel, FormedSelection.bit s.localFuel, s.source⟩

structure Receipt where
  before : Support
  after : Support
  deriving DecidableEq, Repr

def fits : Channel → Receipt → Bool
  | .common, r => r.after.common + 1 == r.before.common &&
      r.after.localStore == r.before.localStore && r.after.source == r.before.source
  | .local, r => r.after.localStore + 1 == r.before.localStore &&
      r.after.common == r.before.common && r.after.source == r.before.source
  | .source, r => r.after.source + 1 == r.before.source &&
      r.after.common == r.before.common && r.after.localStore == r.before.localStore

def family : List Channel := [.common, .local, .source]
def learn (candidates : List Channel) (r : Receipt) : List Channel :=
  candidates.filter (fun channel => fits channel r)

theorem compatible_candidate_retained {c : Channel} {cs : List Channel} {r : Receipt}
    (hc : c ∈ cs) (hr : fits c r = true) : c ∈ learn cs r := by
  exact List.mem_filter.mpr ⟨hc, hr⟩

/-- The native before/after state, not a desired classification, supplies r. -/
theorem actual_repair_identifies_common {M : Nat} {s t : FormedSelection.State}
    (h : FormedSelection.Step M s .repair t) :
    learn family ⟨support s, support t⟩ = [.common] := by
  rcases h with ⟨_, he, rfl⟩
  have hf : 0 < s.fuel := he.2.2
  cases hcount : s.fuel with
  | zero => simp [hcount] at hf
  | succ n =>
    simp [learn, family, fits, support, FormedSelection.advance, hcount]


/-- A learned channel becomes an operative continuation requirement. This is
relative to the declared single-channel consumption family, not ethical worth. -/
def available (c : Channel) (s : FormedSelection.State) : Bool :=
  match c with
  | .common => 0 < s.fuel
  | .local => s.localFuel
  | .source => 0 < s.source

def criterion (cs : List Channel) (s : FormedSelection.State) : Bool :=
  !cs.isEmpty && cs.all (fun c => available c s)

/-- The previous count-only test remains an identifiable component. Adding a
learned continuation requirement changes the content of present sufficiency;
it does not make an already achieved count historically false. -/
def countComplete (target : Nat) (s : FormedSelection.State) : Bool :=
  target ≤ FormedSelection.aCount s

def complete (target : Nat) (requirements : List Channel)
    (s : FormedSelection.State) : Bool :=
  countComplete target s && requirements.all (fun c => available c s)

theorem count_only_criterion (target : Nat) (s : FormedSelection.State) :
    complete target [] s = countComplete target s := by
  simp [complete]

theorem acquired_requirement_changes_completion_content (target : Nat)
    {s t x : FormedSelection.State} {M : Nat}
    (h : FormedSelection.Step M s .repair t)
    (restored : countComplete target x = true) (depleted : x.fuel = 0) :
    complete target [] x = true ∧
      complete target (learn family ⟨support s, support t⟩) x = false ∧
      countComplete target x = true := by
  rw [actual_repair_identifies_common h]
  simp [complete, available, depleted, restored]

/-- Actual criterion use itself consumes common support in the local extension.
Prospective plan assessment must include that operation's state change. -/
def afterRead (s : FormedSelection.State) : FormedSelection.State :=
  { s with fuel := s.fuel - 1 }

def enoughAfterRead (target : Nat) (requirements : List Channel)
    (s : FormedSelection.State) : Bool :=
  0 < s.fuel && complete target requirements (afterRead s)

theorem acquired_common_requirement_reserves_its_reading
    (target : Nat) (s : FormedSelection.State) :
    enoughAfterRead target [.common] s = true ↔
      countComplete target s = true ∧ 2 ≤ s.fuel := by
  simp [enoughAfterRead, complete, available, afterRead, countComplete,
    FormedSelection.aCount]
  omega

theorem free_reading_would_misclassify_completion
    (target : Nat) {s : FormedSelection.State}
    (hc : countComplete target s = true) (hf : s.fuel = 1) :
    complete target [.common] s = true ∧
      enoughAfterRead target [.common] s = false := by
  simp [complete, available, hc, hf, enoughAfterRead, afterRead]

/-- The acquired result predicts the actual repair resource prerequisite.
Resident and damage conditions are preserved separately, not learned here. -/
theorem learned_criterion_fits_repair {M : Nat} {s t x : FormedSelection.State}
    (h : FormedSelection.Step M s .repair t)
    (active : x.resident = .active) (damaged : x.intact = false) :
    criterion (learn family ⟨support s, support t⟩) x = true ↔
      FormedSelection.Enabled M x .repair := by
  rw [actual_repair_identifies_common h]
  simp [criterion, available, FormedSelection.Enabled, active, damaged]

/-- A substantive outside-family rival: it agrees on every observed repair
with positive common support but has a source-funded fallback when common is 0.
The supplied native law excludes it; the acquired success alone does not. -/
def fallbackRepair (s : FormedSelection.State) : FormedSelection.State :=
  if 0 < s.fuel then FormedSelection.advance s .repair
  else { s with intact := true, source := s.source - 1 }

theorem successful_repair_does_not_exclude_fallback
    {M : Nat} {s t : FormedSelection.State} (h : FormedSelection.Step M s .repair t) :
    fallbackRepair s = t := by
  rcases h with ⟨_, he, rfl⟩
  simp [fallbackRepair, he.2.2]

def outsideFamilyState : FormedSelection.State := ⟨1, 1, .active, false, false, 0, 1⟩

theorem fallback_has_a_genuinely_different_continuation :
    ¬ FormedSelection.Enabled 4 outsideFamilyState .repair ∧
    (fallbackRepair outsideFamilyState).intact = true ∧
    (fallbackRepair outsideFamilyState).source = 0 := by decide

namespace Native

structure Config where
  receiptMode : Nat := 0
  clamp : Bool := false
  laterRepair : Bool := true
  forceBulk : Bool := false
  deriving DecidableEq, Repr

structure State where
  plant : FormedSelection.State
  parts : Nat := 0
  targetA : Nat := 0
  episode : Nat := 0
  historical : Nat := 0
  closed : Bool := false
  finished : Bool := false
  blockedSeen : Bool := false
  restoredSeen : Bool := false
  phase : Nat := 0
  pending : Nat := 0
  observed : Nat := 0
  candidates : Nat := 7
  criterionActive : Bool := false
  selected : Nat := 0
  commonSpent : Nat := 0
  totalSpent : Nat := 0
  deriving DecidableEq, Repr

def valid (s : State) : Bool :=
  s.parts ≤ 9 && FormedSelection.population s.plant + 2 * s.parts ≤ 78

def nativeEnabled (s : State) (e : FormedSelection.Event) : Bool :=
  decide (FormedSelection.Enabled (78 - 2 * s.parts) s.plant e)

def emission (before after : FormedSelection.State) : Nat :=
  let r : Receipt := ⟨support before, support after⟩
  (if fits .common r then 1 else 0) +
    (if fits .local r then 2 else 0) + (if fits .source r then 4 else 0)

def charge (s : State) : State :=
  { s with
    plant := afterRead s.plant
    commonSpent := s.commonSpent + 1
    totalSpent := s.totalSpent + 1 }

def nativeStep (s : State) (e : FormedSelection.Event) : State :=
  let p := FormedSelection.advance s.plant e
  let t := { s with
    plant := p
    commonSpent := s.commonSpent + s.plant.fuel - p.fuel
    totalSpent := s.totalSpent + FormedSelection.energy s.plant - FormedSelection.energy p }
  if s.phase == 1 then
    if e == .repair then { t with phase := 2, pending := emission s.plant p }
    else { t with phase := 0, pending := 0 }
  else t

def operative (s : State) (cfg : Config) : Bool := s.criterionActive && !cfg.clamp

def channelMet (s : State) (cfg : Config) (p : FormedSelection.State) : Bool :=
  if !operative s cfg then true else
    (s.candidates == 1 && 0 < p.fuel) ||
    (s.candidates == 2 && p.localFuel) ||
    (s.candidates == 4 && 0 < p.source)

/-- Closing commits a further, actually charged finish operation. -/
def completion (s : State) (cfg : Config) : Bool :=
  0 < s.plant.fuel && countComplete s.targetA s.plant &&
    channelMet s cfg (afterRead s.plant)

/-- One unit for the judgment, one for its actual finish operation, and one
for the learned repair channel. The bare two-unit read lemma is insufficient
for this longer native continuation. -/
theorem native_judgment_and_finish_reserve_three {s : State} {cfg : Config}
    (ha : s.criterionActive = true) (hc : s.candidates = 1) (hr : cfg.clamp = false) :
    completion (charge s) cfg = true ↔
      countComplete s.targetA s.plant = true ∧ 3 ≤ s.plant.fuel := by
  simp [completion, charge, afterRead, channelMet, operative, ha, hc, hr,
    countComplete, FormedSelection.aCount]
  omega

def simulatePlan : State → List FormedSelection.Event → Option State
  | s, [] => some s
  | s, e :: es =>
    if nativeEnabled s e then simulatePlan (nativeStep s e) es else none

def planAccepted (s : State) (cfg : Config) (code : Nat)
    (word : List FormedSelection.Event) : Bool :=
  match simulatePlan s word with
  | none => false
  | some t => 0 < t.plant.fuel &&
      ((cfg.forceBulk && code == 1) || (!cfg.forceBulk && completion (charge t) cfg))

def selection (s : State) (cfg : Config) : Nat :=
  if planAccepted s cfg 1 [.bulkCopyA] then 1
  else if planAccepted s cfg 2 [.capture, .localCopyA] then 2 else 0

inductive Event where
  | plant (e : FormedSelection.Event)
  | assemble | bindTask | openEpisode | judge | probeCapture | armRepair
  | observe | commit | compileCriterion | select | judgeAfter | finish
  deriving DecidableEq, Repr

def enabled (s : State) (_cfg : Config) (event : Event) : Bool :=
  valid s && match event with
  | .plant e => nativeEnabled s e
  | .finish => s.closed && !s.finished && 0 < s.plant.fuel
  | .assemble => 0 < s.plant.fuel && s.parts < 9 &&
      0 < s.plant.aFree && 0 < s.plant.hFree && s.episode == 0
  | e => 0 < s.plant.fuel && s.parts == 9 && match e with
      | .bindTask => s.episode == 0
      | .openEpisode => s.episode == 1 && s.phase == 5 && !s.finished
      | .judge | .probeCapture => s.episode == 1 && !s.finished
      | .armRepair => s.blockedSeen && s.phase == 0 && !s.finished
      | .observe => s.phase == 2
      | .commit => s.phase == 3
      | .compileCriterion => s.phase == 4 && s.restoredSeen
      | .select => s.episode == 2 && !s.closed && !s.finished
      | .judgeAfter => s.episode == 2 && !s.finished
      | _ => false

def advance (s : State) (cfg : Config) (event : Event) : State :=
  match event with
  | .plant e => nativeStep s e
  | .finish => { charge s with finished := true }
  | e =>
    let t := charge s
    match e with
    | .assemble => { t with
        plant := { t.plant with aFree := t.plant.aFree - 1, hFree := t.plant.hFree - 1 },
        parts := t.parts + 1 }
    | .bindTask => { t with targetA := FormedSelection.aCount t.plant, episode := 1, closed := false }
    | .openEpisode => { t with episode := 2, closed := false, selected := 0 }
    | .judge | .judgeAfter => { t with
        historical := if countComplete t.targetA t.plant
          then Nat.lor t.historical (if t.episode == 1 then 1 else 2) else t.historical,
        closed := completion t cfg }
    | .probeCapture =>
        if nativeEnabled t .capture then
          let u := nativeStep t .capture
          { u with restoredSeen := u.restoredSeen || u.blockedSeen }
        else { t with blockedSeen := true, closed := false }
    | .armRepair => { t with phase := 1, pending := 0 }
    | .observe => { t with phase := 3, observed :=
        if cfg.receiptMode == 0 then t.pending else if cfg.receiptMode == 1 then 0 else 4 }
    | .commit => { t with phase := 4, candidates :=
        if t.observed == 0 then t.candidates else Nat.land t.candidates t.observed }
    | .compileCriterion => { t with phase := 5, criterionActive :=
        cfg.laterRepair && t.blockedSeen && t.restoredSeen &&
          (t.candidates == 1 || t.candidates == 2 || t.candidates == 4) }
    | .select => { t with selected := selection t cfg }
    | _ => t

def process (cfg : Config) : Generative.Process State Event where
  step s e t := enabled s cfg e = true ∧ t = advance s cfg e

def run (cfg : Config) : State → List Event → State
  | s, [] => s
  | s, e :: es => run cfg (advance s cfg e) es

def admitted (cfg : Config) : State → List Event → Bool
  | _, [] => true
  | s, e :: es => enabled s cfg e && admitted cfg (advance s cfg e) es

theorem admitted_is_actual_trace (cfg : Config) (s : State) (events : List Event)
    (h : admitted cfg s events = true) :
    Generative.Trace (process cfg) s events (run cfg s events) := by
  induction events generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    have hh : enabled s cfg e = true ∧ admitted cfg (advance s cfg e) es = true := by
      simpa only [admitted, Bool.and_eq_true] using h
    exact .cons ⟨hh.1, rfl⟩ (ih _ hh.2)

/-- Coupled emission is generated by the actual admitted native repair. -/
theorem actual_emission_is_common {M : Nat} {s t : FormedSelection.State}
    (h : FormedSelection.Step M s .repair t) : emission s t = 1 := by
  rcases h with ⟨_, he, rfl⟩
  have hf : 0 < s.fuel := he.2.2
  cases hcount : s.fuel with
  | zero => simp [hcount] at hf
  | succ n => simp [emission, fits, support, FormedSelection.advance, hcount]

/-- Every wrapper-native event remains an original material event, with
occupied recording material removed from copying capacity. -/
theorem admitted_native_is_original {cfg : Config} {s t : State}
    {e : FormedSelection.Event} (h : (process cfg).step s (.plant e) t) :
    FormedSelection.Step (78 - 2 * s.parts) s.plant e t.plant := by
  rcases h with ⟨hguard, rfl⟩
  have hv : FormedSelection.population s.plant + 2 * s.parts ≤ 78 := by
    simp only [enabled, valid, Bool.and_eq_true, decide_eq_true_eq] at hguard
    exact hguard.1.2
  have hnative : FormedSelection.Enabled (78 - 2 * s.parts) s.plant e := by
    simp only [enabled, Bool.and_eq_true, nativeEnabled, decide_eq_true_eq] at hguard
    exact hguard.2
  refine ⟨by unfold FormedSelection.Valid; omega, hnative, ?_⟩
  simp only [advance, nativeStep]
  split
  · split <;> rfl
  · rfl

def residentCode : FormedSelection.Resident → Nat
  | .empty => 0 | .active => 1 | .alternative => 2

def vector (s : State) : List Nat :=
  let p := s.plant
  [p.aFree, p.hFree, residentCode p.resident, FormedSelection.bit p.intact,
   FormedSelection.bit p.localFuel, p.fuel, p.source, s.parts, s.targetA,
   s.episode, s.historical, FormedSelection.bit s.closed,
   FormedSelection.bit s.finished, FormedSelection.bit s.blockedSeen,
   FormedSelection.bit s.restoredSeen, s.phase, s.pending, s.observed,
   s.candidates, FormedSelection.bit s.criterionActive, s.selected,
   s.commonSpent, s.totalSpent]

def vectors (cfg : Config) : State → List Event → List (List Nat)
  | s, [] => [vector s]
  | s, e :: es => vector s :: vectors cfg (advance s cfg e) es

def plantProcess (M : Nat) : Generative.Process FormedSelection.State FormedSelection.Event :=
  ⟨FormedSelection.Step M⟩

def plantRun : FormedSelection.State → List FormedSelection.Event → FormedSelection.State
  | s, [] => s
  | s, e :: es => plantRun (FormedSelection.advance s e) es

def plantAdmitted (M : Nat) : FormedSelection.State → List FormedSelection.Event → Bool
  | _, [] => true
  | s, e :: es => decide (FormedSelection.Valid M s ∧ FormedSelection.Enabled M s e) &&
      plantAdmitted M (FormedSelection.advance s e) es

theorem plant_admitted_is_actual_trace (M : Nat) (s : FormedSelection.State)
    (events : List FormedSelection.Event) (h : plantAdmitted M s events = true) :
    Generative.Trace (plantProcess M) s events (plantRun s events) := by
  induction events generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    have hh : (FormedSelection.Valid M s ∧ FormedSelection.Enabled M s e) ∧
        plantAdmitted M (FormedSelection.advance s e) es = true := by
      simpa only [plantAdmitted, Bool.and_eq_true, decide_eq_true_eq] using h
    exact .cons ⟨hh.1.1, hh.1.2, rfl⟩ (ih _ hh.2)

def plantVector (p : FormedSelection.State) : List Nat :=
  [p.aFree, p.hFree, residentCode p.resident, FormedSelection.bit p.intact,
    FormedSelection.bit p.localFuel, p.fuel, p.source]

def plantVectors : FormedSelection.State → List FormedSelection.Event → List (List Nat)
  | s, [] => [plantVector s]
  | s, e :: es => plantVector s :: plantVectors (FormedSelection.advance s e) es

def initial : State := { plant := ⟨38, 39, .active, true, true, 293, 216⟩ }

def training : List Event := List.replicate 9 .assemble ++
  [.plant .leakLocal, .bindTask, .plant .wearFreeA, .plant .bulkCopyA,
   .judge, .plant .damage, .probeCapture, .armRepair, .plant .repair,
   .observe, .commit, .probeCapture, .compileCriterion]

def faithful : Config := {}
def clamped : Config := { clamp := true }
def forced : Config := { forceBulk := true }
def trained (cfg : Config) : State := run cfg initial training

def decisionWord : List Event := training ++ [.plant .leakLocal] ++
  List.replicate 269 (.plant .leakCommon) ++ [.plant .wearFreeA, .openEpisode]

def decision (cfg : Config) : State := run cfg initial decisionWord
def selected (cfg : Config) : State := advance (decision cfg) cfg .select
def restoredLocal : State :=
  run faithful (selected faithful) [.plant .capture, .plant .localCopyA]
def restoredBulk (cfg : Config) : State :=
  advance (selected cfg) cfg (.plant .bulkCopyA)

theorem actual_training_forms_requirement :
    admitted faithful initial training = true ∧
    (trained faithful).candidates = 1 ∧ (trained faithful).criterionActive = true ∧
    (trained faithful).historical = 1 ∧ (trained faithful).blockedSeen = true ∧
    (trained faithful).restoredSeen = true ∧ (trained faithful).plant.fuel = 274 := by decide

theorem matched_consumer_keeps_acquired_checkpoint :
    decision faithful = decision clamped ∧
    (selected faithful).selected = 2 ∧ (selected clamped).selected = 1 ∧
    (selected faithful).plant = (selected clamped).plant ∧
    (selected faithful).candidates = (selected clamped).candidates ∧
    (selected faithful).totalSpent = (selected clamped).totalSpent := by decide

theorem same_restored_state_different_effective_closure :
    restoredBulk clamped = restoredBulk forced ∧
    (advance (restoredBulk clamped) clamped .judgeAfter).closed = true ∧
    (advance (restoredBulk forced) forced .judgeAfter).closed = false ∧
    enabled (advance (restoredBulk clamped) clamped .judgeAfter) clamped .finish = true ∧
    enabled (advance (restoredBulk forced) forced .judgeAfter) forced .finish = false ∧
    (advance (restoredBulk forced) forced .judgeAfter).plant.fuel = 1 ∧
    (advance (restoredBulk forced) forced .judgeAfter).historical = 3 := by decide

def faithfulWord : List Event := decisionWord ++
  [.select, .plant .capture, .plant .localCopyA, .judgeAfter, .finish,
   .plant .damage, .plant .repair]

def clampedWord : List Event := decisionWord ++
  [.select, .plant .bulkCopyA, .judgeAfter, .finish, .plant .damage]

theorem acquired_criterion_has_actual_further_use :
    Generative.Trace (process faithful) initial faithfulWord (run faithful initial faithfulWord) ∧
    (run faithful initial faithfulWord).plant.intact = true ∧
    (run faithful initial faithfulWord).finished = true ∧
    (run faithful initial faithfulWord).historical = 3 ∧
    (run faithful initial faithfulWord).plant.fuel = 0 := by
  exact ⟨admitted_is_actual_trace _ _ _ (by decide), by decide, by decide, by decide, by decide⟩

theorem clamped_criterion_retains_completed_count_but_loses_repair :
    Generative.Trace (process clamped) initial clampedWord (run clamped initial clampedWord) ∧
    (run clamped initial clampedWord).historical = 3 ∧
    (run clamped initial clampedWord).finished = true ∧
    enabled (run clamped initial clampedWord) clamped (.plant .repair) = false := by
  exact ⟨admitted_is_actual_trace _ _ _ (by decide), by decide, by decide, by decide⟩

end Native

end Generative.AcquiredPurposeCriterion

#print axioms Generative.AcquiredPurposeCriterion.compatible_candidate_retained
#print axioms Generative.AcquiredPurposeCriterion.actual_repair_identifies_common
#print axioms Generative.AcquiredPurposeCriterion.count_only_criterion
#print axioms Generative.AcquiredPurposeCriterion.acquired_requirement_changes_completion_content
#print axioms Generative.AcquiredPurposeCriterion.acquired_common_requirement_reserves_its_reading
#print axioms Generative.AcquiredPurposeCriterion.free_reading_would_misclassify_completion
#print axioms Generative.AcquiredPurposeCriterion.learned_criterion_fits_repair
#print axioms Generative.AcquiredPurposeCriterion.successful_repair_does_not_exclude_fallback
#print axioms Generative.AcquiredPurposeCriterion.fallback_has_a_genuinely_different_continuation
#print axioms Generative.AcquiredPurposeCriterion.Native.admitted_is_actual_trace
#print axioms Generative.AcquiredPurposeCriterion.Native.native_judgment_and_finish_reserve_three
#print axioms Generative.AcquiredPurposeCriterion.Native.actual_emission_is_common
#print axioms Generative.AcquiredPurposeCriterion.Native.admitted_native_is_original
#print axioms Generative.AcquiredPurposeCriterion.Native.plant_admitted_is_actual_trace
#print axioms Generative.AcquiredPurposeCriterion.Native.actual_training_forms_requirement
#print axioms Generative.AcquiredPurposeCriterion.Native.matched_consumer_keeps_acquired_checkpoint
#print axioms Generative.AcquiredPurposeCriterion.Native.same_restored_state_different_effective_closure
#print axioms Generative.AcquiredPurposeCriterion.Native.acquired_criterion_has_actual_further_use
#print axioms Generative.AcquiredPurposeCriterion.Native.clamped_criterion_retains_completed_count_but_loses_repair
