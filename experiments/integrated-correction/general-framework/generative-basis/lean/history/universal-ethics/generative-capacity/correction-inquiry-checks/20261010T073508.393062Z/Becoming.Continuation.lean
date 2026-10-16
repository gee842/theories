import Becoming.Roles

/-!
# Continuation: what a continuing formation must count

Ren's proposal of 10 October 2026 restates the metaethical core in two halves. Anything
that wants its continuation gives that continuation significance; following that want, it
must count what its continuation depends on, and the dynamics, with no ethical premise,
says how far that count reaches. This module states that half on flows and webs. The
center, whose continuation counts, is not settled here: `Becoming.Standpoints` states it.

* **Beyond the boundary.** Across a step, a formation taking part *conveys* from `c` to `d`
  when it takes from `c` and gives to `d` (`Flow.Conveys`); a family is *fed from beyond*
  across the step when something outside it is conveyed into one of its members
  (`Flow.FedFromBeyond`). A step at which the family is fed from beyond is not inward
  (`not_inward_of_fed`), and with equality decided a step at which it is not fed from
  beyond is inward (`inward_of_not_fed`), so the two are exact opposites
  (`inward_iff_not_fed`). Every draw-in law therefore reads as being fed: whatever refutes
  "inward from some step on" refutes "fed from nothing beyond from some step on"
  (`fed_of_not_inward`). Under balance and dissipation, a finite family without
  repetition, enclosed around from some step on, cannot from any step on be fed from
  nothing beyond it, whether taking from it recurs (`fed_from_beyond`), its members rise
  at arbitrarily late steps (`rising_fed_from_beyond`), or, read with one kind of
  relatum, embodied members arise at arbitrarily late steps
  (`Web.generation_fed_from_beyond`). Being fed is needed; no source condition need
  recur: in `Lone` the pool is fed at every step, and each fuel is conveyed from at one
  step only (`Lone.fed`, `Lone.each_fuel_once`). The one formation conveying, the sun, is
  the same at every step.
* **Beyond one's own draw.** Each formation can take from a condition within what the
  step gives it (`WithinOwn`) while together they take more (`WithinJoint` fails;
  `Pair.own_not_joint`). Taking jointly within what is given keeps the level
  (`joint_keeps`); a step of joint excess lowers it by at least one (`excess_lowers`), so
  `n` consecutive steps of joint excess need a level of at least `n` at the start
  (`excess_bounded`), and in the pair no web balances the flow at all (`Pair.no_web`).
* **Renewal that depends on what it renews.** Where every formation giving to a condition
  depends on it at a need of at least `m`, only active formations give and activity needs
  support, a level below `m` stays below `m` at every later step (`stays_below`), and
  every formation depending on the condition at a need of at least `m` is inactive from
  then on (`ends_below`). Joint excess that brings the level below `m` therefore ends the
  renewal and every formation depending on the condition at such a need, a taker among
  them where it so depends (`joint_excess_ends`). The joint count binds a want that
  outlasts what the condition holds: `n` steps of joint excess need only a level of `n`.
  In `Exceeding` a renewer and two takers, each taking within what the step gives, all end
  after two steps (`Exceeding.all_end`); with one taker the same renewer keeps the level
  and all continue (`Alone.all_continue`).
* **What the derived extent does not reach.** Following the want counts what one's
  continuation depends on, and no more. In `Downstream` the self's continuation requires
  only its ground; a formation living on what the self gives ends when it stops giving,
  and the self continues (`Downstream.one_way`). In `Mortal` a formation active for two
  steps has every dependence met while it lives; its taking ends the renewal of a shared
  condition, and another formation depending on it ends after the first has ended
  (`Mortal.after_its_end`); without it, the renewer and the heir continue
  (`Mortal.without_continues`). In `Totalizer`
  a keeper is active at every step, every condition it depends on is renewed and fed from
  beyond, and it takes jointly within what is given from each of them, while it draws
  down the habitat of another formation, which ends (`Totalizer.careful`). The endings in
  these witnesses are stipulated in their activity; each witness shows its ending
  consistent with balance, support and dependence, and the general theorems are where an
  ending is derived. The sun of `Totalizer`, like that of `Lone`, requires nothing.

