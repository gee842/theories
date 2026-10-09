import Becoming.Evolution
import Becoming.Reserve

/-!
# Space: the whole and its parts

Ren proposed that counting all the space, generative and degenerative, gives the theory of
becoming. This module states one structure for that proposal (an AI reading). The space is
every world. The laws stated with no premise hold of each world. The premises of the other
theorems are met by some worlds and not by others, so they carve out parts.

Which parts Ren's "generative" and "degenerative" name is Ren's to choose. Ren said that,
though both are in one becoming model, they do not overlap. The spine offers two readings.
Read as relations, a formation renewing what it takes part in and one consuming what it
draws on (`Web.RenewingIn`, `Web.ConsumingIn`) never coincide
(`Web.renewing_not_consuming`), though one occurrence can take part in both. Read as
activity, arising recurring and ceasing recurring (`World.ArisingRecurs`,
`World.CeasingRecurs`) coincide in finite worlds. This module states the second, under
names that describe activity and do not claim Ren's words.

* **The space.** A world is its relata, read with one kind of relatum (`Becoming.Roles`),
  with the flow among them and their web (`World`). The two-kind reading of any flow and
  web is a world, and arising and ceasing read the same there (`World.ofRoles`,
  `World.arisingRecurs_ofRoles`, `World.ceasingRecurs_ofRoles`).
* **Laws of the whole.** The laws of `Becoming.Change`, and the accounting identity of
  `Becoming.Evolution`, are stated of every web and every amount with no premise about
  the unfolding, so they hold throughout the space. Read of worlds: in a finite world
  whose activity is decided, arising recurs exactly when ceasing does
  (`World.arising_iff_ceasing`). Decidability is part of the representation: over every
  world without it, this law is excluded middle (`World.law_decides`).
* **Finiteness separates them.** Where the relata are infinitely many, either can recur
  without the other (`World.separate`, from `Dawn` and `Dusk`); that these worlds are
  infinite follows from the law.
* **Premises carve parts.** Activity needing support, balance, only active formations
  giving, only active formations taking and only what they draw on, dissipation,
  embodiment and a reserve carrying activity are each met by some worlds and not by others
  (`World.contingent`). They are premises, not laws.
* **Living crosses arising.** Among finite worlds, arising recurring or not occurs both
  with every event living and with some event not living (`World.living_crosses`): two
  sides handing one standing back and forth, the same with a grazer drawing down a pool
  another relatum depends on, mutualists active throughout, and a parent drawing a pool
  down. Whether events are living is not decided by arising and ceasing. The sides
  drawing each on its own standing (`spending`) also has an event that is not living, but
  only on the stepwise verdict about drawing on a self-bearing relatum at its ending,
  which is Ren's to choose.
* **Dissipation brings a finite world to rest.** In a finite, balanced, dissipative world
  whose activity is decided and in which whatever arises is embodied, neither arising nor
  ceasing recurs (`World.rests`). Each premise is needed (`World.rests_needs`): a world
  burning fresh fuel keeps arising with infinitely many relata, two sides handing a
  standing back and forth keep arising without dissipation, the same sides taking their
  own unit and giving nothing keep arising without balance, with a closed family taken
  from at every step, and a relatum whose activity is not its standing keeps arising
  without embodiment. That last world takes part in no exchange from some step on; in a
  finite, balanced, dissipative world taking does not recur, so any such witness does.

Arising recurring, ceasing recurring and living name parts of the space, and none of
them is evaluated here. `Living` is the structural condition that every event is living
in the stepwise reading (`Web.valuation` in `Becoming.Metaethics`). The module does not
show that the theory needs no axiom: it shows which statements need no premise and which
premises carve which parts. No ethical predicate, ranking or axiom occurs.
-/
namespace Becoming

/-- Nothing takes part. -/
def Flow.still {F C : Type} : Flow F C :=
  ⟨fun _ => [], fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- Where nothing takes part, dissipation holds vacuously. -/
theorem Flow.still_dissipative {F C : Type} : (Flow.still : Flow F C).Dissipative :=
  fun _ _ _ _ _ present => nomatch present

/-! ## The space and its parts -/

/-- A world: its relata, read with one kind of relatum, with the flow among them and their
web. -/
structure World where
  Relatum : Type
  flow : Flow Relatum Relatum
  web : Web Relatum Relatum

namespace World

variable (w : World)

/-- Finitely many relata are all there is, each listed once. -/
def Finite : Prop :=
  ∃ all : List w.Relatum, Distinct all ∧ ∀ x, x ∈ all

/-- Arising recurs: some relatum arises at arbitrarily late steps. -/
def ArisingRecurs : Prop :=
  w.web.Unceasing

/-- Ceasing recurs: some relatum ceases at arbitrarily late steps. -/
def CeasingRecurs : Prop :=
  ∀ N, ∃ t x, N ≤ t ∧ w.web.Ceases t x

/-- Every event is living in the stepwise reading: no active relatum undermines. -/
def Living : Prop :=
  ∀ t x, w.web.active t x → ¬ w.web.UnderminingAt t x

