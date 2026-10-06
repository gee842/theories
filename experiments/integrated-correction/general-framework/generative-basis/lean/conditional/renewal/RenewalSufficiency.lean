import RenewalAccounting

/-!
# Renewal sufficiency: a closed, balanced population is a standing renewal

Phase 2 of the renewal–closure roadmap. Take a list `B` of kinds, repeats
allowed, formed afresh on every tick. In the steady configuration, each kind
in `B` keeps one token of every age within its span. One tick then ages every
token, drops those on their last tick, and adds the new formations. That
returns exactly the same configuration, so the configuration is a fixed point
of `channelProcess`.

The tick is admissible when:
- every formed kind has a supporter in `B` whose span is at least two, so a
  token of it survives the tick;
- the formations demand no more than the population opens,
  `Σ demand ≤ Σ rate · span` over `B`.

Two corollaries follow. A support-closed population of kinds that each bring
in at least their formation demand renews forever. So does any support-closed
population that also supports an excess kind, taken with enough repeats. Both
need no reserve at all.

These are possibility results under supplied laws. They do not say a system
reaches the steady configuration, nor that it would be favorable to.
-/

namespace Generative.Conditional.Renewal

open Generative

universe u

variable {Kind : Type u}

/-- Tokens of the formation list that are `d` ticks old. -/
def block (law : ChannelLaw Kind) (d : Nat) : List Kind → List (Token Kind)
  | [] => []
  | k :: rest =>
    if d < law.span k then ⟨k, law.span k - d⟩ :: block law d rest else block law d rest

/-- The steady configuration's tokens: ages `n - 1` down to `0`. -/
def steady (law : ChannelLaw Kind) (B : List Kind) : Nat → List (Token Kind)
  | 0 => []
  | n + 1 => block law n B ++ steady law B n

/-- What the formation list opens over its tokens' whole spans. -/
def spanOpening (law : ChannelLaw Kind) : List Kind → Nat
  | [] => 0
  | k :: rest => law.rate k * law.span k + spanOpening law rest

theorem aged_append :
    ∀ l m : List (Token Kind), aged (l ++ m) = aged l ++ aged m
  | [], m => rfl
  | tok :: rest, m => by
    simp only [List.cons_append, aged]
    by_cases last : tok.remaining ≤ 1
    · rw [if_pos last, if_pos last, aged_append rest m]
    · rw [if_neg last, if_neg last, aged_append rest m]
      rfl

theorem opened_append (w : Kind → Nat) :
    ∀ l m : List (Token Kind), opened w (l ++ m) = opened w l + opened w m
  | [], m => by simp [opened]
  | tok :: rest, m => by
    simp only [List.cons_append, opened, opened_append w rest m]
    omega

/-- Aging moves every block one tick older. -/
theorem aged_block (law : ChannelLaw Kind) (d : Nat) :
    ∀ B : List Kind, aged (block law d B) = block law (d + 1) B
  | [] => rfl
  | k :: rest => by
    have ih := aged_block law d rest
    by_cases young : d < law.span k
    · rw [block, if_pos young, aged]
      by_cases last : law.span k - d ≤ 1
      · have old : ¬ d + 1 < law.span k := by omega
        rw [if_pos last, block, if_neg old, ih]
      · have still : d + 1 < law.span k := by omega
        rw [if_neg last, block, if_pos still, ih]
        have same : law.span k - d - 1 = law.span k - (d + 1) := by omega
        rw [same]
    · have old : ¬ d + 1 < law.span k := by omega
      rw [block, if_neg young, block, if_neg old, ih]

theorem block_beyond (law : ChannelLaw Kind) (n : Nat) :
    ∀ B : List Kind, (∀ k, k ∈ B → law.span k ≤ n) → block law n B = []
  | [], _ => rfl
  | k :: rest, bound => by
    have here := bound k List.mem_cons_self
    have old : ¬ n < law.span k := by omega
    rw [block, if_neg old]
    exact block_beyond law n rest (fun j member => bound j (List.mem_cons_of_mem _ member))

