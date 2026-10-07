import PurposeCorrection

/-!
# Actual finite support handoff

Supplied local assembly and work laws, under the pre-check SEMANTICS.md.
First/second are formation-order and interface positions within one process,
not independent actors. Products are actually constructed from loose material.
An unsupported attempt is physically admitted and recorded, not forbidden by
a moral guard. A failed attempt is not identified with harm or an obligation.
The target is finite; completion permits ending without a replacement.
-/
namespace SupportHandoff

set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

inductive Port where | first | second
  deriving DecidableEq, Repr

structure State where
  loose : Nat
  fuel : Nat
  first : Bool := false
  second : Bool := false
  work : Bool := false
  firstConnected : Bool := false
  secondConnected : Bool := false
  products : Nat := 0
  failedAttempts : Nat := 0
  deriving DecidableEq, Repr

def bit : Bool → Nat | false => 0 | true => 1
def material (s : State) : Nat :=
  s.loose + bit s.first + bit s.second + bit s.work + s.products

def connected (s : State) : Port → Bool
  | .first => s.work && s.first && s.firstConnected
  | .second => s.work && s.second && s.secondConnected

def canProduce (s : State) (p : Port) : Bool := connected s p && 0 < s.loose

inductive Event where
  | assembleFirst | beginWork | assembleSecond | connectSecond
  | attempt (port : Port)
  | dismantleFirst | dismantleSecond | finishWork
  deriving DecidableEq, Repr

def conditions (quota : Nat) (s : State) : Event → Prop
  | .assembleFirst => s.first = false ∧ 0 < s.loose
  | .beginWork => s.work = false ∧ s.first = true ∧ s.products = 0 ∧ 0 < s.loose
  | .assembleSecond => s.second = false ∧ 0 < s.loose
  | .connectSecond => s.work = true ∧ s.second = true ∧ s.secondConnected = false
  | .attempt _ => s.work = true ∧ s.products < quota
  | .dismantleFirst => s.first = true
  | .dismantleSecond => s.second = true
  | .finishWork => s.work = true ∧ s.products = quota

instance (q : Nat) (s : State) (e : Event) : Decidable (conditions q s e) := by
  cases e <;> unfold conditions <;> infer_instance

def Enabled (quota : Nat) (s : State) (e : Event) : Prop :=
  0 < s.fuel ∧ conditions quota s e

instance (q : Nat) (s : State) (e : Event) : Decidable (Enabled q s e) := by
  unfold Enabled
  infer_instance

def advance (s : State) (e : Event) : State :=
  let t := { s with fuel := s.fuel - 1 }
  match e with
  | .assembleFirst => { t with loose := s.loose - 1, first := true }
  | .beginWork =>
    { t with loose := s.loose - 1, work := true, firstConnected := true }
  | .assembleSecond => { t with loose := s.loose - 1, second := true }
  | .connectSecond => { t with secondConnected := true }
  | .attempt p =>
    if canProduce s p then
      { t with loose := s.loose - 1, products := s.products + 1 }
    else { t with failedAttempts := s.failedAttempts + 1 }
  | .dismantleFirst =>
    { t with loose := s.loose + 1, first := false, firstConnected := false }
  | .dismantleSecond =>
    { t with loose := s.loose + 1, second := false, secondConnected := false }
  | .finishWork =>
    { t with loose := s.loose + 1, work := false,
      firstConnected := false, secondConnected := false }

def process (quota : Nat) : Generative.Process State Event where
  step s e t := Enabled quota s e ∧ t = advance s e

def run : State → List Event → State
  | s, [] => s
  | s, e :: es => run (advance s e) es

def Runnable (quota : Nat) : State → List Event → Prop
  | _, [] => True
  | s, e :: es => Enabled quota s e ∧ Runnable quota (advance s e) es

instance runnableDecidable (q : Nat) (s : State) :
    (es : List Event) → Decidable (Runnable q s es)
  | [] => isTrue True.intro
  | e :: es =>
    letI := runnableDecidable q (advance s e) es
    inferInstanceAs (Decidable (Enabled q s e ∧ Runnable q (advance s e) es))

