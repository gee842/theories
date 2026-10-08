import RecursiveSelectionInheritance

/-!
# Transfer entries generated from actual retained carrier pools

Extends the inherited material history without changing its operational law.
The reconstruction recipe now computes its table from available source-tagged
carriers. Reconfiguration changes an existing arrangement before reproduction;
it uses support and retains all eight carriers. The two possible configurations,
the change operation, source association and maximal faithful reconstruction
remain supplied laws. They are not a molecular origin or a selected recipe.
No source replenishment, moral predicate or guaranteed favorable trend occurs.
-/

namespace GeneratedSelectionRecurrence

open RecursiveSelectionInheritance

def weakCapacity (s : State) : Nat := min (s.weakA / 4) (s.weakH / 4)
def strongCapacity (s : State) : Nat := min (s.strongA / 4) (s.strongH / 4)

/-- Maximal source-associated, faithful reconstruction; no per-cycle input table. -/
def generatedTable (s : State) : Transfer :=
  ⟨weakCapacity s, 0, 0, strongCapacity s⟩

def reconstruct (s : State) : Option State := assemble s (generatedTable s)

/-- Operational formation/erosion of a configuration from existing carriers.
    Scheduling and occurrence of the changes are not probabilistically derived. -/
def reconfigure (s : State) (toStrong toWeak : Nat) : Option State :=
  if 0 < toStrong + toWeak ∧ toStrong ≤ s.weak ∧ toWeak ≤ s.strong ∧
      toStrong + toWeak ≤ s.available then
    some { s with
      available := s.available - (toStrong + toWeak)
      spent := s.spent + toStrong + toWeak
      weak := s.weak - toStrong + toWeak
      strong := s.strong - toWeak + toStrong }
  else none

def cycle (s : State) : Option State := (operate s).bind reconstruct

theorem generated_table_carrier_bounds (s : State) :
    4 * weakCapacity s ≤ s.weakA ∧ 4 * weakCapacity s ≤ s.weakH ∧
    4 * strongCapacity s ≤ s.strongA ∧ 4 * strongCapacity s ≤ s.strongH := by
  unfold weakCapacity strongCapacity
  omega

/-- The recipe's exact capacity, not just feasibility of selected witnesses. -/
theorem generated_table_maximal (s : State) (w g : Nat)
    (wa : 4 * w ≤ s.weakA) (wh : 4 * w ≤ s.weakH)
    (ga : 4 * g ≤ s.strongA) (gh : 4 * g ≤ s.strongH) :
    w ≤ weakCapacity s ∧ g ≤ strongCapacity s := by
  unfold weakCapacity strongCapacity
  omega

/-- Batch reconstruction waits if it cannot support the whole maximal batch.
    This scheduling convention is explicit, not a biological necessity. -/
theorem reconstruct_enabled_iff (s : State) :
    (∃ next, reconstruct s = some next) ↔
      0 < weakCapacity s + strongCapacity s ∧
      weakCapacity s + strongCapacity s ≤ s.available := by
  have bounds := generated_table_carrier_bounds s
  unfold reconstruct assemble generatedTable
  dsimp
  split
  · rename_i h
    constructor
    · intro _; omega
    · intro _; exact ⟨_, rfl⟩
  · rename_i h
    constructor
    · rintro ⟨next, actual⟩; cases actual
    · intro enabled; omega

theorem reconstruction_counts {s next : State} (actual : reconstruct s = some next) :
    next.weak = s.weak + weakCapacity s ∧
    next.strong = s.strong + strongCapacity s := by
  unfold reconstruct assemble generatedTable at actual
  dsimp at actual
  split at actual
  · cases Option.some.inj actual
    simp
  · cases actual

theorem reconstructed_comparison {s next : State}
    (actual : reconstruct s = some next) (w : s.weak = 0) (g : s.strong = 0) :
    next.weak < next.strong ↔ weakCapacity s < strongCapacity s := by
  obtain ⟨wc, gc⟩ := reconstruction_counts actual
  omega

/-- A conventional two-type population recurrence is exactly recovered on the
    empty-pool slice whenever the full material history actually admits a cycle.
    This is correspondence, not superior prediction over that same recurrence.
    Pooling permits remainder sharing: the strong term is floor(33*g/2), not 16*g. -/
theorem cycle_population_correspondence {s next : State}
    (actual : cycle s = some next)
    (wa : s.weakA = 0) (wh : s.weakH = 0)
    (ga : s.strongA = 0) (gh : s.strongH = 0) :
    next.weak = 7 * s.weak ∧ next.strong = (33 * s.strong) / 2 := by
  unfold cycle at actual
  cases first : operate s with
  | none => simp [first] at actual
  | some produced =>
    simp only [first, Option.bind_some] at actual
    obtain ⟨wc, gc⟩ := reconstruction_counts actual
    unfold operate at first
    dsimp [RecursiveGenerativeSelection.pooled, RecursiveGenerativeSelection.descendants,
      RecursiveGenerativeSelection.support] at first
    split at first
    · cases Option.some.inj first
      dsimp [weakCapacity, strongCapacity] at wc gc
      omega
    · cases first

