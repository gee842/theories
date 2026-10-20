import Becoming.Unfolding
import Becoming.Witnesses

/-!
# Carriers: one carrier admits incompatible laws, and relations read them as one recurrence

The carrier of a process is its configurations and moves. On one carrier, two configurations and
one move, three laws fit: `idle` takes no step, `static` keeps the configuration and `toggle`
changes it (`same_carrier_incompatible_laws`). The carrier and its products do not fix the law.

* **Symmetry does not fix it either.** `static` and `toggle` are both total, determined and
  reversible by the same move, so each configuration has one predecessor
  (`unique_predecessor_of_total_determined_symmetric`), and both keep their steps under every
  bijective renaming of the two configurations (`BoolRenamingInvariant`, through
  `injective_bool_map_forms`). With all of this they still differ on whether a configuration stays
  unchanged (`symmetric_dynamics_remain_underdetermined`), and no map of configurations carries one
  law to the other (`no_state_map_identifies_static_toggle`).
* **Read relationally, `static` and `toggle` are one dynamics.** With configurations identified only
  by how they relate to their continuations (`Bisimulation` of `Becoming.Unfolding`, on frames
  with no claims, `bare`), every process with one move in which every configuration can continue is
  related throughout to the single recurring move (`continuing_single_event_is_one_recurrence`), so
  `static` and `toggle` are related configuration for configuration (`static_toggle_one_dynamics`)
  and take the same courses (`static_toggle_same_histories`). "A step can leave the configuration
  unchanged" reads the carrier's own equality, which no relation of either process supplies
  (`unchanged_reads_carrier_identity`). What remains is whether anything happens: `idle` is related
  to no recurrence (`idle_differs_from_recurrence`); `toggle` continues without end and `idle`
  cannot continue (`toggle_continues`, `idle_cannot_continue`).
* **Endpoints and feasible words.** A total process takes every word (`feasible_of_step_total`), so
  any two total processes take the same words (`total_processes_same_feasible`); `static` and
  `toggle` take the same words and end differently (`word_feasibility_does_not_determine_endpoints`,
  `static_toggle_not_same_steps`): forgetting endpoints loses the law. That steps and courses with
  their endpoints fix each other is `Becoming.Unfolding`'s `same_steps_iff_traces`.

The underdetermination between `static` and `toggle` comes from giving configurations before
relations; reading the remaining choice, activity or none, as settled by what continues is an
interpretation, not a theorem here. This module states in the core what
`DynamicUnderdetermination`, `RelationalDynamics`, `DynamicSymmetry` and `DynamicConsequences`
(6 to 8 October 2026) proved on their own definitions (board item F3E, 18 October 2026). No ethical
predicate, ranking or axiom occurs; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

universe u v w

namespace Carriers

/-! ## Three laws on one carrier -/

/-- No step. -/
def idle : Process Bool Unit := Witnesses.halted Bool Unit

/-- The configuration stays. -/
def static : Process Bool Unit := ⟨fun s _ t => s = t⟩

/-- The configuration changes. -/
def toggle : Process Bool Unit := Law.process not

theorem idle_no_event (s : Bool) : ¬ Enabled idle s () :=
  fun ⟨_, h⟩ => h

theorem static_event (s : Bool) : static.step s () s := rfl

theorem static_never_changes {s t : Bool} (h : static.step s () t) : s = t := h

theorem toggle_event (s : Bool) : toggle.step s () (!s) := rfl

theorem toggle_always_changes {s t : Bool} (h : toggle.step s () t) : s ≠ t := by
  cases s <;> cases t <;> cases h <;> intro heq <;> cases heq

theorem static_history_never_changes {s t : Bool} {word : List Unit} (h : Trace static s word t) :
    s = t := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact hs.trans ih

theorem toggle_two_event_cycle (s : Bool) : Trace toggle s [(), ()] s :=
  .cons (toggle_event s) (.cons (by cases s <;> rfl) (.nil s))

/-- **One carrier, three laws.** -/
theorem same_carrier_incompatible_laws :
    ¬ idle.step false () true ∧ toggle.step false () true ∧ static.step false () false ∧
      ¬ toggle.step false () false :=
  ⟨fun h => h, rfl, rfl, fun h => nomatch h⟩

/-- The single recurring move on one configuration. -/
def singletonLoop : Process Unit Unit := everyStep Unit Unit

