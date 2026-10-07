import RenewalClosure
import RenewalAccounting

/-!
# One model: renewing configurations carry a realized closure

Phase 2 of the renewal–closure roadmap. It joins the two Phase 1 results on
the same histories. Every token in an execution of `channelProcess` either
came from the initial configuration or was formed on a definite earlier tick.
Its remaining span then records how long ago that was.

Formations are therefore occurrences in the sense of `OccurrenceSupport`. Their
supporters must survive a tick, so only kinds with span at least two can
support. Every late live configuration then descends from a realized closure of
kinds whose supporters outlast the tick on which they act. This is the
timescale separation of Montévil and Mossio, here as a consequence rather than
a definition.

An `Execution` is a history whose initial tokens hold no more than their
kind's span. This is not a premise of the main theorems: every history becomes
an execution once its initial tokens have run out (`History.settled`), and the
theorems are stated for histories from any start.
-/

namespace Generative.Conditional.Renewal

open Generative

universe u

variable {Kind : Type u}

theorem mem_aged {tok : Token Kind} :
    ∀ {l : List (Token Kind)}, tok ∈ aged l →
      ∃ old, old ∈ l ∧ old.kind = tok.kind ∧ tok.remaining + 1 = old.remaining ∧
        2 ≤ old.remaining
  | [], member => by cases member
  | old :: rest, member => by
    by_cases last : old.remaining ≤ 1
    · rw [aged, if_pos last] at member
      obtain ⟨o, inside, kindEq, ageEq, kept⟩ := mem_aged member
      exact ⟨o, List.mem_cons_of_mem _ inside, kindEq, ageEq, kept⟩
    · rw [aged, if_neg last] at member
      cases List.mem_cons.mp member with
      | inl same =>
        subst same
        exact ⟨old, List.mem_cons_self, rfl, by simp only; omega, by omega⟩
      | inr tail =>
        obtain ⟨o, inside, kindEq, ageEq, kept⟩ := mem_aged tail
        exact ⟨o, List.mem_cons_of_mem _ inside, kindEq, ageEq, kept⟩

theorem mem_formed (law : ChannelLaw Kind) {tok : Token Kind} :
    ∀ {births : List Kind}, tok ∈ formed law births →
      tok.kind ∈ births ∧ tok.remaining = law.span tok.kind
  | k :: rest, member => by
    rw [formed] at member
    cases List.mem_cons.mp member with
    | inl same => subst same; exact ⟨List.mem_cons_self, rfl⟩
    | inr tail =>
      obtain ⟨inside, span⟩ := mem_formed law tail
      exact ⟨List.mem_cons_of_mem _ inside, span⟩

/-- A history of the constraint–flow process from any configuration. -/
structure History (law : ChannelLaw Kind) where
  states : Nat → Config Kind
  ticks : Nat → List Kind
  steps : ∀ n, (channelProcess law).step (states n) (ticks n) (states (n + 1))

/-- Every token holds no more than its kind's span. -/
def WithinSpan (law : ChannelLaw Kind) (c : Config Kind) : Prop :=
  ∀ tok, tok ∈ c.tokens → tok.remaining ≤ law.span tok.kind

/-- A history whose initial tokens hold no more than their kind's span. Every
history becomes one once its initial tokens have run out (`History.settled`). -/
structure Execution (law : ChannelLaw Kind) extends History law where
  initialWithinSpan : WithinSpan law (states 0)

