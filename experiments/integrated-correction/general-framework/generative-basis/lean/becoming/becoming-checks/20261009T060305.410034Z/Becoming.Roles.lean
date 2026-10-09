import Becoming.Flow

/-!
# Roles: formations and conditions are roles of one relatum

`Web` and `Flow` relate formations to conditions of another type. The split is a
reading, not two kinds of being: a formation can be a condition of others and of itself,
as parents are of their young, a forest of its understory and a flower of the bee. Read
with two kinds, that is representable only through a proxy condition, and nothing ties a
formation's activity to its standing as a condition. This module reads one kind of
relatum in both roles.

Results:
* The two-kind reading is the one-kind reading in which no formation is a condition
  (`Web.roles`, `Flow.roles`). Read so, a web keeps support, `Dependent`, renewal,
  consumption, the classes of formations, undermining, the living events of the
  stepwise reading, arising and unceasing generation. A flow keeps what is taken and
  given, balance, the takers and renewers of a family, and more without end. In this
  reading no active formation is embodied or bears on itself (`roles_not_embodied`,
  `roles_not_selfBearing`).
* A relatum is *embodied* when it stands as a condition exactly while it is active
  (`Embodied`). It *bears on itself* when, while active, it depends on its own standing
  at a positive need (`SelfBearing`); under `Dependent` it then stands while active
  (`SelfBearing.stands`).
* Life as a condition of life. Under `Dependent`, a formation depending on an embodied
  relatum at a positive need is active only while that relatum is
  (`Embodied.active_of_bearing`). Activity passes along every chain of such dependence
  (`active_along`), so a relatum that is not active ends every formation whose chain
  reaches it (`coextinct`). Consuming an embodied relatum at a need of one ends it
  (`Embodied.ends_when_consumed`). Drawing on an embodied relatum that bears on itself,
  across the step at which it ends, breaks its own dependence whether or not any other
  formation depends on it, so the drawing event is not living
  (`Embodied.ending_breaks`).
* Life from life. In a balanced flow in which only active formations give, an embodied
  relatum arises only as another active formation gives to it
  (`Embodied.arises_given`).
* Witnesses. A bee and a flower, each depending on itself and on the other and drawing
  on the other, renew each other with no third condition, and every event is living
  (`Mutualism`); in `Mutualism.apart` each depends only on the other, and neither bears
  on itself. A fox depending on the hare it eats ends with it, and its eating breaks the
  hare's own dependence (`Predation`). Generation after generation arises, each given by
  the one before, with nothing else (`Brood`).

`Becoming.Correspondence` reads the relations: the one-kind reading keeps the connection
of the valuations, and formations bearing on themselves relate directly.

Which relata are embodied, and whether a formation bears on itself, are
representational choices: remains stand after activity ends, and a condition such as
water stands without being active. `ending_breaks` makes ending another life by drawing
on it count against living when that life bears on itself; whether it should belongs to
the reading of 生生, which is Ren's. Giving costs nothing here; under the dissipation of
`Becoming.Dissipation` it would need taking. No ethical predicate, ranking or axiom
occurs.
-/

open Generative

namespace Becoming

variable {F C X : Type}

/-- A total over a mapped list is the total of the composed quantity. -/
theorem total_map {α β : Type} (g : α → β) (q : β → Nat) :
    ∀ as : List α, total (as.map g) q = total as fun a => q (g a)
  | [] => rfl
  | a :: as => congrArg (q (g a) + ·) (total_map g q as)

/-- Quantities that agree everywhere have the same total. -/
theorem total_congr {α : Type} {p q : α → Nat} (same : ∀ a, p a = q a) :
    ∀ as : List α, total as p = total as q
  | [] => rfl
  | a :: as => (congrArg (· + total as p) (same a)).trans (congrArg (q a + ·) (total_congr same as))

/-! ## One kind of relatum in two roles -/

namespace Web

