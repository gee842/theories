import GenerativeCore

/-!
# A supplied assembly law with regenerated capacity and distinct retained outputs

An AND-prefix network retains every earlier output tap. Each added stage has a
new input and a causal dependency on the preceding output. This is configured
dependency depth, not minimum computational complexity. Raw intake, assembly,
copying and reconstruction occur within one finite trace. Reconstruction is a
supplied operational law requiring a formed stage; no chemistry is derived.

The result is a family of coherent finite histories, with intake at each stage,
not infinite growth from finite stock. The fixed grammar already admits every
prefixCircuit. No ethical predicate, experience claim or universal invention claim is
defined here. See REGENERATIVE-DIVERSITY-MATH.md for correspondence and genealogy.
-/

namespace RegenerativeDiversity

inductive Circuit where
  | source
  | couple (previous : Circuit)
  deriving DecidableEq

def depth : Circuit → Nat
  | .source => 0
  | .couple previous => depth previous + 1

def evaluate : Circuit → (Nat → Bool) → Bool
  | .source, _ => true
  | .couple previous, input => evaluate previous input && input (depth previous)

def prefixCircuit : Nat → Circuit
  | 0 => .source
  | n + 1 => .couple (prefixCircuit n)

inductive Tap : Circuit → Circuit → Prop where
  | self (c : Circuit) : Tap c c
  | previous {a b : Circuit} : Tap a b → Tap a (.couple b)

theorem prefix_depth (n : Nat) : depth (prefixCircuit n) = n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [prefixCircuit, depth, ih]

theorem prefix_evaluation (n : Nat) (input : Nat → Bool) :
    evaluate (prefixCircuit n) input = true ↔ ∀ k, k < n → input k = true := by
  induction n with
  | zero => simp [prefixCircuit, evaluate]
  | succ n ih =>
    simp only [prefixCircuit, evaluate, prefix_depth, Bool.and_eq_true, ih]
    constructor
    · rintro ⟨h, hn⟩ k hk
      by_cases hkn : k < n
      · exact h k hkn
      · have : k = n := by omega
        subst k
        exact hn
    · intro h
      exact ⟨fun k hk => h k (by omega), h n (by omega)⟩

def cutInput (m : Nat) (k : Nat) : Bool := decide (k < m)

/-- Distinct outputs on the very same input domain, not distinct descriptions. -/
theorem prefix_distinguishable {m n : Nat} (h : m < n) :
    evaluate (prefixCircuit m) (cutInput m) = true ∧
      evaluate (prefixCircuit n) (cutInput m) ≠ true := by
  constructor
  · apply (prefix_evaluation m _).mpr
    intro k hk
    simp [cutInput, hk]
  · intro hn
    have hm := (prefix_evaluation n _).mp hn m h
    simp [cutInput] at hm

/-- Earlier organizations remain wired into the actual extended network. -/
theorem retained_tap {k n : Nat} (h : k ≤ n) : Tap (prefixCircuit k) (prefixCircuit n) := by
  induction n with
  | zero =>
    have : k = 0 := by omega
    subst k
    exact .self _
  | succ n ih =>
    by_cases hkn : k ≤ n
    · exact .previous (ih hkn)
    · have : k = n + 1 := by omega
      subst k
      exact .self _

structure State where
  network : Circuit
  copies : List Circuit
  available : Nat
  received : Nat
  spent : Nat
  ready : Bool
  deriving DecidableEq

inductive Event where
  | intake (amount : Nat)
  | assemble
  | duplicate
  | reconstruct
  deriving DecidableEq

def intakeState (s : State) (amount : Nat) : State :=
  { s with available := s.available + amount, received := s.received + amount }

def assemblyState (s : State) : State :=
  { s with
    network := .couple s.network
    available := s.available - 1
    spent := s.spent + 1
    ready := false }

def duplicateState (s : State) : State :=
  { s with
    copies := s.network :: s.copies
    available := s.available - depth s.network
    spent := s.spent + depth s.network
    ready := false }

