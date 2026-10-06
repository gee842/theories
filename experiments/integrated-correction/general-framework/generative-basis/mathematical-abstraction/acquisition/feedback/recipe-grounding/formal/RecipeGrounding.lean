import Std

/-!
Two-row decoder construction and acquired selection under an explicit unary
transduction law. The output-wire primitives and reference-to-target binding
are declared local laws; this does not derive the jig, transducer, assembler,
or their physical origin. Native construction/account correspondence belongs
to the separately checked execution module.

Reliability means recovering the independently addressed physical input for
every Boolean input. It is not a runtime success flag. The selected decoder is
constructed from the two acquired reference responses and is the object whose
composition is proved correct. Constant transductions are rejected.
-/
namespace RecipeGrounding

structure Table where
  zero : Bool
  one : Bool
  deriving DecidableEq, Repr

def Table.read (table : Table) (input : Bool) : Bool :=
  if input then table.one else table.zero

def rowOutputs : List Bool := [false, true]

/-- Two independently chosen output wires generate the table carrier. -/
def generated : List Table :=
  rowOutputs.flatMap (fun zero => rowOutputs.map (fun one => ⟨zero, one⟩))

theorem generated_exact (table : Table) : table ∈ generated := by
  rcases table with ⟨zero, one⟩
  cases zero <;> cases one <;> decide

theorem four_distinct_generated_tables : generated.length = 4 ∧ generated.Nodup := by
  decide

theorem generated_represents_every_unary_function (f : Bool → Bool) :
    ∃ table, table ∈ generated ∧ ∀ input, table.read input = f input := by
  refine ⟨⟨f false, f true⟩, generated_exact _, ?_⟩
  intro input
  cases input <;> rfl

structure Wiring where
  zero : Option Bool := none
  one : Option Bool := none
  deriving DecidableEq, Repr

def Wiring.write (w : Wiring) (raw output : Bool) : Wiring :=
  if raw then { w with one := some output } else { w with zero := some output }

def Wiring.complete (w : Wiring) : Option Table := do
  let zero ← w.zero
  let one ← w.one
  pure ⟨zero, one⟩

/-- Acquired raw reference replies are addresses; reference targets are outputs. -/
def wiringFrom (zeroReply oneReply : Bool) : Wiring :=
  (({} : Wiring).write zeroReply false).write oneReply true

def selectDecoder (zeroReply oneReply : Bool) : Option Table :=
  if zeroReply == oneReply then none else (wiringFrom zeroReply oneReply).complete

theorem selection_exists_iff_distinct (zeroReply oneReply : Bool) :
    (∃ table, selectDecoder zeroReply oneReply = some table) ↔ zeroReply ≠ oneReply := by
  cases zeroReply <;> cases oneReply <;>
    simp [selectDecoder, wiringFrom, Wiring.write, Wiring.complete]

theorem selected_table_is_generated (zeroReply oneReply : Bool) (table : Table)
    (_selected : selectDecoder zeroReply oneReply = some table) : table ∈ generated :=
  generated_exact table

def Recovers (transduction : Bool → Bool) (table : Table) : Prop :=
  ∀ input, table.read (transduction input) = input

theorem actual_selected_decoder_recovers (f : Bool → Bool) (table : Table)
    (selected : selectDecoder (f false) (f true) = some table) : Recovers f table := by
  have casesF : f false = true ∨ f false = false := Bool.eq_false_or_eq_true (f false)
  have casesT : f true = true ∨ f true = false := Bool.eq_false_or_eq_true (f true)
  rcases casesF with hf | hf <;> rcases casesT with ht | ht <;>
    simp [hf, ht, selectDecoder, wiringFrom, Wiring.write, Wiring.complete] at selected
  all_goals subst table
  all_goals intro input; cases input <;> simp [Table.read, hf, ht]

/-- The negative case excludes every possible decoder function, not only generated recipes. -/
theorem equal_reference_replies_preclude_any_decoder (f : Bool → Bool)
    (same : f false = f true) : ¬ ∃ decoder : Bool → Bool, ∀ input, decoder (f input) = input := by
  rintro ⟨decoder, recovery⟩
  have first := recovery false
  have second := recovery true
  rw [same] at first
  have impossible : false = true := first.symm.trans second
  cases impossible

theorem selected_recovery_iff_possible (f : Bool → Bool) :
    (∃ table, selectDecoder (f false) (f true) = some table ∧ Recovers f table) ↔
      ∃ decoder : Bool → Bool, ∀ input, decoder (f input) = input := by
  constructor
  · rintro ⟨table, _, recovery⟩
    exact ⟨table.read, recovery⟩
  · intro possible
    have distinct : f false ≠ f true := by
      intro same
      exact equal_reference_replies_preclude_any_decoder f same possible
    obtain ⟨table, selected⟩ := (selection_exists_iff_distinct _ _).mpr distinct
    exact ⟨table, selected, actual_selected_decoder_recovers f table selected⟩