theorem runnable_trace {q : Nat} {s : State} {es : List Event} (r : Runnable q s es) :
    Generative.Trace (process q) s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons ⟨r.1, rfl⟩ (ih r.2)

theorem step_material {q : Nat} {s t : State} {e : Event}
    (h : (process q).step s e t) : material t = material s := by
  rcases h with ⟨⟨_, he⟩, rfl⟩
  cases e <;> simp only [conditions] at he
  case attempt p =>
    simp only [advance]
    split
    · rename_i hc
      have positive : 0 < s.loose := by
        simpa only [canProduce, Bool.and_eq_true, decide_eq_true_eq] using (Bool.and_eq_true.mp hc).2
      simp only [material]
      omega
    · rfl
  all_goals simp [advance, material, bit, he] <;> omega

theorem step_support {q : Nat} {s t : State} {e : Event}
    (h : (process q).step s e t) : t.fuel + 1 = s.fuel := by
  rcases h with ⟨⟨positive, _⟩, rfl⟩
  cases e <;> simp only [advance]
  case attempt p => split <;> simp only <;> omega
  all_goals simp only <;> omega

theorem trace_material {q : Nat} {s t : State} {es : List Event}
    (h : Generative.Trace (process q) s es t) : material t = material s := by
  induction h with
  | nil => rfl
  | cons step _ ih => exact ih.trans (step_material step)

theorem trace_support {q : Nat} {s t : State} {es : List Event}
    (h : Generative.Trace (process q) s es t) : t.fuel + es.length = s.fuel := by
  induction h with
  | nil => exact Nat.add_zero _
  | cons step _ ih =>
    have balance := step_support step
    simp only [List.length_cons]
    omega

theorem insufficient_support_for_word {q : Nat} {s : State} {es : List Event}
    (low : s.fuel < es.length) : ¬ Generative.Feasible (process q) s es := by
  rintro ⟨t, actual⟩
  have balance := trace_support actual
  omega

/-- Assembly alone does not supply the work connection. -/
theorem disconnected_second_cannot_produce (s : State)
    (disconnected : s.secondConnected = false) : canProduce s .second = false := by
  simp [canProduce, connected, disconnected]

/-- A successful operation changes the material distribution and product count;
completion is not a freely writable pending flag. -/
theorem successful_attempt_constructs_product {q : Nat} {s : State} {p : Port}
    (enabled : Enabled q s (.attempt p)) (available : canProduce s p = true) :
    Generative.Trace (process q) s [.attempt p] (advance s (.attempt p)) ∧
    (advance s (.attempt p)).products = s.products + 1 ∧
    (advance s (.attempt p)).loose + 1 = s.loose ∧
    (advance s (.attempt p)).failedAttempts = s.failedAttempts := by
  refine ⟨.cons ⟨enabled, rfl⟩ (.nil _), ?_⟩
  have positive : 0 < s.loose := by
    have h := (Bool.and_eq_true.mp available).2
    simpa only [decide_eq_true_eq] using h
  simp [advance, available]
  omega

/-- A failed attempt remains an actual event, with a support cost and no product.
No claim that the resulting interruption is an ethical harm is included. -/
theorem unavailable_attempt_is_actual {q : Nat} {s : State} {p : Port}
    (enabled : Enabled q s (.attempt p)) (unavailable : canProduce s p = false) :
    Generative.Trace (process q) s [.attempt p] (advance s (.attempt p)) ∧
    (advance s (.attempt p)).products = s.products ∧
    (advance s (.attempt p)).failedAttempts = s.failedAttempts + 1 ∧
    (advance s (.attempt p)).fuel + 1 = s.fuel := by
  refine ⟨.cons ⟨enabled, rfl⟩ (.nil _), ?_⟩
  have balance := step_support (q := q) (e := .attempt p) ⟨enabled, rfl⟩
  simp [advance, unavailable] at balance ⊢
  exact balance

