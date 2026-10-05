import GenerativeCore

/-!
# Vulnerable support and a finite deadline

This is a natural-time episode model, not a derived physical ontology. Each
positive-time birth requires an earlier parent still functioning at birth.
Finite lifetimes and a bounded strict type rank then imply a finite deadline.
The deadline is derived from local premises; continuation is not assumed.

The type graph describes permitted support. A cycle removes the strict-rank
obstruction but need not be realized or sufficient for continuation. Infinite
acyclic type chains and externally introduced organization are explicit scope
boundaries. No finite-graph cycle-extraction theorem is claimed here.
-/

namespace Generative.Conditional.Support

universe u v

/-- Episodes may be arbitrarily numerous. Initial episodes start at zero, with
their remaining lifetime absorbed into `duration`. A new organized episode
must have an earlier live parent; raw material and energy may remain external.
Birth and expiry coordinates are natural numbers, and expiry is inclusive. -/
structure EpisodeSystem (Kind : Type u) (Episode : Type v) where
  kind : Episode → Kind
  birth : Episode → Nat
  expiry : Episode → Nat
  duration : Kind → Nat
  edge : Kind → Kind → Prop
  ordered : ∀ e, birth e ≤ expiry e
  lifetime : ∀ e, expiry e ≤ birth e + duration (kind e)
  parent : ∀ e, 0 < birth e → ∃ p,
    birth p < birth e ∧ birth e ≤ expiry p ∧ edge (kind p) (kind e)

variable {Kind : Type u} {Episode : Type v}

def Alive (S : EpisodeSystem Kind Episode) (e : Episode) (t : Nat) : Prop :=
  S.birth e ≤ t ∧ t ≤ S.expiry e

/-- A locally justified type potential bounds every episode's actual expiry.
Its edge inequality is stronger than acyclicity alone and can encode unequal
lifetimes. The proof follows actual earlier births, not hypothetical edges. -/
theorem expiry_le_potential (S : EpisodeSystem Kind Episode)
    (deadline : Kind → Nat)
    (initial : ∀ i, S.duration i ≤ deadline i)
    (transfer : ∀ i j, S.edge i j → deadline i + S.duration j ≤ deadline j)
    (e : Episode) : S.expiry e ≤ deadline (S.kind e) := by
  have bounded : ∀ n, ∀ e : Episode, S.birth e = n →
      S.expiry e ≤ deadline (S.kind e) := by
    intro n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro e born
      by_cases hz : n = 0
      · have life := S.lifetime e
        rw [born, hz, Nat.zero_add] at life
        exact Nat.le_trans life (initial (S.kind e))
      · have positive : 0 < S.birth e := by
          rw [born]
          exact Nat.zero_lt_of_ne_zero hz
        obtain ⟨p, earlier, live, supports⟩ := S.parent e positive
        have earlier' : S.birth p < n := by rw [← born]; exact earlier
        have previous := ih (S.birth p) earlier' p rfl
        exact Nat.le_trans (S.lifetime e) (Nat.le_trans
          (Nat.add_le_add_right (Nat.le_trans live previous) _)
          (transfer (S.kind p) (S.kind e) supports))
  exact bounded (S.birth e) e rfl

theorem alive_le_potential (S : EpisodeSystem Kind Episode)
    (deadline : Kind → Nat)
    (initial : ∀ i, S.duration i ≤ deadline i)
    (transfer : ∀ i j, S.edge i j → deadline i + S.duration j ≤ deadline j)
    {e : Episode} {t : Nat} (live : Alive S e t) :
    t ≤ deadline (S.kind e) := by
  exact Nat.le_trans live.2 (expiry_le_potential S deadline initial transfer e)

