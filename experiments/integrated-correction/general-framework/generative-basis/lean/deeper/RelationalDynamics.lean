import DynamicUnderdetermination

/-!
# Dynamics read relationally: what the carrier counterexample depends on

`DynamicUnderdetermination.same_carrier_incompatible_laws` and
`DynamicSymmetry.symmetric_dynamics_remain_underdetermined` show that on one
carrier (two states, one kind of event) the laws `idle`, `static` and `toggle`
all fit the same carrier, and that `static` and `toggle` share totality,
determinism, reversibility and renaming invariance while disagreeing about
whether a state can stay unchanged.

That counterexample gives the states first and the law second. Here states are
identified only through their relations: two configurations count as the same
when each event one admits is matched by the other, with matched results
(bisimulation, a definition, not an axiom). Read this way:

* `static` and `toggle` are one dynamics. Every state of each is related to
  every state of the other, and both are the single recurring event
  (`singletonLoop`) of `event_without_state_distinction`
  (`static_toggle_one_dynamics`). They have exactly the same histories
  (`static_toggle_same_histories`). "Whether a state stays unchanged" reads the
  carrier's own equality, which no relation of the process supplies
  (`unchanged_reads_carrier_identity`).
* More generally, every process with one kind of event in which every
  configuration can continue is this same single recurrence, whatever its
  carrier (`continuing_single_event_is_one_recurrence`).
* The only difference left among the three laws is whether anything happens.
  `idle` is not related to the recurrence (`idle_differs_from_recurrence`);
  `toggle` continues without end and `idle` cannot continue at all
  (`toggle_continues`, `idle_cannot_continue`).

So the underdetermination between `static` and `toggle` is an artifact of
supplying state identity before relations. What remains open is the choice
between activity and no activity. Reading that choice as settled by
generativity (what exists is continuing activity) is an interpretation of the
theory, not a theorem here.
-/

namespace Generative.Deeper

universe u v w

/-- Relational identity of configurations across two processes on the same events. -/
def Bisimulation {S : Type u} {T : Type w} {A : Type v}
    (P : Process S A) (Q : Process T A) (B : S → T → Prop) : Prop :=
  (∀ s t a s', B s t → P.step s a s' → ∃ t', Q.step t a t' ∧ B s' t') ∧
    (∀ s t a t', B s t → Q.step t a t' → ∃ s', P.step s a s' ∧ B s' t')

/-- Related configurations have the same finite histories. -/
theorem bisimulation_feasible {S : Type u} {T : Type w} {A : Type v}
    {P : Process S A} {Q : Process T A} {B : S → T → Prop}
    (bis : Bisimulation P Q B) :
    ∀ (word : List A) (s : S) (t : T), B s t → Feasible P s word → Feasible Q t word := by
  intro word
  induction word with
  | nil => intro s t _ _; exact ⟨t, .nil t⟩
  | cons a rest ih =>
    intro s t related feasible
    obtain ⟨final, trace⟩ := feasible
    cases trace with
    | cons step tail =>
      obtain ⟨t', qstep, related'⟩ := bis.1 _ _ _ _ related step
      obtain ⟨end', tail'⟩ := ih _ t' related' ⟨final, tail⟩
      exact ⟨end', .cons qstep tail'⟩

theorem bisimulation_converse {S : Type u} {T : Type w} {A : Type v}
    {P : Process S A} {Q : Process T A} {B : S → T → Prop}
    (bis : Bisimulation P Q B) : Bisimulation Q P (fun t s => B s t) :=
  ⟨fun t s a t' r h => bis.2 s t a t' r h, fun t s a s' r h => bis.1 s t a s' r h⟩

theorem bisimulation_same_histories {S : Type u} {T : Type w} {A : Type v}
    {P : Process S A} {Q : Process T A} {B : S → T → Prop}
    (bis : Bisimulation P Q B) {s : S} {t : T} (related : B s t) (word : List A) :
    Feasible P s word ↔ Feasible Q t word :=
  ⟨bisimulation_feasible bis word s t related,
    bisimulation_feasible (bisimulation_converse bis) word t s related⟩