/-- The web read with one kind of relatum. Each formation and each condition of `W` is a
relatum: a formation stands at level zero as a condition, and nothing depends on it or
draws on it; a condition is never active, and depends on and draws on nothing. -/
def roles (W : Web F C) : Web (F ⊕ C) (F ⊕ C) where
  level t x := match x with
    | .inl _ => 0
    | .inr c => W.level t c
  active t x := match x with
    | .inl f => W.active t f
    | .inr _ => False
  requires t x y := match x, y with
    | .inl f, .inr c => W.requires t f c
    | .inl _, .inl _ => False
    | .inr _, _ => False
  need t x y := match x, y with
    | .inl f, .inr c => W.need t f c
    | .inl _, .inl _ => 0
    | .inr _, _ => 0
  draws t x y := match x, y with
    | .inl f, .inr c => W.draws t f c
    | .inl _, .inl _ => False
    | .inr _, _ => False

variable (W : Web F C)

theorem roles_supported (t : Nat) (f : F) : W.roles.Supported t (.inl f) ↔ W.Supported t f :=
  ⟨fun supported c => supported (.inr c),
   fun supported y => match y with
    | .inl _ => False.elim
    | .inr c => supported c⟩

theorem roles_dependent : W.roles.Dependent ↔ W.Dependent :=
  ⟨fun dependent t f active => (W.roles_supported t f).mp (dependent t (.inl f) active),
   fun dependent t x => match x with
    | .inl f => fun active => (W.roles_supported t f).mpr (dependent t f active)
    | .inr _ => False.elim⟩

theorem roles_renewed (c : C) : W.roles.Renewed (.inr c) ↔ W.Renewed c :=
  ⟨fun renewed t g => renewed t (.inl g),
   fun renewed t x => match x with
    | .inl g => renewed t g
    | .inr _ => False.elim⟩

/-- Nothing depends on a formation as a condition, so it is renewed. -/
theorem roles_renewed_formation (f : F) : W.roles.Renewed (.inl f) :=
  fun _ x => match x with
    | .inl _ => False.elim
    | .inr _ => False.elim

theorem roles_consumed (c : C) : W.roles.Consumed (.inr c) ↔ W.Consumed c :=
  ⟨fun | ⟨.inl g, T, depends, below⟩ => ⟨g, T, depends, below⟩
       | ⟨.inr _, _, no, _⟩ => False.elim no,
   fun ⟨g, T, depends, below⟩ => ⟨.inl g, T, depends, below⟩⟩

theorem roles_renewingIn (f : F) : W.roles.RenewingIn (.inl f) ↔ W.RenewingIn f :=
  ⟨fun renewing t c joins => (W.roles_renewed c).mp (renewing t (.inr c) joins),
   fun renewing t y => match y with
    | .inl g => fun _ => W.roles_renewed_formation g
    | .inr c => fun joins => (W.roles_renewed c).mpr (renewing t c joins)⟩

theorem roles_consumingIn (f : F) : W.roles.ConsumingIn (.inl f) ↔ W.ConsumingIn f :=
  ⟨fun | ⟨t, .inr c, drawn, consumed⟩ => ⟨t, c, drawn, (W.roles_consumed c).mp consumed⟩
       | ⟨_, .inl _, no, _⟩ => False.elim no,
   fun ⟨t, c, drawn, consumed⟩ => ⟨t, .inr c, drawn, (W.roles_consumed c).mpr consumed⟩⟩

theorem roles_undermining (t : Nat) (f : F) :
    W.roles.UnderminingAt t (.inl f) ↔ W.UnderminingAt t f :=
  ⟨fun | ⟨.inr c, drawn, .inl g, depends, met, fell⟩ => ⟨c, drawn, g, depends, met, fell⟩
       | ⟨.inr _, _, .inr _, no, _⟩ => False.elim no
       | ⟨.inl _, no, _⟩ => False.elim no,
   fun ⟨c, drawn, g, depends, met, fell⟩ => ⟨.inr c, drawn, .inl g, depends, met, fell⟩⟩

theorem roles_arises (t : Nat) (f : F) : W.roles.Arises t (.inl f) ↔ W.Arises t f :=
  Iff.rfl

theorem roles_unceasing : W.roles.Unceasing ↔ W.Unceasing :=
  ⟨fun unceasing N => match unceasing N with
    | ⟨t, .inl f, le, arises⟩ => ⟨t, f, le, arises⟩
    | ⟨_, .inr _, _, _, active⟩ => False.elim active,
   fun unceasing N => match unceasing N with
    | ⟨t, f, le, arises⟩ => ⟨t, .inl f, le, arises⟩⟩