/-- Uniform lifetime plus strict parent-to-child rank generates a valid
deadline potential; the rank is a supplied, checkable certificate. -/
theorem expiry_le_rank_deadline (S : EpisodeSystem Kind Episode)
    (rank : Kind → Nat) (L : Nat)
    (lifeBound : ∀ i, S.duration i ≤ L)
    (rankRises : ∀ i j, S.edge i j → rank i < rank j)
    (e : Episode) : S.expiry e ≤ (rank (S.kind e) + 1) * L := by
  apply expiry_le_potential S (fun i => (rank i + 1) * L)
  · intro i
    have bound : 1 * L ≤ (rank i + 1) * L :=
      Nat.mul_le_mul_right L (Nat.succ_le_succ (Nat.zero_le _))
    rw [Nat.one_mul] at bound
    exact Nat.le_trans (lifeBound i) bound
  · intro i j edge
    have increase := rankRises i j edge
    have multiplication : (rank i + 2) * L ≤ (rank j + 1) * L :=
      Nat.mul_le_mul_right L (Nat.succ_le_succ increase)
    have budget := lifeBound j
    have expansion : (rank i + 2) * L = (rank i + 1) * L + L :=
      Nat.succ_mul (rank i + 1) L
    rw [expansion] at multiplication
    exact Nat.le_trans (Nat.add_le_add_left budget _) multiplication

theorem alive_le_rank_deadline (S : EpisodeSystem Kind Episode)
    (rank : Kind → Nat) (L : Nat)
    (lifeBound : ∀ i, S.duration i ≤ L)
    (rankRises : ∀ i j, S.edge i j → rank i < rank j)
    {e : Episode} {t : Nat} (live : Alive S e t) :
    t ≤ (rank (S.kind e) + 1) * L := by
  exact Nat.le_trans live.2 (expiry_le_rank_deadline S rank L lifeBound rankRises e)

/-- Continuation past a specified level's deadline forces a strictly higher
rank. Thus unbounded continuation cannot be covered by a bounded ranking. -/
theorem late_alive_requires_higher_rank (S : EpisodeSystem Kind Episode)
    (rank : Kind → Nat) (L : Nat)
    (lifeBound : ∀ i, S.duration i ≤ L)
    (rankRises : ∀ i j, S.edge i j → rank i < rank j)
    {e : Episode} {t k : Nat} (live : Alive S e t)
    (late : (k + 1) * L < t) : k < rank (S.kind e) := by
  have deadline := alive_le_rank_deadline S rank L lifeBound rankRises live
  apply Nat.lt_of_not_ge
  intro lower
  have bounded : rank (S.kind e) + 1 ≤ k + 1 := Nat.succ_le_succ lower
  have multiplication := Nat.mul_le_mul_right L bounded
  exact Nat.not_lt_of_ge (Nat.le_trans deadline multiplication) late

/-- A finite range of strict ranks gives a common, observable deadline. This
does not assume finitely many tokens, births, or copies. -/
theorem bounded_rank_deadline (S : EpisodeSystem Kind Episode)
    (rank : Kind → Fin n) (L : Nat)
    (lifeBound : ∀ i, S.duration i ≤ L)
    (rankRises : ∀ i j, S.edge i j → (rank i).val < (rank j).val)
    {e : Episode} {t : Nat} (live : Alive S e t) : t ≤ n * L := by
  have deadline := alive_le_rank_deadline S (fun i => (rank i).val)
    L lifeBound rankRises live
  change t ≤ ((rank (S.kind e)).val + 1) * L at deadline
  have level := (rank (S.kind e)).isLt
  have multiplication : ((rank (S.kind e)).val + 1) * L ≤ n * L :=
    Nat.mul_le_mul_right L level
  exact Nat.le_trans deadline multiplication

theorem no_alive_after_bounded_rank_deadline (S : EpisodeSystem Kind Episode)
    (rank : Kind → Fin n) (L : Nat)
    (lifeBound : ∀ i, S.duration i ≤ L)
    (rankRises : ∀ i j, S.edge i j → (rank i).val < (rank j).val)
    {t : Nat} (late : n * L < t) : ¬ ∃ e, Alive S e t := by
  rintro ⟨e, live⟩
  have deadline := bounded_rank_deadline S rank L lifeBound rankRises live
  exact Nat.not_lt_of_ge deadline late

