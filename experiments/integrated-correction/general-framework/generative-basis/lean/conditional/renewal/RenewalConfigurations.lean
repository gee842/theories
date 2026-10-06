import RenewalCharacterization

/-!
# Renewability of whole configurations

Phase 2b of the renewal–closure roadmap. The renewal–closure theorem is about
laws: whether some history renews forever. Here the object is a whole
configuration, meaning the reserve and every token with its remaining span. A
configuration is renewable when some execution that stays live forever starts
from it.

- **Viability.** A configuration within span is renewable exactly when it is
  live and some step leads to a renewable configuration.
- **Renewability is not gained from within.** Along any execution, if the start
  is not renewable, no later configuration is. A history can keep the
  possibility it starts with, or lose it, but it cannot create it. Only
  something added from outside, held provision or formed tokens, can
  (`renewable_of_more`).
- **What a history can generate is the standing renewal itself.** A
  configuration that seeds every kind of a self-renewing population, with
  enough reserve, reaches the steady configuration within `D + 1` ticks
  (`seeded_renewable`).
- **No goal projection decides it.** Renewability is not a function of the
  reserve and the kinds present, nor of the tokens alone.
- **Damage is a local choice.** From one renewable configuration, one step keeps
  renewability and another loses it for good, although the second holds more
  reserve.

Kinds, edges, spans, demands and rates are supplied. Nothing here ranks
histories or says which should be kept.
-/

namespace Generative.Conditional.Renewal

open Generative

universe u

variable {Kind : Type u}

/-- Every token holds no more than its kind's span. -/
def WithinSpan (law : ChannelLaw Kind) (c : Config Kind) : Prop :=
  ∀ tok, tok ∈ c.tokens → tok.remaining ≤ law.span tok.kind

/-- Some execution that stays live forever starts from the configuration. -/
def Renewable (law : ChannelLaw Kind) (c : Config Kind) : Prop :=
  ∃ X : Execution law, X.states 0 = c ∧ ∀ n, Live (X.states n)

