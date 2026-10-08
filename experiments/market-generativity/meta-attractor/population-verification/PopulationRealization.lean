import PopulationCorrection
import GenerativeCore

/-! Actual material-guarded generations realizing the population recurrence.
All N slots receive new carrier identities. Contracts are copied except for up
to k revisions, made according to the supplied current-return comparison.
N material parts arrive per generation in the sustained construction. -/
namespace PopulationRealization
open PopulationCorrection

structure Carrier where
  economy : State
  generation : Nat
  parts : Nat
  consumed : Nat
  deriving DecidableEq, Repr

structure Input where
  revisions : Nat
  arrivals : Nat

def roster (N r : Nat) : List Bool := List.replicate r false ++ List.replicate (N-r) true

theorem roster_has_all_slots (N r : Nat) (hr : r ≤ N) : (roster N r).length = N := by
  simp [roster]
  omega

def advance (N fee cap : Nat) (i : Input) (s : Carrier) : Carrier :=
  {economy := next N fee cap i.revisions s.economy,
   generation := s.generation+1, parts := s.parts-N+i.arrivals,
   consumed := s.consumed+N}

def process (N fee cap : Nat) : Generative.Process Carrier Input where
  step s i t := N ≤ s.parts ∧ t = advance N fee cap i s

def lineage (N fee cap : Nat) (k : Nat → Nat) (s : Carrier) : Nat → Carrier
  | 0 => s
  | t+1 => advance N fee cap ⟨k t,N⟩ (lineage N fee cap k s t)

theorem exact_economic_projection (N fee cap : Nat) (k : Nat → Nat) (s : Carrier) (t : Nat) :
    (lineage N fee cap k s t).economy = history N fee cap k s.economy t := by
  induction t with
  | zero => rfl
  | succ t ih => simp [lineage,advance,history,ih]

theorem lineage_accounting (N fee cap : Nat) (k : Nat → Nat) (s : Carrier)
    (hp : N ≤ s.parts) (t : Nat) :
    (lineage N fee cap k s t).parts = s.parts ∧
    (lineage N fee cap k s t).generation = s.generation+t ∧
    (lineage N fee cap k s t).consumed = s.consumed+N*t := by
  induction t with
  | zero => simp [lineage]
  | succ t ih => simp [lineage,advance,ih,Nat.mul_add]; omega

theorem actual_generation (N fee cap : Nat) (k : Nat → Nat) (s : Carrier)
    (hp : N ≤ s.parts) (t : Nat) :
    (process N fee cap).step (lineage N fee cap k s t) ⟨k t,N⟩
      (lineage N fee cap k s (t+1)) := by
  constructor
  · rw [(lineage_accounting N fee cap k s hp t).1]; exact hp
  · rfl

def actions (N : Nat) (k : Nat → Nat) : Nat → List Input
  | 0 => []
  | t+1 => actions N k t ++ [⟨k t,N⟩]

theorem actual_core_history (N fee cap : Nat) (k : Nat → Nat) (s : Carrier)
    (hp : N ≤ s.parts) (t : Nat) :
    Generative.Trace (process N fee cap) s (actions N k t) (lineage N fee cap k s t) := by
  induction t with
  | zero => exact .nil s
  | succ t ih =>
    apply Generative.trace_append_iff.mpr
    exact ⟨_,ih,Generative.trace_singleton_iff.mpr (actual_generation N fee cap k s hp t)⟩

def identity (s : Carrier) (slot : Nat) : Nat × Nat := (s.generation,slot)

theorem distinct_generation_carriers (N fee cap : Nat) (k : Nat → Nat) (s : Carrier)
    (hp : N ≤ s.parts) (t u slot otherSlot : Nat) (h : t < u) :
    identity (lineage N fee cap k s t) slot ≠ identity (lineage N fee cap k s u) otherSlot := by
  intro he
  have hg := congrArg Prod.fst he
  simp only [identity] at hg
  rw [(lineage_accounting N fee cap k s hp t).2.1,
    (lineage_accounting N fee cap k s hp u).2.1] at hg
  omega

theorem missing_parts_disable (N fee cap : Nat) (s : Carrier) (i : Input)
    (hp : s.parts < N) : ¬Generative.Enabled (process N fee cap) s i := by
  rintro ⟨t,ht⟩
  have := ht.1
  omega

theorem no_arrival_consumes_stock (N fee cap k : Nat) (s : Carrier) (hp : N ≤ s.parts) :
    (advance N fee cap ⟨k,0⟩ s).parts + N = s.parts := by
  simp [advance]
  omega

theorem constructive_economy_can_lack_realization :
    let s : Carrier := ⟨⟨6,6,12⟩,0,0,0⟩
    s.economy.reserve = 6 ∧ ¬Generative.Enabled (process 6 6 12) s ⟨1,6⟩ := by
  constructor
  · rfl
  · exact missing_parts_disable _ _ _ _ _ (by decide)

theorem destructive_economy_with_actual_successors :
    let s : Carrier := ⟨exampleStart,0,6,0⟩
    ∀ u, Generative.Enabled (process 6 6 12) (lineage 6 6 12 (fun t => t+1) s (4+u)) ⟨5+u,6⟩ ∧
      (lineage 6 6 12 (fun t => t+1) s (4+u)).economy.capacity = 0 := by
  intro s u
  constructor
  · refine ⟨lineage 6 6 12 (fun t => t+1) s ((4+u)+1), ?_⟩
    have h := actual_generation 6 6 12 (fun t => t+1) s (by decide) (4+u)
    have he : 5+u = 4+u+1 := by omega
    rw [he]
    exact h
  · rw [exact_economic_projection]
    exact (growth_eventually_destructive u).2

end PopulationRealization