def initial (fuel : Nat) : State := { loose := 6, fuel := fuel }
def prefix : List Event := [.assembleFirst, .beginWork, .attempt .first]
def prepared := run (initial 14) prefix
def installAndTest : List Event := [.assembleSecond, .connectSecond, .attempt .second]
def tested := run prepared installAndTest
def switched := advance tested .dismantleFirst
def finishing : List Event := [.attempt .second, .finishWork, .dismantleSecond]
def handoffWord := prefix ++ installAndTest ++ [.dismantleFirst] ++ finishing
def handoffFinal := run switched finishing

theorem formation_and_dependency_are_actual :
    Generative.Trace (process 3) (initial 14) prefix prepared ∧
    (initial 14).first = false ∧ (initial 14).second = false ∧
    (initial 14).work = false ∧
    prepared.first = true ∧ prepared.work = true ∧ prepared.second = false ∧
    connected prepared .first = true ∧ prepared.products = 1 ∧
    prepared.failedAttempts = 0 := by
  exact ⟨runnable_trace (by decide), by decide⟩

theorem replacement_is_assembled_connected_and_tested :
    Generative.Trace (process 3) prepared installAndTest tested ∧
    tested.first = true ∧ tested.second = true ∧
    connected tested .first = true ∧ connected tested .second = true ∧
    tested.products = 2 ∧ tested.failedAttempts = 0 ∧
    canProduce (advance prepared .assembleSecond) .second = false := by
  exact ⟨runnable_trace (by decide), by decide⟩

theorem original_support_ends_before_real_completion :
    Generative.Trace (process 3) tested [.dismantleFirst] switched ∧
    switched.first = false ∧ switched.work = true ∧ switched.products = 2 ∧
    connected switched .first = false ∧ connected switched .second = true ∧
    canProduce switched .second = true ∧
    Generative.Trace (process 3) switched finishing handoffFinal ∧
    handoffFinal.products = 3 ∧ handoffFinal.first = false ∧
    handoffFinal.second = false ∧ handoffFinal.work = false ∧
    handoffFinal.failedAttempts = 0 := by
  exact ⟨runnable_trace (by decide), by decide, by decide, by decide, by decide,
    by decide, by decide, by decide, runnable_trace (by decide), by decide⟩

theorem whole_handoff_preserves_material_and_support :
    Generative.Trace (process 3) (initial 14) handoffWord handoffFinal ∧
    material handoffFinal = 6 ∧ handoffFinal.loose = 3 ∧
    handoffWord.length = 10 ∧ handoffFinal.fuel = 4 := by
  exact ⟨runnable_trace (by decide), by decide⟩

def earlyExit : List Event := [.dismantleFirst, .attempt .first]
def interrupted := run prepared earlyExit
def repairWord : List Event :=
  [.assembleSecond, .connectSecond, .attempt .second, .attempt .second,
   .finishWork, .dismantleSecond]
def repaired := run interrupted repairWord

theorem early_exit_reaches_an_actual_failed_attempt :
    Generative.Trace (process 3) prepared earlyExit interrupted ∧
    interrupted.first = false ∧ interrupted.second = false ∧ interrupted.work = true ∧
    interrupted.products = 1 ∧ interrupted.failedAttempts = 1 ∧
    interrupted.loose = 4 ∧ interrupted.fuel = 9 := by
  exact ⟨runnable_trace (by decide), by decide⟩

theorem recovery_can_complete_the_same_activity :
    Generative.Trace (process 3) interrupted repairWord repaired ∧
    repaired.products = 3 ∧ repaired.work = false ∧
    repaired.first = false ∧ repaired.second = false ∧
    repaired.failedAttempts = 1 ∧ material repaired = 6 ∧ repaired.fuel = 3 := by
  exact ⟨runnable_trace (by decide), by decide⟩

def allOriginal : List Event :=
  prefix ++ [.attempt .first, .attempt .first, .finishWork, .dismantleFirst]