theorem reconfiguration_accounts {s next : State} {toStrong toWeak : Nat}
    (actual : reconfigure s toStrong toWeak = some next) :
    material next = material s ∧
    next.available + next.spent = s.available + s.spent ∧
    next.available < s.available := by
  unfold reconfigure at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    dsimp [material]
    omega
  · cases actual

inductive Event where
  | operate
  | reconstruct
  | reconfigure (toStrong toWeak : Nat)
  deriving DecidableEq

def step (event : Event) (s : State) : Option State :=
  match event with
  | .operate => operate s
  | .reconstruct => reconstruct s
  | .reconfigure a b => reconfigure s a b

def run : List Event → State → Option State
  | [], s => some s
  | e :: es, s => (step e s).bind (run es)

theorem step_accounts {event : Event} {s next : State} (actual : step event s = some next) :
    material next = material s ∧ next.available + next.spent = s.available + s.spent := by
  cases event with
  | operate => exact operation_accounts actual
  | reconstruct => exact assembly_accounts actual
  | reconfigure a b =>
    obtain ⟨mat, support, _⟩ := reconfiguration_accounts actual
    exact ⟨mat, support⟩

theorem step_consumes_support {event : Event} {s next : State}
    (actual : step event s = some next) : next.available < s.available := by
  cases event with
  | operate =>
    change operate s = some next at actual
    unfold operate at actual
    dsimp [RecursiveGenerativeSelection.pooled, RecursiveGenerativeSelection.descendants,
      RecursiveGenerativeSelection.support] at actual
    split at actual
    · rename_i enabled
      cases Option.some.inj actual
      dsimp
      omega
    · cases actual
  | reconstruct =>
    change assemble s (generatedTable s) = some next at actual
    unfold assemble at actual
    dsimp at actual
    split at actual
    · rename_i enabled
      cases Option.some.inj actual
      dsimp
      omega
    · cases actual
  | reconfigure a b => exact (reconfiguration_accounts actual).2.2

theorem run_accounts (events : List Event) {s next : State}
    (actual : run events s = some next) :
    material next = material s ∧ next.available + next.spent = s.available + s.spent := by
  induction events generalizing s with
  | nil =>
    cases Option.some.inj actual
    exact ⟨rfl, rfl⟩
  | cons e es ih =>
    simp only [run] at actual
    cases first : step e s with
    | none => simp [first] at actual
    | some middle =>
      simp only [first, Option.bind_some] at actual
      obtain ⟨m1, a1⟩ := step_accounts first
      obtain ⟨m2, a2⟩ := ih actual
      exact ⟨m2.trans m1, a2.trans a1⟩

/-- No arbitrarily long supported history from a fixed unreplenished stock. -/
theorem run_length_bound (events : List Event) {s next : State}
    (actual : run events s = some next) : events.length + next.available ≤ s.available := by
  induction events generalizing s with
  | nil =>
    cases Option.some.inj actual
    simp
  | cons e es ih =>
    simp only [run] at actual
    cases first : step e s with
    | none => simp [first] at actual
    | some middle =>
      simp only [first, Option.bind_some] at actual
      have bound := ih actual
      have consumed := step_consumes_support first
      simp only [List.length_cons]
      omega

def seed : State := ⟨100000, 100000, 0, 2, 0, 0, 0, 0, 0, 0⟩

/-- No initially strong arrangement; an actual reconfiguration precedes its
    reproduction and two computed reconstructions, with no supplied tables. -/
theorem formed_two_cycle_history :
    seed.strong = 0 ∧
    run [.reconfigure 1 0, .operate, .reconstruct, .operate, .reconstruct] seed =
      some ⟨97258, 96921, 3079, 49, 264, 25, 0, 16, 36, 2⟩ := by decide

theorem first_generated_generation :
    run [.reconfigure 1 0, .operate, .reconstruct] seed =
      some ⟨99808, 99784, 216, 7, 16, 2, 0, 2, 4, 2⟩ := by decide

/-- Losing the reconstructed configuration changes the actual next operation. -/
theorem eroded_second_cycle_history :
    run [.reconfigure 1 0, .operate, .reconstruct, .reconfigure 0 16,
      .operate, .reconstruct] seed =
      some ⟨98474, 98273, 1727, 161, 0, 25, 0, 48, 4, 2⟩ := by decide

theorem support_failure_and_residual_limits :
    reconfigure { seed with available := 0 } 1 0 = none ∧
    reconfigure seed 3 0 = none ∧
    reconstruct ⟨0, 100, 0, 0, 0, 0, 3, 100, 100, 3⟩ = none ∧
    reconstruct ⟨0, 22, 0, 0, 0, 0, 28, 30, 68, 66⟩ = none := by decide

/-- Larger realized offspring output can exhaust support earlier. Both states
    here have enough precursor and the SAME available activity support. -/
theorem stronger_operation_can_be_unavailable :
    operate ⟨1000, 100, 0, 1, 0, 0, 0, 0, 0, 0⟩ =
      some ⟨942, 42, 58, 0, 0, 1, 28, 30, 0, 0⟩ ∧
    operate ⟨1000, 100, 0, 0, 1, 0, 0, 0, 0, 0⟩ = none := by decide

end GeneratedSelectionRecurrence