theorem event_without_state_distinction :
    singletonLoop.step () () () ∧ ∀ s t : Unit, s = t :=
  ⟨True.intro, fun () () => rfl⟩

/-! ## Symmetry -/

/-- Every configuration and move has a successor. -/
def StepTotal {S : Type u} {A : Type v} (P : Process S A) : Prop :=
  ∀ s a, ∃ t, P.step s a t

/-- Each step reverses by the same move. -/
def StepSymmetric {S : Type u} {A : Type v} (P : Process S A) : Prop :=
  ∀ s a t, P.step s a t → P.step t a s

/-- Every configuration and move have exactly one predecessor. -/
def UniquePredecessor {S : Type u} {A : Type v} (P : Process S A) : Prop :=
  ∀ t a, ∃ s, P.step s a t ∧ ∀ r, P.step r a t → r = s

/-- A bijection of the two configurations. -/
def BoolBijection (f : Bool → Bool) : Prop :=
  Function.Injective f ∧ ∀ t, ∃ s, f s = t

/-- The whole step relation is kept under every bijective renaming. -/
def BoolRenamingInvariant (P : Process Bool Unit) : Prop :=
  ∀ f : Bool → Bool, BoolBijection f → ∀ s a t, P.step s a t ↔ P.step (f s) a (f t)

/-- **Total, determined and reversible gives one predecessor.** -/
theorem unique_predecessor_of_total_determined_symmetric {S : Type u} {A : Type v}
    (P : Process S A) (total : StepTotal P) (determined : Determined P) (symmetric : StepSymmetric P) :
    UniquePredecessor P :=
  fun t a => match total t a with
    | ⟨s, hs⟩ => ⟨s, symmetric t a s hs, fun r hr => determined t a r s (symmetric r a t hr) hs⟩

theorem static_total : StepTotal static := fun s _ => ⟨s, rfl⟩

theorem toggle_total : StepTotal toggle := fun s _ => ⟨!s, rfl⟩

theorem static_determined : Determined static := fun _ _ _ _ ht hr => ht.symm.trans hr

theorem toggle_determined : Determined toggle := fun _ _ _ _ ht hr => ht.trans hr.symm

theorem static_symmetric : StepSymmetric static := fun _ _ _ h => h.symm

theorem toggle_symmetric : StepSymmetric toggle := by
  intro s a t h
  cases s <;> cases t <;> cases h <;> rfl

theorem static_unique_predecessor : UniquePredecessor static :=
  unique_predecessor_of_total_determined_symmetric static static_total static_determined
    static_symmetric

theorem toggle_unique_predecessor : UniquePredecessor toggle :=
  unique_predecessor_of_total_determined_symmetric toggle toggle_total toggle_determined
    toggle_symmetric

theorem identity_bool_bijection : BoolBijection (fun s => s) :=
  ⟨fun _ _ h => h, fun t => ⟨t, rfl⟩⟩

theorem negation_bool_bijection : BoolBijection Bool.not :=
  ⟨fun s t h => by cases s <;> cases t <;> cases h <;> rfl, fun t => ⟨!t, by cases t <;> rfl⟩⟩

/-- **Every injective map of the two configurations is the identity or the swap.** -/
theorem injective_bool_map_forms (f : Bool → Bool) (hf : Function.Injective f) :
    (∀ s, f s = s) ∨ (∀ s, f s = !s) := by
  cases hfalse : f false <;> cases htrue : f true
  · exact nomatch hf (hfalse.trans htrue.symm)
  · exact .inl fun s => by cases s; exact hfalse; exact htrue
  · exact .inr fun s => by cases s; exact hfalse; exact htrue
  · exact nomatch hf (hfalse.trans htrue.symm)

theorem injective_bool_map_commutes_not (f : Bool → Bool) (hf : Function.Injective f) (s : Bool) :
    f (!s) = !(f s) :=
  match injective_bool_map_forms f hf with
  | .inl hid => (hid (!s)).trans (congrArg Bool.not (hid s)).symm
  | .inr hnot => (hnot (!s)).trans (congrArg Bool.not (hnot s)).symm

theorem static_renaming_invariant : BoolRenamingInvariant static :=
  fun f hf _ _ _ => ⟨fun h => congrArg f h, fun h => hf.1 h⟩

