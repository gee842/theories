import Becoming.Descent

/-!
# Feasibility sketch for the continuation-grounding plan (scratch only)

Checks that the plan's central statements are expressible on the committed core and
provable without axioms: W1 (a continuing family is fed from beyond), W2 (conveyance
crosses the boundary of the family's region), W3 (counting one's own draw does not keep
the commons) and W5 (lives held by standpoints, and the center). Names are working
names.
-/

namespace Becoming

/-! ## W5: lives held by standpoints -/

namespace Valuation

variable {Pos C : Type} (V : Valuation Pos C)

/-- Every living claim lies in the own region of some position. -/
def Held : Prop :=
  ∀ c, V.living c → ∃ p, V.own p c

variable {V}

/-- Where every living claim is some position's own, G0 is S0 at every position with
standpoint neutrality. Neither connection nor relational neutrality is used. -/
theorem significant_iff_held (held : V.Held) :
    V.Significant ↔ (∀ p, V.SelfGood p) ∧ Neutral V.shares :=
  ⟨fun all => ⟨fun p c _ alive => all p c alive, fun ⟨_, q, c⟩ alive _ => all q c alive⟩,
    fun ⟨self, share⟩ q c alive => match held c alive with
      | ⟨p, own⟩ => share (p, q, c) alive (self p c own alive)⟩

variable (V)

/-- A claim no position holds. -/
def Unheld (c : C) : Prop :=
  ¬ ∃ p, V.own p c

variable {V}

/-- With holding decided, where every living claim is reached through formed relations
from a claim some position holds, G0 is S0 at every position with standpoint neutrality
and relational neutrality into claims no position holds. -/
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

namespace OwnStandpoints

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

end OwnStandpoints

namespace Unheld

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

end Unheld

namespace Reached

/-- The held life is related to the unheld one. -/
def related : Bool → Bool → Prop
  | true, false => True
  | true, true => False
  | false, _ => False

def valuation : Valuation Unit Bool := ⟨fun _ => True, related, Unheld.own, Unheld.own⟩

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

end Reached

/-! ## W1: a continuing family is fed from beyond -/

namespace Flow

section Conveying

variable {F C : Type} (L : Flow F C)

/-- Across the step from `t`, some formation taking part takes from `c` and gives to `d`. -/
def Conveys (t : Nat) (c d : C) : Prop :=
  ∃ f, f ∈ L.present t ∧ 0 < L.take t f c ∧ 0 < L.give t f d

/-- Across the step from `t`, something beyond the family is conveyed into it. -/
def FedFromBeyond (ds : List C) (t : Nat) : Prop :=
  ∃ c d, ¬ c ∈ ds ∧ d ∈ ds ∧ L.Conveys t c d

variable {L} {W : Web F C}

/-- With equality decided, a step at which nothing beyond the family is conveyed into it
draws nothing in. -/
theorem inward_of_not_fed [DecidableEq C] {ds : List C} {t : Nat}
    (none : ¬ L.FedFromBeyond ds t) : L.Inward ds t :=
  fun f present gives c takes => match decideMem c ds with
    | .isTrue mem => mem
    | .isFalse outside => match total_pos ds gives with
      | ⟨d, inside, given⟩ => absurd ⟨c, d, outside, inside, f, present, takes, given⟩ none

/-- A continuing family is fed from beyond: under balance and dissipation, where formations
take from a finite family without repetition at arbitrarily late steps and the family is
enclosed around from some step on, it is not the case that from some step on nothing
beyond it is conveyed into it. -/
theorem fed_from_beyond [DecidableEq C] (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List C} (distinct : Distinct ds) {T₀ : Nat} (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fun never => taking_draws_in balances dissipative distinct around recurs N
    fun t later => inward_of_not_fed (never t later)

end Conveying

/-! ## W2: conveyance crosses the boundary of the family's region -/

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

/-- The boundary of a continuing family is crossed by conveyance at arbitrarily late
steps. -/
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

/-- The region of a continuing family is not a cut: some formed relation, conveyance,
leaves it. -/
theorem region_not_a_cut [DecidableEq X] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List X} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t) (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) :
    ¬ Cut (L.conveyance W own sig) (fun e => e.1 ∈ ds) :=
  fun cut => boundary_crossed (own := own) (sig := sig) balances dissipative distinct around recurs 0
    fun t _ ⟨c, d, outside, inside, related⟩ =>
      cut (d, t) (c, t) inside outside ⟨rfl, related.2.symm⟩

