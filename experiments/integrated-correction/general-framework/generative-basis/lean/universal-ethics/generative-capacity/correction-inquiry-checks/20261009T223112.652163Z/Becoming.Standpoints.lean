import Becoming.Descent
import Becoming.Continuation

/-!
# Standpoints: a center at every point

Ren's proposal of 10 October 2026 ends with one axiom: “for anything, its continuation into
the future has significance”. `Becoming.Continuation` states what the dynamics derives with
no ethical premise, the extent a continuing formation must count; it does not settle the
center, whose continuation counts. This module states the center on the valuations of
`Becoming.Metaethics`.

* **Held lives.** A living claim is *held* when some position counts it in its own region
  (`Valuation.Held` for all living claims, `Valuation.Unheld` for a claim no position
  holds). Where every life is held, G0 at the level of claims is exactly S0 at every
  position with standpoint neutrality (`Valuation.significant_iff_held`); neither
  connection nor relational neutrality is used. Where holding is decided and every living
  claim is reached through formed relations from a held one, G0 is S0 at every position,
  standpoint neutrality, and relational neutrality only into claims no position holds
  (`Valuation.significant_iff_reached`). None of these can be dropped: every life held
  and valued by its own standpoint only (`Apart.standpoint_neutrality_is_needed`), a
  life no standpoint holds (`Unclaimed.held_is_needed`), and a reached life no position
  holds (`Relayed.transmission_is_needed`). Read as Ren's proposal reads it, S0 is what
  wanting one's continuation is, and the one axiom puts a center at every point: what
  has significance from one standpoint has it from every standpoint.
* **Each formation its own center.** Read stepwise, with each formation a position whose
  own region is its own events, every living event is held (`Web.held_by_formations`), so
  G0 there is S0 at every formation with standpoint neutrality
  (`Web.significant_iff_self`). The stepwise `living` reading, active and not undermining,
  is one reading of the proposal's weak form, continuation that does not damage another's
  (an AI reading).
* **Conveyance crosses the boundary.** Read with one kind of relatum, conveyance relates
  two events at a common step when something is conveyed between their relata
  (`Flow.conveyance`; `living` is the stepwise reading). A relatum nothing is taken from
  or given to is related to nothing (`Flow.conveyance_idle`). The region of a family
  continuing as in `Flow.fed_from_beyond` is, from no step on, left uncrossed
  (`Flow.boundary_crossed`), so it is not a cut in the relations (`Flow.Cut`,
  `Flow.region_not_a_cut`); under relational neutrality, valuing a relatum's event reaches
  the living event of what is conveyed into it (`Flow.valuing_reaches_source`). In the
  careful totalizer read with one kind of relatum, the supply's region is crossed at every
  step (`Totalizer.crossed`, `Totalizer.supply_not_cut`). Conveyance is a relation the
  earlier readings do not supply: read with one kind of relatum, something conveyed between
  two conditions relates their events (`Flow.roles_conveyance`), while interaction, living
  on and descent relate no two conditions at any steps (`Flow.roles_conditions_unrelated`),
  so the careful totalizer's fuel and supply are related by conveyance alone
  (`Totalizer.conveyance_only`). Whether conveyance counts as a formed relation is Ren's
  choice, as for interaction, living on and descent.
* **The center is not derived.** In the careful totalizer, valued from each formation's own
  standpoint over its own events, every life is held, S0 holds at every position and
  transmission into each position's own region holds, while the other formation's living
  event has no significance from the keeper's standpoint; standpoint neutrality fails and
  G0 fails (`Totalizer.center_not_derived`). With standpoint neutrality added, G0 holds by
  `Web.significant_iff_self`.

S0 read as what wanting is, and standpoint neutrality as the one axiom, are Ren's proposal;
G0 remains the adopted axiom until Ren accepts the restatement. Decided holding is a
disclosed logical commitment of `significant_iff_reached`, as decided equality is of the
conveyance results. Names are working names.
-/

namespace Becoming

/-! ## Held lives -/

namespace Valuation

variable {Pos C : Type} (V : Valuation Pos C)

/-- Every living claim lies in the own region of some position. -/
def Held : Prop :=
  ∀ c, V.living c → ∃ p, V.own p c

/-- A claim no position holds. -/
def Unheld (c : C) : Prop :=
  ¬ ∃ p, V.own p c

variable {V}

/-- Where every living claim is some position's own, G0 is S0 at every position with
standpoint neutrality. Neither connection nor relational neutrality is used. -/
theorem significant_iff_held (held : V.Held) :
    V.Significant ↔ (∀ p, V.SelfGood p) ∧ Neutral V.shares :=
  ⟨fun all => ⟨fun p c _ alive => all p c alive, fun ⟨_, q, c⟩ alive _ => all q c alive⟩,
    fun ⟨self, share⟩ q c alive => match held c alive with
      | ⟨p, own⟩ => share (p, q, c) alive (self p c own alive)⟩

