import RenewalSufficiency
import RenewalLink

/-!
# The renewal–closure theorem

Phase 2 of the renewal–closure roadmap. Under a supplied constraint–flow law
with finitely many kinds, the following are equivalent:
- some history of `channelProcess` stays live forever, with no organization
  imported after the start;
- some nonempty population of kinds is closed under support by constraints that
  outlast a tick, and its tokens open over their spans at least what forming
  them demands.

The second condition is checked on the law alone. It covers the two earlier
cases. A closure whose kinds each bring in enough is one instance. A closure
that supports a kind bringing in more than its demand is another, with enough
repeats of that kind.

When no such population exists, every history stops being live by an
explicit time. That time is fixed by the number of kinds, the longest span, the
longest remaining span among the initial tokens, and the opening potential
(reserve plus what live tokens can still open) one window after those tokens
have run out. With positive formation demands, it is fixed by the law and the
initial configuration alone. The longest span and the largest rate are read off
the finite list of kinds; nothing bounds them in advance. A history may start
from any configuration: initial tokens may hold more than their kind's span,
and spans may be zero.

Necessity runs as follows.
- If a kind that brings in more than its demand is formed late, its formation
  descends from a realized cycle. The cycle plus the walk to that kind is a
  self-renewing population.
- Otherwise, the opening potential cannot rise. Each formation of a kind that
  falls short lowers it by at least one. So some window of length
  `(n + 1) · D + 1` contains no such formation, and the closure that the
  configuration at its end descends from consists of kinds that bring in
  enough.

The proof is carried out for designated kinds (`renewal_keeping_theorem`).
Some history keeps a live token of a designated kind at every time exactly
when some self-renewing population contains a designated kind of positive span.
Renewal itself
is the case where every kind is designated. Records and readers, the
means of correction, can be designated. A closure can then renew forever while
a correction kind it supports cannot be kept (`lapsing_correction_cannot_be_kept`).

Kinds, edges, spans, demands and rates are supplied. Nothing here says which
history occurs, or that continuation is favorable.
-/

namespace Generative.Conditional.Renewal

open Generative

universe u

variable {Kind : Type u}

/-- Kinds closed under support by constraints that outlast a tick. -/
def SupportClosed (law : ChannelLaw Kind) (B : List Kind) : Prop :=
  ∀ k, k ∈ B → ∃ j, j ∈ B ∧ law.edge j k ∧ 2 ≤ law.span j

/-- A self-renewing population: nonempty, closed under support, and opening over
its tokens' spans at least what forming them demands. -/
def SelfRenewing (law : ChannelLaw Kind) (B : List Kind) : Prop :=
  B ≠ [] ∧ SupportClosed law B ∧ formation law B ≤ spanOpening law B

/-- Some history, from any start, stays live forever. -/
def RenewsForever (law : ChannelLaw Kind) : Prop :=
  ∃ H : History law, ∀ n, Live (H.states n)

/-! ## Sufficiency -/

theorem block_within (law : ChannelLaw Kind) (d : Nat) {tok : Token Kind} :
    ∀ {B : List Kind}, tok ∈ block law d B → tok.remaining ≤ law.span tok.kind
  | [], member => by cases member
  | k :: rest, member => by
    by_cases young : d < law.span k
    · rw [block, if_pos young] at member
      cases List.mem_cons.mp member with
      | inl same => subst same; exact Nat.sub_le _ _
      | inr tail => exact block_within law d tail
    · rw [block, if_neg young] at member
      exact block_within law d member

theorem steady_within (law : ChannelLaw Kind) (B : List Kind) {tok : Token Kind} :
    ∀ {N : Nat}, tok ∈ steady law B N → tok.remaining ≤ law.span tok.kind
  | 0, member => by cases member
  | N + 1, member => by
    cases List.mem_append.mp member with
    | inl here => exact block_within law N here
    | inr there => exact steady_within law B there

/-- The steady configuration of a self-renewing population, as an execution. -/
def steadyExecution (law : ChannelLaw Kind) (B : List Kind) (N : Nat)
    (nonempty : B ≠ []) (positive : ∀ k, k ∈ B → 0 < law.span k)
    (bound : ∀ k, k ∈ B → law.span k ≤ N) (supported : SupportClosed law B)
    (balanced : formation law B ≤ spanOpening law B) : Execution law where
  states _ := ⟨0, steady law B N⟩
  ticks _ := B
  steps _ := (steady_renews law B N 0 nonempty positive bound supported balanced).2
  initialWithinSpan _ member := steady_within law B member

/-- The kinds of a list whose span is positive. -/
def positivePart (law : ChannelLaw Kind) : List Kind → List Kind
  | [] => []
  | k :: rest => if 0 < law.span k then k :: positivePart law rest else positivePart law rest

theorem mem_positivePart (law : ChannelLaw Kind) {k : Kind} :
    ∀ {B : List Kind}, k ∈ positivePart law B → k ∈ B ∧ 0 < law.span k
  | [], member => by cases member
  | j :: rest, member => by
    by_cases positive : 0 < law.span j
    · rw [positivePart, if_pos positive] at member
      cases List.mem_cons.mp member with
      | inl same => subst same; exact ⟨List.mem_cons_self, positive⟩
      | inr tail =>
        obtain ⟨inside, kPositive⟩ := mem_positivePart law tail
        exact ⟨List.mem_cons_of_mem _ inside, kPositive⟩
    · rw [positivePart, if_neg positive] at member
      obtain ⟨inside, kPositive⟩ := mem_positivePart law member
      exact ⟨List.mem_cons_of_mem _ inside, kPositive⟩

theorem positivePart_mem (law : ChannelLaw Kind) {k : Kind} (positive : 0 < law.span k) :
    ∀ {B : List Kind}, k ∈ B → k ∈ positivePart law B
  | [], member => by cases member
  | j :: rest, member => by
    by_cases jPositive : 0 < law.span j
    · rw [positivePart, if_pos jPositive]
      cases List.mem_cons.mp member with
      | inl same => subst same; exact List.mem_cons_self
      | inr tail => exact List.mem_cons_of_mem _ (positivePart_mem law positive tail)
    · rw [positivePart, if_neg jPositive]
      cases List.mem_cons.mp member with
      | inl same => subst same; exact False.elim (jPositive positive)
      | inr tail => exact positivePart_mem law positive tail