def reconstructionState (s : State) : State :=
  { s with available := s.available - 1, spent := s.spent + 1, ready := true }

/-- The Bool parameter selects whether the reconstruction channel is present. -/
inductive Step (regenerative : Bool) : State → Event → State → Prop where
  | intake (s : State) (amount : Nat) :
      Step regenerative s (.intake amount) (intakeState s amount)
  | assemble (s : State) (ready : s.ready = true) (stock : 0 < s.available) :
      Step regenerative s .assemble (assemblyState s)
  | duplicate (s : State) (ready : s.ready = true)
      (formed : 0 < depth s.network) (stock : depth s.network ≤ s.available) :
      Step regenerative s .duplicate (duplicateState s)
  | reconstruct (s : State) (channel : regenerative = true)
      (spentCapacity : s.ready = false) (formed : 0 < depth s.network)
      (stock : 0 < s.available) :
      Step regenerative s .reconstruct (reconstructionState s)

def process (regenerative : Bool) : Generative.Process State Event :=
  ⟨Step regenerative⟩

def Balanced (s : State) : Prop := s.available + s.spent = s.received

theorem step_balance {mode : Bool} {s t : State} {e : Event}
    (h : Step mode s e t) (hb : Balanced s) : Balanced t := by
  cases h <;>
    simp only [Balanced, intakeState, assemblyState, duplicateState,
      reconstructionState] at * <;> omega

theorem trace_balance {mode : Bool} {s t : State} {events : List Event}
    (h : Generative.Trace (process mode) s events t) (hb : Balanced s) :
    Balanced t := by
  induction h with
  | nil => exact hb
  | cons hs _ ih => exact ih (step_balance hs hb)

def growthState (n : Nat) : State :=
  ⟨prefixCircuit n, [], 0, 2 * n, 2 * n, true⟩

def growthCycle : List Event := [.intake 2, .assemble, .reconstruct]

def growthHistory : Nat → List Event
  | 0 => []
  | n + 1 => growthHistory n ++ growthCycle

/-- No stage resets the preceding state or imports an assembled organization. -/
theorem growth_cycle (n : Nat) :
    Generative.Trace (process true) (growthState n) growthCycle
      (growthState (n + 1)) := by
  have hs : Step true (growthState n) (.intake 2)
      (intakeState (growthState n) 2) := .intake _ _
  have ha : Step true (intakeState (growthState n) 2) .assemble
      (assemblyState (intakeState (growthState n) 2)) :=
    .assemble _ rfl (by simp [intakeState, growthState])
  have hr : Step true (assemblyState (intakeState (growthState n) 2)) .reconstruct
      (reconstructionState (assemblyState (intakeState (growthState n) 2))) :=
    .reconstruct _ rfl rfl (by simp [assemblyState, intakeState, growthState, depth])
      (by simp [assemblyState, intakeState, growthState])
  have ht : reconstructionState (assemblyState (intakeState (growthState n) 2)) =
      growthState (n + 1) := by
    simp [reconstructionState, assemblyState, intakeState, growthState, prefixCircuit,
      Nat.mul_add, Nat.add_assoc]
  rw [← ht]
  exact .cons hs (.cons ha (.cons hr (.nil _)))

theorem growth_trace (n : Nat) :
    Generative.Trace (process true) (growthState 0) (growthHistory n)
      (growthState n) := by
  induction n with
  | zero => exact .nil _
  | succ n ih =>
    exact Generative.trace_append_iff.mpr ⟨growthState n, ih, growth_cycle n⟩

/-- One actual network contains the pairwise distinct retained output family. -/
theorem growing_repertoire (n : Nat) :
    (∀ k, k ≤ n → Tap (prefixCircuit k) (growthState n).network) ∧
    (∀ i j, i < j → j ≤ n →
      evaluate (prefixCircuit i) (cutInput i) = true ∧
        evaluate (prefixCircuit j) (cutInput i) ≠ true) ∧
    depth (growthState n).network = n ∧ (growthState n).ready = true ∧
    (growthState n).received = 2 * n ∧ (growthState n).available = 0 := by
  exact ⟨fun _ hk => retained_tap hk,
    fun _ _ hij _ => prefix_distinguishable hij, prefix_depth n, rfl, rfl, rfl⟩