/-- The type relation is itself an event process. Events here only mark
support edges; this representation does not identify type paths with token
histories or claim that all permitted edges are executed. -/
def typeProcess (edge : Kind → Kind → Prop) : Process Kind Unit where
  step i _ j := edge i j

theorem strict_rank_bounds_type_trace (edge : Kind → Kind → Prop)
    (rank : Kind → Nat)
    (rankRises : ∀ i j, edge i j → rank i < rank j)
    {i j : Kind} {word : List Unit} (path : Trace (typeProcess edge) i word j) :
    rank i + word.length ≤ rank j := by
  induction path with
  | nil i => exact Nat.le_refl _
  | cons step _ ih =>
    have rising := rankRises _ _ step
    have bound := Nat.le_trans (Nat.add_le_add_right rising _) ih
    rw [Nat.succ_add] at bound
    exact bound

theorem strict_rank_excludes_nonempty_type_cycle (edge : Kind → Kind → Prop)
    (rank : Kind → Nat)
    (rankRises : ∀ i j, edge i j → rank i < rank j)
    {i : Kind} {word : List Unit}
    (cycle : Trace (typeProcess edge) i word i) (nonempty : word ≠ []) : False := by
  have bound := strict_rank_bounds_type_trace edge rank rankRises cycle
  cases word with
  | nil => exact nonempty rfl
  | cons a rest =>
    have positive : 0 < (a :: rest).length := Nat.zero_lt_succ _
    exact Nat.not_lt_of_ge bound (Nat.lt_add_of_pos_right positive)

/-- One support role is replaced by successive episodes. Resource, activation
and conversion requirements beyond the declared law remain supplied. -/
def renewing : EpisodeSystem Unit Nat where
  kind _ := ()
  birth n := n
  expiry n := n + 2
  duration _ := 2
  edge _ _ := True
  ordered n := Nat.le_add_right n 2
  lifetime _ := Nat.le_refl _
  parent n positive := by
    cases n with
    | zero => exact False.elim (Nat.lt_irrefl 0 positive)
    | succ k => exact ⟨k, Nat.lt_succ_self k, Nat.le_succ (k + 1), True.intro⟩

theorem renewing_alive_at_every_time (t : Nat) : Alive renewing t t := by
  exact ⟨Nat.le_refl _, Nat.le_add_right _ _⟩

theorem renewing_has_type_cycle :
    Trace (typeProcess renewing.edge) () [()] () := by
  exact Trace.cons True.intro (Trace.nil ())

theorem renewing_has_no_strict_type_rank :
    ¬ ∃ rank : Unit → Nat, ∀ i j, renewing.edge i j → rank i < rank j := by
  rintro ⟨rank, rises⟩
  have impossible := rises () () True.intro
  exact Nat.lt_irrefl _ impossible

/-- Exactly the same permitted one-type cycle can occur in a system that
never replaces its sole initial episode. Permitted cyclic structure does not
force successful or even attempted renewal. -/
def finiteInitial : EpisodeSystem Unit Unit where
  kind _ := ()
  birth _ := 0
  expiry _ := 2
  duration _ := 2
  edge _ _ := True
  ordered _ := Nat.zero_le _
  lifetime _ := Nat.le_refl _
  parent _ impossible := False.elim (Nat.not_lt_zero _ impossible)

theorem finiteInitial_has_type_cycle :
    Trace (typeProcess finiteInitial.edge) () [()] () := by
  exact Trace.cons True.intro (Trace.nil ())