The draw-in laws this module rereads are those of `Becoming.Dissipation` and
`Becoming.Roles`; the delta is the conveyance form, its exactness, the joint count, the
support-gated end, and the limits. Equality decided is a disclosed logical commitment, as
in `Flow.Enclosed.around`. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

namespace Flow

/-! ## Conveying and being fed from beyond -/

section Conveying

variable (L : Flow F C)

/-- Across the step from `t`, some formation taking part takes from `c` and gives to `d`:
something is conveyed from `c` to `d`. -/
def Conveys (t : Nat) (c d : C) : Prop :=
  ∃ f, f ∈ L.present t ∧ 0 < L.take t f c ∧ 0 < L.give t f d

/-- Across the step from `t`, something beyond the family is conveyed into one of its
members. -/
def FedFromBeyond (ds : List C) (t : Nat) : Prop :=
  ∃ c d, ¬ c ∈ ds ∧ d ∈ ds ∧ L.Conveys t c d

variable {L}

/-- A step at which the family is fed from beyond is not inward. -/
theorem not_inward_of_fed {ds : List C} {t : Nat} (fed : L.FedFromBeyond ds t) :
    ¬ L.Inward ds t :=
  match fed with
  | ⟨c, _, outside, inside, f, present, takes, gives⟩ => fun inward =>
    outside (inward f present (total_pos_of_mem inside gives) c takes)

/-- With equality decided, a step at which nothing beyond the family is conveyed into it
is inward. -/
theorem inward_of_not_fed [DecidableEq C] {ds : List C} {t : Nat}
    (none : ¬ L.FedFromBeyond ds t) : L.Inward ds t :=
  fun f present gives c takes => match decideMem c ds with
    | .isTrue mem => mem
    | .isFalse outside => match total_pos ds gives with
      | ⟨d, inside, given⟩ => absurd ⟨c, d, outside, inside, f, present, takes, given⟩ none

/-- With equality decided, a step is inward exactly when the family is not fed from beyond
across it. -/
theorem inward_iff_not_fed [DecidableEq C] {ds : List C} {t : Nat} :
    L.Inward ds t ↔ ¬ L.FedFromBeyond ds t :=
  ⟨fun inward fed => not_inward_of_fed fed inward, inward_of_not_fed⟩

/-- Whatever refutes "inward from `N` on" refutes "fed from nothing beyond from `N` on". -/
theorem fed_of_not_inward [DecidableEq C] {ds : List C} {N : Nat}
    (opens : ¬ ∀ t, N ≤ t → L.Inward ds t) : ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fun never => opens fun t later => inward_of_not_fed (never t later)

variable {W : Web F C}

/-- A continuing family is fed from beyond: under balance and dissipation, where formations
take from a finite family without repetition at arbitrarily late steps and the family is
enclosed around from some step on, it cannot from any step on be fed from nothing beyond
it. -/
theorem fed_from_beyond [DecidableEq C] (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List C} (distinct : Distinct ds) {T₀ : Nat} (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fed_of_not_inward (taking_draws_in balances dissipative distinct around recurs N)

/-- So is a family whose members rise at arbitrarily late steps. -/
theorem rising_fed_from_beyond [DecidableEq C] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List C} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (rising : ∀ N, ∃ t c, N ≤ t ∧ c ∈ ds ∧ W.Rises t c) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fed_of_not_inward (rising_draws_in balances dissipative distinct around rising N)

end Conveying

/-! ## Counting one's own draw and the joint draw -/

section Joint

/-- Each formation taking part takes from the condition no more than the step gives it. -/
def WithinOwn (L : Flow F C) (t : Nat) (c : C) : Prop :=
  ∀ f, f ∈ L.present t → L.take t f c ≤ L.given t c

/-- Together the formations taking part take from the condition no more than the step
gives it. -/
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

/-- Joint excess cannot last: over `n` consecutive steps of joint excess from `T`, the
level falls by at least `n`. -/
theorem excess_bounded (balances : L.Balances W) {c : C} {T : Nat} :
    ∀ n, (∀ k, k < n → L.given (T + k) c < L.taken (T + k) c) →
      W.level (T + n) c + n ≤ W.level T c
  | 0, _ => Nat.le_refl _
  | n + 1, excess =>
    Nat.le_trans (Nat.le_of_eq (Nat.add_right_comm (W.level (T + n + 1) c) n 1))
      (Nat.le_trans
        (Nat.add_le_add_right (excess_lowers balances (excess n (Nat.lt_succ_self n))) n)
        (excess_bounded balances n fun k below => excess k (Nat.lt_succ_of_lt below)))