/-- Where each token came from: the initial configuration, or a formation on an
earlier tick, with the remaining span fixed by how long ago. -/
theorem token_origin {law : ChannelLaw Kind} (X : History law) :
    ∀ t tok, tok ∈ (X.states t).tokens →
      (∃ first, first ∈ (X.states 0).tokens ∧ first.kind = tok.kind ∧
        tok.remaining + t = first.remaining) ∨
      (∃ m, m < t ∧ tok.kind ∈ X.ticks m ∧ tok.remaining + t = law.span tok.kind + (m + 1))
  | 0, tok, member => Or.inl ⟨tok, member, rfl, rfl⟩
  | t + 1, tok, member => by
    rw [(X.steps t).1] at member
    cases List.mem_append.mp member with
    | inl agedIn =>
      obtain ⟨old, oldIn, kindEq, ageEq, _⟩ := mem_aged agedIn
      cases token_origin X t old oldIn with
      | inl initial =>
        obtain ⟨first, firstIn, firstKind, firstAge⟩ := initial
        exact Or.inl ⟨first, firstIn, firstKind.trans kindEq, by omega⟩
      | inr formedEarlier =>
        obtain ⟨m, earlier, inTick, spanEq⟩ := formedEarlier
        exact Or.inr ⟨m, by omega, kindEq ▸ inTick, by rw [← kindEq]; omega⟩
    | inr formedNow =>
      obtain ⟨inTick, spanEq⟩ := mem_formed law formedNow
      exact Or.inr ⟨t, Nat.lt_succ_self t, inTick, by omega⟩

/-- The largest value of `f` on a list. -/
def maxOver {α : Type u} (f : α → Nat) : List α → Nat
  | [] => 0
  | a :: rest => if f a ≤ maxOver f rest then maxOver f rest else f a

theorem le_maxOver {α : Type u} (f : α → Nat) :
    ∀ {l : List α} {a : α}, a ∈ l → f a ≤ maxOver f l
  | [], _, member => by cases member
  | b :: rest, a, member => by
    rw [maxOver]
    by_cases smaller : f b ≤ maxOver f rest
    · rw [if_pos smaller]
      cases List.mem_cons.mp member with
      | inl same => subst same; exact smaller
      | inr tail => exact le_maxOver f tail
    · rw [if_neg smaller]
      cases List.mem_cons.mp member with
      | inl same => subst same; exact Nat.le_refl _
      | inr tail => exact Nat.le_trans (le_maxOver f tail) (Nat.le_of_lt (Nat.gt_of_not_le smaller))

/-- The history after its first `k` ticks. -/
def History.shift {law : ChannelLaw Kind} (H : History law) (k : Nat) : History law where
  states n := H.states (k + n)
  ticks n := H.ticks (k + n)
  steps n := H.steps (k + n)

/-- The time by which every initial token has run out. -/
def History.settle {law : ChannelLaw Kind} (H : History law) : Nat :=
  maxOver Token.remaining (H.states 0).tokens

/-- Once the initial tokens have run out, every token holds no more than its
kind's span. -/
theorem History.settled_within {law : ChannelLaw Kind} (H : History law) :
    WithinSpan law (H.states H.settle) := by
  intro tok member
  cases token_origin H H.settle tok member with
  | inl initial =>
    obtain ⟨first, firstIn, _, firstAge⟩ := initial
    have bound := le_maxOver Token.remaining firstIn
    have zero : tok.remaining = 0 := by
      show tok.remaining = 0
      have : first.remaining ≤ H.settle := bound
      omega
    rw [zero]
    exact Nat.zero_le _
  | inr formedEarlier =>
    obtain ⟨m, earlier, _, spanEq⟩ := formedEarlier
    omega

/-- Every history, from the time its initial tokens have run out, is an
execution. -/
def History.settled {law : ChannelLaw Kind} (H : History law) : Execution law where
  toHistory := H.shift H.settle
  initialWithinSpan := H.settled_within

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

/-- Formations, and initial tokens at time zero, as occurrences. A supporter
must outlast the tick, so the support edge records a span of at least two. -/
def executionSupport {law : ChannelLaw Kind} (X : Execution law) : OccurrenceSupport Kind where
  occurs k t := (t = 0 ∧ ∃ tok, tok ∈ (X.states 0).tokens ∧ tok.kind = k) ∨
    (∃ m, t = m + 1 ∧ k ∈ X.ticks m)
  edge j k := law.edge j k ∧ 2 ≤ law.span j
  reach j := law.span j - 1
  support := by
    intro k t occ positive
    cases occ with
    | inl initial => exact False.elim (Nat.lt_irrefl 0 (initial.1 ▸ positive))
    | inr formedAt =>
      obtain ⟨n, timeEq, inTick⟩ := formedAt
      subst timeEq
      obtain ⟨tok, agedIn, edgeTK⟩ := (X.steps n).2.2 k inTick
      obtain ⟨old, oldIn, kindEq, _, kept⟩ := mem_aged agedIn
      cases token_origin X.toHistory n old oldIn with
      | inl initial =>
        obtain ⟨first, firstIn, firstKind, firstAge⟩ := initial
        have within := X.initialWithinSpan first firstIn
        rw [firstKind, kindEq] at within
        refine ⟨tok.kind, 0, ⟨edgeTK, by omega⟩, ?_, Nat.zero_lt_succ n, by omega⟩
        exact Or.inl ⟨rfl, first, firstIn, firstKind.trans kindEq⟩
      | inr formedEarlier =>
        obtain ⟨m, earlier, inTick', spanEq⟩ := formedEarlier
        rw [kindEq] at spanEq inTick'
        refine ⟨tok.kind, m + 1, ⟨edgeTK, by omega⟩, Or.inr ⟨m, rfl, inTick'⟩, by omega, by omega⟩