theorem positivePart_balance (law : ChannelLaw Kind) :
    ∀ B : List Kind, formation law (positivePart law B) ≤ formation law B ∧
      spanOpening law (positivePart law B) = spanOpening law B
  | [] => ⟨Nat.le_refl 0, rfl⟩
  | k :: rest => by
    obtain ⟨lower, same⟩ := positivePart_balance law rest
    by_cases positive : 0 < law.span k
    · rw [positivePart, if_pos positive]
      simp only [formation, spanOpening]
      exact ⟨Nat.add_le_add_left lower _, by rw [same]⟩
    · rw [positivePart, if_neg positive]
      have zero : law.span k = 0 := by omega
      simp only [formation, spanOpening, zero, Nat.mul_zero, Nat.zero_add]
      exact ⟨Nat.le_trans lower (Nat.le_add_left _ _), same⟩

/-- Kinds with span zero open nothing, so dropping them keeps a population
self-renewing. -/
theorem positivePart_renewing (law : ChannelLaw Kind) {B : List Kind}
    (renewing : SelfRenewing law B) : SelfRenewing law (positivePart law B) := by
  obtain ⟨nonempty, supported, balanced⟩ := renewing
  obtain ⟨lower, same⟩ := positivePart_balance law B
  refine ⟨?_, ?_, ?_⟩
  · cases B with
    | nil => exact False.elim (nonempty rfl)
    | cons k rest =>
      obtain ⟨j, jIn, _, spanJ⟩ := supported k List.mem_cons_self
      intro empty
      have inside := positivePart_mem law (Nat.lt_of_lt_of_le (Nat.zero_lt_succ 1) spanJ) jIn
      rw [empty] at inside
      cases inside
  · intro k member
    obtain ⟨kIn, _⟩ := mem_positivePart law member
    obtain ⟨j, jIn, edge, spanJ⟩ := supported k kIn
    exact ⟨j, positivePart_mem law (Nat.lt_of_lt_of_le (Nat.zero_lt_succ 1) spanJ) jIn, edge,
      spanJ⟩
  · rw [same]
    exact Nat.le_trans lower balanced

/-- The steady execution of the positive part of a self-renewing population. -/
def standingExecution (law : ChannelLaw Kind) {B : List Kind}
    (renewing : SelfRenewing law B) : Execution law :=
  steadyExecution law (positivePart law B) (maxOver law.span (positivePart law B))
    (positivePart_renewing law renewing).1 (fun _ member => (mem_positivePart law member).2)
    (fun _ member => le_maxOver law.span member) (positivePart_renewing law renewing).2.1
    (positivePart_renewing law renewing).2.2

theorem standingExecution_live (law : ChannelLaw Kind) {B : List Kind}
    (renewing : SelfRenewing law B) (n : Nat) :
    Live ((standingExecution law renewing).states n) :=
  (steady_renews law (positivePart law B) (maxOver law.span (positivePart law B)) 0
    (positivePart_renewing law renewing).1 (fun _ member => (mem_positivePart law member).2)
    (fun _ member => le_maxOver law.span member) (positivePart_renewing law renewing).2.1
    (positivePart_renewing law renewing).2.2).1

/-- **Sufficiency.** A self-renewing population renews forever from its steady
configuration, with no reserve. -/
theorem self_renewing_renews_forever (law : ChannelLaw Kind) {B : List Kind}
    (renewing : SelfRenewing law B) : RenewsForever law :=
  ⟨(standingExecution law renewing).toHistory, standingExecution_live law renewing⟩

/-! ## Searches -/

/-- A decided search through a stretch of ticks. -/
theorem range_search (P : Nat → Prop) (decide : ∀ m, P m ∨ ¬ P m) (a : Nat) :
    ∀ L, (∃ m, a ≤ m ∧ m < a + L ∧ P m) ∨ (∀ m, a ≤ m → m < a + L → ¬ P m)
  | 0 => Or.inr (fun m low high _ => by omega)
  | L + 1 =>
    match range_search P decide a L, decide (a + L) with
    | Or.inl ⟨m, low, high, holds⟩, _ => Or.inl ⟨m, low, by omega, holds⟩
    | Or.inr _, Or.inl here => Or.inl ⟨a + L, Nat.le_add_right a L, by omega, here⟩
    | Or.inr absent, Or.inr notHere => Or.inr (fun m low high =>
        if same : m = a + L then same ▸ notHere else absent m low (by omega))

/-- Whether some kind formed on a tick has a decidable property. -/
theorem tick_search (law : ChannelLaw Kind) (X : Execution law) (Q : Kind → Prop)
    [DecidablePred Q] (m : Nat) :
    (∃ k, k ∈ X.ticks m ∧ Q k) ∨ ¬ ∃ k, k ∈ X.ticks m ∧ Q k :=
  match find_or_none Q (X.ticks m) with
  | Or.inl found => Or.inl found
  | Or.inr absent => Or.inr (fun ⟨k, member, holds⟩ => absent k member holds)

/-! ## The opening potential when nothing brings in more than its demand -/

theorem weighted_formed_eq (law : ChannelLaw Kind) :
    ∀ births : List Kind, weighted law.rate (formed law births) = spanOpening law births
  | [] => rfl
  | k :: rest => by
    simp only [formed, weighted, spanOpening, weighted_formed_eq law rest]

theorem spanOpening_le_formation (law : ChannelLaw Kind) :
    ∀ births : List Kind, (∀ k, k ∈ births → law.rate k * law.span k ≤ law.demand k) →
      spanOpening law births ≤ formation law births
  | [], _ => Nat.le_refl 0
  | k :: rest, each => by
    have here := each k List.mem_cons_self
    have ih := spanOpening_le_formation law rest
      (fun j member => each j (List.mem_cons_of_mem _ member))
    simp only [formation, spanOpening]
    omega

theorem spanOpening_lt_formation (law : ChannelLaw Kind) :
    ∀ births : List Kind, (∀ k, k ∈ births → law.rate k * law.span k ≤ law.demand k) →
      (∃ k, k ∈ births ∧ law.rate k * law.span k + 1 ≤ law.demand k) →
      spanOpening law births + 1 ≤ formation law births
  | [], _, short => by
    obtain ⟨k, member, _⟩ := short
    cases member
  | k :: rest, each, short => by
    obtain ⟨j, member, shortJ⟩ := short
    have here := each k List.mem_cons_self
    have restEach : ∀ i, i ∈ rest → law.rate i * law.span i ≤ law.demand i :=
      fun i inside => each i (List.mem_cons_of_mem _ inside)
    simp only [formation, spanOpening]
    cases List.mem_cons.mp member with
    | inl same =>
      subst same
      have ih := spanOpening_le_formation law rest restEach
      omega
    | inr tail =>
      have ih := spanOpening_lt_formation law rest restEach ⟨j, tail, shortJ⟩
      omega

