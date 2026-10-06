import GenerativeCore
import SupportNecessity

/-!
# Renewal and closure: late activity descends from a realized closure

Phase 1 of the renewal–closure roadmap. An organized kind that occurs at a
positive time needs an earlier occurrence, still able to support it, of a kind
with a support edge to it. No organization arrives from outside after time zero;
raw flows are not represented here and may remain external.

With finitely many kinds and a bound on how long an occurrence can support, any
occurrence late enough descends from a cycle of support kinds, and every kind on
that cycle actually occurred within the recent window. The cycle's kinds form a
closed set in the sense of Montévil and Mossio (2015): each depends on a member
and each supports a member. Acyclic support therefore has a deadline without a
supplied rank, which closes the gap that `SupportNecessity` states.

Kinds, edges and support reach are supplied inputs. Nothing here says which
history occurs or that continuation is favorable.
-/

namespace Generative.Conditional.Renewal

open Generative Generative.Conditional.Support

universe u v

/-- Occurrences of organized kinds in time. Each positive-time occurrence is
supported by an earlier occurrence that can still support it. Both episode
systems and token-count histories give instances. -/
structure OccurrenceSupport (Kind : Type u) where
  occurs : Kind → Nat → Prop
  edge : Kind → Kind → Prop
  reach : Kind → Nat
  support : ∀ k t, occurs k t → 0 < t →
    ∃ j s, edge j k ∧ occurs j s ∧ s < t ∧ t ≤ s + reach j

variable {Kind : Type u}

/-- A walk through support edges that lists every visited kind, both ends
included. -/
inductive Walk (edge : Kind → Kind → Prop) : Kind → List Kind → Kind → Prop where
  | nil (k : Kind) : Walk edge k [k] k
  | cons {i j k : Kind} {vs : List Kind} :
      edge i j → Walk edge j vs k → Walk edge i (i :: vs) k

theorem Walk.snoc {edge : Kind → Kind → Prop} {i j k : Kind} {vs : List Kind}
    (walk : Walk edge i vs j) (step : edge j k) : Walk edge i (vs ++ [k]) k := by
  induction walk with
  | nil j => exact Walk.cons step (Walk.nil k)
  | cons first _ ih => exact Walk.cons first (ih step)

theorem Walk.length_pos {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) : 0 < vs.length := by
  cases walk with
  | nil => exact Nat.zero_lt_succ _
  | cons => exact Nat.zero_lt_succ _

theorem Walk.end_mem {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) : k ∈ vs := by
  induction walk with
  | nil k => exact List.mem_singleton_self k
  | cons _ _ ih => exact List.mem_cons_of_mem _ ih

theorem Walk.split_aux {edge : Kind → Kind → Prop} {x k : Kind} (post : List Kind) :
    ∀ {i : Kind} {vs : List Kind}, Walk edge i vs k → ∀ pre : List Kind,
      vs = pre ++ x :: post → Walk edge i (pre ++ [x]) x ∧ Walk edge x (x :: post) k := by
  intro i vs walk
  induction walk with
  | nil k =>
    intro pre shape
    cases pre with
    | nil =>
      injection shape with same rest
      subst same
      subst rest
      exact ⟨Walk.nil _, Walk.nil _⟩
    | cons p pre =>
      injection shape with _ rest
      cases pre with
      | nil =>
        change ([] : List Kind) = x :: post at rest
        cases rest
      | cons h t =>
        change ([] : List Kind) = h :: (t ++ x :: post) at rest
        cases rest
  | @cons i j k vs step rest ih =>
    intro pre shape
    cases pre with
    | nil =>
      injection shape with same tail
      subst same
      subst tail
      exact ⟨Walk.nil _, Walk.cons step rest⟩
    | cons p pre =>
      injection shape with same tail
      subst same
      have ⟨front, back⟩ := ih pre tail
      exact ⟨Walk.cons step front, back⟩

/-- Splitting a walk at an occurrence of a kind in its vertex list. -/
theorem Walk.split {edge : Kind → Kind → Prop} {i x k : Kind} (pre post : List Kind)
    (walk : Walk edge i (pre ++ x :: post) k) :
    Walk edge i (pre ++ [x]) x ∧ Walk edge x (x :: post) k :=
  Walk.split_aux post walk pre rfl