theorem toggle_renaming_invariant : BoolRenamingInvariant toggle :=
  fun f hf s _ _ =>
    ⟨fun h => (congrArg f h).trans (injective_bool_map_commutes_not f hf.1 s),
     fun h => hf.1 (h.trans (injective_bool_map_commutes_not f hf.1 s).symm)⟩

/-- Total, determined, reversible, one predecessor, renaming-invariant. -/
def SymmetryCandidate (P : Process Bool Unit) : Prop :=
  StepTotal P ∧ Determined P ∧ StepSymmetric P ∧ UniquePredecessor P ∧ BoolRenamingInvariant P

theorem static_symmetry_candidate : SymmetryCandidate static :=
  ⟨static_total, static_determined, static_symmetric, static_unique_predecessor,
   static_renaming_invariant⟩

theorem toggle_symmetry_candidate : SymmetryCandidate toggle :=
  ⟨toggle_total, toggle_determined, toggle_symmetric, toggle_unique_predecessor,
   toggle_renaming_invariant⟩

theorem static_ne_toggle : static ≠ toggle :=
  fun same => toggle_always_changes (same ▸ static_event false : toggle.step false () false) rfl

/-- **No map of configurations carries one law to the other.** -/
theorem no_state_map_identifies_static_toggle (f : Bool → Bool) :
    ¬ ∀ s a t, static.step s a t ↔ toggle.step (f s) a (f t) :=
  fun h => toggle_always_changes ((h false () false).mp (static_event false)) rfl

/-- **The symmetry properties do not select one law.** -/
theorem symmetric_dynamics_remain_underdetermined :
    ∃ P Q : Process Bool Unit, SymmetryCandidate P ∧ SymmetryCandidate Q ∧ P ≠ Q ∧
      P.step false () false ∧ ¬ Q.step false () false :=
  ⟨static, toggle, static_symmetry_candidate, toggle_symmetry_candidate, static_ne_toggle,
   static_event false, fun h => toggle_always_changes h rfl⟩

/-! ## Relations read the laws -/

/-- A process read with no claims. -/
def bare {S : Type u} {A : Type v} (P : Process S A) : Frame S A Empty :=
  ⟨P, fun _ c => nomatch c⟩

/-- **Every process with one move in which every configuration can continue is the single
recurrence**, whatever its carrier. -/
theorem continuing_single_event_is_one_recurrence {S : Type u} (P : Process S Unit)
    (continues : ∀ s, ∃ t, P.step s () t) :
    Bisimulation (bare P) (bare singletonLoop) fun _ _ => True :=
  fun s _ _ =>
    ⟨(fun c => nomatch c), fun _ _ _ => ⟨(), True.intro, True.intro⟩,
     fun () () _ => match continues s with
       | ⟨s', step⟩ => ⟨s', step, True.intro⟩⟩

theorem static_is_one_recurrence : Bisimulation (bare static) (bare singletonLoop) fun _ _ => True :=
  continuing_single_event_is_one_recurrence static fun s => ⟨s, rfl⟩

theorem toggle_is_one_recurrence : Bisimulation (bare toggle) (bare singletonLoop) fun _ _ => True :=
  continuing_single_event_is_one_recurrence toggle fun s => ⟨!s, rfl⟩

/-- **`static` and `toggle` are one dynamics**: every configuration of one is related to every
configuration of the other. -/
theorem static_toggle_one_dynamics : Bisimulation (bare static) (bare toggle) fun _ _ => True :=
  fun _ t _ =>
    ⟨(fun c => nomatch c), fun () _ _ => ⟨!t, rfl, True.intro⟩, fun () _ _ => ⟨_, rfl, True.intro⟩⟩