end Crossing

/-! ## W3: counting one's own draw does not keep the commons -/

section Joint

variable {F C : Type}

/-- Each formation taking part takes from the condition no more than the step gives it. -/
def WithinOwn (L : Flow F C) (t : Nat) (c : C) : Prop :=
  ∀ f, f ∈ L.present t → L.take t f c ≤ L.given t c

/-- Together the formations take from the condition no more than the step gives it. -/
def WithinJoint (L : Flow F C) (t : Nat) (c : C) : Prop :=
  L.taken t c ≤ L.given t c

variable {L : Flow F C} {W : Web F C}

/-- Taking jointly within what is given, the level does not fall. -/
theorem joint_keeps (balances : L.Balances W) {t : Nat} {c : C}
    (within : L.WithinJoint t c) : W.level t c ≤ W.level (t + 1) c :=
  le_of_add_le_add_right (L.taken t c)
    (Nat.le_trans (Nat.add_le_add_left within (W.level t c)) (Nat.le_of_eq (balances t c).symm))

/-- A step of joint excess lowers the level by at least one. -/
theorem excess_lowers (balances : L.Balances W) {t : Nat} {c : C}
    (excess : L.given t c < L.taken t c) : W.level (t + 1) c + 1 ≤ W.level t c :=
  le_of_add_le_add_right (L.given t c)
    (Nat.le_trans
      (Nat.le_of_eq ((Nat.add_assoc _ 1 _).trans
        (congrArg (W.level (t + 1) c + ·) (Nat.add_comm 1 (L.given t c)))))
      (Nat.le_trans
        (Nat.add_le_add_left (show L.given t c + 1 ≤ L.taken t c from excess) _)
        (Nat.le_of_eq (balances t c))))

/-- Joint excess cannot last: over `n` consecutive steps of joint excess from `T` the level
falls by at least `n`. -/
theorem excess_bounded (balances : L.Balances W) {c : C} {T : Nat} :
    ∀ n, (∀ k, k < n → L.given (T + k) c < L.taken (T + k) c) →
      W.level (T + n) c + n ≤ W.level T c
  | 0, _ => Nat.le_refl _
  | n + 1, excess =>
    Nat.le_trans (Nat.le_of_eq (Nat.add_right_comm (W.level (T + n + 1) c) n 1))
      (Nat.le_trans (Nat.add_le_add_right (excess_lowers balances (excess n (Nat.lt_succ_self n))) n)
        (excess_bounded balances n fun k below => excess k (Nat.lt_succ_of_lt below)))

end Joint

end Flow

namespace Pair

/-- Two formations each take one unit from one condition at every step; one of them gives
it one unit back. -/
def flow : Flow Bool Unit :=
  ⟨fun _ => [true, false], fun _ _ _ => 1, fun _ f _ => match f with
    | true => 1
    | false => 0⟩

/-- Each takes within what the step gives, together they take more. -/
theorem own_not_joint (t : Nat) : flow.WithinOwn t () ∧ ¬ flow.WithinJoint t () :=
  ⟨fun _ _ => Nat.le_refl 1, fun within => Nat.not_succ_le_self 1 within⟩

/-- So no web balances it: the joint excess cannot go on. -/
theorem no_web : ¬ ∃ W : Web Bool Unit, flow.Balances W :=
  fun ⟨W, balances⟩ =>
    Nat.not_succ_le_self (W.level 0 ())
      (Nat.le_trans (Nat.le_add_left _ (W.level (0 + (W.level 0 () + 1)) ()))
        (Flow.excess_bounded balances (W.level 0 () + 1) fun _ _ => Nat.lt_succ_self 1))

end Pair

end Becoming