end Joint

/-! ## Renewal that depends on what it renews -/

section Gated

variable {L : Flow F C} {W : Web F C}

/-- Once below `m`, always below `m`: where every formation giving to the condition
depends on it at a need of at least `m`, only active formations give and activity needs
support, nothing gives to the condition while its level is below `m`, so the level stays
below `m`. -/
theorem stays_below (balances : L.Balances W) (acting : L.Acting W)
    (dependent : W.Dependent) {c : C} {m : Nat}
    (gated : ∀ t f, f ∈ L.present t → 0 < L.give t f c →
      W.requires t f c ∧ m ≤ W.need t f c)
    {T : Nat} (below : W.level T c < m) : ∀ n, W.level (T + n) c < m
  | 0 => below
  | n + 1 =>
    have before := stays_below balances acting dependent gated below n
    have none : L.given (T + n) c = 0 := total_eq_zero fun f present =>
      eq_zero_of_not_pos fun gives => match gated (T + n) f present gives with
        | ⟨depends, high⟩ =>
          Nat.lt_irrefl m (Nat.lt_of_le_of_lt (Nat.le_trans high
            (dependent (T + n) f (acting (T + n) f c present gives) c depends)) before)
    Nat.lt_of_le_of_lt
      (Nat.le_trans (Nat.le_add_right _ (L.taken (T + n) c))
        (Nat.le_of_eq ((balances (T + n) c).trans (congrArg (W.level (T + n) c + ·) none))))
      before

/-- Below `m` from `T` on, every formation depending on the condition at a need of at least
`m` is inactive. -/
theorem ends_below (dependent : W.Dependent) {c : C} {m T : Nat}
    (below : ∀ n, W.level (T + n) c < m) :
    ∀ n g, W.requires (T + n) g c → m ≤ W.need (T + n) g c → ¬ W.active (T + n) g :=
  fun n g depends high active =>
    Nat.lt_irrefl m (Nat.lt_of_le_of_lt
      (Nat.le_trans high (dependent (T + n) g active c depends)) (below n))

/-- Joint excess ends gated renewal: if `n` consecutive steps of joint excess from `T`
start below `n + m`, the level is below `m` from `T + n` on, nothing gives to the
condition again, and every formation depending on it at a need of at least `m` is
inactive from then on, the takers included. -/
theorem joint_excess_ends (balances : L.Balances W) (acting : L.Acting W)
    (dependent : W.Dependent) {c : C} {m : Nat}
    (gated : ∀ t f, f ∈ L.present t → 0 < L.give t f c →
      W.requires t f c ∧ m ≤ W.need t f c)
    {T n : Nat} (excess : ∀ k, k < n → L.given (T + k) c < L.taken (T + k) c)
    (start : W.level T c < n + m) :
    ∀ k g, W.requires (T + n + k) g c → m ≤ W.need (T + n + k) g c →
      ¬ W.active (T + n + k) g :=
  ends_below dependent (stays_below balances acting dependent gated
    (Nat.lt_of_add_lt_add_left (n := n)
      (Nat.lt_of_le_of_lt
        (Nat.le_trans (Nat.le_of_eq (Nat.add_comm n _)) (excess_bounded balances n excess))
        start)))

end Gated

end Flow

/-! ## Read with one kind of relatum: generation is fed from beyond -/

namespace Web

variable {X : Type} {W : Web X X} {L : Flow X X}

/-- Under dissipation, a finite family without repetition in which embodied members arise
at arbitrarily late steps, enclosed around from some step on, cannot from any step on be
fed from nothing beyond it. -/
theorem generation_fed_from_beyond [DecidableEq X] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List X} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (arising : ∀ N, ∃ t x, N ≤ t ∧ x ∈ ds ∧ W.Embodied x ∧ W.Arises t x) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  Flow.fed_of_not_inward (generation_draws_in balances dissipative distinct around arising N)

end Web

/-! ## Being fed is needed; no source condition need recur -/

namespace Lone

open Frontier (Condition burning)