/-- A formation's event is living in the one-kind reading exactly when it is living. -/
theorem roles_alive (t : Nat) (f : F) :
    (W.roles.active t (.inl f) ∧ ¬ W.roles.UnderminingAt t (.inl f)) ↔
      (W.active t f ∧ ¬ W.UnderminingAt t f) :=
  ⟨fun ⟨active, sound⟩ => ⟨active, fun undermining =>
      sound ((W.roles_undermining t f).mpr undermining)⟩,
   fun ⟨active, sound⟩ => ⟨active, fun undermining =>
      sound ((W.roles_undermining t f).mp undermining)⟩⟩

/-- Formation events are one to one with their events in the one-kind reading. -/
theorem roles_event_injective :
    ∀ e e' : F × Nat, ((.inl e.1, e.2) : (F ⊕ C) × Nat) = (.inl e'.1, e'.2) → e = e'
  | (_, _), (_, _), rfl => rfl

/-- Every living event of the one-kind reading is a formation's. -/
theorem roles_event_onto (e : (F ⊕ C) × Nat) (active : W.roles.active e.2 e.1) :
    ∃ e' : F × Nat, ((.inl e'.1, e'.2) : (F ⊕ C) × Nat) = e :=
  match e, active with
  | (.inl f, t), _ => ⟨(f, t), rfl⟩

end Web

namespace Flow

/-- The flow read with one kind of relatum: formations take from and give to conditions,
and nothing takes from or gives to a formation. -/
def roles (L : Flow F C) : Flow (F ⊕ C) (F ⊕ C) where
  present t := (L.present t).map .inl
  take t x y := match x, y with
    | .inl f, .inr c => L.take t f c
    | .inl _, .inl _ => 0
    | .inr _, _ => 0
  give t x y := match x, y with
    | .inl f, .inr c => L.give t f c
    | .inl _, .inl _ => 0
    | .inr _, _ => 0

variable (L : Flow F C)

theorem roles_taken (t : Nat) (c : C) : L.roles.taken t (.inr c) = L.taken t c :=
  total_map _ _ (L.present t)

theorem roles_given (t : Nat) (c : C) : L.roles.given t (.inr c) = L.given t c :=
  total_map _ _ (L.present t)

theorem roles_taken_formation (t : Nat) (f : F) : L.roles.taken t (.inl f) = 0 :=
  (total_map _ _ (L.present t)).trans (total_zero (L.present t))

theorem roles_given_formation (t : Nat) (f : F) : L.roles.given t (.inl f) = 0 :=
  (total_map _ _ (L.present t)).trans (total_zero (L.present t))

theorem roles_balances {W : Web F C} : L.roles.Balances W.roles ↔ L.Balances W :=
  ⟨fun balances t c => (congrArg (W.level (t + 1) c + ·) (L.roles_taken t c)).symm.trans
      ((balances t (.inr c)).trans (congrArg (W.level t c + ·) (L.roles_given t c))),
   fun balances t x => match x with
    | .inl f => (congrArg (0 + ·) (L.roles_taken_formation t f)).trans
        (congrArg (0 + ·) (L.roles_given_formation t f)).symm
    | .inr c => (congrArg (W.level (t + 1) c + ·) (L.roles_taken t c)).trans
        ((balances t c).trans (congrArg (W.level t c + ·) (L.roles_given t c)).symm)⟩

theorem roles_takers (cs : List C) (t : Nat) :
    L.roles.takers (cs.map .inr) t = L.takers cs t :=
  (total_map _ _ (L.present t)).trans
    (total_congr (fun _ => congrArg sign (total_map _ _ cs)) (L.present t))

theorem roles_renewers (cs : List C) (t : Nat) :
    L.roles.renewers (cs.map .inr) t = L.renewers cs t :=
  (total_map _ _ (L.present t)).trans
    (total_congr (fun _ => congrArg sign (total_map _ _ cs)) (L.present t))

theorem roles_more (cs : List C) : L.roles.More (cs.map .inr) ↔ L.More cs :=
  ⟨fun more K => match more K with
    | ⟨T, many⟩ => ⟨T, fun t later =>
        Nat.le_trans (many t later) (Nat.le_of_eq (L.roles_takers cs t))⟩,
   fun more K => match more K with
    | ⟨T, many⟩ => ⟨T, fun t later =>
        Nat.le_trans (many t later) (Nat.le_of_eq (L.roles_takers cs t).symm)⟩⟩