/-- Every process with one kind of event in which every configuration can
continue is the single recurring event, whatever its carrier. -/
theorem continuing_single_event_is_one_recurrence {S : Type u} (P : Process S Unit)
    (continues : ∀ s, ∃ t, P.step s () t) :
    Bisimulation P singletonLoop (fun _ _ => True) := by
  constructor
  · intro s t a s' _ _
    exact ⟨(), trivial, trivial⟩
  · intro s t a t' _ _
    obtain ⟨s', step⟩ := continues s
    cases a
    exact ⟨s', step, trivial⟩

theorem static_is_one_recurrence : Bisimulation static singletonLoop (fun _ _ => True) :=
  continuing_single_event_is_one_recurrence static (fun s => ⟨s, rfl⟩)

theorem toggle_is_one_recurrence : Bisimulation toggle singletonLoop (fun _ _ => True) :=
  continuing_single_event_is_one_recurrence toggle (fun s => ⟨!s, rfl⟩)

/-- `static` and `toggle` are one dynamics: every state of one is related to
every state of the other. -/
theorem static_toggle_one_dynamics : Bisimulation static toggle (fun _ _ => True) := by
  constructor
  · intro s t a s' _ _
    cases a
    exact ⟨!t, rfl, trivial⟩
  · intro s t a t' _ _
    cases a
    exact ⟨s, rfl, trivial⟩

theorem static_toggle_same_histories (s t : Bool) (word : List Unit) :
    Feasible static s word ↔ Feasible toggle t word :=
  bisimulation_same_histories static_toggle_one_dynamics trivial word

/-- Within each law the two states are relationally the same configuration. -/
theorem states_relationally_identical :
    Bisimulation static static (fun _ _ => True) ∧
      Bisimulation toggle toggle (fun _ _ => True) :=
  ⟨⟨fun _ t _ _ _ _ => ⟨t, rfl, trivial⟩, fun s _ _ _ _ _ => ⟨s, rfl, trivial⟩⟩,
    ⟨fun _ t _ _ _ _ => ⟨!t, rfl, trivial⟩, fun s _ _ _ _ _ => ⟨!s, rfl, trivial⟩⟩⟩

/-- "A step can leave the state unchanged" separates `static` from `toggle`,
although they are related state for state; it reads the carrier's equality,
which no relation of either process supplies. -/
theorem unchanged_reads_carrier_identity :
    (∃ s, static.step s () s) ∧ ¬ (∃ s, toggle.step s () s) ∧
      Bisimulation static toggle (fun _ _ => True) := by
  refine ⟨⟨false, rfl⟩, ?_, static_toggle_one_dynamics⟩
  rintro ⟨s, h⟩
  cases s <;> cases h

/-- What remains is whether anything happens. -/
theorem idle_differs_from_recurrence (B : Bool → Unit → Prop) (related : ∃ s, B s ()) :
    ¬ Bisimulation idle singletonLoop B := by
  intro bis
  obtain ⟨s, r⟩ := related
  obtain ⟨_, step, _⟩ := bis.2 s () () () r trivial
  exact step

/-- `toggle` (equally `static`) continues without end from every state. -/
theorem toggle_continues (s : Bool) :
    ∃ states : Nat → Bool, states 0 = s ∧ ∀ n, toggle.step (states n) () (states (n + 1)) := by
  refine ⟨fun n => Nat.rec s (fun _ prev => !prev) n, rfl, ?_⟩
  intro n
  rfl

/-- `idle` cannot continue at all. -/
theorem idle_cannot_continue (s : Bool) :
    ¬ ∃ states : Nat → Bool, states 0 = s ∧ ∀ n, idle.step (states n) () (states (n + 1)) := by
  rintro ⟨states, _, steps⟩
  exact steps 0

#print axioms Generative.Deeper.bisimulation_feasible
#print axioms Generative.Deeper.bisimulation_converse
#print axioms Generative.Deeper.bisimulation_same_histories
#print axioms Generative.Deeper.continuing_single_event_is_one_recurrence
#print axioms Generative.Deeper.static_is_one_recurrence
#print axioms Generative.Deeper.toggle_is_one_recurrence
#print axioms Generative.Deeper.static_toggle_one_dynamics
#print axioms Generative.Deeper.static_toggle_same_histories
#print axioms Generative.Deeper.states_relationally_identical
#print axioms Generative.Deeper.unchanged_reads_carrier_identity
#print axioms Generative.Deeper.idle_differs_from_recurrence
#print axioms Generative.Deeper.toggle_continues
#print axioms Generative.Deeper.idle_cannot_continue

end Generative.Deeper
