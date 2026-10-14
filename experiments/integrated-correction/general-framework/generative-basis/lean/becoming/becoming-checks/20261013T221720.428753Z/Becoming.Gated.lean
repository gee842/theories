import Becoming.Frame

/-!
# Gated change: what only a class of moves can change

A class of moves is marked by `gate : A → Bool`. A quantity `q` of configurations is kept by the
ungated moves where every step by an ungated move leaves it as it was (`KeptBy`). This module
states, for every process, what that local condition gives along courses.

* **Kept along every ungated course exactly when kept by every ungated step**
  (`kept_along_iff`). The condition concerns single steps; the conclusion every finite course.
* **Every change passes the gate.** Where the ungated moves keep `q`, a course that changes `q`
  contains a gated move (`change_passes_gate`); with equality of values decided, the course
  splits at a gated step that itself changes `q` (`change_located`).

The gate does not say that a gated move changes anything; it locates where change can enter.
No premise is added; every declaration has an empty axiom report.
-/

namespace Becoming.Gated

open Generative

universe u v w

variable {S : Type u} {A : Type v} {R : Type w}

/-- Every step by an ungated move keeps `q`. -/
def KeptBy (P : Process S A) (gate : A → Bool) (q : S → R) : Prop :=
  ∀ s a t, P.step s a t → gate a = false → q t = q s

/-- A course of ungated moves keeps what every ungated step keeps. -/
theorem kept_along {P : Process S A} {gate : A → Bool} {q : S → R} (kept : KeptBy P gate q) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → (∀ a, a ∈ plan → gate a = false) → q t = q s
  | _, _, [], .nil _, _ => rfl
  | _, _, a :: _, .cons step tail, ungated =>
    (kept_along kept tail fun b mem => ungated b (.tail a mem)).trans
      (kept _ _ _ step (ungated a (.head _)))

/-- **A quantity is kept along every course of ungated moves exactly when every ungated step
keeps it.** -/
theorem kept_along_iff {P : Process S A} {gate : A → Bool} {q : S → R} :
    (∀ s plan t, Trace P s plan t → (∀ a, a ∈ plan → gate a = false) → q t = q s) ↔
      KeptBy P gate q :=
  ⟨fun along s a t step ungated =>
    along s [a] t (.cons step (.nil t)) fun _ mem =>
      match mem with
      | .head _ => ungated,
   fun kept _ _ _ path ungated => kept_along kept path ungated⟩

/-- **Every change passes the gate**: where the ungated moves keep `q`, a course that changes it
contains a gated move. -/
theorem change_passes_gate {P : Process S A} {gate : A → Bool} {q : S → R}
    (kept : KeptBy P gate q) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → q t ≠ q s → ∃ a, a ∈ plan ∧ gate a = true
  | _, _, [], .nil _, changed => absurd rfl changed
  | _, _, a :: _, .cons step tail, changed =>
    match gated : gate a with
    | true => ⟨a, .head _, gated⟩
    | false =>
      match change_passes_gate kept tail fun same =>
          changed (same.trans (kept _ _ _ step gated)) with
      | ⟨b, mem, gatedB⟩ => ⟨b, .tail a mem, gatedB⟩

/-- **The change is located at a gated step.** With equality of values decided, a course that
changes `q` splits into a prefix keeping it, a gated step changing it, and the rest. -/
theorem change_located [DecidableEq R] {P : Process S A} {gate : A → Bool} {q : S → R}
    (kept : KeptBy P gate q) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → q t ≠ q s →
      ∃ pre a post m m', plan = pre ++ a :: post ∧ Trace P s pre m ∧ q m = q s ∧
        P.step m a m' ∧ gate a = true ∧ q m' ≠ q m ∧ Trace P m' post t
  | _, _, [], .nil _, changed => absurd rfl changed
  | s, _, a :: rest, .cons (m := m) step tail, changed =>
    match decEq (q m) (q s) with
    | isFalse moved =>
      match gated : gate a with
      | true => ⟨[], a, rest, s, m, rfl, .nil s, rfl, step, gated, moved, tail⟩
      | false => absurd (kept _ _ _ step gated) moved
    | isTrue same =>
      match change_located kept tail fun same' => changed (same'.trans same) with
      | ⟨pre, b, post, n, n', split, path, keep, stepB, gatedB, movedB, rest'⟩ =>
        ⟨a :: pre, b, post, n, n', congrArg (List.cons a) split, .cons step path,
         keep.trans same, stepB, gatedB, movedB, rest'⟩

end Becoming.Gated