/-- The opening potential of an execution at time `m`. -/
def potential {law : ChannelLaw Kind} (X : Execution law) (m : Nat) : Nat :=
  openingPotential law (X.states m)

theorem tick_potential {law : ChannelLaw Kind} (X : Execution law) (m : Nat)
    (each : ∀ k, k ∈ X.ticks m → law.rate k * law.span k ≤ law.demand k) :
    potential X (m + 1) ≤ potential X m := by
  have step := opening_step law (X.steps m)
  rw [weighted_formed_eq] at step
  have enough := spanOpening_le_formation law (X.ticks m) each
  simp only [potential]
  omega

theorem tick_potential_short {law : ChannelLaw Kind} (X : Execution law) (m : Nat)
    (each : ∀ k, k ∈ X.ticks m → law.rate k * law.span k ≤ law.demand k)
    (short : ∃ k, k ∈ X.ticks m ∧ law.rate k * law.span k + 1 ≤ law.demand k) :
    potential X (m + 1) + 1 ≤ potential X m := by
  have step := opening_step law (X.steps m)
  rw [weighted_formed_eq] at step
  have enough := spanOpening_lt_formation law (X.ticks m) each short
  clear short
  simp only [potential]
  omega

/-- Over a stretch with no formation of a kind that brings in more than its
demand, the opening potential does not rise. -/
theorem stretch_potential {law : ChannelLaw Kind} (X : Execution law) (a : Nat) :
    ∀ L, (∀ m, a ≤ m → m < a + L → ∀ k, k ∈ X.ticks m →
        law.rate k * law.span k ≤ law.demand k) →
      potential X (a + L) ≤ potential X a
  | 0, _ => Nat.le_refl _
  | L + 1, each => by
    have earlier := stretch_potential X a L
      (fun m low high => each m low (by omega))
    have last := tick_potential X (a + L) (each (a + L) (Nat.le_add_right a L) (by omega))
    rw [← Nat.add_assoc]
    exact Nat.le_trans last earlier