/-- The pool is fed from beyond at every step: the sun conveys from the step's fuel. -/
theorem fed (t : Nat) : flow.FedFromBeyond [.pool] t :=
  ⟨.fuel t, .pool, (fun mem => match mem with | .tail _ no => nomatch no),
   .head _, .sun, .head _,
   show 0 < 2 * burning t t from
     Eq.subst (motive := fun b => 0 < 2 * b) (Frontier.burning_self t).symm (Nat.succ_pos 1),
   Nat.zero_lt_one⟩

/-- Each fuel is conveyed from at one step only, its own. -/
theorem each_fuel_once {n t : Nat} {d : Condition} (conveys : flow.Conveys t (.fuel n) d) :
    n = t :=
  match conveys with
  | ⟨f, _, takes, _⟩ => match f, takes with
    | .sun, takes => Frontier.burning_at n t (match h : burning n t with
      | 0 => absurd (Eq.subst (motive := fun b => 0 < 2 * b) h takes) (Nat.lt_irrefl 0)
      | k + 1 => Nat.succ_pos k)
    | .eater, takes => absurd takes (Nat.lt_irrefl 0)

/-- So in a balanced, dissipative flow whose takers recur, the pool is fed at every step,
while no fuel is conveyed from after its step. -/
theorem supply_not_source :
    flow.Balances web ∧ flow.Dissipative ∧ (∀ t, flow.FedFromBeyond [.pool] t) ∧
      ∀ n t, n < t → ∀ d, ¬ flow.Conveys t (.fuel n) d :=
  ⟨balances, dissipative, fed, fun _ _ before _ conveys =>
    Nat.lt_irrefl _ (Eq.subst (motive := fun m => m < _) (each_fuel_once conveys) before)⟩

end Lone

/-! ## Witnesses -/

namespace Pair

/-- Two formations each take one unit from one condition at every step; one of them gives
it one unit back. -/
def flow : Flow Bool Unit :=
  ⟨fun _ => [true, false], fun _ _ _ => 1, fun _ f _ => match f with
    | true => 1
    | false => 0⟩

/-- Each takes within what the step gives; together they take more. -/
theorem own_not_joint (t : Nat) : flow.WithinOwn t () ∧ ¬ flow.WithinJoint t () :=
  ⟨fun _ _ => Nat.le_refl 1, fun within => Nat.not_succ_le_self 1 within⟩

/-- So no web balances it: the joint excess cannot go on. -/
theorem no_web : ¬ ∃ W : Web Bool Unit, flow.Balances W :=
  fun ⟨W, balances⟩ =>
    Nat.not_succ_le_self (W.level 0 ())
      (Nat.le_trans (Nat.le_add_left _ (W.level (0 + (W.level 0 () + 1)) ()))
        (Flow.excess_bounded balances (W.level 0 () + 1) fun _ _ => Nat.lt_succ_self 1))

end Pair

namespace Exceeding

/-- A renewer and two takers share one condition. -/
inductive Member where
  | renewer
  | first
  | second

def level : Nat → Nat
  | 0 => 4
  | 1 => 2
  | _ + 2 => 0

def live : Nat → Prop
  | 0 => True
  | 1 => True
  | _ + 2 => False

def present : Nat → List Member
  | 0 => [.renewer, .first, .second]
  | 1 => [.renewer, .first, .second]
  | _ + 2 => []

/-- The renewer gives two units and each taker takes two, while they take part. -/
def flow : Flow Member Unit where
  present := present
  take _ f _ := match f with
    | .renewer => 0
    | .first => 2
    | .second => 2
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0

/-- Each depends on the condition at need one, the renewer included. -/
def web : Web Member Unit where
  level t _ := level t
  active t _ := live t
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => True

theorem balances : flow.Balances web
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem live_of_present : ∀ t f, f ∈ present t → live t
  | 0, _, _ => trivial
  | 1, _, _ => trivial
  | _ + 2, _, no => nomatch no

theorem acting : flow.Acting web :=
  fun t f _ present _ => live_of_present t f present

theorem dependent : web.Dependent
  | 0, _, _, _, _ => Nat.succ_le_succ (Nat.zero_le 3)
  | 1, _, _, _, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | _ + 2, _, dead, _, _ => nomatch dead

