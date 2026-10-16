import GenerativeCore

/-!
# The Becoming spine: one frame for the whole unfolding

The core `Generative.Process` declares admissible changes of configuration. A
`Frame` adds one thing: which claims are realized at each configuration. Claims
describe differentiated realizations and their relations, not independent owners.
Which claims count as living and further generation, as basic conditions or as
significant is not part of the frame; such readings and premises are stated over
it in later layers. Evaluation therefore has no world model of its own.

This module supplies the combinators that ethics and dynamics modules repeatedly
rebuilt: infinite runs, reachability, invariants and new realization. Every one is
defined through the core `Trace`, so results compose with the core's composition,
product and transport theorems. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

universe u v w

/-- One unfolding: a declared process and the claims realized at each configuration. -/
structure Frame (S : Type u) (A : Type v) (C : Type w) where
  P : Process S A
  realized : S → C → Prop

variable {S : Type u} {A : Type v} {C : Type w}

/-! ## Runs -/

/-- An infinite execution: every successive configuration is an admissible step. -/
structure Run (P : Process S A) where
  state : Nat → S
  act : Nat → A
  step : ∀ n, P.step (state n) (act n) (state (n + 1))

/-- The `k` actions of a run from time `n`. -/
def Run.window {P : Process S A} (r : Run P) : Nat → Nat → List A
  | _, 0 => []
  | n, k + 1 => r.act n :: r.window (n + 1) k

/-- Every finite window of a run is a core trace. -/
theorem Run.window_trace {P : Process S A} (r : Run P) :
    ∀ k n, Trace P (r.state n) (r.window n k) (r.state (n + k))
  | 0, n => .nil _
  | k + 1, n => by
    have shift : n + 1 + k = n + (k + 1) := (Nat.succ_add n k).trans (Nat.add_succ n k).symm
    exact .cons (r.step n) (shift ▸ Run.window_trace r k (n + 1))

/-! ## Reachability -/

/-- Some finite admissible path leads from `s` to `t`. -/
def Reach (P : Process S A) (s t : S) : Prop := ∃ as, Trace P s as t

theorem Reach.refl (P : Process S A) (s : S) : Reach P s s := ⟨[], .nil s⟩

theorem Reach.of_step {P : Process S A} {s t : S} {a : A} (h : P.step s a t) : Reach P s t :=
  ⟨[a], .cons h (.nil t)⟩

theorem Reach.trans {P : Process S A} {s m t : S} :
    Reach P s m → Reach P m t → Reach P s t
  | ⟨xs, hx⟩, ⟨ys, hy⟩ => ⟨xs ++ ys, trace_append_iff.mpr ⟨m, hx, hy⟩⟩

/-- A run reaches every later configuration from every earlier one. -/
theorem Run.reach {P : Process S A} (r : Run P) (n k : Nat) :
    Reach P (r.state n) (r.state (n + k)) :=
  ⟨r.window n k, r.window_trace k n⟩

/-! ## Invariants -/

/-- A property preserved by every admissible step. -/
def Invariant (P : Process S A) (I : S → Prop) : Prop :=
  ∀ s a t, P.step s a t → I s → I t

theorem Invariant.trace {P : Process S A} {I : S → Prop} (inv : Invariant P I)
    {s t : S} {as : List A} (h : Trace P s as t) : I s → I t := by
  induction h with
  | nil => exact id
  | cons step _ ih => exact fun held => ih (inv _ _ _ step held)

theorem Invariant.reach {P : Process S A} {I : S → Prop} (inv : Invariant P I)
    {s t : S} : Reach P s t → I s → I t
  | ⟨_, h⟩ => inv.trace h

theorem Invariant.run {P : Process S A} {I : S → Prop} (inv : Invariant P I)
    (r : Run P) (start : I (r.state 0)) : ∀ n, I (r.state n)
  | 0 => start
  | n + 1 => inv _ _ _ (r.step n) (inv.run r start n)

/-! ## New realization -/

/-- A claim of the given reading realized at `t` and not recorded as realized
before. Following the core convention, the configuration retains whatever history
the question needs, so `before` is an observable of the configuration itself. -/
def Novel (F : Frame S A C) (reading : C → Prop) (before : S → C → Prop) (t : S) : Prop :=
  ∃ c, reading c ∧ F.realized t c ∧ ¬ before t c

/-- Novelty is monotone in the reading. -/
theorem Novel.mono {F : Frame S A C} {reading reading' : C → Prop} {before : S → C → Prop}
    {t : S} (sub : ∀ c, reading c → reading' c) : Novel F reading before t → Novel F reading' before t
  | ⟨c, read, real, fresh⟩ => ⟨c, sub c read, real, fresh⟩

end Becoming
