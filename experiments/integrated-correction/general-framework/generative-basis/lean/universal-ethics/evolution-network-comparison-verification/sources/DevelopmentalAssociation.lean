import GenerativeCore

/-!
# Inherited local division relations generate association

An executable, conditional reconstruction of division, inherited retention,
separation and aggregation. Groups are connected positions in the resulting
bond relation; no collective membership table is an input. A mutable retention
state changes whether later daughters stay attached and is copied at division.

The local division/retention law, event occurrence and unit accounting are
supplied. This is not a molecular derivation, mutation-rate model, energetic
calibration, indefinitely supplied culture, or proof of ethical direction.
Founder origin is genealogical, not genetic identity in the presence of change.
-/

namespace DevelopmentalAssociation

structure State where
  count : Nat
  precursor : Nat
  available : Nat
  spent : Nat
  retains : Nat → Bool
  founder : Nat → Nat
  bonds : List (Nat × Nat)

def material (s : State) : Nat := s.precursor + s.count

/-- Cells have positions below count. Entries outside count have no operative
    cell interpretation. New daughters inherit the parent's current state. -/
def divide (s : State) (parent : Nat) : Option State :=
  if parent < s.count ∧ 0 < s.precursor ∧ 0 < s.available then
    some { s with
      count := s.count + 1
      precursor := s.precursor - 1
      available := s.available - 1
      spent := s.spent + 1
      retains := fun i => if i = s.count then s.retains parent else s.retains i
      founder := fun i => if i = s.count then s.founder parent else s.founder i
      bonds := if s.retains parent then (parent, s.count) :: s.bonds else s.bonds }
  else none

def changeRetention (s : State) (cell : Nat) (value : Bool) : Option State :=
  if cell < s.count ∧ s.retains cell ≠ value ∧ 0 < s.available then
    some { s with
      available := s.available - 1
      spent := s.spent + 1
      retains := fun i => if i = cell then value else s.retains i }
  else none

def detach (s : State) (parent child : Nat) : Option State :=
  if (parent, child) ∈ s.bonds ∧ 0 < s.available then
    some { s with
      available := s.available - 1
      spent := s.spent + 1
      bonds := s.bonds.filter (fun e => e != (parent, child)) }
  else none

/-- A distinct possible association mechanism. Unlike division, it can connect
    existing positions from different founders; it is not assumed clonal. -/
def aggregate (s : State) (a b : Nat) : Option State :=
  if a < s.count ∧ b < s.count ∧ a ≠ b ∧ 0 < s.available then
    some { s with
      available := s.available - 1
      spent := s.spent + 1
      bonds := (a, b) :: s.bonds }
  else none

inductive Event where
  | divide (parent : Nat)
  | changeRetention (cell : Nat) (value : Bool)
  | detach (parent child : Nat)
  | aggregate (a b : Nat)
  deriving DecidableEq

def step (e : Event) (s : State) : Option State :=
  match e with
  | .divide p => divide s p
  | .changeRetention c v => changeRetention s c v
  | .detach p c => detach s p c
  | .aggregate a b => aggregate s a b

def run : List Event → State → Option State
  | [], s => some s
  | e :: es, s => (step e s).bind (run es)

def process : Generative.Process State Event where
  step s e t := step e s = some t

/-- This is an actual instance of the inherited relational core. -/
theorem run_iff_core_trace (word : List Event) (s t : State) :
    run word s = some t ↔ Generative.Trace process s word t := by
  induction word generalizing s with
  | nil => simp [run, Generative.trace_nil_iff]
  | cons e es ih =>
    rw [Generative.trace_cons_iff]
    change ((step e s).bind (run es) = some t) ↔
      ∃ middle, step e s = some middle ∧ Generative.Trace process middle es t
    cases first : step e s with
    | none => simp
    | some middle => simpa using ih middle

theorem division_inherits {s t : State} {p : Nat} (actual : divide s p = some t) :
    t.count = s.count + 1 ∧ t.retains s.count = s.retains p ∧
    t.founder s.count = s.founder p ∧
    t.bonds = (if s.retains p then (p, s.count) :: s.bonds else s.bonds) := by
  unfold divide at actual
  split at actual
  · cases Option.some.inj actual
    simp
  · cases actual

theorem changed_state_governs_division {s changed t : State} {p : Nat} {v : Bool}
    (change : changeRetention s p v = some changed)
    (birth : divide changed p = some t) :
    t.retains changed.count = v ∧
    t.bonds = (if v then (p, changed.count) :: changed.bonds else changed.bonds) := by
  have inherited := division_inherits birth
  unfold changeRetention at change
  split at change
  · cases Option.some.inj change
    simpa using And.intro inherited.2.1 inherited.2.2.2
  · cases change

