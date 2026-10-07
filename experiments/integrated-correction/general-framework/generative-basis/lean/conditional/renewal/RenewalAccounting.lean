import GenerativeCore
import Depletion
import RenewalBasics

/-!
# Renewal accounting: a constraint that brings in less than its formation demands

Phase 1 of the renewal–closure roadmap, accounting part. Organized tokens of
finitely many kinds keep their remaining span; every tick each token's span falls
by one and spent tokens drop out. A live token opens arrival at its kind's rate.
Forming a token of kind `k` makes a demand `demand k` on the reserve and gives
it `span k` ticks. The reserve law is the U1 law of `ResourceContinuation` with
arrival bounded by what live tokens open; raw flow outside is unlimited.

If every kind falls short, `rate k * span k < demand k`, then a combined
potential strictly decreases on every tick at which some token is alive. So
renewal ends by an explicit deadline, by the depletion theorem already in the
core. This holds whatever the support edges are; closure alone cannot save a
system whose constraints never bring in what their formation demands.

Edges, spans, demands and rates are supplied inputs.
-/

namespace Generative.Conditional.Renewal

open Generative

universe u

/-- An organized token and the ticks it has left. -/
structure Token (Kind : Type u) where
  kind : Kind
  remaining : Nat

/-- A whole configuration: the reserve and every organized token. -/
structure Config (Kind : Type u) where
  reserve : Nat
  tokens : List (Token Kind)

/-- Supplied local law of a constraint–flow system. -/
structure ChannelLaw (Kind : Type u) where
  edge : Kind → Kind → Prop
  span : Kind → Nat
  demand : Kind → Nat
  rate : Kind → Nat

variable {Kind : Type u}

/-- One tick of aging: spans fall by one and tokens on their last tick leave. -/
def aged : List (Token Kind) → List (Token Kind)
  | [] => []
  | tok :: rest =>
    if tok.remaining ≤ 1 then aged rest else ⟨tok.kind, tok.remaining - 1⟩ :: aged rest

/-- Remaining span weighted per kind. -/
def weighted (w : Kind → Nat) : List (Token Kind) → Nat
  | [] => 0
  | tok :: rest => w tok.kind * tok.remaining + weighted w rest

/-- What live tokens open this tick, weighted per kind. -/
def opened (w : Kind → Nat) : List (Token Kind) → Nat
  | [] => 0
  | tok :: rest => (if tok.remaining = 0 then 0 else w tok.kind) + opened w rest

/-- Newly formed tokens. -/
def formed (law : ChannelLaw Kind) : List Kind → List (Token Kind)
  | [] => []
  | k :: rest => ⟨k, law.span k⟩ :: formed law rest

/-- Total formation demand of a list of formations. -/
def formation (law : ChannelLaw Kind) : List Kind → Nat
  | [] => 0
  | k :: rest => law.demand k + formation law rest

theorem weighted_append (w : Kind → Nat) :
    ∀ (l m : List (Token Kind)), weighted w (l ++ m) = weighted w l + weighted w m
  | [], m => (Nat.zero_add (weighted w m)).symm
  | tok :: rest, m => by
    show w tok.kind * tok.remaining + weighted w (rest ++ m) =
      w tok.kind * tok.remaining + weighted w rest + weighted w m
    rw [weighted_append w rest m, Nat.add_assoc]

/-- Aging moves exactly what live tokens open out of the weighted span. -/
theorem weighted_aged (w : Kind → Nat) :
    ∀ l : List (Token Kind), weighted w (aged l) + opened w l = weighted w l
  | [] => rfl
  | tok :: rest => by
    have ih := weighted_aged w rest
    by_cases last : tok.remaining ≤ 1
    · rw [aged, if_pos last, opened, weighted]
      by_cases zero : tok.remaining = 0
      · rw [if_pos zero, zero, Nat.mul_zero, Nat.zero_add, Nat.zero_add]
        exact ih
      · rw [if_neg zero]
        have one : tok.remaining = 1 := Nat.le_antisymm last (pos_of_ne_zero_of zero)
        rw [one, Nat.mul_one, Nat.add_left_comm, ih]
    · have notZero : ¬ tok.remaining = 0 := fun zero => last (zero ▸ Nat.zero_le 1)
      have shape : tok.remaining = tok.remaining - 1 + 1 :=
        (sub_add_cancel_of_le (pos_of_ne_zero_of notZero)).symm
      rw [aged, if_neg last, opened, if_neg notZero]
      show w tok.kind * (tok.remaining - 1) + weighted w (aged rest) +
          (w tok.kind + opened w rest) = w tok.kind * tok.remaining + weighted w rest
      calc w tok.kind * (tok.remaining - 1) + weighted w (aged rest) +
            (w tok.kind + opened w rest)
          = w tok.kind * (tok.remaining - 1) + w tok.kind +
            (weighted w (aged rest) + opened w rest) := Nat.add_add_add_comm _ _ _ _
        _ = w tok.kind * tok.remaining + weighted w rest := by
          rw [ih, ← Nat.mul_succ]
          exact congrArg (fun n => w tok.kind * n + weighted w rest) shape.symm