end Flow

/-! ## Life as a condition of life -/

namespace Web

variable (W : Web X X)

/-- A relatum is *embodied* when it stands as a condition exactly while it is active:
what it is to the others is its own activity. -/
def Embodied (x : X) : Prop :=
  ∀ t, W.active t x ↔ 0 < W.level t x

/-- A relatum *bears on itself* when, while it is active, it depends on its own standing
as a condition at a positive need. -/
def SelfBearing (x : X) : Prop :=
  ∀ t, W.active t x → W.requires t x x ∧ 0 < W.need t x x

/-- Dependence at a positive need on embodied relata at a step, as a process on
relata. -/
def bearing (t : Nat) : Process X Unit :=
  ⟨fun g _ y => (W.requires t g y ∧ 0 < W.need t g y) ∧ W.Embodied y⟩

variable {W}

/-- Under `Dependent`, a relatum bearing on itself stands as a condition while it is
active. -/
theorem SelfBearing.stands (dependent : W.Dependent) {x : X} (self : W.SelfBearing x)
    {t : Nat} (active : W.active t x) : 0 < W.level t x :=
  Nat.lt_of_lt_of_le (self t active).2 (dependent t x active x (self t active).1)

/-- Life as a condition of life: under `Dependent`, a formation that depends on an
embodied relatum at a positive need is active only while that relatum is. -/
theorem Embodied.active_of_bearing (dependent : W.Dependent) {y : X}
    (embodied : W.Embodied y) {t : Nat} {g : X} (active : W.active t g)
    (bearing : W.requires t g y ∧ 0 < W.need t g y) : W.active t y :=
  (embodied t).mpr (Nat.lt_of_lt_of_le bearing.2 (dependent t g active y bearing.1))

/-- Under `Dependent`, activity at a step passes along every chain of dependence on
embodied relata. -/
theorem active_along (dependent : W.Dependent) (t : Nat) :
    Invariant (W.bearing t) (W.active t) :=
  fun _ _ _ ⟨bearing, embodied⟩ active => embodied.active_of_bearing dependent active bearing

/-- Coextinction: under `Dependent`, a relatum that is not active at a step ends there
every formation whose chain of dependence on embodied relata reaches it. -/
theorem coextinct (dependent : W.Dependent) {t : Nat} {g y : X}
    (chain : Reach (W.bearing t) g y) (ended : ¬ W.active t y) : ¬ W.active t g :=
  fun active => ended ((active_along dependent t).reach chain active)

/-- Consuming an embodied relatum at a need of one ends it: after the dependence is no
longer met, the relatum is not active. -/
theorem Embodied.ends_when_consumed {y : X} (embodied : W.Embodied y) {T : Nat} {g : X}
    (least : W.need T g y ≤ 1) (below : ∀ t, T < t → W.level t y < W.need T g y) :
    ∀ t, T < t → ¬ W.active t y :=
  fun t later active =>
    Nat.not_le_of_gt (below t later) (Nat.le_trans least ((embodied t).mp active))

/-- Under `Dependent`, drawing on an embodied relatum that bears on itself, across the
step at which it ends, breaks its own dependence; no other formation need depend on it. -/
theorem Embodied.ending_breaks (dependent : W.Dependent) {x : X} (embodied : W.Embodied x)
    (self : W.SelfBearing x) {t : Nat} (active : W.active t x) (ends : ¬ W.active (t + 1) x)
    {f : X} (drawn : W.draws t f x) : W.BreakingOn t f x :=
  ⟨drawn, x, (self t active).1, dependent t x active x (self t active).1,
    Nat.lt_of_le_of_lt (Nat.ge_of_not_lt fun stands => ends ((embodied (t + 1)).mpr stands))
      (self t active).2⟩