/-- A live configuration holds a token with time left. -/
theorem live_has_alive_token {c : Config Kind} (live : Live c) :
    ∃ tok, tok ∈ c.tokens ∧ 1 ≤ tok.remaining := by
  unfold Live at live
  generalize c.tokens = l at live
  induction l with
  | nil => exact False.elim (Nat.not_succ_le_zero 0 live)
  | cons tok rest ih =>
    by_cases zero : tok.remaining = 0
    · rw [opened, if_pos zero, Nat.zero_add] at live
      obtain ⟨found, inside, positive⟩ := ih live
      exact ⟨found, List.mem_cons_of_mem _ inside, positive⟩
    · exact ⟨tok, List.mem_cons_self, Nat.pos_of_ne_zero zero⟩

/-- A token alive after the longest span was formed recently, as an occurrence
of its kind. -/
theorem alive_token_recent_formation {law : ChannelLaw Kind} (X : Execution law)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) {t : Nat} {tok : Token Kind}
    (member : tok ∈ (X.states t).tokens) (alive : 1 ≤ tok.remaining) (late : D < t) :
    ∃ s, (executionSupport X).occurs tok.kind s ∧ s ≤ t ∧ t < s + D := by
  cases token_origin X.toHistory t tok member with
  | inl initial =>
    obtain ⟨first, firstIn, firstKind, firstAge⟩ := initial
    have within := X.initialWithinSpan first firstIn
    have bound := spanBound first.kind
    exact False.elim (by omega)
  | inr formedEarlier =>
    obtain ⟨m, earlier, inTick, spanEq⟩ := formedEarlier
    have bound := spanBound tok.kind
    exact ⟨m + 1, Or.inr ⟨m, rfl, inTick⟩, earlier, by omega⟩

/-- A live configuration after the longest span holds a token formed recently. -/
theorem live_late_has_recent_formation {law : ChannelLaw Kind} (X : Execution law)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) {t : Nat}
    (live : Live (X.states t)) (late : D < t) :
    ∃ k s, (executionSupport X).occurs k s ∧ s ≤ t ∧ t < s + D := by
  obtain ⟨tok, member, alive⟩ := live_has_alive_token live
  obtain ⟨s, occ, before, near⟩ := alive_token_recent_formation X D spanBound member alive late
  exact ⟨tok.kind, s, occ, before, near⟩

