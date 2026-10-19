import Becoming.Weighted
import Becoming.Decidedness
import Becoming.JointPlans

/-!
# List footprints: a plan is realized exactly where what its leaves draw on is supported

`Becoming.Composition` shows that exclusive footprints support every leaf
(`JointPlan.supports_of_realizes`): where each part's footprint lies within its whole's and the
two parts' footprints share nothing, what the leaves of a realized plan draw on repeats nothing
and lies within the root's footprint. This module gives the instance where the converse holds.

A configuration is a list, its footprint its members (`support`), and a whole holds two parts
where each part's members are members of the whole and the parts share none (`joint`). The
footprint laws hold (`parts_within`, `parts_apart`), and a plan is realized at a list exactly where
the list supports what the plan's leaves draw on (`realizes_iff_supports`). Realization therefore
reads only what the leaves draw on: plans drawing on the same list (`realizes_iff_of_draws`), on
lists reassociated (`realizes_reassociate`) or reordered (`realizes_iff_of_perm`) are realized at
the same lists. Repetition is kept: a list drawing on one member twice is supported nowhere.

Every declaration's axiom report is empty. Ported from `Generative.ExplanatoryFootprints`
(bridge fold F3E, 18 October 2026); the port is a restatement on the core's plans, not a new
result.
-/

universe u

namespace Becoming

namespace ListFootprints

variable {R : Type u}

/-- A list's footprint: its members. -/
def support (s : List R) (a : R) : Prop := a ∈ s

/-- A whole holds two parts where the members of each are members of the whole and the parts
share none. -/
def joint (s l r : List R) : Prop :=
  (∀ a, a ∈ l → a ∈ s) ∧ (∀ a, a ∈ r → a ∈ s) ∧ ∀ a, a ∈ l → a ∈ r → False

/-- **Each part's footprint lies within its whole's.** -/
theorem parts_within : PartsWithin (@support R) joint :=
  fun _ _ _ held => ⟨held.1, held.2.1⟩

/-- **The two parts' footprints share nothing.** -/
theorem parts_apart : PartsApart (@support R) joint :=
  fun _ _ _ held => held.2.2

/-- A list repeating nothing repeats nothing in either piece, and its pieces share no member. -/
theorem nodup_split : ∀ {l m : List R}, (l ++ m).Nodup →
    l.Nodup ∧ m.Nodup ∧ ∀ a, a ∈ l → a ∈ m → False
  | [], _, distinct => ⟨.nil, distinct, fun _ mem => nomatch mem⟩
  | a :: l, m, distinct => by
    cases distinct with
    | cons fresh rest =>
      match nodup_split rest with
      | ⟨left, right, apart⟩ =>
        refine ⟨.cons (fun b mem => fresh b (mem_appended_left m mem)) left, right, ?_⟩
        intro b mem mem'
        cases mem with
        | head => exact fresh a (mem_appended_right mem' l) rfl
        | tail _ inside => exact apart b inside mem'

/-- Reordering keeps a list free of repetition. -/
theorem nodup_of_perm {l l' : List R} (perm : l.Perm l') (distinct : l.Nodup) : l'.Nodup := by
  induction perm with
  | nil => exact distinct
  | cons x perm ih =>
    cases distinct with
    | cons fresh rest => exact .cons (fun b mem => fresh b (Coverage.Perm.mem perm mem)) (ih rest)
  | swap x y l =>
    cases distinct with
    | cons freshY rest =>
      cases rest with
      | cons freshX rest =>
        refine .cons (fun b mem => ?_) (.cons (fun b mem => freshY b (.tail x mem)) rest)
        cases mem with
        | head => exact fun same => freshY x (.head l) same.symm
        | tail _ inside => exact freshX b inside
  | trans _ _ ih ih' => exact ih' (ih distinct)

/-- **Where a list supports what a plan's leaves draw on, the list realizes the plan**: it holds
the two lists the sides draw on, which share no member. -/
theorem realizes_of_supports :
    ∀ (p : JointPlan (List R)) (s : List R), Supports support s p.draws →
      JointPlan.Realizes joint (Supports support) s p
  | .leaf _, _, supported => supported
  | .pair p q, _, ⟨distinct, within⟩ =>
    match nodup_split distinct with
    | ⟨left, right, apart⟩ =>
      ⟨p.draws, q.draws,
       ⟨fun a mem => within a (mem_appended_left q.draws mem),
        fun a mem => within a (mem_appended_right mem p.draws), apart⟩,
       realizes_of_supports p p.draws ⟨left, fun _ mem => mem⟩,
       realizes_of_supports q q.draws ⟨right, fun _ mem => mem⟩⟩

/-- **A list realizes a plan exactly where it supports what the plan's leaves draw on.** -/
theorem realizes_iff_supports (p : JointPlan (List R)) (s : List R) :
    JointPlan.Realizes joint (Supports support) s p ↔ Supports support s p.draws :=
  ⟨JointPlan.supports_of_realizes parts_within parts_apart p s, realizes_of_supports p s⟩

/-- **Plans drawing on the same list are realized at the same lists.** -/
theorem realizes_iff_of_draws (p q : JointPlan (List R)) (s : List R) (same : p.draws = q.draws) :
    JointPlan.Realizes joint (Supports support) s p ↔ JointPlan.Realizes joint (Supports support) s q :=
  (realizes_iff_supports p s).trans
    ((Eq.subst (motive := fun xs => Supports support s p.draws ↔ Supports support s xs) same
      Iff.rfl).trans (realizes_iff_supports q s).symm)

/-- **Reassociating a plan keeps where it is realized.** -/
theorem realizes_reassociate (p q r : JointPlan (List R)) (s : List R) :
    JointPlan.Realizes joint (Supports support) s (.pair (.pair p q) r) ↔
      JointPlan.Realizes joint (Supports support) s (.pair p (.pair q r)) :=
  realizes_iff_of_draws _ _ s (ListTests.append_assoc p.draws q.draws r.draws)

/-- **Plans drawing on reorderings of one list are realized at the same lists.** -/
theorem realizes_iff_of_perm (p q : JointPlan (List R)) (s : List R)
    (perm : p.draws.Perm q.draws) :
    JointPlan.Realizes joint (Supports support) s p ↔ JointPlan.Realizes joint (Supports support) s q :=
  (realizes_iff_supports p s).trans
    (Iff.trans
      ⟨fun ⟨distinct, within⟩ => ⟨nodup_of_perm perm distinct,
          fun a mem => within a (Coverage.Perm.mem perm mem)⟩,
       fun ⟨distinct, within⟩ => ⟨nodup_of_perm perm.symm distinct,
          fun a mem => within a (Coverage.Perm.mem perm.symm mem)⟩⟩
      (realizes_iff_supports q s).symm)

end ListFootprints

end Becoming