/-- Life from life: in a balanced flow in which only active formations give, an embodied
relatum arises only as an active formation taking part gives to it, and that formation is
another. -/
theorem Embodied.arises_given {L : Flow X X} (balances : L.Balances W) (acting : L.Acting W)
    {x : X} (embodied : W.Embodied x) {t : Nat} (arises : W.Arises t x) :
    ∃ f, W.active t f ∧ f ∈ L.present t ∧ 0 < L.give t f x ∧ f ≠ x :=
  match balances.renewedBy acting t x (Nat.lt_of_le_of_lt
      (Nat.ge_of_not_lt fun stands => arises.1 ((embodied t).mpr stands))
      ((embodied (t + 1)).mp arises.2)) with
  | ⟨f, active, present, gives⟩ => ⟨f, active, present, gives, fun same => arises.1 (same ▸ active)⟩

variable (W : Web F C)

/-- Read with one kind of relatum, a formation active at some step is not embodied. -/
theorem roles_not_embodied {t : Nat} {f : F} (active : W.active t f) :
    ¬ W.roles.Embodied (.inl f) :=
  fun embodied => Nat.lt_irrefl 0 ((embodied t).mp active)

/-- Read with one kind of relatum, a formation active at some step does not bear on
itself. -/
theorem roles_not_selfBearing {t : Nat} {f : F} (active : W.active t f) :
    ¬ W.roles.SelfBearing (.inl f) :=
  fun self => (self t active).1

end Web

/-! ## Witnesses -/

namespace Mutualism

inductive Relatum where
  | bee
  | flower

/-- The other of the two. -/
def other : Relatum → Relatum
  | .bee => .flower
  | .flower => .bee

theorem other_cancel : ∀ {x y : Relatum}, other x = other y → x = y
  | .bee, .bee, _ => rfl
  | .flower, .flower, _ => rfl
  | .bee, .flower, same => Relatum.noConfusion same
  | .flower, .bee, same => Relatum.noConfusion same

theorem other_ne : ∀ x : Relatum, x ≠ other x
  | .bee => Relatum.noConfusion
  | .flower => Relatum.noConfusion

/-- Each depends on itself and on the other at need one, and draws on the other. Both
stand at level one and are active throughout. -/
def web : Web Relatum Relatum where
  level _ _ := 1
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ x y := y = other x

/-- The same, except that each depends only on the other. -/
def apart : Web Relatum Relatum where
  level _ _ := 1
  active _ _ := True
  requires _ x y := y = other x
  need _ _ _ := 1
  draws _ x y := y = other x

theorem dependent : web.Dependent :=
  fun _ _ _ _ _ => Nat.le_refl 1

theorem embodied (x : Relatum) : web.Embodied x :=
  fun _ => ⟨fun _ => Nat.zero_lt_one, fun _ => trivial⟩

theorem selfBearing (x : Relatum) : web.SelfBearing x :=
  fun _ _ => ⟨trivial, Nat.zero_lt_one⟩

theorem renewing (x : Relatum) : web.RenewingIn x :=
  fun _ _ _ _ _ _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩

theorem apart_renewing (x : Relatum) : apart.RenewingIn x :=
  fun _ _ _ _ _ _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩

/-- Every event of the bee and the flower is living. -/
theorem alive (e : Relatum × Nat) : web.active e.2 e.1 ∧ ¬ web.UnderminingAt e.2 e.1 :=
  ⟨trivial, (Web.renewing_at_active (renewing e.1) trivial).not_undermining⟩

theorem apart_alive (e : Relatum × Nat) : apart.active e.2 e.1 ∧ ¬ apart.UnderminingAt e.2 e.1 :=
  ⟨trivial, (Web.renewing_at_active (apart_renewing e.1) trivial).not_undermining⟩

/-- Where each depends only on the other, neither bears on itself. -/
theorem apart_not_selfBearing (x : Relatum) : ¬ apart.SelfBearing x :=
  fun self => other_ne x (self 0 trivial).1

end Mutualism

namespace Predation

inductive Relatum where
  | fox
  | hare

/-- One until the hare is eaten, across the step from two; zero after. -/
def uneaten : Nat → Nat
  | 0 | 1 | 2 => 1
  | _ + 3 => 0

/-- Each depends on itself, and the fox on the hare, at need one; the fox draws on the
hare. Both stand and are active while the hare lives: it is eaten across the step from
two. -/
def web : Web Relatum Relatum where
  level t _ := uneaten t
  active t _ := 0 < uneaten t
  requires _ x y := y = x ∨ y = .hare
  need _ _ _ := 1
  draws _ x y := x = .fox ∧ y = .hare