/-- **Renewal carries a realized closure.** In any execution with finitely many
kinds and spans at most `D`, a live configuration after `(n + 1) · D` descends
from a closed walk of support kinds. Each supporter on that walk has span at
least two, and each of its kinds was formed within the preceding `(n + 1) · D`
ticks. -/
theorem live_late_descends_from_realized_closure [DecidableEq Kind]
    {law : ChannelLaw Kind} (X : Execution law) (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) {t : Nat}
    (live : Live (X.states t)) (late : (U.length + 1) * D < t) :
    ∃ j cycle, cycle ≠ [] ∧
      Walk (fun a b => law.edge a b ∧ 2 ≤ law.span a) j (j :: cycle) j ∧
      DependenceClosed (fun a b => law.edge a b ∧ 2 ≤ law.span a) cycle ∧
      ∀ v, v ∈ cycle → ∃ s, (executionSupport X).occurs v s ∧ s ≤ t ∧
        t < s + (U.length + 1) * D := by
  have Dbound : D < t := by
    have : D ≤ (U.length + 1) * D := by
      rw [Nat.succ_mul]
      exact Nat.le_add_left _ _
    omega
  obtain ⟨k, s, occ, sBefore, recent⟩ :=
    live_late_has_recent_formation X D spanBound live Dbound
  have reachBound : ∀ j, (executionSupport X).reach j ≤ D := by
    intro j
    have := spanBound j
    show law.span j - 1 ≤ D
    omega
  have lateS : U.length * D < s := by
    rw [Nat.succ_mul] at late
    omega
  obtain ⟨j, cycle, _, nonempty, loop, _, closed, window⟩ :=
    late_occurrence_descends_from_realized_closure (executionSupport X) U complete D reachBound
      occ lateS
  refine ⟨j, cycle, nonempty, loop, closed, ?_⟩
  intro v member
  obtain ⟨r, occV, before, near⟩ := window v (List.mem_append_left _ member)
  refine ⟨r, occV, Nat.le_trans before sBefore, ?_⟩
  rw [Nat.succ_mul]
  omega

/-- A decidable search through a finite list of kinds. -/
theorem find_or_none (P : Kind → Prop) [DecidablePred P] :
    ∀ U : List Kind, (∃ k, k ∈ U ∧ P k) ∨ (∀ k, k ∈ U → ¬ P k)
  | [] => Or.inr (fun _ member => by cases member)
  | k :: rest =>
    if here : P k then Or.inl ⟨k, List.mem_cons_self, here⟩
    else
      match find_or_none P rest with
      | Or.inl ⟨j, inside, holds⟩ => Or.inl ⟨j, List.mem_cons_of_mem _ inside, holds⟩
      | Or.inr absent => Or.inr (fun j member => by
          cases List.mem_cons.mp member with
          | inl same => exact same ▸ here
          | inr tail => exact absent j tail)

/-- **Both necessary conditions on one history.** An execution that stays live
forever has a kind that brings in at least what its formation demands, and every
live configuration after `(n + 1) · D` descends from a realized closure of
support kinds whose supporters outlast the tick. -/
theorem endless_renewal_needs_closure_and_adequate_kind [DecidableEq Kind]
    {law : ChannelLaw Kind} (X : Execution law) (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) (alive : ∀ n, Live (X.states n)) :
    (∃ k, law.demand k ≤ law.rate k * law.span k) ∧
    ∀ t, (U.length + 1) * D < t →
      ∃ j cycle, cycle ≠ [] ∧
        Walk (fun a b => law.edge a b ∧ 2 ≤ law.span a) j (j :: cycle) j ∧
        DependenceClosed (fun a b => law.edge a b ∧ 2 ≤ law.span a) cycle ∧
        ∀ v, v ∈ cycle → ∃ s, (executionSupport X).occurs v s ∧ s ≤ t ∧
          t < s + (U.length + 1) * D := by
  refine ⟨?_, fun t late => live_late_descends_from_realized_closure X U complete D spanBound
    (alive t) late⟩
  cases find_or_none (fun k => law.demand k ≤ law.rate k * law.span k) U with
  | inl found =>
    obtain ⟨k, _, adequate⟩ := found
    exact ⟨k, adequate⟩
  | inr absent =>
    have short : ∀ k, law.rate k * law.span k + 1 ≤ law.demand k :=
      fun k => Nat.gt_of_not_le (absent k (complete k))
    exact False.elim (short_kinds_cannot_renew_forever law D spanBound short
      ⟨X.states, X.ticks, fun n => ⟨alive n, X.steps n⟩⟩)

#print axioms mem_aged
#print axioms mem_formed
#print axioms token_origin
#print axioms le_maxOver
#print axioms History.settled_within
#print axioms step_within
#print axioms execution_within
#print axioms live_has_alive_token
#print axioms alive_token_recent_formation
#print axioms live_late_has_recent_formation
#print axioms live_late_descends_from_realized_closure
#print axioms find_or_none
#print axioms endless_renewal_needs_closure_and_adequate_kind

end Generative.Conditional.Renewal