theorem step_accounts {e : Event} {s t : State} (actual : step e s = some t) :
    material t = material s ∧ t.available + t.spent = s.available + s.spent ∧
      t.available + 1 = s.available := by
  cases e <;> simp only [step] at actual
  all_goals first | unfold divide at actual | unfold changeRetention at actual |
    unfold detach at actual | unfold aggregate at actual
  all_goals split at actual
  all_goals first
    | (rename_i enabled; cases Option.some.inj actual; dsimp [material]; omega)
    | cases actual

theorem core_trace_accounts {word : List Event} {s t : State}
    (actual : Generative.Trace process s word t) :
    material t = material s ∧ t.available + t.spent = s.available + s.spent ∧
      word.length + t.available = s.available := by
  induction actual with
  | nil => simp
  | cons first _ ih =>
    obtain ⟨m, a, used⟩ := step_accounts first
    obtain ⟨mt, accounted, count⟩ := ih
    refine ⟨mt.trans m, accounted.trans a, ?_⟩
    simp only [List.length_cons]
    omega

/-- Lineage consistency does not assert that descendants never mutate. -/
def LineageConsistent (s : State) : Prop :=
  ∀ a b, (a, b) ∈ s.bonds → a < s.count ∧ b < s.count ∧ s.founder a = s.founder b

theorem division_preserves_lineage {s t : State} {p : Nat}
    (consistent : LineageConsistent s) (actual : divide s p = some t) :
    LineageConsistent t := by
  unfold divide at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    intro a b member
    dsimp at member ⊢
    have old : ∀ a b, (a, b) ∈ s.bonds →
        a < s.count + 1 ∧ b < s.count + 1 ∧
        (if a = s.count then s.founder p else s.founder a) =
        (if b = s.count then s.founder p else s.founder b) := by
      intro x y h
      obtain ⟨hx, hy, same⟩ := consistent x y h
      simp only [if_neg (Nat.ne_of_lt hx), if_neg (Nat.ne_of_lt hy)]
      exact ⟨by omega, by omega, same⟩
    split at member
    · rcases List.mem_cons.mp member with fresh | prior
      · rcases Prod.mk.inj fresh with ⟨rfl, rfl⟩
        simp only [if_neg (Nat.ne_of_lt enabled.1)]
        exact ⟨by omega, by omega, rfl⟩
      · exact old a b prior
    · exact old a b member
  · cases actual

def NoAggregation (e : Event) : Prop :=
  match e with
  | .aggregate _ _ => False
  | _ => True

theorem step_preserves_lineage {e : Event} {s t : State}
    (noMix : NoAggregation e) (consistent : LineageConsistent s)
    (actual : step e s = some t) : LineageConsistent t := by
  cases e with
  | divide p => exact division_preserves_lineage consistent actual
  | changeRetention c v =>
    change changeRetention s c v = some t at actual
    unfold changeRetention at actual
    split at actual
    · cases Option.some.inj actual
      exact consistent
    · cases actual
  | detach p c =>
    change detach s p c = some t at actual
    unfold detach at actual
    split at actual
    · cases Option.some.inj actual
      intro a b h
      exact consistent a b (List.mem_filter.mp h).1
    · cases actual
  | aggregate a b => exact False.elim noMix

theorem trace_preserves_lineage {word : List Event} {s t : State}
    (actual : Generative.Trace process s word t)
    (noMix : ∀ e ∈ word, NoAggregation e) (consistent : LineageConsistent s) :
    LineageConsistent t := by
  induction actual with
  | nil => exact consistent
  | cons first _ ih =>
    exact ih (fun e h => noMix e (List.mem_cons_of_mem _ h))
      (step_preserves_lineage (noMix _ (by simp)) consistent first)

/-- Undirected connectivity gives collective association from actual bonds. -/
inductive Connected (bonds : List (Nat × Nat)) : Nat → Nat → Prop where
  | refl (a : Nat) : Connected bonds a a
  | bond {a b : Nat} : (a, b) ∈ bonds → Connected bonds a b
  | symm {a b : Nat} : Connected bonds a b → Connected bonds b a
  | trans {a b c : Nat} : Connected bonds a b → Connected bonds b c → Connected bonds a c

theorem connected_same_founder {s : State} {a b : Nat}
    (consistent : LineageConsistent s) (connected : Connected s.bonds a b) :
    s.founder a = s.founder b := by
  induction connected with
  | refl => rfl
  | bond h => exact (consistent _ _ h).2.2
  | symm _ ih => exact ih.symm
  | trans _ _ ih1 ih2 => exact ih1.trans ih2

/-- With no aggregation, group ancestry is a consequence of local history;
    a fresh investigator-assigned grouping is not a premise. -/