/-- Activity needs support. -/
def Dependent : Prop :=
  w.web.Dependent

/-- The flow balances. -/
def Balanced : Prop :=
  w.flow.Balances w.web

/-- Only active relata give. -/
def Acting : Prop :=
  w.flow.Acting w.web

/-- Only active relata take, and only from what they draw on. -/
def Taking : Prop :=
  w.flow.Taking w.web

/-- The flow dissipates. -/
def Dissipative : Prop :=
  w.flow.Dissipative

/-- Every relatum stands as a condition exactly while it is active. -/
def Embodied : Prop :=
  ∀ x, w.web.Embodied x

/-- Whatever arises is embodied. -/
def ArisingEmbodied : Prop :=
  ∀ t x, w.web.Arises t x → w.web.Embodied x

/-- Some reserve carries activity beyond support (`Becoming.Reserve`). -/
def Carried : Prop :=
  ∃ r, w.web.Carries r

variable {w}

theorem Embodied.arising (embodied : w.Embodied) : w.ArisingEmbodied :=
  fun _ x _ => embodied x

/-- The two-kind reading of a flow and a web, as a world. -/
def ofRoles {F C : Type} (L : Flow F C) (W : Web F C) : World :=
  ⟨F ⊕ C, L.roles, W.roles⟩

theorem arisingRecurs_ofRoles {F C : Type} (L : Flow F C) (W : Web F C) :
    (ofRoles L W).ArisingRecurs ↔ W.Unceasing :=
  W.roles_unceasing

theorem ceasingRecurs_ofRoles {F C : Type} (L : Flow F C) (W : Web F C) :
    (ofRoles L W).CeasingRecurs ↔ ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f :=
  ⟨fun ceasing N => match ceasing N with
    | ⟨t, .inl f, later, ceases⟩ => ⟨t, f, later, ceases⟩
    | ⟨_, .inr _, _, ceases⟩ => False.elim ceases.1,
   fun ceasing N => match ceasing N with
    | ⟨t, f, later, ceases⟩ => ⟨t, .inl f, later, ceases⟩⟩

/-! ## Laws of the whole -/

/-- In a finite world whose activity is decided, arising recurs exactly when ceasing does.
Decidability is part of the representation: without it the law is excluded middle
(`law_decides`). -/
theorem arising_iff_ceasing [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite) :
    w.ArisingRecurs ↔ w.CeasingRecurs :=
  match finite with
  | ⟨_, _, every⟩ => w.web.unceasing_iff every