/-- With holding decided, where every living claim is reached through formed relations
from a living claim some position holds, G0 is S0 at every position, standpoint
neutrality, and relational neutrality into claims no position holds. -/
theorem significant_iff_reached [∀ c, Decidable (∃ p, V.own p c)]
    (reached : ∀ c, V.living c → ∃ c₀ p, V.living c₀ ∧ V.own p c₀ ∧ Reach V.relations c₀ c) :
    V.Significant ↔
      (∀ p, V.SelfGood p) ∧ Neutral V.shares ∧ Within (fun i => V.Unheld i.2.2) V.transmits :=
  ⟨fun all => ⟨fun p c _ alive => all p c alive, fun ⟨_, q, c⟩ alive _ => all q c alive,
      fun ⟨p, _, d⟩ _ _ _ alive => all p d alive⟩,
    fun ⟨self, share, transmit⟩ q c alive => match reached c alive with
      | ⟨c₀, p, alive₀, own, path⟩ =>
        (show Invariant V.relations (V.sig q) from fun c' _ d step held =>
          match (inferInstance : Decidable (∃ p, V.own p d)) with
          | .isTrue ⟨p', own'⟩ => share (p', q, d) step.2 (self p' d own' step.2)
          | .isFalse unheld => transmit (q, c', d) unheld held step.1 step.2).reach path
          (share (p, q, c₀) alive₀ (self p c₀ own alive₀))⟩

end Valuation

/-! ## Each formation its own center -/

namespace Web

variable {F Cond Pos : Type} (W : Web F Cond)

/-- Read stepwise with each formation a position whose own region is its own events, every
living event is held. -/
theorem held_by_formations (sig : F → F × Nat → Prop) :
    (W.valuation (fun f e => e.1 = f) sig).Held :=
  fun e _ => ⟨e.1, rfl⟩

/-- So G0 there is S0 at every formation with standpoint neutrality. -/
theorem significant_iff_self (sig : F → F × Nat → Prop) :
    (W.valuation (fun f e => e.1 = f) sig).Significant ↔
      (∀ f, (W.valuation (fun f e => e.1 = f) sig).SelfGood f) ∧
        Neutral (W.valuation (fun f e => e.1 = f) sig).shares :=
  Valuation.significant_iff_held (W.held_by_formations sig)

end Web

namespace Apart

/-- Two lives, each the own region of its own standpoint. -/
def own : Bool → Bool → Prop
  | true, true => True
  | true, false => False
  | false, true => False
  | false, false => True

def valuation : Valuation Bool Bool := ⟨fun _ => True, fun _ _ => True, own, own⟩

/-- Standpoint neutrality is needed: every life is held and valued by its own standpoint,
and significance is not shared. -/
theorem standpoint_neutrality_is_needed :
    valuation.Held ∧ (∀ p, valuation.SelfGood p) ∧ ¬ Neutral valuation.shares ∧
      ¬ valuation.Significant :=
  ⟨fun c _ => match c with
    | true => ⟨true, trivial⟩
    | false => ⟨false, trivial⟩,
   fun _ _ held _ => held,
   fun share => share (true, false, true) trivial trivial,
   fun all => all false true trivial⟩

end Apart

namespace Unclaimed

/-- One standpoint, whose own region is one of two lives. -/
def own : Unit → Bool → Prop
  | (), true => True
  | (), false => False

def valuation : Valuation Unit Bool := ⟨fun _ => True, fun _ _ => False, own, own⟩

/-- Holding is needed: a life held by no standpoint has no significance though S0 and
standpoint neutrality hold. -/
theorem held_is_needed :
    ¬ valuation.Held ∧ (∀ p, valuation.SelfGood p) ∧ Neutral valuation.shares ∧
      ¬ valuation.Significant :=
  ⟨fun held => match held false trivial with
    | ⟨(), no⟩ => no,
   fun _ _ held _ => held,
   fun ⟨(), (), _⟩ _ held => held,
   fun all => all () false trivial⟩

end Unclaimed

namespace Relayed

/-- The held life is related to the unheld one. -/
def related : Bool → Bool → Prop
  | true, false => True
  | true, true => False
  | false, _ => False

def valuation : Valuation Unit Bool := ⟨fun _ => True, related, Unclaimed.own, Unclaimed.own⟩

/-- Relational neutrality into unheld lives is needed: every life is reached from a held
one, S0 and standpoint neutrality hold, and the unheld life has no significance. -/
theorem transmission_is_needed :
    (∀ c, valuation.living c →
        ∃ c₀ p, valuation.living c₀ ∧ valuation.own p c₀ ∧ Reach valuation.relations c₀ c) ∧
      (∀ p, valuation.SelfGood p) ∧ Neutral valuation.shares ∧
      ¬ Within (fun i => valuation.Unheld i.2.2) valuation.transmits ∧
      ¬ valuation.Significant :=
  ⟨fun c _ => match c with
    | true => ⟨true, (), trivial, trivial, Reach.refl _ true⟩
    | false => ⟨true, (), trivial, trivial, Reach.of_step (a := ()) ⟨trivial, trivial⟩⟩,
   fun _ _ held _ => held,
   fun ⟨(), (), _⟩ _ held => held,
   fun transmit => transmit ((), true, false) (fun ⟨(), no⟩ => no) trivial trivial trivial,
   fun all => all () false trivial⟩

end Relayed

/-! ## Conveyance crosses the boundary -/

namespace Flow

section Crossing

variable {X Pos : Type} (L : Flow X X) (W : Web X X) (own sig : Pos → X × Nat → Prop)

/-- Events read stepwise, related when something is conveyed between their relata across
their common step. -/
def conveyance : Valuation Pos (X × Nat) where
  living e := W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1
  related e e' := e.2 = e'.2 ∧ (L.Conveys e.2 e.1 e'.1 ∨ L.Conveys e.2 e'.1 e.1)
  own := own
  sig := sig

variable {L W own sig}

/-- A relatum nothing is taken from or given to across a step is related to nothing at that
step. -/
theorem conveyance_idle {x : X} {t : Nat}
    (idle : ∀ f, f ∈ L.present t → L.take t f x = 0 ∧ L.give t f x = 0) :
    ∀ e, ¬ (L.conveyance W own sig).related (x, t) e :=
  fun _ ⟨_, conveys⟩ => match conveys with
    | .inl ⟨f, present, takes, _⟩ =>
      Nat.lt_irrefl 0 (Eq.subst (motive := fun n => 0 < n) (idle f present).1 takes)
    | .inr ⟨f, present, _, gives⟩ =>
      Nat.lt_irrefl 0 (Eq.subst (motive := fun n => 0 < n) (idle f present).2 gives)

/-- The boundary of a continuing family is, from no step on, left uncrossed by
conveyance. -/
theorem boundary_crossed [DecidableEq X] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List X} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t) (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t)
    (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ ∃ c d, ¬ c ∈ ds ∧ d ∈ ds ∧
      (L.conveyance W own sig).related (c, t) (d, t) :=
  fun never => fed_from_beyond balances dissipative distinct around recurs N
    fun t later ⟨c, d, outside, inside, conveys⟩ =>
      never t later ⟨c, d, outside, inside, rfl, .inl conveys⟩

/-- Under N_rel, valuing a relatum's event reaches the living event of what is conveyed
into it at that step. -/
theorem valuing_reaches_source (transmit : Neutral (L.conveyance W own sig).transmits)
    {p : Pos} {c d : X} {t : Nat} (conveys : L.Conveys t c d) (held : sig p (d, t))
    (alive : (L.conveyance W own sig).living (c, t)) : sig p (c, t) :=
  transmit (p, (d, t), (c, t)) held ⟨rfl, .inr conveys⟩ alive

/-- No formed relation leaves the region: its boundary is a cut in the relations. -/
def Cut {Q : Type} (V : Valuation Pos Q) (region : Q → Prop) : Prop :=
  ∀ e e', region e → ¬ region e' → ¬ V.related e e'

/-- The region of a continuing family is not a cut: conveyance leaves it. -/
theorem region_not_a_cut [DecidableEq X] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List X} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t) (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) :
    ¬ Cut (L.conveyance W own sig) (fun e => e.1 ∈ ds) :=
  fun cut => boundary_crossed (own := own) (sig := sig) balances dissipative distinct around
    recurs 0 fun t _ ⟨c, d, outside, inside, related⟩ =>
      cut (d, t) (c, t) inside outside ⟨rfl, related.2.symm⟩