theorem Walk.start_mem {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) : i ∈ vs := by
  cases walk with
  | nil => exact List.mem_singleton_self _
  | cons => exact List.mem_cons_self

/-- Each walk is a trace of the type process of `SupportNecessity`. -/
theorem Walk.trace {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) :
    Trace (typeProcess edge) i (vs.tail.map fun _ => ()) k := by
  induction walk with
  | nil k => exact Trace.nil k
  | cons step rest ih =>
    cases rest with
    | nil => exact Trace.cons step ih
    | cons => exact Trace.cons step ih

/-- Within a walk, every listed kind other than the start has a listed
predecessor. -/
theorem Walk.predecessor [DecidableEq Kind] {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) : ∀ v, v ∈ vs → v ≠ i → ∃ u, u ∈ vs ∧ edge u v := by
  induction walk with
  | nil k =>
    intro v member different
    exact False.elim (different (List.mem_singleton.mp member))
  | @cons i j k vs step rest ih =>
    intro v member different
    cases List.mem_cons.mp member with
    | inl same => exact False.elim (different same)
    | inr tail =>
      by_cases first : v = j
      · subst v
        exact ⟨i, List.mem_cons_self, step⟩
      · have ⟨u, inside, edgeUV⟩ := ih v tail first
        exact ⟨u, List.mem_cons_of_mem _ inside, edgeUV⟩

/-- Within a walk, every listed kind other than the end has a listed
successor. -/
theorem Walk.successor {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) : ∀ v, v ∈ vs → v ≠ k → ∃ w, w ∈ vs ∧ edge v w := by
  induction walk with
  | nil k =>
    intro v member different
    exact False.elim (different (List.mem_singleton.mp member))
  | @cons i j k vs step rest ih =>
    intro v member different
    cases List.mem_cons.mp member with
    | inl same =>
      subst v
      cases rest with
      | nil => exact ⟨j, List.mem_cons_of_mem _ (List.mem_singleton_self j), step⟩
      | cons => exact ⟨j, List.mem_cons_of_mem _ List.mem_cons_self, step⟩
    | inr tail =>
      have ⟨w, inside, edgeVW⟩ := ih v tail different
      exact ⟨w, List.mem_cons_of_mem _ inside, edgeVW⟩

/-- A walk with at least one step reaches its end through a listed
predecessor. -/
theorem Walk.end_predecessor {edge : Kind → Kind → Prop} {i k : Kind} {vs : List Kind}
    (walk : Walk edge i vs k) (long : 2 ≤ vs.length) : ∃ u, u ∈ vs ∧ edge u k := by
  induction walk with
  | nil k => exact False.elim (Nat.lt_irrefl 1 long)
  | @cons i j k vs step rest ih =>
    cases rest with
    | nil => exact ⟨i, List.mem_cons_self, step⟩
    | @cons j' m k' vs' step' rest' =>
      have positive := rest'.length_pos
      have ⟨u, inside, edgeUK⟩ := ih (by simp only [List.length_cons]; omega)
      exact ⟨u, List.mem_cons_of_mem _ inside, edgeUK⟩

/-- Closure in the sense of Montévil and Mossio, at the level of kinds: every
member depends on a member and supports a member. A single self-supporting kind
satisfies this with distinct occurrences; the paper's "other constraint" then
holds between occurrences, not between kinds. -/
def DependenceClosed (edge : Kind → Kind → Prop) (C : List Kind) : Prop :=
  C ≠ [] ∧ (∀ v, v ∈ C → ∃ u, u ∈ C ∧ edge u v) ∧ (∀ v, v ∈ C → ∃ w, w ∈ C ∧ edge v w)

/-- The kinds visited by a closed walk, after its start, form a closed set. -/
theorem closed_walk_dependence_closed [DecidableEq Kind] {edge : Kind → Kind → Prop}
    {j : Kind} {cycle : List Kind} (walk : Walk edge j (j :: cycle) j) (nonempty : cycle ≠ []) :
    DependenceClosed edge cycle := by
  cases walk with
  | nil => exact False.elim (nonempty rfl)
  | @cons _ x _ _ first rest =>
    have jIn : j ∈ cycle := rest.end_mem
    refine ⟨nonempty, ?_, ?_⟩
    · intro v member
      by_cases atStart : v = x
      · rw [atStart]
        exact ⟨j, jIn, first⟩
      · exact rest.predecessor v member atStart
    · intro v member
      by_cases atEnd : v = j
      · rw [atEnd]
        exact ⟨x, rest.start_mem, first⟩
      · exact rest.successor v member atEnd