/-- Only the renewer gives, and it depends on the condition at need one. -/
theorem gated : ∀ t f, f ∈ flow.present t → 0 < flow.give t f () →
    web.requires t f () ∧ 1 ≤ web.need t f () :=
  fun _ _ _ _ => ⟨trivial, Nat.le_refl 1⟩

/-- While they take part, each taker takes within what the step gives, and together they
take more. -/
theorem own_not_joint : ∀ t, t < 2 → flow.WithinOwn t () ∧ ¬ flow.WithinJoint t ()
  | 0, _ => ⟨fun f _ => match f with
      | .renewer => Nat.zero_le 2
      | .first => Nat.le_refl 2
      | .second => Nat.le_refl 2,
    fun within => Nat.not_succ_le_self 2 (Nat.le_trans (Nat.le_succ 3) (show 4 ≤ 2 from within))⟩
  | 1, _ => ⟨fun f _ => match f with
      | .renewer => Nat.zero_le 2
      | .first => Nat.le_refl 2
      | .second => Nat.le_refl 2,
    fun within => Nat.not_succ_le_self 2 (Nat.le_trans (Nat.le_succ 3) (show 4 ≤ 2 from within))⟩
  | _ + 2, late => absurd late (Nat.not_lt_of_le (Nat.le_add_left 2 _))

/-- So the renewal ends and every member ends with it, the renewer and both takers: from
step two on nothing is active. The stipulated activity says so; derived here through the
law of gated renewal, the witness shows the law's hypotheses hold with that ending. -/
theorem all_end : ∀ n f, ¬ web.active (2 + n) f :=
  fun n f => Flow.ends_below (W := web) (c := ()) (m := 1) (T := 2) dependent
    (Flow.stays_below balances acting dependent gated (T := 2) Nat.zero_lt_one) n f
    trivial (Nat.le_refl 1)

end Exceeding

namespace Alone

/-- The same renewer with one taker. -/
def flow : Flow Exceeding.Member Unit where
  present _ := [.renewer, .first]
  take _ f _ := match f with
    | .renewer => 0
    | .first => 2
    | .second => 0
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0

def web : Web Exceeding.Member Unit where
  level _ _ := 4
  active _ f := match f with
    | .renewer => True
    | .first => True
    | .second => False
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => False

theorem balances : flow.Balances web := fun _ _ => rfl

theorem dependent : web.Dependent :=
  fun _ _ _ _ _ => Nat.succ_le_succ (Nat.zero_le 3)

/-- The taker takes jointly within what is given, and the renewer and the taker are active
at every step. -/
theorem all_continue :
    flow.Balances web ∧ web.Dependent ∧ (∀ t, flow.WithinJoint t ()) ∧
      ∀ t, web.active t .renewer ∧ web.active t .first :=
  ⟨balances, dependent, fun _ => Nat.le_refl 2, fun _ => ⟨trivial, trivial⟩⟩

end Alone

namespace Downstream

inductive Formation where
  | self
  | down

inductive Condition where
  | ground
  | gift

def giftLevel : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 1
  | 3 => 1
  | _ + 4 => 0

def downLive : Nat → Prop
  | 0 => True
  | 1 => True
  | 2 => True
  | 3 => True
  | _ + 4 => False

/-- The self gives the gift one unit for three steps; the downstream formation takes one
unit of it while it is active. -/
def present : Nat → List Formation
  | 0 => [.self, .down]
  | 1 => [.self, .down]
  | 2 => [.self, .down]
  | 3 => [.down]
  | _ + 4 => []

def flow : Flow Formation Condition where
  present := present
  take _ f c := match f, c with
    | .self, _ => 0
    | .down, .ground => 0
    | .down, .gift => 1
  give _ f c := match f, c with
    | .self, .ground => 0
    | .self, .gift => 1
    | .down, _ => 0

/-- The self depends on its ground, the downstream formation on the gift. -/
def web : Web Formation Condition where
  level t c := match c with
    | .ground => 1
    | .gift => giftLevel t
  active t f := match f with
    | .self => True
    | .down => downLive t
  requires _ f c := match f, c with
    | .self, .ground => True
    | .self, .gift => False
    | .down, .ground => False
    | .down, .gift => True
  need _ _ _ := 1
  draws _ f c := match f, c with
    | .self, _ => False
    | .down, .ground => False
    | .down, .gift => True

