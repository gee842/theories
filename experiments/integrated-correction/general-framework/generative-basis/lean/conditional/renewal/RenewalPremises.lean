import RenewalConfigurations

/-!
# The remaining premises are needed

Ren's rule of 6 October 2026: no premise may stay merely assumed. Each input a
result relies on is derived from the process or proved necessary for the
stated claim. After the span and rate bounds were derived and the span and
initial-token conditions removed, two premises remain. Both are needed.

- **Finitely many kinds.** With kinds `ℕ`, where kind `k` supports kind `k + 1`
  only, a history renews forever, but no population is closed under support
  (`infinitely_many_kinds_break_the_equivalence`). Late activity then descends
  from no realized closure. Nothing else is assumed about the kinds: equality
  between them need not be decidable.
- **Positive formation demand, for a deadline read from the initial
  configuration.** In `freeFormation`, one kind costs nothing to form. The law
  has no self-renewing population, so every history stops being live. But no
  time computed from the starting configuration bounds them all
  (`zero_demand_defeats_initial_deadline`). Forming many free tokens on the first
  tick stores provision that keeps a short cycle going as long as one likes.
  The deadline that does not mention the initial configuration alone
  (`no_self_renewing_population_deadline`) needs no condition on demands.

The law itself, kinds, edges, spans, demands and rates, is the remaining
supplied input. Deriving it from the generative core is roadmap Phase 4.
-/

namespace Generative.Conditional.Renewal

open Generative

universe u

variable {Kind : Type u}

/-! ## Histories that stay live for a while -/

/-- From any configuration, forming nothing is a history. -/
def History.idle (law : ChannelLaw Kind) (c : Config Kind) : History law where
  states n := ⟨c.reserve, agedN n c.tokens⟩
  ticks _ := []
  steps _ := ⟨(append_nil_eq _).symm, Nat.add_le_add_left (Nat.zero_le _) _,
    fun _ member => by cases member⟩

/-- Some history from the configuration is live at every time up to `T`. -/
def LiveFor (law : ChannelLaw Kind) (c : Config Kind) (T : Nat) : Prop :=
  ∃ H : History law, H.states 0 = c ∧ ∀ t, t ≤ T → Live (H.states t)

theorem liveFor_zero {law : ChannelLaw Kind} {c : Config Kind} (live : Live c) :
    LiveFor law c 0 :=
  ⟨History.idle law c, rfl, fun t within => by
    rw [Nat.eq_zero_of_le_zero within]
    exact live⟩

