import RenewalSufficiency
import RenewalLink

/-!
# The renewal–closure theorem

Phase 2 of the renewal–closure roadmap. Under a supplied constraint–flow law
with finitely many kinds and spans between one and `D`, the following are
equivalent:
- some execution of `channelProcess` stays live forever, with no organization
  imported after the start;
- some nonempty population of kinds is closed under support by constraints that
  outlast a tick, and its tokens open over their spans at least what forming
  them demands.

The second condition is checked on the law alone. It covers the two earlier
cases. A closure whose kinds each bring in enough is one instance. A closure
that supports a kind bringing in more than its demand is another, with enough
repeats of that kind.

When no such population exists, every execution stops being live by an
explicit time. That time is fixed by the number of kinds, the longest span and
the opening potential (reserve plus what live tokens can still open) one window
into the history. With positive formation demands and bounded rates, it is
fixed by the initial reserve and initial tokens alone.

Necessity runs as follows.
- If a kind that brings in more than its demand is formed late, its formation
  descends from a realized cycle. The cycle plus the walk to that kind is a
  self-renewing population.
- Otherwise, the opening potential cannot rise. Each formation of a kind that
  falls short lowers it by at least one. So some window of length
  `(n + 1) · D + 1` contains no such formation, and the closure that the
  configuration at its end descends from consists of kinds that bring in
  enough.

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

/-- Some execution stays live forever. -/
def RenewsForever (law : ChannelLaw Kind) : Prop :=
  ∃ X : Execution law, ∀ n, Live (X.states n)

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

/-- **Sufficiency.** A self-renewing population renews forever from its steady
configuration, with no reserve. -/
theorem self_renewing_renews_forever (law : ChannelLaw Kind) (D : Nat)
    (spanBound : ∀ k, law.span k ≤ D) (positive : ∀ k, 0 < law.span k) {B : List Kind}
    (renewing : SelfRenewing law B) : RenewsForever law := by
  obtain ⟨nonempty, supported, balanced⟩ := renewing
  refine ⟨steadyExecution law B D nonempty (fun k _ => positive k) (fun k _ => spanBound k)
    supported balanced, fun _ => ?_⟩
  exact (steady_renews law B D 0 nonempty (fun k _ => positive k) (fun k _ => spanBound k)
    supported balanced).1

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
theorem cycle_with_tail [DecidableEq Kind] {edge : Kind → Kind → Prop} {j q : Kind}
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
    if same : v = j then
      obtain ⟨u, uIn, edgeUV⟩ := closed.2.1 v (same ▸ jIn)
      exact ⟨u, List.mem_append_left _ uIn, edgeUV⟩
    else
      obtain ⟨u, uIn, edgeUV⟩ := tail.predecessor v (List.mem_cons_of_mem _ there) same
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

