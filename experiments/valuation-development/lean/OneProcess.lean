/-
  One process: the study's splits as cuts of a single unfolding.

  7 October 2026. AI-authored formal companion to §19 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module; it changes no verified source. Core Lean 4 only.

  The study wrote `Org` (selection and retention) beside `World` (consequence law),
  and in §14 two organizations beside each other. Those are ways of reading one
  process, not two kinds of thing. This module proves it:
  - an organization with its consequence law is one `Process` of the shared core,
    and its history is a `Trace` of that process;
  - two interacting organizations are one organization on their joint state, whose
    only presented input is what both meet; nothing is outside the pair;
  - cutting the joint process at either center recovers a single organization whose
    "world" is the other's actual activity. The same run is read from either cut, and
    the reduction to a fixed other (`fixed_other_reduces`) is the special case where
    the other's activity does not vary.
-/
import ValuationRenewal

namespace ValuationDevelopment

open Generative

/-! ## An organization with its consequence law is one process -/

/-- The single process an organization and its consequence law make together. -/
def Org.process {M X A C : Type} (o : Org M X A C) (w : World X A C) : Process M X where
  step m x m' := m' = o.next w m x

/-- Every history of the organization is a trace of that one process. -/
theorem run_is_trace {M X A C : Type} (o : Org M X A C) (w : World X A C) :
    ∀ (xs : List X) (m : M), Trace (o.process w) m xs (o.run w m xs) := by
  intro xs
  induction xs with
  | nil => intro m; exact .nil m
  | cons x xs ih => intro m; exact .cons rfl (ih (o.next w m x))

/-- And the process is deterministic: a trace ends where the run ends. -/
theorem trace_is_run {M X A C : Type} (o : Org M X A C) (w : World X A C)
    {m t : M} {xs : List X} (h : Trace (o.process w) m xs t) : t = o.run w m xs := by
  induction h with
  | nil => rfl
  | cons hs _ ih => rw [ih, hs]; rfl

/-! ## Two interacting organizations are one organization -/

/-- The pair as one organization on the joint state. -/
def jointOrg {M X A C : Type} (o₁ o₂ : Org M X A C) : Org (M × M) X (A × A) (C × C) where
  select s x := (o₁.select s.1 x, o₂.select s.2 x)
  retain s x a c := (o₁.retain s.1 x a.1 c.1, o₂.retain s.2 x a.2 c.2)

/-- The joint consequence law: each center meets what both selections together yield. -/
def jointWorld {X A C : Type} (rel : A → A → C) : World X (A × A) (C × C) :=
  fun _ a => (rel a.1 a.2, rel a.2 a.1)

/-- Interaction is one process: the paired history is the history of the joint
organization, whose only input is what both meet. -/
theorem pair_is_one_process {M X A C : Type} (o₁ o₂ : Org M X A C) (rel : A → A → C) :
    ∀ (xs : List X) (s : M × M), pairRun o₁ o₂ rel s xs = (jointOrg o₁ o₂).run (jointWorld rel) s xs := by
  intro xs
  induction xs with
  | nil => intro s; rfl
  | cons x xs ih => intro s; simp only [pairRun]; rw [ih]; rfl

/-! ## Each center's "world" is a cut of the joint process -/

/-- An organization reading a presented condition enriched with another's selection. -/
def Org.cut {M X A C : Type} (o : Org M X A C) : Org M (X × A) A C where
  select m xa := o.select m xa.1
  retain m xa a c := o.retain m xa.1 a c

/-- What a center meets at a cut: the relation of its selection to the other's. -/
def cutWorld {X A C : Type} (rel : A → A → C) : World (X × A) A C := fun xa a => rel a xa.2

/-- The other center's actual selections along the joint history, as seen from the
first center's cut. -/
def otherActs {M X A C : Type} (o₁ o₂ : Org M X A C) (rel : A → A → C) : M × M → List X → List (X × A)
  | _, [] => []
  | s, x :: xs => (x, o₂.select s.2 x) :: otherActs o₁ o₂ rel ((jointOrg o₁ o₂).next (jointWorld rel) s x) xs

/-- The same, as seen from the second center's cut. -/
def firstActs {M X A C : Type} (o₁ o₂ : Org M X A C) (rel : A → A → C) : M × M → List X → List (X × A)
  | _, [] => []
  | s, x :: xs => (x, o₁.select s.1 x) :: firstActs o₁ o₂ rel ((jointOrg o₁ o₂).next (jointWorld rel) s x) xs

/-- **Cut at the first center.** Its part of the joint history is the run of a single
organization whose consequence law is its relation to the other's actual activity. -/
theorem cut_first {M X A C : Type} (o₁ o₂ : Org M X A C) (rel : A → A → C) :
    ∀ (xs : List X) (s : M × M),
      (pairRun o₁ o₂ rel s xs).1 = o₁.cut.run (cutWorld rel) s.1 (otherActs o₁ o₂ rel s xs) := by
  intro xs
  induction xs with
  | nil => intro s; rfl
  | cons x xs ih =>
    intro s
    exact ih ((jointOrg o₁ o₂).next (jointWorld rel) s x)

/-- **Cut at the second center.** The same joint history read from the other side. -/
theorem cut_second {M X A C : Type} (o₁ o₂ : Org M X A C) (rel : A → A → C) :
    ∀ (xs : List X) (s : M × M),
      (pairRun o₁ o₂ rel s xs).2 = o₂.cut.run (cutWorld rel) s.2 (firstActs o₁ o₂ rel s xs) := by
  intro xs
  induction xs with
  | nil => intro s; rfl
  | cons x xs ih =>
    intro s
    exact ih ((jointOrg o₁ o₂).next (jointWorld rel) s x)

/-- **Neither cut is privileged.** Both centers' histories are read off the one
joint history; each one's "world" is the other's activity in relation to its own. -/
theorem both_cuts_one_history {M X A C : Type} (o₁ o₂ : Org M X A C) (rel : A → A → C)
    (xs : List X) (s : M × M) :
    (jointOrg o₁ o₂).run (jointWorld rel) s xs =
      (o₁.cut.run (cutWorld rel) s.1 (otherActs o₁ o₂ rel s xs),
       o₂.cut.run (cutWorld rel) s.2 (firstActs o₁ o₂ rel s xs)) := by
  rw [← pair_is_one_process, ← cut_first, ← cut_second]

end ValuationDevelopment