theorem weighted_formed_le (law : ChannelLaw Kind) (w : Kind → Nat) (D : Nat)
    (spanBound : ∀ k, law.span k ≤ D) (wBound : ∀ k, w k ≤ 1) :
    ∀ births : List Kind, weighted w (formed law births) ≤ D * births.length
  | [] => Nat.zero_le _
  | k :: rest => by
    have ih := weighted_formed_le law w D spanBound wBound rest
    have one : w k * law.span k ≤ D :=
      calc w k * law.span k ≤ 1 * law.span k := Nat.mul_le_mul_right _ (wBound k)
        _ = law.span k := Nat.one_mul _
        _ ≤ D := spanBound k
    show w k * law.span k + weighted w (formed law rest) ≤ D * (rest.length + 1)
    rw [Nat.mul_succ, Nat.add_comm (D * rest.length) D]
    exact Nat.add_le_add one ih

/-- When every kind falls short, a formation's demand exceeds what its tokens
can ever open, by at least one per formation. -/
theorem formation_exceeds_opening (law : ChannelLaw Kind)
    (short : ∀ k, law.rate k * law.span k + 1 ≤ law.demand k) :
    ∀ births : List Kind,
      weighted law.rate (formed law births) + births.length ≤ formation law births
  | [] => Nat.le_refl 0
  | k :: rest => by
    have ih := formation_exceeds_opening law short rest
    show law.rate k * law.span k + weighted law.rate (formed law rest) + (rest.length + 1) ≤
      law.demand k + formation law rest
    rw [Nat.add_comm rest.length 1, Nat.add_add_add_comm]
    exact Nat.add_le_add (short k) ih

/-- One tick of a constraint–flow system. Every formed token needs a support
token that is still alive after aging, so it existed before this tick. -/
def channelProcess (law : ChannelLaw Kind) : Process (Config Kind) (List Kind) where
  step c births c' :=
    c'.tokens = aged c.tokens ++ formed law births ∧
    c'.reserve + formation law births ≤ c.reserve + opened law.rate c.tokens ∧
    ∀ k, k ∈ births → ∃ tok, tok ∈ aged c.tokens ∧ law.edge tok.kind k

/-- Some organized token is alive. -/
def Live (c : Config Kind) : Prop := 1 ≤ opened (fun _ => 1) c.tokens

/-- Ticks of renewal: a token is alive before each tick. -/
def renewingProcess (law : ChannelLaw Kind) : Process (Config Kind) (List Kind) where
  step c births c' := Live c ∧ (channelProcess law).step c births c'

/-- Reserve plus what live tokens can still open. -/
def openingPotential (law : ChannelLaw Kind) (c : Config Kind) : Nat :=
  c.reserve + weighted law.rate c.tokens

/-- Remaining organized life. -/
def lifePotential (c : Config Kind) : Nat := weighted (fun _ => 1) c.tokens

/-- Combined potential: remaining life plus `D` times the opening potential. -/
def renewalPotential (law : ChannelLaw Kind) (D : Nat) (c : Config Kind) : Nat :=
  lifePotential c + D * openingPotential law c