theorem developed_groups_have_common_origin {word : List Event} {s t : State} {a b : Nat}
    (initial : LineageConsistent s) (actual : run word s = some t)
    (noMix : ∀ e ∈ word, NoAggregation e) (associated : Connected t.bonds a b) :
    t.founder a = t.founder b :=
  connected_same_founder
    (trace_preserves_lineage ((run_iff_core_trace word s t).mp actual) noMix initial)
    associated

def seed (n : Nat) : State :=
  ⟨n, 10, 20, 0, fun _ => false, fun i => i, []⟩

theorem seed_lineage (n : Nat) : LineageConsistent (seed n) := by
  intro a b h
  cases h

abbrev Observation := Nat × Nat × Nat × Nat × List Bool × List Nat × List (Nat × Nat)

def observe (s : State) : Observation :=
  (s.count, s.precursor, s.available, s.spent,
    (List.range s.count).map s.retains, (List.range s.count).map s.founder, s.bonds)

def development : List Event :=
  [.changeRetention 0 true, .divide 0, .divide 1, .divide 2]

theorem changed_division_forms_group :
    (run development (seed 1)).map observe =
    some (4, 7, 16, 4, [true, true, true, true], [0, 0, 0, 0],
      [(2, 3), (1, 2), (0, 1)]) := by rfl

/-- A separated descendant inherits the operative division relation and grows
    further with the same remaining material and activity-support accounts. -/
theorem separated_descendant_reconstructs_association :
    (run (development ++ [.detach 1 2, .divide 2]) (seed 1)).map observe =
    some (5, 6, 14, 6, [true, true, true, true, true], [0, 0, 0, 0, 0],
      [(2, 4), (2, 3), (0, 1)]) := by rfl

/-- Restoring separation changes subsequent division but does not magically
    remove pre-existing bonds. -/
theorem restored_separation_changes_later_growth :
    (run (development ++ [.changeRetention 2 false, .divide 2]) (seed 1)).map observe =
    some (5, 6, 14, 6, [true, true, false, true, false], [0, 0, 0, 0, 0],
      [(2, 3), (1, 2), (0, 1)]) := by rfl

def mixed : State := (aggregate (seed 2) 0 1).getD (seed 2)

theorem aggregation_breaks_clonal_conclusion :
    aggregate (seed 2) 0 1 = some mixed ∧ Connected mixed.bonds 0 1 ∧
      mixed.founder 0 ≠ mixed.founder 1 := by
  refine ⟨rfl, Connected.bond ?_, ?_⟩
  · decide
  · decide

def splitMiddle : State :=
  (run (development ++ [.detach 1 2]) (seed 1)).getD (seed 1)
def splitBase : State :=
  (run (development ++ [.detach 0 1]) (seed 1)).getD (seed 1)

abbrev CoarseObservation := Nat × Nat × Nat × Nat × List Bool × List Nat

/-- Gives the comparison full indexed cell states and resources, omitting only
    bonds; it is stronger than a simple frequency/count summary. -/
def coarse (s : State) : CoarseObservation :=
  (s.count, s.precursor, s.available, s.spent,
    (List.range s.count).map s.retains, (List.range s.count).map s.founder)

theorem equal_cell_states_different_continuations :
    coarse splitMiddle = coarse splitBase ∧
    (step (.detach 0 1) splitMiddle).isSome = true ∧
    (step (.detach 0 1) splitBase).isSome = false := by decide

theorem comparison_histories_are_actual :
    Generative.Trace process (seed 1) (development ++ [.detach 1 2]) splitMiddle ∧
    Generative.Trace process (seed 1) (development ++ [.detach 0 1]) splitBase := by
  constructor
  · exact (run_iff_core_trace _ _ _).mp rfl
  · exact (run_iff_core_trace _ _ _).mp rfl

/-- Even when restricted to histories reached from the same single founder,
    indexed cellular states and resources without bonds do not suffice. -/
theorem no_bond_free_exact_predictor :
    ¬ ∃ predict : CoarseObservation → Bool,
      ∀ word s, Generative.Trace process (seed 1) word s →
        predict (coarse s) = (step (.detach 0 1) s).isSome := by
  rintro ⟨predict, faithful⟩
  obtain ⟨same, yes, no⟩ := equal_cell_states_different_continuations
  have l := faithful _ splitMiddle comparison_histories_are_actual.1
  have r := faithful _ splitBase comparison_histories_are_actual.2
  rw [same] at l
  have eq := l.symm.trans r
  rw [yes, no] at eq
  cases eq

theorem ineffective_operations_fail :
    (divide { seed 1 with precursor := 0 } 0).isNone = true ∧
    (divide { seed 1 with available := 0 } 0).isNone = true ∧
    (divide (seed 1) 1).isNone = true ∧
    (changeRetention (seed 1) 0 false).isNone = true ∧
    (detach (seed 1) 0 1).isNone = true := by decide

end DevelopmentalAssociation