theorem finiteInitial_dead_after_two {t : Nat} (late : 2 < t) :
    ¬ ∃ e, Alive finiteInitial e t := by
  rintro ⟨e, live⟩
  have ending : t ≤ 2 := live.2
  exact Nat.not_lt_of_ge ending late

/-- Unbounded novelty of support types admits an indefinitely functioning
acyclic chain while respecting all episode lifetime and parent premises. -/
def infiniteChain : EpisodeSystem Nat Nat where
  kind n := n
  birth n := n
  expiry n := n + 2
  duration _ := 2
  edge i j := j = i + 1
  ordered n := Nat.le_add_right n 2
  lifetime _ := Nat.le_refl _
  parent n positive := by
    cases n with
    | zero => exact False.elim (Nat.lt_irrefl 0 positive)
    | succ k => exact ⟨k, Nat.lt_succ_self k, Nat.le_succ (k + 1), rfl⟩

theorem infiniteChain_alive_at_every_time (t : Nat) : Alive infiniteChain t t := by
  exact ⟨Nat.le_refl _, Nat.le_add_right _ _⟩

theorem infiniteChain_rank_rises (i j : Nat) (edge : infiniteChain.edge i j) :
    i < j := by
  change j = i + 1 at edge
  rw [edge]
  exact Nat.lt_succ_self _

theorem infiniteChain_has_no_nonempty_type_cycle {i : Nat} {word : List Unit}
    (cycle : Trace (typeProcess infiniteChain.edge) i word i)
    (nonempty : word ≠ []) : False := by
  exact strict_rank_excludes_nonempty_type_cycle infiniteChain.edge
    (fun n => n) infiniteChain_rank_rises cycle nonempty

/-- Arrivals at every time can respect uniform finite duration and function
forever even with no support edges. They fail the internal-parent premise,
which is why externally supplied organization is a substantive boundary. -/
theorem external_arrivals_without_internal_parents :
    (∀ t : Nat, t ≤ t ∧ t ≤ t + 2) ∧
    (∀ n : Nat, n + 2 ≤ n + 2) ∧
    ¬ (∀ n : Nat, 0 < n → ∃ p : Nat,
      p < n ∧ n ≤ p + 2 ∧ False) := by
  refine ⟨?_, ?_, ?_⟩
  · intro t; exact ⟨Nat.le_refl _, Nat.le_add_right _ _⟩
  · intro n; exact Nat.le_refl _
  · intro parents
    obtain ⟨p, _, _, impossible⟩ := parents 1 (Nat.zero_lt_succ 0)
    exact impossible

#print axioms Generative.Conditional.Support.expiry_le_potential
#print axioms Generative.Conditional.Support.alive_le_potential
#print axioms Generative.Conditional.Support.expiry_le_rank_deadline
#print axioms Generative.Conditional.Support.alive_le_rank_deadline
#print axioms Generative.Conditional.Support.late_alive_requires_higher_rank
#print axioms Generative.Conditional.Support.bounded_rank_deadline
#print axioms Generative.Conditional.Support.no_alive_after_bounded_rank_deadline
#print axioms Generative.Conditional.Support.strict_rank_bounds_type_trace
#print axioms Generative.Conditional.Support.strict_rank_excludes_nonempty_type_cycle
#print axioms Generative.Conditional.Support.renewing_alive_at_every_time
#print axioms Generative.Conditional.Support.renewing_has_type_cycle
#print axioms Generative.Conditional.Support.renewing_has_no_strict_type_rank
#print axioms Generative.Conditional.Support.finiteInitial_has_type_cycle
#print axioms Generative.Conditional.Support.finiteInitial_dead_after_two
#print axioms Generative.Conditional.Support.infiniteChain_alive_at_every_time
#print axioms Generative.Conditional.Support.infiniteChain_rank_rises
#print axioms Generative.Conditional.Support.infiniteChain_has_no_nonempty_type_cycle
#print axioms Generative.Conditional.Support.external_arrivals_without_internal_parents

end Generative.Conditional.Support