theorem balances : flow.Balances web
  | 0, .ground => rfl
  | 0, .gift => rfl
  | 1, .ground => rfl
  | 1, .gift => rfl
  | 2, .ground => rfl
  | 2, .gift => rfl
  | 3, .ground => rfl
  | 3, .gift => rfl
  | _ + 4, .ground => rfl
  | _ + 4, .gift => rfl

theorem dependent : web.Dependent
  | _, .self, _, .ground, _ => Nat.le_refl 1
  | _, .self, _, .gift, no => nomatch no
  | _, .down, _, .ground, no => nomatch no
  | 0, .down, _, .gift, _ => Nat.le_refl 1
  | 1, .down, _, .gift, _ => Nat.le_refl 1
  | 2, .down, _, .gift, _ => Nat.le_refl 1
  | 3, .down, _, .gift, _ => Nat.le_refl 1
  | _ + 4, .down, dead, .gift, _ => nomatch dead

/-- The derived extent runs one way. The self's continuation requires only its ground, and
the self is active and supported at every step; the formation living on what the self
gives ends once the self stops giving. -/
theorem one_way :
    flow.Balances web ∧ web.Dependent ∧ (∀ t c, web.requires t .self c → c = .ground) ∧
      (∀ t, web.active t .self ∧ web.Supported t .self) ∧
      ∀ n, ¬ web.active (n + 4) .down :=
  ⟨balances, dependent,
   fun _ c depends => match c, depends with | .ground, _ => rfl,
   fun t => ⟨trivial, dependent t .self trivial⟩,
   fun _ dead => dead⟩

end Downstream

namespace Mortal

/-- A renewer, an heir and a formation whose life is two steps. -/
inductive Member where
  | renewer
  | heir
  | mortal

def level : Nat → Nat
  | 0 => 3
  | 1 => 2
  | 2 => 1
  | _ + 3 => 0

def present : Nat → List Member
  | 0 => [.renewer, .heir, .mortal]
  | 1 => [.renewer, .heir, .mortal]
  | 2 => [.heir]
  | _ + 3 => []

/-- The renewer gives one unit; the heir and the mortal formation each take one. -/
def flow : Flow Member Unit where
  present := present
  take _ f _ := match f with
    | .renewer => 0
    | .heir => 1
    | .mortal => 1
  give _ f _ := match f with
    | .renewer => 1
    | .heir => 0
    | .mortal => 0

def live : Nat → Member → Prop
  | 0, _ => True
  | 1, _ => True
  | 2, .renewer => False
  | 2, .heir => True
  | 2, .mortal => False
  | _ + 3, _ => False

/-- The renewer depends on the condition at need two, the heir and the mortal formation at
need one. -/
def web : Web Member Unit where
  level t _ := level t
  active := live
  requires _ _ _ := True
  need _ f _ := match f with
    | .renewer => 2
    | .heir => 1
    | .mortal => 1
  draws _ f _ := match f with
    | .renewer => False
    | .heir => True
    | .mortal => True

theorem balances : flow.Balances web
  | 0, () => rfl
  | 1, () => rfl
  | 2, () => rfl
  | _ + 3, () => rfl

theorem dependent : web.Dependent
  | 0, .renewer, _, _, _ => Nat.succ_le_succ (Nat.succ_le_succ (Nat.zero_le 1))
  | 0, .heir, _, _, _ => Nat.succ_le_succ (Nat.zero_le 2)
  | 0, .mortal, _, _, _ => Nat.succ_le_succ (Nat.zero_le 2)
  | 1, .renewer, _, _, _ => Nat.le_refl 2
  | 1, .heir, _, _, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | 1, .mortal, _, _, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | 2, .renewer, dead, _, _ => nomatch dead
  | 2, .heir, _, _, _ => Nat.le_refl 1
  | 2, .mortal, dead, _, _ => nomatch dead
  | _ + 3, _, dead, _, _ => nomatch dead

/-- The horizon of a want: the mortal formation's dependence is met at every step of its
life, and its taking ends the renewal of the condition; the heir, depending on the
condition, ends after the mortal formation has ended. -/
theorem after_its_end :
    flow.Balances web ∧ web.Dependent ∧
      (∀ t, web.active t .mortal → web.Supported t .mortal) ∧
      ¬ web.active 2 .mortal ∧ web.active 2 .heir ∧ ¬ web.active 2 .renewer ∧
      ∀ n f, ¬ web.active (n + 3) f :=
  ⟨balances, dependent, fun t active => dependent t .mortal active,
   fun dead => dead, trivial, fun dead => dead,
   fun _ _ dead => dead⟩