/-- The reserve law in potential form: what a tick forms is demanded from the
reserve, and what live tokens open comes out of their remaining span. -/
theorem opening_step (law : ChannelLaw Kind) {c c' : Config Kind} {births : List Kind}
    (step : (channelProcess law).step c births c') :
    openingPotential law c' + formation law births ≤
      openingPotential law c + weighted law.rate (formed law births) := by
  have ⟨shape, balance, _⟩ := step
  have aging := weighted_aged law.rate c.tokens
  show c'.reserve + weighted law.rate c'.tokens + formation law births ≤
    c.reserve + weighted law.rate c.tokens + weighted law.rate (formed law births)
  rw [shape, weighted_append, ← aging]
  calc c'.reserve + (weighted law.rate (aged c.tokens) + weighted law.rate (formed law births)) +
        formation law births
      = c'.reserve + formation law births +
        (weighted law.rate (aged c.tokens) + weighted law.rate (formed law births)) :=
        Nat.add_right_comm _ _ _
    _ ≤ c.reserve + opened law.rate c.tokens +
        (weighted law.rate (aged c.tokens) + weighted law.rate (formed law births)) :=
        Nat.add_le_add_right balance _
    _ = c.reserve + (weighted law.rate (aged c.tokens) + opened law.rate c.tokens) +
        weighted law.rate (formed law births) := by
      rw [← Nat.add_assoc, Nat.add_assoc c.reserve, Nat.add_comm (opened law.rate c.tokens)]

/-- With every kind short, each formation lowers the opening potential by at
least one. -/
theorem short_opening_step (law : ChannelLaw Kind)
    (short : ∀ k, law.rate k * law.span k + 1 ≤ law.demand k)
    {c c' : Config Kind} {births : List Kind}
    (step : (channelProcess law).step c births c') :
    openingPotential law c' + births.length ≤ openingPotential law c := by
  have base := opening_step law step
  have gap := formation_exceeds_opening law short births
  apply le_of_add_le_add_right_of (k := weighted law.rate (formed law births))
  calc openingPotential law c' + births.length + weighted law.rate (formed law births)
      = openingPotential law c' + (weighted law.rate (formed law births) + births.length) := by
        rw [Nat.add_assoc, Nat.add_comm births.length]
    _ ≤ openingPotential law c' + formation law births := Nat.add_le_add_left gap _
    _ ≤ openingPotential law c + weighted law.rate (formed law births) := base

/-- A live tick lowers remaining life by at least one, and formations add at
most `D` each. -/
theorem life_step (law : ChannelLaw Kind) (D : Nat) (spanBound : ∀ k, law.span k ≤ D)
    {c c' : Config Kind} {births : List Kind}
    (step : (renewingProcess law).step c births c') :
    lifePotential c' + 1 ≤ lifePotential c + D * births.length := by
  have ⟨live, shape, _, _⟩ := step
  have aging := weighted_aged (fun _ => 1) c.tokens
  have added := weighted_formed_le law (fun _ => 1) D spanBound (fun _ => Nat.le_refl 1) births
  have live : 1 ≤ opened (fun _ => 1) c.tokens := live
  show weighted (fun _ => 1) c'.tokens + 1 ≤ weighted (fun _ => 1) c.tokens + D * births.length
  rw [shape, weighted_append, ← aging]
  calc weighted (fun _ => 1) (aged c.tokens) + weighted (fun _ => 1) (formed law births) + 1
      = weighted (fun _ => 1) (aged c.tokens) + 1 + weighted (fun _ => 1) (formed law births) :=
        Nat.add_right_comm _ _ _
    _ ≤ weighted (fun _ => 1) (aged c.tokens) + opened (fun _ => 1) c.tokens +
        weighted (fun _ => 1) (formed law births) :=
        Nat.add_le_add_right (Nat.add_le_add_left live _) _
    _ ≤ weighted (fun _ => 1) (aged c.tokens) + opened (fun _ => 1) c.tokens +
        D * births.length := Nat.add_le_add_left added _

/-- **Short constraints deplete.** If every kind brings in less than its
formation demands over its span, the renewal potential strictly decreases on
every tick at which some token is alive. -/
theorem short_renewal_depletes (law : ChannelLaw Kind) (D : Nat)
    (spanBound : ∀ k, law.span k ≤ D)
    (short : ∀ k, law.rate k * law.span k + 1 ≤ law.demand k) :
    ∀ c births c', (renewingProcess law).step c births c' →
      renewalPotential law D c' < renewalPotential law D c := by
  intro c births c' step
  have life := life_step law D spanBound step
  have opening := short_opening_step law short step.2
  have scaled := Nat.mul_le_mul_left D opening
  rw [Nat.mul_add] at scaled
  show lifePotential c' + D * openingPotential law c' + 1 ≤
    lifePotential c + D * openingPotential law c
  calc lifePotential c' + D * openingPotential law c' + 1
      = lifePotential c' + 1 + D * openingPotential law c' := Nat.add_right_comm _ _ _
    _ ≤ lifePotential c + D * births.length + D * openingPotential law c' :=
        Nat.add_le_add_right life _
    _ = lifePotential c + (D * openingPotential law c' + D * births.length) := by
        rw [Nat.add_assoc, Nat.add_comm (D * births.length)]
    _ ≤ lifePotential c + D * openingPotential law c := Nat.add_le_add_left scaled _

/-- An explicit deadline: renewal lasts at most the starting renewal potential
in ticks. -/
theorem short_renewal_deadline (law : ChannelLaw Kind) (D : Nat)
    (spanBound : ∀ k, law.span k ≤ D)
    (short : ∀ k, law.rate k * law.span k + 1 ≤ law.demand k)
    {c c' : Config Kind} {ticks : List (List Kind)}
    (history : Trace (renewingProcess law) c ticks c') :
    ticks.length ≤ lifePotential c + D * openingPotential law c :=
  trace_length_bound (renewalPotential law D) (short_renewal_depletes law D spanBound short)
    history

/-- No endless renewal when every kind falls short, whatever the support edges. -/
theorem short_kinds_cannot_renew_forever (law : ChannelLaw Kind) (D : Nat)
    (spanBound : ∀ k, law.span k ≤ D)
    (short : ∀ k, law.rate k * law.span k + 1 ≤ law.demand k) :
    ¬ ∃ states : Nat → Config Kind, ∃ ticks : Nat → List Kind,
      ∀ n, (renewingProcess law).step (states n) (ticks n) (states (n + 1)) :=
  no_infinite_execution_under_depletion (renewalPotential law D)
    (short_renewal_depletes law D spanBound short)

#print axioms weighted_append
#print axioms weighted_aged
#print axioms weighted_formed_le
#print axioms formation_exceeds_opening
#print axioms opening_step
#print axioms short_opening_step
#print axioms life_step
#print axioms short_renewal_depletes
#print axioms short_renewal_deadline
#print axioms short_kinds_cannot_renew_forever

/-- One self-supporting kind that opens a channel: a single closed constraint
open to an unbounded flow. Each token brings in 1 per tick for 3 ticks, and
forming one demands 4. -/
def closedOpenShort : ChannelLaw Unit where
  edge _ _ := True
  span _ := 3
  demand _ := 4
  rate _ := 1

/-- The system really does renew for a tick: a live token supports a new one. -/
theorem closedOpenShort_ticks :
    (renewingProcess closedOpenShort).step
      ⟨4, [⟨(), 3⟩]⟩ [()] ⟨1, [⟨(), 2⟩, ⟨(), 3⟩]⟩ := by
  refine ⟨?_, rfl, ?_, ?_⟩
  · show 1 ≤ opened (fun _ => 1) [(⟨(), 3⟩ : Token Unit)]
    decide
  · show 1 + formation closedOpenShort [()] ≤ 4 + opened closedOpenShort.rate [⟨(), 3⟩]
    decide
  · intro k _
    exact ⟨⟨(), 2⟩, List.mem_singleton_self _, True.intro⟩

/-- **Closure plus openness is not sufficient.** The kind supports itself, so it
is closed; arrival through its tokens is unlimited, so it is open. It still
cannot renew forever, because `1 * 3 < 4`. -/
theorem closed_open_short_cannot_renew_forever :
    ¬ ∃ states : Nat → Config Unit, ∃ ticks : Nat → List Unit,
      ∀ n, (renewingProcess closedOpenShort).step (states n) (ticks n) (states (n + 1)) :=
  short_kinds_cannot_renew_forever closedOpenShort 3 (fun _ => Nat.le_refl 3)
    (fun _ => Nat.le_refl 4)

#print axioms closedOpenShort_ticks
#print axioms closed_open_short_cannot_renew_forever

end Generative.Conditional.Renewal