theorem uneaten_late : ∀ t, 2 < t → uneaten t = 0
  | 0, later => absurd later (Nat.not_lt_zero 2)
  | 1, later => absurd (Nat.le_of_succ_le_succ later) (Nat.not_succ_le_zero 1)
  | 2, later => absurd later (Nat.lt_irrefl 2)
  | _ + 3, _ => rfl

theorem embodied (x : Relatum) : web.Embodied x :=
  fun _ => Iff.rfl

theorem selfBearing (x : Relatum) : web.SelfBearing x :=
  fun _ _ => ⟨.inl rfl, Nat.zero_lt_one⟩

theorem dependent : web.Dependent :=
  fun _ _ active _ _ => active

theorem hare_ends : ∀ t, 2 < t → ¬ web.active t .hare :=
  fun t later active =>
    Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le active (Nat.le_of_eq (uneaten_late t later)))

/-- The fox's eating breaks the hare's own dependence, so it is not living. -/
theorem breaking : web.BreakingOn 2 .fox .hare :=
  (embodied .hare).ending_breaks (t := 2) dependent (selfBearing .hare) Nat.zero_lt_one
    (hare_ends 3 (Nat.lt_succ_self 2)) ⟨rfl, rfl⟩

/-- The fox depends on the hare, so it ends with it. -/
theorem fox_ends : ∀ t, 2 < t → ¬ web.active t .fox :=
  fun t later => Web.coextinct dependent
    (Reach.of_step (a := ()) ⟨⟨.inr rfl, Nat.zero_lt_one⟩, embodied .hare⟩) (hare_ends t later)

end Predation

namespace Brood

/-- One from step `x` on: generation `x` stands from the step after it is given. -/
def standing : Nat → Nat → Nat
  | 0, _ => 1
  | _ + 1, 0 => 0
  | x + 1, t + 1 => standing x t

/-- One for zero, zero otherwise. -/
def first : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- One at the step at which generation `x` is given: the step before it stands. -/
def birth : Nat → Nat → Nat
  | 0, _ => 0
  | x + 1, 0 => first x
  | x + 1, t + 1 => birth x t

theorem grows : ∀ x t, standing x (t + 1) = standing x t + birth x t
  | 0, _ => rfl
  | 1, 0 => rfl
  | _ + 2, 0 => rfl
  | x + 1, t + 1 => grows x t

theorem standing_self : ∀ t, standing t t = 1
  | 0 => rfl
  | t + 1 => standing_self t

theorem standing_before : ∀ t, standing (t + 1) t = 0
  | 0 => rfl
  | t + 1 => standing_before t

/-- Across the step from `t`, generation `t` gives one unit to generation `t + 1`, and
nothing is taken. -/
def flow : Flow Nat Nat where
  present t := [t]
  take _ _ _ := 0
  give t _ x := birth x t

/-- Each generation is active while it stands, and depends on itself at need one. -/
def web : Web Nat Nat where
  level t x := standing x t
  active t x := 0 < standing x t
  requires t x y := y = x ∧ 0 < standing x t
  need _ _ _ := 1
  draws _ _ _ := False

theorem arises (t : Nat) : web.Arises t (t + 1) :=
  ⟨fun stands => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le stands (Nat.le_of_eq (standing_before t))),
   Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (standing_self (t + 1)).symm)⟩

/-- Generation after generation arises, each given by the one before: the flow balances,
only active generations give, each is embodied and bears on itself, activity needs
support, and generation is unceasing. -/
theorem brood : flow.Balances web ∧ flow.Acting web ∧ web.Dependent ∧
    (∀ x, web.Embodied x ∧ web.SelfBearing x) ∧ web.Unceasing :=
  ⟨fun t x => grows x t,
   fun t _ _ present _ => match present with
    | .head _ => Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (standing_self _).symm)
    | .tail _ no => (nomatch no),
   fun _ _ _ c depends => match c, depends with
    | _, ⟨rfl, stands⟩ => stands,
   fun _ => ⟨fun _ => Iff.rfl, fun _ active => ⟨⟨rfl, active⟩, Nat.zero_lt_one⟩⟩,
   fun N => ⟨N, N + 1, Nat.le_refl N, arises N⟩⟩

end Brood

end Becoming