def ended := run (initial 7) allOriginal

theorem real_completion_needs_no_replacement :
    Generative.Trace (process 3) (initial 7) allOriginal ended ∧
    ended.products = 3 ∧ ended.first = false ∧ ended.second = false ∧
    ended.work = false ∧ ended.failedAttempts = 0 ∧ material ended = 6 ∧
    ended.loose = 3 ∧ ended.fuel = 0 := by
  exact ⟨runnable_trace (by decide), by decide⟩

/-- The declared handoff word needs more support than the finite original-only
completion. This is not a global shortest-path or obligation theorem. -/
theorem low_support_blocks_handoff_but_not_finite_ending :
    ¬ Generative.Feasible (process 3) (initial 7) handoffWord ∧
    Generative.Trace (process 3) (initial 7) allOriginal ended :=
  ⟨insufficient_support_for_word (by decide), real_completion_needs_no_replacement.1⟩

/-! The following description is an analyst's occurrence record. It adds no
internal recording apparatus and makes no claim about subjective experience. -/
def descriptions (s : State) (es : List Event) : List (Event × (State × State)) :=
  Generative.CoupledOccurrence.replay advance (fun a _ b => (a, b)) s es

theorem runnable_described_trace {q : Nat} {s : State} {es : List Event}
    (r : Runnable q s es) :
    Generative.Trace (Generative.PurposeCorrection.stateOccurrences (process q))
      s (descriptions s es) (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons ⟨⟨r.1, rfl⟩, rfl⟩ (ih r.2)

def past := prefix ++ earlyExit
def firstFailed := (Event.attempt Port.first,
  (advance prepared .dismantleFirst, interrupted))
def NoFailedAttempt (s : State) : Prop := s.failedAttempts = 0

/-- Existing full-occurrence theorem instantiated with a real failed operation
and a real recovery. Later completion does not rewrite that same past. -/
theorem later_recovery_does_not_erase_failed_occurrence :
    Generative.Trace (Generative.PurposeCorrection.stateOccurrences (process 3))
      (initial 14) (descriptions (initial 14) past ++ descriptions interrupted repairWord) repaired ∧
    ¬ Generative.Trace
      (Generative.PurposeCorrection.stateOccurrences
        (Generative.PurposeCorrection.guarded (process 3) NoFailedAttempt))
      (initial 14) (descriptions (initial 14) past ++ descriptions interrupted repairWord) repaired := by
  apply Generative.PurposeCorrection.actual_violation_not_erased
    (occurrence := firstFailed)
    (runnable_described_trace (q := 3) (s := initial 14) (es := past) (by decide))
    (runnable_described_trace (q := 3) (s := interrupted) (es := repairWord) (by decide))
  · decide
  · decide

end SupportHandoff

#print axioms SupportHandoff.runnable_trace
#print axioms SupportHandoff.step_material
#print axioms SupportHandoff.step_support
#print axioms SupportHandoff.trace_material
#print axioms SupportHandoff.trace_support
#print axioms SupportHandoff.insufficient_support_for_word
#print axioms SupportHandoff.disconnected_second_cannot_produce
#print axioms SupportHandoff.successful_attempt_constructs_product
#print axioms SupportHandoff.unavailable_attempt_is_actual
#print axioms SupportHandoff.formation_and_dependency_are_actual
#print axioms SupportHandoff.replacement_is_assembled_connected_and_tested
#print axioms SupportHandoff.original_support_ends_before_real_completion
#print axioms SupportHandoff.whole_handoff_preserves_material_and_support
#print axioms SupportHandoff.early_exit_reaches_an_actual_failed_attempt
#print axioms SupportHandoff.recovery_can_complete_the_same_activity
#print axioms SupportHandoff.real_completion_needs_no_replacement
#print axioms SupportHandoff.low_support_blocks_handoff_but_not_finite_ending
#print axioms SupportHandoff.runnable_described_trace
#print axioms SupportHandoff.later_recovery_does_not_erase_failed_occurrence