theorem liveFor_of_step {law : ChannelLaw Kind} {c c' : Config Kind} {births : List Kind}
    {T : Nat} (live : Live c) (step : (channelProcess law).step c births c')
    (later : LiveFor law c' T) : LiveFor law c (T + 1) := by
  obtain ⟨H, start, alive⟩ := later
  subst start
  refine ⟨History.cons c births H step, rfl, fun t within => ?_⟩
  cases t with
  | zero => exact live
  | succ t => exact alive t (Nat.le_of_succ_le_succ within)

theorem formed_replicate (law : ChannelLaw Kind) (k : Kind) :
    ∀ m, formed law (List.replicate m k) = List.replicate m ⟨k, law.span k⟩
  | 0 => rfl
  | m + 1 => by
    show ⟨k, law.span k⟩ :: formed law (List.replicate m k) = _
    rw [formed_replicate law k m]
    rfl

theorem aged_replicate_two (k : Kind) :
    ∀ m, aged (List.replicate m (⟨k, 2⟩ : Token Kind)) = List.replicate m ⟨k, 1⟩
  | 0 => rfl
  | m + 1 => by
    show aged (⟨k, 2⟩ :: List.replicate m ⟨k, 2⟩) = ⟨k, 1⟩ :: List.replicate m ⟨k, 1⟩
    rw [aged, if_neg (Nat.not_succ_le_self 1), aged_replicate_two k m]
    rfl

theorem aged_replicate_one (k : Kind) :
    ∀ m, aged (List.replicate m (⟨k, 1⟩ : Token Kind)) = []
  | 0 => rfl
  | m + 1 => by
    show aged (⟨k, 1⟩ :: List.replicate m ⟨k, 1⟩) = []
    rw [aged, if_pos (Nat.le_refl 1), aged_replicate_one k m]

/-! ## Finitely many kinds are needed -/

/-- Kinds are natural numbers, and kind `k` supports only kind `k + 1`. Every
kind has span 2, rate 1 and demand 1. -/
def chainLaw : ChannelLaw Nat where
  edge j k := k = j + 1
  span _ := 2
  demand _ := 1
  rate _ := 1

/-- No kind lies in a support-closed list: kind `0` has no supporter, and kind
`k + 1` only kind `k`. -/
theorem chain_not_supported {B : List Nat} (closed : SupportClosed chainLaw B) :
    ∀ k, k ∉ B
  | 0, member => by
    obtain ⟨j, _, edge, _⟩ := closed 0 member
    have zero : 0 = j + 1 := edge
    exact succ_ne_zero_of j zero.symm
  | k + 1, member => by
    obtain ⟨j, jIn, edge, _⟩ := closed (k + 1) member
    have same : k + 1 = j + 1 := edge
    have kj : k = j := add_right_cancel_eq same
    rw [← kj] at jIn
    exact chain_not_supported closed k jIn

theorem chain_has_no_self_renewing_population : ¬ ∃ B, SelfRenewing chainLaw B := by
  intro found
  obtain ⟨B, nonempty, closed, _⟩ := found
  cases B with
  | nil => exact nonempty rfl
  | cons k rest => exact chain_not_supported closed k List.mem_cons_self

/-- At time `n`, a token of kind `n` on its last tick and a fresh token of kind
`n + 1`; kind `n + 2` is formed. -/
def chainHistory : History chainLaw where
  states n := ⟨0, [⟨n, 1⟩, ⟨n + 1, 2⟩]⟩
  ticks n := [n + 2]
  steps n := by
    refine ⟨rfl, ?_, ?_⟩
    · show 0 + (1 + 0) ≤ 0 + (1 + (1 + 0))
      decide
    · intro k member
      rw [mem_singleton_eq member]
      exact ⟨⟨n + 1, 1⟩, List.mem_singleton_self _, rfl⟩

theorem chain_renews_forever : RenewsForever chainLaw :=
  ⟨chainHistory, fun _ => alive_token_live List.mem_cons_self (Nat.le_refl 1)⟩

/-- **Finitely many kinds are needed.** With infinitely many kinds, a law can
renew forever although no population of kinds is closed under support. -/
theorem infinitely_many_kinds_break_the_equivalence :
    RenewsForever chainLaw ∧ ¬ ∃ B, SelfRenewing chainLaw B :=
  ⟨chain_renews_forever, chain_has_no_self_renewing_population⟩

/-! ## Positive formation demand is needed for a deadline from the start -/

/-- A seed kind that nothing forms, a short self-supporting kind, and a kind
that costs nothing to form. -/
inductive SeedKind where
  | seed
  | cycle
  | free

/-- The seed supports the cycle kind and the free kind; the cycle kind supports
itself. Every kind has span 2 and rate 1. Forming the cycle kind demands 3,
more than its token opens; forming the free kind demands nothing. -/
def freeFormation : ChannelLaw SeedKind where
  edge j k := match j, k with
    | .seed, .seed => False
    | .seed, .cycle => True
    | .seed, .free => True
    | .cycle, .seed => False
    | .cycle, .cycle => True
    | .cycle, .free => False
    | .free, .seed => False
    | .free, .cycle => False
    | .free, .free => False
  span _ := 2
  demand k := match k with
    | .seed => 1
    | .cycle => 3
    | .free => 0
  rate _ := 1

theorem free_formation_closed_members {B : List SeedKind}
    (closed : SupportClosed freeFormation B) : ∀ k, k ∈ B → k = .cycle := by
  have noSeed : SeedKind.seed ∉ B := by
    intro member
    obtain ⟨j, _, edge, _⟩ := closed .seed member
    cases j <;> exact edge
  intro k member
  cases k with
  | seed => exact False.elim (noSeed member)
  | cycle => rfl
  | free =>
    obtain ⟨j, jIn, edge, _⟩ := closed .free member
    cases j with
    | seed => exact False.elim (noSeed jIn)
    | cycle => exact False.elim edge
    | free => exact False.elim edge

theorem free_formation_short {B : List SeedKind} (allCycle : ∀ k, k ∈ B → k = .cycle) :
    spanOpening freeFormation B + B.length ≤ formation freeFormation B := by
  induction B with
  | nil => exact Nat.le_refl 0
  | cons k rest ih =>
    have restShort := ih (fun j member => allCycle j (List.mem_cons_of_mem _ member))
    rw [allCycle k List.mem_cons_self]
    show 2 + spanOpening freeFormation rest + rest.length + 1 ≤
      3 + formation freeFormation rest
    rw [Nat.add_assoc 2, Nat.add_right_comm 2]
    exact Nat.add_le_add_left restShort 3

theorem free_formation_has_no_self_renewing_population :
    ¬ ∃ B, SelfRenewing freeFormation B := by
  intro found
  obtain ⟨B, nonempty, closed, balanced⟩ := found
  have short := free_formation_short (free_formation_closed_members closed)
  cases B with
  | nil => exact nonempty rfl
  | cons k rest =>
    have overdrawn : spanOpening freeFormation (k :: rest) + (rest.length + 1) ≤
        spanOpening freeFormation (k :: rest) := Nat.le_trans short balanced
    exact Nat.not_succ_le_self _
      (Nat.le_trans (Nat.add_le_add_left (Nat.le_add_left 1 rest.length) _) overdrawn)

theorem free_formation_complete : ∀ k : SeedKind, k ∈ [.seed, .cycle, .free] := by
  intro k
  cases k
  · exact List.mem_cons_self
  · exact List.mem_cons_of_mem _ List.mem_cons_self
  · exact List.mem_cons_of_mem _ (List.mem_cons_of_mem _ List.mem_cons_self)

/-- Every history of `freeFormation` stops being live. -/
theorem free_formation_histories_end (H : History freeFormation) :
    ∃ t, ¬ Live (H.states t) := by
  obtain ⟨t, _, dead⟩ := no_self_renewing_population_deadline freeFormation
    [.seed, .cycle, .free] free_formation_complete
    free_formation_has_no_self_renewing_population H
  exact ⟨t, dead⟩

theorem formation_replicate_free :
    ∀ m, formation freeFormation (List.replicate m SeedKind.free) = 0
  | 0 => rfl
  | m + 1 => by
    show 0 + formation freeFormation (List.replicate m SeedKind.free) = 0
    rw [formation_replicate_free m]

theorem opened_replicate_free (s : Nat) :
    ∀ m, opened freeFormation.rate (List.replicate m ⟨SeedKind.free, s + 1⟩) = m
  | 0 => rfl
  | m + 1 => by
    show (if s + 1 = 0 then 0 else 1) +
      opened freeFormation.rate (List.replicate m ⟨SeedKind.free, s + 1⟩) = m + 1
    rw [if_neg (succ_ne_zero_of s), opened_replicate_free s m]
    exact Nat.add_comm 1 m

/-- The short cycle with reserve `R` stays live for `R` ticks. -/
theorem cycle_lives (R : Nat) :
    LiveFor freeFormation ⟨R, [⟨.cycle, 1⟩, ⟨.cycle, 2⟩]⟩ R := by
  induction R with
  | zero => exact liveFor_zero (alive_token_live List.mem_cons_self (Nat.le_refl 1))
  | succ R ih =>
    refine liveFor_of_step (births := [.cycle])
      (alive_token_live List.mem_cons_self (Nat.le_refl 1)) ⟨rfl, ?_, ?_⟩ ih
    · show R + 3 ≤ R + 1 + 2
      exact Nat.le_refl (R + 3)
    · intro k member
      rw [mem_singleton_eq member]
      exact ⟨⟨.cycle, 1⟩, List.mem_singleton_self _, True.intro⟩

/-- The starting configuration: reserve 4 and one fresh seed token. -/
def freeStart : Config SeedKind := ⟨4, [⟨.seed, 2⟩]⟩

/-- Forming the cycle kind with `m` free tokens on the first tick keeps a
history from `freeStart` live for `m + 3` ticks. -/
theorem free_formation_lives_long (m : Nat) : LiveFor freeFormation freeStart (m + 3) := by
  have third := cycle_lives m
  have second : LiveFor freeFormation
      ⟨m + 1, ⟨.cycle, 1⟩ :: (List.replicate m ⟨.free, 1⟩ ++ [⟨.cycle, 2⟩])⟩ (m + 1) := by
    have agedSecond : aged (⟨.cycle, 1⟩ :: (List.replicate m ⟨.free, 1⟩ ++ [⟨.cycle, 2⟩])) =
        [⟨SeedKind.cycle, 1⟩] := by
      rw [aged, if_pos (Nat.le_refl 1), aged_append, aged_replicate_one]
      rfl
    have openedSecond : opened freeFormation.rate
        (⟨.cycle, 1⟩ :: (List.replicate m ⟨.free, 1⟩ ++ [⟨.cycle, 2⟩])) = 1 + (m + 1) := by
      show 1 + opened freeFormation.rate (List.replicate m ⟨.free, 0 + 1⟩ ++ [⟨.cycle, 2⟩]) =
        1 + (m + 1)
      rw [opened_append, opened_replicate_free 0 m]
      rfl
    refine liveFor_of_step (births := [.cycle])
      (alive_token_live List.mem_cons_self (Nat.le_refl 1)) ⟨?_, ?_, ?_⟩ third
    · rw [agedSecond]
      rfl
    · show m + (3 + 0) ≤ m + 1 + opened freeFormation.rate
        (⟨.cycle, 1⟩ :: (List.replicate m ⟨.free, 1⟩ ++ [⟨.cycle, 2⟩]))
      rw [openedSecond]
      exact Nat.add_le_add_left (Nat.succ_le_succ (Nat.le_add_right 1 m)) (m + 1)
    · intro k member
      rw [mem_singleton_eq member, agedSecond]
      exact ⟨⟨.cycle, 1⟩, List.mem_singleton_self _, True.intro⟩
  have first : LiveFor freeFormation
      ⟨2, ⟨.seed, 1⟩ :: ⟨.cycle, 2⟩ :: List.replicate m ⟨.free, 2⟩⟩ (m + 2) := by
    have agedFirst : aged (⟨.seed, 1⟩ :: ⟨.cycle, 2⟩ :: List.replicate m ⟨.free, 2⟩) =
        ⟨SeedKind.cycle, 1⟩ :: List.replicate m ⟨.free, 1⟩ := by
      rw [aged, if_pos (Nat.le_refl 1), aged, if_neg (Nat.not_succ_le_self 1),
        aged_replicate_two]
      rfl
    have openedFirst : opened freeFormation.rate
        (⟨.seed, 1⟩ :: ⟨.cycle, 2⟩ :: List.replicate m ⟨.free, 2⟩) = 1 + (1 + m) := by
      show 1 + (1 + opened freeFormation.rate (List.replicate m ⟨.free, 1 + 1⟩)) = 1 + (1 + m)
      rw [opened_replicate_free 1 m]
    refine liveFor_of_step (births := [.cycle])
      (alive_token_live List.mem_cons_self (Nat.le_refl 1)) ⟨?_, ?_, ?_⟩ second
    · rw [agedFirst]
      rfl
    · show m + 1 + (3 + 0) ≤ 2 + opened freeFormation.rate
        (⟨.seed, 1⟩ :: ⟨.cycle, 2⟩ :: List.replicate m ⟨.free, 2⟩)
      rw [openedFirst, Nat.add_comm 1 m, Nat.add_comm 1 (m + 1), Nat.add_comm 2]
      exact Nat.le_refl (m + 4)
    · intro k member
      rw [mem_singleton_eq member, agedFirst]
      exact ⟨⟨.cycle, 1⟩, List.mem_cons_self, True.intro⟩
  refine liveFor_of_step (births := .cycle :: List.replicate m .free)
    (alive_token_live (c := freeStart) List.mem_cons_self (Nat.le_succ 1)) ⟨?_, ?_, ?_⟩ first
  · show ⟨.seed, 1⟩ :: ⟨.cycle, 2⟩ :: List.replicate m ⟨.free, 2⟩ =
      [⟨.seed, 1⟩] ++ (⟨.cycle, 2⟩ :: formed freeFormation (List.replicate m .free))
    rw [formed_replicate]
    rfl
  · show 2 + (3 + formation freeFormation (List.replicate m .free)) ≤ 4 + (1 + 0)
    rw [formation_replicate_free]
    exact Nat.le_refl 5
  · intro k member
    refine ⟨⟨.seed, 1⟩, List.mem_singleton_self _, ?_⟩
    cases mem_cons_split member with
    | inl same => rw [same]; exact True.intro
    | inr inFree => rw [eq_of_mem_replicate_eq inFree]; exact True.intro

/-- **Positive formation demand is needed for a deadline read from the initial
configuration.** `freeFormation` has no self-renewing population, so every
history stops being live (`free_formation_histories_end`). Yet no time bounds
every history from `freeStart`. -/
theorem zero_demand_defeats_initial_deadline :
    (¬ ∃ B, SelfRenewing freeFormation B) ∧
    ¬ ∃ T, ∀ H : History freeFormation, H.states 0 = freeStart →
      ∃ t, t ≤ T ∧ ¬ Live (H.states t) := by
  refine ⟨free_formation_has_no_self_renewing_population, ?_⟩
  intro found
  obtain ⟨T, bound⟩ := found
  obtain ⟨H, start, alive⟩ := free_formation_lives_long T
  obtain ⟨t, within, dead⟩ := bound H start
  exact dead (alive t (Nat.le_trans within (Nat.le_add_right T 3)))

#print axioms liveFor_zero
#print axioms liveFor_of_step
#print axioms formed_replicate
#print axioms aged_replicate_two
#print axioms aged_replicate_one
#print axioms chain_not_supported
#print axioms chain_has_no_self_renewing_population
#print axioms chain_renews_forever
#print axioms infinitely_many_kinds_break_the_equivalence
#print axioms free_formation_closed_members
#print axioms free_formation_short
#print axioms free_formation_has_no_self_renewing_population
#print axioms free_formation_complete
#print axioms free_formation_histories_end
#print axioms formation_replicate_free
#print axioms opened_replicate_free
#print axioms cycle_lives
#print axioms free_formation_lives_long
#print axioms zero_demand_defeats_initial_deadline

end Generative.Conditional.Renewal
