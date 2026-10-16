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

* **One direction.** A property can be preserved by the ungated moves (holding before a step, it
  holds after: `PreservedBy`) or reflected by them (holding after, it held before: `ReflectedBy`).
  Keeping `q` is preserving, and equally reflecting, every value of it (`keptBy_iff_preserved`,
  `keptBy_iff_reflected`). Where the ungated moves preserve `p`, a course that leaves `p` contains
  a gated move (`leaving_passes_gate`), so `change_passes_gate` is its case `p := (q · = q s)`.
* **Every origin passes the gate.** Where the ungated moves reflect `p`, a course ending where
  `p` holds started where it held, or splits at a gated step after which `p` holds (`origin`). No
  decision of `p` is used: the gate is already decided. With the gate given as a proposition
  instead, the law holds exactly where each gate is decided (`origin_of_decides`), and asked of
  every process it is exactly double-negation elimination (`origin_of_propositions_iff`).

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

/-! ## One direction: preserved and reflected -/

/-- Every step by an ungated move preserves `p`: holding before the step, it holds after. -/
def PreservedBy (P : Process S A) (gate : A → Bool) (p : S → Prop) : Prop :=
  ∀ s a t, P.step s a t → gate a = false → p s → p t

/-- Every step by an ungated move reflects `p`: holding after the step, it held before. -/
def ReflectedBy (P : Process S A) (gate : A → Bool) (p : S → Prop) : Prop :=
  ∀ s a t, P.step s a t → gate a = false → p t → p s

/-- **Keeping a quantity is preserving every value of it.** -/
theorem keptBy_iff_preserved {P : Process S A} {gate : A → Bool} {q : S → R} :
    KeptBy P gate q ↔ ∀ c, PreservedBy P gate (fun s => q s = c) :=
  ⟨fun kept _ s a t step ungated holds => (kept s a t step ungated).trans holds,
   fun preserved s a t step ungated => preserved (q s) s a t step ungated rfl⟩

/-- **Keeping a quantity is reflecting every value of it.** -/
theorem keptBy_iff_reflected {P : Process S A} {gate : A → Bool} {q : S → R} :
    KeptBy P gate q ↔ ∀ c, ReflectedBy P gate (fun s => q s = c) :=
  ⟨fun kept _ s a t step ungated holds => (kept s a t step ungated).symm.trans holds,
   fun reflected s a t step ungated => (reflected (q t) s a t step ungated rfl).symm⟩

/-- A course of ungated moves preserves what every ungated step preserves. -/
theorem preserved_along {P : Process S A} {gate : A → Bool} {p : S → Prop}
    (preserved : PreservedBy P gate p) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → (∀ a, a ∈ plan → gate a = false) → p s → p t
  | _, _, [], .nil _, _, holds => holds
  | _, _, a :: _, .cons step tail, ungated, holds =>
    preserved_along preserved tail (fun b mem => ungated b (.tail a mem))
      (preserved _ _ _ step (ungated a (.head _)) holds)

/-- **A property is preserved along every course of ungated moves exactly when every ungated
step preserves it.** -/
theorem preserved_along_iff {P : Process S A} {gate : A → Bool} {p : S → Prop} :
    (∀ s plan t, Trace P s plan t → (∀ a, a ∈ plan → gate a = false) → p s → p t) ↔
      PreservedBy P gate p :=
  ⟨fun along s a t step ungated =>
    along s [a] t (.cons step (.nil t)) fun _ mem =>
      match mem with
      | .head _ => ungated,
   fun preserved _ _ _ path ungated => preserved_along preserved path ungated⟩

/-- A course of ungated moves reflects what every ungated step reflects. -/
theorem reflected_along {P : Process S A} {gate : A → Bool} {p : S → Prop}
    (reflected : ReflectedBy P gate p) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → (∀ a, a ∈ plan → gate a = false) → p t → p s
  | _, _, [], .nil _, _, holds => holds
  | _, _, a :: _, .cons step tail, ungated, holds =>
    reflected _ _ _ step (ungated a (.head _))
      (reflected_along reflected tail (fun b mem => ungated b (.tail a mem)) holds)