/-- **They take the same courses.** -/
theorem static_toggle_same_histories (s t : Bool) (word : List Unit) :
    Feasible static s word ↔ Feasible toggle t word :=
  ⟨fun ⟨_, path⟩ => match static_toggle_one_dynamics.trace path (s' := t) True.intro with
    | ⟨u, path', _⟩ => ⟨u, path'⟩,
   fun ⟨_, path⟩ => match static_toggle_one_dynamics.converse.trace path (s' := s) True.intro with
    | ⟨u, path', _⟩ => ⟨u, path'⟩⟩

/-- Within each law the two configurations are relationally one. -/
theorem states_relationally_identical :
    Bisimulation (bare static) (bare static) (fun _ _ => True) ∧
      Bisimulation (bare toggle) (bare toggle) (fun _ _ => True) :=
  ⟨fun _ t _ => ⟨(fun c => nomatch c), fun () _ _ => ⟨t, rfl, True.intro⟩,
     fun () _ _ => ⟨_, rfl, True.intro⟩⟩,
   fun _ t _ => ⟨(fun c => nomatch c), fun () _ _ => ⟨!t, rfl, True.intro⟩,
     fun () _ _ => ⟨_, rfl, True.intro⟩⟩⟩

/-- **"A step can leave the configuration unchanged" reads the carrier's equality**: it separates
`static` from `toggle`, which are related configuration for configuration. -/
theorem unchanged_reads_carrier_identity :
    (∃ s, static.step s () s) ∧ ¬ (∃ s, toggle.step s () s) ∧
      Bisimulation (bare static) (bare toggle) (fun _ _ => True) :=
  ⟨⟨false, rfl⟩, (fun ⟨s, h⟩ => by cases s <;> cases h), static_toggle_one_dynamics⟩

/-- **What remains is whether anything happens**: `idle` is related to no recurrence. -/
theorem idle_differs_from_recurrence (B : Bool → Unit → Prop) (related : ∃ s, B s ()) :
    ¬ Bisimulation (bare idle) (bare singletonLoop) B :=
  fun bisim => match related with
    | ⟨s, r⟩ => match (bisim s () r).2.2 () () True.intro with
      | ⟨_, step, _⟩ => step

/-- `toggle` continues without end from every configuration. -/
theorem toggle_continues (s : Bool) :
    ∃ states : Nat → Bool, states 0 = s ∧ ∀ n, toggle.step (states n) () (states (n + 1)) :=
  ⟨fun n => Nat.rec (motive := fun _ => Bool) s (fun _ prev => !prev) n, rfl, fun _ => rfl⟩

/-- `idle` cannot continue at all. -/
theorem idle_cannot_continue (s : Bool) :
    ¬ ∃ states : Nat → Bool, states 0 = s ∧ ∀ n, idle.step (states n) () (states (n + 1)) :=
  fun ⟨_, _, steps⟩ => steps 0

/-! ## Endpoints and feasible words -/

/-- **A total process takes every word.** -/
theorem feasible_of_step_total {S : Type u} {A : Type v} {P : Process S A} (total : StepTotal P) :
    ∀ (s : S) (word : List A), Feasible P s word
  | s, [] => ⟨s, .nil s⟩
  | s, a :: word => match total s a with
    | ⟨t, step⟩ => match feasible_of_step_total total t word with
      | ⟨r, path⟩ => ⟨r, .cons step path⟩

/-- **Two total processes take the same words.** -/
theorem total_processes_same_feasible {S : Type u} {A : Type v} {P Q : Process S A}
    (hp : StepTotal P) (hq : StepTotal Q) (s : S) (word : List A) :
    Feasible P s word ↔ Feasible Q s word :=
  ⟨fun _ => feasible_of_step_total hq s word, fun _ => feasible_of_step_total hp s word⟩

theorem static_toggle_same_feasible (s : Bool) (word : List Unit) :
    Feasible static s word ↔ Feasible toggle s word :=
  total_processes_same_feasible static_total toggle_total s word

theorem static_toggle_singleton_endpoints_differ :
    Trace static false [()] false ∧ ¬ Trace toggle false [()] false :=
  ⟨trace_singleton_iff.mpr (static_event false),
   fun h => toggle_always_changes (trace_singleton_iff.mp h) rfl⟩

theorem static_toggle_not_endpoint_trace_equivalent :
    ¬ ∀ s (word : List Unit) t, Trace static s word t ↔ Trace toggle s word t :=
  fun h => static_toggle_singleton_endpoints_differ.2
    ((h false [()] false).mp static_toggle_singleton_endpoints_differ.1)

theorem static_toggle_not_same_steps : ¬ ∀ s a t, static.step s a t ↔ toggle.step s a t :=
  fun h => static_toggle_not_endpoint_trace_equivalent (same_steps_iff_traces.mp h)

/-- **Forgetting endpoints loses the law**: the same words, different ends. -/
theorem word_feasibility_does_not_determine_endpoints :
    (∀ s (word : List Unit), Feasible static s word ↔ Feasible toggle s word) ∧
      Trace static false [()] false ∧ ¬ Trace toggle false [()] false :=
  ⟨static_toggle_same_feasible, static_toggle_singleton_endpoints_differ⟩

end Carriers

end Becoming