/-- **The dichotomy.** For any execution, either the law has a self-renewing
population, or the execution stops being live by `(P + 2) · W`. Here `W` is
`(n + 1) · D + 1` and `P` is the opening potential at time `W`. -/
theorem renewal_dichotomy [DecidableEq Kind] (law : ChannelLaw Kind) (U : List Kind)
    (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (X : Execution law) :
    (∃ B, SelfRenewing law B) ∨
      ∃ t, t ≤ (potential X ((U.length + 1) * D + 1) + 2) * ((U.length + 1) * D + 1) ∧
        ¬ Live (X.states t) := by
  generalize hW : (U.length + 1) * D + 1 = W
  generalize hK : potential X W = K
  have reachBound : ∀ j, (executionSupport X).reach j ≤ D := by
    intro j
    have := spanBound j
    show law.span j - 1 ≤ D
    omega
  cases range_search
      (fun m => ∃ k, k ∈ X.ticks m ∧ law.demand k + 1 ≤ law.rate k * law.span k)
      (tick_search law X _) W ((K + 1) * W) with
  | inl found =>
    -- A late formation of an excess kind descends from a realized cycle.
    obtain ⟨m, low, _, q, inTick, excess⟩ := found
    have occ : (executionSupport X).occurs q (m + 1) := Or.inr ⟨m, rfl, inTick⟩
    have late : U.length * D < m + 1 := by
      rw [Nat.succ_mul] at hW
      omega
    obtain ⟨j, cycle, rest, nonempty, loop, tail, closed, _⟩ :=
      late_occurrence_descends_from_realized_closure (executionSupport X) U complete D
        reachBound occ late
    obtain ⟨closedAll, qIn⟩ := cycle_with_tail nonempty loop tail closed
    have closedC : SupportClosed law (cycle ++ rest) := by
      intro v member
      obtain ⟨u, uIn, edgeUV, spanU⟩ := closedAll v member
      exact ⟨u, uIn, edgeUV, spanU⟩
    have nonemptyC : cycle ++ rest ≠ [] := append_nonempty nonempty
    exact Or.inl ⟨_, excess_population law nonemptyC closedC qIn excess⟩
  | inr noExcess =>
    have each : ∀ m, W ≤ m → m < W + (K + 1) * W → ∀ k, k ∈ X.ticks m →
        law.rate k * law.span k ≤ law.demand k := by
      intro m low high k member
      have notExcess := noExcess m low high
      exact Nat.le_of_not_lt (fun bigger => notExcess ⟨k, member, bigger⟩)
    -- Some window of length `W` has no formation of a kind that falls short.
    have windows : ∀ i, i ≤ K + 1 →
        (∃ w, w < i ∧ ∀ m, W + w * W ≤ m → m < W + w * W + W → ∀ k, k ∈ X.ticks m →
          law.demand k ≤ law.rate k * law.span k) ∨
        potential X (W + i * W) + i ≤ K := by
      intro i
      induction i with
      | zero =>
        intro _
        refine Or.inr ?_
        rw [Nat.zero_mul, Nat.add_zero, Nat.add_zero, hK]
        exact Nat.le_refl K
      | succ i ih =>
        intro within
        cases ih (Nat.le_of_succ_le within) with
        | inl earlier =>
          obtain ⟨w, below, good⟩ := earlier
          exact Or.inl ⟨w, Nat.lt_succ_of_lt below, good⟩
        | inr bound =>
          have inRange : W + i * W + W ≤ W + (K + 1) * W := by
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
    have found : ∃ w, w < K + 1 ∧ ∀ m, W + w * W ≤ m → m < W + w * W + W →
        ∀ k, k ∈ X.ticks m → law.demand k ≤ law.rate k * law.span k := by
      cases windows (K + 1) (Nat.le_refl _) with
      | inl good => exact good
      | inr impossible => exact False.elim (by omega)
    obtain ⟨w, below, good⟩ := found
    -- At the end of that window, either nothing is live, or the configuration
    -- descends from a closure of kinds that bring in enough.
    have endBound : W + w * W + W ≤ (K + 2) * W := by
      have := Nat.mul_le_mul_right W (Nat.le_of_lt_succ below)
      have shape : (K + 2) * W = W + K * W + W := by
        rw [Nat.succ_mul, Nat.succ_mul]
        omega
      omega
    cases Nat.decLe 1 (opened (fun _ => 1) (X.states (W + w * W + W)).tokens) with
    | isFalse dead =>
      exact Or.inr ⟨W + w * W + W, endBound, dead⟩
    | isTrue live =>
      have late : (U.length + 1) * D < W + w * W + W := by omega
      obtain ⟨_, cycle, nonempty, _, closed, window⟩ :=
        live_late_descends_from_realized_closure X U complete D spanBound live late
      have adequate : ∀ v, v ∈ cycle → law.demand v ≤ law.rate v * law.span v := by
        intro v member
        obtain ⟨s, occ, before, near⟩ := window v member
        cases occ with
        | inl initial =>
          obtain ⟨zero, _⟩ := initial
          exact False.elim (by omega)
        | inr formedAt =>
          obtain ⟨m, timeEq, inTick⟩ := formedAt
          exact good m (by omega) (by omega) v inTick
      refine Or.inl ⟨cycle, nonempty, ?_, balanced_of_each law cycle adequate⟩
      intro v member
      obtain ⟨u, uIn, edgeUV, spanU⟩ := closed.2.1 v member
      exact ⟨u, uIn, edgeUV, spanU⟩

/-- **Necessity.** An execution that stays live forever shows that the law has
a self-renewing population. -/
theorem renews_forever_has_self_renewing_population [DecidableEq Kind]
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) (endless : RenewsForever law) :
    ∃ B, SelfRenewing law B := by
  obtain ⟨X, alive⟩ := endless
  cases renewal_dichotomy law U complete D spanBound X with
  | inl population => exact population
  | inr dies =>
    obtain ⟨t, _, dead⟩ := dies
    exact False.elim (dead (alive t))

