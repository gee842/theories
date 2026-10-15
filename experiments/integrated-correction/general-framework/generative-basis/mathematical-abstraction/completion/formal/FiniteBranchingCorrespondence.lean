import Becoming.Lasting
import FiniteBranching

/-!
# Finite-branching lifting as an instance of lasting some course

`FiniteBranching` lifts courses of every length to an infinite path where a relation branches
finitely. A relation is the process with one move whose steps are its pairs (`process`), and
there:
* `Reach` is the core's `Lasting.Continues` and `Unbounded` its `Lasting.Unbounded`
  (`reach_iff_continues`, `unbounded_iff`), and listed children make the process finitely
  branching (`finitelyBranching`);
* classical reasoning gives the core's `EitherThroughout` (`either_classical`), so the core's
  `EitherThroughout.list` gives `finite_unbounded` (`finite_unbounded_by_core`) and its
  `Lasting.Unbounded.step_of_either` gives `unbounded_child` (`unbounded_child_by_core`);
* Lean's choice selects an unbounded successor wherever one exists, so the core's `Lasting.lifting`
  gives `infinite_from_unbounded` (`infinite_from_unbounded_by_core`), and with
  `Lasting.unbounded_start_of_either`, `finite_initial_lifting` and `labelled_lifting`
  (`finite_initial_lifting_by_core`, `labelled_lifting_by_core`).

The core states what each step needs: with no premise an unbounded configuration cannot fail to
have an unbounded successor (`Lasting.Unbounded.step_not_not`); that it has one is, asked of every
finitely branching process, exactly `EitherThroughout` (`Lasting.step_iff_either`); and a run
needs a selection. `FiniteBranching`'s definitions and statements are unchanged.
-/

namespace Becoming.FiniteBranchingCorrespondence

open CompletionLifting

universe u v

variable {α : Type u}

/-- A relation as the process with one move. -/
def process (R : α → α → Prop) : Generative.Process α Unit :=
  ⟨fun a _ b => R a b⟩

theorem reach_iff_continues (R : α → α → Prop) :
    ∀ (n : Nat) (a : α), CompletionLifting.Reach R a n ↔ Lasting.Continues (process R) n a
  | 0, _ => ⟨fun _ => trivial, fun _ => trivial⟩
  | n + 1, _ =>
    ⟨fun ⟨b, step, reach⟩ => ⟨(), b, step, (reach_iff_continues R n b).mp reach⟩,
     fun ⟨_, b, step, onward⟩ => ⟨b, step, (reach_iff_continues R n b).mpr onward⟩⟩

theorem unbounded_iff (R : α → α → Prop) (a : α) :
    CompletionLifting.Unbounded R a ↔ Lasting.Unbounded (process R) a :=
  ⟨fun unbounded n => (reach_iff_continues R n a).mp (unbounded n),
   fun unbounded n => (reach_iff_continues R n a).mpr (unbounded n)⟩

/-- Listed children make the process finitely branching. -/
theorem finitelyBranching (R : α → α → Prop) (children : α → List α)
    (enumerates : ∀ a b, R a b ↔ b ∈ children a) : Lasting.FinitelyBranching (process R) :=
  fun a => ⟨children a, fun b => ⟨fun ⟨_, step⟩ => (enumerates a b).mp step,
    fun mem => ⟨(), (enumerates a b).mpr mem⟩⟩⟩

/-- Classical reasoning gives the core's `EitherThroughout`. -/
theorem either_classical : EitherThroughout :=
  EitherThroughout.of_em fun p => Classical.em p

/-- **`finite_unbounded` from the core**: `EitherThroughout.list`, with every candidate's depth
decided classically. -/
theorem finite_unbounded_by_core (L : List α) (F : α → Nat → Prop)
    (down : ∀ a m n, m ≤ n → F a n → F a m) (allDepths : ∀ n, ∃ a, a ∈ L ∧ F a n) :
    ∃ a, a ∈ L ∧ ∀ n, F a n :=
  EitherThroughout.list either_classical (P := fun n a => F a n) (fun _ _ => Classical.em _)
    (fun k a => down a k (k + 1) (Nat.le_succ k)) L allDepths

/-- **`unbounded_child` from the core**: `Lasting.Unbounded.step_of_either`. -/
theorem unbounded_child_by_core (R : α → α → Prop) (children : α → List α)
    (enumerates : ∀ a b, R a b ↔ b ∈ children a) (a : α) (ha : CompletionLifting.Unbounded R a) :
    ∃ b, R a b ∧ CompletionLifting.Unbounded R b :=
  match Lasting.Unbounded.step_of_either either_classical (finitelyBranching R children enumerates)
      ((unbounded_iff R a).mp ha) with
  | ⟨b, ⟨_, step⟩, unbounded⟩ => ⟨b, step, (unbounded_iff R b).mpr unbounded⟩