/-- Dissipation brings a finite world to rest: where activity is decided, the flow balances
and dissipates and whatever arises is embodied, neither arising nor ceasing recurs. -/
theorem rests [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match finite with
  | ⟨_, distinct, every⟩ =>
    have quiet : ¬ w.ArisingRecurs := fun arising =>
      Web.generation_ceases balanced dissipative distinct every fun N =>
        match arising N with
        | ⟨t, x, later, arises⟩ => ⟨t, x, later, embodied t x arises, arises⟩
    ⟨quiet, fun ceasing => quiet ((arising_iff_ceasing finite).mpr ceasing)⟩

/-! ## Worlds -/

/-- Two sides hand one standing back and forth (`Handing`). -/
def handing : World :=
  ⟨Bool, Handing.flow, Handing.web⟩

instance handing_decided : ∀ t x, Decidable (handing.web.active t x) :=
  fun t x => Nat.decLt 0 (Handing.stands x t)

theorem handing_finite : handing.Finite :=
  ⟨[true, false], Handing.distinct, Handing.every⟩

theorem handing_arising : handing.ArisingRecurs :=
  fun N => match Handing.recurs true N with
  | ⟨t, later, arises⟩ => ⟨t, true, later, arises⟩

/-- Two sides hand one standing back and forth: a finite world in which arising and ceasing
recur and every event is living. Activity needs support, the flow balances,
only active sides give, and every side is embodied, so the zero reserve carries it; the
sides take without drawing, and the flow does not dissipate. -/
theorem handing_world :
    handing.Finite ∧ handing.ArisingRecurs ∧ handing.CeasingRecurs ∧ handing.Living ∧
    handing.Dependent ∧ handing.Balanced ∧ handing.Acting ∧ ¬ handing.Taking ∧
    ¬ handing.Dissipative ∧ handing.Embodied ∧ handing.Carried :=
  ⟨handing_finite, handing_arising, (arising_iff_ceasing handing_finite).mp handing_arising,
   fun _ _ _ ⟨_, draws, _⟩ => draws, Handing.dependent, Handing.balances, Handing.acting,
   fun taking => (taking 0 true true (.head _) Nat.zero_lt_one).2,
   Handing.handing.2.2.2.2.2.2, fun x => (Handing.embodied x).1,
   ⟨fun _ _ => 0, Web.carries_zero.mpr Handing.dependent⟩⟩

namespace Spending

/-- As in `Handing`, except that each side draws on its own standing while it stands. -/
def web : Web Bool Bool where
  level t x := Handing.stands x t
  active t x := 0 < Handing.stands x t
  requires _ x y := y = x
  need _ _ _ := 1
  draws t x y := y = x ∧ 0 < Handing.stands x t

/-- A side takes only from itself. -/
theorem self_taken {t : Nat} : ∀ {x y : Bool}, 0 < Handing.flow.take t x y → y = x
  | true, true, _ => rfl
  | false, false, _ => rfl
  | true, false, takes => absurd takes (Nat.lt_irrefl 0)
  | false, true, takes => absurd takes (Nat.lt_irrefl 0)

theorem taking : Handing.flow.Taking web :=
  fun t f c present takes => match f, (present : f ∈ [Handing.holder t]), takes with
  | _, .head _, takes => match c, self_taken takes with
    | _, rfl => ⟨Handing.holder_stands t, rfl, Handing.holder_stands t⟩
  | _, .tail _ no, _ => nomatch no

/-- The side holding the standing at the first step draws on itself as it hands its
standing on: the step leaves its own dependence unmet. -/
theorem spends : web.active 0 true ∧ web.UnderminingAt 0 true :=
  ⟨Nat.zero_lt_one, true, ⟨rfl, Nat.zero_lt_one⟩, true, rfl,
   ⟨0, Nat.le_refl 0, fun _ _ _ => rfl, Nat.le_refl 1, Nat.zero_lt_one⟩, Nat.zero_lt_one⟩

end Spending

/-- The sides of `Handing`, each drawing on its own standing while it stands. -/
def spending : World :=
  ⟨Bool, Handing.flow, Spending.web⟩

instance spending_decided : ∀ t x, Decidable (spending.web.active t x) :=
  fun t x => Nat.decLt 0 (Handing.stands x t)

theorem spending_finite : spending.Finite :=
  ⟨[true, false], Handing.distinct, Handing.every⟩

/-- The same activity as `handing`, so arising and ceasing recur, while not every event is
living in the stepwise reading: the holder draws on its own standing as it hands it on,
the undermining of `Embodied.ending_breaks`. Whether such drawing at an ending counts as
not living is Ren's to choose. The flow balances, only active sides give and take, and
they take only from what they draw on. -/
theorem spending_world :
    spending.Finite ∧ spending.ArisingRecurs ∧ spending.CeasingRecurs ∧ ¬ spending.Living ∧
    spending.Dependent ∧ spending.Balanced ∧ spending.Acting ∧ spending.Taking ∧
    spending.Embodied :=
  have arising : spending.ArisingRecurs := fun N => match Handing.recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, true, later, arises⟩
  ⟨spending_finite, arising, (arising_iff_ceasing spending_finite).mp arising,
   fun living => living 0 true Spending.spends.1 Spending.spends.2,
   Handing.dependent, Handing.balances, Handing.acting, Spending.taking,
   fun x => (Handing.embodied x).1⟩

/-- Mutualists active throughout (`Mutualism`), with no flow. -/
def mutualism : World :=
  ⟨Mutualism.Relatum, Flow.still, Mutualism.web⟩

theorem mutualism_finite : mutualism.Finite :=
  ⟨[.bee, .flower],
   ⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩,
   fun
    | .bee => .head _
    | .flower => .tail _ (.head _)⟩

/-- A finite world in which nothing arises or ceases and every event is living. -/
theorem mutualism_world :
    mutualism.Finite ∧ ¬ mutualism.ArisingRecurs ∧ ¬ mutualism.CeasingRecurs ∧
    mutualism.Living ∧ mutualism.Dependent ∧ mutualism.Embodied :=
  ⟨mutualism_finite, fun arising => match arising 0 with
    | ⟨_, _, _, arises⟩ => arises.1 trivial,
   fun ceasing => match ceasing 0 with
    | ⟨_, _, _, ceases⟩ => ceases.2 trivial,
   fun t x _ => (Mutualism.alive (x, t)).2, Mutualism.dependent, Mutualism.embodied⟩

/-- A parent drawing a pool down as it gives to two descendants (`Drawdown`). -/
def drawdown : World :=
  ⟨Drawdown.Relatum, Drawdown.flow, Drawdown.web⟩

instance drawdown_decided : ∀ t x, Decidable (drawdown.web.active t x)
  | _, .pool => isFalse id
  | t, .parent => Nat.decEq t 0
  | _, .same => isFalse id
  | t, .varied => Nat.decEq t 1

theorem drawdown_finite : drawdown.Finite :=
  ⟨[.pool, .parent, .same, .varied],
   ⟨fun mem => match mem with | .tail _ (.tail _ (.tail _ no)) => (nomatch no),
    fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
    fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩,
   fun
    | .pool => .head _
    | .parent => .tail _ (.head _)
    | .same => .tail _ (.tail _ (.head _))
    | .varied => .tail _ (.tail _ (.tail _ (.head _)))⟩

/-- After the first step nothing becomes active. -/
theorem drawdown_quiet : ∀ t x, 1 ≤ t → ¬ Drawdown.web.active (t + 1) x
  | _, .pool, _, active => active
  | t, .parent, _, active => Nat.not_succ_le_zero t (Nat.le_of_eq active)
  | _, .same, _, active => active
  | _, .varied, later, active =>
    Nat.not_succ_le_self 1 (Nat.le_trans (Nat.succ_le_succ later) (Nat.le_of_eq active))

/-- A finite world in which arising does not recur and not every event is living: the
parent's taking leaves the pool below its own need. The pool stands without being active,
so not every relatum is embodied. -/
theorem drawdown_world :
    drawdown.Finite ∧ ¬ drawdown.ArisingRecurs ∧ ¬ drawdown.CeasingRecurs ∧
    ¬ drawdown.Living ∧ drawdown.Dependent ∧ drawdown.Taking ∧ ¬ drawdown.Embodied :=
  have quiet : ¬ drawdown.ArisingRecurs := fun arising => match arising 1 with
    | ⟨t, x, later, arises⟩ => drawdown_quiet t x later arises.2
  ⟨drawdown_finite, quiet, fun ceasing => quiet ((arising_iff_ceasing drawdown_finite).mpr
     ceasing),
   fun living => living 0 .parent rfl ⟨.pool, ⟨rfl, Nat.zero_lt_one⟩, .parent,
     Nat.zero_lt_one, ⟨0, Nat.le_refl 0, fun _ _ _ => Nat.zero_lt_one, Nat.le_refl 2,
       Nat.lt_succ_self 1⟩, Nat.lt_succ_self 1⟩,
   Drawdown.dependent, Drawdown.taking,
   fun embodied => (embodied .pool 0).mpr (Nat.zero_lt_succ 1)⟩

/-- A parent active beyond its support (`Unchecked`). -/
def unchecked : World :=
  ⟨Unchecked.Relatum, Unchecked.flow, Unchecked.web⟩

/-- The sides of `Handing` with no flow: their standing comes and goes with nothing given
or taken. -/
def unbalanced : World :=
  ⟨Bool, Flow.still, Handing.web⟩

theorem unbalanced_world :
    unbalanced.Finite ∧ unbalanced.ArisingRecurs ∧ unbalanced.Dissipative ∧
    unbalanced.Embodied ∧ ¬ unbalanced.Balanced :=
  ⟨⟨[true, false], Handing.distinct, Handing.every⟩, handing_arising,
   Flow.still_dissipative, fun x => (Handing.embodied x).1,
   fun balanced => Nat.zero_ne_one (balanced 0 true)⟩

namespace Idle

/-- One relatum, never active, gives itself a unit across every step. -/
def flow : Flow Unit Unit :=
  ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 1⟩

/-- It stands at the number of steps so far. -/
def web : Web Unit Unit where
  level t _ := t
  active _ _ := False
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Idle

/-- A relatum rising by its own gift though it is never active. -/
def idle : World :=
  ⟨Unit, Idle.flow, Idle.web⟩

theorem idle_world : idle.Balanced ∧ ¬ idle.Acting :=
  ⟨fun _ _ => rfl, fun acting => acting 0 () () (.head _) Nat.zero_lt_one⟩

namespace Restless

/-- One relatum, active at every step, depending on itself at need one while it stands at
nothing. -/
def web : Web Unit Unit where
  level _ _ := 0
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := False

end Restless

/-- A relatum active beyond its support at every step. -/
def restless : World :=
  ⟨Unit, Flow.still, Restless.web⟩

/-- No reserve carries it: activity beyond support at every step outruns every reserve. -/
theorem restless_world : ¬ restless.Carried :=
  fun ⟨_, carries⟩ => carries.active_finitely (f := ()) (T := 0)
    (fun _ _ supported => Nat.not_succ_le_zero 0 (supported () trivial))
    fun N => ⟨N, Nat.le_refl N, trivial⟩

/-- Two sides handing a standing back and forth, burning fresh fuel each step
(`Kindling`). -/
def kindling : World :=
  ⟨Kindling.Relatum, Kindling.flow, Kindling.web⟩

instance kindling_decided : ∀ t x, Decidable (kindling.web.active t x)
  | t, .side x => Nat.decLt 0 (Handing.stands x t)
  | _, .fuel _ => isFalse id

theorem kindling_arising : kindling.ArisingEmbodied
  | _, .side x, _ => (Kindling.kindling.2.2.2.1 x).1
  | _, .fuel _, arises => False.elim arises.2

/-- Balanced and dissipative, whatever arises embodied, and arising recurs: so not
finite. -/
theorem kindling_world :
    kindling.Balanced ∧ kindling.Dissipative ∧ kindling.ArisingEmbodied ∧
    kindling.ArisingRecurs ∧ ¬ kindling.Finite :=
  have arising : kindling.ArisingRecurs := fun N =>
    match Kindling.kindling.2.2.2.2.2 true N with
    | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩
  ⟨Kindling.kindling.1, Kindling.kindling.2.2.2.2.1, kindling_arising, arising,
   fun finite => (rests finite Kindling.kindling.1 Kindling.kindling.2.2.2.2.1
     kindling_arising).1 arising⟩

/-- One relatum whose activity is not its standing (`Flicker`). -/
def flicker : World :=
  ⟨Unit, Flicker.flow, Flicker.web⟩

theorem flicker_world :
    flicker.Finite ∧ flicker.Balanced ∧ flicker.Dissipative ∧ flicker.ArisingRecurs ∧
    ¬ flicker.ArisingEmbodied :=
  ⟨⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun () => .head _⟩, Flicker.flicker.1,
   Flicker.flicker.2.1, Flicker.flicker.2.2.1,
   fun embodied => match Flicker.flicker.2.2.1 0 with
    | ⟨t, (), _, arises⟩ => Flicker.flicker.2.2.2 (embodied t () arises)⟩

/-- Formation `f` arises across step `f` and none ceases (`Dawn`). -/
def dawn : World :=
  ofRoles Flow.still Dawn.web

/-- Every formation is active from the start and formation `f` ceases across step `f`
(`Dusk`). -/
def dusk : World :=
  ofRoles Flow.still Dusk.web

instance dawn_decided : ∀ t x, Decidable (dawn.web.active t x)
  | t, .inl f => Nat.decLt f t
  | _, .inr _ => isFalse id

instance dusk_decided : ∀ t x, Decidable (dusk.web.active t x)
  | t, .inl f => Nat.decLe t f
  | _, .inr _ => isFalse id

namespace Grazing

/-- The two sides of `Handing`, a pool, a grazer and a browser. -/
inductive Relatum where
  | side (x : Bool)
  | pool
  | grazer
  | browser

def level : Nat → Relatum → Nat
  | t, .side y => Handing.stands y t
  | 0, .pool => 2
  | _ + 1, .pool => 1
  | _, .grazer => 1
  | _, .browser => 1

def active : Nat → Relatum → Prop
  | t, .side y => 0 < Handing.stands y t
  | _, .pool => False
  | t, .grazer => t = 0
  | t, .browser => t = 0

/-- Being the pool. -/
def isPool : Relatum → Prop
  | .side _ => False
  | .pool => True
  | .grazer => False
  | .browser => False

def requires : Nat → Relatum → Relatum → Prop
  | _, .side _, _ => False
  | _, .pool, _ => False
  | _, .grazer, c => isPool c
  | _, .browser, c => isPool c

def need : Nat → Relatum → Relatum → Nat
  | _, .side _, _ => 0
  | _, .pool, _ => 0
  | _, .grazer, _ => 1
  | _, .browser, _ => 2

/-- A side draws on its own standing while it stands. -/
def sideDraws (t : Nat) (y : Bool) : Relatum → Prop
  | .side z => z = y ∧ 0 < Handing.stands y t
  | .pool => False
  | .grazer => False
  | .browser => False

/-- The grazer draws on the pool at the first step. -/
def grazes (t : Nat) : Relatum → Prop
  | .side _ => False
  | .pool => t = 0
  | .grazer => False
  | .browser => False

def draws : Nat → Relatum → Relatum → Prop
  | t, .side y, c => sideDraws t y c
  | _, .pool, _ => False
  | t, .grazer, c => grazes t c
  | _, .browser, _ => False

/-- The sides hand a standing back and forth and draw on their own standing; the grazer
and the browser depend on the pool, at needs one and two, and are active at the first
step, when the grazer draws on the pool. -/
def web : Web Relatum Relatum :=
  ⟨level, active, requires, need, draws⟩

def present : Nat → List Relatum
  | 0 => [.side true, .grazer]
  | t + 1 => [.side (Handing.holder (t + 1))]

def sideTake (t : Nat) (x : Bool) : Relatum → Nat
  | .side y => Handing.flow.take t x y
  | .pool => 0
  | .grazer => 0
  | .browser => 0

def sideGive (t : Nat) (x : Bool) : Relatum → Nat
  | .side y => Handing.flow.give t x y
  | .pool => 0
  | .grazer => 0
  | .browser => 0

/-- A unit of the pool. -/
def poolUnit : Relatum → Nat
  | .side _ => 0
  | .pool => 1
  | .grazer => 0
  | .browser => 0

def take : Nat → Relatum → Relatum → Nat
  | t, .side x, c => sideTake t x c
  | _, .pool, _ => 0
  | _, .grazer, c => poolUnit c
  | _, .browser, _ => 0

def give : Nat → Relatum → Relatum → Nat
  | t, .side x, c => sideGive t x c
  | _, .pool, _ => 0
  | _, .grazer, _ => 0
  | _, .browser, _ => 0

/-- As in `Handing`, and across the first step the grazer takes a unit of the pool. -/
def flow : Flow Relatum Relatum :=
  ⟨present, take, give⟩

/-- Which side a side relatum is. -/
def sideOf : Relatum → Bool
  | .side x => x
  | .pool => false
  | .grazer => false
  | .browser => false

theorem sides_distinct : ¬ Relatum.side true ∈ [Relatum.side false] :=
  fun mem => (mem_cons_cases mem).elim
    (fun same => Bool.noConfusion (show true = false from congrArg sideOf same))
    (fun no => nomatch no)

theorem side_mem : ∀ x : Bool,
    Relatum.side x ∈ [.pool, .grazer, .browser, .side true, .side false]
  | true => .tail _ (.tail _ (.tail _ (.head _)))
  | false => .tail _ (.tail _ (.tail _ (.tail _ (.head _))))

theorem side_taking (t : Nat) (x : Bool) (holds : 0 < Handing.stands x t) :
    ∀ c, 0 < take t (.side x) c → active t (.side x) ∧ draws t (.side x) c
  | .side _, takes => match Spending.self_taken takes with
    | rfl => ⟨holds, rfl, holds⟩
  | .pool, takes => absurd takes (Nat.lt_irrefl 0)
  | .grazer, takes => absurd takes (Nat.lt_irrefl 0)
  | .browser, takes => absurd takes (Nat.lt_irrefl 0)

end Grazing

/-- The sides of `Handing`, with a grazer drawing down a pool that a browser also depends
on (the ninth review's probe). -/
def grazing : World :=
  ⟨Grazing.Relatum, Grazing.flow, Grazing.web⟩

theorem grazing_finite : grazing.Finite :=
  ⟨[.pool, .grazer, .browser, .side true, .side false],
   ⟨fun mem => match mem with | .tail _ (.tail _ (.tail _ (.tail _ no))) => (nomatch no),
    fun mem => match mem with | .tail _ (.tail _ (.tail _ no)) => (nomatch no),
    fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
    Grazing.sides_distinct,
    fun no => (nomatch no), trivial⟩,
   fun
    | .pool => .head _
    | .grazer => .tail _ (.head _)
    | .browser => .tail _ (.tail _ (.head _))
    | .side x => Grazing.side_mem x⟩

theorem grazing_arising : grazing.ArisingRecurs :=
  fun N => match Handing.recurs true N with
  | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩

theorem grazing_balanced : grazing.Balanced
  | 0, .side x => match x with
    | true => rfl
    | false => rfl
  | 0, .pool => rfl
  | 0, .grazer => rfl
  | 0, .browser => rfl
  | n + 1, .side y => Handing.balances (n + 1) y
  | _ + 1, .pool => rfl
  | _ + 1, .grazer => rfl
  | _ + 1, .browser => rfl

theorem grazing_acting : grazing.Acting
  | 0, _, _, .head _, _ => Nat.zero_lt_one
  | 0, _, _, .tail _ (.head _), gives => absurd gives (Nat.lt_irrefl 0)
  | 0, _, _, .tail _ (.tail _ rest), _ => nomatch rest
  | n + 1, _, _, .head _, _ => Handing.holder_stands (n + 1)
  | _ + 1, _, _, .tail _ rest, _ => nomatch rest

theorem grazing_taking : grazing.Taking
  | 0, _, c, .head _, takes => Grazing.side_taking 0 true Nat.zero_lt_one c takes
  | 0, _, c, .tail _ (.head _), takes => match c, takes with
    | .pool, _ => ⟨rfl, rfl⟩
    | .side _, takes => absurd takes (Nat.lt_irrefl 0)
    | .grazer, takes => absurd takes (Nat.lt_irrefl 0)
    | .browser, takes => absurd takes (Nat.lt_irrefl 0)
  | 0, _, _, .tail _ (.tail _ rest), _ => nomatch rest
  | n + 1, _, c, .head _, takes =>
    Grazing.side_taking (n + 1) (Handing.holder (n + 1)) (Handing.holder_stands (n + 1)) c takes
  | _ + 1, _, _, .tail _ rest, _ => nomatch rest

theorem grazing_dependent : grazing.Dependent
  | _, .side _, _ => fun _ no => False.elim no
  | _, .pool, active => False.elim active
  | _, .grazer, rfl => fun c depends => match c, depends with
    | .pool, _ => Nat.le_succ 1
    | .side _, no => False.elim no
    | .grazer, no => False.elim no
    | .browser, no => False.elim no
  | _, .browser, rfl => fun c depends => match c, depends with
    | .pool, _ => Nat.le_refl 2
    | .side _, no => False.elim no
    | .grazer, no => False.elim no
    | .browser, no => False.elim no

/-- The grazer draws only on the pool, the pool is never active, and the grazer's own
dependence is still met after the step. -/
theorem grazing_not_self :
    (∀ t c, Grazing.web.draws t .grazer c → c = .pool) ∧
    (∀ t, ¬ Grazing.web.active t .pool) ∧
    Grazing.web.need 0 .grazer .pool ≤ Grazing.web.level 1 .pool :=
  ⟨fun _ c drawn => match c, drawn with
    | .pool, _ => rfl
    | .side _, no => False.elim no
    | .grazer, no => False.elim no
    | .browser, no => False.elim no,
   fun _ active => active, Nat.le_refl 1⟩

/-- A finite world in which arising recurs and not every event is living, whatever is
chosen about drawing at an ending: the grazer's event at the first step undermines the
browser's dependence on the pool, which is not the drawer and never active. Activity needs
support, the flow balances, and only active relata give, and take only what they draw
on. -/
theorem grazing_world :
    grazing.Finite ∧ grazing.ArisingRecurs ∧ ¬ grazing.Living ∧ grazing.Dependent ∧
    grazing.Balanced ∧ grazing.Acting ∧ grazing.Taking :=
  ⟨grazing_finite, grazing_arising,
   fun living => living 0 .grazer rfl
    ⟨.pool, rfl, .browser, trivial,
     ⟨0, Nat.le_refl 0, fun _ _ _ => trivial, Nat.le_refl 2, Nat.lt_succ_self 1⟩,
     Nat.lt_succ_self 1⟩,
   grazing_dependent, grazing_balanced, grazing_acting, grazing_taking⟩

namespace Leaking

/-- Across each step the holder takes its own unit and gives nothing. -/
def flow : Flow Bool Bool :=
  ⟨fun t => [Handing.holder t], fun t x y => Handing.flow.take t x y, fun _ _ _ => 0⟩

theorem takes : ∀ t, 0 < total [true, false] (flow.take t (Handing.holder t))
  | 0 => Nat.zero_lt_one
  | 1 => Nat.zero_lt_one
  | t + 2 => takes t

end Leaking

/-- The sides of `Handing`, the holder taking its own unit and giving nothing (the ninth
review's probe). -/
def leaking : World :=
  ⟨Bool, Leaking.flow, Handing.web⟩

/-- A finite world whose flow takes part at every step, with the family of both sides
closed and taken from at every step, and dissipative: its dissipation is not vacuous.
Every relatum is embodied and arising recurs; only balance fails. -/
theorem leaking_world :
    leaking.Finite ∧ leaking.ArisingRecurs ∧ leaking.Dissipative ∧ leaking.Embodied ∧
    ¬ leaking.Balanced ∧
    ∀ t, Leaking.flow.ClosedAt [true, false] t ∧
      0 < total [true, false] (Leaking.flow.take t (Handing.holder t)) :=
  ⟨⟨[true, false], Handing.distinct, Handing.every⟩, handing_arising,
   fun cs _ _ _ _ _ => Nat.le_trans
     (Nat.le_of_eq ((congrArg (· + _) (total_zero cs)).trans (Nat.zero_add _))) (sign_le _),
   fun x => (Handing.embodied x).1,
   fun balanced => Nat.not_succ_le_zero 0 (Nat.le_of_eq (balanced 0 false)),
   fun t => ⟨fun _ _ c outside => absurd (Handing.every c) outside, Leaking.takes t⟩⟩

namespace Undecided

/-- Period four: inactive, active, `Q`, inactive. -/
def act (Q : Prop) : Nat → Prop
  | 0 => False
  | 1 => True
  | 2 => Q
  | 3 => False
  | n + 4 => act Q n

/-- The starts of the periods. -/
def four : Nat → Nat
  | 0 => 0
  | n + 1 => four n + 4

theorem le_four : ∀ N, N ≤ four N
  | 0 => Nat.le_refl 0
  | N + 1 => Nat.add_le_add (le_four N) (Nat.le_add_left 1 3)

theorem arises_at (Q : Prop) : ∀ N, ¬ act Q (four N) ∧ act Q (four N + 1)
  | 0 => ⟨id, trivial⟩
  | N + 1 => arises_at Q N

/-- One relatum, standing at nothing, depending on nothing, active with period four. -/
def web (Q : Prop) : Web Unit Unit where
  level _ _ := 0
  active t _ := act Q t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Any ceasing decides `Q`. -/
theorem decides (Q : Prop) : ∀ t, act Q t → ¬ act Q (t + 1) → Q ∨ ¬ Q
  | 0, active, _ => False.elim active
  | 1, _, inactive => Or.inr inactive
  | 2, active, _ => Or.inl active
  | 3, active, _ => False.elim active
  | n + 4, active, inactive => decides Q n active inactive

end Undecided

/-- One relatum with no flow, whose activity of period four has `Q` as its third phase
(the ninth review's probe). -/
def undecided (Q : Prop) : World :=
  ⟨Unit, Flow.still, Undecided.web Q⟩

/-- It is finite, and arising recurs whatever `Q` is: it arises at the start of every
period. -/
theorem undecided_world (Q : Prop) : (undecided Q).Finite ∧ (undecided Q).ArisingRecurs :=
  ⟨⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun () => .head _⟩,
   fun N => ⟨Undecided.four N, (), Undecided.le_four N, Undecided.arises_at Q N⟩⟩

/-- Without decidability the finite-world law is excluded middle: if in every finite world
in which arising recurs ceasing also recurs, every proposition is decided. So
`arising_iff_ceasing` needs its decidability, which classically always holds and is a
logical commitment of the representation, not a premise about any unfolding. -/
theorem law_decides (law : ∀ w : World, w.Finite → w.ArisingRecurs → w.CeasingRecurs)
    (Q : Prop) : Q ∨ ¬ Q :=
  match law (undecided Q) (undecided_world Q).1 (undecided_world Q).2 0 with
  | ⟨t, (), _, active, inactive⟩ => Undecided.decides Q t active inactive

/-! ## The parts -/

/-- Each premise is met by some worlds and not by others. -/
theorem contingent :
    (handing.Dependent ∧ ¬ unchecked.Dependent) ∧
    (handing.Balanced ∧ ¬ unbalanced.Balanced) ∧
    (handing.Acting ∧ ¬ idle.Acting) ∧
    (spending.Taking ∧ ¬ handing.Taking) ∧
    (kindling.Dissipative ∧ ¬ handing.Dissipative) ∧
    (handing.Embodied ∧ ¬ drawdown.Embodied) ∧
    (handing.Carried ∧ ¬ restless.Carried) :=
  ⟨⟨Handing.dependent, Unchecked.unchecked.2.2.2.2.1⟩,
   ⟨Handing.balances, unbalanced_world.2.2.2.2⟩,
   ⟨Handing.acting, idle_world.2⟩,
   ⟨Spending.taking, handing_world.2.2.2.2.2.2.2.1⟩,
   ⟨kindling_world.2.1, handing_world.2.2.2.2.2.2.2.2.1⟩,
   ⟨handing_world.2.2.2.2.2.2.2.2.2.1, drawdown_world.2.2.2.2.2.2⟩,
   ⟨handing_world.2.2.2.2.2.2.2.2.2.2, restless_world⟩⟩

/-- Where the relata are infinitely many, arising and ceasing separate: either recurs
without the other. -/
theorem separate :
    (dawn.ArisingRecurs ∧ ¬ dawn.CeasingRecurs ∧ ¬ dawn.Finite) ∧
    (dusk.CeasingRecurs ∧ ¬ dusk.ArisingRecurs ∧ ¬ dusk.Finite) :=
  have dawnArising : dawn.ArisingRecurs := (arisingRecurs_ofRoles _ _).mpr Dawn.unceasing
  have dawnQuiet : ¬ dawn.CeasingRecurs := fun ceasing =>
    match (ceasingRecurs_ofRoles _ _).mp ceasing 0 with
    | ⟨t, f, _, ceases⟩ => Dawn.never_ceases t f ceases
  have duskCeasing : dusk.CeasingRecurs := (ceasingRecurs_ofRoles _ _).mpr Dusk.ceasing
  have duskQuiet : ¬ dusk.ArisingRecurs := fun arising =>
    match (arisingRecurs_ofRoles _ _).mp arising 0 with
    | ⟨t, f, _, arises⟩ => Dusk.nothing_arises t f arises
  ⟨⟨dawnArising, dawnQuiet,
    fun finite => dawnQuiet ((arising_iff_ceasing finite).mp dawnArising)⟩,
   ⟨duskCeasing, duskQuiet,
    fun finite => duskQuiet ((arising_iff_ceasing finite).mpr duskCeasing)⟩⟩

/-- Living crosses arising: among finite worlds, arising recurring or not occurs both with
every event living and with some event not living. In a finite world whose activity is
decided, ceasing recurs exactly when arising does, so the same holds of it. -/
theorem living_crosses :
    (handing.Finite ∧ handing.ArisingRecurs ∧ handing.Living) ∧
    (grazing.Finite ∧ grazing.ArisingRecurs ∧ ¬ grazing.Living) ∧
    (mutualism.Finite ∧ ¬ mutualism.ArisingRecurs ∧ mutualism.Living) ∧
    (drawdown.Finite ∧ ¬ drawdown.ArisingRecurs ∧ ¬ drawdown.Living) :=
  ⟨⟨handing_finite, handing_arising, handing_world.2.2.2.1⟩,
   ⟨grazing_finite, grazing_arising, grazing_world.2.2.1⟩,
   ⟨mutualism_finite, mutualism_world.2.1, mutualism_world.2.2.2.1⟩,
   ⟨drawdown_finite, drawdown_world.2.1, drawdown_world.2.2.2.1⟩⟩

/-- Each premise of `rests` is needed: without finiteness, dissipation, balance or
embodiment, arising can recur. The world failing balance takes part in exchange at every
step, so its dissipation is not vacuous. -/
theorem rests_needs :
    (kindling.Balanced ∧ kindling.Dissipative ∧ kindling.ArisingEmbodied ∧
      kindling.ArisingRecurs ∧ ¬ kindling.Finite) ∧
    (handing.Finite ∧ handing.Balanced ∧ handing.ArisingEmbodied ∧ handing.ArisingRecurs ∧
      ¬ handing.Dissipative) ∧
    (leaking.Finite ∧ leaking.Dissipative ∧ leaking.ArisingEmbodied ∧
      leaking.ArisingRecurs ∧ ¬ leaking.Balanced) ∧
    (flicker.Finite ∧ flicker.Balanced ∧ flicker.Dissipative ∧ flicker.ArisingRecurs ∧
      ¬ flicker.ArisingEmbodied) :=
  ⟨kindling_world,
   ⟨handing_finite, Handing.balances, Embodied.arising handing_world.2.2.2.2.2.2.2.2.2.1,
    handing_arising, handing_world.2.2.2.2.2.2.2.2.1⟩,
   ⟨leaking_world.1, leaking_world.2.2.1, Embodied.arising leaking_world.2.2.2.1,
    leaking_world.2.1, leaking_world.2.2.2.2.1⟩,
   flicker_world⟩

end World

end Becoming