theorem one_reference_cannot_certify_recoverability (reference : Bool) :
    (fun input : Bool => input) reference = (fun _ : Bool => reference) reference ∧
    (∃ table, Recovers (fun input : Bool => input) table) ∧
    ¬ ∃ decoder : Bool → Bool, ∀ input, decoder ((fun _ : Bool => reference) input) = input := by
  refine ⟨rfl, ⟨⟨false, true⟩, ?_⟩, ?_⟩
  · intro input; cases input <;> rfl
  · exact equal_reference_replies_preclude_any_decoder _ rfl

/- Adaptive choices can depend on retained evidence, but not an inaccessible
coordinate. Here both worlds preserve the same addressed target variable;
their target configurations and observation routes differ physically. -/
def acquire {Memory Query Observation : Type} (ask : Memory → Query)
    (update : Memory → Observation → Memory) (observe : Query → Observation) :
    Nat → Memory → Memory
  | 0, memory => memory
  | n + 1, memory => acquire ask update observe n (update memory (observe (ask memory)))

theorem equal_observations_equal_adaptive_memory {Memory Query Observation : Type}
    (ask : Memory → Query) (update : Memory → Observation → Memory)
    (left right : Query → Observation) (same : ∀ query, left query = right query)
    (steps : Nat) (initial : Memory) :
    acquire ask update left steps initial = acquire ask update right steps initial := by
  induction steps generalizing initial with
  | zero => rfl
  | succ steps ih => simp only [acquire, same]; exact ih _

def target (polarity command : Bool) : Bool := command != polarity
def transduction (polarity input : Bool) : Bool := input != polarity
def unreferencedObservation (polarity command : Bool) : Bool :=
  transduction polarity (target polarity command)

theorem compensated_routes_have_equal_observations (command : Bool) :
    unreferencedObservation false command = unreferencedObservation true command := by
  cases command <;> decide

theorem compensated_routes_preserve_real_target_difference (command : Bool) :
    target false command ≠ target true command := by
  cases command <;> decide

theorem opposite_routes_have_no_common_reliable_decoder :
    ¬ ∃ table, Recovers (transduction false) table ∧ Recovers (transduction true) table := by
  rintro ⟨table, left, right⟩
  have first := left false
  have second := right true
  simp [transduction, Table.read] at first second
  exact Bool.noConfusion (first.symm.trans second)

theorem no_adaptive_unreferenced_reliable_selection {Memory : Type}
    (ask : Memory → Bool) (update : Memory → Bool → Memory)
    (choose : Memory → Table) (steps : Nat) (initial : Memory) :
    ¬ (Recovers (transduction false)
        (choose (acquire ask update (unreferencedObservation false) steps initial)) ∧
      Recovers (transduction true)
        (choose (acquire ask update (unreferencedObservation true) steps initial))) := by
  have same := equal_observations_equal_adaptive_memory ask update
    (unreferencedObservation false) (unreferencedObservation true)
    compensated_routes_have_equal_observations steps initial
  rw [same]
  intro both
  exact opposite_routes_have_no_common_reliable_decoder ⟨_, both⟩

theorem changed_use_transduction_defeats_calibrated_recipe :
    selectDecoder (transduction false false) (transduction false true) = some ⟨false, true⟩ ∧
    Recovers (transduction false) ⟨false, true⟩ ∧
    ¬ Recovers (transduction true) ⟨false, true⟩ := by
  refine ⟨by decide, ?_, ?_⟩
  · intro input; cases input <;> decide
  · intro h; have bad := h false; cases bad

theorem swapped_reference_binding_defeats_selected_recipe :
    selectDecoder (transduction false true) (transduction false false) = some ⟨true, false⟩ ∧
    ¬ Recovers (transduction false) ⟨true, false⟩ := by
  refine ⟨by decide, ?_⟩
  intro h; have bad := h false; cases bad

#print axioms generated_exact
#print axioms four_distinct_generated_tables
#print axioms generated_represents_every_unary_function
#print axioms selection_exists_iff_distinct
#print axioms selected_table_is_generated
#print axioms actual_selected_decoder_recovers
#print axioms equal_reference_replies_preclude_any_decoder
#print axioms selected_recovery_iff_possible
#print axioms one_reference_cannot_certify_recoverability
#print axioms equal_observations_equal_adaptive_memory
#print axioms compensated_routes_have_equal_observations
#print axioms compensated_routes_preserve_real_target_difference
#print axioms opposite_routes_have_no_common_reliable_decoder
#print axioms no_adaptive_unreferenced_reliable_selection
#print axioms changed_use_transduction_defeats_calibrated_recipe
#print axioms swapped_reference_binding_defeats_selected_recipe

end RecipeGrounding