/-- Without the mortal formation the renewer and the heir continue at every step. -/
def without : Flow Member Unit where
  present _ := [.renewer, .heir]
  take _ f _ := match f with
    | .renewer => 0
    | .heir => 1
    | .mortal => 0
  give _ f _ := match f with
    | .renewer => 1
    | .heir => 0
    | .mortal => 0

def kept : Web Member Unit where
  level _ _ := 3
  active _ f := match f with
    | .renewer => True
    | .heir => True
    | .mortal => False
  requires _ _ _ := True
  need _ f _ := match f with
    | .renewer => 2
    | .heir => 1
    | .mortal => 1
  draws _ f _ := match f with
    | .renewer => False
    | .heir => True
    | .mortal => False

theorem without_continues :
    without.Balances kept ∧ kept.Dependent ∧ ∀ t, kept.active t .renewer ∧ kept.active t .heir :=
  ⟨fun _ _ => rfl,
   fun _ f _ _ _ => match f with
    | .renewer => Nat.succ_le_succ (Nat.succ_le_succ (Nat.zero_le 1))
    | .heir => Nat.succ_le_succ (Nat.zero_le 2)
    | .mortal => Nat.succ_le_succ (Nat.zero_le 2),
   fun _ => ⟨trivial, trivial⟩⟩

end Mortal


namespace Totalizer

open Frontier (unburnt burning)

/-- A sun, a keeper and another formation. -/
inductive Formation where
  | sun
  | keeper
  | other

/-- The keeper's supply, the other formation's habitat, and the fuels the sun burns. -/
inductive Place where
  | supply
  | habitat
  | fuel (n : Nat)

/-- The keeper takes one unit of the habitat at each of the first two steps. -/
def clearing : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

def habitatLevel : Nat → Nat
  | 0 => 2
  | 1 => 1
  | _ + 2 => 0

def otherLive : Nat → Prop
  | 0 => True
  | 1 => True
  | _ + 2 => False

/-- The sun burns the `t`th fuel, two units, and gives the supply one; the keeper takes one
unit of the supply at every step and clears the habitat. -/
def flow : Flow Formation Place where
  present _ := [.sun, .keeper, .other]
  take t f c := match f, c with
    | .sun, .fuel n => 2 * burning n t
    | .sun, .supply => 0
    | .sun, .habitat => 0
    | .keeper, .supply => 1
    | .keeper, .habitat => clearing t
    | .keeper, .fuel _ => 0
    | .other, _ => 0
  give _ f c := match f, c with
    | .sun, .supply => 1
    | .sun, .habitat => 0
    | .sun, .fuel _ => 0
    | .keeper, _ => 0
    | .other, _ => 0

/-- The keeper depends on its supply, the other formation on its habitat, each at need
one. -/
def web : Web Formation Place where
  level t c := match c with
    | .supply => 1
    | .habitat => habitatLevel t
    | .fuel n => 2 * unburnt n t
  active t f := match f with
    | .sun => True
    | .keeper => True
    | .other => otherLive t
  requires _ f c := match f, c with
    | .keeper, .supply => True
    | .other, .habitat => True
    | .sun, _ => False
    | .keeper, .habitat => False
    | .keeper, .fuel _ => False
    | .other, .supply => False
    | .other, .fuel _ => False
  need _ _ _ := 1
  draws t f c := match f, c with
    | .sun, .fuel n => n = t
    | .sun, .supply => False
    | .sun, .habitat => False
    | .keeper, .supply => True
    | .keeper, .habitat => True
    | .keeper, .fuel _ => False
    | .other, _ => False

theorem balances : flow.Balances web
  | _, .supply => rfl
  | 0, .habitat => rfl
  | 1, .habitat => rfl
  | _ + 2, .habitat => rfl
  | t, .fuel n => show 2 * unburnt n (t + 1) + (2 * burning n t + 0) = 2 * unburnt n t from
      (Nat.left_distrib 2 _ _).symm.trans (congrArg (2 * ·) (Frontier.burns n t))