theorem step_within {law : ChannelLaw Kind} {c c' : Config Kind} {births : List Kind}
    (within : WithinSpan law c) (step : (channelProcess law).step c births c') :
    WithinSpan law c' := by
  intro tok member
  rw [step.1] at member
  cases List.mem_append.mp member with
  | inl agedIn =>
    obtain ⟨old, oldIn, kindEq, ageEq, _⟩ := mem_aged agedIn
    have bound := within old oldIn
    rw [kindEq] at bound
    omega
  | inr formedIn =>
    obtain ⟨_, spanEq⟩ := mem_formed law formedIn
    rw [spanEq]
    exact Nat.le_refl _

theorem execution_within {law : ChannelLaw Kind} (X : Execution law) :
    ∀ n, WithinSpan law (X.states n)
  | 0 => X.initialWithinSpan
  | n + 1 => step_within (execution_within X n) (X.steps n)

theorem opened_one_pos {tok : Token Kind} (alive : 1 ≤ tok.remaining) :
    ∀ {l : List (Token Kind)}, tok ∈ l → 1 ≤ opened (fun _ => 1) l
  | [], member => by cases member
  | head :: rest, member => by
    rw [opened]
    cases List.mem_cons.mp member with
    | inl same =>
      subst same
      rw [if_neg (by omega)]
      exact Nat.le_add_right 1 _
    | inr tail =>
      exact Nat.le_trans (opened_one_pos alive tail) (Nat.le_add_left _ _)

theorem alive_token_live {c : Config Kind} {tok : Token Kind} (member : tok ∈ c.tokens)
    (alive : 1 ≤ tok.remaining) : Live c :=
  opened_one_pos alive member

/-- A configuration with nothing alive forms nothing and stays without life. -/
theorem dead_stays_dead {law : ChannelLaw Kind} {c c' : Config Kind} {births : List Kind}
    (dead : ¬ Live c) (step : (channelProcess law).step c births c') : ¬ Live c' := by
  intro live
  obtain ⟨tok, member, _⟩ := live_has_alive_token live
  apply dead
  rw [step.1] at member
  cases List.mem_append.mp member with
  | inl agedIn =>
    obtain ⟨old, oldIn, _, _, kept⟩ := mem_aged agedIn
    exact alive_token_live oldIn (Nat.le_of_succ_le kept)
  | inr formedIn =>
    obtain ⟨kIn, _⟩ := mem_formed law formedIn
    obtain ⟨supporter, supporterIn, _⟩ := step.2.2 tok.kind kIn
    obtain ⟨old, oldIn, _, _, kept⟩ := mem_aged supporterIn
    exact alive_token_live oldIn (Nat.le_of_succ_le kept)

/-! ## Viability -/

/-- The execution after its first tick. -/
def Execution.next {law : ChannelLaw Kind} (X : Execution law) : Execution law where
  states n := X.states (n + 1)
  ticks n := X.ticks (n + 1)
  steps n := X.steps (n + 1)
  initialWithinSpan := execution_within X 1

/-- An execution with one tick put in front. -/
def Execution.cons {law : ChannelLaw Kind} (c : Config Kind) (births : List Kind)
    (X : Execution law) (within : WithinSpan law c)
    (step : (channelProcess law).step c births (X.states 0)) : Execution law where
  states n := match n with
    | 0 => c
    | n + 1 => X.states n
  ticks n := match n with
    | 0 => births
    | n + 1 => X.ticks n
  steps n := match n with
    | 0 => step
    | n + 1 => X.steps n
  initialWithinSpan := within

theorem renewable_live_step {law : ChannelLaw Kind} {c : Config Kind}
    (renewable : Renewable law c) :
    Live c ∧ ∃ births c', (channelProcess law).step c births c' ∧ Renewable law c' := by
  obtain ⟨X, start, alive⟩ := renewable
  subst start
  exact ⟨alive 0, X.ticks 0, X.states 1, X.steps 0, X.next, rfl, fun n => alive (n + 1)⟩

theorem renewable_of_step {law : ChannelLaw Kind} {c c' : Config Kind} {births : List Kind}
    (within : WithinSpan law c) (live : Live c) (step : (channelProcess law).step c births c')
    (renewable : Renewable law c') : Renewable law c := by
  obtain ⟨X, start, alive⟩ := renewable
  subst start
  refine ⟨Execution.cons c births X within step, rfl, fun n => ?_⟩
  cases n with
  | zero => exact live
  | succ n => exact alive n

/-- **Viability.** A configuration within span is renewable exactly when it is
live and some step leads to a renewable configuration. -/
theorem renewable_iff_step {law : ChannelLaw Kind} {c : Config Kind}
    (within : WithinSpan law c) :
    Renewable law c ↔
      Live c ∧ ∃ births c', (channelProcess law).step c births c' ∧ Renewable law c' :=
  ⟨renewable_live_step, fun ⟨live, _, _, step, renewable⟩ =>
    renewable_of_step within live step renewable⟩

/-- **Renewability is not gained from within.** Along any execution, if the
start is not renewable, no later configuration is. -/
theorem renewability_not_generated {law : ChannelLaw Kind} (X : Execution law)
    (start : ¬ Renewable law (X.states 0)) : ∀ n, ¬ Renewable law (X.states n) := by
  intro n
  induction n with
  | zero => exact start
  | succ n ih =>
    intro renewable
    apply ih
    cases Nat.decLe 1 (opened (fun _ => 1) (X.states n).tokens) with
    | isTrue live => exact renewable_of_step (execution_within X n) live (X.steps n) renewable
    | isFalse dead =>
      exact False.elim (dead_stays_dead dead (X.steps n) (renewable_live_step renewable).1)

/-! ## Import -/

/-- Tokens after `n` ticks of aging. -/
def agedN : Nat → List (Token Kind) → List (Token Kind)
  | 0, l => l
  | n + 1, l => aged (agedN n l)

theorem mem_agedN {l : List (Token Kind)} :
    ∀ n {tok : Token Kind}, tok ∈ agedN n l →
      ∃ old, old ∈ l ∧ old.kind = tok.kind ∧ tok.remaining + n = old.remaining ∧
        (n = 0 ∨ 1 ≤ tok.remaining)
  | 0, tok, member => ⟨tok, member, rfl, rfl, Or.inl rfl⟩
  | n + 1, tok, member => by
    obtain ⟨mid, midIn, midKind, midAge, kept⟩ := mem_aged member
    obtain ⟨old, oldIn, oldKind, oldAge, _⟩ := mem_agedN n midIn
    exact ⟨old, oldIn, oldKind.trans midKind, by omega, Or.inr (by omega)⟩

/-- Adding held provision or formed tokens from outside keeps renewability. -/
def Execution.enlarge {law : ChannelLaw Kind} (X : Execution law) (extraReserve : Nat)
    (extra : List (Token Kind))
    (within : ∀ tok, tok ∈ extra → tok.remaining ≤ law.span tok.kind) : Execution law where
  states n := ⟨(X.states n).reserve + extraReserve, agedN n extra ++ (X.states n).tokens⟩
  ticks := X.ticks
  steps n := by
    obtain ⟨shape, balance, supported⟩ := X.steps n
    refine ⟨?_, ?_, ?_⟩
    · show agedN (n + 1) extra ++ (X.states (n + 1)).tokens =
        aged (agedN n extra ++ (X.states n).tokens) ++ formed law (X.ticks n)
      rw [shape, aged_append, List.append_assoc]
      rfl
    · show (X.states (n + 1)).reserve + extraReserve + formation law (X.ticks n) ≤
        (X.states n).reserve + extraReserve +
          opened law.rate (agedN n extra ++ (X.states n).tokens)
      rw [opened_append]
      omega
    · intro k member
      obtain ⟨tok, agedIn, edge⟩ := supported k member
      refine ⟨tok, ?_, edge⟩
      show tok ∈ aged (agedN n extra ++ (X.states n).tokens)
      rw [aged_append]
      exact List.mem_append_right _ agedIn
  initialWithinSpan tok member := by
    cases List.mem_append.mp member with
    | inl here => exact within tok here
    | inr there => exact X.initialWithinSpan tok there

/-- **Import can generate renewability.** More reserve and more tokens, added
from outside, keep a configuration renewable. -/
theorem renewable_of_more {law : ChannelLaw Kind} {R R' : Nat} {T extra : List (Token Kind)}
    (renewable : Renewable law ⟨R, T⟩) (more : R ≤ R')
    (within : ∀ tok, tok ∈ extra → tok.remaining ≤ law.span tok.kind) :
    Renewable law ⟨R', extra ++ T⟩ := by
  obtain ⟨X, start, alive⟩ := renewable
  refine ⟨X.enlarge (R' - R) extra within, ?_, fun n => ?_⟩
  · show Config.mk ((X.states 0).reserve + (R' - R)) (extra ++ (X.states 0).tokens) =
      ⟨R', extra ++ T⟩
    rw [start]
    show Config.mk (R + (R' - R)) (extra ++ T) = ⟨R', extra ++ T⟩
    exact congrArg (fun r => Config.mk r (extra ++ T)) (by omega)
  · show 1 ≤ opened (fun _ => 1) (agedN n extra ++ (X.states n).tokens)
    rw [opened_append]
    exact Nat.le_trans (alive n) (Nat.le_add_left _ _)

/-! ## Reaching a standing renewal -/

/-- Each kind of `B` has a supporter in the configuration that survives the
next tick. -/
def Seeded (law : ChannelLaw Kind) (c : Config Kind) (B : List Kind) : Prop :=
  ∀ k, k ∈ B → ∃ tok, tok ∈ c.tokens ∧ 2 ≤ tok.remaining ∧ law.edge tok.kind k

theorem mem_aged_of_kept {tok : Token Kind} (kept : 2 ≤ tok.remaining) :
    ∀ {l : List (Token Kind)}, tok ∈ l → ⟨tok.kind, tok.remaining - 1⟩ ∈ aged l
  | [], member => by cases member
  | head :: rest, member => by
    cases List.mem_cons.mp member with
    | inl same =>
      subst same
      rw [aged, if_neg (by omega)]
      exact List.mem_cons_self
    | inr tail =>
      have inside := mem_aged_of_kept kept tail
      by_cases last : head.remaining ≤ 1
      · rw [aged, if_pos last]
        exact inside
      · rw [aged, if_neg last]
        exact List.mem_cons_of_mem _ inside

theorem agedN_empty {law : ChannelLaw Kind} (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    {l : List (Token Kind)} (within : ∀ tok, tok ∈ l → tok.remaining ≤ law.span tok.kind) :
    agedN (D + 1) l = [] := by
  cases shape : agedN (D + 1) l with
  | nil => rfl
  | cons tok rest =>
    have member : tok ∈ agedN (D + 1) l := by
      rw [shape]
      exact List.mem_cons_self
    obtain ⟨old, oldIn, _, age, positive⟩ := mem_agedN (D + 1) member
    have bound := within old oldIn
    have spanD := spanBound old.kind
    cases positive with
    | inl zero => exact False.elim (Nat.succ_ne_zero D zero)
    | inr alive => exact False.elim (by omega)

/-- The configuration after `i` ticks of forming `B`, starting from `c`. -/
def build (law : ChannelLaw Kind) (B : List Kind) (c : Config Kind) (i : Nat) : Config Kind :=
  ⟨c.reserve - i * formation law B, agedN i c.tokens ++ steady law B i⟩

theorem build_within {law : ChannelLaw Kind} {B : List Kind} {c : Config Kind}
    (within : WithinSpan law c) (i : Nat) : WithinSpan law (build law B c i) := by
  intro tok member
  cases List.mem_append.mp member with
  | inl here =>
    obtain ⟨old, oldIn, kindEq, age, _⟩ := mem_agedN i here
    have bound := within old oldIn
    rw [kindEq] at bound
    omega
  | inr there => exact steady_within law B there

theorem build_step {law : ChannelLaw Kind} {B : List Kind} {c : Config Kind} (D : Nat)
    (positive : ∀ k, 0 < law.span k) (renewing : SelfRenewing law B)
    (seeded : Seeded law c B) (enough : D * formation law B ≤ c.reserve) {i : Nat}
    (early : i < D) :
    (channelProcess law).step (build law B c i) B (build law B c (i + 1)) := by
  obtain ⟨_, supported, _⟩ := renewing
  refine ⟨?_, ?_, ?_⟩
  · show agedN (i + 1) c.tokens ++ steady law B (i + 1) =
      aged (agedN i c.tokens ++ steady law B i) ++ formed law B
    rw [formed_eq_block_zero law B (fun k _ => positive k), aged_append, List.append_assoc,
      steady_shift]
    rfl
  · show c.reserve - (i + 1) * formation law B + formation law B ≤
      c.reserve - i * formation law B + opened law.rate (agedN i c.tokens ++ steady law B i)
    have scaled := Nat.mul_le_mul_right (formation law B) (Nat.succ_le_of_lt early)
    rw [Nat.succ_mul] at scaled ⊢
    omega
  · intro k member
    cases i with
    | zero =>
      obtain ⟨tok, tokIn, kept, edge⟩ := seeded k member
      refine ⟨⟨tok.kind, tok.remaining - 1⟩, ?_, edge⟩
      show ⟨tok.kind, tok.remaining - 1⟩ ∈ aged (c.tokens ++ steady law B 0)
      rw [aged_append]
      exact List.mem_append_left _ (mem_aged_of_kept kept tokIn)
    | succ i =>
      obtain ⟨j, jIn, edge, spanJ⟩ := supported k member
      refine ⟨⟨j, law.span j - 1⟩, ?_, edge⟩
      show ⟨j, law.span j - 1⟩ ∈ aged (agedN (i + 1) c.tokens ++ steady law B (i + 1))
      rw [aged_append]
      exact List.mem_append_right _ (block_one_survives law B i (mem_block law 1 jIn spanJ))

theorem build_live {law : ChannelLaw Kind} {B : List Kind} {c : Config Kind}
    (positive : ∀ k, 0 < law.span k) (renewing : SelfRenewing law B)
    (seeded : Seeded law c B) (i : Nat) : Live (build law B c i) := by
  obtain ⟨nonempty, _, _⟩ := renewing
  cases B with
  | nil => exact False.elim (nonempty rfl)
  | cons k rest =>
    cases i with
    | zero =>
      obtain ⟨tok, tokIn, kept, _⟩ := seeded k List.mem_cons_self
      exact alive_token_live (List.mem_append_left _ tokIn) (Nat.le_of_succ_le kept)
    | succ i =>
      exact alive_token_live
        (List.mem_append_right _ (steady_contains_fresh law List.mem_cons_self (positive k)
          (i + 1) (Nat.zero_lt_succ i)))
        (positive k)

/-- **Reaching a standing renewal.** Suppose a configuration seeds every kind of
a self-renewing population `B`, and holds at least `D + 1` times the formation
demand of `B`. Forming `B` on each of the next `D + 1` ticks reaches the steady
configuration, which renews forever. -/
theorem seeded_renewable {law : ChannelLaw Kind} (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    (positive : ∀ k, 0 < law.span k) {B : List Kind} (renewing : SelfRenewing law B)
    {c : Config Kind} (within : WithinSpan law c) (seeded : Seeded law c B)
    (enough : (D + 1) * formation law B ≤ c.reserve) : Renewable law c := by
  have standing : Renewable law (build law B c (D + 1)) := by
    obtain ⟨nonempty, supported, balanced⟩ := renewing
    have empty := agedN_empty D spanBound (l := c.tokens) within
    have steadyRenewable : Renewable law ⟨0, steady law B (D + 1)⟩ :=
      ⟨steadyExecution law B (D + 1) nonempty (fun k _ => positive k)
          (fun k _ => Nat.le_succ_of_le (spanBound k)) supported balanced,
        rfl, fun _ => (steady_renews law B (D + 1) 0 nonempty (fun k _ => positive k)
          (fun k _ => Nat.le_succ_of_le (spanBound k)) supported balanced).1⟩
    have more := renewable_of_more (extra := []) steadyRenewable (Nat.zero_le
      (c.reserve - (D + 1) * formation law B)) (fun _ member => by cases member)
    show Renewable law ⟨c.reserve - (D + 1) * formation law B,
      agedN (D + 1) c.tokens ++ steady law B (D + 1)⟩
    rw [empty]
    exact more
  have back : ∀ j, j ≤ D + 1 → Renewable law (build law B c (D + 1 - j)) := by
    intro j
    induction j with
    | zero => intro _; exact standing
    | succ j ih =>
      intro within'
      have earlier : D + 1 - (j + 1) < D + 1 := by omega
      have next : D + 1 - (j + 1) + 1 = D + 1 - j := by omega
      have step := build_step (D + 1) positive renewing seeded enough earlier
      rw [next] at step
      exact renewable_of_step (build_within within _) (build_live positive renewing seeded _)
        step (ih (Nat.le_of_succ_le within'))
  have start := back (D + 1) (Nat.le_refl _)
  rw [Nat.sub_self] at start
  have same : build law B c 0 = c := by
    show Config.mk (c.reserve - 0 * formation law B) (c.tokens ++ []) = c
    rw [Nat.zero_mul, Nat.sub_zero, List.append_nil]
  rw [same] at start
  exact start

/-! ## Examples: one self-supporting kind with rate 1, span 3, demand 3 -/

theorem balanced_population : SelfRenewing closedOpenBalanced [()] :=
  ⟨List.cons_ne_nil _ _, fun _ _ => ⟨(), List.mem_cons_self, True.intro, Nat.le_succ 2⟩,
    Nat.le_refl 3⟩

theorem young_token_renewable (R : Nat) (enough : 12 ≤ R) :
    Renewable closedOpenBalanced ⟨R, [⟨(), 2⟩]⟩ :=
  seeded_renewable 3 (fun _ => Nat.le_refl 3) (fun _ => Nat.zero_lt_succ 2) balanced_population
    (fun tok member => by
      cases List.mem_singleton.mp member
      exact Nat.le_succ 2)
    (fun _ _ => ⟨⟨(), 2⟩, List.mem_cons_self, Nat.le_refl 2, True.intro⟩) enough

/-- A token on its last tick supports nothing, so nothing is renewable from it. -/
theorem last_tick_not_renewable (R : Nat) :
    ¬ Renewable closedOpenBalanced ⟨R, [⟨(), 1⟩]⟩ := by
  intro renewable
  obtain ⟨X, start, alive⟩ := renewable
  have step := X.steps 0
  rw [start] at step
  obtain ⟨shape, _, supported⟩ := step
  have noBirths : X.ticks 0 = [] := by
    cases births : X.ticks 0 with
    | nil => rfl
    | cons k rest =>
      rw [births] at supported
      obtain ⟨tok, agedIn, _⟩ := supported k List.mem_cons_self
      cases agedIn
  rw [noBirths] at shape
  have dead : (X.states 1).tokens = [] := shape
  have live := alive 1
  unfold Live at live
  rw [dead] at live
  exact Nat.not_succ_le_zero 0 live

/-- With no reserve, the young token cannot meet a formation, and then it
reaches its last tick. -/
theorem young_token_without_reserve_not_renewable :
    ¬ Renewable closedOpenBalanced ⟨0, [⟨(), 2⟩]⟩ := by
  intro renewable
  obtain ⟨X, start, alive⟩ := renewable
  have step := X.steps 0
  rw [start] at step
  obtain ⟨shape, balance, _⟩ := step
  have budget : (X.states 1).reserve + formation closedOpenBalanced (X.ticks 0) ≤ 0 + 1 :=
    balance
  have noBirths : X.ticks 0 = [] := by
    cases births : X.ticks 0 with
    | nil => rfl
    | cons k rest =>
      rw [births] at budget
      have : 3 ≤ formation closedOpenBalanced (k :: rest) := Nat.le_add_right 3 _
      exact False.elim (by omega)
  rw [noBirths] at shape
  have next : X.states 1 = ⟨(X.states 1).reserve, [⟨(), 1⟩]⟩ := by
    cases h : X.states 1 with
    | mk reserve tokens =>
      rw [h] at shape
      have : tokens = [⟨(), 1⟩] := shape
      rw [this]
  exact last_tick_not_renewable (X.states 1).reserve
    (next ▸ ⟨X.next, rfl, fun n => alive (n + 1)⟩)

/-- **No goal projection decides renewability.** Renewability is not a function
of the reserve and the kinds present: two configurations that differ only in a
token's remaining span differ in renewability. -/
theorem renewability_not_function_of_reserve_and_kinds :
    ¬ ∃ f : Nat → List Unit → Prop, ∀ c : Config Unit,
      Renewable closedOpenBalanced c ↔ f c.reserve (c.tokens.map Token.kind) := by
  intro found
  obtain ⟨f, decides⟩ := found
  have young := (decides ⟨12, [⟨(), 2⟩]⟩).mp (young_token_renewable 12 (Nat.le_refl 12))
  exact last_tick_not_renewable 12 ((decides ⟨12, [⟨(), 1⟩]⟩).mpr young)

/-- Nor is it a function of the tokens alone: the reserve matters. -/
theorem renewability_not_function_of_tokens :
    ¬ ∃ f : List (Token Unit) → Prop, ∀ c : Config Unit,
      Renewable closedOpenBalanced c ↔ f c.tokens := by
  intro found
  obtain ⟨f, decides⟩ := found
  have young := (decides ⟨12, [⟨(), 2⟩]⟩).mp (young_token_renewable 12 (Nat.le_refl 12))
  exact young_token_without_reserve_not_renewable ((decides ⟨0, [⟨(), 2⟩]⟩).mpr young)

/-- **Damage is a local choice.** From one renewable configuration, forming a
token keeps renewability, while forming nothing loses it for good. The second
successor holds more reserve than the first. -/
theorem keeping_and_losing_renewal :
    Renewable closedOpenBalanced ⟨15, [⟨(), 2⟩]⟩ ∧
    (channelProcess closedOpenBalanced).step ⟨15, [⟨(), 2⟩]⟩ [()] ⟨13, [⟨(), 1⟩, ⟨(), 3⟩]⟩ ∧
    Renewable closedOpenBalanced ⟨13, [⟨(), 1⟩, ⟨(), 3⟩]⟩ ∧
    (channelProcess closedOpenBalanced).step ⟨15, [⟨(), 2⟩]⟩ [] ⟨16, [⟨(), 1⟩]⟩ ∧
    ¬ Renewable closedOpenBalanced ⟨16, [⟨(), 1⟩]⟩ := by
  refine ⟨young_token_renewable 15 (by decide), ⟨rfl, by decide, ?_⟩, ?_, ⟨rfl, by decide, ?_⟩,
    last_tick_not_renewable 16⟩
  · intro k _
    exact ⟨⟨(), 1⟩, List.mem_cons_self, True.intro⟩
  · refine seeded_renewable 3 (fun _ => Nat.le_refl 3) (fun _ => Nat.zero_lt_succ 2)
      balanced_population ?_ ?_ (by decide)
    · intro tok member
      cases List.mem_cons.mp member with
      | inl same => subst same; exact Nat.le_succ_of_le (Nat.le_succ 1)
      | inr tail =>
        cases List.mem_singleton.mp tail
        exact Nat.le_refl 3
    · intro _ _
      exact ⟨⟨(), 3⟩, List.mem_cons_of_mem _ List.mem_cons_self, Nat.le_succ 2, True.intro⟩
  · intro k member
    cases member

#print axioms step_within
#print axioms execution_within
#print axioms opened_one_pos
#print axioms alive_token_live
#print axioms dead_stays_dead
#print axioms renewable_live_step
#print axioms renewable_of_step
#print axioms renewable_iff_step
#print axioms renewability_not_generated
#print axioms mem_agedN
#print axioms renewable_of_more
#print axioms mem_aged_of_kept
#print axioms agedN_empty
#print axioms build_within
#print axioms build_step
#print axioms build_live
#print axioms seeded_renewable
#print axioms balanced_population
#print axioms young_token_renewable
#print axioms last_tick_not_renewable
#print axioms young_token_without_reserve_not_renewable
#print axioms renewability_not_function_of_reserve_and_kinds
#print axioms renewability_not_function_of_tokens
#print axioms keeping_and_losing_renewal

end Generative.Conditional.Renewal