/-- A formation of a kind that falls short within such a stretch lowers the
potential by at least one. -/
theorem stretch_potential_short {law : ChannelLaw Kind} (X : Execution law) (a L : Nat)
    (each : ∀ m, a ≤ m → m < a + L → ∀ k, k ∈ X.ticks m →
      law.rate k * law.span k ≤ law.demand k)
    (short : ∃ m, a ≤ m ∧ m < a + L ∧
      ∃ k, k ∈ X.ticks m ∧ law.rate k * law.span k + 1 ≤ law.demand k) :
    potential X (a + L) + 1 ≤ potential X a := by
  obtain ⟨m, low, high, shortAt⟩ := short
  have at_m := tick_potential_short X m (each m low high) shortAt
  clear shortAt
  have before := stretch_potential X a (m - a)
    (fun i lowI highI => each i lowI (by omega))
  have shape : a + (m - a) = m := by omega
  rw [shape] at before
  have after := stretch_potential X (m + 1) (a + L - (m + 1))
    (fun i lowI highI => each i (by omega) (by omega))
  have shape' : m + 1 + (a + L - (m + 1)) = a + L := by omega
  rw [shape'] at after
  omega

/-! ## Necessity -/

/-- A closed walk with a walk leaving it: together they are support-closed and
contain the walk's end. -/
theorem cycle_with_tail {edge : Kind → Kind → Prop} {j q : Kind}
    {cycle rest : List Kind} (nonempty : cycle ≠ [])
    (loop : Walk edge j (j :: cycle) j) (tail : Walk edge j (j :: rest) q)
    (closed : DependenceClosed edge cycle) :
    (∀ v, v ∈ cycle ++ rest → ∃ u, u ∈ cycle ++ rest ∧ edge u v) ∧ q ∈ cycle ++ rest := by
  have jIn : j ∈ cycle := by
    cases loop with
    | cons _ rest' => exact rest'.end_mem
    | nil => exact False.elim (nonempty rfl)
  have inside : ∀ v, v ∈ j :: rest → v ∈ cycle ++ rest := by
    intro v member
    cases List.mem_cons.mp member with
    | inl same => exact List.mem_append_left _ (same ▸ jIn)
    | inr tail => exact List.mem_append_right _ tail
  refine ⟨?_, inside q tail.end_mem⟩
  intro v member
  cases List.mem_append.mp member with
  | inl here =>
    obtain ⟨u, uIn, edgeUV⟩ := closed.2.1 v here
    exact ⟨u, List.mem_append_left _ uIn, edgeUV⟩
  | inr there =>
    obtain ⟨after, shape, preds⟩ := tail.after_start
    injection shape with _ same
    rw [← same] at preds
    obtain ⟨u, uIn, edgeUV⟩ := preds v there
    exact ⟨u, inside u uIn, edgeUV⟩

/-- An excess kind supported from a support-closed list gives a self-renewing
population: the list plus enough repeats of the excess kind. -/
theorem excess_population (law : ChannelLaw Kind) {C : List Kind} {q : Kind}
    (nonempty : C ≠ []) (closedC : SupportClosed law C) (qIn : q ∈ C)
    (excess : law.demand q + 1 ≤ law.rate q * law.span q) :
    SelfRenewing law (C ++ List.replicate (formation law C) q) := by
  refine ⟨append_nonempty nonempty, ?_, balanced_with_excess law C q excess⟩
  intro k member
  have supportedIn : ∃ j, j ∈ C ∧ law.edge j k ∧ 2 ≤ law.span j := by
    cases mem_append_replicate member with
    | inl here => exact closedC k here
    | inr same => exact same ▸ closedC q qIn
  obtain ⟨j, jIn, edgeJK, spanJ⟩ := supportedIn
  exact ⟨j, List.mem_append_left _ jIn, edgeJK, spanJ⟩

/-! ## Keeping designated kinds -/

/-- The configuration holds a live token of a designated kind. -/
def Keeps (K : Kind → Prop) (c : Config Kind) : Prop :=
  ∃ tok, tok ∈ c.tokens ∧ 1 ≤ tok.remaining ∧ K tok.kind

/-- Some history keeps a live token of a designated kind at every time. -/
def KeepsForever (law : ChannelLaw Kind) (K : Kind → Prop) : Prop :=
  ∃ H : History law, ∀ n, Keeps K (H.states n)

theorem keeps_decide (K : Kind → Prop) [DecidablePred K] (c : Config Kind) :
    Keeps K c ∨ ¬ Keeps K c :=
  match find_or_none (fun tok : Token Kind => 1 ≤ tok.remaining ∧ K tok.kind) c.tokens with
  | Or.inl ⟨tok, member, alive, kind⟩ => Or.inl ⟨tok, member, alive, kind⟩
  | Or.inr absent => Or.inr (fun ⟨tok, member, alive, kind⟩ => absent tok member ⟨alive, kind⟩)

theorem live_keeps_everything {c : Config Kind} (live : Live c) : Keeps (fun _ => True) c :=
  match live_has_alive_token live with
  | ⟨tok, member, alive⟩ => ⟨tok, member, alive, True.intro⟩

theorem support_closed_append {law : ChannelLaw Kind} {C E : List Kind}
    (closedC : SupportClosed law C) (closedE : SupportClosed law E) :
    SupportClosed law (C ++ E) := by
  intro k member
  cases List.mem_append.mp member with
  | inl here =>
    obtain ⟨j, jIn, edgeJK, spanJ⟩ := closedC k here
    exact ⟨j, List.mem_append_left _ jIn, edgeJK, spanJ⟩
  | inr there =>
    obtain ⟨j, jIn, edgeJK, spanJ⟩ := closedE k there
    exact ⟨j, List.mem_append_right _ jIn, edgeJK, spanJ⟩

/-- A cycle with a walk leaving it, in the support relation of an execution, as
a support-closed list containing the walk's end. -/
theorem traced_support_closed {law : ChannelLaw Kind} {j r : Kind}
    {cycle rest : List Kind} (nonempty : cycle ≠ [])
    (loop : Walk (fun a b => law.edge a b ∧ 2 ≤ law.span a) j (j :: cycle) j)
    (tail : Walk (fun a b => law.edge a b ∧ 2 ≤ law.span a) j (j :: rest) r)
    (closed : DependenceClosed (fun a b => law.edge a b ∧ 2 ≤ law.span a) cycle) :
    SupportClosed law (cycle ++ rest) ∧ r ∈ cycle ++ rest := by
  obtain ⟨closedAll, rIn⟩ := cycle_with_tail nonempty loop tail closed
  refine ⟨?_, rIn⟩
  intro v member
  obtain ⟨u, uIn, edgeUV, spanU⟩ := closedAll v member
  exact ⟨u, uIn, edgeUV, spanU⟩

/-- A live token of a designated kind late in an execution descends from a
realized cycle through a walk. Every kind on both was formed in the preceding
`(n + 1) · D` ticks. -/
theorem kept_kind_descends {law : ChannelLaw Kind} (X : Execution law)
    (U : List Kind) (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    {K : Kind → Prop} {t : Nat} (late : (U.length + 1) * D < t) (keeps : Keeps K (X.states t)) :
    ∃ r j cycle rest, K r ∧ 0 < law.span r ∧ cycle ≠ [] ∧
      Walk (fun a b => law.edge a b ∧ 2 ≤ law.span a) j (j :: cycle) j ∧
      Walk (fun a b => law.edge a b ∧ 2 ≤ law.span a) j (j :: rest) r ∧
      DependenceClosed (fun a b => law.edge a b ∧ 2 ≤ law.span a) cycle ∧
      ∀ v, v ∈ cycle ++ rest → ∃ s, (executionSupport X).occurs v s ∧ s ≤ t ∧
        t < s + (U.length + 1) * D := by
  obtain ⟨tok, member, alive, kTok⟩ := keeps
  have spanPositive : 0 < law.span tok.kind :=
    Nat.lt_of_lt_of_le alive (execution_within X t tok member)
  have Dlate : D < t := by
    have : D ≤ (U.length + 1) * D := by
      rw [Nat.succ_mul]
      exact Nat.le_add_left _ _
    omega
  obtain ⟨s, occ, before, near⟩ := alive_token_recent_formation X D spanBound member alive Dlate
  have reachBound : ∀ j, (executionSupport X).reach j ≤ D := by
    intro j
    have := spanBound j
    show law.span j - 1 ≤ D
    omega
  have lateS : U.length * D < s := by
    rw [Nat.succ_mul] at late
    omega
  obtain ⟨j, cycle, rest, nonempty, loop, tail, closed, window⟩ :=
    late_occurrence_descends_from_realized_closure (executionSupport X) U complete D
      reachBound occ lateS
  refine ⟨tok.kind, j, cycle, rest, kTok, spanPositive, nonempty, loop, tail, closed, ?_⟩
  intro v inside
  obtain ⟨r, occV, beforeV, nearV⟩ := window v inside
  refine ⟨r, occV, Nat.le_trans beforeV before, ?_⟩
  rw [Nat.succ_mul]
  omega

/-- **The window theorem, for designated kinds.** If an execution holds a live
token of a designated kind at every time up to `(P + 2) · W`, the law has a
self-renewing population containing a designated kind of positive span. Here
`W` is `(n + 1) · D + 1` and `P` is the opening potential at time `W`. Nothing
about the designated kinds needs to be decided. -/
theorem kept_through_window_has_population (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (K : Kind → Prop) (X : Execution law)
    (kept : ∀ t, t ≤ (potential X ((U.length + 1) * D + 1) + 2) * ((U.length + 1) * D + 1) →
      Keeps K (X.states t)) :
    ∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k ∧ 0 < law.span k := by
  generalize hW : (U.length + 1) * D + 1 = W at kept
  generalize hP : potential X W = P at kept
  have reachBound : ∀ j, (executionSupport X).reach j ≤ D := by
    intro j
    have := spanBound j
    show law.span j - 1 ≤ D
    omega
  have Wlate : (U.length + 1) * D < W := by omega
  cases range_search
      (fun m => ∃ k, k ∈ X.ticks m ∧ law.demand k + 1 ≤ law.rate k * law.span k)
      (tick_search law X _) W ((P + 1) * W) with
  | inl found =>
    -- A late formation of an excess kind descends from a realized cycle, and so
    -- does a designated kind kept at time `W`.
    obtain ⟨m, low, _, q, inTick, excess⟩ := found
    have keepsW : Keeps K (X.states W) := by
      apply kept W
      have : 1 * W ≤ (P + 2) * W := Nat.mul_le_mul_right W (by omega)
      rw [Nat.one_mul] at this
      exact this
    obtain ⟨r, j₂, cycle₂, rest₂, kR, rPositive, nonempty₂, loop₂, tail₂, closed₂, _⟩ :=
      kept_kind_descends X U complete D spanBound Wlate keepsW
    obtain ⟨closedR, rIn⟩ := traced_support_closed nonempty₂ loop₂ tail₂ closed₂
    have occ : (executionSupport X).occurs q (m + 1) := Or.inr ⟨m, rfl, inTick⟩
    have late : U.length * D < m + 1 := by
      rw [Nat.succ_mul] at hW
      omega
    obtain ⟨j, cycle, rest, nonempty, loop, tail, closed, _⟩ :=
      late_occurrence_descends_from_realized_closure (executionSupport X) U complete D
        reachBound occ late
    obtain ⟨closedQ, qIn⟩ := traced_support_closed nonempty loop tail closed
    have closedC := support_closed_append closedQ closedR
    have nonemptyC : (cycle ++ rest) ++ (cycle₂ ++ rest₂) ≠ [] :=
      append_nonempty (append_nonempty nonempty)
    exact ⟨_, excess_population law nonemptyC closedC (List.mem_append_left _ qIn)
      excess, r, List.mem_append_left _ (List.mem_append_right _ rIn), kR, rPositive⟩
  | inr noExcess =>
    have each : ∀ m, W ≤ m → m < W + (P + 1) * W → ∀ k, k ∈ X.ticks m →
        law.rate k * law.span k ≤ law.demand k := by
      intro m low high k member
      have notExcess := noExcess m low high
      exact Nat.le_of_not_lt (fun bigger => notExcess ⟨k, member, bigger⟩)
    -- Some window of length `W` has no formation of a kind that falls short.
    have windows : ∀ i, i ≤ P + 1 →
        (∃ w, w < i ∧ ∀ m, W + w * W ≤ m → m < W + w * W + W → ∀ k, k ∈ X.ticks m →
          law.demand k ≤ law.rate k * law.span k) ∨
        potential X (W + i * W) + i ≤ P := by
      intro i
      induction i with
      | zero =>
        intro _
        refine Or.inr ?_
        rw [Nat.zero_mul, Nat.add_zero, Nat.add_zero, hP]
        exact Nat.le_refl P
      | succ i ih =>
        intro within
        cases ih (Nat.le_of_succ_le within) with
        | inl earlier =>
          obtain ⟨w, below, good⟩ := earlier
          exact Or.inl ⟨w, Nat.lt_succ_of_lt below, good⟩
        | inr bound =>
          have inRange : W + i * W + W ≤ W + (P + 1) * W := by
            have := Nat.mul_le_mul_right W within
            rw [Nat.succ_mul] at this
            omega
          have eachHere : ∀ m, W + i * W ≤ m → m < W + i * W + W → ∀ k, k ∈ X.ticks m →
              law.rate k * law.span k ≤ law.demand k :=
            fun m low high => each m (by omega) (by omega)
          cases range_search
              (fun m => ∃ k, k ∈ X.ticks m ∧ law.rate k * law.span k + 1 ≤ law.demand k)
              (tick_search law X _) (W + i * W) W with
          | inl shortFound =>
            have drop := stretch_potential_short X (W + i * W) W eachHere shortFound
            clear shortFound
            refine Or.inr ?_
            have shape : W + (i + 1) * W = W + i * W + W := by
              rw [Nat.succ_mul, Nat.add_assoc]
            rw [shape]
            omega
          | inr noShort =>
            refine Or.inl ⟨i, Nat.lt_succ_self i, ?_⟩
            intro m low high k member
            have notShort := noShort m low high
            exact Nat.le_of_not_lt (fun bigger => notShort ⟨k, member, bigger⟩)
    have found : ∃ w, w < P + 1 ∧ ∀ m, W + w * W ≤ m → m < W + w * W + W →
        ∀ k, k ∈ X.ticks m → law.demand k ≤ law.rate k * law.span k := by
      cases windows (P + 1) (Nat.le_refl _) with
      | inl good => exact good
      | inr impossible => exact False.elim (by omega)
    obtain ⟨w, below, good⟩ := found
    -- At the end of that window, either no designated kind is kept, or the one
    -- kept descends from a cycle and walk of kinds that bring in enough.
    have endBound : W + w * W + W ≤ (P + 2) * W := by
      have := Nat.mul_le_mul_right W (Nat.le_of_lt_succ below)
      have shape : (P + 2) * W = W + P * W + W := by
        rw [Nat.succ_mul, Nat.succ_mul]
        omega
      omega
    have keepsEnd := kept (W + w * W + W) endBound
    have late : (U.length + 1) * D < W + w * W + W := by omega
    obtain ⟨r, _, cycle, rest, kR, rPositive, nonempty, loop, tail, closed, window⟩ :=
      kept_kind_descends X U complete D spanBound late keepsEnd
    have adequate : ∀ v, v ∈ cycle ++ rest → law.demand v ≤ law.rate v * law.span v := by
      intro v member
      obtain ⟨s, occ, before, near⟩ := window v member
      cases occ with
      | inl initial =>
        obtain ⟨zero, _⟩ := initial
        exact False.elim (by omega)
      | inr formedAt =>
        obtain ⟨m, timeEq, inTick⟩ := formedAt
        exact good m (by omega) (by omega) v inTick
    obtain ⟨closedC, rIn⟩ := traced_support_closed nonempty loop tail closed
    exact ⟨cycle ++ rest, ⟨append_nonempty nonempty, closedC,
      balanced_of_each law _ adequate⟩, r, rIn, kR, rPositive⟩

/-- **The dichotomy, for designated kinds.** For any execution, either the law
has a self-renewing population containing a designated kind of positive span,
or the execution holds no live token of a designated kind at some time by
`(P + 2) · W`. Naming that time needs the designated kinds to be decidable. -/
theorem renewal_dichotomy_keeping (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (K : Kind → Prop) [DecidablePred K] (X : Execution law) :
    (∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k ∧ 0 < law.span k) ∨
      ∃ t, t ≤ (potential X ((U.length + 1) * D + 1) + 2) * ((U.length + 1) * D + 1) ∧
        ¬ Keeps K (X.states t) := by
  have lostDecide : ∀ t, ¬ Keeps K (X.states t) ∨ ¬ ¬ Keeps K (X.states t) := fun t =>
    match keeps_decide K (X.states t) with
    | Or.inl keeps => Or.inr (fun lost => lost keeps)
    | Or.inr lost => Or.inl lost
  cases range_search (fun t => ¬ Keeps K (X.states t)) lostDecide 0
      ((potential X ((U.length + 1) * D + 1) + 2) * ((U.length + 1) * D + 1) + 1) with
  | inl found =>
    obtain ⟨t, _, high, lost⟩ := found
    rw [Nat.zero_add] at high
    exact Or.inr ⟨t, Nat.le_of_lt_succ high, lost⟩
  | inr notLost =>
    refine Or.inl (kept_through_window_has_population law U complete D spanBound K X ?_)
    intro t within
    cases keeps_decide K (X.states t) with
    | inl keeps => exact keeps
    | inr lost =>
      exact False.elim (notLost t (Nat.zero_le t)
        (by rw [Nat.zero_add]; exact Nat.lt_succ_of_le within) lost)

/-- **The dichotomy.** For any execution, either the law has a self-renewing
population, or the execution stops being live by `(P + 2) · W`. This is the
case where every kind is designated. -/
theorem renewal_dichotomy (law : ChannelLaw Kind) (U : List Kind)
    (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (X : Execution law) :
    (∃ B, SelfRenewing law B) ∨
      ∃ t, t ≤ (potential X ((U.length + 1) * D + 1) + 2) * ((U.length + 1) * D + 1) ∧
        ¬ Live (X.states t) := by
  cases renewal_dichotomy_keeping law U complete D spanBound (fun _ => True) X with
  | inl found =>
    obtain ⟨B, renewing, _⟩ := found
    exact Or.inl ⟨B, renewing⟩
  | inr dies =>
    obtain ⟨t, within, lost⟩ := dies
    exact Or.inr ⟨t, within, fun live => lost (live_keeps_everything live)⟩

/-- The longest span among the listed kinds. -/
theorem span_le_longest (law : ChannelLaw Kind) {U : List Kind} (complete : ∀ k, k ∈ U)
    (k : Kind) : law.span k ≤ maxOver law.span U :=
  le_maxOver law.span (complete k)

/-- **Necessity.** A history that stays live forever shows that the law has a
self-renewing population. -/
theorem renews_forever_has_self_renewing_population
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (endless : RenewsForever law) : ∃ B, SelfRenewing law B := by
  obtain ⟨H, alive⟩ := endless
  obtain ⟨B, renewing, _⟩ := kept_through_window_has_population law U complete
    (maxOver law.span U) (span_le_longest law complete) (fun _ => True) H.settled
    (fun t _ => live_keeps_everything (alive (H.settle + t)))
  exact ⟨B, renewing⟩

/-- **The renewal–closure theorem.** With finitely many kinds, a law admits a
history that renews forever exactly when it has a nonempty population of kinds,
closed under support by constraints that outlast a tick, whose tokens open over
their spans at least what forming them demands. -/
theorem renewal_closure_theorem (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) :
    RenewsForever law ↔ ∃ B, SelfRenewing law B :=
  ⟨renews_forever_has_self_renewing_population law U complete,
    fun ⟨_, renewing⟩ => self_renewing_renews_forever law renewing⟩

theorem steady_contains_fresh (law : ChannelLaw Kind) {B : List Kind} {k : Kind}
    (member : k ∈ B) (positive : 0 < law.span k) :
    ∀ N, 0 < N → ⟨k, law.span k⟩ ∈ steady law B N
  | 0, zero => False.elim (Nat.lt_irrefl 0 zero)
  | N + 1, _ => by
    cases N with
    | zero =>
      have fresh := mem_block law 0 member positive
      rw [Nat.sub_zero] at fresh
      exact List.mem_append_left _ fresh
    | succ M =>
      exact List.mem_append_right _ (steady_contains_fresh law member positive (M + 1)
        (Nat.zero_lt_succ M))

/-- **Keeping designated kinds.** With finitely many kinds, some history keeps a
live token of a designated kind at every time exactly when some self-renewing
population contains a designated kind of positive span. -/
theorem renewal_keeping_theorem (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (K : Kind → Prop) :
    KeepsForever law K ↔ ∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k ∧ 0 < law.span k := by
  constructor
  · intro keeps
    obtain ⟨H, always⟩ := keeps
    exact kept_through_window_has_population law U complete (maxOver law.span U)
      (span_le_longest law complete) K H.settled (fun t _ => always (H.settle + t))
  · intro population
    obtain ⟨B, renewing, k, kIn, kK, kPositive⟩ := population
    have kIn' := positivePart_mem law kPositive kIn
    refine ⟨(standingExecution law renewing).toHistory, fun _ => ?_⟩
    exact ⟨⟨k, law.span k⟩, steady_contains_fresh law kIn' kPositive _
      (Nat.lt_of_lt_of_le kPositive (le_maxOver law.span kIn')), kPositive, kK⟩

/-- The window of the dichotomy: one more than `n + 1` longest spans. -/
def renewalWindow (law : ChannelLaw Kind) (U : List Kind) : Nat :=
  (U.length + 1) * maxOver law.span U + 1

/-- Without a self-renewing population containing a designated kind of positive
span, every history loses its designated kinds by `s + (P + 2) · W`. Here `s` is
the longest remaining span among the initial tokens, `W` is `renewalWindow`, and
`P` is the opening potential at time `s + W`. -/
theorem no_keeping_population_deadline (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (K : Kind → Prop) [DecidablePred K]
    (absent : ¬ ∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k ∧ 0 < law.span k)
    (H : History law) :
    ∃ t, t ≤ H.settle + (openingPotential law (H.states (H.settle + renewalWindow law U)) + 2) *
        renewalWindow law U ∧ ¬ Keeps K (H.states t) := by
  cases renewal_dichotomy_keeping law U complete (maxOver law.span U)
      (span_le_longest law complete) K H.settled with
  | inl population => exact False.elim (absent population)
  | inr dies =>
    obtain ⟨t, within, lost⟩ := dies
    exact ⟨H.settle + t, Nat.add_le_add_left within _, lost⟩

/-- **The deadline.** Without a self-renewing population, every history stops
being live by `s + (P + 2) · W`. -/
theorem no_self_renewing_population_deadline (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (absent : ¬ ∃ B, SelfRenewing law B)
    (H : History law) :
    ∃ t, t ≤ H.settle + (openingPotential law (H.states (H.settle + renewalWindow law U)) + 2) *
        renewalWindow law U ∧ ¬ Live (H.states t) := by
  obtain ⟨t, within, lost⟩ := no_keeping_population_deadline law U complete (fun _ => True)
    (fun ⟨B, renewing, _⟩ => absent ⟨B, renewing⟩) H
  exact ⟨t, within, fun live => lost (live_keeps_everything live)⟩

/-! ## The deadline from the initial configuration -/

theorem opened_le_weighted (w : Kind → Nat) :
    ∀ l : List (Token Kind), opened w l ≤ weighted w l
  | [] => Nat.le_refl 0
  | tok :: rest => by
    have ih := opened_le_weighted w rest
    simp only [opened, weighted]
    by_cases zero : tok.remaining = 0
    · rw [if_pos zero]
      omega
    · rw [if_neg zero]
      have once : w tok.kind ≤ w tok.kind * tok.remaining :=
        Nat.le_mul_of_pos_right _ (Nat.pos_of_ne_zero zero)
      omega

theorem length_le_formation (law : ChannelLaw Kind) (demandPositive : ∀ k, 1 ≤ law.demand k) :
    ∀ births : List Kind, births.length ≤ formation law births
  | [] => Nat.le_refl 0
  | k :: rest => by
    have ih := length_le_formation law demandPositive rest
    have here := demandPositive k
    simp only [List.length_cons, formation]
    omega

theorem spanOpening_le_length (law : ChannelLaw Kind) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D) :
    ∀ births : List Kind, spanOpening law births ≤ A * D * births.length
  | [] => Nat.le_refl 0
  | k :: rest => by
    have ih := spanOpening_le_length law A D rateBound spanBound rest
    have here := Nat.mul_le_mul (rateBound k) (spanBound k)
    simp only [List.length_cons, spanOpening, Nat.mul_succ]
    omega

/-- With positive formation demands, one tick multiplies the opening potential
by at most `1 + A · D`: formations are paid from what is already held or
opened. -/
theorem potential_growth {law : ChannelLaw Kind} (H : History law) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D)
    (demandPositive : ∀ k, 1 ≤ law.demand k) (m : Nat) :
    openingPotential law (H.states (m + 1)) ≤ (1 + A * D) * openingPotential law (H.states m) := by
  have step := opening_step law (H.steps m)
  rw [weighted_formed_eq] at step
  have balance := (H.steps m).2.1
  have openBound := opened_le_weighted law.rate (H.states m).tokens
  have count := length_le_formation law demandPositive (H.ticks m)
  have opening := spanOpening_le_length law A D rateBound spanBound (H.ticks m)
  have few : (H.ticks m).length ≤ openingPotential law (H.states m) := by
    simp only [openingPotential]
    omega
  have scaled := Nat.mul_le_mul_left (A * D) few
  rw [Nat.add_mul, Nat.one_mul]
  omega

theorem potential_bound {law : ChannelLaw Kind} (H : History law) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D)
    (demandPositive : ∀ k, 1 ≤ law.demand k) :
    ∀ m, openingPotential law (H.states m) ≤
      (1 + A * D) ^ m * openingPotential law (H.states 0)
  | 0 => by rw [Nat.pow_zero, Nat.one_mul]; exact Nat.le_refl _
  | m + 1 => by
    have grow := potential_growth H A D rateBound spanBound demandPositive m
    have ih := Nat.mul_le_mul_left (1 + A * D) (potential_bound H A D rateBound spanBound
      demandPositive m)
    rw [Nat.pow_succ, Nat.mul_comm ((1 + A * D) ^ m) (1 + A * D), Nat.mul_assoc]
    exact Nat.le_trans grow ih

/-- The growth factor of the opening potential per tick: one plus the largest
rate times the longest span. -/
def renewalGrowth (law : ChannelLaw Kind) (U : List Kind) : Nat :=
  1 + maxOver law.rate U * maxOver law.span U

/-- **The explicit deadline, for designated kinds.** With positive formation
demands, and without a self-renewing population containing a designated kind of
positive span, every history loses its designated kinds by
`s + (G ^ (s + W) · P₀ + 2) · W`. Here `s` is the longest remaining span among
the initial tokens, `W` is `renewalWindow`, `G` is `renewalGrowth`, and `P₀` is
the initial reserve plus what the initial tokens can open. All of these are read
from the law and the initial configuration. -/
theorem no_keeping_population_explicit_deadline
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (demandPositive : ∀ k, 1 ≤ law.demand k)
    (K : Kind → Prop) [DecidablePred K]
    (absent : ¬ ∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k ∧ 0 < law.span k)
    (H : History law) :
    ∃ t, t ≤ H.settle + (renewalGrowth law U ^ (H.settle + renewalWindow law U) *
        openingPotential law (H.states 0) + 2) * renewalWindow law U ∧
      ¬ Keeps K (H.states t) := by
  obtain ⟨t, within, lost⟩ := no_keeping_population_deadline law U complete K absent H
  have grow := potential_bound H (maxOver law.rate U) (maxOver law.span U)
    (fun k => le_maxOver law.rate (complete k)) (span_le_longest law complete) demandPositive
    (H.settle + renewalWindow law U)
  refine ⟨t, Nat.le_trans within ?_, lost⟩
  exact Nat.add_le_add_left (Nat.mul_le_mul_right _ (Nat.add_le_add_right grow 2)) _

/-- **The explicit deadline.** With positive formation demands, and without a
self-renewing population, every history stops being live by
`s + (G ^ (s + W) · P₀ + 2) · W`. -/
theorem no_self_renewing_population_explicit_deadline
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (demandPositive : ∀ k, 1 ≤ law.demand k)
    (absent : ¬ ∃ B, SelfRenewing law B) (H : History law) :
    ∃ t, t ≤ H.settle + (renewalGrowth law U ^ (H.settle + renewalWindow law U) *
        openingPotential law (H.states 0) + 2) * renewalWindow law U ∧
      ¬ Live (H.states t) := by
  obtain ⟨t, within, lost⟩ := no_keeping_population_explicit_deadline law U complete
    demandPositive (fun _ => True) (fun ⟨B, renewing, _⟩ => absent ⟨B, renewing⟩) H
  exact ⟨t, within, fun live => lost (live_keeps_everything live)⟩

/-! ## Examples -/

/-- The law decides the single short kind: no population of it renews. -/
theorem closed_open_short_has_no_self_renewing_population :
    ¬ ∃ B, SelfRenewing closedOpenShort B := by
  intro found
  obtain ⟨B, nonempty, _, balanced⟩ := found
  have gap : ∀ B : List Unit,
      spanOpening closedOpenShort B + B.length ≤ formation closedOpenShort B := by
    intro B
    induction B with
    | nil => exact Nat.le_refl 0
    | cons k rest ih =>
      simp only [spanOpening, formation, List.length_cons]
      show 1 * 3 + spanOpening closedOpenShort rest + (rest.length + 1) ≤
        4 + formation closedOpenShort rest
      omega
  have short := gap B
  cases B with
  | nil => exact nonempty rfl
  | cons k rest =>
    simp only [List.length_cons] at short
    omega

/-- Two kinds. Kind `false` supports itself and kind `true`; it falls short
(rate 1, span 2, demand 5). Kind `true` supports nothing and brings in more
than its demand (rate 2, span 3, demand 1). -/
def danglingSupport : ChannelLaw Bool where
  edge a _ := a = false
  span k := if k then 3 else 2
  demand k := if k then 1 else 5
  rate k := if k then 2 else 1

/-- The closure alone falls short. -/
theorem dangling_closure_falls_short :
    danglingSupport.rate false * danglingSupport.span false + 1 ≤
      danglingSupport.demand false := by
  show 1 * 2 + 1 ≤ 5
  decide

/-- Kind `true` is in no closed set of the support relation: it supports
nothing. -/
theorem dangling_kind_outside_every_closure (C : List Bool)
    (closed : DependenceClosed
      (fun a b => danglingSupport.edge a b ∧ 2 ≤ danglingSupport.span a) C) :
    true ∉ C := by
  intro member
  obtain ⟨w, _, edgeTW, _⟩ := closed.2.2 true member
  exact Bool.noConfusion edgeTW

/-- Yet the law renews forever. Kind `true` contributes provision: the flow it
opens meets the formation demands of the closure that supports it. Read only
through support, a closure misses it. Read with provision as a second kind of
dependence, `true` is generative for `false`. -/
theorem dangling_support_renews_forever : RenewsForever danglingSupport := by
  refine self_renewing_renews_forever danglingSupport
    (B := [false, true, true, true, true, true]) ⟨List.cons_ne_nil _ _, ?_, ?_⟩
  · intro k _
    exact ⟨false, List.mem_cons_self, rfl, Nat.le_refl 2⟩
  · show 10 ≤ 32
    decide

/-- A closure that exactly renews itself (kind `false`: rate 1, span 3, demand
3) supports a correction kind (`true`: rate 1, span 3, demand 4) that falls
short. -/
def lapsingCorrection : ChannelLaw Bool where
  edge a _ := a = false
  span _ := 3
  demand k := if k then 4 else 3
  rate _ := 1

/-- The closure renews forever. -/
theorem lapsing_closure_renews_forever : RenewsForever lapsingCorrection :=
  self_renewing_renews_forever lapsingCorrection (B := [false])
    ⟨List.cons_ne_nil _ _, fun _ _ => ⟨false, List.mem_cons_self, rfl, Nat.le_succ 2⟩,
      Nat.le_refl 3⟩

theorem lapsing_balance :
    ∀ B : List Bool, spanOpening lapsingCorrection B ≤ formation lapsingCorrection B
  | [] => Nat.le_refl 0
  | k :: rest => by
    have ih := lapsing_balance rest
    cases k with
    | false =>
      show 1 * 3 + spanOpening lapsingCorrection rest ≤ 3 + formation lapsingCorrection rest
      omega
    | true =>
      show 1 * 3 + spanOpening lapsingCorrection rest ≤ 4 + formation lapsingCorrection rest
      omega

theorem lapsing_correction_gap :
    ∀ B : List Bool, true ∈ B →
      spanOpening lapsingCorrection B + 1 ≤ formation lapsingCorrection B
  | [], member => by cases member
  | k :: rest, member => by
    cases k with
    | false =>
      have inside : true ∈ rest := by
        cases List.mem_cons.mp member with
        | inl same => exact Bool.noConfusion same
        | inr tail => exact tail
      have ih := lapsing_correction_gap rest inside
      show 1 * 3 + spanOpening lapsingCorrection rest + 1 ≤
        3 + formation lapsingCorrection rest
      omega
    | true =>
      have ih := lapsing_balance rest
      show 1 * 3 + spanOpening lapsingCorrection rest + 1 ≤
        4 + formation lapsingCorrection rest
      omega

/-- **Correction lapses while the closure renews.** No execution keeps the
correction kind forever. Every execution loses it by an explicit time. -/
theorem lapsing_correction_cannot_be_kept :
    ¬ KeepsForever lapsingCorrection (fun k => k = true) := by
  intro keeps
  have complete : ∀ k : Bool, k ∈ [false, true] := by
    intro k
    cases k
    · exact List.mem_cons_self
    · exact List.mem_cons_of_mem _ List.mem_cons_self
  have population := (renewal_keeping_theorem lapsingCorrection [false, true] complete
    (fun k => k = true)).mp keeps
  obtain ⟨B, ⟨_, _, balanced⟩, k, kIn, kTrue, _⟩ := population
  subst kTrue
  have gap := lapsing_correction_gap B kIn
  omega

#print axioms block_within
#print axioms mem_positivePart
#print axioms positivePart_mem
#print axioms positivePart_balance
#print axioms positivePart_renewing
#print axioms standingExecution_live
#print axioms steady_within
#print axioms self_renewing_renews_forever
#print axioms range_search
#print axioms tick_search
#print axioms weighted_formed_eq
#print axioms spanOpening_le_formation
#print axioms spanOpening_lt_formation
#print axioms tick_potential
#print axioms tick_potential_short
#print axioms stretch_potential
#print axioms stretch_potential_short
#print axioms cycle_with_tail
#print axioms excess_population
#print axioms keeps_decide
#print axioms live_keeps_everything
#print axioms support_closed_append
#print axioms traced_support_closed
#print axioms kept_kind_descends
#print axioms kept_through_window_has_population
#print axioms renewal_dichotomy_keeping
#print axioms renewal_dichotomy
#print axioms steady_contains_fresh
#print axioms renewal_keeping_theorem
#print axioms no_keeping_population_deadline
#print axioms span_le_longest
#print axioms renews_forever_has_self_renewing_population
#print axioms renewal_closure_theorem
#print axioms no_self_renewing_population_deadline
#print axioms opened_le_weighted
#print axioms length_le_formation
#print axioms spanOpening_le_length
#print axioms potential_growth
#print axioms potential_bound
#print axioms no_keeping_population_explicit_deadline
#print axioms no_self_renewing_population_explicit_deadline
#print axioms closed_open_short_has_no_self_renewing_population
#print axioms dangling_closure_falls_short
#print axioms dangling_kind_outside_every_closure
#print axioms dangling_support_renews_forever
#print axioms lapsing_closure_renews_forever
#print axioms lapsing_balance
#print axioms lapsing_correction_gap
#print axioms lapsing_correction_cannot_be_kept

end Generative.Conditional.Renewal