theorem dependent : web.Dependent
  | _, .keeper, _, .supply, _ => Nat.le_refl 1
  | 0, .other, _, .habitat, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | 1, .other, _, .habitat, _ => Nat.le_refl 1
  | _ + 2, .other, dead, .habitat, _ => nomatch dead
  | _, .sun, _, _, no => nomatch no
  | _, .keeper, _, .habitat, no => nomatch no
  | _, .keeper, _, .fuel _, no => nomatch no
  | _, .other, _, .supply, no => nomatch no
  | _, .other, _, .fuel _, no => nomatch no

/-- Every family without repetition closed across a step is dissipated on: the sun gives
the supply one unit and burns two; the keeper and the other formation give nothing. -/
theorem dissipative : flow.Dissipative
  | ds, t, distinct, closed, f, mem => match f, mem with
    | .keeper, _ => Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_zero ds)).trans
        (Nat.zero_add _))) (sign_le _)
    | .other, _ => show total ds (fun _ => 0) + sign (total ds (fun _ => 0)) ≤
          total ds (fun _ => 0) from
        Eq.subst (motive := fun x => x + sign x ≤ x) (total_zero ds).symm (Nat.le_refl 0)
    | .sun, mem =>
      have gives : total ds (flow.give t .sun) ≤ 1 :=
        total_le_at (q := flow.give t .sun) (a := .supply) (fun c given => match c, given with
          | .supply, _ => rfl
          | .habitat, given => absurd given (Nat.lt_irrefl 0)
          | .fuel _, given => absurd given (Nat.lt_irrefl 0)) distinct
      have burnt : flow.take t .sun (.fuel t) = 2 :=
        (congrArg (2 * ·) (Frontier.burning_self t)).trans (Nat.mul_one _)
      match Nat.decLe (total ds (flow.give t .sun) + sign (total ds (flow.take t .sun)))
          (total ds (flow.take t .sun)) with
      | isTrue le => le
      | isFalse not => absurd (fun inside : Place.fuel t ∈ ds => not
          (Nat.le_trans (Nat.add_le_add gives (sign_le_one _))
            (Nat.le_trans (Nat.le_of_eq burnt.symm) (le_total_of_mem inside))))
          fun outside => Nat.noConfusion (burnt.symm.trans (closed .sun mem (.fuel t) outside).1)

/-- The supply is fed from beyond at every step: the sun conveys from the step's fuel. -/
theorem fed (t : Nat) : flow.FedFromBeyond [.supply] t :=
  ⟨.fuel t, .supply, (fun mem => match mem with | .tail _ no => nomatch no),
   .head _, .sun, .head _,
   show 0 < 2 * burning t t from
     Eq.subst (motive := fun b => 0 < 2 * b) (Frontier.burning_self t).symm (Nat.succ_pos 1),
   Nat.zero_lt_one⟩

/-- The careful totalizer. The keeper is active and supported at every step; the only
condition it depends on is its supply, which is renewed, fed from beyond and taken from
jointly within what each step gives; in a balanced, dissipative flow. Its clearing of the
habitat undermines at step one, and the other formation, depending on the habitat, is
inactive from step two on. -/
theorem careful :
    flow.Balances web ∧ flow.Dissipative ∧ web.Dependent ∧
      (∀ t c, web.requires t .keeper c → c = .supply) ∧
      (∀ t, web.active t .keeper ∧ web.Supported t .keeper) ∧
      web.Renewed .supply ∧ (∀ t, flow.FedFromBeyond [.supply] t) ∧
      (∀ t, flow.WithinJoint t .supply) ∧
      web.UnderminingAt 1 .keeper ∧ ∀ n, ¬ web.active (n + 2) .other :=
  ⟨balances, dissipative, dependent,
   fun _ c depends => match c, depends with | .supply, _ => rfl,
   fun t => ⟨trivial, dependent t .keeper trivial⟩,
   fun _ g depends => match g, depends with | .keeper, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩,
   fed, fun _ => Nat.le_refl 1,
   ⟨.habitat, trivial, .other, trivial,
    Web.MetAbove.now (W := web) (t := 1) (g := Formation.other) (c := Place.habitat)
      trivial (Nat.le_refl 1) Nat.zero_lt_one,
    Nat.zero_lt_one⟩,
   fun _ dead => dead⟩

end Totalizer

end Becoming
