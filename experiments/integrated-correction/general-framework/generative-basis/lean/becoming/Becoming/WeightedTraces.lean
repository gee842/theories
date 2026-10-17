import Becoming.Weighted

/-!
# Weighted traces: integrating out and memory, on the traces of processes

`Becoming.Weighted` states that integrating out through a description is exact at every horizon
exactly where it is exact at one step (`Weights.lumped_iff`), for every weighting of steps; that
the possibility weights reading a process's steps are the core's relation of traces
(`possibility_transfer_iff`); and that a weighting with memory is not a weighting of steps of the
configurations it is given on (`Memory.not_of_steps`) but is one on configurations that keep what
it needs (`Memory.of_kept`). This module states these on processes of the spine.

* **Lumpability of a process.** With every move and configuration listed and a representative of
  each value of the description `π`, whether some trace of `n` moves from a configuration reaches
  one whose description meets `g` depends only on the description of the start, for every `n`
  and `g`, exactly where it does for one move (`lumped_iff`): the possibility form of
  `carries_law_iff` on a process of the spine.
* **Memory is kept in the configuration.** No process on one configuration whose steps are read by
  possibility weights has as its courses of two moves exactly those whose second move differs from
  the first (`memory_not_steps`); the law on configurations keeping the last move (`keptLaw`) has
  exactly those (`kept_traces`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace WeightedTraces

universe u v x

/-- Two values that hold together are one. -/
theorem bool_eq_of_iff : ∀ {b c : Bool}, (b = true ↔ c = true) → b = c
  | true, true, _ => rfl
  | true, false, h => Bool.noConfusion (h.mp rfl)
  | false, true, h => Bool.noConfusion (h.mpr rfl)
  | false, false, _ => rfl

variable {S : Type u} {A : Type v} {K : Type x}

/-- Some trace of `n` moves of `P` from `s` reaches a configuration whose description meets `g`. -/
def Reaches (P : Process S A) (π : S → K) (g : K → Bool) (n : Nat) (s : S) : Prop :=
  ∃ as t, as.length = n ∧ Trace P s as t ∧ g (π t) = true

/-- **Integrating out a process's courses is exact at every number of moves exactly where it is
exact at one.** Where the possibility weights `step` read the steps of `P`, every move and
configuration is listed, and each value of the description has a representative, what the traces
reach through the description depends only on the description of the start for every number of
moves exactly where it does for one move. -/
theorem lumped_iff (P : Process S A) (step : S → A → S → Bool)
    (reads : ∀ s a t, step s a t = true ↔ P.step s a t) (moves : List A) (all : List S)
    (every_move : ∀ a, a ∈ moves) (every : ∀ s, s ∈ all) (π : S → K) (rep : K → S)
    (represents : ∀ k, π (rep k) = k) :
    (∀ n (g : K → Bool) s s', π s = π s' → (Reaches P π g n s ↔ Reaches P π g n s')) ↔
      ∀ (g : K → Bool) s s', π s = π s' → (Reaches P π g 1 s ↔ Reaches P π g 1 s') :=
  have reach : ∀ n (g : K → Bool) s,
      possibility.transfer step moves all (fun m => g (π m)) n s = true ↔ Reaches P π g n s :=
    fun n _ s => possibility_transfer_iff P step reads moves all every_move every _ n s
  have conv : ∀ n (g : K → Bool) s s',
      possibility.transfer step moves all (fun m => g (π m)) n s =
          possibility.transfer step moves all (fun m => g (π m)) n s' ↔
        (Reaches P π g n s ↔ Reaches P π g n s') :=
    fun n g s s' =>
      ⟨fun same => (reach n g s).symm.trans
          ((Eq.to_iff (congrArg (· = true) same)).trans (reach n g s')),
       fun iff => bool_eq_of_iff ((reach n g s).trans (iff.trans (reach n g s').symm))⟩
  have lumped := Weights.lumped_iff (W := possibility) step moves all π rep represents
  ⟨fun every_n g s s' same =>
    (conv 1 g s s').mp
      (lumped.mp (fun n g s s' same => (conv n g s s').mpr (every_n n g s s' same)) g s s' same),
   fun one n g s s' same =>
    (conv n g s s').mp
      (lumped.mpr (fun g s s' same => (conv 1 g s s').mpr (one g s s' same)) n g s s' same)⟩

/-! ## Memory is kept in the configuration -/

/-- **No process on one configuration, its steps read by possibility weights, has as its courses
of two moves exactly those whose second move differs from the first.** -/
theorem memory_not_steps :
    ¬ ∃ (P : Process Unit Bool) (step : Unit → Bool → Unit → Bool),
      (∀ s a t, step s a t = true ↔ P.step s a t) ∧
        ∀ a b, (Trace P () [a, b] () ↔ Memory.differ a b = true) :=
  fun ⟨_, step, reads, traces⟩ =>
    Memory.not_of_steps step (fun _ => true) fun a b => bool_eq_of_iff
      ⟨fun along => match bool_of_and_true along with
        | ⟨first, rest⟩ => (traces a b).mp
            (.cons ((reads _ _ _).mp first)
              (.cons ((reads _ _ _).mp (bool_of_and_true rest).1) (.nil ()))),
       fun differs => match trace_cons_iff.mp ((traces a b).mpr differs) with
        | ⟨(), first, rest⟩ => match trace_cons_iff.mp rest with
          | ⟨(), second, _⟩ =>
            bool_and_true ((reads _ _ _).mpr first) (bool_and_true ((reads _ _ _).mpr second) rfl)⟩

/-- The law on configurations keeping the last move: a move lands where it is kept and differs
from the move kept before. -/
def keptLaw : Process (Option Bool) Bool := ⟨fun last a next => Memory.kept last a next = true⟩

theorem lands_eq : ∀ {m : Option Bool} {a : Bool}, Memory.lands m a = true → m = some a
  | some true, true, _ => rfl
  | some false, false, _ => rfl
  | some true, false, h => Bool.noConfusion h
  | some false, true, h => Bool.noConfusion h
  | none, _, h => Bool.noConfusion h

/-- **On configurations keeping the last move, the courses of two moves from none are exactly
those whose second move differs from the first.** -/
theorem kept_traces (a b : Bool) :
    Trace keptLaw none [a, b] (some b) ↔ Memory.differ a b = true :=
  ⟨fun path => match trace_cons_iff.mp path with
    | ⟨m, first, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨m', second, last⟩ =>
        have at_m : m = some a := lands_eq (bool_of_and_true first).1
        have at_m' : m' = some b := (trace_nil_iff.mp last)
        have first' : Memory.kept none a (some a) = true :=
          Eq.subst (motive := fun x => Memory.kept none a x = true) at_m first
        have second' : Memory.kept (some a) b (some b) = true :=
          Eq.subst (motive := fun x => Memory.kept x b (some b) = true) at_m
            (Eq.subst (motive := fun y => Memory.kept m b y = true) at_m' second)
        (Memory.of_kept a b).symm.trans (bool_and_true first' (bool_and_true second' rfl)),
   fun differs =>
    have along := (Memory.of_kept a b).trans differs
    match bool_of_and_true along with
    | ⟨first, rest⟩ => .cons first (.cons (bool_of_and_true rest).1 (.nil _))⟩

end WeightedTraces

end Becoming