/-- Remove the first copy of `y`. Defined here so the pigeonhole argument does
not inherit classical dependencies from library lemmas about `List.erase`. -/
def removeOne [DecidableEq Kind] (y : Kind) : List Kind → List Kind
  | [] => []
  | z :: zs => if z = y then zs else z :: removeOne y zs

theorem mem_removeOne_of_ne [DecidableEq Kind] {y x : Kind} :
    ∀ {l : List Kind}, x ≠ y → x ∈ l → x ∈ removeOne y l
  | [], _, member => by cases member
  | z :: zs, different, member => by
    by_cases zy : z = y
    · rw [removeOne, if_pos zy]
      cases List.mem_cons.mp member with
      | inl same => exact absurd (same.trans zy) different
      | inr tail => exact tail
    · rw [removeOne, if_neg zy]
      cases List.mem_cons.mp member with
      | inl same => rw [same]; exact List.mem_cons_self
      | inr tail => exact List.mem_cons_of_mem _ (mem_removeOne_of_ne different tail)

theorem length_removeOne_of_mem [DecidableEq Kind] {y : Kind} :
    ∀ {l : List Kind}, y ∈ l → (removeOne y l).length + 1 = l.length
  | [], member => by cases member
  | z :: zs, member => by
    by_cases zy : z = y
    · rw [removeOne, if_pos zy]
      rfl
    · rw [removeOne, if_neg zy]
      have inTail : y ∈ zs := by
        cases List.mem_cons.mp member with
        | inl same => exact absurd same.symm zy
        | inr tail => exact tail
      have ih := length_removeOne_of_mem inTail
      simp only [List.length_cons]
      omega

/-- Pigeonhole for lists drawn from a finite list of kinds. -/
theorem duplicate_of_long [DecidableEq Kind] :
    ∀ (U vs : List Kind), (∀ x, x ∈ vs → x ∈ U) → U.length < vs.length →
      ∃ pre x mid post, vs = pre ++ x :: (mid ++ x :: post)
  | U, [], _, long => False.elim (Nat.not_lt_zero _ long)
  | U, y :: rest, inside, long => by
    by_cases repeated : y ∈ rest
    · have ⟨mid, post, split⟩ := List.append_of_mem repeated
      exact ⟨[], y, mid, post, by rw [split]; rfl⟩
    · have yU : y ∈ U := inside y List.mem_cons_self
      have restInside : ∀ x, x ∈ rest → x ∈ removeOne y U := by
        intro x member
        have different : x ≠ y := fun same => repeated (same ▸ member)
        exact mem_removeOne_of_ne different (inside x (List.mem_cons_of_mem _ member))
      have shorter : (removeOne y U).length < rest.length := by
        have removed := length_removeOne_of_mem yU
        simp only [List.length_cons] at long
        omega
      have ⟨pre, x, mid, post, split⟩ := duplicate_of_long (removeOne y U) rest restInside shorter
      exact ⟨y :: pre, x, mid, post, by rw [split]; rfl⟩

/-- Backward chain: an occurrence later than `m * D` descends through a walk of
`m` support steps, each visited kind occurring within the window. -/
theorem support_walk (S : OccurrenceSupport Kind) (D : Nat)
    (bound : ∀ j, S.reach j ≤ D) :
    ∀ (m t : Nat) (k : Kind), S.occurs k t → m * D < t →
      ∃ j vs, Walk S.edge j vs k ∧ vs.length = m + 1 ∧
        ∀ v, v ∈ vs → ∃ s, S.occurs v s ∧ t ≤ s + m * D
  | 0, t, k, occ, _ => by
    refine ⟨k, [k], Walk.nil k, rfl, ?_⟩
    intro v member
    have same := List.mem_singleton.mp member
    subst v
    exact ⟨t, occ, by omega⟩
  | m + 1, t, k, occ, late => by
    have positive : 0 < t := Nat.lt_of_le_of_lt (Nat.zero_le _) late
    have ⟨j, s, edgeJK, occJ, earlier, within⟩ := S.support k t occ positive
    have reachBound := bound j
    have lateS : m * D < s := by
      rw [Nat.succ_mul] at late
      omega
    have ⟨i, vs, walk, length, window⟩ := support_walk S D bound m s j occJ lateS
    refine ⟨i, vs ++ [k], walk.snoc edgeJK, by simp [length], ?_⟩
    intro v member
    cases List.mem_append.mp member with
    | inl old =>
      have ⟨r, occV, near⟩ := window v old
      refine ⟨r, occV, ?_⟩
      rw [Nat.succ_mul]
      omega
    | inr new =>
      have same := List.mem_singleton.mp new
      subst v
      exact ⟨t, occ, by omega⟩