theorem formed_eq_block_zero (law : ChannelLaw Kind) :
    ∀ B : List Kind, (∀ k, k ∈ B → 0 < law.span k) → formed law B = block law 0 B
  | [], _ => rfl
  | k :: rest, positive => by
    have here := positive k List.mem_cons_self
    rw [formed, block, if_pos here, Nat.sub_zero,
      formed_eq_block_zero law rest (fun j member => positive j (List.mem_cons_of_mem _ member))]

/-- The shift identity: aging the steady tokens and adding fresh formations
gives the next older block in front of the same steady tokens. -/
theorem steady_shift (law : ChannelLaw Kind) (B : List Kind) :
    ∀ n, aged (steady law B n) ++ block law 0 B = block law n B ++ steady law B n
  | 0 => by simp [steady, aged]
  | n + 1 => by
    have ih := steady_shift law B n
    rw [steady, aged_append, aged_block, List.append_assoc, ih]

/-- **The steady configuration is a fixed point of one tick.** -/
theorem steady_fixed (law : ChannelLaw Kind) (B : List Kind) (N : Nat)
    (positive : ∀ k, k ∈ B → 0 < law.span k) (bound : ∀ k, k ∈ B → law.span k ≤ N) :
    aged (steady law B N) ++ formed law B = steady law B N := by
  rw [formed_eq_block_zero law B positive, steady_shift, block_beyond law N B bound,
    List.nil_append]

theorem opened_block (law : ChannelLaw Kind) (w : Kind → Nat) (d : Nat) :
    ∀ B : List Kind,
      opened w (block law d B) = (B.map fun k => if d < law.span k then w k else 0).sum
  | [] => rfl
  | k :: rest => by
    have ih := opened_block law w d rest
    by_cases young : d < law.span k
    · rw [block, if_pos young, opened]
      have nonzero : ¬ law.span k - d = 0 := by omega
      simp only [if_neg nonzero, ih, List.map_cons, List.sum_cons, if_pos young]
    · rw [block, if_neg young, ih]
      simp only [List.map_cons, List.sum_cons, if_neg young, Nat.zero_add]

theorem capped_step (w s N : Nat) :
    w * min s (N + 1) = w * min s N + (if N < s then w else 0) := by
  by_cases young : N < s
  · rw [if_pos young, Nat.min_eq_right (by omega), Nat.min_eq_right (by omega), Nat.mul_succ]
  · rw [if_neg young, Nat.min_eq_left (by omega), Nat.min_eq_left (by omega), Nat.add_zero]

theorem sum_map_add (f g : Kind → Nat) :
    ∀ B : List Kind, (B.map f).sum + (B.map g).sum = (B.map fun k => f k + g k).sum
  | [] => rfl
  | k :: rest => by
    have ih := sum_map_add f g rest
    simp only [List.map_cons, List.sum_cons]
    omega

theorem sum_map_zero (f : Kind → Nat) (zero : ∀ k, f k = 0) :
    ∀ B : List Kind, (B.map f).sum = 0
  | [] => rfl
  | k :: rest => by
    simp only [List.map_cons, List.sum_cons, zero k, sum_map_zero f zero rest]

/-- What the steady tokens open: each kind contributes for every tick of its
span, capped by the number of blocks. -/
theorem opened_steady (law : ChannelLaw Kind) (w : Kind → Nat) (B : List Kind) :
    ∀ N, opened w (steady law B N) = (B.map fun k => w k * min (law.span k) N).sum
  | 0 => by
    rw [sum_map_zero _ (fun k => by rw [Nat.min_zero, Nat.mul_zero]) B]
    rfl
  | N + 1 => by
    rw [steady, opened_append, opened_block, opened_steady law w B N, Nat.add_comm,
      sum_map_add]
    have pointwise : (fun k => w k * min (law.span k) N + (if N < law.span k then w k else 0)) =
        (fun k => w k * min (law.span k) (N + 1)) := by
      funext k
      exact (capped_step _ _ _).symm
    rw [pointwise]