/-- **Leaving passes the gate**: where the ungated moves preserve `p`, a course from where `p`
holds to where it fails contains a gated move. -/
theorem leaving_passes_gate {P : Process S A} {gate : A → Bool} {p : S → Prop}
    (preserved : PreservedBy P gate p) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → p s → ¬ p t → ∃ a, a ∈ plan ∧ gate a = true
  | _, _, [], .nil _, holds, fails => absurd holds fails
  | _, _, a :: _, .cons step tail, holds, fails =>
    match gated : gate a with
    | true => ⟨a, .head _, gated⟩
    | false =>
      match leaving_passes_gate preserved tail (preserved _ _ _ step gated holds) fails with
      | ⟨b, mem, gatedB⟩ => ⟨b, .tail a mem, gatedB⟩

/-- **Every origin passes the gate**: where the ungated moves reflect `p`, a course ending where
`p` holds started where it held, or splits into a prefix, a gated step after which `p` holds, and
the rest. Nothing about `p` is decided. -/
theorem origin {P : Process S A} {gate : A → Bool} {p : S → Prop}
    (reflected : ReflectedBy P gate p) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → p t →
      p s ∨ ∃ pre a post m m', plan = pre ++ a :: post ∧ Trace P s pre m ∧
        P.step m a m' ∧ gate a = true ∧ p m' ∧ Trace P m' post t
  | _, _, [], .nil _, holds => .inl holds
  | s, _, a :: rest, .cons (m := m) step tail, holds =>
    match origin reflected tail holds with
    | .inr ⟨pre, b, post, n, n', split, path, stepB, gatedB, holdsB, rest'⟩ =>
      .inr ⟨a :: pre, b, post, n, n', congrArg (List.cons a) split, .cons step path, stepB, gatedB,
        holdsB, rest'⟩
    | .inl holdsM =>
      match gated : gate a with
      | true => .inr ⟨[], a, rest, s, m, rfl, .nil s, step, gated, holdsM, tail⟩
      | false => .inl (reflected _ _ _ step gated holdsM)

/-- **The origin law where each gate is decided.** With the gate a proposition, the law holds
wherever every move's gate holds or fails. -/
theorem origin_of_decides {P : Process S A} {gate : A → Prop} (decides : ∀ a, gate a ∨ ¬ gate a)
    {p : S → Prop} (reflected : ∀ s a t, P.step s a t → ¬ gate a → p t → p s) :
    ∀ {s t : S} {plan : List A}, Trace P s plan t → p t → p s ∨ ∃ a, a ∈ plan ∧ gate a
  | _, _, [], .nil _, holds => .inl holds
  | _, _, a :: _, .cons step tail, holds =>
    match origin_of_decides decides reflected tail holds with
    | .inr ⟨b, mem, gatedB⟩ => .inr ⟨b, .tail a mem, gatedB⟩
    | .inl holdsM =>
      match decides a with
      | .inl gatedA => .inr ⟨a, .head _, gatedA⟩
      | .inr ungated => .inl (reflected _ _ _ step ungated holdsM)

/-- **Asked of every process, the origin law with the gate a proposition is exactly
double-negation elimination.** The witness: one move from `false` to `true`, `p` holding at
`true`, and the gate `Q`. The move reflects `p` exactly where `Q` cannot fail, and the law then
gives `Q`. -/
theorem origin_of_propositions_iff :
    (∀ (S A : Type) (P : Process S A) (gate : A → Prop) (p : S → Prop),
      (∀ s a t, P.step s a t → ¬ gate a → p t → p s) →
      ∀ s plan t, Trace P s plan t → p t → p s ∨ ∃ a, a ∈ plan ∧ gate a) ↔
    ∀ Q : Prop, ¬ ¬ Q → Q :=
  ⟨fun law Q notNot =>
    match law Bool Unit ⟨fun s _ t => s = false ∧ t = true⟩ (fun _ => Q) (fun t => t = true)
        (fun _ _ _ _ fails _ => absurd fails notNot) false [()] true
        (.cons ⟨rfl, rfl⟩ (.nil true)) rfl with
    | .inl atFalse => nomatch atFalse
    | .inr ⟨_, _, holds⟩ => holds,
   fun eliminate _ _ _ _ _ reflected _ _ _ path holds =>
    origin_of_decides
      (fun _ => eliminate _ fun neither => neither (.inr fun g => neither (.inl g)))
      reflected path holds⟩

end Becoming.Gated