end Crossing

section Roles

variable {F C Pos : Type} (L : Flow F C) (W : Web F C) (own sig : Pos → (F ⊕ C) × Nat → Prop)

/-- Read with one kind of relatum, something conveyed between two conditions relates their
events at that step. -/
theorem roles_conveyance {t : Nat} {c d : C} (conveys : L.Conveys t c d) :
    (L.roles.conveyance W.roles own sig).related (.inr c, t) (.inr d, t) :=
  match conveys with
  | ⟨f, present, takes, gives⟩ => ⟨rfl, .inl ⟨.inl f, mem_map_of present, takes, gives⟩⟩

/-- Interaction, living on and descent relate no two events of relata that take no part:
read with one kind of relatum, no two conditions are related by them, at any steps. -/
theorem roles_conditions_unrelated (c d : C) (t t' : Nat) :
    ¬ (W.roles.interaction own sig).related (.inr c, t) (.inr d, t') ∧
      ¬ (W.roles.sustenance own sig).related (.inr c, t) (.inr d, t') ∧
      ¬ (L.roles.descent W.roles own sig).related (.inr c, t) (.inr d, t') :=
  have apart : ¬ ∃ x, W.roles.Interacts x (.inr c, t) (.inr d, t') :=
    fun ⟨_, interacts⟩ => match interacts with
      | .inl ⟨drawn, _⟩ => drawn
      | .inr ⟨⟨required, _⟩, _⟩ => required
  ⟨apart,
   fun related => match related with
    | .inl interacts => apart interacts
    | .inr (.inl ⟨drawn, _⟩) => drawn
    | .inr (.inr ⟨drawn, _⟩) => drawn,
   fun related => match related with
    | .inl interacts => apart interacts
    | .inr (.inl ⟨_, present, _⟩) => inr_not_mem present
    | .inr (.inr ⟨_, present, _⟩) => inr_not_mem present⟩

end Roles

end Flow

/-! ## The careful totalizer from its standpoints -/

namespace Totalizer

open Frontier (burning)

/-- Read with one kind of relatum, conveyance relates the step's fuel to the supply at
every step. -/
theorem crossed {Pos : Type} (own sig : Pos → (Formation ⊕ Place) × Nat → Prop) (t : Nat) :
    (Flow.conveyance flow.roles web.roles own sig).related (.inr (.fuel t), t)
      (.inr .supply, t) :=
  ⟨rfl, .inl ⟨.inl .sun, .head _,
    show 0 < 2 * burning t t from
      Eq.subst (motive := fun b => 0 < 2 * b) (Frontier.burning_self t).symm (Nat.succ_pos 1),
    Nat.zero_lt_one⟩⟩

/-- So the supply's region is not a cut in the relations. -/
theorem supply_not_cut {Pos : Type} (own sig : Pos → (Formation ⊕ Place) × Nat → Prop) :
    ¬ Flow.Cut (Flow.conveyance flow.roles web.roles own sig)
      (fun e => e.1 ∈ [Sum.inr Place.supply]) :=
  fun cut => cut (.inr .supply, 0) (.inr (.fuel 0), 0) (.head _)
    (fun mem => match mem with | .tail _ no => nomatch no)
    ⟨rfl, (crossed own sig 0).2.symm⟩

/-- Conveyance relates the step's fuel and the supply, which neither interaction, living on
nor descent relates. -/
theorem conveyance_only {Pos : Type} (own sig : Pos → (Formation ⊕ Place) × Nat → Prop)
    (t : Nat) :
    (Flow.conveyance flow.roles web.roles own sig).related (.inr (.fuel t), t)
        (.inr .supply, t) ∧
      ¬ (web.roles.interaction own sig).related (.inr (.fuel t), t) (.inr .supply, t) ∧
      ¬ (web.roles.sustenance own sig).related (.inr (.fuel t), t) (.inr .supply, t) ∧
      ¬ (flow.roles.descent web.roles own sig).related (.inr (.fuel t), t) (.inr .supply, t) :=
  ⟨crossed own sig t, Flow.roles_conditions_unrelated flow web own sig (.fuel t) .supply t t⟩

/-- Each formation holds and values exactly its own events. -/
def own : Formation → Formation × Nat → Prop :=
  fun f e => e.1 = f

def valuation : Valuation Formation (Formation × Nat) :=
  web.valuation own own

/-- The center is not derived. Valued from each formation's own standpoint over its own
events, every life is held, S0 holds at every position, and transmission into each
position's own region holds; the other formation's event at step zero is living, and has
no significance from the keeper's standpoint, so standpoint neutrality and G0 fail. -/
theorem center_not_derived :
    valuation.Held ∧ (∀ f, valuation.SelfGood f) ∧
      Within (fun i => own i.1 i.2.2) valuation.transmits ∧
      valuation.living (.other, 0) ∧ ¬ valuation.sig .keeper (.other, 0) ∧
      ¬ Neutral valuation.shares ∧ ¬ valuation.Significant :=
  have alive : valuation.living (.other, 0) := ⟨trivial, fun ⟨_, draws, _⟩ => draws⟩
  have apart : ¬ valuation.sig .keeper (.other, 0) := fun same => Formation.noConfusion same
  ⟨web.held_by_formations own, fun _ _ owned _ => owned, fun _ bound _ _ _ => bound,
   alive, apart, fun share => apart (share (.other, .keeper, (.other, 0)) alive rfl),
   fun all => apart (all .keeper (.other, 0) alive)⟩

end Totalizer

end Becoming