/-- **`infinite_from_unbounded` from the core**: `Lasting.lifting`, with `EitherThroughout` classical
and Lean's choice selecting an unbounded successor wherever one exists. -/
theorem infinite_from_unbounded_by_core (R : α → α → Prop) (children : α → List α)
    (enumerates : ∀ a b, R a b ↔ b ∈ children a) (a : α) (ha : CompletionLifting.Unbounded R a) :
    ∃ path : Nat → α, path 0 = a ∧ ∀ n, R (path n) (path (n + 1)) :=
  match Lasting.lifting either_classical (finitelyBranching R children enumerates)
      (fun _ exists_ => ⟨((), Classical.choose exists_), match Classical.choose_spec exists_ with
        | ⟨⟨_, step⟩, unbounded⟩ => ⟨step, unbounded⟩⟩)
      ((unbounded_iff R a).mp ha) with
  | ⟨r, start, _⟩ => ⟨r.state, start, r.step⟩

/-- **`finite_initial_lifting` from the core**: `Lasting.unbounded_start_of_either`, then the
lifting. -/
theorem finite_initial_lifting_by_core (R : α → α → Prop) (initial : List α)
    (children : α → List α) (enumerates : ∀ a b, R a b ↔ b ∈ children a)
    (arbitraryDepth : ∀ n, ∃ a, a ∈ initial ∧ CompletionLifting.Reach R a n) :
    ∃ path : Nat → α, path 0 ∈ initial ∧ ∀ n, R (path n) (path (n + 1)) :=
  match Lasting.unbounded_start_of_either either_classical (finitelyBranching R children enumerates)
      initial (fun n => match arbitraryDepth n with
        | ⟨a, mem, reach⟩ => ⟨a, mem, (reach_iff_continues R n a).mp reach⟩) with
  | ⟨a, mem, unbounded⟩ =>
    match infinite_from_unbounded_by_core R children enumerates a ((unbounded_iff R a).mpr unbounded) with
    | ⟨path, start, steps⟩ => ⟨path, start ▸ mem, steps⟩

/-- **`labelled_lifting` from the core**: the clocked relation `RequestedStep` branches finitely,
and `finite_initial_lifting_by_core` lifts it. -/
theorem labelled_lifting_by_core {σ : Type v} (step : α → σ → α → Prop) (word : Nat → σ)
    (initial : List α) (children : α → σ → List α)
    (enumerates : ∀ a label b, step a label b ↔ b ∈ children a label)
    (arbitraryDepth : ∀ n, ∃ a, a ∈ initial ∧ CompletionLifting.Reach (RequestedStep step word) (0, a) n) :
    ∃ path : Nat → α, path 0 ∈ initial ∧ ∀ n, step (path n) (word n) (path (n + 1)) := by
  let roots : List (Nat × α) := initial.map (fun a => (0, a))
  let nexts : (Nat × α) → List (Nat × α) := fun p =>
    (children p.2 (word p.1)).map (fun a => (p.1 + 1, a))
  have hen : ∀ p q, RequestedStep step word p q ↔ q ∈ nexts p := by
    intro p q
    constructor
    · rintro ⟨ht, he⟩
      exact List.mem_map.mpr ⟨q.2, (enumerates _ _ _).mp he, Prod.ext ht.symm rfl⟩
    · intro h
      obtain ⟨a, ha, hq⟩ := List.mem_map.mp h
      cases hq
      exact ⟨rfl, (enumerates _ _ _).mpr ha⟩
  have harb : ∀ n, ∃ p, p ∈ roots ∧ CompletionLifting.Reach (RequestedStep step word) p n := by
    intro n
    obtain ⟨a, ha, hr⟩ := arbitraryDepth n
    exact ⟨(0, a), List.mem_map.mpr ⟨a, ha, rfl⟩, hr⟩
  obtain ⟨path, hroot, hedge⟩ :=
    finite_initial_lifting_by_core (RequestedStep step word) roots nexts hen harb
  obtain ⟨a, ha, hzero⟩ := List.mem_map.mp hroot
  have clock : ∀ n, (path n).1 = n := by
    intro n
    induction n with
    | zero => exact congrArg Prod.fst hzero.symm
    | succ n ih => exact (hedge n).1.trans (congrArg (fun k => k + 1) ih)
  refine ⟨fun n => (path n).2, ?_, ?_⟩
  · have hs := congrArg Prod.snd hzero
    change (path 0).2 ∈ initial
    rw [← hs]
    exact ha
  · intro n
    have hh := (hedge n).2
    rw [clock] at hh
    exact hh

end Becoming.FiniteBranchingCorrespondence