/-- **The renewal–closure theorem.** With finitely many kinds and spans between
one and `D`, a law admits an execution that renews forever exactly when it has
a nonempty population of kinds, closed under support by constraints that
outlast a tick, whose tokens open over their spans at least what forming them
demands. -/
theorem renewal_closure_theorem [DecidableEq Kind] (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (positive : ∀ k, 0 < law.span k) :
    RenewsForever law ↔ ∃ B, SelfRenewing law B :=
  ⟨renews_forever_has_self_renewing_population law U complete D spanBound,
    fun ⟨_, renewing⟩ => self_renewing_renews_forever law D spanBound positive renewing⟩

/-- **The deadline.** Without a self-renewing population, every execution stops
being live by `(P + 2) · W`. -/
theorem no_self_renewing_population_deadline [DecidableEq Kind] (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (none : ¬ ∃ B, SelfRenewing law B) (X : Execution law) :
    ∃ t, t ≤ (potential X ((U.length + 1) * D + 1) + 2) * ((U.length + 1) * D + 1) ∧
      ¬ Live (X.states t) := by
  cases renewal_dichotomy law U complete D spanBound X with
  | inl population => exact False.elim (none population)
  | inr dies => exact dies

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
theorem potential_growth {law : ChannelLaw Kind} (X : Execution law) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D)
    (demandPositive : ∀ k, 1 ≤ law.demand k) (m : Nat) :
    potential X (m + 1) ≤ (1 + A * D) * potential X m := by
  have step := opening_step law (X.steps m)
  rw [weighted_formed_eq] at step
  have balance := (X.steps m).2.1
  have openBound := opened_le_weighted law.rate (X.states m).tokens
  have count := length_le_formation law demandPositive (X.ticks m)
  have opening := spanOpening_le_length law A D rateBound spanBound (X.ticks m)
  have few : (X.ticks m).length ≤ potential X m := by
    simp only [potential, openingPotential]
    omega
  have scaled := Nat.mul_le_mul_left (A * D) few
  rw [Nat.add_mul, Nat.one_mul]
  simp only [potential] at step scaled ⊢
  omega

theorem potential_bound {law : ChannelLaw Kind} (X : Execution law) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D)
    (demandPositive : ∀ k, 1 ≤ law.demand k) :
    ∀ m, potential X m ≤ (1 + A * D) ^ m * potential X 0
  | 0 => by rw [Nat.pow_zero, Nat.one_mul]; exact Nat.le_refl _
  | m + 1 => by
    have grow := potential_growth X A D rateBound spanBound demandPositive m
    have ih := Nat.mul_le_mul_left (1 + A * D) (potential_bound X A D rateBound spanBound
      demandPositive m)
    rw [Nat.pow_succ, Nat.mul_comm ((1 + A * D) ^ m) (1 + A * D), Nat.mul_assoc]
    exact Nat.le_trans grow ih

/-- **The explicit deadline.** With rates at most `A` and positive formation
demands, and without a self-renewing population, every execution stops being
live by `((1 + A · D) ^ W · P₀ + 2) · W`. Here `W = (n + 1) · D + 1` and `P₀`
is the initial reserve plus what the initial tokens can open. -/
theorem no_self_renewing_population_explicit_deadline [DecidableEq Kind]
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D)
    (demandPositive : ∀ k, 1 ≤ law.demand k)
    (none : ¬ ∃ B, SelfRenewing law B) (X : Execution law) :
    ∃ t, t ≤ ((1 + A * D) ^ ((U.length + 1) * D + 1) *
        openingPotential law (X.states 0) + 2) * ((U.length + 1) * D + 1) ∧
      ¬ Live (X.states t) := by
  obtain ⟨t, within, dead⟩ := no_self_renewing_population_deadline law U complete D
    spanBound none X
  have grow := potential_bound X A D rateBound spanBound demandPositive
    ((U.length + 1) * D + 1)
  refine ⟨t, Nat.le_trans within ?_, dead⟩
  exact Nat.mul_le_mul_right _ (Nat.add_le_add_right grow 2)

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
  refine self_renewing_renews_forever danglingSupport 3 ?_ ?_
    (B := [false, true, true, true, true, true]) ⟨List.cons_ne_nil _ _, ?_, ?_⟩
  · intro k
    cases k <;> decide
  · intro k
    cases k <;> decide
  · intro k _
    exact ⟨false, List.mem_cons_self, rfl, Nat.le_refl 2⟩
  · show 10 ≤ 32
    decide

#print axioms block_within
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
#print axioms renewal_dichotomy
#print axioms renews_forever_has_self_renewing_population
#print axioms renewal_closure_theorem
#print axioms no_self_renewing_population_deadline
#print axioms opened_le_weighted
#print axioms length_le_formation
#print axioms spanOpening_le_length
#print axioms potential_growth
#print axioms potential_bound
#print axioms no_self_renewing_population_explicit_deadline
#print axioms closed_open_short_has_no_self_renewing_population
#print axioms dangling_closure_falls_short
#print axioms dangling_kind_outside_every_closure
#print axioms dangling_support_renews_forever

end Generative.Conditional.Renewal