theorem spanOpening_eq (law : ChannelLaw Kind) (B : List Kind) (N : Nat)
    (bound : ∀ k, k ∈ B → law.span k ≤ N) :
    (B.map fun k => law.rate k * min (law.span k) N).sum = spanOpening law B := by
  induction B with
  | nil => rfl
  | cons k rest ih =>
    have here := bound k List.mem_cons_self
    rw [List.map_cons, List.sum_cons, spanOpening, Nat.min_eq_left here,
      ih (fun j member => bound j (List.mem_cons_of_mem _ member))]

theorem mem_block (law : ChannelLaw Kind) (d : Nat) {j : Kind} :
    ∀ {B : List Kind}, j ∈ B → d < law.span j → ⟨j, law.span j - d⟩ ∈ block law d B
  | k :: rest, member, young => by
    by_cases young' : d < law.span k
    · rw [block, if_pos young']
      cases List.mem_cons.mp member with
      | inl same => subst same; exact List.mem_cons_self
      | inr tail => exact List.mem_cons_of_mem _ (mem_block law d tail young)
    · rw [block, if_neg young']
      cases List.mem_cons.mp member with
      | inl same => subst same; exact False.elim (young' young)
      | inr tail => exact mem_block law d tail young

theorem block_one_survives (law : ChannelLaw Kind) (B : List Kind) :
    ∀ n {tok : Token Kind}, tok ∈ block law 1 B → tok ∈ aged (steady law B (n + 1))
  | 0, tok, member => by
    rw [steady, steady, List.append_nil, aged_block]
    exact member
  | n + 1, tok, member => by
    rw [steady, aged_append]
    exact List.mem_append_right _ (block_one_survives law B n member)

/-- **A closed, balanced population renews forever.** Forming `B` on every tick
from the steady configuration is a renewing tick back to the same
configuration, whatever the reserve. -/
theorem steady_renews (law : ChannelLaw Kind) (B : List Kind) (N R : Nat)
    (nonempty : B ≠ [])
    (positive : ∀ k, k ∈ B → 0 < law.span k) (bound : ∀ k, k ∈ B → law.span k ≤ N)
    (supported : ∀ k, k ∈ B → ∃ j, j ∈ B ∧ law.edge j k ∧ 2 ≤ law.span j)
    (balanced : formation law B ≤ spanOpening law B) :
    (renewingProcess law).step ⟨R, steady law B N⟩ B ⟨R, steady law B N⟩ := by
  have Npos : 0 < N := by
    cases B with
    | nil => exact False.elim (nonempty rfl)
    | cons k rest =>
      exact Nat.lt_of_lt_of_le (positive k List.mem_cons_self) (bound k List.mem_cons_self)
  obtain ⟨M, shape⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  refine ⟨?_, (steady_fixed law B N positive bound).symm, ?_, ?_⟩
  · show 1 ≤ opened (fun _ => 1) (steady law B N)
    rw [opened_steady]
    cases B with
    | nil => exact False.elim (nonempty rfl)
    | cons k rest =>
      have here := positive k List.mem_cons_self
      simp only [List.map_cons, List.sum_cons, Nat.one_mul]
      have : 1 ≤ min (law.span k) N := by
        rw [Nat.le_min]
        exact ⟨here, Npos⟩
      omega
  · show R + formation law B ≤ R + opened law.rate (steady law B N)
    rw [opened_steady, spanOpening_eq law B N bound]
    omega
  · intro k member
    have ⟨j, jIn, edgeJK, long⟩ := supported k member
    refine ⟨⟨j, law.span j - 1⟩, ?_, edgeJK⟩
    rw [shape]
    exact block_one_survives law B M (mem_block law 1 jIn (by omega))

/-- The standing renewal as an endless execution. -/
theorem steady_endless (law : ChannelLaw Kind) (B : List Kind) (N R : Nat)
    (nonempty : B ≠ [])
    (positive : ∀ k, k ∈ B → 0 < law.span k) (bound : ∀ k, k ∈ B → law.span k ≤ N)
    (supported : ∀ k, k ∈ B → ∃ j, j ∈ B ∧ law.edge j k ∧ 2 ≤ law.span j)
    (balanced : formation law B ≤ spanOpening law B) :
    ∃ states : Nat → Config Kind, ∃ ticks : Nat → List Kind,
      ∀ n, (renewingProcess law).step (states n) (ticks n) (states (n + 1)) :=
  ⟨fun _ => ⟨R, steady law B N⟩, fun _ => B,
    fun _ => steady_renews law B N R nonempty positive bound supported balanced⟩

theorem formation_append (law : ChannelLaw Kind) :
    ∀ B C : List Kind, formation law (B ++ C) = formation law B + formation law C
  | [], C => by simp [formation]
  | k :: rest, C => by
    simp only [List.cons_append, formation, formation_append law rest C]
    omega

theorem spanOpening_append (law : ChannelLaw Kind) :
    ∀ B C : List Kind, spanOpening law (B ++ C) = spanOpening law B + spanOpening law C
  | [], C => by simp [spanOpening]
  | k :: rest, C => by
    simp only [List.cons_append, spanOpening, spanOpening_append law rest C]
    omega

theorem formation_replicate (law : ChannelLaw Kind) (q : Kind) :
    ∀ n, formation law (List.replicate n q) = n * law.demand q
  | 0 => by simp [formation]
  | n + 1 => by
    rw [List.replicate_succ, formation, formation_replicate law q n, Nat.succ_mul]
    omega

theorem spanOpening_replicate (law : ChannelLaw Kind) (q : Kind) :
    ∀ n, spanOpening law (List.replicate n q) = n * (law.rate q * law.span q)
  | 0 => by simp [spanOpening]
  | n + 1 => by
    rw [List.replicate_succ, spanOpening, spanOpening_replicate law q n, Nat.succ_mul]
    omega

/-- Kinds that each bring in at least their formation demand form a balanced
population. -/
theorem balanced_of_each (law : ChannelLaw Kind) :
    ∀ B : List Kind, (∀ k, k ∈ B → law.demand k ≤ law.rate k * law.span k) →
      formation law B ≤ spanOpening law B
  | [], _ => Nat.le_refl 0
  | k :: rest, each => by
    have here := each k List.mem_cons_self
    have ih := balanced_of_each law rest (fun j member => each j (List.mem_cons_of_mem _ member))
    simp only [formation, spanOpening]
    omega

/-- **(B) A balanced closure renews forever.** -/
theorem balanced_closure_renews (law : ChannelLaw Kind) (C : List Kind) (N : Nat)
    (nonempty : C ≠ [])
    (positive : ∀ k, k ∈ C → 0 < law.span k) (bound : ∀ k, k ∈ C → law.span k ≤ N)
    (supported : ∀ k, k ∈ C → ∃ j, j ∈ C ∧ law.edge j k ∧ 2 ≤ law.span j)
    (each : ∀ k, k ∈ C → law.demand k ≤ law.rate k * law.span k) :
    ∃ states : Nat → Config Kind, ∃ ticks : Nat → List Kind,
      ∀ n, (renewingProcess law).step (states n) (ticks n) (states (n + 1)) :=
  steady_endless law C N 0 nonempty positive bound supported (balanced_of_each law C each)

theorem mem_append_replicate {C : List Kind} {q k : Kind} {n : Nat}
    (member : k ∈ C ++ List.replicate n q) : k ∈ C ∨ k = q := by
  cases List.mem_append.mp member with
  | inl here => exact Or.inl here
  | inr there => exact Or.inr (List.eq_of_mem_replicate there)

theorem append_nonempty {C D : List Kind} (nonempty : C ≠ []) : C ++ D ≠ [] := by
  cases C with
  | nil => exact False.elim (nonempty rfl)
  | cons k rest => exact List.cons_ne_nil _ _

/-- Enough formations of an excess kind cover any population's shortfall. -/
theorem balanced_with_excess (law : ChannelLaw Kind) (C : List Kind) (q : Kind)
    (excess : law.demand q + 1 ≤ law.rate q * law.span q) :
    formation law (C ++ List.replicate (formation law C) q) ≤
      spanOpening law (C ++ List.replicate (formation law C) q) := by
  rw [formation_append, spanOpening_append, formation_replicate, spanOpening_replicate]
  have scaled := Nat.mul_le_mul_left (formation law C) excess
  rw [Nat.mul_add, Nat.mul_one] at scaled
  omega

/-- **(E) A closure that supports an excess kind renews forever.** The closure's
own kinds may fall short; enough formations of the excess kind cover them. -/
theorem excess_supported_by_closure_renews (law : ChannelLaw Kind) (C : List Kind)
    (q : Kind) (N : Nat) (nonempty : C ≠ [])
    (positive : ∀ k, k ∈ C → 0 < law.span k) (bound : ∀ k, k ∈ C → law.span k ≤ N)
    (qPositive : 0 < law.span q) (qBound : law.span q ≤ N)
    (supported : ∀ k, k ∈ C → ∃ j, j ∈ C ∧ law.edge j k ∧ 2 ≤ law.span j)
    (qSupported : ∃ j, j ∈ C ∧ law.edge j q ∧ 2 ≤ law.span j)
    (excess : law.demand q + 1 ≤ law.rate q * law.span q) :
    ∃ states : Nat → Config Kind, ∃ ticks : Nat → List Kind,
      ∀ n, (renewingProcess law).step (states n) (ticks n) (states (n + 1)) := by
  refine steady_endless law (C ++ List.replicate (formation law C) q) N 0
    (append_nonempty nonempty) ?_ ?_ ?_ (balanced_with_excess law C q excess)
  · intro k member
    cases mem_append_replicate member with
    | inl here => exact positive k here
    | inr same => exact same ▸ qPositive
  · intro k member
    cases mem_append_replicate member with
    | inl here => exact bound k here
    | inr same => exact same ▸ qBound
  · intro k member
    cases mem_append_replicate member with
    | inl here =>
      have ⟨j, jIn, edgeJK, long⟩ := supported k here
      exact ⟨j, List.mem_append_left _ jIn, edgeJK, long⟩
    | inr same =>
      have ⟨j, jIn, edgeJQ, long⟩ := qSupported
      exact ⟨j, List.mem_append_left _ jIn, same ▸ edgeJQ, long⟩

/-- One self-supporting kind with rate 1, span 3 and demand 3: balanced. -/
def closedOpenBalanced : ChannelLaw Unit where
  edge _ _ := True
  span _ := 3
  demand _ := 3
  rate _ := 1

/-- The balanced version renews forever, unlike `closedOpenShort` (demand 4),
which `closed_open_short_cannot_renew_forever` shows cannot. Together they
show the renewal inequality is exactly where the boundary falls for this kind. -/
theorem closed_open_balanced_renews_forever :
    ∃ states : Nat → Config Unit, ∃ ticks : Nat → List Unit,
      ∀ n, (renewingProcess closedOpenBalanced).step (states n) (ticks n) (states (n + 1)) :=
  balanced_closure_renews closedOpenBalanced [()] 3 (List.cons_ne_nil _ _)
    (fun _ _ => Nat.zero_lt_succ 2) (fun _ _ => Nat.le_refl 3)
    (fun _ _ => ⟨(), List.mem_singleton_self _, True.intro, Nat.le_succ 2⟩)
    (fun _ _ => Nat.le_refl 3)

#print axioms aged_append
#print axioms opened_append
#print axioms aged_block
#print axioms block_beyond
#print axioms formed_eq_block_zero
#print axioms steady_shift
#print axioms steady_fixed
#print axioms opened_block
#print axioms capped_step
#print axioms sum_map_add
#print axioms sum_map_zero
#print axioms opened_steady
#print axioms spanOpening_eq
#print axioms mem_block
#print axioms block_one_survives
#print axioms steady_renews
#print axioms steady_endless
#print axioms formation_append
#print axioms spanOpening_append
#print axioms formation_replicate
#print axioms spanOpening_replicate
#print axioms balanced_of_each
#print axioms balanced_closure_renews
#print axioms mem_append_replicate
#print axioms append_nonempty
#print axioms balanced_with_excess
#print axioms excess_supported_by_closure_renews
#print axioms closed_open_balanced_renews_forever

end Generative.Conditional.Renewal