def OneShotBound (s : State) : Prop :=
  depth s.network ≤ 1 ∧ (s.ready = true → depth s.network = 0)

theorem one_shot_step {s t : State} {e : Event} (h : Step false s e t)
    (hb : OneShotBound s) : OneShotBound t := by
  cases h with
  | intake => exact hb
  | assemble hr _ =>
    have hz := hb.2 hr
    simp [OneShotBound, assemblyState, depth, hz]
  | duplicate _ _ _ =>
    exact ⟨hb.1, by simp [duplicateState]⟩
  | reconstruct hc _ _ _ => cases hc

/-- Even unlimited later raw intake cannot repair the missing channel. -/
theorem one_shot_trace {t : State} {events : List Event}
    (h : Generative.Trace (process false) (growthState 0) events t) :
    depth t.network ≤ 1 := by
  have init : OneShotBound (growthState 0) := by
    simp [OneShotBound, growthState, prefixCircuit, depth]
  have general : ∀ {s t : State} {es : List Event},
      Generative.Trace (process false) s es t → OneShotBound s → OneShotBound t := by
    intro s t es ht
    induction ht with
    | nil => exact fun hs => hs
    | cons hs _ ih => exact fun hb => ih (one_shot_step hs hb)
  exact (general h init).1

def copyState (n : Nat) : State :=
  ⟨prefixCircuit 1, List.replicate n (prefixCircuit 1), 0,
    2 * (n + 1), 2 * (n + 1), true⟩

def copyCycle : List Event := [.intake 2, .duplicate, .reconstruct]

def copyHistory : Nat → List Event
  | 0 => []
  | n + 1 => copyHistory n ++ copyCycle

theorem copy_cycle (n : Nat) :
    Generative.Trace (process true) (copyState n) copyCycle (copyState (n + 1)) := by
  have hs : Step true (copyState n) (.intake 2)
      (intakeState (copyState n) 2) := .intake _ _
  have hd : Step true (intakeState (copyState n) 2) .duplicate
      (duplicateState (intakeState (copyState n) 2)) :=
    .duplicate _ rfl (by simp [intakeState, copyState, prefixCircuit, depth])
      (by simp [intakeState, copyState, prefixCircuit, depth])
  have hr : Step true (duplicateState (intakeState (copyState n) 2)) .reconstruct
      (reconstructionState (duplicateState (intakeState (copyState n) 2))) :=
    .reconstruct _ rfl rfl
      (by simp [duplicateState, intakeState, copyState, prefixCircuit, depth])
      (by simp [duplicateState, intakeState, copyState, prefixCircuit, depth])
  have ht : reconstructionState (duplicateState (intakeState (copyState n) 2)) =
      copyState (n + 1) := by
    simp [reconstructionState, duplicateState, intakeState, copyState,
      prefixCircuit, depth, Nat.mul_add, Nat.add_assoc, List.replicate_succ]
  rw [← ht]
  exact .cons hs (.cons hd (.cons hr (.nil _)))

/-- Continued reconstruction and more copies do not require a larger repertoire. -/
theorem copying_without_diversification (n : Nat) :
    Generative.Trace (process true) (growthState 0)
      (growthHistory 1 ++ copyHistory n) (copyState n) ∧
    (copyState n).network = prefixCircuit 1 ∧ (copyState n).copies = List.replicate n (prefixCircuit 1) ∧
    (copyState n).ready = true := by
  have hc : Generative.Trace (process true) (copyState 0) (copyHistory n)
      (copyState n) := by
    induction n with
    | zero => exact .nil _
    | succ n ih =>
      exact Generative.trace_append_iff.mpr ⟨copyState n, ih, copy_cycle n⟩
  exact ⟨Generative.trace_append_iff.mpr ⟨growthState 1, growth_trace 1, hc⟩,
    rfl, rfl, rfl⟩

end RegenerativeDiversity