/-- **Late activity descends from a realized closure.** With every kind listed in
`U` and support reach at most `D`, an occurrence after `U.length * D` descends
from a nonempty closed walk of kinds. Every kind on that walk occurs within the
last `U.length * D` time units before the late occurrence, so the closure is
realized recently, not merely permitted by the edges. -/
theorem late_occurrence_descends_from_realized_closure [DecidableEq Kind]
    (S : OccurrenceSupport Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (bound : ∀ j, S.reach j ≤ D) {t : Nat} {k : Kind}
    (occ : S.occurs k t) (late : U.length * D < t) :
    ∃ j cycle rest,
      cycle ≠ [] ∧ Walk S.edge j (j :: cycle) j ∧ Walk S.edge j (j :: rest) k ∧
      DependenceClosed S.edge cycle ∧
      ∀ v, v ∈ cycle → ∃ s, S.occurs v s ∧ t ≤ s + U.length * D := by
  have ⟨i, vs, walk, length, window⟩ := support_walk S D bound U.length t k occ late
  have long : U.length < vs.length := by omega
  have ⟨pre, x, mid, post, split⟩ :=
    duplicate_of_long U vs (fun v _ => complete v) long
  subst split
  have ⟨_, back⟩ := Walk.split pre (mid ++ x :: post) walk
  have reshaped : x :: (mid ++ x :: post) = (x :: mid) ++ x :: post := rfl
  rw [reshaped] at back
  have ⟨loop, tail⟩ := Walk.split (x :: mid) post back
  have loopShape : (x :: mid) ++ [x] = x :: (mid ++ [x]) := rfl
  rw [loopShape] at loop
  have nonempty : mid ++ [x] ≠ [] := by simp
  refine ⟨x, mid ++ [x], post, nonempty, loop, tail,
    closed_walk_dependence_closed loop nonempty, ?_⟩
  intro v member
  apply window v
  cases List.mem_append.mp member with
  | inl inMid => simp [inMid]
  | inr isX =>
    have same := List.mem_singleton.mp isX
    subst v
    simp

/-- The same conclusion as a nonempty cycle of the type process, the form used
by `SupportNecessity`. -/
theorem late_occurrence_requires_type_cycle [DecidableEq Kind]
    (S : OccurrenceSupport Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (bound : ∀ j, S.reach j ≤ D) {t : Nat} {k : Kind}
    (occ : S.occurs k t) (late : U.length * D < t) :
    ∃ j word, word ≠ [] ∧ Trace (typeProcess S.edge) j word j := by
  have ⟨j, cycle, _, nonempty, loop, _⟩ :=
    late_occurrence_descends_from_realized_closure S U complete D bound occ late
  refine ⟨j, cycle.map (fun _ => ()), ?_, loop.trace⟩
  intro empty
  exact nonempty (List.map_eq_nil_iff.mp empty)

/-- **Deadline without a supplied rank.** If the support edges allow no nonempty
type cycle, nothing occurs after `U.length * D`. -/
theorem acyclic_support_deadline [DecidableEq Kind]
    (S : OccurrenceSupport Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (bound : ∀ j, S.reach j ≤ D)
    (acyclic : ∀ j word, word ≠ [] → ¬ Trace (typeProcess S.edge) j word j)
    {t : Nat} (late : U.length * D < t) : ∀ k, ¬ S.occurs k t := by
  intro k occ
  have ⟨j, word, nonempty, cycle⟩ :=
    late_occurrence_requires_type_cycle S U complete D bound occ late
  exact acyclic j word nonempty cycle

/-- Episode systems are occurrence systems: an episode's birth is an occurrence
of its kind, supported by its parent until the parent's lifetime bound. -/
def episodeSupport {Episode : Type v} (S : EpisodeSystem Kind Episode) :
    OccurrenceSupport Kind where
  occurs k t := ∃ e, S.kind e = k ∧ S.birth e = t
  edge := S.edge
  reach := S.duration
  support := by
    intro k t ⟨e, kindE, birthE⟩ positive
    subst kindE
    subst birthE
    have ⟨p, earlier, stillAlive, edgePE⟩ := S.parent e positive
    exact ⟨S.kind p, S.birth p, edgePE, ⟨p, rfl, rfl⟩, earlier,
      Nat.le_trans stillAlive (S.lifetime p)⟩

/-- **The gap `SupportNecessity` names, closed.** In an episode system with
finitely many kinds and lifetimes at most `L`, if the type relation has no
nonempty cycle then no episode is alive after `(U.length + 1) * L`. No rank
certificate is supplied. -/
theorem episode_acyclic_deadline [DecidableEq Kind] {Episode : Type v}
    (S : EpisodeSystem Kind Episode) (U : List Kind) (complete : ∀ k, k ∈ U)
    (L : Nat) (lifeBound : ∀ k, S.duration k ≤ L)
    (acyclic : ∀ j word, word ≠ [] → ¬ Trace (typeProcess S.edge) j word j)
    {t : Nat} (late : (U.length + 1) * L < t) : ¬ ∃ e, Alive S e t := by
  rintro ⟨e, born, expires⟩
  have life := S.lifetime e
  have bornLate : U.length * L < S.birth e := by
    have bound := lifeBound (S.kind e)
    rw [Nat.succ_mul] at late
    omega
  exact acyclic_support_deadline (episodeSupport S) U complete L lifeBound acyclic
    bornLate (S.kind e) ⟨e, rfl, rfl⟩

/-- In an episode system, an episode alive after `(U.length + 1) * L` descends
from a realized closure of kinds. -/
theorem episode_late_life_descends_from_realized_closure [DecidableEq Kind]
    {Episode : Type v} (S : EpisodeSystem Kind Episode) (U : List Kind)
    (complete : ∀ k, k ∈ U) (L : Nat) (lifeBound : ∀ k, S.duration k ≤ L)
    {e : Episode} {t : Nat} (alive : Alive S e t) (late : (U.length + 1) * L < t) :
    ∃ j cycle rest,
      cycle ≠ [] ∧ Walk S.edge j (j :: cycle) j ∧ Walk S.edge j (j :: rest) (S.kind e) ∧
      DependenceClosed S.edge cycle ∧
      ∀ v, v ∈ cycle → ∃ p, S.kind p = v ∧ S.birth e ≤ S.birth p + U.length * L := by
  have life := S.lifetime e
  have bound := lifeBound (S.kind e)
  have bornLate : U.length * L < S.birth e := by
    rw [Nat.succ_mul] at late
    have := alive.2
    omega
  have ⟨j, cycle, rest, nonempty, loop, tail, closed, window⟩ :=
    late_occurrence_descends_from_realized_closure (episodeSupport S) U complete L lifeBound
      (k := S.kind e) ⟨e, rfl, rfl⟩ bornLate
  refine ⟨j, cycle, rest, nonempty, loop, tail, closed, ?_⟩
  intro v member
  have ⟨s, ⟨p, kindP, birthP⟩, near⟩ := window v member
  exact ⟨p, kindP, by rw [birthP]; exact near⟩

#print axioms Walk.snoc
#print axioms Walk.length_pos
#print axioms Walk.end_mem
#print axioms Walk.split_aux
#print axioms Walk.split
#print axioms Walk.start_mem
#print axioms Walk.trace
#print axioms Walk.predecessor
#print axioms Walk.successor
#print axioms Walk.end_predecessor
#print axioms closed_walk_dependence_closed
#print axioms mem_removeOne_of_ne
#print axioms length_removeOne_of_mem
#print axioms duplicate_of_long
#print axioms support_walk
#print axioms late_occurrence_descends_from_realized_closure
#print axioms late_occurrence_requires_type_cycle
#print axioms acyclic_support_deadline
#print axioms episode_acyclic_deadline
#print axioms episode_late_life_descends_from_realized_closure

end Generative.Conditional.Renewal
